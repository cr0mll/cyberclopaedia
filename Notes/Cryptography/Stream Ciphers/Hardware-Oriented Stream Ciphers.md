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

## Linear Feedback Shift Registers (LFSR)
Linear Feedback Shift Registers are FSRs which are equipped with a linear feedback function, namely a procedure which XORs together some of the bits of the current state. The bits that get XOR-ed together are defined by a set of boolean *feedback coefficients*. It is important that the feedback coefficients are *not* allowed to mutate throughout any update, since they define the feedback function. The number of bits in the bit array of the register is called its *degree*.

![](Resources/Images/LFSR.png)

For a register consisting of bits $s_{n-1},...,s_0$ and feedback coefficients $c_{n-1},...,c_0$, the state of the LFSR is updated by shifting the register to the right and replacing the left-most bit with the output of the feedback function. Namely, if the register state at time $t$ is described by $s_{n-1}^{(t)},...,{}_{t}s_0^{(t)}$, the state after an update (also called a *clock tick*) would be given by:

$$s_i^{(t+1)} \colon= s_{i+1}^{(t)}, \text{where } i = 0,...,n-2$$
$$s_{n-1}^{(t+1)} \colon= \bigoplus_{i=0}^{n-1} c_i s_i^{(t)}$$

For each clock tick, the LFSR outputs the value of the right-most bit, $s_0$. Thus, if the initial state of the LFSR is $s_{n-1}^{(0)},...,s_0^{(t)}$, then the first $n$ bits of the output stream will be the sequence $s_0^{(0)},...,s_{n-1}^{(0)}$, with the next output bit being $s_{n-1}^{(1)} = \bigoplus_{i=0}^{n-1} c_i s_i^{(0)}$.

The maximal period of an LFSR is $2^n-1$, where $n$ is the degree of the LFSR, for the all-zeros state can never be mutated via a XOR operation. It is paramount that the correct feedback coefficients are chosen in order to ensure a maximal period. Luckily, there is a procedure for accomplishing just that. Starting from 1 for the left-most bit moving up to $n$ for the right-most bit, we construct a polynomial of the form $p(x) = 1 + x + x^2 + x^3 + ... + x^n$, where the term $x^i$ is only included if the $i$th bit has a feedback coefficient equal to 1 (it is included in the XOR operation). Now, the period is maximal if and only if this polynomial is *primitive*. A polynomial is primitive when it is irreducible (factorisation is impossible) and also satisfies additional mathematical criteria, which I unfortunately do not comprehend myself, but you can read more about them [here](https://en.wikipedia.org/wiki/Primitive_polynomial_(field_theory)).

LFSRs are inherently insecure due to their linearity. Given known feedback coefficients, the first $n$ output bits will reveal the initial state and from then on it is possible to determine the entirety of all future bits. Even with unknown feedback coefficients, an attacker needs at most $2n$ output bits to determine both the feedback coefficients and the initial state. If we denote the first $n$ output bits as $y_0,...,y_{n-1}$ and the next $n$ bits as $y_n,...,y_{2n-1}$, we can construct the following system of linear equations:

$$\begin{align}
y_n &= c_{n-1} y_{n-1} \bigoplus \cdots \bigoplus c_0 y_0 \newline
\vdots \newline 
y_{2n-1} &= c_{n-1} y_{2n-2} \bigoplus \cdots \bigoplus c_0 y_{n-1} 
\end{align}$$

It is possible to show that for a maximal period LFSR the equations in the system are linearly independent ($\mod 2$) and can be solved through basic linear algebra.

## Introducing Nonlinearity
LFSRs can be strengthen by introducing nonlinearity in the encryption process by different means. This means that it is not only XOR operations that are used, but also logical ANDs and ORs. For example, it is possible to make the feedback loop nonlinear by setting the value of the leftmost bit at each clock tick to be a nonlinear function of the bits in the previous state. If the register's state at time $t$ is $s_{n-1}^{(t)},...,s_0^{(t)}$, the state at $t+1$ would be

$$s_i^{(t+1)} \colon= s_{i+1}^{(t)}, \text{where } i = 0,...,n-2$$
$$s_{n-1}^{(t+1)} \colon= g(s_{n-1}^{(t)},...,s_0^{(t)})$$

As before, the rightmost bit, $s_0$ is outputted at each clock tick. In order for the FSR to be secure, the feedback function, $g$ should be balanced in the sense that $\text{Pr}[g( s_{n-1},...,s_0 ) = 1] \approx \frac{1}{2}$. This is called an NFSR.

![](Resources/Images/NFSR.png)

### Filtered FSRs
In the above example, the FSR itself is nonlinear, since the way that the leftmost is altered at each clock tick is determined by a nonlinear function. However, it is also possible to keep the FSR linear and instead pass its output to a filter function, $g$. Instead of outputting the rightmost bit, $s_0$, the entire register is passed to the filter function and the output of the register is determined by the output of $g$.

![](Resources/Images/Filtered_FSR.png)