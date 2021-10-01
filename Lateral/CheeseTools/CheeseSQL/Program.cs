using CheeseSQL.Helpers;
using System;
using System.Collections.Generic;
using System.IO;

namespace CheeseSQL
{
    public class Program
    {
        private static void FileExecute(string commandName, Dictionary<string, string> parsedArgs)
        {
            // Execute with stdout/stderr redirected to a file
            string file = parsedArgs["/consoleoutfile"];

            TextWriter realStdOut = Console.Out;
            TextWriter realStdErr = Console.Error;

            using (StreamWriter writer = new StreamWriter(file, true))
            {
                writer.AutoFlush = true;
                Console.SetOut(writer);
                Console.SetError(writer);

                MainExecute(commandName, parsedArgs);

                Console.Out.Flush();
                Console.Error.Flush();
            }
            Console.SetOut(realStdOut);
            Console.SetError(realStdErr);
        }

        private static void MainExecute(string commandName, Dictionary<string, string> parsedArgs)
        {
            Info.ShowLogo();

            try
            {
                var commandFound = new CommandCollection().ExecuteCommand(commandName, parsedArgs);

                // Show usage - If no commands were found
                if (commandFound == false)
                    Info.ShowUsage();
            }
            catch (Exception e)
            {
                Console.WriteLine("\r\n[!] Unhandled SharpSQL exception:\r\n");
                Console.WriteLine(e);
            }
        }

        public static string MainString(string command)
        {
            // Helper that executes an input string command and returns results
            string[] args = command.Split();

            var parsed = ArgParser.Parse(args);
            if (parsed.ParsedOk == false)
            {
                Info.ShowLogo();
                Info.ShowUsage();
                return $"Error parsing arguments: {command}";
            }

            var commandName = args.Length != 0 ? args[0] : "";

            TextWriter realStdOut = Console.Out;
            TextWriter realStdErr = Console.Error;
            TextWriter stdOutWriter = new StringWriter();
            TextWriter stdErrWriter = new StringWriter();
            Console.SetOut(stdOutWriter);
            Console.SetError(stdErrWriter);

            MainExecute(commandName, parsed.Arguments);

            Console.Out.Flush();
            Console.Error.Flush();
            Console.SetOut(realStdOut);
            Console.SetError(realStdErr);

            string output = "";
            output += stdOutWriter.ToString();
            output += stdErrWriter.ToString();

            return output;
        }

        public static void Main(string[] args)
        {
            // Parse the command line arguments - Show usage on failure
            var parsed = ArgParser.Parse(args);
            if (parsed.ParsedOk == false)
            {
                Info.ShowLogo();
                Info.ShowUsage();
                return;
            }

            var commandName = args.Length != 0 ? args[0] : "";

            if (parsed.Arguments.ContainsKey("/consoleoutfile"))
            {
                // Redirect output to a file specified
                FileExecute(commandName, parsed.Arguments);
            }
            else
            {
                MainExecute(commandName, parsed.Arguments);
            }
        }
    }
}
