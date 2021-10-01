#### 24. Powershell Remoting Part 5

#### Advanced PowerShell Remoting
- Using ```Invoke-Command``` ```state-fully``` across ```sessions```

```PowerShell
PS C:\Users\Administrator\Desktop> New-PSSession -ComputerName JOHN-PC -Credential John-PC\John

 Id Name            ComputerName    State         ConfigurationName     Availability
 -- ----            ------------    -----         -----------------     ------------
  7 Session7        JOHN-PC         Opened        Microsoft.PowerShell     Available


PS C:\Users\Administrator\Desktop>
```

```PowerShell
PS C:\Users\Administrator\Desktop> Get-PSSession

 Id Name            ComputerName    State         ConfigurationName     Availability
 -- ----            ------------    -----         -----------------     ------------
  7 Session7        JOHN-PC         Opened        Microsoft.PowerShell     Available


PS C:\Users\Administrator\Desktop>
```

```PowerShell
PS C:\Users\Administrator\Desktop> $sess = Get-PSSession
```

```PowerShell
PS C:\Users\Administrator\Desktop> Invoke-Command -ScriptBlock { $procs = Get-Process } -Session $sess
```

```PowerShell
PS C:\Users\Administrator\Desktop> Invoke-Command -ScriptBlock { $procs } -Session $sess

Handles  NPM(K)    PM(K)      WS(K) VM(M)   CPU(s)     Id ProcessName                                                              PSComputerName
-------  ------    -----      ----- -----   ------     -- -----------                                                              --------------
     23       2     1756       2020    30     0.00   1288 cmd                                                                      JOHN-PC
     22       2     1688       2060    30     0.01   1552 cmd                                                                      JOHN-PC
     40       3      708       3228    42     0.05   1220 conhost                                                                  JOHN-PC
     34       2      596       2664    32     0.00   3124 conhost                                                                  JOHN-PC
    417       5     1112       2300    33     0.12    352 csrss                                                                    JOHN-PC
    205       6     1220       2932    33     0.47    408 csrss                                                                    JOHN-PC
     66       3      892       2704    38     0.02    912 dwm                                                                      JOHN-PC
    789      23    24836      36064   196     2.99    696 explorer                                                                 JOHN-PC
      0       0        0         12     0               0 Idle                                                                     JOHN-PC
    731      12     3044       6840    32     1.11    492 lsass                                                                    JOHN-PC
    195       5     1628       3524    23     0.10    500 lsm                                                                      JOHN-PC
     56       3      868       4040    57     0.07   3160 notepad                                                                  JOHN-PC
    134       5     6272       4712    63     0.13   2924 python                                                                   JOHN-PC
    645      16    22040      13084   108     0.62   1664 SearchIndexer                                                            JOHN-PC
    194       7     4120       5824    35     0.74    476 services                                                                 JOHN-PC
     29       1      216        520     4     0.06    272 smss                                                                     JOHN-PC
    282       9     4356       5732    58     0.03   1356 spoolsv                                                                  JOHN-PC
    347       7     2876       6084    38     0.41    624 svchost                                                                  JOHN-PC
    256       8     2496       5120    26     0.45    736 svchost                                                                  JOHN-PC
    554      13    14144      11188    77     0.75    788 svchost                                                                  JOHN-PC
    525      13    22960      26920   101     4.31    872 svchost                                                                  JOHN-PC
   1169      30    17248      20256   116     4.56    960 svchost                                                                  JOHN-PC
    440      16     6260       9468    55     0.64   1124 svchost                                                                  JOHN-PC
    693      26    12396      12236    81     0.97   1232 svchost                                                                  JOHN-PC
    303      24     9356       9012    48     0.72   1392 svchost                                                                  JOHN-PC
    347      15     5192       8320    66     0.41   1500 svchost                                                                  JOHN-PC
    357      35   144352      18592   210    11.60   1956 svchost                                                                  JOHN-PC
    346      13     7988       9420    66     1.43   2772 svchost                                                                  JOHN-PC
     94       7     1092       3908    25     0.10   3816 svchost                                                                  JOHN-PC
    562       0       44        556     2               4 System                                                                   JOHN-PC
    138       8     1972       3976    38     0.05   1292 taskhost                                                                 JOHN-PC
    115       5     1656       3420    44     0.35    684 VBoxService                                                              JOHN-PC
    138       5     1220       3724    60     0.06   2104 VBoxTray                                                                 JOHN-PC
     74       5      780       2488    32     0.23    400 wininit                                                                  JOHN-PC
    113       4     1492       3156    39     0.27    448 winlogon                                                                 JOHN-PC
    439      15     7812       9964   107     0.58    556 wmpnetwk                                                                 JOHN-PC
    211      10    27928      36028   143     0.73   3476 wsmprovhost                                                              JOHN-PC

PS C:\Users\Administrator\Desktop>
```

- ```Implicit Remoting```

```PowerShell
PS C:\Users\Administrator\Desktop> New-PSSession -ComputerName JOHN-PC -Credential John-PC\John

 Id Name            ComputerName    State         ConfigurationName     Availability
 -- ----            ------------    -----         -----------------     ------------
  7 Session7        JOHN-PC         Opened        Microsoft.PowerShell     Available


PS C:\Users\Administrator\Desktop>
```

```PowerShell
PS C:\Users\Administrator\Desktop> Get-PSSession

 Id Name            ComputerName    State         ConfigurationName     Availability
 -- ----            ------------    -----         -----------------     ------------
  7 Session7        JOHN-PC         Opened        Microsoft.PowerShell     Available


PS C:\Users\Administrator\Desktop>
```

```PowerShell
PS C:\Users\Administrator\Desktop> $sess = Get-PSSession
```

Create a ```Get-Sysinfo``` function on the remote machine

```PowerShell
PS C:\Users\Administrator\Desktop> Invoke-Command -ScriptBlock { function Get-Sysinfo { whoami; $env:COMPUTERNAME } } -Session $sess
```

Import the ```Get-Sysinfo``` function on our local machine

```PowerShell
PS C:\Users\Administrator\Desktop> Import-PSSession -CommandName Get-Sysinfo -Session $sess

ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Script     1.0        tmp_4giwtlau.knk                    Get-Sysinfo


PS C:\Users\Administrator\Desktop>
```

```PowerShell
PS C:\Users\Administrator\Desktop> Get-Sysinfo
john-pc\john
JOHN-PC
PS C:\Users\Administrator\Desktop>
```

Export the ```Get-Sysinfo``` function into a module

```PowerShell
PS C:\Users\Administrator\Desktop> Export-PSSession -ModuleName domainmodule -CommandName Get-Sysinfo -Session $sess
WARNING: Proxy creation has been skipped for the following command: 'Get-Sysinfo', because it would shadow an existing local command.  Use the AllowClobber parameter if you want to shadow existing local
 commands.
Export-PSSession : No command proxies have been created, because all of the requested remote commands would shadow existing local commands.  Use the AllowClobber parameter if you want to shadow
existing local commands.
At line:1 char:1
+ Export-PSSession -ModuleName domainmodule -CommandName Get-Sysinfo -Session $ses ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidResult: (:) [Export-PSSession], ArgumentException
    + FullyQualifiedErrorId : ErrorNoCommandsImportedBecauseOfSkipping,Microsoft.PowerShell.Commands.ExportPSSessionCommand
PS C:\Users\Administrator\Desktop>
```

```PowerShell
PS C:\Users\Administrator\Desktop> Export-PSSession -ModuleName domainmodule -CommandName Get-Sysinfo -Session $sess -AllowClobber -Force

    Directory: C:\Users\Administrator\Documents\WindowsPowerShell\Modules\domainmodule


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
-a---         7/11/2017   5:15 PM         99 domainmodule.format.ps1xml
-a---         7/11/2017   5:15 PM        596 domainmodule.psd1
-a---         7/11/2017   5:15 PM      11689 domainmodule.psm1

PS C:\Users\Administrator\Desktop>
```

```PowerShell
PS C:\Users\Administrator\Desktop> Import-Module domainmodule
```

```PowerShell
PS C:\Users\Administrator\Desktop> Get-Command -Module domainmodule

CommandType     Name                                               ModuleName
-----------     ----                                               ----------
Function        Get-Sysinfo                                        domainmodule

PS C:\Users\Administrator\Desktop>
```

```PowerShell
PS C:\Users\Administrator\Desktop> Get-Sysinfo
john-pc\john
JOHN-PC
PS C:\Users\Administrator\Desktop>
```