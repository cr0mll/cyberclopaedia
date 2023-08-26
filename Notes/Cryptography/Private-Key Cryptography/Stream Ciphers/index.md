# Introduction
Stream ciphers avail themselves of [pseudorandom generators (PRGs)](../../Pseudorandom%20Generators%20(PRGs).md) in order to allow for messages with a length arbitrarily larger than the key's. Under the hood, they are nothing more than the [One-Time Pad](../One-Time%20Pad.md) paired with a pseudorandom generator.

```admonish danger title="Definition: Stream Cipher"
A *stream cipher* is a cipher $(\textit{Enc},\textit{Dec})$ equipped with a pseudorandom generator $\textit{Gen}(seed: str[S]) \to str[\ge l]$ which takes a key $k$ of length $n$, a message $m$ of length $l$ and produces a ciphertext $c$ of length $C = l$ and is defined as follows:

$$\textit{Enc}_k(m) \coloneqq \textit{Gen}(s)[0..l] \oplus m$$
$$\textit{Dec}_k(c) \coloneqq \textit{Gen}(s)[0..l] \oplus c$$

The seed $s$ is derived from the key $k$.
```

```admonish tip title="Definition Breakdown"
To encrypt a message a stream cipher first derives a seed $s$ from the key $k$. It then passes this seed to the generator $\textit{Gen}$ to generate a string of pseudorandom bits, called a *keystream*, which is as at least as long as the message $m$. The first $l$ bits of the keystream are then XOR-ed with the message to obtain the ciphertext and the rest of the keystream is simply discarded.

The decryption algorithm once again uses the key $k$ to derive the seed $s$. The seed is then passed on to the generator $\textit{Gen}$ in order to produce the same keystream used during the encryption. The first $l$ bits of the keystream are then XOR-ed with the ciphertext to retrieve the message. As before, if the keystream is longer than the message, any additional bits are simply ignored.

Note that the message and the resulting ciphertext are of equal length.
```

# Seed Derivation
In order to generate the keystream, the pseudorandom generator needs a seed. In the most basic cases, the key $k$ is used as the seed. However, usually the seed is created by appending to the key another binary string called the *initialisation vector (IV)*. 

![](Resources/Images/Keystream%20Generation.svg)

The IV must be a random string and the same IV should *never* be used with the same key. Moreover, the IV must be known for decryption in order to derive the same seed from the key. Therefore, decryption requires both the key and the IV to function.

The purpose of the initialisation vector is to allow for key reuse. So long as the same key is used with different IVs, it poses no threat to the security of the cipher under a [ciphertext-only attack](../Security%20Notions/index.md).
