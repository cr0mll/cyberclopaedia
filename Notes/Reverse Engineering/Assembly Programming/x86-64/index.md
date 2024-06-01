# x86-64

Source code gets compiled to assembly and then assembly gets compiled to machine code. Assembly has a direct one-to-one mapping of its instructions to those in machine language. This makes assembly the only possible way to disambiguously take a look at what a program does. Assembly is essentially a human readable version of machine code.

## Intel vs AT\&T Syntax

There are two general syntax formats for writing Assembly - Intel and AT\&T. I will be using Intel throughout my notes, but here is a list of common differences between the two because you never know which one you might have to read:

### Intel

* Instruction format - `operation destination, source`
* Instruction sufixes - none
* Register & Immediate value prefixes - none
* Dereferencing - done with `[]`

### AT\&T

* Instruction format - `operation source, destination`
*   Mnemonic sufixes - mnemonics have a suffix depending on the size of their operands - `b` for byte, `w` for word, `l` long

    ```
    movb %bl,%al
    movw %bx,%ax
    movl  %ebx,%eax
    movl (%ebx),%eax
    ```
* Register & Immediate value prefixes - registers are prefixed with `%` and immediate values with `$`
* Dereferencing - done with `()`
