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
- binary strings $\{0,1}^*$ - strings which only contain 0s and 1s
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
- binary strings - $\{0,1\}^*
```

# Functions
