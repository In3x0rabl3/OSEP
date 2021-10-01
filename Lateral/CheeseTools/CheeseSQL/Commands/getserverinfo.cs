using CheeseSQL.Helpers;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;

namespace CheeseSQL.Commands
{
    public class getserverinfo : ICommand
    {
        public static string CommandName => "getserverinfo";
        public string Description()
        {
            return $"Retrieve current values of 'xp_cmdshell', 'ole automation procedures' and 'clr enabled'";
        }

        public string Usage()
        {
            return $@"{Description()} 
Required arguments:
  /server:SERVER                   Server to connect to

Optional arguments:
  /target:TARGET                   Specify a linked SQL server as the target
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

            // I am confused about why it is necessary to perform this step as a separate procedure
            // But it seems in-line impersonation doesn't work properly
            if (!String.IsNullOrEmpty(argumentSet.impersonate))
            {
                Console.WriteLine("[*] Attempting impersonation as {0}", argumentSet.impersonate);
                SQLExecutor.ExecuteProcedure(connection, "", argumentSet.impersonate);
            }

            var configurations = new string[] {
                "show advanced options",
                "xp_cmdshell",
                "ole automation procedures",
                "clr enabled",
                "clr strict security",
            };

            var queries = new List<string>();
            queries.Add("SELECT name FROM sys.configurations WHERE name = '{0}'");
            queries.Add("SELECT value FROM sys.configurations WHERE name = '{0}'");
            queries.Add("SELECT value_in_use FROM sys.configurations WHERE name = '{0}'");

            foreach (string config in configurations)
            {
                Console.WriteLine("[*] Checking {0} settings on {1}..", config, String.IsNullOrEmpty(argumentSet.target) ? argumentSet.connectserver : argumentSet.target);
                foreach (string query in queries)
                {
                    if (string.IsNullOrEmpty(argumentSet.target) && string.IsNullOrEmpty(argumentSet.intermediate))
                    {
                        SQLExecutor.ExecuteQuery(
                            connection,
                            String.Format(query, config),
                            argumentSet.impersonate
                            );
                    }
                    else if (string.IsNullOrEmpty(argumentSet.intermediate))
                    {
                        SQLExecutor.ExecuteLinkedQuery(
                            connection, 
                            String.Format(query, config), 
                            argumentSet.target, 
                            argumentSet.impersonate, 
                            argumentSet.impersonate_linked
                            );
                    }
                    else
                    {
                        SQLExecutor.ExecuteDoublyLinkedQuery(
                            connection, 
                            String.Format(query, config), 
                            argumentSet.target,
                            argumentSet.intermediate,
                            argumentSet.impersonate,
                            argumentSet.impersonate_linked,
                            argumentSet.impersonate_intermediate
                            );
                    }
                }
                Console.WriteLine(" -----------------------------------");
            }
            connection.Close();

        }
    }


}
