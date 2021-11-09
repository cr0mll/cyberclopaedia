# Instructions
Each program is comprised of a set of instructions which tell the CPU what operations it needs to perform. Different CPU architectures make use of different instruction sets, however, all of them boil down to two things - an opertation code (opcode) and optional data that the instruction operates with. These are all represented using bits - 1s and 0s.


## `mov`
Moves the value inside one register to another:
```
mov rax, rdx
```

## `lea` - Load Effective Address
This instruction calculates the address of its second operand and moves it into its first operand:
```
lea rdx, [rax+0x10]
```
This will move `rax+0x10` inside `rdx`.

## `add`
This instruction adds its operands and stores the result in its first operand:
```
add rax, rdx
```

## `sub`
This instruction subtracts the second operand from the first and stores the result in its first operand
```
sub rax, 0x9
```

## `xor`
It performs XOR-ing on its operands and stores the results into the first operand:
```
xor rdx, rax
```

The `and` and `or` are the same, but instead perform a binary `AND` and a binary `OR` operation, respectively.

## `push`
Decreases the stack pointer (grows the stack) by 8 (4 on x86) bytes and stores the contents of its operand on the stack:
```
push rax
```

## `pop`
Increases the stack pointer (shrinks the stack) by 8 (4 on x86) bytes and stores the popped value from the stack into its operand:
```
pop rax
```

## `jmp`
Jumps to the address specified - used for redirecting code execution:
```
jmp 0x6A2B10
```

## `call`
Used for invoking procedures. It first pushes the values of the base and stack pointers onto the stack and then jumps to the specified address. After the function is finished, a `ret` instruction is issued which restores the values of the stack and base pointers from the stack and continues execution from where it left off.

## `cmp`
It compares the value of its two operands and sets the according flags depending on the result:
```
cmp rax, rdx
```

If `rax` < `rdx`, the zero flag is set to 0 and the carry flag is set to 1.

If `rax` > `rdx`, the zero flag is set to 0 and the carry flag is set to 0.

If `rax` = `rdx`, the zero flag is set to 1 and the carry flag is set to 0.

## `jz` / `jnz`
`jump-if-zero` and `jump-if-not-zero` execute depending on the state of the zero flag.