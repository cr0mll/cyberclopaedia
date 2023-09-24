# The Cipher Block Chaining (CBC) Mode
Cipher Block Chaining is one of the most widely used modes of operation due to its security. 

Similarly to [ECB Mode](Electronic%20Cookbook%20(ECB)%20Mode.md), encryption begins by dividing the message into blocks $\mu_1, \mu_2, ..., \mu_q$ of length $l_b$. Unlike ECB, however, the next step is to generate a random *initialisation vector (IV)*, also of length $l_b$. The $i$-th ciphertext block is obtained by applying the block cipher's encryption function $\textit{Enc}_k$ to the XOR of the $i$-th message block with the previous ciphertext block. The first block is XOR-ed with the IV. 

$$\sigma_1 = \textit{Enc}_k(\mu_1 \oplus IV)$$
$$\sigma_i = \textit{Enc}_k(\mu_i \oplus c_{i-1})$$

Finally, the ciphertext of the message is obtained by concatenating all ciphertext blocks and prepending them with the initialisation vector. Because of this, the ciphertext in this encryption scheme is *longer* than the message by the length of one block - this is necessary for decryption.

![](Resources/Images/CBC%20Encryption.svg)

Conversely, decryption is the exact same process but carried out in reverse. It begins by parsing the ciphertext back into an initialisation vector and ciphertext blocks $\sigma_1, \sigma_2, ..., \sigma_q$, all of length $l_b$. The $i$-th message block is obtained by decrypting the $i$-th ciphertext block and XOR-ing the output with preceeding ciphertext block. The first block of the original message is recovered last by XOR-ing the decryption of its corresponding ciphertext block with the IV. 

$$\mu_i = \textit{Dec}_k(\sigma_i) \oplus \sigma_{i-1}$$
$$\mu_1 = \textit{Dec}_k(\sigma_1) \oplus IV$$

The original message is then recovered by concatenating all of the resulting message blocks.

![](Resources/Images/CBC%20Decryption.svg)

Interestingly enough, there is an optimisational discrepancy between the encryption and decryption algorithms in CBC. Namely, the decryption function is *parallelisable*, while the encryption function is not. This is the major drawback of CBC - every block needs to wait for the previous one to be encrypted so that it can be XOR-ed with the resulting ciphertext block, which means that CBC encryption can be slow. On the other hand, each block can be decrypted separately since all ciphertext blocks are already known beforehand.

# Security of CBC Mode
So long as the block cipher truly uses a [pseudorandom permutation (PRP)](../../../Primitives/Pseudorandom%20Permutations%20(PRPs).md) for its encryption function $\textit{Enc}_k$ and the initialisation vector is also chosen uniformly at random, CBC mode will be [CPA-secure](../../Security%20Notions/Chosen%20Plaintext%20Attack%20(CPA).md).

```admonish check collapsible=true title="Proof: CPA-Security of CBC Mode"
Suppose, towards contradiction, there is an efficient adversary Eve which after querying our block cipher in CBC mode $\text{CBC}[\textit{Enc}_k]$ with $q$ messages $m_1, m_2, ..., m_q$ and obtaining their corresponding ciphertexts $c_1, c_2, ..., c_q$ can determine with probability $\frac{1}{2} + \xi$, for some non-negligible $\xi$, if a ciphertext $c$ belongs to the message $m_a$ or $m_b$, where $m_a$ and $m_b$ are allowed to be one of $m_1, m_2, ..., m_q$.

For simplicity, we assume that all messages have the same length $l$ which is a multiple of the block length $l_b$ for the cipher. Consider the special case where the encrypted message is just one block long, i.e. $l = l_b$. In this case, CBC encryption reduces to passing a random string (the XOR of a string with a random string, i.e. the IV, is also a random string) to $\textit{Enc}_k$.

If instead of a PRP, the encryption function $\textit{Enc}_k$ were a truly random function, then Eve would have no real power and would only be able to guess with probability $\frac{1}{2}$ if a ciphertext $c$ belonged to a message $m_a$ or $m_b$. Therefore, we can construct a distinguisher $D$ which can distinguish between the output of a pseudorandom permutation and a truly random function. 

Essentially, if Eve guesses correctly which message was encrypted to obtain $c$, then the distinguisher is going to output $1$. Otherwise, it will output $0$. Given a truly random string $c$, Eve will guess correctly with probability $\frac{1}{2}$ and thus our distinguisher will output $1$ with probability only $\frac{1}{2}$. However, if $c$ was the encryption of one of two messages $m_a$ or $m_b$, then Eve would guess correctly with probability $\frac{1}{2} + \xi$, for some non-negligible $\xi$, and therefore our distinguisher would output $1$ with probability $\frac{1}{2} + \xi$ - it has a higher probability of outputting $1$ when given the output of a pseudorandom permutation than when given a truly random string. This means that this distinguisher can distinguish between a pseudorandom string a truly random string, which is a contradiction.

This specific case is in a proof by contradiction and is thus enough to establish the CPA-security of the CBC mode. Nevertheless, the same argument can be extended to messages of larger lengths since concatenations of random strings are also random strings and concatenations of pseudorandom strings are also pseudorandom strings.
```

### IV Reuse Attack
If two messages $m$ and $m'$ are CBC-encrypted with the same IV and the same key and you have only their ciphertexts $c$ and $c'$, then you can check if the two messages begin in the same way - if the first $j$ blocks of the messages $m$ and $m'$ are the same, then the first $j$ blocks of the ciphertexts $c$ and $c'$ would also be the same.