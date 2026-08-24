# Symmetrized Relative-Entropy Hessian

For a twice differentiable faithful state family on one fixed finite algebra, the two orientations of relative entropy have the same coincidence Hessian, namely the Bogoliubov--Kubo--Mori metric; their sum therefore has Hessian twice that metric. This exact local result fixes a factor of two, but it does not identify the metric with a Euclidean correlator, a Lorentzian response, or a probability precision.

Claim labels follow [[program-core/axioms-and-principles#Status vocabulary|the programme-wide status vocabulary]].

## The coincidence theorem

Let \(\rho_\lambda\) be a \(C^2\) family of faithful density operators on one finite-dimensional algebra, with \(\lambda=0\) the reference point. Write

$$
D(\rho\Vert\sigma)
:=\operatorname{Tr}\!\left[\rho(\log\rho-\log\sigma)\right]
$$

and let \(u=u^i\partial_i\) be a tangent at \(\lambda=0\). Under the usual support and differentiability hypotheses,

$$
D(\rho_{tu}\Vert\rho_0)
=\frac{t^2}{2}g^{\mathrm{BKM}}_0(u,u)+o(t^2),
$$

$$
D(\rho_0\Vert\rho_{tu})
=\frac{t^2}{2}g^{\mathrm{BKM}}_0(u,u)+o(t^2).
$$

Consequently, for the Jeffreys or symmetrized divergence

$$
\mathscr J(\lambda)
:=D(\rho_\lambda\Vert\rho_0)
+D(\rho_0\Vert\rho_\lambda),
$$

one has

$$
\boxed{
\operatorname{Hess}_0\mathscr J(u,v)
=2g^{\mathrm{BKM}}_0(u,v).}
$$

This is **[EXACT]** in the declared regular finite setting. The factor two comes from adding two divergences whose quadratic terms agree. It is not evidence that the reverse divergence is a complex-conjugate wavefunctional.

For a regular quantum exponential family

$$
\rho_\lambda
=\exp\!\left(
\log\rho_0+\lambda^iA_i-\psi(\lambda)
\right),
$$

with centered scores \(\widetilde A_i=A_i-\operatorname{Tr}(\rho_0A_i)\mathbf 1\), the coefficient is

$$
g^{\mathrm{BKM}}_{ij}
=\int_0^1
\operatorname{Tr}\!\left(
\rho_0^s\widetilde A_i
\rho_0^{1-s}\widetilde A_j
\right)\,\mathrm ds .
$$

When the scores commute with the state, this reduces to their ordinary covariance. In general the BKM ordering is part of the object.

## Why both orientations agree only to second order

Relative entropy is directed. The equality above says that its two orientations induce the same Riemannian metric on the diagonal; it does not say

$$
D(\rho_\lambda\Vert\rho_0)
=D(\rho_0\Vert\rho_\lambda)
$$

at finite separation. Their cubic and higher derivatives generally differ. [[basic-concepts/hessians/higher-relative-entropy-is-not-cumulants|The higher-derivative no-go]] makes this failure explicit even for a commuting one-parameter exponential family.

## Continuum boundary

Local relativistic QFT algebras are generally type III and need not admit density operators or an ordinary trace. A continuum upgrade requires faithful normal states on a common von Neumann algebra, Araki relative entropy, a controlled perturbation class, and a proof that the relevant second variation is finite or renormalized. The foundational sources are [[causal-wall-spectral-theory/sources/papers/1976-araki-relative-entropy-von-neumann-algebras-i.pdf|Araki I]], [[causal-wall-spectral-theory/sources/papers/1977-araki-relative-entropy-von-neumann-algebras-ii.pdf|Araki II]], and [[causal-wall-spectral-theory/sources/papers/1973-araki-relative-hamiltonian-faithful-normal-states.pdf|the relative-Hamiltonian construction]]. The relation between relative entropy and monotone quantum metrics is treated by [[causal-wall-spectral-theory/sources/papers/9808016-lesniewski-ruskai-monotone-riemannian-metrics-relative-entropy.pdf|Lesniewski--Ruskai]] and [[causal-wall-spectral-theory/sources/papers/1995-petz-sudar-geometries-quantum-states-substitute.pdf|Petz--Sudar]].

No finite-dimensional calculation constructs the scale-indexed wall state, the cross-fiber transport, or the continuum response measure required by [[wall-construction-interface/entry|the wall interface]].

## What the theorem does not identify

The conclusion is one local state-space bilinear form. Further equalities require separate theorems:

$$
g^{\mathrm{BKM}}
\not\equiv
\langle TT\rangle_{\mathrm E}
\not\equiv
G^{\mathrm R}_{TT}
\not\equiv
\Gamma^{(2)}
\not\equiv
\mathcal C^{-1}.
$$

Some of these objects coincide in particular commuting, equilibrium, Gaussian, or analytically continued models. The hypotheses establishing each arrow are not contained in the word *Hessian* or in the numerical factor two.
