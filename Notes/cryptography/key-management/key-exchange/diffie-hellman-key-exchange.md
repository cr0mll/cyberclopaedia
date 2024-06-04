# Diffie-Hellman Key Exchange

## Introduction

The Diffie-Hellman key exchange protocol allows two parties, Alice and Bob, to agree on a secret key without having exchanged any secret information beforehand! The method is based in [cyclic groups](../../public-key-cryptography/mathematical-prerequisites.md#groups), so read up on that in the mathematical prerequisites.

## Diffie-Hellman Key Exchange

The protocol itself is based on the group $$\mathbb{Z}_p^*$$, where $$p$$ is some _huge_ prime number. The prime numbers that can be used in the Diffie-Hellman (DH) key exchange are standardised - they are public knowledge and can be found in various RFCs on the Internet. More specifically, the prime $$p$$ must be a _safe prime_, i.e. a prime such that $$p = 2q + 1$$, where $$q$$ is also prime.

<details>

<summary>Example: Diffie-Hellman Prime</summary>

One such prime $$p$$ can be found in [RFC 3526](https://www.rfc-editor.org/rfc/rfc3526#page-5) and is 4096 bits long.

</details>

Notice that since $$p = 2q + 1$$, the prime $$q$$ divides $$p - 1$$ and so the group $$\mathbb{Z}_p^*$$ has an element $$g$$ of order $$q$$ and the powers of $$g$$ generate the group $$\langle g \rangle \coloneqq {0,1,\cdots,q-1}$$_._ It turns out that this group $$\langle g \rangle$$ is a subgroup of $$\mathbb{Z}_p^*$$. We are now ready to outline the DH key exchange.

The primes $$p,q$$ as well as the generator $$g$$ are public knowledge and are standardised in various RFCs.

Alice picks a random power between 0 and $$q-1$$, i.e. a uniform $$a \leftarrow_R \mathbb{Z}_q$$ and computes $$A \coloneqq g^a$$. Similarly, Bob picks a uniform $$b \leftarrow_R \mathbb{Z}_q$$ and computes $$B \coloneqq g^b$$. Alice and Bob then exchange the values $$A$$ and $$B$$ which they computed - Alice obtains $$B$$ from Bob and Bob obtains $$A$$ from Alice.

Alice now computes $$B^a = (g^b)^a = g^{ab}$$ and Bob computes $$A^b = (g^a)^b = g^{ab}$$ - the two parties have arrived at the same key $$k \coloneqq g^{ab}$$! Interestingly enough, any eavesdropping adversary cannot arrive at the same value by just observing the communication channel, since they do not know the secret values $$a$$ and $$b$$ which Alice and Bob picked separately for themselves.

|            |                  Alice                  |                   Bob                   |                   Eve                   |
| :--------: | :-------------------------------------: | :-------------------------------------: | :-------------------------------------: |
|    $$p$$   | <mark style="color:green;">known</mark> | <mark style="color:green;">known</mark> | <mark style="color:green;">known</mark> |
|    $$q$$   | <mark style="color:green;">known</mark> | <mark style="color:green;">known</mark> | <mark style="color:green;">known</mark> |
|    $$g$$   | <mark style="color:green;">known</mark> | <mark style="color:green;">known</mark> | <mark style="color:green;">known</mark> |
|    $$a$$   | <mark style="color:green;">known</mark> | <mark style="color:red;">unknown</mark> | <mark style="color:red;">unknown</mark> |
|    $$b$$   | <mark style="color:red;">unknown</mark> | <mark style="color:green;">known</mark> | <mark style="color:red;">unknown</mark> |
|   $$g^a$$  | <mark style="color:green;">known</mark> | <mark style="color:green;">known</mark> | <mark style="color:green;">known</mark> |
|   $$g^b$$  | <mark style="color:green;">known</mark> | <mark style="color:green;">known</mark> | <mark style="color:green;">known</mark> |
| $$g^{ab}$$ | <mark style="color:green;">known</mark> | <mark style="color:green;">known</mark> | <mark style="color:red;">unknown</mark> |

## The Diffie-Hellman Problems

The security of the Diffie-Hellman protocol is defined according to certain mathematical problems.

In trying to break the Diffie-Hellman key exchange, the adversary Eve is in a way trying to solve the _discrete logarithm problem_. The function $$\text{Dlog}_g$$ denotes the discrete logarithm function with base $$g$$ and is the function that returns the power $$x \in \mathbb{Z}_q$$ which you need to raise $$g$$ to in order to obtain $$g^x$$, i.e. Eve is trying to compute $$\text{Dlog}_g(g^x)$$. The logarithm is called _discrete_ because it only returns integer values due to the fact that we are working with groups.

{% hint style="danger" %}
<mark style="color:red;">**Definition: The Discrete Logarithm Problem**</mark>

The adversary $$\textit{Eve}$$ is given the generator $$g$$ as well as the order $$q$$ of the generated group $$\langle g \rangle$$ and is provided with the group element $$g^x$$ for some uniform, unknown, $$x \leftarrow_R \mathbb{Z}_q$$. Her goal is to find the value of $$x$$.

We say that the discrete logarithm problem is _hard relative to_ $$\langle g \rangle$$ if no matter what Eve does, the probability that she can find $$x$$ is negligible, i.e.

$$\displaystyle\Pr_{x\leftarrow_R \mathbb{Z}_q}[\textit{Eve}(g, q, g^x) = x] \le \textit{negl}(\cdot)$$
{% endhint %}

It should be obvious that the computational difficulty of the discrete logarithm largely depends on the group itself and so not every group yields a secure Diffie-Hellman key exchange.

There are two additional problems which are similar to the discrete logarithm problem and are known to be related but not equivalent to the each other.

{% hint style="danger" %}
<mark style="color:red;">**Definition: The Computational Diffie-Hellman (CDH) Problem**</mark>

The adversary Eve is given the generator $$g$$ as well as the order $$q$$ of the generated group $$\langle g \rangle$$ and is provided with two group elements $$g^a$$ and $$g^b$$ for some uniform, unknown, $$a,b \leftarrow_R \mathbb{Z}_q$$. Her goal is to then find the value of $$g^{ab}$$.

We say that the computational diffie-hellman problem is _hard relative to_ $$\langle g \rangle$$ if, no matter what Eve does, the probability that she can find $$g^{ab}$$ is negligible, i.e.

$$\displaystyle\Pr_{a,b \leftarrow_R \mathbb{Z}_q}[\textit{Eve}(g, q, g^a, g^b) = g^{ab}] \le \textit{negl}(\cdot)$$
{% endhint %}

The CDH problem is essentially an exact description of the Diffie-Hellman scenario. Eve can observe the communication between Alice and Bob and is thus able to obtain the values $$g^a$$ and $$g^b$$. However, Alice and Bob ultimately end up using the value $$g^{ab}$$ as a key and so Eve has to find a way to compute it using only $$g^a$$ and $$g^b$$.

The second problem is related to the CDH problem but the two problems are not known to be equivalent.

{% hint style="danger" %}
<mark style="color:red;">**Definition: The Decisional Diffie-Hellman (DDH) Problem**</mark>

The adversary Eve knows the cyclic group $$\mathbb{G}$$, one of its generators $$g$$ and its order $$q$$. She is given two group elements $$g^{\alpha}, g^{\beta}$$ which are generated by $$g$$ for some uniform, unknown to Eve, powers $$\alpha, \beta \leftarrow_R \mathbb{Z}_q$$. Finally, Eve is either given a third such element $$g^{\gamma}$$ generated by some uniform unknown $$\gamma \leftarrow_R \mathbb{Z}_q$$ or she is given the element $$g^{\alpha\beta}$$. Eve's goal is to then determine if she has $$g^{\alpha\beta}$$ or $$g^{\gamma}$$.

We say that the DDH problem is _hard relative to_ $$\mathbb{G}$$ if no matter what Eve does, the probability that she achieves her goal is negligible, i.e.

$$\displaystyle\left|\Pr[\textit{Eve}(\mathbb{G}, g, q, g^{\alpha}, g^{\beta}, g^{\gamma}) = 1] - \Pr[\textit{Eve}(\mathbb{G}, g, q, g^{\alpha}, g^{\beta}, g^{\alpha\beta}) = 1] \right| \le \textit{negl}(\cdot)$$
{% endhint %}

If the CDH problem is easy relative to some group, then so is the DDH problem.