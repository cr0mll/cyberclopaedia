# Pseudorandom Permutations
A *pseudorandom permutation (PRP)* is a specific type of [pseudorandom function (PRF)](Pseudorandom%20Function%20Generators%20(PRFGs).md).

```admonish danger title="Definition: Pseudorandom Permutation (PRP)"
A *pseudorandom permutation* $\textit{PRP}(\textit{idb}: \textbf{str}[l]) \to \textbf{str}[l]$ is a pseudorandom function which satisfies the following properties:

- The output length $l_{\text{out}}$ is the same as the input length $l$, i.e. $l_{\text{out}} = l$.
- The function $\textit{PRP}$ is a permutation of $\{0,1\}^l$, i.e. the function is bijective.
- The function is *reversible*, i.e. there is an efficient algorithm $\textit{RevPRP}$ such that $\textit{RevPRP}(\textit{PRP}(x)) = x$ for all $x \in \{0,1\}^l$.
```

```admonish tip title="Definition Breakdown"
A pseudorandom permutation is a subtype of a pseudorandom function where the output length matches the input length $l$. Furthermore, a PRP is a [bijection](../Mathematical%20Prerequisites.md#admonition-injection-surjection-and-bijection) which maps each binary string of length $l$ to a single binary string, also of length $l$. Finally, the PRP must be reversible in the sense that there is an efficient algorithm which can recover the input that was passed to the PRP in order to obtain a specific output.

The input/output length is often called the *block length*.
```

Pseudorandom permutation are useful in the construction of block ciphers because they have inputs and outputs of the same length. 

### Theoretical Implementation - PRPs from PRFs
Since PRPs are a subtype of PRFs, it is not unreasonable to believe that the latter can be used to construct the former. In particular, three pseudorandom functions $f_1, f_2, f_3: \{0,1\}^S \to \{0,1\}^S$ with equal-length inputs and outputs can be used to construct a pseudorandom permutation $\textit{PRP}(\textit{idb}: \textbf{str}[2S]) \to \textbf{str}[2S]$ whose block length is twice that of the original function, i.e $l = 2S$.

```admonish note
This is purely a theoretical construct used solely for illustrative purposes and it is *not* utilised in practice.
```

To construct such a PRP from three such PRFs, we use several rounds of the so-called [Feistel transformation](https://en.wikipedia.org/wiki/Feistel_cipher). Our PRP begins by parsing its input $x \in \{0,1\}^{2S}$ as two separate strings $x_1, x_2$ by splitting it in half, i.e. $x_1 \coloneqq x[0..S]$ and $x_2 \coloneqq x[S..]$. It then invokes $f_1(x_2)$ and XORs its output with $x_1$  to produce the value $y_1 = f_1(x_2) \oplus x_1$. Subsequently, the PRP calls the next pseudorandom function $f_2$ on $y_1$ and XORs its output with $x_2$ to produce the value $y_2 = f_2(y_1) \oplus x_2$. The penultimate step is to produce the value $z = f_3(y_2) \oplus y_1$ by invoking the third pseudorandom function $f_3$ on $y_2$ and XOR-ing its output with $y_1$. Finally, our PRP outputs the concatenation of $z$ and $y_2$.

![](Resources/Images/PRP%20Theoretical%20Implementation.svg)

```rust
fn PRP(input: str[2S]) -> str[2S]
{
	let x1 = input[0..S];
	let x2 = input[S..];
	
	let y1 = xor(f1(x2), x1);
	let y2 = xor(f2(y1), x2);
	
	let z = xor(f3(y2), y1);
	
	return z + y2;
}
```

All operations used are efficient and they are also used a fixed number of times for any input which means that this PRP is indeed efficient. Moreover, it is easily reversible simply by executing these operations in reverse order.

```rust
fn RevPRP(input: str[2S]) -> str[2S]
{
	let z = input[0..S];
	let y2 = input[S..];
	
	let y1 = xor(f3(y2), z);
	
	let x2 = xor(f2(y1), y2);
	let x1 = xor(f1(x2), y1);
	
	return x1 + x2;
}
```

The more arduous task is proving that this permutation is indeed pseudorandom.

```admonish check collapsible=true title="Proof of Pseudorandomness"
TODO!
```

# Pseudorandom Permutation Generator (PRPG)
Since PRPs are a subtype of PRFs and [pseudorandom function generators (PRFGs)](Pseudorandom%20Function%20Generators%20(PRFGs).md) are a way to produce pseudorandom functions, we can reason about a restricted subtype of PRFGs which produce pseudorandom permutations.

```admonish danger title="Definition: Pseudorandom Permutation Generator (PRPG)"
A *pseudorandom permutation generator* $\textit{PRPG}(\textit{seed}: \textbf{str}[S]) \to \textbf{function<}\textbf{str}[S] \to \textbf{str}[S]\textbf{>}$ is a pseudorandom function generator which takes a seed $s \in \{0,1\}^S$ and outputs a pseudorandom permutation over $\{0,1\}^S$.
```

```admonish tip title="Definition Breakdown"
A PRPG is a PRFG for pseudorandom permutations. The block length of the PRPs produced by a given PRPG is the same as the length $S$ of the seed used for it.

As with PRFs, it is common to denote the function output by a PRPG for some particular seed $s$ as $\textit{PRP}_s$.
```

Similarly to PRFGs, it is important to remember that the output of a PRPG is still a *function*. Nevertheless, this did not stop mathematicians' folly before and it certainly will not stop it now - it is common to see a PRPG as a two input algorithm $\textit{PRPG}(\textit{seed}: \textbf{str}[S], idb: \textbf{str}[S]) \to \textbf{str}[S]$ that takes a seed $s$ and an input data block $i$ and acts like a pseudorandom permutation $\textit{PRP}_s(i)$. In this case, $\textit{PRPG}(s,i)$ internally obtains the function $\textit{PRP}_s$ from the seed $s$ and then passes it the data block $i$. Finally, the PRPG returns the output of the permutation $\textit{PRP}_s$.

```rust
fn PRPG(seed: str[S], idb: str[S]) -> str[S] {
	let PRP = get_prp_from_seed(seed);
	return PRP(idb);
}
```
