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

    COOKIE = resp.getheader("Set-Cookie").split(";", 1)[0]
    conn.close()

    print("[+] Login OK")


def ipa_rpc(host, method, params=None):
    """Perform a JSON-RPC request to FreeIPA."""
    global COOKIE
    ctx = ssl._create_unverified_context()

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

    conn = http.client.HTTPSConnection(host, context=ctx)
    conn.request("POST", IPA_ENDPOINT, payload, headers)
    resp = conn.getresponse()

    raw = resp.read().decode()
    conn.close()

    # Try parsing JSON
    try:
        data = json.loads(raw)
    except:
        print("[!] IPA returned non-JSON response:")
        print(raw)
        return None

    # IPA sometimes returns errors in the JSON
    if "error" in data and data["error"] is not None:
        print("\n[!] IPA SERVER ERROR:")
        print(json.dumps(data["error"], indent=2))
        return None

    return data


def safe_get_hosts(result):
    """Extract host list safely without NoneType crashes."""
    if not isinstance(result, dict):
        return []

    outer = result.get("result")
    if not isinstance(outer, dict):
        return []

    inner = outer.get("result")
    if not isinstance(inner, list):
        return []

    return inner


def main():
    if len(sys.argv) != 4:
        print("Usage: get_pentest_hosts.py <ipa_host> <username> <password>")
        sys.exit(1)

    host, user, password = sys.argv[1], sys.argv[2], sys.argv[3]

    ipa_login(host, user, password)

    print("[*] Searching for hosts in group 'pentest_hosts'...")

    params = [[], {"in_group": "pentest_hosts", "all": True}]
    result = ipa_rpc(host, "host_find", params)

    if result is None:
        print("[!] No usable response from IPA.")
        sys.exit(1)

    # SAFE EXTRACTION (fix for line 93 + line 115 errors)
    hosts = safe_get_hosts(result)

    print(f"[+] Found {len(hosts)} host entries")

    if not hosts:
        print("[!] No hosts found in group 'pentest_hosts'.")
        sys.exit(0)

    for entry in hosts:
        if not isinstance(entry, dict):
            continue

        fqdn = entry.get("fqdn", ["UNKNOWN"])[0]
        principals = entry.get("krbprincipalname", [])
        mac = entry.get("macaddress", ["N/A"])

        print(f"\nHost: {fqdn}")
        print(f"  Principals: {principals}")
        print(f"  MAC: {mac}")

    print("\n[+] Done.")


if __name__ == "__main__":
    main()
