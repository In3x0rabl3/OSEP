#### 20. Remoting Part 1

###### Running Cmdlets on remote computers

- Help topics for ```Remoting```

```PowerShell
PS C:\Users\Administrator> Get-Help *remote*

Name                              Category  Module                    Synopsis
----                              --------  ------                    --------
Get-RDRemoteApp                   Function  RemoteDesktop             ...
New-RDRemoteApp                   Function  RemoteDesktop             ...
Set-RDRemoteApp                   Function  RemoteDesktop             ...
Remove-RDRemoteApp                Function  RemoteDesktop             ...
Get-RDRemoteDesktop               Function  RemoteDesktop             ...
Set-RDRemoteDesktop               Function  RemoteDesktop             ...
about_Remote                      HelpFile                            Describes how to run remote commands in Windows PowerShell.
about_Remote_Disconnected_Sess... HelpFile                            Explains how to disconnect from and reconnect to a PSSession
about_Remote_FAQ                  HelpFile                            Contains questions and answers about running remote commands
about_Remote_Jobs                 HelpFile                            Describes how to run background jobs on remote computers.
about_Remote_Output               HelpFile                            Describes how to interpret and format the output of remote commands.
about_Remote_Requirements         HelpFile                            Describes the system requirements and configuration requirements for
about_Remote_Troubleshooting      HelpFile                            Describes how to troubleshoot remote operations in Windows PowerShell.
about_Remote_Variables            HelpFile                            Explains how to use local and remote variables in remote


PS C:\Users\Administrator>
```

- ```Cmdlet``` which accept parameter ```ComputerName```

```PowerShell
PS C:\Users\Administrator> Get-Command -CommandType Cmdlet -ParameterName ComputerName

CommandType     Name                                               ModuleName
-----------     ----                                               ----------
Cmdlet          Add-Computer                                       Microsoft.PowerShell.Management
Cmdlet          Clear-EventLog                                     Microsoft.PowerShell.Management
Cmdlet          Connect-PSSession                                  Microsoft.PowerShell.Core
Cmdlet          Enter-PSSession                                    Microsoft.PowerShell.Core
Cmdlet          Get-EventLog                                       Microsoft.PowerShell.Management
Cmdlet          Get-HotFix                                         Microsoft.PowerShell.Management
Cmdlet          Get-Process                                        Microsoft.PowerShell.Management
Cmdlet          Get-PSSession                                      Microsoft.PowerShell.Core
Cmdlet          Get-Service                                        Microsoft.PowerShell.Management
Cmdlet          Get-WmiObject                                      Microsoft.PowerShell.Management
Cmdlet          Invoke-Command                                     Microsoft.PowerShell.Core
Cmdlet          Invoke-WmiMethod                                   Microsoft.PowerShell.Management
Cmdlet          Limit-EventLog                                     Microsoft.PowerShell.Management
Cmdlet          New-EventLog                                       Microsoft.PowerShell.Management
Cmdlet          New-PSSession                                      Microsoft.PowerShell.Core
Cmdlet          Receive-Job                                        Microsoft.PowerShell.Core
Cmdlet          Receive-PSSession                                  Microsoft.PowerShell.Core
Cmdlet          Register-WmiEvent                                  Microsoft.PowerShell.Management
Cmdlet          Remove-Computer                                    Microsoft.PowerShell.Management
Cmdlet          Remove-EventLog                                    Microsoft.PowerShell.Management
Cmdlet          Remove-PSSession                                   Microsoft.PowerShell.Core
Cmdlet          Remove-WmiObject                                   Microsoft.PowerShell.Management
Cmdlet          Rename-Computer                                    Microsoft.PowerShell.Management
Cmdlet          Restart-Computer                                   Microsoft.PowerShell.Management
Cmdlet          Set-Service                                        Microsoft.PowerShell.Management
Cmdlet          Set-WmiInstance                                    Microsoft.PowerShell.Management
Cmdlet          Show-EventLog                                      Microsoft.PowerShell.Management
Cmdlet          Stop-Computer                                      Microsoft.PowerShell.Management
Cmdlet          Test-Connection                                    Microsoft.PowerShell.Management
Cmdlet          Write-EventLog                                     Microsoft.PowerShell.Management

PS C:\Users\Administrator>
```

```PowerShell
PS C:\Users\Windows10-32> Get-Command -CommandType Cmdlet | Where-Object {$_.Parameters.Keys -contains 'ComputerName'}

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Cmdlet          Add-Computer                                       3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Clear-EventLog                                     3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Connect-PSSession                                  3.0.0.0    Microsoft.PowerShell.Core
Cmdlet          Enter-PSSession                                    3.0.0.0    Microsoft.PowerShell.Core
Cmdlet          Get-EventLog                                       3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Get-HotFix                                         3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Get-Process                                        3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Get-PSSession                                      3.0.0.0    Microsoft.PowerShell.Core
Cmdlet          Get-Service                                        3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Get-WmiObject                                      3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Invoke-Command                                     3.0.0.0    Microsoft.PowerShell.Core
Cmdlet          Invoke-WmiMethod                                   3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Limit-EventLog                                     3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          New-EventLog                                       3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          New-PSSession                                      3.0.0.0    Microsoft.PowerShell.Core
Cmdlet          Receive-Job                                        3.0.0.0    Microsoft.PowerShell.Core
Cmdlet          Receive-PSSession                                  3.0.0.0    Microsoft.PowerShell.Core
Cmdlet          Register-WmiEvent                                  3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Remove-Computer                                    3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Remove-EventLog                                    3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Remove-PSSession                                   3.0.0.0    Microsoft.PowerShell.Core
Cmdlet          Remove-WmiObject                                   3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Rename-Computer                                    3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Restart-Computer                                   3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Set-Service                                        3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Set-WmiInstance                                    3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Show-EventLog                                      3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Stop-Computer                                      3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Test-Connection                                    3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Write-EventLog                                     3.1.0.0    Microsoft.PowerShell.Management

PS C:\Users\Windows10-32>
```

- ```Cmdlet``` which accept parameter ```ComputerName``` and ```Credential```

```PowerShell
PS C:\Users\Administrator> Get-Command -CommandType Cmdlet -ParameterName ComputerName,Credential

CommandType     Name                                               ModuleName
-----------     ----                                               ----------
Cmdlet          Add-Computer                                       Microsoft.PowerShell.Management
Cmdlet          Add-Content                                        Microsoft.PowerShell.Management
Cmdlet          Clear-Content                                      Microsoft.PowerShell.Management
Cmdlet          Clear-EventLog                                     Microsoft.PowerShell.Management
Cmdlet          Clear-Item                                         Microsoft.PowerShell.Management
Cmdlet          Clear-ItemProperty                                 Microsoft.PowerShell.Management
Cmdlet          Connect-PSSession                                  Microsoft.PowerShell.Core
Cmdlet          Copy-Item                                          Microsoft.PowerShell.Management
Cmdlet          Copy-ItemProperty                                  Microsoft.PowerShell.Management
Cmdlet          Enter-PSSession                                    Microsoft.PowerShell.Core
Cmdlet          Get-Content                                        Microsoft.PowerShell.Management
Cmdlet          Get-EventLog                                       Microsoft.PowerShell.Management
Cmdlet          Get-HotFix                                         Microsoft.PowerShell.Management
Cmdlet          Get-Item                                           Microsoft.PowerShell.Management
Cmdlet          Get-ItemProperty                                   Microsoft.PowerShell.Management
Cmdlet          Get-Process                                        Microsoft.PowerShell.Management
Cmdlet          Get-PSSession                                      Microsoft.PowerShell.Core
Cmdlet          Get-Service                                        Microsoft.PowerShell.Management
Cmdlet          Get-WmiObject                                      Microsoft.PowerShell.Management
Cmdlet          Invoke-Command                                     Microsoft.PowerShell.Core
Cmdlet          Invoke-Item                                        Microsoft.PowerShell.Management
Cmdlet          Invoke-WmiMethod                                   Microsoft.PowerShell.Management
Cmdlet          Join-Path                                          Microsoft.PowerShell.Management
Cmdlet          Limit-EventLog                                     Microsoft.PowerShell.Management
Cmdlet          Move-Item                                          Microsoft.PowerShell.Management
Cmdlet          Move-ItemProperty                                  Microsoft.PowerShell.Management
Cmdlet          New-EventLog                                       Microsoft.PowerShell.Management
Cmdlet          New-Item                                           Microsoft.PowerShell.Management
Cmdlet          New-ItemProperty                                   Microsoft.PowerShell.Management
Cmdlet          New-PSDrive                                        Microsoft.PowerShell.Management
Cmdlet          New-PSSession                                      Microsoft.PowerShell.Core
Cmdlet          New-Service                                        Microsoft.PowerShell.Management
Cmdlet          New-WebServiceProxy                                Microsoft.PowerShell.Management
Cmdlet          Receive-Job                                        Microsoft.PowerShell.Core
Cmdlet          Receive-PSSession                                  Microsoft.PowerShell.Core
Cmdlet          Register-WmiEvent                                  Microsoft.PowerShell.Management
Cmdlet          Remove-Computer                                    Microsoft.PowerShell.Management
Cmdlet          Remove-EventLog                                    Microsoft.PowerShell.Management
Cmdlet          Remove-Item                                        Microsoft.PowerShell.Management
Cmdlet          Remove-ItemProperty                                Microsoft.PowerShell.Management
Cmdlet          Remove-PSSession                                   Microsoft.PowerShell.Core
Cmdlet          Remove-WmiObject                                   Microsoft.PowerShell.Management
Cmdlet          Rename-Computer                                    Microsoft.PowerShell.Management
Cmdlet          Rename-Item                                        Microsoft.PowerShell.Management
Cmdlet          Rename-ItemProperty                                Microsoft.PowerShell.Management
Cmdlet          Reset-ComputerMachinePassword                      Microsoft.PowerShell.Management
Cmdlet          Resolve-Path                                       Microsoft.PowerShell.Management
Cmdlet          Restart-Computer                                   Microsoft.PowerShell.Management
Cmdlet          Save-Help                                          Microsoft.PowerShell.Core
Cmdlet          Set-Content                                        Microsoft.PowerShell.Management
Cmdlet          Set-Item                                           Microsoft.PowerShell.Management
Cmdlet          Set-ItemProperty                                   Microsoft.PowerShell.Management
Cmdlet          Set-Service                                        Microsoft.PowerShell.Management
Cmdlet          Set-WmiInstance                                    Microsoft.PowerShell.Management
Cmdlet          Show-EventLog                                      Microsoft.PowerShell.Management
Cmdlet          Split-Path                                         Microsoft.PowerShell.Management
Cmdlet          Start-Job                                          Microsoft.PowerShell.Core
Cmdlet          Start-Process                                      Microsoft.PowerShell.Management
Cmdlet          Stop-Computer                                      Microsoft.PowerShell.Management
Cmdlet          Test-ComputerSecureChannel                         Microsoft.PowerShell.Management
Cmdlet          Test-Connection                                    Microsoft.PowerShell.Management
Cmdlet          Test-Path                                          Microsoft.PowerShell.Management
Cmdlet          Update-Help                                        Microsoft.PowerShell.Core
Cmdlet          Write-EventLog                                     Microsoft.PowerShell.Management

PS C:\Users\Administrator>
```

```PowerShell
PS C:\Users\Administrator> Get-Command -CommandType Cmdlet | Where-Object {$_.Parameters.Keys -contains 'ComputerName' -and $_.Parameters.Keys -contains 'Credential'}

CommandType     Name                                               ModuleName
-----------     ----                                               ----------
Cmdlet          Add-Computer                                       Microsoft.PowerShell.Management
Cmdlet          Connect-PSSession                                  Microsoft.PowerShell.Core
Cmdlet          Enter-PSSession                                    Microsoft.PowerShell.Core
Cmdlet          Get-HotFix                                         Microsoft.PowerShell.Management
Cmdlet          Get-PSSession                                      Microsoft.PowerShell.Core
Cmdlet          Get-WmiObject                                      Microsoft.PowerShell.Management
Cmdlet          Invoke-Command                                     Microsoft.PowerShell.Core
Cmdlet          Invoke-WmiMethod                                   Microsoft.PowerShell.Management
Cmdlet          New-PSSession                                      Microsoft.PowerShell.Core
Cmdlet          Receive-PSSession                                  Microsoft.PowerShell.Core
Cmdlet          Register-WmiEvent                                  Microsoft.PowerShell.Management
Cmdlet          Remove-WmiObject                                   Microsoft.PowerShell.Management
Cmdlet          Restart-Computer                                   Microsoft.PowerShell.Management
Cmdlet          Set-WmiInstance                                    Microsoft.PowerShell.Management
Cmdlet          Stop-Computer                                      Microsoft.PowerShell.Management
Cmdlet          Test-Connection                                    Microsoft.PowerShell.Management

PS C:\Users\Administrator>
```

- ```Cmdlet``` which accept parameter ```ComputerName``` and not ```Session ```

```PowerShell
PS C:\Users\Administrator> Get-Command -CommandType Cmdlet | Where-Object {$_.Parameters.Keys -contains 'ComputerName' -and $_.Parameters.Keys -notcontains 'Session'}

CommandType     Name                                               ModuleName
-----------     ----                                               ----------
Cmdlet          Add-Computer                                       Microsoft.PowerShell.Management
Cmdlet          Clear-EventLog                                     Microsoft.PowerShell.Management
Cmdlet          Get-EventLog                                       Microsoft.PowerShell.Management
Cmdlet          Get-HotFix                                         Microsoft.PowerShell.Management
Cmdlet          Get-Process                                        Microsoft.PowerShell.Management
Cmdlet          Get-PSSession                                      Microsoft.PowerShell.Core
Cmdlet          Get-Service                                        Microsoft.PowerShell.Management
Cmdlet          Get-WmiObject                                      Microsoft.PowerShell.Management
Cmdlet          Invoke-WmiMethod                                   Microsoft.PowerShell.Management
Cmdlet          Limit-EventLog                                     Microsoft.PowerShell.Management
Cmdlet          New-EventLog                                       Microsoft.PowerShell.Management
Cmdlet          Register-WmiEvent                                  Microsoft.PowerShell.Management
Cmdlet          Remove-Computer                                    Microsoft.PowerShell.Management
Cmdlet          Remove-EventLog                                    Microsoft.PowerShell.Management
Cmdlet          Remove-WmiObject                                   Microsoft.PowerShell.Management
Cmdlet          Rename-Computer                                    Microsoft.PowerShell.Management
Cmdlet          Restart-Computer                                   Microsoft.PowerShell.Management
Cmdlet          Set-Service                                        Microsoft.PowerShell.Management
Cmdlet          Set-WmiInstance                                    Microsoft.PowerShell.Management
Cmdlet          Show-EventLog                                      Microsoft.PowerShell.Management
Cmdlet          Stop-Computer                                      Microsoft.PowerShell.Management
Cmdlet          Test-Connection                                    Microsoft.PowerShell.Management
Cmdlet          Write-EventLog                                     Microsoft.PowerShell.Management

PS C:\Users\Administrator>
```

- ```Get-Member``` will enumerate the properties and methods of that object

```PowerShell
PS C:\Users\Administrator> Get-Command -CommandType Cmdlet | Get-Member


   TypeName: System.Management.Automation.CmdletInfo

Name                MemberType     Definition
----                ----------     ----------
Equals              Method         bool Equals(System.Object obj)
GetHashCode         Method         int GetHashCode()
GetType             Method         type GetType()
ResolveParameter    Method         System.Management.Automation.ParameterMetadata ResolveParameter(string name)
ToString            Method         string ToString()
CommandType         Property       System.Management.Automation.CommandTypes CommandType {get;}
DefaultParameterSet Property       string DefaultParameterSet {get;}
Definition          Property       string Definition {get;}
HelpFile            Property       string HelpFile {get;}
ImplementingType    Property       type ImplementingType {get;}
Module              Property       psmoduleinfo Module {get;}
ModuleName          Property       string ModuleName {get;}
Name                Property       string Name {get;}
Noun                Property       string Noun {get;}
Options             Property       System.Management.Automation.ScopedItemOptions Options {get;set;}
OutputType          Property       System.Collections.ObjectModel.ReadOnlyCollection[System.Management.Automation.PSTypeName] OutputType {get;}
Parameters          Property       System.Collections.Generic.Dictionary[string,System.Management.Automation.ParameterMetadata] Parameters {get;}
ParameterSets       Property       System.Collections.ObjectModel.ReadOnlyCollection[System.Management.Automation.CommandParameterSetInfo] ParameterSets {get;}
PSSnapIn            Property       System.Management.Automation.PSSnapInInfo PSSnapIn {get;}
RemotingCapability  Property       System.Management.Automation.RemotingCapability RemotingCapability {get;}
Verb                Property       string Verb {get;}
Visibility          Property       System.Management.Automation.SessionStateEntryVisibility Visibility {get;set;}
DLL                 ScriptProperty System.Object DLL {get=$this.ImplementingType.Assembly.Location;}
HelpUri             ScriptProperty System.Object HelpUri {get=$oldProgressPreference = $ProgressPreference...

PS C:\Users\Administrator>
```

- Run ```Get-HotFix``` on the remote machine

In Local Machine

```PowerShell
PS C:\Users\Administrator> $env:COMPUTERNAME
WIN-2012-DC
PS C:\Users\Administrator> $env:USERDOMAIN
PFPT
PS C:\Users\Administrator> $env:USERNAME
Administrator
PS C:\Users\Administrator>
```

In Remote Machine

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
PS C:\Users\Administrator> Get-HotFix -ComputerName JOHN-PC -Credential John-PC\John
```

```PowerShell
PS C:\Users\Administrator> Enter-PSSession -Credential(Get-Credential) -ComputerName JOHN-PC

cmdlet Get-Credential at command pipeline position 1
Supply values for the following parameters:
Credential
[JOHN-PC]: PS C:\Users\John\Documents> Get-HotFix
[JOHN-PC]: PS C:\Users\John\Documents> exit
```

- ```Test-Connection```

```PowerShell
PS C:\Users\Administrator> foreach ($pc in ('JOHN-PC', 'localhost', 'google.com')) {Test-Connection $pc}

Source        Destination     IPV4Address      IPV6Address                              Bytes    Time(ms)
------        -----------     -----------      -----------                              -----    --------
WIN-2012-DC   JOHN-PC         10.0.0.129       fe80::613e:76ef:5029:c2c1%12             32       0
WIN-2012-DC   JOHN-PC         10.0.0.129       fe80::613e:76ef:5029:c2c1%12             32       0
WIN-2012-DC   JOHN-PC         10.0.0.129       fe80::613e:76ef:5029:c2c1%12             32       0
WIN-2012-DC   JOHN-PC         10.0.0.129       fe80::613e:76ef:5029:c2c1%12             32       0
WIN-2012-DC   localhost       127.0.0.1        ::1                                      32       0
WIN-2012-DC   localhost       127.0.0.1        ::1                                      32       0
WIN-2012-DC   localhost       127.0.0.1        ::1                                      32       0
WIN-2012-DC   localhost       127.0.0.1        ::1                                      32       0
WIN-2012-DC   google.com      216.58.194.206   2607:f8b0:4005:806::200e                 32       25
WIN-2012-DC   google.com      216.58.194.206   2607:f8b0:4005:806::200e                 32       16
WIN-2012-DC   google.com      216.58.194.206   2607:f8b0:4005:806::200e                 32       15
WIN-2012-DC   google.com      216.58.194.206   2607:f8b0:4005:806::200e                 32       17


PS C:\Users\Administrator>
```

###### Exercise

- Set up a Windows 7 VM on your computer.
- Using ```Get-HotFix``` with the ```–ComputerName``` and ```-Credential``` parameters, check for the presence of ```KB2871997``` (the Pass the hash fix) on the VM

```PowerShell
PS C:\Users\Administrator> Get-HotFix -ComputerName JOHN-PC -Credential John-PC\John -id KB2871997
Get-HotFix : Cannot find the requested hotfix on the 'JOHN-PC' computer. Verify the input and run the command again.
At line:1 char:1
+ Get-HotFix -ComputerName JOHN-PC -Credential John-PC\John -id KB2871997
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (:) [Get-HotFix], ArgumentException
    + FullyQualifiedErrorId : GetHotFixNoEntriesFound,Microsoft.PowerShell.Commands.GetHotFixCommand

PS C:\Users\Administrator>
```

```PowerShell
PS C:\Users\Administrator> Enter-PSSession -Credential(Get-Credential) -ComputerName JOHN-PC

cmdlet Get-Credential at command pipeline position 1
Supply values for the following parameters:
Credential
[JOHN-PC]: PS C:\Users\John\Documents> Get-HotFix
[JOHN-PC]: PS C:\Users\John\Documents> Get-HotFix -id KB2871997
Get-HotFix : This command cannot find hot-fix on the machine 'localhost'. Verify the input and Run your command again.
    + CategoryInfo          : ObjectNotFound: (:) [Get-HotFix], ArgumentException
    + FullyQualifiedErrorId : GetHotFixNoEntriesFound,Microsoft.PowerShell.Commands.GetHotFixCommand

[JOHN-PC]: PS C:\Users\John\Documents> exit
PS C:\Users\Administrator>
```

###### Remoting Issues Fix

- Disable Firewall
- [```WSMan:\localhost\client\trustedhosts``` on local machine](https://github.com/Kan1shka9/PowerShell-for-Pentesters/blob/master/21-Remoting-Part-2.md#21-remoting-part-2)
- [Windows Update Module for PowerShell Access Denied on Remote PC in Workgroup](https://community.spiceworks.com/topic/954498-windows-update-module-for-powershell-access-denied-on-remote-pc-in-workgroup?page=1#entry-4650660)
- [Run remote powershell as administrator](https://serverfault.com/questions/473991/run-remote-powershell-as-administrator)
