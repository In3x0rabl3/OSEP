#### 2. Introduction to Powershell

###### [PowerShell](https://technet.microsoft.com/en-us/library/bb978526.aspx)

- Windows PowerShell is a task-based command-line shell and scripting language designed especially for system administration.
- Built on the .NET Framework, Windows PowerShell helps IT professionals and power users control and automate the administration of the Windows operating system and applications that run on Windows
- A powerful shell and scripting language already present on the most general targets in a pen test – Windows computers.
- Less dependence on Metasploit and *nix based scripting.
- Stick to PowerShell v2 as this is the version available on most of the targets (default on Windows 7 and Server 2008 R2)
- Provides access to almost everything on a Windows platform which could be useful for us as attackers.
- Easy to learn and really powerful.
- Based on .Net framework and is tightly integrated with Windows.
- Trusted by the countermeasures and system administrators.

- Get ```powershell version```

```Powershell
PS C:\Users\Windows-32> Get-Host


Name             : ConsoleHost
Version          : 2.0
InstanceId       : 648eccf6-c720-415f-af58-3a94b395097a
UI               : System.Management.Automation.Internal.Host.InternalHostUserInterface
CurrentCulture   : en-US
CurrentUICulture : en-US
PrivateData      : Microsoft.PowerShell.ConsoleHost+ConsoleColorProxy
IsRunspacePushed : False
Runspace         : System.Management.Automation.Runspaces.LocalRunspace



PS C:\Users\Windows-32>
```

- ```Directory Listing```

```Powershell
PS C:\> dir


    Directory: C:\


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----         7/13/2009   7:37 PM            PerfLogs
d-r--         5/28/2017   2:21 PM            Program Files
d-r--         5/28/2017  11:33 AM            Users
d----         5/28/2017   2:21 PM            Windows
-a---         6/10/2009   2:42 PM         24 autoexec.bat
-a---         6/10/2009   2:42 PM         10 config.sys


PS C:\>
```
```Powershell
PS C:\> ls


    Directory: C:\


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----         7/13/2009   7:37 PM            PerfLogs
d-r--         5/28/2017   2:21 PM            Program Files
d-r--         5/28/2017  11:33 AM            Users
d----         5/28/2017   2:21 PM            Windows
-a---         6/10/2009   2:42 PM         24 autoexec.bat
-a---         6/10/2009   2:42 PM         10 config.sys


PS C:\>
```

- ```Process Listing```

```Powershell
PS C:\> ps

Handles  NPM(K)    PM(K)      WS(K) VM(M)   CPU(s)     Id ProcessName
-------  ------    -----      ----- -----   ------     -- -----------
    125       5    14936      13560    43             996 audiodg
     51       3     1572       4648    46     0.02   2588 conhost
    496       5     1092       2740    33             344 csrss
    190       6     1060       3344    31             400 csrss
     70       4      980       3584    40     0.03    300 dwm
    740      23    25336      34964   169     1.34    356 explorer
      0       0        0         12     0               0 Idle
     41       3     1656       3488    52     0.00    332 jusched
    758      13     2804       7792    36             492 lsass
    152       4     1048       2684    14             500 lsm
    332      10    35048      34128   167     0.43   2580 powershell
    586      13    11612       7032    81            1180 SearchIndexer
    234       9     4412       7440    39             484 services
     29       1      260        712     4             268 smss
    302      10     4384       8316    58            1332 spoolsv
    150       4     1844       6540    29            1516 sppsvc
    358       7     2516       6156    35             608 svchost
    261       8     2064       4760    26             720 svchost
    506      12    13364      13024    74             772 svchost
    563      14    18352      25724    86             892 svchost
   1014      29    13012      21836   102             932 svchost
    534      19     6176      10936    52            1100 svchost
    421      14     7660       9644    56            1228 svchost
    328      26     7852       9072    42            1368 svchost
    377      17     5236      10136    69            1460 svchost
    101       7     1096       3828    25            1820 svchost
    352      39     7232       9140    63            2364 svchost
    534       0       44        540     2               4 System
    153       8     2120       4836    40     0.03   2028 taskhost
    117       5     1428       3924    44             668 VBoxService
    143       6     1320       4740    62     0.04   1612 VBoxTray
     89       6      952       3200    33             392 wininit
    120       5     1600       4468    39             440 winlogon
    113       4     1796       4452    27            2524 WmiPrvSE
    469      16     7412      19308   108            2088 wmpnetwk


PS C:\>
```

- ```Powershell help system```

```Powershell
PS C:\> Get-Help
TOPIC
    Get-Help

SHORT DESCRIPTION
    Displays help about Windows PowerShell cmdlets and concepts.

LONG DESCRIPTION

SYNTAX
    get-help {<CmdletName> | <TopicName>}
    help {<CmdletName> | <TopicName>}
    <CmdletName> -?

    "Get-help" and "-?" display help on one page.
    "Help" displays help on multiple pages.

    Examples:
      get-help get-process   : Displays help about the Get-Process cmdlet.
      get-help about_signing : Displays help about signing scripts.
      help where-object      : Displays help about the Where-Object cmdlet.
      help about_foreach     : Displays help about foreach loops in PowerShell.
      set-service -?         : Displays help about the Set-Service cmdlet.

    You can use wildcard characters in the help commands (not with -?).
    If multiple help topics match, PowerShell displays a list of matching
    topics. If only one help topic matches, PowerShell displays the topic.

    Examples:
      get-help *      : Displays all help topics.
      get-help get-*  : Displays topics that begin with get-.
      help *object*   : Displays topics with "object" in the name.
      get-help about* : Displays all conceptual topics.


    For information about wildcards, type:
      get-help about_wildcard


REMARKS
    To learn about Windows PowerShell, read the following help topics:
      get-command  : Gets information about cmdlets from the cmdlet code.
      get-member   : Gets the properties and methods of an object.
      where-object : Filters object properties.
      about_object : Explains the use of objects in Windows PowerShell.
      about_remote : Tells how to run commands on remote computers.

    Conceptual help files are named "about_<topic>", such as:
      about_regular_expression.

    The names of conceptual help files must be entered in English
    even on non-English versions of Windows PowerShell.

    The help commands also display the aliases of the cmdlets. These
    are alternate names or nicknames that are often easier to type.
    For example, the alias for the Invoke-Command cmdlet is "remote".

    To get the aliases, type:

      get-alias

PS C:\>
```

- Get all ```powershell help topics```

```Powershell
PS C:\> Get-Help *

Name                              Category  Synopsis
----                              --------  --------
ac                                Alias     Add-Content
asnp                              Alias     Add-PSSnapin
clc                               Alias     Clear-Content
cli                               Alias     Clear-Item
clp                               Alias     Clear-ItemProperty
clv                               Alias     Clear-Variable
compare                           Alias     Compare-Object
cpi                               Alias     Copy-Item
cpp                               Alias     Copy-ItemProperty
cvpa                              Alias     Convert-Path
dbp                               Alias     Disable-PSBreakpoint
diff                              Alias     Compare-Object
ebp                               Alias     Enable-PSBreakpoint
epal                              Alias     Export-Alias
epcsv                             Alias     Export-Csv
fc                                Alias     Format-Custom
fl                                Alias     Format-List
foreach                           Alias     ForEach-Object
%                                 Alias     ForEach-Object
ft                                Alias     Format-Table
fw                                Alias     Format-Wide
gal                               Alias     Get-Alias
gbp                               Alias     Get-PSBreakpoint
gc                                Alias     Get-Content
gci                               Alias     Get-ChildItem
gcm                               Alias     Get-Command
gdr                               Alias     Get-PSDrive
gcs                               Alias     Get-PSCallStack
ghy                               Alias     Get-History
gi                                Alias     Get-Item
gl                                Alias     Get-Location
gm                                Alias     Get-Member
gmo                               Alias     Get-Module
gp                                Alias     Get-ItemProperty
gps                               Alias     Get-Process
group                             Alias     Group-Object
gsv                               Alias     Get-Service
gsnp                              Alias     Get-PSSnapin
gu                                Alias     Get-Unique
gv                                Alias     Get-Variable
gwmi                              Alias     Get-WmiObject
iex                               Alias     Invoke-Expression
ihy                               Alias     Invoke-History
ii                                Alias     Invoke-Item
ipmo                              Alias     Import-Module
iwmi                              Alias     Invoke-WmiMethod
ipal                              Alias     Import-Alias
ipcsv                             Alias     Import-Csv
measure                           Alias     Measure-Object
mi                                Alias     Move-Item
mp                                Alias     Move-ItemProperty
nal                               Alias     New-Alias
ndr                               Alias     New-PSDrive
ni                                Alias     New-Item
nv                                Alias     New-Variable
nmo                               Alias     New-Module
oh                                Alias     Out-Host
ogv                               Alias     Out-GridView
ise                               Alias     powershell_ise.exe
rbp                               Alias     Remove-PSBreakpoint
rdr                               Alias     Remove-PSDrive
ri                                Alias     Remove-Item
rni                               Alias     Rename-Item
rnp                               Alias     Rename-ItemProperty
rp                                Alias     Remove-ItemProperty
rmo                               Alias     Remove-Module
rsnp                              Alias     Remove-PSSnapin
rv                                Alias     Remove-Variable
rwmi                              Alias     Remove-WmiObject
rvpa                              Alias     Resolve-Path
sal                               Alias     Set-Alias
sasv                              Alias     Start-Service
sbp                               Alias     Set-PSBreakpoint
sc                                Alias     Set-Content
select                            Alias     Select-Object
si                                Alias     Set-Item
sl                                Alias     Set-Location
swmi                              Alias     Set-WmiInstance
sleep                             Alias     Start-Sleep
sort                              Alias     Sort-Object
sp                                Alias     Set-ItemProperty
saps                              Alias     Start-Process
start                             Alias     Start-Process
spps                              Alias     Stop-Process
spsv                              Alias     Stop-Service
sv                                Alias     Set-Variable
tee                               Alias     Tee-Object
where                             Alias     Where-Object
?                                 Alias     Where-Object
write                             Alias     Write-Output
cat                               Alias     Get-Content
cd                                Alias     Set-Location
clear                             Alias     Clear-Host
cp                                Alias     Copy-Item
h                                 Alias     Get-History
history                           Alias     Get-History
kill                              Alias     Stop-Process
lp                                Alias     Out-Printer
ls                                Alias     Get-ChildItem
man                               Alias     help
mount                             Alias     New-PSDrive
md                                Alias     mkdir
mv                                Alias     Move-Item
popd                              Alias     Pop-Location
ps                                Alias     Get-Process
pushd                             Alias     Push-Location
pwd                               Alias     Get-Location
r                                 Alias     Invoke-History
rm                                Alias     Remove-Item
rmdir                             Alias     Remove-Item
echo                              Alias     Write-Output
cls                               Alias     Clear-Host
chdir                             Alias     Set-Location
copy                              Alias     Copy-Item
del                               Alias     Remove-Item
dir                               Alias     Get-ChildItem
erase                             Alias     Remove-Item
move                              Alias     Move-Item
rd                                Alias     Remove-Item
ren                               Alias     Rename-Item
set                               Alias     Set-Variable
type                              Alias     Get-Content
icm                               Alias     Invoke-Command
clhy                              Alias     Clear-History
gjb                               Alias     Get-Job
rcjb                              Alias     Receive-Job
rjb                               Alias     Remove-Job
sajb                              Alias     Start-Job
spjb                              Alias     Stop-Job
wjb                               Alias     Wait-Job
nsn                               Alias     New-PSSession
gsn                               Alias     Get-PSSession
rsn                               Alias     Remove-PSSession
ipsn                              Alias     Import-PSSession
epsn                              Alias     Export-PSSession
etsn                              Alias     Enter-PSSession
exsn                              Alias     Exit-PSSession
Get-WinEvent                      Cmdlet    Gets events from event logs and event tracing log files on local and rem...
Get-Counter                       Cmdlet    Gets performance counter data from local and remote computers.
Import-Counter                    Cmdlet    Imports performance counter log files (.blg, .csv, .tsv) and creates the...
Export-Counter                    Cmdlet    The Export-Counter cmdlet takes PerformanceCounterSampleSet objects and ...
Disable-WSManCredSSP              Cmdlet    Disables Credential Security Service Provider (CredSSP) authentication o...
Enable-WSManCredSSP               Cmdlet    Enables Credential Security Service Provider (CredSSP) authentication on...
Get-WSManCredSSP                  Cmdlet    Gets the Credential Security Service Provider-related configuration for ...
Set-WSManQuickConfig              Cmdlet    Configures the local computer for remote management.
Test-WSMan                        Cmdlet    Tests whether the WinRM service is running on a local or remote computer.
Invoke-WSManAction                Cmdlet    Invokes an action on the object that is specified by the Resource URI an...
Connect-WSMan                     Cmdlet    Connects to the WinRM service on a remote computer.
Disconnect-WSMan                  Cmdlet    Disconnects the client from the WinRM service on a remote computer.
Get-WSManInstance                 Cmdlet    Displays management information for a resource instance specified by a R...
Set-WSManInstance                 Cmdlet    Modifies the management information that is related to a resource.
Remove-WSManInstance              Cmdlet    Deletes a management resource instance.
New-WSManInstance                 Cmdlet    Creates a new instance of a management resource.
New-WSManSessionOption            Cmdlet    Creates a WS-Management session option hash table to use as input parame...
Get-Command                       Cmdlet    Gets basic information about cmdlets and other elements of Windows Power...
Get-Help                          Cmdlet    Displays information about Windows PowerShell commands and concepts.
Get-History                       Cmdlet    Gets a list of the commands entered during the current session.
Invoke-History                    Cmdlet    Runs commands from the session history.
Add-History                       Cmdlet    Appends entries to the session history.
Clear-History                     Cmdlet    Deletes entries from the command history.
Register-PSSessionConfiguration   Cmdlet    Creates and registers a new session configuration.
Unregister-PSSessionConfiguration Cmdlet    Deletes registered session configurations from the computer.
Get-PSSessionConfiguration        Cmdlet    Gets the registered session configurations on the computer.
Set-PSSessionConfiguration        Cmdlet    Changes the properties of a registered session configuration.
Enable-PSSessionConfiguration     Cmdlet    Enables the session configurations on the local computer.
Disable-PSSessionConfiguration    Cmdlet    Denies access to the session configurations on the local computer.
Enable-PSRemoting                 Cmdlet    Configures the computer to receive remote commands.
Invoke-Command                    Cmdlet    Runs commands on local and remote computers.
New-PSSession                     Cmdlet    Creates a persistent connection to a local or remote computer.
Get-PSSession                     Cmdlet    Gets the Windows PowerShell sessions (PSSessions) in the current session.
Remove-PSSession                  Cmdlet    Closes one or more Windows PowerShell sessions (PSSessions).
Start-Job                         Cmdlet    Starts a Windows PowerShell background job.
Get-Job                           Cmdlet    Gets Windows PowerShell background jobs that are running in the current ...
Receive-Job                       Cmdlet    Gets the results of the Windows PowerShell background jobs in the curren...
Stop-Job                          Cmdlet    Stops a Windows PowerShell background job.
Wait-Job                          Cmdlet    Suppresses the command prompt until one or all of the Windows PowerShell...
Remove-Job                        Cmdlet    Deletes a Windows PowerShell background job.
Enter-PSSession                   Cmdlet    Starts an interactive session with a remote computer.
Exit-PSSession                    Cmdlet    Ends an interactive session with a remote computer.
New-PSSessionOption               Cmdlet    Creates an object that contains advanced options for a PSSession.
ForEach-Object                    Cmdlet    Performs an operation against each of a set of input objects.
Where-Object                      Cmdlet    Creates a filter that controls which objects will be passed along a comm...
Set-PSDebug                       Cmdlet    Turns script debugging features on and off, sets the trace level, and to...
Set-StrictMode                    Cmdlet    Establishes and enforces coding rules in expressions, scripts, and scrip...
New-Module                        Cmdlet    Creates a new dynamic module that exists only in memory.
Import-Module                     Cmdlet    Adds modules to the current session.
Export-ModuleMember               Cmdlet    Specifies the module members that are exported.
Get-Module                        Cmdlet    Gets the modules that have been imported or that can be imported into th...
Remove-Module                     Cmdlet    Removes modules from the current session.
New-ModuleManifest                Cmdlet    Creates a new module manifest.
Test-ModuleManifest               Cmdlet    Verifies that a module manifest file accurately describes the contents o...
Add-PSSnapin                      Cmdlet    Adds one or more Windows PowerShell snap-ins to the current session.
Remove-PSSnapin                   Cmdlet    Removes Windows PowerShell snap-ins from the current session.
Get-PSSnapin                      Cmdlet    Gets the Windows PowerShell snap-ins on the computer.
Export-Console                    Cmdlet    Exports the names of snap-ins in the current session to a console file.
Format-List                       Cmdlet    Formats the output as a list of properties in which each property appear...
Format-Custom                     Cmdlet    Uses a customized view to format the output.
Format-Table                      Cmdlet    Formats the output as a table.
Format-Wide                       Cmdlet    Formats objects as a wide table that displays only one property of each ...
Out-Null                          Cmdlet    Deletes output instead of sending it to the console.
Out-Default                       Cmdlet    Sends the output to the default formatter and to the default output cmdlet.
Out-Host                          Cmdlet    Sends output to the command line.
Out-File                          Cmdlet    Sends output to a file.
Out-Printer                       Cmdlet    Sends output to a printer.
Out-String                        Cmdlet    Sends objects to the host as a series of strings.
Out-GridView                      Cmdlet    Sends output to an interactive table in a separate window.
Get-FormatData                    Cmdlet    Gets the formatting data in the current session.
Export-FormatData                 Cmdlet    Saves formatting data from the current session in a formatting file.
Register-ObjectEvent              Cmdlet    Subscribes to the events that are generated by a Microsoft .NET Framewor...
Register-EngineEvent              Cmdlet    Subscribes to events that are generated by the Windows PowerShell engine...
Wait-Event                        Cmdlet    Waits until a particular event is raised before continuing to run.
Get-Event                         Cmdlet    Gets the events in the event queue.
Remove-Event                      Cmdlet    Deletes events from the event queue.
Get-EventSubscriber               Cmdlet    Gets the event subscribers in the current session.
Unregister-Event                  Cmdlet    Cancels an event subscription.
New-Event                         Cmdlet    Creates a new event.
Add-Member                        Cmdlet    Adds a user-defined custom member to an instance of a Windows PowerShell...
Add-Type                          Cmdlet    Adds a Microsoft .NET Framework type (a class) to a Windows PowerShell s...
Compare-Object                    Cmdlet    Compares two sets of objects.
ConvertTo-Html                    Cmdlet    Converts Microsoft .NET Framework objects into HTML that can be displaye...
ConvertFrom-StringData            Cmdlet    Converts a string containing one or more key/value pairs to a hash table.
Export-CSV                        Cmdlet    Converts Microsoft .NET Framework objects into a series of comma-separat...
Import-CSV                        Cmdlet    Converts object properties in a comma-separated value (CSV) file into CS...
ConvertTo-CSV                     Cmdlet    Converts Microsoft .NET Framework objects into a series of comma-separat...
ConvertFrom-CSV                   Cmdlet    Converts object properties in comma-separated value (CSV) format into CS...
Export-Alias                      Cmdlet    Exports information about currently defined aliases to a file.
Invoke-Expression                 Cmdlet    Runs commands or expressions on the local computer.
Get-Alias                         Cmdlet    Gets the aliases for the current session.
Get-Culture                       Cmdlet    Gets the current culture set in the operating system.
Get-Date                          Cmdlet    Gets the current date and time.
Get-Host                          Cmdlet    Gets an object that represents the current host program. And, displays W...
Get-Member                        Cmdlet    Gets the properties and methods of objects.
Get-Random                        Cmdlet    Gets a random number, or selects objects randomly from a collection.
Get-UICulture                     Cmdlet    Gets the current user interface (UI) culture settings in the operating s...
Get-Unique                        Cmdlet    Returns the unique items from a sorted list.
Export-PSSession                  Cmdlet    Imports commands from another session and saves them in a Windows PowerS...
Import-PSSession                  Cmdlet    Imports commands from another session into the current session.
Import-Alias                      Cmdlet    Imports an alias list from a file.
Import-LocalizedData              Cmdlet    Imports language-specific data into scripts and functions based on the U...
Select-String                     Cmdlet    Finds text in strings and files.
Measure-Object                    Cmdlet    Calculates the numeric properties of objects, and the characters, words,...
New-Alias                         Cmdlet    Creates a new alias.
New-TimeSpan                      Cmdlet    Creates a TimeSpan object.
Read-Host                         Cmdlet    Reads a line of input from the console.
Set-Alias                         Cmdlet    Creates or changes an alias (alternate name) for a cmdlet or other comma...
Set-Date                          Cmdlet    Changes the system time on the computer to a time that you specify.
Start-Sleep                       Cmdlet    Suspends the activity in a script or session for the specified period of...
Tee-Object                        Cmdlet    Saves command output in a file or variable, and displays it in the console.
Measure-Command                   Cmdlet    Measures the time it takes to run script blocks and cmdlets.
Update-List                       Cmdlet    Adds items to and removes items from a property value that contains a co...
Update-TypeData                   Cmdlet    Updates the current extended type configuration by reloading the *.types...
Update-FormatData                 Cmdlet    Updates the formatting data in the current session.
Write-Host                        Cmdlet    Writes customized output to a host.
Write-Progress                    Cmdlet    Displays a progress bar within a Windows PowerShell command window.
New-Object                        Cmdlet    Creates an instance of a Microsoft .NET Framework or COM object.
Select-Object                     Cmdlet    Selects specified properties of an object or set of objects. It can also...
Group-Object                      Cmdlet    Groups objects that contain the same value for specified properties.
Sort-Object                       Cmdlet    Sorts objects by property values.
Get-Variable                      Cmdlet    Gets the variables in the current console.
New-Variable                      Cmdlet    Creates a new variable.
Set-Variable                      Cmdlet    Sets the value of a variable. Creates the variable if one with the reque...
Remove-Variable                   Cmdlet    Deletes a variable and its value.
Clear-Variable                    Cmdlet    Deletes the value of a variable.
Export-Clixml                     Cmdlet    Creates an XML-based representation of an object or objects and stores i...
Import-Clixml                     Cmdlet    Imports a CLIXML file and creates corresponding objects within Windows P...
ConvertTo-XML                     Cmdlet    Creates an XML-based representation of an object.
Select-XML                        Cmdlet    Finds text in an XML string or document.
Write-Debug                       Cmdlet    Writes a debug message to the console.
Write-Verbose                     Cmdlet    Writes text to the verbose message stream.
Write-Warning                     Cmdlet    Writes a warning message.
Write-Error                       Cmdlet    Writes an object to the error stream.
Write-Output                      Cmdlet    Sends the specified objects to the next command in the pipeline. If the ...
Set-PSBreakpoint                  Cmdlet    Sets a breakpoint on a line, command, or variable.
Get-PSBreakpoint                  Cmdlet    Gets the breakpoints that are set in the current session.
Remove-PSBreakpoint               Cmdlet    Deletes breakpoints from the current console.
Enable-PSBreakpoint               Cmdlet    Enables the breakpoints in the current console.
Disable-PSBreakpoint              Cmdlet    Disables the breakpoints in the current console.
Get-PSCallStack                   Cmdlet    Displays the current call stack.
Send-MailMessage                  Cmdlet    Sends an e-mail message.
Get-TraceSource                   Cmdlet    Gets the Windows PowerShell components that are instrumented for tracing.
Set-TraceSource                   Cmdlet    Configures, starts, and stops a trace of Windows PowerShell components.
Trace-Command                     Cmdlet    Configures and starts a trace of the specified expression or command.
Start-Transcript                  Cmdlet    Creates a record of all or part of a Windows PowerShell session in a tex...
Stop-Transcript                   Cmdlet    Stops a transcript.
Add-Content                       Cmdlet    Adds content to the specified items, such as adding words to a file.
Clear-Content                     Cmdlet    Deletes the contents of an item, such as deleting the text from a file, ...
Clear-ItemProperty                Cmdlet    Deletes the value of a property but does not delete the property.
Join-Path                         Cmdlet    Combines a path and a child path into a single path. The provider suppli...
Convert-Path                      Cmdlet    Converts a path from a Windows PowerShell path to a Windows PowerShell p...
Copy-ItemProperty                 Cmdlet    Copies a property and value from a specified location to another location.
Get-EventLog                      Cmdlet    Gets the events in an event log, or a list of the event logs, on the loc...
Clear-EventLog                    Cmdlet    Deletes all entries from specified event logs on the local or remote com...
Write-EventLog                    Cmdlet    Writes an event to an event log.
Limit-EventLog                    Cmdlet    Sets the event log properties that limit the size of the event log and t...
Show-EventLog                     Cmdlet    Displays the event logs of the local or a remote computer in Event Viewer.
New-EventLog                      Cmdlet    Creates a new event log and a new event source on a local or remote comp...
Remove-EventLog                   Cmdlet    Deletes an event log or unregisters an event source.
Get-ChildItem                     Cmdlet    Gets the items and child items in one or more specified locations.
Get-Content                       Cmdlet    Gets the content of the item at the specified location.
Get-ItemProperty                  Cmdlet    Gets the properties of a specified item.
Get-WmiObject                     Cmdlet    Gets instances of Windows Management Instrumentation (WMI) classes or in...
Invoke-WmiMethod                  Cmdlet    Calls Windows Management Instrumentation (WMI) methods.
Move-ItemProperty                 Cmdlet    Moves a property from one location to another.
Get-Location                      Cmdlet    Gets information about the current working location.
Set-Location                      Cmdlet    Sets the current working location to a specified location.
Push-Location                     Cmdlet    Adds the current location to the top of a list of locations (a "stack").
Pop-Location                      Cmdlet    Changes the current location to the location most recently pushed onto t...
New-PSDrive                       Cmdlet    Creates a Windows PowerShell drive in the current session.
Remove-PSDrive                    Cmdlet    Removes a Windows PowerShell drive from its location.
Get-PSDrive                       Cmdlet    Gets the Windows PowerShell drives in the current session.
Get-Item                          Cmdlet    Gets the item at the specified location.
New-Item                          Cmdlet    Creates a new item.
Set-Item                          Cmdlet    Changes the value of an item to the value specified in the command.
Remove-Item                       Cmdlet    Deletes the specified items.
Move-Item                         Cmdlet    Moves an item from one location to another.
Rename-Item                       Cmdlet    Renames an item in a Windows PowerShell provider namespace.
Copy-Item                         Cmdlet    Copies an item from one location to another within a namespace.
Clear-Item                        Cmdlet    Deletes the contents of an item, but does not delete the item.
Invoke-Item                       Cmdlet    Performs the default action on the specified item.
Get-PSProvider                    Cmdlet    Gets information about the specified Windows PowerShell provider.
New-ItemProperty                  Cmdlet    Creates a new property for an item and sets its value. For example, you ...
Split-Path                        Cmdlet    Returns the specified part of a path.
Test-Path                         Cmdlet    Determines whether all elements of a path exist.
Get-Process                       Cmdlet    Gets the processes that are running on the local computer or a remote co...
Stop-Process                      Cmdlet    Stops one or more running processes.
Wait-Process                      Cmdlet    Waits for the processes to be stopped before accepting more input.
Debug-Process                     Cmdlet    Debugs one or more processes running on the local computer.
Start-Process                     Cmdlet    Starts one or more processes on the local computer.
Remove-ItemProperty               Cmdlet    Deletes the property and its value from an item.
Remove-WmiObject                  Cmdlet    Deletes an instance of an existing Windows Management Instrumentation (W...
Rename-ItemProperty               Cmdlet    Renames a property of an item.
Register-WmiEvent                 Cmdlet    Subscribes to a Windows Management Instrumentation (WMI) event.
Resolve-Path                      Cmdlet    Resolves the wildcard characters in a path, and displays the path contents.
Get-Service                       Cmdlet    Gets the services on a local or remote computer.
Stop-Service                      Cmdlet    Stops one or more running services.
Start-Service                     Cmdlet    Starts one or more stopped services.
Suspend-Service                   Cmdlet    Suspends (pauses) one or more running services.
Resume-Service                    Cmdlet    Resumes one or more suspended (paused) services.
Restart-Service                   Cmdlet    Stops and then starts one or more services.
Set-Service                       Cmdlet    Starts, stops, and suspends a service, and changes its properties.
New-Service                       Cmdlet    Creates a new Windows service.
Set-Content                       Cmdlet    Writes or replaces the content in an item with new content.
Set-ItemProperty                  Cmdlet    Creates or changes the value of a property of an item.
Set-WmiInstance                   Cmdlet    Creates or updates an instance of an existing Windows Management Instrum...
Get-Transaction                   Cmdlet    Gets the current (active) transaction.
Start-Transaction                 Cmdlet    Starts a transaction.
Complete-Transaction              Cmdlet    Commits the active transaction.
Undo-Transaction                  Cmdlet    Rolls back the active transaction.
Use-Transaction                   Cmdlet    Adds the script block to the active transaction.
New-WebServiceProxy               Cmdlet    Creates a Web service proxy object that lets you use and manage the Web ...
Get-HotFix                        Cmdlet    Gets the hotfixes that have been applied to the local and remote computers.
Test-Connection                   Cmdlet    Sends ICMP echo request packets ("pings") to one or more computers.
Enable-ComputerRestore            Cmdlet    Enables the System Restore feature on the specified file system drive.
Disable-ComputerRestore           Cmdlet    Disables the System Restore feature on the specified file system drive.
Checkpoint-Computer               Cmdlet    Creates a system restore point on the local computer.
Get-ComputerRestorePoint          Cmdlet    Gets the restore points on the local computer.
Restart-Computer                  Cmdlet    Restarts ("reboots") the operating system on local and remote computers.
Stop-Computer                     Cmdlet    Stops (shuts down) local and remote computers.
Restore-Computer                  Cmdlet    Starts a system restore on the local computer.
Add-Computer                      Cmdlet    Add the local computer to a domain or workgroup.
Remove-Computer                   Cmdlet    Remove the local computer from a workgroup or domain.
Test-ComputerSecureChannel        Cmdlet    Tests and repairs the secure channel between the local computer and its ...
Reset-ComputerMachinePassword     Cmdlet    Resets the machine account password for the computer.
Get-Acl                           Cmdlet    Gets the security descriptor for a resource, such as a file or registry ...
Set-Acl                           Cmdlet    Changes the security descriptor of a specified resource, such as a file ...
Get-PfxCertificate                Cmdlet    Gets information about .pfx certificate files on the computer.
Get-Credential                    Cmdlet    Gets a credential object based on a user name and password.
Get-ExecutionPolicy               Cmdlet    Gets the execution policies for the current session.
Set-ExecutionPolicy               Cmdlet    Changes the user preference for the Windows PowerShell execution policy.
Get-AuthenticodeSignature         Cmdlet    Gets information about the Authenticode signature in a file.
Set-AuthenticodeSignature         Cmdlet    Adds an Authenticode signature to a Windows PowerShell script or other f...
ConvertFrom-SecureString          Cmdlet    Converts a secure string into an encrypted standard string.
ConvertTo-SecureString            Cmdlet    Converts encrypted standard strings to secure strings. It can also conve...
WSMan                             Provider  Provides access to Web Services for Management (WS-Management) configura...
Alias                             Provider  Provides access to the Windows PowerShell aliases and the values that th...
Environment                       Provider  Provides access to the Windows environment variables.
FileSystem                        Provider  Provides access to files and directories.
Function                          Provider  Provides access to the functions defined in Windows PowerShell.
Registry                          Provider  Provides access to the system registry keys and values from Windows Powe...
Variable                          Provider  Provides access to the Windows PowerShell variables and to their values.
Certificate                       Provider  Provides access to X.509 certificate stores and certificates from within...
about_aliases                     HelpFile  Describes how to use alternate names for cmdlets and commands in Windows
about_Arithmetic_Operators        HelpFile  Describes the operators that perform arithmetic in Windows PowerShell.
about_arrays                      HelpFile  Describes a compact data structure for storing data elements.
about_Assignment_Operators        HelpFile  Describes how to use operators to assign values to variables.
about_Automatic_Variables         HelpFile  Describes variables that store state information for Windows PowerShell.
about_Break                       HelpFile  Describes a statement you can use to immediately exit Foreach, For, While,
about_command_precedence          HelpFile  Describes how Windows PowerShell determines which command to run.
about_Command_Syntax              HelpFile  Describes the notation used for Windows PowerShell syntax in Help.
about_Comment_Based_Help          HelpFile  Describes how to write comment-based Help topics for functions and scripts.
about_CommonParameters            HelpFile  Describes the parameters that can be used with any cmdlet.
about_Comparison_Operators        HelpFile  Describes the operators that compare values in Windows PowerShell.
about_Continue                    HelpFile  Describes how the Continue statement immediately returns the program flow
about_Core_Commands               HelpFile  Lists the cmdlets that are designed for use with Windows PowerShell
about_data_sections               HelpFile  Explains Data sections, which isolate text strings and other read-only
about_debuggers                   HelpFile  Describes the Windows PowerShell debugger.
about_do                          HelpFile  Runs a statement list one or more times, subject to a While or Until
about_environment_variables       HelpFile  Describes how to access Windows environment variables in Windows
about_escape_characters           HelpFile  Introduces the escape character in Windows PowerShell and explains
about_eventlogs                   HelpFile  Windows PowerShell creates a Windows event log that is
about_execution_policies          HelpFile  Describes the Windows PowerShell execution policies and explains
about_For                         HelpFile  Describes a language command you can use to run statements based on a
about_Foreach                     HelpFile  Describes a language command you can use to traverse all the items in a
about_format.ps1xml               HelpFile  The Format.ps1xml files in Windows PowerShell define the default display
about_functions                   HelpFile  Describes how to create and use functions in Windows PowerShell.
about_functions_advanced          HelpFile  Introduces advanced functions that act similar to cmdlets.
about_functions_advanced_methods  HelpFile  Describes how functions that specify the CmdletBinding attribute can use
about_functions_advanced_param... HelpFile  Explains how to add static and dynamic parameters to functions that declare
about_functions_cmdletbindinga... HelpFile  Describes an attribute that declares a function that acts similar to a
about_hash_tables                 HelpFile  Describes how to create, use, and sort hash tables in Windows PowerShell.
about_History                     HelpFile  Describes how to retrieve and run commands in the command history.
about_If                          HelpFile  Describes a language command you can use to run statement lists based
about_jobs                        HelpFile  Provides information about how Windows PowerShell background jobs run a
about_job_details                 HelpFile  Provides details about background jobs on local and remote computers.
about_join                        HelpFile  Describes how the join operator (-join) combines multiple strings into a
about_Language_Keywords           HelpFile  Describes the keywords in the Windows PowerShell scripting language.
about_Line_Editing                HelpFile  Describes how to edit commands at the Windows PowerShell command prompt.
about_locations                   HelpFile  Describes how to access items from the working location in Windows
about_logical_operators           HelpFile  Describes the operators that connect statements in Windows PowerShell.
about_methods                     HelpFile  Describes how to use methods to perform actions on objects in Windows
about_modules                     HelpFile  Explains how to install, import, and use Windows PowerShell modules.
about_objects                     HelpFile  Provides essential information about objects in Windows PowerShell.
about_operators                   HelpFile  Describes the operators that are supported by Windows PowerShell.
about_parameters                  HelpFile  Describes how to work with cmdlet parameters in Windows PowerShell.
about_Parsing                     HelpFile  Describes how Windows PowerShell parses commands.
about_Path_Syntax                 HelpFile  Describes the full and relative path name formats in Windows PowerShell.
about_pipelines                   HelpFile  Combining commands into pipelines in the Windows PowerShell
about_preference_variables        HelpFile  Variables that customize the behavior of Windows PowerShell
about_profiles                    HelpFile  Describes how to create and use a Windows PowerShell profile.
about_prompts                     HelpFile  Describes the Prompt function and demonstrates how to create a custom
about_properties                  HelpFile  Describes how to use object properties in Windows PowerShell.
about_providers                   HelpFile  Describes how Windows PowerShell providers provide access to data and
about_pssessions                  HelpFile  Describes Windows PowerShell sessions (PSSessions) and explains how to
about_pssession_details           HelpFile  Provides detailed information about Windows PowerShell sessions and the
about_PSSnapins                   HelpFile  Describes Windows PowerShell snap-ins and shows how to use and manage them.
about_Quoting_Rules               HelpFile  Describes rules for using single and double quotation marks
about_Redirection                 HelpFile  Describes how to redirect output from Windows PowerShell to text files.
about_Ref                         HelpFile  Describes how to create and use a reference variable type.
about_regular_expressions         HelpFile  Describes regular expressions in Windows PowerShell.
about_remote                      HelpFile  Describes how to run remote commands in Windows PowerShell.
about_remote_FAQ                  HelpFile  Contains questions and answers about running remote commands
about_remote_jobs                 HelpFile  Describes how to run background jobs on remote computers.
about_remote_output               HelpFile  Describes how to interpret and format the output of remote commands.
about_remote_requirements         HelpFile  Describes the system requirements and configuration requirements for
about_remote_troubleshooting      HelpFile  Describes how to troubleshoot remote operations in Windows PowerShell.
about_requires                    HelpFile  Prevents a script from running by requiring the specified snap-ins and
about_Reserved_Words              HelpFile  Lists the reserved words that cannot be used as identifiers because they
about_Return                      HelpFile  Exits the current scope, which can be a function, script, or script block.
about_scopes                      HelpFile  Explains the concept of scope in Windows PowerShell and shows how to set
about_scripts                     HelpFile  Describes how to write and run scripts in Windows PowerShell.
about_script_blocks               HelpFile  Defines what a script block is and explains how to use script blocks in
about_script_internationalization HelpFile  Describes the script internationalization features of Windows PowerShell...
about_Session_Configurations      HelpFile  Describes session configurations, which determine the users who can
about_Signing                     HelpFile  Explains to how sign scripts so that they comply with the Windows
about_Special_Characters          HelpFile  Describes the special characters that you can use to control how
about_split                       HelpFile  Explains how to use the split operator to split one or more strings into
about_Switch                      HelpFile  Explains how to use a switch to handle multiple If statements.
about_Throw                       HelpFile  Describes the Throw keyword, which generates a terminating error.
about_transactions                HelpFile  Describes how to manage transacted operations in Windows PowerShell.
about_trap                        HelpFile  Describes a keyword that handles a terminating error.
about_try_catch_finally           HelpFile  Describes how to use the Try, Catch, and Finally blocks to handle
about_types.ps1xml                HelpFile  Explains how the Types.ps1xml files let you extend the Microsoft .NET
about_type_operators              HelpFile  Describes the operators that work with Microsoft .NET Framework types.
about_Variables                   HelpFile  Describes how variables store values that can be used in Windows
about_While                       HelpFile  Describes a language statement that you can use to run a command block
about_wildcards                   HelpFile  Describes how to use wildcard characters in Windows PowerShell.
about_Windows_PowerShell_2.0      HelpFile  Describes the new features that are included in Windows PowerShell 2.0.
about_Windows_PowerShell_ISE      HelpFile  Describes the features and system requirements of Windows PowerShell
about_WMI_Cmdlets                 HelpFile  Provides background information about Windows Management Instrumentation
about_WS-Management_Cmdlets       HelpFile  Provides an overview of Web Services for Management (WS-Management) as
default                           HelpFile  Displays help about Windows PowerShell cmdlets and concepts.


PS C:\>
```

- Get all ```powershell``` help topics for ```process```

```Powershell
PS C:\> Get-Help *process

Name                              Category  Synopsis
----                              --------  --------
Get-Process                       Cmdlet    Gets the processes that are running on the local computer or a remote co...
Stop-Process                      Cmdlet    Stops one or more running processes.
Wait-Process                      Cmdlet    Waits for the processes to be stopped before accepting more input.
Debug-Process                     Cmdlet    Debugs one or more processes running on the local computer.
Start-Process                     Cmdlet    Starts one or more processes on the local computer.


PS C:\>
```

- ```Get-Process``` Cmdlet

```Powershell
PS C:\> Get-Process

Handles  NPM(K)    PM(K)      WS(K) VM(M)   CPU(s)     Id ProcessName
-------  ------    -----      ----- -----   ------     -- -----------
    109       5    14812       9284    43             996 audiodg
     52       3     1600       4688    46     0.44   2588 conhost
    452       5     1092       2584    33             344 csrss
    178       6     1080       3124    31             400 csrss
     68       4      964       3080    39     0.03    300 dwm
    695      21    23220      25500   166     1.38    356 explorer
      0       0        0         12     0               0 Idle
     41       3     1672       2980    53     0.00    332 jusched
    756      13     2860       7264    35             492 lsass
    144       4     1048       2540    14             500 lsm
     75       4     1312       3752    31            3528 mscorsvw
    413      10    81340      81328   218     1.83   2580 powershell
    576      13    11580       5804    80            1180 SearchIndexer
    217       7     4004       5388    35             484 services
     29       1      212        628     4             268 smss
    285      10     4468       6516    58            1332 spoolsv
    140       4     1768       3728    28            1516 sppsvc
    353       7     2460       5292    34             608 svchost
    276       8     1996       4380    26             720 svchost
    561      13    14644      12140    77             772 svchost
    529      13    22324      29264   100             892 svchost
   1239      35    20608      23608   127             932 svchost
    498      17     5776       9092    50            1100 svchost
    378      13     7728       8008    55            1228 svchost
    318      25     8292       8060    47            1368 svchost
    344      15     4952       8300    67            1460 svchost
     96       7     1068       3392    25            1820 svchost
     71       4      964       3560    22            2056 svchost
    349      37     7504       8204    63            2364 svchost
    400      34   143888      48300   208            3556 svchost
    592       0       44       1416     3               4 System
    146       8     2120       4372    40     0.03   2028 taskhost
    327      10     8012      14516    82            3944 TrustedInstaller
    115       5     1444       3524    45             668 VBoxService
    139       6     1328       4308    62     0.04   1612 VBoxTray
    123       5     1416       4744    28            2348 VSSVC
     74       5      808       2904    32             392 wininit
    111       4     1524       3668    39             440 winlogon
    113       4     1712       3952    26            2524 WmiPrvSE
    172       6     3152       6856    37            3820 WmiPrvSE
    428      15     7364      14860   108            2088 wmpnetwk
     98       5     1356       4680    45            4048 WuSetupV


PS C:\>
```

- Get all ```powershell``` help topics for ```alias```

```Powershell
PS C:\> Get-Help *alias*

Name                              Category  Synopsis
----                              --------  --------
Export-Alias                      Cmdlet    Exports information about currently defined aliases to a file.
Get-Alias                         Cmdlet    Gets the aliases for the current session.
Import-Alias                      Cmdlet    Imports an alias list from a file.
New-Alias                         Cmdlet    Creates a new alias.
Set-Alias                         Cmdlet    Creates or changes an alias (alternate name) for a cmdlet or other comma...
Alias                             Provider  Provides access to the Windows PowerShell aliases and the values that th...
about_aliases                     HelpFile  Describes how to use alternate names for cmdlets and commands in Windows


PS C:\>
```

- ```Get-Alias``` Cmdlet

```Powershell
PS C:\> Get-Alias

CommandType     Name                                                Definition
-----------     ----                                                ----------
Alias           %                                                   ForEach-Object
Alias           ?                                                   Where-Object
Alias           ac                                                  Add-Content
Alias           asnp                                                Add-PSSnapIn
Alias           cat                                                 Get-Content
Alias           cd                                                  Set-Location
Alias           chdir                                               Set-Location
Alias           clc                                                 Clear-Content
Alias           clear                                               Clear-Host
Alias           clhy                                                Clear-History
Alias           cli                                                 Clear-Item
Alias           clp                                                 Clear-ItemProperty
Alias           cls                                                 Clear-Host
Alias           clv                                                 Clear-Variable
Alias           compare                                             Compare-Object
Alias           copy                                                Copy-Item
Alias           cp                                                  Copy-Item
Alias           cpi                                                 Copy-Item
Alias           cpp                                                 Copy-ItemProperty
Alias           cvpa                                                Convert-Path
Alias           dbp                                                 Disable-PSBreakpoint
Alias           del                                                 Remove-Item
Alias           diff                                                Compare-Object
Alias           dir                                                 Get-ChildItem
Alias           ebp                                                 Enable-PSBreakpoint
Alias           echo                                                Write-Output
Alias           epal                                                Export-Alias
Alias           epcsv                                               Export-Csv
Alias           epsn                                                Export-PSSession
Alias           erase                                               Remove-Item
Alias           etsn                                                Enter-PSSession
Alias           exsn                                                Exit-PSSession
Alias           fc                                                  Format-Custom
Alias           fl                                                  Format-List
Alias           foreach                                             ForEach-Object
Alias           ft                                                  Format-Table
Alias           fw                                                  Format-Wide
Alias           gal                                                 Get-Alias
Alias           gbp                                                 Get-PSBreakpoint
Alias           gc                                                  Get-Content
Alias           gci                                                 Get-ChildItem
Alias           gcm                                                 Get-Command
Alias           gcs                                                 Get-PSCallStack
Alias           gdr                                                 Get-PSDrive
Alias           ghy                                                 Get-History
Alias           gi                                                  Get-Item
Alias           gjb                                                 Get-Job
Alias           gl                                                  Get-Location
Alias           gm                                                  Get-Member
Alias           gmo                                                 Get-Module
Alias           gp                                                  Get-ItemProperty
Alias           gps                                                 Get-Process
Alias           group                                               Group-Object
Alias           gsn                                                 Get-PSSession
Alias           gsnp                                                Get-PSSnapIn
Alias           gsv                                                 Get-Service
Alias           gu                                                  Get-Unique
Alias           gv                                                  Get-Variable
Alias           gwmi                                                Get-WmiObject
Alias           h                                                   Get-History
Alias           history                                             Get-History
Alias           icm                                                 Invoke-Command
Alias           iex                                                 Invoke-Expression
Alias           ihy                                                 Invoke-History
Alias           ii                                                  Invoke-Item
Alias           ipal                                                Import-Alias
Alias           ipcsv                                               Import-Csv
Alias           ipmo                                                Import-Module
Alias           ipsn                                                Import-PSSession
Alias           ise                                                 powershell_ise.exe
Alias           iwmi                                                Invoke-WMIMethod
Alias           kill                                                Stop-Process
Alias           lp                                                  Out-Printer
Alias           ls                                                  Get-ChildItem
Alias           man                                                 help
Alias           md                                                  mkdir
Alias           measure                                             Measure-Object
Alias           mi                                                  Move-Item
Alias           mount                                               New-PSDrive
Alias           move                                                Move-Item
Alias           mp                                                  Move-ItemProperty
Alias           mv                                                  Move-Item
Alias           nal                                                 New-Alias
Alias           ndr                                                 New-PSDrive
Alias           ni                                                  New-Item
Alias           nmo                                                 New-Module
Alias           nsn                                                 New-PSSession
Alias           nv                                                  New-Variable
Alias           ogv                                                 Out-GridView
Alias           oh                                                  Out-Host
Alias           popd                                                Pop-Location
Alias           ps                                                  Get-Process
Alias           pushd                                               Push-Location
Alias           pwd                                                 Get-Location
Alias           r                                                   Invoke-History
Alias           rbp                                                 Remove-PSBreakpoint
Alias           rcjb                                                Receive-Job
Alias           rd                                                  Remove-Item
Alias           rdr                                                 Remove-PSDrive
Alias           ren                                                 Rename-Item
Alias           ri                                                  Remove-Item
Alias           rjb                                                 Remove-Job
Alias           rm                                                  Remove-Item
Alias           rmdir                                               Remove-Item
Alias           rmo                                                 Remove-Module
Alias           rni                                                 Rename-Item
Alias           rnp                                                 Rename-ItemProperty
Alias           rp                                                  Remove-ItemProperty
Alias           rsn                                                 Remove-PSSession
Alias           rsnp                                                Remove-PSSnapin
Alias           rv                                                  Remove-Variable
Alias           rvpa                                                Resolve-Path
Alias           rwmi                                                Remove-WMIObject
Alias           sajb                                                Start-Job
Alias           sal                                                 Set-Alias
Alias           saps                                                Start-Process
Alias           sasv                                                Start-Service
Alias           sbp                                                 Set-PSBreakpoint
Alias           sc                                                  Set-Content
Alias           select                                              Select-Object
Alias           set                                                 Set-Variable
Alias           si                                                  Set-Item
Alias           sl                                                  Set-Location
Alias           sleep                                               Start-Sleep
Alias           sort                                                Sort-Object
Alias           sp                                                  Set-ItemProperty
Alias           spjb                                                Stop-Job
Alias           spps                                                Stop-Process
Alias           spsv                                                Stop-Service
Alias           start                                               Start-Process
Alias           sv                                                  Set-Variable
Alias           swmi                                                Set-WMIInstance
Alias           tee                                                 Tee-Object
Alias           type                                                Get-Content
Alias           where                                               Where-Object
Alias           wjb                                                 Wait-Job
Alias           write                                               Write-Output


PS C:\>
```

- Examples of ```Get-Help```

```Powershell
PS C:\> Get-Help Get-Help -Examples

NAME
    Get-Help

SYNOPSIS
    Displays information about Windows PowerShell commands and concepts.

    -------------------------- EXAMPLE 1 --------------------------

    C:\PS>get-help


    Description
    -----------
    This command displays help about the Windows PowerShell help system.




    -------------------------- EXAMPLE 2 --------------------------

    C:\PS>get-help *


    Description
    -----------
    This command displays a list of all help files in the Windows PowerShell help system.




    -------------------------- EXAMPLE 3 --------------------------

    C:\PS>get-help get-alias

    C:\PS>help get-alias

    C:\PS>get-alias -?


    Description
    -----------
    These commands display basic information about the get-alias cmdlet. The "Get-Help" and "-?" commands display the i
    nformation on a single page. The "Help" command displays the information one page at a time.




    -------------------------- EXAMPLE 4 --------------------------

    C:\PS>get-help about_*


    Description
    -----------
    This command displays a list of the conceptual topics included in Windows PowerShell help. All of these topics begi
    n with the characters "about_". To display a particular help file, type "get-help <topic-name>, for example, "get-h
    elp about_signing".




    -------------------------- EXAMPLE 5 --------------------------

    C:\PS>get-help ls -detailed


    Description
    -----------
    This command displays detailed help for the Get-ChildItem cmdlet by specifying one of its aliases, "ls." The Detail
    ed parameter requests the detailed view of the help file, which includes parameter descriptions and examples. To se
    e the complete help file for a cmdlet, use the Full parameter.




    -------------------------- EXAMPLE 6 --------------------------

    C:\PS>get-help format-string -full


    Description
    -----------
    This command displays the full view help for the Format-String cmdlet. The full view of help includes parameter des
    criptions, examples, and a table of technical details about the parameters.




    -------------------------- EXAMPLE 7 --------------------------

    C:\PS>get-help start-service -examples


    Description
    -----------
    This command displays examples of using start-service in Windows PowerShell commands.




    -------------------------- EXAMPLE 8 --------------------------

    C:\PS>get-help get-childitem -parameter f*


    Description
    -----------
    This command displays descriptions of the parameters of the Get-ChildItem cmdlet that begin with "f" (filter and fo
    rce). For descriptions of all parameters, type "get-help get-childitem parameter*".




    -------------------------- EXAMPLE 9 --------------------------

    C:\PS>(get-help write-output).syntax


    Description
    -----------
    This command displays only the syntax of the Write-Output cmdlet.

    Syntax is one of many properties of help objects; others are description, details, examples, and parameters. To fin
    d all properties and methods of help objects, type "get-help <cmdlet-name> | get-member"; for example, "get-help st
    art-service | get member".




    -------------------------- EXAMPLE 10 --------------------------

    C:\PS>(get-help trace-command).alertset


    Description
    -----------
    This command displays the notes about the cmdlet. The notes are stored in the alertSet property of the help object.

    The notes include conceptual information and tips for using the cmdlet. By default, the notes are displayed only wh
    en you use the Full parameter of Get-Help, but you can also display them by using the alertSet property.




    -------------------------- EXAMPLE 11 --------------------------

    C:\PS>get-help add-member -full | out-string -stream | select-string -pattern clixml


    Description
    -----------
    This example shows how to search for a word in particular cmdlet help topic. This command searches for the word "cl
    ixml" in the full version of the help topic for the Add-Member cmdlet.

    Because the Get-Help cmdlet generates a MamlCommandHelpInfo object, not a string, you need to use a command that tr
    ansforms the help topic content into a string, such as Out-String or Out-File.




    -------------------------- EXAMPLE 12 --------------------------

    C:\PS>get-help get-member -online


    Description
    -----------
    This command displays the online version of the help topic for the Get-Member cmdlet.




    -------------------------- EXAMPLE 13 --------------------------

    C:\PS>get-help remoting


    Description
    -----------
    This command displays a list of topics that include the word "remoting" in their contents.

    When you enter a word that does not appear in any topic title, Get-Help displays a list of topics that include that
     word.




    -------------------------- EXAMPLE 14 --------------------------

    C:\PS>get-help get-item -path SQLSERVER:\DataCollection

    NAME
        Get-Item

    SYNOPSIS
        Gets a collection of Server objects for the local computer and any computers to which you have made a SQL Serve
    r PowerShell connection.
    ...

    C:\PS> cd SQLSERVER:\DataCollection
    C:\PS> SQLSERVER:\DataCollection> get-help get-item


    NAME
        Get-Item

    SYNOPSIS
        Gets a collection of Server objects for the local computer and any computers to which you have made a SQL Serve
    r PowerShell connection.
    ...


    C:\PS> Get-Item

    NAME
        Get-Item

    SYNOPSIS
        Gets the item at the specified location.

    ...


    Description
    -----------
    This example shows how to get help for the Get-Item cmdlet that explains how to use the cmdlet in the DataCollectio
    n node of the Windows PowerShell SQL Server provider.

    The example shows two ways of getting the custom help for Get-Item.

    The first command uses the Path parameter of Get-Help to specify the provider path. This command can be entered at
    any path location.

    The second command uses the Set-Location cmdlet (alias = "cd") to go to the provider path. From that location, even
     without the Path parameter, the Get-Help command gets the custom help for the provider path.

    The third command shows that a Get-Help command in a file system path, and without the Path parameter, gets the sta
    ndard help for the Get-Item cmdlet.




    -------------------------- EXAMPLE 15 --------------------------

    C:\PS>get-help c:\ps-test\MyScript.ps1


    Description
    -----------
    This command gets help for the MyScript.ps1 script. For information about writing help for your functions and scrip
    ts, see about_Comment_Based_Help.

PS C:\>
```

- Get all ```powershell``` help topics for ```alias```

```Powershell
PS C:\> Get-Help *alias*

Name                              Category  Synopsis
----                              --------  --------
Export-Alias                      Cmdlet    Exports information about currently defined aliases to a file.
Get-Alias                         Cmdlet    Gets the aliases for the current session.
Import-Alias                      Cmdlet    Imports an alias list from a file.
New-Alias                         Cmdlet    Creates a new alias.
Set-Alias                         Cmdlet    Creates or changes an alias (alternate name) for a cmdlet or other comma...
Alias                             Provider  Provides access to the Windows PowerShell aliases and the values that th...
about_aliases                     HelpFile  Describes how to use alternate names for cmdlets and commands in Windows


PS C:\>
```

- Getting help for ```about_aliases```

```Powershell
PS C:\> Get-Help about_aliases
TOPIC
    about_aliases

SHORT DESCRIPTION
    Describes how to use alternate names for cmdlets and commands in Windows
    PowerShell.

LONG DESCRIPTION
    An alias is an alternate name or nickname for a cmdlet or for a command
    element, such as a function, script, file, or executable file. You
    can use the alias instead of the command name in any Windows PowerShell
    commands.

    To create an alias, use the New-Alias cmdlet. For example, the following
    command creates the "gas" alias for the Get-AuthenticodeSignature cmdlet:

        new-alias -name gas -value Get-AuthenticodeSignature

    After you create the alias for the cmdlet name, you can use the alias
    instead of the cmdlet name. For example, to get the Authenticode signature
    for the SqlScript.ps1 file, type:

        get-authenticodesignature sqlscript.ps1

    Or, type:

        gas sqlscript.ps1


    If you create "word" as the alias for Microsoft Office Word, you can type
    "word" instead of the following:


        "c:\program files\microsoft office\office11\winword.exe"

BUILT-IN ALIASES
    Windows PowerShell includes a set of built-in aliases, including "cd" and
    "chdir" for the Set-Location cmdlet, and "ls" and "dir" for the
    Get-ChildItem cmdlet.

    To get all the aliases on the computer, including the built-in aliases,
    type:

        get-alias

ALIAS CMDLETS
    Windows PowerShell includes the following cmdlets, which are designed for
    working with aliases:

        - Get-Alias. Gets all the aliases in the current session.
        - New-Alias. Creates a new alias.
        - Set-Alias. Creates or changes an alias.
        - Export-Alias. Exports one or more aliases to a file.
        - Import-Alias. Imports an alias file into Windows PowerShell.

    For detailed information about the cmdlets, type:

        get-help <cmdlet-name> -detailed

    For example, type:

        get-help export-alias -detailed

CREATING AN ALIAS
    To create a new alias, use the New-Alias cmdlet. For example, to create the
    "gh" alias for Get-Help, type:

        new-alias -name gh -value get-help

    You can use the alias in commands, just as you would use the full cmdlet
    name, and you can use the alias with parameters.

    For example, to get detailed Help for the Get-WmiObject cmdlet, type:

        get-help get-wmiobject -detailed

    Or, type:

        gh get-wmiobject -detailed

SAVING ALIASES
    The aliases that you create are saved only in the current session. To use
    the aliases in a different session, add the alias to your Windows
    PowerShell profile. Or, use the Export-Alias cmdlet to save the aliases to
    a file.

    For more information, type:

        get-help about_profile

GETTING ALIASES
    To get all the aliases in the current session, including the built-in
    aliases, the aliases in your Windows PowerShell profiles, and the aliases
    that you have created in the current session, type:

        get-alias

    To get particular aliases, use the Name parameter of the Get-Alias cmdlet.
    For example, to get aliases that begin with "p", type:

        get-alias -name p*

    To get the aliases for a particular item, use the Definition parameter.
    For example, to get the aliases for the Get-ChildItem cmdlet type:

        get-alias -definition Get-ChildItem


ALTERNATE NAMES FOR COMMANDS WITH PARAMETERS
    You can assign an alias to a cmdlet, script, function, or executable file.
    However, you cannot assign an alias to a command and its parameters.
    For example, you can assign an alias to the Get-EventLog cmdlet, but you
    cannot assign an alias to the "get-eventlog -logname system" command.

    However, you can create a function that includes the command. To create a
    function, type the word "function" followed by a name for the function.
    Type the command, and enclose it in braces ({}).

    For example, the following command creates the syslog function. This
    function represents the "get-eventlog -logname system" command:

        function syslog {get-eventlog -logname system}

    You can now type "syslog" instead of the command. And, you can create
    aliases for the syslog function.

    For more information about functions, type:

        get-help about_functions

ALIAS OBJECTS
     Windows PowerShell aliases are represented by objects that are instances
     of the System.Management.Automation.AliasInfo class. For more information
     about this type of object, see "AliasInfo Class" in the Microsoft
     Developer Network (MSDN) library at
     http://go.microsoft.com/fwlink/?LinkId=143644.

     To view the properties and methods of the alias objects, get the
     aliases. Then, pipe them to the Get-Member cmdlet. For example:

        get-alias | get-member

     To view the values of the properties of a specific alias, such as the
     "dir" alias, get the alias. Then, pipe it to the Format-List cmdlet. For
     example, the following command gets the "dir" alias. Next, the command
     pipes the alias to the Format-List cmdlet. Then, the command uses the
     Property parameter of Format-List with a wildcard character (*) to display
     all the properties of the "dir" alias. The following command performs
     these tasks:

        get-alias -name dir | format-list -property *

WINDOWS POWERSHELL ALIAS PROVIDER
    Windows PowerShell includes the Alias provider. The Alias provider lets you
    view the aliases in Windows PowerShell as though they were on a file system
    drive.

    The Alias provider exposes the Alias: drive. To go into the Alias: drive,
    type:

        set-location alias:

    To view the contents of the drive, type:

        get-childitem

    To view the contents of the drive from another Windows PowerShell drive,
    begin the path with the drive name. Include the colon (:). For example:

        get-childitem -path alias:

    To get information about a particular alias, type the drive name and
    the alias name. Or, type a name pattern. For example, to get all the
    aliases that begin with "p", type:

        get-childitem -path alias:p*

    For more information about the Windows PowerShell Alias provider,
    type:

        get-help alias-psprovider


SEE ALSO

    new-alias
    get-alias
    set-alias
    export-alias
    import-alias
    get-psprovider
    get-psdrive
    about_functions
    about_profiles
    about_providers

PS C:\>
```

###### Exercise

- Use ```Get-Help``` to retrieve help about ```Get-Command```.

```Powershell
PS C:\Users\Windows-32> Get-Help Get-Command

NAME
    Get-Command

SYNOPSIS
    Gets basic information about cmdlets and other elements of Windows PowerShell commands.


SYNTAX
    Get-Command [[-Name] <string[]>] [-CommandType {Alias | Function | Filter | Cmdlet | ExternalScript | Application |
     Script | All}] [[-ArgumentList] <Object[]>] [-Module <string[]>] [-Syntax] [-TotalCount <int>] [<CommonParameters>
    ]

    Get-Command [-Noun <string[]>] [-Verb <string[]>] [[-ArgumentList] <Object[]>] [-Module <string[]>] [-Syntax] [-Tot
    alCount <int>] [<CommonParameters>]


DESCRIPTION
    The Get-Command cmdlet gets basic information about cmdlets and other elements of Windows PowerShell commands in th
    e session, such as aliases, functions, filters, scripts, and applications.

    Get-Command gets its data directly from the code of a cmdlet, function, script, or alias, unlike Get-Help, which ge
    ts its information from help topic files.

    Without parameters, "Get-Command" gets all of the cmdlets and functions in the current session. "Get-Command *" get
    s all Windows PowerShell elements and all of the non-Windows-PowerShell files in the Path environment variable ($en
    v:path). It groups the files in the "Application" command type.

    You can use the Module parameter of Get-Command to find the commands that were added to the session by adding a Win
    dows PowerShell snap-in or importing a module.


RELATED LINKS
    Online version: http://go.microsoft.com/fwlink/?LinkID=113309
    about_Command_Precedence
    Get-Help
    Get-PSDrive
    Get-Member
    Import-PSSession
    Export-PSSession

REMARKS
    To see the examples, type: "get-help Get-Command -examples".
    For more information, type: "get-help Get-Command -detailed".
    For technical information, type: "get-help Get-Command -full".



PS C:\Users\Windows-32>
```

- Use Get-Help ```about_<topic>``` to retrieve help about ```powershell.exe```.

```Powershell
PS C:\Users\Windows-32> Get-Help about*

Name                              Category  Synopsis
----                              --------  --------
about_aliases                     HelpFile  Describes how to use alternate names for cmdlets and commands in Windows
about_Arithmetic_Operators        HelpFile  Describes the operators that perform arithmetic in Windows PowerShell.
about_arrays                      HelpFile  Describes a compact data structure for storing data elements.
about_Assignment_Operators        HelpFile  Describes how to use operators to assign values to variables.
about_Automatic_Variables         HelpFile  Describes variables that store state information for Windows PowerShell.
about_Break                       HelpFile  Describes a statement you can use to immediately exit Foreach, For, While,
about_command_precedence          HelpFile  Describes how Windows PowerShell determines which command to run.
about_Command_Syntax              HelpFile  Describes the notation used for Windows PowerShell syntax in Help.
about_Comment_Based_Help          HelpFile  Describes how to write comment-based Help topics for functions and scripts.
about_CommonParameters            HelpFile  Describes the parameters that can be used with any cmdlet.
about_Comparison_Operators        HelpFile  Describes the operators that compare values in Windows PowerShell.
about_Continue                    HelpFile  Describes how the Continue statement immediately returns the program flow
about_Core_Commands               HelpFile  Lists the cmdlets that are designed for use with Windows PowerShell
about_data_sections               HelpFile  Explains Data sections, which isolate text strings and other read-only
about_debuggers                   HelpFile  Describes the Windows PowerShell debugger.
about_do                          HelpFile  Runs a statement list one or more times, subject to a While or Until
about_environment_variables       HelpFile  Describes how to access Windows environment variables in Windows
about_escape_characters           HelpFile  Introduces the escape character in Windows PowerShell and explains
about_eventlogs                   HelpFile  Windows PowerShell creates a Windows event log that is
about_execution_policies          HelpFile  Describes the Windows PowerShell execution policies and explains
about_For                         HelpFile  Describes a language command you can use to run statements based on a
about_Foreach                     HelpFile  Describes a language command you can use to traverse all the items in a
about_format.ps1xml               HelpFile  The Format.ps1xml files in Windows PowerShell define the default display
about_functions                   HelpFile  Describes how to create and use functions in Windows PowerShell.
about_functions_advanced          HelpFile  Introduces advanced functions that act similar to cmdlets.
about_functions_advanced_methods  HelpFile  Describes how functions that specify the CmdletBinding attribute can use
about_functions_advanced_param... HelpFile  Explains how to add static and dynamic parameters to functions that declare
about_functions_cmdletbindinga... HelpFile  Describes an attribute that declares a function that acts similar to a
about_hash_tables                 HelpFile  Describes how to create, use, and sort hash tables in Windows PowerShell.
about_History                     HelpFile  Describes how to retrieve and run commands in the command history.
about_If                          HelpFile  Describes a language command you can use to run statement lists based
about_jobs                        HelpFile  Provides information about how Windows PowerShell background jobs run a
about_job_details                 HelpFile  Provides details about background jobs on local and remote computers.
about_join                        HelpFile  Describes how the join operator (-join) combines multiple strings into a
about_Language_Keywords           HelpFile  Describes the keywords in the Windows PowerShell scripting language.
about_Line_Editing                HelpFile  Describes how to edit commands at the Windows PowerShell command prompt.
about_locations                   HelpFile  Describes how to access items from the working location in Windows
about_logical_operators           HelpFile  Describes the operators that connect statements in Windows PowerShell.
about_methods                     HelpFile  Describes how to use methods to perform actions on objects in Windows
about_modules                     HelpFile  Explains how to install, import, and use Windows PowerShell modules.
about_objects                     HelpFile  Provides essential information about objects in Windows PowerShell.
about_operators                   HelpFile  Describes the operators that are supported by Windows PowerShell.
about_parameters                  HelpFile  Describes how to work with cmdlet parameters in Windows PowerShell.
about_Parsing                     HelpFile  Describes how Windows PowerShell parses commands.
about_Path_Syntax                 HelpFile  Describes the full and relative path name formats in Windows PowerShell.
about_pipelines                   HelpFile  Combining commands into pipelines in the Windows PowerShell
about_preference_variables        HelpFile  Variables that customize the behavior of Windows PowerShell
about_profiles                    HelpFile  Describes how to create and use a Windows PowerShell profile.
about_prompts                     HelpFile  Describes the Prompt function and demonstrates how to create a custom
about_properties                  HelpFile  Describes how to use object properties in Windows PowerShell.
about_providers                   HelpFile  Describes how Windows PowerShell providers provide access to data and
about_pssessions                  HelpFile  Describes Windows PowerShell sessions (PSSessions) and explains how to
about_pssession_details           HelpFile  Provides detailed information about Windows PowerShell sessions and the
about_PSSnapins                   HelpFile  Describes Windows PowerShell snap-ins and shows how to use and manage them.
about_Quoting_Rules               HelpFile  Describes rules for using single and double quotation marks
about_Redirection                 HelpFile  Describes how to redirect output from Windows PowerShell to text files.
about_Ref                         HelpFile  Describes how to create and use a reference variable type.
about_regular_expressions         HelpFile  Describes regular expressions in Windows PowerShell.
about_remote                      HelpFile  Describes how to run remote commands in Windows PowerShell.
about_remote_FAQ                  HelpFile  Contains questions and answers about running remote commands
about_remote_jobs                 HelpFile  Describes how to run background jobs on remote computers.
about_remote_output               HelpFile  Describes how to interpret and format the output of remote commands.
about_remote_requirements         HelpFile  Describes the system requirements and configuration requirements for
about_remote_troubleshooting      HelpFile  Describes how to troubleshoot remote operations in Windows PowerShell.
about_requires                    HelpFile  Prevents a script from running by requiring the specified snap-ins and
about_Reserved_Words              HelpFile  Lists the reserved words that cannot be used as identifiers because they
about_Return                      HelpFile  Exits the current scope, which can be a function, script, or script block.
about_scopes                      HelpFile  Explains the concept of scope in Windows PowerShell and shows how to set
about_scripts                     HelpFile  Describes how to write and run scripts in Windows PowerShell.
about_script_blocks               HelpFile  Defines what a script block is and explains how to use script blocks in
about_script_internationalization HelpFile  Describes the script internationalization features of Windows PowerShell...
about_Session_Configurations      HelpFile  Describes session configurations, which determine the users who can
about_Signing                     HelpFile  Explains to how sign scripts so that they comply with the Windows
about_Special_Characters          HelpFile  Describes the special characters that you can use to control how
about_split                       HelpFile  Explains how to use the split operator to split one or more strings into
about_Switch                      HelpFile  Explains how to use a switch to handle multiple If statements.
about_Throw                       HelpFile  Describes the Throw keyword, which generates a terminating error.
about_transactions                HelpFile  Describes how to manage transacted operations in Windows PowerShell.
about_trap                        HelpFile  Describes a keyword that handles a terminating error.
about_try_catch_finally           HelpFile  Describes how to use the Try, Catch, and Finally blocks to handle
about_types.ps1xml                HelpFile  Explains how the Types.ps1xml files let you extend the Microsoft .NET
about_type_operators              HelpFile  Describes the operators that work with Microsoft .NET Framework types.
about_Variables                   HelpFile  Describes how variables store values that can be used in Windows
about_While                       HelpFile  Describes a language statement that you can use to run a command block
about_wildcards                   HelpFile  Describes how to use wildcard characters in Windows PowerShell.
about_Windows_PowerShell_2.0      HelpFile  Describes the new features that are included in Windows PowerShell 2.0.
about_Windows_PowerShell_ISE      HelpFile  Describes the features and system requirements of Windows PowerShell
about_WMI_Cmdlets                 HelpFile  Provides background information about Windows Management Instrumentation
about_WS-Management_Cmdlets       HelpFile  Provides an overview of Web Services for Management (WS-Management) as


PS C:\Users\Windows-32>
```

```Powershell
PS C:\Users\Windows-32> Get-Help about_Windows_PowerShell_2.0
TOPIC
    about_Windows_PowerShell_2.0

SHORT DESCRIPTION
    Describes the new features that are included in Windows PowerShell 2.0.


LONG DESCRIPTION
    Windows PowerShell 2.0 includes several significant features that
    extend its use, improve its usability, and allow you to control and
    manage Windows-based environments more easily and comprehensively.


    Windows PowerShell 2.0 is backward compatible. Cmdlets, providers,
    snap-ins, scripts, functions, and profiles that were designed for Windows
    PowerShell 1.0 work in Windows PowerShell 2.0 without changes.


NEW FEATURES
    Windows PowerShell 2.0 includes the following new features.


  Remoting

      Windows PowerShell 2.0 lets you run commands on one or many remote
      computers with a single Windows PowerShell command. You can run
      individual commands, or you can create a persistent connection
      (a session) to run a series of related commands. You can also start a
      session with a remote computer so that the commands you type run
      directly on the remote computer.


      The remoting features of Windows PowerShell are built on Windows
      Remote Management (WinRM). WinRM is the Microsoft implementation of
      the WS-Management protocol, a standard SOAP-based, firewall-compatible
      communications protocol.


      The remote computers must have Windows PowerShell 2.0, the Microsoft .NET
      Framework 2.0, and the WinRM service. Remote commands are supported
      on all operating systems that can run Windows PowerShell. The
      current user must have permission to run commands on the remote
      computers. For more information, see about_Remote_Requirements.


      To support remoting, the Invoke-Command, Enter-PSSession, and
      Exit-PSSession cmdlets have been added, along with other cmdlets
      that contain the PSSession noun. These cmdlets let you create and manage
      persistent connections.


      The ComputerName parameter has also been added to several cmdlets,
      including the Get-Process, Get-Service, and Get-Eventlog cmdlets. This
      parameter allows you to get information about remote computers.
      These cmdlets use .NET Framework methods to get their data,
      so they do not rely on Windows PowerShell remoting. They do not require
      any new programs or configuration. For more information, see the Help for
      each cmdlet.


      For more information about remote commands, see about_Remote and
      about_Remote_FAQ. For more information about sessions, see
      about_PSSessions.


  Windows PowerShell ISE

      Windows PowerShell 2.0 includes Windows PowerShell Integrated
      Scripting Environment (ISE), a host application that lets you run
      commands, and design, write, test, and debug scripts in a graphical,
      color-coded, Unicode-based environment.


      Windows PowerShell ISE requires the Microsoft .NET Framework 3.0 or
      later.


      Windows PowerShell ISE includes:

      -  A Command pane that lets you run interactive commands just as you
         would in the Windows PowerShell console. Just type a command, and then
         press ENTER. The output appears in the Output pane.

      -  A Script pane that lets you compose, edit, debug, and run functions
         and scripts.

      -  Multiple tabs, each with its own Command and Script pane, that let you
         work on one or several tasks independently.


      Windows PowerShell ISE is designed for both novice and advanced users.


  Background Jobs

      Background jobs are commands that run asynchronously. When you run a
      background job, the command prompt returns immediately, even if the
      command is still running. You can use the background job feature to run a
      complex command in the background so that you can use your session for
      other work while the command runs.


      You can run a background job on a local or remote computer and then save
      the results on the local or remote computer. To run a job remotely, use
      the Invoke-Command cmdlet.


      Windows PowerShell includes a set of cmdlets that contain the Job noun
      (the Job cmdlets). Use these cmdlets for creating, starting, managing,
      and deleting background jobs and for getting the results of a background
      job. To get a list of the job cmdlets, type the following command:

          get-command *-job


      For more information about background jobs, see about_Jobs.


  Script Debugger

      Windows PowerShell 2.0 includes a cmdlet-based debugger for scripts and
      functions. The debugger is supported by a fully documented public API
      that you can use to build your own debugger or to customize or extend
      the debugger.


      The debugger cmdlets let you set breakpoints on lines, columns,
      variables, and commands. These cmdlets let you manage the breakpoints
      and display the call stack. You can create conditional breakpoints and
      specify custom actions at a breakpoint, such as running diagnostic and
      logging scripts.


      When you reach a breakpoint, Windows PowerShell suspends execution
      and starts the debugger. The debugger includes a set of custom commands
      that let you step through the code. You can also run standard Windows
      PowerShell commands to display the values of variables, and you can use
      cmdlets to investigate the results.


      For more information about debugging, see about_Debuggers.


  Data Section

      Scripts designed for Windows PowerShell 2.0 can have one or more
      DATA sections that isolate the data from the script logic. The data in
      the new DATA section is restricted to a specified subset of the Windows
      PowerShell scripting language.


      In Windows PowerShell 2.0, the DATA section is used to support
      script internationalization. You can use the DATA section to isolate
      and identify user message strings that will be translated into
      multiple user interface languages.


      For more information, see about_Data_Sections.


  Script Internationalization

      Windows PowerShell 2.0 script internationalization features allow you
      to better serve users throughout the world. Script internationalization
      enables scripts and functions to display messages and Help text to users
      in multiple languages.


      The script internationalization features query the operating system user
      interface culture ($PsUICulture) during execution and then import the
      appropriate translated text strings so you can display them to the user.
      The Data section lets you store text strings separate from code so that
      they are easily identified. A new cmdlet, ConvertFrom-StringData,
      converts text strings into dictionary-like hash tables to facilitate
      translation.


      For more information, see about_Script_Internationalization.



  WMI Cmdlets

      The Windows Management Instrumentation (WMI) functionality of
      Windows PowerShell 2.0 is improved with the addition of the following
      cmdlets:

          - Remove-WmiObject
          - Set-WmiInstance
          - Invoke-WmiMethod


      New parameters have been added to the Get-WmiObject cmdlet. All the WMI
      cmdlets now support the following parameters:

          - EnableAllPrivileges
          - Impersonation
          - Authentication
          - Authority


      These new parameters give you more refined control over the security
      configuration of your WMI operations without requiring you to work
      directly with the types in the .NET Framework Class Library.


      For a list of WMI cmdlets, type the following command:

          get-help *wmi*

      To get help for each cmdlet, type get-help followed by the cmdlet name.


  The Get-WinEvent Cmdlet

      The Get-WinEvent cmdlet gets events from Event Viewer logs and from
      Event Tracing for Windows (ETW) event log files on local and remote
      computers. It can get events from classic event logs and from the
      Windows Event Logs that were introduced in Windows Vista.


      You can use Get-WinEvent to get the objects that represent event logs, event
      log providers, and the events in the logs. Get-WinEvent lets you combine
      events from different sources in a single command. It supports
      advanced queries in XML Path Language (XPath), XML, and hash table
      format.


      Get-WinEvent requires Windows Vista or Windows Server 2008 and the
      Microsoft .NET Framework 3.5.


  The Out-Gridview Cmdlet

      The Out-GridView cmdlet displays the results of other commands in an
      interactive table in which you can search, sort, group, and filter the
      results. For example, you can send the results of a Get-Process,
      Get-WmiObject, Get-WinEvent, or Get-Eventlog command to Out-GridView and
      then use the table features to examine the data.

        help out-gridview -full


  The Add-Type Cmdlet

      The Add-Type cmdlet lets you add .NET Framework types to
      Windows PowerShell from the source code of another .NET Framework
      language.


      Add-Type compiles the source code that creates the types and generates
      assemblies that contain the new .NET Framework types. Then, you can use
      the .NET Framework types in Windows PowerShell commands along with the
      standard object types provided by the .NET Framework.


      You can also use Add-Type to load assemblies into your session so that
      you can use the types in the assemblies in Windows PowerShell.


      Add-Type allows you develop new .NET Framework types, to
      use .NET Framework types in C# libraries, and to access Win32 APIs.


      For more information, see Add-Type.


  Event Notification

      Windows PowerShell 2.0 introduces event notification. Users can register
      and subscribe to events, such as Windows PowerShell events, WMI events,
      or .NET Framework events. And, users can listen, forward, and act on
      management and system events both synchronously and asynchronously.


      Developers can write applications that use the event architecture
      to receive notification about state changes. Users can write
      scripts that subscribe to various events and that react to the content.


      Windows PowerShell provides cmdlets that create new events, get
      events and event subscriptions, register and unregister events,
      wait for events, and delete events. For more information about these
      cmdlets, type the following command:

          get-command *-event


  Modules

      Windows PowerShell modules let you divide and organize your
      Windows PowerShell scripts into independent, self-contained,
      reusable units. Code from a module executes in its own context,
      so it does not add to, conflict with, or overwrite the variables,
      functions, aliases, and other resources in the session.


      You can write, distribute, combine, share, and reuse modules to build
      simple scripts and complex applications.


      Windows PowerShell 2.0 includes cmdlets to add, get, and remove modules
      and to export module members. For more information about the cmdlets
      that are related to modules, type the following command:

          get-command *-module*


  Transactions

      Windows PowerShell 2.0 includes support for transactions. Transactions
      let you undo an entire series of operations. Transactions are available
      only for operations that support transactions. They are designed for
      applications that require atomicity, consistency, isolation, and
      recoverability, like databases and message queuing.


      Cmdlets and providers that support transactions have a new
      UseTransaction parameter. To start an operation within a transaction,
      use the Start-Transaction cmdlet. Then, when you use the cmdlets that
      perform the operation, use the UseTransaction parameter of each cmdlet
      when you want the command to be part of a transaction.


      If any command in the transaction fails at any point, use the
      Rollback-Transaction cmdlet to undo all the commands in the transaction.
      If all the commands succeed, use the Commit-Transaction cmdlet to make
      the command actions permanent.


      Windows PowerShell 2.0 includes cmdlets to start, use, commit, and roll
      back transactions. For information about these cmdlets, type the
      following command:

          get-command *transaction*



 Breaking Changes to Windows PowerShell 1.0

     -- The value of the PowerShellVersion registry entry in
        HKLM\SOFTWARE\Microsoft\PowerShell\1\PowerShellEngine
        is changed to 2.0.

     -- New cmdlets and variables have been added. These additions might
       conflict with variables and functions in profiles and scripts.

     -- The -IEQ operator performs a case insensitive comparison on characters.

     -- The Get-Command cmdlet gets functions by default, in addition to
        cmdlets.

     -- Native commands that generate a user interface cannot be piped to the
        Out-Host cmdlet.

     -- The new Begin, Process, End, and Dynamic Param language keywords might
        conflict with similar words used in scripts and functions. Interpreting
        these words as language keywords might result in parsing errors.

     -- Cmdlet name resolution has changed. In Windows PowerShell 1.0, a
        runtime error was generated when two Windows PowerShell snap-ins
        exported cmdlets with the same name. In Windows PowerShell 2.0, the
        last cmdlet that is added to the session runs when you type the command
        name. To run a command that does not run by default, qualify the cmdlet
        name with the name of the snap-in or module in which it originated.

     -- A function name followed by '-?' gets the help topic for the function,
        if one is included in the function.

    --  Parameter resolution for Microsoft .Net Frameword methods have changed.
        In Windows PowerShell 1.0, if you called an overloaded .NET method
        that has more than one best fit syntax, no error was reported. In
        Windows PowerShell 2.0, an ambiguity error is reported.

        In addition, in Windows PowerShell 2.0, the algorithm for choosing the
        best fit method has been revised significantly to minimize the number
        of ambiguities.

     -- If you are enumerating a collection in the pipeline and you try to
        modify the collection in the pipeline, Windows PowerShell throws an
        exception.

        For example, the following commands would work in Windows
        PowerShell 1.0, but would fail after first pipeline iteration in
        Windows PowerShel 2.0.

            $h = @{Name="Hello"; Value="Test"}
            $h.keys | foreach-object {$h.remove($_)}

        To avoid this error, create a sub-expression for the enumerator
        by using the $() characters. For example:

            $($h.keys) | foreach-object {$h.remove($_)}



    For more information about Windows PowerShell 2.0, visit the following Web
    sites:

    -- Windows PowerShell Web Site
       http://go.microsoft.com/fwlink/?LinkID=106031

    -- Windows PowerShell Team Blog:
       http://go.microsoft.com/fwlink/?LinkId=143696


SEE ALSO
    about_Data_Sections
    about_Debuggers
    about_Functions_Advanced
    about_Jobs
    about_Join
    about_PSSessions
    about_Remote
    about_Script_Internationalization
    about_Split
PS C:\Users\Windows-32>
```

```Powershell
PS C:\Users\Windows-32> Get-Help about_Windows_PowerShell_ISE
TOPIC
    about_Windows_PowerShell_ISE

SHORT DESCRIPTION
    Describes the features and system requirements of Windows PowerShell
    Integrated Scripting Environment (ISE).


LONG DESCRIPTION
    Windows PowerShell ISE is a host application for Windows PowerShell.
    In Windows PowerShell ISE, you can run commands and write, test, and debug
    scripts in a single Windows-based graphical user interface. Its features
    include multiline editing, tab completion, syntax coloring, selective
    execution, context-sensitive Help, and support for right-to-left languages.

    Notes: Because this feature requires a user interface, it does not work on
           Server Core installations of Windows Server.

           Window PowerShell ISE is built on the Windows Presentation
           Foundation (WPF). If the graphical elements of Windows PowerShell
           ISE do not render correctly on your system, you might resolve the
           problem by adding or adjusting the graphics rendering settings on
           your system. This might be required if the computer has an older
           video driver or you are using virtualization software. For more
           information, see "Graphics Rendering Registry Settings" in the MSDN
           library at http://go.microsoft.com/fwlink/?LinkId=144711.

 Running Interactive Commands

    You can run any Windows PowerShell expression or command in Windows
    PowerShell ISE. You can use cmdlets, providers, snap-ins, and modules as
    you would use them in the Windows PowerShell console.


    You can type or paste interactive commands in the Command pane. To run the
    commands, you can use buttons, menu items, and keyboard shortcuts.


    You can use the multiline editing feature to type or paste several lines
    of code into the Command pane at once. When you press the UP ARROW key to
    recall the previous command, all the lines in the command are recalled.
    When you type commands, press SHIFT+ENTER to make a new blank line appear
    under the current line.


 Viewing Output

    The results of commands and scripts are displayed in the Output pane. You
    can move or copy the results from the Output pane by using keyboard
    shortcuts or the Output toolbar, and you can paste the results in other
    programs. You can also clear the Output pane by clicking the Clear Output
    button or by typing one of the following commands:

        clear-host

        cls


 Writing Scripts and Functions

    In the Script pane, you can open, compose, edit, and run scripts. The
    Script pane lets you edit scripts by using buttons and keyboard shortcuts.
    You can also copy, cut, and paste text between the Script pane and the
    Command pane.


    You can use the selective run feature to run all or part of a script. To
    run part of a script, select the text you want to run, and then click the
    Run Script button. Or, press F5.


 Debugging Scripts

    You can use the Windows PowerShell ISE debugger to debug a Windows
    PowerShell script or function. When you debug a script, you can use menu
    items and shortcut keys to perform many of the same tasks that you would
    perform in the Windows PowerShell console. For example, to set a line
    breakpoint in a script, right-click the line of code, and then click
    Toggle Breakpoint.


    You can also use the Windows PowerShell debugger cmdlets in the Command
    pane just as you would use them in the console.


 Tab Completion

    Windows PowerShell ISE has tab completion for cmdlet names, parameter
    names, and Microsoft .NET Framework static types. To use tab completion,
    type the beginning of the name, and then press the TAB key.


 Getting Help

    Windows PowerShell ISE includes a searchable compiled Help file that
    describes Windows PowerShell ISE and Windows PowerShell. This Help file
    includes all the Help that is available from the Get-Help cmdlet. To view
    the Help file in Windows PowerShell ISE, use the Help menu. Or, press F1.


    The Help is context sensitive. For example, if you type Invoke-Item and
    then press F1, the Help file opens to the Help topic for the Invoke-Item
    cmdlet.


    And, you can use the Get-Help cmdlet in Windows PowerShell as you would in
    the Windows PowerShell console.


 Customizing the View

    You can use Windows PowerShell ISE features to move and to resize the
    Command pane, the Output pane, and the Script pane. You can show and hide
    the Script pane, and you can change the text size in all the panes.


    You can also use the $Host variable to change some aspects of the
    appearance of Windows PowerShell ISE, including the window title and the
    foreground and background colors in the Output pane. In addition, Windows
    PowerShell ISE has its own custom host variable, $psgHost. You can use
    this variable to customize Windows PowerShell ISE, including adding menus
    and menu items.


 Windows PowerShell ISE Profile

    Windows PowerShell ISE has its own Windows PowerShell profile,
    Microsoft.PowerShellISE_profile.ps1. In this profile, you can store
    functions, aliases, variables, and commands that you use in Windows
    PowerShell ISE.


    Items in the Windows PowerShell AllHosts profiles (CurrentUser\AllHosts
    and AllUsers\AllHosts) are also available in Windows PowerShell ISE, just
    as they are in any Windows PowerShell host program. However, the items
    in your Windows PowerShell console profiles are not available in Windows
    PowerShell ISE.


    Instructions for moving and reconfiguring your profiles are available in
    Windows PowerShell ISE Help and in about_Profiles.


 System Requirements

    -Operating Systems:
         - Windows 7
         - Windows Server 2008
         - Windows Server 2003 with Service Pack 2
         - Windows Vista with Service Pack 1
         - Windows XP with Service Pack 2

    - Microsoft .NET Framework 3.0

    - Windows PowerShell remoting requires Windows Remote Management 2.0.


 Notes

    - The Get-WinEvent cmdlet requires Windows Vista and later versions of
       Windows and the  Microsoft .NET Framework 3.5.

    - The Export-Counter cmdlet runs only in Windows 7.


 Starting Windows PowerShell ISE

    - To start Windows PowerShell ISE, click Start, point to All Programs,
      point to Windows PowerShell, and then click Windows PowerShell ISE.

    - In the Windows PowerShell console, Cmd.exe, or in the Run box,
      type "powershell_ise.exe".


SEE ALSO
    about_Profiles
    Get-Help

PS C:\Users\Windows-32>
```

- Use ```Get-Help``` with ```wildcards``` to list help about ```“command”```.

```Powershell
PS C:\Users\Windows-32> Get-Help *command*

Name                              Category  Synopsis
----                              --------  --------
Get-Command                       Cmdlet    Gets basic information about cmdlets and other elements of Windows Power...
Invoke-Command                    Cmdlet    Runs commands on local and remote computers.
Measure-Command                   Cmdlet    Measures the time it takes to run script blocks and cmdlets.
Trace-Command                     Cmdlet    Configures and starts a trace of the specified expression or command.
about_command_precedence          HelpFile  Describes how Windows PowerShell determines which command to run.
about_Command_Syntax              HelpFile  Describes the notation used for Windows PowerShell syntax in Help.
about_Core_Commands               HelpFile  Lists the cmdlets that are designed for use with Windows PowerShell


PS C:\Users\Windows-32>
```

```Powershell
PS C:\Users\Windows-32> Get-Help Get-Command

NAME
    Get-Command

SYNOPSIS
    Gets basic information about cmdlets and other elements of Windows PowerShell commands.


SYNTAX
    Get-Command [[-Name] <string[]>] [-CommandType {Alias | Function | Filter | Cmdlet | ExternalScript | Application |
     Script | All}] [[-ArgumentList] <Object[]>] [-Module <string[]>] [-Syntax] [-TotalCount <int>] [<CommonParameters>
    ]

    Get-Command [-Noun <string[]>] [-Verb <string[]>] [[-ArgumentList] <Object[]>] [-Module <string[]>] [-Syntax] [-Tot
    alCount <int>] [<CommonParameters>]


DESCRIPTION
    The Get-Command cmdlet gets basic information about cmdlets and other elements of Windows PowerShell commands in th
    e session, such as aliases, functions, filters, scripts, and applications.

    Get-Command gets its data directly from the code of a cmdlet, function, script, or alias, unlike Get-Help, which ge
    ts its information from help topic files.

    Without parameters, "Get-Command" gets all of the cmdlets and functions in the current session. "Get-Command *" get
    s all Windows PowerShell elements and all of the non-Windows-PowerShell files in the Path environment variable ($en
    v:path). It groups the files in the "Application" command type.

    You can use the Module parameter of Get-Command to find the commands that were added to the session by adding a Win
    dows PowerShell snap-in or importing a module.


RELATED LINKS
    Online version: http://go.microsoft.com/fwlink/?LinkID=113309
    about_Command_Precedence
    Get-Help
    Get-PSDrive
    Get-Member
    Import-PSSession
    Export-PSSession

REMARKS
    To see the examples, type: "get-help Get-Command -examples".
    For more information, type: "get-help Get-Command -detailed".
    For technical information, type: "get-help Get-Command -full".



PS C:\Users\Windows-32>
```

```Powershell
PS C:\Users\Windows-32> Get-Help about_command_precedence
TOPIC
    about_Command_Precedence

SHORT DESCRIPTION
    Describes how Windows PowerShell determines which command to run.

LONG DESCRIPTION
    This topic explains how Windows PowerShell determines which command to
    run, especially when a session contains more than one command with the
    same name. It also explains how to run commands that do not run by
    default, and it explains how to avoid command-name conflicts in your
    session.


  COMMAND PRECEDENCE
      When a session includes commands that have the same name, Windows
      PowerShell uses the following rules to decide which command to run.

      These rules become very important when you add commands to your session
      from modules, snap-ins, and other sessions.


      -- If you specify the path to a command, Windows PowerShell runs the
         command at the location specified by the path.

         For example, the following command runs the FindDocs.ps1
         script in the C:\TechDocs directory:

             C:\TechDocs\FindDocs.ps1

         As a security feature, Windows PowerShell does not run executable
         (native) commands, including Windows PowerShell scripts, unless the
         command is located in a path that is listed in the Path environment
         variable ($env:path) or unless you specify the path to the script
         file.

         To run a script that is in the current directory, specify the full
         path, or type a dot (.) to represent the current directory.

         For example, to run the FindDocs.ps1 file in the current directory,
         type:

             .\FindDocs.ps1


      -- If you do not specify a path, Windows PowerShell uses the following
         precedence order when it runs commands:

              1. Alias
              2. Function
              3. Cmdlet
              4. Native Windows commands

          Therefore, if you type "help", Windows PowerShell first looks for an
          alias named "help", then a function named "Help", and finally a
          cmdlet named "Help". It runs the first "help" item that it finds.

          For example, assume you have a function named Get-Map. Then, you add
          or import a cmdlet named Get-Map. By default, Windows PowerShell
          runs the function when you type "Get-Map".


      -- When the session contains items of the same type that have the same
         name, such as two cmdlets with the same name, Windows PowerShell
         runs the item that was added to the session most recently.

         For example, assume you have a cmdlet named Get-Date. Then, you import
         another cmdlet named Get-Date. By default, Windows PowerShell runs
         the most-recently imported cmdlet when you type "Get-Date".


  HIDDEN and REPLACED ITEMS
      As a result of these rules, items can be replaced or hidden by items with
      the same name.

      --  Items are "hidden" or "shadowed" if you can still access the original
          item, such as by qualifying the item name with a module or snap-in
          name.

          For example, if you import a function that has the same name as a
          cmdlet in the session, the cmdlet is hidden (but not replaced)
          because it was imported from a snap-in or module.


      --  Items are "replaced" or "overwritten" if you can no longer access
          the original item.

          For example, if you import a variable that has the same name as a
          a variable in the session, the original variable is replaced and is
          no longer accessible. You cannot qualify a variable with a module
          name.

          Also, if you type a function at the command line and then import
          a function with the same name, the original function is replaced and
          is no longer accessible.


  RUNNING HIDDEN COMMANDS
      You can run particular commands by specifying item properties that
      distinguish the command from other commands that might have the same
      name.

      You can use this method to run any command, but it is especially useful
      for running hidden commands.

      Use this method as a best practice when writing scripts that you intend
      to distribute because you cannot predict which commands might be present
      in the session in which the script runs.


      QUALIFIED NAMES
      You can run commands that have been imported from a Windows PowerShell
      snap-in or module or from another session by qualifying the command
      name with the name of the module or snap-in in which it originated.

      You can qualify commands, but you cannot qualify variables or aliases.

      For example, if the Get-Date cmdlet from the Microsoft.PowerShell.Utility
      snap-in is hidden by an alias, function, or cmdlet with the same name, you
      can run it by using the snap-in-qualified name of the cmdlet:

          Microsoft.PowerShell.Utility\Get-Date


      To run a New-Map command that was added by the MapFunctions module, use
      its module-qualified name:

          MapFunctions\New-Map


      To find the snap-in or module from which a command was imported, use the
      following Get-Command command format:

          get-command <command-name> | format-list -property Name, PSSnapin, Module


      For example, to find the source of the Get-Date cmdlet, type:


          get-command get-date | format-list -property Name, PSSnapin, Module

          Name     : Get-Date
          PSSnapIn : Microsoft.PowerShell.Utility
          Module   :


      CALL OPERATOR
      You can also use the Call operator (&) to run any command that you
      can get by using a Get-ChildItem (the alias is "dir"), Get-Command, or
      Get-Module command.

      To run a command, enclose the Get-Command command in parentheses,
      and use the Call operator (&) to run the command.

          &(get-command ...)

      - or -

          &(dir ... )


      For example, if you have a function named Map that is hidden by an
      alias named Map, use the following command to run the function.

          &(get-command -name map -type function)

      - or -

          &(dir function:\map)


      You can also save your hidden command in a variable to make it
      easier to run.

      For example, the following command saves the Map function in the
      $myMap variable and then uses the Call operator to run it.

          $myMap = (get-command -name map -type function)

          &($myMap)


      If a command originated in a module, you can use the following
      format to run it.

         & <PSModuleInfo-object> <command>

      For example, to run the Add-File cmdlet in the FileCommands
      module, use the following command sequence.

         $FileCommands = get-module -name FileCommands

         & $FileCommands Add-File



  REPLACED ITEMS
      Items that have not been imported from a module or snap-in, such as
      functions, variables, and aliases that you create in your session or
      that you add by using a profile can be replaced by commands that have
      the same name. If they are replaced, you cannot access them.

      Variables and aliases are always replaced even if they have been
      imported from a module or snap-in because you cannot use a call operator
      or a qualified name to run them.

      For example, if you type a Get-Map function in your session, and you
      import a function called Get-Map, the original function is replaced.
      You cannot retrieve it in the current session.


  AVOIDING NAME CONFLICTS
      The best way to manage command name conflicts is to prevent them. When
      you name your commands, use a name that is very specific or is likely to
      be unique. For example, add your initials or company name acronym to the
      nouns in your commands.

      Also, when you import commands into your session from a Windows PowerShell
      module or from another session, use the Prefix parameter of the
      Import-Module or Import-PSSession cmdlet to add a prefix to the nouns
      in the names of commands.

      For example, the following command avoids any conflict with the Get-Date
      and Set-Date cmdlets that come with Windows PowerShell when you import
      the DateFunctions module.

          import-module -name DateFunctions -prefix ZZ

      For more information, see Import-Module and Import-PSSession.


SEE ALSO
    about_Path_Syntax
    about_Aliases
    about_Functions
    Alias (provider)
    Function (provider)
    Get-Command
    Import-Module
    Import-PSSession
PS C:\Users\Windows-32>
```
