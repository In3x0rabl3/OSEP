#### 15. Advanced Functions in Powershell

###### Advanced Functions
- param statement
- Parameter attributes
    - Mandatory
    -  ```ParameterSetName``` - closest to ```function overloading```
    - Position
    - ValueFromPipeline
- Parameter Validation
    - AllowEmptyString
    - AllowNull
    - AllowEmptyCollection
    - ValidateLength
    - ValidatePattern
    - ValidateSet
    
- ```paramatrributes.ps1```

```PowerShell
function advancedfunction
{
    param (
    [Parameter (Mandatory = $True, Position = 0, ValueFromPipeline = $True, ParameterSetName="ParamSet1")]
    [ValidateSet(1,2,3)]
#   [AllowNull()]
    $a,

    [Parameter (Position = 1)]
    $b
    )

    Write-Output "a is $a"
    Write-Output "b is $b"
}
```

```PowerShell
PS C:\Users\Administrator\Desktop\15> ls


    Directory: C:\Users\Administrator\Desktop\15


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
-a---         7/10/2017   6:25 PM        306 paramatrributes.ps1


PS C:\Users\Administrator\Desktop\15>
```

- ```Dot Sourcing```

```PowerShell
PS C:\Users\Administrator\Desktop\15> . .\paramatrributes.ps1
```

```PowerShell
PS C:\Users\Administrator\Desktop\15> paramattributes 1 2
a is 1
b is 2
PS C:\Users\Administrator\Desktop\15>
```

```PowerShell
PS C:\Users\Administrator\Desktop\15> paramattributes -a 2 -b 6
a is 2
b is 6
PS C:\Users\Administrator\Desktop\15>
```

```PowerShell
PS C:\Users\Administrator\Desktop\15> paramattributes

cmdlet paramattributes at command pipeline position 1
Supply values for the following parameters:
a: 3
b: 4
a is 3
b is 4
PS C:\Users\Administrator\Desktop\15>
```

```PowerShell
PS C:\Users\Administrator\Desktop\15> 1 | paramattributes -b 7
a is 1
b is 7
PS C:\Users\Administrator\Desktop\15>
```

```PowerShell
PS C:\Users\Administrator\Desktop\15> paramattributes -a $null -b 6
```
