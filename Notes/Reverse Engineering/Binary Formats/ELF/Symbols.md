# Introduction
ELF symbols represent symbolic references to certain pieces of code and data such as functions and global variables. For example, the `printf()` function will have such an entry in the `.symtab` and `.dynsym` sections (if the object is dynamically linked).

# The Symbol Tables
Ultimately, there exist at most two symbol tables in an ELF object - `.symtab` and `.dynsym`. The former will also contain the contents of the latter, however, it is not necessary for dynamic linking and is thus usually omitted in the memory image of a binary. The extraneous symbols in `.symtab` are simply too big and completely useless during execution time, so `.dynsym` only contains the information absolutely necessary for dynamic linking. You will see that `.symtab` has no flags, while `.dynsym` is marked as `ALLOC`.

![](Resources/Images/ELF_Symbol_Tables_Flags.png)

Both symbol tables contain entries of the following types:

```cpp
typedef struct
{
  Elf32_Word	st_name;		/* Symbol name (string tbl index) */
  Elf32_Addr	st_value;		/* Symbol value */
  Elf32_Word	st_size;		/* Symbol size */
  unsigned char	st_info;		/* Symbol type and binding */
  unsigned char	st_other;		/* Symbol visibility */
  Elf32_Section	st_shndx;		/* Section index */
} Elf32_Sym;

typedef struct
{
  Elf64_Word	st_name;		/* Symbol name (string tbl index) */
  unsigned char	st_info;		/* Symbol type and binding */
  unsigned char st_other;		/* Symbol visibility */
  Elf64_Section	st_shndx;		/* Section index */
  Elf64_Addr	st_value;		/* Symbol value */
  Elf64_Xword	st_size;		/* Symbol size */
} Elf64_Sym;
```

![](Resources/Images/ELF_Symbol.png)

- `st_name` - an offset (in bytes) from the beginning of the symbol name string table (either `.dynstr` or `.strtab`), where the name of the symbol is located.
- `st_value` - the value of the symbol, which is either an address or an offset of its location.
- `st_size` - symbols may have an associated size. If this field is 0, the symbol has no size or it is unknown
- `st_other` - defines the symbol's visibility.
- `st_shndx` - since each symbol is defined in relation to some section, the index of the section header corresponding to the relevant section is stored in this field.
- `st_info` - this field specifies the symbol type and binding.

You can view the symbol tables by adding the `-s` flag to `readelf`:

![](Resources/Images/ELF_Read_Symbols.png)

If a symbol's value refers to a specific location within a section, `st_shndx` holds an index into the section header table. As the section moves during relocation, the symbol's value changes as well. Certain section indices, however, have reserved semantics:

`SHN_ABS` specifies that the symbol value is absolute and won't change during relocation.

`SHN_COMMON` labels a yet unallocated common block. The symbol's value holds alignment constraints. The linker allocates storage for the symbol at an address that is a multiple of the symbol value, while the `st_size` field holds the number of bytes necessary for the allocation. Such symbols may only occur in relocatable files.

`SHN_UNDEF` specifies an undefined symbol. When the linker combines this object file with another which defines the symbol, this file's references to the symbol will be linked directly to the actual definition.

`SHN_XINDEX` serves as an escape value and indicates that the relevant section header index is too large to fit in the the symbol. Therefore, the section header index is actually found in the `SHT_SYMTAB_SHNDX` section whose entries correspond one-to-one with those in the symbol table. 

# Symbol Types & Bindings
The following table contains the possible symbol bindings:

| Name       | Value |
|------------|-------|
| `STB_LOCAL`  | 0     |
| `STB_GLOBAL` | 1     |
| `STB_WEAK`   | 2     |
| `STB_LOOS`   | 10    |
| `STB_HIOS`   | 12    |
| `STB_LOPROC` | 13    |
| `STB_HIPROC` | 15    |

`STB_LOCAL` defines a local symbol. Such symbols are only visible in the object file containing their definition. This means that multiple local symbols with the same name may exist independently inside multiple object files without interfering with each other during linking.

`STB_GLOBAL` defines a global symbol. These symbols are visible to all files being combined. One file's definition of a global symbol will satisfy another file's reference to the same symbol. Multiple global symbols with the same name are not allowed.

`STB_WEAK` defines a weak symbol. Such symbols resemble global symbols, but have definitions with lower precedence. Consequently, the definition of an `STB_WEAK` symbol will be overridden by the definition of a different symbol with the same name, if such a symbol exists.

The other values are reserved for OS- and processor-specific semantics.

Following is a table containing the possible symbol types:

| Name        | Value |
|-------------|-------|
| `STT_NOTYPE`  | 0     |
| `STT_OBJECT`  | 1     |
| `STT_FUNC`    | 2     |
| `STT_SECTION` | 3     |
| `STT_FILE`    | 4     |
| `STT_COMMON`  | 5     |
| `STT_TLS`     | 6     |
| `STT_LOOS`    | 10    |
| `STT_HIOS`    | 12    |
| `STT_LOPROC`  | 13    |
| `STT_HIPROC`  | 15    |

`STT_NOTYPE` defines a symbol with an undefined type.

`STT_OBJECT` represents a symbol that is associated with data such as a variable, an array, etc.

`STT_FUNC` is a symbol associated with a function.

`STT_SECTION` is a symbol associated with a section. Such entries are typically used for relocation and are of the `STB_LOCAL` binding.

`STT_FILE` symbols contain the names of source files associated with object files. Such symbols are local, have a section index of `SHN_ABS` and precede any other local symbols in the file.

`STT_COMMON` describes an uninitialised common block. 

`STT_TLS` is a thread-local storage entity. It stores an offset to the symbol and not its address. Such symbols may only be referenced by thread-local storage relocations.

A symbol's type and binding are encoded into and decoded from the `st_info` field by means of the following macros:

```cpp
/* How to extract and insert information held in the st_info field.  */

#define ELF32_ST_BIND(val)		(((unsigned char) (val)) >> 4)
#define ELF32_ST_TYPE(val)		((val) & 0xf)
#define ELF32_ST_INFO(bind, type)	(((bind) << 4) + ((type) & 0xf))

/* Both Elf32_Sym and Elf64_Sym use the same one-byte st_info field.  */
#define ELF64_ST_BIND(val)		ELF32_ST_BIND (val)
#define ELF64_ST_TYPE(val)		ELF32_ST_TYPE (val)
#define ELF64_ST_INFO(bind, type)	ELF32_ST_INFO ((bind), (type))
```

# Symbol Visibility
The visibility of a symbol specifies how the symbol should be accessed once it has become a part of and executable or shared object, notwithstanding that it may be specified in a relocatable file. In essence, a symbol's visibility tells the linker how that symbol will be used in the end file. Following is a table with the possible visibility values.

| Name          | Value |
|---------------|-------|
| `STV_DEFAULT`   | 0     |
| `STV_INTERNAL`  | 1     |
| `STV_HIDDEN`    | 2     |
| `STV_PROTECTED` | 3     |

`STV_DEFAULT` symbols have a visibility equivalent to the one defined by their binding. 

`STV_PROTECTED` symbols are visible to other files in the linking process (components), but are not *preemptable*. This means that references to such symbols from within the defining component *must* be resolved to the definition in that component. Local symbols cannot be protected.

`STV_HIDDEN` symbols have names which are invisible to external components and may be used for specifying the external interface of a given component. Hidden symbols in relocatable files must be transformed into local symbols by the linker.

`STV_INTERNAL` symbols have a platform-dependent meaning. Ultimately, however, the linker should be able to treat them as hidden symbols. 

