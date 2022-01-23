using System;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics;
using System.Runtime.InteropServices;

using static SysCall.Native;

namespace SysCall
{
    /// <summary>
    /// The syscalls
    /// </summary>
    /// <remarks>The syscall codes are specifically for Windows 10 Pro (build 10.0.19042), make sure you use the right ones for your target!</remarks>
    class Syscalls
    {
        
        static IntPtr ntdllBaseAddress = IntPtr.Zero;

        /// <summary>
        /// Gets the base address of ntdll.dll
        /// </summary>
        public static IntPtr NtDllBaseAddress
        {
            get
            {
                if(ntdllBaseAddress == IntPtr.Zero)
                    ntdllBaseAddress = GetNtdllBaseAddress();
                return ntdllBaseAddress;    
            }
        }

        static byte[] bNtOpenProcess =
        {
            0x4C, 0x8B, 0xD1,               // mov r10, rcx
            0xB8, 0x26, 0x00, 0x00, 0x00,   // mov eax, 0x26 (NtOpenProcess Syscall)
            0x0F, 0x05,                     // syscall
            0xC3                            // ret
        };

        static byte[] bNtAllocateVirtualMemory =
        {
            0x4C, 0x8B, 0xD1,               // mov r10, rcx
            0xB8, 0x18, 0x00, 0x00, 0x00,   // mov eax, 0x18 (NtAllocateVirtualMemory Syscall)
            0x0F, 0x05,                     // syscall
            0xC3                            // ret
        };

        static byte[] bNtWriteVirtualMemory =
        {
            0x4C, 0x8B, 0xD1,               // mov r10, rcx
            0xB8, 0x3a, 0x00, 0x00, 0x00,   // mov eax, 0x3a (NtWriteVirtualMemory Syscall)
            0x0F, 0x05,                     // syscall
            0xC3                            // ret
        };

        static byte[] bNtCreateThreadEx =
        {
            0x4C, 0x8B, 0xD1,               // mov r10, rcx
            0xB8, 0xc1, 0x00, 0x00, 0x00,   // mov eax, 0xc1 (NtCreateThreadEx Syscall)
            0x0F, 0x05,                     // syscall
            0xC3                            // ret
        };

        static byte[] bNtProtectVirtualMemory =
        {
            0x4C, 0x8B, 0xD1,               // mov r10, rcx
            0xB8, 0x50, 0x00, 0x00, 0x00,   // mov eax, 0x50 (NtCreateThreadEx Syscall)
            0x0F, 0x05,                     // syscall
            0xC3                            // ret
        };

        public static NTSTATUS NtOpenProcess(ref IntPtr ProcessHandle, UInt32 AccessMask, ref OBJECT_ATTRIBUTES ObjectAttributes, ref CLIENT_ID ClientId)
        {
            // dynamically resolve the syscall
            byte[] syscall = bNtOpenProcess;
            syscall[4] = GetSysCallId("NtOpenProcess");

            unsafe
            {
                fixed (byte* ptr = syscall)
                {
                    IntPtr memoryAddress = (IntPtr)ptr;

                    if (!VirtualProtect(memoryAddress, (UIntPtr)syscall.Length, (uint)AllocationProtect.PAGE_EXECUTE_READWRITE, out uint lpflOldProtect))
                    {
                        throw new Win32Exception();
                    }

                    Delegates.NtOpenProcess assembledFunction = (Delegates.NtOpenProcess)Marshal.GetDelegateForFunctionPointer(memoryAddress, typeof(Delegates.NtOpenProcess));

                    return (NTSTATUS)assembledFunction(ref ProcessHandle, AccessMask, ref ObjectAttributes, ref ClientId);
                }
            }
        }

        public static NTSTATUS NtAllocateVirtualMemory(IntPtr ProcessHandle, ref IntPtr BaseAddress, IntPtr ZeroBits, ref IntPtr RegionZize, UInt32 AllocationType, UInt32 Protect)
        {
            // dynamically resolve the syscall
            byte[] syscall = bNtAllocateVirtualMemory;
            syscall[4] = GetSysCallId("NtAllocateVirtualMemory");

            unsafe
            {
                fixed (byte* ptr = syscall)
                {
                    IntPtr memoryAddress = (IntPtr)ptr;

                    if (!VirtualProtect(memoryAddress, (UIntPtr)syscall.Length, (uint)AllocationProtect.PAGE_EXECUTE_READWRITE, out uint lpflOldProtect))
                    {
                        throw new Win32Exception();
                    }

                    Delegates.NtAllocateVirtualMemory assembledFunction = (Delegates.NtAllocateVirtualMemory)Marshal.GetDelegateForFunctionPointer(memoryAddress, typeof(Delegates.NtAllocateVirtualMemory));

                    return (NTSTATUS)assembledFunction(ProcessHandle, ref BaseAddress, ZeroBits, ref RegionZize, AllocationType, Protect);
                }
            }
        }

        public static NTSTATUS NtWriteVirtualMemory(IntPtr hProcess, IntPtr baseAddress, IntPtr buffer, UInt32 Length, ref UInt32 bytesWritten)
        {
            // dynamically resolve the syscall
            byte[] syscall = bNtWriteVirtualMemory;
            syscall[4] = GetSysCallId("NtWriteVirtualMemory");


            unsafe
            {
                fixed (byte* ptr = syscall)
                {
                    IntPtr memoryAddress = (IntPtr)ptr;

                    if (!VirtualProtect(memoryAddress, (UIntPtr)syscall.Length, (uint)AllocationProtect.PAGE_EXECUTE_READWRITE, out uint lpflOldProtect))
                    {
                        throw new Win32Exception();
                    }

                    Delegates.NtWriteVirtualMemory assembledFunction = (Delegates.NtWriteVirtualMemory)Marshal.GetDelegateForFunctionPointer(memoryAddress, typeof(Delegates.NtWriteVirtualMemory));

                    return (NTSTATUS)assembledFunction(hProcess, baseAddress, buffer, (uint)Length, ref bytesWritten);
                }
            }
        }

        public static NTSTATUS NtProtectVirtualMemory(IntPtr ProcessHandle, ref IntPtr BaseAddress, ref IntPtr RegionSize, uint NewProtect, ref uint OldProtect)
        {
            // dynamically resolve the syscall
            byte[] syscall = bNtProtectVirtualMemory;
            syscall[4] = GetSysCallId("NtProtectVirtualMemory");

            unsafe
            {
                fixed (byte* ptr = syscall)
                {
                    IntPtr memoryAddress = (IntPtr)ptr;

                    if (!VirtualProtect(memoryAddress, (UIntPtr)syscall.Length, (uint)AllocationProtect.PAGE_EXECUTE_READWRITE, out uint lpflOldProtect))
                    {
                        throw new Win32Exception();
                    }

                    Delegates.NtProtectVirtualMemory assembledFunction = (Delegates.NtProtectVirtualMemory)Marshal.GetDelegateForFunctionPointer(memoryAddress, typeof(Delegates.NtProtectVirtualMemory));

                    return (NTSTATUS)assembledFunction(ProcessHandle, ref BaseAddress, ref RegionSize, NewProtect, ref OldProtect);
                }
            }
        }

        public static NTSTATUS NtCreateThreadEx(out IntPtr threadHandle, ACCESS_MASK desiredAccess, IntPtr objectAttributes, IntPtr processHandle, IntPtr startAddress, IntPtr parameter, bool createSuspended, int stackZeroBits, int sizeOfStack, int maximumStackSize, IntPtr attributeList)
        {
            // dynamically resolve the syscall
            byte[] syscall = bNtCreateThreadEx;
            syscall[4] = GetSysCallId("NtCreateThreadEx");

            unsafe
            {
                fixed (byte* ptr = syscall)
                {
                    IntPtr memoryAddress = (IntPtr)ptr;

                    if (!VirtualProtect(memoryAddress, (UIntPtr)syscall.Length, (uint)AllocationProtect.PAGE_EXECUTE_READWRITE, out uint lpflOldProtect))
                    {
                        throw new Win32Exception();
                    }

                    Delegates.NtCreateThreadEx assembledFunction = (Delegates.NtCreateThreadEx)Marshal.GetDelegateForFunctionPointer(memoryAddress, typeof(Delegates.NtCreateThreadEx));

                    return (NTSTATUS)assembledFunction(out threadHandle, desiredAccess, objectAttributes, processHandle, startAddress, parameter, createSuspended, stackZeroBits, sizeOfStack, maximumStackSize, attributeList);
                }
            }
        }

        private static IntPtr GetNtdllBaseAddress()
        {
            Process hProc = Process.GetCurrentProcess();
            
            foreach(ProcessModule m in hProc.Modules)
            {
                if (m.ModuleName.ToUpper().Equals("NTDLL.DLL"))
                    return m.BaseAddress;
            }

            // we can't find the base address
            return IntPtr.Zero;
        }
        
        public static byte GetSysCallId(string FunctionName)
        {
            // first get the proc address
            IntPtr funcAddress = GetProcAddress(NtDllBaseAddress, FunctionName);

            byte count = 0;

            // loop until we find an unhooked function
            while (true)
            {
                // is the function hooked - we are looking for the 0x4C, 0x8B, 0xD1, instructions - this is the start of a syscall
                bool hooked = false;

                var instructions = new byte[5];
                Marshal.Copy(funcAddress, instructions, 0, 5);
                if (!StructuralComparisons.StructuralEqualityComparer.Equals(new byte[3] { instructions[0], instructions[1], instructions[2] }, new byte[3] { 0x4C, 0x8B, 0xD1 }))
                    hooked = true;

                if (!hooked)
                    return (byte)(instructions[4] - count);

                funcAddress = (IntPtr)((UInt64)funcAddress + ((UInt64)32));
                count++;
            }
        }

        struct Delegates
        {
            [UnmanagedFunctionPointer(CallingConvention.StdCall)]
            public delegate
            NTSTATUS NtOpenProcess(ref IntPtr ProcessHandle, UInt32 AccessMask, ref OBJECT_ATTRIBUTES ObjectAttributes, ref CLIENT_ID ClientId);

            [UnmanagedFunctionPointer(CallingConvention.StdCall)]
            public delegate
            NTSTATUS NtAllocateVirtualMemory(IntPtr ProcessHandle, ref IntPtr BaseAddress, IntPtr ZeroBits, ref IntPtr RegionZize, UInt32 AllocationType, UInt32 Protect);

            [UnmanagedFunctionPointer(CallingConvention.StdCall)]
            public delegate
            NTSTATUS NtWriteVirtualMemory(IntPtr hProcess, IntPtr baseAddress, IntPtr buffer, UInt32 Length, ref UInt32 bytesWritten);

            [UnmanagedFunctionPointer(CallingConvention.StdCall)]
            public delegate
            NTSTATUS NtProtectVirtualMemory(IntPtr ProcessHandle, ref IntPtr BaseAddress, ref IntPtr RegionSize, uint NewProtect, ref uint OldProtect);

            [UnmanagedFunctionPointer(CallingConvention.StdCall)]
            public delegate
            NTSTATUS NtCreateThreadEx(out IntPtr threadHandle, ACCESS_MASK desiredAccess, IntPtr objectAttributes, IntPtr processHandle, IntPtr startAddress, IntPtr parameter, bool createSuspended, int stackZeroBits, int sizeOfStack, int maximumStackSize, IntPtr attributeList);
        };
    }
}
