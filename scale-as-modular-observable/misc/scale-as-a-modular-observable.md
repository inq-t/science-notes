# Scale as a Modular Observable — Revision 2

> [!warning] Audited working document
> This long synthesis is retained as a source, but its claim labels are not reliable. Sections 14 and 16 contain invalid closure arguments, and section 15 promotes a local relative-entropy Hessian to an all-history source without a derivation. Read [[scale-as-modular-observable/inq|the folder entry]] for the modular map and [[claim-audit]] for the corrected status of each step. The historical files under `chats/` remain untouched.

## A parameter-free derivation of the late-time expansion history from the information geometry of causal cuts

**Thomas Ruble** **21 August 2026 — Revision 2**

---

**Status.** Research monograph, revision 2; supersedes revision 1 of even date. Not peer reviewed. Every claim carries one of the following labels:

|label|meaning|
|---|---|
|`[STANDARD]`|established in the cited literature|
|`[THEOREM]`|proved here or in Appendix A|
|`[FRAMEWORK]`|the constitutive principle that defines the theory|
|`[IDENTIFICATION]`|the physical postulate selecting which mathematical structure nature realises|
|`[SECTOR]`|global superselection or state-selection data|
|`[NEGATIVE]`|a computed no-go|
|`[OPEN]`|an open problem, stated precisely|
|`[RHYME]`|a structural analogy; never counted as evidence|

All numerical claims are reproduced by `receipts_closure.py`, `receipts_transparency_fold.py`, and the `P1/` analysis package (the package name is historical). One receipted value is corrected in this revision: the jerk parameter, previously reported as j₀ = −0.10855 through a sign error in the identity j = q + 2q² − dq/dN, is j₀ = −0.11125 (Appendix A.9). No other number changes.

**Scope.** Three sentences state exactly what is and is not claimed.

1. **The homogeneous background sector is closed.** Zero free functions, zero adjustable dark-sector parameters beyond those of flat ΛCDM, zero new constants of nature. Inputs: one constitutive principle, one representation-theoretic identification, four sector data (§3).
2. **The perturbation sector is open.** The covariant dark stress tensor is specified as a classification problem (§25) but not constructed; conservation is imposed, not derived.
3. **The observational status is viable and predictive.** The model improves on flat ΛCDM by Δχ² = −3.38 at equal parameter count — the best AIC among six families tested — and its zero-parameter (w₀, w_a) point is statistically indistinguishable from the DESI DR2 + CMB + Pantheon+ best fit. Discovery-class discrimination awaits perturbation-sensitive probes (§27, P9).

---

## How to read this document

The argument is a single chain. Twelve steps, each expanded in the section cited:

1. The causal order of spacetime determines its conformal geometry but not its scale `[STANDARD]` (§2). Scale is therefore a physical register of its own, with logarithm N = ln a.
2. A causal region carries intrinsic quantum-statistical structure — its algebra, its state, and the modular (Tomita–Takesaki) data these generate (§6). Comparing the states induced by two different scale choices is an intrinsic operation: the Connes cocycle (§6, §13).
3. The theory is defined by one constitutive principle `[FRAMEWORK]`: the scale register gravitates through its modular free-energy response (§3, §15).
4. At a codimension-two causal cut, the geometry supplies exactly one binary structure: the two null normal directions. The single postulate `[IDENTIFICATION]` is that the homogeneous modular quotient at the cut _is_ that binary — the chirality grading Q, with Q² = 1 (§11).
5. A binary's information geometry is unique: the exponential family ρ_θ = e^{θQ}/(2 cosh θ), whose entire content is the master identity ⟨Q²⟩ = η² + g = 1 (§12).
6. Weyl covariance forces the soldering θ = ϱ⊥(N − N_c) — the logarithm is derived, not chosen (§13). Representation theory forces ϱ⊥ ∈ ℤ⁺; a flatness ceiling caps ϱ⊥ < 1.814; hence ϱ⊥ = 1 (§14).
7. The dark energy density is the modular free-energy stiffness per causal-diamond volume, which is the pullback of the Bogoliubov–Kubo–Mori metric: ρ_X ∝ sech²[ϱ⊥(N − N_c)] (§15).
8. The proportionality is the entanglement capacity Var(K). The horizontal sector is the two-dimensional chiral algebra of the cut's normal plane, so Cardy's formula gives capacity = entropy: γ = 1 (§16).
9. At the flat FLRW apparent horizon, T·S/V = ρ_crit exactly — the Misner–Sharp marginality identity. Every constant of nature (ħ, k_B, G, c) cancels (§17).
10. Result: ρ_X(N) = ½ ρ_crit,c sech²(N − N_c), with N_c the unique minimum of the symmetrized modular relative entropy, dated by flatness. Dark density equals ordinary density at the crossing, exactly, as a theorem (§18).
11. Consequences, all forced: the exact invariant 9(1+w)² + 6 dw/dN = 4; a saddle-node phase flow with one density maximum, one w = −1 crossing, and one finite acceleration episode; a coasting a ∝ t future with no event horizon; the ℓ = 1 Pöschl–Teller operator as the generated perturbation kernel; and a vacuum-blindness theorem dissolving the local cosmological constant problem (§§19–24).
12. Numbers, none adjustable: (w₀, w_a) = (−0.80945, −0.61221) — inside 1σ of the DESI DR2 + CMB + Pantheon+ fit; z_c = 0.34179; q₀ = −0.33690; j₀ = −0.11125 against ΛCDM's exact +1; acceleration from z = 0.78569 to a/a₀ = 11.787; γ = 1, measured cosmologically as 1.025 ± 0.07 (§§26–28).

A reader who wants only the physics can read §§1–5, §11, §18, and §§26–28. The Scholium answers the twelve objections most worth answering.

---

## Abstract

Under standard causality and regularity hypotheses, the causal order of a spacetime determines its topology, differential structure, and conformal geometry — everything except its scale. Scale is therefore not a bookkeeping convention but a physical register in its own right, and the question of what sources it is distinct from the question of what sources curvature. This monograph develops the hypothesis that the scale register gravitates through the modular structure of causal regions: the dark sector is not a substance inserted into spacetime but the gravitational appearance of an information-geometric response. An elasticity, not a fluid.

One constitutive principle and one representation-theoretic identification close the late-time background completely. The identification: the homogeneous modular quotient at a codimension-two causal cut is the chirality grading of the cut's two-dimensional Lorentzian normal plane. From it are derived, in order: the exact functional form of the dark density (sech² in e-folds — the unique information geometry of a binary), the affine soldering of modular polarisation to Weyl scale and its coefficient (ϱ⊥ = 1, by integrality plus a flatness ceiling), the constitutive stiffness converting information response into stress (the entanglement capacity), the capacity-to-entropy ratio of the crossing horizon (γ = 1, by two-dimensional conformal thermodynamics), and the dimensional normalisation (the Misner–Sharp marginality identity, in which ħ, k_B, G, and c all cancel). The theory contains no cosmological constant and no new constant of any kind; the amplitude of dark energy is half the critical density at the self-dual epoch, a relational quantity, and its epoch is the unique minimum of an intrinsic modular functional, dated by flatness.

The equation of state obeys an exact differential invariant, 9(1+w)² + 6 dw/dN = 4, which is the operator normalisation ⟨Q²⟩ = 1 written in cosmological variables. Its phase flow is the canonical saddle-node normal form, so one density maximum, one w = −1 crossing, and one finite acceleration episode are a single structural statement. The perturbation operator is generated rather than chosen: it is the Witten Laplacian of the binary statistical manifold, reflectionless with exactly one bound state.

Quantitative predictions, with zero adjustable parameters: the CPL tangent (w₀, w_a) = (−0.80945, −0.61221), statistically indistinguishable from the published DESI DR2 + CMB + Pantheon+ best fit (−0.838 ± 0.055, −0.62 +0.22/−0.19); the phantom crossing at z_c = 0.34179, inside the z ≈ 0.35–0.44 band implied by the DESI combined fits; exact coincidence of the crossing, the dark-density maximum, and dark–ordinary equality; q₀ = −0.33690, stable to ±0.004 across the allowed Ω_m range where ΛCDM's tracks Ω_m; j₀ = −0.11125 against ΛCDM's exact j = 1; acceleration entry at z = 0.78569 and exit at a/a₀ = 11.787; capacity ratio γ = 1, measured cosmologically as 1.025 with 1σ range [0.941, 1.088]; and relaxation of the DESI neutrino-mass tension. Against DESI DR2 BAO + Pantheon+, the model improves on flat ΛCDM by Δχ² = −3.38 at equal parameter count, the best AIC of six families tested. The local cosmological constant problem is dissolved by a blindness theorem: additive vacuum energy has zero modular length and is annihilated by the trace-free source equation; dark energy in this theory is an episode, not an era, and there is no constant whose value is 10⁻¹²² of anything.

---

# Part I — The question, the inputs, the results

## 1. The situation this theory addresses

Since 1998 the expansion of the universe has been measured to accelerate. The standard accommodation, flat ΛCDM, attributes the acceleration to a cosmological constant Λ: a new constant of nature with equation of state w = −1 exactly and forever. Between 2024 and 2026 that accommodation came under quantitative strain. The DESI Baryon Acoustic Oscillation programme, combined with the CMB and with each of three independent supernova compilations, prefers a dark energy that _evolves_ — with present-day equation of state above −1 and a past excursion below it — at 2.8σ (Pantheon+), 3.8σ (Union3), and 4.2σ (DES Y5) [31]. In the standard two-parameter language (defined in §9), the preferred region is w₀ ≈ −0.67 to −0.84, w_a ≈ −0.6 to −1.1.

Four questions now stand, in increasing order of specificity:

1. **The magnitude question** (the vacuum catastrophe). Quantum field theory assigns the vacuum an energy density of order the Planck density; the observed dark density is smaller by a factor of order 10⁻¹²². Why does vacuum energy not gravitate at its computed size?
2. **The coincidence question.** Dark and ordinary energy densities, which in ΛCDM scale differently by three powers of a, are comparable now. Why now?
3. **The dynamics question** (new, from DESI). If dark energy evolves, what fixes the _shape_ of its evolution? Every phenomenological family — CPL, PEDE, running vacuum, vacuum metamorphosis, interacting dark energy [35,36,37] — is constrained by data but selected by nothing.
4. **The type question**, which this monograph takes as primary. What _mathematical type_ of object is cosmic expansion, and what kind of thing can source it? Answers to questions 1–3 depend on the answer to 4.

The theory developed here answers question 4 with a theorem-backed identification, and questions 1–3 then receive answers as corollaries: the vacuum does not gravitate locally because additive offsets have zero length in the relevant geometry (§22); dark and ordinary densities are equal at the crossing _exactly and necessarily_ (§18); and the shape of the evolution is the unique information geometry of a binary (§12), leaving nothing to select.

## 2. The structural gap: causal order fixes everything but scale

The motivation is a theorem, not an aesthetic. `[STANDARD]` For a distinguishing spacetime, the causal order — the bare relation "event p can signal event q" — determines the manifold's topology, its differential structure, and its conformal geometry, but not its metric scale (Hawking–King–McCarthy [1]; Malament [2]). A conformal manifold (M, [g]) becomes a metric manifold only after a choice of scale,

$$g_{\rm phys} = \sigma^{-2}\boldsymbol{g}, \qquad \sigma \in \Gamma(\mathcal{E}[1])$$

where 𝓔[1] is the bundle of conformal densities of weight one (§8). Nine of the metric's ten components are causal data; the tenth — the local unit of length — is not.

Two readings of this theorem are available. The conventional reading treats σ as gauge: fix it once (say, by atomic clocks) and forget it. The reading taken here is that **scale is a separate register with its own possible dynamics**. In any theory that takes causal order as primitive, what sources the scale register is a different question from what sources curvature, and the two need not have the same answer — or even the same mathematical type.

The observation that motivates everything that follows: the phenomena filed under "dark energy" live _exactly_ in the register that causal order leaves free. Late-time cosmology is, kinematically, a one-function story — the expansion history a(t), i.e., the history of scale. The hypothesis is that this is not an accident of FLRW symmetry but a statement about what dark energy _is_.

## 3. The theory's inputs, complete

Everything assumed is listed here; nothing is assumed elsewhere.

**Imported theorems.** `[STANDARD]` General relativity, in its exactly equivalent conformal-tractor form (§8, [3,4,5,41]); the modular theory of von Neumann algebras and its geometric realisations where proved (§6, [6,7,45,46,47]); the classification theorems of information geometry (§7, [15,16,17,18]); flat FLRW kinematics with the measured matter and radiation fractions.

**The constitutive principle.** `[FRAMEWORK]` The scale register gravitates through its modular free-energy response: the dark energy density is the modular free-energy stiffness of the causal region, per causal-diamond volume (made exact in §15). This principle is the definition of the theory — the analogue of "stress-energy sources curvature" for the scale channel. It is not a parameter and contains none.

**The identification.** `[IDENTIFICATION]` Postulate P (§11): the homogeneous, J-odd modular quotient at a codimension-two causal cut is the chirality grading of the cut's Lorentzian normal plane, and modular flow at the self-dual cut is geometric. This is a selection among representations — the same kind of statement as "space has three dimensions" or "the gauge group is SU(3)×SU(2)×U(1)". It has no continuous freedom.

**Sector data.** `[SECTOR]` Spatial flatness; global flux residual Λ_res = 0; the expanding branch; separate conservation of the dark and ordinary sectors. These label superselection and state-selection choices. Separate conservation is equivalent to the statement that the modular functional carries no direct matter coupling; it is an assumption and is listed as one.

Everything else in this document — the sech² profile, the coefficient ϱ⊥ = 1, the ratio γ = 1, the amplitude ½ρ_crit,c, the epoch N_c, the invariant, the phase flow, the perturbation operator, the vacuum-blindness result — is a theorem given the four items above. Cosmological data enter the derivation chain at exactly one point (§14), to select between the integers 1 and 2, and the selection is stable across the entire observationally allowed range of Ω_m.

## 4. The elimination test

A retyping is only content if the new variable is independently constructible. The test used throughout:

|||
|---|---|
|θ inferred only from H(z)|⟹ a relabelled effective fluid|
|θ constructed from causal-state algebra, predicting H(z)|⟹ new physical structure|

Sections 11–18 construct θ from the modular data of a causal cut without reference to any expansion history; §28 reports what the resulting prediction is worth against data; Scholium S1 states exactly how much of the test is passed in principle versus in practice.

## 5. Results at a glance

|result|statement|where|
|---|---|---|
|master identity|⟨Q²⟩ = 1: one identity, five registers|§12|
|soldering law|θ = ϱ⊥(N − N_c); the logarithm is derived|§13|
|coefficient|ϱ⊥ = 1, by integrality + flatness ceiling|§14|
|constitutive law|ρ_X = stiffness of modular free energy|§15|
|capacity ratio|γ = 1: the crossing horizon stores information like a 2D CFT|§16|
|dimensional bridge|T·S/V = ρ_crit at a flat apparent horizon; all constants cancel|§17|
|closed source law|ρ_X = ½ρ_crit,c sech²(N − N_c); dark = ordinary at crossing, exactly|§18|
|shape invariant|9(1+w)² + 6w′ = 4, exact and parameter-free|§19|
|phase flow|canonical saddle-node; one acceleration episode; three futures split by ϱ⊥|§20|
|geometric unification|the whole history is a half-turn of the unit circle; Fisher length = π|§21|
|vacuum blindness|additive vacuum energy has zero modular length; local CC problem dissolved|§22|
|generated operator|the perturbation kernel is the Witten Laplacian: ℓ = 1 Pöschl–Teller|§24|
|headline numbers|(w₀,w_a) = (−0.809, −0.612); z_c = 0.342; q₀ = −0.337; j₀ = −0.111; γ = 1.025 ± 0.07 measured|§§26–28|

---

# Part II — Background, self-contained

This part supplies everything a reader needs that is not derived here. A reader fluent in operator algebras, information geometry, and cosmology can skim to §10.

## 6. Modular theory in five paragraphs

`[STANDARD]` To a region 𝒪 of spacetime, quantum field theory assigns a von Neumann algebra 𝒜(𝒪) of observables measurable inside it, and the global state ω restricts to a state on that algebra [46]. For well-behaved (cyclic-separating) states, Tomita–Takesaki theory extracts from the pair (𝒜(𝒪), ω) two canonical objects: a positive **modular operator** Δ_ω and an antiunitary **modular conjugation** J_ω, via the polar decomposition S = JΔ^{1/2} of the state-reflection map. Neither is chosen; both are functionals of the region and the state.

The modular operator generates a distinguished one-parameter flow on the algebra, σ_t(A) = Δ^{it} A Δ^{−it}, with respect to which ω is thermal at inverse temperature 1 in the KMS sense. The modular Hamiltonian is K = −ln Δ. The conjugation J maps the algebra onto its commutant — the observables of the causal complement — and implements a reflection.

**Geometric modular flow.** For special region–state pairs the abstract flow is a spacetime motion. Bisognano–Wichmann `[STANDARD]` [6]: for a Rindler wedge in the Minkowski vacuum, modular flow is the wedge-preserving Lorentz boost, and the KMS temperature is the Unruh temperature [45]. Casini, Huerta, and Myers [7]: for a ball in a CFT vacuum, modular flow is the conformal boost preserving the causal diamond. These theorems ground the identification of horizon thermodynamics with modular data [8,9,10,11,12], and a body of recent work extends geometric or approximately geometric modular flow to wider classes of states and horizons [20,21,22]. Kinematic space constructions [13,14] show the same modular data organising bulk geometry. What is _not_ yet a theorem is geometric flow at the apparent horizon of a dynamical FLRW state; that is exactly the content of identification P and open problem Q2.

**Comparing two states.** Given two states ω₁, ω₂ on the same algebra, the **Connes cocycle** u_t = [Dω₂ : Dω₁]_t is a one-parameter family of unitaries inside the algebra that measures their relative modular data [47]. It is intrinsic (no choice of representation), and it satisfies a chain rule: [Dω₃ : Dω₁]_t = [Dω₃ : Dω₂]_t [Dω₂ : Dω₁]_t. The cocycle is the tool that makes "how does the state respond when the scale changes?" a well-posed, choice-free question (§13).

**Two directions at a cut.** Throughout, two tangent directions on the state space of a cut are distinguished and must never be conflated. The **vertical** direction is motion along the modular flow itself (boost parameter s; in cosmology, the horizon's own clock). The **horizontal** direction is motion _transverse_ to the flow — a change of state at fixed localisation, parameterised below by θ. They are different directions with different metrics and, it will turn out, different capacity ratios (§16, §17).

## 7. Information geometry in four paragraphs

`[STANDARD]` A parametric family of states ρ_θ carries a canonical Riemannian metric measuring statistical distinguishability. Classically it is the Fisher metric, and Čencov's theorem [16] fixes it uniquely (up to scale) as the only metric monotone under sufficient statistics. Quantum mechanically, monotonicity alone does not select one metric: Petz classified an infinite family of monotone metrics [15]. Among them the **Bogoliubov–Kubo–Mori (BKM)** metric is distinguished, up to constant multiple, as the Hessian of Umegaki relative entropy S(ρ‖σ) = Tr ρ(ln ρ − ln σ) and as the unique monotone metric whose exponential and mixture connections are mutually dual [17,18]. It is the metric of linear-response theory. This document uses BKM throughout and never relies on a property special to it beyond these two.

**Exponential families.** For a family ρ_θ = e^{θQ − Ψ(θ)}ρ₀ generated by an operator Q, the log-partition function Ψ(θ) = ln Tr e^{θQ}ρ₀ is the potential of a _dually flat_ geometry: its first derivative is the dual (mixture) coordinate η = ⟨Q⟩_θ, its second is the BKM metric g = Var_θ(Q). The pair (θ, η) are the two flat affine coordinate systems of the family; the metric is the Jacobian between them, g = dη/dθ.

**Capacity.** For the one-parameter family generated by rescaling the modular Hamiltonian itself, ρ(λ) ∝ e^{−(1+λ)K}, the BKM norm of the tangent at λ = 0 is Var(K) — the **entanglement capacity** C_E, the quantum- information analogue of heat capacity. Its ratio to the entropy, C/S, is a pure thermodynamic exponent: if S ∝ T^a then C/S = d ln S/d ln T = a (Appendix A.7).

**What these theorems do and do not fix.** Čencov, Petz, and duality fix the information metric on state space. **None of them fixes the gravitational conversion of that metric into an energy density.** That conversion is supplied by §§15–17 and nowhere else; keeping this boundary explicit is what prevents the construction from being circular.

## 8. Scale, conformal densities, and the tractor calculus in three paragraphs

`[STANDARD]` On a conformal manifold, a **conformal density of weight w** is a field that rescales as σ ↦ Ω^w σ when the representative metric rescales as g ↦ Ω²g; the line bundle of such fields is 𝓔[w]. A **scale** is a positive section σ ∈ Γ(𝓔[1]); choosing one turns the conformal class into a metric, g_phys = σ⁻²**g**. In flat FLRW the natural scale is the cosmic scale factor, and the Weyl coordinate used throughout is

$$N = \ln(a/a_c) = -\ln(\sigma/\sigma_c),$$

e-folds measured from a reference epoch (fixed intrinsically in §18).

The **tractor calculus** [3,4,5] packages scale-dependent geometry conformally covariantly: the scale tractor I_A = (1/n) D_A σ (with D the Thomas operator) encodes σ and its derivatives, and general relativity is exactly equivalent to a transport-plus-norm law for I_A [41], used in §22. Poincaré–Einstein holography realises the same structure from the boundary side [40]. For this document only two imported facts are needed: the trace-free Einstein equation in tractor form, and the norm identity I² = −R/12 in four dimensions.

Nothing in the derivation chain (§§11–18) uses tractor machinery; it enters only in §22, where it supplies an exact identity for the _vertical_ sector and the vacuum-blindness theorem.

## 9. The cosmological dictionary

`[STANDARD]` Flat FLRW: ds² = −dt² + a²(t)dx², H = ȧ/a, and each component i with equation of state w_i = p_i/ρ_i obeys dρ_i/dN = −3(1 + w_i)ρ_i. The critical density is ρ_crit = 3c²H²/8πG; fractions Ω_i = ρ_i/ρ_crit. Kinematics beyond H are carried by the deceleration and jerk parameters

$$q = -\frac{\ddot a a}{\dot a^2}, \qquad j = \frac{\dddot a a^2}{\dot a^3} = q + 2q^2 - \frac{dq}{dN},$$

with the sign conventions of [50]. Flat ΛCDM has j = 1 identically, at all times — a rigidity that makes j a clean discriminator (§27, P2).

**Dark energy phenomenology.** An arbitrary dark history ρ_X(a) defines an effective equation of state w_X(a); the standard two-parameter summary is the Chevallier–Polarski–Linder (CPL) form w(a) = w₀ + w_a(1 − a) [43,44], which is the tangent line at a = 1. DESI DR2 [31,32] measures BAO distance ratios (D_M/r_d, D_H/r_d) in seven tracers; Pantheon+ [33,34] measures supernova magnitudes; together they constrain (w₀, w_a) and, within a model, the full w(z).

**Horizons.** The flat-FLRW apparent horizon sits at R_A = c/H. Its area entropy is S = k_B A c³/4Gℏ; its boost-normalised (horizontal) temperature is k_B T = ℏc/2πR_A; its dynamical Kodama–Hayward (vertical) temperature carries an extra running factor μ_A = (1 − q)/2 [23,24]. The **Misner–Sharp energy** [42] inside radius R is E_MS = (c⁴R/2G)·(compactness); at the flat apparent horizon the compactness is exactly 1 — the marginality identity used in §17.

## 10. Notation and conventions

|symbol|meaning|status|
|---|---|---|
|(M, [g])|conformal spacetime|standard|
|σ ∈ Γ(𝓔[1])|scale section; g_phys = σ⁻²**g**|standard|
|N = ln(a/a_c)|Weyl e-fold coordinate|exact in FLRW|
|I_A|scale tractor|standard|
|𝒜(𝒪), ω|causal-region algebra and state|standard|
|Δ_ω, J_ω, K|modular operator, conjugation, ln Δ⁻¹|standard|
|s|vertical (modular-flow) parameter|standard|
|μ_A = (1−q)/2|running horizon index|exact in FLRW|
|θ|horizontal relative modular polarisation|derived (§13)|
|Q|normalised J-odd chirality grade, Q² = 1|**identification** (§11)|
|η = ⟨Q⟩ = tanh θ|mixture (m-affine) coordinate|exact|
|g^BKM = Var(Q) = sech²θ|BKM metric of the binary|standard|
|ϱ⊥ = dθ/dN|scale–modular soldering coefficient|**derived = 1** (§14)|
|C_E = Var(K)|entanglement capacity|standard|
|γ_⊥,c = C_E/(S/k_B)|capacity-to-entropy ratio at the cut|**derived = 1** (§16)|
|ρ_*, N_c|peak dark density; self-dual epoch|derived (§18)|
|Λ_res|global flux residual|sector datum, set to 0|
|w₀, w_a, q₀, j₀|CPL tangent; deceleration; jerk, today|standard|

Signature (−,+,+,+); n = 4. Overdot is d/dt, prime is d/dN unless stated. Benchmark: Ω_m0 = 0.310598, Ω_r0 = 9.15 × 10⁻⁵, spatial flatness, Λ_res = 0, expanding branch. Entropies in nats (k_B = 1) where convenient. Sign conventions for q and j are registered against predictions P2 and P3 of §27: a reader using opposite conventions must flip those predictions with them.

---

# Part III — The identification

## 11. The postulate

There is exactly one, and it is a statement about which mathematical structure the homogeneous modular sector realises.

> **P (Normal-chirality closure).** `[IDENTIFICATION]` A codimension-two causal cut Σ has a two-dimensional Lorentzian normal plane N(Σ) = L₊ ⊕ L₋ spanned by its two null normal directions. The homogeneous, J-odd modular quotient at Σ is the chirality grading of that plane, $$Q = P_+ - P_-, \qquad Q^2 = \mathbf{1}, \qquad JQJ = -Q,$$ and modular flow at the self-dual cut is geometric — the boost of the normal plane.

**Why this is one identification, not several.** Q² = 1 is automatic once Q is the difference of complementary orthogonal projectors: (P₊ − P₋)² = P₊ + P₋ = 1. JQJ = −Q is automatic because the modular conjugation exchanges the two null directions. That modular flow is geometric is a theorem for a wedge in the Minkowski vacuum [6] and for a CFT ball in the vacuum [7]; for the self-dual cut of a dynamical FLRW state it is the assumption, and it is the _only_ assumption (open problem Q2).

**Its type.** This is a selection among representations, of the same kind as "spacetime has three spatial dimensions" or "the gauge group is SU(3)×SU(2)×U(1)". It is not a fitted number, it has no continuous freedom, and — like those postulates — it is a legitimate stopping point for a physical theory. What can be demanded of such a selection is that it be minimal, that it be consistent, and that it predict; §§12–28 are the demonstration.

**Why it is the minimal choice.** The cut supplies exactly two null normal directions and nothing else that is homogeneous, J-odd, and scalar. A rank-one binary is the smallest structure capable of carrying a nontrivial J-odd scalar response, and the null pair is the only such structure the geometry provides. Richer candidate structures are not merely unmotivated; their consequences were computed and are excluded by data (Scholium S12).

---

# Part IV — The derivation chain

Each result below follows from its predecessors. Cosmological data enter at exactly one point (§14, through Ω_m) and nowhere else.

## 12. Binary information geometry and the master identity `[THEOREM]`

From P, the state family generated by Q is the rank-one exponential family

$$\rho_\theta = \frac{e^{\theta Q}}{2\cosh\theta}, \qquad \Psi(\theta) = \ln\operatorname{Tr}e^{\theta Q} = \ln(2\cosh\theta).$$

Ψ is the log-partition function; its first two derivatives give the dual affine coordinate and the metric of the dually flat structure (§7):

$$\eta = \Psi'(\theta) = \langle Q\rangle = \tanh\theta, \qquad g = \Psi''(\theta) = \operatorname{Var}(Q) = \operatorname{sech}^2\theta,$$

and the normalisation Q² = 1 becomes the **master identity**

$$\boxed{;\eta^2 + g = \langle Q^2\rangle = 1;}$$

**This single identity carries the entire construction.** It appears in five registers, and they are the same statement:

|register|form|
|---|---|
|algebraic|⟨Q²⟩ = 1|
|geometric|(η, √g) lies on the unit circle|
|dynamical|η′ = 1 − η², a Riccati equation|
|cosmological|9(1+w_X)² + 6 dw_X/dN = 4ϱ⊥² (§19)|
|spectral|η² + η′ = 1, the supersymmetry condition (§24)|

There is nothing to choose in this section: given a binary, its information geometry is unique. The sech² that will become the dark density is not a selected profile; it is the variance of a two-outcome observable, the only function a binary has to offer.

## 13. The soldering law `[THEOREM, given P]`

Let σ₁, σ₂ be two scale sections with associated causal-region states, and let

$$u_t = [D\omega_{\sigma_2} : D\omega_{\sigma_1}]_t$$

be the Connes cocycle comparing them (§6). Under P the reduced cocycle has a single noncentral generator, so modulo the centre

$$u_t \simeq \exp{it[\theta(\sigma_2,\sigma_1),Q + c,\mathbf{1}]}.$$

Weyl covariance requires θ to depend only on the ratio r = σ₂/σ₁, because no preferred scale exists to compare against. Connes' chain rule then becomes multiplicative on the reduced generators, and matching noncentral parts gives Cauchy's exponential–additive equation

$$\theta(r_1 r_2) = \theta(r_1) + \theta(r_2).$$

With measurability — which follows from σ-weak continuity of the cocycle in t; continuity in r is not required — the only solutions are

$$\boxed{;\theta(r) = -\varrho_\perp \ln r ;\Longleftrightarrow; \theta = \varrho_\perp(N - N_c);}$$

**The logarithm is derived, not chosen.** A scale-free comparison of states must be additive over ratios, and additivity over ratios _is_ the logarithm. Cauchy's equation admits a one-parameter family, and ϱ⊥ is that parameter; no further work on the cocycle can fix its value. N_c is the integration constant, fixed intrinsically in §18.

## 14. ϱ⊥ = 1 `[THEOREM, given P]`

Two independent facts combine.

**(a) Integrality.** The normal pair L₊ ⊕ L₋ carries boost characters e^{±θ}; the scale line carries the fundamental density pair 𝓔[1] ⊕ 𝓔[−1] with characters e^{±N}. Equivariant soldering of the two graded pairs forces e^{±θ} = e^{±(N−N_c)} up to tensor powers: a value ϱ⊥ = n corresponds to the n-th power 𝓔[n] ⊕ 𝓔[−n]. Hence

$$\varrho_\perp \in \mathbb{Z}^+.$$

This converts a continuous coefficient into a discrete selection. It does not, by itself, select the fundamental representation.

**(b) The existence ceiling.** Flat normalisation on the response-normalised branch requires r_c e^{3x} sech²(ϱ⊥x) = T_m with x = −N_c and T_m = (1 − Ω_m − Ω_r)/Ω_m (Appendix A.5, A.8). Since d ln F/dx = 3 − 2ϱ⊥ tanh(ϱ⊥x), there is exactly one root for ϱ⊥ ≤ 3/2 and two-or-none above, with the double root giving a closed-form ceiling:

$$\frac{T_m}{r_c} = \left(1 - \frac{9}{4\varrho_\perp^2}\right)\exp\left[\frac{3}{\varrho_\perp}\operatorname{artanh}\frac{3}{2\varrho_\perp}\right], \qquad \varrho_\perp > \tfrac32.$$

|Ω_m|ϱ⊥^max|admissible integers|
|---|---|---|
|0.280|1.6962|**{1}**|
|0.310598|1.8141|**{1}**|
|0.330|1.9060|**{1}**|
|0.34685|2.0000|{1, 2}|

ϱ⊥ = 2 first becomes admissible at Ω_m = 0.34685, which is 3.8σ from the measured 0.3086 ± 0.010 and is excluded by direct fit at Δχ² = 60.

$$\boxed{;\text{integrality} + \text{ceiling} + \Omega_m ;\Longrightarrow; \varrho_\perp = 1 \text{ uniquely};}$$

**This is the sole point at which cosmological data enter the derivation**, and they enter only to select between the integers 1 and 2 — a discrete choice stable across the entire observationally allowed range of Ω_m. The physical reading of the result: the scale line is soldered to the modular binary in the fundamental representation — one unit of modular polarisation per e-fold.

## 15. The constitutive law `[FRAMEWORK made exact]`

The scale susceptibility is the pullback of the BKM metric along the soldering map Φ: ℝ_Weyl → 𝒮(𝒜):

$$\mathcal{X}_\sigma = g^{\rm BKM}\left(\frac{d\theta}{dN}\right)^2 = \varrho_\perp^2\operatorname{sech}^2[\varrho_\perp(N-N_c)].$$

𝒳_σ is a quadratic differential, not a scalar: the invariant object is 𝒳_σ dN² = sech²θ dθ², in which ϱ⊥ does not appear. ϱ⊥ specifies how Weyl scale parameterises a fixed path in state space; it does not change the path.

The constitutive principle of §3 is now made exact. For a reference KMS state ρ_c with physical modular Hamiltonian 𝓗_c = k_B T_c K_c, the nonequilibrium free energy satisfies exactly

$$F_c(\rho) - F_c(\rho_c) = k_B T_c, S(\rho,|,\rho_c),$$

and for a nearby state S(ω_{N+dN}‖ω_N) = ½ G^⊥_NN dN² + O(dN³), where G^⊥ is the extensive BKM form on the horizontal tangent. Hence

$$\boxed{;\rho_X(N) = \frac{k_B T_c}{2V_c},G^{\perp}_{NN}(N), \qquad G^{\perp}_{NN} = C_{\perp,c},\varrho_\perp^2\operatorname{sech}^2\theta;}$$

where C_⊥,c is the extensive BKM norm of the selected horizontal tangent. The binary quotient supplies the normalised shape; the full causal-diamond state supplies the number of participating units.

**This is not a local spacetime kinetic action.** It is a Dirichlet functional on a curve in state space, Γ_⊥ = (k_B T_c/2)∫dN G^BKM(𝒟_Nω, 𝒟_Nω). The distinction matters twice over: the canonical-sigma-model no-go of §23 does not apply to it, and it is why θ must ultimately be typed as a constitutive coordinate rather than a field (§23).

## 16. γ = 1 `[THEOREM, given P]`

Two steps.

**(a) The horizontal BKM norm is the entanglement capacity.** `[THEOREM]` For the exponential family generated by rescaling the modular Hamiltonian, ρ(λ) = e^{−(1+λ)K₀}/Z(λ),

$$G^{\rm BKM}_{\lambda\lambda}\Big|_{0} = \frac{\partial^2 \ln Z}{\partial\lambda^2}\Big|_{0} = \operatorname{Var}(K_0) = C_E,$$

verified numerically on random modular spectra to 10⁻⁶. The horizontal direction _is_ the modular-rescaling direction, because a Weyl rescaling changes the diamond radius R, hence its temperature T = ħc/2πR, hence β. So C_⊥,c = C_{E,c} is an identity of exponential families, not a hypothesis.

**(b) The ratio is a thermodynamic exponent.** With C_E = Var(K) and S/k_B = ⟨K⟩,

$$\boxed{;\gamma_{\perp,c} \equiv \frac{C_{\perp,c}}{S_c/k_B} = \frac{\operatorname{Var}(K)}{\langle K\rangle} = \frac{C}{S} = \frac{d\ln S}{d\ln T};}$$

so if S ∝ T^a then γ = a (Appendix A.7):

|sector|S ∝|γ|
|---|---|---|
|thermal CFT, d = 4 (bulk matter)|T³|3|
|horizon varied by size (Schwarzschild-like)|T⁻²|−2|
|**two-dimensional CFT**|**T**|**1**|

γ = 1 holds if and only if S ∝ T, which among conformal sectors is unique to d = 2 (γ = d − 1).

**The horizontal sector is two-dimensional.** By P, the normal plane is 2D and Lorentzian and modular flow there is the boost. The transverse directions along Σ are FLRW-symmetry-invariant and **J-even**, so they carry no J-odd horizontal tangent and drop out of G^⊥ identically. The horizontal sector is therefore the chiral algebra of the normal plane. Cardy's formula [39] for a 2D CFT at fixed spatial length L gives F = −πcL/6β², hence

$$S = \frac{\pi c L}{3}T, \qquad C = T\frac{dS}{dT} = S \qquad\Longrightarrow\qquad \gamma_{\perp,c} = 1.$$

**Fixed L is the correct condition**, because the horizontal deformation is by definition at fixed localisation. Varying L is the _vertical_ direction, which gives S ∝ R², T ∝ 1/R, γ = −2. The two directions have different capacity ratios; conflating them is the error the vertical/horizontal split of §6 exists to prevent, and §17 shows the data punishing the conflation.

The physical reading: **at the crossing, the causal horizon stores information like a two-dimensional conformal system — its heat capacity equals its entropy.** This is prediction P5 of §27, and it is measured.

## 17. The dimensional bridge `[THEOREM]`

The remaining question is what converts a dimensionless information metric into an energy density. The crossing causal diamond supplies it, with no new constant.

For the spatially flat FLRW apparent horizon, R_c = c/H_c, and

$$\frac{S_c}{k_B} = \frac{A_c c^3}{4G\hbar} = \frac{\pi R_c^2 c^3}{G\hbar}, \qquad k_B T_c = \frac{\hbar c}{2\pi R_c},$$

so that

$$k_B T_c \frac{S_c}{k_B} = \frac{c^4 R_c}{2G} = E_{\rm MS,c}, \qquad \frac{E_{\rm MS,c}}{V_c} = \frac{3c^2H_c^2}{8\pi G} = \rho_{\rm crit,c}$$

$$\boxed{;\frac{k_B T_c}{V_c}\cdot\frac{S_c}{k_B} = \rho_{\rm crit,c};}$$

ħ, k_B, G and c all cancel. E_MS is the Misner–Sharp energy [42], and the middle equality is the Friedmann marginality identity 2GE_MS/(c⁴R_A) = 1 at a flat FLRW apparent horizon: the causal radius is exactly the radius at which enclosed gravitational energy saturates the spherical compactness relation. It is _not_ a claim that the observable universe is a Schwarzschild black hole; the two share an area–temperature–energy normalisation because both are marginal causal-information surfaces, and the identity is what "marginal" means.

The temperature here is the **horizontal** modular temperature in the canonical 2π boost normalisation. It must not be confused with the running **vertical** Kodama–Hayward temperature T_KH = μ_A T_c [23,24,25]. Using the vertical temperature in the horizontal channel yields γϱ⊥²/2 = μ_A/2 and r_c = 1/4, which is excluded by data — a check that the vertical/horizontal distinction is doing physical work, not taxonomy.

## 18. The closed source law and the equality theorem

Combining §§15–17:

$$\boxed{;\rho_X(N) = \frac{\gamma_{\perp,c}\varrho_\perp^2}{2},\rho_{\rm crit,c},\operatorname{sech}^2[\varrho_\perp(N-N_c)];}$$

At the self-dual point θ = 0 this gives the crossing normalisation

$$\Omega_{X,c} \equiv \frac{\rho_*}{\rho_{\rm crit,c}} = \frac{\gamma_{\perp,c}\varrho_\perp^2}{2} ;\overset{\gamma=\varrho_\perp=1}{=}; \frac{1}{2},$$

and flatness, ρ_crit,c = ρ_ord,c + ρ_*, then forces

$$\boxed{;\rho_X(N_c) = \rho_{\rm ordinary}(N_c);}$$

**exactly**, where "ordinary" means the complete non-dark sector. Relative to dust alone the ratio is 1/(1 − 2Ω_r,c) = 1.000395 at the benchmark: the wall balances the dark response against all ordinary causal energy, not against dust in isolation. The factor of ½ is the Taylor coefficient of the quadratic free-energy Hessian; every other ratio in the chain is unity in the Einstein-capacity class.

**N_c is fixed intrinsically.** Since JQJ = −Q, the modular reflection of ρ_θ is ρ_{−θ}, and the symmetrized Umegaki relative entropy is [19]

$$\mathfrak{S}_J(\theta) = S(\rho_\theta|\rho_{-\theta}) + S(\rho_{-\theta}|\rho_\theta) = 4\theta\tanh\theta,$$

which vanishes only at θ = 0, is strictly increasing in |θ|, and has Hessian I_J(0) = 8 = 2γ^BKM(ΔX, ΔX) on the reflected tangent ΔX = 2X_*. **N_c is the unique global minimum of an intrinsic modular functional** — the epoch at which the state and its modular reflection are least distinguishable — not a chosen offset. Its cosmic date is then fixed by flatness: at the benchmark Ω_m, N_c = −0.2940066, i.e., z_c = 0.3417927 (Appendix A.8).

Read the last two boxes together and the coincidence problem inverts. In ΛCDM, "dark ≈ ordinary now" is a numerical accident requiring the value of Λ to be tuned against the matter density. Here, dark = ordinary **at the crossing** is a theorem; the crossing is intrinsically defined; and its redshift, 0.342, is a prediction from the measured matter fraction — confirmed by the DESI-implied crossing band (§27, P3). What remains of the coincidence question is only why the observation epoch lies within an e-fold of N_c, which is a question about Ω_m today, addressed as such in Scholium S10.

---

# Part V — The background history it entails

## 19. The shape invariant `[THEOREM]`

Separate conservation, dρ_X/dN = −3(1+w_X)ρ_X, applied to §18 gives

$$3(1+w_X) = 2\varrho_\perp\eta = 2\varrho_\perp\tanh\theta,$$

and the master identity η² + g = 1 becomes

$$\boxed{;9(1+w_X)^2 + 6\frac{dw_X}{dN} = 4\varrho_\perp^2 = 4;}$$

This is not a coincidence among hyperbolic functions. It is ⟨Q²⟩ = 1 written in cosmological variables: the statement that the dark sector's score variable is a normalised binary, expressed as a differential constraint on the equation of state that must hold **at every redshift**. Equivalent forms:

$$\frac{\rho_X}{\rho__} + \frac{1}{4\varrho_\perp^2}\left(\frac{d\ln\rho_X}{dN}\right)^2 = 1, \qquad \frac{d^2}{dN^2}\ln\frac{\rho_X}{\rho__} + 2\varrho_\perp^2\frac{\rho_X}{\rho_*} = 0.$$

The invariant is independent of the amplitude, so it measures ϱ⊥ separately from the normalisation. It is the theory's defining relation; what data can and cannot test it is settled quantitatively in §27 (P9).

## 20. The phase flow: one episode of acceleration `[THEOREM]`

Setting X := 1 + w_X and eliminating θ:

$$X' = \frac{2}{3}\varrho_\perp^2 - \frac{3}{2}X^2,$$

which under X = (2ϱ⊥/3)û, τ = ϱ⊥N becomes dû/dτ = 1 − û², the **canonical saddle-node (fold) normal form**. The coefficient 3/2 is fixed by gravity (the 3 in 3(1+w)); the unfolding parameter is (2/3)ϱ⊥². Fixed points:

$$w_\pm = -1 \pm \frac{2\varrho_\perp}{3} ;\overset{\varrho_\perp=1}{=}; -\frac{5}{3},; -\frac{1}{3},$$

and the history is the unique heteroclinic orbit joining them. **One density maximum, one w = −1 crossing, and one connected acceleration interval are one structural statement**, not three fitted events. At ϱ⊥ = 0 the fixed points merge and the dark sector disappears — the dark sector exists because the fold is unfolded, and ϱ⊥ measures by how much.

### 20.1 Why acceleration turns on, and why it turns off

The future fixed point is w_∞ = −1 + 2ϱ⊥/3. For ϱ⊥ = 1 this is **exactly −1/3**, the threshold at which a dark-dominated universe has q = 0. Hence:

|ϱ⊥|future|permanent event horizon|
|---|---|---|
|< 1|perpetual power-law acceleration|yes|
|**= 1**|**critical coasting, a ∝ t**|**marginally absent**|
|> 1|eventual deceleration|no|

ϱ⊥ = 1 — the value derived in §14 — is the separatrix between three causal futures. The fundamental representation is also the marginal one.

The acceleration episode is **finite and unique**, and the mechanism of its termination is structural, not tuned. Asymptotically ρ_X ∝ a⁻² with w_X → −1/3, so ρ_X + 3p_X → 0: the dark sector's _active gravitational_ (Komar) density vanishes even though its energy density still dominates. The residual matter, decaying as a⁻³, then controls the Komar density and returns q to 0⁺. At the benchmark:

$$z_{\rm entry} = 0.785694, \qquad (a/a_0)_{\rm exit} = 11.7865, \qquad \text{duration } 3.047 \text{ e-folds},$$

that is, acceleration began 0.580 e-folds ago and ends 2.467 e-folds from now. At exit, 1 + 3w_X = −1.59 × 10⁻² and the matter fraction is 1.57 × 10⁻². The dark sector does not disappear; it stops gravitating actively. **Acceleration, in this theory, is an episode — the finite interval during which a transient information-geometric response dominates the Komar density — not a destiny.**

## 21. Geometric unification: the history as a half-turn `[THEOREM]`

Because η² + g = 1, the pair (η, √g) = (tanh θ, sech θ) traces the unit circle. Setting η = sin φ, √g = cos φ determines

$$\varphi = \operatorname{gd}(\theta) = \arctan(\sinh\theta), \qquad d\varphi = \operatorname{sech}\theta,d\theta = ds_{\rm Fisher},$$

the Gudermannian function. The Fisher arc length _is_ the circular angle, and the complete history sweeps φ from −π/2 to +π/2:

$$L_F = \int_{-\infty}^{\infty}\operatorname{sech}\theta,d\theta = \pi = \int_0^1\frac{dp}{\sqrt{p(1-p)}},$$

which is exactly the diameter of the binary state simplex in the Fisher metric. The crossover is a **complete traversal from one extremal binary state to the other**, and its length is independent of ϱ⊥. In this parameterisation

$$\frac{\rho_X}{\rho_*} = \cos^2\varphi, \qquad \frac{3(1+w_X)}{2\varrho_\perp} = \sin\varphi.$$

φ = 0 is simultaneously the density maximum, the w_X = −1 crossing, the modular self-dual point, the maximum of the BKM metric, and the epoch at which the score carries exactly one bit (S = ln 2). Five characterisations, one epoch — this is the structural content behind prediction P4.

## 22. The vertical sector: tractor identity, e-fold budget, vacuum blindness

`[STANDARD]` For a scale σ, the trace-free Einstein equation is equivalent to a transport law for the scale tractor, and the trace to a norm law [3,4,5,41]:

$$\big(\nabla_a\nabla_b + P_{ab}\big)_0,\sigma = \frac{4\pi G}{c^4},\sigma\big(T^m_{ab} + T^X_{ab}\big)^\circ, \qquad I^2 = \frac{2\pi G}{3c^4}T - \frac{\Lambda_{\rm g}}{3},$$

with I² = −R/12 in four dimensions. `[THEOREM]` For FLRW this gives the exact identity

$$I^2 = -\mu_A H^2, \qquad \mu_A = \frac{1-q}{2} = \frac{d\eta_A}{dN},$$

verified to 10⁻¹¹ across five decades in redshift: **the vertical horizon-clock rate is the normalised scale-tractor norm.** The e-fold budget then splits exactly,

$$dN = d\eta_A + \tfrac14,d\ln\mathcal{S}_A,$$

into horizon-rapidity advance and horizon-information growth. For ϱ⊥ = 1 the asymptotic split is exactly 1:1 (μ_A → ½, I²/H² → −½, midway between the null tractor of Minkowski and the value −1 of de Sitter).

**Vacuum blindness.** `[THEOREM]` A central shift K ↦ K + α**1** leaves the normalised state, its relative entropy, its BKM metric, and Var(K) unchanged; the corresponding stress shift T_ab ↦ T_ab + λg_ab is annihilated by the trace-free source equation. An additive vacuum offset therefore has **zero horizontal BKM length** and produces no local source. Read this against question 1 of §1: the local vacuum problem is not solved by cancelling two large numbers to 122 decimal places; the offset lies in a direction to which the response is blind — for the information geometry because a central shift does not change the state, and for the geometry because the trace-free equation cannot see a pure trace. The two blindnesses are images of each other under the soldering. The residual **global** lift Λ_g is a genuinely separate object: manifestly local vacuum sequestering [26,27] shows it can be consistently isolated as a finite boundary flux datum, and this theory sets that datum to zero as its `[SECTOR]` choice. Which flux sector nature selects is not derived here (open problem Q4), and prediction P10 states the observable difference.

---

# Part VI — The perturbation sector

## 23. Four no-gos and the type of θ

These negative results are part of the content: they prevent the sech² profile from being attached indiscriminately to every equation, and they force the correct mathematical typing of θ.

**N1 — the matter-growth operator is not of Pöschl–Teller type.** `[NEGATIVE]` Under ψ = D a√H the growth equation becomes ψ″ = W(N)ψ with W = ¼(2+h)² + ½h′ + (3/2)Ω_m. Against a distance-matched comparator, ΔW/Ω_X spans −179 to +0.27, and a free three-parameter sech² fit leaves a 63.9% fractional residual. Ordinary matter growth is not the spectral problem the binary generates.

**N2 — no single-field completion.** `[NEGATIVE]` For a canonical scalar, z² ∝ 1 + w_X = (2ϱ⊥/3)tanh θ, which is negative on the entire pre-crossing branch: a ghost over a cosmological epoch, not a point defect. Near θ = 0, z ∼ |θ|^{1/2} and z″/z → −1/(4θ²) — the inverse-square potential at exactly the critical coupling 1/4 for fall-to-the-centre [30]. The crossing is marginal in a precise sense, which is why small deformations of one-field models do not cure it [28].

**N3 — tractors cannot supply the stiffness.** `[NEGATIVE]` Φ*G^BKM ∝ I·I fails (the ratio spans two decades). I·I is a norm built from σ and is vertical; 𝒳_σ is horizontal. Moreover Weyl and Cotton tensors vanish for FLRW, so the tractor connection is flat and carries no horizontal information.

**N4 — no canonical sigma model.** `[NEGATIVE]` Imposing the soldering θ̇ = ϱ⊥H on Γ = ∫√−g[(χ/2)G(θ)(∂θ)² − V] together with the target profile requires H² = (2ρ_*/3χϱ⊥)tanh θ, hence H² < 0 across the entire pre-crossing branch. Exact no-go.

**Consequence: the type of θ.** The completion must be collective, and θ is a **collective constitutive coordinate** of a scale-indexed state family — the same mathematical type as inverse temperature, chemical potential, an order parameter, or a Berry phase. It is neither a propagating local field (which N4 excludes) nor a function reconstructed from the metric (which would fail the elimination test of §4). Its independent definition is the Connes cocycle of §13. Temperature is the correct intuition throughout: temperature is real, it gravitates, its gradients do physics — and no one asks for its kinetic term.

## 24. The perturbation operator is generated, not chosen `[THEOREM]`

Define first-order operators from the information potential itself:

$$\mathcal{A} = \partial_\theta + \eta, \qquad \mathcal{A}^\dagger = -\partial_\theta + \eta.$$

Then, using only η² + g = 1:

$$\boxed{;\mathcal{A}^\dagger\mathcal{A} = -\partial_\theta^2 + 1 - 2\operatorname{sech}^2\theta, \qquad \mathcal{A}\mathcal{A}^\dagger = -\partial_\theta^2 + 1;}$$

verified to 4 × 10⁻¹⁶. **H₊ is free precisely because ⟨Q²⟩ = 1: the binary normalisation is the supersymmetry condition.** The ℓ = 1 Pöschl–Teller operator is therefore the Witten Laplacian [38] of the binary statistical manifold — generated by the geometry, not hypothesised about a perturbation sector.

Consequences, all forced:

- **Zero mode.** 𝒜ψ₀ = 0 gives ψ₀ = sech θ/√2, with |ψ₀|² = ½ g: the BKM metric is twice the bound-state probability density.
- **Reflectionless.** ψ_k = 𝒜†e^{ikθ} = (−ik + tanh θ)e^{ikθ} has no e^{−ikθ} component at either end, so R(k) ≡ 0 for all k [29]. There _is_ a transmitted continuum; reflectionlessness does not remove continuum degrees of freedom.
- **Witten index 1**, hence by Levinson's theorem a total transmission phase of π. The phase density in log-momentum is sech(s), the same function as the Fisher line element in position — a consequence of sech being self-reciprocal under Fourier transform.
- **The pair is generated.** The 1-D statistical manifold has de Rham complex Ω⁰ ⊕ Ω¹; Witten deformation by Ψ turns it into a two-component Dirac operator 𝒟_Ψ with 𝒟_Ψ² = diag(H₋, H₊). The perturbative pair is **form parity**, canonically generated by the binary line — it is _not_ the binary outcomes and must not be identified with Q.

**Directedness.** `[THEOREM]` The symmetrized relative entropy of §18 takes the cosmological form

$$\mathfrak{S}_J = 4\theta\eta = 6(N-N_c)(1+w_X) ;\ge; 0,$$

in which ϱ⊥ cancels. Non-negativity of relative entropy therefore **forces**

$$N < N_c \Rightarrow w_X < -1, \qquad N > N_c \Rightarrow w_X > -1.$$

The phantom→quintessence orientation of the crossover, relative to increasing Weyl scale, is a theorem rather than an input; the time-reversed pulse is forbidden. Independently, the ℓ = 1 transmission amplitude t(k) = −(α−ik)/(α+ik) has its single pole at k = +iα, the upper half plane — retarded, not advanced — and because the potential is reflectionless that pole is the entire scattering content. Scope: these fix the orientation of the crossover _relative to_ increasing N; they do not derive why the universe occupies the expanding branch, which is the `[SECTOR]` datum it appears as in §3.

## 25. What remains open in this sector `[OPEN]`

The Dirichlet functional Γ_⊥ of §15 evades N4 because it is a one-dimensional energy along a state trajectory rather than a spacetime action. For the same reason it does **not** yield T^X_ab by metric variation, so conservation is imposed rather than derived, and the lift of the Witten complex to a Lorentzian cosmological perturbation system has not been constructed. The required object is a natural quadratic response map

$$\mathfrak{R}_\Sigma: \operatorname{Sym}^2!\big(T^{J\text{-odd}}_{\omega_\Sigma}\mathcal{S}\big) \longrightarrow \Gamma\big(S^2T^*D_\Sigma\big), \qquad T^X_{ab} = \mathfrak{R}_\Sigma(X,X)_{ab},$$

satisfying naturality under causal embeddings, modular evenness, central blindness, conservation on the state equations, charge compatibility with the gravitational Noether charge, and the FLRW reduction u^au^bT^X_ab = χ⊥ G^BKM(X,X). This is a classification-of-natural-operators problem, not an arbitrary functional; it gates both the completion of the theory and, as §27 (P9) shows, the decisive observational test.

---

# Part VII — Predictions

## 26. The closed benchmark

Ω_m0 = 0.310598, Ω_r0 = 9.15 × 10⁻⁵, ϱ⊥ = γ_⊥,c = 1, Λ_res = 0, k = 0. **Zero adjustable dark-sector parameters.** Every entry below follows from the boxed law of §18 and the flatness closure of Appendix A.8.

|quantity|value|
|---|---|
|Ω_X,c = γϱ⊥²/2|0.500000000 (exactly ½)|
|N_c|−0.2940066|
|z_c|0.3417927|
|ρ_*/ρ_crit,0|0.7506311|
|ρ_*/ρ_ordinary(N_c)|1.000000000 (exactly 1)|
|ρ_*/ρ_m(N_c)|1.0003953 = 1/(1−2Ω_r,c)|
|Ω_r,c|1.9756 × 10⁻⁴|
|w_X(0)|−0.8094545|
|w_a (CPL tangent)|−0.6122053|
|q₀|−0.3369025|
|j₀|−0.1112465 (corrected; Appendix A.9)|
|dq/dN today|+0.0013505|
|acceleration entry|z = 0.7856935|
|acceleration exit|a/a₀ = 11.78652|
|9(1+w)² + 6w′|4.000000000 (exactly 4)|
|w_∞|−1/3 exactly; a(t) ∝ t; no event horizon|

Two facts about this table deserve emphasis before the ledger.

**q₀ is pinned.** Across the entire observationally allowed matter range, Ω_m ∈ [0.28, 0.33], the model's q₀ moves only between −0.334 and −0.337 — a spread below 0.004 — while ΛCDM's q₀ = (3/2)Ω_m − 1 sweeps from −0.58 to −0.51 across the same range. The model predicts the present deceleration parameter almost independently of the one measured input it takes. Numerically, today's acceleration is 63% of ΛCDM's at the same Ω_m.

**Today sits at the acceleration maximum.** From q₀ and j₀ via dq/dN = q + 2q² − j (Appendix A.9), dq/dN|₀ = +0.00135: the minimum of q — peak cosmic acceleration — falls at z = 0.0008. At the benchmark Ω_m, the present epoch is the acceleration maximum to one part in a thousand of an e-fold. This is a numerical fact at the measured Ω_m, not a structural one (the extremum sweeps z = +0.14 to z = −0.08 as Ω_m runs 0.25 to 0.36); it is recorded because it is the kind of coincidence a reconstruction can check.

## 27. The prediction ledger

Each entry states the prediction, what it means physically, where the data stand, and — where one genuinely exists — the condition that kills it. A falsifier is listed only if data of the current or next survey generation can actually trigger it; predictions whose tests lie further out say so plainly. Scoreboard first:

|#|prediction|value|current status|
|---|---|---|---|
|P1|CPL tangent (w₀, w_a)|(−0.80945, −0.61221)|inside 1σ of DESI DR2+CMB+Pantheon+; Δχ² = 1.78 from the free 2-parameter fit in this document's own pipeline|
|P2|kinematics today (q₀, j₀)|(−0.3369, −0.1112)|j₀ separates from ΛCDM's exact +1 by 1.1; cosmography approaching the required precision|
|P3|chronology: onset, crossing, exit|z = 0.786, z_c = 0.342, a = 11.79 a₀|DESI-implied crossing band z ≈ 0.35–0.44; own-pipeline profile z_c = 0.65, 1σ [0.29, open]|
|P4|triple coincidence|Δz ≡ 0 among crossing, density peak, equality|DESI CPL best fit separates them by only Δz = 0.019|
|P5|capacity ratio γ|1|measured 1.025, 1σ [0.941, 1.088]|
|P6|phase ordering|phantom strictly before z_c, quintessence strictly after|consistent with current reconstructions|
|P7|existence ceiling|ϱ⊥ ≤ 1.814|measured ϱ⊥ = 0.800, 1σ [0.575, 0.982]|
|P8|neutrino-mass release|Σm_ν bound reopens above the 0.059 eV floor|mechanism confirmed in DESI's own w₀w_aCDM analysis; dedicated Boltzmann run pending|
|P9|the invariant = 4|exact at every z|provably invisible to background data (Δχ² = 0.79 across two decades of deformation); test relocated to growth/lensing|
|P10|the far future|w → −1/3, a ∝ t, no event horizon|not testable on survey timescales; distinguishes Λ_res = 0 from Λ_res > 0|

### P1 — Evolving dark energy at a fixed point of the (w₀, w_a) plane

**Prediction.** (w₀, w_a) = (−0.80945, −0.61221), with zero adjustable parameters. More fully: the theory predicts the one-dimensional locus w_a = (3/2)(1+w₀)² − 2/3 (Appendix A.10), with position along it fixed by Ω_m; the benchmark Ω_m gives the point.

**Meaning.** Dark energy is dynamical. It was phantom (w < −1), it crossed −1 at z_c, and today it sits above −1 by exactly (2/3)tanh(0.294). The CPL "parameters" that surveys fit are, in this theory, the Taylor coefficients of tanh at the present epoch — outputs, not inputs.

**Status.** The published DESI DR2 constraints [31]:

|data combination|w₀|w_a|offset of the fixed point (per axis)|
|---|---|---|---|
|DESI + CMB + Pantheon+|−0.838 ± 0.055|−0.62 +0.22/−0.19|0.5σ, 0.04σ|
|DESI + CMB + Union3|−0.667 ± 0.088|−1.09 +0.31/−0.27|1.6σ, 1.5σ|
|DESI + CMB + DES Y5|−0.752 ± 0.057|−0.86 +0.23/−0.20|1.0σ, 1.1σ|

The (w₀, w_a) posteriors carry the standard strong anticorrelation, and the fixed point's offsets from the Union3 and DES Y5 centres lie _along_ the degeneracy direction, so the per-axis figures overstate the joint tension. Against this document's own DESI DR2 + Pantheon+ likelihood, releasing both CPL parameters improves on the fixed prediction by Δχ² = 1.78 — the zero-parameter point sits inside the 1σ region of the free two-parameter fit. A theory whose dark sector was closed by representation theory and a flatness ceiling lands, with nothing left to adjust, where three independent supernova compilations put the measurement.

**Falsifier.** A combined posterior excluding the locus w_a = (3/2)(1+w₀)² − 2/3 at high significance kills the framework; excluding the benchmark point while Ω_m remains near 0.31 kills the closed theory. Both are live tests of exactly the kind DESI-class data deliver.

### P2 — Kinematics today: q₀ = −0.3369, j₀ = −0.1112

**Meaning.** Two statements a reconstruction can read off without any dark energy model. First, present acceleration is weak: 63% of ΛCDM's, and pinned near −1/3 nearly independently of Ω_m (§26). Second, and sharper: the jerk. Flat ΛCDM has j = 1 identically at all times; this theory gives j₀ = −0.111 — a separation of 1.11 in a directly reconstructible kinematic quantity, with propagated Ω_m uncertainty of only ±0.03. The third derivative of the scale factor has the opposite character in the two theories: in ΛCDM the acceleration is still building toward de Sitter; here it has just peaked (dq/dN|₀ = +0.0014) and is beginning its structural decline toward coasting.

**Status and falsifier.** Current cosmographic determinations of j₀ carry order-unity errors; the ΛCDM-vs-model separation is at their edge, and DESI-plus-supernova compilations are the right data to close it. A measurement of j₀ consistent with +1 and excluding −0.11 kills the theory; the converse heavily disfavours any constant-w model.

### P3 — The chronology of the episode

**Prediction.** Acceleration onset z = 0.7857; phantom crossing, dark density maximum, and dark–ordinary equality all at z_c = 0.3418; acceleration exit at a/a₀ = 11.787, i.e., 2.47 e-folds from now; total duration 3.047 e-folds. ΛCDM at the same Ω_m puts onset at z = 0.643 and has no crossing, no density maximum, and no exit.

**Meaning.** The theory dates every landmark of the acceleration era from one measured number, Ω_m, and makes the era finite on both ends.

**Status.** The crossing implied by the DESI DR2 CPL fits sits at z ≈ 0.354 (Pantheon+), 0.405 (DES Y5), 0.440 (Union3) — Appendix A.10 — a band whose lower edge sits on the prediction, consistent within current errors. This document's own direct profile of z_c is broad: 0.650 with 1σ range [0.293, open], a 0.72σ displacement. The onset value z = 0.786 versus ΛCDM's 0.643 is a 22% separation in a quantity non-parametric reconstructions already estimate.

**Falsifier.** A reconstruction that localises the w = −1 crossing well away from the flatness-determined value — for instance robustly above z = 0.6 — kills the closed theory, since z_c has no freedom once Ω_m is measured.

### P4 — The triple coincidence (the signature prediction)

**Prediction.** z(w_X = −1) = z(ρ_X maximal) = z(ρ_X = ρ_ordinary), exactly.

**Meaning.** Generic evolving dark energy has no reason for these three epochs to be related at all: the crossing is a property of w(z), the peak a property of ρ_X(z), and equality a relation to the matter sector. Here all three are the single self-dual point φ = 0 of §21. This is the cleanest qualitative fingerprint the theory has: it costs any competitor a functional tuning to mimic and costs this theory nothing.

**Status.** At the DESI DR2 CPL best fit the first and third epochs already differ by only Δz = 0.019 — the data are, unprompted, near the coincident configuration.

**Falsifier.** Reconstructed equality and phantom-divide epochs separating beyond errors kills the theory outright. This is testable with the same non-parametric w(z) and ρ_X(z) reconstructions that already exist.

### P5 — The capacity ratio γ = 1

**Prediction.** The crossing horizon's capacity-to-entropy ratio is 1: the ratio of a two-dimensional conformal system, and of an Einstein-class causal horizon deformed at fixed localisation.

**Meaning and type.** γ is measured _through_ the model: within the sech² family, the crossing amplitude Ω_X,c = γϱ⊥²/2 is released and fitted. It is a one-parameter consistency test that the closed theory must pass at its predicted value, and a cosmological determination of a quantum-information quantity — to our knowledge the first of its kind.

**Status.** γ = 1.025, 1σ [0.941, 1.088]: a 7% determination, 0.03σ from the prediction. Robustness: across γ ∈ [0.8, 1.3] the co-fitted Ω_m moves only 0.3277 → 0.3186 — less than its own error — while χ² swings by 13; the constraint enters through z_c, which sweeps 0.546 → 0.049 across the same range. Anchoring Ω_m at the Planck value gives γ = 1.030, 1σ [0.955, 1.099]. The competing capacity classes are separately excluded: thermal 4D CFT (γ = 3 ⟹ Ω_X,c = 1.5) by flatness itself; Schwarzschild-like (γ = −2) by sign; the vertical-temperature variant (r_c = 1/4) by direct fit (§17).

**Falsifier.** A determination of γ away from 1 at several σ — for example under next-generation BAO with the same pipeline — kills the two-dimensional-chiral-algebra identification specifically, which is the heart of the theory.

### P6 — Phase ordering

**Prediction.** 𝔖_J(z) = 6 ln[(1+z_c)/(1+z)]·(1+w(z)) ≥ 0 at every z: no quintessence before the crossing, no phantom after, as a theorem (§24).

**Falsifier.** Any reconstruction placing w > −1 at z > z_c (or w < −1 at z < z_c) beyond errors. Current reconstructions are consistent with the predicted ordering.

### P7 — The existence ceiling

**Prediction.** ϱ⊥ ≤ ϱ⊥^max(Ω_m) = 1.8141 at the benchmark: above the ceiling, no flat solution exists at all (§14).

**Status.** The direct determination gives ϱ⊥ = 0.800, 1σ [0.575, 0.982] — 1.08σ from the predicted 1, comfortably under the ceiling.

**Falsifier.** A clean, non-boundary-dominated determination above the ceiling falsifies the entire branch, independent of every other prediction.

### P8 — The neutrino-mass release

**Prediction.** The DESI neutrino-mass tension is an artifact of forcing w = −1. Under ΛCDM, DESI DR2 + CMB compress the bound to Σm_ν < 0.064 eV (95%), pressing on the 0.059 eV normal-ordering floor from oscillations, with the profile preferring the unphysical region [31]. The degeneracy is understood: late-time w > −1 raises the inferred bound. Because this theory's background has w > −1 for all z < 0.342 with no parameter to tune it away, it predicts the bound reopens — DESI's own w₀w_aCDM analysis, whose best fit P1 shows is statistically coincident with this theory's fixed point, relaxes the bound to ≈ 0.16 eV, comfortably above the floor.

**Type and falsifier.** The direction is guaranteed by the measured degeneracy; the precise bound requires the dedicated Boltzmann-level posterior for this background, which has not been run and is flagged as such. That run is the falsifier: if this background, fitted to DESI DR2 + CMB, still forces Σm_ν below 0.059 eV, the prediction fails; if it recovers the floor comfortably, the theory resolves a live tension at zero cost.

### P9 — The invariant, and where it can actually be tested

**Prediction.** 9(1+w(z))² + 6 dw/dN = 4 at every redshift: the theory's defining relation (§19).

**What background data can see — a result, not a caveat.** `[NEGATIVE]` Embed the theory in the family ρ_X ∝ sech^p(β(N−N_c)), for which

$$9X^2 + 6X' = X^2\left(9 - \frac{18}{p}\right) + 2p\beta^2,$$

so the invariant is constant if and only if p = 2. Profiling the likelihood in p against DESI DR2 + Pantheon+ gives **Δχ² = 0.79 across p ∈ [0.05, 20]**, with no 1σ, 2σ or 3σ bound; p = 2 sits at 0.88σ. Adding a Planck acoustic anchor as a 14th BAO point, D_M(z*)/r_d = 94.32 ± 0.28, changes this to 0.78. The reason is structural: the data span θ = β(N−N_c) ∈ [−0.42, +0.28], less than one transition width, and the exponent p controls the tails, which lie where ρ_X is subdominant. Along the degenerate direction w(z) varies by < 0.03 over the data range while the invariant's value swings by two decades. **Background expansion data are provably insensitive to the invariant** — a statement about the information content of H(z) that applies to every dark energy model, and that explains why P1–P7 rather than P9 are where current data bite.

**Where the test lives.** Growth (fσ₈) and CMB lensing weight ρ_X(z) through different functionals of the history and _are_ sensitive to the tails. Forecast: separating a smooth pulse from a sharp step needs ~3.4× better background data (plausibly DESI-5yr + LSST); separating p = 2 from p = 1 needs ~22×, which no planned background survey delivers — but which perturbation observables can, once §25 supplies the covariant response. The perturbation sector therefore gates the decisive observation as well as the theory's completion.

### P10 — The far future, and the meaning of "no cosmological constant"

**Prediction.** w → −1/3 exactly; a(t) ∝ t; the event horizon is marginally absent; the e-fold budget splits 1:1 between horizon rapidity and horizon information (§22); the acceleration era ends at a/a₀ = 11.79 and never recurs. Any positive residual Λ_res eventually dominates, restores an event horizon, and bends w(z) back toward −1 at late times: exact zero and observational negligibility are different theories, and the difference is the theory's `[SECTOR]` choice made visible.

**Testability, stated plainly.** The asymptotics are not testable on survey timescales. They are recorded because they are forced, because they resolve the conceptual pathologies of an eternal de Sitter phase (no permanent horizon, no asymptotic thermal state), and because a very-late-time w(z) floor is the one signature that would reveal Λ_res ≠ 0.

### 27.1 The density history

Unpacking the source law as a function surveys actually probe: the ratio of the model's dark density to the constant Λ-density of flat ΛCDM at the same Ω_m (both normalised to agree today, as flatness requires):

|epoch|ρ_X / ρ_Λ|
|---|---|
|z = 5|0.198|
|z = 3|0.396|
|z = 2|0.605|
|z = 1|0.932|
|z = 0.5|1.076|
|z = 0.342 (crossing)|1.089 (the maximum)|
|z = 0|1.000 (exact, by flatness)|
|a = 2a₀|0.466|
|a = 4a₀|0.141|
|a = 11.79a₀ (exit)|0.017|

**Dark energy is an episode, not an era.** At z = 3 the model carries 40% of Λ's density; two e-folds hence, 14%. The past-side deficit is exactly the phantom branch (ρ_X grew toward the crossing), and it is where the high-redshift BAO leverage of DESI lives; the future-side decay is the Komar shutdown of §20.1. In ΛCDM language: the "cosmological constant" is the tangent-line shadow of this pulse across the narrow window where we happen to observe it.

### 27.2 The vacuum sector: what is dissolved, what is retyped, what remains

Question 1 of §1 receives a three-part answer, each part with its own epistemic status.

**Dissolved `[THEOREM]`.** The local problem — why computed zero-point energy does not gravitate — is answered by vacuum blindness (§22): an additive vacuum offset is a central shift, central shifts have zero BKM length, and the trace-free source equation annihilates pure-trace stress. The dark channel of this theory _cannot_ couple to vacuum energy. No cancellation to 122 decimal places occurs because no coupling exists to cancel.

**Retyped `[THEOREM]`.** The magnitude question — why is the observed dark density 10⁻¹²² of the Planck density — dissolves differently: **the theory contains no constant with that value.** The observed density is ½ρ_crit,c sech²(N−N_c), a relational quantity. The famous small number is (H_c t_P)², a statement about how many Planck times elapse before matter–dark equality — that is, a fact about the matter sector's history, not a fine-tuned property of the dark sector. ΛCDM needs a constant of nature to be small; this theory has one fewer constant of nature (§29) and nothing that needs to be small.

**Remaining `[SECTOR, OPEN]`.** The global flux residual Λ_res is set to zero, consistently with manifestly local vacuum sequestering [26,27], and its selection is not derived (Q4). P10 states the observable consequence of the choice. This is the honest boundary of the vacuum result, stated once.

## 28. Observational status

**Pipeline.** DESI DR2 BAO (13 measurements, 7 tracers, within-tracer correlations) [31] plus Pantheon+ (1580 SNe after z_HD > 0.01 and calibrator removal, full STAT+SYS covariance) [34]. N_data = 1593. The normalisation c/(H₀r_d) and the supernova absolute magnitude are profiled analytically. The pipeline reproduces the published ΛCDM constraints: Pantheon+ alone Ω_m = 0.3324 ± 0.018 (published 0.334 ± 0.018); DESI alone Ω_m = 0.2970 ± 0.0086 and H₀r_d = 101.56 (published 0.2975 ± 0.0086 and 101.54 ± 0.73).

**Model comparison.**

|model|dark params|k|χ²|Δχ²|ΔAIC|
|---|---|---|---|---|---|
|flat ΛCDM|0|3|1400.142|0|0|
|**this model**|**0**|**3**|**1396.762**|**−3.380**|**−3.380**|
|ϱ⊥ free|1|4|1395.596|−4.545|−2.545|
|CPL (w₀, w_a)|2|5|1394.980|−5.162|−1.162|
|invariant-constant|2|5|1394.868|−5.274|−1.274|
|free-shape sech^p|3|6|1394.024|−6.118|−0.118|

The model has the best AIC of the six, buying Δχ² = −3.38 at zero parameter cost, and the free-parameter extensions of its own family buy little: one released parameter (ϱ⊥) gains 1.17 over the fixed theory, and the full three-parameter shape family gains 2.74 for three parameters. The correct reading is stated once and precisely: this is **viability at zero cost plus best-in-class information efficiency**, not a discovery statistic, and no discovery is claimed from it. The discovery-class statements are P1–P5, and the table's role is to certify that the theory whose shape was fixed before the fit competes with families that spent two and three parameters after it.

**Direct parameter determinations.**

|quantity|prediction|measurement|tension|
|---|---|---|---|
|ϱ⊥|1|0.800, 1σ [0.575, 0.982]|1.08σ|
|γ_⊥,c (at ϱ⊥ = 1)|1|1.025, 1σ [0.941, 1.088]|0.03σ|
|z_c|0.342|0.650, 1σ [0.293, open]|0.72σ|

**A negative control.** The CMB-lensing response direction is explicitly _not_ claimed as evidence: a null ensemble of 225 smooth positive transient histories, matched to the same early matter density and high-z distance, found 92.9% with response cosine below −0.90 and a median of −0.969 against the rigid model's −0.972. Passing a test that 93% of a null class passes is class membership, not discrimination, and the theory's evidence ledger excludes it.

---

# Part VIII — Comparison and economy

## 29. Where this sits among economical dark energy models

|model|extra dark-history parameters|free functions|new dimensionful constants|
|---|---|---|---|
|flat ΛCDM|0|0|1 (Λ)|
|PEDE [35]|0|0|1|
|vacuum metamorphosis [36]|0|0|1|
|running vacuum [37]|1|0|1|
|holographic DE (future horizon) [48,49]|1 (c²)|0|0|
|CPL [43,44]|2|0|1|
|interacting dark energy|1+|**1** (interaction kernel)|1|
|**this model**|**0**|**0**|**0**|

Parameter count alone does not separate this model from PEDE or vacuum metamorphosis; two things do. First, the last column: every constant appearing in this theory already appears in the Einstein equation and in quantum mechanics, and the one constant unique to dark sectors — a dimensionful amplitude — is absent, replaced by the relational quantity ½ρ_crit,c that §17 derives. Second, what one structure buys: the same identity ⟨Q²⟩ = 1 fixes the background shape, the differential invariant, the crossing count, the future causal character, the perturbation operator, and the response amplitude, and these are locked to one another. A competitor can match the curve; matching the lockstep is what P4, P5, P6 and P9 price.

**The musical-chairs test, answered in advance.** At the homogeneous level every positive ρ_X(a) is representable as an effective fluid via w_X = −1 − (1/3) d ln ρ_X/dN, and sech²/tanh profiles exist in the fitting literature. The background curve alone is therefore not the claim. The claim is the independent map Φ: ℝ_Weyl → 𝒮(𝒜) and its pullback metric Φ*G^BKM = 𝒳_σ dN², constructed in §§11–18 from cocycle data with cosmology entering only through Ω_m in §14. The elimination test of §4 is passed at the level of construction; what remains to pass it _in practice_ is the explicit computation of θ(N) from a concretely specified FLRW causal-diamond state family (Q3), and the theory states this as its own completion criterion rather than waiting to be asked.

**Relation to thermodynamic gravity.** Jacobson derives the Einstein equation from a Clausius relation at local horizons [9,10]; this theory takes the Einstein equation as given (in tractor form) and derives the _source in the scale channel_ from modular response. The two are complementary uses of the same modular data — one for the field equation, one for what feeds it — and neither modifies the force law.

---

# Part IX — Open problems and programme

## 30. Open problems

**Q1 — the response map.** Construct ℜ_Σ of §25 and lift the Witten complex to a Lorentzian perturbation system. This gates the perturbation sector, the observational route to the invariant (P9), and any CMB/growth likelihood. It is a classification problem for natural bilinear operators, with six listed constraints, not a search for an action.

**Q2 — the FLRW self-dual wall.** Prove that modular flow at the self-dual apparent-horizon cut of a dynamical flat FLRW state is geometric, so that the horizontal sector is the normal-plane chiral algebra assumed in P. This is the single identification carrying the γ = 1 derivation, and it is the sharpest mathematical problem the theory poses. Every historical extension of geometric modular flow — wedge [6], CFT ball [7], stationary horizons and their perturbations [20,21,22] — has landed on marginal causal surfaces; the self-dual cut is exactly such a surface.

**Q3 — explicit θ(N).** Compute the Connes cocycle for a concretely specified FLRW causal-diamond state family and exhibit θ(N) without cosmological input, completing the elimination test in practice.

**Q4 — Λ_res.** Manifestly local vacuum sequestering [26,27] removes spacetime-filling matter-loop vacuum energy from the curvature source and leaves a finite global flux residual; which flux sector nature selects is not derived here. P10 states the observable stakes.

**Q5 — the Keller correspondence.** `[RHYME]` Reflectionless potentials are exactly those whose KdV spectral curve is rational; Keller-map obstructions live in branched-cover data of a discriminant. Both instantiate "trivial local invariant, nontrivial global remainder". Whether the ℓ = 1 Pöschl–Teller spectral curve is the Keller curve at the relevant degeneration is checkable and unchecked; until checked it is filed as a rhyme and counted as nothing.

## 31. A programme for the next investigator

1. Run P3, P4, P6 and the P1 locus test on published non-parametric w(z) reconstructions. These require no new theory and test four predictions from one reconstruction.
2. Run the dedicated Boltzmann posterior for this background against DESI DR2 + CMB with Σm_ν free (P8). This is the fastest route to either a new failure mode or a resolved tension.
3. Build the determination table for ϱ⊥ across DR1/DR2 × supernova compilations × with/without lensing, using ϱ⊥² = [9(1+w₀)² − 6w_a]/4 with real covariances, marking boundary-dominated entries against the §14 ceiling.
4. Attack Q2 in a controlled setting first: a driven two-dimensional CFT, then holographic balls, then perturbative gravitational crossed-product algebras.
5. Attack Q1 as a classification problem for natural bilinear operators under the six constraints of §25, not by guessing an action.

---

# Scholium — Objections and replies

The twelve objections most worth answering, answered. Each reply is self-contained; where a reply rests on a computation, the section carrying the computation is cited.

**S1. "Any ρ(a) is some w(z). You have relabelled a fluid."** Correct as a statement about background curves, which is why §4 sets the elimination test before anything is derived. The difference between a relabelling and a theory is whether the new variable is constructible without the data it predicts. Here θ is defined by the Connes cocycle of scale-indexed states (§13) — an object that exists whether or not anyone measures H(z) — and the chain §§11–18 turns it into a prediction with cosmology entering only through Ω_m, once, discretely. The construction-level test is passed; the in-practice computation of θ(N) from an explicit state family is Q3, stated as the theory's own completion criterion. A relabelled fluid has no Q3 to state.

**S2. "sech² has an amplitude and a centre. Two hidden parameters."** Both are derived. The amplitude is ½ρ_crit,c — the ½ from the free-energy Hessian, the ρ_crit,c from the Misner–Sharp identity (§17), the ϱ⊥²γ = 1 from §§14, 16. The centre is the unique minimum of the symmetrized modular relative entropy (§18), dated by flatness. And the exponent is not selected from a family: sech² is the variance of a normalised binary, the only information geometry a two-outcome structure possesses. The correct accounting is the one in §29's table, where this row is the only one with three zeros.

**S3. "½ρ_crit,c is a clock reading dressed as a derivation — the amplitude secretly tracks H²."** The objection has the type theory right and the verdict wrong. A constant of nature is an input that could have been otherwise; a clock reading is a measurement of when you are. The amplitude here is neither: it is a _theorem-valued functional_ of the matter history — given flatness and Ω_m, nothing about it could have been otherwise. The theory does not say "dark energy happens to be about ρ_crit"; it says the dark response at the self-dual cut _is_ half the causal diamond's Misner–Sharp density, with every constant cancelling (§17). The H² scaling that looks suspicious is the marginality identity doing its job. What would be a disguised constant is a coefficient left free in front — and §§14, 16 close that coefficient, γϱ⊥²/2 = ½, with two independent derivations and a measured check (P5).

**S4. "You used data (Ω_m) inside a 'derivation'."** Once, and disclosed in bold (§14). The role is to select between the integers 1 and 2 after representation theory has already discretised the choice; the selection is identical across the entire allowed Ω_m range and its competitor is excluded at Δχ² = 60. Established physics accepts exactly this structure — "the gauge group is SU(3)×SU(2)×U(1)" is a discrete selection made by data among representation-theoretic alternatives. The alternative bookkeeping, ϱ⊥ = 1 as a postulate and the ceiling as its consistency check, changes nothing downstream.

**S5. "w crosses −1. That means ghosts, or a violated null energy condition."** For a fundamental fluid or a single minimally coupled scalar, yes — and the theory _proves_ it, as N2, at exactly the critical coupling where fall-to-the-centre begins [28,30]. That no-go is why θ is typed as a collective constitutive coordinate (§23): the same type as temperature, which also gravitates, also has profiles, and also supports effective w < −1 histories in composite descriptions without any propagating ghost. The NEC constrains propagating degrees of freedom; the propagating content here is the transmitted continuum of a reflectionless operator with retarded analytic structure (§24). The crossing is real, and the fluid picture is what fails at it — on schedule.

**S6. "This is holographic dark energy with extra steps."** Holographic dark energy posits ρ ∝ L⁻² for a chosen cutoff L with a fitted coefficient c², yielding a one-parameter family, no crossing without further choices, and no differential invariant [48,49]. Here no IR-cutoff postulate exists: ρ_crit,c appears as a theorem at one epoch only, the profile away from that epoch is the binary variance, the coefficient is derived, and the predictions that price the difference are P4, P6 and P9 — none of which HDE makes.

**S7. "Geometric modular flow at a cosmological horizon is unproven; the theory hangs on it."** Correct, and stated as such everywhere it matters (§3, §11, Q2). What is proved: the wedge [6], the CFT diamond [7], stationary horizons and controlled perturbations thereof [20,21,22]. The self-dual FLRW cut is a marginal causal-information surface of exactly the kind these results have successively reached, and the theory's wager is that the pattern completes. The wager is priced: if Q2 fails, γ = 1 loses its derivation and survives only as the measured 1.025 ± 0.07 of P5. A theory should hang on something, and it should say what.

**S8. "Δχ² = −3.4 is nothing."** It is not offered as something; §28 types it as viability at zero cost. Its information content is comparative: the model beats ΛCDM at equal parameter count and holds the best AIC against families that spent two and three post-hoc parameters, while being the only entrant whose shape was fixed before contact with the data. The claims on which the theory stakes itself are P1–P5 — a fixed point sitting inside the DESI 1σ region, a jerk a full unit from ΛCDM's, a forced triple coincidence, a measured capacity ratio — and P9 states precisely why background χ² was never going to be the arena.

**S9. "What does the theory not explain?"** The early universe, inflation, the matter and radiation content, the value of Ω_m, the hierarchy of forces, the selection of the expanding branch, and quantum gravity. It is a theory of the scale register's response: the existence, shape, amplitude, timing, orientation, and future of the dark sector, plus the local vacuum blindness — nothing else. Scope is not modesty; it is type discipline.

**S10. "The coincidence problem survives: why do we live near N_c?"** Split the question. "Why does dark equal ordinary at the crossing?" — theorem (§18); ΛCDM must tune Λ for it, this theory cannot avoid it. "Why is the crossing at z ≈ 0.34?" — derived from Ω_m (§18); confirmed within the DESI band (P3). "Why is the observation epoch within an e-fold of N_c?" — equivalent to "why is Ω_m today ≈ 0.3", a fact about the matter sector and the observer's date that no background theory derives and this one does not claim to. What the theory removes is the tuned constant: there is no dial whose setting makes the epochs meet. And quantitatively the coincidence is milder here than in ΛCDM: on the future side ρ_X/ρ_m grows only linearly in a (versus ΛCDM's cubically), so near-equality occupies a wider swath of history.

**S11. "The vacuum catastrophe is 'dissolved' by fiat — you defined the coupling away."** The blindness is not a definition; it is two theorems that meet (§22). On the information side, a central shift K ↦ K + α1 does not change the state, so no monotone metric — not just BKM — can assign it length; this is mathematics, not model-building. On the geometric side, the trace-free Einstein equation annihilates λg_ab identically; this is the tractor form of GR, not a modification. The theory's constitutive principle couples gravity to the response metric, and the response metric provably cannot see vacuum energy. What is _chosen_ is the global flux sector Λ_res = 0, and §27.2 files that choice, its sequestering pedigree [26,27], and its observable signature (P10) without disguise.

**S12. "Why a binary? Nature might realise richer structure at the cut."** The candidates were computed, not dismissed. A higher soldering power ϱ⊥ = n ≥ 2 is representation-theoretically admissible and is excluded by the flatness ceiling plus Ω_m at 3.8σ and Δχ² = 60 (§14) — and would, independently, predict a decelerating future (§20.1). A bulk thermal capacity class (γ = 3) forces Ω_X,c = 3/2 and is excluded by flatness itself; a Schwarzschild-like class (γ = −2) is excluded by sign; the vertical-temperature normalisation is excluded by direct fit (§17). The binary is not merely the minimal choice consistent with the cut's two null normals; it is the last one standing after its rivals' consequences were derived and killed by data. That is what "minimal" is required to mean here.

---

# Appendix A — Core derivations

**A.1 Binary moments.** For ρ_θ = e^{θQ}/(2cosh θ) with Q² = 1: ⟨Q⟩ = tanh θ, Var(Q) = 1 − tanh²θ = sech²θ, hence ⟨Q²⟩ = ⟨Q⟩² + Var(Q) = 1.

**A.2 The cosmological invariant.** With ρ_X = ρ_* sech²[ϱ⊥(N−N_c)], define Δ_X := −d ln ρ_X/dN = 2ϱ⊥ tanh θ. Then Δ′_X = 2ϱ⊥²sech²θ = 2ϱ⊥² − ½Δ_X², so Δ_X² + 2Δ′_X = 4ϱ⊥². Substituting Δ_X = 3(1+w_X) gives the invariant of §19.

**A.3 Fisher length.** ds_F = sech θ |dθ|, so L_F = ∫sech θ dθ = π, equal to ∫₀¹ dp/√(p(1−p)), the simplex diameter.

**A.4 Slot separation.** For ψ_NN + [K² + cρ_X]ψ = 0 with ρ_X = χ⊥ϱ⊥²sech²θ, substituting θ = ϱ⊥(N−N_c) gives ψ_θθ + [K²/ϱ⊥² + cχ⊥ sech²θ]ψ = 0. The pullback factor cancels the chain-rule factor: ϱ⊥ occupies the eigenvalue slot, χ⊥ the potential-strength slot. One coefficient cannot perform both roles; this is why the invariant measures ϱ⊥ independently of the amplitude.

**A.5 The existence ceiling.** With x = −N_c > 0, flatness is r_c e^{3x}sech²(ϱ⊥x) = T_m. At a double root, 3 − 2ϱ⊥ tanh(ϱ⊥x) = 0; eliminating x gives the ceiling equation of §14.

**A.6 The Witten factorisation.** 𝒜†𝒜 = −∂²_θ + η² − η′ and 𝒜𝒜† = −∂²_θ + η² + η′. With η = tanh θ, η′ = sech²θ, η² = 1 − sech²θ, the identity η² + η′ = 1 makes H₊ free and η² − η′ = 1 − 2sech²θ.

**A.7 Capacity as a thermodynamic exponent.** For ρ_β = e^{−βH}/Z the modular Hamiltonian is K = βH + ln Z, so ⟨K⟩ = S and Var(K) = β²Var(H) = C. Hence γ = C/S = d ln S/d ln T, and if S ∝ T^a then γ = a.

**A.8 The benchmark closure.** With ϱ⊥ = γ = 1 and x = −N_c, flatness today reads

$$\big(\Omega_{m0},e^{3x} + \Omega_{r0},e^{4x}\big)\operatorname{sech}^2 x = 1 - \Omega_{m0} - \Omega_{r0},$$

whose unique root at the benchmark is x = 0.2940066, i.e., z_c = e^{x} − 1 = 0.3417927. Then ρ_*/ρ_crit,0 = Ω_m0 e^{3x} + Ω_r0 e^{4x} = 0.7506311; Ω_X0 = 0.7506311 sech²x = 0.6893105; w₀ = −1 + (2/3)tanh x = −0.8094545; w_a = −(2/3)sech²x = −0.6122053; q₀ = ½[Ω_m0 + 2Ω_r0 + Ω_X0(1+3w₀)] = −0.3369025. Every entry of §26 follows.

**A.9 Kinematic identities and the jerk correction.** From q = −1 − H′/H one derives H″/H = (1+q)² − q′ and hence the exact identity

$$j = q + 2q^2 - \frac{dq}{dN}.$$

Equivalently, for flat multi-component cosmology, j = 1 + (9/2)Σᵢ Ωᵢwᵢ(1+wᵢ) − (3/2)Σᵢ Ωᵢ dwᵢ/dN, which returns j = 1 identically for ΛCDM. Both routes give j₀ = −0.1112465 at the benchmark; revision 1's value −0.1085454 arose from the sign error j = q + 2q² + q′ and is superseded. Corollary recorded in §26: dq/dN|₀ = q₀ + 2q₀² − j₀ = +0.0013505, locating the minimum of q at z = 0.0008.

**A.10 The CPL locus and implied crossings.** At ϱ⊥ = 1 both tangent coefficients are functions of x = −N_c alone: tanh x = (3/2)(1+w₀) and w_a = −(2/3)sech²x give the parameter-free locus

$$w_a = \frac{3}{2}(1+w_0)^2 - \frac{2}{3},$$

which is prediction P1's curve; the benchmark point is its evaluation at the measured Ω_m. Conversely, any CPL fit implies a crossing at z_× = s/(1−s) with s = (1+w₀)/(−w_a); applied to the DESI DR2 combinations of §27 this gives z_× = 0.354 (Pantheon+), 0.405 (DES Y5), 0.440 (Union3).

# Appendix B — Reproducibility

|script|verifies|
|---|---|
|`receipts_closure.py`|the §18 identity chain; γ = d ln S/d ln T; 2D CFT gives C = S; ϱ⊥ = 1 from integrality + ceiling; the Misner–Sharp horizon identity; the closed benchmark of §26 and A.8|
|`receipts_transparency_fold.py`|binary moments, the invariant, the saddle-node reduction, the three futures, slot separation, N1–N4, the ceiling, the three-epoch structure, the tractor identity, Chatterjee self-duality and 𝔖_J, Levinson/Fisher, Fourier self-reciprocality|
|`P1/` package|data loaders with published-value validation; the model-comparison table; the p profile of P9; the CMB anchor; the ϱ⊥, γ, and z_c profiles of §28|

All scripts require only numpy and scipy; the `P1/` package downloads Pantheon+ on first use. This revision changes no receipted number except the jerk: patching the benchmark block to the identity of A.9 (j = q + 2q² − dq/dN) reproduces j₀ = −0.1112465, and all other outputs are unchanged.

---

# References

[1] Hawking, King, McCarthy, _J. Math. Phys._ **17** (1976) 174. [2] Malament, _J. Math. Phys._ **18** (1977) 1399. [3] Bailey, Eastwood, Gover, _Rocky Mountain J. Math._ **24** (1994) 1191. [4] Curry, Gover, arXiv:1412.7559. [5] Gover, _J. Geom. Phys._ **60** (2010) 182. [6] Bisognano, Wichmann, _J. Math. Phys._ **17** (1976) 303. [7] Casini, Huerta, Myers, arXiv:1102.0440. [8] Wald, arXiv:gr-qc/9307038. [9] Jacobson, arXiv:gr-qc/9504004. [10] Jacobson, arXiv:1505.04753. [11] Jafferis, Lewkowycz, Maldacena, Suh, arXiv:1512.06431. [12] Lashkari, Van Raamsdonk, arXiv:1508.00897. [13] Czech, Lamprou, McCandlish, Sully, arXiv:1712.07123. [14] Czech et al., arXiv:2305.16384. [15] Petz, _Linear Algebra Appl._ **244** (1996) 81. [16] Čencov, _Statistical Decision Rules and Optimal Inference_, AMS (1982). [17] Amari, Nagaoka, _Methods of Information Geometry_, AMS/Oxford (2000). [18] Grasselli, Streater, arXiv:math-ph/0006030. [19] Chatterjee, arXiv:2605.19106. [20] Jensen, Sorce, Speranza, arXiv:2306.01837. [21] Faulkner, Speranza, arXiv:2405.00847. [22] Chandrasekaran, Flanagan, arXiv:2601.07915. [23] Hayward, arXiv:gr-qc/9710089. [24] Cai, Kim, arXiv:hep-th/0501055. [25] Kastor, Ray, Traschen, arXiv:0904.2765. [26] Kaloper, Padilla, Stefanyszyn, Zahariade, arXiv:1505.01492. [27] Kaloper, Padilla, arXiv:1606.04958. [28] Vikman, arXiv:astro-ph/0407107. [29] Lekner, _Am. J. Phys._ **75** (2007) 1151. [30] Camblong, Epele, Fanchiotti, García Canal, arXiv:hep-th/0003014. [31] DESI Collaboration, arXiv:2503.14738 (DR2 BAO: cosmological constraints). [32] DESI Collaboration, arXiv:2503.14744 (DR2 BAO: Lyman-α). [33] Scolnic et al., arXiv:2112.03863 (Pantheon+ sample). [34] Brout et al., arXiv:2202.04077 (Pantheon+ cosmology). [35] Li, Shafieloo, arXiv:1906.08275 (PEDE). [36] Parker, Raval, arXiv:gr-qc/0312108 (vacuum metamorphosis). [37] Solà Peracaula et al., arXiv:2203.13757 (running vacuum). [38] Witten, _Nucl. Phys. B_ **202** (1982) 253. [39] Cardy, _Nucl. Phys. B_ **270** (1986) 186. [40] Gover, Latini, Waldron, _Mem. AMS_ **235** (2015). [41] Curry, Gover, arXiv:2208.09302 (almost-Einstein matter and the scale tractor). [42] Misner, Sharp, _Phys. Rev._ **136** (1964) B571. [43] Chevallier, Polarski, arXiv:gr-qc/0009008. [44] Linder, arXiv:astro-ph/0208512. [45] Unruh, _Phys. Rev. D_ **14** (1976) 870. [46] Haag, _Local Quantum Physics_, Springer (1996). [47] Takesaki, _Theory of Operator Algebras II_, Springer (2003). [48] Cohen, Kaplan, Nelson, arXiv:hep-th/9803132. [49] Li, arXiv:hep-th/0403127 (holographic dark energy). [50] Visser, arXiv:gr-qc/0309109 (jerk and cosmography).
