using System;
using System.ServiceProcess;
using System.Text.RegularExpressions;
using System.Threading;
using static CheeseExec.NativeMethods;


namespace CheeseExec
{
    internal static class SimplePathValidator
    {
        public static bool IsValidPath(string path)
        {
            var r = new Regex(
                @"^(([a-zA-Z]:|\\\\\w[ \w\.]*)(\\\w*[ \w\.]*|\\+%[ \w\.]+%+)+|%[ \w\.]+%(\\\w[ \w\.]*|\\%[ \w\.]+%+)*)");
            return r.IsMatch(path);
        }
    }

    public class ServiceExecutor
    {
        private string _binPath;
        private IntPtr _svc;
        private IntPtr _svcman;

        public ServiceExecutor(string target, string serviceName, string binPath)
        {
            Target = target;
            ServiceName = ServiceDisplayName = serviceName;
            ServiceExecutable = binPath;
            SvcManager = IntPtr.Zero;
            Service = IntPtr.Zero;
            CallSvcManager();
            //GetServiceHandle();
        }


        public SERVICE_STATUS ServiceStatus { get; set; }

        public IntPtr SvcManager
        {
            get => _svcman;
            set
            {
                if (value != null) _svcman = value;
            }
        }

        public IntPtr Service
        {
            get => _svc;
            set
            {
                if (value != null) _svc = value;
            }
        }

        public string ServiceName { get; set; }

        public string ServiceDisplayName { get; set; }

        public string ServiceExecutable
        {
            get => _binPath;
            set
            {
                if (SimplePathValidator.IsValidPath(value)) _binPath = value;
            }
        }

        public string Target { get; set; }


        public void CallSvcManager()
        {
            if (Target != null && Target != "")
                SvcManager = OpenSCManager(Target, null, SCM_ACCESS.SC_MANAGER_ALL_ACCESS);
        }

        public bool Create()
        {
            if (SvcManager == IntPtr.Zero) CallSvcManager();
            Service = CreateService(SvcManager, ServiceName, ServiceDisplayName, SERVICE_ACCESS.SERVICE_ALL_ACCESS,
                SERVICE_TYPE.SERVICE_WIN32_OWN_PROCESS, SERVICE_START.SERVICE_DEMAND_START,
                SERVICE_ERROR.SERVICE_ERROR_NORMAL, ServiceExecutable, null, null, null, null, null);
            Console.WriteLine($"[+] Service Pointer: {Service.ToString()}");
            return Service != IntPtr.Zero;
        }


        public bool Restart()
        {
            var checkpoint = false;

            checkpoint = Stop();
            if (checkpoint)
            {
                Start();
            }

            return IsRunning();
        }

        public bool Start()
        {
            var checkpoint = false;
            if (SvcManager == IntPtr.Zero) CallSvcManager();
            if (Service == IntPtr.Zero)
                try
                {
                    GetServiceHandle();
                }
                catch
                {
                    Console.WriteLine($"[-] Unknown Service: {ServiceName}");
                    Console.WriteLine($"[*] Creating Service: {ServiceName}");
                    checkpoint = Create();
                }

            if (checkpoint)
            {
                StartService(Service, 0, null);
                Wait();
            }

            return IsRunning();
        }

        public bool Stop()
        {
            if (SvcManager == IntPtr.Zero) CallSvcManager();
            if (Service == IntPtr.Zero) GetServiceHandle();

            var status = new SERVICE_STATUS();
            var hResult = ControlService(Service, SERVICE_CONTROL.STOP, ref status);
            ServiceStatus = status;
            Wait();
            return IsStopped();
        }

        public bool Delete()
        {
            if (SvcManager == IntPtr.Zero) CallSvcManager();
            if (Service == IntPtr.Zero) GetServiceHandle();
            if (IsRunning())
            {
                Console.WriteLine($"[-] Service {ServiceName} running! Stopping...");
                Stop();
                // Potentially Dangerous Operation (Infinite Loop)
                var attempts = 3;
                while (!IsStopped(true) && attempts > 0)
                {
                    Wait();
                    attempts -= 1;
                }
            }

            return DeleteService(Service);
        }

        public bool Exists()
        {
            var exists = false;
            foreach (var service in ServiceController.GetServices(Target.Replace("\\\\", "")))
                if (service.ServiceName == ServiceName)
                    exists = true;
            return exists;
        }

        public bool IsRunning()
        {
            var running = false;
            foreach (var service in ServiceController.GetServices(Target.Replace("\\\\", "")))
                if (service.ServiceName == ServiceName &&
                    (service.Status == ServiceControllerStatus.Running ||
                     service.Status == ServiceControllerStatus.StartPending))
                    running = true;
            return running;
        }

        public bool IsStopped(bool fullstop = false)
        {
            var stopped = false;
            foreach (var service in ServiceController.GetServices(Target.Replace("\\\\", "")))
                if (service.ServiceName == ServiceName &&
                    (service.Status == ServiceControllerStatus.Stopped ||
                     service.Status == ServiceControllerStatus.StopPending))
                    stopped = fullstop ? true : service.Status == ServiceControllerStatus.Stopped;
            return stopped;
        }

        public void GetServiceHandle()
        {
            if (SvcManager == IntPtr.Zero) CallSvcManager();
            if (Exists())
                try
                {
                    Service = OpenService(SvcManager, ServiceName, SERVICE_ACCESS.SERVICE_ALL_ACCESS);
                }
                catch
                {
                    throw new Exception("Cannot open service");
                }
            else
                throw new Exception($"Error:  Unknown service {ServiceName}");
        }

        public void CloseHandles()
        {
            if (SvcManager != null) CloseServiceHandle(SvcManager);
            if (Service != null) CloseServiceHandle(Service);
        }

        public void Wait()
        {
            Thread.Sleep(3000);
        }
    }

    internal class Program
    {
        private static void Main(string[] args)
        {
            var FAILED_ACCESS_MANAGER = "[x] Failed to access service manager";
            var FAILED_OPEN_SERVICE = "[x] Failed to open service";
            var FAILED_CREATE_SERVICE = "[x] Failed to create service";
            var FAILED_START_SERVICE = "[x] Failed to start service";
            var FAILED_STOP_SERVICE = "[x] Failed to stop service";
            var FAILED_DELETE_SERVICE = "[x] Failed to delete service";
            var SUCCESS_ACCESS_MANAGER = "[+] Accessed service manager";
            var SUCCESS_OPEN_SERVICE = "[+] Service handle created";
            var SUCCESS_CREATE_SERVICE = "[+] Service created";
            var SUCCESS_START_SERVICE = "[+] Service started";
            var SUCCESS_STOP_SERVICE = "[+] Service stopped";
            var SUCCESS_DELETE_SERVICE = "[+] Service deleted";

            if (args.Length < 3)
            {
                Console.WriteLine(" [x] Invalid number of arguments");
                Console.WriteLine("     Usage: CsExec.exe <targetMachine> <serviceName> <binPath> <action>");
                Console.WriteLine("     Actions: start|stop|create|delete");
                Console.WriteLine("     Actions: leave blank to perform a full sequence create|start|restart|stop|delete");
                return;
            }

            var target = $@"\\{args[0]}";
            var serviceName = args[1];
            var binPath = args[2];
            var action = args.Length < 4 ? "sequence" : args[3].ToLowerInvariant();

            try
            {
                var sex = new ServiceExecutor(target, serviceName, binPath);
                Console.WriteLine($"[+] Created Service Executor on {target}");
                Console.Write("Service Info:" +
                              $"{Environment.NewLine}\tService Name: {sex.ServiceName}" +
                              $"{Environment.NewLine}\tService Display Name: {sex.ServiceDisplayName}" +
                              $"{Environment.NewLine}\tBinPath: {sex.ServiceExecutable}" +
                              $"{Environment.NewLine}");

                if (sex.SvcManager == null || sex.SvcManager == IntPtr.Zero)
                {
                    Console.WriteLine(FAILED_ACCESS_MANAGER);
                    sex.CloseHandles();
                    return;
                }

                Console.WriteLine(SUCCESS_ACCESS_MANAGER);
                if (sex.Service == null)
                {
                    Console.WriteLine(FAILED_OPEN_SERVICE);
                    sex.CloseHandles();
                    return;
                }

                Console.WriteLine(SUCCESS_OPEN_SERVICE);

                if (action == "sequence")
                {
                    if (!sex.Create())
                    {
                        Console.WriteLine(FAILED_CREATE_SERVICE);
                        sex.CloseHandles();
                        return;
                    }

                    Console.WriteLine(SUCCESS_CREATE_SERVICE);
                    if (!sex.Start())
                    {
                        Console.WriteLine(FAILED_START_SERVICE);
                        sex.CloseHandles();
                        return;
                    }

                    Console.WriteLine(SUCCESS_START_SERVICE);
                    if (!sex.Stop())
                    {
                        Console.WriteLine(FAILED_STOP_SERVICE);
                        sex.CloseHandles();
                        return;
                    }

                    Console.WriteLine(SUCCESS_STOP_SERVICE);
                    if (!sex.Delete())
                    {
                        Console.WriteLine(FAILED_DELETE_SERVICE);
                        sex.CloseHandles();
                        return;
                    }

                    Console.WriteLine(SUCCESS_DELETE_SERVICE);
                }
                else if (action == "create")
                {
                    if (!sex.Create()) Console.WriteLine(FAILED_CREATE_SERVICE);
                    Console.WriteLine(SUCCESS_CREATE_SERVICE);
                }
                else if (action == "start")
                {
                    if (!sex.Start()) Console.WriteLine(FAILED_START_SERVICE);
                    Console.WriteLine(SUCCESS_START_SERVICE);
                }
                else if (action == "restart")
                {
                    if (!sex.Restart()) Console.WriteLine(FAILED_START_SERVICE);
                    Console.WriteLine(SUCCESS_START_SERVICE);
                }
                else if (action == "stop")
                {
                    if (!sex.Stop()) Console.WriteLine(FAILED_STOP_SERVICE);
                    Console.WriteLine(SUCCESS_STOP_SERVICE);
                }
                else if (action == "delete")
                {
                    if (!sex.Delete()) Console.WriteLine(FAILED_DELETE_SERVICE);
                    Console.WriteLine(SUCCESS_DELETE_SERVICE);
                }
                else
                {
                    Console.WriteLine("[x] Invalid Action");
                }

                sex.CloseHandles();
            }
            catch (Exception e)
            {
                Console.WriteLine("[x] {0}", e.Message);
            }
        }
    }
}