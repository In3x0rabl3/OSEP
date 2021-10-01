using CheeseSQL.Helpers;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;


namespace CheeseSQL.Commands
{
    public class openquery : ICommand
    {
        public static string CommandName => "openquery";

        public string Description()
        {
            return $"Execute an arbitrary query using 'OPENQUERY'";
        }

        public string Usage()
        {
            return $@"{Description()} 
Required arguments:
  /server:SERVER                   Server to connect to
  /target:TARGET                   Specify a linked SQL server as the target
  /query:SQL                       Query to execute

Optional arguments:
  /db:DB                           Specify an alternate database to connect 
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
            string query = "";

            ArgumentSet argumentSet;
            try
            {
                argumentSet = ArgumentSet.FromDictionary(
                    arguments,
                    new List<string>() {
                        "/server",
                        "/command",
                        "/target"
                    });
            }
            catch (Exception e)
            {
                Console.WriteLine($"[x] Error: {e.Message}");
                return;
            }

            argumentSet.GetExtraString("/query", out query);

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

            if (String.IsNullOrEmpty(argumentSet.intermediate))
            {
                SQLExecutor.ExecuteLinkedQuery(
                    connection, 
                    query,
                    argumentSet.target,
                    argumentSet.impersonate,
                    argumentSet.impersonate_linked
                    );
            }
            else 
            {
                SQLExecutor.ExecuteDoublyLinkedQuery(
                    connection, 
                    query, 
                    argumentSet.target,
                    argumentSet.intermediate,
                    argumentSet.impersonate,
                    argumentSet.impersonate_linked,
                    argumentSet.impersonate_intermediate
                    );
            }

            connection.Close();
        }
    }
}
