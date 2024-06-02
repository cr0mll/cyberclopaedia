# Relocations

## Introduction

During compilation, the compiler assumes that the PE file will be loaded at a certain base address, which is stored in `IMAGE_OPTIONAL_HEADER.ImageBase`. The compiler may take some addresses during compilation and make them absolute by hardcoding them based on the `ImageBase`. Unfortunately, the file is rarely loaded at its desired image base and so these addresses will be invalidated. Therefore, the linker needs to perform _relocations_ - it needs to fix those absolute addresses based on the actual image base.

## The Relocation Table

A list of these `ImageBase`-based addresses will be generated and stored in the _relocation table_. This is a Data Directory within the `.reloc` section and is divided into blocks, with each block representing the base relocations for a 4KB page and where each block must be aligned to a value of 32.

Each block begins with an `IMAGE_BASE_RELOCATION` structure and is followed by any number of _offset field entries_. This struct holds the RVA of the block as well as its size.

```cpp
typedef struct _IMAGE_BASE_RELOCATION {

    DWORD   VirtualAddress;
    DWORD   SizeOfBlock;
    
} IMAGE_BASE_RELOCATION;
typedef IMAGE_BASE_RELOCATION UNALIGNED * PIMAGE_BASE_RELOCATION;
```

An offset field entry is represented by a WORD, with the first 4 bits specifying the relocation type (which you can find on [Microsoft's documentation](https://docs.microsoft.com/en-us/windows/win32/debug/pe-format)) and the last 12 bits storing an offset from the `VirtualAddress` field of the corresponding relocation block.

The absolute address of the location that needs fixing then be obtained by adding the page RVA to the preferred image base and then adding the offset of the corresponding relocation (offset field) entry.

Relocations can also be inspected with PE-Bear:

![](<../../../Reverse Engineering/Binary Formats/PE/Resources/Images/PE\_Relocations.png>)
