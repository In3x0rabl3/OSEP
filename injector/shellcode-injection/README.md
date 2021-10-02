# shellcode-injection
> Warning: The PoCs in this repository were not created with evading AV in mind. It's more like a reference for me using the Win32 API. If you try to compile and run any of these programs on a modern Windows machine with Defender running, don't be confused if they get deleted instantly.

Compile using the C# compiler
```CMD
C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe <Program>.cs
```

## FormatShellcode
Helper class to print the shellcode.
Expects to have a shellcode.bin file present (generate with MSFvenom: _-f raw -o shellcode.bin_)

Execute it:
```CMD
FormatShellcode.exe shellcode.bin
```

## InjectLocalProcess
Injects the shellcode into the current process.

Execute it:
```CMD
InjectLocalProcess.exe
```

## InjectRemoteProcess
Injects the shellcode in a remote process.

> The process has to have at least the same privileges as the current user executing (eg. non-administrative shells cannot inject into process owned by NT\SYSTEM).

Execute it:
```CMD
InjectRemoteProcess.exe <ProcessName>
```

## PSInject
Simple PowerShell PoC for local process injection. Since PowerShell leverages the .NET framework, you can re-write every C# code using PowerShell.
