#### 41. Recon and Scanning Part 2

###### [Posh-Shodan](https://github.com/darkoperator/Posh-Shodan)

- Import [```Posh-Shodan```](http://www.powershellmagazine.com/2014/07/15/posh-shodan-module-for-the-shodan-service/)

```PowerShell
PS C:\Users\Administrator> cd .\Desktop\Posh-Shodan-master
```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-Shodan-master> Import-Module .\Posh-Shodan.psd1
```

- List the ```commands``` exported by the module

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-Shodan-master> Get-Command -Module Posh-Shodan

CommandType     Name                                               ModuleName
-----------     ----                                               ----------
Function        Get-ShodanAPIInfo                                  Posh-Shodan
Function        Get-ShodanDNSResolve                               Posh-Shodan
Function        Get-ShodanDNSReverse                               Posh-Shodan
Function        Get-ShodanHostService                              Posh-Shodan
Function        Get-ShodanMyIP                                     Posh-Shodan
Function        Get-ShodanService                                  Posh-Shodan
Function        Measure-ShodanExploit                              Posh-Shodan
Function        Measure-ShodanHost                                 Posh-Shodan
Function        Read-ShodanAPIKey                                  Posh-Shodan
Function        Search-ShodanExploit                               Posh-Shodan
Function        Search-ShodanHost                                  Posh-Shodan
Function        Set-ShodanAPIKey                                   Posh-Shodan

PS C:\Users\Administrator\Desktop\Posh-Shodan-master>
```

- List ```help``` topics for ```Shodan```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-Shodan-master> help *shodan*

Name                              Category  Module                    Synopsis
----                              --------  ------                    --------
Get-ShodanAPIInfo                 Function  Posh-Shodan               Get features and information for a given API Key.
Get-ShodanDNSResolve              Function  Posh-Shodan               Look up the IP address for the provided list of hostnames.
Get-ShodanDNSReverse              Function  Posh-Shodan               Look up the hostnames that have been defined for the given list of IP addresses.
Get-ShodanHostService             Function  Posh-Shodan
Get-ShodanMyIP                    Function  Posh-Shodan               Get your current IP address as seen from the Internet.
Get-ShodanService                 Function  Posh-Shodan
Measure-ShodanExploit             Function  Posh-Shodan               Search across a variety of data sources for exploits and get summary information using Shodan.
Measure-ShodanHost                Function  Posh-Shodan               Returns the total number of results that matched the query and any facet information that was requested.
Read-ShodanAPIKey                 Function  Posh-Shodan               Read from disk the saved Shodan API Key
Search-ShodanExploit              Function  Posh-Shodan               Search across a variety of data sources for exploits. using Shodan
Search-ShodanHost                 Function  Posh-Shodan               Search Shodan using the same query syntax as the website and use facets to get summary information for different properties.
Set-ShodanAPIKey                  Function  Posh-Shodan               Set a default Shodan API key for use by Posh-Shodan module.
about_Shodan_Host_Search_Facets   HelpFile                            Describes the search facets that can be used when performing a search for
about_Shodan_Host_Search_Filters  HelpFile                            Describes the search filters that can be used when performing a search for

PS C:\Users\Administrator\Desktop\Posh-Shodan-master>
```

- Set the [```Shodan API Key```](https://account.shodan.io/)

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-Shodan-master> Set-ShodanAPIKey -APIKey Y2DmqAThPzLFP1b1Ubanif3YGaqsoQlx

cmdlet Set-ShodanAPIKey at command pipeline position 1
Supply values for the following parameters:
MasterPassword: ****
PS C:\Users\Administrator\Desktop\Posh-Shodan-master>
```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-Shodan-master> Read-ShodanAPIKey

cmdlet Read-ShodanAPIKey at command pipeline position 1
Supply values for the following parameters:
MasterPassword: ****
PS C:\Users\Administrator\Desktop\Posh-Shodan-master>
```

- ```Shodan API Info```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-Shodan-master> Get-ShodanAPIInfo

Unlocked_Left : 0
Telnet        : False
Plan          : oss
HTTPS         : False
Unlocked      : False

PS C:\Users\Administrator\Desktop\Posh-Shodan-master>
```

- ```Shodan DNS Resolution```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-Shodan-master> Get-ShodanDNSResolve -Hostname google.com

google.com
----------
216.58.194.174

PS C:\Users\Administrator\Desktop\Posh-Shodan-master>
```

- ```Measure all Shodan Hosts```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-Shodan-master> Measure-ShodanHost -Query "default password"

Total  : 80630
Facets :

PS C:\Users\Administrator\Desktop\Posh-Shodan-master>
```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-Shodan-master> Measure-ShodanHost -Query "RDP"

Total  : 947
Facets :

PS C:\Users\Administrator\Desktop\Posh-Shodan-master>
```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-Shodan-master> Measure-ShodanHost -Query "phpmyadmin"

Total  : 36173
Facets :

PS C:\Users\Administrator\Desktop\Posh-Shodan-master>
```

- List all ```Shodan services```

```PowerShell
PS C:\Users\Administrator\Desktop\Posh-Shodan-master> Get-ShodanService

623   : IPMI
626   : serialnumbered
5985  : WinRM 2.0
2455  : Codesys
5560  : Oracle HTTP
8098  : Riak Web Interface
9000  : NAS Web Interfaces
7071  : Zimbra HTTP
62078 : iPhone
137   : NetBIOS
3000  : ntop
67    : DHCP
8090  : Insteon Hub
2087  : WHM + SSL
9151  : Tor control port
1900  : UPnP
9200  : ElasticSearch
2323  : Telnet (2323)
25    : SMTP
3128  : Squid Proxy
5353  : mDNS
21    : FTP
22    : SSH
23    : Telnet
44818 : EtherNetIP
10000 : Webmin
4949  : Munin
3790  : Metasploit
3388  : RDP (3388)
8139  : Puppet Agent
2404  : IEC-104
1723  : PPTP
2152  : GPRS Tunneling Protocol
8089  : Splunk
502   : Modbus
5986  : WinRM 2.0 + SSL
500   : IKE
995   : POP3 + SSL
631   : CUPS
5060  : SIP
993   : IMAP + SSL
992   : Telnet + SSL
465   : SMTP + SSL
8140  : Puppet Master
2628  : Dictionary
18245 : General Electric SRTP
2123  : GPRS Tunneling Protocol
32764 : Router backdoor
8333  : Bitcoin
123   : NTP
20000 : DNP3
1911  : Tridium Fox
129   : Password generator protocol
161   : SNMP
9981  : HTS/ tvheadend
11    : Systat
9999  : Telnet (Lantronix)
13    : Daytime
15    : Netstat
1023  : Telnet (1023)
17    : Quote of the day
20547 : ProConOS
19    : Character Generator
5222  : XMPP
4443  : Symantec Data Center Security
16010 : Hbase
8181  : HTTP (8181)
53    : DNS
6666  : Voldemort
5901  : VNC (5901)
9944  : Pipeline Pilot
4022  : Udpxy
28017 : MongoDB Web Interface
2067  : DLSW
64738 : Mumble server
5007  : Mitsubishi MELSEC-Q
10001 : Automated Tank Gauge
9600  : OMRON FINS
2086  : WHM
7657  : HTTP (7657)
4369  : Erlang Port Mapper Daemon
1200  : Codesys
9100  : Printer Job Language
1604  : Citrix
9051  : Tor control port
3306  : MySQL
88    : Kerberos
111   : Portmap
110   : POP3
25565 : Minecraft
8443  : HTTPS (8443)
82    : HTTP (82)
83    : HTTP (83)
80    : HTTP
81    : HTTP (81)
119   : NNTP
84    : HTTP (84)
5006  : Mitsubishi MELSEC-Q
3386  : GPRS Tunneling Protocol
8888  : AndroMouse
4040  : Chef
9943  : Pipeline Pilot + SSL
9160  : Cassandra
8069  : OpenERP
5094  : HART-IP
3479  : 2-Wire RPC
1962  : PCWorx
3389  : RDP
7777  : Oracle
5432  : PostgreSQL
18246 : General Electric SRTP
7     : Echo
523   : IBM DB2
50100 : Telnet
49152 : Supermicro Web Interface
1234  : Udpxy
3780  : Nexpose
5001  : Synology
5000  : Synology
771   : RealPort
143   : IMAP
443   : HTTPS
55553 : Metasploit (55553)
5008  : NetMobility
5357  : Microsoft-HTTPAPI/2.0
55554 : Metasploit (55554)
445   : SMB
11211 : MemCache
4500  : IKE-NAT-T
8129  : Snapstream
8834  : Nessus
102   : Siemens S7
389   : LDAP
8000  : Qconn
79    : Finger
47808 : BACnet
1434  : MS-SQL Monitor
8087  : Riak Protobuf
8080  : HTTP (8080)
6000  : X Windows
2082  : cPanel
2083  : cPanel + SSL
27017 : MongoDB
6001  : X Windows (6001)
37    : rdate
789   : Red Lion
5632  : PC Anywhere
4911  : Tridium Fox + SSL
6379  : Redis
1471  : Hak5 Pineapple
2375  : Docker
2376  : Docker + SSL
515   : Line Printer Daemon
5900  : VNC
10243 : Microsoft-HTTPAPI/2.0
7547  : Modem Web Interface

PS C:\Users\Administrator\Desktop\Posh-Shodan-master>
```

###### [PowerSploit](https://github.com/PowerShellMafia/PowerSploit)

- Import ```PowerSploit```

```PowerShell
PS C:\Users\Administrator> cd .\Desktop\PowerSploit-master
```

```PowerShell
PS C:\Users\Administrator\Desktop\PowerSploit-master> Import-Module .\PowerSploit.psd1
```

- File and Directory enumeration on web servers.
(```Get-HttpStatus```)

```PowerShell
PS C:\Users\Administrator\Desktop\PowerSploit-master> Get-Help Get-HttpStatus

NAME
    Get-HttpStatus

SYNOPSIS
    Returns the HTTP Status Codes and full URL for specified paths.

    PowerSploit Function: Get-HttpStatus
    Author: Chris Campbell (@obscuresec)
    License: BSD 3-Clause
    Required Dependencies: None
    Optional Dependencies: None


SYNTAX
    Get-HttpStatus [-Target] <String> [[-Path] <String>] [[-Port] <Int32>] [-UseSSL] [<CommonParameters>]


DESCRIPTION
    A script to check for the existence of a path or file on a webserver.


RELATED LINKS
    http://obscuresecurity.blogspot.com
    http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html

REMARKS
    To see the examples, type: "get-help Get-HttpStatus -examples".
    For more information, type: "get-help Get-HttpStatus -detailed".
    For technical information, type: "get-help Get-HttpStatus -full".
    For online help, type: "get-help Get-HttpStatus -online"

PS C:\Users\Administrator\Desktop\PowerSploit-master>
```

```PowerShell
PS C:\Users\Administrator\Desktop\PowerSploit-master> Get-Help Get-HttpStatus -Examples

NAME
    Get-HttpStatus

SYNOPSIS
    Returns the HTTP Status Codes and full URL for specified paths.

    PowerSploit Function: Get-HttpStatus
    Author: Chris Campbell (@obscuresec)
    License: BSD 3-Clause
    Required Dependencies: None
    Optional Dependencies: None

    -------------------------- EXAMPLE 1 --------------------------

    C:\PS>Get-HttpStatus -Target www.example.com -Path c:\dictionary.txt | Select-Object {where StatusCode -eq 20*}



    -------------------------- EXAMPLE 2 --------------------------

    C:\PS>Get-HttpStatus -Target www.example.com -Path c:\dictionary.txt -UseSSL


PS C:\Users\Administrator\Desktop\PowerSploit-master>
```

```PowerShell
PS C:\Users\Administrator\Desktop\PowerSploit-master> Get-HttpStatus -Target www.commercefun.com -Path .\Recon\Dictionaries\generic.txt -Port 80 | Where-Object {$_.Status -match "ok"}

                                                                                               Status URL
                                                                                               ------ ---
                                                                                                   OK http://www.commercefun.com/../
                                                                                                   OK http://www.commercefun.com/0/
```

###### Exercise

- Write a script which could save ```home/default``` page for a list of web servers.

```Get-DefaultPage.ps1```

```PowerShell
$reader = [System.IO.File]::OpenText("C:\Users\Administrator\Desktop\Code\41\ip.txt")

while($null -ne ($line = $reader.ReadLine())) {
    $filename = [System.IO.Path]::GetFileName($line)
    Invoke-WebRequest $line -OutFile $filename
}
```

- Try ```Get-HttpStatus``` on multiple machines.

```PowerShell
PS C:\Users\Administrator\Desktop\PowerSploit-master> Get-HttpStatus -Target www.msn.com -Path .\Recon\Dictionaries\generic.txt -Port 80 | Where-Object {$_.Status -match "ok"}

                                                                                               Status URL
                                                                                               ------ ---
                                                                                                   OK http://www.msn.com/../
                                                                                                   OK http://www.msn.com/crossdomain.xml
PS C:\Users\Administrator\Desktop\PowerSploit-master>
```

```PowerShell
PS C:\Users\Administrator\Desktop\PowerSploit-master> Get-HttpStatus -Target www.commercefun.com -Path .\Recon\Dictionaries\generic.txt -Port 80 | Where-Object {$_.Status -match "ok"}

                                                                                               Status URL
                                                                                               ------ ---
                                                                                                   OK http://www.commercefun.com/../
                                                                                                   OK http://www.commercefun.com/0/
```

```PowerShell
PS C:\Users\Administrator\Desktop\PowerSploit-master> Get-HttpStatus -Target www.google.com -Path .\Recon\Dictionaries\generic.txt -UseSSL | Where-Object {$_.Status -match "ok"}

                                                                                               Status URL
                                                                                               ------ ---
                                                                                                   OK https://www.google.com/../
                                                                                                   OK https://www.google.com/a/
PS C:\Users\Administrator\Desktop\PowerSploit-master>
```
