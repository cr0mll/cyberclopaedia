# Introduction
Windows uses the New Technology File System (NTFS) for managing its files and folders. What makes it special is its ability to automatically repair files and folders on disk using log files in case of a failure.

Additionally, it lifts certain limitations which were characteristic of its predecessors by supporting files larger than 4GB, being able to set permissions on specific files and folders and being able to avail itself of both compression and encryption. Another peculiar feature of NTFS are [Alternate Data Streams](#alternate-data-streams-ads).

# Permissions
NTFS allows for every user/group to have its own set of permissions on every file and folder in the file system tree. The following six types of permissions can be set:

|Permission|On Files|On Folders|
|:-----:|:----|:---|
|Read|View or access the file's contents.|View and list files and subfolders.|
|Write|Write to the file.|Add files or subfolders.|
|Read & Execute|View or access the file's contents as well as execute the file.|View and list files and subfolders as well as execute files. Inherited by both files and folders.|
|List Folder Contents|N/A|View and list files and subfolders as well as execute files. Inherited only by folders.|
|Modify|Read and write to the file, or delete it.|Read and write to files and subfolders, or delete the folder.|
|Full Control|Read, write, change or delete the file.|Read, write, change or delete files and subfolders.|

### Inspecting Permissions
Permissions can be inspected from the command line by running
```powershell
icacls <path>
```

![](Resources/Images/File%20System/icacls%20Inspect%20Permissions.png)

The last set of `()` for each user/group tell you the permissions:
- **F** - Full Control
- **M** - Modify
- **RX** - Read & Execute
- **R** - Read
- **W** - Write

Additionally, the permissions on a file/folder can be inspected by right-clicking on the item in Windows Explorer, following `Properties->Security` and then selecting the user/group you want to see the permissions for.

![](Resources/Images/File%20System/Inspect%20Folder%20Permissions.png)

# Alternate Data Streams (ADS)
A not very well-known, yet interesting feature of NTFS are the so-called Alternate Data Streams. These were implemented for better Macintosh file support, but they can lead to security vulnerabilities and ways to hide data.

A data stream can be thought of as a file within another file. Each stream has its own allocated disk space, size and file locks. Moreover, alternate data streams are invisible to Windows Explorer which makes them an easy way to hide data within legitimately looking files.

Every file in NTFS has at least one default data stream where its data is stored. The default data stream is innominate and any stream which *does* have a name is considered an alternate data stream.

### Working with ADSs
ADSs cannot be manipulated via Windows Explorer and so the command-line is needed. File operations with alternate data streams on the command-line work the same, but you will need to use the `<file name>:<stream name>` format to refer to the stream you want to manipulate.

For example, 
```
echo hello > file.txt
echo secret > file.txt:hidden
```

![](Resources/Images/File%20System/Oblivious%20Windows%20Explorer.png)

Windows Explorer is completely oblivious to the alternate data stream. The command-line, however, is not:

![](Resources/Images/File%20System/Read%20ADS.png)

Additionally, the `dir /R` command can be used to list alternate data streams for files in a directory:

![](Resources/Images/File%20System/Show%20ADSs.png)

A more sophisticated tool for managing ADSs, called [Streams](https://learn.microsoft.com/en-us/sysinternals/downloads/streams) comes with the [SysInternals](https://learn.microsoft.com/en-us/sysinternals/) suite. It can be used with the `-s` option to recursively show all streams for the files in a directory:

![](Resources/Images/File%20System/Streams%20Recurse%20Folders.png)

The number next to the stream name is the size of the data stored in the stream.

Streams can also be used to delete all streams from a file with the `-d` option:

![](Resources/Images/File%20System/Delete%20All%20Streams.png)
