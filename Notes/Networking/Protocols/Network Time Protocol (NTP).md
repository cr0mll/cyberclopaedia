# Introduction
The **N**etwork **T**ime **P**rotocol (NTP) is a protocol for clock synchronisation across computer systems. Its existence is paramount in order to pinpoint events occurring at a certain moment within a network. Devices with unsynchronised clocks will report that the event transpired at different times thus making it very difficult to figure out the actual time of occurrence.

This protocol works over UDP on port 123.
# How does NTP work?
NTP utilises a hierarchy system. Each clock is assigned a *stratum*. Stratum values range between 0 and 15, with a value of 16 denoting an unsynchronised clock. Devices of Stratum 0 are called reference clocks and these are one of the most accurate time-keeping machines such as atomic clocks. The stratum value, therefore, represents the distance from the reference clock or how accurate a given clock is in comparison to a device of Stratum 0. Every new layer adds a 1 to the stratum value.

Reference clocks are not directly connected to the network. Instead, the so-called *primary time servers* connect to the reference clock and synchronise their clocks with it. These servers have a stratum value of 1. For each layer you go down the chain, the stratum value increases by 1, since the distance from the reference clocks augments.

![](Resources/Images/NTP_Hierarchy.png)

