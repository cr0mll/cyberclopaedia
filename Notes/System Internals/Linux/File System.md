# Unified File System
Linux uses a unified file system which begins at the `/` directory (pronounced "root", notwithstanding this unfortunate naming). 

![](Resources/Images/File%20System/Linux%20File%20System.svg)

|Directory|Description|
|:--------:|:--------:|
|`/`|The anchor of the file system. Pronounced "root".|
|`/root`|The home directory of the `root` user.|
|`/home`|The home directories of non-root users are stored here.|
|`/usr`|All system files are stored here - the **U**nix **S**ystem **R**esource.|
|`/etc`|Stores configuration files.|
|`/var`|Stores variable data files such as logs, caches, etc.|
|`/opt`|Any additional software which is not built-in should be installed here.|
|`/tmp`|Temporary data storage. Its contents are erased at every boot or at a certain period.|
|`/proc`|Runtime process information.|

## Symbolic Links
A symbolic, or *soft*, link is a reference in the file system to a particular file. When the symbolic link is used in a command, the file which it references will be used instead.

![](Resources/Images/File%20System/Symbolic%20Links.png)

Symbolic links between files (or directories for that matter) can be created by using the following command:

```bash
ln -s <file> <link>
```

It is important to note that when using relative paths for the link, the path is relative to the link (even after it is moved) and not the current working directory.

![](Resources/Images/File%20System/Symbolic%20Link%20Relative%20Path.png)

Essentially, when creating a link with a relative path, the link points to `./file`. However, if the link is moved, then `./` will refer to a different directory and the link won't be able to find what it is referencing.

## Hard Links
Hard links are different from the symbolic links in the sense that they do *not* have any relationship to the original path where they link to, but only to its contents. They are just files which reference the same *data* as another file.

Hard links are created by using the following syntax:
```bash
ln <file> <link>
```

![](Resources/Images/File%20System/Hard%20Links.png)

Because hard links bear no connection to the path they were created with, they will still point to the same data even after they are relocated.

# Permissions
Every file and directory in Linux is owned by a certain user and a group and is assigned three sets of permissions - owner, group, and all users. The owner permissions describe what the user owning the file can do with it, the group permissions describe what members of the group owning the file can do with it, and the all users permissions describe what the rest of the non-root (root is allowed everything) users which are not members of the file's group can do with it.

![](Resources/Images/File%20System/File%20Permissions.png)

There are 3 possible type of permissions - read (`r`), write (`x`) and execute (`x`). Regarding the file shown here, the permissions are shown on the left and are represented by every 3 characters after the initial dash (`-`). So, here the file's owner (cr0mll) has `rwx` permissions on it. Every member of the `sysint` group will have `rw` permissions on the file and all other users will only be able to read it.

## Set Owner User ID (SUID)
The Set Owner User ID (SUID) is a special permission which can be set on executable files. When a file with SUID set is executed, it will always run with the effective UID of the user who owns it, irrespective of which user actually passed the command (so long as the user invoking the command also has execute permissions on the file).

The SUID permission is indicated by replacing the `x` in the permissions of the owning user with `s`.

![](Resources/Images/File%20System/SUID.png)

Setting SUID on a file can be done with the following command:
```bash
chmod u+s <file>
```

*Note that the SUID permission on scripts is ignored.*

## Set Group ID (SGID)
Similarly to SUID, the Set Group ID (SGID) is a special permission which can be set on both executable files *and* directories. When set on files, it behaves in the same way SUID but rather than the files executing with the privileges of the owning user, they execute with the effective GID the owning group.

When set on a directory, any file created within that directory will automatically have their group ownership set to one specified by the folder.

Setting SGID on a file can be done with the following command:
```bash
chmod g+s <path>
```

*Note that the SGID permission on scripts is ignored.*

## Sticky Bit
The sticky bit is a special permission which can be applied to directories in order to limit file deletion within them to the owners of the files. It is denoted by a `t` in the place of the `x` permission for the directory and can be set with the following command:

```bash
chmod +t <directory>
```