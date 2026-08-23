# Scale as a Modular Observable

## A parameter-free derivation of the late-time expansion history from causal-cut information geometry

**Thomas Ruble**
**21 August 2026**

---

**Status.** Working research monograph; not peer reviewed. Claims carry one of:
`[STANDARD]` (established in the cited literature), `[THEOREM]` (proved here or
in the appendix), `[IDENTIFICATION]` (a physical hypothesis about which
mathematical structure nature realises), `[NEGATIVE]` (a computed no-go),
`[OPEN]`. All numerical claims are reproduced by `receipts_closure.py`,
`receipts_transparency_fold.py`, and the `P1/` analysis package.

**What is and is not closed.** The **homogeneous background sector is closed**:
zero free dimensionless constants, zero free dimensionful constants, zero free
functions, one structural identification. The **perturbation sector is open**: a
covariant stress tensor obtained by metric variation has not been constructed,
and conservation is imposed rather than derived. The **observational status is
viability, not discovery**: the model improves on flat ΛCDM by Δχ² = −3.38 at
zero parameter cost against DESI DR2 BAO + Pantheon+, which is modest,
background-only, and partly retrodictive.

---

## Abstract

Under standard causality and regularity hypotheses, the causal order of a
spacetime determines its conformal structure but not its scale. The missing
datum is a positive section σ of the conformal density bundle 𝓔[1]. This
monograph develops the hypothesis that σ is soldered to an independently defined
quantum-statistical object: the relative modular state of a causal region.

The construction proceeds from a single structural identification — that the
homogeneous modular quotient at a codimension-two causal cut is the chirality
grading of the cut's two-dimensional Lorentzian normal plane. From this, the
following are derived rather than assumed: the exact functional form of the dark
energy density, the coefficient relating modular polarisation to Weyl scale
(ϱ⊥ = 1), the constitutive stiffness converting information-geometric response to
stress, and the capacity-to-entropy ratio of the crossing horizon (γ = 1). The
result is a late-time expansion history with **no free parameters** beyond those
already present in flat ΛCDM, and **one fewer dimensionful constant** (ΛCDM
carries Λ; this carries none).

The dark energy density is retyped as the Jacobian between the two flat affine
coordinate systems of a binary information geometry, pulled back along conformal
scale. The equation of state obeys an exact differential invariant,
9(1+w)² + 6 dw/dN = 4, which is the normalisation ⟨Q²⟩ = 1 written in
cosmological variables. The associated phase flow is the canonical saddle-node
normal form, so a single density maximum, a single w = −1 crossing, and a single
finite acceleration episode are one structural statement rather than three fitted
events. The perturbation operator is not chosen but generated: it is the Witten
Laplacian of the binary statistical manifold, reflectionless with exactly one
bound state.

Quantitative predictions include z_c = 0.34179, (w₀, w_a) = (−0.80945, −0.61221),
q₀ = −0.33690, acceleration entry at z = 0.78569 and exit at a/a₀ = 11.787, and
the capacity ratio γ = 1, which is measured cosmologically as 1.025 with 1σ range
[0.941, 1.088].

---

# Part I — Motivation and framing

## 1. The kind of question being asked

Standard late-time cosmology asks: *what fluid or field must be added to the
stress tensor to reproduce the observed expansion history?* Answers to that
question are constrained by data but not by structure, which is why the field
contains many phenomenologically adequate models — CPL, PEDE, vacuum
metamorphosis, running vacuum, sign-switching Λ, interacting dark energy — with
no principle selecting among them.

This programme asks a prior question: **what mathematical type is cosmic
expansion, and what kind of object can source it?**

The motivation is a theorem. `[STANDARD]` The causal order of a distinguishing
spacetime determines its topology, differential structure, and conformal
structure, but not its metric scale [1,2]. A conformal manifold (M, [g]) becomes
a metric manifold only after a choice of scale,

$$g_{\rm phys} = \sigma^{-2}\boldsymbol{g}, \qquad \sigma \in \Gamma(\mathcal{E}[1])$$

This means that in any theory taking causal order as primitive, **scale is a
separate register with its own possible dynamics**. The question of what sources
it is not the same question as what sources curvature, and the two need not have
the same answer or even the same mathematical type.

The hypothesis developed here is that the scale register is soldered to the
*modular* structure of the causal region — the Tomita–Takesaki data of the
region's algebra and state. The dark sector is then not a fluid inserted into
spacetime but the gravitational image of an information-geometric response.

## 2. The elimination test

A retyping is only content if the new variable is independently constructible.
The test used throughout:

| | |
|---|---|
| θ inferred only from H(z) | ⟹ a relabelled effective fluid |
| θ constructed from causal-state algebra, predicting H(z) | ⟹ new physical structure |

Sections 6–8 construct θ from the modular data of a causal cut without reference
to any expansion history. Section 12 reports what the resulting prediction is
worth against data.

---

# Part II — Notation

## 3. Symbols

| symbol | meaning | status |
|---|---|---|
| (M, [g]) | conformal spacetime | standard |
| σ ∈ Γ(𝓔[1]) | scale section; g_phys = σ⁻²**g** | standard |
| N = ln(a/a_c) = −ln(σ/σ_c) | Weyl e-fold coordinate | exact in FLRW |
| I_A = ¼ D_A σ | scale tractor (Thomas-D of σ) | standard |
| P_ab, J = P^a_a | Schouten tensor and trace | standard |
| 𝒜(𝒪), ω | causal-region von Neumann algebra and state | standard |
| Δ_ω, J_ω | modular operator and conjugation | standard |
| s | vertical modular automorphism parameter | standard |
| η_A | geometric horizon rapidity potential | exact when flow is geometric |
| μ_A = (1−q)/2 | running horizon index, dη_A/dN | exact in FLRW |
| θ | horizontal relative modular polarisation | derived (§7) |
| Q | normalised J-odd chirality grade, Q² = 1 | **identification** (§5) |
| η = ⟨Q⟩ | mixture (m-affine) coordinate | exact |
| g^BKM = Var(Q) | Bogoliubov–Kubo–Mori metric | standard |
| 𝒳_σ | pullback scale susceptibility | defined (§9) |
| ϱ⊥ = dθ/dN | scale-modular soldering coefficient | **derived = 1** (§8) |
| C_E = Var(K) | entanglement capacity | standard |
| γ_⊥,c = C_E/(S/k_B) | capacity-to-entropy ratio at the cut | **derived = 1** (§10) |
| ρ_\*, N_c | peak dark density, self-dual epoch | derived |
| Λ_res | global flux residual | sector datum, set to 0 |

## 4. Conventions

Signature (−,+,+,+); n = 4. Overdot is d/dt, prime is d/dN unless stated.
Benchmark: Ω_m0 = 0.310598, Ω_r0 = 9.15 × 10⁻⁵, spatial flatness, Λ_res = 0,
expanding branch. ρ_crit = 3c²H²/(8πG). Entropies in nats (k_B = 1) where
convenient.

---

# Part III — Structural input

## 5. The postulate

There is exactly one, and it is a statement about which mathematical structure
the homogeneous modular sector realises.

> **P (Normal-chirality closure).** `[IDENTIFICATION]`
> A codimension-two causal cut Σ has a two-dimensional Lorentzian normal plane
> N(Σ) = L₊ ⊕ L₋. The homogeneous, J-odd modular quotient at Σ is the chirality
> grading of that plane,
> $$Q = P_+ - P_-, \qquad Q^2 = \mathbf{1}, \qquad JQJ = -Q$$
> and modular flow at Σ is geometric (the boost of the normal plane).

**Why this is one identification, not several.** Q² = 1 is automatic once Q is
the difference of complementary orthogonal projectors: (P₊−P₋)² = P₊ + P₋ = 1.
JQJ = −Q is automatic because the modular conjugation exchanges the two null
directions. That modular flow is geometric is a theorem for a wedge in the
Minkowski vacuum (Bisognano–Wichmann [6]) and for a CFT ball in the vacuum
(Casini–Huerta–Myers [7]); for a dynamical FLRW apparent horizon it is the
assumption.

**What its type is.** This is a selection among representations, of the same kind
as "spacetime has three spatial dimensions" or "the gauge group is
SU(3)×SU(2)×U(1)". It is not a fitted number and it has no continuous freedom.

**Why it is the minimal choice.** The cut supplies exactly two null normal
directions. A rank-one binary is the smallest structure capable of carrying a
nontrivial J-odd scalar response, and the null pair is the only such structure
the geometry provides.

**Additional sector data.** `[SECTOR]` Spatial flatness, Λ_res = 0, the expanding
branch, and separate conservation of the dark and ordinary sectors. These label
global superselection choices and state-selection data, not tunable parameters.
Separate conservation is equivalent to the statement that the modular functional
carries no direct matter coupling; it is an assumption and should be listed as
one.

---

# Part IV — The derivation chain

Each result below follows from its predecessors. Cosmological data enter at only
one point (§8, through Ω_m) and nowhere else.

## 6. Binary information geometry `[THEOREM]`

From P, the state family generated by Q is the rank-one exponential family

$$\rho_\theta = \frac{e^{\theta Q}}{2\cosh\theta}, \qquad \Psi(\theta) = \ln\operatorname{Tr}e^{\theta Q} = \ln(2\cosh\theta)$$

Ψ is the log-partition function; its first two derivatives give the dual affine
coordinate and the metric of the dually flat structure [17]:

$$\eta = \Psi'(\theta) = \langle Q\rangle = \tanh\theta, \qquad g = \Psi''(\theta) = \operatorname{Var}(Q) = \operatorname{sech}^2\theta$$

and the normalisation Q² = 1 becomes the **master identity**

$$\boxed{\;\eta^2 + g = \langle Q^2\rangle = 1\;}$$

**This single identity carries the entire construction.** It appears in five
registers, and they are the same statement:

| register | form |
|---|---|
| algebraic | ⟨Q²⟩ = 1 |
| geometric | (η, √g) lies on the unit circle |
| dynamical | η′ = 1 − η², a Riccati equation |
| cosmological | 9(1+w_X)² + 6 dw_X/dN = 4ϱ⊥² (§13) |
| spectral | η² + η′ = 1, the supersymmetry condition (§15) |

**Metric uniqueness.** `[STANDARD]` Čencov's theorem fixes the classical Fisher
metric up to a global scale under sufficient-statistic invariance [16]. Petz
classified the quantum monotone metrics; monotonicity alone does *not* select one
[15]. BKM is distinguished, up to constant multiple, as the Hessian of Umegaki
relative entropy and as the unique monotone metric for which the exponential and
mixture connections are mutually dual [17,18]. **None of these theorems fixes the
gravitational conversion to energy density**; that requires §§9–11.

## 7. The soldering law `[THEOREM]`

Let σ₁, σ₂ be two scale sections with associated causal-region states, and let

$$u_t = [D\omega_{\sigma_2} : D\omega_{\sigma_1}]_t$$

be the Connes cocycle comparing them. Under P the reduced cocycle has a single
noncentral generator, so modulo the centre

$$u_t \simeq \exp\{it[\theta(\sigma_2,\sigma_1)Q + c\,\mathbf{1}]\}$$

Weyl covariance requires θ to depend only on the ratio r = σ₂/σ₁ (no preferred
scale exists). Connes' chain rule then becomes multiplicative on the reduced
generators, and matching noncentral parts gives Cauchy's exponential–additive
equation

$$\theta(r_1 r_2) = \theta(r_1) + \theta(r_2)$$

With measurability — which follows from σ-weak continuity of the cocycle in t;
continuity in r is not required — the only solutions are

$$\boxed{\;\theta(r) = -\varrho_\perp \ln r \;\Longleftrightarrow\; \theta = \varrho_\perp(N - N_c)\;}$$

**Affine soldering is derived, not postulated.** Cauchy's equation admits a
one-parameter family, and ϱ⊥ *is* that parameter; no further work on the cocycle
can fix its value. N_c is the integration constant, fixed intrinsically in §12.

## 8. ϱ⊥ = 1 `[THEOREM, given P]`

Two independent facts combine.

**(a) Integrality.** The normal pair L₊ ⊕ L₋ carries characters e^{±θ}; the scale
line carries the fundamental pair 𝓔[1] ⊕ 𝓔[−1] with characters e^{±N}.
Equivariant soldering of the two pairs forces e^{±θ} = e^{±(N−N_c)}. A value
ϱ⊥ = n corresponds to the n-th tensor power 𝓔[n] ⊕ 𝓔[−n]. Hence

$$\varrho_\perp \in \mathbb{Z}^+$$

This converts a continuous coefficient into a discrete selection, but does not by
itself select the fundamental representation.

**(b) The existence ceiling.** Flat normalisation on the response-normalised
branch requires r_c e^{3x} sech²(ϱ⊥x) = T_m with x = −N_c and
T_m = (1−Ω_m−Ω_r)/Ω_m. Since d ln F/dx = 3 − 2ϱ⊥ tanh(ϱ⊥x), there is exactly one
root for ϱ⊥ ≤ 3/2 and two-or-none above. The double root gives a closed-form
ceiling:

$$\frac{T_m}{r_c} = \left(1 - \frac{9}{4\varrho_\perp^2}\right)\exp\left[\frac{3}{\varrho_\perp}\operatorname{artanh}\frac{3}{2\varrho_\perp}\right], \qquad \varrho_\perp > \tfrac32$$

| Ω_m | ϱ⊥^max | admissible integers |
|---|---|---|
| 0.280 | 1.6962 | **{1}** |
| 0.310598 | 1.8141 | **{1}** |
| 0.330 | 1.9060 | **{1}** |
| 0.34685 | 2.0000 | {1, 2} |

ϱ⊥ = 2 first becomes admissible at Ω_m = 0.34685, which is 3.8σ from the measured
0.3086 ± 0.010 and is excluded by direct fit at Δχ² = 60.

$$\boxed{\;\text{integrality} + \text{ceiling} + \Omega_m \;\Longrightarrow\; \varrho_\perp = 1 \text{ uniquely}\;}$$

This is the sole point at which cosmological data enter the derivation, and it
enters only to exclude ϱ⊥ = 2.

## 9. The constitutive law

The scale susceptibility is the pullback of the BKM metric along
Φ: ℝ_Weyl → 𝒮(𝒜):

$$\mathcal{X}_\sigma = g^{\rm BKM}\left(\frac{d\theta}{dN}\right)^2 = \varrho_\perp^2\operatorname{sech}^2[\varrho_\perp(N-N_c)]$$

Note that 𝒳_σ is a quadratic differential, not a scalar: the invariant object is
𝒳_σ dN² = sech²θ dθ², in which ϱ⊥ does not appear. ϱ⊥ specifies how Weyl scale
parameterises a fixed path; it does not change the path.

The constitutive hypothesis is that the dark energy density is the **modular
free-energy stiffness per causal-diamond volume**. For a reference KMS state ρ_c
with physical modular Hamiltonian 𝓗_c = k_B T_c K_c, the nonequilibrium free
energy satisfies exactly

$$F_c(\rho) - F_c(\rho_c) = k_B T_c\, S(\rho\,\|\,\rho_c)$$

and for a nearby state S(ω_{N+dN}‖ω_N) = ½ G^⊥_NN dN² + O(dN³). Hence

$$\boxed{\;\rho_X(N) = \frac{k_B T_c}{2V_c}\,G^{\perp}_{NN}(N), \qquad G^{\perp}_{NN} = C_{\perp,c}\,\varrho_\perp^2\operatorname{sech}^2\theta\;}$$

where C_⊥,c is the extensive BKM norm of the selected horizontal tangent. The
binary quotient supplies the normalised shape; the full causal-diamond state
supplies the number of participating units.

**This is not a local spacetime kinetic action.** It is a Dirichlet functional on
a curve in state space, Γ_⊥ = (k_B T_c/2)∫dN G^BKM(𝒟_Nω, 𝒟_Nω). The distinction
matters: the canonical-sigma-model no-go of §17 does not apply to it.

## 10. γ = 1 `[THEOREM, given P]`

Two steps.

**(a) The horizontal BKM norm is the entanglement capacity.** `[THEOREM]` For the
exponential family generated by rescaling the modular Hamiltonian,
ρ(λ) = e^{−(1+λ)K₀}/Z(λ),

$$G^{\rm BKM}_{\lambda\lambda}\Big|_{0} = \frac{\partial^2 \ln Z}{\partial\lambda^2}\Big|_{0} = \operatorname{Var}(K_0) = \operatorname{Var}(K) = C_E$$

verified numerically on random modular spectra to 10⁻⁶. The horizontal direction
*is* the modular-rescaling direction, because a Weyl rescaling changes the
diamond radius R and hence its temperature T = ħc/2πR and hence β. So
C_⊥,c = C_E,c is an identity of exponential families, not a hypothesis.

**(b) The ratio is a thermodynamic exponent.** With C_E = Var(K) and
S/k_B = ⟨K⟩,

$$\boxed{\;\gamma_{\perp,c} \equiv \frac{C_{\perp,c}}{S_c/k_B} = \frac{\operatorname{Var}(K)}{\langle K\rangle} = \frac{C}{S} = \frac{d\ln S}{d\ln T}\;}$$

so if S ∝ T^a then γ = a:

| sector | S ∝ | γ |
|---|---|---|
| thermal CFT, d = 4 (bulk matter) | T³ | 3 |
| horizon varied by size (Schwarzschild-like) | T⁻² | −2 |
| **two-dimensional CFT** | **T** | **1** |

γ = 1 holds if and only if S ∝ T, which among conformal sectors is unique to
d = 2 (γ = d − 1 = 1).

**The horizontal sector is two-dimensional.** By P, the normal plane is 2D and
Lorentzian and modular flow there is the boost. The transverse directions along Σ
are FLRW-symmetry-invariant and **J-even**, so they carry no J-odd horizontal
tangent and drop out of G^⊥ identically. The horizontal sector is therefore the
chiral algebra of the normal plane. Cardy's formula for a 2D CFT at fixed spatial
length L gives F = −πcL/6β², hence

$$S = \frac{\pi c L}{3}T, \qquad C = T\frac{dS}{dT} = S \qquad\Longrightarrow\qquad \gamma_{\perp,c} = 1$$

**Fixed L is the correct condition**, because the horizontal deformation is by
definition at fixed localisation. Varying L is the *vertical* direction, which
gives S ∝ R², T ∝ 1/R, γ = −2. The two directions have different capacity ratios;
conflating them is precisely the error corrected in §21.

## 11. The dimensional bridge `[THEOREM]`

The remaining question is what converts a dimensionless information metric into
an energy density. The crossing causal diamond supplies it, with no new constant.

For the spatially flat FLRW apparent horizon, R_c = c/H_c, and

$$\frac{S_c}{k_B} = \frac{A_c c^3}{4G\hbar} = \frac{\pi R_c^2 c^3}{G\hbar}, \qquad k_B T_c = \frac{\hbar c}{2\pi R_c}$$

so that

$$k_B T_c \frac{S_c}{k_B} = \frac{c^4 R_c}{2G} = E_{\rm MS,c}, \qquad \frac{E_{\rm MS,c}}{V_c} = \frac{3c^2H_c^2}{8\pi G} = \rho_{\rm crit,c}$$

$$\boxed{\;\frac{k_B T_c}{V_c}\cdot\frac{S_c}{k_B} = \rho_{\rm crit,c}\;}$$

ħ, k_B, G and c all cancel. E_MS is the Misner–Sharp energy, and the middle
equality is the Friedmann marginality identity 2GE_MS/(c⁴R_A) = 1 at a flat FLRW
apparent horizon — a statement that the causal radius is exactly the radius at
which enclosed gravitational energy saturates the spherical compactness relation.
It is *not* a claim that the observable universe is a Schwarzschild black hole;
the two share an area–temperature–energy normalisation because both are marginal
causal-information surfaces.

The temperature here is the **horizontal** modular temperature in the canonical
2π boost normalisation. It must not be confused with the running **vertical**
Kodama–Hayward temperature T_KH = μ_A T_c [23,24]. Using the vertical temperature
in the horizontal channel yields γϱ⊥²/2 = μ_A/2 and r_c = 1/4, which is excluded
by data — a useful check that the vertical/horizontal distinction is doing real
work.

## 12. The closed source law

Combining §§9–11:

$$\boxed{\;\rho_X(N) = \frac{\gamma_{\perp,c}\varrho_\perp^2}{2}\,\rho_{\rm crit,c}\,\operatorname{sech}^2[\varrho_\perp(N-N_c)]\;}$$

At the self-dual point θ = 0 this gives the crossing normalisation

$$\Omega_{X,c} \equiv \frac{\rho_*}{\rho_{\rm crit,c}} = \frac{\gamma_{\perp,c}\varrho_\perp^2}{2} \;\overset{\gamma=\varrho_\perp=1}{=}\; \frac{1}{2}$$

and flatness, ρ_crit,c = ρ_ord,c + ρ_\*, then forces

$$\boxed{\;\rho_X(N_c) = \rho_{\rm ordinary}(N_c)\;}$$

**exactly**, where "ordinary" means the complete non-dark sector. Relative to dust
alone the ratio is 1/(1 − 2Ω_r,c) = 1.000395 at the benchmark: the wall balances
the dark response against all ordinary causal energy, not against dust in
isolation. The factor of ½ is the Taylor coefficient of the quadratic free-energy
Hessian; every other ratio in the chain is unity in the Einstein-capacity class.

**N_c is fixed intrinsically.** Since JQJ = −Q, the modular reflection of ρ_θ is
ρ_{−θ}, and the symmetrized Umegaki relative entropy is [19]

$$\mathfrak{S}_J(\theta) = S(\rho_\theta\|\rho_{-\theta}) + S(\rho_{-\theta}\|\rho_\theta) = 4\theta\tanh\theta$$

which vanishes only at θ = 0, is strictly increasing in |θ|, and has Hessian
I_J(0) = 8 = 2γ^BKM(ΔX, ΔX) on the reflected tangent ΔX = 2X_\*. **N_c is the
unique global minimum of an intrinsic modular functional**, not a chosen offset.
Its cosmic date is then fixed by flatness.

---

# Part V — The background cosmology

## 13. The shape invariant `[THEOREM]`

Separate conservation, dρ_X/dN = −3(1+w_X)ρ_X, applied to §12 gives

$$3(1+w_X) = 2\varrho_\perp\eta = 2\varrho_\perp\tanh\theta$$

and the master identity η² + g = 1 becomes

$$\boxed{\;9(1+w_X)^2 + 6\frac{dw_X}{dN} = 4\varrho_\perp^2 = 4\;}$$

This is not a coincidence among hyperbolic functions. It is ⟨Q²⟩ = 1 written in
cosmological variables. Equivalent forms:

$$\frac{\rho_X}{\rho_*} + \frac{1}{4\varrho_\perp^2}\left(\frac{d\ln\rho_X}{dN}\right)^2 = 1, \qquad \frac{d^2}{dN^2}\ln\frac{\rho_X}{\rho_*} + 2\varrho_\perp^2\frac{\rho_X}{\rho_*} = 0$$

The invariant is independent of the amplitude, so it measures ϱ⊥ separately from
the normalisation.

## 14. Phase flow, the acceleration episode, and the futures `[THEOREM]`

Setting X := 1 + w_X and eliminating θ:

$$X' = \frac{2}{3}\varrho_\perp^2 - \frac{3}{2}X^2$$

which under X = (2ϱ⊥/3)û, τ = ϱ⊥N becomes dû/dτ = 1 − û², the **canonical
saddle-node (fold) normal form**. The coefficient 3/2 is fixed by gravity (the 3
in 3(1+w)); the unfolding parameter is (2/3)ϱ⊥². Fixed points:

$$w_\pm = -1 \pm \frac{2\varrho_\perp}{3} \;\overset{\varrho_\perp=1}{=}\; -\frac{5}{3},\; -\frac{1}{3}$$

and the history is the unique heteroclinic orbit joining them. **One density
maximum, one w = −1 crossing, and one connected acceleration interval are one
structural statement**, not three fitted events. At ϱ⊥ = 0 the fixed points merge
and the dark sector disappears.

### 14.1 Why acceleration turns on, and why it turns off

The future fixed point is w_∞ = −1 + 2ϱ⊥/3. For ϱ⊥ = 1 this is **exactly
−1/3**, the threshold at which a dark-dominated universe has q = 0. Hence:

| ϱ⊥ | future | permanent event horizon |
|---|---|---|
| < 1 | perpetual power-law acceleration | yes |
| **= 1** | **critical coasting, a ∝ t** | **marginally absent** |
| > 1 | eventual deceleration | no |

ϱ⊥ = 1 is the separatrix between three causal futures.

The acceleration episode is **finite and unique**, and the mechanism for its
termination is structural. Asymptotically ρ_X ∝ a⁻² with w_X → −1/3, so
ρ_X + 3p_X → 0: the dark sector's *active gravitational* (Komar) density vanishes
even though its energy density still dominates. The residual matter, decaying as
a⁻³, then controls the Komar density and returns q to 0⁺. At the benchmark:

$$z_{\rm entry} = 0.785694, \qquad (a/a_0)_{\rm exit} = 11.7865, \qquad \text{duration } 3.047 \text{ e-folds}$$

At exit, 1 + 3w_X = −1.59 × 10⁻², matter fraction 1.57 × 10⁻². The dark sector
does not disappear; it stops gravitating actively.

## 15. Geometric unification of the history

`[THEOREM]` Because η² + g = 1, the pair (η, √g) = (tanh θ, sech θ) traces the
unit circle. Setting η = sin φ, √g = cos φ determines

$$\varphi = \operatorname{gd}(\theta) = \arctan(\sinh\theta), \qquad d\varphi = \operatorname{sech}\theta\,d\theta = ds_{\rm Fisher}$$

the Gudermannian function. The Fisher arc length *is* the circular angle, and the
complete history sweeps φ from −π/2 to +π/2:

$$L_F = \int_{-\infty}^{\infty}\operatorname{sech}\theta\,d\theta = \pi = \int_0^1\frac{dp}{\sqrt{p(1-p)}}$$

which is exactly the diameter of the binary state simplex in the Fisher metric.
The crossover is a **complete traversal from one extremal binary state to the
other**, and its length is independent of ϱ⊥. In this parameterisation

$$\frac{\rho_X}{\rho_*} = \cos^2\varphi, \qquad \frac{3(1+w_X)}{2\varrho_\perp} = \sin\varphi$$

φ = 0 is simultaneously the density maximum, the w_X = −1 crossing, the modular
self-dual point, the maximum of the BKM metric, and the epoch at which the score
carries exactly one bit (S = ln 2).

## 16. Tractor form of the vertical sector `[THEOREM]`

`[STANDARD]` For a scale σ, the trace-free Einstein equation is equivalent to a
transport law for the scale tractor, and the trace to a norm law [3,4,5,51]:

$$\big(\nabla_a\nabla_b + P_{ab}\big)_0\,\sigma = \frac{4\pi G}{c^4}\,\sigma\big(T^m_{ab} + T^X_{ab}\big)^\circ, \qquad I^2 = \frac{2\pi G}{3c^4}T - \frac{\Lambda_{\rm g}}{3}$$

with I² = −R/12 in four dimensions. `[THEOREM]` For FLRW this gives the exact
identity

$$I^2 = -\mu_A H^2, \qquad \mu_A = \frac{1-q}{2} = \frac{d\eta_A}{dN}$$

verified to 10⁻¹¹ across five decades in redshift: **the vertical horizon-clock
rate is the normalised scale-tractor norm.** The e-fold budget then splits
exactly,

$$dN = d\eta_A + \tfrac14\,d\ln\mathcal{S}_A$$

into horizon-rapidity advance and horizon-information growth. For ϱ⊥ = 1 the
asymptotic split is exactly 1:1 (μ_A → ½, I²/H² → −½, midway between the null
tractor of Minkowski and the value −1 of de Sitter).

**Vacuum blindness.** `[THEOREM]` A central shift K ↦ K + α**1** leaves the
normalised state, its relative entropy, its BKM metric, and Var(K) unchanged; the
corresponding stress shift T_ab ↦ T_ab + λg_ab is annihilated by the trace-free
source equation. An additive vacuum offset therefore has **zero horizontal BKM
length** and produces no local source. The local vacuum problem is not solved by
cancelling large numbers; the offset lies in a direction to which the local
response is blind. The residual global lift Λ_g remains a separate problem and is
set to zero as a sector choice.

---

# Part VI — The perturbation sector

## 17. Negative results that constrain the completion

These are part of the content: they prevent the sech² profile from being attached
indiscriminately to every equation.

**N1 — the matter-growth operator is not of Pöschl–Teller type.** `[NEGATIVE]`
Under ψ = D a√H the growth equation becomes ψ″ = W(N)ψ with
W = ¼(2+h)² + ½h′ + (3/2)Ω_m. Against a distance-matched comparator, ΔW/Ω_X
spans −179 to +0.27, and a free three-parameter sech² fit leaves a 63.9%
fractional residual. Ordinary growth is not the spectral problem.

**N2 — no single-field completion.** `[NEGATIVE]` For a canonical scalar,
z² ∝ 1 + w_X = (2ϱ⊥/3)tanh θ, which is negative on the entire pre-crossing
branch: a ghost over a cosmological epoch, not a point defect. Near θ = 0,
z ∼ |θ|^{1/2} and z″/z → −1/(4θ²) — the inverse-square potential at exactly the
critical coupling 1/4 for fall-to-the-centre [30]. The crossing is marginal in a
precise sense, which is why small deformations of one-field models do not cure it
[28].

**N3 — tractors cannot supply the stiffness.** `[NEGATIVE]` Φ\*G^BKM ∝ I·I fails
(the ratio spans two decades). I·I is a norm built from σ and is vertical; 𝒳_σ is
horizontal. Moreover Weyl and Cotton tensors vanish for FLRW, so the tractor
connection is flat and carries no horizontal information.

**N4 — no canonical sigma model.** `[NEGATIVE]` Imposing the soldering
θ̇ = ϱ⊥H on Γ = ∫√−g[(χ/2)G(θ)(∂θ)² − V] together with the target profile
requires H² = (2ρ_\*/3χϱ⊥)tanh θ, hence H² < 0 across the entire pre-crossing
branch. Exact no-go.

**Consequence.** The completion must be collective, and θ must be typed as a
**collective constitutive coordinate** of a scale-indexed state family — the same
mathematical type as inverse temperature, chemical potential, an order parameter,
or a Berry phase. It is neither a propagating local field (which N4 excludes) nor
a function reconstructed from the metric (which would fail the elimination test).
Its independent definition is the Connes cocycle of §7.

## 18. The perturbation operator is generated, not chosen `[THEOREM]`

Define first-order operators from the information potential itself:

$$\mathcal{A} = \partial_\theta + \eta, \qquad \mathcal{A}^\dagger = -\partial_\theta + \eta$$

Then, using only η² + g = 1:

$$\boxed{\;\mathcal{A}^\dagger\mathcal{A} = -\partial_\theta^2 + 1 - 2\operatorname{sech}^2\theta, \qquad \mathcal{A}\mathcal{A}^\dagger = -\partial_\theta^2 + 1\;}$$

verified to 4 × 10⁻¹⁶. **H₊ is free precisely because ⟨Q²⟩ = 1: the binary
normalisation is the supersymmetry condition.** The ℓ = 1 Pöschl–Teller operator
is therefore the Witten Laplacian of the binary statistical manifold, not a
hypothesis about a perturbation sector.

Consequences, all forced:

- **Zero mode.** 𝒜ψ₀ = 0 gives ψ₀ = sech θ/√2, with |ψ₀|² = ½ g: the BKM metric
  is twice the bound-state probability density.
- **Reflectionless.** ψ_k = 𝒜†e^{ikθ} = (−ik + tanh θ)e^{ikθ} has no e^{−ikθ}
  component at either end, so R(k) ≡ 0 for all k [29]. There *is* a transmitted
  continuum; reflectionlessness does not remove continuum degrees of freedom.
- **Witten index 1**, hence by Levinson's theorem a total transmission phase of π.
  The phase density in log-momentum is sech(s), the same function as the Fisher
  line element in position — a consequence of sech being self-reciprocal under
  Fourier transform.
- **The pair is generated.** The 1-D statistical manifold has de Rham complex
  Ω⁰ ⊕ Ω¹; Witten deformation by Ψ turns it into a two-component Dirac operator
  𝒟_Ψ with 𝒟_Ψ² = diag(H₋, H₊). The perturbative pair is **form parity**,
  canonically generated by the binary line — it is *not* the binary outcomes and
  must not be identified with Q.

## 19. Directedness `[THEOREM]`

The symmetrized relative entropy of §12 takes the cosmological form

$$\mathfrak{S}_J = 4\theta\eta = 6(N-N_c)(1+w_X) \;\ge\; 0$$

in which ϱ⊥ cancels. Non-negativity of relative entropy therefore **forces**

$$N < N_c \Rightarrow w_X < -1, \qquad N > N_c \Rightarrow w_X > -1$$

The phantom→quintessence orientation of the crossover, relative to increasing
Weyl scale, is a theorem rather than an input; the time-reversed pulse is
forbidden. Independently, the ℓ = 1 transmission amplitude
t(k) = −(α−ik)/(α+ik) has its single pole at k = +iα, the upper half plane —
retarded, not advanced — and because the potential is reflectionless that pole is
the entire scattering content.

**Scope.** These fix the orientation of the crossover *relative to* increasing N.
They do not derive why the universe occupies the expanding branch, nor does the
pole's half-plane explain why nature selects retarded response; that is a causal
boundary condition.

## 20. What remains open in this sector `[OPEN]`

The Dirichlet functional Γ_⊥ of §9 evades N4 because it is a one-dimensional
energy along a state trajectory rather than a spacetime action. For the same
reason it does **not** yield T^X_ab by metric variation, so conservation is
imposed rather than derived, and the lift of the Witten complex to a Lorentzian
cosmological perturbation system has not been constructed. The required object is
a natural quadratic response map

$$\mathfrak{R}_\Sigma: \operatorname{Sym}^2\!\big(T^{J\text{-odd}}_{\omega_\Sigma}\mathcal{S}\big) \longrightarrow \Gamma\big(S^2T^*D_\Sigma\big), \qquad T^X_{ab} = \mathfrak{R}_\Sigma(X,X)_{ab}$$

satisfying naturality under causal embeddings, modular evenness, central
blindness, conservation on the state equations, charge compatibility with the
gravitational Noether charge, and the FLRW reduction u^au^bT^X_ab = χ⊥ G^BKM(X,X).
This is a classification-of-natural-operators problem, not an arbitrary
functional.

---

# Part VII — Predictions

## 21. The closed benchmark

Ω_m0 = 0.310598, Ω_r0 = 9.15 × 10⁻⁵, ϱ⊥ = γ_⊥,c = 1, Λ_res = 0, k = 0.
**Zero free dark parameters.**

| quantity | value |
|---|---|
| Ω_X,c = γϱ⊥²/2 | 0.500000000 (exactly ½) |
| N_c | −0.2940066 |
| z_c | 0.3417927 |
| ρ_\*/ρ_crit,0 | 0.7506311 |
| ρ_\*/ρ_ordinary(N_c) | 1.000000000 (exactly 1) |
| ρ_\*/ρ_m(N_c) | 1.0003953 = 1/(1−2Ω_r,c) |
| Ω_r,c | 1.9756 × 10⁻⁴ |
| w_X(0) | −0.8094545 |
| w_a (CPL tangent) | −0.6122053 |
| q₀ | −0.3369025 |
| j₀ | −0.1085454 |
| acceleration entry | z = 0.7856935 |
| acceleration exit | a/a₀ = 11.78652 |
| 9(1+w)² + 6w′ | 4.000000000 (exactly 4) |
| w_∞ | −1/3 exactly; a(t) ∝ t; no event horizon |

## 22. Falsifiable predictions and kill conditions

**P1 — the shape invariant.** 9(1+w(z))² + 6 dw/dN = 4 at every z, tested bin by
bin against non-parametric w(z) reconstructions. **K1:** fails if the
reconstructed combination varies with z beyond errors. *See §24 for the
demonstrated limitation of this test.*

**P2 — the local tangent.** (w₀, w_a) = (−0.80945, −0.61221), zero free
parameters. **K2:** fails if a clean posterior excludes the curve
w_a = (3/2)(1+w₀)² − (2/3)ϱ⊥² for all admissible ϱ⊥.

**P3 — the crossover epoch.** z_c = 0.34179, fixed by flatness and not adjusted
after fitting distances. **K3:** fails if a direct reconstruction places the
w = −1 crossing far from the flatness-determined value.

**P4 — the equality coincidence.** z(w_X = −1) = z(ρ_X = ρ_\*) = z(ρ_X = ρ_ord).
Generic dark energy separates these; at the DESI CPL best fit they differ by
Δz = 0.019. **K4:** fails if reconstructed equality and the phantom divide
separate beyond errors.

**P5 — the existence ceiling.** ϱ⊥ ≤ ϱ⊥^max(Ω_m, r_c); 1.8141 at the benchmark.
**K5:** a clean, non-boundary-dominated determination above the ceiling falsifies
the branch.

**P6 — modular positivity.** 𝔖_J(z) = 6 ln[(1+z_c)/(1+z)](1+w(z)) ≥ 0 at every z.
**K6:** fails if the reconstruction places quintessence before the crossing.

**P7 — the capacity ratio.** γ_⊥,c = 2Ω_X,c/ϱ⊥² = 1. This is a cross-disciplinary
prediction: the late-time cosmological crossing should exhibit the same
capacity-to-entropy ratio as an Einstein causal horizon. Flatness independently
excludes the thermal-CFT class (γ = 3 ⟹ Ω_X,c = 1.5) and the Schwarzschild class
(γ = 2 ⟹ Ω_X,c = 1). **K7:** fails if γ is measured away from 1.

**P8 — the future.** w_∞ = −1/3, a ∝ t, marginal absence of an event horizon,
asymptotic 1:1 horizon budget, and exactly one finite acceleration episode ending
at a/a₀ ≈ 11.8. Any positive residual floor Λ_res eventually dominates and
restores an event horizon, so exact zero and observational negligibility are
different hypotheses.

**Explicitly not discriminating.** The CMB-lensing response direction. A null
ensemble of 225 smooth positive transient histories, matched to the same early
matter density and high-z distance, found 92.9% with response cosine below −0.90
and a median of −0.969 against the rigid model's −0.972. This is a
class-membership check, not evidence.

---

# Part VIII — Observational status

## 23. Model comparison

DESI DR2 BAO (13 measurements, 7 tracers, within-tracer correlations) [31] plus
Pantheon+ (1580 SNe after z_HD > 0.01 and calibrator removal, full STAT+SYS
covariance) [34]. N_data = 1593. The normalisation c/(H₀r_d) and the supernova
absolute magnitude are profiled analytically. The pipeline reproduces published
ΛCDM constraints: Pantheon+ alone Ω_m = 0.3324 ± 0.018 (published 0.334 ± 0.018);
DESI alone Ω_m = 0.2970 ± 0.0086 and H₀r_d = 101.56 (published 0.2975 ± 0.0086
and 101.54 ± 0.73).

| model | dark params | k | χ² | Δχ² | ΔAIC |
|---|---|---|---|---|---|
| flat ΛCDM | 0 | 3 | 1400.142 | 0 | 0 |
| **this model** | **0** | **3** | **1396.762** | **−3.380** | **−3.380** |
| ϱ⊥ free | 1 | 4 | 1395.596 | −4.545 | −2.545 |
| CPL (w₀, w_a) | 2 | 5 | 1394.980 | −5.162 | −1.162 |
| invariant-constant | 2 | 5 | 1394.868 | −5.274 | −1.274 |
| free-shape sech^p | 3 | 6 | 1394.024 | −6.118 | −0.118 |

The model has the best AIC of the six, buying Δχ² = −3.38 at zero parameter cost.
This is evidence of **viability**, not discovery: it is modest, background-only,
non-nested against ΛCDM, and partly retrodictive.

## 24. Direct parameter determinations

| quantity | prediction | measurement | tension |
|---|---|---|---|
| ϱ⊥ | 1 | 0.800, 1σ [0.575, 0.982] | 1.08σ |
| γ_⊥,c (at ϱ⊥ = 1) | 1 | 1.025, 1σ [0.941, 1.088] | 0.03σ |
| z_c | 0.342 | 0.650, 1σ [0.293, open] | 0.72σ |

The γ constraint was checked against degeneracy with Ω_m: across γ ∈ [0.8, 1.3]
the best-fit Ω_m moves only 0.3277 → 0.3186 — less than its own error — while χ²
swings by 13. The constraint enters through z_c, which sweeps 0.546 → 0.049
across the same range. Fixing Ω_m externally at the Planck value gives
γ = 1.030, 1σ [0.955, 1.099].

**This is a ~7% cosmological determination of a capacity-to-entropy ratio,
consistent with the value predicted by two-dimensional conformal thermodynamics.**

## 25. The demonstrated limitation of P1

`[NEGATIVE]` P1 as originally designated the primary test **cannot be performed
with background data, and this is structural rather than statistical.**

Embed the theory in the family ρ_X ∝ sech^p(β(N−N_c)), for which

$$9X^2 + 6X' = X^2\left(9 - \frac{18}{p}\right) + 2p\beta^2$$

so the invariant is constant if and only if p = 2. Profiling the likelihood in p
against DESI DR2 + Pantheon+ gives **Δχ² = 0.79 across p ∈ [0.05, 20]**, with no
1σ, 2σ or 3σ bound; p = 2 sits at 0.88σ. Adding a Planck acoustic anchor as a
14th BAO point, D_M(z\*)/r_d = 94.32 ± 0.28, changes this to 0.78.

The reason: the data span θ = β(N−N_c) ∈ [−0.42, +0.28], **less than one
transition width**. The exponent p controls the tails of sech^p, and the tails
lie where ρ_X is subdominant. Along the entire degenerate direction w(z) varies by
< 0.03 over the data range while the invariant's value swings by two decades.
Forecast: distinguishing a smooth pulse from a sharp step requires ~3.4× better
data (plausibly DESI-5yr + LSST); distinguishing p = 2 from p = 1 requires ~22×,
which no planned background survey delivers.

**P1 should therefore be demoted from primary test**, and P2, P3, P4, P7 promoted
in its place. If the invariant is testable at all it will be through growth
(fσ₈) or CMB lensing, which weight ρ_X(z) through different functionals — which
makes the perturbation sector (§20) the gate for observation as well as theory.

---

# Part IX — Comparison and economy

## 26. Existing economical competitors

| model | extra dark-history parameters | free functions | new dimensionful constants |
|---|---|---|---|
| flat ΛCDM | 0 | 0 | 1 (Λ) |
| PEDE [35] | 0 | 0 | 1 |
| vacuum metamorphosis [36] | 0 | 0 | 1 |
| running vacuum [37] | 1 | 0 | 1 |
| CPL | 2 | 0 | 1 |
| interacting dark energy | 1+ | **1** (interaction term) | 1 |
| **this model** | **0** | **0** | **0** |

**Parameter count alone does not distinguish this model from PEDE or vacuum
metamorphosis.** Two things do. First, the third column: the stiffness is
relational, χ⊥ = (γϱ⊥²/2)ρ_crit,c, supplied by the crossing diamond rather than
inserted. Second, what one structure buys: the same identity ⟨Q²⟩ = 1 fixes the
background shape, the differential invariant, the crossing count, the future
causal character, the perturbation operator, and the response amplitude, and
these are locked to one another.

## 27. The musical-chairs test

At the homogeneous level every positive ρ_X(a) is representable as an effective
fluid via w_X = −1 − (1/3) d ln ρ_X/dN, and the sech²/tanh family is not new. The
background curve alone is therefore not a paradigm shift. The candidate novelty
is the independent map Φ: ℝ_Weyl → 𝒮(𝒜) and its pullback metric
Φ\*G^BKM = 𝒳_σ(N)dN². The elimination test of §2 is passed to the extent that
§§5–12 construct θ from cocycle data, with cosmology entering only through Ω_m in
§8; it is not yet passed *in practice*, because the explicit computation of
θ(N) from a concretely specified FLRW causal-diamond state family has not been
performed.

---

# Part X — Morgue and open problems

## 28. Claims withdrawn or demoted

Recorded because the record is part of the method.

| former claim | disposition | cause |
|---|---|---|
| KMS strip dimension forces an A₂ three-sheet structure | withdrawn | complexified flow is not a two-parameter miniversal deformation |
| constant tractor norm iff parallel tractor | withdrawn | radiation + Λ is an exact flat-FLRW counterclass |
| the observable universe *is* a Schwarzschild black hole | withdrawn | replaced by the Misner–Sharp marginality identity (§11) |
| 10¹²² is a unit artifact | withdrawn | Λℓ_P² is dimensionless |
| one acceleration sign flip | corrected | one finite interval, with entry and exit (§14.1) |
| horizon boost rate equals horizontal state rate | withdrawn | vertical and horizontal are different tangent directions |
| CMB-lensing anti-alignment is evidence | demoted | 92.9% of smooth transients pass the same test |
| growth equation supplies the transparency operator | withdrawn | N1 |
| a single scalar field realises the crossing | withdrawn | N2 |
| Petz/Čencov fix the gravitational normalisation | withdrawn | they constrain information metrics, not the BKM-to-stress stiffness |
| transparency fixes χ⊥ | withdrawn | χ⊥ multiplies the whole quadratic form; the spectrum is independent of it |
| the neutrino residual is resolved | not established | no direct Boltzmann posterior; proposal-level structured residual only |
| P1 is the primary observational test | demoted | §25 |

Two analysis errors were caught and are recorded: a profile-likelihood
continuation trapped at β → 0 produced a spurious 2.30σ tension in z_c (true
value 0.72σ), and a single-bracket root-finder misread the two-root regime as
"no solution", producing a spurious existence ceiling of 1.57 (true value 1.814).

## 29. Open problems

**Q1 — the response map.** Construct ℜ_Σ of §20 and lift the Witten complex to a
Lorentzian perturbation system. This gates the perturbation sector, the
observational route to the invariant, and any CMB/growth likelihood.

**Q2 — the FLRW self-dual wall.** Prove that modular flow at the self-dual
apparent-horizon cut of a dynamical flat FLRW state is geometric, so that the
horizontal sector is the normal-plane chiral algebra assumed in P. This is the
single identification carrying the γ = 1 derivation.

**Q3 — explicit θ(N).** Compute the Connes cocycle for a concretely specified
FLRW causal-diamond state family and exhibit θ(N) without cosmological input,
completing the elimination test in practice.

**Q4 — Λ_res.** The global flux residual is set to zero as a sector choice.
Manifestly local vacuum sequestering [26,27] removes spacetime-filling
matter-loop vacuum energy from the curvature source and leaves a finite global
flux residual; which flux sector nature selects is not derived here.

**Q5 — the Keller correspondence.** `[RHYME, unresolved]` Reflectionless
potentials are exactly those whose KdV spectral curve is rational; Keller
obstructions live in branched-cover data of a discriminant. Both instantiate
"trivial local invariant, nontrivial global remainder". Whether the ℓ = 1
Pöschl–Teller spectral curve is the Keller curve at the A₂ degeneration is
checkable and unchecked. Note that the programme uses "A₂" only for the genuine
catastrophe-theory folds of §14 and §8(b); generic turning-point, Airy, cusp, KdV
and Dynkin correspondences are not treated as evidence.

## 30. Suggested first steps for a new investigator

1. Run P2, P3, P4 and P6 on published non-parametric w(z) reconstructions. These
   require no new theory and test four predictions from one reconstruction.
2. Build the determination table for ϱ⊥ across DR1/DR2 × supernova compilations ×
   with/without lensing, using ϱ⊥² = [9(1+w₀)² − 6w_a]/4 with real covariances,
   marking boundary-dominated entries against the §8 ceiling.
3. Attack Q2 in a controlled setting first: a driven two-dimensional CFT, then
   holographic balls, then perturbative gravitational crossed-product algebras.
4. Attack Q1 as a classification problem for natural bilinear operators, not by
   guessing an action.

---

# References

[1] Hawking, King, McCarthy, *J. Math. Phys.* **17** (1976) 174.
[2] Malament, *J. Math. Phys.* **18** (1977) 1399.
[3] Bailey, Eastwood, Gover, *Rocky Mountain J. Math.* **24** (1994) 1191.
[4] Curry, Gover, arXiv:1412.7559.
[5] Gover, *J. Geom. Phys.* **60** (2010) 182.
[6] Bisognano, Wichmann, *J. Math. Phys.* **17** (1976) 303.
[7] Casini, Huerta, Myers, arXiv:1102.0440.
[8] Wald, arXiv:gr-qc/9307038.
[9] Jacobson, arXiv:gr-qc/9504004.
[10] Jacobson, arXiv:1505.04753.
[11] Jafferis, Lewkowycz, Maldacena, Suh, arXiv:1512.06431.
[12] Lashkari, Van Raamsdonk, arXiv:1508.00897.
[13] Czech, Lamprou, McCandlish, Sully, arXiv:1712.07123.
[14] Czech et al., arXiv:2305.16384.
[15] Petz, *Linear Algebra Appl.* **244** (1996) 81.
[16] Čencov, *Statistical Decision Rules and Optimal Inference*, AMS (1982).
[17] Amari, Nagaoka, *Methods of Information Geometry*, AMS/Oxford (2000).
[18] Grasselli, Streater, arXiv:math-ph/0006030.
[19] Chatterjee, arXiv:2605.19106.
[20] Jensen, Sorce, Speranza, arXiv:2306.01837.
[21] Faulkner, Speranza, arXiv:2405.00847.
[22] Chandrasekaran, Flanagan, arXiv:2601.07915.
[23] Hayward, arXiv:gr-qc/9710089.
[24] Cai, Kim, arXiv:hep-th/0501055.
[25] Kastor, Ray, Traschen, arXiv:0904.2765.
[26] Kaloper, Padilla, Stefanyszyn, Zahariade, arXiv:1505.01492.
[27] Kaloper, Padilla, arXiv:1606.04958.
[28] Vikman, arXiv:astro-ph/0407107.
[29] Lekner, *Am. J. Phys.* **75** (2007) 1151.
[30] Camblong et al., arXiv:hep-th/0003014.
[31] DESI Collaboration, arXiv:2503.14738.
[32] DESI Collaboration, arXiv:2503.14744.
[33] Scolnic et al., arXiv:2112.03863.
[34] Brout et al., arXiv:2202.04077.
[35] Li, Shafieloo, arXiv:1906.08275.
[36] Parker, Raval, arXiv:gr-qc/0312108.
[37] Solà Peracaula et al., arXiv:2203.13757.
[38] Witten, *Nucl. Phys. B* **202** (1982) 253 (supersymmetry and Morse theory).
[39] Cardy, *Nucl. Phys. B* **270** (1986) 186.
[40] Gover, Latini, Waldron, *Mem. AMS* **235** (2015) (Poincaré–Einstein holography).
[51] Curry, Gover, and the almost-Einstein-matter scale tractor, arXiv:2208.09302.

---

# Appendix A — Core derivations

**A.1 Binary moments.** For ρ_θ = e^{θQ}/(2cosh θ) with Q² = 1: ⟨Q⟩ = tanh θ,
Var(Q) = 1 − tanh²θ = sech²θ, hence ⟨Q²⟩ = ⟨Q⟩² + Var(Q) = 1.

**A.2 The cosmological invariant.** With ρ_X = ρ_\* sech²[ϱ⊥(N−N_c)], define
Δ_X := −d ln ρ_X/dN = 2ϱ⊥ tanh θ. Then Δ′_X = 2ϱ⊥²sech²θ = 2ϱ⊥² − ½Δ_X², so
Δ_X² + 2Δ′_X = 4ϱ⊥². Substituting Δ_X = 3(1+w_X) gives the invariant.

**A.3 Fisher length.** ds_F = sech θ |dθ|, so L_F = ∫sech θ dθ = π, equal to
∫₀¹ dp/√(p(1−p)), the simplex diameter.

**A.4 Slot separation.** For ψ_NN + [K² + cρ_X]ψ = 0 with ρ_X = χ⊥ϱ⊥²sech²θ,
substituting θ = ϱ⊥(N−N_c) gives ψ_θθ + [K²/ϱ⊥² + cχ⊥ sech²θ]ψ = 0. The
pullback factor cancels the chain-rule factor: ϱ⊥ occupies the eigenvalue slot,
χ⊥ the potential-strength slot. One coefficient cannot perform both roles.

**A.5 The existence ceiling.** With x = −N_c > 0, flatness is
r_c e^{3x}sech²(ϱ⊥x) = T_m. At a double root, 3 − 2ϱ⊥ tanh(ϱ⊥x) = 0; eliminating
x gives the ceiling equation of §8.

**A.6 The Witten factorisation.** 𝒜†𝒜 = −∂²_θ + η² − η′ and
𝒜𝒜† = −∂²_θ + η² + η′. With η = tanh θ, η′ = sech²θ, η² = 1 − sech²θ, the
identity η² + η′ = 1 makes H₊ free and η² − η′ = 1 − 2sech²θ.

**A.7 Capacity as a thermodynamic exponent.** For ρ_β = e^{−βH}/Z the modular
Hamiltonian is K = βH + ln Z, so ⟨K⟩ = S and Var(K) = β²Var(H) = C. Hence
γ = C/S = d ln S/d ln T, and if S ∝ T^a then γ = a.

# Appendix B — Reproducibility

| script | verifies |
|---|---|
| `receipts_closure.py` | clause 3 identity; γ = dlnS/dlnT; 2D CFT gives C = S; ϱ⊥ = 1 from integrality + ceiling; horizon identity; the closed benchmark |
| `receipts_transparency_fold.py` | R1–R21: binary moments, invariant, saddle-node, futures, slot separation, N1, N2, ceiling, three-epoch structure, tractor identity, N3, Chatterjee self-duality, 𝔖_J, Levinson/Fisher, Fourier self-reciprocality, Version-B falsification |
| `P1/` package | data loaders with published-value validation; model comparison; the p profile; CMB anchor; ϱ⊥ and z_c profiles |

All scripts require only numpy and scipy; the P1 package downloads Pantheon+ on
first use.
