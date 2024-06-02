# Introduction
The x86-64 assembly paradigm has quite a lot of different instructions available at its disposal. An instructions consists of an operation and a set of operands where the latter specify the data and the former specifies what is to be done to that data. 

## Operand Notation
Typically, instruction signatures are represented using the following operand notation.

|Operand Notation|Description|
|:------:|:-------:|
|`<reg>`|Register operand.|
|`<reg8>`, `<reg16>`, `<reg32>`, `<reg64>`|Register operand with a specific size requirement.|
|`<src>`|Source operand. |
|`<dest>`|Destination operand - this may be a register or memory location.|
|`<RXdest>`|Floating-point destination register operand.|
|`<imm>`|Immediate value (a literal). Base-10 by default, but can be preceded with `0x` to make it hexadecimal.|
|`<mem>`|Memory location - a variable name or an address.|
|`<op>`|Arbitrary operand - immediate value, register or memory location.|
|`<label>`|Programme label.|
