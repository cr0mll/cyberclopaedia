# Address Resolution

The source wants to send an IP datagram to the destination. This is what happens in order to determine the destination's MAC address:

1. _The source device checks its cache:_ - The source device examines its own ARP cache. If it has an entry for the destination, then the IP datagram is forwarded directly, since the MAC address for this IP is known, and address resolution ends here. If there is no entry in the ARP cache, continue with step 2.
2. _The source device generates an ARP_ [_request_](index.md#terminology)_:_ The source device generates an ARP request by filling the [Sender Hardware Address](<ARP Message Format.md>) and [Sender Protocol Address](<ARP Message Format.md>) with its own MAC and IP addresses, respectively. The [Target Protocol Address](<ARP Message Format.md>) is filled with the destination's IP address and the [Target Hardware Address](<ARP Message Format.md>) is left blank, since that is what the source is trying to determine.
3. _The source device broadcasts the ARP request:_ The source device broadcasts the generated ARP request to all devices connected to the network. All devices whose IP address does not match the Target Protocol Address in the request (i.e. all devices which are not the destination) simply ignore it.
4. _The destination device receives the ARP request:_ The destination device receives the ARP request and constructs an appropriate ARP response by filling the Sender Hardware Address and the Sender Protocol Address with its own MAC and IP address, respectively. It then fills the Target Hardware Address and Target Protocol Address with the MAC and IP address of the source, which are extracted from the ARP request. Since it is likely for further communication to take place between these two devices, as an optimisation, the destination updates its ARP cache with an entry for the source, in order to remember its IP and MAC address.
5. _The destination device sends the ARP response to the source:_ The destination devices sends the ARP response back to the source. Note that, in contrast to the ARP request, the response is _not_ broadcast to all devices.
6. _The source device receives the ARP response:_ The source device receives the ARP response from the destination and extracts the Sender Hardware Address from it, which is the destination's MAC address. This is now used to send the IP datagram. Additionally, the source updates its ARP cache by adding to it the Sender Hardware Address and Sender Protocol Address of the ARP response, in order to remember the destination's MAC and IP address for any future communication.

![](<Resources/Images/ARP Address Resolution.svg>)

{% hint style="info" %}
<pre data-overflow="wrap"><code><strong>
</strong><strong>In step 3, the ARP standard actually requires that all devices which receive the broadcasted ARP request update their ARP cache with an entry for the source. However, this might be undesirable on large networks, as every device would very quickly have an ARP cache table filled with entries for all other devices on the network. In practice, this is left up to the underlying implementation.
</strong><strong>
</strong></code></pre>
{% endhint %}
