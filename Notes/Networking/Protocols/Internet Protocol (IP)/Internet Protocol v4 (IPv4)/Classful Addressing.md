# Introduction
This was the original addressing scheme devised for IP which divided the IP address space into *classes*, each dedicated to specific uses. Certain classes would be devoted to large networks on the Internet, while others would be assigned to smaller organisation, and yet others would be reserved for special purposes. Needless to say, this system has outlived its usefulness due to the huge number of hosts connected to the Internet at present day. Nevertheless, one should still be able to understand it.

## Classes
There are 5 classes defined for this system and they are outlined in the table below:

|Class|Portion of the Total IP Address Space|Number of Network ID bits|Number of Host ID bits|Use|
|:----:|:-----:|:----:|:----:|:---:|
|Class A|1/2|8|24|Unicast addressing for very large organisations (hundreds of thousands to millions of hosts.|
|Class B|1/4|16|16|Unicast addressing for medium-size organisations (hundreds to thousands of hosts).|
|Class C|1/8|24|8|Unicast addressing for small organisations (no more than 250 hosts).|
|Class D|1/16|N/A|N/A|IP Multicasting.|
|Class E|1/16|N/A|N/A|Reserved for experimental use.|

The class an IP address belongs to is determined by its first four bits:
1. If the first bit is 0, then the IP address belongs to class A. If the first bit is a 1, proceed with the next step.
2. If the second bit is 0, then the iP address belongs to class B. If the second bit is a 1, proceed with the next step.
3. If the third bit is 0, then the IP address belongs to class C. If the third bit is a 1, proceed with the next step.
4. If the fourth bit is 0, then the IP address belongs to class D. If the fourth bit is 1, the IP belongs to class E.

Since the beginning of every IP determines its class, each class is associated with a specific IP range.

|Class|First Octet|Network ID / Host ID Octets|Theoretical Range|
|:---:|:----:|:----:|:----:|
|Class A|0xxx xxxx|1/3|1.0.0.0 - 126.255.255.255|
|Class B|10xx xxxx|2/2|128.0.0.0 - 191.255.255.255|
|Class C|110x xxxx|3/1|192.0.0.0 - 223.255.255.255|
|Class D|1110 xxxx|N/A|224.0.0.0 - 239.255.255.255|
|Class E|1111 xxxx|N/A|240.0.0.0 - 255.255.255.255|

![](Resources/Images/Classful%20IP%20Address%20Format.svg)

The provided ranges are solely theoretical due to the fact that many IP addresses are actually reserved and/or have special meanings. 

## Loopback Addressing
The IP range from `127.0.0.0` to `127.255.255.255` is reserved for *loopback addressing*. Datagrams sent to an IP address in this range are not passed down to the data link layer and are instead directly "loop-ed back" to the host that sent them. In a sense, loopback addresses mean "me". Sending a datagram to such an address is equivalent as sending it to yourself.

While the most commonly used loopback address is `127.0.0.1`, *any* IP address in this range will result in the same functionality.

## Problems
1. Lack of internal address flexibility - large organisations are assigned large blocks of addresses which do not necessarily match well the structure of the underlying internal networks. It is not possible to create an internal hierarchies of IP addresses - all hosts in big networks such as class A or class B networks would have to share a single address space.
2. Low Granularity - a lot of the IP addresses space is wasted because of the existence of only three possible network sizes - classes A, B and C. Suppose an organisation had a network with only 1,000 hosts. It would be assigned an entire class B network (these are two many hosts to fit into a class C network) which would result in the wasting of nearly 64,000 possible IP addresses!