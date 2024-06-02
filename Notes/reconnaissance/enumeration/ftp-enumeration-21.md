# FTP Enumeration (21)

The [File Transfer Protocol (FTP)](../../networking/protocols/file-transfer-protocol-ftp.md) is a common protocol which you may find during a penetration test. It is a TCP-based protocol and runs on port 21. Luckily, its enumeration is simple and rather straight-forward.

You can use the `ftp` command if you have credentials:

```bash
ftp <ip>
```

![](<../../Reconnaissance/Enumeration/Resources/Images/FTP Login.png>)

You can then proceed with typical navigation commands like `dir`, `cd`, `pwd`, `get` and `send` to navigate and interact with the remote file system.

If you don't have credentials you can try with the usernames `guest`, `anonymous`, or `ftp` and an empty password in order to test for anonymous login.

![](<../../Reconnaissance/Enumeration/Resources/Images/FTP Anonymous Login.png>)
