$url = "http://www.google.com"

$ie_o = New-Object -ComObject InternetExplorer.Application.1

$ie_o.visible = $False;

$ie_o.navigate($url);