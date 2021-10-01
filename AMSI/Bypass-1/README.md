# AMSI-Bypass
Rasta's mouse AMSI patch but with function that makes it undetectable.

## How to run
Download AMSI_Bypass.zip or build project and run following command in powershell on targets computer.

```console
[System.Reflection.Assembly]::LoadFile("full_path_to_dll")
[Bypass]::amsi()
```
```
[Bypass] - Class
amsi() - Method in Bypass class
```
