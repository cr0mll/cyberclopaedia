# Introduction
Segments split the ELF binary into parts which are then loaded into memory by the OS programme loader. They can be thought of as grouping sections by their attributes and only selecting those which will be loaded into memory. In essence, segments contain information needed at runtime, while sections contain information needed at link-time. 

# The Programme Header Table
Segments are described by *programme headers* which are stored in the Programme Header Table (PHT). These structs are again defined in `<elf.h>`:

```cpp
typedef struct
{
  Elf32_Word	p_type;			/* Segment type */
  Elf32_Off	    p_offset;		/* Segment file offset */
  Elf32_Addr	p_vaddr;		/* Segment virtual address */
  Elf32_Addr	p_paddr;		/* Segment physical address */
  Elf32_Word	p_filesz;		/* Segment size in file */
  Elf32_Word	p_memsz;		/* Segment size in memory */
  Elf32_Word	p_flags;		/* Segment flags */
  Elf32_Word	p_align;		/* Segment alignment */
} Elf32_Phdr;

typedef struct
{
  Elf64_Word	p_type;			/* Segment type */
  Elf64_Word	p_flags;		/* Segment flags */
  Elf64_Off	    p_offset;		/* Segment file offset */
  Elf64_Addr	p_vaddr;		/* Segment virtual address */
  Elf64_Addr	p_paddr;		/* Segment physical address */
  Elf64_Xword	p_filesz;		/* Segment size in file */
  Elf64_Xword	p_memsz;		/* Segment size in memory */
  Elf64_Xword	p_align;		/* Segment alignment */
} Elf64_Phdr;
```

![](Resources/Images/ELF_Programme_Header.png)

- `p_type` - describes the type of the segment.
- `p_offset` - the offset from the beginning of the file where the segment resides.
- `p_vaddr` - the virtual address at which the segment resides in memory.
- `p_paddr` - the segment's physical address, which is relevant only for systems with physical addressing. This member holds unspecified contents for executables and shared objects
- `p_filesz` - the number of bytes the segment occupies in the file image. It may be 0.
- `p_memsz` - the number of bytes the segment occupies in the memory image. It may be 0.
- `p_align` - the value to which the segments are aligned in the file and in memory. If this holds 0 or 1, then no alignment is required. Otherwise, `p_align` should be a positive integer power of 2 and `p_vaddr` should be equal to `p_offset % p_align`.

# Segment Types
| Name       | Value      |
|------------|------------|
| `PT_NULL`    | 0          |
| `PT_LOAD`    | 1          |
| `PT_DYNAMIC` | 2          |
| `PT_INTERP`  | 3          |
| `PT_NOTE`    | 4          |
| `PT_SHLIB`   | 5          |
| `PT_PHDR`    | 6          |
| `PT_TLS`     | 7          |
| `PT_LOOS`    | 0x60000000 |
| `PT_HIOS`    | 0x6fffffff |
| `PT_LOPROC`  | 0x70000000 |
| `PT_HIPROC`  | 0x7fffffff |

## `PT_LOAD`
This specifies a loadable segment described by `p_filesz` and `p_memsz` which means the segment is going to be mapped into memory. Bytes from the file are mapped to the beginning of the memory segment. Should the memory size be larger than the file size, the extra bytes are filled with 0s and are placed after the segment's data. Note that the file size cannot be larger than the memory size. 

Entries of this type are sorted in an ascending order in the PHT according to their `p_vaddr` field.

All executable files must contain at least one `PT_LOAD` segment.
