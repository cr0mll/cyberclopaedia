# Introduction
A user in AD stores information about an employee or contractor who works for the organisation. These objects are instances of the [User class](https://learn.microsoft.com/en-us/windows/win32/adschema/c-user). User objects are leaf objects, since they do not contain any other objects.

Every user is considered a security principal and has its own SID and GUID. Additionally, user objects can have numerous different attributes such as display name, email address, last login time, etc - well in excess of 800.