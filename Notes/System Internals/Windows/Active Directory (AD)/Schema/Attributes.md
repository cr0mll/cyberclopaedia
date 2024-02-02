# Attributes
Attributes represent the properties which Active Directory objects have. Similarly to [classes](Classes.md), they are represented by [attributeSchema](https://learn.microsoft.com/en-us/windows/win32/ad/characteristics-of-attributes) *objects* in the schema of the Active Directory environment. The properties of this object describe the characteristics of the attribute.

```admonish tip title="How-To: Modify an Attribute Definition in the AD Schema" collapsible=true
Modifying attribute definitions is done through the [Microsoft Management Console](index.md).
```

### Syntax
The *syntax* of an attribute specifies the kind of information that it can hold and is similar to data types in programming languages. There are 23 possible [syntaxes](https://learn.microsoft.com/en-us/windows/win32/adschema/syntaxes) which are specified by the combination of the `attributeSyntax` and `oMSyntax` properties of the attribute.

|Syntax|`attributeSyntax`|`oMSyntax`|Description|
|:--|:--:|:--:|--:|
|Boolean|2.5.5.8|1|A boolean value - either true or false.|
|String(Case Sensitive)|2.5.5.3|27|A case-sensitive ASCII string.|
|Integer|2.5.5.9|2|A 32-bit signed integer.|
|LargeInteger|2.5.5.16|65|A 64-bit signed integer.|
|Object(DS-DN)|2.5.5.1|127|A string containing a Distinguished Name.|
|String(Unicode)|2.5.5.12|64|A case-insensitive Unicode string.|
|String(Object-Identifier)|2.5.5.2|6|An OID string, i.e. a string containing digits 0-9 and decimal dots (`.`).|
|String(Octet)|2.5.5.10|4|A string representing an array of bytes.|
|String(Printable)|2.5.5.5|19|A case-sensitive string containing characters from the printable set.|
|String(Generalized-Time)|2.5.5.11|24|A string for storing time values in Generalized-Time format as defined by ASN.1.|
|String(UTC-Time)|2.5.5.11|13|A string for storing time values in UTC-Time format as defined by ASN.1.|

Most of these represent typical data types in programming languages. When unsure which syntax to use, take a look at already existing attributes to get an idea of which syntax might be appropriate.

### systemFlags
Each attribute definition in the Schema has a `systemFlags` property which describes how the attribute should be handled. It is a 32-bit big-endian field representing various flags as single-bit switches. Most of the bits are not used and should be left as zeros.

|Flag|Bit|Description|
|:--|:--:|--:|
|`FLAG_ATTR_NOT_REPLICATED` (NR)|31|The attribute will not be replicated.|
|`FLAG_ATTR_REQ_PARTIAL_SET_MEMBER` (PS)|30|The attribute is a member of a partial attribute set (PAS).|
|`FLAG_ATTR_IS_CONSTRUCTED` (CS)|29|The attribute is constructed. This flag should only be set by Microsoft.|
|`FLAG_ATTR_IS_OPERATIONAL` (OP)|28|The attribute is operational.|
|`FLAG_SCHEMA_BASE_OBJECT` (BS)|27|The attribute is part of the base (default) schema.|
|`FLAG_ATTR_IS_RDN` (RD)|26|The attribute can be used an RDN attribute.|

## Constructed Attributes
Certain attributes are *not* stored directly in the Active Directory database. The value of these *constructed attributes* is instead calculated whenever it is needed. This usually involves other attributes in the calculation. The functionality constructed attributes provide may range from telling you approximately how many objects are stored directly under a given container (`msDS-Approx-Immed-Subordinates`) to yielding information about attributes you have write access to on a given object (`allowedAttributesEffective`). 

Due to their special implementation, constructed attributes abide by certain rules:
- They are *not* replicated.
- They *cannot* be used in server-side sorting.
- They *cannot* be used for queries (with the exception of `aNR`).

The definition of a constructed attribute has the `FLAG_ATTR_IS_CONSTRUCTED` field in the `systemFlags` set to 1.

## Indexed Attributes
Attribute indexing is the process of storing the values of all instances of the attribute in a sorted table. This is done in order to boost query performance, since any queries involving the indexed attribute can be optimised by only looking through the table responsible for the specific attribute.

Unfortunately, it is not always possible to use indexing to speed up querying:
- Queries containing bitwise operations on the indexed attribute nullify the effect of indexing. These are queries which involving bit masks such as `systemFlags`.
- Queries containing the `NOT` operation on a bitwise attribute cannot avail themselves of indexing because negation necessitates the enumeration of all objects to determine which ones lack the attribute.

```admonish note
Indexing attributes comes with a disk space trade-off. Indexing an attribute which is present in a large number of objects may result in a significant disk consumption for the index's table.
```

~~~admonish tip title="How-To: Index an Attribute in Active Directory" collapsible=true
To specify that an attribute should be indexed, right-click on the attribute in the MMC and click `Properties`. In the properties, simply tick `Index this attribute`:

![](Resources/Images/Index%20Attribute.png)

~~~

Attribute indexing is reflected in the `searchFlags` property of the corresponding `attributeSchema` object:

|Flag|Bit|Description|
|:--|:--:|--:|
|`fATTINDEX` (IX)|31|Specifies an indexed attribute. All other index-based flags require this flag to be set.|
|`fPDNTATTINDEX` (PI)|30|Specifies Create an index for the attribute in each container.|
|`fTUPLEINDEX` (TP)|26|Specifies that a tuple index for medial searches (ones which contain wildcards *not* at the end of the value) should be created.|
|`fSUBTREEATTINDEX`(ST)|25|Specifies that subtree index for Virtual List View (VLV) searches should be created.|

## Linked Attributes
Attributes with an `attributeSyntax` of 2.5.5.1, 2.5.5.7, or 2.5.5.14 can be *linked* to attributes with an `attributeSyntax` of 2.5.5.1. Linked attributes come in pairs - one is called the *forward link* and the other is called the *back link*. Linking simply means that the value of the back link is calculated based on the value of the forward link.

A pair of linked attributes is identified by the `linkID` properties of the two `attributeSchema` objects representing the attribute definitions. The `linkID` of the forward link must be a unique even number and the `linkID` of its corresponding back link must be the forward link's `linkID` plus one.