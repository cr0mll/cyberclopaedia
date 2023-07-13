# Introduction
This is the contemporary IP addressing scheme, which completely does away with the separation between IP networks into classes. It is particularly flexible because it allows network blocks of arbitrary size, however, it does come with added complexity.

### CIDR ("Slash") Notation
The dividing line between the Network and Host IDs is specified via the slash notation: `x.x.x.x/y`. The number after the slash specifies the number of bits that are used for the Network ID.