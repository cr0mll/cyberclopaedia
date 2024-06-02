# Internet Protocol v4 (IPv4)

## Introduction

IPv4 is the most widely used version of the internet protocol and facilitates the delivery of datagrams across an internetwork. Not only does this protocol identify a particular network interface, but it also provides _routing_ which is required when the source and destination lie in different networks.

## IP Addressing

Every device which has a network interface used for data transfer at the network layer will have at least one IP address - one for every interface. Additionally, a single interface may have multiple IP addresses if it is _multihomed_. Lower-level network equipment such as repeaters, bridges and switches don't require IP addresses because they operate solely at layer 2.

Every IP address needs to be unique - no two hosts are allowed to share an IP address. This was easy to implement in the early ages of the Internet because there weren't that many hosts. However, as time progressed, the number of devices on the Internet rapidly increased and at one point exceeded the total number of available IP addresses!

### Public vs Private Addresses

This lead to the division of IP addresses into public and private and gave birth to IP Network Address Translation (NAT).

A _private_ or _local_ IP address is the IP addresses assigned to you when you join a private network such as your home Wi-Fi network or you connect to your work's network via an Ethernet cable. The same private IP address can be assigned to the same device when it is connected to different private networks. For example, your phone could be given the IP `192.168.0.101` on your home network and then be given the same IP address when you later go to your friend's house and connect to their Wi-Fi.

A _public_ or _global_ IP address is the IP address which is assigned to you on the entirety of the Internet. For example, your home Wi-Fi router will have a global IP addresses provided by your ISP. These are unique in the scope of the entire Internet! If you have the public IP `54.236.18.128`, then no other person in the world can have this same public IP.

### IP Address Format

An IP address is essentially a 32-bit number. For us humans, it is useful to divide it into four octets and convert it to decimal to make it easier to read, but computers make no such distinction. This is called dotted decimal notation since the IP address is presented in the format `x.x.x.x`. Each octet value can range from 0 to 255 inclusive. For example, the IP `76.233.44.184` has the following format in binary and hex:

![](<../../../../Networking/Protocols/Internet Protocol (IP)/Internet Protocol v4 (IPv4)/Resources/Images/IP Dotted Decimal.svg>)

Since IP addresses are 32 bits wide, the number of possible IP addresses is $2^{32} = 4,294,967,296$. Not only is the actual number way lower due to addresses reserved by the protocol's specification, but there are already a lot more than 4,294,967,296 devices using the Internet!

The 32 bits of an IP address are logically divided into a _Network Identifier (Network ID)_, sometimes also called the _(network) prefix_, and a _Host Identifier (Host ID)_. The cusp between those two parts, however, is not fixed and is determined by the type of addressing used.

The Network ID is what causes IPs to be network-specific, enabling the separation between private networks and the Internet as well as nesting of private networks. On the other hand, it also necessitates NAT.

![](<../../../../Networking/Protocols/Internet Protocol (IP)/Internet Protocol v4 (IPv4)/Resources/Images/Network and Host ID.svg>)

The line dividing the two components of an IP address is usually at the border between two octets, but as shown in the above example, that may not be the case.
