# Introduction
Registers are value containers which reside on the CPU (separately from RAM). They are small in size and some have special purposes. x86-64 assembly operates with 16 general-purpose registers (GPRs). It should be noted that the 8-byte (`r`) variants do not exist in 32-bit mode.

 64-bit Register | Lower 4 Bytes | Lower 2 Bytes | Lower 1 Byte 
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

Each row contains names which refer to different parts of the *same* register. Note, the lower 16 bits of the `rip` register (instruction pointer) are inaccessible on their own.

For example, the `rax` register could be set to the following:

```asm
rax = 0x0000 000AB 10CA 07F0
```

The name `eax` would then only refer to the part of the `rax` register which contains `10CA 07F0`. Similarly, `ax` would represent `07F0`, and `al` would be just `F0`.

Additionally, the upper byte of `ax`, `bx`, `cx` and `dx` may be separately accessed by means of the `ah`, `bh`, `ch` and `dh` monikers, which exist for legacy reasons.

# Register Specialisation
Not all registers available in the x86-64 paradigm are created equal. Certain registers are reserved for specific purposes, despite being called general-purpose.

### The Stack Pointer `rsp`
The stack pointer `rsp` (`esp` for 32-bit machines) is used to point to the current top of the stack and should *not* be used for any other purpose other than in instructions which involve stack manipulation.

### The Base Pointer `rbp`
The base pointer `rbp` (`ebp` for 32-bit machines) is the twin brother of the stack pointer and is used as a base pointer when calling functions. It points to the beginning of the current function's stack frame. Interestingly enough, its use is actually gratuitous because compilers can manage the stack frames of functions equally well without a separate base pointer. It is mostly used to make assembly code more comprehensible for humans.

### The Instruction Pointer `rip`
The instruction pointer `rip` (`eip` for 32-bit machines) points to the *next* instruction to be executed. It is paramount not to get confused when using a debugger, since the `rip` does *not* actually point to the instruction currently being executed.

### The Flag Register `rFlags`
The flag register `rFlags` (`eFlags` for 32-bit machines) is an isolated register which is automatically updated by the CPU after every instruction and is not directly accessible by programmes. Following is a table of the meaning assigned to different bits of this register. Note that only the lower 32 bits are used even on 64-bit machines.

|Name|Symbol|Bit|Usage|=1|=0|
|:----:|:------:|:-----:|:-----:|:-----:|:----:|
|Carry|CF|0|Indicates whether the previous operation resulted in a carry-over.|CY (Carry)|CN (No Carry)|
|||1|Reserved. Always set to 1 for `eFlags`.|||
|Parity|PF|2|Indicates whether the least significant byte of the previous instruction's result has an even number of 1's.|PE (Parity Even)|PO (Parity Odd)|
|||3|Reserved.|||
|Auxiliary Carry|AF|4|Used to support binary-coded decimal operations.|AC (Auxiliary Carry)|NA (No Auxiliary Carry)|
|||5|Reserved.|||
|Zero|ZF|6|Indicates whether the previous operation resulted in a zero.|ZR (Zero)|NZ (Not Zero)|
|Sign|SF|7|Indicates whether the most significant bit was set to 1 in the previous operation (implies a negative result in signed-data contexts).|NG (Negative)|PL (Positive)|
|Trap|TF|8|Used by debuggers when single-stepping through a programme.|||
|Interrupt Enable|IF|9|Indicates whether or not the CPU should immediately respond to maskable hardware interrupts.|EI (Enable Interrupt)|DI (Disable Interrupt)|
|Direction|DF|10|Indicates the direction in which several bytes of data should be copied from one location to another.|DN (Down)|UP (Up)|
|Overflow|OF|11|Indicates whether the previous operation resulted in an integer overflow.|OV (Overflow)|NV (No Overflow)|
|I/O Privilege Level|IOPL|12-13||||
|Nested Task|NT|14||||
|Mode|MD|15||||
|Resume|RF|16||||
|Virtual 8086 Mode|VM|17||||
|||31-63|Reserved.|||

### Floating-Point Registers and SSE
In addition to the aforementioned registers, the x86-64 paradigm includes 16 registers, `xmm[0-15]`, which are used for 32- and 64-bit floating-point operations. Furthermore, the same registers are used to support the Streaming SIMD Extensions (SSE) which allow for the execution of Single Instruction Multiple Data (SIMD) instructions.

