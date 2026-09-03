# The Causal Patch, the Boundary, and the Two Times

Locality may be a red herring as an *explanatory primitive* without being dispensable as an observable correspondence rule. A finite causal patch does not by itself remove ultraviolet singularities or make its observable algebra finite, but it changes the constitutive question: instead of deriving the global physical carrier from a local field equation, construct an accessible patch by a boundary or restriction map, construct causal directedness through one-sided fact-and-record growth, and recover reversible clock evolution only inside the resulting physical representation. A dimensionless gap of the causal operator becomes a Yang--Mills mass gap only after a noncircular carrier comparison, an energy solder, an independent yardstick, and continuum-stable recovery of local QFT.

**Status: [EXACT TYPE DISTINCTIONS; EXACT SYMMETRIC-SEMIGROUP AND COMPARISON THEOREM; INTERPRETIVE REVERSAL; OPEN PRE-QFT AND YANG--MILLS CONSTRUCTION].** Nothing below proves that causal formation occurs by the proposed operator. It identifies what that operator would have to operate on, which notions of boundary and time it may join, and the precise additional theorem needed before its dimensionless coercivity has the meaning of mass.

## The qualified locality reversal

Five claims are often hidden inside the word *locality*:

1. **Primitive point locality:** manifold points and fields at points are ontologically prior.
2. **Local dynamical presentation:** the action, equations, or interaction density is assembled from fields and finitely many derivatives at a spacetime point.
3. **Observable microcausality:** gauge-invariant observables assigned to spacelike separated regions commute; a separately declared charged-field algebra may instead carry graded locality.
4. **Regional independence:** suitably separated observable algebras satisfy a split, tensor-product, or other declared independence property.
5. **Finite propagation:** disturbances obey a causal support or influence bound.

The present reversal directly challenges the first claim and leaves open whether the second is fundamental. It cannot simply discard the last three. They are mutually distinct recovery obligations. On an already specified commuting inclusion, a split or tensor-product property is stronger than commutation; in general, Einstein locality and statistical independence should not be treated as one predicate, and neither alone proves a finite-propagation theorem. Any theory compatible with observed relativistic QFT must recover isotony, microcausality, covariance, and the correct gauge-invariant observables. The Minkowski/Poincare target additionally requires a positive-energy representation; curved-spacetime recovery instead uses local covariance and Hadamard or microlocal-spectrum admissibility. [[compatible-with-existing-physics/relations-among-theories|Relations among theories]] therefore permits local QFT to remain the grammar of each observable fiber even if the global gluing law is more primitive.

The useful claim is consequently:

> Locality is a red herring when it is asked to *constitute the physical carrier from within one local presentation*. It is not a red herring when it states the tested relations among already constituted observables.

This is why the mass gap should not be sought only as a local mass term. The gap belongs to the global spectrum of the physical vacuum representation. A local Yang--Mills Lagrangian constrains that representation, but the existence, vacuum selection, gauge reduction, and coercivity of the whole carrier are additional problems.

## A finite causal patch is not a finite theory

Several inequivalent finiteness claims must be kept apart.

| Claim | What is bounded | What does not follow |
|---|---|---|
| causally bounded patch | the region accessible between declared causal cuts | finitely many field modes or finite-dimensional Hilbert space |
| compact spatial section | geometric volume at one clock time | ultraviolet regularity at coincident points |
| finite lattice regulator | number of cells and link variables at fixed cutoff | existence of a continuum theory |
| finite entropy of a chosen state | one state-dependent entropy functional | finite-dimensional carrier or finite regional capacity |
| finite-index inclusion | relative size of one algebra inclusion | a state entropy or a bound on field modes |
| nuclearity bound | an energy- or temperature-dependent phase-space map | finite-dimensional local algebra |
| finite-dimensional algebra | number of independent matrix degrees of freedom | relativistic local QFT in the continuum |

Continuum QFT can assign a type-III von Neumann algebra to a bounded region. Such an algebra has neither a finite-dimensional density-matrix factorization nor a normal finite trace merely because the region is finite. [[library/the-role-of-type-iii-factors-in-quantum-field-theory/inq|The type-III review]] emphasizes that the net of inclusions, rather than a tensor product of finite regional systems, carries the local structure.

The main infinities also live at different ends:

- ultraviolet singularities arise when fields or distributions are multiplied at coincident or arbitrarily short-separated points;
- infrared and thermodynamic questions concern large distance, zero modes, or the infinite-volume limit;
- horizon questions concern causal accessibility, redshift, modular structure, edge data, or entanglement across a cut.

A finite geometric or accessibility radius supplies a candidate infrared scale without regulating the first class. An actual box spectrum or finite-size gap additionally requires dynamics, boundary conditions, and the relevant compactness or spectral theorem; null boundaries, redshift, and zero modes can defeat the naive box analogy. Event horizons can introduce genuine boundary and state questions, but they are not the generic source of ultraviolet renormalization. [[library/local-wick-polynomials-and-time-ordered-products/inq|Local Wick products]] make the short-distance problem explicit: renormalized time-ordered products are controlled by their scaling near the total diagonal. Effective field theory is likewise not merely a repair for a mistaken infinity; it is a controlled statement about which operators and scales affect a specified observational regime.

This correction strengthens the boundary programme. It says that *causal finiteness*, *UV regulation*, and *informational capacity* must be three separately constructed inputs or outputs rather than three names for one intuition.

## What “everything is connected” can mean

Inside one causal patch, “everything is connected with everything” has at least five mathematical readings:

| Reading | Candidate structure | Does it permit signalling? |
|---|---|---|
| common state | joint correlations or entanglement | no, not by itself |
| global constraint | Gauss law, gauge reduction, or a fixed total charge | no, not by itself |
| common boundary law | amplitudes sewn through shared boundary data | no, not by itself |
| algebraic accessibility | one observable algebra generated from overlapping subalgebras | not without a dynamical influence map |
| causal influence | an intervention here changes outcome statistics there | yes; this is the notion constrained by relativistic causality |

The first four can be global while observables at spacelike separation still commute. Reeh--Schlieder correlations are therefore not superluminal causal influence, and Gauss-law nonfactorization is not a signal channel. A global or nonlocal ontology can remain empirically local only after it proves this distinction in the recovered observable sector.

## The structural boundary

The boundary need not first be the geometric edge of a light cone. Begin with a pre-observable algebra or carrier \(\mathcal M\), an accessible algebra \(\mathcal A\), and an inclusion

$$
i:\mathcal A\hookrightarrow\mathcal M.
$$

The canonical contravariant operation is restriction of states,

$$
i^*:S(\mathcal M)\longrightarrow S(\mathcal A),
\qquad
i^*(\omega)=\omega|_{\mathcal A}.
$$

It can be many-to-one. A conditional expectation is additional structure,

$$
E:\mathcal M\longrightarrow\mathcal A,
\qquad
E^2=E,
\qquad
\omega\circ E=\omega,
$$

where the last equality names the faithful normal state used by the GNS construction below. The expectation is usually required to be normal, unital, completely positive, and \(\mathcal A\)-bimodular. Not every inclusion admits an expectation preserving the declared \(\omega\). Moreover, a faithful conditional expectation can still be non-injective as a linear map: *faithful on positive elements* is not the same predicate as *one-to-one on the whole vector space*. The wall's operationally erased directions are therefore best represented by the kernel pair

$$
x\sim_E y
\quad\Longleftrightarrow\quad
E(x)=E(y),
$$

or by \(\ker E\) when the additive structure is the intended one. They are “nothing for this readout,” not metaphysical nonbeing. [[algebra/inbox/radical-copernicanism/commentary-part-2/varieties-of-nothing|The varieties of nothing]] prevents this kernel, an empty set, a vacuum, a gauge orbit, and an unpointed torsor from being identified.

The wall still does not make a fact. For a discrete outcome set, an instrument is a separately supplied family of normal completely positive maps satisfying

$$
\{\mathcal I_y\}_{y\in Y},
\qquad
\sum_{y\in Y}\mathcal I_y(\mathbf1)=\mathbf1.
$$

It determines

$$
p_y=\omega(\mathcal I_y(\mathbf1)),
\qquad
\omega_y(A)
=
\frac{\omega(\mathcal I_y(A))}{p_y}
\quad(p_y>0).
$$

The family, probabilities, and posterior states do not select the obtained value. Factivity additionally requires a character or value in a declared commutative readout algebra, an actuality rule, and a dynamically stable record. Restriction or expectation and the instrument are separate inputs; the structural chain is

$$
\boxed{
\bigl(i^*\omega\text{ or a declared coarse state},\{\mathcal I_y\}\bigr)
\longrightarrow
\bigl((p_y,\omega_y)\bigr)_{y\in Y}
\longrightarrow
\overset{\mathrm{actuality}}{y_*}
\longrightarrow
\overset{\mathrm{stabilization}}{\text{persistent record}}.}
$$

Each arrow has a different domain and codomain. None should be renamed “collapse” without specifying which arrow is intended.

## One patch is not enough

Locality is a relation among overlapping and spacelike-incomparable regions, so a fundamental patch theory requires an atlas or site rather than one privileged box. A minimal regulated signature is

$$
\mathfrak P_\epsilon
=
\bigl(
\mathsf P,\leq,\perp,\operatorname{Cov},\partial;
\mathcal A_\epsilon,\omega,\iota;
\mathcal K^\partial_\epsilon,Z,\operatorname{Sew},\Lambda
\bigr),
$$

where \(\mathsf P\) is a family of patches, \(\operatorname{Cov}(D)\) declares covers or a Grothendieck topology, and \(\perp\) is a spacelike relation. The accessible-algebra functor supplies injective maps

$$
\iota_{DE}:\mathcal A_\epsilon(D)\hookrightarrow\mathcal A_\epsilon(E),
\qquad
\iota_{EF}\iota_{DE}=\iota_{DF}
\quad(D\leq E\leq F).
$$

Overlap and cover data still require a descent or gluing theorem. Compatible patch states obey

$$
\omega_E\circ\iota_{DE}=\omega_D.
$$

This compatibility is necessary but is not itself a state-gluing theorem. At the finite regulator, let \(\mathcal K^\partial_\epsilon(\partial D)\) be a declared boundary Hilbert carrier, let \(Z_D\in\mathcal K^\partial_\epsilon(\partial D)\) be an amplitude vector, and type sewing along an oppositely oriented common boundary \(\Sigma\) by

$$
\operatorname{Sew}_\Sigma(Z_-,Z_+)
:=
\langle Z_-,Z_+\rangle_{\mathcal K^\partial_\epsilon(\Sigma)}.
$$

The response \(\Lambda_D\) is a separate operator or form on boundary variations when it exists. More singular continuum amplitudes require a replacement pairing and domain theorem rather than silently changing the type of \(Z_D\).

Observable locality must be stated after embedding both algebras into a common carrier. For \(D_1,D_2\leq F\), require

$$
D_1\perp D_2
\quad\Longrightarrow\quad
[\iota_{D_1F}(A_1),\iota_{D_2F}(A_2)]=0
\quad
(A_i\in\mathcal A(D_i))
$$

after regulator removal, or a regulated influence estimate strong enough to yield it. A totally ordered chain of horizons may encode one-sided succession, but it contains no spacelike-incomparable pair and cannot by itself reconstruct \(3+1\)-dimensional localization.

The boundary symbol \(\partial D\) must also be typed. It may denote a geometric cut, a boundary-condition carrier, an edge-mode algebra, the interface of an inclusion, or the domain of a Dirichlet-to-Neumann response. These are not interchangeable. Integrating out a local bulk can produce a nonlocal boundary response such as \(\sqrt{-\Delta+m^2}\), so boundary nonlocality neither refutes bulk locality nor uniquely reconstructs a bulk.

For a patch-relative construction, the boundary of a finite causal diamond with declared endpoints,

$$
\partial\!\left(J^+(p)\cap J^-(q)\right),
$$

is a cleaner primitive candidate than a black-hole event horizon \(\partial J^-(\mathscr I^+)\) or an observer horizon \(\partial J^-(\gamma^+)\), both of which can depend on an entire future. The eventual theory may recover such horizons, but it should not silently use global spacetime information while claiming to construct locality from finite-patch data.

## Causal order and clock time are different types

There are two main temporal roles and at least two auxiliary parameters.

| Structure | Exact carrier | Parameter | Reversibility | What it measures |
|---|---|---|---|---|
| factive or ontological order | persistent record algebras and obtained characters | a preorder or poset, not necessarily a number | one-sided by inclusion | which facts are settled before which later records |
| carrier formation | a CP semigroup on an ambient or pre-observable carrier with an accessible stable range | \(\sigma\geq0\) | generally no CP inverse | approach to, or stabilization of, an accessible carrier |
| accessible relaxation | a CP or endomorphism semigroup on the formed accessible algebra and its GNS carrier | \(s\geq0\) | generally no CP inverse | loss or mixing among accessible state directions |
| Euclidean preparation | a transfer operator on a boundary-slice carrier or an OS contraction semigroup | \(\tau_E\geq0\) | not a physical inverse-time group | composition of slabs and vacuum preparation |
| Lorentzian clock evolution | automorphisms of the physical observable algebra | \(t\in\mathbb R\) | two-sided | reversible dynamical comparison measured by a clock |
| modular flow | one algebra and one faithful state or weight | \(u\in\mathbb R\) | two-sided; trivial for a trace | state-relative automorphic flow; physical clock meaning needs a Bisognano--Wichmann, KMS/thermal-time, or comparable identification |

A minimal factual history is a directed system

$$
\iota_{\mathsf r,\mathsf r'}:
\mathcal R_{\mathsf r}\hookrightarrow\mathcal R_{\mathsf r'},
\qquad
\mathsf r\preceq\mathsf r',
$$

with obtained characters satisfying record persistence,

$$
\boxed{
\chi_{\mathsf r'}\circ
\iota_{\mathsf r,\mathsf r'}
=
\chi_{\mathsf r}.}
$$

This is a precise arrow of fact. It supplies neither elapsed duration nor an energy operator. [[cosmodynamics/fact-record-history|Fact, Record, and History]] owns the further stability and observer-compatibility obligations.

A one-sided algebraic process may be represented by normal unital completely positive maps

$$
\Phi_s:\mathcal A\longrightarrow\mathcal A,
\qquad
\Phi_{s+t}=\Phi_s\Phi_t,
\qquad
s,t\geq0.
$$

If it does not extend to a group of \(*\)-automorphisms on the accessible algebra, its parameter is mathematically one-sided. An operational arrow requires a declared process interpretation; an ontological arrow additionally requires soldering to obtained values and persistent records. [[sufficient-reason/algebraic-arrow-of-time|The algebraic arrow]] states this missing bridge.

By contrast, once a physical Hilbert representation and clock have been constructed,

$$
\alpha_t(A)=U(t)^*AU(t),
\qquad
U(t)=e^{-itH/\hbar},
\qquad
t\in\mathbb R,
$$

is a reversible automorphism group. Energy is the generator dual to this clock parameter. It is not what is “spent” merely because a fact becomes settled.

After OS reconstruction—or after a regulated transfer generator has independently been identified with the physical Hamiltonian—let \(E_0:=\inf\sigma(H)\), assume the ground-energy eigenspace exists in the stated setup, and write \(H_0:=H-E_0I\geq0\) for the vacuum-normalized Hamiltonian. Euclidean depth is represented by

$$
T_{\tau_E}=e^{-\tau_EH_0/\hbar}.
$$

That phrase hides an exact descent gate. Start with a reflection \(\theta\), a positive-time algebra \(\mathcal A_+\), a reflection-positive functional \(\omega\), and a distinguished family of Euclidean translations \(\tau_s\). Quotient \(\mathcal A_+\) by the null space of

$$
\langle[F],[G]\rangle_{\mathrm{OS}}
:=
\omega\!\left(\theta(F)^*G\right).
$$

The positive translations must preserve this null space and descend to a strongly continuous self-adjoint contraction semigroup on the completed OS carrier. Only then does the spectral theorem give

$$
T(s)=e^{-sH_0/\hbar},
\qquad H_0\geq0.
$$

Euclidean covariance, the OS regularity and growth conditions, locality or symmetry of the Euclidean fields, and analytic continuation are further requirements for identifying the unshifted \(H=H_0+E_0I\) with the clock Hamiltonian of a positive-energy Poincare theory. Reflection positivity alone does not turn an arbitrary Markov, modular, RG, or record-order semigroup into time translation.

[[library/the-semigroup-characterization-of-osterwalder-schrader-path-spaces/inq|Klein's semigroup characterization]] isolates this quotient-semigroup step, while [[library/from-euclidean-field-theory-to-quantum-field-theory/inq|Schlingemann's algebraic reconstruction]] begins with Euclidean local data and an additional time-zero condition in order to recover a Haag--Kastler net.

[[past-future-angle-and-the-transfer-gap]] gives a sharp geometric realization when the OS path space is also stationary, reversible, Markov, and Hilbert-positive. Conditional expectations onto disjoint past and future half-spaces at Euclidean separation \(\ell>0\) have Friedrichs cosine

$$
c_F(\ell)
=
\left\|e^{-\ell H_0/(\hbar c)}(1-P_0)\right\|,
\qquad
P_0=E_{H_0}(\{0\}).
$$

The positive return \(qpq\) lives on the history carrier. If \(J_+^0\) is the centered endpoint isometry, then the exact carrier identification is

$$
(J_+^0)^*(qpq)J_+^0
=
e^{-2\ell H_0/(\hbar c)}(1-P_0).
$$

Thus its supported logarithm per slab thickness recovers \(H_0\) after endpoint identification. The positive separation is load bearing: touching halves share the entire time-zero algebra, and subtracting their common range removes the transfer datum. Nor may the step size be hidden. For adjacent lattice cuts \(1-c_F(a)\to0\) at finite physical gap; a fixed-thickness contraction or \(-(\hbar c/a)\log c_F(a)\) is the continuum-stable statement.

It composes and prepares the ground-state space but is not a Lorentzian clock and does not select an outcome. For self-adjoint \(H_0\geq0\), finite-depth \(T_{\tau_E}\) is injective even though its inverse is generally unbounded, and the spectral theorem gives

$$
e^{-\tau_EH_0/\hbar}
\xrightarrow[\tau_E\to\infty]{\mathrm{strong}}
P_{\ker H_0}.
$$

No positive gap is needed for this strong limit. It equals \(P_\Omega\) only when the ground-state space is one-dimensional. [[vacuum-boundary-gluing-and-wall-response|Vacuum boundary gluing]] proves the abstract finite-regulator version.

The integrated transfer gives a second exact distinction. On the vacuum complement,

$$
\mathcal D_{\mathrm E}
:=
\int_0^\infty e^{-2\ell H_0/(\hbar c)}(1-P_0)\,\mathrm d\ell
=
\frac{\hbar c}{2}H_0^{-1}
$$

as an extended positive form on the vacuum complement, with \(H_0^{-1}\) understood there. [[phase-modulus-pointing-and-euclidean-dwell]] proves that \(H_0\geq\Delta I\) on that complement exactly when \(\mathcal D_{\mathrm E}\leq\hbar c/(2\Delta)I\). This is a uniform Euclidean persistence ceiling, not a minimum interval between facts. Factive record order still has no metric duration until a clock solder is supplied.

There is also a useful bounded-generator firewall. On any Banach space, if \(\mathcal L\) is bounded, then

$$
e^{s\mathcal L}
$$

is linearly invertible for every finite \(s\), with inverse \(e^{-s\mathcal L}\). The inverse may fail to be positive or completely positive, so the process can be operationally irreversible, but finite-time vector-space information has not literally vanished. Exact many-to-one forgetting requires noninjectivity at the declared time, a noninjective restriction, expectation, readout, or instrument, or a limiting projection. Infinite-dimensional non-surjectivity alone means failure of a global inverse, not loss of input information. This is why “irreversible operator” must name the sense of irreversibility.

## A dimensionless causal generator

The cleanest spectral construction begins with a von Neumann algebra \(\mathcal A_C\), a faithful normal state \(\omega_C\), and a semigroup \(\Phi_s\) of normal unital completely positive maps satisfying

$$
\omega_C\circ\Phi_s=\omega_C.
$$

On the GNS carrier \((\pi_C,\mathcal H_C,\Omega_C)\), define

$$
S_s\pi_C(A)\Omega_C
:=
\pi_C(\Phi_s(A))\Omega_C.
$$

Kadison--Schwarz and state invariance give

$$
\|S_s\pi_C(A)\Omega_C\|^2
\leq
\omega_C(\Phi_s(A^*A))
=
\omega_C(A^*A),
$$

so \(S_s\) is a contraction. Assume in addition that \(s\mapsto S_s\) is strongly continuous. Pointwise ultraweak continuity of the algebra maps is not being used as a silent substitute for this GNS continuity hypothesis. If \(\Phi_s\) is GNS-symmetric, \(S_s\) is then a strongly continuous self-adjoint contraction semigroup and therefore

$$
S_s=e^{-sK_C}
$$

for a positive self-adjoint generator \(K_C\). Unitality gives \(S_s\Omega_C=\Omega_C\). When \(s\) is dimensionless, so is \(K_C\). Its closed dissipation form is

$$
\operatorname{Dom}\mathfrak d_C
=
\operatorname{Dom}K_C^{1/2},
\qquad
\mathfrak d_C[\xi]
:=
\|K_C^{1/2}\xi\|^2.
$$

Assume the fixed space is exactly \(\mathbb C\Omega_C\) and separately require the strictly positive lower edge

$$
\kappa_C
:=
\inf\sigma\!\left(
K_C\!\restriction_{\Omega_C^\perp}
\right)
>0.
$$

Equivalently,

$$
\boxed{
\mathfrak d_C[\xi]
\geq
\kappa_C\|(1-P_C)\xi\|^2,
\qquad
P_C=|\Omega_C\rangle\langle\Omega_C|.}
\tag{C}
$$

for every \(\xi\in\operatorname{Dom}K_C^{1/2}\). Triviality of the fixed space is only ergodicity; it does not by itself imply \(\kappa_C>0\). This operator acts on centered GNS directions of a declared accessible state. It does not act on bare spacetime, propositions, or facts. Equation (C) says that no normalized nonstationary direction relaxes arbitrarily slowly under the declared causal process. It is a dimensionless Poincare inequality, not yet an energy gap, mass, outcome gap, or proof of record formation.

For a nonsymmetric CP semigroup, the real dissipative part

$$
-\operatorname{Re}\langle\xi,\mathcal L_C\xi\rangle
$$

can control relaxation, but it does not automatically define a self-adjoint observable. Sectorial closability, invariant-space control, and a comparison to the physical symmetric energy form must then be proved separately. The symmetric case is the exact theorem target, not an assertion that ontology itself is reversible.

## The range--kernel obstruction

One irreversible operator cannot be assigned every desired role. Suppose \(E\) is a normal conditional expectation preserving the same faithful normal state \(\omega\) used for the GNS construction:

$$
E:\mathcal M\longrightarrow\mathcal A,
\qquad
\omega\circ E=\omega.
$$

It forms the accessible algebra, and its GNS implementation is

$$
e\,\pi_\omega(x)\Omega_\omega
:=
\pi_\omega(Ex)\Omega_\omega.
$$

Bimodularity and state preservation make \(e\) the orthogonal projection onto

$$
\mathcal K_{\mathrm{obs}}
:=
\overline{\pi_\omega(\mathcal A)\Omega_\omega}.
$$

Then, exactly,

$$
(1-e)\xi=0
\qquad
\text{for every }\xi\in\mathcal K_{\mathrm{obs}}.
$$

Therefore the raw forgetting form

$$
\mathfrak d_{\mathrm{forget}}[\xi]
:=
\|(1-e)\xi\|^2
$$

vanishes on the entire formed physical carrier. It cannot distinguish its vacuum from any of its excitations and hence cannot be its mass-gap form.

The same obstruction holds for a formation semigroup. If \(S_s=e^{-sK_{\mathrm{form}}}\) approaches the projection onto a nontrivial stable carrier and

$$
\mathcal K_{\mathrm{obs}}
\subseteq
\ker K_{\mathrm{form}},
$$

then every comparison map with

$$
\operatorname{Ran}J\subseteq\mathcal K_{\mathrm{obs}}
$$

obeys

$$
\mathfrak d_{\mathrm{form}}[J\Psi]=0.
$$

A positive transverse relaxation gap controls approach *to* the formed carrier; it says nothing about the energy spectrum *within* that carrier. Conversely, if \(\ker K_C=\mathbb C\Omega_C\) as assumed in (C), then the semigroup relaxes every observable excitation and is not, by itself, a projection onto a rich clock-bearing observable algebra.

This forces a three-operator architecture:

$$
\boxed{
\text{formation }E\text{ or }K_{\mathrm{form}}
\longrightarrow
\text{tangential response }\Lambda_\partial\text{ or }\mathscr D_\parallel
\longrightarrow
\text{clock generator }H.}
$$

The first operator identifies or prepares the accessible carrier. The second operates on variations *of retained boundary data* and measures the cost of compatible extension or distinction. The third generates physical clock translations. In a finite type-I debugging decomposition one may visualize

$$
\mathcal K_{\mathrm{pre}}
=
\mathcal K_{\mathrm{obs}}\oplus\mathcal K_{\mathrm{lost}},
\qquad
K_{\mathrm{form}}
=
\begin{pmatrix}
0&0\\
0&K_\perp
\end{pmatrix},
$$

while the relevant boundary form is

$$
\Lambda_\partial\geq0
\quad\text{self-adjoint},
\qquad
\mathfrak d_\partial[f]
=
\|\Lambda_\partial^{1/2}f\|^2,
\qquad
f\in\operatorname{Dom}\Lambda_\partial^{1/2}
\subseteq\mathcal K_{\mathrm{obs}}.
$$

The exact Gaussian Dirichlet-to-Neumann calculation realizes this distinction: fiber integration prepares a boundary amplitude, while \(\Lambda_\partial=\sqrt{-\Delta+m^2}\) acts tangentially on its boundary values. This \(\Lambda_\partial\) has inverse-length or frequency units; a dimensionless causal generator would instead use an independently normalized \(\widehat\Lambda_\partial=\ell_*\Lambda_\partial\), with the compensating energy coefficient carried by \(E_*\). The mass gap comes only after that response form is soldered to the Hamiltonian form. The wall projection itself has no such content.

## The causal-response-to-Hamiltonian-gap theorem

Let \((\mathcal H_{\mathrm{YM}},\Omega,H)\) be a physical vacuum representation, with \(H\geq0\), \(H\Omega=0\), and closed energy form

$$
h[\Psi]=\|H^{1/2}\Psi\|^2.
$$

Let \((\mathcal H_C,\Omega_C,K_C)\) satisfy (C). Suppose there is a bounded complex-linear comparison map

$$
J:\mathcal H_{\mathrm{YM}}\longrightarrow\mathcal H_C,
\qquad
J(\operatorname{Dom}h)
\subseteq
\operatorname{Dom}K_C^{1/2},
$$

that respects vacuum and centering,

$$
J\Omega=\Omega_C,
\qquad
J\bigl(\operatorname{Dom}h\cap
(\mathcal H_{\mathrm{YM}}\ominus\mathbb C\Omega)\bigr)
\subseteq
\mathcal H_C\ominus\mathbb C\Omega_C.
\tag{J0}
$$

Assume that for every centered \(\Psi\in\operatorname{Dom}h\), the map has a lower norm bound

$$
\|J\Psi\|_C^2
\geq
b_J\|\Psi\|_{\mathrm{YM}}^2,
\qquad b_J>0,
\tag{J1}
$$

and, for every \(\Psi\in\operatorname{Dom}h\), the physical energy form dominates the transported causal form,

$$
\boxed{
h[\Psi]
\geq
\eta_{\mathrm{sol}}E_*\mathfrak d_C[J\Psi],}
\qquad
\eta_{\mathrm{sol}}>0,\quad E_*>0.
\tag{J2}
$$

Here \(\eta_{\mathrm{sol}}\) and \(b_J\) are dimensionless, while \(E_*\) has units of energy and is fixed independently of the desired gap.

**Comparison theorem.** Under (C), (J0), (J1), and (J2),

$$
\boxed{
H
\geq
\eta_{\mathrm{sol}}E_*\,\kappa_C b_J
\,(1-P_\Omega)}
\tag{M}
$$

in quadratic-form sense. Therefore

$$
\boxed{
\Delta_E
\geq
\eta_{\mathrm{sol}}\kappa_C b_J E_*>0.}
$$

**Proof.** For arbitrary \(\Psi\in\operatorname{Dom}h\), put \(\Psi_0=(1-P_\Omega)\Psi\). Since \(H\Omega=0\),

$$
h[\Psi]=h[\Psi_0].
$$

Complex linearity, (J0), and \(K_C\Omega_C=0\) likewise give

$$
\mathfrak d_C[J\Psi]
=
\mathfrak d_C[J\Psi_0].
$$

Apply (J2) to the centered vector \(\Psi_0\), then (C), then (J1):

$$
h[\Psi]
=h[\Psi_0]
\geq
\eta_{\mathrm{sol}}E_*\mathfrak d_C[J\Psi_0]
\geq
\eta_{\mathrm{sol}}E_*\kappa_C\|J\Psi_0\|_C^2
\geq
\eta_{\mathrm{sol}}E_*\kappa_Cb_J
\|(1-P_\Omega)\Psi\|^2.
$$

The representation theorem for closed forms gives (M). \(\square\)

The conclusion at this stage is a positive **Hamiltonian** gap in the declared physical vacuum representation. It is a Yang--Mills mass-gap theorem only after that representation has independently been identified as the continuum, Poincare-covariant, gauge-invariant pure Yang--Mills theory required by the problem. Lorentz invariance of the joint translation spectrum together with the positive-energy spectrum condition then turns the isolated vacuum energy threshold into the corresponding positive invariant-mass threshold.

This theorem exposes four independent obligations:

1. \(\kappa_C\): the causal process uniformly distinguishes every nonstationary direction;
2. \(b_J\): the carrier map does not make a physical direction invisible;
3. \(\eta_{\mathrm{sol}}\): causal dissipation is genuinely controlled by physical energy on the compared carrier;
4. \(E_*\): a separately calibrated energy unit converts dimensionless response into a spectrum.

If \(J\) is defined using the spectral projections of \(H\), if \(E_*\) is fitted to the desired mass, or if (J2) is merely the mass-gap inequality rewritten, the construction is circular. A physically meaningful \(J\) must arise from declared state-compatible GNS, gauge-descent, boundary, or reconstruction maps and must respect the required covariance, locality, and regulator limits; an arbitrary Hilbert-space embedding can hide the answer. If \(J\) reaches only a topological or knot sector, the theorem controls only that sector. If \(b_J\to0\), \(\kappa_C\to0\), or the calibrated product vanishes during volume or regulator removal, no continuum gap follows.

There is also a normalization firewall. Reparameterizing the causal semigroup rescales \(K_C\) and \(\kappa_C\), while rescaling \(J\) or its carrier norm moves factors between \(b_J\) and \(\eta_{\mathrm{sol}}\). Before a canonical parameter, GNS norm, comparison map, and yardstick have been fixed, the individual constants have no invariant physical meaning. Only the calibrated product

$$
\eta_{\mathrm{sol}}\kappa_Cb_JE_*
$$

appearing in the same-carrier energy inequality can survive those presentation changes.

This is the semigroup version of [[causal-frame-coercivity|causal-frame coercivity]]. The frame theorem allows a whole family of wall tests on the physical carrier; the present theorem makes explicit how a separately constructed causal relaxation carrier would have to be transported into the Yang--Mills energy form.

By the range--kernel obstruction, \(K_C\) in this theorem cannot be merely the transverse generator that projects onto the observable carrier when \(J\) lands inside that carrier. It must be a distinction or response generator that remains nonzero on centered accessible directions—for example, a boundary Dirichlet-to-Neumann form, an inherited coordinate carré du champ, or a canonically normalized family of overlapping wall responses.

## Where mass, energy, space, and scale enter

The theorem deliberately does not equate units with concepts.

| Concept | Mathematical role in this construction | Dimensional statement |
|---|---|---|
| Lorentzian causal order | chronological or causal precedence among reconstructed events | no unit required |
| factive order | precedence of persistent record extensions | no unit required |
| clock time | parameter of a physical automorphism group | seconds after clock calibration |
| energy | self-adjoint generator dual to clock translations | action per clock time |
| space | reconstructed localization, incidence, or intrinsic form geometry among observable registers | length only after a metric scale is supplied |
| scale | comparison of distinguishability or metric normalization between carriers | dimensionless ratio before a yardstick |
| mass | invariant spectral threshold in a Poincare-covariant physical representation satisfying the spectrum condition | \(\Delta_E/c^2\) |

[[mass-as-casimir-and-realization]] refines the final row: the translation generators \(P_\mu\) vary within irreducible Poincare representations, while \(P^2/c^2\) is one invariant label of their type. Its common realization ledger also separates measurement pointing and broken-vacuum selection from the independent coercivity statement that isolates the vacuum.

If a Poincare-covariant vacuum representation with Lorentz-invariant joint spectrum and the spectrum condition has been recovered, the rest-mass gap is

$$
m_{\mathrm{gap}}=\frac{\Delta_E}{c^2},
$$

and its associated Compton inverse length is

$$
\ell_C^{-1}=\frac{\Delta_E}{\hbar c}.
$$

Equality with an observed Euclidean correlation-decay rate requires a spectral representation and an interpolating observable with nonzero overlap with the lowest relevant sector; correlation lengths can otherwise be operator-dependent. These equations translate one physical spectral threshold into different unit conventions; they do not identify mass, energy, and length as concepts. Likewise, \(\hbar\) alone is an action unit, \(c\) is a spacetime conversion speed after Lorentzian structure exists, \(k_BT\) is an energy only after a temperature scale exists, and \(G\) does not by itself choose the Yang--Mills scale. A proposed yardstick such as

$$
E_*=\frac{\hbar c}{\ell_*}
\quad\text{or}\quad
E_*=k_BT_*
$$

is explanatory only if \(\ell_*\) or \(T_*\) is independently derived and the solder to the Yang--Mills carrier is proved.

There is one exact geometric result especially close to the proposed reversal. In spacetime dimension at least three, under the standard distinguishing and smoothness hypotheses, an order-preserving identification between already-given smooth spacetimes determines their Lorentzian metrics only up to conformal class:

$$
\boxed{
\text{causal order}
\longrightarrow
[g],
\qquad
\text{not }g.}
$$

A positive conformal scale section \(\sigma\in\Gamma(\mathcal E[1])\) then selects a representative from the conformal metric \(\mathbf g\in\Gamma(S^2T^*M\otimes\mathcal E[2])\):

$$
g_\sigma=\sigma^{-2}\mathbf g.
$$

Thus causal order can precede metric calibration in an exact rigidity theorem, but the theorem does not construct a manifold from an arbitrary ordered set and does not derive the missing scale section. [[library/the-class-of-continuous-timelike-curves-determines-the-topology-of-spacetime/inq|Malament's reconstruction result]] supplies the primary theorem, while [[conformal-scale-geometry/causal-order-and-metric-scale|Causal order and metric scale]] records its hypotheses and programme limitation. The finite value of \(c\) fixes the null-cone conversion only after spatial and clock units are compared; it does not choose \(\sigma\), a Yang--Mills vacuum, or a spectral gap.

Similarly, if a dimensionless record or scale grading \(N\) is constructed, a physical clock rate is extra:

$$
\varpi_*:=\left.\frac{\mathrm dN}{\mathrm d\tau}\right|_*,
\qquad
E_*=\hbar\varpi_*.
$$

The first equation is a clock solder, not a consequence of order. [[program-core/record-scale-soldering|Record--scale soldering]] states the compatibility conditions needed before \(N\) can orient a physical history.

The Copernican reversal is still available. A strongly local regular Dirichlet form can, under additional hypotheses, define an intrinsic metric; incidence and commutation data can define localization; and an algebraic net can reconstruct relational spatial organization. Thus one may construct the form before calling its intrinsic geometry “space.” But a nonlocal jump form reconstructs a different geometry, and a spectrum alone does not determine unique spatial ontology.

## The boundary-first gain

The boundary route has now removed one unnecessary assumption. [[vacuum-boundary-gluing-and-wall-response|Euclidean gluing]] constructs the time-zero vacuum measure by integrating bulk histories over fibers and sewing half-space amplitudes. Its logarithmic boundary weight can be nonlocal. More importantly, a bulk Poincare or logarithmic-Sobolev inequality for a product carré du champ passes exactly to a coordinate marginal equipped with the inherited coordinate form. Therefore the proof need not first manufacture a local boundary action or a quasilocal boundary Gibbs specification.

That is the precise sense in which boundary locality is a red herring for the current coercivity route:

$$
\text{bulk functional inequality}
\longrightarrow
\text{slice marginal inequality}
\longrightarrow
\text{energy-form comparison}
\longrightarrow
\text{gap}.
$$

The first arrow is marginalization, not wave-function collapse. The second is the open kinetic solder. The third is functional analysis. None selects a fact.

A truly prelocal version owes more. It must construct the patch category, the accessible algebras, and the gluing operation without presupposing a spacetime manifold, then recover the local covariant Yang--Mills net as an observable face. Until that reconstruction exists, Euclidean lattice gluing is a concrete model of the grammar, not a derivation from pregeometry.

## Exact invariance, decomposition, persistence, and charge balance

A one-sided semigroup is not automatically a Noether symmetry. Noether's theorem requires a differentiable variational symmetry or an appropriate covariant phase-space replacement; a noninvertible process need not carry the solution set onto itself. [[philosophy/noether-conservation/where-the-synthesis-fails|Where the synthesis fails]] therefore blocks the inference from “there is an irreversible operator” to “there is a conserved causal charge.”

Several exact balances remain available, but they have different types.

### Stationary state

Because \(\Phi_s\) is unital, its predual preserves the normalization of every normal state. If, separately,

$$
\omega_C\circ\Phi_s=\omega_C,
$$

then the reference state is invariant under the semigroup and its expectations are stationary. Neither statement is a scalar charge exchanged between being and nonbeing.

### Retained and erased distinction

For the finite tracial conditional-expectation theorem, let \(E_*\) be the state-side predual of the observable-algebra expectation and put \(\bar\rho=E_*(\rho)\). In a finite tracial representation, the trace pairing identifies \(E_*=E\). With tracial reference \(\tau\),

$$
\boxed{
D(\rho\Vert\tau)
=
D(\bar\rho\Vert\tau)
+
D(\rho\Vert\bar\rho).}
$$

At coincidence, the BKM response splits into retained and wall blocks. [[spectral-wall-descent/conditional-expectation-balance|Conditional-expectation balance]] proves the scoped identity. It is an accounting theorem for distinguishability relative to a declared subalgebra and reference, not conservation of information as a substance and not a temporal law.

### Persistent records

The compatibility equation

$$
\chi_t\circ\iota_{s,t}=\chi_s
$$

says that a later record retains an earlier obtained value. This is persistence through a one-sided history, not unitary transport of a complete prior state.

### Genuine charge and boundary flux

If independently constructed sectors carry Hamiltonian actions of the same continuous group \(G\), their moment maps land in one dual Lie algebra and add under the diagonal action. For an invariant Hamiltonian, the total moment-map component is conserved:

$$
\frac{\mathrm d}{\mathrm dt}Q_\xi^{\mathrm{tot}}=0.
$$

This is the exact finite-dimensional Hamiltonian statement. A bounded-region balance of the form

$$
\boxed{
Q_\xi[\Sigma_2]-Q_\xi[\Sigma_1]
+
\mathcal F_\xi[W]=0.}
$$

requires additional local-current or covariant-presymplectic data, an orientation, and a Stokes theorem identifying the wall flux \(\mathcal F_\xi[W]\). The common group, normalized infinitesimal generator, compatible carriers, and moment maps do not alone imply this regional flux formula. [[conservation-of-causal-charge/diagonal-charge-balance|Diagonal charge balance]] proves the general moment-map theorem and records why its causal and regional application remains conjectural.

### Compositional invariants

When a separately proved homotopy, correspondence, or index theorem applies, a \(K\)-theory, \(KK\), index, or correspondence-fusion class may persist while representatives change. For dualizable correspondences, categorical dimensions can multiply and their logarithms can add. These are structural invariants or valuations, not energy and not automatically Noether charges. [[conservation-of-causal-charge/unitarity-and-ontological-time|Why unitarity is not the wall symmetry]] treats compositional exactness as the strongest present upstream principle.

The honest answer to “what is conserved between being and nonbeing?” is therefore not yet one number. The current exact register is:

| Philosophical word | Defensible mathematical surrogate | Status |
|---|---|---|
| Being | invariant relational, index, or composition structure | several exact candidates; no unique physical selection |
| Nothing | indiscernibility class, erased response block, or absence of an obtained value | exact only relative to a declared readout |
| Becoming | one-sided record extension or nonautomorphic accessible action | exact structural criterion; physical instantiation open |
| conservation | moment-map/flux law for one continuous symmetry | exact theorem template; causal symmetry data missing |

This keeps the philosophical proposal live while refusing to turn four different equalities into one conservation law.

## The actual stopping condition

The causal-patch programme contributes to the Yang--Mills mass-gap problem only when it completes the following chain without importing the answer:

1. construct the prelocal or regulator-level carrier, patch operation, and accessible algebra;
2. construct the restriction, expectation, instrument, and fact/record arrows that are actually claimed, without calling them one descent;
3. construct a one-sided semigroup or record poset and prove why its orientation is physical rather than a chosen parameter convention;
4. derive a canonically normalized \(\kappa_C>0\) on the declared causal-response carrier, uniformly in volume and temporal depth;
5. construct \(J\) and prove that the combined comparison strength \(\kappa_Cb_J\) stays positive on every non-vacuum physical direction, without using the Yang--Mills spectrum;
6. prove the energy-form solder (J2) and independently fix \(E_*\);
7. pass the calibrated product through the continuum limit with generalized Mosco or an equally strong form convergence theorem and convergence of the complete vacuum projections;
8. reconstruct or identify the Poincare-covariant gauge-invariant Yang--Mills theory and its local observable correspondence; and
9. if a causal charge is claimed, separately construct its continuous action, normalized generator, moment map or covariant charge, and flux balance.

The programme fails if causal boundedness is used as a UV regulator without a short-distance theorem; if correlation is renamed influence; if Euclidean depth, modular flow, cosmic scale, record order, and clock time share a symbol without comparison maps; if a CP relaxation gap is simply renamed energy; or if empirical locality is abandoned rather than recovered.

## Claim ledger

| Status | Claim |
|---|---|
| Exact distinction | causal boundedness, UV regulation, finite algebra, and finite information capacity do not imply one another |
| Standard QFT correction | bounded local continuum regions can carry type-III algebras; UV renormalization concerns short-distance/coincident-point products rather than spatial infinity alone |
| Exact type distinction | state correlation, Gauss constraint, common gluing data, and causal influence are different relations |
| Exact operator algebra | state restriction is canonical to an inclusion; a state-preserving conditional expectation is extra structure; faithfulness on positives does not mean linear injectivity |
| Exact temporal distinction | record inclusions, CP-semigroup depth, Euclidean preparation, Lorentzian clock evolution, and modular flow are differently typed |
| Exact finite-dimensional no-go | \(e^{s\mathcal L}\) is linearly invertible at finite \(s\) for bounded \(\mathcal L\); lack of a CP inverse is not literal linear information erasure |
| Exact under stated hypotheses | an invariant GNS-symmetric CP semigroup induces a positive self-adjoint dimensionless generator and dissipation form |
| Exact range--kernel no-go | the defect of an expectation, or a formation generator vanishing on its stable range, gives the zero form on the formed observable carrier and cannot be its mass-gap operator |
| Exact conditional theorem | causal coercivity, carrier coverage, energy soldering, and an independent energy scale imply \(\Delta_E\geq\eta_{\mathrm{sol}}\kappa_Cb_JE_*\) |
| Exact scoped balances | unital normalization, stationary-state invariance, conditional-expectation relative-entropy decomposition, record persistence, and total moment-map conservation are different theorems; regional wall flux needs additional current and Stokes hypotheses |
| Interpretation | local QFT may be the observable fiber grammar of a more global boundary-first construction |
| Open | construct the causal carrier, wall, record process, uniform causal coercivity, comparison map, energy solder, and continuum Yang--Mills recovery |
