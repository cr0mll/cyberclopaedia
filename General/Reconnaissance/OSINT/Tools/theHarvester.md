# What is theHarvester?
theHarvester is a powerful tool for gathering emails, names, subdomains, IPs, and URLs using a multitude of publicly available data sources. The tool is primarily a passive reconnaissance tool, however, it does employ some active reconnaissance, too. The active aspects are the DNS brute force and the screenshot it can take of any subdomains that were found. The GitHub page for theHarvester is located at https://github.com/laramies/theHarvester.

# Email and subdomain harvesting
All you need to get started is a domain name. You specify it with the `-d` argument. You need to provide a data source using the `-b` option. These are the sources you can choose from:

```baidu, bing, bingapi, dogpile, google, googleCSE, googleplus, google-profiles, linkedin, pgp, twitter, vhost, virustotal, threatcrowd, crtsh, netcraft, yahoo, all```

This is a simple theHarvester query:
```bash
theHarvester -d kali.org -b google
```

![](theHarvester-simple-results.png)

Additional options:
- `-l` - limit the number of results to work with
- `-s` - start in the specified result number
- `-h` - use SHODAN database to query discovered hosts