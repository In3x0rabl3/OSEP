using System;
using System.Security.Cryptography;
using System.Linq;
using System.Text;
using System.IO;

namespace ShellcodeInjectionTechniques
{
    class AesHelper
    {

        public static byte[] Decrypt(string key, string aes_base64)
        {
            byte[] tempKey = Encoding.ASCII.GetBytes(key);
            tempKey = SHA256.Create().ComputeHash(tempKey);

            byte[] data = Convert.FromBase64String(aes_base64);

            // decrypt data
            Aes aes = new AesManaged();
            aes.Mode = CipherMode.CBC;
            aes.Padding = PaddingMode.PKCS7;
            ICryptoTransform dec = aes.CreateDecryptor(tempKey, SubArray(tempKey, 16));

            using (MemoryStream msDecrypt = new MemoryStream())
            {
                using (CryptoStream csDecrypt = new CryptoStream(msDecrypt, dec, CryptoStreamMode.Write))
                {

                    csDecrypt.Write(data, 0, data.Length);
                    return msDecrypt.ToArray();
                }
            }
        }

        public static byte[] SubArray(byte[] a, int length)
        {
            byte[] b = new byte[length];
            for (int i = 0; i < length; i++)
            {
                b[i] = a[i];
            }
            return b;
        }

        public static byte[] SubArray(byte[] a, int startIndex, int length)
        {
            int lengthOfArrayToCopy = length;
            if (length + startIndex > a.Length)
                lengthOfArrayToCopy = a.Length - startIndex;

            byte[] b = new byte[lengthOfArrayToCopy];
            for (int i = 0; i < lengthOfArrayToCopy; i++)
            {
                b[i] = a[startIndex + i];
            }
            return b;
        }
    }
}