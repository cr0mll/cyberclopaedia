# Electronic Cookbook (ECB) Mode

## Introduction

The most naive mode of operation is called _Electronic Cookboook (ECB)_ mode. It divides the message into blocks $\mu\_1, \mu\_2, ..., \mu\_q$ with length $l\_b$, according to whatever block cipher is used, and then separately encrypts each block with the block cipher's encryption algorithm and the same key $k$. The final ciphertext is produced by concatenating the ciphertexts of each block.

![](<../../../../Cryptography/Private-Key Cryptography/Block Ciphers/Modes of Operation/Resources/Images/ECB Encryption.svg>)

Decryption is just the opposite - it divides the ciphertext into blocks $\sigma\_1, \sigma\_2, ..., \sigma\_q$ and decrypts each one separately. The original message is recovered by concatenating the decryptions of every ciphertext block.

![](<../../../../Cryptography/Private-Key Cryptography/Block Ciphers/Modes of Operation/Resources/Images/ECB Decryption.svg>)

## Security of ECB Mode

The ECB Mode is very simple so it comes as no surprise that it is not very secure.

```admonish
The ECB mode should *never* be used.
```

In particular, it is _not_ [CPA-secure](../../security-definitions/chosen-plaintext-attack-cpa.md), since it is entirely deterministic. Moreover, it is not even [semantically secure](../../security-definitions/index/semantic-security.md) because if a block is repeated in the plaintext, then the corresponding ciphertext block will also be repeated in the ciphertext which reveals a lot of information about the underlying message.

```admonish
A famous example of ECB's egregious insecurity is called the ECB penguin. Here is the original image of Linux's mascot [Tux](https://en.wikipedia.org/wiki/Tux_(mascot)), created by Larry Ewing:

![](Resources/Images/Tux.png)

And here is the same image encrypted with AES-128 using ECB mode:

![](Resources/Images/ECB%20Tux.png)

Not particularly secure, is it?
```
