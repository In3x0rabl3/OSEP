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