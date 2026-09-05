# Polarization Is Not Positive State Geometry

A polarization in Hodge theory or geometric quantization and the Bogoliubov--Kubo--Mori metric on faithful states are different structures. The signature-\((1,1)\) invariant form in the torus-fibered \(S^6\) construction blocks a polarized-Hodge route through that family and cannot directly serve as positive BKM geometry on the full rank-two Hodge bundle. It neither destroys the established integrable complex structure nor forbids a separately constructed positive state subquotient.

## Three uses of positivity

Several positive structures occur in mathematical physics and should not be merged.

### Hermitian metric on a complex manifold

A Hermitian metric is a smoothly varying positive form on \(T^{1,0}X\). Every paracompact complex manifold admits such metrics. Its associated real two-form need not be closed.

### Symplectic and Kähler geometry

A Kähler metric has a closed positive fundamental form \(\omega\). In conventional geometric quantization, one begins with a symplectic form satisfying an integrality condition, constructs a prequantum line bundle whose connection has curvature proportional to \(\omega\), and chooses a polarization to reduce the prequantum sections to a quantum state space.

For a compact manifold diffeomorphic to \(S^6\),

$$
H^2(S^6;\mathbb R)=0.
$$

If a symplectic form existed, it would be exact, \(\omega=\mathrm d\alpha\), and hence

$$
\int_{S^6}\omega^3
=
\int_{S^6}\mathrm d(\alpha\wedge\omega^2)
=0.
$$

This contradicts positivity of symplectic volume. Thus the smooth \(S^6\) admits no symplectic form, every integrable complex structure on it is non-Kähler, and conventional Kostant geometric quantization cannot use it directly as a symplectic phase space.

### BKM metric on faithful states

Let

$$
\rho\in M_n(\mathbb C),
\qquad
\rho>0,
\qquad
\operatorname{Tr}\rho=1,
$$

and let \(A,B\) be self-adjoint exponential-score representatives. Define

$$
\widetilde A
:=A-\operatorname{Tr}(\rho A)\mathbf1,
\qquad
\widetilde B
:=B-\operatorname{Tr}(\rho B)\mathbf1.
$$

The score-coordinate BKM form is

$$
g^{\mathrm{BKM}}_\rho(A,B)
=
\int_0^1
\operatorname{Tr}
\left(
\rho^s\widetilde A
\rho^{1-s}\widetilde B
\right)\,\mathrm ds.
$$

For density tangents one instead composes with the inverse Kubo--Mori map

$$
\Omega_\rho(C)
:=
\int_0^1\rho^sC\rho^{1-s}\,\mathrm ds.
$$

The carrier is a faithful-state manifold of a represented operator algebra. BKM is not a two-form on \(X\), and it need not be obtained from the Hodge structure of \(X\).

## What the manuscript actually obstructs

The manuscript identifies, up to sign, a monodromy-invariant alternating form \(Q_0\). To avoid confusing two unrelated uses of \(\tau\), write its period function as \(\tau_{\mathrm{per}}\) in this note. With the manuscript's other period functions \(\mu,\beta\), define

$$
D
:=
\operatorname{Im}\beta
-
\frac{6(\operatorname{Im}\mu)^2}
{\operatorname{Im}\tau_{\mathrm{per}}}
<0.
$$

On the Hodge subspace \(F^1(z)\), the associated Hermitian form has

$$
\det h
=
24\,\operatorname{Im}\tau_{\mathrm{per}}\,D
<0,
$$

and therefore signature \((1,1)\). The manuscript concludes that the torus family carries no monodromy-compatible polarization and that its unipotent degeneration supports no \(Q_0\)-polarized limiting mixed Hodge structure.

This is **[EXACT INSIDE THE CONDITIONAL MANUSCRIPT]**. It rules out using that full-rank Hodge form directly as a positive BKM metric. The unqualified equality

$$
iQ_0(-,\overline{-})
=
g_{\mathrm{BKM}}
$$

would already be ill-typed because its two sides live on different carriers. A positive subquotient is not logically excluded, but it would require a monodromy-compatible selection functor and an independently constructed map into state tangents. Nor does the signature computation prove that no positive Hermitian metric exists on the total complex manifold.

## The philosophically stronger separation

One metric need not simultaneously perform four incompatible jobs:

$$
\begin{array}{c|c|c}
\text{object} & \text{carrier} & \text{role}\\
\hline
Q_0 & \text{lattice/Hodge data} & \text{monodromy-invariant alternating form}\\
h_{Q_0} & F^1 & \text{Hodge signature and polarization test}\\
g_{\mathrm{BKM}} & T\mathcal S_{\mathrm{faithful}} & \text{quantum distinguishability}\\
g_{\mathrm L} & TM_{3+1} & \text{Lorentzian intervals and causal cones}
\end{array}
$$

The programme's ontology can contain all four, connected by maps, without reducing them to one master metric. This is not retreat from mathematical realism. It is ontological type-checking.

## Required state-bundle construction

Let \(B^\circ\) be the nonsingular parameter base of a complex family. A positive response layer would require a bundle or field of operator algebras and faithful states

$$
b\longmapsto(\mathcal A_b,\rho_b)
$$

together with cross-fiber transport. Monodromy should act by state-preserving \(*\)-isomorphisms, correspondences, or another explicitly declared morphism class. Only then can the vertical BKM forms be compared and asked to descend:

$$
g^{\mathrm{BKM}}_{\rho_b}
\stackrel{?}{\longrightarrow}
g^{\mathrm{BKM}}_{\mathrm{desc}}.
$$

The missing realization functor must explain why this state bundle is selected by the complex family rather than placed beside it. A common spectral family may help: Gibbs states, heat kernels, and determinant lines can be different functorial constructions from one \(D_b\), while remaining different mathematical objects.

[[algebra/exceptional-context-response|Exceptional context response]] gives a finite construction from a different upstream object: an order-three Albert automorphism determines a positive Jordan retraction, whose regular multiplication representation intertwines an associative CP expectation. On a declared faithful matrix-state family, the relative-entropy-loss Hessian is exactly proportional to the Jordan residue. This realizes an order-to-state-response map without using a Hodge polarization; it does not yet select a state bundle from the integrable complex family or cover the entire matrix-state tangent space.

## Relation to real form and factivity

A positive state metric also does not choose an actual real locus. [[algebra/real-forms-and-factive-spacetime|Real-form selection]] requires an antiholomorphic involution, written here as

$$
\tau_{\mathrm{real}}:X\longrightarrow X
$$

to distinguish it from \(\tau_{\mathrm{per}}\). Factivity then requires a separate noninvertible operation selecting compatible records. Neither follows from a Hodge polarization, and neither is contradicted by the absence of one.

The correct conclusion is consequently narrow and useful:

$$
\boxed{
\text{no invariant Hodge polarization}
\Longrightarrow
\text{do not use this full Hodge form directly as positive response}.}
$$

Every stronger physical conclusion requires an additional theorem.
