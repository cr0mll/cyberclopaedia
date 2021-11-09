# Registers
Registers are value containers which reside on the CPU and not in RAM. They are small in size and some have special purposes. You may store both addresses and values in registers and depending on the instruction used, the data inside will be interpreted in a different way - this is commonly called an *addressing mode*.

In x86 Intel assembly (i386), the registers are 32 bits (4 bytes) in size and some of them are reserved:

`ebp` - the base pointer, points to the bottom of the current stack frame

`esp` - the stack pointer, points to the top of the current stack frame

`eip` - the instruction pointer, points to the next instruction to be executed

The other registers are general purpose registers and can be used for anything you like:
`eax`, `ebx`, `ecx`, `edx`, `esi`, `edi`.

x64 AMD assembly (amd64) extends these 32-bit registers to 64-bit ones and denotes these new version by replacing the initial `e` with an `r`: `rbp`, `rsp`, `rip`, `eax`, ... It is important to note that these are *not* different registers - `eax` and `rax` refer to the same space on the CPU, however, `eax` only provides access to the lower 32 bits of the 64-bit register. You can also get access to the lower 16 and 8 bits of the register using different names:


 8 Byte Register | Lower 4 Bytes | Lower 2 Bytes | Lower Byte 
:---------------:|:-------------:|:-------------:|:---------------:
   rbp           |     ebp       |     bp        |     bpl    
   rsp           |     esp       |     sp        |     spl    
   rip           |     eip       |               |            
   rax           |     eax       |     ax        |     al     
   rbx           |     ebx       |     bx        |     bl     
   rcx           |     ecx       |     cx        |     cl     
   rdx           |     edx       |     dx        |     dl     
   rsi           |     esi       |     si        |     sil    
   rdi           |     edi       |     di        |     dil    
   r8            |     r8d       |     r8w       |     r8b    
   r9            |     r9d       |     r9w       |     r9b    
   r10           |     r10d      |     r10w      |     r10b   
   r11           |     r11d      |     r11w      |     r11b  
   r12           |     r12d      |     r12w      |     r12b   
   r13           |     r13d      |     r13w      |     r13b   
   r14           |     r14d      |     r14w      |     r14b   
   r15           |     r15d      |     r15w      |     r15b   


Each row contains names which refer to different parts of the *same* register. Note, you cannot access the lower 16 or 8 bits of the instruction pointer.

You might sometimes see `WORD` or `DWORD` being used in a similar context - `WORD` means 2 bytes and `DWORD` means 4 bytes.

## Register Use in x64 Linux
Under x64 Linux, function arguments are passed via registers:
```
rdi:    First Argument
rsi:    Second Argument
rdx:    Third Argument
rcx:    Fourth Argument
r8:     Fifth Argument
r9:     Sixth Argument
```

The return value is store in `rax` (`eax` on 32-bit machines).

## Register Dereferencing
Register dereferencing occurs when the value of the register is treated as an address to the actual data to be used, rather than the data itself. This means that addressed can be stored in registers and used later - this is useful when dealing with large data sizes.

For example,

```
mov rax, [rdx]
```

Will check the value inside `rdx` and treat it as an address - it will go to the location where this address points and get its data from there. It will then move this data into `rax`. If we hadn't used `[]`, it would have treated the address in `rdx` simply as a value and moved it directly into `rax`.