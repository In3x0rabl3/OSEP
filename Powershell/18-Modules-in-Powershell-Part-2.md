#### 18. Modules in Powershell Part 2

###### Writing Modules

```Show-AdvancedScript.psm1```

```PowerShell
function Show-AdvancedScript
{
    [CmdletBinding( SupportsShouldProcess = $True)]
    param(
    [Parameter()]
    $Global:FilePath
    )

    Write-Verbose "Deleting $FilePath"
    if ($PSCmdlet.ShouldProcess("$FilePath", "Deleting file permanently"))
    {
    Remove-Item $FilePath
    }


}

function Test-FileExistence
{
    Test-Path $FilePath
}

function DoNoNeedToShow
{
    Write-Output "No Need to show this to user"
}

Export-ModuleMember -Function *-*
```

- ```Import``` the module

```PowerShell
PS C:\Users\Windows10-32> cd .\Desktop

PS C:\Users\Windows10-32\Desktop> Import-Module .\Show-AdvancedScript.psm1

PS C:\Users\Windows10-32\Desktop> Get-Module

ModuleType Version    Name                                ExportedCommands                                                                   
---------- -------    ----                                ----------------                                                                   
Script     1.0.0.0    ISE                                 {Get-IseSnippet, Import-IseSnippet, New-IseSnippet}                                
Manifest   3.1.0.0    Microsoft.PowerShell.Management     {Add-Computer, Add-Content, Checkpoint-Computer, Clear-Content...}                 
Manifest   3.1.0.0    Microsoft.PowerShell.Utility        {Add-Member, Add-Type, Clear-Variable, Compare-Object...}                          
Script     0.0        Show-AdvancedScript                 {Show-AdvancedScript, Test-FileExistence}                                          



PS C:\Users\Windows10-32\Desktop> 
```

```PowerShell
PS C:\Users\Windows10-32\Desktop> Import-Module .\Show-AdvancedScript.psm1 -Verbose
VERBOSE: Loading module from path 'C:\Users\Windows10-32\Desktop\Show-AdvancedScript.psm1'.
VERBOSE: Importing function 'Show-AdvancedScript'.
VERBOSE: Importing function 'Test-FileExistence'.

PS C:\Users\Windows10-32\Desktop> 
```

- List the ```functions``` of a module

```PowerShell
PS C:\Users\Windows10-32\Desktop> Get-Command -Module Show-AdvancedScript

CommandType     Name                                               Version    Source                                                         
-----------     ----                                               -------    ------                                                         
Function        Show-AdvancedScript                                0.0        Show-AdvancedScript                                            
Function        Test-FileExistence                                 0.0        Show-AdvancedScript                                            



PS C:\Users\Windows10-32\Desktop> 
```

- Run the ```functions``` of the ```module```

```PowerShell
PS C:\Users\Administrator\Desktop\Code\18> Show-AdvancedScript C:\Users\Administrator\Desktop\1.txt

PS C:\Users\Administrator\Desktop\Code\18> Test-FileExistence C:\Users\Administrator\Desktop\1.txt
False

PS C:\Users\Administrator\Desktop\Code\18> 
```

- ```Remove``` module

```PowerShell
PS C:\Users\Windows10-32\Desktop> Remove-Module Show-AdvancedScript
```

```PowerShell
PS C:\Users\Windows10-32\Desktop> Get-Module

ModuleType Version    Name                                ExportedCommands                                                                   
---------- -------    ----                                ----------------                                                                   
Script     1.0.0.0    ISE                                 {Get-IseSnippet, Import-IseSnippet, New-IseSnippet}                                
Manifest   3.1.0.0    Microsoft.PowerShell.Management     {Add-Computer, Add-Content, Checkpoint-Computer, Clear-Content...}                 
Manifest   3.1.0.0    Microsoft.PowerShell.Utility        {Add-Member, Add-Type, Clear-Variable, Compare-Object...}                          



PS C:\Users\Windows10-32\Desktop> 
```

- Controlling ```visibility```

```PowerShell
PS C:\Users\Windows10-32\Desktop> Remove-Module Show-AdvancedScript
```

```PowerShell
PS C:\Users\Windows10-32\Desktop> Get-Module 

ModuleType Version    Name                                ExportedCommands                                                                   
---------- -------    ----                                ----------------                                                                   
Script     1.0.0.0    ISE                                 {Get-IseSnippet, Import-IseSnippet, New-IseSnippet}                                
Manifest   3.1.0.0    Microsoft.PowerShell.Management     {Add-Computer, Add-Content, Checkpoint-Computer, Clear-Content...}                 
Manifest   3.1.0.0    Microsoft.PowerShell.Utility        {Add-Member, Add-Type, Clear-Variable, Compare-Object...}                          



PS C:\Users\Windows10-32\Desktop>
```

```PowerShell
PS C:\Users\Windows10-32\Desktop> Import-Module .\Show-AdvancedScript.psm1 -Verbose
VERBOSE: Importing function 'Show-AdvancedScript'.
VERBOSE: Importing function 'Test-FileExistence'.

PS C:\Users\Windows10-32\Desktop> 
```

###### Exercise

Write a module which checks for the presence of KB2871997 (the Pass the hash fix). The module must have at least two functions:

- One which does the actual stuff which should not be exported.
- Another for displaying the results to the user with a warning if the patch is not present.

```Check-PassTheHash.psm1```

```PowerShell
function Check-PassTheHash
{
    $hotfixes = "KB2871997"
    #checks the computer it's run on if any of the listed hotfixes are present
    $hotfix = Get-HotFix -ComputerName $env:computername | Where-Object {$hotfixes -contains $_.HotfixID} | Select-Object -property "HotFixID"  
    $Global:out = Get-HotFix | Where-Object {$hotfixes -contains $_.HotfixID}
}

function Result-PassTheHash
{  
    if ($out)
    {
        "Found HotFix: " + $out.HotFixID
    } 
    else 
    {
        "Didn't Find HotFix"
    }

}
```

```PowerShell
PS C:\Users\Administrator\Desktop> Import-Module .\Check-PassTheHash.psm1
WARNING: The names of some imported commands from the module 'Check-PassTheHash' include unapproved verbs that might make them less discoverab
le. To find the commands with unapproved verbs, run the Import-Module command again with the Verbose parameter. For a list of approved verbs, 
type Get-Verb.

PS C:\Users\Administrator\Desktop>
```

```PowerShell
PS C:\Users\Administrator\Desktop> Get-Command -Module Check-PassTheHash

CommandType     Name                                               ModuleName                                                                
-----------     ----                                               ----------                                                                
Function        Check-PassTheHash                                  Check-PassTheHash                                                         
Function        Result-PassTheHash                                 Check-PassTheHash                                                         

PS C:\Users\Administrator\Desktop>
```

```PowerShell
PS C:\Users\Administrator\Desktop> Check-PassTheHash
```

```PowerShell
PS C:\Users\Administrator\Desktop> Result-PassTheHash
Didn't Find HotFix

PS C:\Users\Administrator\Desktop> 
```
