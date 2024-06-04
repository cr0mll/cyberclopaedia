# Private-Key Cryptography

Private-key cryptography uses the same secret key for both encryption and decryption. It is important that modern cryptography is usually concerned entirely with the encryption and decryption of binary data, i.e. binary strings. That is why both the message, the key and the encrypted message are represented as binary strings of 1s and 0s.

A private-key encryption scheme has an algorithm for encryption and decryption. The message to be encrypted is called the _plaintext_ and the resulting string after encryption is called the _ciphertext_.

{% hint style="danger" %}
<mark style="color:red;">**Definition: Shannon Cipher**</mark>

Given a key-length $$n \in \mathbb{N}$$, a plaintext length function $$l: \mathbb{N} \to \mathbb{N}$$ and a ciphertext length function $$C: \mathbb{N} \to \mathbb{N}$$, a _valid private-key encryption scheme_ or _Shannon cipher_ is a pair of polynomial-time computable functions $$(\textit{Enc}, \textit{Dec})$$ such that for every key $$k \in \mathcal{K}$$ and plaintext $$m \in \mathcal{M}$$, it is true that:

$$\textit{Dec}(k, \textit{Enc}(k,m)) = m$$

The first parameter, i.e. the key $$k$$, can also be denoted as a subscript - $$\textit{Dec}_k$$ and $$\textit{Enc}_k$$.

<img src="../../.gitbook/assets/Private-Key Encryption Scheme.svg" alt="" data-size="original">

The set of all possible keys is called the _key space_ and is denoted by $$\mathcal{K} \subseteq \{0,1\}^n$$. The set of all possible plaintexts is called the _message space_ and is denoted by $$\mathcal{M} \subseteq \{0,1\}^{l(n)}$$. The set of all possible ciphertexts is called the _ciphertext space_ and is denoted by $$\mathcal{C} \subseteq \{0,1\}^{C(n)}$$.
{% endhint %}

<details>

<summary><strong>Definition Breakdown</strong></summary>

The encryption function is denoted by $$\textit{Enc}$$ and the decryption function is called $$\textit{Dec}$$. The first function, $$\textit{Enc}$$, takes a key $$k$$ and a plaintext $$m$$ and outputs a ciphertext $$c$$, while the latter, $$\textit{Dec}$$, does the opposite - it takes a key $$k$$ and a ciphertext $$c$$ and produces the plaintext $$m$$ which was encrypted to get the ciphertext.

The key, the plaintext and the ciphertext are all binary strings and their lengths, i.e. the number of bits in them, are denoted by $$n$$, $$l(n)$$ and $$C(n)$$, respectively. For simplicity, these are often substituted by just $$n$$, $$l$$ and $$C$$.

The term _polynomial-time computable_ means that the encryption and decryption functions should be fast to compute for long keys and messages, which is not an unreasonable requirement. After all, encryption and decryption would be useless if we could never hide or see the message's contents, even if they were intended for us.

The final requirement, i.e. that $$\textit{Dec}_k(\textit{Enc}_k(m)) = m$$, is essential and is called the _correctness property_. It tells us that under any Shannon cipher, the encryption function is one-to-one which means that every no two plaintexts can be encrypted to the same ciphertext if the same key $$k$$ is used. It might seem obvious that this should be true, but it is _not_ the case for hash functions, for example, and so hash functions are _not_ valid private-key encryption schemes.

</details>
