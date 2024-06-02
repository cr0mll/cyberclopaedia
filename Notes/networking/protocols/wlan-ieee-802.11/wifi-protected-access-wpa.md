# WiFi Protected Access (WPA)

WPA, WPA2, and WPA3 are consecutive versions of the most-widely used WiFi security standard today. All versions support two authentication modes:

* **Personal Mode** - this mode uses a pre-shared key (PSK) for authentication and is commonly referred to as WPA-PSK. This is typically utilised in home and small office networks. The PSK is derived from the WiFi network's password and its SSID, but is actually never sent over the air for security reasons. Instead, it is used for the derivation of other encryption keys.
* **Enterprise Mode** - this mode uses [802.1X authentication](authentication-and-association.md#the-extensible-authentication-protocol-eap) and supports all EAP methods. As the name implies, this authentication mode is typically used in larger enterprise networks.

WPA was developed after WEP was found to be vulnerable. Its encryption and MIC were provided by [TKIP](encryption-and-integrity.md#temporal-key-integrity-protocol-tkip).

It was superseded by WPA2 in 2004 which utilises [CCMP](encryption-and-integrity.md#counter-cbc-mac-protocol-ccmp) for encryption and MIC.

WPA3 is the successor to WPA2 introduced in 2018 and uses [GCMP](encryption-and-integrity.md#galois-counter-mode-protocol-gcmp). Furthermore, it now mandates _Protected Management Frames (PMF)_ to protect 802.11 [management frames](index/) from eavesdropping and forging. Moreover, the 4-way handshake in Personal Mode is protected by _Simultaneous Authentication of Equals (SAE)_ and forward secrecy is used to prevent save-now-decrypt-later attacks of frames.
