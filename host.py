#!/usr/bin/env python3
import http.client
import ssl
import json
import sys

IPA = "/ipa/session/json"
COOKIE = None

def ipa_login(host, user, password):
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

    COOKIE = resp.getheader("Set-Cookie").split(";", 1)[0]
    conn.close()
    print("[+] Logged in")


def ipa_rpc(host, method, params):
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
        data = json.loads(raw)
    except:
        print("[!] Non-JSON response:")
        print(raw)
        return None

    if "error" in data and data["error"]:
        print("[!] IPA Error:")
        print(json.dumps(data["error"], indent=2))
        return None

    return data


def main():
    if len(sys.argv) != 4:
        print("Usage: list_pentest_groups.py <ipa_host> <username> <password>")
        sys.exit(1)

    host, user, password = sys.argv[1], sys.argv[2], sys.argv[3]
    ipa_login(host, user, password)

    print("[*] Searching for groups containing 'pentest' ...")

    # REAL FreeIPA search (no wildcard)
    params = [["pentest"], {"all": True}]
    result = ipa_rpc(host, "group_find", params)

    if not result or "result" not in result:
        print("[!] IPA returned no data")
        sys.exit(1)

    groups = result["result"].get("result") or []

    print(f"[+] Found {len(groups)} groups containing 'pentest'")

    if not groups:
        print("[!] No results; verify groups exist")
        sys.exit(0)

    # Print full contents
    for g in groups:
        name = g.get("cn", ["UNKNOWN"])[0]
        print("\n=======================================")
        print(f"GROUP: {name}")
        print("=======================================")

        print(json.dumps(g, indent=2))

        print("\n--- CLEAN MEMBERS ---")
        print("Users:",        g.get("member_user", []))
        print("Hosts:",        g.get("member_host", []))
        print("Groups:",       g.get("member_group", []))
        print("Hostgroups:",   g.get("member_hostgroup", []))
        print("Services:",     g.get("member_service", []))
        print("Netgroups:",    g.get("member_netgroup", []))
        print("Indirect:",     g.get("memberofindirect", []))

    print("\n[+] Done.")


if __name__ == "__main__":
    main()
