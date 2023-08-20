# Introduction
Randomness is the mainstay of modern cryptography. Designing ciphers is no trifling task and it is also important *how* a cipher's security is achieved. Essentially, an encryption scheme consists of three things - an encryption function, a decryption function and a key. One might think that a good way to ensure the cipher cannot be broken is to simply conceal the encryption and decryption process - after all, if the adversary does not know what they are breaking, how can they break it? 

Unfortunately, if the cipher *does* get broken (and it will by dint of reverse engineering), an entirely different cipher needs to be conceived because the previous one relied on security by obscurity. Quite the predicament, isn't it? 

```admonish warning title="Kerckhoff's Principle"
A cipher needs to be secure even if everything about it except the key is known. 
```

The reason why the key should be the only unknown variable is that keys are just strings of bits and are thus relatively easy to change in comparison to the other components of a cipher. But in order to be sure that the cipher is as secure as possible, the key must be completely random - no single key should be more likely to be used than any other.

# Obtaining Randomness
Cryptography requires randomness and it requires a lot of it, too. However, computers (at least classical ones) are entirely deterministic, so it turns out that randomness is actually quite difficult to come by. For example, a computer might use information from its temperature sensors or from surrounding electromagnetic noise. Nevertheless, these sources can only provide so many random bits and rarely satisfy the needs for randomness at a given time. 

So, it would be useful to be able to use these random bits to obtain *more* random bits, wouldn't it? However, there is a caveat. Since classical computers are deterministic, it is not really possible to obtain *truly* random bits, so we will have to settle for something that *looks* random.

## Statistical Tests
There is a caveat, however. Since classical computers are deterministic, it is not really possible to obtain *truly* random bits, so we will have to settle for something that *looks* random. But in order to determine what it means to *look random*, we must know what it means to *be random*. This is where *statistical tests* come in.

~~~admonish danger title="Definition: Statistical Test"
A *statistical test* is an algorithm $\textit{ST}(x: str[m]) \to bit$ defined as
$$\textit{ST}(x) = \begin{cases}1, \text{ the input } x \text{ appears random} \\ 0, \text{ the input } x \text{ does not appear random}\end{cases}$$
~~~

```admonish tip title="Definition Breakdown"
A statistical test is a definition of what "random" means.
```

Let's look at some possible statistical tests, or as we already saw, some possible *definitions of random*.

```admonish example
In a uniformly chosen string one would expect that the number of 0s and the number of 1s are approximately equal, so one possible statistical test is

$$\textit{ST}(x) = \begin{cases} 1, |\textit{Num}(0) - \textit{Num}(1)| \le 10\cdot \sqrt{n} \\ 0, \text{ otherwise} \end{cases}$$

where $m$ is the length of the binary string $x$.

Similarly, one would expect the longest sequence of 1s in a uniformly chosen string to be around $\log_2(m)$ and so another possible statistical test would be

$$\textit{ST}(x) = \begin{cases}1, \textit{LS1s}(x) \le \log_2(m) \\ 0, \text{ otherwise} \end{cases}$$
```

Since statistical tests can be pretty much anything and we have no way of really determining that a given statistical test is "better" than another, why don't we build our definition of what it means to "look random" by taking all the possible definitions for what "random is"?

```admonish danger title="Definition: Pseudorandomness"
A string of bits $s \in \{0,1\}^m$ is *pseudorandom*, i.e. *looks random*, if for every efficient statistical test $\textit{ST}$ running in time $p(m)$, where $p$ is some polynomial, it holds true that

$$\left| \Pr[\textit{ST}(s) = 1] - \Pr_{r \leftarrow_R \{0,1\}^m}[\textit{ST(r)} = 1] \right| \lt \frac{1}{p(m)}$$
```

```admonish tip title="Definition Breakdown"
Essentially, a string of bits $s$ with length $m$ is pseudorandom if there is no statistical test which can distinguish with non-negligible probability between it and a string uniformly chosen from all strings of length $m$. In other words, the difference between the probability that the statistical test classifies a string $s$ as random and that it classifies a uniformly chosen string as random should be very very small, i.e. negligible.
```

### Pseudorandom Generators
An algorithm which fulfils the task of generating more seemingly random bits from a smaller number of truly random bits is called a *pseudorandom generator (PRG)* - it takes a short string of random bits, called a *seed*, and expands them into a larger string of pseudorandom bits. 

```admonish danger title="Definition: Generator"
A *generator* is an efficient algorithm $\textit{Gen}(x: str[X]) \to str[R]$ where $R\gt X$ which takes a binary string as an input and produces a longer binary string as an output.
```

```admonish danger title="Definition: (Secure) Pseudorandom Generator (PRG)"
A (secure) *pseudorandom generator* $\textit{PRG}(seed: str[S]) \to str[R]$ is a generator such that for every input, called a *seed*, $s \in \{0,1\}^S$ and every efficient statistical test $\textit{ST}: \{0,1\}^R \to \{0,1\}$ which runs in time $p(R)$ for some polynomial $R$, the output $\textit{PRG}(s)$ is *pseudorandom*, i.e. it holds that

$$\left|\Pr[\textit{ST}(\textit{PRG}(s)) = 1] - \Pr_{r \leftarrow_R \mathcal{R}}[\textit{ST}(r) = 1]\right| \lt \frac{1}{p(R)}$$

The set $\mathcal{S} \coloneqq \{0,1\}^S$ is called the *seed space* and the set $\mathcal{R} \coloneqq \{0,1\}^R$ is called the *output space*.
```

```admonish tip title="Definition Breakdown"
This definition tells us that an algorithm $\textit{PRG}$ which takes a uniformly chosen binary string of length $S$ (i.e. "truly random" string), called a *seed*, and outputs a longer binary string of length $R$, is a pseudorandom generator if there is no efficient statistical test which can distinguish between $\textit{PRG}$'s output and a string chosen uniformly at random from the output space $\mathcal{R}$ with non-negligible probability.

Essentially, the definition says that the probability that any statistical test thinks a string generated by $\textit{PRG}$ is random is approximately equal to the probability that the same statistical test thinks a string uniformly chosen from $\mathcal{R}$ is random, i.e.

$$\Pr_{s\leftarrow_R \mathcal{S}}[\textit{ST}(\textit{PRG}(s)) = 1] \approx \frac{1}{|\mathcal{R}|}$$
```

It does not matter if you understand the nitty-gritty details of this definition for the security of a pseudorandom generator because it is one of the most useless pieces of information you will encounter in your lifetime. The reason for this is that there is no known PRG which has been proven to satisfy this definition because being able to prove it means that one is able to prove that $P \ne NP$.

Nevertheless, it gives us an idealised model for what a secure PRG *should* be.

### Determining the Security of a PRG
We can derive some properties from the definition of a PRG which can hint that a candidate PRG is secure and can be trusted.

```admonish info title="PRG Properties"
1. A secure PRG is *unpredictable* in the sense that there is no algorithm which given the first $i$ bits of the output of $\textit{PRG}$ can guess what the $i+1$ bit would be with probability that is non-negligibly greater than $\frac{1}{2}$. Similarly, an unpredictable PRG is secure.
2. A predictable PRG is *insecure*.
```

It can be proven that insecurity follows predictability and it can be proven that security means unpredictability (and vice versa).

```admonish check collapsible=true title="Proof: Unpredictability<p>&lrarr;</p>Security and Predictability<p>&rarr;</p>Insecurity"
1. Suppose, towards contradiction, that there exists an efficient algorithm $\mathcal{P}$ which given the bits $y[0], y[1], ..., y[i]$ of the output of a secure $\textit{PRG}$ can guess the bit $y[i+1]$ is probability greater than $\frac{1}{2} + \xi$ for some non-negligible $\xi$, i.e.
	
$$\Pr_{s \leftarrow_R \mathcal{S}}[\mathcal{P}(\textit{PRG}(s)|_{\{0,1,...,i\}}) = \textit{PRG}(s)_{i+1}] \gt \frac{1}{2} + \xi$$
	
We define a statistical test $\textit{ST}$ which outputs 1 only if $
```

However, these two properties only provide a potential way to rule out an PRG as insecure. Proving the first property is equally difficult as proving that a PRG is secure, since it is essentially an equivalent definition of security for a PRG.  

```admonish note
At the end of the day we just *assume* that secure generators exists. In fact, we have many PRGs that we believe to be secure but are just unable to prove it. Similarly, we have many PRGs that have been shown to be *insecure* and should not be used. So really, we consider a PRG to be secure until someone comes along and shows a way to break it. Since we have no better alternative, i.e. we do not know how to prove that a PRG is secure, we are forced to take the leap of faith and make-do with what we have. 
```


