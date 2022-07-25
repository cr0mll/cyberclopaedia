# Introduction
Immediately following the [DOS header](The%20DOS%20Header.md) is the DOS Stub. This is a tiny portion of executable instructions which get executed instead of the programme when run in DOS mode. Its purpose is to print an error message that the programme cannot be run in DOS mode. It is possible to also alter the message displayed.

We can analyse the DOS stub with a disassembler:

```asm
0x0000000000000000:  0E                   push  cs  
0x0000000000000001:  1F                   pop   ds  
0x0000000000000002:  BA 0E 00             mov   dx, 0xe  
0x0000000000000005:  B4 09                mov   ah, 9  
0x0000000000000007:  CD 21                int   0x21
0x0000000000000009:  B8 01 4C             mov   ax, 0x4c01  
0x000000000000000c:  CD 21                int   0x21
```

The first two instructions set the code and data segments to the same value. Next, `mov dx, 0xe` moves the address, `0xe`, of the string containing the error message into `dx`. The error message follows right after the stub instructions. At `0x7`, interrupt `0x21` is invoked and its function is determined by the value that was moved into `ah` - in this case it will print a message. At the end, the same interrupt is invoked but this time with a different argument - `0x4c01`. This ultimately tells the programme to exit with an error code of 1.