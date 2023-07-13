# Introduction
The [Leightweight Directory Access Protocol (LDAP)](../../Networking/Protocols/Leightweight%20Directory%20Access%20Protocol%20(LDAP).md) is a protocol which facilitates the access and locating of resources within networks set up with directory services. It stores valuable data such as user information about the organisation in question and has functionality for user authentication and authorisation.

What makes LDAP especially easy to enumerate is the possible support of null credentials and the fact that even the most basic domain user credentials will suffice to enumerate a substantial portion of the domain.

LDAP runs on the default ports 389 and 636 (for LDAPS), while Global Catalog ([Active Directory](../../System%20Internals/Windows/Active%20Directory%20(AD)/index.md)'s instance of LDAP) is available on ports 3268 and 3269.

Tools which can be used to enumerate LDAP include [ldapsearch](https://docs.ldap.com/ldap-sdk/docs/tool-usages/ldapsearch.html) and [windapsearch](https://github.com/ropnop/go-windapsearch).

# Sniffing Clear Text Credentials
LDAP stores its data in a plain-text format which is human-readable. If the secure version of the protocol is not used (LDAP over SSL), then you can just sniff for credentials over the network. The simplest way to do this is to use [Wireshark](https://www.wireshark.org/) with the following filter:
```
ldap.authentication
```

![](Resources/Images/LDAP/Wireshark%20Sniffing.png)

# Credentials Validation
You should always first check if null credentials are valid:
```powershell
ldapsearch -x -H ldap://<IP> -D '' -w '' -b "DC=<DOMAIN>,DC=<TLD>"
```

![](Resources/Images/LDAP/Null%20Credentials%20Check.png)

If the response contains something about "bind must be completed", then null credentials are *not* valid.

A similar command can be used to check for the validity of a set of credentials:
```powershell
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "DC=<DOMAIN>,DC=<TLD>"
```

![](Resources/Images/LDAP/Credentials%20Validation.png)

# Enumerating the Database
`ldapsearch` is an exceptionally powerful tool because it allows you to use [filters](../../Networking/Protocols/Leightweight%20Directory%20Access%20Protocol%20(LDAP).md#ldap-filters) to find objects within LDAP by searching by their attributes. 

Extract **Users**:
```powershell
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b 'DC=<DOMAIN>,DC=<TLD>' '(&(objectClass=user)(!(objectClass=computer)))'
```

Extract **Computers**:
```powershell
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b 'DC=<DOMAIN>,DC=<TLD>' '(objectclass=computer)'
```