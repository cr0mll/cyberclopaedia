# Introduction
Variables in assembly do not exists in the same sense as they do in higher-level programming languages. This is especially true of local variabls such as those inside functions. Instead of allocating space for a particular value and having that place be "named" according to a variable, the compiler may use a combination of stack and heap allocations as well as registers to achieve behaviour resembling a variable.

That being said, there are some parallels with higher-level programming languages as well.

When manually programming assembly, it should be noted that variable names are more or less identical to addresses.
# Constants
Assembly constants cannot be changed during run-time execution. Their value is substituted at assembly-time (corresponding to compile-time substitution for constants in higher-level languages). Consequently, constants are not even assigned a location in memory, for they turn into hard-coded values.

Defining constants in assembly is done in the following way:
```asm
<NAME> equ <value>
```

For example,
```asm
EXAMPLE equ 0xdeadbeef
```

# Static Initialised Data
Static or global variables which are initialised before the programme executes are stored in the `.data` section. In order to define such a variable, you must give it a name, data size and value. In contrast with constants, such data can be mutated during run-time.

The following data size declarations can be used:

|Declaration|Size (in bits)|Type|
|:--------:|:---------:|:-------:|
|`db`|8||
|`dw`|16||
|`dd`|32||
|`dq`|64||
|`ddq`|128|Integer|
|`dt`|128|Floating-Point|

The syntax for declaring such variables is as follows:
```asm
<name> <dataSize> <initalValue>
```

For example:
```asm
byteVar db 0x1A ; byte variable
```

# Static Uninitialised Data
Static uninitialised data is stored in the `.bss` section. The syntax for allocating such variables is following:

```asm
<name> <resType> <count>
```

Such variables are usually allocated as chunks, hence the required `count`. The primary data types are as follows:

|Declaration|Size (in bits)|
|:---:|:-----:|
|`resb`|8|
|`resw`|16|
|`resd`|32|
|`resq`|64|
|`resdq`|128|

Some examples:
```asm
bArr resb 10 ; 10 element byte array  
wArr resw 50 ; 50 element word array  
dArr resd 100 ; 100 element double array  
qArr resq 200 ; 200 element quad array
```

