using CheeseSQL.Helpers;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;


namespace CheeseSQL.Commands
{
    public class getlogin : ICommand
    {
        public static string CommandName => "getlogin";

        public string Description()
        {
            return $"Retrieve SQL Logins Available for Impersonation";
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

            var queries = new List<string>();

            queries.Add("SELECT SYSTEM_USER as 'Logged in as', CURRENT_USER as 'Mapped as';");
            queries.Add("SELECT distinct b.name AS 'Login that can be impersonated' FROM sys.server_permissions a INNER JOIN sys.server_principals b ON a.grantor_principal_id = b.principal_id WHERE a.permission_name = 'IMPERSONATE';");
            queries.Add("SELECT name as 'Owner that can be impersonated', db as 'Trustworthy DB' FROM (SELECT distinct b.name FROM sys.server_permissions a INNER JOIN sys.server_principals b ON a.grantor_principal_id = b.principal_id WHERE a.permission_name = 'IMPERSONATE') impersonable LEFT JOIN (select name AS db, suser_sname( owner_sid ) as owner, is_trustworthy_on from sys.databases) owners ON owners.owner = impersonable.name WHERE is_trustworthy_on = 1;");

            foreach (string query in queries)
            {
                if (String.IsNullOrEmpty(argumentSet.target) && String.IsNullOrEmpty(argumentSet.intermediate)) 
                {
                    SQLExecutor.ExecuteQuery(
                        connection, 
                        query, 
                        argumentSet.impersonate
                        );
                } else if (String.IsNullOrEmpty(argumentSet.intermediate)) 
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
            }

            connection.Close();
        }
    }
}
