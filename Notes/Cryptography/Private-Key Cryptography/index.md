# Introduction
Private-key cryptography uses the same secret key for both encryption and decryption. It is important that modern cryptography is usually concerned entirely with the encryption and decryption of binary data, i.e. binary strings. That is why both the message, the key and the encrypted message are represented as binary strings of 1s and 0s.

A private-key encryption scheme has an algorithm for encryption and decryption. The message to be encrypted is called the *plaintext* and the resulting string after encryption is called the *ciphertext*.

```admonish danger title="Formal Definition: Shannon Cipher"
Given a key-length $n \in \mathbb{N}$, a plaintext length function $l: \mathbb{N} \to \mathbb{N}$ and a ciphertext length function $C: \mathbb{N} \to \mathbb{N}$, a *valid private-key encryption scheme* or *Shannon cipher* is a pair of polynomial-time computable functions $(\textit{Enc}, \textit{Dec})$ such that for every key $k \in \mathcal{K}$ and plaintext $m \in \mathcal{M}$, it is true that:

$$\textit{Dec}(k, \textit{Enc}(k,m)) = m$$

The first parameter, i.e. the key $k$, can also be denoted as a subscript - $\textit{Dec}_k$ and $\textit{Enc}_k$.

![](Resources/Images/Private-Key%20Encryption%20Scheme.svg)

The set of all possible keys is called the *key space* and is denoted by $\mathcal{K} \subseteq \{0,1\}^n$. The set of all possible plaintexts is called the *message space* and is denoted by $\mathcal{M} \subseteq \{0,1\}^{l(n)}$. The set of all possible ciphertexts is called the *ciphertext space* and is denoted by $\mathcal{C} \subseteq \{0,1\}^{C(n)}$.

```

```admonish tip title="Definition Breakdown"
The encryption function is denoted by $\textit{Enc}$ and the decryption function is called $\textit{Dec}$. The first function, $\textit{Enc}$,  takes a key $k$ and a plaintext $m$ and outputs a ciphertext $c$, while the latter, $\textit{Dec}$, does the opposite - it takes a key $k$ and a ciphertext $c$ and produces the plaintext $m$ which was encrypted to get the ciphertext.

The key $k$, the plaintext $m$ and the ciphertext $c$ are all binary strings and their lengths, i.e. the number of bits in them, are denoted by $n$, $l(n)$ and $C(n)$, respectively. For simplicity, these are often substituted by just $n$, $l$ and $C$.

The term *polynomial-time computable* means that the encryption and decryption functions should be fast to compute for long keys and messages, which is not an unreasonable requirement. After all, encryption and decryption would be useless if we could never hide or see the message's contents, even if they were intended for us.

The final requirement, i.e. that $\textit{Dec}_k(\textit{Enc}_k(m)) = m$, is essential and is called the *correctness property*. It tells us that under any Shannon cipher, the encryption function is [one-to-one](../Mathematical%20Prerequisites.md#admonition-injection-surjection-and-bijection) which means that every no two plaintexts can be encrypted to the same ciphertext if the same key $k$ is used. It might seem obvious that this should be true, but it is *not* the case for [hash functions](../Hash%20Functions/index.md), for example, and so hash functions are *not* valid private-key encryption schemes.
```

