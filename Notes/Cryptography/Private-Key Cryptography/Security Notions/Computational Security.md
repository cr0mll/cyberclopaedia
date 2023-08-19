# Introduction
[Perfect Secrecy](Perfect%20Secrecy.md) turns out to be an achievable yet impractical goal because it requires the key to be at least as long as the message to be encrypted which poses huge logistical problems when the message is longer that a few hundred bits (pretty much always). So we seek a relaxed definition for security which allows us to use keys shorter than the message but is still reasonable and as close to perfect secrecy as possible.

# Computational Security
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
A Shannon cipher $(\textit{Enc},\textit{Dec})$ is *computationally secure* if for every two distinct plaintexts $m_1,m_2 \in \mathcal{M}$ and every polynomial-time strategy of Eve, if a random message $m$ is chosen from $\{m_1,m_2\}$ and is encrypted with a random key $k \in \mathcal{K}$, then the probability that Eve guesses which message was chosen after seeing $\textit{Enc}_k(m)$ is at most $\frac{1}{2} + \mu(n)$ for some negligible function $\mu(n)$.
```

```admonish tip title="Definition Breakdown"
All this definition entails is that a cipher is considered computationally secure if there is no strategy for Eve which can give a non-negligible advantage over $\frac{1}{2}$.

The negligible function $\mu$ is given the key length $n$ as an input.
```

The description "negligible" here means that the advantage is small enough that we don't need to care about it in practice. 

### Negligible Functions
```admonish danger title="Definition: Negligible Function"
A function $\mu :\mathbb{N} \to [0,1]$ is *negligible* if for every polynomial $p: \mathbb{N} \to \mathbb{N}$ there exists a number $N \in \mathbb{N}$ such that $\mu(n) \lt \frac{1}{p(n)}$ for every $n \gt N$.
```

The definition itself is not that important, just remember that a negligible function approaches 0 and it does so quickly as its input approaches infinity.

```admonish tip title="Definition Breakdown"
Essentially, a function is negligble if it approaches 0 as its input becomes larger and larger. That is, no matter how big a polynomial one can think of, after some input $N$ the function will always be smaller than the reciprocal of the polynomial. 

The reason the function outputs a number between 0 and 1 is that such functions are usually used in the context of probabilities (as is the case here).
```

The reason we want the negligible function to get smaller and smaller as its input gets larger and larger is because we are using the key length $n$ for its input, so we want to say that longer keys are still more secure than shorter ones but at the same time we do not need to use *massive* keys. By today's standards, a reasonable negligible function would be one which is already on the order of $\frac{1}{2^{128}}$ for an input $n = 128$. So, not only does the function need to approach 0, but it also needs to do so fairly quickly.

# P vs NP
*Every* private-key encryption scheme (yes, even perfectly secret ones) can be broken in the sense that you can find whether a ciphertext $c$ corresponds to $m_1$ or $m_2$ simply by trying all possible keys - an approach called a *brute force attack*.

```python
def BruteForce(ciphertext, plaintext1, plaintext2):
	for key in [0..2^n - 1]:
		if Enc(key, plaintext1) == ciphertext:
			return plaintext1
		if Enc(key, plaintext2) == ciphertext:
			return plaintext2
```

The reason we are not really worried about this attack, which works for *every* cipher, is that it runs in exponential time - the `for` loop will execute $2^n$ number of times in the worst case scenario and on average it will run $2^{\frac{n+1}{2}}$ number of times in order to crack a given ciphertext. This means that as the key gets longer and longer, the number of times that the `for` loop needs to execute on average to crack a given ciphertext gets larger and it does so very fast. In essence, this is a strategy which always works but is very slow. A key length of just 256 bits means that the algorithm will need to run $2^{128.5}$ number of steps to crack a given ciphertext on average which is *practically impossible* for even the most powerful supercomputers.

```admonish example
According to Wikipedia, the most powerful supercomputer currently in existence is [Frontier](https://en.wikipedia.org/wiki/Frontier_(supercomputer)). It has $606\,208$ AMD Epyc cores running at 2 GHz each and $8\,335\,360$ AMD Radeon Instinct cores which we will also assume to be running at 2 GHz each. This gives us a total of $\,8\,941\,568$ cores all executing $2\times 10^9$ cycles per second which amounts to

$$8\,941\,568 \times 2\times 10^9 = 1.79\times 10^{16} \text{ cycles/s}$$

If we assume that every cycle corresponds to a single key tried (a pretty generous assumption, mind you), then on average this computer would need $\frac{2^{128.5}}{1.79\times 10^{16}} = 2.69 \times 10^{22}$ seconds to crack a ciphertext encrypted with a 256-bit key. This amounts to $8.53 \times 10^{14}$ years which is approximately $62\,263$ times the current age of the Universe. Yes, a *very long time*, indeed.
```

Therefore, we know that the problem of cracking a ciphertext encrypted with a given $n$-bit key is solvable (i.e. there is an algorithm to do it) in exponential time - it takes $O(2^n)$ number of steps to execute. This makes it an NP problem. 

However, it can be shown that if *any* NP problem can be shown to have an algorithm which executes much faster (i.e. in polynomial time) and is thus a P problem, then *all* NP problems can be solved much faster. This is called the $P=NP$ hypothesis and remains unproven and with little evidence to speak for it so far. What it entails, however, is that cryptography is basically useless if it turns out to be true, for it means that the brute force attack can also be sped up drastically - instead of $2^n$ steps to execute, it will be able to run in $n^{10}$ or $n^2$ or maybe even $n$ steps, all of which are much smaller than $2^n$. 

```admonish example title="P <p>&#61;</p> NP Breaks Cryptography"
If the brute force attack could be optimised to run in $n^{10}$ steps, then it would take only $1.21 \times 10^{24}$ steps to crack a 256-bit key. This can be done on the Frontier supercomputer in a little over 2 years which is *not* infeasible and can be momentous for military purposes, for example.
```