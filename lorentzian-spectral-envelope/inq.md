---
inq.module: "lorentzian-spectral-envelope"
inq.include:
  - "**/*.md"
inq.ambient:
  - "**/*.py"
---
# Lorentzian Spectral Envelope

This module owns the causal-register reading of spectral data that [[cauchy-spectral-envelope/inq|the Cauchy envelope]] deliberately declined: the exact Fourier dictionaries relating a Cauchy line to two-sided exponential correlation and Euclidean clustering to spectral support; the Osterwalder--Schrader reflection construction of a Hilbert carrier from Euclidean data; the transfer semigroup that reads a gap once that carrier and its dynamics exist; modular precedents for recovering causal structure from algebras and states; and the de Sitter damping scale. The strict dictionaries, standard reconstruction results, and proposed programme comparisons are kept separate. The module does not prove that a wall causes a gap, identify a transfer operator with a conditional expectation, construct a Lorentzian wall, prove a continuum gap, derive a unit conversion, or identify any pole with the causal grain.

The Cauchy module's terminology firewall stands unchanged: a Lorentzian *line shape* and a Lorentzian *signature* are unrelated meanings of one word, and no implication runs between them. Section 1 relates the line shape to a decay law in time — both in the line-shape register. Lorentzian signature enters only in section 3, through modular theory, and nowhere else.

## 1. Line shape and decay law

**[STANDARD]** In units \(\hbar=1\), let a stationary autocorrelation decay symmetrically away from \(t=0\), with rate \(\Gamma/2\) about a center \(E_*\):

$$
C(t)=e^{-\Gamma|t|/2}\,e^{-iE_*t}.
$$

Its spectral density is the Cauchy line

$$
\boxed{
\widehat S(\omega)=\int_{-\infty}^{\infty}C(t)e^{i\omega t}\,\mathrm dt
=\frac{\Gamma}{(\omega-E_*)^2+\Gamma^2/4},}
$$

with full width at half maximum exactly \(\Gamma\). **A Cauchy line is the Fourier transform of a two-sided exponential correlation in \(\lvert t\rvert\).** With the standard retarded Green-function convention, the causal amplitude is

$$
G_R(t)=-i\,\Theta(t)e^{-(\Gamma/2+iE_*)t}
$$

instead has the complex transform

$$
\widehat G_R(\omega)=\frac{1}{\omega-E_*+i\Gamma/2},
$$

so both \(\lvert\widehat G_R\rvert^2\) and the spectral function \(-2\operatorname{Im}\widehat G_R\) have the Lorentzian denominator, with the latter equal to the displayed Cauchy line. The receipt checks the two-sided Fourier pair at five frequencies and verifies the half-maximum width; it does not conflate that pair with the retarded transform.

**[STANDARD]** The exact model correlator \(C(\tau)=e^{-m|\tau|}\) has transform

$$
\boxed{\int e^{-m|\tau|}e^{i\omega\tau}\,\mathrm d\tau=\frac{2m}{\omega^2+m^2},}
$$

a pole at \(\omega=\pm im\); the receipt recovers the pole position from the numerical transform by fitting its reciprocal. Under Osterwalder--Schrader reconstruction, a general operator channel instead has a positive spectral measure

$$
C_O(\tau)=\int_{[0,\infty)}e^{-E|\tau|}\,\mathrm d\mu_O(E).
$$

Its leading exponential rate is the infimum of the non-vacuum support of \(\mu_O\). It equals the global Hamiltonian gap only when that channel reaches the lightest excitation; a continuum threshold can also add a power-law prefactor. The special function \(e^{-m|\tau|}\) corresponds to a spectral atom, so its isolated poles are more information than the bare existence of a gap.

The invariant mass-gap statement is

$$
\boxed{E_H((0,\Delta))=0\quad\text{for some }\Delta>0,}
$$

where \(E_H\) is the spectral measure of the reconstructed Hamiltonian and the vacuum lies at zero. The spectrum may begin continuously at \(\Delta\). By contrast, [[the-grain-of-causal-scale/causal-spectrum|the causal-spectrum note]]'s resonance form \(z_*=E_*-\tfrac i2\Gamma_*\) has \(\Gamma_*=0\) for a stable pole. A vacuum gap, a stable one-particle pole, and a resonance are three distinct spectral statements.

## 2. The OS quotient constructs the carrier; the transfer semigroup reads the gap

**[STANDARD]** Let \(\theta\) reflect Euclidean time across a hyperplane and let \(\mathcal A_+\) be the algebra of functionals supported on one side. Osterwalder--Schrader positivity is

$$
\langle\theta F,F\rangle\ \ge\ 0\qquad(F\in\mathcal A_+),
$$

and the associated pre-Hilbert space is \(\mathcal A_+\) modulo the null vectors of this form; completing that quotient gives the Hilbert carrier. Together with the other Osterwalder--Schrader hypotheses, the one-sided pairing reconstructs a positive-energy Hilbert theory; reflection positivity alone is not the whole reconstruction theorem. Calling the reflection hyperplane a programme “wall” is a proposed comparison, not part of the standard theorem. On a lattice the construction is exact: a positive transfer operator \(T_a\) acts across physical Euclidean slice length \(a\); after division by its vacuum eigenvalue, its logarithmic generator is conventionally written \(\widetilde T_a=e^{-aH_0/(\hbar c)}\), where \(H_0\) is a vacuum-normalized energy and lattice conventions often set \(\hbar=c=1\). Osterwalder and Seiler proved reflection positivity for Wilson's lattice gauge action at every coupling (*Ann. Phys.* **110**, 440 (1978)). The rigorous gap supplied by the accompanying strong-coupling analysis is restricted to that regime; reflection positivity by itself does not imply a gap.

[[positive-kernels-and-reflection-positivity|Positive kernels and reflection positivity]] gives a decisive type check: the stationary sech-squared kernel has a positive Fourier transform but a negative reflected two-point determinant. Its legitimate density and Witten-operator roles survive; they do not certify an OS two-point function.

**[DEFINITION]** Let \(P_0\) be the vacuum projection and normalize the transfer operator by its vacuum eigenvalue,

$$
\widetilde T_a:=\lambda_0(T_a)^{-1}T_a,
\qquad
r_a:=\left\|\widetilde T_a(1-P_0)\right\|.
$$

The general transfer-semigroup form of the gap is

$$
\boxed{\Delta_{E,a}=-\frac{\hbar c}{a}\ln r_a.}
$$

In finite spatial volume, when a next eigenvalue exists, this reduces to

$$
\boxed{\frac{a\Delta_{E,a}}{\hbar c}=-\ln\frac{\lambda_1(T_a)}{\lambda_0(T_a)}.}
$$

Thus \(r_a<1\) is the strict contraction equivalent of a gap after the Hilbert carrier and time-translation semigroup have been constructed. It is not by itself a non-invertible descent. **[RECEIPT]** The one-dimensional Ising transfer matrix is the complete debugging model: \(T=\begin{pmatrix}e^{K}&e^{-K}\\e^{-K}&e^{K}\end{pmatrix}\), \(\lambda_0=2\cosh K\), \(\lambda_1=2\sinh K\), and in the infinite-chain limit \(\langle s_0s_n\rangle=(\lambda_1/\lambda_0)^n=(\tanh K)^n\), with \(\xi^{-1}=-\ln\tanh K\). For every tested \(K>0\), \(\det T=2\sinh(2K)>0\): the matrix is invertible even though its normalized vacuum complement contracts. The receipt checks this distinction, reproduces the finite-ring two-point function with its correction term, and samples the analytic approach of the gap toward zero through \(K=5\).

**[EXACT -- MARKOV--OS SPECIALIZATION]** [[contemporary-puzzles/yang-mills-mass-gap/past-future-angle-and-the-transfer-gap|The separated past--future theorem]] reconstructs the same \(r_\ell\) from relative subspace geometry. For a stationary reversible Hilbert-positive Markov path space, conditional expectations onto disjoint half-spaces separated by \(\ell>0\) have

$$
c_F(\ell)
=
\left\|e^{-\ell H_0/(\hbar c)}(1-P_0)\right\|,
$$

and, writing \(J_+^0\) for the centered endpoint isometry and \(q p q\) for the history-carrier positive return,

$$
(J_+^0)^*(qpq)J_+^0
=
e^{-2\ell H_0/(\hbar c)}(1-P_0).
$$

Touching halves share the whole time-zero carrier and do not have this reduced-angle interpretation. [[contemporary-puzzles/yang-mills-mass-gap/phase-modulus-pointing-and-euclidean-dwell|The phase--modulus note]] then gives

$$
\int_0^\infty e^{-2\ell H_0/(\hbar c)}(1-P_0)\,\mathrm d\ell
=
\frac{\hbar c}{2}H_0^{-1}
$$

on the vacuum complement, with \(H_0^{-1}\) understood there. Thus a gap is exactly a finite uniform Euclidean-persistence ceiling after the transfer carrier exists. Neither theorem constructs that carrier or proves its contraction from four-dimensional Yang--Mills.

**[PROPOSED COMPARISON]** Three arrows must remain distinct. The Osterwalder--Schrader quotient \(q:\mathcal A_+\to\mathcal H_{\mathrm{OS}}\) can have a kernel and constructs the carrier. [[spectral-wall-descent/conditional-expectation-balance|The conditional-expectation balance]] uses an idempotent completely positive algebra map and proves the entropic cost \(\Sigma_E(\rho)=S(\bar\rho)-S(\rho)\ge0\). The transfer operator \(e^{-aH_0/(\hbar c)}\) is instead an injective Hilbert-space semigroup operator; in finite dimension it is invertible. This is the same injective-smoothing versus quotient-like-forgetting distinction enforced by [[cauchy-spectral-envelope/inq#Descent and factivity: smoothing is not forgetting|the Cauchy envelope]]. A programme wall may eventually induce all three, but identifying its expectation with its transfer dynamics requires an explicit carrier map or intertwiner. Without that construction, "descent cost" and "spectral contraction" are only a proposed comparison.

**[EXACT -- HSMI SCOPE]** [[the-grain-of-causal-scale/causal-spectrum|The HSMI no-gap theorem]] shows that the particular positive translation generator \(P\) of a dilation-covariant half-sided modular inclusion has \(\sigma(P)=\{0\}\) or \(\sigma(P)=[0,\infty)\), with no nonzero point spectrum. This forbids locating an isolated gap in that generator while its exact modular scaling law remains unbroken. It does not show that every object called "pre-wall" is gapless, and an Osterwalder--Schrader reflection plane can occur in both massive and massless theories without itself breaking dilation covariance. **[STANDARD]** Classical Yang--Mills in four dimensions is dilation covariant, while the quantum scale enters through the trace anomaly. A scale is not yet a gap: in the expected chirally broken phase of massless-quark QCD, the pions are Goldstone modes, and a theory flowing to an infrared fixed point can likewise remain gapless.

**[OPEN -- NOT OWNED HERE]** For a regulator family \(T_{a,L}\), the required estimate is a positive lower bound on

$$
\Delta_{E,a,L}=-\frac{\hbar c}{a}\ln\left\|\widetilde T_{a,L}(1-P_{0,a,L})\right\|
$$

that is uniform through the infinite-volume limit and remains positive in fixed physical units along the tuned continuum trajectory. For a fixed physical gap, the raw per-slice residue satisfies \(1-r_a\sim a\Delta_E/(\hbar c)\to0\); it must *not* stay bounded away from zero. Constructing the nontrivial local Poincaré-covariant limit is the other inseparable part of the Yang--Mills problem; [[contemporary-puzzles/yang-mills-mass-gap/inq|the puzzle module]] states it in full.

## 3. Lorentzian causal structure from modular data

The programme has asked for the algebraic meaning of \(c\). In the Riemannian register the answer is Connes' distance formula, \(d(x,y)=\sup\{|a(x)-a(y)|:\lVert[D,a]\rVert\le1\}\), in which the commutator bound is the unit-Lipschitz condition and the metric is a supremum over the algebra; the vault has never taken that norm, and the construction is recorded below as open. In the Lorentzian register two theorems recover the *causal structure and its symmetry group* from modular data. Neither recovers a unit conversion: they return the group of boosts, not the number \(c\).

**[STANDARD]** Bisognano–Wichmann (*J. Math. Phys.* **16**, 985 (1975); **17**, 303 (1976)): for a Wightman theory, the modular group of the vacuum restricted to a wedge algebra is the one-parameter group of boosts preserving that wedge, \(\Delta^{it}=U(\Lambda_W(-2\pi t))\), and the modular conjugation is the CPT operator composed with a rotation. The boost generator — the Lorentz symmetry that fixes the light cone — is modular data of the vacuum state.

**[STANDARD — with the source's conditions]** The condition of geometric modular action ([Buchholz, Dreyer, Florig, Summers](https://arxiv.org/abs/math-ph/9805026), *Rev. Math. Phys.* **12**, 475 (2000)), held and graded THEOREM in the local raw survey at inbox/radical-copernicanism/algebra-of-causality.md, reconstructs the spacetime symmetry group and the causal structure from the modular conjugations of a family of algebras and a state, under additional conditions stated in the source and carried out there for four-dimensional Minkowski and three-dimensional de Sitter space. Together with Bisognano–Wichmann it is the sense in which causal order is encoded in state plus algebra rather than supplied as background.

**[STANDARD — lattice]** On a lattice the analogous object is a Lieb–Robinson bound (*Commun. Math. Phys.* **28**, 251 (1972)): for bounded local Hamiltonians, \(\lVert[A(t),B]\rVert\le C\,\lVert A\rVert\,\lVert B\rVert\,e^{-(d(A,B)-v|t|)/\xi}\), a commutator norm bounding causality with an emergent velocity \(v\). It is the lattice sibling of the Lipschitz bound in Connes' formula and belongs to the fixed-cutoff setting where gauge theory is mathematically defined nonperturbatively. Its extension to gauge links with unbounded electric terms requires care and is not asserted here.

## 4. The de Sitter anchor

**[STANDARD -- cited, with a weight qualification]** In the static patch of de Sitter space a scalar field of conformal weight \(\Delta_\pm\) has quasinormal frequencies

$$
\omega_{n,\ell}=-i\,(\Delta_\pm+\ell+2n)\,H,\qquad n,\ell\in\mathbb Z_{\ge0},
$$

with the overtone label stepping by \(2H\) and the angular label by \(H\) (López-Ortega, *Gen. Relativ. Gravit.* **38**, 1565 (2006)). They are purely imaginary only when \(\Delta_\pm\) is real. In \(D\)-dimensional de Sitter space, a principal-series weight \(\Delta_\pm=(D-1)/2\pm i\mu\) instead gives a real part \(\pm\mu H\). These are resonances of an analytically continued open-system problem, not eigenvalues of a self-adjoint Hamiltonian, and the HSMI no-gap theorem is not their explanation.

Under this module's convention \(z=E-i\Gamma/2=\hbar\omega\), the full linewidth is

$$
\boxed{\Gamma=-2\hbar\,\operatorname{Im}\omega.}
$$

Thus \(\hbar H\) is a natural *damping-energy scale*, not generically the linewidth of the fundamental mode and not by itself a line center. The Pöschl--Teller receipt in [[the-grain-of-causal-scale/causal-spectrum|the causal-spectrum note]] gives \(\Gamma_0=\hbar\kappa\) because its fundamental pole has \(\operatorname{Im}\omega_0=-\kappa/2\); that factor is model-specific. The definition \(\Gamma_c:=\hbar H_c\) remains a dimensional address until a constructed pole satisfies \(-2\operatorname{Im}\omega=H_c\). The enormous \(Q_c=E_*/\Gamma_c\sim10^{40}\) is not supplied by the de Sitter tower.

## 5. Nuclearity as an independent phase-space ledger

**[STANDARD]** Buchholz--Wichmann nuclearity (*Commun. Math. Phys.* **106**, 321 (1986)) asks that the maps \(A\mapsto e^{-\beta H}A\Omega\) from a local algebra's unit ball be nuclear, with a nuclearity index bounding the density of localized states. This is an additional phase-space condition, not a consequence of a mass gap: a gapped theory can have excessive species growth, and standard massless free fields can satisfy nuclearity. When a suitable nuclearity estimate is already available, a gap can improve its low-temperature behavior by factors of order \(e^{-\beta m}\). Nuclearity implies the split property under the standard hypotheses (Buchholz, D'Antoni, Longo, *Commun. Math. Phys.* **129**, 115 (1990)); a standard split inclusion then has a canonical intermediate type-I factor through the Doplicher--Longo standard split isomorphism (*Invent. Math.* **75**, 493 (1984)). The unconditional implication used here is

$$
\text{nuclearity}\ \Longrightarrow\ \text{split}\ \Longrightarrow\ \text{canonical type-I corner}.
$$

**[PROPOSED COMPARISON]** The last object is the same broad type-I interpolation pattern as [[spectral-wall-descent/finite-index-area-weld|the type-I product cell]] of the programme, but not the same object: the split-property interpolating factor sits in a generically infinite-index inclusion of type-III₁ factors, whereas the weld note's exact identity is finite-index and already records the type obstruction against finite index out of type III. The nuclearity index is a capacity of an inclusion with a state, but it controls high-energy phase-space growth rather than serving as a synonym for an infrared gap.

**[OPEN]** A wall-capacity condition that implies an infrared spectral gap would need information stronger than ordinary nuclearity, since nuclearity is compatible with massless theories. No such capacity-to-gap theorem is present in the vault. Modular nuclearity in the sense of Lechner (*Commun. Math. Phys.* **277**, 821 (2008)) has helped construct interacting two-dimensional models when suitable scattering and mass data are supplied; [[library/deformations-of-half-sided-modular-inclusions-and-non-local-chiral-field-theories/inq|the half-sided-inclusion deformations]] held in the library are part of that construction school.

## Claim ledger

| Status | Content |
|---|---|
| Standard | the two-sided correlation--Cauchy Fourier pair; the retarded resolvent with the same denominator; the clustering--spectral-support dictionary under OS reconstruction; reflection positivity for Wilson lattice gauge theory and the strong-coupling gap in its proved regime; the trace anomaly as the source of the Yang--Mills scale; Bisognano--Wichmann; geometric modular action under its source's conditions; Lieb--Robinson for bounded local Hamiltonians; the qualified de Sitter quasinormal spectrum; nuclearity and split under their own hypotheses |
| Definition | the Hamiltonian energy gap \(E_H((0,\Delta_E))=0\); equivalently \(\Delta_{E,a}=-(\hbar c/a)\ln\lVert\widetilde T_a(1-P_0)\rVert\), with the eigenvalue ratio only in discrete finite-volume settings |
| Receipt | the Fourier pair and pole fit; the invertible Ising transfer matrix whose normalized vacuum complement contracts; the sampled closing-gap trend |
| Exact, Markov--OS specialization | disjoint past/future expectation projections have Friedrichs cosine equal to the vacuum-reduced transfer norm across their slab; their supported positive return recovers the transfer generator, and finite uniform Euclidean dwell is equivalent to a positive gap |
| Exact, scoped | the no-gap theorem for the positive generator of a dilation-covariant half-sided modular inclusion, imported from [[the-grain-of-causal-scale/causal-spectrum|the causal-spectrum note]] |
| Proposed comparison | an explicit wall realization may relate the OS quotient, a conditional expectation, and transfer dynamics; the split-property type-I corner and the programme's type-I product cell share an interpolation pattern |
| Open construction | a Lorentzian realization of the core pre-wall; an intertwiner from wall dynamics to a physical transfer semigroup; the norm \(\lVert[D,a]\rVert\) and the Connes distance in this vault; any operator whose damping convention realizes \(\Gamma_c=\hbar H_c\); Lieb--Robinson for unbounded gauge links |
| Open, not owned | a nontrivial four-dimensional continuum Yang--Mills theory with a positive infinite-volume gap in fixed physical units |
| Failure condition | a constructed transfer semigroup with norm one on the vacuum complement has no gap regardless of wall index or entropy; identifying injective attenuation with quotient-like forgetting contradicts [[cauchy-spectral-envelope/inq|the Cauchy envelope]]; a claimed isolated line in the HSMI generator contradicts the scoped exact row |

## What this module does not do

It does not build a Lorentzian spectral triple, and the Krein-space template in [[library/algebraic-backgrounds/inq|algebraic backgrounds]] is not imported past its abstract. It does not identify the Ising model with a physical wall, make the reflection plane cause a gap, or identify an injective transfer semigroup with a conditional expectation. It does not derive \(c\), \(\hbar\), or a mass from modular data; Bisognano--Wichmann and geometric modular action recover a *group*, not a unit conversion. It does not let a de Sitter damping scale become a line center, turn a scale into a gap, or prove that any interacting four-dimensional theory has a gap.

## Receipt

[[lorentzian-spectral-envelope/receipts/verify_lorentzian_envelope.py|The receipt]] checks the two-sided Fourier pair at five frequencies and its half-maximum width; recovers the model-correlator pole \(\omega=\pm im\) by fitting the reciprocal of the numerical transform; verifies that the finite Ising transfer matrix is invertible while its normalized vacuum complement contracts; reproduces the ring two-point function against \((\tanh K)^n\) with the finite-ring correction for \(K\in\{0.2,0.8,2.0,5.0\}\); checks the sampled approach of the gap toward zero; and records the mismatch between the pure-gauge correlation length and the causal grain. Standard library only; nonzero exit on any failure; output stored beside it.
