# Deauth Attack

A deauthentication, or deauth, attack injects [deathentication frames](../../networking/protocols/wlan-ieee-802.11/index/authentication-frames.md#deauthentication-frame) in order to disconnect a target from a network. It works on pretty much any network and can be extremely useful in many other attacks in order to force a handshake, since most devices automatically try to connect to any networks in the area that they recognise. Moreover, a deauth attack can serve as a DOS attack, temporarily precluding a particular client from connecting to a network.

`aireplay-ng` can be to disconnect a device already connected to the network:

```
aireplay-ng --deauth <count> -a <access point> -c <client> -D <dev>
```

* `--deauth` specifies the amount of deauth frames to send. If this is 0, then `aireplay-ng` will produce a continuous stream of deauthentication packets, resulting in a DOS attack.
* `-a` is the MAC address (BSSID) of the network you want to attack.
* `-c` is the MAC address (BSSID) of the device you want to disconnect from the network. If this is not specified, `aireplay-ng` will disconnect all devices connected to the network.
* `-D` will ensure that the deauth packets are forcibly sent. The attack may not work if this option is not specified, since `aireplay-ng` will look for the target network in all channels and may not find it in time. This can be omitted if the wireless adapter is already locked on a specific channel by, for example, `airodump-ng` when listening to a particular network and channel.
* `<dev>` is the wireless adapter you wish to use for the attack.

![](<../../Hardware Hacking/Wireless Attacks/Resources/Images/WIFI\_aireplay\_deauth.png>)

If the target is not disconnected on the first try, you can always send more deauthentication frames!
