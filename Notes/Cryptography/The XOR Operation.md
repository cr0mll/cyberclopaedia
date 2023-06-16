# Introduction
A large portion of cryptography is based on the eXclusive-OR (XOR) operation. It is a bitwise operation which returns 0 if the input bits are the same and returns 1 otherwise. Its definition can be summarised via the following truth table:

|Input 1|Input 2|Output|
|:---:|:----:|:---:|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0|

The XOR operation is denoted by a plus within a circle - $\oplus$.

Numbers made up of multiple bits are XOR-ed on a bit-per-bit basis. So $0101 \oplus 1110 = 1011$. Non-binary data needs to be converted to binary before it can be operated on by XOR.

# Properties
The XOR operation has four major properties which are used extensively throughout the cryptographic field:

|Property|Formula|
|:----:|:----:|
|Commutativity|$A \oplus B = B \oplus A$|
|Associativity|$(A \oplus B) \oplus C = A \oplus (B \oplus C)$|
|Identity|$A \oplus 0 = A$|
|Involution|$A \oplus B = C \implies \begin{cases}A = C \oplus B \\ B = C \oplus A\end{cases} \implies A \oplus A  = 0$|

The XOR operation is commutative - the result is the same if you change the order of the operands. Additionally, associativity means that for a given chain of XOR operations, the order in which we do them is irrelevant. Furthermore, there exists an identity elements, $0$, which when XOR-ed with a value will leave it unchanged.

Involution is perhaps the most essential property that XOR exhibits and it is a fancy word for "self-inverse" - the inverse operation of XOR is itself. This means that when given the result of a XOR operation and one of the operands, the second operand can be recovered by XOR-ing the result with the given input. Moreover, this implies that anything XOR-ed with itself will result in 0. Here is a simple proof:

$$A \oplus B = C \implies \begin{cases}A = C \oplus B \\ B = C \oplus A\end{cases} \implies A = C \oplus (C \oplus A) \implies A = (C \oplus C) \oplus A$$

Now the existence of an identity element tells us that $A \oplus 0 = A$ and so $C \oplus C$ must be 0.