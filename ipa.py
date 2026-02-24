#!/usr/bin/env python3
import http.client
import json
import ssl
import sys

IPA_ENDPOINT = "/ipa/session/json"
COOKIE = None

# Enable verbose debug output
DEBUG = True

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

    debug(f"→ RPC CALL: {method}  params={params}")

    conn = http.client.HTTPSConnection(host, context=context)
    conn.request("POST", IPA_ENDPOINT, payload, headers)
    response = conn.getresponse()

    set_cookie = response.getheader("Set-Cookie")
    if set_cookie:
        COOKIE = set_cookie.split(";", 1)[0]
        debug(f"[DEBUG] Updated session cookie: {COOKIE}")

    data = response.read().decode()
    conn.close()

    try:
        parsed = json.loads(data)
        debug(f"← RPC RESULT: {method} returned keys {list(parsed.keys())}")
        return parsed
    except json.JSONDecodeError:
        debug(f"[DEBUG] INVALID JSON from {method}: {data[:200]}")
        return {"error": "invalid_json", "raw": data}


def login(host, user, password):
    global COOKIE

    debug("Attempting login…")

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

    print("[+] Authenticated successfully.")
    debug(f"[DEBUG] Received session cookie: {COOKIE}")


def pretty(label, data):
    print(f"\n=== {label} ===")
    try:
        print(json.dumps(data.get("result", data), indent=2))
    except:
        print(data)


#######################################################################
#  RED TEAM ANALYSIS ENGINE (SAFE + ONLY USES AVAILABLE DATA)
#######################################################################

def redteam_findings(env, users, groups, hosts, services):
    findings = []

    # Weak password policy
    if "result" in env:
        maxlife = env["result"].get("krbmaxpwdlife")
        minlength = env["result"].get("krbpwdminlength")

        if maxlife and isinstance(maxlife, int) and maxlife > 30:
            findings.append("[!] Password lifetime > 30 days → password spraying viable.")
        if minlength and isinstance(minlength, int) and minlength < 10:
            findings.append("[!] Password minimum length < 10 → brute force easier.")

    # User enumeration
    if "result" in users and isinstance(users["result"].get("result"), list):
        user_count = len(users["result"]["result"])
        if user_count > 1:
            findings.append(f"[!] Low-priv user can enumerate {user_count} users → intel leak.")

    # Group enumeration
    if "result" in groups and isinstance(groups["result"].get("result"), list):
        findings.append("[!] Groups visible → RBAC structure leaked.")

    # Hosts visible
    if "result" in hosts and isinstance(hosts["result"].get("result"), list):
        count = len(hosts["result"]["result"])
        if count > 0:
            findings.append(f"[!] {count} hosts visible → lateral movement / recon target expansion.")

    # Services visible
    if "result" in services and isinstance(services["result"].get("result"), list):
        findings.append("[!] Kerberos service principals visible → potential service abuse mapping.")

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

    print("[*] Logging in...")
    login(host, user, password)

    print("[*] Performing stable enumeration...\n")

    env = request(host, "env")
    users = request(host, "user_find", [[], {"all": True}])
    groups = request(host, "group_find", [[], {"all": True}])
    hosts = request(host, "host_find", [[], {"all": True}])
    services = request(host, "service_find", [[], {"all": True}])

    pretty("Environment", env)
    pretty("Users", users)
    pretty("Groups", groups)
    pretty("Hosts", hosts)
    pretty("Services", services)

    print("\n=== RED TEAM FINDINGS ===")
    findings = redteam_findings(env, users, groups, hosts, services)

    if not findings:
        print("No obvious misconfigurations detected.")
    else:
        for f in findings:
            print(f)

    print("\n[+] Enumeration completed.")


if __name__ == "__main__":
    main()
