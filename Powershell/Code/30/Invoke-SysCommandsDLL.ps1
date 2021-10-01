$DotnetCode = @"
public class SysCommands
{
    public static void lookup (string domainname)
    {
        System.Diagnostics.Process.Start("nslookup.exe",domainname);
    }

    public void netcmd (string cmd)
    {
        string cmdstring = "/k net.exe " + cmd;
        System.Diagnostics.Process.Start("cmd.exe",cmdstring);

    }

    public static void Main()
    {
        string cmdstring = "/k net.exe " + "user";
        System.Diagnostics.Process.Start("cmd.exe",cmdstring);
    }
}

"@

#Add-Type -TypeDefinition $DotnetCode -OutputType Library -OutputAssembly C:\Users\Administrator\Desktop\SysCommands.dll
Add-Type -TypeDefinition $DotnetCode -OutputType ConsoleApplication -OutputAssembly C:\Users\Administrator\Desktop\SysCommand.exe

<##[SysCommands]::lookup("google.com")

$obj = New-Object SysCommands
$obj.netcmd("user")#>