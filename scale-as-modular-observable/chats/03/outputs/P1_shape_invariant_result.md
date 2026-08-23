# P1 — The Shape-Invariant Test

## Run against DESI DR2 BAO + Pantheon+. Result, method, and reclassification.

**Thomas Ruble research programme — AI-assisted analysis**
**21 August 2026**

Code and data in `P1/`. Every number below is reproduced by the scripts listed in §9.

---

## 0. Result

> **K1 does not fire. But the theory did not pass — the test could not be
> performed.**
>
> The shape exponent is unconstrained: Δχ² = 0.79 across p ∈ [0.05, 20], with the
> theory value p = 2 at 0.88σ. The reason is structural, not statistical, and it
> will not go away with better background data.

**P1 should be demoted from primary test.** It should be replaced by ϱ⊥ and z_c,
which *are* constrained now, and by the zero-parameter model comparison, which is
the strongest statement the data currently support:

$$\chi^2_{\rm rigid} - \chi^2_{\Lambda{\rm CDM}} = -3.38 \quad\text{with zero extra parameters}$$

the best AIC of any model tested, including CPL.

---

## 1. Making P1 well-posed

The invariant is 9(1+w)² + 6 dw/dN = 4ϱ⊥². Testing it by differentiating a
non-parametric w(z) reconstruction requires three derivatives of distance data
and is hopeless. Instead, embed the theory in the family that nests it:

$$\rho_X(N) = \rho_*\operatorname{sech}^p\!\big[\beta(N-N_c)\big], \qquad N = \ln a$$

With X := 1 + w_X, separate conservation gives

$$X = \tfrac{p\beta}{3}\tanh(\beta u), \qquad \frac{dX}{dN} = \frac{p\beta^2}{3} - \frac{3}{p}X^2$$
$$\boxed{\;9X^2 + 6\frac{dX}{dN} = X^2\left(9 - \frac{18}{p}\right) + 2p\beta^2\;}$$

**The invariant is constant if and only if p = 2**, and then it equals 4β², i.e.
ϱ⊥ = β. The family also nests ΛCDM (β → 0, sech^p → 1).

> **P1 reduces to measuring one number. The theory predicts p = 2 exactly.**

Verified analytically against numerical differentiation of w(z) to 6×10⁻¹⁰, and
the p = 2 invariant is z-independent to machine precision (`p1_validate.py`, V6).

---

## 2. Data and likelihood

**DESI DR2 BAO** — 13 measurements from 7 tracers, 0.295 ≤ z_eff ≤ 2.330
(Abdul Karim et al., arXiv:2503.14738), with the within-tracer correlations
ρ(D_M/r_d, D_H/r_d) = −0.459, −0.404, −0.416, −0.434, −0.500, −0.431. The
normalisation 𝒟 = c/(H₀r_d) is profiled analytically.

**Pantheon+** — Scolnic et al. 2022 / Brout et al. 2022, full STAT+SYS
covariance. Cuts: z_HD > 0.01 **and** IS_CALIBRATOR = 0 → **1580 SNe**. The
often-quoted 1590 is z_HD > 0.01 alone, which retains 10 calibrators whose
magnitudes are tied to Cepheid distances; those must go for a cosmology-only fit.
M_B is profiled analytically, so SNe constrain only the shape of D_L(z).

The released covariance is symmetric only to 3×10⁻⁸ (778 entries of 2.9M, at the
file's 8-decimal text precision). Symmetrised.

**Distance integrals** on a graded grid — 1001 points below z = 0.15, 2001 above.
A uniform grid fails at low z, where Pantheon+ reaches z = 0.0102 and the small
integral amplifies interpolation error. Worst relative error 3.3×10⁻⁷, four
orders below the smallest datum's precision.

---

## 3. Validation

No result was believed until these passed.

| check | this work | published |
|---|---|---|
| distance integral vs `scipy.quad` | 3.3×10⁻⁷ worst | — |
| Pantheon+ alone, flat ΛCDM | Ω_m = 0.3324 **+0.0185 −0.0180** | 0.334 ± 0.018 (Brout+22) |
| DESI DR2 alone, flat ΛCDM | Ω_m = 0.2970 **+0.0087 −0.0084** | 0.2975 ± 0.0086 (DESI DR2) |
| DESI DR2, H₀r_d | **101.56** (100 km/s) | 101.54 ± 0.73 |
| DESI BAO χ²/dof at best fit | 10.551 / 11 = 0.959 | — |
| sech^p → ΛCDM as β → 0 | exact | — |
| sech^p(p=2, β=1, N_c) = rigid branch | exact | — |

---

## 4. Model comparison

DESI DR2 BAO + Pantheon+, N_data = 1593. "dark" counts dark-sector shape
parameters; k counts all fitted parameters including 𝒟 and M_B.

| model | dark | k | χ² | Δχ² vs ΛCDM | ΔAIC |
|---|---|---|---|---|---|
| ΛCDM | 0 | 3 | 1400.142 | 0 | 0 |
| **rigid: p=2, ϱ⊥=1, r_c=1** | **0** | **3** | **1396.762** | **−3.380** | **−3.380** |
| rigid, ϱ⊥ free (r_c=1) | 1 | 4 | 1395.596 | −4.545 | −2.545 |
| CPL (w₀, w_a) | 2 | 5 | 1394.980 | −5.162 | −1.162 |
| invariant-constant (p=2) | 2 | 5 | 1394.868 | −5.274 | −1.274 |
| sech^p (p, β, N_c free) | 3 | 6 | 1394.024 | −6.118 | −0.118 |

Best fits: ΛCDM Ω_m = 0.3039; rigid Ω_m = 0.3224; rigid ϱ⊥ free Ω_m = 0.3155,
ϱ⊥ = 0.8005; CPL Ω_m = 0.3056, w₀ = −0.886, w_a = −0.239; invariant-constant
Ω_m = 0.3086, β = 0.588, z_c = 0.634.

**The rigid branch has the best AIC of any model tested.** It buys Δχ² = −3.38
over ΛCDM at zero parameter cost. This is modest, background-only, and partly
retrodictive — evidence of viability, not discovery — but it is the strongest
claim the current data support.

---

## 5. The P1 test itself

Profile likelihood in p, minimising over (Ω_m, β, N_c) at each p, with the β
bound widened to 60 to expose the runaway direction.

| p | 0.05 | 0.25 | 1.0 | **2.0** | 5.0 | 20.0 |
|---|---|---|---|---|---|---|
| Δχ² | 0.000 | 0.644 | 0.756 | **0.775** | 0.786 | 0.791 |
| β | 5.66 | 1.78 | 0.84 | **0.588** | 0.369 | 0.184 |
| Ω_m | 0.3083 | 0.3084 | 0.3086 | **0.3086** | 0.3086 | 0.3086 |

**Total Δχ² across p ∈ [0.05, 20] is 0.791.** There is no 1σ, 2σ or 3σ bound.
The theory value p = 2 sits at Δχ² = 0.775, i.e. 0.88σ from a boundary minimum.

**A Planck acoustic anchor does not help.** Writing θ\* as a 14th BAO point in the
same units — D_M(z\*)/r_d = (r_s\*/r_d)/θ\* = 94.32 ± 0.28, needing neither h nor
ω_b — the total Δχ² becomes 0.779 and p = 2 sits at 0.762 (0.87σ). The ΛCDM
prediction 93.84 is 1.7σ from the anchor, so the anchor is consistent and the
sanity check passes; it simply carries no information about p.

### Why, and why it will not improve

The best-fit crossing is z_c = 0.634 with width 1/β = 1.70 e-folds. The data span
z ∈ [0.0102, 2.33], i.e.

$$\theta = \beta(N-N_c) \in [-0.42,\, +0.28]$$

**less than one transition width in total.** The exponent p controls the *tails*
of sech^p, and the tails lie where ρ_X is subdominant — reaching θ = −2 would
require data at z ≈ 48, where there is no dark-energy signal to measure.

The degeneracy is observational, not numerical. Along the entire flat direction:

| p | w(0.5) | w(1.5) | I(0) | I(1) | I(1)/I(0) |
|---|---|---|---|---|---|
| 0.05 | −0.9543 | −1.0927 | 0.124 | 1.202 | 9.71 |
| 2.00 | −0.9802 | −1.0960 | 1.383 | 1.383 | 1.000 |
| 20.0 | −0.9804 | −1.0955 | 1.454 | 1.371 | 0.943 |

w(z) varies by < 0.03 over the data range while the invariant's value swings by
two decades and its constancy ratio by an order of magnitude. **These are
observationally the same model.**

---

## 6. What the data *can* constrain

Profiles recomputed with grid-scan starts (see §7).

| quantity | best fit | 1σ | 2σ | theory | tension |
|---|---|---|---|---|---|
| **ϱ⊥**, rigid branch (r_c = 1) | 0.800 | [0.575, 0.982] | [open, 1.146] | 1 | **1.08σ** |
| **ϱ⊥**, invariant-constant branch | 0.600 | [open, 0.906] | [open, 1.144] | 1 | 1.36σ |
| **z_c**, p = 2 branch | 0.650 | [0.293, open] | [0.159, open] | 0.342 | **0.72σ** |

Both rigid predictions are consistent at ~1σ. The intervals are one-sided
because ϱ⊥ → 0 and z_c → large both approach ΛCDM, which is only Δχ² ≈ 5 worse.

**Independent confirmation of T4.** The fitting code's root-finder locates the
existence ceiling — where the two flatness roots merge and the rigid branch
ceases to exist — at ϱ⊥^max = 1.81413 for Ω_m = 0.310598, agreeing with T4's
closed form to 10⁻⁷ across Ω_m ∈ [0.28, 0.35]. This is production fitting code
reproducing a theorem derived independently.

---

## 7. Two errors caught in this analysis

Recorded because they nearly produced a false result.

**E1 — a spurious 2.3σ.** The first z_c profile used solution-continuation and
reported Δχ² = 5.27 at z_c = 0.342, i.e. **2.30σ tension with the rigid
prediction**. Direct scanning showed the optimiser was trapped at β → 0 for all
z_c < 0.5: at z_c = 0.342 the true minimum is β = 0.8 with χ² = 1395.38, not
β → 0 with χ² = 1400.14. The correct tension is **Δχ² = 0.518, i.e. 0.72σ**. All
profiles were recomputed with coarse grid-scan starts.

**E2 — a spurious ceiling.** The T4 root-finder used `brentq` on a single
bracket. Above ϱ⊥ = 3/2 the flatness condition has *two* roots, so the bracket
endpoints share a sign and `brentq` fails — which the code misread as "no
solution", reporting a ceiling at ϱ⊥ ≈ 1.57. Replaced with a sign-change scan
selecting the root continuously connected to the low-ϱ⊥ branch; the ceiling then
reproduces the closed form exactly.

Neither error would have been visible in the output alone.

---

## 8. Forecast

Δχ² scales as 1/f² when all errors scale by f.

| discrimination | Δχ² now | improvement for 3σ |
|---|---|---|
| smooth pulse vs sharp step (p=2 vs p=0.05) | 0.775 | **3.4×** |
| p = 2 vs p = 1 | 0.018 | 22.4× |
| p = 2 vs p → ∞ | 0.017 | 23.0× |

DESI-5yr plus LSST plausibly reach 3.4× and could therefore distinguish a smooth
pulse from a sharp step. Nothing planned reaches 22×, so the fine shape — the
actual content of the invariant — stays out of reach of background data.

---

## 9. Reclassification recommended

**Demote P1 from "primary test."** The invariant's constancy is a statement about
the tails of the transition, and the tails are where the dark sector does not
exist. This is a structural limitation of background probes, not a temporary one.
The master document's §13.1 should say so.

**Promote in its place:**

1. **ϱ⊥** — measurable now at ~20%, currently 0.80 [0.575, 0.982] on the rigid
   branch, 1.08σ from unity. This is the determination-table entry the programme
   has been asking for, and it is the first one from a direct rigid-shape fit
   rather than a CPL compression.
2. **z_c** — 0.65 [0.293, open], 0.72σ from the rigid 0.342.
3. **The zero-parameter model comparison** — Δχ² = −3.38 vs ΛCDM, best AIC of six
   models. Modest, but honest and it costs nothing.

**Where the invariant might still be testable:** not in the background. Growth
data (fσ₈) depend on ρ_X(z) through a different functional, and CMB lensing
weights a different redshift window. If the invariant is to be tested at all, it
will be there — which makes the perturbation sector, and therefore Q1, the
gating problem for observations as well as for theory.

---

## 10. Files

| file | contents |
|---|---|
| `p1_data.py` | DESI DR2 BAO table with correlations; Pantheon+ loader (auto-downloads, applies cuts, symmetrises covariance) |
| `p1_model.py` | E(z) for ΛCDM / CPL / sech^p / rigid; graded-grid distances; profiled BAO and SN likelihoods; the invariant |
| `p1_validate.py` | V1–V6, the validation suite of §3 |
| `p1_stage1.py` → `p1_stage1.json` | model comparison (§4), ~90 s |
| `p1_stage2.py` → `p1_stage2.json` | the p profile (§5), ~180 s |
| `p1_stage3.py` → `p1_stage3.json` | CMB acoustic anchor (§5), ~130 s |
| `p1_stage4.py` → `p1_stage4.json` | ϱ⊥ and z_c profiles, grid-scan starts (§6), ~260 s |

Run `python3 p1_validate.py` first. It must pass before any stage is believed.
