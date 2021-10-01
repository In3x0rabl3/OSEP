#### 9. Conditional Statements in Powershell

###### If Conditional Statement

- If, elseif, else
- Supports usage of commands, cmdlets and pipeline in the condition part

```PowerShell
PS C:\Users\Windows-32> if (1 -gt 0) {"One"} else {"Something"}
One
PS C:\Users\Windows-32> if (1 -gt 4) {"One"} else {"Something"}
Something
PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> if ( ((Get-Process).Count) -gt 40 ) {"Too many processes"} else {"OK"}
OK
PS C:\Users\Windows-32>
```

###### Switch Statement

- Supports parameters like (```–Exact, –Wildcard, -Regex```) for condition matching

```PowerShell
PS C:\Users\Windows-32> switch (1) { 1 {"One"} 2 {"Two"} }
One
PS C:\Users\Windows-32> switch (11) { 1 {"One"} 2 {"Two"} default {"Default"} }
Default
```

```PowerShell
PS C:\Users\Windows-32> switch -wildcard ('abc') { a* {"A"} *b* {"B"} c* {"C"} }
A
B
PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Administrator> switch -Exact (111) { 1* {"Just one"} 2* {"Just two"} *1* {"All one"} 111 {"Exact all one"} }
Exact all one
PS C:\Users\Administrator>
```

- Ability to process files using the ```-file``` parameter

```PowerShell
PS C:\Users\Windows-32> switch -Regex -File C:\test\WindowsUpdate.log { 'Validating'{$_} }
```
