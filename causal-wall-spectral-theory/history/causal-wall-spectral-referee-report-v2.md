# Referee Report — Causal-Wall Spectral Theory v2.0

**Document under review:** *Causal-Wall Spectral Theory: A Non-Stochastic Completion of the Scalar Cosmological Sector*, technical memorandum v2.0 (2026-08-21), authored independently of the v1.0 audit (`descent-spectrum-audit-v1.md`) and completion (`descent-spectrum-completion-v1_1.md`).
**Filed:** 2026-08-21. **Receipts:** `verify_causal_wall_spectral_v2_1.py` → `causal_wall_spectral_receipts_v2_1.json` — **12/12 pass** (S1–S12).
**Dispositions:** every finding below points at the section of `causal-wall-spectral-completion-v2_1.md` (sections §14–§23, continuing v2.0's numbering) that closes it.

---

## Verdict

The mathematics is clean and the epistemics have improved. Every displayed number in v2.0 reproduces (S1–S4, S8), the holographic dictionary is internally consistent to the symbol (S1), and the scalar normalization Δ²_S = 4/(π⁴c⁽⁰⁾) is literature-verbatim — McFadden's spectral-density formulation of the ⟨TT⟩ two-point function, with the Källén–Lehmann representation ⟨T(x)T(0)⟩ = (π/8)∫dρ c(ρ)∫(d³q/(2π)³) q⁴/(q²+ρ²)e^{iq·x}. The demotions (inflation to "one geometric dual"; the Einstein dictionary r = 16ε, I_ζ = ε𝔖 to conditional bulk reconstruction) are correct register discipline, fully consistent with flag DS-F1 filed in v1.1.

**Convergent verification.** v2.0 was written without sight of the v1.1 audit, yet its conditional reconstruction bounds (8.4)–(8.6) — ε < 2.25×10⁻³, 𝔖 > 2.12×10¹¹, H < 4.7×10¹³ GeV — are numerically identical to v1.1's independent tensor-sector derivation (receipt S4 confirms both routes agree exactly). Two documents, two methods, one number set. This is the strongest kind of internal check the programme can produce short of new data.

Three findings are **gating** (F1–F3): the §3 weld needs its load-bearing structure stated (it is exact, but the exactness rests on an exponential-family/BKM identity, an abelianization step, and a contact-term quotient that v2.0 leaves implicit); the conformal fixed-point limit is a 0×∞ the memo walks past; and the two-invariant economy claim needs typing before it can be filed. All three are closable with existing programme material — no new physics is required — and are closed in the completion. Nothing found is fatal. One live observational stress test (F4) is identified that v2.0 misses entirely and that current data already presses on.

---

## Findings ledger

### F1 [gating] — §3's identification is correct but its proof obligations are unstated. → Completion §14

Equation (2.7) defines K₂ as the Hessian of relative entropy; §3 then computes the second Weyl variation of a "Euclidean connected generating functional" W_Σ and reads off ⟨TT⟩ + contacts. Three joints are silently crossed:

**(a) Which functional, and why do the Hessians agree?** Hess S_rel and Hess W are different objects in general; they coincide at coincidence because the scale-to-state functor acts (to second order) as an *exponential tilt* of the wall state by the smeared trace: dΦ[δζ] = tilt by ∫ζT. For a tilted family the relative entropy is the Legendre remainder S_rel(ζ) = ζψ′(ζ) − ψ(ζ), whose Hessian at ζ = 0 equals ψ″(0) = Var(T) — *even though the first variations differ* (⟨T⟩ = ψ′(0) ≠ 0 is allowed). Receipt S5 verifies the lemma symbolically. This is the classical shadow of the quantum statement: **K₂ = the BKM (Kubo–Mori) two-point function of the stress trace**, which is exactly what "Φ*G^BKM" in (2.7) says — but §3 never connects (2.7) to (3.3), and a referee outside the programme will read the step as a covariance/precision confusion. It is not one; ζ is a *coordinate on state space* (a coupling direction), T is its conjugate score, and Fisher-in-coordinates = covariance-of-scores. Say so.

**(b) BKM vs. Euclidean vs. Wightman.** The BKM correlator, the symmetrized correlator, and the Euclidean ⟨TT⟩ differ by known KMS kernels for a general state. They coincide on the observable sector because that sector is abelian to O(e^{−3N_out}) — v1.1 §15.2/L1 (Chentsov collapse). The weld from v1.1 is load-bearing here and should be imported by name: *abelianize first, and the correlator ambiguity never arises.*

**(c) The Im prescription is the contact-term quotient.** (3.3) says "plus local contact terms" and then drops them without justification. The justification is one line: contact terms are polynomial (analytic) in q², hence have no branch cut, hence do not contribute to Im B(−q²−i0). The spectral projection *is* the quotient by contacts. Bonus hygiene, worth stating because it strengthens the memo: **d = 3 has no local Weyl anomaly** (odd dimension), so there is no anomaly channel for the scalar response to hide in — the entire response is genuine spectral flow, which is precisely §5's thesis. The one parity-odd contact in 3d ⟨TT⟩ (gravitational Chern–Simons) is killed by the same Im/parity projection.

**(d) Sign convention unregistered.** K_ζ > 0 requires a branch/sign choice. McFadden–Skenderis publish Δ²_S(q) = −q³/(16π² Im B(−iq)) — with an explicit minus under their −iq continuation. v2.0's Δ²_S = q³/(16π² Im B(−q²−i0)) absorbs the sign into the −i0 prescription. Fine, but per the programme rule (conventions registered with predictions, the P3 lesson), register it: **Im B(−q²−i0) ≥ 0 ⇔ spectral positivity of the trace–trace Källén–Lehmann density.** Same for Im A.

### F2 [gating] — The conformal fixed-point limit is a 0×∞ the memo does not confront. → Completion §15

§5: at the fixed point the trace vanishes, "local scale is gauge." But then c⁽⁰⁾ → 0 ⇒ K_ζ → 0 ⇒ Δ²_ζ = 4/(π⁴c⁽⁰⁾) → ∞. A hostile reader lands the obvious hit: *the theory's "scale is gauge" limit predicts infinite lumpiness.* The resolution exists and is a strength once stated: at the fixed point ζ decouples from every observable (all its couplings pass through T = βᴵO_I), so the divergent covariance multiplies vanishing couplings; the divergence is the zero-information-cost statement for a gauge direction, identical in content to the known 1/ε divergence of Δ²_ζ in the exact de Sitter limit (v1.1 L5: ζ is the dilation zero mode at ε = 0). Receipt S6 records the bookkeeping identity ε·Δ²_ζ = 1/𝔖.

A second conflation hides in the same paragraph: **two senses of "near-conformal."** (i) The *exponent* is near-critical: δ ≈ 0.03 ≪ 1 (slow flow). (ii) The *amplitude* is anything but small: c⁽⁰⁾ ≈ 2×10⁷ is a large spectral density — a large effective central charge, reading as N ~ √c⁽⁰⁾ ≈ 4.4×10³ in the large-N normalization (receipt S12), squarely in the "perturbative large-N QFT" regime McFadden–Skenderis themselves proposed. The observed sky is shape-near-critical and amplitude-large, and these are different facts: the smallness of Δ²_ζ = 1/I_ζ is the *largeness of capacity*; the redness is the *slowness of flow*. The memo's own best sentence is available once the limit is confronted: *structure exists because scale is almost, but not exactly, gauge.*

### F3 [gating] — The two-invariant economy claim (§10) is under-typed. → Completion §19, §23

"Two state invariants (c⁽⁰⁾(k*), δ*)" is the minimal *universality class*, not the theory's parameter count. Until the wall algebra is identified, c⁽⁰⁾(k) is one free *function* — the same residual as v1.1's DS-O1 (ε(N)), transported to wall-RG coordinates (in the geometric member they are literally the same function: c⁽⁰⁾ = 4ε𝔖/π⁴, so d ln c⁽⁰⁾/d ln k = 2ε + d ln ε/d ln k — the v1.1 tilt decomposition, re-derived; receipt S4). The memo's §13.4 correctly names the microscopic task; §10 should not be phrased so that a reader could count parameters before that task is done. Also: prediction 4, "zero running at leading constant-exponent order," is as stated a *class definition*, not a prediction. Its predictive content is quantitative and should be filed as such: |α_s| ≲ δ² ≈ 1.2×10⁻³ (Planck) / 0.7×10⁻³ (ACT) — receipt S9 — against which a kill condition can bite (F4).

### F4 [major] — The Planck–ACT tilt difference is the sector's live near-term stress test, and v2.0 files it as a shrug. → Completion §19

§7 presents δ_Planck = 0.0351 ± 0.0042 and δ_ACT ≈ 0.026 ± 0.003 as "current determinations under different data combinations." Quantify it: with P-ACT-LB (n_s = 0.9743 ± 0.0034; the combination should be registered — see F9), Δδ = 0.0094, a **1.74σ** difference (receipt S9). Not yet a wound. But the memo's own minimal class makes this comparison sharp: constant δ means the *same* exponent at every scale, so if the difference is physical scale dependence rather than systematics, it implies α_s ≈ Δδ/Δln k ≈ +3–6×10⁻³ across the relevant lever arms — **above the minimal-class bound δ² ≈ 10⁻³** (receipt S9). And the sign matters: the ACT DR6 extended-models analysis itself reports that P-ACT-LB *mildly prefers positive running* (while excluding the Lyman-α negative running α = −0.010 at >3σ). So the data are currently leaning, weakly, exactly on the axis where the minimal class is thinnest. Verdict to file: [WATCH], with pre-registered consequence — a confirmed |α_s| ≳ 3×10⁻³ kills the constant-exponent class (the *typing* survives as a running-exponent flow; the distinction between class kill and typing kill must be filed now, before the data move).

### F5 [major] — Tensor slot: correct demotion, three repairs. → Completion §16–§17

(i) **Wording slip in §8:** "at least two orders of magnitude more precise against spin-two deformation." The *spectral-density* ratio is c⁽²⁾/c⁽⁰⁾ > 222 (2.35 orders); the *per-mode precision* ratio is K_γ/K_ζ = 2/r > 55.6 (1.74 orders) — receipt S3. The sentence is true for the density and false for the per-mode precision; register which ratio is quoted. (ii) The tensor normalization Δ²_T = 32/(π⁴c⁽²⁾) fixes Im A(−q²−i0) = (π²/16)c⁽²⁾q³ — a relative factor of 4 against the scalar's (π²/64) — which is a legitimate definition of c⁽²⁾ but is nowhere registered as one (receipt S1). (iii) **A free weld is left on the table:** in the geometric member, c⁽⁰⁾ = 4ε𝔖/π⁴ and c⁽²⁾ = 2𝔖/π⁴ reproduce r = 16ε, Δ²_t = 16/𝔖, and every bound in §8.4–8.6 identically (receipt S4). Stating the member identities costs two lines and buys the full concordance between v2.0 and v1.1, including the tensor-tilt comparison: geometric member n_t = −r/8 versus general near-critical wall class n_t = −d ln c⁽²⁾/d ln k = O(δ²) (c⁽²⁾ ≈ c_T is fixed-point-stationary; running enters at second order in the deformation). Both are ≲ few×10⁻³ — honest statement: n_t discriminates classes only in the far future; the near-term tensor content is the r value itself, which fixes c⁽²⁾ in one reading.

### F6 [major] — "Quasi-free ⇒ very small cumulants" (§9) is the conclusion wearing the mechanism's clothes. → Completion §18

*Why* is the leading wall state quasi-free? The available mechanism is the same as v1.1 §17, now in wall-native units: **large-capacity factorization.** If the wall's connected cumulant kernels are extensive in the spectral density (large central charge / large N), normalized cumulants scale as κ_n ~ c^{1−n/2}; the capacity floor is 1/√c⁽⁰⁾ ≈ 2.3×10⁻⁴ (receipt S10), with the geometric member tightening the intrinsic quantum piece to 1/√𝔖 ≲ 2×10⁻⁶. Above both sit the flow-induced pieces O(ε, δ) ≈ 10⁻²–10⁻³ (shape-dependent) and the dilation Ward term f_NL^sq = 5δ/12 = 0.0146 (Planck) / 0.0108 (ACT). Current data (Planck 2018 IX: local −0.9±5.1, equilateral −26±47, orthogonal −38±24) sit within 1.6σ of zero on every shape — receipt S10. The kill condition inherited from v1.1 should be restated here with the wall-native reason: the sector has **no c_s dial** (falsification 7 already bans it), so any |f_NL| ≳ 1 on any shape kills the near-critical large-capacity class outright, not a parameter choice.

### F7 [major] — Conservation joint again unstated. → Completion §20

Same gap as v1.0's G3, inherited verbatim: the dictionary outputs a wall/superhorizon covariance; the transfer integral (9.4) consumes it at re-entry; the bridge is one line — rank one ⇒ δp_nad = 0 ⇒ ζ constant on superhorizon scales (Wands–Malik–Lyth–Liddle; Weinberg). In the holographic frame this is implicit in "the QFT computes late-time correlators," but the programme does not file implicit joints.

### F8 [major] — §6 borrows empirical support from a different member of the family. → Completion §19.3

"Published fits have shown that such non-geometric holographic models can fit the CMB comparably" — true (Afshordi–Gould–Skenderis; Easther–Flauger–McFadden–Skenderis before them), but the fitted spectral density in those works is the *perturbative-QFT* form with logarithmic running, c(q) ~ q³/[g̃² ln²-type], **not** v2.0's minimal constant-δ power law. The support is for the *typing* (spectra from a wall ⟨TT⟩ spectral density), not for the minimal class. File the AGS form as a named in-family alternative; the discriminant between the two members is low-k/low-ℓ behavior — a data question, and an honest one to leave open.

### F9 [registration] — Conventions to register (P3 lesson). → Completion §21

(i) Im-branch positivity (F1d). (ii) The ACT combination behind δ_ACT = 0.026: **P-ACT-LB** (n_s = 0.9743 ± 0.0034); P-ACT alone gives 0.9709 ± 0.0038 (δ = 0.029) — quoting "ACT" without the suffix is ambiguous across a half-σ. (iii) The c⁽²⁾ normalization (F5ii). (iv) k is the comoving wavenumber *and* the wall resolution coordinate — the MS identification of boundary momentum with comoving momentum, stated once. (v) Pivot k* = 0.05 Mpc⁻¹ for every boxed number. (vi) A glossary freezing the register: **capacity** (𝔖, or the c⁽²⁾/c_T scale), **response** (c⁽⁰⁾ — defect-weighted capacity), **discernibility** (I_ζ), **precision** (K_ζ) — v2.0 currently calls c⁽⁰⁾ "capacity" (§7, Fig. 3) while v1.1 reserved that word for 𝔖; the collision is exactly the kind of drift the taxonomy exists to prevent.

### F10 [minor] — "No intrinsic wall length" vs. RG running. → Completion §21

The axioms of §4 forbid an intrinsic length; §5 then runs a coupling. The reconciliation is the criticality-class statement (v1.1 §14.1): the axioms fix the *critical* kernel; the log channel is the one dilation-covariance-breaking channel, and it is occupied — by the tilt. One hygiene line prevents the cheap objection.

### F11 [minor] — §11's block-diagonality is asserted, not argued. → Completion §21

G_Nζ = 0 holds because the constant mode is quotiented out of T_σ̄Sc(Σ) (eq. 2.3): the homogeneous direction is orthogonal to C∞(Σ)/ℝ by construction. Say it in one sentence; as written it looks like an assumption.

### F12 [minor] — §1's age/ontology paragraph is right but untagged. → Completion §21

The claim ("the underlying state need not be parameterized by FLRW proper time; apparent chart age does not fix ontological duration") is a correct register move — it is the wall/block discipline applied to cosmic time — and it is properly agnostic *both ways* (it does not claim the reconstruction is young, either). Tag it [REMARK — register discipline] so it cannot be quoted as a physics claim.

### F13 [minor] — Presentation items.

(i) The abstract's dictionary line must typeset unambiguously as Δ²_ζ = k³/(16π² Im B) — the plain-text extraction reads as a product. (ii) (3.3)'s "precisely the datum needed for the scalar covariance" → "for the scalar *precision* (covariance by inversion)"; the current wording invites the F1a misreading. (iii) §13.1's "not a random force" framing is earned by this point, but only if §14's chain is in place.

### F14 [checks passed]

All of: dictionary internal consistency (S1); c⁽⁰⁾(k*) = 1.9564×10⁷, I_ζ = 4.7644×10⁸, per-e-fold growth 3.57%/2.63% (S2); tensor bounds 222.2 and 4.35×10⁹ (S3); conditional reconstruction bounds identical to v1.1's independent computation (S4); ⟨TT⟩ = 4B trace algebra exact (S7); P3 spectrum to 1.9×10⁻³¹ (S8); Ward f_NL values (S10); tilt identities (S11). No numerical error found anywhere in v2.0.

### F15 [strengths, for the record]

The holographic weld is the *right* generalization — it converts v1.0's postulated precision operator into a named QFT observable with an existing computational literature (2-pt, 3-pt, and fit machinery all published); the demotions are correct register discipline and independently reproduce v1.1's flag DS-F1; the overclaim guard box in §10 is exactly programme-grade; the falsification list exists (it needs numbers, which the completion supplies); and §1's decomposition of the "quantum fluctuations" sentence into three separable claims is clean enough to reuse verbatim in any external-facing document.

### F16 [cross-memo] — One open-problem list, not two. → Completion §16, §23

v1.1 §20 filed {DS-T1 state selection, DS-T2 norm supply, DS-O1 constitutive law}; v2.0 §13.4 files {identify wall QFT/state; compute c⁽⁰⁾, c⁽²⁾, ⟨TTT⟩}. These are the same obligations in two coordinate systems and must be merged or the programme will double-count its debts: **CW-T1** (identify wall algebra/state) ⊇ DS-T1; **CW-T2** (compute c⁽⁰⁾(k)) ⊇ DS-T2 + DS-O1; **CW-T3** (compute c⁽²⁾(k)); **CW-T4** (compute ⟨TTT⟩). The completion issues the merged list with kill shapes and a supersession note; v1.1 remains the geometric-member derivation record.

---

## Receipt map

| Receipt | Verifies | Finding |
|---|---|---|
| S1 | Dictionary internal consistency; c⁽²⁾ normalization made explicit | F1, F5ii |
| S2 | Calibration c⁽⁰⁾, I_ζ, per-e-fold growth | F14 |
| S3 | Tensor bounds; density-ratio vs precision-ratio | F5i |
| S4 | Geometric-member weld; v1.1 concordance; two-route 𝔖 bound; H bound | F5iii, F16 |
| S5 | Exponential-family Hessian lemma | F1a |
| S6 | Gauge-limit bookkeeping ε·Δ² = 1/𝔖 | F2 |
| S7 | ⟨TT⟩ = 4B trace algebra | F14 |
| S8 | P3 spectrum | F14 |
| S9 | Tilt tension 1.74σ; class bound δ²; implied-α band | F3, F4 |
| S10 | Ward f_NL; capacity floors; Planck headroom | F6 |
| S11 | Tilt identities; α_s = 0 for constant δ | F3 |
| S12 | Dual-N reading of the amplitude | F2 |

**Recommendation:** accept with the completion (v2.1) attached; the three gating findings are closed there with existing programme material; the [WATCH] item (F4) is filed with pre-registered consequences before the next data release can move it.
