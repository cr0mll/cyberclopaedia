# Introduction
The Advanced Encryption Standard (AES) is an encryption standard which has been ubiquitously adopted due to its security and has been standardised by NIST. It is comprised of three symmetric block ciphers which all take blocks of size 128 bits and output blocks of the same size. AES has three versions depending on the length of the key it can take. These are AES-128, AES-192, and AES-256, for 128-, 192-, and 256-bit keys, respectively. 

The key length also determines the number of rounds that each 128-bit block goes through:

|Key Length|Number of Rounds|
|:----------:|:--------------------:|
|128|10|
|192|12|
|256|14|

# Initialisation
AES round operations are performed on a 2D array (matrix) called the *State*. The State has dimensions 4x4 and contains bytes at each cell. Each element in the State can be referred to as $s_{r,c}$, or $s\left[r,c\right]$, where $r$ and $c$ denote respectively the row and column of the element and begin from 0. 

At the beginning of the Cipher and Inverse Cipher, the State is populated in the following way:
$$s\left[r,c\right] = in\left[r+4c\right]$$
At the end of the Cipher and Inverse Cipher, the State is mapped back again into the output bytes in the following manner:
$$out\left[r+4c\right] = s\left[r,c\right]$$

$$
\begin{bmatrix}
in_0 & in_1 & in_2 & in_3 & in_4 & in_5 & in_6 & in_7 & in_8 & in_9 & in_{10} & in_{11} & in_{12} & in_{13} & in_{14} & in_{15}
\end{bmatrix}
$$

$$\big\Downarrow $$

$$
\begin{bmatrix}
s_{0,0} & s_{0,1} & s_{0,2} & s_{0,3} \\
s_{1,0} & s_{1,1} & s_{1,2} & s_{1,3} \\
s_{2,0} & s_{2,1} & s_{2,2} & s_{2,3} \\
s_{3,0} & s_{3,1} & s_{3,2} & s_{3,3} \\
\end{bmatrix}
$$

$$\big\Downarrow $$

$$
\begin{bmatrix}
out_0 & out_1 & out_2 & out_3 & out_4 & out_5 & out_6 & out_7 & out_8 & out_9 & out_{10} & out_{11} & out_{12} & out_{13} & out_{14} & out_{15}
\end{bmatrix}
$$

# Key Expansion
Every round uses a different round key, $K_i$, in order to encrypt the block. These keys are generated from the initial key, $K_0$, which was chosen.

