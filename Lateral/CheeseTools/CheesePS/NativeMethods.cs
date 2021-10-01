using System;
using System.Runtime.InteropServices;

namespace CheesePS
{
    internal class NativeMethods
    {
        public const int S_OK = 0;

        //implement required kernel32.dll functions 
        [DllImport("kernel32")]
        public static extern IntPtr LoadLibrary(string name);

        [DllImport("kernel32", SetLastError = true)]
        public static extern IntPtr GetModuleHandleA(string name);

        [DllImport("kernel32")]
        public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);

        [DllImport("kernel32")]
        public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr dwSize, uint flNewProtect,
            out uint lpflOldProtect);

        [DllImport("kernel32.dll", EntryPoint = "RtlMoveMemory", SetLastError = false)]
        public static extern void CopyMemory(IntPtr dest, IntPtr src, int size);

        //[DllImport("wldp.dll")]
        public static int WldpQueryDynamicCodeTrustStub(SafeHandle fileHandle, IntPtr baseImage, uint ImageSize)
        {
            return S_OK;
        }
        public static void WldpQueryDynamicCodeTrustStubEnd() { }
    }
}