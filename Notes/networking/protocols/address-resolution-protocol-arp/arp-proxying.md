# Introduction
Sometimes, two devices, X and Y, might be configured on the same subnet, but be separated physically by a router. ARP is not designed to function in situations like these, since it relies on broadcasting. Routers do not forward broadcasts across networks, so a broadcasted ARP request from device X will never reach device Y and vice-versa.

# ARP Proxying
The solution in such cases is to proxy the ARP protocol. When the router receives an ARP broadcast from device X, it will send an ARP response with its own MAC address. Device X will, therefore, believe the router to be device Y and send any traffic for device Y to the router. The router will in turn forward the datagrams to device Y on the other network and vice versa.

The main advantage of proxying is that it is transparent to the two devices - neither device X nor device Y is ever aware of the fact that they are on physically separate networks. However, proxying introduces additional complexity and unexpected problems may rise if two or more routers, instead of one, provide the link between the two physical networks.