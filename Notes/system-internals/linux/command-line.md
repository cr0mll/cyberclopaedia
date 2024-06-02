# Command Line

## Introduction

The command line, is a text-based interface which allows for interaction with the computer and execution of commands. The actual command interpreter which carries out the commands is referred to as the _shell_ and there are multiple examples of shells such as `bash`, `zsh`, `sh`, etc.

## Input and Output Redirection

It is possible to redirect input and output from and to files when invoking commands:

|  Redirection  |                                 Description                                |
| :-----------: | :------------------------------------------------------------------------: |
|  `< in_file`  |            Redirect `in_file` into the command's standard input.           |
|  `> out_file` |  Redirect the command's standard output into `out_file` by overwriting it. |
| `>> out_file` | Redirect the command's standard output into `out_file` by appending to it. |
|  `> err_file` |  Redirect the command's standard error into `err_file` by overwriting it.  |
| `>> err_file` |  Redirect the command's standard error into `err_file` by appending to it. |

![](<../../System Internals/Linux/Resources/Images/Command Line/Input File Redirection.png>)

![](<../../System Internals/Linux/Resources/Images/Command Line/Output File Redirection.png>)

### Pipes

Moreover, information may be redirected directly from one command to another by using unnamed pipes (`|`).

![](<../../System Internals/Linux/Resources/Images/Command Line/Unnamed Pipe Redirection.png>)
