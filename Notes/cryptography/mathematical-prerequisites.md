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


## Negligible Functions
```admonish danger title="Definition: Negligible Function"
A function $\mu :\mathbb{N} \to [0,1]$ is *negligible* if for every polynomial $p: \mathbb{N} \to \mathbb{N}$ there exists a number $N \in \mathbb{N}$ such that $\mu(n) \lt \frac{1}{p(n)}$ for every $n \gt N$.
```

The definition itself is not that important, just remember that a negligible function approaches 0 and it does so quickly as its input approaches infinity.

```admonish tip title="Definition Breakdown"
Essentially, a function is negligble if it approaches 0 as its input becomes larger and larger. That is, no matter how big a polynomial one can think of, after some input $N$ the function will always be smaller than the reciprocal of the polynomial. 

The reason the function outputs a number between 0 and 1 is that such functions are usually used in the context of probabilities (as is the case here).
```

The reason we want the negligible function to get smaller and smaller as its input gets larger and larger is because we are using the key length $n$ for its input, so we want to say that longer keys are still more secure than shorter ones but at the same time we do not need to use *massive* keys. By today's standards, a reasonable negligible function would be one which is already on the order of $\frac{1}{2^{128}}$ for an input $n = 128$. So, not only does the function need to approach 0, but it also needs to do so fairly quickly.

# Probability
When we perform an experiment such as tossing a fair coin, we obtain a certain result from it called its *outcome*.

```admonish danger title="Definition: Outcome of an Experiment"
The *outcome* of an experiment is all the information about the experiment after it has been carried out.
```

For the experiment of the coin toss, the outcome is simply the coin's face after the toss and will be either *heads* ($H$) or *tails* ($T$). If the coin was tossed three times, then the outcome of this experiment could be $THT$ or $HTT$ or $HHH$, etc. Therefore, different experiments can have multiple possible outcomes and the set of *all* possible outcomes is called the *sample space* for the experiment.

```admonish danger title="Definition: Sample Space"
The *sample space* of an experiment is the set of *all* possible outcomes from the experiment.
```

```admonish example
Consider the experiment of tossing a coin three times. Its sample space is $\{HHH,HHT,HTH,HTT,THH,THT,TTH,TTT\}$, or equivalently $\{000,001,010,011,100,101,110,111\}$ if we encoded "heads" with $0$ and "tails" with $1$. 
```

Each outcome can be associated with a number, called its *probability*, which describes how likely this outcome is. However, not all outcomes in the sample space need to have the same probability. Suppose that our coin was "rigged" (maybe it weighed more on one side) and actually was more inclined to result in heads rather than tails. Then, if the coin was tossed three times, the outcome $HHH$ would clearly be more likely than $TTT$. The way probability is assigned to the outcomes in the sample space is called a *probability function*.

```admonish danger title="Formal Definition: Probability Space"
A *probability space* is a sample space $S$ with a total function $\Pr: S \to [0,1]$ such that

$$\sum_{s \in S} \Pr(s) = 1$$

The function $\Pr$ is called a *probability function* over the sample space $S$.
```

```admonish tip title="Definition Breakdown"
The probability function $\Pr$ assigns to each possible outcome a probability value between 0 and 1. The sum of all the probabilities must be one because *some* outcome is guaranteed to happen. If the probabilities did not sum up to one, then there would be a chance that the experiment resulted in an outcome outside its sample space, which is impossible, since the sample space is the set of *all* possible outcomes.
```


If all outcomes from the experiment are equally likely, then they have the same probability and the probability of every outcome $s$ in the experiment's sample space $S$ is 

$$\Pr(s) = \frac{1}{|S|}$$

When this is the case, the probability function $\Pr$ is called *uniform*.

## Events
An *event* $E$ can be thought of as a subset of the sample space of a given experiment which contains only the outcomes we are interested in. Then we would say that an *event has occurred* if the outcome after performing the experiment is in $E$.

The probability of this event occurring (i.e. getting one of its elements as an outcome), denoted by $\Pr_{s\sim S}[E]$ for the sample space $S$, is the sum of the probabilities of all outcomes in the event.

$$\Pr_{s\sim S}[E] = \sum_{s\in E} \Pr(s)$$

When the sample space is understood from context, this can be simply written as

$$\Pr[E] = \sum_{s\in E} \Pr(s)$$

```admonish example
If we wanted to describe the event that we get "tails" an even number of times from the three coin tosses, then we would do it as $E = \{s: s \text{ has an an even number of "tails"}\} = \{HHH, HTT, THT, TTH\}$. The probability of this event is the sum of the probabilities of its outcomes. We assumed a fair coin, so each outcome in the sample space $S$ has the same probability $P(s) = \frac{1}{|S|}$. Then,

$$\Pr[E] = \sum_{s \in E} \Pr(s) = 4\times \frac{1}{|S|}$$

The total number of outcomes, $|S|$, is eight as we saw earlier, so

$$\Pr[E] = \frac{4}{8} = \frac{1}{2}$$
```

### Logic with Events
For an event $E$, we can describe the event $\overline{E}$ which simply encompasses all outcomes for which $E$ does *not* occur. The probability of $\overline{E}$ is the probability that $E$ does *not* happen and is equal to the following:

$$\Pr[\overline{E}] = 1 - \Pr[E]$$

Given two possible events $A$ and $B$, we can talk about both $A$ *and* $B$ happening or $A$ *or* $B$ (or both) happening. These correspond to the *intersection* and union of the two events, respectively. Therefore,

$$A \land B \equiv A \cap B$$

$$A \lor B \equiv A \cup B$$

## Random Variables
A *random variable* (which is a terrible misnomer, but again, mathematicians...) is a way to assign a number to every outcome in the sample space $S$. Formally, a random variable is a function $X: S \to \mathbb{R}$. 

```admonish example
Consider the experiment of rolling a fair die three times. Each roll has six possible outcomes - $\{1,2,3,4,5,6\}$ - and there are three rolls, so the sample space is $\{1,2,3,4,5,6\}^3$. One possible random variable for this experiment would be the sum $\textit{SUM}: \{1,2,3,4,5,6\}^n \to \mathbb{R}$ of the points from the three rolls ($n = 3$ in this case).
```

In fact, we have already seen another possible random variable which can be defined for every sample space - that's right, probability! Since the probability function $\Pr$ assigns to every outcome in the sample space a number ranging from $0$ to $1$ (which is a subset of the real numbers), this means that it is a random variable.

### Expectation Value
The *expectation value* of a random variable $X$ over a sample space $|S|$, denoted by $\mathbb{E}[X]$ or $\langle X \rangle$, is the average value of the random variable:

$$\mathbb{E}[X] \coloneqq \sum_{x \in S} \frac{X(x)}{|S|}$$

The expectation value is calculated by summing all the values of the random variable for the outcomes in the sample space and then dividing it by the total number of outcomes.

```admonish example
For the previous example where $\textit{SUM}: \{1,2,3,4,5,6\}^n \to \mathbb{R}$ was the random variable which for each outcome was equal to the sum of the three rolls, the expectation value can be calculated as follows:

$$\mathbb{E}[\textit{SUM}] = \sum_{x\in\{1,2,3,4,5,6\}^3} \frac{SUM(x)}{|\{1,2,3,4,5,6\}^3|} = \frac{2268}{216} = 10.5$$

Of course, calculating this by summing up all the numbers for every outcome is tedious, but it can be circumvented using some properties of expectation.
```

There are two properties of the expectation value that one should be aware of.

```admonish abstract title="Linearity"
For every two random variables $X$ and $Y$ over the same sample space $S$, the expectation value of their sum (which is itself a random variable defined as $X(x) + Y(x)$ for every $x\in S$) is equal to sum of the expectation values of $X$ and $Y$.

$$\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$$

Similarly, for every random variable $X$ and constant $k \in \mathbb{R}$, the expectation value of $k$ multiplied by $X$ is equal to $k$ multiplied by the expectation value of $X$.

$$\mathbb{E}[kX] = k\mathbb{E}[X]$$
```

```admonish check collapsible=true title="Proof of Linearity"
For the sum part,

$$\mathbb{E}[X + Y] = \sum_{x\in S} \frac{X(x) + Y(x)}{|S|} = \sum_{x\in S} \frac{X(x)}{|S|} + \sum_{x\in S} \frac{Y(x)}{|S|} = \mathbb{E}[X] + \mathbb{E}[Y]$$

For the multiplication by a constant part,

$$\mathbb{E}[kX] = \sum_{x\in S} \frac{k\times X(x)}{|S|} = k\times \sum_{x\in S} \frac{X(x)}{|S|} = k \mathbb{E}[X]$$
```

```admonish example
Linearity can be used to calculate the expectation of the $\textit{SUM}$ random variable which we defined for the experiment of rolling a dice three times. For each separate roll the sum is just the number of points on the die's face and the sum of three rolls is just the sum of the points from the three rolls which can also be said as "the sum of the three rolls is the sum of the sums of each separate roll". This allows us to use linearity.

If we denoted the number of points from the first, second and third roll with $a,b,c$, respectively, then the final outcome will be written as $abc$ (this is concatenation, not multiplication) and we have, by linearity,

$$\begin{align}\mathbb{E}[\textit{SUM}(abc)] &= \mathbb{E}[\textit{SUM}(a)+\textit{SUM}(b)+\textit{SUM}(c)] \\ &= \mathbb{E}[\textit{SUM}(a)] + \mathbb{E}[\textit{SUM}(b)] + \mathbb{E}[\textit{SUM}(c)] \\ &= \sum_{x\in\{1,2,3,4,5,6\}} \frac{\textit{SUM}(x)}{6} + \sum_{x\in\{1,2,3,4,5,6\}} \frac{\textit{SUM}(x)}{6} + \sum_{x\in\{1,2,3,4,5,6\}} \frac{\textit{SUM}(x)}{6} \\ &= 3 \times \sum_{x\in\{1,2,3,4,5,6\}} \frac{\textit{SUM}(x)}{6} \\ &= 3\times \frac{1+2+3+4+5+6}{6} \\ &= 3\times 3.5 = 10.5\end{align}$$
```

## Distributions
Random variables (which output only real numbers) are a special case of all total surjective functions $f: S \to O$ which assign some value in the finite output set $O$ to every element of $S$. The function is surjective, so $O$ is the set of *all* possible outputs and for every $o \in O$ there must be at least one $s \in S$ for which $f(s) = o$. However, that doesn't stop the function from outputting the same $o$ given two or more different $s_1, s_2,...\in S$. The number of times that each $o \in O$ is obtained when executing $f$ on every $s \in S$ is described by a *probability distribution*.

```admonish danger title="Formal Definition: Probability Distribution"
A *probability distribution* over a finite set $O$ is a total *probability function* $\Pr$ such that

$$\sum_{o \in O} \Pr(o) = 1$$
```

```admonish tip title="Definition Breakdown"
This definition is quite broad and does not even mention the function $f$. This is because a probability distribution is just a way to assign a probability value to every member of a set $O$.

When we say that we "choose a random member from a set $O$" according to some distribution $\mathcal{D}$, we simply mean that the probability of choosing a particular $o \in O$ is equal to $\Pr(o)$.

The requirement that the sum of all the probabilities is equal to 1 is very intuitive - we are choosing from a finite set $O$, so we must get *some* member of it.
```

This is all great, but how do we know what probability $\Pr$ will assign to a given $o \in O$. This is where the function $f$ comes in. We say that a "distribution over a set $O$ is obtained by sampling $s \leftarrow_R S$ and outputting $f(s)$" when the set $O$ is generated by executing $f(s)$ on every $s \in S$ and counting how many $s_1,s_2,... \in S$ produce a specific output $o \in O$ in order to define the probability function $\Pr$. For each $o \in O$ then, the probability function is defined as follows:

$$\Pr(o) = \frac{\textit{number of inputs }s\in S\textit{ for which } f(s) = o}{|S|}$$

```admonish info title="Probability"
In this way, it makes some sense to call this a *probability function* because $\Pr(o)$ tells us how likely it is that $f$ outputs $o$ when choosing an $s \in S$ uniformly at random. 
```

