# The Closure Family and Its Kills

At a homogeneous reference cut, restricting the dimensionful inputs to one macroscopic radius $R_c$ and one microscopic length $\lambda$ gives the general dimensional form $\chi_*=\lambda^{-2}F(R_c/\lambda;\mathbf g)$, with arbitrary dimensionless data $\mathbf g$. The power-law closures studied here are a one-parameter monomial subfamily, not every possible closure. Within that declared family the note tests unscreened live running against lunar laser ranging, conditionally tests the rigid Jones ladder using the reproduced direct matching-ratio profile, rejects a crossed-product normalization that imports gravity, and computes four illustrative closures. All quoted numbers are asserted in `receipts/g_closures.py`; the cosmological diagnostics use the Planck 2018 flat-$\Lambda$CDM baseline and are not construction inputs.

## The macroscopic collapse lemma

**[EXACT WITHIN THE DECLARED FLAT-$\Lambda$CDM BACKGROUND]** At the bookkeeping crossing cut ($\rho_X=\tfrac12\rho_{\mathrm{crit}}$, hence $z_c=(\Omega_\Lambda/\Omega_m)^{1/3}-1=0.296$, $H_c=1.170\,H_0$):

- the horizon temperature is $T_c=\hbar H_c/2\pi k_B=3.11\times10^{-30}$ K — a pure function of $H_c$, no new datum;
- the apparent-horizon radius, area, and volume are $c/H_c$ and its powers — functions of $H_c$;
- the critical density $\rho_{\mathrm{crit},c}=3H_c^2/8\pi G$ and the horizon mass $M_c=c^3/2GH_c=7.9\times10^{52}$ kg *contain G* — circular as inputs.

So "temperature of the cosmos" is redundant given $H_c$, while "total mass" is inadmissible in a derivation of $G$. Under the declared two-scale restriction, dimensional analysis gives

$$
\boxed{
\chi_*=\frac{1}{\lambda^2}
F\!\left(\frac{R_c}{\lambda};\mathbf g\right),}
$$

where $F$ is an arbitrary dimensionless function and $\mathbf g$ denotes any independently fixed dimensionless algebraic or matter data. The closures computed below use the monomial subfamily

$$
F(x;\mathbf g)=C\,s_*x^a,
\qquad
G=\frac{c^3\,\lambda^{2+a}}{4\hbar\,C\,s_*\,R_c^{\,a}},
$$

with dimensionless exponent $a$, cell geometry $C=O(1)$, entropy per channel $s_*$, microscopic length $\lambda$, and $R_c=c/H_c$. Logs, thresholds, crossover functions, and dependence on additional dimensionless couplings belong to the general $F$ and are not exhausted by this subfamily.

## Kill 1 — live running (lunar laser ranging)

**[EMPIRICAL KILL OF THE DECLARED UNSCREENED LIVE-RUNNING LAWS]** If $\lambda$ and the dimensionless data are fixed and a monomial closure tracks the instantaneous horizon, $G\propto R_H^{-a}$ gives $\dot G/G=-a(1+q_0)H_0$ today. Against the LLR bound $|\dot G/G|\lesssim1.5\times10^{-13}\,\mathrm{yr^{-1}}$ (Hofmann and Müller, Class. Quantum Grav. **35**, 035015 (2018), $(7.1\pm7.6)\times10^{-14}$; MESSENGER gives the same order):

| Closure | Predicted running (per yr) | Excess over bound |
|---|---|---|
| a = 1 | 3.26e-11 | factor 217 |
| a = 2 | 6.51e-11 | factor 434 |
| logarithmic in R | 3.50e-13 | factor 2.3 |

The displayed logarithmic ansatz also exceeds the quoted bound. Within the unscreened monomial tracking branch, the surviving exponent satisfies $|a|\le4.6\times10^{-3}$. Thus the examples studied here must be nearly microscopic ($a\simeq0$) or **fossilized** — set at the crossing and thereafter conserved. Screening, thresholds, environmental dependence, or a more general $F$ require their own calculation and are not killed by this table. Fossilization itself requires a conservation law and makes [[conservation-of-causal-charge/entry|conservation of causal charge]] load-bearing, alongside the event-locus conjecture that the reference cut is a physical wall.

## Kill 2 — the rigid channel ladder

Executed in [[index-not-entropy]] using the reproduced unit-rate profile on fully released 2025 data. Every maximally mixed cell on the rigid sub-4 Jones ladder predicts $\mathfrak R_c\ge1/\ln2=1.4427$, above the $\Delta\chi^2\le3.84$ upper endpoint $1.165563$, so that ladder is conditionally excluded. The maximally mixed qutrit predicts $\mathfrak R_c=1/\ln3=0.91024$: it lies outside the $\Delta\chi^2\le1$ contour but inside the wider contour and is therefore only mildly disfavored. Both conclusions remain conditional on channel additivity, the unit-rate branch, and the model-to-wall identification.

## Kill 3 — the crossed-product route is circular by construction

**[STRUCTURAL]** The type-II crossed-product constructions define entropy only up to a state-independent additive constant, fixed in practice by matching to generalized entropy $A/4\hbar G$ — that is, by *inputting* $G$ through the gravitational constraint ([[library/gravity-and-the-crossed-product/entry|Witten]]; [[library/de-sitter-observables-algebra/entry|Chandrasekaran–Longo–Penington–Witten]]; the constraint's justification is itself delicate, [[library/linearization-instabilities-and-crossed-products/entry|De Vuyst–Eccles–Höhn–Kirklin]]). The vertical machinery normalizes its trace *by* gravity and therefore cannot output gravity's constant. This sharpens the first pass's trace-normalization obstruction from "unsolved" to "wrong register in principle" and is the fully typed form of [[the-modular-register-is-g-free|the modular audit]].

## The closures, computed

**A. Fossil Weinberg ($a=1$, bulk channel counting).** One channel per Compton volume of a carrier, projected on the cut: $\chi=R_c/\lambda^3$. Solving $4\zeta\,\ell_P^2R_c=\lambda^3$ gives $\lambda=3.1$–$5.0$ fm, carrier mass $m_*=40$–$63$ MeV for order-one conventions — the chiral/QCD window ($m_\pi/2=70$ MeV, $f_\pi=92$ MeV). This is Weinberg's empirical relation $m^3\approx\hbar^2H/Gc$ (*Gravitation and Cosmology*, Wiley 1972; lineage: Dirac's large numbers, Nature **139**, 323 (1937)) retyped as a channel-counting law and *frozen at the crossing* to survive Kill 1. Grade: COINCIDENCE plus an unconstructed freezing law. It is falsifiable to $O(1)$ once $\zeta$ is derived, and it predicts $G$ knows $H_c$.

**B. Microscopic spectral closure ($a=0$, NCG).** The spectral action's curvature stiffness must satisfy $\sqrt{f_2}\,\Lambda=2.71\times10^{18}$ GeV (receipts; Chamseddine–Connes, Comm. Math. Phys. **186**, 731 (1997); the closure equation is stated against the observable spectral action in [[deriving-value-of-g/spectral-index-area-route|the first pass]]). With the cutoff fixed independently at gauge unification, $\Lambda\approx1.1\times10^{17}$ GeV ([[library/why-the-standard-model/entry|Chamseddine–Connes]]; [[library/ncg-standard-model-neutrino-mixing/entry|Connes]]), the required moment is $f_2\approx605$ against a natural $O(0.5)$ — a miss of order $10^3$ in $G$, the known G–Λ normalization tension of the spectral action, with Sakharov's induced gravity (Dokl. Akad. Nauk SSSR **177**, 70 (1967)) as the general ancestor. Grade: the best genuinely microscopic computation on the table, currently three orders short on a 122-order question, and it predicts $G$ knows nothing of $H_c$.

**C. The holographic acceptance test.** Whatever the closure, the wall must deliver $\iota(\Sigma_c)=A_c/4\ell_P^2=1.654\times10^{122}$ nats at the crossing cut. Any candidate wall algebra can be executed against this number before any other question is asked. (In the II$_1$ reading of [[library/de-sitter-observables-algebra/entry|CLPW]] this is the finite total ledger of the static patch.)

**D. The a = 2 closure (dark-energy scale).** $\lambda=(4C\ell_P^2R_c^2)^{1/4}=61.6\,\mu$m at $C=1$ against the measured dark-energy length $\hbar c/E_\Lambda=88.1\,\mu$m ($E_\Lambda=2.24$ meV): $C=4.19$, order one. Dead as running by Kill 1 (factor 434), alive only as fossil.

**The classification observation.** Weinberg's pion relation, the millimeter dark-energy scale, and the $10^{122}$ holographic count — the three canonical cosmic "numerical coincidences" — are the $a=1$, $a=2$, and boundary members of this single family. They are one unknown exponent, not three mysteries.

## Promotion and failure

Promotion of A requires the freezing law, a derivation of $\zeta$ and of the carrier (why the chiral scale), and then a parameter-free check of $Gm_*^3=\hbar^2H_c/4c\cdot\zeta^{-1}$. Promotion of B requires the spectral-action normalization to close the $10^3$ gap without touching measured $G$. A and B are mutually exclusive in their strong forms and empirically distinguishable: A ties $G$ to the crossing epoch, B unties it. Failure of both leaves C as a bare acceptance test and returns the value question to the open state of the first pass.
