function Check-PassTheHash
{
    $hotfixes = "KB2871997"
    #checks the computer it's run on if any of the listed hotfixes are present
    $hotfix = Get-HotFix -ComputerName $env:computername | Where-Object {$hotfixes -contains $_.HotfixID} | Select-Object -property "HotFixID"  
    $Global:out = Get-HotFix | Where-Object {$hotfixes -contains $_.HotfixID}
}

function Result-PassTheHash
{  
    if ($out)
    {
        "Found HotFix: " + $out.HotFixID
    } 
    else 
    {
        "Didn't Find HotFix"
    }

}