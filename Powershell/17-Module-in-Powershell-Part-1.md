#### 17. Module in Powershell Part 1

###### Modules

- Help topic for ```module```

```PowerShell
PS C:\Users\Windows10-32> Get-Help *module*

Name                              Category  Module                    Synopsis
----                              --------  ------                    --------
ImportSystemModules               Function                            ...
Export-ModuleMember               Cmdlet    Microsoft.PowerShell.Core ...
Get-Module                        Cmdlet    Microsoft.PowerShell.Core ...
Import-Module                     Cmdlet    Microsoft.PowerShell.Core ...
New-Module                        Cmdlet    Microsoft.PowerShell.Core ...
New-ModuleManifest                Cmdlet    Microsoft.PowerShell.Core ...
Remove-Module                     Cmdlet    Microsoft.PowerShell.Core ...
Test-ModuleManifest               Cmdlet    Microsoft.PowerShell.Core ...
InModuleScope                     Function  Pester                    ...
Uninstall-Module                  Function  PowerShellGet             ...
Install-Module                    Function  PowerShellGet             ...
Publish-Module                    Function  PowerShellGet             ...
Update-ModuleManifest             Function  PowerShellGet             ...
Save-Module                       Function  PowerShellGet             ...
Update-Module                     Function  PowerShellGet             ...
Get-InstalledModule               Function  PowerShellGet             ...
Find-Module                       Function  PowerShellGet             ...


PS C:\Users\Windows10-32>
```

- Listing Modules

```PowerShell
PS C:\Users\Windows10-32> Get-Module -ListAvailable -All


    Directory: C:\Program Files\WindowsPowerShell\Modules\Microsoft.PowerShell.Operation.Validation\1.0.1\Test\Modules


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Manifest   1.0.1      Example2.Diagnostics


    Directory: C:\Program Files\WindowsPowerShell\Modules


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Binary     0.0.0.0    Microsoft.PackageManagement
Binary     0.0.0.0    Microsoft.PackageManagement.Arch...
Binary     0.0.0.0    Microsoft.PackageManagement.Core...
Binary     0.0.0.0    Microsoft.PackageManagement.Meta...
Binary     0.0.0.0    Microsoft.PackageManagement.MsiP...
Binary     0.0.0.0    Microsoft.PackageManagement.MsuP...
Script     1.0.1      Microsoft.PowerShell.Operation.V... {Get-OperationValidation, Invoke-OperationValidation}
Script     1.0.1      Microsoft.PowerShell.Operation.V... {Get-OperationValidation, Invoke-OperationValidation}
Binary     3.0.0.0    Microsoft.PowerShell.PackageMana... {Find-Package, Get-Package, Get-PackageProvider, Get-PackageSource...}
Binary     3.0.0.0    Microsoft.PowerShell.PSReadline     {Get-PSReadlineOption, Set-PSReadlineOption, Set-PSReadlineKeyHandler, Get-PSReadlineKeyHandler...}
Manifest   0.0        OperationValidationResources
Binary     1.0.0.1    PackageManagement                   {Find-Package, Get-Package, Get-PackageProvider, Get-PackageSource...}
Script     0.0        PackageProviderFunctions            {Write-Debug, Write-Error, Write-Progress, Write-Verbose...}
Script     3.4.0      Pester                              {Describe, Context, It, Should...}
Script     3.4.0      Pester                              {Describe, Context, It, Should...}
Script     1.0.0.1    PowerShellGet                       {Install-Module, Find-Module, Save-Module, Update-Module...}
Script     1.0.0.1    PowerShellGet                       {Install-Module, Find-Module, Save-Module, Update-Module...}
Manifest   0.0        PSGet.Resource
Script     1.2        PSReadline                          {Get-PSReadlineKeyHandler, Set-PSReadlineKeyHandler, Remove-PSReadlineKeyHandler, Get-PSReadlineOption...}
Script     0.0        PSReadline                          {Get-PSReadlineOption, Set-PSReadlineKeyHandler, Get-PSReadlineKeyHandler, Set-PSReadlineOption...}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Manifest   1.0.0.0    AppBackgroundTask                   {Disable-AppBackgroundTaskDiagnosticLog, Enable-AppBackgroundTaskDiagnosticLog, Set-AppBackgroundTaskResourcePolicy, Unregister-AppBackground...
Manifest   2.0.0.0    AppLocker                           {Get-AppLockerFileInformation, Get-AppLockerPolicy, New-AppLockerPolicy, Set-AppLockerPolicy...}
Manifest   1.0.0.0    AppvClient                          {Add-AppvClientConnectionGroup, Add-AppvClientPackage, Add-AppvPublishingServer, Disable-Appv...}
Script     0.0        AppVClientCmdlets                   {Get-AppvVirtualProcess, Start-AppvVirtualProcess}
Manifest   2.0.0.0    Appx                                {Add-AppxPackage, Get-AppxPackage, Get-AppxPackageManifest, Remove-AppxPackage...}
Script     0.0        Appx                                {Get-AppxLastError, Get-AppxLog}
Script     1.0.0.0    AssignedAccess                      {Clear-AssignedAccess, Get-AssignedAccess, Set-AssignedAccess}
Script     0.0        AssignedAccess                      {Get-AssignedAccess, Set-AssignedAccess, Clear-AssignedAccess}
Manifest   1.0.0.0    BitLocker                           {Unlock-BitLocker, Suspend-BitLocker, Resume-BitLocker, Remove-BitLockerKeyProtector...}
Script     1.0.0.0    BitLocker                           {Unlock-BitLocker, Suspend-BitLocker, Resume-BitLocker, Remove-BitLockerKeyProtector...}
Manifest   2.0.0.0    BitsTransfer                        {Add-BitsFile, Complete-BitsTransfer, Get-BitsTransfer, Remove-BitsTransfer...}
Manifest   1.0.0.0    BranchCache                         {Add-BCDataCacheExtension, Clear-BCCache, Disable-BC, Disable-BCDowngrading...}
Cim        1.0.0      BranchCacheClientSettingData        Get-BCClientConfiguration
Cim        1.0.0      BranchCacheContentServerSettingData Get-BCContentServerConfiguration
Cim        1.0.0      BranchCacheHostedCacheServerSett... Get-BCHostedCacheServerConfiguration
Cim        1.0.0      BranchCacheNetworkSettingData       Get-BCNetworkConfiguration
Cim        1.0.0      BranchCacheOrchestrator             {Add-BCDataCacheExtension, Clear-BCCache, Disable-BC, Disable-BCDowngrading...}
Cim        1.0.0      BranchCachePrimaryPublicationCac... Get-BCHashCache
Cim        1.0.0      BranchCachePrimaryRepublicationC... Get-BCDataCache
Cim        1.0.0      BranchCacheSecondaryRepublicatio... Get-BCDataCacheExtension
Cim        1.0.0      BranchCacheStatus                   Get-BCStatus
Cim        1.0        CIM_PhysicalComputerSystemView      {Get-PcsvDevice, Start-PcsvDevice, Stop-PcsvDevice, Restart-PcsvDevice...}
Manifest   1.0.0.0    CimCmdlets                          {Get-CimAssociatedInstance, Get-CimClass, Get-CimInstance, Get-CimSession...}
Script     0.0        CmdletHelpers                       {CmdletShouldProcess, Get-NetworkSwitchRegisteredProfileFromNamespace, Get-NetworkSwitchImplementationNamespace, New-LocalCimInstance...}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules\PSDesiredStateConfiguration


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Script     0.0        CompositeResourceHelper             {BuildResourceCommonParameters, BuildResourceString}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Manifest   1.0        ConfigCI                            {Get-SystemDriver, New-CIPolicyRule, New-CIPolicy, Get-CIPolicy...}
Manifest   1.0        Defender                            {Get-MpPreference, Set-MpPreference, Add-MpPreference, Remove-MpPreference...}
Manifest   1.0.0.0    DirectAccessClientComponents        {Disable-DAManualEntryPointSelection, Enable-DAManualEntryPointSelection, Get-DAClientExperienceConfiguration, Get-DAEntryPointTableItem...}
Cim        2.0.0.0    Disable-DscDebug                    Disable-DscDebug
Cim        1.0.0.0    Disk                                {Get-Disk, Initialize-Disk, Clear-Disk, New-Partition...}
Cim        1.0.0.0    DiskImage                           {Get-DiskImage, Mount-DiskImage, Dismount-DiskImage}
Script     3.0        Dism                                {Add-AppxProvisionedPackage, Add-WindowsDriver, Add-WindowsCapability, Add-WindowsImage...}
Script     3.0        Dism                                {Add-AppxProvisionedPackage, Add-WindowsDriver, Add-WindowsCapability, Add-WindowsImage...}
Manifest   1.0.0.0    DnsClient                           {Resolve-DnsName, Clear-DnsClientCache, Get-DnsClient, Get-DnsClientCache...}
Binary     10.0.0.0   dnslookup                           Resolve-DnsName


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules\PSDesiredStateConfiguration\DownloadManager


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Manifest   1.0        DSCFileDownloadManager              {Get-DscAction, Get-DSCDocument, Get-DSCModule}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules\PSDesiredStateConfiguration


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Script     0.0        DSCResourceHelper                   IsNanoServer


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Cim        2.0.0.0    Enable-DscDebug                     Enable-DscDebug
Manifest   1.0.0.0    EventTracingManagement              {New-EtwTraceSession, Get-EtwTraceSession, Set-EtwTraceSession, Send-EtwTraceSession...}
Cim        1.0.0.0    FileIntegrity                       {Get-FileIntegrity, Set-FileIntegrity, Repair-FileIntegrity}
Cim        1.0.0.0    FileServer                          {Get-StorageFileServer, Remove-StorageFileServer, Set-StorageFileServer, New-FileShare}
Cim        1.0.0.0    FileShare                           {Get-FileShare, Remove-FileShare, Grant-FileShareAccess, Block-FileShareAccess...}
Cim        1.0.0.0    FileStorageTier                     {Get-FileStorageTier, Set-FileStorageTier, Clear-FileStorageTier}
Cim        2.0.0.0    Get-DscConfiguration                Get-DscConfiguration
Cim        2.0.0.0    Get-DscConfigurationStatus          Get-DscConfigurationStatus
Cim        2.0.0.0    Get-DSCLocalConfigurationManager    Get-DscLocalConfigurationManager
Script     0.0        GetStartApps                        {Get-StartApps, Get-AllStartApps}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules\PSDesiredStateConfiguration\DSCResources


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Script     1.0        GroupSet                            {BuildResourceCommonParameters, BuildResourceString}
Script     1.0        GroupSet                            {BuildResourceCommonParameters, BuildResourceString}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Cim        1.0.0.0    InitiatorId                         {Get-InitiatorId, Remove-InitiatorId}
Cim        1.0.0.0    InitiatorPort                       {Get-InitiatorPort, Set-InitiatorPort}
Manifest   2.0.0.0    International                       {Get-WinDefaultInputMethodOverride, Set-WinDefaultInputMethodOverride, Get-WinHomeLocation, Set-WinHomeLocation...}
Manifest   1.0.0.0    iSCSI                               {Get-IscsiTargetPortal, New-IscsiTargetPortal, Remove-IscsiTargetPortal, Update-IscsiTargetPortal...}
Cim        1.0        iSCSIConnection                     Get-IscsiConnection
Cim        1.0        iSCSISession                        {Get-IscsiSession, Unregister-IscsiSession, Register-IscsiSession, Set-IscsiChapSecret}
Cim        1.0        iSCSITarget                         {Get-IscsiTarget, Disconnect-IscsiTarget, Update-IscsiTarget, Connect-IscsiTarget}
Cim        1.0        iSCSITargetPortal                   {Get-IscsiTargetPortal, Remove-IscsiTargetPortal, Update-IscsiTargetPortal, New-IscsiTargetPortal}
Script     1.0.0.0    ise                                 {New-IseSnippet, Import-IseSnippet, Get-IseSnippet}
Script     0.0        ise                                 {Import-IseSnippet, Get-IseSnippet, New-IseSnippet}
Manifest   1.0.0.0    Kds                                 {Add-KdsRootKey, Get-KdsRootKey, Test-KdsRootKey, Set-KdsConfiguration...}
Cim        1.0.0.0    MaskingSet                          {Get-MaskingSet, Remove-MaskingSet, Rename-MaskingSet, Add-InitiatorIdToMaskingSet...}
Binary     10.0.0.0   Microsoft.AppV.AppvClientComCons...
Binary     10.0.0.0   Microsoft.AppV.AppVClientPowerShell {Add-AppvClientConnectionGroup, Add-AppvClientPackage, Add-AppvPublishingServer, Disable-Appv...}
Binary     0.0.0.0    Microsoft.AppV.ClientProgrammabi...
Binary     0.0.0.0    Microsoft.BackgroundIntelligentT...
Binary     0.0.0.0    Microsoft.BitLocker.Structures
Binary     10.0.0.0   Microsoft.Dism.PowerShell           {Add-WindowsPackage, Remove-WindowsPackage, Get-WindowsPackage, Enable-WindowsOptionalFeature...}
Manifest   1.0.1.0    Microsoft.PowerShell.Archive        {Compress-Archive, Expand-Archive}
Script     0.0        Microsoft.PowerShell.Archive        {Compress-Archive, Expand-Archive, GetResolvedPathHelper, Add-CompressionAssemblies...}
Manifest   3.0.0.0    Microsoft.PowerShell.Diagnostics    {Get-WinEvent, Get-Counter, Import-Counter, Export-Counter...}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules\PSDesiredStateConfiguration\DownloadManager


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Binary     3.0.0.0    Microsoft.PowerShell.DSC.FileDow... {Get-DscAction, Get-DSCDocument, Get-DSCModule}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Manifest   3.0.0.0    Microsoft.PowerShell.Host           {Start-Transcript, Stop-Transcript}
Binary     3.0.0.0    Microsoft.PowerShell.LocalAccounts  {Add-LocalGroupMember, Disable-LocalUser, Enable-LocalUser, Get-LocalGroup...}
Manifest   1.0.0.0    Microsoft.PowerShell.LocalAccounts  {Add-LocalGroupMember, Disable-LocalUser, Enable-LocalUser, Get-LocalGroup...}
Manifest   3.1.0.0    Microsoft.PowerShell.Management     {Add-Content, Clear-Content, Clear-ItemProperty, Join-Path...}
Script     1.0        Microsoft.PowerShell.ODataUtils     Export-ODataEndpointProxy
Script     1.0        Microsoft.PowerShell.ODataUtils     Export-ODataEndpointProxy
Manifest   3.0.0.0    Microsoft.PowerShell.Security       {Get-Acl, Set-Acl, Get-PfxCertificate, Get-Credential...}
Manifest   3.1.0.0    Microsoft.PowerShell.Utility        {Format-List, Format-Custom, Format-Table, Format-Wide...}
Script     0.0        Microsoft.PowerShell.Utility        {Get-FileHash, New-TemporaryFile, New-Guid, Format-Hex...}
Binary     10.0.0.0   Microsoft.Uev.Commands              {Clear-UevConfiguration, Clear-UevAppxPackage, Restore-UevBackup, Set-UevTemplateProfile...}
Binary     10.0.0.0   Microsoft.Windows.AppBackgroundT... {Enable-AppBackgroundTaskDiagnosticLog, Disable-AppBackgroundTaskDiagnosticLog, Set-AppBackgroundTaskResourcePolicy}
Binary     10.0.0.0   Microsoft.Windows.Firewall.Commands {New-NetIPsecAuthProposal, New-NetIPsecMainModeCryptoProposal, New-NetIPsecQuickModeCryptoProposal, Get-DAPolicyChange}
Binary     10.0.0.0   Microsoft.WindowsErrorReporting.... {Enable-WindowsErrorReporting, Disable-WindowsErrorReporting, Get-WindowsErrorReporting}
Binary     10.0.0.0   Microsoft.WindowsSearch.Commands    {Get-WindowsSearchSetting, Set-WindowsSearchSetting}
Manifest   3.0.0.0    Microsoft.WSMan.Management          {Disable-WSManCredSSP, Enable-WSManCredSSP, Get-WSManCredSSP, Set-WSManQuickConfig...}
Manifest   1.0        MMAgent                             {Disable-MMAgent, Enable-MMAgent, Set-MMAgent, Get-MMAgent...}
Manifest   1.0.0.0    MsDtc                               {New-DtcDiagnosticTransaction, Complete-DtcDiagnosticTransaction, Join-DtcDiagnosticResourceManager, Receive-DtcDiagnosticTransaction...}
Cim        1.0        MSFT_3DPrinter_v1.0


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules\PSDesiredStateConfiguration\DSCResources


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Script     0.0        MSFT_ArchiveResource                {Test-TargetResource, Set-TargetResource, Get-TargetResource}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Cim        1.0.0.0    MSFT_AutologgerConfig_v1.0          {Get-AutologgerConfig, Set-AutologgerConfig, Remove-AutologgerConfig, New-AutologgerConfig}
Cim        1.0        MSFT_DAClientExperienceConfigura... {Get-DAClientExperienceConfiguration, Set-DAClientExperienceConfiguration, Reset-DAClientExperienceConfiguration}
Cim        1.0        MSFT_DAConnectionStatus             Get-DAConnectionStatus
Cim        1.0        MSFT_DASiteTableEntry               {Get-DAEntryPointTableItem, Set-DAEntryPointTableItem, Remove-DAEntryPointTableItem, Reset-DAEntryPointTableItem...}
Cim        1.0.0      MSFT_DnsClient                      {Get-DnsClient, Set-DnsClient, Register-DnsClient}
Cim        1.0.0      MSFT_DnsClientCache                 {Get-DnsClientCache, Clear-DnsClientCache}
Cim        1.0.0      MSFT_DnsClientGlobalSetting         {Get-DnsClientGlobalSetting, Set-DnsClientGlobalSetting}
Cim        1.0.0      MSFT_DnsClientServerAddress         {Get-DnsClientServerAddress, Set-DnsClientServerAddress}
Cim        1.0        MSFT_DtcAdvancedHostSettingTask_... {Get-DtcAdvancedHostSetting, Set-DtcAdvancedHostSetting}
Cim        1.0        MSFT_DtcAdvancedSettingTask_v1.0    {Get-DtcAdvancedSetting, Set-DtcAdvancedSetting}
Cim        1.0        MSFT_DtcClusterDefaultTask_v1.0     {Get-DtcClusterDefault, Set-DtcClusterDefault}
Cim        1.0        MSFT_DtcClusterTMMappingTask_v1.0   {Add-DtcClusterTMMapping, Get-DtcClusterTMMapping, Remove-DtcClusterTMMapping, Set-DtcClusterTMMapping}
Cim        1.0        MSFT_DtcDefaultTask_v1.0            {Get-DtcDefault, Set-DtcDefault}
Cim        1.0        MSFT_DtcLogTask_v1.0                {Get-DtcLog, Reset-DtcLog, Set-DtcLog}
Cim        1.0        MSFT_DtcNetworkSettingTask_v1.0     {Get-DtcNetworkSetting, Set-DtcNetworkSetting}
Cim        1.0        MSFT_DtcTask_v1.0                   {Get-Dtc, Install-Dtc, Start-Dtc, Stop-Dtc...}
Cim        1.0        MSFT_DtcTransactionsStatisticsTa... Get-DtcTransactionsStatistics
Cim        1.0        MSFT_DtcTransactionsTraceSession... {Get-DtcTransactionsTraceSession, Set-DtcTransactionsTraceSession, Start-DtcTransactionsTraceSession, Stop-DtcTransactionsTraceSession...}
Cim        1.0        MSFT_DtcTransactionsTraceSetting... {Get-DtcTransactionsTraceSetting, Set-DtcTransactionsTraceSetting}
Cim        1.0        MSFT_DtcTransactionTask_v1.0        {Get-DtcTransaction, Set-DtcTransaction}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules\PSDesiredStateConfiguration\DSCResources


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Script     0.0        MSFT_EnvironmentResource            {Get-TargetResource, Set-TargetResource, Test-TargetResource}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Cim        1.0.0.0    MSFT_EtwTraceProvider_v1.0          {Get-EtwTraceProvider, Set-EtwTraceProvider, Remove-EtwTraceProvider, Add-EtwTraceProvider}
Cim        1.0.0.0    MSFT_EtwTraceSession_v1.0           {Get-EtwTraceSession, Remove-EtwTraceSession, Set-EtwTraceSession, Send-EtwTraceSession...}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules\PSDesiredStateConfiguration\DSCResources


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Script     0.0        MSFT_GroupResource                  {Get-TargetResource, Set-TargetResource, Test-TargetResource}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Cim        1.0        MSFT_LocalPrinterPort_v1.0
Cim        1.0        MSFT_LprPrinterPort_v1.0
Cim        1.0        MSFT_MpComputerStatus               Get-MpComputerStatus
Cim        1.0        MSFT_MpPreference                   {Get-MpPreference, Set-MpPreference, Add-MpPreference, Remove-MpPreference}
Cim        1.0        MSFT_MpScan                         Start-MpScan
Cim        1.0        MSFT_MpSignature                    Update-MpSignature
Cim        1.0        MSFT_MpThreat                       {Get-MpThreat, Remove-MpThreat}
Cim        1.0        MSFT_MpThreatCatalog                Get-MpThreatCatalog
Cim        1.0        MSFT_MpThreatDetection              Get-MpThreatDetection
Cim        1.0        MSFT_MpWDOScan                      Start-MpWDOScan
Cim        1.0        MSFT_NCSIPolicyConfiguration        {Get-NCSIPolicyConfiguration, Set-NCSIPolicyConfiguration, Reset-NCSIPolicyConfiguration}
Cim        1.0        MSFT_Net6to4Configuration           {Get-Net6to4Configuration, Set-Net6to4Configuration, Reset-Net6to4Configuration}
Cim        1.0        MSFT_NetAdapter.cmdletDefinition    {Get-NetAdapter, Enable-NetAdapter, Disable-NetAdapter, Restart-NetAdapter...}
Cim        1.0        MSFT_NetAdapterAdvancedProperty.... {Get-NetAdapterAdvancedProperty, Set-NetAdapterAdvancedProperty, Remove-NetAdapterAdvancedProperty, Reset-NetAdapterAdvancedProperty...}
Cim        1.0        MSFT_NetAdapterBinding.cmdletDef... {Get-NetAdapterBinding, Set-NetAdapterBinding, Enable-NetAdapterBinding, Disable-NetAdapterBinding}
Cim        1.0        MSFT_NetAdapterChecksumOffload      {Get-NetAdapterChecksumOffload, Set-NetAdapterChecksumOffload, Enable-NetAdapterChecksumOffload, Disable-NetAdapterChecksumOffload}
Cim        1.0        MSFT_NetAdapterEncapsulatedPacke... {Get-NetAdapterEncapsulatedPacketTaskOffload, Set-NetAdapterEncapsulatedPacketTaskOffload, Enable-NetAdapterEncapsulatedPacketTaskOffload, Di...
Cim        1.0        MSFT_NetAdapterHardwareInfo.cmdl... Get-NetAdapterHardwareInfo
Cim        1.0        MSFT_NetAdapterIPsecOffload         {Get-NetAdapterIPsecOffload, Set-NetAdapterIPsecOffload, Enable-NetAdapterIPsecOffload, Disable-NetAdapterIPsecOffload}
Cim        1.0        MSFT_NetAdapterLso                  {Get-NetAdapterLso, Set-NetAdapterLso, Enable-NetAdapterLso, Disable-NetAdapterLso}
Cim        1.0        MSFT_NetAdapterPacketDirect         {Get-NetAdapterPacketDirect, Set-NetAdapterPacketDirect, Enable-NetAdapterPacketDirect, Disable-NetAdapterPacketDirect}
Cim        1.0        MSFT_NetAdapterPowerManagement.c... {Get-NetAdapterPowerManagement, Set-NetAdapterPowerManagement, Enable-NetAdapterPowerManagement, Disable-NetAdapterPowerManagement}
Script     0.0        MSFT_NetAdapterPowerManagement.F... {Format-NdisConfigurationValue, Format-WakePatternType, Format-BitmapWakePattern}
Cim        1.0        MSFT_NetAdapterQos                  {Get-NetAdapterQos, Set-NetAdapterQos, Enable-NetAdapterQos, Disable-NetAdapterQos}
Script     0.0        MSFT_NetAdapterQos.Format.Helper    {Format-NetAdapterQosIntegerArray, Format-NetAdapterQosTrafficClass, Format-NetAdapterQosFlowControl, Format-NetAdapterQosClassification}
Cim        1.0        MSFT_NetAdapterRdma                 {Get-NetAdapterRdma, Set-NetAdapterRdma, Enable-NetAdapterRdma, Disable-NetAdapterRdma}
Cim        1.0        MSFT_NetAdapterRsc                  {Get-NetAdapterRsc, Set-NetAdapterRsc, Enable-NetAdapterRsc, Disable-NetAdapterRsc}
Cim        1.0        MSFT_NetAdapterRss.cmdletDefinition {Get-NetAdapterRss, Set-NetAdapterRss, Enable-NetAdapterRss, Disable-NetAdapterRss}
Cim        1.0        MSFT_NetAdapterSriov                {Get-NetAdapterSriov, Set-NetAdapterSriov, Enable-NetAdapterSriov, Disable-NetAdapterSriov}
Cim        1.0        MSFT_NetAdapterSriovVf.cmdletDef... Get-NetAdapterSriovVf
Cim        1.0        MSFT_NetAdapterStatistics.cmdlet... Get-NetAdapterStatistics
Cim        1.0        MSFT_NetAdapterVmq.cmdletDefinition {Get-NetAdapterVmq, Set-NetAdapterVmq, Enable-NetAdapterVmq, Disable-NetAdapterVmq}
Cim        1.0        MSFT_NetAdapterVmqQueue.cmdletDe... Get-NetAdapterVmqQueue
Cim        1.0        MSFT_NetAdapterVPort.cmdletDefin... Get-NetAdapterVPort
Cim        1.0        MSFT_NetCompartment                 Get-NetCompartment
Cim        1.0        MSFT_NetConnectionProfile           {Get-NetConnectionProfile, Set-NetConnectionProfile}
Cim        1.0        MSFT_NetDnsTransitionConfiguration  {Get-NetDnsTransitionConfiguration, Enable-NetDnsTransitionConfiguration, Disable-NetDnsTransitionConfiguration, Reset-NetDnsTransitionConfig...
Cim        1.0        MSFT_NetDnsTransitionMonitoring     Get-NetDnsTransitionMonitoring
Cim        1.1        MSFT_NetEventNetworkAdapter         {Get-NetEventNetworkAdapter, Remove-NetEventNetworkAdapter, Add-NetEventNetworkAdapter}
Cim        1.0        MSFT_NetEventPacketCaptureProvider  {Get-NetEventPacketCaptureProvider, Remove-NetEventPacketCaptureProvider, Set-NetEventPacketCaptureProvider, Add-NetEventPacketCaptureProvider}
Cim        1.0        MSFT_NetEventProvider               {Get-NetEventProvider, Remove-NetEventProvider, Set-NetEventProvider, Add-NetEventProvider}
Cim        1.0        MSFT_NetEventSession                {Get-NetEventSession, Remove-NetEventSession, Set-NetEventSession, Start-NetEventSession...}
Cim        1.0        MSFT_NetEventVFPProvider            {Get-NetEventVFPProvider, Remove-NetEventVFPProvider, Set-NetEventVFPProvider, Add-NetEventVFPProvider}
Cim        1.0        MSFT_NetEventVmNetworkAdatper       {Get-NetEventVmNetworkAdapter, Remove-NetEventVmNetworkAdapter, Add-NetEventVmNetworkAdapter}
Cim        1.0        MSFT_NetEventVmSwitch               {Get-NetEventVmSwitch, Remove-NetEventVmSwitch, Add-NetEventVmSwitch}
Cim        1.0        MSFT_NetEventVmSwitchProvider       {Get-NetEventVmSwitchProvider, Remove-NetEventVmSwitchProvider, Set-NetEventVmSwitchProvider, Add-NetEventVmSwitchProvider}
Cim        1.0        MSFT_NetEventWFPCaptureProvider     {Get-NetEventWFPCaptureProvider, Remove-NetEventWFPCaptureProvider, Set-NetEventWFPCaptureProvider, Add-NetEventWFPCaptureProvider}
Cim        1.0.0      MSFT_NetIPAddress                   {Get-NetIPAddress, Set-NetIPAddress, Remove-NetIPAddress, New-NetIPAddress}
Cim        1.0        MSFT_NetIpHTTPsConfiguration        {Get-NetIPHttpsConfiguration, Set-NetIPHttpsConfiguration, Remove-NetIPHttpsConfiguration, Reset-NetIPHttpsConfiguration...}
Cim        1.0        MSFT_NetIpHTTPsState                Get-NetIPHttpsState
Cim        1.0.0      MSFT_NetIPInterface                 {Get-NetIPInterface, Set-NetIPInterface}
Cim        1.0.0      MSFT_NetIPv4Protocol                {Get-NetIPv4Protocol, Set-NetIPv4Protocol}
Cim        1.0.0      MSFT_NetIPv6Protocol                {Get-NetIPv6Protocol, Set-NetIPv6Protocol}
Cim        1.0        MSFT_NetISATAPConfiguration         {Get-NetIsatapConfiguration, Set-NetIsatapConfiguration, Reset-NetIsatapConfiguration}
Cim        1.0        MSFT_NetLbfoTeam                    {Get-NetLbfoTeam, Remove-NetLbfoTeam, Set-NetLbfoTeam, New-NetLbfoTeam...}
Cim        1.0        MSFT_NetLbfoTeamMember              {Get-NetLbfoTeamMember, Set-NetLbfoTeamMember, Remove-NetLbfoTeamMember, Add-NetLbfoTeamMember}
Cim        1.0        MSFT_NetLbfoTeamNic                 {Get-NetLbfoTeamNic, Set-NetLbfoTeamNic, Remove-NetLbfoTeamNic, Add-NetLbfoTeamNic}
Cim        1.0        MSFT_NetNat                         {Get-NetNat, Set-NetNat, Remove-NetNat, New-NetNat}
Cim        1.0        MSFT_NetNatExternalAddress          {Get-NetNatExternalAddress, Remove-NetNatExternalAddress, Add-NetNatExternalAddress}
Cim        1.0        MSFT_NetNatGlobal                   {Get-NetNatGlobal, Set-NetNatGlobal}
Cim        1.0        MSFT_NetNatSession                  Get-NetNatSession
Cim        1.0        MSFT_NetNatStaticMapping            {Get-NetNatStaticMapping, Remove-NetNatStaticMapping, Add-NetNatStaticMapping}
Cim        1.0        MSFT_NetNatTransitionConfiguration  {Get-NetNatTransitionConfiguration, Set-NetNatTransitionConfiguration, Enable-NetNatTransitionConfiguration, Disable-NetNatTransitionConfigur...
Cim        1.0        MSFT_NetNatTransitionMonitoring     Get-NetNatTransitionMonitoring
Cim        1.0.0      MSFT_NetNeighbor                    {Get-NetNeighbor, Set-NetNeighbor, Remove-NetNeighbor, New-NetNeighbor}
Cim        1.0.0      MSFT_NetOffloadGlobalSetting        {Get-NetOffloadGlobalSetting, Set-NetOffloadGlobalSetting}
Cim        1.0.0      MSFT_NetPrefixPolicy                Get-NetPrefixPolicy
Cim        1.0        MSFT_NetQosPolicy                   {Get-NetQosPolicy, Set-NetQosPolicy, Remove-NetQosPolicy, New-NetQosPolicy}
Script     0.0        MSFT_NetQosPolicy.Format.Helper     Format-NetQosPolicySpeed
Cim        1.0.0      MSFT_NetRoute                       {Get-NetRoute, Set-NetRoute, Remove-NetRoute, New-NetRoute...}
Cim        1.0        MSFT_NetSwitchTeam                  {Get-NetSwitchTeam, Remove-NetSwitchTeam, New-NetSwitchTeam, Rename-NetSwitchTeam...}
Cim        1.0        MSFT_NetSwitchTeamMember            Get-NetSwitchTeamMember
Cim        1.0.0      MSFT_NetTCPConnection               Get-NetTCPConnection
Cim        1.0.0      MSFT_NetTCPSetting                  {Get-NetTCPSetting, Set-NetTCPSetting}
Cim        1.0        MSFT_NetTeredoConfiguration         {Get-NetTeredoConfiguration, Set-NetTeredoConfiguration, Reset-NetTeredoConfiguration}
Cim        1.0        MSFT_NetTeredoState                 Get-NetTeredoState
Cim        1.0.0      MSFT_NetTransportFilter             {Get-NetTransportFilter, Remove-NetTransportFilter, New-NetTransportFilter}
Cim        1.0.0      MSFT_NetUDPEndpoint                 Get-NetUDPEndpoint
Cim        1.0.0      MSFT_NetUDPSetting                  {Get-NetUDPSetting, Set-NetUDPSetting}
Cim        1.0        MSFT_OdbcDriverTask_v1.0            {Get-OdbcDriver, Set-OdbcDriver}
Cim        1.0        MSFT_OdbcDsnTask_v1.0               {Add-OdbcDsn, Get-OdbcDsn, Remove-OdbcDsn, Set-OdbcDsn}
Cim        1.0        MSFT_OdbcPerfCounterTask_v1.0       {Disable-OdbcPerfCounter, Enable-OdbcPerfCounter, Get-OdbcPerfCounter}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules\PSDesiredStateConfiguration\DSCResources


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Script     0.0        MSFT_PackageResource                {Test-TargetResource, Get-TargetResource, Set-TargetResource}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Cim        1.0        MSFT_Printer_v1.0                   {Get-Printer, Remove-Printer, Set-Printer, Add-Printer...}
Cim        1.0        MSFT_PrinterConfiguration_v1.0      {Get-PrintConfiguration, Set-PrintConfiguration}
Cim        1.0        MSFT_PrinterDriver_v1.0             {Get-PrinterDriver, Remove-PrinterDriver, Add-PrinterDriver}
Cim        1.0        MSFT_PrinterNfcTag_v1.0
Cim        1.0        MSFT_PrinterNfcTagTasks_v1.0        {Read-PrinterNfcTag, Write-PrinterNfcTag}
Cim        1.0        MSFT_PrinterPort_v1.0               {Get-PrinterPort, Remove-PrinterPort}
Cim        1.0        MSFT_PrinterPortTasks_v1.0          Add-PrinterPort
Cim        1.0        MSFT_PrinterProperty_v1.0           {Get-PrinterProperty, Set-PrinterProperty}
Cim        1.0        MSFT_PrintJob_v1.0                  {Get-PrintJob, Remove-PrintJob, Restart-PrintJob, Resume-PrintJob...}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules\PSDesiredStateConfiguration\DSCResources


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Script     0.0        MSFT_ProcessResource                {Get-TargetResource, Set-TargetResource, Test-TargetResource}
Script     0.0        MSFT_RegistryResource               {Get-TargetResource, Set-TargetResource, Test-TargetResource}
Script     0.0        MSFT_RoleResource                   {Get-TargetResource, Set-TargetResource, Test-TargetResource}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Cim        1.0        MSFT_ScheduledTask_v1.0             {Get-ScheduledTask, Unregister-ScheduledTask}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules\PSDesiredStateConfiguration\DSCResources


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Script     0.0        MSFT_ScriptResource                 {Get-TargetResource, Set-TargetResource, Test-TargetResource}
Script     0.0        MSFT_ServiceResource                {Get-TargetResource, Test-TargetResource, Set-TargetResource}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Cim        1.0        MSFT_TcpIpPrinterPort_v1.0


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules\PSDesiredStateConfiguration\DSCResources


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Script     0.0        MSFT_UserResource                   {Get-TargetResource, Set-TargetResource, Test-TargetResource}
Script     0.0        MSFT_WaitForAll                     {Get-TargetResource, Set-TargetResource, Test-TargetResource}
Script     0.0        MSFT_WaitForAny                     {Get-TargetResource, Set-TargetResource, Test-TargetResource}
Script     0.0        MSFT_WaitForSome                    {Get-TargetResource, Set-TargetResource, Test-TargetResource}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Cim        1.0        MSFT_WdacBidTraceTask_v1.0          {Disable-WdacBidTrace, Enable-WdacBidTrace, Get-WdacBidTrace}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules\PSDesiredStateConfiguration\DSCResources


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Script     0.0        MSFT_WindowsOptionalFeature         {Get-TargetResource, Set-TargetResource, Test-TargetResource}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Cim        1.0        MSFT_WsdPrinterPort_v1.0
Manifest   2.0.0.0    NetAdapter                          {Disable-NetAdapter, Disable-NetAdapterBinding, Disable-NetAdapterChecksumOffload, Disable-NetAdapterEncapsulatedPacketTaskOffload...}
Script     0.0        NetAdapter.Format.Helper            {Format-MacAddress, Format-AdapterName, Format-AdapterInstanceID, Format-LinkSpeed}
Manifest   1.0.0.0    NetConnection                       {Get-NetConnectionProfile, Set-NetConnectionProfile}
Manifest   1.0.0.0    NetEventPacketCapture               {New-NetEventSession, Remove-NetEventSession, Get-NetEventSession, Set-NetEventSession...}
Cim        1.0.0.0    NetFirewallAddressFilter.cmdletD... {Get-NetFirewallAddressFilter, Set-NetFirewallAddressFilter}
Cim        1.0.0.0    NetFirewallApplicationFilter.cmd... {Get-NetFirewallApplicationFilter, Set-NetFirewallApplicationFilter}
Cim        1.0.0.0    NetFirewallInterfaceFilter.cmdle... {Get-NetFirewallInterfaceFilter, Set-NetFirewallInterfaceFilter}
Cim        1.0.0.0    NetFirewallInterfaceTypeFilter.c... {Get-NetFirewallInterfaceTypeFilter, Set-NetFirewallInterfaceTypeFilter}
Cim        1.0.0.0    NetFirewallPortFilter.cmdletDefi... {Get-NetFirewallPortFilter, Set-NetFirewallPortFilter}
Cim        1.0.0.0    NetFirewallProfile.cmdletDefinition {Get-NetFirewallProfile, Set-NetFirewallProfile}
Cim        1.0.0.0    NetFirewallRule.cmdletDefinition    {Get-NetFirewallRule, Set-NetFirewallRule, Remove-NetFirewallRule, Rename-NetFirewallRule...}
Cim        1.0.0.0    NetFirewallSecurityFilter.cmdlet... {Get-NetFirewallSecurityFilter, Set-NetFirewallSecurityFilter}
Cim        1.0.0.0    NetFirewallServiceFilter.cmdletD... {Get-NetFirewallServiceFilter, Set-NetFirewallServiceFilter}
Cim        1.0.0.0    NetFirewallSetting.cmdletDefinition {Get-NetFirewallSetting, Set-NetFirewallSetting}
Cim        1.0.0.0    NetGPO.cmdletDefinition             {Open-NetGPO, Save-NetGPO}
Script     0.0        NetIPConfiguration                  {Get-NetIPConfiguration, gip}
Cim        1.0.0.0    NetIPsecDospSetting.cmdletDefini... {Get-NetIPsecDospSetting, Set-NetIPsecDospSetting, Remove-NetIPsecDospSetting, New-NetIPsecDospSetting}
Cim        1.0.0.0    NetIPsecIdentity.cmdletDefinition
Cim        1.0.0.0    NetIPsecMainModeCryptoSet.cmdlet... {Get-NetIPsecMainModeCryptoSet, Set-NetIPsecMainModeCryptoSet, Remove-NetIPsecMainModeCryptoSet, Rename-NetIPsecMainModeCryptoSet...}
Cim        1.0.0.0    NetIPsecMainModeRule.cmdletDefin... {Get-NetIPsecMainModeRule, Set-NetIPsecMainModeRule, Remove-NetIPsecMainModeRule, Rename-NetIPsecMainModeRule...}
Cim        1.0.0.0    NetIPsecMainModeSA.cmdletDefinition {Get-NetIPsecMainModeSA, Remove-NetIPsecMainModeSA}
Cim        1.0.0.0    NetIPsecPhase1AuthSet.cmdletDefi... {Get-NetIPsecPhase1AuthSet, Set-NetIPsecPhase1AuthSet, Remove-NetIPsecPhase1AuthSet, Rename-NetIPsecPhase1AuthSet...}
Cim        1.0.0.0    NetIPsecPhase2AuthSet.cmdletDefi... {Get-NetIPsecPhase2AuthSet, Set-NetIPsecPhase2AuthSet, Remove-NetIPsecPhase2AuthSet, Rename-NetIPsecPhase2AuthSet...}
Cim        1.0.0.0    NetIPsecPolicyChange.cmdletDefin...
Cim        1.0.0.0    NetIPsecQuickModeCryptoSet.cmdle... {Get-NetIPsecQuickModeCryptoSet, Set-NetIPsecQuickModeCryptoSet, Remove-NetIPsecQuickModeCryptoSet, Rename-NetIPsecQuickModeCryptoSet...}
Cim        1.0.0.0    NetIPsecQuickModeSA.cmdletDefini... {Get-NetIPsecQuickModeSA, Remove-NetIPsecQuickModeSA}
Cim        1.0.0.0    NetIPsecRule.cmdletDefinition       {Get-NetIPsecRule, Set-NetIPsecRule, Remove-NetIPsecRule, Rename-NetIPsecRule...}
Manifest   2.0.0.0    NetLbfo                             {Add-NetLbfoTeamMember, Add-NetLbfoTeamNic, Get-NetLbfoTeam, Get-NetLbfoTeamMember...}
Manifest   1.0.0.0    NetNat                              {Get-NetNat, Get-NetNatExternalAddress, Get-NetNatStaticMapping, Get-NetNatSession...}
Manifest   2.0.0.0    NetQos                              {Get-NetQosPolicy, Set-NetQosPolicy, Remove-NetQosPolicy, New-NetQosPolicy}
Manifest   2.0.0.0    NetSecurity                         {Get-DAPolicyChange, New-NetIPsecAuthProposal, New-NetIPsecMainModeCryptoProposal, New-NetIPsecQuickModeCryptoProposal...}
Manifest   1.0.0.0    NetSwitchTeam                       {New-NetSwitchTeam, Remove-NetSwitchTeam, Get-NetSwitchTeam, Rename-NetSwitchTeam...}
Manifest   1.0.0.0    NetTCPIP                            {Get-NetIPAddress, Get-NetIPInterface, Get-NetIPv4Protocol, Get-NetIPv6Protocol...}
Manifest   1.0.0.0    NetworkConnectivityStatus           {Get-DAConnectionStatus, Get-NCSIPolicyConfiguration, Reset-NCSIPolicyConfiguration, Set-NCSIPolicyConfiguration}
Script     0.0        NetworkSwitchConfiguration          {Restore-NetworkSwitchConfiguration, Save-NetworkSwitchConfiguration, CmdletShouldProcess, Get-NetworkSwitchRegisteredProfileFromNamespace...}
Script     0.0        NetworkSwitchEthernetPort           {Disable-NetworkSwitchEthernetPort, Enable-NetworkSwitchEthernetPort, Get-NetworkSwitchEthernetPort, Remove-NetworkSwitchEthernetPortIPAddres...
Script     0.0        NetworkSwitchFeature                {Disable-NetworkSwitchFeature, Enable-NetworkSwitchFeature, Get-NetworkSwitchFeature, CmdletShouldProcess...}
Script     0.0        NetworkSwitchGlobalSettingData      {Get-NetworkSwitchGlobalData, CmdletShouldProcess, Get-NetworkSwitchRegisteredProfileFromNamespace, Get-NetworkSwitchImplementationNamespace...}
Manifest   1.0.0.0    NetworkSwitchManager                {Disable-NetworkSwitchEthernetPort, Enable-NetworkSwitchEthernetPort, Get-NetworkSwitchEthernetPort, Remove-NetworkSwitchEthernetPortIPAddres...
Script     0.0        NetworkSwitchVlan                   {Disable-NetworkSwitchVlan, Enable-NetworkSwitchVlan, Get-NetworkSwitchVlan, New-NetworkSwitchVlan...}
Manifest   1.0.0.0    NetworkTransition                   {Add-NetIPHttpsCertBinding, Disable-NetDnsTransitionConfiguration, Disable-NetIPHttpsProfile, Disable-NetNatTransitionConfiguration...}
Cim        1.0.0.0    OffloadDataTransferSetting          Get-OffloadDataTransferSetting
Cim        1.0.0.0    Partition                           {Get-Partition, Remove-Partition, Resize-Partition, Get-PartitionSupportedSize...}
Manifest   1.0.0.0    PcsvDevice                          {Get-PcsvDevice, Start-PcsvDevice, Stop-PcsvDevice, Restart-PcsvDevice...}
Cim        1.0.0.0    PhysicalDisk                        {Get-PhysicalDisk, Enable-PhysicalDiskIdentification, Disable-PhysicalDiskIdentification, Reset-PhysicalDisk...}
Manifest   1.0.0.0    pki                                 {Add-CertificateEnrollmentPolicyServer, Export-Certificate, Export-PfxCertificate, Get-CertificateAutoEnrollmentPolicy...}
Cim        1.0        PnpDevice                           {Get-PnpDevice, Enable-PnpDevice, Disable-PnpDevice, Get-PnpDeviceProperty}
Manifest   1.0.0.0    PnpDevice                           {Get-PnpDevice, Get-PnpDeviceProperty, Enable-PnpDevice, Disable-PnpDevice}
Manifest   0.0        PnpDevice.Resource
Manifest   1.1        PrintManagement                     {Add-Printer, Add-PrinterDriver, Add-PrinterPort, Get-PrintConfiguration...}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules\PSDesiredStateConfiguration\DSCResources


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Script     1.0        ProcessSet                          {BuildResourceCommonParameters, BuildResourceString}
Script     1.0        ProcessSet                          {BuildResourceCommonParameters, BuildResourceString}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Cim        1.0        PS_BackgroundTask                   {Get-AppBackgroundTask, Start-AppBackgroundTask, Unregister-AppBackgroundTask}
Cim        1.0        PS_ClusteredScheduledTask_v1.0      {Get-ClusteredScheduledTask, Register-ClusteredScheduledTask, Set-ClusteredScheduledTask, Unregister-ClusteredScheduledTask}
Cim        1.0.0      PS_DnsClientNRPTGlobal_v1.0.0       {Get-DnsClientNrptGlobal, Set-DnsClientNrptGlobal}
Cim        1.0.0      PS_DnsClientNrptPolicy_v1.0.0       Get-DnsClientNrptPolicy
Cim        1.0.0      PS_DnsClientNRPTRule_v1.0.0         {Add-DnsClientNrptRule, Get-DnsClientNrptRule, Remove-DnsClientNrptRule, Set-DnsClientNrptRule}
Cim        1.0.0      PS_EapConfiguration_v1.0.0          New-EapConfiguration
Cim        1.0        ps_mmagent_v1.0                     {Debug-MMAppPrelaunch, Disable-MMAgent, Enable-MMAgent, Get-MMAgent...}
Cim        1.0        PS_ScheduledTask_v1.0               {Disable-ScheduledTask, Enable-ScheduledTask, Export-ScheduledTask, Get-ScheduledTaskInfo...}
Cim        1.0.0      PS_VpnConnection_v1.0.0             {Add-VpnConnection, Get-VpnConnection, Remove-VpnConnection, Set-VpnConnection}
Cim        1.0        PS_VpnConnectionIPsecConfigurati... Set-VpnConnectionIPsecConfiguration
Cim        1.0        PS_VpnConnectionProxy_v1.0          Set-VpnConnectionProxy
Cim        1.0        PS_VpnConnectionRoute_v1.0          {Add-VpnConnectionRoute, Remove-VpnConnectionRoute}
Cim        1.0        PS_VpnConnectionTrigger_v1.0        Get-VpnConnectionTrigger
Cim        1.0        PS_VpnConnectionTriggerApplicati... {Add-VpnConnectionTriggerApplication, Remove-VpnConnectionTriggerApplication}
Cim        1.0        PS_VpnConnectionTriggerDnsConfig... {Add-VpnConnectionTriggerDnsConfiguration, Remove-VpnConnectionTriggerDnsConfiguration, Set-VpnConnectionTriggerDnsConfiguration}
Cim        1.0        PS_VpnConnectionTriggerTrustedNe... {Add-VpnConnectionTriggerTrustedNetwork, Remove-VpnConnectionTriggerTrustedNetwork, Set-VpnConnectionTriggerTrustedNetwork}
Cim        1.0        PS_VpnServerAddress_v1.0            New-VpnServerAddress
Manifest   1.1        PSDesiredStateConfiguration         {Set-DscLocalConfigurationManager, Start-DscConfiguration, Test-DscConfiguration, Publish-DscConfiguration...}
Script     0.0        PSDesiredStateConfiguration         {Generate-VersionInfo, Set-PSMetaConfigDocInsProcessedBeforeMeta, Get-PSMetaConfigurationProcessed, Get-PSMetaConfigDocumentInstVersionInfo...}
Script     1.0.0.0    PSDiagnostics                       {Disable-PSTrace, Disable-PSWSManCombinedTrace, Disable-WSManTrace, Enable-PSTrace...}
Script     1.0.0.0    PSDiagnostics                       {Disable-PSTrace, Disable-PSWSManCombinedTrace, Disable-WSManTrace, Enable-PSTrace...}
Script     0.0        PSDscXMachine                       {Get-_InternalPSDscXMachineTR, Set-_InternalPSDscXMachineTR, Test-_InternalPSDscXMachineTR}
Binary     1.1.0.0    PSScheduledJob                      {New-JobTrigger, Add-JobTrigger, Remove-JobTrigger, Get-JobTrigger...}
Manifest   2.0.0.0    PSWorkflow                          {New-PSWorkflowExecutionOption, New-PSWorkflowSession, nwsn}
Script     0.0        PSWorkflow                          {New-PSWorkflowSession, nwsn}
Manifest   1.0.0.0    PSWorkflowUtility                   Invoke-AsWorkflow
Script     0.0        PSWorkflowUtility                   Invoke-AsWorkflow
Cim        2.0.0.0    Remove-DscConfigurationDocument     Remove-DscConfigurationDocument
Cim        1.0.0.0    ResiliencySetting                   {Get-ResiliencySetting, Set-ResiliencySetting}
Cim        2.0.0.0    Restore-DscConfiguration            Restore-DscConfiguration


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules\PSDesiredStateConfiguration


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Script     0.0        RunAsHelper                         {Get-DomainAndUserName, Import-DscNativeMethods, IsNanoServer}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Manifest   1.0.0.0    ScheduledTasks                      {Get-ScheduledTask, Set-ScheduledTask, Register-ScheduledTask, Unregister-ScheduledTask...}
Manifest   2.0.0.0    SecureBoot                          {Confirm-SecureBootUEFI, Set-SecureBootUEFI, Get-SecureBootUEFI, Format-SecureBootUEFI...}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules\PSDesiredStateConfiguration\DSCResources


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Script     1.0        ServiceSet                          {BuildResourceCommonParameters, BuildResourceString}
Script     1.0        ServiceSet                          {BuildResourceCommonParameters, BuildResourceString}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Cim        1.0        SmbBandwidthLimit                   {Get-SmbBandwidthLimit, Remove-SmbBandwidthLimit, Set-SmbBandwidthLimit, gsmbb...}
Cim        1.0        SmbClientConfiguration              {Get-SmbClientConfiguration, Set-SmbClientConfiguration, gsmbcc, ssmbcc}
Cim        1.0        SmbClientNetworkInterface           {Get-SmbClientNetworkInterface, gsmbcn}
Cim        1.0        SmbConnection                       {Get-SmbConnection, gsmbc}
Cim        1.0        SmbMapping                          {Get-SmbMapping, Remove-SmbMapping, New-SmbMapping, gsmbm...}
Cim        1.0        SmbMultichannelConnection           {Get-SmbMultichannelConnection, Update-SmbMultichannelConnection, gsmbmc, udsmbmc}
Cim        1.0        SmbMultichannelConstraint           {Get-SmbMultichannelConstraint, Remove-SmbMultichannelConstraint, New-SmbMultichannelConstraint, gsmbt...}
Cim        1.0        SmbOpenFile                         {Get-SmbOpenFile, Close-SmbOpenFile, gsmbo, cssmbo}
Script     0.0        SmbScriptModule                     {Set-SmbPathAcl, Get-SmbDelegation, Enable-SmbDelegation, Disable-SmbDelegation...}
Cim        1.0        SmbServerConfiguration              {Get-SmbServerConfiguration, Set-SmbServerConfiguration, gsmbsc, ssmbsc}
Cim        1.0        SmbServerNetworkInterface           {Get-SmbServerNetworkInterface, gsmbsn}
Cim        1.0        SmbSession                          {Get-SmbSession, Close-SmbSession, gsmbse, cssmbse}
Cim        1.0        SmbShare                            {Get-SmbShare, Remove-SmbShare, Set-SmbShare, Block-SmbShareAccess...}
Manifest   2.0.0.0    SmbShare                            {Get-SmbShare, Remove-SmbShare, Set-SmbShare, Block-SmbShareAccess...}
Script     0.0        SmbShare.Format.Helper              Format-LinkSpeed
Manifest   2.0.0.0    SmbWitness                          {Get-SmbWitnessClient, Move-SmbWitnessClient, gsmbw, msmbw...}
Cim        1.0        SmbWitnessWmiClient                 {Get-SmbWitnessClient, Move-SmbWitnessClient, gsmbw, msmbw...}
Manifest   1.0.0.0    StartLayout                         {Export-StartLayout, Import-StartLayout, Get-StartApps}
Cim        2.0.0.0    Stop-DscConfiguration               Stop-DscConfiguration
Manifest   2.0.0.0    Storage                             {Add-InitiatorIdToMaskingSet, Add-PartitionAccessPath, Add-PhysicalDisk, Add-TargetPortToMaskingSet...}
Cim        1.0.0.0    StorageCmdlets                      {Set-Disk, Set-Volume, Set-Partition, Set-PhysicalDisk...}
Cim        1.0.0.0    StorageEnclosure                    {Get-StorageEnclosure, Enable-StorageEnclosureIdentification, Disable-StorageEnclosureIdentification, Get-StorageEnclosureVendorData}
Cim        1.0.0.0    StorageHealth                       {Get-StorageHealth, Get-StorageHealthSettingInternal, Set-StorageHealthSettingInternal, Remove-StorageHealthSettingInternal}
Cim        1.0.0.0    StorageJob                          {Get-StorageJob, Stop-StorageJob}
Cim        1.0.0.0    StorageNode                         Get-StorageNode
Cim        1.0.0.0    StoragePool                         {Get-StoragePool, New-VirtualDisk, New-StorageTier, Remove-StoragePool...}
Cim        1.0.0.0    StorageProvider                     {Get-StorageProvider, Update-StorageProviderCache, Register-StorageSubsystem, Unregister-StorageSubsystem...}
Cim        1.0.0.0    StorageReliabilityCounter           {Get-StorageReliabilityCounterDeprecated, Reset-StorageReliabilityCounter}
Script     0.0        StorageScripts                      {CreateErrorRecord, Get-PhysicalDiskStorageNodeView, Get-DiskStorageNodeView, Get-StorageEnclosureStorageNodeView...}
Cim        1.0.0.0    StorageSetting                      {Get-StorageSetting, Set-StorageSetting, Update-HostStorageCache}
Cim        1.0.0.0    StorageSubSystem                    {Get-StorageSubSystem, New-StoragePool, New-StorageSubsystemVirtualDisk, New-MaskingSet...}
Cim        1.0.0.0    StorageTier                         {Get-StorageTier, Remove-StorageTier, Resize-StorageTier, Get-StorageTierSupportedSize}
Cim        1.0.0.0    TargetPort                          Get-TargetPort
Cim        1.0.0.0    TargetPortal                        Get-TargetPortal
Script     0.0        TestDtc                             {Get-DAPolicyChange, New-NetIPsecAuthProposal, New-NetIPsecMainModeCryptoProposal, New-NetIPsecQuickModeCryptoProposal...}
Script     0.0        Test-NetConnection                  {Test-NetConnection, TNC}
Manifest   2.0.0.0    tls                                 {New-TlsSessionTicketKey, Enable-TlsSessionTicketKey, Disable-TlsSessionTicketKey, Export-TlsSessionTicketKey...}
Manifest   1.0.0.0    TroubleshootingPack                 {Get-TroubleshootingPack, Invoke-TroubleshootingPack}
Manifest   2.0.0.0    TrustedPlatformModule               {Get-Tpm, Initialize-Tpm, Clear-Tpm, Unblock-Tpm...}
Binary     2.1.639.0  UEV                                 {Clear-UevConfiguration, Clear-UevAppxPackage, Restore-UevBackup, Set-UevTemplateProfile...}
Cim        1.0.0.0    VirtualDisk                         {Get-VirtualDisk, Remove-VirtualDisk, Show-VirtualDisk, Hide-VirtualDisk...}
Cim        1.0.0.0    Volume                              {Get-Volume, Format-Volume, Repair-Volume, Optimize-Volume...}
Manifest   2.0.0.0    VpnClient                           {Add-VpnConnection, Set-VpnConnection, Remove-VpnConnection, Get-VpnConnection...}
Manifest   1.0.0.0    Wdac                                {Get-OdbcDriver, Set-OdbcDriver, Get-OdbcDsn, Add-OdbcDsn...}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules\PSDesiredStateConfiguration


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Binary     1.0        WebDownloadManager                  {Get-DscDocument, Get-DscModule, Get-DscAction, Send-DscStatus...}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Manifest   1.0.0.0    WindowsDeveloperLicense             {Get-WindowsDeveloperLicense, Unregister-WindowsDeveloperLicense, Show-WindowsDeveloperLicenseRegistration}
Script     1.0        WindowsErrorReporting               {Enable-WindowsErrorReporting, Disable-WindowsErrorReporting, Get-WindowsErrorReporting}
Script     1.0        WindowsErrorReporting               {Enable-WindowsErrorReporting, Disable-WindowsErrorReporting, Get-WindowsErrorReporting}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules\PSDesiredStateConfiguration\DSCResources


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Script     1.0        WindowsFeatureSet                   {BuildResourceCommonParameters, BuildResourceString}
Script     1.0        WindowsFeatureSet                   {BuildResourceCommonParameters, BuildResourceString}
Script     1.0        WindowsOptionalFeatureSet           {BuildResourceCommonParameters, BuildResourceString}
Script     1.0        WindowsOptionalFeatureSet           {BuildResourceCommonParameters, BuildResourceString}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules\PSDesiredStateConfiguration\DSCClassResources


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Script     1.0        WindowsPackageCab
Script     1.0        WindowsPackageCab


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Manifest   1.0.0.0    WindowsSearch                       {Get-WindowsSearchSetting, Set-WindowsSearchSetting}
Manifest   1.0.0.0    WindowsUpdate                       Get-WindowsUpdateLog
Script     0.0        WindowsUpdateLog                    Get-WindowsUpdateLog


PS C:\Users\Windows10-32>
```

- Loading/Importing Modules

```PowerShell
PS C:\Users\Windows10-32> Import-Module <Path of the module>
```

```PowerShell
PS C:\Users\Administrator\Desktop\nishang-master> Import-Module .\nishang.psm1
WARNING: The names of some imported commands from the module 'nishang' include unapproved verbs that might make them less discoverable. To find the commands with unapproved verbs, run the Import-Module
command again with the Verbose parameter. For a list of approved verbs, type Get-Verb.
WARNING: Some imported command names contain one or more of the following restricted characters: # , ( ) {{ }} [ ] & - / \ $ ^ ; : " ' < > | ? @ ` * % + = ~
PS C:\Users\Administrator\Desktop\nishang-master>
```

```PowerShell
PS C:\Users\Administrator\Desktop\nishang-master> Get-Module

ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Manifest   3.1.0.0    Microsoft.PowerShell.Management     {Add-Computer, Add-Content, Checkpoint-Computer, Clear-Content...}
Manifest   3.1.0.0    Microsoft.PowerShell.Utility        {Add-Member, Add-Type, Clear-Variable, Compare-Object...}
Script     0.0        nishang                             {Add-Exfiltration, Add-Persistence, Add-RegBackdoor, Add-ScrnSaveBackdoor...}


PS C:\Users\Administrator\Desktop\nishang-master>
```

- PSModulePath

```PowerShell
PS C:\Users\Administrator\Desktop\nishang-master> $env:PSModulePath
C:\Users\Administrator\Documents\WindowsPowerShell\Modules;C:\Program Files\WindowsPowerShell\Modules;C:\Windows\system32\WindowsPowerShell\v1.0\Modules\
PS C:\Users\Administrator\Desktop\nishang-master>
```

- Unloading/Removing Modules

```PowerShell
PS C:\Users\Administrator\Desktop\nishang-master> Get-Module

ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Manifest   3.1.0.0    Microsoft.PowerShell.Management     {Add-Computer, Add-Content, Checkpoint-Computer, Clear-Content...}
Manifest   3.1.0.0    Microsoft.PowerShell.Utility        {Add-Member, Add-Type, Clear-Variable, Compare-Object...}
Script     0.0        nishang                             {Add-Exfiltration, Add-Persistence, Add-RegBackdoor, Add-ScrnSaveBackdoor...}


PS C:\Users\Administrator\Desktop\nishang-master>
```

```PowerShell
PS C:\Users\Administrator\Desktop\nishang-master> Remove-Module nishang
```

```PowerShell
PS C:\Users\Administrator\Desktop\nishang-master> Get-Module

ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Manifest   3.1.0.0    Microsoft.PowerShell.Management     {Add-Computer, Add-Content, Checkpoint-Computer, Clear-Content...}
Manifest   3.1.0.0    Microsoft.PowerShell.Utility        {Add-Member, Add-Type, Clear-Variable, Compare-Object...}


PS C:\Users\Administrator\Desktop\nishang-master>
```

- [Different types of Modules](https://msdn.microsoft.com/en-us/library/dd878324(v=vs.85).aspx)
    - Script Modules
    - Binary Modules
    - Manifest Modules
    - Dynamic Modules
