# Introduction
[Perfect Secrecy](Perfect%20Secrecy.md) turns out to be an achievable yet impractical goal because it requires the key to be at least as long as the message to be encrypted which poses huge logistical problems when the message is longer that a few hundred bits (pretty much always). So we seek a relaxed definition for security which allows us to use keys shorter than the message but is still reasonable and as close to perfect secrecy as possible.

# Semantic Security
Let's consider again the scenario where we choose one from two plaintexts $m_1, m_2$ encrypted with the same, unknown to Eve key $k$ and Eve tries to guess which plaintext we chose. Without having the ciphertext of the chosen message, the probability that Eve guesses correctly is $\frac{1}{2}$. If the cipher used is perfectly secret, then this is true even after Eve sees the ciphertext $c$ of the chosen message. However, if the key used is shorter than the message, even by a single bit, then the adversary Eve can first pick a random key and decrypt the ciphertext with it. The probability that she chose the correct key and the decryption resulted in one of the messages $m_1$ or $m_2$ (i.e. Eve now knows which plaintext was used to obtain the ciphertext) is $\frac{1}{|\mathcal{K}|} = \frac{1}{2^n}$. If Eve did not guess the key correctly and $\textit{Dec}_k(c)$ is neither equal to $m_1$ nor $m_2$, then Eve can, as before, just guess randomly which message was used with probability $\frac{1}{2}$. This strategy can be implemented by the following algorithm:

```python
def Distinguish(ciphertext,plaintext1,plaintext2):
	key = random(0, 2^(n-1)) # Pick a random key from the 2^n possible keys
	
	if Dec(key, ciphertext) == plaintext1:
		return plaintext1
	if Dec(key, ciphertext) == plaintext2:
		return plaintext2
	
	return choice([plaintext1,plaintext2]) # If the key was not correct, then randomly pick a plaintext 
```

The probability that Eve guesses correctly is then the probability that she picks the correct key or that she picks the wrong key and guesses correctly simply by choosing one of the messages and is equal to $\frac{1}{2} + \frac{1}{2^{n+1}}$ which is greater than $\frac{1}{2}$.

```admonish check collapsible=true title="Proof"
Let's say that we picked the message $m_1$ and encrypted it with the key $k$ to obtain the ciphertext $c$.

$$\Pr[\textit{Eve}(c) = m_1] =$$
$$\Pr[\text{Eve guesses the key correctly} \lor \\ (\text{Eve does not guess the key} \land \text{Eve correctly chooses a plaintext from } m_1 \text{ and } m_2)] = $$ 
$$\begin{align} &= \frac{1}{2^n} + \left(1 - \frac{1}{2^n}\right)\times \frac{1}{2} \\ &= \frac{1}{2^n} + \frac{2^n - 1}{2^n}\times\frac{1}{2} \\ &= \frac{2 + 2^n - 1}{2^{n+1}} \\ &= \frac{1}{2} + \frac{1}{2^{n+1}}\end{align}$$
```

This strategy is *universal* in the sense that it works for any encryption scheme which uses a key shorter than the plaintext. Fortunately, the advantage that the adversary Eve gains using this strategy gets really small for larger and larger keys. For example, a 128-bit key (a key-length ubiquitous nowadays) provides an advantage of only $\frac{1}{2^{129}}$, which is really, *really* tiny. Keys used for private-key encryption rarely exceed 512 bits in length which is a tractable key length to deal with and we have already seen that even 128 bit keys ensure a pretty much negligible advantage.

This entails that *some* advantage over $\frac{1}{2}$ is always possible when the key is shorter than the message and our goal with the definition of computational security is to keep this advantage as low as possible for any potential strategy that Eve might employ.

```admonish danger title="Definition: Computational Security"
A Shannon cipher $(\textit{Enc},\textit{Dec})$ is *computationally secure* if for every two distinct plaintexts $m_1,m_2 \in \mathcal{M}$ and every polynomial-time strategy of Eve, if a random message $m$ is chosen from $\{m_1,m_2\}$ and is encrypted with a random key $k \in \mathcal{K}$, then the probability that Eve guesses which message was chosen after seeing $\textit{Enc}_k(m)$ is at most $\frac{1}{2} + \epsilon(n)$ for some negligible function $\epsilon(n)$.
```

```admonish tip title="Definition Breakdown"
All this definition entails is that a cipher is considered computationally secure if there is no strategy for Eve which can give a non-negligible advantage over $\frac{1}{2}$.

The negligible function $\epsilon$ is given the key length $n$ as an input.
```

The description "negligible" here means that the advantage is small enough that we don't need to care about it in practice. 

# Leap of Faith
As it turns out, proving that a cipher is semantically secure is not a trivial task. Similarly to [Pseudorandom Generators (PRGs)](../../Pseudorandom%20Generators%20(PRGs).md#leap-of-faith), we are actually forced to *assume* that such ciphers exist. On the one hand, there are some ciphers which have withstood years of attempts to be broken . Therefore, we really do believe that they are secure but we are, unfortunately, unable to prove this. On the other hand, we have ruled out many ciphers as insecure by showing a way to break them. Essentially, a cipher is considered semantically secure until a way to break it is found.

Nevertheless, in order to be as safe as possible, one needs to make as few assumptions as possible and indeed that is what cryptography does. In this regard, cryptography makes only *one* assumption about the existence of a specific semantically secure cipher.

```admonish question title="Assumption: Existence of a Semantically Secure Cipher"
There exists a semantically secure cipher with keys of length $n$ and messages of length $l(n) = n + 1$.
```

This is indeed a very limited assumption which does not provide much advantage over perfect secrecy - the message can only be a single bit longer than the key. However, it turns out that such a cipher can be used to construct a cipher which uses messages with a length $t(n)$ that are arbitrarily longer than the key.

So, we are given a semantically secure cipher $(\textit{Enc}', \textit{Dec}')$ which takes a key of length $n$ and a message of length $n+1$. The encryption $\textit{Enc}$ of our new cipher which uses keys of length $n$ and messages of length $t$ follows this algorithm:

![Length Extension Encryption](Resources/Images/Semantic%20Security/Length%20Extension%20Encryption.svg)

The encryption algorithm $\textit{Enc}$ naturally uses $\textit{Enc'}$. It processes the plaintext on a bit-per-bit basis. At the first step our cipher generates a random *ephemeral key* $k_0$ of length $n$ and appends to it the first bit of the plaintext - $m[0]$, resulting in a temporary string $r_0 = k_0m[0]$ of length $n+1$. It then encrypts this string with the key $k$ to produce the first part of the ciphertext - $c_0 = \textit{Enc}'(k, k_0m[0])$. This happens at each subsequent stage, however a new random ephemeral key is generated for each stage and one bit of the message is appended to it. This is then encrypted with the *ephemeral key from the previous stage* to produce a ciphertext portion. At the end, the resulting ciphertext is simply the concatenation of all the generated ciphertext parts.

The ephemeral keys are randomly generated on-demand by our encryption algorithm $\textit{Enc}$, which makes the encryption algorithm *non-deterministic*. They should *not* be dependent on any other component of the cipher such as the key or the message. 

The decryption algorithm is the following:

![](Resources/Images/Semantic%20Security/Length%20Extension%20Decryption.svg)

The decryption algorithm $\textit{Dec}$ takes the first $C'$ bits of the ciphertext $c$ and decrypts it using the key $k$ and $\textit{Dec'}$ in order to obtain the first ephemeral key and the first bit of the message. Subsequent stages use the ephemeral key from the preceding stage to get one bit of the message as well the next ephemeral key.

```admonish check collapsible=true title="Proof of Semantic Security"
We have assumed that $(\textit{Enc'},\textit{Dec'})$ is semantically secure and need to prove that $(\textit{Enc}, \textit{Dec})$ as described above is secure, too.

Let $m,m' \in \{0,1\}^t$ be two messages. 
```

This algorithm serves only as a proof-of-concept. It is not particularly useful due to the very large ciphertext that it produces - a single bit of the message gets transformed into $C'$ bits of ciphertext. Nevertheless, it illustrates that it is possible to obtain a cipher with an arbitrary length $t$. Well, there is actually one restriction - the message length $t$ must be polynomial in the key-length $n$ because the encryption algorithm iterates over the message bit by bit. If its length were not polynomial, then the algorithm would take non-polynomial time to execute and would therefore be inefficient and would not count as a valid private-key encryption scheme.