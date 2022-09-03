# Introduction
Before connecting to a wireless network, a client needs to be aware of its existence and parameters. This can either be achieved in two ways - passive and active scanning.

Passive scanning is when the client goes through all available channels in turn and listens for beacon frames from the APs in the area. The time spent on each channel is defined by the device's driver.

Active scanning is when the client sends probe requests to each channel in turn in order to discover what networks are available on it.

# Management Frame Fields & Information Elements
These are management frame fields and information elements specifically found in discovery management frames - beacon, probe request, and probe response.

## Frame Fields
### Timestamp
This is an 8-byte long field which contains the number of μs that the AP has been active. It is used in [beacon](Discovery%20Frames.md#beacon-frames) and [probe response](Discovery%20Frames.md#probe-response-frames) frames. Stations avail themselves of this field in order to synchronise their clocks using a Time Synchronising Function (TSF). Should the timestamp exceed its maximum value, it will simply be reset to 0 and the counter would continue, although that would take 580 000 years.

### Beacon Interval
This 2-byte field represents the interval, in time units (1 TU = 1 kμs = 1 024 μs), between target beacon transmission times (TBTTs). It defaults to 100 TU but small changes may be allowed by certain drivers. It is found in [beacon](Discovery%20Frames.md#beacon-frames) and [probe response](Discovery%20Frames.md#probe-response-frames) .

## Information Elements
### Extended Rate PHY (ERP) Element
This element is found only in beacon and probe response frames on 2.4 GHz networks which support 802.11g.

![](Resources/Images/ERP_MFIE.svg)

This field is essential to the operation of 802.11b/g/n networks.

The `Non-EPR Present` bit is set to 1 when either of the following criteria are met:
- A non-ERP station (legacy 802.11 or 802.11b) gets associated with the network.
- An adjoining network which only supports non-ERP data rates is detected, typically via a beacon frame from this BSS/IBSS.
- A management frame (except for probe requests) is received from an adjoining network which only supports non-ERP data rates.

The `UseProtection` bit is set to 1 as soon as a non-ERP client is associated with the network. It indicates the presence of a station lacking support for 802.11g and signals to ERP clients that the use of a protection mechanism (RTS/CTS or CTS to self) is necessitated before transmission. Within an IBSS, this behaviour is extended to any ERP station receiving a frame from a non-ERP one due to the lack of proper "association". This bit serves as a warning to other ERP stations to signal the presence of the non-ERP station and should spread to the other ERP stations (they should also set the `UseProtection` bit to 1 in their frames). It is common nowadays to witness the same procedure within a BSS, although it is not standard behaviour.

The `Barker Preamble Mode` bit is set to 0 to indicate, when using protection, that short preambles are permitted and is set to 1 when only long preambles should be utilised.  

## IBSS Parameter Set
This element is found in [beacon](Discovery%20Frames.md#beacon-frames) and [probe response](Discovery%20Frames.md#probe-response-frames) of stations within an IBSS. 

![](Resources/Images/IBSS_Parameter_Set.svg)

It contains the Announcement Traffic Indication Message (ATIM) window and indicates the time, in TUs, between ATIM frames in the IBSS.

# Beacon Frames
Beacon frames are used by APs (and stations in IBSS) in order to announce their presence to the surrounding area and to communicate the parameters of the network. Not only are these frames used by potential clients, but it they also serve the active clients in the network.

Beacon frames are broadcasted periodically at the so-called *target beacon transmission time (TBTT)*. The interval between beacon transmissions is defined in the AP MIB and defaults to 100 time units, or a little over 102 ms (1 TU = 1 kμs = 1 024 μs). However, the AP will need to delay the transmission if the network is busy.

Beacon frames are used by the stations in a network for time synchronisation. A timestamp as well as the expected transmission time of the next beacon are included in every beacon frame. The timestamp is utilised by each station in the so-called Timing Synchronisation Function (TSF).

![](Resources/Images/Beacon_Frame.svg)

Following is a table of the possible fields in a beacon frame (the order for optional fields may vary):

|Order|Name|Status|Description|
|:-----:|:------:|:-----:|------------|
|1|[Timestamp](index.md#timestamp)|Mandatory||
|2|[Beacon Interval](index.md#beacon-interval)|Mandatory||
|3|[Capability Information](index.md#capability-information)|Mandatory||
|4|[Service Set Identifier (SSID)](index.md#ssid)|Mandatory||
|5|[Supported Rates](index.md#supported-rates--extended-supported-rates)|Mandatory||
|6|Frequency-Hopping (FH) Parameter Set|Optional|Used by legacy FH stations.|
|7|[DS Parameter Set](index.md#direct-sequence-ds-parameter-set)|Optional|Present within beacon frames with stations with clause 15, 18, and 19 as their provenance.|
|8|CF Parameter Set|Optional|Used for PCF and not present in non-notional situations.|
|9|[IBSS Parameter Set](Discovery%20Frames.md#ibss-parameter-set)|Optional|Used within an IBSS (duh).|
|10|Traffic Indication Map (TIM)|Optional|Present only in beacons with an AP as their provenance.|
|11|[Country](index.md#country)|Optional||
|12|FH Parameters|Optional|Used with legacy FH stations.|
|13|FH Pattern Table|Optional|Used with legacy FH stations.|
|14|[Power Constraint](index.md#power-constraint)|Optional|Used with 802.11h.|
|15|[Channel Switch Announcement](index.md#channel-switch-announcement)|Optional|Used with 802.11h.|
|16|[Quiet](index.md#quiet)|Optional|Used with 802.11h.|
|17|[IBSS DSF](index.md#ibss-dsf)|Optional|Used with 802.11h in an IBSS.|
|18|[TPC Report](index.md#tpc-report)|Optional|Used with 802.11h.|
|19|[ERP Information](Discovery%20Frames.md#extended-rate-phy-erp-element)|Optional||
|20|[Extended Supported Rates](index.md#supported-rates--extended-supported-rates)|Optional|See Supported Rates.|
|21|[RSN](index.md#robust-security-network-rsn)|Optional||
|22|[BSS Load](index.md#bss-load)|Optional|Used with 802.11e QoS.|
|23|[EDCA Parameter](index.md#enhanced-distributed-channel-access-edca-parameter)|Optional|Used with 802.11e QoS when the QoS Capability element is missing.|
|24|[QoS Capability](index.md#qos-capability)|Optional|Used with 802.11e QoS when the EDCA Parameter element is missing.|
|25 - 32, 34 - 36|Vendor Specific|Optional||
|33|Mobility Domain|Optional|Used with 802.11r Fast BSS Transition.|
|37|HT Capabilities|Optional|Used with 802.11n.|
|38|HT Operation|Optional|Used with 802.11n.|
|39|20/40 BSS Coexistence|Optional|Used with 802.11n.|
|40|Overlapping BSS Scan Parameters|Optional||Used with 802.11n.|
|41|Extended Capabilities|Optional|See Capability Information.|

# Probe Request Frame
Probe request frames are employed by devices seeking to uncover what networks are present on a certain channel. They are typically sent to the broadcast address of `FF:FF:FF:FF:FF:FF` using the common CSMA/CA procedure. Once a probe request is sent, the sender station initiates a countdown, typically much shorter than the duration of a beacon interval. When the timer runs out, the device process the probe responses it received.

![](Resources/Images/Probe_Request_Frame.svg)

|Order|Name|Status|Description|
|:-----:|:------:|:-----:|------------|
|1|[Service Set Identifier (SSID)](index.md#ssid)|Mandatory||
|2|[Supported Rates](index.md#supported-rates--extended-supported-rates)|Mandatory||
|3|Request Information|Optional|See below.|
|4|[Extended Supported Rates](index.md#supported-rates--extended-supported-rates)|Optional|See Supported Rates.|
|5|Vendor-Specific|Optional|Used by the vendor as seen fit.|

The SSID of a particular network that the device is looking for may be set in the appropriate field. This way, only the devices bearing the desired SSID should response. Otherwise, the SSID element is still present but is empty. In this case, it signifies a wildcard probe and so all available networks should respond.

The rates supported by the device are sent together with the probe request so as to serve as a reference to the AP's response.

## Request Information Element
The `Request Information` element is optional and may be used to enquire about a particular information element of a network. 

![](Resources/Images/Request_Information_MFIE.svg)

It has an element ID of 10 and its component is a series of 1-byte integers indicating the element IDs of the desired elements. The network should in turn respond with these elements in the Probe Response.

### TPC Request
The Transmit Power Control (TPC) Request information element is a notional element used to request radio link management information. It has no associated data and is really only meant as placeholder for a part of a request information element.

![](Resources/Images/TPC_Request_MFIE.svg)

# Probe Response Frame
This is the type of frame which serves as a response to a Probe Request. It closely resembles a beacon frame, since they both answer the same more or less the same questions - they give information about the AP (or a station in IBSS) and the network. In fact, here are the differences:
- A beacon frame has a TIM field, whereas a probe response does not.
- A beacon frame may contain a QoS Information element, announcing basic QoS support.
- A probe response will also contain the elements requested in the probe request.

![](Resources/Images/Probe_Response_Frame.svg)

A probe response frame is sent as a unicast frame with the destination address being the MAC address of the station which issued a probe request. The probe response is transmitted at the lowest mutually supported rate by the AP and the soliciting station. Just like any unicast frame, a probe response should be acknowledged by the recipient station.

|Order|Name|Status|Description|
|:-----:|:------:|:-----:|------------|
|1|[Timestamp](index.md#timestamp)|Mandatory||
|2|[Beacon Interval](index.md#beacon-interval)|Mandatory||
|3|[Capability Information](index.md#capability-information)|Mandatory||
|4|[Service Set Identifier (SSID)](index.md#ssid)|Mandatory||
|5|[Supported Rates](index.md#supported-rates--extended-supported-rates)|Mandatory||
|6|Frequency-Hopping (FH) Parameter Set|Optional|Used by legacy FH stations.|
|7|[DS Parameter Set](index.md#direct-sequence-ds-parameter-set)|Optional|Present within beacon frames with stations with clause 15, 18, and 19 as their provenance.|
|8|CF Parameter Set|Optional|Used for PCF and not present in non-notional situations.|
|9|[IBSS Parameter Set](Discovery%20Frames.md#ibss-parameter-set)|Optional|Used within an IBSS (duh).|
|10|[Country](index.md#country)|Optional|Used with 802.11d and used with 802.11h.|
|11|FH Parameters|Optional|Used with legacy FH stations.|
|12|FH Pattern Table|Optional|Used with legacy FH stations.|
|13|[Power Constraint](index.md#power-constraint)|Optional|Used with 802.11h.|
|14|[Channel Switch Announcement](index.md#channel-switch-announcement)|Optional|Used with 802.11h.|
|15|[Quiet](index.md#quiet)|Optional|Used with 802.11h.|
|16|[IBSS DSF](index.md#ibss-dsf)|Optional|Used with 802.11h in an IBSS.|
|17|[TPC Report](index.md#tpc-report)|Optional|Used with 802.11h.|
|18|[ERP Information](Discovery%20Frames.md#extended-rate-phy-erp-element)|Optional||
|19|[Extended Supported Rates](index.md#supported-rates--extended-supported-rates)|Optional|See Supported Rates.|
|20|[RSN](index.md#robust-security-network-rsn)|Optional||
|21|[BSS Load](index.md#bss-load)|Optional|Used with 802.11e QoS.|
|22|[EDCA Parameter](index.md#enhanced-distributed-channel-access-edca-parameter)|Optional|Used with 802.11e QoS when the QoS capability element is missing.|
|23|Measurement Pilot Transmission Information|Optional|Used with 802.11k.|
|24|Multiple BSSID|Optional|Used with 802.11k.|
|25|RRM Enabled Capabilities|Optional|Used with 802.11k.|
|26|AP Channel Report|Optional|Used with 802.11k.|
|27|BSS Average Access Delay|Optional|Used with 802.11k.|
|28 - 30|Reserved| - ||
|31|Mobility Domain|Optional|Used with 802.11r.|
|32|DSE Registered Location|Optional|Used with 802.11w.|
|33|Extended Channel Switch Announcement|Optional|Used with 802.11y.|
|34|Supported Regulatory Classes|Optional|Used with 802.11y.|
|35|HT Capabilities|Optional|Used with 802.11n.|
|36|HT Operation|Optional|Used with 802.11n.|
|37|20/40 BSS Coexistence|Optional|Used with 802.11n.|
|38|Overlapping BSS Scan Parameters|Optional||Used with 802.11n.|
|39|Extended Capabilities|Optional|See Capability Information.|
|40 - n|Requested Information Elements|Optional|The information elements requested in the Probe Request.|
|Last|Vendor-Specific|Optional|Follows all other elements.|