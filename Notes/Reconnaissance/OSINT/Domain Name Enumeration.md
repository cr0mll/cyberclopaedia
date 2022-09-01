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

A special domain `in-addr.arpa` is used for reverse DNS lookups. You can read more about it [here](../../Networking/Protocols/Domain%20Name%20System%20(DNS)/The%20in-addr.arpa%20Domain.md).

# Querying name servers with dig
`dig` is a tool for performing DNS queries. It can be used to request specific resource records such as the SOA.
```bash
dig <domain> SOA
```
```bash
┌──(backslash0@kali)-[~]-[]
└─$ dig google.com SOA

; <<>> DiG 9.16.15-Debian <<>> google.com SOA
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 41904
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; MBZ: 0x0005, udp: 512
;; QUESTION SECTION:
;google.com.                    IN      SOA

;; ANSWER SECTION:
google.com.             5       IN      SOA     ns1.google.com. dns-admin.google.com. 396314134 900 900 1800 60

;; Query time: 8 msec
;; SERVER: 192.168.129.2#53(192.168.129.2)
;; WHEN: Tue Sep 14 15:43:28 EEST 2021
;; MSG SIZE  rcvd: 89
```

We can see that the SOA is listed as `ns1.google.com` in the `ANSWER SECTION`. You can find the IP of this name server with dig, too.
```bash
┌──(backslash0@kali)-[~]-[]
└─$ dig ns1.google.com

; <<>> DiG 9.16.15-Debian <<>> ns1.google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 41311
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; MBZ: 0x0005, udp: 512
;; QUESTION SECTION:
;ns1.google.com.                        IN      A

;; ANSWER SECTION:
ns1.google.com.         5       IN      A       216.239.32.10

;; Query time: 43 msec
;; SERVER: 192.168.129.2#53(192.168.129.2)
;; WHEN: Tue Sep 14 15:47:51 EEST 2021
;; MSG SIZE  rcvd: 59
```

Note that usually the SOA for domains of smaller organizations, isn't actually a part of that domain, but is instead a server provided by a hosting company.

Notice how in the answer section for `google.com` there was a `dns-admin.google.com` domain? That's actually not a domain, it's an email address and should be read as `dns-admin@google.com`. Yep, DNS stores emails in zone files, too. But how do you figure out which one is a hostname and which is an email address? The email address comes last.

`dig` can also be used to query specific name servers with the following syntax:
```bash
dig @<name server> <domain>
```
```bash
┌──(backslash0@kali)-[~]-[]
└─$ dig @192.168.129.138 nsa.gov     

; <<>> DiG 9.16.15-Debian <<>> @192.168.129.138 nsa.gov
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 48156
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;nsa.gov.                       IN      A

;; AUTHORITY SECTION:
nsa.gov.                600     IN      SOA     ns1.nsa.gov. root.nsa.gov. 2007010401 3600 600 86400 600

;; Query time: 0 msec
;; SERVER: 192.168.129.138#53(192.168.129.138)
;; WHEN: Tue Sep 14 15:57:47 EEST 2021
;; MSG SIZE  rcvd: 81
```

Here we notice that there is no `ANSWER SECTION`, but there is an `AUTHORITY SECTION`. The queried server didn't reply with a direct answer to our request but instead pointed us to the name server responsible for answering queries about `nsa.gov`, which turns out to be `ns1.nsa.gov`. 