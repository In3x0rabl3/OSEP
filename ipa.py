#!/usr/bin/env python3
import http.client
import json
import ssl
import sys

IPA_ENDPOINT = "/ipa/session/json"
COOKIE = None
DEBUG = True  # Toggle debug output

def debug(msg):
    if DEBUG:
        print(f"[DEBUG] {msg}")

###############################################################################
# RPC CALLER
###############################################################################

def request(host, method, params=None):
    """Perform JSON-RPC request to FreeIPA."""
    global COOKIE
    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://{host}/ipa"
    }
    if COOKIE:
        headers["Cookie"] = COOKIE

    payload = json.dumps({
        "method": method,
        "params": params or [[], {"all": True}]
    })

    ctx = ssl._create_unverified_context()
    debug(f"--> RPC CALL: {method}")

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
        debug(f"Updated cookie: {COOKIE}")

    raw = resp.read().decode()
    conn.close()

    try:
        parsed = json.loads(raw)
        debug(f"<-- RESULT {method}: keys={list(parsed.keys())}")
        return parsed
    except:
        debug(f"[INVALID JSON] {raw[:200]}")
        return {"error": "invalid_json", "raw": raw}


###############################################################################
# LOGIN
###############################################################################

def login(host, user, password):
    """Authenticate with FreeIPA UI backend."""
    global COOKIE
    debug("Authenticating...")

    ctx = ssl._create_unverified_context()
    conn = http.client.HTTPSConnection(host, context=ctx)

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"https://{host}/ipa"
    }

    body = f"user={user}&password={password}"
    conn.request("POST", "/ipa/session/login_password", body, headers)
    resp = conn.getresponse()

    if resp.status != 200:
        print("[!] Login failed")
        sys.exit(1)

    COOKIE = resp.getheader("Set-Cookie").split(";", 1)[0]
    conn.close()

    print("[+] Login successful")
    debug(f"Cookie set: {COOKIE}")


###############################################################################
# OUTPUT HELPERS
###############################################################################

def pretty(label, data):
    print(f"\n====== {label} ======")
    if "result" in data:
        try:
            print(json.dumps(data["result"], indent=2))
        except:
            print(data)
    else:
        print(data)

def extract_list(res):
    try:
        return res.get("result", {}).get("result", [])
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
        krb = u.get("krbprincipalname", [])

        print(f"\n[USER] {uid}")
        print(f"  Groups: {groups}")
        print(f"  SSH Keys: {len(sshkeys)} stored")
        print(f"  HBAC Access: {hbac}")
        print(f"  SUDO Access: {sudo}")
        print(f"  Kerberos Principals: {krb}")

        findings.append(f"[INFO] User {uid} visible → recon exposure")

        if sshkeys:
            findings.append(f"[!] User {uid} has stored SSH keys (persistence surface)")

        if hbac:
            findings.append(f"[!] User {uid} allowed by HBAC: {hbac}")

        if sudo:
            findings.append(f"[!] User {uid} included in SUDO rules: {sudo}")

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
        krb = h.get("krbprincipalname", [])
        hgroups = h.get("memberofindirect_hostgroup", [])
        hbac = h.get("memberofindirect_hbacrule", [])
        sudo = h.get("memberofindirect_sudorule", [])

        print(f"\n[HOST] {fqdn}")
        print(f"  Kerberos Principals: {krb}")
        print(f"  Hostgroups: {hgroups}")
        print(f"  HBAC Rules: {hbac}")
        print(f"  SUDO Rules: {sudo}")

        findings.append(f"[INFO] Host {fqdn} visible (infra enumeration)")

        if hbac:
            findings.append(f"[!] Host {fqdn} controlled by HBAC: {hbac}")

        if sudo:
            findings.append(f"[!] Host {fqdn} has SUDO escalation paths")

    return findings


###############################################################################
# HBAC ANALYSIS
###############################################################################

def analyze_hbac(hbac):
    entries = extract_list(hbac)
    findings = []

    print("\n========== HBAC RULE ANALYSIS ==========")

    for r in entries:
        name = r.get("cn", ["UNKNOWN"])[0]
        users = r.get("memberuser_user", [])
        ugroups = r.get("memberuser_group", [])
        hosts = r.get("memberhost_host", [])
        hgroups = r.get("memberhost_hostgroup", [])

        print(f"\n[HBAC RULE] {name}")
        print(f"  Users: {users}")
        print(f"  Groups: {ugroups}")
        print(f"  Hosts: {hosts}")
        print(f"  Hostgroups: {hgroups}")

        findings.append(f"[!] HBAC {name}: users {users or ugroups} → hosts {hosts or hgroups}")

    return findings


###############################################################################
# SUDO ANALYSIS
###############################################################################

def analyze_sudo(sudo):
    entries = extract_list(sudo)
    findings = []

    print("\n========== SUDO RULE ANALYSIS ==========")

    for r in entries:
        name = r.get("cn", ["UNKNOWN"])[0]
        u = r.get("memberuser_user", [])
        ug = r.get("memberuser_group", [])
        hosts = r.get("memberhost_host", [])
        cmds = r.get("ipasudocommand", [])

        print(f"\n[SUDO RULE] {name}")
        print(f"  Users: {u}")
        print(f"  Groups: {ug}")
        print(f"  Hosts: {hosts}")
        print(f"  Commands: {cmds}")

        findings.append(f"[!] SUDO rule {name} → escalation possible on {hosts}")

    return findings


###############################################################################
# ROASTABILITY SCORING ENGINE (SAFE)
###############################################################################

def analyze_roastability(users):
    entries = extract_list(users)
    findings = []

    print("\n========== ROASTABILITY ANALYSIS ==========")

    SERVICE_PREFIXES = [
        "http/", "host/", "ldap/", "cifs/", "nfs/", "smtp/", "imap/", "ssh/",
        "postgres/", "kafka/", "redis/", "vault/", "mysql/", "mongo/"
    ]

    SERVICE_CLASSES = [
        "ipaservice", "pkiuser", "krbprincipalaux", "ipadb"
    ]

    for u in entries:
        uid = u.get("uid", ["UNKNOWN"])[0]
        principals = u.get("krbprincipalname", [])
        objcls = [c.lower() for c in u.get("objectclass", [])]

        risk = "NO RISK"
        reasons = []

        if len(principals) > 1:
            risk = "MODERATE RISK"
            reasons.append("Multiple Kerberos principals found")

        for p in principals:
            if "/" in p:
                risk = "HIGH RISK"
                reasons.append(f"Service-style principal: {p}")

            for pref in SERVICE_PREFIXES:
                if p.lower().startswith(pref):
                    risk = "HIGH RISK"
                    reasons.append(f"Principal matches service prefix {pref}")

        if any(c in objcls for c in SERVICE_CLASSES):
            risk = "HIGH RISK"
            reasons.append(f"ObjectClass indicates service identity")

        print(f"\n[ROASTABILITY] {uid}")
        print(f"  Principals: {principals}")
        print(f"  ObjectClasses: {objcls}")
        print(f"  Score: {risk}")
        print(f"  Reasons: {reasons or ['None']}")

        if risk != "NO RISK":
            findings.append(f"{uid} roastability={risk}: {reasons}")

    return findings


###############################################################################
# MAIN EXECUTION
###############################################################################

def main():
    if len(sys.argv) != 4:
        print("Usage: freeipa_attackgraph.py <ipa_host> <username> <password>")
        sys.exit(1)

    host, user, password = sys.argv[1], sys.argv[2], sys.argv[3]

    login(host, user, password)

    print("\n[*] Enumerating objects...\n")

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

    pretty("Environment", env)
    pretty("Users", users)
    pretty("Groups", groups)
    pretty("Hosts", hosts)
    pretty("HBAC Rules", hbac)
    pretty("SUDO Rules", sudo)
    pretty("Hostgroups", hostgroups)
    pretty("Netgroups", netgroups)
    pretty("DNS Zones", dnszones)

    print("\n\n===== ATTACK PATH ANALYSIS =====")

    findings = []
    findings += analyze_users(users)
    findings += analyze_hosts(hosts)
    findings += analyze_hbac(hbac)
    findings += analyze_sudo(sudo)
    findings += analyze_roastability(users)

    print("\n===== SUMMARY =====")
    for f in findings:
        print(f)

    print("\n[+] Enumeration complete.")

if __name__ == "__main__":
    main()
