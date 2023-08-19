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

### Statistical Tests
But now comes the problem of what does it mean to "appear to random" or to be "indistinguishable from random". This is where *statistical tests* come in.

```admonish danger title="Definition: Statistical Test"
A *statistical test* is an algorithm $\textit{ST}: \{0,1\}^m \to \{0,1\}$ such that $\textit{ST}(x) = 1$ if the input $x$ appears random and $\textit{ST}(x) = 0$ if the input $x$ does *not* appear random.
```

```admonish tip title="Definition Breakdown"
A statistical test is just a way to determine if a string of bits appears random according to some definition of what "appears to be random" means. In a sense, every statistical test is a different definition of what "random" is.
```

Okay, so a statistical test is a way to determine if a string is random according to some definition of "random".

```admonish example
In a uniformly random string one would expect that the number of 0s and the number of 1s are approximately equal, so one possible statistical test is

$$\textit{ST}(x) = \begin{cases}1, |\textit{Num}(0)} - \textit{Num}(1)| \le 10\times \sqrt{n}\\ 0, \text{ otherwise} \end{cases}$$

where $m$ is the length of the binary string $x$.

Similarly, one would expect the longest sequence of 1s in a uniformly random string to be around $\log_2(m)$ and so another possible statistical test would be

$$\textit{ST}(x) = \begin{cases}1, \textit{Longest string of 1s}(x) \le \log_2(m) \\ 0, \text{ otherwise} \end{cases}$$
```

### Pseudorandom Generators
```admonish tldr
A pseudorandom generator is an algorithm which takes a small number of random bits and produces more random bits.
```

An algorithm which fulfils the task of generating more seemingly random bits from a smaller number of truly random bits is called a *pseudorandom generator (PRG)* - it takes a short string of random bits, called a *seed*, and expands them into a larger string of bits which *appear to be random* (hence the "pseudo"). 

```admonish danger title="Definition: Pseudorandom Generator"
A *pseudorandom generator (PRG)* is an efficiently computable function $\textit{PRG}: \mathcal{S} \to \mathcal{R}, where $\mathcal{S} \coloneqq \{0,1\}^S$ is called the *seed space*, $\mathcal{R} \coloneqq \{0,1\}^R$ is called the *output space* and $R \gt S$. 
```

```admonish danger title="Definition: Security of a PRG"
A pseudorandom generator $\textit{PRG}$ is *secure* if for every seed $s \in \mathcal{S}$ and every efficient statistical test $\textit{ST}: \mathcal{R} \to \{0,1\}$ it holds that

$$|\Pr_{s\leftarrow_R \mathcal{S}}[\textit{ST}(\textit{PRG}(s)) = 1] - \Pr_{r \leftarrow_R \mathcal{R}}[\textit{ST}(r) = 1]| \text{ is negligible}$$
```

```admonish tip title="Definition Breakdown"
This definition tells us that an algorithm $\textit{PRG}$ which takes a uniformly random binary string of length $S$ (i.e. "truly random" string), called a *seed*, and outputs a longer binary string of length $R$, is a pseudorandom generator if there is no efficient statistical test which can distinguish between $\textit{PRG}$'s output and a string chosen uniformly at random from the output space $\mathcal{R}$ with non-negligible probability.

Essentially, the definition says that the probability that any statistical test thinks a string generated by $\textit{PRG}$ is random is approximately equal to the probability that the same statistical test thinks a string uniformly chosen from $\mathcal{R}$ is random, i.e.

$$\Pr_{s\leftarrow_R \mathcal{S}}[\textit{ST}(\textit{PRG}(s)) = 1] \approx \frac{1}{|\mathcal{R}|}$$
```

It does not matter if you understand the nitty-gritty details of this definition for the security of a pseudorandom generator because it is one of the most useless pieces of information you will encounter in your lifetime. The reason for this is that there is no known PRG which has been proven to satisfy this definition because being able to prove it means that one is able to prove that $P \ne NP$.

Nevertheless, it gives us an idealised model for what a secure PRG *should* be.

### Determining the Security of a PRG
We can derive from it certain properties from the definition for security of a PRG which can hint that a candidate PRG is secure and can be trusted.

```admonish info title="PRG Properties"
1. A secure PRG is *unpredictable* in the sense that there is no algorithm which given the first $i$ bits of the output of $\textit{PRG}$ can guess what the $i+1$ bit would be with probability that is non-negligibly greater than $\frac{1}{2}.
2. A predictable PRG is *insecure*.
```

It can be proven that insecurity follows predictability and it can be proven that security means unpredictability.

```admonish check title="Proof: Unpredictability<p>&rarr;</p>Security and Predictability<p>&rarr;</p>Insecurity"
1. Suppose, towards contradiction, that there exists an efficient algorithm $\mathcal{P}$ which given the bits $y[0], y[1], ..., y[i]$ of the output of a secure $\textit{PRG}$ can guess the bit $y[i+1]$ is probability greater than $\frac{1}{2} + \Epsilon$ for some non-negligible $\Epsilon$, i.e.
	
	$$\Pr_{s \in \mathcal{S}}[\mathcal{P}(\textit{PRG}(s)|_{\{0,1,...,i\}}) = textit{PRG}(s)|_{i+1}}] gt \frac{1}{2} + \Epsilon$$
	We define a statistical test $\textit{ST}$ which outputs 1 only if $
```

However, these two properties only provide a potential way to rule out an PRG as insecure. At best, if the first property is proven for some PRG, then it only suggests that the PRG *might* be secure but not necessarily that it *is* secure. A different way to break the PRG might still be found even if the PRG is unpredictable.

```admonish note
At the end of the day we just *assume* that secure generators exists. In fact, we have many PRGs that we believe to be secure but are just unable to prove it. Similarly, we have many PRGs that have been shown to be *insecure* and should not be used. So really, we consider a PRG to be secure until someone comes along and shows a way to break it. Since we have no better alternative, i.e. we do not know how to prove that a PRG is secure, we are forced to take the leap of faith and make-do with what we have. 
```


