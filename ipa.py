#!/usr/bin/env python3
import http.client
import json
import ssl
import sys

IPA_ENDPOINT = "/ipa/session/json"
COOKIE = None

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

    context = ssl._create_unverified_context()  # Ignore cert errors

    conn = http.client.HTTPSConnection(host, context=context)
    conn.request("POST", IPA_ENDPOINT, payload, headers)
    response = conn.getresponse()

    # Capture session cookies
    set_cookie = response.getheader("Set-Cookie")
    if set_cookie:
        COOKIE = set_cookie.split(";", 1)[0]

    data = response.read().decode()
    conn.close()

    try:
        return json.loads(data)
    except:
        return {"error": "invalid json", "raw": data}


def login(host, user, password):
    """Perform password-based login to FreeIPA."""
    global COOKIE

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


def print_result(label, res):
    print(f"\n=== {label} ===")
    if "result" in res:
        print(json.dumps(res["result"], indent=2))
    else:
        print(res)


def main():
    if len(sys.argv) != 4:
        print("Usage: freeipa_enum.py <ipa_host> <username> <password>")
        sys.exit(1)

    host = sys.argv[1]
    user = sys.argv[2]
    password = sys.argv[3]

    print("[*] Logging in...")
    login(host, user, password)

    print("[*] Enumerating FreeIPA...")

    print_result("Environment", request(host, "env"))
    print_result("Users", request(host, "user_find", [[], {"all": True}]))
    print_result("Groups", request(host, "group_find", [[], {"all": True}]))
    print_result("Hosts", request(host, "host_find", [[], {"all": True}]))
    print_result("Services", request(host, "service_find", [[], {"all": True}]))

    # DNS enumeration if enabled
    dnszones = request(host, "dnszone_find", [[], {"all": True}])
    print_result("DNS Zones", dnszones)

    if "result" in dnszones and "result" in dnszones["result"]:
        zones = [z["idnsname"][0] for z in dnszones["result"]["result"] if "idnsname" in z]
        for zone in zones:
            print_result(f"DNS Records for {zone}",
                         request(host, "dnsrecord_find", [[zone], {"all": True}]))

    print("\n[+] Enumeration completed.")


if __name__ == "__main__":
    main()
