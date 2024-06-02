# Groups

## Introduction

Groups are instances of the AD [Group](https://learn.microsoft.com/en-us/windows/win32/adschema/c-group) class. They provide the means to mass assign permissions to users, making administration a lot easier. The administrator assigns a set of privileges to the group and they will be inherited by any user who joins it.

Groups have two essential characteristics - type and scope.

![](<../../../../../System Internals/Windows/Active Directory (AD)/Resources/Images/Groups/Group Creation.png>)

### Group Type

The group type identifies the group's purpose and must be chosen upon creation of the group. There are two types of groups.

_Security groups_ are best suited precisely for the purpose described above - mass assignment of permissions to users.

_Distributions groups_ are a bit different - they are unable to assign any permissions and are really only used by email applications for the distribution of messages to their members. They resemble mailing lists and can be auto-filled in the recipient field when sending emails using Microsoft Outlook.

### Group Scope

There are three possible group scopes and once again must be selected upon creation of the group. The group scope determines the level of permissions that can be assigned via the group.

_Domain Local_ groups can only be used to manage permissions only regarding resources within the domain that the group belongs to. Whilst such groups cannot be used in other domains, they _can_ contain users from other domains. Additionally, nesting of domain local groups is allowed within other domain local groups but not within global ones.

_Global_ groups allow access to resources in a different domain from the one they belong to, although they may only contain users from their origin domain. Nesting of global groups is allowed both in other global groups and local groups.

_Universal_ groups allow permissions management across all domains within the same forest. They are stored in the Global Catalog and any change made directly to them triggers forest-wide replication. To avoid unnecessary replications, administrators are advised to keep users and computers in global groups which are themselves stored in universal groups.

It is also possible to change the scope of a group under certain conditions:

* A global group can be promoted to a universal group if it is not part of another global group.
* A domain local group can be promoted to a universal group if it does not contain any other domain local groups.
* A universal group can be demoted to a global group if it does not contain any other universal groups.
* A universal group can be freely demoted to a domain local group.

## Default Groups

Some built-in groups are automatically created when an AD environment is set up. These groups have specific purposes and _cannot_ contain other groups - only users.

|              Group Name              | Description                                                                                                                                                                                                                                                                                         |
| :----------------------------------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|          `Account Operators`         | Management of most account types with the exception of the Administrator account, administrative user accounts, or members of the Administrators, Server Operators, Account Operators, Backup Operators, or Print Operators groups. Additionally, members can log in locally to domain controllers. |
|           `Administrators`           | Full access to a computer or an entire domain provided that they are in this group on a domain controller.                                                                                                                                                                                          |
|          `Backup Operators`          | Ability to back up or restore all files on a computer, irrespective of the permissions set on it; ability to log on and shut down the computer; ability to log on domain controllers locally; ability to make shadow copies of SAM/NTDS databases.                                                  |
|              `DnsAdmins`             | Access to DNS network information. Only created if the DNS server role is installed at some point on a domain controller.                                                                                                                                                                           |
|            `Domain Admins`           | Full permissions to administer the domain; local administrators on every domain-joined machine.                                                                                                                                                                                                     |
|          `Domain Computers`          | Stores all computers which are not domain controllers.                                                                                                                                                                                                                                              |
|         `Domain Controllers`         | Stores all domain controllers in the domain.                                                                                                                                                                                                                                                        |
|            `Domain Guests`           | Includes the built-in Guest account.                                                                                                                                                                                                                                                                |
|            `Domain Users`            | Stores all users in the domain.                                                                                                                                                                                                                                                                     |
|          `Enterprise Admins`         | Complete configuration access within the domain; ability to make forest-wide changes such as creating child domains and trusts; only exists in root domains.                                                                                                                                        |
|          `Event Log Readers`         | Ability to read event logs on local computers.                                                                                                                                                                                                                                                      |
|     `Group Policy Creator Owners`    | Management of GPOs in the domain.                                                                                                                                                                                                                                                                   |
|       `Hyper-V Administrators`       | Complete access to all Hyper-V features.                                                                                                                                                                                                                                                            |
|              `IIS_IUSRS`             | Used by IIS.                                                                                                                                                                                                                                                                                        |
| `Pre–Windows 2000 Compatible Access` | Provides backwards-compatibility with Windows NT 4.0 or earlier.                                                                                                                                                                                                                                    |
|           `Print Operators`          | Printer management; ability to log on to DCs and load printer drivers.                                                                                                                                                                                                                              |
|           `Protected Users`          | Provides additional protection against attacks such as credential theft or Kerberoasting.                                                                                                                                                                                                           |
|    `Read-Only Domain Controllers`    | Contains all read-only DCs in the domain.                                                                                                                                                                                                                                                           |
|        `Remote Desktop Users`        | Ability to connect to a host via RDP.                                                                                                                                                                                                                                                               |
|       `Remote Management Users`      | Ability to connect to a host via WinRM.                                                                                                                                                                                                                                                             |
|            `Schema Admins`           | Ability to modify the AD schema.                                                                                                                                                                                                                                                                    |
|          `Server Operators`          | Ability to modify services, SMB shares and backup files on domain controllers.                                                                                                                                                                                                                      |
