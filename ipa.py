#!/usr/bin/env python3
import json
import ssl
import sys
import http.client
import time

COOKIE = None
IPA_JSON = "/ipa/session/json"

###########################################################################
# CONFIG
###########################################################################

DEBUG = True   # Set to False to silence debug output

###########################################################################
# HTTP / JSON-RPC HELPERS
###########################################################################

def log(msg):
    if DEBUG:
        print(f"[DEBUG] {msg}")

def rpc(host, method, params=None):
    """
    Send a JSON-RPC request to FreeIPA.
    ALWAYS returns a dict, even on error.
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

    try:
        conn = http.client.HTTPSConnection(host, context=ctx, timeout=5)
        conn.request("POST", IPA_JSON, payload, headers)
        res = conn.getresponse()
        raw = res.read().decode()
        conn.close()
    except Exception as e:
        log(f"RPC network error calling {method}: {e}")
        return {"error": "network"}

    # capture cookie
    set_cookie = res.getheader("Set-Cookie")
    if set_cookie:
        COOKIE = set_cookie.split(";", 1)[0]

    try:
        parsed = json.loads(raw)
        log(f"RPC {method} returned keys: {list(parsed.keys())}")
        return parsed
    except:
        log(f"RPC {method} returned non-JSON: {raw[:200]}")
        return {"error": "invalid_json", "raw": raw}


###########################################################################
# LOGIN
###########################################################################

def login(host, username, password):
    """
    Perform password-based login to FreeIPA UI backend.
    """
    global COOKIE

    ctx = ssl._create_unverified_context()
    conn = http.client.HTTPSConnection(host, context=ctx)

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"https://{host}/ipa"
    }

    body = f"user={username}&password={password}"

    try:
        conn.request("POST", "/ipa/session/login_password", body, headers)
        res = conn.getresponse()
    except Exception as e:
        print(f"[!] Login connection error: {e}")
        sys.exit(1)

    if res.status != 200:
        print("[!] Login failed")
        sys.exit(1)

    COOKIE = res.getheader("Set-Cookie").split(";", 1)[0]
    conn.close()
    print("[+] Authenticated")


###########################################################################
# SAFE FIND HELPER
###########################################################################

def safe_rpc_list(host, method):
    """
    Calls a *_find method safely and returns a list.
    Never throws, never crashes.
    """
    log(f"Calling {method} ...")
    res = rpc(host, method, [[], {"all": True}])

    if not isinstance(res, dict):
        log(f"{method} returned non-dict")
        return []

    if "error" in res:
        log(f"{method} returned error")
        return []

    if "result" not in res:
        log(f"{method} missing result block")
        return []

    r = res["result"]

    if r is None or not isinstance(r, dict):
        log(f"{method} returned null result block")
        return []

    items = r.get("result", [])
    if isinstance(items, list):
        log(f"{method} returned list length: {len(items)}")
        return items

    log(f"{method} result block has no list")
    return []


###########################################################################
# ENUMERATION PHASE
###########################################################################

def enumerate_lowpriv_data(host):
    """
    Enumerates EVERYTHING a low-priv FreeIPA user can possibly see.
    """
    data = {}

    # Always works: env
    log("Fetching env ...")
    env_res = rpc(host, "env")
    data["env"] = env_res.get("result", {})
    log(f"env keys: {list(data['env'].keys())}")

    # User listing
    data["users"] = safe_rpc_list(host, "user_find")

    # Group listing
    data["groups"] = safe_rpc_list(host, "group_find")

    # Host listing (may fail silently)
    data["hosts"] = safe_rpc_list(host, "host_find")

    # Password policy (often visible to everyone)
    data["pwpolicy"] = safe_rpc_list(host, "pwpolicy_find")

    # DNS (usually blocked for low-priv)
    data["dns"] = safe_rpc_list(host, "dnszone_find")

    return data


###########################################################################
# FAST FINDINGS
###########################################################################

def fast_findings(data):
    findings = []

    users = data.get("users", [])
    groups = data.get("groups", [])
    hosts = data.get("hosts", [])
    pwpol = data.get("pwpolicy", [])

    # Can see all users = major information disclosure
    if len(users) > 1:
        findings.append("[!] Low-priv user can enumerate ALL users (usernames harvested)")

    # Can see groups
    if len(groups) > 0:
        findings.append("[!] Low-priv user can enumerate ALL groups (RBAC exposure)")

    # Can see hosts
    if len(hosts) > 0:
        findings.append("[!] Low-priv user can enumerate hosts (infrastructure recon)")

    # Password policy weaknesses
    for pp in pwpol:
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
            findings.append("[!] Weak password lifetime (>30 days) → spraying viable")

        if minlength and minlength < 10:
            findings.append("[!] Weak min password length (<10)")

    return findings


###########################################################################
# ATTACK PATH ANALYSIS (LOW PRIV VERSION)
###########################################################################

def build_attack_paths(data):
    """
    A low-priv user usually cannot see roles/privileges,
    so we infer:
    - user -> group
    - group -> nested group (if any)
    - privileged groups by name heuristic
    """
    users = data.get("users", [])
    groups = data.get("groups", [])

    G = []

    # Identify privileged groups by name heuristic
    priv_group_keywords = ["admin", "sudo", "wheel", "ops", "security"]

    priv_groups = []
    for g in groups:
        name = g.get("cn", ["?"])[0].lower()
        if any(k in name for k in priv_group_keywords):
            priv_groups.append(name)

    # Build edges user -> groups
    for u in users:
        uname = u.get("uid", ["?"])[0]
        memberof = u.get("memberof_group", [])
        for mg in memberof:
            G.append((uname, "member_of", mg))

    # Nested groups
    for g in groups:
        gname = g.get("cn", ["?"])[0]
        if "member_group" in g:
            for ng in g["member_group"]:
                G.append((gname, "nested_group", ng))

    # Detect attack paths: user → group → privileged group
    paths = []
    for (a, rel, b) in G:
        if b.lower() in priv_groups:
            paths.append([(a, rel, b)])

    return paths


###########################################################################
# MAIN
###########################################################################

def main():
    if len(sys.argv) != 4:
        print("Usage: freeipa_lowpriv_enum.py <host> <user> <password>")
        sys.exit(1)

    host = sys.argv[1]
    user = sys.argv[2]
    password = sys.argv[3]

    login(host, user, password)

    print("[*] Running low-priv FreeIPA enumeration...")
    data = enumerate_lowpriv_data(host)

    print("\n=== DEBUG SUMMARY ===")
    for k in data:
        print(f"{k}: {len(data[k]) if isinstance(data[k], list) else 'OK'}")

    print("\n=== FAST FINDINGS ===")
    ff = fast_findings(data)
    if not ff:
        print("No simple misconfigurations detected.")
    else:
        for f in ff:
            print(f)

    print("\n=== ATTACK PATHS (INFERRED) ===")
    paths = build_attack_paths(data)
    if not paths:
        print("No obvious privilege paths found.")
    else:
        for p in paths:
            print("\n[ATTACK PATH]")
            for step in p:
                a, rel, b = step
                print(f"  {a} --{rel}--> {b}")


if __name__ == "__main__":
    main()
