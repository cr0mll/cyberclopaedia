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

```admonish note
The data does *not* figure in the calculation of the checksum.
```

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
IPv4 datagrams are ultimately passed onto the data-link layer. Depending on what protocol is employed at that level, the maximum size of a frame, called the *Maximum Transmission Unit (MTU)*, is limited. The implementation of the IP layer on every device must, therefore, be cognisant of the MTU of the underlying data-link protocol. When an IP datagram is to be transmitted, the IP implementation checks what the size of the datagram would be after the addition of the IP header and if this size exceeds the MTU, then fragmentation is necessary.

This is seen when a datagram passes from a network with a high MTU to a network with a low MTU. Since IP datagrams may hop to and from multiple networks before reaching their ultimate destination, it is common for the fragments of a datagram to themselves get fragmented along the way!

Each router needs to be able to fragment datagrams with a size up to the highest MTU network that the router is connected to. Additionally, every router must support a minimum MTU of 576 bytes, defined in RFC 791, in order to allow for a reasonable message size of 512 bytes including bytes for the IP header.

## Datagram Disassembly
When a datagram's size exceeds the MTU of the network it is to be sent through, the datagram needs to be fragmented. The IP header of the first fragment is largest and has a size which we denote by $s_0$. Each subsequent fragment also gets an IP header, but the size of this header, $s \le s_0$, is the same for all fragments, apart from the first one. 

```admonish note
Datagrams whose size exceeds the MTU but have the *Don't Fragment* flag set to 1 will be dropped and an ICMP Destination Unreachable: "Fragmentation Needed and Don't Fragment Bit Set" message will be returned to the sender.
```

If we let $n$ be the number of bytes the original datagram is made up of, $m$ be the MTU, then the algorithm for datagram fragmentation can be written as follows:

1. Create the first fragment by taking the first $m - s_0$ bytes from the IP datagram's data. 
2. Create the next fragments by taking the first $m - s$ bytes from the remaining data bytes.
3. Create the last fragment by taking all of the left-over data bytes.
4. Generate the IP headers
	- IP header of the first fragment - the original IP header is copied into the IP header of the first fragment.
	- IP header of the subsequent fragments - copy the original IP header but only include the options marked as *Copied*.
	- Populate the fields of the IP headers.

The `Total Length` is set to the size of each fragment, not the size of the original message.

```admonish
The size of each fragment must be a multiple of 8 to allow for proper offset calculation.
```

The `Identification` field is set to a value unique for the message but which is the same for all of the *fragments* of the message and it is used by the destination to determine which fragments belong to the message.

The `More Fragments` flag is set to 1 for all the fragments except for the last one where it is set to 0.

The `Fragment Offset` indicates where a fragment's data is supposed to be in the original datagram. This offset is specified in units of 8 bytes (hence why the length of each fragment must be a multiple of 8).

```admonish example
Suppose we had an MTU of 3300 bytes and a datagram of size 12,000 bytes including the IP header, which, for the sake of simplicity, contained no options and was thus 20 bytes long. Therefore, the size of the actual data will be $12,000 - 20 = 11,980$ bytes.

The first fragment will take the first 3280 bytes of the datagram's data, leaving $11,980 - 3280 = 8700$ bytes of data.

The second fragment will take the next 3280 bytes of data, leaving $8700 - 3280 = 5420$ bytes.

The third fragment will take the next 3280 bytes of data, leaving $5420 - 3280 = 2140$ bytes.

The last fragment will take the remaining 2140 bytes.

The `Total Length` fields of the fragments will be set respectively to 3300, 3300, 3300 and 2160.

The `Identification` field of all the fragments will be set to the same value, for example `0xbeef`.

The `More Fragments` field of the last fragment will be set to 0 and for the rest of the fragments it will be set to 1.

The `Fragment Offset` for the first fragment will be 0. The second fragment's data begins at an offset of 3280 bytes from the start of the initial datagram's data and so its `Fragment Offset` will be set to $3280 / 8 = 410$. The third fragment's data begins at an offset of $3280 + 3280 = 6560$ from the original datagram's data and so its `Fragment Offset` will be set to $6560 / 8 = 820$. Finally, the last fragment will have a `Fragment Offset` equal to $1230$ because its data begins at an offset of $3280 \times 3 = 9840$ from the initial datagram's data.
```



## Datagram Reassembly
Datagram reassembly is the inverse of the fragmentation process but it is *not* symmetric. This is because while an intermediate router can fragment a datagram, it cannot reassemble it. Reassembly is only done by the final recipient and follows this algorithm:

1. Fragment Recognition - the recipient knows it has received fragment from a new message when it sees a datagram with `More Fragments` set to 1 or a `Fragment Offset` different from zero which has a previously unseen `Identification` field.
2. Buffer Initialisation - the recipient initialises a buffer for the new message and populates it with data from message fragments according to their `Fragment Offset` as they arrive.
3. Timer Initialisation - the recipient also initialises a timer. Since fragments may get lost and may thus never be received by the recipient, when the timer expires the message is dropped and an ICMP Time Exceeded message is sent back to the sender.
4. Transmission Completion - the recipient knows it has received the entire message when it has the message fragment with `More Fragments` set to 0 and the entire buffer is filled up. From this point forward, the message is processed as a normal IP datagram.