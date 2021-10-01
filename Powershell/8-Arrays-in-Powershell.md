#### 8. Arrays in Powershell

- Type conversion in PowerShell is done with the help of cast ```[ ]``` operator

```PowerShell
PS C:\Users\Windows-32> $a = 6.7 + 4
PS C:\Users\Windows-32> $a
10.7
PS C:\Users\Windows-32> $a.GetType()

IsPublic IsSerial Name                                     BaseType
-------- -------- ----                                     --------
True     True     Double                                   System.ValueType


PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> [int]$a = 3.2 + 6
PS C:\Users\Windows-32> $a
9
PS C:\Users\Windows-32> $a.GetType()

IsPublic IsSerial Name                                     BaseType
-------- -------- ----                                     --------
True     True     Int32                                    System.ValueType


PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> $b = 5.7 + 5.7
PS C:\Users\Windows-32> $b
11.4
PS C:\Users\Windows-32> $b.GetType()

IsPublic IsSerial Name                                     BaseType
-------- -------- ----                                     --------
True     True     Double                                   System.ValueType


PS C:\Users\Windows-32> [int]$b
11
PS C:\Users\Windows-32> $b.GetType()

IsPublic IsSerial Name                                     BaseType
-------- -------- ----                                     --------
True     True     Double                                   System.ValueType


PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> $result = Get-ChildItem
PS C:\Users\Windows-32> $result.GetType()

IsPublic IsSerial Name                                     BaseType
-------- -------- ----                                     --------
True     True     Object[]                                 System.Array


PS C:\Users\Windows-32>
```

- Arrays
    - Commands in PowerShell return an array of Objects – ```[Object[]]```    - More than one type of elements could be stored

```PowerShell
PS C:\Users\Windows-32> $array = 1,2,3,4,5
PS C:\Users\Windows-32> $array
1
2
3
4
5
PS C:\Users\Windows-32> $array.Length
5
PS C:\Users\Windows-32> $array[0]
1
PS C:\Users\Windows-32> $array[1]
2
PS C:\Users\Windows-32> $array[2]
3
PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> $array_notype = 1,"Hi",4.7
PS C:\Users\Windows-32> $array_notype
1
Hi
4.7
PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> $emptyarray = @()
PS C:\Users\Windows-32> $emptyarray
PS C:\Users\Windows-32> $emptyarray.GetType()

IsPublic IsSerial Name                                     BaseType
-------- -------- ----                                     --------
True     True     Object[]                                 System.Array


PS C:\Users\Windows-32>
```

###### Exercise

- Strongly typed arrays

```PowerShell
PS C:\Users\Windows-32> [int[]] $arr = 1,2,4,3
PS C:\Users\Windows-32> $arr
1
2
4
3
PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> [int[]] $arr1 = 7.5,4.6,5
PS C:\Users\Windows-32> $arr1
8
5
5
PS C:\Users\Windows-32>
```