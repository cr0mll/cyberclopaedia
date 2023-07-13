# Introduction
Packets at the network layer are referred to as *datagrams*. The IP protocol takes date from the transport layer and encapsulates it by adding to it an *IP header*. Once this header is added, the packet becomes an IP datagram. This datagram is then passed onto the data link layer.

# IP Header
An IP datagram is divided into an *IP header* and a *payload*. The latter contains the transport-layer data which was passed to the network layer, while the former contain information about the datagram itself. 

The IP header is a variable-length header with a minimum size of 20 bytes.

![](Resources/Images/IPv4%20Datagram.svg)

### Version
This is a 4-bit field which identifies the IP protocol version used in the datagram. For IPv4, this field is equal to 4. Typically, implementations which run an older version of the IP protocol will reject datagrams which use a newer one, under the assumption that the old implementation might incorrectly handle them.

### Internet Header Length (IHL)
This 4-bit field contains the length (measured in 32-bit words) of the IP header, including options and any padding. The lowest value for this field - when there are no options and thus no padding - is 5 (`5*4 = 20` bytes in total).

### Differentiated Service Code Point (DSCP) & Explicit Congestion Notification (ECN)
These two fields were originally defined as a single *Type of Service (TOS)* field which was supposed to render quality of service features, such as prioritised delivery. It never saw wide adoption which is why it was redefined as two separate field.

The *Differentiated Service Code Point (DSCP)* is a 14-bit field which specifies [differentiated services](https://en.wikipedia.org/wiki/Differentiated_services). It is used by data streaming services such as Voice over IP (VoIP).

The *Explicit Congestion Notification* (ECN) is a 2-bit field which allows for end-to-end notification of network congestion without dropping any datagrams. It is an optional feature available when both the two endpoints and the underlying network support it.

### Total Length (TL)
This 2-byte field specifies the *total length* (in bytes) of the IP datagram - IP header + data payload. Its size, 16-bits, determines the maximum size of an IP datagram - 65 535 bytes. If this limit is exceeded, fragmentation occurs. In practice, most datagrams are much smaller.

### Fragmentation Fields
The next three fields relate to fragmented datagrams.

The *Identification* field is 2 bytes in size and contains a value which is shared by all fragments pertaining to a specific message. It is used by the recipient for datagram reassembly in order to avoid different messages getting mixed up. It is important to note that this field is still populated for unfragmented datagrams because they may need to be split up later in the transmission process.

The *Flags* are 3 bits which control fragmentation.

![](Resources/Images/IPv4%20Fragmentation%20Flags.svg)

|Flag|Meaning|
|:---:|:---:|
|Reserved|Not used.|
|Don't Fragment (DF)|When set to 1, it specifies that the datagram should not be fragmanted. In practice, this flag is only used when testing the maximum transmission unit (MTU) of a link.|
|More Fragments (MF)|A value of 0 indicates that this is the last fragment in the transmission. A value of 1 means that there are more fragments on the way. This bit is always 0 for unfragmented datagrams.|

The *Fragment Offset* field is 13 bits wide and specifies the offset (measured in units of 64 bits or 8 bytes) in the original message  in the original message at which the data from this fragment goes.

### Time To Live (TTL)
This 1-byte field contains the number of remaining router hops before the datagram is deemed expired. Each router that the datagram passes through decrements the TTL by one and If it reaches 0, the datagram is dropped and an ICMP *Time Exceeded* message is usually sent back to the sender to inform them.

This mechanism was put in place in order to prevent datagrams from getting stuck in infinite cycles between routers. While it rarely happens, it is possible for a datagram to be forward from router A to router B to router C and then back to A which would result in a loop.

Interestingly, the TTL can sometimes be used for enumerating the operating system - unix-based systems use an initial TTL of 64, while Windows uses 128.

### Protocol
This 1-byte field indicates the upper-layer protocol encapsulated by the IP datagram. The list of possible values for this field is maintained by IANA.

|Value|Protocol|
|:----:|:-----:|
|`0x00`|Reserved.|
|`0x01`|ICMP|
|`0x02`|IGMP|
|`0x03`|GGP|
|`0x04`|IP-in-IP Encapsulation|
|`0x06`|TCP|
|`0x08`|EGP|
|`0x11`|UDP|
|`0x32`|Encapsulating Security Payload (ESP) Extension Header|
|`0x33`|Authentication Header (AH) Extension Header|

### Header Checksum
This 2-byte field contains a value which is calculated by dividing only the IP header into two-byte sections and then summing their values. This is used to provide basic integrity checking - each router the datagram goes through will perform the same calculation on the IP header and if the result does not match with the specified checksum, the datagram will be discarded as corrupted.

It is important to note that the data does *not* figure in the calculation of the checksum.

### Source & Destination Addresses
These are two 4-byte fields representing respectively the source and destination IP addresses. Even though an IP address may be forwarded multiple times through a bunch of routers, the source and destination addresses are unchanged.

### Options
The *Options* field is variable in length and is, well, optional. Every IP header must be at least 20 bytes in size and contains key information. However, additional information can be added via options, thus increasing the header's size. 

Each option has the following format:

![](Resources/Images/IPv4%20Option.svg)

The *Option Type* is an 8-bit field subdivided into three subfields, which are described in the table below.

|Subfield|Size (in bits)|Meaning|
|:---:|:----:|:----:|
|Copied|1|If this bit is set to 1, then the option should be copied into all fragments if the datagram is fragmented. A value of 0 indicates that this option should *not* be copied.|
|Option Class|2|Specifies one of four potential categories the option belongs to. Only two of the values are used - 0 is for *Control* options and 2 is for *Debugging and Measurement* options.|
|Option Number|5|Specifies the kind of option. Each of the two available classes has a maximum of 32 different types of options.|

The *Option Length* is only present in variable-length options and indicates the size (in bytes) of the *entire* option - including the Option Type, Option Data and itself.

The *Option Data* is only present in variable-length options and stores the data pertinent to the option.

Following is a list of possible IP options. TODO: complete

|Option Name|Option Class|Option Number|Option Length (in bytes)|Description|
|:---:|:---:|:---:|:---:|:---:|
|End of Options List|0|0|1|An option containing a single zero byte which indicates the end of the options list.|
|No Operation|0|1|1|A dummy option which is used for internal alignment requirements on 32-bit boundaries within the Options field when necessary.|
|Security|0|2|11|An option for the military to indicate the security classification of IP datagrams.|
|Loose Source Route|0|3|Variable|Used for source routing.|
|Record Route|0|7|Variable|Allows for the recording of the datagram's route. Each router the datagram passes through will append its IP address to this option. The maximum size for this route is set by the datagram's origin and so if it fills up, no further addresses will be added to it.|
|Strict Source Route|0|9|Variable|Used for source routing.|
|Timestamp|2|4|Similarly to Record Route, each router the datagram passes through will put a timestamp on it. The maximum size of this option is once again said by the original sender and so no further timestamps will be added after it is exceeded.|
|Traceroute|2|18|12|Used in the implementation of the traceroute utility.|

### Padding
The size of the IP header must be a multiple of 32-bits, so padding bits set to 0 may be added following any options in order to fulfil this requirement.

# Fragmentation
