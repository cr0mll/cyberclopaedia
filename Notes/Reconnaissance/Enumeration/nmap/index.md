# Introduction
Nmap is a free and open source port and network scanner, which may also be used for vulnerability scanning through its scripting engine - the NSE. 

# Syntax
The syntax for nmap is as follows:

```bash
nmap <options> target_range
```

It is always good practice to run Nmap with root privileges as they are required for some of the tool's functionality.

You can do a simple scan on a single IP through the following command:

```bash
nmap <IP>
```

![](Resources/Images/simple-nmap-scan.png)

By default, Nmap scans the top 1000 most commonly used ports (these are not necssarily the ports 0-999). You can specify specific ports for scanning with the `-p` flag followed by a comma-separated list of ports. Specifying `-p-` will cause nmap to scan all ports (0-65535).

![](Resources/Images/simple-nmap-scan-specific-ports.png)

# Port States
- **open** - an application is actively listening for TCP connections, UDP datagrams or SCTP associations on this port
- **closed** -  the port is accessible (it receives and responds to Nmap probe packets), but there is no application listening on it
- **filtered** - Nmap cannot determine whether the port is open because packet filtering prevents its probes from reaching the port. Usually, the filter sends no response, so Nmap needs to resend the probe a few times in order to be sure that it wasn't dropped due to traffic congestion. This slows the scan drastically
- **unfiltered** - the port is accessible, but Nmap is unable to determine whether it is open or closed. Only the ACK scan, used for mapping firewall rulesets, may put ports in this state
- **open|filtered** - Nmap is unable to determine whether the port is open or filtered. This occurs for scan types in which open ports give no response
- **closed|filtered** - Nmap is unable to determine whether the port is closed or filtered. It is only used for the IP ID idle scan.