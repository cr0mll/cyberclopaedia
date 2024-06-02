# TCP Connect Scan

This is the default scan for nmap when it does _not_ have elevated privileges. It initiates a full TCP connection and as a result can be slower. Additionally, it is also logged at the application level.

![](<../../../Reconnaissance/Enumeration/Port Scanning/Resources/Images/tcp-connect-scan.png>)

![](<../../../Reconnaissance/Enumeration/Port Scanning/Resources/Images/tcp-connect-scan-wireshark.png>)

This type of scan can also be specified via the `-sT` option.
