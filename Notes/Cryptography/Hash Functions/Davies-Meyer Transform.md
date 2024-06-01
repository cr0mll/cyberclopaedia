# Davies-Meyer Transform

Compression hash functions with fixed-length inputs can be constructed from block ciphers using the Davies-Meyer transform. In particular, given a block cipher $$(\textit{Enc}, \textit{Dec})$$ with key-length $$n$$ and block length $$l$$, we can build a compression function $$h(\textit{input}:\textbf{str}[\textbf{fixed }n+l])\to \textbf{str}[\textbf{fixed }l]$$ as follows:

$$h(x) \coloneqq \textit{Enc}(x[0..n], x[n..l]) \oplus x[n..l]$$

Essentially, we parse the $$n+l$$-bit string $$x$$ as a key $$k \coloneqq x[0..n]$$ of length $$n$$ and a string $$y \coloneqq x[n..l]$$ of length $$l$$. The encryption algorithm is invoked on the string $$y$$ with the key $$k$$ and the resulting "ciphertext" is then XOR-ed with $$y$$ to produce the hash of $$x$$.

![](<Resources/Images/Davies-Meyer Function.svg>)

In practice, one never uses common block ciphers such as AES when implementing Davies-Meyer functions because these ciphers are designed to be fast when encrypting a long message with the same key. However, when combined within the [Merkle-Damgård transform](../Hash%20Functions/Merkle-Damg%C3%A5rd%20Transform.md) Davies-Meyer functions work with relatively short inputs and keys which change for each input. Additionally, common block ciphers have smaller output lengths than is necessary for most hash functions - AES has 128-bit outputs which is a big no no because birthday attacks will be able to find collisions after only $$2^{64}$$ tries (something feasible on a modern computer). Therefore, block ciphers used for the implementation of Davies-Meyer functions are specifically designed for this very purpose and have outputs of length 512 or even 1024 bits.

## Security

It is unknown how to prove that $$h$$ is collision resistant solely based on the fact that the block cipher $$(\textit{Enc}, \textit{Dec})$$ uses a [pseudorandom permutation](<../Primitives/Pseudorandom Permutations (PRPs).md>). However, we _can_ prove collision resistance if the block cipher is _ideal_. This means that the cipher uses a truly random permutation - the _only_ way to know the output of $$\textit{Enc}$$ for a specific $$y$$ and key $$k$$ is to _actually evaluate_ $$\textit{Enc}(k, y)$$ because every output is equally likely.

{% hint style="success" %}
<mark style="color:green;">**Theorem: Davies-Meyer Collision Resistance**</mark>

If the Davies-Meyer function $$h$$ is implemented using an _ideal_ block cipher $$(\textit{Enc}, \textit{Dec})$$, then the probability that any attacker who queries $$(\textit{Enc}, \textit{Dec})$$ with $$q$$ queries can find a collision is at most $$\displaystyle\frac{q^2}{2^l}$$.
{% endhint %}

<details>

<summary><strong>Proof: Davies-Meyer Collision Resistance</strong></summary>

Since the cipher is ideal, the function $$\textit{Enc}$$ is a truly random permutation, and, in particular, for every key $$k \in \mathcal{K}$$ the function $$\textit{Enc}_k$$ is also a truly random permutation (contrast this to the case of pseudorandom permutations, where this holds true only if the key is uniformly chosen).

The attacker is given oracle access to $$(\textit{Enc}, \textit{Dec})$$ and tries to find two strings $$x \ne x'$$ such that $$h(x) = h(x')$$. After parsing these strings as $$(k, y)$$ and $$(k', y')$$, the adversary's goal reduces to finding $$(k, y)$$ and $$(k', y')$$ such that $$\textit{Enc}(k, y) \oplus y = \textit{Enc}(k', y') \oplus y'$$.

We assume that the adversary is "smart" in the sense that they never make the same query twice (otherwise they would just be wasting their own time) and that they never query $$\textit{Dec}$$ with a ciphertext whose plaintext they already know, lest they again waste their own time.

Consider the adversary's $$i$$-th query. A query to $$\textit{Enc}(k_i, y_i)$$ reveals only the hash $$h_i = h(x_i) = h(k_i||y_i) = \textit{Enc}(k_i, y_i) \oplus y_i$$. Similarly, a query to $$\textit{Dec}(k_i', y_i')$$, will only reveal the hash $$h_i = h(x_i') = h(k_i'||y_i') = y_i \oplus \textit{Dec}(k_i, y')$$. A collision only occurs if $$h_i = h_j$$ for some $$i \ne j$$.

Fix $$i, j$$ with $$i \gt j$$. When making the $$i$$-th query, the value of $$h_j$$ is already known, since it was obtained in a previous query. A collision occurs only if the adversary queries $$\textit{Enc}(k_i, y_i)$$ and obtains $$\textit{Enc}(k_i, y_i) = h_j \oplus y_i$$ or they query $$\textit{Dec}(k_i', y_i')$$ and obtain $$\textit{Dec}(k_i', y_i') = h_j \oplus y_i'$$. Each event occurs with probability at most

$$\frac{1}{2^l-(i-1)}$$

This is true because the adversary has already made $$i-1$$ queries and has therefore made at most $$i-1$$ previous queries with the same key $$k_i$$. Since they are not repeating queries, there are (at most) $$i-1$$ fewer possible inputs the adversary can use for $$y_i$$. The probability of a collision at the $$i$$-th step is then the probability that the adversary makes an encryption query and obtains a collision or they make a decryption query and obtain a collision, i.e.

$$\Pr[\text{Coll}_{ij}] = \frac{2}{2^l-(i-1)}$$

Since $$i \le q \lt 2^{l/2}$$ (comparing with the birthday attack), $$i$$ can be at most $$2^{l/2}$$ and for sufficiently large $$l$$, we have $$2^l \gg 2^{l/2}$$ which gives

$$\Pr[\text{Coll}_{ij}] \le \frac{2}{2^l}$$

The probability of a collision in $$q$$ queries can be expressed as

$$\Pr[\text{Coll}_q] = \Pr\left[\bigcup_{j \lt i \le q} \text{Coll}_{ij}\right]$$

By the union bound, we obtain

$$\Pr[\text{Coll}_q] \le \sum_{j\lt i\le q} \Pr[\text{Coll}_{ij}]$$

The number of distinct pairs $$i,j$$ which satisfy $$j \lt i \le q$$ is exactly $$\binom{q}{2}$$ which is upper bounded by $$\frac{q^2}{2}$$. Ultimately, we have that

$$\Pr[\text{Coll}_q] \le \sum_{j\lt i\le q} \Pr[\text{Coll}_{ij}] \le \frac{q^2}{2}\Pr[\text{Coll}_{ij}] = \frac{q^2}{2^l}$$

</details>
