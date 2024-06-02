# Counter (CTR) Mode

## The Counter (CTR) Mode

Counter (CTR) mode takes a different approach to most other modes of operation. It does not even use the block cipher's encryption function $\textit{Enc}\_k$ on the message itself!

The encryption process begins by dividing the message into blocks $\mu\_1, \mu\_2, ..., \mu\_q$ with length $l\_b$. Then, an initialisation vector (IV) of length $\frac{3}{4}l\_b$ is randomly generated. However, instead of passing the $i$-th block to $\textit{Enc}\_k$, CTR mode takes the IV and appends to it a counter $i$ encoded as a binary string of length $\frac{1}{4}l\_b$ and inputs _this_ into $\textit{Enc}\_k$. The $i$-th message block is then XOR-ed with the output to produce the $i$-th ciphertext block:

$$\sigma_i = \mu_i \oplus \textit{Enc}_k(IV||i)$$

The final ciphertext is obtained by concatenating all ciphertext blocks and prepending them with the initialisation vector, which is necessary for decryption just as with [CBC mode](cipher-block-chaining-cbc-mode.md).

![](<../../../../Cryptography/Private-Key Cryptography/Block Ciphers/Modes of Operation/Resources/Images/CTR Encryption.svg>)

This process essentially turns a block cipher into a [stream cipher](../../stream-ciphers/) where the IV and the counter are used to generate a keystream which is then XOR-ed with the message.

The decryption procedure is almost equivalent - the IV is extracted from the ciphertext $c$ and the rest of it is divided into ciphertext blocks $\sigma\_1, \sigma\_2, ..., \sigma\_q$. The $i$-th ciphertext block is XOR-ed with the output of, notice, $\textit{Enc}\_k$ after passing it the concatenation of the IV and $i$ encoded as a binary string of length $\frac{1}{4}l\_b$.

$$\mu_i = \sigma_i \oplus \textit{Enc}_k(IV||i)$$

![](<../../../../Cryptography/Private-Key Cryptography/Block Ciphers/Modes of Operation/Resources/Images/CTR Decryption.svg>)

That's right - the decryption function $\textit{Dec}\_k$ of the block cipher is not even used! This means that the encryption function $\textit{Enc}\_k$ does _not_ need to even be invertible, i.e. it does not need to be a [pseudorandom permutation (PRP)](../../../randomness/pseudorandom-permutations-prps.md), but can simply be a [pseudorandom function (PRF)](../../../randomness/pseudorandom-function-generators-prfgs.md). This is only one major advantage of CTR mode. Another one is the fact that both encryption and decryption are parallelisable, which makes them excellent candidates for optimisation. These two factors, combined with the security provided by this mode, are the reason for CTR's extensive use.

## Security of CTR Mode

So long as the initialisation vector is chosen uniformly at random and the block cipher used is secure, i.e. it uses a pseudorandom function (or permutation) for its $\textit{Enc}\_k$ function, CTR mode will be [CPA-secure](../../security-definitions/chosen-plaintext-attack-cpa.md).

```admonish
First suppose, towards contradiction, that there is an efficient adversary Eve that after querying $\textit{Enc}_k$ with $q$ messages $m_1, m_2, ..., m_q$ and obtaining their ciphertexts $c_1, c_2, ..., c_q$, can distinguish with probability $\frac{1}{2} + \textit{nonnegl}(n)$ if a ciphertext $c$ is the encryption of $m_a$ or $m_b$, for some messages $m_a$ and $m_b$, which are also allowed to be one of the previously queried messages. 

Consider the case where the messages $m_a$ and $m_b$ are only a single block long. If instead of the PRF $\textit{Enc}_k$, the CTR encryption used a truly random function $R$, then Eve would lack any information and so she would only be able guess at best with probability $\frac{1}{2}$ whether a ciphertext $c$ belongs to $m_a$ or $m_b$. This, however, is a contradiction because she would be able to distinguish with non-negligible probability the output of a PRF from the output of a truly random function. Therefore, no such adversary can exist.

This reasoning assumes that the IV is never reused, but since the IV is supposed to be chosen uniformly at random, this *can* happen. So we need to show that this happens with only negligible probability.

Indeed, the adversary Eve makes $q$ queries which means $q$ messages with $q$ IV's. Each IV is chosen uniformly from $\{0,1\}^{\frac{3}{4}l_b}$, so the probability that an IV is repeated is $\frac{q^2}{2^{\frac{3}{4}l_b + 1}}$ which is negligible, since Eve must be efficient and therefore $q$ needs to be polynomial.
```

#### IV Reuse Attack

If you have two ciphertexts $c$ and $c'$ that are the CTR-mode encryptions of two messages $m$ and $m'$ which where encrypted with the same initialisation vector $IV$ and the same secret key $k$ and you know one of the messages - for example $m$ - then you can easily decrypt the other message $m'$.

The first step is to XOR the two ciphertexts $c$ and $c'$ to obtain the XOR of the two messages $m$ and $m'$, since the XOR of something with itself is 0 and XOR-ing with 0 has no effect.

$$\begin{cases}c = m \oplus (\textit{Enc}_k(IV||1) || \textit{Enc}_k(IV||2) \cdots) \\ c' = m' \oplus (\textit{Enc}_k(IV||1) || \textit{Enc}_k(IV||2) \cdots)\end{cases} \implies$$

$$\begin{align}c \oplus c' &= \\ &= (m \oplus (\textit{Enc}_k(IV||1) || \textit{Enc}_k(IV||2) \cdots)) \oplus (m' \oplus (\textit{Enc}_k(IV||1) || \textit{Enc}_k(IV||2) \cdots)) \\ &= (m \oplus m') \oplus ((\textit{Enc}_k(IV||1) || \textit{Enc}_k(IV||2) \cdots) \oplus (\textit{Enc}_k(IV||1) || \textit{Enc}_k(IV||2) \cdots))\\ &= m \oplus m'\end{align}$$

The second and final step is to XOR this result with the known message $m$ to recover the unknown message $m'$:

$$(m \oplus m') \oplus m = (m \oplus m) \oplus m' = m'$$

This attack clearly illustrates that initialisation vectors should _never_ be repeated.

```admonish
Even if the IV is chosen uniformly at random, there is still a chance that it is repeated and security is broken. Nevertheless, the number of possible IVs is usually so large that the probability of this actually happening is negligible.
```
