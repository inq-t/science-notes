# The argument *more geometrico*

### Causal reach, Weyl scale, and entropic response — linear presentation

Everything below is arranged so that each item cites only items above it. Imported results are **Axioms** (established elsewhere, not argued here). The model's own assumptions are **Postulates**. Everything labelled **Proposition** is derived.

---

## I. Definitions

**D1.** $N = \ln a$, logarithmic metric scale. $H = \dot a/a = \dot N$.

**D2.** $\Xi_k = kc/(aH)$, comoving causal reach per e-fold for wavenumber $k$.

**D3.** $q = -a\ddot a/\dot a^2$, deceleration parameter.

**D4.** A **wall** is $w_N = (\mathcal{M}_N, \omega_N, \Sigma_N, \iota_N)$: an observer-accessible algebra, a faithful normal state, a causal cut, and the inclusion or crossed-product data relating it to neighbours.

**D5.** Three directions on the wall family:
 (i) $\tau$ — modular automorphism time, the **fibre**;
 (ii) $N$ — the cut label, the **base**;
 (iii) $\beta$ — KMS-normalized replica deformation, the **spectral** direction.

**D6.** $K$ the modular Hamiltonian; $S = \langle K\rangle$ the entropy; $C_E = \mathrm{Var}(K) = \partial^2_\beta \ln Z_\rho\big|_{\beta=1}$ the **capacity of entanglement**.

**D7.** $C = S_A/k_B = A/4\ell_P^2$, dimensionless horizon capacity.

**D8.** $f = T/T_{\rm CK}$, with $k_B T_{\rm CK} = \hbar H/2\pi$, the **temperature factor**.

**D9.** $n = C_E/C$, the **modular spectral index**.

**D10.** $\nu = f\,n$, the **response index**.

**D11.** Two autonomous grades $z_\pm = \mu_\pm e^{-\lambda_\pm N}$ with constant **grade gap** $g = \lambda_+ - \lambda_- > 0$; valuation $p = z_-/(z_-+z_+)$.

**D12.** $u(N) = C_E(N)/C_E(N_c)$, normalized susceptibility; $N_c$ the crossing $p = 1/2$.

---

## II. Axioms (imported)

**A1.** FLRW kinematics and the Friedmann equations.

**A2.** *(Hawking–King–McCarthy; Malament.)* Causal order determines topology and conformal geometry; a Weyl factor remains additional data.

**A3.** *(Type III$_1$.)* Local algebras have no trace and no normal pure states; and $\omega\circ\sigma^\omega_\tau = \omega$.

**A4.** *(Tomita–Takesaki; Connes.)* The modular automorphism group exists and is canonical modulo inner automorphisms.

**A5.** *(Bekenstein–Hawking.)* Causal horizons carry quarter-area entropy.

**A6.** *(Gibbons–Hawking.)* $k_B T_{\rm dS} = \hbar H/2\pi$ at de Sitter.

**A7.** *(Jacobson.)* First-order entropy balance $\delta Q = T\delta S$ on local causal horizons yields the Einstein equation.

**A8.** *(Cai–Kim.)* The first law at the FLRW apparent horizon with quarter-area entropy yields the Friedmann equations.

**A9.** *(Lashkari–Van Raamsdonk.)* The relative-entropy Hessian equals gravitational canonical energy in controlled holographic settings.

**A10.** *(Chentsov; Petz.)* Fisher–Rao is the unique natural classical metric; the relative-entropy Hessian selects BKM in the quantum case.

**A11.** Monotone metrics on state space are positive-definite.

---

## III. Propositions from the axioms alone

*These hold whether or not the model is true.*

**Prop 1** *(Causal-reach identity).* $\dfrac{d\ln\Xi_k}{dN} = q$. — from D1–D3, A1.
> Acceleration **is** contraction of comoving causal reach per e-fold. No force is involved.

**Prop 2** *(Capacity dictionary).* $q = -1 + \tfrac12\,d\ln\mathfrak{C}/dN$ and $\Xi_k = (k\ell_P/\sqrt\pi)\,e^{-N}\sqrt{\mathfrak{C}}$. — from Prop 1, A5, D7.

**Prop 3** *(Retyping).* FLRW expansion lives precisely in the datum that causal order does not determine. — from A2.

**Prop 4** *(No susceptibility along the fibre).* The BKM speed along a state's own modular orbit vanishes; the susceptibility must be transverse. — from A3, D5, D6.

**Prop 5** *(Spectral-index identity).* If $\ln\mathcal{Z}(\beta) = A\beta^{-n}$ then $C_E = nS$ at $\beta = 1$. — from D6.

**Prop 6** *(Horizon conversion).* $\dfrac{\vartheta_c C_c}{V_c} = f_c\,\varepsilon_{\rm crit,c}$. — from A5, A8, D7, D8.

**Prop 7** *(Kinetic obstruction).* Any diffeomorphism-natural functional of sigma-model type with a positive-definite BKM kinetic term gives $\rho + p = \mathcal{G}_{AB}\dot\Phi^A\dot\Phi^B \geq 0$, hence $w \geq -1$. — from A11.

---

## IV. Postulates

*The model's own commitments. Each is undischarged unless noted.*

**P1** *(Binary wall).* The relevant wall comparison reduces to **two** autonomous grades with constant gap $g$.
> Undischarged, and not on the paper's own theorem list. See §VII.

**P2** *(Spectral gap).* Intra-block modular variance is negligible against $g^2$.
> Currently **unstated** in the paper. Required for P1 to yield a pure pulse rather than a pulse plus offset.

**P3** *(Calibration).* $\left.\dfrac{d\beta}{dN}\right|_{N_c} = 1$ and $\Delta K = g$; globally $\beta - \beta_c = N - N_c$.
> The paper's Conjecture 3.1. This is the sole bridge between phenomenology and algebra.

**P4a** *(Proportional response).* $\rho_X(N) \propto C_E(N)$.

**P4b** *(Response normalization).* The constant is $\tfrac12\vartheta_c C_{E,c}/V_c$.

**P5** *(Crossing normalization).* $\vartheta$, $C$, $V$ are evaluated **once, at $N_c$** — the constitutive law is nonlocal in $N$.
> Currently **unstated**. The local alternative gives $\Omega_{X0} = 0.459$ and is Hubble-cutoff holographic dark energy.

**P6** *(Weyl bridge).* $g = D - 2$.

**P7** *(Unit response).* $\nu_c = f_c n_c = 1$.

**P8** *(Cosmological setting).* Flat; $\Lambda_{\rm g} = 0$; radiation negligible at the crossing.

---

## V. Propositions from the postulates

**Prop 8** *(Single crossing).* $p(N) = \left[1 + e^{-g(N-N_c)}\right]^{-1}$, crossing $1/2$ exactly once. — P1.

**Prop 9** *(The pulse).* $u(N) = \mathrm{sech}^2\!\left[\tfrac g2(N-N_c)\right]$, with exactly one maximum, and $\mathcal{I}_N = \mathrm{Var}(K)$. — Prop 8, P2, P3, A10, Prop 4.
> P3 is what converts a Fisher information into a **capacity of entanglement**. Without it, Prop 9 is a statistical identity with no algebraic content.

**Prop 10** *(Density).* $\varepsilon_X(N) = \tfrac{\nu_c}{2}\,\varepsilon_{\rm crit,c}\,u(N)$. — Prop 9, Prop 5, Prop 6, P4a, P4b, P5, D9, D10.

**Prop 11** *(First integral).* $\left(\dfrac{d\ln\rho_X}{dN}\right)^2 = g^2 - \dfrac{g^2}{\rho_*}\rho_X$; growing and decaying branches fold onto one line. — Prop 9, P4a.

**Prop 12** *(Equation of state).* $w_X = -1 + \tfrac g3\tanh\!\left[\tfrac g2(N-N_c)\right]$; $\dfrac{dw_X}{dN} = \dfrac{g^2}{6} - \dfrac32(1+w_X)^2$. — Prop 9, P4a, A1.

**Prop 13** *(Peak equality).* $r = \dfrac{\nu_c}{2-\nu_c}$ and $q_c = \tfrac12 - \tfrac34\nu_c$; $\nu_c = 1 \iff r = 1$. — Prop 10, P7, P8.

**Prop 14** *(One episode).* $q = 0 \iff r = (1+y^2)^3/16y^5$, minimum $r_{\rm acc} = 27\sqrt5/250 \approx 0.2415$ at $y = \sqrt5$. — Prop 12, P8.

**Prop 15** *(No superacceleration).* $\dot H \le 0$ throughout iff $r \le r_{\rm ns} \approx 13.7457$. — Prop 12, P8.

**Prop 16** *(Response window).* $0.3890 < \nu_c < 1.8644$; equality within $0.72$ e-fold of the crossing. — Prop 13, 14, 15.

**Prop 17** *(Spectral exclusion).* Bulk-thermal scaling $n = d-1 = 3$ lies outside the window under either temperature convention. The horizon spectrum must be Rindler/area-like. — Prop 16, D9, D10.

**Prop 18** *(Grade).* $D = 4 \Rightarrow g = 2$. — P6.

**Prop 19** *(CPL locus).* $w_a = -\tfrac{g^2}{6} + \tfrac32(1+w_0)^2$; with P7, P8 and $\Omega_m$ the pair $(w_0, w_a)$ is fixed. At $\Omega_m = 0.31$: $(-0.809, -0.612)$. — Prop 12, 13, 18.

**Prop 20** *(Jerk).* $j_0 = q_0(2q_0+1) - dq/dN|_0 = -0.114$, against $j \equiv 1$ for ΛCDM. — Prop 12, 13, 18.

**Prop 21** *(Nesting).* As $g \to 0$, $u \to 1$, $w_X \to -1$, $\rho_X \to \rho_*$: ΛCDM is the zero-grade-gap boundary of the family. — Prop 9, 12.

**Prop 22** *(T4 obstruction).* Since Prop 12 gives $w_X < -1$ for $N < N_c$, by Prop 7 the response admits **no** minimally coupled positive-definite sigma-model realization. It must be non-Lagrangian, non-minimally coupled, or observer-dressed. — Prop 7, Prop 12.

---

## VI. Dependency table

| Conclusion | Requires |
|---|---|
| Reframing (Prop 1–3) | axioms only |
| Shape: sech², first integral, branch folding, one maximum | **P1, P2, P3, P4a** |
| $g = 2$ | + **P6** |
| Amplitude, peak equality, $\nu_c$ | + **P4b, P5, P7, P8** |
| One episode, windows | + P8 |
| $(w_0, w_a)$, $j_0$, growth | all of the above |
| Identification as modular capacity | **P3** alone carries this |

---

## VII. The load-bearing analysis

**Four postulates carry the empirical branch.** P1, P2, P3, P4a suffice for the pulse shape, the first integral, and the branch-folding test — the only prediction ΛCDM cannot mimic at any parameter value. The amplitude branch costs four more.

**P3 is the hinge.** Remove it and every proposition in §V survives *as phenomenology* — the logistic is algebra, the sech² is a Fisher pullback, the first integral follows. What dies is the right to call $\mathcal{I}_N$ a capacity of entanglement, and with it the entire §3 ladder, the spectral index, and the amplitude. **P3 alone connects the cosmology to the operator algebra.** It is correctly identified as the paper's central conjecture.

**P1 is the weak link, and it is not on the theorem list.** The sech² does not come from the BKM machinery; it comes from assuming two grades and pulling back Fisher. §3 supplies the *interpretation* of the pulse, not the pulse. Prove P3 and P7 exactly as stated and this remains true: you would have computed the amplitude of a shape you inserted.

> **The unlisted target:** derive P1 from the modular spectrum of the apparent-horizon algebra. A type III$_1$ factor has continuous modular spectrum and no minimal projections; a two-grade reduction is prima facie in tension with that, and P2 is the condition under which the tension is tolerable. Both should be theorem targets and neither is.

**P2 and P5 are hidden.** Neither appears in the paper. P2 is required for the pulse to be pure sech² rather than sech² plus a constant — and note the payoff: an $N$-independent intra-block variance is exactly degenerate with $\Lambda_{\rm g}$, so the additive offset in Prop 11 may *measure* spectral-gap violation. P5 is a substantive nonlocality commitment that also forces the global-crossing branch of the perturbation fork.

**Prop 22 is a result, not an obstacle.** It closes a route and thereby narrows T4. It should be stated as a proposition rather than left implicit.

---

## VIII. Scholium: what remains undischarged

| Postulate | Status | Discharged by |
|---|---|---|
| P1 | open, **unlisted** | derive binary reduction from the wall algebra |
| P2 | open, **unstated** | spectral-gap estimate for the apparent horizon |
| P3 | open, listed (T1–T2) | modular Berry / crossed-product calibration |
| P4a | open, listed (T4) | constitutive theorem, subject to Prop 22 |
| P4b | open, listed (T4) | canonical-energy normalization |
| P5 | open, **unstated** | justify crossing-fixed normalization |
| P6 | open, listed | rank correspondence for the transverse cut |
| P7 | open, listed (T3) | compute $n_c$ and $f_c$ |
| P8 | standard setting | — |

Nine postulates; three of them invisible in the current text; one of them — P1 — generating the shape on which every empirical prediction rests, and absent from the programme that is supposed to discharge it.

The honest one-sentence summary of the edifice:

> *If a cosmological wall admits a two-grade modular reduction with a negligible intra-block spread, and if the replica direction is calibrated affinely to logarithmic scale, then the capacity of entanglement pulses as a sech², and — given a crossing-normalized constitutive map — its amplitude is fixed by the horizon capacity, the modular spectral index, and the temperature factor.*

Both antecedents are open. The first is the harder one, and it is the one currently missing from the plan.
