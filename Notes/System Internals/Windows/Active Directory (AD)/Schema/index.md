# Schema

The schema in an Active Directory environment provides the blueprints for all of the classes and attributes. A forest has a single instance of the schema which is located in the Schema [naming context](<../Naming Contexts.md#schema-naming-context>), under the forest root domain at `cn=schema,cn=Configuration,dc=rootdomain,dc=rootdomainextension`.

Each class in the Active Directory environment is represented by an object of the `classSchema` class and each attribute is defined by an object of the `attributeSchema` class. These objects are then stored in the schema.

{% hint style="info" %}
Class and attribute definitions are themselves objects stored in the AD schema.
{% endhint %}

<figure><img src="../../../../.gitbook/assets/AD Schema .svg" alt=""><figcaption></figcaption></figure>

Every AD environment comes with a default schema containing various pre-defined classes and attributes and administrators are free to add custom ones.

<details>

<summary>Modifying the AD Schema</summary>

Modifying the AD Schema can be graphically done with the Microsoft Management Console (MMC). Press `Win + R` and type in `mmc`.

<img src="../../../../.gitbook/assets/Launch MMC.png" alt="" data-size="original">

Next, add the `Schema` snap-in by clicking on `File -> Add/Remove Snap-in` and selecting `Active Directory Schema`.

<img src="../../../../.gitbook/assets/Add Schema Snap-In MMC.png" alt="" data-size="original">

</details>

{% hint style="info" %}
Only the domain controller which holds the Schema Master FSMO role can make changes to the AD environment's Schema.

There is only one Schema Master allowed per _forest_.
{% endhint %}

### Versioning

Microsoft regularly updates the default schema with new server OS releases and expands the available default classes and attributes.

| OS Release                      | Schema Version |
| ------------------------------- | :------------: |
| Windows 2000                    |       13       |
| Windows Server 2003             |       30       |
| Windows Server 2003 R2          |       31       |
| Windows Server 2008 Beta Schema |       39       |
| Windows Server 2008             |       44       |
| Windows Server 2008 R2          |       47       |
| Windows Server 2012             |       56       |
| Windows Server 2012 R2          |       69       |
| Windows Server 2016             |       87       |
| Windows Server 2019             |       88       |
| Windows Server 2022             |       88       |

One can check the version of the currently used schema with ADSI Edit. Open ADSI Edit, click on `Action -> Connect To...`. Click on `Select a well known Naming Context` and choose the `Schema` [naming context](<../Naming Contexts.md>).

![](<Resources/Images/ADSI Edit Schema NC.png>)

Next, right-click on the `Schema` field with the server icon and select properties. The schema version is contained in the `objectVersion` attribute:

![](<Resources/Images/ADSI Edit Schema Version.png>)

Alternatively, one can use the following PowerShell code:

```powershell
Get-ItemProperty 'AD:\CN=Schema,CN=Configuration,DC=<rootdomain>,DC=<rootdomainextension>' -Name objectVersion
```

![](<Resources/Images/Schema Version PowerShell.png>)

{% hint style="info" %}
You will have to run the Active Directory module for PowerShell, otherwise you will not be able to access the `AD:` drive.
{% endhint %}
