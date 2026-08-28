# Ruble's Equations

## The modular–Weyl scale programme as a closed equation set: meaning, derivation, harmony, and stopping condition

**Thomas Ruble**
**21 August 2026**

All identities verified in `receipts_transparency_fold.py`. Labels: `[POSTULATE]`,
`[THEOREM]`, `[CONSTANT]`, `[BRANCH]`, `[IMPLEMENTATION]`.

---

## 0. The functional signature

Schrödinger did not derive the hydrogen Hamiltonian before writing Ĥψ = iħ∂_tψ.
He supplied a **functional signature** — a form that every system must fill in
its own way — and the field then spent a century filling it in. The equation's
content was the form, not any particular solution.

These equations have that character. They say:

> **A causal region carries two geometries. One is conformal structure with a
> scale (the vertical register). The other is the information geometry of the
> region's modular state (the horizontal register). Gravity is the transport law
> of the first. What we call dark energy is the Legendre Jacobian of the second,
> converted to stress by one constant.**

The form is fixed. Which state family, which causal region, and what χ⊥ measures
to — those are implementations, not gaps.

---

## 1. The stopping condition

A physical theory is finished when every quantity in it is one of:

| type | example elsewhere | here |
|---|---|---|
| **(a) derived** | Kepler's laws from Newton | the pulse, invariant, phase portrait, futures, perturbation operator, Fisher length, ceiling |
| **(b) structural choice** | dim = 3; the gauge group SU(3)×SU(2)×U(1) | **rank-one binary closure, Q² = 1** |
| **(c) constant of nature** | G, ħ, c, α | **ϱ⊥ (dimensionless), χ⊥ (dimensionful)** |

and **nothing** is of the fourth type:

| **(d) free function inserted to fit** | CPL's (w₀, wₐ); IDE's interaction term; an inserted c_s²(k,z) | **none** |

The absence of type (d) is the whole claim. It is what separates this from every
competitor in §9.

There is one further requirement, and it is met: **the theory must be able to
fail.** §8 lists five ways.

`[DEDUCTION]` A theorem of §7 below is that mathematics *cannot* produce a
dimensionful number — it can produce forms and dimensionless ratios only.
Demanding a derivation of χ⊥ therefore demands something provably impossible.
Postulating it is not a deficiency; it is the only available move, and it is the
move every successful theory has made.

**The equations below are complete under this standard.**

---

## 2. The postulate

There is exactly one.

> **P — Rank-one binary closure.** `[POSTULATE]`
> The homogeneous infrared response of a causal region factors through a single
> normalised, modular-odd score
> $$Q^2 = \mathbf{1}, \qquad JQJ = -Q, \qquad \operatorname{spec}(Q) = \{-1,+1\}$$

Everything in §§3–6 follows. Its type is that of "space has three dimensions" or
"the gauge group is SU(3)×SU(2)×U(1)": a structural selection, not a fitted
number. Its geometric candidate is the grading of the null pair (ℓ, n) spanning
the Lorentzian normal plane of a codimension-two cut, where Q² = 1 holds exactly.

---

## 3. The master identity, and its five faces

From P, the exponential family and its log-partition function are forced:

$$\omega_\theta = e^{\theta Q - \Psi(\theta)}, \qquad \Psi(\theta) = \ln(2\cosh\theta)$$

with dual coordinate and metric

$$\eta = \Psi'(\theta) = \langle Q\rangle = \tanh\theta, \qquad g = \Psi''(\theta) = \operatorname{Var}(Q) = \operatorname{sech}^2\theta$$

and therefore

$$\boxed{\;\eta^2 + g = \langle Q^2\rangle = 1\;}$$

**This single identity is the entire theory.** It appears in five registers and
they are the same statement:

| register | form | meaning |
|---|---|---|
| **algebraic** | ⟨Q²⟩ = 1 | the score is a normalised binary |
| **geometric** | (η, √g) on the unit circle | §4 |
| **dynamical** | η′ = 1 − η² | Riccati; the saddle-node normal form |
| **cosmological** | 9(1+w_X)² + 6 dw_X/dN = 4ϱ⊥² | the shape invariant, testable bin by bin |
| **spectral** | η² + η′ = 1 | the SUSY condition making H₊ free (§5) |

That one normalisation does five jobs in five different mathematical languages is
the reason to take the construction seriously. It is not five coincidences.

---

## 4. The harmony: one half-turn

`[THEOREM]` Because η² + g = 1, the pair (η, √g) traces the unit circle. Write

$$\eta = \sin\varphi, \qquad \sqrt{g} = \cos\varphi$$

Then φ is determined:

$$\boxed{\;\varphi = \operatorname{gd}(\theta) = \arctan(\sinh\theta)\;}$$

the **Gudermannian** — the classical function joining hyperbolic to circular
trigonometry without passing through the complex numbers. Verified to 2×10⁻¹⁶.

And its differential is the Fisher line element:

$$d\varphi = \operatorname{sech}\theta\, d\theta = ds_{\rm Fisher}$$

> **The Fisher arc length *is* the angle. The entire cosmic dark history is one
> half-turn of the unit circle, φ: −π/2 → +π/2, total length π.**

The whole history in one angle:

$$\frac{\rho_X}{\rho_*} = \cos^2\varphi, \qquad \frac{3(1+w_X)}{2\varrho_\perp} = \sin\varphi, \qquad \frac{ds_F}{dN} = \varrho_\perp\cos\varphi$$

| φ/π | epoch | ρ_X/ρ_\* | 3(1+w)/2ϱ⊥ |
|---|---|---|---|
| −0.45 | deep past | 0.0245 | −0.9877 |
| −0.25 | past | 0.5000 | −0.7071 |
| **0.00** | **crossing** | **1.0000** | **0.0000** |
| +0.25 | future | 0.5000 | +0.7071 |
| +0.45 | far future | 0.0245 | +0.9877 |

φ = 0 is simultaneously: the density maximum, the w_X = −1 crossing, the
modular self-dual point, the maximum of the BKM metric, and the epoch at which
the score carries exactly **one bit** (S = ln 2). Five descriptions, one event.

**And the same function governs momentum space.** The transmission phase of the
perturbation operator (§5) satisfies

$$\arg t(s) = \frac{\pi}{2} - \operatorname{gd}(s), \qquad s = \ln(k/\varrho_\perp)$$

verified to 4×10⁻¹⁶. The Fisher angle in position and the scattering phase in
momentum are the *same Gudermannian*, each sweeping π. Position and momentum
give one picture because sech is self-reciprocal under Fourier transform.

---

## 5. The perturbation operator is not chosen — it is generated

`[THEOREM]` Define the first-order operators built from the information
potential itself:

$$\mathcal{A} = \partial_\theta + \eta, \qquad \mathcal{A}^\dagger = -\partial_\theta + \eta$$

Then, using **only** η² + g = 1:

$$\boxed{\;\mathcal{A}^\dagger\mathcal{A} = -\partial_\theta^2 + 1 - 2\operatorname{sech}^2\theta, \qquad \mathcal{A}\mathcal{A}^\dagger = -\partial_\theta^2 + 1\;}$$

Verified to 4×10⁻¹⁶. **H₊ is free precisely because ⟨Q²⟩ = 1.** The binary
normalisation *is* the supersymmetry condition. The ℓ = 1 Pöschl–Teller operator
is the Witten Laplacian of the binary statistical manifold — not a hypothesis
about a perturbation sector, but a theorem about the postulate.

Consequences, all forced:

- **Zero mode** 𝒜ψ₀ = 0 gives ψ₀ = sech θ/√2, and $|\psi_0|^2 = \tfrac12 g$ — **the BKM metric is twice the bound-state density.**
- **Reflectionless.** ψ_k = 𝒜†e^{ikθ} = (−ik + tanh θ)e^{ikθ} has no e^{−ikθ} component at either end. R(k) ≡ 0.
- **Witten index 1** — one bound mode, and Levinson's theorem then gives total phase π, matching §4.
- **The pair is generated, not assumed.** The 1-D statistical manifold has de Rham complex Ω⁰ ⊕ Ω¹; Witten deformation by Ψ turns it into the two-component Dirac operator. The perturbative pair is *form parity*, canonically generated by the binary line — it is not the binary outcomes themselves, and must not be conflated with Q.

---

## 6. The equations

### Vertical register — geometry

**R1 (scale).** `[STANDARD]` Causal order fixes conformal structure but not scale.
$$g_{\rm phys} = \sigma^{-2}\boldsymbol{g}, \qquad N = -\ln(\sigma/\sigma_c) = \ln(a/a_c), \qquad I_A = \tfrac14 D_A\sigma$$

**R2 (transport).** `[STANDARD]` Trace-free stress obstructs parallel scale transport.
$$\mathcal{E}_{ab}(\sigma) = \frac{4\pi G}{c^4}\,\sigma\left(T^m_{ab} + T^X_{ab}\right)^\circ$$

**R3 (norm).** `[STANDARD]` The stress trace and one global lift set the tractor norm.
$$I^2 = \frac{2\pi G}{3c^4}T - \frac{\Lambda_g}{3}, \qquad I^2 = -\frac{R}{12}$$

**R4 (the horizon bridge).** `[THEOREM]` Verified to 10⁻¹¹.
$$I^2 = -\mu_A H^2, \qquad \mu_A = \frac{1-q}{2} = \frac{d\eta_A}{dN}$$
The vertical horizon-clock rate *is* the normalised tractor norm. The e-fold
budget then splits exactly:
$$dN = d\eta_A + \tfrac14 d\ln\mathcal{S}_A$$

### Horizontal register — state

**R5 (the postulate).** `[POSTULATE]` §2.

**R6 (dual coordinates).** `[THEOREM]` §3. Ψ = ln(2cosh θ), η = tanh θ, g = sech²θ.

**R7 (the master identity).** `[THEOREM]` η² + g = 1.

**R8 (soldering).** `[THEOREM, conditional]` If the reduced Connes cocycle has a
single noncentral generator and depends only on the scale ratio, the cocycle
identity forces Cauchy's equation θ(r₁r₂) = θ(r₁) + θ(r₂). With measurability,
$$\frac{d\theta}{dN} = \varrho_\perp \;\Longleftrightarrow\; \theta = \varrho_\perp(N - N_c)$$
Affine soldering is **derived**. ϱ⊥ is the single integration constant Cauchy's
equation permits — which is exactly why no further work on the cocycle can fix
its value.

**R9 (the Gudermannian).** `[THEOREM]` §4. φ = gd(θ), ds_F = dφ, L_F = π.

**R10 (the Witten complex).** `[THEOREM]` §5.

### The soldering law — one constant

**R11 (constitutive response).** `[CONSTANT]`
$$\mathcal{X}_\sigma = g\left(\frac{d\theta}{dN}\right)^2 = \varrho_\perp^2\operatorname{sech}^2\theta, \qquad \boxed{\;\rho_X = \chi_\perp\,\mathcal{X}_\sigma\;}$$

This is the analogue of T_ab = (c⁴/8πG)G_ab. **χ⊥ is a stiffness with dimensions
of energy density, exactly as G is a stiffness converting stress to curvature.**

### Consequences — all derived

**R12 (equation of state).** From separate conservation, dρ_X/dN = −3(1+w_X)ρ_X:
$$3(1+w_X) = 2\varrho_\perp\eta = 2\varrho_\perp\sin\varphi$$

**R13 (shape invariant).** `[THEOREM]` R7 in cosmological variables:
$$9(1+w_X)^2 + 6\frac{dw_X}{dN} = 4\varrho_\perp^2$$

**R14 (phase flow).** `[THEOREM]` With X = 1 + w_X:
$$X' = \tfrac23\varrho_\perp^2 - \tfrac32 X^2$$
the canonical saddle-node normal form. One density maximum, one w = −1 crossing,
one heteroclinic episode are **one** structural statement, not three fitted
events. Fixed points w_± = −1 ± 2ϱ⊥/3.

**R15 (self-duality and orientation).** `[THEOREM]` The symmetrized relative
entropy against the modular reflection is
$$\mathfrak{S}_J = 4\theta\eta = 6(N-N_c)(1+w_X) \ge 0$$
Non-negativity of relative entropy then **forces** w_X < −1 before the crossing
and w_X > −1 after. The orientation of the crossover relative to increasing Weyl
scale is a theorem, not an input.

**R16 (the future).** `[THEOREM]` w_∞ = −1 + 2ϱ⊥/3, a(t) ∝ t^{1/ϱ⊥}, and
$$\varrho_\perp = 1 \iff w_\infty = -\tfrac13 \iff q_\infty = 0 \iff a \propto t \iff \frac{I^2}{H^2} \to -\tfrac12$$
Unity is the separatrix between three causal futures, and sits exactly halfway
between the null tractor (Minkowski, 0) and de Sitter (−1).

**R17 (the moduli ceiling).** `[THEOREM]` Flatness gives
r_c e^{3x}sech²(ϱ⊥x) = T_m, with a double root at
$$\frac{T_m}{r_c} = \left(1 - \frac{9}{4\varrho_\perp^2}\right)\exp\left[\frac{3}{\varrho_\perp}\operatorname{artanh}\frac{3}{2\varrho_\perp}\right]$$
so ϱ⊥ ≤ 1.814 at the benchmark. A second saddle-node, in the moduli of flat
histories.

---

## 7. The two constants

`[THEOREM]` 𝒳_σ is built entirely from dimensionless quantities; ρ_X is an energy
density. **Therefore χ⊥ must carry dimensions, and no theorem about a
dimensionless statistical manifold can output them.** This is not a gap in the
theory — it is a theorem about what mathematics can do. Ratios and forms are
derivable; scales are measured.

The conformally natural alternative — putting the pure number on the fraction,
Ω_X = λ𝒳_σ — was tested and **falsified**: it puts w_X = +0.0002 at the
susceptibility peak where it needs −1, losing both the three-epoch coincidence
and the shape invariant. The dimensionful χ⊥ is forced.

| | ϱ⊥ | χ⊥ |
|---|---|---|
| **type** | dimensionless | energy density |
| **analogue** | α, the fine-structure constant | G |
| **rigid value** | 1 | such that r_c = 1 |
| **measured** | 1.0 ± 0.2, from four determinations | z_c = 0.342 at the benchmark |
| **independent test** | P1, the shape invariant, bin by bin | P4, the equality coincidence |

### Why r_c = 1 is a plausible measured value

Write χ⊥ = κ·ρ_crit(N_c). Flat self-consistency at the crossing then gives, with
**no further input**,

$$\boxed{\;r_c = \frac{\kappa}{1-\kappa}\;} \qquad\Longrightarrow\qquad r_c = 1 \iff \kappa = \tfrac12 \text{ exactly}$$

`[CONJECTURE]` For the apparent horizon R = 1/H, the identity
$$\frac{T_c S_c}{V_c} = \frac{3H_c^2}{8\pi G} = \rho_{\rm crit}(N_c)$$
holds **exactly** with the Hubble temperature T = H/2π. So if the constitutive
stiffness is the modular free-energy Hessian per unit volume,
χ⊥ = (T_c/2V_c)·C_E with capacity C_E = S_c, then κ = ½ and

$$r_c = 1.00039528, \qquad z_c = 0.341793$$

with the 4×10⁻⁴ departure being exactly ρ_r/ρ_m at the crossing. **The rigid
value is not fine-tuned; it is what a capacity–entropy relation would give.**

Two honest caveats, stated before the work: with the Kodama–Hayward temperature
instead, κ = μ_A/2 and self-consistency gives r_c = 1/4, which the background fit
excludes. And the ansatz identifies a squared displacement with a squared rate,
which carries a per-e-fold convention. This is a **route**, not yet a
derivation — and if it fails, χ⊥ remains a measured constant and nothing above
changes.

---

## 8. Predictions and kill conditions

Benchmark: Ω_m = 0.310598, Ω_r = 9.15×10⁻⁵, ϱ⊥ = 1, r_c = 1, Λ_res = 0, k = 0.
N_c = −0.29417, z_c = 0.3420, q₀ = −0.3368, z_acc = 0.7857.

**P1 — the invariant, redshift by redshift.** `[PRIMARY]`
9(1+w(z))² + 6 dw/dN = 4, at **every** z. Not a fitted number; a differential
law tested independently in every reconstructed bin.
**K1:** dies if the reconstructed combination varies with z beyond errors.

**P2 — the local tangent.** (w₀, wₐ) = (−0.809, −0.612), zero free parameters,
against DESI DR2+CMB+Pantheon+ (−0.838 ± 0.055, −0.62 ± 0.20): 0.53σ and 0.04σ.

**P3 — the crossover.** z_c = 0.3420, fixed by flatness, not adjusted after fitting.

**P4 — the equality coincidence.** `[DIRECT TEST OF r_c]`
z(w_X = −1) = z(ρ_X = ρ_\*) = z(ρ_X = ρ_m). In the DESI CPL best fit these
separate by Δz = 0.019, so the identification is falsifiable.
**K4:** dies if they separate beyond errors.

**P5 — modular positivity.** \(\mathfrak S_J(z)=6\ln\!\bigl((1+z_c)/(1+z)\bigr)\bigl(1+w(z)\bigr)\geq0\) everywhere.
A relative entropy cannot be negative.
**K5:** dies if the reconstruction puts quintessence before the crossing.

**P6 — the ceiling.** ϱ⊥ ≤ 1.814 at r_c = 1. A clean determination above it
falsifies the branch.

**P7 — the future.** w_∞ = −1/3, a ∝ t, no event horizon, μ_A → ½.

**Explicitly not evidence.** The CMB-lensing anti-alignment: 92.9% of random
smooth transient histories pass it. A class-membership check, nothing more.

---

## 9. Economy

| model | extra dark-history parameters | free functions | new dimensionful constants |
|---|---|---|---|
| flat ΛCDM | 0 | 0 | 1 (Λ) |
| PEDE, vacuum metamorphosis | 0 | 0 | 1 |
| running vacuum | 1 | 0 | 1 |
| CPL | 2 | 0 | 1 |
| interacting DE | 1+ | **1 (the interaction term)** | 1 |
| **modular–Weyl rigid** | **0** | **0** | **1 (χ⊥)** |

Parameter count alone does not distinguish the programme from PEDE or vacuum
metamorphosis. What distinguishes it is the **third column together with what one
constant buys**: in ΛCDM, one constant gives you a constant; here, one constant
gives you an entire history, its equation of state, its running, its phase
portrait, its future, and its perturbation operator — all locked to each other by
a single algebraic identity.

That is the compression claim, and it is the honest one.

---

## 10. What is implementation, not gap

In the Schrödinger analogy: the wave equation was complete before anyone knew the
helium Hamiltonian. These are the corresponding open implementations.

**I1 — the response map.** Construct the natural quadratic map
ℜ_Σ: Sym²(T^{J-odd}𝒮) → Γ(S²T\*D) sending a horizontal state tangent to
spacetime stress, satisfying naturality, modular evenness, central blindness,
conservation, and charge compatibility, with FLRW reduction u^au^bT^X_ab =
χ⊥G^BKM(X,X). This is a classification-of-natural-operators problem, not an
arbitrary functional.

**I2 — the physical score.** Which local J-odd scale deformation realises Q.
Candidate: the null-pair grading at a codimension-two cut.

**I3 — the spacetime lift.** The Witten complex is internal to the state
manifold. Lifting it to a Lorentzian perturbation system remains open, and a
canonical sigma model provably cannot do it (`[NEGATIVE]`: imposing the soldering
demands H² ∝ tanh θ, hence H² < 0 across the whole pre-crossing branch).

**I4 — the value of κ.** §7. Either it comes out ½, and r_c = 1 is predicted, or
χ⊥ is measured. Both are complete theories.

None of these is a free parameter. Each is a construction whose absence leaves
the equations intact and the predictions unchanged.

---

## 11. The stopping declaration

Against §1:

- **(a) derived:** R6, R7, R9, R10, R12–R17, and the whole of §§3–5, from P alone.
- **(b) structural choice:** one — rank-one binary closure.
- **(c) constants of nature:** two — ϱ⊥ (dimensionless, measured 1.0 ± 0.2) and χ⊥ (dimensionful, measured such that r_c = 1).
- **(d) free functions:** **none.**
- **failure modes:** five, registered in §8.

> **The equation set is closed. What remains is implementation and measurement.**

The theory can now be shared, tested, and killed. That is what "finished" means
for a physical theory — not that every constant has been derived from nothing,
which is not a thing any theory has ever done, but that the constants are of a
recognised type, the forms are derived, and the predictions can fail.

---

## Appendix — the one-line summary

$$\boxed{\;\langle Q^2\rangle = 1 \;\Longrightarrow\; \eta^2 + g = 1 \;\Longrightarrow\; 9(1+w_X)^2 + 6\frac{dw_X}{dN} = 4\varrho_\perp^2\;}$$

A normalised binary score, soldered to Weyl scale at rate ϱ⊥ and converted to
stress by stiffness χ⊥, traverses one half-turn of the unit circle. That
half-turn is the history of dark energy.
