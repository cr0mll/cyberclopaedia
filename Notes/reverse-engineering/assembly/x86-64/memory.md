# Memory

## Endianness

Memory is nothing more than a series of bytes which can be individually addressed. When storing values which are larger than a single byte, the bytes under the x86-64 paradigms are stored in _little-endian_ order - the least significant byte (LSB) at the lowest memory address and the most significant byte (MSB) at the highest memory address.

![](<../../../Reverse Engineering/Assembly Programming/x86-64/Resources/Images/Byte Names.svg>)

For example, the variable `var = 0xDEADBEEF` would be represented in memory as follows:

![](<../../../Reverse Engineering/Assembly Programming/x86-64/Resources/Images/Little Endian Variable Representation.svg>)

Note how the right-most byte is at a lower address and the addresses for the rest of the bytes increase as we go right-to-left.

## Memory Layout

Below is the general memory layout of a programme:

![](<../../../Reverse Engineering/Assembly Programming/x86-64/Resources/Images/Programme Memory Layout.svg>)

The reserved section is unavailable to user programmes. The `.text` sections stores the instructions which comprise the programme's code. Static variables which were declared and given a value at assemble-time are stored in the `.data` section. The `.bss` section stores static uninitialised data, i.e variables which were declared but were not provided with an initial value. If such variables are used before they are initialised, their value will be meaningless.

The Stack and the Heap are where data can be allocated at run-time. The Stack is used for allocating space for small amounts of data with a size known at compile-time and grows from higher to lower addresses. Conversely, the Heap allows for the dynamic allocation of space for data of size known at run-time and grows from lower to higher addresses.
