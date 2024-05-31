# Introduction
Since [ARP](index.md) is a dynamic resolution protocol, every address resolution requires the exchange of messages on the network. this consumes bandwidth and inhibits the overall performance of the network. Whilst ARP messages are not big, sending them too often will inevitably take its toll.

The solution to this is **caching**.

# The ARP Cache Table
Each device maintains its own **ARP Cache Table**, which is a simple table containing IP - MAC address pairs for every host the device is aware of. There are two types of entries in the ARP cache table:

- *Static Entries:* These entries are manually added to the ARP cache table, usually by an administrator, and remain there until they are manually removed.
- *Dynamic Entries:* These entries are added naturally whenever a successful address resolution occurs. They are only temporary and are automatically removed after a certain period of time.

Static entries are good for devices that are unlikely to change addresses. For example, a workstation might have a static ARP entry for its enterprise router and file server at the office. The main disadvantage of static entries is that they require manual intervention every time when there is a change in an IP or a MAC address.


