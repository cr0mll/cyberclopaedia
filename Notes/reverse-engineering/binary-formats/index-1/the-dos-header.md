# The DOS Header

The DOS header is a 64-byte struct located at the beginning of a PE file. It is mainly a legacy structure and so most of its fields are only relevant to MS-DOS. The ones pertinent to PE files are `e_magic` and `e_lfanew`. The following struct is defined in `<winnt.h>`

```cpp
typedef struct _IMAGE_DOS_HEADER {      // DOS .EXE header
    WORD   e_magic;                     // Magic number
    WORD   e_cblp;                      // Bytes on last page of file
    WORD   e_cp;                        // Pages in file
    WORD   e_crlc;                      // Relocations
    WORD   e_cparhdr;                   // Size of header in paragraphs
    WORD   e_minalloc;                  // Minimum extra paragraphs needed
    WORD   e_maxalloc;                  // Maximum extra paragraphs needed
    WORD   e_ss;                        // Initial (relative) SS value
    WORD   e_sp;                        // Initial SP value
    WORD   e_csum;                      // Checksum
    WORD   e_ip;                        // Initial IP value
    WORD   e_cs;                        // Initial (relative) CS value
    WORD   e_lfarlc;                    // File address of relocation table
    WORD   e_ovno;                      // Overlay number
    WORD   e_res[4];                    // Reserved words
    WORD   e_oemid;                     // OEM identifier (for e_oeminfo)
    WORD   e_oeminfo;                   // OEM information; e_oemid specific
    WORD   e_res2[10];                  // Reserved words
    LONG   e_lfanew;                    // File address of new exe header
  } IMAGE_DOS_HEADER, *PIMAGE_DOS_HEADER;
```

`e_magic` is a word, occupying 2 bytes, which identifies the file as an MS-DOS executable and always contains the value `0x5a4d`, or `MZ` in ASCII.

`e_lfanew` is located at an offset of `0x3c` from the start of the DOS header and holds an offset to the beginning of the NT headers, which is paramount to the PE loader on Windows.

The DOS header of a PE file can be inspected with PE-Bear:

![](<../../../Reverse Engineering/Binary Formats/PE/Resources/Images/PE\_DOS\_Header.png>)
