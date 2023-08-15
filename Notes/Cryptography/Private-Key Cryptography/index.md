# Introduction
Private-key cryptography uses the same secret key for both encryption and decryption. It is important that modern cryptography is usually concerned entirely with the encryption and decryption of binary data, i.e. binary strings. That is why both the message, the key and the encrypted message are represented as binary strings of 1s and 0s.

What defines a given *cipher* is a *private-key encryption scheme* which has an algorithm for encryption and decryption. The message to be encrypted is called the *plaintext* and the resulting string after encryption is called the *ciphertext*.

```admonish danger title="Formal Definition: Valid Private-Key Encryption Scheme"
Given a key-length $n \in \mathbb{N}$, a plaintext length function $l: \mathbb{N} \to \mathbb{N}$ and a ciphertext length function $C: \mathbb{N} \to \mathbb{N}$, a *valid private-key encryption scheme* is a pair of polynomial-time computable functions $(\textit{Enc}, \textit{Dec})$ such that for every key $k \in \{0,1\}^n$ and plaintext $m \in \{0,1\}^{l(n)}$, it is true that:

$$\textit{Dec}(k, \textit{Enc}(k,m)) = m$$

The first parameter, i.e. the key $k$, can also be denoted as a subscript - $\textit{Dec}_k$ and $\textit{Enc}_k$.

![](Resources/Images/Private-Key%20Encryption%20Scheme.svg)

The set of all possible keys is called the *key space* and is denoted by $\mathcal{K} \subseteq \{0,1\}^n$. The set of all possible plaintexts is called the *message space* and is denoted by $\mathcal{M} \subseteq \{0,1\}^{l(n)}$. The set of all possible ciphertexts is called the *ciphertext space* and is denoted by $\mathcal{C} \subseteq \{0,1\}^{C(n)}$.

```

```admonish tip title="Definition Breakdown"
The encryption function is denoted by $\textit{Enc}$ and the decryption function is called $\textit{Dec}$. The first function, $\textit{Enc}$,  takes a key $k$ and a plaintext $m$ and outputs a ciphertext $c$, while the latter, $\textit{Dec}$, does the opposite - it takes a key $k$ and a ciphertext $c$ and produces the plaintext $m$ which was encrypted to get the ciphertext. Since both will be used with the same key for a given encryption scheme, the key is often written as a subscript, i.e. $\textit{Enc}_k$ and $\textit{Dec}_k$

The key $k$, the plaintext $m$ and the ciphertext $c$ are all binary strings and their lengths, i.e. the number of bits in them, are denoted by $n$, $l(n)$ and $C(n)$, respectively. For simplicity, these are often substituted by just $n$, $l$ and $C$.

The term *polynomial-time computable* means that the encryption and decryption functions should be fast to compute for long keys and messages, which is not an unreasonable requirement. After all, encryption and decryption would be useless if we could never hide or see the message's contents, even if they were intended for us.

The final requirement, i.e. that $\textit{Dec}_k(\textit{Enc}_k(m)) = m$ is essential. It tells us that under any private-key encryption scheme, the encryption function is [one-to-one](../Mathematical%20Prerequisites.md#admonition-injection-surjection-and-bijection) which means that every plaintext produces a unique ciphertext - no two plaintexts can be encrypted to the same ciphertext if the same key $k$ is used. It might seem obvious that this should be true, but it is *not* the case for [hash functions](../Hash%20Functions/index.md), for example, and so hash functions are *not* valid private-key encryption schemes.
```

# Security Notions
The definition given for a *valid* private-key encryption scheme specifies *what* functions can be used for encryption and decryption, but says nothing about *how secure* those functions should be. For example, the trivial encryption function $\textit{Enc}_k(m) = m$ which simply encrypts a plaintext to itself is a valid private-key encryption function but is far from secure.

Defining what makes a private-key encryption scheme *secure* is a bit tricky. 

## Randomness
Getting an outcome from the sample space can be rephrased as choosing an element from it at random. The question of what "at random" *is*, however, does not have as intuitive an answer as one would hope. 

```danger title="Definition: \"Random\""
Something is *random* if there is no way to predict its outcome with absolute certainty.
```

Consider again the example of tossing a fair coin - it has 50% chance of landing on "heads" and 50% chance of landing on "tails". This for sure is *random* - there is no way to tell for certain the outcome of the toss. But now consider a "rigged" coin (maybe it weighs more on one side) which has a 25% chance of landing on "heads" and a 75% chance of landing on "tails". Is this random? Of course it is! Sure we know that there is more chance for the coin to land on "tails", but can we tell with certainty that it will? No, we cannot and so this rigged coin is still random.

## Perfect Secrecy
The foundations of the contemporary definition for security were laid out by [Claude Shannon](https://en.wikipedia.org/wiki/Claude_Shannon) who realised that an encryption scheme is secure if *the ciphertext reveals nothing about the plaintext* - a principle called *perfect secrecy*.

```admonish danger title="Formal Definition: Perfect Secrecy"
An encryption scheme $(\textit{Enc}, \textit{Dec})$ is *perfectly secret* if for every set of plaintexts $M \subseteq \mathcal{M}$ and for every strategy employed by the adversary Eve, if the plaintext $m \in M$ was chosen at random and was encrypted with a random key $k \in \mathcal{K}$, then the probability that Eve can guess the plaintext after seeing its ciphertext $c = \textit{Enc}_k(m)$ is at most $\frac{1}{|M|}$.
```

```admonish tip title="Definition Breakdown"
When stripped of its mathematical coating, the definition is pretty simple. A plaintext is chosen at random from a set of plaintexts $M$, which is a subset of the message space. There are $|M|$ possible messages for this choice, so the chance that Eve can guess the chosen message without having seen its ciphertext is $\frac{1}{|M|}$. The premise behind perfect secrecy is that this holds true even if Eve *does* have access to the ciphertext - Eve should not be able to obtain any information from the ciphertext that would improve her chances of guessing the chosen plaintext.
```

Determining whether a given encryption scheme is perfectly secret might prove tricky when using this definition. Fortunately, there are some properties which are unique to perfectly secret encryption schemes - every perfectly secret encryption scheme has them and if a given encryption scheme has *one* of these properties, then it is perfectly secret and by extension has *all* of these properties (what is known are "if and only if" conditions).

```admonish abstract title="Perfect Secrecy Properties"
For any perfectly secret encryption scheme $(\textit{Enc},\textit{Dec})$, it is true that:

1. For every two distinct plaintexts $m_0, m_1 \in \mathcal{M}$ and any strategy employed by the adversary $\textit{Eve}: \mathcal{C} \to \mathcal{M}$, if Eve is given a ciphertext of one of the plaintexts $m_0$ or $m_1$, then the probability that Eve can guess the message the ciphertext belongs to is less than or equal to $\frac{1}{2}$, i.e.

$$\Pr_{b\leftarrow_R\{0,1\},k\leftarrow_R \mathcal{K}}[\textit{Eve}(\textit{Enc}_k(m_b)) = m_b] \le \frac{1}{2}$$

2. For every two fixed plaintexts $m,m' \in \mathcal{M}$, the distributions $\{\textit{Enc}_k(m)\}_{k\leftarrow_R \mathcal{K}}$ and $\{\textit{Enc}_k(m')\}_{k\leftarrow_R \mathcal{K}}$ obtained by sampling the key space $\mathcal{K}$ are identical.

3. For every distribution $\mathcal{D}$ over $\mathcal{M}$ and strategy $\textit{Eve}: \mathcal{C} \to \mathcal{M}$, the probability that Eve can guess a message chosen according to $\mathcal{D}$ from its corresponding ciphertext is less than or equal to the highest probability assigned by the distribution $\mathcal{D}$, i.e.

$$\Pr_{m\leftarrow_R \mathcal{D}, k\leftarrow_R \mathcal{K}}[\textit{Eve}(\textit{Enc}_k(m)) = m] \le \max(\mathcal{D})$$
```

```admonish check collapsible=true title="Proof: Perfect Secrecy Properties"
**Proof of the first property**:

If an encryption is scheme $(\textit{Enc}, \textit{Dec})$ is perfectly secret, then the first property follows directly from the definition of perfect secrecy.

To prove the "if" direction we use a proof by contradiction. We need to show that if there were some set of plaintexts $M \subseteq \mathcal{M}$ and a strategy for Eve to guess a chosen plaintext from $M$ with a probability greater than $\frac{1}{|M|}$ (i.e., the encryption scheme were *not* perfectly secret), then there would also exist a set $M'$ of size 2 for which Eve can guess a plaintext chosen from $M'$ with probability greater than $\frac{1}{2}$.

Essentially, this set would be $M' = \{m_0,m_1\}$ for some plaintexts $m_0$ and $m_1$ such that $\Pr[\textit{Eve}(\textit{Enc}_k(m_1)) = m_1] \gt \Pr[\textit{Eve}(\textit{Enc}_k(m_1)) = m_0]$. 

To do this, fix $m_0$ to be the message of all 0s and pick a message $m_1$ uniformly at random from $M$. Under our assumption, for any $k$, it is true that

$$\Pr_{m_1\leftarrow_R M}[\textit{Eve}(\textit{Enc}_k(m_1)) = 1] \gt \frac{1}{|M|}$$

This can also be rewritten as

$$\underset{m_1\leftarrow_R M}{\mathbb{E}} \Pr[\textit{Eve}(\textit{Enc}_k(m_1)) = 1] \gt \frac{1}{|M|}$$

On the other hand, the string $m' = \textit{Eve}(\textit{Enc}_k(m_0))$ does not depend on $m_1$ for any choice of the key $k$, so if $m_1$ is selected uniformly at random from $M$, then the probability that $m_1 = m'$ is $\frac{1}{|M|}$.

$$\Pr_{m_1\leftarrow_R M}[m_1 = m'] = \frac{1}{|M|}$$

This can also be rewritten as

$$\underset{m_1\leftarrow_R M}{\mathbb{E}} \Pr[m_1 = m'] = \frac{1}{|M|}$$

Now, by linearity of expectation

$$\underset{m_1 \leftarrow_R M}{\mathbb{E}} ( \Pr[\textit{Eve}(\textit{Enc}_k(m_1)) = m_1] - \Pr[\textit{Eve}(\textit{Enc}_k(m_0)) = m_0] ) \gt 0$$

By the averaging argument, there *must* exist some $m_1$ for which $\Pr[\textit{Eve}(\textit{Enc}_k(m_1)) = m_1] \gt \Pr[\textit{Eve}(\textit{Enc}_k(m_1)) = m_0]$. 

In other words, we just proved the existence of two messages $m_0,m_1$ for which $\Pr[\textit{Eve}(\textit{Enc}_k(m_1)) = m_1] \gt \Pr[\textit{Eve}(\textit{Enc}_k(m_1)) = m_0]$ and can now construct the set $M' = \{m_0,m_1\}$ which contradicts our initial condition. Therefore, $M'$ cannot exist and by extension $M$ cannot either, making the encryption scheme perfectly secret.

**Proof of Second Property**
This can be thought of as the definition of perfect secrecy but with the message and key swapped.

**Proof of Third Property**
TODO

```

Now, these properties are useful, but does there actually exist a perfectly secret encryption scheme? The answer to that is yes and perhaps the most famous example of such a cipher is the [One-Time Pad](One-Time%20Pad.md). 

### Long Keys Requirement
Perfect secrecy does impose one huge restriction - for an encryption scheme to be perfectly secret, its key cannot have a length shorter than that of the message. 

```admonish abstract title="Theorem: Long Keys Requirement"
For every perfectly secret encryption scheme $(\textit{Enc},\textit{Dec})$, the message length function $l(n)$ satisfies $n \ge l(n)$.
```

```admonish check collapsible=true title="Proof: Long Keys Requirement"
Given an encryption scheme $(\textit{Enc}, \textit{Dec})$, if the key was shorter than the message, then there would be a fewer number of possible keys than possible messages, i.e. $|\mathcal{K}| \lt |\mathcal{M}|$. An adversary can gain an edge by choosing a key instead of a plaintext at random and simply decrypting the known ciphertext $c$ with it. The probability that the decrypted ciphertext results in the hidden message $m$, i.e. $\Pr[\textit{Dec}_k(c) = m]$, will be $\frac{1}{|K|}$ and since there are less keys than messages, this probability is greater than $\frac{1}{|M|}$, thus making the encryption scheme not perfectly secret.
```

In more general, however, the proof of this theorem tells us the following principle.

```admonish warning title="Size of the Key and Message Spaces"
For an encryption scheme to be perfectly secret, the size of the key space $\mathcal{K}$ must always be greater than or equal to the size of the message space $\mathcal{M}$.
```

The aforementioned relationship between the key and message lengths is just a corollary of this. This is a profound fact which limits the practicality of perfect secrecy. For example, if one wanted to securely transmit a 1 GB file using a perfectly secret encryption scheme, then they would also require a 1 GB key!
