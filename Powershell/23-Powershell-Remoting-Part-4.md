#### 23. Powershell Remoting Part 4

###### PowerShell Remoting – One-to-Many

- ```Invoke-Command```

    - Running ```Commands```
    
	```PowerShell
	PS C:\Users\Administrator> Invoke-Command -ScriptBlock {whoami;(Get-Host).Version;Get-Process} -ComputerName JOHN-PC -Credential John-PC\John
	john-pc\john
	
	Major  Minor  Build  Revision PSComputerName
	-----  -----  -----  -------- --------------
	1      0      0      0        JOHN-PC
	
	Id             : 1288
	Handles        : 23
	CPU            : 0
	Name           : cmd
	PSComputerName : JOHN-PC
	
	
	Id             : 1552
	Handles        : 22
	CPU            : 0.0100144
	Name           : cmd
	PSComputerName : JOHN-PC
	
	
	Id             : 1220
	Handles        : 40
	CPU            : 0.050072
	Name           : conhost
	PSComputerName : JOHN-PC
	
	
	Id             : 3124
	Handles        : 34
	CPU            : 0
	Name           : conhost
	PSComputerName : JOHN-PC
	
	
	Id             : 352
	Handles        : 433
	CPU            : 0.100144
	Name           : csrss
	PSComputerName : JOHN-PC
	
	
	Id             : 408
	Handles        : 206
	CPU            : 0.4706768
	Name           : csrss
	PSComputerName : JOHN-PC
	
	
	Id             : 2920
	Handles        : 79
	CPU            : 0.0100144
	Name           : dllhost
	PSComputerName : JOHN-PC
	
	
	Id             : 912
	Handles        : 66
	CPU            : 0.0200288
	Name           : dwm
	PSComputerName : JOHN-PC
	
	
	Id             : 696
	Handles        : 786
	CPU            : 2.9342192
	Name           : explorer
	PSComputerName : JOHN-PC
	
	
	Id             : 0
	Handles        : 0
	CPU            :
	Name           : Idle
	PSComputerName : JOHN-PC
	
	
	Id             : 492
	Handles        : 744
	CPU            : 0.901296
	Name           : lsass
	PSComputerName : JOHN-PC
	
	
	Id             : 500
	Handles        : 196
	CPU            : 0.0701008
	Name           : lsm
	PSComputerName : JOHN-PC
	
	
	Id             : 3160
	Handles        : 56
	CPU            : 0.0701008
	Name           : notepad
	PSComputerName : JOHN-PC
	
	
	Id             : 2924
	Handles        : 134
	CPU            : 0.1301872
	Name           : python
	PSComputerName : JOHN-PC
	
	
	Id             : 1664
	Handles        : 627
	CPU            : 0.50072
	Name           : SearchIndexer
	PSComputerName : JOHN-PC
	
	
	Id             : 476
	Handles        : 199
	CPU            : 0.7310512
	Name           : services
	PSComputerName : JOHN-PC
	
	
	Id             : 272
	Handles        : 29
	CPU            : 0.0600864
	Name           : smss
	PSComputerName : JOHN-PC
	
	
	Id             : 1356
	Handles        : 280
	CPU            : 0.0200288
	Name           : spoolsv
	PSComputerName : JOHN-PC
	
	
	Id             : 624
	Handles        : 354
	CPU            : 0.3605184
	Name           : svchost
	PSComputerName : JOHN-PC
	
	
	Id             : 736
	Handles        : 267
	CPU            : 0.3304752
	Name           : svchost
	PSComputerName : JOHN-PC
	
	
	Id             : 788
	Handles        : 550
	CPU            : 0.50072
	Name           : svchost
	PSComputerName : JOHN-PC
	
	
	Id             : 872
	Handles        : 514
	CPU            : 3.50504
	Name           : svchost
	PSComputerName : JOHN-PC
	
	
	Id             : 960
	Handles        : 1142
	CPU            : 3.5150544
	Name           : svchost
	PSComputerName : JOHN-PC
	
	
	Id             : 1124
	Handles        : 452
	CPU            : 0.4706768
	Name           : svchost
	PSComputerName : JOHN-PC
	
	
	Id             : 1232
	Handles        : 696
	CPU            : 0.6609504
	Name           : svchost
	PSComputerName : JOHN-PC
	
	
	Id             : 1392
	Handles        : 306
	CPU            : 0.5708208
	Name           : svchost
	PSComputerName : JOHN-PC
	
	
	Id             : 1500
	Handles        : 349
	CPU            : 0.200288
	Name           : svchost
	PSComputerName : JOHN-PC
	
	
	Id             : 1956
	Handles        : 373
	CPU            : 11.3262864
	Name           : svchost
	PSComputerName : JOHN-PC
	
	
	Id             : 2772
	Handles        : 344
	CPU            : 0.9413536
	Name           : svchost
	PSComputerName : JOHN-PC
	
	
	Id             : 3816
	Handles        : 96
	CPU            : 0.0300432
	Name           : svchost
	PSComputerName : JOHN-PC
	
	
	Id             : 4
	Handles        : 565
	CPU            :
	Name           : System
	PSComputerName : JOHN-PC
	
	
	Id             : 1292
	Handles        : 138
	CPU            : 0.050072
	Name           : taskhost
	PSComputerName : JOHN-PC
	
	
	Id             : 3528
	Handles        : 149
	CPU            : 0.0600864
	Name           : taskhost
	PSComputerName : JOHN-PC
	
	
	Id             : 684
	Handles        : 115
	CPU            : 0.25036
	Name           : VBoxService
	PSComputerName : JOHN-PC
	
	
	Id             : 2104
	Handles        : 140
	CPU            : 0.0600864
	Name           : VBoxTray
	PSComputerName : JOHN-PC
	
	
	Id             : 400
	Handles        : 74
	CPU            : 0.2303312
	Name           : wininit
	PSComputerName : JOHN-PC
	
	
	Id             : 448
	Handles        : 113
	CPU            : 0.2703888
	Name           : winlogon
	PSComputerName : JOHN-PC
	
	
	Id             : 556
	Handles        : 417
	CPU            : 0.4105904
	Name           : wmpnetwk
	PSComputerName : JOHN-PC
	
	
	Id             : 3532
	Handles        : 247
	CPU            : 0.7711088
	Name           : wsmprovhost
	PSComputerName : JOHN-PC
	
	
	
	PS C:\Users\Administrator>
	```

    - Running ```Scripts```

	```PowerShell
	PS C:\Users\Administrator\Desktop> Invoke-Command -FilePath .\HelloWorld.ps1 -ComputerName JOHN-PC -Credential John-PC\John
	Hello World
	PS C:\Users\Administrator\Desktop>
	```
	
	```PowerShell
	PS C:\Users\Administrator\Desktop> Invoke-Command -FilePath .\nishang-master\Gather\Check-VM.ps1 -ComputerName JOHN-PC -Credential John-PC\John
	```

    - Running ```Modules```
    
        - Import the ```Module```
    
		```PowerShell
		PS C:\Users\Administrator\Desktop> Import-Module .\nishang-master\powerpreter\Powerpreter.psm1
		WARNING: The names of some imported commands from the module 'Powerpreter' include unapproved verbs that might make them less discoverable. To find the commands with unapproved verbs, run the
		Import-Module command again with the Verbose parameter. For a list of approved verbs, type Get-Verb.
		WARNING: Some imported command names contain one or more of the following restricted characters: # , ( ) {{ }} [ ] & - / \ $ ^ ; : " ' < > | ? @ ` * % + = ~
		PS C:\Users\Administrator\Desktop>
		```
		
		- Check that the ```Module``` is imported

		```PowerShell
		PS C:\Users\Administrator\Desktop> Get-Module
		
		ModuleType Version    Name                                ExportedCommands
		---------- -------    ----                                ----------------
		Manifest   3.1.0.0    Microsoft.PowerShell.Management     {Add-Computer, Add-Content, Checkpoint-Computer, Clear-Content...}
		Manifest   3.0.0.0    Microsoft.PowerShell.Security       {ConvertFrom-SecureString, ConvertTo-SecureString, Get-Acl, Get-AuthenticodeSignature...}
		Manifest   3.1.0.0    Microsoft.PowerShell.Utility        {Add-Member, Add-Type, Clear-Variable, Compare-Object...}
		Manifest   3.0.0.0    Microsoft.WSMan.Management          {Connect-WSMan, Disable-WSManCredSSP, Disconnect-WSMan, Enable-WSManCredSSP...}
		Script     0.0        Powerpreter                         {Add-ScrnSaveBackdoor, Base64ToString, Check-VM, Copy-VSS...}
		
		PS C:\Users\Administrator\Desktop>
		```
		
		- List the ```Functions``` of the ```Module```

		```PowerShell
		PS C:\Users\Administrator\Desktop> Get-Command -Module Powerpreter
		
		CommandType     Name                                               ModuleName
		-----------     ----                                               ----------
		Function        Add-ScrnSaveBackdoor                               Powerpreter
		Function        Base64ToString                                     Powerpreter
		Function        Check-VM                                           Powerpreter
		Function        Copy-VSS                                           Powerpreter
		Function        Create-MultipleSessions                            Powerpreter
		Function        DNS_TXT_Pwnage                                     Powerpreter
		Function        Do-Exfiltration                                    Powerpreter
		Function        Download                                           Powerpreter
		Function        Download_Execute                                   Powerpreter
		Function        Download-Execute-PS                                Powerpreter
		Function        Enable-DuplicateToken                              Powerpreter
		Function        Execute-Command-MSSQL                              Powerpreter
		Function        Execute-DNSTXT-Code                                Powerpreter
		Function        Execute-OnTime                                     Powerpreter
		Function        ExetoText                                          Powerpreter
		Function        FireBuster                                         Powerpreter
		Function        FireListener                                       Powerpreter
		Function        Get-Information                                    Powerpreter
		Function        Get-LsaSecret                                      Powerpreter
		Function        Get-PassHashes                                     Powerpreter
		Function        Get-PassHints                                      Powerpreter
		Function        Get-Wlan-Keys                                      Powerpreter
		Function        Gupt-Backdoor                                      Powerpreter
		Function        HTTP-Backdoor                                      Powerpreter
		Function        Invoke-BruteForce                                  Powerpreter
		Function        Invoke-CredentialsPhish                            Powerpreter
		Function        Invoke-Decode                                      Powerpreter
		Function        Invoke-Encode                                      Powerpreter
		Function        Invoke-NetworkRelay                                Powerpreter
		Function        Invoke-PortScan                                    Powerpreter
		Function        Invoke-PSGcat                                      Powerpreter
		Function        Invoke-PsGcatAgent                                 Powerpreter
		Function        Invoke-PsUACme                                     Powerpreter
		Function        Keylogger                                          Powerpreter
		Function        Out-CHM                                            Powerpreter
		Function        Out-DnsTxt                                         Powerpreter
		Function        Out-Excel                                          Powerpreter
		Function        Out-HTA                                            Powerpreter
		Function        Out-Java                                           Powerpreter
		Function        Out-Shortcut                                       Powerpreter
		Function        Out-WebQuery                                       Powerpreter
		Function        Out-Word                                           Powerpreter
		Function        Persistence                                        Powerpreter
		Function        Pivot                                              Powerpreter
		Function        Remove-Persistence                                 Powerpreter
		Function        Remove-Update                                      Powerpreter
		Function        StringtoBase64                                     Powerpreter
		Function        TexttoEXE                                          Powerpreter
		Function        Use-Session                                        Powerpreter
		
		PS C:\Users\Administrator\Desktop>
		```
		
		- Run the ```Function``` of the ```Module```

		```PowerShell
		PS C:\Users\Administrator\Desktop> Invoke-Command -ScriptBlock ${Function:Get-WLAN-Keys} -ComputerName JOHN-PC -Credential John-PC\John
		You cannot call a method on a null-valued expression.
		    + CategoryInfo          : InvalidOperation: (Replace:String) [], RuntimeException
		    + FullyQualifiedErrorId : InvokeMethodOnNull
		    + PSComputerName        : JOHN-PC
		
		The Wireless AutoConfig Service (wlansvc) is not running.
		PS C:\Users\Administrator\Desktop>
		```
		
- “Fan-Out” or “One-to-Many”

```PowerShell
Invoke-Command -ScriptBlock {whoami;(Get-Host).Version;Get-Process} -ComputerName <DOMAIN_PC>,<DOMAIN_CONTROLLER> -Credential <DOMAIN_NAME>\Administrator
```

```PowerShell
Invoke-Command -ScriptBlock {whoami;(Get-Host).Version;Get-Process} -ComputerName {Get-Content .\servers.txt} -Credential <DOMAIN_NAME>\Administrator
```

###### Exercise

- Write a ```PowerShell``` script which searches for the presence of strings like ```“password”```, ```“username”``` and ```“credentials”``` in the ```C:\``` directory.

```Search-Sensitive.ps1```

```PowerShell
$file = Get-ChildItem -Path C:\ -Filter *.txt -Recurse

Write-Output "`nFiles Found " --------------------- $file.Count

Write-Output "`nScript Output " ---------------------

Select-String $file -Pattern username, password, credential
```

- Run this script on remote machines.

```PowerShell
PS C:\Users\Administrator> Invoke-Command -FilePath .\Desktop\Code\23\Search-Sensitive.ps1 -ComputerName JOHN-PC -Credential John-PC\John


Files Found 
---------------------
477

Script Output 
---------------------

C:\Program Files (x86)\Nmap\nselib\data\enterprise_numbers.txt:42994:43124    PasswordBox Inc.
C:\Program Files (x86)\Nmap\nselib\data\http-folders.txt:563:/password/
C:\Program Files (x86)\Nmap\nselib\data\http-folders.txt:564:/passwords/
C:\Program Files (x86)\Nmap\nselib\data\rtsp-urls.txt:14:/CAM_ID.password.mp2
C:\Program Files (x86)\Nmap\nselib\data\rtsp-urls.txt:178:/user=admin_password=tlJwpbo6_channel=1_stream=0.sdp?real_stream
C:\Program Files (x86)\Nmap\nselib\data\tftplist.txt:167:password.bin
C:\Program Files (x86)\Nmap\nselib\data\tftplist.txt:168:password.cfg
C:\Program Files (x86)\Nmap\nselib\data\tftplist.txt:169:password.ini
C:\Python27\NEWS.txt:4376:- Issue #13642: Unquote before b64encoding user:password during Basic
C:\Python27\NEWS.txt:4796:  test_tk or test_ttk_guionly under a username that is not currently logged
C:\Python27\NEWS.txt:7185:  long passwords.  Initial patch by JP St. Pierre.
C:\Python27\NEWS.txt:7749:  TLS with authentication credentials.
C:\Python27\NEWS.txt:11063:- Patch #1698: allow '@' in username parsed by urlparse.py.
C:\Python27\NEWS.txt:11144:- When encountering a password-protected robots.txt file the
C:\Python27\NEWS.txt:11145:  RobotFileParser no longer prompts interactively for a username and
C:\Python27\NEWS.txt:11146:  password (bug 813986).
C:\Python27\NEWS.txt:11240:- Added an optional credentials argument to SMTPHandler, for use with
C:\Users\Administrator\Desktop\log.txt:12:C:\Program Files (x86)\Nmap\nselib\data\enterprise_numbers.txt:42994:43124    PasswordBox Inc.
C:\Users\Administrator\Desktop\log.txt:13:C:\Program Files (x86)\Nmap\nselib\data\http-folders.txt:563:/password/
C:\Users\Administrator\Desktop\log.txt:14:C:\Program Files (x86)\Nmap\nselib\data\http-folders.txt:564:/passwords/
C:\Users\Administrator\Desktop\log.txt:15:C:\Program Files (x86)\Nmap\nselib\data\rtsp-urls.txt:14:/CAM_ID.password.mp2
C:\Users\Administrator\Desktop\log.txt:16:C:\Program Files 
(x86)\Nmap\nselib\data\rtsp-urls.txt:178:/user=admin_password=tlJwpbo6_channel=1_stream=0.sdp?real_stream
C:\Users\Administrator\Desktop\log.txt:17:C:\Program Files (x86)\Nmap\nselib\data\tftplist.txt:167:password.bin
C:\Users\Administrator\Desktop\log.txt:18:C:\Program Files (x86)\Nmap\nselib\data\tftplist.txt:168:password.cfg
C:\Users\Administrator\Desktop\log.txt:19:C:\Program Files (x86)\Nmap\nselib\data\tftplist.txt:169:password.ini
C:\Users\Administrator\Desktop\log.txt:20:C:\Python27\NEWS.txt:4376:- Issue #13642: Unquote before b64encoding user:password during Basic
C:\Users\Administrator\Desktop\log.txt:21:C:\Python27\NEWS.txt:4796:  test_tk or test_ttk_guionly under a username that is not currently 
logged
C:\Users\Administrator\Desktop\log.txt:22:C:\Python27\NEWS.txt:7185:  long passwords.  Initial patch by JP St. Pierre.
C:\Users\Administrator\Desktop\log.txt:23:C:\Python27\NEWS.txt:7749:  TLS with authentication credentials.
C:\Users\Administrator\Desktop\log.txt:24:C:\Python27\NEWS.txt:11063:- Patch #1698: allow '@' in username parsed by urlparse.py.
C:\Users\Administrator\Desktop\log.txt:25:C:\Python27\NEWS.txt:11144:- When encountering a password-protected robots.txt file the
C:\Users\Administrator\Desktop\log.txt:26:C:\Python27\NEWS.txt:11145:  RobotFileParser no longer prompts interactively for a username and
C:\Users\Administrator\Desktop\log.txt:27:C:\Python27\NEWS.txt:11146:  password (bug 813986).
C:\Users\Administrator\Desktop\log.txt:28:C:\Python27\NEWS.txt:11240:- Added an optional credentials argument to SMTPHandler, for use with
C:\Users\Administrator\Desktop\log.txt:29:nishang-master\CHANGELOG.txt:32:- Added support for dumping cleartext credentials from RDP 
sessions for Invoke-MimikatzWfigestDowngrade.
C:\Users\Administrator\Desktop\log.txt:30:nishang-master\CHANGELOG.txt:49:- Removed hard coded credentials from Invoke-PSGcat.ps1 and 
Invoke-PSGcat in Powerpreter. So embarrassing!
C:\Users\Administrator\Desktop\log.txt:31:nishang-master\CHANGELOG.txt:74:- Credentials script renamed to Invoke-CredentialsPhish.
C:\Users\Administrator\Desktop\log.txt:32:nishang-master\CHANGELOG.txt:186:- Fixed help in Credentials.ps1
C:\Users\Administrator\Desktop\log.txt:33:nishang-master\CHANGELOG.txt:191:- Fixed a bug in Credentials.ps1
C:\Users\Administrator\Desktop\log.txt:34:nishang-master\CHANGELOG.txt:195:- Credentials payload now validates both local and AD crdentials. 
If creds entered could not be validated 
C:\Users\Administrator\Desktop\log.txt:35:locally or at AD, credential prompt is shown again.
C:\Users\Administrator\Desktop\log.txt:36:nishang-master\CHANGELOG.txt:208:- Removed delay in the credentials payload's prompt. Now the 
prompt asking for credentials will keep 
C:\Users\Administrator\Desktop\log.txt:38:nishang-master\CHANGELOG.txt:210:- Removed hard coded credentials from Credentials.ps1 :| and 
edited the code to accept user input.
C:\Users\Administrator\Desktop\log.txt:39:PowerSploit-master\Recon\Dictionaries\generic.txt:969:password/
C:\Users\Administrator\Desktop\log.txt:40:PowerSploit-master\Recon\Dictionaries\generic.txt:970:passwords/
C:\Users\Administrator\Desktop\log.txt:41:SEC505-Scripts\Laptop-Setup-README-NOW.txt:46:Note: The script will reset your password to 
"P@ssword" inside the VM.
C:\Users\Administrator\Desktop\log.txt:42:SEC505-Scripts\Day1-PowerShell\Examples\signatures.txt:17:iisadmpwd                Attempts to 
access the IIS 4.0 change password scripts 
C:\Users\Administrator\Desktop\log.txt:44:SEC505-Scripts\Day1-PowerShell\Examples\signatures.txt:47:/\~.+|\%2f\%7e                Attempts 
to use a /~ in a request (possible username 
C:\Users\Administrator\Desktop\log.txt:46:SEC505-Scripts\Day1-PowerShell\Misc\Sample_PowerShell_Transcript_Log.txt:4:Username: 
TESTING\TestUser47
C:\Users\Administrator\Desktop\log.txt:47:SEC505-Scripts\Day2-Hardening\IIS\Log_Analysis\Signatures.txt:17:iisadmpwd                Attempts 
to access the IIS 4.0 change password 
C:\Users\Administrator\Desktop\log.txt:50:username search).
C:\Users\Administrator\Desktop\log.txt:51:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:4:The passwords of local administrative 
accounts should be changed regularly and these 
C:\Users\Administrator\Desktop\log.txt:52:passwords should be different from one computer to the next.  But how can this been done securely 
and conveniently?  How can this be done 
C:\Users\Administrator\Desktop\log.txt:54:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:15:Copy the Update-PasswordArchive.ps1 
script into that shared folder (\\server\share).
C:\Users\Administrator\Desktop\log.txt:55:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:17:Using Group Policy, SCCM, a third-party 
EMS, SCHTASKS.EXE or some other technique, 
C:\Users\Administrator\Desktop\log.txt:57:command: "powershell.exe \\server\share\update-passwordarchive.ps1 -certificatefilepath 
\\server\share\cert.cer -passwordarchivepath 
C:\Users\Administrator\Desktop\log.txt:58:\\server\share -localusername administrator".  This resets the password on the local Administrator 
account, or whatever account is 
C:\Users\Administrator\Desktop\log.txt:59:specified, with a 15-25 character, random complex password.  The password is encrypted in memory 
with the public key of the certificate 
C:\Users\Administrator\Desktop\log.txt:61:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:19:When a password for a computer (laptop47) 
needs to be recovered, the trusted 
C:\Users\Administrator\Desktop\log.txt:62:administrator should run from their own local computer the following PowerShell script: 
"recover-passwordarchive.ps1 -passwordarchivepath 
C:\Users\Administrator\Desktop\log.txt:63:\\server\share -computername laptop47 -username helpdesk".  This downloads the necessary encrypted 
files and decrypts them locally in memory 
C:\Users\Administrator\Desktop\log.txt:64:using the private key of the administrator, displaying the plaintext password within PowerShell.
C:\Users\Administrator\Desktop\log.txt:65:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:26:PowerShell 2.0 or later must be installed 
on both the computer with the local user 
C:\Users\Administrator\Desktop\log.txt:66:account whose password is to be reset and also on the administrators' computers who will recover 
these passwords in plaintext.
C:\Users\Administrator\Desktop\log.txt:67:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:28:The Update-PasswordArchive.ps1 script, 
which resets the password, must run with 
C:\Users\Administrator\Desktop\log.txt:69:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:41:Copy the \Day2-DAC\UpdatePasswords folder 
to your hard drive.
C:\Users\Administrator\Desktop\log.txt:70:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:43:In File Explorer, double-click the 
"Password-is-password.pfx" file to import the 
C:\Users\Administrator\Desktop\log.txt:71:test certificate and private key into your current user store (accept all the defaults).  The 
password is...password.
C:\Users\Administrator\Desktop\log.txt:72:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:45:Open PowerShell with administrative 
privileges and run this command to reset the 
C:\Users\Administrator\Desktop\log.txt:73:password on the Guest account:
C:\Users\Administrator\Desktop\log.txt:74:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:47:    .\Update-PasswordArchive.ps1 
-LocalUserName Guest -CertificateFilePath 
C:\Users\Administrator\Desktop\log.txt:76:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:53:If you open the file in Notepad or a hex 
editor, you'll see that it has been 
C:\Users\Administrator\Desktop\log.txt:78:user certificate store, hence, you can use your private key to extract the password from the 
encrypted file.  Unless hackers have stolen 
C:\Users\Administrator\Desktop\log.txt:79:your private key, they will not be able to decrypt the file and obtain the password inside it.
C:\Users\Administrator\Desktop\log.txt:80:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:55:To obtain the plaintext password, run 
this command:
C:\Users\Administrator\Desktop\log.txt:81:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:57:    .\Recover-PasswordArchive.ps1 
-ComputerName $env:computername -UserName Guest
C:\Users\Administrator\Desktop\log.txt:82:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:59:The output is an object with the 
plaintext password and other properties, similar 
C:\Users\Administrator\Desktop\log.txt:84:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:63:    UserName : Guest
C:\Users\Administrator\Desktop\log.txt:85:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:68:    Password : b4EAti!HiLX]QI2
C:\Users\Administrator\Desktop\log.txt:86:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:70:The password property can now be piped 
into other commands or copied into the 
C:\Users\Administrator\Desktop\log.txt:88:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:74:    get-help -full 
.\Update-PasswordArchive.ps1 
C:\Users\Administrator\Desktop\log.txt:89:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:81:The password is never sent over the 
network in plaintext, never saved to disk in 
C:\Users\Administrator\Desktop\log.txt:90:plaintext, and never exposed as a command-line argument, either when resetting the password or 
when recovering it later.  The new password 
C:\Users\Administrator\Desktop\log.txt:91:is generated randomly in the memory of the PowerShell process running on the computer where the 
password is reset.  The process runs for 
C:\Users\Administrator\Desktop\log.txt:93:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:83:Different certificates can be used at 
different times, as long as their private 
C:\Users\Administrator\Desktop\log.txt:94:keys are available to the administrator.  When recovering a password, the correct certificate and 
private key will be used automatically.  A 
C:\Users\Administrator\Desktop\log.txt:96:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:85:If the shared folder is not accessible to 
the computer when the scheduled job runs, 
C:\Users\Administrator\Desktop\log.txt:97:the password is not reset.
C:\Users\Administrator\Desktop\log.txt:98:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:87:If multiple administrators must be able 
to recover the plaintext passwords, export 
C:\Users\Administrator\Desktop\log.txt:102:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:91:The update script writes to the 
Application event log whenever and wherever the 
C:\Users\Administrator\Desktop\log.txt:103:script is run (Source: PasswordArchive, Event ID: 9013).
C:\Users\Administrator\Desktop\log.txt:104:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:93:The script can only be used to reset the 
passwords of local accounts, not domain 
C:\Users\Administrator\Desktop\log.txt:106:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:100:Keep the private key for the 
certificate used to encrypt the password archive 
C:\Users\Administrator\Desktop\log.txt:108:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:102:If the private key for the certificate 
is compromised, create a new key pair, 
C:\Users\Administrator\Desktop\log.txt:110:Policy, SCHTASKS.EXE or some other technique.  Once all passwords have been changed, the fact 
that the old private key has been compromised 
C:\Users\Administrator\Desktop\log.txt:111:does not mean any current passwords are known. 
C:\Users\Administrator\Desktop\log.txt:112:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:104:Use an RSA public key which is 2048 
bits or larger.  The public key encrypts a 
C:\Users\Administrator\Desktop\log.txt:113:random 256-bit Rijndael key, which encrypts the password.  Every file has a different Rijndael 
key.  RSA and Rijndael are used for maximum 
C:\Users\Administrator\Desktop\log.txt:115:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:106:Prevent modification of the 
Update-PasswordArchive.ps1 script itself by digitally 
C:\Users\Administrator\Desktop\log.txt:118:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:108:Attackers may try to corrupt or delete 
the existing password archive files to 
C:\Users\Administrator\Desktop\log.txt:119:prevent access to current passwords.  Each archive file contains an encrypted SHA256 hash of the 
username, computername and password in that 
C:\Users\Administrator\Desktop\log.txt:120:file in order to detect modified or damaged bits; the hash is checked whenever a password is 
recovered.  
C:\Users\Administrator\Desktop\log.txt:121:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:127:An attacker might try to generate 
millions of spoofed archive files and add them 
C:\Users\Administrator\Desktop\log.txt:126:machines.  Besides, the benefit to us of managing local administrative account passwords 
correctly far exceeds the potential negative of 
C:\Users\Administrator\Desktop\log.txt:128:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:136:The output of the 
Recover-PasswordArchive.ps1 script can be piped into other 
C:\Users\Administrator\Desktop\log.txt:129:scripts to automate other tasks which require the plaintext password, such as executing commands, 
doing WMI queries, opening an RDP session, 
C:\Users\Administrator\Desktop\log.txt:130:or immediately resetting the password again when finished.
C:\Users\Administrator\Desktop\log.txt:131:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:138:When recovering a password, you can 
pipe the password into the built-in clip.exe 
C:\Users\Administrator\Desktop\log.txt:132:utility to put the password into the clipboard, like this:
C:\Users\Administrator\Desktop\log.txt:133:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:140:    
\\controller\password-archives\Recover-PasswordArchive.ps1 `
C:\Users\Administrator\Desktop\log.txt:134:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:141:    -PasswordArchivePath 
\\controller\password-archives -ComputerName laptop47 ` 
C:\Users\Administrator\Desktop\log.txt:135:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:142:    -UserName Administrator | 
select-object -expandproperty password | clip.exe
C:\Users\Administrator\Desktop\log.txt:136:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:144:Keep the number of files in the archive 
folder manageable by using the 
C:\Users\Administrator\Desktop\log.txt:137:CleanUp-PasswordArchives.ps1 script.  Perhaps running this script as a scheduled job every two or 
four weeks.
C:\Users\Administrator\Desktop\log.txt:138:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:146:To optimize the performance of the 
Recover-PasswordArchive.ps1 script when there 
C:\Users\Administrator\Desktop\log.txt:139:are more than 100,000 files in the folder containing the password archives, disable 8.3 file name 
generation and strip all current 8.3 names 
C:\Users\Administrator\Desktop\log.txt:141:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:150:You can also perform an immediate 
password update with commands wrapped in a 
C:\Users\Administrator\Desktop\log.txt:143:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:153:    Invoke-Command -ComputerName 
laptop47 -filepath .\Update-PasswordArchive.ps1 
C:\Users\Administrator\Desktop\log.txt:145:SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:158:The above Invoke-Command can be done by 
specifying UNC paths instead, but this 
C:\Users\Administrator\Desktop\log.txt:146:requires delegation of credentials to the remote computer, which is not ideal for limiting token 
abuse attacks, so the certificate and 
C:\Users\Administrator\Desktop\log.txt:148:SEC505-Scripts\Day6-Servers\Event_Log_ID_Numbers.txt:23:529 = Logon Failure: Unknown user name or 
bad password
C:\Users\Administrator\Desktop\log.txt:149:SEC505-Scripts\Day6-Servers\Event_Log_ID_Numbers.txt:29:535 = The specified account's password 
has expired
C:\Users\Administrator\Desktop\log.txt:150:SEC505-Scripts\Day6-Servers\Event_Log_ID_Numbers.txt:72:627 = Change Password Attempt
C:\Users\Administrator\Desktop\log.txt:151:SEC505-Scripts\Day6-Servers\Event_Log_ID_Numbers.txt:73:628 = User Account password set
C:\Users\Administrator\Desktop\log.txt:152:SEC505-Scripts\Day6-Servers\Kali-Linux-CheatSheet.txt:6:Default username is "root", password is 
"toor".
C:\Users\Administrator\Desktop\log.txt:153:SEC505-Scripts\Day6-Servers\Kali-Linux-CheatSheet.txt:63:     Password, User and Group Management
C:\Users\Administrator\Desktop\log.txt:154:SEC505-Scripts\Day6-Servers\Kali-Linux-CheatSheet.txt:65:passwd <username>
C:\Users\Administrator\Desktop\log.txt:155:SEC505-Scripts\Day6-Servers\Kali-Linux-CheatSheet.txt:67:id [<username>]
C:\Users\Administrator\Desktop\log.txt:156:SEC505-Scripts\Day6-Servers\Kali-Linux-CheatSheet.txt:69:adduser <username>
C:\Users\Administrator\Desktop\log.txt:157:SEC505-Scripts\Day6-Servers\Kali-Linux-CheatSheet.txt:70:deluser <username>
C:\Users\Administrator\Desktop\log.txt:158:SEC505-Scripts\Day6-Servers\Kali-Linux-CheatSheet.txt:139:smbclient -U <username> -W <domain> 
//server/share
C:\Users\Administrator\Desktop\log.txt:159:SEC505-Scripts\Day6-Servers\Kali-Linux-CheatSheet.txt:140:smbclient -U <username> -W <domain> 
//server/share "<passphrase>"
C:\Users\Administrator\Desktop\log.txt:160:SEC505-Scripts\Day6-Servers\Kali-Linux-CheatSheet.txt:245:# To install meterpreter with a 
username and password/hash:
C:\Users\Administrator\Desktop\log.txt:161:SEC505-Scripts\Day6-Servers\Kerberos\License.txt:14:MEMBER ACCOUNT, PASSWORD, AND SECURITY
C:\Users\Administrator\Desktop\log.txt:162:SEC505-Scripts\Day6-Servers\Kerberos\License.txt:56:MEMBER ACCOUNT, PASSWORD, AND SECURITY
C:\Users\Administrator\Desktop\log.txt:165:are entirely responsible for maintaining the confidentiality of your password and account. 
Furthermore, you are entirely responsible for any 
C:\Users\Administrator\Desktop\log.txt:167:other breach of security. Microsoft will not be liable for any loss that you may incur as a 
result of someone else using your password or 
C:\Users\Administrator\Desktop\log.txt:169:someone else using your account or password. You may not use anyone else's account without the 
permission of the account holder. 
C:\Users\Administrator\Desktop\log.txt:174:connected to any Microsoft server or to any of the Services, through hacking, password mining or 
any other means. You may not obtain or 
C:\Users\Administrator\Desktop\log.txt:176:SEC505-Scripts\Day6-Servers\Kerberos\README.txt:1:This folder contains a PowerShell script to 
reset the password of
C:\Users\Administrator\Desktop\log.txt:177:SEC505-Scripts\Extras\VBScript\passwords.txt:1:password
C:\Users\Administrator\Desktop\log.txt:178:SEC505-Scripts\Extras\VBScript\signatures.txt:17:iisadmpwd                attempts to access the 
IIS 4.0 change password scripts 
C:\Users\Administrator\Desktop\log.txt:180:SEC505-Scripts\Extras\VBScript\signatures.txt:47:/\~.+|\%2f\%7e                attempts to use a 
/~ in a request (possible username search).
C:\Users\Administrator\Desktop\log.txt:182:Sysinternals tools may include personally identifiable or other sensitive information (such as 
usernames, passwords, paths to files 
C:\Users\Administrator\Desktop\log.txt:185:SysinternalsSuite\readme.txt:18:Autologon - Bypass password screen during logon.
C:\Users\Administrator\Desktop\log.txt:186:SysinternalsSuite\readme.txt:102:PsPasswd - Changes account passwords.
C:\Users\Administrator\Desktop\log.txt:187:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Automatic_Variables.help.txt:109:       
typically C:\Users\<UserName>.
C:\Users\Administrator\Desktop\log.txt:188:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Functions_Advanced_Parameters.help.txt:181:
        parameter set, a UserName 
C:\Users\Administrator\Desktop\log.txt:190:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Functions_Advanced_Parameters.help.txt:194:
            $UserName,
C:\Users\Administrator\Desktop\log.txt:191:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Functions_Advanced_Parameters.help.txt:220:
            $UserName,
C:\Users\Administrator\Desktop\log.txt:192:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Functions_Advanced_Parameters.help.txt:561:
            $UserName
C:\Users\Administrator\Desktop\log.txt:193:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Functions_OutputTypeAttribute.help.txt:133:
               $UserName
C:\Users\Administrator\Desktop\log.txt:195:credentials. It
C:\Users\Administrator\Desktop\log.txt:196:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Jobs.help.txt:305:    credentials to run 
the command. The value of the Reason 
C:\Users\Administrator\Desktop\log.txt:198:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Language_Modes.help.txt:172:        
PSCredential
C:\Users\Administrator\Desktop\log.txt:199:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Pipelines.help.txt:367:            
Parameter [Credential] PIPELINE INPUT 
C:\Users\Administrator\Desktop\log.txt:201:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Preference_Variables.help.txt:1084:        
    ProxyCredential                   :
C:\Users\Administrator\Desktop\log.txt:203:credentials of a member of 
C:\Users\Administrator\Desktop\log.txt:204:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_PSSession_Details.help.txt:142:    only if 
you can supply the credentials of the user 
C:\Users\Administrator\Desktop\log.txt:206:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_PSSession_Details.help.txt:144:    
includes RunAs credentials. Otherwise, you can 
C:\Users\Administrator\Desktop\log.txt:209:credentials that were used 
C:\Users\Administrator\Desktop\log.txt:211:credentials of
C:\Users\Administrator\Desktop\log.txt:212:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_FAQ.help.txt:63:    name and 
password credentials on the local computer or the 
C:\Users\Administrator\Desktop\log.txt:213:credentials
C:\Users\Administrator\Desktop\log.txt:214:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_FAQ.help.txt:65:    The credentials 
and the rest of the transmission are 
C:\Users\Administrator\Desktop\log.txt:216:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_FAQ.help.txt:513:    to use the 
Credential parameter of the Invoke-Command, 
C:\Users\Administrator\Desktop\log.txt:218:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_FAQ.help.txt:514:    or 
Enter-PSSession cmdlets to provide the credentials of 
C:\Users\Administrator\Desktop\log.txt:220:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_FAQ.help.txt:521:    credentials.
C:\Users\Administrator\Desktop\log.txt:221:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Requirements.help.txt:62:    
provide the credentials of an administrator. 
C:\Users\Administrator\Desktop\log.txt:223:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:273:    
HOW TO PROVIDE ADMINISTRATOR CREDENTIALS 
C:\Users\Administrator\Desktop\log.txt:224:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:279:    
computer. Credentials are sometimes required 
C:\Users\Administrator\Desktop\log.txt:226:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:283:    
computer, or can provide the credentials of a 
C:\Users\Administrator\Desktop\log.txt:228:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:284:    
group, use the Credential parameter of the 
C:\Users\Administrator\Desktop\log.txt:231:the credentials of an
C:\Users\Administrator\Desktop\log.txt:233:-Credential Domain01\Admin01
C:\Users\Administrator\Desktop\log.txt:234:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:292:    
For more information about the Credential 
C:\Users\Administrator\Desktop\log.txt:236:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:374:    2. 
Use the Credential parameter in all remote 
C:\Users\Administrator\Desktop\log.txt:239:submitting the credentials
C:\Users\Administrator\Desktop\log.txt:240:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:400:    2. 
Verify that a password is set on the 
C:\Users\Administrator\Desktop\log.txt:242:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:401:       
password is not set or the password value 
C:\Users\Administrator\Desktop\log.txt:244:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:404:       
To set password for your user account, use 
C:\Users\Administrator\Desktop\log.txt:246:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:408:    3. 
Use the Credential parameter in all remote 
C:\Users\Administrator\Desktop\log.txt:249:submitting the credentials
C:\Users\Administrator\Desktop\log.txt:250:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:544:       
 --  ProxyCredential
C:\Users\Administrator\Desktop\log.txt:252:ProxyAuthentication, and ProxyCredential
C:\Users\Administrator\Desktop\log.txt:254:-ProxyCredential Domain01\User01
C:\Users\Administrator\Desktop\log.txt:255:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Return.help.txt:44:          function 
ScreenPassword($instance)
C:\Users\Administrator\Desktop\log.txt:257:ScreenPassword($a) }
C:\Users\Administrator\Desktop\log.txt:258:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Return.help.txt:53:      This script 
checks each user account. The ScreenPassword 
C:\Users\Administrator\Desktop\log.txt:261:password-protected 
C:\Users\Administrator\Desktop\log.txt:262:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Return.help.txt:55:      screen saver. If 
the screen saver is password protected, the 
C:\Users\Administrator\Desktop\log.txt:264:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Scopes.help.txt:529:           $Cred = 
Get-Credential
C:\Users\Administrator\Desktop\log.txt:265:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Scopes.help.txt:530:           
Invoke-Command $s {Remove-Item .\Test*.ps1 -Credential 
C:\Users\Administrator\Desktop\log.txt:267:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Scopes.help.txt:537:           $Cred = 
Get-Credential
C:\Users\Administrator\Desktop\log.txt:269:-Credential $c} -ArgumentList $Cred  
C:\Users\Administrator\Desktop\log.txt:270:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Script_Internationalization.help.txt:157:if
 (!($username)) { $msgTable.promptMsg }   
C:\Users\Administrator\Desktop\log.txt:272:can supply the credentials of a
C:\Users\Administrator\Desktop\log.txt:273:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Session_Configuration_Files.help.txt:230:  
    RunAsPassword                 
C:\Users\Administrator\Desktop\log.txt:274:NoteProperty   System.String RunAsPassword=
C:\Users\Administrator\Desktop\log.txt:276:password. The 
C:\Users\Administrator\Desktop\log.txt:277:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:174:    password ensures 
that no one can use or access the 
C:\Users\Administrator\Desktop\log.txt:279:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:175:    your consent. 
Create and enter a password that you can 
C:\Users\Administrator\Desktop\log.txt:281:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:176:    use this password 
later to retrieve the certificate.
C:\Users\Administrator\Desktop\log.txt:282:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:277:        6. Type a 
password, and then type it again to confirm.
C:\Users\Administrator\Desktop\log.txt:283:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:293:        4. On the 
Password page, select "Enable strong private 
C:\Users\Administrator\Desktop\log.txt:285:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:294:           and then 
enter the password that you assigned during 
C:\Users\Administrator\Desktop\log.txt:288:UseDefaultCredentials
C:\Users\Administrator\Desktop\log.txt:289:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Updatable_Help.help.txt:157:    parameter 
that provides the explicit credentials of 
C:\Users\Administrator\Desktop\log.txt:292:Credential
C:\Users\Administrator\Desktop\log.txt:293:C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Updatable_Help.help.txt:164:    Credential 
parameter is valid only when you use the 
C:\Users\Administrator\Desktop\log.txt:295:C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory.hel
p.txt:32:    Account and Password Policy 
C:\Users\Administrator\Desktop\log.txt:298:Remove-ADFineGrainedPasswordPolicy.
C:\Users\Administrator\Desktop\log.txt:300:bad password count greater than five:
C:\Users\Administrator\Desktop\log.txt:302:ADFineGrainedPasswordPolicy
C:\Users\Administrator\Desktop\log.txt:304:(sAMUserName)
C:\Users\Administrator\Desktop\log.txt:306:ADFineGrainedPasswordPolicy
C:\Users\Administrator\Desktop\log.txt:308:ADDefaultDomainPasswordPolicy
C:\Users\Administrator\Desktop\log.txt:310:ADFineGrainedPasswordPolicy
C:\Users\Administrator\Desktop\log.txt:312:fine grained password policy object; that is, an AD
C:\Users\Administrator\Desktop\log.txt:314:msDS-PasswordSettings in AD DS and is derived from
C:\Users\Administrator\Desktop\log.txt:316:ADFineGrainedPasswordPolicy may contain the following properties in
C:\Users\Administrator\Desktop\log.txt:318:attribute: msDS-PasswordComplexityEnabled
C:\Users\Administrator\Desktop\log.txt:319:C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_Obj
ectModel.help.txt:215:      MaxPasswordAge 
C:\Users\Administrator\Desktop\log.txt:322:attribute: msDS-MaximumPasswordAge
C:\Users\Administrator\Desktop\log.txt:323:C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_Obj
ectModel.help.txt:218:      MinPasswordAge 
C:\Users\Administrator\Desktop\log.txt:326:attribute: msDS-MinimumPasswordAge
C:\Users\Administrator\Desktop\log.txt:328:MinPasswordLength - A property of type System.Int32, derived from the
C:\Users\Administrator\Desktop\log.txt:330:attribute: msDS-MinimumPasswordLength
C:\Users\Administrator\Desktop\log.txt:332:PasswordHistoryCount - A property of type System.Int32, derived from
C:\Users\Administrator\Desktop\log.txt:334:attribute: msDS-PasswordHistoryLength
C:\Users\Administrator\Desktop\log.txt:336:attribute: msDS-PasswordSettingsPrecedence
C:\Users\Administrator\Desktop\log.txt:338:msDS-PasswordReversibleEncryptionEnabled
C:\Users\Administrator\Desktop\log.txt:340:AllowReversiblePasswordEncryption - A property of type System.Boolean,
C:\Users\Administrator\Desktop\log.txt:342:ms-DS-UserEncryptedTextPasswordAllowed
C:\Users\Administrator\Desktop\log.txt:344:CannotChangePassword - A property of type System.Boolean, derived from
C:\Users\Administrator\Desktop\log.txt:346:LastBadPasswordAttempt - A property of type System.DateTime, derived
C:\Users\Administrator\Desktop\log.txt:348:directory attribute: badPasswordTime
C:\Users\Administrator\Desktop\log.txt:350:PasswordExpired - A property of type System.Boolean, for AD DS it is
C:\Users\Administrator\Desktop\log.txt:352:attribute msDS-UserPasswordExpired
C:\Users\Administrator\Desktop\log.txt:354:PasswordLastSet - A property of type System.DateTime, derived from the
C:\Users\Administrator\Desktop\log.txt:356:PasswordNeverExpires - A property of type System.Boolean, for AD LDS
C:\Users\Administrator\Desktop\log.txt:358:attribute: msDS-UserDontExpirePassword
C:\Users\Administrator\Desktop\log.txt:360:PasswordNotRequired - A property of type System.Boolean, for AD DS it
C:\Users\Administrator\Desktop\log.txt:362:attribute: ms-DS-UserPasswordNotRequired
C:\Users\Administrator\Desktop\log.txt:364:ADDefaultDomainPasswordPolicy
C:\Users\Administrator\Desktop\log.txt:366:domain-wide password policy of an Active Directory
C:\Users\Administrator\Desktop\log.txt:368:ADDefaultDomainPasswordPolicy may contain the following properties
C:\Users\Administrator\Desktop\log.txt:369:C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_Obj
ectModel.help.txt:721:      MaxPasswordAge 
C:\Users\Administrator\Desktop\log.txt:371:C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_Obj
ectModel.help.txt:724:      MinPasswordAge 
C:\Users\Administrator\Desktop\log.txt:374:MinPasswordLength - A property of type System.Int32, derived from the
C:\Users\Administrator\Desktop\log.txt:376:PasswordHistoryCount - A property of type System.Int32, derived from
C:\Users\Administrator\Desktop\log.txt:378:C:\Users\<UserName>\AppData\Local\Microsoft\Windows\PowerShell\ScheduledJob
C:\Users\Administrator\Desktop\log.txt:380:permissions of the user who is specified by the Credential
C:\Users\Administrator\Desktop\log.txt:382:C:\Users\<UserName>\AppData\Local\Microsoft\Windows\PowerShell
C:\Users\Administrator\Desktop\log.txt:383:C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_ActivityCommonParameters
.help.txt:55:    PSCredential
C:\Users\Administrator\Desktop\log.txt:384:C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_ActivityCommonParameters
.help.txt:216:        user's credentials 
C:\Users\Administrator\Desktop\log.txt:387:NegotiateWithImplicitCredential. The default 
C:\Users\Administrator\Desktop\log.txt:388:C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_ActivityCommonParameters
.help.txt:227:       CAUTION: Credential 
C:\Users\Administrator\Desktop\log.txt:391:which the user's credentials are passed 
C:\Users\Administrator\Desktop\log.txt:393:computer is compromised, the credentials that 
C:\Users\Administrator\Desktop\log.txt:395:command must include the PSCredential 
C:\Users\Administrator\Desktop\log.txt:396:C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_ActivityCommonParameters
.help.txt:336:    -PSCredential 
C:\Users\Administrator\Desktop\log.txt:397:<PSCredential>
C:\Users\Administrator\Desktop\log.txt:399:that contains a PSCredential object, 
C:\Users\Administrator\Desktop\log.txt:401:Get-Credential cmdlet returns. If 
C:\Users\Administrator\Desktop\log.txt:402:C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_ActivityCommonParameters
.help.txt:348:        password.
C:\Users\Administrator\Desktop\log.txt:404:PSCredential. The PS-prefixed parameters configure
C:\Users\Administrator\Desktop\log.txt:406:mechanism that is used to authenticate the user's credentials
C:\Users\Administrator\Desktop\log.txt:408:Kerberos, Negotiate, and NegotiateWithImplicitCredential.
C:\Users\Administrator\Desktop\log.txt:409:C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_WorkflowCommonParameters
.help.txt:102:       CAUTION: Credential 
C:\Users\Administrator\Desktop\log.txt:412:credentials are passed to a remote computer to be
C:\Users\Administrator\Desktop\log.txt:414:credentials that are passed to it can be used to control
C:\Users\Administrator\Desktop\log.txt:416:the PSCredential parameter. Also, the computer must be
C:\Users\Administrator\Desktop\log.txt:417:C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_WorkflowCommonParameters
.help.txt:209:   -PSCredential 
C:\Users\Administrator\Desktop\log.txt:418:<PSCredential>
C:\Users\Administrator\Desktop\log.txt:420:contains a PSCredential object, such as one that the
C:\Users\Administrator\Desktop\log.txt:421:C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_WorkflowCommonParameters
.help.txt:216:        Get-Credential 
C:\Users\Administrator\Desktop\log.txt:424:password.
C:\Users\Administrator\Desktop\log.txt:425:C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_Workflows.help.txt:157: 
                   -Credential 
C:\Users\Administrator\Desktop\log.txt:427:C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_Workflows.help.txt:174: 
                   -Credential 
C:\Users\Administrator\Desktop\log.txt:429:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Automatic_Variables.help.txt:109:       
typically C:\Users\<UserName>.
C:\Users\Administrator\Desktop\log.txt:430:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Functions_Advanced_Parameters.help.txt:181:
        parameter set, a UserName 
C:\Users\Administrator\Desktop\log.txt:432:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Functions_Advanced_Parameters.help.txt:194:
            $UserName,
C:\Users\Administrator\Desktop\log.txt:433:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Functions_Advanced_Parameters.help.txt:220:
            $UserName,
C:\Users\Administrator\Desktop\log.txt:434:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Functions_Advanced_Parameters.help.txt:561:
            $UserName
C:\Users\Administrator\Desktop\log.txt:435:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Functions_OutputTypeAttribute.help.txt:133:
               $UserName
C:\Users\Administrator\Desktop\log.txt:437:credentials. It
C:\Users\Administrator\Desktop\log.txt:438:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Jobs.help.txt:305:    credentials to run 
the command. The value of the Reason 
C:\Users\Administrator\Desktop\log.txt:440:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Language_Modes.help.txt:172:        
PSCredential
C:\Users\Administrator\Desktop\log.txt:441:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Pipelines.help.txt:367:            
Parameter [Credential] PIPELINE INPUT 
C:\Users\Administrator\Desktop\log.txt:443:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Preference_Variables.help.txt:1084:        
    ProxyCredential                   :
C:\Users\Administrator\Desktop\log.txt:445:credentials of a member of 
C:\Users\Administrator\Desktop\log.txt:446:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_PSSession_Details.help.txt:142:    only if 
you can supply the credentials of the user 
C:\Users\Administrator\Desktop\log.txt:448:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_PSSession_Details.help.txt:144:    
includes RunAs credentials. Otherwise, you can 
C:\Users\Administrator\Desktop\log.txt:451:credentials that were used 
C:\Users\Administrator\Desktop\log.txt:453:credentials of
C:\Users\Administrator\Desktop\log.txt:454:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_FAQ.help.txt:63:    name and 
password credentials on the local computer or the 
C:\Users\Administrator\Desktop\log.txt:455:credentials
C:\Users\Administrator\Desktop\log.txt:456:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_FAQ.help.txt:65:    The credentials 
and the rest of the transmission are 
C:\Users\Administrator\Desktop\log.txt:458:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_FAQ.help.txt:513:    to use the 
Credential parameter of the Invoke-Command, 
C:\Users\Administrator\Desktop\log.txt:460:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_FAQ.help.txt:514:    or 
Enter-PSSession cmdlets to provide the credentials of 
C:\Users\Administrator\Desktop\log.txt:462:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_FAQ.help.txt:521:    credentials.
C:\Users\Administrator\Desktop\log.txt:463:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Requirements.help.txt:62:    
provide the credentials of an administrator. 
C:\Users\Administrator\Desktop\log.txt:465:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:273:    
HOW TO PROVIDE ADMINISTRATOR CREDENTIALS 
C:\Users\Administrator\Desktop\log.txt:466:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:279:    
computer. Credentials are sometimes required 
C:\Users\Administrator\Desktop\log.txt:468:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:283:    
computer, or can provide the credentials of a 
C:\Users\Administrator\Desktop\log.txt:470:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:284:    
group, use the Credential parameter of the 
C:\Users\Administrator\Desktop\log.txt:473:the credentials of an
C:\Users\Administrator\Desktop\log.txt:475:-Credential Domain01\Admin01
C:\Users\Administrator\Desktop\log.txt:476:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:292:    
For more information about the Credential 
C:\Users\Administrator\Desktop\log.txt:478:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:374:    2. 
Use the Credential parameter in all remote 
C:\Users\Administrator\Desktop\log.txt:481:submitting the credentials
C:\Users\Administrator\Desktop\log.txt:482:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:400:    2. 
Verify that a password is set on the 
C:\Users\Administrator\Desktop\log.txt:484:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:401:       
password is not set or the password value 
C:\Users\Administrator\Desktop\log.txt:486:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:404:       
To set password for your user account, use 
C:\Users\Administrator\Desktop\log.txt:488:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:408:    3. 
Use the Credential parameter in all remote 
C:\Users\Administrator\Desktop\log.txt:491:submitting the credentials
C:\Users\Administrator\Desktop\log.txt:492:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:544:       
 --  ProxyCredential
C:\Users\Administrator\Desktop\log.txt:494:ProxyAuthentication, and ProxyCredential
C:\Users\Administrator\Desktop\log.txt:496:-ProxyCredential Domain01\User01
C:\Users\Administrator\Desktop\log.txt:497:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Return.help.txt:44:          function 
ScreenPassword($instance)
C:\Users\Administrator\Desktop\log.txt:499:ScreenPassword($a) }
C:\Users\Administrator\Desktop\log.txt:500:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Return.help.txt:53:      This script 
checks each user account. The ScreenPassword 
C:\Users\Administrator\Desktop\log.txt:503:password-protected 
C:\Users\Administrator\Desktop\log.txt:504:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Return.help.txt:55:      screen saver. If 
the screen saver is password protected, the 
C:\Users\Administrator\Desktop\log.txt:506:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Scopes.help.txt:529:           $Cred = 
Get-Credential
C:\Users\Administrator\Desktop\log.txt:507:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Scopes.help.txt:530:           
Invoke-Command $s {Remove-Item .\Test*.ps1 -Credential 
C:\Users\Administrator\Desktop\log.txt:509:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Scopes.help.txt:537:           $Cred = 
Get-Credential
C:\Users\Administrator\Desktop\log.txt:511:-Credential $c} -ArgumentList $Cred  
C:\Users\Administrator\Desktop\log.txt:512:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Script_Internationalization.help.txt:157:if
 (!($username)) { $msgTable.promptMsg }   
C:\Users\Administrator\Desktop\log.txt:514:can supply the credentials of a
C:\Users\Administrator\Desktop\log.txt:515:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Session_Configuration_Files.help.txt:230:  
    RunAsPassword                 
C:\Users\Administrator\Desktop\log.txt:516:NoteProperty   System.String RunAsPassword=
C:\Users\Administrator\Desktop\log.txt:518:password. The 
C:\Users\Administrator\Desktop\log.txt:519:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:174:    password ensures 
that no one can use or access the 
C:\Users\Administrator\Desktop\log.txt:521:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:175:    your consent. 
Create and enter a password that you can 
C:\Users\Administrator\Desktop\log.txt:523:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:176:    use this password 
later to retrieve the certificate.
C:\Users\Administrator\Desktop\log.txt:524:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:277:        6. Type a 
password, and then type it again to confirm.
C:\Users\Administrator\Desktop\log.txt:525:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:293:        4. On the 
Password page, select "Enable strong private 
C:\Users\Administrator\Desktop\log.txt:527:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:294:           and then 
enter the password that you assigned during 
C:\Users\Administrator\Desktop\log.txt:530:UseDefaultCredentials
C:\Users\Administrator\Desktop\log.txt:531:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Updatable_Help.help.txt:157:    parameter 
that provides the explicit credentials of 
C:\Users\Administrator\Desktop\log.txt:534:Credential
C:\Users\Administrator\Desktop\log.txt:535:C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Updatable_Help.help.txt:164:    Credential 
parameter is valid only when you use the 
C:\Users\Administrator\Desktop\nishang-master\CHANGELOG.txt:32:- Added support for dumping cleartext credentials from RDP sessions for 
Invoke-MimikatzWfigestDowngrade.
C:\Users\Administrator\Desktop\nishang-master\CHANGELOG.txt:49:- Removed hard coded credentials from Invoke-PSGcat.ps1 and Invoke-PSGcat in 
Powerpreter. So embarrassing!
C:\Users\Administrator\Desktop\nishang-master\CHANGELOG.txt:74:- Credentials script renamed to Invoke-CredentialsPhish.
C:\Users\Administrator\Desktop\nishang-master\CHANGELOG.txt:186:- Fixed help in Credentials.ps1
C:\Users\Administrator\Desktop\nishang-master\CHANGELOG.txt:191:- Fixed a bug in Credentials.ps1
C:\Users\Administrator\Desktop\nishang-master\CHANGELOG.txt:195:- Credentials payload now validates both local and AD crdentials. If creds 
entered could not be validated locally or at AD, credential prompt is shown again.
C:\Users\Administrator\Desktop\nishang-master\CHANGELOG.txt:208:- Removed delay in the credentials payload's prompt. Now the prompt asking 
for credentials will keep appearing instantly if nothing is entered.
C:\Users\Administrator\Desktop\nishang-master\CHANGELOG.txt:210:- Removed hard coded credentials from Credentials.ps1 :| and edited the code 
to accept user input.
C:\Users\Administrator\Desktop\PowerSploit-master\Recon\Dictionaries\generic.txt:969:password/
C:\Users\Administrator\Desktop\PowerSploit-master\Recon\Dictionaries\generic.txt:970:passwords/
C:\Users\Administrator\Desktop\SEC505-Scripts\Laptop-Setup-README-NOW.txt:46:Note: The script will reset your password to "P@ssword" inside 
the VM.
C:\Users\Administrator\Desktop\SEC505-Scripts\Day1-PowerShell\Examples\signatures.txt:17:iisadmpwd                Attempts to access the IIS 
4.0 change password scripts (reconnaissance).
C:\Users\Administrator\Desktop\SEC505-Scripts\Day1-PowerShell\Examples\signatures.txt:47:/\~.+|\%2f\%7e                Attempts to use a /~ 
in a request (possible username search).
C:\Users\Administrator\Desktop\SEC505-Scripts\Day1-PowerShell\Misc\Sample_PowerShell_Transcript_Log.txt:4:Username: TESTING\TestUser47
C:\Users\Administrator\Desktop\SEC505-Scripts\Day2-Hardening\IIS\Log_Analysis\Signatures.txt:17:iisadmpwd                Attempts to access 
the IIS 4.0 change password scripts (reconnaissance).
C:\Users\Administrator\Desktop\SEC505-Scripts\Day2-Hardening\IIS\Log_Analysis\Signatures.txt:47:/\~.+|\%2f\%7e                Attempts to 
use a /~ in a request (possible username search).
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:4:The passwords of local administrative accounts should 
be changed regularly and these passwords should be different from one computer to the next.  But how can this been done securely and 
conveniently?  How can this be done for free?  
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:15:Copy the Update-PasswordArchive.ps1 script into that 
shared folder (\\server\share).
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:17:Using Group Policy, SCCM, a third-party EMS, 
SCHTASKS.EXE or some other technique, create a scheduled job on every computer that runs once per week (or every night) under Local System 
context that executes the following command: "powershell.exe \\server\share\update-passwordarchive.ps1 -certificatefilepath 
\\server\share\cert.cer -passwordarchivepath \\server\share -localusername administrator".  This resets the password on the local 
Administrator account, or whatever account is specified, with a 15-25 character, random complex password.  The password is encrypted in 
memory with the public key of the certificate (cert.cer) and saved to an archive file to the specified share (\\server\share).  
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:19:When a password for a computer (laptop47) needs to 
be recovered, the trusted administrator should run from their own local computer the following PowerShell script: 
"recover-passwordarchive.ps1 -passwordarchivepath \\server\share -computername laptop47 -username helpdesk".  This downloads the necessary 
encrypted files and decrypts them locally in memory using the private key of the administrator, displaying the plaintext password within 
PowerShell.
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:26:PowerShell 2.0 or later must be installed on both 
the computer with the local user account whose password is to be reset and also on the administrators' computers who will recover these 
passwords in plaintext.
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:28:The Update-PasswordArchive.ps1 script, which resets 
the password, must run with administrative or Local System privileges.
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:41:Copy the \Day2-DAC\UpdatePasswords folder to your 
hard drive.
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:43:In File Explorer, double-click the 
"Password-is-password.pfx" file to import the test certificate and private key into your current user store (accept all the defaults).  The 
password is...password.
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:45:Open PowerShell with administrative privileges and 
run this command to reset the password on the Guest account:
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:47:    .\Update-PasswordArchive.ps1 -LocalUserName 
Guest -CertificateFilePath .\PublicKeyCert.cer
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:53:If you open the file in Notepad or a hex editor, 
you'll see that it has been encrypted with the public key in the PublicKeyCert.cer file.  The private key for this public key has already 
been imported into your local user certificate store, hence, you can use your private key to extract the password from the encrypted file.  
Unless hackers have stolen your private key, they will not be able to decrypt the file and obtain the password inside it.
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:55:To obtain the plaintext password, run this command:
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:57:    .\Recover-PasswordArchive.ps1 -ComputerName 
$env:computername -UserName Guest
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:59:The output is an object with the plaintext password 
and other properties, similar to this:
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:63:    UserName : Guest
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:68:    Password : b4EAti!HiLX]QI2
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:70:The password property can now be piped into other 
commands or copied into the wetware clipboard through your retinas.
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:74:    get-help -full .\Update-PasswordArchive.ps1 
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:81:The password is never sent over the network in 
plaintext, never saved to disk in plaintext, and never exposed as a command-line argument, either when resetting the password or when 
recovering it later.  The new password is generated randomly in the memory of the PowerShell process running on the computer where the 
password is reset.  The process runs for less than a second as Local System in the background.    
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:83:Different certificates can be used at different 
times, as long as their private keys are available to the administrator.  When recovering a password, the correct certificate and private 
key will be used automatically.  A smart card can be used too.  The script has been successfully tested with the Common Access Card (CAC) 
used by the U.S. military and DoD.  
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:85:If the shared folder is not accessible to the 
computer when the scheduled job runs, the password is not reset.
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:87:If multiple administrators must be able to recover 
the plaintext passwords, export the relevant certificate and private key to a PFX file and import it into each administrator's local 
profile.  Because this is not a certificate used to uniquely identify a person or device, everyone on the help desk could have a copy of its 
private key (though this increases the risk of private key exposure as more copies are distributed).  
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:91:The update script writes to the Application event 
log whenever and wherever the script is run (Source: PasswordArchive, Event ID: 9013).
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:93:The script can only be used to reset the passwords 
of local accounts, not domain accounts in AD.
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:100:Keep the private key for the certificate used to 
encrypt the password archive files secure, such as on a smart card.  This is the most important factor.  
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:102:If the private key for the certificate is 
compromised, create a new key pair, replace the certificate file (.CER) in the shared folder, and immediately remotely trigger the scheduled 
job on all machines using Group Policy, SCHTASKS.EXE or some other technique.  Once all passwords have been changed, the fact that the old 
private key has been compromised does not mean any current passwords are known. 
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:104:Use an RSA public key which is 2048 bits or larger. 
 The public key encrypts a random 256-bit Rijndael key, which encrypts the password.  Every file has a different Rijndael key.  RSA and 
Rijndael are used for maximum backwards compatibility (using AES explicitly in the script requires .NET Framework 3.5 or later).  
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:106:Prevent modification of the 
Update-PasswordArchive.ps1 script itself by digitally signing the script, enforcing script signature requirements, and using restrictive 
NTFS permissions.  Only allow NTFS read access to the script to those identities (computer accounts) which need to run it.  Use NTFS 
auditing to track changes to the script.
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:108:Attackers may try to corrupt or delete the existing 
password archive files to prevent access to current passwords.  Each archive file contains an encrypted SHA256 hash of the username, 
computername and password in that file in order to detect modified or damaged bits; the hash is checked whenever a password is recovered.  
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:127:An attacker might try to generate millions of 
spoofed archive files and add them to the shared folder.  This is possible because the script and public key would be accessible to the 
attacker too.  Realistically, though, a DoS attack in which millions of new archive files are created would likely be of low value for the 
attacker since it would be easy to detect, easy to log the name or IP of the machine creating the new files, easy to use timestamps in the 
share to identify post-attack files, easy to recover from nightly or weekly backups, and the DoS attack would not allow the hacker to expand 
their existing powers to new machines.  Besides, the benefit to us of managing local administrative account passwords correctly far exceeds 
the potential negative of this sort of DoS attack.  
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:136:The output of the Recover-PasswordArchive.ps1 
script can be piped into other scripts to automate other tasks which require the plaintext password, such as executing commands, doing WMI 
queries, opening an RDP session, or immediately resetting the password again when finished.
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:138:When recovering a password, you can pipe the 
password into the built-in clip.exe utility to put the password into the clipboard, like this:
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:140:    
\\controller\password-archives\Recover-PasswordArchive.ps1 `
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:141:    -PasswordArchivePath 
\\controller\password-archives -ComputerName laptop47 ` 
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:142:    -UserName Administrator | select-object 
-expandproperty password | clip.exe
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:144:Keep the number of files in the archive folder 
manageable by using the CleanUp-PasswordArchives.ps1 script.  Perhaps running this script as a scheduled job every two or four weeks.
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:146:To optimize the performance of the 
Recover-PasswordArchive.ps1 script when there are more than 100,000 files in the folder containing the password archives, disable 8.3 file 
name generation and strip all current 8.3 names on the volume containing that folder.  Search the Internet on "fsutil.exe 8dot3name" to see 
how.  
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:150:You can also perform an immediate password update 
with commands wrapped in a function like the following:
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:153:    Invoke-Command -ComputerName laptop47 -filepath 
.\Update-PasswordArchive.ps1 -argumentlist "C:\publickeycert.cer","Administrator","c:\"
C:\Users\Administrator\Desktop\SEC505-Scripts\Day4-Admins\UpdatePasswords\README.txt:158:The above Invoke-Command can be done by specifying 
UNC paths instead, but this requires delegation of credentials to the remote computer, which is not ideal for limiting token abuse attacks, 
so the certificate and archive files should be copied back-and-forth manually.  Besides, wrapped in a function, all these steps would be 
hidden from us anyway.
C:\Users\Administrator\Desktop\SEC505-Scripts\Day6-Servers\Event_Log_ID_Numbers.txt:23:529 = Logon Failure: Unknown user name or bad password
C:\Users\Administrator\Desktop\SEC505-Scripts\Day6-Servers\Event_Log_ID_Numbers.txt:29:535 = The specified account's password has expired
C:\Users\Administrator\Desktop\SEC505-Scripts\Day6-Servers\Event_Log_ID_Numbers.txt:72:627 = Change Password Attempt
C:\Users\Administrator\Desktop\SEC505-Scripts\Day6-Servers\Event_Log_ID_Numbers.txt:73:628 = User Account password set
C:\Users\Administrator\Desktop\SEC505-Scripts\Day6-Servers\Kali-Linux-CheatSheet.txt:6:Default username is "root", password is "toor".
C:\Users\Administrator\Desktop\SEC505-Scripts\Day6-Servers\Kali-Linux-CheatSheet.txt:63:     Password, User and Group Management
C:\Users\Administrator\Desktop\SEC505-Scripts\Day6-Servers\Kali-Linux-CheatSheet.txt:65:passwd <username>
C:\Users\Administrator\Desktop\SEC505-Scripts\Day6-Servers\Kali-Linux-CheatSheet.txt:67:id [<username>]
C:\Users\Administrator\Desktop\SEC505-Scripts\Day6-Servers\Kali-Linux-CheatSheet.txt:69:adduser <username>
C:\Users\Administrator\Desktop\SEC505-Scripts\Day6-Servers\Kali-Linux-CheatSheet.txt:70:deluser <username>
C:\Users\Administrator\Desktop\SEC505-Scripts\Day6-Servers\Kali-Linux-CheatSheet.txt:139:smbclient -U <username> -W <domain> //server/share
C:\Users\Administrator\Desktop\SEC505-Scripts\Day6-Servers\Kali-Linux-CheatSheet.txt:140:smbclient -U <username> -W <domain> //server/share 
"<passphrase>"
C:\Users\Administrator\Desktop\SEC505-Scripts\Day6-Servers\Kali-Linux-CheatSheet.txt:245:# To install meterpreter with a username and 
password/hash:
C:\Users\Administrator\Desktop\SEC505-Scripts\Day6-Servers\Kerberos\License.txt:14:MEMBER ACCOUNT, PASSWORD, AND SECURITY
C:\Users\Administrator\Desktop\SEC505-Scripts\Day6-Servers\Kerberos\License.txt:56:MEMBER ACCOUNT, PASSWORD, AND SECURITY
C:\Users\Administrator\Desktop\SEC505-Scripts\Day6-Servers\Kerberos\License.txt:57:If any of the Services requires you to open an account, 
you must complete the registration process by providing us with current, complete and accurate information as prompted by the applicable 
registration form. You are entirely responsible for maintaining the confidentiality of your password and account. Furthermore, you are 
entirely responsible for any and all activities that occur under your account. You agree to notify Microsoft immediately of any unauthorized 
use of your account or any other breach of security. Microsoft will not be liable for any loss that you may incur as a result of someone 
else using your password or account, either with or without your knowledge. However, you could be held liable for losses incurred by 
Microsoft or another party due to someone else using your account or password. You may not use anyone else's account without the permission 
of the account holder. 
C:\Users\Administrator\Desktop\SEC505-Scripts\Day6-Servers\Kerberos\License.txt:61:As a condition of your use of Services, you will not use 
them for any purpose that is unlawful or prohibited by these terms, conditions, and notices. You may not use the Services in any manner that 
could damage, disable, overburden, or impair any Microsoft server, or the network(s) connected to any Microsoft server, or interfere with 
any other party’s use and enjoyment of any Services. You may not attempt to gain unauthorized access to any Services, other accounts, 
computer systems or networks connected to any Microsoft server or to any of the Services, through hacking, password mining or any other 
means. You may not obtain or attempt to obtain any materials or information through any means not intentionally made available through the 
Services. 
C:\Users\Administrator\Desktop\SEC505-Scripts\Day6-Servers\Kerberos\README.txt:1:This folder contains a PowerShell script to reset the 
password of
C:\Users\Administrator\Desktop\SEC505-Scripts\Extras\VBScript\passwords.txt:1:password
C:\Users\Administrator\Desktop\SEC505-Scripts\Extras\VBScript\signatures.txt:17:iisadmpwd                attempts to access the IIS 4.0 
change password scripts (reconnaissance).
C:\Users\Administrator\Desktop\SEC505-Scripts\Extras\VBScript\signatures.txt:47:/\~.+|\%2f\%7e                attempts to use a /~ in a 
request (possible username search).
C:\Users\Administrator\Desktop\SysinternalsSuite\Eula.txt:28:Please be aware that, similar to other debug tools that capture “process state” 
information, files saved by Sysinternals tools may include personally identifiable or other sensitive information (such as usernames, 
passwords, paths to files accessed, and paths to registry accessed). By using this software, you acknowledge that you are aware of this and 
take sole responsibility for any personally identifiable or other sensitive information provided to Microsoft or any other party through 
your use of the software.
C:\Users\Administrator\Desktop\SysinternalsSuite\readme.txt:18:Autologon - Bypass password screen during logon.
C:\Users\Administrator\Desktop\SysinternalsSuite\readme.txt:102:PsPasswd - Changes account passwords.
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Automatic_Variables.help.txt:109:       typically C:\Users\<UserName>.
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Functions_Advanced_Parameters.help.txt:181:        parameter set, a UserName 
parameter in the User parameter set, and a 
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Functions_Advanced_Parameters.help.txt:194:            $UserName,
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Functions_Advanced_Parameters.help.txt:220:            $UserName,
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Functions_Advanced_Parameters.help.txt:561:            $UserName
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Functions_OutputTypeAttribute.help.txt:133:               $UserName
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Jobs.help.txt:287:    The following command starts a job without the required 
credentials. It
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Jobs.help.txt:305:    credentials to run the command. The value of the Reason 
property is:
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Language_Modes.help.txt:172:        PSCredential
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Pipelines.help.txt:367:            Parameter [Credential] PIPELINE INPUT 
ValueFromPipelineByPropertyName NO COERCION
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Preference_Variables.help.txt:1084:            ProxyCredential                   :
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_PSSession_Details.help.txt:106:    the current user must be able to supply the 
credentials of a member of 
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_PSSession_Details.help.txt:142:    only if you can supply the credentials of the user 
who created the
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_PSSession_Details.help.txt:144:    includes RunAs credentials. Otherwise, you can 
get, connect to, use,
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Disconnected_Sessions.help.txt:94:    but only if they can supply the 
credentials that were used 
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Disconnected_Sessions.help.txt:95:    to create the session, or use the RunAs 
credentials of
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_FAQ.help.txt:63:    name and password credentials on the local computer or the 
credentials
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_FAQ.help.txt:65:    The credentials and the rest of the transmission are 
encrypted. 
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_FAQ.help.txt:513:    to use the Credential parameter of the Invoke-Command, 
New-PSSession,
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_FAQ.help.txt:514:    or Enter-PSSession cmdlets to provide the credentials of 
a member of the 
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_FAQ.help.txt:521:    credentials.
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Requirements.help.txt:62:    provide the credentials of an administrator. 
Otherwise, the command fails.
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:273:    HOW TO PROVIDE ADMINISTRATOR CREDENTIALS 
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:279:    computer. Credentials are sometimes required 
even when the current user is
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:283:    computer, or can provide the credentials of a 
member of the Administrators
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:284:    group, use the Credential parameter of the 
New-PSSession, Enter-PSSession
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:287:    For example, the following command provides 
the credentials of an
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:290:        Invoke-Command -ComputerName Server01 
-Credential Domain01\Admin01
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:292:    For more information about the Credential 
parameter, see New-PSSession,
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:374:    2. Use the Credential parameter in all remote 
commands.
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:376:       This is required even when you are 
submitting the credentials
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:400:    2. Verify that a password is set on the 
workgroup-based computer. If a
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:401:       password is not set or the password value 
is empty, you cannot run
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:404:       To set password for your user account, use 
User Accounts in Control
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:408:    3. Use the Credential parameter in all remote 
commands.
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:410:       This is required even when you are 
submitting the credentials
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:544:        --  ProxyCredential
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:548:        1. Use the ProxyAccessType, 
ProxyAuthentication, and ProxyCredential
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:562:                -ProxyAuthentication Negotiate 
-ProxyCredential Domain01\User01
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Return.help.txt:44:          function ScreenPassword($instance)
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Return.help.txt:50:          foreach ($a in @(get-wmiobject win32_desktop)) { 
ScreenPassword($a) }
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Return.help.txt:53:      This script checks each user account. The ScreenPassword 
function returns 
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Return.help.txt:54:      the name of any user account that does not have a 
password-protected 
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Return.help.txt:55:      screen saver. If the screen saver is password protected, the 
function 
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Scopes.help.txt:529:           $Cred = Get-Credential
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Scopes.help.txt:530:           Invoke-Command $s {Remove-Item .\Test*.ps1 -Credential 
$Using:Cred}  
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Scopes.help.txt:537:           $Cred = Get-Credential
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Scopes.help.txt:538:           Invoke-Command $s {param($c) Remove-Item .\Test*.ps1 
-Credential $c} -ArgumentList $Cred  
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Script_Internationalization.help.txt:157:if (!($username)) { $msgTable.promptMsg }   
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Session_Configurations.help.txt:304:      the WithProfile session configuration or 
can supply the credentials of a
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Session_Configuration_Files.help.txt:230:      RunAsPassword                 
NoteProperty   System.String RunAsPassword=
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:173:    The MakeCert.exe tool will prompt you for a private key 
password. The 
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:174:    password ensures that no one can use or access the 
certificate without
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:175:    your consent. Create and enter a password that you can 
remember. You will 
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:176:    use this password later to retrieve the certificate.
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:277:        6. Type a password, and then type it again to confirm.
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:293:        4. On the Password page, select "Enable strong private 
key protection",
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:294:           and then enter the password that you assigned during 
the export 
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Updatable_Help.help.txt:156:    The Update-Help and Save-Help cmdlets have a 
UseDefaultCredentials
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Updatable_Help.help.txt:157:    parameter that provides the explicit credentials of 
the current
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Updatable_Help.help.txt:161:    The Update-Help and Save-Help cmdlets also have a 
Credential
C:\Windows\System32\WindowsPowerShell\v1.0\en-US\about_Updatable_Help.help.txt:164:    Credential parameter is valid only when you use the 
SourcePath
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory.help.txt:32:    Account and Password Policy 
Management are supported by cmdlets such as
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory.help.txt:34:    Set-ADAccountControl, and 
Remove-ADFineGrainedPasswordPolicy.
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_Filter.help.txt:133:    Get entries with a 
bad password count greater than five:
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_Identity.help.txt:105:    
ADFineGrainedPasswordPolicy
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_Identity.help.txt:151:      SAM User Name 
(sAMUserName)
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:34:        
ADFineGrainedPasswordPolicy
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:45:      
ADDefaultDomainPasswordPolicy
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:192:    
ADFineGrainedPasswordPolicy
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:193:      Represents a 
fine grained password policy object; that is, an AD
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:194:      object of type 
msDS-PasswordSettings in AD DS and is derived from
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:197:      An 
ADFineGrainedPasswordPolicy may contain the following properties in
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:204:      the directory 
attribute: msDS-PasswordComplexityEnabled
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:215:      MaxPasswordAge 
- A property of type System.TimeSpan, derived from the
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:216:      directory 
attribute: msDS-MaximumPasswordAge
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:218:      MinPasswordAge 
- A property of type System.TimeSpan, derived from the
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:219:      directory 
attribute: msDS-MinimumPasswordAge
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:221:      
MinPasswordLength - A property of type System.Int32, derived from the
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:222:      directory 
attribute: msDS-MinimumPasswordLength
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:224:      
PasswordHistoryCount - A property of type System.Int32, derived from
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:225:      the directory 
attribute: msDS-PasswordHistoryLength
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:228:      directory 
attribute: msDS-PasswordSettingsPrecedence
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:232:      
msDS-PasswordReversibleEncryptionEnabled
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:433:      
AllowReversiblePasswordEncryption - A property of type System.Boolean,
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:436:      attribute: 
ms-DS-UserEncryptedTextPasswordAllowed
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:441:      
CannotChangePassword - A property of type System.Boolean, derived from
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:463:      
LastBadPasswordAttempt - A property of type System.DateTime, derived
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:464:      from the 
directory attribute: badPasswordTime
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:479:      
PasswordExpired - A property of type System.Boolean, for AD DS it is
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:482:      directory 
attribute msDS-UserPasswordExpired
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:484:      
PasswordLastSet - A property of type System.DateTime, derived from the
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:487:      
PasswordNeverExpires - A property of type System.Boolean, for AD LDS
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:490:      directory 
attribute: msDS-UserDontExpirePassword
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:492:      
PasswordNotRequired - A property of type System.Boolean, for AD DS it
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:495:      directory 
attribute: ms-DS-UserPasswordNotRequired
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:698:    
ADDefaultDomainPasswordPolicy
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:699:      Represents the 
domain-wide password policy of an Active Directory
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:703:      An 
ADDefaultDomainPasswordPolicy may contain the following properties
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:721:      MaxPasswordAge 
- A property of type System.TimeSpan, derived from the
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:724:      MinPasswordAge 
- A property of type System.TimeSpan, derived from the
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:727:      
MinPasswordLength - A property of type System.Int32, derived from the
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\en-US\about_ActiveDirectory_ObjectModel.help.txt:730:      
PasswordHistoryCount - A property of type System.Int32, derived from
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSScheduledJob\en-US\about_Scheduled_Jobs_Troubleshooting.help.txt:94:        
C:\Users\<UserName>\AppData\Local\Microsoft\Windows\PowerShell\ScheduledJob
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSScheduledJob\en-US\about_Scheduled_Jobs_Troubleshooting.help.txt:394:   job or the 
permissions of the user who is specified by the Credential
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSScheduledJob\en-US\about_Scheduled_Jobs_Troubleshooting.help.txt:425:       
C:\Users\<UserName>\AppData\Local\Microsoft\Windows\PowerShell
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_ActivityCommonParameters.help.txt:55:    PSCredential
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_ActivityCommonParameters.help.txt:216:        user's credentials 
when connecting to the target computers. 
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_ActivityCommonParameters.help.txt:218:        Negotiate, and 
NegotiateWithImplicitCredential. The default 
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_ActivityCommonParameters.help.txt:227:       CAUTION: Credential 
Security Service Provider (CredSSP) 
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_ActivityCommonParameters.help.txt:228:       authentication, in 
which the user's credentials are passed 
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_ActivityCommonParameters.help.txt:233:       If the remote 
computer is compromised, the credentials that 
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_ActivityCommonParameters.help.txt:273:        parameter, the 
command must include the PSCredential 
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_ActivityCommonParameters.help.txt:336:    -PSCredential 
<PSCredential>
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_ActivityCommonParameters.help.txt:345:        or enter a variable 
that contains a PSCredential object, 
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_ActivityCommonParameters.help.txt:346:        such as one that the 
Get-Credential cmdlet returns. If 
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_ActivityCommonParameters.help.txt:348:        password.
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_WorkflowCommonParameters.help.txt:21:    PSComputerName and 
PSCredential. The PS-prefixed parameters configure
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_WorkflowCommonParameters.help.txt:93:        Specifies the 
mechanism that is used to authenticate the user's credentials
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_WorkflowCommonParameters.help.txt:95:        Credssp, Digest, 
Kerberos, Negotiate, and NegotiateWithImplicitCredential.
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_WorkflowCommonParameters.help.txt:102:       CAUTION: Credential 
Security Service Provider (CredSSP) authentication, in
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_WorkflowCommonParameters.help.txt:103:       which the user's 
credentials are passed to a remote computer to be
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_WorkflowCommonParameters.help.txt:107:       is compromised, the 
credentials that are passed to it can be used to control
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_WorkflowCommonParameters.help.txt:160:        command must include 
the PSCredential parameter. Also, the computer must be
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_WorkflowCommonParameters.help.txt:209:   -PSCredential 
<PSCredential>
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_WorkflowCommonParameters.help.txt:215:        variable that 
contains a PSCredential object, such as one that the
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_WorkflowCommonParameters.help.txt:216:        Get-Credential 
cmdlet returns. If you enter only a user name, you will be
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_WorkflowCommonParameters.help.txt:217:        prompted for a 
password.
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_Workflows.help.txt:157:                    -Credential 
Domain01\Admin01
C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSWorkflow\en-US\about_Workflows.help.txt:174:                    -Credential 
Domain01\Admin01          
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Automatic_Variables.help.txt:109:       typically C:\Users\<UserName>.
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Functions_Advanced_Parameters.help.txt:181:        parameter set, a UserName 
parameter in the User parameter set, and a 
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Functions_Advanced_Parameters.help.txt:194:            $UserName,
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Functions_Advanced_Parameters.help.txt:220:            $UserName,
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Functions_Advanced_Parameters.help.txt:561:            $UserName
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Functions_OutputTypeAttribute.help.txt:133:               $UserName
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Jobs.help.txt:287:    The following command starts a job without the required 
credentials. It
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Jobs.help.txt:305:    credentials to run the command. The value of the Reason 
property is:
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Language_Modes.help.txt:172:        PSCredential
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Pipelines.help.txt:367:            Parameter [Credential] PIPELINE INPUT 
ValueFromPipelineByPropertyName NO COERCION
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Preference_Variables.help.txt:1084:            ProxyCredential                   :
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_PSSession_Details.help.txt:106:    the current user must be able to supply the 
credentials of a member of 
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_PSSession_Details.help.txt:142:    only if you can supply the credentials of the user 
who created the
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_PSSession_Details.help.txt:144:    includes RunAs credentials. Otherwise, you can 
get, connect to, use,
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Disconnected_Sessions.help.txt:94:    but only if they can supply the 
credentials that were used 
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Disconnected_Sessions.help.txt:95:    to create the session, or use the RunAs 
credentials of
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_FAQ.help.txt:63:    name and password credentials on the local computer or the 
credentials
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_FAQ.help.txt:65:    The credentials and the rest of the transmission are 
encrypted. 
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_FAQ.help.txt:513:    to use the Credential parameter of the Invoke-Command, 
New-PSSession,
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_FAQ.help.txt:514:    or Enter-PSSession cmdlets to provide the credentials of 
a member of the 
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_FAQ.help.txt:521:    credentials.
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Requirements.help.txt:62:    provide the credentials of an administrator. 
Otherwise, the command fails.
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:273:    HOW TO PROVIDE ADMINISTRATOR CREDENTIALS 
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:279:    computer. Credentials are sometimes required 
even when the current user is
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:283:    computer, or can provide the credentials of a 
member of the Administrators
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:284:    group, use the Credential parameter of the 
New-PSSession, Enter-PSSession
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:287:    For example, the following command provides 
the credentials of an
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:290:        Invoke-Command -ComputerName Server01 
-Credential Domain01\Admin01
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:292:    For more information about the Credential 
parameter, see New-PSSession,
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:374:    2. Use the Credential parameter in all remote 
commands.
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:376:       This is required even when you are 
submitting the credentials
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:400:    2. Verify that a password is set on the 
workgroup-based computer. If a
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:401:       password is not set or the password value 
is empty, you cannot run
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:404:       To set password for your user account, use 
User Accounts in Control
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:408:    3. Use the Credential parameter in all remote 
commands.
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:410:       This is required even when you are 
submitting the credentials
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:544:        --  ProxyCredential
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:548:        1. Use the ProxyAccessType, 
ProxyAuthentication, and ProxyCredential
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Remote_Troubleshooting.help.txt:562:                -ProxyAuthentication Negotiate 
-ProxyCredential Domain01\User01
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Return.help.txt:44:          function ScreenPassword($instance)
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Return.help.txt:50:          foreach ($a in @(get-wmiobject win32_desktop)) { 
ScreenPassword($a) }
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Return.help.txt:53:      This script checks each user account. The ScreenPassword 
function returns 
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Return.help.txt:54:      the name of any user account that does not have a 
password-protected 
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Return.help.txt:55:      screen saver. If the screen saver is password protected, the 
function 
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Scopes.help.txt:529:           $Cred = Get-Credential
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Scopes.help.txt:530:           Invoke-Command $s {Remove-Item .\Test*.ps1 -Credential 
$Using:Cred}  
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Scopes.help.txt:537:           $Cred = Get-Credential
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Scopes.help.txt:538:           Invoke-Command $s {param($c) Remove-Item .\Test*.ps1 
-Credential $c} -ArgumentList $Cred  
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Script_Internationalization.help.txt:157:if (!($username)) { $msgTable.promptMsg }   
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Session_Configurations.help.txt:304:      the WithProfile session configuration or 
can supply the credentials of a
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Session_Configuration_Files.help.txt:230:      RunAsPassword                 
NoteProperty   System.String RunAsPassword=
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:173:    The MakeCert.exe tool will prompt you for a private key 
password. The 
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:174:    password ensures that no one can use or access the 
certificate without
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:175:    your consent. Create and enter a password that you can 
remember. You will 
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:176:    use this password later to retrieve the certificate.
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:277:        6. Type a password, and then type it again to confirm.
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:293:        4. On the Password page, select "Enable strong private 
key protection",
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Signing.help.txt:294:           and then enter the password that you assigned during 
the export 
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Updatable_Help.help.txt:156:    The Update-Help and Save-Help cmdlets have a 
UseDefaultCredentials
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Updatable_Help.help.txt:157:    parameter that provides the explicit credentials of 
the current
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Updatable_Help.help.txt:161:    The Update-Help and Save-Help cmdlets also have a 
Credential
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\en-US\about_Updatable_Help.help.txt:164:    Credential parameter is valid only when you use the 
SourcePath

PS C:\Users\Administrator> 
```
