# Introduction
Domain Controllers (DCs) are at the heart of Active Directory. There are Flexible Single Master Operation (FSMO) roles which can be assigned separately to domain controllers in order to avoid conflicts when data is update in the AD environment. These roles are the following:

|Role|Description|
|:----:|:----|
|Schema Master|Management of the AD schema.|
|Domain Naming Master|Management of domain names - ensures that no two domains in the same forest share the same name.|
|Relative ID (RID) Master|Assignment of RIDs to other DCs within the domain, which helps to ensure that no two objects share the same SID.|
|PDC Emulator|The authoritative DC in the domain - responds to authentication requests, password changes, and manages Group Policy Objects (GPOs). Additionally, it keeps track of time within the domain.|
|Infrastructure Master|Translation of GUIDs, SIDs, and DNs between domains in the same forest.|