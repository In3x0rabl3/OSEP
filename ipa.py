#!/usr/bin/env python3
import http.client
import json
import ssl
import sys

IPA_ENDPOINT = "/ipa/session/json"
COOKIE = None
DEBUG = True

# GLOBAL LOOKUP TABLES
GLOBAL_USERS = []
GLOBAL_HOSTS = []

def debug(msg):
    if DEBUG:
        print(f"[DEBUG] {msg}")

###############################################################################
# RPC HELPER
###############################################################################

def request(host, method, params=None):
    global COOKIE
    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://{host}/ipa",
    }
    if COOKIE:
        headers["Cookie"] = COOKIE

    payload = json.dumps({
        "method": method,
        "params": params or [[], {"all": True}],
    })

    ctx = ssl._create_unverified_context()
    debug(f"--> RPC {method}")

    try:
        conn = http.client.HTTPSConnection(host, context=ctx)
        conn.request("POST", IPA_ENDPOINT, payload, headers)
        resp = conn.getresponse()
    except Exception as e:
        debug(f"RPC ERROR {method}: {e}")
        return {"error": str(e)}

    set_cookie = resp.getheader("Set-Cookie")
    if set_cookie:
        COOKIE = set_cookie.split(";", 1)[0]
        debug(f"[COOKIE] {COOKIE}")

    raw = resp.read().decode()
    conn.close()

    try:
        return json.loads(raw)
    except:
        debug(f"[INVALID JSON] {raw[:200]}")
        return {"error": "invalid_json", "raw": raw}


###############################################################################
# LOGIN
###############################################################################

def login(host, user, password):
    global COOKIE
    debug("Logging in...")

    ctx = ssl._create_unverified_context()
    conn = http.client.HTTPSConnection(host, context=ctx)
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"https://{host}/ipa",
    }

    body = f"user={user}&password={password}"
    conn.request("POST", "/ipa/session/login_password", body, headers)
    resp = conn.getresponse()

    if resp.status != 200:
        print("[!] Login failed")
        sys.exit(1)

    COOKIE = resp.getheader("Set-Cookie").split(";", 1)[0]
    conn.close()
    print("[+] Login OK")
    debug(f"COOKIE={COOKIE}")


###############################################################################
# UTILS
###############################################################################

def pretty(label, obj):
    print(f"\n===== {label} =====")
    if "result" in obj:
        try:
            print(json.dumps(obj["result"], indent=2))
        except:
            print(obj)
    else:
        print(obj)

def extract_list(resp):
    try:
        return resp.get("result", {}).get("result", [])
    except:
        return []


###############################################################################
# USER ANALYSIS
###############################################################################

def analyze_users(users):
    entries = extract_list(users)
    findings = []

    print("\n========== USER ANALYSIS ==========")

    for u in entries:
        uid = u.get("uid", ["UNKNOWN"])[0]
        groups = u.get("memberof_group", [])
        sshkeys = u.get("ipasshpubkey", [])
        hbac = u.get("memberof_hbacrule", [])
        sudo = u.get("memberof_sudorule", [])
        principals = u.get("krbprincipalname", [])

        print(f"\n[USER] {uid}")
        print(f"  Principals: {principals}")
        print(f"  Groups: {groups}")
        print(f"  HBAC: {hbac}")
        print(f"  SUDO: {sudo}")
        print(f"  SSH Keys: {len(sshkeys)} stored")

        findings.append(f"[INFO] User {uid} visible → recon surface")

        if sshkeys:
            findings.append(f"[!] User {uid} stores SSH keys in IPA → persistence vector")

        if hbac:
            findings.append(f"[!] HBAC access for {uid}: {hbac}")

        if sudo:
            findings.append(f"[!] SUDO rule applies to user {uid}: {sudo}")

    return findings


###############################################################################
# HOST ANALYSIS
###############################################################################

def analyze_hosts(hosts):
    entries = extract_list(hosts)
    findings = []

    print("\n========== HOST ANALYSIS ==========")

    for h in entries:
        fqdn = h.get("fqdn", ["UNKNOWN"])[0]
        principals = h.get("krbprincipalname", [])
        hgroups = h.get("memberofindirect_hostgroup", [])
        hbac = h.get("memberofindirect_hbacrule", [])
        sudo = h.get("memberofindirect_sudorule", [])

        print(f"\n[HOST] {fqdn}")
        print(f"  Principals: {principals}")
        print(f"  Hostgroups: {hgroups}")
        print(f"  HBAC: {hbac}")
        print(f"  SUDO: {sudo}")

        findings.append(f"[INFO] Host {fqdn} visible")

        if hbac:
            findings.append(f"[!] Host {fqdn} part of HBAC rule: {hbac}")

        if sudo:
            findings.append(f"[!] Host {fqdn} part of SUDO rule")

    return findings


###############################################################################
# HBAC PRINCIPAL-AWARE ANALYSIS
###############################################################################

def analyze_hbac(hbac):
    entries = extract_list(hbac)
    findings = []

    print("\n========== HBAC RULE ANALYSIS ==========")

    # Create lookup maps
    user_map = {u.get("uid", ["UNKNOWN"])[0]: u.get("krbprincipalname", [])
                for u in GLOBAL_USERS}

    host_map = {h.get("fqdn", ["UNKNOWN"])[0]: h.get("krbprincipalname", [])
                for h in GLOBAL_HOSTS}

    for r in entries:
        name = r.get("cn", ["UNKNOWN"])[0]
        users = r.get("memberuser_user", [])
        ugroups = r.get("memberuser_group", [])
        hosts = r.get("memberhost_host", [])
        hgroups = r.get("memberhost_hostgroup", [])

        print(f"\n[HBAC] {name}")
        print("  Users:")
        for u in users:
            print(f"    - {u} → {user_map.get(u, ['NO PRINCIPAL'])}")

        print(f"  Groups: {ugroups}")

        print("  Hosts:")
        for h in hosts:
            print(f"    - {h} → {host_map.get(h, ['NO PRINCIPAL'])}")

        print(f"  Hostgroups: {hgroups}")

        findings.append(f"[!] HBAC {name}: users {users or ugroups} → {hosts or hgroups}")

    return findings


###############################################################################
# SUDO PRINCIPAL-AWARE ANALYSIS (FIXED)
###############################################################################

def analyze_sudo(sudo):
    entries = extract_list(sudo)
    findings = []

    print("\n========== SUDO RULE ANALYSIS ==========")

    user_map = {u.get("uid", ["UNKNOWN"])[0]: u.get("krbprincipalname", [])
                for u in GLOBAL_USERS}

    host_map = {h.get("fqdn", ["UNKNOWN"])[0]: h.get("krbprincipalname", [])
                for h in GLOBAL_HOSTS}

    for r in entries:
        name = r.get("cn", ["UNKNOWN"])[0]
        users = r.get("memberuser_user", [])
        ugroups = r.get("memberuser_group", [])
        hosts = r.get("memberhost_host", [])
        cmds = r.get("ipasudocommand", [])

        print(f"\n[SUDO RULE] {name}")

        print("  Users:")
        for u in users:
            print(f"    - {u} → {user_map.get(u, ['NO PRINCIPAL'])}")

        print(f"  Groups: {ugroups}")

        print("  Hosts:")
        for h in hosts:
            print(f"    - {h} → {host_map.get(h, ['NO PRINCIPAL'])}")

        print(f"  Commands: {cmds}")

        findings.append(
            f"[!] SUDO {name}: {users} → {hosts} (principal aware)"
        )

    return findings


###############################################################################
# ROASTABILITY SCORING
###############################################################################

def analyze_roastability(users):
    entries = extract_list(users)
    findings = []

    print("\n========== ROASTABILITY ANALYSIS ==========")

    SERVICE_PREFIXES = [
        "http/", "ldap/", "cifs/", "nfs/", "smtp/", "imap/", "ssh/", "host/"
    ]
    SERVICE_CLASSES = ["ipaservice", "krbprincipalaux", "pkiuser"]

    for u in entries:
        uid = u.get("uid", ["UNKNOWN"])[0]
        principals = u.get("krbprincipalname", [])
        objcls = [c.lower() for c in u.get("objectclass", [])]

        risk = "NO RISK"
        reasons = []

        if len(principals) > 1:
            risk = "MODERATE"
            reasons.append("Multiple principals")

        for p in principals:
            if "/" in p:
                risk = "HIGH"
                reasons.append(f"Service-style principal: {p}")
            for pref in SERVICE_PREFIXES:
                if p.lower().startswith(pref):
                    risk = "HIGH"
                    reasons.append(f"Matches service prefix: {pref}")

        if any(c in objcls for c in SERVICE_CLASSES):
            risk = "HIGH"
            reasons.append("Service objectclass present")

        print(f"\n[ROASTABILITY] {uid}")
        print(f"  Principals: {principals}")
        print(f"  Score: {risk}")
        print(f"  Reasons: {reasons or ['none']}")

        if risk != "NO RISK":
            findings.append(f"{uid}: {risk} → {reasons}")

    return findings


###############################################################################
# MAIN
###############################################################################

def main():
    global GLOBAL_USERS, GLOBAL_HOSTS

    if len(sys.argv) != 4:
        print("Usage: freeipa_attackgraph.py <ipa_host> <username> <password>")
        sys.exit(1)

    host, user, password = sys.argv[1], sys.argv[2], sys.argv[3]

    login(host, user, password)

    print("\n[*] Enumerating FreeIPA objects...\n")

    env = request(host, "env")
    users = request(host, "user_find")
    groups = request(host, "group_find")
    hosts = request(host, "host_find")
    services = request(host, "service_find")
    hbac = request(host, "hbacrule_find")
    sudo = request(host, "sudorule_find")
    hostgroups = request(host, "hostgroup_find")
    netgroups = request(host, "netgroup_find")
    dnszones = request(host, "dnszone_find")

    GLOBAL_USERS = extract_list(users)
    GLOBAL_HOSTS = extract_list(hosts)

    pretty("Environment", env)
    pretty("Users", users)
    pretty("Groups", groups)
    pretty("Hosts", hosts)
    pretty("HBAC Rules", hbac)
    pretty("SUDO Rules", sudo)
    pretty("Hostgroups", hostgroups)
    pretty("Netgroups", netgroups)
    pretty("DNS Zones", dnszones)

    print("\n===== ATTACK PATH ANALYSIS =====")

    findings = []
    findings += analyze_users(users)
    findings += analyze_hosts(hosts)
    findings += analyze_hbac(hbac)
    findings += analyze_sudo(sudo)
    findings += analyze_roastability(users)

    print("\n===== SUMMARY =====")
    for f in findings:
        print(f)

    print("\n[+] Enumeration and analysis complete.")


if __name__ == "__main__":
    main()
