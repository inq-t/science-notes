# Pair-Annihilation Quotient and the Baryon-Acoustic Carrier

Pair annihilation supplies a concrete physical model of descent with a retained directed residue. In comoving variables, creation or annihilation changes baryon and antibaryon populations together, so it moves along the diagonal pair direction while preserving their difference. Quotienting that cancelable direction leaves net baryon number; an algebraic complete-annihilation retraction forgets the symmetric pair load and exposes one oriented survivor sector. The later mass solder folds its two orientations into a positive rest-energy loading, so standard photon--baryon transfer can retain only the magnitude of the survivor abundance. BAO is therefore downstream of one highly compressed material consequence, not evidence for the annihilation history, its directed sign, or an event at the conditionally retyped \(46.27\,\mathrm{MeV}\) causal-grain presentation.

**Status: [EXACT] for the pair quotient, algebraic complete-annihilation retraction, binary-information identities, and conditional conservation statements; [STANDARD] for equilibrium population formulas and photon--baryon loading; [NUMERICAL DIAGNOSTIC] for the ideal-nucleon exposure temperatures; [INTERPRETIVE TEMPLATE] for causal descent; [OPEN] for a common-origin map from the causal grain and for any Yang--Mills realization.**

## The cancelable direction and its residue

Fix a comoving reference cell and let

$$
\mathcal C:=\mathbb R_{\geq0}^2
$$

carry its coarse-grained comoving baryon--antibaryon populations

$$
x=(b,\bar b),
\qquad
b:=a^3n_B,
\qquad
\bar b:=a^3n_{\bar B}.
$$

Thus \(b\) and \(\bar b\) are comoving number densities, not dimensionless numbers. Expansion alone has been removed from these variables. In physical-density coordinates, the Hubble dilution term is not diagonal pair annihilation and must be kept separately.

Pair creation and annihilation change the two entries by the same amount. Their reversible presentation direction is therefore the diagonal

$$
\Delta:=\{(r,r):r\in\mathbb R\}.
$$

The linear difference map

$$
q:\mathbb R^2\longrightarrow\mathbb R,
\qquad
q(b,\bar b):=b-\bar b
\tag{BQ1}
$$

has \(\ker q=\Delta\), so group completion gives the exact sequence

$$
0
\longrightarrow
\Delta
\longrightarrow
\mathbb R^2
\xrightarrow{\,q\,}
\mathbb R
\longrightarrow
0.
\tag{BQ2}
$$

On the positive cone, two population states have the same quotient class exactly when they have the same difference:

$$
(b,\bar b)\sim(b',\bar b')
\quad\Longleftrightarrow\quad
b-\bar b=b'-\bar b'.
\tag{BQ3}
$$

Every equivalence class has one representative of least total population. It is selected by

$$
\boxed{
\Pi(b,\bar b)
=
\bigl((b-\bar b)_+,(\bar b-b)_+\bigr),
}
\tag{BQ4}
$$

where \(u_+:=\max(u,0)\). The map obeys

$$
\Pi^2=\Pi,
\qquad
q\Pi=q,
\qquad
\operatorname{im}\Pi
=
\bigl(\mathbb R_{\geq0}\times\{0\}\bigr)
\cup
\bigl(\{0\}\times\mathbb R_{\geq0}\bigr).
\tag{BQ5}
$$

It is noninjective: every amount of symmetric comoving pair load

$$
L_{\mathrm{pair}}(b,\bar b)
:=
b+\bar b-|b-\bar b|
=
2\min(b,\bar b)
\tag{BQ6}
$$

is forgotten. It is also deterministic. Apparent indeterminacy arises only if one is given \(\Pi(x)\) and asked to reconstruct the erased point on its diagonal fiber.

This is an exact reduced-carrier instance of the structure described in [[sufficient-reason/noninvertible-presentation-and-apparent-chance]]: local forward evolution can be completely determined while its coarse output has no unique inverse. Physical annihilation does not establish destruction of information in the complete microscopic state. It establishes forgetting after restriction to the baryon-population carrier.

## The boundary is where an oriented residue is exposed

Write

$$
S:=b+\bar b,
\qquad
D:=b-\bar b.
\tag{BQ7}
$$

The projection \(\Pi\) selects the unique least-population representative in each fiber: \(S=|D|\), precisely on one axis of \(\mathcal C\). The sign of \(D\) selects which axis:

$$
D>0\Rightarrow\Pi(b,\bar b)=(D,0),
\qquad
D<0\Rightarrow\Pi(b,\bar b)=(0,-D).
\tag{BQ8}
$$

The diagonal \(D=0\) is the wall between those branches. Nothing in (BQ1)--(BQ8) chooses the sign; baryogenesis or an earlier boundary condition must supply it. Once a sign is supplied and difference-changing reactions are absent, pair processes cannot erase it. But \(\Pi\) is an algebraic complete-annihilation retraction, not a generic physical terminal evolution. A finite-rate reaction network can remain in chemical equilibrium, approach an axis only asymptotically, or freeze with a nonzero minority population.

For \(S>0\), normalize the residue by the currently accessible population:

$$
m_B:=\frac{D}{S},
\qquad
g_B:=\frac{4b\bar b}{S^2}.
\tag{BQ9}
$$

Then

$$
\boxed{m_B^2+g_B=1.}
\tag{BQ10}
$$

If \(b,\bar b>0\), define

$$
p_B:=\frac bS,
\qquad
p_{\bar B}:=\frac{\bar b}{S},
\qquad
\theta_B:=\frac12\log\frac b{\bar b},
\tag{BQ11}
$$

the exact binary chart is

$$
m_B=\tanh\theta_B,
\qquad
g_B=\operatorname{sech}^2\theta_B.
\tag{BQ12}
$$

On the terminal axes, (BQ12) extends only by the limits \(\theta_B\to\pm\infty\); (BQ9)--(BQ10) themselves remain well-defined there.

Thus the same balanced binary geometry used in [[binary-information-geometry/inq]] occurs on an ordinary physical carrier. Here \(m_B\) is population orientation and \(g_B\) is its binary susceptibility or complement. Neither is a mass, Hamiltonian gap, entropy, or causal-grain valuation. The algebraic identity supplies the grammar; the population dynamics supplies the directed path through it.

## The annihilation operator is vertical, not massive

The rate operator must be typed just as carefully as the quotient. Let a pair-reaction vector field have the form

$$
V(b,\bar b)
=
\alpha(b,\bar b)(1,1).
\tag{BQ12a}
$$

Then

$$
\mathrm Dq_{(b,\bar b)}V(b,\bar b)=0.
\tag{BQ12b}
$$

Equivalently, if a Markov generator \(\mathcal L_{\mathrm{pair}}\) permits only pair moves within the fibers of \(q\), every observable depending only on the retained difference is harmonic:

$$
\mathcal L_{\mathrm{pair}}(F\circ q)=0
\qquad
\text{for every admissible }F.
\tag{BQ12c}
$$

The pair-reaction generator can have a positive relaxation edge after one fixes \(D\) and removes its conserved modes. That edge measures vertical approach toward the minimal or equilibrium representative inside one quotient fiber. It cannot be the energetic mass of the retained baryon sector, because its descended action on functions of \(D\) is zero.

This is the finite physical analogue of the vertical-coercivity result in [[descent-loss-cocycle-and-recovery-fork]]: a channel can strongly charge what it forgets while inducing no positive form on what it retains. The mass solder in (BQ25) must therefore come from a different operator. Comparing a collision rate with \(H\) diagnoses kinetic memory; it does not derive a Poincare-Casimir gap.

## Entropy normalizes the retained charge

During an epoch in which net baryon number and total comoving entropy are conserved,

$$
Q_B:=a^3(n_B-n_{\bar B}),
\qquad
S_c:=a^3s
\tag{BQ13}
$$

are separately constant. By the carrier definition above, \(Q_B=D=q(b,\bar b)\). It is a comoving number density, not a dimensionless charge. Their quotient

$$
Y_B:=\frac{n_B-n_{\bar B}}s
=
\frac{Q_B}{S_c}
\tag{BQ14}
$$

is a dimensionless retained charge per entropy capacity. Pair annihilation transfers energy and entropy into the surrounding bath while leaving \(Q_B\) unchanged. In an adiabatic equilibrium treatment it need not produce net comoving entropy; disappearance of a species, trace loading, and entropy production are different statements, as [[trace-residue-as-a-scale-cocycle]] makes explicit.

Equation (BQ14) is a useful physical analogue of “causal charge,” not an identification with the workspace's proposed primitive causal charge. Standard Model baryon number is also not exact at every scale: the conditional conservation claim applies only after baryon-number-changing processes are negligible.

## Chemical equilibrium gives the hyperbolic coordinate

Use natural units \(k_B=\hbar=c=1\) throughout this thermodynamic block. In a Maxwell--Boltzmann baryon gas whose particles carry charges \(\pm1\), let \(n_0(T)\) be the zero-chemical-potential physical density on one sign branch. Chemical equilibrium gives

$$
n_B=n_0(T)e^{\mu_B/T},
\qquad
n_{\bar B}=n_0(T)e^{-\mu_B/T}.
\tag{BQ15}
$$

Therefore

$$
\theta_B=\frac{\mu_B}{T},
\qquad
n_B-n_{\bar B}
=
2n_0(T)\sinh\theta_B.
\tag{BQ16}
$$

For an adiabatic history with supplied \(Y_B\), define

$$
u(T)
:=
\frac{Y_Bs(T)}{2n_0(T)}
=
\sinh\theta_B.
\tag{BQ17}
$$

Then

$$
m_B(T)
=
\frac{u(T)}{\sqrt{1+u(T)^2}},
\qquad
g_B(T)
=
\frac1{1+u(T)^2},
\tag{BQ18}
$$

and

$$
\frac{n_{\bar B}}{n_B}
=
e^{-2\operatorname{arsinh}u}
=
\bigl(\sqrt{1+u^2}-u\bigr)^2.
\tag{BQ19}
$$

At high temperature \(n_0/s\) is large, so \(u\ll1\): the retained difference is almost invisible inside a nearly symmetric pair population. Cooling suppresses \(n_0\), \(u\) grows, and the same conserved difference becomes the dominant surviving population. Mass does not first come into existence at this crossover. A previously present oriented charge becomes materially exposed after its cancelable background has drained away.

One possible information-geometric reference point is

$$
m_B^2=g_B=\frac12
\quad\Longleftrightarrow\quad
|u|=1.
\tag{BQ20}
$$

On the observed positive-baryon branch, \(u=+1\), and then

$$
u=1
\quad\Longleftrightarrow\quad
\frac{n_{\bar B}}{n_B}=(\sqrt2-1)^2.
\tag{BQ20a}
$$

This balance is mathematically canonical inside the declared binary chart, but nature is not required to mark it as an event.

## The \(46\,\mathrm{MeV}\) thermal reading fails this first test

For an ideal proton--neutron gas,

$$
n_0(T)
=
\frac{g_Nm_N^2T}{2\pi^2}K_2(m_N/T),
\qquad
g_N=4,
\tag{BQ21}
$$

on one baryon-sign branch. Using \(Y_B=8.7\times10^{-11}\), selected [[library/primordial-gravitational-waves-precisely/inq|Saikawa--Shirai]] entropy-degree rows, and log-linear interpolation gives the diagnostic values

$$
\begin{aligned}
T=46.2747\,\mathrm{MeV}:&
\quad
u\simeq0.006825,
\quad
m_B\simeq0.006825,
\quad
\frac{n_{\bar B}}{n_B}\simeq0.98644,\\
u=1:&
\quad
T_{\mathrm{bal}}\simeq36.6\,\mathrm{MeV}.
\end{aligned}
\tag{BQ22}
$$

This stripped-down calculation omits the hadron-resonance gas, quantum-statistical corrections, reaction kinetics, chemical-potential constraints, and uncertainties. Its purpose is negative: even after one makes the extra identification \(E_g=k_BT\), the retyped \(46.27\,\mathrm{MeV}\) value does not select the declared \(|u|=1\) balance criterion. [[library/evolution-of-antibaryon-abundances-in-the-early-universe-and-in-heavy-ion-collisions/inq|Satarov, Mishustin, and Greiner]] likewise find that the primordial baryon and antibaryon populations remain nearly symmetric above roughly \(50\,\mathrm{MeV}\), with the conserved excess becoming important during later annihilation and residual antibaryon freeze-out occurring at still lower temperature. This neither excludes the broader pair-exposure epoch nor establishes any causal connection between that epoch and the grain.

Most importantly,

$$
E_g=\frac{\hbar c}{\lambda_g}
\qquad\not\Rightarrow\qquad
E_g=k_BT_{\mathrm{event}}.
\tag{BQ23}
$$

The left side is a reduced-Compton presentation of a conditionally calibrated length. The right side would be a new material/thermal solder. Equation (BQ22) rejects only the selected \(|u|=1\) event criterion; it does not rule out every possible thermal event definition, and it does not touch a nonthermal causal-grain class.

## BAO carries only unsigned survivor loading after a mass solder

Once the minority population is negligible and baryon number is effectively conserved, the positive rest-energy density is

$$
\varepsilon_b(a)
\simeq
\bar m_bc^2\frac{|Q_B|}{a^3}
=
\bar m_bc^2|Y_B|s(a),
\tag{BQ24}
$$

where \(\bar m_b\) is the appropriate mass per surviving baryon after composition and binding are specified, and \(s(a)\) is the physical entropy density in the convention of (BQ14). On the observed positive-baryon branch, the absolute-value signs are redundant. The two typed versions of the material solder are

$$
\boxed{
Q_B
\xrightarrow{\ |\cdot|/a^3\ }
|n_B-n_{\bar B}|
\xrightarrow{\ \bar m_bc^2\ }
\varepsilon_b(a),
\qquad
Y_B
\xrightarrow{\ |\cdot|s(a)\ }
|n_B-n_{\bar B}|
\xrightarrow{\ \bar m_bc^2\ }
\varepsilon_b(a).}
\tag{BQ25}
$$

This solder is not orientation-preserving: it identifies \(Q_B\) and \(-Q_B\). The quotient construction explains why a directed population residue can survive pair reactions, but it does not derive \(\bar m_b\), the QCD scale, or a mass gap.

In the tightly coupled photon--baryon plasma, use rest-energy densities for both components and define

$$
R_b(a)
:=
\frac{3\varepsilon_b(a)}{4\varepsilon_\gamma(a)},
\qquad
c_s^2(a)
=
\frac{c^2}{3(1+R_b(a))}.
\tag{BQ26}
$$

The comoving sound horizon is an integrated functional of this loading and the expansion history:

$$
r_s(a)
=
\int^a_0
\frac{c_s(a')}{a'^2H(a')}
\,\mathrm da'.
\tag{BQ27}
$$

Its two nearby but distinct endpoints must not be conflated:

$$
r_s(a_*)\longrightarrow\mathcal O_{\mathrm{CMB}},
\qquad
r_s(a_d)=:r_d\longrightarrow\mathcal O_{\mathrm{BAO}},
\tag{BQ27a}
$$

where \(a_*\) is photon last scattering and \(a_d\) is baryon drag. The quotient-to-loading chain is therefore only

$$
\boxed{
(b,\bar b)
\xrightarrow{\ \pi\ }
[(b,\bar b)]_\Delta
\xrightarrow{\ \bar q\ }
Q_B
\xrightarrow{\ |\cdot|\ }
|Q_B|
\xrightarrow{\ \bar m_bc^2/a^3\ }
\varepsilon_b(a),
}
\tag{BQ28}
$$

where \(\pi\) is the quotient map and \(\bar q([(b,\bar b)]_\Delta)=b-\bar b\) is the induced coordinate on the quotient. Producing an acoustic observable additionally requires independent primordial perturbations, metric and dark-matter evolution, the expansion history, recombination, opacity, and drag physics:

$$
\bigl(\varepsilon_b,\mathcal P_{\mathcal R},
\text{metric/dark matter},H,
\text{recombination/opacity/drag}\bigr)
\xrightarrow{\ \mathfrak T_{\mathrm{ac}}\ }
(\mathcal O_{\mathrm{CMB}},\mathcal O_{\mathrm{BAO}}).
\tag{BQ28a}
$$

In a charge-conjugation-symmetric material and transfer model, this readout obeys the exact evenness relation

$$
\boxed{
\mathfrak T_{\mathrm{ac}}(Q_B;\mathcal I)
=
\mathfrak T_{\mathrm{ac}}(-Q_B;\mathcal I),
}
\tag{BQ28b}
$$

for fixed charge-even inputs \(\mathcal I\). Equivalently, the comparison conjugates the complete material sector—electrons with positrons and nuclei with antinuclei—while holding its charge-even masses, cross sections, perturbations, and background history fixed. Acoustic data in this loading channel therefore cannot retain the orientation sign; this is not a claim that every conceivable pre-CMB observable is charge blind. Nor can the channel identify an annihilation trajectory: any earlier history producing the same \(|Y_B|\), entropy history, masses, perturbations, and transfer inputs has the same standard acoustic readout. The defensible shell-casing statement is narrower: BAO is a downstream record of the magnitude of surviving baryon loading, conditional on the standard intervening history. It is not a microscopic wavelength stretched into \(147\,\mathrm{Mpc}\), and it is not evidence for the quotient operation that happened upstream. [[library/baryonic-features-in-the-matter-transfer-function/inq|The standard baryonic transfer calculation]] owns the acoustic propagation; the quotient supplies only one possible upstream description of the survivor abundance.

## The causal-grain hypothesis now has a typed target

Let \(\omega_{\mathrm{wall}}\) be a proposed pre-clock transition class. To claim that the baryon-acoustic residue is its descendant requires maps

$$
\omega_{\mathrm{wall}}
\xrightarrow{\ \mathfrak R_B\ }
(b,\bar b)
\xrightarrow{\ \pi\ }
[(b,\bar b)]_{\Delta}
\xrightarrow{\ \bar q\ }
Q_B
\xrightarrow{\ |\cdot|/S_c\ }
|Y_B|
\xrightarrow{\ \mathfrak M_{\mathrm{QCD}}\ }
\varepsilon_b(a)
\xrightarrow{\ \mathfrak T_{\mathrm{ac}}\ }
(\mathcal O_{\mathrm{CMB}},\mathcal O_{\mathrm{BAO}}).
\tag{BQ29}
$$

Every arrow has a different type:

1. \(\mathfrak R_B\) realizes a pre-observable class on a material pair carrier;
2. \(\pi\) forgets symmetric pair load, while \(\bar q\) identifies the oriented quotient coordinate with \(Q_B\);
3. \(|\cdot|/S_c\) discards that orientation and normalizes the survivor magnitude by entropy capacity;
4. \(\mathfrak M_{\mathrm{QCD}}\) supplies mass per charge, dilution, composition, and constitutive history;
5. \(\mathfrak T_{\mathrm{ac}}\), together with the independent inputs in (BQ28a), propagates the positive loading into finite observables.

Neither the common-count calibration nor the numerical value of \(Y_B\) constructs these maps. The same-origin claim becomes testable only if \(\mathfrak R_B\) and the metric-grain branch are independently derived from one \(\omega_{\mathrm{wall}}\), and a predeclared charge-even finite signature of that class survives the acoustic readout in [[trace-residue-as-a-scale-cocycle#The fossil readout is a quotient operator|the finite-rank fossil theorem]]. A directed signature requires some other observable because (BQ28b) puts it in an acoustic equivalence class.

## What this teaches the mass-gap programme

The pair model separates four structures that “mass switched on” can otherwise blur:

$$
\begin{array}{rcl}
\text{cancelable direction}
&=&
\ker q,\\[2pt]
\text{retained distinction}
&=&
\mathcal C/{\sim},\\[2pt]
\text{least-population representative}
&=&
\Pi,\\[2pt]
\text{energetic cost}
&=&
\text{a positive form on the retained carrier}.
\end{array}
\tag{BQ30}
$$

Only the last item can become a mass gap. The vertical annihilation rate belongs between the first two rows and vanishes on the retained charge; it is not the last row. If \(X_{\mathrm{phys}}\) is the quotient carrier and \(\mathfrak d\) its independently constructed dimensionless form, the required next statement is a coercive estimate

$$
\mathfrak d[\xi]
\geq
\kappa\|\xi\|^2,
\qquad
\xi\in X_{\mathrm{phys}}\ominus\mathbb C\Omega,
\qquad
\kappa>0,
\tag{BQ31}
$$

followed by the same-carrier Casimir solder developed in [[joint-causal-generators-and-the-mass-casimir]]. A quotient class, topological sector, conserved charge, or noninvertible terminal map does not imply (BQ31). Conversely, (BQ31) without the quotient construction does not explain what physical distinctions the operator acts on.

The Yang--Mills analogue to seek is therefore not “a gluon acquires a mass.” It is:

$$
\boxed{
\text{reversible/gauge presentation directions}
\longrightarrow
\text{physical quotient residue}
\longrightarrow
\text{uniform distinction form}
\longrightarrow
\text{Poincaré-Casimir floor}.}
\tag{BQ32}
$$

The baryon model proves that this category of quotient construction exists in familiar physics and that a late acoustic observable can sit downstream of an unsigned magnitude coordinate of its survivor. It does not make BAO evidence for the quotient history; nor does it prove that gauge descent has the same kernel, that its residue is baryon number, or that the causal grain constructs either one.

## Promotion and kill conditions

The baryon-acoustic route is promoted only if:

- a pre-clock wall class independently selects the material quotient, predicts the magnitude seen by the acoustic branch, and assigns any directed sign to an independently sign-sensitive observable;
- the same construction supplies or predicts the QCD mass-per-charge solder without reading measured masses backward;
- a reaction network and perturbation transfer propagate a predeclared signature into CMB/BAO observables;
- that signature survives nuisance projection with nonzero stable rank; and
- the grain's metric and material descendants satisfy a common-signature intertwining test rather than a numerical resemblance.

It is killed as an explanation of the \(46.27\,\mathrm{MeV}\) number if:

- \(E_g\) is simply set equal to \(k_BT\) after inspecting the hadronic history;
- an arbitrary “onset” percentage in \(m_B(T)\) is chosen to hit the number;
- pair exposure is called mass generation;
- net baryon number is treated as exact through an epoch where its violation is essential; or
- BAO is claimed to preserve the full annihilation history rather than one highly compressed material consequence.

[[receipts/baryon_asymmetry_exposure_receipt.py|The companion receipt]] checks (BQ18)--(BQ22) in the declared ideal-nucleon model. It certifies the algebra and displayed arithmetic, not the full hadronic history, a causal-grain date, or a Yang--Mills gap.
