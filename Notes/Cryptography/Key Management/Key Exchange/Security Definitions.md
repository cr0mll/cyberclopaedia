# Introduction
There is one essential security property for key exchange protocols - an adversary should be unable to obtain the same final key as the two legitimate parties. Nevertheless, we still need to define our threat models, i.e. the capabilities of the adversary and how powerful they are.

```admonish danger title="Definition: Security in the Presence of an Eavesdropper"
The adversary $\textit{Eve}$ can observe all communication between the legitimate parties Alice and Bob.
```

The aforementioned security definition assumes a *passive* adversary, i.e. an adversary who can observe the communication between the 
