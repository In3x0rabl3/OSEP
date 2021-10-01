#### 16. Advanced Scripting with Powershell

###### PowerShell Scripting

- Dot sourcing
- CmdletBinding
    - Verbose Output
    - Parameter Checks
    - SupportsShouldProcess (```-WhatIf``` and ```-Confirm```)
    
- ```Show-AdvancedScript.ps1```

```Powershell
function Show-AdvancedScript
{
    [CmdletBinding( SupportsShouldProcess = $True)]
    param(
    [Parameter()]
    $FilePath
    )

    Write-Verbose "Deleting $FilePath"
    if ($PSCmdlet.ShouldProcess("$Filepath", "Deleting file permanently"))
    {
    Remove-Item $FilePath
    }
}
```

```Powershell
PS C:\Users\Windows10-32> C:\Users\Windows10-32\Desktop\Show-AdvancedScript.ps1
```

```Powershell
PS C:\Users\Windows10-32> Show-AdvancedScript -FilePath .\1.txt
```

```Powershell
PS C:\Users\Windows10-32> Show-AdvancedScript -FilePath .\2.txt -Verbose
VERBOSE: Deleting .\2.txt
VERBOSE: Performing the operation "Deleting file permanently" on target ".\2.txt".

PS C:\Users\Windows10-32>
```

```Powershell
PS C:\Users\Windows10-32> Show-AdvancedScript -FilePath .\3.txt -WhatIf
What if: Performing the operation "Deleting file permanently" on target ".\3.txt".

PS C:\Users\Windows10-32>
```

```Powershell
PS C:\Users\Windows10-32> Show-AdvancedScript -FilePath .\3.txt -Confirm
```
