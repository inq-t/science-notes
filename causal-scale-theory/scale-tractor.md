# Scale-Tractor Transport

Scale-tractor calculus packages the metric selected by a scale section into conformally covariant data. In four dimensions, the trace-free Einstein equation becomes an exact equation for scale-tractor transport, while the trace and residual vacuum channels remain independent. CST uses this as an interface to gravity, not as a derivation of gravity from information geometry.

Let $\sigma$ be a weight-one scale and $D_A$ the Thomas operator. In four dimensions define the scale tractor

$$
I_A:=\frac14D_A\sigma.
$$

In a metric splitting its slots are

$$
I_A
\simeq
\left(
\sigma,
\nabla_a\sigma,
-\frac14(\Delta\sigma+J_{\mathrm{Sch}}\sigma)
\right),
\qquad
J_{\mathrm{Sch}}:=\frac R6.
$$

The notation $J_{\mathrm{Sch}}$ prevents confusion with either geometric reflection or Tomita conjugation.

In these four-dimensional conventions the Schouten tensor is

$$
P_{ab}
=\frac12\left(R_{ab}-\frac16R g_{ab}\right),
\qquad
J_{\mathrm{Sch}}=P^a{}_a=\frac R6.
$$

In a choice of metric $g\in[g]$, the trace-free tensor

$$
\mathcal E_{ab}
:=\bigl(\nabla_a\nabla_b\sigma+P_{ab}\sigma\bigr)_0
$$

is the component that measures failure of $I_A$ to be parallel. Here $P_{ab}$ is the Schouten tensor and the subscript $0$ denotes trace-free part.

On the open set where $\sigma\ne0$,

$$
\boxed{
\nabla_a^T I_B=0
\quad\Longleftrightarrow\quad
\mathcal E_{ab}=0
\quad\Longleftrightarrow\quad
g_\sigma\ \text{is Einstein}.}
$$

This is the standard almost-Einstein equivalence in the declared conventions. With sources, trace-free stress is precisely the local obstruction to that parallel transport.

With the conventional normalization used in the source masters, the trace-free Einstein equation is equivalently

$$
\boxed{
\mathcal E_{ab}
=\frac{4\pi G}{c^4}\,\sigma T^\circ_{ab}}
$$

where

$$
T^\circ_{ab}:=T_{ab}-\frac14Tg_{ab}.
$$

This is an **[EXACT — REFORMULATION]** of the trace-free field equation once the conformal and tractor conventions are fixed. It is not an independent field equation and does not determine $G$.

## The scalar channel

The tractor norm carries the trace information. In the physical metric $g_\sigma=\sigma^{-2}g$, the standard norm--curvature identity is

$$
\boxed{I^2=-\frac{R[g_\sigma]}{12}.}
$$

Combining it with the trace of the Einstein equation gives, in the same conventions,

$$
I^2
=\frac{2\pi G}{3c^4}T-\frac{\Lambda_g}{3}.
$$

The split is therefore

$$
\text{trace-free transport}
\quad\oplus\quad
\text{scalar norm constraint}.
$$

A common central or vacuum-like shift is invisible to $T^\circ_{ab}$ but not thereby physically absent. It reappears in the scalar/global channel. [[vacuum-residual-sector]] keeps this distinction explicit.

## Why this matters for causal scale

The causal-order theorem supplies $[g]$; the scale tractor records how a chosen $\sigma$ is embedded in that conformal geometry. CST's proposed state-space law would have to determine or constrain this scale data while remaining compatible with the local equation above.

This produces a precise interface question:

$$
\text{horizontal state geometry}
\stackrel{?}{\longrightarrow}
\text{admissible }\sigma
\stackrel{\text{tractor identity}}{\longrightarrow}
\text{metric response}.
$$

Only the second arrow is presently controlled. The first is represented at homogeneous level by [[causal-scale-theory/free-energy-source|the constitutive source law]], [[horizontal-temperature|the horizontal-temperature identification]], and [[causal-scale-theory/hawking-friedmann|the horizon conversion]], not by a general covariant theorem.

At the response maximum, an additional exact conditional statement is available: [[causal-scale-theory/trace-free-crossing|the response becomes trace-free silent]] because $w_X=-1$. This does not make the total scale tractor parallel in the presence of ordinary matter or radiation.

## What is not established

- Local trace-free blindness is not a solution to the cosmological-constant problem.
- The tractor equation does not derive the binary channel, the BKM metric, or either unit law.
- A homogeneous density history is not yet a covariant stress tensor $T^X_{ab}$.
- Importing Einstein dynamics as the local metric fiber is compatible with CST, but stronger claims of emergence would require reconstruction. See [[compatible-with-existing-physics/local-physics-interface|the local-physics interface]].
