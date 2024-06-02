# Data Representation

## Introduction

Data representation refers to the way that values are stored in a computer. For technical reasons, computers do not use the familiar base-10 number system but rather avail themselves of the base-2 (binary) system. Under this paradigm, numbers are represented as 1's and 0's.

## Integer Representation

When storing an integer value, there are two ways to represent it - signed and unsigned - depending on whether the value should be entirely non-negative or may also have a "-" sign. Based on the number of bits used for storing a value, the value may have a different range.

|            Size            |  Range Size |     Unsigned Range     |              Signed Range             |
| :------------------------: | :---------: | :--------------------: | :-----------------------------------: |
|        Byte (8 bits)       |   $$2^8$$   |      $$[0..255]$$      |            $$[-128..+127]$$           |
|       Word (16 bits)       |  $$2^{16}$$ |     $$[0..65,535]$$    |         $$[-32,768..+32,767]$$        |
|    Doubleword (32 bits)    |  $$2^{32}$$ | $$[0..4,294,967,295]$$ | $$[-2,147,483,648.. +2,147,483,647]$$ |
|     Quadword (64 bits)     |  $$2^{64}$$ |    $$[0..2^{64}-1]$$   |        $$[-2^{63}..+2^{63}-1]$$       |
| Double Quadword (128 bits) | $$2^{128}$$ |  $$[0..2^{128} - 1]$$  |     $$[-2^{127}.. + 2^{127} - 1]$$    |

Unsigned integers are represented in their typical binary form.

### Two's Complement

Signed integers are represented using two's complement. In order to convert a acquire the negative form of a number in two's complement, is two negate all of its bits and add 1 to the number. A corollary of this representation is that it adds no complexity to the addition and subtraction operations.
