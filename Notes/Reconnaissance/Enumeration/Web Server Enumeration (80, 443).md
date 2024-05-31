# Web Server Enumeration (80, 443)

## Obtaining Version Information

Web servers usually run on port 80 or 443 depending on whether they run HTTP or HTTPS. Version information about the underlying web server application can be obtained via [nmap](<Port Scanning/index.md>) using the `-sV` option.

```bash
nmap -p80,443 -sV <target>
```

![](<Resources/Images/Web/Nmap Version Information.png>)

We can also use the `http-enum` NSE script which will perform some basic web server enumeration for us:

```bash
nmap -p80 --script=http-enum <target>
```

![](<Resources/Images/Web/http-enum Script.png>)

{% hint style="info" %}
Web servers are also commonly set up on custom ports, but one can enumerate those in the same way.
{% endhint %}

## Directory Brute Force

This is the first step one needs to take after discovering a web application. The goal is to identify all publicly-accessible routes on the server such as files, directories and API endpoints. In order to do so, we can use various tools such as [gobuster](https://github.com/OJ/gobuster) and [feroxbuster](https://github.com/epi052/feroxbuster).

The technique works by sampling common file and directory names from a wordlist and then querying the server with these routes. Depending on the response code the server returns, one can determine which routes are publicly-accessible, which ones require some sort of authentication and which ones simply do not exist on the server.

The basic syntax for `feroxbuster` is the following:

```bash
feroxbuster -u <target> -w <wordlist>
```

![](<Resources/Images/Web/Basic Directory Brute Force.png>)

The 200's (green) codes indicate a file or directory that is publicly accessible. The 300's (orange) code numbers represent a web page which redirects to another page. This may be because we are currently not authenticated as a user who can view said page. The 400's (red) codes represent errors. More specifically, 404 means that the web page does not exist on the server and 403 means that the page does exists, but we are not allowed to access it.

{% hint style="info" %}
[SecLists](https://github.com/danielmiessler/SecLists) is a large collection of wordlists whose contents range from commmon URLs and file names to usernames and passwords.
{% endhint %}

In contrast to other directory brute forcing tools, `feroxbuster` is recursive by default. If it finds a directory, it is going to begin brute forcing its contents as well. This is useful because it generates a comprehensive list of most, if not all, files and directories on the server. Nevertheless, this does usually take a lot of time. This behaviour can be disabled by using the `--no-recursion` flag.

`feroxbuster` also supports appending filename extensions by using the `-x <extension>` command-line argument. This can come in handy, for example, when one has discovered the primary language / framework used on the server (PHP, ASPX, etc.).
