# Introduction
The One-Time Pad (OTP) or also known as the Vernam Cipher is the most famous (and perhaps the only remotely useful) [perfectly secret](index.md#perfect-secrecy) cipher. It uses a plaintext and a key and produces a ciphertext of all which have the same bit-length. The mainstay of this cipher is the [XOR operation](../Mathematical%20Prerequisites.md#xor-operation). Encryption simply XORs the key with the plaintext and decryption XORs the ciphertext with the key to retrieve the plaintext.

$$\textit{Enc}(k, m) = k \oplus m$$
$$\textit{Dec}(k, c) = k \oplus c$$

```admonish check collapsible=true title="Proof: Perfect Secrecy of OTP"
We claim that for every $m \in \mathcal{M}$, the distribution $D_m$ obtained by sampling the keyspace $k \leftarrow_R \mathcal{K}$ and outputting $\textit{Enc}_k(m)$ is the uniform distribution over $\mathcal{C}$ and therefore, the distributions $D_m$ and $D_{m'}$ are identical for every $m,m' \in \mathcal{M}$.

Observe that every ciphertext $c \in \mathcal{C}$ is output by $\textit{Enc}_k(m)$ if and only if $c = m \oplus k$. This in turn is true if and only if $k = m \oplus c$. The key $k$ is chosen uniformly at random from $\mathcal{K}$, so the probability that $k$ happens to be $m \oplus c$ is exactly $\frac{1}{|\mathcal{K}|}$. Moreover, the key, plaintext and ciphertext have the same length, so $|\mathcal{K}|=|\mathcal{M}|=|\mathcal{C}|$ which means that this probability is equal to $\frac{1}{|\mathcal{M}|}$, thus making the cipher perfectly secret.
```

# Attacks on the One-Time Pad
The One-Time Pad is indeed perfectly secret but only if the same key is never reused. If an adversary had access to two or more ciphertexts, then they could obtain information about the XOR of the two underlying plaintexts by XOR-ing the ciphertexts together. 

$$c_1 = m_1 \oplus k$$

$$c_2 = m_2 \oplus k$$

$$c_1 \oplus c_2 = (m_1 \oplus k) \oplus (m_2 \oplus k) = (m_1 \oplus m_2) \oplus (k \oplus k) = m_1 \oplus m_2$$