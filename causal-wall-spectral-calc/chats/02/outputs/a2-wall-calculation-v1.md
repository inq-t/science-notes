# The A₂ Wall — Executing CW-T1…T4 under the Keller Import

**Memo v1.0 · Filed 2026-08-21**
**Continues:** *Causal-Wall Spectral Theory* v2.0 + completion v2.1 (open list CW-T1–T4, §23).
**Imports:** *The A₂ Spectral Geometry of the 2026 Jacobian Counterexample* (JC strand, filed July 2026): the counterexample's inverse problem is governed by a family of binary cubics; near the triple-root curve the family is the miniversal deformation **u³ + au + b** of the A₂ singularity (times one smooth parameter); the Keller obstruction (nonproperness) germ is the cuspidal discriminant **4a³ + 27b² = 0**; the generic inverse cover has full monodromy **S₃ = W(A₂)**.
**Receipts:** `verify_a2_wall_v1.py` → `a2_wall_receipts_v1.json` — **18/18 pass** (A1–A7, R1–R4, K1–K7).

**Status box (read first).** "Perform the remaining calculation" cannot lawfully terminate in the amplitude: c⁽⁰⁾(k\*) is an epoch reading (flag DS-F1; v2.1 §15.3), and receipt K6 verifies that the bar fires when tested — every numerological route from A₂ data to 1.956×10⁷ dies by ≥10⁶×. What the calculation *can* terminate in, and below *does*, is: (i) the collapse of the sector's last free function to **one structural rational plus epoch readings**, conditional on the import; (ii) a **kill battery** that executes every registered kill condition against current data and against the import itself, killing five of seven candidate flow laws and three numerological readings of the clue; (iii) **two surviving members with pre-registered, separable point predictions for α_s**, both positive, both inside the band implied by the Planck–ACT tilt drift; (iv) the honest microscopic residue, named. Everything below the import line is **conditional on CW-P3**; the import's own verification lives in the JC strand.

---

## 1. The import, typed

**[IMPORT CW-P3]** (from the A₂ preprint, JC strand): *The spectral geometry of the Keller obstruction is A₂* — concretely, the obstruction germ is the discriminant of the miniversal deformation u³ + au + b, and the covering monodromy is W(A₂) = S₃.

Cross-strand kill shape (lives in the JC strand): exhibit a normal form of the obstruction germ inequivalent to A₂, or a covering monodromy ≠ S₃. This memo's every conditional claim dies with it.

Reading adopted here: the causal wall's near-conformal degeneration *is* the Keller obstruction; the wall's deformation space is the A₂ base (a, b); the conformal fixed point ("scale is gauge," v2.1 §15) *is* the discriminant locus — on it, the cubic degenerates, the cover ramifies, and the scale residue decouples. Off it, by the distance the flow has traveled, structure is discernible. This gives v2.1 §15.2's sentence a geometric address: **near-conformal = near-discriminant.**

## 2. The A₂ dossier (receipts A1–A7)

All machine-verified; each line ends with what it welds to.

1. **Milnor monodromy** M = T_aT_b = [[0,1],[−1,1]] ∈ SL(2,ℤ): M³ = −𝟙, order exactly 6; PSL-image order 3 (A1). → The **ℤ₃ sheet monodromy of the descent strand is the PSL-shadow of the ℤ₆ Milnor monodromy** (ℤ₆ = ℤ₂ × ℤ₃; the ℤ₂ factor's physical role is [OPEN]).
2. **Eigenvalues** e^{±iπ/3}: char poly t² − t + 1, discriminant −3 < 0 — *no real eigenvalues*; minimal splitting field ℚ(ζ₆) (A2). → [RHYME — necessity-of-i echo]: the obstruction's own monodromy is irreducibly complex; the Eisenstein field ℚ(ζ₃) ⊂ ℚ(ζ₆) is where the strand's cube-root grading lives.
3. **Braid → modular:** the twist matrices satisfy σ₁σ₂σ₁ = σ₂σ₁σ₂; (σ₁σ₂)³ = −𝟙, (σ₁σ₂)⁶ = 𝟙, so SL(2,ℤ) = B₃/⟨(σ₁σ₂)⁶⟩ acts on H₁ of the once-punctured-torus Milnor fiber — MCG(T²∖pt) = SL(2,ℤ) (A3). → The wall acquires a **canonical modular group**, the natural home for the programme's Cardy/γ = 1 machinery. [SLOT CW-S2: make that identification explicit.]
4. **Sheet quotient:** B₃ ↠ S₃ = W(A₂), with (σ₁σ₂) ↦ a 3-cycle (A4). → The strand's S₃ is not adjacent structure; it is the Weyl group of the import.
5. **Spectrum and Coxeter data:** spectral numbers {5/6, 7/6} (symmetric about 1, exponentiating to the monodromy eigenvalues); exponents {1, 2}; **Coxeter number h = 3** (A5). → h = 3 = the sheet count = the order of P₃. [SLOT CW-S3: is d = h(A₂) a theorem or a coincidence? Two independent derivations of the same 3 currently exist (dimension; Coxeter). **Do not lean on it.**]
6. **Miniversal deformation** u³ + au + b: the quadratic term is *removable by translation, exactly* (A6). → **The same quotient in three costumes:** removable u² = the constant-mode quotient C∞(Σ)/ℝ = P₃'s ℓ = 0 kernel. The wall's "a constant ζ is not inhomogeneity" is, under the import, the normal-form statement that A₂ has no quadratic deformation direction. Also verified: disc = −(4a³+27b²); quasi-homogeneity of weight 12 under (a,b) → (λ⁴a, λ⁶b); and the modulus j = 6912a³/(4a³+27b²) is **weight-zero** — the deformation space's invariant coordinate is weight-0, as ζ is on the wall. [RHYME, one line, no weight put on it.]
7. **Milnor number μ = 2** (basis {1, u}) (A7). → **[WELD — typing]:** μ(A₂) = 2 = the number of state invariants of the minimal universality class (c⁽⁰⁾(k\*), δ\*). The class's parameter count *is* the Milnor number: v2.0 §10's economy claim acquires a structural reason. Counting match; nothing tuned.

## 3. CW-T1, executed conditionally: the wall algebra and its flow

**[DEDUCTION under CW-P3]** The wall algebra is the ℤ₆-graded algebra of the A₂ Milnor fibration: observables graded by monodromy weight; sheet sector = the ℤ₃ PSL-shadow (the descent strand's S₃-cover data); modular group SL(2,ℤ) acting on the fiber. The **candidate modular flow is the geometric monodromy itself** — the fibration's holonomy, order 6 on homology.

**The state is a trajectory, not a point.** The A₂ base (a, b) is 2-real-parameter (μ = 2); the wall's RG motion is a path on it; the fixed point is the discriminant. So CW-T1's "select the state" reorganizes into "select the flow": the functor picks the trajectory approaching the discriminant, and the KMS(2π) condition becomes the requirement that the state be **monodromy-invariant along it**. What remains open is exactly one joint:

**[SLOT CW-S1 — the clock weld].** *Prove that the monodromy-invariant state on the A₂ fibration is KMS(2π) for the wall inclusion, and identify which base coordinate is ln k.* This is DS-T1's successor and the single load-bearing unproven step below. Everything in §4 is conditional on a clock choice; the discipline applied is: **enumerate every candidate clock, register each with its prediction, and let the kill battery execute.**

## 4. CW-T2, executed: the Reduction, the kill battery, and the two survivors

### 4.1 The reduction. [DEDUCTION under CW-P3 + clock choice]

The sector's one free function (c⁽⁰⁾(k), equivalently ε(N)) is the flow of the A₂ deformation coupling. A deformation coupling has exactly two universality behaviors:

- **Relevant (power) clock C:** coupling of definite A₂ weight ⇒ δ(k) = δ\*(k/k\*)^{−m}, with m an A₂ exponent. Then **α_s = +m·δ(k)** (receipt R2, symbolic).
- **Marginal (log) clock B:** near-marginal deformation, one-loop universal ⇒ δ(k) = 1/(b·ln(k/Λ)), b the one-loop coefficient (a rational in any standard normalization). Then **α_s = +b·δ²** (receipt R1, symbolic).

Closed forms (both verified symbolically to reproduce their tilt and running):

  **Member B:** Δ²_ζ(k) = A_s·[ln(k\*/Λ)/ln(k/Λ)]^{1/b}, with Λ fixed by δ\* once b is fixed (one reading).
  **Member C:** Δ²_ζ(k) = A_s·exp{(δ\*/m)[(k/k\*)^{−m} − 1]} (one reading).

Either way: **zero free functions; one structural rational; one position reading (δ\*); one amplitude reading (A_s).** The compression audit is in §8.

### 4.2 The kill battery on the clocks. [receipts K1, K2]

Every A₂-salient rational is enumerated and executed against Planck's α_s = −0.0045 ± 0.0067:

| Clock | rate | α_s (Planck-cal) | z vs Planck | verdict |
|---|---|---|---|---|
| C | m = 7/6 | 4.10×10⁻² | 6.78σ | DEAD |
| C | m = 1 | 3.51×10⁻² | 5.91σ | DEAD |
| C | m = 5/6 | 2.93×10⁻² | 5.04σ | DEAD |
| C | m = 2/3 | 2.34×10⁻² | 4.16σ | DEAD |
| C | m = 1/2 | 1.76×10⁻² | 3.29σ | DEAD |
| C | m = 1/3 | 1.17×10⁻² | 2.42σ | STRAINED (dying) |
| **C** | **m = 1/6** | **5.85×10⁻³** | **1.54σ** | **ALIVE** |
| B | b = 1 | 1.23×10⁻³ | 0.86σ | alive, below drift band |
| B | b = 2 | 2.46×10⁻³ | 1.04σ | alive, below drift band |
| **B** | **b = 3** | **3.70×10⁻³** | **1.22σ** | **ALIVE, in drift band** |
| B | b = 6 | 7.39×10⁻³ | 1.77σ | alive, above drift band |

Two facts the battery establishes: (i) **every O(1) A₂ exponent is dead or dying as a relevant rate** — the data have already executed most of the clue's naive readings; (ii) against the band implied by the Planck→ACT tilt drift if physical (α ∈ [3.1, 6.3]×10⁻³, receipt from v2.1 S9), exactly **two members survive inside it**, and each is pinned to a canonical A₂ number:

  **Member B: b = h(A₂) = 3** (the Coxeter number). **Member C: m = 1/6** (the spectral gap |s − 1|).

### 4.3 Pre-registered point predictions. [PREDICTION; receipt K3]

  **Member B (marginal, b = 3): α_s = 3δ² = +3.70×10⁻³** (Planck-calibrated), +1.98×10⁻³ at ACT-era δ.
  **Member C (relevant, m = 1/6): α_s = δ/6 = +5.85×10⁻³** (Planck-calibrated), +4.28×10⁻³ at ACT-era δ.

Both **positive** — the sign the ACT DR6 extended analysis mildly prefers, and opposite to plateau-inflation's small negative α ≈ −2/N² ≈ −5×10⁻⁴. Discriminants, in order of arrival: (1) sign and rough size of α_s at σ(α) ~ 2–3×10⁻³ separates {A₂ survivors} from {minimal constant-δ class, α = 0} and from {plateau inflation, α < 0}; (2) at σ(α) ~ 1×10⁻³ (SO/CMB-S4 era) the two survivors separate from each other by 2.3σ (their α's scale as δ² vs δ); (3) running-of-running is *not* a discriminant (both predict β_s ≈ −0.8 to −1.0×10⁻³, receipt K3). Kill shapes: α_s measured ≤ 0 at 3σ kills both members; |α_s| < 1×10⁻³ established kills both and revives the minimal class; α_s in one member's band and out of the other's kills the loser.

### 4.4 Anchors and low-ℓ behavior. [receipts K4, K5]

Member B's IR anchor: Λ = k\*e^{−1/(3δ\*)} = 3.76×10⁻⁶ Mpc⁻¹ — **4.1 e-folds beyond today's horizon** (k_H = 2.25×10⁻⁴): the log flow's reference scale is super-horizon, entering observation only through δ(k). Member C's δ → 1 only at k ≈ 9×10⁻¹¹ Mpc⁻¹ (15 e-folds out; inert). Both members predict a **steepening red tilt at low k** — +4.0% (B) and +5.8% (C) excess over constant tilt at ℓ ≈ 14, against ~26% cosmic variance there. No kill available; but the *direction* is enhancement where Planck's low-ℓ lean is a mild deficit. Filed **[WATCH-2]**, shared by both members (and by the AGS class, which also deviates at low ℓ).

### 4.5 What is *not* derived. [OPEN CW-O1 — the true microscopic residue]

The rational itself. b = 3 is chosen by structural salience (the Coxeter number; the same 3 as the sheet count and P₃'s order), m = 1/6 by the spectral gap — salience is not derivation. The remaining microscopic calculation, now maximally sharpened, is: **compute the one-loop coefficient of the A₂ deformation on the wall theory** (member B), or the deformation's anomalous dimension (member C). Success = 3 (resp. 1/6). The free function of DS-O1/CW-T2 has been reduced to **one rational number with two named candidate values, each carrying a falsifiable α_s.** The amplitude stays a reading, as the type rule demands (K6/N2 verifies the bar).

## 5. CW-T3, executed: verdict NEGATIVE on the structural route

**[NEGATIVE N3; receipt K6]** Can A₂ data fix c⁽²⁾/c⁽⁰⁾? Every bounded A₂ invariant (μ = 2, h = 3, |W| = 6, monodromy order 6, quasi-weight 12) falls short of the required > 222.2 by ≥ 19×. The ratio is **kinematic, not structural**: c⁽²⁾/c⁽⁰⁾ = 1/(2ε) in the member, an epoch reading. The slot stands exactly as v2.1 §17 left it; the member's post-detection check n_t = −r/8 is unchanged; the A₂ class adds only the transport ε ∝ [ln(k/Λ)]^{1/3} (member B; receipt R3) — near-flat r(k), no new kill trips.

## 6. CW-T4, executed conditionally: the single-vertex hierarchy

**[DEDUCTION under CW-P3; receipt R4]** The A₂ normal form is a single cubic — and its miniversal deformation contains **no independent higher vertex** (deformations stop at degree 1; degree 2 is the removable gauge direction). So the wall's connected hierarchy has exactly one independent vertex; everything above the bispectrum is composite:

- Squeezed: pinned by the dilation Ward identity, f_NL^sq = 5δ/12 = 0.0146 (Planck-cal) / 0.0108 (ACT-cal) — unchanged.
- All shapes: single-vertex band **|f_NL| = O(δ) ≈ 10⁻²**, sitting between the flow scale and the capacity floor (2.3×10⁻⁴), far above the geometric-member intrinsic 2.2×10⁻⁶.
- Trispectrum: **Suyama–Yamaguchi saturated**, τ_NL = (6f_NL/5)² = 3.1×10⁻⁴ (Planck bound < 2800: headroom ~10⁷); g_NL = O(f_NL²) ≈ 2×10⁻⁴ (Planck σ ≈ 6.5×10⁴: headroom ~10⁸).
- Kills verified live (K7 row 4): every shape within 1.6σ of zero; |f_NL| ≳ 1 remains the class kill; the A₂ class additionally dies if the trispectrum ever arrives *unsaturated* (τ_NL ≫ (6f_NL/5)²: a second vertex/second source).

## 7. The kill battery, full re-run [receipt K7 + K1, K2, K6]

| Row | Condition | Verdict now |
|---|---|---|
| 1 | Isocurvature (rank one) | PASS |
| 2 | Coherence / TE | PASS |
| 3 | Features | PASS |
| 4 | NG (all shapes; A₂ band O(δ); SY saturation) | PASS, headroom 10²–10⁸ |
| 5 | α_s class kill (≳3×10⁻³ kills constant-exponent) | OPEN; A₂ survivors now *predict* +3.7 or +5.9×10⁻³ |
| 6 | Planck–ACT drift | LIVE at 1.74σ — **the WATCH is now prediction-bearing** |
| 7 | Tensor slot | OPEN; structural route CLOSED (N3); member check n_t = −r/8 stands |
| 8 | P₃ form | PASS structurally (quotient reproduced); full Hessian = CW-S1 + CW-O1 |
| 9 | No c_s/slip | PASS (single vertex; no dial exists in the A₂ class either) |
| 10 | Soft budget r ≤ 8(1−n_s) | PASS (weak) |
| N1 | δ as a bare A₂ exponent | **DEAD — 31σ** (nearest candidate 1/6 vs measured 0.0351) |
| N2 | Amplitude from A₂ combinatorics | **DEAD — short by ≥10⁶×**, and barred by DS-F1 regardless |
| N3 | Tensor ratio from the A₂ lattice | **DEAD — short by ≥19×**; ratio is kinematic |
| N4 | Relevant clocks, m ≥ 1/3 | **DEAD/dying — 2.4–6.8σ** |

Morgue additions: **M-A2-1** (δ-as-exponent), **M-A2-2** (amplitude-from-combinatorics), **M-A2-3** (lattice tensor ratio). Each was a live reading of the clue; each was executed by arithmetic before it could become an epicycle. The morgue is a credential.

## 8. Ledger

**Compression audit.** Before: one free function c⁽⁰⁾(k) [= ε(N)]. After, conditional on CW-P3 + clock: **one structural rational (b = 3 or m = 1/6) + two epoch readings (A_s, δ\*)** — and the rational is doubly constrained (A₂-salient *and* inside the measured drift band). Inputs: the JC-strand import + 2 readings + 1 rational. Outputs: the full spectrum Δ²_ζ(k) in closed form including the sign and size of α_s, β_s, the low-ℓ shape, the NG hierarchy with SY saturation, plus everything previously derived. Output strictly exceeds input. The sector is now **zero-free-function** in the exact sense the programme's standard defines — conditional on one import and one slot.

**Open items after this memo.**
- **[SLOT CW-S1]** The clock weld: monodromy-invariant state is KMS(2π); which A₂-base coordinate is ln k. (Successor to DS-T1; the load-bearing joint.)
- **[OPEN CW-O1]** Compute the rational: one-loop coefficient (target 3) or anomalous dimension (target 1/6) of the A₂ deformation on the wall. (Successor to DS-T2 + DS-O1 + CW-T2's residue.)
- **[SLOT CW-S2]** Canonical identification of the wall SL(2,ℤ) (Milnor-fiber MCG) with the Cardy/γ = 1 modular structure.
- **[SLOT CW-S3]** d = h(A₂): theorem or coincidence. Do not lean.
- **[OPEN]** Physical role of the ℤ₂ in ℤ₆ = ℤ₂ × ℤ₃.
- **CW-T3/CW-T4 residues:** compute c⁽²⁾(k) and the ⟨TTT⟩ shape functions from the fibration algebra (bands now pre-registered to receive them).

**Supersessions.** CW-T2's success criterion is restated per DS-F1: *derive the flow law and its rational; the pivot value is an epoch reading* (the original wording could be misread as demanding the amplitude, which N2 verifies is barred). v2.1 §23's list remains authoritative with CW-S1–S3 and CW-O1 appended as the named refinements. The Planck–ACT [WATCH] of v2.1 §19.2 is upgraded: outcome (b) — positive running ≳3×10⁻³ — is no longer merely survivable; it is the **prediction** of both surviving A₂ members.

**One-sentence close.** Under the JC strand's A₂ theorem, the last free function of the perturbation sector collapses to a single rational number with two named candidate values — the Coxeter number 3 or the spectral gap 1/6 — each carrying a falsifiable, positive, already-mildly-favored prediction for α_s; five clock laws and three numerological readings of the same clue were executed by the kill battery on the way; and what remains is one weld, one rational, and the data.

---

## References

[E1] *The A₂ Spectral Geometry of the 2026 Jacobian Counterexample*, JC-strand preprint (filed July 2026; Zenodo). — the import CW-P3.
[E2] *Necessary Ambiguity* (Paper A); *The Necessity of i* (Paper B) — JC strand; the S₃/monodromy grammar.
[E3] Causal-Wall Spectral Theory v2.0 + completion v2.1; Descent Spectrum v1.0 + completion v1.1 — this strand's records (receipts S1–S12, R1–R11).
[E4] Planck 2018 X (α_s = −0.0045 ± 0.0067); Planck 2018 IX (f_NL, τ_NL, g_NL); BICEP/Keck 2110.00483 (r < 0.036); Louis et al. 2503.14452 + Calabrese et al. 2503.14454 (P-ACT-LB n_s; mild positive-running preference).
[E5] Arnold–Gusein-Zade–Varchenko, *Singularities of Differentiable Maps* (A₂ normal form, spectrum, monodromy); Milnor, *Singular Points of Complex Hypersurfaces* (fibration; trefoil).
