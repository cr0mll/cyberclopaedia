# Merkle Trees

## Introduction

Consider the case where you upload a file $x$ to a server and later want to retrieve it. How can you be sure that the file $x'$ is the same as the file you originally uploaded? Perhaps someone hacked the server in the meantime and tampered with the file - how can you detect this?

Well, a (gormless) solution would be to simply store a copy of $x$ on your local machine and then check if the file $x'$ returned from the server matches your local copy. For one, this verification might take a while to finish depending on the size of the file, and, secondly, having to maintain a local copy defeats the entire purpose of using the server for storage.

Another thing you could do is to [hash](../hash-functions/) the file with a [collision resistant](../hash-functions/security-definitions.md) hash function and store only its digest $h = H(x)$. Later on, when retrieving the file from the server, you can simply check if the hash $H(x')$ of the server's file matches the hash $h$ which you stored on your system. This is indeed an excellent solution for single files, but what about the case when multiple files are involved?

## Merkle Trees

Merkle trees provide a way to solve this very problem. More generally, whenever one has $q$ different components that comprise some object $o$, a Merkle tree can be used to verify both the integrity of the entire object $o$ as well as that of its individual components.

Suppose you have $q$ different files $x\_1, ..., x\_q$ where $q$ is a power of 2 for simplicity (otherwise you can just use additional dummy files until $q$ becomes a power of 2). The first step is to hash each of the files $x\_1, ..., x\_q$ to obtain their corresponding hashes $h\_1, ..., h\_q$. Next, divide the hashes into pairs according to their adjacency - $(h\_1, h\_2), (h\_3,h\_4), ..., (h\_{q-1}, h\_q)$. Concatenate the elements of each pair and hash the results. This process is repeated until there is only a single hash $h\_{\text{root\}}$ left which is what you store on your machine.

![](<../../Cryptography/Integrity Verification/Resources/Images/Merkle Tree.svg>)

Later, when you are retrieving a specific file from the remote host, the server will send you the file $x\_i'$ together with the hashes necessary to calculate $h\_{\text{root\}}'$. For example, if you are requesting $x\_3$, then the server will return a file $x\_3'$ together with the hashes $h\_4'$, $h\_{1-2}'$, and $h\_{5-8}'$. You are going to hash $x\_3'$ to obtain $h\_3' = H(x\_3')$ and then use this with $h\_4'$ to compute $h\_{3-4}' = H(h\_3'||h\_4')$. This can now be used to calculate $h\_{1-4}' = H(h\_{1-2}'||h\_{3-4}')$ and subsequently $h\_{\text{root\}}' = H(h\_{1-4}'||h\_{5-8}')$. If this new root hash $h\_{\text{root\}}'$, which is based on the server's information, matches the root hash $h\_{\text{root\}}$, which you computed when uploading the files, then you know that the file has not been tampered with!

```admonish
In fact, you know that *no* file has been tampered with on the server's end because all the files are taken into account when the server sends you the hashes. If one of these hashes is not correct, then neither will be the root hash.
```
