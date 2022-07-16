# Introduction
The **Executable and Linkable Format** (ELF) has established itself as the standard binary format for Unix operating systems and their derivatives. Under LINUX, BSD variants, and other operating systems, ELF is used for executables, shared libraries, object files, core files, and even the kernel boot image. 

# Structure
An ELF file comprises an ELF header followed by data. Inside lie the Program Header Table and the Section Header Table. The former describes memory [segments](Segments.md), while the latter outlies the [sections](Sections.md). 

# File Types
An ELF file may be any of the following:
- `ET_NONE` - indicates an unknown file type which has not yet been defined.
- `ET_REL` - a relocatable file, also sometimes referred to as an object filed. Relocatable object files typically contain position independent code (PIC) that has not yet been linked into an executable and often have the extension `.o`.
- `ET_EXEC` - this is an executable file.
- `ET_DYN` - a shared object. This file can be dynamically linked and is also known as a shared library. Such files are loaded and linked into a process' image at runtime by the dynamic linker. Additionally, these `DYN` files can also serve as standalone executables.
- `ET_CORE` - a coredump file. These are full images of a process during a crash or when a `SIGSEGV` is returned. These files can be read by debuggers to aid in determining the cause of the crash