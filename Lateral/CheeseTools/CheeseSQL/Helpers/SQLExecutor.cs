using System;
using System.Collections.Generic;
using System.Data.SqlClient;

namespace CheeseSQL.Helpers
{
    /**
      WARNING: This class is currently in development, to try reducing code duplication when executing SQL statements
               It's usage has been mildly tested and seem to "work", but   
     */
    public class SQLExecutor
    {
        public static string FixBaseCmd(string baseCmd)
        {
            baseCmd = baseCmd.Replace("'", "''");
            if (baseCmd.Trim().StartsWith("DROP") || baseCmd.Trim().StartsWith("CREATE") || baseCmd.Trim().StartsWith("DECLARE"))
            {
                baseCmd = $"EXECUTE(''{baseCmd.Replace("'", "''")}'')";
            }

            if (!baseCmd.Trim().StartsWith("EXEC"))
            {
                baseCmd = $"EXEC {baseCmd}";
            }

            return baseCmd;
        }
        public static string FixBaseQuery(string baseCmd)
        {
            return baseCmd.Replace("'", "''");
        }

        public static void ConnectionInfo(Dictionary<string, string> arguments, string connectserver, string database, bool sqlauth, out string connectInfo)
        {
            string user = String.Empty;
            string password = String.Empty;
            connectInfo = String.Empty;

            if (sqlauth)
            {
                if (arguments.ContainsKey("/user"))
                {
                    user = arguments["/user"];
                }
                if (arguments.ContainsKey("/password"))
                {
                    password = arguments["/password"];
                }
                if (String.IsNullOrEmpty(user))
                {
                    Console.WriteLine("\r\n[X] You must supply the SQL account user!\r\n");
                    ;
                }
                if (String.IsNullOrEmpty(password))
                {
                    Console.WriteLine("\r\n[X] You must supply the SQL account password!\r\n");
                }
                connectInfo = "Data Source= " + connectserver + "; Initial Catalog= " + database + "; User ID=" + user + "; Password=" + password;
            }
            else
            {
                connectInfo = "Server = " + connectserver + "; Database = " + database + "; Integrated Security = True;";
            }
        }

        public static bool Authenticate(string connectInfo, out SqlConnection connection)
        {
            connection = new SqlConnection(connectInfo);
            try
            {
                connection.Open();
                Console.WriteLine($"[+] Authentication succeeded!");
                return true;
            }
            catch
            {
                Console.WriteLine($"[-] Authentication failed.");
                return false;
            }

        }

        public static string PrepareSimpleStatement(string statement, string impersonate) {
            if (!String.IsNullOrEmpty(impersonate)) {
                statement = $"EXECUTE AS LOGIN = '{impersonate}' {statement}";
            }
            return statement;
        }
        
        public static void ExecuteProcedure(SqlConnection connection, string procedure, string impersonate, bool separator = false)
        {
            TrySqlExecute(connection, PrepareSimpleStatement(procedure, impersonate), separator);
        }

        public static void ExecuteQuery(SqlConnection connection, string query, string impersonate, bool separator = false)
        {
            TrySqlExecute(connection, PrepareSimpleStatement(query, impersonate), separator);
        }

        public static string PrepareLinkedQuery(string baseQuery, string target, string impersonate, string impersonate_linked)
        {
            baseQuery = FixBaseQuery(baseQuery);

            string query = $"SELECT * FROM OPENQUERY(\"{target}\", '{baseQuery}')";

            if (!String.IsNullOrEmpty(impersonate_linked))
            {
                query = $"SELECT * FROM OPENQUERY(\"{target}\", 'EXECUTE AS LOGIN = ''{impersonate_linked}'' {baseQuery}')";
            }


            if (!String.IsNullOrEmpty(impersonate))
            {
                query = $"EXECUTE AS LOGIN = '{impersonate}'; {query}";
            }
            return query;
        }
        public static void ExecuteLinkedQuery(SqlConnection connection, string baseQuery, string target, string impersonate, string impersonate_linked, bool separator = false)
        {

            string query = PrepareLinkedQuery(baseQuery, target, impersonate, impersonate_linked);
            TrySqlExecute(connection, query, separator);

        }
        public static string PrepareDoublyLinkedQuery(string baseQuery, string target, string intermediate, string impersonate, string impersonate_linked, string impersonate_intermediate)
        {
            string query = baseQuery;

            if (!String.IsNullOrEmpty(impersonate_linked))
            {
                query = $"EXECUTE AS LOGIN = '{impersonate_linked}' {query}";
            }

            query = FixBaseQuery(baseQuery);
            query = $"SELECT * FROM OPENQUERY(\"{target}\", '{query}')";


            if (!String.IsNullOrEmpty(impersonate_intermediate))
            {
                query = $"EXECUTE AS LOGIN = '{impersonate_intermediate}' {query}";
            }

            query = FixBaseQuery(query);
            query = $"SELECT * FROM OPENQUERY(\"{intermediate}\", '{query}')";

            if (!String.IsNullOrEmpty(impersonate))
            {
                query = $"EXECUTE AS LOGIN = '{impersonate}' {query}";
            }

            return query;
        }        
        
        public static void ExecuteDoublyLinkedQuery(SqlConnection connection, string baseQuery, string target, string intermediate, string impersonate, string impersonate_linked, string impersonate_intermediate, bool separator = false)
        {

            string query = PrepareDoublyLinkedQuery(baseQuery, target, intermediate, impersonate, impersonate_linked, impersonate_intermediate);
            TrySqlExecute(connection, query, separator);

        }

        public static void ExecuteLinkedProcedure(SqlConnection connection, string baseCmd, string target, string impersonate, string impersonate_linked, bool separator = false)
        {

            baseCmd = FixBaseCmd(baseCmd);

            string procedure = $"EXEC ('{baseCmd}') AT [{target}]";
            if (!String.IsNullOrEmpty(impersonate_linked))
            {
                procedure = $"EXEC('EXECUTE AS LOGIN = ''{impersonate_linked}'' {baseCmd}') AT [{target}]";
            }

            if (!String.IsNullOrEmpty(impersonate))
            {
                procedure = $"EXECUTE AS LOGIN = '{impersonate}' {procedure}";
            }
            TrySqlExecute(connection, procedure, separator);
        }

        public static void ExecuteDoubleLinkedProcedure(SqlConnection connection, string baseCmd, string target, string intermediate, string impersonate, string impersonate_linked, string impersonate_intermediate, bool separator = false)
        {

            baseCmd = FixBaseCmd(baseCmd);
            baseCmd = FixBaseCmd(baseCmd);

            string procedure = $"EXEC ('EXEC (''{baseCmd}'') AT [{target}]') AT [{intermediate}]";

            if (!String.IsNullOrEmpty(impersonate_linked) && !String.IsNullOrEmpty(impersonate_intermediate))
            {
                procedure = $"EXEC ('EXECUTE AS LOGIN = ''{impersonate_intermediate}'' EXEC (''EXECUTE AS LOGIN = ''''{impersonate_linked}'''' {baseCmd}'') AT [{target}]') AT [{intermediate}]";
            }
            else if (!String.IsNullOrEmpty(impersonate_linked))
            {
                procedure = $"EXEC ('EXEC (''EXECUTE AS LOGIN = ''''{impersonate_linked}'''' {baseCmd}'') AT [{target}]') AT [{intermediate}]";
            }
            else if (!String.IsNullOrEmpty(impersonate_intermediate))
            {
                procedure = $"EXEC ('EXECUTE AS LOGIN = ''{impersonate_intermediate}'' EXEC (''{baseCmd}'') AT [{target}]') AT [{intermediate}]";
            }

            if (!String.IsNullOrEmpty(impersonate))
            {
                procedure = $"EXECUTE AS LOGIN = '{impersonate}' {procedure}";
            }
            TrySqlExecute(connection, procedure, separator);
        }

        public static void TrySqlExecute(SqlConnection connection, string procedure, bool separator)
        {
            
            try
            {
                SqlCommand command = new SqlCommand(procedure, connection);
                using (SqlDataReader reader = command.ExecuteReader())
                {
                    try
                    {

                        while (reader.Read())
                        {
                            if (reader.FieldCount == 0) { break; }
                            else
                            {
                                int written = 0;
                                string msg = String.Empty;

                                for (var i = 0; i < reader.FieldCount; i++)
                                {
                                    string name = reader.GetName(i);

                                    string value;
                                    if (reader.GetFieldType(i) == typeof(bool))
                                    {
                                        value = reader.GetBoolean(i).ToString();
                                    }
                                    else if (reader.GetFieldType(i) == typeof(Int32))
                                    {
                                        value = reader.GetInt32(i).ToString();
                                    }
                                    else if (reader.GetFieldType(i) == typeof(String))
                                    {
                                        value = reader.GetString(i);
                                    }
                                    else
                                    {
                                        value = reader.GetValue(i).ToString();
                                    }
                                    msg = (written == 0) ?
                                        String.Format("[+] {0:-15}: {1}", name, value) :
                                        String.Format("    {0:-15}: {1}", name, value);
                                    Console.WriteLine(msg);
                                    written++;
                                }
                                if (written > 1 && separator) {
                                    Console.WriteLine("   {0}", new String('-', 40));
                                }
                                written = 0;
                            }
                        }

                    }
                    catch (Exception e){ Console.WriteLine(e); }
                }
            }
            catch (SqlException e)
            {
                if (e.Message.Contains("Execution Timeout Expired"))
                {
                    Console.WriteLine("[*] The SQL Query hit the timeout. If you were executing a reverse shell, this is normal");
                    connection.Open();
                }
                else if (e.Message.Contains("Could not find server"))
                {
                    throw new Exception("Couldn't connect to linked server. Check the spelling");
                }
                else
                {
                    Console.WriteLine($"[-] Exception: {e.Message}");
                    return;
                }
            }
        }
    }
}

