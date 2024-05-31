# Whois Enumeration

## Introduction

_Whois_ is a service which can provide information about domain names. Domains are given out by registrars, and information about them is usually public because registrars charge extra for private registration.

In order to function, `whois` needs two things - a domain name to look up and a whois server. The `whois` server is a database which is periodically updated with information from various registrars about the domains associated with them.

## Whois Look-up

The command itself is very simple.

```bash
whois <domain name>
```

![](<Resources/Images/whois lookup.png>)

As we can see, `whois` yielded information about the domain name's registrar, the time of creation, the time of the last update and much more. In fact, `example.com` uses private registration so this information is actually not that much. When the domain is publicly registered, a `whois` look-up can provide information such as the phone number, email address, ISP and country of residence of the person / organisation that owns the domain, additional domains owned by the same organisation as well as email servers.

It is also possible to specify a custom `whois` server with the `-h` flag.

```bash
whois <domain name> -h <whois server>
```

## Reverse Whois Lookup

`whois` is also capable of obtaining information from an IP address.

```bash
whois <ip>
```

![](<Resources/Images/Reverse Whois Lookup.png>)

This is the result from the reverse `whois` lookup for the IP address of `example.com`. The reverse lookup provides us with information about who is hosting the IP. This time it yielded a person's name, an address and a phone number. Looking these up on Google, we see that they are actually associated with a physical office of `edg.io`.

{% hint style="info" %}
One should ways do both a normal as well as a reverse whois lookup because on might reveal information that the other does not.
{% endhint %}
