#### 6. Advanced Operators

- Logical (```-and, -or, -xor, -not, !```)

```PowerShell
PS C:\Users\Windows-32> (1 -le 6) -and (6 -ge 6)
True
PS C:\Users\Windows-32> (1 -le 6) -and (6 -ge 8)
False
PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> (1 -le 6) -or (6 -ge 8)
True
PS C:\Users\Windows-32>
```

- Split and Join (```-split, -join```)

```PowerShell
PS C:\Users\Windows-32> "Welcome to PowerShell" -split " "
Welcome
to
PowerShell
PS C:\Users\Windows-32>
PS C:\Users\Windows-32> "Welcome to PowerShell" -split "t"
Welcome
o PowerShell
PS C:\Users\Windows-32>
PS C:\Users\Windows-32> "Welcome to PowerShell" -split "t",3
Welcome
o PowerShell
PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> "Wel"," Please" -join "come"
Welcome Please
PS C:\Users\Windows-32>
```

- Type Operators (```-is, -isnot, -as```)

```PowerShell
PS C:\Users\Windows-32> 3 -is "int"
True
PS C:\Users\Windows-32> "3" -is "string"
True
PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> 0x12 -as "int"
18
PS C:\Users\Windows-32> 0x12 -as "string"
18
PS C:\Users\Windows-32>
```
