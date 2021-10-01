using CheeseSQL.Helpers;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;

namespace CheeseSQL.Commands
{
    public class getdbuser : ICommand
    {
        public static string CommandName => "getdbuser";
        public string Description()
        {
            return $"Retrieve Information on the SQL Login, Currently Mapped User, and Available User Roles";
        }

        public string Usage()
        {
            return $@"{Description()} 
Required arguments:
  /server:SERVER                   Server to connect to

Optional arguments:
  /permissions                     If set, print a table with full user permissions
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
            bool permissions;

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

            argumentSet.GetExtraBool("/permissions", out permissions);

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
            queries.Add("SELECT IS_SRVROLEMEMBER('public') as 'Public role';");
            queries.Add("SELECT IS_SRVROLEMEMBER('sysadmin') as 'Sysadmin role';");

            foreach (string query in queries)
            {
                if (String.IsNullOrEmpty(argumentSet.target) && String.IsNullOrEmpty(argumentSet.intermediate))
                {
                    SQLExecutor.ExecuteQuery(
                        connection, 
                        query,
                        argumentSet.impersonate);
                }
                else if (String.IsNullOrEmpty(argumentSet.intermediate))
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

            /* 
             The following query is quite difficult to wrap within my SQLExecutor, mostly due to the fact I implemented the output in tabular format
             */

            if (permissions)
            {
                Console.WriteLine("[*] Checking user permissions..");

                string query = @"SELECT *
    FROM(SELECT 'OBJECT' AS entity_class,
                NAME,
                subentity_name,
                permission_name
        FROM   sys.objects
                CROSS APPLY fn_my_permissions(QUOTENAME(NAME), 'OBJECT') a
        UNION ALL
        SELECT 'DATABASE' AS entity_class,
                NAME,
                subentity_name,
                permission_name
        FROM   sys.databases
                CROSS APPLY fn_my_permissions(QUOTENAME(NAME), 'DATABASE') a
        UNION ALL
        SELECT 'SERVER'     AS entity_class,
                @@SERVERNAME AS NAME,
                subentity_name,
                permission_name
        FROM   fn_my_permissions(NULL, 'SERVER')) p
    ORDER  BY entity_class,
            NAME";

                if (!String.IsNullOrEmpty(argumentSet.intermediate) && !String.IsNullOrEmpty(argumentSet.target))
                {
                    query = SQLExecutor.PrepareDoublyLinkedQuery(
                        query, 
                        argumentSet.target, 
                        argumentSet.intermediate, 
                        argumentSet.impersonate, 
                        argumentSet.impersonate_linked, 
                        argumentSet.impersonate_intermediate
                        );
                }
                else if (!String.IsNullOrEmpty(argumentSet.target))
                {
                    query = SQLExecutor.PrepareLinkedQuery(
                        query, 
                        argumentSet.target, 
                        argumentSet.impersonate, 
                        argumentSet.impersonate_linked
                        );
                }

                SqlCommand command = new SqlCommand(query, connection);

                TablePrinter.PrintRow("ENTITY", "NAME", "SUBENTITY", "PERMISSION");
                TablePrinter.PrintLine();
                using (SqlDataReader reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        TablePrinter.PrintRow(reader.GetString(0), reader.GetString(1), reader.GetString(2), reader.GetString(3));
                    }
                }
                TablePrinter.PrintLine();
            }
            connection.Close();

        }
    }


}
