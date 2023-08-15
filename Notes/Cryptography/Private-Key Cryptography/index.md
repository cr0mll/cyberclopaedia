# Introduction
Private-key cryptography uses the same secret key for both encryption and decryption. It is important that modern cryptography is usually concerned entirely with the encryption and decryption of binary data, i.e. binary strings. That is why both the message, the key and the encrypted message are represented as binary strings of 1s and 0s.

What defines a given *cipher* is a *private-key encryption scheme* which has an algorithm for encryption and decryption. The message to be encrypted is called the *plaintext* and the resulting string after encryption is called the *ciphertext*.

```admonish danger title="Formal Definition: Valid Private-Key Encryption Scheme"
Given a key-length $n \in \mathbb{N}$, a plaintext length function $l: \mathbb{N} \to \mathbb{N}$ and a ciphertext length function $C: \mathbb{N} \to \mathbb{N}$, a *valid private-key encryption scheme* is a pair of polynomial-time computable functions $(\textit{Enc}, \textit{Dec})$ such that for every key $k \in \{0,1\}^n$ and plaintext $m \in \{0,1\}^{l(n)}$, it is true that:

$$|\textit{Enc}(k, m)| = C(n) \text{ and } \textit{Dec}(k, \textit{Enc}(k,m)) = m$$

The first parameter, i.e. the key $k$, can also be denoted as a subscript - $\textit{Dec}_k$ and $\textit{Enc}_k$.

![](Resources/Images/Private-Key%20Encryption%20Scheme.svg)

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
An encryption scheme $(\textit{Enc}, \textit{Dec})$ is *perfectly secret* if for every set of plaintexts $M \subseteq \{0,1\}^l$ and for every strategy employed by the adversary Eve, if the plaintext $m \in M$ was chosen at random and was encrypted with a random key $k \in \{0,1\}^n$, then the probability that Eve can guess the plaintext after seeing its ciphertext $c = \textit{Enc}_k(m)$ is at most $\frac{1}{|M|}$.
```

```admonish tip title="Definition Breakdown"
When stripped it of its mathematical coating, the definition is pretty simple. A plaintext is chosen at random from a set of possible plaintexts (often called the *message space*) $M$. There are $|M|$ possible messages, so the chance that Eve can guess the chosen message without having seen its ciphertext is $\frac{1}{|M|}$. The premise behind perfect secrecy is that this holds true even if Eve *does* have access to the ciphertext - Eve should not be able to obtain any information from the ciphertext that would improve her chances of guessing the chosen plaintext.
```