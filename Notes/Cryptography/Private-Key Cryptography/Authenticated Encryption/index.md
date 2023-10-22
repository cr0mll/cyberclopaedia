# Introduction
Most of the time, confidentiality is *not* enough - it needs to be combined with integrity in order for an application to be secure. So, even if an encryption scheme is [CCA-secure](../Security%20Definitions/Chosen%20Ciphertext%20Attack%20(CCA).md), there is still room for ciphertext forgery. This necessitates even stronger security notions which are satisfied by *authenticated encryption schemes*.

```admonish danger title="Definition: Authenticated Encryption (AE-Security)"
A cipher $(\textit{Enc}, \textit{Dec})$ is an *authenticated encryption* scheme or is *AE-secure* if it is [CPA-secure](Security%20Notions/Chosen%20Plaintext%20Attack%20(CPA).md) and provides [ciphertext integrity (CI)](Security%20Notions/Ciphertext%20Integrity%20(CI).md).
```

AE-security is the most widely adopted security notion and is ubiquitous in web applications. It is *stronger* than [CCA-security](../Security%20Definitions/Chosen%20Ciphertext%20Attack%20(CCA).md) - the constructs which satisfy AE-security also satisfy CCA-security. However, there is no real efficiency difference between ciphers which are AE-secure and ciphers which are only CCA-secure.

```admonish abstract title="Theorem: AE-Security implies CCA-Security"
Every AE-secure cipher is also CCA-secure.
```

```admonish check collapsible=true title="Proof: AE-Security implies CCA-Security"
Let $(\textit{Enc}, \textit{Dec})$ be an AE-secure cipher and let $\textit{Mallory}$ be a CCA-adversary. In particular, suppose that Mallory makes $q_e$ encryption queries to obtain the plaintext-ciphertext pairs $(m_1,c_1), (m_2,c_2), ..., (m_{q_e},c_{q_e})$ and also makes $q_d$ decryption queries to obtain the ciphertext-plaintext pairs $(c_1', m_1'), (c_2', m_2'), ..., (c_{q_d}', m_{q_d}')$. 

Since the cipher is AE-secure and thus provides ciphertext integrity, the probability that in a given decryption query Mallory finds a ciphertext $c_j'$ such that $\textit{Dec}_k(c_j') \ne \textbf{error}$ is negligible. Mallory sumbits $q_d$ queries, so the probability that any of them turn out to be valid is $q_d\cdot\textit{negl}(n)$, which is also negligible. This means that the decryption queries do not help Mallory in any way and can be ignored, thereby reducing the CCA scenario to a CPA one. AE-security provides CPA-security by definition, which completes the proof.
```

This explains why ciphers which are only CCA-secure are rarely used in practice - why would you opt for less security when there is not even an efficiency benefit?

# Implementation
There are many ways to implement authenticated encryption. Some include combining a CPA-secure cipher with a secure 

## Construction from a Cipher and a MAC
 AE-secure encryption schemes can be constructed by combining a [CPA-secure](../Security%20Definitions/Chosen%20Plaintext%20Attack%20(CPA).md) cipher $(\textit{Enc}', \textit{Dec}')$with a [CMA-secure](../Message%20Authentication%20Codes%20(MACs)/index.md) message authentication code system $(\textit{Sign}, \textit{Verify})$. Such approaches use two separate keys - $k_E$ for encryption / decryption and $k_S$ for message signing and verification. These keys *must* be independent of each other.
 
 However, it turns out that not all ways of combining these two systems yield an authenticated encryption and even if the correct approach is used, the keys $k_E$ and $k_S$ must still be completely independent, lest AE-security is broken.

### Encrypt-and-Sign
In this approach, encryption and message signing are carried out independently from each other and in parallel.  The supposedly AE-secure cipher $(\textit{Enc}, \textit{Dec})$ is constructed by encrypting the message $m$ with some encryption function $\textit{Enc}'$ to produce a ciphertext $c$. The message is also separately signed by the MAC and the resulting tag $\tau$ is appended to $c$.

$$c \coloneqq \textit{Enc}_{k_E}'(m)$$
$$\tau \coloneqq \textit{Sign}_{k_S}(m)$$

The final ciphertext is the concatenation of $c$ and the message tag $\tau$, i.e.

$$\textit{Enc}(k_E, k_S, m) \coloneqq c||\tau$$

To decrypt the ciphertext $c$, the decryption function first parses it back into a message ciphertext and a message tag $\tau$. It then decrypts the ciphertext using $\textit{Dec}_{k_E}'$ to obtain the message $m$. Finally, it verifies the decrypted message with the tag $\tau$. If the message is valid, then it is returned. Otherwise, an error is produced.

$$\textit{Dec}(k_E, k_S, c||\tau) = \begin{cases}\textit{Dec}_{k_E}'(c), \text{ if } \textit{Dec}_{k_E}'(c) \ne \textbf{error} \text{ and } \textit{Verify}(k_S, \textit{Dec}_{k_E}'(c), \tau) = 1\\ \textbf{error}, \text{ otherwise}\end{cases}$$

This is certainly a good attempt at constructing an authenticated encryption but it fails horribly.

```admonish warning
The Encrypt-and-Sign approach is *not* AE-secure.
```

Since the message $m$ is signed directly before being encrypted, nothing is stopping the tag $\tau$ from leaking information about it (CMA-secure MACs provide no secrecy guarantees). For example, a MAC might be CMA-secure but have tags whose first bit is always identical to the first bit of the message. This means that the Encrypt-and-Sign method might not even be [semantically security](../Security%20Definitions/Ciphertext-Only%20Attack%20(COA)/Semantic%20Security.md).

Moreover, it is not CPA-secure because deterministic MACs will produce the same tag when given the same message, provided that the same signing key $k_S$ is used. This is a real concern, since most MAC systems used in practice *are* deterministic.

### Sign-then-Encrypt
In this approach the first step is to compute the tag $\tau$ of the message $m$, i.e. $\tau \coloneqq \textit{Sign}_{k_S}(m)$. It is then appended to the message $m$ and the resulting concatenation is what actually gets encrypted to obtain the ciphertext $c$.

$$\textit{Enc}(k_E, k_S, m) = \textit{Enc}_{k_E}'(m||\tau)$$

The decryption function decrypts the ciphertext $c$ to obtain the concatenation of the message $m$ with the tag $\tau$ and then verifies them. If either $\textit{Dec}'$ or validation result in an error, then $\textit{Dec}$ simply errors out.

$$\textit{Dec}(k_E, k_S, m) = \begin{cases}\textit{Dec}_{k_E}'(c), \text{ if } \textit{Dec}_{k_E}'(c) \ne \textbf{error} \text{ and } \textit{Verify}(k_S, m, \tau) = 1\\ \textbf{error}, \text{ otherwise}\end{cases}$$

```admonish warning
The Sign-then-Encrypt approach *may* be AE-secure, but this depends highly on the specifics of the cipher and the MAC used. Since it does not provide AE-security in the general case of an arbitrary cipher and an arbitrary MAC, it should be avoided - there is simply too much room for mistakes when implementing it.
```

For example, if there are different error types depending on whether validation or decryption fails, something which is very much necessary in practice, then the security of this approach can be broken by [padding oracle attacks](../Block%20Ciphers/Padding%20Oracle%20Attack.md).

### Encrypt-then-Sign
This approach requires a MAC system with [strong unforgeablity](../Message%20Authentication%20Codes%20(MACs)/index.md#admonition-definition-strong-unforgeability). First, the message is encrypted. The resulting ciphertext $c$ is then signed and the tag $\tau$ is appended to it to obtain the final ciphertext.

$$c \coloneqq \textit{Enc}_{k_E}'(m)$$
$$\tau \coloneqq \textit{Sign}_{k_S}(c)$$
$$\textit{Enc}(k_E, k_S, m) \coloneqq c||\tau$$

The decryption function parses the ciphertext $c||\tau$ back into a message ciphertext and a ciphertext tag $\tau$. If ciphertext verification fails, then it returns an error. Otherwise, it returns the decryption of $c$.

$$\textit{Dec}(k_E, k_S, c||\tau) \coloneqq \begin{cases}\textit{Dec}_{k_E}'(c), \text{ if } \textit{Verify}(k_S, c, \tau) =1 \\ \textbf{error} \text{ otherwise}\end{cases}$$

This approach is quite similar to Encrypt-and-Sign, but the tag is computed on the ciphertext instead of the plaintext. This small difference turns out to be crucial as it is what makes Encrypt-then-Sign AE-secure. Since the tag is verifying the ciphertext, no adversary can tamper with it. This reduces any CCA adversary to a CPA adversary and the CPA-security of $(\textit{Enc}', \textit{Dec}')$ guarantees protection against this.

```admonish check collapsible=true title="Proof: AE-Security of Encrypt-then-Sign"
Suppose that $\mathcal{A}$ is a CCA adversary. 

For each of the adversary's decryption queries, the strong unforgeability of the MAC guarantees that the probability that $\mathcal{A}$ can produce a valid ciphertext $c||\tau$ is negligible, since to produce such a ciphertext, $\mathcal{A}$ would have to find a valid ciphertext-tag pair. The MAC system is secure, so this only happens with probability at most $\frac{1}{2^n} + \textit{negl(n)}$, which is negligible. If $\mathcal{A}$ makes $q$ decryption queries, then the probability that one of them is valid is $q(\frac{1}{2^n} + \textit{negl}(n))$ which is also negligible, since $q$ has to be polynomial. This means that the cipher provides [ciphertext integrity (CI)](../Security%20Notions/Ciphertext%20Integrity%20(CI).md), even in the more empowering scenario which allows $\mathcal{A}$ to submit decryption queries.

What remains is to prove that the cipher $(\textit{Enc}, \textit{Dec}')$ is CPA-secure (remember that CPA-security combined with the already established ciphertext integrity implies CCA-security). Suppose, towards contradiction, that $\mathcal{B}$ is a CPA adversary which can break the CPA-security of $(\textit{Enc}, \textit{Dec})$, i.e. $\mathcal{B}$ can distinguish if a ciphertext $c||\tau$ is the encryption of $m_a$ or $m_b$ with probability $\frac{1}{2} + \textit{nonnegl}(n)$. 

Now, let $\mathcal{B}'$ be a CPA adversary against $(\textit{Enc}',\textit{Dec}')$. When $\mathcal{B}'$ receives its challenge ciphertext $c$, it will compute its tag $\tau$ (this is allowed because the signing key $k_S$ is different from the encryption key $k_E$) and then it will forward $c||\tau$ together with $m_a$ and $m_b$ to $\mathcal{B}$. However, the adversary $\mathcal{B}$ is also a CPA adversary (albeit against $(\textit{Enc}, \textit{Dec})$) and may thus require encryption queries to achieve its goal. This is no problem as $\mathcal{B}'$ can provide answers to any encryption queries that $\mathcal{B}$ might have. Whenever $\mathcal{B}$ submits a plaintext $m$ as a query, the adversary $\mathcal{B}'$ will be able to fulfil it by using its own encryption oracle $\textit{Enc}'$ and then computing the tag for the resulting ciphertext.

Ultimately, $\mathcal{B}'$ will output whichever message, either $m_a$ or $m_b$, that $\mathcal{B}$ does. Since $\mathcal{B}$ will guess correctly if $c||\tau$ is the encryption of $m_a$ or $m_b$ with probability $\frac{1}{2} + \textit{nonnegl}(n)$, then $\mathcal{B}'$ will guess if $c$ is the encryption of $m_a$ or $m_b$ with probability $\frac{1}{2} + \textit{nonnegl}(n)$. This is a contradiction, since it would be a breach of the CPA-security of $(\textit{Enc}',\textit{Dec}')$.
```

It is paramount that the MAC system used has strong unforgeability. Otherwise, a CCA adversary challenged with a ciphertext $c||\tau$ can generate a new valid tag $\tau'$ for $c$ with non-negligible probability. Since $c||\tau \ne c||\tau'$, the adversary is allowed to submit this new tag $\tau'$ with $c$ to its decryption oracle which will pass verification. The decryption oracle will then hand the exact decryption of $c$ to the adversary and so they will know for sure if $c$ was the encryption of some message $m_a$ or another message $m_b$. This would be a breach of CCA-security and therefore also a breach of AE-security.