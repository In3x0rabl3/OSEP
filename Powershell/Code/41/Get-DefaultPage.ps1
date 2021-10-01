$reader = [System.IO.File]::OpenText("C:\Users\Administrator\Desktop\Code\41\ip.txt")

while($null -ne ($line = $reader.ReadLine())) {
    $filename = [System.IO.Path]::GetFileName($line)
    Invoke-WebRequest $line -OutFile $filename
}