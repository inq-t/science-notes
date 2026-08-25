# The Mercury Moment

What would play, for this programme, the role the perihelion of Mercury played for general relativity — and what would not. Written 2026-08-25; observational claims reflect the DESI DR2 era and must be re-verified against current releases before any fit is run.

## Typing the question

Mercury's 43″/century was a specific epistemic object: a small, precisely quantified residual in *existing* precision data, retrodicted with **zero free parameters** — the number fell out of structure fixed by entirely different requirements (the Newtonian limit). Three anomaly types must not be conflated:

- **Michelson–Morley type** — a null or catastrophic mismatch that demands a *retyping* and is dissolved, not predicted. No number comes out; a wrongness goes away. These anomalies recruit; they do not test.
- **Eclipse type** — a novel prediction requiring new apparatus and a future expedition.
- **Mercury type** — a known quantified residual, retrodicted rigidly, anti-circularity manifest, with a clean death available if the residual resolves against the theory.

## The Mercury candidate: the phantom-crossing residual in the expansion history

Since 2024–2025, DESI BAO combined with CMB and supernova compilations has produced a quantified residual against ΛCDM: a 2.8–4.2σ preference (compilation-dependent) for dark energy that was phantom in the past ($w<-1$), crossed $w=-1$ at low redshift, and is thawing now — the "phantom-crossing anomaly" (DESI DR2 dynamical dark energy, Nature Astronomy 2025; arXiv:2508.10514; arXiv:2511.04610 names the anomaly). It is live and contested: global Bayesian reanalyses (arXiv:2605.13546) argue the preference does not persist. That is the correct epistemic state for a Mercury test — real enough to name, small enough to dispute.

Three observations make this the candidate.

**1. The shape is native to CST and pathological for the competition.** For the pulse $\rho_X\propto\operatorname{sech}^2(\nu x)$, continuity alone gives

$$
w_X(x)=-1+\frac{2\nu}{3}\tanh(\nu x),
$$

phantom before the peak, exactly $-1$ at the crossing, thawing after. (Check against [[causal-scale-theory/theorems/rigid-sech-response-identities|the rigid identity]]: $9(1+w)^2=4\nu^2\tanh^2$, $6w'=4\nu^2\operatorname{sech}^2$, sum $=4\nu^2$. ✓) Any *peaked response* crosses the phantom divide at its peak — $\mathrm d\rho_X/\mathrm dN>0$ on the way up simply is $w<-1$. For field-theoretic dark energy the crossing is famously sick (a single scalar needs ghosts to do it); for a susceptibility response it is not an exotic feature but a triviality, because $\rho_X$ is not a kinetic sector. **The feature of the data that embarrasses quintessence is the generic signature of a pulse.**

**2. The rigid identities put a zero-parameter curve in exactly the plane where the anomaly lives.** The rigid-response theorem's CPL tangent,

$$
w_a=\frac32(1+w_0)^2-\frac{2\nu^2}{3},
$$

is, on the unit branch $\nu=1$, a **parameter-free curve in the $(w_0,w_a)$ plane** — the plane in which the DESI contours are reported. The crossing location is not free either: [[causal-scale-theory/theorems/dimensional-crossing-partition|the crossing-partition theorem]] ties $\Sigma_c$ to equal partition, hence to measured $\Omega_m$.

**SKETCH — replace with receipt-grade recomputation.** Taking $z_c\approx0.3$ from equal partition with $\Omega_m\approx0.31$: $x_0=\ln(1+z_c)\approx0.26$, so $w_0\approx-0.83$ and $w_a\approx-0.62$. The DESI DR2 + CMB + Pantheon+ contour center is approximately $(-0.84,-0.62)$; Union3 and DESY5 combinations sit roughly 1–2σ off along the degeneracy direction. If the sketch survives recomputation, the unit branch lands on the Pantheon+ center. These numbers are back-of-envelope, computed at one sitting from the tangent relation and a partition estimate of $z_c$; the receipts must own them before they are quoted anywhere.

**3. The epistemology is already in place.** GR8 anti-circularity: $\nu$ and $\mathfrak R_c$ come from the unit principles, $N_c$ from partition plus measured $\Omega_m$ — nothing set by the DESI likelihood. [[causal-scale-theory/empirical-status|The empirical-status note]] already records a background comparison ($\Delta\chi^2\approx3.3$ in CST's favor at equal parameter count, status REPORTED FIT — LIMITED), and its promotion path — a versioned direct forward fit of the $(\nu,\mathfrak R_c)$ branches — *is* the Mercury computation.

## The test statistic: posterior mass at the predicted point, not Δχ²

Mercury was not "GR fits orbits better than Newton plus a fudge" — flexible models always fit. Mercury was "the number 43 comes out." Do not compete with $w_0w_a$CDM on fit quality: it spends two fitted numbers chasing what CST asserts. The statistic is the **posterior mass at the predicted point/curve** — how much of the data posterior sits on the parameter-free unit-branch locus — together with the comparator-ensemble rule already stated in [[causal-scale-theory/observables|the observables note]] (many smooth transients imitate the broad transition; the sharp content is the point, not the class). Two standing cautions from that note apply verbatim: a generic CPL posterior need not estimate the local CST tangent, so the tangent relation is a *posterior consistency check after* direct forward fitting, never the headline; and derivative-based reconstructions of $w_X'$ are noisy, so the shape invariant is a secondary check.

**The clean death.** If the anomaly resolves back to Λ exactly (as the global-Bayesian critiques contend it may), the unit branch dies. A test that cannot fail is not a Mercury moment; this one can.

The "acceleration sign flip" belongs to this same item: the pulse makes acceleration an *episode* ([[causal-scale-theory/future-asymptotics|the finite-acceleration future class]]), and its near-term observational shadow is exactly $w_a<0$ — decaying, not eternal, dark energy. Same residual, same test.

## Sorting the other candidates

- **Vacuum catastrophe; coincidence problem — Michelson–Morley type.** The $10^{122}$ catastrophe presupposes vacuum energy has the type "local bulk density that gravitates by mode-summing"; under the retyping (`retyped-conservation.md`, `energy-time-and-the-cosmic-clock.md`) it is a global sector datum — the conjugate of the cosmic clock, the class in [[causal-scale-theory/conjectures/local-global-vacuum-completion|the vacuum-completion conjecture]] — and the catastrophe becomes a type error, dissolved rather than predicted. The coincidence problem is likewise dissolved structurally: the crossing is a fixed point (the channel at its own trace, `retyped-conservation.md`; equal partition as conditional theorem), so "why now" retypes to "why near the crossing." Dissolutions motivate the retyping; they do not test it.
- **Value of G — eclipse type.** $G_{\mathrm{pred}}=c^3/4\hbar\chi_*$ is the announced expedition: a novel cross-register prediction gated on the wall construction and independent normalization. Highest prize on the board; not available until the wall exists; must not be spent early.
- **Neutrino mass — derivative discriminator, and cheap.** The current mild anomaly (cosmological fits preferring $\Sigma m_\nu$ at or below the oscillation floor) is background-degenerate with evolving dark energy. Rerun the chains with the sech² background and watch whether the neutrino posterior relaxes toward the oscillation minimum: a second retrodiction costing compute, not theorems. Keep the discipline of the empirical-status note — the historical neutrino exercise is model-class comparison, not distinctive support.
- **Dark matter — the Neptune-or-Vulcan fork, undecidable today.** Le Verrier's one method produced both Neptune (real unseen matter) and Vulcan (a phantom signaling wrong dynamics). Which one dark matter is lies in the perturbed, inhomogeneous register that CST cannot touch until [[causal-scale-theory/conjectures/covariant-response-sector|the covariant response sector]] exists. Anything said now would be the "kernel gravitates" gloss wearing a lab coat.
- **Perturbations; CMB anomalies — wrong register now, and the vault's own history warns.** The observables table marks growth/lensing/CMB "not honestly executable" before the covariant conjecture closes, and the wall/spectral lineage carries ten revoked claims from precisely this temptation. CMB anomalies are additionally poor Mercurys in principle: a-posteriori statistics with look-elsewhere pathologies, where Mercury's 43″ was unambiguous. Perturbations are the *second* Mercury — an ISW/growth signature with a derived (not borrowed) sound speed — waiting on the covariant completion.

## The orientation, in one breath

**Near-term Mercury:** the parameter-free unit-branch locus in the $(w_0,w_a)$ plane, laid across a living ~3σ anomaly whose most awkward feature — the phantom crossing — is the generic signature of a peaked response. **Standing Michelson–Morley:** vacuum catastrophe and coincidence, dissolved by the retyping. **Announced eclipse:** the value of G, after the wall. Everything else waits its register.

Execution order: (1) receipt-grade recomputation of $z_c$, $w_0$, $w_a$ on the unit branch from partition + measured $\Omega_m$ alone; (2) the versioned direct forward fit demanded by the empirical-status promotion path, scored by posterior mass at the predicted point with a comparator ensemble; (3) the tangent and shape-invariant relations as posterior consistency checks; (4) the neutrino-chain rerun as the derivative discriminator.

## External references (verify before formal citation)

DESI DR2 dynamical dark energy: Nature Astronomy (2025), s41550-025-02669-6. Evidence from DR2 BAO + Pantheon+/DES-Dovekie/Union3: arXiv:2508.10514. The named anomaly: arXiv:2511.04610. The skeptical global-Bayesian reanalysis: arXiv:2605.13546. Review of the DESI-era evidence and tensions: IOPscience 10.1088/1674-4527/ae8429. Significance quoted as 2.8–4.2σ, compilation-dependent, as of DR2; re-verify against the current data release before running the fit.
