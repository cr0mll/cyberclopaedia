# Introduction
Perfect secrecy provides security against a limited variant of the [ciphertext-only attack (COA)](Notes/Cryptography/Private-Key%20Cryptography/Security%20Definitions/Ciphertext-Only%20Attack%20(COA)/index.md) where the adversary is presented with only a single ciphertext - no more, no less. It was first described by the father of information theory - [Claude Shannon](https://en.wikipedia.org/wiki/Claude_Shannon) who realised that for a cipher to be invulnerable to a single-COA attack (i.e. a ciphertext-only attack with a single ciphertext), the ciphertext must not reveal anything about the underlying plaintext.

```admonish danger title="Definition: Perfect Secrecy"
An encryption scheme $(\textit{Enc}, \textit{Dec})$ is *perfectly secret* if for every subset $M \subseteq \mathcal{M}$ and for every strategy employed by the adversary Eve, if the plaintext $m \in M$ was chosen at uniformly at random and was encrypted with a uniformly random key $k \in \mathcal{K}$, then the probability that Eve can guess the plaintext when knowing its ciphertext $c = \textit{Enc}_k(m)$ is at most $\frac{1}{|M|}$.
```

```admonish tip title="Definition Breakdown"
When stripped of its mathematical coating, the definition is pretty simple. A plaintext is chosen at random from a set of plaintexts $M$, which is a subset of the message space. There are $|M|$ possible messages for this choice, so the chance that Eve can guess the chosen message without having seen its ciphertext is $\frac{1}{|M|}$. The premise behind perfect secrecy is that this holds true even if Eve *does* have access to the ciphertext - Eve should not be able to obtain any information from the ciphertext that would improve her chances of guessing the chosen plaintext.
```

Determining whether a given encryption scheme is perfectly secret might prove tricky when using this definition. Fortunately, there are some properties which can come in handy - every perfectly secret cipher has them and if a given encryption scheme has *one* of these properties, then it is perfectly secret and by extension has *all* of these properties (what are known as "if and only if" conditions).

```admonish abstract title="Perfect Secrecy Equivalent Definitions"
Since these properties go both ways - every perfectly secret cipher has these and every cipher which has *one* of these has all of them and is perfectly secret, they are called *equivalent definitions*.

For any perfectly secret encryption scheme $(\textit{Enc},\textit{Dec})$, it is true that:

1. For every two distinct plaintexts $m_0, m_1 \in \mathcal{M}$ and any strategy employed by the adversary $\textit{Eve}: \mathcal{C} \to \mathcal{M}$, if Eve is given a ciphertext of one of the plaintexts $m_0$ or $m_1$, then the probability that Eve can guess the message the ciphertext belongs to is less than or equal to $\frac{1}{2}$, i.e.

$$\Pr_{b\leftarrow_R\{0,1\},k\leftarrow_R \mathcal{K}}[\textit{Eve}(\textit{Enc}_k(m_b)) = m_b] \le \frac{1}{2}$$

2. For every two fixed plaintexts $m,m' \in \mathcal{M}$, the distributions $\{\textit{Enc}_k(m)\}_{k\leftarrow_R \mathcal{K}}$ and $\{\textit{Enc}_k(m')\}_{k\leftarrow_R \mathcal{K}}$ obtained by sampling the key space $\mathcal{K}$ are identical.

3. For every distribution $\mathcal{D}$ over $\mathcal{M}$ and strategy $\textit{Eve}: \mathcal{C} \to \mathcal{M}$, the probability that Eve can guess a message chosen according to $\mathcal{D}$ from its corresponding ciphertext is less than or equal to the highest probability assigned by the distribution $\mathcal{D}$, i.e.

$$\Pr_{m\leftarrow_R \mathcal{D}, k\leftarrow_R \mathcal{K}}[\textit{Eve}(\textit{Enc}_k(m)) = m] \le \max(\mathcal{D})$$
```

```admonish check collapsible=true title="Proof: Perfect Secrecy Properties"
**Proof of the first property**:

If a Shannon cipher $(\textit{Enc}, \textit{Dec})$ is perfectly secret, then the first property follows directly from the definition of perfect secrecy.

To prove the "if" direction we use a proof by contradiction. We need to show that if there were some set of plaintexts $M \subseteq \mathcal{M}$ and a strategy for Eve to guess a chosen plaintext from $M$ with a probability greater than $\frac{1}{|M|}$ (i.e., the cipher were *not* perfectly secret), then there would also exist a set $M'$ of size 2 for which Eve can guess a plaintext chosen from $M'$ with probability greater than $\frac{1}{2}$.

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

In other words, we just proved the existence of two messages $m_0,m_1$ for which $\Pr[\textit{Eve}(\textit{Enc}_k(m_1)) = m_1] \gt \Pr[\textit{Eve}(\textit{Enc}_k(m_1)) = m_0]$ and can now construct the set $M' = \{m_0,m_1\}$ which contradicts our initial condition. Therefore, $M'$ cannot exist and by extension $M$ cannot either, making the cipher perfectly secret.

**Proof of Second Property**
TODO

**Proof of Third Property**
TODO

```

Now, these properties are useful, but does there actually exist a perfectly secret encryption scheme? The answer to that is yes and perhaps the most famous example of such a cipher is the [One-Time Pad](One-Time%20Pad.md). 

## Long Keys Requirement
Perfect secrecy does impose one huge restriction - for an encryption scheme to be perfectly secret, its key cannot have a length shorter than that of the message. 

```admonish abstract title="Theorem: Long Keys Requirement"
For every perfectly secret encryption scheme $(\textit{Enc},\textit{Dec})$, the message length function $l(n)$ satisfies $n \ge l(n)$.
```

```admonish check collapsible=true title="Proof: Long Keys Requirement"
Given a Shannon cipher $(\textit{Enc}, \textit{Dec})$, if the key was shorter than the message, then there would be fewer possible keys than possible messages, i.e. $|\mathcal{K}| \lt |\mathcal{M}|$. An adversary can gain an edge by choosing a key instead of a plaintext at random and simply decrypting the known ciphertext $c$ with it. The probability that the decrypted ciphertext results in the hidden message $m$, i.e. $\Pr[\textit{Dec}_k(c) = m]$, will be $\frac{1}{|K|}$ and since there are fewer keys than messages, this probability is greater than $\frac{1}{|M|}$, thus making the cipher not perfectly secret.
```

In proving the theorem, we have actually proved the following, more general statement.

```admonish warning title="Shannon's Theorem"
For a Shannon cipher to be perfectly secret, the number of possible keys must be greater than or equal to the number of possible messages, i.e. $|\mathcal{K}| \ge |\mathcal{M}|$.
```

The aforementioned relationship between the key and message lengths is just a corollary of this. This is a profound fact which limits the practicality of perfect secrecy. For example, if one wanted to securely transmit a 1 GB file using a perfectly secret encryption scheme, then they would also require a 1 GB key!

In conclusion, perfect secrecy is an amazing (and even implementable!) idea, but it is not practical. Due to this fact, perfectly secret ciphers are rarely employed in practice. Instead, relaxed security notions which are still good enough are used. As with most things in life, one cannot have their cake and eat it, too.