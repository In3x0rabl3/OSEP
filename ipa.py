#!/usr/bin/env python3
import http.client
import json
import ssl
import sys

IPA_ENDPOINT = "/ipa/session/json"
COOKIE = None
DEBUG = True  # Turn debug logging on/off

def debug(msg):
    if DEBUG:
        print(f"[DEBUG] {msg}")

###########################################################################
# RPC HELPERS
###########################################################################

def request(host, method, params=None):
    """Perform a JSON-RPC call to FreeIPA."""
    global COOKIE

    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://{host}/ipa",
    }
    if COOKIE:
        headers["Cookie"] = COOKIE

    payload = json.dumps({
        "method": method,
        "params": params or [[], {"all": True}]
    })

    context = ssl._create_unverified_context()

    debug(f"--> RPC CALL: {method}")

    try:
        conn = http.client.HTTPSConnection(host, context=context)
        conn.request("POST", IPA_ENDPOINT, payload, headers)
        resp = conn.getresponse()
    except Exception as e:
        debug(f"RPC ERROR: {method}: {e}")
        return {"error": str(e)}

    # Capture cookies
    set_cookie = resp.getheader("Set-Cookie")
    if set_cookie:
        COOKIE = set_cookie.split(";", 1)[0]
        debug(f"Updated cookie: {COOKIE}")

    raw = resp.read().decode()
    conn.close()

    try:
        parsed = json.loads(raw)
        debug(f"<-- RPC RESULT: {method} keys={list(parsed.keys())}")
        return parsed
    except:
        debug(f"[INVALID JSON] {raw[:200]}")
        return {"error": "invalid_json", "raw": raw}


###########################################################################
# LOGIN
###########################################################################

def login(host, user, password):
    global COOKIE

    debug("Logging in...")

    context = ssl._create_unverified_context()
    conn = http.client.HTTPSConnection(host, context=context)

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"https://{host}/ipa",
    }

    body = f"user={user}&password={password}"
    conn.request("POST", "/ipa/session/login_password", body, headers)
    resp = conn.getresponse()

    if resp.status != 200:
        print("[!] Login failed!")
        sys.exit(1)

    COOKIE = resp.getheader("Set-Cookie").split(";", 1)[0]
    conn.close()

    print("[+] Authenticated")
    debug(f"Cookie={COOKIE}")


###########################################################################
# PRETTY PRINT
###########################################################################

def pretty(label, data):
    print(f"\n===== {label} =====")
    if "result" in data:
        try:
            print(json.dumps(data["result"], indent=2))
        except:
            print(data)
    else:
        print(data)


###########################################################################
# ATTACK PATH ENGINE
###########################################################################

def extract_list(res):
    try:
        return res.get("result", {}).get("result", [])
    except:
        return []

def analyze_users(users):
    entries = extract_list(users)
    findings = []

    print("\n========== USER ANALYSIS ==========")

    for u in entries:
        uid = u.get("uid", ["UNKNOWN"])[0]
        groups = u.get("memberof_group", [])
        hbac = u.get("memberof_hbacrule", [])
        sudo = u.get("memberof_sudorule", [])
        sshkeys = u.get("ipasshpubkey", [])
        krb = u.get("krbprincipalname", [])

        print(f"\n[USER] {uid}")
        print(f"  Groups: {groups}")
        print(f"  HBAC Access: {hbac}")
        print(f"  SUDO Access: {sudo}")
        print(f"  SSH Keys: {len(sshkeys)} keys")
        print(f"  Kerberos Principals: {krb}")

        if not sshkeys:
            findings.append(f"[!] User {uid} has no SSH keys → password-only auth.")
        else:
            findings.append(f"[!] User {uid} has SSH keys in IPA → persistence risk.")

        if len(krb) > 1:
            findings.append(f"[!] User {uid} has multiple Kerberos identities.")

        if hbac:
            findings.append(f"[!] User {uid} can access hosts via HBAC rules: {hbac}")

        if sudo:
            findings.append(f"[!] User {uid} has sudo capability via rules: {sudo}")

    return findings


def analyze_hosts(hosts):
    entries = extract_list(hosts)
    findings = []

    print("\n========== HOST ANALYSIS ==========")

    for h in entries:
        fqdn = h.get("fqdn", ["UNKNOWN"])[0]
        krb = h.get("krbprincipalname", [])
        sshkeys = h.get("ipasshpubkey", [])
        hgroups = h.get("memberofindirect_hostgroup", [])
        hbac = h.get("memberofindirect_hbacrule", [])
        sudo = h.get("memberofindirect_sudorule", [])

        print(f"\n[HOST] {fqdn}")
        print(f"  Principals: {krb}")
        print(f"  Hostgroups: {hgroups}")
        print(f"  HBAC Rules: {hbac}")
        print(f"  SUDO Rules: {sudo}")
        print(f"  SSH keys: {len(sshkeys)} stored")

        findings.append(f"[INFO] Host {fqdn} is visible → recon exposure")

        if hbac:
            findings.append(f"[!] Host {fqdn} participates in HBAC: {hbac}")

        if sudo:
            findings.append(f"[!] Host {fqdn} participates in SUDO rules.")

    return findings


def analyze_hbac(hbac):
    entries = extract_list(hbac)
    findings = []

    print("\n========== HBAC RULES ==========")

    for r in entries:
        name = r.get("cn", ["UNKNOWN"])[0]
        u = r.get("memberuser_user", [])
        ug = r.get("memberuser_group", [])
        hg = r.get("memberhost_hostgroup", [])
        hosts = r.get("memberhost_host", [])

        print(f"\n[HBAC RULE] {name}")
        print(f"  Users: {u}")
        print(f"  User Groups: {ug}")
        print(f"  Hostgroups: {hg}")
        print(f"  Hosts: {hosts}")

        findings.append(f"[!] HBAC rule {name} → users {u or ug} can access hosts {hosts or hg}")

    return findings


def analyze_sudo(sudo):
    entries = extract_list(sudo)
    findings = []

    print("\n========== SUDO RULES ==========")

    for r in entries:
        name = r.get("cn", ["UNKNOWN"])[0]
        u = r.get("memberuser_user", [])
        ug = r.get("memberuser_group", [])
        hg = r.get("memberhost_hostgroup", [])
        hosts = r.get("memberhost_host", [])
        cmds = r.get("ipasudocommand", [])

        print(f"\n[SUDO RULE] {name}")
        print(f"  Users: {u}")
        print(f"  Groups: {ug}")
        print(f"  Hosts: {hosts}")
        print(f"  Commands: {cmds}")

        findings.append(f"[!] SUDO rule {name} grants escalation on hosts {hosts}")

    return findings


###########################################################################
# RUN ENUM + ATTACK ANALYSIS
###########################################################################

def main():
    if len(sys.argv) != 4:
        print("Usage: freeipa_attackgraph.py <ipa_host> <username> <password>")
        sys.exit(1)

    host = sys.argv[1]
    user = sys.argv[2]
    password = sys.argv[3]

    login(host, user, password)

    # Core enumerations
    env = request(host, "env")
    users = request(host, "user_find")
    groups = request(host, "group_find")
    hosts = request(host, "host_find")
    services = request(host, "service_find")

    # New critical queries:
    hbac = request(host, "hbacrule_find")
    sudo = request(host, "sudorule_find")
    hostgroup = request(host, "hostgroup_find")
    netgroup = request(host, "netgroup_find")
    dnszones = request(host, "dnszone_find")

    pretty("Environment", env)
    pretty("Users", users)
    pretty("Groups", groups)
    pretty("Hosts", hosts)
    pretty("HBAC Rules", hbac)
    pretty("SUDO Rules", sudo)
    pretty("Hostgroups", hostgroup)
    pretty("Netgroups", netgroup)
    pretty("DNS Zones", dnszones)

    print("\n\n===== ATTACK PATH ANALYSIS =====")

    findings = []
    findings += analyze_users(users)
    findings += analyze_hosts(hosts)
    findings += analyze_hbac(hbac)
    findings += analyze_sudo(sudo)

    print("\n===== SUMMARY =====")
    for f in findings:
        print(f)

    print("\n[+] FreeIPA Attack Graph Enumeration Complete")

if __name__ == "__main__":
    main()
