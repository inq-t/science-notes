# The Convergence

## Reclassification of the modular–Weyl open problems, and the single remaining gap

**Thomas Ruble research programme — AI-assisted technical hand-off**
**21 August 2026**

**Companion documents.** `transparency_binariness_and_the_fold.md` (results T1–T14,
negatives N1–N3, presentation guide) and `receipts_transparency_fold.py` (R1–R19,
no external data). This document does not repeat those results; it reports what
happened to the *open problems* when they were probed, and states what is left.

---

## 0. Thesis

Five open problems were probed. Four of them either closed, were absorbed, or
turned out to be the same problem wearing different clothes. What remains is

> **one dimensionless coefficient, and one physical identification that
> determines it.**

The programme has, in the process, separated cleanly into **two rigid
formalisms joined by a single screw**. The vertical/geometric sector is now
entirely conformal tractor calculus, exact and with no free normalisation. The
horizontal/state sector is now entirely information geometry of a rank-one
exponential family, exact and — by Petz and Chentsov — with no free
normalisation either. Everything that was free has been squeezed into the one
coefficient that joins them.

That is why solving it should simplify the framework rather than complicate it,
and §6 makes that precise.

**One caution up front, because it is load-bearing.** The convergence is
*conditional*. It rests on a hypothesis (§7.1) that has already been falsified
for one candidate operator. If it fails again, the convergence unwinds and r_c
returns to being an independent postulate.

---

## 1. What was probed, and what came back

Compressed; full derivations and receipts are in the companion document.

### 1.1 The Chatterjee self-duality calculation (R13–R15)

Run against arXiv:2605.19106. The binary family satisfies the hypotheses
exactly: JQJ = −Q gives ρ_J(θ) = ρ_{−θ}, so the parameter involution is
r(θ) = −θ with fixed point θ = 0. The symmetrized Umegaki relative entropy has
the closed form 𝔖_J = 4θ tanh θ, and Chatterjee's Eqs. (35)–(37) all check:
𝔖_J(0) = 0, first variation vanishes, I_J(0) = 8 = 2γ^BKM(ΔX, ΔX) with the
reflected tangent ΔX = 2X_*.

**Two things came back.**

- **N_c left the postulate ledger.** 𝔖_J ≥ 0 vanishes only at θ = 0 and is
  strictly increasing in |θ|, so the self-dual point is the *unique global
  minimum* of an intrinsic modular functional. N_c is variational, not chosen.
- **An arrow came out unasked.** 𝔖_J = 6(N − N_c)(1 + w_X), ϱ⊥-free, and
  non-negativity of relative entropy then forces w < −1 before the crossing and
  w > −1 after. The phantom → quintessence direction is a theorem.

Blocked at: the dimensional bridge to χ⊥, which needs the FLRW causal-diamond
modular Hamiltonian **and** the physical identification of Q. The second is
upstream of the first.

### 1.2 The r_c interrogation (R10–R12)

r_c = 1 was shown to be a **three-epoch identification**: matter–dark equality
coincides with the susceptibility peak, which is the w_X = −1 crossing. The
acceleration onset (z = 0.786) is a derived output, not identified. In the DESI
CPL best fit the first two epochs separate by Δz = 0.019, so the identification
is a falsifiable coincidence claim, not a convention.

**The useful finding**: the shape invariant is **blind to r_c** — 9(1+w)² + 6w′
= 4ϱ⊥² for every r_c. So ϱ⊥ and r_c are separately measurable, and the observed
degeneracy is a *data* degeneracy, breakable by P1 with no new theory.

Three theorems became claimable from the literature: **Petz (1996)** — monotone
metrics are classified with f(1) = 1, so G^BKM carries no free normalisation and
every scrap of ambiguity sits in χ⊥; **Chentsov (1982)** — the Fisher metric is
unique up to a *global* scale, so χ⊥ = const is a theorem, not an assumption;
**Amari–Nagaoka** — BKM is the unique monotone metric admitting a dually flat
structure, which is what makes the e/m dual-coordinate table a theorem rather
than a coincidence of hyperbolic identities.

### 1.3 The tractor calculation (R16–R17)

FLRW is conformally flat — Weyl vanishes identically for every k and every
a(η) — so **conformal geometry sees nothing in a cosmology and all content is
scale data.** "Spatial flatness" is a scale-frame choice, not a geometric fact.
Taking the conformal structure flat gives σ = 1/a, σ′ = −H, σ″ = −aḢ, and

$$I\cdot I = -\left(H^2 + \tfrac{\dot H}{2}\right) = -\frac{R}{12} = -\mu_A H^2 = \frac{2\pi G}{3}\,T$$

verified three ways to 1e-8 and against the "almost-Einstein-matter scale
tractor" of arXiv:2208.09302 eq. (3.20), which gives I·I = −R/(n(n−1)).

Three readings, all exact:

- **The vertical horizon clock rate *is* the normalised tractor norm.** The
  allocation law becomes 1 = −I·I/H² + ¼(ln 𝒮_A)′.
- **The tractor norm *is* the Weyl/dilatation anomaly charge**, since
  I·I ∝ T = −ρ + 3p. So I·I = 0 ⟺ T = 0 ⟺ w = 1/3 ⟺ conformal invariance ⟺ null
  tractor ⟺ the AdS/dS separatrix. All one statement.
- **ϱ⊥ = 1 ⟹ I·I/H² → −1/2**, exactly halfway between the null tractor
  (Minkowski, 0) and de Sitter (−1).

**And a negative that mattered (N3).** Φ\*G^BKM ∝ I·I is *false* — the ratio
spans two decades. I·I is a norm built from σ, which is vertical; 𝒳_σ is
horizontal. The conjecture re-committed the exact conflation the v5.1 erratum
corrected. Worse: Weyl = Cotton = 0 for FLRW, so the tractor **connection** is
flat and its holonomy carries no horizontal data at all. **Tractors cannot
supply χ⊥.** The horizontal sector is genuinely extra structure, not hidden
geometry.

The repair (T14): ∇I is sourced by the trace-free stress, and
τ̊_ab = (ρ+p)[u_au_b + ¼g_ab], so τ̊ = 0 ⟺ ρ+p = 0. At the self-dual point
w_X = −1 exactly, so **the dark sector is entirely tractor-parallel and matter
is entirely tractor-source.**

### 1.4 The structural-balance test

The obvious next move was to read T14's 1:1 parallel/source balance as a
conservation law. It is not one, and the check is worth recording.

- **The split is canonical and forced.** Any perfect fluid decomposes uniquely
  into ρ_Λ = −p (parallel, no inertia) and ρ_d = ρ + p (the whole source). ρ+p
  is the **enthalpy**, i.e. the relativistic inertial density — literally the
  transport cost. The "cost/residue" reading is exact.
- **The balance is a restatement.** Because w_X(N_c) = −1 exactly,
  w_tot(N_c) = −r_c/(1+r_c) identically, so ρ_Λ/ρ_d|_{N_c} = r_c. The map is the
  identity. "1:1 balance at the self-dual point" and "r_c = 1" are the same
  sentence in two languages; proving one by unpacking proves nothing.
- **No conservation law.** ∫(ρ_Λ − ρ_d)dN is −843, −40, +0.05, −355631 on four
  natural ranges. And w_tot = −1/2 is a *level crossing*, occurring twice
  (N = −0.2938 and +0.4082) with the minimum of w_tot between them — not a fixed
  point, not an extremum.
- **And it cannot be made definitional.** Defining N_c by the balance discards
  T11. The coincidence of two independently defined epochs is precisely what
  gives r_c = 1 content, and precisely what forbids deriving it by unpacking.

What the tractor language *did* buy is a **retyping**: the postulate moved from
"amplitude equals matter density at an epoch" (an ugly dimensionful coincidence)
to "equipartition between two geometrically defined sectors." Better-shaped
target, same logical status.

### 1.5 The Levinson identity (R18–R19)

The ℓ = 1 reflectionless transmission amplitude is a single Blaschke factor,
t(k) = −(α−ik)/(α+ik), so arg t = π − 2 arctan(k/α). In log-momentum
s = ln(k/α):

$$\left|\frac{d(\arg t)}{ds}\right| = \operatorname{sech}(s), \qquad \int_{-\infty}^{\infty}\!\operatorname{sech}(s)\,ds = \pi$$

verified to 1e-11. That is Levinson's theorem with one bound state. And the
BKM/Fisher line element on the binary family is ds = sech(θ)dθ, total **π** —
the simplex diameter (T5). **Same function, same total, difference 0.00e+00.**

**And it is not a coincidence.** ∫sech(ax)e^{−ikx}dx = (π/a)sech(πk/2a), and at
a = √(π/2) this is an eigenfunction relation: **sech is Fourier
self-reciprocal**, one of the two classical self-reciprocal profiles alongside
the Gaussian. So the potential (= the BKM metric, sech²) and the phase density
(= the Fisher line element, sech) are position/momentum images of one another.
The matching π is self-duality of the profile.

**Directedness, rigorously.** The single pole of t(k) sits at k = +iα — the
upper half plane, i.e. retarded and causal. Because the potential is
reflectionless, that pole is the *entire* scattering content, so the arrow is
literally which half-plane it occupies; time reversal moves it to the lower
half-plane, which is acausal. This is an analytic-structure statement, not a
coarse-graining statement — and it **agrees with the independent entropy arrow
of T12.**

---

## 2. The reclassification

| | before | after |
|---|---|---|
| **Q1** — is the rank-two structure for sech² the same as the crossing no-go's pair structure? | one of five | **the sole gap.** Everything else feeds into it, and it now has a sharp operational form (§4) |
| **Q2** — Keller spectral curve ↔ ℓ=1 Pöschl–Teller at A₂ | speculative | still `[RHYME]`, but now with a **mechanism to test**: self-reciprocality is the "no local obstruction / nontrivial global remainder" statement. Demoted from load-bearing to targeted speculation |
| **Q3** — derive r_c = 1 | the load-bearing gap | **absorbed into Q1**, conditionally, via r_c = ℓ(ℓ+1)ϱ⊥²/(c ρ_m(N_c)). Not an independent problem |
| **Q4** — is ϱ⊥ = 1 selected? | open | **over-characterised**: four independent characterisations (§5). Still not derived from an action, but no longer looks arbitrary |
| **Q5** — construct Γ_MW | open | **split**. The vertical half is *done* — it is tractor calculus, exact (§1.3). The horizontal half needs exactly what Q1 needs (N3: tractors cannot supply χ⊥) |

Two items also **left** the ledger outright:

- **N_c** — derived (T11), the unique minimum of 𝔖_J.
- **The arrow** — derived twice, independently (T12 entropy positivity; R18 pole
  half-plane).

---

## 3. Two rigid formalisms, one screw

This is the structural picture that emerged, and it is the reason the
reclassification is not just bookkeeping.

**The vertical / geometric sector is conformal tractor calculus.** Exact,
closed, nothing free:

$$I\cdot I = -\frac{R}{12} = -\mu_A H^2 = \frac{2\pi G}{3}T, \qquad 1 = -\frac{I\cdot I}{H^2} + \tfrac14 (\ln\mathcal{S}_A)'$$

The horizon clock, the Weyl anomaly, the allocation law, and the AdS/dS
separatrix are one object. Nothing here is adjustable. And by N3, nothing here
reaches the horizontal sector.

**The horizontal / state sector is information geometry of a rank-one
exponential family.** Also exact, also nothing free:

$$G^{\rm BKM}_{\theta\theta} = \operatorname{Var}(Q) = \operatorname{sech}^2\theta, \quad \int \!ds_{\rm BKM} = \pi, \quad \mathfrak{S}_J = 4\theta\tanh\theta, \quad \langle Q\rangle^2 + \operatorname{Var}(Q) = 1$$

Petz forbids a normalisation freedom in the metric; Chentsov forbids the scale
from varying; Amari–Nagaoka fixes BKM as the unique dually flat choice.

**The join is one coefficient.**

$$\rho_X = \chi_\perp\, \mathcal{X}_\sigma$$

Every remaining freedom in the theory is in χ⊥. That is not a rhetorical claim —
it is what Petz plus Chentsov plus T1's slot separation *prove*.

---

## 4. The gap, stated precisely

Three equivalent statements of one question, in ascending operational sharpness.

**(A) Physical form.** *What two-state distinction does the binary grade Q
label?* The erratum's rank-one reduction is explicitly schematic. Nothing yet
says which physical dichotomy θ polarises.

**(B) Operator form.** *In the pair-completed linearised dark sector, does the
perturbation operator have a ρ_X-proportional potential — and if so, with what
coefficient c?*

$$\psi_{NN} + \big[K^2 + c\,\rho_X\big]\psi = 0 \;\;?$$

**(C) Numerical form.** By T1, any such operator reduces in the θ-frame to
Pöschl–Teller with strength Λ = cχ⊥, independent of ϱ⊥. Transparency (T2) then
requires cχ⊥ = ℓ(ℓ+1), and by definition r_c = χ⊥ϱ⊥²/ρ_m(N_c). Therefore

$$\boxed{\;r_c = \frac{\ell(\ell+1)\,\varrho_\perp^2}{c\,\rho_m(N_c)}\;}$$

and with ℓ = 1, ϱ⊥ = 1, ρ_m(N_c) = 0.750710 (units of ρ_crit,0), the claim
r_c = 1 is the **preregistered prediction**

$$\boxed{\;c\cdot\rho_m(N_c) = \ell(\ell+1)\,\varrho_\perp^2 = 2 \quad\Longrightarrow\quad c = 2.664146\;}$$

(A) → (B) → (C). They are the same question.

### What (C) closes, and what it independently checks

| closes | how |
|---|---|
| χ⊥ | χ⊥ = ℓ(ℓ+1)/c |
| r_c | r_c = χ⊥ϱ⊥²/ρ_m(N_c), computed not posited |
| criterion 7 ("no independent dark clustering mode") | derived from ℓ = 1 (one bound state), instead of passed by fiat under PPF |
| the perturbation sector | the operator is the thing being constructed |

| independently checks | how |
|---|---|
| χ⊥ again | knowing Q makes the Chatterjee type III stress-tensor representation computable, giving χ⊥ from modular data — a *second* determination, hence a real test rather than a fit |
| Q2 | knowing Q makes the spectral-curve comparison with Keller concrete |

**That double payoff is the reason this is worth the whole week.** A single
determination of χ⊥ would be a fit. Two independent determinations agreeing is
the Eötvös standard, and the gap is the only thing standing between the corpus
and having them.

---

## 5. What is now standing (do not re-derive these)

| item | status |
|---|---|
| sech² profile | derived from binariness (Var of a two-point distribution) |
| the invariant 9(1+w)² + 6w′ = 4ϱ⊥² | derived; it is ⟨Q²⟩ = 1 rescaled |
| N_c | derived; unique global minimum of 𝔖_J |
| the crossing direction (arrow) | derived twice: 𝔖_J ≥ 0, and the pole's half-plane |
| ℓ = 1 | total Levinson phase π = Fisher diameter π; four statements, one fact |
| ϱ⊥ = 1 | **over-characterised, not derived**: (i) q_∞ = 0, the acceleration separatrix, with the event horizon marginally absent; (ii) I·I/H² → −1/2, halfway between null and de Sitter; (iii) N is e-affine with the Q² = 1 normalisation; (iv) one Weyl e-fold = one e-fold of spectral momentum |
| χ⊥ = constant | theorem (Chentsov), not assumption |
| G^BKM normalisation | theorem (Petz f(1)=1); no freedom |
| the vertical sector | exact tractor calculus, nothing free |
| the two-lobed H(z) signature | **not evidence** — forced by distance-matching (IVT) |
| the CMB-lensing anti-alignment | **not evidence** — 92.9% of random transient histories pass |

---

## 6. Why solving it should simplify the framework

The intuition that this will make things *simpler* is, I think, correct, and it
can be stated precisely.

The programme currently maintains **three vocabularies** — modular /
operator-algebraic, conformal / tractor, and cosmological / fluid — related by
translation dictionaries kept by hand. That is expensive, it is where the v5.0
λ-conflation came from, and it is what makes the corpus hard to hand to a
referee.

After c:

- the vertical side is **entirely** tractor calculus; the modular vocabulary is
  not needed there at all (I·I = −μ_A H² makes η_A redundant);
- the horizontal side is **entirely** information geometry; the cosmological
  vocabulary is not needed there (θ, G^BKM, 𝔖_J are self-contained);
- and they are joined by **one number**.

That is the shape of every theory that worked: differential geometry plus matter
joined by G; Hilbert space plus observables joined by ħ. Two rigid formalisms
and a coefficient is *simpler* than five open problems in three dialects, and
the "modular–Weyl" compound noun stops being a separate thing to learn. It
becomes a soldering coefficient between two standard subjects.

---

## 7. How the convergence could be illusory

Stated before the work, so it counts.

### 7.1 The load-bearing hypothesis has already failed once

The absorption Q3 ⊂ Q1 requires that the perturbation potential be
**ρ_X-proportional** — that is T1's hypothesis. **N1 showed it fails for the
linear growth operator**: ΔW/Ω_X spans −179 to +0.27, and a free sech² fit gives
a 63.9% residual. The growth equation is a zero-energy problem with no spectral
parameter, so it was never a candidate — but the point stands that the
hypothesis is currently satisfied by *no* operator we can write down. If the
pair-completed operator also fails it, the convergence unwinds and r_c returns
to being an independent postulate.

### 7.2 Other ways it breaks

- **ℓ ≠ 1.** The Fisher-diameter argument for ℓ = 1 is suggestive, not a proof.
  ℓ = 2 gives cχ⊥ = 6 and every downstream number moves.
- **Q may not exist as a single physical observable.** The rank-one reduction is
  described as schematic in the erratum. If the relevant modular family is
  higher rank, sech² is not forced and the invariant's value is not 4ϱ⊥².
- **The Levinson identification may be folklore.** Levinson is textbook and the
  Fisher diameter is textbook; only the identification is new *to me*. The
  Birman–Kreĭn spectral shift function ξ = δ/π is exactly this object and is
  well studied. Check before claiming priority.
- **The tractor side, though exact, is sterile.** N3: the FLRW tractor
  connection is flat, so the vertical formalism contributes nothing to the gap.
  "Two rigid formalisms" is accurate; it is not two sources of leverage.

### 7.3 Kill conditions on the convergence itself

- **KC1.** The pair-completed operator's potential is not ρ_X-proportional →
  Q3 ⊂ Q1 fails; r_c is an independent postulate again.
- **KC2.** c is determined and c·ρ_m(N_c) ≠ 2 → either transparency or r_c = 1
  is wrong. Both cannot survive.
- **KC3.** χ⊥ from the Chatterjee route ≠ χ⊥ from the transparency route → the
  soldering law is wrong somewhere.
- **KC4.** The computed r_c ≠ 1 → the zero-new-dimensionful-constants claim
  collapses and the model is level with Λ_sCDM on economy, not ahead of it.

**KC4 is the real stake and it should be written into the master document before
the calculation is run**, not after.

---

## 8. Attack routes, ranked

1. **Identify Q.** The whole gap. Two entry points, and they should be run
   against each other: *from below*, ask what two-level structure the crossing
   no-go's pair completion actually supplies, and whether its BKM metric is the
   sech² already in use; *from above*, ask what dichotomy has JQJ = −Q with the
   self-dual point at matter–dark equality.
2. **Write the pair-completed operator and read off c.** This is (B). Even a
   partial answer tests KC1, which gates everything.
3. **The Chatterjee type III construction for the FLRW diamond**, once Q is
   known — the second determination of χ⊥, and therefore the difference between
   a fit and a test.
4. **Q2** (Keller ↔ spectral curve). Independent, cheap, high variance. Now has
   a specific mechanism: self-reciprocality as the no-local-obstruction
   statement.
5. **P1, P4, P8 on w(z) reconstructions.** Data-side, requires no theory,
   breaks the r_c–ϱ⊥ degeneracy (T9), and tests three predictions off one
   reconstruction. Should run in parallel with everything above.

---

## 9. Receipt index (new material)

| receipt | verifies |
|---|---|
| R13 | binary family is a Chatterjee self-dual family; 𝔖_J = 4θ tanh θ; Eqs. 35/36/37; I_J(0) = 8 (T11) |
| R14 | I_J = 2γ^BKM on the modular-selected tangent ΔX = 2X_\* (T11) |
| R15 | 𝔖_J = 6(N−N_c)(1+w), ϱ⊥-free; positivity forces the crossing direction (T12) |
| R16 | I·I three ways; **I·I = −μ_A H²** to 1e-11; I·I ∝ T (T13) |
| R17 | **[NEGATIVE]** Φ\*G^BKM ∝ I·I fails; τ̊ = 0 ⟺ ρ+p = 0; the 1:1 split (N3, T14) |
| R18 | **[NEW]** Levinson phase density = sech = BKM line element, both → π; pole in the upper half plane (T15) |
| R19 | **[NEW]** sech is Fourier self-reciprocal — the structural reason; the preregistered c·ρ_m(N_c) = 2 (T16) |

All in `receipts_transparency_fold.py`. No external data required.

---

## 10. One-sentence hand-off

> Everything in the modular–Weyl branch is now either derived, over-characterised,
> or determined by a single coefficient c fixed by how the BKM susceptibility
> enters the pair-completed perturbation operator — and the only thing needed to
> obtain it is to say what two-state distinction the binary grade labels.
