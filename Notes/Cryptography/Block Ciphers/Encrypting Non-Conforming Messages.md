# Introduction
A non-conforming message is a message whose length is not evenly divisible by the block size. For example, you might have a message of size 18 bytes and a block size of 16 bytes. In this case, there are two main ways to resolve the issue.

## Message Padding
Padding allows for the encryption of messages of arbitrary lengths, even ones which are shorter than a single block. It is used to expand a message in order to fill a complete block by appending bytes to the plaintext and it is a highly standardised procedure. 

The most common padding algorithm is described by PKCS#7 in RFC 5652.

Given a block size, $n$, and a message of length $m$, the message is padded with $n-m$ number of bytes of value $n-m$.  A concrete example with 16-byte blocks is the following:
- If there's is one byte left until the message length is divisible by 16 - for example, it is 17 or 33 bytes long - then pad the message with 15 bytes `0x0f` (15 in decimal).
- If there are two bytes left until the message length is divisible by 16 - for example, it is 18 or 34 bytes long - then pad the message with 14 bytes `0x0e` (14 in decimal).
- If there are three bytes left until the message length is divisible by 16, then pad the message with 13 bytes `0x0d` (13 in decimal), and so on.

If the message length is already divisible by the block size, then an additional *block* containing bytes with value equal to the block size is appended in order to signify to the decryption algorithm whether the last block is part of the plaintext or just padding. In the above example, if the message length was already divisible by 16, then another 16 bytes of value `0x10` would have been appended to it.

Decryption is fairly simple and works by first deciphering all the unpadded blocks. Subsequently, the last block is decrypted and the last bytes of the resulting plaintext are checked for conformity with the aforementioned scheme. If such is not found, the message is rejected. Otherwise, the padding bytes are stripped before returning the plaintext.

## Ciphertext Stealing
Ciphertext stealing is another technique for encrypting messages of arbitrary length. Whilst more complex, it has several benefits:
- Plaintexts are allowed to be of any *bit* length and are not restrained to bytes - it is possible to encrypt a message which is 155 bits long.
- Ciphertext have the same length as plaintexts.

In CBC mode, ciphertext stealing extends the last incomplete plaintext block by taking bits from the previous ciphertext block, thus splitting the penultimate ciphertext block. Once the last plaintext block is complete, it is encrypted and its ciphertext is placed as the penultimate ciphertext block. Now, the first bits (the ones which were not appended) of the broken ciphertext block are placed at the end as a reduced ciphertext block, meaning that the last ciphertext block has a length less than the block size.

![](../Resources/Images/Block_Cipher_Ciphertext_Stealing.png)

