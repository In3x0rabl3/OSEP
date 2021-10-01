#### 26. Jobs in Powershell

###### Jobs

- ```Help``` system for ```job```

```PowerShell
PS C:\Users\Administrator> help *job*

Start-Job                         Cmdlet    Microsoft.PowerShell.Core Starts a Windows PowerShell background job.
Get-Job                           Cmdlet    Microsoft.PowerShell.Core Gets Windows PowerShell background jobs that are running in the current session.
Receive-Job                       Cmdlet    Microsoft.PowerShell.Core Gets the results of the Windows PowerShell background jobs in the current session.
Stop-Job                          Cmdlet    Microsoft.PowerShell.Core Stops a Windows PowerShell background job.
Wait-Job                          Cmdlet    Microsoft.PowerShell.Core Suppresses the command prompt until one or all of the Windows PowerShell background jobs running in the session are complete.
Remove-Job                        Cmdlet    Microsoft.PowerShell.Core Deletes a Windows PowerShell background job.
Suspend-Job                       Cmdlet    Microsoft.PowerShell.Core Temporarily stops workflow jobs.
Resume-Job                        Cmdlet    Microsoft.PowerShell.Core Restarts a suspended job
Get-PrintJob                      Function  PrintManagement           ...
Remove-PrintJob                   Function  PrintManagement           ...
Restart-PrintJob                  Function  PrintManagement           ...
Resume-PrintJob                   Function  PrintManagement           ...
Suspend-PrintJob                  Function  PrintManagement           ...
New-JobTrigger                    Cmdlet    PSScheduledJob            New-JobTrigger...
Add-JobTrigger                    Cmdlet    PSScheduledJob            Add-JobTrigger...
Remove-JobTrigger                 Cmdlet    PSScheduledJob            Remove-JobTrigger...
Get-JobTrigger                    Cmdlet    PSScheduledJob            Get-JobTrigger...
Set-JobTrigger                    Cmdlet    PSScheduledJob            Set-JobTrigger...
Enable-JobTrigger                 Cmdlet    PSScheduledJob            Enable-JobTrigger...
Disable-JobTrigger                Cmdlet    PSScheduledJob            Disable-JobTrigger...
New-ScheduledJobOption            Cmdlet    PSScheduledJob            New-ScheduledJobOption...
Get-ScheduledJobOption            Cmdlet    PSScheduledJob            Get-ScheduledJobOption...
Set-ScheduledJobOption            Cmdlet    PSScheduledJob            Set-ScheduledJobOption...
Register-ScheduledJob             Cmdlet    PSScheduledJob            Register-ScheduledJob...
Get-ScheduledJob                  Cmdlet    PSScheduledJob            Get-ScheduledJob...
Set-ScheduledJob                  Cmdlet    PSScheduledJob            Set-ScheduledJob...
Unregister-ScheduledJob           Cmdlet    PSScheduledJob            Unregister-ScheduledJob...
Enable-ScheduledJob               Cmdlet    PSScheduledJob            Enable-ScheduledJob...
Disable-ScheduledJob              Cmdlet    PSScheduledJob            Disable-ScheduledJob...
Get-RDVirtualDesktopCollection... Function  RemoteDesktop             ...
Stop-RDVirtualDesktopCollectio... Function  RemoteDesktop             ...
Get-StorageJob                    Function  Storage                   ...
about_Jobs                        HelpFile                            Provides information about how Windows PowerShell background jobs run a
about_Job_Details                 HelpFile                            Provides details about background jobs on local and remote computers.
about_Remote_Jobs                 HelpFile                            Describes how to run background jobs on remote computers.
about_Scheduled_Jobs              HelpFile                            Describes scheduled jobs and explains how to use and manage
about_Scheduled_Jobs_Advanced     HelpFile                            Explains advanced scheduled job topics, including the file structure
about_Scheduled_Jobs_Basics       HelpFile                            Explains how to create and manage scheduled jobs.
about_Scheduled_Jobs_Troublesh... HelpFile                            Explains how to resolve problems with scheduled jobs

PS C:\Users\Administrator>
```

- ```Commands``` with ```jobs```

```PowerShell
PS C:\Users\Administrator> Get-Command *job*

CommandType     Name                                               ModuleName
-----------     ----                                               ----------
Function        Get-PrintJob                                       PrintManagement
Function        Get-RDVirtualDesktopCollectionJobStatus            RemoteDesktop
Function        Get-StorageJob                                     Storage
Function        Remove-PrintJob                                    PrintManagement
Function        Restart-PrintJob                                   PrintManagement
Function        Resume-PrintJob                                    PrintManagement
Function        Stop-RDVirtualDesktopCollectionJob                 RemoteDesktop
Function        Suspend-PrintJob                                   PrintManagement
Cmdlet          Add-JobTrigger                                     PSScheduledJob
Cmdlet          Disable-JobTrigger                                 PSScheduledJob
Cmdlet          Disable-ScheduledJob                               PSScheduledJob
Cmdlet          Enable-JobTrigger                                  PSScheduledJob
Cmdlet          Enable-ScheduledJob                                PSScheduledJob
Cmdlet          Get-Job                                            Microsoft.PowerShell.Core
Cmdlet          Get-JobTrigger                                     PSScheduledJob
Cmdlet          Get-ScheduledJob                                   PSScheduledJob
Cmdlet          Get-ScheduledJobOption                             PSScheduledJob
Cmdlet          New-JobTrigger                                     PSScheduledJob
Cmdlet          New-ScheduledJobOption                             PSScheduledJob
Cmdlet          Receive-Job                                        Microsoft.PowerShell.Core
Cmdlet          Register-ScheduledJob                              PSScheduledJob
Cmdlet          Remove-Job                                         Microsoft.PowerShell.Core
Cmdlet          Remove-JobTrigger                                  PSScheduledJob
Cmdlet          Resume-Job                                         Microsoft.PowerShell.Core
Cmdlet          Set-JobTrigger                                     PSScheduledJob
Cmdlet          Set-ScheduledJob                                   PSScheduledJob
Cmdlet          Set-ScheduledJobOption                             PSScheduledJob
Cmdlet          Start-Job                                          Microsoft.PowerShell.Core
Cmdlet          Stop-Job                                           Microsoft.PowerShell.Core
Cmdlet          Suspend-Job                                        Microsoft.PowerShell.Core
Cmdlet          Unregister-ScheduledJob                            PSScheduledJob
Cmdlet          Wait-Job                                           Microsoft.PowerShell.Core

PS C:\Users\Administrator>
```

- ```Start``` a ```job```

```PowerShell
PS C:\Users\Administrator> Start-Job -ScriptBlock {whoami}

Id     Name            PSJobTypeName   State         HasMoreData     Location             Command
--     ----            -------------   -----         -----------     --------             -------
2      Job2            BackgroundJob   Running       True            localhost            whoami

PS C:\Users\Administrator>
```

- List all ```jobs```

```PowerShell
PS C:\Users\Administrator> Get-Job

Id     Name            PSJobTypeName   State         HasMoreData     Location             Command
--     ----            -------------   -----         -----------     --------             -------
2      Job2            BackgroundJob   Completed     True            localhost            whoami

PS C:\Users\Administrator>
```

- Receive ```output``` of a ```job``````PowerShell
PS C:\Users\Administrator> Get-Job | Receive-Job
pfpt\administrator
PS C:\Users\Administrator>
```

- Remove ```job```

```PowerShell
PS C:\Users\Administrator> Get-Job | Remove-Jobs
```

```PowerShell
PS C:\Users\Administrator> Get-Job
```

- ```Local job```

```PowerShell
PS C:\Users\Administrator> Start-Job -FilePath .\Desktop\HelloWorld.ps1

Id     Name            PSJobTypeName   State         HasMoreData     Location             Command
--     ----            -------------   -----         -----------     --------             -------
2      Job2            BackgroundJob   Running       True            localhost            "Hello World"


PS C:\Users\Administrator>
```

```PowerShell
PS C:\Users\Administrator> Get-Job -Id 2

Id     Name            PSJobTypeName   State         HasMoreData     Location             Command
--     ----            -------------   -----         -----------     --------             -------
2      Job2            BackgroundJob   Completed     True            localhost            "Hello World"


PS C:\Users\Administrator>
```

```PowerShell
PS C:\Users\Administrator> Get-Job -Id 2 | Receive-Job
Hello World
PS C:\Users\Administrator>
```

- ```Remote job```

```Cmdlets``` with parameter ```Asjob```

```PowerShell
PS C:\Users\Administrator> Get-Command -ParameterName Asjob

CommandType     Name                                               ModuleName
-----------     ----                                               ----------
Cmdlet          Get-WmiObject                                      Microsoft.PowerShell.Management
Cmdlet          Invoke-Command                                     Microsoft.PowerShell.Core
Cmdlet          Invoke-WmiMethod                                   Microsoft.PowerShell.Management
Cmdlet          Remove-WmiObject                                   Microsoft.PowerShell.Management
Cmdlet          Restart-Computer                                   Microsoft.PowerShell.Management
Cmdlet          Set-WmiInstance                                    Microsoft.PowerShell.Management
Cmdlet          Stop-Computer                                      Microsoft.PowerShell.Management
Cmdlet          Test-Connection                                    Microsoft.PowerShell.Management


PS C:\Users\Administrator>
```

```PowerShell
PS C:\Users\Administrator> Invoke-Command -ScriptBlock {ps} -ComputerName JOHN-PC -Credential John-PC\John

Handles  NPM(K)    PM(K)      WS(K) VM(M)   CPU(s)     Id ProcessName                                                              PSComputerName
-------  ------    -----      ----- -----   ------     -- -----------                                                              --------------
    128       5    14992      11460    44            1004 audiodg                                                                  JOHN-PC
     35       2     1344       3288    33     0.02   3108 conhost                                                                  JOHN-PC
    460       5     1064       2596    33     0.11    348 csrss                                                                    JOHN-PC
    214       6     1104       3628    32     0.26    404 csrss                                                                    JOHN-PC
    162       8     2344       8804    72     0.19   3772 dllhost                                                                  JOHN-PC
     68       4      932       3196    39     0.03   1132 dwm                                                                      JOHN-PC
    996      32    30576      44884   241     2.82    940 explorer                                                                 JOHN-PC
      0       0        0         12     0               0 Idle                                                                     JOHN-PC
    803      15     2944       8192    33     0.61    496 lsass                                                                    JOHN-PC
    196       5     1596       3916    23     0.05    504 lsm                                                                      JOHN-PC
    235      10    28168      36120   156     0.44   3100 powershell                                                               JOHN-PC
    668      16    16072       9712    89     0.30   2224 SearchIndexer                                                            JOHN-PC
    201       7     4272       6148    34     0.63    488 services                                                                 JOHN-PC
     29       1      216        664     4     0.05    272 smss                                                                     JOHN-PC
    281       9     4404       7320    58     0.06   1324 spoolsv                                                                  JOHN-PC
    143       4     1788       4076    28     0.38   1524 sppsvc                                                                   JOHN-PC
    355       7     2420       5748    34     0.31    608 svchost                                                                  JOHN-PC
    271       8     2128       4724    26     0.15    720 svchost                                                                  JOHN-PC
    551      14    14492      13176    81     0.32    772 svchost                                                                  JOHN-PC
    558      14    22972      30108   104     0.82    856 svchost                                                                  JOHN-PC
   1061      28    17912      20664   107     0.83    944 svchost                                                                  JOHN-PC
    589      21     6380      11044    58     0.24   1104 svchost                                                                  JOHN-PC
    624      27     9440      11600    75     0.32   1220 svchost                                                                  JOHN-PC
    318      25     8088       8468    47     0.34   1360 svchost                                                                  JOHN-PC
    363      35   147468      42280   210     8.04   1436 svchost                                                                  JOHN-PC
     96       7     1060       3676    25     0.04   1916 svchost                                                                  JOHN-PC
    423      17     5504      11052    70     0.19   2444 svchost                                                                  JOHN-PC
    335      38     7168       8608    62     0.23   2672 svchost                                                                  JOHN-PC
    548       0       48        600     2               4 System                                                                   JOHN-PC
    153       9     2128       4588    41     0.02    364 taskhost                                                                 JOHN-PC
    116       5     1444       3724    45     0.05    668 VBoxService                                                              JOHN-PC
    134       5     1216       4284    61     0.03   2052 VBoxTray                                                                 JOHN-PC
     74       5      784       3012    32     0.09    396 wininit                                                                  JOHN-PC
    113       4     1532       4260    39     0.24    444 winlogon                                                                 JOHN-PC
    118       4     1788       4204    27     0.11   2840 WmiPrvSE                                                                 JOHN-PC
    421      15     7296      17944   107     0.40   2344 wmpnetwk                                                                 JOHN-PC
    209      10    27684      35648   139     0.72    880 wsmprovhost                                                              JOHN-PC


PS C:\Users\Administrator>
```

```PowerShell
PS C:\Users\Administrator> $sess = New-PSSession -ComputerName JOHN-PC -Credential John-PC\John
```

```PowerShell
PS C:\Users\Administrator> Invoke-Command -ScriptBlock {Start-Job -ScriptBlock {ps}} -Session $sess

Id     Name            PSJobTypeName   State         HasMoreData     Location             Command                   PSComputerName
--     ----            -------------   -----         -----------     --------             -------                   --------------
1      Job1                            Running       True            localhost            ps                        JOHN-PC

PS C:\Users\Administrator>
```

```PowerShell
PS C:\Users\Administrator> Invoke-Command -ScriptBlock {Get-Job} -Session $sess

Id     Name            PSJobTypeName   State         HasMoreData     Location             Command                   PSComputerName
--     ----            -------------   -----         -----------     --------             -------                   --------------
1      Job1                            Completed     True            localhost            ps                        JOHN-PC

PS C:\Users\Administrator>
```

```PowerShell
PS C:\Users\Administrator> Invoke-Command -ScriptBlock {Get-Job | Receive-Job} -Session $sess

Handles  NPM(K)    PM(K)      WS(K) VM(M)   CPU(s)     Id ProcessName                                                              PSComputerName
-------  ------    -----      ----- -----   ------     -- -----------                                                              --------------
     31       2      492       1980    17     0.01   2156 conhost                                                                  JOHN-PC
    427       5     1080       2492    33     0.13    348 csrss                                                                    JOHN-PC
    161       6     1128       3488    32     0.27    404 csrss                                                                    JOHN-PC
     66       3      892       2908    38     0.03   1132 dwm                                                                      JOHN-PC
    823      26    28592      42576   207     2.92    940 explorer                                                                 JOHN-PC
      0       0        0         12     0               0 Idle                                                                     JOHN-PC
    791      15     3072       7340    33     0.64    496 lsass                                                                    JOHN-PC
    197       5     1600       3572    23     0.05    504 lsm                                                                      JOHN-PC
    240      11    24716      34280   147     0.37   4012 powershell                                                               JOHN-PC
    661      15    15920       8708    88     0.31   2224 SearchIndexer                                                            JOHN-PC
    192       7     4236       4748    33     0.63    488 services                                                                 JOHN-PC
     29       1      216        576     4     0.05    272 smss                                                                     JOHN-PC
    275       9     4312       5688    57     0.06   1324 spoolsv                                                                  JOHN-PC
    344       7     2452       5256    34     0.32    608 svchost                                                                  JOHN-PC
    257       8     2212       4532    26     0.19    720 svchost                                                                  JOHN-PC
    548      14    14412      11644    81     0.36    772 svchost                                                                  JOHN-PC
    515      13    25176      30232   103     1.57    856 svchost                                                                  JOHN-PC
   1009      25    11884      17924    88     0.94    944 svchost                                                                  JOHN-PC
    530      20     6088       9388    55     0.25   1104 svchost                                                                  JOHN-PC
    606      21     9660      10564    75     0.34   1220 svchost                                                                  JOHN-PC
    308      25     7956       6348    46     0.34   1360 svchost                                                                  JOHN-PC
    335      35   144320      23808   206     8.32   1436 svchost                                                                  JOHN-PC
     96       7     1060       3276    25     0.04   1916 svchost                                                                  JOHN-PC
    400      16     5376      10520    69     0.19   2444 svchost                                                                  JOHN-PC
    343      28     7832       8452    64     0.25   2672 svchost                                                                  JOHN-PC
    550       0       48        600     2               4 System                                                                   JOHN-PC
    147       8     2044       4344    40     0.02    364 taskhost                                                                 JOHN-PC
    116       5     1424       3352    44     0.05    668 VBoxService                                                              JOHN-PC
    136       5     1192       3948    59     0.03   2052 VBoxTray                                                                 JOHN-PC
     74       5      784       2816    32     0.09    396 wininit                                                                  JOHN-PC
    113       4     1496       3596    39     0.24    444 winlogon                                                                 JOHN-PC
    112       4     1692       4000    26     0.11   2840 WmiPrvSE                                                                 JOHN-PC
    409      15     7232       3556   106     0.40   2344 wmpnetwk                                                                 JOHN-PC
    256      11    30032      38152   145     0.36   3140 wsmprovhost                                                              JOHN-PC

PS C:\Users\Administrator>
```

Using ```AsJob```

```PowerShell
PS C:\Users\Administrator> Invoke-Command -ScriptBlock {ps} -ComputerName JOHN-PC -Credential John-PC\John -AsJob

Id     Name            PSJobTypeName   State         HasMoreData     Location             Command
--     ----            -------------   -----         -----------     --------             -------
7      Job7            RemoteJob       Running       True            JOHN-PC              ps

PS C:\Users\Administrator>
```

```PowerShell
PS C:\Users\Administrator>  Get-Job

Id     Name            PSJobTypeName   State         HasMoreData     Location             Command
--     ----            -------------   -----         -----------     --------             -------
7      Job7            RemoteJob       Completed     True            JOHN-PC              ps

PS C:\Users\Administrator>
```

```PowerShell
PS C:\Users\Administrator> Get-Job -id 7 | Receive-Job

Handles  NPM(K)    PM(K)      WS(K) VM(M)   CPU(s)     Id ProcessName                                                              PSComputerName
-------  ------    -----      ----- -----   ------     -- -----------                                                              --------------
    421       5     1080       2488    33     0.14    348 csrss                                                                    JOHN-PC
    161       6     1128       3492    32     0.27    404 csrss                                                                    JOHN-PC
     66       3      892       2908    38     0.03   1132 dwm                                                                      JOHN-PC
    827      26    28528      42488   206     2.92    940 explorer                                                                 JOHN-PC
      0       0        0         12     0               0 Idle                                                                     JOHN-PC
    798      15     3080       7416    33     0.65    496 lsass                                                                    JOHN-PC
    198       5     1608       3580    23     0.05    504 lsm                                                                      JOHN-PC
    655      15    15712       8244    81     0.31   2224 SearchIndexer                                                            JOHN-PC
    194       8     4324       4808    34     0.63    488 services                                                                 JOHN-PC
     29       1      216        576     4     0.05    272 smss                                                                     JOHN-PC
    275       9     4312       5704    57     0.06   1324 spoolsv                                                                  JOHN-PC
    343       7     2420       5228    33     0.32    608 svchost                                                                  JOHN-PC
    256       8     2172       4500    26     0.20    720 svchost                                                                  JOHN-PC
    551      14    14392      11708    81     0.36    772 svchost                                                                  JOHN-PC
    516      13    25204      29328   103     1.78    856 svchost                                                                  JOHN-PC
   1010      25    11336      17900    88     0.95    944 svchost                                                                  JOHN-PC
    528      20     6060       9376    55     0.25   1104 svchost                                                                  JOHN-PC
    612      25     9764      10676    75     0.36   1220 svchost                                                                  JOHN-PC
    300      24     8076       6392    46     0.34   1360 svchost                                                                  JOHN-PC
    352      35   147444      17736   209     8.34   1436 svchost                                                                  JOHN-PC
     96       7     1060       3272    25     0.04   1916 svchost                                                                  JOHN-PC
    398      16     5376      10524    69     0.19   2444 svchost                                                                  JOHN-PC
    344      18     7840       8540    64     0.27   2672 svchost                                                                  JOHN-PC
    546       0       48        600     2               4 System                                                                   JOHN-PC
    147       8     2044       4344    40     0.02    364 taskhost                                                                 JOHN-PC
    116       5     1444       3348    44     0.06    668 VBoxService                                                              JOHN-PC
    136       5     1192       3940    59     0.03   2052 VBoxTray                                                                 JOHN-PC
     74       5      784       2816    32     0.09    396 wininit                                                                  JOHN-PC
    113       4     1496       3596    39     0.24    444 winlogon                                                                 JOHN-PC
    112       4     1772       4092    26     0.11   2840 WmiPrvSE                                                                 JOHN-PC
    409      15     7232       3864   106     0.40   2344 wmpnetwk                                                                 JOHN-PC
    290      11    19988      29536   145     0.41   3140 wsmprovhost                                                              JOHN-PC
    209      10    27672      35632   139     0.70   3172 wsmprovhost                                                              JOHN-PC

PS C:\Users\Administrator>
```

###### Exercise

- Run jobs in a ```PSSession```

```PowerShell
PS C:\Users\Administrator> Enter-PSSession -ComputerName JOHN-PC -Credential John-PC\John
```

```PowerShell
[JOHN-PC]: PS C:\Users\John\Documents> Get-Job
```

```PowerShell
[JOHN-PC]: PS C:\Users\John\Documents> Start-Job -ScriptBlock {whoami}

Id              Name            State      HasMoreData     Location             Command
--              ----            -----      -----------     --------             -------
1               Job1            Running    True            localhost            whoami

[JOHN-PC]: PS C:\Users\John\Documents>
```

```PowerShell
[JOHN-PC]: PS C:\Users\John\Documents> Start-Job -ScriptBlock {ps}

Id              Name            State      HasMoreData     Location             Command
--              ----            -----      -----------     --------             -------
3               Job3            Running    True            localhost            ps

[JOHN-PC]: PS C:\Users\John\Documents>
```

```PowerShell
[JOHN-PC]: PS C:\Users\John\Documents> Get-Job

Id              Name            State      HasMoreData     Location             Command
--              ----            -----      -----------     --------             -------
1               Job1            Completed  False           localhost            whoami
3               Job3            Completed  True            localhost            ps

[JOHN-PC]: PS C:\Users\John\Documents>
```

```PowerShell
[JOHN-PC]: PS C:\Users\John\Documents> Get-Job -id 1 | Receive-Job
john-pc\john
[JOHN-PC]: PS C:\Users\John\Documents>
```

```PowerShell
[JOHN-PC]: PS C:\Users\John\Documents> Get-Job -id 3 | Receive-Job

Handles  NPM(K)    PM(K)      WS(K) VM(M)   CPU(s)     Id ProcessName
-------  ------    -----      ----- -----   ------     -- -----------
     31       2      488       1968    17     0.00   3212 conhost
    561       6     1164       2652    34     0.24    348 csrss
    174       6     1128       3496    32     0.28    404 csrss
     66       3      892       2900    38     0.03   1132 dwm
    799      24    27856      40772   195     2.95    940 explorer
      0       0        0         12     0               0 Idle
    824      15     3184       7756    33     2.79    496 lsass
    199       5     1624       3616    23     0.11    504 lsm
    244      11    24744      34284   147     0.35   3692 powershell
    136       7    10036      13220    60     6.42   2068 rundll32
    682      17    18292      14416   121     1.20   2224 SearchIndexer
    214       7     4364       5936    37     0.90    488 services
     29       1      216        576     4     0.05    272 smss
    279       9     4356       5748    58     0.06   1324 spoolsv
    347       7     2540       5456    35     0.41    608 svchost
    275       8     2164       4560    26     0.20    720 svchost
    563      14    15432      12408    84     0.40    772 svchost
    503      12    31660      37072    99     4.56    856 svchost
   1024      25    12088      18948    91     1.07    944 svchost
    547      21     6480      10076    56     0.25   1104 svchost
    618      25    12424      12244    78     1.45   1220 svchost
    311      25     8172       6796    46     0.34   1360 svchost
    354      35   147768      42368   208   199.65   1436 svchost
     98       7     1088       3332    25     0.04   1916 svchost
    397      16     5376      10564    69     0.24   2444 svchost
    342      16     7988       8712    65     0.38   2672 svchost
     68       4      932       3616    25     0.02   4028 svchost
    583       0       48       1456     3               4 System
    150       9     2072       4384    40     0.02    364 taskhost
    121       5     2652       6600    35     0.87   1808 TrustedInstaller
    116       5     1444       3380    44     0.19    668 VBoxService
    136       5     1192       3924    59     0.05   2052 VBoxTray
    119       5     1344       4832    30     0.06   2168 VSSVC
     74       5      784       2816    32     0.09    396 wininit
    113       4     1496       3592    39     0.24    444 winlogon
    173       7     4016       7880    53     0.08   2500 WmiPrvSE
    411      15     7396       7460   107     0.46   2344 wmpnetwk
    287      11    19404      25684   144     0.41   3140 wsmprovhost
    360      12    43684      53604   161     1.05   3936 wsmprovhost


[JOHN-PC]: PS C:\Users\John\Documents>
```

```PowerShell
[JOHN-PC]: PS C:\Users\John\Documents> exit
PS C:\Users\Administrator>
```