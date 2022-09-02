# Introduction
`radare2` is an open-source framework for reverse engineering. The framework includes multiple tools which all work in tandem in order to aid in the analysis of binary files. 

It uses short abbreviations for its commands - single letters - and many of its commands have subcommands which are also expressed as single letters. Luckily, you can always append a `?` to a specific command in order to view its subcommands and what they do.

To quit `radare2`, use the `q` command.

# Loading a Binary
You can load a binary by invoking the `r2` command. You might sometimes need to also add the `-e io.cache=true` option in order to fix relocations in disassembly.

![](Resources/Images/load-binary.png)