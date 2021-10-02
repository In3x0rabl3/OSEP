using System;
using System.Text;
using System.IO;

namespace FormatShellcode
{
        public static void PrintShellcode(byte[] shellcodeBytes)
        {
            StringBuilder shellcode = new StringBuilder();
            shellcode.Append("byte[] shellcode = new byte[");
            shellcode.Append(shellcodeBytes.Length);
            shellcode.Append("] { ");

            for(int i = 0; i < shellcodeBytes.Length; i++)
            {
                shellcode.Append("0x");
                shellcode.AppendFormat("{0:x2}", shellcodeBytes[i]);
                if(i < shellcodeBytes.Length -1)
                {
                    shellcode.Append(", ");
                }
            }

            shellcode.Append(" };");
            Console.WriteLine(shellcode.ToString());
        }

        public static void Main(string[] args)
        {
            byte[] shellcode = File.ReadAllBytes(args[0]);
            PrintShellcode(shellcode);
        }
    }
}
