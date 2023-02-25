# Introduction
The [File Transfer Protocol (FTP)](../../Networking/Protocols/File%20Transfer%20Protocol%20(FTP).md) is a common protocol which you may find during a penetration test. It is a TCP-based protocol and runs on port 21. Luckily, its enumeration is simple and rather straight-forward.

You can use the `ftp` command if you have credentials:
```bash
ftp <ip>
```

![](Resources/Images/FTP%20Login.png)

You can then proceed with typical navigation commands like `dir`, `cd`, `pwd`, `get` and `send` to navigate and interact with the remote file system.

If you don't have credentials you can try with the usernames `guest`, `anonymous`, or `ftp` and an empty password in order to test for anonymous login.

![](Resources/Images/FTP%20Anonymous%20Login.png)