# Causal-Wall Spectral Theory

Causal-Wall Spectral Theory is a non-peer-reviewed research programme that treats primordial scalar structure as the correlation geometry of the dimensionless inhomogeneous scale residue in $-\delta\ln\sigma=\delta N+\zeta_{\mathrm{wall}}$. Its Fourier identities are exact definitions, and a standard domain-wall/cosmology dictionary supplies a conditional spectral representation; the causal-wall state family, its information-geometric weld to that representation, and the covariant spacetime descent remain unconstructed. The present result is therefore a disciplined formulation of a target, not a microscopic completion or a recovery of QFT or the Standard Model.

> [!warning] Status of the long source
> The [editable v3 source](latest-version/Causal_Wall_Spectral_Theory_v3.tex) and [rendered PDF](latest-version/Causal_Wall_Spectral_Theory_v3.pdf) are the latest master document. Version 3 corrects several genuine errors in v2, but its phrases “exact holographic dictionary” and “exact weld” still need the domain and hypotheses recorded in [[causal-wall-spectral-theory/claim-audit|the claim audit]]. The v3 [[causal-wall-spectral-theory/latest-version/Causal_Wall_Spectral_Theory_v3_referee_disposition|referee disposition]] is a revision record, not an independent validation. Files under `old-versions/` and `convo/` remain source history rather than canonical statements of the theory.

The primary literature, official likelihoods, released chains, and reproducibility code used in this review are mirrored in [[causal-wall-spectral-theory/sources/entry|the local source library]]. Canonical citations below resolve to those local copies; upstream locations are kept only in the library's provenance ledger.

## Construction

1. [[causal-scale-interface|The causal-scale interface]] must distinguish the observer-region algebra, the horizon or cut reduction, and a possible three-dimensional spectral representation. Local QFT may supply the fibers; the proposed new structure is the horizontal scale-to-state relation.
2. [[information-geometric-weld|The information-geometric weld]] starts with a scale-indexed state family and an exact exponential-family Hessian lemma. It still needs a continuum algebraic realization and a proof that its BKM kernel becomes the cosmological probability or 1PI precision.
3. [[spectral-dictionary|The spectral dictionary]] fixes the scalar and tensor normalizations in a domain-wall/cosmology member. It is not a universal identity for every QFT or every causal wall.
4. [[critical-kernel|The critical kernel]] follows from homogeneity, isotropy, positivity, dilation covariance, and a dimensionless scalar. The flat kernel has $|k|^3$ shape; a curved $P_3$ representative additionally depends on filling and domain data.
5. [[cosmological-descent|Cosmological descent]] must identify the wall residue with a gauge-invariant curvature perturbation, supply a conserved passive mode, and connect the scalar, tensor, and higher-point responses to ordinary Einstein--Boltzmann transfer.

The [[interpretation|non-stochastic interpretation]] is a separate reading of this construction: it denies that the data require ontological random kicks, but does not eliminate operational probability or solve quantum measurement. [[causal-wall-spectral-theory/open-problems|The theorem programme]] records the construction, recovery, and falsification conditions.

## Central conditional chain

Let $\zeta_{\mathrm{cos}}$ denote the gauge-invariant cosmological curvature perturbation used in the observable power spectrum; in this section $\zeta$ abbreviates $\zeta_{\mathrm{cos}}$. On its physical nonzero-mode subspace, define scalar precision as inverse covariance:

$$
\mathcal K_\zeta(k)
:=P_\zeta(k)^{-1}
=\frac{k^3}{2\pi^2\Delta_\zeta^2(k)}.
$$

For a cosmology possessing the required holographic representation, let $\rho_B^{\mathrm{cos}}(k)>0$ denote the appropriately continued spin-zero response. With the registered normalization

$$
\rho_B^{\mathrm{cos}}(k)
:=\frac{\pi^2}{64}c^{(0)}(k)k^3,
\qquad
\mathcal I_\zeta(k):=\frac{\pi^4}{4}c^{(0)}(k),
$$

the dictionary is

$$
\boxed{
\mathcal K_\zeta(k)
=8\rho_B^{\mathrm{cos}}(k)
=\frac{\pi^2}{8}c^{(0)}(k)k^3
=\frac{\mathcal I_\zeta(k)}{2\pi^2}k^3,
\qquad
\Delta_\zeta^2(k)=\mathcal I_\zeta(k)^{-1}.}
$$

The first equality, $\mathcal K_\zeta=8\rho_B^{\mathrm{cos}}$, is conditional on the stated domain-wall/cosmology representation. The remaining equalities follow algebraically from the registered definitions. The specifically causal-wall claims are the two still-open identifications

$$
\boxed{
-\delta\ln\sigma=\delta N+\zeta_{\mathrm{wall}},
\qquad
\zeta_{\mathrm{wall}}
\stackrel{?}{=}
\zeta_{\mathrm{cos}},
\qquad
\operatorname{Hess}\mathscr J_{\mathrm{wall,spec}}
\stackrel{?}{=}
\mathcal K_{\zeta_{\mathrm{cos}}}.}
$$

Matching a factor of two does not prove the Hessian-to-precision equality: one must relate a relative-entropy Hessian, a Euclidean stress response, the continued wavefunctional, and the inverse connected covariance without conflating them.

## Claim ledger

| Status | Content |
|---|---|
| Exact or standard in its stated domain | Fourier covariance/precision conversion; the regular exponential-family BKM Hessian; the three-dimensional stress-tensor tensor decomposition; algebraic scalar/tensor normalization conversions; the flat $|k|^3$ scaling result; tilt and running identities; numerical arithmetic |
| Conditional established framework | McFadden--Skenderis domain-wall/cosmology spectra after the required analytic continuations, vacuum/state choice, and holographic assumptions; fractional $P_3$ from suitable conformal filling data; standard conserved-curvature transfer after the usual spacetime assumptions |
| Programme hypotheses | an observer-relative causal-scale interface; a common algebra or controlled transport between algebras, together with faithful scale-indexed states; stress-trace generation of the horizontal tangent; BKM-to-spectral-to-probability weld; one physical scalar clock; passive rank-one descent |
| Open functions or sectors | $c^{(0)}(k)$, $c^{(2)}(k)$, cubic and higher vertices, the state-selection law, the tensor prediction, and the covariant perturbation dynamics |
| Interpretive | primordial correlations need not be caused by temporally localized ontological random events; the three-dimensional QFT may be a representation rather than the wall's ontology |
| Not demonstrated | locality, unitarity, hyperbolicity, stability, a complete action or constraint system, a Standard Model recovery/decoupling limit, and an end-to-end likelihood derived from the wall construction |

## Present verdict

The work is not flagrantly at odds with prevailing physics when read as an interface proposal that imports ordinary local QFT, GR constraints, and standard transfer. It does **not** presently recover QFT or the Standard Model in the strong sense in which Newtonian gravity is recovered inside GR. Its most secure achievement is a careful reparameterization of the observable correlation target plus a useful list of mathematical joints that a genuine wall realization would have to close.
