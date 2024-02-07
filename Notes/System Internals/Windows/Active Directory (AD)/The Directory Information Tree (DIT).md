# The Directory Information Tree (DIT)
All data in a given Active Directory environment is stored in a database called the *Directory Information Tree (DIT)*. Every domain controller maintains a partial copy of this database containing all the relevant information for the domain the controller belongs to. 

By default, the database is stored by domain controllers in `C:\Windows\NTDS\ntds.dit` and it has three main tables.

## The Hidden Table
The hidden table contains only a single row with information used by Active Directory to configuration-related information in the data table. Most importantly, this table holds a pointer to the domain controller's NTDS Settings object in the data table.

## The Data Table
Most of the data in the AD environment is stored in the data table. Every attribute defined in the Schema is represented by a column and every object has a row dedicated to it. The values of the object's attributes are stored in the cells under the corresponding columns and if the object does not have a particular attribute, then that cell is left empty.

```admonish note
The large number of columns and the ability to add / remove new ones is one of the reasons why Microsoft does not use a classic relational database, since these are typically limited to a relatively small number of columns. 
```

In addition to a column for each attribute, the data table contains a few special columns. 

The first column is the *distinguished name tag (DNT)* which identifies each row (i.e. object) in the table. The DNT is *not* replicated which means that each object is likely to have a different DNT on different domain controllers. Furthermore, a domain controller is not allowed to reuse DNTs even after the object they refer to has been deleted. Since there can be at most $2^{31} - 255$ DNTs, a domain controller may eventually be unable to create new objects.

The *parent DNT (PDNT)* column stores the DNT of the object's direct parent. When the object is moved, its PDNT is automatically update to reflect its new parent.

The *NCDNT* column contains the DNT of the [naming contexts](Naming%20Contexts.md) the object belongs to, which illustrates that directory partitions are simply logical divisions and are not reflected "physically" (i.e. by creating separate folders for them or something similar).

The *Ancestors* columns stores the DNTs of the all of the object's ancestors (from the root down to the object itself) which essentially represents the hierarchy.

~~~admonish example title="Example: NTDS Database"

|DNT|PDNT|NCDNT|RDNType|RDN|Ancestors|Attr1|Attr2|$\cdots$|
|:-:|:--:|:---:|:-----:|:-:|:-------:|:---:|:---:|:------:|
|1337|2|N/A|`dc=`|`local`|{2,1337}|$\cdots$|$\cdots$|$\cdots$|
|1338|1337|2|`dc=`|`cybercorp`|{2,1337,1338}|$\cdots$|$\cdots$|$\cdots$|
|7899|1338|N/A|`cn=`|`Configuration`|{2,1337,1338, 7899}|$\cdots$|$\cdots$|$\cdots$|
|8946|7899|N/A|`cn=`|`Schema`|{2,1337,1338, 7899, 8946}|$\cdots$|$\cdots$|$\cdots$|
|2898|8946|8946|`cn=`|`SAM-Account-Name`|{2,1337,1338, 7899, 8946, 2898}|$\cdots$|$\cdots$|$\cdots$|
|1243|7899|7899|`cn=`|`Sites`|{2,1337,1338, 7899, 1243}|$\cdots$|$\cdots$|$\cdots$|
|5449|1338|1338|`cn=`|`Users`|{2,1337,1338, 5449}|$\cdots$|$\cdots$|$\cdots$|
|6345|1338|1338|`cn=`|`Computers`|{2,1337,1338, 6345}|$\cdots$|$\cdots$|$\cdots$|
|3333|6345|1338|`cn=`|`PC01`|{2,1337,1338, 6345, 3333}|$\cdots$|$\cdots$|$\cdots$|

~~~
