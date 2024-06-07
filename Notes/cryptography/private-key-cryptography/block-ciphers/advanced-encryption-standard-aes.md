# Advanced Encryption Standard (AES)

## Introduction

The Advanced Encryption Standard (AES) is an encryption standard which has been ubiquitously adopted due to its security and has been standardised by NIST. It is comprised of three symmetric block ciphers which all take blocks of size 128 bits and output blocks of the same size. AES has three versions depending on the length of the key it can take. These are AES-128, AES-192, and AES-256, for 128-, 192-, and 256-bit keys, respectively. While the different AES versions may use a different length for the initial key, all round keys derived from it will still be the same size as the block - 128 bits.

The key length also determines the number of rounds that each 128-bit block goes through:

| Key Length | Number of Rounds |
| :--------: | :--------------: |
|     128    |        10        |
|     192    |        12        |
|     256    |        14        |

AES operates on a 4x4 matrix called the State ( $S$ ). Each of its elements contains a single byte.

$$S = \begin{bmatrix} s_{0,0} & s_{0,1} & s_{0,2} & s_{0,3} \\ s_{1,0} & s_{1,1} & s_{1,2} & s_{1,3} \\ s_{2,0} & s_{2,1} & s_{2,2} & s_{2,3} \\ s_{3,0} & s_{3,1} & s_{3,2} & s_{3,3} \\ \end{bmatrix}$$

At the beginning of both the encryption and decryption algorithms, the state is populated with the 16 bytes from the input block in the following way:

$$S[r, c] = \text{in}[4r + c]$$

The indices $$r$$ and $$c$$ denote the row and the column of the cell currently being populated.

At the end, the final State is mapped back to a 16-byte output array by a similar procedure:

$$\text{out}[4r + c] = S[r, c]$$

## AES Operations

AES has 4 basic of operations: _SubBytes_, _ShiftRows_, _MixColumns_ and _AddRoundKey_. Encryption and decryption boil down to stringing these operations in a certain order. Note that for decryption we have the inverse of these operations: _InvSubBytes_, _InvShiftRows_ and _InvMixColumns_ (AddRoundKey is its own inverse).

#### SubBytes

The SubBytes operation substitutes each element of the state with one from a predefined 16x16 lookup table called the S-box. This is an essential part of the cipher because it introduces _complexity_ which makes it difficult to deduce any information about the key form the ciphertext. This complexity is based in non-linearity. Basically, complicated non-linear function is applied to every byte in the state. To speed up the process, the substitutions have been pre-computed for the byte values `0x00` to `0xff` and summarised into the S-box. Note that there are two versions of the S-box - one for encryption and the other for decryption.

![](<../../../Cryptography/Private-Key Cryptography/Block Ciphers/Resources/Images/AES/AES S-Box.png>)

![](<../../../Cryptography/Private-Key Cryptography/Block Ciphers/Resources/Images/AES/AES Inverse S-box.png>)

The row is specified by the most significant nibble and the column by the least significant.

#### ShiftRows & MixColumns

These two operations introduce _diffusion_ to the AES algorithm. For a cipher to be as secure as possible, changes in the plaintext should propagate to many bits in the ciphertext. Ideally, changing one bit of the plaintext should alter at least half the bits in the ciphertext. This is known as the [Avalanche effect](https://en.wikipedia.org/wiki/Avalanche\_effect).

ShiftRows is the simplest of AES operations and ensures that the columns of the State are _not_ encrypted independently. This operation leaves the first row unchanged and shifts the second row one byte to the left, wrapping around. The third row is similarly shifted left by two bytes, again wrapping around, and the fourth row is shifted 3 bytes to left, wrapping around:

$$\begin{bmatrix} s_{0,0} & s_{0,1} & s_{0,2} & s_{0,3} \\ s_{1,0} & s_{1,1} & s_{1,2} & s_{1,3} \\ s_{2,0} & s_{2,1} & s_{2,2} & s_{2,3} \\ s_{3,0} & s_{3,1} & s_{3,2} & s_{3,3} \\ \end{bmatrix} \overset{\text{ShiftRows}}{\Rightarrow} \begin{bmatrix} s_{0,0} & s_{0,1} & s_{0,2} & s_{0,3} \\ s_{1,1} & s_{1,2} & s_{1,3} & s_{1,0} \\ s_{2,2} & s_{2,3} & s_{2,0} & s_{2,1} \\ s_{3,3} & s_{3,0} & s_{3,1} & s_{3,2} \\ \end{bmatrix}$$

MixColumns is a lot more complex and involves matrix multiplication in Rijndael's Galois field between the State and a pre-computed matrix. The key takeaway is that every byte affects all other bytes in the same column.

#### AddRoundKey

The AddRoundKey operation is quite simple - all it does is XOR the state with the current round key:

$$\begin{bmatrix} s_{0,0} & s_{0,1} & s_{0,2} & s_{0,3} \\ s_{1,0} & s_{1,1} & s_{1,2} & s_{1,3} \\ s_{2,0} & s_{2,1} & s_{2,2} & s_{2,3} \\ s_{3,0} & s_{3,1} & s_{3,2} & s_{3,3} \\ \end{bmatrix} \bigoplus \begin{bmatrix} k_{0,0} & k_{0,1} & k_{0,2} & k_{0,3} \\ k_{1,0} & k_{1,1} & k_{1,2} & k_{1,3} \\ k_{2,0} & k_{2,1} & k_{2,2} & k_{2,3} \\ k_{3,0} & k_{3,1} & k_{3,2} & k_{3,3} \\ \end{bmatrix} \equiv \begin{bmatrix} s_{0,0} \oplus k_{0,0} & s_{0,1} \oplus k_{0,1} & s_{0,2} \oplus k_{0,2} & s_{0,3} \oplus k_{0,3} \\ s_{1,0} \oplus k_{1,0} & s_{1,1} \oplus k_{1,1} & s_{1,2} \oplus k_{1,2} & s_{1,3} \oplus k_{1,3} \\ s_{2,0} \oplus k_{2,0} & s_{2,1} \oplus k_{2,1} & s_{2,2} \oplus k_{2,2} & s_{2,3} \oplus k_{2,3} \\ s_{3,0} \oplus k_{3,0} & s_{3,1} \oplus k_{3,1} & s_{3,2} \oplus k_{3,2} & s_{3,3} \oplus k_{3,3} \\ \end{bmatrix}$$

## Encryption

![](<../../../Cryptography/Private-Key Cryptography/Block Ciphers/Resources/Images/AES/AES Encryption.svg>)

First is the Key Expansion phase where $$n + 1$$ keys of length 128 bits are derived from the master key. Before the first round, an AddRoundKey is performed with the plaintext and the first generated key. Then comes the round chain. Every round, apart from the last one, is comprised of a SubBytes, ShiftRows, MixColumns and an AddRoundKey operation in that order. The MixColumns operation is dropped from the last round.

## Decryption

Decryption involves running the inverse round operations and in reverse order. Again, the Key Expansion phase generates the same $$n + 1$$ round keys as with encryption, but these keys are used in reverse order. Before the first round, the an AddRoundKey operation is performed on the ciphertext and the first generated key:

![](<../../../Cryptography/Private-Key Cryptography/Block Ciphers/Resources/Images/AES/AES Decryption.svg>)

The InvMixColumns operation is again dropped from the final round.
