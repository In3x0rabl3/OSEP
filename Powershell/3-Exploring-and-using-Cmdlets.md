#### 3. Exploring and using Cmdlets

- ```Get-Help``` for ```Get-Command``` Cmdlets

```Powershell
PS C:\Users\Windows-32> Get-Help Get-Command

NAME
    Get-Command

SYNOPSIS
    Gets basic information about cmdlets and other elements of Windows PowerShell commands.


SYNTAX
    Get-Command [[-Name] <string[]>] [-CommandType {Alias | Function | Filter | Cmdlet | ExternalScript | Application |
     Script | All}] [[-ArgumentList] <Object[]>] [-Module <string[]>] [-Syntax] [-TotalCount <int>] [<CommonParameters>
    ]

    Get-Command [-Noun <string[]>] [-Verb <string[]>] [[-ArgumentList] <Object[]>] [-Module <string[]>] [-Syntax] [-Tot
    alCount <int>] [<CommonParameters>]


DESCRIPTION
    The Get-Command cmdlet gets basic information about cmdlets and other elements of Windows PowerShell commands in th
    e session, such as aliases, functions, filters, scripts, and applications.

    Get-Command gets its data directly from the code of a cmdlet, function, script, or alias, unlike Get-Help, which ge
    ts its information from help topic files.

    Without parameters, "Get-Command" gets all of the cmdlets and functions in the current session. "Get-Command *" get
    s all Windows PowerShell elements and all of the non-Windows-PowerShell files in the Path environment variable ($en
    v:path). It groups the files in the "Application" command type.

    You can use the Module parameter of Get-Command to find the commands that were added to the session by adding a Win
    dows PowerShell snap-in or importing a module.


RELATED LINKS
    Online version: http://go.microsoft.com/fwlink/?LinkID=113309
    about_Command_Precedence
    Get-Help
    Get-PSDrive
    Get-Member
    Import-PSSession
    Export-PSSession

REMARKS
    To see the examples, type: "get-help Get-Command -examples".
    For more information, type: "get-help Get-Command -detailed".
    For technical information, type: "get-help Get-Command -full".



PS C:\Users\Windows-32>
```

- ```Get-Command``` Cmdlets

```Powershell
PS C:\Users\Windows-32> Get-Command

CommandType     Name                                                Definition
-----------     ----                                                ----------
Alias           %                                                   ForEach-Object
Alias           ?                                                   Where-Object
Function        A:                                                  Set-Location A:
Alias           ac                                                  Add-Content
Cmdlet          Add-Computer                                        Add-Computer [-DomainName] <String> [-Credential...
Cmdlet          Add-Content                                         Add-Content [-Path] <String[]> [-Value] <Object[...
Cmdlet          Add-History                                         Add-History [[-InputObject] <PSObject[]>] [-Pass...
Cmdlet          Add-Member                                          Add-Member [-MemberType] <PSMemberTypes> [-Name]...
Cmdlet          Add-PSSnapin                                        Add-PSSnapin [-Name] <String[]> [-PassThru] [-Ve...
Cmdlet          Add-Type                                            Add-Type [-TypeDefinition] <String> [-Language <...
Alias           asnp                                                Add-PSSnapIn
Function        B:                                                  Set-Location B:
Function        C:                                                  Set-Location C:
Alias           cat                                                 Get-Content
Alias           cd                                                  Set-Location
Function        cd..                                                Set-Location ..
Function        cd\                                                 Set-Location \
Alias           chdir                                               Set-Location
Cmdlet          Checkpoint-Computer                                 Checkpoint-Computer [-Description] <String> [[-R...
Alias           clc                                                 Clear-Content
Alias           clear                                               Clear-Host
Cmdlet          Clear-Content                                       Clear-Content [-Path] <String[]> [-Filter <Strin...
Cmdlet          Clear-EventLog                                      Clear-EventLog [-LogName] <String[]> [[-Computer...
Cmdlet          Clear-History                                       Clear-History [[-Id] <Int32[]>] [[-Count] <Int32...
Function        Clear-Host                                          $space = New-Object System.Management.Automation...
Cmdlet          Clear-Item                                          Clear-Item [-Path] <String[]> [-Force] [-Filter ...
Cmdlet          Clear-ItemProperty                                  Clear-ItemProperty [-Path] <String[]> [-Name] <S...
Cmdlet          Clear-Variable                                      Clear-Variable [-Name] <String[]> [-Include <Str...
Alias           clhy                                                Clear-History
Alias           cli                                                 Clear-Item
Alias           clp                                                 Clear-ItemProperty
Alias           cls                                                 Clear-Host
Alias           clv                                                 Clear-Variable
Alias           compare                                             Compare-Object
Cmdlet          Compare-Object                                      Compare-Object [-ReferenceObject] <PSObject[]> [...
Cmdlet          Complete-Transaction                                Complete-Transaction [-Verbose] [-Debug] [-Error...
Cmdlet          Connect-WSMan                                       Connect-WSMan [[-ComputerName] <String>] [-Appli...
Cmdlet          ConvertFrom-Csv                                     ConvertFrom-Csv [-InputObject] <PSObject[]> [[-D...
Cmdlet          ConvertFrom-SecureString                            ConvertFrom-SecureString [-SecureString] <Secure...
Cmdlet          ConvertFrom-StringData                              ConvertFrom-StringData [-StringData] <String> [-...
Cmdlet          Convert-Path                                        Convert-Path [-Path] <String[]> [-Verbose] [-Deb...
Cmdlet          ConvertTo-Csv                                       ConvertTo-Csv [-InputObject] <PSObject> [[-Delim...
Cmdlet          ConvertTo-Html                                      ConvertTo-Html [[-Property] <Object[]>] [[-Head]...
Cmdlet          ConvertTo-SecureString                              ConvertTo-SecureString [-String] <String> [[-Sec...
Cmdlet          ConvertTo-Xml                                       ConvertTo-Xml [-InputObject] <PSObject> [-Depth ...
Alias           copy                                                Copy-Item
Cmdlet          Copy-Item                                           Copy-Item [-Path] <String[]> [[-Destination] <St...
Cmdlet          Copy-ItemProperty                                   Copy-ItemProperty [-Path] <String[]> [-Destinati...
Alias           cp                                                  Copy-Item
Alias           cpi                                                 Copy-Item
Alias           cpp                                                 Copy-ItemProperty
Alias           cvpa                                                Convert-Path
Function        D:                                                  Set-Location D:
Alias           dbp                                                 Disable-PSBreakpoint
Cmdlet          Debug-Process                                       Debug-Process [-Name] <String[]> [-Verbose] [-De...
Alias           del                                                 Remove-Item
Alias           diff                                                Compare-Object
Alias           dir                                                 Get-ChildItem
Cmdlet          Disable-ComputerRestore                             Disable-ComputerRestore [-Drive] <String[]> [-Ve...
Cmdlet          Disable-PSBreakpoint                                Disable-PSBreakpoint [-Breakpoint] <Breakpoint[]...
Function        Disable-PSRemoting                                  ...
Cmdlet          Disable-PSSessionConfiguration                      Disable-PSSessionConfiguration [[-Name] <String[...
Cmdlet          Disable-WSManCredSSP                                Disable-WSManCredSSP [-Role] <String> [-Verbose]...
Cmdlet          Disconnect-WSMan                                    Disconnect-WSMan [[-ComputerName] <String>] [-Ve...
Function        E:                                                  Set-Location E:
Alias           ebp                                                 Enable-PSBreakpoint
Alias           echo                                                Write-Output
Cmdlet          Enable-ComputerRestore                              Enable-ComputerRestore [-Drive] <String[]> [-Ver...
Cmdlet          Enable-PSBreakpoint                                 Enable-PSBreakpoint [-Id] <Int32[]> [-PassThru] ...
Cmdlet          Enable-PSRemoting                                   Enable-PSRemoting [-Force] [-Verbose] [-Debug] [...
Cmdlet          Enable-PSSessionConfiguration                       Enable-PSSessionConfiguration [[-Name] <String[]...
Cmdlet          Enable-WSManCredSSP                                 Enable-WSManCredSSP [-Role] <String> [[-Delegate...
Cmdlet          Enter-PSSession                                     Enter-PSSession [-ComputerName] <String> [-Crede...
Alias           epal                                                Export-Alias
Alias           epcsv                                               Export-Csv
Alias           epsn                                                Export-PSSession
Alias           erase                                               Remove-Item
Alias           etsn                                                Enter-PSSession
Cmdlet          Exit-PSSession                                      Exit-PSSession [-Verbose] [-Debug] [-ErrorAction...
Cmdlet          Export-Alias                                        Export-Alias [-Path] <String> [[-Name] <String[]...
Cmdlet          Export-Clixml                                       Export-Clixml [-Path] <String> [-Depth <Int32>] ...
Cmdlet          Export-Console                                      Export-Console [[-Path] <String>] [-Force] [-NoC...
Cmdlet          Export-Counter                                      Export-Counter [-Path] <String> [-FileFormat <St...
Cmdlet          Export-Csv                                          Export-Csv [-Path] <String> [[-Delimiter] <Char>...
Cmdlet          Export-FormatData                                   Export-FormatData [-InputObject <ExtendedTypeDef...
Cmdlet          Export-ModuleMember                                 Export-ModuleMember [[-Function] <String[]>] [-C...
Cmdlet          Export-PSSession                                    Export-PSSession [-Session] <PSSession> [-Output...
Alias           exsn                                                Exit-PSSession
Function        F:                                                  Set-Location F:
Alias           fc                                                  Format-Custom
Alias           fl                                                  Format-List
Alias           foreach                                             ForEach-Object
Cmdlet          ForEach-Object                                      ForEach-Object [-Process] <ScriptBlock[]> [-Inpu...
Cmdlet          Format-Custom                                       Format-Custom [[-Property] <Object[]>] [-Depth <...
Cmdlet          Format-List                                         Format-List [[-Property] <Object[]>] [-GroupBy <...
Cmdlet          Format-Table                                        Format-Table [[-Property] <Object[]>] [-AutoSize...
Cmdlet          Format-Wide                                         Format-Wide [[-Property] <Object>] [-AutoSize] [...
Alias           ft                                                  Format-Table
Alias           fw                                                  Format-Wide
Function        G:                                                  Set-Location G:
Alias           gal                                                 Get-Alias
Alias           gbp                                                 Get-PSBreakpoint
Alias           gc                                                  Get-Content
Alias           gci                                                 Get-ChildItem
Alias           gcm                                                 Get-Command
Alias           gcs                                                 Get-PSCallStack
Alias           gdr                                                 Get-PSDrive
Cmdlet          Get-Acl                                             Get-Acl [[-Path] <String[]>] [-Audit] [-Filter <...
Cmdlet          Get-Alias                                           Get-Alias [[-Name] <String[]>] [-Exclude <String...
Cmdlet          Get-AuthenticodeSignature                           Get-AuthenticodeSignature [-FilePath] <String[]>...
Cmdlet          Get-ChildItem                                       Get-ChildItem [[-Path] <String[]>] [[-Filter] <S...
Cmdlet          Get-Command                                         Get-Command [[-ArgumentList] <Object[]>] [-Verb ...
Cmdlet          Get-ComputerRestorePoint                            Get-ComputerRestorePoint [[-RestorePoint] <Int32...
Cmdlet          Get-Content                                         Get-Content [-Path] <String[]> [-ReadCount <Int6...
Cmdlet          Get-Counter                                         Get-Counter [[-Counter] <String[]>] [-SampleInte...
Cmdlet          Get-Credential                                      Get-Credential [-Credential] <PSCredential> [-Ve...
Cmdlet          Get-Culture                                         Get-Culture [-Verbose] [-Debug] [-ErrorAction <A...
Cmdlet          Get-Date                                            Get-Date [[-Date] <DateTime>] [-Year <Int32>] [-...
Cmdlet          Get-Event                                           Get-Event [[-SourceIdentifier] <String>] [-Verbo...
Cmdlet          Get-EventLog                                        Get-EventLog [-LogName] <String> [[-InstanceId] ...
Cmdlet          Get-EventSubscriber                                 Get-EventSubscriber [[-SourceIdentifier] <String...
Cmdlet          Get-ExecutionPolicy                                 Get-ExecutionPolicy [[-Scope] <ExecutionPolicySc...
Cmdlet          Get-FormatData                                      Get-FormatData [[-TypeName] <String[]>] [-Verbos...
Cmdlet          Get-Help                                            Get-Help [[-Name] <String>] [-Path <String>] [-C...
Cmdlet          Get-History                                         Get-History [[-Id] <Int64[]>] [[-Count] <Int32>]...
Cmdlet          Get-Host                                            Get-Host [-Verbose] [-Debug] [-ErrorAction <Acti...
Cmdlet          Get-HotFix                                          Get-HotFix [[-Id] <String[]>] [-ComputerName <St...
Cmdlet          Get-Item                                            Get-Item [-Path] <String[]> [-Filter <String>] [...
Cmdlet          Get-ItemProperty                                    Get-ItemProperty [-Path] <String[]> [[-Name] <St...
Cmdlet          Get-Job                                             Get-Job [[-Id] <Int32[]>] [-Verbose] [-Debug] [-...
Cmdlet          Get-Location                                        Get-Location [-PSProvider <String[]>] [-PSDrive ...
Cmdlet          Get-Member                                          Get-Member [[-Name] <String[]>] [-InputObject <P...
Cmdlet          Get-Module                                          Get-Module [[-Name] <String[]>] [-All] [-Verbose...
Cmdlet          Get-PfxCertificate                                  Get-PfxCertificate [-FilePath] <String[]> [-Verb...
Cmdlet          Get-Process                                         Get-Process [[-Name] <String[]>] [-ComputerName ...
Cmdlet          Get-PSBreakpoint                                    Get-PSBreakpoint [[-Script] <String[]>] [-Verbos...
Cmdlet          Get-PSCallStack                                     Get-PSCallStack [-Verbose] [-Debug] [-ErrorActio...
Cmdlet          Get-PSDrive                                         Get-PSDrive [[-Name] <String[]>] [-Scope <String...
Cmdlet          Get-PSProvider                                      Get-PSProvider [[-PSProvider] <String[]>] [-Verb...
Cmdlet          Get-PSSession                                       Get-PSSession [[-ComputerName] <String[]>] [-Ver...
Cmdlet          Get-PSSessionConfiguration                          Get-PSSessionConfiguration [[-Name] <String[]>] ...
Cmdlet          Get-PSSnapin                                        Get-PSSnapin [[-Name] <String[]>] [-Registered] ...
Cmdlet          Get-Random                                          Get-Random [[-Maximum] <Object>] [-SetSeed <Null...
Cmdlet          Get-Service                                         Get-Service [[-Name] <String[]>] [-ComputerName ...
Cmdlet          Get-TraceSource                                     Get-TraceSource [[-Name] <String[]>] [-Verbose] ...
Cmdlet          Get-Transaction                                     Get-Transaction [-Verbose] [-Debug] [-ErrorActio...
Cmdlet          Get-UICulture                                       Get-UICulture [-Verbose] [-Debug] [-ErrorAction ...
Cmdlet          Get-Unique                                          Get-Unique [-InputObject <PSObject>] [-AsString]...
Cmdlet          Get-Variable                                        Get-Variable [[-Name] <String[]>] [-ValueOnly] [...
Function        Get-Verb                                            ...
Cmdlet          Get-WinEvent                                        Get-WinEvent [[-LogName] <String[]>] [-MaxEvents...
Cmdlet          Get-WmiObject                                       Get-WmiObject [-Class] <String> [[-Property] <St...
Cmdlet          Get-WSManCredSSP                                    Get-WSManCredSSP [-Verbose] [-Debug] [-ErrorActi...
Cmdlet          Get-WSManInstance                                   Get-WSManInstance [-ResourceURI] <Uri> [-Applica...
Alias           ghy                                                 Get-History
Alias           gi                                                  Get-Item
Alias           gjb                                                 Get-Job
Alias           gl                                                  Get-Location
Alias           gm                                                  Get-Member
Alias           gmo                                                 Get-Module
Alias           gp                                                  Get-ItemProperty
Alias           gps                                                 Get-Process
Alias           group                                               Group-Object
Cmdlet          Group-Object                                        Group-Object [[-Property] <Object[]>] [-NoElemen...
Alias           gsn                                                 Get-PSSession
Alias           gsnp                                                Get-PSSnapIn
Alias           gsv                                                 Get-Service
Alias           gu                                                  Get-Unique
Alias           gv                                                  Get-Variable
Alias           gwmi                                                Get-WmiObject
Alias           h                                                   Get-History
Function        H:                                                  Set-Location H:
Function        help                                                ...
Alias           history                                             Get-History
Function        I:                                                  Set-Location I:
Alias           icm                                                 Invoke-Command
Alias           iex                                                 Invoke-Expression
Alias           ihy                                                 Invoke-History
Alias           ii                                                  Invoke-Item
Cmdlet          Import-Alias                                        Import-Alias [-Path] <String> [-Scope <String>] ...
Cmdlet          Import-Clixml                                       Import-Clixml [-Path] <String[]> [-Verbose] [-De...
Cmdlet          Import-Counter                                      Import-Counter [-Path] <String[]> [-StartTime <D...
Cmdlet          Import-Csv                                          Import-Csv [-Path] <String[]> [[-Delimiter] <Cha...
Cmdlet          Import-LocalizedData                                Import-LocalizedData [-BindingVariable] <String>...
Cmdlet          Import-Module                                       Import-Module [-Name] <String[]> [-Global] [-Pre...
Cmdlet          Import-PSSession                                    Import-PSSession [-Session] <PSSession> [[-Comma...
Function        ImportSystemModules                                 ...
Cmdlet          Invoke-Command                                      Invoke-Command [-ScriptBlock] <ScriptBlock> [-In...
Cmdlet          Invoke-Expression                                   Invoke-Expression [-Command] <String> [-Verbose]...
Cmdlet          Invoke-History                                      Invoke-History [[-Id] <String>] [-Verbose] [-Deb...
Cmdlet          Invoke-Item                                         Invoke-Item [-Path] <String[]> [-Filter <String>...
Cmdlet          Invoke-WmiMethod                                    Invoke-WmiMethod [-Class] <String> [-Name] <Stri...
Cmdlet          Invoke-WSManAction                                  Invoke-WSManAction [-ResourceURI] <Uri> [-Action...
Alias           ipal                                                Import-Alias
Alias           ipcsv                                               Import-Csv
Alias           ipmo                                                Import-Module
Alias           ipsn                                                Import-PSSession
Alias           ise                                                 powershell_ise.exe
Alias           iwmi                                                Invoke-WMIMethod
Function        J:                                                  Set-Location J:
Cmdlet          Join-Path                                           Join-Path [-Path] <String[]> [-ChildPath] <Strin...
Function        K:                                                  Set-Location K:
Alias           kill                                                Stop-Process
Function        L:                                                  Set-Location L:
Cmdlet          Limit-EventLog                                      Limit-EventLog [-LogName] <String[]> [-ComputerN...
Alias           lp                                                  Out-Printer
Alias           ls                                                  Get-ChildItem
Function        M:                                                  Set-Location M:
Alias           man                                                 help
Alias           md                                                  mkdir
Alias           measure                                             Measure-Object
Cmdlet          Measure-Command                                     Measure-Command [-Expression] <ScriptBlock> [-In...
Cmdlet          Measure-Object                                      Measure-Object [[-Property] <String[]>] [-InputO...
Alias           mi                                                  Move-Item
Function        mkdir                                               ...
Function        more                                                param([string[]]$paths)...
Alias           mount                                               New-PSDrive
Alias           move                                                Move-Item
Cmdlet          Move-Item                                           Move-Item [-Path] <String[]> [[-Destination] <St...
Cmdlet          Move-ItemProperty                                   Move-ItemProperty [-Path] <String[]> [-Destinati...
Alias           mp                                                  Move-ItemProperty
Alias           mv                                                  Move-Item
Function        N:                                                  Set-Location N:
Alias           nal                                                 New-Alias
Alias           ndr                                                 New-PSDrive
Cmdlet          New-Alias                                           New-Alias [-Name] <String> [-Value] <String> [-D...
Cmdlet          New-Event                                           New-Event [-SourceIdentifier] <String> [[-Sender...
Cmdlet          New-EventLog                                        New-EventLog [-LogName] <String> [-Source] <Stri...
Cmdlet          New-Item                                            New-Item [-Path] <String[]> [-ItemType <String>]...
Cmdlet          New-ItemProperty                                    New-ItemProperty [-Path] <String[]> [-Name] <Str...
Cmdlet          New-Module                                          New-Module [-ScriptBlock] <ScriptBlock> [-Functi...
Cmdlet          New-ModuleManifest                                  New-ModuleManifest [-Path] <String> -NestedModul...
Cmdlet          New-Object                                          New-Object [-TypeName] <String> [[-ArgumentList]...
Cmdlet          New-PSDrive                                         New-PSDrive [-Name] <String> [-PSProvider] <Stri...
Cmdlet          New-PSSession                                       New-PSSession [[-ComputerName] <String[]>] [-Cre...
Cmdlet          New-PSSessionOption                                 New-PSSessionOption [-MaximumRedirection <Int32>...
Cmdlet          New-Service                                         New-Service [-Name] <String> [-BinaryPathName] <...
Cmdlet          New-TimeSpan                                        New-TimeSpan [[-Start] <DateTime>] [[-End] <Date...
Cmdlet          New-Variable                                        New-Variable [-Name] <String> [[-Value] <Object>...
Cmdlet          New-WebServiceProxy                                 New-WebServiceProxy [-Uri] <Uri> [[-Class] <Stri...
Cmdlet          New-WSManInstance                                   New-WSManInstance [-ResourceURI] <Uri> [-Selecto...
Cmdlet          New-WSManSessionOption                              New-WSManSessionOption [-ProxyAccessType <ProxyA...
Alias           ni                                                  New-Item
Alias           nmo                                                 New-Module
Alias           nsn                                                 New-PSSession
Alias           nv                                                  New-Variable
Function        O:                                                  Set-Location O:
Alias           ogv                                                 Out-GridView
Alias           oh                                                  Out-Host
Cmdlet          Out-Default                                         Out-Default [-InputObject <PSObject>] [-Verbose]...
Cmdlet          Out-File                                            Out-File [-FilePath] <String> [[-Encoding] <Stri...
Cmdlet          Out-GridView                                        Out-GridView [-InputObject <PSObject>] [-Title <...
Cmdlet          Out-Host                                            Out-Host [-Paging] [-InputObject <PSObject>] [-V...
Cmdlet          Out-Null                                            Out-Null [-InputObject <PSObject>] [-Verbose] [-...
Cmdlet          Out-Printer                                         Out-Printer [[-Name] <String>] [-InputObject <PS...
Cmdlet          Out-String                                          Out-String [-Stream] [-Width <Int32>] [-InputObj...
Function        P:                                                  Set-Location P:
Alias           popd                                                Pop-Location
Cmdlet          Pop-Location                                        Pop-Location [-PassThru] [-StackName <String>] [...
Function        prompt                                              $(if (test-path variable:/PSDebugContext) { '[DB...
Alias           ps                                                  Get-Process
Alias           pushd                                               Push-Location
Cmdlet          Push-Location                                       Push-Location [[-Path] <String>] [-PassThru] [-S...
Alias           pwd                                                 Get-Location
Function        Q:                                                  Set-Location Q:
Alias           r                                                   Invoke-History
Function        R:                                                  Set-Location R:
Alias           rbp                                                 Remove-PSBreakpoint
Alias           rcjb                                                Receive-Job
Alias           rd                                                  Remove-Item
Alias           rdr                                                 Remove-PSDrive
Cmdlet          Read-Host                                           Read-Host [[-Prompt] <Object>] [-AsSecureString]...
Cmdlet          Receive-Job                                         Receive-Job [-Job] <Job[]> [[-Location] <String[...
Cmdlet          Register-EngineEvent                                Register-EngineEvent [-SourceIdentifier] <String...
Cmdlet          Register-ObjectEvent                                Register-ObjectEvent [-InputObject] <PSObject> [...
Cmdlet          Register-PSSessionConfiguration                     Register-PSSessionConfiguration [-Name] <String>...
Cmdlet          Register-WmiEvent                                   Register-WmiEvent [-Class] <String> [[-SourceIde...
Cmdlet          Remove-Computer                                     Remove-Computer [[-Credential] <PSCredential>] [...
Cmdlet          Remove-Event                                        Remove-Event [-SourceIdentifier] <String> [-Verb...
Cmdlet          Remove-EventLog                                     Remove-EventLog [-LogName] <String[]> [[-Compute...
Cmdlet          Remove-Item                                         Remove-Item [-Path] <String[]> [-Filter <String>...
Cmdlet          Remove-ItemProperty                                 Remove-ItemProperty [-Path] <String[]> [-Name] <...
Cmdlet          Remove-Job                                          Remove-Job [-Id] <Int32[]> [-Force] [-Verbose] [...
Cmdlet          Remove-Module                                       Remove-Module [-Name] <String[]> [-Force] [-Verb...
Cmdlet          Remove-PSBreakpoint                                 Remove-PSBreakpoint [-Breakpoint] <Breakpoint[]>...
Cmdlet          Remove-PSDrive                                      Remove-PSDrive [-Name] <String[]> [-PSProvider <...
Cmdlet          Remove-PSSession                                    Remove-PSSession [-Id] <Int32[]> [-Verbose] [-De...
Cmdlet          Remove-PSSnapin                                     Remove-PSSnapin [-Name] <String[]> [-PassThru] [...
Cmdlet          Remove-Variable                                     Remove-Variable [-Name] <String[]> [-Include <St...
Cmdlet          Remove-WmiObject                                    Remove-WmiObject [-Class] <String> [-AsJob] [-Im...
Cmdlet          Remove-WSManInstance                                Remove-WSManInstance [-ResourceURI] <Uri> [-Sele...
Alias           ren                                                 Rename-Item
Cmdlet          Rename-Item                                         Rename-Item [-Path] <String> [-NewName] <String>...
Cmdlet          Rename-ItemProperty                                 Rename-ItemProperty [-Path] <String> [-Name] <St...
Cmdlet          Reset-ComputerMachinePassword                       Reset-ComputerMachinePassword [-Server <String>]...
Cmdlet          Resolve-Path                                        Resolve-Path [-Path] <String[]> [-Relative] [-Cr...
Cmdlet          Restart-Computer                                    Restart-Computer [[-ComputerName] <String[]>] [[...
Cmdlet          Restart-Service                                     Restart-Service [-Name] <String[]> [-Force] [-Pa...
Cmdlet          Restore-Computer                                    Restore-Computer [-RestorePoint] <Int32> [-Verbo...
Cmdlet          Resume-Service                                      Resume-Service [-Name] <String[]> [-PassThru] [-...
Alias           ri                                                  Remove-Item
Alias           rjb                                                 Remove-Job
Alias           rm                                                  Remove-Item
Alias           rmdir                                               Remove-Item
Alias           rmo                                                 Remove-Module
Alias           rni                                                 Rename-Item
Alias           rnp                                                 Rename-ItemProperty
Alias           rp                                                  Remove-ItemProperty
Alias           rsn                                                 Remove-PSSession
Alias           rsnp                                                Remove-PSSnapin
Alias           rv                                                  Remove-Variable
Alias           rvpa                                                Resolve-Path
Alias           rwmi                                                Remove-WMIObject
Function        S:                                                  Set-Location S:
Alias           sajb                                                Start-Job
Alias           sal                                                 Set-Alias
Alias           saps                                                Start-Process
Alias           sasv                                                Start-Service
Alias           sbp                                                 Set-PSBreakpoint
Alias           sc                                                  Set-Content
Alias           select                                              Select-Object
Cmdlet          Select-Object                                       Select-Object [[-Property] <Object[]>] [-InputOb...
Cmdlet          Select-String                                       Select-String [-Pattern] <String[]> -InputObject...
Cmdlet          Select-Xml                                          Select-Xml [-XPath] <String> [-Xml] <XmlNode[]> ...
Cmdlet          Send-MailMessage                                    Send-MailMessage [-To] <String[]> [-Subject] <St...
Alias           set                                                 Set-Variable
Cmdlet          Set-Acl                                             Set-Acl [-Path] <String[]> [-AclObject] <ObjectS...
Cmdlet          Set-Alias                                           Set-Alias [-Name] <String> [-Value] <String> [-D...
Cmdlet          Set-AuthenticodeSignature                           Set-AuthenticodeSignature [-FilePath] <String[]>...
Cmdlet          Set-Content                                         Set-Content [-Path] <String[]> [-Value] <Object[...
Cmdlet          Set-Date                                            Set-Date [-Date] <DateTime> [-DisplayHint <Displ...
Cmdlet          Set-ExecutionPolicy                                 Set-ExecutionPolicy [-ExecutionPolicy] <Executio...
Cmdlet          Set-Item                                            Set-Item [-Path] <String[]> [[-Value] <Object>] ...
Cmdlet          Set-ItemProperty                                    Set-ItemProperty [-Path] <String[]> [-Name] <Str...
Cmdlet          Set-Location                                        Set-Location [[-Path] <String>] [-PassThru] [-Ve...
Cmdlet          Set-PSBreakpoint                                    Set-PSBreakpoint [-Script] <String[]> [-Line] <I...
Cmdlet          Set-PSDebug                                         Set-PSDebug [-Trace <Int32>] [-Step] [-Strict] [...
Cmdlet          Set-PSSessionConfiguration                          Set-PSSessionConfiguration [-Name] <String> [-Ap...
Cmdlet          Set-Service                                         Set-Service [-Name] <String> [-ComputerName <Str...
Cmdlet          Set-StrictMode                                      Set-StrictMode -Version <Version> [-Verbose] [-D...
Cmdlet          Set-TraceSource                                     Set-TraceSource [-Name] <String[]> [[-Option] <P...
Cmdlet          Set-Variable                                        Set-Variable [-Name] <String[]> [[-Value] <Objec...
Cmdlet          Set-WmiInstance                                     Set-WmiInstance [-Class] <String> [[-Arguments] ...
Cmdlet          Set-WSManInstance                                   Set-WSManInstance [-ResourceURI] <Uri> [[-Select...
Cmdlet          Set-WSManQuickConfig                                Set-WSManQuickConfig [-UseSSL] [-Force] [-Verbos...
Cmdlet          Show-EventLog                                       Show-EventLog [[-ComputerName] <String>] [-Verbo...
Alias           si                                                  Set-Item
Alias           sl                                                  Set-Location
Alias           sleep                                               Start-Sleep
Alias           sort                                                Sort-Object
Cmdlet          Sort-Object                                         Sort-Object [[-Property] <Object[]>] [-Descendin...
Alias           sp                                                  Set-ItemProperty
Alias           spjb                                                Stop-Job
Cmdlet          Split-Path                                          Split-Path [-Path] <String[]> [-LiteralPath <Str...
Alias           spps                                                Stop-Process
Alias           spsv                                                Stop-Service
Alias           start                                               Start-Process
Cmdlet          Start-Job                                           Start-Job [-ScriptBlock] <ScriptBlock> [[-Initia...
Cmdlet          Start-Process                                       Start-Process [-FilePath] <String> [[-ArgumentLi...
Cmdlet          Start-Service                                       Start-Service [-Name] <String[]> [-PassThru] [-I...
Cmdlet          Start-Sleep                                         Start-Sleep [-Seconds] <Int32> [-Verbose] [-Debu...
Cmdlet          Start-Transaction                                   Start-Transaction [-Timeout <Int32>] [-Independe...
Cmdlet          Start-Transcript                                    Start-Transcript [[-Path] <String>] [-Append] [-...
Cmdlet          Stop-Computer                                       Stop-Computer [[-ComputerName] <String[]>] [[-Cr...
Cmdlet          Stop-Job                                            Stop-Job [-Id] <Int32[]> [-PassThru] [-Verbose] ...
Cmdlet          Stop-Process                                        Stop-Process [-Id] <Int32[]> [-PassThru] [-Force...
Cmdlet          Stop-Service                                        Stop-Service [-Name] <String[]> [-Force] [-PassT...
Cmdlet          Stop-Transcript                                     Stop-Transcript [-Verbose] [-Debug] [-ErrorActio...
Cmdlet          Suspend-Service                                     Suspend-Service [-Name] <String[]> [-PassThru] [...
Alias           sv                                                  Set-Variable
Alias           swmi                                                Set-WMIInstance
Function        T:                                                  Set-Location T:
Function        TabExpansion                                        ...
Alias           tee                                                 Tee-Object
Cmdlet          Tee-Object                                          Tee-Object [-FilePath] <String> [-InputObject <P...
Cmdlet          Test-ComputerSecureChannel                          Test-ComputerSecureChannel [-Repair] [-Server <S...
Cmdlet          Test-Connection                                     Test-Connection [-ComputerName] <String[]> [[-So...
Cmdlet          Test-ModuleManifest                                 Test-ModuleManifest [-Path] <String> [-Verbose] ...
Cmdlet          Test-Path                                           Test-Path [-Path] <String[]> [-Filter <String>] ...
Cmdlet          Test-WSMan                                          Test-WSMan [[-ComputerName] <String>] [-Authenti...
Cmdlet          Trace-Command                                       Trace-Command [-Name] <String[]> [-Expression] <...
Alias           type                                                Get-Content
Function        U:                                                  Set-Location U:
Cmdlet          Undo-Transaction                                    Undo-Transaction [-Verbose] [-Debug] [-ErrorActi...
Cmdlet          Unregister-Event                                    Unregister-Event [-SourceIdentifier] <String> [-...
Cmdlet          Unregister-PSSessionConfiguration                   Unregister-PSSessionConfiguration [-Name] <Strin...
Cmdlet          Update-FormatData                                   Update-FormatData [[-AppendPath] <String[]>] [-P...
Cmdlet          Update-List                                         Update-List [[-Property] <String>] [-Add <Object...
Cmdlet          Update-TypeData                                     Update-TypeData [[-AppendPath] <String[]>] [-Pre...
Cmdlet          Use-Transaction                                     Use-Transaction [-TransactedScript] <ScriptBlock...
Function        V:                                                  Set-Location V:
Function        W:                                                  Set-Location W:
Cmdlet          Wait-Event                                          Wait-Event [[-SourceIdentifier] <String>] [-Time...
Cmdlet          Wait-Job                                            Wait-Job [-Id] <Int32[]> [-Any] [-Timeout <Int32...
Cmdlet          Wait-Process                                        Wait-Process [-Name] <String[]> [[-Timeout] <Int...
Alias           where                                               Where-Object
Cmdlet          Where-Object                                        Where-Object [-FilterScript] <ScriptBlock> [-Inp...
Alias           wjb                                                 Wait-Job
Alias           write                                               Write-Output
Cmdlet          Write-Debug                                         Write-Debug [-Message] <String> [-Verbose] [-Deb...
Cmdlet          Write-Error                                         Write-Error [-Message] <String> [-Category <Erro...
Cmdlet          Write-EventLog                                      Write-EventLog [-LogName] <String> [-Source] <St...
Cmdlet          Write-Host                                          Write-Host [[-Object] <Object>] [-NoNewline] [-S...
Cmdlet          Write-Output                                        Write-Output [-InputObject] <PSObject[]> [-Verbo...
Cmdlet          Write-Progress                                      Write-Progress [-Activity] <String> [-Status] <S...
Cmdlet          Write-Verbose                                       Write-Verbose [-Message] <String> [-Verbose] [-D...
Cmdlet          Write-Warning                                       Write-Warning [-Message] <String> [-Verbose] [-D...
Function        X:                                                  Set-Location X:
Function        Y:                                                  Set-Location Y:
Function        Z:                                                  Set-Location Z:


PS C:\Users\Windows-32>
```

- Make ```Get-Command``` to only lists ```Cmdlet```

```Powershell
PS C:\Users\Windows-32> Get-Command -CommandType cmdlet

CommandType     Name                                                Definition
-----------     ----                                                ----------
Cmdlet          Add-Computer                                        Add-Computer [-DomainName] <String> [-Credential...
Cmdlet          Add-Content                                         Add-Content [-Path] <String[]> [-Value] <Object[...
Cmdlet          Add-History                                         Add-History [[-InputObject] <PSObject[]>] [-Pass...
Cmdlet          Add-Member                                          Add-Member [-MemberType] <PSMemberTypes> [-Name]...
Cmdlet          Add-PSSnapin                                        Add-PSSnapin [-Name] <String[]> [-PassThru] [-Ve...
Cmdlet          Add-Type                                            Add-Type [-TypeDefinition] <String> [-Language <...
Cmdlet          Checkpoint-Computer                                 Checkpoint-Computer [-Description] <String> [[-R...
Cmdlet          Clear-Content                                       Clear-Content [-Path] <String[]> [-Filter <Strin...
Cmdlet          Clear-EventLog                                      Clear-EventLog [-LogName] <String[]> [[-Computer...
Cmdlet          Clear-History                                       Clear-History [[-Id] <Int32[]>] [[-Count] <Int32...
Cmdlet          Clear-Item                                          Clear-Item [-Path] <String[]> [-Force] [-Filter ...
Cmdlet          Clear-ItemProperty                                  Clear-ItemProperty [-Path] <String[]> [-Name] <S...
Cmdlet          Clear-Variable                                      Clear-Variable [-Name] <String[]> [-Include <Str...
Cmdlet          Compare-Object                                      Compare-Object [-ReferenceObject] <PSObject[]> [...
Cmdlet          Complete-Transaction                                Complete-Transaction [-Verbose] [-Debug] [-Error...
Cmdlet          Connect-WSMan                                       Connect-WSMan [[-ComputerName] <String>] [-Appli...
Cmdlet          ConvertFrom-Csv                                     ConvertFrom-Csv [-InputObject] <PSObject[]> [[-D...
Cmdlet          ConvertFrom-SecureString                            ConvertFrom-SecureString [-SecureString] <Secure...
Cmdlet          ConvertFrom-StringData                              ConvertFrom-StringData [-StringData] <String> [-...
Cmdlet          Convert-Path                                        Convert-Path [-Path] <String[]> [-Verbose] [-Deb...
Cmdlet          ConvertTo-Csv                                       ConvertTo-Csv [-InputObject] <PSObject> [[-Delim...
Cmdlet          ConvertTo-Html                                      ConvertTo-Html [[-Property] <Object[]>] [[-Head]...
Cmdlet          ConvertTo-SecureString                              ConvertTo-SecureString [-String] <String> [[-Sec...
Cmdlet          ConvertTo-Xml                                       ConvertTo-Xml [-InputObject] <PSObject> [-Depth ...
Cmdlet          Copy-Item                                           Copy-Item [-Path] <String[]> [[-Destination] <St...
Cmdlet          Copy-ItemProperty                                   Copy-ItemProperty [-Path] <String[]> [-Destinati...
Cmdlet          Debug-Process                                       Debug-Process [-Name] <String[]> [-Verbose] [-De...
Cmdlet          Disable-ComputerRestore                             Disable-ComputerRestore [-Drive] <String[]> [-Ve...
Cmdlet          Disable-PSBreakpoint                                Disable-PSBreakpoint [-Breakpoint] <Breakpoint[]...
Cmdlet          Disable-PSSessionConfiguration                      Disable-PSSessionConfiguration [[-Name] <String[...
Cmdlet          Disable-WSManCredSSP                                Disable-WSManCredSSP [-Role] <String> [-Verbose]...
Cmdlet          Disconnect-WSMan                                    Disconnect-WSMan [[-ComputerName] <String>] [-Ve...
Cmdlet          Enable-ComputerRestore                              Enable-ComputerRestore [-Drive] <String[]> [-Ver...
Cmdlet          Enable-PSBreakpoint                                 Enable-PSBreakpoint [-Id] <Int32[]> [-PassThru] ...
Cmdlet          Enable-PSRemoting                                   Enable-PSRemoting [-Force] [-Verbose] [-Debug] [...
Cmdlet          Enable-PSSessionConfiguration                       Enable-PSSessionConfiguration [[-Name] <String[]...
Cmdlet          Enable-WSManCredSSP                                 Enable-WSManCredSSP [-Role] <String> [[-Delegate...
Cmdlet          Enter-PSSession                                     Enter-PSSession [-ComputerName] <String> [-Crede...
Cmdlet          Exit-PSSession                                      Exit-PSSession [-Verbose] [-Debug] [-ErrorAction...
Cmdlet          Export-Alias                                        Export-Alias [-Path] <String> [[-Name] <String[]...
Cmdlet          Export-Clixml                                       Export-Clixml [-Path] <String> [-Depth <Int32>] ...
Cmdlet          Export-Console                                      Export-Console [[-Path] <String>] [-Force] [-NoC...
Cmdlet          Export-Counter                                      Export-Counter [-Path] <String> [-FileFormat <St...
Cmdlet          Export-Csv                                          Export-Csv [-Path] <String> [[-Delimiter] <Char>...
Cmdlet          Export-FormatData                                   Export-FormatData [-InputObject <ExtendedTypeDef...
Cmdlet          Export-ModuleMember                                 Export-ModuleMember [[-Function] <String[]>] [-C...
Cmdlet          Export-PSSession                                    Export-PSSession [-Session] <PSSession> [-Output...
Cmdlet          ForEach-Object                                      ForEach-Object [-Process] <ScriptBlock[]> [-Inpu...
Cmdlet          Format-Custom                                       Format-Custom [[-Property] <Object[]>] [-Depth <...
Cmdlet          Format-List                                         Format-List [[-Property] <Object[]>] [-GroupBy <...
Cmdlet          Format-Table                                        Format-Table [[-Property] <Object[]>] [-AutoSize...
Cmdlet          Format-Wide                                         Format-Wide [[-Property] <Object>] [-AutoSize] [...
Cmdlet          Get-Acl                                             Get-Acl [[-Path] <String[]>] [-Audit] [-Filter <...
Cmdlet          Get-Alias                                           Get-Alias [[-Name] <String[]>] [-Exclude <String...
Cmdlet          Get-AuthenticodeSignature                           Get-AuthenticodeSignature [-FilePath] <String[]>...
Cmdlet          Get-ChildItem                                       Get-ChildItem [[-Path] <String[]>] [[-Filter] <S...
Cmdlet          Get-Command                                         Get-Command [[-ArgumentList] <Object[]>] [-Verb ...
Cmdlet          Get-ComputerRestorePoint                            Get-ComputerRestorePoint [[-RestorePoint] <Int32...
Cmdlet          Get-Content                                         Get-Content [-Path] <String[]> [-ReadCount <Int6...
Cmdlet          Get-Counter                                         Get-Counter [[-Counter] <String[]>] [-SampleInte...
Cmdlet          Get-Credential                                      Get-Credential [-Credential] <PSCredential> [-Ve...
Cmdlet          Get-Culture                                         Get-Culture [-Verbose] [-Debug] [-ErrorAction <A...
Cmdlet          Get-Date                                            Get-Date [[-Date] <DateTime>] [-Year <Int32>] [-...
Cmdlet          Get-Event                                           Get-Event [[-SourceIdentifier] <String>] [-Verbo...
Cmdlet          Get-EventLog                                        Get-EventLog [-LogName] <String> [[-InstanceId] ...
Cmdlet          Get-EventSubscriber                                 Get-EventSubscriber [[-SourceIdentifier] <String...
Cmdlet          Get-ExecutionPolicy                                 Get-ExecutionPolicy [[-Scope] <ExecutionPolicySc...
Cmdlet          Get-FormatData                                      Get-FormatData [[-TypeName] <String[]>] [-Verbos...
Cmdlet          Get-Help                                            Get-Help [[-Name] <String>] [-Path <String>] [-C...
Cmdlet          Get-History                                         Get-History [[-Id] <Int64[]>] [[-Count] <Int32>]...
Cmdlet          Get-Host                                            Get-Host [-Verbose] [-Debug] [-ErrorAction <Acti...
Cmdlet          Get-HotFix                                          Get-HotFix [[-Id] <String[]>] [-ComputerName <St...
Cmdlet          Get-Item                                            Get-Item [-Path] <String[]> [-Filter <String>] [...
Cmdlet          Get-ItemProperty                                    Get-ItemProperty [-Path] <String[]> [[-Name] <St...
Cmdlet          Get-Job                                             Get-Job [[-Id] <Int32[]>] [-Verbose] [-Debug] [-...
Cmdlet          Get-Location                                        Get-Location [-PSProvider <String[]>] [-PSDrive ...
Cmdlet          Get-Member                                          Get-Member [[-Name] <String[]>] [-InputObject <P...
Cmdlet          Get-Module                                          Get-Module [[-Name] <String[]>] [-All] [-Verbose...
Cmdlet          Get-PfxCertificate                                  Get-PfxCertificate [-FilePath] <String[]> [-Verb...
Cmdlet          Get-Process                                         Get-Process [[-Name] <String[]>] [-ComputerName ...
Cmdlet          Get-PSBreakpoint                                    Get-PSBreakpoint [[-Script] <String[]>] [-Verbos...
Cmdlet          Get-PSCallStack                                     Get-PSCallStack [-Verbose] [-Debug] [-ErrorActio...
Cmdlet          Get-PSDrive                                         Get-PSDrive [[-Name] <String[]>] [-Scope <String...
Cmdlet          Get-PSProvider                                      Get-PSProvider [[-PSProvider] <String[]>] [-Verb...
Cmdlet          Get-PSSession                                       Get-PSSession [[-ComputerName] <String[]>] [-Ver...
Cmdlet          Get-PSSessionConfiguration                          Get-PSSessionConfiguration [[-Name] <String[]>] ...
Cmdlet          Get-PSSnapin                                        Get-PSSnapin [[-Name] <String[]>] [-Registered] ...
Cmdlet          Get-Random                                          Get-Random [[-Maximum] <Object>] [-SetSeed <Null...
Cmdlet          Get-Service                                         Get-Service [[-Name] <String[]>] [-ComputerName ...
Cmdlet          Get-TraceSource                                     Get-TraceSource [[-Name] <String[]>] [-Verbose] ...
Cmdlet          Get-Transaction                                     Get-Transaction [-Verbose] [-Debug] [-ErrorActio...
Cmdlet          Get-UICulture                                       Get-UICulture [-Verbose] [-Debug] [-ErrorAction ...
Cmdlet          Get-Unique                                          Get-Unique [-InputObject <PSObject>] [-AsString]...
Cmdlet          Get-Variable                                        Get-Variable [[-Name] <String[]>] [-ValueOnly] [...
Cmdlet          Get-WinEvent                                        Get-WinEvent [[-LogName] <String[]>] [-MaxEvents...
Cmdlet          Get-WmiObject                                       Get-WmiObject [-Class] <String> [[-Property] <St...
Cmdlet          Get-WSManCredSSP                                    Get-WSManCredSSP [-Verbose] [-Debug] [-ErrorActi...
Cmdlet          Get-WSManInstance                                   Get-WSManInstance [-ResourceURI] <Uri> [-Applica...
Cmdlet          Group-Object                                        Group-Object [[-Property] <Object[]>] [-NoElemen...
Cmdlet          Import-Alias                                        Import-Alias [-Path] <String> [-Scope <String>] ...
Cmdlet          Import-Clixml                                       Import-Clixml [-Path] <String[]> [-Verbose] [-De...
Cmdlet          Import-Counter                                      Import-Counter [-Path] <String[]> [-StartTime <D...
Cmdlet          Import-Csv                                          Import-Csv [-Path] <String[]> [[-Delimiter] <Cha...
Cmdlet          Import-LocalizedData                                Import-LocalizedData [-BindingVariable] <String>...
Cmdlet          Import-Module                                       Import-Module [-Name] <String[]> [-Global] [-Pre...
Cmdlet          Import-PSSession                                    Import-PSSession [-Session] <PSSession> [[-Comma...
Cmdlet          Invoke-Command                                      Invoke-Command [-ScriptBlock] <ScriptBlock> [-In...
Cmdlet          Invoke-Expression                                   Invoke-Expression [-Command] <String> [-Verbose]...
Cmdlet          Invoke-History                                      Invoke-History [[-Id] <String>] [-Verbose] [-Deb...
Cmdlet          Invoke-Item                                         Invoke-Item [-Path] <String[]> [-Filter <String>...
Cmdlet          Invoke-WmiMethod                                    Invoke-WmiMethod [-Class] <String> [-Name] <Stri...
Cmdlet          Invoke-WSManAction                                  Invoke-WSManAction [-ResourceURI] <Uri> [-Action...
Cmdlet          Join-Path                                           Join-Path [-Path] <String[]> [-ChildPath] <Strin...
Cmdlet          Limit-EventLog                                      Limit-EventLog [-LogName] <String[]> [-ComputerN...
Cmdlet          Measure-Command                                     Measure-Command [-Expression] <ScriptBlock> [-In...
Cmdlet          Measure-Object                                      Measure-Object [[-Property] <String[]>] [-InputO...
Cmdlet          Move-Item                                           Move-Item [-Path] <String[]> [[-Destination] <St...
Cmdlet          Move-ItemProperty                                   Move-ItemProperty [-Path] <String[]> [-Destinati...
Cmdlet          New-Alias                                           New-Alias [-Name] <String> [-Value] <String> [-D...
Cmdlet          New-Event                                           New-Event [-SourceIdentifier] <String> [[-Sender...
Cmdlet          New-EventLog                                        New-EventLog [-LogName] <String> [-Source] <Stri...
Cmdlet          New-Item                                            New-Item [-Path] <String[]> [-ItemType <String>]...
Cmdlet          New-ItemProperty                                    New-ItemProperty [-Path] <String[]> [-Name] <Str...
Cmdlet          New-Module                                          New-Module [-ScriptBlock] <ScriptBlock> [-Functi...
Cmdlet          New-ModuleManifest                                  New-ModuleManifest [-Path] <String> -NestedModul...
Cmdlet          New-Object                                          New-Object [-TypeName] <String> [[-ArgumentList]...
Cmdlet          New-PSDrive                                         New-PSDrive [-Name] <String> [-PSProvider] <Stri...
Cmdlet          New-PSSession                                       New-PSSession [[-ComputerName] <String[]>] [-Cre...
Cmdlet          New-PSSessionOption                                 New-PSSessionOption [-MaximumRedirection <Int32>...
Cmdlet          New-Service                                         New-Service [-Name] <String> [-BinaryPathName] <...
Cmdlet          New-TimeSpan                                        New-TimeSpan [[-Start] <DateTime>] [[-End] <Date...
Cmdlet          New-Variable                                        New-Variable [-Name] <String> [[-Value] <Object>...
Cmdlet          New-WebServiceProxy                                 New-WebServiceProxy [-Uri] <Uri> [[-Class] <Stri...
Cmdlet          New-WSManInstance                                   New-WSManInstance [-ResourceURI] <Uri> [-Selecto...
Cmdlet          New-WSManSessionOption                              New-WSManSessionOption [-ProxyAccessType <ProxyA...
Cmdlet          Out-Default                                         Out-Default [-InputObject <PSObject>] [-Verbose]...
Cmdlet          Out-File                                            Out-File [-FilePath] <String> [[-Encoding] <Stri...
Cmdlet          Out-GridView                                        Out-GridView [-InputObject <PSObject>] [-Title <...
Cmdlet          Out-Host                                            Out-Host [-Paging] [-InputObject <PSObject>] [-V...
Cmdlet          Out-Null                                            Out-Null [-InputObject <PSObject>] [-Verbose] [-...
Cmdlet          Out-Printer                                         Out-Printer [[-Name] <String>] [-InputObject <PS...
Cmdlet          Out-String                                          Out-String [-Stream] [-Width <Int32>] [-InputObj...
Cmdlet          Pop-Location                                        Pop-Location [-PassThru] [-StackName <String>] [...
Cmdlet          Push-Location                                       Push-Location [[-Path] <String>] [-PassThru] [-S...
Cmdlet          Read-Host                                           Read-Host [[-Prompt] <Object>] [-AsSecureString]...
Cmdlet          Receive-Job                                         Receive-Job [-Job] <Job[]> [[-Location] <String[...
Cmdlet          Register-EngineEvent                                Register-EngineEvent [-SourceIdentifier] <String...
Cmdlet          Register-ObjectEvent                                Register-ObjectEvent [-InputObject] <PSObject> [...
Cmdlet          Register-PSSessionConfiguration                     Register-PSSessionConfiguration [-Name] <String>...
Cmdlet          Register-WmiEvent                                   Register-WmiEvent [-Class] <String> [[-SourceIde...
Cmdlet          Remove-Computer                                     Remove-Computer [[-Credential] <PSCredential>] [...
Cmdlet          Remove-Event                                        Remove-Event [-SourceIdentifier] <String> [-Verb...
Cmdlet          Remove-EventLog                                     Remove-EventLog [-LogName] <String[]> [[-Compute...
Cmdlet          Remove-Item                                         Remove-Item [-Path] <String[]> [-Filter <String>...
Cmdlet          Remove-ItemProperty                                 Remove-ItemProperty [-Path] <String[]> [-Name] <...
Cmdlet          Remove-Job                                          Remove-Job [-Id] <Int32[]> [-Force] [-Verbose] [...
Cmdlet          Remove-Module                                       Remove-Module [-Name] <String[]> [-Force] [-Verb...
Cmdlet          Remove-PSBreakpoint                                 Remove-PSBreakpoint [-Breakpoint] <Breakpoint[]>...
Cmdlet          Remove-PSDrive                                      Remove-PSDrive [-Name] <String[]> [-PSProvider <...
Cmdlet          Remove-PSSession                                    Remove-PSSession [-Id] <Int32[]> [-Verbose] [-De...
Cmdlet          Remove-PSSnapin                                     Remove-PSSnapin [-Name] <String[]> [-PassThru] [...
Cmdlet          Remove-Variable                                     Remove-Variable [-Name] <String[]> [-Include <St...
Cmdlet          Remove-WmiObject                                    Remove-WmiObject [-Class] <String> [-AsJob] [-Im...
Cmdlet          Remove-WSManInstance                                Remove-WSManInstance [-ResourceURI] <Uri> [-Sele...
Cmdlet          Rename-Item                                         Rename-Item [-Path] <String> [-NewName] <String>...
Cmdlet          Rename-ItemProperty                                 Rename-ItemProperty [-Path] <String> [-Name] <St...
Cmdlet          Reset-ComputerMachinePassword                       Reset-ComputerMachinePassword [-Server <String>]...
Cmdlet          Resolve-Path                                        Resolve-Path [-Path] <String[]> [-Relative] [-Cr...
Cmdlet          Restart-Computer                                    Restart-Computer [[-ComputerName] <String[]>] [[...
Cmdlet          Restart-Service                                     Restart-Service [-Name] <String[]> [-Force] [-Pa...
Cmdlet          Restore-Computer                                    Restore-Computer [-RestorePoint] <Int32> [-Verbo...
Cmdlet          Resume-Service                                      Resume-Service [-Name] <String[]> [-PassThru] [-...
Cmdlet          Select-Object                                       Select-Object [[-Property] <Object[]>] [-InputOb...
Cmdlet          Select-String                                       Select-String [-Pattern] <String[]> -InputObject...
Cmdlet          Select-Xml                                          Select-Xml [-XPath] <String> [-Xml] <XmlNode[]> ...
Cmdlet          Send-MailMessage                                    Send-MailMessage [-To] <String[]> [-Subject] <St...
Cmdlet          Set-Acl                                             Set-Acl [-Path] <String[]> [-AclObject] <ObjectS...
Cmdlet          Set-Alias                                           Set-Alias [-Name] <String> [-Value] <String> [-D...
Cmdlet          Set-AuthenticodeSignature                           Set-AuthenticodeSignature [-FilePath] <String[]>...
Cmdlet          Set-Content                                         Set-Content [-Path] <String[]> [-Value] <Object[...
Cmdlet          Set-Date                                            Set-Date [-Date] <DateTime> [-DisplayHint <Displ...
Cmdlet          Set-ExecutionPolicy                                 Set-ExecutionPolicy [-ExecutionPolicy] <Executio...
Cmdlet          Set-Item                                            Set-Item [-Path] <String[]> [[-Value] <Object>] ...
Cmdlet          Set-ItemProperty                                    Set-ItemProperty [-Path] <String[]> [-Name] <Str...
Cmdlet          Set-Location                                        Set-Location [[-Path] <String>] [-PassThru] [-Ve...
Cmdlet          Set-PSBreakpoint                                    Set-PSBreakpoint [-Script] <String[]> [-Line] <I...
Cmdlet          Set-PSDebug                                         Set-PSDebug [-Trace <Int32>] [-Step] [-Strict] [...
Cmdlet          Set-PSSessionConfiguration                          Set-PSSessionConfiguration [-Name] <String> [-Ap...
Cmdlet          Set-Service                                         Set-Service [-Name] <String> [-ComputerName <Str...
Cmdlet          Set-StrictMode                                      Set-StrictMode -Version <Version> [-Verbose] [-D...
Cmdlet          Set-TraceSource                                     Set-TraceSource [-Name] <String[]> [[-Option] <P...
Cmdlet          Set-Variable                                        Set-Variable [-Name] <String[]> [[-Value] <Objec...
Cmdlet          Set-WmiInstance                                     Set-WmiInstance [-Class] <String> [[-Arguments] ...
Cmdlet          Set-WSManInstance                                   Set-WSManInstance [-ResourceURI] <Uri> [[-Select...
Cmdlet          Set-WSManQuickConfig                                Set-WSManQuickConfig [-UseSSL] [-Force] [-Verbos...
Cmdlet          Show-EventLog                                       Show-EventLog [[-ComputerName] <String>] [-Verbo...
Cmdlet          Sort-Object                                         Sort-Object [[-Property] <Object[]>] [-Descendin...
Cmdlet          Split-Path                                          Split-Path [-Path] <String[]> [-LiteralPath <Str...
Cmdlet          Start-Job                                           Start-Job [-ScriptBlock] <ScriptBlock> [[-Initia...
Cmdlet          Start-Process                                       Start-Process [-FilePath] <String> [[-ArgumentLi...
Cmdlet          Start-Service                                       Start-Service [-Name] <String[]> [-PassThru] [-I...
Cmdlet          Start-Sleep                                         Start-Sleep [-Seconds] <Int32> [-Verbose] [-Debu...
Cmdlet          Start-Transaction                                   Start-Transaction [-Timeout <Int32>] [-Independe...
Cmdlet          Start-Transcript                                    Start-Transcript [[-Path] <String>] [-Append] [-...
Cmdlet          Stop-Computer                                       Stop-Computer [[-ComputerName] <String[]>] [[-Cr...
Cmdlet          Stop-Job                                            Stop-Job [-Id] <Int32[]> [-PassThru] [-Verbose] ...
Cmdlet          Stop-Process                                        Stop-Process [-Id] <Int32[]> [-PassThru] [-Force...
Cmdlet          Stop-Service                                        Stop-Service [-Name] <String[]> [-Force] [-PassT...
Cmdlet          Stop-Transcript                                     Stop-Transcript [-Verbose] [-Debug] [-ErrorActio...
Cmdlet          Suspend-Service                                     Suspend-Service [-Name] <String[]> [-PassThru] [...
Cmdlet          Tee-Object                                          Tee-Object [-FilePath] <String> [-InputObject <P...
Cmdlet          Test-ComputerSecureChannel                          Test-ComputerSecureChannel [-Repair] [-Server <S...
Cmdlet          Test-Connection                                     Test-Connection [-ComputerName] <String[]> [[-So...
Cmdlet          Test-ModuleManifest                                 Test-ModuleManifest [-Path] <String> [-Verbose] ...
Cmdlet          Test-Path                                           Test-Path [-Path] <String[]> [-Filter <String>] ...
Cmdlet          Test-WSMan                                          Test-WSMan [[-ComputerName] <String>] [-Authenti...
Cmdlet          Trace-Command                                       Trace-Command [-Name] <String[]> [-Expression] <...
Cmdlet          Undo-Transaction                                    Undo-Transaction [-Verbose] [-Debug] [-ErrorActi...
Cmdlet          Unregister-Event                                    Unregister-Event [-SourceIdentifier] <String> [-...
Cmdlet          Unregister-PSSessionConfiguration                   Unregister-PSSessionConfiguration [-Name] <Strin...
Cmdlet          Update-FormatData                                   Update-FormatData [[-AppendPath] <String[]>] [-P...
Cmdlet          Update-List                                         Update-List [[-Property] <String>] [-Add <Object...
Cmdlet          Update-TypeData                                     Update-TypeData [[-AppendPath] <String[]>] [-Pre...
Cmdlet          Use-Transaction                                     Use-Transaction [-TransactedScript] <ScriptBlock...
Cmdlet          Wait-Event                                          Wait-Event [[-SourceIdentifier] <String>] [-Time...
Cmdlet          Wait-Job                                            Wait-Job [-Id] <Int32[]> [-Any] [-Timeout <Int32...
Cmdlet          Wait-Process                                        Wait-Process [-Name] <String[]> [[-Timeout] <Int...
Cmdlet          Where-Object                                        Where-Object [-FilterScript] <ScriptBlock> [-Inp...
Cmdlet          Write-Debug                                         Write-Debug [-Message] <String> [-Verbose] [-Deb...
Cmdlet          Write-Error                                         Write-Error [-Message] <String> [-Category <Erro...
Cmdlet          Write-EventLog                                      Write-EventLog [-LogName] <String> [-Source] <St...
Cmdlet          Write-Host                                          Write-Host [[-Object] <Object>] [-NoNewline] [-S...
Cmdlet          Write-Output                                        Write-Output [-InputObject] <PSObject[]> [-Verbo...
Cmdlet          Write-Progress                                      Write-Progress [-Activity] <String> [-Status] <S...
Cmdlet          Write-Verbose                                       Write-Verbose [-Message] <String> [-Verbose] [-D...
Cmdlet          Write-Warning                                       Write-Warning [-Message] <String> [-Verbose] [-D...


PS C:\Users\Windows-32>
```

- ```Print full help```

```Powershell
PS C:\Users\Windows-32> Get-Help Get-Command -full

NAME
    Get-Command

SYNOPSIS
    Gets basic information about cmdlets and other elements of Windows PowerShell commands.

SYNTAX
    Get-Command [[-Name] <string[]>] [-CommandType {Alias | Function | Filter | Cmdlet | ExternalScript | Application |
     Script | All}] [[-ArgumentList] <Object[]>] [-Module <string[]>] [-Syntax] [-TotalCount <int>] [<CommonParameters>
    ]

    Get-Command [-Noun <string[]>] [-Verb <string[]>] [[-ArgumentList] <Object[]>] [-Module <string[]>] [-Syntax] [-Tot
    alCount <int>] [<CommonParameters>]


DESCRIPTION
    The Get-Command cmdlet gets basic information about cmdlets and other elements of Windows PowerShell commands in th
    e session, such as aliases, functions, filters, scripts, and applications.

    Get-Command gets its data directly from the code of a cmdlet, function, script, or alias, unlike Get-Help, which ge
    ts its information from help topic files.

    Without parameters, "Get-Command" gets all of the cmdlets and functions in the current session. "Get-Command *" get
    s all Windows PowerShell elements and all of the non-Windows-PowerShell files in the Path environment variable ($en
    v:path). It groups the files in the "Application" command type.

    You can use the Module parameter of Get-Command to find the commands that were added to the session by adding a Win
    dows PowerShell snap-in or importing a module.


PARAMETERS
    -ArgumentList <Object[]>
        Gets information about a cmdlet or function when it is used with the specified  parameters ("arguments"), such
        as a path.  The alias for ArgumentList is Args.

        To detect parameters that are added to a cmdlet when it is used with a particular provider, set the value of Ar
        gumentList to a path in the provider drive, such as "HKML\Software" or "cert:\my".

        Required?                    false
        Position?                    2
        Default value
        Accept pipeline input?       false
        Accept wildcard characters?  false

    -CommandType <CommandTypes>
        Gets only the specified types of commands. Use "CommandType" or its alias, "Type". By default, Get-Command gets
         cmdlets and functions.

        Valid values are:
        -- Alias: All Windows PowerShell aliases in the current session.

        -- All: All command types. It is the equivalent of "get-command *".

        -- Application: All non-Windows-PowerShell files in paths listed in the Path environment variable ($env:path),
        including .txt, .exe, and .dll files.

        -- Cmdlet: The cmdlets in the current session. "Cmdlet" is the default.

        -- ExternalScript: All .ps1 files in the paths listed in the Path environment variable ($env:path).

        -- Filter and Function: All Windows PowerShell functions.

        -- Script: Script blocks in the current session.

        Required?                    false
        Position?                    named
        Default value
        Accept pipeline input?       true (ByPropertyName)
        Accept wildcard characters?  false

    -Module <string[]>
        Gets the commands that came from the specified modules or snap-ins. Enter the names of modules or snap-ins, or
        enter snap-in or module objects.

        You can refer to this parameter by its name, Module, or by its alias, PSSnapin. The parameter name that you cho
        ose has no effect on the command or its output.

        This parameter takes string values, but you can also supply a PSModuleInfo or PSSnapinInfo object, such as the
        objects that Get-Module, Get-PSSnapin, and Import-PSSession return.

        Required?                    false
        Position?                    named
        Default value                None
        Accept pipeline input?       true (ByPropertyName)
        Accept wildcard characters?  false

    -Name <string[]>
        Gets information only about the cmdlets or command elements with the specified name. <String> represents all or
         part of the name of the cmdlet or command element. Wildcards are permitted.

        To list commands with the same name in execution order, type the command name without wildcard characters. For
        more information, see the Notes section.

        Required?                    false
        Position?                    1
        Default value
        Accept pipeline input?       true (ByValue, ByPropertyName)
        Accept wildcard characters?  false

    -Noun <string[]>
        Gets cmdlets and functions with names that include the specified noun. <String> represents one or more nouns or
         noun patterns, such as "process" or "*item*". Wildcards are permitted.

        Required?                    false
        Position?                    named
        Default value
        Accept pipeline input?       true (ByPropertyName)
        Accept wildcard characters?  false

    -Syntax [<SwitchParameter>]
        Gets only specified data about the command element.
                   * For aliases, retrieves the standard name.
                   * For cmdlets, retrieves the syntax.
                   * For functions and filters, retrieves the function definition.
                   * For scripts and applications (files), retrieves the path and filename.

        Required?                    false
        Position?                    named
        Default value
        Accept pipeline input?       true (ByPropertyName)
        Accept wildcard characters?  false

    -TotalCount <int>
        Gets only the specified number of command elements. You can use this parameter to limit the output of a command
        .

        Required?                    false
        Position?                    named
        Default value
        Accept pipeline input?       true (ByPropertyName)
        Accept wildcard characters?  false

    -Verb <string[]>
        Gets information about cmdlets and functions with names that include the specified verb. <String> represents on
        e or more verbs or verb patterns, such as "remove" or *et". Wildcards are permitted.

        Required?                    false
        Position?                    named
        Default value
        Accept pipeline input?       true (ByPropertyName)
        Accept wildcard characters?  false

    <CommonParameters>
        This cmdlet supports the common parameters: Verbose, Debug,
        ErrorAction, ErrorVariable, WarningAction, WarningVariable,
        OutBuffer and OutVariable. For more information, type,
        "get-help about_commonparameters".

INPUTS
    System.String
        You can pipe a "Name", "Command", and "Verb" noun-property specified, or a string object to Get-Command.


OUTPUTS
    Object
        The type of object returned depends on the type of command element retrieved. For example, Get-Command on a cmd
        let retrieves a CmdletInfo object, while Get-Command on a DLL retrieves an ApplicationInfo object.


NOTES


        Without parameters, "Get-Command" gets information about the Windows PowerShell cmdlets and functions. Use the
        parameters to qualify the elements retrieved.

        Unlike Get-Help, which displays the contents of XML-based help topic files, Get-Command gets its cmdlet informa
        tion directly from the cmdlet code in the system.

        Get-Command returns the commands in alphabetical order. When the session contains more than one command with th
        e same name, Get-Command returns the commands in execution order.  The first command that is listed is the comm
        and that runs when you type the command name without qualification. For more information, see about_Command_Pre
        cedence.


    -------------------------- EXAMPLE 1 --------------------------

    C:\PS>get-command


    Description
    -----------
    This command gets information about all of the Windows PowerShell cmdlets and functions.

    The default display lists the command type ("Cmdlet" or "Function" or "Filter"), the name of the cmdlet or function
    , and the syntax or function definition.





    -------------------------- EXAMPLE 2 --------------------------

    C:\PS>get-command -verb set | format-list


    Description
    -----------
    This command gets information about all of the cmdlets and functions with the verb "set", and it displays some of t
    hat information in a list.

    The list format includes fields that are omitted from the table display, including the complete syntax. To display
    all fields (all properties of the object), type "get-command -verb set | format-list *".





    -------------------------- EXAMPLE 3 --------------------------

    C:\PS>get-command -type cmdlet | sort-object noun | format-table -group noun


    Description
    -----------
    This command retrieves all of the cmdlets, sorts them alphabetically by the noun in the cmdlet name, and then displ
    ays them in noun-based
    groups. This display can help you find the cmdlets for a task.

    By default, Get-Command displays items in the order in which the system discovers them, which is also the order in
    which they are selected to run when a run command is ambiguous.





    -------------------------- EXAMPLE 4 --------------------------

    C:\PS>get-command -module Microsoft.PowerShell.Security, TestModule


    Description
    -----------
    This command gets the commands in the Microsoft.PowerShell.Security snap-in and the Test-Module module.

    The Module parameter gets commands that were added by importing modules or adding Windows PowerShell snap-ins.





    -------------------------- EXAMPLE 5 --------------------------

    C:\PS>get-command get-childitem -args cert: -syntax


    Description
    -----------
    This command retrieves information about the Get-ChildItem cmdlet when Get-ChildItem is used with the Windows Power
    Shell Certificate provider.

    When you compare the syntax displayed in the output with the syntax that is displayed when you omit the Args (Argum
    entList) parameter, you'll see that the Certificate provider dynamically adds a parameter, CodeSigningCert, to the
    Get-ChildItem cmdlet.





    -------------------------- EXAMPLE 6 --------------------------

    C:\PS>(get-command get-childitem -ArgumentList cert:).parametersets[0].parameters | where-object { $_.IsDynamic }


    Description
    -----------
    This command retrieves only parameters that are added to the Get-ChildItem cmdlet dynamically when it is used with
    the Windows PowerShell Certificate provider. This is an alternative to the method used in the previous example.

    In this command, the "get-command get-childitem -ArgumentList cert:" is processed first. It requests information fr
    om Get-Command about the Get-ChildItem cmdlet when it is used with the Certificate provider. The ".parametersets[0]
    " selects the first parameter set (set 0) of "get-childitem -argumentList cert:" and ".parameters" selects the para
    meters in that parameter set. The resulting parameters are piped to the Where-Object cmdlet to test each parameter
    ("$_.") by using the IsDynamic property. To find the properties of the objects in a command, use Get-Member.





    -------------------------- EXAMPLE 7 --------------------------

    C:\PS>get-command *


    Description
    -----------
    This command gets information about the Windows PowerShell cmdlets, functions, filters, scripts, and aliases in the
     current console.

    It also gets information about all of the files in the paths of the Path environment variable ($env:path). It retur
    ns an ApplicationInfo object (System.Management.Automation.ApplicationInfo) for each file, not a FileInfo object (S
    ystem.IO.FileInfo).





    -------------------------- EXAMPLE 8 --------------------------

    C:\PS>get-command | where-object {$_.definition -like "*first*"}

    CommandType     Name                        Definition
    -----------     ----                        ---------
    Cmdlet          Select-Object               Select-Object [[-Property]


    Description
    -----------
    This command finds a cmdlet or function based on the name of one of its parameters. You can use this command to ide
    ntify a cmdlet or function when all that you can recall is the name of one of its parameters.

    In this case, you recall that one of the cmdlets or functions has a First parameter that gets the first "n" objects
     in a list, but you cannot remember which cmdlet it is.

    This command uses the Get-Command cmdlet to get a CmdletInfo object representing each of the cmdlets and functions
    in the session. The CmdletInfo object has a Definition property that contains the syntax of the cmdlet or function,
     which includes its parameters.

    The command uses a pipeline operator (|) to pass the CmdletInfo object to the Where-Object cmdlet, which examines t
    he definition (syntax) of each object ($_) for a value that includes "first".

    The result shows that the First parameter belongs to the Select-Object cmdlet.





    -------------------------- EXAMPLE 9 --------------------------

    C:\PS>get-command dir | format-list

    Name              : dir
    CommandType       : Alias
    Definition        : Get-ChildItem
    ReferencedCommand : Get-ChildItem
    ResolvedCommand   : Get-ChildItem


    Description
    -----------
    This example shows how to use the Get-Command cmdlet with an alias. Although it is typically used on cmdlets, Get-C
    ommand also displays information about the code in scripts, functions, aliases, and executable files.

    This command displays the "dir" alias in the current console. The command pipes the result to the Format-List cmdle
    ts.





    -------------------------- EXAMPLE 10 --------------------------

    C:\PS>get-command notepad

    CommandType     Name           Definition
    -----------     ----           ----------
    Application     notepad.exe    C:\WINDOWS\system32\notepad.exe
    Application     NOTEPAD.EXE    C:\WINDOWS\NOTEPAD.EXE


    Description
    -----------
    This example shows how to use Get-Command to determine which command Windows PowerShell runs when it has access to
    multiple commands with the same name. When you use the Name parameter without wildcard characters, Get-Command list
    s the commands with that name in execution precedence order.

    This command shows which Notepad program Windows PowerShell runs when you type "Notepad" without a fully qualified
    path. The command uses the Name parameter without wildcard characters.

    The sample output shows the Notepad commands in the current console. It indicates that Windows PowerShell will run
    the instance of Notepad.exe in the C:\Windows\System32 directory.





    -------------------------- EXAMPLE 11 --------------------------

    C:\PS>(get-command get-date).pssnapin

    C:\PS> (get-command remove-gpo).module


    Description
    -----------
    These commands show how to find the snap-in or module from which a particular cmdlet originated.

    The first command uses the PSSnapin property of the CmdletInfo object to find the snap-in that added the Get-Date c
    mdlet.

    The second command uses the Module property of the CmdletInfo object to find the module that added the Remove-GPO c
    mdlet.






RELATED LINKS
    Online version: http://go.microsoft.com/fwlink/?LinkID=113309
    about_Command_Precedence
    Get-Help
    Get-PSDrive
    Get-Member
    Import-PSSession
    Export-PSSession



PS C:\Users\Windows-32>
```

- List all parameters of ```Get-Command```

```Powershell
PS C:\Users\Windows-32> Get-Help Get-Command -Parameter *

-ArgumentList <Object[]>
    Gets information about a cmdlet or function when it is used with the specified  parameters ("arguments"), such as a
     path.  The alias for ArgumentList is Args.

    To detect parameters that are added to a cmdlet when it is used with a particular provider, set the value of Argume
    ntList to a path in the provider drive, such as "HKML\Software" or "cert:\my".

    Required?                    false
    Position?                    2
    Default value
    Accept pipeline input?       false
    Accept wildcard characters?  false


-CommandType <CommandTypes>
    Gets only the specified types of commands. Use "CommandType" or its alias, "Type". By default, Get-Command gets cmd
    lets and functions.

    Valid values are:
    -- Alias: All Windows PowerShell aliases in the current session.

    -- All: All command types. It is the equivalent of "get-command *".

    -- Application: All non-Windows-PowerShell files in paths listed in the Path environment variable ($env:path), incl
    uding .txt, .exe, and .dll files.

    -- Cmdlet: The cmdlets in the current session. "Cmdlet" is the default.

    -- ExternalScript: All .ps1 files in the paths listed in the Path environment variable ($env:path).

    -- Filter and Function: All Windows PowerShell functions.

    -- Script: Script blocks in the current session.

    Required?                    false
    Position?                    named
    Default value
    Accept pipeline input?       true (ByPropertyName)
    Accept wildcard characters?  false


-Module <string[]>
    Gets the commands that came from the specified modules or snap-ins. Enter the names of modules or snap-ins, or ente
    r snap-in or module objects.

    You can refer to this parameter by its name, Module, or by its alias, PSSnapin. The parameter name that you choose
    has no effect on the command or its output.

    This parameter takes string values, but you can also supply a PSModuleInfo or PSSnapinInfo object, such as the obje
    cts that Get-Module, Get-PSSnapin, and Import-PSSession return.

    Required?                    false
    Position?                    named
    Default value                None
    Accept pipeline input?       true (ByPropertyName)
    Accept wildcard characters?  false


-Name <string[]>
    Gets information only about the cmdlets or command elements with the specified name. <String> represents all or par
    t of the name of the cmdlet or command element. Wildcards are permitted.

    To list commands with the same name in execution order, type the command name without wildcard characters. For more
     information, see the Notes section.

    Required?                    false
    Position?                    1
    Default value
    Accept pipeline input?       true (ByValue, ByPropertyName)
    Accept wildcard characters?  false


-Noun <string[]>
    Gets cmdlets and functions with names that include the specified noun. <String> represents one or more nouns or nou
    n patterns, such as "process" or "*item*". Wildcards are permitted.

    Required?                    false
    Position?                    named
    Default value
    Accept pipeline input?       true (ByPropertyName)
    Accept wildcard characters?  false


-Syntax [<SwitchParameter>]
    Gets only specified data about the command element.
               * For aliases, retrieves the standard name.
               * For cmdlets, retrieves the syntax.
               * For functions and filters, retrieves the function definition.
               * For scripts and applications (files), retrieves the path and filename.

    Required?                    false
    Position?                    named
    Default value
    Accept pipeline input?       true (ByPropertyName)
    Accept wildcard characters?  false


-TotalCount <int>
    Gets only the specified number of command elements. You can use this parameter to limit the output of a command.

    Required?                    false
    Position?                    named
    Default value
    Accept pipeline input?       true (ByPropertyName)
    Accept wildcard characters?  false


-Verb <string[]>
    Gets information about cmdlets and functions with names that include the specified verb. <String> represents one or
     more verbs or verb patterns, such as "remove" or *et". Wildcards are permitted.

    Required?                    false
    Position?                    named
    Default value
    Accept pipeline input?       true (ByPropertyName)
    Accept wildcard characters?  false




PS C:\Users\Windows-32>
```

- List all ```Cmdlet``` of ```Get-Command``` with name ```process```

```Powershell
PS C:\Users\Windows-32> Get-Command -CommandType cmdlet -Name *process*

CommandType     Name                                                Definition
-----------     ----                                                ----------
Cmdlet          Debug-Process                                       Debug-Process [-Name] <String[]> [-Verbose] [-De...
Cmdlet          Get-Process                                         Get-Process [[-Name] <String[]>] [-ComputerName ...
Cmdlet          Start-Process                                       Start-Process [-FilePath] <String> [[-ArgumentLi...
Cmdlet          Stop-Process                                        Stop-Process [-Id] <Int32[]> [-PassThru] [-Force...
Cmdlet          Wait-Process                                        Wait-Process [-Name] <String[]> [[-Timeout] <Int...


PS C:\Users\Windows-32>
```

- List all ```Cmdlet``` of ```Get-Command``` with name ```service```

```Powershell
PS C:\Users\Windows-32> Get-Command -CommandType cmdlet -Name *service*

CommandType     Name
-----------     ----
Cmdlet          Get-Service
Cmdlet          New-Service
Cmdlet          New-WebServiceProxy
Cmdlet          Restart-Service
Cmdlet          Resume-Service
Cmdlet          Set-Service
Cmdlet          Start-Service
Cmdlet          Stop-Service
Cmdlet          Suspend-Service


PS C:\Users\Windows-32>
```

- Count ```Cmdlet``` of ```Get-Command```

```Powershell
PS C:\Users\Windows-32> Get-Command -CommandType cmdlet | Measure-Object


Count    : 236
Average  :
Sum      :
Maximum  :
Minimum  :
Property :



PS C:\Users\Windows-32>
```

- ```Process Listing```

```Powershell
PS C:\Users\Windows-32> Get-Process

Handles  NPM(K)    PM(K)      WS(K) VM(M)   CPU(s)     Id ProcessName
-------  ------    -----      ----- -----   ------     -- -----------
     23       2     1752       1608    27     0.01   2864 cmd
     91       4   196908     201960   250     2.94   2444 conhost
     53       3      872       3536    43     0.04   2872 conhost
    379       5     1092       2192    30             352 csrss
    206       6     1104       3360    31             396 csrss
     69       3      972       2732    36     0.02    324 dwm
    716      23    22560      23892   181     1.64    740 explorer
      0       0        0         12     0               0 Idle
     60       3     2024       3180    51     0.01   2020 jusched
    723      12     2928       5880    29             488 lsass
    141       3     1020       2284    13             496 lsm
    101       6     7772       9384    79     1.30   2716 notepad++
    829      10    43692      39648   184     1.71   2432 powershell
    134       5     6364       9644    60     0.18   3008 python
     95       4     1392       3920    36            2608 SearchFilterHost
    630      15    17092      10908    88             292 SearchIndexer
    278       5     2080       5696    42            3440 SearchProtocolHost
    194       7     4248       4536    29             480 services
     29       1      212        564     4             264 smss
    288       9     4368       5372    55            1328 spoolsv
    347       7     2552       5104    31             600 svchost
    250       8     2072       4080    23             712 svchost
    543      13    13692      10848    74             764 svchost
    508      12    25240      28872    92             884 svchost
   1048      27    13140      19608    96             924 svchost
    441      16     5452       7284    46            1128 svchost
    379      13     7620       7488    51            1232 svchost
    305      24     8600       6560    43            1364 svchost
    349      15     5044       7136    63            1468 svchost
     98       7     1184       3092    22            1828 svchost
    349      13     8112       8236    59            2376 svchost
    353      23    45640      14440   207            3488 svchost
    539       0       48        868     2               4 System
    185       9     6728       5232    45     0.04    328 taskhost
    115       5     1400       3292    43             660 VBoxService
    143       5     1308       3920    58     0.03   1116 VBoxTray
     75       5      836       2676    29             384 wininit
    113       4     1508       3308    35             436 winlogon
    421      15     7788       7104   104            2092 wmpnetwk
     91       4     1152       4632    53     0.01   3860 wuauclt


PS C:\Users\Windows-32>
```

- ```Service Listing```

```Powershell
PS C:\Users\Windows-32> Get-Service

Status   Name               DisplayName
------   ----               -----------
Stopped  AeLookupSvc        Application Experience
Stopped  ALG                Application Layer Gateway Service
Stopped  AppIDSvc           Application Identity
Stopped  Appinfo            Application Information
Stopped  AppMgmt            Application Management
Running  AudioEndpointBu... Windows Audio Endpoint Builder
Running  Audiosrv           Windows Audio
Stopped  AxInstSV           ActiveX Installer (AxInstSV)
Stopped  BDESVC             BitLocker Drive Encryption Service
Running  BFE                Base Filtering Engine
Stopped  BITS               Background Intelligent Transfer Ser...
Running  Browser            Computer Browser
Stopped  bthserv            Bluetooth Support Service
Stopped  CertPropSvc        Certificate Propagation
Stopped  clr_optimizatio... Microsoft .NET Framework NGEN v2.0....
Stopped  COMSysApp          COM+ System Application
Running  CryptSvc           Cryptographic Services
Running  CscService         Offline Files
Running  DcomLaunch         DCOM Server Process Launcher
Stopped  defragsvc          Disk Defragmenter
Running  Dhcp               DHCP Client
Running  Dnscache           DNS Client
Stopped  dot3svc            Wired AutoConfig
Running  DPS                Diagnostic Policy Service
Stopped  EapHost            Extensible Authentication Protocol
Stopped  EFS                Encrypting File System (EFS)
Stopped  ehRecvr            Windows Media Center Receiver Service
Stopped  ehSched            Windows Media Center Scheduler Service
Running  eventlog           Windows Event Log
Running  EventSystem        COM+ Event System
Stopped  Fax                Fax
Running  fdPHost            Function Discovery Provider Host
Running  FDResPub           Function Discovery Resource Publica...
Stopped  FontCache          Windows Font Cache Service
Stopped  FontCache3.0.0.0   Windows Presentation Foundation Fon...
Running  gpsvc              Group Policy Client
Stopped  hidserv            Human Interface Device Access
Stopped  hkmsvc             Health Key and Certificate Management
Running  HomeGroupProvider  HomeGroup Provider
Stopped  idsvc              Windows CardSpace
Running  IKEEXT             IKE and AuthIP IPsec Keying Modules
Stopped  IPBusEnum          PnP-X IP Bus Enumerator
Running  iphlpsvc           IP Helper
Running  KeyIso             CNG Key Isolation
Stopped  KtmRm              KtmRm for Distributed Transaction C...
Running  LanmanServer       Server
Running  LanmanWorkstation  Workstation
Stopped  lltdsvc            Link-Layer Topology Discovery Mapper
Running  lmhosts            TCP/IP NetBIOS Helper
Stopped  Mcx2Svc            Media Center Extender Service
Stopped  MMCSS              Multimedia Class Scheduler
Stopped  MozillaMaintenance Mozilla Maintenance Service
Running  MpsSvc             Windows Firewall
Stopped  MSDTC              Distributed Transaction Coordinator
Stopped  MSiSCSI            Microsoft iSCSI Initiator Service
Stopped  msiserver          Windows Installer
Stopped  napagent           Network Access Protection Agent
Stopped  Netlogon           Netlogon
Running  Netman             Network Connections
Running  netprofm           Network List Service
Stopped  NetTcpPortSharing  Net.Tcp Port Sharing Service
Running  NlaSvc             Network Location Awareness
Running  nsi                Network Store Interface Service
Running  p2pimsvc           Peer Networking Identity Manager
Running  p2psvc             Peer Networking Grouping
Stopped  PcaSvc             Program Compatibility Assistant Ser...
Stopped  PeerDistSvc        BranchCache
Stopped  pla                Performance Logs & Alerts
Running  PlugPlay           Plug and Play
Stopped  PNRPAutoReg        PNRP Machine Name Publication Service
Running  PNRPsvc            Peer Name Resolution Protocol
Running  PolicyAgent        IPsec Policy Agent
Running  Power              Power
Running  ProfSvc            User Profile Service
Stopped  ProtectedStorage   Protected Storage
Stopped  QWAVE              Quality Windows Audio Video Experience
Stopped  RasAuto            Remote Access Auto Connection Manager
Stopped  RasMan             Remote Access Connection Manager
Stopped  RemoteAccess       Routing and Remote Access
Stopped  RemoteRegistry     Remote Registry
Running  RpcEptMapper       RPC Endpoint Mapper
Stopped  RpcLocator         Remote Procedure Call (RPC) Locator
Running  RpcSs              Remote Procedure Call (RPC)
Running  SamSs              Security Accounts Manager
Stopped  SCardSvr           Smart Card
Running  Schedule           Task Scheduler
Stopped  SCPolicySvc        Smart Card Removal Policy
Stopped  SDRSVC             Windows Backup
Stopped  seclogon           Secondary Logon
Running  SENS               System Event Notification Service
Stopped  SensrSvc           Adaptive Brightness
Stopped  SessionEnv         Remote Desktop Configuration
Stopped  SharedAccess       Internet Connection Sharing (ICS)
Running  ShellHWDetection   Shell Hardware Detection
Stopped  SNMPTRAP           SNMP Trap
Running  Spooler            Print Spooler
Stopped  sppsvc             Software Protection
Stopped  sppuinotify        SPP Notification Service
Running  SSDPSRV            SSDP Discovery
Stopped  SstpSvc            Secure Socket Tunneling Protocol Se...
Stopped  StiSvc             Windows Image Acquisition (WIA)
Stopped  swprv              Microsoft Software Shadow Copy Prov...
Running  SysMain            Superfetch
Stopped  TabletInputService Tablet PC Input Service
Stopped  TapiSrv            Telephony
Stopped  TBS                TPM Base Services
Stopped  TermService        Remote Desktop Services
Running  Themes             Themes
Stopped  THREADORDER        Thread Ordering Server
Running  TrkWks             Distributed Link Tracking Client
Stopped  TrustedInstaller   Windows Modules Installer
Stopped  UI0Detect          Interactive Services Detection
Stopped  UmRdpService       Remote Desktop Services UserMode Po...
Running  upnphost           UPnP Device Host
Running  UxSms              Desktop Window Manager Session Manager
Stopped  VaultSvc           Credential Manager
Running  VBoxService        VirtualBox Guest Additions Service
Stopped  vds                Virtual Disk
Stopped  VSS                Volume Shadow Copy
Stopped  W32Time            Windows Time
Stopped  wbengine           Block Level Backup Engine Service
Stopped  WbioSrvc           Windows Biometric Service
Stopped  wcncsvc            Windows Connect Now - Config Registrar
Stopped  WcsPlugInService   Windows Color System
Running  WdiServiceHost     Diagnostic Service Host
Stopped  WdiSystemHost      Diagnostic System Host
Stopped  WebClient          WebClient
Stopped  Wecsvc             Windows Event Collector
Stopped  wercplsupport      Problem Reports and Solutions Contr...
Stopped  WerSvc             Windows Error Reporting Service
Running  WinDefend          Windows Defender
Stopped  WinHttpAutoProx... WinHTTP Web Proxy Auto-Discovery Se...
Running  Winmgmt            Windows Management Instrumentation
Stopped  WinRM              Windows Remote Management (WS-Manag...
Stopped  Wlansvc            WLAN AutoConfig
Stopped  wmiApSrv           WMI Performance Adapter
Running  WMPNetworkSvc      Windows Media Player Network Sharin...
Stopped  WPCSvc             Parental Controls
Stopped  WPDBusEnum         Portable Device Enumerator Service
Running  wscsvc             Security Center
Running  WSearch            Windows Search
Running  wuauserv           Windows Update
Stopped  wudfsvc            Windows Driver Foundation - User-mo...
Stopped  WwanSvc            WWAN AutoConfig


PS C:\Users\Windows-32>
```

- List all ```Cmdlet``` of ```Get-Command``` with name ```start```

```Powershell
PS C:\Users\Windows-32> Get-Command -Verb start

CommandType     Name
-----------     ----
Cmdlet          Start-Job
Cmdlet          Start-Process
Cmdlet          Start-Service
Cmdlet          Start-Sleep
Cmdlet          Start-Transaction
Cmdlet          Start-Transcript


PS C:\Users\Windows-32>
```

- List all ```Cmdlet``` of ```Get-Command``` with name ```stop```

```Powershell
PS C:\Users\Windows-32> Get-Command -Verb stop

CommandType     Name
-----------     ----
Cmdlet          Stop-Computer
Cmdlet          Stop-Job
Cmdlet          Stop-Process
Cmdlet          Stop-Service
Cmdlet          Stop-Transcript


PS C:\Users\Windows-32>
```

- Examples of ```Start-Process```

```Powershell
PS C:\Users\Windows-32> Get-Help Start-Process -Examples

NAME
    Start-Process

SYNOPSIS
    Starts one or more processes on the local computer.

    -------------------------- EXAMPLE 1 --------------------------

    C:\PS>start-process sort.exe


    Description
    -----------
    This command starts a process that uses the Sort.exe file in the current directory. The command uses all of the default values, including the default window style, working directory, and credentials.




    -------------------------- EXAMPLE 2 --------------------------

    C:\PS>start-process myfile.txt -workingdirectory "C:\PS-Test" -verb Print


    Description
    -----------
    This command starts a process that prints the C:\PS-Test\MyFile.txt file.




    -------------------------- EXAMPLE 3 --------------------------

    C:\PS>start-process Sort.exe -RedirectStandardInput Testsort.txt -RedirectStandardOutput Sorted.txt -RedirectStandardError SortError.txt -UseNewEnvironment


    Description
    -----------
    This command starts a process that sorts items in the Testsort.txt file and returns the sorted items in the Sorted.txt files. Any errors are written to the SortError.txt file.

    The UseNewEnvironment parameter specifies that the process runs with its own environment variables.




    -------------------------- EXAMPLE 4 --------------------------

    C:\PS>start-process notepad -wait -windowstyle Maximized


    Description
    -----------
    This command starts the Notepad process. It maximizes the window and retains the window until the process completes.

PS C:\Users\Windows-32>
```

- ```Start-Process```

```Powershell
PS C:\Users\Windows-32> Start-Process notepad.exe
```

- ```Stop-Process```

```Powershell
PS C:\Users\Windows-32> Stop-Process -Name notepad
```

- ```Start-Process``` and ```Stop-Process```

```Powershell
PS C:\Users\Windows-32> Get-Process -Name notepad

Handles  NPM(K)    PM(K)      WS(K) VM(M)   CPU(s)     Id ProcessName
-------  ------    -----      ----- -----   ------     -- -----------
     56       3      912       4256    55     0.15   1592 notepad
     56       3      912       4136    55     0.04   2360 notepad
     56       3      916       4208    55     0.07   2960 notepad
     56       3      916       4208    55     0.07   3288 notepad


PS C:\Users\Windows-32>
```

```Powershell
PS C:\Users\Windows-32> Stop-Process -Id 1592
```

```Powershell
PS C:\Users\Windows-32> Get-Process -Name notepad

Handles  NPM(K)    PM(K)      WS(K) VM(M)   CPU(s)     Id ProcessName
-------  ------    -----      ----- -----   ------     -- -----------
     56       3      912       4136    55     0.04   2360 notepad
     56       3      916       4208    55     0.07   2960 notepad
     56       3      916       4208    55     0.07   3288 notepad


PS C:\Users\Windows-32>
```

- List all ```Hotfixes```

```Powershell
PS C:\Users\Windows-32> Get-HotFix
```

- ```Get-Help``` for ```command```

```Powershell
PS C:\Users\Windows-32> Get-Help *command*

Name                              Category  Synopsis
----                              --------  --------
Get-Command                       Cmdlet    Gets basic information about cmdlets and other elements of Windows PowerShell commands.
Invoke-Command                    Cmdlet    Runs commands on local and remote computers.
Measure-Command                   Cmdlet    Measures the time it takes to run script blocks and cmdlets.
Trace-Command                     Cmdlet    Configures and starts a trace of the specified expression or command.
about_command_precedence          HelpFile  Describes how Windows PowerShell determines which command to run.
about_Command_Syntax              HelpFile  Describes the notation used for Windows PowerShell syntax in Help.
about_Core_Commands               HelpFile  Lists the cmdlets that are designed for use with Windows PowerShell


PS C:\Users\Windows-32>
```

- ```Get-Help``` for ```about_Core_Commands```

```Powershell
PS C:\Users\Windows-32> Get-Help about_Core_Commands
TOPIC
    about_Core_Commands

SHORT DESCRIPTION
    Lists the cmdlets that are designed for use with Windows PowerShell
    providers.


LONG DESCRIPTION
    Windows PowerShell includes a set of cmdlets that are specifically
    designed to manage the items in the data stores that are exposed by Windows
    PowerShell providers. You can use these cmdlets in the same ways to manage
    all the different types of data that the providers make available to you.
    For more information about providers, type "get-help about_providers".


    For example, you can use the Get-ChildItem cmdlet to list the files in a
    file system directory, the keys under a registry key, or the items that are
    exposed by a provider that you write or download.


    The following is a list of the Windows PowerShell cmdlets that are designed
    for use with providers:


  ChildItem cmdlets
      Get-ChildItem


  Content cmdlets
      Add-Content
      Clear-Content
      Get-Content
      Set-Content


  Item cmdlets
      Clear-Item
      Copy-Item
      Get-Item
      Invoke-Item
      Move-Item
      New-Item
      Remove-Item
      Rename-Item
      Set-Item


  ItemProperty cmdlets
      Clear-ItemProperty
      Copy-ItemProperty
      Get-ItemProperty
      Move-ItemProperty
      New-ItemProperty
      Remove-ItemProperty
      Rename-ItemProperty
      Set-ItemProperty


  Location cmdlets
      Get-Location
      Pop-Location
      Push-Location
      Set-Location


  Path cmdlets
      Join-Path
      Convert-Path
      Split-Path
      Resolve-Path
      Test-Path


  PSDrive cmdlets
      Get-PSDrive
      New-PSDrive
      Remove-PSDrive


  PSProvider cmdlets
      Get-PSProvider


    For more information about a cmdlet, type "get-help <cmdlet-name>".

SEE ALSO
    about_Providers
PS C:\Users\Windows-32>
```

###### Exercise

Explore ```cmdlets``` using ```Get-Command``` and pick ten ```cmdlets``` which could be useful in ```penetration tests```.

- List of all ```cmdlet```

```Powershell
PS C:\Users\Windows-32> Get-Command -type cmdlet

CommandType     Name
-----------     ----
Cmdlet          Add-Computer
Cmdlet          Add-Content
Cmdlet          Add-History
Cmdlet          Add-Member
Cmdlet          Add-PSSnapin
Cmdlet          Add-Type
Cmdlet          Checkpoint-Computer
Cmdlet          Clear-Content
Cmdlet          Clear-EventLog
Cmdlet          Clear-History
Cmdlet          Clear-Item
Cmdlet          Clear-ItemProperty
Cmdlet          Clear-Variable
Cmdlet          Compare-Object
Cmdlet          Complete-Transaction
Cmdlet          Connect-WSMan
Cmdlet          ConvertFrom-Csv
Cmdlet          ConvertFrom-SecureString
Cmdlet          ConvertFrom-StringData
Cmdlet          Convert-Path
Cmdlet          ConvertTo-Csv
Cmdlet          ConvertTo-Html
Cmdlet          ConvertTo-SecureString
Cmdlet          ConvertTo-Xml
Cmdlet          Copy-Item
Cmdlet          Copy-ItemProperty
Cmdlet          Debug-Process
Cmdlet          Disable-ComputerRestore
Cmdlet          Disable-PSBreakpoint
Cmdlet          Disable-PSSessionConfiguration
Cmdlet          Disable-WSManCredSSP
Cmdlet          Disconnect-WSMan
Cmdlet          Enable-ComputerRestore
Cmdlet          Enable-PSBreakpoint
Cmdlet          Enable-PSRemoting
Cmdlet          Enable-PSSessionConfiguration
Cmdlet          Enable-WSManCredSSP
Cmdlet          Enter-PSSession
Cmdlet          Exit-PSSession
Cmdlet          Export-Alias
Cmdlet          Export-Clixml
Cmdlet          Export-Console
Cmdlet          Export-Counter
Cmdlet          Export-Csv
Cmdlet          Export-FormatData
Cmdlet          Export-ModuleMember
Cmdlet          Export-PSSession
Cmdlet          ForEach-Object
Cmdlet          Format-Custom
Cmdlet          Format-List
Cmdlet          Format-Table
Cmdlet          Format-Wide
Cmdlet          Get-Acl
Cmdlet          Get-Alias
Cmdlet          Get-AuthenticodeSignature
Cmdlet          Get-ChildItem
Cmdlet          Get-Command
Cmdlet          Get-ComputerRestorePoint
Cmdlet          Get-Content
Cmdlet          Get-Counter
Cmdlet          Get-Credential
Cmdlet          Get-Culture
Cmdlet          Get-Date
Cmdlet          Get-Event
Cmdlet          Get-EventLog
Cmdlet          Get-EventSubscriber
Cmdlet          Get-ExecutionPolicy
Cmdlet          Get-FormatData
Cmdlet          Get-Help
Cmdlet          Get-History
Cmdlet          Get-Host
Cmdlet          Get-HotFix
Cmdlet          Get-Item
Cmdlet          Get-ItemProperty
Cmdlet          Get-Job
Cmdlet          Get-Location
Cmdlet          Get-Member
Cmdlet          Get-Module
Cmdlet          Get-PfxCertificate
Cmdlet          Get-Process
Cmdlet          Get-PSBreakpoint
Cmdlet          Get-PSCallStack
Cmdlet          Get-PSDrive
Cmdlet          Get-PSProvider
Cmdlet          Get-PSSession
Cmdlet          Get-PSSessionConfiguration
Cmdlet          Get-PSSnapin
Cmdlet          Get-Random
Cmdlet          Get-Service
Cmdlet          Get-TraceSource
Cmdlet          Get-Transaction
Cmdlet          Get-UICulture
Cmdlet          Get-Unique
Cmdlet          Get-Variable
Cmdlet          Get-WinEvent
Cmdlet          Get-WmiObject
Cmdlet          Get-WSManCredSSP
Cmdlet          Get-WSManInstance
Cmdlet          Group-Object
Cmdlet          Import-Alias
Cmdlet          Import-Clixml
Cmdlet          Import-Counter
Cmdlet          Import-Csv
Cmdlet          Import-LocalizedData
Cmdlet          Import-Module
Cmdlet          Import-PSSession
Cmdlet          Invoke-Command
Cmdlet          Invoke-Expression
Cmdlet          Invoke-History
Cmdlet          Invoke-Item
Cmdlet          Invoke-WmiMethod
Cmdlet          Invoke-WSManAction
Cmdlet          Join-Path
Cmdlet          Limit-EventLog
Cmdlet          Measure-Command
Cmdlet          Measure-Object
Cmdlet          Move-Item
Cmdlet          Move-ItemProperty
Cmdlet          New-Alias
Cmdlet          New-Event
Cmdlet          New-EventLog
Cmdlet          New-Item
Cmdlet          New-ItemProperty
Cmdlet          New-Module
Cmdlet          New-ModuleManifest
Cmdlet          New-Object
Cmdlet          New-PSDrive
Cmdlet          New-PSSession
Cmdlet          New-PSSessionOption
Cmdlet          New-Service
Cmdlet          New-TimeSpan
Cmdlet          New-Variable
Cmdlet          New-WebServiceProxy
Cmdlet          New-WSManInstance
Cmdlet          New-WSManSessionOption
Cmdlet          Out-Default
Cmdlet          Out-File
Cmdlet          Out-GridView
Cmdlet          Out-Host
Cmdlet          Out-Null
Cmdlet          Out-Printer
Cmdlet          Out-String
Cmdlet          Pop-Location
Cmdlet          Push-Location
Cmdlet          Read-Host
Cmdlet          Receive-Job
Cmdlet          Register-EngineEvent
Cmdlet          Register-ObjectEvent
Cmdlet          Register-PSSessionConfiguration
Cmdlet          Register-WmiEvent
Cmdlet          Remove-Computer
Cmdlet          Remove-Event
Cmdlet          Remove-EventLog
Cmdlet          Remove-Item
Cmdlet          Remove-ItemProperty
Cmdlet          Remove-Job
Cmdlet          Remove-Module
Cmdlet          Remove-PSBreakpoint
Cmdlet          Remove-PSDrive
Cmdlet          Remove-PSSession
Cmdlet          Remove-PSSnapin
Cmdlet          Remove-Variable
Cmdlet          Remove-WmiObject
Cmdlet          Remove-WSManInstance
Cmdlet          Rename-Item
Cmdlet          Rename-ItemProperty
Cmdlet          Reset-ComputerMachinePassword
Cmdlet          Resolve-Path
Cmdlet          Restart-Computer
Cmdlet          Restart-Service
Cmdlet          Restore-Computer
Cmdlet          Resume-Service
Cmdlet          Select-Object
Cmdlet          Select-String
Cmdlet          Select-Xml
Cmdlet          Send-MailMessage
Cmdlet          Set-Acl
Cmdlet          Set-Alias
Cmdlet          Set-AuthenticodeSignature
Cmdlet          Set-Content
Cmdlet          Set-Date
Cmdlet          Set-ExecutionPolicy
Cmdlet          Set-Item
Cmdlet          Set-ItemProperty
Cmdlet          Set-Location
Cmdlet          Set-PSBreakpoint
Cmdlet          Set-PSDebug
Cmdlet          Set-PSSessionConfiguration
Cmdlet          Set-Service
Cmdlet          Set-StrictMode
Cmdlet          Set-TraceSource
Cmdlet          Set-Variable
Cmdlet          Set-WmiInstance
Cmdlet          Set-WSManInstance
Cmdlet          Set-WSManQuickConfig
Cmdlet          Show-EventLog
Cmdlet          Sort-Object
Cmdlet          Split-Path
Cmdlet          Start-Job
Cmdlet          Start-Process
Cmdlet          Start-Service
Cmdlet          Start-Sleep
Cmdlet          Start-Transaction
Cmdlet          Start-Transcript
Cmdlet          Stop-Computer
Cmdlet          Stop-Job
Cmdlet          Stop-Process
Cmdlet          Stop-Service
Cmdlet          Stop-Transcript
Cmdlet          Suspend-Service
Cmdlet          Tee-Object
Cmdlet          Test-ComputerSecureChannel
Cmdlet          Test-Connection
Cmdlet          Test-ModuleManifest
Cmdlet          Test-Path
Cmdlet          Test-WSMan
Cmdlet          Trace-Command
Cmdlet          Undo-Transaction
Cmdlet          Unregister-Event
Cmdlet          Unregister-PSSessionConfiguration
Cmdlet          Update-FormatData
Cmdlet          Update-List
Cmdlet          Update-TypeData
Cmdlet          Use-Transaction
Cmdlet          Wait-Event
Cmdlet          Wait-Job
Cmdlet          Wait-Process
Cmdlet          Where-Object
Cmdlet          Write-Debug
Cmdlet          Write-Error
Cmdlet          Write-EventLog
Cmdlet          Write-Host
Cmdlet          Write-Output
Cmdlet          Write-Progress
Cmdlet          Write-Verbose
Cmdlet          Write-Warning


PS C:\Users\Windows-32>
```

- List of all ```cmdlet``` useful in Penetration tests

    - Add-Computer
    - Clear-EventLog
    - Clear-History
    - Disable-ComputerRestore
    - Get-Acl
    - Remove-EventLog
    - Set-Date
    - Start-Process
    - Start-Service
    - Stop-Process
    - Stop-Service
    - Write-Output
