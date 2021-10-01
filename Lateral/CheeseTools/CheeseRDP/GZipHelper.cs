using System;
using System.IO;
using System.IO.Compression;

namespace CheeseRDP
{
    class GZipHelper
    {
        public static void CopyTo(Stream src, Stream dest)
        {
            byte[] bytes = new byte[4096];

            int cnt;

            while ((cnt = src.Read(bytes, 0, bytes.Length)) != 0)
            {
                dest.Write(bytes, 0, cnt);
            }
        }

        public static byte[] Zip(byte[] bytes)
        {

            using (var msi = new MemoryStream(bytes))
            using (var mso = new MemoryStream())
            {
                using (var gs = new GZipStream(mso, CompressionMode.Compress))
                {
                    CopyTo(msi, gs);
                }

                return mso.ToArray();
            }
        }

        public static byte[] NZip(byte[] bytes, int times)
        {
            byte[] temp = bytes;
            for (int i = 0; i < times; i++)
            {
                temp = Zip(temp);
            }
            return temp;
        }
        public static byte[] NUnzip(byte[] bytes, int times)
        {
            byte[] temp = bytes;
            for (int i = 0; i < times; i++)
            {
                temp = Unzip(temp);
            }
            return temp;
        }

        public static byte[] Unzip(byte[] bytes)
        {
            using (var msi = new MemoryStream(bytes))
            using (var mso = new MemoryStream())
            {
                using (var gs = new GZipStream(msi, CompressionMode.Decompress))
                {
                    CopyTo(gs, mso);
                }

                return mso.ToArray();
            }
        }

        public static void test(string base64in, int iterations)
        {
            byte[] bytes = Convert.FromBase64String(base64in);
            byte[] zipped = GZipHelper.NZip(bytes, iterations);
            string base64out = Convert.ToBase64String(zipped);

            Console.WriteLine(base64out);
            int previous_length;
            previous_length = base64in.Length;

            for (int i = 1; i <= iterations; i++)
            {

                int current_length = Convert.ToBase64String(GZipHelper.NUnzip(zipped, i)).Length;

                if (current_length < previous_length)
                {
                    Console.WriteLine($"Working for {i} iterations with {previous_length - current_length} difference");
                }
                previous_length = current_length;
            }
            if (base64in == Convert.ToBase64String(GZipHelper.NUnzip(zipped, iterations)))
            {
                Console.WriteLine("It works!");
                Console.ReadKey();
            }
        }

    }
}
