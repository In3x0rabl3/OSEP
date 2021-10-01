$ApiCode = @"

[DllImport("kernel32.dll")]
public static extern bool CreateSymbolicLink(string lpSymlinkFileName, string lpTargetFileName, int dwFlags);

"@

$SymLink = Add-Type -MemberDefinition $ApiCode -Name Symlink  -Namespace CreatSymLink -PassThru
$SymLink::CreateSymbolicLink('C:\link', 'C:\Users\', 1)