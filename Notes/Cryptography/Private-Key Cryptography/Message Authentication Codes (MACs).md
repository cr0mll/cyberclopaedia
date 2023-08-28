# Introduction
Cryptography facilitates the secure communication between different parties. However, sometimes the meaning of "security" changes. It is often the case that we are not so much concerned with the contents of the message being exposed to an adversary than we are concerned with whether the party sending the message really are who they say and whether or not the message was modified by an adversary somewhere along the way.

```admonish example
Suppose that a bank receives a request to transfer 10,000€ from Alice's account to Eve's. The bank has to consider two things:

1. Is the request authentic? I.e., was it really Alice who issued the request?
2. Is the request unaltered? I.e., did the request get from Alice's computer to the bank's server without being modified by a an adversary?

It maybe the case that Eve is pretending to be Alice and it is she who sent the request. Or perhaps Alice really did want to transfer money to someone, say Bob, but Eve intercepted the request and changed the recipient (and maybe even the transfer amount).
```

Essentially, we are more interested in protecting the message's *integrity* rather its *security*.

# Message Authentication Codes
Message authentication codes provide a way to do just that. They allow Alice to prove that she really did send the request and they also allow the bank to verify that the request originally sent by Alice was received by the bank unmodified. MACs achieve this by using *tags*. Whenever Alice sends a request, she also generates a tag using a secret key that only she and the bank know. The message itself is also used in the creation of the tag which allows the bank to then use the message and tag it receives together with the secret key in order to verify that the message was sent by the correct party and was not modified along the way.

![](Resources/Images/MACs/MAC%20Mechanism.svg)

The mechanism behind MACs is pretty clever and solves both of the bank's conundrums. If Eve wants to pretend to be Alice, then Eve needs Alice's secret key to sign messages as her. Since the bank also uses Alice's key, if Eve uses any other key, the tag she sends to the bank will be deemed invalid and the request will be discarded. Similarly, if Eve intercepts a message signed by Alice and modifies it, she still needs to have Alice's key in order to sign the modified message in her name.

```admonish danger title="Definition: Message Authentication Code"
A *message authentication code (MAC)* is a pair of efficient algorithms $\textit{Sign}(key: \textit{\textbf{str}}, message: \textit{\textbf{str}}) \to \textit{\textbf{str}}$ and $\textit{Verify}(key: \textit{\textbf{str}}, message: \textit{\textbf{str}}, tag: \textit{\textbf{str}}) \to \textit{\textbf{bit}}$ where $\textit{Sign}$ takes as input a key $k$ and a message $m$ and produces a tag $\tau \in \{0,1\}^*$, while $\textit{Verify}$ takes a key, a message and a tag and produces a single bit:

$$\textit{Verify}(k, m, \tau) \coloneqq 
\begin{cases}1, \text{ if the tag } \tau \text{ was produced using the message } m \text{ and key } k \\ 0, \text{ otherwise}\end{cases}$$
```

```admonish tip title="Definition Breakdown"
The $\textit{Sign}$ algorithm is described exactly as above - it uses the message and the secret key in order to generate a tag which can be used to authenticate the message. The $\textit{Verify}$ algorithm takes uses the secret key and a message to check if the tag was generated using that specific key and that specific message. If $\textit{Verify}$ outputs 1, then the message is accepted. Otherwise, the message is discarded.
```

For all practical purposes, the tag is much shorter than the message - we do not want to overwhelm the network channel that is used by sending unnecessarily large tags. However, this does mean that multiple messages will produce the same tag when signed with a given key $k$.

```admonish note
Just how the two communicating parties exchange a particular secret key without the adversary getting their hands on it usually relies on public-key cryptography. 
```

## Security
It is now time to describe what it means for a MAC system to be secure. As it turns out, the most pertinent threat model for MACs is a [chosen-message attack](index.md). The adversary has access to some messages and their corresponding tags and they are even free to choose the messages to be signed. The adversary's goal is to then find an entirely new *valid* message-tag pair without any knowledge of the secret key.

```admonish danger title="Definition: CMA-Security for Message Authentication Codes"
A MAC system $(\textit{Sign}, \textit{Verify})$ is *CMA-secure* if for any set of message-tag pairs $(m_1, \tau_1), (m_2,\tau_2), ..., (m_q, \tau_q)$ that were signed with the same key $k \leftarrow_R \mathcal{K}$ and for every efficient adversary $\textit{Eve}$ which has access to those message-tag pairs, the probability that $\textit{Eve}$ can produce a new valid message-tag pair $(m, \tau)$, called an *existential forgery*, is negligble, i.e.

$$\Pr_{k \leftarrow_R \mathcal{K}}[\textit{Verify}(k, m, \tau) = 1] \le \epsilon$$

for some negligible $\epsilon$.
```

```admonish tip title="Definition Breakdown"
The adversary $\textit{Eve}$ is free to choose the messages $m_1,m_2,...,m_q$ and is then presented with their tags $t_1, t_2, ..., t_q$ which are signed with the secret key $k$, i.e. $\tau_i \leftarrow \textit{Sign}(k, m_i)$. The attacker then produces a new candidate pair $(m, \tau)$, called an *existential forgery*, with the goal that this pair fools $\textit{Verify}$ when checked with the secret key $k$. The MAC system is secure if the existential forgery can fool $\textit{Verify}$ with only an extremely small probability.
```

The good thing about this notion of security is that it captures the case where the adversary is trying to find a second valid tag $\tau'$ for the same message $m$ with an already known tag $\tau$. However, this definition provides no protection against *replay attacks*.

### Replay Attacks
A replay attack describes the scenario where the adversary eavesdropping on the communication channel has captured a bunch of valid message-tag pairs and later sends, or *replays*, them again. Since the pairs were generated by an authentic party and are merely being resent again by a malicious actor, they will pass verification at the receiving end with no problem.

```admonish example
Image that Alice really does want to transfer 100€ to Bob's account, so she sends an authentic request with a valid tag to the bank. However, if Bob copies this request on its way to the bank, Bob can later pretend to be Alice by sending the exact same message with the same valid tag and the bank will think this is a legitimate request and will transfer another 100€ to Bob's account.
```

Message authentication codes on their own provide no protection mechanisms against such attacks which is why additional measures must be implemented.

# Implementing MACs
