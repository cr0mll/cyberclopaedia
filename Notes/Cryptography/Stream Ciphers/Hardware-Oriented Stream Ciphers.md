# Introduction
Hardware-oriented stream ciphers are designed to be run on *dedicated hardware*. They typically work on the bit-level, since hardware can be custom-tailored to be more efficient with these operations. Almost all hardware stream ciphers are built upon a concept called *feedback shift registers (FSRs).*

# Feedback Shift Registers
An FSR is comprised of a bit array, called a *register*, which is equipped with an update feedback function, denoted as $f$, which takes a bit array and produces a single bit based on it. Each update alters the register and produces a single output bit. Given a current register state, $R_i$, the subsequent state will be this:

$$ R_{i+1} = (R_i << 1) | f(R_i)$$

The current state $R_i$ is left-shifted by a single position. The bit leaving the register is returned as the output for this update cycle and the bit in the end of the register is filled with $f(R_i)$.  Here, `|` denotes the OR operation.

For example, suppose you had a feedback function, $f$ which simply XOR-ed all the bits of the register. Given an initial state, $0101$, you would have $f(0101) = 0 \bigoplus 1 \bigoplus 0 \bigoplus 1 = 0$. The new state would thus be $(0101 << 1)|0 = 1010$.

Given a feedback function $f$ and an initial state $R_0$, we define the *period* of the FSR to be the number of updates that the FSR can go through until the new state repeats with one of the previous states, thus forming a cycle. Note, that the period of the FSR will be the same if we substituted $R_0$ for any other state which is produced during its cycle and any single state may only belong to a single cycle. 

With the above function, $f$, and state, $0101$, the period would be 6.

Naturally, an FSR with a larger period will produce a more unpredictable output.

# Linear Feedback Shift Registers (LFSR)
Linear Feedback Shift Registers are FSRs which are equipped with a linear feedback function, namely a procedure which XORs together some of the bits of the current state. The bits that get XOR-ed together are defined by a set of boolean *feedback coefficients*. It is important that the feedback coefficients are *not* allowed to mutate throughout any update, since they define the feedback function. The number of bits in the bit array of the register is called its *degree*.

![](Resources/Images/LFSR.png)

For a register consisting of bits $s_{n-1},...,s_0$ and feedback coefficients $c_{n-1},...,c_0$, the state of the LFSR is updated by shifting the register to the right and replacing the left-most bit with the output of the feedback function. Namely, if the register state at time $t$ is described by $s_{n-1}^{(t)},...,{}_{t}s_0^{(t)}$, the state after an update (also called a *clock tick*) would be given by:

$$s_i^{(t+1)} \coloneqq s_{i+1}^{(t)}, \text{where } i = 0,...,n-2$$
$$s_{n-1}^{(t+1)} \coloneqq \bigoplus_{i=0}^{n-1} c_i s_i^{(t)}$$

For each clock tick, the LFSR outputs the value of the right-most bit, $s_0$. Thus, if the initial state of the LFSR is $s_{n-1}^{(0)},...,s_0^{(t)}$, then the first $n$ bits of the output stream will be the sequence $s_0^{(0)},...,s_{n-1}^{(0)}$, with the next output bit being $s_{n-1}^{(1)} = \bigoplus_{i=0}^{n-1} c_i s_i^{(0)}$.