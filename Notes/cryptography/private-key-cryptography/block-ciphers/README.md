# Block Ciphers

## Introduction

Due to their ubiquitous use, block ciphers are often called the work horse of cryptography. They operate on plaintexts of a fixed size, called _blocks_, and produce ciphertexts of the same length.

{% hint style="danger" %}
<mark style="color:red;">**Definition: Block Cipher**</mark>

A _**block cipher**_ is a Shannon cipher $$(\textit{Enc}, \textit{Dec})$$ with identical message and ciphertext spaces, i.e. $$\mathcal{M} \equiv \mathcal{C}$$, such that for every key $$k \in \mathcal{K}$$ the encryption function $$\textit{Enc}_k$$ is a pseudorandom permutation over $$\mathcal{M}$$ and the decryption function $$\textit{Dec}_k$$ is its inverse.
{% endhint %}

<details>

<summary><strong>Definition Breakdown</strong></summary>

The construction of a block cipher is rooted in pseudorandom permutations (PRPs), hence why the plaintexts (also known as the _data blocks_) and the ciphertexts are always of the same length. Furthermore, since every PRP is required to be invertible, there is a natural implementation for the decryption function which is simply the inverse of the PRP used for encryption.

</details>

## Implementation

In practice, block ciphers are built by iteration in the so-called rounds using a _round function_ and each block cipher uses a different number of rounds.

The first phase of encryption is the _key expansion_. The key $$k$$ (also called the _master key_) is expanded into several _round keys_ $$k_1, k_2, ..., k_d$$ of size $$n'$$ - one for each round. At each round, the round key $$k_i$$ is used in the round function $$R$$ together with the output of the previous round. The first round uses the initial plaintext as input.

![](<../../../Cryptography/Private-Key Cryptography/Block Ciphers/Resources/Images/Block Cipher Encryption.svg>)

Similarly, decryption also begins by expanding the master key $$k$$ into the same set of round keys $$k_1, k_2, ..., k_d$$. This time, however, the keys are used in reverse order together with the inverse of the round function - $$R^{-1}$$.

![](<../../../Cryptography/Private-Key Cryptography/Block Ciphers/Resources/Images/Block Cipher Decryption.svg>)

The reason for constructing practical block ciphers is two fold. First, encryption and decryption use more or less the same algorithm which makes it easy to create specialised hardware for them, drastically speeding up these operations.

{% hint style="info" %}
The Advanced Encryption Standard (AES) is the most ubiquitous block cipher in the world and most CPUs have dedicated hardware and instructions for it.
{% endhint %}

Second, the round function $$R$$ can be a very simple operation and it might not even be considered secure on its own! Heuristic evidence suggests that the security of a block cipher comes from the _iteration_ of the round function and not necessarily from the round function itself.

{% hint style="info" %}
Although iteration can be used to achieve security, not all round functions can be used. For example, no matter how many times one iterates a linear round function, it will never be secure.
{% endhint %}
