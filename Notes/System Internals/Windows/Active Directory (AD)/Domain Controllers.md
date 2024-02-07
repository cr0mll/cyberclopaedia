# Domain Controller
A *domain controller* in Active Directory is a Windows Server which hosts all services and protocols within a given domain. Each domain controller may only service a single domain but roles within the *same* domain are usually distributed across a few different domain controllers.

## Flexible Single-Master Operation (FSMO) Roles
Although Active Directory follows a multi-master model, some functions and services are still best managed by a single domain controller in order to avoid unnecessary complexity. These functions are grouped together into *Flexible Single-Master Operation (FSMO, pronounced "fizmo")* roles which are then assigned to specific domain controllers. There are five such roles:

|FSMO Role|Holders|
|:--:|:--:|
|Schema Master|One domain controller per forest.|
|Domain Naming Master|One domain controller per forest.|
|Infrastructure Master|One domain controller per domain.|
|RID Master|One domain controller per domain.|
|PDC Emulator Master|One domain controller per domain.|

By default, all of the FSMO roles are assigned to the first domain controller in the forest and they can be subsequently transferred to other servers.

### Schema Master
There is only one Schema Master domain controller in a forest and it is the sole controller which is allowed to make changes to the Active Directory [Schema](Schema/index.md). If there is no domain controller with this role, then it is not possible to make changes to the schema.

One can view who the Schema Master is with the following PowerShell command:

```powershell
Get-ADForest | Select SchemaMaster
```

![](Resources/Images/Domain%20Controllers/View%20Schema%20Master.png)

```admonish note
If there is no domain controller with the Schema Master role, then it will not be possible to make changes to the AD schema.
```

### Domain Naming Master
As with the Schema Master, there is a single Domain Naming Master for the entire forest and it is the domain controller responsible for add and removing domains to and from the forest. The Domain Naming Master is the only DC allowed to add or remove domains and 
[application partitions](Naming%20Contexts.md#).

One can view the Domain Naming Master with the following PowerShell command:

```powershell
Get-ADForest | Select DomainNamingMaster
```

![](Resources/Images/Domain%20Controllers/View%20Domain%20Naming%20Master.png)

```admonish note
If there is no domain controller with the Domain Naming Master role, then it will not be possible to add or remove domains to and from the forest.
```

### Infrastructure Master
