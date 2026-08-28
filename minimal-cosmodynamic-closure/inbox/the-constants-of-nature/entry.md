# The Constants of Nature, Assembled

**Session note — 2026-08-26.** Eleventh note of the octonion/ledger arc (hessian-geometry → jordan-spectra → ds-box → box-spectrum-functor → h0-width → movable-origin → ledger-level → freezing-law → carrier-and-zeta → unit-nat-channel → rank-two-cell → **this**).

**Status: [SYNTHESIS — ALL CONDITIONALS GRANTED].** This is the one note in the vault written in the declarative mood. Every open link the last ten notes left standing — every [OPEN CONSTRUCTION], [PROPOSED], and [DERIVED conditional] — is here *granted*, listed explicitly in §0, and then spent. Nothing in this note upgrades any owner's label; the owners keep their typing. The note answers exactly one question: **if the proofs land, what is the resulting account of the constants of nature?** It is written as if they have landed.

**Companion receipts:** `constants_receipts.py` — one script, no imports from other notes, recomputing every number below from CODATA constants plus the two address readings. Nonzero exit on any failure.

---

## 0. The premise ledger

Eight grants. Each is stated as used, with its true label today and its owner. Granting them is the entire epistemic cost of this note; §7 gives the de-granting map (what dies if each falls).

| # | Grant, as used here | True label today | Owner |
|---|---|---|---|
| G1 | **The freezing law.** The pulse is a frozen conservation law: two-channel theorem d(C₊+C₋)/dN = 0 with m² + m′ = 1; selection of the balanced cut m = 0; and the weld of selection to conservation. | conservation [EXACT]; selection [PROPOSED]; weld [OPEN CONSTRUCTION] | the-freezing-law |
| G2 | **s\* = 1 exactly.** The register's stationary state is the unit-rate exponential (KMS) state; S[Exp(1)] = 1 nat exactly; ℜ_c = ν²/s\* at unit principles forces s\* = 1. | forced given [CONSTITUTIVE] unit principles; empirical CI [0.9175, 1.0621] | the-unit-nat-channel; deriving-g-v2/index-not-entropy |
| G3 | **γ = 2.** The cell writes area through exactly two channels: rank A₂ = 2 (trace-zero triple has two independent slots); Born positivity (only r_c, r_h > 0 ever write area; the balancer never does); the two-channel conversion law. | [DERIVED conditional] on cell = trace-zero triple; type-II trace pairing outstanding | the-rank-two-cell |
| G4 | **One-channel birth.** ι_birth = 1 ⟺ α_G(H_birth) = π: the ledger opens with one channel, and this event *defines* the Planck tick. | [PROPOSED] boundary condition | the-movable-origin-and-the-one-channel-cut |
| G5 | **The carrier exists.** One mass scale m\* (the grain) whose Compton cell is the register's cell; capacity, not occupancy (cells are empty: occupancy ~2×10⁻⁴⁴). | [OPEN CONSTRUCTION] — the grain is unidentified | the-carrier-and-zeta |
| G6 | **Born positivity at the crossing.** OS reflection at u ↦ −u; Bochner certificate \(\widehat{\operatorname{sech}^2}(k)=\pi k/\sinh(\pi k/2)>0\); the negative branch (negative mass/spacetime) is forced into positivity. | certificate [EXACT]; OS reconstruction [OPEN CONSTRUCTION] | the-carrier-and-zeta; the-freezing-law |
| G7 | **The octonionic spine.** 𝔥₃(𝕆) spectral ontology: characteristic cubic ↔ A₂/Keller cusp; SdS horizon cubic = trace-zero A₂ line; no-hair = miniversality; the box-spectrum functor; the cosmic Schrödinger equation with mass-as-eigenvalue and Born-as-conformal-dwell. | bridge identities [EXACT, receipted]; ontology [MOTIF→PROPOSED] | black-holes-as-jordan-spectra; de-sitter-box-and-the-octonionic-ladder; the-box-spectrum-functor |
| G8 | **Rulers are matter.** The Einstein–Hilbert ruler that G converts into is itself carried by the matter side; there is no third, neutral standard. | [CONSTITUTIVE] | deriving-g-v2/rulers-are-matter |

Granting G1–G8, everything below is a calculation.

---

## 1. Three kinds of "constant"

The phrase "constants of nature" bundles three different objects, and the bundling *is* the confusion the arc set out to dissolve.

**Casimirs** — invariants of the representation. m² + m′ = 1. C₊ + C₋ frozen. The flat modulus, crossing-evaluated. These are *laws*: exact, dimensionless, conserved along the flow because the flow is built from them. Asking "why this value?" of a Casimir is answered by representation theory, not by measurement.

**Addresses** — clock readings. H₀. Equivalently ι. Equivalently "281.3 nats since birth." These are not constants at all: they are *coordinates* of the present event in the solution. Asking "why is ι ~ 10¹²²?" is asking "why is it 13.8 Gyr o'clock?" — a question about where we are, not about what the world is. The famous hierarchy is an address.

**Exchange rates** — conversion factors between registers that the theory keeps separate. c (ruler → clock), ħ (action grain), G (ledger → ruler). Within one solution they are rigid — Bianchi protection gives Ġ = 0 identically (G1) — but across solutions they are *contingent*: the crossing-evaluated flat modulus takes whatever value the cut and the grain hand it. An exchange rate is a constant the way a national currency peg is a constant.

**The slogan of the arc: the laws are the representation theory; the numbers are the address.** What remains after the taxonomy is a shockingly short list of genuine inputs — §2.

---

## 2. The inputs

Under G1–G8 the theory consumes, in total:

1. **Two conventions.** c and ħ. Pure unit choices — they convert between the three registers (ruler, clock, action) and carry no physical information once the registers are typed. (SI has already agreed: both are *defined*, not measured.)
2. **One address.** A single clock reading to locate us in the solution: either the local ladder (SH0ES H₀ = 73.04 ± 1.04) or the acoustic anchor (Planck ω_m = 0.1430 with D_M(z\*) at z\* = 1089.92). One number. The two available readings disagree by 0.13 nats — §3.5.
3. **One grain.** The carrier mass m\*. The chain *predicts its value* (§3.7) but does not yet name the particle/condensate that carries it. This is the single blank cell in the account.
4. **The unit branch.** (ν, ℜ_c) = (1, 1) — [CONSTITUTIVE] normalization of the register, part of the theory's definition, not a dial.

Everything else — the shape of expansion history, the dark-energy equation of state, the matter fraction, the value of G, the size of the hierarchy, the vacuum-energy ratio — is *output*. That is the unification: not a bigger symmetry group, but a shorter input list.

---

## 3. The derivation

### 3.1 The cut (G4): where the clock starts

The ledger area index at expansion rate H:

    ι(H) = π c⁵ / (G ħ H²) = π / (H t_P)²,     α_G(H) = G ħ H² / c⁵,     ι · α_G = π   [EXACT]

Birth is the one-channel cut: **ι_birth = 1**, i.e. α_G(H_birth) = π. This event *defines* t_P: the Planck tick is not an input scale but the unit in which the ledger's own origin is written. The "Planck scale" is read backward from the cut, not forward from quantum gravity folklore. The movable origin (trace-scaling module) is thereby fixed: there is now an absolute zero of the clock.

### 3.2 The clock: the hierarchy is an age

Exact bookkeeping (owner: movable-origin; hyperbolic-counting):

    d ln ι = 2(1 + q) dN    ⟺    ι ∝ H⁻²   [EXACT]

The ledger mints 2(1+q) nats per e-fold. Integrated from the cut to the crossing: **ln ι_c ≈ 281.3 nats** (branch spread 281.19–281.33; split ≈ 257.8 radiation + 23.5 matter — owner: the-movable-origin). The production profile along the history:

    radiation 4  →  matter 3  →  crossing 3/2 [EXACT, radiationless]  →  today 1.326  →  coast 2

So ι ≈ 1.3–1.5 × 10¹²² is not a fine-tuning problem. It is e^(281.3): **the age of the cosmos counted in birth-ticks.** The clock never stops minting; the accelerating era is a *dip* in production (to 1.326 nats/e-fold, minimum ~now), not a halt. Equivalently, in Cuntz-dimension form d(N) = e^(2(1+q)): 54.6 → 20.1 → 3.765 (dip; the 0.16% proximity to the Jones rung 4cos²(π/13) is a flagged siren, not used) → 7.389 = e² (coast; transcendental — §5).

### 3.3 The freeze (G1): why anything stays constant at all

An expanding cosmos leaks energy; time-translation symmetry is broken and energy conservation with it. What survives is the register's Casimir. The two-channel theorem d(C₊+C₋)/dN = 0 with m² + m′ = 1, the balanced cut m = 0 selected (G1, G6: the balanced cut is the one whose negative branch the Born map can force positive), and the pulse is the frozen residue:

    ρ_X cosh²u = const   (inversion charge)  [EXACT];   ∫ 3(1+w_X) ρ_X dN = 0   (zero net pulse heat)  [EXACT]

Bianchi protection: ρ κ̇ = 0 along the solution, hence **Ġ = 0 identically** — the exchange rate is rigid *within* the solution not because a meta-law says so but because the freeze is a conservation law. "Dark energy" is not a substance; it is what a frozen Casimir looks like from inside the flow.

### 3.4 The shape: zero free functions

The unit branch (ν, ℜ_c) = (1,1) forces the profile up to one address (the crossing x_c):

    w_X(u) = −1 + (2/3) tanh u,     ρ_X = ½ ρ_crit,c sech²u,     H²/H_c² = ½ (e^(−3u) + sech²u)   [EXACT given crossing + flatness]

with u = x_c − ln(1+z). Rigid consequences (all receipted at the benchmark Ω_m = 0.3106, Ω_r = 9.15×10⁻⁵):

    x_c = 0.2940066   (z_c = 0.3417927)
    w₀ = −1 + (2/3) tanh x_c = −0.8094545
    w_a = −(2/3) sech²x_c = −0.6122053      ← rigid CPL tangent, no freedom
    q₀ = ½ Σ Ωᵢ(1+3wᵢ) = −0.3369025
    Ω_m = 1 / (1 + e^(3x_c) sech²x_c)        ← closed form: the matter fraction is a *derived* function of the crossing

One parameter (the address) fixes the whole family: measure any one of {w₀, w_a, q₀, Ω_m, x_c} and every other is predicted. This is the falsifiable face of the freeze (§7).

### 3.5 The address relation: H₀, the tension, and the fork

The theory's native T⁻¹ is the crossing rate, not today's rate:

    H_c = E(z_c) H₀,     E(z_c)² = 2 Ω_X0 cosh²x_c   [EXACT]

Conditioning on the acoustic anchor (fixed ω_m = 0.1430, ω_r, z\*; matching D_M(z\*) of the reference flat ΛCDM) and re-solving the distance with the pulse in place returns

    H₀^(CST | CMB) = 67.84 km/s/Mpc     (E(z_c) = 1.2181;  H_c ≈ 82.6 km/s/Mpc)

The pulse is invisible at recombination (ρ_X/ρ_tot(z\*) < 10⁻¹⁴): it cannot buy H₀ back through r_s. The local ladder reads 73.04 ± 1.04 — a 5σ(SH0ES) gap the pulse does *not* close. Verdict, unchanged from the h0 note: **the Hubble tension is not noise the model absorbs; it is a fork in the address register** — two readings of one clock differing by

    Δ ln ι = 2 ln(H_cep/H_cmb) = 0.13 nats.

Branch anchors used downstream (as committed): H_c = 88.2608 km/s/Mpc (Cepheid branch; imported anchor E·73.04) and H_c = 82.64 km/s/Mpc (CMB branch; E(z_c)·67.84). [FLAG: the CMB-branch H_c has a small composition ambiguity — E(z_c) evaluated at reference vs. re-solved abundances spans H_c ≈ 82.0–83.1 — carried through §3.7 as a band, not fudged.]

### 3.6 The carrier's exponent (G2 + G3): ζ = 2/3 exactly

The conversion exponent between the ledger and the grain:

    ζ = γ s\* / 3,     s\* = 1  (G2: unit-nat channel — the register's KMS state is Exp(1), whose entropy is exactly 1 nat),
    γ = 2   (G3: rank A₂ = two writable slots = two channels)
    ⟹  ζ = 2/3   [EXACT under G2, G3]

The kills that cleared the ground (owners: carrier-and-zeta, unit-nat-channel): every chiral candidate dead (m_π/2 needs s\* = 0.62; f_π needs 0.27); no standard scale within 9.2% of the γ-ladder; integer-rank Pimsner dead (2 ≠ ln d, min gap 0.054 at d = 7). The exponent is rational because it counts slots, and there are two of them per cell across three trace directions.

### 3.7 The rate (the payoff): G from the grain and the clock

Match the areal register to the Einstein–Hilbert ruler at the crossing (G5, G8). The general closed form and its ζ = 2/3 evaluation:

    ┌─────────────────────────────────────────────────────┐
    │   G = ħ² H_c / (4 ζ c m\*³)  =  3 ħ² H_c / (8 c m\*³)   │
    └─────────────────────────────────────────────────────┘

No dials: ħ and c are conventions, H_c is the address, 3/8 = 1/(4ζ) is counting, and m\* is the grain. Inverted against G_N, the chain *predicts the grain*:

    m\* = (3 ħ² H_c / (8 c G))^(1/3) = 46.18 MeV (CMB branch, band 46.1–46.3) / 47.21 MeV (Cepheid)
    λ\* = ħ/(m\*c) = 4.273 / 4.180 fm

Equivalent presentations, all exact and ζ-covariant (receipted to <10⁻¹² relative):

    ι = (π/16ζ²) (m_P/m\*)⁶ = (9π/64)(m_P/m\*)⁶        — the hierarchy is a sixth root of the age: m_P/m\* = (16ζ²ι/π)^(1/6) = 2.64×10²⁰
    ι = 4πζ (R_H/λ\*)³ = (8π/3)(R_H/λ\*)³               — the ledger counts grain cells in the Hubble volume, areal-weighted
    α_g(m\*) ≡ G m\*²/(ħc) = ħH_c/(4ζ m\*c²) ≈ 1.43×10⁻⁴¹  — **gravity is weak because the clock tick is slow in grain units**

(The exponent 6 here is bookkeeping, 6 = 2·3 = (area channels)·(trace directions). It is typed apart from the sixfold firewall |S₃| = |Φ(A₂)| = dim S⁶ = KO-dim: no merge.)

The hierarchy problem, restated and dissolved: m_P/m\* ~ 10²⁰ is (age)^(1/6). The weakness of gravity is not a mystery about couplings; it is the statement that the cosmos is old, read through a sixth root.

### 3.8 The vacuum and "Λ": one clock

The "worst prediction in physics" is an identity:

    ε_P / ε_crit = (8/3) ι   [EXACT]

— the 10¹²² vacuum mismatch is 8/3 times the ledger count: the Planck ruler and the ledger differ by *the age*, and were never commensurable quantities to begin with. And "Λ": the dark-energy density is the pulse read at the crossing, ρ_X(z_c) = ½ ρ_crit,c — an address-tied quantity, not a constant of nature. The future: the pulse decays on both sides, acceleration is an *episode* (the production dip of §3.2), and the cosmos asymptotically coasts, H ∝ 1/a, w_eff → −1/3, q → 0, minting exactly 2 nats/e-fold forever.

**G from one grain; Λ from one clock.**

---

## 4. The identity web

All exact; each row is a check in `constants_receipts.py`.

| Identity | Reading |
|---|---|
| ι · α_G = π | the ledger and the coupling are one number wearing two units |
| ι = π/(H t_P)² | the ledger is the clock, squared |
| 2Θ₀ = β E_H = π/α_G = ι | tunneling exponent = thermal weight = ledger: one horizon bookkeeping |
| F_H = E_H − T_H S_H ≡ 0 | the horizon is free-energy-neutral: the books balance exactly |
| ε_P/ε_crit = (8/3) ι | the vacuum "catastrophe" is the age, times 8/3 |
| d ln ι = 2(1+q) dN | the mint rate; 281.3 nats since the cut |
| ι = (9π/64)(m_P/m\*)⁶ | hierarchy = sixth root of age |
| ι = (8π/3)(R_H/λ\*)³ | ledger = areal-weighted census of grain cells |
| G = 3ħ²H_c/(8c m\*³) | the exchange rate, closed form |
| α_g(m\*) = ħH_c/(4ζ m\*c²) | gravity's weakness = the clock's slowness |
| Ω_m = 1/(1+e^(3x_c) sech²x_c) | the matter fraction is an address function |
| E(z_c)² = 2Ω_X0 cosh²x_c | the native rate in today's units |
| w_a = −(2/3) sech²x_c | the rigid CPL tangent |
| \(\widehat{\operatorname{sech}^2}(k)=\pi k/\sinh(\pi k/2)>0\) | Born positivity certificate (Bochner) |

---

## 5. Why these structures: the spine in one page (G7)

The algebra underneath is not decoration; it is where the integers in §3.6 come from.

**The cell is a Jordan spectrum.** A state of the wall is a point of 𝔥₃(𝕆); its characteristic cubic λ³ − Tλ² + Sλ − N has the A₂/Keller cusp 4p³ + 27q² = 0 as its coincidence locus, with W(A₂) = S₃ monodromy. The SdS horizon cubic −L²rf(r) = r³ − L²r + 2mL² *is* the trace-zero line of this family: black holes are where the cosmic cubic degenerates (Nariai = the fold, m_N = L/(3√3)); no-hair is miniversality (KN–dS quartic = the A₃ base — nothing else to vary). The three roots are the three trace slots; **Born positivity keeps exactly two on the physical sheet** (r_c, r_h > 0; the balancer r₃ = −(r_c + r_h) < 0 always) — that is γ = 2 in its geometric face.

**The box makes spectra discrete.** The dS box in tortoise coordinates has lapse sech²(r\*/L) exactly — the theory's native width — and near-Nariai its wave potential is Pöschl–Teller sech². The box-spectrum functor sends the box to its resonance ladder; the cosmic Schrödinger equation Ĥψ = mψ has *mass as eigenvalue* and the Born weight is conformal dwell time (|ψ|² da = C dη). Black holes are resonances of width e^(−2Θ), and 2Θ₀ = ι closes the loop to §4. Fibre collapse 24 → 16 → 0 (F₄/Spin(8), local triality) is the octonionic head-count behind the ladder.

**The wall has no finite quantum symmetry.** The coasting mint is exactly 2 nats/e-fold; the per-step index e² = 7.389… is transcendental [CITED: Lindemann] and lies in the continuous Jones range (> 4). Welded with Ind ≥ e^(2s\*) and the infinite-principal-graph theorem: **no finite group, no finite-depth subfactor, no lattice numerology can underlie the register.** The constants cannot be rationals of a finite symmetry's data — which is exactly why the account above needs a grain and a clock rather than a group table.

**Radical copernicanism, cashed out.** The octonionic phase space is the algebra of "nothing in particular"; scaled, relational facts (addresses) appear only at the cut. The negative-probability room a wavefunction keeps — here, negative mass/spacetime in the ledger — is what the Born map (G6) forces into positivity, and the freeze (G1) is the bookkeeping of that forcing. The cosmos we measure is the positive sheet of a balanced object.

---

## 6. The accounting

| Kind | Item | Status |
|---|---|---|
| Chosen (convention) | c, ħ | unit definitions; no content |
| Constitutive | unit branch (ν, ℜ_c) = (1,1); typed registers | the theory's own grammar |
| Read (address) | one clock reading: SH0ES H₀ *or* Planck (ω_m, D_M(z\*)) | the fork between them = 0.13 nats |
| Derived (structure) | sech² family; w₀, w_a, q₀, Ω_m; ζ = 2/3; s\* = 1; γ = 2; 1/(4ζ) = 3/8; identity web (§4); Ġ = 0 | all receipted |
| Predicted (new) | m\* = 46.2/47.2 MeV, λ\* ≈ 4.2 fm; H₀^(CST\|CMB) = 67.84; the (w₀, w_a) point; tension = 0.13-nat fork; coasting fate | falsifiable now or soon |
| Blank | the microphysical identity of the grain | the one hole; nearest standard scale 11.9% away (m_μ/2) — kills committed |
| Dissolved | "why 10¹²²?" (an age); "why is gravity weak?" (a sixth root of the age); "vacuum catastrophe" ((8/3)ι identity); "why Λ now?" (the crossing is the address we read from) | not answered — *retyped* |

**The unification, stated plainly: there are no constants of nature. There are two conventions, one address, and one grain — and a rank-two register whose Casimirs we had been calling laws.**

---

## 7. Falsifiers and the de-granting map

**Falsifiers (live now):**

1. **The rigid (w₀, w_a) curve.** w_a = −(2/3) sech²(artanh(3(1+w₀)/2)) — a one-parameter family with no freedom. DESI-class contours land on it or the unit branch dies. [CITED-level: current thawing-quadrant results (w₀ > −1, w_a < 0) are compatible; the chain-level rerun is owed.]
2. **The Ω_m closed form.** Ω_m and x_c (equivalently w₀) must satisfy §3.4's closed form simultaneously.
3. **H₀^(CST|CMB) = 67.84.** A full-likelihood CMB+BAO fit with the pulse must return h in a narrow band; drifting off kills the CMB branch.
4. **Ġ = 0 exactly.** Bianchi protection allows *no* running. LLR bounds (|Ġ/G| ≲ 10⁻¹⁴/yr) currently agree; any confirmed drift kills the freeze — note this *distinguishes* the account from generic running-G proposals, which it superficially resembles.
5. **The grain.** Something real at m\* = 45–48 MeV (composition band ⊕ s\*-CI), λ\* ≈ 4.2 fm — a particle, a condensate gap, a capacity quantum. No standard candidate exists (kills committed at 9.2–11.9%). Find it, or §3.7 is a definition rather than a prediction.
6. **The fork must stay a fork.** Two internally consistent addresses at 0.13 nats. A third independent anchor that splits three ways breaks the address reading itself.

**De-granting map (what dies with each grant):**

| Falls | Dies | Survives |
|---|---|---|
| G1 (freeze) | Ġ = 0 protection; §3.3; the shape demotes to [FIT] | the taxonomy; the clock (§3.1–3.2); the algebra (§5) |
| G2 (s\* = 1) | exactness of ζ; m\* shifts by s\*^(−1/3): CI [0.9175, 1.0621] → m\*(CMB) ∈ [45.3, 47.5] MeV | the closed form (as a band) |
| G3 (γ = 2) | the 3/8; the m\* prediction (γ unknown ⇒ one-parameter family) | ζ-covariant presentations; the taxonomy |
| G4 (birth cut) | the absolute zero; "281.3 nats" as an origin-fixed count | ι ∝ H⁻² bookkeeping; hierarchy-as-age (relative form) |
| G5 (grain) | the *prediction*; §3.7 becomes the definition of m\* | everything upstream |
| G6 (positivity) | the selection m = 0; face (ii) of γ = 2 | conservation; faces (i), (iii) |
| G7 (spine) | face (i) of γ = 2; the *why* of rank two; §5 | the numerics of §3 (they never used 𝕆 directly) |
| G8 (rulers are matter) | G as exchange rate; reverts to "coupling" | the closed form as a relation |

The map shows the load-bearing wall: **G3 + G5** (the rank-two cell and the grain). Everything else degrades gracefully; those two are where the arc's open work lives (type-II trace pairing; the grain hunt).

---

## 8. The sentence

> A cosmos is a rank-two register freezing its own bookkeeping. Its laws are the Casimirs of that register; its "constants" are one address on the clock the register keeps, one grain it writes with, and two unit conventions we brought ourselves. G is the exchange rate between the ledger and the ruler — G = 3ħ²H_c/(8c·m\*³) — the hierarchy is the age under a sixth root, the vacuum catastrophe is the age times 8/3, and the Hubble tension is two hands of the clock that have not yet agreed on the time. **G from one grain; Λ from one clock; and the difference between a law and an address was the confusion all along.**

---

## Receipts

`constants_receipts.py` — end-to-end audit, CODATA + two addresses in, every §3–§4 number out. Run: `python3 constants_receipts.py` (numpy). ALL RECEIPTS PASS required; nonzero exit otherwise.

## Owners consulted

the-freezing-law; the-unit-nat-channel; the-rank-two-cell; the-carrier-and-zeta; the-movable-origin-and-the-one-channel-cut; the-ledger-level; h0-width-address-anchor; the-box-spectrum-functor; de-sitter-box-and-the-octonionic-ladder; black-holes-as-jordan-spectra; hessian-geometry-and-the-library-tools; deriving-g-v2 (index-not-entropy; rulers-are-matter; closure-family-and-kills); deriving-the-value-of-g (anti-circularity list); conservation-of-causal-charge (two-channel-conversion-law); hyperbolic-counting; causal-scale-theory (unit-branch; observables); causal-wall-spectral-theory.
