$file = Get-ChildItem -Path C:\ -Filter *.txt -Recurse

Write-Output "`nFiles Found " --------------------- $file.Count

Write-Output "`nScript Output " ---------------------

Select-String $file -Pattern username, password, credential