# The Domain Name System

## Introduction

Computers connected to the Internet have a numerical identifier - called an Internet Protocol Address (IP Address) - which is used to communicate with this machine. However, remembering a 32-bit number for each computer you want to connect to - even if it's formatted nicely into four separate sections - isn't practical at all. As such, a systematic way of resolving this issue was a created - a sort of lookup table for IP addresses, known as the Domain Name System.

## What is the DNS?

The Domain Name System (or DNS for short) is a decentrialised database which provides answers to queries for _domain names_. Such a query is for example "What is the IP address of google.com? " When such a request is sent out, it will go through the DNS and eventually return with an IP address (if such was found). This saves the average user from having to remember a myriad different IPs for each website they want to visit.

## The DNS Hierarchy

The DNS utilises a hierarchical structure for both storing and serving requested information.

![](../../../Networking/Resources/Images/DNSHierarchy.png)

At the top of the hierarchy are positioned the root name servers. These store and serve information about the top-level domains (TLDs) such as `.net`, `.com`, and `.org`. The TLD servers provide information about domains which use their corresponding TLD - `.com` servers contain information about domains such as `google.com` or `duckduckgo.com`. They won't give you the IP addresses for these hosts, but will instead point you in the right direction - to another DNS server.

The DNS can be thought of as a file system - one where the addresses are read from right to left and instead of forwards slashes, dots are used. The root is represented by a single dot (.), which is usually not visible. Next follow the top-level domains - similar to directories. Going further, we get second level domains and then subdomains, followed by hosts.

## Dissecting a Basic DNS Query

Typing a domain name - such as `google.com` - into your browser will cause your operating system to attempt to resolve that domain name, or in other words - determine its IP address. It will first check locally for an answer as this is the fastest option. It will look into the local cache and the `/etc/hosts` file (on UNIX-like system, or `C:\Windows\System32\drivers\etc\hosts` on Windows). If an answer is not found, the DNS request will be forwarded to your DNS server, which will usually be your home router. Your DNS server may have the answer cached because someone on your network recently queried the same domain. If not, the DNS server will contain an IP address for another name server where you can forward your request - for example the DNS server at your ISP. It's very unlikely that your ISP's name server won't have a cached answer, given the amount of queries that constantly go through it. However, if this happens to be the case, the ISP's name server will carry out further requests on your behalf - exactly how your router forwards the query to your ISP's name server. Name servers can be configured to perform such lookups recursively or not.

If your ISP's name server does not know the IP for the server responsible for `.com` domains, it will ask one of the 13 root name servers, which are designated with the letters A through M). In reality, there are more than 13 physical machines handling these requests. More information about the root name servers you can find [here](https://www.iana.org/domains/root/servers).

This process will continue until you are forwarded to the name server responsible for the domain you are looking for. This name server will provide you with the IP address of your desired domain, which will be cached, allowing quicker access later.

## Zones and Authority

Some name servers are authoritative in a particular subsection of the DNS - they answer queries only for domains in a particular space. Only one name server, known as the _Start of Authority (SOA)_ could give a decisive answer for a particular query. Other name servers may have the answer cached, but only if they have previously requested it in the span of the time-to-live (TTL).

For example, the SOA for `google.com` is only responsible for domains in the `google.com` space. The spaces or _name spaces_ within the DNS are usually referred to as _zones of authority_ or simply _zones_. In reality, there is usually more than a single name server for a big company like Google, however, they both do the same job and are considered the SOA. Their names usually go ns1, ns2, and so forth. Should one name server go offline, the next one would take its place in processing queries.

## DNS Resource Records

I already mentioned that the DNS is similar to a database - one split up and stored around the globe. The entries in this database are called _resource records_ and are usually stored in a flat-file format. Resource records do not only store IP addresses and hostnames - they contain other useful information, as well. These are the most common different types of resource records (a complete list can be found [here](https://en.wikipedia.org/wiki/List\_of\_DNS\_record\_types)):

* **Address of Host (A)** - the IPv4 address of the host
* **Address of Host (AAAA)** - the IPv6 address of the host
* **Canonical Name (CNAME)** - also an alias; two domains might point to the same place, in which case, one would be an alias. Querying the domain in this server will result in the A record.
* **Mail Exchanger (MX)** - refers to a mail server and can contain either an IP address or a hostname
* **Name Server (NS)** - contains the name server information for a given zone
* **Start of Authority (SOA)** - found at the beginning of every zone file, this record is bigger than others and stores the primary name server for the zone, including some other information
* **Pointer (PTR)** - used for reverse DNS lookups - finding the hostname by providing an IP address
* **Text (TXT)** - a simple text record used for adding extra functionality to DNS and storing miscellaneous information. Sometimes used by administrators for leaving humand-readable notes.
