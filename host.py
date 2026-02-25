#!/usr/bin/env python3
import http.client
import ssl
import json
import sys

IPA_ENDPOINT = "/ipa/session/json"
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
        print("[!] Login failed.")
        sys.exit(1)

    # Store session cookie
    COOKIE = resp.getheader("Set-Cookie").split(";", 1)[0]
    conn.close()

    print("[+] Login successful.")


def ipa_rpc(host, method, params=None):
    """Perform a JSON-RPC request to FreeIPA."""
    global COOKIE
    ctx = ssl._create_unverified_context()

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

    conn = http.client.HTTPSConnection(host, context=ctx)
    conn.request("POST", IPA_ENDPOINT, payload, headers)
    resp = conn.getresponse()

    raw = resp.read().decode()
    conn.close()

    # Try parsing JSON
    try:
        return json.loads(raw)
    except:
        print("[!] Invalid JSON returned by server:")
        print(raw)
        return None


def main():
    if len(sys.argv) != 4:
        print("Usage: get_pentest_hosts.py <ipa_host> <username> <password>")
        sys.exit(1)

    host = sys.argv[1]
    user = sys.argv[2]
    password = sys.argv[3]

    ipa_login(host, user, password)

    print("[*] Querying hosts in group 'pentest_hosts'...")

    # Search for hosts in the group
    params = [[], {"in_group": "pentest_hosts", "all": True}]
    result = ipa_rpc(host, "host_find", params)

    if not result or "result" not in result:
        print("[!] FreeIPA returned no usable data.")
        sys.exit(1)

    # FIX: handle None or missing fields
    hosts = result.get("result", {}).get("result") or []

    print(f"[+] Found {len(hosts)} host machine accounts in 'pentest_hosts'")

    if not hosts:
        print("[!] No hosts found. Group may be empty or not exist.")
        sys.exit(0)

    # Print details of each host
    for entry in hosts:
        fqdn = entry.get("fqdn", ["UNKNOWN"])[0]
        principals = entry.get("krbprincipalname", [])
        mac = entry.get("macaddress", ["N/A"])

        print(f"\nHost: {fqdn}")
        print(f"  Principals: {principals}")
        print(f"  MAC Addresses: {mac}")

    print("\n[+] Done.")


if __name__ == "__main__":
    main()
