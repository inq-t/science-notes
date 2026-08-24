# The Lemmas, and What Γ_MW Must Contain

## Establishing L1 and L3, and a structural audit for hidden parameters

**Thomas Ruble research programme — AI-assisted technical hand-off**
**21 August 2026**

Receipts R20–R21 in `receipts_transparency_fold.py`. Companion: master v6.0.

---

## 0. Summary of findings

| | result |
|---|---|
| **L1 (cocycle)** | **Closed**, modulo one named hypothesis. Affine soldering is a theorem of Cauchy's functional equation. ϱ⊥ appears as its single integration constant — so the *form* is derived and the *value* is not, and cannot be by this route |
| **L3 (rank one)** | **Splits.** L3a (one-dimensional invariant direction) is a cheap symmetry argument. **L3b (Q² = 1) does not follow from it** and is the load-bearing half — a new finding |
| **L2 (weight)** | **Not closed**, and now obstructed for a reason: see §4 |
| **N4** | **New negative, exact.** No canonical sigma model with the BKM target metric can realise the rigid pulse under the soldering law |
| **Scale audit** | χ⊥ is dimensionful. The constitutive law reintroduces a fixed length into a programme founded on scale-freedom |
| **Version B** | The conformally natural law Ω_X = λ𝒳_σ is **falsified**: it puts w_X = 0 at the peak, not −1. The dimensionful χ⊥ is forced |
| **The dilemma** | Economy and novelty pull in **opposite** directions inside Γ_MW (§6). This is the deepest structural finding here |

---

## 1. Lemma 1 — affine soldering `[THEOREM, conditional]`

**Hypotheses.**
- **(H-rank)** Under FLRW reduction the Connes cocycle comparing the states of two scale sections has, modulo the centre, a single noncentral generator:
  [Dω_{σ₂} : Dω_{σ₁}]_t ≃ exp{it[θ(σ₂,σ₁)Q + c𝟙]}.
- **(H-ratio)** θ depends on σ₂, σ₁ only through the ratio r = σ₂/σ₁.
- **(H-meas)** θ is measurable in r.

**Proof.** Connes' chain rule gives
[Dω₃:Dω₁]_t = [Dω₃:Dω₂]_t · σ_t^{ω₂}([Dω₂:Dω₁]_t). Under (H-rank) the reduced
generators commute, so the modular automorphism acts trivially on the reduced
cocycle and the identity becomes multiplicative. Matching noncentral parts,

$$\theta(r_1 r_2) = \theta(r_1) + \theta(r_2), \qquad r_i \in \mathbb{R}_{>0}$$

This is Cauchy's exponential–additive equation. With (H-meas) — measurability
suffices; continuity is not needed — the only solutions are

$$\boxed{\;\theta(r) = -\varrho_\perp \ln r \;\Longleftrightarrow\; \theta = \varrho_\perp (N - N_c)\;}$$

∎

**What this settles.** Affine soldering is no longer a postulate. Given (H-rank),
the *linearity* of θ in N is forced by the cocycle identity alone. This removes
one item from §2.2's ledger.

**What it cannot settle, and why that is a theorem not a gap.** Cauchy's equation
has a **one-parameter** solution family, and ϱ⊥ *is* that parameter. No amount of
additional work on the cocycle can fix its value, because the functional equation
is indifferent to it. ϱ⊥ is meaningful — it is not absorbable, since Q² = 1 fixes
Q's normalisation and N = ln a fixes the group's — but it must be fixed by
something outside the cocycle structure.

`[CORRECTION to v6.0 §16.2]` The document says continuity forces the log. It is
weaker: measurability suffices, by the standard Cauchy/Banach argument. Worth
stating, because measurability follows from the σ-weak continuity of the cocycle
whereas continuity in r would need separate argument.

---

## 2. Lemma 3 — rank one, and where it actually bites

v6.0 §5.2 correctly declines to claim the type III modular spectrum has only two
grades. It does not need to. But the reduction splits into two claims that the
document runs together, and they have very different costs.

### L3a — one-dimensional invariant direction `[cheap, plausible]`

At a codimension-two FLRW-symmetric cut, the normal bundle is a
two-dimensional Lorentzian plane spanned by the null pair (ℓ, n). The relative
modular Hamiltonian must be invariant under the cut's symmetry group (which acts
transitively on Σ) and J-odd. Invariance forces it to be constant on Σ, so it is
characterised by its normal-plane structure; the available structures there are
the metric (J-even) and the boost generator (J-odd). Hence

> the space of symmetry-invariant, J-odd relative-modular directions at a
> homogeneous cut is **one-dimensional**, spanned by the normal boost.

This is an invariant-theory statement about the isometry group acting on modular
data — dramatically cheaper than any spectral claim, and it is the claim actually
used.

### L3b — Q² = 1 `[LOAD-BEARING, does not follow]`

**But L3a gives a one-dimensional *direction*, not a two-point *spectrum*.** A
boost generator on a type III algebra has continuous, unbounded spectrum. The
claim Q² = 1, spec(Q) = {−1, +1}, is a separate and far stronger reduction, and
it is what does all the work downstream:

- Var(Q) = sech²θ — hence the entire pulse shape;
- ⟨Q²⟩ = 1 — hence the invariant's *value* 4ϱ⊥², hence T6, T7, T3, T4.

Without L3b, Var(Q) is not sech²θ and nothing in §6–7 survives.

`[CORRECTION to v6.0 §5.2]` The structural hypothesis should be split. The
current wording ("the homogeneous infrared response factors through one
normalized J-odd score Q with Q² = 1") bundles a cheap symmetry claim with an
expensive spectral one. Split them; L3a is nearly free and L3b is the real
postulate.

**A candidate for L3b.** The null pair (ℓ, n) spans a genuinely two-dimensional
space, and its grading operator — +1 on ℓ, −1 on n — satisfies Q² = 1 exactly.
So L3b is the claim that *the FLRW-reduced modular grade is the null-pair
grading*. That is a specific geometric object rather than an abstraction, which
is progress, but it is a claim about a reduction from type III data to a
two-dimensional factor, and it is not established.

---

## 3. Lemma 2 — why it is obstructed

The weight lemma (𝓛_pol ≅ 𝓔[2] ⟹ ϱ⊥ = 1) hits a specific obstruction. θ is a
log of a probability ratio: it is **dimensionless and weight-zero**. Under a
constant Weyl rescaling both N and N_c shift together, so θ is invariant. There
is no weight to read off from θ itself.

The weight has to be read off from the *cocycle*, not from θ — i.e. from how
[Dω_{σ₂}:Dω_{σ₁}]_t transforms under a Weyl rescaling of the representative
metric, which requires knowing how the state family ω_σ is constructed from σ.
That construction is exactly what Γ_MW is supposed to supply. **Lemma 2 is
downstream of Γ_MW, not independent of it.** It should be re-ordered in the work
plan accordingly.

A cleaner reformulation worth attempting instead: the ℓ = 1 bound state falls off
as a^{∓ϱ⊥}, so ϱ⊥ = 1 ⟺ **the localised collective mode is a conformal density
of weight one — i.e. it is itself a scale.** Self-consistency of that kind is a
better-shaped target than a bundle isomorphism.

---

## 4. `[NEGATIVE N4]` The canonical sigma model cannot carry the soldering

The obvious Γ_MW is a nonlinear sigma model with the BKM target metric:

$$\Gamma = \int\!\sqrt{-g}\left[\tfrac{\chi}{2}G^{\rm BKM}(\theta)\,g^{\mu\nu}\partial_\mu\theta\,\partial_\nu\theta - V(\theta)\right]$$

giving ρ = ½χGθ̇² + V, p = ½χGθ̇² − V, hence 1 + w = χGθ̇²/ρ. Impose the
soldering θ̇ = ϱ⊥H together with the target profile 1 + w_X = (2ϱ⊥/3)tanh θ,
ρ_X = ρ_* sech²θ, G = sech²θ:

$$H^2 = \frac{2\rho_*}{3\chi\varrho_\perp}\tanh\theta$$

For all θ < 0 — **the entire pre-crossing branch** — this demands H² < 0 (R20).

> No canonical sigma model with the BKM target metric realises the rigid pulse
> under the soldering law.

This is N2 seen from the Lagrangian side, and it is exact rather than
perturbative. Γ_MW must be non-canonical: constrained, multi-component with
indefinite kinetic structure, nonlocal, or algebraic.

---

## 5. The scale audit — and the death of the conformally natural law

### 5.1 χ⊥ carries a length

𝒳_σ = G^BKM(dθ/dN)² is built entirely from dimensionless quantities: it is
weight zero and contains no length. ρ_X is an energy density — 1/length² in
geometric units. Therefore **χ⊥ must carry 1/length².**

> In a programme whose founding claim is that causal order fixes geometry only
> *up to scale*, the constitutive law silently reintroduces the scale that was
> removed.

And r_c = 1 is precisely the statement that this length is not new: it equals
ρ_m(N_c)^{−1/2}. **That is why r_c carries the entire economy claim**, and why it
looks like a coincidence — it is asserting that a constitutive constant coincides
with a contingent cosmological density.

### 5.2 The alternative is falsified

The conformally natural law puts the pure number on the *fraction*:

$$\text{Version A: } \rho_X = \chi_\perp \mathcal{X}_\sigma \quad\text{vs.}\quad \text{Version B: } \Omega_X = \lambda\,\mathcal{X}_\sigma$$

Version B introduces no length, is algebraic (H² = (ρ_m+ρ_r)/(1−Ω_X), no new
integration constant), and is what a sigma-model reduction actually produces.
Tested (R21):

| λ | Ω_X max | status |
|---|---|---|
| 0.500 | 0.500 | **excluded** — cannot reach Ω_X(0) = 0.689 |
| 0.689 | 0.689 | crossing forced to today, z_c = 0 |
| 0.850 | 0.850 | viable window |
| 1.000 | 1.000 | **singular**, Ω_X → 1, H² → ∞ |

So λ = ½ (equipartition) is excluded and λ = 1 (no coefficient at all) is
singular; the viable window (0.689, 1) contains no natural value. Worse, at
λ = 0.85:

$$w_X(\text{peak}) = +0.000156 \quad\text{— it needs } -1$$

**Version B does not put w_X = −1 at the susceptibility peak.** It therefore
loses T8 (the three-epoch coincidence) *and* the shape invariant. Version B is
dead.

> **The dimensionful χ⊥ is forced, and with it a fixed length. This is not a
> choice the programme can make differently.**

---

## 6. The dilemma inside Γ_MW

N4 says the soldering cannot be the field equation of a canonical sigma model.
That leaves two forks, and they pull in opposite directions.

**Fork I — θ is an independent field.** Then the soldering θ̇ = ϱ⊥H must emerge
from exotic dynamics: an indefinite kinetic matrix, a constraint with a Lagrange
multiplier, or a nonlocal/algebraic closure. Each of these is a place where free
functions enter. In particular a two-component kinetic matrix generically brings
a free sound speed c_s²(k, N) — the exact epicycle the programme is trying to
avoid, and the one that transparency was meant to forestall but (under the
Weyl-weight reading) cannot, since a weight-space operator is blind to spatial
gradients.

**Fork II — θ is slaved to the geometry.** The soldering is a *kinematic
identification*, not a dynamical equation; θ is determined by g rather than
evolving alongside it. This is maximally economical: **no new degrees of freedom
at all**, and criterion 7 ("no independent dark clustering mode") is satisfied by
construction rather than by transparency. Transparency becomes moot, since there
is no independent operator to be transparent.

**The dilemma.** Fork II is the economical answer — and it fails v6.0's own
elimination test *by construction*. If θ is defined from the geometry, it cannot
independently predict H(z); it is a relabelled fluid in the document's precise
sense. Fork I can pass the elimination test but reopens the parameter question.

> **Economy and novelty are in tension inside Γ_MW.** Every step toward "no new
> degrees of freedom" is a step toward "θ is not independent," which is a step
> toward the relabelled-fluid side of §1's test.

This, not r_c, is the deepest structural issue in the programme, and it should be
stated in the master document.

---

## 7. Hidden-parameter census

What Γ_MW must contain, sorted by whether it is forced or free:

| item | status |
|---|---|
| affine soldering | **derived** (L1), given H-rank |
| one-dimensional invariant direction | **near-free** (L3a, symmetry) |
| Q² = 1 | **postulate**, load-bearing, not implied by L3a |
| ϱ⊥ value | **free**, one Cauchy integration constant; not fixable by cocycle methods |
| χ⊥ dimensionful | **forced** (§5) — Version B is dead |
| χ⊥ value | **free**, unless r_c = 1 is derived |
| non-canonical kinetic structure | **forced** (N4) |
| c_s² or clustering prescription | **free under Fork I**, absent under Fork II |
| separate conservation | **assumption** — equivalent to Γ_MW having no matter coupling; not currently on the ledger |

**Two genuinely free numbers (ϱ⊥, χ⊥), one load-bearing spectral postulate
(Q² = 1), one forced structural exotic (non-canonical kinetics), and one
fork-dependent free function (c_s²).** That is the honest count. It is not a
zoo — but "zero parameters" is not right either.

---

## 8. On "physics is mathematics"

The results above sharpen the thesis rather than contradicting it, and the
sharpening is itself a theorem.

**Mathematics fixes form and dimensionless structure; it does not fix scale.**
Cauchy's equation *derives* θ = −ϱ⊥ ln r and *cannot* derive ϱ⊥ — the solution
family is one-dimensional as a matter of proof. The weight audit *forces* χ⊥ to
be dimensionful and *therefore* forbids pure mathematics from supplying its
number.

The correct target is therefore not "derive χ⊥ from mathematics" but **express
χ⊥ as a ratio to something already in the theory**, because ratios are
dimensionless and dimensionless quantities are exactly what mathematics can
produce. r_c = 1 is precisely such an expression: χ⊥ϱ⊥² = ρ_m(N_c). Its shape is
right. What remains is *why that ratio and not another* — and that is a question
mathematics can answer, because it is a question about a pure number.

The same holds for ϱ⊥. Do not look for a derivation of "1" from an isolated
construction; look for a second, independent determination of the same
dimensionless quantity. That is the Eötvös standard, and it is what would convert
a chosen unity into a measured constant.

---

## 9. Revised work order

1. **Close L3a properly** — write the invariant-theory argument at a
   codimension-two FLRW cut. Cheap, and it shortens the ledger visibly.
2. **Attack L3b** — is the FLRW-reduced grade the null-pair grading? This is the
   load-bearing postulate and it now has a concrete geometric candidate.
3. **Decide the fork (§6) explicitly and in writing.** This determines whether
   the programme is chasing economy or novelty, and it changes what Γ_MW must be.
   Do not build Γ_MW before deciding.
4. **Only then Γ_MW**, with the fork fixed.
5. **L2 after Γ_MW**, not before — it is downstream (§3).
6. **P1/P4/P8 on w(z) reconstructions**, in parallel throughout. Data-side, no
   theory required, and P1 is publishable on its own.

---

## 10. Corrections to master v6.0

1. **§16.2** — measurability, not continuity, suffices in Cauchy's equation.
2. **§5.2** — split the structural hypothesis into L3a (symmetry, cheap) and
   L3b (Q² = 1, load-bearing).
3. **§6.1** — affine soldering is derivable (L1); move it from postulate to
   conditional theorem with H-rank named.
4. **§2.2 / §6.3** — state that χ⊥ is necessarily dimensionful and that the
   conformally natural alternative is falsified (R21). This is the strongest
   argument *for* the current constitutive law and it is currently missing.
5. **§2.3** — add separate conservation, typed as "Γ_MW has no matter coupling."
6. **New section** — the Fork of §6. It is more fundamental than r_c.
7. **§8.3** — delete the sound-speed bullet (a weight-space operator is blind to
   spatial gradients) and drop the claim that transparency derives criterion 7.
8. **§15.2** — "zero extra parameters after fixing two unities," not "0."
