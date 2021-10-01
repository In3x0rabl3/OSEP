#### 28. Using .NET in Powershell Part 2

###### System.Windows.Forms

- ```Add-Type``` Cmdlet with ```AssemblyName``` ```System.Windows.Forms```

```PowerShell
PS C:\> Add-Type -AssemblyName System.Windows.Forms
```

- Check if ```System.Windows.Forms``` is loaded

```PowerShell
PS C:\> [System.Windows.Forms.SendKeys]

IsPublic IsSerial Name                                     BaseType
-------- -------- ----                                     --------
True     False    SendKeys                                 System.Object

PS C:\>
```

- List ```Static``` members of ```System.Windows.Forms```

```PowerShell
PS C:\> [System.Windows.Forms.SendKeys] | Get-Member -Static

   TypeName: System.Windows.Forms.SendKeys

Name            MemberType Definition
----            ---------- ----------
Equals          Method     static bool Equals(System.Object objA, System.Object objB)
Flush           Method     static System.Void Flush()
ReferenceEquals Method     static bool ReferenceEquals(System.Object objA, System.Object objB)
Send            Method     static System.Void Send(string keys)
SendWait        Method     static System.Void SendWait(string keys)

PS C:\>
```

```PowerShell
PS C:\> [System.Windows.Forms.SendKeys] | Get-Member -Static | Format-List *

TypeName   : System.Windows.Forms.SendKeys
Name       : Equals
MemberType : Method
Definition : static bool Equals(System.Object objA, System.Object objB)

TypeName   : System.Windows.Forms.SendKeys
Name       : Flush
MemberType : Method
Definition : static System.Void Flush()

TypeName   : System.Windows.Forms.SendKeys
Name       : ReferenceEquals
MemberType : Method
Definition : static bool ReferenceEquals(System.Object objA, System.Object objB)

TypeName   : System.Windows.Forms.SendKeys
Name       : Send
MemberType : Method
Definition : static System.Void Send(string keys)

TypeName   : System.Windows.Forms.SendKeys
Name       : SendWait
MemberType : Method
Definition : static System.Void SendWait(string keys)

PS C:\>
```

- Use ```SendWait``` ```Static``` member

```PowerShell
PS C:\> [System.Windows.Forms.SendKeys]::SendWait

MemberType          : Method
OverloadDefinitions : {static System.Void SendWait(string keys)}
TypeNameOfValue     : System.Management.Automation.PSMethod
Value               : static System.Void SendWait(string keys)
Name                : SendWait
IsInstance          : True

PS C:\>
```

```PowerShell
PS C:\> [System.Windows.Forms.SendKeys]::SendWait("Powershell for Pentesters")
PS C:\> Powershell for Pentesters
PS C:\> 
```

###### System.ServiceProcess

- ```Add-Type``` Cmdlet with ```AssemblyName``` ```System.ServiceProcess```

```PowerShell
PS C:\> Add-Type -AssemblyName System.ServiceProcess
```

- Check if ```System.ServiceProcess.ServiceController``` is loaded

```PowerShell
PS C:\> [System.ServiceProcess.ServiceController]

IsPublic IsSerial Name                                     BaseType
-------- -------- ----                                     --------
True     False    ServiceController                        System.ComponentModel.Component

PS C:\>
```

- List ```Static``` members of ```System.ServiceProcess.ServiceController```

```PowerShell
PS C:\> [System.ServiceProcess.ServiceController] | Get-Member -Static

   TypeName: System.ServiceProcess.ServiceController

Name            MemberType Definition
----            ---------- ----------
Equals          Method     static bool Equals(System.Object objA, System.Object objB)
GetDevices      Method     static System.ServiceProcess.ServiceController[] GetDevices(), static System.ServiceProcess.ServiceController[] GetDevices(string machineName)
GetServices     Method     static System.ServiceProcess.ServiceController[] GetServices(), static System.ServiceProcess.ServiceController[] GetServices(string machineName)
ReferenceEquals Method     static bool ReferenceEquals(System.Object objA, System.Object objB)

PS C:\>
```

```PowerShell
PS C:\> [System.ServiceProcess.ServiceController] | Get-Member -Static | Format-List *

TypeName   : System.ServiceProcess.ServiceController
Name       : Equals
MemberType : Method
Definition : static bool Equals(System.Object objA, System.Object objB)

TypeName   : System.ServiceProcess.ServiceController
Name       : GetDevices
MemberType : Method
Definition : static System.ServiceProcess.ServiceController[] GetDevices(), static System.ServiceProcess.ServiceController[] GetDevices(string machineName)

TypeName   : System.ServiceProcess.ServiceController
Name       : GetServices
MemberType : Method
Definition : static System.ServiceProcess.ServiceController[] GetServices(), static System.ServiceProcess.ServiceController[] GetServices(string machineName)

TypeName   : System.ServiceProcess.ServiceController
Name       : ReferenceEquals
MemberType : Method
Definition : static bool ReferenceEquals(System.Object objA, System.Object objB)

PS C:\>
```

- Use ```GetDevices``` ```Static``` member

```PowerShell
PS C:\> [System.ServiceProcess.ServiceController]::GetDevices()

Status   Name               DisplayName
------   ----               -----------
Stopped  1394ohci           1394 OHCI Compliant Host Controller
Running  ACPI               Microsoft ACPI Driver
Stopped  AcpiPmi            ACPI Power Meter Driver
Stopped  adp94xx            adp94xx
Stopped  adpahci            adpahci
Stopped  adpu320            adpu320
Running  AFD                Ancillary Function Driver for Winsock
Stopped  agp440             Intel AGP Bus Filter
Stopped  aic78xx            aic78xx
Stopped  aliide             aliide
Stopped  amdagp             AMD AGP Bus Filter Driver
Stopped  amdide             amdide
Stopped  AmdK8              AMD K8 Processor Driver
Stopped  AmdPPM             AMD Processor Driver
Stopped  amdsata            amdsata
Stopped  amdsbs             amdsbs
Running  amdxata            amdxata
Stopped  AppID              AppID Driver
Stopped  arc                arc
Stopped  arcsas             arcsas
Stopped  AsyncMac           RAS Asynchronous Media Driver
Running  atapi              IDE Channel
Stopped  b06bdrv            Broadcom NetXtreme II VBD
Stopped  b57nd60x           Broadcom NetXtreme Gigabit Ethernet...
Running  Beep               Beep
Running  blbdrive           blbdrive
Running  bowser             Browser Support Driver
Stopped  BrFiltLo           Brother USB Mass-Storage Lower Filt...
Stopped  BrFiltUp           Brother USB Mass-Storage Upper Filt...
Stopped  Brserid            Brother MFC Serial Port Interface D...
Stopped  BrSerWdm           Brother WDM Serial driver
Stopped  BrUsbMdm           Brother MFC USB Fax Only Modem
Stopped  BrUsbSer           Brother MFC USB Serial WDM Driver
Stopped  BTHMODEM           Bluetooth Serial Communications Driver
Stopped  cdfs               CD/DVD File System Reader
Running  cdrom              CD-ROM Driver
Stopped  circlass           Consumer IR Devices
Running  CLFS               Common Log (CLFS)
Stopped  CmBatt             Microsoft ACPI Control Method Batte...
Stopped  cmdide             cmdide
Running  CNG                CNG
Running  Compbatt           Microsoft Composite Battery Driver
Stopped  CompositeBus       Composite Bus Enumerator Driver
Stopped  crcdisk            Crcdisk Filter Driver
Running  CSC                Offline Files Driver
Running  DfsC               DFS Namespace Client Driver
Running  discache           System Attribute Cache
Running  Disk               Disk Driver
Stopped  drmkaud            Microsoft Trusted Audio Drivers
Stopped  DXGKrnl            LDDM Graphics Subsystem
Stopped  E1G60              Intel(R) PRO/1000 NDIS 6 Adapter Dr...
Stopped  ebdrv              Broadcom NetXtreme II 10 GigE VBD
Stopped  elxstor            elxstor
Stopped  ErrDev             Microsoft Hardware Error Device Driver
Stopped  exfat              exFAT File System Driver
Stopped  fastfat            FAT12/16/32 File System Driver
Stopped  fdc                Floppy Disk Controller Driver
Running  FileInfo           File Information FS MiniFilter
Stopped  Filetrace          Filetrace
Stopped  flpydisk           Floppy Disk Driver
Running  FltMgr             FltMgr
Stopped  FsDepends          File System Dependency Minifilter
Running  fvevol             Bitlocker Drive Encryption Filter D...
Stopped  gagp30kx           Microsoft Generic AGPv3.0 Filter fo...
Stopped  hcw85cir           Hauppauge Consumer Infrared Receiver
Stopped  HdAudAddService    Microsoft 1.1 UAA Function Driver f...
Stopped  HDAudBus           Microsoft UAA Bus Driver for High D...
Stopped  HidBatt            HID UPS Battery Driver
Stopped  HidBth             Microsoft Bluetooth HID Miniport
Stopped  HidIr              Microsoft Infrared HID Driver
Stopped  HidUsb             Microsoft HID Class Driver
Stopped  HpSAMD             HpSAMD
Running  HTTP               HTTP
Running  hwpolicy           Hardware Policy Driver
Stopped  i8042prt           i8042 Keyboard and PS/2 Mouse Port ...
Stopped  iaStorV            iaStorV
Stopped  iirsp              iirsp
Stopped  intelide           intelide
Stopped  intelppm           Intel Processor Driver
Stopped  IpFilterDriver     IP Traffic Filter Driver
Stopped  IPMIDRV            IPMIDRV
Stopped  IPNAT              IP Network Address Translator
Stopped  IRENUM             IR Bus Enumerator
Stopped  isapnp             isapnp
Stopped  iScsiPrt           iScsiPort Driver
Stopped  kbdclass           Keyboard Class Driver
Stopped  kbdhid             Keyboard HID Driver
Running  KSecDD             KSecDD
Running  KSecPkg            KSecPkg
Running  lltdio             Link-Layer Topology Discovery Mappe...
Stopped  LSI_FC             LSI_FC
Stopped  LSI_SAS            LSI_SAS
Stopped  LSI_SAS2           LSI_SAS2
Stopped  LSI_SCSI           LSI_SCSI
Running  luafv              UAC File Virtualization
Stopped  megasas            megasas
Stopped  MegaSR             MegaSR
Stopped  Modem              Modem
Stopped  monitor            Microsoft Monitor Class Function Dr...
Stopped  mouclass           Mouse Class Driver
Stopped  mouhid             Mouse HID Driver
Running  mountmgr           Mount Point Manager
Stopped  mpio               mpio
Running  mpsdrv             Windows Firewall Authorization Driver
Stopped  MRxDAV             WebDav Client Redirector Driver
Running  mrxsmb             SMB MiniRedirector Wrapper and Engine
Running  mrxsmb10           SMB 1.x MiniRedirector
Running  mrxsmb20           SMB 2.0 MiniRedirector
Running  msahci             msahci
Stopped  msdsm              msdsm
Running  Msfs               Msfs
Stopped  mshidkmdf          Pass-through HID to KMDF Filter Driver
Running  msisadrv           msisadrv
Stopped  MSKSSRV            Microsoft Streaming Service Proxy
Stopped  MSPCLOCK           Microsoft Streaming Clock Proxy
Stopped  MSPQM              Microsoft Streaming Quality Manager...
Stopped  MsRPC              MsRPC
Running  mssmbios           Microsoft System Management BIOS Dr...
Stopped  MSTEE              Microsoft Streaming Tee/Sink-to-Sin...
Stopped  MTConfig           Microsoft Input Configuration Driver
Running  Mup                Mup
Stopped  NativeWifiP        NativeWiFi Filter
Running  NDIS               NDIS System Driver
Stopped  NdisCap            NDIS Capture LightWeight Filter
Stopped  NdisTapi           Remote Access NDIS TAPI Driver
Stopped  Ndisuio            NDIS Usermode I/O Protocol
Stopped  NdisWan            Remote Access NDIS WAN Driver
Stopped  NDProxy            NDIS Proxy
Running  NetBIOS            NetBIOS Interface
Running  NetBT              NetBT
Stopped  nfrd960            nfrd960
Running  Npfs               Npfs
Running  nsiproxy           NSI proxy service driver.
Stopped  Ntfs               Ntfs
Running  Null               Null
Stopped  nvraid             nvraid
Stopped  nvstor             nvstor
Stopped  nv_agp             NVIDIA nForce AGP Bus Filter
Stopped  ohci1394           1394 OHCI Compliant Host Controller...
Stopped  Parport            Parallel port driver
Running  partmgr            Partition Manager
Stopped  Parvdm             Parvdm
Running  pci                PCI Bus Driver
Stopped  pciide             pciide
Stopped  pcmcia             pcmcia
Running  pcw                Performance Counters for Windows Dr...
Running  PEAUTH             PEAUTH
Stopped  PptpMiniport       WAN Miniport (PPTP)
Stopped  Processor          Processor Driver
Running  Psched             QoS Packet Scheduler
Stopped  ql2300             ql2300
Stopped  ql40xx             ql40xx
Stopped  QWAVEdrv           QWAVE driver
Stopped  RasAcd             Remote Access Auto Connection Driver
Stopped  RasAgileVpn        WAN Miniport (IKEv2)
Stopped  Rasl2tp            WAN Miniport (L2TP)
Stopped  RasPppoe           Remote Access PPPOE Driver
Stopped  RasSstp            WAN Miniport (SSTP)
Running  rdbss              Redirected Buffering Sub Sysytem
Stopped  rdpbus             Remote Desktop Device Redirector Bu...
Running  RDPCDD             RDPCDD
Running  RDPDR              Terminal Server Device Redirector D...
Running  RDPENCDD           RDP Encoder Mirror Driver
Running  RDPREFMP           Reflector Display Driver used to ga...
Stopped  RDPWD              RDP Winstation Driver
Running  rdyboost           ReadyBoost
Running  rspndr             Link-Layer Topology Discovery Respo...
Stopped  s3cap              s3cap
Stopped  sbp2port           sbp2port
Stopped  scfilter           Smart card PnP Class Filter Driver
Running  secdrv             Security Driver
Stopped  Serenum            Serenum Filter Driver
Stopped  Serial             Serial Port Driver
Stopped  sermouse           Serial Mouse Driver
Stopped  sffdisk            SFF Storage Class Driver
Stopped  sffp_mmc           SFF Storage Protocol Driver for MMC
Stopped  sffp_sd            SFF Storage Protocol Driver for SDBus
Stopped  sfloppy            High-Capacity Floppy Disk Drive
Stopped  sisagp             SIS AGP Bus Filter
Stopped  SiSRaid2           SiSRaid2
Stopped  SiSRaid4           SiSRaid4
Stopped  Smb                Message-oriented TCP/IP and TCP/IPv...
Running  spldr              Security Processor Loader Driver
Running  srv                Server SMB 1.xxx Driver
Running  srv2               Server SMB 2.xxx Driver
Running  srvnet             srvnet
Stopped  stexstor           stexstor
Running  storflt            Disk Virtual Machine Bus Accelerati...
Stopped  storvsc            storvsc
Stopped  swenum             Software Bus Driver
Running  Tcpip              TCP/IP Protocol Driver
Stopped  TCPIP6             Microsoft IPv6 Protocol Driver
Running  tcpipreg           TCP/IP Registry Compatibility
Stopped  TDPIPE             TDPIPE
Stopped  TDTCP              TDTCP
Running  tdx                NetIO Legacy TDI Support Driver
Running  TermDD             Terminal Device Driver
Stopped  tssecsrv           Remote Desktop Services Security Fi...
Stopped  tunnel             Microsoft Tunnel Miniport Adapter D...
Stopped  uagp35             Microsoft AGPv3.5 Filter
Stopped  udfs               udfs
Stopped  uliagpkx           Uli AGP Bus Filter
Stopped  umbus              UMBus Enumerator Driver
Stopped  UmPass             Microsoft UMPass Driver
Stopped  usbccgp            Microsoft USB Generic Parent Driver
Stopped  usbcir             eHome Infrared Receiver (USBCIR)
Stopped  usbehci            Microsoft USB 2.0 Enhanced Host Con...
Stopped  usbhub             Microsoft USB Standard Hub Driver
Stopped  usbohci            Microsoft USB Open Host Controller ...
Stopped  usbprint           Microsoft USB PRINTER Class
Stopped  USBSTOR            USB Mass Storage Driver
Stopped  usbuhci            Microsoft USB Universal Host Contro...
Running  VBoxGuest          VirtualBox Guest Driver
Stopped  VBoxMouse          VirtualBox Guest Mouse Service
Running  VBoxSF             VirtualBox Shared Folders
Stopped  VBoxVideo          VBoxVideo
Running  vdrvroot           Microsoft Virtual Drive Enumerator ...
Stopped  vga                vga
Running  VgaSave            VgaSave
Stopped  vhdmp              vhdmp
Stopped  viaagp             VIA AGP Bus Filter
Stopped  ViaC7              VIA C7 Processor Driver
Stopped  viaide             viaide
Stopped  vmbus              Virtual Machine Bus
Stopped  VMBusHID           VMBusHID
Running  volmgr             Volume Manager Driver
Running  volmgrx            Dynamic Volume Manager
Running  volsnap            Storage volumes
Stopped  vsmraid            vsmraid
Stopped  vwifibus           Virtual WiFi Bus Driver
Stopped  WacomPen           Wacom Serial Pen HID Driver
Stopped  WANARP             Remote Access IP ARP Driver
Running  Wanarpv6           Remote Access IPv6 ARP Driver
Stopped  Wd                 Wd
Running  Wdf01000           Kernel Mode Driver Frameworks service
Running  WfpLwf             WFP Lightweight Filter
Stopped  WIMMount           WIMMount
Stopped  WmiAcpi            Microsoft Windows Management Interf...
Stopped  ws2ifsl            Winsock IFS Driver
Stopped  WudfPf             User Mode Driver Frameworks Platfor...

PS C:\>
```

###### Exercise

- Explore the .Net assemblies and find one which deals with DNS. (–match is your friend)
    - [Dns Class](https://msdn.microsoft.com/en-us/library/system.net.dns(v=vs.110).aspx)- Explore the class and do a DNS lookup using a static method (or otherwise)

```Solution```

- ```Add-Type``` Cmdlet with ```AssemblyName``` ```System.Net```

```PowerShell
PS C:\> Add-Type -AssemblyName System.Net
```

- Check if ```System.Net.Dns``` is loaded

```PowerShell
PS C:\> [System.Net.Dns]

IsPublic IsSerial Name                                     BaseType
-------- -------- ----                                     --------
True     False    Dns                                      System.Object

PS C:\>
```

- List ```Static``` members of ```System.Net.Dns```

```PowerShell
PS C:\> [System.Net.Dns] | Get-Member -Static

   TypeName: System.Net.Dns

Name                  MemberType Definition
----                  ---------- ----------
BeginGetHostAddresses Method     static System.IAsyncResult BeginGetHostAddresses(string hostNameOrAddress, System.AsyncCallback requestCallback, System.Object state)
BeginGetHostByName    Method     static System.IAsyncResult BeginGetHostByName(string hostName, System.AsyncCallback requestCallback, System.Object stateObject)
BeginGetHostEntry     Method     static System.IAsyncResult BeginGetHostEntry(string hostNameOrAddress, System.AsyncCallback requestCallback, System.Object stateObject), static System.IAsyncResult BeginGetHostEntry(ipaddress address, System.AsyncCallback requestCallback, System.Object stateObject)
BeginResolve          Method     static System.IAsyncResult BeginResolve(string hostName, System.AsyncCallback requestCallback, System.Object stateObject)
EndGetHostAddresses   Method     static ipaddress[] EndGetHostAddresses(System.IAsyncResult asyncResult)
EndGetHostByName      Method     static System.Net.IPHostEntry EndGetHostByName(System.IAsyncResult asyncResult)
EndGetHostEntry       Method     static System.Net.IPHostEntry EndGetHostEntry(System.IAsyncResult asyncResult)
EndResolve            Method     static System.Net.IPHostEntry EndResolve(System.IAsyncResult asyncResult)
Equals                Method     static bool Equals(System.Object objA, System.Object objB)
GetHostAddresses      Method     static ipaddress[] GetHostAddresses(string hostNameOrAddress)
GetHostByAddress      Method     static System.Net.IPHostEntry GetHostByAddress(string address), static System.Net.IPHostEntry GetHostByAddress(ipaddress address)
GetHostByName         Method     static System.Net.IPHostEntry GetHostByName(string hostName)
GetHostEntry          Method     static System.Net.IPHostEntry GetHostEntry(string hostNameOrAddress), static System.Net.IPHostEntry GetHostEntry(ipaddress address)
GetHostName           Method     static string GetHostName()
ReferenceEquals       Method     static bool ReferenceEquals(System.Object objA, System.Object objB)
Resolve               Method     static System.Net.IPHostEntry Resolve(string hostName)

PS C:\>
```

```PowerShell
PS C:\> [System.Net.Dns] | Get-Member -Static | Format-List *

TypeName   : System.Net.Dns
Name       : BeginGetHostAddresses
MemberType : Method
Definition : static System.IAsyncResult BeginGetHostAddresses(string hostNameOrAddress, System.AsyncCallback requestCallback, System.Object state)

TypeName   : System.Net.Dns
Name       : BeginGetHostByName
MemberType : Method
Definition : static System.IAsyncResult BeginGetHostByName(string hostName, System.AsyncCallback requestCallback, System.Object stateObject)

TypeName   : System.Net.Dns
Name       : BeginGetHostEntry
MemberType : Method
Definition : static System.IAsyncResult BeginGetHostEntry(string hostNameOrAddress, System.AsyncCallback requestCallback, System.Object stateObject), static System.IAsyncResult BeginGetHostEntry(ipaddress address, System.AsyncCallback requestCallback, System.Object stateObject)

TypeName   : System.Net.Dns
Name       : BeginResolve
MemberType : Method
Definition : static System.IAsyncResult BeginResolve(string hostName, System.AsyncCallback requestCallback, System.Object stateObject)

TypeName   : System.Net.Dns
Name       : EndGetHostAddresses
MemberType : Method
Definition : static ipaddress[] EndGetHostAddresses(System.IAsyncResult asyncResult)

TypeName   : System.Net.Dns
Name       : EndGetHostByName
MemberType : Method
Definition : static System.Net.IPHostEntry EndGetHostByName(System.IAsyncResult asyncResult)

TypeName   : System.Net.Dns
Name       : EndGetHostEntry
MemberType : Method
Definition : static System.Net.IPHostEntry EndGetHostEntry(System.IAsyncResult asyncResult)

TypeName   : System.Net.Dns
Name       : EndResolve
MemberType : Method
Definition : static System.Net.IPHostEntry EndResolve(System.IAsyncResult asyncResult)

TypeName   : System.Net.Dns
Name       : Equals
MemberType : Method
Definition : static bool Equals(System.Object objA, System.Object objB)

TypeName   : System.Net.Dns
Name       : GetHostAddresses
MemberType : Method
Definition : static ipaddress[] GetHostAddresses(string hostNameOrAddress)

TypeName   : System.Net.Dns
Name       : GetHostByAddress
MemberType : Method
Definition : static System.Net.IPHostEntry GetHostByAddress(string address), static System.Net.IPHostEntry GetHostByAddress(ipaddress address)

TypeName   : System.Net.Dns
Name       : GetHostByName
MemberType : Method
Definition : static System.Net.IPHostEntry GetHostByName(string hostName)

TypeName   : System.Net.Dns
Name       : GetHostEntry
MemberType : Method
Definition : static System.Net.IPHostEntry GetHostEntry(string hostNameOrAddress), static System.Net.IPHostEntry GetHostEntry(ipaddress address)

TypeName   : System.Net.Dns
Name       : GetHostName
MemberType : Method
Definition : static string GetHostName()

TypeName   : System.Net.Dns
Name       : ReferenceEquals
MemberType : Method
Definition : static bool ReferenceEquals(System.Object objA, System.Object objB)

TypeName   : System.Net.Dns
Name       : Resolve
MemberType : Method
Definition : static System.Net.IPHostEntry Resolve(string hostName)

PS C:\>
```

- Use ```GetHostAddresses ``` ```Static``` member

```PowerShell
PS C:\> [System.Net.Dns]::GetHostAddresses("www.google.com")

Address           :
AddressFamily     : InterNetworkV6
ScopeId           : 0
IsIPv6Multicast   : False
IsIPv6LinkLocal   : False
IsIPv6SiteLocal   : False
IPAddressToString : 2607:f8b0:4005:809::2004

Address           : 604428716
AddressFamily     : InterNetwork
ScopeId           :
IsIPv6Multicast   : False
IsIPv6LinkLocal   : False
IsIPv6SiteLocal   : False
IPAddressToString : 172.217.6.36

PS C:\>
```