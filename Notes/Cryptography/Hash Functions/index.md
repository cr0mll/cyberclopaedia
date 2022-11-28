# Introduction
Hash functions take long inputs and produce outputs of a fixed bit-length, usually 256 or 512 bits. Their use is ubiquitous and is typically focused around verifying the integrity of data. The output of a hash function is called the *hash* (value) or *digest*.

![](Resources/Images/Hash%20Function.svg)

# Security Notions
Security notions for hash functions are different from those pertaining to ciphers. Their security lies in the fact that they should be unpredictable. Id est, it should be impossible to make predictions about the hash of a message when you have another message and its hash. For example, take the following three hashes:

```
ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d
2e7d2c03a9507ae265ecf5b5356885a53393a2029d241394997265a1a25aefc6
```

These are the SHA-256 hash values of the letters "a", "b", and "c", respectively. While these messages only differ by a single bit when represented as ASCII, their hashes are like chalk and cheese.

Hash functions are also sometimes called *one-way functions* because it should be impossible to find a message, $M$, which was hashed to get the digest $D$, when $D$ is given. This notion is called *preimage resistance*, where a *preimage* of a hash is simply a message which hashes to that particular digest. It should be easy to compute the hash of a message, but it should be impossible to compute the message from the hash.

Preimage resistance is further subdivided into *first-* and *second-preimage resistance*. The former refers to what we already described. Second-preimage resistance entails that given a message, $M_1$ and its digest $D$, it should be impossible to find another message, $M_2$, which hashes to the same $D$, by using solely $M_1$ and $D$.

The other security notion is *collision resistance* and it describes the situation where we have found two or more messages, $M_1, M_2, ...$, which hash to the same digest, $D$. Now, since the input space of a hash functions is much larger than its fixed-length output space, collisions are *inevitable*. What collision resistance entails, however, is that it should be extremely difficult to find such messages which hash to the same hash value.