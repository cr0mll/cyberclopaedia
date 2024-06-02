# Introduction
Addressing modes refer to the supported methods for accessing and manipulating data. There are three basic addressing modes in x86-64: register, immediate and memory.

## Register Mode Addressing
In register mode addressing, the operand is a register (*brain undergoing nuclear-fission*).

```asm
mov rax, rbx
```

The value inside `rbx` is copied to `rax`.

## Immediate Mode Addressing
In immediate mode addressing, the operand is an immediate value, or a *literal*. These are simply constant values such as `10`, `0xfa3`, `"lol"`, and so on.

```asm
mov rax, 123
```

The number 123 is copied into `rax`.

## Memory Mode Addressing
In memory mode addressing, the operand is treated as a memory location. This is referred to as *indirection* or *dereferencing* and is similar to how pointers can be dereferenced in C/C++. In assembly, this is done by wrapping the operand in square brackets: `[]`.

So for example, `rax` refers to the value stored within the register `rax`. However, `[rax]` means "treat `rax` like a pointer and use the value it points to". Essentially, `[rax]` treats the value inside the register as an address and uses that address to find the actual value it needs. 

```asm
mov DWORD PTR [rax], 0xdeadbeef
```

The value `0xdeadbeef` is copied into the location pointed to by `rax`.

Since memory is byte-addressable, it is oftentimes required to specify how many bytes we want to access. This is done by prepending one of the following specifiers to the operand:

|Specifier|Number of Bytes|
|:----:|:------:|
|`BYTE PTR` / `byte`|1|
|`WORD PTR` / `word`|2|
|`DWORD PTR` / `dword`|4|
|`QWORD PTR` / `qword`|8|

Moreover, the actual formula for memory addressing is a bit more complicated, since it was developed mainly for making the implementation of arrays easier.
```asm
[baseAddr + (indexReg * scaleValue) + offset]
```

The `baseAddr` must be a register or variable name, although it may be omitted in which case the address is relative to the beginning of the data segment. `indexReg` is a register which specifies contains an index into the array and the `scaleValue` is the size (in bytes) of a single member of the array. The offset must be an immediate value.

```asm
mov eax, dword [ebx] ; move into eax the value which ebx points to
mov rax, QWORD PTR [rbx + rsi] ; move into rax the value which (rbx + rsi) points to
mov rcx, qword [rax+(rsi*8)] ; move into rcx the value which (rax + (rsi*8)) points to
```