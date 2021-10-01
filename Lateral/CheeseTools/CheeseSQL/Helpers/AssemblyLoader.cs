using System;
using System.IO;
using System.Net;
using System.Security.Cryptography;

namespace CheeseSQL.Helpers
{
    public class AssemblyLoader
    {
        public static string LoadAssembly(string filename, out string hash, string className = null, string methodName = null, bool compile = false)
        {
            SHA512 shaM = new SHA512Managed();

            byte[] byteData = new byte[] { };
            if (compile)
            {
                byteData = Helpers.AssemblyCompiler.compileWithRoselyn(className, methodName, filename);
            }
            else if (File.Exists(filename))
            {
                byteData = File.ReadAllBytes(filename);
            }
            else if (filename.StartsWith("http"))
            {
                byteData = (new WebClient()).DownloadData(filename);
            }
            else if (filename.StartsWith("0x"))
            {
                throw new FormatException("[-] Pure Hex string format not supported");
            }
            else
            {
                throw new FormatException();
            }

            hash = "0x" + BitConverter.ToString(shaM.ComputeHash(byteData)).Replace("-", String.Empty);
            return "0x" + BitConverter.ToString(byteData).Replace("-", String.Empty);
        }
    }
}
