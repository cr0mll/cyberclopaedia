# Using whois for gathering domain name and IP address information
`whois` is a tool for finding domain name and IP address information which can be used as part of your OSINT gathering because it uses public data sources. You can use it as follows:
```bash
whois <hostname>
```
```bash
┌──(backslash0@kali)-[~]-[]
└─$ whois tesla.com                                                                                                                                                                                                                      1 ⨯
   Domain Name: TESLA.COM
   Registry Domain ID: 187902_DOMAIN_COM-VRSN
   Registrar WHOIS Server: whois.markmonitor.com
   Registrar URL: http://www.markmonitor.com
   Updated Date: 2020-10-02T09:07:57Z
   Creation Date: 1992-11-04T05:00:00Z
   Registry Expiry Date: 2022-11-03T05:00:00Z
   Registrar: MarkMonitor Inc.
   Registrar IANA ID: 292
   Registrar Abuse Contact Email: abusecomplaints@markmonitor.com
   Registrar Abuse Contact Phone: +1.2083895740
   Domain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited
   Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
   Domain Status: clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited
   Domain Status: serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited
   Domain Status: serverTransferProhibited https://icann.org/epp#serverTransferProhibited
   Domain Status: serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited
   Name Server: A1-12.AKAM.NET
   Name Server: A10-67.AKAM.NET
   Name Server: A12-64.AKAM.NET
   Name Server: A28-65.AKAM.NET
   Name Server: A7-66.AKAM.NET
   Name Server: A9-67.AKAM.NET
   Name Server: EDNS69.ULTRADNS.BIZ
   Name Server: EDNS69.ULTRADNS.COM
   Name Server: EDNS69.ULTRADNS.NET
   Name Server: EDNS69.ULTRADNS.ORG
   DNSSEC: unsigned
   URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/
>>> Last update of whois database: 2021-09-14T09:01:10Z <<<
```

# Using host for quick lookups
`host` is DNS querying tool which can be used for quick lookups. It will often return more than a single IP address:
```bash
host <hostname or IP>
```
```bash
┌──(backslash0@kali)-[~]-[]
└─$ host google.com                
google.com has address 172.217.169.174
google.com has IPv6 address 2a00:1450:4017:80a::200e
google.com mail is handled by 10 aspmx.l.google.com.
google.com mail is handled by 20 alt1.aspmx.l.google.com.
google.com mail is handled by 40 alt3.aspmx.l.google.com.
google.com mail is handled by 30 alt2.aspmx.l.google.com.
google.com mail is handled by 50 alt4.aspmx.l.google.com.
```

You can also do reverse name lookups by supplying an IP address:
```bash
┌──(backslash0@kali)-[~]-[]
└─$ host 8.8.8.8        
8.8.8.8.in-addr.arpa domain name pointer dns.google.
```

A special domain `in-addr.arpa` is used for reverse DNS lookups. You can read more about it [here](../../Networking/DNS/The%20in-addr.arpa%20Domain.md).