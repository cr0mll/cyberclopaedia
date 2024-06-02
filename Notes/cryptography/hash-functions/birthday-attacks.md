# Birthday Attacks

## Introduction

As with normal ciphers, there is a trivial brute-force attack which can find a collision in any hash function $$H$$. If the hashes produced by the $$H$$ are all of length $$l_{\text{out}}$$, then to find a collision we can just evaluate $$H$$ on $$2^{l_{\text{out}}}+1$$ different inputs. Since the number of possible hashes is only $$2^{l_{\text{out}}}$$, then at least two inputs must have produced the same hash and our job is done.

Usually, we are not particularly worried about this attack because it takes $$O(2^{l_{\text{out}}})$$ steps to execute. However, it turns out that there is a much more efficient attack which can find a collision against any hash function.

### The Birthday Paradox

To illustrate the attack we are going to answer the following question: given $$q$$ people in a room, what is the probability that two of them share a birthday? One should see how this is equivalent to asking what is the likelihood that from $$q$$ messages $$m_1, m_2, ..., m_q$$ two produce a collision in the hash function $$H$$.

We assume that each birthday date is equally likely and that we are only working with the $$B = 365$$ possible birthdays in a non-leap year. The probability that two people share the same birthday is the same as the negation of the probability that _no_ people share a birthday, i.e. the probability of a collision is the negation of the probability that there is _no_ collision amongst the $$q$$ messages $$m_1, ..., m_q$$.

$$\Pr[\text{Coll}] = 1 - \Pr[\text{NoColl}_q]$$

Imagine the people entering the room one by one (or equivalently, the messages being generated independently one after the other). The probability that there is no collision in the birthdays of the $$q$$ people is the probability that there is no collision in the birthdays of the first $$q-1$$ people _and_ that the $$q$$-th person's birthday also does not collide with the previous birthdays, i.e.

$$\Pr[\text{NoColl}_q] = \Pr[\text{NoColl}_{q-1}]\times \frac{B-q+1}{B}$$

This is true because if there were no collisions in the first $$q-1$$ people, then there must be $$q-1$$ unique birthdays and so the probability that the $$q-1$$-th person's birthday is also unique is $$\frac{B-(q-1)}{B} = \frac{B-q+1}{B}$$. This logic can be continued until we reach the first person. Therefore,

$$\Pr[\text{NoColl}_q] = 1\times \frac{B-1}{B} \times \frac{B-2}{B}\times\cdots \times\frac{B-q+2}{B}\times \frac{B-q+1}{B}$$

The 1 at the beginning represents the probability that the first person's birthday does _not_ collide with someone's else when entering the room, which is 100%, since there are no other people in the room until the first one enters. This probability can be rewritten as the following product:

$$\Pr[\text{NoColl}_q] = \prod_{i=1}^{q-1}\left(1-\frac{i}{B}\right)$$

Therefore, the probability that a collision _does_ occur can be written as

$$\Pr[\text{Coll}] = 1 - \prod_{i=1}^{q-1}\left(1-\frac{i}{B}\right)$$

We are now going to use a well-known inequality (we are going to take it for granted because proving it is out of scope), namely that $$1-x \le e^{-x}$$. Plugging in $$\frac{i}{B}$$ for $$x$$, we get that

$$1 - \prod_{i=1}^{q-1}\left(1-\frac{i}{B}\right) \ge 1 - \prod_{i=1}^{q-1}e^{-\frac{i}{B}}$$

What is nice about exponential functions with the same base is that when multiplying them, the exponents simply add, yielding

$$1 - \prod_{i=1}^{q-1}e^{-\frac{i}{B}} = 1 - e^{-\frac{1}{B}\sum_{i=1}^{q-1}i} = 1 - e^{-\frac{1}{B}\frac{q(q-1)}{2}}$$

The function $$\frac{q(q-1)}{2}$$ is always greater than $$\frac{q^2}{2}$$ for positive integers $$q$$ and so we have

$$1 - e^{-\frac{1}{B}\frac{q(q-1)}{2}} \ge 1 - e^{-\frac{q^2}{2B}}$$

Recall that the left-hand side is smaller than the probability of a collision. Therefore,

$$\Pr[\text{Coll}] \ge 1 - e^{-\frac{q^2}{2B}}$$

While we did not obtain an exact equation for the value of $$\Pr[\text{Coll}]$$, we did obtain a lower bound for it!

{% hint style="info" %}
<mark style="color:blue;">**Corollary**</mark>

Given $$q$$ elements which are uniformly and independently chosen from a set of $$B$$ possible elements, the probability that two elements are the same is at least $$1 - e^{-\frac{q^2}{B}}$$.
{% endhint %}

Now let's put the theorem to work. How many people do we need in the room in order for there to be 50% chance that two of them share a birthday? Well, plug in $$B = 365$$ and set

$$1 - e^{-\frac{q^2}{2\cdot365}} = \frac{1}{2}$$

Solving this equation yields $$q = 23$$. We need only 23 people for there to be a 50% chance of two of them sharing a birthday!

## Naive Birthday Attack

If we have a hash function $H$ with outputs of length $l\_{\text{out\}}$, then in order to have a 50% chance of a collision, we need $q \approx 1.2\times2^{\frac{1}{2}l\_{\text{out\}}}$ different messages (this can be obtained from the Birthday theorem bound by setting $B = 2^{l\_{\text{out\}}}$).

The naive birthday attack does precisely this. First, it chooses $2^{\frac{1}{2}l\_{\text{out\}}}$ different messages $m\_1, m\_2, ..., m\_q$. It then computes their hashes $h\_1, h\_2, ..., h\_q$. Finally, it looks for a collision amongst these hashes $h\_i = h\_j$. With probability approximately $\frac{1}{2}$ it is going to find such a collision. If it does not, it simply starts over. On average, this attack is going to need just 2 iterations to get a colliding pair and its running time is $O(2^{l\_{\text{out\}}/2})$. Compare that to the brute-force approach whose running time was $O(2^{l\_{\text{out\}}})$.

This variation is called _naive_ because it has a huge space complexity, namely $O(2^{l\_{\text{out\}}/2})$, since the algorithm will have to store all the computed hashes while checking them for collisions.

```admonish
Since the birthday attack is universal and works for any hash function, it is used instead of the simple brute force attack as the gold standard when creating security proofs.
```

{% hint style="info" %}
<mark style="color:blue;">**Universality of the Birthday Attack**</mark>

Since the birthday attack is universal and works for any hash function, it is used instead of the simple brute force attack as the gold standard when creating security proofs.
{% endhint %}

### Small-Space Birthday Attack

There is an improved version of the birthday attack which has approximately the same probability success and running time but only takes a _constant_ amount of memory. This attack uses [Floyd's cycle finding algorithm](https://en.wikipedia.org/wiki/Cycle\_detection).

Begin by choosing a random initial message $$x_0$$ and set $$x \coloneqq x_0, x' \coloneqq x_0$$. At the $$i$$-th iteration compare the values $$x_i = H(x_{i-1})$$ and $$x_i' = H(H(x_{i-1}'))$$. If $$x_i = x_i'$$, then we know that there must have been a collision somewhere along the way - it might simply happen that $$x_{i-1} \ne H(x_{i-1}')$$, in which case we would have immediately found the collision pair $$x_{i-1}, H(x_{i-1}')$$. However, it could very well be the case that $$x_{i-1} = H(x_{i-1}')$$ and so the actual collision, i.e. the two different inputs that produced the same hash, happened earlier. Since we did not store all of the hashes we burnt through, we will need to iterate over them again to find precisely which ones collide.

Store the index $$i$$ for which we found that $$x_i = x_i'$$ and reset $$x = x_0, x' = x_0$$ to the initial value $$x_0$$. This time we will iterate until $$i$$. At each step $$j$$, we check if $$H(x_j) = H(x_j')$$ and if it is, we have our collision - simply return $$x_j$$ and $$x_j'$$. Otherwise, we set $$x_j = H(x_j)$$ and $$x_j' =H(x_j')$$.

```rust
fn SmallSpaceBirthdayAttack()
{
	let x_0 = random_binary_string();
	let x = x_0;
	let x' = x_0;
	let i = 0;
	
	while(true)
	{
		x = H(x);
		x' = H(H(x'));
		
		if (x = x')
		{
			break;
		}
		else
		{
			++i;
		}
	}
	
	let x = x_0;
	let x' = x_0;
	
	for(let j = 0; j < i; ++j)
	{
		if (H(x) = H(x'))
		{
			return (x, x');
		}
		else
		{
			x = H(x);
			x' = H(x');
		}
	}
}
```

This attack uses much less memory than the naive method because it only needs to store the initial value $$x_0$$ as well as the two values $$x$$ and $$x'$$ which are being checked at each iteration. As before, we have a $$\approx 50%$$ chance of finding a collision within the first $$2^{l_{\text{out}}/2}$$ hashes we check.
