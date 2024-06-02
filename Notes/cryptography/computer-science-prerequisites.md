# Computer Science Prerequisites

## Algorithms

An algorithm/programme is a sequence of instructions which takes an input and produces an output. One might think that they are the same as mathematical functions, but that is _not_ the case. A function specify _what_ one wants to achieve and an algorithm tells us _how_ to achieve what we want. In a way, a function _specifies_ a problem and an algorithm _solves_ that problem.

````admonish
Consider the function $\textit{ADD}: \{0,1\}^* \times \{0,1\}^* \to \{0,1\}^*$ which takes two numbers represented using 2's complement and outputs their sum, again in 2's complement. This function is called *computable* because there is an algorithm which does exactly what the function says.

```rust
fn add(x: str, y: str) -> str {
	let i = max(x.len(), y.len()) - 1; // Iterating starts from the last - 1 element because indexing starts at 0
	let j = min(x.len(), y.len());
	let carry: bit = 0;
	
	let result: str[i+1]; // The result has the same length as the longest input
	
	while i > j {
		result[i] = xor(carry, )
	}
	// TODO
}
```
````

However, not every function is computable because not every problem has a solution. In fact, here is a problem which _cannot_ be solved by _any_ algorithm.

```admonish
Consider the function $H$ which takes an algorithm $A$ and an input for the algorithm $x$ and outputs 1 if and only if the algorithm does *not* enter an infinite loop when given $x$, i.e. the algorithm *halts*:

$$H(A, x) = \begin{cases}1, A(x) \text{ halts} \\ 0, A(x) \text{ does not halt}\end{cases}$$
```

This is called the _Halting problem_ and describes the situation where we want to know if a given programme gets stuck in an infinite loop. Being able to solve this problem would be exceptionally useful because it would mean that we could also for example make the ultimate antivirus detector. Unfortunately, the Halting problem is _uncomputable_. It is not that we do not _know_ how to solve it, it is just that the problem _cannot_ be solved. There is no algorithm $\textit{HALTS}$, and there never will be, which when given an arbitrary algorithm $A$ and input $x$ can decide if $A$ gets stuck when given $x$ as an input.

```admonish
The Halting problem is one of the best ways to illustrate the difference between functions and algorithms / programmes.
```

### Running Time

Some algorithms are inherently faster than others. Moreover, algorithms take more time to run on longer inputs. The way we measure how long an algorithm takes to run on a particular input is called its _time complexity_.

```admonish
The *time complexity* $T(n)$ of an algorithm is the number of atomic operations that the algorithm performs before completion when given an input of length $n$. We say that the algorithm runs in $T(n)$ time.
```

```admonish
The time complexity $T(n)$ is a function which depends on the input's length. An *atomic operation* is the most basic operation which the algorithm can perform and is assumed to always take a constant amount of time to run, which is why they serve as the units in which time complexity is measured.
```

Precisely what an _atomic operation_ is differs from one computational model to another. Cryptography operates on the bit-level and so it is most useful to use Boolean circuits to model it. This means that cryptography uses the [logical gates](mathematical-prerequisites.md) AND, OR, NOT and NAND. These operations take in two bits and output a single bit and we assume that our computer can only do these four operations - they are our atomic operations and have a running time equal to 1. Any other operations we might want to do will have to be defined using these four operations (which is very much possible, do not worry).

However, when actually analysing an algorithm's time complexity, one rarely stoops down to the level of Boolean gates. Instead the atomic operations are inferred from context and usually represent lines. Fear not, for these discrepancies are taken care of by [big-O notation](computer-science-prerequisites.md#admonition-definition-big-o-notation).

```admonish
Actually, the gates AND/OR/NOT can be computed by only using NAND gates, so NAND is the only gate which is really necessary. Nevertheless, we include the other three to make our lives easier.
```

#### Analysing Time Complexity

Analysing precise time complexity turns out be a highly non-trivial task and we are also not really interested in _precisely_ knowing how an algorithm's time complexity, but rather we simply want to know how this complexity changes as the input's length increases. For example, the difference between $T(n) = n^7$ and $T(n) = 3n^3 + n^2 + 3$ is much more significant than the difference between $T(n) = 3n^3 + n^2 + 3$ and $T(n) = 3n^3$. Furthermore, we are usually interested in the running time of the worst-case scenario. This is where _big-O notation_ comes in.

```admonish
For two functions $F,G: \mathbb{N} \to \mathbb{R}_+$ which take a natural number as an input and produce a non-negative real output:
- we say that $F = O(G)$ if there exists a constant $c$ and a number $N \in \mathbb{N}$ such that $F(n) \le c\cdot G(n)$ for every $n \gt N$
- we say that $F = \Theta(G)$ if $F = O(G)$ and $G = O(F)$, i.e. there exist two constants $c_1, c_2$ and a number $N \in \mathbb{N}$ such that $c_1 \cdot G(n) \le F(n) \le c_2 \cdot G(n)$ for every $n \gt N$
- we say that $F = \Omega(G)$ if $G = O(F)$
```

```admonish
The functions $F$ and $G$ are like functions which calculate time complexity - they take a natural number (the length of the input) and produce a number of steps:

- $F = O(G)$ means that $F$ is *upper-bound* by $G$, i.e. there is a constant $c$ by which we can multiply $G$ and then $F$ would always be smaller than $c\cdot G(n)$ for every input $n$ after some critical input $N$. This essentially tells us that as the input gets larger and larger, $F(n)$ will always remain smaller than $c \cdot G(n)$.
- $F = \Omega(G)$ means that $F$ is *lower-bound* by $G$, i.e. there is a constant $c$ by which we can multiply $G$ and then $F$ would always be bigger than $c \cdot G(n)$ for every input $n$ after some critical input $N$. This essentially tells us that as the input gets larger and larger, $F(n)$ will always remain bigger than $c \cdot G(n)$.
- $F = \Theta(G)$ means that $F$ is both *upper-* and *lower-bound* by $G$, i.e. $F$ is always between two functions which are constant multiples of $G$.
```

Since big-O notation describes bounds, it is very useful for our case of comparing time complexities. When we say that $T(n) = O(n^2)$, we are saying that the algorithm will complete in at most $c \times n^2$ steps for some constant $c$ and every input large input length $n$. The reason we compare running time for large values of $n$ is that if the input length is small, then it does not really matter if the algorithm runs in $O(n^2)$ or $O(n^3)$ time. However, as $n$ grows it becomes evident that an algorithm running in $O(n^3)$ is much slower than an algorithm which runs in $O(n^2)$.

```admonish
1. Multiplicative constants don't matter - if $F(n) = O(G(n))$ then so are:

$$100\cdot F(n) = O(G(n))$$

$$1000000 \cdot F(n) = O(G(n))$$

$$\frac{1}{100}F(n) = O(G(n))$$

2. When inspecting a function which is a sum of other functions, only the largest function is relevant:

$$n^4 + 2n^3 + 100003n^2 + n - 10000 = O(n^4)$$

$$2^n + n^2 - \ln(n) = O(2^n)$$

3. If a function is upper-bound by some other function, then it is also upper-bound by any function which upper-binds the binding function - if $F(n) = O(G(n))$ and $G(n) = O(P(n))$, then $F(n) = O(P(n))$.
```

These examples show that big-O notation only provides a relative idea of the performance of an algorithm in general as the input grows larger. For example, an algorithm that runs in $T(n) = 100000000000000 \cdot n$ time is "faster" than an algorithm that runs in $T(n) = n^2$ according to big-O notation because the first one is $O(n)$ and the second one is $O(n^2)$. But clearly, for most practical purposes, the second algorithm will be faster (if $n=1000$, then the second algorithm takes a million steps to complete while the first takes... well... calculate it if you can be bothered). Nevertheless, the constants which are concealed by big-O notation are rarely so big and therefore, we need not worry about such extreme cases in general.

Here is a graph which provides a general overview of how running times compare to one another:

![Wikipedia Image](https://upload.wikimedia.org/wikipedia/commons/7/7e/Comparison\_computational\_complexity.svg)

#### Efficient and Inefficient Algorithms

The time complexity of an algorithm tells us how the algorithm's performance scales as the input length grows larger and larger. It would be useful if there was a way to classify algorithms by their time complexity in order to obtain some useful information about their performance.

```admonish
An algorithm is *efficient* if its time complexity if its time complexity $T(n)$ is on the order of $O(n^c)$ for some constant $c$, i.e. there is a polynomial $p(n)$ of degree $c$ such that $T(n) \le p(n)$.
```

```admonish
Basically, we are saying that an algorithm is efficient if its time complexity is a at most polynomial in the input length $n$. 
```

Notice that this definition of "efficient" naturally includes algorithms whose time complexity is better than polynomial, for example algorithms with $T(n) = \sqrt{n}$. This is true due to the fact that $\sqrt{n} = O(n)$. Similarly an algorithm running in $\log\_2(n)$ time is considered efficient because $\log\_2(n)$ is upper bound by $n$, too.

An inefficient algorithm is then any algorithm that is not efficient.

## Problem Classes
