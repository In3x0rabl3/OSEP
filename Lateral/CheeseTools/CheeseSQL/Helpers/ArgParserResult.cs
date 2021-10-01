using System.Collections.Generic;

namespace CheeseSQL.Helpers
{
    public class ArgParserResult
    {
        public bool ParsedOk { get; }
        public Dictionary<string, string> Arguments { get; }

        private ArgParserResult(bool parsedOk, Dictionary<string, string> arguments)
        {
            ParsedOk = parsedOk;
            Arguments = arguments;
        }

        public static ArgParserResult Success(Dictionary<string, string> arguments)
            => new ArgParserResult(true, arguments);

        public static ArgParserResult Failure()
            => new ArgParserResult(false, null);

    }
}