HollowProcess
=============
_Please note that this project is a **proof-of-concept**._

Process hollowing (also known as RunPE) is a technique where the memory of a target process is replaced with another (malicious) executable. It is often used by malware to evade detection. 

This project implements this technique in Python 3.

### Dependencies
* [pefile](https://github.com/erocarrera/pefile)

### Testing
I used a (64-bit) [Windows 10 vm](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/) for testing.

#### Payload
For the payload I used the following simple program:
```C++
#include <windows.h>

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
	MessageBox(NULL, L"World!", L"Hello", MB_OK);
	return 0;
}
```

`32.exe` and `64.exe` are the 32-bit and 64-bit compiled versions of this program, respectively.

#### Target
For the target executable I used the Windows Calculator. Specifically: 
* 32-bit: `C:\WINDOWS\SysWOW64\calc.exe`
* 64-bit: `C:\WINDOWS\System32\calc.exe`

I also tested some cases with other Windows executables (such as`notepad.exe`, `svchost.exe`, `explorer.exe`).

#### Results
Using Python 3.9.5 32-bit I was able to get the following working:
* A 32-bit payload with a 32-bit target.
* A 32-bit payload with a 64-bit target.

Using Python 3.9.5 64-bit I was able to get the following working:
* A 64-bit payload with a 64-bit target.

### Resources
These are some useful sources that helped me better understand this tecnique:
* [Dynamic forking (Process hollowing)](http://www.rohitab.com/discuss/topic/40262-dynamic-forking-process-hollowing/)
* [Process Hollowing](https://github.com/m0n0ph1/Process-Hollowing)
* [runpe](https://github.com/oueldz4/runpe)
* [ProcessHollowing32-64](https://github.com/idan1288/ProcessHollowing32-64)
* Practical Malware Analysis: The Hands-on Guide to Dissecting Malicious Software by Andrew Honig and Michael Sikorski
