# Modes of Operation

The block length of all practical [block ciphers](../) is very small, usually 64-256 bits, but messages commonly exceed 16 bytes. Therefore, we need a means of dividing a message into blocks which match the block length of the cipher used. There are numerous ways to achieve this, called _modes of operations_, and, as it turns out, not all methods are created equal.

```admonish
Using a secure block cipher is *not* enough - one needs to also use a proper mode of operation. A secure block cipher ensures that each *block* is encrypted securely, while a secure mode of operation ensures that *the entire message* is encrypted securely.
```

In practice, a block cipher is never used on its own - there is always a mode of operation involved. Therefore, saying that one "encrypts something with AES" is not enough - one needs to also specify the mode of operation used, for example AES-CBC or DES-CTR.

```admonish
When discussing modes of operation, the message length is assumed to be a multiple of the block length. In practice, however, this is not the case and certain techniques need to be used to make all message blocks of the same length.
```
