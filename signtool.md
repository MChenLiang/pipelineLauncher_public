# 数字签名

## 需要的工具

* win10sdk[下载链接]<https://developer.microsoft.com/pt-br/windows/downloads/sdk-archive>
  

## 生产数字签名
```shell
makecert.exe -sv mykey.pvk -n "CN=名称" mycert.cer
cert2spc.exe mycert.cer mycert.spc
pvk2pfx -pvk mykey.pvk -pi "输入密码" -spc mycert.spc -pfx mycert.pfx -po "输入密码"
```

## 对exe进行签名
```shell
signTool sign /f mycert.pfx /p "输入密码" /v exe文件
```
