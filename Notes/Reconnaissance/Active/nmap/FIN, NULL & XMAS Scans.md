# Overview
These scan types make use of a small loophole in the [TCP RFC](http://www.rfc-editor.org/rfc/rfc793.txt) to differentiate between `open` and `closed` ports. RFC 793 dictates that "if the destination port state is CLOSED .... an incoming segment not containing a RST causes a RST to be sent in response.” It also says the following about packets sent to open ports without the SYN, RST, or ACK bits set: “you are unlikely to get here, but if you do, drop the segment, and return".

Scanning systems compliant with this RFC text, any packet not containing `SYN`, `RST`, or `ACK` bits will beget an `RST` if the port is closed and no response at all if the port is open. So long as none of these flags are set, any combination of the other three (`FIN`, `PSH`, and `URG`) is fine.

These scan types can sneak through certain non-stateful firewalls and packet filtering routers and are a little more stealthy than even a SYN scan. However, not all systems are compliant with RFC 793 - some send a `RST` even if the port is open. Some operating systems that do this include Microsoft Windows, a lot of Cisco devices, IBM OS/400, and BSDI. These scans will work against most Unix-based systems.

It is not possible to distinguish an `open` from a `filtered` port with these scans, hence why the port states will be `open|filtered`.

# Null Scan
Doesn't set any flags. Since null scanning does not set any set flags, it can sometimes penetrate firewalls and edge routers that filter incoming packets with certain flags. It is invoked with the `-sN` option:

![](Resources/Images/null-scan.png)

# FIN Scan
Sets just the `FIN` bit to on. It is invoked with `-sF`:

![](Resources/Images/fin-scan.png)

# Xmas Scan
Sets the FIN, PSH, and URG flags, lighting the packet up like a Christmas tree. It is performed through the `-sX` option:

![](Resources/Images/xmas-scan.png)