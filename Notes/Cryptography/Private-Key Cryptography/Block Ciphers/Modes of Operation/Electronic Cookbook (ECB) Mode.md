# Introduction
The most naive mode of operation is called *Electronic Cookboook (ECB)* mode. It divides the message into blocks $\mu_1, \mu_2, ..., \mu_q$ with length $l_b$, according to whatever block cipher is used, and then separately encrypts each block with the block cipher's encryption algorithm and the same key $k$. The final ciphertext is produced by concatenating the ciphertexts of each block.

![](Resources/Images/ECB%20Encryption.svg)

Decryption is just the opposite - it divides the ciphertext into blocks $\sigma_1, \sigma_2, ..., \sigma_q$ and decrypts each one separately. The original message is recovered by concatenating the decryptions of every ciphertext block.

![](Resources/Images/ECB%20Decryption.svg)

# Security of ECB Mode
The ECB Mode is very simple so it comes as no surprise that it is not very secure. 

```admonish warning
The ECB mode should *never* be used.
```

In particular, it is *not* [CPA-secure](../../Security%20Definitions/Chosen%20Plaintext%20Attack%20(CPA).md), since it is entirely deterministic. Moreover, it is not even [semantically secure](../../Security%20Definitions/Ciphertext-Only%20Attack%20(COA)/Semantic%20Security.md) because if a block is repeated in the plaintext, then the corresponding ciphertext block will also be repeated in the ciphertext which reveals a lot of information about the underlying message. 

```admonish example
A famous example of ECB's egregious insecurity is called the ECB penguin. Here is the original image of Linux's mascot [Tux](https://en.wikipedia.org/wiki/Tux_(mascot)), created by Larry Ewing:

![](Resources/Images/Tux.png)

And here is the same image encrypted with AES-128 using ECB mode:

![](Resources/Images/ECB%20Tux.png)

Not particularly secure, is it?
```
