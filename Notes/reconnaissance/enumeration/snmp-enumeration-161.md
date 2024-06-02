# SNMP Enumeration (161)

## Introduction

You will need working knowledge of [SNMP](../../networking/protocols/simple-network-management-protocol-snmp.md) in order to follow through.

## SNMP Enumeration using `snmp-check`

`snmp-check` is a simple utility for basic SNMP enumeration. You only need to provide it with the IP address to enumerate:

```
snmp-check [IP]
```

Furthermore, you have the following command-line options:

* `-p`: Change the port to enumerate. Default is 161.
* `-c`: Change the community string to use. Default is `public`
* `-v`: Change the SNMP version to use. Default is v1.

There are additional arguments that can be provided but these are the salient ones.

![](../../Reconnaissance/Enumeration/Resources/Images/SNMP\_snmp\_check.png)

## SNMP Enumeration using `snmpwalk`

`snmpwalk` is a much more versatile tool for SNMP enumeration. It's syntax is mostly the same as `snmp-check`:

![](../../Reconnaissance/Enumeration/Resources/Images/SNMP\_snmpwalk.png)

## Bruteforce community strings with `onesixtyone`

Notwithstanding its age, `onesixtyone` is a good tool which allows you to bruteforce community strings by specifying a file instead of a single string with its `-c` option. It's syntax is rather simple:

![](../../Reconnaissance/Enumeration/Resources/Images/SNMP\_onesixtyone\_syntax.png)

![](../../Reconnaissance/Enumeration/Resources/Images/SNMP\_onesixtyone\_bruteforce.png)
