using CheeseSQL.Commands;
using System;
using System.Collections.Generic;
using System.DirectoryServices;
using System.Linq;

namespace CheeseSQL
{

    public class findspn : ICommand
    {
        public static string CommandName => "findspn";
        public string Description()
        {
            return $"Find MSSQL Instances, using Domain SPNs";
        }

        public string Usage()
        {
            return $@"{Description()} 
Optional arguments:
  /ldapPath:LDAP                   Specify the LDAP Path for the search
  /account:ACCOUTN                 Specify an LDAP account filter for the search
  /computer                        If set, consider the account filter as a Machine account";
        }
 
        public void Execute(Dictionary<string, string> arguments)
        {
            
            string logonServer = Environment.GetEnvironmentVariable("logonserver");
            if (string.IsNullOrEmpty(logonServer)) {
                Console.WriteLine("[-] Unable to find a logon server. Ensure you are in a Domain context");
                return;
            }
            var domainController = string.Format("LDAP://{0}", logonServer.Replace("\\", string.Empty));
            string distinguishedName;
            DirectoryEntry directoryEntry;
            string spnFilter = string.Empty;
            SearchResultCollection resultCollection;

            string _filter = null;

            string ldapPath = null;
            arguments.TryGetValue("/ldapPath", out ldapPath);
            arguments.TryGetValue("/account", out _filter);
        
            if (!String.IsNullOrEmpty(_filter) && arguments.ContainsKey("/computer"))
            {
                spnFilter = GetComputerAccountFilter(_filter);
            }
            else if (!String.IsNullOrEmpty(_filter))
            {
                spnFilter = GetDomainAccountFilter(_filter);
            }

            string filter = string.Format("(&(servicePrincipalName={0}){1})", "MSSQL*", spnFilter);


            try
            {
                directoryEntry = new DirectoryEntry(domainController);
                distinguishedName = (string)directoryEntry.Properties["distinguishedName"].Value;
                if (!string.IsNullOrEmpty(ldapPath))
                {
                    ldapPath = string.Format("/{0},{1}", ldapPath, distinguishedName);
                    directoryEntry = new DirectoryEntry(domainController + ldapPath);
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("[-] Error: {0}, {1}", domainController, ex.Message);
                return;
            }

            var directorySearcher = new DirectorySearcher(directoryEntry)
            {
                SizeLimit = 10,
                Filter = filter,
                SearchScope = SearchScope.Subtree
            };

            try
            {
                resultCollection = directorySearcher.FindAll();
            }
            catch (Exception ex)
            {
                if (ex is InvalidOperationException)
                    Console.WriteLine("{0} : Invalid Operation Exception Occured: {1}", domainController, ex.Message);
                else if (ex is NotSupportedException)
                    Console.WriteLine("{0} : Not Supported Exception Occured: {1}", domainController, ex.Message);
                else
                    Console.WriteLine("{0} : {1}", domainController, ex.Message);
                return;
            }
            // Print found MSSQL instances
            ParseCollection(resultCollection);

        }

        protected string GetDomainAccountFilter(string accountName)
        {
            return string.Format("(objectcategory=person)(SamAccountName={0})", accountName);
        }

        protected string GetComputerAccountFilter(string accountName)
        {
            return string.Format("(objectcategory=computer)(SamAccountName={0}$)", accountName);
        }

        internal bool ParseCollection(SearchResultCollection resultCollection)
        {
            Console.WriteLine("SPNs Returned : {0}", resultCollection.Count);
            foreach (SearchResult item in resultCollection)
            {
                foreach (string spn in item.Properties["ServicePrincipalName"])
                {
                    string spnService = spn.Split(new string[] { "/" }, StringSplitOptions.RemoveEmptyEntries).First();
                    if (!spnService.Contains("MSSQL"))
                        continue;

                    string spnServer = spn.Split(new string[] { "/" }, StringSplitOptions.RemoveEmptyEntries).Last()
                        .Split(new string[] { ":" }, StringSplitOptions.RemoveEmptyEntries).First()
                        .Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries).First();

                    string instance = spn.Split(new string[] { ":" }, StringSplitOptions.RemoveEmptyEntries).LastOrDefault();

                    int port = 0;
                    string serverInstance = spn.Split(new string[] { "/" }, StringSplitOptions.RemoveEmptyEntries).Last()
                        .Replace(':', int.TryParse(instance, out port) ? ',' : '\\');

                    DateTime lastLogon = DateTime.MinValue;

                    if (null != item.Properties["lastlogontimestamp"])
                    {
                        if (item.Properties["lastlogontimestamp"].Count > 0)
                        {
                            lastLogon = DateTime.FromFileTime((long)item.Properties["lastlogontimestamp"][0]);
                        }
                    }
                    string samAccountName = "";
                    if (null != item.Properties["samaccountname"])
                    {
                        if (item.Properties["samaccountname"].Count > 0)
                        {
                            samAccountName = item.Properties["samaccountname"][0].ToString();
                        }
                    }

                    string userCN = "";
                    if (null != item.Properties["cn"])
                    {
                        if (item.Properties["cn"].Count > 0)
                        {
                            samAccountName = item.Properties["cn"][0].ToString();
                        }
                    }

                    string description = "";
                    if (null != item.Properties["description"])
                    {
                        if (item.Properties["description"].Count > 0)
                        {
                            description = item.Properties["description"][0].ToString();
                        }
                    }

                    string userSid = "";
                    if (null != item.Properties["objectsid"])
                    {
                        if (item.Properties["objectsid"].Count > 0)
                        {
                            if (item.Properties["objectsid"][0].GetType().Equals(typeof(byte[])))
                            {
                                userSid = BitConverter.ToString((byte[])item.Properties["objectsid"][0]).Replace("-", "");
                            }
                            else if (item.Properties["objectsid"][0].GetType().Equals(typeof(string)))
                            {
                                userSid = item.Properties["objectsid"][0].ToString();
                            }
                        }
                    }


                    Console.Write($@"
SPN:            {spn}
ServerInstance: {serverInstance}
Server:         {spnServer}
Service:        {spnService}
UserSid:        {userSid}
User:           {samAccountName}
UserCN:         {userCN}
LastLogon:      {lastLogon}
Description:    {description}
 ---------------------------------
                ");
                }
            }
            return true;
        }
    }
}
