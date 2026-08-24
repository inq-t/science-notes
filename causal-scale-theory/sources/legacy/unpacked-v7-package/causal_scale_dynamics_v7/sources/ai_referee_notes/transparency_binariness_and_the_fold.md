# Transparency, Binariness, and the Fold

## Structural derivations on the rigid modular–Weyl branch — and a presentation guide for the master document

**Thomas Ruble research programme — AI-assisted technical hand-off**
**21 August 2026**

---

**Status.** Working hand-off memorandum, not peer reviewed. Every numerical claim
is reproduced by `receipts_transparency_fold.py` (R1–R12), which requires no
external data. Exact algebraic results carry `[THEOREM]`. Conditional results
state their hypothesis. Structural analogies carry `[RHYME]` and are not
load-bearing. Two results are negative and labelled as such; they are as
important as the positive ones.

**How to use this document.** Part I is what is derived. Part II is the r_c
problem, which is the load-bearing gap. Part III is the A₂ ledger. Part IV is
predictions. **Part V is a presentation guide for the master document** and is
the part to read if you only have twenty minutes. Part VI is the work order.

---

# Part 0 — Executive summary

| | claim | status |
|---|---|---|
| **T1** | Any operator with a ρ_X-proportional potential reduces in the θ-frame to exactly Pöschl–Teller with strength Λ = c·χ⊥, **independent of ϱ⊥** | `[THEOREM]` |
| **T2** | Transparency ⟺ c·χ⊥ = ℓ(ℓ+1); ℓ = 1 ⟺ one bound state ⟺ no continuum dark mode | `[THEOREM]`, conditional on T1's hypothesis |
| **T3** | ϱ⊥ = 1 ⟺ w_∞ = −1/3 ⟺ q_∞ = 0 ⟺ a ∝ t ⟺ event horizon marginally absent | `[THEOREM]` |
| **T4** | Flatness + r_c impose a hard ceiling ϱ⊥ ≤ ϱ⊥^max = 1.814123 at Ω_m = 0.310598, r_c = 1 — a saddle-node in the moduli of solutions | `[THEOREM]` |
| **T5** | The crossover traverses Fisher length π = the diameter of the binary state space, independent of ϱ⊥ | `[THEOREM]` |
| **T6** | The shape invariant is exactly ⟨Q⟩² + Var(Q) = ⟨Q²⟩ = 1 | `[THEOREM]` |
| **T7** | X := 1+w obeys the canonical A₂ saddle-node normal form X′ = A − BX², A = (2/3)ϱ⊥², B = 3/2; ϱ⊥ = 0 is the fold | `[THEOREM]` |
| **T8** | r_c = 1 ⟺ matter–dark equality coincides exactly with the susceptibility peak and the w_X = −1 crossing; the acceleration onset (z = 0.786) is *derived*, not identified | `[THEOREM]` |
| **T9** | The shape invariant is **blind to r_c** ⟹ ϱ⊥ and r_c are separately measurable; the observed degeneracy is a data degeneracy, not a structural one | `[THEOREM]` |
| **T10** | The T4 ceiling scales with r_c: ϱ⊥^max = 1.648 (r_c = 0.8), 1.814 (1.0), 2.481 (1.5) | `[THEOREM]` |
| **N1** | The linear growth operator does **not** satisfy T1's hypothesis | `[NEGATIVE]` |
| **N2** | The single-field completion is a ghost through the whole phantom era, and at the crossing is an inverse-square potential at **exactly** the critical coupling g = 1/4 | `[NEGATIVE]` |

**The single most useful result is T1.** It proves ϱ⊥ and χ⊥ act on *different
slots of the same operator*. That is not an analogy to the c/G grammar of general
relativity; it is the same structural fact.

**The most consequential surprise is T4.** Both anomalous determinations of ϱ⊥ —
1.839 ± 0.376 from DESI+CMB without supernovae, and the 1.7–1.8 the addendum
reports when r_c is freed — sit *at the ceiling*. They are boundary-dominated,
the same pathology diagnosed one level down for Σm_ν ≥ 0. Repaired discrepancy,
**not** confirmation.

**The most actionable result is T9.** The r_c–ϱ⊥ degeneracy that currently
threatens the parameter-count claim is breakable *now*, with no new theory, by
measuring the shape invariant from a w(z) reconstruction.

---

# Part I — What is derived

## 1. The derivation already in the erratum

Erratum §2 posits the rank-one binary family ρ_θ = e^{θQ}/(2cosh θ), Q = ±1,
from which the BKM metric follows in one line as the variance of a two-point
distribution:

$$G^{\rm BKM}_{\theta\theta} = \operatorname{Var}_{\rho_\theta}(Q) = \operatorname{sech}^2\theta$$

**This does derive sech².** It is not a chosen bump function; it is the variance
of a binary observable along an exponential family (R1, machine precision).

Note precisely what is used. For a general binary Q ∈ {q₊, q₋},
Var(Q) = ¼(q₊−q₋)² sech²θ. So:

- `[THEOREM]` binariness (rank two) ⟹ sech² **shape**
- `[THEOREM]` Q² = 1 ⟹ the invariant equals exactly 4ϱ⊥² (T6)

The derivation moves the question from *"why sech²"* — ugly, no natural answer —
to *"why rank one"*, which is clean and has an independently motivated candidate:
the crossing no-go already demands pair structure (§4). Whether those are the
same two-level structure is **Q1**, and in my judgement the highest-value theorem
target in the programme.

Still postulated after the derivation: rank one; the soldering law dθ/dN = ϱ⊥;
the constitutive law ρ_X = χ⊥𝒳_σ; the value ϱ⊥ = 1 (partly addressed by T3);
the normalisation r_c = 1 (**Part II**).

## 2. The two-constant grammar, made exact

### 2.1 The invariant object is ϱ⊥-free

𝒳_σ is the pullback of the BKM metric along Φ: ℝ_Weyl → 𝒮(𝒜), hence a *quadratic
differential*, not a scalar. The invariant object is

$$\boxed{\;\mathcal{X}_\sigma\, dN^2 = \operatorname{sech}^2\theta\; d\theta^2\;}$$

in which **ϱ⊥ does not appear**. The state path and its Fisher metric are
absolute; ϱ⊥ says only how Weyl scale parameterises the path.

Two corollaries (R1):

- Total Fisher length ∫v_B dN = ∫sech θ dθ = **π**, independent of ϱ⊥ (T5).
- π is exactly the diameter of the binary state simplex, ∫₀¹dp/√(p(1−p)) = π. The
  crossover is a **complete traversal from one pure state to the other**. Not "a"
  transition; *the* transition.

### 2.2 The two slots `[THEOREM T1]`

Let ψ_NN + [K² + c ρ_X]ψ = 0 with ρ_X = χ⊥ϱ⊥² sech²[ϱ⊥(N−N_c)]. Substituting
θ = ϱ⊥(N−N_c), so d²/dN² = ϱ⊥² d²/dθ²:

$$\boxed{\;\psi_{\theta\theta} + \left[\frac{K^2}{\varrho_\perp^2} + c\,\chi_\perp\operatorname{sech}^2\theta\right]\psi = 0\;}$$

The ϱ⊥² inside ρ_X — from the pullback factor (dθ/dN)² — **exactly cancels** the
ϱ⊥² from the chain rule. The Pöschl–Teller strength Λ = c·χ⊥ contains no ϱ⊥.

| | slot | role | GR analogue |
|---|---|---|---|
| **ϱ⊥** | eigenvalue: K² → K²/ϱ⊥² | reparameterises the spectral coordinate; sets which modes see the pulse and how wide it is | **c** — relates coordinate measures, never a coupling |
| **χ⊥** | potential strength Λ = cχ⊥ | how strongly the information geometry gravitates; sets reflection, bound states, transparency | **G** — couples stress-energy to curvature |

`[DEDUCTION]` One constant cannot do both jobs, because they occupy different
positions in the same second-order operator. The addendum's instinct that making
one number do both "would itself be a category error" is correct and now has a
one-line proof.

### 2.3 Rigidity ≠ value

Two different claims with different evidence:

- **ϱ⊥ = constant** ⟺ N is an *e-affine* parameter of the exponential family (θ
  is the canonical coordinate; constant slope means N is affinely related to it).
  This is the **soldering law**.
- **ϱ⊥ = 1** ⟺ the affine normalisation matches Q² = 1. This is a **value**, and
  T3 gives it an independent characterisation.

Also endorse the addendum's reading: θ = ½ln(p₊/p₋) ⟹ p₊/p₋ = (a/a_c)^{2ϱ⊥}, so
2ϱ⊥ is the Weyl character exponent of the modular odds ratio, and the
𝓛_pol ≅ 𝓔[2] target follows.

### 2.4 The dual-coordinate table

| information geometry | cosmology | relation |
|---|---|---|
| e-affine coordinate θ | Weyl scale N | θ = ϱ⊥(N − N_c) |
| m-affine coordinate η = ⟨Q⟩ | equation of state | η = tanh θ = (3/2ϱ⊥)(1+w_X) |
| metric g = dη/dθ = Var(Q) | energy density | ρ_X = χ⊥ϱ⊥² g |
| normalisation ⟨Q²⟩ = 1 | shape invariant | 9(1+w)² + 6w′ = 4ϱ⊥² |

**ρ_X is the Jacobian of the Legendre transform between the dual flat
structures.** Dark energy is not a fluid; it is the conversion factor between the
two flat connections of a dually flat manifold. This is the retyping, and it is
the strongest single sentence the programme owns.

## 3. Transparency `[THEOREM T2]`

The Pöschl–Teller operator is reflectionless iff Λ = ℓ(ℓ+1), ℓ ∈ ℤ⁺, with exactly
ℓ bound states (R5: |R|² drops to machine zero precisely at Λ = 2, 6, 12).
Combining with T1:

$$\boxed{\;\text{transparency}\;\Longleftrightarrow\; c\,\chi_\perp = \ell(\ell+1)\;}$$

An **integrality condition on the stiffness alone**, with zero cosmological
input, containing no ϱ⊥. This is the precise form of the V₀/α² = χ⊥ observation.

ℓ = 1 is the case to want: Λ = 2, exactly one bound state — a single normalisable
mode localised at the crossing, no continuum instability. Preregistered success
criterion 7 ("no independent dark-energy clustering mode or unstable crossing")
is currently slated to be met by PPF, which cannot fail it because PPF has no
dynamics. Transparency would replace an unfalsifiable pass with a theorem. And
ℓ = 1 = rank one: the chain closes.

`[CONJECTURE C1]` The pair-completed dark perturbation operator is reflectionless
with ℓ = 1, i.e. c·χ⊥ = 2.

## 4. `[NEGATIVE N1]` The growth operator fails T1's hypothesis

Under ψ = D·a·√H the growth equation reduces to ψ″ = W(N)ψ with
W = ¼(2+h)² + ½h′ + (3/2)Ω_m(N), h = dlnH/dN. Against the CMB-distance-matched
ΛCDM comparator (R6):

- ΔW/Ω_X(N) spans **−179 to +0.27**. Under T1 it would be constant.
- A free three-parameter sech² fit gives **63.9% fractional RMS residual** and
  recovers ϱ⊥_fit = 5.3 against an input of 1.0.
- The offender is the (2+h)²/4 term, dominated by the matter sector.

**Diagnosis.** The growth equation is a *zero-energy* problem in N — no spectral
parameter, no reflection channel, no transparency concept. Transparency must live
in the dark-sector operator, which needs the pair completion. **C1 cannot be
tested until Q1 is answered.** This fixes the order of work.

## 5. `[NEGATIVE N2]` The single-field no-go, quantified

For a single-field completion, z² ∝ (1+w_X) = (2ϱ⊥/3)tanh θ (R7):

**(a) Ghost, not defect.** 1+w_X < 0 for *all* θ < 0 — the entire pre-crossing
era. Wrong-sign kinetic term over a cosmological epoch, not at a point. Any
narrative treating the crossing as a removable singularity mis-states the
pathology.

**(b) Critically marginal.** Near θ = 0, z ∼ |θ|^{1/2}, so z″/z → −1/(4θ²)
(verified to ratio 1.0008 at θ = 10⁻⁵). The inverse-square potential −g/x² has
critical coupling g = 1/4. **The crossing sits exactly at the critical coupling** —
not merely unstable, the marginal case, which is why no small deformation of a
single-field model rescues it.

`[DEDUCTION]` The completion must be non-single-field. This independently
motivates rank ≥ 2 — the same rank that generates sech². **Q1 asks whether these
are the same two.**

## 6. The A₂ fold in the phase plane `[THEOREM T7]`

Eliminating θ from the invariant with X := 1+w, Y = X′:

$$X' = A - BX^2, \qquad A = \tfrac23\varrho_\perp^2,\quad B = \tfrac32$$

the **canonical saddle-node (fold, A₂) normal form**. Rescaling X = (2ϱ⊥/3)û,
τ = ϱ⊥N gives exactly dû/dτ = 1 − û² (R3, residual 8.9 × 10⁻⁹).

- **B = 3/2 is fixed by gravity** (the 3 in 3(1+w)); not adjustable.
- **A = (2/3)ϱ⊥² is the unfolding parameter.**
- Fixed points X = ±(2/3)ϱ⊥, i.e. w_± = −1 ± (2/3)ϱ⊥; the history is the
  **heteroclinic orbit** between them.
- **ϱ⊥ = 0 is the fold**: fixed points merge and annihilate, ρ_X ≡ 0.

`[DEDUCTION]` "Exactly one density maximum, exactly one w = −1 crossing, one
connected acceleration interval" are not three predictions. They are the single
statement that a 1-D flow with two hyperbolic fixed points has one heteroclinic
orbit. The rigidity *is* the structural stability of the saddle-node normal form.

## 7. ϱ⊥ = 1 and the acceleration separatrix `[THEOREM T3]`

$$\boxed{\;\varrho_\perp = 1 \iff w_\infty = -\tfrac13 \iff q_\infty = 0 \iff a(t)\propto t\;}$$

In a dark-dominated future E ∼ e^{−sN}, s = (3/2)(1+w_∞), and ∫dN/(aH) ∼
∫e^{(s−1)N}dN converges iff w_∞ < −1/3 (R4):

| ϱ⊥ | future | event horizon |
|---|---|---|
| < 1 | eternal acceleration, de Sitter-like | **exists** |
| **= 1** | **marginal, coasting a ∝ t** | **marginally absent** |
| > 1 | deceleration resumes | absent |

`[SLOT]` A selection-principle candidate with physical content: ϱ⊥ = 1 is the
unique value at which the universe accelerates today yet has no asymptotic event
horizon, so asymptotic observables exist. For an operator-algebraic programme,
the absence of a good late-time algebra in de Sitter is a real obstruction, and
ϱ⊥ = 1 is exactly the value that evades it. It also recovers the erratum's
horizon budget: q_∞ = 0 ⟹ μ_A = ½ ⟹ 50/50 equipartition.

`[CONJECTURE C2]` ϱ⊥ = 1 is selected by asymptotic equipartition of the horizon
e-fold budget, equivalently by well-definedness of the late-time causal algebra.

## 8. The second fold: an existence ceiling `[THEOREM T4]`

Flatness requires F(x) = T, where x := −N_c > 0, F(x) = r_c e^{3x}sech²(ϱ⊥x),
T := (1−Ω_m−Ω_r)/Ω_m. Since dlnF/dx = 3 − 2ϱ⊥tanh(ϱ⊥x):

- **ϱ⊥ ≤ 3/2**: F strictly increasing ⟹ **unique** root always exists.
- **ϱ⊥ > 3/2**: F rises then decays ⟹ **two roots or none**.

The double root gives a closed-form ceiling:

$$\boxed{\;\frac{T}{r_c} = \left(1 - \frac{9}{4\varrho_\perp^2}\right)\exp\left[\frac{3}{\varrho_\perp}\operatorname{artanh}\frac{3}{2\varrho_\perp}\right], \qquad \varrho_\perp > \tfrac32\;}$$

At Ω_m = 0.310598, r_c = 1: **ϱ⊥^max = 1.814123**, roots merging at
N_c = −0.649394 (z_c = 0.914). R8 verifies; R12 gives the r_c scaling (T10).

This is a **second A₂ fold** — T7's lives in the dynamical phase plane, T4's in
the *moduli of solutions*: two admissible crossing epochs merge and annihilate.

**It explains both anomalous determinations.** Applying the estimator
ϱ⊥² = [9(1+w₀)² − 6w_a]/4 (R9):

| source | ϱ⊥ |
|---|---|
| DESI DR2 + CMB + Pantheon+ | **0.995 ± 0.173** |
| DESI DR2 + CMB, no SN | **1.839 ± 0.376** |
| ceiling at r_c = 1 | **1.814** |
| addendum, r_c freed | **1.7 – 1.8** |

`[DEDUCTION]` Both anomalies are boundary-dominated. The correct statement is
*the no-SN determination is uninformative*, leaving the table with **one** usable
entry. Two points, one at a boundary, is not clustering. ϱ⊥ = 1 sits at 0.551 of
the ceiling and is **not** saturating — T3, not T4, is the live selection
principle.

## 9. How the theorems fold together

```
                    [POSTULATE] rank one / binariness
                                 |
                    +------------+------------+
                    |                         |
              Var(Q)=sech^2 θ            <Q^2> = 1
                    |                         |
        X_σ = ϱ⊥² sech²[ϱ⊥(N-N_c)]     9(1+w)²+6w' = 4ϱ⊥²   [T6]
                    |                         |
        +-----------+-----------+             v
        |                       |        X' = A - BX²        [T7]
   X_σ dN² = sech²θ dθ²   ρ_X = χ⊥ X_σ   A=(2/3)ϱ⊥², B=3/2
   (ϱ⊥-FREE)                    |             |
        |                       |             +--> fold at ϱ⊥ = 0
        v                       v             |
   ∫v_B dN = π  [T5]     ψ_θθ+[K²/ϱ⊥²         +--> w_± = -1 ± (2/3)ϱ⊥
   = simplex diameter      + cχ⊥ sech²θ]ψ=0   |
                                  [T1]        v
                                   |     ϱ⊥=1 <=> q_∞=0 <=> a∝t   [T3]
                          two slots:      <=> no event horizon
                          ϱ⊥ -> eigenvalue    <=> 50/50 horizon budget
                          χ⊥ -> strength
                                   |
                                   v
                          cχ⊥ = ℓ(ℓ+1)  [T2]
                          ℓ=1 <=> one bound state
                          <=> criterion 7 DERIVED
                                   |
                                   X  blocked by N1
                                   X  needs pair completion (Q1)

  [POSTULATE] r_c  +  flatness ---> ϱ⊥ ≤ ϱ⊥^max(r_c)   [T4, T10]
       |                              (second fold, moduli)
       +--> r_c = 1 <=> equality epoch = susceptibility peak   [T8]
       +--> invariant is r_c-blind ==> separability            [T9]
```

One postulate (rank one) plus one soldering law generates the entire left branch;
the right branch follows from the invariant alone, which is just Q² = 1. The costs
are concentrated in exactly two places: **rank one**, and **r_c**.

---

# Part II — The r_c problem

## 10. What r_c means, exactly `[THEOREM T8]`

r_c := ρ_*/ρ_m(N_c), i.e. χ⊥ϱ⊥² = r_c·ρ_m(N_c). The ratio is

$$\frac{\rho_X}{\rho_m} = r_c \operatorname{sech}^2\theta\, e^{3\theta/\varrho_\perp}, \qquad \frac{d}{d\theta}\ln\frac{\rho_X}{\rho_m} = -2\tanh\theta + \frac{3}{\varrho_\perp} > 0$$

for ϱ⊥ < 3/2. Strictly monotone ⟹ matter–dark equality is **unique**, and at
θ = 0 the ratio equals r_c exactly. Therefore:

> **r_c = 1 ⟺ matter–dark equality occurs exactly at the susceptibility peak —
> which is exactly where w_X = −1.**

Three epochs, two identified by fiat (R10):

| epoch | z |
|---|---|
| susceptibility peak / w_X = −1 crossing | 0.34202 |
| matter–dark equality | 0.34202 ← *identified by r_c = 1* |
| acceleration onset (q = 0) | 0.78579 ← *derived output* |

**The identification is nontrivial.** At the DESI CPL best fit the two epochs
separate: w = −1 at z = 0.3537, equality at z = 0.3351, Δz = 0.019. Generic dark
energy does not put them together. So r_c = 1 is a falsifiable coincidence claim
about two independently measurable redshifts, not a convention.

## 11. The good news `[THEOREM T9]`

**The shape invariant is blind to r_c.** Since w_X depends only on θ (R11):

| r_c | z_c | w₀ | w_a | 9(1+w₀)²−6w_a |
|---|---|---|---|---|
| 0.5 | 0.851 | −0.634 | −0.466 | **4.000000** |
| 1.0 | 0.342 | −0.809 | −0.612 | **4.000000** |
| 2.0 | 0.036 | −0.977 | −0.666 | **4.000000** |
| 3.0 | −0.093 | −1.065 | −0.660 | **4.000000** |

Distances can trade r_c against ϱ⊥ freely — that is the addendum's degeneracy,
and R12 confirms the direction (ϱ⊥^max = 1.648 at r_c = 0.8, 1.814 at 1.0, 2.481
at 1.5, so a fit that frees r_c and drifts to 1.7–1.8 is moving *along* the
degeneracy toward a **moving** boundary). But the invariant cannot be traded.

> **Measure ϱ⊥ from the shape invariant; then measure r_c from the residual
> amplitude.** The degeneracy is a *data* degeneracy, not a structural one, and
> P1 breaks it. This requires no new theory and can be done this week.

## 12. Why it is structurally hard

χ⊥ has dimensions of energy density — the only new dimensionful object in the
theory. r_c = 1 sets it equal to ρ_m at a particular epoch. A constant equal to a
contingent, epoch-dependent quantity is one of three things:

1. **A coincidence** — fine-tuning; the failure mode.
2. **χ⊥ is not fundamental** — dynamically driven to that value. This is the
   tracker-quintessence playbook (Zlatev–Wang–Steinhardt 1999 turned "why now"
   into an attractor). Requires promoting χ⊥ or ω_c to dynamical, which changes
   the theory. Hold in reserve.
3. **N_c is not contingent** — the reference state ω_c is canonically selected,
   and r_c = 1 follows.

Route 3 is the one, and it is further along than the corpus currently reflects.

## 13. The literature route: your own reference [3]

Chatterjee, arXiv:2605.19106, cited in the erratum but not yet exploited.

> Modular self-duality singles out parameter values at which a state coincides
> with its modularly reflected partner. The natural comparison functional near
> that locus is the symmetrized Umegaki relative entropy; it vanishes at
> coincidence, differentiability forces its first variation to vanish, and its
> Hessian is governed by the BKM quantum Fisher information along the reflected
> tangent direction — identifying a canonical BKM susceptibility selected by
> modular structure.

Your family has JQJ = −Q, so the modular reflection of ρ_θ is ρ_{−θ}, and **the
self-dual fixed point is exactly θ = 0.** That is N_c. It is not a choice; it is
the critical point of a functional, with the first variation vanishing for
differentiability reasons alone.

The payoff: Chatterjee extends the construction to local type III algebras, where
the fixed-localization Hessian at the self-dual point defines a type III BKM
susceptibility, with exact coherent-state realizations for the free scalar on
wedge algebras and the chiral U(1) current on half-line algebras — and the
susceptibility coefficients admit **explicit boost-energy, stress-tensor, or
half-line integral representations**.

Those coefficients are χ⊥, computed rather than fitted, in two solvable cases.

**The programme is therefore concrete:** construct the analogue for the FLRW
causal diamond, read χ⊥ off the stress-tensor representation, and check whether
χ⊥ϱ⊥² = ρ_m at the self-dual point. That converts r_c = 1 from `[POSTULATE]` to
**prediction** — and it may come out false, which is exactly what you want from
it.

## 14. Three theorems claimable immediately

**Petz (1996), monotone metrics on matrix spaces.** All monotone Riemannian
metrics on density matrices are classified by operator-monotone f with f(1) = 1
and f(t) = t f(1/t). Consequence: **the BKM metric carries no free
normalisation.** Once f(1) = 1, G^BKM = Var(Q) exactly. Every scrap of
normalisation ambiguity in the theory sits in χ⊥ and nowhere else. Put this in the
master doc — it shortens the assumption ledger visibly.

**Chentsov (1982).** The Fisher metric is unique up to a *global* scale under
sufficient-statistic invariance. Consequence: **χ⊥ = constant is a theorem, not an
assumption.** It cannot be a function of N. Currently assumed; promote it.

**Amari–Nagaoka.** BKM/Fisher is the unique monotone metric admitting a dually
flat structure. This is what makes §2.4's e/m dual-coordinate table a theorem
rather than a coincidence of hyperbolic identities. Cite it there.

**Supporting templates for fixing χ⊥:** Jacobson (1995, gr-qc/9504004) fixes the
coupling by demanding the Clausius relation on all local Rindler horizons;
Jacobson (2015, 1505.04753) by δS_total = 0 in small causal diamonds;
Lashkari–Van Raamsdonk (1508.00897) show canonical energy **equals** quantum
Fisher information with no free coefficient. That last is the closest structural
precedent to ρ_X = χ⊥𝒳_σ. Note also what r_c = 1 looks like in that language: at
the J-fixed point, where ⟨Q⟩ = 0 and the grade has no preferred direction, the
first law reduces to a *balance* between susceptibility and matter terms.
ρ_X = ρ_m at θ = 0 is structurally an entanglement-equilibrium condition.

## 15. Consolidation, and two warnings

**Q3 (r_c) is not independent of Q5 (Γ_MW).** Constructing Γ_MW the Jacobson way
fixes χ⊥ automatically, and r_c = 1 either falls out or does not. Two open
problems collapse to one, and it is one you already knew you needed. Say so
explicitly in the master doc; it shortens the ledger honestly.

**Warning 1.** r_c = 1 does **not** solve the coincidence problem. It relocates it
into "why Ω_m ≈ 0.31," since flatness plus r_c = 1 is what puts z_c near today.
Do not let the master doc claim otherwise.

**Warning 2.** The self-duality route may return χ⊥ϱ⊥² ≠ ρ_m(N_c), in which case
the zero-new-dimensionful-constants claim collapses and the theory acquires a
genuine free parameter — putting it level with Λ_sCDM rather than ahead of it.
That is the real stake, and it should be stated in the master doc *before* the
result is known.

---

# Part III — The A₂ ledger

The three connections in the circulated notes are **genericity results** and
should be demoted:

| claim | verdict |
|---|---|
| turning points merge at the bottom of a sech² well → A₂ | `[RHYME]` — true of every smooth Morse minimum, including the harmonic oscillator |
| wave-breaking caustics of sech² solitons are A₂/A₃ | `[RHYME]` — Whitney: generic planar maps have only folds and cusps, for essentially all initial data |
| Airy asymptotics near the turning point | `[RHYME]` — universal for any V with V′(x_t) ≠ 0; sech² contributes nothing |

Minor correction: sech² is the **KdV** soliton; mKdV's is sech.

**Hazard.** sech² is one of the most over-determined functions in mathematics
(KdV soliton, Pöschl–Teller, logistic derivative, BCS gap, kink energy density,
∂tanh), and ADE classifications are pervasive enough that "my object is A₂" is
nearly always findable on a hard enough look. This is the epicycle failure mode
in pure-mathematical clothing: not free parameters but **free correspondences**.
Same discipline: does the identification produce consequences the bare structure
lacked?

**What survives as theorem:** two genuine A₂ folds, T7 (dynamical, ϱ⊥ = 0) and T4
(moduli, ϱ⊥ = ϱ⊥^max). Neither was found by pattern-matching; both fell out of the
equations.

**Do not conflate three A₂'s.** Catastrophe A₂ (x³ + ax), surface singularity A₂
(x³ + y² = 0), and Dynkin A₂ (SU(3)) are linked by the simple-singularity/McKay
correspondence — a theorem with hypotheses, not a free identification. T4 and T7
are *catastrophe* A₂.

**The honest weld target.** What is special about sech² is not that it instances
A₂ but that it is the **anti**-A₂: reflectionless potentials have *trivial*
continuum scattering data where generic potentials have A₂ caustics and
nontrivial connection matrices. That inversion is the Keller move:

| | local defect | obstruction lives at |
|---|---|---|
| **Keller map** | det *JF* ≡ 1: no critical points, no folds permitted | infinity / nonproperness / monodromy |
| **reflectionless sech²** | no reflection at any energy | discrete spectrum |
| **rigid pulse** | ρ_X > 0 everywhere, smooth | comparison to the wrong basis |

*An object forbidden from carrying a local defect, whose obstruction survives
globally.* Descent-with-remainder in three presentations — and "trivial local
invariant, nontrivial global one" is the setup for a monodromy or sheaf-
cohomological statement, not an analogy.

`[SLOT] Q2.` Reflectionless potentials are exactly those whose KdV spectral curve
is rational (genus-0, branch points collided). Keller obstructions live in
branched-cover data of a discriminant. **Is the spectral curve of the ℓ = 1
Pöschl–Teller operator the Keller spectral curve at the A₂ degeneration?**
Checkable. Until checked, the Keller–pulse link stays `[RHYME]`.

---

# Part IV — Predictions and kill conditions

Ω_m = 0.310598, ϱ⊥ = 1, r_c = 1, Λ_res = 0, k = 0.

**P1 — The invariant, bin by bin.** `[strongest test; run it first]`
9(1+w(z))² + 6 dw/dN = 4ϱ⊥² = 4 at every z. A differential relation, not a
number: every reconstructed bin tests the same relation. This is what "structure
is content" cashes out to. Testable now against non-parametric w(z)
reconstructions. **By T9 it also fixes ϱ⊥ independently of r_c.**
**K1:** dies if the reconstructed combination varies with z beyond errors.

**P2 — Zero-parameter (w₀, w_a).** (−0.80935, −0.61215) against (−0.838 ± 0.055,
−0.62 ± 0.20): 0.53σ and 0.04σ.
**K2:** dies on a clean determination outside [0, ϱ⊥^max] at that analysis's Ω_m
and r_c.

**P3 — Crossover epoch.** z_c = 0.34202, rigidly tied to Ω_m by flatness.
**K3:** dies if BAO/SN require a crossover displaced from the flatness value.

**P4 — The equality coincidence.** `[new, T8]` z(w = −1) = z(ρ_X = ρ_m) = 0.342.
Two independently measurable redshifts, separated by Δz ≈ 0.019 in the CPL best
fit. **This is the direct observational test of r_c = 1.**
**K4:** dies if the reconstructed w = −1 crossing and the equality epoch separate
beyond errors.

**P5 — The ceiling.** ϱ⊥ ≤ ϱ⊥^max(r_c), closed form in §8.
**K5:** a clean, non-boundary-dominated determination above the ceiling
falsifies the branch. A real kill: the theory forbids a region data could occupy.

**P6 — The future.** w_∞ = −1/3 exactly, a ∝ t, no event horizon, asymptotic
50/50 horizon budget. A sharp fork against the erratum's strong-identification
branch (w_∞ = −5/9, permanent acceleration, a ∝ t^{3/2}).

**P7 — Transparency.** If C1 holds, modes crossing the pulse acquire a pure phase
shift; the dark sector has exactly one bound mode; no independent clustering mode.
**K6:** dies if the pair-completed operator gives c·χ⊥ ∉ {2, 6, 12, …}.

**Explicitly not a prediction.** The CMB-lensing anti-alignment. The addendum's
null-ensemble audit — 225 smooth transient histories, 92.9% with cos < −0.90,
median −0.969 against the pulse's −0.972 — independently confirms the earlier
null control. It is a **class membership test**, passed, with no discriminating
power. Report as a necessary condition; never as evidence.

---

# Part V — Presentation guide for the master document

## 16. Diagnosis: what is currently costing the programme

Read across the four documents, six patterns recur. Each is fixable.

1. **The weakest claim leads.** The neutrino result headlines two documents. It
   is degenerate (Λ_sCDM, IDE, and a hierarchy-informed prior all remove it),
   importance-sampled at k̂ = 0.91, and boundary-dependent. Meanwhile T1 and the
   dually-flat retyping — the strongest things here — are never foregrounded.
2. **Discovery order, not dependency order.** Results appear as they were found,
   so each reads as a separate assumption rather than a consequence. §9's map is
   the true order.
3. **Rhetorical escalation.** "Mercury," "materially," "extraordinarily
   compressed," "conceptually gorgeous," "genuine retyping of gravity." The
   morgue exists because of this failure mode.
4. **Overprecision.** 0.07747 eV at N_eff = 332; 0.6599; +2.078%; +0.157%. The
   erratum tells the reader one significant digit and the appendix then prints
   five. Confidence-by-decimal-place.
5. **Negatives buried.** N1, N2, the Pareto tail, the null-ensemble audit — the
   credibility engine — sit in appendices and caveat sections.
6. **Structural claims without their null.** The two-lobed signature (forced by
   the distance-matching integral) and the lensing cosine (matched by 93% of
   random transient histories) were both presented as results.

## 17. Ten presentation rules

**R1. Lead with the grammar, not the cosmology.** Open on T1 and §2.4. A referee
who meets the neutrino result first reads everything after as motivated
reasoning; one who meets the slot separation first does not.

**R2. Present in dependency order.** T6 → T7 → T3 → T4 → T1 → T2 → T8/T9. This
reads as one argument rather than nine results, and it makes visible how little
is independently assumed.

**R3. Every structural claim carries its null control in the same sentence.**
Not "cos α = −0.97, strongly anti-aligned" but "cos α = −0.97, against −0.97 for
a featureless boost and a −0.969 median across 225 random transient histories."
Make this a standing rule with a reusable script.

**R4. One baseline per document, declared in the status block.** The
0.0341 ≈ 0.0317 error was a ΛCDM-baselined number compared to a CPL-baselined
one. The rule prevents recurrence structurally.

**R5. Significant figures capped by the diagnostic.** With k̂ = 0.91 and
N_eff = 332, report 0.077 eV and 66 ± 3%. Never let the appendix print more
digits than the body permits.

**R6. Negatives in the body, numbered like theorems.** N1 and N2 as first-class
results with their own labels. A document with three numbered negatives in the
main text is far more credible than one with nine positives.

**R7. Taxonomy labels mandatory, including in summary tables.** The Direct CMB
document has none. Every boxed equation and every table row gets a label.

**R8. Register declaration for temporal and causal language.** ϱ⊥ is a derivative
with respect to *scale*. "Velocity of becoming" is a wall-level phrase attached to
a block-level object. Retire it as the headline; keep v_B = ds_BKM/dN as the
technical object and ϱ⊥ = max_N v_B as its invariant characterisation.

**R9. State the strongest claim you can *defend*, not the strongest that is
true-ish.** "50%–85% of the lensing direction" is inflated at the top end by
weightings no experiment uses; mode-count weighting gives 50–65%. Lead with the
defensible number and relegate the rest to a sensitivity row.

**R10. Every constant gets a determination *table*, not a determination.** One
entry is not evidence. Mark boundary-dominated entries as such. This is the Eötvös
standard, and it is the only thing that will make ϱ⊥ = 1 credible.

## 18. Proposed master-document outline

```
0.  Status, epistemic taxonomy, ONE declared baseline
1.  The claim in one page: gravity retyped as the Legendre Jacobian
    of a dually flat modular geometry.  §2.4 table. No cosmology yet.
2.  The postulate ledger, up front: rank one, soldering, constitutive
    law, r_c.  Four items.  What each buys, what each costs.
3.  From rank one to sech^2                             [T6, one line]
4.  The invariant and its consequences                  [T6 -> T7 -> T3]
      the A2 normal form; one crossing; the future; the separatrix
5.  The two constants                                   [T1]
      slot separation; the c/G grammar; Petz, Chentsov, Amari-Nagaoka
6.  Transparency and the perturbation sector            [T2, N1, N2]
      what it would derive; what blocks it; the no-go quantified
7.  Normalisation                                       [T8, T9, T10]
      what r_c means; the equality coincidence; separability;
      the Chatterjee self-duality route; the ceiling
8.  Predictions and kill conditions                     [P1-P7, K1-K6]
      invariant test first; determination table; null controls inline
9.  Cosmological application                            <- LAST, not first
      the neutrino result at its correct weight: a proposal-level
      signal, k-hat = 0.91, driven by BAO geometry, downgraded
10. Morgue: withdrawn claims with causes of death
11. Open problems Q1-Q5, with the Q3 c Q5 consolidation
```

The single most important structural change is moving cosmology from §1 to §9.

## 19. Sentences to retire, and their replacements

| retire | use |
|---|---|
| "The Neutrino Mercury Test" | "A structural test of the rigid branch against the DESI neutrino residual" |
| "The answer is yes, materially." | "Necessary condition met; the null control shows it is not discriminating." |
| "This is the strongest result of the calculation." (two-lobed signature) | "The sign change is forced by the distance-matching constraint. The content is the crossing redshift and the amplitudes." |
| "Correct spectral direction." | "Residual tilt mismatch: a discriminating prediction." |
| "roughly 50%–85% of the CMB-lensing direction" | "50–65% under mode-count weighting; higher only under weightings no experiment uses" |
| "conceptually gorgeous" | *(delete; let the equation carry it)* |
| "It would be a genuine retyping of gravity." | "If Γ_MW exists with Φ*G^BKM as pullback metric, the dark sector is the Legendre Jacobian of a dually flat geometry rather than a fluid." |
| "materially raises the prior probability that such a run will improve rather than destroy the result" | "Predicted shift for the Boltzmann run: [state the number in advance]." |
| "velocity of becoming" *(as headline)* | "the dark-energy episode is exactly one e-fold wide, and is a complete traversal of the space of two-state distinctions — total Fisher length π" |
| "extraordinarily compressed" | "zero extra shape parameters and zero new dimensionful constants — conditional on r_c = 1" |

## 20. Figures and tables the master document needs

1. **The dually flat diagram.** θ ↔ N and η ↔ (1+w) with the Legendre pairing and
   ρ_X as the Jacobian. This is the paper's thesis in one picture and does not
   exist yet.
2. **The (X, X′) phase portrait** with both fixed points, the heteroclinic orbit,
   and the fold at ϱ⊥ = 0. Makes "one crossing, one acceleration episode" visibly
   a theorem.
3. **The ϱ⊥–r_c plane** with the ceiling curve ϱ⊥^max(r_c), the distance
   degeneracy direction, and contours of the invariant crossing it transversally.
   One figure showing both the degeneracy and how P1 breaks it.
4. **The determination table** for ϱ⊥, with the ceiling marked and boundary-
   dominated entries flagged. Currently one usable row; that is the honest state.
5. **The Fisher-length picture.** The binary simplex as an arc of length π, with
   the cosmological history drawn as the complete traversal.
6. **The postulate ledger table**, front-loaded (§2 of the outline).

## 21. The claim ladder

State every claim at its level, and never in the grammar of a higher one.

| level | content | permitted grammar |
|---|---|---|
| **1. Proved** | T1–T10, N1, N2 | "is", "follows", "exactly" |
| **2. Conditional** | T2 given the pair completion; the transparency route | "if … then"; hypothesis named in the same sentence |
| **3. Conjectured** | C1, C2, C3; the self-duality route to r_c | "would", "is a candidate", "target" |
| **4. Not established** | the neutrino result as a resolution; the Keller link; the microscopic interpretation | "proposal-level signal"; `[RHYME]`; explicit non-claim |

The characteristic failure across the corpus is level-3 content in level-1
grammar. A single pass enforcing this table would do more for the master
document's reception than any new calculation.

---

# Part VI — Open problems and work order

- **Q1.** Is the rank-two structure required for sech² the same rank-two structure
  required by the crossing no-go? Construct the pair-completed dark perturbation
  operator. *Blocks C1, P7, criterion 7.*
- **Q2.** Is the ℓ = 1 Pöschl–Teller spectral curve the Keller spectral curve at
  the A₂ degeneration? *Would weld the two tracks.*
- **Q3 ⊂ Q5.** Derive r_c via the Chatterjee self-dual point: build the FLRW
  causal-diamond analogue of the wedge/half-line cases and read χ⊥ from the
  stress-tensor representation.
- **Q4.** Prove or refute C2: is ϱ⊥ = 1 selected by asymptotic equipartition of
  the horizon budget / well-definedness of the late-time causal algebra?
- **Q5.** Construct Γ_MW with Φ*G^BKM as pullback metric, δ_gΓ_MW = T^X_ab,
  δ²_gΓ_MW = a stable perturbation kernel. Solving this solves Q3.

**Order:**

1. **P1 on w(z) reconstructions.** Cheapest, sharpest, breaks the r_c–ϱ⊥
   degeneracy by T9, requires no new theory. Do this first.
2. **P4, the equality coincidence.** Direct observational test of r_c = 1 from
   quantities already reconstructed for P1.
3. **The determination table (R10).** ϱ⊥² = [9(1+w₀)² − 6w_a]/4 with real
   covariances across DR1/DR2 × {Pantheon+, Union3, DES-Y5, DES-Dovekie} ×
   {with, without lensing}, each marked against the ceiling at its own Ω_m and r_c.
4. **Q1.** Theory work, no data. Everything downstream is blocked on it by N1.
5. **Q3 ⊂ Q5** via Chatterjee §III–IV.
6. **Q2.** High variance, high payoff, no data needed.
7. **The master document**, per Part V.

---

## Appendix — Receipt index

All in `receipts_transparency_fold.py`; no external data required.

| receipt | verifies |
|---|---|
| R1 | binary moments, Var(Q) = sech²θ, ⟨Q²⟩ = 1, Fisher length π = simplex diameter (T5, T6) |
| R2 | invariant = 4ϱ⊥² exactly, ϱ⊥ ∈ [0.6, 1.5] (T6) |
| R3 | A₂ saddle-node normal form, residual 8.9e-9, fold at ϱ⊥ = 0 (T7) |
| R4 | future attractor, q_∞, event-horizon convergence (T3) |
| R5 | θ-frame reduction; exact PT transmission → reflectionless at Λ = ℓ(ℓ+1) (T1, T2) |
| R6 | **[NEGATIVE]** growth operator not PT: 63.9% residual, ratio spans 2 decades (N1) |
| R7 | **[NEGATIVE]** single-field ghost + z″/z → −1/(4θ²) critical coupling (N2) |
| R8 | existence ceiling, closed form, ϱ⊥^max = 1.814123 (T4) |
| R9 | ϱ⊥ → (z_c, w₀, w_a) map and the inverse estimator on published fits |
| R10 | r_c as a three-epoch identification; nontriviality vs CPL (T8) |
| R11 | invariant blind to r_c; the degeneracy and its breaking (T9) |
| R12 | ceiling scaling with r_c (T10) |
