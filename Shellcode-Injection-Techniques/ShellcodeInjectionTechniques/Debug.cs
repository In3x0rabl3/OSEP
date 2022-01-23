using System;

namespace ShellcodeInjectionTechniques
{
    class Debugger
    {

        public static void Debug(string text, string[] args)
        {
#if DEBUG
            Console.WriteLine(text, args);
#endif
        }

        public static void Debug(string text)
        {
            Debug(text, null);
        }
    }
}
