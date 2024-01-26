# Introduction
A user in AD stores information about an employee or contractor who works for the organisation. These objects are instances of the [User class](https://learn.microsoft.com/en-us/windows/win32/adschema/c-user). User objects are leaf objects, since they do not contain any other objects.

Every user is considered a security principal and has its own SID and GUID. Additionally, user objects can have numerous different attributes such as display name, email address, last login time, etc - well in excess of 800.

# Domain Users
Domain Users in AD are the ones who are capable of accessing resources in the Active Directory environment. These users can log into any host on the network. All domain users have 5 essential naming attributes as well as many others:

|Attribute|Description|
|:-----:|:-----|
|`UserPrincipalName` (UPN)|The primary logon name for the user, which uses the user's email by convention.|
|`ObjectGUID`|A unique identifier for the user which is never changed even after removal of the user.|
|`SAMAccountName`|A logon name providing support for previous versions of Windows.|
|`objectSID`|The user's security identifier (SID) which identifies the user and their group memberships.|
|`sIDHistory`|A history of the user's SIDs which keeps track of the SIDs for the user when they migrate from one domain to another.|