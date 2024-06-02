# ARP Message Format

![](<../../../Networking/Protocols/Resources/Images/ARP/ARP Message Format.svg>)

The **Hardware Type (HRD)** field specifies the Layer 1 technology powering the network and thus also identifies the type of addressing employed.

| HRD Value |           Hardware Type          |
| :-------: | :------------------------------: |
|     1     |         Ethernet (10 mb)         |
|     6     |         IEEE 802 Network         |
|     7     |              ARCNET              |
|     15    |            Frame Relay           |
|     16    | Asynchronous Transfer Mode (ATM) |
|     17    |               HDLC               |
|     18    |           Fibre Channel          |
|     19    |  Asynchronous Trasfer Mode (ATM) |
|     20    |            Serial Line           |

The **Protocol Type (PRO)** field specifies the type of Layer 3 addresses used in the ARP message. The value for this field match the [EtherType](../../../Networking/Protocols/Address%20Resolution%20Protocol%20\(ARP\)/Ethernet%20\(IEEE%20802.3\).md) codes in an Ethernet frame.

The **Hardware Address Length (HLN)** and **Protocol Address Length (PLN)** specify the lengths, respectively, of the Layer 2 and Layer 3 address used in the ARP message. ARP supports addresses of different sizes in order to be able to operate with technologies which differ from IP and IEEE 802 MAC addresses.

The **Opcode (OP)** indicates the type of message being transmitted.

| Opcode |  Message Type |
| :----: | :-----------: |
|    1   |  ARP Request  |
|    2   |   ARP Reply   |
|    3   |  RARP Request |
|    4   |   RARP Reply  |
|    5   | DRARP Request |
|    6   |  DRARP Reply  |
|    7   |  DRARP Error  |
|    8   | InARP Request |
|    9   |  InArp Reply  |

The **Sender Hardware Address (SHA)** is the hardware address of the host issuing the ARP request.

The **Sender Protocol Address (SPA)** is the Layer 3 address of the device issuing the ARP request.

The **Target Hardware Address (THA)** is where the hardware address of the sought device goes.

The **Target Protocol Address (TPA)** is the Layer 3 address of the sought device.
