using System;
using System.Diagnostics;
using System.Runtime.ConstrainedExecution;
using System.Runtime.InteropServices;
using System.Security;
using System.Text;
using System.Threading;

namespace _2Simple_Dll_Injector
{
    class Program
    {
        static void Main(string[] args)
        {
            if(args[0] == null || args[1] == null)
            {
                Console.WriteLine("2Simple Dll Injector.exe <Process Name> <Path To DLL>");
                return;
            }
            Injector.Inject(args[0],args[1]);
        }
    }

    class Injector
    {
        [DllImport("kernel32.dll")]
        public static extern IntPtr OpenProcess(int dwDesiredAccess, bool bInheritHandle, int dwProcessId);

        [DllImport("kernel32.dll", CharSet = CharSet.Auto)]
        public static extern IntPtr GetModuleHandle(string lpModuleName);

        [DllImport("kernel32", CharSet = CharSet.Ansi, ExactSpelling = true, SetLastError = true)]
        static extern IntPtr GetProcAddress(IntPtr hModule, string procName);

        [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
        static extern IntPtr VirtualAllocEx(IntPtr hProcess, IntPtr lpAddress,
            uint dwSize, uint flAllocationType, uint flProtect);

        [DllImport("kernel32.dll", SetLastError = true)]
        static extern bool WriteProcessMemory(IntPtr hProcess, IntPtr lpBaseAddress, byte[] lpBuffer, uint nSize, out UIntPtr lpNumberOfBytesWritten);

        [DllImport("kernel32.dll")]
        static extern IntPtr CreateRemoteThread(IntPtr hProcess,
            IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);

        [DllImport("kernel32.dll", SetLastError = true)]
        static extern UInt32 WaitForSingleObject(IntPtr hHandle, UInt32 dwMilliseconds);

        [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
        static extern bool VirtualFreeEx(IntPtr hProcess, IntPtr lpAddress, int dwSize, uint dwFreeType);

        [DllImport("kernel32.dll", SetLastError = true)]
        [ReliabilityContract(Consistency.WillNotCorruptState, Cer.Success)]
        [SuppressUnmanagedCodeSecurity]
        [return: MarshalAs(UnmanagedType.Bool)]
        static extern bool CloseHandle(IntPtr hObject);

        public static void Inject(string procname, string path)
        {
            string dll = path;
            Process targetProcess = null;
            bool found = false;

            do
            {
                try
                {
                    targetProcess = Process.GetProcessesByName(procname)[0];
                    found = true;
                }
                catch (Exception)
                {
                    Console.WriteLine("Could not find process!");
                    Thread.Sleep(1000);
                    continue;
                }
            }
            while (found == false);

            Console.WriteLine("Process found. ID: " + targetProcess.Id);

            //Open a handle to the target process and get all access 
            IntPtr handle = OpenProcess(0x001F0FFF, false, targetProcess.Id); //0x001F0FFF: Access - All

            //CreateRemoteThread will use LoadLibraryA to load dll as an argument
            IntPtr LibraryAddress = GetProcAddress(GetModuleHandle("kernel32.dll"), "LoadLibraryA");

            //Allocate memory for the dll 
            IntPtr AllocatedMemory = VirtualAllocEx(handle, IntPtr.Zero, (uint)dll.Length + 1, 0x00001000, 4); //0x00001000: Memory - commit, 4: Page - Read and Write
            Console.WriteLine("DLL allocated at: " + AllocatedMemory.ToString());

            //Write dll into allocated memory
            UIntPtr bytesWritten;
            WriteProcessMemory(handle, AllocatedMemory, Encoding.Default.GetBytes(dll), (uint)dll.Length + 1, out bytesWritten);

            //Program loads dll
            IntPtr threadHandle = CreateRemoteThread(handle, IntPtr.Zero, 0, LibraryAddress, AllocatedMemory, 0, IntPtr.Zero);

            //Wait for the loader to finish thread
            WaitForSingleObject(handle, 0xFFFFFFFF); //0xFFFFFFFF: Infinite

            //Freeing the injected thread handle
            CloseHandle(threadHandle);
            //Free allocated memory for the dll 
            VirtualFreeEx(handle, AllocatedMemory, dll.Length + 1, 0x8000); //0x8000: Memory - release
            //Freeing handle for the target process
            CloseHandle(handle);
        }
    }
}
