#!/usr/bin/env python3
import http.client
import json
import ssl
import sys

IPA_ENDPOINT = "/ipa/session/json"
COOKIE = None
DEBUG = True  # Keep debug on so you can see RPC behavior

def debug(msg):
    if DEBUG:
        print(f"[DEBUG] {msg}")

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
        "params": params or [[], {}]
    })

    context = ssl._create_unverified_context()
    debug(f"RPC CALL: {method}")

    conn = http.client.HTTPSConnection(host, context=context)
    conn.request("POST", IPA_ENDPOINT, payload, headers)
    response = conn.getresponse()

    # Session cookie update
    set_cookie = response.getheader("Set-Cookie")
    if set_cookie:
        COOKIE = set_cookie.split(";", 1)[0]
        debug(f"Updated session cookie: {COOKIE}")

    raw = response.read().decode()
    conn.close()

    # Parse JSON
    try:
        parsed = json.loads(raw)
        debug(f"RPC RESULT: {method} keys: {list(parsed.keys())}")
        return parsed
    except:
        debug(f"[INVALID JSON] {raw[:200]}")
        return {"error": "invalid_json", "raw": raw}


def login(host, user, password):
    global COOKIE
    debug("Attempting login...")

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
        print("[!] Login failed")
        sys.exit(1)

    COOKIE = resp.getheader("Set-Cookie").split(";", 1)[0]
    conn.close()

    print("[+] Authenticated")
    debug(f"Cookie: {COOKIE}")


def pretty(label, data):
    print(f"\n=== {label} ===")
    try:
        print(json.dumps(data.get("result", data), indent=2))
    except Exception:
        print(data)


#######################################################################
#  RED TEAM FINDINGS WITH PER-OBJECT CONTEXT
#######################################################################

def analyze_users(users):
    findings = []

    user_list = users.get("result", {}).get("result", [])
    print("\n========== USER ANALYSIS ==========")

    for u in user_list:
        uid = u.get("uid", ["UNKNOWN"])[0]
        mail = u.get("mail", ["no-email"])[0]
        groups = u.get("memberof_group", [])
        authtype = u.get("ipauserauthtype", ["no-2fa"])

        print(f"\n[USER] {uid}")
        print(f"  Email: {mail}")
        print(f"  Groups: {groups}")

        # Vulnerability: No 2FA
        if "otp" not in authtype:
            print("  [VULN] User has NO 2FA configured")
            findings.append(f"User {uid} has no 2FA → vulnerable to phishing/credential reuse")

        # Low-priv user can see all users
        print("  [INFO] Low-priv user can enumerate this account (privacy leak)")

    return findings


def analyze_groups(groups):
    group_list = groups.get("result", {}).get("result", [])
    findings = []

    print("\n========== GROUP ANALYSIS ==========")

    for g in group_list:
        name = g.get("cn", ["UNKNOWN"])[0]
        members = g.get("member_user", [])
        nested = g.get("member_group", [])

        print(f"\n[GROUP] {name}")
        print(f"  Members: {members}")
        print(f"  Nested Groups: {nested}")

        # Privileged group detection
        priv_keywords = ["admin", "wheel", "sudo", "ops"]
        if any(k in name.lower() for k in priv_keywords):
            print(f"  [VULN] Low-priv user can SEE privileged group: {name}")
            findings.append(f"Group {name} visible → RBAC structure leak")

    return findings


def analyze_hosts(hosts):
    host_list = hosts.get("result", {}).get("result", [])
    findings = []

    print("\n========== HOST ANALYSIS ==========")

    for h in host_list:
        fqdn = h.get("fqdn", ["UNKNOWN"])[0]
        krb = h.get("krbprincipalname", [])

        print(f"\n[HOST] {fqdn}")
        print(f"  Kerberos Principals: {krb}")

        print("  [INFO] Host visible to low-priv user (infra exposure)")

        findings.append(f"Host {fqdn} visible → facilitates lateral movement reconnaissance")

    return findings


def analyze_services(services):
    svc_list = services.get("result", {}).get("result", [])
    findings = []

    print("\n========== SERVICE PRINCIPAL ANALYSIS ==========")

    for s in svc_list:
        princ = s.get("krbprincipalname", ["UNKNOWN"])[0]
        print(f"\n[SERVICE] {princ}")

        # All service principals reveal internal architecture
        findings.append(f"Service {princ} visible → reveals internal service topology")

    return findings


#######################################################################
#  MAIN EXECUTION
#######################################################################

def main():
    if len(sys.argv) != 4:
        print("Usage: freeipa_enum.py <ipa_host> <username> <password>")
        sys.exit(1)

    host = sys.argv[1]
    user = sys.argv[2]
    password = sys.argv[3]

    login(host, user, password)

    print("\n[*] Enumerating FreeIPA objects...\n")

    env = request(host, "env")
    users = request(host, "user_find", [[], {"all": True}])
    groups = request(host, "group_find", [[], {"all": True}])
    hosts = request(host, "host_find", [[], {"all": True}])
    services = request(host, "service_find", [[], {"all": True}])

    # Print raw results
    pretty("Environment", env)
    pretty("Users", users)
    pretty("Groups", groups)
    pretty("Hosts", hosts)
    pretty("Services", services)

    print("\n\n======== RED TEAM FINDINGS (DETAILED PER-OBJECT) ========")

    findings = []
    findings += analyze_users(users)
    findings += analyze_groups(groups)
    findings += analyze_hosts(hosts)
    findings += analyze_services(services)

    print("\n======== SUMMARY ========")
    if not findings:
        print("No vulnerabilities found (based on visible data).")
    else:
        for f in findings:
            print(f"- {f}")

    print("\n[+] Enumeration completed.\n")


if __name__ == "__main__":
    main()
