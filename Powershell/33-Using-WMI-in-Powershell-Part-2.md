#### 33. Using WMI in Powershell Part 2

- Using ```Get-WmiObject``` - ```Local```

```PowerShell
PS C:\Users\Administrator> Get-WmiObject -Class Win32_Process

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="0"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="0"
Caption                    : System Idle Process
CommandLine                :
CreationClassName          : Win32_Process
CreationDate               :
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : System Idle Process
ExecutablePath             :
ExecutionState             :
Handle                     : 0
HandleCount                : 0
InstallDate                :
KernelModeTime             : 199884687500
MaximumWorkingSetSize      :
MinimumWorkingSetSize      :
Name                       : System Idle Process
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 0
OtherTransferCount         : 0
PageFaults                 : 1
PageFileUsage              : 0
ParentProcessId            : 0
PeakPageFileUsage          : 0
PeakVirtualSize            : 65536
PeakWorkingSetSize         : 4
Priority                   : 0
PrivatePageCount           : 0
ProcessId                  : 0
QuotaNonPagedPoolUsage     : 0
QuotaPagedPoolUsage        : 0
QuotaPeakNonPagedPoolUsage : 0
QuotaPeakPagedPoolUsage    : 0
ReadOperationCount         : 0
ReadTransferCount          : 0
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 1
UserModeTime               : 0
VirtualSize                : 65536
WindowsVersion             : 6.3.9600
WorkingSetSize             : 4096
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : System Idle Process
Handles                    : 0
VM                         : 65536
WS                         : 4096
Path                       :

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="4"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="4"
Caption                    : System
CommandLine                :
CreationClassName          : Win32_Process
CreationDate               : 20170712121425.018613-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : System
ExecutablePath             :
ExecutionState             :
Handle                     : 4
HandleCount                : 805
InstallDate                :
KernelModeTime             : 479687500
MaximumWorkingSetSize      :
MinimumWorkingSetSize      :
Name                       : System
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 3466
OtherTransferCount         : 152451
PageFaults                 : 4798
PageFileUsage              : 112
ParentProcessId            : 0
PeakPageFileUsage          : 276
PeakVirtualSize            : 7389184
PeakWorkingSetSize         : 1716
Priority                   : 8
PrivatePageCount           : 114688
ProcessId                  : 4
QuotaNonPagedPoolUsage     : 0
QuotaPagedPoolUsage        : 0
QuotaPeakNonPagedPoolUsage : 0
QuotaPeakPagedPoolUsage    : 0
ReadOperationCount         : 195
ReadTransferCount          : 53093300
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 75
UserModeTime               : 0
VirtualSize                : 3432448
WindowsVersion             : 6.3.9600
WorkingSetSize             : 139264
WriteOperationCount        : 13174
WriteTransferCount         : 207929144
PSComputerName             : WIN-2012-DC
ProcessName                : System
Handles                    : 805
VM                         : 3432448
WS                         : 139264
Path                       :

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="208"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="208"
Caption                    : smss.exe
CommandLine                :
CreationClassName          : Win32_Process
CreationDate               : 20170712121425.018613-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : smss.exe
ExecutablePath             :
ExecutionState             :
Handle                     : 208
HandleCount                : 52
InstallDate                :
KernelModeTime             : 156250
MaximumWorkingSetSize      :
MinimumWorkingSetSize      :
Name                       : smss.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 266
OtherTransferCount         : 31584
PageFaults                 : 595
PageFileUsage              : 276
ParentProcessId            : 4
PeakPageFileUsage          : 336
PeakVirtualSize            : 25382912
PeakWorkingSetSize         : 1032
Priority                   : 11
PrivatePageCount           : 282624
ProcessId                  : 208
QuotaNonPagedPoolUsage     : 3
QuotaPagedPoolUsage        : 13
QuotaPeakNonPagedPoolUsage : 7
QuotaPeakPagedPoolUsage    : 53
ReadOperationCount         : 4
ReadTransferCount          : 29188
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 2
UserModeTime               : 0
VirtualSize                : 4317184
WindowsVersion             : 6.3.9600
WorkingSetSize             : 217088
WriteOperationCount        : 1
WriteTransferCount         : 32
PSComputerName             : WIN-2012-DC
ProcessName                : smss.exe
Handles                    : 52
VM                         : 4317184
WS                         : 217088
Path                       :

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="292"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="292"
Caption                    : csrss.exe
CommandLine                :
CreationClassName          : Win32_Process
CreationDate               : 20170712121426.081561-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : csrss.exe
ExecutablePath             :
ExecutionState             :
Handle                     : 292
HandleCount                : 171
InstallDate                :
KernelModeTime             : 5000000
MaximumWorkingSetSize      :
MinimumWorkingSetSize      :
Name                       : csrss.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 14627
OtherTransferCount         : 839996
PageFaults                 : 2988
PageFileUsage              : 1552
ParentProcessId            : 284
PeakPageFileUsage          : 1552
PeakVirtualSize            : 45264896
PeakWorkingSetSize         : 3352
Priority                   : 13
PrivatePageCount           : 1589248
ProcessId                  : 292
QuotaNonPagedPoolUsage     : 11
QuotaPagedPoolUsage        : 114
QuotaPeakNonPagedPoolUsage : 13
QuotaPeakPagedPoolUsage    : 122
ReadOperationCount         : 64
ReadTransferCount          : 55340
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 8
UserModeTime               : 781250
VirtualSize                : 44208128
WindowsVersion             : 6.3.9600
WorkingSetSize             : 1372160
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : csrss.exe
Handles                    : 171
VM                         : 44208128
WS                         : 1372160
Path                       :

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="344"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="344"
Caption                    : csrss.exe
CommandLine                :
CreationClassName          : Win32_Process
CreationDate               : 20170712121426.456426-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : csrss.exe
ExecutablePath             :
ExecutionState             :
Handle                     : 344
HandleCount                : 185
InstallDate                :
KernelModeTime             : 3906250
MaximumWorkingSetSize      :
MinimumWorkingSetSize      :
Name                       : csrss.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 3146
OtherTransferCount         : 69640
PageFaults                 : 65653
PageFileUsage              : 1496
ParentProcessId            : 336
PeakPageFileUsage          : 1552
PeakVirtualSize            : 85655552
PeakWorkingSetSize         : 35324
Priority                   : 13
PrivatePageCount           : 1531904
ProcessId                  : 344
QuotaNonPagedPoolUsage     : 16
QuotaPagedPoolUsage        : 162
QuotaPeakNonPagedPoolUsage : 17
QuotaPeakPagedPoolUsage    : 192
ReadOperationCount         : 34150
ReadTransferCount          : 1055474
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 10
UserModeTime               : 312500
VirtualSize                : 71057408
WindowsVersion             : 6.3.9600
WorkingSetSize             : 23605248
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : csrss.exe
Handles                    : 185
VM                         : 71057408
WS                         : 23605248
Path                       :

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="352"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="352"
Caption                    : wininit.exe
CommandLine                : wininit.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712121426.456426-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : wininit.exe
ExecutablePath             : C:\Windows\system32\wininit.exe
ExecutionState             :
Handle                     : 352
HandleCount                : 79
InstallDate                :
KernelModeTime             : 312500
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : wininit.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 1036
OtherTransferCount         : 2788
PageFaults                 : 1112
PageFileUsage              : 728
ParentProcessId            : 284
PeakPageFileUsage          : 956
PeakVirtualSize            : 45092864
PeakWorkingSetSize         : 3524
Priority                   : 13
PrivatePageCount           : 745472
ProcessId                  : 352
QuotaNonPagedPoolUsage     : 8
QuotaPagedPoolUsage        : 88
QuotaPeakNonPagedPoolUsage : 10
QuotaPeakPagedPoolUsage    : 90
ReadOperationCount         : 1
ReadTransferCount          : 6656
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 1
UserModeTime               : 156250
VirtualSize                : 41603072
WindowsVersion             : 6.3.9600
WorkingSetSize             : 294912
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : wininit.exe
Handles                    : 79
VM                         : 41603072
WS                         : 294912
Path                       : C:\Windows\system32\wininit.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="380"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="380"
Caption                    : winlogon.exe
CommandLine                : winlogon.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712121426.472426-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : winlogon.exe
ExecutablePath             : C:\Windows\system32\winlogon.exe
ExecutionState             :
Handle                     : 380
HandleCount                : 156
InstallDate                :
KernelModeTime             : 937500
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : winlogon.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 1216
OtherTransferCount         : 145120
PageFaults                 : 10679
PageFileUsage              : 1216
ParentProcessId            : 336
PeakPageFileUsage          : 2624
PeakVirtualSize            : 59760640
PeakWorkingSetSize         : 8728
Priority                   : 13
PrivatePageCount           : 1245184
ProcessId                  : 380
QuotaNonPagedPoolUsage     : 9
QuotaPagedPoolUsage        : 117
QuotaPeakNonPagedPoolUsage : 14
QuotaPeakPagedPoolUsage    : 117
ReadOperationCount         : 3
ReadTransferCount          : 144816
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 2
UserModeTime               : 0
VirtualSize                : 58621952
WindowsVersion             : 6.3.9600
WorkingSetSize             : 8900608
WriteOperationCount        : 1
WriteTransferCount         : 160
PSComputerName             : WIN-2012-DC
ProcessName                : winlogon.exe
Handles                    : 156
VM                         : 58621952
WS                         : 8900608
Path                       : C:\Windows\system32\winlogon.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="440"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="440"
Caption                    : services.exe
CommandLine                :
CreationClassName          : Win32_Process
CreationDate               : 20170712121426.721992-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : services.exe
ExecutablePath             :
ExecutionState             :
Handle                     : 440
HandleCount                : 220
InstallDate                :
KernelModeTime             : 2187500
MaximumWorkingSetSize      :
MinimumWorkingSetSize      :
Name                       : services.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 2992
OtherTransferCount         : 66586
PageFaults                 : 4283
PageFileUsage              : 2160
ParentProcessId            : 352
PeakPageFileUsage          : 2920
PeakVirtualSize            : 29523968
PeakWorkingSetSize         : 5740
Priority                   : 9
PrivatePageCount           : 2211840
ProcessId                  : 440
QuotaNonPagedPoolUsage     : 10
QuotaPagedPoolUsage        : 91
QuotaPeakNonPagedPoolUsage : 17
QuotaPeakPagedPoolUsage    : 92
ReadOperationCount         : 6
ReadTransferCount          : 243828
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 4
UserModeTime               : 2343750
VirtualSize                : 21508096
WindowsVersion             : 6.3.9600
WorkingSetSize             : 2916352
WriteOperationCount        : 1
WriteTransferCount         : 160
PSComputerName             : WIN-2012-DC
ProcessName                : services.exe
Handles                    : 220
VM                         : 21508096
WS                         : 2916352
Path                       :

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="448"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="448"
Caption                    : lsass.exe
CommandLine                : C:\Windows\system32\lsass.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712121426.768868-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : lsass.exe
ExecutablePath             : C:\Windows\system32\lsass.exe
ExecutionState             :
Handle                     : 448
HandleCount                : 1280
InstallDate                :
KernelModeTime             : 72343750
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : lsass.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 52553
OtherTransferCount         : 4821854
PageFaults                 : 40173
PageFileUsage              : 37732
ParentProcessId            : 352
PeakPageFileUsage          : 64580
PeakVirtualSize            : 1225867264
PeakWorkingSetSize         : 66640
Priority                   : 9
PrivatePageCount           : 38637568
ProcessId                  : 448
QuotaNonPagedPoolUsage     : 123
QuotaPagedPoolUsage        : 182
QuotaPeakNonPagedPoolUsage : 148
QuotaPeakPagedPoolUsage    : 187
ReadOperationCount         : 8959
ReadTransferCount          : 81985973
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 27
UserModeTime               : 46875000
VirtualSize                : 1202966528
WindowsVersion             : 6.3.9600
WorkingSetSize             : 28327936
WriteOperationCount        : 1541
WriteTransferCount         : 2072357
PSComputerName             : WIN-2012-DC
ProcessName                : lsass.exe
Handles                    : 1280
VM                         : 1202966528
WS                         : 28327936
Path                       : C:\Windows\system32\lsass.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="572"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="572"
Caption                    : svchost.exe
CommandLine                : C:\Windows\system32\svchost.exe -k DcomLaunch
CreationClassName          : Win32_Process
CreationDate               : 20170712121428.268496-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : svchost.exe
ExecutablePath             : C:\Windows\system32\svchost.exe
ExecutionState             :
Handle                     : 572
HandleCount                : 364
InstallDate                :
KernelModeTime             : 1562500
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 533
OtherTransferCount         : 22364
PageFaults                 : 5554
PageFileUsage              : 3372
ParentProcessId            : 440
PeakPageFileUsage          : 8228
PeakVirtualSize            : 50991104
PeakWorkingSetSize         : 12264
Priority                   : 8
PrivatePageCount           : 3452928
ProcessId                  : 572
QuotaNonPagedPoolUsage     : 15
QuotaPagedPoolUsage        : 174
QuotaPeakNonPagedPoolUsage : 20
QuotaPeakPagedPoolUsage    : 174
ReadOperationCount         : 2
ReadTransferCount          : 4608
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 8
UserModeTime               : 1250000
VirtualSize                : 47263744
WindowsVersion             : 6.3.9600
WorkingSetSize             : 7065600
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : svchost.exe
Handles                    : 364
VM                         : 47263744
WS                         : 7065600
Path                       : C:\Windows\system32\svchost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="600"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="600"
Caption                    : svchost.exe
CommandLine                : C:\Windows\system32\svchost.exe -k RPCSS
CreationClassName          : Win32_Process
CreationDate               : 20170712121428.502822-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : svchost.exe
ExecutablePath             : C:\Windows\system32\svchost.exe
ExecutionState             :
Handle                     : 600
HandleCount                : 333
InstallDate                :
KernelModeTime             : 6562500
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 1702
OtherTransferCount         : 82954
PageFaults                 : 5020
PageFileUsage              : 3080
ParentProcessId            : 440
PeakPageFileUsage          : 4380
PeakVirtualSize            : 32124928
PeakWorkingSetSize         : 7540
Priority                   : 8
PrivatePageCount           : 3153920
ProcessId                  : 600
QuotaNonPagedPoolUsage     : 18
QuotaPagedPoolUsage        : 71
QuotaPeakNonPagedPoolUsage : 26
QuotaPeakPagedPoolUsage    : 72
ReadOperationCount         : 0
ReadTransferCount          : 0
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 7
UserModeTime               : 10781250
VirtualSize                : 27353088
WindowsVersion             : 6.3.9600
WorkingSetSize             : 3796992
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : svchost.exe
Handles                    : 333
VM                         : 27353088
WS                         : 3796992
Path                       : C:\Windows\system32\svchost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="716"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="716"
Caption                    : dwm.exe
CommandLine                : "dwm.exe"
CreationClassName          : Win32_Process
CreationDate               : 20170712121428.721530-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : dwm.exe
ExecutablePath             : C:\Windows\system32\dwm.exe
ExecutionState             :
Handle                     : 716
HandleCount                : 174
InstallDate                :
KernelModeTime             : 6718750
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : dwm.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 276
OtherTransferCount         : 1874
PageFaults                 : 141908
PageFileUsage              : 25232
ParentProcessId            : 380
PeakPageFileUsage          : 29976
PeakVirtualSize            : 151556096
PeakWorkingSetSize         : 64424
Priority                   : 13
PrivatePageCount           : 25837568
ProcessId                  : 716
QuotaNonPagedPoolUsage     : 18
QuotaPagedPoolUsage        : 248
QuotaPeakNonPagedPoolUsage : 21
QuotaPeakPagedPoolUsage    : 285
ReadOperationCount         : 1
ReadTransferCount          : 60
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 7
UserModeTime               : 7343750
VirtualSize                : 135208960
WindowsVersion             : 6.3.9600
WorkingSetSize             : 48881664
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : dwm.exe
Handles                    : 174
VM                         : 135208960
WS                         : 48881664
Path                       : C:\Windows\system32\dwm.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="744"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="744"
Caption                    : VBoxService.exe
CommandLine                : C:\Windows\System32\VBoxService.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712121428.800220-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : VBoxService.exe
ExecutablePath             : C:\Windows\System32\VBoxService.exe
ExecutionState             :
Handle                     : 744
HandleCount                : 138
InstallDate                :
KernelModeTime             : 3750000
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : VBoxService.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 465654
OtherTransferCount         : 12640194
PageFaults                 : 84135
PageFileUsage              : 1912
ParentProcessId            : 440
PeakPageFileUsage          : 1972
PeakVirtualSize            : 60723200
PeakWorkingSetSize         : 4924
Priority                   : 8
PrivatePageCount           : 1957888
ProcessId                  : 744
QuotaNonPagedPoolUsage     : 10
QuotaPagedPoolUsage        : 98
QuotaPeakNonPagedPoolUsage : 11
QuotaPeakPagedPoolUsage    : 99
ReadOperationCount         : 2295
ReadTransferCount          : 9180
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 10
UserModeTime               : 1093750
VirtualSize                : 59535360
WindowsVersion             : 6.3.9600
WorkingSetSize             : 2842624
WriteOperationCount        : 2295
WriteTransferCount         : 36720
PSComputerName             : WIN-2012-DC
ProcessName                : VBoxService.exe
Handles                    : 138
VM                         : 59535360
WS                         : 2842624
Path                       : C:\Windows\System32\VBoxService.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="828"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="828"
Caption                    : svchost.exe
CommandLine                : C:\Windows\System32\svchost.exe -k LocalServiceNetworkRestricted
CreationClassName          : Win32_Process
CreationDate               : 20170712121428.974985-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : svchost.exe
ExecutablePath             : C:\Windows\System32\svchost.exe
ExecutionState             :
Handle                     : 828
HandleCount                : 454
InstallDate                :
KernelModeTime             : 2656250
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 11449
OtherTransferCount         : 278936
PageFaults                 : 15593
PageFileUsage              : 11600
ParentProcessId            : 440
PeakPageFileUsage          : 12628
PeakVirtualSize            : 417185792
PeakWorkingSetSize         : 18704
Priority                   : 8
PrivatePageCount           : 11878400
ProcessId                  : 828
QuotaNonPagedPoolUsage     : 20
QuotaPagedPoolUsage        : 99
QuotaPeakNonPagedPoolUsage : 90
QuotaPeakPagedPoolUsage    : 775
ReadOperationCount         : 630
ReadTransferCount          : 20226304
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 12
UserModeTime               : 4062500
VirtualSize                : 61456384
WindowsVersion             : 6.3.9600
WorkingSetSize             : 10960896
WriteOperationCount        : 1981
WriteTransferCount         : 24967416
PSComputerName             : WIN-2012-DC
ProcessName                : svchost.exe
Handles                    : 454
VM                         : 61456384
WS                         : 10960896
Path                       : C:\Windows\System32\svchost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="868"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="868"
Caption                    : svchost.exe
CommandLine                : C:\Windows\system32\svchost.exe -k netsvcs
CreationClassName          : Win32_Process
CreationDate               : 20170712121429.077424-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : svchost.exe
ExecutablePath             : C:\Windows\system32\svchost.exe
ExecutionState             :
Handle                     : 868
HandleCount                : 1475
InstallDate                :
KernelModeTime             : 1416875000
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 16234650
OtherTransferCount         : 4483847620
PageFaults                 : 7101408
PageFileUsage              : 32672
ParentProcessId            : 440
PeakPageFileUsage          : 529172
PeakVirtualSize            : 1013297152
PeakWorkingSetSize         : 503340
Priority                   : 8
PrivatePageCount           : 33456128
ProcessId                  : 868
QuotaNonPagedPoolUsage     : 55
QuotaPagedPoolUsage        : 310
QuotaPeakNonPagedPoolUsage : 1411
QuotaPeakPagedPoolUsage    : 545
ReadOperationCount         : 636061
ReadTransferCount          : 4894774184
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 36
UserModeTime               : 2436875000
VirtualSize                : 701538304
WindowsVersion             : 6.3.9600
WorkingSetSize             : 32976896
WriteOperationCount        : 66929
WriteTransferCount         : 6173153501
PSComputerName             : WIN-2012-DC
ProcessName                : svchost.exe
Handles                    : 1475
VM                         : 701538304
WS                         : 32976896
Path                       : C:\Windows\system32\svchost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="916"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="916"
Caption                    : svchost.exe
CommandLine                : C:\Windows\system32\svchost.exe -k LocalService
CreationClassName          : Win32_Process
CreationDate               : 20170712121429.146469-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : svchost.exe
ExecutablePath             : C:\Windows\system32\svchost.exe
ExecutionState             :
Handle                     : 916
HandleCount                : 476
InstallDate                :
KernelModeTime             : 937500
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 8412
OtherTransferCount         : 477118
PageFaults                 : 5256
PageFileUsage              : 4960
ParentProcessId            : 440
PeakPageFileUsage          : 5688
PeakVirtualSize            : 86732800
PeakWorkingSetSize         : 10468
Priority                   : 8
PrivatePageCount           : 5079040
ProcessId                  : 916
QuotaNonPagedPoolUsage     : 26
QuotaPagedPoolUsage        : 176
QuotaPeakNonPagedPoolUsage : 31
QuotaPeakPagedPoolUsage    : 180
ReadOperationCount         : 58
ReadTransferCount          : 7882
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 17
UserModeTime               : 2500000
VirtualSize                : 82997248
WindowsVersion             : 6.3.9600
WorkingSetSize             : 7589888
WriteOperationCount        : 13
WriteTransferCount         : 1156
PSComputerName             : WIN-2012-DC
ProcessName                : svchost.exe
Handles                    : 476
VM                         : 82997248
WS                         : 7589888
Path                       : C:\Windows\system32\svchost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="976"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="976"
Caption                    : svchost.exe
CommandLine                : C:\Windows\system32\svchost.exe -k NetworkService
CreationClassName          : Win32_Process
CreationDate               : 20170712121429.232454-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : svchost.exe
ExecutablePath             : C:\Windows\system32\svchost.exe
ExecutionState             :
Handle                     : 976
HandleCount                : 765
InstallDate                :
KernelModeTime             : 27968750
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 114190
OtherTransferCount         : 7318686
PageFaults                 : 69903
PageFileUsage              : 10460
ParentProcessId            : 440
PeakPageFileUsage          : 28680
PeakVirtualSize            : 1432371200
PeakWorkingSetSize         : 37824
Priority                   : 8
PrivatePageCount           : 10711040
ProcessId                  : 976
QuotaNonPagedPoolUsage     : 59
QuotaPagedPoolUsage        : 198
QuotaPeakNonPagedPoolUsage : 635
QuotaPeakPagedPoolUsage    : 681
ReadOperationCount         : 2943
ReadTransferCount          : 24663723
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 18
UserModeTime               : 21406250
VirtualSize                : 1192726528
WindowsVersion             : 6.3.9600
WorkingSetSize             : 13594624
WriteOperationCount        : 47787
WriteTransferCount         : 240797843
PSComputerName             : WIN-2012-DC
ProcessName                : svchost.exe
Handles                    : 765
VM                         : 1192726528
WS                         : 13594624
Path                       : C:\Windows\system32\svchost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="432"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="432"
Caption                    : svchost.exe
CommandLine                : C:\Windows\system32\svchost.exe -k LocalServiceNoNetwork
CreationClassName          : Win32_Process
CreationDate               : 20170712121429.404423-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : svchost.exe
ExecutablePath             : C:\Windows\system32\svchost.exe
ExecutionState             :
Handle                     : 432
HandleCount                : 367
InstallDate                :
KernelModeTime             : 468750
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 4261
OtherTransferCount         : 204542
PageFaults                 : 9080
PageFileUsage              : 6392
ParentProcessId            : 440
PeakPageFileUsage          : 6732
PeakVirtualSize            : 53354496
PeakWorkingSetSize         : 10496
Priority                   : 8
PrivatePageCount           : 6545408
ProcessId                  : 432
QuotaNonPagedPoolUsage     : 33
QuotaPagedPoolUsage        : 87
QuotaPeakNonPagedPoolUsage : 36
QuotaPeakPagedPoolUsage    : 89
ReadOperationCount         : 0
ReadTransferCount          : 0
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 17
UserModeTime               : 1718750
VirtualSize                : 51679232
WindowsVersion             : 6.3.9600
WorkingSetSize             : 5402624
WriteOperationCount        : 1
WriteTransferCount         : 32768
PSComputerName             : WIN-2012-DC
ProcessName                : svchost.exe
Handles                    : 367
VM                         : 51679232
WS                         : 5402624
Path                       : C:\Windows\system32\svchost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1416"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="1416"
Caption                    : spoolsv.exe
CommandLine                : C:\Windows\System32\spoolsv.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712121450.375156-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : spoolsv.exe
ExecutablePath             : C:\Windows\System32\spoolsv.exe
ExecutionState             :
Handle                     : 1416
HandleCount                : 371
InstallDate                :
KernelModeTime             : 468750
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : spoolsv.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 862
OtherTransferCount         : 34088
PageFaults                 : 3144
PageFileUsage              : 3036
ParentProcessId            : 440
PeakPageFileUsage          : 3424
PeakVirtualSize            : 74260480
PeakWorkingSetSize         : 8664
Priority                   : 8
PrivatePageCount           : 3108864
ProcessId                  : 1416
QuotaNonPagedPoolUsage     : 20
QuotaPagedPoolUsage        : 153
QuotaPeakNonPagedPoolUsage : 24
QuotaPeakPagedPoolUsage    : 158
ReadOperationCount         : 3
ReadTransferCount          : 1464
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 9
UserModeTime               : 468750
VirtualSize                : 72437760
WindowsVersion             : 6.3.9600
WorkingSetSize             : 2703360
WriteOperationCount        : 2
WriteTransferCount         : 320
PSComputerName             : WIN-2012-DC
ProcessName                : spoolsv.exe
Handles                    : 371
VM                         : 72437760
WS                         : 2703360
Path                       : C:\Windows\System32\spoolsv.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1368"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="1368"
Caption                    : Microsoft.ActiveDirectory.WebServices.exe
CommandLine                : C:\Windows\ADWS\Microsoft.ActiveDirectory.WebServices.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712121450.413055-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : Microsoft.ActiveDirectory.WebServices.exe
ExecutablePath             : C:\Windows\ADWS\Microsoft.ActiveDirectory.WebServices.exe
ExecutionState             :
Handle                     : 1368
HandleCount                : 1137
InstallDate                :
KernelModeTime             : 1718750
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : Microsoft.ActiveDirectory.WebServices.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 19837
OtherTransferCount         : 664902
PageFaults                 : 36144
PageFileUsage              : 30624
ParentProcessId            : 440
PeakPageFileUsage          : 33404
PeakVirtualSize            : 595652608
PeakWorkingSetSize         : 40372
Priority                   : 8
PrivatePageCount           : 31358976
ProcessId                  : 1368
QuotaNonPagedPoolUsage     : 38
QuotaPagedPoolUsage        : 350
QuotaPeakNonPagedPoolUsage : 45
QuotaPeakPagedPoolUsage    : 351
ReadOperationCount         : 145
ReadTransferCount          : 429485
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 9
UserModeTime               : 4218750
VirtualSize                : 591695872
WindowsVersion             : 6.3.9600
WorkingSetSize             : 8187904
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : Microsoft.ActiveDirectory.WebServices.exe
Handles                    : 1137
VM                         : 591695872
WS                         : 8187904
Path                       : C:\Windows\ADWS\Microsoft.ActiveDirectory.WebServices.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1408"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="1408"
Caption                    : dfsrs.exe
CommandLine                : C:\Windows\system32\DFSRs.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712121450.696161-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : dfsrs.exe
ExecutablePath             : C:\Windows\system32\DFSRs.exe
ExecutionState             :
Handle                     : 1408
HandleCount                : 326
InstallDate                :
KernelModeTime             : 82187500
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : dfsrs.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 1135772
OtherTransferCount         : 205072548
PageFaults                 : 24017
PageFileUsage              : 14000
ParentProcessId            : 440
PeakPageFileUsage          : 16580
PeakVirtualSize            : 634163200
PeakWorkingSetSize         : 20244
Priority                   : 8
PrivatePageCount           : 14336000
ProcessId                  : 1408
QuotaNonPagedPoolUsage     : 31
QuotaPagedPoolUsage        : 125
QuotaPeakNonPagedPoolUsage : 35
QuotaPeakPagedPoolUsage    : 125
ReadOperationCount         : 2257
ReadTransferCount          : 11713324
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 16
UserModeTime               : 167031250
VirtualSize                : 632573952
WindowsVersion             : 6.3.9600
WorkingSetSize             : 8740864
WriteOperationCount        : 7233
WriteTransferCount         : 96925643
PSComputerName             : WIN-2012-DC
ProcessName                : dfsrs.exe
Handles                    : 326
VM                         : 632573952
WS                         : 8740864
Path                       : C:\Windows\system32\DFSRs.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1508"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="1508"
Caption                    : dns.exe
CommandLine                : C:\Windows\system32\dns.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712121450.752362-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : dns.exe
ExecutablePath             : C:\Windows\system32\dns.exe
ExecutionState             :
Handle                     : 1508
HandleCount                : 10288
InstallDate                :
KernelModeTime             : 5625000
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : dns.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 57082
OtherTransferCount         : 1418712
PageFaults                 : 30531
PageFileUsage              : 89072
ParentProcessId            : 440
PeakPageFileUsage          : 89472
PeakVirtualSize            : 147890176
PeakWorkingSetSize         : 87164
Priority                   : 8
PrivatePageCount           : 91209728
ProcessId                  : 1508
QuotaNonPagedPoolUsage     : 10059
QuotaPagedPoolUsage        : 1262
QuotaPeakNonPagedPoolUsage : 10295
QuotaPeakPagedPoolUsage    : 1264
ReadOperationCount         : 75
ReadTransferCount          : 8700
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 14
UserModeTime               : 2812500
VirtualSize                : 146837504
WindowsVersion             : 6.3.9600
WorkingSetSize             : 9383936
WriteOperationCount        : 78
WriteTransferCount         : 12000
PSComputerName             : WIN-2012-DC
ProcessName                : dns.exe
Handles                    : 10288
VM                         : 146837504
WS                         : 9383936
Path                       : C:\Windows\system32\dns.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1548"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="1548"
Caption                    : ismserv.exe
CommandLine                : C:\Windows\System32\ismserv.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712121450.809793-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : ismserv.exe
ExecutablePath             : C:\Windows\System32\ismserv.exe
ExecutionState             :
Handle                     : 1548
HandleCount                : 88
InstallDate                :
KernelModeTime             : 156250
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : ismserv.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 377
OtherTransferCount         : 6646
PageFaults                 : 1448
PageFileUsage              : 1380
ParentProcessId            : 440
PeakPageFileUsage          : 1640
PeakVirtualSize            : 29483008
PeakWorkingSetSize         : 4108
Priority                   : 8
PrivatePageCount           : 1413120
ProcessId                  : 1548
QuotaNonPagedPoolUsage     : 11
QuotaPagedPoolUsage        : 39
QuotaPeakNonPagedPoolUsage : 12
QuotaPeakPagedPoolUsage    : 39
ReadOperationCount         : 0
ReadTransferCount          : 0
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 6
UserModeTime               : 0
VirtualSize                : 26324992
WindowsVersion             : 6.3.9600
WorkingSetSize             : 839680
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : ismserv.exe
Handles                    : 88
VM                         : 26324992
WS                         : 839680
Path                       : C:\Windows\System32\ismserv.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1700"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="1700"
Caption                    : wlms.exe
CommandLine                : C:\Windows\system32\wlms\wlms.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712121451.074083-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : wlms.exe
ExecutablePath             : C:\Windows\system32\wlms\wlms.exe
ExecutionState             :
Handle                     : 1700
HandleCount                : 39
InstallDate                :
KernelModeTime             : 0
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : wlms.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 51
OtherTransferCount         : 194
PageFaults                 : 1090
PageFileUsage              : 484
ParentProcessId            : 440
PeakPageFileUsage          : 576
PeakVirtualSize            : 15691776
PeakWorkingSetSize         : 2620
Priority                   : 8
PrivatePageCount           : 495616
ProcessId                  : 1700
QuotaNonPagedPoolUsage     : 4
QuotaPagedPoolUsage        : 29
QuotaPeakNonPagedPoolUsage : 5
QuotaPeakPagedPoolUsage    : 29
ReadOperationCount         : 0
ReadTransferCount          : 0
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 2
UserModeTime               : 0
VirtualSize                : 14626816
WindowsVersion             : 6.3.9600
WorkingSetSize             : 1306624
WriteOperationCount        : 48
WriteTransferCount         : 1228
PSComputerName             : WIN-2012-DC
ProcessName                : wlms.exe
Handles                    : 39
VM                         : 14626816
WS                         : 1306624
Path                       : C:\Windows\system32\wlms\wlms.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1708"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="1708"
Caption                    : dfssvc.exe
CommandLine                : C:\Windows\system32\dfssvc.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712121451.112485-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : dfssvc.exe
ExecutablePath             : C:\Windows\system32\dfssvc.exe
ExecutionState             :
Handle                     : 1708
HandleCount                : 131
InstallDate                :
KernelModeTime             : 156250
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : dfssvc.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 437
OtherTransferCount         : 10480
PageFaults                 : 2137
PageFileUsage              : 1912
ParentProcessId            : 440
PeakPageFileUsage          : 2068
PeakVirtualSize            : 32190464
PeakWorkingSetSize         : 5000
Priority                   : 8
PrivatePageCount           : 1957888
ProcessId                  : 1708
QuotaNonPagedPoolUsage     : 13
QuotaPagedPoolUsage        : 48
QuotaPeakNonPagedPoolUsage : 15
QuotaPeakPagedPoolUsage    : 48
ReadOperationCount         : 15
ReadTransferCount          : 3374
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 11
UserModeTime               : 0
VirtualSize                : 30593024
WindowsVersion             : 6.3.9600
WorkingSetSize             : 2887680
WriteOperationCount        : 14
WriteTransferCount         : 6034
PSComputerName             : WIN-2012-DC
ProcessName                : dfssvc.exe
Handles                    : 131
VM                         : 30593024
WS                         : 2887680
Path                       : C:\Windows\system32\dfssvc.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1316"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="1316"
Caption                    : vds.exe
CommandLine                : C:\Windows\System32\vds.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712121512.030634-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : vds.exe
ExecutablePath             : C:\Windows\System32\vds.exe
ExecutionState             :
Handle                     : 1316
HandleCount                : 158
InstallDate                :
KernelModeTime             : 625000
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : vds.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 841
OtherTransferCount         : 28175
PageFaults                 : 2931
PageFileUsage              : 1772
ParentProcessId            : 440
PeakPageFileUsage          : 2152
PeakVirtualSize            : 48394240
PeakWorkingSetSize         : 7856
Priority                   : 8
PrivatePageCount           : 1814528
ProcessId                  : 1316
QuotaNonPagedPoolUsage     : 16
QuotaPagedPoolUsage        : 88
QuotaPeakNonPagedPoolUsage : 19
QuotaPeakPagedPoolUsage    : 92
ReadOperationCount         : 32
ReadTransferCount          : 94208
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 11
UserModeTime               : 156250
VirtualSize                : 45608960
WindowsVersion             : 6.3.9600
WorkingSetSize             : 1138688
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : vds.exe
Handles                    : 158
VM                         : 45608960
WS                         : 1138688
Path                       : C:\Windows\System32\vds.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1248"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="1248"
Caption                    : svchost.exe
CommandLine                : C:\Windows\System32\svchost.exe -k termsvcs
CreationClassName          : Win32_Process
CreationDate               : 20170712121512.705767-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : svchost.exe
ExecutablePath             : C:\Windows\System32\svchost.exe
ExecutionState             :
Handle                     : 1248
HandleCount                : 401
InstallDate                :
KernelModeTime             : 937500
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 262
OtherTransferCount         : 840
PageFaults                 : 4263
PageFileUsage              : 3432
ParentProcessId            : 440
PeakPageFileUsage          : 3548
PeakVirtualSize            : 76869632
PeakWorkingSetSize         : 7380
Priority                   : 8
PrivatePageCount           : 3514368
ProcessId                  : 1248
QuotaNonPagedPoolUsage     : 19
QuotaPagedPoolUsage        : 151
QuotaPeakNonPagedPoolUsage : 19
QuotaPeakPagedPoolUsage    : 154
ReadOperationCount         : 0
ReadTransferCount          : 0
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 22
UserModeTime               : 781250
VirtualSize                : 75804672
WindowsVersion             : 6.3.9600
WorkingSetSize             : 2772992
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : svchost.exe
Handles                    : 401
VM                         : 75804672
WS                         : 2772992
Path                       : C:\Windows\System32\svchost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1336"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="1336"
Caption                    : svchost.exe
CommandLine                : C:\Windows\system32\svchost.exe -k NetworkServiceNetworkRestricted
CreationClassName          : Win32_Process
CreationDate               : 20170712121512.750613-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : svchost.exe
ExecutablePath             : C:\Windows\system32\svchost.exe
ExecutionState             :
Handle                     : 1336
HandleCount                : 107
InstallDate                :
KernelModeTime             : 1406250
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 2288
OtherTransferCount         : 122758
PageFaults                 : 2380
PageFileUsage              : 1052
ParentProcessId            : 440
PeakPageFileUsage          : 1204
PeakVirtualSize            : 22446080
PeakWorkingSetSize         : 4368
Priority                   : 8
PrivatePageCount           : 1077248
ProcessId                  : 1336
QuotaNonPagedPoolUsage     : 11
QuotaPagedPoolUsage        : 46
QuotaPeakNonPagedPoolUsage : 13
QuotaPeakPagedPoolUsage    : 46
ReadOperationCount         : 0
ReadTransferCount          : 0
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 3
UserModeTime               : 312500
VirtualSize                : 21381120
WindowsVersion             : 6.3.9600
WorkingSetSize             : 1826816
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : svchost.exe
Handles                    : 107
VM                         : 21381120
WS                         : 1826816
Path                       : C:\Windows\system32\svchost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="2060"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="2060"
Caption                    : svchost.exe
CommandLine                : C:\Windows\system32\svchost.exe -k LocalSystemNetworkRestricted
CreationClassName          : Win32_Process
CreationDate               : 20170712121512.780955-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : svchost.exe
ExecutablePath             : C:\Windows\system32\svchost.exe
ExecutionState             :
Handle                     : 2060
HandleCount                : 261
InstallDate                :
KernelModeTime             : 625000
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 1670
OtherTransferCount         : 37440
PageFaults                 : 6773
PageFileUsage              : 7724
ParentProcessId            : 440
PeakPageFileUsage          : 11332
PeakVirtualSize            : 1166675968
PeakWorkingSetSize         : 12516
Priority                   : 8
PrivatePageCount           : 7909376
ProcessId                  : 2060
QuotaNonPagedPoolUsage     : 18
QuotaPagedPoolUsage        : 126
QuotaPeakNonPagedPoolUsage : 19
QuotaPeakPagedPoolUsage    : 127
ReadOperationCount         : 389
ReadTransferCount          : 12832768
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 8
UserModeTime               : 0
VirtualSize                : 628494336
WindowsVersion             : 6.3.9600
WorkingSetSize             : 3465216
WriteOperationCount        : 360
WriteTransferCount         : 2072576
PSComputerName             : WIN-2012-DC
ProcessName                : svchost.exe
Handles                    : 261
VM                         : 628494336
WS                         : 3465216
Path                       : C:\Windows\system32\svchost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="2600"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="2600"
Caption                    : msdtc.exe
CommandLine                : C:\Windows\System32\msdtc.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712121711.180176-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : msdtc.exe
ExecutablePath             : C:\Windows\System32\msdtc.exe
ExecutionState             :
Handle                     : 2600
HandleCount                : 158
InstallDate                :
KernelModeTime             : 0
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : msdtc.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 158
OtherTransferCount         : 274
PageFaults                 : 2084
PageFileUsage              : 2312
ParentProcessId            : 440
PeakPageFileUsage          : 2480
PeakVirtualSize            : 42795008
PeakWorkingSetSize         : 6812
Priority                   : 8
PrivatePageCount           : 2367488
ProcessId                  : 2600
QuotaNonPagedPoolUsage     : 12
QuotaPagedPoolUsage        : 74
QuotaPeakNonPagedPoolUsage : 13
QuotaPeakPagedPoolUsage    : 74
ReadOperationCount         : 0
ReadTransferCount          : 0
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 9
UserModeTime               : 0
VirtualSize                : 41689088
WindowsVersion             : 6.3.9600
WorkingSetSize             : 413696
WriteOperationCount        : 3
WriteTransferCount         : 1286144
PSComputerName             : WIN-2012-DC
ProcessName                : msdtc.exe
Handles                    : 158
VM                         : 41689088
WS                         : 413696
Path                       : C:\Windows\System32\msdtc.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="260"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="260"
Caption                    : taskhostex.exe
CommandLine                : taskhostex.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712145926.030215-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : taskhostex.exe
ExecutablePath             : C:\Windows\system32\taskhostex.exe
ExecutionState             :
Handle                     : 260
HandleCount                : 195
InstallDate                :
KernelModeTime             : 468750
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : taskhostex.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 787
OtherTransferCount         : 10860
PageFaults                 : 2543
PageFileUsage              : 2676
ParentProcessId            : 868
PeakPageFileUsage          : 3172
PeakVirtualSize            : 232296448
PeakWorkingSetSize         : 7604
Priority                   : 8
PrivatePageCount           : 2740224
ProcessId                  : 260
QuotaNonPagedPoolUsage     : 17
QuotaPagedPoolUsage        : 168
QuotaPeakNonPagedPoolUsage : 21
QuotaPeakPagedPoolUsage    : 170
ReadOperationCount         : 27
ReadTransferCount          : 1724416
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 5
UserModeTime               : 156250
VirtualSize                : 230174720
WindowsVersion             : 6.3.9600
WorkingSetSize             : 7614464
WriteOperationCount        : 43
WriteTransferCount         : 835584
PSComputerName             : WIN-2012-DC
ProcessName                : taskhostex.exe
Handles                    : 195
VM                         : 230174720
WS                         : 7614464
Path                       : C:\Windows\system32\taskhostex.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1188"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="1188"
Caption                    : explorer.exe
CommandLine                : C:\Windows\Explorer.EXE
CreationClassName          : Win32_Process
CreationDate               : 20170712145926.061690-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : explorer.exe
ExecutablePath             : C:\Windows\Explorer.EXE
ExecutionState             :
Handle                     : 1188
HandleCount                : 1207
InstallDate                :
KernelModeTime             : 167343750
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : explorer.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 38649
OtherTransferCount         : 982340
PageFaults                 : 151042
PageFileUsage              : 37648
ParentProcessId            : 1860
PeakPageFileUsage          : 48264
PeakVirtualSize            : 588001280
PeakWorkingSetSize         : 91248
Priority                   : 8
PrivatePageCount           : 38551552
ProcessId                  : 1188
QuotaNonPagedPoolUsage     : 67
QuotaPagedPoolUsage        : 1049
QuotaPeakNonPagedPoolUsage : 95
QuotaPeakPagedPoolUsage    : 1189
ReadOperationCount         : 3022
ReadTransferCount          : 3067227
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 43
UserModeTime               : 78593750
VirtualSize                : 509153280
WindowsVersion             : 6.3.9600
WorkingSetSize             : 75325440
WriteOperationCount        : 151
WriteTransferCount         : 25552
PSComputerName             : WIN-2012-DC
ProcessName                : explorer.exe
Handles                    : 1207
VM                         : 509153280
WS                         : 75325440
Path                       : C:\Windows\Explorer.EXE

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="3492"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="3492"
Caption                    : VBoxTray.exe
CommandLine                : "C:\Windows\System32\VBoxTray.exe"
CreationClassName          : Win32_Process
CreationDate               : 20170712145937.014436-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : VBoxTray.exe
ExecutablePath             : C:\Windows\System32\VBoxTray.exe
ExecutionState             :
Handle                     : 3492
HandleCount                : 175
InstallDate                :
KernelModeTime             : 156250
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : VBoxTray.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 29914
OtherTransferCount         : 226456
PageFaults                 : 11696
PageFileUsage              : 1792
ParentProcessId            : 1188
PeakPageFileUsage          : 1888
PeakVirtualSize            : 89497600
PeakWorkingSetSize         : 6284
Priority                   : 8
PrivatePageCount           : 1835008
ProcessId                  : 3492
QuotaNonPagedPoolUsage     : 12
QuotaPagedPoolUsage        : 152
QuotaPeakNonPagedPoolUsage : 13
QuotaPeakPagedPoolUsage    : 153
ReadOperationCount         : 4590
ReadTransferCount          : 36720
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 10
UserModeTime               : 0
VirtualSize                : 85270528
WindowsVersion             : 6.3.9600
WorkingSetSize             : 6385664
WriteOperationCount        : 2295
WriteTransferCount         : 9180
PSComputerName             : WIN-2012-DC
ProcessName                : VBoxTray.exe
Handles                    : 175
VM                         : 85270528
WS                         : 6385664
Path                       : C:\Windows\System32\VBoxTray.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="3944"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="3944"
Caption                    : cmd.exe
CommandLine                : "C:\Windows\system32\cmd.exe"
CreationClassName          : Win32_Process
CreationDate               : 20170712151804.014863-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : cmd.exe
ExecutablePath             : C:\Windows\system32\cmd.exe
ExecutionState             :
Handle                     : 3944
HandleCount                : 31
InstallDate                :
KernelModeTime             : 0
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : cmd.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 226
OtherTransferCount         : 3268
PageFaults                 : 634
PageFileUsage              : 1516
ParentProcessId            : 1188
PeakPageFileUsage          : 2612
PeakVirtualSize            : 13705216
PeakWorkingSetSize         : 2184
Priority                   : 8
PrivatePageCount           : 1552384
ProcessId                  : 3944
QuotaNonPagedPoolUsage     : 3
QuotaPagedPoolUsage        : 24
QuotaPeakNonPagedPoolUsage : 4
QuotaPeakPagedPoolUsage    : 25
ReadOperationCount         : 0
ReadTransferCount          : 0
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 1
UserModeTime               : 0
VirtualSize                : 12517376
WindowsVersion             : 6.3.9600
WorkingSetSize             : 2215936
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : cmd.exe
Handles                    : 31
VM                         : 12517376
WS                         : 2215936
Path                       : C:\Windows\system32\cmd.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="3120"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="3120"
Caption                    : conhost.exe
CommandLine                : \??\C:\Windows\system32\conhost.exe 0x4
CreationClassName          : Win32_Process
CreationDate               : 20170712151804.031029-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : conhost.exe
ExecutablePath             : C:\Windows\system32\conhost.exe
ExecutionState             :
Handle                     : 3120
HandleCount                : 57
InstallDate                :
KernelModeTime             : 312500
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : conhost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 275
OtherTransferCount         : 12923
PageFaults                 : 1915
PageFileUsage              : 1012
ParentProcessId            : 3944
PeakPageFileUsage          : 1128
PeakVirtualSize            : 62922752
PeakWorkingSetSize         : 6096
Priority                   : 8
PrivatePageCount           : 1036288
ProcessId                  : 3120
QuotaNonPagedPoolUsage     : 7
QuotaPagedPoolUsage        : 107
QuotaPeakNonPagedPoolUsage : 8
QuotaPeakPagedPoolUsage    : 125
ReadOperationCount         : 11
ReadTransferCount          : 452
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 2
UserModeTime               : 0
VirtualSize                : 53530624
WindowsVersion             : 6.3.9600
WorkingSetSize             : 5320704
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : conhost.exe
Handles                    : 57
VM                         : 53530624
WS                         : 5320704
Path                       : C:\Windows\system32\conhost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="3832"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="3832"
Caption                    : python.exe
CommandLine                : python  -m SimpleHTTPServer
CreationClassName          : Win32_Process
CreationDate               : 20170712151820.171032-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : python.exe
ExecutablePath             : C:\Python27\python.exe
ExecutionState             :
Handle                     : 3832
HandleCount                : 162
InstallDate                :
KernelModeTime             : 468750
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : python.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 22459
OtherTransferCount         : 434276
PageFaults                 : 2794
PageFileUsage              : 5664
ParentProcessId            : 3944
PeakPageFileUsage          : 5816
PeakVirtualSize            : 88002560
PeakWorkingSetSize         : 10712
Priority                   : 8
PrivatePageCount           : 5799936
ProcessId                  : 3832
QuotaNonPagedPoolUsage     : 11
QuotaPagedPoolUsage        : 146
QuotaPeakNonPagedPoolUsage : 157
QuotaPeakPagedPoolUsage    : 146
ReadOperationCount         : 240
ReadTransferCount          : 1208439
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 1
UserModeTime               : 937500
VirtualSize                : 83390464
WindowsVersion             : 6.3.9600
WorkingSetSize             : 10915840
WriteOperationCount        : 44
WriteTransferCount         : 1051
PSComputerName             : WIN-2012-DC
ProcessName                : python.exe
Handles                    : 162
VM                         : 83390464
WS                         : 10915840
Path                       : C:\Python27\python.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="3116"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="3116"
Caption                    : firefox.exe
CommandLine                : "C:\Program Files\Mozilla Firefox\firefox.exe"
CreationClassName          : Win32_Process
CreationDate               : 20170712152444.358480-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : firefox.exe
ExecutablePath             : C:\Program Files\Mozilla Firefox\firefox.exe
ExecutionState             :
Handle                     : 3116
HandleCount                : 749
InstallDate                :
KernelModeTime             : 23750000
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : firefox.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 41297
OtherTransferCount         : 712762
PageFaults                 : 1368464
PageFileUsage              : 144784
ParentProcessId            : 1188
PeakPageFileUsage          : 180008
PeakVirtualSize            : 1768960000
PeakWorkingSetSize         : 221460
Priority                   : 8
PrivatePageCount           : 148258816
ProcessId                  : 3116
QuotaNonPagedPoolUsage     : 62
QuotaPagedPoolUsage        : 607
QuotaPeakNonPagedPoolUsage : 87
QuotaPeakPagedPoolUsage    : 731
ReadOperationCount         : 5632
ReadTransferCount          : 373181628
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 42
UserModeTime               : 124531250
VirtualSize                : 1683611648
WindowsVersion             : 6.3.9600
WorkingSetSize             : 200855552
WriteOperationCount        : 632356
WriteTransferCount         : 143084163
PSComputerName             : WIN-2012-DC
ProcessName                : firefox.exe
Handles                    : 749
VM                         : 1683611648
WS                         : 200855552
Path                       : C:\Program Files\Mozilla Firefox\firefox.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="2992"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="2992"
Caption                    : firefox.exe
CommandLine                : "C:\Program Files\Mozilla Firefox\firefox.exe" -contentproc --channel="3116.0.1418504536\2120526436" -childID 1 -isForBrowser -intPrefs 5:50|6:-1|28:1000|33:20|34:10|43:128|
                             44:10000|48:0|50:400|51:1|52:0|53:0|58:0|59:120|60:120|133:2|134:1|147:5000|157:0|159:0|170:10000|182:-1|187:128|188:10000|189:0|195:24|196:32768|198:0|199:0|207:5|211:10485
                             76|212:100|213:5000|215:600|217:1|226:1|231:0|241:60000| -boolPrefs 1:0|2:0|4:0|26:1|27:1|30:0|35:1|36:0|37:0|38:0|39:1|40:0|41:1|42:1|45:0|46:0|47:0|49:0|54:1|55:1|56:0|57:
                             1|61:1|62:1|63:0|64:1|65:1|66:0|67:1|70:0|71:0|74:1|75:1|79:1|80:1|81:0|82:0|84:0|85:0|86:1|87:0|90:0|91:1|92:1|93:1|94:1|95:1|96:0|97:0|98:1|99:0|100:0|101:0|102:1|103:1|10
                             4:0|105:1|106:1|107:0|108:0|109:1|110:1|111:1|112:0|113:1|114:1|115:1|116:1|117:1|118:1|119:1|120:1|122:0|123:0|124:0|125:1|126:0|127:1|131:1|132:1|135:1|136:0|141:0|146:0|1
                             49:1|152:1|154:1|158:0|161:1|164:1|165:1|171:0|172:0|173:1|175:0|181:0|183:1|184:0|185:0|186:0|193:0|194:0|197:1|200:0|202:0|204:1|205:0|210:0|214:1|219:0|220:0|221:0|222:1|
                             224:1|225:1|228:0|233:0|234:0|235:1|236:1|237:0|238:1|239:1|240:0|242:0|243:0|245:0|253:1|254:1|255:0|256:0|257:0| -stringPrefs "3:7;release|174:3;1.0|191:332; ¼½¾!???:?????
                             %????????       ???????-’·?????????‹›?/???????????????/:?????????????????? ???????????????????./???????|192:8;moderate|227:38;{d130b7e4-5618-427c-891a-ee8a0888c2a8}|"
                             -greomni "C:\Program Files\Mozilla Firefox\omni.ja" -appomni "C:\Program Files\Mozilla Firefox\browser\omni.ja" -appdir "C:\Program Files\Mozilla Firefox\browser"  3116
                             "\\.\pipe\gecko-crash-server-pipe.3116" tab
CreationClassName          : Win32_Process
CreationDate               : 20170712152446.155540-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : firefox.exe
ExecutablePath             : C:\Program Files\Mozilla Firefox\firefox.exe
ExecutionState             :
Handle                     : 2992
HandleCount                : 286
InstallDate                :
KernelModeTime             : 2812500
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : firefox.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 976
OtherTransferCount         : 12866
PageFaults                 : 37633
PageFileUsage              : 34096
ParentProcessId            : 3116
PeakPageFileUsage          : 44108
PeakVirtualSize            : 1400070144
PeakWorkingSetSize         : 82424
Priority                   : 8
PrivatePageCount           : 34914304
ProcessId                  : 2992
QuotaNonPagedPoolUsage     : 30
QuotaPagedPoolUsage        : 454
QuotaPeakNonPagedPoolUsage : 32
QuotaPeakPagedPoolUsage    : 474
ReadOperationCount         : 3966
ReadTransferCount          : 70438261
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 17
UserModeTime               : 6875000
VirtualSize                : 1378304000
WindowsVersion             : 6.3.9600
WorkingSetSize             : 72314880
WriteOperationCount        : 2307
WriteTransferCount         : 487820
PSComputerName             : WIN-2012-DC
ProcessName                : firefox.exe
Handles                    : 286
VM                         : 1378304000
WS                         : 72314880
Path                       : C:\Program Files\Mozilla Firefox\firefox.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="956"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="956"
Caption                    : notepad.exe
CommandLine                : "C:\Windows\system32\NOTEPAD.EXE" C:\Users\Administrator\Desktop\log.txt
CreationClassName          : Win32_Process
CreationDate               : 20170712153213.828260-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : notepad.exe
ExecutablePath             : C:\Windows\system32\NOTEPAD.EXE
ExecutionState             :
Handle                     : 956
HandleCount                : 95
InstallDate                :
KernelModeTime             : 937500
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : notepad.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 207
OtherTransferCount         : 1744
PageFaults                 : 4672
PageFileUsage              : 3024
ParentProcessId            : 1188
PeakPageFileUsage          : 4012
PeakVirtualSize            : 151597056
PeakWorkingSetSize         : 10756
Priority                   : 8
PrivatePageCount           : 3096576
ProcessId                  : 956
QuotaNonPagedPoolUsage     : 9
QuotaPagedPoolUsage        : 278
QuotaPeakNonPagedPoolUsage : 10
QuotaPeakPagedPoolUsage    : 289
ReadOperationCount         : 1
ReadTransferCount          : 60
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 1
UserModeTime               : 625000
VirtualSize                : 148074496
WindowsVersion             : 6.3.9600
WorkingSetSize             : 10457088
WriteOperationCount        : 10
WriteTransferCount         : 672390
PSComputerName             : WIN-2012-DC
ProcessName                : notepad.exe
Handles                    : 95
VM                         : 148074496
WS                         : 10457088
Path                       : C:\Windows\system32\NOTEPAD.EXE

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="3416"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="3416"
Caption                    : powershell.exe
CommandLine                : "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
CreationClassName          : Win32_Process
CreationDate               : 20170712164403.172486-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : powershell.exe
ExecutablePath             : C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
ExecutionState             :
Handle                     : 3416
HandleCount                : 448
InstallDate                :
KernelModeTime             : 23281250
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : powershell.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 99601
OtherTransferCount         : 6543278
PageFaults                 : 298573
PageFileUsage              : 112212
ParentProcessId            : 1188
PeakPageFileUsage          : 114860
PeakVirtualSize            : 659030016
PeakWorkingSetSize         : 122112
Priority                   : 8
PrivatePageCount           : 114905088
ProcessId                  : 3416
QuotaNonPagedPoolUsage     : 35
QuotaPagedPoolUsage        : 431
QuotaPeakNonPagedPoolUsage : 40
QuotaPeakPagedPoolUsage    : 436
ReadOperationCount         : 1024
ReadTransferCount          : 3479940
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 10
UserModeTime               : 164531250
VirtualSize                : 657010688
WindowsVersion             : 6.3.9600
WorkingSetSize             : 122355712
WriteOperationCount        : 3
WriteTransferCount         : 5430
PSComputerName             : WIN-2012-DC
ProcessName                : powershell.exe
Handles                    : 448
VM                         : 657010688
WS                         : 122355712
Path                       : C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1928"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="1928"
Caption                    : conhost.exe
CommandLine                : \??\C:\Windows\system32\conhost.exe 0x4
CreationClassName          : Win32_Process
CreationDate               : 20170712164403.172486-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : conhost.exe
ExecutablePath             : C:\Windows\system32\conhost.exe
ExecutionState             :
Handle                     : 1928
HandleCount                : 58
InstallDate                :
KernelModeTime             : 42812500
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : conhost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 71097
OtherTransferCount         : 4783207
PageFaults                 : 5369
PageFileUsage              : 7316
ParentProcessId            : 3416
PeakPageFileUsage          : 11276
PeakVirtualSize            : 88776704
PeakWorkingSetSize         : 18428
Priority                   : 8
PrivatePageCount           : 7491584
ProcessId                  : 1928
QuotaNonPagedPoolUsage     : 7
QuotaPagedPoolUsage        : 142
QuotaPeakNonPagedPoolUsage : 8
QuotaPeakPagedPoolUsage    : 161
ReadOperationCount         : 24
ReadTransferCount          : 816
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 2
UserModeTime               : 2812500
VirtualSize                : 78757888
WindowsVersion             : 6.3.9600
WorkingSetSize             : 16302080
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : conhost.exe
Handles                    : 58
VM                         : 78757888
WS                         : 16302080
Path                       : C:\Windows\system32\conhost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="840"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="840"
Caption                    : WmiPrvSE.exe
CommandLine                : C:\Windows\system32\wbem\wmiprvse.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712165108.172589-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : WmiPrvSE.exe
ExecutablePath             : C:\Windows\system32\wbem\wmiprvse.exe
ExecutionState             :
Handle                     : 840
HandleCount                : 129
InstallDate                :
KernelModeTime             : 312500
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : WmiPrvSE.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 1184
OtherTransferCount         : 244
PageFaults                 : 4433
PageFileUsage              : 2152
ParentProcessId            : 572
PeakPageFileUsage          : 2624
PeakVirtualSize            : 35962880
PeakWorkingSetSize         : 5924
Priority                   : 8
PrivatePageCount           : 2203648
ProcessId                  : 840
QuotaNonPagedPoolUsage     : 9
QuotaPagedPoolUsage        : 62
QuotaPeakNonPagedPoolUsage : 11
QuotaPeakPagedPoolUsage    : 64
ReadOperationCount         : 0
ReadTransferCount          : 0
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 7
UserModeTime               : 156250
VirtualSize                : 34516992
WindowsVersion             : 6.3.9600
WorkingSetSize             : 5709824
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : WmiPrvSE.exe
Handles                    : 129
VM                         : 34516992
WS                         : 5709824
Path                       : C:\Windows\system32\wbem\wmiprvse.exe

PS C:\Users\Administrator>
```

- Using ```Get-WmiObject``` - ```Remote```

```
PS C:\Users\Administrator> Get-WmiObject -Class Win32_Process -ComputerName JOHN-PC -Credential John-PC\John

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="0"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="0"
Caption                    : System Idle Process
CommandLine                :
CreationClassName          : Win32_Process
CreationDate               :
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : System Idle Process
ExecutablePath             :
ExecutionState             :
Handle                     : 0
HandleCount                : 0
InstallDate                :
KernelModeTime             : 203835200624
MaximumWorkingSetSize      :
MinimumWorkingSetSize      :
Name                       : System Idle Process
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 0
OtherTransferCount         : 0
PageFaults                 : 0
PageFileUsage              : 0
ParentProcessId            : 0
PeakPageFileUsage          : 0
PeakVirtualSize            : 0
PeakWorkingSetSize         : 0
Priority                   : 0
PrivatePageCount           : 0
ProcessId                  : 0
QuotaNonPagedPoolUsage     : 0
QuotaPagedPoolUsage        : 0
QuotaPeakNonPagedPoolUsage : 0
QuotaPeakPagedPoolUsage    : 0
ReadOperationCount         : 0
ReadTransferCount          : 0
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 1
UserModeTime               : 0
VirtualSize                : 0
WindowsVersion             : 6.1.7600
WorkingSetSize             : 12288
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : JOHN-PC
ProcessName                : System Idle Process
Handles                    : 0
VM                         : 0
WS                         : 12288
Path                       :

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="4"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="4"
Caption                    : System
CommandLine                :
CreationClassName          : Win32_Process
CreationDate               : 20170712122327.686019-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : System
ExecutablePath             :
ExecutionState             :
Handle                     : 4
HandleCount                : 566
InstallDate                :
KernelModeTime             : 96638960
MaximumWorkingSetSize      :
MinimumWorkingSetSize      :
Name                       : System
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 7608
OtherTransferCount         : 617853
PageFaults                 : 10151
PageFileUsage              : 44
ParentProcessId            : 0
PeakPageFileUsage          : 180
PeakVirtualSize            : 6365184
PeakWorkingSetSize         : 4840
Priority                   : 8
PrivatePageCount           : 45056
ProcessId                  : 4
QuotaNonPagedPoolUsage     : 0
QuotaPagedPoolUsage        : 0
QuotaPeakNonPagedPoolUsage : 0
QuotaPeakPagedPoolUsage    : 0
ReadOperationCount         : 1468
ReadTransferCount          : 26788136
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 85
UserModeTime               : 0
VirtualSize                : 1966080
WindowsVersion             : 6.1.7600
WorkingSetSize             : 606208
WriteOperationCount        : 6499
WriteTransferCount         : 59286136
PSComputerName             : JOHN-PC
ProcessName                : System
Handles                    : 566
VM                         : 1966080
WS                         : 606208
Path                       :

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="272"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="272"
Caption                    : smss.exe
CommandLine                : \SystemRoot\System32\smss.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712122327.696033-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : smss.exe
ExecutablePath             :
ExecutionState             :
Handle                     : 272
HandleCount                : 29
InstallDate                :
KernelModeTime             : 600864
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : smss.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 318
OtherTransferCount         : 8646
PageFaults                 : 293
PageFileUsage              : 216
ParentProcessId            : 4
PeakPageFileUsage          : 268
PeakVirtualSize            : 17027072
PeakWorkingSetSize         : 720
Priority                   : 11
PrivatePageCount           : 221184
ProcessId                  : 272
QuotaNonPagedPoolUsage     : 1
QuotaPagedPoolUsage        : 8
QuotaPeakNonPagedPoolUsage : 5
QuotaPeakPagedPoolUsage    : 20
ReadOperationCount         : 12
ReadTransferCount          : 29214
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 2
UserModeTime               : 0
VirtualSize                : 4145152
WindowsVersion             : 6.1.7600
WorkingSetSize             : 532480
WriteOperationCount        : 5
WriteTransferCount         : 20
PSComputerName             : JOHN-PC
ProcessName                : smss.exe
Handles                    : 29
VM                         : 4145152
WS                         : 532480
Path                       :

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="348"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="348"
Caption                    : csrss.exe
CommandLine                : %SystemRoot%\system32\csrss.exe ObjectDirectory=\Windows SharedSection=1024,12288,512 Windows=On SubSystemType=Windows ServerDll=basesrv,1
                             ServerDll=winsrv:UserServerDllInitialization,3 ServerDll=winsrv:ConServerDllInitialization,2 ServerDll=sxssrv,4 ProfileControl=Off MaxRequestThreads=16
CreationClassName          : Win32_Process
CreationDate               : 20170712122328.577300-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : csrss.exe
ExecutablePath             : C:\Windows\system32\csrss.exe
ExecutionState             :
Handle                     : 348
HandleCount                : 370
InstallDate                :
KernelModeTime             : 1502160
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : csrss.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 1996
OtherTransferCount         : 93042
PageFaults                 : 1636
PageFileUsage              : 1116
ParentProcessId            : 340
PeakPageFileUsage          : 1116
PeakVirtualSize            : 34533376
PeakWorkingSetSize         : 2688
Priority                   : 13
PrivatePageCount           : 1142784
ProcessId                  : 348
QuotaNonPagedPoolUsage     : 5
QuotaPagedPoolUsage        : 56
QuotaPeakNonPagedPoolUsage : 9
QuotaPeakPagedPoolUsage    : 58
ReadOperationCount         : 182
ReadTransferCount          : 144624
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 8
UserModeTime               : 400576
VirtualSize                : 34271232
WindowsVersion             : 6.1.7600
WorkingSetSize             : 2179072
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : JOHN-PC
ProcessName                : csrss.exe
Handles                    : 370
VM                         : 34271232
WS                         : 2179072
Path                       : C:\Windows\system32\csrss.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="396"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="396"
Caption                    : wininit.exe
CommandLine                : wininit.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712122328.627372-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : wininit.exe
ExecutablePath             : C:\Windows\system32\wininit.exe
ExecutionState             :
Handle                     : 396
HandleCount                : 74
InstallDate                :
KernelModeTime             : 801152
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : wininit.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 719
OtherTransferCount         : 3906
PageFaults                 : 1051
PageFileUsage              : 784
ParentProcessId            : 340
PeakPageFileUsage          : 928
PeakVirtualSize            : 49909760
PeakWorkingSetSize         : 3208
Priority                   : 13
PrivatePageCount           : 802816
ProcessId                  : 396
QuotaNonPagedPoolUsage     : 5
QuotaPagedPoolUsage        : 42
QuotaPeakNonPagedPoolUsage : 7
QuotaPeakPagedPoolUsage    : 51
ReadOperationCount         : 1
ReadTransferCount          : 5632
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 3
UserModeTime               : 0
VirtualSize                : 34000896
WindowsVersion             : 6.1.7600
WorkingSetSize             : 2568192
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : JOHN-PC
ProcessName                : wininit.exe
Handles                    : 74
VM                         : 34000896
WS                         : 2568192
Path                       : C:\Windows\system32\wininit.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="404"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="404"
Caption                    : csrss.exe
CommandLine                : %SystemRoot%\system32\csrss.exe ObjectDirectory=\Windows SharedSection=1024,12288,512 Windows=On SubSystemType=Windows ServerDll=basesrv,1
                             ServerDll=winsrv:UserServerDllInitialization,3 ServerDll=winsrv:ConServerDllInitialization,2 ServerDll=sxssrv,4 ProfileControl=Off MaxRequestThreads=16
CreationClassName          : Win32_Process
CreationDate               : 20170712122328.627372-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : csrss.exe
ExecutablePath             : C:\Windows\system32\csrss.exe
ExecutionState             :
Handle                     : 404
HandleCount                : 221
InstallDate                :
KernelModeTime             : 5307632
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : csrss.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 2622
OtherTransferCount         : 33872
PageFaults                 : 20109
PageFileUsage              : 1272
ParentProcessId            : 388
PeakPageFileUsage          : 1404
PeakVirtualSize            : 239112192
PeakWorkingSetSize         : 11168
Priority                   : 13
PrivatePageCount           : 1302528
ProcessId                  : 404
QuotaNonPagedPoolUsage     : 9
QuotaPagedPoolUsage        : 115
QuotaPeakNonPagedPoolUsage : 14
QuotaPeakPagedPoolUsage    : 239
ReadOperationCount         : 9108
ReadTransferCount          : 482433
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 9
UserModeTime               : 1301872
VirtualSize                : 107212800
WindowsVersion             : 6.1.7600
WorkingSetSize             : 2985984
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : JOHN-PC
ProcessName                : csrss.exe
Handles                    : 221
VM                         : 107212800
WS                         : 2985984
Path                       : C:\Windows\system32\csrss.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="444"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="444"
Caption                    : winlogon.exe
CommandLine                : winlogon.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712122328.707488-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : winlogon.exe
ExecutablePath             : C:\Windows\system32\winlogon.exe
ExecutionState             :
Handle                     : 444
HandleCount                : 112
InstallDate                :
KernelModeTime             : 1301872
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : winlogon.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 1197
OtherTransferCount         : 6288
PageFaults                 : 3096
PageFileUsage              : 1492
ParentProcessId            : 388
PeakPageFileUsage          : 2776
PeakVirtualSize            : 51965952
PeakWorkingSetSize         : 6028
Priority                   : 13
PrivatePageCount           : 1527808
ProcessId                  : 444
QuotaNonPagedPoolUsage     : 5
QuotaPagedPoolUsage        : 40
QuotaPeakNonPagedPoolUsage : 11
QuotaPeakPagedPoolUsage    : 52
ReadOperationCount         : 3
ReadTransferCount          : 5776
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 3
UserModeTime               : 600864
VirtualSize                : 40443904
WindowsVersion             : 6.1.7600
WorkingSetSize             : 3280896
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : JOHN-PC
ProcessName                : winlogon.exe
Handles                    : 112
VM                         : 40443904
WS                         : 3280896
Path                       : C:\Windows\system32\winlogon.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="488"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="488"
Caption                    : services.exe
CommandLine                : C:\Windows\system32\services.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712122328.777588-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : services.exe
ExecutablePath             : C:\Windows\system32\services.exe
ExecutionState             :
Handle                     : 488
HandleCount                : 194
InstallDate                :
KernelModeTime             : 8412096
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : services.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 2999
OtherTransferCount         : 420188
PageFaults                 : 6561
PageFileUsage              : 4460
ParentProcessId            : 396
PeakPageFileUsage          : 7296
PeakVirtualSize            : 40091648
PeakWorkingSetSize         : 9768
Priority                   : 9
PrivatePageCount           : 4567040
ProcessId                  : 488
QuotaNonPagedPoolUsage     : 8
QuotaPagedPoolUsage        : 27
QuotaPeakNonPagedPoolUsage : 16
QuotaPeakPagedPoolUsage    : 32
ReadOperationCount         : 117
ReadTransferCount          : 500876
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 8
UserModeTime               : 1702448
VirtualSize                : 35315712
WindowsVersion             : 6.1.7600
WorkingSetSize             : 4816896
WriteOperationCount        : 973
WriteTransferCount         : 3821996
PSComputerName             : JOHN-PC
ProcessName                : services.exe
Handles                    : 194
VM                         : 35315712
WS                         : 4816896
Path                       : C:\Windows\system32\services.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="496"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="496"
Caption                    : lsass.exe
CommandLine                : C:\Windows\system32\lsass.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712122328.807632-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : lsass.exe
ExecutablePath             : C:\Windows\system32\lsass.exe
ExecutionState             :
Handle                     : 496
HandleCount                : 800
InstallDate                :
KernelModeTime             : 8311952
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : lsass.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 5618
OtherTransferCount         : 583732
PageFaults                 : 3438
PageFileUsage              : 3120
ParentProcessId            : 396
PeakPageFileUsage          : 3120
PeakVirtualSize            : 34959360
PeakWorkingSetSize         : 7556
Priority                   : 9
PrivatePageCount           : 3194880
ProcessId                  : 496
QuotaNonPagedPoolUsage     : 15
QuotaPagedPoolUsage        : 50
QuotaPeakNonPagedPoolUsage : 16
QuotaPeakPagedPoolUsage    : 50
ReadOperationCount         : 1713
ReadTransferCount          : 109701
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 11
UserModeTime               : 8011520
VirtualSize                : 34435072
WindowsVersion             : 6.1.7600
WorkingSetSize             : 7110656
WriteOperationCount        : 1470
WriteTransferCount         : 138645
PSComputerName             : JOHN-PC
ProcessName                : lsass.exe
Handles                    : 800
VM                         : 34435072
WS                         : 7110656
Path                       : C:\Windows\system32\lsass.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="504"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="504"
Caption                    : lsm.exe
CommandLine                : C:\Windows\system32\lsm.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712122328.807632-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : lsm.exe
ExecutablePath             : C:\Windows\system32\lsm.exe
ExecutionState             :
Handle                     : 504
HandleCount                : 200
InstallDate                :
KernelModeTime             : 200288
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : lsm.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 133
OtherTransferCount         : 560
PageFaults                 : 4457
PageFileUsage              : 1648
ParentProcessId            : 396
PeakPageFileUsage          : 1648
PeakVirtualSize            : 24059904
PeakWorkingSetSize         : 3924
Priority                   : 8
PrivatePageCount           : 1687552
ProcessId                  : 504
QuotaNonPagedPoolUsage     : 5
QuotaPagedPoolUsage        : 25
QuotaPeakNonPagedPoolUsage : 6
QuotaPeakPagedPoolUsage    : 25
ReadOperationCount         : 0
ReadTransferCount          : 0
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 11
UserModeTime               : 901296
VirtualSize                : 23797760
WindowsVersion             : 6.1.7600
WorkingSetSize             : 3575808
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : JOHN-PC
ProcessName                : lsm.exe
Handles                    : 200
VM                         : 23797760
WS                         : 3575808
Path                       : C:\Windows\system32\lsm.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="608"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="608"
Caption                    : svchost.exe
CommandLine                : C:\Windows\system32\svchost.exe -k DcomLaunch
CreationClassName          : Win32_Process
CreationDate               : 20170712122329.378452-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : svchost.exe
ExecutablePath             : C:\Windows\system32\svchost.exe
ExecutionState             :
Handle                     : 608
HandleCount                : 353
InstallDate                :
KernelModeTime             : 8111664
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 29613
OtherTransferCount         : 530904
PageFaults                 : 67578
PageFileUsage              : 3020
ParentProcessId            : 488
PeakPageFileUsage          : 3020
PeakVirtualSize            : 40407040
PeakWorkingSetSize         : 6016
Priority                   : 8
PrivatePageCount           : 3092480
ProcessId                  : 608
QuotaNonPagedPoolUsage     : 7
QuotaPagedPoolUsage        : 36
QuotaPeakNonPagedPoolUsage : 13
QuotaPeakPagedPoolUsage    : 39
ReadOperationCount         : 0
ReadTransferCount          : 0
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 10
UserModeTime               : 3404896
VirtualSize                : 36839424
WindowsVersion             : 6.1.7600
WorkingSetSize             : 6021120
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : JOHN-PC
ProcessName                : svchost.exe
Handles                    : 353
VM                         : 36839424
WS                         : 6021120
Path                       : C:\Windows\system32\svchost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="668"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="668"
Caption                    : VBoxService.exe
CommandLine                : C:\Windows\System32\VBoxService.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712122329.568726-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : VBoxService.exe
ExecutablePath             : C:\Windows\System32\VBoxService.exe
ExecutionState             :
Handle                     : 668
HandleCount                : 118
InstallDate                :
KernelModeTime             : 3605184
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : VBoxService.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 174313
OtherTransferCount         : 4164921
PageFaults                 : 48385
PageFileUsage              : 2344
ParentProcessId            : 488
PeakPageFileUsage          : 2352
PeakVirtualSize            : 46714880
PeakWorkingSetSize         : 3876
Priority                   : 8
PrivatePageCount           : 2400256
ProcessId                  : 668
QuotaNonPagedPoolUsage     : 5
QuotaPagedPoolUsage        : 36
QuotaPeakNonPagedPoolUsage : 6
QuotaPeakPagedPoolUsage    : 37
ReadOperationCount         : 4047
ReadTransferCount          : 16188
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 12
UserModeTime               : 1201728
VirtualSize                : 46706688
WindowsVersion             : 6.1.7600
WorkingSetSize             : 3919872
WriteOperationCount        : 4047
WriteTransferCount         : 64752
PSComputerName             : JOHN-PC
ProcessName                : VBoxService.exe
Handles                    : 118
VM                         : 46706688
WS                         : 3919872
Path                       : C:\Windows\System32\VBoxService.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="720"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="720"
Caption                    : svchost.exe
CommandLine                : C:\Windows\system32\svchost.exe -k RPCSS
CreationClassName          : Win32_Process
CreationDate               : 20170712122329.739972-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : svchost.exe
ExecutablePath             : C:\Windows\system32\svchost.exe
ExecutionState             :
Handle                     : 720
HandleCount                : 273
InstallDate                :
KernelModeTime             : 3605184
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 322
OtherTransferCount         : 15508
PageFaults                 : 3747
PageFileUsage              : 3140
ParentProcessId            : 488
PeakPageFileUsage          : 3140
PeakVirtualSize            : 29499392
PeakWorkingSetSize         : 5388
Priority                   : 8
PrivatePageCount           : 3215360
ProcessId                  : 720
QuotaNonPagedPoolUsage     : 10
QuotaPagedPoolUsage        : 40
QuotaPeakNonPagedPoolUsage : 10
QuotaPeakPagedPoolUsage    : 41
ReadOperationCount         : 0
ReadTransferCount          : 0
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 8
UserModeTime               : 6909936
VirtualSize                : 29499392
WindowsVersion             : 6.1.7600
WorkingSetSize             : 5517312
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : JOHN-PC
ProcessName                : svchost.exe
Handles                    : 273
VM                         : 29499392
WS                         : 5517312
Path                       : C:\Windows\system32\svchost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="772"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="772"
Caption                    : svchost.exe
CommandLine                : C:\Windows\System32\svchost.exe -k LocalServiceNetworkRestricted
CreationClassName          : Win32_Process
CreationDate               : 20170712122329.795051-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : svchost.exe
ExecutablePath             : C:\Windows\System32\svchost.exe
ExecutionState             :
Handle                     : 772
HandleCount                : 564
InstallDate                :
KernelModeTime             : 6208928
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 3507
OtherTransferCount         : 95164
PageFaults                 : 8131
PageFileUsage              : 13912
ParentProcessId            : 488
PeakPageFileUsage          : 14620
PeakVirtualSize            : 84037632
PeakWorkingSetSize         : 12680
Priority                   : 8
PrivatePageCount           : 14245888
ProcessId                  : 772
QuotaNonPagedPoolUsage     : 13
QuotaPagedPoolUsage        : 72
QuotaPeakNonPagedPoolUsage : 16
QuotaPeakPagedPoolUsage    : 76
ReadOperationCount         : 269
ReadTransferCount          : 5796459
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 21
UserModeTime               : 3805472
VirtualSize                : 79962112
WindowsVersion             : 6.1.7600
WorkingSetSize             : 10862592
WriteOperationCount        : 629
WriteTransferCount         : 1781499
PSComputerName             : JOHN-PC
ProcessName                : svchost.exe
Handles                    : 564
VM                         : 79962112
WS                         : 10862592
Path                       : C:\Windows\System32\svchost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="900"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="900"
Caption                    : svchost.exe
CommandLine                : C:\Windows\System32\svchost.exe -k LocalSystemNetworkRestricted
CreationClassName          : Win32_Process
CreationDate               : 20170712122330.290762-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : svchost.exe
ExecutablePath             : C:\Windows\System32\svchost.exe
ExecutionState             :
Handle                     : 900
HandleCount                : 502
InstallDate                :
KernelModeTime             : 56781648
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 157709
OtherTransferCount         : 6589070
PageFaults                 : 53228
PageFileUsage              : 31136
ParentProcessId            : 488
PeakPageFileUsage          : 36328
PeakVirtualSize            : 112607232
PeakWorkingSetSize         : 39640
Priority                   : 8
PrivatePageCount           : 31883264
ProcessId                  : 900
QuotaNonPagedPoolUsage     : 13
QuotaPagedPoolUsage        : 79
QuotaPeakNonPagedPoolUsage : 15
QuotaPeakPagedPoolUsage    : 82
ReadOperationCount         : 777
ReadTransferCount          : 16290731
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 24
UserModeTime               : 79714624
VirtualSize                : 107683840
WindowsVersion             : 6.1.7600
WorkingSetSize             : 32575488
WriteOperationCount        : 17711
WriteTransferCount         : 6508584
PSComputerName             : JOHN-PC
ProcessName                : svchost.exe
Handles                    : 502
VM                         : 107683840
WS                         : 32575488
Path                       : C:\Windows\System32\svchost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="940"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="940"
Caption                    : svchost.exe
CommandLine                : C:\Windows\system32\svchost.exe -k netsvcs
CreationClassName          : Win32_Process
CreationDate               : 20170712122330.356857-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : svchost.exe
ExecutablePath             : C:\Windows\system32\svchost.exe
ExecutionState             :
Handle                     : 940
HandleCount                : 1401
InstallDate                :
KernelModeTime             : 147912688
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 876271
OtherTransferCount         : 249422697
PageFaults                 : 278297
PageFileUsage              : 24528
ParentProcessId            : 488
PeakPageFileUsage          : 105120
PeakVirtualSize            : 234819584
PeakWorkingSetSize         : 90176
Priority                   : 8
PrivatePageCount           : 25116672
ProcessId                  : 940
QuotaNonPagedPoolUsage     : 35
QuotaPagedPoolUsage        : 132
QuotaPeakNonPagedPoolUsage : 140
QuotaPeakPagedPoolUsage    : 173
ReadOperationCount         : 150899
ReadTransferCount          : 614189472
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 48
UserModeTime               : 108055376
VirtualSize                : 164155392
WindowsVersion             : 6.1.7600
WorkingSetSize             : 21028864
WriteOperationCount        : 7077
WriteTransferCount         : 393943192
PSComputerName             : JOHN-PC
ProcessName                : svchost.exe
Handles                    : 1401
VM                         : 164155392
WS                         : 21028864
Path                       : C:\Windows\system32\svchost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1108"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="1108"
Caption                    : svchost.exe
CommandLine                : C:\Windows\system32\svchost.exe -k LocalService
CreationClassName          : Win32_Process
CreationDate               : 20170712122330.665299-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : svchost.exe
ExecutablePath             : C:\Windows\system32\svchost.exe
ExecutionState             :
Handle                     : 1108
HandleCount                : 498
InstallDate                :
KernelModeTime             : 5708208
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 13888
OtherTransferCount         : 523968
PageFaults                 : 7285
PageFileUsage              : 6252
ParentProcessId            : 488
PeakPageFileUsage          : 6940
PeakVirtualSize            : 64761856
PeakWorkingSetSize         : 10784
Priority                   : 8
PrivatePageCount           : 6402048
ProcessId                  : 1108
QuotaNonPagedPoolUsage     : 19
QuotaPagedPoolUsage        : 61
QuotaPeakNonPagedPoolUsage : 24
QuotaPeakPagedPoolUsage    : 66
ReadOperationCount         : 310
ReadTransferCount          : 183135
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 21
UserModeTime               : 4907056
VirtualSize                : 55312384
WindowsVersion             : 6.1.7600
WorkingSetSize             : 9084928
WriteOperationCount        : 42
WriteTransferCount         : 2452
PSComputerName             : JOHN-PC
ProcessName                : svchost.exe
Handles                    : 498
VM                         : 55312384
WS                         : 9084928
Path                       : C:\Windows\system32\svchost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1240"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="1240"
Caption                    : svchost.exe
CommandLine                : C:\Windows\system32\svchost.exe -k NetworkService
CreationClassName          : Win32_Process
CreationDate               : 20170712122330.991419-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : svchost.exe
ExecutablePath             : C:\Windows\system32\svchost.exe
ExecutionState             :
Handle                     : 1240
HandleCount                : 594
InstallDate                :
KernelModeTime             : 6809792
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 53068
OtherTransferCount         : 2086541
PageFaults                 : 9584
PageFileUsage              : 11972
ParentProcessId            : 488
PeakPageFileUsage          : 12872
PeakVirtualSize            : 84770816
PeakWorkingSetSize         : 11320
Priority                   : 8
PrivatePageCount           : 12259328
ProcessId                  : 1240
QuotaNonPagedPoolUsage     : 20
QuotaPagedPoolUsage        : 74
QuotaPeakNonPagedPoolUsage : 25
QuotaPeakPagedPoolUsage    : 75
ReadOperationCount         : 284
ReadTransferCount          : 739919
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 24
UserModeTime               : 2103024
VirtualSize                : 79527936
WindowsVersion             : 6.1.7600
WorkingSetSize             : 10477568
WriteOperationCount        : 541
WriteTransferCount         : 1281099
PSComputerName             : JOHN-PC
ProcessName                : svchost.exe
Handles                    : 594
VM                         : 79527936
WS                         : 10477568
Path                       : C:\Windows\system32\svchost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1332"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="1332"
Caption                    : spoolsv.exe
CommandLine                : C:\Windows\System32\spoolsv.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712122331.205295-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : spoolsv.exe
ExecutablePath             : C:\Windows\System32\spoolsv.exe
ExecutionState             :
Handle                     : 1332
HandleCount                : 280
InstallDate                :
KernelModeTime             : 400576
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : spoolsv.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 782
OtherTransferCount         : 11299
PageFaults                 : 2916
PageFileUsage              : 4324
ParentProcessId            : 488
PeakPageFileUsage          : 4564
PeakVirtualSize            : 61775872
PeakWorkingSetSize         : 8532
Priority                   : 8
PrivatePageCount           : 4427776
ProcessId                  : 1332
QuotaNonPagedPoolUsage     : 10
QuotaPagedPoolUsage        : 56
QuotaPeakNonPagedPoolUsage : 10
QuotaPeakPagedPoolUsage    : 56
ReadOperationCount         : 4
ReadTransferCount          : 1225
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 12
UserModeTime               : 100144
VirtualSize                : 60256256
WindowsVersion             : 6.1.7600
WorkingSetSize             : 5652480
WriteOperationCount        : 2
WriteTransferCount         : 232
PSComputerName             : JOHN-PC
ProcessName                : spoolsv.exe
Handles                    : 280
VM                         : 60256256
WS                         : 5652480
Path                       : C:\Windows\System32\spoolsv.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1368"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="1368"
Caption                    : svchost.exe
CommandLine                : C:\Windows\system32\svchost.exe -k LocalServiceNoNetwork
CreationClassName          : Win32_Process
CreationDate               : 20170712122331.351993-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : svchost.exe
ExecutablePath             : C:\Windows\system32\svchost.exe
ExecutionState             :
Handle                     : 1368
HandleCount                : 308
InstallDate                :
KernelModeTime             : 3004320
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 69575
OtherTransferCount         : 1630938
PageFaults                 : 19463
PageFileUsage              : 8512
ParentProcessId            : 488
PeakPageFileUsage          : 28608
PeakVirtualSize            : 65683456
PeakWorkingSetSize         : 26852
Priority                   : 8
PrivatePageCount           : 8716288
ProcessId                  : 1368
QuotaNonPagedPoolUsage     : 25
QuotaPagedPoolUsage        : 36
QuotaPeakNonPagedPoolUsage : 27
QuotaPeakPagedPoolUsage    : 40
ReadOperationCount         : 509
ReadTransferCount          : 43006740
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 18
UserModeTime               : 5307632
VirtualSize                : 47792128
WindowsVersion             : 6.1.7600
WorkingSetSize             : 7675904
WriteOperationCount        : 10
WriteTransferCount         : 424892
PSComputerName             : JOHN-PC
ProcessName                : svchost.exe
Handles                    : 308
VM                         : 47792128
WS                         : 7675904
Path                       : C:\Windows\system32\svchost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1504"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="1504"
Caption                    : svchost.exe
CommandLine                : C:\Windows\system32\svchost.exe -k LocalServiceAndNoImpersonation
CreationClassName          : Win32_Process
CreationDate               : 20170712122331.467871-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : svchost.exe
ExecutablePath             : C:\Windows\system32\svchost.exe
ExecutionState             :
Handle                     : 1504
HandleCount                : 303
InstallDate                :
KernelModeTime             : 2904176
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 55150
OtherTransferCount         : 1627911
PageFaults                 : 5999
PageFileUsage              : 4296
ParentProcessId            : 488
PeakPageFileUsage          : 4932
PeakVirtualSize            : 70107136
PeakWorkingSetSize         : 8540
Priority                   : 8
PrivatePageCount           : 4399104
ProcessId                  : 1504
QuotaNonPagedPoolUsage     : 15
QuotaPagedPoolUsage        : 61
QuotaPeakNonPagedPoolUsage : 25
QuotaPeakPagedPoolUsage    : 62
ReadOperationCount         : 1
ReadTransferCount          : 92
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 20
UserModeTime               : 2303312
VirtualSize                : 66961408
WindowsVersion             : 6.1.7600
WorkingSetSize             : 6828032
WriteOperationCount        : 1
WriteTransferCount         : 116
PSComputerName             : JOHN-PC
ProcessName                : svchost.exe
Handles                    : 303
VM                         : 66961408
WS                         : 6828032
Path                       : C:\Windows\system32\svchost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1896"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="1896"
Caption                    : svchost.exe
CommandLine                : C:\Windows\system32\svchost.exe -k NetworkServiceNetworkRestricted
CreationClassName          : Win32_Process
CreationDate               : 20170712122332.174175-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : svchost.exe
ExecutablePath             : C:\Windows\system32\svchost.exe
ExecutionState             :
Handle                     : 1896
HandleCount                : 94
InstallDate                :
KernelModeTime             : 701008
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 4399
OtherTransferCount         : 97894
PageFaults                 : 1276
PageFileUsage              : 1104
ParentProcessId            : 488
PeakPageFileUsage          : 1132
PeakVirtualSize            : 26558464
PeakWorkingSetSize         : 3892
Priority                   : 8
PrivatePageCount           : 1130496
ProcessId                  : 1896
QuotaNonPagedPoolUsage     : 7
QuotaPagedPoolUsage        : 30
QuotaPeakNonPagedPoolUsage : 9
QuotaPeakPagedPoolUsage    : 30
ReadOperationCount         : 0
ReadTransferCount          : 0
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 5
UserModeTime               : 600864
VirtualSize                : 26292224
WindowsVersion             : 6.1.7600
WorkingSetSize             : 3489792
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : JOHN-PC
ProcessName                : svchost.exe
Handles                    : 94
VM                         : 26292224
WS                         : 3489792
Path                       : C:\Windows\system32\svchost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1668"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="1668"
Caption                    : svchost.exe
CommandLine                : C:\Windows\System32\svchost.exe -k secsvcs
CreationClassName          : Win32_Process
CreationDate               : 20170712122344.727197-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : svchost.exe
ExecutablePath             : C:\Windows\System32\svchost.exe
ExecutionState             :
Handle                     : 1668
HandleCount                : 359
InstallDate                :
KernelModeTime             : 14621024
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 12927
OtherTransferCount         : 444738
PageFaults                 : 166121
PageFileUsage              : 145148
ParentProcessId            : 488
PeakPageFileUsage          : 245408
PeakVirtualSize            : 317341696
PeakWorkingSetSize         : 243872
Priority                   : 8
PrivatePageCount           : 148631552
ProcessId                  : 1668
QuotaNonPagedPoolUsage     : 36
QuotaPagedPoolUsage        : 64
QuotaPeakNonPagedPoolUsage : 41
QuotaPeakPagedPoolUsage    : 75
ReadOperationCount         : 917
ReadTransferCount          : 46138771
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 13
UserModeTime               : 47968976
VirtualSize                : 219480064
WindowsVersion             : 6.1.7600
WorkingSetSize             : 8355840
WriteOperationCount        : 214
WriteTransferCount         : 6614
PSComputerName             : JOHN-PC
ProcessName                : svchost.exe
Handles                    : 359
VM                         : 219480064
WS                         : 8355840
Path                       : C:\Windows\System32\svchost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1192"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="1192"
Caption                    : SearchIndexer.exe
CommandLine                : C:\Windows\system32\SearchIndexer.exe /Embedding
CreationClassName          : Win32_Process
CreationDate               : 20170712122548.509448-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : SearchIndexer.exe
ExecutablePath             : C:\Windows\system32\SearchIndexer.exe
ExecutionState             :
Handle                     : 1192
HandleCount                : 667
InstallDate                :
KernelModeTime             : 4606624
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : SearchIndexer.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 52920
OtherTransferCount         : 4811782
PageFaults                 : 9205
PageFileUsage              : 15412
ParentProcessId            : 488
PeakPageFileUsage          : 16316
PeakVirtualSize            : 113541120
PeakWorkingSetSize         : 12264
Priority                   : 8
PrivatePageCount           : 15781888
ProcessId                  : 1192
QuotaNonPagedPoolUsage     : 17
QuotaPagedPoolUsage        : 71
QuotaPeakNonPagedPoolUsage : 22
QuotaPeakPagedPoolUsage    : 96
ReadOperationCount         : 609
ReadTransferCount          : 6666438
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 11
UserModeTime               : 7310512
VirtualSize                : 87171072
WindowsVersion             : 6.1.7600
WorkingSetSize             : 7647232
WriteOperationCount        : 210
WriteTransferCount         : 962228
PSComputerName             : JOHN-PC
ProcessName                : SearchIndexer.exe
Handles                    : 667
VM                         : 87171072
WS                         : 7647232
Path                       : C:\Windows\system32\SearchIndexer.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1264"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="1264"
Caption                    : dwm.exe
CommandLine                : "C:\Windows\system32\Dwm.exe"
CreationClassName          : Win32_Process
CreationDate               : 20170712123339.426000-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : dwm.exe
ExecutablePath             : C:\Windows\system32\Dwm.exe
ExecutionState             :
Handle                     : 1264
HandleCount                : 66
InstallDate                :
KernelModeTime             : 0
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : dwm.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 226
OtherTransferCount         : 786
PageFaults                 : 993
PageFileUsage              : 872
ParentProcessId            : 900
PeakPageFileUsage          : 1036
PeakVirtualSize            : 42967040
PeakWorkingSetSize         : 3464
Priority                   : 8
PrivatePageCount           : 892928
ProcessId                  : 1264
QuotaNonPagedPoolUsage     : 4
QuotaPagedPoolUsage        : 40
QuotaPeakNonPagedPoolUsage : 4
QuotaPeakPagedPoolUsage    : 44
ReadOperationCount         : 1
ReadTransferCount          : 15398
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 3
UserModeTime               : 200288
VirtualSize                : 40202240
WindowsVersion             : 6.1.7600
WorkingSetSize             : 3006464
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : JOHN-PC
ProcessName                : dwm.exe
Handles                    : 66
VM                         : 40202240
WS                         : 3006464
Path                       : C:\Windows\system32\Dwm.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="980"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="980"
Caption                    : explorer.exe
CommandLine                : C:\Windows\Explorer.EXE
CreationClassName          : Win32_Process
CreationDate               : 20170712123339.446028-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : explorer.exe
ExecutablePath             : C:\Windows\Explorer.EXE
ExecutionState             :
Handle                     : 980
HandleCount                : 671
InstallDate                :
KernelModeTime             : 9513680
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : explorer.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 10039
OtherTransferCount         : 899546
PageFaults                 : 16650
PageFileUsage              : 17808
ParentProcessId            : 144
PeakPageFileUsage          : 18464
PeakVirtualSize            : 197206016
PeakWorkingSetSize         : 27632
Priority                   : 8
PrivatePageCount           : 18235392
ProcessId                  : 980
QuotaNonPagedPoolUsage     : 22
QuotaPagedPoolUsage        : 189
QuotaPeakNonPagedPoolUsage : 27
QuotaPeakPagedPoolUsage    : 195
ReadOperationCount         : 880
ReadTransferCount          : 2500972
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 20
UserModeTime               : 4306192
VirtualSize                : 195244032
WindowsVersion             : 6.1.7600
WorkingSetSize             : 27623424
WriteOperationCount        : 7
WriteTransferCount         : 1622
PSComputerName             : JOHN-PC
ProcessName                : explorer.exe
Handles                    : 671
VM                         : 195244032
WS                         : 27623424
Path                       : C:\Windows\Explorer.EXE

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1344"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="1344"
Caption                    : taskhost.exe
CommandLine                : "taskhost.exe"
CreationClassName          : Win32_Process
CreationDate               : 20170712123339.466057-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : taskhost.exe
ExecutablePath             : C:\Windows\system32\taskhost.exe
ExecutionState             :
Handle                     : 1344
HandleCount                : 141
InstallDate                :
KernelModeTime             : 200288
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : taskhost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 297
OtherTransferCount         : 692
PageFaults                 : 1863
PageFileUsage              : 2024
ParentProcessId            : 488
PeakPageFileUsage          : 2120
PeakVirtualSize            : 44015616
PeakWorkingSetSize         : 4780
Priority                   : 8
PrivatePageCount           : 2072576
ProcessId                  : 1344
QuotaNonPagedPoolUsage     : 9
QuotaPagedPoolUsage        : 45
QuotaPeakNonPagedPoolUsage : 9
QuotaPeakPagedPoolUsage    : 46
ReadOperationCount         : 3
ReadTransferCount          : 62250
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 8
UserModeTime               : 200288
VirtualSize                : 41598976
WindowsVersion             : 6.1.7600
WorkingSetSize             : 4276224
WriteOperationCount        : 2
WriteTransferCount         : 142
PSComputerName             : JOHN-PC
ProcessName                : taskhost.exe
Handles                    : 141
VM                         : 41598976
WS                         : 4276224
Path                       : C:\Windows\system32\taskhost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="2056"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="2056"
Caption                    : VBoxTray.exe
CommandLine                : "C:\Windows\System32\VBoxTray.exe"
CreationClassName          : Win32_Process
CreationDate               : 20170712123340.046892-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : VBoxTray.exe
ExecutablePath             : C:\Windows\System32\VBoxTray.exe
ExecutionState             :
Handle                     : 2056
HandleCount                : 136
InstallDate                :
KernelModeTime             : 1502160
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : VBoxTray.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 52845
OtherTransferCount         : 349038
PageFaults                 : 13153
PageFileUsage              : 1244
ParentProcessId            : 980
PeakPageFileUsage          : 1280
PeakVirtualSize            : 65552384
PeakWorkingSetSize         : 4516
Priority                   : 8
PrivatePageCount           : 1273856
ProcessId                  : 2056
QuotaNonPagedPoolUsage     : 6
QuotaPagedPoolUsage        : 53
QuotaPeakNonPagedPoolUsage : 6
QuotaPeakPagedPoolUsage    : 54
ReadOperationCount         : 8095
ReadTransferCount          : 81006
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 11
UserModeTime               : 300432
VirtualSize                : 61358080
WindowsVersion             : 6.1.7600
WorkingSetSize             : 3899392
WriteOperationCount        : 4047
WriteTransferCount         : 16188
PSComputerName             : JOHN-PC
ProcessName                : VBoxTray.exe
Handles                    : 136
VM                         : 61358080
WS                         : 3899392
Path                       : C:\Windows\System32\VBoxTray.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="2244"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="2244"
Caption                    : firefox.exe
CommandLine                : "C:\Program Files\Mozilla Firefox\firefox.exe"
CreationClassName          : Win32_Process
CreationDate               : 20170712123342.971132-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : firefox.exe
ExecutablePath             : C:\Program Files\Mozilla Firefox\firefox.exe
ExecutionState             :
Handle                     : 2244
HandleCount                : 622
InstallDate                :
KernelModeTime             : 103649040
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : firefox.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 67866
OtherTransferCount         : 1039678
PageFaults                 : 381767
PageFileUsage              : 122084
ParentProcessId            : 980
PeakPageFileUsage          : 148096
PeakVirtualSize            : 604745728
PeakWorkingSetSize         : 155248
Priority                   : 8
PrivatePageCount           : 125014016
ProcessId                  : 2244
QuotaNonPagedPoolUsage     : 28
QuotaPagedPoolUsage        : 200
QuotaPeakNonPagedPoolUsage : 158
QuotaPeakPagedPoolUsage    : 203
ReadOperationCount         : 7689
ReadTransferCount          : 411068937
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 45
UserModeTime               : 438530576
VirtualSize                : 579633152
WindowsVersion             : 6.1.7600
WorkingSetSize             : 135786496
WriteOperationCount        : 941843
WriteTransferCount         : 176029996
PSComputerName             : JOHN-PC
ProcessName                : firefox.exe
Handles                    : 622
VM                         : 579633152
WS                         : 135786496
Path                       : C:\Program Files\Mozilla Firefox\firefox.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="2480"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="2480"
Caption                    : firefox.exe
CommandLine                : "C:\Program Files\Mozilla Firefox\firefox.exe" -contentproc --channel="2244.0.548555581\175440830" -childID 1 -isForBrowser -intPrefs 5:50|6:-1|28:1000|33:20|34:10|43:128|44
                             :10000|48:0|50:400|51:1|52:0|53:0|58:0|59:120|60:120|133:2|134:1|147:5000|157:0|159:0|170:10000|182:-1|187:128|188:10000|189:0|195:24|196:32768|198:0|199:0|207:5|211:1048576
                             |212:100|213:5000|215:600|217:1|226:1|231:0|241:60000| -boolPrefs 1:0|2:0|4:0|26:1|27:1|30:0|35:1|36:0|37:0|38:0|39:1|40:0|41:1|42:1|45:0|46:0|47:0|49:0|54:1|55:1|56:0|57:1|
                             61:1|62:1|63:0|64:1|65:1|66:0|67:1|70:0|71:0|74:1|75:1|79:1|80:1|81:0|82:0|84:0|85:0|86:1|87:0|90:0|91:1|92:1|93:1|94:1|95:1|96:0|97:0|98:1|99:0|100:0|101:0|102:1|103:1|104:
                             0|105:1|106:1|107:0|108:0|109:1|110:1|111:1|112:0|113:1|114:1|115:1|116:1|117:1|118:1|119:1|120:1|122:0|123:0|124:0|125:1|126:0|127:1|131:1|132:1|135:1|136:0|141:0|146:0|149
                             :1|152:1|154:1|158:0|161:1|164:1|165:1|171:0|172:0|173:1|175:0|181:0|183:1|184:0|185:0|186:0|193:0|194:0|197:1|200:0|202:0|204:1|205:0|210:0|214:1|219:0|220:0|221:0|222:1|22
                             4:1|225:1|228:0|233:0|234:0|235:1|236:1|237:0|238:1|239:1|240:0|242:0|243:0|245:0|253:1|254:1|255:0|256:0|257:0| -stringPrefs "3:7;release|174:3;1.0|191:332; ¼½¾!???:?????%?
                             ???????       ???????-’·?????????‹›?/???????????????/:?????????????????? ???????????????????./???????|192:8;moderate|227:38;{1a7261b9-5e44-4ce3-bde9-ad3e4a859d9a}|"
                             -greomni "C:\Program Files\Mozilla Firefox\omni.ja" -appomni "C:\Program Files\Mozilla Firefox\browser\omni.ja" -appdir "C:\Program Files\Mozilla Firefox\browser"  2244
                             "\\.\pipe\gecko-crash-server-pipe.2244" tab
CreationClassName          : Win32_Process
CreationDate               : 20170712123344.804771-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : firefox.exe
ExecutablePath             : C:\Program Files\Mozilla Firefox\firefox.exe
ExecutionState             :
Handle                     : 2480
HandleCount                : 291
InstallDate                :
KernelModeTime             : 10214688
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : firefox.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 2838
OtherTransferCount         : 21324
PageFaults                 : 26002
PageFileUsage              : 30428
ParentProcessId            : 2244
PeakPageFileUsage          : 36828
PeakVirtualSize            : 374845440
PeakWorkingSetSize         : 61540
Priority                   : 8
PrivatePageCount           : 31158272
ProcessId                  : 2480
QuotaNonPagedPoolUsage     : 16
QuotaPagedPoolUsage        : 152
QuotaPeakNonPagedPoolUsage : 21
QuotaPeakPagedPoolUsage    : 159
ReadOperationCount         : 6709
ReadTransferCount          : 59186239
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 20
UserModeTime               : 7110224
VirtualSize                : 361779200
WindowsVersion             : 6.1.7600
WorkingSetSize             : 42983424
WriteOperationCount        : 4326
WriteTransferCount         : 576704
PSComputerName             : JOHN-PC
ProcessName                : firefox.exe
Handles                    : 291
VM                         : 361779200
WS                         : 42983424
Path                       : C:\Program Files\Mozilla Firefox\firefox.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="2844"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="2844"
Caption                    : wmpnetwk.exe
CommandLine                : "C:\Program Files\Windows Media Player\wmpnetwk.exe"
CreationClassName          : Win32_Process
CreationDate               : 20170712123348.174625-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : wmpnetwk.exe
ExecutablePath             : C:\Program Files\Windows Media Player\wmpnetwk.exe
ExecutionState             :
Handle                     : 2844
HandleCount                : 220
InstallDate                :
KernelModeTime             : 901296
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : wmpnetwk.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 3426
OtherTransferCount         : 106030
PageFaults                 : 13164
PageFileUsage              : 3292
ParentProcessId            : 488
PeakPageFileUsage          : 3732
PeakVirtualSize            : 84627456
PeakWorkingSetSize         : 8672
Priority                   : 8
PrivatePageCount           : 3371008
ProcessId                  : 2844
QuotaNonPagedPoolUsage     : 8
QuotaPagedPoolUsage        : 81
QuotaPeakNonPagedPoolUsage : 9
QuotaPeakPagedPoolUsage    : 86
ReadOperationCount         : 710
ReadTransferCount          : 147842
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 9
UserModeTime               : 2002880
VirtualSize                : 78745600
WindowsVersion             : 6.1.7600
WorkingSetSize             : 3600384
WriteOperationCount        : 8
WriteTransferCount         : 544
PSComputerName             : JOHN-PC
ProcessName                : wmpnetwk.exe
Handles                    : 220
VM                         : 78745600
WS                         : 3600384
Path                       : C:\Program Files\Windows Media Player\wmpnetwk.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="3024"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="3024"
Caption                    : svchost.exe
CommandLine                : C:\Windows\System32\svchost.exe -k LocalServicePeerNet
CreationClassName          : Win32_Process
CreationDate               : 20170712123348.685360-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : svchost.exe
ExecutablePath             : C:\Windows\System32\svchost.exe
ExecutionState             :
Handle                     : 3024
HandleCount                : 341
InstallDate                :
KernelModeTime             : 19327792
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 201161
OtherTransferCount         : 7589924
PageFaults                 : 12646
PageFileUsage              : 8156
ParentProcessId            : 488
PeakPageFileUsage          : 8188
PeakVirtualSize            : 76333056
PeakWorkingSetSize         : 9876
Priority                   : 8
PrivatePageCount           : 8351744
ProcessId                  : 3024
QuotaNonPagedPoolUsage     : 13
QuotaPagedPoolUsage        : 57
QuotaPeakNonPagedPoolUsage : 40
QuotaPeakPagedPoolUsage    : 58
ReadOperationCount         : 73
ReadTransferCount          : 1984308
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 7
UserModeTime               : 9413536
VirtualSize                : 69562368
WindowsVersion             : 6.1.7600
WorkingSetSize             : 9433088
WriteOperationCount        : 835
WriteTransferCount         : 1454446
PSComputerName             : JOHN-PC
ProcessName                : svchost.exe
Handles                    : 341
VM                         : 69562368
WS                         : 9433088
Path                       : C:\Windows\System32\svchost.exe

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
WorkingSetSize             : 37801984
WriteOperationCount        : 3
WriteTransferCount         : 6434
PSComputerName             : JOHN-PC
ProcessName                : powershell.exe
Handles                    : 519
VM                         : 184668160
WS                         : 37801984
Path                       : C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="3244"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="3244"
Caption                    : conhost.exe
CommandLine                : \??\C:\Windows\system32\conhost.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712123353.452214-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : conhost.exe
ExecutablePath             : C:\Windows\system32\conhost.exe
ExecutionState             :
Handle                     : 3244
HandleCount                : 39
InstallDate                :
KernelModeTime             : 8111664
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : conhost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 172
OtherTransferCount         : 824
PageFaults                 : 2443
PageFileUsage              : 3840
ParentProcessId            : 404
PeakPageFileUsage          : 4984
PeakVirtualSize            : 47939584
PeakWorkingSetSize         : 7048
Priority                   : 8
PrivatePageCount           : 3932160
ProcessId                  : 3244
QuotaNonPagedPoolUsage     : 3
QuotaPagedPoolUsage        : 46
QuotaPeakNonPagedPoolUsage : 3
QuotaPeakPagedPoolUsage    : 47
ReadOperationCount         : 22
ReadTransferCount          : 11850
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 2
UserModeTime               : 701008
VirtualSize                : 47136768
WindowsVersion             : 6.1.7600
WorkingSetSize             : 6479872
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : JOHN-PC
ProcessName                : conhost.exe
Handles                    : 39
VM                         : 47136768
WS                         : 6479872
Path                       : C:\Windows\system32\conhost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="3444"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="3444"
Caption                    : cmd.exe
CommandLine                : "C:\Windows\system32\cmd.exe"
CreationClassName          : Win32_Process
CreationDate               : 20170712124552.936782-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : cmd.exe
ExecutablePath             : C:\Windows\system32\cmd.exe
ExecutionState             :
Handle                     : 3444
HandleCount                : 23
InstallDate                :
KernelModeTime             : 200288
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : cmd.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 259
OtherTransferCount         : 1746
PageFaults                 : 576
PageFileUsage              : 1760
ParentProcessId            : 980
PeakPageFileUsage          : 1760
PeakVirtualSize            : 31256576
PeakWorkingSetSize         : 2168
Priority                   : 8
PrivatePageCount           : 1802240
ProcessId                  : 3444
QuotaNonPagedPoolUsage     : 3
QuotaPagedPoolUsage        : 33
QuotaPeakNonPagedPoolUsage : 6
QuotaPeakPagedPoolUsage    : 33
ReadOperationCount         : 1
ReadTransferCount          : 11742
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 1
UserModeTime               : 0
VirtualSize                : 31256576
WindowsVersion             : 6.1.7600
WorkingSetSize             : 2097152
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : JOHN-PC
ProcessName                : cmd.exe
Handles                    : 23
VM                         : 31256576
WS                         : 2097152
Path                       : C:\Windows\system32\cmd.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="3712"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="3712"
Caption                    : conhost.exe
CommandLine                : \??\C:\Windows\system32\conhost.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712124552.946796-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : conhost.exe
ExecutablePath             : C:\Windows\system32\conhost.exe
ExecutionState             :
Handle                     : 3712
HandleCount                : 36
InstallDate                :
KernelModeTime             : 0
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : conhost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 170
OtherTransferCount         : 758
PageFaults                 : 714
PageFileUsage              : 604
ParentProcessId            : 404
PeakPageFileUsage          : 624
PeakVirtualSize            : 42553344
PeakWorkingSetSize         : 2696
Priority                   : 8
PrivatePageCount           : 618496
ProcessId                  : 3712
QuotaNonPagedPoolUsage     : 3
QuotaPagedPoolUsage        : 37
QuotaPeakNonPagedPoolUsage : 3
QuotaPeakPagedPoolUsage    : 45
ReadOperationCount         : 15
ReadTransferCount          : 12236
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 2
UserModeTime               : 0
VirtualSize                : 33808384
WindowsVersion             : 6.1.7600
WorkingSetSize             : 2752512
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : JOHN-PC
ProcessName                : conhost.exe
Handles                    : 36
VM                         : 33808384
WS                         : 2752512
Path                       : C:\Windows\system32\conhost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="3524"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="3524"
Caption                    : python.exe
CommandLine                : python  -m SimpleHTTPServer
CreationClassName          : Win32_Process
CreationDate               : 20170712124602.320275-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : python.exe
ExecutablePath             : C:\Python27\python.exe
ExecutionState             :
Handle                     : 3524
HandleCount                : 134
InstallDate                :
KernelModeTime             : 1201728
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : python.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 42258
OtherTransferCount         : 678289
PageFaults                 : 2591
PageFileUsage              : 6324
ParentProcessId            : 3444
PeakPageFileUsage          : 6384
PeakVirtualSize            : 72130560
PeakWorkingSetSize         : 9872
Priority                   : 8
PrivatePageCount           : 6475776
ProcessId                  : 3524
QuotaNonPagedPoolUsage     : 6
QuotaPagedPoolUsage        : 56
QuotaPeakNonPagedPoolUsage : 23
QuotaPeakPagedPoolUsage    : 56
ReadOperationCount         : 204
ReadTransferCount          : 907444
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 2
UserModeTime               : 701008
VirtualSize                : 66035712
WindowsVersion             : 6.1.7600
WorkingSetSize             : 5103616
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : JOHN-PC
ProcessName                : python.exe
Handles                    : 134
VM                         : 66035712
WS                         : 5103616
Path                       : C:\Python27\python.exe

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
WorkingSetSize             : 32100352
WriteOperationCount        : 3
WriteTransferCount         : 6434
PSComputerName             : JOHN-PC
ProcessName                : powershell.exe
Handles                    : 384
VM                         : 170201088
WS                         : 32100352
Path                       : C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="2960"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="2960"
Caption                    : conhost.exe
CommandLine                : \??\C:\Windows\system32\conhost.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712130457.209371-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : conhost.exe
ExecutablePath             : C:\Windows\system32\conhost.exe
ExecutionState             :
Handle                     : 2960
HandleCount                : 39
InstallDate                :
KernelModeTime             : 1201728
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : conhost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 161
OtherTransferCount         : 648
PageFaults                 : 1803
PageFileUsage              : 4224
ParentProcessId            : 404
PeakPageFileUsage          : 4224
PeakVirtualSize            : 47144960
PeakWorkingSetSize         : 6612
Priority                   : 8
PrivatePageCount           : 4325376
ProcessId                  : 2960
QuotaNonPagedPoolUsage     : 3
QuotaPagedPoolUsage        : 46
QuotaPeakNonPagedPoolUsage : 3
QuotaPeakPagedPoolUsage    : 47
ReadOperationCount         : 22
ReadTransferCount          : 12622
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 2
UserModeTime               : 300432
VirtualSize                : 47136768
WindowsVersion             : 6.1.7600
WorkingSetSize             : 6746112
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : JOHN-PC
ProcessName                : conhost.exe
Handles                    : 39
VM                         : 47136768
WS                         : 6746112
Path                       : C:\Windows\system32\conhost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="3408"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="3408"
Caption                    : notepad.exe
CommandLine                : "C:\Windows\system32\NOTEPAD.EXE" C:\Users\John\Desktop\log.txt
CreationClassName          : Win32_Process
CreationDate               : 20170712130654.798456-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : notepad.exe
ExecutablePath             : C:\Windows\system32\NOTEPAD.EXE
ExecutionState             :
Handle                     : 3408
HandleCount                : 56
InstallDate                :
KernelModeTime             : 600864
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : notepad.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 265
OtherTransferCount         : 1230
PageFaults                 : 1104
PageFileUsage              : 1008
ParentProcessId            : 980
PeakPageFileUsage          : 1008
PeakVirtualSize            : 57073664
PeakWorkingSetSize         : 4256
Priority                   : 8
PrivatePageCount           : 1032192
ProcessId                  : 3408
QuotaNonPagedPoolUsage     : 4
QuotaPagedPoolUsage        : 58
QuotaPeakNonPagedPoolUsage : 4
QuotaPeakPagedPoolUsage    : 58
ReadOperationCount         : 2
ReadTransferCount          : 19076
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 1
UserModeTime               : 200288
VirtualSize                : 57016320
WindowsVersion             : 6.1.7600
WorkingSetSize             : 4304896
WriteOperationCount        : 1
WriteTransferCount         : 6205
PSComputerName             : JOHN-PC
ProcessName                : notepad.exe
Handles                    : 56
VM                         : 57016320
WS                         : 4304896
Path                       : C:\Windows\system32\NOTEPAD.EXE

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1604"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="1604"
Caption                    : wuauclt.exe
CommandLine                : "C:\Windows\system32\wuauclt.exe"
CreationClassName          : Win32_Process
CreationDate               : 20170712171611.519551-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : wuauclt.exe
ExecutablePath             : C:\Windows\system32\wuauclt.exe
ExecutionState             :
Handle                     : 1604
HandleCount                : 87
InstallDate                :
KernelModeTime             : 200288
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : wuauclt.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 581
OtherTransferCount         : 3230
PageFaults                 : 1465
PageFileUsage              : 1116
ParentProcessId            : 940
PeakPageFileUsage          : 1176
PeakVirtualSize            : 74887168
PeakWorkingSetSize         : 4552
Priority                   : 8
PrivatePageCount           : 1142784
ProcessId                  : 1604
QuotaNonPagedPoolUsage     : 5
QuotaPagedPoolUsage        : 54
QuotaPeakNonPagedPoolUsage : 6
QuotaPeakPagedPoolUsage    : 74
ReadOperationCount         : 1
ReadTransferCount          : 16278
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 3
UserModeTime               : 100144
VirtualSize                : 54349824
WindowsVersion             : 6.1.7600
WorkingSetSize             : 3743744
WriteOperationCount        : 8
WriteTransferCount         : 862
PSComputerName             : JOHN-PC
ProcessName                : wuauclt.exe
Handles                    : 87
VM                         : 54349824
WS                         : 3743744
Path                       : C:\Windows\system32\wuauclt.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="2356"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : JOHN-PC
__NAMESPACE                : root\cimv2
__PATH                     : \\JOHN-PC\root\cimv2:Win32_Process.Handle="2356"
Caption                    : WmiPrvSE.exe
CommandLine                : C:\Windows\system32\wbem\wmiprvse.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712181550.475665-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : JOHN-PC
Description                : WmiPrvSE.exe
ExecutablePath             : C:\Windows\system32\wbem\wmiprvse.exe
ExecutionState             :
Handle                     : 2356
HandleCount                : 115
InstallDate                :
KernelModeTime             : 100144
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : WmiPrvSE.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows 7 Ultimate |C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 423
OtherTransferCount         : 1538
PageFaults                 : 1238
PageFileUsage              : 1820
ParentProcessId            : 608
PeakPageFileUsage          : 1820
PeakVirtualSize            : 26275840
PeakWorkingSetSize         : 4460
Priority                   : 8
PrivatePageCount           : 1863680
ProcessId                  : 2356
QuotaNonPagedPoolUsage     : 5
QuotaPagedPoolUsage        : 26
QuotaPeakNonPagedPoolUsage : 5
QuotaPeakPagedPoolUsage    : 26
ReadOperationCount         : 1
ReadTransferCount          : 37802
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 7
UserModeTime               : 200288
VirtualSize                : 26275840
WindowsVersion             : 6.1.7600
WorkingSetSize             : 4567040
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : JOHN-PC
ProcessName                : WmiPrvSE.exe
Handles                    : 115
VM                         : 26275840
WS                         : 4567040
Path                       : C:\Windows\system32\wbem\wmiprvse.exe

PS C:\Users\Administrator>
```

- ```Get-WmiObject``` - ```Filter```

```PowerShell
PS C:\Users\Administrator> Get-WmiObject -Class Win32_Process -Filter {Name = "powershell.exe"}

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="3416"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="3416"
Caption                    : powershell.exe
CommandLine                : "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
CreationClassName          : Win32_Process
CreationDate               : 20170712164403.172486-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : powershell.exe
ExecutablePath             : C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
ExecutionState             :
Handle                     : 3416
HandleCount                : 523
InstallDate                :
KernelModeTime             : 26718750
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : powershell.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 144949
OtherTransferCount         : 7251556
PageFaults                 : 300851
PageFileUsage              : 110900
ParentProcessId            : 1188
PeakPageFileUsage          : 114860
PeakVirtualSize            : 736120832
PeakWorkingSetSize         : 123328
Priority                   : 8
PrivatePageCount           : 113561600
ProcessId                  : 3416
QuotaNonPagedPoolUsage     : 40
QuotaPagedPoolUsage        : 577
QuotaPeakNonPagedPoolUsage : 46
QuotaPeakPagedPoolUsage    : 578
ReadOperationCount         : 1110
ReadTransferCount          : 3557444
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 12
UserModeTime               : 176250000
VirtualSize                : 733343744
WindowsVersion             : 6.3.9600
WorkingSetSize             : 124723200
WriteOperationCount        : 80
WriteTransferCount         : 18596
PSComputerName             : WIN-2012-DC
ProcessName                : powershell.exe
Handles                    : 523
VM                         : 733343744
WS                         : 124723200
Path                       : C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe

PS C:\Users\Administrator>
```

- ```Get-WmiObject``` - ```Where-Object```

```PowerShell
PS C:\Users\Administrator> Get-WmiObject -Class Win32_Process | Where-Object {$_.Name -eq "powershell.exe"}

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="3416"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="3416"
Caption                    : powershell.exe
CommandLine                : "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
CreationClassName          : Win32_Process
CreationDate               : 20170712164403.172486-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : powershell.exe
ExecutablePath             : C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
ExecutionState             :
Handle                     : 3416
HandleCount                : 564
InstallDate                :
KernelModeTime             : 26718750
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : powershell.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 146742
OtherTransferCount         : 7521736
PageFaults                 : 301103
PageFileUsage              : 110920
ParentProcessId            : 1188
PeakPageFileUsage          : 114860
PeakVirtualSize            : 736120832
PeakWorkingSetSize         : 123328
Priority                   : 8
PrivatePageCount           : 113582080
ProcessId                  : 3416
QuotaNonPagedPoolUsage     : 40
QuotaPagedPoolUsage        : 577
QuotaPeakNonPagedPoolUsage : 46
QuotaPeakPagedPoolUsage    : 578
ReadOperationCount         : 1110
ReadTransferCount          : 3557444
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 12
UserModeTime               : 176875000
VirtualSize                : 734392320
WindowsVersion             : 6.3.9600
WorkingSetSize             : 124850176
WriteOperationCount        : 80
WriteTransferCount         : 18596
PSComputerName             : WIN-2012-DC
ProcessName                : powershell.exe
Handles                    : 564
VM                         : 734392320
WS                         : 124850176
Path                       : C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe

PS C:\Users\Administrator>
```

- ```Get-WmiObject``` - ```Query ```

```PowerShell
PS C:\Users\Administrator> Get-WmiObject -Query {Select * from Win32_Process where Name="powershell.exe"}

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="3416"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="3416"
Caption                    : powershell.exe
CommandLine                : "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
CreationClassName          : Win32_Process
CreationDate               : 20170712164403.172486-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : powershell.exe
ExecutablePath             : C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
ExecutionState             :
Handle                     : 3416
HandleCount                : 546
InstallDate                :
KernelModeTime             : 27187500
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : powershell.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 149572
OtherTransferCount         : 8065898
PageFaults                 : 301349
PageFileUsage              : 111084
ParentProcessId            : 1188
PeakPageFileUsage          : 114860
PeakVirtualSize            : 736120832
PeakWorkingSetSize         : 123328
Priority                   : 8
PrivatePageCount           : 113750016
ProcessId                  : 3416
QuotaNonPagedPoolUsage     : 39
QuotaPagedPoolUsage        : 577
QuotaPeakNonPagedPoolUsage : 46
QuotaPeakPagedPoolUsage    : 578
ReadOperationCount         : 1110
ReadTransferCount          : 3557444
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 11
UserModeTime               : 177656250
VirtualSize                : 733859840
WindowsVersion             : 6.3.9600
WorkingSetSize             : 125005824
WriteOperationCount        : 80
WriteTransferCount         : 18596
PSComputerName             : WIN-2012-DC
ProcessName                : powershell.exe
Handles                    : 546
VM                         : 733859840
WS                         : 125005824
Path                       : C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe

PS C:\Users\Administrator>
```

```PowerShell
PS C:\Users\Administrator> Get-WmiObject -Query {Select * from Win32_Process where Name="notepad.exe"}

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="956"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="956"
Caption                    : notepad.exe
CommandLine                : "C:\Windows\system32\NOTEPAD.EXE" C:\Users\Administrator\Desktop\log.txt
CreationClassName          : Win32_Process
CreationDate               : 20170712153213.828260-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : notepad.exe
ExecutablePath             : C:\Windows\system32\NOTEPAD.EXE
ExecutionState             :
Handle                     : 956
HandleCount                : 95
InstallDate                :
KernelModeTime             : 937500
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : notepad.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 207
OtherTransferCount         : 1744
PageFaults                 : 4672
PageFileUsage              : 3024
ParentProcessId            : 1188
PeakPageFileUsage          : 4012
PeakVirtualSize            : 151597056
PeakWorkingSetSize         : 10756
Priority                   : 8
PrivatePageCount           : 3096576
ProcessId                  : 956
QuotaNonPagedPoolUsage     : 9
QuotaPagedPoolUsage        : 278
QuotaPeakNonPagedPoolUsage : 10
QuotaPeakPagedPoolUsage    : 289
ReadOperationCount         : 1
ReadTransferCount          : 60
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 1
UserModeTime               : 625000
VirtualSize                : 148074496
WindowsVersion             : 6.3.9600
WorkingSetSize             : 10457088
WriteOperationCount        : 10
WriteTransferCount         : 672390
PSComputerName             : WIN-2012-DC
ProcessName                : notepad.exe
Handles                    : 95
VM                         : 148074496
WS                         : 10457088
Path                       : C:\Windows\system32\NOTEPAD.EXE

PS C:\Users\Administrator>
```

- ```Remove-WmiObject```

```PowerShell
PS C:\Users\Administrator> Get-WmiObject -Query {Select * from Win32_Process where Name="notepad.exe"} | Remove-WmiObject
```

###### [Excercise](http://windowsitpro.com/powershell/powershell-basics-filtering-objects)

- List the path of Executables for each process on your machine.

```PowerShell
PS C:\Users\Administrator> Get-WmiObject -Class Win32_Process | Select-Object -Property Name,Path

Name                                                                                                  Path
----                                                                                                  ----
System Idle Process
System
smss.exe
csrss.exe
csrss.exe
wininit.exe                                                                                           C:\Windows\system32\wininit.exe
winlogon.exe                                                                                          C:\Windows\system32\winlogon.exe
services.exe
lsass.exe                                                                                             C:\Windows\system32\lsass.exe
svchost.exe                                                                                           C:\Windows\system32\svchost.exe
svchost.exe                                                                                           C:\Windows\system32\svchost.exe
dwm.exe                                                                                               C:\Windows\system32\dwm.exe
VBoxService.exe                                                                                       C:\Windows\System32\VBoxService.exe
svchost.exe                                                                                           C:\Windows\System32\svchost.exe
svchost.exe                                                                                           C:\Windows\system32\svchost.exe
svchost.exe                                                                                           C:\Windows\system32\svchost.exe
svchost.exe                                                                                           C:\Windows\system32\svchost.exe
svchost.exe                                                                                           C:\Windows\system32\svchost.exe
spoolsv.exe                                                                                           C:\Windows\System32\spoolsv.exe
Microsoft.ActiveDirectory.WebServices.exe                                                             C:\Windows\ADWS\Microsoft.ActiveDirectory.WebServices.exe
dfsrs.exe                                                                                             C:\Windows\system32\DFSRs.exe
dns.exe                                                                                               C:\Windows\system32\dns.exe
ismserv.exe                                                                                           C:\Windows\System32\ismserv.exe
wlms.exe                                                                                              C:\Windows\system32\wlms\wlms.exe
dfssvc.exe                                                                                            C:\Windows\system32\dfssvc.exe
vds.exe                                                                                               C:\Windows\System32\vds.exe
svchost.exe                                                                                           C:\Windows\System32\svchost.exe
svchost.exe                                                                                           C:\Windows\system32\svchost.exe
svchost.exe                                                                                           C:\Windows\system32\svchost.exe
msdtc.exe                                                                                             C:\Windows\System32\msdtc.exe
taskhostex.exe                                                                                        C:\Windows\system32\taskhostex.exe
explorer.exe                                                                                          C:\Windows\Explorer.EXE
VBoxTray.exe                                                                                          C:\Windows\System32\VBoxTray.exe
cmd.exe                                                                                               C:\Windows\system32\cmd.exe
conhost.exe                                                                                           C:\Windows\system32\conhost.exe
python.exe                                                                                            C:\Python27\python.exe
firefox.exe                                                                                           C:\Program Files\Mozilla Firefox\firefox.exe
firefox.exe                                                                                           C:\Program Files\Mozilla Firefox\firefox.exe
powershell.exe                                                                                        C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
conhost.exe                                                                                           C:\Windows\system32\conhost.exe
WmiPrvSE.exe                                                                                          C:\Windows\system32\wbem\wmiprvse.exe
notepad.exe                                                                                           C:\Windows\system32\NOTEPAD.EXE

PS C:\Users\Administrator>
```