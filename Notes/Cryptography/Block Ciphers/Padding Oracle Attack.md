# Introduction
A padding oracle attack which abuses padding validation information in order to decrypt an arbitrary message. In order to achieve, it requires a *padding oracle*. A padding oracle is any system which, given a ciphertext, behaves differently depending on whether the decrypted plaintext has valid padding or not. For the sake of simplicity, you can think of it as a sending an arbitrary ciphertext to a server and it returning "Success" when the corresponding plaintext has valid padding, and spitting out "Failure" otherwise. Note that the ciphertexts you query the oracle with need not have meaningful plaintexts behind them and you will not even be generating them by encryption, but rather crafting them in a custom manner in order to exploit the information from the oracle.

# How It Works
Let's remind ourselves of how CBC decryption works by taking a simplified look at the last two blocks:

![](Resources/Images/Padding_Oracle_Original_Encryption.png)

The last ciphertext $C_2$ is decrypted with the key $k$ to an intermediate block $I_2$. This intermediate state is then XOR-ed with the penultimate ciphertext block, $C_1$, in order to retrieve the plaintext block $P_2$. Note, all block here are made from bytes.

Now, let's imagine a second scenario, where $C_2$ is kept the same, be we purposefully alter the last byte of $C_1$. After this modification, we send the ciphertext to the oracle. Our goal here is to obtain a "success" from it, meaning that it has managed to decrypt the ciphertext we sent it to a plaintext with a valid padding. Since we are only altering the last byte for now, we want to generate a ciphertext which when decrypted will result in a plaintext, whose last byte is `0x01`.

![](Resources/Images/Padding_Oracle_C1_Bruteforce.png)

Since, we didn't change $C_2$, the intermediate $x_1$ also remains the same. Additionally, $y_1$ is a single byte so it can only take a total of 256 values. This makes it rather easy to bruteforce what $y_1$ should be, simply by sending queries at max 256 queries to the oracle. Once the oracle returns a "Success", we have found the right value for $y_1$. We can now simply XOR $y_1$ with `0x01` to obtain the value of $x_1$, $x_1 = y_1 \bigoplus \text{0x01}$. 

Since $x_1$ is the same in both the original and the attack scenario, we can now XOR $x_1$ with the original last byte of $C_1$ in order to obtain the last byte of the original plaintext! This procedure can be further repeated to obtain the penultimate byte, then the antepenultimate byte and so forth! All that is needed is to find the two bytes at the end of $C_1$ that would result in a plaintext ending in `0x0202`.

![](Resources/Images/Padding_Oracle_C12_Bruteforce.png)

We already know $x_1$, so we can obtain the new $y_1 = x_1 \bigoplus \text{0x02}$. We now only need to bruteforce $y_2$ with the same technique described above. Once the oracle returns a "Success", we have found the correct value for $y_2$ and can obtain $x_2 = y_2 \bigoplus \text{0x02}$. Going back to the original scenario, we compute the penultimate byte of the plaintext by XOR-ing the penultimate byte of the unaltered $C_1$ with the value of $x_2$. Rinse and repeat and you have decrypted the entire plaintext! Note, you will have to reset the procedure from `0x01` with each new block.

# Reverse Oracle Padding
Apart from allowing you to *decrypt* a ciphertext, an oracle padding vulnerability can allow you to *encrypt* (almost) any plaintext. This could be useful for example when you need to encrypt a plaintext cookie to a ciphertext in order to use it, but you don't have the key.

First of all you will need to choose the plaintext you want to encrypt, $P_n$ and pad it appropriately. Then generate a random block of data. This will be the last ciphertext block $C_n$. Next, we set $C_{n-1}$ to be a block of 0s and perform a padding oracle attack the usual way, until we obtain the value of $C_{n-1}$ for which $C_n$ decrypts to a full block of padding (in the case of block size 8 this would be `0x0808080808080808`).

We now XOR these together to obtain $I_n = \text{0x0808080808080808} \bigoplus C_{n-1}$. Afterwards, XOR the desired plaintext $P_n$ with the intermediate state $I_n$ in order to obtain a new value for $C_{n-1}$ which will force $C_n$ to be decrypted to the appropriate plaintext. Repeat this process with the rest of the ciphertext blocks, but now use the ultimately obtained $C_{n-1}$ instead of the randomly generated $C_n$, and then the next ultimately obtained $C_{n-i}$, and... ta-da, you have the ciphertext of your desired plaintext. Unforunately, unless you have control of the IV, the last block will always decrypt to garbage.

# Padding Oracle Attacks with `padbuster`



