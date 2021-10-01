$DotnetCode = @"
public class SysCommands
{

    public static void lookup(string domainname)
    {
        System.Diagnostics.Process.Start("nslookup.exe",domainname);
    }

    public void netcmd (string cmd)
    {
        string cmdstring = "/k net.exe " + cmd;
        System.Diagnostics.Process.Start("cmd.exe",cmdstring);
    }

}
"@

Add-Type -TypeDefinition $DotnetCode
#[SysCommands]::lookup("google.com")

$obj = New-Object SysCommands
$obj.netcmd("user")