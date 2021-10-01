#### 13. Functions in Powershell Part 2

- Dynamic number of Parameters

```PowerShell
PS C:\Users\Windows-32> function fixed_params ($a, $b) {
>> $a
>> $b
>> }
>>
PS C:\Users\Windows-32> fixed_params 2 4
2
4
PS C:\Users\Windows-32> fixed_params 2 4 7
2
4
PS C:\Users\Windows-32>
```

```PowerShell
PS C:\Users\Windows-32> function var_params ($a, $b) {
>> $a
>> $b
>> $args
>> }
>>
PS C:\Users\Windows-32> var_params 1 2 4 5 7
1
2
4
5
7
PS C:\Users\Windows-32>
```

- Type declaration of the Parameters

```PowerShell
PS C:\Users\Windows-32> function addInt ([int]$a, [int]$b) { $a + $b }
PS C:\Users\Windows-32> addInt 3 6
9
PS C:\Users\Windows-32>
```

- Default Values

```PowerShell
PS C:\Users\Windows-32> function default_value ($a=8, $b) {
>> $a
>> $b
>> }
>>
PS C:\Users\Windows-32> default_value
8
PS C:\Users\Windows-32> default_value 7 5
7
5
PS C:\Users\Windows-32>
```