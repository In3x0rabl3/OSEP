#### 32. Using WMI in Powershell Part 1

###### [WMI](http://searchwindowsserver.techtarget.com/definition/Windows-Management-Instrumentation) – Exploring

- Get help on ```WMI```

```PowerShell
PS C:\Users\Administrator> Get-Help *wmi*

Name                              Category  Module                    Synopsis
----                              --------  ------                    --------
gwmi                              Alias                               Get-WmiObject
iwmi                              Alias                               Invoke-WmiMethod
rwmi                              Alias                               Remove-WmiObject
swmi                              Alias                               Set-WmiInstance
Get-WmiObject                     Cmdlet    Microsoft.PowerShell.M... Gets instances of Windows Management Instrumentation (WMI) classes or information about the available classes.
Invoke-WmiMethod                  Cmdlet    Microsoft.PowerShell.M... Calls Windows Management Instrumentation (WMI) methods.
Register-WmiEvent                 Cmdlet    Microsoft.PowerShell.M... Subscribes to a Windows Management Instrumentation (WMI) event.
Remove-WmiObject                  Cmdlet    Microsoft.PowerShell.M... Deletes an instance of an existing Windows Management Instrumentation (WMI) class.
Set-WmiInstance                   Cmdlet    Microsoft.PowerShell.M... Creates or updates an instance of an existing Windows Management Instrumentation (WMI) class.
about_WMI                         HelpFile                            Windows Management Instrumentation (WMI) uses the
about_Wmi_Cmdlets                 HelpFile                            Provides background information about Windows Management Instrumentation

PS C:\Users\Administrator>
```

- Exploring ```namespaces``` 
    - ```Namespaces``` are collection of ```classes``` which hold ```objects``` of different types
    - [List even the nested namespaces](http://www.powershellmagazine.com/2013/10/18/pstip-list-all-wmi-namespaces-on-a-system/)

```PowerShell
PS C:\Users\Administrator> Get-WmiObject -Namespace "root" -Class "__Namespace" | Select-Object Name

Name
----
subscription
DEFAULT
MicrosoftDfs
CIMV2
msdtc
Cli
nap
MicrosoftActiveDirectory
SECURITY
RSOP
MicrosoftDNS
StandardCimv2
WMI
AccessLogging
directory
Policy
InventoryLogging
Interop
Hardware
ServiceModel
Microsoft

PS C:\Users\Administrator>
```

- Exploring ```classes``` 

```PowerShell
PS C:\Users\Administrator> Get-WmiObject -Namespace "root/cimv2" -List

   NameSpace: ROOT\cimv2

Name                                Methods              Properties
----                                -------              ----------
CIM_Indication                      {}                   {CorrelatedIndications, IndicationFilterName, IndicationIdentifier, IndicationTime...}
CIM_ClassIndication                 {}                   {ClassDefinition, CorrelatedIndications, IndicationFilterName, IndicationIdentifier...}
CIM_ClassDeletion                   {}                   {ClassDefinition, CorrelatedIndications, IndicationFilterName, IndicationIdentifier...}
CIM_ClassCreation                   {}                   {ClassDefinition, CorrelatedIndications, IndicationFilterName, IndicationIdentifier...}
CIM_ClassModification               {}                   {ClassDefinition, CorrelatedIndications, IndicationFilterName, IndicationIdentifier...}
CIM_InstIndication                  {}                   {CorrelatedIndications, IndicationFilterName, IndicationIdentifier, IndicationTime...}
CIM_InstCreation                    {}                   {CorrelatedIndications, IndicationFilterName, IndicationIdentifier, IndicationTime...}
CIM_InstModification                {}                   {CorrelatedIndications, IndicationFilterName, IndicationIdentifier, IndicationTime...}
CIM_InstDeletion                    {}                   {CorrelatedIndications, IndicationFilterName, IndicationIdentifier, IndicationTime...}
__NotifyStatus                      {}                   {StatusCode}
__ExtendedStatus                    {}                   {Description, Operation, ParameterInfo, ProviderName...}
Win32_PrivilegesStatus              {}                   {Description, Operation, ParameterInfo, PrivilegesNotHeld...}
Win32_JobObjectStatus               {}                   {AdditionalDescription, Description, Operation, ParameterInfo...}
CIM_Error                           {}                   {CIMStatusCode, CIMStatusCodeDescription, ErrorSource, ErrorSourceFormat...}
MSFT_WmiError                       {}                   {CIMStatusCode, CIMStatusCodeDescription, error_Category, error_Code...}
MSFT_ExtendedStatus                 {}                   {CIMStatusCode, CIMStatusCodeDescription, error_Category, error_Code...}
__SecurityRelatedClass              {}                   {}
__Trustee                           {}                   {Domain, Name, SID, SidLength...}
Win32_Trustee                       {}                   {Domain, Name, SID, SidLength...}
__NTLMUser9X                        {}                   {Authority, Flags, Mask, Name...}
__ACE                               {}                   {AccessMask, AceFlags, AceType, GuidInheritedObjectType...}
Win32_ACE                           {}                   {AccessMask, AceFlags, AceType, GuidInheritedObjectType...}
__SecurityDescriptor                {}                   {ControlFlags, DACL, Group, Owner...}
Win32_SecurityDescriptor            {}                   {ControlFlags, DACL, Group, Owner...}
__PARAMETERS                        {}                   {}
__SystemClass                       {}                   {}
__ProviderRegistration              {}                   {provider}
__EventProviderRegistration         {}                   {EventQueryList, provider}
__ObjectProviderRegistration        {}                   {InteractionType, provider, QuerySupportLevels, SupportsBatching...}
__ClassProviderRegistration         {}                   {CacheRefreshInterval, InteractionType, PerUserSchema, provider...}
__InstanceProviderRegistration      {}                   {InteractionType, provider, QuerySupportLevels, SupportsBatching...}
__MethodProviderRegistration        {}                   {provider}
__PropertyProviderRegistration      {}                   {provider, SupportsGet, SupportsPut}
__EventConsumerProviderRegistration {}                   {ConsumerClassNames, provider}
__thisNAMESPACE                     {}                   {SECURITY_DESCRIPTOR}
__NAMESPACE                         {}                   {Name}
__IndicationRelated                 {}                   {}
__FilterToConsumerBinding           {}                   {Consumer, CreatorSID, DeliverSynchronously, DeliveryQoS...}
__EventConsumer                     {}                   {CreatorSID, MachineName, MaximumQueueSize}
__AggregateEvent                    {}                   {NumberOfEvents, Representative}
__TimerNextFiring                   {}                   {NextEvent64BitTime, TimerId}
__EventFilter                       {}                   {CreatorSID, EventAccess, EventNamespace, Name...}
__Event                             {}                   {SECURITY_DESCRIPTOR, TIME_CREATED}
__NamespaceOperationEvent           {}                   {SECURITY_DESCRIPTOR, TargetNamespace, TIME_CREATED}
__NamespaceModificationEvent        {}                   {PreviousNamespace, SECURITY_DESCRIPTOR, TargetNamespace, TIME_CREATED}
__NamespaceDeletionEvent            {}                   {SECURITY_DESCRIPTOR, TargetNamespace, TIME_CREATED}
__NamespaceCreationEvent            {}                   {SECURITY_DESCRIPTOR, TargetNamespace, TIME_CREATED}
__ClassOperationEvent               {}                   {SECURITY_DESCRIPTOR, TargetClass, TIME_CREATED}
__ClassDeletionEvent                {}                   {SECURITY_DESCRIPTOR, TargetClass, TIME_CREATED}
__ClassModificationEvent            {}                   {PreviousClass, SECURITY_DESCRIPTOR, TargetClass, TIME_CREATED}
__ClassCreationEvent                {}                   {SECURITY_DESCRIPTOR, TargetClass, TIME_CREATED}
__InstanceOperationEvent            {}                   {SECURITY_DESCRIPTOR, TargetInstance, TIME_CREATED}
__InstanceCreationEvent             {}                   {SECURITY_DESCRIPTOR, TargetInstance, TIME_CREATED}
__MethodInvocationEvent             {}                   {Method, Parameters, PreCall, SECURITY_DESCRIPTOR...}
__InstanceModificationEvent         {}                   {PreviousInstance, SECURITY_DESCRIPTOR, TargetInstance, TIME_CREATED}
__InstanceDeletionEvent             {}                   {SECURITY_DESCRIPTOR, TargetInstance, TIME_CREATED}
__TimerEvent                        {}                   {NumFirings, SECURITY_DESCRIPTOR, TIME_CREATED, TimerId}
__ExtrinsicEvent                    {}                   {SECURITY_DESCRIPTOR, TIME_CREATED}
__SystemEvent                       {}                   {SECURITY_DESCRIPTOR, TIME_CREATED}
__EventDroppedEvent                 {}                   {Event, IntendedConsumer, SECURITY_DESCRIPTOR, TIME_CREATED}
__EventQueueOverflowEvent           {}                   {CurrentQueueSize, Event, IntendedConsumer, SECURITY_DESCRIPTOR...}
__QOSFailureEvent                   {}                   {ErrorCode, ErrorDescription, Event, IntendedConsumer...}
__ConsumerFailureEvent              {}                   {ErrorCode, ErrorDescription, ErrorObject, Event...}
MSFT_SCMEvent                       {}                   {SECURITY_DESCRIPTOR, TIME_CREATED}
MSFT_SCMEventLogEvent               {}                   {SECURITY_DESCRIPTOR, TIME_CREATED}
MSFT_NetSevereServiceFailed         {}                   {SECURITY_DESCRIPTOR, Service, TIME_CREATED}
MSFT_NetTransactInvalid             {}                   {SECURITY_DESCRIPTOR, TIME_CREATED}
MSFT_NetServiceNotInteractive       {}                   {SECURITY_DESCRIPTOR, Service, TIME_CREATED}
MSFT_NetTakeOwnership               {}                   {RegistryKey, SECURITY_DESCRIPTOR, TIME_CREATED}
MSFT_NetServiceConfigBackoutFailed  {}                   {ConfigField, SECURITY_DESCRIPTOR, Service, TIME_CREATED}
MSFT_NetServiceShutdownFailed       {}                   {SECURITY_DESCRIPTOR, Service, TIME_CREATED}
MSFT_NetServiceStartHung            {}                   {SECURITY_DESCRIPTOR, Service, TIME_CREATED}
MSFT_NetServiceStopControlSuccess   {}                   {Comment, Control, Reason, ReasonText...}
MSFT_NetServiceSlowStartup          {}                   {SECURITY_DESCRIPTOR, Service, StartupTime, TIME_CREATED}
MSFT_NetCallToFunctionFailed        {}                   {Error, FunctionName, SECURITY_DESCRIPTOR, TIME_CREATED}
MSFT_NetBadAccount                  {}                   {SECURITY_DESCRIPTOR, TIME_CREATED}
MSFT_NetBadServiceState             {}                   {SECURITY_DESCRIPTOR, Service, State, TIME_CREATED}
MSFT_NetConnectionTimeout           {}                   {Milliseconds, SECURITY_DESCRIPTOR, Service, TIME_CREATED}
MSFT_NetCircularDependencyAuto      {}                   {SECURITY_DESCRIPTOR, TIME_CREATED}
MSFT_NetServiceStartTypeChanged     {}                   {NewStartType, OldStartType, SECURITY_DESCRIPTOR, Service...}
MSFT_NetServiceLogonTypeNotGranted  {}                   {Account, Error, SECURITY_DESCRIPTOR, Service...}
MSFT_NetServiceStartFailedGroup     {}                   {Group, SECURITY_DESCRIPTOR, Service, TIME_CREATED}
MSFT_NetDependOnLaterService        {}                   {SECURITY_DESCRIPTOR, Service, TIME_CREATED}
MSFT_NetFirstLogonFailedII          {}                   {Account, Error, SECURITY_DESCRIPTOR, Service...}
MSFT_NetServiceDifferentPIDConne... {}                   {ActualPID, ExpectedPID, SECURITY_DESCRIPTOR, Service...}
MSFT_NetServiceCrashNoAction        {}                   {SECURITY_DESCRIPTOR, Service, TIME_CREATED, TimesFailed}
MSFT_NetCircularDependencyDemand    {}                   {SECURITY_DESCRIPTOR, Service, TIME_CREATED}
MSFT_NetServiceExitFailed           {}                   {Error, SECURITY_DESCRIPTOR, Service, TIME_CREATED}
MSFT_NetServiceStartFailedII        {}                   {DependedOnService, Error, SECURITY_DESCRIPTOR, Service...}
MSFT_NetServiceExitFailedSpecific   {}                   {Error, SECURITY_DESCRIPTOR, Service, TIME_CREATED}
MSFT_NetBootSystemDriversFailed     {}                   {DriverList, SECURITY_DESCRIPTOR, TIME_CREATED}
MSFT_NetServiceCrash                {}                   {Action, ActionDelay, ActionType, SECURITY_DESCRIPTOR...}
MSFT_NetServiceRecoveryFailed       {}                   {Action, ActionType, Error, SECURITY_DESCRIPTOR...}
MSFT_NetServiceStatusSuccess        {}                   {Control, SECURITY_DESCRIPTOR, Service, TIME_CREATED}
MSFT_NetTransactTimeout             {}                   {Milliseconds, SECURITY_DESCRIPTOR, Service, TIME_CREATED}
MSFT_NetFirstLogonFailed            {}                   {Error, SECURITY_DESCRIPTOR, TIME_CREATED}
MSFT_NetServiceControlSuccess       {}                   {Control, SECURITY_DESCRIPTOR, Service, sid...}
MSFT_NetServiceStartFailed          {}                   {Error, SECURITY_DESCRIPTOR, Service, TIME_CREATED}
MSFT_NetServiceStartFailedNone      {}                   {NonExistingService, SECURITY_DESCRIPTOR, Service, TIME_CREATED}
MSFT_NetReadfileTimeout             {}                   {Milliseconds, SECURITY_DESCRIPTOR, TIME_CREATED}
MSFT_NetRevertedToLastKnownGood     {}                   {SECURITY_DESCRIPTOR, TIME_CREATED}
MSFT_NetCallToFunctionFailedII      {}                   {Argument, Error, FunctionName, SECURITY_DESCRIPTOR...}
MSFT_NetDependOnLaterGroup          {}                   {SECURITY_DESCRIPTOR, Service, TIME_CREATED}
MSFT_WmiSelfEvent                   {}                   {SECURITY_DESCRIPTOR, TIME_CREATED}
MSFT_WmiEssEvent                    {}                   {SECURITY_DESCRIPTOR, TIME_CREATED}
MSFT_WmiThreadPoolEvent             {}                   {SECURITY_DESCRIPTOR, ThreadId, TIME_CREATED}
MSFT_WmiThreadPoolThreadCreated     {}                   {SECURITY_DESCRIPTOR, ThreadId, TIME_CREATED}
MSFT_WmiThreadPoolThreadDeleted     {}                   {SECURITY_DESCRIPTOR, ThreadId, TIME_CREATED}
MSFT_WmiRegisterNotificationSink    {}                   {Namespace, Query, QueryLanguage, SECURITY_DESCRIPTOR...}
MSFT_WmiFilterEvent                 {}                   {Name, Namespace, Query, QueryLanguage...}
MSFT_WmiFilterDeactivated           {}                   {Name, Namespace, Query, QueryLanguage...}
MSFT_WmiFilterActivated             {}                   {Name, Namespace, Query, QueryLanguage...}
MSFT_WmiCancelNotificationSink      {}                   {Namespace, Query, QueryLanguage, SECURITY_DESCRIPTOR...}
MSFT_WmiProviderEvent               {}                   {Namespace, ProviderName, SECURITY_DESCRIPTOR, TIME_CREATED}
MSFT_WmiConsumerProviderEvent       {}                   {Machine, Namespace, ProviderName, SECURITY_DESCRIPTOR...}
MSFT_WmiConsumerProviderSinkLoaded  {}                   {Consumer, Machine, Namespace, ProviderName...}
MSFT_WmiConsumerProviderSinkUnlo... {}                   {Consumer, Machine, Namespace, ProviderName...}
MSFT_WmiConsumerProviderUnloaded    {}                   {Machine, Namespace, ProviderName, SECURITY_DESCRIPTOR...}
MSFT_WmiConsumerProviderLoaded      {}                   {Machine, Namespace, ProviderName, SECURITY_DESCRIPTOR...}
Msft_WmiProvider_OperationEvent     {}                   {HostingGroup, HostingSpecification, Locale, Namespace...}
Msft_WmiProvider_ComServerLoadOp... {}                   {Clsid, HostingGroup, HostingSpecification, InProcServer...}
Msft_WmiProvider_OperationEvent_... {}                   {HostingGroup, HostingSpecification, Locale, Namespace...}
Msft_WmiProvider_PutInstanceAsyn... {}                   {Flags, HostingGroup, HostingSpecification, InstanceObject...}
Msft_WmiProvider_CreateInstanceE... {}                   {ClassName, Flags, HostingGroup, HostingSpecification...}
Msft_WmiProvider_DeleteInstanceA... {}                   {Flags, HostingGroup, HostingSpecification, Locale...}
Msft_WmiProvider_CancelQuery_Post   {}                   {HostingGroup, HostingSpecification, Locale, Namespace...}
Msft_WmiProvider_NewQuery_Post      {}                   {HostingGroup, HostingSpecification, Locale, Namespace...}
Msft_WmiProvider_ProvideEvents_Post {}                   {Flags, HostingGroup, HostingSpecification, Locale...}
Msft_WmiProvider_ExecQueryAsyncE... {}                   {Flags, HostingGroup, HostingSpecification, Locale...}
Msft_WmiProvider_AccessCheck_Post   {}                   {HostingGroup, HostingSpecification, Locale, Namespace...}
Msft_WmiProvider_CreateClassEnum... {}                   {Flags, HostingGroup, HostingSpecification, Locale...}
Msft_WmiProvider_DeleteClassAsyn... {}                   {ClassName, Flags, HostingGroup, HostingSpecification...}
Msft_WmiProvider_ExecMethodAsync... {}                   {Flags, HostingGroup, HostingSpecification, InputParameters...}
Msft_WmiProvider_GetObjectAsyncE... {}                   {Flags, HostingGroup, HostingSpecification, Locale...}
Msft_WmiProvider_PutClassAsyncEv... {}                   {ClassObject, Flags, HostingGroup, HostingSpecification...}
Msft_WmiProvider_InitializationO... {}                   {HostingGroup, HostingSpecification, Locale, Namespace...}
Msft_WmiProvider_InitializationO... {}                   {HostingGroup, HostingSpecification, Locale, Namespace...}
Msft_WmiProvider_LoadOperationFa... {}                   {Clsid, HostingGroup, HostingSpecification, InProcServer...}
Msft_WmiProvider_ComServerLoadOp... {}                   {Clsid, HostingGroup, HostingSpecification, InProcServer...}
Msft_WmiProvider_UnLoadOperation... {}                   {HostingGroup, HostingSpecification, Locale, Namespace...}
Msft_WmiProvider_LoadOperationEvent {}                   {Clsid, HostingGroup, HostingSpecification, InProcServer...}
Msft_WmiProvider_OperationEvent_Pre {}                   {HostingGroup, HostingSpecification, Locale, Namespace...}
Msft_WmiProvider_DeleteInstanceA... {}                   {Flags, HostingGroup, HostingSpecification, Locale...}
Msft_WmiProvider_AccessCheck_Pre    {}                   {HostingGroup, HostingSpecification, Locale, Namespace...}
Msft_WmiProvider_ExecQueryAsyncE... {}                   {Flags, HostingGroup, HostingSpecification, Locale...}
Msft_WmiProvider_DeleteClassAsyn... {}                   {ClassName, Flags, HostingGroup, HostingSpecification...}
Msft_WmiProvider_NewQuery_Pre       {}                   {HostingGroup, HostingSpecification, Locale, Namespace...}
Msft_WmiProvider_PutInstanceAsyn... {}                   {Flags, HostingGroup, HostingSpecification, InstanceObject...}
Msft_WmiProvider_CreateClassEnum... {}                   {Flags, HostingGroup, HostingSpecification, Locale...}
Msft_WmiProvider_ExecMethodAsync... {}                   {Flags, HostingGroup, HostingSpecification, InputParameters...}
Msft_WmiProvider_ProvideEvents_Pre  {}                   {Flags, HostingGroup, HostingSpecification, Locale...}
Msft_WmiProvider_CancelQuery_Pre    {}                   {HostingGroup, HostingSpecification, Locale, Namespace...}
Msft_WmiProvider_PutClassAsyncEv... {}                   {ClassObject, Flags, HostingGroup, HostingSpecification...}
Msft_WmiProvider_GetObjectAsyncE... {}                   {Flags, HostingGroup, HostingSpecification, Locale...}
Msft_WmiProvider_CreateInstanceE... {}                   {ClassName, Flags, HostingGroup, HostingSpecification...}
MSFT_WMI_GenericNonCOMEvent         {}                   {ProcessId, PropertyNames, PropertyValues, ProviderName...}
Win32_ComputerSystemEvent           {}                   {MachineName, SECURITY_DESCRIPTOR, TIME_CREATED}
Win32_ComputerShutdownEvent         {}                   {MachineName, SECURITY_DESCRIPTOR, TIME_CREATED, Type}
Win32_IP4RouteTableEvent            {}                   {SECURITY_DESCRIPTOR, TIME_CREATED}
MSFT_NCProvEvent                    {}                   {Namespace, ProviderName, Result, SECURITY_DESCRIPTOR...}
MSFT_NCProvCancelQuery              {}                   {ID, Namespace, ProviderName, Result...}
MSFT_NCProvClientConnected          {}                   {Inproc, Namespace, ProviderName, Result...}
MSFT_NCProvNewQuery                 {}                   {ID, Namespace, ProviderName, Query...}
MSFT_NCProvAccessCheck              {}                   {Namespace, ProviderName, Query, QueryLanguage...}
RegistryEvent                       {}                   {SECURITY_DESCRIPTOR, TIME_CREATED}
RegistryKeyChangeEvent              {}                   {Hive, KeyPath, SECURITY_DESCRIPTOR, TIME_CREATED}
RegistryTreeChangeEvent             {}                   {Hive, RootPath, SECURITY_DESCRIPTOR, TIME_CREATED}
RegistryValueChangeEvent            {}                   {Hive, KeyPath, SECURITY_DESCRIPTOR, TIME_CREATED...}
Win32_SystemTrace                   {}                   {SECURITY_DESCRIPTOR, TIME_CREATED}
Win32_ProcessTrace                  {}                   {ParentProcessID, ProcessID, ProcessName, SECURITY_DESCRIPTOR...}
Win32_ProcessStartTrace             {}                   {ParentProcessID, ProcessID, ProcessName, SECURITY_DESCRIPTOR...}
Win32_ProcessStopTrace              {}                   {ExitStatus, ParentProcessID, ProcessID, ProcessName...}
Win32_ModuleTrace                   {}                   {SECURITY_DESCRIPTOR, TIME_CREATED}
Win32_ModuleLoadTrace               {}                   {DefaultBase, FileName, ImageBase, ImageChecksum...}
Win32_ThreadTrace                   {}                   {ProcessID, SECURITY_DESCRIPTOR, ThreadID, TIME_CREATED}
Win32_ThreadStartTrace              {}                   {ProcessID, SECURITY_DESCRIPTOR, StackBase, StackLimit...}
Win32_ThreadStopTrace               {}                   {ProcessID, SECURITY_DESCRIPTOR, ThreadID, TIME_CREATED}
Win32_PowerManagementEvent          {}                   {EventType, OEMEventCode, SECURITY_DESCRIPTOR, TIME_CREATED}
Win32_DeviceChangeEvent             {}                   {EventType, SECURITY_DESCRIPTOR, TIME_CREATED}
Win32_SystemConfigurationChangeE... {}                   {EventType, SECURITY_DESCRIPTOR, TIME_CREATED}
Win32_VolumeChangeEvent             {}                   {DriveName, EventType, SECURITY_DESCRIPTOR, TIME_CREATED}
__EventGenerator                    {}                   {}
__TimerInstruction                  {}                   {SkipIfPassed, TimerId}
__AbsoluteTimerInstruction          {}                   {EventDateTime, SkipIfPassed, TimerId}
__IntervalTimerInstruction          {}                   {IntervalBetweenEvents, SkipIfPassed, TimerId}
__Provider                          {}                   {Name}
__Win32Provider                     {}                   {ClientLoadableCLSID, CLSID, Concurrency, DefaultMachineName...}
__SystemSecurity                    {GetSD, GetSecuri... {}
Win32_CollectionStatistics          {}                   {Collection, Stats}
Win32_NamedJobObjectStatistics      {}                   {Collection, Stats}
Win32_NTLogEvent                    {}                   {Category, CategoryString, ComputerName, Data...}
CIM_Configuration                   {}                   {Caption, Description, Name}
CIM_LogicalIdentity                 {}                   {SameElement, SystemElement}
Win32_ActiveRoute                   {}                   {SameElement, SystemElement}
Win32_AccountSID                    {}                   {Element, Setting}
CIM_Location                        {}                   {Address, Name, PhysicalPosition}
CIM_DependencyContext               {}                   {Context, Dependency}
Win32_SecurityDescriptorHelper      {Win32SDToSDDL, W... {}
CIM_Setting                         {}                   {Caption, Description, SettingID}
Win32_TimeZone                      {}                   {Bias, Caption, DaylightBias, DaylightDay...}
Win32_PageFileSetting               {}                   {Caption, Description, InitialSize, MaximumSize...}
Win32_Desktop                       {}                   {BorderWidth, Caption, CoolSwitch, CursorBlinkRate...}
Win32_ShadowContext                 {}                   {Caption, ClientAccessible, Description, Differential...}
Win32_MSIResource                   {}                   {Caption, Description, SettingID}
Win32_ServiceControl                {}                   {Arguments, Caption, Description, Event...}
Win32_Property                      {}                   {Caption, Description, ProductCode, Property...}
Win32_Patch                         {}                   {Attributes, Caption, Description, File...}
Win32_PatchPackage                  {}                   {Caption, Description, PatchID, ProductCode...}
Win32_Binary                        {}                   {Caption, Data, Description, Name...}
Win32_AutochkSetting                {}                   {Caption, Description, SettingID, UserInputDelay}
Win32_SerialPortConfiguration       {}                   {AbortReadWriteOnError, BaudRate, BinaryModeEnabled, BitsPerByte...}
CIM_MonitorResolution               {}                   {Caption, Description, HorizontalResolution, MaxRefreshRate...}
Win32_StartupCommand                {}                   {Caption, Command, Description, Location...}
Win32_BootConfiguration             {}                   {BootDirectory, Caption, ConfigurationPath, Description...}
Win32_NetworkLoginProfile           {}                   {AccountExpires, AuthorizationFlags, BadPasswordCount, Caption...}
Win32_NamedJobObjectLimitSetting    {}                   {ActiveProcessLimit, Affinity, Caption, Description...}
CIM_VideoControllerResolution       {}                   {Caption, Description, HorizontalResolution, MaxRefreshRate...}
Win32_NamedJobObjectSecLimitSetting {}                   {Caption, Description, PrivilegesToDelete, RestrictedSIDs...}
Win32_DisplayConfiguration          {}                   {BitsPerPel, Caption, Description, DeviceName...}
Win32_NetworkAdapterConfiguration   {EnableDHCP, Rene... {ArpAlwaysSourceRoute, ArpUseEtherSNAP, Caption, DatabasePath...}
Win32_QuotaSetting                  {}                   {Caption, DefaultLimit, DefaultWarningLimit, Description...}
Win32_SecuritySetting               {GetSecurityDescr... {Caption, ControlFlags, Description, SettingID}
Win32_LogicalFileSecuritySetting    {GetSecurityDescr... {Caption, ControlFlags, Description, OwnerPermissions...}
Win32_LogicalShareSecuritySetting   {GetSecurityDescr... {Caption, ControlFlags, Description, Name...}
Win32_DisplayControllerConfigura... {}                   {BitsPerPixel, Caption, ColorPlanes, Description...}
Win32_WMISetting                    {}                   {ASPScriptDefaultNamespace, ASPScriptEnabled, AutorecoverMofs, AutoStartWin9X...}
Win32_OSRecoveryConfiguration       {}                   {AutoReboot, Caption, DebugFilePath, DebugInfoType...}
Win32_COMSetting                    {}                   {Caption, Description, SettingID}
Win32_ClassicCOMClassSetting        {}                   {AppID, AutoConvertToClsid, AutoTreatAsClsid, Caption...}
Win32_DCOMApplicationSetting        {GetLaunchSecurit... {AppID, AuthenticationLevel, Caption, CustomSurrogate...}
Win32_VideoConfiguration            {}                   {ActualColorResolution, AdapterChipType, AdapterCompatibility, AdapterDACType...}
Win32_ODBCAttribute                 {}                   {Attribute, Caption, Description, Driver...}
Win32_ODBCSourceAttribute           {}                   {Attribute, Caption, DataSource, Description...}
ScriptingStandardConsumerSetting    {}                   {Caption, Description, MaximumScripts, SettingID...}
Win32_PrinterConfiguration          {}                   {BitsPerPel, Caption, Collate, Color...}
Win32_CurrentTime                   {}                   {Day, DayOfWeek, Hour, Milliseconds...}
Win32_UTCTime                       {}                   {Day, DayOfWeek, Hour, Milliseconds...}
Win32_LocalTime                     {}                   {Day, DayOfWeek, Hour, Milliseconds...}
CIM_FRU                             {}                   {Caption, Description, FRUNumber, IdentifyingNumber...}
CIM_Action                          {Invoke}             {ActionID, Caption, Description, Direction...}
Win32_ShortcutAction                {Invoke}             {ActionID, Arguments, Caption, Description...}
CIM_RebootAction                    {Invoke}             {ActionID, Caption, Description, Direction...}
Win32_ExtensionInfoAction           {Invoke}             {ActionID, Argument, Caption, Command...}
CIM_DirectoryAction                 {Invoke}             {ActionID, Caption, Description, Direction...}
CIM_CreateDirectoryAction           {Invoke}             {ActionID, Caption, Description, Direction...}
Win32_CreateFolderAction            {Invoke}             {ActionID, Caption, Description, Direction...}
CIM_RemoveDirectoryAction           {Invoke}             {ActionID, Caption, Description, Direction...}
Win32_RegistryAction                {Invoke}             {ActionID, Caption, Description, Direction...}
Win32_ClassInfoAction               {Invoke}             {ActionID, AppID, Argument, Caption...}
CIM_ModifySettingAction             {Invoke}             {ActionID, ActionType, Caption, Description...}
Win32_SelfRegModuleAction           {Invoke}             {ActionID, Caption, Cost, Description...}
Win32_TypeLibraryAction             {Invoke}             {ActionID, Caption, Cost, Description...}
CIM_ExecuteProgram                  {Invoke}             {ActionID, Caption, CommandLine, Description...}
Win32_BindImageAction               {Invoke}             {ActionID, Caption, Description, Direction...}
Win32_RemoveIniAction               {Invoke}             {Action, ActionID, Caption, Description...}
Win32_MIMEInfoAction                {Invoke}             {ActionID, Caption, CLSID, ContentType...}
Win32_FontInfoAction                {Invoke}             {ActionID, Caption, Description, Direction...}
Win32_PublishComponentAction        {Invoke}             {ActionID, AppData, Caption, ComponentID...}
CIM_FileAction                      {Invoke}             {ActionID, Caption, Description, Direction...}
Win32_MoveFileAction                {Invoke}             {ActionID, Caption, Description, DestFolder...}
CIM_CopyFileAction                  {Invoke}             {ActionID, Caption, DeleteAfterCopy, Description...}
Win32_DuplicateFileAction           {Invoke}             {ActionID, Caption, DeleteAfterCopy, Description...}
CIM_RemoveFileAction                {Invoke}             {ActionID, Caption, Description, Direction...}
Win32_RemoveFileAction              {Invoke}             {ActionID, Caption, Description, Direction...}
Win32_ProductResource               {}                   {Product, Resource}
Win32_FolderRedirectionHealth       {}                   {HealthStatus, LastSuccessfulSyncTime, LastSyncStatus, LastSyncTime...}
Win32_MountPoint                    {}                   {Directory, Volume}
CIM_Statistics                      {}                   {Element, Stats}
CIM_ErrorCountersForDevice          {}                   {Element, Stats}
Msft_Providers                      {Suspend, Resume,... {HostingGroup, HostingSpecification, HostProcessIdentifier, Locale...}
Win32_UserProfile                   {ChangeOwner}        {AppDataRoaming, Contacts, Desktop, Documents...}
CIM_RelatedStatistics               {}                   {RelatedStats, Stats}
CIM_Export                          {}                   {Directory, ExportedDirectoryName, LocalFS}
Win32_RoamingProfileMachineConfi... {}                   {AddAdminGroupToRUPEnabled, AllowCrossForestUserPolicy, BackgroundUploadParams, DeleteProfilesOlderDays...}
Win32_ManagedSystemElementResource  {}                   {}
Win32_SoftwareElementResource       {}                   {Element, Setting}
CIM_FRUPhysicalElements             {}                   {Component, FRU}
CIM_ParticipatesInSet               {}                   {Element, Set}
CIM_FromDirectoryAction             {}                   {FileName, SourceDirectory}
Win32_SID                           {}                   {AccountName, BinaryRepresentation, ReferencedDomainName, SID...}
CIM_ElementCapacity                 {}                   {Capacity, Element}
Win32_ActionCheck                   {}                   {Action, Check}
CIM_ElementSetting                  {}                   {Element, Setting}
Win32_UserDesktop                   {}                   {Element, Setting}
CIM_MonitorSetting                  {}                   {Element, Setting}
Win32_DeviceSettings                {}                   {Element, Setting}
Win32_PrinterSetting                {}                   {Element, Setting}
Win32_NetworkAdapterSetting         {}                   {Element, Setting}
Win32_SerialPortSetting             {}                   {Element, Setting}
Win32_SystemSetting                 {}                   {Element, Setting}
Win32_SystemProgramGroups           {}                   {Element, Setting}
Win32_SystemBootConfiguration       {}                   {Element, Setting}
Win32_SystemTimeZone                {}                   {Element, Setting}
Win32_SystemDesktop                 {}                   {Element, Setting}
Win32_ClassicCOMClassSettings       {}                   {Element, Setting}
Win32_VolumeQuota                   {}                   {Element, Setting}
Win32_WMIElementSetting             {}                   {Element, Setting}
Win32_COMApplicationSettings        {}                   {Element, Setting}
CIM_VideoSetting                    {}                   {Element, Setting}
Win32_VideoSettings                 {}                   {Element, Setting}
Win32_SecuritySettingOfObject       {}                   {Element, Setting}
Win32_SecuritySettingOfLogicalShare {}                   {Element, Setting}
Win32_SecuritySettingOfLogicalFile  {}                   {Element, Setting}
Win32_PageFileElementSetting        {}                   {Element, Setting}
Win32_OperatingSystemAutochkSetting {}                   {Element, Setting}
Win32_VolumeQuotaSetting            {}                   {Element, Setting}
CIM_ToDirectorySpecification        {}                   {DestinationDirectory, FileName}
CIM_ProductSoftwareFeatures         {}                   {Component, Product}
Win32_ProductSoftwareFeatures       {}                   {Component, Product}
Win32_ImplementedCategory           {}                   {Category, Component}
Win32_RoamingProfileUserConfigur... {}                   {DirectoriesToSyncAtLogonLogoff, ExcludedProfileDirs, IsConfiguredByWMI}
CIM_InstalledSoftwareElement        {}                   {Software, System}
Win32_InstalledSoftwareElement      {}                   {Software, System}
Win32_SoftwareFeatureCheck          {}                   {Check, Element}
Win32_LUIDandAttributes             {}                   {Attributes, LUID}
Win32_VolumeUserQuota               {}                   {Account, DiskSpaceUsed, Limit, Status...}
Msft_WmiProvider_Counters           {}                   {ProviderOperation_AccessCheck, ProviderOperation_CancelQuery, ProviderOperation_CreateClassEnumAsync, ProviderOperation_CreateInstanceEnumAsy...
Win32_LUID                          {}                   {HighPart, LowPart}
CIM_Check                           {Invoke}             {Caption, CheckID, CheckMode, Description...}
CIM_DiskSpaceCheck                  {Invoke}             {AvailableDiskSpace, Caption, CheckID, CheckMode...}
CIM_DirectorySpecification          {Invoke}             {Caption, CheckID, CheckMode, Description...}
Win32_DirectorySpecification        {Invoke}             {Caption, CheckID, CheckMode, DefaultDir...}
Win32_SoftwareElementCondition      {Invoke}             {Caption, CheckID, CheckMode, Condition...}
Win32_ODBCDriverSpecification       {Invoke}             {Caption, CheckID, CheckMode, Description...}
CIM_MemoryCheck                     {Invoke}             {Caption, CheckID, CheckMode, Description...}
Win32_ServiceSpecification          {Invoke}             {Caption, CheckID, CheckMode, Dependencies...}
CIM_FileSpecification               {Invoke}             {Caption, CheckID, CheckMode, CheckSum...}
Win32_FileSpecification             {Invoke}             {Attributes, Caption, CheckID, CheckMode...}
Win32_IniFileSpecification          {Invoke}             {Action, Caption, CheckID, CheckMode...}
CIM_SoftwareElementVersionCheck     {Invoke}             {Caption, CheckID, CheckMode, Description...}
CIM_SettingCheck                    {Invoke}             {Caption, CheckID, CheckMode, CheckType...}
Win32_LaunchCondition               {Invoke}             {Caption, CheckID, CheckMode, Condition...}
Win32_ODBCDataSourceSpecification   {Invoke}             {Caption, CheckID, CheckMode, DataSource...}
Win32_ODBCTranslatorSpecification   {Invoke}             {Caption, CheckID, CheckMode, Description...}
Win32_ProgIDSpecification           {Invoke}             {Caption, CheckID, CheckMode, Description...}
CIM_SwapSpaceCheck                  {Invoke}             {Caption, CheckID, CheckMode, Description...}
Win32_EnvironmentSpecification      {Invoke}             {Caption, CheckID, CheckMode, Description...}
Win32_ReserveCost                   {Invoke}             {Caption, CheckID, CheckMode, Description...}
CIM_VersionCompatibilityCheck       {Invoke}             {AllowDownVersion, AllowMultipleVersions, Caption, CheckID...}
CIM_OSVersionCheck                  {Invoke}             {Caption, CheckID, CheckMode, Description...}
Win32_Condition                     {Invoke}             {Caption, CheckID, CheckMode, Condition...}
CIM_ProductFRU                      {}                   {FRU, Product}
Win32_ShadowStorage                 {Create}             {AllocatedSpace, DiffVolume, MaxSpace, UsedSpace...}
Win32_DCOMApplicationAccessAllow... {}                   {Element, Setting}
StdRegProv                          {CreateKey, Delet... {}
CIM_FRUIncludesProduct              {}                   {Component, FRU}
Win32_FolderRedirection             {}                   {ContentsMoved, ContentsMovedOnPolicyRemoval, ContentsRenamedInLocalCache, ExclusiveRightsGranted...}
CIM_ProductPhysicalElements         {}                   {Component, Product}
CIM_CollectedMSEs                   {}                   {Collection, Member}
Win32_NamedJobObjectProcess         {}                   {Collection, Member}
CIM_PhysicalElementLocation         {}                   {Element, PhysicalLocation}
Win32_TokenPrivileges               {}                   {PrivilegeCount, Privileges}
CIM_CollectionOfMSEs                {}                   {Caption, CollectionID, Description}
Win32_NamedJobObject                {}                   {BasicUIRestrictions, Caption, CollectionID, Description}
CIM_FromDirectorySpecification      {}                   {FileName, SourceDirectory}
Win32_PnPDevice                     {}                   {SameElement, SystemElement}
CIM_StorageError                    {}                   {DeviceCreationClassName, DeviceID, EndingAddress, StartingAddress...}
Win32_ServiceSpecificationService   {}                   {Check, Element}
Win32_ShareToDirectory              {}                   {Share, SharedElement}
Win32_SettingCheck                  {}                   {Check, Setting}
Win32_PatchFile                     {}                   {Check, Setting}
Win32_ODBCDriverAttribute           {}                   {Check, Setting}
Win32_ODBCDataSourceAttribute       {}                   {Check, Setting}
Win32_ClientApplicationSetting      {}                   {Application, Client}
CIM_ElementConfiguration            {}                   {Configuration, Element}
Win32_RoamingUserHealthConfigura... {}                   {HealthStatusForTempProfiles, LastProfileDownloadIntervalCautionInHours, LastProfileDownloadIntervalUnhealthyInHours, LastProfileUploadInterva...
CIM_ReplacementSet                  {}                   {Description, Name}
Win32_UserStateConfigurationCont... {}                   {FolderRedirection, OfflineFiles, RoamingUserProfile}
Win32_ServerFeature                 {}                   {ID, Name, ParentID}
CIM_DirectorySpecificationFile      {}                   {DirectorySpecification, FileSpecification}
CIM_SettingContext                  {}                   {Context, Setting}
Win32_SecuritySettingOwner          {}                   {Owner, SecuritySetting}
Win32_LogicalFileOwner              {}                   {Owner, SecuritySetting}
CIM_ManagedSystemElement            {}                   {Caption, Description, InstallDate, Name...}
CIM_PhysicalElement                 {}                   {Caption, CreationClassName, Description, InstallDate...}
CIM_PhysicalComponent               {}                   {Caption, CreationClassName, Description, HotSwappable...}
CIM_PhysicalMedia                   {}                   {Capacity, Caption, CleanerMedia, CreationClassName...}
Win32_PhysicalMedia                 {}                   {Capacity, Caption, CleanerMedia, CreationClassName...}
CIM_Chip                            {}                   {Caption, CreationClassName, Description, FormFactor...}
CIM_PhysicalMemory                  {}                   {BankLabel, Capacity, Caption, CreationClassName...}
Win32_PhysicalMemory                {}                   {BankLabel, Capacity, Caption, CreationClassName...}
Win32_OnBoardDevice                 {}                   {Caption, CreationClassName, Description, DeviceType...}
CIM_PhysicalPackage                 {IsCompatible}       {Caption, CreationClassName, Depth, Description...}
CIM_Card                            {IsCompatible}       {Caption, CreationClassName, Depth, Description...}
Win32_BaseBoard                     {IsCompatible}       {Caption, ConfigOptions, CreationClassName, Depth...}
CIM_PhysicalFrame                   {IsCompatible}       {AudibleAlarm, BreachDescription, CableManagementStrategy, Caption...}
CIM_Rack                            {IsCompatible}       {AudibleAlarm, BreachDescription, CableManagementStrategy, Caption...}
CIM_Chassis                         {IsCompatible}       {AudibleAlarm, BreachDescription, CableManagementStrategy, Caption...}
Win32_SystemEnclosure               {IsCompatible}       {AudibleAlarm, BreachDescription, CableManagementStrategy, Caption...}
Win32_PhysicalMemoryArray           {IsCompatible}       {Caption, CreationClassName, Depth, Description...}
CIM_PhysicalConnector               {}                   {Caption, ConnectorPinout, ConnectorType, CreationClassName...}
CIM_Slot                            {}                   {Caption, ConnectorPinout, ConnectorType, CreationClassName...}
Win32_SystemSlot                    {}                   {Caption, ConnectorPinout, ConnectorType, CreationClassName...}
Win32_PortConnector                 {}                   {Caption, ConnectorPinout, ConnectorType, CreationClassName...}
CIM_PhysicalLink                    {}                   {Caption, CreationClassName, Description, InstallDate...}
CIM_LogicalElement                  {}                   {Caption, Description, InstallDate, Name...}
CIM_Thread                          {}                   {Caption, CreationClassName, CSCreationClassName, CSName...}
Win32_Thread                        {}                   {Caption, CreationClassName, CSCreationClassName, CSName...}
Win32_COMApplication                {}                   {Caption, Description, InstallDate, Name...}
Win32_DCOMApplication               {}                   {AppID, Caption, Description, InstallDate...}
CIM_Job                             {}                   {Caption, Description, ElapsedTime, InstallDate...}
Win32_ScheduledJob                  {Create, Delete}     {Caption, Command, DaysOfMonth, DaysOfWeek...}
Win32_PrintJob                      {Pause, Resume}      {Caption, Color, DataType, Description...}
Win32_ServerSession                 {}                   {ActiveTime, Caption, ClientType, ComputerName...}
CIM_System                          {}                   {Caption, CreationClassName, Description, InstallDate...}
CIM_ComputerSystem                  {}                   {Caption, CreationClassName, Description, InstallDate...}
CIM_UnitaryComputerSystem           {SetPowerState}      {Caption, CreationClassName, Description, InitialLoadInfo...}
Win32_ComputerSystem                {SetPowerState, R... {AdminPasswordStatus, AutomaticManagedPagefile, AutomaticResetBootOption, AutomaticResetCapability...}
CIM_ApplicationSystem               {}                   {Caption, CreationClassName, Description, InstallDate...}
Win32_NTDomain                      {}                   {Caption, ClientSiteName, CreationClassName, DcSiteName...}
CIM_SoftwareFeature                 {}                   {Caption, Description, IdentifyingNumber, InstallDate...}
Win32_SoftwareFeature               {Reinstall, Confi... {Accesses, Attributes, Caption, Description...}
CIM_VideoBIOSFeature                {}                   {Caption, CharacteristicDescriptions, Characteristics, Description...}
CIM_BIOSFeature                     {}                   {Caption, CharacteristicDescriptions, Characteristics, Description...}
CIM_LogicalDevice                   {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
CIM_Sensor                          {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
CIM_BinarySensor                    {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
CIM_MultiStateSensor                {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
CIM_DiscreteSensor                  {SetPowerState, R... {AcceptableValues, Availability, Caption, ConfigManagerErrorCode...}
CIM_NumericSensor                   {SetPowerState, R... {Accuracy, Availability, Caption, ConfigManagerErrorCode...}
CIM_TemperatureSensor               {SetPowerState, R... {Accuracy, Availability, Caption, ConfigManagerErrorCode...}
Win32_TemperatureProbe              {SetPowerState, R... {Accuracy, Availability, Caption, ConfigManagerErrorCode...}
CIM_Tachometer                      {SetPowerState, R... {Accuracy, Availability, Caption, ConfigManagerErrorCode...}
CIM_VoltageSensor                   {SetPowerState, R... {Accuracy, Availability, Caption, ConfigManagerErrorCode...}
Win32_VoltageProbe                  {SetPowerState, R... {Accuracy, Availability, Caption, ConfigManagerErrorCode...}
CIM_CurrentSensor                   {SetPowerState, R... {Accuracy, Availability, Caption, ConfigManagerErrorCode...}
Win32_CurrentProbe                  {SetPowerState, R... {Accuracy, Availability, Caption, ConfigManagerErrorCode...}
Win32_Bus                           {SetPowerState, R... {Availability, BusNum, BusType, Caption...}
CIM_UserDevice                      {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
CIM_Keyboard                        {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
Win32_Keyboard                      {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
CIM_Display                         {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
CIM_FlatPanel                       {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
CIM_DesktopMonitor                  {SetPowerState, R... {Availability, Bandwidth, Caption, ConfigManagerErrorCode...}
Win32_DesktopMonitor                {SetPowerState, R... {Availability, Bandwidth, Caption, ConfigManagerErrorCode...}
CIM_PointingDevice                  {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
Win32_PointingDevice                {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
CIM_USBDevice                       {SetPowerState, R... {Availability, Caption, ClassCode, ConfigManagerErrorCode...}
CIM_USBHub                          {SetPowerState, R... {Availability, Caption, ClassCode, ConfigManagerErrorCode...}
Win32_USBHub                        {SetPowerState, R... {Availability, Caption, ClassCode, ConfigManagerErrorCode...}
CIM_NetworkAdapter                  {SetPowerState, R... {AutoSense, Availability, Caption, ConfigManagerErrorCode...}
Win32_NetworkAdapter                {SetPowerState, R... {AdapterType, AdapterTypeId, AutoSense, Availability...}
CIM_AlarmDevice                     {SetPowerState, R... {AudibleAlarm, Availability, Caption, ConfigManagerErrorCode...}
CIM_Battery                         {SetPowerState, R... {Availability, BatteryStatus, Caption, Chemistry...}
Win32_Battery                       {SetPowerState, R... {Availability, BatteryRechargeTime, BatteryStatus, Caption...}
Win32_PortableBattery               {SetPowerState, R... {Availability, BatteryStatus, CapacityMultiplier, Caption...}
Win32_SoundDevice                   {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
Win32_MotherboardDevice             {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
CIM_PowerSupply                     {SetPowerState, R... {ActiveInputVoltage, Availability, Caption, ConfigManagerErrorCode...}
CIM_UninterruptiblePowerSupply      {SetPowerState, R... {ActiveInputVoltage, Availability, Caption, ConfigManagerErrorCode...}
CIM_MediaAccessDevice               {SetPowerState, R... {Availability, Capabilities, CapabilityDescriptions, Caption...}
CIM_DiskDrive                       {SetPowerState, R... {Availability, Capabilities, CapabilityDescriptions, Caption...}
Win32_DiskDrive                     {SetPowerState, R... {Availability, BytesPerSector, Capabilities, CapabilityDescriptions...}
CIM_DisketteDrive                   {SetPowerState, R... {Availability, Capabilities, CapabilityDescriptions, Caption...}
Win32_FloppyDrive                   {SetPowerState, R... {Availability, Capabilities, CapabilityDescriptions, Caption...}
CIM_TapeDrive                       {SetPowerState, R... {Availability, Capabilities, CapabilityDescriptions, Caption...}
Win32_TapeDrive                     {SetPowerState, R... {Availability, Capabilities, CapabilityDescriptions, Caption...}
CIM_MagnetoOpticalDrive             {SetPowerState, R... {Availability, Capabilities, CapabilityDescriptions, Caption...}
CIM_CDROMDrive                      {SetPowerState, R... {Availability, Capabilities, CapabilityDescriptions, Caption...}
Win32_CDROMDrive                    {SetPowerState, R... {Availability, Capabilities, CapabilityDescriptions, Caption...}
CIM_WORMDrive                       {SetPowerState, R... {Availability, Capabilities, CapabilityDescriptions, Caption...}
CIM_Scanner                         {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
Win32_PnPEntity                     {SetPowerState, R... {Availability, Caption, ClassGuid, CompatibleID...}
CIM_PotsModem                       {SetPowerState, R... {AnswerMode, Availability, Caption, CompressionInfo...}
Win32_POTSModem                     {SetPowerState, R... {AnswerMode, AttachedTo, Availability, BlindOff...}
CIM_CoolingDevice                   {SetPowerState, R... {ActiveCooling, Availability, Caption, ConfigManagerErrorCode...}
CIM_HeatPipe                        {SetPowerState, R... {ActiveCooling, Availability, Caption, ConfigManagerErrorCode...}
Win32_HeatPipe                      {SetPowerState, R... {ActiveCooling, Availability, Caption, ConfigManagerErrorCode...}
CIM_Refrigeration                   {SetPowerState, R... {ActiveCooling, Availability, Caption, ConfigManagerErrorCode...}
Win32_Refrigeration                 {SetPowerState, R... {ActiveCooling, Availability, Caption, ConfigManagerErrorCode...}
CIM_Fan                             {SetPowerState, R... {ActiveCooling, Availability, Caption, ConfigManagerErrorCode...}
Win32_Fan                           {SetPowerState, R... {ActiveCooling, Availability, Caption, ConfigManagerErrorCode...}
CIM_Printer                         {SetPowerState, R... {Availability, AvailableJobSheets, Capabilities, CapabilityDescriptions...}
Win32_Printer                       {SetPowerState, R... {Attributes, Availability, AvailableJobSheets, AveragePagesPerMinute...}
CIM_Controller                      {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
CIM_ManagementController            {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
CIM_SCSIController                  {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
Win32_SCSIController                {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
CIM_InfraredController              {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
Win32_InfraredDevice                {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
CIM_PCIController                   {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
CIM_PCMCIAController                {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
Win32_PCMCIAController              {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
Win32_FloppyController              {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
CIM_VideoController                 {SetPowerState, R... {AcceleratorCapabilities, Availability, CapabilityDescriptions, Caption...}
CIM_PCVideoController               {SetPowerState, R... {AcceleratorCapabilities, Availability, CapabilityDescriptions, Caption...}
Win32_VideoController               {SetPowerState, R... {AcceleratorCapabilities, AdapterCompatibility, AdapterDACType, AdapterRAM...}
CIM_USBController                   {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
Win32_USBController                 {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
CIM_SerialController                {SetPowerState, R... {Availability, Capabilities, CapabilityDescriptions, Caption...}
Win32_SerialPort                    {SetPowerState, R... {Availability, Binary, Capabilities, CapabilityDescriptions...}
CIM_ParallelController              {SetPowerState, R... {Availability, Capabilities, CapabilityDescriptions, Caption...}
Win32_ParallelPort                  {SetPowerState, R... {Availability, Capabilities, CapabilityDescriptions, Caption...}
Win32_IDEController                 {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
Win32_1394Controller                {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
CIM_StorageExtent                   {SetPowerState, R... {Access, Availability, BlockSize, Caption...}
CIM_Memory                          {SetPowerState, R... {Access, AdditionalErrorData, Availability, BlockSize...}
CIM_VolatileStorage                 {SetPowerState, R... {Access, AdditionalErrorData, Availability, BlockSize...}
CIM_NonVolatileStorage              {SetPowerState, R... {Access, AdditionalErrorData, Availability, BlockSize...}
CIM_CacheMemory                     {SetPowerState, R... {Access, AdditionalErrorData, Associativity, Availability...}
Win32_CacheMemory                   {SetPowerState, R... {Access, AdditionalErrorData, Associativity, Availability...}
CIM_StorageVolume                   {SetPowerState, R... {Access, Availability, BlockSize, Caption...}
Win32_Volume                        {SetPowerState, R... {Access, Automount, Availability, BlockSize...}
CIM_PhysicalExtent                  {SetPowerState, R... {Access, Availability, BlockSize, Caption...}
Win32_SMBIOSMemory                  {SetPowerState, R... {Access, AdditionalErrorData, Availability, BlockSize...}
Win32_MemoryArray                   {SetPowerState, R... {Access, AdditionalErrorData, Availability, BlockSize...}
Win32_MemoryDevice                  {SetPowerState, R... {Access, AdditionalErrorData, Availability, BlockSize...}
CIM_ProtectedSpaceExtent            {SetPowerState, R... {Access, Availability, BlockSize, Caption...}
CIM_AggregatePSExtent               {SetPowerState, R... {Access, Availability, BlockSize, Caption...}
CIM_AggregatePExtent                {SetPowerState, R... {Access, Availability, BlockSize, Caption...}
CIM_VolumeSet                       {SetPowerState, R... {Access, Availability, BlockSize, Caption...}
CIM_LogicalDisk                     {SetPowerState, R... {Access, Availability, BlockSize, Caption...}
Win32_LogicalDisk                   {SetPowerState, R... {Access, Availability, BlockSize, Caption...}
Win32_MappedLogicalDisk             {SetPowerState, R... {Access, Availability, BlockSize, Caption...}
CIM_DiskPartition                   {SetPowerState, R... {Access, Availability, BlockSize, Bootable...}
Win32_DiskPartition                 {SetPowerState, R... {Access, Availability, BlockSize, Bootable...}
CIM_Processor                       {SetPowerState, R... {AddressWidth, Availability, Caption, ConfigManagerErrorCode...}
Win32_Processor                     {SetPowerState, R... {AddressWidth, Architecture, Availability, Caption...}
Win32_OptionalFeature               {}                   {Caption, Description, InstallDate, InstallState...}
Win32_DfsNode                       {Create}             {Caption, Description, InstallDate, Name...}
Win32_ComponentCategory             {}                   {Caption, CategoryId, Description, InstallDate...}
Win32_ProgramGroupOrItem            {}                   {Caption, Description, InstallDate, Name...}
Win32_LogicalProgramGroupItem       {}                   {Caption, Description, InstallDate, Name...}
Win32_LogicalProgramGroup           {}                   {Caption, Description, GroupName, InstallDate...}
Win32_NetworkConnection             {}                   {AccessMask, Caption, Comment, ConnectionState...}
Win32_COMClass                      {}                   {Caption, Description, InstallDate, Name...}
Win32_ClassicCOMClass               {}                   {Caption, ComponentId, Description, InstallDate...}
Win32_Account                       {}                   {Caption, Description, Domain, InstallDate...}
Win32_UserAccount                   {Rename}             {AccountType, Caption, Description, Disabled...}
Win32_Group                         {Rename}             {Caption, Description, Domain, InstallDate...}
Win32_SystemAccount                 {}                   {Caption, Description, Domain, InstallDate...}
CIM_Service                         {StartService, St... {Caption, CreationClassName, Description, InstallDate...}
Win32_BaseService                   {StartService, St... {AcceptPause, AcceptStop, Caption, CreationClassName...}
Win32_SystemDriver                  {StartService, St... {AcceptPause, AcceptStop, Caption, CreationClassName...}
Win32_Service                       {StartService, St... {AcceptPause, AcceptStop, Caption, CheckPoint...}
Win32_TerminalService               {StartService, St... {AcceptPause, AcceptStop, Caption, CheckPoint...}
CIM_BootService                     {StartService, St... {Caption, CreationClassName, Description, InstallDate...}
Win32_PnPSignedDriver               {StartService, St... {Caption, ClassGuid, CompatID, CreationClassName...}
CIM_ClusteringService               {StartService, St... {Caption, CreationClassName, Description, InstallDate...}
Win32_ApplicationService            {StartService, St... {Caption, CreationClassName, Description, InstallDate...}
Win32_PrinterDriver                 {StartService, St... {Caption, ConfigFile, CreationClassName, DataFile...}
CIM_ServiceAccessPoint              {}                   {Caption, CreationClassName, Description, InstallDate...}
Win32_TCPIPPrinterPort              {}                   {ByteCount, Caption, CreationClassName, Description...}
CIM_ClusteringSAP                   {}                   {Caption, CreationClassName, Description, InstallDate...}
CIM_BootSAP                         {}                   {Caption, CreationClassName, Description, InstallDate...}
Win32_CommandLineAccess             {}                   {Caption, CommandLine, CreationClassName, Description...}
CIM_SystemResource                  {}                   {Caption, Description, InstallDate, Name...}
CIM_MemoryMappedIO                  {}                   {Caption, CreationClassName, CSCreationClassName, CSName...}
Win32_SystemMemoryResource          {}                   {Caption, CreationClassName, CSCreationClassName, CSName...}
Win32_PortResource                  {}                   {Alias, Caption, CreationClassName, CSCreationClassName...}
Win32_DeviceMemoryAddress           {}                   {Caption, CreationClassName, CSCreationClassName, CSName...}
CIM_IRQ                             {}                   {Availability, Caption, CreationClassName, CSCreationClassName...}
Win32_IRQResource                   {}                   {Availability, Caption, CreationClassName, CSCreationClassName...}
Win32_Environment                   {}                   {Caption, Description, InstallDate, Name...}
CIM_DMA                             {}                   {AddressSize, Availability, BurstMode, ByteMode...}
Win32_DMAChannel                    {}                   {AddressSize, Availability, BurstMode, ByteMode...}
Win32_Share                         {Create, SetShare... {AccessMask, AllowMaximum, Caption, Description...}
Win32_ClusterShare                  {Create, SetShare... {AccessMask, AllowMaximum, Caption, Description...}
CIM_FileSystem                      {}                   {AvailableSpace, BlockSize, Caption, CasePreserved...}
CIM_RemoteFileSystem                {}                   {AvailableSpace, BlockSize, Caption, CasePreserved...}
CIM_NFS                             {}                   {AttributeCaching, AttributeCachingForDirectoriesMax, AttributeCachingForDirectoriesMin, AttributeCachingForRegularFilesMax...}
CIM_LocalFileSystem                 {}                   {AvailableSpace, BlockSize, Caption, CasePreserved...}
Win32_NetworkProtocol               {}                   {Caption, ConnectionlessService, Description, GuaranteesDelivery...}
Win32_ShadowProvider                {}                   {Caption, CLSID, Description, ID...}
CIM_RedundancyGroup                 {}                   {Caption, CreationClassName, Description, InstallDate...}
CIM_ExtraCapacityGroup              {}                   {Caption, CreationClassName, Description, InstallDate...}
CIM_StorageRedundancyGroup          {}                   {Caption, CreationClassName, Description, InstallDate...}
CIM_SpareGroup                      {}                   {Caption, CreationClassName, Description, InstallDate...}
Win32_QuickFixEngineering           {}                   {Caption, CSName, Description, FixComments...}
Win32_IP4RouteTable                 {}                   {Age, Caption, Description, Destination...}
Win32_ShadowCopy                    {Create, Revert}     {Caption, ClientAccessible, Count, Description...}
Win32_LoadOrderGroup                {}                   {Caption, Description, DriverEnabled, GroupOrder...}
CIM_Process                         {}                   {Caption, CreationClassName, CreationDate, CSCreationClassName...}
Win32_Process                       {Create, Terminat... {Caption, CommandLine, CreationClassName, CreationDate...}
Win32_Session                       {}                   {Caption, Description, InstallDate, Name...}
Win32_LogonSession                  {}                   {AuthenticationPackage, Caption, Description, InstallDate...}
Win32_ServerConnection              {}                   {ActiveTime, Caption, ComputerName, ConnectionID...}
CIM_JobDestination                  {}                   {Caption, CreationClassName, Description, InstallDate...}
Win32_DfsTarget                     {}                   {Caption, Description, InstallDate, LinkName...}
Win32_NetworkClient                 {}                   {Caption, Description, InstallDate, Manufacturer...}
Win32_PageFileUsage                 {}                   {AllocatedBaseSize, Caption, CurrentUsage, Description...}
CIM_OperatingSystem                 {Reboot, Shutdown}   {Caption, CreationClassName, CSCreationClassName, CSName...}
Win32_OperatingSystem               {Reboot, Shutdown... {BootDevice, BuildNumber, BuildType, Caption...}
CIM_LogicalFile                     {TakeOwnerShip, C... {AccessMask, Archive, Caption, Compressed...}
CIM_Directory                       {TakeOwnerShip, C... {AccessMask, Archive, Caption, Compressed...}
Win32_Directory                     {TakeOwnerShip, C... {AccessMask, Archive, Caption, Compressed...}
CIM_DeviceFile                      {TakeOwnerShip, C... {AccessMask, Archive, Caption, Compressed...}
CIM_DataFile                        {TakeOwnerShip, C... {AccessMask, Archive, Caption, Compressed...}
Win32_ShortcutFile                  {TakeOwnerShip, C... {AccessMask, Archive, Caption, Compressed...}
Win32_CodecFile                     {TakeOwnerShip, C... {AccessMask, Archive, Caption, Compressed...}
Win32_NTEventlogFile                {TakeOwnerShip, C... {AccessMask, Archive, Caption, Compressed...}
Win32_PageFile                      {TakeOwnerShip, C... {AccessMask, Archive, Caption, Compressed...}
Win32_IP4PersistedRouteTable        {}                   {Caption, Description, Destination, InstallDate...}
Win32_Registry                      {}                   {Caption, CurrentSize, Description, InstallDate...}
CIM_SoftwareElement                 {}                   {BuildNumber, Caption, CodeSet, Description...}
CIM_BIOSElement                     {}                   {BuildNumber, Caption, CodeSet, Description...}
Win32_BIOS                          {}                   {BiosCharacteristics, BIOSVersion, BuildNumber, Caption...}
Win32_SoftwareElement               {}                   {Attributes, BuildNumber, Caption, CodeSet...}
CIM_VideoBIOSElement                {}                   {BuildNumber, Caption, CodeSet, Description...}
NTEventlogProviderConfig            {}                   {LastBootUpTime}
Win32_ShortcutSAP                   {}                   {Action, Element}
Win32_MethodParameterClass          {}                   {}
Win32_ProcessStartup                {}                   {CreateFlags, EnvironmentVariables, ErrorMode, FillAttribute...}
Win32_PingStatus                    {}                   {Address, BufferSize, NoFragmentation, PrimaryAddressResolutionStatus...}
CIM_ProductSupport                  {}                   {Product, Support}
CIM_AdjacentSlots                   {}                   {DistanceBetweenSlots, SharedSlots, SlotA, SlotB}
CIM_SoftwareElementChecks           {}                   {Check, Element, Phase}
Win32_SoftwareElementCheck          {}                   {Check, Element, Phase}
Win32_ODBCDriverSoftwareElement     {}                   {Check, Element, Phase}
CIM_Component                       {}                   {GroupComponent, PartComponent}
CIM_SystemComponent                 {}                   {GroupComponent, PartComponent}
Win32_SystemServices                {}                   {GroupComponent, PartComponent}
Win32_SystemNetworkConnections      {}                   {GroupComponent, PartComponent}
CIM_HostedFileSystem                {}                   {GroupComponent, PartComponent}
CIM_ComputerSystemResource          {}                   {GroupComponent, PartComponent}
Win32_SystemResources               {}                   {GroupComponent, PartComponent}
CIM_ComputerSystemMappedIO          {}                   {GroupComponent, PartComponent}
CIM_ComputerSystemDMA               {}                   {GroupComponent, PartComponent}
CIM_ComputerSystemIRQ               {}                   {GroupComponent, PartComponent}
Win32_SystemBIOS                    {}                   {GroupComponent, PartComponent}
Win32_SystemLoadOrderGroups         {}                   {GroupComponent, PartComponent}
Win32_SystemUsers                   {}                   {GroupComponent, PartComponent}
CIM_InstalledOS                     {}                   {GroupComponent, PartComponent, PrimaryOS}
Win32_SystemOperatingSystem         {}                   {GroupComponent, PartComponent, PrimaryOS}
CIM_SystemDevice                    {}                   {GroupComponent, PartComponent}
Win32_SystemDevices                 {}                   {GroupComponent, PartComponent}
Win32_ComputerSystemProcessor       {}                   {GroupComponent, PartComponent}
Win32_SystemPartitions              {}                   {GroupComponent, PartComponent}
Win32_SystemSystemDriver            {}                   {GroupComponent, PartComponent}
CIM_ApplicationSystemSoftwareFea... {}                   {GroupComponent, PartComponent}
Win32_SystemProcesses               {}                   {GroupComponent, PartComponent}
CIM_LinkHasConnector                {}                   {GroupComponent, PartComponent}
CIM_CollectionOfSensors             {}                   {GroupComponent, PartComponent}
CIM_ProcessThread                   {}                   {GroupComponent, PartComponent}
Win32_COMApplicationClasses         {}                   {GroupComponent, PartComponent}
Win32_ClassicCOMApplicationClasses  {}                   {GroupComponent, PartComponent}
CIM_DirectoryContainsFile           {}                   {GroupComponent, PartComponent}
CIM_FileStorage                     {}                   {GroupComponent, PartComponent}
Win32_UserInDomain                  {}                   {GroupComponent, PartComponent}
Win32_LoadOrderGroupServiceMembers  {}                   {GroupComponent, PartComponent}
CIM_OperatingSystemSoftwareFeature  {}                   {GroupComponent, PartComponent}
CIM_RedundancyComponent             {}                   {GroupComponent, PartComponent}
CIM_AggregateRedundancyComponent    {}                   {GroupComponent, PartComponent}
CIM_PExtentRedundancyComponent      {}                   {GroupComponent, PartComponent}
Win32_LogicalDiskRootDirectory      {}                   {GroupComponent, PartComponent}
CIM_SoftwareFeatureSoftwareElements {}                   {GroupComponent, PartComponent}
Win32_SoftwareFeatureSoftwareEle... {}                   {GroupComponent, PartComponent}
CIM_VideoBIOSFeatureVideoBIOSEle... {}                   {GroupComponent, PartComponent}
CIM_BIOSFeatureBIOSElements         {}                   {GroupComponent, PartComponent}
Win32_MemoryDeviceArray             {}                   {GroupComponent, PartComponent}
Win32_GroupInDomain                 {}                   {GroupComponent, PartComponent}
CIM_OSProcess                       {}                   {GroupComponent, PartComponent}
Win32_GroupUser                     {}                   {GroupComponent, PartComponent}
Win32_ProgramGroupContents          {}                   {GroupComponent, PartComponent}
Win32_SubDirectory                  {}                   {GroupComponent, PartComponent}
CIM_Container                       {}                   {GroupComponent, LocationWithinContainer, PartComponent}
CIM_ConnectorOnPackage              {}                   {GroupComponent, LocationWithinContainer, PartComponent}
CIM_PackageInChassis                {}                   {GroupComponent, LocationWithinContainer, PartComponent}
CIM_ChassisInRack                   {}                   {BottomU, GroupComponent, LocationWithinContainer, PartComponent}
CIM_PackagedComponent               {}                   {GroupComponent, LocationWithinContainer, PartComponent}
CIM_MemoryOnCard                    {}                   {GroupComponent, LocationWithinContainer, PartComponent}
Win32_PhysicalMemoryLocation        {}                   {GroupComponent, LocationWithinContainer, PartComponent}
CIM_CardOnCard                      {}                   {GroupComponent, LocationWithinContainer, MountOrSlotDescription, PartComponent}
Win32_FolderRedirectionUserConfi... {}                   {AppDataRoaming, Contacts, Desktop, Documents...}
Win32_Reliability                   {}                   {}
Win32_ReliabilityStabilityMetrics   {GetRecordCount}     {EndMeasurementDate, RelID, StartMeasurementDate, SystemStabilityIndex...}
Win32_ReliabilityRecords            {GetRecordCount}     {ComputerName, EventIdentifier, InsertionStrings, Logfile...}
Win32_NTLogEventLog                 {}                   {Log, Record}
Win32_DiskQuota                     {}                   {DiskSpaceUsed, Limit, QuotaVolume, Status...}
Win32_ComClassAutoEmulator          {}                   {NewVersion, OldVersion}
Win32_FolderRedirectionHealthCon... {}                   {LastSyncDurationCautionInHours, LastSyncDurationUnhealthyInHours}
Win32_ComClassEmulator              {}                   {NewVersion, OldVersion}
Win32_SoftwareFeatureAction         {}                   {Action, Element}
CIM_StatisticalInformation          {}                   {Caption, Description, Name}
Win32_NamedJobObjectActgInfo        {}                   {ActiveProcesses, Caption, Description, Name...}
CIM_DeviceErrorCounts               {ResetCounter}       {Caption, CriticalErrorCount, Description, DeviceCreationClassName...}
Win32_Perf                          {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData                   {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData             {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_SecuritySettingGroup          {}                   {Group, SecuritySetting}
Win32_LogicalFileGroup              {}                   {Group, SecuritySetting}
Win32_DCOMApplicationLaunchAllow... {}                   {Element, Setting}
Win32_SecuritySettingAuditing       {}                   {AuditedAccessMask, GuidInheritedObjectType, GuidObjectType, Inheritance...}
Win32_LogicalFileAuditing           {}                   {AuditedAccessMask, GuidInheritedObjectType, GuidObjectType, Inheritance...}
Win32_LogicalShareAuditing          {}                   {AuditedAccessMask, GuidInheritedObjectType, GuidObjectType, Inheritance...}
SoftwareLicensingProduct            {UninstallProduct... {ADActivationCsvlkPid, ADActivationCsvlkSkuId, ADActivationObjectDN, ADActivationObjectName...}
CIM_SoftwareElementActions          {}                   {Action, Element}
Win32_SoftwareElementAction         {}                   {Action, Element}
CIM_Dependency                      {}                   {Antecedent, Dependent}
CIM_ServiceAccessBySAP              {}                   {Antecedent, Dependent}
CIM_BootServiceAccessBySAP          {}                   {Antecedent, Dependent}
Win32_ApplicationCommandLine        {}                   {Antecedent, Dependent}
CIM_ClusterServiceAccessBySAP       {}                   {Antecedent, Dependent}
Win32_SubSession                    {}                   {Antecedent, Dependent}
Win32_ShadowVolumeSupport           {}                   {Antecedent, Dependent}
CIM_SAPSAPDependency                {}                   {Antecedent, Dependent}
CIM_PackageTempSensor               {}                   {Antecedent, Dependent}
CIM_JobDestinationJobs              {}                   {Antecedent, Dependent}
CIM_BIOSLoadedInNV                  {}                   {Antecedent, Dependent, EndingAddress, StartingAddress}
CIM_AssociatedCooling               {}                   {Antecedent, Dependent}
Win32_DeviceBus                     {}                   {Antecedent, Dependent}
Win32_SessionConnection             {}                   {Antecedent, Dependent}
Win32_ShadowFor                     {}                   {Antecedent, Dependent}
Win32_LogonSessionMappedDisk        {}                   {Antecedent, Dependent}
CIM_ConnectedTo                     {}                   {Antecedent, Dependent}
CIM_SlotInSlot                      {}                   {Antecedent, Dependent}
Win32_PrinterShare                  {}                   {Antecedent, Dependent}
CIM_BootOSFromFS                    {}                   {Antecedent, Dependent}
Win32_PnPSignedDriverCIMDataFile    {}                   {Antecedent, Dependent}
CIM_AssociatedAlarm                 {}                   {Antecedent, Dependent}
CIM_ElementsLinked                  {}                   {Antecedent, Dependent}
Win32_ConnectionShare               {}                   {Antecedent, Dependent}
Win32_LoadOrderGroupServiceDepen... {}                   {Antecedent, Dependent}
CIM_DeviceSAPImplementation         {}                   {Antecedent, Dependent}
CIM_AssociatedSensor                {}                   {Antecedent, Dependent}
CIM_AssociatedSupplyCurrentSensor   {}                   {Antecedent, Dependent, MonitoringRange}
CIM_AssociatedSupplyVoltageSensor   {}                   {Antecedent, Dependent, MonitoringRange}
CIM_Mount                           {}                   {Antecedent, Dependent}
CIM_ComputerSystemPackage           {}                   {Antecedent, Dependent}
CIM_PackageCooling                  {}                   {Antecedent, Dependent}
CIM_ProcessExecutable               {}                   {Antecedent, BaseAddress, Dependent, GlobalProcessCount...}
CIM_HostedService                   {}                   {Antecedent, Dependent}
CIM_HostedBootService               {}                   {Antecedent, Dependent}
CIM_DeviceAccessedByFile            {}                   {Antecedent, Dependent}
Win32_SessionResource               {}                   {Antecedent, Dependent}
Win32_SessionProcess                {}                   {Antecedent, Dependent}
CIM_AssociatedMemory                {}                   {Antecedent, Dependent}
CIM_AssociatedProcessorMemory       {}                   {Antecedent, BusSpeed, Dependent}
Win32_AssociatedProcessorMemory     {}                   {Antecedent, BusSpeed, Dependent}
Win32_SoftwareFeatureParent         {}                   {Antecedent, Dependent}
CIM_DeviceServiceImplementation     {}                   {Antecedent, Dependent}
CIM_AssociatedBattery               {}                   {Antecedent, Dependent}
Win32_ShadowOn                      {}                   {Antecedent, Dependent}
Win32_PrinterDriverDll              {}                   {Antecedent, Dependent}
CIM_PackageInSlot                   {}                   {Antecedent, Dependent}
CIM_CardInSlot                      {}                   {Antecedent, Dependent}
CIM_MemoryWithMedia                 {}                   {Antecedent, Dependent}
CIM_ServiceServiceDependency        {}                   {Antecedent, Dependent, TypeOfDependency}
Win32_DependentService              {}                   {Antecedent, Dependent, TypeOfDependency}
CIM_BasedOn                         {}                   {Antecedent, Dependent, EndingAddress, StartingAddress}
CIM_LogicalDiskBasedOnPartition     {}                   {Antecedent, Dependent, EndingAddress, StartingAddress}
Win32_LogicalDiskToPartition        {}                   {Antecedent, Dependent, EndingAddress, StartingAddress}
CIM_LogicalDiskBasedOnVolumeSet     {}                   {Antecedent, Dependent, EndingAddress, StartingAddress}
CIM_PSExtentBasedOnPExtent          {}                   {Antecedent, Dependent, EndingAddress, StartingAddress}
Win32_OperatingSystemQFE            {}                   {Antecedent, Dependent}
Win32_LoggedOnUser                  {}                   {Antecedent, Dependent}
CIM_RunningOS                       {}                   {Antecedent, Dependent}
Win32_SystemDriverPNPEntity         {}                   {Antecedent, Dependent}
CIM_SoftwareFeatureServiceImplem... {}                   {Antecedent, Dependent}
CIM_ServiceSAPDependency            {}                   {Antecedent, Dependent}
Win32_DfsNodeTarget                 {}                   {Antecedent, Dependent}
Win32_CIMLogicalDeviceCIMDataFile   {}                   {Antecedent, Dependent, Purpose, PurposeDescription}
CIM_DeviceConnection                {}                   {Antecedent, Dependent, NegotiatedDataWidth, NegotiatedSpeed}
CIM_ControlledBy                    {}                   {AccessState, Antecedent, Dependent, NegotiatedDataWidth...}
Win32_SCSIControllerDevice          {}                   {AccessState, Antecedent, Dependent, NegotiatedDataWidth...}
Win32_POTSModemToSerialPort         {}                   {AccessState, Antecedent, Dependent, NegotiatedDataWidth...}
Win32_USBControllerDevice           {}                   {AccessState, Antecedent, Dependent, NegotiatedDataWidth...}
CIM_SCSIInterface                   {}                   {AccessState, Antecedent, Dependent, NegotiatedDataWidth...}
Win32_PrinterController             {}                   {AccessState, Antecedent, Dependent, NegotiatedDataWidth...}
Win32_IDEControllerDevice           {}                   {AccessState, Antecedent, Dependent, NegotiatedDataWidth...}
CIM_SerialInterface                 {}                   {AccessState, Antecedent, Dependent, FlowControlInfo...}
CIM_USBControllerHasHub             {}                   {AccessState, Antecedent, Dependent, NegotiatedDataWidth...}
Win32_ControllerHasHub              {}                   {AccessState, Antecedent, Dependent, NegotiatedDataWidth...}
Win32_1394ControllerDevice          {}                   {AccessState, Antecedent, Dependent, NegotiatedDataWidth...}
Win32_DriverForDevice               {}                   {Antecedent, Dependent}
Win32_LogicalProgramGroupItemDat... {}                   {Antecedent, Dependent}
CIM_AllocatedResource               {}                   {Antecedent, Dependent}
Win32_PNPAllocatedResource          {}                   {Antecedent, Dependent}
CIM_SoftwareFeatureSAPImplementa... {}                   {Antecedent, Dependent}
CIM_DeviceSoftware                  {}                   {Antecedent, Dependent, Purpose, PurposeDescription}
CIM_Realizes                        {}                   {Antecedent, Dependent}
CIM_RealizesPExtent                 {}                   {Antecedent, Dependent, StartingAddress}
Win32_DiskDrivePhysicalMedia        {}                   {Antecedent, Dependent}
CIM_RealizesDiskPartition           {}                   {Antecedent, Dependent, StartingAddress}
Win32_MemoryDeviceLocation          {}                   {Antecedent, Dependent}
Win32_MemoryArrayLocation           {}                   {Antecedent, Dependent}
CIM_RealizesAggregatePExtent        {}                   {Antecedent, Dependent}
Win32_ShadowBy                      {}                   {Antecedent, Dependent}
Win32_AllocatedResource             {}                   {Antecedent, Dependent}
CIM_HostedAccessPoint               {}                   {Antecedent, Dependent}
CIM_HostedBootSAP                   {}                   {Antecedent, Dependent}
CIM_ResidesOnExtent                 {}                   {Antecedent, Dependent}
CIM_MediaPresent                    {}                   {Antecedent, Dependent}
Win32_DiskDriveToDiskPartition      {}                   {Antecedent, Dependent}
CIM_HostedJobDestination            {}                   {Antecedent, Dependent}
Win32_LogicalProgramGroupDirectory  {}                   {Antecedent, Dependent}
Win32_ShadowDiffVolumeSupport       {}                   {Antecedent, Dependent}
CIM_PackageAlarm                    {}                   {Antecedent, Dependent}
CIM_Docked                          {}                   {Antecedent, Dependent}
CIM_Product                         {}                   {Caption, Description, IdentifyingNumber, Name...}
Win32_Product                       {Install, Admin, ... {AssignmentType, Caption, Description, HelpLink...}
Win32_ComputerSystemProduct         {}                   {Caption, Description, IdentifyingNumber, Name...}
CIM_ActionSequence                  {}                   {Next, Prior}
CIM_CollectedCollections            {}                   {Collection, CollectionInCollection}
Win32_ProductCheck                  {}                   {Check, Product}
SoftwareLicensingService            {InstallProductKe... {ClientMachineID, DiscoveredKeyManagementServiceMachineIpAddress, DiscoveredKeyManagementServiceMachineName, DiscoveredKeyManagementServiceMac...
Win32_NTLogEventUser                {}                   {Record, User}
CIM_ProductParentChild              {}                   {Child, Parent}
Win32_ProtocolBinding               {}                   {Antecedent, Dependent, Device}
CIM_SupportAccess                   {}                   {CommunicationInfo, CommunicationMode, Description, Locale...}
CIM_CollectionSetting               {}                   {Collection, Setting}
Win32_NamedJobObjectLimit           {}                   {Collection, Setting}
Win32_NamedJobObjectSecLimit        {}                   {Collection, Setting}
Win32_NTLogEventComputer            {}                   {Computer, Record}
Win32_TokenGroups                   {}                   {GroupCount, Groups}
SoftwareLicensingTokenActivation... {Uninstall}          {AdditionalInfo, AuthorizationStatus, Description, ExpirationDate...}
CIM_PhysicalCapacity                {}                   {Caption, Description, Name}
CIM_MemoryCapacity                  {}                   {Caption, Description, MaximumMemoryCapacity, MemoryType...}
Win32_DefragAnalysis                {}                   {AverageFileSize, AverageFragmentsPerFile, AverageFreeSpacePerExtent, ClusterSize...}
CIM_ProductProductDependency        {}                   {DependentProduct, RequiredProduct, TypeOfDependency}
Win32_SIDandAttributes              {}                   {Attributes, SID}
Win32_CheckCheck                    {}                   {Check, Location}
CIM_CompatibleProduct               {}                   {CompatibilityDescription, CompatibleProduct, Product}
Win32_RoamingProfileBackgroundUp... {}                   {Interval, SchedulingMethod, Time}
CIM_ToDirectoryAction               {}                   {DestinationDirectory, FileName}
CIM_ActsAsSpare                     {}                   {Group, HotStandby, Spare}
Win32_RoamingProfileSlowLinkParams  {}                   {ConnectionTransferRate, TimeOut}
Win32_SecuritySettingAccess         {}                   {AccessMask, GuidInheritedObjectType, GuidObjectType, Inheritance...}
Win32_LogicalFileAccess             {}                   {AccessMask, GuidInheritedObjectType, GuidObjectType, Inheritance...}
Win32_LogicalShareAccess            {}                   {AccessMask, GuidInheritedObjectType, GuidObjectType, Inheritance...}
Win32_OfflineFilesHealth            {}                   {LastSuccessfulSyncTime, LastSyncStatus, LastSyncTime, OfflineAccessEnabled...}
CIM_StorageDefect                   {}                   {Error, Extent}
Win32_PerfFormattedData_ADWS_ADWS   {}                   {ActiveWebServiceSessions, AllocatedConnections, Caption, ChangeOptionalFeatureOperationsPerSecond...}
Win32_PerfRawData_ADWS_ADWS         {}                   {ActiveWebServiceSessions, AllocatedConnections, Caption, ChangeOptionalFeatureOperationsPerSecond...}
Win32_PerfFormattedData_AFDCount... {}                   {Caption, Description, DroppedDatagrams, DroppedDatagramsPersec...}
Win32_PerfRawData_AFDCounters_Mi... {}                   {Caption, Description, DroppedDatagrams, DroppedDatagramsPersec...}
Win32_PerfFormattedData_Authoriz... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_AuthorizationM... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_BITS_BIT... {}                   {BITSDownloadBlockSizeBytes, BITSDownloadResponseIntervalmsec, Caption, Description...}
Win32_PerfRawData_BITS_BITSNetUt... {}                   {BITSDownloadBlockSizeBytes, BITSDownloadResponseIntervalmsec, Caption, Description...}
Win32_PerfFormattedData_Counters... {}                   {AAAAqueriesFailed, AAAAqueriesSuccessful, AAAASynthesizedrecords, Caption...}
Win32_PerfRawData_Counters_DNS64... {}                   {AAAAqueriesFailed, AAAAqueriesSuccessful, AAAASynthesizedrecords, Caption...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_Counters_Event... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Counters... {}                   {BufferMemoryUsageNonPagedPool, BufferMemoryUsagePagedPool, Caption, Description...}
Win32_PerfRawData_Counters_Event... {}                   {BufferMemoryUsageNonPagedPool, BufferMemoryUsagePagedPool, Caption, Description...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, FileSystemBytesRead, FileSystemBytesWritten...}
Win32_PerfRawData_Counters_FileS... {}                   {Caption, Description, FileSystemBytesRead, FileSystemBytesWritten...}
Win32_PerfFormattedData_Counters... {}                   {AuthIPMainModeNegotiationTime, AuthIPQuickModeNegotiationTime, Caption, Description...}
Win32_PerfRawData_Counters_Gener... {}                   {AuthIPMainModeNegotiationTime, AuthIPQuickModeNegotiationTime, Caption, Description...}
Win32_PerfFormattedData_Counters... {}                   {Caption, CurrentUrisCached, Description, Frequency_Object...}
Win32_PerfRawData_Counters_HTTPS... {}                   {Caption, CurrentUrisCached, Description, Frequency_Object...}
Win32_PerfFormattedData_Counters... {}                   {ArrivalRate, CacheHitRate, Caption, CurrentQueueSize...}
Win32_PerfRawData_Counters_HTTPS... {}                   {ArrivalRate, CacheHitRate, Caption, CurrentQueueSize...}
Win32_PerfFormattedData_Counters... {}                   {AllRequests, BytesReceivedRate, BytesSentRate, BytesTransferredRate...}
Win32_PerfRawData_Counters_HTTPS... {}                   {AllRequests, BytesReceivedRate, BytesSentRate, BytesTransferredRate...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_Counters_Hyper... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, DropsNeighborresolutiontimeouts, ErrorsAuthenticationErrors...}
Win32_PerfRawData_Counters_IPHTT... {}                   {Caption, Description, DropsNeighborresolutiontimeouts, ErrorsAuthenticationErrors...}
Win32_PerfFormattedData_Counters... {}                   {Bytesreceivedonthissession, Bytessentonthissession, Caption, Description...}
Win32_PerfRawData_Counters_IPHTT... {}                   {Bytesreceivedonthissession, Bytessentonthissession, Caption, Description...}
Win32_PerfFormattedData_Counters... {}                   {ActiveExtendedModeSAs, ActiveMainModeSAs, ActiveQuickModeSAs, Caption...}
Win32_PerfRawData_Counters_IPsec... {}                   {ActiveExtendedModeSAs, ActiveMainModeSAs, ActiveQuickModeSAs, Caption...}
Win32_PerfFormattedData_Counters... {}                   {ActiveExtendedModeSAs, ActiveMainModeSAs, ActiveQuickModeSAs, Caption...}
Win32_PerfRawData_Counters_IPsec... {}                   {ActiveExtendedModeSAs, ActiveMainModeSAs, ActiveQuickModeSAs, Caption...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_Counters_IPsec... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Counters... {}                   {Caption, CurrentStateEntries, Description, Frequency_Object...}
Win32_PerfRawData_Counters_IPsec... {}                   {Caption, CurrentStateEntries, Description, Frequency_Object...}
Win32_PerfFormattedData_Counters... {}                   {ActiveSecurityAssociations, BytesReceivedinTransportModePersec, BytesReceivedinTunnelModePersec, BytesSentinTransportModePersec...}
Win32_PerfRawData_Counters_IPsec... {}                   {ActiveSecurityAssociations, BytesReceivedinTransportModePersec, BytesReceivedinTunnelModePersec, BytesSentinTransportModePersec...}
Win32_PerfFormattedData_Counters... {}                   {ActiveMainModeSAs, ActiveQuickModeSAs, Caption, Description...}
Win32_PerfRawData_Counters_IPsec... {}                   {ActiveMainModeSAs, ActiveQuickModeSAs, Caption, Description...}
Win32_PerfFormattedData_Counters... {}                   {ActiveMainModeSAs, ActiveQuickModeSAs, Caption, Description...}
Win32_PerfRawData_Counters_IPsec... {}                   {ActiveMainModeSAs, ActiveQuickModeSAs, Caption, Description...}
Win32_PerfFormattedData_Counters... {}                   {ActiveMainModeSAs, ActiveQuickModeSAs, Caption, Description...}
Win32_PerfRawData_Counters_IPsec... {}                   {ActiveMainModeSAs, ActiveQuickModeSAs, Caption, Description...}
Win32_PerfFormattedData_Counters... {}                   {ActiveMainModeSAs, ActiveQuickModeSAs, Caption, Description...}
Win32_PerfRawData_Counters_IPsec... {}                   {ActiveMainModeSAs, ActiveQuickModeSAs, Caption, Description...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, FailedRequests, Frequency_Object...}
Win32_PerfRawData_Counters_KPSSVC   {}                   {Caption, Description, FailedRequests, Frequency_Object...}
Win32_PerfFormattedData_Counters... {}                   {AverageSemaphoreHoldTime, Caption, Description, Frequency_Object...}
Win32_PerfRawData_Counters_Netlogon {}                   {AverageSemaphoreHoldTime, AverageSemaphoreHoldTime_Base, Caption, Description...}
Win32_PerfFormattedData_Counters... {}                   {Bytestransmitted, BytestransmittedPersec, Caption, Description...}
Win32_PerfRawData_Counters_Netwo... {}                   {Bytestransmitted, BytestransmittedPersec, Caption, Description...}
Win32_PerfFormattedData_Counters... {}                   {Averagepacketsinnetcard, Averagepacketsinsequencer, Averagepacketsinshaper, Bytesscheduled...}
Win32_PerfRawData_Counters_Pacer... {}                   {Averagepacketsinnetcard, Averagepacketsinsequencer, Averagepacketsinshaper, Bytesscheduled...}
Win32_PerfFormattedData_Counters... {}                   {Averagepacketsinnetcard, Averagepacketsinsequencer, Averagepacketsinshaper, Caption...}
Win32_PerfRawData_Counters_Pacer... {}                   {Averagepacketsinnetcard, Averagepacketsinsequencer, Averagepacketsinshaper, Caption...}
Win32_PerfFormattedData_Counters... {}                   {BuildScatterGatherCyclesPersec, Caption, Description, Frequency_Object...}
Win32_PerfRawData_Counters_PerPr... {}                   {BuildScatterGatherCyclesPersec, Caption, Description, Frequency_Object...}
Win32_PerfFormattedData_Counters... {}                   {BuildScatterGatherListCallsPersec, Caption, Description, DPCsDeferredPersec...}
Win32_PerfRawData_Counters_PerPr... {}                   {BuildScatterGatherListCallsPersec, Caption, Description, DPCsDeferredPersec...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, DevicePowerState, Frequency_Object...}
Win32_PerfRawData_Counters_Physi... {}                   {Caption, Description, DevicePowerState, Frequency_Object...}
Win32_PerfFormattedData_Counters... {}                   {ActivityHostManagerhostprocessespoolsize, ActivityHostManagerNumberofbusyhostprocesses, ActivityHostManagerNumberofcreatedhostprocesses, Acti...
Win32_PerfRawData_Counters_Power... {}                   {ActivityHostManagerhostprocessespoolsize, ActivityHostManagerNumberofbusyhostprocesses, ActivityHostManagerNumberofcreatedhostprocesses, Acti...
Win32_PerfFormattedData_Counters... {}                   {AverageIdleTime, C1TransitionsPersec, C2TransitionsPersec, C3TransitionsPersec...}
Win32_PerfRawData_Counters_Proce... {}                   {AverageIdleTime, AverageIdleTime_Base, C1TransitionsPersec, C2TransitionsPersec...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_Counters_RDMAA... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Counters... {}                   {AverageEncodingTime, Caption, Description, FrameQuality...}
Win32_PerfRawData_Counters_Remot... {}                   {AverageEncodingTime, Caption, Description, FrameQuality...}
Win32_PerfFormattedData_Counters... {}                   {BaseTCPRTT, BaseUDPRTT, Caption, CurrentTCPBandwidth...}
Win32_PerfRawData_Counters_Remot... {}                   {BaseTCPRTT, BaseUDPRTT, Caption, CurrentTCPBandwidth...}
Win32_PerfFormattedData_Counters... {}                   {AvgBytesPerRead, AvgBytesPerWrite, AvgDataBytesPerRequest, AvgDataQueueLength...}
Win32_PerfRawData_Counters_SMBCl... {}                   {AvgBytesPerRead, AvgBytesPerRead_Base, AvgBytesPerWrite, AvgBytesPerWrite_Base...}
Win32_PerfFormattedData_Counters... {}                   {BytesRDMAReadPersec, BytesRDMAWrittenPersec, BytesReceivedPersec, BytesSentPersec...}
Win32_PerfRawData_Counters_SMBDi... {}                   {BytesRDMAReadPersec, BytesRDMAWrittenPersec, BytesReceivedPersec, BytesSentPersec...}
Win32_PerfFormattedData_Counters... {}                   {AvgBytesPerRead, AvgBytesPerWrite, AvgDataBytesPerRequest, AvgDataQueueLength...}
Win32_PerfRawData_Counters_SMBSe... {}                   {AvgBytesPerRead, AvgBytesPerRead_Base, AvgBytesPerWrite, AvgBytesPerWrite_Base...}
Win32_PerfFormattedData_Counters... {}                   {AvgBytesPerRead, AvgBytesPerWrite, AvgDataBytesPerRequest, AvgDataQueueLength...}
Win32_PerfRawData_Counters_SMBSe... {}                   {AvgBytesPerRead, AvgBytesPerRead_Base, AvgBytesPerWrite, AvgBytesPerWrite_Base...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, ExecResourceAcquiresAcqExclLitePersec, ExecResourceAcquiresAcqShrdLitePersec...}
Win32_PerfRawData_Counters_Synch... {}                   {Caption, Description, ExecResourceAcquiresAcqExclLitePersec, ExecResourceAcquiresAcqShrdLitePersec...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, ExecResourceAcquiresAcqExclLitePersec, ExecResourceAcquiresAcqShrdLitePersec...}
Win32_PerfRawData_Counters_Synch... {}                   {Caption, Description, ExecResourceAcquiresAcqExclLitePersec, ExecResourceAcquiresAcqShrdLitePersec...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_Counters_Tered... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_Counters_Tered... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_Counters_Tered... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_Counters_Therm... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_Counters_WFP      {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Counters... {}                   {ActiveInboundConnections, ActiveOutboundConnections, AllowedClassifiesPersec, BlockedBinds...}
Win32_PerfRawData_Counters_WFPv4    {}                   {ActiveInboundConnections, ActiveOutboundConnections, AllowedClassifiesPersec, BlockedBinds...}
Win32_PerfFormattedData_Counters... {}                   {ActiveInboundConnections, ActiveOutboundConnections, AllowedClassifiesPersec, BlockedBinds...}
Win32_PerfRawData_Counters_WFPv6    {}                   {ActiveInboundConnections, ActiveOutboundConnections, AllowedClassifiesPersec, BlockedBinds...}
Win32_PerfFormattedData_Counters... {}                   {ActiveOperations, ActiveShells, ActiveUsers, Caption...}
Win32_PerfRawData_Counters_WSMan... {}                   {ActiveOperations, ActiveShells, ActiveUsers, Caption...}
Win32_PerfFormattedData_Counters... {}                   {AllocationCount, Caption, Description, FreeCount...}
Win32_PerfRawData_Counters_XHCIC... {}                   {AllocationCount, Caption, Description, FreeCount...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, DpcRequeueCount, DPCsPersec...}
Win32_PerfRawData_Counters_XHCII... {}                   {Caption, Description, DpcRequeueCount, DPCsPersec...}
Win32_PerfFormattedData_Counters... {}                   {BytesPerSec, Caption, Description, FailedTransferCount...}
Win32_PerfRawData_Counters_XHCIT... {}                   {BytesPerSec, Caption, Description, FailedTransferCount...}
Win32_PerfFormattedData_DdmCount... {}                   {BytesReceivedByDisconnectedClients, BytesTransmittedByDisconnectedClients, Caption, Description...}
Win32_PerfRawData_DdmCounterProv... {}                   {BytesReceivedByDisconnectedClients, BytesTransmittedByDisconnectedClients, Caption, Description...}
Win32_PerfFormattedData_DFSNServ... {}                   {Caption, Description, FolderCount, Frequency_Object...}
Win32_PerfRawData_DFSNServerServ... {}                   {Caption, Description, FolderCount, Frequency_Object...}
Win32_PerfFormattedData_DFSNServ... {}                   {AvgResponseTime, Caption, Description, Frequency_Object...}
Win32_PerfRawData_DFSNServerServ... {}                   {AvgResponseTime, AvgResponseTime_Base, Caption, Description...}
Win32_PerfFormattedData_DFSNServ... {}                   {AvgResponseTime, Caption, Description, Frequency_Object...}
Win32_PerfRawData_DFSNServerServ... {}                   {AvgResponseTime, AvgResponseTime_Base, Caption, Description...}
Win32_PerfFormattedData_dfsr_DFS... {}                   {BandwidthSavingsUsingDFSReplication, Caption, CompressedSizeofFilesReceived, ConflictBytesCleanedup...}
Win32_PerfRawData_dfsr_DFSReplic... {}                   {BandwidthSavingsUsingDFSReplication, Caption, CompressedSizeofFilesReceived, ConflictBytesCleanedup...}
Win32_PerfFormattedData_dfsr_DFS... {}                   {BandwidthSavingsUsingDFSReplication, BytesReceivedPerSecond, Caption, CompressedSizeofFilesReceived...}
Win32_PerfRawData_dfsr_DFSReplic... {}                   {BandwidthSavingsUsingDFSReplication, BytesReceivedPerSecond, Caption, CompressedSizeofFilesReceived...}
Win32_PerfFormattedData_dfsr_DFS... {}                   {Caption, DatabaseCommits, DatabaseLookups, Description...}
Win32_PerfRawData_dfsr_DFSReplic... {}                   {Caption, DatabaseCommits, DatabaseLookups, Description...}
Win32_PerfFormattedData_Director... {}                   {ABANRPersec, ABBrowsesPersec, ABClientSessions, ABMatchesPersec...}
Win32_PerfRawData_DirectoryServi... {}                   {ABANRPersec, ABBrowsesPersec, ABClientSessions, ABMatchesPersec...}
Win32_PerfFormattedData_DNS_DNS     {}                   {AXFRRequestReceived, AXFRRequestSent, AXFRResponseReceived, AXFRSuccessReceived...}
Win32_PerfRawData_DNS_DNS           {}                   {AXFRRequestReceived, AXFRRequestSent, AXFRResponseReceived, AXFRSuccessReceived...}
Win32_PerfFormattedData_ESENT_Da... {}                   {Caption, DatabaseCacheMemoryCommitted, DatabaseCacheMemoryCommittedMB, DatabaseCacheMemoryReserved...}
Win32_PerfRawData_ESENT_Database    {}                   {Caption, DatabaseCacheMemoryCommitted, DatabaseCacheMemoryCommittedMB, DatabaseCacheMemoryReserved...}
Win32_PerfFormattedData_ESENT_Da... {}                   {Caption, DatabaseCacheMissesPersec, DatabaseCachePercentHit, DatabaseCachePercentHitUncorrelated...}
Win32_PerfRawData_ESENT_Database... {}                   {Caption, DatabaseCacheMissesPersec, DatabaseCachePercentHit, DatabaseCachePercentHit_Base...}
Win32_PerfFormattedData_ESENT_Da... {}                   {Caption, DatabaseCacheMissesPersec, DatabaseCachePercentHit, DatabaseCachePercentHitUncorrelated...}
Win32_PerfRawData_ESENT_Database... {}                   {Caption, DatabaseCacheMissesPersec, DatabaseCachePercentHit, DatabaseCachePercentHit_Base...}
Win32_PerfFormattedData_LocalSes... {}                   {ActiveSessions, Caption, Description, Frequency_Object...}
Win32_PerfRawData_LocalSessionMa... {}                   {ActiveSessions, Caption, Description, Frequency_Object...}
Win32_PerfFormattedData_Lsa_Secu... {}                   {Caption, ContextHandles, CredentialHandles, Description...}
Win32_PerfRawData_Lsa_SecurityPe... {}                   {Caption, ContextHandles, CredentialHandles, Description...}
Win32_PerfFormattedData_Lsa_Secu... {}                   {ActiveSchannelSessionCacheEntries, Caption, Description, DigestAuthentications...}
Win32_PerfRawData_Lsa_SecuritySy... {}                   {ActiveSchannelSessionCacheEntries, Caption, Description, DigestAuthentications...}
Win32_PerfFormattedData_MSDTC_Di... {}                   {AbortedTransactions, AbortedTransactionsPersec, ActiveTransactions, ActiveTransactionsMaximum...}
Win32_PerfRawData_MSDTC_Distribu... {}                   {AbortedTransactions, AbortedTransactionsPersec, ActiveTransactions, ActiveTransactionsMaximum...}
Win32_PerfFormattedData_MSDTCBri... {}                   {Averageparticipantcommitresponsetime, Averageparticipantprepareresponsetime, Caption, CommitretrycountPersec...}
Win32_PerfRawData_MSDTCBridge400... {}                   {Averageparticipantcommitresponsetime, Averageparticipantcommitresponsetime_Base, Averageparticipantprepareresponsetime, Averageparticipantpre...
Win32_PerfFormattedData_NETCLRDa... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_NETCLRData_NET... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_NETCLRNe... {}                   {BytesReceived, BytesSent, Caption, ConnectionsEstablished...}
Win32_PerfRawData_NETCLRNetworki... {}                   {BytesReceived, BytesSent, Caption, ConnectionsEstablished...}
Win32_PerfFormattedData_NETCLRNe... {}                   {BytesReceived, BytesSent, Caption, ConnectionsEstablished...}
Win32_PerfRawData_NETCLRNetworki... {}                   {BytesReceived, BytesSent, Caption, ConnectionsEstablished...}
Win32_PerfFormattedData_NETDataP... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_NETDataProvide... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_NETDataP... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_NETDataProvide... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_NETFrame... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_NETFramework_N... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_NETFrame... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_NETFramework_N... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_NETFrame... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_NETFramework_N... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_NETFrame... {}                   {AssemblySearchLength, BytesinLoaderHeap, Caption, Currentappdomains...}
Win32_PerfRawData_NETFramework_N... {}                   {AssemblySearchLength, BytesinLoaderHeap, Caption, Currentappdomains...}
Win32_PerfFormattedData_NETFrame... {}                   {Caption, ContentionRatePersec, CurrentQueueLength, Description...}
Win32_PerfRawData_NETFramework_N... {}                   {Caption, ContentionRatePersec, CurrentQueueLength, Description...}
Win32_PerfFormattedData_NETFrame... {}                   {AllocatedBytesPersec, Caption, Description, FinalizationSurvivors...}
Win32_PerfRawData_NETFramework_N... {}                   {AllocatedBytesPersec, Caption, Description, FinalizationSurvivors...}
Win32_PerfFormattedData_NETFrame... {}                   {Caption, Channels, ContextBoundClassesLoaded, ContextBoundObjectsAllocPersec...}
Win32_PerfRawData_NETFramework_N... {}                   {Caption, Channels, ContextBoundClassesLoaded, ContextBoundObjectsAllocPersec...}
Win32_PerfFormattedData_NETFrame... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_NETFramework_N... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_NETMemor... {}                   {CacheEntries, CacheHitRatio, CacheHits, CacheMisses...}
Win32_PerfRawData_NETMemoryCache... {}                   {CacheEntries, CacheHitRatio, CacheHitRatio_Base, CacheHits...}
Win32_PerfFormattedData_NTDS_NTDS   {}                   {ABANRPersec, ABBrowsesPersec, ABClientSessions, ABMatchesPersec...}
Win32_PerfRawData_NTDS_NTDS         {}                   {ABANRPersec, ABBrowsesPersec, ABClientSessions, ABMatchesPersec...}
Win32_PerfFormattedData_PerfDisk... {}                   {AvgDiskBytesPerRead, AvgDiskBytesPerTransfer, AvgDiskBytesPerWrite, AvgDiskQueueLength...}
Win32_PerfRawData_PerfDisk_Logic... {}                   {AvgDiskBytesPerRead, AvgDiskBytesPerRead_Base, AvgDiskBytesPerTransfer, AvgDiskBytesPerTransfer_Base...}
Win32_PerfFormattedData_PerfDisk... {}                   {AvgDiskBytesPerRead, AvgDiskBytesPerTransfer, AvgDiskBytesPerWrite, AvgDiskQueueLength...}
Win32_PerfRawData_PerfDisk_Physi... {}                   {AvgDiskBytesPerRead, AvgDiskBytesPerRead_Base, AvgDiskBytesPerTransfer, AvgDiskBytesPerTransfer_Base...}
Win32_PerfFormattedData_PerfNet_... {}                   {AnnouncementsDomainPersec, AnnouncementsServerPersec, AnnouncementsTotalPersec, Caption...}
Win32_PerfRawData_PerfNet_Browser   {}                   {AnnouncementsDomainPersec, AnnouncementsServerPersec, AnnouncementsTotalPersec, Caption...}
Win32_PerfFormattedData_PerfNet_... {}                   {BytesReceivedPersec, BytesTotalPersec, BytesTransmittedPersec, Caption...}
Win32_PerfRawData_PerfNet_Redire... {}                   {BytesReceivedPersec, BytesTotalPersec, BytesTransmittedPersec, Caption...}
Win32_PerfFormattedData_PerfNet_... {}                   {BlockingRequestsRejected, BytesReceivedPersec, BytesTotalPersec, BytesTransmittedPersec...}
Win32_PerfRawData_PerfNet_Server    {}                   {BlockingRequestsRejected, BytesReceivedPersec, BytesTotalPersec, BytesTransmittedPersec...}
Win32_PerfFormattedData_PerfNet_... {}                   {ActiveThreads, AvailableThreads, AvailableWorkItems, BorrowedWorkItems...}
Win32_PerfRawData_PerfNet_Server... {}                   {ActiveThreads, AvailableThreads, AvailableWorkItems, BorrowedWorkItems...}
Win32_PerfFormattedData_PerfOS_C... {}                   {AsyncCopyReadsPersec, AsyncDataMapsPersec, AsyncFastReadsPersec, AsyncMDLReadsPersec...}
Win32_PerfRawData_PerfOS_Cache      {}                   {AsyncCopyReadsPersec, AsyncDataMapsPersec, AsyncFastReadsPersec, AsyncMDLReadsPersec...}
Win32_PerfFormattedData_PerfOS_M... {}                   {AvailableBytes, AvailableKBytes, AvailableMBytes, CacheBytes...}
Win32_PerfRawData_PerfOS_Memory     {}                   {AvailableBytes, AvailableKBytes, AvailableMBytes, CacheBytes...}
Win32_PerfFormattedData_PerfOS_N... {}                   {AvailableMBytes, Caption, Description, FreeAndZeroPageListMBytes...}
Win32_PerfRawData_PerfOS_NUMANod... {}                   {AvailableMBytes, Caption, Description, FreeAndZeroPageListMBytes...}
Win32_PerfFormattedData_PerfOS_O... {}                   {Caption, Description, Events, Frequency_Object...}
Win32_PerfRawData_PerfOS_Objects    {}                   {Caption, Description, Events, Frequency_Object...}
Win32_PerfFormattedData_PerfOS_P... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_PerfOS_PagingFile {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_PerfOS_P... {}                   {C1TransitionsPersec, C2TransitionsPersec, C3TransitionsPersec, Caption...}
Win32_PerfRawData_PerfOS_Processor  {}                   {C1TransitionsPersec, C2TransitionsPersec, C3TransitionsPersec, Caption...}
Win32_PerfFormattedData_PerfOS_S... {}                   {AlignmentFixupsPersec, Caption, ContextSwitchesPersec, Description...}
Win32_PerfRawData_PerfOS_System     {}                   {AlignmentFixupsPersec, Caption, ContextSwitchesPersec, Description...}
Win32_PerfFormattedData_PerfProc... {}                   {Caption, Description, ExecReadOnly, ExecReadPerWrite...}
Win32_PerfRawData_PerfProc_FullI... {}                   {Caption, Description, ExecReadOnly, ExecReadPerWrite...}
Win32_PerfFormattedData_PerfProc... {}                   {Caption, Description, ExecReadOnly, ExecReadPerWrite...}
Win32_PerfRawData_PerfProc_Image... {}                   {Caption, Description, ExecReadOnly, ExecReadPerWrite...}
Win32_PerfFormattedData_PerfProc... {}                   {Caption, CurrentPercentKernelModeTime, CurrentPercentProcessorTime, CurrentPercentUserModeTime...}
Win32_PerfRawData_PerfProc_JobOb... {}                   {Caption, CurrentPercentKernelModeTime, CurrentPercentProcessorTime, CurrentPercentUserModeTime...}
Win32_PerfFormattedData_PerfProc... {}                   {Caption, CreatingProcessID, Description, ElapsedTime...}
Win32_PerfRawData_PerfProc_JobOb... {}                   {Caption, CreatingProcessID, Description, ElapsedTime...}
Win32_PerfFormattedData_PerfProc... {}                   {Caption, CreatingProcessID, Description, ElapsedTime...}
Win32_PerfRawData_PerfProc_Process  {}                   {Caption, CreatingProcessID, Description, ElapsedTime...}
Win32_PerfFormattedData_PerfProc... {}                   {BytesFree, BytesImageFree, BytesImageReserved, BytesReserved...}
Win32_PerfRawData_PerfProc_Proce... {}                   {BytesFree, BytesImageFree, BytesImageReserved, BytesReserved...}
Win32_PerfFormattedData_PerfProc... {}                   {Caption, ContextSwitchesPersec, Description, ElapsedTime...}
Win32_PerfRawData_PerfProc_Thread   {}                   {Caption, ContextSwitchesPersec, Description, ElapsedTime...}
Win32_PerfFormattedData_PerfProc... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_PerfProc_Threa... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_PowerMet... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_PowerMeterCoun... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_RemoteAc... {}                   {AlignmentErrors, BufferOverrunErrors, BytesReceived, BytesReceivedPerSec...}
Win32_PerfRawData_RemoteAccess_R... {}                   {AlignmentErrors, BufferOverrunErrors, BytesReceived, BytesReceivedPerSec...}
Win32_PerfFormattedData_RemoteAc... {}                   {AlignmentErrors, BufferOverrunErrors, BytesReceived, BytesReceivedPerSec...}
Win32_PerfRawData_RemoteAccess_R... {}                   {AlignmentErrors, BufferOverrunErrors, BytesReceived, BytesReceivedPerSec...}
Win32_PerfFormattedData_ServiceM... {}                   {Calls, CallsDuration, CallsFailed, CallsFailedPerSecond...}
Win32_PerfRawData_ServiceModel40... {}                   {Calls, CallsDuration, CallsDuration_Base, CallsFailed...}
Win32_PerfFormattedData_ServiceM... {}                   {CallFailedPerSecond, Calls, CallsDuration, CallsFailed...}
Win32_PerfRawData_ServiceModel40... {}                   {CallFailedPerSecond, Calls, CallsDuration, CallsDuration_Base...}
Win32_PerfFormattedData_ServiceM... {}                   {Calls, CallsDuration, CallsFailed, CallsFailedPerSecond...}
Win32_PerfRawData_ServiceModel40... {}                   {Calls, CallsDuration, CallsDuration_Base, CallsFailed...}
Win32_PerfFormattedData_SMSvcHos... {}                   {Caption, ConnectionsAcceptedovernetpipe, ConnectionsAcceptedovernettcp, ConnectionsDispatchedovernetpipe...}
Win32_PerfRawData_SMSvcHost4000_... {}                   {Caption, ConnectionsAcceptedovernetpipe, ConnectionsAcceptedovernettcp, ConnectionsDispatchedovernetpipe...}
Win32_PerfFormattedData_Spooler_... {}                   {AddNetworkPrinterCalls, BytesPrintedPersec, Caption, Description...}
Win32_PerfRawData_Spooler_PrintQ... {}                   {AddNetworkPrinterCalls, BytesPrintedPersec, Caption, Description...}
Win32_PerfFormattedData_TapiSrv_... {}                   {ActiveLines, ActiveTelephones, Caption, ClientApps...}
Win32_PerfRawData_TapiSrv_Telephony {}                   {ActiveLines, ActiveTelephones, Caption, ClientApps...}
Win32_PerfFormattedData_Tcpip_ICMP  {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_Tcpip_ICMP        {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Tcpip_IC... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_Tcpip_ICMPv6      {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Tcpip_IPv4  {}                   {Caption, DatagramsForwardedPersec, DatagramsOutboundDiscarded, DatagramsOutboundNoRoute...}
Win32_PerfRawData_Tcpip_IPv4        {}                   {Caption, DatagramsForwardedPersec, DatagramsOutboundDiscarded, DatagramsOutboundNoRoute...}
Win32_PerfFormattedData_Tcpip_IPv6  {}                   {Caption, DatagramsForwardedPersec, DatagramsOutboundDiscarded, DatagramsOutboundNoRoute...}
Win32_PerfRawData_Tcpip_IPv6        {}                   {Caption, DatagramsForwardedPersec, DatagramsOutboundDiscarded, DatagramsOutboundNoRoute...}
Win32_PerfFormattedData_Tcpip_NB... {}                   {BytesReceivedPersec, BytesSentPersec, BytesTotalPersec, Caption...}
Win32_PerfRawData_Tcpip_NBTConne... {}                   {BytesReceivedPersec, BytesSentPersec, BytesTotalPersec, Caption...}
Win32_PerfFormattedData_Tcpip_Ne... {}                   {BytesReceivedPersec, BytesSentPersec, BytesTotalPersec, Caption...}
Win32_PerfRawData_Tcpip_NetworkA... {}                   {BytesReceivedPersec, BytesSentPersec, BytesTotalPersec, Caption...}
Win32_PerfFormattedData_Tcpip_Ne... {}                   {BytesReceivedPersec, BytesSentPersec, BytesTotalPersec, Caption...}
Win32_PerfRawData_Tcpip_NetworkI... {}                   {BytesReceivedPersec, BytesSentPersec, BytesTotalPersec, Caption...}
Win32_PerfFormattedData_Tcpip_TCPv4 {}                   {Caption, ConnectionFailures, ConnectionsActive, ConnectionsEstablished...}
Win32_PerfRawData_Tcpip_TCPv4       {}                   {Caption, ConnectionFailures, ConnectionsActive, ConnectionsEstablished...}
Win32_PerfFormattedData_Tcpip_TCPv6 {}                   {Caption, ConnectionFailures, ConnectionsActive, ConnectionsEstablished...}
Win32_PerfRawData_Tcpip_TCPv6       {}                   {Caption, ConnectionFailures, ConnectionsActive, ConnectionsEstablished...}
Win32_PerfFormattedData_Tcpip_UDPv4 {}                   {Caption, DatagramsNoPortPersec, DatagramsPersec, DatagramsReceivedErrors...}
Win32_PerfRawData_Tcpip_UDPv4       {}                   {Caption, DatagramsNoPortPersec, DatagramsPersec, DatagramsReceivedErrors...}
Win32_PerfFormattedData_Tcpip_UDPv6 {}                   {Caption, DatagramsNoPortPersec, DatagramsPersec, DatagramsReceivedErrors...}
Win32_PerfRawData_Tcpip_UDPv6       {}                   {Caption, DatagramsNoPortPersec, DatagramsPersec, DatagramsReceivedErrors...}
Win32_PerfFormattedData_TCPIPCou... {}                   {Caption, Deniedconnectorsendrequestsinlowpowermode, Description, Frequency_Object...}
Win32_PerfRawData_TCPIPCounters_... {}                   {Caption, Deniedconnectorsendrequestsinlowpowermode, Description, Frequency_Object...}
Win32_PerfFormattedData_TermServ... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_TermService_Te... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_usbhub_USB  {}                   {AvgBytesPerTransfer, AvgmslatencyforISOtransfers, BulkBytesPerSec, Caption...}
Win32_PerfRawData_usbhub_USB        {}                   {AvgBytesPerTransfer, AvgBytesPerTransfer_Base, AvgmslatencyforISOtransfers, AvgmslatencyforISOtransfers_Base...}
Win32_PerfFormattedData_WindowsW... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_WindowsWorkflo... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_WinNatCo... {}                   {Caption, CurrentSessionCount, Description, DroppedICMPerrorpackets...}
Win32_PerfRawData_WinNatCounters... {}                   {Caption, CurrentSessionCount, Description, DroppedICMPerrorpackets...}
Win32_PerfFormattedData_WinNatCo... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_WinNatCounters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_WinNatCo... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_WinNatCounters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_WinNatCo... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_WinNatCounters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_WinNatCo... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_WinNatCounters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Workflow... {}                   {AverageWorkflowLoadTime, AverageWorkflowPersistTime, Caption, Description...}
Win32_PerfRawData_WorkflowServic... {}                   {AverageWorkflowLoadTime, AverageWorkflowLoadTime_Base, AverageWorkflowPersistTime, AverageWorkflowPersistTime_Base...}

PS C:\Users\Administrator>
```

```PowerShell
PS C:\Users\Administrator> Get-WmiObject -Namespace "root/cimv2" -List | Where-Object {$_.Name -match "process"}

   NameSpace: ROOT\cimv2

Name                                Methods              Properties
----                                -------              ----------
Win32_ProcessTrace                  {}                   {ParentProcessID, ProcessID, ProcessName, SECURITY_DESCRIPTOR...}
Win32_ProcessStartTrace             {}                   {ParentProcessID, ProcessID, ProcessName, SECURITY_DESCRIPTOR...}
Win32_ProcessStopTrace              {}                   {ExitStatus, ParentProcessID, ProcessID, ProcessName...}
Win32_NamedJobObjectProcess         {}                   {Collection, Member}
CIM_Processor                       {SetPowerState, R... {AddressWidth, Availability, Caption, ConfigManagerErrorCode...}
Win32_Processor                     {SetPowerState, R... {AddressWidth, Architecture, Availability, Caption...}
CIM_Process                         {}                   {Caption, CreationClassName, CreationDate, CSCreationClassName...}
Win32_Process                       {Create, Terminat... {Caption, CommandLine, CreationClassName, CreationDate...}
Win32_ProcessStartup                {}                   {CreateFlags, EnvironmentVariables, ErrorMode, FillAttribute...}
Win32_ComputerSystemProcessor       {}                   {GroupComponent, PartComponent}
Win32_SystemProcesses               {}                   {GroupComponent, PartComponent}
CIM_ProcessThread                   {}                   {GroupComponent, PartComponent}
CIM_OSProcess                       {}                   {GroupComponent, PartComponent}
CIM_ProcessExecutable               {}                   {Antecedent, BaseAddress, Dependent, GlobalProcessCount...}
Win32_SessionProcess                {}                   {Antecedent, Dependent}
CIM_AssociatedProcessorMemory       {}                   {Antecedent, BusSpeed, Dependent}
Win32_AssociatedProcessorMemory     {}                   {Antecedent, BusSpeed, Dependent}
Win32_PerfFormattedData_Counters... {}                   {BuildScatterGatherCyclesPersec, Caption, Description, Frequency_Object...}
Win32_PerfRawData_Counters_PerPr... {}                   {BuildScatterGatherCyclesPersec, Caption, Description, Frequency_Object...}
Win32_PerfFormattedData_Counters... {}                   {BuildScatterGatherListCallsPersec, Caption, Description, DPCsDeferredPersec...}
Win32_PerfRawData_Counters_PerPr... {}                   {BuildScatterGatherListCallsPersec, Caption, Description, DPCsDeferredPersec...}
Win32_PerfFormattedData_Counters... {}                   {AverageIdleTime, C1TransitionsPersec, C2TransitionsPersec, C3TransitionsPersec...}
Win32_PerfRawData_Counters_Proce... {}                   {AverageIdleTime, AverageIdleTime_Base, C1TransitionsPersec, C2TransitionsPersec...}
Win32_PerfFormattedData_Lsa_Secu... {}                   {Caption, ContextHandles, CredentialHandles, Description...}
Win32_PerfRawData_Lsa_SecurityPe... {}                   {Caption, ContextHandles, CredentialHandles, Description...}
Win32_PerfFormattedData_PerfOS_P... {}                   {C1TransitionsPersec, C2TransitionsPersec, C3TransitionsPersec, Caption...}
Win32_PerfRawData_PerfOS_Processor  {}                   {C1TransitionsPersec, C2TransitionsPersec, C3TransitionsPersec, Caption...}
Win32_PerfFormattedData_PerfProc... {}                   {Caption, CreatingProcessID, Description, ElapsedTime...}
Win32_PerfRawData_PerfProc_Process  {}                   {Caption, CreatingProcessID, Description, ElapsedTime...}
Win32_PerfFormattedData_PerfProc... {}                   {BytesFree, BytesImageFree, BytesImageReserved, BytesReserved...}
Win32_PerfRawData_PerfProc_Proce... {}                   {BytesFree, BytesImageFree, BytesImageReserved, BytesReserved...}

PS C:\Users\Administrator>
```

```PowerShell
PS C:\Users\Administrator> Get-WmiObject -Namespace "root/cimv2" -List | Where-Object {$_.Name -match "computer"}

   NameSpace: ROOT\cimv2

Name                                Methods              Properties
----                                -------              ----------
Win32_ComputerSystemEvent           {}                   {MachineName, SECURITY_DESCRIPTOR, TIME_CREATED}
Win32_ComputerShutdownEvent         {}                   {MachineName, SECURITY_DESCRIPTOR, TIME_CREATED, Type}
CIM_ComputerSystem                  {}                   {Caption, CreationClassName, Description, InstallDate...}
CIM_UnitaryComputerSystem           {SetPowerState}      {Caption, CreationClassName, Description, InitialLoadInfo...}
Win32_ComputerSystem                {SetPowerState, R... {AdminPasswordStatus, AutomaticManagedPagefile, AutomaticResetBootOption, AutomaticResetCapability...}
CIM_ComputerSystemResource          {}                   {GroupComponent, PartComponent}
CIM_ComputerSystemMappedIO          {}                   {GroupComponent, PartComponent}
CIM_ComputerSystemDMA               {}                   {GroupComponent, PartComponent}
CIM_ComputerSystemIRQ               {}                   {GroupComponent, PartComponent}
Win32_ComputerSystemProcessor       {}                   {GroupComponent, PartComponent}
CIM_ComputerSystemPackage           {}                   {Antecedent, Dependent}
Win32_ComputerSystemProduct         {}                   {Caption, Description, IdentifyingNumber, Name...}
Win32_NTLogEventComputer            {}                   {Computer, Record}

PS C:\Users\Administrator>
```

```PowerShell
PS C:\Users\Administrator> Get-WmiObject -Namespace "root/cimv2" -List | Where-Object {$_.Name -match "win32"}

   NameSpace: ROOT\cimv2

Name                                Methods              Properties
----                                -------              ----------
__Win32Provider                     {}                   {ClientLoadableCLSID, CLSID, Concurrency, DefaultMachineName...}
Win32_ComputerSystemEvent           {}                   {MachineName, SECURITY_DESCRIPTOR, TIME_CREATED}
Win32_ComputerShutdownEvent         {}                   {MachineName, SECURITY_DESCRIPTOR, TIME_CREATED, Type}
Win32_IP4RouteTableEvent            {}                   {SECURITY_DESCRIPTOR, TIME_CREATED}
Win32_SystemTrace                   {}                   {SECURITY_DESCRIPTOR, TIME_CREATED}
Win32_ProcessTrace                  {}                   {ParentProcessID, ProcessID, ProcessName, SECURITY_DESCRIPTOR...}
Win32_ProcessStartTrace             {}                   {ParentProcessID, ProcessID, ProcessName, SECURITY_DESCRIPTOR...}
Win32_ProcessStopTrace              {}                   {ExitStatus, ParentProcessID, ProcessID, ProcessName...}
Win32_ModuleTrace                   {}                   {SECURITY_DESCRIPTOR, TIME_CREATED}
Win32_ModuleLoadTrace               {}                   {DefaultBase, FileName, ImageBase, ImageChecksum...}
Win32_ThreadTrace                   {}                   {ProcessID, SECURITY_DESCRIPTOR, ThreadID, TIME_CREATED}
Win32_ThreadStartTrace              {}                   {ProcessID, SECURITY_DESCRIPTOR, StackBase, StackLimit...}
Win32_ThreadStopTrace               {}                   {ProcessID, SECURITY_DESCRIPTOR, ThreadID, TIME_CREATED}
Win32_PowerManagementEvent          {}                   {EventType, OEMEventCode, SECURITY_DESCRIPTOR, TIME_CREATED}
Win32_DeviceChangeEvent             {}                   {EventType, SECURITY_DESCRIPTOR, TIME_CREATED}
Win32_SystemConfigurationChangeE... {}                   {EventType, SECURITY_DESCRIPTOR, TIME_CREATED}
Win32_VolumeChangeEvent             {}                   {DriveName, EventType, SECURITY_DESCRIPTOR, TIME_CREATED}
Win32_PrivilegesStatus              {}                   {Description, Operation, ParameterInfo, PrivilegesNotHeld...}
Win32_JobObjectStatus               {}                   {AdditionalDescription, Description, Operation, ParameterInfo...}
Win32_Trustee                       {}                   {Domain, Name, SID, SidLength...}
Win32_ACE                           {}                   {AccessMask, AceFlags, AceType, GuidInheritedObjectType...}
Win32_SecurityDescriptor            {}                   {ControlFlags, DACL, Group, Owner...}
Win32_CollectionStatistics          {}                   {Collection, Stats}
Win32_NamedJobObjectStatistics      {}                   {Collection, Stats}
Win32_NTLogEvent                    {}                   {Category, CategoryString, ComputerName, Data...}
Win32_ActiveRoute                   {}                   {SameElement, SystemElement}
Win32_AccountSID                    {}                   {Element, Setting}
Win32_SecurityDescriptorHelper      {Win32SDToSDDL, W... {}
Win32_TimeZone                      {}                   {Bias, Caption, DaylightBias, DaylightDay...}
Win32_PageFileSetting               {}                   {Caption, Description, InitialSize, MaximumSize...}
Win32_Desktop                       {}                   {BorderWidth, Caption, CoolSwitch, CursorBlinkRate...}
Win32_ShadowContext                 {}                   {Caption, ClientAccessible, Description, Differential...}
Win32_MSIResource                   {}                   {Caption, Description, SettingID}
Win32_ServiceControl                {}                   {Arguments, Caption, Description, Event...}
Win32_Property                      {}                   {Caption, Description, ProductCode, Property...}
Win32_Patch                         {}                   {Attributes, Caption, Description, File...}
Win32_PatchPackage                  {}                   {Caption, Description, PatchID, ProductCode...}
Win32_Binary                        {}                   {Caption, Data, Description, Name...}
Win32_AutochkSetting                {}                   {Caption, Description, SettingID, UserInputDelay}
Win32_SerialPortConfiguration       {}                   {AbortReadWriteOnError, BaudRate, BinaryModeEnabled, BitsPerByte...}
Win32_StartupCommand                {}                   {Caption, Command, Description, Location...}
Win32_BootConfiguration             {}                   {BootDirectory, Caption, ConfigurationPath, Description...}
Win32_NetworkLoginProfile           {}                   {AccountExpires, AuthorizationFlags, BadPasswordCount, Caption...}
Win32_NamedJobObjectLimitSetting    {}                   {ActiveProcessLimit, Affinity, Caption, Description...}
Win32_NamedJobObjectSecLimitSetting {}                   {Caption, Description, PrivilegesToDelete, RestrictedSIDs...}
Win32_DisplayConfiguration          {}                   {BitsPerPel, Caption, Description, DeviceName...}
Win32_NetworkAdapterConfiguration   {EnableDHCP, Rene... {ArpAlwaysSourceRoute, ArpUseEtherSNAP, Caption, DatabasePath...}
Win32_QuotaSetting                  {}                   {Caption, DefaultLimit, DefaultWarningLimit, Description...}
Win32_SecuritySetting               {GetSecurityDescr... {Caption, ControlFlags, Description, SettingID}
Win32_LogicalFileSecuritySetting    {GetSecurityDescr... {Caption, ControlFlags, Description, OwnerPermissions...}
Win32_LogicalShareSecuritySetting   {GetSecurityDescr... {Caption, ControlFlags, Description, Name...}
Win32_DisplayControllerConfigura... {}                   {BitsPerPixel, Caption, ColorPlanes, Description...}
Win32_WMISetting                    {}                   {ASPScriptDefaultNamespace, ASPScriptEnabled, AutorecoverMofs, AutoStartWin9X...}
Win32_OSRecoveryConfiguration       {}                   {AutoReboot, Caption, DebugFilePath, DebugInfoType...}
Win32_COMSetting                    {}                   {Caption, Description, SettingID}
Win32_ClassicCOMClassSetting        {}                   {AppID, AutoConvertToClsid, AutoTreatAsClsid, Caption...}
Win32_DCOMApplicationSetting        {GetLaunchSecurit... {AppID, AuthenticationLevel, Caption, CustomSurrogate...}
Win32_VideoConfiguration            {}                   {ActualColorResolution, AdapterChipType, AdapterCompatibility, AdapterDACType...}
Win32_ODBCAttribute                 {}                   {Attribute, Caption, Description, Driver...}
Win32_ODBCSourceAttribute           {}                   {Attribute, Caption, DataSource, Description...}
Win32_PrinterConfiguration          {}                   {BitsPerPel, Caption, Collate, Color...}
Win32_CurrentTime                   {}                   {Day, DayOfWeek, Hour, Milliseconds...}
Win32_UTCTime                       {}                   {Day, DayOfWeek, Hour, Milliseconds...}
Win32_LocalTime                     {}                   {Day, DayOfWeek, Hour, Milliseconds...}
Win32_ShortcutAction                {Invoke}             {ActionID, Arguments, Caption, Description...}
Win32_ExtensionInfoAction           {Invoke}             {ActionID, Argument, Caption, Command...}
Win32_CreateFolderAction            {Invoke}             {ActionID, Caption, Description, Direction...}
Win32_RegistryAction                {Invoke}             {ActionID, Caption, Description, Direction...}
Win32_ClassInfoAction               {Invoke}             {ActionID, AppID, Argument, Caption...}
Win32_SelfRegModuleAction           {Invoke}             {ActionID, Caption, Cost, Description...}
Win32_TypeLibraryAction             {Invoke}             {ActionID, Caption, Cost, Description...}
Win32_BindImageAction               {Invoke}             {ActionID, Caption, Description, Direction...}
Win32_RemoveIniAction               {Invoke}             {Action, ActionID, Caption, Description...}
Win32_MIMEInfoAction                {Invoke}             {ActionID, Caption, CLSID, ContentType...}
Win32_FontInfoAction                {Invoke}             {ActionID, Caption, Description, Direction...}
Win32_PublishComponentAction        {Invoke}             {ActionID, AppData, Caption, ComponentID...}
Win32_MoveFileAction                {Invoke}             {ActionID, Caption, Description, DestFolder...}
Win32_DuplicateFileAction           {Invoke}             {ActionID, Caption, DeleteAfterCopy, Description...}
Win32_RemoveFileAction              {Invoke}             {ActionID, Caption, Description, Direction...}
Win32_ProductResource               {}                   {Product, Resource}
Win32_FolderRedirectionHealth       {}                   {HealthStatus, LastSuccessfulSyncTime, LastSyncStatus, LastSyncTime...}
Win32_MountPoint                    {}                   {Directory, Volume}
Win32_UserProfile                   {ChangeOwner}        {AppDataRoaming, Contacts, Desktop, Documents...}
Win32_RoamingProfileMachineConfi... {}                   {AddAdminGroupToRUPEnabled, AllowCrossForestUserPolicy, BackgroundUploadParams, DeleteProfilesOlderDays...}
Win32_ManagedSystemElementResource  {}                   {}
Win32_SoftwareElementResource       {}                   {Element, Setting}
Win32_SID                           {}                   {AccountName, BinaryRepresentation, ReferencedDomainName, SID...}
Win32_ActionCheck                   {}                   {Action, Check}
Win32_UserDesktop                   {}                   {Element, Setting}
Win32_DeviceSettings                {}                   {Element, Setting}
Win32_PrinterSetting                {}                   {Element, Setting}
Win32_NetworkAdapterSetting         {}                   {Element, Setting}
Win32_SerialPortSetting             {}                   {Element, Setting}
Win32_SystemSetting                 {}                   {Element, Setting}
Win32_SystemProgramGroups           {}                   {Element, Setting}
Win32_SystemBootConfiguration       {}                   {Element, Setting}
Win32_SystemTimeZone                {}                   {Element, Setting}
Win32_SystemDesktop                 {}                   {Element, Setting}
Win32_ClassicCOMClassSettings       {}                   {Element, Setting}
Win32_VolumeQuota                   {}                   {Element, Setting}
Win32_WMIElementSetting             {}                   {Element, Setting}
Win32_COMApplicationSettings        {}                   {Element, Setting}
Win32_VideoSettings                 {}                   {Element, Setting}
Win32_SecuritySettingOfObject       {}                   {Element, Setting}
Win32_SecuritySettingOfLogicalShare {}                   {Element, Setting}
Win32_SecuritySettingOfLogicalFile  {}                   {Element, Setting}
Win32_PageFileElementSetting        {}                   {Element, Setting}
Win32_OperatingSystemAutochkSetting {}                   {Element, Setting}
Win32_VolumeQuotaSetting            {}                   {Element, Setting}
Win32_ProductSoftwareFeatures       {}                   {Component, Product}
Win32_ImplementedCategory           {}                   {Category, Component}
Win32_RoamingProfileUserConfigur... {}                   {DirectoriesToSyncAtLogonLogoff, ExcludedProfileDirs, IsConfiguredByWMI}
Win32_InstalledSoftwareElement      {}                   {Software, System}
Win32_SoftwareFeatureCheck          {}                   {Check, Element}
Win32_LUIDandAttributes             {}                   {Attributes, LUID}
Win32_VolumeUserQuota               {}                   {Account, DiskSpaceUsed, Limit, Status...}
Win32_LUID                          {}                   {HighPart, LowPart}
Win32_DirectorySpecification        {Invoke}             {Caption, CheckID, CheckMode, DefaultDir...}
Win32_SoftwareElementCondition      {Invoke}             {Caption, CheckID, CheckMode, Condition...}
Win32_ODBCDriverSpecification       {Invoke}             {Caption, CheckID, CheckMode, Description...}
Win32_ServiceSpecification          {Invoke}             {Caption, CheckID, CheckMode, Dependencies...}
Win32_FileSpecification             {Invoke}             {Attributes, Caption, CheckID, CheckMode...}
Win32_IniFileSpecification          {Invoke}             {Action, Caption, CheckID, CheckMode...}
Win32_LaunchCondition               {Invoke}             {Caption, CheckID, CheckMode, Condition...}
Win32_ODBCDataSourceSpecification   {Invoke}             {Caption, CheckID, CheckMode, DataSource...}
Win32_ODBCTranslatorSpecification   {Invoke}             {Caption, CheckID, CheckMode, Description...}
Win32_ProgIDSpecification           {Invoke}             {Caption, CheckID, CheckMode, Description...}
Win32_EnvironmentSpecification      {Invoke}             {Caption, CheckID, CheckMode, Description...}
Win32_ReserveCost                   {Invoke}             {Caption, CheckID, CheckMode, Description...}
Win32_Condition                     {Invoke}             {Caption, CheckID, CheckMode, Condition...}
Win32_ShadowStorage                 {Create}             {AllocatedSpace, DiffVolume, MaxSpace, UsedSpace...}
Win32_DCOMApplicationAccessAllow... {}                   {Element, Setting}
Win32_FolderRedirection             {}                   {ContentsMoved, ContentsMovedOnPolicyRemoval, ContentsRenamedInLocalCache, ExclusiveRightsGranted...}
Win32_NamedJobObjectProcess         {}                   {Collection, Member}
Win32_TokenPrivileges               {}                   {PrivilegeCount, Privileges}
Win32_NamedJobObject                {}                   {BasicUIRestrictions, Caption, CollectionID, Description}
Win32_PnPDevice                     {}                   {SameElement, SystemElement}
Win32_ServiceSpecificationService   {}                   {Check, Element}
Win32_ShareToDirectory              {}                   {Share, SharedElement}
Win32_SettingCheck                  {}                   {Check, Setting}
Win32_PatchFile                     {}                   {Check, Setting}
Win32_ODBCDriverAttribute           {}                   {Check, Setting}
Win32_ODBCDataSourceAttribute       {}                   {Check, Setting}
Win32_ClientApplicationSetting      {}                   {Application, Client}
Win32_RoamingUserHealthConfigura... {}                   {HealthStatusForTempProfiles, LastProfileDownloadIntervalCautionInHours, LastProfileDownloadIntervalUnhealthyInHours, LastProfileUploadInterva...
Win32_UserStateConfigurationCont... {}                   {FolderRedirection, OfflineFiles, RoamingUserProfile}
Win32_ServerFeature                 {}                   {ID, Name, ParentID}
Win32_SecuritySettingOwner          {}                   {Owner, SecuritySetting}
Win32_LogicalFileOwner              {}                   {Owner, SecuritySetting}
Win32_PhysicalMedia                 {}                   {Capacity, Caption, CleanerMedia, CreationClassName...}
Win32_PhysicalMemory                {}                   {BankLabel, Capacity, Caption, CreationClassName...}
Win32_OnBoardDevice                 {}                   {Caption, CreationClassName, Description, DeviceType...}
Win32_BaseBoard                     {IsCompatible}       {Caption, ConfigOptions, CreationClassName, Depth...}
Win32_SystemEnclosure               {IsCompatible}       {AudibleAlarm, BreachDescription, CableManagementStrategy, Caption...}
Win32_PhysicalMemoryArray           {IsCompatible}       {Caption, CreationClassName, Depth, Description...}
Win32_SystemSlot                    {}                   {Caption, ConnectorPinout, ConnectorType, CreationClassName...}
Win32_PortConnector                 {}                   {Caption, ConnectorPinout, ConnectorType, CreationClassName...}
Win32_Thread                        {}                   {Caption, CreationClassName, CSCreationClassName, CSName...}
Win32_COMApplication                {}                   {Caption, Description, InstallDate, Name...}
Win32_DCOMApplication               {}                   {AppID, Caption, Description, InstallDate...}
Win32_ScheduledJob                  {Create, Delete}     {Caption, Command, DaysOfMonth, DaysOfWeek...}
Win32_PrintJob                      {Pause, Resume}      {Caption, Color, DataType, Description...}
Win32_ServerSession                 {}                   {ActiveTime, Caption, ClientType, ComputerName...}
Win32_ComputerSystem                {SetPowerState, R... {AdminPasswordStatus, AutomaticManagedPagefile, AutomaticResetBootOption, AutomaticResetCapability...}
Win32_NTDomain                      {}                   {Caption, ClientSiteName, CreationClassName, DcSiteName...}
Win32_SoftwareFeature               {Reinstall, Confi... {Accesses, Attributes, Caption, Description...}
Win32_TemperatureProbe              {SetPowerState, R... {Accuracy, Availability, Caption, ConfigManagerErrorCode...}
Win32_VoltageProbe                  {SetPowerState, R... {Accuracy, Availability, Caption, ConfigManagerErrorCode...}
Win32_CurrentProbe                  {SetPowerState, R... {Accuracy, Availability, Caption, ConfigManagerErrorCode...}
Win32_Bus                           {SetPowerState, R... {Availability, BusNum, BusType, Caption...}
Win32_Keyboard                      {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
Win32_DesktopMonitor                {SetPowerState, R... {Availability, Bandwidth, Caption, ConfigManagerErrorCode...}
Win32_PointingDevice                {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
Win32_USBHub                        {SetPowerState, R... {Availability, Caption, ClassCode, ConfigManagerErrorCode...}
Win32_NetworkAdapter                {SetPowerState, R... {AdapterType, AdapterTypeId, AutoSense, Availability...}
Win32_Battery                       {SetPowerState, R... {Availability, BatteryRechargeTime, BatteryStatus, Caption...}
Win32_PortableBattery               {SetPowerState, R... {Availability, BatteryStatus, CapacityMultiplier, Caption...}
Win32_SoundDevice                   {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
Win32_MotherboardDevice             {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
Win32_DiskDrive                     {SetPowerState, R... {Availability, BytesPerSector, Capabilities, CapabilityDescriptions...}
Win32_FloppyDrive                   {SetPowerState, R... {Availability, Capabilities, CapabilityDescriptions, Caption...}
Win32_TapeDrive                     {SetPowerState, R... {Availability, Capabilities, CapabilityDescriptions, Caption...}
Win32_CDROMDrive                    {SetPowerState, R... {Availability, Capabilities, CapabilityDescriptions, Caption...}
Win32_PnPEntity                     {SetPowerState, R... {Availability, Caption, ClassGuid, CompatibleID...}
Win32_POTSModem                     {SetPowerState, R... {AnswerMode, AttachedTo, Availability, BlindOff...}
Win32_HeatPipe                      {SetPowerState, R... {ActiveCooling, Availability, Caption, ConfigManagerErrorCode...}
Win32_Refrigeration                 {SetPowerState, R... {ActiveCooling, Availability, Caption, ConfigManagerErrorCode...}
Win32_Fan                           {SetPowerState, R... {ActiveCooling, Availability, Caption, ConfigManagerErrorCode...}
Win32_Printer                       {SetPowerState, R... {Attributes, Availability, AvailableJobSheets, AveragePagesPerMinute...}
Win32_SCSIController                {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
Win32_InfraredDevice                {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
Win32_PCMCIAController              {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
Win32_FloppyController              {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
Win32_VideoController               {SetPowerState, R... {AcceleratorCapabilities, AdapterCompatibility, AdapterDACType, AdapterRAM...}
Win32_USBController                 {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
Win32_SerialPort                    {SetPowerState, R... {Availability, Binary, Capabilities, CapabilityDescriptions...}
Win32_ParallelPort                  {SetPowerState, R... {Availability, Capabilities, CapabilityDescriptions, Caption...}
Win32_IDEController                 {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
Win32_1394Controller                {SetPowerState, R... {Availability, Caption, ConfigManagerErrorCode, ConfigManagerUserConfig...}
Win32_CacheMemory                   {SetPowerState, R... {Access, AdditionalErrorData, Associativity, Availability...}
Win32_Volume                        {SetPowerState, R... {Access, Automount, Availability, BlockSize...}
Win32_SMBIOSMemory                  {SetPowerState, R... {Access, AdditionalErrorData, Availability, BlockSize...}
Win32_MemoryArray                   {SetPowerState, R... {Access, AdditionalErrorData, Availability, BlockSize...}
Win32_MemoryDevice                  {SetPowerState, R... {Access, AdditionalErrorData, Availability, BlockSize...}
Win32_LogicalDisk                   {SetPowerState, R... {Access, Availability, BlockSize, Caption...}
Win32_MappedLogicalDisk             {SetPowerState, R... {Access, Availability, BlockSize, Caption...}
Win32_DiskPartition                 {SetPowerState, R... {Access, Availability, BlockSize, Bootable...}
Win32_Processor                     {SetPowerState, R... {AddressWidth, Architecture, Availability, Caption...}
Win32_OptionalFeature               {}                   {Caption, Description, InstallDate, InstallState...}
Win32_DfsNode                       {Create}             {Caption, Description, InstallDate, Name...}
Win32_ComponentCategory             {}                   {Caption, CategoryId, Description, InstallDate...}
Win32_ProgramGroupOrItem            {}                   {Caption, Description, InstallDate, Name...}
Win32_LogicalProgramGroupItem       {}                   {Caption, Description, InstallDate, Name...}
Win32_LogicalProgramGroup           {}                   {Caption, Description, GroupName, InstallDate...}
Win32_NetworkConnection             {}                   {AccessMask, Caption, Comment, ConnectionState...}
Win32_COMClass                      {}                   {Caption, Description, InstallDate, Name...}
Win32_ClassicCOMClass               {}                   {Caption, ComponentId, Description, InstallDate...}
Win32_Account                       {}                   {Caption, Description, Domain, InstallDate...}
Win32_UserAccount                   {Rename}             {AccountType, Caption, Description, Disabled...}
Win32_Group                         {Rename}             {Caption, Description, Domain, InstallDate...}
Win32_SystemAccount                 {}                   {Caption, Description, Domain, InstallDate...}
Win32_BaseService                   {StartService, St... {AcceptPause, AcceptStop, Caption, CreationClassName...}
Win32_SystemDriver                  {StartService, St... {AcceptPause, AcceptStop, Caption, CreationClassName...}
Win32_Service                       {StartService, St... {AcceptPause, AcceptStop, Caption, CheckPoint...}
Win32_TerminalService               {StartService, St... {AcceptPause, AcceptStop, Caption, CheckPoint...}
Win32_PnPSignedDriver               {StartService, St... {Caption, ClassGuid, CompatID, CreationClassName...}
Win32_ApplicationService            {StartService, St... {Caption, CreationClassName, Description, InstallDate...}
Win32_PrinterDriver                 {StartService, St... {Caption, ConfigFile, CreationClassName, DataFile...}
Win32_TCPIPPrinterPort              {}                   {ByteCount, Caption, CreationClassName, Description...}
Win32_CommandLineAccess             {}                   {Caption, CommandLine, CreationClassName, Description...}
Win32_SystemMemoryResource          {}                   {Caption, CreationClassName, CSCreationClassName, CSName...}
Win32_PortResource                  {}                   {Alias, Caption, CreationClassName, CSCreationClassName...}
Win32_DeviceMemoryAddress           {}                   {Caption, CreationClassName, CSCreationClassName, CSName...}
Win32_IRQResource                   {}                   {Availability, Caption, CreationClassName, CSCreationClassName...}
Win32_Environment                   {}                   {Caption, Description, InstallDate, Name...}
Win32_DMAChannel                    {}                   {AddressSize, Availability, BurstMode, ByteMode...}
Win32_Share                         {Create, SetShare... {AccessMask, AllowMaximum, Caption, Description...}
Win32_ClusterShare                  {Create, SetShare... {AccessMask, AllowMaximum, Caption, Description...}
Win32_NetworkProtocol               {}                   {Caption, ConnectionlessService, Description, GuaranteesDelivery...}
Win32_ShadowProvider                {}                   {Caption, CLSID, Description, ID...}
Win32_QuickFixEngineering           {}                   {Caption, CSName, Description, FixComments...}
Win32_IP4RouteTable                 {}                   {Age, Caption, Description, Destination...}
Win32_ShadowCopy                    {Create, Revert}     {Caption, ClientAccessible, Count, Description...}
Win32_LoadOrderGroup                {}                   {Caption, Description, DriverEnabled, GroupOrder...}
Win32_Process                       {Create, Terminat... {Caption, CommandLine, CreationClassName, CreationDate...}
Win32_Session                       {}                   {Caption, Description, InstallDate, Name...}
Win32_LogonSession                  {}                   {AuthenticationPackage, Caption, Description, InstallDate...}
Win32_ServerConnection              {}                   {ActiveTime, Caption, ComputerName, ConnectionID...}
Win32_DfsTarget                     {}                   {Caption, Description, InstallDate, LinkName...}
Win32_NetworkClient                 {}                   {Caption, Description, InstallDate, Manufacturer...}
Win32_PageFileUsage                 {}                   {AllocatedBaseSize, Caption, CurrentUsage, Description...}
Win32_OperatingSystem               {Reboot, Shutdown... {BootDevice, BuildNumber, BuildType, Caption...}
Win32_Directory                     {TakeOwnerShip, C... {AccessMask, Archive, Caption, Compressed...}
Win32_ShortcutFile                  {TakeOwnerShip, C... {AccessMask, Archive, Caption, Compressed...}
Win32_CodecFile                     {TakeOwnerShip, C... {AccessMask, Archive, Caption, Compressed...}
Win32_NTEventlogFile                {TakeOwnerShip, C... {AccessMask, Archive, Caption, Compressed...}
Win32_PageFile                      {TakeOwnerShip, C... {AccessMask, Archive, Caption, Compressed...}
Win32_IP4PersistedRouteTable        {}                   {Caption, Description, Destination, InstallDate...}
Win32_Registry                      {}                   {Caption, CurrentSize, Description, InstallDate...}
Win32_BIOS                          {}                   {BiosCharacteristics, BIOSVersion, BuildNumber, Caption...}
Win32_SoftwareElement               {}                   {Attributes, BuildNumber, Caption, CodeSet...}
Win32_ShortcutSAP                   {}                   {Action, Element}
Win32_MethodParameterClass          {}                   {}
Win32_ProcessStartup                {}                   {CreateFlags, EnvironmentVariables, ErrorMode, FillAttribute...}
Win32_PingStatus                    {}                   {Address, BufferSize, NoFragmentation, PrimaryAddressResolutionStatus...}
Win32_SoftwareElementCheck          {}                   {Check, Element, Phase}
Win32_ODBCDriverSoftwareElement     {}                   {Check, Element, Phase}
Win32_SystemServices                {}                   {GroupComponent, PartComponent}
Win32_SystemNetworkConnections      {}                   {GroupComponent, PartComponent}
Win32_SystemResources               {}                   {GroupComponent, PartComponent}
Win32_SystemBIOS                    {}                   {GroupComponent, PartComponent}
Win32_SystemLoadOrderGroups         {}                   {GroupComponent, PartComponent}
Win32_SystemUsers                   {}                   {GroupComponent, PartComponent}
Win32_SystemOperatingSystem         {}                   {GroupComponent, PartComponent, PrimaryOS}
Win32_SystemDevices                 {}                   {GroupComponent, PartComponent}
Win32_ComputerSystemProcessor       {}                   {GroupComponent, PartComponent}
Win32_SystemPartitions              {}                   {GroupComponent, PartComponent}
Win32_SystemSystemDriver            {}                   {GroupComponent, PartComponent}
Win32_SystemProcesses               {}                   {GroupComponent, PartComponent}
Win32_COMApplicationClasses         {}                   {GroupComponent, PartComponent}
Win32_ClassicCOMApplicationClasses  {}                   {GroupComponent, PartComponent}
Win32_UserInDomain                  {}                   {GroupComponent, PartComponent}
Win32_LoadOrderGroupServiceMembers  {}                   {GroupComponent, PartComponent}
Win32_LogicalDiskRootDirectory      {}                   {GroupComponent, PartComponent}
Win32_SoftwareFeatureSoftwareEle... {}                   {GroupComponent, PartComponent}
Win32_MemoryDeviceArray             {}                   {GroupComponent, PartComponent}
Win32_GroupInDomain                 {}                   {GroupComponent, PartComponent}
Win32_GroupUser                     {}                   {GroupComponent, PartComponent}
Win32_ProgramGroupContents          {}                   {GroupComponent, PartComponent}
Win32_SubDirectory                  {}                   {GroupComponent, PartComponent}
Win32_PhysicalMemoryLocation        {}                   {GroupComponent, LocationWithinContainer, PartComponent}
Win32_FolderRedirectionUserConfi... {}                   {AppDataRoaming, Contacts, Desktop, Documents...}
Win32_Reliability                   {}                   {}
Win32_ReliabilityStabilityMetrics   {GetRecordCount}     {EndMeasurementDate, RelID, StartMeasurementDate, SystemStabilityIndex...}
Win32_ReliabilityRecords            {GetRecordCount}     {ComputerName, EventIdentifier, InsertionStrings, Logfile...}
Win32_NTLogEventLog                 {}                   {Log, Record}
Win32_DiskQuota                     {}                   {DiskSpaceUsed, Limit, QuotaVolume, Status...}
Win32_ComClassAutoEmulator          {}                   {NewVersion, OldVersion}
Win32_FolderRedirectionHealthCon... {}                   {LastSyncDurationCautionInHours, LastSyncDurationUnhealthyInHours}
Win32_ComClassEmulator              {}                   {NewVersion, OldVersion}
Win32_SoftwareFeatureAction         {}                   {Action, Element}
Win32_NamedJobObjectActgInfo        {}                   {ActiveProcesses, Caption, Description, Name...}
Win32_Perf                          {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData                   {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData             {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_SecuritySettingGroup          {}                   {Group, SecuritySetting}
Win32_LogicalFileGroup              {}                   {Group, SecuritySetting}
Win32_DCOMApplicationLaunchAllow... {}                   {Element, Setting}
Win32_SecuritySettingAuditing       {}                   {AuditedAccessMask, GuidInheritedObjectType, GuidObjectType, Inheritance...}
Win32_LogicalFileAuditing           {}                   {AuditedAccessMask, GuidInheritedObjectType, GuidObjectType, Inheritance...}
Win32_LogicalShareAuditing          {}                   {AuditedAccessMask, GuidInheritedObjectType, GuidObjectType, Inheritance...}
Win32_SoftwareElementAction         {}                   {Action, Element}
Win32_ApplicationCommandLine        {}                   {Antecedent, Dependent}
Win32_SubSession                    {}                   {Antecedent, Dependent}
Win32_ShadowVolumeSupport           {}                   {Antecedent, Dependent}
Win32_DeviceBus                     {}                   {Antecedent, Dependent}
Win32_SessionConnection             {}                   {Antecedent, Dependent}
Win32_ShadowFor                     {}                   {Antecedent, Dependent}
Win32_LogonSessionMappedDisk        {}                   {Antecedent, Dependent}
Win32_PrinterShare                  {}                   {Antecedent, Dependent}
Win32_PnPSignedDriverCIMDataFile    {}                   {Antecedent, Dependent}
Win32_ConnectionShare               {}                   {Antecedent, Dependent}
Win32_LoadOrderGroupServiceDepen... {}                   {Antecedent, Dependent}
Win32_SessionResource               {}                   {Antecedent, Dependent}
Win32_SessionProcess                {}                   {Antecedent, Dependent}
Win32_AssociatedProcessorMemory     {}                   {Antecedent, BusSpeed, Dependent}
Win32_SoftwareFeatureParent         {}                   {Antecedent, Dependent}
Win32_ShadowOn                      {}                   {Antecedent, Dependent}
Win32_PrinterDriverDll              {}                   {Antecedent, Dependent}
Win32_DependentService              {}                   {Antecedent, Dependent, TypeOfDependency}
Win32_LogicalDiskToPartition        {}                   {Antecedent, Dependent, EndingAddress, StartingAddress}
Win32_OperatingSystemQFE            {}                   {Antecedent, Dependent}
Win32_LoggedOnUser                  {}                   {Antecedent, Dependent}
Win32_SystemDriverPNPEntity         {}                   {Antecedent, Dependent}
Win32_DfsNodeTarget                 {}                   {Antecedent, Dependent}
Win32_CIMLogicalDeviceCIMDataFile   {}                   {Antecedent, Dependent, Purpose, PurposeDescription}
Win32_SCSIControllerDevice          {}                   {AccessState, Antecedent, Dependent, NegotiatedDataWidth...}
Win32_POTSModemToSerialPort         {}                   {AccessState, Antecedent, Dependent, NegotiatedDataWidth...}
Win32_USBControllerDevice           {}                   {AccessState, Antecedent, Dependent, NegotiatedDataWidth...}
Win32_PrinterController             {}                   {AccessState, Antecedent, Dependent, NegotiatedDataWidth...}
Win32_IDEControllerDevice           {}                   {AccessState, Antecedent, Dependent, NegotiatedDataWidth...}
Win32_ControllerHasHub              {}                   {AccessState, Antecedent, Dependent, NegotiatedDataWidth...}
Win32_1394ControllerDevice          {}                   {AccessState, Antecedent, Dependent, NegotiatedDataWidth...}
Win32_DriverForDevice               {}                   {Antecedent, Dependent}
Win32_LogicalProgramGroupItemDat... {}                   {Antecedent, Dependent}
Win32_PNPAllocatedResource          {}                   {Antecedent, Dependent}
Win32_DiskDrivePhysicalMedia        {}                   {Antecedent, Dependent}
Win32_MemoryDeviceLocation          {}                   {Antecedent, Dependent}
Win32_MemoryArrayLocation           {}                   {Antecedent, Dependent}
Win32_ShadowBy                      {}                   {Antecedent, Dependent}
Win32_AllocatedResource             {}                   {Antecedent, Dependent}
Win32_DiskDriveToDiskPartition      {}                   {Antecedent, Dependent}
Win32_LogicalProgramGroupDirectory  {}                   {Antecedent, Dependent}
Win32_ShadowDiffVolumeSupport       {}                   {Antecedent, Dependent}
Win32_Product                       {Install, Admin, ... {AssignmentType, Caption, Description, HelpLink...}
Win32_ComputerSystemProduct         {}                   {Caption, Description, IdentifyingNumber, Name...}
Win32_ProductCheck                  {}                   {Check, Product}
Win32_NTLogEventUser                {}                   {Record, User}
Win32_ProtocolBinding               {}                   {Antecedent, Dependent, Device}
Win32_NamedJobObjectLimit           {}                   {Collection, Setting}
Win32_NamedJobObjectSecLimit        {}                   {Collection, Setting}
Win32_NTLogEventComputer            {}                   {Computer, Record}
Win32_TokenGroups                   {}                   {GroupCount, Groups}
Win32_DefragAnalysis                {}                   {AverageFileSize, AverageFragmentsPerFile, AverageFreeSpacePerExtent, ClusterSize...}
Win32_SIDandAttributes              {}                   {Attributes, SID}
Win32_CheckCheck                    {}                   {Check, Location}
Win32_RoamingProfileBackgroundUp... {}                   {Interval, SchedulingMethod, Time}
Win32_RoamingProfileSlowLinkParams  {}                   {ConnectionTransferRate, TimeOut}
Win32_SecuritySettingAccess         {}                   {AccessMask, GuidInheritedObjectType, GuidObjectType, Inheritance...}
Win32_LogicalFileAccess             {}                   {AccessMask, GuidInheritedObjectType, GuidObjectType, Inheritance...}
Win32_LogicalShareAccess            {}                   {AccessMask, GuidInheritedObjectType, GuidObjectType, Inheritance...}
Win32_OfflineFilesHealth            {}                   {LastSuccessfulSyncTime, LastSyncStatus, LastSyncTime, OfflineAccessEnabled...}
Win32_PerfFormattedData_ADWS_ADWS   {}                   {ActiveWebServiceSessions, AllocatedConnections, Caption, ChangeOptionalFeatureOperationsPerSecond...}
Win32_PerfRawData_ADWS_ADWS         {}                   {ActiveWebServiceSessions, AllocatedConnections, Caption, ChangeOptionalFeatureOperationsPerSecond...}
Win32_PerfFormattedData_AFDCount... {}                   {Caption, Description, DroppedDatagrams, DroppedDatagramsPersec...}
Win32_PerfRawData_AFDCounters_Mi... {}                   {Caption, Description, DroppedDatagrams, DroppedDatagramsPersec...}
Win32_PerfFormattedData_Authoriz... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_AuthorizationM... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_BITS_BIT... {}                   {BITSDownloadBlockSizeBytes, BITSDownloadResponseIntervalmsec, Caption, Description...}
Win32_PerfRawData_BITS_BITSNetUt... {}                   {BITSDownloadBlockSizeBytes, BITSDownloadResponseIntervalmsec, Caption, Description...}
Win32_PerfFormattedData_Counters... {}                   {AAAAqueriesFailed, AAAAqueriesSuccessful, AAAASynthesizedrecords, Caption...}
Win32_PerfRawData_Counters_DNS64... {}                   {AAAAqueriesFailed, AAAAqueriesSuccessful, AAAASynthesizedrecords, Caption...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_Counters_Event... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Counters... {}                   {BufferMemoryUsageNonPagedPool, BufferMemoryUsagePagedPool, Caption, Description...}
Win32_PerfRawData_Counters_Event... {}                   {BufferMemoryUsageNonPagedPool, BufferMemoryUsagePagedPool, Caption, Description...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, FileSystemBytesRead, FileSystemBytesWritten...}
Win32_PerfRawData_Counters_FileS... {}                   {Caption, Description, FileSystemBytesRead, FileSystemBytesWritten...}
Win32_PerfFormattedData_Counters... {}                   {AuthIPMainModeNegotiationTime, AuthIPQuickModeNegotiationTime, Caption, Description...}
Win32_PerfRawData_Counters_Gener... {}                   {AuthIPMainModeNegotiationTime, AuthIPQuickModeNegotiationTime, Caption, Description...}
Win32_PerfFormattedData_Counters... {}                   {Caption, CurrentUrisCached, Description, Frequency_Object...}
Win32_PerfRawData_Counters_HTTPS... {}                   {Caption, CurrentUrisCached, Description, Frequency_Object...}
Win32_PerfFormattedData_Counters... {}                   {ArrivalRate, CacheHitRate, Caption, CurrentQueueSize...}
Win32_PerfRawData_Counters_HTTPS... {}                   {ArrivalRate, CacheHitRate, Caption, CurrentQueueSize...}
Win32_PerfFormattedData_Counters... {}                   {AllRequests, BytesReceivedRate, BytesSentRate, BytesTransferredRate...}
Win32_PerfRawData_Counters_HTTPS... {}                   {AllRequests, BytesReceivedRate, BytesSentRate, BytesTransferredRate...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_Counters_Hyper... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, DropsNeighborresolutiontimeouts, ErrorsAuthenticationErrors...}
Win32_PerfRawData_Counters_IPHTT... {}                   {Caption, Description, DropsNeighborresolutiontimeouts, ErrorsAuthenticationErrors...}
Win32_PerfFormattedData_Counters... {}                   {Bytesreceivedonthissession, Bytessentonthissession, Caption, Description...}
Win32_PerfRawData_Counters_IPHTT... {}                   {Bytesreceivedonthissession, Bytessentonthissession, Caption, Description...}
Win32_PerfFormattedData_Counters... {}                   {ActiveExtendedModeSAs, ActiveMainModeSAs, ActiveQuickModeSAs, Caption...}
Win32_PerfRawData_Counters_IPsec... {}                   {ActiveExtendedModeSAs, ActiveMainModeSAs, ActiveQuickModeSAs, Caption...}
Win32_PerfFormattedData_Counters... {}                   {ActiveExtendedModeSAs, ActiveMainModeSAs, ActiveQuickModeSAs, Caption...}
Win32_PerfRawData_Counters_IPsec... {}                   {ActiveExtendedModeSAs, ActiveMainModeSAs, ActiveQuickModeSAs, Caption...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_Counters_IPsec... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Counters... {}                   {Caption, CurrentStateEntries, Description, Frequency_Object...}
Win32_PerfRawData_Counters_IPsec... {}                   {Caption, CurrentStateEntries, Description, Frequency_Object...}
Win32_PerfFormattedData_Counters... {}                   {ActiveSecurityAssociations, BytesReceivedinTransportModePersec, BytesReceivedinTunnelModePersec, BytesSentinTransportModePersec...}
Win32_PerfRawData_Counters_IPsec... {}                   {ActiveSecurityAssociations, BytesReceivedinTransportModePersec, BytesReceivedinTunnelModePersec, BytesSentinTransportModePersec...}
Win32_PerfFormattedData_Counters... {}                   {ActiveMainModeSAs, ActiveQuickModeSAs, Caption, Description...}
Win32_PerfRawData_Counters_IPsec... {}                   {ActiveMainModeSAs, ActiveQuickModeSAs, Caption, Description...}
Win32_PerfFormattedData_Counters... {}                   {ActiveMainModeSAs, ActiveQuickModeSAs, Caption, Description...}
Win32_PerfRawData_Counters_IPsec... {}                   {ActiveMainModeSAs, ActiveQuickModeSAs, Caption, Description...}
Win32_PerfFormattedData_Counters... {}                   {ActiveMainModeSAs, ActiveQuickModeSAs, Caption, Description...}
Win32_PerfRawData_Counters_IPsec... {}                   {ActiveMainModeSAs, ActiveQuickModeSAs, Caption, Description...}
Win32_PerfFormattedData_Counters... {}                   {ActiveMainModeSAs, ActiveQuickModeSAs, Caption, Description...}
Win32_PerfRawData_Counters_IPsec... {}                   {ActiveMainModeSAs, ActiveQuickModeSAs, Caption, Description...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, FailedRequests, Frequency_Object...}
Win32_PerfRawData_Counters_KPSSVC   {}                   {Caption, Description, FailedRequests, Frequency_Object...}
Win32_PerfFormattedData_Counters... {}                   {AverageSemaphoreHoldTime, Caption, Description, Frequency_Object...}
Win32_PerfRawData_Counters_Netlogon {}                   {AverageSemaphoreHoldTime, AverageSemaphoreHoldTime_Base, Caption, Description...}
Win32_PerfFormattedData_Counters... {}                   {Bytestransmitted, BytestransmittedPersec, Caption, Description...}
Win32_PerfRawData_Counters_Netwo... {}                   {Bytestransmitted, BytestransmittedPersec, Caption, Description...}
Win32_PerfFormattedData_Counters... {}                   {Averagepacketsinnetcard, Averagepacketsinsequencer, Averagepacketsinshaper, Bytesscheduled...}
Win32_PerfRawData_Counters_Pacer... {}                   {Averagepacketsinnetcard, Averagepacketsinsequencer, Averagepacketsinshaper, Bytesscheduled...}
Win32_PerfFormattedData_Counters... {}                   {Averagepacketsinnetcard, Averagepacketsinsequencer, Averagepacketsinshaper, Caption...}
Win32_PerfRawData_Counters_Pacer... {}                   {Averagepacketsinnetcard, Averagepacketsinsequencer, Averagepacketsinshaper, Caption...}
Win32_PerfFormattedData_Counters... {}                   {BuildScatterGatherCyclesPersec, Caption, Description, Frequency_Object...}
Win32_PerfRawData_Counters_PerPr... {}                   {BuildScatterGatherCyclesPersec, Caption, Description, Frequency_Object...}
Win32_PerfFormattedData_Counters... {}                   {BuildScatterGatherListCallsPersec, Caption, Description, DPCsDeferredPersec...}
Win32_PerfRawData_Counters_PerPr... {}                   {BuildScatterGatherListCallsPersec, Caption, Description, DPCsDeferredPersec...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, DevicePowerState, Frequency_Object...}
Win32_PerfRawData_Counters_Physi... {}                   {Caption, Description, DevicePowerState, Frequency_Object...}
Win32_PerfFormattedData_Counters... {}                   {ActivityHostManagerhostprocessespoolsize, ActivityHostManagerNumberofbusyhostprocesses, ActivityHostManagerNumberofcreatedhostprocesses, Acti...
Win32_PerfRawData_Counters_Power... {}                   {ActivityHostManagerhostprocessespoolsize, ActivityHostManagerNumberofbusyhostprocesses, ActivityHostManagerNumberofcreatedhostprocesses, Acti...
Win32_PerfFormattedData_Counters... {}                   {AverageIdleTime, C1TransitionsPersec, C2TransitionsPersec, C3TransitionsPersec...}
Win32_PerfRawData_Counters_Proce... {}                   {AverageIdleTime, AverageIdleTime_Base, C1TransitionsPersec, C2TransitionsPersec...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_Counters_RDMAA... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Counters... {}                   {AverageEncodingTime, Caption, Description, FrameQuality...}
Win32_PerfRawData_Counters_Remot... {}                   {AverageEncodingTime, Caption, Description, FrameQuality...}
Win32_PerfFormattedData_Counters... {}                   {BaseTCPRTT, BaseUDPRTT, Caption, CurrentTCPBandwidth...}
Win32_PerfRawData_Counters_Remot... {}                   {BaseTCPRTT, BaseUDPRTT, Caption, CurrentTCPBandwidth...}
Win32_PerfFormattedData_Counters... {}                   {AvgBytesPerRead, AvgBytesPerWrite, AvgDataBytesPerRequest, AvgDataQueueLength...}
Win32_PerfRawData_Counters_SMBCl... {}                   {AvgBytesPerRead, AvgBytesPerRead_Base, AvgBytesPerWrite, AvgBytesPerWrite_Base...}
Win32_PerfFormattedData_Counters... {}                   {BytesRDMAReadPersec, BytesRDMAWrittenPersec, BytesReceivedPersec, BytesSentPersec...}
Win32_PerfRawData_Counters_SMBDi... {}                   {BytesRDMAReadPersec, BytesRDMAWrittenPersec, BytesReceivedPersec, BytesSentPersec...}
Win32_PerfFormattedData_Counters... {}                   {AvgBytesPerRead, AvgBytesPerWrite, AvgDataBytesPerRequest, AvgDataQueueLength...}
Win32_PerfRawData_Counters_SMBSe... {}                   {AvgBytesPerRead, AvgBytesPerRead_Base, AvgBytesPerWrite, AvgBytesPerWrite_Base...}
Win32_PerfFormattedData_Counters... {}                   {AvgBytesPerRead, AvgBytesPerWrite, AvgDataBytesPerRequest, AvgDataQueueLength...}
Win32_PerfRawData_Counters_SMBSe... {}                   {AvgBytesPerRead, AvgBytesPerRead_Base, AvgBytesPerWrite, AvgBytesPerWrite_Base...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, ExecResourceAcquiresAcqExclLitePersec, ExecResourceAcquiresAcqShrdLitePersec...}
Win32_PerfRawData_Counters_Synch... {}                   {Caption, Description, ExecResourceAcquiresAcqExclLitePersec, ExecResourceAcquiresAcqShrdLitePersec...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, ExecResourceAcquiresAcqExclLitePersec, ExecResourceAcquiresAcqShrdLitePersec...}
Win32_PerfRawData_Counters_Synch... {}                   {Caption, Description, ExecResourceAcquiresAcqExclLitePersec, ExecResourceAcquiresAcqShrdLitePersec...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_Counters_Tered... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_Counters_Tered... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_Counters_Tered... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_Counters_Therm... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_Counters_WFP      {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Counters... {}                   {ActiveInboundConnections, ActiveOutboundConnections, AllowedClassifiesPersec, BlockedBinds...}
Win32_PerfRawData_Counters_WFPv4    {}                   {ActiveInboundConnections, ActiveOutboundConnections, AllowedClassifiesPersec, BlockedBinds...}
Win32_PerfFormattedData_Counters... {}                   {ActiveInboundConnections, ActiveOutboundConnections, AllowedClassifiesPersec, BlockedBinds...}
Win32_PerfRawData_Counters_WFPv6    {}                   {ActiveInboundConnections, ActiveOutboundConnections, AllowedClassifiesPersec, BlockedBinds...}
Win32_PerfFormattedData_Counters... {}                   {ActiveOperations, ActiveShells, ActiveUsers, Caption...}
Win32_PerfRawData_Counters_WSMan... {}                   {ActiveOperations, ActiveShells, ActiveUsers, Caption...}
Win32_PerfFormattedData_Counters... {}                   {AllocationCount, Caption, Description, FreeCount...}
Win32_PerfRawData_Counters_XHCIC... {}                   {AllocationCount, Caption, Description, FreeCount...}
Win32_PerfFormattedData_Counters... {}                   {Caption, Description, DpcRequeueCount, DPCsPersec...}
Win32_PerfRawData_Counters_XHCII... {}                   {Caption, Description, DpcRequeueCount, DPCsPersec...}
Win32_PerfFormattedData_Counters... {}                   {BytesPerSec, Caption, Description, FailedTransferCount...}
Win32_PerfRawData_Counters_XHCIT... {}                   {BytesPerSec, Caption, Description, FailedTransferCount...}
Win32_PerfFormattedData_DdmCount... {}                   {BytesReceivedByDisconnectedClients, BytesTransmittedByDisconnectedClients, Caption, Description...}
Win32_PerfRawData_DdmCounterProv... {}                   {BytesReceivedByDisconnectedClients, BytesTransmittedByDisconnectedClients, Caption, Description...}
Win32_PerfFormattedData_DFSNServ... {}                   {Caption, Description, FolderCount, Frequency_Object...}
Win32_PerfRawData_DFSNServerServ... {}                   {Caption, Description, FolderCount, Frequency_Object...}
Win32_PerfFormattedData_DFSNServ... {}                   {AvgResponseTime, Caption, Description, Frequency_Object...}
Win32_PerfRawData_DFSNServerServ... {}                   {AvgResponseTime, AvgResponseTime_Base, Caption, Description...}
Win32_PerfFormattedData_DFSNServ... {}                   {AvgResponseTime, Caption, Description, Frequency_Object...}
Win32_PerfRawData_DFSNServerServ... {}                   {AvgResponseTime, AvgResponseTime_Base, Caption, Description...}
Win32_PerfFormattedData_dfsr_DFS... {}                   {BandwidthSavingsUsingDFSReplication, Caption, CompressedSizeofFilesReceived, ConflictBytesCleanedup...}
Win32_PerfRawData_dfsr_DFSReplic... {}                   {BandwidthSavingsUsingDFSReplication, Caption, CompressedSizeofFilesReceived, ConflictBytesCleanedup...}
Win32_PerfFormattedData_dfsr_DFS... {}                   {BandwidthSavingsUsingDFSReplication, BytesReceivedPerSecond, Caption, CompressedSizeofFilesReceived...}
Win32_PerfRawData_dfsr_DFSReplic... {}                   {BandwidthSavingsUsingDFSReplication, BytesReceivedPerSecond, Caption, CompressedSizeofFilesReceived...}
Win32_PerfFormattedData_dfsr_DFS... {}                   {Caption, DatabaseCommits, DatabaseLookups, Description...}
Win32_PerfRawData_dfsr_DFSReplic... {}                   {Caption, DatabaseCommits, DatabaseLookups, Description...}
Win32_PerfFormattedData_Director... {}                   {ABANRPersec, ABBrowsesPersec, ABClientSessions, ABMatchesPersec...}
Win32_PerfRawData_DirectoryServi... {}                   {ABANRPersec, ABBrowsesPersec, ABClientSessions, ABMatchesPersec...}
Win32_PerfFormattedData_DNS_DNS     {}                   {AXFRRequestReceived, AXFRRequestSent, AXFRResponseReceived, AXFRSuccessReceived...}
Win32_PerfRawData_DNS_DNS           {}                   {AXFRRequestReceived, AXFRRequestSent, AXFRResponseReceived, AXFRSuccessReceived...}
Win32_PerfFormattedData_ESENT_Da... {}                   {Caption, DatabaseCacheMemoryCommitted, DatabaseCacheMemoryCommittedMB, DatabaseCacheMemoryReserved...}
Win32_PerfRawData_ESENT_Database    {}                   {Caption, DatabaseCacheMemoryCommitted, DatabaseCacheMemoryCommittedMB, DatabaseCacheMemoryReserved...}
Win32_PerfFormattedData_ESENT_Da... {}                   {Caption, DatabaseCacheMissesPersec, DatabaseCachePercentHit, DatabaseCachePercentHitUncorrelated...}
Win32_PerfRawData_ESENT_Database... {}                   {Caption, DatabaseCacheMissesPersec, DatabaseCachePercentHit, DatabaseCachePercentHit_Base...}
Win32_PerfFormattedData_ESENT_Da... {}                   {Caption, DatabaseCacheMissesPersec, DatabaseCachePercentHit, DatabaseCachePercentHitUncorrelated...}
Win32_PerfRawData_ESENT_Database... {}                   {Caption, DatabaseCacheMissesPersec, DatabaseCachePercentHit, DatabaseCachePercentHit_Base...}
Win32_PerfFormattedData_LocalSes... {}                   {ActiveSessions, Caption, Description, Frequency_Object...}
Win32_PerfRawData_LocalSessionMa... {}                   {ActiveSessions, Caption, Description, Frequency_Object...}
Win32_PerfFormattedData_Lsa_Secu... {}                   {Caption, ContextHandles, CredentialHandles, Description...}
Win32_PerfRawData_Lsa_SecurityPe... {}                   {Caption, ContextHandles, CredentialHandles, Description...}
Win32_PerfFormattedData_Lsa_Secu... {}                   {ActiveSchannelSessionCacheEntries, Caption, Description, DigestAuthentications...}
Win32_PerfRawData_Lsa_SecuritySy... {}                   {ActiveSchannelSessionCacheEntries, Caption, Description, DigestAuthentications...}
Win32_PerfFormattedData_MSDTC_Di... {}                   {AbortedTransactions, AbortedTransactionsPersec, ActiveTransactions, ActiveTransactionsMaximum...}
Win32_PerfRawData_MSDTC_Distribu... {}                   {AbortedTransactions, AbortedTransactionsPersec, ActiveTransactions, ActiveTransactionsMaximum...}
Win32_PerfFormattedData_MSDTCBri... {}                   {Averageparticipantcommitresponsetime, Averageparticipantprepareresponsetime, Caption, CommitretrycountPersec...}
Win32_PerfRawData_MSDTCBridge400... {}                   {Averageparticipantcommitresponsetime, Averageparticipantcommitresponsetime_Base, Averageparticipantprepareresponsetime, Averageparticipantpre...
Win32_PerfFormattedData_NETCLRDa... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_NETCLRData_NET... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_NETCLRNe... {}                   {BytesReceived, BytesSent, Caption, ConnectionsEstablished...}
Win32_PerfRawData_NETCLRNetworki... {}                   {BytesReceived, BytesSent, Caption, ConnectionsEstablished...}
Win32_PerfFormattedData_NETCLRNe... {}                   {BytesReceived, BytesSent, Caption, ConnectionsEstablished...}
Win32_PerfRawData_NETCLRNetworki... {}                   {BytesReceived, BytesSent, Caption, ConnectionsEstablished...}
Win32_PerfFormattedData_NETDataP... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_NETDataProvide... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_NETDataP... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_NETDataProvide... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_NETFrame... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_NETFramework_N... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_NETFrame... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_NETFramework_N... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_NETFrame... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_NETFramework_N... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_NETFrame... {}                   {AssemblySearchLength, BytesinLoaderHeap, Caption, Currentappdomains...}
Win32_PerfRawData_NETFramework_N... {}                   {AssemblySearchLength, BytesinLoaderHeap, Caption, Currentappdomains...}
Win32_PerfFormattedData_NETFrame... {}                   {Caption, ContentionRatePersec, CurrentQueueLength, Description...}
Win32_PerfRawData_NETFramework_N... {}                   {Caption, ContentionRatePersec, CurrentQueueLength, Description...}
Win32_PerfFormattedData_NETFrame... {}                   {AllocatedBytesPersec, Caption, Description, FinalizationSurvivors...}
Win32_PerfRawData_NETFramework_N... {}                   {AllocatedBytesPersec, Caption, Description, FinalizationSurvivors...}
Win32_PerfFormattedData_NETFrame... {}                   {Caption, Channels, ContextBoundClassesLoaded, ContextBoundObjectsAllocPersec...}
Win32_PerfRawData_NETFramework_N... {}                   {Caption, Channels, ContextBoundClassesLoaded, ContextBoundObjectsAllocPersec...}
Win32_PerfFormattedData_NETFrame... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_NETFramework_N... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_NETMemor... {}                   {CacheEntries, CacheHitRatio, CacheHits, CacheMisses...}
Win32_PerfRawData_NETMemoryCache... {}                   {CacheEntries, CacheHitRatio, CacheHitRatio_Base, CacheHits...}
Win32_PerfFormattedData_NTDS_NTDS   {}                   {ABANRPersec, ABBrowsesPersec, ABClientSessions, ABMatchesPersec...}
Win32_PerfRawData_NTDS_NTDS         {}                   {ABANRPersec, ABBrowsesPersec, ABClientSessions, ABMatchesPersec...}
Win32_PerfFormattedData_PerfDisk... {}                   {AvgDiskBytesPerRead, AvgDiskBytesPerTransfer, AvgDiskBytesPerWrite, AvgDiskQueueLength...}
Win32_PerfRawData_PerfDisk_Logic... {}                   {AvgDiskBytesPerRead, AvgDiskBytesPerRead_Base, AvgDiskBytesPerTransfer, AvgDiskBytesPerTransfer_Base...}
Win32_PerfFormattedData_PerfDisk... {}                   {AvgDiskBytesPerRead, AvgDiskBytesPerTransfer, AvgDiskBytesPerWrite, AvgDiskQueueLength...}
Win32_PerfRawData_PerfDisk_Physi... {}                   {AvgDiskBytesPerRead, AvgDiskBytesPerRead_Base, AvgDiskBytesPerTransfer, AvgDiskBytesPerTransfer_Base...}
Win32_PerfFormattedData_PerfNet_... {}                   {AnnouncementsDomainPersec, AnnouncementsServerPersec, AnnouncementsTotalPersec, Caption...}
Win32_PerfRawData_PerfNet_Browser   {}                   {AnnouncementsDomainPersec, AnnouncementsServerPersec, AnnouncementsTotalPersec, Caption...}
Win32_PerfFormattedData_PerfNet_... {}                   {BytesReceivedPersec, BytesTotalPersec, BytesTransmittedPersec, Caption...}
Win32_PerfRawData_PerfNet_Redire... {}                   {BytesReceivedPersec, BytesTotalPersec, BytesTransmittedPersec, Caption...}
Win32_PerfFormattedData_PerfNet_... {}                   {BlockingRequestsRejected, BytesReceivedPersec, BytesTotalPersec, BytesTransmittedPersec...}
Win32_PerfRawData_PerfNet_Server    {}                   {BlockingRequestsRejected, BytesReceivedPersec, BytesTotalPersec, BytesTransmittedPersec...}
Win32_PerfFormattedData_PerfNet_... {}                   {ActiveThreads, AvailableThreads, AvailableWorkItems, BorrowedWorkItems...}
Win32_PerfRawData_PerfNet_Server... {}                   {ActiveThreads, AvailableThreads, AvailableWorkItems, BorrowedWorkItems...}
Win32_PerfFormattedData_PerfOS_C... {}                   {AsyncCopyReadsPersec, AsyncDataMapsPersec, AsyncFastReadsPersec, AsyncMDLReadsPersec...}
Win32_PerfRawData_PerfOS_Cache      {}                   {AsyncCopyReadsPersec, AsyncDataMapsPersec, AsyncFastReadsPersec, AsyncMDLReadsPersec...}
Win32_PerfFormattedData_PerfOS_M... {}                   {AvailableBytes, AvailableKBytes, AvailableMBytes, CacheBytes...}
Win32_PerfRawData_PerfOS_Memory     {}                   {AvailableBytes, AvailableKBytes, AvailableMBytes, CacheBytes...}
Win32_PerfFormattedData_PerfOS_N... {}                   {AvailableMBytes, Caption, Description, FreeAndZeroPageListMBytes...}
Win32_PerfRawData_PerfOS_NUMANod... {}                   {AvailableMBytes, Caption, Description, FreeAndZeroPageListMBytes...}
Win32_PerfFormattedData_PerfOS_O... {}                   {Caption, Description, Events, Frequency_Object...}
Win32_PerfRawData_PerfOS_Objects    {}                   {Caption, Description, Events, Frequency_Object...}
Win32_PerfFormattedData_PerfOS_P... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_PerfOS_PagingFile {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_PerfOS_P... {}                   {C1TransitionsPersec, C2TransitionsPersec, C3TransitionsPersec, Caption...}
Win32_PerfRawData_PerfOS_Processor  {}                   {C1TransitionsPersec, C2TransitionsPersec, C3TransitionsPersec, Caption...}
Win32_PerfFormattedData_PerfOS_S... {}                   {AlignmentFixupsPersec, Caption, ContextSwitchesPersec, Description...}
Win32_PerfRawData_PerfOS_System     {}                   {AlignmentFixupsPersec, Caption, ContextSwitchesPersec, Description...}
Win32_PerfFormattedData_PerfProc... {}                   {Caption, Description, ExecReadOnly, ExecReadPerWrite...}
Win32_PerfRawData_PerfProc_FullI... {}                   {Caption, Description, ExecReadOnly, ExecReadPerWrite...}
Win32_PerfFormattedData_PerfProc... {}                   {Caption, Description, ExecReadOnly, ExecReadPerWrite...}
Win32_PerfRawData_PerfProc_Image... {}                   {Caption, Description, ExecReadOnly, ExecReadPerWrite...}
Win32_PerfFormattedData_PerfProc... {}                   {Caption, CurrentPercentKernelModeTime, CurrentPercentProcessorTime, CurrentPercentUserModeTime...}
Win32_PerfRawData_PerfProc_JobOb... {}                   {Caption, CurrentPercentKernelModeTime, CurrentPercentProcessorTime, CurrentPercentUserModeTime...}
Win32_PerfFormattedData_PerfProc... {}                   {Caption, CreatingProcessID, Description, ElapsedTime...}
Win32_PerfRawData_PerfProc_JobOb... {}                   {Caption, CreatingProcessID, Description, ElapsedTime...}
Win32_PerfFormattedData_PerfProc... {}                   {Caption, CreatingProcessID, Description, ElapsedTime...}
Win32_PerfRawData_PerfProc_Process  {}                   {Caption, CreatingProcessID, Description, ElapsedTime...}
Win32_PerfFormattedData_PerfProc... {}                   {BytesFree, BytesImageFree, BytesImageReserved, BytesReserved...}
Win32_PerfRawData_PerfProc_Proce... {}                   {BytesFree, BytesImageFree, BytesImageReserved, BytesReserved...}
Win32_PerfFormattedData_PerfProc... {}                   {Caption, ContextSwitchesPersec, Description, ElapsedTime...}
Win32_PerfRawData_PerfProc_Thread   {}                   {Caption, ContextSwitchesPersec, Description, ElapsedTime...}
Win32_PerfFormattedData_PerfProc... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_PerfProc_Threa... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_PowerMet... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_PowerMeterCoun... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_RemoteAc... {}                   {AlignmentErrors, BufferOverrunErrors, BytesReceived, BytesReceivedPerSec...}
Win32_PerfRawData_RemoteAccess_R... {}                   {AlignmentErrors, BufferOverrunErrors, BytesReceived, BytesReceivedPerSec...}
Win32_PerfFormattedData_RemoteAc... {}                   {AlignmentErrors, BufferOverrunErrors, BytesReceived, BytesReceivedPerSec...}
Win32_PerfRawData_RemoteAccess_R... {}                   {AlignmentErrors, BufferOverrunErrors, BytesReceived, BytesReceivedPerSec...}
Win32_PerfFormattedData_ServiceM... {}                   {Calls, CallsDuration, CallsFailed, CallsFailedPerSecond...}
Win32_PerfRawData_ServiceModel40... {}                   {Calls, CallsDuration, CallsDuration_Base, CallsFailed...}
Win32_PerfFormattedData_ServiceM... {}                   {CallFailedPerSecond, Calls, CallsDuration, CallsFailed...}
Win32_PerfRawData_ServiceModel40... {}                   {CallFailedPerSecond, Calls, CallsDuration, CallsDuration_Base...}
Win32_PerfFormattedData_ServiceM... {}                   {Calls, CallsDuration, CallsFailed, CallsFailedPerSecond...}
Win32_PerfRawData_ServiceModel40... {}                   {Calls, CallsDuration, CallsDuration_Base, CallsFailed...}
Win32_PerfFormattedData_SMSvcHos... {}                   {Caption, ConnectionsAcceptedovernetpipe, ConnectionsAcceptedovernettcp, ConnectionsDispatchedovernetpipe...}
Win32_PerfRawData_SMSvcHost4000_... {}                   {Caption, ConnectionsAcceptedovernetpipe, ConnectionsAcceptedovernettcp, ConnectionsDispatchedovernetpipe...}
Win32_PerfFormattedData_Spooler_... {}                   {AddNetworkPrinterCalls, BytesPrintedPersec, Caption, Description...}
Win32_PerfRawData_Spooler_PrintQ... {}                   {AddNetworkPrinterCalls, BytesPrintedPersec, Caption, Description...}
Win32_PerfFormattedData_TapiSrv_... {}                   {ActiveLines, ActiveTelephones, Caption, ClientApps...}
Win32_PerfRawData_TapiSrv_Telephony {}                   {ActiveLines, ActiveTelephones, Caption, ClientApps...}
Win32_PerfFormattedData_Tcpip_ICMP  {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_Tcpip_ICMP        {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Tcpip_IC... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_Tcpip_ICMPv6      {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Tcpip_IPv4  {}                   {Caption, DatagramsForwardedPersec, DatagramsOutboundDiscarded, DatagramsOutboundNoRoute...}
Win32_PerfRawData_Tcpip_IPv4        {}                   {Caption, DatagramsForwardedPersec, DatagramsOutboundDiscarded, DatagramsOutboundNoRoute...}
Win32_PerfFormattedData_Tcpip_IPv6  {}                   {Caption, DatagramsForwardedPersec, DatagramsOutboundDiscarded, DatagramsOutboundNoRoute...}
Win32_PerfRawData_Tcpip_IPv6        {}                   {Caption, DatagramsForwardedPersec, DatagramsOutboundDiscarded, DatagramsOutboundNoRoute...}
Win32_PerfFormattedData_Tcpip_NB... {}                   {BytesReceivedPersec, BytesSentPersec, BytesTotalPersec, Caption...}
Win32_PerfRawData_Tcpip_NBTConne... {}                   {BytesReceivedPersec, BytesSentPersec, BytesTotalPersec, Caption...}
Win32_PerfFormattedData_Tcpip_Ne... {}                   {BytesReceivedPersec, BytesSentPersec, BytesTotalPersec, Caption...}
Win32_PerfRawData_Tcpip_NetworkA... {}                   {BytesReceivedPersec, BytesSentPersec, BytesTotalPersec, Caption...}
Win32_PerfFormattedData_Tcpip_Ne... {}                   {BytesReceivedPersec, BytesSentPersec, BytesTotalPersec, Caption...}
Win32_PerfRawData_Tcpip_NetworkI... {}                   {BytesReceivedPersec, BytesSentPersec, BytesTotalPersec, Caption...}
Win32_PerfFormattedData_Tcpip_TCPv4 {}                   {Caption, ConnectionFailures, ConnectionsActive, ConnectionsEstablished...}
Win32_PerfRawData_Tcpip_TCPv4       {}                   {Caption, ConnectionFailures, ConnectionsActive, ConnectionsEstablished...}
Win32_PerfFormattedData_Tcpip_TCPv6 {}                   {Caption, ConnectionFailures, ConnectionsActive, ConnectionsEstablished...}
Win32_PerfRawData_Tcpip_TCPv6       {}                   {Caption, ConnectionFailures, ConnectionsActive, ConnectionsEstablished...}
Win32_PerfFormattedData_Tcpip_UDPv4 {}                   {Caption, DatagramsNoPortPersec, DatagramsPersec, DatagramsReceivedErrors...}
Win32_PerfRawData_Tcpip_UDPv4       {}                   {Caption, DatagramsNoPortPersec, DatagramsPersec, DatagramsReceivedErrors...}
Win32_PerfFormattedData_Tcpip_UDPv6 {}                   {Caption, DatagramsNoPortPersec, DatagramsPersec, DatagramsReceivedErrors...}
Win32_PerfRawData_Tcpip_UDPv6       {}                   {Caption, DatagramsNoPortPersec, DatagramsPersec, DatagramsReceivedErrors...}
Win32_PerfFormattedData_TCPIPCou... {}                   {Caption, Deniedconnectorsendrequestsinlowpowermode, Description, Frequency_Object...}
Win32_PerfRawData_TCPIPCounters_... {}                   {Caption, Deniedconnectorsendrequestsinlowpowermode, Description, Frequency_Object...}
Win32_PerfFormattedData_TermServ... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_TermService_Te... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_usbhub_USB  {}                   {AvgBytesPerTransfer, AvgmslatencyforISOtransfers, BulkBytesPerSec, Caption...}
Win32_PerfRawData_usbhub_USB        {}                   {AvgBytesPerTransfer, AvgBytesPerTransfer_Base, AvgmslatencyforISOtransfers, AvgmslatencyforISOtransfers_Base...}
Win32_PerfFormattedData_WindowsW... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_WindowsWorkflo... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_WinNatCo... {}                   {Caption, CurrentSessionCount, Description, DroppedICMPerrorpackets...}
Win32_PerfRawData_WinNatCounters... {}                   {Caption, CurrentSessionCount, Description, DroppedICMPerrorpackets...}
Win32_PerfFormattedData_WinNatCo... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_WinNatCounters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_WinNatCo... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_WinNatCounters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_WinNatCo... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_WinNatCounters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_WinNatCo... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfRawData_WinNatCounters... {}                   {Caption, Description, Frequency_Object, Frequency_PerfTime...}
Win32_PerfFormattedData_Workflow... {}                   {AverageWorkflowLoadTime, AverageWorkflowPersistTime, Caption, Description...}
Win32_PerfRawData_WorkflowServic... {}                   {AverageWorkflowLoadTime, AverageWorkflowLoadTime_Base, AverageWorkflowPersistTime, AverageWorkflowPersistTime_Base...}

PS C:\Users\Administrator>
```

```PowerShell
PS C:\Users\Administrator> Get-WmiObject -Class Win32_process

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
KernelModeTime             : 152086718750
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
HandleCount                : 808
InstallDate                :
KernelModeTime             : 478281250
MaximumWorkingSetSize      :
MinimumWorkingSetSize      :
Name                       : System
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 3337
OtherTransferCount         : 131409
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
WriteOperationCount        : 13027
WriteTransferCount         : 206413624
PSComputerName             : WIN-2012-DC
ProcessName                : System
Handles                    : 808
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
HandleCount                : 180
InstallDate                :
KernelModeTime             : 5000000
MaximumWorkingSetSize      :
MinimumWorkingSetSize      :
Name                       : csrss.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 14627
OtherTransferCount         : 839996
PageFaults                 : 2986
PageFileUsage              : 1552
ParentProcessId            : 284
PeakPageFileUsage          : 1552
PeakVirtualSize            : 45264896
PeakWorkingSetSize         : 3352
Priority                   : 13
PrivatePageCount           : 1589248
ProcessId                  : 292
QuotaNonPagedPoolUsage     : 11
QuotaPagedPoolUsage        : 116
QuotaPeakNonPagedPoolUsage : 13
QuotaPeakPagedPoolUsage    : 122
ReadOperationCount         : 64
ReadTransferCount          : 55340
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 8
UserModeTime               : 781250
VirtualSize                : 44339200
WindowsVersion             : 6.3.9600
WorkingSetSize             : 1380352
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : csrss.exe
Handles                    : 180
VM                         : 44339200
WS                         : 1380352
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
OtherOperationCount        : 3137
OtherTransferCount         : 69162
PageFaults                 : 64988
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
ReadOperationCount         : 33315
ReadTransferCount          : 1039202
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 10
UserModeTime               : 312500
VirtualSize                : 71077888
WindowsVersion             : 6.3.9600
WorkingSetSize             : 23592960
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : csrss.exe
Handles                    : 185
VM                         : 71077888
WS                         : 23592960
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
OtherOperationCount        : 1203
OtherTransferCount         : 144580
PageFaults                 : 9367
PageFileUsage              : 1200
ParentProcessId            : 336
PeakPageFileUsage          : 2624
PeakVirtualSize            : 59760640
PeakWorkingSetSize         : 8708
Priority                   : 13
PrivatePageCount           : 1228800
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
WorkingSetSize             : 8896512
WriteOperationCount        : 1
WriteTransferCount         : 160
PSComputerName             : WIN-2012-DC
ProcessName                : winlogon.exe
Handles                    : 156
VM                         : 58621952
WS                         : 8896512
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
HandleCount                : 227
InstallDate                :
KernelModeTime             : 2187500
MaximumWorkingSetSize      :
MinimumWorkingSetSize      :
Name                       : services.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 2885
OtherTransferCount         : 64186
PageFaults                 : 4054
PageFileUsage              : 2156
ParentProcessId            : 352
PeakPageFileUsage          : 2920
PeakVirtualSize            : 29523968
PeakWorkingSetSize         : 5740
Priority                   : 9
PrivatePageCount           : 2207744
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
WorkingSetSize             : 2891776
WriteOperationCount        : 1
WriteTransferCount         : 160
PSComputerName             : WIN-2012-DC
ProcessName                : services.exe
Handles                    : 227
VM                         : 21508096
WS                         : 2891776
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
HandleCount                : 1276
InstallDate                :
KernelModeTime             : 59062500
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : lsass.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 42608
OtherTransferCount         : 4026319
PageFaults                 : 38862
PageFileUsage              : 37588
ParentProcessId            : 352
PeakPageFileUsage          : 64580
PeakVirtualSize            : 1225867264
PeakWorkingSetSize         : 66640
Priority                   : 9
PrivatePageCount           : 38490112
ProcessId                  : 448
QuotaNonPagedPoolUsage     : 123
QuotaPagedPoolUsage        : 181
QuotaPeakNonPagedPoolUsage : 148
QuotaPeakPagedPoolUsage    : 187
ReadOperationCount         : 7663
ReadTransferCount          : 73721023
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 27
UserModeTime               : 37656250
VirtualSize                : 1202966528
WindowsVersion             : 6.3.9600
WorkingSetSize             : 27443200
WriteOperationCount        : 1182
WriteTransferCount         : 1727779
PSComputerName             : WIN-2012-DC
ProcessName                : lsass.exe
Handles                    : 1276
VM                         : 1202966528
WS                         : 27443200
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
HandleCount                : 367
InstallDate                :
KernelModeTime             : 1562500
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 532
OtherTransferCount         : 22332
PageFaults                 : 5374
PageFileUsage              : 3224
ParentProcessId            : 440
PeakPageFileUsage          : 8228
PeakVirtualSize            : 50991104
PeakWorkingSetSize         : 12264
Priority                   : 8
PrivatePageCount           : 3301376
ProcessId                  : 572
QuotaNonPagedPoolUsage     : 15
QuotaPagedPoolUsage        : 173
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
WorkingSetSize             : 6938624
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : svchost.exe
Handles                    : 367
VM                         : 47263744
WS                         : 6938624
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
HandleCount                : 356
InstallDate                :
KernelModeTime             : 6093750
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 1409
OtherTransferCount         : 68138
PageFaults                 : 4600
PageFileUsage              : 3216
ParentProcessId            : 440
PeakPageFileUsage          : 4380
PeakVirtualSize            : 32124928
PeakWorkingSetSize         : 7540
Priority                   : 8
PrivatePageCount           : 3293184
ProcessId                  : 600
QuotaNonPagedPoolUsage     : 19
QuotaPagedPoolUsage        : 69
QuotaPeakNonPagedPoolUsage : 26
QuotaPeakPagedPoolUsage    : 71
ReadOperationCount         : 0
ReadTransferCount          : 0
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 9
UserModeTime               : 10312500
VirtualSize                : 28418048
WindowsVersion             : 6.3.9600
WorkingSetSize             : 3805184
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : svchost.exe
Handles                    : 356
VM                         : 28418048
WS                         : 3805184
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
KernelModeTime             : 6562500
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : dwm.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 270
OtherTransferCount         : 1874
PageFaults                 : 134538
PageFileUsage              : 25236
ParentProcessId            : 380
PeakPageFileUsage          : 27916
PeakVirtualSize            : 151556096
PeakWorkingSetSize         : 64424
Priority                   : 13
PrivatePageCount           : 25841664
ProcessId                  : 716
QuotaNonPagedPoolUsage     : 18
QuotaPagedPoolUsage        : 249
QuotaPeakNonPagedPoolUsage : 20
QuotaPeakPagedPoolUsage    : 285
ReadOperationCount         : 1
ReadTransferCount          : 60
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 7
UserModeTime               : 6250000
VirtualSize                : 135200768
WindowsVersion             : 6.3.9600
WorkingSetSize             : 48685056
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : dwm.exe
Handles                    : 174
VM                         : 135200768
WS                         : 48685056
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
KernelModeTime             : 3437500
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : VBoxService.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 360692
OtherTransferCount         : 9815652
PageFaults                 : 65824
PageFileUsage              : 1880
ParentProcessId            : 440
PeakPageFileUsage          : 1972
PeakVirtualSize            : 60723200
PeakWorkingSetSize         : 4924
Priority                   : 8
PrivatePageCount           : 1925120
ProcessId                  : 744
QuotaNonPagedPoolUsage     : 10
QuotaPagedPoolUsage        : 98
QuotaPeakNonPagedPoolUsage : 11
QuotaPeakPagedPoolUsage    : 99
ReadOperationCount         : 1339
ReadTransferCount          : 5356
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 10
UserModeTime               : 156250
VirtualSize                : 59535360
WindowsVersion             : 6.3.9600
WorkingSetSize             : 2777088
WriteOperationCount        : 1339
WriteTransferCount         : 21424
PSComputerName             : WIN-2012-DC
ProcessName                : VBoxService.exe
Handles                    : 138
VM                         : 59535360
WS                         : 2777088
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
HandleCount                : 470
InstallDate                :
KernelModeTime             : 2343750
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 9748
OtherTransferCount         : 195486
PageFaults                 : 14264
PageFileUsage              : 11492
ParentProcessId            : 440
PeakPageFileUsage          : 12628
PeakVirtualSize            : 417185792
PeakWorkingSetSize         : 18704
Priority                   : 8
PrivatePageCount           : 11767808
ProcessId                  : 828
QuotaNonPagedPoolUsage     : 21
QuotaPagedPoolUsage        : 100
QuotaPeakNonPagedPoolUsage : 90
QuotaPeakPagedPoolUsage    : 775
ReadOperationCount         : 571
ReadTransferCount          : 18125696
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 14
UserModeTime               : 3750000
VirtualSize                : 62521344
WindowsVersion             : 6.3.9600
WorkingSetSize             : 10477568
WriteOperationCount        : 1612
WriteTransferCount         : 21053256
PSComputerName             : WIN-2012-DC
ProcessName                : svchost.exe
Handles                    : 470
VM                         : 62521344
WS                         : 10477568
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
HandleCount                : 1485
InstallDate                :
KernelModeTime             : 1415468750
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 16223299
OtherTransferCount         : 4483312296
PageFaults                 : 7083952
PageFileUsage              : 38180
ParentProcessId            : 440
PeakPageFileUsage          : 529172
PeakVirtualSize            : 1013297152
PeakWorkingSetSize         : 503340
Priority                   : 8
PrivatePageCount           : 39096320
ProcessId                  : 868
QuotaNonPagedPoolUsage     : 55
QuotaPagedPoolUsage        : 308
QuotaPeakNonPagedPoolUsage : 1411
QuotaPeakPagedPoolUsage    : 545
ReadOperationCount         : 635856
ReadTransferCount          : 4894533179
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 37
UserModeTime               : 2435000000
VirtualSize                : 701550592
WindowsVersion             : 6.3.9600
WorkingSetSize             : 39227392
WriteOperationCount        : 66889
WriteTransferCount         : 6173042829
PSComputerName             : WIN-2012-DC
ProcessName                : svchost.exe
Handles                    : 1485
VM                         : 701550592
WS                         : 39227392
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
HandleCount                : 437
InstallDate                :
KernelModeTime             : 937500
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 6327
OtherTransferCount         : 354042
PageFaults                 : 4821
PageFileUsage              : 4896
ParentProcessId            : 440
PeakPageFileUsage          : 5260
PeakVirtualSize            : 85487616
PeakWorkingSetSize         : 10468
Priority                   : 8
PrivatePageCount           : 5013504
ProcessId                  : 916
QuotaNonPagedPoolUsage     : 25
QuotaPagedPoolUsage        : 171
QuotaPeakNonPagedPoolUsage : 31
QuotaPeakPagedPoolUsage    : 178
ReadOperationCount         : 57
ReadTransferCount          : 7766
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 16
UserModeTime               : 1718750
VirtualSize                : 81354752
WindowsVersion             : 6.3.9600
WorkingSetSize             : 6328320
WriteOperationCount        : 12
WriteTransferCount         : 996
PSComputerName             : WIN-2012-DC
ProcessName                : svchost.exe
Handles                    : 437
VM                         : 81354752
WS                         : 6328320
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
HandleCount                : 752
InstallDate                :
KernelModeTime             : 27031250
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 95839
OtherTransferCount         : 6023602
PageFaults                 : 68229
PageFileUsage              : 10644
ParentProcessId            : 440
PeakPageFileUsage          : 28680
PeakVirtualSize            : 1432371200
PeakWorkingSetSize         : 37824
Priority                   : 8
PrivatePageCount           : 10899456
ProcessId                  : 976
QuotaNonPagedPoolUsage     : 60
QuotaPagedPoolUsage        : 199
QuotaPeakNonPagedPoolUsage : 635
QuotaPeakPagedPoolUsage    : 681
ReadOperationCount         : 2841
ReadTransferCount          : 24656487
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 18
UserModeTime               : 20781250
VirtualSize                : 1193250816
WindowsVersion             : 6.3.9600
WorkingSetSize             : 10711040
WriteOperationCount        : 47699
WriteTransferCount         : 240781127
PSComputerName             : WIN-2012-DC
ProcessName                : svchost.exe
Handles                    : 752
VM                         : 1193250816
WS                         : 10711040
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
HandleCount                : 372
InstallDate                :
KernelModeTime             : 312500
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 3442
OtherTransferCount         : 148426
PageFaults                 : 8106
PageFileUsage              : 6340
ParentProcessId            : 440
PeakPageFileUsage          : 6732
PeakVirtualSize            : 51179520
PeakWorkingSetSize         : 10496
Priority                   : 8
PrivatePageCount           : 6492160
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
ThreadCount                : 18
UserModeTime               : 1718750
VirtualSize                : 50114560
WindowsVersion             : 6.3.9600
WorkingSetSize             : 4313088
WriteOperationCount        : 1
WriteTransferCount         : 32768
PSComputerName             : WIN-2012-DC
ProcessName                : svchost.exe
Handles                    : 372
VM                         : 50114560
WS                         : 4313088
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
HandleCount                : 372
InstallDate                :
KernelModeTime             : 468750
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : spoolsv.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 856
OtherTransferCount         : 33608
PageFaults                 : 3104
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
WorkingSetSize             : 2629632
WriteOperationCount        : 2
WriteTransferCount         : 320
PSComputerName             : WIN-2012-DC
ProcessName                : spoolsv.exe
Handles                    : 372
VM                         : 72437760
WS                         : 2629632
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
HandleCount                : 347
InstallDate                :
KernelModeTime             : 1718750
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : Microsoft.ActiveDirectory.WebServices.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 15655
OtherTransferCount         : 520054
PageFaults                 : 33220
PageFileUsage              : 30536
ParentProcessId            : 440
PeakPageFileUsage          : 33404
PeakVirtualSize            : 595652608
PeakWorkingSetSize         : 40372
Priority                   : 8
PrivatePageCount           : 31268864
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
ThreadCount                : 10
UserModeTime               : 4218750
VirtualSize                : 592752640
WindowsVersion             : 6.3.9600
WorkingSetSize             : 7741440
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : Microsoft.ActiveDirectory.WebServices.exe
Handles                    : 347
VM                         : 592752640
WS                         : 7741440
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
HandleCount                : 335
InstallDate                :
KernelModeTime             : 80781250
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : dfsrs.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 1123795
OtherTransferCount         : 204591110
PageFaults                 : 22967
PageFileUsage              : 14024
ParentProcessId            : 440
PeakPageFileUsage          : 16580
PeakVirtualSize            : 634163200
PeakWorkingSetSize         : 20244
Priority                   : 8
PrivatePageCount           : 14360576
ProcessId                  : 1408
QuotaNonPagedPoolUsage     : 32
QuotaPagedPoolUsage        : 125
QuotaPeakNonPagedPoolUsage : 35
QuotaPeakPagedPoolUsage    : 125
ReadOperationCount         : 1814
ReadTransferCount          : 11538526
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 15
UserModeTime               : 166406250
VirtualSize                : 632041472
WindowsVersion             : 6.3.9600
WorkingSetSize             : 8839168
WriteOperationCount        : 5850
WriteTransferCount         : 96397765
PSComputerName             : WIN-2012-DC
ProcessName                : dfsrs.exe
Handles                    : 335
VM                         : 632041472
WS                         : 8839168
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
HandleCount                : 10284
InstallDate                :
KernelModeTime             : 5156250
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : dns.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 49639
OtherTransferCount         : 1110789
PageFaults                 : 28714
PageFileUsage              : 88328
ParentProcessId            : 440
PeakPageFileUsage          : 89316
PeakVirtualSize            : 147890176
PeakWorkingSetSize         : 87164
Priority                   : 8
PrivatePageCount           : 90447872
ProcessId                  : 1508
QuotaNonPagedPoolUsage     : 10076
QuotaPagedPoolUsage        : 1262
QuotaPeakNonPagedPoolUsage : 10295
QuotaPeakPagedPoolUsage    : 1264
ReadOperationCount         : 57
ReadTransferCount          : 6612
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 12
UserModeTime               : 2343750
VirtualSize                : 145772544
WindowsVersion             : 6.3.9600
WorkingSetSize             : 6610944
WriteOperationCount        : 60
WriteTransferCount         : 9120
PSComputerName             : WIN-2012-DC
ProcessName                : dns.exe
Handles                    : 10284
VM                         : 145772544
WS                         : 6610944
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
OtherOperationCount        : 337
OtherTransferCount         : 6006
PageFaults                 : 1422
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
OtherOperationCount        : 47
OtherTransferCount         : 178
PageFaults                 : 1068
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
WriteOperationCount        : 42
WriteTransferCount         : 1080
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
HandleCount                : 129
InstallDate                :
KernelModeTime             : 156250
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : dfssvc.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 421
OtherTransferCount         : 10160
PageFaults                 : 2123
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
WorkingSetSize             : 2871296
WriteOperationCount        : 14
WriteTransferCount         : 6034
PSComputerName             : WIN-2012-DC
ProcessName                : dfssvc.exe
Handles                    : 129
VM                         : 30593024
WS                         : 2871296
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
PageFaults                 : 2770
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
WorkingSetSize             : 512000
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : vds.exe
Handles                    : 158
VM                         : 45608960
WS                         : 512000
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
OtherOperationCount        : 261
OtherTransferCount         : 808
PageFaults                 : 3772
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
WorkingSetSize             : 2723840
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : svchost.exe
Handles                    : 401
VM                         : 75804672
WS                         : 2723840
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
KernelModeTime             : 1250000
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : svchost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 1377
OtherTransferCount         : 71686
PageFaults                 : 1988
PageFileUsage              : 1004
ParentProcessId            : 440
PeakPageFileUsage          : 1204
PeakVirtualSize            : 22446080
PeakWorkingSetSize         : 4368
Priority                   : 8
PrivatePageCount           : 1028096
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
UserModeTime               : 156250
VirtualSize                : 21381120
WindowsVersion             : 6.3.9600
WorkingSetSize             : 1564672
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : svchost.exe
Handles                    : 107
VM                         : 21381120
WS                         : 1564672
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
OtherOperationCount        : 1484
OtherTransferCount         : 33964
PageFaults                 : 6573
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
ReadOperationCount         : 308
ReadTransferCount          : 12500992
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 8
UserModeTime               : 0
VirtualSize                : 628494336
WindowsVersion             : 6.3.9600
WorkingSetSize             : 3321856
WriteOperationCount        : 296
WriteTransferCount         : 1810432
PSComputerName             : WIN-2012-DC
ProcessName                : svchost.exe
Handles                    : 261
VM                         : 628494336
WS                         : 3321856
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
OtherOperationCount        : 745
OtherTransferCount         : 10612
PageFaults                 : 2471
PageFileUsage              : 2676
ParentProcessId            : 868
PeakPageFileUsage          : 3172
PeakVirtualSize            : 232296448
PeakWorkingSetSize         : 7600
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
WorkingSetSize             : 7581696
WriteOperationCount        : 43
WriteTransferCount         : 835584
PSComputerName             : WIN-2012-DC
ProcessName                : taskhostex.exe
Handles                    : 195
VM                         : 230174720
WS                         : 7581696
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
HandleCount                : 1199
InstallDate                :
KernelModeTime             : 166875000
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : explorer.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 37916
OtherTransferCount         : 959574
PageFaults                 : 147573
PageFileUsage              : 36700
ParentProcessId            : 1860
PeakPageFileUsage          : 48264
PeakVirtualSize            : 588001280
PeakWorkingSetSize         : 91248
Priority                   : 8
PrivatePageCount           : 37580800
ProcessId                  : 1188
QuotaNonPagedPoolUsage     : 66
QuotaPagedPoolUsage        : 1044
QuotaPeakNonPagedPoolUsage : 95
QuotaPeakPagedPoolUsage    : 1189
ReadOperationCount         : 2784
ReadTransferCount          : 3005114
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 39
UserModeTime               : 78437500
VirtualSize                : 507023360
WindowsVersion             : 6.3.9600
WorkingSetSize             : 74444800
WriteOperationCount        : 151
WriteTransferCount         : 25552
PSComputerName             : WIN-2012-DC
ProcessName                : explorer.exe
Handles                    : 1199
VM                         : 507023360
WS                         : 74444800
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
OtherOperationCount        : 17572
OtherTransferCount         : 134264
PageFaults                 : 7529
PageFileUsage              : 1680
ParentProcessId            : 1188
PeakPageFileUsage          : 1796
PeakVirtualSize            : 89497600
PeakWorkingSetSize         : 6160
Priority                   : 8
PrivatePageCount           : 1720320
ProcessId                  : 3492
QuotaNonPagedPoolUsage     : 12
QuotaPagedPoolUsage        : 152
QuotaPeakNonPagedPoolUsage : 13
QuotaPeakPagedPoolUsage    : 153
ReadOperationCount         : 2678
ReadTransferCount          : 21424
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 10
UserModeTime               : 0
VirtualSize                : 85270528
WindowsVersion             : 6.3.9600
WorkingSetSize             : 6270976
WriteOperationCount        : 1339
WriteTransferCount         : 5356
PSComputerName             : WIN-2012-DC
ProcessName                : VBoxTray.exe
Handles                    : 175
VM                         : 85270528
WS                         : 6270976
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
OtherOperationCount        : 271
OtherTransferCount         : 12671
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
OtherOperationCount        : 13025
OtherTransferCount         : 225557
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
QuotaPeakNonPagedPoolUsage : 29
QuotaPeakPagedPoolUsage    : 146
ReadOperationCount         : 218
ReadTransferCount          : 883050
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 1
UserModeTime               : 937500
VirtualSize                : 83390464
WindowsVersion             : 6.3.9600
WorkingSetSize             : 10915840
WriteOperationCount        : 42
WriteTransferCount         : 983
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
HandleCount                : 745
InstallDate                :
KernelModeTime             : 16875000
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : firefox.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 30643
OtherTransferCount         : 536836
PageFaults                 : 827850
PageFileUsage              : 141292
ParentProcessId            : 1188
PeakPageFileUsage          : 180008
PeakVirtualSize            : 1768960000
PeakWorkingSetSize         : 218196
Priority                   : 8
PrivatePageCount           : 144683008
ProcessId                  : 3116
QuotaNonPagedPoolUsage     : 62
QuotaPagedPoolUsage        : 607
QuotaPeakNonPagedPoolUsage : 87
QuotaPeakPagedPoolUsage    : 731
ReadOperationCount         : 4966
ReadTransferCount          : 249050437
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 42
UserModeTime               : 86718750
VirtualSize                : 1681330176
WindowsVersion             : 6.3.9600
WorkingSetSize             : 198397952
WriteOperationCount        : 318221
WriteTransferCount         : 80063549
PSComputerName             : WIN-2012-DC
ProcessName                : firefox.exe
Handles                    : 745
VM                         : 1681330176
WS                         : 198397952
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
PageFaults                 : 37617
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
ReadOperationCount         : 3950
ReadTransferCount          : 70436713
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 17
UserModeTime               : 6875000
VirtualSize                : 1378304000
WindowsVersion             : 6.3.9600
WorkingSetSize             : 72286208
WriteOperationCount        : 2307
WriteTransferCount         : 487820
PSComputerName             : WIN-2012-DC
ProcessName                : firefox.exe
Handles                    : 286
VM                         : 1378304000
WS                         : 72286208
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
HandleCount                : 94
InstallDate                :
KernelModeTime             : 937500
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : notepad.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 173
OtherTransferCount         : 1420
PageFaults                 : 2987
PageFileUsage              : 1460
ParentProcessId            : 1188
PeakPageFileUsage          : 1612
PeakVirtualSize            : 101261312
PeakWorkingSetSize         : 9816
Priority                   : 8
PrivatePageCount           : 1495040
ProcessId                  : 956
QuotaNonPagedPoolUsage     : 9
QuotaPagedPoolUsage        : 185
QuotaPeakNonPagedPoolUsage : 9
QuotaPeakPagedPoolUsage    : 195
ReadOperationCount         : 1
ReadTransferCount          : 60
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 1
UserModeTime               : 312500
VirtualSize                : 96096256
WindowsVersion             : 6.3.9600
WorkingSetSize             : 8454144
WriteOperationCount        : 8
WriteTransferCount         : 21612
PSComputerName             : WIN-2012-DC
ProcessName                : notepad.exe
Handles                    : 94
VM                         : 96096256
WS                         : 8454144
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
HandleCount                : 497
InstallDate                :
KernelModeTime             : 20937500
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : powershell.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 72072
OtherTransferCount         : 5471444
PageFaults                 : 294868
PageFileUsage              : 111616
ParentProcessId            : 1188
PeakPageFileUsage          : 113024
PeakVirtualSize            : 659030016
PeakWorkingSetSize         : 119420
Priority                   : 8
PrivatePageCount           : 114294784
ProcessId                  : 3416
QuotaNonPagedPoolUsage     : 35
QuotaPagedPoolUsage        : 433
QuotaPeakNonPagedPoolUsage : 38
QuotaPeakPagedPoolUsage    : 436
ReadOperationCount         : 1024
ReadTransferCount          : 3479940
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 10
UserModeTime               : 156093750
VirtualSize                : 656982016
WindowsVersion             : 6.3.9600
WorkingSetSize             : 120922112
WriteOperationCount        : 3
WriteTransferCount         : 5430
PSComputerName             : WIN-2012-DC
ProcessName                : powershell.exe
Handles                    : 497
VM                         : 656982016
WS                         : 120922112
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
HandleCount                : 56
InstallDate                :
KernelModeTime             : 17656250
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : conhost.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 47060
OtherTransferCount         : 2990951
PageFaults                 : 3531
PageFileUsage              : 5312
ParentProcessId            : 3416
PeakPageFileUsage          : 5456
PeakVirtualSize            : 62046208
PeakWorkingSetSize         : 13364
Priority                   : 8
PrivatePageCount           : 5439488
ProcessId                  : 1928
QuotaNonPagedPoolUsage     : 7
QuotaPagedPoolUsage        : 113
QuotaPeakNonPagedPoolUsage : 8
QuotaPeakPagedPoolUsage    : 114
ReadOperationCount         : 23
ReadTransferCount          : 756
SessionId                  : 1
Status                     :
TerminationDate            :
ThreadCount                : 2
UserModeTime               : 1250000
VirtualSize                : 61644800
WindowsVersion             : 6.3.9600
WorkingSetSize             : 13651968
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : conhost.exe
Handles                    : 56
VM                         : 61644800
WS                         : 13651968
Path                       : C:\Windows\system32\conhost.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="1816"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="1816"
Caption                    : WmiPrvSE.exe
CommandLine                : C:\Windows\system32\wbem\wmiprvse.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712164708.672298-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : WmiPrvSE.exe
ExecutablePath             : C:\Windows\system32\wbem\wmiprvse.exe
ExecutionState             :
Handle                     : 1816
HandleCount                : 327
InstallDate                :
KernelModeTime             : 10781250
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : WmiPrvSE.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 5019
OtherTransferCount         : 78910
PageFaults                 : 42193
PageFileUsage              : 21748
ParentProcessId            : 572
PeakPageFileUsage          : 24180
PeakVirtualSize            : 103436288
PeakWorkingSetSize         : 29212
Priority                   : 8
PrivatePageCount           : 22269952
ProcessId                  : 1816
QuotaNonPagedPoolUsage     : 22
QuotaPagedPoolUsage        : 140
QuotaPeakNonPagedPoolUsage : 26
QuotaPeakPagedPoolUsage    : 156
ReadOperationCount         : 7
ReadTransferCount          : 2721134
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 9
UserModeTime               : 5312500
VirtualSize                : 91705344
WindowsVersion             : 6.3.9600
WorkingSetSize             : 27447296
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : WmiPrvSE.exe
Handles                    : 327
VM                         : 91705344
WS                         : 27447296
Path                       : C:\Windows\system32\wbem\wmiprvse.exe

__GENUS                    : 2
__CLASS                    : Win32_Process
__SUPERCLASS               : CIM_Process
__DYNASTY                  : CIM_ManagedSystemElement
__RELPATH                  : Win32_Process.Handle="932"
__PROPERTY_COUNT           : 45
__DERIVATION               : {CIM_Process, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                   : WIN-2012-DC
__NAMESPACE                : root\cimv2
__PATH                     : \\WIN-2012-DC\root\cimv2:Win32_Process.Handle="932"
Caption                    : WmiApSrv.exe
CommandLine                : C:\Windows\system32\wbem\WmiApSrv.exe
CreationClassName          : Win32_Process
CreationDate               : 20170712164914.625986-420
CSCreationClassName        : Win32_ComputerSystem
CSName                     : WIN-2012-DC
Description                : WmiApSrv.exe
ExecutablePath             : C:\Windows\system32\wbem\WmiApSrv.exe
ExecutionState             :
Handle                     : 932
HandleCount                : 128
InstallDate                :
KernelModeTime             : 156250
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : WmiApSrv.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 350
OtherTransferCount         : 24138
PageFaults                 : 1338
PageFileUsage              : 1172
ParentProcessId            : 440
PeakPageFileUsage          : 1264
PeakVirtualSize            : 29896704
PeakWorkingSetSize         : 4956
Priority                   : 8
PrivatePageCount           : 1200128
ProcessId                  : 932
QuotaNonPagedPoolUsage     : 10
QuotaPagedPoolUsage        : 56
QuotaPeakNonPagedPoolUsage : 12
QuotaPeakPagedPoolUsage    : 57
ReadOperationCount         : 0
ReadTransferCount          : 0
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 5
UserModeTime               : 0
VirtualSize                : 29233152
WindowsVersion             : 6.3.9600
WorkingSetSize             : 5062656
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : WmiApSrv.exe
Handles                    : 128
VM                         : 29233152
WS                         : 5062656
Path                       : C:\Windows\system32\wbem\WmiApSrv.exe

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
HandleCount                : 136
InstallDate                :
KernelModeTime             : 156250
MaximumWorkingSetSize      : 1380
MinimumWorkingSetSize      : 200
Name                       : WmiPrvSE.exe
OSCreationClassName        : Win32_OperatingSystem
OSName                     : Microsoft Windows Server 2012 R2 Standard Evaluation|C:\Windows|\Device\Harddisk0\Partition2
OtherOperationCount        : 120
OtherTransferCount         : 122
PageFaults                 : 1403
PageFileUsage              : 2060
ParentProcessId            : 572
PeakPageFileUsage          : 2060
PeakVirtualSize            : 35057664
PeakWorkingSetSize         : 5352
Priority                   : 8
PrivatePageCount           : 2109440
ProcessId                  : 840
QuotaNonPagedPoolUsage     : 10
QuotaPagedPoolUsage        : 62
QuotaPeakNonPagedPoolUsage : 10
QuotaPeakPagedPoolUsage    : 63
ReadOperationCount         : 0
ReadTransferCount          : 0
SessionId                  : 0
Status                     :
TerminationDate            :
ThreadCount                : 8
UserModeTime               : 156250
VirtualSize                : 35057664
WindowsVersion             : 6.3.9600
WorkingSetSize             : 5480448
WriteOperationCount        : 0
WriteTransferCount         : 0
PSComputerName             : WIN-2012-DC
ProcessName                : WmiPrvSE.exe
Handles                    : 136
VM                         : 35057664
WS                         : 5480448
Path                       : C:\Windows\system32\wbem\wmiprvse.exe

PS C:\Users\Administrator>
```

```PowerShell
PS C:\Users\Administrator> Get-WmiObject -Class Win32_process | Select Name

Name
----
System Idle Process
System
smss.exe
csrss.exe
csrss.exe
wininit.exe
winlogon.exe
services.exe
lsass.exe
svchost.exe
svchost.exe
dwm.exe
VBoxService.exe
svchost.exe
svchost.exe
svchost.exe
svchost.exe
svchost.exe
spoolsv.exe
Microsoft.ActiveDirectory.WebServices.exe
dfsrs.exe
dns.exe
ismserv.exe
wlms.exe
dfssvc.exe
vds.exe
svchost.exe
svchost.exe
svchost.exe
msdtc.exe
taskhostex.exe
explorer.exe
VBoxTray.exe
cmd.exe
conhost.exe
python.exe
firefox.exe
firefox.exe
notepad.exe
powershell.exe
conhost.exe
WmiPrvSE.exe
WmiApSrv.exe
WmiPrvSE.exe

PS C:\Users\Administrator>
```

- Exploring ```Methods```

```PowerShell
PS C:\Users\Administrator> Get-WmiObject -Class Win32_process -List

   NameSpace: ROOT\cimv2

Name                                Methods              Properties
----                                -------              ----------
Win32_Process                       {Create, Terminat... {Caption, CommandLine, CreationClassName, CreationDate...}

PS C:\Users\Administrator>
```

```PowerShell
PS C:\Users\Administrator> Get-WmiObject -Class Win32_process -List | Select-Object -ExpandProperty Methods

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
