# Mass as a Calibrated Distinction Rate

Within an already reconstructed and metrically calibrated quantum theory, a spectral gap admits an exact rate presentation. The logarithm of vacuum-reduced Euclidean transfer attenuation is dimensionless and additive under slab composition; its quotient by Euclidean length or duration is an inverse-length or inverse-time rate, and multiplication by \(\hbar c\) or \(\hbar\) returns the clock-energy gap. Only after Poincare reconstruction does division by \(c^2\) retype that energy threshold as mass. Calling the same number a *factification rate* is a promising further hypothesis, but it requires a record-producing process and noncircular clock, action, and carrier comparisons: finite-depth transfer attenuation is injective, reversible clock phase is unitary, and neither operation by itself selects or records a fact.

**Status: [EXACT] for the transfer-rate identities, the rest-phase rate, and the rapidity-rate expression of acceleration; [STANDARD] for the classical Schwarzschild and leading semiclassical area-law inputs; [EXACT -- AFTER REDUCTION] for the algebraic rate identities conditional on those inputs; [CONDITIONAL THEOREM] for the factification-rate solder; [IDENTIFICATION] for reading attenuation as unresolved distinction persistence or Schwarzschild entropy as a rate-ratio capacity; [OPEN CONSTRUCTION] for a prelocal or octonionic carrier, its Yang--Mills realization, and any cosmological common origin.**

[[vacuum-aligned-innovation-completion/boundary-action-fixed-points-and-physical-linearization|Boundary-action fixed points]] supplies an exact functional interpretation of this rate. Integrating one more transfer layer acts nonlinearly on logarithmic boundary actions modulo constants; its derivative at the vacuum is the actual Doob transfer on the complete centered physical tangent space. Entropy enters through a conditional variational identity with a specified reference law. This does not equate entropy with mass, and contraction of a selected quadratic ansatz need not control the full tangent spectrum.

## The quotient carried by mass

Let \(H\geq0\), let \(P_0=E_H(\{0\})\), and assume the nonvacuum carrier \(\mathcal K=(1-P_0)\mathcal H\) is nonzero. For Euclidean length \(\ell>0\), put

$$
C_\ell
:=
e^{-\ell H/(\hbar c)}\big|_{\mathcal K},
\qquad
R(\ell)
:=
-\log\|C_\ell\|.
\tag{MDR1}
$$

If

$$
\Delta_E:=\inf\sigma(H|_{\mathcal K}),
\tag{MDR2}
$$

then spectral calculus gives

$$
\|C_\ell\|
=e^{-\ell\Delta_E/(\hbar c)},
\qquad
R(\ell)
=\ell\frac{\Delta_E}{\hbar c}.
\tag{MDR3}
$$

Consequently,

$$
R(\ell_1+\ell_2)
=R(\ell_1)+R(\ell_2),
\qquad
\kappa_\ell
:=
\frac{R(\ell)}{\ell}
=\frac{\Delta_E}{\hbar c}.
\tag{MDR4}
$$

The numerator \(R\) is dimensionless logarithmic attenuation depth. The quotient \(\kappa_\ell\) has dimensions of inverse length. With Euclidean duration \(\tau=\ell/c\), the same statement is

$$
\gamma_\tau
:=
\frac{R(c\tau)}{\tau}
=\frac{\Delta_E}{\hbar}
=c\kappa_\ell.
\tag{MDR5}
$$

The exact conversion ladder is therefore

| Presentation | Definition | Dimension |
|---|---|---|
| distinction depth | \(R=-\log\|C\|\) | \(1\) |
| attenuation per length | \(\kappa_\ell=\mathrm dR/\mathrm d\ell\) | \(L^{-1}\) |
| attenuation per duration | \(\gamma_\tau=(\mathrm d/\mathrm d\tau)R(c\tau)\) | \(T^{-1}\) |
| clock-energy gap | \(\Delta_E=\hbar\gamma_\tau=\hbar c\kappa_\ell\) | energy |
| relativistic rest-mass gap | \(m_{\mathrm{gap}}=\Delta_E/c^2\) | mass |

After the Poincare-Casimir identification,

$$
\boxed{
m_{\mathrm{gap}}
=
\frac{\hbar}{c}\frac{\mathrm dR}{\mathrm d\ell}
=
\frac{\hbar}{c^2}
\frac{\mathrm d}{\mathrm d\tau}R(c\tau).}
\tag{MDR6}
$$

Equations (MDR1)--(MDR6) are downstream identities on an already clocked quantum carrier: \(H\), \(\ell\), \(c\), and \(\hbar\) have all been supplied. They retype mass without explaining the origin of the clock or the action scale. [[hbar-clock-and-the-calibration-firewall]] proves the parameter-rescaling obstruction and states the separate solder required if mass or spacetime is supposed to be emergent.

This answers “a rate of what?” at the level already proved by [[past-future-angle-and-the-transfer-gap]]: it is the slowest logarithmic attenuation exponent, hence the uniform lower attenuation rate over all nonvacuum directions across a Euclidean slab. Individual spectral directions can attenuate faster. Equivalently, [[phase-modulus-pointing-and-euclidean-dwell]] shows that its reciprocal controls the supremal integrated Euclidean persistence.

[[auxiliary-response-localization/inq|Auxiliary response localization]] moves the construction one step upstream without identifying an auxiliary sampler clock with physical time. If a local action-derived Markov semigroup forgets centered observables at rate \(\kappa\) while its two-observable multiplicativity defect propagates no faster than \(v\) with spatial exponent \(\alpha\), balancing the two estimates returns the static inverse-length certificate

$$
\sigma_{\mathrm{aux}}
=
\frac{2\alpha\kappa}{\alpha v+2\kappa}.
\tag{MDR6a}
$$

The arbitrary rescaling of that proof clock cancels between \(\kappa\) and \(v\). This makes \(\sigma_{\mathrm{aux}}\) a noncircular candidate for the numerator in (MDR6), not yet its physical value. The identification requires regulator-uniform bounds in the Yang--Mills law, transport to the OS translation direction, a common exponent on a limiting total local family, and full OS/Poincare reconstruction.

The word *attenuation* is load bearing. Every \(C_\ell\) is injective at finite \(\ell\). It need not identify two inputs, erase information, form a record, or choose an outcome. The rate in (MDR6) becomes a rate of fact-making only if an additional theorem identifies this transfer geometry with a process that actually produces stable facts.

## The factor of two in Born-form persistence

The positive return is

$$
E_\ell=C_\ell^*C_\ell
=e^{-2\ell H/(\hbar c)}\big|_{\mathcal K}.
\tag{MDR7}
$$

For \(\|\psi\|=1\),

$$
b_\psi(\ell)
:=
\langle\psi,E_\ell\psi\rangle
=
\int_{(0,\infty)}
e^{-2\ell E/(\hbar c)}
\,\mathrm d\mu_\psi(E).
\tag{MDR8}
$$

If \(\psi\) is supported in the \(\Delta_E\)-eigenspace, then

$$
-\frac{1}{2}
\frac{\mathrm d}{\mathrm d\ell}
\log b_\psi(\ell)
=
\frac{\Delta_E}{\hbar c}.
\tag{MDR9}
$$

If it is not attained, the same edge is recovered as the worst-case operator-norm exponent or an asymptotic lower-support rate. The factor two comes from probability-like positive return rather than one-way amplitude attenuation. Since \(0\leq E_\ell\leq I_{\mathcal K}\), declaring the two-effect POVM \(\{E_\ell,I_{\mathcal K}-E_\ell\}\) already makes \(b_\psi(\ell)\) an outcome probability. A specified instrument is additionally required to define the conditional post-outcome state and its record; neither follows from (MDR7) alone.

## After clock and action calibration, rest mass has a phase-rate presentation

For a relativistic particle of fixed rest mass \(m\), the proper-time action contains

$$
S_{\mathrm{rest}}
=
-mc^2\int\mathrm d\tau.
\tag{MDR10}
$$

Its clock amplitude therefore carries the phase

$$
e^{-imc^2\tau/\hbar},
\qquad
\omega_m
:=
\frac{mc^2}{\hbar}.
\tag{MDR11}
$$

Thus rest mass is exactly convertible into a proper-time phase rate. This does not mean that the phase is a stream of facts. Within one sharp-mass sector it can be an unobservable common phase; only relative phases between components can interfere. Under Euclidean continuation the same positive generator appears as attenuation rather than rotation, but the Osterwalder--Schrader bridge and its hypotheses are what license that comparison. The imaginary unit changes the presentation of the generator from positive to skew-adjoint; it does not create the generator or its lower edge.

For a state not confined to one irreducible mass sector, let \(M\geq0\) denote the reconstructed mass operator. The rigorous “wavefunction of mass” is already a spectral direct integral:

$$
\mathcal H
\cong
\int_{\sigma(M)}^\oplus
\mathcal H_{m}\,
\mathrm d\nu(m),
\qquad
\psi
\cong
\int^\oplus\psi_m\,\mathrm d\nu(m).
\tag{MDR12}
$$

Its mass spectral measure can have atoms, continuous support, or resonance structure. The mass gap asks whether its physical vacuum representation excludes every nonvacuum value below a positive threshold. This construction requires no new canonical mass coordinate and no octonions, although a deeper algebra might still be proposed to explain why this spectral carrier exists.

## Acceleration is a rate in the same dimensional register

Proper acceleration also becomes an inverse-time rate after division by \(c\). In one spatial direction, if \(\chi\) is dimensionless rapidity,

$$
a
=
c\,\frac{\mathrm d\chi}{\mathrm d\tau},
\qquad
\alpha_a
:=
\frac{a}{c}
=
\frac{\mathrm d\chi}{\mathrm d\tau}.
\tag{MDR13}
$$

Mass and acceleration can therefore be compared as two rates of dimensionless quantities:

$$
\omega_m=\frac{mc^2}{\hbar},
\qquad
\alpha_a=\frac{a}{c},
\qquad
\frac{\omega_m}{\alpha_a}
=
\frac{mc^3}{\hbar a}.
\tag{MDR14}
$$

Equivalently, every mass determines the acceleration-valued conversion

$$
a_m:=c\omega_m=\frac{mc^3}{\hbar},
\qquad
m=\frac{\hbar}{c^3}a_m.
\tag{MDR14a}
$$

This is a reduced-Compton acceleration scale, not evidence that the mass is undergoing proper acceleration. It says that \(\hbar\) and \(c\) provide an isomorphism between the corresponding one-dimensional quantity lines once those constants and their physical roles are fixed.

They are not identical concepts. \(\omega_m\) is a phase or Euclidean-attenuation rate after the required reconstruction; \(\alpha_a\) is a Lorentz-boost or rapidity rate along an accelerated worldline. The detector relation derived in [[library/notes-on-black-hole-evaporation/inq|Unruh's original analysis]],

$$
k_BT_U
=
\frac{\hbar a}{2\pi c}
\tag{MDR15}
$$

compares them only after a Rindler horizon, state, and temperature normalization have been supplied. Equating \(mc^2\) with \(k_BT_U\) gives

$$
\omega_m
=
\frac{\alpha_a}{2\pi},
\tag{MDR16}
$$

but that equality is a declared physical comparison, not a dimensional theorem or a Yang--Mills scale derivation. Its real attraction is structural: a mass rate can be soldered to a modular/boost rate, and the \(2\pi\) records the chosen geometric normalization.

## What a factification rate would require

A fact is not merely a contracted vector. A minimal fact-producing signature needs:

1. a nontrivial possibility or readout algebra;
2. a state that weights its alternatives;
3. an instrument or branching law;
4. an obtained character or actuality rule; and
5. a persistent record order.

Pointing and forgetting remain distinct. A measurement interaction can copy a value into a record while a global reversible dilation retains the correlations; an operational restriction may later forget distinctions. Entropy of a state, relative-entropy loss under a channel, thermodynamic entropy production, and growth of a record algebra are likewise different quantities. [[pointed-facts-and-the-shorted-response]] separates the visible counterfactual alternatives from the hidden antecedent fibre and constructs the first exact operator answering “what does it operate on?”: the Schur short of a positive whole-response acts on the retained local distinction and measures its least cost over all compatible hidden extensions.

Suppose, nevertheless, that a constructed record process induces, on an appropriate symmetric linearized carrier, a strongly continuous self-adjoint contraction semigroup

$$
S_u=e^{-uK_F},
\qquad u\geq0,
\tag{MDR17}
$$

on a Hilbert carrier of unresolved alternatives, where \(K_F\geq0\) is self-adjoint and \(u\) is, initially, a dimensionless compositional or record-depth parameter. Let \(P_F=E_{K_F}(\{0\})\) project onto the settled or invariant subspace and define the dimensionless edge

$$
\kappa_F
:=
\inf\sigma\!\left(
K_F\big|_{(1-P_F)\mathcal H_F}
\right).
\tag{MDR18}
$$

This is a candidate *uniform settling exponent per unit record depth*, not yet a rate per second. Suppose an independent clock solder fixes

$$
\nu_F:=\frac{\mathrm du}{\mathrm d\tau}>0,
\qquad
[\nu_F]=T^{-1},
$$

and a positive action solder \(\mathfrak a_Q>0\) converts clock frequency to energy; ordinary quantum theory takes \(\mathfrak a_Q=\hbar\). Let \(\eta_F,b_F>0\). The construction becomes relevant to mass only after a linear comparison map \(J:\mathcal H_{\mathrm{phys}}\to\mathcal H_F\) satisfies

$$
J\!\left[D(H^{1/2})\cap(1-P_0)\mathcal H_{\mathrm{phys}}\right]
\subseteq
D(K_F^{1/2})
$$

and a domain-correct solder proves, for every

$$
\Psi\in D(H^{1/2})\cap(1-P_0)\mathcal H_{\mathrm{phys}},
$$

the quadratic-form and coverage bounds

$$
\|H^{1/2}\Psi\|^2
\geq
\eta_F\mathfrak a_Q\nu_F
\|K_F^{1/2}J\Psi\|^2,
\qquad
\|(1-P_F)J\Psi\|^2
\geq
b_F\|\Psi\|^2
\tag{MDR19}
$$

on the physical vacuum complement. Then the energy threshold obeys the first bound below; only after Poincare reconstruction and the Casimir equivalence does the second line define an invariant mass threshold:

$$
\Delta_E
\geq
\eta_F b_F\mathfrak a_Q\nu_F\kappa_F,
\qquad
m_{\mathrm{gap}}
\geq
\eta_F b_F\frac{\mathfrak a_Q\nu_F}{c^2}\kappa_F.
\tag{MDR20}
$$

This is a conditional comparison theorem, not an identification. The direction of (MDR19), the norms, the parameter \(u\), the clock and action solders, the carrier map, and the constants must all be fixed independently of the desired mass. Under \(u\mapsto\lambda u\), \(K_F\mapsto K_F/\lambda\); the product \(\nu_F\kappa_F\) is invariant only when the clock solder transforms with the same reparameterization. [[hbar-clock-and-the-calibration-firewall]] owns this normalization no-go.

A relative-entropy contraction or strong data-processing inequality can motivate a candidate tangent contraction, but it does not by itself construct the self-adjoint \(K_F\) in (MDR17). [[cosmic-geon-hypothesis-and-horizon-rate-ledger]] gives the exact additive channel residue \(\mathfrak R_{T_*}=D-D\circ T_*\) that may serve as a dimensionless numerator. A continuous channel semigroup, an invariant faithful reference state, enough differentiability to linearize it, and a detailed-balance or reversibility condition are additionally needed to make the tangent generator symmetric and self-adjoint on the chosen Hilbert completion. Relating that generator to the past--future Friedrichs angle requires still more: a stationary reversible Markov or OS dilation and an endpoint-transfer identification. But an observer-facing stochastic law need not be ontologically stochastic, and entropy contraction still does not select the obtained fact. The defensible hypothesis is therefore:

> Mass magnitude may be the clock-energy image of a primitive uniform settling exponent, but only clock, action, and carrier-correct solders can make “factification rate” more than a metaphor.

## Black holes separate capacity from rate

Black-hole thermodynamics supplies a stringent test of “more mass means more fact-making.” For a Schwarzschild exterior,

$$
r_s=\frac{2GM}{c^2},
\qquad
S_{\mathrm{BH}}
=
\frac{4\pi k_BGM^2}{\hbar c},
\qquad
a_H
=
\frac{c^4}{4GM},
\tag{MDR21}
$$

where \(a_H\) is the surface-gravity acceleration in the asymptotic normalization. Define the mass phase rate and horizon boost rate

$$
\omega_M:=\frac{Mc^2}{\hbar},
\qquad
\alpha_H:=\frac{a_H}{c}
=\frac{c^3}{4GM}.
\tag{MDR22}
$$

Then, conditional on the classical Schwarzschild formulas and the leading semiclassical area law, two algebraically exact identities are

$$
\boxed{
\omega_M\alpha_H
=
\frac{c^5}{4G\hbar}
=
\frac{1}{4t_P^2},}
\qquad
\boxed{
\frac{S_{\mathrm{BH}}}{k_B}
=
\pi\frac{\omega_M}{\alpha_H}.}
\tag{MDR23}
$$

Here \(t_P=\sqrt{\hbar G/c^5}\). With \(\ell_P=ct_P=\sqrt{\hbar G/c^3}\), the inverse-Compton rate per length \(\kappa_M=Mc/\hbar\) and horizon boost rate per length \(\kappa_H=a_H/c^2\) obey

$$
\kappa_M\kappa_H
=
\frac{1}{4\ell_P^2}.
\tag{MDR24}
$$

This gives a more precise version of the intuition. Within this leading Schwarzschild semiclassical comparison, increasing \(M\) raises the mass phase rate and the entropy capacity, but it lowers the horizon boost rate and Hawking temperature. Identifying entropy here as a capacity, it is proportional to the **ratio** of those rates, not to an entropy-production or event-count rate; an equilibrium black hole can have large entropy without “more happening.” At fixed areal radius \(R\), the Schwarzschild compactness comparison \(M\leq c^2R/(2G)\) and the area law describe saturation relative to that boundary scale, not an absolute maximum mass or a proof that the interior is ontologically absent. [[horizon-saturation-and-entropic-distinction]] owns the exterior-algebra and no-interior reconstruction boundary.

The rate duality in (MDR23) is exact after reduction from those standard classical and leading semiclassical inputs; it is not a Yang--Mills derivation. It does, however, suggest a clean three-register question: can one primitive construction yield a mass/attenuation rate, a causal-boundary boost rate, and an entropy capacity as related shadows without inserting \(G,\hbar,c\) by hand?

## Cosmic confinement cannot replace the infinite-volume theorem

A real cosmological rate does occur before any geon interpretation. For freely propagating radiation in a fixed comoving cell, FLRW stress conservation gives \(E_\gamma\propto a^{-1}\), hence

$$
-\frac{\mathrm d}{\mathrm dt}\log E_\gamma=H.
$$

Thus the Hubble parameter is exactly a logarithmic redshift-loss rate on that declared carrier. It is not the same operator as the mass phase rate \(mc^2/\hbar\), and redshift in a comoving cell is not literal flux through a cosmic exterior. [[cosmic-geon-hypothesis-and-horizon-rate-ledger]] derives this identity, the distinct apparent-horizon rate ledger, and the whole-to-local descent residue.

A literal finite box or cosmic cavity can create a lowest normal-mode frequency of order \(c/L\). That is a finite-size gap and ordinarily vanishes as \(L\to\infty\). The Clay problem instead requires a positive pure-Yang--Mills gap in the infinite-volume continuum theory for every compact simple gauge group. Cosmic confinement, a Hubble radius, or a boundary resonance can therefore define a separate common-origin proposal but cannot replace the gravity-independent theorem.

For a prelocal whole to explain both, it must derive two descendants:

$$
\text{one primitive scale/rate structure}
\longrightarrow
\begin{cases}
\text{local Yang--Mills transfer/Casimir gap},\\
\text{cosmological boundary or fossil observable},
\end{cases}
\tag{MDR25}
$$

with independently fixed maps and normalizations. Reading the observed acoustic ruler or glueball scale backward to choose the primitive resonance is circular. A time-dependent \(\hbar\), \(c\), or \(G\) proposal further owes a dimensionless observable that distinguishes physical drift from coordinated changes of units and rods.

## What octonions would have to do

Octonionic nonassociativity is not yet causal asymmetry. The octonions have conjugation, a positive norm, alternative multiplication, and reversible automorphism symmetries; none by itself defines a one-sided semigroup, an obtained fact, entropy production, or a positive mass floor. The exact exceptional-Jordan flag theorem in [[oriented-descent-angle-and-emergent-symmetry]] is valuable because it shows how a selected complex face can have a derived familiar stabilizer. It does not select the face or give it dynamics.

An octonionic mass carrier would have to supply at least:

1. a real or Jordan carrier with a positive state geometry;
2. a typed selection of the complex local observable face;
3. an ordered transport or record structure not erased by that selection;
4. an associative or otherwise operationally complete algebra for local probabilities;
5. a positive transfer modulus with a full-complement lower rate;
6. a reconstruction map to the Poincare translation representation; and
7. a proof that the resulting rate survives infinite volume and continuum removal.

The strongest present constraint is negative but useful: a nonassociative multiplication table, Jordan rank, knot class, cocycle, or chirality label may organize sectors or the polar phase, but it contributes to mass only if it controls the all-direction positive modulus or constructs the missing carrier/solder.

## Stopping condition

The rate retyping advances the programme if a proposed primitive operator answers all of these questions:

- **What does it operate on?** A declared carrier of unresolved alternatives, regional distinctions, or records.
- **What is dimensionless?** A logarithmic attenuation, relative-entropy defect, record increment, or other composable depth.
- **What is the denominator?** A canonically normalized Euclidean length, clock duration, modular parameter, or record parameter with an independent clock/length solder.
- **Why is the exponent positive on every nonvacuum direction?** A fixed-thickness contraction, functional inequality, or closed-range theorem not extracted from the desired spectrum.
- **How does it become energy?** A phase/OS bridge, an action solder, and a same-carrier comparison with the transfer Hamiltonian.
- **How does it become mass?** Poincare reconstruction and the full Casimir equivalence.
- **How does it become a fact?** An instrument, obtained character, and persistent record—not attenuation alone.

The category error is now sharply located for pure Yang--Mills. Asking a local gauge-field mass term to explain its gauge-invariant vacuum-sector gap mistakes a global spectral rate for a coefficient in a local presentation; asking how electroweak vector masses arise from a supplied Higgs sector remains a legitimate local-QFT question. The Copernican replacement is not yet “mass is factification,” but the typed theorem target:

$$
\boxed{
\text{positive dimensionless distinction exponent}
\xrightarrow{\text{clock solder}}
\text{frequency gap}
\xrightarrow{\text{action solder }\mathfrak a_Q}
\text{clock-energy gap}
\xrightarrow{\text{Poincare/Casimir}}
\text{mass gap}.}
\tag{MDR26}
$$

Whether that distinction rate is also the rate at which facts become stably recorded is the next construction problem.
