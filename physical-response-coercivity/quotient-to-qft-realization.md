# Quotient-to-QFT Realization

A forgetful pre-observable quotient can coexist with exact recovery of the effective Yang–Mills theory. The quotient must form a compatible regional net, its state channel must be constructed separately, and the effective Euclidean states and forms must converge to data admitting physical reconstruction. Neither an algebraic quotient nor Mosco convergence alone supplies the local QFT, its vacuum, its translations, or its gap.

## QFT compatibility belongs after the nonfaithful quotient

[[algebra/nonfaithful-realization|A genuinely forgetful realization]] cannot itself be an equivalence. To avoid an untyped quotient, first use the algebraic-net version. For every declared Euclidean region $O$, let

$$
q_{r,O}:\mathcal A^{\mathrm{pre}}_{r,G}(O)
\longrightarrow
\mathcal Q_{r,G}(O)
$$

be a surjective $*$-homomorphism with closed two-sided $*$-ideal $I_r(O):=\ker q_{r,O}$. Require, under each declared inclusion $O_1\subseteq O_2$, that $I_r(O_1)=\mathcal A^{\mathrm{pre}}_{r,G}(O_1)\cap I_r(O_2)$. Then the induced quotient inclusions are injective, $q_r$ is a natural quotient map, and

$$
\mathcal Q_{r,G}(O)
\cong
\mathcal A^{\mathrm{pre}}_{r,G}(O)/I_r(O).
$$

Let $\mathcal R_r$ be a declared state-preserving Euclidean-net morphism or localization/reconstruction functor into a reflection-positive Euclidean data package. The **[CONDITIONAL ARCHITECTURE]** is then

$$
\boxed{
(\mathcal A^{\mathrm{pre}}_{r,G}(-),F_t^r)
\xrightarrow[\mathrm{nonfaithful}]{q_r}
\mathcal Q_{r,G}(-)
\xrightarrow{\mathcal R_r}
\mathfrak B^{\mathrm E}_{r,G}
\xrightarrow[\text{directed regulator limit}]
{\text{Mosco plus Euclidean state/correlation convergence}}
\mathfrak B^{\mathrm E}_G
\xrightarrow{\mathrm{OS}}
\mathfrak A_G^{\mathrm{YM}}.}
\tag{D19}
$$

Here $r$ denotes the directed regulator data, including $a\to0$ and $L\to\infty$ when a lattice is used. The symbols $\mathfrak B^{\mathrm E}_{r,G}$ and $\mathfrak B^{\mathrm E}_G$ denote full Euclidean state/correlation/form packages, not bare $C^*$-algebras. Mosco convergence governs their forms and operators on changing Hilbert spaces; convergence of the Euclidean states or Schwinger functions is additional; OS reconstruction applies only after the OS axioms hold and is the later passage to the Lorentzian physical carrier. Thus (D19) is a typed construction target, not one theorem supplied by the quotient. [[yang-mills-continuum-crossover/inq|The continuum-crossover module]] owns the separate uniform-rate, correlation-convergence, and reconstruction requirements. At finite lattice regulator $\mathfrak B^{\mathrm E}_{r,G}$ has only the declared lattice symmetries and reflection structure. Continuous Poincare covariance is a continuum reconstruction target, not a finite-lattice property.

Only the effective image $\mathcal Q_{r,G}(-)$, after carrier reconstruction, is required to recover the Yang--Mills net. The full pre-observable net is not. If $F_t^r(I_r(O))\subseteq I_r(O)$ compatibly for every region, the deterministic preflow descends to the quotient net. If the primitive object is instead a category and $q_r$ is a functor, then $\mathcal Q_{r,G}$ must be defined as the coequalizer of a declared object-and-arrow kernel-pair congruence, when that coequalizer exists; the bare notation $\mathcal C/\ker q$ is not sufficient.

The continuum target must be a pointed Poincare-covariant net, including its inclusions, vacuum state, translation representation, energy form, spectrum condition, and renormalized scale. Recovering one Type-III factor is not enough. An exact state- and Poincare-covariance-preserving natural isomorphism with $\mathfrak A_G^{\mathrm{YM}}$ induces a GNS unitary intertwining translations, and therefore preserves the Poincare Casimir and the mass gap.

The BKM wall is a separate typed datum. Let $\Phi_r$ be a state channel with faithful reference state $\sigma_r$, and set

$$
A_r:=(\mathrm d\Phi_r)_{\sigma_r}.
$$

No formal identity equates the algebraic quotient $q_r$ with the tangent contraction $A_r$. A realization theorem must show that $\Phi_r$ implements the declared accessible quotient and that its reachable BKM tangents belong to the reconstructed physical package.

Approximate low-energy compatibility is weaker. It should compare the full net on energy-bounded states or smeared observables with explicit regulator, volume, heavy-sector, and background errors; a sharp spectral subspace should not be misnamed a local subalgebra. [[physical-response-coercivity/causal-frame-coercivity#Recovery of observed QFT below a UV threshold|The compatibility ledger]] states the exact extension, effective-recovery, and strong-emergence contracts separately.

This factorization respects [[channel-loss-and-recovery/relative-entropy-loss-and-sufficiency|the relative-entropy sufficiency criterion]]. The wall may forget distinctions that do not survive into $\mathcal Q_{r,G}$ while the reconstructed effective image exactly realizes QFT. Petz recovery of the *full source* is neither required nor desired. What must be recovered is the observable net from the effective quotient. Conversely, if a proposed positive residue is evaluated on a family claimed to be Petz-recoverable through the same wall, it vanishes and cannot explain a gap.

## The concrete Yang--Mills research question

The physical realization must supply the following data before [[physical-response-coercivity/retained-output-casimir-bound|the retained-output Casimir implication]] or [[physical-response-coercivity/paired-wall-casimir-comparison|the paired-wall alternative]] can be applied:

1. construct a gauge-invariant scale-indexed source carrier and deterministic or algebraic preflow;
2. construct the accessible algebraic quotient $q_r$, a compatible state channel $\Phi_r$, its reference state and BKM metrics, and the derivative $A_r=(\mathrm d\Phi_r)_{\sigma_r}$ without spectral input;
3. prove that a physically normalized retained-output response is uniformly coercive on the complete reconstructed nonvacuum carrier; genuine contraction of a general channel can supply a nonzero form, whereas one adapted preserving expectation cannot; a relative closed-range criterion must refer to this same form and physical norm;
4. prove a same-carrier Casimir solder and calibrate $E_{*,r}$ from the renormalization trajectory rather than the observed glueball mass;
5. establish [[yang-mills-continuum-crossover/two-scale-rg-descent-and-the-crossover-lemma|controlled ultraviolet-to-infrared transport]] of the physical bound across all remaining scales; and
6. prove that the resulting effective quotient recovers the local Yang--Mills net, state, covariance, and clock dynamics.

This is the precise sense in which “the cause is there but cannot be worked backward toward” may contribute to the mass-gap problem. A declared channel makes an exact incoming distinction residue; noninvertibility can place part of it in inaccessible vertical fibers. The vertical residue alone is not mass. Only a separately nonzero, physically normalized response on retained directions, after carrier reconstruction and energy comparison, could enter a mass-gap theorem.
