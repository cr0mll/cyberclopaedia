# Introduction
[Active Directory (AD)](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview) is a directory service for Windows network environments. It allows an organisation to store directory data and make it available to the users in a given network. AD has a distributed hierarchical structure that allows for the management of an organisation's resources such as users, computers, groups, network devices, file shares, group policies, servers, workstations and trusts. Furthermore, it provides authentication and authorization functionality to Windows domain environments. 

Essentially, AD is a large database of information which is accessible to all users within a domain, irrespective of their privilege level. This means that a standard user account can be used to enumerate a large portion of all AD components.

# Object Organisation

## Distinguished Name (DN) & Relative Distinguished Name (RDN)
The full path to an object in AD is specified via a [Distinguished Name (DN)](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/ldap/distinguished-names). A [Relative Distinguished Name (RDN)](https://docs.microsoft.com/en-us/windows/win32/ad/object-names-and-identities) is a single component of the DN that separates the object from other objects at the current level in the naming hierarchy. RDNs are represented as attribute-value pairs in the form `attribute=value`, typically expressed in UTF-8. 

A DN is simply a comma-separated list of RDNs which begins with the top-most hierarchical layer and becomes more specific as you go to the right. For example, the DN for the John Doe user would be `dc=local,dc=company,dc=admin,ou=employees,ou=users,cn=jdoe`.

The following attribute names for RDNs are defined:

|LDAP Name|Attribute|
|:---:|:---:|
|DC|domainComponent|
|CN|commonName|
|OU|organizationalUnitName|
|O|organizationName|
|STREET|streetAddress|
|L|localityName|
|ST|stateOrProvinceName|
|C|countryName|
|UID|userid|

It is also important to note that the following characters are special and need to be escaped by a `\` if they appear in the attribute value:

|Character|Description|
|:---:|:---:|
||space or `#` at the beginning of a string|
||space at the end of a string|
|`,`|comma|
|`+`|plus sign|
|`"`|double quotes|
|`\`|backslash|
|`/`|forwards slash|
|`<`|left angle bracket|
|`>`|right angle bracket|
|`;`|semicolon|
|`LF`|line feed|
|`CR`|carriage return|
|`=`|equals sign|

