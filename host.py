#!/usr/bin/env python3
import http.client
import ssl
import json
import sys

IPA_ENDPOINT = "/ipa/session/json"
COOKIE = None


def ipa_login(host, user, password):
    """Authenticate to FreeIPA and store session cookie."""
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

    COOKIE = resp.getheader("Set-Cookie").split(";", 1)[0]
    conn.close()

    print("[+] Login successful.")


def ipa_rpc(host, method, params=None):
    """Perform JSON-RPC call to FreeIPA."""
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
        "params": params or [[], {"all": True}]
    })

    conn = http.client.HTTPSConnection(host, context=ctx)
    conn.request("POST", IPA_ENDPOINT, payload, headers)
    resp = conn.getresponse()

    raw = resp.read().decode()
    conn.close()

    try:
        return json.loads(raw)
    except:
        print("[!] Server returned non-JSON:")
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

    print("[*] Looking up group 'pentest_hosts'...")

    # Query all hosts in this group
    params = [[], {"in_group": "pentest_hosts", "all": True}]
    result = ipa_rpc(host, "host_find", params)

    if not result or "result" not in result:
        print("[!] No results returned.")
        sys.exit(1)

    hosts = result["result"]["result"]
    print(f"[+] Found {len(hosts)} hosts in group 'pentest_hosts'")

    for h in hosts:
        fqdn = h.get("fqdn", ["UNKNOWN"])[0]
        principals = h.get("krbprincipalname", [])
        print(f"\nHost: {fqdn}")
        print(f"  Principals: {principals}")

    print("\n[+] Done.")


if __name__ == "__main__":
    main()
