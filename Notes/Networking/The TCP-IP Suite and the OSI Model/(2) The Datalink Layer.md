# Introduction
There are two major standards which govern how data is transmitted at the datalink layer. The first on is a protocol called [Ethernet](../Protocols/Ethernet%20(IEEE%20802.3).md) and it describes the transfer of data in wired LANs. It is defined in the IEEE 802.3 standard.

The second one is the IEEE 802.11 WLAN standard and it describes how data is transferred in *wireless* networks over WiFi.

# MAC Addresses
Both protocols avail themselves of the so-called *MAC addresses*. In order words, MAC addresses operate at the datalink layer. A MAC address is a 6-byte (48-bit) value assigned to every device when it is manufactured and typically takes the form of `XX:XX:XX:XX:XX:XX` in hexadecimal. It may also be referred to as a burnt-in address (BIA). This address is globally unique and no two devices in the world should have the same MAC addresses.

The first 3 bytes of every MAC addresses are the *Organisationally Unique Identifier (OUI)* and it is assigned to the company making the device. All devices manufactured by this company will share the same 3 bytes - the company's OUI. The second half the MAC address is unique for every device and is what identifies it.

MAC addresses are used extensively in switches and routers at the datalink layer.
