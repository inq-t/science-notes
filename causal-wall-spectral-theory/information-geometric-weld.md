# The Information-Geometric Weld

The proposed weld identifies the information metric of a scale-deformed wall state with the inverse covariance of the cosmological scale residue. The finite or regularized exponential-family Hessian is exact; every arrow from that Hessian to a continuum stress spectral density and then to a cosmological probability kernel requires additional structure that has not yet been constructed.

## Scale residue and physical subspace

Let $\sigma$ be a positive scale section and $\bar\sigma$ a homogeneous reference. Write

$$
-\delta\ln\sigma(x)=\delta N+\zeta(x).
$$

The homogeneous displacement $\delta N$ and the inhomogeneous residue $\zeta$ are different tangent directions. On a compact wall one may impose

$$
\int_\Sigma\zeta=0,
$$

and in flat space remove the $k=0$ mode. This gives the vector-space decomposition

$$
T_{\bar\sigma}\mathfrak{Sc}(\Sigma)
\simeq\mathbb R\oplus C^\infty(\Sigma)/\mathbb R.
$$

The quotient removes a homogeneous redundancy; it does not by itself make the two summands orthogonal in an information metric. At a homogeneous and isotropic reference, harmonic symmetry makes $k=0$ orthogonal to $k\ne0$ at quadratic order. Mixed terms can return beyond quadratic order or on an inhomogeneous background.

The notation also does not yet prove that this $\zeta$ is the gauge-invariant comoving curvature perturbation used in CMB calculations. That is a separate spacetime reconstruction problem in [[cosmological-descent]].

## Exact regular exponential-family lemma

On one finite-dimensional algebra, or in a controlled regularization, consider

$$
\rho_\zeta
:=\exp\!\left(
\log\rho_0+X[\zeta]-\psi[\zeta]
\right),
\qquad
X[\zeta]
:=\int_\Sigma\sqrt g\,\zeta(x)T(x),
$$

where $\psi$ normalizes the state. For the symmetrized relative entropy

$$
\mathscr J[\zeta]
:=D(\rho_\zeta\Vert\rho_0)
+D(\rho_0\Vert\rho_\zeta),
$$

both orientations have the same quadratic term at $\zeta=0$. Therefore

$$
\boxed{
\left.
\frac{\delta^2\mathscr J}
{\delta\zeta(x)\delta\zeta(y)}
\right|_{0}
=2G^{\mathrm{BKM}}_{TT}(x,y).}
$$

This is the sound mathematical core of the v3 factor-of-two correction. It assumes a regular exponential family on a fixed algebra and identifies the score $T$ by construction; the relation between relative entropy and monotone quantum metrics is standard information geometry, as reviewed by [[causal-wall-spectral-theory/sources/papers/9808016-lesniewski-ruskai-monotone-riemannian-metrics-relative-entropy.pdf|Lesniewski and Ruskai]] and classified in operator-monotone form by [[causal-wall-spectral-theory/sources/papers/1995-petz-sudar-geometries-quantum-states-substitute.pdf|Petz and Sudár]].

Local relativistic QFT algebras are generally type III and need not admit density matrices or an ordinary trace. A continuum statement must use faithful normal states, [[causal-wall-spectral-theory/sources/papers/1976-araki-relative-entropy-von-neumann-algebras-i.pdf|Araki relative entropy]] with the [[causal-wall-spectral-theory/sources/papers/1977-araki-relative-entropy-von-neumann-algebras-ii.pdf|support qualifications of Part II]], relative modular operators, and a controlled cocycle or source perturbation. [[causal-wall-spectral-theory/sources/papers/1973-araki-relative-hamiltonian-faithful-normal-states.pdf|Araki's relative-Hamiltonian construction]] is a natural starting point for an algebraic exponential perturbation, but the required wall family has not been built from it. The finite formula demonstrates the desired local geometry; it does not instantiate the physical wall family.

## Four kernels that must not be conflated

The construction involves four related but distinct quadratic objects.

1. **State-space metric:** $G^{\mathrm{BKM}}_{TT}$ is the Hessian of relative entropy for the chosen state family.
2. **Euclidean source response:** $\delta^2W/\delta\zeta\delta\zeta$ is a connected Euclidean stress-trace correlator plus local contact terms.
3. **Wavefunctional kernel:** a domain-wall/cosmology continuation may turn a Euclidean response into the quadratic exponent of a cosmological wavefunctional.
4. **Probability or 1PI precision:** the inverse connected covariance is $\mathcal C_\zeta^{-1}$; for a Gaussian probability weight it is also the quadratic coefficient of $-\log\mathbb P$.

In a generic noncommutative or thermal state, BKM, Euclidean, Wightman, retarded, and spectral kernels are connected by state-dependent modular or KMS transforms; they are not numerically identical merely because the same operator $T$ appears. Similarly, reverse relative entropy is not the complex-conjugate wavefunctional. [[causal-wall-spectral-theory/sources/papers/1104.2621-harlow-stanford-operator-dictionaries-wave-functions.pdf|Harlow and Stanford]] show in a controlled AdS/dS setting why analytic continuation at wavefunction level does not collapse the distinct operator dictionaries. Symmetrization supplies the desired numerical factor but does not derive the passage from $\mathscr J$ to $|\Psi|^2$.

For a non-Gaussian field, the raw quadratic term in $-\log\mathbb P[\zeta]$ is not generally the exact inverse covariance. The exact relation

$$
\Gamma^{(2)}=\mathcal C_\zeta^{-1}
$$

belongs to the Legendre 1PI effective action $\Gamma$. The wall programme must therefore either establish a Gaussian/quasi-free regime or show that the spectral Hessian of $\mathscr J$ is the relevant 1PI Hessian.

## Weyl source and stress response

For a renormalized Euclidean generating functional $W[g]=\log Z[g]$, a local Weyl variation conventionally gives

$$
\frac{\delta W}{\delta\zeta(x)}
=\sqrt g\,\langle T^i{}_i(x)\rangle
$$

up to the registered sign. The second variation contains

$$
\frac{\delta^2W}{\delta\zeta(x)\delta\zeta(y)}
=\langle T(x)T(y)\rangle_c
+\text{local terms}.
$$

This source identity does not prove that the physical scale map $\Phi:\sigma\mapsto\omega_\sigma$ is the exponential or Araki-perturbed family generated by $T$. Nor does it identify the four-dimensional matter trace, a horizon boost generator, and the three-dimensional holographic trace; the relevant maps among those operators remain part of the weld.

Local counterterms polynomial in $q^2$ have zero discontinuity across a spectral cut:

$$
\operatorname{Disc}p(q^2)=0.
$$

This is a useful one-way removal of contact ambiguity. Saying that the discontinuity is *precisely* the quotient by contacts additionally requires analyticity, dispersion, and growth assumptions; not every zero-discontinuity term is automatically a local polynomial. Boundaries, defects, parity-odd sectors, and anomaly terms also require separate bookkeeping.

## The proposed equality

With all intermediate maps displayed, the intended chain is

$$
\operatorname{Hess}\mathscr J_{\mathrm{wall}}
=2G^{\mathrm{BKM}}_{TT}
\stackrel{?}{\longrightarrow}
\text{continued stress response}
\stackrel{?}{\longrightarrow}
\Gamma^{(2)}_\zeta
=\mathcal K_\zeta.
$$

In the v3 convention the desired endpoint is

$$
\mathcal K_\zeta(k)=8\rho_B^{\mathrm{cos}}(k).
$$

The coefficient is consistent with the Fourier and holographic normalizations in [[spectral-dictionary]]. Consistency of coefficients is a necessary normalization check, not a derivation of the arrows.

## Success and failure conditions

A proof of the weld must provide:

- a common algebra and faithful scale-deformed state family;
- a renormalized trace operator that genuinely generates its Weyl tangent;
- the exact BKM-to-Euclidean kernel relation for the selected state;
- the state, vacuum, regulator, and complete analytic continuation to cosmology;
- a probability or 1PI construction with the factor of two counted once;
- positivity and invertibility on the physical quotient; and
- the identification of the resulting variable with cosmological curvature.

The proposed causal-wall realization fails if these data yield a different kernel, an uncontrolled KMS factor, no positive physical continuation, or no common algebra on which the relative state geometry exists.
