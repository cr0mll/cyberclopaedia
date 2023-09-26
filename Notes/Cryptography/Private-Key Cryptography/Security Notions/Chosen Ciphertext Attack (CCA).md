# Introduction
[Semantic](Ciphertext-Only%20Attack%20(COA)/Semantic%20Security.md) and [CPA-Security](Chosen%20Plaintext%20Attack%20(CPA).md) only provide protection against *passive* adversaries who can observe but cannot directly interfere with the communication between Alice and Bob. However, oftentimes an attacker Mallory *can* actually inject traffic between the two legitimate parties.

Consider the scenario where Alice encrypts a message $m$ and sends the resulting ciphertext $c$ to Bob. Mallory can tamper with the communication channel and so she can intercept $c$ and modify it into some other ciphertext $c'$. Bob will then decrypt $c'$ to a different message $m'$. Whilst Mallory does not know exactly what $m'$ is, she might be able to obtain some information about it from the way Bob behaves after receiving it. For example, Bob might be expecting a message in a very specific format and if the message he receives is *not* formatted correctly, he might take significantly longer to respond. Abusing this, Mallory will know if $c'$ decrypts to a correctly formatted message or not.

```admonish example
A more practical and grave example are [padding oracle attacks](../Block%20Ciphers/Padding%20Oracle%20Attack.md) which allow an attacker to completely break the security of [CBC encryption](../Block%20Ciphers/Modes%20of%20Operation/Cipher%20Block%20Chaining%20(CBC)%20Mode.md) and only require a way to know if a ciphertext decrypts to a valid message.
```

Essentially, a chosen ciphertext attack allows an adversary to force a legitimate party to decrypt arbitrary ciphertexts and to subsequently obtain certain information about the plaintext these ciphertexts decrypt to. 

# Chosen Ciphertext Attack (CCA)
It is very difficult to actually describe what information the adversary might be able to obtain about the decrypted messages and so this threat model assumes the worst case scenario - it assumes that Mallory is actually able to see the entire message $m'$ which $c'$ decrypts to.

The CCA threat model builds on [CPA](Chosen%20Plaintext%20Attack%20(CPA).md). In particular, Mallory can query both $\textit{Enc}_k$ *and* $\textit{Dec}_k$ and her goal is to obtain information about a message $m$ which is the decryption of a particular ciphertext $c$ without directly being able to query $\textit{Dec}_k(c)$. Notice, however, that since CCA builds on CPA, Mallory *is* allowed to query $\textit{Enc}_k$ which again means that any cipher which hopes to be CCA-secure *must* have a [non-deterministic encryption function](Chosen%20Plaintext%20Attack%20(CPA).md#admonition-necessity-of-randomness) $\textit{Enc}_k$.

# CCA-Security
With the description of the CCA-model, we can now give a definition of what it means for a cipher to be secure under it.

```admonish danger title="Definition: CCA-Security"
The adversary Mallory is allowed to make two types of queries:
- Encryption query - Mallory can query $\textit{Enc}_k$ with $q$ messages $m_1, m_2, ..., m_q$ in order to obtain their corresponding ciphertexts $c_1, c_2, ..., c_q$.
- Decryption query - Mallory can also query $\textit{Dec}_k$ with $q'$ ciphertexts $c_1', c_2', ..., c_{q'}'$ in order to obtain their decryptions $m_1', m_2', ..., m_{q'}'$. 

Finally, Mallory chooses two messages $m_a, m_b$, which *can* be one of $m_1, m_2, ..., m_q$ or $m_1', m_2', ..., m_{q'}'$, and is then presented with a ciphertext $c$ which is either the encryption of $m_a$ or $m_b$. Her goal is to determine whether $c$ belongs to $m_a$ or $m_b$, but she is *not* allowed to directly query $\textit{Dec}_k(c)$. 

The cipher $(\textit{Enc}, \textit{Dec})$ is *CCA-secure*, if for all keys $k \in \mathcal{K}$, Mallory cannot guess with probability better than $\frac{1}{2} + \textit{negl}(n)$ whether $c$ is the encryption of $m_a$, or $m_b$, i.e.

$$\Pr_{k \leftarrow_R \mathcal{K}, m \leftarrow_R \{m_a, m_b\}}[\textit{Mallory}(\textit{Enc}_k(m)) = m] \le \frac{1}{2} + \textit{negl}(n)$$
```

```admonish tip title="Definition Breakdown"
As with [CPA](Chosen%20Plaintext%20Attack%20(CPA).md), Mallory is allowed to query $\textit{Enc}_k$ with messages $m_1, m_2, ..., m_q$ of her choice. She is additionally allowed to query $\textit{Dec}_k$ with ciphertexts $c_1, c_2, ..., c_q$ of her choice. Mallory is also allowed to pick the messages $m_a$ and $m_b$ herself and they can even be two of the previously queried messages or two of the decryptions of the queried ciphertexts, or both. She is then given a ciphertext $c$ and has to determine if it is an encryption of $m_a$ or $m_b$. The only restriction is that Mallory cannot directly query $\textit{Dec}_k$ with $c$, for otherwise no cipher would ever satisfy the definition.

A cipher is CCA-secure if no matter what Mallory does, she cannot determine whether $c$ is the encryption of $m_a$ or $m_b$ with probability significantly better than $\frac{1}{2}$.
```

Although there are ciphers which provide CCA-security, they are not used in practice because they provide no benefit in either security or efficiency over ciphers which satisfy the even stronger notion of [Authenticated Encryption](../Authenticated%20Encryption.md).