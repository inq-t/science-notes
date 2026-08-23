# Causal-Wall Spectral Theory — Completion Memo v2.1

**Supplement to:** *Causal-Wall Spectral Theory: A Non-Stochastic Completion of the Scalar Cosmological Sector*, v2.0 (2026-08-21).
**Filed:** 2026-08-21 · **Sections continue v2.0's numbering (14–23).**
**Receipts:** `verify_causal_wall_spectral_v2_1.py` → `causal_wall_spectral_receipts_v2_1.json` — 12/12 pass (S1–S12).
**Referee report:** `causal-wall-spectral-referee-report-v2.md` (findings F1–F16; this memo's sections are its dispositions).
**Companion record:** the Einstein-member derivations remain filed in `descent-spectrum-completion-v1_1.md` (memo v1.1); §16 below establishes the concordance and §23 merges the open-problem lists.

Notation as in v2.0: ζ = −δ ln σ; K_ζ the descent precision; c⁽⁰⁾, c⁽²⁾ the spin-0/spin-2 spectral densities; I_ζ = π⁴c⁽⁰⁾/4 = 1/Δ²_ζ; δ = 1 − n_s. From the Einstein member: ε = −Ḣ/H², 𝔖 = π/(GH²) = 8π²M_P²/H². Pivot k\* = 0.05 Mpc⁻¹ throughout. All claims carry programme tags.

---

## 14. The weld made exact: precision as the BKM correlator of the stress trace

This section supplies the load-bearing structure §3 uses implicitly (closes F1). Nothing in v2.0 changes; four joints acquire proofs or registrations.

### 14.1 Exponential-family structure of the functor. [DEDUCTION + lemma]

To second order about the reference, the scale-to-state functor acts as an exponential tilt of the wall state by the smeared stress trace: the tangent action of Φ on the wall algebra is
  dΦ[δζ] : ω ↦ ω tilted by ∫√g δζ T,
which is exactly the statement of the first Weyl variation (3.2). For a tilted (exponential) family with cumulant functional ψ(ζ) — classically ψ = log E₀[e^{∫ζT}], quantum-mechanically the BKM analogue — the relative entropy is the Legendre remainder
  S_rel(ω_ζ‖ω_0) = ζψ′(ζ) − ψ(ζ),
and its Hessian at coincidence equals ψ″(0), **even though the first variations of S_rel and ψ differ** (⟨T⟩ = ψ′(0) ≠ 0 is permitted; the wall state need not be exactly critical). Receipt S5 verifies d²/dζ²[ζψ′ − ψ]|₀ = ψ″(0) symbolically. Consequence:

  **K₂(x, y) = δ²S_rel/δζ(x)δζ(y)|₀ = ⟨T(x); T(y)⟩_BKM.**

This is the precise content of (2.7)'s Φ\*G^BKM and it dissolves the covariance/precision worry a reader may bring to §3: ζ is a *coordinate on state space* (a coupling direction), T is its conjugate score, and the Fisher/BKM metric in coordinates is the covariance of scores. Precision-in-ζ = covariance-of-T. No inversion is being confused; the inversion appears only afterwards, when (2.8) converts the ζ-precision into the ζ-covariance the sky measures.

### 14.2 Which correlator, and why it doesn't matter where the data live. [WELD]

BKM, symmetrized, and Euclidean ⟨TT⟩ differ by known KMS kernels for a general state. On the observable super-wall sector the ζ-algebra is abelian to O(e^{−3N_out}) (memo v1.1, §15.2, receipt R11 there), and on a commutative sector Chentsov's theorem collapses the entire monotone family to the unique classical Fisher object (v1.1, L1). Hence on the sector the data constrain, **all candidate correlators coincide**, and (3.3)'s Euclidean ⟨TT⟩ is unambiguous. The order of operations from v1.1 transfers verbatim: *abelianize first; the metric-choice question then never arises.* Any residual BKM-vs-other distinction lives in the sub-wall non-commuting sector, which is not what the CMB measures.

### 14.3 The Im prescription is the contact-term quotient. [DEDUCTION]

Contact terms in ⟨TT⟩ are polynomial — analytic — in q². Analytic functions have no branch cut, so they drop from Im B(−q²−i0) identically: **the spectral projection is the quotient by contacts**, not a convenient discard. Two reinforcements specific to d = 3:
(i) **No local Weyl anomaly exists in odd dimensions.** There is no anomaly channel for the scalar response to hide in; whatever survives the Im projection is genuine flow. This is §5's thesis made structural: in d = 3, "the tilt is RG" is not one option among several — it is the only occupant of the dilation-breaking channel.
(ii) The one parity-odd contact available in 3d ⟨TT⟩ (the gravitational Chern–Simons term) is removed by the same projection: it is imaginary-contact and parity-odd, and the precision operator is the parity-even spectral part.

### 14.4 Registered conventions. [CONVENTION — registered per the P3 lesson]

(a) **Branch and sign:** Im B(−q²−i0) ≥ 0 and Im A(−q²−i0) ≥ 0 define the continuation; equivalently, spectral positivity of the trace–trace (spin-0) and TT (spin-2) Källén–Lehmann densities. McFadden–Skenderis's published form carries an explicit minus with their −iq continuation — Δ²_S(q) = −q³/(16π² Im B(−iq)) — and v2.0's writing absorbs that sign into the branch choice. Same object, registered branch.
(b) **Scalar normalization is literature-verbatim:** Δ²_S = 4/(π⁴c(q)) with c(q) the spectral density of ⟨TT⟩ in the representation ⟨T(x)T(0)⟩ = (π/8)∫₀^∞ dρ c(ρ)∫(d³q/(2π)³) q⁴/(q²+ρ²)e^{iq·x} (McFadden). v2.0's c⁽⁰⁾ *is* that c.
(c) **Tensor normalization is a registered definition:** Δ²_T = 32/(π⁴c⁽²⁾) is consistent with (3.6) iff Im A(−q²−i0) = (π²/16)c⁽²⁾q³ — a relative factor of 4 against the scalar's (π²/64) (receipt S1). c⁽²⁾ is hereby defined by that normalization; the physics-facing relation r = 8c⁽⁰⁾/c⁽²⁾ is then exact.

With 14.1–14.4 in place, §3's chain is closed: (2.7) ⇒ K₂ = BKM⟨T;T⟩ [14.1] = Euclidean spectral ⟨TT⟩ on the observable sector [14.2] = 8 Im B with contacts quotiented [14.3] = (π²/8)c⁽⁰⁾k³ [14.4b]. Every step is either a theorem, a verified identity, or a registered convention. [WELD complete]

---

## 15. The near-gauge resolution: why the sky is lumpy at all, and why so faintly

Closes F2. The fixed-point limit c⁽⁰⁾ → 0 sends K_ζ → 0 and Δ²_ζ → ∞ while §5 declares scale "gauge." Both statements are correct, and their coexistence is the theory's explanatory core rather than its embarrassment.

### 15.1 The 0×∞, resolved. [DEDUCTION]

At the fixed point ζ couples to nothing: every coupling of the scale residue to matter passes through T = βᴵO_I, and β → 0. A direction of state space that costs zero information to deform *is* a gauge direction, and a gauge direction's covariance is divergent by definition — the state assigns no penalty. The divergence multiplies vanishing couplings; observables are the 0×∞, and they go to zero, not infinity. This is the same limit v1.1 handles as ε → 0 (exact de Sitter): there ζ is the dilation zero mode, canonical energy vanishes linearly in ε, and Δ²_ζ ∝ 1/ε diverges — the *known* infrared behavior of the curvature perturbation, now typed. Receipt S6 records the bookkeeping: the coupling-weighted covariance ε·Δ²_ζ = 1/𝔖 stays finite (capacity-bounded) as ε → 0.

### 15.2 Two senses of "near-conformal," disentangled. [VERDICT]

(i) **Exponent:** δ = 0.026–0.035 ≪ 1. The flow is slow; the *shape* is near-critical.
(ii) **Amplitude:** c⁽⁰⁾(k\*) = 1.956×10⁷ is enormous against O(1) central charges. The wall's trace response is weak *per distinction* but the wall holds very many distinctions: in large-N normalization c⁽⁰⁾ ~ N² reads N ≈ 4.4×10³ (receipt S12) — the "perturbative large-N QFT" regime McFadden–Skenderis proposed for the strongly-gravitating phase, and the regime the published holographic fits actually occupy.

These are independent facts and v2.0's §5 lets them blur. The observed situation is: **shape-near-critical, amplitude-large.** The smallness of Δ²_ζ = 1/I_ζ ≈ 2×10⁻⁹ is the *largeness of capacity*; the redness is the *slowness of flow*; and the existence of structure at all is the *nonvanishing* of the flow. One sentence now carries the sector's explanation of the sky:

> **Structure exists because scale is almost, but not exactly, gauge; its faintness is the wall's capacity; its redness is the wall's flow.**

### 15.3 What the amplitude is a reading of. [REMARK, register discipline]

c⁽⁰⁾(k\*) is an epoch/window reading in exactly the sense of flag DS-F1 (v1.1 §18.2): in the geometric member c⁽⁰⁾ = 4ε𝔖/π⁴ with 𝔖 ∝ H⁻², a clock reading. The sector retrodicts the *structure* of the amplitude (why one number, why k³, why slowly running), not its value; deriving the value is CW-T2 (§23). Any future promotion of c⁽⁰⁾(k\*) to a constant of nature repeats the χ_MW category error and is pre-emptively barred.

---

## 16. The geometric member and the concordance with memo v1.1

Closes F5iii and F16's first half. v2.0 correctly demotes the Einstein dictionary to a conditional reconstruction; what it omits is that the member's identities are *free* — two lines that lock the two memos together.

### 16.1 Member identities. [DEDUCTION within the Einstein single-clock reconstruction; receipt S4]

  **c⁽⁰⁾ = 4ε𝔖/π⁴,  c⁽²⁾ = 2𝔖/π⁴.**

Consequences, all exact (S4, symbolic):
- r = 8c⁽⁰⁾/c⁽²⁾ = 16ε — (8.1) reproduces v1.1's tensor-to-scalar reading.
- Δ²_t = 32/(π⁴c⁽²⁾) = 16/𝔖 — v1.1's tensor amplitude law.
- I_ζ = π⁴c⁽⁰⁾/4 = ε𝔖 — the v1.1 coefficient identity, verbatim.
- δ = d ln c⁽⁰⁾/d ln k = 2ε + d ln ε/d ln k — the v1.1 tilt decomposition, now read as: *the response's running = capacity running + defect running.* The BK18-forced dominance of the second term (≥ 87.2% of the tilt; v1.1 §16.2) transfers unchanged.
- n_t = −d ln c⁽²⁾/d ln k = −d ln 𝔖/d ln k = −2ε = −r/8 — the wall consistency relation, now typed as the *member's* tensor-tilt law (see §17.2 for the general class).

### 16.2 Numerical concordance. [receipt S4]

The 𝔖 bound computed two independent ways — route 1: 𝔖 = I_ζ/ε with ε ≤ r/16; route 2: 𝔖 = π⁴c⁽²⁾/2 at the c⁽²⁾ bound — agrees exactly: 𝔖 > 2.118×10¹¹, hence ε < 2.25×10⁻³ and H_mint < 4.70×10¹³ GeV, identical to v2.0 (8.4)–(8.6) *and* to v1.1 §16.2, which was derived without the holographic frame. Two documents, two methods, one number set. [CONVERGENT VERIFICATION — filed]

### 16.3 Status ledger for the member. [VERDICT]

The general wall-spectral typing (v2.0) and the Einstein member (v1.1) are now one structure viewed in two coordinate systems: (ε(N), 𝔖(N)) bulk-side, (c⁽⁰⁾(k), c⁽²⁾(k)) wall-side, with the change of coordinates given by 16.1. v1.1's ladder rungs L1–L3 supply exactly the proof obligations §14 consumed (Chentsov collapse; Gaussian precision; benchmark evaluation), and v1.1's DS-T1/DS-T2 are the member-side names of the microscopic task v2.0 files as (13.4). The merged list is issued in §23. v1.1 remains the derivation record for everything member-specific; v2.0 is the general statement.

---

## 17. Tensor slot, quantified

Closes F5i–ii and the tensor half of F3.

### 17.1 Two ratios, registered. [receipt S3]

The BK18 bound r < 0.036 gives, at k\*:
- **Spectral-density ratio:** c⁽²⁾/c⁽⁰⁾ > 222.2 (2.35 orders of magnitude); c⁽²⁾(k\*) > 4.35×10⁹.
- **Per-mode precision ratio:** K_γ/K_ζ = 2/r > 55.6 per polarization (1.74 orders).

§8's sentence ("at least two orders of magnitude more precise") is correct for the density ratio and is hereby registered as quoting it; the per-mode precision statement is the weaker 1.74 orders. Both are readings of one bound.

### 17.2 Tensor tilt across the family. [DEDUCTION + SLOT]

- **General near-critical wall class:** c⁽²⁾ tracks the TT central charge c_T, which is a fixed-point datum; its running enters at second order in the deformation, so |n_t| = |d ln c⁽²⁾/d ln k| = O(δ²) ≈ 10⁻³.
- **Geometric member:** n_t = −r/8 exactly (§16.1), with |n_t| < 4.5×10⁻³ under BK18.

Both are ≲ few×10⁻³: the tensor tilt is a class discriminant in principle and out of reach in practice for the near term. **The operative near-term tensor content is the r value itself:** any detection fixes c⁽²⁾(k\*) = 8c⁽⁰⁾/r in one reading, and — within the member — fixes ε = r/16, 𝔖 = 16I_ζ/r, and H_mint simultaneously, after which n_t = −r/8 becomes the member's post-detection consistency check (falsification table, row 8). Until CW-T3 computes it, c⁽²⁾(k) is a **[SLOT]**: dictionary fixed, value open — and the slot's honesty cost is stated plainly: with c⁽²⁾ free, no r value can kill the general typing; only the member is exposed to r.

---

## 18. Higher cumulants: the mechanism, the hierarchy, the kill

Closes F6; supersedes the one-line claim in §9 with structure.

### 18.1 Mechanism. [POSTULATE CW-P2 — extensivity, the wall-native form of v1.1's DS-P2]

The wall's connected cumulant kernels are extensive in the spectral density: K_n = c·O(1) for all n, with O(1) built from the same axioms and coefficients not scaling with c. This is large-capacity factorization — in the dual reading, ordinary large-N factorization of stress-tensor correlators. **Consequence [DEDUCTION]:** normalized connected cumulants scale as κ_n ~ c^{1−n/2}; the wall is quasi-free *because* it is large, not by fiat.

### 18.2 The hierarchy, with numbers. [receipt S10]

| Contribution | Scale | Value at k\* |
|---|---|---|
| Dilation Ward term (squeezed) | 5δ/12 | 0.0146 (Planck) / 0.0108 (P-ACT-LB) |
| Flow-induced (shape-dependent) | O(ε, δ) | ≲ 10⁻²–10⁻³ |
| Capacity floor (any shape) | 1/√c⁽⁰⁾ | 2.3×10⁻⁴ |
| Geometric-member intrinsic quantum piece | 1/√𝔖 | ≤ 2.2×10⁻⁶ |

Planck 2018 IX: f_NL^local = −0.9±5.1, f_NL^equil = −26±47, f_NL^ortho = −38±24 — every shape within 1.6σ of zero, with the predicted values 2–4 orders below current sensitivity. Passing with room.

### 18.3 Kill condition. [PREDICTION / kill; ties falsification 7]

The sector owns **no c_s dial**: the axioms admit no intrinsic wall speed besides the causal one, so the large-equilateral/orthogonal escape hatch of single-field EFT is welded shut. Any established |f_NL| ≳ 1 on any shape kills the near-critical large-capacity wall class outright — mechanism, not parameter. The named computation that would sharpen ≳ 1 into a shape-by-shape band is CW-T4 (⟨TTT⟩; the holographic 3-point machinery exists: McFadden–Skenderis 1104.3894, Bzowski–McFadden–Skenderis 1211.4550).

---

## 19. The running class: quantitative predictions, the live stress test, and the named alternative

Closes F3's scalar half, F4, and F8.

### 19.1 The minimal class, made falsifiable. [PREDICTION]

Constant exponent δ ⇒ α_s = 0 at that order (receipt S11, symbolic). The predictive content is the *bound at the next order*: for a slowly varying exponent, |α_s| ~ |δ·dδ/d ln k| ≲ δ², i.e.

  **|α_s| ≲ 1.2×10⁻³ (Planck calibration) / 0.7×10⁻³ (P-ACT-LB calibration).**

Current data: Planck 2018 gives α_s = −0.0045 ± 0.0067 — consistent with zero and with the class bound. **Kill [pre-registered]:** an established |α_s| ≳ 3×10⁻³ kills the constant-exponent class. It does **not** kill the typing: the framework survives as a running-exponent flow (δ = δ(k)), losing one unit of economy. The class-kill/typing-kill distinction is filed now, before data move.

### 19.2 The Planck–ACT tilt difference: [WATCH]. [receipt S9]

Registered combinations: Planck 2018, δ = 0.0351 ± 0.0042; **P-ACT-LB** (Planck + ACT DR6 + lensing + DESI BAO), n_s = 0.9743 ± 0.0034 ⇒ δ = 0.0257 ± 0.0034. (P-ACT alone: n_s = 0.9709 ± 0.0038.) Difference: Δδ = 0.0094 = **1.74σ** — not a wound, but the minimal class makes it sharp: constant δ means the same exponent at all scales, so a *physical* scale dependence of this size implies α_s ≈ Δδ/Δln k ≈ **+3–6×10⁻³** across the plausible lever arms (Δln k ≈ 1.5–3) — above the class bound of §19.1. Directional corroboration: the ACT DR6 extended-models analysis itself reports that P-ACT-LB mildly prefers *positive* running, and excludes the Lyman-α-preferred α = −0.010 at over 3σ. The data lean, weakly, exactly on the minimal class's thinnest axis.

**Filed verdict:** [WATCH], with pre-registered outcomes — (a) the difference resolves as systematics/data-combination effects → the minimal class stands and the episode is filed as a passed stress; (b) the difference hardens into a confirmed positive α_s ≳ 3×10⁻³ → the minimal class dies by §19.1's kill, the typing survives as a running-exponent flow, and the wall QFT target (CW-T2) inherits a *measured* second invariant to reproduce. Either outcome is informative; neither is an epicycle opportunity.

### 19.3 The named in-family alternative. [BRANCH]

The published holographic fits (Easther–Flauger–McFadden–Skenderis; Afshordi–Gould–Skenderis; Afshordi–Corianò–Delle Rose–Gould–Skenderis) use the *perturbative-QFT* spectral density — logarithmic running of the form c(q) governed by a dimensionful coupling, not a constant power law. Their empirical success therefore supports the **typing** (spectra from a wall ⟨TT⟩ spectral density) and not v2.0's **minimal class**; §6's borrowed support is retyped accordingly. The AGS form is filed as the named in-family alternative; the discriminant between members is low-k/low-ℓ behavior (the AGS class deviates from a power law most strongly at the largest scales, where it was found competitive with — by some measures preferable to — ΛCDM over part of the range). Adjudication is a data question and is left open with both members on the table.

---

## 20. Conservation and the transfer joint

Closes F7. The dictionary outputs the wall/superhorizon covariance; the transfer integral (9.4) consumes it at re-entry. The bridge: rank-one descent (9.1) is equivalent to vanishing non-adiabatic pressure, δp_nad = 0, and the standard conservation theorem then gives dζ/dN = O((k/aH)²) on superhorizon scales (Wands–Malik–Lyth–Liddle astro-ph/0003278; Weinberg astro-ph/0302326). The wall reading is transported unchanged to re-entry; the deterministic transfer of §9 then does the rest. Economy note transferred from v1.1: rank one ⇒ adiabaticity ∧ conservation ∧ single-clock coherence — one hypothesis, three consequences; three passing tests of one structural claim, not three successes.

---

## 21. Hygiene registrations

Closes F9–F13. Each item is one sentence and is henceforth citable.

1. **Branch positivity:** Im B(−q²−i0) ≥ 0, Im A(−q²−i0) ≥ 0 (§14.4a). [CONVENTION]
2. **Data combinations:** "Planck" = Planck 2018 (n_s = 0.9649 ± 0.0042); "ACT" = **P-ACT-LB** (n_s = 0.9743 ± 0.0034); P-ACT alone = 0.9709 ± 0.0038. [CONVENTION]
3. **c⁽²⁾ normalization:** Im A = (π²/16)c⁽²⁾q³, defining Δ²_T = 32/(π⁴c⁽²⁾) (§14.4c). [CONVENTION]
4. **k is comoving = wall resolution coordinate:** the MS identification of boundary momentum with comoving momentum; only ratios k/k\* enter dimensionless quantities; pivot k\* = 0.05 Mpc⁻¹ for every boxed number. [CONVENTION]
5. **Glossary (register freeze):** *capacity* = 𝔖 (equivalently the c⁽²⁾/c_T scale); *response* = c⁽⁰⁾ (defect-weighted capacity); *discernibility* = I_ζ; *precision* = K_ζ. v2.0's use of "capacity" for c⁽⁰⁾ (§7, Fig. 3) is deprecated in favor of "response"; Fig. 3's caption should read "scalar wall response and the spin-two capacity bound." [CONVENTION]
6. **"No intrinsic length" is a criticality-class statement:** the axioms fix the critical kernel; the single dilation-breaking channel is logarithmic and occupied — by the tilt. Running is the controlled breaking, not a violated axiom. [REMARK]
7. **Block-diagonality in §11:** G_Nζ = 0 holds by construction — the homogeneous mode is quotiented out of T_σ̄Sc(Σ) = C∞(Σ)/ℝ, so the N-direction is orthogonal to every ζ-direction. Not an assumption. [DEDUCTION]
8. **§1's age paragraph:** tagged [REMARK — register discipline]. It asserts only that FLRW proper time is a chart parameter of the reconstruction, agnostic in both directions about pre-observable "duration." It may not be quoted as a physics claim about the universe's age.
9. **Typography:** the abstract's dictionary line is to be read (and in any revision, typeset) as Δ²_ζ(k) = k³/(16π² Im B(−k²−i0)); and (3.3)'s "datum needed for the scalar covariance" is corrected to "datum for the scalar *precision* (covariance by inversion)."

---

## 22. Updated falsification table (supersedes v2.0 §12; numbers attached)

| # | Statement | Type | Status |
|---|---|---|---|
| 1 | No independent isocurvature source (rank one); Planck β_iso limits at the few-percent level | RETRODICTION | passing |
| 2 | No incoherent active seeding; superhorizon TE anticorrelation (ℓ ≈ 30–200) from single-clock coherence | RETRODICTION | passing |
| 3 | No arbitrary spectral features; controlled spectral density only | PREDICTION | passing (none seen) |
| 4 | NG hierarchy of §18.2; **kill: any established \|f_NL\| ≳ 1 on any shape** | PREDICTION / kill | open; passing at 2–4 orders of headroom |
| 5 | Minimal class: \|α_s\| ≲ δ² ≈ 10⁻³; **kill: established \|α_s\| ≳ 3×10⁻³** (class kill, not typing kill) | PREDICTION / kill | open; Planck α_s = −0.0045±0.0067 passing |
| 6 | Planck–ACT tilt difference (1.74σ): resolves as combination effects, or hardens into positive running that triggers row 5 | WATCH | live |
| 7 | Tensor slot: any detected r fixes c⁽²⁾ = 8c⁽⁰⁾/r; geometric member then predicts **n_t = −r/8** as post-detection consistency; general class predicts \|n_t\| = O(δ²) | SLOT + member PREDICTION | open (needs r detection) |
| 8 | Wall Hessian produces the P3 critical form (fails ⇒ CW-T1/CW-T2 dead) | kill on the typing | open — the microscopic task |
| 9 | No phenomenological c_s or slip function; **any required insertion kills the class** (ties row 4) | PREDICTION / kill | passing |
| 10 | Member soft budget r ≤ 8(1−n_s) ≈ 0.28 (declining-ε branch) | CONSISTENCY | passing (weak) |

---

## 23. One open-problem list (supersedes v1.1 §20 and v2.0 §13.4 jointly)

The member-side targets of memo v1.1 and the wall-side targets of v2.0 (13.4) are the same obligations in two coordinate systems. Merged and renamed; the v1.x names are retired as aliases.

**CW-T1 — Identify the wall algebra and state.** [⊇ DS-T1] Construct the causal-wall QFT/algebraic state whose modular data realize the scale-to-state functor; member-side success criterion: the state's quasi-free sector at minting is the unique regular KMS(2π) (Hadamard) sector (Bisognano–Wichmann shape). **Kill shape:** exhibit a second regular KMS(2π) wall state with a different quasi-free sector — uniqueness dies and selection needs a law, not a fact.

**CW-T2 — Compute c⁽⁰⁾(k).** [⊇ DS-T2 + DS-O1] Derive the spin-0 spectral density from the identified wall structure. Member-side this is the norm supply (z² = 2εa²M_P² from the wall first law, ε as dilation-zero-mode projection weight) *plus* the constitutive law ε(N): one function in either coordinate system, per §16.1. **Success criteria:** c⁽⁰⁾(k\*) = 1.956×10⁷ and δ within the measured band, from structure, with zero fitted functions. **Kill shape:** the computed density fails the P3 critical form (row 8) or misses the calibration by more than the running can absorb.

**CW-T3 — Compute c⁽²⁾(k).** Spin-2 spectral density of the same wall structure; closes the r slot. **Success criterion:** a predicted r (or a structural bound tighter than BK18). **Kill shape:** predicted r excluded by data, or c⁽²⁾/c⁽⁰⁾ < 222.2.

**CW-T4 — Compute ⟨TTT⟩.** Higher stress correlators of the wall structure; sharpens §18.3's ≳ 1 into shape-by-shape bands. **Kill shape:** predicted bands excluded, or any shape forced above 1.

Supersession note: `descent-spectrum-completion-v1_1.md` remains the derivation record for the geometric member (ladder L1–L5, tensor laws, tilt decomposition, near-miss registration); its open list is retired into the above. Future sessions cite CW-T1–T4 only.

**Closing statement.** With this completion, the scalar-sector reformulation stands as: a theorem-grade weld from relative-entropy precision to the stress-trace spectral density (§14, resting on v1.1's L1–L2 plus one lemma); an explanatory core stated in one sentence (§15.2); exact concordance with the Einstein member and with memo v1.1's independent numbers (§16); a quantified tensor slot (§17); a mechanism-backed Gaussianity hierarchy with a pre-registered kill (§18); a falsifiable running class with a live, pre-registered watch item (§19); and a single four-entry open-problem list with kill shapes (§23). The outstanding problem is, as v2.0 says, a spectral calculation and not an ether-wind search — with the one addition the programme's standard requires: the calculation's success criteria and failure modes are now filed *before* anyone attempts it.

---

## References added in v2.1

[D1] P. McFadden, K. Skenderis, "Holography for cosmology," Phys. Rev. D 81 (2010) 021301, arXiv:0907.5542. (Dictionary; large-N regime.)
[D2] P. McFadden, "On the power spectrum of inflationary cosmologies dual to a deformed CFT," JHEP 10 (2013) 071, arXiv:1308.0331. (Spectral-density normalization Δ²_S = 4/(π⁴c); power spectrum inverse to the trace spectral density.)
[D3] R. Easther, R. Flauger, P. McFadden, K. Skenderis, "Constraining holographic inflation with WMAP," JCAP 09 (2011) 030, arXiv:1104.2040. (First fits; perturbative-QFT class.)
[D4] N. Afshordi, C. Corianò, L. Delle Rose, E. Gould, K. Skenderis, "From Planck data to Planck era," Phys. Rev. Lett. 118 (2017) 041301, arXiv:1607.04878; N. Afshordi, E. Gould, K. Skenderis, arXiv:1703.05385. (Named in-family alternative, §19.3.)
[D5] E. Calabrese et al. (ACT), "The Atacama Cosmology Telescope: DR6 constraints on extended cosmological models," JCAP 11 (2025) 063, arXiv:2503.14454. (P-ACT-LB n_s; mild positive-running preference; −0.010 excluded at >3σ.)
[D6] T. Louis et al. (ACT), arXiv:2503.14452. (DR6 power spectra and ΛCDM parameters — already v2.0's [10]; registered here for the combination naming.)
[D7] N. Lashkari, M. Van Raamsdonk, arXiv:1508.00897; S. Hollands, R. M. Wald, arXiv:1201.0463. (Canonical energy = quantum Fisher; member-side norm-supply route, carried from v1.1.)
[D8] D. Wands, K. A. Malik, D. H. Lyth, A. R. Liddle, arXiv:astro-ph/0003278; S. Weinberg, arXiv:astro-ph/0302326. (Conservation joint, §20.)
[D9] N. N. Chentsov (1972/1982); D. Petz, Lin. Alg. Appl. 244 (1996) 81. (Abelian collapse, §14.2, carried from v1.1.)
(v2.0's references [1]–[12] carry over unchanged.)
