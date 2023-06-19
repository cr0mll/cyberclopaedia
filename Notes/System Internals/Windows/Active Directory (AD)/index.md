# Introduction
[Active Directory (AD)](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview) is a directory service for Windows network environments. It allows an organisation to store directory data and make it available to the users in a given network. AD has a distributed hierarchical structure that allows for the management of an organisation's resources such as users, computers, groups, network devices, file shares, group policies, servers, workstations and trusts. Furthermore, it provides authentication and authorization functionality to Windows domain environments. 

Essentially, AD is a large database of information which is accessible to all users within a domain, irrespective of their privilege level. This means that a standard user account can be used to enumerate a large portion of all AD components.

# Objects
Resources in Active Directory are represented by objects. An object is any resource present within Active Directory such as OUs, printers, users, domain controllers, etc. Every object has a set of characteristic attributes which describe it. For example, a computer object has attributes such as hostname and DNS name. Additionally, all AD attributes are associated with an LDAP name which can be used when performing LDAP queries.

Every object carries information in these attributes, some of which are mandatory and some optional. Objects can be instantiated with a predefined set of attributes from a *class* in order to make the process of object creation easier. For example, the computer object `PC1` will be an instance of the computer class in Active Directory.

It is common for objects to contain other objects, in which case they are called *containers*. An object holding no other objects is known as a *leaf*.

# Object Organisation
Objects are organised in logical groups called *domains*. These can further have nested subdomains in them and can either operate independently or be linked to other domains via trust relationships. A root domain together with all of its subdomains and nested objects is known as a *tree*. 

A collection of trees is referred to as a *forest* (really???). It is the root container for all objects in a given AD environment.

Following is an example forest with a single tree:

```
COMPANY.LOCAL/
├─ ADMIN.COMPANY.LOCAL
│  ├─ GPOs
│  ├─ OUs
│  │  ├─ EMPLOYEES
│  │  │  ├─ COMPUTERS
│  │  │  │  ├─ PC1
│  │  │  ├─ USERS
│  │  │  │  ├─ jdoe
│  │  │  ├─ GROUPS
│  │  │  │  ├─ STAFF
├─ DEV.COMPANY.LOCAL
├─ MAIL.COMPANY.LOCAL
```

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

It is also important to note that the following characters are special and need to be escaped by a `\` if the appear in the attribute value:

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

# Trusts
Trusts in Active Directory allow for forest-forest or domain-domain links. They allow users in one domain to access resources in another domain where their account does not reside. The way they work is by linking the authentication systems between two domains.

The two parties in a trust do not necessarily have the same capabilities with respect to each other:
- One-way trusts allow only one party to access the resources of the other. The trusted domain is considered the one *accessing* the resources and the trusting domain is the one providing them.
- Two-way trusts allow the parties to mutually access each other's resources.

Additionally, trusts can either be transitive or non-transitive. Transitivity means that the trust relationship is propagated upwards through a domain tree as it is formed. For example, a transitive two-way trust is established between a new domain and its parent domain upon creation. Any children of the new domain (grandchildren of the parent domain) will also then share a trust relationship with the master parent. 

Five possible types of trusts can be discerned depending on the relationships between the systems being linked:

|Trust|Description|
|:-----:|:-----:|
|Parent-child|A two-way transitive relationship between a parent and a child domain.|
|Cross-link|A trust between two child domains at the same hierarchical level, which is used to speed up authentication.|
|External|A non-transitive trust between two separate domains in separate forests which are not already linked by a forest trust.|
|Tree-root|A two-way transitive trust between a forest root domain and a new tree root domain.|
|Forest|A transitive trust between two forest root domains in separate forests.|