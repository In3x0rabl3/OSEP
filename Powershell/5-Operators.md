#### 5. Operators

- Arithmetic (```+, -, *, /, %```)

```PowerShell
PS C:\Users\Windows-32> 4+7
11
PS C:\Users\Windows-32> 5/3
1.66666666666667
PS C:\Users\Windows-32> 3-6
-3
PS C:\Users\Windows-32> 7*4
28
PS C:\Users\Windows-32> 16%9
7
PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> "Hello" + " World"
Hello World
PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> "Hello" + 5
Hello5
PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> 5 + "Hello"
Cannot convert value "Hello" to type "System.Int32". Error: "Input string was not in a correct format."
At line:1 char:4
+ 5 + <<<<  "Hello"
    + CategoryInfo          : NotSpecified: (:) [], RuntimeException
    + FullyQualifiedErrorId : RuntimeException

PS C:\Users\Windows-32>
```

- Assignment (```=, +=, -=, *=, /=, %=```)

```PowerShell
PS C:\Users\Windows-32> $a = 4
```

```PowerShell
PS C:\Users\Windows-32> $a *= 6
PS C:\Users\Windows-32> $a
24
PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> $a += 4
PS C:\Users\Windows-32> $a
28
PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> $a -= 10
PS C:\Users\Windows-32> $a
18
PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> $a /= 4
PS C:\Users\Windows-32> $a
4.5
PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> $a %= 2
PS C:\Users\Windows-32> $a
0.5
PS C:\Users\Windows-32>
```

- Comparison (```-eq, -ne, -gt, -lt, -le, -ge, -match, -notmatch, -replace, -like, -notlike, -in, -notin, -contains, -notcontains```)

```PowerShell
PS C:\Users\Windows-32> 6 -eq 5
False
PS C:\Users\Windows-32> 5 -eq 5
True
PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> 5 -gt 3
True
PS C:\Users\Windows-32> 5 -gt 7
False
PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> "Hello PowerShell" -match "power"
True
PS C:\Users\Windows-32> "Hello PowerShell" -match "Power"
True
PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> "Hello PowerShell" -replace "Shell"
Hello Power
PS C:\Users\Windows-32> "Hello PowerShell" -replace "shell"
Hello Power
PS C:\Users\Windows-32> "Hello PowerShell" -replace "Shell","Bell"
Hello PowerBell
PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Administrator> "lo" -in "lower"
False
PS C:\Users\Administrator> "lo" -in "lo"
True
PS C:\Users\Administrator>
```

```PowerShell
PS C:\Users\Administrator> 1 -in 1,2,3
True
PS C:\Users\Administrator> 4 -in 1,2,3
False
PS C:\Users\Administrator>
```

- Redirection(```>, >>, 2> and 2>&1```)

Stream   | Number
---------|--------
Pipeline | 1>  
Error    | 2>  
Warning  | 3>
Debug    | 4>

```PowerShell
PS C:\Users\Windows-32> Get-Location

Path
----
C:\Users\Windows-32


PS C:\Users\Windows-32> Get-Location > loc.txt
PS C:\Users\Windows-32> cat .\loc.txt

Path
----
C:\Users\Windows-32
PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> cd ..
PS C:\Users> Get-Location >> .\Windows-32\loc.txt
PS C:\Users> Get-Content .\Windows-32\loc.txt

Path
----
C:\Users\Windows-32

Path
----
C:\Users
PS C:\Users>
```

```PowerShell
PS C:\Users> Get-Process none,explorer 2>&1
Get-Process : Cannot find a process with the name "none". Verify the process name and call the cmdlet again.
At line:1 char:12
+ Get-Process <<<<  none,explorer 2>&1
    + CategoryInfo          : ObjectNotFound: (none:String) [Get-Process], ProcessCommandException
    + FullyQualifiedErrorId : NoProcessFoundForGivenName,Microsoft.PowerShell.Commands.GetProcessCommand


Handles  NPM(K)    PM(K)      WS(K) VM(M)   CPU(s)     Id ProcessName
-------  ------    -----      ----- -----   ------     -- -----------
    774      24    26976      22140   189     4.27    988 explorer


PS C:\Users>
```

###### Exercise

- Explore the PowerShell help system and locate help topics for various operators
