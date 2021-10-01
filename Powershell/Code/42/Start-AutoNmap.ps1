$outputpath = "C:\Users\Administrator\Desktop"
$IPRanges = "10.0.0.1/24"
foreach ($range in $IPRanges)
{
    $temp = $range -split "/"
    $file = $temp[0]
    & "nmap.exe" "-nvv" "-Pn" "--top-ports" "20" "$range" "-oX" "$Outputpath\$file.xml"
}