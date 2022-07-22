# Introduction
The word "relocation" describes the process of matching symbol references with symbol definitions. ELF files contain *relocation entries* which store information about how to modify the contents of the file's sections in order to resolve the symbol references.

These relocation entries are represented by the following structs and are stored in *relocation sections*:

```cpp
/* Relocation table entry without addend (in section of type SHT_REL).  */

typedef struct
{
  Elf32_Addr	r_offset;		/* Address */
  Elf32_Word	r_info;			/* Relocation type and symbol index */
} Elf32_Rel;

typedef struct
{
  Elf64_Addr	r_offset;		/* Address */
  Elf64_Xword	r_info;			/* Relocation type and symbol index */
} Elf64_Rel;

/* Relocation table entry with addend (in section of type SHT_RELA).  */

typedef struct
{
  Elf32_Addr	r_offset;		/* Address */
  Elf32_Word	r_info;			/* Relocation type and symbol index */
  Elf32_Sword	r_addend;		/* Addend */
} Elf32_Rela;

typedef struct
{
  Elf64_Addr	r_offset;		/* Address */
  Elf64_Xword	r_info;			/* Relocation type and symbol index */
  Elf64_Sxword	r_addend;		/* Addend */
} Elf64_Rela;
```

The `r_offset` field points to the location that ultimately needs to be altered when the relocation is performed. For example, for functions this will typically point to somewhere in the Global Offset Table. For relocatable files this field contains an offset within a section to be modified. For shared objects and executable files, `r_offset` stores a virtual address where the relocation should take place.

`r_info` holds the symbol table index for the associated index as well as the type of relocation to be performed, which is platform-specific. Relocation types are ultimately computations that are performed in order to determine what value is to be stored at the relocation site. This information can be extracted by means of the following macros:

```cpp
#define ELF32_R_SYM(val)		((val) >> 8)
#define ELF32_R_TYPE(val)		((val) & 0xff)
#define ELF32_R_INFO(sym, type)		(((sym) << 8) + ((type) & 0xff))

#define ELF64_R_SYM(i)			((i) >> 32)
#define ELF64_R_TYPE(i)			((i) & 0xffffffff)
#define ELF64_R_INFO(sym,type)		((((Elf64_Xword) (sym)) << 32) + (type))
```

`r_addend` just specifies a constant value which is used to compute the value which will be ultimately stored at the relocation site.

Entries of type `ElfN_Rel` are stored in sections of type `SHT_REL`, while entries of type `ElfN_Rela` are stored in sections of type `SHT_RELA`. An ELF file may only contain relocation entries of one type and the reasons for using one type over the other are typically architecture-dependent. Every relocation sections can contain references to two other sections. First of all, a relocation section will be linked to its corresponding symbol table and the index of its section header can be retrieved from the `sh_link` field of the relocation section. For relocatable files, the index of the section for which `r_offset` is relevant is stored in the `sh_info` field of the relocation section's header.

You can view the relocation entries of an ELF file by using the `-r` flag with `readelf`:

![](Resources/Images/ELF_Read_Relocations.png)