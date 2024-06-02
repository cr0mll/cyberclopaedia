# Introduction
Randomness is the mainstay of modern cryptography. Designing ciphers is no trifling task and it is also important *how* a cipher's security is achieved. Essentially, an encryption scheme consists of three things - an encryption function, a decryption function and a key. One might think that a good way to ensure the cipher cannot be broken is to simply conceal the encryption and decryption process - after all, if the adversary does not know what they are breaking, how can they break it? 

Unfortunately, if the cipher *does* get broken (and it will by dint of reverse engineering), an entirely different cipher needs to be conceived because the previous one relied on security by obscurity. Quite the predicament, isn't it? 

```admonish warning title="Kerckhoff's Principle"
A cipher needs to be secure even if everything about it except the key is known. 
```

The reason why the key should be the only unknown variable is that keys are just strings of bits and are thus relatively easy to change in comparison to the other components of a cipher. But in order to be sure that the cipher is as secure as possible, the key must be completely random - no single key should be more likely to be used than any other.

## Statistical Tests
And so here comes the question - what is *random*? 

```admonish danger title="Definition: Randomness"
A binary string is *random* if it was produced by a uniform distribution.
```

```admonish tip title="Definition Breakdown"
A binary string is random if it was the outcome of a process where all possible outcomes had equal probability of happening.
```

Okay, but how do we determine that a binary string came from a uniform distribution if we are just given the string and know nothing else about it,, i.e. no one has told us it was obtained from a uniform distribution? This is where *statistical tests* come in.

~~~admonish danger title="Definition: Statistical Test"
A *statistical test* is an algorithm $\textit{ST}(x: str[m]) \to bit$ defined as
$$\textit{ST}(x) = \begin{cases}1, \text{ the input } x \text{ looks random} \\ 0, \text{ the input } x \text{ does not look random}\end{cases}$$
~~~

```admonish tip title="Definition Breakdown"
A statistical test is an *attempt* to determine if a given binary string was obtained from a uniform distribution.
```

It is important to notice that since we lack any additional information other than the binary string itself, we can only make certain assumptions about what a uniformly chosen string would look like and see if the given string fits those assumptions. Each statistical test is an assumption which we use in order to try to check if a string was chosen uniformly at random. Since there is no other information, there is no "best" way or "best" statistical test.

```admonish example title="Example: Statistical Tests"
In a uniformly chosen string one would expect that the number of 0s and the number of 1s are approximately equal, so one possible statistical test is

$$\textit{ST}(x) = \begin{cases} 1, |\textit{Num}(0) - \textit{Num}(1)| \le 10\cdot \sqrt{n} \\ 0, \text{ otherwise} \end{cases}$$

where $m$ is the length of the binary string $x$.

Similarly, one would expect the longest sequence of 1s in a uniformly chosen string to be around $\log_2(m)$ and so another possible statistical test would be

$$\textit{ST}(x) = \begin{cases}1, \textit{LS1s}(x) \le \log_2(m) \\ 0, \text{ otherwise} \end{cases}$$
```

These examples illustrate that statistical tests can be pretty much anything and that if we are given no other information about a string other than the string itself, we cannot with certainty determine if it came from a uniform distribution. We can only test the string for properties that we would expect from a uniformly chosen string.

```admonish note title="Distinguishers"
Statistical tests are often called *distinguishers* since they attempt to distinguish whether their input came from one distribution or another.
```

# Obtaining Randomness
Cryptography requires randomness and it requires a lot of it, too. However, computers (at least classical ones) are entirely deterministic, so it turns out that randomness is actually quite difficult to come by. For example, a computer might use information from its temperature sensors or from surrounding electromagnetic noise. Nevertheless, these sources can only provide so many random bits and rarely satisfy the needs for randomness at a given time. 

So, it would be useful to be able to use these random bits to obtain *more* random bits, wouldn't it? 

## Pseudorandomness
There is a caveat to the process of obtaining more randomness via a computer, however. Since classical computers are deterministic, it is not really possible to obtain *truly* random bits - classical computers cannot really "choose a string from a uniform distribution". Besides, producing longer strings from shorter ones requires *generating information* - it is like filling in the gaps in some puzzle with missing pieces. Classical computers do not have a way for randomly generating information - they can only obtain it from their surroundings as mentioned previously. But these surroundings can only provide so much randomness. The rest requires an algorithm and an algorithm means a *pattern*. Therefore, we will have to settle for something that is *close enough* to random - i.e. the pattern is *extremely difficult* to detect.

```admonish danger title="Definition: Pseudorandomness"
A string of bits $s \in \{0,1\}^m$ is *pseudorandom*, if for every efficient statistical test $\textit{ST}$ running in time $p(m)$, where $p$ is some polynomial, it holds true that

$$\left| \Pr[\textit{ST}(s) = 1] - \Pr_{r \leftarrow_R \{0,1\}^m}[\textit{ST(r)} = 1] \right| \lt \frac{1}{p(m)}$$
```

```admonish tip title="Definition Breakdown"
Essentially, a string of bits $s$ with length $m$ is pseudorandom if there is no statistical test which can distinguish with non-negligible probability between it and a string uniformly chosen from all strings of length $m$. In other words, the difference between the probability that any statistical test classifies a string $s$ as random and that it classifies a uniformly chosen string as random should be very very small, i.e. negligible.
```

## Comparing Distributions
Statistical tests provide a way to determine if a string is likely to have been obtained from a uniform distribution. In a sense, they compare a given string with a string from a uniform distribution. Now, this begs the question if statistical tests can be used to compare two distributions? Indeed, they can!

```admonish danger title="Definition: Computational Indistinguishability"
Two distributions $X$ and $Y$ over $\{0,1\}^m$ are $(T, \epsilon)$*-computationally indistinguishable*, denoted by $X \approx_{T,\epsilon} Y$, if for every algorithm $\mathcal{A}(s: str[m]) \to bool$ computable in at most $T$ operations, it holds that

$$\left|\Pr_{x\sim X}[\mathcal{A}(x) = 1]-\Pr_{y\sim Y}[\mathcal{A}(y) = 1]\right| \le \epsilon$$
```

```admonish tip title="Definition Breakdown"
One can think of the algorithm $\mathcal{A}$ as an algorithm which tries to determine if its input was obtained from the distribution $X$ or from the distribution $Y$, i.e.

$$\mathcal{A}(s) = \begin{cases}1, s \text{ came from } X \\ 0, s \text{ came from } Y \end{cases}$$

Essentially, the definition says that if $X$ and $Y$ are $(T, \epsilon)$-computationally indistinguishable, then there is no such algorithm $\mathcal{A}$ which takes $T$ steps to run that can differentiate if its input $s$ came from $X$ or $Y$ with non-negligible probability. In other words, the algorithm $\mathcal{A}$ is approximately equally likely to think that any given input $s$ came from $X$ as it is to believe that it came from $Y$, i.e.

$$\Pr_{x\sim X}[\mathcal{A}(x) = 1] \approx \Pr_{y\sim Y}[\mathcal{A}(y) = 1]$$
```

The numbers $T$ and $\epsilon$ are *parameters*. If an algorithm had more time to run, i.e. $T$ was a big number, then it could perform more computations and so it is reasonable to expect that it could better distinguish between the two distributions. Just *how* better is quantified by the number $\epsilon$ which is the difference in the probabilities that the algorithm thinks an input came from the distribution $X$ and that it came from the distribution $Y$. 

```admonish example
Consider the two distributions $X \approx_{100m,0.001}Y$ over $\{0,1\}^m$ which are $(100m, 0.001)$-computationally indistinguishable. This means that for any algorithm $\mathcal{A}$, which takes $100m$ steps to complete on an input $s$ of length $m$, it is true that the difference in the probability that $\mathcal{A}$ thinks $s$ came from $X$ and the probability that $\mathcal{A}$ thinks $s$ came from $Y$ is at most $\epsilon$.

$$\left|\Pr_{x\sim X}[\mathcal{A}(x) = 1]-\Pr_{y\sim Y}[\mathcal{A}(y) = 1]\right| \le 0.001$$
```

Computational indistinguishability is a way to measure how "close" or "similar" two distributions are, i.e. how different the probabilities they assign to the same string are. It is reasonable to expect that if the distribution $X$ is computationally indistinguishable from the distribution $Y$ and $Y$ is computationally indistinguishable from the distribution $Z$, then $X$ is also computationally indistinguishable from $Z$. After all, if one thing is close to another thing which is close to a third thing, then the third thing is also close to the first. And indeed, this turns out to be true for computationally indistinguishable distributions!

```admonish abstract title="Theorem: Triangle Inequality for Computational Indistinguishability"
If $X_1 \approx_{T,\epsilon} X_2 \approx_{T,\epsilon} \cdots \approx_{T,\epsilon} X_m$, then $X_1 \approx_{T, (m-1)\epsilon} X_m$.
```

```admonish tip title="Theorem Breakdown"
If you have a sequence of distrbutions $X_1, X_2, ..., X_m$, where adjacent distributions are close to one another, then it makes sense that the first and the last distribution are also close to one another. However, it is still the case that $X_m$ is closer to $X_{m-1}$ than it is to $X_1$ which is why $X_1$ and $X_m$ are only $(T, (m-1)\epsilon)$ indistinguishable and not $(T, \epsilon)$. The "distance" between $X_m$ and $X_1$ is greater than the distance between $X_m$ and $X_{m-1}$ which is why an algorithm running in time $T$ in both cases would be a bit better in distinguishing $X_{m-1}$ from $X_1$ than distinguishing $X_{m-1}$ from $X_1$, hence why $(m-1)\epsilon \gt \epsilon$.
```

```admonish check collapsible=true title="Proof: Triangle Inequality for Computational Indistinguishability"
Suppose that there is an algorithm $\mathcal{A}$ running in time $T$ such that

$$\left|\Pr_{x\sim X_1}[\mathcal{A}(x) = 1] - \Pr_{x\sim X_m}[\mathcal{A}(x) = 1]\right| \gt (m-1)\epsilon$$

The left-hand side can be rewritten as

$$\Pr_{x\sim X_1}[\mathcal{A}(x) = 1] - \Pr_{x\sim X_m}[\mathcal{A}(x) = 1] = \sum_{i=1}^{m-1} \left(\Pr_{x\sim X_i}[\mathcal{A}(x) = 1] - \Pr_{x\sim X_{i+1}}[\mathcal{A}(x) = 1]\right)$$

Therefore, 
$$\sum_{i=1}^{m-1} \left(\Pr_{x\sim X_i}[\mathcal{A}(x) = 1] - \Pr_{x\sim X_{i+1}}[\mathcal{A}(x) = 1]\right) \gt (m-1)\epsilon$$

and hence there must be two distributions $X_i$ and $X_{i+1}$ for which

$$\left|\Pr_{x\sim X_i}[\mathcal{A}(x) = 1] - \Pr_{x\sim X_{i+1}}[\mathcal{A}(x) = 1]\right| \gt \epsilon$$

This contradicts the assumption that $X_i \approx_{T, \epsilon}$ for all $i \in \{1,2,...,m-1\}$.
```






