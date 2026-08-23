# CAUSAL-SCALE PARTITION GEOMETRY

## A master document: definitions, identity tower, empirical pipeline, falsifiers, and research program

**Status.** Self-contained foundation document. Every identity marked [T·] is machine-verified symbolically and every number in §7 is generated from the stated inputs by the accompanying certificate `verify_cspg_master.py`. Nothing below claims to derive the values of physical constants; two boundary numbers are empirical inputs, exactly as G is Newton's and c is Einstein's. The claim is structural: the homogeneous universe, conventionally described by a basket of substances and a list of puzzles, is one concave curve — mathematically a **free energy** — whose slope, bend, and higher derivatives *are* the standard cosmological observables.

---

# PART I — MOTIVATION AND PRIMITIVES

## 1. The problem this notation solves

Standard background cosmology carries a large inventory of apparently independent items: an expansion history a(t); a deceleration parameter; a flatness puzzle; a horizon problem; a "coincidence" that the Hubble sphere's compactness sits near the Schwarzschild value; a dark-energy substance with a tuned equation of state; an inflaton field with a potential (a *function's* worth of freedom); a "why now" coincidence; and four separately-quoted big numbers (Hubble radius, Hubble mass, horizon entropy, holographic qubit count). The standard of value adopted here is the one met by ψ and by E = mc²: **fit the data with fewer independent things**, claiming no "why."

This document shows that the inventory above compresses to: **one curve, one fixed integer spectrum, a handful of weights, one directed episode, and two boundary numbers** — with the puzzles becoming identities or theorems of the curve.

## 2. Primitive assumptions

**A0 (Background).** There exists a homogeneous, isotropic background with scale factor a(t) > 0 and expansion rate H = ȧ/a > 0 over the era described. (Anisotropy and inhomogeneity are the research program, §10, not the present scope.)

**A1 (Log coordinates).** All multiplicative structure is booked additively: the horizontal coordinate is the e-fold number **N = ln(a/a₀)**; the vertical coordinate is the **log causal radius X = ln(R_H/R₀), R_H = c/H**. Nothing physical is assumed here; A1 is a choice of chart, made because the invariant content of expansion is a *ratio drift* (see §5, T11-remark) and ratios are additive in logs.

**A2 (The constraint as a partition function).** The Friedmann constraint H² = (8πG/3)ρ_tot, with the total density resolved into scaling sectors, is *rewritten* — not modified — as
> **𝒵(N) ≡ H²(N)/H₀² = Σᵢ Ω_{i0} e^{−nᵢN},  X(N) = −½ ln 𝒵(N).**

**A3 (Kinematic spectrum).** Each sector with constant equation of state w dilutes by the continuity equation as ρᵢ ∝ a^{−3(1+w)}, so its exponent is **nᵢ = 3(1+wᵢ)** [T-A3, verified]. In three spatial dimensions the standard sectors have *fixed integer* exponents:

| sector | w | n | reason |
|---|---|---|---|
| vacuum / singlet | −1 | **0** | boost-invariance forces p = −ρ (identity, §4 T9) |
| curvature | −1/3 | **2** | Gauss law: k/a² |
| matter | 0 | **3** | volume counting |
| radiation | +1/3 | **4** | volume + wavelength stretch |
| stiff/shear | +1 | **6** | kinetic domination |

**The spectrum is kinematics; only the weights Ω_{i0} are data.**

**A4 (Passivity clause — the fine print of every no-go below).** The "passive" theorems (T2, T5, T10) require **all weights Ω_{i0} ≥ 0 and all exponents nᵢ constant**. Closed-universe curvature (Ω_k < 0) exits the probability reading; running-w sectors exit by construction. Violations of A4 are not errors — they are the *definition* of an **active episode** (§6).

**A5 (Optional modules).** (i) *Horizon-entropy reading:* assigning the apparent horizon the area entropy S_H ∝ R_H^{d−1} (the Jacobson/Cai–Kim/Padmanabhan line) makes X = ln S_H/(d−1) + const — the vertical axis doubles as log-entropy. (ii) *Planck normalization:* X_P ≡ ln(R_H/ℓ_P) is the absolute height. Both modules are used for readings, never for derivations.

**Empirical inputs of the theory (complete list):** H₀, Ω_{m0}, T_CMB (fixing radiation), N_eff, Ω_k — i.e., the weights and one rate. Structurally: **the height of the curve today and its weights.** These play the role G and c play elsewhere.

## 3. Definitions

- **The curve:** Γ : N ↦ X(N). The entire homogeneous history is this one graph.
- **Weights:** pᵢ(N) = Ω_{i0}e^{−nᵢN}/𝒵 — a probability distribution on the spectrum (given A4). ⟨·⟩ denotes its mean.
- **Slope and coasting line:** X′ = dX/dN; the line X′ = 1 is *coasting* (a ∝ t).
- **Displacement:** W = X − N = ln(1/aH) + const — the log **comoving screen** (the comoving Hubble scale). *Terminological rule:* "screen," never "wall"; nothing degenerates there — it is a moving horizon of influence, not an existence boundary.
- **Deceleration:** q ≡ −äa/ȧ².
- **Planck height:** X_P = ln(R_H/ℓ_P).

---

# PART II — THE IDENTITY TOWER

Each identity below is exact and machine-verified. Derivations are given in one or two lines; they are elementary once the chart A1 is adopted — which is the point.

## 4. The cumulant tower: cosmography is one distribution

Because ln 𝒵 is a **cumulant generating function** in the natural parameter N:

> **[T1] X′ = ½⟨n⟩** — the slope is the mean dilation weight. *(Differentiate −½ln𝒵.)*
> **[T2] X″ = −½Var(n) ≤ 0** — the bend is minus the variance: the passive curve is **concave**. *(Second derivative of a CGF is the variance.)*
> **[T3] X‴ = +½κ₃(n)** — the jerk is the skewness. The entire cosmographic/statefinder hierarchy is **the cumulant tower of one probability distribution on {0,2,3,4}.**
> **[T4] q = X′ − 1** — deceleration is the slope measured from the coasting line. *(From q = −1 − Ḣ/H² and X′ = −d lnH/dN.)* Hence **w_eff = −1 + ⟨n⟩/3.**

**Information-geometric reading [T-F]:** the pᵢ(N) form a one-parameter **exponential family** with N as natural parameter; the Fisher information is I(N) = Var(n) = −2X″. The curve bends exactly where observation of the expansion is most informative about the mixture — the era crossovers.

## 5. One derivative, four famous phenomena

> **[T5] W′ = q** — acceleration ⟺ the comoving screen **contracts**. *(W = X − N.)* This is the horizon-problem mechanism and the acceleration statement in one line.
> **[T6] d ln|Ω_k|/dN = 2q** — the flatness flow. Since n_curvature = 2 and the acceleration threshold is ⟨n⟩ = 2: **flatness is attracting exactly when expansion accelerates**, repelling when it decelerates. Flatness, acceleration, and screen-contraction are three names for the inequality ⟨n⟩ < 2.
> **[T7] (Raychaudhuri reading)** R_{ab}u^au^b/(3H²) = q — "matter attracts, vacuum repels" is the sign of ⟨n⟩ − 2, not two forces.
> **[T8] 2GM_H/(R_H c²) = Ω_tot exactly, at every epoch** — the Hubble sphere's compactness *is* the total density fraction. The "near-Schwarzschild coincidence" and the "near-flatness puzzle" are **one measurement**: deviation of compactness from ½ equals Ω_k/2. Two mysteries were one identity.
> **[T9] (Vacuum identity)** Boost invariance of a stress tensor forces p = −ρ; the n = 0 sector is not a substance with a tuned property but the **frame-singlet**, whose w = −1 is definitional and whose non-dilution (n = 0) is the unique fixed point of the flow.

## 6. Dynamics of the ensemble: H-theorem, no-go, and the active equation

> **[T10] (H-theorem)** d⟨n⟩/dN = −Var(n) ≤ 0 under A4: the mean weight **never increases**; ⟨n⟩ is a Lyapunov function; the flow is an **annealing** of a finite-level system toward its ground level (n = 0), with e-folds as inverse temperature.
> **[T10′] (One-crossing no-go)** Since X′ = ½⟨n⟩ falls monotonically, a passive basket crosses the coasting line **at most once** — it can produce radiation → matter → late acceleration, but **cannot exit an early accelerating phase**. Therefore an early exit (inflation → hot era) *requires* an active episode: an annealing system cannot reheat itself.
> **[T-Q] (Active equation)** Allowing transfer ρᵢ′ = −nᵢρᵢ + Qᵢ with ΣQᵢ = 0:
> **X″ = ½⟨n′⟩ − ½Var(n) + (1/2𝒵)ΣQᵢnᵢ.**
> Three terms: running exponents; passive dilution; **directed conversion**. A single conversion pulse into high-n sectors raises the slope above coasting (the hot era); when it ends, T2's variance term lowers it again — inevitably — revealing the ground state. **Inflation and dark energy are the same structural phase (X′ < 1) visited on the two sides of the history's one directed episode.**

## 7. Endpoints, and the collapse of the big numbers

> **[T11] (Endpoint integrability)** Proper time is dt = H₀⁻¹e^X dN and conformal time is dη ∝ e^W dN. Hence: the Bang can sit at N = −∞ with **finite proper age** (the age integral converges at the past end), and a **future event horizon exists iff ∫^∞ e^W dN < ∞** — dark energy is the statement that the world's remaining conformal reach is a *finite number*. Beginning and end are convergence properties of the two ends of one curve.
> *(Chart remark: "expanding space," "drifting local standards," and "slowing global transport" are three bookings of the same dimensionless drift; a bare lapse is flat, and c cannot carry the drift because it is the unit of comparison. The invariant is the curve.)*
> **[T12] (Tropical limit)** The textbook era-diagram (straight segments of slope 2, 3/2, 0 with kinks) is the **max-plus limit** of Γ, and the smooth curve deviates from this skeleton by at most **½ ln 2 nats per two-sector crossing** [verified]. Cosmology's cartoon differs from its free energy by half a bit per era.
> **[T13] (Planck collapse)** R_H/ℓ_P = e^{X_P}; M_H/m_P = ½e^{X_P}; S_H/k_B = πe^{2X_P}; N_qubit = (π/ln2)e^{2X_P}; and ln(1/Λℓ_P²) = 2X_P − ln(3Ω_Λ). **Size, mass, entropy, capacity, and the cosmological constant's smallness are powers of one number — the height of the curve.**

---

# PART III — THE EMPIRICAL PIPELINE

## 8. Inputs → outputs (generated by the certificate)

**Inputs (five):** H₀ = 68.17 km s⁻¹Mpc⁻¹, Ω_{m0} = 0.3027 [DESI DR2 + CMB flat-ΛCDM], T_CMB = 2.7255 K, N_eff = 3.044, Ω_k = 0.
**Derived weights:** Ω_γ = 5.32×10⁻⁵ (from T_CMB via ρ_γ = a_rad T⁴/c²), Ω_ν = 3.68×10⁻⁵, Ω_r = 9.00×10⁻⁵, Ω_Λ = 0.6972 (closure).

| Output | Formula | Value | Empirical anchor |
|---|---|---|---|
| q₀ | ½⟨n⟩₀ − 1 | **−0.5458** | SNe: ≈ −0.55 |
| acceleration transition | ⟨n⟩ = 2 | **z = 0.664** | SNe: 0.6–0.7 |
| matter–radiation equality | Ω_m e^{−3N} = Ω_r e^{−4N} | **z = 3362** | CMB: ≈ 3387 |
| Λ–matter equality | Ω_m e^{−3N} = Ω_Λ | **z = 0.321** | onset of Λ domination |
| dimensionless age | ∫𝒵^{−1/2}dN | **H₀t₀ = 0.9613** | — |
| age | H₀t₀/H₀ | **13.788 Gyr** | oldest stars / CMB ≈ 13.8 |
| future conformal reach | ∫₀^∞ e^W dN | **1.142 c/H₀ (finite)** | event horizon exists |
| Hubble radius | c/H₀ | **14.34 Gly** | — |
| Hubble mass | c³/2GH₀ | **9.14×10⁵² kg** | — |
| curve height | ln(R_H/ℓ_P) | **X_P = 140.283** | — |
| horizon entropy | πe^{2X_P} | **2.21×10¹²²** | the famous 10¹²² |
| qubit capacity | S/ln2 | **3.19×10¹²²** | holographic bound |
| owed logarithm | 2X_P − ln(3Ω_Λ) | **279.83** | ln(1/Λℓ_P²) |

Thirteen outputs from five inputs, three of which (T_CMB, N_eff, Ω_k) are shared with all of physics. The era slopes (2, 3/2, 0) and every identity of Part II are parameter-free.

---

# PART IV — WHAT THE THEORY FORBIDS, AND WHAT IT ASKS

## 9. Falsifiers

1. **No convexity:** any passive era with measured X″ > 0 (w_eff *rising* without an identified transfer) violates T2. **Live test:** DESI's 2.8–4.2σ preference for evolving w is, in this language, a claimed concavity violation in the dark sector — i.e., a claim that the terminal sector is *active now*. Flat asymptote (w ≡ −1) ⟺ the terminal sector is the fixed point.
2. **One crossing:** no passive history exhibits two q = 0 crossings. Any reconstructed expansion history with accel → decel → accel *entails* a directed episode between them — this is how the theory *forces* (not merely permits) an inflaton-like event.
3. **Compactness lock:** 2GM_H/R_Hc² must track Ω_tot at every epoch. Deviation from ½ measures Ω_k/2 — a consistency identity between two observables.
4. **Endpoint integrability:** a future horizon exists iff the reach integral converges; reconstructed H(z) determines the verdict with no freedom.

## 10. The research program (what would make this physics rather than the free energy *of* physics)

The five pre-geometric supplies, in order of leverage:
1. **The dilation operator D** whose spectrum is {0,2,3,4}: define it prior to geometry (candidate home: the scaling generator of an emergent-metric program; the spectrum's integers come from d = 3, so a derivation of d = 3+1 upstream fixes the species of curve).
2. **The positive weight** producing 𝒵: what state, on what algebra, has the Ω's as its sector weights?
3. **The active episode Q** as a structural process (a wall-crossing / record-production event), not a parametrized source: the no-go proves *that* it happened; the program owes *what it is*.
4. **X ↔ metric:** derive the emergent causal metric from the curve rather than reading the curve off the metric (the Jacobson/entropic route runs this direction; module A5(i) is its docking port).
5. **Perturbations:** local structure riding on Γ — the theory's evidence-bearing sector (spectral tilt, growth) is entirely outside the present homogeneous scope, and honesty requires saying so in bold: **this document governs the background only.**
Secondary: the Bianchi/anisotropic extension (N becomes matrix-valued; the partition function acquires shear sectors n = 6); the DESI verdict as the first scheduled falsification test.

## 11. Relation to prior art

Misner's logarithmic intrinsic time supplies A1's pedigree. **Wainwright–Ellis Hubble-normalized dynamical systems is the nearest neighbor** and owns the attractor/fixed-point content; the present contribution relative to it is the free-energy identification (cumulant tower T1–T3, Fisher reading, tropical limit T12, H-theorem framing) and the endpoint/compactness identities (T8, T11, T13). The statefinder program is *subsumed*: its tower is the cumulants of one distribution. Horizon thermodynamics (Jacobson; Cai–Kim; Padmanabhan) is the optional module A5 and the intended docking port for §10.4. Wetterich's "universe without expansion" certifies the chart-freedom remark in T11. The two boundary numbers (X_P and the terminal slope) are the theory's empirical constants, in exactly the sense that G and c are constants elsewhere: **no honored theory derives its constants; the structure is the theory.**

## 12. Glossary

**N** — e-folds, ln a. **X** — log causal radius, −½ln𝒵; also log horizon entropy /(d−1). **W** — X − N; log comoving screen. **Γ** — the curve N ↦ X. **𝒵** — the partition function H²/H₀². **nᵢ** — dilation weight, 3(1+wᵢ); kinematic integers {0,2,3,4,6}. **pᵢ** — sector weights; an exponential family in N. **⟨n⟩** — mean weight; 2X′; a Lyapunov function. **q** — deceleration; X′ − 1; W′; ½ d ln|Ω_k|/dN; normalized focusing. **X_P** — ln(R_H/ℓ_P); the height; today 140.283. **Screen** — the comoving Hubble scale (never "wall"). **Active episode** — any violation of A4; required exactly once by T10′ if early acceleration occurred. **Coasting line** — X′ = 1; the threshold shared by acceleration, flatness-attraction, and screen-contraction.

---

**Certificate.** `verify_cspg_master.py` — Part A verifies T1–T4, T6, T8, T10, A3 symbolically; Part B generates every number in §8 from the five inputs. Everything in this document that can be checked by machine has been.

*The universe's background, in this notation: a four-level system, spectrum fixed by kinematics, annealing toward its ground state with e-folds for inverse temperature — interrupted exactly once, as it had to be, because an annealing system cannot reheat itself. Its cartoon misses it by half a bit per era. Its puzzles are its identities. Its constants are its inputs. What remains is the research program: name the operator, name the state, name the episode — and then this stops being the free energy of physics, and becomes physics.*
