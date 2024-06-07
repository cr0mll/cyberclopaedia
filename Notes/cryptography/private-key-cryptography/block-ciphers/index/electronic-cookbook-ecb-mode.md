# Electronic Cookbook (ECB) Mode

## Introduction

The most naive mode of operation is called _Electronic Cookboook (ECB)_ mode. It divides the message into blocks $$\mu_1, \mu_2, ..., \mu_q$$ with length $$l_b$$, according to whatever block cipher is used, and then separately encrypts each block with the block cipher's encryption algorithm and the same key $$k$$. The final ciphertext is produced by concatenating the ciphertexts of each block.

![](<../../../../Cryptography/Private-Key Cryptography/Block Ciphers/Modes of Operation/Resources/Images/ECB Encryption.svg>)

Decryption is just the opposite - it divides the ciphertext into blocks $$\sigma_1, \sigma_2, ..., \sigma_q$$ and decrypts each one separately. The original message is recovered by concatenating the decryptions of every ciphertext block.

![](<../../../../Cryptography/Private-Key Cryptography/Block Ciphers/Modes of Operation/Resources/Images/ECB Decryption.svg>)

## Security of ECB Mode

The ECB Mode is very simple so it comes as no surprise that it is not very secure.

{% hint style="warning" %}
The ECB mode should _never_ be used.
{% endhint %}

In particular, it is _not_ [CPA-secure](../../security-definitions/chosen-plaintext-attack-cpa.md), since it is entirely deterministic. Moreover, it is not even [semantically secure](../../security-definitions/index/semantic-security.md) because if a block is repeated in the plaintext, then the corresponding ciphertext block will also be repeated in the ciphertext which reveals a lot of information about the underlying message.

<details>

<summary><mark style="color:purple;"><strong>Example: Insecurity of the ECB Mode</strong></mark></summary>

A famous example of ECB's egregious insecurity is called the ECB penguin. Here is the original image of Linux's mascot [Tux](https://en.wikipedia.org/wiki/Tux\_\(mascot\)), created by Larry Ewing:

<img src="../../../../.gitbook/assets/Tux.png" alt="" data-size="original">

And here is the same image encrypted with AES-128 using ECB mode:

<img src="../../../../.gitbook/assets/ECB Tux.png" alt="" data-size="original">

Not particularly secure, is it?

</details>
