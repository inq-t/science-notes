# Scale-Tractor Transport

Scale-tractor calculus packages a chosen conformal scale and its first two derivatives into a conformally covariant object. In four dimensions, parallel transport of the scale tractor is equivalent to the selected metric being Einstein; after Einstein gravity is separately assumed, trace-free stress appears as the local obstruction while the trace and cosmological channels remain in a scalar norm equation.

Let \((M,[g])\) be a four-dimensional conformal manifold of the kind separated from its metric calibration in [[conformal-scale-geometry/causal-order-and-metric-scale|causal order and metric scale]]. Let \(\sigma\in\Gamma(\mathcal E[1])\), and let \(D_A\) be the Thomas \(D\)-operator. Define the scale tractor

$$
I_A:=\frac14D_A\sigma.
$$

In a metric splitting determined by \(g\in[g]\),

$$
I_A
\simeq
\left(
\sigma,
\nabla_a\sigma,
-\frac14(\Delta\sigma+J_{\mathrm{Sch}}\sigma)
\right),
$$

where

$$
P_{ab}
=\frac12\left(
R_{ab}-\frac16Rg_{ab}
\right),
\qquad
J_{\mathrm{Sch}}
:=P^a{}_a
=\frac R6.
$$

The label \(J_{\mathrm{Sch}}\) distinguishes the Schouten trace from reflection operators and modular conjugations used elsewhere.

Define the trace-free scale tensor

$$
\mathcal E_{ab}
:=
\bigl(
\nabla_a\nabla_b\sigma
+P_{ab}\sigma
\bigr)_0.
$$

On the open set where \(\sigma\neq0\),

$$
\boxed{
\nabla_a^T I_B=0
\quad\Longleftrightarrow\quad
\mathcal E_{ab}=0
\quad\Longleftrightarrow\quad
g^\sigma=\sigma^{-2}g
\text{ is Einstein}.}
$$

This is the standard almost-Einstein equivalence in the declared four-dimensional conventions.

## Einstein sources as a transport obstruction

Once Einstein gravity and the source normalization are independently granted, the trace-free field equation can be rewritten as

$$
\boxed{
\mathcal E_{ab}
=\frac{4\pi G}{c^4}\,
\sigma T^\circ_{ab},}
$$

with

$$
T^\circ_{ab}
:=
T_{ab}-\frac14Tg_{ab}.
$$

This is an exact reformulation in the stated convention, not a new gravitational equation and not a derivation of \(G\). It says that trace-free stress obstructs parallel scale-tractor transport.

## The scalar channel

The tractor norm retains information discarded by the trace-free projection. In the physical metric \(g^\sigma\),

$$
\boxed{
I^2
=-\frac{R[g^\sigma]}{12}.}
$$

Combining this identity with the trace of the Einstein equation gives

$$
I^2
=\frac{2\pi G}{3c^4}T
-\frac{\Lambda_g}{3}
$$

in the same conventions. The field equation is therefore naturally displayed as

$$
\text{trace-free transport}
\quad\oplus\quad
\text{scalar norm constraint}.
$$

A metric-proportional source shift is invisible to \(T^\circ_{ab}\), but it is not thereby physically absent. Its effect belongs to the trace, scalar, boundary, or global sector.

## Scope

The tractor construction covariantly describes how metric scale sits inside conformal geometry. It does not select a scale section, identify scale with state distinguishability, construct a state-to-geometry map, or solve a residual-vacuum problem. Any proposed state-space explanation of the transport obstruction remains a separate constitutive problem.
