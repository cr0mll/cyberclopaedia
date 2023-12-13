# Introduction
All services which need to somehow interface with the network a host is connected to run on ports and port scanning allows us to enumerate them in order to gather information such as what service is running, which version of the service is running, OS information, etc.

```admonish warning
Port scanning is very heavy on network bandwidth and generates a lot of traffic which can cause the target to slow down or crash altogether. During a penetration test, you should *always* inform the client when you are about to perform a port scan.
```

```admonish danger
Port scanning without prior written permission from the target may be considered illegal in some jurisdictions.
```

The de-facto standard port scanner is [nmap](https://nmap.org/), although alternatives such as [masscan](https://github.com/robertdavidgraham/masscan) and [RustScan](https://github.com/RustScan/RustScan) do exist.

```admonish info
A lot of nmap's techniques require elevated privileges, so it is advisable to always run the tool with `sudo`.
```

### TCP vs UDP
There are two types of ports depending on the transport-layer protocol that they support. Both TCP and UDP ports range from 0 to 65535 but they are completely separate. For example, [DNS](../../../Networking/Protocols/Domain%20Name%20System%20(DNS)/index.md) uses UDP port 53 for queries but it uses TCP port 53 for zone transfers.

To scan UDP ports, nmap requires elevated privileges and the `-sU` flag.

```bash
nmap -sU <target>
```

```admonish note
Due to the nature of the protocol, UDP scanning takes a lot longer than TCP does.
```

# Port States
When scanning, nmap will determine that a port is in one of the following states:

- **open** - an application is actively listening for TCP connections, UDP datagrams or SCTP associations on this port
- **closed** -  the port is accessible (it receives and responds to Nmap probe packets), but there is no application listening on it
- **filtered** - Nmap cannot determine whether the port is open because packet filtering prevents its probes from reaching the port. Usually, the filter sends no response, so Nmap needs to resend the probe a few times in order to be sure that it wasn't dropped due to traffic congestion. This slows the scan drastically
- **unfiltered** - the port is accessible, but Nmap is unable to determine whether it is open or closed. Only the ACK scan, used for mapping firewall rulesets, may put ports in this state
- **open|filtered** - Nmap is unable to determine whether the port is open or filtered. This occurs for scan types in which open ports give no response
- **closed|filtered** - Nmap is unable to determine whether the port is closed or filtered. It is only used for the IP ID idle scan.

By default, nmap scans only the 1000 most common TCP ports. One can scan specific ports by listing them separated by commas *directly* after the `-p` flag.

```bash
nmap -pport1,port2,... <target>
```

If no ports are specified after the `-p` flag, nmap will scan *all* ports (either UDP or TCP depending on the type of scan).

```bash
nmap -p <target>
```