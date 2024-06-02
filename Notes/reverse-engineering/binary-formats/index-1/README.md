# PE

## Introduction

PE is short for _Portable Executable_ and it describes the structure of image and object files under the Windows family of operating systems. It is the successor of COFF files and encompasses a wide range of formats, including executables (`.exe`), dynamic-link libraries (`.dll`), kernel modules (`.srv`), and control panel applications (`.cpl`).

A very good programme for analysing PE files is [PE-Bear](https://hshrzd.wordpress.com/pe-bear/).

## Structure

The structure of a typical PE file looks like the following:

![](<../../../Reverse Engineering/Binary Formats/PE/Resources/Images/PE\_Structure.png>)

The file begins with a DOS header which marks it as an MS-DOS executable. Next follows the DOS stub, which is a simple programme which gets executed if the PE file is run in DOS mode and typically prints an error message. Following are the three NT headers - the PE 4-byte PE signature, the standard COFF file header, and the Optional header. Furthermore, it is possible that between the DOS Stub and the NT headers there is a space called the Rich Header. After the NT headers follows the Section Table which contains a section header for each section. At the end are the sections themselves which contain the actual contents of the file.
