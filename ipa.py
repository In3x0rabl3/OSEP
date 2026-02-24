#!/usr/bin/env python3
import subprocess
import json
import sys
import shutil

BANNER = r"""
===========================================
     FreeIPA Enumeration Tool (No deps)
===========================================
"""

def run_cmd(cmd):
    """Run a shell command and return output or empty string."""
    try:
        result = subprocess.check_output(
            cmd, stderr=subprocess.DEVNULL, shell=True, text=True
        )
        return result.strip()
    except Exception:
        return ""


def check_tools():
    """Ensure required system tools are installed."""
    required = ["ldapsearch", "ipa", "klist"]
    missing = [t for t in required if shutil.which(t) is None]

    if missing:
        print(f"[!] Missing required system tools: {', '.join(missing)}")
        print("[!] Install FreeIPA client packages on the machine.")
        sys.exit(1)

def get_kcred_info():
    """Check if Kerberos credentials exist."""
    print("[*] Checking Kerberos TGT...")
    out = run_cmd("klist")
    if "Default principal" in out:
        print("[+] Kerberos ticket found.")
        print(out)
    else:
        print("[!] No Kerberos ticket detected. Run:")
        print("    kinit username")
        sys.exit(1)


def enum_ipa_env():
    print("\n[*] Enumerating IPA environment settings...")
    out = run_cmd("ipa env")
    print(out if out else "[!] Failed to get IPA environment.")


def enum_users():
    print("\n[*] Enumerating users...")
    out = run_cmd("ipa user-find --all --raw")
    print(out if out else "[!] Could not enumerate users.")


def enum_groups():
    print("\n[*] Enumerating groups...")
    out = run_cmd("ipa group-find --all --raw")
    print(out if out else "[!] Could not enumerate groups.")


def enum_hosts():
    print("\n[*] Enumerating hosts...")
    out = run_cmd("ipa host-find --all --raw")
    print(out if out else "[!] Could not enumerate hosts.")


def enum_services():
    print("\n[*] Enumerating services...")
    out = run_cmd("ipa service-find --all --raw")
    print(out if out else "[!] Could not enumerate services.")


def enum_dns():
    print("\n[*] Enumerating DNS zones...")
    zones = run_cmd("ipa dnszone-find --all --raw")
    if zones:
        print(zones)
        print("\n[*] Enumerating DNS records...")
        zone_names = [
            line.split(":")[1].strip()
            for line in zones.splitlines()
            if line.startswith("idnsname:")
        ]
        for z in zone_names:
            print(f"\n=== DNS Zone: {z} ===")
            recs = run_cmd(f"ipa dnsrecord-find {z} --all --raw")
            print(recs if recs else "[!] No records returned.")
    else:
        print("[!] DNS enumeration unavailable.")


def enum_ldap_raw():
    print("\n[*] Attempting raw LDAP dump via ldapsearch (GSSAPI)...")
    cmd = (
        "ldapsearch -Y GSSAPI -b '' -s base '+' '*'"
    )
    out = run_cmd(cmd)
    print(out if out else "[!] ldapsearch failed (no GSSAPI bind?).")


def main():
    print(BANNER)
    check_tools()
    get_kcred_info()

    enum_ipa_env()
    enum_users()
    enum_groups()
    enum_hosts()
    enum_services()
    enum_dns()
    enum_ldap_raw()

    print("\n[+] Enumeration complete.\n")

if __name__ == "__main__":
    main()
