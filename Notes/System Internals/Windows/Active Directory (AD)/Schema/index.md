# The Active Directory Schema
The schema in an Active Directory environment provides the blueprints for all of the classes and attributes. A forest has a single instance of the schema which is located in the Schema [naming context](../Naming%20Contexts.md#schema-naming-context), under the forest root domain at `cn=schema,cn=Configuration,dc=rootdomain,dc=rootdomainextension`. 

Each class in the Active Directory environment is represented by an object of the `classSchema` class and each attribute is defined by an object of the `attributeSchema` class. These objects are then stored in the schema. 

```admonish info title="Important: Class and Attribute Definitions as Objects"
Class and attribute definitions are themselves objects stored in the AD schema.

![](Resources/Images/AD%20Schema%20.svg)

```
 
Every AD environment comes with a default schema containing various pre-defined classes and attributes and administrators are free to add custom ones. 

~~~admonish tip title="How-To: Modify the Active Directory Schema" collapsible=true
Modifying the AD Schema can be graphically done with the Microsoft Management Console (MMC). Press `Win + R` and type in `mmc`.

![](Resources/Images/Launc%20MMC.png)

Next, add the `Schema` snap-in by clicking on `File -> Add/Remove Snap-in` and selecting `Active Directory Schema`.

![](Resources/Images/Add%20Schema%20Snap-In%20MMC.png)
~~~

~~~admonish note title="Info: Schema Master FSMO Role"
Only the domain controller which holds the Schema Master FSMO role can make changes to the AD environment's Schema.

There is only one Schema Master allowed per *forest*.
~~~

### Versioning
Microsoft regularly updates the default schema with new server OS releases and expands the available default classes and attributes.

|OS Release|Schema Version|
|:--|:--:|
|Windows 2000|13|
|Windows Server 2003|30|
|Windows Server 2003 R2|31|
|Windows Server 2008 Beta Schema|39|
|Windows Server 2008|44|
|Windows Server 2008 R2|47|
|Windows Server 2012|56|
|Windows Server 2012 R2|69|
|Windows Server 2016|87|
|Windows Server 2019|88|
|Windows Server 2022|88|

One can check the version of the currently used schema with ADSI Edit. Open ADSI Edit, click on `Action -> Connect To...`. Click on `Select a well known Naming Context` and choose the `Schema` [naming context](../Naming%20Contexts.md).

![](Resources/Images/ADSI%20Edit%20Schema%20NC.png)

Next, right-click on the `Schema` field with the server icon and select properties. The schema version is contained in the `objectVersion` attribute:

![](Resources/Images/ADSI%20Edit%20Schema%20Version.png)

Alternatively, one can use the following PowerShell code:

```powershell
Get-ItemProperty 'AD:\CN=Schema,CN=Configuration,DC=<rootdomain>,DC=<rootdomainextension>' -Name objectVersion
```

![](Resources/Images/Schema%20Version%20PowerShell.png)

~~~admonish note
You will have to run the Active Directory module for PowerShell, otherwise you will not be able to access the `AD:` drive.

![](Resources/Images/Active%20Directory%20Module%20for%20PowerShell.png)
~~~

