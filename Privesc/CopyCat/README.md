# CopyCat
Simple rapper for Mimikatz, bypass Defender


Start a cmd shell (with admin priv.) like this and run CopyCat.exe and enjoy Mimikatz (If you are running 64 bit Windows 10)

cmd coffee

if one like to try "sekurlsa::logonpasswords" don't type it in mimikatz # - hit enter one time !


Compile: csc.exe /platform:x64 /target:exe CopyCat.cs

After compiling paste Mimikatz shellcode with hex editor into string starting with "A
