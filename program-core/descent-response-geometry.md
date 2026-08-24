# Descent-Response Geometry

The proposed mathematical bottom of the causal-response branch is a positive, localized response geometry on the physical horizontal quotient. It begins after algebra, state, causal cut, scale, transport, differentiability, and a prospective area carrier have been supplied. Its primary object is a measure-valued bilinear form; the scalar areal modulus used in homogeneous cosmology is a contraction and average of that richer object.

## The state bundle is an open construction

For each admissible causal cut, the programme seeks

$$
N\longmapsto
(\Sigma_N,\mathcal A_N,\omega_N,\mathcal T_{N_2N_1}),
$$

where \(\mathcal T_{N_2N_1}\) transports states or observables to a common carrier. Without this comparison structure, \(\partial_N\omega_N\) and relative entropy between scales are not well typed. The wall algebra, preferred state family, and transport must be constructed independently of the target cosmological history and of the gravitational coefficient to be explained.

Write \(\widetilde\omega_{N+\delta N}^{(N)}\) for \(\omega_{N+\delta N}\) transported into the \(N\)-fiber by the declared dual transport. The tilde is part of the typing, not optional notation.

Let \(\Phi\) denote the resulting scale-to-state map and \(H_p\) the physical horizontal tangent object from [[program-core/physical-quotient|the quotient construction]]. The physical scale tangent is

$$
v_N:=D^{\mathrm{hor}}\Phi(\partial_N).
$$

The declaration that \(v_N\) is canonical includes its normalization. A rescaling \(v_N\mapsto av_N\) rescales every quadratic capacity by \(a^2\).

## Coincidence distinguishability

When the compared family is sufficiently regular,

$$
D(\widetilde\omega_{N+\delta N}^{(N)}\Vert\omega_N)
=\frac12g^{\mathrm{BKM}}_{\omega_N}(v_N,v_N)
\delta N^2+o(\delta N^2).
$$

Define

$$
G^{\perp}_{NN}
:=g^{\mathrm{BKM}}_{\omega_N}(v_N,v_N)\geq0
$$

after the declared vertical, central, gauge, and null directions have been removed. This is a local squared speed or susceptibility along one state path. It is dimensionless when \(N\) is dimensionless.

The equality with a BKM form is **[EXACT — UNDER THE ANALYTIC AND COMPARABILITY HYPOTHESES]**. The existence of a finite continuum wall norm and its physical interpretation are open. [[basic-concepts/hessians/entry#Log-partition Hessians and Fisher geometry|The Hessian module]] owns the analytic result and its scope; [[basic-concepts/hessians/gibbs-free-energy-relative-entropy|the fixed-Gibbs corollary]] keeps its thermodynamic use separate from an all-history source.

## Localization is an additional theorem target

For physical horizontal tangents \(v,w\), require a symmetric bilinear map into finite signed measures on measurable patches \(U\subseteq\Sigma\),

$$
\mu^{\mathrm{desc}}_{v,w}(U),
$$

whose diagonal \(\mu^{\mathrm{desc}}_{v,v}\) is positive and countably additive. Localization must recover the global BKM form:

$$
\boxed{
\mu^{\mathrm{desc}}_{v,w}(\Sigma)
=g^{\mathrm{BKM}}_{\omega}(v,w).}
$$

Cross measures may equivalently be obtained by polarization,

$$
\mu^{\mathrm{desc}}_{v,w}
=\frac14\left(
\mu^{\mathrm{desc}}_{v+w,v+w}
-\mu^{\mathrm{desc}}_{v-w,v-w}
\right),
$$

provided a measure-level Cauchy--Schwarz bound makes them finite. The form should be local or controlledly quasilocal, covariant under presentation arrows, finite after a declared renormalization, and compatible with restriction to subregions.

Let \(\mu_A\) be an independently normalized causal-area measure. Require every diagonal measure to satisfy

$$
\mu^{\mathrm{desc}}_{v,v}\ll\mu_A.
$$

With the polarization and Cauchy--Schwarz hypotheses, the cross measures are then absolutely continuous as well. Equivalently, one may posit an absolutely continuous matrix-valued measure from the outset. The Radon--Nikodym derivative defines the **areal descent modulus**

$$
\boxed{
\boldsymbol\chi_{\Sigma,\omega}(v,w;p)
:=
\frac{\mathrm d\mu^{\mathrm{desc}}_{v,w}}
{\mathrm d\mu_A}(p),\qquad p\in\Sigma.}
$$

For \(v=w\), it is nonnegative almost everywhere. In a smooth finite-rank realization with dimensionless normalized tangent coordinates, its components form an \(L^{-2}\)-valued symmetric bilinear form on the physical horizontal tangent bundle. In a singular groupoid or stack it may instead belong to a tangent complex or stratified family; the scalar notation does not prejudge regularity.

## Local density, cut average, and universal scalar

Three objects must not share one symbol:

1. the local contraction

   $$
   \chi_N(p):=\boldsymbol\chi(v_N,v_N;p);
   $$

2. the cut average

   $$
   \overline\chi_{\Sigma,N}
   :=\frac{\mu^{\mathrm{desc}}_{v_N,v_N}(\Sigma)}
   {A_\Sigma};
   $$

3. a universal Einstein-class scalar \(\chi_*\), if the local density is shown to be constant throughout a declared class.

The first can vary over a cut, the second can hide that variation, and the third is a strong universality statement. Extensive scaling on one cosmological horizon proves neither locality nor universality.

The historical scalar notation is retained only as an alias for the cut average:

$$
\boxed{
\chi_\downarrow[\Sigma,N]
:=\frac{G^\perp_{NN}(N)}{A_\Sigma}
=\overline\chi_{\Sigma,N}.}
$$

It must not be substituted for the local field \(\chi_N(p)\) without a homogeneity theorem.

The inverse on a nondegenerate sector is **causal compliance**:

$$
\mathfrak a_N(p):=\chi_N(p)^{-1},
\qquad
[\mathfrak a_N]=L^2.
$$

It is area per unit natural-log distinguishability curvature. It is not automatically an area atom, minimal pixel, or spectrum eigenvalue.

## Why the primary object is tensorial

Scalarizing at the outset assumes that every admissible physical direction has the same response. The local bilinear form allows:

- different homogeneous and inhomogeneous response blocks;
- anisotropic eigenvalues;
- null or constrained directions;
- state-, species-, curvature-, or scale-dependent response; and
- mixing terms between sectors.

Einstein universality would be the special case in which the relevant state-to-geometry identification makes this form proportional to one gravitational form with one constant coefficient. A modified return value is therefore informative rather than a definitional failure.

## Global and nonconstant observational response blocks

A useful construction chart separates the canonically normalized global scale direction from physical nonconstant differentiations in the observational descent:

$$
H_\Sigma^{\mathrm{candidate}}
\simeq
\mathbb R v_N
\oplus
\left(C^\infty(\Sigma)/\mathbb R\right)_{\mathrm{phys}}.
$$

The second summand does not assert that the sub-observable algebra is a fundamentally lumpy spatial object. Under [[program-core/contextual-descent-from-homogeneity|contextual descent]], it may instead parameterize how one homogeneous algebraic datum becomes distinguishable through nonconstant readout modes. The subscript is essential: gauge, constraint, boundary, and null directions must be removed, so the displayed decomposition is a schematic chart rather than a canonical splitting. In such a chart the global response has the operator-block form

$$
g^{\mathrm{BKM}}
\simeq
\begin{pmatrix}
G^\perp_{NN} & G_{N\zeta}\\
G_{\zeta N} & G_{\zeta\zeta}
\end{pmatrix},
$$

and the localized object has the corresponding matrix of measures or densities. The off-diagonal blocks test mixing; they are not presumed to vanish.

[[program-core/common-response-matrix|The common-response construction]] refines this display as a pullback BKM or descent-cost Hessian and includes hidden or constrained modes before physical reduction. The construction succeeds only if one common carrier, transport, tangent quotient, and renormalization prescription produce both the global contraction and the abstract nonconstant block. A three-dimensional Fourier precision is a further representation, not part of that block merely by notation. Only after a three-dimensional carrier has been constructed may a consumer seek a map

$$
G_{\zeta\zeta}
\xrightarrow{\;\mathfrak B\;}
\mathcal K_\zeta,
\qquad
\langle f,\mathcal K_\zeta f\rangle
:=
\int\frac{\mathrm d^3k}{(2\pi)^3}
\mathcal K_\zeta(k)|f_{\mathbf k}|^2.
$$

The core supplies no \(\mathfrak B\). [[causal-wall-spectral-theory/conjectures/state-response-is-spatial-precision|CWST's state-to-spatial-precision conjecture]] owns the carrier-changing transfer, while [[causal-wall-spectral-theory/conjectures/homogeneous-inhomogeneous-common-geometry|the CWST common-matrix note]] states the consumer-specific claim that the homogeneous and spectral returns descend from this one core geometry. If the pulse coefficient and \(\mathcal K_\zeta\) are supplied by independent ansätze or separately fitted normalizations, they have not been shown to be representations of one response.

The homogeneous areal modulus must also remain distinct from any spectral response density carried by a three-dimensional measure. For example, a kernel \(\mathcal K_\zeta\) normalized per volume has units \(L^{-3}\), not \(L^{-2}\). Relating such a spectral object to \(\boldsymbol\chi\) requires an explicit integration, boundary map, or soldering theorem; similarity of interpretation does not repair the dimensional mismatch.

## Binary geometry is a reduced shape, not the modulus

For a granted balanced binary family,

$$
g^{\mathrm{bin}}_{\theta\theta}
=\operatorname{sech}^2\theta
$$

is an exact normalized shape. A physical wall norm has an extensive factor and a physical tangent normalization:

$$
G^{\perp}_{NN}(N)
=C_\perp(N)
\left(\frac{\mathrm d\theta}{\mathrm dN}\right)^2
\operatorname{sech}^2\theta.
$$

The binary algebra determines neither \(C_\perp\) nor the number of channels per square metre. Replicating a channel changes the extensive norm while preserving its normalized Casimir. This is the missing dimensional content identified by [[deriving-value-of-g/obstructions-to-an-unconditional-proof|the capacity no-go results]].

## Susceptibility is not fact formation

The BKM form compares neighboring states. It does not select an outcome, prove that a fact occurs, or show that a lost distinction has become geometry. The proposed causal-individuation architecture therefore has three separately typed layers:

$$
\text{physical quotient}
\longrightarrow
\text{response geometry}
\dashrightarrow
\text{facts and records}.
$$

The quotient and response nodes both have partial construction targets with standard mathematical ingredients; the localization and continuum completion are not yet supplied. The solid arrow names that response construction. The dashed response-to-fact arrow is the separate, philosophically motivated factive step and remains mathematically open.
