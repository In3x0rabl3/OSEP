#### 36. Registry and Powershell Part 1

###### Reading Windows Registry

- Registry Provider

```PowerShell
PS C:\> Get-PSProvider -PSProvider Registry

Name                 Capabilities                                                                               Drives
----                 ------------                                                                               ------
Registry             ShouldProcess, Transactions                                                                {HKLM, HKCU}

PS C:\>
```

- Reading Registry

    - ```Get-Item```

	```PowerShell
	PS C:\> Get-Item 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion'
	
	    Hive: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT
	
	
	Name                           Property
	----                           --------
	CurrentVersion                 SystemRoot             : C:\Windows
	                               SoftwareType           : System
	                               RegisteredOwner        : Windows User
	                               InstallDate            : 1499628648
	                               CurrentVersion         : 6.3
	                               CurrentBuild           : 9600
	                               RegisteredOrganization :
	                               CurrentType            : Multiprocessor Free
	                               InstallationType       : Server
	                               EditionID              : ServerStandardEval
	                               ProductName            : Windows Server 2012 R2 Standard Evaluation
	                               ProductId              : 00252-10000-00000-AA228
	                               DigitalProductId       : {164, 0, 0, 0...}
	                               DigitalProductId4      : {248, 4, 0, 0...}
	                               CurrentBuildNumber     : 9600
	                               BuildLab               : 9600.winblue_ltsb.170613-0600
	                               BuildLabEx             : 9600.18730.amd64fre.winblue_ltsb.170613-0600
	                               BuildGUID              : ffffffff-ffff-ffff-ffff-ffffffffffff
	                               PathName               : C:\Windows
	                               UBR                    : 18756
	
	PS C:\>
	```

	- ```Get-ItemProperty```

	```PowerShell
	PS C:\> Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion'
	
	SystemRoot             : C:\Windows
	SoftwareType           : System
	RegisteredOwner        : Windows User
	InstallDate            : 1499628648
	CurrentVersion         : 6.3
	CurrentBuild           : 9600
	RegisteredOrganization :
	CurrentType            : Multiprocessor Free
	InstallationType       : Server
	EditionID              : ServerStandardEval
	ProductName            : Windows Server 2012 R2 Standard Evaluation
	ProductId              : 00252-10000-00000-AA228
	DigitalProductId       : {164, 0, 0, 0...}
	DigitalProductId4      : {248, 4, 0, 0...}
	CurrentBuildNumber     : 9600
	BuildLab               : 9600.winblue_ltsb.170613-0600
	BuildLabEx             : 9600.18730.amd64fre.winblue_ltsb.170613-0600
	BuildGUID              : ffffffff-ffff-ffff-ffff-ffffffffffff
	PathName               : C:\Windows
	UBR                    : 18756
	PSPath                 : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion
	PSParentPath           : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT
	PSChildName            : CurrentVersion
	PSDrive                : HKLM
	PSProvider             : Microsoft.PowerShell.Core\Registry
	
	PS C:\>
	```

	```PowerShell
	PS C:\> Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion' | Format-List *
	
	SystemRoot             : C:\Windows
	SoftwareType           : System
	RegisteredOwner        : Windows User
	InstallDate            : 1499628648
	CurrentVersion         : 6.3
	CurrentBuild           : 9600
	RegisteredOrganization :
	CurrentType            : Multiprocessor Free
	InstallationType       : Server
	EditionID              : ServerStandardEval
	ProductName            : Windows Server 2012 R2 Standard Evaluation
	ProductId              : 00252-10000-00000-AA228
	DigitalProductId       : {164, 0, 0, 0...}
	DigitalProductId4      : {248, 4, 0, 0...}
	CurrentBuildNumber     : 9600
	BuildLab               : 9600.winblue_ltsb.170613-0600
	BuildLabEx             : 9600.18730.amd64fre.winblue_ltsb.170613-0600
	BuildGUID              : ffffffff-ffff-ffff-ffff-ffffffffffff
	PathName               : C:\Windows
	UBR                    : 18756
	PSPath                 : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion
	PSParentPath           : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT
	PSChildName            : CurrentVersion
	PSDrive                : HKLM
	PSProvider             : Microsoft.PowerShell.Core\Registry
	
	PS C:\>
	```
	
	- ```Get-ChildItem```

	```PowerShell
	PS C:\> Get-ChildItem 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion'
	
	    Hive: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion
	
	
	Name                           Property
	----                           --------
	Accessibility
	Active Directory
	AeDebug                        UserDebuggerHotKey : 0
	AppCompatFlags                 MirrorCompatBinaryExtension : C:\Windows\System32\MirrorDrvCompat.dll
	                               AmiCacheVersion             : 2
	ASR                            OfflineDriverInjectionExtension : drvstore.dll,DriverStoreOfflineAddDriverPackageW
	Audit
	BackgroundModel
	Compatibility32                winword : 0x80000000
	Console
	CorruptedFileRecovery          TraceLevel : 0
	                               RunCount   : 0
	DefaultProductKey              ProductId         : 00252-10000-00001-AA599
	                               DigitalProductId  : {164, 0, 0, 0...}
	                               DigitalProductId4 : {248, 4, 0, 0...}
	DeviceDisplayObjects           DeviceStatusPropertyDescriptionList :
	                               prop:System.Devices.Status;System.PrintStatus.ErrorStatus;System.PrintStatus.WarningStatus;System.PrintStatus.DocumentCount;System.PrintStatus.InfoStatus;System.Pri
	                                                                     ntStatus.Preferences;System.ScanStatus.Profile;System.PrintStatus.Location;System.PrintStatus.Comment;System.Devices.Connected
	DNS Server
	drivers.desc                   wdmaud.drv : Microsoft 1.1 UAA Function Driver for High Definition Audio
	Drivers32                      vidc.yuy2      : msyuv.dll
	                               vidc.i420      : iyuv_32.dll
	                               msacm.msgsm610 : msgsm32.acm
	                               msacm.msg711   : msg711.acm
	                               vidc.yvyu      : msyuv.dll
	                               vidc.yvu9      : tsbyuv.dll
	                               wavemapper     : msacm32.drv
	                               midimapper     : midimap.dll
	                               vidc.uyvy      : msyuv.dll
	                               vidc.iyuv      : iyuv_32.dll
	                               vidc.mrle      : msrle32.dll
	                               msacm.imaadpcm : imaadp32.acm
	                               msacm.msadpcm  : msadp32.acm
	                               vidc.msvc      : msvidc32.dll
	                               wave           : wdmaud.drv
	                               midi           : wdmaud.drv
	                               mixer          : wdmaud.drv
	                               aux            : wdmaud.drv
	EFS
	Event Viewer                   MicrosoftRedirectionURL                          : http://go.microsoft.com/fwlink/events.asp
	                               MicrosoftRedirectionProgramCommandLineParameters :
	                               MicrosoftRedirectionProgram                      :
	Font Drivers                   Adobe Type Manager : atmfd.dll
	Font Management                Auto Deactivation Exclude : {Calibri, Cambria, Consolas, Georgia...}
	                               Metadata                  : C:\Windows\Fonts\fms_metadata.xml
	FontDPI                        LogPixels : 96
	FontLink                       FontLinkControl     : 0
	                               FontLinkDefaultChar : 12539
	FontMapper                     @MS Mincho      : 57472
	                               @MS Gothic      : 41088
	                               @GulimChe       : 41089
	                               @Batang         : 24705
	                               @PMingLiU       : 8328
	                               MingLiU         : 32904
	                               MS Gothic       : 32896
	                               @BatangChe      : 57473
	                               @MS PGothic     : 8320
	                               @DotumChe       : 45185
	                               @MS PMincho     : 24704
	                               BatangChe       : 49281
	                               NSimSun         : 32902
	                               DotumChe        : 36993
	                               SMALL FONTS     : 2048
	                               SimSun          : 134
	                               @Gulim          : 8321
	                               MS SANS SERIF   : 4096
	                               FIXEDSYS        : 36864
	                               @Dotum          : 12417
	                               COURIER         : 34816
	                               PMingLiU        : 136
	                               @MingLiU        : 41096
	                               @SimSun         : 8326
	                               GulimChe        : 32897
	                               MS PGothic      : 128
	                               SYMBOL          : 16386
	                               @Gungsuh        : 28801
	                               ARIAL           : 0
	                               Dotum           : 4225
	                               Gungsuh         : 20609
	                               WINGDINGS       : 2
	                               GungsuhChe      : 53377
	                               Gulim           : 129
	                               MS PMincho      : 16512
	                               MS Mincho       : 49280
	                               MS SERIF        : 20480
	                               @NSimSun        : 41094
	                               COURIER NEW     : 32768
	                               @GungsuhChe     : 61569
	                               SYMBOL1         : 40962
	                               TIMES NEW ROMAN : 16384
	                               Batang          : 16513
	                               DEFAULT         : 0
	Fonts                          SimSun-ExtB (TrueType)                                                               : simsunb.ttf
	                               KodchiangUPC Bold (TrueType)                                                         : upckb.ttf
	                               Kokila Bold (TrueType)                                                               : kokilab.ttf
	                               Shonar Bangla (TrueType)                                                             : Shonar.ttf
	                               Mangal (TrueType)                                                                    : mangal.ttf
	                               BrowalliaUPC Bold Italic (TrueType)                                                  : browauz.ttf
	                               Sakkal Majalla Bold (TrueType)                                                       : majallab.ttf
	                               LilyUPC Bold Italic (TrueType)                                                       : upclbi.ttf
	                               Palatino Linotype Bold (TrueType)                                                    : palab.ttf
	                               MoolBoran (TrueType)                                                                 : moolbor.ttf
	                               Franklin Gothic Medium Italic (TrueType)                                             : framdit.ttf
	                               Cordia New (TrueType)                                                                : cordia.ttf
	                               Arial Italic (TrueType)                                                              : ariali.ttf
	                               Kokila Italic (TrueType)                                                             : kokilai.ttf
	                               AngsanaUPC Italic (TrueType)                                                         : angsaui.ttf
	                               JasmineUPC (TrueType)                                                                : upcjl.ttf
	                               Trebuchet MS Bold (TrueType)                                                         : trebucbd.ttf
	                               Microsoft Tai Le (TrueType)                                                          : taile.ttf
	                               Utsaah (TrueType)                                                                    : utsaah.ttf
	                               Malgun Gothic (TrueType)                                                             : malgun.ttf
	                               Simplified Arabic Fixed (TrueType)                                                   : simpfxo.ttf
	                               Gisha (TrueType)                                                                     : gisha.ttf
	                               Utsaah Bold Italic(TrueType)                                                         : utsaahbi.ttf
	                               Microsoft JhengHei Light (TrueType) & Microsoft JhengHei UI Light (TrueType)         : msjhl.ttc
	                               Comic Sans MS Bold (TrueType)                                                        : comicbd.ttf
	                               BrowalliaUPC (TrueType)                                                              : browau.ttf
	                               Segoe UI Symbol (TrueType)                                                           : seguisym.ttf
	                               Kokila (TrueType)                                                                    : kokila.ttf
	                               Vrinda Bold (TrueType)                                                               : vrindab.ttf
	                               FreesiaUPC Bold Italic (TrueType)                                                    : upcfbi.ttf
	                               Traditional Arabic Bold (TrueType)                                                   : tradbdo.ttf
	                               Aparajita Bold (TrueType)                                                            : aparajb.ttf
	                               Sitka Bold Italic                                                                    : SitkaZ.ttc
	                               Nirmala UI Semilight (TrueType)                                                      : NirmalaS.ttf
	                               Leelawadee UI Bold (TrueType)                                                        : leelauib.ttf
	                               KodchiangUPC Bold Italic (TrueType)                                                  : upckbi.ttf
	                               Gadugi Bold (TrueType)                                                               : gadugib.ttf
	                               Microsoft New Tai Lue (TrueType)                                                     : ntailu.ttf
	                               DokChampa (TrueType)                                                                 : dokchamp.ttf
	                               Palatino Linotype Bold Italic (TrueType)                                             : palabi.ttf
	                               Segoe UI Italic (TrueType)                                                           : segoeuii.ttf
	                               Calibri Bold (TrueType)                                                              : calibrib.ttf
	                               Cordia New Bold Italic (TrueType)                                                    : cordiaz.ttf
	                               Miriam (TrueType)                                                                    : mriam.ttf
	                               Angsana New Bold (TrueType)                                                          : angsab.ttf
	                               Iskoola Pota (TrueType)                                                              : iskpota.ttf
	                               FreesiaUPC (TrueType)                                                                : upcfl.ttf
	                               Kartika (TrueType)                                                                   : kartika.ttf
	                               Segoe UI Semilight (TrueType)                                                        : segoeuisl.ttf
	                               Vijaya (TrueType)                                                                    : vijaya.ttf
	                               Nirmala UI (TrueType)...
	FontSubstitutes                Arabic Transparent,0       : Arial,178
	                               Arabic Transparent Bold,0  : Arial Bold,178
	                               Arabic Transparent Bold    : Arial Bold
	                               Rod Transparent            : Rod
	                               Courier New CYR,204        : Courier New,204
	                               Times New Roman CYR,204    : Times New Roman,204
	                               Helvetica                  : Arial
	                               Arial CE,238               : Arial,238
	                               MS Shell Dlg 2             : Tahoma
	                               David Transparent          : David
	                               Courier New TUR,162        : Courier New,162
	                               Times New Roman TUR,162    : Times New Roman,162
	                               Times                      : Times New Roman
	                               Miriam Transparent         : Miriam
	                               Times New Roman CE,238     : Times New Roman,238
	                               Arial Greek,161            : Arial,161
	                               KaiTi_GB2312               : KaiTi
	                               Courier New CE,238         : Courier New,238
	                               Arial Baltic,186           : Arial,186
	                               Tahoma Armenian            : Tahoma
	                               FangSong_GB2312            : FangSong
	                               Arial TUR,162              : Arial,162
	                               Tms Rmn                    : MS Serif
	                               Courier New Greek,161      : Courier New,161
	                               Times New Roman Baltic,186 : Times New Roman,186
	                               Arial CYR,204              : Arial,204
	                               Arabic Transparent         : Arial
	                               Helv                       : MS Sans Serif
	                               Courier New Baltic,186     : Courier New,186
	                               Times New Roman Greek,161  : Times New Roman,161
	                               Fixed Miriam Transparent   : Miriam Fixed
	                               MS Shell Dlg               : Microsoft Sans Serif
	GRE_Initialize                 DisableRemoteFontBootCache  : 0
	                               ServicingStackModifiedFonts : 2
	ICM
	Image File Execution Options
	IniFileMapping
	InstalledFeatures
	KnownFunctionTableDlls         C:\Windows\Microsoft.NET\Framework64\v4.0.30319\mscordacwks.dll : 0
	KnownManagedDebuggingDlls      C:\Windows\Microsoft.NET\Framework64\v4.0.30319\mscordacwks.dll : 0
	                               C:\Windows\System32\mrt_map.dll                                 : 0
	LanguagePack                   OpenType : 0
	MCI Extensions                 aiff : MPEGVideo
	                               dat  : MPEGVideo
	                               m2t  : MPEGVideo
	                               mpa  : MPEGVideo
	                               wmx  : MPEGVideo
	                               wmv  : MPEGVideo
	                               Mid  : Sequencer
	                               m3u  : MPEGVideo
	                               avi  : avivideo
	                               ivf  : MPEGVideo
	                               wvx  : MPEGVideo
	                               m4v  : MPEGVideo
	                               mts  : MPEGVideo
	                               mp4v : MPEGVideo
	                               mp2v : MPEGVideo
	                               adts : MPEGVideo
	                               wma  : MPEGVideo
	                               mpeg : MPEGVideo
	                               tts  : MPEGVideo
	                               mpv2 : MPEGVideo
	                               au   : MPEGVideo
	                               3gpp : MPEGVideo
	                               m4a  : MPEGVideo
	                               wax  : MPEGVideo
	                               aif  : MPEGVideo
	                               asx  : MPEGVideo
	                               m2ts : MPEGVideo
	                               mov  : MPEGVideo
	                               Wav  : WaveAudio
	                               aac  : MPEGVideo
	                               wpl  : MPEGVideo
	                               3gp2 : MPEGVideo
	                               mp4  : MPEGVideo
	                               mp3  : MPEGVideo
	                               mp2  : MPEGVideo
	                               wm   : MPEGVideo
	                               adt  : MPEGVideo
	                               cda  : CDAudio
	                               3g2  : MPEGVideo
	                               asf  : MPEGVideo
	                               mod  : MPEGVideo
	                               m1v  : MPEGVideo
	                               ts   : MPEGVideo
	                               rmi  : Sequencer
	                               mpg  : MPEGVideo
	                               3gp  : MPEGVideo
	                               aifc : MPEGVideo
	                               mpe  : MPEGVideo
	                               m2v  : MPEGVideo
	                               snd  : MPEGVideo
	MCI32                          AVIVideo  : mciavi32.dll
	                               Sequencer : mciseq.dll
	                               CDAudio   : mcicda.dll
	                               WaveAudio : mciwave.dll
	                               MPEGVideo : mciqtz32.dll
	MiniDumpAuxiliaryDlls          C:\Windows\system32\jscript9.dll                             : C:\Windows\System32\jscript9diag.dll
	                               C:\Windows\Microsoft.NET\Framework64\v2.0.50727\mscorwks.dll : C:\Windows\Microsoft.NET\Framework64\v2.0.50727\mscordacwks.dll
	                               C:\Windows\Microsoft.NET\Framework64\v4.0.30319\clr.dll      : C:\Windows\Microsoft.NET\Framework64\v4.0.30319\mscordacwks.dll
	                               C:\Windows\system32\mrt100.dll                               : C:\Windows\System32\mrt_map.dll
	MsiCorruptedFileRecovery
	Multimedia
	NetworkCards
	NetworkList                    (default)       : 192.228.79.201
	                               RootDnsIpv6Addr : 2001:478:65::53
	                               FirstNetwork    : 0
	NoImeModeImes
	Notifications
	NtVdm64
	OpenGLDrivers
	PeerDist
	Perflib                        Version             : 65537
	                               Last Help           : 8909
	                               Last Counter        : 8908
	                               Base Index          : 1847
	                               ExtCounterTestLevel : 4
	Ports                          LPT1:       :
	                               COM3:       : 9600,n,8,1
	                               LPT2:       :
	                               COM4:       : 9600,n,8,1
	                               LPT3:       :
	                               PORTPROMPT: :
	                               FILE:       :
	                               COM1:       : 9600,n,8,1
	                               COM2:       : 9600,n,8,1
	                               Ne00:       :
	Print                          DoNotInstallCompatibleDriverFromWindowsUpdate : 1
	ProfileGuid
	ProfileList                    Default           : C:\Users\Default
	                               ProfilesDirectory : C:\Users
	                               ProgramData       : C:\ProgramData
	                               Public            : C:\Users\Public
	ProfileLoader
	ProfileNotification            Load    : *
	                               Migrate : *
	                               Delete  : *
	                               Upgrade : *
	                               Unload  : *
	                               Create  : *
	related.desc                   wave :
	RemoteRegistry                 DisableIdleStop : 0
	Schedule                       DomainJoinDetected        : 1
	                               MigrationCleanupCompleted : 1
	                               MTRCompleted              : 1
	                               HashingCompleted          : 1
	SCW                            (default) : C:\Windows\System32\scw.exe
	                               Path      : C:\Windows\security\msscw\
	SecEdit                        SetupCompDebugLevel  : 1
	                               EnvironmentVariables : {%AppData%, %UserProfile%, %AllUsersProfile%, %ProgramFiles%...}
	                               DefaultTemplate      : C:\Windows\Inf\secrecs.inf
	                               LastUsedDatabase     : C:\WINDOWS\Security\Database\secedit.sdb
	                               TemplateUsed         : C:\Windows\inf\defltdc.inf
	                               LastWinLogonConfig   : 1184467804
	Sensor
	Server
	setup
	SoftwareProtectionPlatform     VLRenewalInterval        : 10080
	                               UserOperations           : 0
	                               SkipRearm                : 0
	                               VLActivationInterval     : 120
	                               KeepRunningThresholdMins : 15
	                               TokenStore               : %WINDIR%\System32\spp\store\2.0
	                               InactivityShutdownDelay  : 30
	                               CacheStore               : %WINDIR%\System32\spp\store\2.0\cache
	                               ServiceSessionId         : {34, 57, 148, 180...}
	                               LicStatusArray           : {19, 111, 103, 229...}
	                               PolicyValuesArray        : {52, 39, 201, 85...}
	                               actionlist               : {139, 59, 15, 219...}
	                               HasOOBERun               : 1
	                               WSServiceTlrTrigger      : 1
	Superfetch
	Svchost                        RPCSS                            : {RpcEptMapper, RpcSs}
	                               LocalService                     : {nsi, WdiServiceHost, w32time, EventSystem...}
	                               WepHostSvcGroup                  : {WepHostSvc}
	                               defragsvc                        : {defragsvc}
	                               KpsSvcGroup                      : {kpssvc}
	                               DcomLaunch                       : {Power, LSM, BrokerInfrastructure, PlugPlay...}
	                               LocalSystemNetworkRestricted     : {WdiSystemHost, ScDeviceEnum, trkwks, AudioEndpointBuilder...}
	                               netsvcs                          : {AeLookupSvc, CertPropSvc, SCPolicySvc, lanmanserver...}
	                               WerSvcGroup                      : {wersvc}
	                               LocalServiceNoNetwork            : {DPS, PLA, BFE, mpssvc}
	                               termsvcs                         : {TermService}
	                               swprv                            : {swprv}
	                               wsappx                           : {WSService, AppXSvc}
	                               ICService                        : {vmicheartbeat, vmicrdv}
	                               smphost                          : {smphost}
	                               LocalServiceNetworkRestricted    : {DHCP, eventlog, AudioSrv, LmHosts...}
	                               LocalServicePeerNet              : {PNRPSvc, p2pimsvc, p2psvc, PnrpAutoReg}
	                               NetworkServiceAndNoImpersonation : {KtmRm}
	                               regsvc                           : {RemoteRegistry}
	                               wcssvc                           : {WcsPlugInService}
	                               TapiSrv                          : {TapiSrv}
	                               LocalServiceAndNoImpersonation   : {SSDPSRV, upnphost, SCardSvr, BthHFSrv...}
	                               NetworkServiceNetworkRestricted  : {PolicyAgent}
	                               AppReadiness                     : {AppReadiness}
	                               NetworkService                   : {CryptSvc, nlasvc, lanmanworkstation, NapAgent...}
	                               print                            : {PrintNotify}
	                               utcsvc                           : {DiagTrack}
	Terminal Server
	Time Zones                     TzVersion : 132187136
	Tracing
	UnattendSettings
	Userinstallable.drivers        wave : wdmaud.drv
	WbemPerf
	Windows                        (default)                    : mnmsrvc
	                               Spooler                      : yes
	                               DeviceNotSelectedTimeout     : 15
	                               TransmissionRetryTimeout     : 90
	                               EnableDwmInputProcessing     : 7
	                               ShutdownWarningDialogTimeout : 4294967295
	                               USERProcessHandleQuota       : 10000
	                               LoadAppInit_DLLs             : 0
	                               IconServiceLib               : IconCodecService.dll
	                               DesktopHeapLogging           : 1
	                               DdeSendTimeout               : 0
	                               DwmInputUsesIoCompletionPort : 1
	                               USERPostMessageLimit         : 10000
	                               USERNestedWindowLimit        : 50
	                               AppInit_DLLs                 :
	                               NaturalInputHandler          : Ninput.dll
	                               ThreadUnresponsiveLogTimeout : 500
	                               GDIProcessHandleQuota        : 10000
	                               RequireSignedAppInit_DLLs    : 1
	                               Win32kLastWriteTime          : 1D2EB62FDEA7E06
	WindowsServerBackup
	Winlogon                       Userinit               : C:\Windows\system32\userinit.exe,
	                               LegalNoticeText        :
	                               Shell                  : explorer.exe
	                               LegalNoticeCaption     :
	                               DebugServerCommand     : no
	                               ForceUnlockLogon       : 0
	                               ReportBootOk           : 1
	                               VMApplet               : SystemPropertiesPerformance.exe /pagefile
	                               AutoRestartShell       : 1
	                               PowerdownAfterShutdown : 0
	                               ShutdownWithoutLogon   : 0
	                               Background             : 0 0 0
	                               PreloadFontFile        : SC-Load.All
	                               PasswordExpiryWarning  : 5
	                               CachedLogonsCount      : 10
	                               WinStationsDisabled    : 0
	                               PreCreateKnownFolders  : {A520A1A4-1780-4FF6-BD18-167343C5AF16}
	                               DisableCAD             : 1
	                               scremoveoption         : 0
	                               ShutdownFlags          : 2147483751
	                               AutoLogonSID           : S-1-5-32
	                               LastUsedUsername       :
	                               DisableLockWorkstation : 0
	                               DefaultDomainName      : PFPT
	WSService
	WUDF                           DefaultHostProcessGUID : {193a1820-d9ac-4997-8c55-be817523f6aa}
	                               Logkd                  : 0
	                               LogFlushPeriodSeconds  : 300
	                               LogEnable              : 0
	                               LogMinidumpType        : 4384
	                               HostFailKdDebugBreak   : 1
	                               LogFlags               : 16777215
	                               LogLevel               : 3
	                               NumDeviceStacksMax     : 3
	
	PS C:\>
	```
	
	```PowerShell
	PS C:\> Get-ChildItem 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion' -Recurse
	```
	
###### Accessing all Registry hives

- ```Method 1```

```PowerShell
PS C:\> Set-Location Registry::
```

```PowerShell
PS Microsoft.PowerShell.Core\Registry::> ls

    Hive:


Name                           Property
----                           --------
HKEY_LOCAL_MACHINE
HKEY_CURRENT_USER
HKEY_CLASSES_ROOT
HKEY_CURRENT_CONFIG
HKEY_USERS
HKEY_PERFORMANCE_DATA          Global : {80, 0, 69, 0...}
                               Costly : {80, 0, 69, 0...}

PS Microsoft.PowerShell.Core\Registry::>
```

```PowerShell
PS Microsoft.PowerShell.Core\Registry::> cd HKEY_CLASSES_ROOT
```

```PowerShell
PS Microsoft.PowerShell.Core\Registry::HKEY_CLASSES_ROOT>
```

- ```Method 2```

```PowerShell
PS C:\> New-PSDrive -name RegistryDrive -PSProvider Registry -Root Registry::HKEY_CLASSES_ROOT

Name           Used (GB)     Free (GB) Provider      Root                                                                                                                                  CurrentLocation
----           ---------     --------- --------      ----                                                                                                                                  ---------------
Registr...                             Registry      HKEY_CLASSES_ROOT

PS C:\>
```

```PowerShell
PS C:\> cd RegistryDrive:
```

```PowerShell
PS RegistryDrive:\> ls


    Hive: HKEY_CLASSES_ROOT


Name                           Property
----                           --------
*                              ContentViewModeForBrowse              :
                               prop:~System.ItemNameDisplay;System.ItemTypeText;~System.LayoutPattern.PlaceHolder;~System.LayoutPattern.PlaceHolder;System.DateModified;System.Size
                               ContentViewModeLayoutPatternForBrowse : delta
                               SetDefaultsFor                        : prop:System.Author;System.Document.DateCreated
                               InfoTip                               : prop:System.ItemTypeText;System.Size;System.DateModified
                               ContentViewModeForSearch              :
                               prop:~System.ItemNameDisplay;~System.ItemFolderPathDisplay;~System.LayoutPattern.PlaceHolder;System.ItemTypeText;System.DateModified;System.Size
                               ContentViewModeLayoutPatternForSearch : delta
                               ConflictPrompt                        : prop:System.ItemTypeText;System.Size;System.DateModified;System.DateCreated
                               AlwaysShowExt                         :
                               ExtendedTileInfo                      : prop:System.ItemTypeText;System.Size;System.DateModified;System.OfflineAvailability
                               FullDetails                           :
                               prop:System.PropGroup.FileSystem;System.ItemNameDisplay;System.ItemTypeText;System.ItemFolderPathDisplay;System.Size;System.DateCreated;System.DateModified;System
                                                                       .FileAttributes;*System.OfflineAvailability;*System.OfflineStatus;*System.SharedWith;*System.FileOwner;*System.ComputerName
                               PreviewTitle                          : prop:System.ItemNameDisplay;System.ItemTypeText
                               QuickTip                              : prop:System.ItemTypeText;System.Size;System.DateModified
                               NoStaticDefaultVerb                   :
                               PreviewDetails                        : prop:System.DateModified;System.Size;System.DateCreated;*System.OfflineAvailability;*System.OfflineStatus;*System.SharedWith
                               NoRecentDocs                          :
                               TileInfo                              : prop:System.ItemTypeText;System.Size;System.DateModified
.386                           (default)     : vxdfile
                               PerceivedType : system
.a
.accountpicture-ms             (default)    : accountpicturefile
                               Content Type : application/windows-accountpicture
.ai                            Content Type : application/postscript
.aif                           PerceivedType : audio
```

```PowerShell
PS RegistryDrive:\> Get-PSDrive

Name           Used (GB)     Free (GB) Provider      Root                                                                                                                                  CurrentLocation
----           ---------     --------- --------      ----                                                                                                                                  ---------------
Alias                                  Alias
C                  17.41         14.25 FileSystem    C:\
Cert                                   Certificate   \
D                    .06               FileSystem    D:\
Env                                    Environment
Function                               Function
HKCU                                   Registry      HKEY_CURRENT_USER
HKLM                                   Registry      HKEY_LOCAL_MACHINE
Registr...                             Registry      HKEY_CLASSES_ROOT
Variable                               Variable
WSMan                                  WSMan

PS RegistryDrive:\>
```

###### Exercise
- Get a list of [```TypedURLs```](http://www.wikihow.com/Clear-Internet-Explorer%27s-URL-History-by-Editing-the-Registry) from Windows Registry.

```PowerShell
PS C:\> Get-Item 'HKCU:\SOFTWARE\Microsoft\Internet Explorer\TypedURLs'

    Hive: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Internet Explorer


Name                           Property
----                           --------
TypedURLs                      url1 : https://www.google.com/
                               url2 : https://github.com/samratashok/nishang
                               url3 : http://www.bing.com/search?q=nishang&FORM=IE8SRC
                               url4 : http://go.microsoft.com/fwlink/p/?LinkId=255141

PS C:\>
```

- List all [```installed software```](https://social.technet.microsoft.com/Forums/windows/en-US/d913471a-d7fb-448d-869b-da9025dcc943/where-does-addremove-programs-get-its-information-from-in-the-registry?forum=w7itprogeneral) on a computer from Windows Registry

```PowerShell
PS C:\> Get-ChildItem 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall'

    Hive: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall


Name                           Property
----                           --------
AddressBook
Connection Manager             SystemComponent : 1
DirectDrawEx
Fontcore
IE40
IE4Data
IE5BAKEX
IEData
MobileOptionPack
Mozilla Firefox 54.0.1 (x64    Comments        : Mozilla Firefox 54.0.1 (x64 en-US)
en-US)                         DisplayIcon     : C:\Program Files\Mozilla Firefox\firefox.exe,0
                               DisplayName     : Mozilla Firefox 54.0.1 (x64 en-US)
                               DisplayVersion  : 54.0.1
                               HelpLink        : https://support.mozilla.org
                               InstallLocation : C:\Program Files\Mozilla Firefox
                               Publisher       : Mozilla
                               UninstallString : "C:\Program Files\Mozilla Firefox\uninstall\helper.exe"
                               URLUpdateInfo   : https://www.mozilla.org/firefox/54.0.1/releasenotes
                               URLInfoAbout    : https://www.mozilla.org
                               NoModify        : 1
                               NoRepair        : 1
                               EstimatedSize   : 103916
MozillaMaintenanceService      DisplayName     : Mozilla Maintenance Service
                               UninstallString : "C:\Program Files (x86)\Mozilla Maintenance Service\uninstall.exe"
                               DisplayIcon     : C:\Program Files (x86)\Mozilla Maintenance Service\Uninstall.exe,0
                               DisplayVersion  : 54.0.1
                               Publisher       : Mozilla
                               Comments        : Mozilla Maintenance Service
                               NoModify        : 1
                               EstimatedSize   : 278
Oracle VM VirtualBox Guest     DisplayName     : Oracle VM VirtualBox Guest Additions 5.1.22
Additions                      UninstallString : C:\Program Files\Oracle\VirtualBox Guest Additions\uninst.exe
                               DisplayVersion  : 5.1.22.0
                               URLInfoAbout    : http://www.virtualbox.org
                               Publisher       : Oracle Corporation
SchedulingAgent
WIC                            NoRemove : 1

PS C:\>
```