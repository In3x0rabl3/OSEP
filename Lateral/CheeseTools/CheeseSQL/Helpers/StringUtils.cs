using System;
using System.Linq;

namespace CheeseSQL.Helpers
{
    public class StringUtils
    {
        private static Random random = new Random();
        public static string RandomString(int length)
        {
            string rs = "0";
            const string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
            while (char.IsDigit(rs[0]))
            {
                rs = new string(Enumerable.Repeat(chars, length)
                  .Select(s => s[random.Next(s.Length)]).ToArray());
            }
            return rs;
        }

        public static string ConvertByteToHex(byte[] byteData)
        {
            return BitConverter.ToString(byteData).Replace("-", "");
        }

    }
}
