#!/usr/bin/env python3
import json
import ssl
import sys
import http.client

IPA_ENDPOINT = "/ipa/session/json"
COOKIE = None

###############################################################################
#                           JSON-RPC WRAPPER
###############################################################################

def rpc(host, method, params=None):
    """Send a JSON-RPC request to FreeIPA."""
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

    data = res.read().decode()
    conn.close()

    try:
        return json.loads(data)
    except:
        return {"error": "Invalid JSON", "raw": data}

###############################################################################
#                               LOGIN
###############################################################################

def login(host, username, password):
    """Password authentication using FreeIPA login session."""
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
#                       ENUMERATION HELPERS
###############################################################################

def safe_find(host, method):
    """Call find method but safely handle missing capability."""
    res = rpc(host, method, [[], {"all": True}])
    if "result" not in res:
        return []
    return res["result"].get("result", []) or []


def gather_data(host):
    """Collect all IPA objects that are relevant for attack-path generation."""
    data = {}

    data["env"] = rpc(host, "env").get("result", {})
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

    # DNS records per zone
    zones = []
    for z in data["dnszones"]:
        if "idnsname" in z:
            zone = z["idnsname"][0]
            recs = rpc(host, "dnsrecord_find", [[zone], {"all": True}])
            if "result" in recs:
                z["records"] = recs["result"].get("result", [])

    return data

###############################################################################
#                       FAST MODE (Simple Findings)
###############################################################################

def fast_findings(data):
    """Print quick red-team actionable findings."""
    findings = []

    # Weak password policy
    for pp in data["pwpolicy"]:
        if "krbmaxpwdlife" in pp and int(pp["krbmaxpwdlife"][0]) > 30:
            findings.append("[!] Weak password policy: password life > 30 days (spray viable)")
        if "krbpwdminlength" in pp and int(pp["krbpwdminlength"][0]) < 10:
            findings.append("[!] Weak password policy: minimum length < 10")

    # Users missing 2FA
    for u in data["users"]:
        if "uid" in u and "ipauserauthtype" not in u:
            findings.append(f"[!] User {u['uid'][0]} has no 2FA — credential reuse & phishing viable")

    # HBAC ANYHOST rule
    for h in data["hbacrules"]:
        if "hbacsvc" not in h and "memberuser_user" not in h:
            findings.append(f"[!] HBAC rule '{h.get('cn',[\"?\"])[0]}' may allow broad access")

    # SUDO ANYCMD
    for s in data["sudorules"]:
        if "sudoallowcommand" in s:
            cmds = s["sudoallowcommand"]
            if any("ALL" in c.upper() for c in cmds):
                rulename = s["cn"][0]
                findings.append(f"[CRITICAL] Sudo rule '{rulename}' allows ALL commands — root escalation path")

    # DNS wildcard
    for z in data["dnszones"]:
        for rec in z.get("records", []):
            if "idnsname" in rec and rec["idnsname"][0] in ["*", "wildcard"]:
                findings.append(f"[!] Wildcard DNS record in zone {z['idnsname'][0]} — phishing/subdomain takeover")

    return findings

###############################################################################
#                          DEEP MODE ATTACK PATHS
###############################################################################

def deep_attack_paths(data):
    """
    Build a directed graph of:
    user → group → role → privilege → permission → (access)
    and locate chained escalation or domain takeover paths.
    """

    def get_name(obj, key="cn"):
        return obj.get(key, obj.get("uid", ["?"]))[0]

    users = {get_name(u, "uid"): u for u in data["users"]}
    groups = {get_name(g): g for g in data["groups"]}
    roles = {get_name(r): r for r in data["roles"]}
    privileges = {get_name(p): p for p in data["privileges"]}
    permissions = {get_name(p): p for p in data["permissions"]}

    edges = []  # list of (src, relation, dst)

    # User → Groups
    for u_name, u in users.items():
        for g in u.get("memberof_group", []):
            edges.append((u_name, "member_of_group", g))

    # Groups → Roles
    for r_name, r in roles.items():
        for g in r.get("member_group", []):
            edges.append((g, "grants_role", r_name))

    # Roles → Privileges
    for p_name, p in privileges.items():
        for r in p.get("memberof_role", []):
            edges.append((r, "grants_privilege", p_name))

    # Privileges → Permissions
    for perm_name, perm in permissions.items():
        for p in perm.get("memberof_privilege", []):
            edges.append((p, "grants_permission", perm_name))

    # Permissions → capabilities
    for perm_name, perm in permissions.items():
        # Write access to hosts
        if "ipapermright" in perm and "write" in perm["ipapermright"]:
            if "ipapermtarget" in perm:
                tgt = perm["ipapermtarget"][0]
                if "host" in tgt:
                    edges.append((perm_name, "can_modify_hosts", tgt))

        # Modify HBAC rules
        if "ipapermlocation" in perm and "hbac" in perm["ipapermlocation"][0]:
            edges.append((perm_name, "modify_hbac", "HBAC_RULES"))

        # Modify Sudo rules
        if "ipapermlocation" in perm and "sudo" in perm["ipapermlocation"][0]:
            edges.append((perm_name, "modify_sudo", "SUDO_RULES"))

    ###########################################################################
    # PATH SEARCH
    ###########################################################################
    def dfs(start, target_keywords, visited=None, path=None):
        if visited is None: visited = set()
        if path is None: path = []

        visited.add(start)

        for (src, rel, dst) in edges:
            if src != start:
                continue

            new_path = path + [(src, rel, dst)]

            # If destination is a target privilege/capability
            if any(k in rel or (isinstance(dst, str) and k in dst) for k in target_keywords):
                yield new_path

            if dst not in visited:
                yield from dfs(dst, target_keywords, visited, new_path)

    ###########################################################################
    # ATTACK PATH ANALYSIS
    ###########################################################################

    attack_paths = []

    TARGETS = ["can_modify_hosts", "modify_hbac", "modify_sudo"]

    for user in users:
        for path in dfs(user, TARGETS):
            attack_paths.append(path)

    return attack_paths


###############################################################################
#                               MAIN
###############################################################################

def main():
    if len(sys.argv) != 5:
        print("Usage: freeipa_attack_paths.py <host> <user> <password> <mode>")
        print("Modes: fast | deep")
        sys.exit(1)

    host = sys.argv[1]
    user = sys.argv[2]
    pw = sys.argv[3]
    mode = sys.argv[4]

    login(host, user, pw)
    data = gather_data(host)

    if mode == "fast":
        print("\n=== FAST MODE FINDINGS ===\n")
        findings = fast_findings(data)
        if not findings:
            print("No obvious misconfigurations found.")
        else:
            for f in findings:
                print(f)

    elif mode == "deep":
        print("\n=== DEEP ATTACK PATH MODE ===\n")
        paths = deep_attack_paths(data)
        if not paths:
            print("No multi-hop attack paths found.")
        else:
            for p in paths:
                print("\n[ATTACK PATH]")
                for (src, rel, dst) in p:
                    print(f"  {src} --{rel}--> {dst}")

    else:
        print("Invalid mode. Use fast or deep.")


if __name__ == "__main__":
    main()
