# Introduction
The Physical layer is the lowest layer in the OSI model. It provides the electrical, mechanical, or electromagnetic means by which data is physically transferred between hosts. At the core of the Physical layer lie interfaces and mediums. Interfaces are what allow devices to send receive data, while mediums are what the data travels through between interfaces. Data at the physical layer is transmitted in *bits*, not bytes, hence why internet speeds are typically measured in multiples of bits per seconds or bps.

# Mediums
## Copper (UTP) Cables
The following standards are defined for copper cable Ethernet:

|Speed|Common Name|IEEE Standard|Informal Name|Max Length|
|:-----:|:---------------:|:-------------:|:--------------:|:------------:|
| 10 Mbps| Ethernet | 802.3i | 10BASE-T| 100m |
| 100 Mbps| Fast Ethernet | 802.3u | 100BASE-T| 100m |
| 1 Gbps| Gigabit Ethernet | 802.3ab | 1000BASE-T| 100m |
| 10 Gbps| 10 Gig Ethernet | 802.3an | 10GBASE-T| 100m |

In the above nomenclature, `BASE` refers to baseband signaling, while `T` indicates *twisted pair*.

The copper cables described by the above standards are *Unshielded Twisted Pair* (UTP) cables which comprise 4 pairs of 8 wires.

![](https://upload.wikimedia.org/wikipedia/commons/c/cb/UTP_cable.jpg)

"Unshielded" means that the wires lack a metallic shield which increases their susceptibility to electrical interference. The "twisted pair" part is pretty self-explanatory and serves the purpose of reducing electromagnetic interference.

The RJ-45 jacks used for Ethernet have 8 pins - one pin per wire - however, not all pins are in use by all standards. 10BASE-T and 100BASE-T avail themselves only of pins 1, 2, 3, and 6. Moreover, different devices use these pins differently. Switches utilise pins 3 and 6 for *transmitting* (Tx) data and use pins 1 and 2 for *receiving* (Rx) data. This separation allows for *full-duplex* transmission - the device is able to both receive and send data at the same time. Most other devices, however, such as PCs, routers, and firewalls do the opposite - they use pins 3 and 6 for receiving and use pins 1 and 2 for sending data.

![](Resources/Images/UTP_10_100_BASE_T_straight_through.png)

The above is a diagram of a *straight-through cable*, since there is a one-to-one correspondence between the pins. This is a simple approach, but unfortunately only works when devices of opposite types are being connected - you can't use it to connect a router to another router, a switch to another switch, or a PC to another PC. This is where *crossover cables* come. In these cables, different pins on one end correspond to different pins on the other.

![](Resources/Images/UTP_10_100_BASE_T_crossover.png)

|Device Type|Tx Pins|Rx Pins|
|:-----------:|:-----:|:------:|
|Router|1 and 2|3 and 6|
|Firewall|1 and 2|3 and 6|
|PC|1 and 2|3 and 6|
|Switch|3 and 6|1 and 2|

Most modern devices, however, support a feature called Auto MDI-X. This allows them to detect which pins their neighbour is transmitting data on and automatically adjust their own use of Tx and Rx pins to allow for proper communication. This makes the use of different types of cables often obsolete.

Higher speed standards avail themselves of all the pins. Additionally, in 1000BASE-T and 10GBASE-T are bidirectional and allow for both transmission and reception which allows for greater speeds.

![](Resources/Images/UTP_1000_10GBASE_T.png)

## Fibre-Optic Cables
Fibre-Optic cables are a new generation of cables. Instead of transferring electrical signals through copper wiring, these cables conduct signals in the form of *light*, which makes them immune to EMI. In order to use fibre-optics, a special type of connector called SFP is required, which is short for *Small Form-Factor Pluggable* and looks like this:

![](https://upload.wikimedia.org/wikipedia/commons/0/0e/QSFP-40G-SR4_Transceiver.jpg)

Data is transferred through the fibre-optic cable which has two connections on each end - one for sending and one for receiving:

![](https://upload.wikimedia.org/wikipedia/commons/c/cb/Lc-sc-fiber-connectors.jpg)

The fibre-optic cable is comprised of 4 main layers. The innermost layer is the fibreglass core, which is what the light travels through. This core is enveloped in a cladding layer which reflects the light beam travelling through the cable. Around the cladding is a protective buffer, which is in turn wrapped in the outer jacket.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Singlemode_fibre_structure.svg/1024px-Singlemode_fibre_structure.svg.png)

There are two main types of fibre-optic cables in the wild. The first type is multi-mode fibre which allows for light to enter at multiple angles. It has a larger glass core and allows for a greater transmission distance than UTP and is also cheaper than single-mode fibre. Single-mode fibre, on the other hand allows for light to enter only at a single angle, called a *mode*, and has a much greater maximum distance than that of multi-mode (step index).

![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Optical_fiber_types.svg/1920px-Optical_fiber_types.svg.png)

The following fibre-optic cable standards are defined:

| Informal Name | IEEE Standard | Speed | Cable Type | Maximum Length |
|:-----------------:|:---------------:|:-------:|:------------:|:--------------------:|
| 1000BASE-LX | 802.3z | 1 Gbps | Multi- or single-mode | 550 m (MM), 5 km (SM) |
| 10GBASE-SR | 802.3ae | 10 Gbps | Multi-mode | 400 m |
| 10GBASE-LR | 802.3ae | 10 Gbps | Single-mode | 10 km |
| 10GBASE-ER | 802.3ae | 10 Gbps | Single-mode | 30 km |


