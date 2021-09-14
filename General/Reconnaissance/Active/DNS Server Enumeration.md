# Enumerating BIND servers with CHAOS
The BIND software is the most commonly used name server software, which supports CHAOSNET queries. This can be used to query the name server for its software type and version. We are no longer querying the domain name system but are instead requesting information about the BIND instance instead. Our queries will still take the form of domain names - using `.bind` as the top-level domain. The results from such a query are returned as `TXT` records. Use the following syntax for quering BIND with the CHAOS class:
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