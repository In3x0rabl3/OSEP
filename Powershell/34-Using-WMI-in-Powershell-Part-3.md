#### 34. Using WMI in Powershell Part 3

- Explore ```Methods``` of a ```Class```

```PowerShell
PS C:\Users\Administrator> Get-WmiObject -Class Win32_Process -List | Select-Object -ExpandProperty Methods

Name          : Create
InParameters  : System.Management.ManagementBaseObject
OutParameters : System.Management.ManagementBaseObject
Origin        : Win32_Process
Qualifiers    : {Constructor, Implemented, MappingStrings, Privileges...}

Name          : Terminate
InParameters  : System.Management.ManagementBaseObject
OutParameters : System.Management.ManagementBaseObject
Origin        : Win32_Process
Qualifiers    : {Destructor, Implemented, MappingStrings, Privileges...}

Name          : GetOwner
InParameters  :
OutParameters : System.Management.ManagementBaseObject
Origin        : Win32_Process
Qualifiers    : {Implemented, MappingStrings, ValueMap}

Name          : GetOwnerSid
InParameters  :
OutParameters : System.Management.ManagementBaseObject
Origin        : Win32_Process
Qualifiers    : {Implemented, MappingStrings, ValueMap}

Name          : SetPriority
InParameters  : System.Management.ManagementBaseObject
OutParameters : System.Management.ManagementBaseObject
Origin        : Win32_Process
Qualifiers    : {Implemented, MappingStrings, ValueMap}

Name          : AttachDebugger
InParameters  :
OutParameters : System.Management.ManagementBaseObject
Origin        : Win32_Process
Qualifiers    : {Implemented, ValueMap}

Name          : GetAvailableVirtualSize
InParameters  :
OutParameters : System.Management.ManagementBaseObject
Origin        : Win32_Process
Qualifiers    : {Implemented, ValueMap}

PS C:\Users\Administrator>
```

- ```Invoke-WmiMethod``` - ```Local```

```PowerShell
PS C:\Users\Administrator> Invoke-WmiMethod -Class Win32_Process -Name Create -ArgumentList "notepad.exe"

__GENUS          : 2
__CLASS          : __PARAMETERS
__SUPERCLASS     :
__DYNASTY        : __PARAMETERS
__RELPATH        :
__PROPERTY_COUNT : 2
__DERIVATION     : {}
__SERVER         :
__NAMESPACE      :
__PATH           :
ProcessId        : 1164
ReturnValue      : 0
PSComputerName   :

PS C:\Users\Administrator>
```

```PowerShell
PS C:\Users\Administrator> Invoke-WmiMethod -Class Win32_Process -Name Create -ArgumentList "cmd.exe"

__GENUS          : 2
__CLASS          : __PARAMETERS
__SUPERCLASS     :
__DYNASTY        : __PARAMETERS
__RELPATH        :
__PROPERTY_COUNT : 2
__DERIVATION     : {}
__SERVER         :
__NAMESPACE      :
__PATH           :
ProcessId        : 1044
ReturnValue      : 0
PSComputerName   :

PS C:\Users\Administrator> 
```

```PowerShell
PS C:\Users\Administrator> Invoke-WmiMethod -Class Win32_Process -Name Create -ArgumentList "powershell.exe"

__GENUS          : 2
__CLASS          : __PARAMETERS
__SUPERCLASS     :
__DYNASTY        : __PARAMETERS
__RELPATH        :
__PROPERTY_COUNT : 2
__DERIVATION     : {}
__SERVER         :
__NAMESPACE      :
__PATH           :
ProcessId        : 3996
ReturnValue      : 0
PSComputerName   :

PS C:\Users\Administrator>
```

- ```Invoke-WmiMethod``` - ```Remote```

```PowerShell
PS C:\Users\Administrator> Invoke-WmiMethod -Class Win32_Process -Name Create -ArgumentList "powershell.exe" -ComputerName JOHN-PC -Credential John-PC\John

__GENUS          : 2
__CLASS          : __PARAMETERS
__SUPERCLASS     :
__DYNASTY        : __PARAMETERS
__RELPATH        :
__PROPERTY_COUNT : 2
__DERIVATION     : {}
__SERVER         :
__NAMESPACE      :
__PATH           :
ProcessId        : 3536
ReturnValue      : 0
PSComputerName   :

PS C:\Users\Administrator>
```

```ProcessId``` determines that the command has been executed.

- Run ```PowerShell``` commands - ```Local```

```PowerShell
PS C:\Users\Administrator> Invoke-WmiMethod -Class Win32_Process -Name Create -ArgumentList "powershell.exe -c Get-Service"

__GENUS          : 2
__CLASS          : __PARAMETERS
__SUPERCLASS     :
__DYNASTY        : __PARAMETERS
__RELPATH        :
__PROPERTY_COUNT : 2
__DERIVATION     : {}
__SERVER         :
__NAMESPACE      :
__PATH           :
ProcessId        : 2412
ReturnValue      : 0
PSComputerName   :

PS C:\Users\Administrator>
```

```PowerShell
PS C:\Users\Administrator> Invoke-WmiMethod -Class Win32_Process -Name Create -ArgumentList "powershell.exe -noexit -c Get-Service"

__GENUS          : 2
__CLASS          : __PARAMETERS
__SUPERCLASS     :
__DYNASTY        : __PARAMETERS
__RELPATH        :
__PROPERTY_COUNT : 2
__DERIVATION     : {}
__SERVER         :
__NAMESPACE      :
__PATH           :
ProcessId        : 2096
ReturnValue      : 0
PSComputerName   :

PS C:\Users\Administrator>
```

- Run ```PowerShell``` commands - ```Remote```

```PowerShell
PS C:\Users\Administrator> Invoke-WmiMethod -Class Win32_Process -Name Create -ArgumentList "powershell.exe -noexit -c Get-Service" -ComputerName JOHN-PC -Credential John-PC\John

__GENUS          : 2
__CLASS          : __PARAMETERS
__SUPERCLASS     :
__DYNASTY        : __PARAMETERS
__RELPATH        :
__PROPERTY_COUNT : 2
__DERIVATION     : {}
__SERVER         :
__NAMESPACE      :
__PATH           :
ProcessId        : 2280
ReturnValue      : 0
PSComputerName   :

PS C:\Users\Administrator>
```

Check that ```powershell.exe -noexit -c Get-Service``` has executed on the ```remote``` machine

```PowerShell
PS C:\Users\Administrator> Get-WmiObject -Class Win32_Process -Filter {Name="powershell.exe"} -ComputerName JOHN-PC -Credential John-PC\John

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="3236"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="3236"
Caption                    : powershell.exe
CommandLine                : "C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe"
CreationClassName          : Win32_Process
CreationDate               : 20170712123353.342056-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : powershell.exe
ExecutablePath             : C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe
ExecutionState             :
Handle                     : 3236
HandleCount                : 519
InstallDate                :
KernelModeTime             : 3905616
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : powershell.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 4376
OtherTransferCount         : 46062
PageFaults                 : 12085
PageFileUsage              : 24428
ParentProcessId            : 980
PeakPageFileUsage          : 37584
PeakVirtualSize            : 195739648
PeakWorkingSetSize         : 38424
Priority                   : 8
PrivatePageCount           : 25014272
ProcessId                  : 3236
QuotaNonPagedPoolUsage     : 12
QuotaPagedPoolUsage        : 148
QuotaPeakNonPagedPoolUsage : 12
QuotaPeakPagedPoolUsage    : 148
ReadOperationCount         : 267
ReadTransferCount          : 972300
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 5
UserModeTime               : 7811232
VirtualSize                : 184668160
WindowsVersion             : 6.1.7600
WorkingSetSize             : 30765056
WriteOperationCount        : 3
WriteTransferCount         : 6434
PSComputerName             : JOHN-PC
ProcessName                : powershell.exe
Handles                    : 519
VM                         : 184668160
WS                         : 30765056
Path                       : C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="3136"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="3136"
Caption                    : powershell.exe
CommandLine                : "C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe"
CreationClassName          : Win32_Process
CreationDate               : 20170712130457.189342-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : powershell.exe
ExecutablePath             : C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe
ExecutionState             :
Handle                     : 3136
HandleCount                : 384
InstallDate                :
KernelModeTime             : 1402016
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : powershell.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 3210
OtherTransferCount         : 39824
PageFaults                 : 10441
PageFileUsage              : 21412
ParentProcessId            : 980
PeakPageFileUsage          : 35928
PeakVirtualSize            : 180490240
PeakWorkingSetSize         : 37160
Priority                   : 8
PrivatePageCount           : 21925888
ProcessId                  : 3136
QuotaNonPagedPoolUsage     : 11
QuotaPagedPoolUsage        : 135
QuotaPeakNonPagedPoolUsage : 12
QuotaPeakPagedPoolUsage    : 135
ReadOperationCount         : 267
ReadTransferCount          : 978070
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 5
UserModeTime               : 3905616
VirtualSize                : 170201088
WindowsVersion             : 6.1.7600
WorkingSetSize             : 30535680
WriteOperationCount        : 3
WriteTransferCount         : 6434
PSComputerName             : JOHN-PC
ProcessName                : powershell.exe
Handles                    : 384
VM                         : 170201088
WS                         : 30535680
Path                       : C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="3536"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="3536"
Caption                    : powershell.exe
CommandLine                : powershell.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712190711.835494-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : powershell.exe
ExecutablePath             : C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
ExecutionState             :
Handle                     : 3536
HandleCount                : 226
InstallDate                :
KernelModeTime             : 801152
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : powershell.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 2476
OtherTransferCount         : 25882
PageFaults                 : 8693
PageFileUsage              : 26280
ParentProcessId            : 3656
PeakPageFileUsage          : 36124
PeakVirtualSize            : 159596544
PeakWorkingSetSize         : 33440
Priority                   : 8
PrivatePageCount           : 26910720
ProcessId                  : 3536
QuotaNonPagedPoolUsage     : 10
QuotaPagedPoolUsage        : 109
QuotaPeakNonPagedPoolUsage : 11
QuotaPeakPagedPoolUsage    : 109
ReadOperationCount         : 243
ReadTransferCount          : 936885
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 5
UserModeTime               : 1602304
VirtualSize                : 149045248
WindowsVersion             : 6.1.7600
WorkingSetSize             : 34164736
WriteOperationCount        : 3
WriteTransferCount         : 8132
PSComputerName             : JOHN-PC
ProcessName                : powershell.exe
Handles                    : 226
VM                         : 149045248
WS                         : 34164736
Path                       : C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="2280"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="2280"
Caption                    : powershell.exe
CommandLine                : powershell.exe -noexit -c Get-Service
CreationClassName          : Win32_Process
CreationDate               : 20170712191345.110997-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : powershell.exe
ExecutablePath             : C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
ExecutionState             :
Handle                     : 2280
HandleCount                : 240
InstallDate                :
KernelModeTime             : 1101584
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : powershell.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 2461
OtherTransferCount         : 29198
PageFaults                 : 9211
PageFileUsage              : 25280
ParentProcessId            : 2308
PeakPageFileUsage          : 36980
PeakVirtualSize            : 160145408
PeakWorkingSetSize         : 35136
Priority                   : 8
PrivatePageCount           : 25886720
ProcessId                  : 2280
QuotaNonPagedPoolUsage     : 10
QuotaPagedPoolUsage        : 109
QuotaPeakNonPagedPoolUsage : 11
QuotaPeakPagedPoolUsage    : 110
ReadOperationCount         : 243
ReadTransferCount          : 932839
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 5
UserModeTime               : 2303312
VirtualSize                : 149331968
WindowsVersion             : 6.1.7600
WorkingSetSize             : 34226176
WriteOperationCount        : 3
WriteTransferCount         : 8132
PSComputerName             : JOHN-PC
ProcessName                : powershell.exe
Handles                    : 240
VM                         : 149331968
WS                         : 34226176
Path                       : C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe

PS C:\Users\Administrator>
```

- Stop ```process``` using ```Remove-WmiObject```

```PowerShell
PS C:\Users\Administrator> Get-WmiObject -Class Win32_Process -Filter {Name="powershell.exe"} -ComputerName JOHN-PC -Credential John-PC\John | Remove-WmiObject
```

```PowerShell
PS C:\Users\Administrator> Get-WmiObject -Class Win32_Process -Filter {Name="powershell.exe"} -ComputerName JOHN-PC -Credential John-PC\John
```
