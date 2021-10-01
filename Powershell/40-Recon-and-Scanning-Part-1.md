#### 40. Recon and Scanning Part 1

###### Recon and Scanning

- Host Discovery
- Port-Scan
- Other Recon methods

###### [Nishang](https://github.com/samratashok/nishang) - PowerShell for penetration testing and offensive security

- Import ```Nishang```

```PowerShell
PS C:\Users\Administrator> cd .\Desktop\nishang-master
```

```PowerShell
PS C:\Users\Administrator\Desktop\nishang-master> Import-Module .\nishang.psm1
WARNING: The names of some imported commands from the module 'nishang' include unapproved verbs that might make them less discoverable. To find the commands with unapproved verbs, run the Import-Module
command again with the Verbose parameter. For a list of approved verbs, type Get-Verb.
WARNING: Some imported command names contain one or more of the following restricted characters: # , ( ) {{ }} [ ] & - / \ $ ^ ; : " ' < > | ? @ ` * % + = ~
PS C:\Users\Administrator\Desktop\nishang-master>
```

- List the ```commands``` exported by the module

```PowerShell
PS C:\Users\Administrator\Desktop\nishang-master> Get-Command -Module nishang

CommandType     Name                                               ModuleName
-----------     ----                                               ----------
Function        Add-Exfiltration                                   nishang
Function        Add-Persistence                                    nishang
Function        Add-RegBackdoor                                    nishang
Function        Add-ScrnSaveBackdoor                               nishang
Function        Base64ToString                                     nishang
Function        Check-VM                                           nishang
Function        ConvertTo-ROT13                                    nishang
Function        Copy-VSS                                           nishang
Function        Create-MultipleSessions                            nishang
Function        DNS_TXT_Pwnage                                     nishang
Function        Do-Exfiltration                                    nishang
Function        Download                                           nishang
Function        Download_Execute                                   nishang
Function        Download-Execute-PS                                nishang
Function        Enable-DuplicateToken                              nishang
Function        Execute-Command-MSSQL                              nishang
Function        Execute-DNSTXT-Code                                nishang
Function        Execute-OnTime                                     nishang
Function        ExetoText                                          nishang
Function        FireBuster                                         nishang
Function        FireListener                                       nishang
Function        Get-Information                                    nishang
Function        Get-LsaSecret                                      nishang
Function        Get-PassHashes                                     nishang
Function        Get-PassHints                                      nishang
Function        Get-Unconstrained                                  nishang
Function        Get-WebCredentials                                 nishang
Function        Get-Wlan-Keys                                      nishang
Function        Get-WmiShellOutput                                 nishang
Function        Gupt-Backdoor                                      nishang
Function        HTTP-Backdoor                                      nishang
Function        Invoke-ADSBackdoor                                 nishang
Function        Invoke-AmsiBypass                                  nishang
Function        Invoke-BruteForce                                  nishang
Function        Invoke-CredentialsPhish                            nishang
Function        Invoke-Decode                                      nishang
Function        Invoke-Encode                                      nishang
Function        Invoke-Interceptor                                 nishang
Function        Invoke-JSRatRegsvr                                 nishang
Function        Invoke-JSRatRundll                                 nishang
Function        Invoke-Mimikatz                                    nishang
Function        Invoke-MimikatzWDigestDowngrade                    nishang
Function        Invoke-Mimikittenz                                 nishang
Function        Invoke-NetworkRelay                                nishang
Function        Invoke-PortScan                                    nishang
Function        Invoke-PoshRatHttp                                 nishang
Function        Invoke-PoshRatHttps                                nishang
Function        Invoke-PowerShellIcmp                              nishang
Function        Invoke-PowerShellTcp                               nishang
Function        Invoke-PowerShellUdp                               nishang
Function        Invoke-PowerShellWmi                               nishang
Function        Invoke-Prasadhak                                   nishang
Function        Invoke-PSGcat                                      nishang
Function        Invoke-PsGcatAgent                                 nishang
Function        Invoke-PsUACme                                     nishang
Function        Invoke-SSIDExfil                                   nishang
Function        Out-CHM                                            nishang
Function        Out-DnsTxt                                         nishang
Function        Out-Excel                                          nishang
Function        Out-HTA                                            nishang
Function        Out-Java                                           nishang
Function        Out-JS                                             nishang
Function        Out-RundllCommand                                  nishang
Function        Out-SCF                                            nishang
Function        Out-SCT                                            nishang
Function        Out-Shortcut                                       nishang
Function        Out-WebQuery                                       nishang
Function        Out-Word                                           nishang
Function        Parse_Keys                                         nishang
Function        Remove-Persistence                                 nishang
Function        Remove-PoshRat                                     nishang
Function        Remove-Update                                      nishang
Function        Run-EXEonRemote                                    nishang
Function        Show-TargetScreen                                  nishang
Function        Speak                                              nishang
Function        Start-CaptureServer                                nishang
Function        StringtoBase64                                     nishang
Function        TexttoEXE                                          nishang

PS C:\Users\Administrator\Desktop\nishang-master>
```

- ```Port Scan```

```PowerShell
PS C:\Users\Administrator\Desktop\nishang-master> Get-Help Invoke-PortScan -Examples

NAME
    Invoke-PortScan

SYNOPSIS
    Nihsang payload which Scan IP-Addresses, Ports and HostNames

    -------------------------- EXAMPLE 1 --------------------------

    PS >Invoke-PortScan -StartAddress 192.168.0.1 -EndAddress 192.168.0.254







    -------------------------- EXAMPLE 2 --------------------------

    PS >Invoke-PortScan -StartAddress 192.168.0.1 -EndAddress 192.168.0.254 -ResolveHost







    -------------------------- EXAMPLE 3 --------------------------

    PS >Invoke-PortScan -StartAddress 192.168.0.1 -EndAddress 192.168.0.254 -ResolveHost -ScanPort


    Use above to do a port scan on default ports.




    -------------------------- EXAMPLE 4 --------------------------

    PS >Invoke-PortScan -StartAddress 192.168.0.1 -EndAddress 192.168.0.254 -ResolveHost -ScanPort -TimeOut 500







    -------------------------- EXAMPLE 5 --------------------------

    PS >Invoke-PortScan -StartAddress 192.168.0.1 -EndAddress 192.168.10.254 -ResolveHost -ScanPort -Port 80

PS C:\Users\Administrator\Desktop\nishang-master>
```

```PowerShell
PS C:\Users\Administrator\Desktop\nishang-master> Invoke-PortScan -StartAddress 10.0.0.1 -EndAddress 10.0.0.255 -ResolveHost

IPAddress                                                           HostName                                                            Ports
---------                                                           --------                                                            -----
10.0.0.1
10.0.0.95                                                           MACBOOKPRO-5ED1
10.0.0.129                                                          John-PC.pfpt.com
10.0.0.233                                                          WIN-2012-DC.pfpt.com
10.0.0.254                                                          WIN-2012-DC.pfpt.com

PS C:\Users\Administrator\Desktop\nishang-master>
```

```PowerShell
PS C:\Users\Administrator\Desktop\nishang-master> Invoke-PortScan -StartAddress 10.0.0.1 -EndAddress 10.0.0.255 -ResolveHost -ScanPort

IPAddress                                                           HostName                                                            Ports
---------                                                           --------                                                            -----
10.0.0.1                                                                                                                                {53, 80, 443}
10.0.0.95                                                           MACBOOKPRO-5ED1                                                     {}
10.0.0.129                                                          John-PC.pfpt.com                                                    {139, 445, 3389}
10.0.0.233                                                          WIN-2012-DC.pfpt.com                                                {53, 139, 389, 445...}
10.0.0.254                                                          WIN-2012-DC.pfpt.com                                                {111}

PS C:\Users\Administrator\Desktop\nishang-master>
```

###### [Posh-SecMod](https://github.com/darkoperator/Posh-SecMod) - PowerShell Module with Security cmdlets for security work

- Import ```Posh-SecMod```

```PowerShell
PS C:\Users\Administrator> cd .\Desktop
PS C:\Users\Administrator\Desktop> cd .\Posh-SecMod-master
```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-SecMod-master> Import-Module .\Posh-SecMod.psd1
```

- List the ```commands``` exported by the module

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-SecMod-master> Get-Command -Module Posh-SecMod

CommandType     Name                                               ModuleName
-----------     ----                                               ----------
Function        Add-Zip                                            Posh-SecMod
Function        Compress-PostScript                                Posh-SecMod
Function        Confirm-IsAdmin                                    Posh-SecMod
Function        Connect-DBSQLite3                                  Posh-SecMod
Function        ConvertTo-InAddrARPA                               Posh-SecMod
Function        ConvertTo-PostBase64Command                        Posh-SecMod
Function        ConvertTo-PostFiletoHex                            Posh-SecMod
Function        ConvertTo-PostHextoFile                            Posh-SecMod
Function        Expand-Zip                                         Posh-SecMod
Function        Get-ApplicationHost                                Posh-SecMod
Function        Get-AuditDSComputerAccount                         Posh-SecMod
Function        Get-AuditDSDeletedAccount                          Posh-SecMod
Function        Get-AuditDSDisabledUserAcount                      Posh-SecMod
Function        Get-AuditDSLockedUserAcount                        Posh-SecMod
Function        Get-AuditDSUserAcount                              Posh-SecMod
Function        Get-AuditFileTimeStamp                             Posh-SecMod
Function        Get-AuditInstallSoftware                           Posh-SecMod
Function        Get-AuditLogedOnSessions                           Posh-SecMod
Function        Get-AuditPrefechList                               Posh-SecMod
Function        Get-AuditRegKeyLastWriteTime                       Posh-SecMod
Function        Get-ComObject                                      Posh-SecMod
Function        Get-DBSQLite3Connection                            Posh-SecMod
Function        Get-FileHash                                       Posh-SecMod
Function        Get-LogDateString                                  Posh-SecMod
Function        Get-MDNSRecords                                    Posh-SecMod
Function        Get-PoshSecModVersion                              Posh-SecMod
Function        Get-PostCopyNTDS                                   Posh-SecMod
Function        Get-PostHashdumpScript                             Posh-SecMod
Function        Get-PostReverTCPShell                              Posh-SecMod
Function        Get-RegKeys                                        Posh-SecMod
Function        Get-RegKeySecurityDescriptor                       Posh-SecMod
Function        Get-RegValue                                       Posh-SecMod
Function        Get-RegValues                                      Posh-SecMod
Function        Get-SystemDNSServer                                Posh-SecMod
Function        Get-Webconfig                                      Posh-SecMod
Function        Get-WebFile                                        Posh-SecMod
Function        Get-Whois                                          Posh-SecMod
Function        Get-Zip                                            Posh-SecMod
Function        Get-ZipChildItems_Recurse                          Posh-SecMod
Function        Import-DNSReconXML                                 Posh-SecMod
Function        Import-NmapXML                                     Posh-SecMod
Function        Invoke-ARPScan                                     Posh-SecMod
Function        Invoke-DBSQLite3Query                              Posh-SecMod
Function        Invoke-EnumSRVRecords                              Posh-SecMod
Function        Invoke-PingScan                                    Posh-SecMod
Function        Invoke-PortScan                                    Posh-SecMod
Function        Invoke-ReverseDNSLookup                            Posh-SecMod
Function        New-DBSQLConnectionString                          Posh-SecMod
Function        New-IPRange                                        Posh-SecMod
Function        New-IPv4Range                                      Posh-SecMod
Function        New-IPv4RangeFromCIDR                              Posh-SecMod
Function        New-PostDownloadExecutePE                          Posh-SecMod
Function        New-PostDownloadExecuteScript                      Posh-SecMod
Function        New-RegKey                                         Posh-SecMod
Function        New-Zip                                            Posh-SecMod
Function        Remove-DBSQLite3Connection                         Posh-SecMod
Function        Remove-RegKey                                      Posh-SecMod
Function        Remove-RegValue                                    Posh-SecMod
Function        Resolve-DNSRecord                                  Posh-SecMod
Function        Resolve-HostRecord                                 Posh-SecMod
Function        Set-RegValue                                       Posh-SecMod
Function        Start-PostRemoteProcess                            Posh-SecMod
Function        Test-RegKeyAccess                                  Posh-SecMod
Function        Update-SysinternalsTools                           Posh-SecMod

PS C:\Users\Administrator\Desktop\Posh-SecMod-master>
```

- Host Discovery - ```ARP Scan```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-SecMod-master> Get-Help Invoke-ARPScan -Examples

NAME
    Invoke-ARPScan

SYNOPSIS
    Performs an ARP scan against a given range of IPv4 IP Addresses.

    -------------------------- EXAMPLE 1 --------------------------

    C:\PS>Invoke an ARP Scan against a range of IPs specified in CIDR Format


    PS C:\> Invoke-ARPScan -CIDR 172.20.10.1/24

     MAC                                                       Address
     ---                                                       -------
     14:10:9F:D5:1A:BF                                         172.20.10.2
     00:0C:29:93:10:B5                                         172.20.10.3
     00:0C:29:93:10:B5                                         172.20.10.15

PS C:\Users\Administrator\Desktop\Posh-SecMod-master>
```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-SecMod-master> Invoke-ARPScan -CIDR 10.0.0.1/24

MAC                                                                                                   Address
---                                                                                                   -------
BC:9F:EF:69:35:19                                                                                     10.0.0.19
40:F0:2F:57:6C:13                                                                                     10.0.0.53
00:9A:CD:C9:77:54                                                                                     10.0.0.61
08:00:27:CA:01:8E                                                                                     10.0.0.94
F4:0F:24:33:5E:D1                                                                                     10.0.0.95
C8:21:58:31:F6:73                                                                                     10.0.0.173
08:00:27:7C:C3:C9                                                                                     10.0.0.233
E4:A7:A0:09:3A:12                                                                                     10.0.0.234
00:05:04:03:02:01                                                                                     10.0.0.254

PS C:\Users\Administrator\Desktop\Posh-SecMod-master>
```

- Enumerate ```DNS SRV Records```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-SecMod-master> Get-Help Invoke-EnumSRVRecords -Examples

NAME
    Invoke-EnumSRVRecords

SYNOPSIS
    Enumerates common DNS SRV Records for a given domain.

    -------------------------- EXAMPLE 1 --------------------------

    PS C:\>Invoke-EnumSRVRecords -Domain microsoft.com


    Type     : SRV
     Name     : _sip._tls.microsoft.com
     Port     : 443
     Priority : 0
     Target   : sip.microsoft.com.
     Address   : @{Name=sip.microsoft.com; Type=A; Address=65.55.30.130}

     Type     : SRV
     Name     : _sipfederationtls._tcp.microsoft.com
     Port     : 5061
     Priority : 0
     Target   : sipfed.microsoft.com.
     Address   : @{Name=sipfed.microsoft.com; Type=A; Address=65.55.30.130}

     Type     : SRV
     Name     : _xmpp-server._tcp.microsoft.com
     Port     : 5269
     Priority : 0
     Target   : sipdog3.microsoft.com.
     Address   : @{Name=sipdog3.microsoft.com; Type=A; Address=131.107.1.47}

PS C:\Users\Administrator\Desktop\Posh-SecMod-master>
```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-SecMod-master> Invoke-EnumSRVRecords -Domain google.com

Type     : SRV
Name     : _ldap._tcp.google.com
Port     : 389
Priority : 0
Target   : ldap.google.com.
Address  : @{Name=ldap.google.com; Type=A; Address=216.239.32.58}

Type     : SRV
Name     : _jabber._tcp.google.com
Port     : 5269
Priority : 0
Target   : alt2.xmpp-server.l.google.com.
Address  : @{Name=alt2.xmpp-server.l.google.com; Type=A; Address=173.194.219.125}

Type     : SRV
Name     : _jabber._tcp.google.com
Port     : 5269
Priority : 0
Target   : alt1.xmpp-server.l.google.com.
Address  : @{Name=alt1.xmpp-server.l.google.com; Type=A; Address=64.233.181.125}

Type     : SRV
Name     : _jabber._tcp.google.com
Port     : 5269
Priority : 0
Target   : alt3.xmpp-server.l.google.com.
Address  : @{Name=alt3.xmpp-server.l.google.com; Type=A; Address=74.125.192.125}

Type     : SRV
Name     : _jabber._tcp.google.com
Port     : 5269
Priority : 0
Target   : alt4.xmpp-server.l.google.com.
Address  : @{Name=alt4.xmpp-server.l.google.com; Type=A; Address=173.194.214.125}

Type     : SRV
Name     : _jabber._tcp.google.com
Port     : 5269
Priority : 0
Target   : xmpp-server.l.google.com.
Address  : @{Name=xmpp-server.l.google.com; Type=A; Address=74.125.135.125}

Type     : SRV
Name     : _xmpp-server._tcp.google.com
Port     : 5269
Priority : 0
Target   : xmpp-server.l.google.com.
Address  : @{Name=xmpp-server.l.google.com; Type=A; Address=74.125.135.125}

Type     : SRV
Name     : _xmpp-server._tcp.google.com
Port     : 5269
Priority : 0
Target   : alt2.xmpp-server.l.google.com.
Address  : @{Name=alt2.xmpp-server.l.google.com; Type=A; Address=173.194.219.125}

Type     : SRV
Name     : _xmpp-server._tcp.google.com
Port     : 5269
Priority : 0
Target   : alt4.xmpp-server.l.google.com.
Address  : @{Name=alt4.xmpp-server.l.google.com; Type=A; Address=173.194.214.125}

Type     : SRV
Name     : _xmpp-server._tcp.google.com
Port     : 5269
Priority : 0
Target   : alt3.xmpp-server.l.google.com.
Address  : @{Name=alt3.xmpp-server.l.google.com; Type=A; Address=74.125.192.125}

Type     : SRV
Name     : _xmpp-server._tcp.google.com
Port     : 5269
Priority : 0
Target   : alt1.xmpp-server.l.google.com.
Address  : @{Name=alt1.xmpp-server.l.google.com; Type=A; Address=64.233.181.125}

Type     : SRV
Name     : _xmpp-client._tcp.google.com
Port     : 5222
Priority : 0
Target   : alt1.xmpp.l.google.com.
Address  : {@{Name=alt1.xmpp.l.google.com; Type=A; Address=64.233.181.125}, @{Name=alt1.xmpp.l.google.com; Type=AAAA; Address=2607:f8b0:4001:c09::7d}}

Type     : SRV
Name     : _xmpp-client._tcp.google.com
Port     : 5222
Priority : 0
Target   : xmpp.l.google.com.
Address  : {@{Name=xmpp.l.google.com; Type=A; Address=74.125.135.125}, @{Name=xmpp.l.google.com; Type=AAAA; Address=2607:f8b0:400e:c01::7d}}

Type     : SRV
Name     : _xmpp-client._tcp.google.com
Port     : 5222
Priority : 0
Target   : alt3.xmpp.l.google.com.
Address  : {@{Name=alt3.xmpp.l.google.com; Type=A; Address=74.125.192.125}, @{Name=alt3.xmpp.l.google.com; Type=AAAA; Address=2607:f8b0:400d:c00::7d}}

Type     : SRV
Name     : _xmpp-client._tcp.google.com
Port     : 5222
Priority : 0
Target   : alt4.xmpp.l.google.com.
Address  : {@{Name=alt4.xmpp.l.google.com; Type=A; Address=173.194.214.125}, @{Name=alt4.xmpp.l.google.com; Type=AAAA; Address=2607:f8b0:400c:c0b::7d}}

Type     : SRV
Name     : _xmpp-client._tcp.google.com
Port     : 5222
Priority : 0
Target   : alt2.xmpp.l.google.com.
Address  : {@{Name=alt2.xmpp.l.google.com; Type=A; Address=173.194.219.125}, @{Name=alt2.xmpp.l.google.com; Type=AAAA; Address=2607:f8b0:4002:c03::7d}}

Type     : SRV
Name     : _jabber-client._tcp.google.com
Port     : 5222
Priority : 0
Target   : xmpp.l.google.com.
Address  : {@{Name=xmpp.l.google.com; Type=A; Address=74.125.135.125}, @{Name=xmpp.l.google.com; Type=AAAA; Address=2607:f8b0:400e:c01::7d}}

Type     : SRV
Name     : _jabber-client._tcp.google.com
Port     : 5222
Priority : 0
Target   : alt1.xmpp.l.google.com.
Address  : {@{Name=alt1.xmpp.l.google.com; Type=A; Address=64.233.181.125}, @{Name=alt1.xmpp.l.google.com; Type=AAAA; Address=2607:f8b0:4001:c09::7d}}

Type     : SRV
Name     : _jabber-client._tcp.google.com
Port     : 5222
Priority : 0
Target   : alt4.xmpp.l.google.com.
Address  : {@{Name=alt4.xmpp.l.google.com; Type=A; Address=173.194.214.125}, @{Name=alt4.xmpp.l.google.com; Type=AAAA; Address=2607:f8b0:400c:c0b::7d}}

Type     : SRV
Name     : _jabber-client._tcp.google.com
Port     : 5222
Priority : 0
Target   : alt2.xmpp.l.google.com.
Address  : {@{Name=alt2.xmpp.l.google.com; Type=A; Address=173.194.219.125}, @{Name=alt2.xmpp.l.google.com; Type=AAAA; Address=2607:f8b0:4002:c03::7d}}

Type     : SRV
Name     : _jabber-client._tcp.google.com
Port     : 5222
Priority : 0
Target   : alt3.xmpp.l.google.com.
Address  : {@{Name=alt3.xmpp.l.google.com; Type=A; Address=74.125.192.125}, @{Name=alt3.xmpp.l.google.com; Type=AAAA; Address=2607:f8b0:400d:c00::7d}}

PS C:\Users\Administrator\Desktop\Posh-SecMod-master>
```

###### [PowerSploit](https://github.com/PowerShellMafia/PowerSploit) - A PowerShell Post-Exploitation Framework

- Import ```PowerSploit```

```PowerShell
PS C:\Users\Administrator> cd .\Desktop\PowerSploit-master
```

```PowerShell
PS C:\Users\Administrator\Desktop\PowerSploit-master> Import-Module .\PowerSploit.psd1
```

- List the ```commands``` exported by the module

```PowerShell
PS C:\Users\Administrator\Desktop\PowerSploit-master> Get-Command -Module PowerSploit

CommandType     Name                                               ModuleName
-----------     ----                                               ----------
Function        Add-NetUser                                        PowerSploit
Function        Add-ObjectAcl                                      PowerSploit
Function        Add-Persistence                                    PowerSploit
Function        Add-ServiceDacl                                    PowerSploit
Function        Find-AVSignature                                   PowerSploit
Function        Find-ComputerField                                 PowerSploit
Function        Find-ForeignGroup                                  PowerSploit
Function        Find-ForeignUser                                   PowerSploit
Function        Find-GPOComputerAdmin                              PowerSploit
Function        Find-GPOLocation                                   PowerSploit
Function        Find-InterestingFile                               PowerSploit
Function        Find-LocalAdminAccess                              PowerSploit
Function        Find-ManagedSecurityGroups                         PowerSploit
Function        Find-PathDLLHijack                                 PowerSploit
Function        Find-ProcessDLLHijack                              PowerSploit
Function        Get-ADObject                                       PowerSploit
Function        Get-ApplicationHost                                PowerSploit
Function        Get-ComputerDetails                                PowerSploit
Function        Get-ComputerProperty                               PowerSploit
Function        Get-CurrentUserTokenGroupSid                       PowerSploit
Function        Get-DFSshare                                       PowerSploit
Function        Get-DomainPolicy                                   PowerSploit
Function        Get-ExploitableSystem                              PowerSploit
Function        Get-GPPPassword                                    PowerSploit
Function        Get-HttpStatus                                     PowerSploit
Function        Get-Keystrokes                                     PowerSploit
Function        Get-ModifiablePath                                 PowerSploit
Function        Get-ModifiableRegistryAutoRun                      PowerSploit
Function        Get-ModifiableScheduledTaskFile                    PowerSploit
Function        Get-ModifiableService                              PowerSploit
Function        Get-ModifiableServiceFile                          PowerSploit
Function        Get-NetComputer                                    PowerSploit
Function        Get-NetDomainTrust                                 PowerSploit
Function        Get-NetFileServer                                  PowerSploit
Function        Get-NetForestTrust                                 PowerSploit
Function        Get-NetGPO                                         PowerSploit
Function        Get-NetGPOGroup                                    PowerSploit
Function        Get-NetGroup                                       PowerSploit
Function        Get-NetGroupMember                                 PowerSploit
Function        Get-NetLocalGroup                                  PowerSploit
Function        Get-NetOU                                          PowerSploit
Function        Get-NetSite                                        PowerSploit
Function        Get-NetSubnet                                      PowerSploit
Function        Get-NetUser                                        PowerSploit
Function        Get-ObjectAcl                                      PowerSploit
Function        Get-PathAcl                                        PowerSploit
Function        Get-RegistryAlwaysInstallElevated                  PowerSploit
Function        Get-RegistryAutoLogon                              PowerSploit
Function        Get-SecurityPackages                               PowerSploit
Function        Get-ServiceDetail                                  PowerSploit
Function        Get-ServiceUnquoted                                PowerSploit
Function        Get-SiteListPassword                               PowerSploit
Function        Get-System                                         PowerSploit
Function        Get-TimedScreenshot                                PowerSploit
Function        Get-UnattendedInstallFile                          PowerSploit
Function        Get-UserProperty                                   PowerSploit
Function        Get-VaultCredential                                PowerSploit
Function        Get-VolumeShadowCopy                               PowerSploit
Function        Get-WebConfig                                      PowerSploit
Function        Install-ServiceBinary                              PowerSploit
Function        Install-SSP                                        PowerSploit
Function        Invoke-ACLScanner                                  PowerSploit
Function        Invoke-AllChecks                                   PowerSploit
Function        Invoke-CredentialInjection                         PowerSploit
Function        Invoke-DllInjection                                PowerSploit
Function        Invoke-EnumerateLocalAdmin                         PowerSploit
Function        Invoke-EventHunter                                 PowerSploit
Function        Invoke-FileFinder                                  PowerSploit
Function        Invoke-MapDomainTrust                              PowerSploit
Function        Invoke-Mimikatz                                    PowerSploit
Function        Invoke-NinjaCopy                                   PowerSploit
Function        Invoke-Portscan                                    PowerSploit
Function        Invoke-ProcessHunter                               PowerSploit
Function        Invoke-ReflectivePEInjection                       PowerSploit
Function        Invoke-ReverseDnsLookup                            PowerSploit
Function        Invoke-ServiceAbuse                                PowerSploit
Function        Invoke-ShareFinder                                 PowerSploit
Function        Invoke-Shellcode                                   PowerSploit
Function        Invoke-TokenManipulation                           PowerSploit
Function        Invoke-UserHunter                                  PowerSploit
Function        Invoke-WmiCommand                                  PowerSploit
Function        Mount-VolumeShadowCopy                             PowerSploit
Function        New-ElevatedPersistenceOption                      PowerSploit
Function        New-UserPersistenceOption                          PowerSploit
Function        New-VolumeShadowCopy                               PowerSploit
Function        Out-CompressedDll                                  PowerSploit
Function        Out-EncodedCommand                                 PowerSploit
Function        Out-EncryptedScript                                PowerSploit
Function        Out-Minidump                                       PowerSploit
Function        Remove-Comments                                    PowerSploit
Function        Remove-VolumeShadowCopy                            PowerSploit
Function        Restore-ServiceBinary                              PowerSploit
Function        Set-ADObject                                       PowerSploit
Function        Set-CriticalProcess                                PowerSploit
Function        Set-MasterBootRecord                               PowerSploit
Function        Set-ServiceBinPath                                 PowerSploit
Function        Test-ServiceDaclPermission                         PowerSploit
Function        Write-HijackDll                                    PowerSploit
Function        Write-ServiceBinary                                PowerSploit
Function        Write-UserAddMSI                                   PowerSploit
Filter          Convert-NameToSid                                  PowerSploit
Filter          Convert-SidToName                                  PowerSploit
Filter          Find-UserField                                     PowerSploit
Filter          Get-CachedRDPConnection                            PowerSploit
Filter          Get-LastLoggedOn                                   PowerSploit
Filter          Get-NetDomain                                      PowerSploit
Filter          Get-NetDomainController                            PowerSploit
Filter          Get-NetForest                                      PowerSploit
Filter          Get-NetForestCatalog                               PowerSploit
Filter          Get-NetForestDomain                                PowerSploit
Filter          Get-NetLoggedon                                    PowerSploit
Filter          Get-NetProcess                                     PowerSploit
Filter          Get-NetRDPSession                                  PowerSploit
Filter          Get-NetSession                                     PowerSploit
Filter          Get-NetShare                                       PowerSploit
Filter          Get-Proxy                                          PowerSploit
Filter          Get-UserEvent                                      PowerSploit
Filter          Invoke-CheckLocalAdminAccess                       PowerSploit

PS C:\Users\Administrator\Desktop\PowerSploit-master>
```

- ```Port Scan```

```PowerShell
PS C:\Users\Administrator\Desktop\PowerSploit-master> Get-Help Invoke-Portscan -Examples

NAME
    Invoke-Portscan

SYNOPSIS
    Simple portscan module

    PowerSploit Function: Invoke-Portscan
    Author: Rich Lundeen (http://webstersProdigy.net)
    License: BSD 3-Clause
    Required Dependencies: None
    Optional Dependencies: None

    -------------------------- EXAMPLE 1 --------------------------

    C:\PS>Invoke-Portscan -Hosts "webstersprodigy.net,google.com,microsoft.com" -TopPorts 50


    Description
    -----------
    Scans the top 50 ports for hosts found for webstersprodigy.net,google.com, and microsoft.com




    -------------------------- EXAMPLE 2 --------------------------

    C:\PS>echo webstersprodigy.net | Invoke-Portscan -oG test.gnmap -f -ports "80,443,8080"


    Description
    -----------
    Does a portscan of "webstersprodigy.net", and writes a greppable output file




    -------------------------- EXAMPLE 3 --------------------------

    C:\PS>Invoke-Portscan -Hosts 192.168.1.1/24 -T 4 -TopPorts 25 -oA localnet


    Description
    -----------
    Scans the top 20 ports for hosts found in the 192.168.1.1/24 range, outputs all file formats

PS C:\Users\Administrator\Desktop\PowerSploit-master>
```

```PowerShell
PS C:\Users\Administrator\Desktop\PowerSploit-master> Invoke-Portscan -Hosts "google.com"

Hostname      : google.com
alive         : True
openPorts     : {80, 443}
closedPorts   : {}
filteredPorts : {79, 88, 2049, 8081...}
finishTime    : 7/9/2017 6:05:12 PM

PS C:\Users\Administrator\Desktop\PowerSploit-master>
```

```PowerShell
PS C:\Users\Administrator\Desktop\PowerSploit-master> $result = Invoke-Portscan -Hosts "google.com"
```

```PowerShell
PS C:\Users\Administrator\Desktop\PowerSploit-master> $result | Select-Object -ExpandProperty FilteredPorts
5900
993
995
111
1723
22
8080
3306
135
53
143
139
445
110
3389
21
23
32768
8000
8443
2000
1026
179
6001
81
113
548
1720
1025
79
88
2049
8081
49153
631
5631
5000
646
5666
1027
49154
8008
515
2001
49152
1433
26
554
PS C:\Users\Administrator\Desktop\PowerSploit-master>
```
