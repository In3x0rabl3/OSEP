#### 27. Using .NET in Powershell Part 1

- Loaded ```assemblies``` in ```Powershell``` session

```PowerShell
PS C:\> [AppDomain]::CurrentDomain.GetAssemblies()

GAC    Version        Location
---    -------        --------
True   v2.0.50727     C:\Windows\Microsoft.NET\Framework\v2.0.50727\mscorlib.dll
True   v2.0.50727     C:\Windows\assembly\GAC_MSIL\Microsoft.PowerShell.ConsoleHost\1.0.0.0__31bf3856ad364e35\Micros...
True   v2.0.50727     C:\Windows\assembly\GAC_MSIL\System\2.0.0.0__b77a5c561934e089\System.dll
True   v2.0.50727     C:\Windows\assembly\GAC_MSIL\System.Management.Automation\1.0.0.0__31bf3856ad364e35\System.Man...
True   v2.0.50727     C:\Windows\assembly\GAC_MSIL\Microsoft.PowerShell.Commands.Diagnostics\1.0.0.0__31bf3856ad364e...
True   v2.0.50727     C:\Windows\assembly\GAC_MSIL\System.Core\3.5.0.0__b77a5c561934e089\System.Core.dll
True   v2.0.50727     C:\Windows\assembly\GAC_MSIL\System.Configuration.Install\2.0.0.0__b03f5f7f11d50a3a\System.Con...
True   v2.0.50727     C:\Windows\assembly\GAC_MSIL\Microsoft.WSMan.Management\1.0.0.0__31bf3856ad364e35\Microsoft.WS...
True   v2.0.50727     C:\Windows\assembly\GAC_32\System.Transactions\2.0.0.0__b77a5c561934e089\System.Transactions.dll
True   v2.0.50727     C:\Windows\assembly\GAC_MSIL\Microsoft.PowerShell.Commands.Utility\1.0.0.0__31bf3856ad364e35\M...
True   v2.0.50727     C:\Windows\assembly\GAC_MSIL\Microsoft.PowerShell.Commands.Management\1.0.0.0__31bf3856ad364e3...
True   v2.0.50727     C:\Windows\assembly\GAC_MSIL\Microsoft.PowerShell.Security\1.0.0.0__31bf3856ad364e35\Microsoft...
True   v2.0.50727     C:\Windows\assembly\GAC_MSIL\System.Xml\2.0.0.0__b77a5c561934e089\System.Xml.dll
True   v2.0.50727     C:\Windows\assembly\GAC_MSIL\System.Management\2.0.0.0__b03f5f7f11d50a3a\System.Management.dll
True   v2.0.50727     C:\Windows\assembly\GAC_MSIL\System.DirectoryServices\2.0.0.0__b03f5f7f11d50a3a\System.Directo...
True   v2.0.50727     C:\Windows\assembly\GAC_32\System.Data\2.0.0.0__b77a5c561934e089\System.Data.dll

PS C:\>
```

- Get the ```type``` of the ```Assembly```

```PowerShell
PS C:\> [AppDomain]::CurrentDomain.GetAssemblies() | ForEach-Object {$_.GetType()}

IsPublic IsSerial Name                                     BaseType
-------- -------- ----                                     --------
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object

PS C:\>
```

- ```Assemblies``` where ```IsPublic``` is ```True```

```PowerShell
PS C:\> [AppDomain]::CurrentDomain.GetAssemblies() | ForEach-Object {$_.GetType()} | Where-Object {$_.IsPublic -eq "True"}

IsPublic IsSerial Name                                     BaseType
-------- -------- ----                                     --------
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object
True     True     Assembly                                 System.Object

PS C:\>
```

- Use ```.Net``` class to print ```processes``` on the ```Machine```

```PowerShell
PS C:\> $Classes =  [AppDomain]::CurrentDomain.GetAssemblies() | ForEach-Object {$_.GetType()} | Where-Object {$_.IsPublic -eq "True"}
```

```PowerShell
PS C:\> $Classes | Where-Object {$_.Name -eq "Process"}
```

```PowerShell
PS C:\> $ProcClass = $Classes | Where-Object { $_.Name -eq "Process" }
```

List ```methods``` / ```properties``` of an object

```PowerShell
PS C:\> $ProcClass | Get-Member
```

```PowerShell
PS C:\> $ProcClass | Get-Member -MemberType Method
```

```PowerShell
PS C:\> $ProcClass | Get-Member -MemberType Method -Static
```

```PowerShell
PS C:\> $ProcClass::GetCurrentProcess()
```

```PowerShell
PS C:\> $ProcClass.FullName
System.Diagnostics.Process
PS C:\>
```

```PowerShell
PS C:\> [System.Diagnostics.Process]::GetCurrentProcess()
```

```PowerShell
PS C:\> [System.Diagnostics.Process]::GetProcesses()
```

```PowerShell
PS C:\> $ProcClass | Get-Member | Format-List *
```