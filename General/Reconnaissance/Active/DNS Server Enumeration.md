# Enumerating BIND servers with CHAOS
The BIND software is the most commonly used name server software, which supports CHAOSNET queries. This can be used to query the name server for its software type and version. We are no longer querying the domain name system but are instead requesting information about the BIND instance. Our queries will still take the form of domain names - using `.bind` as the top-level domain. The results from such a query are returned as `TXT` records. Use the following syntax for quering BIND with the CHAOS class:
```bash
dig @<name server> <class> <domain name> <record type>
```
```bash
┌──(backslash0@kali)-[~]-[]
└─$ dig @192.168.129.138 chaos version.bind txt 

; <<>> DiG 9.16.15-Debian <<>> @192.168.129.138 chaos version.bind txt
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 38138
;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 1, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;version.bind.                  CH      TXT

;; ANSWER SECTION:
version.bind.           0       CH      TXT     "9.8.1"

;; AUTHORITY SECTION:
version.bind.           0       CH      NS      version.bind.

;; Query time: 0 msec
;; SERVER: 192.168.129.138#53(192.168.129.138)
;; WHEN: Tue Sep 14 16:24:35 EEST 2021
;; MSG SIZE  rcvd: 73
```
Looking at the answer section, we see that this name server is running BIND 9.8.1. Other chaos records you can request are `hostname.bind`, `authors.bind`, and `server-id.bind`.

# DNS Zone Transfer
A *Zone transfer* request provides the means for copying a DNS zone file from one name server to another. This, however, only works over TCP. By doing this, you can obtain all the records of a DNS server for a particular zone. This is done through the `AXFR` request type:
```bash
dig @<name server> AXFR <domain>
```
```bash
┌──(backslash0@kali)-[~]-[]
└─$ dig @192.168.129.138 AXFR nsa.gov 

; <<>> DiG 9.16.15-Debian <<>> @192.168.129.138 AXFR nsa.gov
; (1 server found)
;; global options: +cmd
nsa.gov.                3600    IN      SOA     ns1.nsa.gov. root.nsa.gov. 2007010401 3600 600 86400 600
nsa.gov.                3600    IN      NS      ns1.nsa.gov.
nsa.gov.                3600    IN      NS      ns2.nsa.gov.
nsa.gov.                3600    IN      MX      10 mail1.nsa.gov.
nsa.gov.                3600    IN      MX      20 mail2.nsa.gov.
fedora.nsa.gov.         3600    IN      TXT     "The black sparrow password"
fedora.nsa.gov.         3600    IN      AAAA    fd7f:bad6:99f2::1337
fedora.nsa.gov.         3600    IN      A       10.1.0.80
firewall.nsa.gov.       3600    IN      A       10.1.0.105
fw.nsa.gov.             3600    IN      A       10.1.0.102
mail1.nsa.gov.          3600    IN      TXT     "v=spf1 a mx ip4:10.1.0.25 ~all"
mail1.nsa.gov.          3600    IN      A       10.1.0.25
mail2.nsa.gov.          3600    IN      TXT     "v=spf1 a mx ip4:10.1.0.26 ~all"
mail2.nsa.gov.          3600    IN      A       10.1.0.26
ns1.nsa.gov.            3600    IN      A       10.1.0.50
ns2.nsa.gov.            3600    IN      A       10.1.0.51
prism.nsa.gov.          3600    IN      A       172.16.40.1
prism6.nsa.gov.         3600    IN      AAAA    ::1
sigint.nsa.gov.         3600    IN      A       10.1.0.101
snowden.nsa.gov.        3600    IN      A       172.16.40.1
vpn.nsa.gov.            3600    IN      A       10.1.0.103
web.nsa.gov.            3600    IN      CNAME   fedora.nsa.gov.
webmail.nsa.gov.        3600    IN      A       10.1.0.104
www.nsa.gov.            3600    IN      CNAME   fedora.nsa.gov.
xkeyscore.nsa.gov.      3600    IN      TXT     "knock twice to enter"
xkeyscore.nsa.gov.      3600    IN      A       10.1.0.100
nsa.gov.                3600    IN      SOA     ns1.nsa.gov. root.nsa.gov. 2007010401 3600 600 86400 600
;; Query time: 4 msec
;; SERVER: 192.168.129.138#53(192.168.129.138)
;; WHEN: Fri Sep 17 22:38:47 EEST 2021
;; XFR size: 27 records (messages 1, bytes 709)
```

