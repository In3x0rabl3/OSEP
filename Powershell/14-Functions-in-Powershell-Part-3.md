#### 14. Functions in Powershell Part 3

- Switch Parameters

```PowerShell
PS C:\Users\Windows-32> function switchable ($a, $b, [switch]$flip) {
>> $a + $b
>> if ($flip) { $a - $b }
>> }
>>
PS C:\Users\Windows-32> switchable 1 2
3
PS C:\Users\Windows-32> switchable 1 2 -flip
3
-1
PS C:\Users\Windows-32>
```

- Returning values

```PowerShell
PS C:\Users\Windows-32> $output = switchable 1 4
PS C:\Users\Windows-32> $output
5
PS C:\Users\Windows-32>
```

- Scope of variables and functions

```PowerShell
PS C:\Users\Windows-32> $var1 = 33
PS C:\Users\Windows-32> function fun1 ($var1 = 22) {$var1}
PS C:\Users\Windows-32> $var1
33
PS C:\Users\Windows-32> fun1
22
PS C:\Users\Windows-32> $var1
33
PS C:\Users\Windows-32>
```

- List all function

```PowerShell
PS C:\Users\Windows-32> ls function:

CommandType     Name
-----------     ----
Function        A:
Function        addInt
Function        B:
Function        C:
Function        cd..
Function        cd\
Function        Clear-Host
Function        D:
Function        default_value
Function        Disable-PSRemoting
Function        E:
Function        F:
Function        fixed_params
Function        fun1
Function        G:
Function        Get-Verb
Function        H:
Function        help
Function        I:
Function        ImportSystemModules
Function        J:
Function        K:
Function        L:
Function        M:
Function        mkdir
Function        more
Function        N:
Function        O:
Function        P:
Function        prompt
Function        Q:
Function        R:
Function        S:
Function        switchable
Function        T:
Function        TabExpansion
Function        U:
Function        V:
Function        var_params
Function        W:
Function        X:
Function        Y:
Function        Z:


PS C:\Users\Windows-32>
```

###### Exercise

- Create a function which accepts name of a process or service and stops it.

```PowerShell
PS C:\Users\Windows-32> Start-Process notepad
PS C:\Users\Windows-32> function ProcessStop ($name) { Stop-Process -Name $name }
PS C:\Users\Windows-32> ProcessStop "notepad"
PS C:\Users\Windows-32>
```

- Use a switch variable in the above function to add the ability of stopping a service as well.

```PowerShell
PS C:\Windows\system32> function ProcessStop ($name1, $name2, [switch]$flip) {
>> Stop-Process -Name $name1
>> if ($flip) { Stop-Service $name2 }
>> }
>>
PS C:\Windows\system32> ProcessStop "notepad" "WwanSvc" -flip
PS C:\Windows\system32>
```

- Accept a PID parameter too. If a PID is passed to the function, attempt should be made only to stop a process.

```PowerShell
PS C:\Windows\system32> function ProcessStop ($name1, $name2, $p_id, [switch]$flip) {
>> if ($p_id) { Stop-Process $p_id }
>> else { Stop-Process -Name $name1 }
>> if ($flip) { Stop-Service $name2 }
>> }
>>
PS C:\Windows\system32>
```

```PowerShell
PS C:\Windows\system32> Start-Process notepad
PS C:\Windows\system32> Start-Process calc
PS C:\Windows\system32> Get-Process notepad

Handles  NPM(K)    PM(K)      WS(K) VM(M)   CPU(s)     Id ProcessName
-------  ------    -----      ----- -----   ------     -- -----------
     56       3      920       4220    55     0.04   2868 notepad


PS C:\Windows\system32> Get-Process calc

Handles  NPM(K)    PM(K)      WS(K) VM(M)   CPU(s)     Id ProcessName
-------  ------    -----      ----- -----   ------     -- -----------
     70       7     5236       9276    67     0.05   3684 calc


PS C:\Windows\system32>
```

```PowerShell
PS C:\Windows\system32> ProcessStop "calc" "" 2868
```

```PowerShell
PS C:\Windows\system32> Get-Process notepad
Get-Process : Cannot find a process with the name "notepad". Verify the process name and call the cmdlet again.
At line:1 char:12
+ Get-Process <<<<  notepad
    + CategoryInfo          : ObjectNotFound: (notepad:String) [Get-Process], ProcessCommandException
    + FullyQualifiedErrorId : NoProcessFoundForGivenName,Microsoft.PowerShell.Commands.GetProcessCommand

PS C:\Windows\system32>
```

```PowerShell
PS C:\Windows\system32> Get-Process calc

Handles  NPM(K)    PM(K)      WS(K) VM(M)   CPU(s)     Id ProcessName
-------  ------    -----      ----- -----   ------     -- -----------
     70       7     5236       9276    67     0.05   3684 calc


PS C:\Windows\system32>
```