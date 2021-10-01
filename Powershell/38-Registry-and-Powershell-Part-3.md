#### 38. Registry and Powershell Part 3

###### Windows Registry on Remote Computer

###### Ways of access Registry on a remote computer

- ```Enter-PSSession```

```PowerShell
PS C:\> Enter-PSSession -ComputerName JOHN-PC -Credential John-PC\John
```

```PowerShell
[JOHN-PC]: PS C:\Users\John\Documents> Get-Item 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion'

    Hive: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT


SKC  VC Name                           Property
---  -- ----                           --------
 80  20 CurrentVersion                 {CurrentVersion, CurrentBuild, SoftwareType, CurrentType...}

[JOHN-PC]: PS C:\Users\John\Documents> 
```

```PowerShell
[JOHN-PC]: PS C:\Users\John\Documents> Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion'

PSPath                 : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion
PSParentPath           : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT
PSChildName            : CurrentVersion
PSDrive                : HKLM
PSProvider             : Microsoft.PowerShell.Core\Registry
CurrentVersion         : 6.1
CurrentBuild           : 7600
SoftwareType           : System
CurrentType            : Multiprocessor Free
InstallDate            : 1499805246
RegisteredOrganization :
RegisteredOwner        : John
SystemRoot             : C:\Windows
InstallationType       : Client
EditionID              : Ultimate
ProductName            : Windows 7 Ultimate
ProductId              : 00426-OEM-8992662-00497
DigitalProductId       : {164, 0, 0, 0...}
DigitalProductId4      : {248, 4, 0, 0...}
CurrentBuildNumber     : 7600
BuildLab               : 7600.win7_rtm.090713-1255
BuildLabEx             : 7600.16385.x86fre.win7_rtm.090713-1255
BuildGUID              : e331ce24-377a-47bd-86de-92ae1aa1ae65
CSDBuildNumber         : 1
PathName               : C:\Windows

[JOHN-PC]: PS C:\Users\John\Documents>
```

```PowerShell
[JOHN-PC]: PS C:\Users\John\Documents> Get-ChildItem 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion'

    Hive: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion


SKC  VC Name                           Property
---  -- ----                           --------
  1   0 Accessibility                  {}
  0   0 AdaptiveDisplayBrightness      {}
  1   1 AeDebug                        {UserDebuggerHotKey}
  0  10 APITracing                     {LogFileDirectory, InstalledManifests, LogApiNamesOnly, LogApisRecursively...}
  6   1 AppCompatFlags                 {ApphelpUIExe}
  0   1 ASR                            {OfflineDriverInjectionExtension}
  1   0 Audit                          {}
  0   1 BootMgr                        {KB935509}
  0 174 Compatibility                  {_3DPC, _BNOTES, _LNOTES, ACAD...}
  0   1 Compatibility32                {winword}
  3   0 Console                        {}
  1   2 CorruptedFileRecovery          {RunCount, TraceLevel}
  0   3 DefaultProductKey              {ProductId, DigitalProductId, DigitalProductId4}
  0   3 DefaultProductKey2             {ProductId, DigitalProductId, DigitalProductId4}
  4   1 DeviceDisplayObjects           {DeviceStatusPropertyDescriptionList}
  2   0 DiskDiagnostics                {}
  0   1 Drivers                        {timer}
  0   2 drivers.desc                   {C:\Windows\System32\l3codeca.acm, wdmaud.drv}
  0  20 Drivers32                      {vidc.mrle, vidc.msvc, msacm.imaadpcm, msacm.msg711...}
  0   0 EFS                            {}
  0   0 EMDMgmt                        {}
  0   3 Event Viewer                   {MicrosoftRedirectionProgram, MicrosoftRedirectionProgramCommandLineParameters, MicrosoftRedirectionURL}
  0   1 Font Drivers                   {Adobe Type Manager}
  0   2 Font Management                {Metadata, Auto Deactivation Exclude}
  0   1 FontDPI                        {LogPixels}
  1   2 FontLink                       {FontLinkControl, FontLinkDefaultChar}
  1  44 FontMapper                     {ARIAL, Batang, BatangChe, @Batang...}
  0 244 Fonts                          {Arial (TrueType), Arial Italic (TrueType), Arial Bold (TrueType), Arial Bold Italic (TrueType)...}
  0  32 FontSubstitutes                {Arabic Transparent, Arabic Transparent Bold, Arabic Transparent,0, Arabic Transparent Bold,0...}
  2   2 GRE_Initialize                 {DisableRemoteFontBootCache, LastBootTimeFontCacheState}
  2   0 ICM                            {}
  2   0 Image File Execution Options   {}
  5   0 IniFileMapping                 {}
  1   0 InstalledFeatures              {}
  0   2 KnownFunctionTableDlls         {C:\Windows\Microsoft.NET\Framework\v2.0.50727\mscordacwks.dll, C:\Windows\Microsoft.NET\Framework\v4.0.30319\mscordacwks.dll}
  0   2 KnownManagedDebuggingDlls      {C:\Windows\Microsoft.NET\Framework\v2.0.50727\mscordacwks.dll, C:\Windows\Microsoft.NET\Framework\v4.0.30319\mscordacwks.dll}
  2   1 LanguagePack                   {OpenType}
  0   4 MCI                            {AVIVideo, Sequencer, CDAudio, WaveAudio}
  0  50 MCI Extensions                 {avi, cda, Mid, rmi...}
  0   5 MCI32                          {AVIVideo, CDAudio, Sequencer, WaveAudio...}
  0   2 MiniDumpAuxiliaryDlls          {C:\Windows\Microsoft.NET\Framework\v2.0.50727\mscorwks.dll, C:\Windows\Microsoft.NET\Framework\v4.0.30319\clr.dll}
  0  15 ModuleCompatibility            {CWD, INSTBI01, INSTBI02, INSTBIN...}
  1   0 MsiCorruptedFileRecovery       {}
  1   0 Multimedia                     {}
  1   0 NetworkCards                   {}
  5   2 NetworkList                    {(default), FirstNetwork}
  0   0 NvCache                        {}
  1   0 OpenGLDrivers                  {}
  6   0 PeerDist                       {}
  2   0 PeerNet                        {}
  3   5 Perflib                        {Base Index, Version, Last Counter, Last Help...}
131   1 PerHwIdStorage                 {LastUpdateTime}
  1   0 PolicyGuid                     {}
  0  11 Ports                          {COM1:, COM2:, COM3:, COM4:...}
  0   3 Prefetcher                     {BootFilesOptimized, LastDiskLayoutTime, LastDiskLayoutTimeString}
  5   1 Print                          {DoNotInstallCompatibleDriverFromWindowsUpdate}
  1   0 ProfileGuid                    {}
  5   4 ProfileList                    {ProfilesDirectory, Default, Public, ProgramData}
  1   0 ProfileLoader                  {}
  8   6 ProfileNotification            {Create, Delete, Migrate, Upgrade...}
  0   1 related.desc                   {wave}
  7   1 Schedule                       {DomainJoinDetected}
  2   6 SeCEdit                        {SetupCompDebugLevel, DefaultTemplate, EnvironmentVariables, LastUsedDatabase...}
  1   0 setup                          {}
  5   7 SoftwareProtectionPlatform     {VLActivationInterval, VLRenewalInterval, UserOperations, InactivityShutdownDelay...}
  2   1 SPP                            {LastIndex}
  2   5 Superfetch                     {ServiceFlags, ProcessorTime, PfPdData, MemMonitorState...}
 16  25 Svchost                        {RPCSS, defragsvc, LocalSystemNetworkRestricted, LocalService...}
  3   3 SystemRestore                  {RPSessionInterval, FirstRun, LastIndex}
  1   0 Terminal Server                {}
 91   1 Time Zones                     {TzVersion}
  3   0 Tracing                        {}
  0   1 Userinstallable.drivers        {wave}
  0   0 WbemPerf                       {}
  0  14 Windows                        {IconServiceLib, DdeSendTimeout, DesktopHeapLogging, GDIProcessHandleQuota...}
  2  21 Winlogon                       {ReportBootOk, Shell, PreCreateKnownFolders, Userinit...}
  1  22 Winsat                         {MOOBE, LastExitCode, LastExitCodeCantMsg, LastExitCodeWhyMsg...}
  0   9 WinSATAPI                      {LastFormalAssessment, TaskErrorCount, IdleWinSATRunCount, FirstIdleRunTimeDate...}
  6   0 WOW                            {}
  1   9 WUDF                           {LogEnable, Logkd, LogFlags, LogLevel...}

[JOHN-PC]: PS C:\Users\John\Documents>
```

- ```PowerShell Remoting```

```PowerShell
PS C:\> Invoke-Command -ScriptBlock {Get-Item HKLM:\SOFTWARE} -ComputerName JOHN-PC -Credential John-PC\John

    Hive: HKEY_LOCAL_MACHINE

Name                           Property                                                                              PSComputerName
----                           --------                                                                              --------------
SOFTWARE                                                                                                             JOHN-PC

PS C:\>
```

- ```WMI```

```PowerShell
PS C:\> $RemoteReg = Get-WmiObject -List "StdRegProv" -ComputerName JOHN-PC -Credential John-PC\John
```

```PowerShell
PS C:\> $RemoteReg

   NameSpace: ROOT\cimv2

Name                                Methods              Properties
----                                -------              ----------
StdRegProv                          {CreateKey, Delet... {}

PS C:\>
```

```PowerShell
PS C:\> $RemoteReg | Select-Object -ExpandProperty methods

Name          : CreateKey
InParameters  : System.Management.ManagementBaseObject
OutParameters : System.Management.ManagementBaseObject
Origin        : StdRegProv
Qualifiers    : {implemented, static}

Name          : DeleteKey
InParameters  : System.Management.ManagementBaseObject
OutParameters : System.Management.ManagementBaseObject
Origin        : StdRegProv
Qualifiers    : {implemented, static}

Name          : EnumKey
InParameters  : System.Management.ManagementBaseObject
OutParameters : System.Management.ManagementBaseObject
Origin        : StdRegProv
Qualifiers    : {implemented, static}

Name          : EnumValues
InParameters  : System.Management.ManagementBaseObject
OutParameters : System.Management.ManagementBaseObject
Origin        : StdRegProv
Qualifiers    : {implemented, static}

Name          : DeleteValue
InParameters  : System.Management.ManagementBaseObject
OutParameters : System.Management.ManagementBaseObject
Origin        : StdRegProv
Qualifiers    : {implemented, static}

Name          : SetDWORDValue
InParameters  : System.Management.ManagementBaseObject
OutParameters : System.Management.ManagementBaseObject
Origin        : StdRegProv
Qualifiers    : {implemented, static}

Name          : SetQWORDValue
InParameters  : System.Management.ManagementBaseObject
OutParameters : System.Management.ManagementBaseObject
Origin        : StdRegProv
Qualifiers    : {implemented, static}

Name          : GetDWORDValue
InParameters  : System.Management.ManagementBaseObject
OutParameters : System.Management.ManagementBaseObject
Origin        : StdRegProv
Qualifiers    : {implemented, static}

Name          : GetQWORDValue
InParameters  : System.Management.ManagementBaseObject
OutParameters : System.Management.ManagementBaseObject
Origin        : StdRegProv
Qualifiers    : {implemented, static}

Name          : SetStringValue
InParameters  : System.Management.ManagementBaseObject
OutParameters : System.Management.ManagementBaseObject
Origin        : StdRegProv
Qualifiers    : {implemented, static}

Name          : GetStringValue
InParameters  : System.Management.ManagementBaseObject
OutParameters : System.Management.ManagementBaseObject
Origin        : StdRegProv
Qualifiers    : {implemented, static}

Name          : SetMultiStringValue
InParameters  : System.Management.ManagementBaseObject
OutParameters : System.Management.ManagementBaseObject
Origin        : StdRegProv
Qualifiers    : {implemented, static}

Name          : GetMultiStringValue
InParameters  : System.Management.ManagementBaseObject
OutParameters : System.Management.ManagementBaseObject
Origin        : StdRegProv
Qualifiers    : {implemented, static}

Name          : SetExpandedStringValue
InParameters  : System.Management.ManagementBaseObject
OutParameters : System.Management.ManagementBaseObject
Origin        : StdRegProv
Qualifiers    : {implemented, static}

Name          : GetExpandedStringValue
InParameters  : System.Management.ManagementBaseObject
OutParameters : System.Management.ManagementBaseObject
Origin        : StdRegProv
Qualifiers    : {implemented, static}

Name          : SetBinaryValue
InParameters  : System.Management.ManagementBaseObject
OutParameters : System.Management.ManagementBaseObject
Origin        : StdRegProv
Qualifiers    : {implemented, static}

Name          : GetBinaryValue
InParameters  : System.Management.ManagementBaseObject
OutParameters : System.Management.ManagementBaseObject
Origin        : StdRegProv
Qualifiers    : {implemented, static}

Name          : CheckAccess
InParameters  : System.Management.ManagementBaseObject
OutParameters : System.Management.ManagementBaseObject
Origin        : StdRegProv
Qualifiers    : {implemented, static}

Name          : SetSecurityDescriptor
InParameters  : System.Management.ManagementBaseObject
OutParameters : System.Management.ManagementBaseObject
Origin        : StdRegProv
Qualifiers    : {implemented, Privileges, static}

Name          : GetSecurityDescriptor
InParameters  : System.Management.ManagementBaseObject
OutParameters : System.Management.ManagementBaseObject
Origin        : StdRegProv
Qualifiers    : {implemented, Privileges, static}

PS C:\>
```

[Hive](https://github.com/darkoperator/Posh-SecMod/blob/master/Registry/Registry.ps1) | Value
-----|-----------
HKCR | 2147483648
HKCU | 2147483649
HKLM | 2147483650
HKUS | 2147483651
HKCC | 2147483653

```PowerShell
PS C:\> $RemoteReg.GetStringValue(2147483650, "Software\Microsoft\Windows NT\CurrentVersion", "ProductName")

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
ReturnValue      : 0
sValue           : Windows 7 Ultimate
PSComputerName   :

PS C:\>
```

- ```.Net``` - ```[Microsoft.Win32.RegistryKey]```
    - [Can’t pass alternate credentials](http://psremoteregistry.codeplex.com/)

```PowerShell
PS C:\> [Microsoft.Win32.RegistryKey].GetMethods()

Name                       : Close
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663541
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : False
IsSecuritySafeCritical     : False
IsSecurityTransparent      : True
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : System.Void
ReturnTypeCustomAttributes : Void
ReturnParameter            : Void
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {}

Name                       : Flush
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663543
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : System.Void
ReturnTypeCustomAttributes : Void
ReturnParameter            : Void
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Security.SecuritySafeCriticalAttribute()]}

Name                       : Dispose
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663544
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : False
IsSecuritySafeCritical     : False
IsSecurityTransparent      : True
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, Final, Virtual, HideBySig, VtableLayoutMask
CallingConvention          : Standard, HasThis
ReturnType                 : System.Void
ReturnTypeCustomAttributes : Void
ReturnParameter            : Void
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : True
IsVirtual                  : True
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {}

Name                       : CreateSubKey
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663545
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : False
IsSecuritySafeCritical     : False
IsSecurityTransparent      : True
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : Microsoft.Win32.RegistryKey
ReturnTypeCustomAttributes : Microsoft.Win32.RegistryKey
ReturnParameter            : Microsoft.Win32.RegistryKey
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {}

Name                       : CreateSubKey
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663546
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : False
IsSecuritySafeCritical     : False
IsSecurityTransparent      : True
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : Microsoft.Win32.RegistryKey
ReturnTypeCustomAttributes : Microsoft.Win32.RegistryKey
ReturnParameter            : Microsoft.Win32.RegistryKey
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Runtime.InteropServices.ComVisibleAttribute((Boolean)False)]}

Name                       : CreateSubKey
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663547
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : False
IsSecuritySafeCritical     : False
IsSecurityTransparent      : True
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : Microsoft.Win32.RegistryKey
ReturnTypeCustomAttributes : Microsoft.Win32.RegistryKey
ReturnParameter            : Microsoft.Win32.RegistryKey
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Runtime.InteropServices.ComVisibleAttribute((Boolean)False)]}

Name                       : CreateSubKey
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663548
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : False
IsSecuritySafeCritical     : False
IsSecurityTransparent      : True
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : Microsoft.Win32.RegistryKey
ReturnTypeCustomAttributes : Microsoft.Win32.RegistryKey
ReturnParameter            : Microsoft.Win32.RegistryKey
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Runtime.InteropServices.ComVisibleAttribute((Boolean)False)]}

Name                       : CreateSubKey
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663549
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : False
IsSecuritySafeCritical     : False
IsSecurityTransparent      : True
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : Microsoft.Win32.RegistryKey
ReturnTypeCustomAttributes : Microsoft.Win32.RegistryKey
ReturnParameter            : Microsoft.Win32.RegistryKey
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Runtime.InteropServices.ComVisibleAttribute((Boolean)False)]}

Name                       : CreateSubKey
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663550
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : False
IsSecuritySafeCritical     : False
IsSecurityTransparent      : True
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : Microsoft.Win32.RegistryKey
ReturnTypeCustomAttributes : Microsoft.Win32.RegistryKey
ReturnParameter            : Microsoft.Win32.RegistryKey
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Runtime.InteropServices.ComVisibleAttribute((Boolean)False)]}

Name                       : CreateSubKey
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663551
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : False
IsSecuritySafeCritical     : False
IsSecurityTransparent      : True
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : Microsoft.Win32.RegistryKey
ReturnTypeCustomAttributes : Microsoft.Win32.RegistryKey
ReturnParameter            : Microsoft.Win32.RegistryKey
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Runtime.InteropServices.ComVisibleAttribute((Boolean)False)]}

Name                       : DeleteSubKey
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663553
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : False
IsSecuritySafeCritical     : False
IsSecurityTransparent      : True
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : System.Void
ReturnTypeCustomAttributes : Void
ReturnParameter            : Void
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {}

Name                       : DeleteSubKey
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663554
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : System.Void
ReturnTypeCustomAttributes : Void
ReturnParameter            : Void
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Security.SecuritySafeCriticalAttribute()]}

Name                       : DeleteSubKeyTree
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663555
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : False
IsSecuritySafeCritical     : False
IsSecurityTransparent      : True
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : System.Void
ReturnTypeCustomAttributes : Void
ReturnParameter            : Void
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {}

Name                       : DeleteSubKeyTree
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663556
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : System.Void
ReturnTypeCustomAttributes : Void
ReturnParameter            : Void
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Security.SecuritySafeCriticalAttribute()], [System.Runtime.InteropServices.ComVisibleAttribute((Boolean)False)]}

Name                       : DeleteValue
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663558
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : False
IsSecuritySafeCritical     : False
IsSecurityTransparent      : True
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : System.Void
ReturnTypeCustomAttributes : Void
ReturnParameter            : Void
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {}

Name                       : DeleteValue
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663559
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : System.Void
ReturnTypeCustomAttributes : Void
ReturnParameter            : Void
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Security.SecuritySafeCriticalAttribute()]}

Name                       : OpenBaseKey
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663562
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, Static, HideBySig
CallingConvention          : Standard
ReturnType                 : Microsoft.Win32.RegistryKey
ReturnTypeCustomAttributes : Microsoft.Win32.RegistryKey
ReturnParameter            : Microsoft.Win32.RegistryKey
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : True
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Security.SecuritySafeCriticalAttribute()], [System.Runtime.InteropServices.ComVisibleAttribute((Boolean)False)]}

Name                       : OpenRemoteBaseKey
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663563
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : False
IsSecuritySafeCritical     : False
IsSecurityTransparent      : True
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, Static, HideBySig
CallingConvention          : Standard
ReturnType                 : Microsoft.Win32.RegistryKey
ReturnTypeCustomAttributes : Microsoft.Win32.RegistryKey
ReturnParameter            : Microsoft.Win32.RegistryKey
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : True
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {}

Name                       : OpenRemoteBaseKey
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663564
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, Static, HideBySig
CallingConvention          : Standard
ReturnType                 : Microsoft.Win32.RegistryKey
ReturnTypeCustomAttributes : Microsoft.Win32.RegistryKey
ReturnParameter            : Microsoft.Win32.RegistryKey
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : True
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Runtime.InteropServices.ComVisibleAttribute((Boolean)False)], [System.Security.SecuritySafeCriticalAttribute()]}

Name                       : OpenSubKey
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663565
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : Microsoft.Win32.RegistryKey
ReturnTypeCustomAttributes : Microsoft.Win32.RegistryKey
ReturnParameter            : Microsoft.Win32.RegistryKey
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Security.SecuritySafeCriticalAttribute()]}

Name                       : OpenSubKey
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663566
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : Microsoft.Win32.RegistryKey
ReturnTypeCustomAttributes : Microsoft.Win32.RegistryKey
ReturnParameter            : Microsoft.Win32.RegistryKey
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Security.SecuritySafeCriticalAttribute()], [System.Runtime.InteropServices.ComVisibleAttribute((Boolean)False)]}

Name                       : OpenSubKey
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663567
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : Microsoft.Win32.RegistryKey
ReturnTypeCustomAttributes : Microsoft.Win32.RegistryKey
ReturnParameter            : Microsoft.Win32.RegistryKey
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Security.SecuritySafeCriticalAttribute()], [System.Runtime.InteropServices.ComVisibleAttribute((Boolean)False)]}

Name                       : OpenSubKey
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663568
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : Microsoft.Win32.RegistryKey
ReturnTypeCustomAttributes : Microsoft.Win32.RegistryKey
ReturnParameter            : Microsoft.Win32.RegistryKey
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Security.SecuritySafeCriticalAttribute()], [System.Runtime.InteropServices.ComVisibleAttribute((Boolean)False)]}

Name                       : OpenSubKey
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663571
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : False
IsSecuritySafeCritical     : False
IsSecurityTransparent      : True
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : Microsoft.Win32.RegistryKey
ReturnTypeCustomAttributes : Microsoft.Win32.RegistryKey
ReturnParameter            : Microsoft.Win32.RegistryKey
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {}

Name                       : get_SubKeyCount
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663572
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig, SpecialName
CallingConvention          : Standard, HasThis
ReturnType                 : System.Int32
ReturnTypeCustomAttributes : Int32
ReturnParameter            : Int32
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : True
IsConstructor              : False
CustomAttributes           : {[System.Security.SecuritySafeCriticalAttribute()]}

Name                       : get_View
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663573
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig, SpecialName
CallingConvention          : Standard, HasThis
ReturnType                 : Microsoft.Win32.RegistryView
ReturnTypeCustomAttributes : Microsoft.Win32.RegistryView
ReturnParameter            : Microsoft.Win32.RegistryView
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : True
IsConstructor              : False
CustomAttributes           : {[System.Security.SecuritySafeCriticalAttribute()]}

Name                       : get_Handle
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663574
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : False
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig, SpecialName, HasSecurity
CallingConvention          : Standard, HasThis
ReturnType                 : Microsoft.Win32.SafeHandles.SafeRegistryHandle
ReturnTypeCustomAttributes : Microsoft.Win32.SafeHandles.SafeRegistryHandle
ReturnParameter            : Microsoft.Win32.SafeHandles.SafeRegistryHandle
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : True
IsConstructor              : False
CustomAttributes           : {[System.Security.Permissions.SecurityPermissionAttribute()], [System.Security.SecurityCriticalAttribute()]}

Name                       : FromHandle
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663575
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : False
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, Static, HideBySig, HasSecurity
CallingConvention          : Standard
ReturnType                 : Microsoft.Win32.RegistryKey
ReturnTypeCustomAttributes : Microsoft.Win32.RegistryKey
ReturnParameter            : Microsoft.Win32.RegistryKey
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : True
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Security.Permissions.SecurityPermissionAttribute()], [System.Security.SecurityCriticalAttribute()],
                             [System.Runtime.InteropServices.ComVisibleAttribute((Boolean)False)]}

Name                       : FromHandle
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663576
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : False
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, Static, HideBySig, HasSecurity
CallingConvention          : Standard
ReturnType                 : Microsoft.Win32.RegistryKey
ReturnTypeCustomAttributes : Microsoft.Win32.RegistryKey
ReturnParameter            : Microsoft.Win32.RegistryKey
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : True
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Security.Permissions.SecurityPermissionAttribute()], [System.Runtime.InteropServices.ComVisibleAttribute((Boolean)False)],
                             [System.Security.SecurityCriticalAttribute()]}

Name                       : GetSubKeyNames
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663578
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : System.String[]
ReturnTypeCustomAttributes : System.String[]
ReturnParameter            : System.String[]
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Security.SecuritySafeCriticalAttribute()]}

Name                       : get_ValueCount
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663580
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig, SpecialName
CallingConvention          : Standard, HasThis
ReturnType                 : System.Int32
ReturnTypeCustomAttributes : Int32
ReturnParameter            : Int32
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : True
IsConstructor              : False
CustomAttributes           : {[System.Security.SecuritySafeCriticalAttribute()]}

Name                       : GetValueNames
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663582
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : System.String[]
ReturnTypeCustomAttributes : System.String[]
ReturnParameter            : System.String[]
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Security.SecuritySafeCriticalAttribute()]}

Name                       : GetValue
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663583
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : System.Object
ReturnTypeCustomAttributes : System.Object
ReturnParameter            : System.Object
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Security.SecuritySafeCriticalAttribute()]}

Name                       : GetValue
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663584
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : System.Object
ReturnTypeCustomAttributes : System.Object
ReturnParameter            : System.Object
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Security.SecuritySafeCriticalAttribute()]}

Name                       : GetValue
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663585
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : System.Object
ReturnTypeCustomAttributes : System.Object
ReturnParameter            : System.Object
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Runtime.InteropServices.ComVisibleAttribute((Boolean)False)], [System.Security.SecuritySafeCriticalAttribute()]}

Name                       : GetValueKind
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663587
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : Microsoft.Win32.RegistryValueKind
ReturnTypeCustomAttributes : Microsoft.Win32.RegistryValueKind
ReturnParameter            : Microsoft.Win32.RegistryValueKind
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Runtime.InteropServices.ComVisibleAttribute((Boolean)False)], [System.Security.SecuritySafeCriticalAttribute()]}

Name                       : get_Name
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663592
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig, SpecialName
CallingConvention          : Standard, HasThis
ReturnType                 : System.String
ReturnTypeCustomAttributes : System.String
ReturnParameter            : System.String
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : True
IsConstructor              : False
CustomAttributes           : {[System.Security.SecuritySafeCriticalAttribute()]}

Name                       : SetValue
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663594
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : False
IsSecuritySafeCritical     : False
IsSecurityTransparent      : True
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : System.Void
ReturnTypeCustomAttributes : Void
ReturnParameter            : Void
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {}

Name                       : SetValue
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663595
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : System.Void
ReturnTypeCustomAttributes : Void
ReturnParameter            : Void
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Runtime.InteropServices.ComVisibleAttribute((Boolean)False)], [System.Security.SecuritySafeCriticalAttribute()]}

Name                       : ToString
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663597
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, Virtual, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : System.String
ReturnTypeCustomAttributes : System.String
ReturnParameter            : System.String
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : True
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Security.SecuritySafeCriticalAttribute()]}

Name                       : GetAccessControl
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663598
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : False
IsSecuritySafeCritical     : False
IsSecurityTransparent      : True
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : System.Security.AccessControl.RegistrySecurity
ReturnTypeCustomAttributes : System.Security.AccessControl.RegistrySecurity
ReturnParameter            : System.Security.AccessControl.RegistrySecurity
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {}

Name                       : GetAccessControl
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663599
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : System.Security.AccessControl.RegistrySecurity
ReturnTypeCustomAttributes : System.Security.AccessControl.RegistrySecurity
ReturnParameter            : System.Security.AccessControl.RegistrySecurity
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Security.SecuritySafeCriticalAttribute()]}

Name                       : SetAccessControl
DeclaringType              : Microsoft.Win32.RegistryKey
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663600
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : System.Void
ReturnTypeCustomAttributes : Void
ReturnParameter            : Void
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Security.SecuritySafeCriticalAttribute()]}

Name                       : GetLifetimeService
DeclaringType              : System.MarshalByRefObject
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100667337
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : False
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, Final, Virtual, HideBySig, VtableLayoutMask
CallingConvention          : Standard, HasThis
ReturnType                 : System.Object
ReturnTypeCustomAttributes : System.Object
ReturnParameter            : System.Object
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : True
IsVirtual                  : True
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Security.SecurityCriticalAttribute()]}

Name                       : InitializeLifetimeService
DeclaringType              : System.MarshalByRefObject
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100667338
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : False
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, Virtual, HideBySig, VtableLayoutMask
CallingConvention          : Standard, HasThis
ReturnType                 : System.Object
ReturnTypeCustomAttributes : System.Object
ReturnParameter            : System.Object
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : True
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Security.SecurityCriticalAttribute()]}

Name                       : CreateObjRef
DeclaringType              : System.MarshalByRefObject
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100667339
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : False
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, Virtual, HideBySig, VtableLayoutMask
CallingConvention          : Standard, HasThis
ReturnType                 : System.Runtime.Remoting.ObjRef
ReturnTypeCustomAttributes : System.Runtime.Remoting.ObjRef
ReturnParameter            : System.Runtime.Remoting.ObjRef
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : True
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Security.SecurityCriticalAttribute()]}

Name                       : Equals
DeclaringType              : System.Object
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663839
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : False
IsSecuritySafeCritical     : False
IsSecurityTransparent      : True
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, Virtual, HideBySig, VtableLayoutMask
CallingConvention          : Standard, HasThis
ReturnType                 : System.Boolean
ReturnTypeCustomAttributes : Boolean
ReturnParameter            : Boolean
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : True
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[__DynamicallyInvokableAttribute()]}

Name                       : GetHashCode
DeclaringType              : System.Object
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663842
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : False
IsSecuritySafeCritical     : False
IsSecurityTransparent      : True
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, Virtual, HideBySig, VtableLayoutMask
CallingConvention          : Standard, HasThis
ReturnType                 : System.Int32
ReturnTypeCustomAttributes : Int32
ReturnParameter            : Int32
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : IL
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : True
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[__DynamicallyInvokableAttribute()]}

Name                       : GetType
DeclaringType              : System.Object
ReflectedType              : Microsoft.Win32.RegistryKey
MemberType                 : Method
MetadataToken              : 100663843
Module                     : CommonLanguageRuntimeLibrary
IsSecurityCritical         : True
IsSecuritySafeCritical     : True
IsSecurityTransparent      : False
MethodHandle               : System.RuntimeMethodHandle
Attributes                 : PrivateScope, Public, HideBySig
CallingConvention          : Standard, HasThis
ReturnType                 : System.Type
ReturnTypeCustomAttributes : System.Type
ReturnParameter            : System.Type
IsGenericMethod            : False
IsGenericMethodDefinition  : False
ContainsGenericParameters  : False
MethodImplementationFlags  : InternalCall
IsPublic                   : True
IsPrivate                  : False
IsFamily                   : False
IsAssembly                 : False
IsFamilyAndAssembly        : False
IsFamilyOrAssembly         : False
IsStatic                   : False
IsFinal                    : False
IsVirtual                  : False
IsHideBySig                : True
IsAbstract                 : False
IsSpecialName              : False
IsConstructor              : False
CustomAttributes           : {[System.Security.SecuritySafeCriticalAttribute()], [__DynamicallyInvokableAttribute()]}

PS C:\>
```

- [```Posh-SecMod```](https://github.com/darkoperator/Posh-SecMod) [```Registry```](https://github.com/darkoperator/Posh-SecMod/tree/master/Registry) module

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-SecMod-master> ls

    Directory: C:\Users\Administrator\Desktop\Posh-SecMod-master


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----          7/9/2017   5:32 PM            Assemblies
d----          7/9/2017   5:32 PM            Audit
d----          7/9/2017   5:32 PM            Database
d----          7/9/2017   5:32 PM            Discovery
d----          7/9/2017   5:32 PM            Parse
d----          7/9/2017   5:32 PM            PostExploitation
d----          7/9/2017   5:32 PM            Registry
d----          7/9/2017   5:32 PM            Utility
-----         8/12/2015   8:31 AM        483 .gitattributes
-----         8/12/2015   8:31 AM       1970 .gitignore
-----         8/12/2015   8:31 AM      12840 LICENSE.txt
-----         8/12/2015   8:31 AM       5554 Posh-SecMod.psd1
-----         8/12/2015   8:31 AM        751 Posh-SecMod.psm1
-----         8/12/2015   8:31 AM       1889 README.md


PS C:\Users\Administrator\Desktop\Posh-SecMod-master>
```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-SecMod-master> cd .\Registry
```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry> ls

    Directory: C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
-----         8/12/2015   8:31 AM      27860 Registry.ps1
-----         8/12/2015   8:31 AM      27864 Registry.psm1

PS C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry> 
```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry> Import-Module .\Registry.psm1
```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry> Get-Module

ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Manifest   3.1.0.0    Microsoft.PowerShell.Management     {Add-Computer, Add-Content, Checkpoint-Computer, Clear-Content...}
Manifest   3.1.0.0    Microsoft.PowerShell.Utility        {Add-Member, Add-Type, Clear-Variable, Compare-Object...}
Script     0.0        Registry                            {Get-RegKeys, Get-RegKeySecurityDescriptor, Get-RegValue, Get-RegValues...}

PS C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry>
```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry> Get-Command -Module Registry

CommandType     Name                                               ModuleName
-----------     ----                                               ----------
Function        Get-RegKeys                                        Registry
Function        Get-RegKeySecurityDescriptor                       Registry
Function        Get-RegValue                                       Registry
Function        Get-RegValues                                      Registry
Function        New-RegKey                                         Registry
Function        Remove-RegKey                                      Registry
Function        Remove-RegValue                                    Registry
Function        Set-RegValue                                       Registry
Function        Test-RegKeyAccess                                  Registry

PS C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry>
```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry> Get-Help Get-RegKeys -Examples

NAME
    Get-RegKeys

SYNOPSIS
    Enumerates the keys that are under a given Registry Key.

    -------------------------- EXAMPLE 1 --------------------------

    C:\PS>Listing all of the keys under HKCU\Software key


    PS C:\> Get-RegKeys -Hive HKCU -Key software

     Key                                                                  FullPath
     ---                                                                  --------
     7-Zip                                                                HKCU\software\7-Zip
     AppDataLow                                                           HKCU\software\AppDataLow
     Macromedia                                                           HKCU\software\Macromedia
     Microsoft                                                            HKCU\software\Microsoft
     Microsoft Corporation                                                HKCU\software\Microsoft Corporation
     Mine                                                                 HKCU\software\Mine
     Policies                                                             HKCU\software\Policies
     RegisteredApplications                                               HKCU\software\RegisteredApplications
     ThinPrint                                                            HKCU\software\ThinPrint
     VMware, Inc.                                                         HKCU\software\VMware, Inc.
     Wow6432Node                                                          HKCU\software\Wow6432Node
     Classes                                                              HKCU\software\Classes

PS C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry>
```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry> Get-Help Get-RegKeySecurityDescriptor -Examples

NAME
    Get-RegKeySecurityDescriptor

SYNOPSIS
    Gets the Security DACL and Owner of a given Registry Key.

    -------------------------- EXAMPLE 1 --------------------------

    C:\PS>Get the DACL for the SAM key in HKLM


    PS C:\> Get-RegKeySecurityDescriptor -Hive HKlm -Key sam

     Trustee                                                                                                              Permission

     -------                                                                                                              ----------

     BUILTIN\Administrators                                                                                               Owner

     BUILTIN\Users                                                                                                        Read Access

     BUILTIN\Administrators                                                                                               All Access

     NT AUTHORITY\SYSTEM                                                                                                  All Access

     \CREATOR OWNER                                                                                                       All Access

     APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES                                                               Read Access

PS C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry>
```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry> Get-Help Get-RegValue -Examples

NAME
    Get-RegValue

SYNOPSIS
    Retrives a the content of a specified value in a given key.

    -------------------------- EXAMPLE 1 --------------------------

    C:\PS>Getting the Windows Version fromt the registry


    PS C:\> Get-RegValue -Hive HKLM -key "SOFTWARE\Microsoft\Windows NT\CurrentVersion" -Name ProductName
    Windows 8 Enterprise




    -------------------------- EXAMPLE 2 --------------------------

    C:\PS>Read registry binary data and turn it in to ASCII String


    PS C:\> $bindata = Get-RegValue -Hive HKCU -Key _deleteme -Name binval
    PS C:\> ([System.Text.Encoding]::ASCII).GetString($bindata)
    PowerShell

    PS C:\Wind

PS C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry>
```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry> Get-Help New-RegKey -Examples

NAME
    New-RegKey

SYNOPSIS
    Creates a registry key under a given Registry Key.

    -------------------------- EXAMPLE 1 --------------------------

    C:\PS>Create a key named _deleteme under the registry HKCU key.


    PS C:\> New-RegKey -Hive HKCU -Key _deleteme -Verbose
    VERBOSE: Key HKCU\_deleteme was created.

PS C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry>
```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry> Get-Help Remove-RegKey -Examples

NAME
    Remove-RegKey

SYNOPSIS
    Removes a registry key under a given Registry Key.

    -------------------------- EXAMPLE 1 --------------------------

    C:\PS>Remove a key named _deleteme under the registry HKCU key.


    PS C:\> Remove-RegKey -Hive HKCU -Key _deleteme -Verbose
    VERBOSE: Key HKCU\_deleteme was removed.

PS C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry>
```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry> Get-Help Remove-RegValue -Examples

NAME
    Remove-RegValue

SYNOPSIS
    Removes a specified value in a given key.

    -------------------------- EXAMPLE 1 --------------------------

    C:\PS>Removing a value from the registry


    PS C:\> Remove-RegValue -Hive HKCU -Key _deleteme -Name dworval -Verbose
    VERBOSE: Value dworval has been removed.

PS C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry>
```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry> Get-Help Set-RegValue -Examples

NAME
    Set-RegValue

SYNOPSIS
    Set a value on a given key.

    -------------------------- EXAMPLE 1 --------------------------

    C:\PS>set a SZ value.


    PS C:\> Set-RegValue -Hive HKCU -Key _deleteme -Name stringval -Type SZ -Data "data" -Verbose
    VERBOSE: Value set on HKCU\_deletme\stringval of type SZ




    -------------------------- EXAMPLE 2 --------------------------

    C:\PS>Set a MULTISZ value.


    PS C:\> Set-RegValue -Hive HKCU -Key _deleteme -Name multistring -Type MULTISZ -Data "str1","str2","str3" -Verbose
    VERBOSE: Value set on HKCU\_deletme\multistring of type MULTISZ




    -------------------------- EXAMPLE 3 --------------------------

    C:\PS>Set a QWORD value.


    PS C:\> Set-RegValue -Hive HKCU -Key _deleteme -Name qval -Type QWORD -Data 4060 -Verbose
    VERBOSE: Value set on HKCU\_deletme\qval of type QWORD




    -------------------------- EXAMPLE 4 --------------------------

    C:\PS>Set a EXPANDSZ value.


    PS C:\> Set-RegValue -Hive HKCU -Key _deleteme -Name expanval -Type EXPANDSZ -Data "%envvar%" -Verbose
    VERBOSE: Value set on HKCU\_deletme\expanval of type EXPANDSZ




    -------------------------- EXAMPLE 5 --------------------------

    C:\PS>Set a DWORD value.


    PS C:\> Set-RegValue -Hive HKCU -Key _deleteme -Name dworval -Type DWORD -Data 10 -Verbose
    VERBOSE: Value set on HKCU\_deletme\dworval of type DWORD




    -------------------------- EXAMPLE 6 --------------------------

    C:\PS>Set a Binary value.


    PS C:\> Set-RegValue -Hive HKCU -Key _deleteme -Name binval -Type BINARY -Data @([char[]]'PowerShell') -Verbose
    VERBOSE: Value set on HKCU\_deletme\binval of type BINARY

PS C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry>
```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry> Get-Help Test-RegKeyAccess -Examples

NAME
    Test-RegKeyAccess

SYNOPSIS
    Checks for specific access type on a given registry key.

    -------------------------- EXAMPLE 1 --------------------------

    PS C:\>Test-RegKeyAccess -Hive hkcu -Key software -AccessType DELETE


    True

PS C:\Users\Administrator\Desktop\Posh-SecMod-master\Registry>
```

###### Exercise

- Try the ```Macro Security script``` from previous exercise on a remote computer.
