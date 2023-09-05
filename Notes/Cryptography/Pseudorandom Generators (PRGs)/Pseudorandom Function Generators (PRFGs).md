# Pseudorandom Functions
In order to understand what a pseudorandom function generator (PRFG) is, one needs to understand what it means for a function to be random or pseudorandom.

A truly random function $H: \{0,1\}^S \to \{0,1\}^{l_{\textit{out}}}$ is a function chosen according to the uniform distribution of all functions that take a string of length $S$ and output a string of length $\{0,1\}^{l_{\textit{out}}}$. Alternatively, a random function can be thought of as a function which outputs a random string of length $l_{\textit{out}}$ for every input $i \in \{0,1\}^S$, called an *input data block (IDB)*. This can be pictured as a table of all possible IDBs and their corresponding, at the beginning undetermined, outputs. Whenever $H$ is invoked with an IDB $i$, that IDB is looked up in the table. If its entry already has an output, then this value is directly returned. Otherwise, the function $H$ "flips a coin" $l_{\textit{out}}$ times to determine each bit of the output, fills the generated output in the table and finally returns it. Subsequent queries for the same input data block will provide the already generated output.

![](Resources/Images/Random%20Function.svg)

```admonish note
The input to a PRF may sometimes be treated as an integer between $0$ and $2^S - 1$, which can be represented as a binary string of length $S$. In these cases, it is called an *index* instead of an input data block.
```

The reason that these two notions of a random function are equivalent is that each "coin toss" can be thought of as making a step forward in search for the function $H$ which on input a specific $i$ outputs a specific output $o$. Before the first coin flip, there are $2^{l_{\text{out}}}$ possible outputs. After the first coin flip, there are $2^{l_{\text{out}} - 1}$ possible outputs - the first bit $b_0$ has been generated and the output has the form $b_0\cdots$ where the dots represent the remaining $l_{\text{out}} - 1$ bits, which are unknown. After the second flip, the output has two bits generated and $l_{\text{out}} - 2$ unknown bits - there are $2^{l_{\text{out}} - 2}$ remaining possibilities for the final output string. Each coin flip halves the number of possibilities for the output until the final flip settles on a single output. Since a function can only have a single output for a given input, deciding this output is like picking a function from all possible functions. The probability that we get a specific function $H$ is $\frac{1}{2^{l_{\text{out}}}}$ - the same as if simply choosing a function from a uniform distribution.

```admonish note
A random function is still *deterministic* in the sense that when input the same data block it will always give the same output.
```

Unfortunately, truly random functions present a great implementational challenge for classical computers due to their difficulty in obtaining true randomness. A computer cannot really "flip a coin $l_{\textit{out}}$ times" and is limited by its external [randomness sources](../Private-Key%20Cryptography/Security%20Notions/Randomness.md).

This is why we have to settle for *pseudorandom functions*.

```admonish danger title="Definition: Pseudorandom Function (PRF)"
A *pseudorandom function* is an efficient algorithm $\textit{PRF}(idb: \mathbf{str}[S]) \to \mathbf{str}[l_{\textit{out}}]$ such that for every efficient distinguisher $D(\textit{func}: \textbf{function<}\mathbf{str}[S] \to \mathbf{str}[l_{\textit{out}}]\textbf{>}) \to \mathbf{bit}$ it holds that

$$\left|\Pr[D(\textit{PRF}) = 1] - \Pr_{H \leftarrow_R \{0,1\}^S \to \{0,1\}^{l_{\text{out}}}}[D(H) = 1]\right| \le \epsilon(S)$$

for some negligible $\epsilon$.
```

```admonish tip title="Definition Breakdown"
The distinguisher $D(\textit{func}: \textbf{function<}\mathbf{str}[S] \to \mathbf{str}[l_{\text{out}}]\textbf{>}$ takes a function whose inputs are strings of length $S$ and which outputs a string of length $l_{\text{out}}$ and tries to determine if the function is a truly random function. This notation means that the distinguisher has *oracle access* to the function - it can freely query the function with any inputs and can inspect the resulting outputs. Sometimes, the objectively worse notation $D^f(1^S)$ is also used to denote that the distinguisher $D$ has oracle access to the function $f$.

A function is pseudorandom if there is no efficient distinguisher which can tell the difference between it and a truly random function $H$ which was chosen from the uniform distribution of all functions $\{0,1\}^S \to \{0,1\}^{l_{\text{out}}}$ with non-negligible probability.
```

Pseudorandom functions are useful because they are a generalisation of [pseudorandom generators](index.md). The length of the output of a PRG must always be greater than the length of its seed, but PRFs allow for an output whose length is independent of the input data block. Mostly, however, they are useful because they produce pseudorandom strings, just like PRGs. 

But as with most things in cryptography, it is unknown if pseudorandom functions actually exist. The definition is quite broad in the sense that there should be absolutely no distinguisher which can tell that the function is actually not truly random - a pretty difficult thing to do. So, once again, we are forced to hope that they do exist because otherwise cryptography falls apart - we consider a given algorithm to be a pseudorandom function until someone strings along and proves us wrong. Nevertheless, we still want to make as few assumptions as possible and build the rest on top of it.

```admonish question title="Assumption: Existence of a One-Bit Pseudorandom Function"
There exists a pseudorandom function $\textit{PRF}(idb: \mathbf{str}[S]) \to \mathbf{bit}$ which outputs a single bit, i.e. $l_{\text{out}} = 1$. 
```

As it turns out, such a pseudorandom function can be used to construct PRFs with any output length. 

# Pseudorandom Function Generators (PRFGs)
[Pseudorandom generators](index.md) produces pseudorandom strings, while pseudorandom function generators (PRFGs) produce pseudorandom functions. 

```admonish danger title="Definition: Pseudorandom Function Generator (PRFG)"
A *pseudorandom function generator (PRFG)* is an efficient algorithm $\textit{PRFG}(seed: \textbf{str}[S]) \to \textbf{function<}\textbf{int}[0..2^S-1] \to \textbf{str}[l_{\text{out}}]\textbf{>}$ which takes a seed $s \in \{0,1\}^S$ and outputs a pseudorandom function whose input is a data block of size $S$ and whose output is a string of length $l_{\text{out}}$.
```
```admonish tip title="Definition Breakdown"
A pseudorandom function generator takes a seed and produces a pseudorandom function. The resulting function takes input data blocks with the same length $S$ as the PRFG's seed and its outputs have length $l_{\text{out}}$. It is common to notate a PRF that was produced by PRFG as $f_s$ where $f$ is the function's name and $s$ is the seed used to obtain it.
```

It is important to remember that the output of a PRFG is a *function*. Specifically, a PRFG produces a function which takes inputs of the same size as the PRFG's seed. This coincidence has unfortunately led to PRFs and PRFGs commonly being mixed up. It is common to see a PRFG as a two input algorithm $\textit{PRFG}(seed: \textbf{str}[S], idb: \textbf{str}[S]) \to l_{\text{out}}$ that takes a seed $s$ *and* an input data block $i$ and acts like a pseudorandom function $f_s(i)$. In this case, $\textit{PRFG}(s,i)$ internally obtains the function $f$ from the seed $s$ and then passes it the data block $i$. Finally, the PRFG returns the output of the function $f$.

```rust
fn PRFG(seed: str[S], idb: str[S]) -> str[l_out] {
	let f = get_function_from_seed(seed);
	return f(idb);
}
```

## PRFGs from PRGs
Okay but how can we construct a PRFG algorithm? Well, as it turns out a [pseudorandom generators](index.md) can be used to construct such algorithms. In particular, a PRG $G(seed: \textbf{str}[S]) \to \textbf{str}[2S]$, which takes a seed of length $S$ and outputs a pseudorandom string of double that length, can be used to construct a pseudorandom function generator $PRFG(seed: \textbf{str}[S], idb: \textbf{str}[S]) \to \textbf{str}[S]$. TODO