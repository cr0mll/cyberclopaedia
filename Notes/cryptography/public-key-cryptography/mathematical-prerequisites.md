# Modular Arithmetic
Modular arithmetic is concerned with the arithmetic of *remainders* from division.

### Modulo Reduction
Dividing $a$ by $N$ can be written as $a = Nq + r$, where $q$ is the quotient and $r$ is the remainder. The modulo operation (`%`) returns the remainder $r$ when dividing $a$ by $N$. Programmatically, this is written as `a % N` and the mathematical equivalent is $a\mod N$. 

Mapping an integer $a$ to its remainder upon division by some number $N$ is known as *reduction modulo* $N$ and boils down to mapping the integer $a$ to an integer between $0$ and $N-1$. 

### Modulo Congruence
Two numbers are said to be *congruent modulo* $N$, written as $a = b \mod N$ (terrific notation, mathematicians) if they have the same remainder when dividing by $N$, i.e. $[a \mod N] = [b \mod N]$. The good thing about modulo congruence is that it under addition, subtraction and multiplication:

$$\begin{cases}a = a' \mod N \\ b = b' \mod N\end{cases} \iff \begin{cases}(a\pm b) = (a'\pm b') \mod N \\ ab = a'b' \mod N\end{cases}$$

### Modulo Inversion
If there is an integer $c$ such that $bc = 1 \mod N$, then $b$ is said to be *invertible* modulo $N$ and $c$ is said to be a (multiplicative) *inverse* of $b$ modulo $N$. A given integer $b$ may have many multiplicative inverses - for example, it is fairly easy to show that if $c$ is a multiplicative inverse of $b$, then so is $c \mod N$ and if $c'$ is yet another inverse of $b$, then $[c \mod N] = [c' \mod N]$. For simplicity, *the* multiplicative inverse of $b$ which is in the range $\{0, 1, ..., N - 1\}$ is denoted by $b^{-1}$. 

Modulo *division* by $b$ can then be defined as multiplication by $b^{-1}$ and this gives the following nice property:

$$ab = cb \mod N \implies (ab)b^{-1} = (cb)b^{-1} \mod N \implies a = c \mod N$$

# Groups
A *group* is simply a set $\mathbb{G}$ equipped with a group operation $\circ$ which satisfy the following properties:
- **Closure:** For all $g, h \in \mathbb{G}$, $g \circ h \in \mathbb{G}$
- **Identity:** There exists an identity element $e \in \mathbb{G}$ such that for all $g \in \mathbb{G}, g \circ e = g = e \circ g$
- **Invertibility:**  For each $g \in \mathbb{G}$ there exists an *inverse* element $h \in \mathbb{G}$ such that $g \circ h = e = h \circ g$
- **Associativity:** For all $g_1, g_2, g_3 \in \mathbb{G}, (g_1 \circ g_2) \circ g_3 = g_1 (\circ g_2 \circ g_3)$ 

A group whose operation also supports commutativity (i.e., $g \circ h = h \circ g$) is called *abelian*.

The order of a group, denoted by $|\mathbb{G}|$, is the number of elements in the group.

### Additive vs Multiplicative Notation
The group operation $\circ$ is often denoted in a different way.

*Additive notation* uses the $+$ sign for its group operation, i.e. $g \circ h \equiv g + h$. However, this does *not* mean that the group's operation is necessarily addition. The identity element here is denoted by $0$ and the inverse of an element $g$ is written as $-g$. Applying the group operation to a single element $g$ a total of $m$ times is denoted as

$$mg = \underset{m \text{ times}}{\underbrace{{g + g + \cdots + g}}}$$

Note that $m$ is an *integer* while $g$ is an element of the group and so $mg$ is *not* the group operation applied between $m$ and $g$.

*Multiplicative notation* denotes the group operation either by $g\cdot h$ or by $gh$. Once again, this does *not* mean that the group operation is necessarily multiplication - it is simply written this way. The identity element here is denoted by $1$ and the inverse of an element $g$ is written as $g^{-1}$. Applying the group operation to a single element $g$ a total of $m$ times is denoted via exponentiation:

$$g^m = \underset{m \text{ times}}{\underbrace{g\cdots g}}$$

Once again, $m$ is an *integer* and *not* a member of the group. This is useful notation because it truly "behaves" like exponentiation in regards to its properties: $g^m\cdot g^n = g^{m+n}, (g^m)^n = g^{mn}$ and $g^1 = g$. Furthermore, if the group $\mathbb{G}$ is abelian, then for all $g, h \in \mathbb{G}$ it holds that $g^m \cdot h^m = (gh)^m$. 

### Some Facts about Groups

```admonish info title="Lemma: Cancelation Law for Group Operations"
For all $a,b,c \in \mathbb{G}$, if $a\circ c = b \circ c$, then $a = b$ and in particular, if $ac = c$, then $a$ is the identity element of $\mathbb{G}$.
```

```admonish check collapsible=true title="Proof"
TODO
```

Interestingly, if the group is finite and $m = |\mathbb{G}|$, applying the group operation a single element $m$ number of times, then we get the identity element.

```admonish info title="Theorem"
For any finite group $\mathbb{G}$ and element $g \in \mathbb{G}$, it holds that g^{|\mathbb{G}|} = 1$.
```

```admonish check collapsible=true title="Proof"
TODO
```

As a corollary of this, it turns out that applying the group operation to the same element more than $|\mathbb{G}|$ times has the same effect as doing it $\mod |\mathbb{G}|$ times which brings computational benefits.

```admonish info title="Theorem"
For any finite group $\mathbb{G}$ with $|\mathbb{G}| \gt 1$ and any $g \in \mathbb{G}$, it holds that $g^x = g^{[x \mod |\mathbb{G}|]}$
```

```admonish check collapsible=true title="Proof"
```

### The Groups $\mathbb{Z}_N$ and $\mathbb{Z}_N^*$
The abelian group $\mathbb{Z}_N$ denotes the set of integers $\{0,1, ..., N - 1\}$ equipped with addition modulo $N$ as its group operation. The closure property is trivially satisfied because modulo reduction produces a number in the range $\{0,...,N_1\}$. Similarly, associativity and commutativity follow from the fact that integers have these properties. The identity element is $0$. Since $a + (N - a) = 0 \mod N$, it follows that the inverse of any element is $N - a$.

We would like to have a similar group but with multiplication modulo $N$ as the group operation. However, this is not trivial to do because even non-zero elements in $\{0,1,..., N -1\}$ might lack an inverse. It turns out that the elements in $\{0,1,..., N -1\}$ which *are* invertible modulo $N$ are precisely those integers which are relatively prime with $N$. Therefore, we can define the set for $\mathbb{Z}_N^*$ as follows:

$$\mathbb{Z}_N^* \coloneqq \{b \in \{1, 2, ..., N - 1\} | \gcd(b, N) = 1\} $$

We equip this set with the operation multiplication modulo $N$ to yield the abelian group $\mathbb{Z}_N^*$.

### Cyclic Groups
For any $g \in \mathbb{G}$, where $\mathbb{G}$ is some finite group, consider the following set:

$$\langle g \rangle \coloneqq \{g^0, g^1, g^2, ...\}$$

We know for sure that $g^{|\mathbb{G}|} = 1$. Let $i\le |\mathbb{G}|$ be the smallest positive integer such that $g^i = 1$. We know then that the sequence $\{g^0, g^1, g^2, ...\}$ repeats every $i$ elements, i.e. $g^i = g^0, g^{i+1} = g^1$, etc. Therefore,

$$\langle g \rangle = \{g^0, g^1, ..., g^{i-1}\}$$

It is not hard to verify that $\langle g \rangle$ is a subgroup of $\mathbb{G}$ of order $i$ and is thus said to be *generated* by $g$.  The integer $i$ is also sometimes simply referred to as the order of the element $g$.

There are some interesting properties of such elements.

```admonish info title="Lemma"
For any element $g$ of order $i$ in the finite group $\mathbb{G}$, it holds that $g^x = g^y$ if and only if $x = y \mod i$.
```

```admonish check collapsible=true title="Proof"
TODO
```

```admonish info title="Lemma"
The order $i$ of any element $g$ in a finite group $\mathbb{G}$, must be a factor of the group order, i.e. $i | m$, where $m$ is the order of $\mathbb{G}$.
```

```admonish check collapsible=true title="Proof"
TODO
```


```admonish tip title="Cyclic Groups"
A group $\mathbb{G}$ is called *cyclic* if all of its elements can be obtained by applying the group operation repetitevely to *one* of its elements.
```

The group $\mathbb{G}$ is called *cyclic*, if there is an element $g \in \mathbb{G}$ of order $|\mathbb{G}|$. Such an element is called a *generator* of $\mathbb{G}$. Therefore, any element $h \in \mathbb{G}$ is equal to $g^x$ for some $x \in \{0,1,..., |\mathbb{G}| -1\}$ - the group $\langle g \rangle$ has $|\mathbb{G}|$ elements and so does the group $|\mathbb{G}|$ and since $\langle g \rangle$ is a subgroup of $\mathbb{G}$, then they must contain the exact same elements.

Cyclic groups have some interesting properties.

```admonish info title="Theorem: Prime Order"
Any group $\mathbb{G}$ with a prime order $p$ is cyclic and all of its elements, except for the identity, are its generators.
```

```admonish check collapsible=true title="Proof"
The group order $p$ *must* be divisible by the order $i$ of any element and so $i = p$ or $i = 1$. Only the identity element has order $1$ and so all the other elements must be of order $p$ and are therefore generators of the group.
```

An immediate corollary of this theorem is that the group $\mathbb{Z}_p^*$, where $p$ is some prime number, is a cyclic group of order $p-1$.
