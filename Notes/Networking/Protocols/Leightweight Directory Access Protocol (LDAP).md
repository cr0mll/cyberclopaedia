# Introduction
The Leightweight Directory Access Protocol (LDAP) is a protocol used to facilitate the communication with directory services such as OpenLDAP or [Active Directory](../../System%20Internals/Windows/Active%20Directory%20(AD)/index.md). These act as repositories for user information by storing credentials, users, groups, etc. Because of this, LDAP can also be used for the authentication and authorisation of users.

What makes LDAP easy to use is that it operates with its data in a plain text format called the LDAP Data Interchange Format (LDIF).

This protocol works on TCP port 389. Its secure variation (LDAPS) runs on TCP port 636 and establishes a TLS/SSL connection.

# Data Organisation
Information within LDAP has a hierarchical tree structure called the Directory Information Tree (DIT). This structure is flexible and there are no real restrictions to the way its levels are organised. The root of the tree is usually the domain which LDAP operates in. This domain is then split into domain components (dc) at each `.` character. From then on, you are more or less free to organise your DIT in any way you like.

![](Resources/Images/LDAP/LDAP%20Directory%20Information%20Tree.svg)

The LDAP DIT can be distributed across multiple directory servers which do not even need to be based in the same physical country.

## Entities
LDAP stores its data in the form of entities. These are instantiated from *objectClasses*, which are just templates for making the creation of entities easier.

An entity is comprised of *attributes*. These are key-value pairs with the possible "keys" (attribute names) being predefined by the objectClass that the entity is an instance of. Furthermore, the data stored in the attribute must match the data type defined for it in the objectClass.

Setting attributes is done by separating the name and value by a colon:

```
mail: jdoe@cyberclopaedia.com
```

When this attribute is later queried (but not set), an "equals" sign is used instead.
```
mail=jdoe@cyberclopaedia.com
```

An example user entity displayed in LDIF could be:

```
dn: sn=Doe,ou=users,ou=employees,dc=cyberclopaedia,dc=com
objectclass: person
sn: Doe
cn: John Doe
```

### Distinguished Name (DN) & Relative Distinguished Name (RDN)
The full path to an entity in LDAP is specified via a Distinguished Name (DN). A Relative Distinguished Name (RDN) is a single component of the DN that separates the entity from other entities at the current level in the naming hierarchy. RDNs are represented as attribute-value pairs in the form `attribute=value`, typically expressed in UTF-8. 

A DN is simply a comma-separated list of RDNs which hierarchically follows the path to the LDAP entry. For example, the DN for the John Doe user would be `dc=local,dc=company,dc=admin,ou=employees,ou=users,cn=jdoe`.

The following attribute names for RDNs are defined:

|LDAP Name|Meaning|
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
