# VLANs

Virtual LANs provide the means for logically separating a LAN at Layer 2 and can be thought of as the Layer 2 counterpart to the Layer 3 subnets. The reasons to do this are typically bandwidth- and security-related and have to do with broadcast frames.

Imagine the following LAN, without VLANs configured:

![](../Networking/Resources/Images/VLAN\_not.png)

The Engineering and Sales departments are assigned to different subnets.

If PC1 wants to send a broadcast frame, or even just an unknown unicast frame, to the Engineering department, it has to send it to the switch with a destination MAC address of `FF:FF:FF:FF:FF:FF`. You would expect that the switch would now only broadcast this frame to the Engineering department, but since there are no VLANs configured and the switch isn't aware of subnets - it only works with Layer 2, - the frame is actually broadcasted to the Sales department, as well! This is suboptimal because there is unnecessary traffic sent (the frame was meant for the Engineering department) and because it may unnecessarily leak information to the Sales department which poses a security risk.

One solution is to buy separate switches for the two departments but this is not very budget-friendly. Another solution is to configure separate virtual LANs for the Engineering and Sales departments. This is done in the switch and is configured with respect to the switch's interfaces -it is _not_ done with respect to the MAC addresses. A group of interfaces is grouped into a VLAN and any host connected to that interface becomes part of the VLAN.

![](../Networking/Resources/Images/VLAN.png)

In the above example, the switch's interfaces `FO/0`, `FO/1`, `FO/2`, `FO/3` have been grouped into VLAN10, while `FO/4`, `FO/5`, `FO/6`, `FO/7` have been configured into VLAN20. These interfaces are referred to as _access ports_, since they only allow traffic from a single VLAN. Now, whenever PC1 sends out a broadcast frame with `FF:FF:FF:FF:FF:FF` as its destination, the switch is only going to broadcast the frame to the interfaces in VLAN10.

But what happens when PC1 wants to communicate with a device that is in the Sales department? In this case, PC1 sets the destination MAC to the MAC of the router which will then replace the source MAC with its own and forward the frame to the correct destination. In other words, all traffic that crosses between VLANs must be routed by the router.

## Trunk Ports

Typically, every interface can only forward traffic from a single VLAN. This, however, results in the wasting of many interfaces. Such is the case with the above router - there is an interface taken for every VLAN. In order to remedy this, the so-called _trunk ports_ can be used.

![](../Networking/Resources/Images/VLAN\_trunk.png)

However, since a trunk port allows for traffic from many VLANs, it is not possible to determine to which VLAN the traffic belongs solely based on the interface it is flowing through. Therefore, a way of _tagging_ each frame must be implemented by the switch. There are two main protocols for achieving this - the now obsolescent ISL (Inter-Switch Link) protocol, which is a propriety Cisco protocol which is not even used by Cisco anymore, and the [IEEE 802.1Q standard](protocols/ethernet-ieee-802.3.md#8021q-encapsulation) (also called "dot1q").

![](../Networking/Resources/Images/VLAN\_trunking.png)

Due to the size of the VID field in the dot1q tag, there are a total of $2^{12} = 4096$ VLANs. Two of them - the first and last one - are reserved and cannot be used. Therefore, the actual range for VLANs is from 1 to 4094. This range is further subdivided:

* Normal VLANs: 1 - 1005
* Extended VLANs: 1006 - 4094

Very rarely, the extended range may not be supported by older switches.

Note that in order to turn a router interface into a trunk port, it needs to be specifically configured in the router. This is referred to as a Router-On-A-Stick (ROAS).

### Native VLAN

802.1Q is equipped with an additional feature called _native VLAN_. This is configured _per trunk port_ and defaults to VLAN 1. Frames in the native VLAN are not augmented with a 802.1Q tag by the switch. When a frame is received by a switch on an untagged trunk port, it is assumed that his frame belongs to the native VLAN. It is paramount that the native VLANs for a trunk link match between switches! Otherwise, situations can arise where traffic is dropped.

![](../Networking/Resources/Images/VLAN\_native\_mismatch.png)

Suppose that SW1 and SW2 have their trunk ports' native VLANs set to 20 and 10, respectively. Suppose that the PC3 wants to communicate with PC1. PC3 sends a frame to SW2 which forwards it without adding a tag, since the trunk port's native VLAN is 10 and the frame originates from this VLAN. Once the frame reaches SW1, it sees that the frame is untagged and, since the native VLAN for the trunk port for SW1 is configured to be 20, it assumes that the frame pertains to VLAN 20. However, the destination MAC does not belong to VLAN 20, so the switch assumes that an error occurred and drops the frame.

![](../Networking/Resources/Images/VLAN\_native\_mismatch\_2.png)

Similarly, if PC3 wants to communicate with PC5, it sends out a frame to SW2. This frame is forwarded to the router and then returned back to SW2 where it is tagged with VLAN 20 and sent to SW1. However, when the frame is received by SW1, the switch expects a frame for VLAN 20 to be untagged due to its configuration. However, this frame _does_ contain a tag because the native VLAN of SW2 is different. Thus, SW1 assumes an error occurred and drops the frame.
