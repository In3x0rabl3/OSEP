#### 22. Powershell Remoting Part 3

###### PowerShell Remoting – One-to-One

- Interactive Session - ```PSSession```
    - Runs in a new process ```(wsmprovhost)```
    - Is Stateful
- Using PSSessions
    - Initiating
    - Interacting
    - Closing

- ```PowerShell Version```

```PowerShell
PS C:\Users\Administrator> $PSVersionTable

Name                           Value
----                           -----
PSVersion                      4.0
WSManStackVersion              3.0
SerializationVersion           1.1.0.1
CLRVersion                     4.0.30319.34014
BuildVersion                   6.3.9600.16394
PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0}
PSRemotingProtocolVersion      2.2

PS C:\Users\Administrator>
```

- Help on ```session```

```PowerShell
PS C:\Users\Administrator> help *session*

Set-PSSessionConfiguration        Cmdlet    Microsoft.PowerShell.Core Changes the properties of a registered session configuration.
Enable-PSSessionConfiguration     Cmdlet    Microsoft.PowerShell.Core Enables the session configurations on the local computer.
Disable-PSSessionConfiguration    Cmdlet    Microsoft.PowerShell.Core Disables session configurations on the local computer.
New-PSSession                     Cmdlet    Microsoft.PowerShell.Core Creates a persistent connection to a local or remote computer.
Disconnect-PSSession              Cmdlet    Microsoft.PowerShell.Core Disconnects from a session.
Connect-PSSession                 Cmdlet    Microsoft.PowerShell.Core Reconnects to disconnected sessions
Receive-PSSession                 Cmdlet    Microsoft.PowerShell.Core Gets results of commands in disconnected sessions
Get-PSSession                     Cmdlet    Microsoft.PowerShell.Core Gets the Windows PowerShell sessions on local and remote computers.
Remove-PSSession                  Cmdlet    Microsoft.PowerShell.Core Closes one or more Windows PowerShell sessions (PSSessions).
Enter-PSSession                   Cmdlet    Microsoft.PowerShell.Core Starts an interactive session with a remote computer.
Exit-PSSession                    Cmdlet    Microsoft.PowerShell.Core Ends an interactive session with a remote computer.
New-PSSessionOption               Cmdlet    Microsoft.PowerShell.Core Creates an object that contains advanced options for a PSSession.
New-PSSessionConfigurationFile    Cmdlet    Microsoft.PowerShell.Core Creates a file that defines a session configuration.
Test-PSSessionConfigurationFile   Cmdlet    Microsoft.PowerShell.Core Verifies the keys and values in a session configuration file.
Export-PSSession                  Cmdlet    Microsoft.PowerShell.U... Imports commands from another session and saves them in a Windows PowerShell module.
Import-PSSession                  Cmdlet    Microsoft.PowerShell.U... Imports commands from another session into the current session.
Get-CimSession                    Cmdlet    CimCmdlets                Get-CimSession...
New-CimSession                    Cmdlet    CimCmdlets                New-CimSession...
New-CimSessionOption              Cmdlet    CimCmdlets                New-CimSessionOption...
Remove-CimSession                 Cmdlet    CimCmdlets                Remove-CimSession...
Get-IscsiSession                  Function  iSCSI                     ...
Register-IscsiSession             Function  iSCSI                     ...
Unregister-IscsiSession           Function  iSCSI                     ...
New-WSManSessionOption            Cmdlet    Microsoft.WSMan.Manage... Creates a WS-Management session option hash table to use as input parameters to the following WS-Management cmdlets: Get-WSManIns...
Get-DtcTransactionsTraceSession   Function  MsDtc                     ...
Set-DtcTransactionsTraceSession   Function  MsDtc                     ...
Start-DtcTransactionsTraceSession Function  MsDtc                     ...
Stop-DtcTransactionsTraceSession  Function  MsDtc                     ...
Write-DtcTransactionsTraceSession Function  MsDtc                     ...
New-NetEventSession               Function  NetEventPacketCapture     ...
Remove-NetEventSession            Function  NetEventPacketCapture     ...
Get-NetEventSession               Function  NetEventPacketCapture     ...
Set-NetEventSession               Function  NetEventPacketCapture     ...
Start-NetEventSession             Function  NetEventPacketCapture     ...
Stop-NetEventSession              Function  NetEventPacketCapture     ...
Get-NetNatSession                 Function  NetNat                    ...
Disconnect-NfsSession             Function  NFS                       ...
Get-NfsSession                    Function  NFS                       ...
New-PSWorkflowSession             Function  PSWorkflow                ...
New-RDSessionDeployment           Function  RemoteDesktop             ...
Get-RDSessionCollection           Function  RemoteDesktop             ...
Remove-RDSessionCollection        Function  RemoteDesktop             ...
New-RDSessionCollection           Function  RemoteDesktop             ...
Get-RDSessionHost                 Function  RemoteDesktop             ...
Set-RDSessionHost                 Function  RemoteDesktop             ...
Remove-RDSessionHost              Function  RemoteDesktop             ...
Add-RDSessionHost                 Function  RemoteDesktop             ...
Get-RDSessionCollectionConfigu... Function  RemoteDesktop             ...
Set-RDSessionCollectionConfigu... Function  RemoteDesktop             ...
Get-RDUserSession                 Function  RemoteDesktop             ...
Get-SmbSession                    Function  SmbShare                  ...
Close-SmbSession                  Function  SmbShare                  ...
New-TlsSessionTicketKey           Cmdlet    TLS                       New-TlsSessionTicketKey...
Enable-TlsSessionTicketKey        Cmdlet    TLS                       Enable-TlsSessionTicketKey...
Disable-TlsSessionTicketKey       Cmdlet    TLS                       Disable-TlsSessionTicketKey...
Export-TlsSessionTicketKey        Cmdlet    TLS                       Export-TlsSessionTicketKey...
about_PSSessions                  HelpFile                            Describes Windows PowerShell sessions (PSSessions) and explains how to
about_PSSession_Details           HelpFile                            Provides detailed information about Windows PowerShell sessions and the
about_Remote_Disconnected_Sess... HelpFile                            Explains how to disconnect from and reconnect to a PSSession
about_Session_Configurations      HelpFile                            Describes session configurations, which determine the users who can
about_Session_Configuration_Files HelpFile                            Describes session configuration files, which can be used in a
about_CimSession                  HelpFile                            Describes a CimSession object and the difference between CIM sessions and

PS C:\Users\Administrator>
```

- In ```Local Machine```

```PowerShell
PS C:\Users\Administrator> $env:COMPUTERNAME
WIN-2012-DC
PS C:\Users\Administrator> $env:USERDOMAIN
PFPT
PS C:\Users\Administrator> $env:USERNAME
Administrator
PS C:\Users\Administrator>
```

```PowerShell
PS C:\Users\Administrator> Enable-PSRemoting -Force
WinRM is already set up to receive requests on this computer.
WinRM is already set up for remote management on this computer.
PS C:\Users\Administrator>
```

- In ```Remote Machine```

```PowerShell
PS C:\Windows\system32> $env:COMPUTERNAME
JOHN-PC
PS C:\Windows\system32> $env:USERDOMAIN
John-PC
PS C:\Windows\system32> $env:USERNAME
John
PS C:\Windows\system32>
```

```PowerShell
PS C:\Windows\system32> Enable-PSRemoting -Force
WinRM already is set up to receive requests on this machine.
WinRM already is set up for remote management on this machine.
PS C:\Windows\system32>
```

- ```New-PSSession```

```PowerShell
PS C:\Users\Administrator> New-PSSession -ComputerName JOHN-PC -Credential John-PC\John

 Id Name            ComputerName    State         ConfigurationName     Availability
 -- ----            ------------    -----         -----------------     ------------
  1 Session1        JOHN-PC         Opened        Microsoft.PowerShell     Available


PS C:\Users\Administrator>
```

- ```Get-PSSession```

```PowerShell
PS C:\Users\Administrator> Get-PSSession

 Id Name            ComputerName    State         ConfigurationName     Availability
 -- ----            ------------    -----         -----------------     ------------
  1 Session1        JOHN-PC         Opened        Microsoft.PowerShell     Available


PS C:\Users\Administrator>
```

- ```Enter-PSSession```

```PowerShell
PS C:\Users\Administrator> Enter-PSSession -ComputerName JOHN-PC -Credential John-PC\John
[JOHN-PC]: PS C:\Users\John\Documents> $env:COMPUTERNAME
JOHN-PC
[JOHN-PC]: PS C:\Users\John\Documents> $env:USERDOMAIN
John-PC
[JOHN-PC]: PS C:\Users\John\Documents> $env:USERNAME
John
[JOHN-PC]: PS C:\Users\John\Documents>
```

```PowerShell
PS C:\Users\Administrator> Enter-PSSession -Id 1
[JOHN-PC]: PS C:\Users\John\Documents> whoami
john-pc\john
[JOHN-PC]: PS C:\Users\John\Documents> $env:COMPUTERNAME
JOHN-PC
[JOHN-PC]: PS C:\Users\John\Documents> $env:USERDOMAIN
John-PC
[JOHN-PC]: PS C:\Users\John\Documents> $env:USERNAME
John
[JOHN-PC]: PS C:\Users\John\Documents> Get-Process

Handles  NPM(K)    PM(K)      WS(K) VM(M)   CPU(s)     Id ProcessName
-------  ------    -----      ----- -----   ------     -- -----------
     23       2     1756       2156    30     0.00   1288 cmd
     40       3      708       3192    42     0.04   1220 conhost
     39       3     1468       4036    43     0.06   2496 conhost
    415       5     1112       2404    33     0.09    352 csrss
    214       6     1196       3600    32     0.40    408 csrss
     76       3      892       3544    32     0.03   3672 dllhost
     66       3      892       3252    38     0.02    912 dwm
    821      25    25344      38764   219     2.81    696 explorer
      0       0        0         12     0               0 Idle
    741      13     3040       7516    32     0.76    492 lsass
    196       5     1604       3608    23     0.06    500 lsm
     56       3      868       4248    57     0.06   3160 notepad
    501      12    23172      33576   165     0.49   2476 powershell
    134       5     6272       9764    63     0.12   2924 python
    626      15    18692      10972    85     0.45   1664 SearchIndexer
    193       7     4100       5844    35     0.65    476 services
     29       1      216        548     4     0.06    272 smss
    280       9     4312       5884    57     0.02   1356 spoolsv
    350       7     2868       5940    35     0.30    624 svchost
    267       8     2168       4848    26     0.24    736 svchost
    548      13    14856      12548    77     0.36    788 svchost
    512      12    22584      27856    99     2.41    872 svchost
   1150      30    14364      22076   106     1.62    960 svchost
    456      17     5932       9784    55     0.36   1124 svchost
    690      26    11620      10904    79     0.40   1232 svchost
    305      24     9636       9264    48     0.53   1392 svchost
    359      15     4960       8800    67     0.15   1500 svchost
    356      36   144368      18092   210    10.70   1956 svchost
    349      13     8020       9796    64     0.53   2772 svchost
     96       7     1056       3856    25     0.03   3816 svchost
    568       0       44        552     2               4 System
    138       8     1972       4428    38     0.05   1292 taskhost
    117       5     1524       3460    44     0.10    684 VBoxService
    140       5     1236       4400    61     0.03   2104 VBoxTray
     74       5      780       2620    32     0.23    400 wininit
    113       4     1492       3620    39     0.27    448 winlogon
    452      16     7468       7376   108     0.32    556 wmpnetwk
    283      11    41784      51948   161     1.04   3768 wsmprovhost

[JOHN-PC]: PS C:\Users\John\Documents> exit
PS C:\Users\Administrator>
```

- ```Remove-PSSession```

```PowerShell
PS C:\Users\Administrator> Remove-PSSession -id 1
```

```PowerShell
PS C:\Users\Administrator> Get-PSSession
```

###### Exercise

- Try connecting a PS Session to a VM.
    - Refer above for - ```New-PSSession```, ```Get-PSSession```, ```Enter-PSSession```, ```Remove-PSSession```
- Compare ```Enter-PSSession``` to ```PsExec```. [Think over pros and cons.](https://4sysops.com/archives/psexec-vs-the-powershell-remoting-cmdlets-invoke-command-and-enter-pssession/#psexec-vs-powershell-remoting)
- Which one do you find easier to use as an attacker?
- What are the detection rates?

	- ```Enter-PSSession```
	
 	```PowerShell
	PS C:\Users\Administrator> Enter-PSSession -ComputerName JOHN-PC -Credential John-PC\John
	[JOHN-PC]: PS C:\Users\John\Documents> $env:COMPUTERNAME
	JOHN-PC
	[JOHN-PC]: PS C:\Users\John\Documents> $env:USERDOMAIN
	John-PC
	[JOHN-PC]: PS C:\Users\John\Documents> $env:USERNAME
	John
	[JOHN-PC]: PS C:\Users\John\Documents>
	```   
	

	- ```PsExec```

	```Remote Machine```

	```PowerShell
	PS C:\Windows\system32> $env:COMPUTERNAME
	JOHN-PC
	PS C:\Windows\system32> $env:USERDOMAIN
	John-PC
	PS C:\Windows\system32> $env:USERNAME
	John
	PS C:\Windows\system32>
	```

	```PowerShell
	PS C:\Users\Administrator\Desktop\SysinternalsSuite> .\PsExec.exe \\JOHN-PC -u John-PC\John cmd
	
	PsExec v2.2 - Execute processes remotely
	Copyright (C) 2001-2016 Mark Russinovich
	Sysinternals - www.sysinternals.com
	
	Password:
	
	Microsoft Windows [Version 6.1.7600]
	Copyright (c) 2009 Microsoft Corporation.  All rights reserved.
	
	C:\Windows\system32>ipconfig
	
	Windows IP Configuration
	
	
	Ethernet adapter Local Area Connection:
	
	   Connection-specific DNS Suffix  . : hsd1.ca.comcast.net
	   IPv6 Address. . . . . . . . . . . : 2601:644:8501:6c87::c308
	   IPv6 Address. . . . . . . . . . . : 2601:644:8501:6c87:613e:76ef:5029:c2c1
	   Temporary IPv6 Address. . . . . . : 2601:644:8501:6c87:bc3b:5ba5:fa78:5474
	   Link-local IPv6 Address . . . . . : fe80::613e:76ef:5029:c2c1%11
	   IPv4 Address. . . . . . . . . . . : 10.0.0.129
	   Subnet Mask . . . . . . . . . . . : 255.255.255.0
	   Default Gateway . . . . . . . . . : fe80::250:f1ff:fe80:0%11
	                                       10.0.0.1
	
	Tunnel adapter isatap.hsd1.ca.comcast.net:
	
	   Media State . . . . . . . . . . . : Media disconnected
	   Connection-specific DNS Suffix  . : hsd1.ca.comcast.net
	
	Tunnel adapter Local Area Connection* 11:
	
	   Connection-specific DNS Suffix  . :
	   IPv6 Address. . . . . . . . . . . : 2001:0:9d38:90d7:2013:2547:b6b9:5698
	   Link-local IPv6 Address . . . . . : fe80::2013:2547:b6b9:5698%13
	   Default Gateway . . . . . . . . . :
	
	C:\Windows\system32>
	```
	
	```PowerShell
	PS C:\Users\Administrator\Desktop\SysinternalsSuite> .\PsExec.exe \\JOHN-PC -u John-PC\John -p Ab12345 cmd
	
	PsExec v2.2 - Execute processes remotely
	Copyright (C) 2001-2016 Mark Russinovich
	Sysinternals - www.sysinternals.com
	
	
	Microsoft Windows [Version 6.1.7600]
	Copyright (c) 2009 Microsoft Corporation.  All rights reserved.
	
	C:\Windows\system32>ipconfig
	
	Windows IP Configuration
	
	
	Ethernet adapter Local Area Connection:
	
	   Connection-specific DNS Suffix  . : hsd1.ca.comcast.net
	   IPv6 Address. . . . . . . . . . . : 2601:644:8501:6c87::c308
	   IPv6 Address. . . . . . . . . . . : 2601:644:8501:6c87:613e:76ef:5029:c2c1
	   Temporary IPv6 Address. . . . . . : 2601:644:8501:6c87:bc3b:5ba5:fa78:5474
	   Link-local IPv6 Address . . . . . : fe80::613e:76ef:5029:c2c1%11
	   IPv4 Address. . . . . . . . . . . : 10.0.0.129
	   Subnet Mask . . . . . . . . . . . : 255.255.255.0
	   Default Gateway . . . . . . . . . : fe80::250:f1ff:fe80:0%11
	                                       10.0.0.1
	
	Tunnel adapter isatap.hsd1.ca.comcast.net:
	
	   Media State . . . . . . . . . . . : Media disconnected
	   Connection-specific DNS Suffix  . : hsd1.ca.comcast.net
	
	Tunnel adapter Local Area Connection* 11:
	
	   Connection-specific DNS Suffix  . :
	   IPv6 Address. . . . . . . . . . . : 2001:0:9d38:90d7:2013:2547:b6b9:5698
	   Link-local IPv6 Address . . . . . : fe80::2013:2547:b6b9:5698%13
	   Default Gateway . . . . . . . . . :
	
	C:\Windows\system32>
	```
	
	```PowerShell
	PS C:\Users\Administrator\Desktop\SysinternalsSuite> .\PsExec.exe -h
	
	PsExec v2.2 - Execute processes remotely
	Copyright (C) 2001-2016 Mark Russinovich
	Sysinternals - www.sysinternals.com
	
	PsExec executes a program on a remote system, where remotely executed console
	applications execute interactively.
	
	Usage: psexec [\\computer[,computer2[,...] | @file]][-u user [-p psswd][-n s][-r servicename][-h][-l][-s|-e][-x][-i [session]][-c [-f|-v]][-w directory][-d][-<priority>][-a n,n,...] cmd [arguments]
	     -a         Separate processors on which the application can run with
	                commas where 1 is the lowest numbered CPU. For example,
	                to run the application on CPU 2 and CPU 4, enter:
	                "-a 2,4"
	     -c         Copy the specified program to the remote system for
	                execution. If you omit this option the application
	                must be in the system path on the remote system.
	     -d         Don't wait for process to terminate (non-interactive).
	     -e         Does not load the specified account's profile.
	     -f         Copy the specified program even if the file already
	                exists on the remote system.
	     -i         Run the program so that it interacts with the desktop of the
	                specified session on the remote system. If no session is
	                specified the process runs in the console session.
	     -h         If the target system is Vista or higher, has the process
	                run with the account's elevated token, if available.
	     -l         Run process as limited user (strips the Administrators group
	                and allows only privileges assigned to the Users group).
	                On Windows Vista the process runs with Low Integrity.
	     -n         Specifies timeout in seconds connecting to remote computers.
	     -p         Specifies optional password for user name. If you omit this
	                you will be prompted to enter a hidden password.
	     -r         Specifies the name of the remote service to create or interact.
	                with.
	     -s         Run the remote process in the System account.
	     -u         Specifies optional user name for login to remote
	                computer.
	     -v         Copy the specified file only if it has a higher version number
	                or is newer on than the one on the remote system.
	     -w         Set the working directory of the process (relative to
	                remote computer).
	     -x         Display the UI on the Winlogon secure desktop (local system
	                only).
	     -arm       Specifies the remote computer is of ARM architecture.
	     -priority  Specifies -low, -belownormal, -abovenormal, -high or
	                -realtime to run the process at a different priority. Use
	                -background to run at low memory and I/O priority on Vista.
	     computer   Direct PsExec to run the application on the remote
	                computer or computers specified. If you omit the computer
	                name PsExec runs the application on the local system,
	                and if you specify a wildcard (\\*), PsExec runs the
	                command on all computers in the current domain.
	     @file      PsExec will execute the command on each of the computers listed
	                in the file.
	     cmd            Name of application to execute.
	     arguments  Arguments to pass (note that file paths must be
	                absolute paths on the target system).
	     -accepteula This flag suppresses the display of the license dialog.
	     -nobanner   Do not display the startup banner and copyright message.
	
	You can enclose applications that have spaces in their name with
	quotation marks e.g. psexec \\marklap "c:\long name app.exe".
	Input is only passed to the remote system when you press the enter
	key, and typing Ctrl-C terminates the remote process.
	
	If you omit a user name the process will run in the context of your
	account on the remote system, but will not have access to network
	resources (because it is impersonating). Specify a valid user name
	in the Domain\User syntax if the remote process requires access
	to network resources or to run in a different account. Note that
	the password and command is encrypted in transit to the remote system.
	
	Error codes returned by PsExec are specific to the applications you
	execute, not PsExec.
	
	PS C:\Users\Administrator\Desktop\SysinternalsSuite>
	```
