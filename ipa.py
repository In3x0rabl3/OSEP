#!/usr/bin/env python3
import json
import ssl
import sys
import http.client

IPA_ENDPOINT = "/ipa/session/json"
COOKIE = None

###############################################################################
# JSON-RPC WRAPPER
###############################################################################

def rpc(host, method, params=None):
    """
    Send JSON-RPC request to FreeIPA.
    Always returns a dictionary, even on errors.
    """
    global COOKIE

    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://{host}/ipa"
    }

    if COOKIE:
        headers["Cookie"] = COOKIE

    payload = json.dumps({
        "method": method,
        "params": params if params else [[], {}]
    })

    ctx = ssl._create_unverified_context()
    conn = http.client.HTTPSConnection(host, context=ctx)
    conn.request("POST", IPA_ENDPOINT, payload, headers)

    res = conn.getresponse()
    set_cookie = res.getheader("Set-Cookie")
    if set_cookie:
        COOKIE = set_cookie.split(";", 1)[0]

    try:
        data = res.read().decode()
        conn.close()
    except:
        conn.close()
        return {"error": "failed_read"}

    try:
        return json.loads(data)
    except:
        return {"error": "invalid_json", "raw": data}


###############################################################################
# LOGIN
###############################################################################

def login(host, username, password):
    """Password auth via FreeIPA login session."""
    global COOKIE

    ctx = ssl._create_unverified_context()
    conn = http.client.HTTPSConnection(host, context=ctx)

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"https://{host}/ipa"
    }

    body = f"user={username}&password={password}"

    conn.request("POST", "/ipa/session/login_password", body, headers)
    res = conn.getresponse()

    if res.status != 200:
        print("[!] Authentication failed")
        sys.exit(1)

    COOKIE = res.getheader("Set-Cookie").split(";", 1)[0]
    conn.close()
    print("[+] Authenticated")


###############################################################################
# SAFE FIND (FIXED)
###############################################################################

def safe_find(host, method):
    """
    Calls an IPA *_find method and ALWAYS returns a list.
    Never crashes, even when:
    - plugin is disabled
    - API unsupported
    - empty results
    - "result" is null
    - RPC returns an error block
    """
    res = rpc(host, method, [[], {"all": True}])

    if not isinstance(res, dict):
        return []

    if "error" in res:
        return []

    if "result" not in res:
        return []

    if res["result"] is None:
        return []

    result_block = res["result"]
    if not isinstance(result_block, dict):
        return []

    items = result_block.get("result", [])
    if isinstance(items, list):
        return items

    return []


###############################################################################
# ENUMERATION
###############################################################################

def gather_data(host):
    print("[*] Enumerating FreeIPA objects...")

    data = {}

    # env usually always works
    env = rpc(host, "env")
    data["env"] = env.get("result", {})

    data["users"] = safe_find(host, "user_find")
    data["groups"] = safe_find(host, "group_find")
    data["roles"] = safe_find(host, "role_find")
    data["privileges"] = safe_find(host, "privilege_find")
    data["permissions"] = safe_find(host, "permission_find")
    data["sudorules"] = safe_find(host, "sudorule_find")
    data["hbacrules"] = safe_find(host, "hbacrule_find")
    data["hosts"] = safe_find(host, "host_find")
    data["dnszones"] = safe_find(host, "dnszone_find")
    data["pwpolicy"] = safe_find(host, "pwpolicy_find")

    # DNS records per zone (ignore failures)
    for z in data["dnszones"]:
        if "idnsname" in z:
            zone = z["idnsname"][0]
            recs = rpc(host, "dnsrecord_find", [[zone], {"all": True}])
            if "result" in recs and recs["result"] and isinstance(recs["result"], dict):
                z["records"] = recs["result"].get("result", [])

    return data


###############################################################################
# FAST MODE FINDINGS
###############################################################################

def fast_findings(data):
    findings = []

    # Weak password policies
    for pp in data.get("pwpolicy", []):
        maxlife = None
        minlength = None

        if "krbmaxpwdlife" in pp and isinstance(pp["krbmaxpwdlife"], list):
            try:
                maxlife = int(pp["krbmaxpwdlife"][0])
            except:
                pass

        if "krbpwdminlength" in pp and isinstance(pp["krbpwdminlength"], list):
            try:
                minlength = int(pp["krbpwdminlength"][0])
            except:
                pass

        if maxlife and maxlife > 30:
            findings.append("[!] Weak password policy: password lifetime > 30 days")

        if minlength and minlength < 10:
            findings.append("[!] Weak password policy: minimum length < 10")

    # Users with no 2FA
    for u in data["users"]:
        uname = u.get("uid", ["?"])[0]
        if "ipauserauthtype" not in u:
            findings.append(f"[!] User {uname} has no 2FA configured")

    # HBAC too broad
    for h in data["hbacrules"]:
        name = h.get("cn", ["?"])[0]
        # If no user restriction + no service restriction
        if "memberuser_user" not in h and "hbacsvc" not in h:
            findings.append(f"[!] HBAC '{name}' may allow broad access")

    # SUDO ANYCMD
    for s in data["sudorules"]:
        sname = s.get("cn", ["?"])[0]
        cmds = s.get("sudoallowcommand", [])
        if any("ALL" in c.upper() for c in cmds):
            findings.append(f"[CRITICAL] Sudo rule '{sname}' allows ALL commands")

    # DNS wildcard
    for z in data["dnszones"]:
        zname = z.get("idnsname", ["?"])[0]
        for rec in z.get("records", []):
            rname = rec.get("idnsname", ["?"])[0]
            if rname == "*" or rname.lower() == "wildcard":
                findings.append(f"[!] Wildcard DNS entry detected in zone '{zname}'")

    return findings


###############################################################################
# DEEP ATTACK PATH ENGINE
###############################################################################

def deep_attack_paths(data):
    """BloodHound-style multi-hop privilege path detection."""

    def get_name(obj, key="cn", alt="uid"):
        if key in obj:
            return obj[key][0]
        if alt in obj:
            return obj[alt][0]
        return "?"

    # Build name maps
    users = {get_name(u, "uid"): u for u in data["users"]}
    roles = {get_name(r): r for r in data["roles"]}
    privileges = {get_name(p): p for p in data["privileges"]}
    permissions = {get_name(p): p for p in data["permissions"]}

    edges = []

    # User → Group
    for uname, u in users.items():
        for g in u.get("memberof_group", []):
            edges.append((uname, "member_of_group", g))

    # Group → Role
    for rname, r in roles.items():
        for g in r.get("member_group", []):
            edges.append((g, "grants_role", rname))

    # Role → Privilege
    for pname, p in privileges.items():
        for r in p.get("memberof_role", []):
            edges.append((r, "grants_privilege", pname))

    # Privilege → Permission
    for permname, perm in permissions.items():
        for p in perm.get("memberof_privilege", []):
            edges.append((p, "grants_permission", permname))

    # Permission → Capabilities
    for permname, perm in permissions.items():
        rights = perm.get("ipapermright", [])
        locs = perm.get("ipapermlocation", [])

        if "write" in rights:
            if any("host" in l for l in locs):
                edges.append((permname, "can_modify_hosts", "HOST_WRITE"))

        if any("hbac" in l for l in locs):
            edges.append((permname, "modify_hbac", "HBAC_RULES"))

        if any("sudo" in l for l in locs):
            edges.append((permname, "modify_sudo", "SUDO_RULES"))

    TARGETS = ["can_modify_hosts", "modify_hbac", "modify_sudo"]

    def dfs(start, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(start)

        for src, rel, dst in edges:
            if src != start:
                continue

            new_path = path + [(src, rel, dst)]

            if rel in TARGETS:
                yield new_path

            if dst not in visited:
                yield from dfs(dst, visited, new_path)

    attack_paths = []
    for user in users:
        for p in dfs(user):
            attack_paths.append(p)

    return attack_paths


###############################################################################
# MAIN
###############################################################################

def main():
    if len(sys.argv) != 5:
        print("Usage: freeipa_attack_paths.py <host> <user> <password> <mode>")
        print("Modes: fast | deep")
        sys.exit(1)

    host = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    mode = sys.argv[4]

    login(host, username, password)
    data = gather_data(host)

    if mode == "fast":
        print("\n=== FAST MODE FINDINGS ===\n")
        f = fast_findings(data)
        if not f:
            print("No immediate misconfigurations found.")
            return
        for x in f:
            print(x)

    elif mode == "deep":
        print("\n=== DEEP ATTACK PATHS ===\n")
        paths = deep_attack_paths(data)
        if not paths:
            print("No multi-hop attack paths found.")
            return

        for p in paths:
            print("\n[ATTACK PATH]")
            for src, rel, dst in p:
                print(f"  {src} --{rel}--> {dst}")

    else:
        print("Invalid mode. Use fast or deep.")


if __name__ == "__main__":
    main()
