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

    COOKIE = resp.getheader("Set-Cookie").split(";",1)[0]
    conn.close()
    print("[+] Logged in")


def ipa_rpc(host, method, params):
    global COOKIE
    ctx = ssl._create_unverified_context()
    conn = http.client.HTTPSConnection(host, context=ctx)

    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://{host}/ipa",
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


def print_group(title, entries):
    print(f"\n===== {title} ({len(entries)}) =====")
    for g in entries:
        name = g.get("cn", ["UNKNOWN"])[0]
        print("\n--------------------------------------")
        print(f"NAME: {name}")
        print("--------------------------------------")
        print(json.dumps(g, indent=2))
        print("\n--- MEMBERS ---")
        print("Users:       ", g.get("member_user", []))
        print("Hosts:       ", g.get("member_host", []))
        print("Groups:      ", g.get("member_group", []))
        print("HostGroups:  ", g.get("member_hostgroup", []))
        print("Services:    ", g.get("member_service", []))
        print("Netgroups:   ", g.get("member_netgroup", []))
        print("Indirect:    ", g.get("memberofindirect", []))


def main():
    if len(sys.argv) != 4:
        print("Usage: list_pentest_groups.py <ipa_host> <username> <password>")
        sys.exit(1)

    host, user, password = sys.argv[1], sys.argv[2], sys.argv[3]
    ipa_login(host, user, password)

    print("[*] Searching for POSIX groups containing 'pentest'...")
    posix_result = ipa_rpc(host, "group_find", [["pentest"], {"all": True}])
    posix_groups = posix_result["result"].get("result") or []

    print("[*] Searching for HOST groups containing 'pentest'...")
    hostg_result = ipa_rpc(host, "hostgroup_find", [["pentest"], {"all": True}])
    host_groups = hostg_result["result"].get("result") or []

    print_group("POSIX GROUPS", posix_groups)
    print_group("HOST GROUPS", host_groups)

    print("\n[+] Done.")


if __name__ == "__main__":
    main()
