
function Invoke-SharpEncrypt
{
<#
    .DESCRIPTION
        AES Encrypt and GZip CSharp Files.
        Credits to Cn33liz for https://github.com/Cn33liz/p0wnedLoader
        Author: @S3cur3Th1sSh1t
    #>

Param
    (
        [Parameter(Mandatory=$true)]
        [string]
        $file,
        [Parameter(Mandatory=$true)]
	    [string]
        $password,
        [Parameter(Mandatory=$true)]
	    [string]
        $outfile
	)


$sharpencrypt = @"
using System;
using System.Text;
using System.IO;
using System.IO.Compression;
using System.Security.Cryptography;


public class SharpEncrypt
{
    public static void PrintBanner()
    {
        Console.WriteLine(@"   ______                ____                       __ ");
        Console.WriteLine(@"  / __/ /  ___ _______  / __/__  __________ _____  / /_");
        Console.WriteLine(@" _\ \/ _ \/ _ `/__/ _ \/ _// _ \/ __/ __/ // / _ \/ __/");
        Console.WriteLine(@"/___/_//_/\_,_/_// .__/___/_//_/\__/_/  \_, / .__/\__/ ");
        Console.WriteLine(@"                /_/                    /___/_/         ");
        Console.WriteLine(@"                                                       ");
        Console.WriteLine(@"                       Compress and AES encrypt files  ");
        Console.WriteLine();
    }

    public static byte[] AES_Encrypt(byte[] bytesToBeEncrypted, byte[] passwordBytes)
    {
        byte[] encryptedBytes = null;

        // Set your salt here, change it to meet your flavor:
        // The salt bytes must be at least 8 bytes.
        byte[] saltBytes = new byte[] { 1, 2, 3, 4, 5, 6, 7, 8 };

        using (MemoryStream ms = new MemoryStream())
        {
            using (RijndaelManaged AES = new RijndaelManaged())
            {
                AES.KeySize = 256;
                AES.BlockSize = 128;

                var key = new Rfc2898DeriveBytes(passwordBytes, saltBytes, 1000);
                AES.Key = key.GetBytes(AES.KeySize / 8);
                AES.IV = key.GetBytes(AES.BlockSize / 8);

                AES.Mode = CipherMode.CBC;

                using (var cs = new CryptoStream(ms, AES.CreateEncryptor(), CryptoStreamMode.Write))
                {
                    cs.Write(bytesToBeEncrypted, 0, bytesToBeEncrypted.Length);
                    cs.Close();
                }
                encryptedBytes = ms.ToArray();
            }
        }

        return encryptedBytes;
    }

    public static byte[] GetRandomBytes()
    {
        int _saltSize = 4;
        byte[] ba = new byte[_saltSize];
        RNGCryptoServiceProvider.Create().GetBytes(ba);
        return ba;
    }

    public static byte[] CompressBin(byte[] data)
    {
        using (var compressedStream = new MemoryStream())
        using (var zipStream = new GZipStream(compressedStream, CompressionMode.Compress))
        {
            zipStream.Write(data, 0, data.Length);
            zipStream.Close();
            return compressedStream.ToArray();
        }
    }

    public static string Base64_Encode(byte[] data)
    {
        if (data == null)
            throw new ArgumentNullException("data");
        return Convert.ToBase64String(data);
    }

    public static void Main(params string[] args)
    {
        PrintBanner();
        
        if (File.Exists(args[0]))
        {
            string FileName = args[0];
            string Password = args[1];
            string OutFile = args[2];

            Console.Write("[*] First Read All Bytes.".PadRight(58));
            byte[] FileBytes = File.ReadAllBytes(FileName);
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("-> Done");
            Console.ResetColor();

            Console.Write("[*] AES Encrypt our Bytes.".PadRight(58));
            byte[] PasswordBytes = Encoding.UTF8.GetBytes(Password);
            PasswordBytes = SHA256.Create().ComputeHash(PasswordBytes);

            // Generating salt bytes
            byte[] saltBytes = GetRandomBytes();

            // Appending salt bytes to original bytes
            byte[] bytesToBeEncrypted = new byte[saltBytes.Length + FileBytes.Length];
            for (int i = 0; i < saltBytes.Length; i++)
            {
                bytesToBeEncrypted[i] = saltBytes[i];
            }
            for (int i = 0; i < FileBytes.Length; i++)
            {
                bytesToBeEncrypted[i + saltBytes.Length] = FileBytes[i];
            }

            byte[] bytesEncrypted = AES_Encrypt(bytesToBeEncrypted, PasswordBytes);
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("-> Done");
            Console.ResetColor();

            Console.Write("[*] Now let's Compress our Bytes.".PadRight(58));
            byte[] compress = CompressBin(bytesEncrypted);
            string encoded = Base64_Encode(compress);
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("-> Done");
            Console.ResetColor();

            Console.Write("[*] And finally encode our Bytes as a Base64 string.".PadRight(58));
            File.WriteAllText(OutFile, encoded);
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("-> Done");
            Console.ResetColor();

            Console.WriteLine("\n[!] Base64 string saved as " + OutFile);
        }
        else
        {
            Console.WriteLine("[!] File " + args[0] + " does not exist...");
            
        }

    }
}

"@

Add-Type -TypeDefinition $sharpencrypt


[sharpencrypt]::main("$file","$password","$outfile")
}
