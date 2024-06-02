# Leightweight Directory Access Protocol (LDAP)

## Introduction

The Leightweight Directory Access Protocol (LDAP) is a protocol used to facilitate the communication with directory services such as OpenLDAP or [Active Directory](../../system-internals/windows/active-directory/). These act as repositories for user information by storing credentials, users, groups, etc. Because of this, LDAP can also be used for the authentication and authorisation of users.

What makes LDAP easy to use is that it operates with its data in a plain text format called the LDAP Data Interchange Format (LDIF).

This protocol works on TCP port 389. Its secure variation (LDAPS) runs on TCP port 636 and establishes a TLS/SSL connection.

## Data Organisation

Information within LDAP has a hierarchical tree structure called the Directory Information Tree (DIT). This structure is flexible and there are no real restrictions to the way its levels are organised. The root of the tree is usually the domain which LDAP operates in. This domain is then split into domain components (dc) at each `.` character. From then on, you are more or less free to organise your DIT in any way you like.

![](<../../Networking/Protocols/Resources/Images/LDAP/LDAP Directory Information Tree.svg>)

The LDAP DIT can be distributed across multiple directory servers which do not even need to be based in the same physical country.

### Entities

LDAP stores its data in the form of entities. These are instantiated from _objectClasses_, which are just templates for making the creation of entities easier.

An entity is comprised of _attributes_. These are key-value pairs with the possible "keys" (attribute names) being predefined by the objectClass that the entity is an instance of. Furthermore, the data stored in the attribute must match the data type defined for it in the objectClass.

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

#### Distinguished Name (DN) & Relative Distinguished Name (RDN)

The full path to an entity in LDAP is specified via a Distinguished Name (DN). A Relative Distinguished Name (RDN) is a single component of the DN that separates the entity from other entities at the current level in the naming hierarchy. RDNs are represented as attribute-value pairs in the form `attribute=value`, typically expressed in UTF-8.

A DN is simply a comma-separated list of RDNs which hierarchically follows the path to the LDAP entry. For example, the DN for the John Doe user would be `dc=local,dc=company,dc=admin,ou=employees,ou=users,cn=jdoe`.

The following attribute names for RDNs are defined:

| LDAP Name |         Meaning        |
| :-------: | :--------------------: |
|     DC    |     domainComponent    |
|     CN    |       commonName       |
|     OU    | organizationalUnitName |
|     O     |    organizationName    |
|   STREET  |      streetAddress     |
|     L     |      localityName      |
|     ST    |   stateOrProvinceName  |
|     C     |       countryName      |
|    UID    |         userid         |

It is also important to note that the following characters are special and need to be escaped by a `\` if they appear in the attribute value:

| Character |                Description                |
| :-------: | :---------------------------------------: |
|           | space or `#` at the beginning of a string |
|           |        space at the end of a string       |
|    `,`    |                   comma                   |
|    `+`    |                 plus sign                 |
|    `"`    |               double quotes               |
|    `\`    |                 backslash                 |
|    `/`    |               forwards slash              |
|    `<`    |             left angle bracket            |
|    `>`    |            right angle bracket            |
|    `;`    |                 semicolon                 |
|    `LF`   |                 line feed                 |
|    `CR`   |              carriage return              |
|    `=`    |                equals sign                |

## LDAP Filters

[Filters](https://ldap.com/ldap-filters/) are logically meaningful combinations of attribute-value pairs of the format which must be encapsulated in `()`. The value may be replaced by an asterisk (`*`) in order to match any objects which simply have that attribute, regardless of what its value is.

As already demonstrated, LDAP filters are represented as strings. Therefore, any characters that have special meaning in LDAP must be escaped if they are used as a literal part of an attribute name or value:

|                 Character                 | Escape Sequence |
| :---------------------------------------: | :-------------: |
|                    `(`                    |      `\28`      |
|                    `)`                    |      `\29`      |
|                    `*`                    |      `\2a`      |
|                    `\`                    |      `\5c`      |
| null character (must _always_ be escaped) |      `\00`      |

#### Presence Filters

The simplest possible filter is the presence filter which matches all objects that have a certain attribute regardless of its value. It has the format `(attribute=*)`. For example, the filter `(objectClass=*)` is often used to match all entries because any entry must have at least one objectClass.

#### Comparison Filters

These filters are a bit more complex and involve the comparison of the attribute's value with some desired value.

The simplest of these is an equality filter which checks if the attribute has a certain value. It has the format `(attribute=value)`. For example, the filter `(objectClass=user)` will return all objects which have an objectClass of User.

Greater-or-Equal and Less-or-Equal filters will match an object if it has at least one value for the specified attribute that is `>=` or `<=` to the provided value, respectively. They are constructed in the same way as equality filters but use `>=` or `<=` in lieu of the equal sign. The way the comparison is done depends on the data type. For example, attributes whose values are expected to be numbers will use numeric comparison, while strings will be compared lexicographically. For some attributes comparisons like this may not even make sense and thus these filters cannot be used with them. For example, it doesn't make sense to say that the colour blue is greater than red or vice versa.
