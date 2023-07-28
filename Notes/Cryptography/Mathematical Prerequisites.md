# Sets
A *set* is simply a collection of objects, called its *elements* or *members*. The name of a set is typically denoted with an upper case letter ($A, B, C, S, ...$) while its elements are usually denoted with lower case letters ($a, b, c, s, ...)$. Sets can contain any type of object you can imagine such as numbers, letters, cars, phones, people, countries, etc. and they can contain objects of multiple types. Furthermore, since a set is itself a type of object, sets are allowed to contain other sets, too. Nevertheless, sets most often contain numbers because they are primarily used in a mathematical context.

```admonish info title="Set Representation"
There are three main ways to represent and define sets.

The *descriptive form* uses words to describe a set. For example, the set $S$ is the set of all odd natural numbers which are less than 12.

The *set-builder form* defines a set by specifying a condition that all of its members satisfies and looks like this:

$$\text{set } = \{\text{ placeholder }|\text{ condition }\}$$

The placeholder is simply there so you can use it to more easily write the condition. The `|` character can be read as "such that". For example, specifying the aforementioned set $S$ using set-builder notation will look like the following.

$$S = \{s|s \text{ is an odd number and } 0 \lt s \lt 12\}$$

The final way to define a set is simply by listing all of its elements or listing enough of them, so that whoever is reading the definition can easily establish the pattern they follow. For example, the aforementioned set will be written as

$$S = \{1,3,5,7,9,11\}$$
```

To state that an object is a member of a particular set, we notate $s \in S$. To show that an object is *not* a member of a particular set, we use $s \notin S$. A *subset* of a set $S$ is a set whose elements are all also element of $S$. For example, if $S = \{1,2,3,4\}$ and $S' = \{2,4\}$, then $S'$ is a subset of $S$ and this is denoted by $S'\subset S$. If we are unsure whether a set is a subset or is in fact equal to another set, then instead of $\subset$ we use $\subseteq$.

```admonish tip title="Special Sets"
- $\emptyset$ - the empty set, which is the set with *no* elements and is considered to be a subset of every set
- $\mathbb{N} = \{0,1,2,3,...\}$ - the set of all natural numbers; some definitions include zero while others do not, here it is included for simplicity
- $\mathbb{N}_0$ - the set of all natural numbers with 0 explicitly included
- $\mathbb{Z} = \{...,-2,-1,0,1,2,...\}$ - the set of all integers
- $\mathbb{Q}$ - the set of all rationals numbers, i.e. numbers which can be represented as the division of two integers
- $\mathbb{R}$ - the set of all real numbers; this is the set of all the rational numbers and all the irrational numbers such as $\pi$ and $e$
```

### Set Size
The number of elements in a set is called its *cardinality* and is denoted by $|S|$. For example, the set $\{0,1,4,17\}$ has a cadinality equal to 4. Some sets like this one have a finite number of elements, but others, such as the set of all natural numbers, do not. The latter are called *infinite sets*.

```admonish note
If a set contains more than a single copy of one of its elements, the additional copies are not taken into account. For example, $\{1,2,3,4,1,5,2\}$ is mathematically considered the exact same set as $\{1,2,3,4,5\}$ and so the size of both sets is 5.
```

### Set Operations
The *union* of two sets, denoted by $A\cup B$, is a set which contains all the elements from $A$ and $B$. For example,

$$\{0,1,4,17\} \cup \{1,2,3,4,5\} = \{0,1,2,3,4,5,17\}$$

The *intersection* of two sets, denoted by $A\cap B$, is a set which contains only the elements which are found in both $A$ and $B$. For example,

$$\{0,1,4,17\} \cap \{1,2,3,4,5\} = \{1,4\}$$

```admonish note
If the two sets have no elements in common, then their intersection is the empty set $\emptyset$.
```

The *relative complement* of a set $A$ with respect to another set $B$, denoted by $A - B$, is the set obtained by removing from $A$ all of its elements that are also found in $B$. For example,

$$\{0,1,4,17\} - \{1,2,3,4,5\} = \{0,17\}$$
$$\{1,2,3,4,5\} - \{0,1,4,17\} = \{2,3,5\}$$

### Strings
A *string* is a sequence of characters. The set of characters that we can choose from to make our string is called an *alphabet* and is usually denoted by $\Sigma$. For example, if $\Sigma = \{a,b,c,d\}$, then some valid strings over that alphabet will be `abcd`, `ac`,`acd`,`c`, etc.

The set of all strings with a certain length $n$ over some alphabet $\Sigma$ is denoted by $\Sigma^n$. For example, the set of 2-letter strings which we can make from $\{a,b,c\}$ is 

$$\{a,b,c\}^2 = \{aa,ab,ac,ba,bb,bc,ca,cb,cc\}$$

If we wanted to denote the set of all possible strings of any finite length over a given alphabet $\Sigma$, then we would write $\Sigma^*$ or, for our example, $\{a,b,c,d\}^*$. This would be the set of all strings which can be written with the letter a,b,c and d such as `ab` or `aaccdba`.

```admonish tip title="Special Strings"
- the empty string "" which has no characters and can be constructed with any alphabet
- binary strings $\{0,1\}^*$ - strings which only contain 0s and 1s
```

### Summary
```admonish summary
Membership:
- $s$ is a member of $S$ - $s \in S$
- $s$ is *not* a member of $S$ - $s \notin S$
- $S'$ is a strict subset of $S$ - $S' \subset S$
- $S'$ is either a subset or is equal to $S$ - $S' \subseteq S$

Cardinality:
- $|S|$ - the number of elements in $S$

Set Operations:
- union of $A$ and $B$ - $A \cup B$
- intersection of $A$ and $B$ - $A \cap B$
- relative complement of $A$ with respect to $B$ - $A - B$

Strings:
- string - a sequence of characters
- alphabet $\Sigma$ - the set of characters we can choose from to make our string
- the set of all strings with a certain length $n$ over some alphabet $\Sigma$ - $\Sigma^n$
- the set of all strings over some alphabet $\Sigma$ - $\Sigma^*$
- binary strings - $\{0,1\}^*$
```

# Functions
A *function* takes an input and produces an output. The inputs of a function are called its *arguments* and can be different types of objects and so can its output. For example, a function may take in a natural number and a binary string and may output a single bit. The types of the inputs and outputs of the functions are specified by sets in its *declaration* which has the following syntax:

$$\text{name}: \text{input set 1} \times \text{input set 2} \times \cdots \to \text{output set 1} \times \text{output set 2} \times \cdots$$

```admonish example

Consider the following function:

$$F: \{0,1\}^3 \to \{0,1\}$$ 

We do not know what precisely this function does, but we know that it takes a binary string of length 3 and outputs a single bit - 0 or 1. Similarly, the function

$$F: \mathbb{N} \times \{0,1\}^* \to \{0,1\}^* \times \{0,1\}^*$$

takes in a natural number and a binary string of any length and outputs two binary strings of arbitrary length, too. An example of such a function would a function which splits a given binary string at the position indicated by the natural number and returns the two split parts.
```

The input sets are called the function's *domain* and *codomain*.

## Function Definition
A function *definition* describes what the function outputs given a particular input and has the syntax

$$\text{name}(\text{arg1},\text{arg2},...) \coloneqq \text{expression}$$

The *expression* can be a mathematical formula, it can be a sentence explaining what the function does, or it can be a mixture of both.

```admonish example
The function $f: \mathbb{R} \to \mathbb{R}$ which returns the square of its input would be defined as follows:

$$f(x) \coloneqq x^2$$

The $x$ is just an arbitrary placeholder for the argument - we could have very well used $y$ or a word or anything we would like.

The function $PALINDROME: \{0,1\}^* \to \{0,1\}$ is the function which outputs 1 if its input is a palindrome string and outputs 0 otherwise. This was an example of a definition with a sentence.
```

Functions can also be *piecewise-defined*. This is when the function does different things depending on whether its input satisfies a given condition. For example, the $EVEN: \mathbb{N} \to \{0,1\}$ function can be defined as:

$$EVEN(n) \coloneqq \begin{cases}1, \text{if } n \text{ is even} \\ 0, \text{if } n \text{ is odd} \end{cases}$$

The absolute value function $||: \mathbb{R} \to \mathbb{R}$ is also piecewise-defined:

$$|x| \coloneqq \begin{cases}-x, x \lt 0 \\+x, x \ge 0\end{cases}$$

Finally, a function can be specified by a table listing all its inputs and their corresponding outputs. For example,

|$x$|$g(x)$|
|:--:|:---:|
|0|4|
|2|17|
|3|1|
|4|26|
|...|...|

This does not give us a very good idea of what the function $g$ is actually supposed to do, but it certainly is a way to define it.

```admonish tip title="Partial & Total Functions"
A function need not be defined for all values in its domain. For example, the division function $DIV: \mathbb{R} \times \mathbb{R} \to \mathbb{R}$, or alternatively $DIV(a,b) = \frac{a}{b}$, is not defined for $b = 0$ because one cannot divide by 0. Such functions are called *partial* and the set of all values for which the function is actually defined is called its *natural domain*. This can be seen from the following diagram for a function $f: X \to Y$:

![](Resources/Images/Function%20Domain.svg)

The domain is $X$, while the natural domain is $\{x_1,x_2,x_3,...\} \subset X$. A function which is defined for *all* values in its domain is called a *total* function.
```

```admonish tip title="Injection, Surjection and Bijection"
These are terms which describe the relationship a function establishes between its input sets and its output sets.

An *injective* function, or one-to-one function, is a function which given two different inputs, will always produce two different outputs - every element in its input sets is mapped to a single element from its output sets. An example of such a function is $f(x) = x + 1$ - there are no two inputs $x \ne x'$ for which $f(x) = f(x')$. However, the function $g(x) = x^2$ is *not* an  injection because opposite numbers produce the same output, i.e. $g(2) = g(-2) = 4$.

A *surjective* function is a function which covers its entire codomain. For example, $f: \mathbb{R} \to \mathbb{R}$ with $f(x) = x + 1$ is a surjection because every real number can be produced from it, i.e. for every $y \in \mathbb{R}$ there is at least one number $x$ such that $f(x) = y$. Contrastingly, the absolute value function $||: \mathbb{R} \to \mathbb{R}$ is *not* surjective because it cannot produce negative values. The subset of the codomain which contains all values which can be obtained from the function is called the function's *image*.

A *bijective* function, also known as a one-to-one map or one-to-one correspondence, is a function which is both surjective and injective, i.e. it covers its entire codomain and assigns to every element it in it, only *one* element from its natural domain.

![](Resources/Images/Injection,%20Surjection,%20Bijection.svg)

```

## Logical Operations
There are a few functions used extensively throughout cryptography and computer science. Although they are defined on single bits, every one of them can be extended to binary strings simply by applying the function on a bit-by-bit basis.

### Logical NOT
The $NOT: \{0,1\} \to \{0,1\}$ function takes a single bit and flips its value - if the bit is 0 it becomes 1 and if it is 1 it becomes zero.

|a|NOT(a)|
|:--:|:---:|
|0|1|
|1|0|

```admonish note title="Notation"
The function $NOT(a)$ can also be written as $\neg a$.
```

### Logical AND
The $AND: \{0,1\} \times \{0,1\} \to \{0,1\}$ function takes two bits and outputs 1 only if both bits are equal to 1.

|a|b|AND(a,b)|
|:--:|:--:|:--:|
|0|0|0|
|0|1|0|
|1|0|0|
|1|1|1|

```admonish note title="Notation"
The function $AND(a,b)$ can also be written as $a \land b$.
```

### Logical OR
The $OR: \{0,1\} \times \{0,1\} \to \{0,1\}$ function takes two bits and outputs 1 if either one (or both) of them is 1.

|a|b|OR(a,b)|
|:--:|:--:|:--:|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|1|

```admonish note title="Notation"
The function $OR(a,b)$ can also be written as $a \lor b$.
```

### Exclusive OR
The eXclusive OR function, $XOR: \{0,1\} \times \{0,1\} \to \{0,1\}$, is similar to the logical OR operation, however it outputs 1 if either one of its inputs is 1, but not both.

|a|b|XOR(a,b)|
|:--:|:--:|:--:|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0|

```admonish note title="Notation"
The function $XOR(a,b)$ can also be written as $a \oplus b$.
```

This function is ubiquitous in cryptography due to its four essential properties:

|Property|Formula|
|:----:|:----:|
|Commutativity|$A \oplus B = B \oplus A$|
|Associativity|$(A \oplus B) \oplus C = A \oplus (B \oplus C)$|
|Identity|$A \oplus 0 = A$|
|Involution|$A \oplus B = C \implies \begin{cases}A = C \oplus B \\ B = C \oplus A\end{cases}$|

*Commutativity* means that the two inputs can change places and the output would still be the same. *Associativity* means that, given a chain of XOR operations, the order in which they are executed is irrelevant to the final result. *Identity* indicates that there is a specific input, called the *identity element*, for which the XOR operation simply outputs the other input.

*Involution* is a fancy way of saying that XOR is its own inverse operation. Given the output of a XOR operation and one of its inputs, the other input can be obtained by XOR-ing the output with the known input.

```admonish tip title="XOR(a,a)"
Another interesting property of $XOR$ is that XOR-ing a bit with itself will always produce 0. This is often used in computers to reset a [register](../Reverse%20Engineering/Assembly%20Programming/x86-64/Registers.md) to 0. 
```