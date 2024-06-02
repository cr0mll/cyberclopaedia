# Basic Reverse Engineering using objdump, strace, and ltrace

## Reverse Engineering with objdump

`objdump` is a program for displaying information from binaries. It can be used for showing different aspects of the object file. By default, it generates AT\&T assembly, but you can change this with the `-M intel` option.

*   disassemble everything - `-D`

    ```
    objdump -D <binary> -M intel
    ```

    ![](<../Reverse Engineering/Resources/Images/objdump-basic.png>)
*   display sections headers - `-h`

    ```
    objdump -h <binary>
    ```

    ![](<../Reverse Engineering/Resources/Images/objdump-section-headers.png>)
*   print private headers - `-p`

    ```
    objdump -p <binary>
    ```

    Note the flags on the private headers. If the `x` flag is on, then that section is executable.

    ![](<../Reverse Engineering/Resources/Images/objdump-private-headers.png>)

## Tracing syscalls with strace

`strace` is a program for tracing what system calls a binary issues during runtime. It can be used with the following basic syntax:

```
strace <binary>
```

Note, that if the binary is in your current working directory, you will need to prepend `./` to its name because `strace` works with processes and not the actual stored binary.

![](<../Reverse Engineering/Resources/Images/strace-basic.png>)

## Tracing library calls with ltrace

`ltrace` is rather similar to `strace`, but instead of system calls, it traces calls to functions in certain libraries. The syntax for it isn't unlike that for `strace`.

```
ltrace <binary>
```

Note, that if the binary is in your current working directory, you will need to prepend `./` to its name because `ltrace` works with processes and not the actual stored binary.

![](<../Reverse Engineering/Resources/Images/ltrace-basic.png>)
