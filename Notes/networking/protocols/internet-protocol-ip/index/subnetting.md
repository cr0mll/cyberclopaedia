# Subnetting

## Introduction

Subnetting is an extension of the [classful addressing](classful-addressing.md) scheme. It strives to solve some of its problems by introducing a three-level hierarchy. It divides networks into _subnets_ (sub-networks) each of which contains a number of hosts. This gives rise to the two main advantages:

* **Flexibility** - each organisation can customise the number of subnets and hosts per subnet to better suit its physical network structure.
* **Invisibility** - subnets are invisible to the public Internet and so no information about an organisation's internal structure is revealed to the public.

## Subnet Addressing

In order to achieve its goals, subnetting introduce a third division of the IP address - the _subnet ID_. This is done by taking bits from the host ID and repurposing them. Additionally, the number of subnets may vary from network to network and so the the subnet ID lacks a fixed size. Therefore, an additional piece of information called the _subnet mask_ is necessary in order to determine where the cusp between the subnet ID and the host ID lies.

![](<../../../../Networking/Protocols/Internet Protocol (IP)/Internet Protocol v4 (IPv4)/Resources/Images/Subnetting.svg>)

### Subnet Mask

The subnet mask is what determines which bits of an IP address identify the subnet it belongs to and is what determines the boundary between the subnet ID and the host ID. Similarly to an IP address, it is a 32-bit number and so it often represented as an IP even though in reality it is not.

The bits which are set to 1 in the subnet mask indicate which bits in the IP address are part of the network ID or the subnet ID. On the other hand, the bits set to 0 in the subnet mask indicate the bits in the IP address which represent the host ID. That's really all there is to it.

The subnet mask is called this way because it can be used with bitwise operations to obtain from an IP address only the part which represents the network and subnet. When AND-ing the mask with an IP, the bits in the address which represent the host ID are set to 0, while the rest are left intact. The address obtained from this operation is the _subnet address_.

For example, consider the IP address `134.12.67.203` belonging to a class B network and suppose we are using 5 bits for the subnet ID. This means that our subnet mask will contain $16 + 5 = 21$ bits equal to 1 and the rest will be 0.

![](<../../../../Networking/Protocols/Internet Protocol (IP)/Internet Protocol v4 (IPv4)/Resources/Images/Subnet Mask.svg>)

Interestingly enough, subnet masks need not be contiguous. Technically, the bits for the subnet ID can between bits representing the host ID, giving rise to the following monstrosity: `11111111.11111111.10101010.01010101`. Yeah, good luck trying to figure out what is the host ID and what is the subnet ID of an IP address when using this mask. Thankfully, this is never used in practice and a lot of hardware does not even support it. Why was it created? Your answer is as good as mine.

#### Default Subnet Mask

Since the subnet mask indicates which bits belong to either the network ID or the subnet ID, if no bits are used for the subnet ID, then all the bits in the subnet mask will correspond to the network ID. This gives rise to a concept known as the _default subnet mask_ for each of the unicast classes.

![](<../../../../Networking/Protocols/Internet Protocol (IP)/Internet Protocol v4 (IPv4)/Resources/Images/Default Subnet Masks.svg>)

These are essentially the subnet masks that are used by an organisation when it has not created any subnets for it internal structure.

#### Custom Subnet Mask

Now, when an organisation wants to create subnets within its network, it needs to first decide how many subnets it will have. If the number of bits it decides to use for the the subnet ID is $n$, then it can have a total of $2^n$ subnets which will all be of the same size.

To construct the subnet mask for this network, start with the default subnet mask for the class the network belongs to and then flip $n$ of the zero bits to 1s.

### Number of Subnets & Hosts

One network uses a single subnet mask to determine _how many_ subnets it has. But this subnet mask can also be used to determine size of each subnet (i.e., the number of hosts any subnet on the network can have.

The _number of subnets_ is equal to $2^s$ where $s$ denotes the number of bits comprising the subnet ID.

The _number of hosts_ is equal to $2^{32 - (s+n)} - 2$ where $s$ is the number of subnet ID bits and $n$ is the number of network ID bits. In other words, the number of hosts is equal to 2 to the power of the number of 0s in the subnet mask minus 2 or $2^h - 2$ where $h$ is the number of host ID bits. We need to subtract the 2 because the hosts ID of all zero's and all one's are reserved.

This is summarised in the following table:

![](<../../../../Networking/Protocols/Internet Protocol (IP)/Internet Protocol v4 (IPv4)/Resources/Images/Subnetting Summary.svg>)
