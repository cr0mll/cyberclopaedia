# Security Definitions

A _**collision**_ is a pair of two inputs $$x \ne x'$$ which produce the same digest when hashed, i.e. $$H(x) = H(x')$$.

When the input space is larger than the digest space (as is usually the case for hash functions), collisions are _guaranteed_ to exist thanks to the [pigeonhole principle](https://en.wikipedia.org/wiki/Pigeonhole\_principle) - if you have 6 holes and 7 pigeons and you want to fit all pigeons into a hole, then at least one hole must contain more than one pigeon. However, collisions are the cause of many headaches and so we had to come up with ways to minimise them.

## (First-) Preimage Resistance

Each output $$y$$ of a hash function $$H$$ can be obtained from multiple possible inputs $$x_1, x_2, ...$$ (if, as usual, the output length is shorter than the input length). Preimage resistance means that given full knowledge of how $$H$$ works and a digest $$y$$, it is very difficult to find _any_ one of the inputs that hash to $$y$$.

{% hint style="danger" %}
<mark style="color:red;">**Definition: Preimage Resistance**</mark>

A hash function $$H$$ has _preimage resistance_ or is _preimage resistant_ if for all efficient adversaries $$\mathcal{A}$$ given a digest $$y \leftarrow_R \mathcal{D}$$ and full knowledge of $$H$$ the probability that $$\mathcal{A}$$ can find an input $$x$$ such that $$y = H(x)$$ is negligible, i.e.

$$\displaystyle\Pr_{y\leftarrow_R \mathcal{D}}[H(\mathcal{A}(y)) = y] \le \textit{negl}()$$
{% endhint %}

Preimage resistant hash functions are also called _one-way functions_ because it is very difficult to reverse the output back into one of the inputs that can be used to obtain it. In fact, it is _impossible_ to find exactly the input $$x$$ that was hashed to the digest $$y$$ - even if we do find some $$x'$$ such that $$H(x') = y$$, we can never be sure if $$x'=x$$, since there are multiple inputs which hash to the same digest.

The notion of preimage resistance is heavily relied on in the secure storage of passwords - when an adversary manages to get their hands on the hash of a password, we want to be sure that they cannot recover the actual password from it.

### Second-Preimage Resistance

There is a stronger notion of preimage resistance which means that given one input $$x$$, its digest $$y = H(x)$$ and full knowledge of the hash function $$H$$, it is very difficult to find one of the other inputs $$x' \ne x$$ which produces the same hash $$y$$.



{% hint style="danger" %}
<mark style="color:red;">**Definition: Second-Preimage Resistance**</mark>

A hash function $$H$$ has _second-preimage resistance_ or is _second-preimage resistant_ if for all efficient adversaries $$\mathcal{A}$$ given an input $$x$$, its digest $$y = H(x)$$ and full knowledge of the internals of $$H$$, the probability that $$\mathcal{A}$$ can find another input $$x' \ne x$$ such that $$H(x') = H(x)$$ is negligible, i.e.

$$\displaystyle\Pr_{x\leftarrow_R\mathcal{M}}[\mathcal{A}(x) \ne x \land H(A(x)) = H(x)] \le \textit{negl}()$$
{% endhint %}

Second-preimage resistance is stronger in the sense that second-preimage resistant hash functions are also first-preimage resistant.

{% hint style="success" %}
<mark style="color:green;">**Theorem: Second-Preimage Resistance -> Preimage Resistance**</mark>

Every hash function that is second-preimage resistant is also first-preimage resistant.
{% endhint %}

If an adversary who is given $$x$$ and $$y = H(x)$$ cannot find an input $$x' \ne x$$ such that $$H(x') = y$$, then they certainly cannot do it when given only $$y = H(x)$$.

## Collision Resistance

The definition of collision resistance is particularly strong and states that if a hash function is collision resistant, then it should be very difficult to find _any collisions_ in it.

{% hint style="danger" %}
<mark style="color:red;">**Definition: Collision Resistance**</mark>

A hash function $$H$$ provides _**collision resistance**_ or is _**collision resistant**_ if for all efficient collision finders $$\mathcal{F}$$, the probability that $$\mathcal{F}$$ finds two inputs $$x_1 \ne x_2$$ such that $$H(x_1) \ne H(x_2)$$ is negligible, i.e.

$$\displaystyle\Pr_{x_1, x_2 \leftarrow \mathcal{F}()}[H(x_1) = H(x_2)] \le \textit{negl}()$$
{% endhint %}

{% hint style="info" %}
<mark style="color:blue;">**Definition Breakdown**</mark>

An algorithm $$\mathcal{F}$$ which tries to find a collision for a given hash function is called a collision finder. The hash function $$H$$ is considered to be collision resistant if there is no collision finder that can find a collision in it with significant probability.
{% endhint %}

It is not difficult to see that a collision resistant hash function is also second-preimage resistant and by extension first-preimage resistant. After all, if an adversary can find a colliding pair without any external help, such as an input $x$ and its digest $y$, then it can certainly find a colliding pair _with_ such help.

{% hint style="success" %}
<mark style="color:green;">T</mark><mark style="color:green;">**heorem: Collision Resistance → Second-Preimage Resistance**</mark>

Every collision resistant hash function is also second-preimage resistant.
{% endhint %}

{% hint style="success" %}
<mark style="color:green;">**Theorem: Collision Resistance → First-Preimage Resistance**</mark>

Every collision resistant hash function is also first-preimage resistant, since it is second-preimage resistant.
{% endhint %}
