# PowerShell Constrained Language Mode Bypass

This will build an executable which executes a Full Language Mode powershell session even when Constrained Language Mode is enabled. At the time of writing, the only bypass methods I have found are downgrading to PowerShell version 2 or using Runspaces from .Net. PowerShell version 2 is not commonly available now, and Runspaces do not natively provide an interactive interface. This method will provide a full powershell session just like running `powershell.exe`, but will *always* be in Full Language Mode.

This is accomplished by doing the following:

1. We reflectively load the internal `SystemPolicy` class within `System.Management.Automation`
2. We ensure the static method `GetSystemLockdownPolicy` has been compiled by the JIT engine.
3. We retrieve a function pointer for the compiled method.
4. We utilize VirtualProtect to ensure the function code is writable.
5. We overwrite the method with the stub `xor rax,rax; ret`. This effectively forces `GetSystemLockdownPolicy` to return `SystemEnforcementMode.None`.
6. We utilize the `Microsoft.PowerShell.ConsoleShell` module to load an interactive PowerShell session within this process.

We also implement a method similar to the `rasta-mouse` AMSI Bypass to ensure the new shell is not scanned by AMSI.

It's worth noting that this will not spawn `powershell.exe`. The PowerShell prompt and interpreter are run from memory in the current process.

## Executing a FLM Shell under AppControl

If `AppControl` is enabled, you can use the well known `InstallUtil` method. This project supports being loaded by `InstallUtil`. Simply place the binary in a safe directory (`C:\Windows\Tasks\` is a common safe directory) and run the following:

```batch
REM find `InstallUtil`
dir \Windows\Microsoft.NET\* /s/b | findstr InstallUtil.exe$
REM Run the FLM powershell session
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\InstallUtil.exe /logfile= /LogToConsole=false /U "C:\Windows\Tasks\bypass-clm.exe"
```