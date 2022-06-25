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