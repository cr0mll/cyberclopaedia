---
cover: ../../../.gitbook/assets/favicon_black.png
coverY: 0
---

# Reverse Address Resolution (RARP)

## Introduction

The ARP protocol can also be used to find the IP address of a device when only knowing its MAC address.

{% hint style="info" %}
When ARP is utilised to find an IP address, it is called RARP for "reverse ARP".
{% endhint %}

This is a common situation in the so-called "bootstrapping", or starting from zero. In such cases a device X may not know its own IP address, but know its MAC address, since it is embedded in the hardware. But who knows X's IP address if not X itself?

The answer is a RARP server. The RARP server listens for RARP broadcasts and responds to them with the appropriate IP address.

## Reverse Address Resolution

The process for reverse address resolution avails itself of the same ARP protocol and the terminology remains the same, except that the source and the destination may now be the exact same device.

1. _The source device generates a RARP request message:_ This is done by using the value 3 for the [Opcode](arp-message-format.md) of the request. It populates the [Sender Hardware Address](./) and [Target Hardware Address](./) with its own MAC address, but leaves the [Sender Protocol Address](./) and [Target Protocol Address](./), since they are unknown.
2. _The source device broadcasts the RARP request on the network:_ All devices which are not a RARP server simply ignore the broadcast.
3. _RARP server receives the RARP request and generates a RARP response:_ Any device set up as a RARP server will process the broadcasted request and generate an appropriate response. The Opcode for a RARP response is the value 4. The RARP server sets the Sender Hardware Address and Sender Protocol Address to its own MAC and IP address, respectively, and populates the Target Hardware Address with the MAC address which it obtained from the request. Ultimately, it looks up this MAC address in a table in order to determine the corresponding IP address which it then places in the Target Protocol Address field.
4. _RARP server sends the RARP response back to the source:_ Note that there is no need to broadcast the response.
5. _The source device receives the RARP response:_ The source device may receive multiple responses if multiple RARP servers are configured. In this case, it usually uses the first response, whilst ignoring the rest. The source determines its own IP address from the Target Protocol Address in the response.

![](<../../../Networking/Protocols/Address Resolution Protocol (ARP)/Resources/Images/Reverse Address Resolution.svg>)
