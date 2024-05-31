# Subdomain Enumeration

## Introduction

Subdomain enumeration is an essential step in the reconnaissance stage as any found subdomains increase the potential attack surface. Open-Source Intelligence techniques can be used to find subdomains for a given domain without interacting with the target in the slightest.

### Subdomain Enumeration with Sublist3r

The first tool one usually hears about in regards to passive subdomain enumeration is [Sublist3r](https://github.com/aboul3la/Sublist3r). It is pre-installed on Kali Linux but one can easily install it on other systems by following the instructions on the GitHub repository. Its syntax is straight-forward:

```bash
sublist3r -d <domain> -o <output file>
```

![](<Resources/Images/Subdomain Enumeration/Sublist3r Example.png>)

Sublist3r will use various search engines to find and extract subdomains for the specified domain. Unfortunately, the tool was last updated in 2020 and so it does not perform as well as one would expect today.

### Subdomain Enumeration with Amass

[OWASP Amass](https://github.com/owasp-amass/amass) is currently broken, so we are waiting for a fix before writing this section.

## Finding Live Domains

The above enumeration techniques find subdomain candidates by crawling the Internet and examining thousands of web pages. This means that not all found subdomains will be valid or "live" - some subdomains may have been long taken down or they may have been moved to another place. Therefore, one needs to filter through the list of potential subdomains and see which ones are still accessible.

A great tool to do this is [httprobe](https://github.com/tomnomnom/httprobe). To use it, you will need to install the Go language and then the tool itself:

```bash
sudo apt install golang-go;
go install github.com/tomnomnom/httprobe@latest
```

Its usage is fairly simple. You just need to pipe the file containing the potential subdomains into `httprobe`:

```bash
cat potential_subdomains.txt | httprobe
```

![](<Resources/Images/Subdomain Enumeration/httprobe Example.png>)

The tool will try to visit every subdomain in the list and will only return the subdomains which respond back. By default, it checks ports 80 and 443 for HTTP and HTTPS, respectively, but this behaviour can be overriden by providing `-p <protocol>:<port>` flags.

{% hint style="info" %}
This step of the reconnaissance stage is technically _not_ passive because you have to visit the domains in order to determine if they are active or not.
{% endhint %}
