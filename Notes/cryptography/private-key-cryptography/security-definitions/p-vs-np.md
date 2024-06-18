# P vs NP

_Every_ private-key encryption scheme (yes, even perfectly secret ones) can be broken in the sense that you can find whether a ciphertext $$c$$ corresponds to $$m_1$$ or $$m_2$$ simply by trying all possible keys - an approach called a _brute force attack_.

```python
def BruteForce(ciphertext, plaintext1, plaintext2):
	for key in [0..2^n - 1]:
		if Enc(key, plaintext1) == ciphertext:
			return plaintext1
		if Enc(key, plaintext2) == ciphertext:
			return plaintext2
```

The reason we are not really worried about this attack, which works for _every_ cipher, is that it runs in exponential time - the `for` loop will execute $$2^n$$ number of times in the worst case scenario and on average it will run $$2^{\frac{n+1}{2}}$$ number of times in order to crack a given ciphertext. This means that as the key gets longer and longer, the number of times that the `for` loop needs to execute on average to crack a given ciphertext gets larger and it does so very fast. In essence, this is a strategy which always works but is very slow. A key length of just 256 bits means that the algorithm will need to run $$2^{128.5}$$ number of steps to crack a given ciphertext on average which is _practically impossible_ for even the most powerful supercomputers.

<details>

<summary><mark style="color:purple;"><strong>Example</strong></mark></summary>

According to Wikipedia, the most powerful supercomputer currently in existence is [Frontier](https://en.wikipedia.org/wiki/Frontier\_\(supercomputer\)). It has $$606,208$$ AMD Epyc cores running at 2 GHz each and $$8,335,360$$ AMD Radeon Instinct cores which we will also assume to be running at 2 GHz each. This gives us a total of $$,8,941,568$$ cores all executing $$2\times 10^9$$ cycles per second which amounts to

$$8\,941\,568 \times 2\times 10^9 = 1.79\times 10^{16} \text{ cycles/s}$$

If we assume that every cycle corresponds to a single key tried (a pretty generous assumption, mind you), then on average this computer would need $$\frac{2^{128.5}}{1.79\times 10^{16}} = 2.69 \times 10^{22}$$ seconds to crack a ciphertext encrypted with a 256-bit key. This amounts to $$8.53 \times 10^{14}$$ years which is approximately $$62,263$$ times the current age of the Universe. Yes, a _very long time_, indeed.

</details>

Therefore, we know that the problem of cracking a ciphertext encrypted with a given $$n$$-bit key is solvable (i.e. there is an algorithm to do it) in exponential time - it takes $$O(2^n)$$ number of steps to execute. This makes it an NP problem.

However, it can be shown that if _any_ NP problem can be shown to have an algorithm which executes much faster (i.e. in polynomial time) and is thus a P problem, then _all_ NP problems can be solved much faster. This is called the $$P=NP$$ hypothesis and remains unproven and with little evidence to speak for it so far. What it entails, however, is that cryptography is basically useless if it turns out to be true, for it means that the brute force attack can also be sped up drastically - instead of $$2^n$$ steps to execute, it will be able to run in $$n^{10}$$ or $$n^2$$ or maybe even $$n$$ steps, all of which are much smaller than $$2^n$$.

{% hint style="info" %}
If the brute force attack could be optimised to run in $$n^{10}$$ steps, then it would take only $$1.21 \times 10^{24}$$ steps to crack a 256-bit key. This can be done on the Frontier supercomputer in a little over 2 years which is _not_ infeasible and can be momentous for military purposes, for example.
{% endhint %}
