# Introduction
The definition given for a *valid* private-key encryption scheme specifies *what* functions can be used for encryption and decryption, but says nothing about *how secure* those functions should be. For example, the trivial encryption function $\textit{Enc}_k(m) = m$ which simply encrypts a plaintext to itself is a valid private-key encryption function but is far from secure.

Defining what makes a private-key encryption scheme *secure* is a bit tricky. 

# Threat Models
When defining security, we need to know what we are defining it against. Mainly this boils down to the information available to an adversary and there are four major attack scenarios:
- **Ciphertext-Only Attack (COA)** - the adversary has access only to one or more ciphertexts and attempts to glean information about their underlying plaintexts.
- **Known-Plaintext Attack (KPA)** - the adversary has access to one or more plaintext-ciphertext pairs as well as an additional ciphertext which were generated with some key and attempts to deduce information about the plaintext underlying the additional ciphertext.
- **Chosen-Plaintext Attack (CPA)** - this the KPA attack model but the adversary can free *choose* the plaintext-ciphertext pairs, i.e. it has access to something which can compute the ciphertext of a given plaintext, but not vice-versa, without revealing the key. 
- **Chosen-Ciphertext Attack (CCA)** - the adversary can choose ciphertexts obtain information about (or simply) the underlying plaintext for these ciphertexts when decrypted with some key and attempts to determine information about the plaintext of some other ciphertext (whose decryption cannot be obtained directly by the adversary) which was generated using the same key.

```admonish warning
If a cipher is secure against *one* of these threat models, this does *not* mean that it is secure against *all* of them.
```