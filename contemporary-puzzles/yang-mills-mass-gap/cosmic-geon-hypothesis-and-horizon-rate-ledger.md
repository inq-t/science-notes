# The Cosmic-Geon Hypothesis and the Horizon Rate Ledger

A spatially flat Einstein--FLRW apparent-horizon sphere has an exact geon-like ledger: its critical energy has unit compactness, its canonical horizon heat times its area entropy equals that energy, and its energy-normalized signed supply rate equals the logarithmic growth rate of horizon capacity. This does not prove that the cosmos is a Wheeler geon or that radiation literally leaks through an exterior boundary. It isolates the rigorous content of the analogy and suggests a sharper Copernican hypothesis: a whole-state confinement structure may present internally as expansion, redshift, and changing causal accessibility, while local mass would have to arise from a separate tangential cost of maintaining pointed distinctions after the whole-to-part passage.

**Status: [EXACT] for the FLRW continuity and rate identities under their stated conventions; [STANDARD -- MODEL DEPENDENT] for the Einstein apparent-horizon, Misner--Sharp, area-entropy, and canonical-temperature inputs; [IDENTIFICATION] for calling horizon entropy a capacity; [CONJECTURE] for the cosmic-geon and whole-to-part descent readings; [OPEN CONSTRUCTION] for a common carrier that yields both the cosmological ledger and an infinite-volume Yang--Mills mass gap.**

## Two meanings of leak

The first exact ledger concerns a fixed comoving region. Let \(\varepsilon\) and \(p\) be energy density and pressure in an FLRW solution. Local stress-energy conservation gives

$$
\dot\varepsilon+3H(\varepsilon+p)=0.
\tag{CG1}
$$

For freely propagating radiation, \(p_\gamma=\varepsilon_\gamma/3\), so

$$
\varepsilon_\gamma a^4=\text{constant}.
\tag{CG2}
$$

If \(V_0\) is a fixed comoving coordinate volume, its physical volume is \(V=a^3V_0\), and the radiation energy assigned to it is

$$
E_\gamma
:=
\varepsilon_\gamma a^3V_0
\propto a^{-1}.
$$

Therefore

$$
\boxed{
-\frac{\mathrm d}{\mathrm dt}\log E_\gamma=H.}
\tag{CG3}
$$

For \(H>0\), the Hubble parameter is exactly the logarithmic redshift-loss rate of radiation energy in a comoving cell; for contraction the same signed identity describes a gain. No net radiative flux through the comoving boundary is required. The standard work ledger is \(\mathrm dE_\gamma=-p_\gamma\,\mathrm dV\), and individual microscopic trajectories need not respect the bookkeeping boundary. In a general FLRW spacetime there is no global timelike Killing symmetry whose Noether charge would make the cell's changing energy part of one globally conserved energy stock. Equation (CG3) is local covariant bookkeeping, not evidence that a compensating object was emitted into an exterior.

Nor is it automatically entropy production. For equilibrium radiation with fixed effective species and adiabatic expansion, \(T\propto a^{-1}\), the entropy density scales as \(s\propto T^3\), and \(S_\gamma=sa^3V_0\) is constant. Radiation energy can redshift while fine-grained or comoving thermodynamic entropy does not increase. Energy attenuation, entropy production, and record production remain different types.

The second ledger concerns a moving apparent horizon and must not be identified with (CG3). For a spatially flat expanding Einstein--FLRW solution, define

$$
R_A:=\frac cH,
\qquad
q:=-1-\frac{\dot H}{H^2},
\qquad
\Theta_A:=k_BT_A^{\mathrm{can}}=\frac{\hbar H}{2\pi},
$$

and

$$
\iota_A
:=
\frac{S_A}{k_B}
=
\frac{\pi c^5}{G\hbar H^2}.
\tag{CG4}
$$

Here \(\Theta_A\) is the canonical \(2\pi\) energy-valued horizon temperature and \(\iota_A\) is the dimensionless Einstein area entropy. [[conformal-scale-geometry/hawking-friedmann-identity]] gives

$$
\rho_{\mathrm{crit}}
:=
\frac{3c^2H^2}{8\pi G},
\qquad
V_A
:=
\frac{4\pi}{3}R_A^3,
\qquad
E_{\mathrm{MS},A}
:=
\frac{c^4R_A}{2G}.
\tag{CG4a}
$$

The canonical temperature is an algebraic horizon scale; no equilibrium state on a dynamical apparent horizon is inferred merely from its definition. With the displayed energy-density convention, the Hawking--Friedmann identity is

$$
\boxed{
E_A
:=
\rho_{\mathrm{crit}}V_A
=
E_{\mathrm{MS},A}
=
\Theta_A\iota_A
=
\frac{c^5}{2GH}.}
\tag{CG5}
$$

Choose the apparent-horizon energy-supply orientation for which

$$
P_A
:=
-\frac{\dot H}{H^2}\frac{c^5}{G}
=
(1+q)\frac{c^5}{G}.
\tag{CG6}
$$

This is the standard matter-register apparent-horizon flux convention used by [[deriving-g-v2/the-leak-register]]; [[library/first-law-of-thermodynamics-and-friedmann-equations-of-frw-universe/inq|Cai and Kim]] supply the primary apparent-horizon thermodynamic precedent. Reversing the horizon orientation reverses the flux sign. The factor \(c\) enters through \(HR_A=c\), not because material objects cross the horizon at light speed.

Differentiating (CG4)--(CG6) yields the exact rate ledger

$$
\boxed{
\frac{P_A}{E_A}
=
\frac{\mathrm d}{\mathrm dt}\log\iota_A
=
2H(1+q),}
\tag{CG7}
$$

and

$$
\boxed{
\dot E_A=\frac{P_A}{2},
\qquad
\Theta_A\dot\iota_A=P_A,
\qquad
\iota_A\dot\Theta_A=-\frac{P_A}{2}.}
\tag{CG8}
$$

Thus the moving-horizon energy changes at half of the signed supply rate: the capacity term contributes \(P_A\), while the temperature term contributes \(-P_A/2\). For \(1+q>0\) the horizon cools and the quasi-local energy grows; the signs reverse in a phantom regime. In this restricted model the alleged leak is not simply radiation leaving a cosmic container. It is a balance among quasi-local energy, boundary capacity, temperature, and motion of the subsystem boundary.

## Exact critical compactness, without an exterior mass

Let \(M_A:=E_A/c^2\). Equations (CG5) and \(R_A=c/H\) give

$$
\boxed{
\frac{2GM_A}{R_Ac^2}=1.}
\tag{CG9}
$$

This is the same dimensionless compactness value as a Schwarzschild horizon. It is a serious structural rhyme: the flat Friedmann constraint places the critical contents of the apparent-horizon sphere at a marginal compactness relation. But \(M_A\) is a Misner--Sharp quasi-local mass in a homogeneous cosmology, not the ADM or rest mass of an isolated object. The apparent horizon is not generally the particle horizon or event horizon, and the FLRW spacetime supplies no asymptotically flat exterior into which the whole cosmos radiates.

Wheeler's original [[library/geons/inq|geon]] is specifically a localized, self-gravitating configuration of electromagnetic radiation that can leak into an exterior and is generally metastable. The exact overlap and the decisive differences are:

| Register | Wheeler geon | Flat FLRW apparent-horizon sphere |
|---|---|---|
| carrier | localized radiation in an asymptotic spacetime | homogeneous cosmological solution |
| mass notion | isolated gravitational/rest-like mass | Misner--Sharp quasi-local energy |
| confinement | recurrent self-gravitating radiation | Friedmann constraint and moving marginal sphere |
| leak | radiation escaping the localized configuration | redshift in a comoving cell or signed supply across a moving apparent horizon |
| outside | physical asymptotic exterior | no exterior of the cosmos is supplied |
| lifetime | metastability measured in clock periods | one cosmological history \(H(t)\) |

The defensible claim is therefore not “the cosmos has been proved to be one geon.” It is:

> Flat FLRW possesses a geon-like self-consistency grammar in which energy, boundary scale, capacity, temperature, and rate are all functions of one cosmological scale section. A deeper theory may explain that ledger as the internal presentation of whole-state confinement, but it must construct rather than assume the comparison.

## The relative background of a Copernican fact

The radical Copernican insight can be stated without first presupposing a spatial whole. Let \(\mathcal A_W\) be a candidate whole-register von Neumann algebra, let \(\mathcal A_O\) be an accessible von Neumann algebra for a context \(O\), and suppose a normal unital inclusion

$$
i_O:\mathcal A_O\hookrightarrow\mathcal A_W
$$

has actually been constructed. For \(\omega\in\mathsf S_{\mathrm n}(\mathcal A_W)\), restriction gives the local normal state

$$
r_O(\omega):=\omega\circ i_O.
$$

The background forgotten by this local presentation is exactly the restriction equivalence class

$$
\boxed{
[\omega]_O
:=
\{\varphi\in\mathsf S_{\mathrm n}(\mathcal A_W):
\varphi\circ i_O=\omega\circ i_O\}.}
\tag{CG10}
$$

Its members are globally different but locally indiscernible. This is a precise relational meaning of “background,” “nothing for this readout,” and “what is not determined by this readout alone.” An admissible-state or dynamics theorem would be needed to prove stronger retrodictive impossibility. The fibre is not nonbeing and need not be a linear kernel.

A pointed fact is additional. Choose a unital commutative \(C^*\)-readout algebra \(\mathcal D_O\subseteq\mathcal A_O\); a local classical value functional is a character

$$
\chi_O:\mathcal D_O\longrightarrow\mathbb C.
\tag{CG11}
$$

A state supplies weights over alternatives, while an instrument supplies outcome-conditioned state change and a record extension. On a diffuse von Neumann context a character need not be normal, so it is not automatically a normal physical posterior. Neither restriction nor a character alone explains why this value is obtained. [[sufficient-reason/facticity-and-pointing]] and [[algebra/local-global-individuation]] own those distinctions.

For a finite or discrete outcome set, one carrier-correct schematic is

$$
\mathsf S_{\mathrm n}(\mathcal A_W)
\xrightarrow{\ r_O\ }
\mathsf S_{\mathrm n}(\mathcal A_O)
\xrightarrow{\ \mathcal M_*\ }
\operatorname{CQ}(Y,\mathcal A_O)
\xrightarrow{\ \mathrm{condition\ on}\ y\ }
\mathsf S_{\mathrm n}(\mathcal A_O)\times\mathcal R_y.
\tag{CG11a}
$$

Here the instrument channel has components \(\mathcal M_*(\rho_O)=(\rho_y)_{y\in Y}\) with \(\rho_y\) positive normal subnormalized functionals and \(\sum_y\rho_y(1)=1\). Its classical marginal is the outcome law \(p_\rho(y)=\rho_y(1)\); when \(p_\rho(y)>0\), conditioning gives \(\rho_y/p_\rho(y)\), while a compatible record extension supplies \(\mathcal R_y\). The arrows may have different carriers and none may silently stand in for all the others.

For normal states \(\rho,\sigma\) with \(D_{\mathcal A_W}(\rho\Vert\sigma)<\infty\), one exact measure of background distinguishability lost under restriction is the Araki relative-entropy decrement

$$
\delta_O(\rho,\sigma)
:=
D_{\mathcal A_W}(\rho\Vert\sigma)
-
D_{\mathcal A_O}(r_O\rho\Vert r_O\sigma)
\geq0,
\tag{CG12}
$$

The finiteness assumption prevents an undefined \(\infty-\infty\) difference, while data processing makes the restricted term finite and proves the inequality. This is a state-pair functional, not yet a mass, clock rate, outcome, or conserved charge. Equality characterizes a recoverability/sufficiency regime only under the appropriate recovery theorem.

More generally, let \(T_*\) be the Schrödinger-picture predual channel induced by a normal unital completely positive Heisenberg map. For states with \(D(\rho\Vert\sigma)<\infty\), define its descent residue

$$
\mathfrak R_{T_*}(\rho:\sigma)
:=
D(\rho\Vert\sigma)
-
D(T_*\rho\Vert T_*\sigma).
\tag{CG12a}
$$

Data processing gives \(\mathfrak R_{T_*}\geq0\). For composable predual channels \(T_*\) and \(S_*\), direct cancellation gives the exact cocycle-like allocation law

$$
\boxed{
\mathfrak R_{S_*\circ T_*}(\rho:\sigma)
=
\mathfrak R_{T_*}(\rho:\sigma)
+
\mathfrak R_{S_*}(T_*\rho:T_*\sigma).}
\tag{CG12b}
$$

This is the cleanest current mathematical meaning of a “residue cost paid under descent”: relative distinguishability loss is allocated between successive whole-to-part arrows. It is not automatically a torsor, obstruction class, heat, emitted energy, or mass. A torsor description additionally requires a specified free transitive group action; an obstruction requires a declared lifting or gluing problem. Vanishing residue becomes a recoverability or sufficiency statement only under the hypotheses of the relevant recovery theorem.

The finite arithmetic identities in (CG3), (CG5), and (CG7)--(CG9), together with the finite classical-channel analogue of (CG12b), are exercised by [[contemporary-puzzles/yang-mills-mass-gap/receipts/cosmic_geon_rate_receipt.py|the cosmic-geon rate receipt]] and [[contemporary-puzzles/yang-mills-mass-gap/receipts/cosmic-geon-rate-receipt-output.txt|its stored output]]; the receipt explicitly makes no Araki, ontological, continuum, or mass-gap claim.

If \((T_{u,*})_{u\geq0}\) is a strongly continuous semigroup of predual channels on the declared state or tangent topology,

$$
T_{0,*}=\mathrm{id},
\qquad
T_{u+v,*}=T_{u,*}\circ T_{v,*},
$$

with canonically normalized dimensionless parameter \(u\), invariant faithful normal reference state \(T_{u,*}\sigma=\sigma\), and the uniform contraction

$$
D(T_{u,*}\rho\Vert\sigma)
\leq
e^{-2\kappa_{\mathrm{desc}}u}
D(\rho\Vert\sigma),
\tag{CG12c}
$$

then \(\kappa_{\mathrm{desc}}>0\) is an admissible dimensionless lower contraction exponent; the intrinsic optimal exponent is the supremum of all admissible values. Turning it into a self-adjoint tangent generator requires differentiability, a chosen Hilbert completion, and detailed balance or another symmetry hypothesis. Turning that generator into mass still requires the independent clock, action, carrier, and Casimir solders below.

## Why Type III is useful—and insufficient

Type-III local algebras are useful here because they force the framework away from atomic “little things in boxes.” They can carry normal states and commutative readout contexts, but have no nonzero normal semifinite trace and no minimal projections. Araki relative entropy and modular comparison do not require a density matrix or trace on the local algebra. Connes cocycles compare faithful modular presentations, and the canonical core packages those comparisons without privileging a weight.

The type cannot do the rest of the work. In particular:

- type III does not select a character, outcome, or record;
- massless and massive QFTs can both have type-III local algebras, so type alone does not imply a gap;
- for a type-\(\mathrm{III}_1\) factor the flow of weights on the center of the core is trivial, although the dual action on the core still scales its semifinite trace;
- that vertical trace-scaling action is not cosmic expansion until a horizontal realization theorem relates the carriers; and
- modular flow is a reversible group, while a physical history needs a one-sided accessible action or persistent record order.

Half-sided modular inclusions can rigorously make an ambient reversible group appear as a one-sided semigroup on an accessible algebra. Their single positive generator cannot itself supply the floor: if \(P\geq0\), \(P\neq0\), and its modular covariance is

$$
\Delta^{it}P\Delta^{-it}=e^{-2\pi t}P
\qquad(t\in\mathbb R),
$$

then scale covariance forces \(\sigma(P)=[0,\infty)\). The mass candidate must instead be a joint invariant—such as a full Poincare Casimir reconstructed from compatible oppositely scaling directions—or another positive tangential response with a proved floor. [[wall-construction-interface/half-sided-modular-tunnel]] and [[joint-causal-generators-and-the-mass-casimir]] own that distinction.

## The forgetting operator cannot itself be mass

There is a decisive range--kernel obstruction. Suppose a normal conditional expectation \(E:\mathcal A_W\to\mathcal A_O\) implements the formation of the accessible carrier and preserves a faithful normal state \(\varphi\), so \(\varphi\circ E=\varphi\). In its GNS triple \((\pi_\varphi,\mathcal H_\varphi,\Omega_\varphi)\), define

$$
e\,\pi_\varphi(x)\Omega_\varphi
:=
\pi_\varphi(Ex)\Omega_\varphi.
$$

Then \(e\) is the orthogonal projection onto

$$
\mathcal K_O
=
\overline{\pi_\varphi(\mathcal A_O)\Omega_\varphi}.
$$

Then \((1-e)\xi=0\) for every \(\xi\in\mathcal K_O\). The raw forgetting form \(\|(1-e)\xi\|^2\) vanishes on the entire formed carrier, so it cannot distinguish the vacuum from excitations within that carrier. The act that forgets the background cannot also be the mass operator of what remains.

Within this expectation/projection model, the no-go forces at least the three-stage architecture isolated in [[causal-patch-boundary-and-two-times]]:

$$
\boxed{
\text{carrier formation or restriction}
\longrightarrow
\text{tangential distinction response}
\longrightarrow
\text{clock Hamiltonian and Casimir}.}
\tag{CG13}
$$

This is the most important correction to “the leak is the cost of mass.” The literal forgetting map forms the local arena. A different operator must measure the cost of varying or compatibly extending distinctions *within the retained arena* against the whole-register constraints. Only a carrier-correct lower-bound theorem may then identify that tangential cost with physical energy and mass.

[[pointed-facts-and-the-shorted-response]] now makes that reversal exact for a bounded positive response. Pointing among visible alternatives and forgetting distinctions inside an antecedent fibre are independent axes. If a whole-response form is split into retained and hidden blocks, minimizing over every compatible hidden extension produces the Schur short

$$
S_A=G-BC^{-1}B^*,
$$

which acts on the retained local distinction and equals its least whole-register cost. The short satisfies \(0\leq S_A\leq G\): background elimination can expose the residual tangential stiffness but cannot create it from a zero retained block. A mass candidate is therefore a positive lower edge of this shorted response, not the raw fibre, lost entropy, or forgetting projection.

The philosophical claim survives in a sharper form:

> Mass may be the calibrated rate-cost of keeping a local distinction pointed and dynamically persistent relative to the background its presentation excludes—not the norm of the excluded background and not the transverse act of forgetting it.

## Hubble rate and mass rate

After physical clock and action calibration, a rest mass has the proper-time phase-rate presentation

$$
\omega_m=\frac{mc^2}{\hbar}.
$$

The cosmological redshift rate in (CG3) is \(H\). Their quotient

$$
\boxed{
\mathcal N_m(t)
:=
\frac{\omega_m}{H(t)}
=
\frac{mc^2}{\hbar H(t)}}
\tag{CG14}
$$

is dimensionless. This is the correct type of observable target for a common-origin proposal. It does not identify the underlying structures: \(H\) is a logarithmic scale/redshift rate along cosmic time, while \(\omega_m\) is a phase or Euclidean-attenuation rate on a reconstructed mass sector. A theory must derive the comparison map and specify the epoch rather than equating two quantities merely because both have units of inverse time.

The noncircular construction sought by [[mass-as-a-calibrated-distinction-rate]] begins with a dimensionless positive tangential generator \(K_\parallel\) and a canonically normalized composition parameter. It must then construct:

1. a clock solder converting its edge into a frequency;
2. an action solder converting frequency into energy;
3. a map covering every physical nonvacuum direction; and
4. strongly commuting Poincare translation generators with forward-cone joint spectrum;
5. a full-carrier lower bound for their invariant Casimir, together with the theorem relating it to the Hamiltonian threshold.

Only after these arrows exist can (CG14) become a prediction rather than a unit conversion. A cosmological value of \(H\), \(G\), \(c\), or \(\hbar\) cannot be fitted to the desired gap and then advertised as its origin.

## Expansion is not a variable-\(c\) theory

Because \(c\) solders reconstructed length and clock quantity lines, a coordinated change of rods, clocks, and the numerical value assigned to \(c\) can redescribe the same observations. A physical varying-\(c\) proposal must specify modified dynamics and a changing dimensionless observable—such as a clock-frequency ratio or a dimensionless coupling—not merely \(c(t)\).

Nor does superluminal recession imply local light-speed violation or radiation crossing the edge of the observable universe. The Hubble sphere is not generally a particle or event horizon. Conformal coordinates can make null paths look unexpanded without removing redshift. The viable Copernican claim is about a different bookkeeping of the whole-to-part relation, not a coordinate relabeling presented as new dynamics.

## The acceleration and dimensional firewalls

Radiation redshift does not explain late acceleration inside unmodified Einstein gravity. With vanishing cosmological constant and ordinary positive radiation density,

$$
\frac{\ddot a}{a}
=
-\frac{4\pi G}{3c^2}
(\varepsilon+3p)
=
-\frac{8\pi G}{3c^2}\varepsilon_\gamma
<0.
\tag{CG15}
$$

A cosmic-geon model must therefore derive a modified whole-to-local dynamics, an effective negative-pressure contribution, or another forward prediction. Relabeling redshift as leakage cannot by itself produce acceleration.

There is nevertheless a dimensional clue. In \(D=d+1\) Einstein--FLRW dimensions, [[conformal-scale-geometry/dimensional-horizon-conversion]] proves

$$
\Theta_A\iota_A
=
\frac{2}{d-1}\rho_{\mathrm{crit}}V_A.
\tag{CG16}
$$

The coefficient becomes one at \(d=3\). This sits suggestively beside the special topology of ordinary knots, but it does not select three dimensions: the Einstein area law, Friedmann equation, and dimension have already been supplied. A dimensional-selection theorem would have to derive why the whole-to-part descent, knot or flux obstruction, and horizon conversion are jointly consistent only for \(d=3\).

## Stopping condition

The cosmic-geon hypothesis becomes a physical construction only if it provides:

1. a whole-register carrier with no secretly assumed external spacetime;
2. a typed family of accessible algebras and restriction, correspondence, or realization maps;
3. a self-consistent confinement invariant and a declared meaning of leakage;
4. a proof that its cosmological image yields (CG3) and/or (CG7)--(CG8), rather than fitting \(H(t)\);
5. an instrument and persistent-record structure for factual pointing;
6. a tangential response generator whose kernel is only the vacuum and whose positive edge is uniform in volume and regulator removal;
7. a nontrivial pure Yang--Mills theory on \(\mathbb R^4\), for the declared compact simple gauge group, satisfying the required OS/Wightman-strength axioms after continuum and infinite-volume reconstruction;
8. independent clock, action, carrier, and strongly commuting Poincare-translation solders, the forward-cone spectrum condition, and a full joint-Casimir lower bound;
9. a gravity-decoupling limit retaining that pure Yang--Mills theory and gap in infinite volume; and
10. at least one dimensionless prediction—such as a derived \(\omega_{\mathrm{gap}}/H_*\), a fossil signature, or a clock-ratio drift—that distinguishes the theory from a change of units or coordinates.

The exact gain is now visible. The cosmos can be modeled without imagining a container leaking into a larger spatial exterior: the apparent-horizon system already has a rigorous internal rate ledger. The open Copernican move is to construct one deeper whole-to-part law whose cosmological shadow is that ledger and whose local spectral shadow is a positive invariant mass floor. Until the common carrier and both realization maps exist, “cosmos as one geon” is a strong theorem-shaped hypothesis, not yet a solution of the mass-gap problem.
