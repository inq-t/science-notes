# The Residual Vacuum Sector

Trace-free gravitational transport and normalized state comparisons are locally insensitive to certain common scalar shifts. That insensitivity is a kernel of the local description, not a proof that the residual vanishes. CST therefore treats the zero-residual future as a global sector choice.

For a metric-proportional shift

$$
T_{ab}\longmapsto T_{ab}-\lambda g_{ab},
$$

the trace-free tensor is unchanged:

$$
(T_{ab}-\lambda g_{ab})^\circ=T^\circ_{ab}.
$$

Accordingly, the transport equation in [[conformal-scale-geometry/scale-tractor-transport]] cannot determine the common scalar part by itself. The scalar norm equation, boundary data, global constraint, or another completion must carry that information.

A related phenomenon occurs in normalized state families: adding a scalar multiple of the identity to a modular Hamiltonian changes its unnormalized exponential but cancels from the normalized density operator. Again, cancellation from a normalized comparison does not imply cancellation from gravity.

In the finite Gibbs illustration,

$$
\frac{e^{-\beta(H+C\mathbf1)}}
{\operatorname{Tr}e^{-\beta(H+C\mathbf1)}}
=
\frac{e^{-\beta H}}
{\operatorname{Tr}e^{-\beta H}},
$$

and

$$
\operatorname{Var}(K+\alpha\mathbf1)
=\operatorname{Var}(K).
$$

For local type-III algebras, these density-matrix formulas are analogies; the exact formulation must use an appropriate relative-entropy or crossed-product comparison.

A fixed-background Hamiltonian shift is also not the same operation as varying a gravitational effective action. The term

$$
\Gamma_\Lambda[g]
=-\int\mathrm d^4x\sqrt{-g}\,\Lambda
$$

has nonzero metric variation. Quantum loops can additionally generate curvature terms such as

$$
\int\sqrt{-g}\,R,
\qquad
\int\sqrt{-g}\,R^2,
\qquad
\int\sqrt{-g}\,R_{ab}R^{ab}.
$$

Central blindness of one normalized state channel therefore does not erase the gravitational effective action.

## Sector parameter

At homogeneous level one may write

$$
\rho_{\mathrm{tot}}
=\rho_m+\rho_r+\rho_X+\rho_{\mathrm{res}},
$$

with constant $\rho_{\mathrm{res}}$ as the simplest residual realization. A selected CST member determines $\rho_X$, not $\rho_{\mathrm{res}}$; the currently developed localized pulse is CST-B2.

The canonical transient branch selects

$$
\boxed{\rho_{\mathrm{res}}=0.}
$$

This is **[SECTOR]**. A positive residual produces an asymptotic de Sitter regime; a negative residual may eventually force a turnaround, depending on the other sectors. Neither alternative changes CST-B2's exact balanced-binary profile before background closure, although another [[causal-scale-theory/response-family-interface|response member]] may have a different profile.

## What local blindness does not prove

- It does not solve the cosmological-constant problem.
- It does not establish radiative stability of the zero sector.
- It does not show that the residual is a flux, integration constant, or superselection label; those are completion-dependent possibilities.
- It does not permit vacuum energy to be dropped from local QFT calculations without a matching gravitational prescription.

The open task is to construct a global law that selects and stabilizes a residual sector while preserving the imported local physics. Until then, late coasting in [[unit-branch]] is conditional on the declared zero-residual choice.

[[conjectures/local-global-vacuum-completion|The local--global completion conjecture]] records the stronger possibility that the quotient and scalar equation are two parts of one theory.
