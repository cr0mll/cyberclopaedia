# Dynamic Linking

## Introduction

Dynamic linking permits the loading of libraries at runtime, which avoids their incorporation into the executable at compile time and, consequently, saves a drastic amount of disk space at the cost of significantly complicating the linking process. The dynamic linker has to go through the instructions and fix any calls to external functions after the required libraries have been mapped into the running executable. Additionally, the default behaviour is the so-called lazy loading - function addresses aren’t even resolved until the first time a procedure is invoked (although this can be overridden when compiling the executable).

## How It Works

Dynamically-linked programmes contain a segment of type `PT_INTERP` which holds the path to the programme's interpreter. Upon execution, the interpreter is invoked and control flow is transferred to it. Subsequently, the interpreter loads the `PT_LOAD` segments of the programme. Then it uses the dynamic segment (`.dynamic`) to locate and load all dependencies from disk into memory. Since each dependency may also contain other dynamic dependencies, this process is recursive. Once this is done, [relocations](relocations.md) are performed. Subsequently, the initialisation functions (those in the `.preinit_array`, `.init`, and `.init_array` sections) of the shared libraries are invoked. Finally, the interpreter transfers execution to the programme's entry point as if nothing had happened.

![](<../../../Reverse Engineering/Binary Formats/ELF/Resources/Images/ELF\_Dynamic\_Linking.png>)

### Lazy Loading <a href="#lazy-loading" id="lazy-loading"></a>

The above process, while working, is very unoptimised. Imagine how much time will be wasted loading thousands of symbols at start-up for large programmes. Moreover, a programme could exit prematurely due to incorrect input and what then? All those symbols which got loaded never got used and so resources were again wasted. The solution to this problem, which is also nowadays the default behaviour, is to use the so-called \*lazy loading\*. Instead of loading every symbol before the programme even starts, symbols are loaded at the time of their first use. More specifically, functions are resolved when they are first invoked. This is all enabled by the \*Procedure Linkage Table (PLT)\* and the \*Global Offset Table (GOT)\*.

#### The Global Offset Table <a href="#got" id="got"></a>

The Global Offset Table is a section which gets loaded into the memory image of an ELF file. When lazy loading is enabled, the GOT is writable. Ultimately, the GOT stores absolute addresses but is referenced in a position-independent way. Thus, it serves as a converter from relative to absolute addresses. It is an array of 32- or 64-bit addresses. It is paramount to note that the GOT holds \*values\* and \*not\* instructions, so disassembling it will result in garbage.

#### The Procedure Linkage Table <a href="#plt" id="plt"></a>

The Procedure Linkage Table resembles the GOT in the sense that it redirects position-independent function calls to absolute locations. This table contains entries of executable code which are 3 instructions long. You can view the PLT of an ELF file using this command: \`objdump -d -j .plt \`

![](<../../../Reverse Engineering/Binary Formats/ELF/Resources/Images/ELF\_PLT.png>)

There is an entry for every function that is located in a shared library. The first instruction in each entry jumps to the location specified in the corresponding entry of the Global Offset Table. If the function has been called before, this will be the absolute address of its definition in the shared library and so execution flow will be forwarded directly to the function.

![](<../../../Reverse Engineering/Binary Formats/ELF/Resources/Images/ELF\_PLT\_GOT\_Called.png>)

If this is the first time that the procedure is being invoked, the entry in the Global Offset Table will point to the next instruction in the relevant PLT entry. This instruction pushes the _relocation argument_ (`relog_arg`) for this symbol onto the stack. Finally, the third instruction jumps to the first entry in the PLT - PLT0. This entry is special. In reality, it only contains two instructions (the third is there for alignment purposes). The first instruction in PLT0 pushes the address of the _link map_ onto the stack. The link map is a structure which describes all the dependencies that the ELF file requires and its address is stored in the first entry of the GOT. Next, PLT0 jumps to a function called `_dl_runtime_resolve`, whose address is stored in the second entry of the GOT.

![](<../../../Reverse Engineering/Binary Formats/ELF/Resources/Images/ELF\_PLT\_GOT\_Uncalled.png>)

#### `_dl_runtime_resolve`

`_dl_runtime_resolve` is a special procedure which is what actuates the dynamic linking process. It does not follow standard calling conventions and instead retrieves its arguments directly from the stack. It takes the `link_map` and the relocation argument, `reloc_arg`. Under the hood, `_dl_runtime_resolve` is just a wrapper around several other procedures which will ultimately locate the requested symbol, change its entry in the GOT and then forward execution to it.

Initially, the relocation argument is used in order to locate the appropriate entry in the relocation table of the executable. The `r_info` member of this entry is then used to find the corresponding element in the dynamic symbol table. From there, `st_name` is utilised to pinpoint the location of the name of the function in the string table. Subsequently, `_dl_runtime_resolve` avails itself of this string in order to look it up in the code of the library. Once the address is found, `r_offset` is used to locate where in the GOT the address should be placed (note that despite its use, `r_offset` is actually an offset from the beginning of the ELF header). At last, `_dl_runtime_resolve_` forwards execution to the function initially invoked with any arguments which were provided to it.

![](<../../../Reverse Engineering/Binary Formats/ELF/Resources/Images/ELF\_dl\_runtime\_resolve.png.png>)
