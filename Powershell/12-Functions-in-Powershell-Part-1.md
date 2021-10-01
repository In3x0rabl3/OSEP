#### 12. Functions in Powershell Part 1

###### Functions
- Simple usage

```PowerShell
PS C:\Users\Windows-32\Desktop> function add { 1 + 3 }
PS C:\Users\Windows-32\Desktop> add
4
PS C:\Users\Windows-32\Desktop>
```
- Parameters of a PowerShell function.    - $args
    
	```PowerShell
	PS C:\Users\Windows-32\Desktop> function paramshow { $args }
	PS C:\Users\Windows-32\Desktop> paramshow
	PS C:\Users\Windows-32\Desktop> paramshow "Hi"
	Hi
	PS C:\Users\Windows-32\Desktop> paramshow 666
	666
	PS C:\Users\Windows-32\Desktop>
	```
	
	```PowerShell
	PS C:\Users\Windows-32\Desktop> function paramadd { $args[0] + $args[1] }
	PS C:\Users\Windows-32\Desktop> paramadd 3 7
	10
	PS C:\Users\Windows-32\Desktop>
	```

    - Declaring parameters

	```PowerShell
	PS C:\Users\Windows-32\Desktop> function newFunction ( $num1, $num2 ) { $num1 * $num2 }
	PS C:\Users\Windows-32\Desktop> newFunction 2 6
	12
	PS C:\Users\Windows-32\Desktop>
	```

    - Positional and named parameters
	
	```PowerShell
	PS C:\Users\Windows-32\Desktop> function posfunc ($param1, $param2) { $param1 }
	PS C:\Users\Windows-32\Desktop> posfunc -param1 2 -param2 4
	2
	PS C:\Users\Windows-32\Desktop> posfunc 2 4
	2
	PS C:\Users\Windows-32\Desktop> posfunc -param2 2 -param1 4
	4
	PS C:\Users\Windows-32\Desktop>
	```