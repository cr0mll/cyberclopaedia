# Overview
Different web servers handle duplicating parameters in a variety of ways. An example of duplicate parameters would be:

```
https://www.bank.com/transfer?sender=abcdef&amount=1000&recipient=ghijkl&sender=ABCDEF
```

Here, there are two `sender=` parameters.
# Handling
- Apache - uses the last occurrence
- Apache Tomcat - uses the first occurrence
- ASP - uses all occurrences
- ISP - uses all occurrences

A more exhaustive list may be found at https://owasp.org/www-pdf-archive/AppsecEU09_CarettoniDiPaola_v0.8.pdf. 