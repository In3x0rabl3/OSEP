using CheeseSQL.Helpers;
using System.Collections.Generic;

namespace CheeseSQL.Commands
{
    public interface ICommand
    {
        void Execute(Dictionary<string, string> arguments);
        string Description();
        string Usage();
    }
}