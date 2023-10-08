# Introduction
Hash functions are used ubiquitously not only in cryptography but also in more general algorithms and data structures like [hash tables](https://en.wikipedia.org/wiki/Hash_table). At its core, a hash function is simply an algorithm which takes an input of arbitrary length, denoted by $l_\text{in}$, and produces an output of a fixed length $l_{\text{out}}$. Usually the output length is much smaller than the input length, i.e. $l_{\text{out}} \lt l_{\text{in}}$, and so hash functions are also often called *compression functions*, although they have little to do with the modern notion of compression (in fact, in many ways they are the exact opposite).

```admonish danger title="Definition: (Keyless) Hash Function"
A *(keyless) hash function* is an efficient deterministic algorithm $H(\textit{input}: \textbf{str}[l_{\text{in}}]) \to \textbf{str}[\textbf{const } l_{\text{out}}]$ which takes a binary string of arbitrary length $l_{\text{in}}$ as input and outputs a binary string of a fixed length $l_{\text{out}}$.
```

The input space, also called the message space, $\mathcal{M}$ is the set of all possible inputs for the hash function. The output of the hash function is called a *digest* or *hash* and the set of all possible outputs is called the *digest/hash space* $\mathcal{D}$. If $l_{\text{out}} \lt l_{\text{in}}$, then $H$ is said to be a *compression function*. In this case, the input space is much larger than the digest space, i.e. $|\mathcal{M}| \gt |\mathcal{D}|$.

The word "keyless" means that the hash function does *not* take in an additional input key. This is in contrast to the following definition of *keyed hash functions*.

```admonish danger title="Definition: Keyed Hash Function"
A *keyed hash function* is an efficient deterministic algorithm $H(\textit{key}: \textbf{str}[n], \textit{input}: \textbf{str}[l_{\text{in}}]) \to \textbf{str}[\textbf{const } l_{\text{out}}]$ which takes a binary string of arbitrary length $l_{\text{in}}$ as input and outputs a binary string of a fixed length $l_{\text{out}}$. 

The key $k$ is often denoted as a subscript, i.e. $H_k$.
```

In practice, *all* hash functions are *keyless*. By contrast, keyed hash functions are merely a theoretical tool designed to circumvent some limitations in the theoretical description of certain security notions pertaining to hash functions. Pretty much all proofs involving keyed hash functions can be transformed into proofs about keyless functions and vice-versa with ease - the key seldom appears in proofs. Therefore, we will have little to say about keyed hash functions, so that we can focus more on the practical side of hashing.