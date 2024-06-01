# Naming Contexts

## Introduction

The distributed nature of Active Directory necessitates data segregation. These partitions which organise various data are called _Naming Contexts (NCs)_, also known as _directory partitions_. Active Directory comes with three types of predefined naming contexts:

* Domain Naming Context - for each domain in the forest;
* Configuration Naming Context - one per forest;
* Schema Naming Context - one per forest.

Additionally, administrators can define additional naming contexts for organising data by using _Application Partitions_.

<details>

<summary>How-To: View Naming Contexts</summary>

One can inspect the naming contexts accessible to a given domain controller by using LDP. Launch `ldp.exe` and from the toolbar navigate to `Connection -> Connect`. Type in the IP address of the domain controller you want to inspect and click `OK`.

<img src="../../../.gitbook/assets/LDP Connect.png" alt="" data-size="original">

This will produce a lot of information, so one needs to look out for the `namingContexts` attribute. The various naming contexts are given with their distinguished names and are separated by semicolons:

<img src="../../../.gitbook/assets/LDP Naming Contexts.png" alt="" data-size="original">

Alternatively, one can use PowerShell:

```powershell
Get-ADRootDSE -Server <IP> | Select-Object -ExpandProperty namingContexts
```

<img src="../../../.gitbook/assets/PowerShell Naming Contexts.png" alt="" data-size="original">

</details>

## Domain Naming Context

Every domain in an Active Directory environment has a _Domain Naming Context_ designed for storing data pertaining to that specific domain. The root of this directory partition is called the _NC head_ and is represented by the domain's distinguished name (in this case `dc=cybercorp,dc=com`). Every domain controller in the domain maintains a copy of the domain's naming context.

## Configuration Naming Context

The Configuration Naming Context stores configuration information about the entire forest and is located under the configuration container `cn=Configuration,dc=<forest root domain>,dc=<forest root domain extension>` (in the example case, `cn=Configuration,dc=cybercorp,dc=com`). The configuration partition is replicated to every domain controller inside the forest. Furthermore, writable domain controllers maintain a writable copy of it.

## Schema Naming Context

The Schema Naming Context contains the [Schema](Schema/index.md) of the Active Directory environment. Since there is a single schema for the entire forest, this partition is also replicated to every domain controller in the forest. It can be found under `cn=Schema,Configuration,dc=<forest root domain>,dc=<forest root domain extension>`.

{% hint style="info" %}
Although the Schema NC appears to be a child of the Configuration NC, they are actually completely separate, which can be seen in ADSI Edit.

<img src="../../../.gitbook/assets/Naming Context Segregation.png" alt="" data-size="original">
{% endhint %}

## Application Partitions

Application partitions allow administrators to create custom data storage areas on domain controllers of their choice, rather than entire domains or the forest. One can easily define which domain controllers should maintain a replica of a given application partition because Active Directory automatically sets up the replication after the domain controllers are chosen.

Naming application partitions is similar to naming domains - for example, `dc=apppartition,dc=cybercorp,dc=local`. Furthermore, the location of an application partition is rather flexible. They can be positioned under domains, under other application partitions or they can be the root of an entirely new domain tree.

There are, however, certain limitations to the objects that an application partition may contain. Application partitions cannot store security principals and the objects within cannot be relocated outside the partition. Moreover, objects in an application partition are not tracked by the Global Catalog.

<details>

<summary>How-To: Create or Delete Application Partition</summary>

One can create application partitions via `ntdsutil.exe`. Run the executable and type in `partition management`. Create an application partition with the following syntax:

```
create nc "<partition DN>" <domain controller>
```

<img src="../../../.gitbook/assets/Create Application Partition.png" alt="" data-size="original">

Contrastingly, deleting an application partition is done by deleting the `crossRef` object corresponding to the partition in the Configuration NC. Simply navigate to the `Partitions` container in the Configuration NC and delete the application partition's `crossRef` object.

<img src="../../../.gitbook/assets/Delete Application Partition.png" alt="" data-size="original">

</details>

<details>

<summary>How-To: Add Application Partitions Replicas</summary>

This is again done through `ntdsutil.exe`. Run the executable and type in `partition management`. You will need to first connect to the domain controller which you want to maintain a replica of the application partition. Type in `connections` and then use the following command:

```
connect to server <domain controller>
```

Type in `quit` to return to the partition management menu and use the following syntax to add the domain controller as a replica:

```
add nc replica "<partition DN>" <domain controller>
```

</details>
