using CheeseSQL.Helpers;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;

namespace CheeseSQL.Commands
{
    public class listdb : ICommand
    {
        public static string CommandName => "listdb";
        public string Description()
        {
            return $"List available Databases on the server";
        }

        public string Usage()
        {
            return $@"{Description()} 
Required arguments:
  /server:SERVER                   Server to connect to

Optional arguments:
  /verbose                         If set, more info on the DB
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
            string connectInfo;
            bool verbose;
            bool exclude_default;

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

            argumentSet.GetExtraBool("/verbose", out verbose);
            argumentSet.GetExtraBool("/nodefault", out exclude_default);

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

            string select = verbose ? 
                "name AS 'Database', suser_sname(owner_sid) AS 'Owner', is_trustworthy_on AS 'Trustworthy'": 
                "name AS 'Database'" ;

            string where = exclude_default ?
                "WHERE name NOT IN('master', 'tempdb', 'model', 'msdb')" :
                "";

            var queries = new List<string>();
            
            queries.Add(
                $@"SELECT {select} FROM sys.databases {where};"
             );
 
            foreach (string query in queries)
            {
                if (String.IsNullOrEmpty(argumentSet.target) && String.IsNullOrEmpty(argumentSet.intermediate))
                {
                    SQLExecutor.ExecuteQuery(
                        connection, 
                        query,
                        argumentSet.impersonate,
                        true
                        );
                }
                else if (String.IsNullOrEmpty(argumentSet.intermediate))
                {
                    SQLExecutor.ExecuteLinkedQuery(
                        connection, 
                        query, 
                        argumentSet.target, 
                        argumentSet.impersonate, 
                        argumentSet.impersonate_linked,
                        true
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
                        argumentSet.impersonate_intermediate,
                        true
                        );
                }
            }
            connection.Close();

        }
    }


}
