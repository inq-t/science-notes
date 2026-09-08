# Scale-Wall-to-Casimir Comparison

A sharp logistic Poincare inequality reaches the physical mass problem only through a complex-linear analysis map that covers the complete vacuum complement and an independently normalized comparison with the Poincare Casimir. The theorem below gives that conditional implication, distinguishes the exact OS interface leg from the still-open boundary-to-scale leg, and shows why a universal resolvent frame does not by itself fill the latter. The scale law and normalization choices are supplied by [[logistic-scale-geometry/pointing-coercivity-and-the-flat-partner-law|pointing coercivity]].

## A gapless causal direction is compatible with the scale edge

The generator \(L_{\nu,N_c}\) acts on distinctions across logarithmic core scale. It is not either null-translation generator \(P_+\) or \(P_-\). A nonzero HSMI translation generator is forced by dilation covariance to have spectrum \([0,\infty)\), so attaching the edge \(\nu^2\) directly to one such generator would contradict the exact no-gap theorem.

The permitted route is the one in [[mass-scale-calibration/joint-causal-generators-and-the-mass-casimir]]: a compatible modular constellation must first reconstruct one positive-energy Poincare representation and the strongly commuting family \(P_\mu\); mass is then the joint invariant \(\mathcal C=H^2-c^2\mathbf P^2\). [[library/relative-positions-of-half-sided-modular-inclusions/inq|Koot's relative-position analysis]] shows why separately available half-sided inclusions do not automatically provide the required commutation. The wall form may serve as a comparison norm for \(\mathcal C\) only after this kinematic reconstruction. It never requires either causal direction itself to become gapped.

## The wall--Casimir sandwich

The scale-shadow gap becomes relevant to Yang--Mills only through the missing carrier map. Let \(\mathcal H_r\) be a physical carrier at a stage where a strongly continuous positive-energy Poincare representation has already been reconstructed. Let its strongly commuting translation generators be \((H_r,\mathbf P_r)\), and let \(P_{0,r}\) be the vacuum projection reducing them. Define

$$
\mathcal C_r
=
H_r^2-c^2\mathbf P_r^2
$$

as its positive Poincare Casimir. A finite lattice regulator does not yet have this exact Casimir; there the analogous comparison must first be made with the reflection-positive transfer-energy form and then carried through covariance recovery. Allow a multiplicity space \(\mathcal K_r\) for all physical wall channels, and write

$$
\mathcal V^{\mathrm{sc}}_{\nu_r,N_{c,r}}
:=
\left\{
F\in L_0^2(\mu_{\nu_r,N_{c,r}}):
\partial_NF\in L^2(\mu_{\nu_r,N_{c,r}})
\right\}
$$

for the mean-zero scale form domain, equipped with the graph norm

$$
\|F\|_{\mathcal V^{\mathrm{sc}}}^2
:=
\|F\|_{L^2(\mu)}^2
+
\int_{\mathbb R}\|\partial_NF\|^2\,\mathrm d\mu.
$$

The analysis map must not hide the already constructible correspondence leg. Under the reflection-Markov, reflection-fixed-separator, and dense-interface-insertion hypotheses of [[global-local-response-reconstruction/vacuum-boundary-gluing-and-wall-response#The OS quotient factors exactly through a reflection interface|the OS interface theorem]], conditional expectation induces a unitary

$$
B_r^{\mathrm{OS}}:
\mathcal H_{\mathrm{OS},r}
\longrightarrow
L^2(\nu_{r,I})^{\mathrm{GI}},
$$

which sends the distinguished OS reference vector to \(1\) and exactly factors the OS null subspace. After infinite-depth preparation and a proof that this vector is the unique vacuum, write its projection as \(P_{0,r}\). The remaining composite leg is then a geometrically defined boundary-to-log-scale analysis transform

$$
S_r:
L_0^2(\nu_{r,I})^{\mathrm{GI}}
\longrightarrow
\mathcal V^{\mathrm{sc}}_{\nu_r,N_{c,r}}
\widehat\otimes\mathcal K_r,
$$

and the physical-to-scale map must factor as

$$
\boxed{
\mathcal J_r
=
S_rB_r^{\mathrm{OS}}(1-P_{0,r}).}
\tag{PC7b}
$$

An abstract Hilbert-space unitary cannot serve as \(S_r\): it must arise from boundary/RG geometry, respect the relevant form domains and complex phases, and be natural under regulator comparison. When \(I\) is thicker than the canonical transfer slice, \(S_r\) must also include or factor through a separately constructed interface-to-slice map. Thus the OS quotient-to-interface leg is exact under declared hypotheses; selecting its physical scale operator remains open.

[[logistic-scale-geometry/resolvent-logistic-scale-transform]] now supplies an exact candidate for the **coverage** part of this missing leg. Given an independently constructed nonnegative self-adjoint interface operator \(L_{r,I}\) with \(\ker L_{r,I}=\mathbb C1\), effect--odds functional calculus defines

$$
(S_r^{\mathrm{res}}f)(N)
=
\frac{(e^N\widehat L_{r,I})^{1/2}}
{1+e^N\widehat L_{r,I}}f,
\qquad
\widehat L_{r,I}=L_{r,I}/L_{*,r},
\tag{PC7c}
$$

with exact identity

$$
\int_{\mathbb R}\|S_r^{\mathrm{res}}f(N)\|^2\,\mathrm dN
=\|f\|^2
\tag{PC7d}
$$

on the constant complement. It is complex-linear, unitary-natural, and turns rescaling of \(L_{r,I}\) into translation of \(N\). Every spectral channel is a translated logistic half-density with \(\nu=1/2\) when \(N\) is the logarithm of the parameter multiplying \(L_{r,I}\).

This does not insert directly into (PC8). Its codomain uses log-Haar measure \(\mathrm dN\) and retains a spectral-value-dependent center, whereas \(\mathcal V^{\mathrm{sc}}_{\nu,N_c}\widehat\otimes\mathcal K_r\) is one fixed-center weighted probability carrier. Recentring every channel while discarding its center would erase precisely whether eigenvalues accumulate at zero. More decisively, the transform exists with the same logistic shape for every gapless positive operator. The \(1/4\) scale-shadow edge is therefore a universal profile constant, not a lower edge of \(L_{r,I}\). The remaining physical theorem is a uniform ceiling on the invariant center \(-\log\widehat L_{r,I}\), followed by the independent Casimir comparison. Equation (PC7c) narrows the open map; it does not prove (PC10).

At a stage where a Poincare carrier has been reconstructed, require the resulting complex-linear analysis map

$$
\mathcal J_r:
\operatorname{Dom}(\mathcal C_r^{1/2})
\longrightarrow
\mathcal V^{\mathrm{sc}}_{\nu_r,N_{c,r}}\widehat\otimes\mathcal K_r.
\tag{PC8}
$$

The map must obey \(\mathcal J_rP_{0,r}=0\), factor through the gauge quotient and OS null subspace, be natural under regional inclusions and RG comparison, and be constructed without the desired spectrum. Define

$$
\mathfrak d_r[\Psi]
:=
\int_{\mathbb R}
\left\|
\partial_N(\mathcal J_r\Psi)(N)
\right\|_{\mathcal K_r}^2
\,\mathrm d\mu_{\nu_r,N_{c,r}}(N).
$$

Suppose on the common Casimir/scale form domain that the dimensionless constants \(b\) and \(\eta\) can be chosen uniformly in volume and regulator, with

$$
\|\mathcal J_r\Psi\|^2
\geq
b\|(1-P_{0,r})\Psi\|^2,
\qquad
b>0,
\tag{PC9}
$$

and that an independently normalized same-carrier solder satisfies

$$
\|\mathcal C_r^{1/2}\Psi\|^2
\geq
\eta E_{*,r}^2\mathfrak d_r[\Psi],
\qquad
\eta>0.
\tag{PC10}
$$

Applying [[logistic-scale-geometry/pointing-coercivity-and-the-flat-partner-law#Exact scale-shadow gap|the sharp scale Poincare inequality (PC1)]] fiberwise gives the regulatorwise sandwich

$$
\boxed{
\|\mathcal C_r^{1/2}\Psi\|^2
\geq
\eta E_{*,r}^2\nu_r^2b
\|(1-P_{0,r})\Psi\|^2.}
\tag{PC11}
$$

Positive energy and the theorem in [[mass-scale-calibration/joint-causal-generators-and-the-mass-casimir|joint causal generators and the mass Casimir]] then imply

$$
\boxed{
H_r
\geq
E_{*,r}\nu_r\sqrt{\eta b}\,(1-P_{0,r}).}
\tag{PC12}
$$

This is an exact implication from the declared hypotheses: joint functional calculus gives \(H_r^2=\mathcal C_r+c^2\mathbf P_r^2\geq\mathcal C_r\), and positivity gives (PC12). Uniform positive mass in a limiting family additionally requires

$$
\inf_r E_{*,r}\nu_r>0
$$

or convergence of this product to a positive limit. Its irreducible open data are now the geometric selection and localization of \(L_{r,I}\), together with an information-preserving bridge from the resolvent transform's log-Haar carrier to the fixed wall carrier. Without those, the exact OS boundary carrier and the proposed wall carrier remain different mathematical objects.
Equivalently, if one permits regulator-dependent comparison constants rather than the uniform \(b,\eta\) assumed above, the single product condition that keeps this derived lower bound positive is \(\inf_r\eta_rb_r(E_{*,r}\nu_r)^2>0\).

If the projection-coded capacity/odds solder or the [[wall-construction-interface/scale-character-solder#A boundary law that selects the projection-branch value|nondegenerate incoming-density axiom]] is independently justified, then \(\nu_r=1/2\) and the same conditional theorem specializes to

$$
\boxed{
H_r
\geq
\frac{E_{*,r}}{2}\sqrt{\eta b}\,(1-P_{0,r}).}
\tag{PC12a}
$$

The coefficient \(1/2\) is then dimensionless and algebraically fixed under that proposed normalization; \(E_{*,r}\), \(\eta\), \(b\), and the carrier map remain separate obligations. The competing normalized-involution solder would instead put \(\nu_r=1\) in (PC12), so no numerical coefficient is canonical before this fork is resolved.

## Compatibility with local QFT

The scale coordinate must not be silently introduced as an observable scalar field. Compatibility requires the chain in [[measured-response-carriers/descent-loss-cocycle-and-recovery-fork#QFT compatibility belongs after the nonfaithful quotient|the QFT-recovery fork]]:

$$
\mathcal A_r^{\mathrm{pre}}
\xrightarrow{q_r}
\mathcal Q_r
\longrightarrow
\mathfrak B_r^{\mathrm E}
\xrightarrow{\mathrm{limit}}
\mathfrak B^{\mathrm E}_{\mathrm{YM}}
\xrightarrow{\mathrm{OS}}
\mathfrak A^{\mathrm{YM}}.
$$

The wall may forget vertical pre-observable distinctions, but (PC8) must act on retained physical directions. If the entire scale form lies in \(\ker q_r\), the recovery fork says it cannot charge an excitation in the observable image. If instead its degree of freedom survives as an additional local particle, ordinary pure Yang--Mills has not been recovered. The viable middle is a natural transformation that makes wall variation control the existing gauge-invariant energy form without adding an independent low-energy field.

Generalized Mosco convergence of the scaled forms, convergence of vacuum projections, reflection positivity, Euclidean-state convergence, and recovery of the local Poincare-covariant net are still required. A fixed scale-shadow gap alone proves none of them.
