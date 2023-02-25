# Introduction
The Address Resolution Protocol (ARP) serves a method for converting between layer 3 (IP) and layer 2 (MAC) addresses. Whilst applications communicate logically at layer 3, the actual data is transmitted via layers 1 and 2 and so even if the application only knows the destination's IP address, in order for communication to take place, the destination's MAC address is also required.

This is where ARP comes in. However, its naming convention is a bit confusing. The *Source* is always the device which seeks another host's hardware address, whilst the *Destination* is always the host whose MAC address is being sought.

## How does ARP work?
The dynamic resolution method employed by the ARP protocol is rather simple and begins when a machine (the Source) wants to send an IP datagram somewhere:

1. The Source checks its ARP cache to see if it doesn't already have the Destination's MAC address. If so, then simply forward the data there.
2. If not, then broadcast an *ARP Request* frame which contains the Source's MAC and IP addresses and the Destination's IP address.
3. Every host on the network receives the Source's ARP request. If the IP address in the request is not theirs, they simply ignore it.
4. The Destination receives the ARP request and sees that the IP address inside is its own. It then updates its own cache with the Source's MAC and IP address.
5. The Destination sends a unicast ARP reply to the Source with its MAC address.
6. The Source updates its cache with the Destination's MAC and IP addresses and then proceeds with sending its data.

## ARP Message Format

![](Resources/Images/ARP/ARP%20Message%20Format.svg)

The **Hardware Type (HRD)** field specifies the Layer 1 technology powering the network and thus also identifies the type of addressing employed.

|HRD Value|Hardware Type|
|:---:|:---:|
|1|Ethernet (10 mb)|
|6|IEEE 802 Network|
|7|ARCNET|
|15|Frame Relay|
|16|Asynchronous Transfer Mode (ATM)|
|17|HDLC|
|18|Fibre Channel|
|19|Asynchronous Trasfer Mode (ATM)|
|20|Serial Line|

The **Protocol Type (PRO)** field specifies the type of Layer 3 addresses used in the ARP message. The value for this field match the [EtherType](Ethernet%20(IEEE%20802.3).md) codes in an Ethernet frame.

The **Hardware Address Length (HLN)** and **Protocol Address Length (PLN)** specify the lengths, respectively, of the Layer 2 and Layer 3 address used in the ARP message. ARP supports addresses of different sizes in order to be able to operate with technologies which differ from IP and IEEE 802 MAC addresses.

The **Opcode (OP)** indicates the type of message being transmitted.

|Opcode|Message Type|
|:---:|:----:|
|1|ARP Request|
|2|ARP Reply|
|3|RARP Request|
|4|RARP Reply|
|5|DRARP Request|
|6|DRARP Reply|
|7|DRARP Error|
|8|InARP Request|
|9|InArp Reply|

The **Sender Hardware Address (SHA)** is the hardware address of the host issuing the ARP request.

The **Sender Protocol Address (SPA)** is the Layer 3 address of the device issuing the ARP request.

The **Target Hardware Address (THA)** is where the hardware address of the sought device goes.

The **Target Protocol Address (TPA)** is the Layer 3 address of the sought device.

## ARP Caching
