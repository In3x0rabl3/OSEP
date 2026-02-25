#!/usr/bin/env python3
import http.client
import ssl
import json
import sys

IPA = "/ipa/session/json"
COOKIE = None

def ipa_login(host, user, password):
    """Login to FreeIPA and capture cookie."""
    global COOKIE
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

    COOKIE = resp.getheader("Set-Cookie").split(";",1)[0]
    conn.close()
    print("[+] Logged in successfully")


def ipa_rpc(host, method, params):
    """Safely call FreeIPA JSON-RPC."""
    global COOKIE
    ctx = ssl._create_unverified_context()
    conn = http.client.HTTPSConnection(host, context=ctx)

    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://{host}/ipa"
    }
    if COOKIE:
        headers["Cookie"] = COOKIE

    payload = json.dumps({"method": method, "params": params})
    conn.request("POST", IPA, payload, headers)

    resp = conn.getresponse()
    raw = resp.read().decode()
    conn.close()

    try:
        return json.loads(raw)
    except:
        print("[!] Non-JSON response:")
        print(raw)
        return None


def main():
    if len(sys.argv) != 4:
        print("Usage: list_pentest_groups.py <ipa_host> <username> <password>")
        sys.exit(1)

    host, user, password = sys.argv[1], sys.argv[2], sys.argv[3]
    ipa_login(host, user, password)

    print("[*] Searching for groups matching 'pentest*' ...")

    # Find all groups starting with pentest*
    params = [["pentest*"], {"all": True}]
    group_result = ipa_rpc(host, "group_find", params)

    if not group_result or "result" not in group_result:
        print("[!] No response from server")
        sys.exit(1)

    groups = group_result["result"].get("result") or []

    print(f"[+] Found {len(groups)} matching groups\n")

    if not groups:
        print("[!] No groups named pentest*")
        sys.exit(0)

    # Print EVERYTHING inside each group
    for g in groups:
        name = g.get("cn", ["UNKNOWN"])[0]
        print("\n========================================")
        print(f"GROUP: {name}")
        print("========================================")

        print(json.dumps(g, indent=2))

        # Expand: Print members cleanly
        print("\n--- Members ---")
        print("Users:        ", g.get("member_user", []))
        print("Groups:       ", g.get("member_group", []))
        print("Hosts:        ", g.get("member_host", []))
        print("Host Groups:  ", g.get("member_hostgroup", []))
        print("Services:     ", g.get("member_service", []))
        print("Netgroups:    ", g.get("member_netgroup", []))
        print("Indirect:     ", g.get("memberofindirect", []))


    print("\n[+] Done.")

if __name__ == "__main__":
    main()
