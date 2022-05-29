# The Shift Cipher
One of the oldest known cipher's is known as Caesar's cipher. Julius Caesar encrypted his messages by shifting every letter of the alphabet three spaces forward and looping back when the end of the alphabet is reached. Consequently, `A` would be mapped to `D` and `Z` would be mapped to `C`.

An immediate problem with this cipher is the lack of a key - the shift amount is always the same. A natural extension of the cipher wouold then be to let the shift amount vary, turning it into a key whose possible values are the numbers between 0 and 25. Therefore, the key space is  $K \equiv \{ 0, ..., 25 \}$.

An encryption algorithm $Enc_k$ would take a plaintext $m$, shift its letters forwards by $k$ positions and spit out a ciphertext $c$. In contrast, a decryption algorithm $Dec_k$ would take the ciphertext $c$ and shift its letters *backwards* by $k$ places to retrieve the original plaintext. If we map the alphabet to the set $\set{0,...,25}$ ($a = 0, b = 1$, etc.), a more mathematical description is obtained. Encryption of any message $m = m_1 \cdot\cdot\cdot m_l$ ($m_i \in \set {0,...,25}$) using the key $k$ is given by
 
 $$Enc_k (m_1 \cdot\cdot\cdot m_l) = c_1 \cdot\cdot\cdot c_l, \hspace{1cm} where \hspace{1mm} c_i = [(m_i + k) \mod 26]$$

The notation $[a \mod N]$ is the remained of $a$ upon division by $N$ where $0\leq[a \mod N] < N$ and $\cdot\cdot\cdot$ denotes concatenation and not multiplication. Decryption of a cyphertext $c = c_1 \cdot\cdot\cdot c_l$ using a key $k$ would then be given by 

 $$Dec_k (c_1 \cdot\cdot\cdot c_l) = m_1 \cdot\cdot\cdot m_l, \hspace{1cm} where \hspace{1mm} m_i = [(c_i - k) \mod 26]$$

It is only natural to now ask, is this cipher secure? And the simple answer is no. There are only 26 possible keys and so the key-space is not sufficiently big. You can even go through all 26 possible keys with a given ciphertext by hand and check which resulting plaintext makes sense. Most likely, there will be only one and so you have recovered the original message.

Another method to crack this cipher is by using frequency analysis. Since the shift cipher is a one-to-one mapping on a letter-by-letter basis, the frequency distribution of letters is preserved. For example, the most common letter in English is the letter "e". If we analyse the ciphertext and discover that the most common letter there is "g", then we know that most likely the letter "g" is the letter "e" encrypted with the given key. From this we can calculate the key to be 2 (however, the plaintext, and therefore the ciphertext, may actually deviate from this distribution, so it is not with 100% certainty that the key is 2). We can also perform the same procedure with the rest of the letters in the ciphertext and retrieve the original plaintext. This process can also be automated with some math.

![](Resources/Images/English_Letter_Frequency_Table.png)

Let's once again map the alphabet with the intergers 0 through 25 and also this time let $p_i$ ($0 \leq p_i \leq 1$) denote the frequency of the $i$th letter. Using the above table, we can calculate that

$$ \sum_{i=0}^{25} p_i^2 \approx 0.065$$

Now, let $q_i$ denote the frequency of the $i$th letter in the ciphertext - this is just equal to the number of occurences of the $i$th letter divided by the length of the ciphertext. If the key is $k$, then $p_i$ should be approximately equal to $q_{i+k}$, since the $i$th letter gets mapped to the $(i+k)$th letter (technically, these should be $i+k \mod 26$, but that's too cumbersome to write here). Therefore, if we compute

$$ I_j \overset{\mathrm{def}}{=} \sum_{i=0}^{25} p_i \cdot q_{i+j}$$

for every value of $j \in \{0,...,25\}$, then $I_k$ should be approximately equal to 0.065, where $k$ is the actual key. For all $j \neq k$, $I_j$ would be different from 0.065. This ultimately leads to a way to recover the original key that is fairly easy to automate.

