New-Item -Name 'bin' -ItemType 'Directory' -Force
New-Item -Name 'build' -ItemType 'Directory' -Force
Set-Location -Path 'build'

Start-Process -FilePath 'cmake' -ArgumentList '..', '-D CMAKE_C_COMPILER=gcc', '-G "MinGW Makefiles"' -NoNewWindow -Wait
Start-Process -FilePath 'cmake' -ArgumentList '--build', '.' -NoNewWindow -Wait

$Bin = Join-Path -Path '..' -ChildPath 'bin'
Move-Item -Path (Join-Path -Path 'bin' -ChildPath '*.exe') -Destination $Bin -Force