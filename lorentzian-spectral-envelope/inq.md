---
inq.module: "lorentzian-spectral-envelope"
inq.include:
  - "**/*.md"
inq.ambient:
  - "**/*.py"
---
# Lorentzian Spectral Envelope

This module owns the causal-register reading of spectral data that [[cauchy-spectral-envelope/inq|the Cauchy envelope]] deliberately declined: the exact dictionary between a Cauchy line in energy, one-sided exponential decay in time, exponential clustering of a Euclidean measure, and a spectral gap of a Hamiltonian; the reflection-positivity wall as the constructor that turns statistical positivity into Hilbert positivity and yields a transfer operator whose contraction residue is, by definition, the gap; the modular route by which Lorentzian causal structure is recovered from state and algebra; and the de Sitter anchor at which the Hubble rate appears as a quantum of damping rather than a frequency. Everything here is an exact dictionary, a definition, or a standard theorem with its hypotheses named. The module does not construct a Lorentzian wall, prove any continuum gap, take the norm of a Dirac commutator, derive a unit conversion, or identify any pole with the causal grain; each of those is listed as open at the end.

The Cauchy module's terminology firewall stands unchanged: a Lorentzian *line shape* and a Lorentzian *signature* are unrelated meanings of one word, and no implication runs between them. Section 1 relates the line shape to a decay law in time — both in the line-shape register. Lorentzian signature enters only in section 3, through modular theory, and nowhere else.

## 1. Line shape and decay law

**[STANDARD]** Let an autocorrelation decay one-sidedly in time with rate \(\Gamma/2\) about a center \(E_*\):

$$
C(t)=e^{-\Gamma|t|/2}\,e^{-iE_*t}.
$$

Its spectral density is the Cauchy line

$$
\boxed{
\widehat S(\omega)=\int_{-\infty}^{\infty}C(t)e^{i\omega t}\,\mathrm dt
=\frac{\Gamma}{(\omega-E_*)^2+\Gamma^2/4},}
$$

with full width at half maximum exactly \(\Gamma\). **A Lorentzian in energy is one-sided exponential decay in time.** The receipt checks the pair numerically at five frequencies and verifies the half-maximum width.

**[STANDARD]** The Euclidean shadow is the gap dictionary. A Euclidean two-point function clustering as \(e^{-m|\tau|}\) has transform

$$
\boxed{\int e^{-m|\tau|}e^{i\omega\tau}\,\mathrm d\tau=\frac{2m}{\omega^2+m^2},}
$$

a pole at \(\omega=\pm im\); the receipt recovers the pole position from the numerical transform by fitting its reciprocal. Under Osterwalder–Schrader reconstruction the clustering rate of a Euclidean correlator is the mass of the lightest state the corresponding operator creates; it equals the spectral gap of the reconstructed Hamiltonian when that operator overlaps the lightest excitation, and otherwise gives the mass in that operator's channel. [[the-grain-of-causal-scale/causal-spectrum|The causal-spectrum note]] states the corresponding resonance form \(z_*=E_*-\tfrac i2\Gamma_*\); a mass gap is the case \(\Gamma_*=0\), a real isolated point strictly below the continuum, which is a different object from a resonance and must not be conflated with one.

## 2. The wall constructs the Hilbert space; the gap is the wall's contraction residue by definition

**[STANDARD]** Reflection positivity is a wall in the programme's sense. Let \(\theta\) reflect Euclidean time across a hyperplane and let \(\mathcal A_+\) be the algebra of functionals supported on one side. Osterwalder–Schrader positivity is

$$
\langle\theta F,F\rangle\ \ge\ 0\qquad(F\in\mathcal A_+),
$$

and the Hilbert space of the theory is \(\mathcal A_+\) modulo the null vectors of this form. Positivity of energy and the Hamiltonian are *constructed* by this one-sided pairing; they are not present in the Euclidean measure before the wall is chosen. On a lattice the construction is exact: the transfer operator \(T=e^{-aH}\) acts across one slice, it is positive by reflection positivity, and Osterwalder and Seiler proved reflection positivity for Wilson's lattice gauge action at every coupling (*Ann. Phys.* **110**, 440 (1978)), with a mass gap at strong coupling by cluster expansion.

**[DEFINITION]** In lattice energy units the gap is

$$
\boxed{ma=-\ln\frac{\lambda_1(T)}{\lambda_0(T)},}
$$

where \(\lambda_0\) is the vacuum eigenvalue and \(\lambda_1\) the next. This is not a finding; it is what the spectral gap of a transfer operator means. Its value for the programme is that it is *already typed* as the contraction residue of a positive non-invertible map across one slice — a descent across a wall — so the programme's conjecture "the residue of the descent is the gap" is, in this register, the definition rather than a discovery. **[RECEIPT]** The one-dimensional Ising transfer matrix is the complete debugging model: \(T=\begin{pmatrix}e^{K}&e^{-K}\\e^{-K}&e^{K}\end{pmatrix}\), \(\lambda_0=2\cosh K\), \(\lambda_1=2\sinh K\), \(\langle s_0s_n\rangle=(\lambda_1/\lambda_0)^n=(\tanh K)^n\), \(\xi^{-1}=-\ln\tanh K\). The receipt reproduces the two-point function by explicit contraction on a ring across a sweep of \(K\), and checks that the gap decreases monotonically in \(K\) and vanishes in the degenerate limit — the regime in which the check can fail.

**[PROPOSED COMPARISON]** The programme's descent grammar and the transfer grammar are the same species. [[spectral-wall-descent/conditional-expectation-balance|The conditional-expectation balance]] proves the entropic shadow, \(\Sigma_E(\rho)=S(\bar\rho)-S(\rho)\ge0\), a nonnegative cost of one non-invertible step. The transfer operator is likewise a positive non-invertible map across one slice, and its strict contraction on the complement of the vacuum is the gap. The comparison is proposed, not identified: the theorem carrying a given wall's expectation to a given theory's transfer operator is not in the vault, and without it "residue of descent" and "mass gap" are two instances of one grammar.

**[EXACT]** Before any wall there is no gap. [[the-grain-of-causal-scale/causal-spectrum|The pre-wall no-gap theorem]] shows that dilation covariance of a half-sided modular inclusion forces \(\sigma(P)=\{0\}\) or \(\sigma(P)=[0,\infty)\), with no nonzero point spectrum. A gap therefore requires that the wall break the dilation orbit — a box, a corner, a reflection hyperplane, a matter correlation. **[STANDARD]** Classical Yang–Mills in four dimensions is exactly dilation covariant, and the quantum theory's *scale* is the failure of that covariance to survive quantization — the trace anomaly. A scale is not yet a gap: QCD with massless quarks transmutes a scale and has massless pions, and a theory flowing to an infrared fixed point has a scale in its flow and no gap. The exact statement is only that without the broken covariance neither is available.

**[OPEN — NOT OWNED HERE]** What remains, for any interacting four-dimensional theory, is that the residue \(1-\lambda_1/\lambda_0\) stay bounded away from zero in physical units as the lattice spacing is removed. That sentence is the content of the Yang–Mills existence-and-mass-gap problem; [[contemporary-puzzles/yang-mills-mass-gap/inq|the puzzle module]] states it in full.

## 3. Lorentzian causal structure from modular data

The programme has asked for the algebraic meaning of \(c\). In the Riemannian register the answer is Connes' distance formula, \(d(x,y)=\sup\{|a(x)-a(y)|:\lVert[D,a]\rVert\le1\}\), in which the commutator bound is the unit-Lipschitz condition and the metric is a supremum over the algebra; the vault has never taken that norm, and the construction is recorded below as open. In the Lorentzian register two theorems recover the *causal structure and its symmetry group* from modular data. Neither recovers a unit conversion: they return the group of boosts, not the number \(c\).

**[STANDARD]** Bisognano–Wichmann (*J. Math. Phys.* **16**, 985 (1975); **17**, 303 (1976)): for a Wightman theory, the modular group of the vacuum restricted to a wedge algebra is the one-parameter group of boosts preserving that wedge, \(\Delta^{it}=U(\Lambda_W(-2\pi t))\), and the modular conjugation is the CPT operator composed with a rotation. The boost generator — the Lorentz symmetry that fixes the light cone — is modular data of the vacuum state.

**[STANDARD — with the source's conditions]** The condition of geometric modular action (Buchholz, Dreyer, Florig, Summers, *Rev. Math. Phys.* **12**, 475 (2000)), held and graded THEOREM in [[inbox/radical-copernicanism/algebra-of-causality|the algebra-of-causality survey]], reconstructs the spacetime symmetry group and the causal structure from the modular conjugations of a family of algebras and a state, under additional conditions stated in the source and carried out there for four-dimensional Minkowski and three-dimensional de Sitter space. Together with Bisognano–Wichmann it is the sense in which causal order is encoded in state plus algebra rather than supplied as background.

**[STANDARD — lattice]** On a lattice the analogous object is a Lieb–Robinson bound (*Commun. Math. Phys.* **28**, 251 (1972)): for bounded local Hamiltonians, \(\lVert[A(t),B]\rVert\le C\,\lVert A\rVert\,\lVert B\rVert\,e^{-(d(A,B)-v|t|)/\xi}\), a commutator norm bounding causality with an emergent velocity \(v\). It is the lattice sibling of the Lipschitz bound in Connes' formula and the only register in which Yang–Mills is presently constructed. Its extension to gauge links with unbounded electric terms requires care and is not asserted here.

## 4. The de Sitter anchor

**[STANDARD — cited]** In the static patch of de Sitter space a scalar field of conformal weight \(\Delta_\pm\) has quasinormal frequencies

$$
\omega_{n,\ell}=-i\,(\Delta_\pm+\ell+2n)\,H,\qquad n,\ell\in\mathbb Z_{\ge0},
$$

purely imaginary, with the overtone tower stepping by \(2H\), the angular tower by \(H\), and a generically non-integer offset \(\Delta_\pm H\) (López-Ortega, *Gen. Relativ. Gravit.* **38**, 1565 (2006)). There is no real part: **\(H\) is a quantum of damping, not a quantum of energy.** These are resonances of the analytically continued resolvent of an open system leaking through its horizon, not eigenvalues of a self-adjoint operator, and the pre-wall no-gap theorem — a statement about a positive translation generator — is not the reason for them. What the anchor supplies is a home for [[the-grain-of-causal-scale/causal-spectrum|the causal-spectrum note]]'s definition \(\Gamma_c:=\hbar H_c\): the fundamental de Sitter width is \(\hbar H\), exactly as the Pöschl–Teller receipt there returns \(\Gamma_0=\hbar\kappa\) when \(\kappa=H_c\). The firewall recorded in that note stands: \(\Gamma_c\) is a dimensional definition until one constructed operator makes \(H_c\) its decay rate, and the enormous quality factor \(Q_c=E_*/\Gamma_c\sim10^{40}\) is not supplied by any damping spectrum — a damping quantum sets widths, never a line center.

## 5. Nuclearity as a ledger of the gap

**[STANDARD]** Buchholz–Wichmann nuclearity (*Commun. Math. Phys.* **106**, 321 (1986)) asks that the maps \(A\mapsto e^{-\beta H}A\Omega\) from a local algebra's unit ball be nuclear, with a nuclearity index bounding the local phase-space density. A mass gap improves these bounds by factors of order \(e^{-\beta m}\); nuclearity implies the split property (Buchholz, D'Antoni, Longo, *Commun. Math. Phys.* **129**, 115 (1990)); and the split property supplies, for a standard split inclusion \(\mathcal N\subset\mathcal M\), a canonical intermediate type-I factor and a canonical conditional expectation through the Doplicher–Longo standard split isomorphism (*Invent. Math.* **75**, 493 (1984)). The chain runs

$$
\text{gap}\ \Longrightarrow\ \text{nuclearity bounds}\ \Longrightarrow\ \text{split}\ \Longrightarrow\ \text{canonical type-I corner and expectation}.
$$

**[PROPOSED COMPARISON]** The last object is the same species as [[spectral-wall-descent/finite-index-area-weld|the type-I product cell]] of the programme, arriving from the field-theory side — but not the same object: the split-property interpolating factor sits in a generically infinite-index inclusion of type-III₁ factors, whereas the weld note's exact identity is a finite-index construction with a recorded type obstruction against finite index out of type III. The nuclearity index is a capacity of an inclusion with a state — a ledger quantity in the programme's vocabulary — controlled by the gap.

**[OPEN]** The arrows run from the gap to the structure. The converse — a capacity condition on a wall that implies a gap — is not a theorem, and it is the correctly typed form of the programme's conjecture that the algebra of descent requires a nonzero residue. Modular nuclearity in the sense of Lechner (*Commun. Math. Phys.* **277**, 821 (2008)) is the one operator-algebraic route that has actually produced interacting models with a gap, in two dimensions, with the gap as input; [[library/deformations-of-half-sided-modular-inclusions-and-non-local-chiral-field-theories/inq|the half-sided-inclusion deformations]] held in the library are that school's construction technique.

## Claim ledger

| Status | Content |
|---|---|
| Standard | the line-shape–decay Fourier pair and its half-width; the clustering–pole dictionary under OS reconstruction, with the channel-overlap hypothesis; reflection positivity for Wilson lattice gauge theory and the strong-coupling gap; the trace anomaly as the source of the Yang–Mills scale; Bisognano–Wichmann; the condition of geometric modular action under its source's conditions; Lieb–Robinson for bounded local Hamiltonians; the de Sitter quasinormal spectrum; nuclearity, split, and the standard split isomorphism |
| Definition | the transfer-operator gap \(ma=-\ln(\lambda_1/\lambda_0)\) as the contraction residue across the wall |
| Receipt | the Ising debugging model across a \(K\)-sweep with its degenerate limit; the pole position recovered from the numerical transform |
| Exact | the pre-wall no-gap theorem imported from [[the-grain-of-causal-scale/causal-spectrum\|the causal-spectrum note]] |
| Proposed comparison | transfer operator and wall expectation as one descent grammar; the split-property type-I corner and the programme's type-I product cell as one species |
| Open construction | a Lorentzian realization of the core pre-wall; the norm \(\lVert[D,a]\rVert\) and the Connes distance in this vault; any operator whose decay rate is \(H_c\); Lieb–Robinson for unbounded gauge links |
| Open, not owned | uniform continuum persistence of the transfer residue for four-dimensional Yang–Mills |
| Failure condition | a constructed wall whose transfer operator is not a strict contraction on the vacuum complement has no gap regardless of its index or entropy; a claimed causal line at a real frequency inside a dilation-covariant positive generator contradicts the exact row |

## What this module does not do

It does not build a Lorentzian spectral triple, and the Krein-space template in [[library/algebraic-backgrounds/inq|algebraic backgrounds]] is not imported past its abstract. It does not identify the Ising or any finite transfer matrix with a physical wall. It does not derive \(c\), \(\hbar\), or a mass from modular data; Bisognano–Wichmann and geometric modular action recover a *group*, not a unit conversion. It does not let the de Sitter damping quantum become a line center. It does not turn a scale into a gap. And it does not prove that any interacting four-dimensional theory has a gap: it types where such a gap would have to live and what would have to contract.

## Receipt

[[lorentzian-spectral-envelope/receipts/verify_lorentzian_envelope.py|The receipt]] checks the Fourier pair at five frequencies and its half-maximum width; recovers the clustering pole \(\omega=\pm im\) by fitting the reciprocal of the numerical transform; reproduces the Ising ring two-point function against \((\tanh K)^n\) with the finite-ring correction for \(K\in\{0.2,0.8,2.0,5.0\}\), and checks that the gap decreases monotonically and vanishes as \(K\to\infty\); and records the mismatch between the pure-gauge gap length \(\hbar c/m_{0^{++}}\approx0.11\)–\(0.12\,\mathrm{fm}\) and the causal grain \(\lambda_*\approx4.18\)–\(4.26\,\mathrm{fm}\), a factor of \(35\)–\(37\). Standard library only; nonzero exit on any failure; output stored beside it.
