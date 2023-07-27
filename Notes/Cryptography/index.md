# Introduction
Cryptography is the study and application of techniques for secure communication and it is concerned with the confidentiality of data. Suppose that Alice wants to send Bob a secret message, but that there is also a malicious person Eve who also wants to read the message. The problem of how Alice can send the message to Bob without Eve finding out what its contents are lies at the core of all cryptography.

The solution is for Alice to *encrypt* the message, i.e. alter it, in such a way that only Bob can *decrypt* it to restore its original contents.

```admonish info title="Mathematical Prerequisites"
Cryptography is heavily based on rigorous mathematics and any decent understanding of its ideas and algorithms necessitates understanding of the underlying math as well. Fortunately (or unfortunately for the mathematicians), most of this math is superfluous and does not serve much of a purpose other than dressing up definitions in fancy notation.

Every concept will first be presented and explained intuitively with as little math as possible. Then, a veritable formal definition will be given, with all the gory mathematical details. Finally, this formal definition will be broken down piece by piece and every term in it will be explained. Further reading will also be provided for those interested in a particular subject.

That said, *some* mathematical knowledge is required, but everything needed is found in the [Mathematical Prerequisites](Mathematical%20Prerequisites.md). You may read it all at once before starting with cryptography or you can refer to it as new concepts get introduced.
```

# Historical Background
Cryptography has an old, although not particularly remarkable, history. Evidence of its use dates back to Antiquity. The first ciphers used were *transposition ciphers* where the letters of a message are rearranged, creating an anagram. The Spartans employed a device called a [Scytale](https://en.wikipedia.org/wiki/Scytale) to encrypt and decrypt messages during military campaigns. It was a simple mechanism that consisted of a leather strip wrapped around a wooden log. 

![](https://upload.wikimedia.org/wikipedia/commons/5/51/Skytale.png)

The sender would write their message on the strip while it was wrapped and when they unfurled it, it would look like gibberish. 

Transposition ciphers were unreliable because there are only so many anagrams for a given word. Additionally, decrypting the message was fairly difficult even for the intended recipient because they would have to figure out what the anagram was for - they had to do doing the same thing that an adversary would if they were trying to crack the message.

### Caesar's Cipher
This problem gave birth to *substitution ciphers*, the most famous of which is the [Ceasar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) used by Julius Caesar during to communicate with his military commanders. Julius Caesar encrypted his messages by shifting every letter of the alphabet three spaces forward and looping back when the end of the alphabet was reached. For example, `A` would be mapped to `D` and `Z` would be mapped to `C`. Of course, the number 3 was just a personal preference - this cipher has 25 variants for the 25 possible shift values. 

The issue with this was that there are only 25 possible shifts. One could brute-force their way through them to recover the original message. Certainly tedious, but not impossible for someone in ancient Rome to do.

### Substitution Ciphers
Ceasar's shift cipher was a specific form of the more general mono-alphabetic substitution cipher which replaced all occurrences of a particular letter in the message with another letter, which would be specified for example by a table or a key. And for a few centuries these ciphers did pretty well - until in the 9th century AD an ingenious Islamic philosopher known as [Al-Kindi](https://en.wikipedia.org/wiki/Al-Kindi) figured out a way to break them by dint of *frequency analysis*. Since each letter in the message was always assigned to the same letter in the encrypted, one note down how many times each letter occurred in the encrypted message. Then, they could match those frequencies with the overall letter frequencies in the language the message to reveal its contents. For example, the most common letter in English is "e", followed by "t", so it is not unreasonable to assume that if the most common letters in the encrypted message were "c" and "f" then they would correspond to "e" and "t". 

```admonish info
Of course, this technique could not be used unconditionally because depending on the context, some letters might deviate from the statistics. Some guesswork would be necessary, but this was nothing a determined adversary could not do. 
```

During the Middle Ages, Europe was not particularly interested in cryptography. However, this all changed in the Renaissance, mainly due to political reasons. By the end of the 15th century, every court had a cipher office and every ambassador had a cipher secretary. As the Islamic code-breaking techniques became wide-spread on the continent, cryptographers saw the need for new ways to encrypt their messages. The first was the introduction of the so-called *nulls* into the encrypted message, which are simply symbols which have no actual meaning. Other ways to thwart cryptanalysts was to misspell words or use code words which had a hidden meaning known only to the sender and recipient. None of these techniques, however, were enough to stop a tenacious cryptanalyst, as is evident by the case of Mary the Queen of Scots.

She was an heir to the throne of England and in 1587 she conspired to assassinate her cousin, queen Elisabeth I. She communicated with Sir Anthony Babington using a substitution cipher in her letters. Elisabeth's space, however, intercepted those letters and broke the cipher using frequency analysis. Mary was consequently executed, guilty of treason. It became manifest that a brand new encryption technique was required. 

Little did people suspect that such a cipher had already been conceived a year earlier, in 1586, by [Blaise de Vigenère](https://en.wikipedia.org/wiki/Blaise_de_Vigen%C3%A8re) who constructed the *tabula recta*:

![](https://upload.wikimedia.org/wikipedia/commons/9/9a/Vigen%C3%A8re_square_shading.svg)

The Vigenère cipher relies on a key which is usually a short word that is overlaid onto the message. Each letter in the message corresponds to a row in the tabula recta and the letter chosen from it to be its encryption is determined by the key letter that is overlaid onto it.

~~~admonish example
Consider the message `MESSAGE` and the key `KEY`. Overlaying the key onto the message produces the following:

```
KEYKEYK
MESSAGE
```

To encrypt the message look up each of its letters in the tabula recta - the row is the letter itself and the column is the key letter it is matched to. So, `MESSAGE` would become `WIQCEEO`. The power of the Vigenère cipher is that it destroys the patterns on which frequency analysis relies - the `S` character was once encrypted to `Q` and once to `C`. Moreover, the two `E`s in the resulting encrypted message correspond to different letters - `A` and `G`. 
~~~

```admonish tip
Another way to specify the Vigenère cipher (which is equivalent to the tabula recta) is to think of it as a collection of shift ciphers. Every letter of th message is encrypted by shifting it an amount equal to the place in the alphabet of the key letter that is overlaid onto it.
```

For nearly 300 years the Vigenère cipher was considered unbreakable and even got the moniker "le chiffre indéchiffrable" - the undecipherable cipher. Nevertheless, in 1863 [Friedrich Kasiski](https://en.wikipedia.org/wiki/Friedrich_Kasiski) published a book in which he described a way to break the cipher. 

### The Enigma
Perhaps the most famous example of a device used to perform encryption is the [Enigma](https://en.wikipedia.org/wiki/Enigma_machine) machine. The key it used was not a word but rather the configuration of rotors and wires within the actual machine. Some Germans considered it to be unbreakable even *after* WW2 was over, even though a joint effort between the Polish and the Brits had already proved otherwise. For example, one fatal flaw of the Enigma was that it would never encrypt a letter to itself. 

```admonish info title="Mavis Batey"
Interestingly, in March 1941 [Mavis Batey](https://en.wikipedia.org/wiki/Mavis_Batey), who was a British cryptanalyst, exploited this flaw by noticing that an intercepted message had no `L`s in it. The chances of the original message containing no `L`s were very low, so she concluded that the original message consisted entirely of `L`s! Perhaps someone was testing out the machine by typing in only `L`s. 
```

___

#### Further Reading
- [Breaking the Vigenère cipher](Breaking%20Classical%20Cryptrography.md#the-vigenère-cipher)