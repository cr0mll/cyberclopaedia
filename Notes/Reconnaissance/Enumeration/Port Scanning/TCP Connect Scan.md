# TCP Connect Scan
This is the default scan for nmap when it does *not* have elevated privileges. It initiates a full TCP connection and as a result can be slower. Additionally, it is also logged at the application level. 

![](../Port%20Scanning/Resources/Images/tcp-connect-scan.png)

![](../Port%20Scanning/Resources/Images/tcp-connect-scan-wireshark.png)

This type of scan can also be specified via the `-sT` option.