# Horizon Saturation and the Entropic Cost of Distinction

A horizon supplies a precise model of boundary-relative saturation: for fixed areal radius, Schwarzschild compactness reaches unity at a definite mass, the semiclassical entropy scales with boundary area, and an exterior observer cannot distinguish putative realizations that agree on the complete exterior algebra. This does not force the ontology of a classical black-hole interior. It suggests a sharper pre-QFT programme in which localization need not continue past the reconstructed boundary, a black hole begins as an exterior equivalence class rather than a hidden material ball, entropy measures unresolved multiplicity relative to that exterior presentation, temperature gives an energy dimension to entropy variation when a thermodynamic or modular comparison exists, and a mass gap requires the further theorem that every nonvacuum physical direction has a uniform positive clock-energy cost.

**Status: [EXACT DIMENSIONAL IDENTITIES; STANDARD SEMICLASSICAL THERMODYNAMICS; CONDITIONAL ALGEBRAIC REFORMULATION; OPEN NO-INTERIOR RECONSTRUCTION].** The Schwarzschild, Bekenstein--Hawking, Hawking-temperature, relative-entropy, and semigroup identities below hold at their stated levels. Declining to make interior localization primitive is an ontological construction target, not a consequence of classical general relativity or existing Yang--Mills theory.

## What is actually saturated

Let \(R\) be areal radius, so a spherical surface has area \(A=4\pi R^2\), and define the compactness

$$
\chi(M,R)
:=
\frac{2GM}{Rc^2}.
$$

For the four-dimensional, neutral, nonrotating, asymptotically flat Schwarzschild family with \(M>0\), the event-horizon condition is

$$
\boxed{
\chi=1
\quad\Longleftrightarrow\quad
M_R=\frac{c^2R}{2G}.}
\tag{H1}
$$

This is the rigorous Schwarzschild kernel of “maximum mass for the space occupied.” Calling it a ceiling for a larger class requires a declared quasi-local mass and hypotheses on spherical symmetry, matter, and trapped surfaces. In a general spherically symmetric spacetime, the Misner--Sharp mass is instead defined by

$$
g^{ab}\nabla_aR\nabla_bR
=
1-\frac{2Gm_{\mathrm{MS}}}{Rc^2},
$$

and equality of the compactness ratio with one characterizes a marginal sphere, not automatically a global event horizon. There is no universal upper bound on ADM mass: asymptotically flat black holes can have arbitrarily large \(M\) by having larger \(R\), and charge, angular momentum, matter assumptions, and cosmological curvature change the relation.

At the Schwarzschild saturation point, four-dimensional Einstein gravity at leading semiclassical order gives

$$
S_{\mathrm{BH}}
=
\frac{k_BA}{4\ell_P^2}
=
\frac{\pi k_BR^2}{\ell_P^2}
=
\frac{4\pi k_BGM^2}{\hbar c},
\qquad
\ell_P^2=\frac{\hbar G}{c^3},
\tag{H2}
$$

Bekenstein's proposed entropy--energy bound for a system of effective radius \(R\) is

$$
S
\leq
\frac{2\pi k_BER}{\hbar c}.
$$

Within a comparison class for which both that bound and the compactness ceiling \(M\leq M_R\) apply, setting \(E=Mc^2\) gives the conditional chain

$$
\boxed{
S
\leq
\frac{2\pi k_BMcR}{\hbar}
\leq
\frac{\pi k_BR^2}{\ell_P^2}.}
\tag{H2a}
$$

The Schwarzschild configuration saturates both inequalities. This is the precise conjunction of “maximum mass for a fixed boundary scale” and “maximum entropy for the same scale.” The naive Bekenstein bound is not an unrestricted theorem for every possible definition of system, radius, and entropy; its regulator-safe QFT successor is the relative-entropy inequality below. [[library/universal-upper-bound-on-the-entropy-to-energy-ratio-for-bounded-systems/inq|Bekenstein's 1981 paper]] owns the proposed bound and its saturation claim.

The corresponding Hawking temperature at infinity, for Killing time normalized at spatial infinity, is

$$
k_BT_H
=
\frac{\hbar c^3}{8\pi GM}
=
\frac{\hbar c}{4\pi R}.
\tag{H3}
$$

Consequently, at this leading order,

$$
\boxed{T_HS_{\mathrm{BH}}=\frac12Mc^2.}
\tag{H4}
$$

The area law is therefore a boundary-saturation benchmark at fixed \(R\), not the statement that one universal object has both maximum mass and maximum entropy. Quantum and higher-curvature corrections can modify (H2)--(H4). In a static thermal equilibrium state, such as the Hartle--Hawking state, the local Tolman relation is

$$
T_{\mathrm{loc}}(r)
\sqrt{1-\frac{2GM}{rc^2}}
=
T_H^{(\infty)},
\qquad
r>\frac{2GM}{c^2}.
$$

An evaporating state with flux and greybody effects need not be an exactly Tolman-redshifted thermal bath.

A cosmological scale makes the relativity explicit. For the Schwarzschild--de Sitter convention

$$
f(r)
=
1-\frac{2GM}{c^2r}-\frac{\Lambda r^2}{3},
\qquad
\Lambda>0,
$$

distinct positive black-hole and cosmological horizons require

$$
M>0,
\qquad
0<\frac{3GM\sqrt{\Lambda}}{c^2}<1.
$$

The Nariai endpoint obeys

$$
9G^2M_{\mathrm N}^2\Lambda/c^4=1,
\qquad
M_{\mathrm N}
=
\frac{c^2}{3G\sqrt{\Lambda}},
\qquad
r_b=r_c=\Lambda^{-1/2},
$$

but \(M\) here is a metric parameter, not an asymptotically flat ADM mass, and its maximum exists only after the external scale \(\Lambda^{-1/2}\) has been supplied. Counting both limiting horizon components,

$$
S_{\mathrm{N,tot}}
=
\frac{2\pi k_B}{\Lambda\ell_P^2}
<
\frac{3\pi k_B}{\Lambda\ell_P^2}
=
S_{\mathrm{dS}}.
$$

[[library/black-holes-and-entropy/inq|Bekenstein]] introduced horizon area as inaccessible information and the generalized second law. [[library/particle-creation-by-black-holes/inq|Hawking]] fixed the temperature and the \(1/4\) coefficient. [[library/cosmological-event-horizons-thermodynamics-and-particle-creation/inq|Gibbons and Hawking]] made the observer-relative cosmological horizon explicit.

## No interior is a coherent reconstruction target

The recovery target is not a visible interior object. It is a family of observed exterior responses—charges, lensing, orbital dynamics, absorption, ringdown, and merger radiation—together with semiclassical predictions such as horizon thermodynamics and Hawking emission. Classical GR extends the exterior solution through a horizon and assigns geometry to an interior. A deeper theory is not logically required to promote that continuation into primitive ontology if it reproduces the complete exterior observable and dynamical structure.

The word *exterior* must itself be operational rather than imported from a pre-assumed classical interior. Let \(\mathfrak A_{\mathrm{ext}}\) be the algebra generated by all observables available in a declared asymptotic or domain-of-outer-communications experiment, including its time evolution and radiation observables, and let \(\mathfrak A_{\mathrm{pre}}\) be a candidate upstream algebra. A unital embedding

$$
j:
\mathfrak A_{\mathrm{ext}}
\hookrightarrow
\mathfrak A_{\mathrm{pre}}
$$

defines exterior restriction of each candidate prestate \(\omega_x\). Define

$$
x\sim_{\mathrm{ext}}y
\quad\Longleftrightarrow\quad
\omega_x\circ j
=
\omega_y\circ j.
\tag{H5}
$$

The exterior black-hole object can begin as the equivalence class \([x]_{\mathrm{ext}}\), labelled at minimum by the exterior charges that survive restriction. Its restricted state has a GNS representation

$$
(\pi_x,\mathcal H_x,\Omega_x)
:=
\operatorname{GNS}(\omega_x\circ j).
\tag{H5a}
$$

Calling such a class a **sector** requires a further criterion—factoriality, quasi-equivalence, disjointness, a central character, or another declared representation-theoretic relation. Calling the boundary **terminal** would likewise require an actual category and universal property. No set of localized interior “things” appears in the target algebra merely from (H5). In this precise sense, “nothing inside” can mean **no independently individuated interior object in the exterior observable theory**. It does not mean that an empty subset of an already assumed interior manifold has been proved to exist.

This is structurally like the modern meaning of particle. A particle is not fundamentally a tiny visible bead; it is identified through a representation of observable symmetry and scattering structure. A black hole may analogously begin as a charge-labelled exterior equivalence class and become a mass-labelled boundary or asymptotic sector only after the GNS and sector criteria are proved; its upstream realization need not be represented by interior-localized objects.

The hypothesis incurs a strict recovery debt. It must reconstruct all exterior predictions, causal response, conserved charges, horizon thermodynamics, perturbative ringdown, and unitary or otherwise explicitly stated information accounting. Calling the GR singularity a symptom is philosophically admissible; replacing the interior is physics only after those maps and predictions exist.

## Entropy measures unresolved alternatives, not non-being

If an explicitly constructed finite realization fiber has \(N\) equiprobable alternatives, its Shannon information is \(s=\log N\) nats. Multiplication by \(k_B\) expresses it in thermodynamic entropy units, but thermodynamic interpretation additionally requires an ensemble and suitable dynamics. Under a microstate interpretation, the semiclassical area law suggests the effective multiplicity

$$
N_{\mathrm{eff}}
\sim
\exp\!\left(\frac{A}{4\ell_P^2}\right),
\tag{H6}
$$

but no finite microstate set is thereby constructed. In an operator-algebraic theory, relative entropy, subfactor index, or modular data are distinct possible measures of information loss; none can replace literal cardinality without a carrier-specific comparison theorem.

The phrase “nothing in particular” is captured by the fiber before a point is selected: exterior facts determine an equivalence class, not one underlying realization. Entropy quantifies the unresolved alternatives relative to that coarse observable presentation. It is not the quantity of non-being, and it does not itself select which realization obtains.

This also corrects the strongest form of “facts require entropy.” A pure state can have zero von Neumann entropy and still support definite records. What fact formation requires is an algebra of alternatives, a state or weighting when probabilities are used, an obtained point, and a persistent record. Positive entropy or relative-entropy loss may quantify unresolved or discarded distinctions, but noninjectivity alone does not force positive output entropy.

## The exact entropy--energy solder

Entropy and energy are different types. In finite dimensions, let \(\sigma\) be a faithful reference state and define its dimensionless modular Hamiltonian

$$
K_\sigma:=-\log\sigma.
$$

For another state \(\rho\), write \(s(\rho)=-\operatorname{Tr}(\rho\log\rho)\). Then quantum relative entropy satisfies

$$
\boxed{
D(\rho\Vert\sigma)
=
\Delta\langle K_\sigma\rangle
-
\Delta s
\geq0,}
\tag{H7}
$$

where differences are taken from \(\sigma\) to \(\rho\). For a faithful Gibbs reference at \(T>0\),

$$
\sigma
=
Z^{-1}e^{-H/(k_BT)},
$$

equation (H7) becomes

$$
\boxed{
k_BT\,D(\rho\Vert\sigma)
=
\Delta\langle H\rangle
-
T\Delta S.}
\tag{H8}
$$

This is the clean algebraic role of temperature: \(k_BT\) converts a dimensionless relative entropy into the units of a free-energy difference when the reference state is genuinely Gibbs for \(H\). It is not a generic energy cost for each distinction. For local type-III QFT algebras there need be no density matrix or finite absolute entropy; Araki relative entropy and the relative modular operator are the correct intrinsic objects. [[library/relative-entropy-and-the-bekenstein-bound/inq|Casini's formulation of the Bekenstein bound]] uses the regulator-independent statement

$$
D_{\mathfrak A}(\rho\Vert\sigma)\geq0.
$$

When the vacuum-subtracted terms exist separately, this may be displayed as

$$
\frac{\Delta S}{k_B}
\leq
\Delta\langle K\rangle
$$

for a state and the vacuum restricted to a region. On a general type-III algebra those two displayed terms need not exist separately, so the relative-entropy statement is primary rather than shorthand for a difference of divergent quantities.

The operator ledger matters:

| Object | Operates on | Returns |
|---|---|---|
| restriction or channel | global states or observables | exterior/coarse state or algebra |
| Shannon or von Neumann entropy | one probability law or state on a declared algebra | dimensionless uncertainty or mixedness |
| relative entropy | an ordered pair of states on the same algebra | dimensionless distinguishability |
| modular operator | a standard/GNS carrier with faithful normal state or cyclic-separating vector, or the appropriate support restriction | dimensionless modular flow |
| relative modular operator | a standard carrier and ordered state pair | relative modular comparison |
| clock Hamiltonian | the physical Hilbert carrier | energy and reversible time translations |
| temperature or another yardstick | entropy units and clock normalization | an energy comparison |

An identification \(K=H/(k_BT)+\text{constant}\) holds for the finite Gibbs density matrix above, not for every modular Hamiltonian. For a general KMS state, the modular automorphism group can agree with a rescaled physical automorphism group on the algebra without identifying its standard-form modular generator with \(H\) on the same Hilbert carrier. For a stationary Killing horizon, with a specified normalization of its generator and an appropriate regular Hawking/KMS state, surface gravity provides the comparison. If \(\kappa_{\mathrm{acc}}\) has acceleration units,

$$
k_BT
=
\frac{\hbar|\kappa_{\mathrm{acc}}|}{2\pi c}
\tag{H9}
$$

if \(\kappa_{\mathrm{geom}}\) has inverse-length units, the equivalent convention is \(k_BT=\hbar c|\kappa_{\mathrm{geom}}|/(2\pi)\). The Unruh formula uses proper acceleration in the first convention. This displays all four types: geometric acceleration, \(c\) as the space--time unit comparison, \(\hbar\) as frequency--energy conversion, and \(k_B\) as nat--temperature conversion. The Killing-vector normalization rescales both surface gravity and temperature and remains an input unless a deeper geometry selects it.

## Irreversible order is not clock time

Unitary Lorentzian evolution preserves the fine-grained entropy of a closed state. Let \(\Phi_*\) be a CPTP map on states, equivalently the predual of a normal unital completely positive map on observables. Data processing gives, with values allowed in \([0,\infty]\),

$$
D(\rho\Vert\sigma)
\geq
D(\Phi_*\rho\Vert\Phi_*\sigma).
\tag{H10}
$$

Information distinguishability cannot increase after declared distinctions are forgotten. Equality can hold for unitary or recoverable channels. When the relative entropies are finite and the usual support hypotheses hold, equality has the Petz recovery characterization; extended-valued equality such as \(+\infty=+\infty\) does not establish recoverability. Irreversible loss therefore requires a declared state family and strict loss or a proved failure of recovery. Data processing supplies an information-accessibility preorder, not by itself a record order. A directed record order additionally requires a specified channel family or algebra inclusion, a persistent record subalgebra, compatible dynamics, and a no-recovery or monotonicity law along that family. [[causal-patch-boundary-and-two-times]] separates such one-sided order from Lorentzian clock time, Euclidean preparation depth, and modular flow.

A horizon is a natural place for this distinction because exterior accessibility changes what can be compared. But neither a partial trace nor an algebra restriction proves that something ontologically exists on the discarded side. It only defines the equivalence relation seen by the retained algebra.

## The mass gap as a vacuum-complement Euclidean decay scale

Now let \(H\geq0\) be the physical vacuum Hamiltonian, let \(P_0=E_H(\{0\})\) be its complete zero-energy projection, and suppose a proven lower bound \(\delta>0\) satisfies

$$
H\geq\delta(1-P_0).
$$

Then, for \(\tau\geq0\), Euclidean clock evolution satisfies the exact contraction bound

$$
\left\|
e^{-\tau H/\hbar}(1-P_0)
\right\|
\leq
e^{-\tau\delta/\hbar}.
\tag{H11}
$$

Writing \(a=c\tau\geq0\) gives the uniform decay-length bound

$$
\boxed{
\xi_\delta
=
\frac{\hbar c}{\delta},
\qquad
\left\|
e^{-aH/(\hbar c)}(1-P_0)
\right\|
\leq
e^{-a/\xi_\delta}.}
\tag{H12}
$$

If \((1-P_0)\mathcal H\neq\{0\}\) and \(\delta=\Delta_E:=\inf\sigma(H|_{(1-P_0)\mathcal H})\) is the optimal positive threshold, then \(\xi_{\mathrm{gap}}=\hbar c/\Delta_E\) is the optimal worst-case vacuum-complement contraction length. If \(\delta\) is merely a nonoptimal proven lower bound, then \(\xi_{\mathrm{gap}}\leq\xi_\delta\). Only after Poincare covariance, the spectrum condition, and the invariant joint-spectrum threshold have been recovered may one identify \(m_{\mathrm{gap}}=\Delta_E/c^2\) and write \(\xi_{\mathrm{gap}}=\hbar/(m_{\mathrm{gap}}c)\).

This is a rigorous sense in which a mass gap supplies scale: it controls Hilbert-norm contraction under Euclidean evolution. The map \(e^{-\tau H/\hbar}\) is not a trace-preserving quantum channel, so (H11) is not itself operational distinguishability or relative-entropy decay. Vectors supported above the threshold decay faster. Under additional locality and spectral hypotheses the gap is related to exponential clustering of separated observables. It is not a spatial pixel, a minimum observable distance, or entropy production under real-time unitary evolution.

The entropy route to a Yang--Mills gap would therefore need a lower bound, not merely an entropy ceiling. Define the Hamiltonian form

$$
h[\Psi]
:=
\|H^{1/2}\Psi\|^2,
\qquad
D(h)=D(H^{1/2}).
$$

A candidate construction must produce a state-perturbation map whose pullback makes a relative-entropy Hessian into a closed positive dimensionless form \(\mathfrak d_{\mathrm{ent}}\) on the same physical carrier, with \(D(h)\subseteq D(\mathfrak d_{\mathrm{ent}})\). For every \(\Psi\in D(h)\), it must prove

$$
\mathfrak d_{\mathrm{ent}}[\Psi]
\geq
\kappa_{\mathrm{ent}}
\|(1-P_0)\Psi\|^2,
\qquad
h[\Psi]
\geq
\eta_{\mathrm{sol}}E_*
\mathfrak d_{\mathrm{ent}}[\Psi].
\tag{H13}
$$

Then

$$
H
\geq
\eta_{\mathrm{sol}}\kappa_{\mathrm{ent}}E_*(1-P_0).
$$

The conclusion is an operator inequality in quadratic-form sense, assuming \(\kappa_{\mathrm{ent}},\eta_{\mathrm{sol}},E_*>0\). The possible role of temperature is exact but restricted: \(E_*\) could be calibrated by a canonically selected \(k_BT_*\) only if the resulting coefficient survives as a state-independent zero-temperature Yang--Mills scale after gravity and acceleration are removed. An Unruh or Hawking temperature does not suffice unless the programme independently derives its acceleration or surface gravity, maps its modular carrier to the Yang--Mills vacuum carrier, and proves the two inequalities in (H13). Positivity of relative entropy gives an upper entropy bound; it does not by itself give \(\kappa_{\mathrm{ent}}>0\).

[[compensated-incidence-response-and-four-dimensional-balance]] makes one possible scale law precise. If logarithmic length is \(A\), an order-one inverse-length presentation contributes \(e^{-2A}\) to its squared pullback form. A codimension-two cut in \(D\) spacetime dimensions has area character \(e^{(D-2)A}\), so a response with that independently derived two-sided power character would be scale-neutral only for \(D=4\). The word *response* is load-bearing: an area law, a number of boundary channels, or entropy proportional to area does not imply that the entropy Hessian obeys \(R_{\mathrm{ent}}\gtrsim e^{(D-2)A}\) on every normalized physical tangent. Local or boundary channels may share blind directions. Even in four dimensions the residual dimensionless running must have a positive lower edge. The four-dimensional balance is therefore a conditional construction target for \(\kappa_{\mathrm{ent}}>0\), not a consequence of black-hole entropy and not a source of \(E_*\).

## Stopping condition for the no-interior route

The hypothesis becomes physics only after it supplies:

1. a boundary or exterior observable algebra and a non-circular map from the proposed pre-observable carrier;
2. an exterior equivalence class, and then any claimed GNS sector, reconstructed from the complete exterior dynamics without presupposing an interior manifold;
3. the area law and generalized second law in an operator-algebraic form, with finite relative quantities;
4. a derivation of the clock normalization or temperature scale rather than insertion of the desired mass;
5. a state-to-tangent map and entropy Hessian satisfying a uniform lower-frame bound \(\mathfrak d_{\mathrm{ent},n}[\Psi]\geq\kappa_{\mathrm{ent},n}\|(1-P_{0,n})\Psi\|^2\), with explicit carrier-identification maps, a positive uniform \(\liminf_n\kappa_{\mathrm{ent},n}\), generalized Mosco or another adequate convergence of the pulled-back entropy and Hamiltonian forms, and convergence of the vacuum projections;
6. an independent same-carrier domination \(h\geq\eta_{\mathrm{sol}}E_*\mathfrak d_{\mathrm{ent}}\); and
7. exact or controlled recovery of the \(G\)-free pure Yang--Mills carrier, local observable net, gauge identities, locality, Poincare covariance, spectrum condition, nontriviality, vacuum, and limiting Hamiltonian form when the claim concerns the Clay problem.

Until then, the productive conjecture is not “black holes prove the mass gap.” It is:

$$
\boxed{
\begin{aligned}
\text{boundary saturation}
&\longrightarrow
\text{exterior equivalence classes},\\
\text{entropy}
&\longrightarrow
\text{a candidate dimensionless distinction form},\\
\text{uniform coverage}
&\longrightarrow
\mathfrak d_{\mathrm{ent}}\geq
\kappa_{\mathrm{ent}}(1-P_0),\\
\text{same-carrier energy domination}
&\longrightarrow
h\geq\eta_{\mathrm{sol}}E_*\mathfrak d_{\mathrm{ent}},\\
\text{both inequalities}
&\Longrightarrow
H\geq
\eta_{\mathrm{sol}}\kappa_{\mathrm{ent}}E_*(1-P_0).
\end{aligned}}
$$

Every arrow has a different source and target. That is the conceptual chain the operator construction must realize.
