# Introduction
A contact in AD contains information about an external person or company that may need to be contacted on a regular basis. Contact objects are instances of the [Contact class](https://learn.microsoft.com/en-us/windows/win32/adschema/c-contact) and are considered leaf objects. Their attributes include first name, last name, email address, telephone number, etc.

Contacts are not security principals - they lack a SID and only have a GUID.