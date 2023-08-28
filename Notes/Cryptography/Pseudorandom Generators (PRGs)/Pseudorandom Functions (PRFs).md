# Introduction
Pseudorandom functions (PRFs) are a generalisation of pseudorandom generators. They take a seed and an integer and produce a single bit.

```admonish danger title="Definition: Pseudorandom Function (PRF)"
A *pseudorandom function (PRF)* is an efficient algorithm $\textit{PRF}(seed: \textbf{str}[S], index: \textbf{int}[0..2^S - 1]) \to \textbf{bit}$ which takes a seed $s \in \{0,1\}^S$ of length $S$ and an integer $i \in \{0,1,...,2^S - 1\}$, called an *index*, and outputs a single bit.

The seed may also be denoted as a subscript - $\textit{PRF}_s(i)$.
```

In its core, a PRF is just a function which produces a single bit at a time. However, what does the "pseudorandom" stand for in this case? The answer is that it is related to the *security* of the PRF.

```admonish danger title="Definition: Security of a PRF"
A pseudorandom function $\textit{PRF}(seed: \textbf{str}[S], index: \textbf{int}[0..2^S - 1]) \to \textbf{bit}$ is *secure* if for every seed $s$ and efficient distinguisher $D(input: \textbf{str}[t]) \to \textbf{bit}$ that has oracle access to $\textit{PRF}_s$,

$$\left|\Pr_{\tau \leftarrow_R \{0,1\}^t}[D^{\textit{PRF}_s} (\tau) = 1] - \Pr_{H \leftarrow_R ([2^t] \to \{0,1\})}[D^H(\tau) = 1] \right| \le \epsilon(t)$$

for some negligible $\epsilon$.
```

```admonish tip title="Definition Breakdown"
*Oracle / Black-box* access means that the distinguisher can query $\textit{PRF}_s$ with any index $i$ and do any number of times, so long as it is polynomial in $t$ (otherwise the distinguisher itself won't be efficient). Whilst the distinguish eris free to choose the indices it queries, it neither knows nor is allowed to change the seed. A PRF is then secure if no distinguisher can tell with non-negligible probability the difference between a string that was obtain from $\textit{PRF}_s$ using some indices $i_0, i_1, ..., i_{t-1}$ and a string that was produced by concatenating sequential bits obtained from a truly random function $H$.
```

A truly random function $H(index: \textbf{int}[0..2^t - 1]) \to \textbf{bit}$ is a function which outputs a random bit for every index. Note, however, that $H$ is still deterministic - it always outputs the same bit if the same index is used. One can picture such a function as a table of all possible indices and their corresponding, at the beginning undetermined outputs. Whenever $H$ is invoked with an index $i$, that index is looked up in the table. If its entry already has an output associated, then this value is directly returned. Otherwise, the function $H$ "flips a coin" to determine if the output for this index should be 1 or 0, fills it in the table and then returns it. 

### PRGs from PRFs
It is obvious that we can build a pseudorandom generator$\textit{PRG}(seed: \textbf{str}[S]) \to \textbf{str}[R]$ from a pseudorandom function by simply running the PRF for each index between $0$ and $R - 1$. In order for the constructed PRG to be secure, it is necessary that the PRF used must be, too. Recall that a secure PRG is *unpredictable*. Since the PRF is used to generate the output of the PRG one bit at a time, then the only way for the PRG to be unpredictable is if the PRF is also unpredictable.

```admonish info title="PRF Unpredictability"
A secure $\textit{PRF}_s$ is unpredictable in the sense that there is no efficient predictor algorithm $P$ which takes the bits $y[0],y[1],...,y[i]$ output by the PRF for the indices $\{0,1,...,i\} and can guess $\textit{PRG}_s(i+1)$ with probability better than $\frac{1}{2} + \epsilon$ for some negligible $\epsilon$.
```

Essentially, the unpredictability of a PRF translates directly into the unpredictability of any PRG that is built from it.

### PRFs from PRGs
Interestingly enough, the converse direction is also true - a secure PRG can be used to construct a secure PRF. To illustrate this, we are going to show that we can use a secure pseudorandom generator $G(seed: \textbf{str}[S]) \to \textbf{str}[2S]$, which expands a seed of size $S$ into a string twice that size, to construct a secure pseudorandom function $F$.

---

#### Further Reading
- Alternative Definition of security
A pseudorandom function $\textit{PRF}$ is *secure* if for every efficient adversary $\mathcal{A}$ which takes the bits $\textit{PRF}_s(0), \textit{PRF}_s(1), ..., \textit{PRF}_s(i)$, the probability that $\mathcal{A}$ can guess $\textit{PRF}_s(i+1)$ is only negligibly greater than $\frac{1}{2}$.

$$\Pr_{s \leftarrow_R \mathcal{S}}[\mathcal{A}(\textit{PRF}_s(0), \textit{PRF}_s(1), ..., \textit{PRF}_s(i)) = \textit{PRF}_s(i+1))] = \frac{1}{2} + \epsilon(S)$$

for some negligible $\epsilon$.
