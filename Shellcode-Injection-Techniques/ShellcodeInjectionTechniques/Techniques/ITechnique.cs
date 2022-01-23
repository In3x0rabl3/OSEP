using System;
using System.Diagnostics;

namespace ShellcodeInjectionTechniques
{
    interface ITechnique
    {
        void Run(Process target, byte[] shellcode);
    }
}
