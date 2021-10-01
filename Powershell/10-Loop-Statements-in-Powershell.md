#### 10. Loop Statements in Powershell

###### Loop Statements

- while() {}

```PowerShell
PS C:\Users\Windows-32> $count = 3
PS C:\Users\Windows-32> while ( $count -ge 0 )
>> {
>> "Iteration $count"
>> $count--
>> }
>>
Iteration 3
Iteration 2
Iteration 1
Iteration 0
PS C:\Users\Windows-32>
```

- do {} while()
- do {} until()
- for(;;){}
- foreach ( in ){}

```PowerShell
PS C:\Users\Windows-32> $process = Get-Process
PS C:\Users\Windows-32> foreach ( $i in $process ) {
>> $i.Name
>> }
>>
cmd
conhost
conhost
csrss
csrss
dwm
explorer
Idle
jusched
lsass
lsm
notepad++
powershell
PresentationFontCache
python
SearchIndexer
services
smss
spoolsv
svchost
svchost
svchost
svchost
svchost
svchost
svchost
svchost
svchost
svchost
svchost
svchost
System
taskhost
VBoxService
VBoxTray
wininit
winlogon
wmpnetwk
wuauclt
PS C:\Users\Windows-32>
```

###### Loop Cmdlets

- ForEach-Object

```PowerShell
PS C:\Users\Windows-32> Get-Process | ForEach-Object {$_.Name}
cmd
conhost
conhost
csrss
csrss
dwm
explorer
Idle
jusched
lsass
lsm
notepad++
powershell
PresentationFontCache
python
SearchFilterHost
SearchIndexer
SearchProtocolHost
services
smss
spoolsv
svchost
svchost
svchost
svchost
svchost
svchost
svchost
svchost
svchost
svchost
svchost
svchost
System
taskhost
VBoxService
VBoxTray
wininit
winlogon
wmpnetwk
wuauclt
PS C:\Users\Windows-32>
```

- Where-Object

```PowerShell
PS C:\Users\Windows-32> Get-ChildItem C:\Users\Windows-32 | Where-Object { $_.Name -match "txt" }


    Directory: C:\Users\Windows-32


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
-a---          7/6/2017   9:20 PM         10 text.txt


PS C:\Users\Windows-32>
```

###### Exercise

Iterate through the processes running on your computer and print the path of the executable for each process.

```PowerShell
PS C:\Users\Administrator> Get-Process | ForEach-Object {$_.Name, $_.Path}
cmd
C:\Windows\system32\cmd.exe
conhost
C:\Windows\system32\conhost.exe
conhost
C:\Windows\system32\conhost.exe
csrss
csrss
dfsrs
C:\Windows\system32\DFSRs.exe
dfssvc
C:\Windows\system32\dfssvc.exe
dns
C:\Windows\system32\dns.exe
dwm
C:\Windows\system32\dwm.exe
explorer
C:\Windows\Explorer.EXE
firefox
C:\Program Files\Mozilla Firefox\firefox.exe
firefox
C:\Program Files\Mozilla Firefox\firefox.exe
Idle
ismserv
C:\Windows\System32\ismserv.exe
lsass
C:\Windows\system32\lsass.exe
Microsoft.ActiveDirectory.WebServices
C:\Windows\ADWS\Microsoft.ActiveDirectory.WebServices.exe
msdtc
C:\Windows\System32\msdtc.exe
notepad
C:\Windows\system32\NOTEPAD.EXE
powershell
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
python
C:\Python27\python.exe
services
smss
spoolsv
C:\Windows\System32\spoolsv.exe
svchost
C:\Windows\system32\svchost.exe
svchost
C:\Windows\system32\svchost.exe
svchost
C:\Windows\system32\svchost.exe
svchost
C:\Windows\system32\svchost.exe
svchost
C:\Windows\system32\svchost.exe
svchost
C:\Windows\System32\svchost.exe
svchost
C:\Windows\system32\svchost.exe
svchost
C:\Windows\system32\svchost.exe
svchost
C:\Windows\system32\svchost.exe
svchost
C:\Windows\System32\svchost.exe
System
taskhostex
C:\Windows\system32\taskhostex.exe
VBoxService
C:\Windows\System32\VBoxService.exe
VBoxTray
C:\Windows\System32\VBoxTray.exe
vds
C:\Windows\System32\vds.exe
wininit
C:\Windows\system32\wininit.exe
winlogon
C:\Windows\system32\winlogon.exe
wlms
C:\Windows\system32\wlms\wlms.exe
PS C:\Users\Administrator>
```
