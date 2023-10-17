# Introduction
Consider the case where you upload a file $x$ to a server and later want to retrieve it. How can you be sure that the file $x'$ is the same as the file you originally uploaded? Perhaps someone hacked the server in the meantime and tampered with the file - how can you detect this? 

Well, a (gormless) solution would be to simply store a copy of $x$ on your local machine and then check if the file $x'$ returned from the server matches your local copy. For one, this verification might take a while to finish depending on the size of the file, and, secondly, having to maintain a local copy defeats the entire purpose of using the server for storage.

Another thing you could do is to [hash](../Hash%20Functions/index.md) the file with a [collision resistant](../Hash%20Functions/Security%20Definitions.md) hash function and store only its digest $h = H(x)$. Later on, when retrieving the file from the server, you can simply check if the hash $H(x')$ of the server's file matches the hash $h$ which you stored on your system. This is indeed an excellent solution for single files, but what about the case when multiple files are involved?

# Merkle Trees
Merkle trees provide a way to solve this very problem. More generally, whenever one has $q$ different components that comprise some object $o$, a Merkle tree can be used to verify both the integrity of the entire object $o$ as well as that of its individual components. 

Suppose you have $q$ different files $x_1, ..., x_q$ where $q$ is a power of 2 for simplicity (otherwise you can just use additional dummy files until $q$ becomes a power of 2). The first step is to hash each of the files $x_1, ..., x_q$ to obtain their corresponding hashes $h_1, ..., h_q$. Next, divide the hashes into pairs according to their adjacency - $(h_1, h_2), (h_3,h_4), ..., (h_{q-1}, h_q)$. Concatenate the elements of each pair and hash the results. This process is repeated until there is only a single hash $h_{\text{root}}$ left which is what you store on your machine.

![](Resources/Images/Merkle%20Tree.svg)

Later, when you are retrieving a specific file from the remote host, the server will send you the file $x_i'$ together with the hashes necessary to calculate $h_{\text{root}}'$. For example, if you are requesting $x_3$, then the server will return a file $x_3'$ together with the hashes $h_4'$, $h_{1-2}'$, and $h_{5-8}'$. You are going to hash $x_3'$ to obtain $h_3' = H(x_3')$ and then use this with $h_4'$ to compute $h_{3-4}' = H(h_3'||h_4')$. This can now be used to calculate $h_{1-4}' = H(h_{1-2}'||h_{3-4}')$ and subsequently $h_{\text{root}}' = H(h_{1-4}'||h_{5-8}')$. If this new root hash $h_{\text{root}}'$, which is based on the server's information, matches the root hash $h_{\text{root}}$, which you computed when uploading the files, then you know that the file has not been tampered with!

```admonish note
In fact, you know that *no* file has been tampered with on the server's end because all the files are taken into account when the server sends you the hashes. If one of these hashes is not correct, then neither will be the root hash.
```