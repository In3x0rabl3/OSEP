import json
import os
import sys
import re
import argparse
from colorama import Fore

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Chameleon PSTranslate - Helper to search obfuscated functions'
    )
    parser.add_argument('-f', '--function', required=True, type=str, default=None, help='Function to search')
    parser.add_argument('mapping', help='Mapping file')

    args = parser.parse_args()

    os.system('color')

    if not os.path.isfile(args.mapping):
        print("[-] Mapping file not found")
        sys.exit(1)

    with open(args.mapping, "r") as ps:
        mapping = json.load(ps)

    function = args.function

    for k in mapping.keys():
        if re.search(function, k, re.IGNORECASE):

            rainbow = [Fore.LIGHTBLUE_EX,
                       Fore.LIGHTGREEN_EX,
                       Fore.LIGHTRED_EX,
                       Fore.LIGHTCYAN_EX,
                       Fore.LIGHTMAGENTA_EX,
                       Fore.LIGHTYELLOW_EX
                       ]

            op = mapping[k]['params']['original']
            np = mapping[k]['params']['repl']

            orig_params = ", ".join([f"{rainbow[j%5]}{op[j]}{Fore.WHITE}" for j in range(len(op))])
            new_params = ", ".join([f"{rainbow[j%5]}{np[j]}{Fore.WHITE}"for j in range(len(np))])

            print(f"[+] Found func : {rainbow[5]}{k}{Fore.WHITE}")
            print(f"  [>] Replaced by: {rainbow[5]}{mapping[k]['repl']}{Fore.WHITE}")
            print(f"  [>] Original params: {orig_params}")
            print(f"  [>] Obfuscated with: {new_params}")
            print()
