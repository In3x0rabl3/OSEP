#### 7. Types in Powershell

- ```Dynamic Types``` - Not strictly typed

```PowerShell
PS C:\Users\Windows-32> $value = "string" + 1
PS C:\Users\Windows-32> $value.GetType()

IsPublic IsSerial Name                                     BaseType
-------- -------- ----                                     --------
True     True     String                                   System.Object


PS C:\Users\Windows-32>
```

- Basis of ```PowerShell``` types is ```.Net```

- [```Type Adaption```](https://blogs.msdn.microsoft.com/besidethepoint/2011/11/22/psobject-and-the-adapted-and-extended-type-systems-ats-and-ets/) – Provides access to alternate object systems like WMI, COM, ADSI etc.

- ```Single quoted``` vs ```Double qouted```

```PowerShell
PS C:\Users\Windows-32> $str = "This is a string"
PS C:\Users\Windows-32> $str.GetType()

IsPublic IsSerial Name                                     BaseType
-------- -------- ----                                     --------
True     True     String                                   System.Object


PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> $str = 'This is a string'
PS C:\Users\Windows-32> $str.GetType()

IsPublic IsSerial Name                                     BaseType
-------- -------- ----                                     --------
True     True     String                                   System.Object


PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> "Another String $str"
Another String This is a string
PS C:\Users\Windows-32>
PS C:\Users\Windows-32> 'Another String $str'
Another String $str
PS C:\Users\Windows-32>
```

- ```Here Strings``` - Multiline 

```PowerShell
PS C:\Users\Windows-32> @"
>> hi
>> this
>> is
>> a
>> line
>> "@
>>
hi
this
is
a
line
PS C:\Users\Windows-32>
```
