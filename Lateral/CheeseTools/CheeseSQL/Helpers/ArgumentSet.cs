using System;
using System.Collections.Generic;
using System.Diagnostics;

namespace CheeseSQL.Helpers
{
    /** The argument Set specifies the default parameters of almost any command, and populate an object with the related arguments
     */
    public class ArgumentSet
    {
        public string database;
        public string connectserver;
        public string target;
        public string intermediate;
        public string query;
        public string impersonate;
        public string impersonate_intermediate;
        public string impersonate_linked;
        public bool sqlauth;

        Dictionary<string, string> extras;

        public ArgumentSet(
            string connectserver, 
            string database, 
            string target = null, 
            string intermediate = null, 
            string impersonate = null, 
            string impersonate_intermediate = null, 
            string impersonate_linked = null,
            bool sqlauth = false,
            Dictionary<string, string> extras = null)
        {
            this.connectserver = connectserver;
            this.database = database;
            this.target = target;
            this.intermediate = intermediate;
            this.impersonate = impersonate;
            this.impersonate_intermediate = impersonate_intermediate;
            this.impersonate_linked = impersonate_linked;
            this.sqlauth = sqlauth;
            this.extras = extras;
        }

        public void GetExtraString(string key, out string value) {
            this.extras.TryGetValue(key, out value);
        }
        public void GetExtraBool(string key, out bool value) {
            value = this.extras.ContainsKey(key);
        }

        public static ArgumentSet FromDictionary(Dictionary<string, string> arguments, List<string> required = null)
        {
            if (required == null) {
                required = new List<string>() {  };
            }

            string database = "master";
            string connectserver;
            string target;
            string intermediate;
            string impersonate;
            string impersonate_intermediate;
            string impersonate_linked;

            bool sqlauth = arguments.ContainsKey("/sqlauth");

            foreach (string key in required) {
                if (!arguments.ContainsKey(key)) {
                    throw new Exception($"Argument {key} is required");
                }
            }

            if (arguments.TryGetValue("/impersonate", out impersonate)) {
                arguments.Remove("/impersonate");
            }
            if (arguments.TryGetValue("/intermediate", out intermediate)) {
                arguments.Remove("/intermediate");
            }
            if (arguments.TryGetValue("/target", out target)) {
                arguments.Remove("/target");
            }
            if (arguments.TryGetValue("/impersonate-intermediate", out impersonate_intermediate)) {
                arguments.Remove("/impersonate-intermediate");
            }
            if (arguments.TryGetValue("/impersonate-linked", out impersonate_linked)) {
                arguments.Remove("/impersonate-linked");
            }
            if (arguments.TryGetValue("/db", out database))
            {
                arguments.Remove("/db");
            }
            if (arguments.TryGetValue("/server", out connectserver))
            {
                arguments.Remove("/server");
            }

            return new ArgumentSet(connectserver, database, target, intermediate, impersonate, impersonate_intermediate, impersonate_linked, sqlauth, arguments);
        }
    }
}
