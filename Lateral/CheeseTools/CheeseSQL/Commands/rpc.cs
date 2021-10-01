using CheeseSQL.Helpers;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;


namespace CheeseSQL.Commands
{
    public class rpc : ICommand
    {
        public static string CommandName => "rpc";

        public string Description()
        {
            return $"Configure Linked SQL Server to Allow RPC connections";
        }

        public string Usage()
        {
            return $@"{Description()} 
Required arguments:
  /server:SERVER                   Server to connect to
  /target:TARGET                   Specify a linked SQL server as the target

Optional arguments:
  /db:DB                           Specify an alternate database to connect 
  /impersonate:(USER|LOGIN):USER   Impersonate on the connect server using EXECUTE AS LOGIN or EXECUTE AS USER
  /impersonate-intermediate:USER   Impersonate a user on the intermediate server
  /sqlauth                         If set, use SQL authentication
    /user:SQLUSER                  If /sqlauth, set the user for SQL authentication
    /password:SQLPASSWORD          If /sqlauth, set the password for SQL authentication";
        }

        public void Execute(Dictionary<string, string> arguments)
        {
            string connectInfo = "";

            ArgumentSet argumentSet;
            try
            {
                argumentSet = ArgumentSet.FromDictionary(
                    arguments,
                    new List<string>() {
                        "/server"
                    });
            }
            catch (Exception e)
            {
                Console.WriteLine($"[x] Error: {e.Message}");
                return;
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

            var procedures = new Dictionary<string, string>();

            // I am confused about why it is necessary to perform this step as a separate procedure
            // But it seems in-line impersonation doesn't work properly
            if (!String.IsNullOrEmpty(argumentSet.impersonate))
            {
                Console.WriteLine("[*] Attempting impersonation as {0}", argumentSet.impersonate);
                SQLExecutor.ExecuteProcedure(connection, "", argumentSet.impersonate);
            }

            procedures.Add("Enabling RPC..", $"EXEC sp_serveroption '{argumentSet.target}', 'rpc', 'true'; EXEC sp_serveroption '{argumentSet.target}', 'rpc out', 'true';");

            foreach (string step in procedures.Keys)
            {
                Console.WriteLine("[*] {0}", step);
                if (String.IsNullOrEmpty(argumentSet.intermediate))
                {
                    SQLExecutor.ExecuteProcedure(
                        connection,
                        procedures[step],
                        argumentSet.impersonate
                        );
                }
                else 
                {
                    // This may appear strange, but when we perform this kind of procedure, 
                    // we're not on the target server itself, but on an adjacent server
                    SQLExecutor.ExecuteLinkedProcedure(
                        connection, 
                        procedures[step], 
                        argumentSet.intermediate,
                        argumentSet.impersonate,
                        argumentSet.impersonate_intermediate
                        );
                }
            }

            connection.Close();
        }
    }
}
