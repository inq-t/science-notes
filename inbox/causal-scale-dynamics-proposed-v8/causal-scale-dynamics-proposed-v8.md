# Causal Scale Dynamics

## Modular information geometry, horizon capacity, and the Ruble equations

**Thomas Ruble — 21 August 2026 — v8.0 (unified master)**

---

**Status.** Working master research note. Not peer reviewed. This document supersedes and consolidates two lineages:

|superseded document|what v8.0 takes from it|
|---|---|
|_Causal Scale Dynamics_ v7.0 + _Ruble Equations Reference_ (21 Aug 2026)|the Ruble-equation organisation R1–R14; the Scale–Capacity Equivalence Principle ℜ_c = 1; the adversarial audit rejecting two Revision-2 derivations; the vertical/horizontal clock split and the horizon index μ_A; the general-dimension corollary; the time taxonomy; the four economies|
|_Scale as a Modular Observable_, Revision 2 (21 Aug 2026)|the self-contained primers; the full derivation chain and no-gos; the quantitative prediction ledger P1–P10 with the validated DESI DR2 + Pantheon+ pipeline; the existence ceiling; the Fisher/Gudermannian geometry; the Scholium; the appendix derivations and receipts discipline|

Nothing in either parent remains authoritative where this document differs.

**Cumulative correction record.** Corrections are absorbed in place and indexed here, most recent first.

- **C5** — the v7.0 background χ² table (1401.63 / 1398.29 / 1397.26) is an earlier baseline run; §28 replaces it with the validated pipeline of Revision 2 (1400.142 / 1396.762 / …). The two runs agree on Δχ² ≈ −3.4 at equal parameter count; the earlier run is filed, not used.
- **C4** — v7.0 §7.3 cited the sequestering construction as [26,27], which in its own list are capacity papers; the correct references are Kaloper et al. Corrected here ([26,27] in this document's numbering, which is the Revision-2 list).
- **C3** — **withdrawn:** Revision 2 §16(b) derived the capacity ratio γ = 1 by treating the horizontal sector as a two-dimensional chiral CFT and applying Cardy's formula. A two-dimensional Lorentzian normal _plane_ is a fiber, not a 1+1-dimensional conformal field theory; the derivation is invalid. Autopsy and surviving remnants in §31.3. Replaced by the Scale–Capacity Equivalence Principle R7 `[PRINCIPLE]`.
- **C2** — **withdrawn:** Revision 2 §14(a) derived ϱ⊥ ∈ ℤ from conformal-weight integrality of the null-pair grading. Density bundles 𝓔[w] exist for every real w; the characters of the positive scale group form a continuum; there is no integrality theorem. Autopsy and surviving remnants in §31.2. Replaced by the fundamental-representation postulate R6 `[PRINCIPLE]`.
- **C1** — Revision 1's jerk j₀ = −0.1085454 arose from the sign error j = q + 2q² + q′; the correct identity is j = q + 2q² − dq/dN, giving j₀ = −0.1112465 (Appendix A.9). Corrected in Revision 2, retained here.

**Notation changes in v8.0.** The Revision-2 symbol γ (capacity-to-entropy ratio) is retired; its operational content is the Ruble number ℜ_c, and every measurement row is relabelled accordingly. The Revision-2 perturbation response map, formerly written with the same fraktur letter, is renamed 𝓡_Σ to reserve ℜ exclusively for the Ruble number.

**Gating decision closed.** The v5.0 master carried two incompatible specifications of the modular–Weyl coefficient and posed three exits. Exit 2 — decouple the horizontal state rapidity θ from the vertical geometric rapidity η_A — is the one taken, implemented by the vertical/horizontal split of §5 and §19, with the exact residual relation θ′ − η′_A = ¼ (ln 𝒮_A)′. The companion objection, that the amplitude was a disguised clock reading, is resolved by anchoring the amplitude at the intrinsic self-dual event (§12, S3). The decision is recorded as closed in §31.6.

**Label taxonomy.** Every load-bearing statement carries one of:

|label|meaning|
|---|---|
|`[STANDARD]`|established mathematics or physics, cited|
|`[THEOREM]`|proved here from stated hypotheses; receipts verify|
|`[CONDITIONAL]`|theorem given explicitly named unproved hypotheses|
|`[PRINCIPLE]`|declared physical law; not a theorem; falsifiable|
|`[IDENTIFICATION]`|structural identification of two mathematical objects|
|`[DEDUCTION]`|follows from laws + principles above it|
|`[SECTOR]`|global choice among mathematically admissible sectors|
|`[ANALYSIS]`|data analysis performed for this programme; scripts filed|
|`[NEGATIVE]`|proved impossibility or null result|
|`[OPEN]`|posed, not solved|
|`[RHYME]`|structural analogy; counted as nothing|

**Scope.** The homogeneous theory is closed: two declared unit laws and one global sector choice determine the entire late-time background with zero free functions and zero fitted constants. The covariant perturbation theory and the global vacuum sector are open research layers, not unfixed background parameters. The declared baseline is four-dimensional spatially flat FLRW with radiation, pressureless matter, one collective scale-capacity response, and an exactly zero residual late-time floor. Observational comparisons are background-level or response-level `[ANALYSIS]`, not a joint Boltzmann likelihood.

---

## How to read this document

Twelve steps, each usable without the others.

1. **§1** states the theory as fourteen equations (the Ruble equations) and one table separating law from solution data from measurement.
2. **§2** isolates the two structural unit laws — width and amplitude — and gives each its logical status, its precedents, its existence ceiling, and its measured value. This is the chapter to test the theory against.
3. **§§3–7** are self-contained primers: six notions of time, tractor calculus, vertical versus horizontal modular geometry, information geometry, conventions. A reader with the background skips them.
4. **§§8–14** are the derivation chain, each link labelled.
5. **§§15–19** solve the dynamics exactly: the invariant, the phase flow, the chronology, the Fisher geometry, the vertical clock budget.
6. **§§20–22** treat gravitational sourcing and the vacuum: what is dissolved, what is retyped, what remains, and what the far future is.
7. **§§23–25** give the perturbation sector: the canonical Witten pair, the four no-gos, and the stopping condition. This sector is open and says so.
8. **§§26–29** are the predictions: the closed benchmark, the ledger P1–P10 with data status, the observational pipeline, and kill conditions K1–K8, each naming the law it executes.
9. **§30** prices the theory against economical competitors.
10. **§31** is the audit record: two withdrawn derivations with autopsies, the withdrawn-claims register, and why the revised closure is stronger.
11. **§§32–33** state the open problems Q1–Q5 and the work programme.
12. The **Scholium** answers the thirteen best objections; the **appendices** carry the derivations, the receipts ledger, the epistemic ledger, and the symbol dictionary.

---

## Abstract

This note develops a formulation of gravity and cosmic history in which causal order, metric scale, modular state geometry, horizon entropy, and late-time acceleration are registers of one structure rather than unrelated inputs.

Causal order determines a Lorentzian spacetime only up to conformal scale `[STANDARD]`. The metric is a conformal class [g] plus a positive scale section σ ∈ Γ(𝓔[1]); the two-jet of σ is the scale tractor I_A = ¼D_Aσ. In four dimensions the trace-free Einstein equation is the scale-transport equation ℰ_ab(σ) = (4πG/c⁴)σT°_ab, and the trace fixes I² = (2πG/3c⁴)T − Λ_g/3: trace-free stress is the obstruction to parallel transport of scale, and the cosmological constant lives in a separate global calibration channel `[STANDARD]`.

A causal region and faithful state carry a second geometry: modular flow, relative entropy, and its Bogoliubov–Kubo–Mori Hessian. The theory separates **vertical** modular automorphism flow from **horizontal** deformation of the state family — the distinction whose absence broke v5.0. At a homogeneous codimension-two cut the normal plane supplies a canonical chirality Q = P₊ − P₋ with Q² = 1 and JQJ = −Q; the associated binary exponential family has η = tanh θ and G^BKM_θθ = sech²θ. Cocycle composition makes the horizontal coordinate affine in Weyl scale, θ = ϱ⊥(N − N_c) `[CONDITIONAL]`.

Two structural unit laws close the homogeneous theory, and this document is explicit that both are declared physical principles, not theorems of mathematics — the two Revision-2 arguments that claimed otherwise are withdrawn in §31 with full autopsies:

- **Width** `[PRINCIPLE]`: ϱ⊥ = 1 — the fundamental null-normal character is identified with the fundamental scale character; one unit of modular polarisation per Weyl e-fold.
- **Amplitude** `[PRINCIPLE]`: the Scale–Capacity Equivalence, ℜ_c := (k_B/S_c)G⊥_NN(N_c) = 1 — at the self-dual causal wall the entropy-normalised BKM speed of the state under Weyl translation is unity. Equivalently: state self-duality is budget self-duality.

With horizon thermodynamics supplying the exact dimensional bridge k_BT_c(S_c/k_B)/V_c = ρ_crit,c `[THEOREM]`, the closed source is

ρ_X(N) = ½ρ_crit,c sech²(N − N_c), w_X = −1 + ⅔ tanh(N − N_c),

with N_c fixed by flatness from the measured (Ω_m0, Ω_r0). At the crossing: Ω_X = ½, ρ_X = ρ_ordinary, and w_X = −1, simultaneously and exactly. The parameter-free differential invariant is 9(1+w_X)² + 6w′_X = 4. Acceleration begins (z = 0.786), peaks (z ≈ 0), and ends (a = 11.79 a₀) as one episode; the far future coasts with no event horizon if the global residual floor is exactly zero `[SECTOR]`.

Both unit laws are measured: ϱ⊥ = 0.800, 1σ [0.575, 0.982], against a flatness existence ceiling of 1.814; ℜ_c = 1.025, 1σ [0.941, 1.088], against an absolute ceiling of 2. The benchmark predicts (w₀, w_a) = (−0.80945, −0.61221) — inside 1σ of DESI DR2 + CMB + Pantheon+ — q₀ = −0.33690, j₀ = −0.11125 against ΛCDM's exact +1, and the background comparison gives the best AIC of six models at zero dark parameters (Δχ² = −3.38 versus flat ΛCDM). This is viability plus locked structure, not a discovery claim; the discovery-class statements are the ledger's P1–P5, and the kill conditions are K1–K8.

The theory contains no continuously fitted dark-history function, no fitted constant, two declared unit laws, and one global sector choice. The perturbation lift and the vacuum sector are the next layers, not repairs to the background.

---

# Part I — The theory in one chapter

## 1. The Ruble equations

The theory is most compactly stated as a sequence of definitions, two physical principles, and their consequences, organised by mathematical type rather than by discovery history. Sections 8–14 derive each link; this chapter is the reference card.

### 1.1 Kinematic and geometric register

**R1 — causal scale.**

$$g_{\rm phys} = \sigma^{-2}g, \qquad N = -\ln\frac{\sigma}{\sigma_c} = \ln\frac{a}{a_c}.$$

The conformal metric g fixes causal cones; the scale section σ ∈ Γ(𝓔[1]) fixes physical calibration. N is logarithmic Weyl scale, not Newtonian absolute time.

**R2 — scale tractor.**

$$I_A = \tfrac{1}{4}D_A\sigma.$$

The scale tractor packages σ, its first derivative, and the trace combination of its second derivative.

**R3 — tractor transport and norm.**

$$(\nabla_a\nabla_b\sigma + P_{ab}\sigma)_0 = \frac{4\pi G}{c^4},\sigma T^\circ_{ab}, \qquad I^2 = \frac{2\pi G}{3c^4}T - \frac{\Lambda_g}{3}.$$

The first equation is local and trace-free; the second fixes the scalar calibration channel up to a global constant.

### 1.2 Horizontal state register

**R4 — normal chirality.**

$$Q = P_+ - P_-, \qquad Q^2 = 1, \qquad JQJ = -Q.$$

P± project onto the two null lines of the Lorentzian normal plane of a codimension-two cut. The homogeneous horizontal response is assumed to factor through this fundamental chirality quotient `[IDENTIFICATION]`.

**R5 — binary exponential family.**

$$\omega_\theta = \frac{e^{\theta Q}}{2\cosh\theta}, \qquad \Psi(\theta) = \ln(2\cosh\theta),$$

$$\eta = \Psi'(\theta) = \tanh\theta, \qquad G^{\rm BKM}_{\theta\theta} = \Psi''(\theta) = \operatorname{sech}^2\theta, \qquad \eta^2 + G^{\rm BKM}_{\theta\theta} = 1.$$

The last identity is the normalised binary moment relation ⟨Q²⟩ = 1.

**R6 — horizontal soldering and the width law.**

Under the rank-one ratio and measurability hypotheses, the Connes cocycle chain rule gives

$$\theta = \varrho_\perp(N - N_c) \quad \text{[CONDITIONAL]}, \qquad \boxed{;\varrho_\perp = 1;} \quad \text{[PRINCIPLE]}.$$

The affine form is derived; the coefficient is not. The unit value is the **fundamental-representation postulate**: the fundamental null-normal character is identified with the fundamental scale/inverse-scale character. It is not a theorem of Cauchy's equation and it is not obtained from an integer restriction on conformal weights (§31.2).

### 1.3 Scale-capacity closure

**R7 — the Ruble number and the amplitude law.**

Let G⊥_NN be the physical BKM norm of the selected horizontal scale tangent and S_c the horizon entropy of the self-dual wall. Define

$$\Re_c := \frac{k_B}{S_c},G^\perp_{NN}(N_c).$$

The **Scale–Capacity Equivalence Principle** is

$$\boxed{;\Re_c = 1;} \quad \text{[PRINCIPLE]}, \qquad \text{equivalently} \qquad \frac{k_B}{S_c}G^\perp_{NN}(N) = \operatorname{sech}^2(N - N_c).$$

One Weyl e-fold moves the state, at self-duality, through exactly one horizon-entropy unit of squared BKM distance: the fundamental scale translation is isometric to the fundamental state translation when the state metric is normalised by horizon capacity.

**R8 — modular free-energy source.**

$$\rho_X(N) = \frac{k_BT_c}{2V_c},G^\perp_{NN}(N).$$

The constitutive law: dimensionless relative-entropy curvature is converted to energy density by the physical modular temperature and the causal-wall volume. The ½ is the Taylor coefficient of relative entropy at coincidence.

**R9 — Hawking–Friedmann conversion.**

For a flat four-dimensional FLRW apparent horizon,

$$R_c = \frac{c}{H_c}, \qquad \frac{S_c}{k_B} = \frac{\pi R_c^2c^3}{G\hbar}, \qquad k_BT_c = \frac{\hbar c}{2\pi R_c},$$

$$k_BT_c,\frac{S_c}{k_B} = E_{\rm MS,c} = \rho_{\rm crit,c}V_c.$$

**R10 — closed source.**

Combining R7–R9,

$$\boxed{;\rho_X(N) = \tfrac{1}{2}\rho_{\rm crit,c}\operatorname{sech}^2(N - N_c);}$$

and at the crossing

$$\Omega_{X,c} = \tfrac{1}{2}, \qquad \rho_X(N_c) = \rho_{\rm ordinary}(N_c).$$

The exact equality is with the complete non-dark sector; relative to dust alone the ratio is 1 + ρ_r(N_c)/ρ_m(N_c) = 1.0003953 at the benchmark.

### 1.4 Dynamical consequences

**R11 — equation of state.** Separate conservation ρ′_X = −3(1+w_X)ρ_X gives

$$w_X(N) = -1 + \tfrac{2}{3}\tanh(N - N_c).$$

**R12 — shape invariant.**

$$\boxed{;9(1+w_X)^2 + 6w'_X = 4;}$$

with equivalent forms ρ_X/ρ_* + ¼(d ln ρ_X/dN)² = 1 and X′ = 2/3 − (3/2)X² for X := 1 + w_X.

**R13 — self-dual comparison.** The symmetrized relative entropy of the state and its modular reflection is

$$\mathfrak{S}_J(\theta) = 4\theta\tanh\theta, \qquad \mathfrak{S}_J = 6(N-N_c)(1+w_X),$$

nonnegative, vanishing only at θ = 0, with 𝔖″_J(0) = 8. Relative-entropy positivity fixes the phantom-to-quintessence orientation relative to increasing Weyl scale.

**R14 — central blindness.**

$$\operatorname{Var}(K + \alpha\mathbf{1}) = \operatorname{Var}(K).$$

The local response is blind to the absolute energy zero; a global scalar lift remains in Λ_g.

### 1.5 Dependency structure

```
causal order [g]      scale section σ∈𝓔[1]      normal pair Q = P₊ − P₋
      \                     |                          /
       \                    |                         /
        +---- R6 width  +  R7 scale–capacity  (the two unit laws) ----+
       /                    |                                          \
tractor gravity      closed dark history                        predictions
ℰ_ab(σ) ∝ σT°_ab     ρ_X = ½ρ_crit,c sech²(N−N_c)        9(1+w)² + 6w′ = 4
```

### 1.6 What is law, what is solution data, and what is measured

|quantity|type|role|
|---|---|---|
|[g]|causal/conformal geometry|fixes null cones and causal order|
|σ|scale section|metric calibration|
|N|Weyl coordinate|logarithmic scale displacement|
|Q|normalised normal chirality|fundamental horizontal binary score|
|θ|horizontal state coordinate|relative modular polarisation|
|ϱ⊥|width law|postulated value 1 `[PRINCIPLE]`; measured 0.800 [0.575, 0.982]|
|ℜ_c|amplitude law|postulated value 1 `[PRINCIPLE]`; measured 1.025 [0.941, 1.088]|
|N_c|solution origin|intrinsic self-dual event; date fixed by flatness|
|Ω_m0, Ω_r0|measured state data|locate the crossing in the closed background|
|Λ_g, Λ_res|global lift/sector|zero in the open-future branch `[SECTOR]`|

**The theory in one line.** Given the measured ordinary budget and spatial flatness, R1–R14 determine the entire late-time history — density, equation of state, chronology, kinematics, operator structure — with no adjustable function and no adjustable constant. What can still be adjusted is nothing; what can still be _refuted_ is listed in §29.

## 2. The two structural laws

Everything above the waterline of R10 is standard mathematics, conditional theorems, or bookkeeping. The theory's entire physical content beyond general relativity is concentrated in two dimensionless unit laws. This chapter gives each its exact statement, its logical status, its supporting precedents, its existence ceiling, and its measured value — and states plainly what changed since Revision 2, where both were wrongly claimed as theorems.

### 2.1 Why exactly two numbers

The closed family has the form

$$\rho_X(N) = \frac{\Re_c}{2},\rho_{\rm crit,c}\operatorname{sech}^2!\big[\varrho_\perp(N-N_c)\big],$$

with N_c eliminated by flatness. Its observable content therefore carries exactly two structural dimensionless numbers: the **width** ϱ⊥, measured by the generalised invariant 9(1+w)² + 6w′ = 4ϱ⊥² (Appendix A.2) and by the CPL tangent locus (Appendix A.10); and the **amplitude** ℜ_c, measured by the crossing fraction Ω_X,c = ℜ_c/2. The split of G⊥_NN into (slope)² × (capacity) is representation data — rescaling θ moves ϱ⊥ and G⊥_θθ oppositely and leaves G⊥_NN fixed — but in the canonical binary normalisation Q² = 1 the two numbers are separately meaningful and separately measured. Two invariant observables; two unit laws; nothing else.

### 2.2 The width law: ϱ⊥ = 1 `[PRINCIPLE]`

**Statement.** In the canonical binary coordinate, one Weyl e-fold produces one unit of modular polarisation: dθ/dN = 1.

**What is derived and what is declared.** The affine form θ = ϱ⊥(N − N_c) is a conditional theorem: if the reduced noncentral cocycle depends on two scales only through their ratio and is measurable, Cauchy's functional equation forces the logarithm (§9). The coefficient is _not_ forced. The fundamental null-normal pair L₊ ⊕ L₋ and the fundamental scale pair 𝓔[1] ⊕ 𝓔[−1] both carry the characters e^{±x}; the law identifies these fundamental representations with each other — fundamental couples to fundamental, as matter couples to gauge fields in the fundamental. Higher real powers are mathematically admissible; the unit is a physical choice of representation, in the same logical position as "the gauge group is SU(3)×SU(2)×U(1)."

**What was withdrawn.** Revision 2 claimed ϱ⊥ ∈ ℤ from the grading and then selected 1 by the existence ceiling. The integrality premise is false — 𝓔[w] exists for all real w — and the claim is withdrawn with autopsy in §31.2. The ceiling survives as a prediction and consistency bound; the discrete-selection logic survives as a pattern awaiting a discrete menu; a possible Euclidean-periodicity route to re-deriving integrality is filed `[OPEN]` in §9 and counted as nothing.

**Ceiling and measurement.** Flatness admits no closed solution above ϱ⊥^max(Ω_m) = 1.814 at the benchmark (§14): the theory could have been internally impossible at its declared value and is not. The direct determination from DESI DR2 + Pantheon+ is ϱ⊥ = 0.800, 1σ [0.575, 0.982] — 1.08σ from unity, comfortably under the ceiling (P7).

### 2.3 The amplitude law: ℜ_c = 1 `[PRINCIPLE]`

**Statement.** Define the Ruble number

$$\Re_c := \frac{k_B}{S_c},G^\perp_{NN}(N_c) = \frac{k_B,C_{\perp,c}}{S_c},\varrho_\perp^2.$$

It is invariant under reparametrisation of θ — metric and slope transform oppositely — and it is the entropy-normalised squared BKM speed of the horizontal state under one Weyl e-fold, evaluated at the intrinsic self-dual event. The Scale–Capacity Equivalence Principle sets ℜ_c = 1.

**Three equivalent readings.**

1. _Isometry:_ the pullback of the entropy-normalised BKM metric along the soldering map equals dN² at self-duality.
2. _Capacity saturation:_ in the canonical representation ϱ⊥ = 1, the law reads C_⊥,c = S_c/k_B — the selected wall mode carries exactly the Einstein capacity, Var(K) = ⟨K⟩.
3. _Self-duality squared:_ the state's self-dual point (the unique minimum of 𝔖_J) is also the energy budget's self-dual point (Ω_X,c = ½, equal partition with everything else). State self-duality is budget self-duality. The unit value is also the exact midpoint of the existence interval ℜ_c ∈ (0, 2) that flatness allows (§14) — the law places the theory at the symmetric point of its own allowed range.

**Precedents `[STANDARD]`.** The law is not derived here, but it is not unsupported. Capacity of entanglement equals entropy, C_E = S_EE/k_B, in controlled spherical Einstein-holographic settings [51]; modular-Hamiltonian variance equal to horizon entropy has been proposed for flat, de Sitter, and holographic causal diamonds [52, 53, 54]; the BKM Hessian of relative entropy equals gravitational canonical energy in controlled holographic perturbation theory [12]; and apparent-horizon thermodynamics supplies the exact dimensional conversion (§11) [23, 24, 55]. These results characterise an **Einstein-capacity universality class**; the law asserts the self-dual FLRW wall belongs to it. That assertion has not been proved for a dynamical FLRW causal wall — it is the theory's equivalence principle and the most direct target for independent derivation or refutation (Q2, K6).

**What was withdrawn.** Revision 2 derived C = S from Cardy's formula by declaring the horizontal sector a two-dimensional chiral CFT. The dimensionality of a normal plane does not supply a field theory, a Hamiltonian, a central charge, or a thermodynamic limit; the derivation is withdrawn with autopsy in §31.3. What survives from that section is the exponential-family identity G_λλ = Var(K) = C_E `[THEOREM]` and the fixed-localisation argument separating horizontal from vertical capacity classes — both now supporting structure for R7 rather than its proof.

**Ceiling and measurement.** Flatness bounds the amplitude absolutely: Ω_X,c = ℜ_c/2 < 1 requires ℜ_c < 2, with ℜ_c = 2 the degenerate all-dark crossing (§14). The direct determination is ℜ_c = 1.025, 1σ [0.941, 1.088] — a 7% cosmological measurement of a quantum-information quantity, 0.3σ from unity (P5).

### 2.4 The accounting after closure

|item|status|
|---|---|
|causal conformal geometry + scale section|`[STANDARD]` factorisation|
|trace-free tractor source equation|exact reformulation of GR `[STANDARD]`|
|boost-charge unity for the local source|`[CONDITIONAL]` principle, §20|
|fundamental normal chirality quotient|`[IDENTIFICATION]`, §8|
|affine cocycle soldering|`[CONDITIONAL]` theorem, §9|
|**width law ϱ⊥ = 1**|**`[PRINCIPLE]`**, measured (P7)|
|**amplitude law ℜ_c = 1**|**`[PRINCIPLE]`**, measured (P5)|
|separate homogeneous conservation|effective-sector assumption pending §25|
|Λ_res = 0|`[SECTOR]` choice, §21|
|spatial flatness, Ω_m0, Ω_r0|measured state data|

**The compression test, passed.** Inputs: two dimensionless units, one sector bit, the measured ordinary budget. Outputs: the full density and equation-of-state history, a differential invariant, a forced triple coincidence, a bounded acceleration episode with dated endpoints, present kinematics to four digits, a canonical perturbation pair, and the local vacuum blindness — all locked to one another. Input does not equal output.

**What "zero free functions" now means, exactly.** Zero fitted functions of redshift; zero continuously fitted constants; two _discrete_ unit laws whose values were declared before the fits that now measure them at ≈1σ; one global sector bit. Revision 2 claimed the two units as theorems and was wrong; the theory's numbers did not move by the withdrawal — only their labels did. The programme's standard — no type-d free functions — holds with room to spare, and the honest ledger is the point (S13).

---

# Part II — Background, self-contained

## 3. Six things called "time"

The framework uses several ordered parameters that must never be conflated; the v5.0 inconsistency arose from fusing the last two rows.

|symbol / concept|mathematical type|behaviour|
|---|---|---|
|causal order x ≺ y|partial order on events|orientation is part of the relation|
|coordinate t|parameter in equations|often reversed by t ↦ −t|
|proper time τ|metric length along a timelike curve|needs the calibrated metric|
|Weyl scale N = ln a|additive coordinate on scale ratios|reverses between expansion and contraction|
|modular parameter s|**vertical** automorphism parameter of one state|reversible one-parameter group|
|horizon rapidity η_A|**vertical** geometric boost coordinate at a cut|runs at rate μ_A per e-fold|
|horizontal polarisation θ|**horizontal** coordinate comparing different states|state deformation, not elapsed modular time|

The corrected relations, exact along the closed history (§19):

$$\frac{d\eta_A}{dN} = \mu_A(N) = \frac{1-q}{2}, \qquad \frac{d\theta}{dN} = \varrho_\perp = 1, \qquad \theta' - \eta'_A = \tfrac{1}{4}(\ln\mathcal{S}_A)'.$$

The first is a running horizon-clock rate; the second is the width law; the third says the horizontal and vertical clocks differ by exactly the horizon information growth. **Register discipline:** every temporal or causal claim below declares which row of this table it lives in.

## 4. Conformal geometry, scale, and the tractor dictionary

**Densities and tractors `[STANDARD]`.** A conformal manifold is (M, [g]) with g ∼ Ω²g. A positive section σ ∈ Γ(𝓔[1]) selects g_σ = σ⁻²g; the pair ([g], σ) carries the same information as a metric, but the two factors may obey different laws — that separation is the physical proposal. With the Schouten tensor P_ab and J = P^a_a = R/6, the scale tractor is I_A = ¼D_Aσ ≃ (σ, ∇_aσ, −¼(Δσ + Jσ)). On the set where σ ≠ 0:

$$\nabla^T_a I_B = 0 \iff \mathcal{E}_{ab}(\sigma) := (\nabla_a\nabla_b\sigma + P_{ab}\sigma)_0 = 0 \iff g_\sigma \text{ is Einstein},$$

and in the physical scale I² = −R[g_σ]/12 [3, 4, 5, 40, 41].

**GR in transport form `[STANDARD]`.** The trace-free Einstein equation is ℰ_ab(σ) = (4πG/c⁴)σT°_ab; the trace gives I² = (2πG/3c⁴)T − Λ_g/3. Slogans: vacuum geometry = parallel scale transport; noncentral stress = transport defect; stress trace = norm variation; Λ_g = global scalar lift. A measured w_X ≠ −1 is, in this language, evidence that the dark sector contributes to the failure of scale-tractor parallelism.

**Flat FLRW dictionary `[THEOREM]`.** For ds² = a²(η)(−dη² + dx²) with the flat conformal representative, σ = 1/a, N = ln a = −ln σ, and with primes denoting conformal time,

$$\sigma' = -H, \qquad \mathcal{R} := \frac{1}{aH} = -\frac{\sigma}{\sigma'}, \qquad \mathcal{R}' = q, \qquad q = -1 + \frac{\sigma\sigma''}{\sigma'^2}.$$

The homogeneous null-energy condition is convexity of the scale section, ρ + p ≥ 0 ⟺ σ″ ≥ 0; accelerated expansion is log-concavity of scale, q < 0 ⟺ (ln σ)″ < 0. The tractor norm is I² = −½(1−q)H².

**The horizon index `[THEOREM]`.** For a spherical horizon define μ_H := |κ_H|R_H/c². For the flat FLRW apparent horizon R_A = c/H with the Kodama–Hayward surface gravity [23, 24],

$$\mu_A = \frac{1-q}{2} = -\frac{I^2}{H^2} = \frac{T_AS_A}{E_A},$$

a running state index — horizon kinematics on the left, scale-tractor geometry in the middle, horizon thermodynamics on the right.

|regime|w|q|μ_A|
|---|---|---|---|
|radiation|1/3|1|0|
|matter|0|1/2|1/4|
|coasting / acceleration threshold|−1/3|0|1/2|
|de Sitter|−1|−1|1|
|benchmark, today|—|−0.3369|0.6685|
|benchmark, crossing|—|−0.2499|0.6250|

Acceleration is exactly μ_A > ½, and ½ is also |κ|R/c² for a four-dimensional Schwarzschild horizon — a shared dimensionless surface-gravity balance at marginality, not an identification of the two spacetimes.

## 5. Modular theory: vertical and horizontal

For a local von Neumann algebra 𝒜 and faithful state ω, Tomita–Takesaki theory supplies the modular operator Δ_ω, the conjugation J_ω, and the flow σ^ω_s(A) = Δ^{is}AΔ^{−is} [46, 47]. Bisognano–Wichmann makes the flow geometric — the boost — for the Rindler wedge [6]; Casini–Huerta–Myers for the CFT diamond [7]; stationary horizons and controlled perturbations extend the family [20, 21, 22]. This is **vertical** motion: an automorphism at fixed state.

A family N ↦ ω_N is **horizontal** motion through state space; a Connes cocycle or modular Berry connection [13, 14] compares modular frames of different fibers. Schematically,

$$\partial_N K_N = [\mathcal{A}_N, K_N] + (\mathcal{D}_NK_N)_\perp + c'_N\mathbf{1},$$

with the three terms respectively vertical gauge, physical horizontal noncentral deformation, and central normalisation shift. The gravitational boost-charge principle (§20) acts on the vertical generator; the scale-capacity law acts on the horizontal tangent; the vacuum energy zero is central (§21). In holographic code subspaces the JLMS relation [11] decomposes boundary modular charge into area charge plus bulk modular charge plus a central term — the controlled laboratory in which modular charge, area, information Hessian, and symplectic structure demonstrably cohere.

## 6. Information geometry and capacity

**Classical and quantum metrics `[STANDARD]`.** Čencov's theorem fixes the Fisher metric up to scale under statistical morphisms [16, 17]; Petz classifies quantum monotone metrics [15, 18]. Monotonicity alone does not select BKM; the Hessian of Umegaki relative entropy does: S(ω_{θ+dθ}‖ω_θ) = ½G^BKM_θθ dθ² + O(dθ³). For the binary family R5 the metric is sech²θ and the total Fisher length of the crossover is

$$L_F = \int_{-\infty}^{\infty}\operatorname{sech}\theta,d\theta = \pi,$$

the full simplex diameter: the state traverses the complete binary simplex from one extremal ray to the other, and the width law fixes how that fixed distance is distributed over cosmic scale.

**Capacity `[STANDARD]` + `[THEOREM]`.** The entanglement capacity of a state is C_E = Var(K). For the exponential family generated by rescaling the modular Hamiltonian, ρ(λ) = e^{−(1+λ)K₀}/Z(λ),

$$G^{\rm BKM}_{\lambda\lambda}\Big|_0 = \partial_\lambda^2\ln Z\Big|_0 = \operatorname{Var}(K_0) = C_E,$$

an identity of exponential families, verified numerically on random modular spectra to 10⁻⁶. The horizontal direction is the modular-rescaling direction because a Weyl rescaling changes the diamond radius R, hence its temperature ħc/2πk_BR, hence β `[IDENTIFICATION]`. Capacity is _not_ equal to entropy for arbitrary states; C_E = S/k_B holds in controlled spherical Einstein-holographic settings [51] and is proposed for causal diamonds [52, 53, 54] — the Einstein-capacity universality class that R7 invokes. None of the classification theorems converts dimensionless curvature into energy density; that conversion is R8 + R9, not a hidden normalisation theorem.

## 7. Conventions

Metric signature (−,+,+,+); primes on cosmological quantities denote d/dN unless a section declares conformal time; x := −N_c > 0. Jerk convention **registered with its prediction** (a lesson this programme paid for once): j := (d³a/dt³)/(aH³), identity j = q + 2q² − dq/dN [50], Appendix A.9. CPL tangent (w₀, w_a) via w(a) = w₀ + w_a(1 − a) [43, 44]. Dimensionless horizon entropy 𝒮_A := S_A/k_B = πc⁵/(GħH²). The symbol ℜ is reserved for the Ruble number; the perturbation response map is 𝓡_Σ; the Revision-2 symbol γ is retired (its content is ℜ_c). Full symbol dictionary in Appendix D.

---

# Part III — The derivation chain

## 8. Normal chirality and the binary family

A spacelike codimension-two cut Σ has a Lorentzian normal plane N(Σ) = L₊ ⊕ L₋. With P± the null-line projectors, the normal chirality Q = P₊ − P₋ satisfies Q² = P₊ + P₋ = 1, and normal reflection exchanges the rays: JQJ = −Q. The full modular generator of a type-III algebra need not have two eigenvalues; the structural identification is narrower and is the theory's P:

**Fundamental normal reduction `[IDENTIFICATION]`.** The homogeneous J-odd horizontal response is the infrared projection of the full state deformation onto the normal chirality quotient. The transverse directions along Σ are FLRW-symmetry-invariant and J-even, carry no J-odd horizontal tangent, and drop out of G⊥ identically.

The maximum-entropy family generated by Q is R5, and its normalisation ⟨Q²⟩ = 1 is the **master identity**, readable in five registers `[THEOREM]`:

1. _Operator:_ Q² = 1 — the cut has exactly two null normals.
2. _Moments:_ ⟨Q⟩² + Var(Q) = 1 — orientation plus susceptibility exhaust the binary.
3. _Information geometry:_ η² + G_θθ = 1 — the dual coordinates trace the unit circle.
4. _Dynamics:_ (3(1+w_X)/2)² + ρ_X/ρ_* = 1 — which is R12, the invariant.
5. _Scattering:_ sech²θ is the ℓ = 1 reflectionless potential — which is the Witten pair of §23.

One identity; five theories' worth of consequences; that lockstep is what the ledger prices (§30).

## 9. Soldering: what Cauchy gives and what it cannot

Assume the reduced relative cocycle depends on two scale sections only through r = σ₂/σ₁ (rank-one ratio hypothesis) and has one noncentral generator Q. Connes' chain rule collapses to the Cauchy equation θ(r₁r₂) = θ(r₁) + θ(r₂); measurability suffices to solve it:

$$\theta(r) = -\varrho_\perp\ln r = \varrho_\perp(N - N_c) \quad \text{[CONDITIONAL]}.$$

The affine _form_ is derived; the coefficient is not — the characters of the positive scale group form a continuum r^s, s ∈ ℝ, and density bundles 𝓔[w] exist for every real w. R6 declares the unit as the fundamental representation (§2.2).

**A possible resurrection route, filed and priced `[OPEN]`.** Euclidean continuation turns the modular boost into a rotation with period 2π; single-valuedness under that rotation quantises weights — the mechanism behind spin quantisation and conical regularity. If the horizontal character extended to the continued angle, integrality could return as a theorem. Two obstructions are recorded now: the quantised slope would be dθ per unit _rotation angle_, i.e., tied to the vertical rapidity η_A rather than to N; and along the closed history dη_A/dN = μ_A(N_c) = 0.6250 ≠ 1, so even a proved angular integrality would not directly integerise dθ/dN. Until someone closes that gap, the route is counted as nothing.

## 10. The constitutive law

The scale susceptibility is the pullback of the BKM metric along the soldering map Φ: ℝ_Weyl → 𝒮(𝒜): the invariant object is Φ*G^BKM = sech²θ dθ², in which ϱ⊥ specifies how Weyl scale parameterises a fixed path in state space without changing the path. For a reference KMS state ω_c with physical modular Hamiltonian ℋ_c = k_BT_cK_c, nonequilibrium free energy obeys exactly F_c(ρ) − F_c(ω_c) = k_BT_c S(ρ‖ω_c), and for a neighbouring scale state S(ω_{c+δN}‖ω_c) = ½G⊥_NN(N_c)δN² + O(δN³) (Appendix A.13). The homogeneous source law distributes that quadratic free-energy curvature over the causal-wall volume — R8:

$$\rho_X(N) = \frac{k_BT_c}{2V_c},G^\perp_{NN}(N), \qquad G^\perp_{NN} = C_{\perp,c},\varrho_\perp^2\operatorname{sech}^2\theta.$$

**This is not a local spacetime kinetic action.** It is a Dirichlet functional on a curve in state space; θ is a collective constitutive coordinate of the same type as temperature. The distinction matters twice: the canonical single-field no-go of §24 does not apply to it, and it is why the ghost that kills the fluid picture at the crossing kills the fluid picture rather than the theory.

**The intrinsic-anchor point (resolving the old clock-reading objection).** T_c, V_c, and S_c are evaluated at the self-dual event — the unique global minimum of 𝔖_J, an intrinsically defined point of the state family, not an observer's date. The amplitude ½ρ_crit,c is therefore a relational, event-indexed quantity: given flatness and the ordinary budget, nothing about it could have been otherwise. The suspicious-looking H² scaling is the marginality identity of §11 doing its job (S3).

## 11. The Hawking–Friedmann bridge `[THEOREM]`

For the spatially flat FLRW apparent horizon, R_c = c/H_c and

$$\frac{S_c}{k_B} = \frac{\pi R_c^2c^3}{G\hbar}, \qquad k_BT_c = \frac{\hbar c}{2\pi R_c} \implies k_BT_c\frac{S_c}{k_B} = \frac{c^4R_c}{2G} = E_{\rm MS,c},$$

$$\boxed{;\frac{k_BT_c}{V_c}\cdot\frac{S_c}{k_B} = \frac{3c^2H_c^2}{8\pi G} = \rho_{\rm crit,c};}$$

ħ, k_B, G, c all cancel. E_MS is the Misner–Sharp energy [42]; the middle equality is Friedmann marginality, 2GE_MS/(c⁴R_A) = 1: the causal radius is exactly the radius at which enclosed gravitational energy saturates the spherical compactness relation. This is _not_ a claim that the observable universe is a black hole; both are marginal causal-information surfaces, and the shared normalisation is what "marginal" means.

**The temperature is the horizontal one.** T_c = ħc/2πk_BR_c is the canonically normalised causal-diamond temperature of the 2π boost — the horizontal modular normalisation. It must not be confused with the running vertical Kodama–Hayward temperature T_KH = μ_AT_c [23, 24, 55]. Using the vertical temperature in the horizontal channel multiplies the amplitude by μ_A(N_c) and is excluded by direct fit (S12) — the vertical/horizontal split doing physical work, not taxonomy. The Smarr relation of stationary black holes, (D−3)E = (D−2)TS, is the vertical statement; the bridge above is the horizontal one.

## 12. The closed law, the equality theorem, and the intrinsic crossing

Writing G⊥_NN(N) = ℜ_c(S_c/k_B)sech²(N−N_c) per R7 and inserting the bridge,

$$\rho_X(N) = \frac{\Re_c}{2},\rho_{\rm crit,c}\operatorname{sech}^2(N-N_c) \xrightarrow{;\Re_c=1;} \frac{1}{2},\rho_{\rm crit,c}\operatorname{sech}^2(N-N_c).$$

**Equality `[DEDUCTION]`.** At the crossing Ω_X,c = ½; flatness gives ρ_ordinary,c = ρ_crit,c − ρ_X,c = ½ρ_crit,c; hence ρ_X(N_c) = ρ_ordinary(N_c) exactly, with the complete non-dark sector. Relative to dust alone the ratio is 1 + ρ_r,c/ρ_m,c = 1.0003953 at the benchmark — a calculable 4×10⁻⁴ radiation correction, not a new parameter. The former free normalisation r_c = 1 of earlier drafts is thereby replaced by a law.

**The crossing is intrinsic `[THEOREM]`.** Because JQJ = −Q, modular reflection acts as Jω_θJ = ω_{−θ}, and the symmetrized relative entropy 𝔖_J(θ) = 4θ tanh θ [19] is nonnegative, vanishes only at θ = 0, and has 𝔖″_J(0) = 8: the crossing is the unique self-dual state of the family — an event defined by the state geometry alone. Its _date_ relative to today is solution data fixed by flatness and (Ω_m0, Ω_r0). Along the history 𝔖_J = 6(N−N_c)(1+w_X) ≥ 0 fixes the orientation: phantom strictly before, quintessence strictly after (P6). What it does not fix is the choice of the expanding over the time-reversed branch — an initial-condition question the theory does not claim (§32).

## 13. General spatial dimension `[THEOREM]`

For d spatial dimensions, A = Ω_{d−1}R^{d−1}, V = Ω_{d−1}R^d/d, and Einstein–Friedmann marginality give (Appendix A.11)

$$\frac{k_BT_c(S_c/k_B)}{V_c} = \frac{2}{d-1},\rho_{\rm crit,c} \implies \Omega_{X,c} = \frac{\Re_c}{d-1}, \qquad \frac{\rho_{X,c}}{\rho_{\rm ordinary,c}} = \frac{\Re_c}{d-1-\Re_c}.$$

For ℜ_c = 1 the equal partition ρ_X = ρ_ordinary occurs **only** in d = 3. This does not prove space must be three-dimensional; it shows the unit scale-capacity law and equal self-dual partition are mutually compatible precisely in the observed dimension — a consistency principle available to dimensional-selection programmes, typed as such and no further (P6′ in §27).

## 14. Two ceilings, one for each law `[THEOREM + ANALYSIS]`

Both unit laws face nontrivial existence bounds; both could have failed; neither does; data land within ≈1σ of both units.

**The width ceiling.** With x = −N_c > 0, the flatness closure (dust form) is e^{3x}sech²(ϱ⊥x) = T_m with T_m = (1−Ω_m−Ω_r)/Ω_m. Since d ln F/dx = 3 − 2ϱ⊥tanh(ϱ⊥x), there is exactly one root for ϱ⊥ ≤ 3/2 and two-or-none above, with the double root giving the closed-form ceiling (Appendix A.5):

$$T_m = \Big(1 - \frac{9}{4\varrho_\perp^2}\Big)\exp\Big[\frac{3}{\varrho_\perp}\operatorname{artanh}\frac{3}{2\varrho_\perp}\Big], \qquad \varrho_\perp > \tfrac{3}{2}.$$

|Ω_m|ϱ⊥^max|
|---|---|
|0.280|1.6962|
|0.310598|1.8141|
|0.330|1.9060|
|0.34685|2.0000|

A hypothetical ϱ⊥ = 2 first becomes admissible at Ω_m = 0.34685 — 3.8σ from the measured 0.3086 ± 0.010 and excluded by direct fit at Δχ² = 60 `[ANALYSIS]`. In Revision 2 this ceiling served as the selector in a now-withdrawn integrality argument; its honest role is the one stated here — a prediction and consistency bound the declared unit satisfies with margin (P7), and an independent kill switch (K5).

**The amplitude ceiling.** Ω_X,c = ℜ_c/2 together with a positive ordinary sector at the crossing bounds ℜ_c ∈ (0, 2) absolutely; ℜ_c = 2 is the degenerate all-dark crossing. The declared unit is the exact midpoint of the allowed interval and the unique equal-partition value. The measured 1.025 [0.941, 1.088] sits on it.

---

# Part IV — The background history it entails

## 15. The closed background equation

With radiation, pressureless matter, and the scale-capacity source,

$$H^2(N) = \frac{8\pi G}{3c^2}\Big[\rho_{m0}e^{-3N} + \rho_{r0}e^{-4N} + \tfrac{1}{2}\rho_{\rm crit,c}\operatorname{sech}^2(N-N_c)\Big],$$

and present flatness determines N_c with no dark input (Appendix A.8):

$$\big(\Omega_{m0}e^{3x} + \Omega_{r0}e^{4x}\big)\operatorname{sech}^2x = 1 - \Omega_{m0} - \Omega_{r0}, \qquad x = -N_c.$$

N_c is therefore not a fitted dark parameter: its intrinsic meaning is fixed by self-duality (§12); its position relative to today is fixed by the measured ordinary state and flatness. At the benchmark the unique root is x = 0.2940066.

## 16. The invariant, the phase flow, and the three futures

**The invariant `[THEOREM]`.** With Δ_X := −d ln ρ_X/dN = 2ϱ⊥tanh θ, Δ′_X = 2ϱ⊥² − ½Δ_X², so Δ_X² + 2Δ′_X = 4ϱ⊥², i.e. (Appendix A.2)

$$9(1+w_X)^2 + 6w'_X = 4\varrho_\perp^2 \xrightarrow{;\varrho_\perp=1;} 4,$$

independent of amplitude and crossing date — the width law's fingerprint at every redshift, and the primary structural test (P9, K1).

**The phase flow `[THEOREM]`.** X := 1 + w_X obeys the autonomous equation X′ = 2/3 − (3/2)X², a saddle-node pair with fixed points w₋ = −5/3 and w₊ = −1/3. The observed history is the unique heteroclinic orbit between them: one density maximum, one w = −1 crossing, no repetition — none of these is a separately adjusted feature, and a second episode is a kill condition (K7). Acceleration occurs while (2 − 3(1+w_X))ρ_X > ρ_m + 2ρ_r; since the response is negligible in the deep past and decays as a⁻² in the far future, the inequality holds on one finite interval: one observed entry, one predicted exit.

**Three futures, one chosen by the sector bit.** With Λ_res = 0 exactly, ρ_X ∝ a⁻², w_X → −1/3, H ∝ a⁻¹, a(t) ∼ t: coasting, with the future conformal-time integral divergent and hence no permanent event horizon. Any positive residual, however observationally negligible today, eventually dominates and restores de Sitter — exact zero and negligible are different theories (P10, §21). A hypothetical ϱ⊥ ≥ 3/2 branch would instead decelerate permanently; the declared unit does not.

## 17. The chronology of the episode

All dates follow from (Ω_m0, Ω_r0) = (0.310598, 9.15×10⁻⁵) and flatness.

|event|value|
|---|---|
|acceleration onset|z = 0.785694 (ΛCDM at same Ω_m: 0.643)|
|self-dual crossing = density peak = equality = w = −1|z_c = 0.341793|
|deceleration at crossing|q(N_c) = −0.249901|
|horizon index at crossing|μ_A(N_c) = 0.624951|
|today|q₀ = −0.336902, j₀ = −0.111246, dq/dN|
|acceleration maximum|z = 0.0008 — essentially now|
|acceleration exit|a/a₀ = 11.7865, i.e. 2.47 e-folds hence|
|total accelerating span|3.047 e-folds|
|state at exit|1 + 3w_X = −0.0159; matter fraction 0.0157|

Today sits at the acceleration maximum to one part in 10³ of an e-fold — the theory's version of "why now" is that the peak is where a half-e-fold-wide window is most likely to catch the episode, and the sharper coincidence is P4's. The Komar density of the response, ρ_X(1 + 3w_X), crosses zero at w_X = −1/3: the pull shuts itself off, which is why the exit exists and never recurs.

## 18. The geometry of the history: one half-turn

Substituting the flat Fisher coordinate φ = gd(θ) (the Gudermannian), dφ = sech θ dθ, the entire dark history is uniform motion along a quarter arc on each side of the crossing: total Fisher length L_F = π, a half-turn of the unit circle, with the crossing at the midpoint. Five characterisations of the same point coincide exactly `[THEOREM]`:

1. the unique minimum of the symmetrized relative entropy 𝔖_J;
2. the w_X = −1 crossing;
3. dark–ordinary equality (given ℜ_c = 1);
4. the Fisher-arc midpoint;
5. the susceptibility and density maximum.

And two nearby events are _distinct_ from it: the acceleration onset (z = 0.786) and the acceleration maximum (z ≈ 0) — the theory forbids conflating them, and reconstructions that merge them are misreading it. The sech pulse is its own Fourier transform up to scaling `[ANALYSIS]`; the retarded scattering phase of the associated operator reproduces the Fisher length by Levinson's theorem — consequences of one factorisation, recorded in §23 and not counted as independent evidence.

## 19. The vertical sector: clock allocation and vacuum blindness

The dimensionless horizon entropy is 𝒮_A = πc⁵/(GħH²), so d ln 𝒮_A/dN = 2(1+q) exactly. Defining the vertical horizon rapidity by dη_A/dt = |κ_A|/c, one has dη_A/dN = μ_A, and one Weyl e-fold decomposes exactly (Appendix A.12):

$$dN = d\eta_A + \tfrac{1}{4},d\ln\mathcal{S}_A, \qquad \theta' - \eta'_A = 1 - \mu_A = \tfrac{1}{4}(\ln\mathcal{S}_A)'.$$

Radiation-era e-folds are almost pure information growth (μ_A = 0); the de Sitter limit is pure rapidity (μ_A = 1); the far-future coast splits 1:1 (μ_A = ½); today's e-fold splits 0.6685 : 0.3315. The horizontal clock θ advances at unit rate throughout — the width law — and the difference between the horizontal and vertical clocks is exactly the horizon information rate: the corrected form of what v5.0 tried to say with one conflated parameter.

**Vacuum blindness `[THEOREM]`.** A constant shift K ↦ K + α**1** does not change the normalised state, so no monotone state metric — not just BKM — assigns it length: Var(K + α**1**) = Var(K). On the geometric side the trace-free source equation annihilates λg_ab identically. An additive vacuum offset is central in both languages; the local causal response provably cannot see it. What blindness does not do is stabilise or select the global scalar lift — that is §21.

---

# Part V — Sourcing, the vacuum, and the far future

## 20. One causal boost charge `[CONDITIONAL]`

For an equilibrium causal cut, propose that the modular boost charge of the restricted state and the gravitational Noether boost charge of the cut are two representations of one causal charge. The state side is the entanglement first law δS_out = δ⟨K⟩ [7, 9, 10]; the geometric side is the area charge S_grav = k_BA/4ℓ_P² [8]; Raychaudhuri focusing ties area variation to R_abk^ak^b. Equating the two responses for every local null direction yields R_abk^ak^b = (8πG/c⁴)T_abk^ak^b, hence the trace-free Einstein equation and the tractor transport law of §4. One unity principle plus established ingredients; conditional, and independent of the late-time model — the scale-capacity law neither uses nor supports it.

## 21. The vacuum: dissolved, retyped, remaining

**Dissolved `[THEOREM]`.** Why computed zero-point energy does not gravitate in the dark channel: vacuum blindness (§19). The response metric cannot couple to a central shift; the trace-free equation cannot couple to pure trace. No cancellation to 122 decimals occurs because no coupling exists to cancel.

**Retyped `[THEOREM]`.** Why the observed dark density is 10⁻¹²² of the Planck density: **the theory contains no constant with that value.** The observed density is ½ρ_crit,c sech²(N−N_c), relational and event-indexed. The famous small number is (H_ct_P)² — a statement about how many Planck times elapse before the matter sector dilutes to the crossing, i.e., a fact about the matter history, not a fine-tuned dark-sector property. ΛCDM needs a constant of nature to be small; this theory has one fewer constant of nature and nothing that needs to be small.

**Remaining `[SECTOR, OPEN]`.** The global lift Λ_res is a flux or superselection datum, not a local source. Manifestly local vacuum-energy sequestering [26, 27] is one published completion in which four-form sectors force the cosmological variables to spacetime constants while global constraints subtract the spacetime-averaged vacuum, with a Gauss–Bonnet extension proposed for the graviton-loop sector — a candidate with the right mathematical type, not a consequence of this framework. The rigid branch takes Λ_res = 0 exactly; which flux sector nature selects is not derived (Q4). `[RHYME]` The causal-set programme predicts a _fluctuating_ residual of magnitude Λ ∼ 1/√V — arithmetically the same magnitude this programme's companion strand reaches by a different route — while the branch taken here fixes w ≡ −1/3 asymptotics with zero residual: same magnitude, opposite modality, and DESI-class data are the live adjudicator. Filed as a rhyme, counted as nothing.

## 22. Future causal character

With Λ_res = 0: ρ_X ∝ a⁻², ȧ → const, ∫dt/a(t) diverges — no permanent event horizon, no asymptotic thermal state, no de Sitter entropy puzzle. The acceleration era ends at a = 11.79a₀ and never recurs. A positive residual, however small, eventually dominates, restores the horizon, and bends w(z) back toward −1: the difference between the sectors is observable in principle only through a very-late-time w(z) floor (P10).

---

# Part VI — The perturbation sector

## 23. The canonical Witten–Darboux pair `[THEOREM]`

The binary potential Ψ(θ) = ln(2cosh θ) generates first-order operators 𝒜 = ∂_θ + η, 𝒜† = −∂_θ + η with η = tanh θ. Since η² + η′ = 1 exactly,

$$\mathcal{H}_- = \mathcal{A}^\dagger\mathcal{A} = -\partial_\theta^2 + 1 - 2\operatorname{sech}^2\theta, \qquad \mathcal{H}_+ = \mathcal{A}\mathcal{A}^\dagger = -\partial_\theta^2 + 1,$$

the ℓ = 1 Pöschl–Teller partner and the free operator — generated by the information potential, not guessed [38, 29]. The zero mode 𝒜ψ₀ = 0 gives ψ₀ = 2^{−1/2}sech θ, so 2|ψ₀|² = sech²θ: the BKM metric density, the normalised dark history, and the bound-state density are one function. The continuum ψ_k = (−ik + tanh θ)e^{ikθ} has R(k) = 0 at both ends — transmitted with a phase shift, not absent. The Witten index is 1; the Levinson phase of the single bound state is π; the total Fisher length is π — three faces of one factorisation, recorded as one fact.

## 24. Four negative results `[NEGATIVE]`

**N1 — ordinary matter growth is not the pair operator.** The smooth-dark-response growth equation reduces to a Schrödinger-like zero-energy problem whose potential contains matter and Hubble-friction terms; it is not proportional to ρ_X and is not Pöschl–Teller. Numerically, forcing transparency on it misassigns the potential by two orders of magnitude (ΔW/Ω_X ranging −179 → +0.27 across the history) and leaves a 64% residual at best. Transparency belongs to the internal horizontal sector; do not rebrand standard growth.

**N2 — no canonical single-field completion.** A minimally coupled scalar's kinetic normalisation is ∝ (1+w_X), negative on the whole pre-crossing branch [28]; at the crossing the mode function behaves as z ∼ |θ|^{1/2}, so z″/z ∼ −1/(4θ²) — exactly the critical inverse-square coupling where fall-to-the-centre begins [30]. The horizontal coordinate is not an ordinary local scalar field; the completion must be collective, constrained, multi-component, or otherwise noncanonical. This is the fluid picture failing at the crossing on schedule, not the theory failing.

**N3 — the tractor sector is not the response sector.** Releasing the tractor-norm channel to imitate the response fails across two decades of scale, and the Weyl and Cotton obstructions vanish identically on the conformally flat background: the vertical geometry has no room to fake the horizontal signal.

**N4 — no H² < 0 branch.** The closed equation never drives H² negative on the physical branch; the history is globally defined.

## 25. What remains open, and the stopping condition `[OPEN]`

The pair fixes the internal horizontal operator geometry: why ℓ = 1, why one localised mode, why a reflectionless continuum. It does not yet identify these operators with scalar/vector/tensor spacetime perturbations. The missing object is the response map 𝓡_Σ from causal-cut deformations to horizontal state tangents, constrained six ways: conserved δT^X_ab; regular crossing; mode count fixed by the pair; definite gradient/cone structure; ghost-free hyperbolicity; Boltzmann-implementable CMB/lensing/growth responses. A perturbative completion is adequate when it derives all six without arbitrary functions — until then the background is closed and the perturbation theory is honestly absent, and P9's decisive observation waits on it. This is a classification problem for natural bilinear operators, not a search for an action (Q1).

---

# Part VII — Predictions

## 26. The closed benchmark

Inputs: Ω_m0 = 0.310598, Ω_r0 = 9.15×10⁻⁵, flatness, R1–R14. Everything below is output.

|quantity|value|
|---|---|
|crossing location|N_c = −0.2940066, z_c = 0.3417927|
|crossing density|ρ_*/ρ_crit,0 = 0.7506311|
|exact ordinary-sector equality|ρ_*/(ρ_m + ρ_r)(N_c) = 1|
|dust-only ratio|ρ_*/ρ_m(N_c) = 1.0003953|
|radiation fraction at crossing|Ω_r,c = 1.976×10⁻⁴|
|present dark fraction|Ω_X0 = 0.6893105|
|equation of state today|w₀ = −0.8094545|
|CPL tangent|w_a = −0.6122053|
|deceleration today|q₀ = −0.3369025|
|jerk today|j₀ = −0.1112465|
|deceleration at crossing|q(N_c) = −0.2499012|
|horizon index at crossing|μ_A(N_c) = 0.6249506|
|acceleration entry|z = 0.785694|
|acceleration exit|a/a₀ = 11.7865|

Two pinning facts sharpen the table. q₀ is pinned near −1/3 almost independently of Ω_m (spread < 0.004 over Ω_m ∈ [0.28, 0.33]) — present acceleration is 63% of ΛCDM's at the same Ω_m (ratio 0.631). And the jerk carries only ±0.03 of propagated Ω_m uncertainty against a full-unit gap from ΛCDM's exact j = 1.

## 27. The prediction ledger

Scoreboard first; each entry then states prediction, meaning, data status, and — where one genuinely exists on survey timescales — the condition that kills it.

|#|prediction|value|current status|
|---|---|---|---|
|P1|CPL tangent (w₀, w_a)|(−0.80945, −0.61221)|inside 1σ of DESI DR2+CMB+Pantheon+; Δχ² = 1.78 from the free 2-parameter fit in this pipeline|
|P2|kinematics today (q₀, j₀)|(−0.3369, −0.1112)|j₀ separates from ΛCDM's exact +1 by 1.11; cosmography approaching the precision|
|P3|chronology: onset, crossing, exit|z = 0.786, z_c = 0.342, a = 11.79a₀|DESI-implied crossing band z ≈ 0.35–0.44; own-pipeline profile z_c = 0.65, 1σ [0.29, open]|
|P4|triple coincidence|Δz ≡ 0 among crossing, density peak, equality|DESI CPL best fit separates them by only Δz = 0.019|
|P5|Ruble number ℜ_c|1|measured 1.025, 1σ [0.941, 1.088]|
|P6|phase ordering|phantom strictly before z_c, quintessence strictly after|consistent with current reconstructions|
|P7|width and its ceiling|ϱ⊥ = 1, with ϱ⊥ ≤ 1.814 required to exist|measured 0.800, 1σ [0.575, 0.982]|
|P8|neutrino-mass release|Σm_ν bound reopens above the 0.059 eV floor|mechanism confirmed in DESI's own w₀w_aCDM analysis; dedicated Boltzmann run pending|
|P9|the invariant = 4|exact at every z|provably invisible to background data; test relocated to growth/lensing|
|P10|the far future|w → −1/3, a ∝ t, no event horizon|not survey-testable; distinguishes Λ_res = 0 from Λ_res > 0|

### P1 — Evolving dark energy at a fixed point of the (w₀, w_a) plane

**Prediction.** (w₀, w_a) = (−0.80945, −0.61221) with zero adjustable parameters; more fully, the one-dimensional locus w_a = (3/2)(1+w₀)² − 2/3 (Appendix A.10), with position along it fixed by Ω_m. The CPL "parameters" surveys fit are, here, the Taylor coefficients of tanh at the present epoch — outputs, not inputs.

**Status `[ANALYSIS]`.** Published DESI DR2 constraints [31]:

|data combination|w₀|w_a|offset of the fixed point (per axis)|
|---|---|---|---|
|DESI + CMB + Pantheon+|−0.838 ± 0.055|−0.62 +0.22/−0.19|0.5σ, 0.04σ|
|DESI + CMB + Union3|−0.667 ± 0.088|−1.09 +0.31/−0.27|1.6σ, 1.5σ|
|DESI + CMB + DES Y5|−0.752 ± 0.057|−0.86 +0.23/−0.20|1.0σ, 1.1σ|

The posteriors carry the standard strong anticorrelation, and the fixed point's offsets from the Union3 and DES Y5 centres lie _along_ the degeneracy direction, so per-axis figures overstate the joint tension. Against this document's own DESI DR2 + Pantheon+ likelihood, releasing both CPL parameters improves on the fixed prediction by only Δχ² = 1.78: the zero-parameter point sits inside the 1σ region of the free two-parameter fit. A dark sector closed by two declared units, with nothing left to adjust, lands where three independent supernova compilations put the measurement.

**Falsifier.** K2.

### P2 — Kinematics today

q₀ = −0.3369, pinned; j₀ = −0.1112 against ΛCDM's identical +1 — a separation of 1.11 in a directly reconstructible kinematic quantity with ±0.03 propagated model uncertainty. The third derivative of the scale factor has opposite character in the two theories: ΛCDM's acceleration is still building toward de Sitter; here it peaked essentially today (dq/dN|₀ = +0.0014, minimum of q at z = 0.0008) and is beginning its structural decline toward coasting. Current cosmographic j₀ determinations carry order-unity errors — the separation sits at their edge, and DESI-plus-supernova compilations are the right data to close it. Falsifier: K4.

### P3 — The chronology of the episode

Onset z = 0.7857 (ΛCDM at the same Ω_m: 0.643 — a 22% separation in a quantity nonparametric reconstructions already estimate); crossing, density maximum, and equality all at z_c = 0.3418; exit at a = 11.787a₀; total accelerating span 3.047 e-folds. The crossing implied by the DESI DR2 CPL fits sits at z = 0.354 (Pantheon+), 0.405 (DES Y5), 0.440 (Union3) (Appendix A.10) — a band whose lower edge sits on the prediction. This pipeline's direct profile of z_c is broad: 0.650, 1σ [0.293, open], a 0.72σ displacement. Falsifier: a reconstruction localising the crossing robustly away from the flatness-determined value — e.g. above z = 0.6 — kills the closed theory (K7), since z_c has no freedom once Ω_m is measured.

### P4 — The triple coincidence (the signature prediction)

z(w_X = −1) = z(ρ_X maximal) = z(ρ_X = ρ_ordinary), exactly. Generic evolving dark energy has no reason for these epochs to be related: the crossing is a property of w(z), the peak of ρ_X(z), equality a relation to the matter sector. Here all three are the single self-dual point of §18 — the cleanest qualitative fingerprint, costing competitors a functional tuning and this theory nothing. At the DESI DR2 CPL best fit the first and third already differ by only Δz = 0.019: the data sit, unprompted, near the coincident configuration. Falsifier: K3.

### P5 — The Ruble number ℜ_c = 1

**Prediction.** The entropy-normalised BKM speed at self-duality is unity — formerly "the capacity ratio γ = 1," relabelled with its logical status corrected (`[PRINCIPLE]`, §2.3, §31.3).

**Meaning and type.** ℜ_c is measured _through_ the model: within the sech² family the crossing amplitude Ω_X,c = ℜ_c/2 is released and fitted — a one-parameter consistency test the closed theory must pass at its declared value, and a cosmological determination of a quantum-information quantity; to our knowledge the first.

**Status `[ANALYSIS]`.** ℜ_c = 1.025, 1σ [0.941, 1.088]: a 7% determination, 0.3σ from unity. Robustness: across ℜ_c ∈ [0.8, 1.3] the co-fitted Ω_m moves only 0.3277 → 0.3186 — under its own error — while χ² swings by 13; the constraint enters through z_c, which sweeps 0.546 → 0.049 across the same range. Anchoring Ω_m at the Planck value gives ℜ_c = 1.030, 1σ [0.955, 1.099]. The competing capacity classes are separately excluded: bulk-thermal (ℜ_c = 3 ⟹ Ω_X,c = 3/2) by flatness itself; Schwarzschild-like (ℜ_c = −2) by sign; the vertical-temperature misallocation (amplitude ×μ_A) by direct fit (S12).

**Falsifiers.** A determination away from 1 at several σ under next-generation BAO with this pipeline (statistical); the Q2 first-principles computation of the wall capacity ratio returning ≠ 1 (structural, K6).

### P6 — Phase ordering

𝔖_J(z) = 6 ln[(1+z_c)/(1+z)]·(1+w(z)) ≥ 0 at every z: no quintessence before the crossing, no phantom after `[THEOREM]` (§12). Any reconstruction placing w > −1 at z > z_c or w < −1 at z < z_c beyond errors kills it. Current reconstructions are consistent with the ordering.

**P6′ — dimension consistency.** In d spatial dimensions Ω_X,c = ℜ_c/(d−1); the unit law and equal partition are compatible only in d = 3 (§13). Not an empirical prediction within the observed dimension; a structural consistency condition, typed as such.

### P7 — The width and its ceiling

ϱ⊥ = 1 declared; ϱ⊥ ≤ 1.8141 required for a flat solution to exist at the benchmark (§14). Direct determination: ϱ⊥ = 0.800, 1σ [0.575, 0.982] — 1.08σ from unity, comfortably under the ceiling. A clean, non-boundary-dominated determination above the ceiling falsifies the entire branch independently of every other prediction (K5); a several-σ exclusion of unity kills the width law specifically.

### P8 — The neutrino-mass release

**Prediction.** The DESI neutrino-mass tension is an artifact of forcing w = −1. Under ΛCDM, DESI DR2 + CMB compress the bound to Σm_ν < 0.064 eV (95%), pressing on the 0.059 eV normal-ordering floor, with the profile preferring the unphysical region [31, 32]. The degeneracy is understood: late-time w > −1 raises the inferred bound. This background has w > −1 for all z < 0.342 with no parameter to tune it away, so the bound must reopen — DESI's own w₀w_aCDM analysis, whose best fit P1 shows is statistically coincident with this theory's fixed point, relaxes it to ≈ 0.16 eV, comfortably above the floor. An earlier geometry-level pushforward placed the released weight near the normal-ordering sum, 0.07–0.08 eV `[ANALYSIS, prior baseline; unaudited here]`.

**Type, control, and falsifier.** The direction is guaranteed by the measured degeneracy; the magnitude requires the dedicated Boltzmann posterior, which has not been run and is flagged as the gating computation (K8). And the claim is disciplined by its own negative control: a null ensemble of 225 smooth positive transient histories, matched to the same early matter density and high-z distance, found 92.9% with CMB-lensing response cosine below −0.90, median −0.969 against this model's −0.972. Passing a test 93% of a null class passes is class membership, not discrimination; the lensing anti-alignment is _necessary_ structure, claimed as nothing more.

### P9 — The invariant, and where it can actually be tested

**Prediction.** 9(1+w(z))² + 6dw/dN = 4 at every redshift — the width law's fingerprint (§16).

**What background data can see — a result, not a caveat `[NEGATIVE]`.** Embed the theory in ρ_X ∝ sech^p(β(N−N_c)), for which

$$9X^2 + 6X' = X^2\Big(9 - \frac{18}{p}\Big) + 2p\beta^2,$$

constant iff p = 2. Profiling p against DESI DR2 + Pantheon+ gives **Δχ² = 0.79 across p ∈ [0.05, 20]** — no 1σ bound at all; p = 2 sits at 0.88σ; adding a Planck acoustic anchor as a 14th BAO point, D_M(z*)/r_d = 94.32 ± 0.28, changes 0.79 to 0.78. The reason is structural: the data span θ ∈ [−0.42, +0.28], less than one transition width, and p controls tails where ρ_X is subdominant; along the degenerate direction w(z) moves < 0.03 over the data range while the invariant swings two decades. **Background expansion data are provably insensitive to the invariant** — a statement about the information content of H(z) that applies to every dark-energy model and explains why P1–P7, not P9, is where current data bite.

**Where the test lives.** Growth (fσ₈) and CMB lensing weight the history through different functionals and _are_ tail-sensitive. Forecast: separating a smooth pulse from a sharp step needs ≈3.4× better background data (plausibly DESI-5yr + LSST); separating p = 2 from p = 1 needs ≈22×, which no planned background survey delivers — but which perturbation observables can once §25 supplies the covariant response. The perturbation sector gates the decisive observation as well as the theory's completion; K1 is executed by derivative-level reconstruction, not by distances.

### P10 — The far future, and the meaning of "no cosmological constant"

w → −1/3 exactly; a(t) ∝ t; the event horizon marginally absent; the e-fold budget splits 1:1 between horizon rapidity and horizon information; the acceleration era ends and never recurs. Any positive residual eventually dominates, restores the horizon, and bends w(z) back toward −1: exact zero and observational negligibility are different theories — the `[SECTOR]` choice made visible. Not testable on survey timescales; recorded because forced, and because a very-late-time w(z) floor is the one signature of Λ_res ≠ 0.

### 27.1 The density history

The model's dark density against the constant Λ-density of flat ΛCDM at the same Ω_m, both normalised to agree today as flatness requires:

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

**Dark energy is an episode, not an era.** At z = 3 the model carries 40% of Λ's density; two e-folds hence, 14%. The past-side deficit is the phantom branch and is where DESI's high-redshift BAO leverage lives; the future-side decay is the Komar shutdown of §17. In ΛCDM language: the "cosmological constant" is the tangent-line shadow of this pulse across the narrow window where we happen to observe it.

## 28. Observational status

**Pipeline `[ANALYSIS]`.** DESI DR2 BAO (13 measurements, 7 tracers, within-tracer correlations) [31] plus Pantheon+ (1580 SNe after z_HD > 0.01 and calibrator removal, full STAT+SYS covariance) [33, 34]; N_data = 1593; c/(H₀r_d) and the SN absolute magnitude profiled analytically. Validation against published ΛCDM constraints: Pantheon+ alone Ω_m = 0.3324 ± 0.018 (published 0.334 ± 0.018); DESI alone Ω_m = 0.2970 ± 0.0086 and H₀r_d = 101.56 (published 0.2975 ± 0.0086 and 101.54 ± 0.73). Further DR2 releases (Lyα full-shape [56]) are not yet folded in.

**Model comparison.**

|model|dark params|k|χ²|Δχ²|ΔAIC|
|---|---|---|---|---|---|
|flat ΛCDM|0|3|1400.142|0|0|
|**this model**|**0**|**3**|**1396.762**|**−3.380**|**−3.380**|
|ϱ⊥ free|1|4|1395.596|−4.545|−2.545|
|CPL (w₀, w_a)|2|5|1394.980|−5.162|−1.162|
|invariant-constant|2|5|1394.868|−5.274|−1.274|
|free-shape sech^p|3|6|1394.024|−6.118|−0.118|

Best AIC of the six at zero dark-parameter cost; the released-parameter extensions of its own family buy little (ϱ⊥ free gains 1.17 for one parameter; the full shape family 2.74 for three). An earlier independent baseline run (filed with v7.0) gave 1401.63 / 1398.29 / 1397.26 on a slightly different data preparation — consistent Δχ² ≈ −3.3 at equal count — and is superseded by the validated table above (C5). The correct reading, stated once: **viability at zero cost plus best-in-class information efficiency**, not a discovery statistic, and no discovery is claimed from it. The discovery-class statements are P1–P5; the table certifies that a shape fixed before the fit competes with families that spent two and three parameters after it.

**Direct determinations of the two unit laws.**

|quantity|declared|measured|tension|
|---|---|---|---|
|ϱ⊥ (width)|1|0.800, 1σ [0.575, 0.982]|1.08σ|
|ℜ_c (amplitude)|1|1.025, 1σ [0.941, 1.088]|0.3σ|
|z_c (solution datum)|0.342|0.650, 1σ [0.293, open]|0.72σ|

## 29. Kill conditions

Each condition names the statement it executes; each is triggerable by data of the current or next survey generation unless marked otherwise.

- **K1 → R5/R6 (binary-affine core).** A statistically significant redshift dependence of 9(1+w)² + 6w′, in a derivative-level reconstruction with honest covariance. (Background distances cannot execute this — P9.)
- **K2 → closed branch.** A combined posterior excluding the locus w_a = (3/2)(1+w₀)² − 2/3 at high significance; excluding the benchmark point while Ω_m stays near 0.31 kills the closed theory.
- **K3 → R7.** Reconstructed w = −1 crossing and dark–ordinary equality separating beyond errors (also executes P4).
- **K4 → closed branch.** A robust model-independent j₀ near +1 excluding −0.11.
- **K5 → R6/branch.** A clean, non-boundary-dominated determination of ϱ⊥ above the ceiling 1.814, or excluding 1 at several σ.
- **K6 → R7 (structural).** The Q2 first-principles computation of (k_B/S)G⊥_NN at a dynamical FLRW self-dual wall returning a value inconsistent with 1.
- **K7 → framework.** A dark history with multiple maxima or repeated crossing episodes; or the crossing localised robustly away from the flatness-determined date (e.g. z_c > 0.6 with Ω_m ≈ 0.31).
- **K8 → P8 / perturbation claim.** The dedicated Boltzmann posterior for this background still forcing Σm_ν < 0.059 eV; or every derived perturbation completion proving unstable, acausal, or arbitrarily tunable, or realising a bound-state count ≠ 1.

The scale-tractor reformulation and the vacuum-blind quotient survive failure of the late-time capacity model; the dependencies are deliberately modular.

---

# Part VIII — Economy

## 30. Four economies and the competition

Parameter count alone is not explanatory economy. Distinguish:

$$\mathcal{E}_{\rm fit} = \text{fitted parameters}, \quad \mathcal{E}_{\rm law} = \text{postulated laws/functions}, \quad \mathcal{E}_{\rm ontology} = \text{new fields/fluids/forces}, \quad \mathcal{E}_{\rm consequence} = \text{predictions locked together}.$$

Epicycles fail because corrections are _independently adjustable_; a fixed but unexplained function can have zero fitted parameters and still be ad hoc. This theory's account: 𝓔_fit = 0; 𝓔_law = two unit principles plus one sector bit, each falsifiable and two of them already measured; 𝓔_ontology = 0 new fields (a constitutive response of existing structure); and 𝓔_consequence is the lockstep — one density maximum, one crossing, the invariant, one acceleration interval with dated endpoints, the future separatrix, the self-dual amplitude, the canonical Witten pair, and vacuum blindness, all from ⟨Q²⟩ = 1 plus two units.

|model|extra dark-history parameters|free functions|new dimensionful constants|
|---|---|---|---|
|flat ΛCDM|0|0|1 (Λ)|
|PEDE [35]|0|0|1|
|vacuum metamorphosis [36]|0|0|1|
|running vacuum [37]|1|0|1|
|holographic DE (future horizon) [48, 49]|1 (c²)|0|0|
|CPL [43, 44]|2|0|1|
|interacting dark energy|1+|**1** (kernel)|1|
|**this model**|**0**|**0**|**0**|

Parameter count does not separate this model from PEDE or vacuum metamorphosis; two things do. First, the last column: every constant here already appears in the Einstein equation and quantum mechanics, and the one constant unique to dark sectors — a dimensionful amplitude — is absent, replaced by the relational ½ρ_crit,c of §11–12. Second, the lockstep: a competitor can match the curve; matching P4 + P5 + P6 + P9 simultaneously is what the ledger prices. Tanh-crossing fitting families reproduce the background with two shape parameters and none of the locks.

**The musical-chairs test, answered in advance.** Every positive ρ_X(a) is some effective fluid, and sech²/tanh profiles exist in the fitting literature — so the background curve alone is not the claim. The claim is the independent map Φ: ℝ_Weyl → 𝒮(𝒜) with pullback sech²θ dθ², constructed from cocycle data with cosmology entering only as solution data. The criterion: θ defined by rearranging H(z) ⟹ relabelled fluid; θ defined by an independent causal-state construction ⟹ physical structure. The construction-level test is passed; the in-practice computation of θ(N) from an explicit FLRW wall-state family is Q3, stated as the theory's own completion criterion. A relabelled fluid has no Q3 to state.

**Relation to thermodynamic gravity.** Jacobson derives the Einstein equation from a Clausius relation at local horizons [9, 10]; this theory takes the field equation as given (in tractor form) and derives the _source in the scale channel_ from modular response — complementary uses of the same modular data, neither modifying the force law.

**Stopping condition.** A foundational theory need not derive every axiom from something deeper. It is adequate when primitives are typed; independent representations are connected by explicit equivalence laws; no hidden functions fit individual anomalies; the laws produce many linked predictions; failure conditions are stated; and further elaboration concerns new regimes, not repair of the background law. By that standard the homogeneous theory has reached a defensible stopping point: R6 and R7 are its declared laws, §29 its failure conditions, and §§32–33 its new regimes.

---

# Part IX — Audit record

## 31. Two withdrawals, their autopsies, and what replaced them

Adversarial audit of Revision 2's closure (conducted in the v7.0 lineage) identified two invalid deductions. Both are accepted, withdrawn, and autopsied here; the register at §31.4 is the permanent record. Nothing numerical changed: every benchmark value, every ledger entry, and both measured unit values are identical before and after — what changed is the logical status of two links, which is exactly what a working register is for.

### 31.1 What the audit confirmed

Retained from Revision 2 without change: the vertical/horizontal distinction; the BKM Hessian of the modular-rescaling family as a capacity/variance `[THEOREM]`; the self-dual crossing as the natural evaluation point; the demand that the theory end in one structural law rather than an expanding assumption ledger; and the open status of the perturbation sector.

### 31.2 Withdrawn: conformal-weight integrality (Revision 2 §14a)

**The claim.** The null-pair grading L₊ ⊕ L₋ and density pair 𝓔[1] ⊕ 𝓔[−1] force ϱ⊥ ∈ ℤ⁺; the existence ceiling then excludes every integer ≥ 2 at the measured Ω_m; hence ϱ⊥ = 1 as a theorem.

**Why it fails.** The first premise is false. Conformal density bundles 𝓔[w] exist for every real w; the characters of the multiplicative group ℝ₊ form the continuum r ↦ r^s, s ∈ ℝ. There is no compact group in the problem and therefore no character lattice; "up to tensor powers" smuggled in a discreteness the representation theory does not supply.

**What the failure is not.** The _logic_ — a discrete menu plus observational exclusion, the pattern of "the gauge group is SU(3)×SU(2)×U(1)" — is programme-legitimate and is retained as a pattern. It failed here only because the menu is not discrete; with a continuum of admissible characters, the argument reverts to measuring a continuous parameter, which is what R6 now honestly declares instead of deriving.

**Surviving remnants.** (i) The fundamental-character identification — both graded pairs carry e^{±x}, and R6 states that fundamental couples to fundamental — survives as the content of the postulate. (ii) The existence ceiling survives as a genuine prediction and consistency bound (§14, P7, K5). (iii) A Euclidean-periodicity route to re-deriving integrality is filed `[OPEN]` in §9, with its two recorded obstructions, and counted as nothing.

### 31.3 Withdrawn: the normal plane as a two-dimensional CFT (Revision 2 §16b)

**The claim.** The horizontal sector is the chiral algebra of the two-dimensional normal plane; Cardy's formula for a 2D CFT gives S ∝ T, hence C = S, hence the capacity ratio is 1 as a theorem.

**Why it fails.** A two-dimensional Lorentzian normal vector space is a _fiber_ of the normal bundle at a cut, not a 1+1-dimensional spacetime carrying a conformal quantum field theory. Cardy's formula requires a CFT, a Hamiltonian, a central charge, boundary conditions, and a thermodynamic regime [39]; the dimension of a plane supplies none of them.

**Surviving remnants.** (i) The exponential-family identity G_λλ = Var(K) = C_E `[THEOREM]`, verified to 10⁻⁶, and the identification of the horizontal direction with modular rescaling — the correct half of the old §16. (ii) The fixed-localisation argument separating horizontal from vertical capacity classes, with the vertical class excluded by direct fit — now supporting structure for the vertical/horizontal split rather than a derivation. (iii) The capacity-class taxonomy γ = d ln S/d ln T (Appendix A.7) survives as the classification the data used to kill the rivals (S12). (iv) The _serious_ version of the withdrawn idea exists in the literature: near-horizon Virasoro constructions that derive horizon thermodynamics from an emergent 2D conformal symmetry [57]. Establishing one at the self-dual FLRW wall would upgrade R7 from principle to theorem; that is precisely Q2, and this is the constructive residue of the withdrawal.

### 31.4 Withdrawn-claims register

|claim|filed as|killed by|status now|surviving remnant|
|---|---|---|---|---|
|ϱ⊥ ∈ ℤ from conformal-weight integrality|Rev 2 §14a `[THEOREM]`|continuum of real characters; 𝓔[w] for all real w|withdrawn (C2)|fundamental-character content of R6; ceiling as bound; Euclidean route `[OPEN]`|
|horizontal sector = 2D chiral CFT; Cardy ⟹ C = S|Rev 2 §16b `[THEOREM]`|a fiber is not a field theory; Cardy's hypotheses absent|withdrawn (C3)|Var(K) = C_E `[THEOREM]`; capacity-class taxonomy; Q2 as the upgrade path [57]|

(Revision 1's jerk sign is a corrected error, not a withdrawn claim; it is indexed as C1.)

### 31.5 Why the revised closure is stronger

The final laws require no integrality theorem and no assumed CFT. ℜ_c is coordinate-invariant, combining slope and capacity into one measurable number; its precedents are theorems in controlled settings rather than category errors; its consequences (Ω_X,c = ½, equality, the general-d formula) are algebra; and it stands exposed to an independent first-principles computation (Q2/K6) that the old "theorems" would have falsely preempted. Two honest principles with measured values and stated kill conditions constrain more than two invalid proofs.

### 31.6 The v5.0 gating decision, closed

v5.0 carried two incompatible specifications of its modular–Weyl coefficient — a horizon identity in one section, flat soldering in another, disagreeing by factors of 1.5–4 off de Sitter — and an amplitude proportional to H₀² that its own type rules classed as a clock reading. Three exits were posed: reidentify the cut; decouple the state rapidity from the geometric rapidity; find stabilising structure in the constitutive law. **Exit 2 is taken.** The vertical/horizontal split (§3, §5, §19) makes θ and η_A different coordinates with the exact residual relation θ′ − η′_A = ¼(ln 𝒮_A)′, which is what the old single coefficient was failing to be; and the scale-capacity law anchors the amplitude at the intrinsic self-dual event, dissolving the clock-reading objection (§10, S3). The coincidence-problem verdict recorded then — "assumed, not predicted" — is superseded by the present split verdict in S10: equality at the crossing is now a consequence of a declared law (`[PRINCIPLE]` + `[DEDUCTION]`), the crossing date is solution data, and the epoch question remains honestly open.

### 31.7 Errata absorbed

v7.0's §7.3 cited its capacity references where the sequestering papers belong (fixed here as [26, 27] of this list, C4); its background χ² table was the earlier baseline run (superseded, C5); its prediction chapter dropped the quantitative ledger, per-axis offsets, robustness sweeps, the negative control, and the invariant-invisibility result — all restored in §§26–28.

---

# Part X — Programme

## 32. Open problems

**Q1 — the response map.** Construct 𝓡_Σ under the six constraints of §25 and lift the Witten complex to a Lorentzian perturbation system. Gates the perturbation sector, the P9 observation, and any CMB/growth likelihood. A classification problem for natural bilinear operators, not a search for an action.

**Q2 — the FLRW self-dual wall.** Construct the scale-indexed algebras and states of a dynamical flat-FLRW apparent-horizon cut, prove or refute geometric modular flow there, and **compute (k_B/S)G⊥_NN from modular data** — deriving or falsifying ℜ_c = 1 (K6) and, if a near-horizon Virasoro structure exists [57], upgrading R7 to a theorem. Every historical extension of geometric modular flow — wedge [6], CFT ball [7], stationary horizons and perturbations [20, 21, 22] — landed on marginal causal surfaces; the self-dual cut is exactly such a surface. The sharpest mathematical problem the theory poses.

**Q3 — explicit θ(N).** Compute the Connes cocycle for a concretely specified FLRW causal-diamond state family and exhibit θ(N) without cosmological input, completing the musical-chairs test in practice.

**Q4 — Λ_res.** Which global flux sector nature selects is not derived; sequestering [26, 27] is the type-compatible published completion; P10 states the observable stakes; the fluctuating-residual alternative is the recorded rhyme of §21.

**Q5 — the Keller correspondence `[RHYME]`.** Reflectionless potentials are those with rational KdV spectral curves; Keller-map obstructions live in branched-cover data of a discriminant. Both instantiate "trivial local invariant, nontrivial global remainder." Whether the ℓ = 1 Pöschl–Teller spectral curve is the Keller curve at the relevant degeneration is checkable and unchecked; until checked, counted as nothing.

## 33. A programme for the next investigator

1. Run P3, P4, P6 and the P1 locus test on published nonparametric w(z) reconstructions — four predictions from one reconstruction, no new theory required.
2. Run the dedicated Boltzmann posterior for this background against DESI DR2 + CMB with Σm_ν free (P8/K8) — the fastest route to a new failure mode or a resolved tension.
3. Build the ϱ⊥ determination table across DR1/DR2 × supernova compilations × with/without lensing via ϱ⊥² = [9(1+w₀)² − 6w_a]/4 with real covariances, marking boundary-dominated entries against the §14 ceiling.
4. Attack Q2 in a controlled ladder: driven 2D CFT, holographic balls, perturbative gravitational crossed-product algebras, then the FLRW wall — with the capacity ratio as the computable target at each rung.
5. Attack Q1 as classification under the six constraints, not by guessing an action.
6. Keep the register: any new closure claim enters with its kill condition pre-filed, per §29's pattern.

---

# Scholium — Objections and replies

The thirteen objections most worth answering, answered. Each reply is self-contained; where it rests on a computation, the carrying section is cited.

**S1. "Any ρ(a) is some w(z). You have relabelled a fluid."** Correct as a statement about background curves, which is why the musical-chairs criterion of §30 is set before anything is derived. The difference between a relabelling and a theory is whether the new variable is constructible without the data it predicts. θ is defined by the Connes cocycle of scale-indexed states (§9) — an object that exists whether or not anyone measures H(z) — and the chain §§8–14 turns it into predictions with cosmology entering only as solution data. The construction-level test is passed; the in-practice computation of θ(N) from an explicit state family is Q3, stated as the theory's own completion criterion. A relabelled fluid has no Q3 to state.

**S2. "sech² has an amplitude and a centre. Two hidden parameters."** Both are fixed. The amplitude is ½ρ_crit,c — the ½ from the free-energy Hessian (§10), ρ_crit,c from the Misner–Sharp bridge (§11), the unit coefficient from the scale-capacity law (R7, measured at P5). The centre is the unique minimum of the symmetrized modular relative entropy (§12), dated by flatness. The exponent is not selected from a family: sech² is the variance of a normalised binary, the only information geometry a two-outcome structure possesses. The accounting is §30's table, where this row alone has three zeros.

**S3. "½ρ_crit,c is a clock reading dressed as a derivation — the amplitude secretly tracks H²."** The objection has the type theory right and the verdict wrong. A constant of nature is an input that could have been otherwise; a clock reading is a measurement of when you are. The amplitude here is neither: it is a law-valued functional of the matter history, evaluated at an _intrinsic_ event — the unique self-dual state — so that given flatness and Ω_m nothing about it could have been otherwise. The H² scaling that looks suspicious is the marginality identity doing its job (§11). What would be a disguised constant is a coefficient left free in front; R7 closes that coefficient as a declared, measured law, and K6 exposes it to first-principles refutation. This objection retired the v5.0 formulation and is the reason the present one anchors at N_c (§31.6).

**S4. "You used data (Ω_m) inside a 'derivation'."** In Revision 2, yes — and the derivation it served is withdrawn (§31.2). In the present formulation cosmological data enter no derivation: Ω_m and Ω_r are solution data locating N_c (§15), and the ceiling is a consistency bound (§14), not a selector. The old defence — discrete selection by data among representation-theoretic alternatives, as with the Standard Model gauge group — was sound logic resting on a false discreteness premise; with the premise gone, the defence is retired with it. What remains is cleaner: declared units, measured values, no data inside any derivation at all.

**S5. "w crosses −1. That means ghosts, or a violated null energy condition."** For a fundamental fluid or a single minimally coupled scalar, yes — and the theory _proves_ it as N2, at exactly the critical inverse-square coupling where fall-to-the-centre begins [28, 30]. That no-go is why θ is typed as a collective constitutive coordinate (§10): the same type as temperature, which also gravitates, also has profiles, and also supports effective w < −1 histories in composite descriptions without a propagating ghost. The NEC constrains propagating degrees of freedom; the propagating content here is the transmitted continuum of a reflectionless operator with retarded analytic structure (§23). The crossing is real, and the fluid picture is what fails at it — on schedule.

**S6. "This is holographic dark energy with extra steps."** HDE posits ρ ∝ L⁻² for a chosen cutoff with a fitted coefficient c², yielding a one-parameter family, no crossing without further choices, and no differential invariant [48, 49]. Here no IR-cutoff postulate exists: ρ_crit,c appears as a theorem at one intrinsic epoch only, the profile away from it is the binary variance, the coefficient is a measured unit law, and the predictions pricing the difference — P4, P6, P9 — are ones HDE does not make.

**S7. "Geometric modular flow at a cosmological horizon is unproven; the theory hangs on it."** Correct, and stated wherever it matters (§5, §8, Q2). What is proved: the wedge [6], the CFT diamond [7], stationary horizons and controlled perturbations [20, 21, 22]. The self-dual FLRW cut is a marginal causal-information surface of exactly the kind these results have successively reached, and the theory's wager is that the pattern completes. The wager is priced: if Q2 fails, ℜ_c = 1 loses its best route to a derivation and survives only as the measured 1.025 ± 0.07 of P5 — a principle with one leg. A theory should hang on something, and should say what.

**S8. "Δχ² = −3.4 is nothing."** It is not offered as something; §28 types it as viability at zero cost. Its information content is comparative: best AIC at equal parameter count against families that spent two and three post-hoc parameters, from the only entrant whose shape was fixed before contact with the data. The staked claims are P1–P5 — a fixed point inside the DESI 1σ region, a jerk a full unit from ΛCDM's, a forced triple coincidence, two measured unit laws — and P9 states precisely why background χ² was never going to be the arena.

**S9. "What does the theory not explain?"** The early universe, inflation, the matter and radiation content, the value of Ω_m, the hierarchy of forces, the selection of the expanding branch, and quantum gravity. It is a theory of the scale register's response — the existence, shape, amplitude, timing, orientation, and future of the dark sector, plus local vacuum blindness — nothing else. Scope is not modesty; it is type discipline.

**S10. "The coincidence problem survives: why do we live near N_c?"** Split the question. "Why does dark equal ordinary at the crossing?" — consequence of the amplitude law (R7 `[PRINCIPLE]` ⟹ `[DEDUCTION]`, §12); ΛCDM must tune Λ for it, this theory cannot avoid it, and the equality is independently testable (K3). "Why is the crossing at z ≈ 0.34?" — solution data from Ω_m (§15), confirmed within the DESI band (P3). "Why is the observation epoch within an e-fold of N_c?" — equivalent to "why is Ω_m today ≈ 0.3," a fact about the matter sector and the observer's date that no background theory derives and this one does not claim. What the theory removes is the tuned constant: there is no dial whose setting makes the epochs meet. Quantitatively the coincidence is milder than ΛCDM's: on the future side ρ_X/ρ_m grows only linearly in a (ΛCDM: cubically), so near-equality occupies a wider swath of history.

**S11. "The vacuum catastrophe is 'dissolved' by fiat — you defined the coupling away."** The blindness is two theorems that meet (§19, §21). Information side: a central shift does not change the state, so no monotone metric — not just BKM — can assign it length; mathematics, not model-building. Geometric side: the trace-free Einstein equation annihilates λg_ab identically; the tractor form of GR, not a modification. What is _chosen_ is the global flux sector Λ_res = 0, filed with its sequestering pedigree [26, 27] and its observable signature (P10) without disguise.

**S12. "Why a binary? Nature might realise richer structure at the cut."** The candidates were computed, not dismissed. A higher soldering power ϱ⊥ ≥ 2 is representation-theoretically admissible and is excluded by the flatness ceiling plus Ω_m at 3.8σ and Δχ² = 60 (§14) — and would, independently, predict a permanently decelerating future. A bulk-thermal capacity class (ℜ_c = 3) forces Ω_X,c = 3/2 and is excluded by flatness itself; a Schwarzschild-like class (ℜ_c = −2) by sign; the vertical-temperature normalisation (amplitude ×μ_A) by direct fit (§11, P5). The binary with unit width and unit amplitude is not merely the minimal choice consistent with the cut's two null normals; it is the last configuration standing after its rivals' consequences were derived and killed by data. That is what "minimal" is required to mean here.

**S13. "Revision 2 had two theorems; v8.0 has two postulates. The theory got weaker. And isn't ℜ_c just γ renamed?"** The _claims_ got weaker; the theory did not move by one digit. Every benchmark value, every ledger entry, both measured unit values, and the closed history are identical before and after the withdrawals — compare §26 here with Revision 2's §26. What changed is bookkeeping, in the direction that matters: two invalid proofs were converted into two declared laws, each now exposed to an independent first-principles computation (Q2) and a named kill condition (K5, K6) that the false theorems would have preempted. On the renaming: operationally yes — ℜ_c is the quantity the γ fit measured — and the rename marks exactly the two corrections: the logical status (`[THEOREM]` → `[PRINCIPLE]`) and the packaging (a reparametrisation- invariant number replacing a convention-dependent slope²×capacity split). The programme's standard was never "zero postulates"; it is zero free functions and honest labels. Both hold, and the register that records the withdrawals is what distinguishes a research programme from a fit that cannot be wrong.

---

# Appendix A — Core derivations

**A.1 Binary moments.** For ω_θ = e^{θQ}/(2cosh θ) with Q² = 1: Ψ = ln tr e^{θQ} = ln(2cosh θ), ⟨Q⟩ = Ψ′ = tanh θ, Var(Q) = Ψ″ = sech²θ, hence ⟨Q⟩² + Var(Q) = ⟨Q²⟩ = 1.

**A.2 The invariant, generalised.** With ρ_X = ρ_* sech²[ϱ⊥(N−N_c)], define Δ_X := −d ln ρ_X/dN = 2ϱ⊥tanh θ. Then Δ′_X = 2ϱ⊥²sech²θ = 2ϱ⊥² − ½Δ_X², so

$$\Delta_X^2 + 2\Delta_X' = 4\varrho_\perp^2 \iff 9(1+w_X)^2 + 6w_X' = 4\varrho_\perp^2,$$

the unit-width case being R12. The invariant measures the width independently of amplitude and date; receipts verify it at ϱ⊥ ∈ {0.8, 1, 1.5}.

**A.3 Fisher length.** ds_F = sech θ|dθ|, so L_F = ∫sech θ dθ = π, equal to ∫₀¹dp/√(p(1−p)), the binary simplex diameter. The flat coordinate is the Gudermannian φ = gd(θ).

**A.4 Slot separation.** For ψ_NN + [K² + cρ_X]ψ = 0 with ρ_X = χ⊥ϱ⊥²sech²θ, substituting θ = ϱ⊥(N−N_c) gives ψ_θθ + [K²/ϱ⊥² + cχ⊥sech²θ]ψ = 0: the pullback factor cancels the chain-rule factor, ϱ⊥ occupies the eigenvalue slot and the amplitude the potential-strength slot. One coefficient cannot perform both roles — why the invariant measures the width independently of the amplitude, i.e., why P5 and P7 are two measurements and not one.

**A.5 The two ceilings.** _Width:_ with x = −N_c > 0, dust flatness is e^{3x}sech²(ϱ⊥x) = T_m, T_m = (1−Ω_m−Ω_r)/Ω_m. d ln F/dx = 3 − 2ϱ⊥tanh(ϱ⊥x) gives one root for ϱ⊥ ≤ 3/2 and two-or-none above; at the double root, eliminating x yields the closed form of §14, with brentq root 1.8141 at the benchmark. _Amplitude:_ Ω_X,c = ℜ_c/2 and ρ_ordinary,c > 0 give ℜ_c ∈ (0, 2); ℜ_c = 1 is the midpoint and the unique equal-partition value.

**A.6 The Witten factorisation.** 𝒜†𝒜 = −∂²_θ + η² − η′, 𝒜𝒜† = −∂²_θ + η² + η′; with η = tanh θ, η² + η′ = 1 makes ℋ₊ free and η² − η′ = 1 − 2sech²θ. Zero mode ψ₀ = 2^{−1/2}sech θ; continuum ψ_k = (−ik + tanh θ)e^{ikθ}, R(k) = 0.

**A.7 Capacity as a thermodynamic exponent.** For ρ_β = e^{−βH}/Z the modular Hamiltonian is K = βH + ln Z, so ⟨K⟩ = S/k_B and Var(K) = β²Var(H) = C/k_B. Hence C/S = d ln S/d ln T, and S ∝ T^a gives C/S = a: bulk thermal CFT in d = 4, a = 3; horizon varied by size, a = −2; S ∝ T, a = 1. In Revision 2 this table fed a Cardy derivation now withdrawn (§31.3); its honest role is the classification by which the rival capacity classes were computed and killed (S12).

**A.8 The benchmark closure.** With ϱ⊥ = ℜ_c = 1 and x = −N_c, flatness today reads

$$\big(\Omega_{m0}e^{3x} + \Omega_{r0}e^{4x}\big)\operatorname{sech}^2x = 1 - \Omega_{m0} - \Omega_{r0},$$

with unique benchmark root x = 0.2940066, z_c = e^x − 1 = 0.3417927. Then ρ_*/ρ_crit,0 = Ω_m0e^{3x} + Ω_r0e^{4x} = 0.7506311; Ω_X0 = 0.7506311 sech²x = 0.6893105; w₀ = −1 + (2/3)tanh x = −0.8094545; w_a = −(2/3)sech²x = −0.6122053; q₀ = ½[Ω_m0 + 2Ω_r0 + Ω_X0(1+3w₀)] = −0.3369025. At the crossing, q(N_c) = −¼ + ½Ω_r,c = −0.2499012 with Ω_r,c = 1.976×10⁻⁴, and μ_A(N_c) = (1−q_c)/2 = 0.6249506. Every entry of §26 follows.

**A.9 Kinematic identities and the jerk correction.** From q = −1 − H′/H one derives H″/H = (1+q)² − q′ and the exact identity

$$j = q + 2q^2 - \frac{dq}{dN},$$

equivalently j = 1 + (9/2)ΣᵢΩᵢwᵢ(1+wᵢ) − (3/2)ΣᵢΩᵢdwᵢ/dN, which returns j = 1 identically for ΛCDM [50]. Both routes give j₀ = −0.1112465; Revision 1's −0.1085454 arose from the sign error j = q + 2q² + q′ and is superseded (C1). Corollary: dq/dN|₀ = q₀ + 2q₀² − j₀ = +0.0013505, locating the minimum of q at z = 0.0008.

**A.10 The CPL locus, generalised, and implied crossings.** At general width both tangent coefficients are functions of x alone: 1 + w₀ = (2ϱ⊥/3)tanh(ϱ⊥x) and w_a = −(2ϱ⊥²/3)sech²(ϱ⊥x), giving the locus

$$w_a = \frac{3}{2}(1+w_0)^2 - \frac{2}{3}\varrho_\perp^2 \iff \varrho_\perp^2 = \frac{9(1+w_0)^2 - 6w_a}{4},$$

reducing at ϱ⊥ = 1 to P1's curve and supplying the P7 estimator. Conversely any CPL fit implies a crossing at z_× = s/(1−s) with s = (1+w₀)/(−w_a); applied to the DESI DR2 combinations this gives z_× = 0.354 (Pantheon+), 0.405 (DES Y5), 0.440 (Union3).

**A.11 General-dimension conversion.** In d spatial dimensions, A = Ω_{d−1}R^{d−1}, V = Ω_{d−1}R^d/d, S/k_B = A c³/4Għ, k_BT = ħc/2πR, and flat Friedmann ρ_crit = d(d−1)c²H²/16πG give

$$\frac{k_BT(S/k_B)}{V} = \frac{d,c^2H^2}{8\pi G} = \frac{2}{d-1},\rho_{\rm crit},$$

hence Ω_X,c = ℜ_c/(d−1) and ρ_X,c/ρ_ord,c = ℜ_c/(d−1−ℜ_c); receipts verify d = 3…10.

**A.12 Clock-allocation identities.** 𝒮_A = πc⁵/GħH² gives d ln 𝒮_A/dN = −2 d ln H/dN = 2(1+q) exactly; with dη_A/dN = μ_A = (1−q)/2, μ_A + ¼·2(1+q) = 1, i.e. dN = dη_A + ¼d ln 𝒮_A. The tractor chain: I² = −½(1−q)H² ⟹ μ_A = −I²/H², and T_AS_A/E_A = (1−q)/2 with the Kodama–Hayward temperature.

**A.13 The free-energy Hessian.** For a KMS reference ω_c with ℋ_c = k_BT_cK_c, F_c(ρ) − F_c(ω_c) = k_BT_c S(ρ‖ω_c) exactly; at coincidence S(ω_{c+δN}‖ω_c) = ½G⊥_NN(N_c)δN² + O(δN³), so the quadratic free-energy curvature per causal-wall volume is ρ_X,c = (k_BT_c/2V_c)G⊥_NN(N_c) — R8's coefficient, with nothing hidden in the ½.

---

# Appendix B — Reproducibility

|script|verifies|
|---|---|
|`receipts_v8.py` (this revision)|the full merged suite: binary moments; the generalised invariant at ϱ⊥ ∈ {0.8, 1, 1.5}; Fisher length; slot separation; both ceilings (closed-form width root 1.8141; amplitude interval); the Hawking–Friedmann bridge and the general-d chain d = 3…10; the benchmark closure and every §26 entry including q(N_c), μ_A(N_c), Ω_r,c; the jerk identity both routes; the generalised CPL locus and implied crossings; clock allocation d ln 𝒮/dN = 2(1+q) and the μ_A regime table; the two-route q consistency; the saddle-node fixed points and three futures; the Witten factorisation, zero mode, and reflectionlessness; Chatterjee 𝔖_J, Hessian 8, and directedness; the density-history table; N1–N4|
|`receipts_revision2.py`|Revision 2's 37-check suite (all subsumed above; retained for the record)|
|`receipts_closure.py`, `receipts_transparency_fold.py`|prior-session suites; the closure script's integrality and Cardy checks are superseded by §31 and retained only as history|
|`P1/` package|data loaders with published-value validation; the §28 model table; the P9 p-profile and Planck anchor; the ϱ⊥, ℜ_c, z_c profiles|

All scripts require only numpy and scipy; the `P1/` package downloads Pantheon+ on first use. v8.0 changes no receipted number: the withdrawals of §31 changed labels, not values.

---

# Appendix C — Epistemic status ledger

|statement|status|
|---|---|
|causal order fixes conformal geometry (standard hypotheses)|`[STANDARD]` theorem [1, 2]|
|scale as Γ(𝓔[1]); scale tractor; Einstein ⟺ parallel I_A|`[STANDARD]` [3, 4, 5]|
|trace-free tractor source equation|exact reformulation of GR `[STANDARD]`|
|boost-charge unity for the local source|`[CONDITIONAL]` principle (§20)|
|fundamental normal chirality quotient|`[IDENTIFICATION]` (§8)|
|affine cocycle soldering|`[CONDITIONAL]` theorem (§9)|
|ϱ⊥ = 1|`[PRINCIPLE]` — fundamental representation (R6); measured P7|
|binary BKM metric sech²θ|`[THEOREM]` after chirality reduction|
|ℜ_c = 1|`[PRINCIPLE]` — scale–capacity equivalence (R7); measured P5|
|free-energy source law R8|constitutive definition, exact coefficient (A.13)|
|Hawking–Friedmann conversion R9|`[THEOREM]` in the stated regime|
|closed pulse R10; equality; invariant R12|`[DEDUCTION]` from the above|
|𝔖_J self-duality, Hessian 8, directedness|`[THEOREM]` [19]|
|Witten pair, zero mode, reflectionless continuum|`[THEOREM]` (§23)|
|N1–N4|`[NEGATIVE]`|
|general-d partition formula|`[THEOREM]` (A.11)|
|covariant perturbation theory|`[OPEN]` (Q1)|
|FLRW wall capacity from modular data|`[OPEN]` (Q2); kill K6|
|Λ_res = 0|`[SECTOR]` choice; sequestering as published candidate|
|observational pipeline results|`[ANALYSIS]` (§28)|
|integrality of ϱ⊥; 2D-CFT Cardy closure|**withdrawn** (§31)|

---

# Appendix D — Symbol dictionary

|symbol|definition|type / status|
|---|---|---|
|(M, [g])|conformal spacetime|standard Lorentzian conformal geometry|
|σ ∈ Γ(𝓔[1])|positive scale section|metric calibration; g_phys = σ⁻²g|
|I_A = ¼D_Aσ|scale tractor|packages the scale two-jet|
|P_ab, J|Schouten tensor and its trace|standard conformal curvature|
|N = ln(a/a_c)|Weyl e-fold coordinate|additive scale displacement|
|s|vertical modular parameter|automorphism flow at fixed state|
|η_A|vertical horizon rapidity|dη_A/dN = μ_A; geometric definition|
|θ|horizontal state coordinate|noncentral relative modular polarisation|
|Q = P₊ − P₋|normal chirality|Q² = 1, JQJ = −Q|
|Ψ(θ) = ln(2cosh θ)|log-partition potential|binary exponential family|
|η = ⟨Q⟩ = tanh θ|mixture coordinate|dual to θ|
|G^BKM|BKM metric|Hessian of Umegaki relative entropy|
|G⊥_NN|pullback BKM norm|extensive horizontal capacity per e-fold²|
|C_⊥,c|extensive capacity at crossing|= Var(K) for the selected mode|
|S_c, T_c, V_c|wall entropy, horizontal temperature, areal volume|Bekenstein–Hawking; ħc/2πk_BR_c; 4πR_c³/3|
|ℜ_c|Ruble number (k_B/S_c)G⊥_NN(N_c)|`[PRINCIPLE]` value 1; measured 1.025|
|ϱ⊥|soldering slope dθ/dN|`[PRINCIPLE]` value 1; measured 0.800|
|ρ_X, w_X|response density and equation of state|R10, R11|
|N_c, z_c|self-dual crossing|intrinsic event; date from flatness|
|x = −N_c|crossing displacement|benchmark 0.2940066|
|μ_A = (1−q)/2|horizon modular–Weyl index|= −I²/H² = T_AS_A/E_A|
|𝒮_A|dimensionless horizon entropy|πc⁵/GħH²|
|𝔖_J|symmetrized relative entropy|4θ tanh θ [19]|
|𝒜, 𝒜†, ℋ±|Witten/Darboux pair|ℓ = 1 Pöschl–Teller + free|
|𝓡_Σ|perturbation response map|`[OPEN]`, six constraints (§25)|
|Λ_g, Λ_res|scalar lift / global residual|`[SECTOR]`; zero on the rigid branch|
|γ|retired symbol (Revision 2)|content = ℜ_c|

---

# References

Numbering [1]–[50] continues Revision 2's list for cross-document stability; [51]–[57] are new in v8.0.

[1] Hawking, King, McCarthy, _J. Math. Phys._ **17** (1976) 174. [2] Malament, _J. Math. Phys._ **18** (1977) 1399. [3] Bailey, Eastwood, Gover, _Rocky Mountain J. Math._ **24** (1994) 1191. [4] Curry, Gover, arXiv:1412.7559. [5] Gover, _J. Geom. Phys._ **60** (2010) 182. [6] Bisognano, Wichmann, _J. Math. Phys._ **17** (1976) 303. [7] Casini, Huerta, Myers, arXiv:1102.0440. [8] Wald, arXiv:gr-qc/9307038. [9] Jacobson, arXiv:gr-qc/9504004. [10] Jacobson, arXiv:1505.04753. [11] Jafferis, Lewkowycz, Maldacena, Suh, arXiv:1512.06431. [12] Lashkari, Van Raamsdonk, arXiv:1508.00897. [13] Czech, Lamprou, McCandlish, Sully, arXiv:1712.07123. [14] Czech et al., arXiv:2305.16384. [15] Petz, _Linear Algebra Appl._ **244** (1996) 81. [16] Čencov, _Statistical Decision Rules and Optimal Inference_, AMS (1982). [17] Amari, Nagaoka, _Methods of Information Geometry_, AMS/Oxford (2000). [18] Grasselli, Streater, arXiv:math-ph/0006030. [19] Chatterjee, arXiv:2605.19106. [20] Jensen, Sorce, Speranza, arXiv:2306.01837. [21] Faulkner, Speranza, arXiv:2405.00847. [22] Chandrasekaran, Flanagan, arXiv:2601.07915. [23] Hayward, arXiv:gr-qc/9710089. [24] Cai, Kim, arXiv:hep-th/0501055. [25] Kastor, Ray, Traschen, arXiv:0904.2765. [26] Kaloper, Padilla, Stefanyszyn, Zahariade, arXiv:1505.01492. [27] Kaloper, Padilla, arXiv:1606.04958. [28] Vikman, arXiv:astro-ph/0407107. [29] Lekner, _Am. J. Phys._ **75** (2007) 1151. [30] Camblong, Epele, Fanchiotti, García Canal, arXiv:hep-th/0003014. [31] DESI Collaboration, arXiv:2503.14738 (DR2 BAO: cosmological constraints). [32] DESI Collaboration, arXiv:2503.14744 (DR2: neutrino constraints). [33] Scolnic et al., arXiv:2112.03863 (Pantheon+ sample). [34] Brout et al., arXiv:2202.04077 (Pantheon+ cosmology). [35] Li, Shafieloo, arXiv:1906.08275 (PEDE). [36] Parker, Raval, arXiv:gr-qc/0312108 (vacuum metamorphosis). [37] Solà Peracaula et al., arXiv:2203.13757 (running vacuum). [38] Witten, _Nucl. Phys. B_ **202** (1982) 253. [39] Cardy, _Nucl. Phys. B_ **270** (1986) 186. [40] Gover, Latini, Waldron, _Mem. AMS_ **235** (2015). [41] Curry, Gover, arXiv:2208.09302 (almost-Einstein matter and the scale tractor). [42] Misner, Sharp, _Phys. Rev._ **136** (1964) B571. [43] Chevallier, Polarski, arXiv:gr-qc/0009008. [44] Linder, arXiv:astro-ph/0208512. [45] Unruh, _Phys. Rev. D_ **14** (1976) 870. [46] Haag, _Local Quantum Physics_, Springer (1996). [47] Takesaki, _Theory of Operator Algebras II_, Springer (2003). [48] Cohen, Kaplan, Nelson, arXiv:hep-th/9803132. [49] Li, arXiv:hep-th/0403127 (holographic dark energy). [50] Visser, arXiv:gr-qc/0309109 (jerk and cosmography). [51] de Boer, Järvelä, Keski-Vakkuri, arXiv:1807.07357 (capacity of entanglement). [52] Banks, Zurek, arXiv:2108.04806 (near-horizon vacuum states). [53] Banks, Draper, arXiv:2404.13684 (entanglement capacity of de Sitter). [54] Verlinde, Zurek, arXiv:1911.02018 (modular fluctuations, ⟨ΔK²⟩ = ⟨K⟩). [55] Akbar, Cai, arXiv:hep-th/0609128 (Friedmann thermodynamics at the apparent horizon). [56] DESI Collaboration, arXiv:2607.27410 (DR2: Lyα full-shape). [57] Carlip, arXiv:gr-qc/9812013 (horizon entropy from conformal symmetry).