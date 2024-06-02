# Operation Security (OpSec)

One way to avoid detection when port scanning is to flood the logs with fake scans. Whilst your IP will still be present in them, so will a bunch of other random IP addresses, thus making it difficult to pinpoint you as the source of the port scan.

This can be done by using the `-D RND:<number>` flag with Nmap, where `<number>` is the number of fake IPs you want Nmap to generate. When you run the scan, Nmap will duplicate all packets it sends and it will spoof their IPs to random ones:

![](<../../../Reconnaissance/Enumeration/Port Scanning/Resources/Images/Decoy Scan.png>)

As we can see, Nmap generated a bunch of fake packets by spoofing multiple source IPs in order to make it difficult to figure out the actual source of the scan.

{% hint style="warning" %}
This type of scan generates a lot of traffic to the target host!
{% endhint %}
