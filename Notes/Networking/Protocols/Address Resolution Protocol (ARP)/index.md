# Address Resolution Protocol (ARP)

## Introduction

Applications identify hosts on a network via their layer 3 (IP) address, but the actual data is transmitted by dint of layer 2 (MAC) addresses. It is, therefore, necessary to find a way to match an [IP address](<../Internet Protocol (IP)/index.md>) with the appropriate MAC address. This process is called **address resolution**.

There are two main ways to achieve this:

* _Direct Mapping_ - a formula is used to map layer 3 addresses to layer 2 ones. This is the more efficient technique but it is limited in terms of the size of the data link addresses compared to the network layer addresses.
* _Dynamic Resolution_ - this is the method used by the ARP protocol. It allows a host which has just the IP address of its target to determine the MAC address of the target, usually achieved by asking one or more hosts on the network for their MAC and IP addresses. Whilst less efficient and more complex, this technique provides more flexibility.

## The Address Resolution Protocol (ARP)

The **Address Resolution Protocol (ARP)** is the de-facto standard protocol for translating between IP and MAC addresses and vice-versa. It is a _dynamic resolution_ protocol and supports a wide array of layer two technologies, even though it was initially developed for [Ethernet](<../Ethernet (IEEE 802.3).md>).

### Terminology

An ARP **transaction** is the process of two hosts undergoing address resolution. The **source** of a transaction is always the host which wants to send a packet to another device, but does not know the layer 2 address of said device, i.e. the source is the device looking for the appropriate MAC address. The **destination** of a transaction is always the host whose MAC address is being searched for.

Address resolution is done via **messages**, of which there are two types - **requests** and **replies**.

{% hint style="info" %}
{% code overflow="wrap" %}
```
Regardless of the type of message, the **sender** is always the device which transmits the message and the **target** is always the device the message is meant for.
```
{% endcode %}
{% endhint %}

The **Sender Hardware Address** is the layer 2 (MAC) address of the message sender and the **Sender Protocol Address** is their layer 3 (IP) address. The situation is analogous for the **Target Hardware Address** and the **Target Protocol Address**.

{% hint style="warning" %}
```
Do not confuse sender / target with source / destination.
```
{% endhint %}
