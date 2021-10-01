function Show-AdvancedScript
{
    [CmdletBinding( SupportsShouldProcess = $True)]
    param(
    [Parameter()]
    $FilePath
    )

    Write-Verbose "Deleting $FilePath"
    if ($PSCmdlet.ShouldProcess("$FilePath", "Deleting file permanently"))
    {
    Remove-Item $FilePath
    }


}