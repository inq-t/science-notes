# Causal-Frame Coercivity Beneath the Mass Gap

The proposed pre-QFT explanation of a mass gap is a three-factor theorem rather than a new particle-mass term: a canonically normalized family of physically constructed causal distinctions must detect every non-vacuum direction with a dimensionless lower frame bound; the member dynamics must dominate that distinction form by a dimensionless solder coefficient; and an independently fixed energy scale must calibrate the result. Their product is a certified lower bound on the gap. This makes causal completeness a dimensionless analytic obstruction rather than a pixel length; it becomes geometric only when the tests and normalization are geometrically constructed. The theorem states exactly what Type III algebras, Connes transport, entropy Hessians, fibers, knots, and a dimensional yardstick would each have to contribute.

**Status: [EXACT CONDITIONAL FRAME THEOREM; EXACT LOCAL-EXPECTATION NO-GO UNDER REEH--SCHLIEDER HYPOTHESES; OPEN YANG--MILLS CONSTRUCTION].** The functional-analytic implications are proved below. No causal wall family, energy solder, or continuum member satisfying all premises has yet been constructed for four-dimensional Yang--Mills.

## The category error, precisely stated

Five objects are commonly collapsed into one:

1. a gauge-dependent presentation field such as $A_\mu$;
2. the gauge-invariant observable algebra;
3. a state and its GNS representation;
4. the positive generator of physical time in that representation; and
5. the dimensional calibration that turns the generator's dimensionless spectral ratios into seconds, inverse metres, or joules.

The mathematical gap belongs to levels 2--4: an observable algebra in its vacuum representation and the generator of translations. Level 5 fixes its numerical value in physical units. It is not a coefficient at level 1. This is the valid category-error diagnosis behind the statement that “massless gluons acquire a mass”: a gauge-fixed propagator and the spectrum of the physical observable representation are differently typed objects.

The Clay problem itself is not a category error. It asks for a nontrivial continuum theory and a positive spectral interval above its vacuum for every compact simple gauge group. [[library/quantum-yang-mills-theory/inq|Jaffe and Witten]] explicitly formulate the gap as a property of the Hamiltonian and require the full axiomatic construction. A pre-QFT theory can explain why an admissible whole-state realization is coercive, but it does not evade the construction and continuum-limit clauses.

There is a deeper explanatory mismatch worth preserving. A local Lagrangian is asked to explain the selection of the global physical carrier, vacuum state, and energy form on which its own observables are represented. The proposed reversal is:

$$
\text{causal distinctions and their gluing}
\longrightarrow
\text{closed positive form}
\longrightarrow
\text{physical generator and emergent geometry},
$$

not

$$
\text{a pre-given spacetime and particle mass}
\longrightarrow
\text{a posteriori interpretation of the spectrum}.
$$

This is a carrier-first constitutive proposal. It is stronger than rephrasing the known gap and weaker than a completed Yang--Mills construction.

## What the operator operates on

Fix one regulated or continuum member only after its gauge and null directions have been removed. Let

$$
(\pi,\mathcal H,\Omega)
$$

be the physical GNS representation of a selected state, with $\|\Omega\|=1$. The centered physical carrier is

$$
\mathcal H_0:=\mathcal H\ominus\mathbb C\Omega,
\qquad
P_\Omega:=|\Omega\rangle\langle\Omega|.
$$

The operator does not act on spacetime, mass, or “information” in the abstract. Its input is a physical state-vector direction in $\mathcal H_0$, or an observable representative whose centered GNS vector lies there. Gauge representatives, BRST-exact vectors, and state-normalization directions must already have been quotiented out.

This means the theorem below is not yet a pre-QFT construction. A genuine underlying theory must supply a physical-realization functor, or at least a linear quotient-and-completion map

$$
Q_{\alpha,\omega}:\mathfrak C_\alpha
\longrightarrow\mathcal H_{\alpha,\omega},
$$

where $\mathfrak C_\alpha$ is a complex vector-space or algebraic carrier for member $\alpha$, $\omega$ supplies a positive GNS seminorm, and $Q_{\alpha,\omega}$ quotients its null space and completes the result. More explicitly, require linear maps

$$
\delta^{\mathrm{pre}}_{w,\alpha}:
\mathcal D^{\mathrm{pre}}_{w,\alpha}\subseteq\mathfrak C_\alpha
\longrightarrow\mathcal K^{\mathrm{pre}}_{w,\alpha},
\qquad
V_{w,\alpha,\omega}:\mathcal K^{\mathrm{pre}}_{w,\alpha}
\longrightarrow\mathcal K^{\mathrm{phys}}_{w,\alpha,\omega},
$$

with Hilbert response spaces and bounded $V_{w,\alpha,\omega}$. The composite $V_{w,\alpha,\omega}\delta^{\mathrm{pre}}_{w,\alpha}$ must annihilate $\ker Q_{\alpha,\omega}\cap\mathcal D^{\mathrm{pre}}_{w,\alpha}$ and be closable in the seminorm $\|Q_{\alpha,\omega}\xi\|$. It then factors uniquely through $Q_{\alpha,\omega}(\mathcal D^{\mathrm{pre}}_{w,\alpha})$ and extends to a closable physical map $\delta^{\mathrm{phys}}_{w,\alpha,\omega}$, with $Q_{\alpha,\omega}\mathcal D^{\mathrm{pre}}_{w,\alpha}\subseteq\operatorname{Dom}\delta^{\mathrm{phys}}_{w,\alpha,\omega}$ and

$$
V_{w,\alpha,\omega}\,\delta^{\mathrm{pre}}_{w,\alpha}
=
\delta^{\mathrm{phys}}_{w,\alpha,\omega}\,Q_{\alpha,\omega}
$$

on that domain. This quotient-factorization criterion constructs the physical distinction map instead of assuming it. The surrounding theory must still construct the observable net, state, and dynamics. The energy-solder inequality is a form comparison on the resulting carrier; it is not this realization map.

Let $\mathsf W$ be a measured family of admissible causal walls, contexts, cuts, or scale-localized tests. Require a measurable field of Hilbert response carriers $w\mapsto\mathcal K_w$, a dimensionless wall measure $\nu_{\mathsf W}$, and canonically fixed normalizations of both the fiber norms and $\nu_{\mathsf W}$. Each $w\in\mathsf W$ supplies a linear dimensionless distinction map on one common dense linear domain $\mathcal V\ni\Omega$,

$$
\delta_w:\mathcal V\subseteq\mathcal H\longrightarrow\mathcal K_w,
\qquad
\delta_w\Omega=0.
$$

Require $w\mapsto\delta_w\Psi$ to be measurable and square-integrable for every $\Psi\in\mathcal V$,

$$
\int_{\mathsf W}\|\delta_w\Psi\|_{\mathcal K_w}^2\,\mathrm d\nu_{\mathsf W}(w)<\infty.
$$

The densely defined direct-integral analysis operator and its initial quadratic form are

$$
\mathscr D\Psi:=(\delta_w\Psi)_{w\in\mathsf W},
\qquad
\mathfrak d_0[\Psi]
:=\|\mathscr D\Psi\|^2
=\int_{\mathsf W}\|\delta_w\Psi\|_{\mathcal K_w}^2\,\mathrm d\nu_{\mathsf W}(w).
$$

Assume $\mathscr D$ itself is closable and thereafter write

$$
\mathfrak d[\Psi]
:=
\|\overline{\mathscr D}\Psi\|^2,
\qquad
\operatorname{Dom}\mathfrak d
=
\operatorname{Dom}\overline{\mathscr D}.
$$

The family is a **causally complete distinction frame** when there is a dimensionless $\kappa_{\mathrm{fr}}>0$ such that

$$
\boxed{
\mathfrak d[\Psi]
\geq
\kappa_{\mathrm{fr}}\,\|(1-P_\Omega)\Psi\|^2.}
\tag{CF}
$$

For bounded $\delta_w$ with a companion upper bound, this is the ordinary [[library/continuous-frames-in-hilbert-space/inq|continuous-frame grammar]]. The derivation-valued continuum case is an unbounded closed-form analogue and should not be called a bounded frame without its domain theorem.

Equation (CF) is the exact algebraic meaning proposed for a **causal-frame lower bound**, or distinction grain: there is no normalized non-vacuum direction that becomes arbitrarily invisible to the entire physically admissible wall family. It is not a shortest distance. It is a lower singular-value bound for the analysis of physical distinction. The repository's dimensional causal grain $\lambda_*$ remains a correlation-length candidate; identifying $E_*=\hbar c/\lambda_*$ requires a separate same-carrier matching theorem.

The normalization clause is essential. Under $\delta_w\mapsto a\delta_w$, or the equivalent rescaling $\nu_{\mathsf W}\mapsto a^2\nu_{\mathsf W}$, one has $\mathfrak d\mapsto a^2\mathfrak d$ and $\kappa_{\mathrm{fr}}\mapsto a^2\kappa_{\mathrm{fr}}$. No separately meaningful number $\kappa_{\mathrm{fr}}$ exists until the response norms and measure are fixed by geometry rather than by the target spectrum. The subscripts also prevent unit collisions: $\kappa_{\mathrm{fr}}$ is not surface gravity, and the solder $\eta_{\mathrm{sol}}$ below is not an entropy-per-area density.

## The causal-frame gap theorem

Let $h$ be a densely defined closed nonnegative quadratic form on $\mathcal H$, with associated self-adjoint generator $H\geq0$, and suppose

$$
\Omega\in\operatorname{Dom}h,
\qquad
h[\Omega]=0.
$$

Assume the causal frame inequality (CF), $\operatorname{Dom}h\subseteq\operatorname{Dom}\mathfrak d$, an independently fixed energy scale $E_*>0$, and an independently proved **energy-solder inequality**

$$
\boxed{
h[\Psi]
\geq
\eta_{\mathrm{sol}}E_*\,\mathfrak d[\Psi]}
\tag{ES}
$$

for every $\Psi\in\operatorname{Dom}h$, where $\eta_{\mathrm{sol}}>0$ is dimensionless. More generally, it is enough that the common domain be a form core for $h$ and that the inequality extend under form closure.

**Causal-frame coercivity theorem.** Under these hypotheses, the following holds in quadratic-form sense:

$$
\boxed{
H\geq
\kappa_{\mathrm{fr}}\eta_{\mathrm{sol}}E_*(1-P_\Omega).}
\tag{Gap}
$$

Consequently $\Omega$ is the unique zero-energy vector and the energy gap satisfies

$$
\Delta_E\geq\kappa_{\mathrm{fr}}\eta_{\mathrm{sol}}E_*>0.
$$

**Proof.** Positivity and $h[\Omega]=0$ make $\Omega$ form-orthogonal to the whole form domain. Hence $h[\Psi]=h[(1-P_\Omega)\Psi]$. Applying (ES) and then (CF) gives

$$
h[\Psi]
\geq\eta_{\mathrm{sol}}E_*\mathfrak d[\Psi]
\geq\kappa_{\mathrm{fr}}\eta_{\mathrm{sol}}E_*\|(1-P_\Omega)\Psi\|^2.
$$

The representation theorem for closed forms gives the operator inequality. $\square$

Equivalently, the closed distinction form determines a positive operator

$$
L_{\mathrm{caus}}=\overline{\mathscr D}^{\,*}\overline{\mathscr D},
$$

and a stronger constitutive signature would first posit or derive the form sum

$$
h=\eta_{\mathrm{sol}}E_*\mathfrak d+\mathfrak r,
\qquad \mathfrak r\geq0,
$$

on a declared common form domain, with closure or relative-form-boundedness hypotheses. Only then may the associated operator be denoted schematically by $H=\eta_{\mathrm{sol}}E_*L_{\mathrm{caus}}+R$. This is the reversal tactic in operator form: the distinction form defines a generator; further Markov, locality, or carré-du-champ hypotheses are needed to reconstruct geometry. The spectrum of the generator does not retrospectively define the distinctions.

The theorem is exact but conditional. If $\mathscr D$ is chosen to be $(H|_{\mathcal H_0})^{1/2}$, or if the wall family is built from spectral projections of $H$, it is circular and explains nothing. The content lies entirely in constructing $\Omega$, $\delta_w$, $\nu_{\mathsf W}$, $\kappa_{\mathrm{fr}}$, $\eta_{\mathrm{sol}}$, and $E_*$ without using the gap they are meant to prove. Although $\kappa_{\mathrm{fr}}$ and $\eta_{\mathrm{sol}}$ transform reciprocally under an arbitrary rescaling of $\mathfrak d$, their product is invariant; the canonical normalization makes the separate factors explanatory rather than conventional.

## The three independent obligations

The product $\kappa_{\mathrm{fr}}\eta_{\mathrm{sol}}E_*$ separates three questions that equations in natural units usually obscure.

### Distinction completeness

The lower bound $\kappa_{\mathrm{fr}}$ is analytic and dimensionless, and geometric only when the tests, fiber norms, and measure are geometrically constructed. It asks whether the allowed causal tests cover the physical vacuum complement without blind directions. A merely separating family, for which

$$
\bigcap_w\ker\delta_w=\mathbb C\Omega,
$$

is insufficient: injective operators can have arbitrarily small singular values. A gap needs **uniform** separation, namely (CF).

This is where topology, incidence, knotting, cusp geometry, octonionic incidence data, finite index, or a descent obstruction could legitimately enter. They may define the channel family, its canonical normalization, its blind sectors, and therefore the analytic completeness problem whose answer is $\kappa_{\mathrm{fr}}$. Topology alone does not calculate a normalized lower frame bound, and it does not provide an energy unit. Wilson, 't Hooft, and Chern--Simons data also presuppose gauge data; they do not select $SU(3)$.

### Energetic soldering

The inequality (ES) says that a canonically normalized unit of algebraic distinction has a minimum cost relative to the independently calibrated physical energy form. The dimensionless comparison number is $\eta_{\mathrm{sol}}$. BKM response, relative entropy, conditional expectations, knot classes, and Connes cocycles are not energy simply because their quadratic expressions resemble an action.

A non-circular proof must be local or constitutive. For example, if

$$
h=\sum_xh_x,
\qquad
\mathfrak d=\sum_x\mathfrak d_x,
$$

one may prove $h_x\geq\eta_{\mathrm{sol}}E_*\mathfrak d_x$ from independently specified local algebra, state, and coupling data, then sum the inequalities. Merely declaring the global inequality is the gap assertion in new notation.

### Dimensional calibration

The dimensionless number $\kappa_{\mathrm{fr}}\eta_{\mathrm{sol}}$ cannot become a mass by multiplication with $c$, $\hbar$, or $k_B$ unless an independently constructed time, length, or temperature scale is also supplied. The clean alternatives are

$$
E_*=\hbar\omega_*,
\qquad
E_*=\frac{\hbar c}{\ell_*},
\qquad
E_*=k_BT_*,
$$

where $\omega_*$ is an angular frequency and $\omega_*$, $\ell_*$, or $T_*$ is physical member data rather than a renamed dimensionless logarithm. Newton's $G$ is different: together with $\hbar$ and $c$ it imports a gravitational coupling and the Planck scale, not a neutral unit conversion. Using it is substantive physical input and is circular in any purported derivation of $G$. Only after relativistic recovery may one write

$$
m_{\mathrm{gap}}=\frac{\Delta_E}{c^2},
\qquad
\tau_*=\frac{\hbar}{\Delta_E},
\qquad
\ell_*=\frac{\hbar c}{\Delta_E}.
$$

These are calibrated Compton presentations of one spectral threshold; they do not make energy, mass, time, and length the same concept. They become a measured channel's correlation time or length only if that channel has nonzero overlap with the lowest spectral support.

For pure four-dimensional Yang--Mills, the standard scheme-labelled candidate yardstick is the RG-invariant scale $\Lambda_{\mathrm{YM}}^{(s)}$, expressed here in energy units and fixed by a renormalization condition independent of the target gap. Along a tuned regulator trajectory, let $\widehat\Lambda_{\mathrm{YM},r}^{(s)}$ denote a finite-regulator estimator required to converge to that fixed scale. A useful target is therefore

$$
E_{*,r}=\widehat\Lambda_{\mathrm{YM},r}^{(s)},
\qquad
\inf_r\eta_{\mathrm{sol},r}^{(s)}>0,
$$

with the solder written $h_r\geq\eta_{\mathrm{sol},r}^{(s)}E_{*,r}\mathfrak d_r$ and the scheme dependence cancelling only in the complete physical product. A deeper causal-scale theory would improve this by independently constructing $\omega_*$ or $\ell_*$ and proving a same-carrier matching theorem to $\Lambda_{\mathrm{YM}}^{(s)}$; reciprocal transformation of a proposed $\eta_{\mathrm{sol}}^{(s)}$ cannot merely be assumed. Core trace scaling fixes an additive dimensionless coordinate $N$; it does not fix $\mathrm dN/\mathrm d\tau$. [[program-core/record-scale-soldering|Record--scale soldering]] already proves why order, clock rate, and acceleration are separate.

## Concrete realizations of the distinction maps

The abstract symbol $\delta_w$ has several legitimate realizations, but they cannot be mixed within one proof without an intertwiner.

### Gauge-flux derivations

At finite lattice regulator, after Gauss descent and the ground-state transform, left-invariant link derivatives give

$$
\mathfrak d_{a,L}[f]
=
\sum_{e,A}\int|X_e^Af|^2\,\mathrm d\nu_{a,L}.
$$

[[gauge-descent-flux-fisher-coercivity|Gauge descent, flux, and Fisher coercivity]] shows exactly that the transformed Kogut--Susskind energy is a dimensional kinetic coefficient times this vacuum-weighted Dirichlet form. Its dimensionless optimal Poincare constant, multiplied by that coefficient, is the energy gap. This is already one finite-regulator instance of the framework. Its unresolved parts are the independent construction/control of the vacuum measure and a lower bound uniform in volume and continuum removal.

The broader derivation grammar is mathematically standard: [[library/derivations-as-square-roots-of-dirichlet-forms/inq|closable derivations into Hilbert bimodules]] can square to Dirichlet forms and their positive generators. That gives a rigorous sense in which algebraic differentiation can precede the operator that later looks like a Laplacian. It does not choose the physical derivations or their scale.

### Conditional-expectation shells

Suppose a common faithful state admits a decreasing family

$$
\mathcal M_0\supseteq\mathcal M_1\supseteq\cdots
$$

and compatible Takesaki-admissible expectations $F_j:\mathcal M_0\to\mathcal M_j$. Their GNS implementations $Q_j$ are orthogonal projections on one common carrier, with $Q_jQ_k=Q_{\max(j,k)}$. If

$$
D_j:=Q_j-Q_{j+1},
\qquad
Q_0=I,
\qquad
Q_j\xrightarrow{s}P_\Omega,
$$

then

$$
\sum_j\|D_j\Psi\|^2
=
\|(1-P_\Omega)\Psi\|^2.
$$

This is a Parseval distinction frame with $\kappa_{\mathrm{fr}}=1$. [[spectral-wall-descent/conditional-expectation-balance|Conditional-expectation balance]] supplies the finite BKM Pythagorean analogue, while [[library/conditional-expectations-in-von-neumann-algebras/inq|Takesaki's theorem]] states the modular-invariance gate for the expectations.

There is an immediate anti-theorem: the two-stage expectation $\mathcal M\to\mathbb C1$ manufactures $1-P_\Omega$ for any state and is therefore tautological. A physical tower must be fixed before the spectrum by causal localization, bounded complexity, gauge equivariance, compositional descent, and scale covariance. Proving that such a tower exhausts only the vacuum is substantive.

There is also a continuum AQFT no-go. Let $\mathcal N\subseteq\mathcal M$ be ordinary nested local region algebras in the vacuum representation, with the vacuum cyclic for $\mathcal N$ and separating for $\mathcal M$, as supplied in the usual setting by [[library/remarks-on-unitary-equivalence-of-lorentz-invariant-fields/inq|Reeh--Schlieder]] and locality. If a vacuum-preserving conditional expectation $E:\mathcal M\to\mathcal N$ existed, then for every $n\in\mathcal N$ and $a\in\mathcal M$,

$$
\langle n\Omega,(a-Ea)\Omega\rangle=0.
$$

Density of $\mathcal N\Omega$ gives $(a-Ea)\Omega=0$, and separation gives $a=Ea$. Thus $\mathcal N=\mathcal M$. Under these hypotheses there is no proper vacuum-preserving expectation between the local region algebras. The shell route must therefore use regulator or RG coarse-graining algebras, a different comparison carrier or state, nonlocal but controlled blocks, or a weakened inequality in place of exact expectation. Ordinary AQFT inclusions cannot simply be relabelled as the desired wall tower.

### State-response Hessians

A faithful state family and a specified readout can equip state tangents with the BKM Hessian. Lost and retained directions under a state-preserving expectation then split orthogonally. This can supply the norm on $\mathcal K_w$, including central-sector resolution through [[program-core/center-valued-response|center-valued response]].

The Hessian is a metric of distinguishability. It is not yet the Hamiltonian form. The energy-solder map must take a transported state tangent to a vector or form direction on the physical carrier and prove (ES). The [[program-core/common-response-form|common response form]] correctly leaves this consumer map open.

### Topological and knot channels

Wilson loops, dual flux operators, linking pairings, and knot-sector projectors can add distinction channels. [[knotting-as-dimensional-presentation/inq|Knotting as dimensional presentation]] gives a conditional three-dimensional selection only for a primitive ordinary $S^1$ carrier with a faithful ambient embedding, nontrivial ambient isotopy, and a minimal-ambient-dimension rule; higher-dimensional codimension-two knots remain possible. It also explains why topology plus a scale-balancing energy can protect nontrivial sectors.

Topology alone is not a frame on $\mathcal H_0$. Ordinary fluctuations in the topologically trivial sector can remain invisible to all sector labels, making $\kappa_{\mathrm{fr}}=0$. Knot data contribute to a Yang--Mills gap only after a completeness theorem proves that the combined local, flux, and topological channels uniformly detect the entire vacuum complement.

## The factivity bridge: from nowhere in particular to here and now

The measurement analogy becomes useful only after separating three inequivalent meanings of “gap.”

1. A **pointing gap** is a change of type: an unpointed family, orbit, or torsor acquires a distinguished point. It has no numerical magnitude by itself.
2. An **information defect** is the distinction erased by a nonfaithful realization or coarse-graining map. A norm, relative entropy, or Hessian can measure it, but the result is dimensionless until soldered.
3. A **spectral gap** is the infimum of the physical energy form on normalized vectors orthogonal to the vacuum. It has energy units.

These can be stages of one construction, but they are not synonyms. [[algebra/local-global-individuation|Strict descent]] glues compatible local data and can be an equivalence; it need not forget anything. A torsor is likewise not a quotient with missing information: it has exact relative differences but no preferred origin. Choosing a point trivializes the torsor. A genuinely many-to-one operation instead requires a nonfaithful functor, quotient, channel, or conditional expectation as typed in [[algebra/nonfaithful-realization|nonfaithful realization]]. Not every fiber is a torsor, and not every descent residue is an entropy.

The finite commutative measurement model makes the next distinction exact. Let a readout context be

$$
\mathcal C_w\cong C(X_w)\cong\mathbb C^{n_w}
$$

with minimal events $e_{w,x}$ for $x\in X_w$. Restricting a state gives only the probability law

$$
p_\omega(x)=\omega(e_{w,x})\in\operatorname{Prob}(X_w).
$$

Even an instrument $\{\mathcal I_{w,x}\}_{x\in X_w}$, represented in the Heisenberg picture by normal completely positive maps with $\sum_x\mathcal I_{w,x}$ unital, supplies only

$$
p_\omega(x)=\omega\!\left(\mathcal I_{w,x}(1)\right),
\qquad
\omega_{w,x}(a)
=
\frac{\omega(\mathcal I_{w,x}(a))}{p_\omega(x)}
$$

when $p_\omega(x)>0$. An actual fact additionally supplies the character

$$
\chi_x:C(X_w)\longrightarrow\mathbb C,
\qquad
\chi_x(f)=f(x).
$$

Thus a state or probability law, an instrument branch, and an obtained value are differently typed. Within the finite commutative context, pure states do coincide with characters; purity of a state on the ambient noncommutative algebra does not make it multiplicative there. The algebra does not contain a canonical arrow from a general point of the probability simplex to one of its vertices. [[sufficient-reason/facticity-and-pointing|Factivity and pointing]] and [[conservation-of-causal-charge/factive-descent-and-records|factive descent and records]] isolate this missing selection without calling it unitary dynamics.

A durable “now” requires more than the obtained value. It is a stage in a directed record system $(\mathcal R_n,r_n)$ whose embeddings preserve the already realized characters. A “here” selects a contextual or spatial locus. Those are two separate pointings. The phrase “nowhere in particular to here and now” can therefore be made precise as

$$
\text{unpointed presentation}
\longrightarrow
\text{chosen context}
\longrightarrow
\text{outcome character}
\longrightarrow
\text{record extension}.
$$

None of these arrows is yet an energy operator. In particular, the obtained outcome is not the image of “phase space under collapse.” A finite readout restricts a state to a probability vector on $X_w$; the realized character evaluates each self-adjoint readout at one real value. The selection of that character is extra event data.

The phrase **residue cost** also needs a typed decomposition. If a finite tracial algebra admits a trace-preserving expectation $E:\mathcal M\to\mathcal N\subseteq\mathcal M$, view it as the trace-self-adjoint channel on $\mathcal M$ and use the same symbol for its action on density matrices. Then for a faithful density $\rho$ one has the exact information identity

$$
D(\rho\Vert E\rho)=S(E\rho)-S(\rho),
$$

where $S(\rho)=-\operatorname{Tr}(\rho\log\rho)$ is dimensionless; thermodynamic entropy in conventional units is $k_BS$. At a faithful reference density $\sigma\in\mathcal N$ fixed by $E$, write $\rho_t=\sigma+tX+O(t^2)$. Under the corresponding BKM-orthogonality hypothesis, the expectation is orthogonal at that common reference, so

$$
g_\sigma(X,X)-g_\sigma(EX,EX)
=
g_\sigma((1-E)X,(1-E)X).
$$

This is a dimensionless information residue. A cohomological obstruction to gluing, the kernel of a nonfaithful realization, this entropy defect, and the increment of a persistent record are four different residues. Any claimed conservation law for “causal charge” must first say which one is additive under which composition.

This suggests a **pre-factive causal-frame package** for each wall:

$$
\mathfrak W_w^{\mathrm{pre}}
=
\bigl(
\mathcal C_w,
E_w,
\{\mathcal I_{w,x}\}_{x\in X_w},
\mathcal R_w,
\delta_w
\bigr).
$$

Here $\mathcal C_w$ types the alternatives, $E_w$ or another declared coarse map types what becomes observationally indistinguishable, the instrument types conditional state change, $\mathcal R_w$ types possible persistence, and $\delta_w$ analyzes the corresponding *potential* physical distinction on the centered GNS carrier. It becomes factive only after adjoining pointed data

$$
\bigl(x_w,\chi_{x_w},r_w\bigr),
$$

where $x_w$ is obtained, $\chi_{x_w}$ is its context character, and $r_w$ is a compatible realized record character. When a state-preserving expectation is admissible on a common GNS carrier, one possible defect map is

$$
\delta_w(a\Omega)
=
\bigl(a-E_w(a)\bigr)\Omega.
$$

Its quadratic norm measures what the wall forgets; it does not select $x$. In ordinary nested vacuum local algebras the Reeh--Schlieder no-go above forbids a nontrivial expectation of this precise kind, so a viable package must use regulator, scale, comparison, or process data rather than silently assuming local projections.

The existing [[wall-construction-interface/core-spectral-wall|core spectral wall]] supplies one exact clue at the pointing stage: under its trace-scaling hypotheses, no nonzero normal state is invariant under the full scale action. A normalized viewpoint therefore cannot remain completely unpointed along scale. That theorem forces scale non-invariance; it does not choose an outcome character, create a record, identify physical time, or prove a Hamiltonian gap.

The strongest defensible common thesis is now this: the wall responsible for factive localization may also construct and canonically normalize the family $\{\delta_w\}$ whose completeness is measured by $\kappa_{\mathrm{fr}}$. If member dynamics then proves the independent solder $h\geq\eta_{\mathrm{sol}}E_*\mathfrak d$, the same architecture relates factual distinction to the mass gap without identifying them. The mass gap is not the energy released by wavefunction collapse. It is the minimum energetic price of a non-vacuum physical distinction **after** a carrier, vacuum, and time generator have been realized.

To turn the resemblance between the measurement and mass-gap problems into a theorem, the programme must therefore construct one process category and prove five separate facts:

1. a non-arbitrary pointing or factive rule yields contexts, outcomes, and persistent records;
2. its forgetful defects descend through $Q_{\alpha,\omega}$ to canonically normalized maps on the physical carrier;
3. those maps satisfy the uniform frame bound (CF);
4. the member energy satisfies the independent solder (ES); and
5. the realized carrier and dynamics recover the appropriate local QFT regime.

This is the exact place where “distinction precedes symmetry” can become mathematics. Symmetry organizes transformations within a presentation; pointing supplies the datum relative to which a presentation becomes this one. But only steps 3 and 4 imply a spectral gap.

## Why Type III and Connes data matter without being the gap

[[library/the-role-of-type-iii-factors-in-quantum-field-theory/inq|Local relativistic observable algebras are generically Type III]], so a density-matrix factorization of a region and its complement is not fundamental. More importantly, individual local factors can be abstractly isomorphic while different theories are carried by their inclusions, state spaces, covariance, and dynamics. This supports the relational diagnosis: the net and its gluing contain physical information that a single local algebra does not.

The Falcone--Takesaki core provides a canonical semifinite comparison carrier for Type III algebras, and Connes cocycles compare faithful state presentations. [[wall-construction-interface/core-spectral-wall|The core spectral wall]] already constructs exact trace-scaled cuts, transport, and a nonzero binary response. These data can:

- transport distinction maps between state or scale fibers;
- express coherence of the wall family under change of faithful weight;
- supply finite corners on which regulated response forms can be tested; and
- separate a dimensionless scale coordinate from state-dependent pointing.

They do not automatically supply physical time, the Yang--Mills vacuum, a Lorentzian Hamiltonian, or a positive gap. Modular flow and physical time may coincide in special KMS or wedge settings only after a physical identification. The Connes cocycle is a transport datum, not an energy unit.

A naturality condition for a causal-frame family has the schematic form

$$
V_{f,w}\,\delta_w
=
\delta_{f(w)}\,U_f,
$$

where $f$ is a causal inclusion or scale morphism, $U_f$ transports the physical carrier, and $V_{f,w}$ transports its response fiber. This is the descent statement needed before a collection of local wall tests can be called one geometric object.

## The continuum theorem target

Let $r=(a,L,\ldots)$ index regulators and volumes. Suppose each physical carrier has a vacuum $\Omega_r$, a densely defined closed energy form $h_r$, and a densely defined closed distinction form $\mathfrak d_r$, with

$$
h_r\geq0,
\qquad
h_r[\Omega_r]=0,
$$

and $\operatorname{Dom}h_r\subseteq\operatorname{Dom}\mathfrak d_r$. Require, for every $\Psi\in\operatorname{Dom}h_r$,

$$
\mathfrak d_r[\Psi]
\geq\kappa_{\mathrm{fr},0}\|(1-P_{\Omega_r})\Psi\|^2,
$$

$$
h_r[\Psi]
\geq\eta_{\mathrm{sol},0}\Lambda_r\mathfrak d_r[\Psi],
$$

where $\kappa_{\mathrm{fr},0},\eta_{\mathrm{sol},0}>0$ are independent of $r$, and $\Lambda_r\to\Lambda_*>0$ in one fixed renormalization convention. In the Yang--Mills target, $\Lambda_r$ may be the declared finite-regulator estimator $\widehat\Lambda_{\mathrm{YM},r}^{(s)}$ and $\Lambda_*=\Lambda_{\mathrm{YM}}^{(s)}$; the RG-invariant limit scale itself is not said to run along the tuned trajectory.

Assume additionally that:

- the varying physical Hilbert spaces have declared comparison maps;
- $h_r$ converges to a densely defined closed nonnegative form $h$ in the generalized Mosco sense;
- normalized vacua converge generalized-strongly, and their rank-one projections converge generalized-strongly relative to those maps, strongly enough that every recovery sequence $\Psi_r\to\Psi$ satisfies $P_{\Omega_r}\Psi_r\to P_\Omega\Psi$; and
- the limit reconstruction supplies the required local observable net, Poincare action, spectral condition, and nontriviality.

Generalized Mosco lower semicontinuity applied to $\Omega_r\to\Omega$ gives $h[\Omega]=0$. For any $\Psi\in\operatorname{Dom}h$, choose a Mosco recovery sequence $\Psi_r\to\Psi$. Then

$$
h[\Psi]
\geq\limsup_r h_r[\Psi_r]
\geq\kappa_{\mathrm{fr},0}\eta_{\mathrm{sol},0}\Lambda_*
\|(1-P_\Omega)\Psi\|^2,
$$

where the second inequality uses the uniform estimate, convergence $\Lambda_r\to\Lambda_*$, and the declared projection convergence. Hence

$$
\boxed{
h[\Psi]
\geq
\kappa_{\mathrm{fr},0}\eta_{\mathrm{sol},0}\Lambda_*
\|(1-P_\Omega)\Psi\|^2.}
$$

Thus the limit Hamiltonian has a zero-energy vacuum and a gap at least $\kappa_{\mathrm{fr},0}\eta_{\mathrm{sol},0}\Lambda_*$. This is a sufficient continuum theorem, not a claim that its premises have been proved for four-dimensional Yang--Mills. It exposes the exact place the problem lives: **uniform causal completeness plus uniform energetic soldering on an independently constructed continuum trajectory**.

Ordinary strong-resolvent language without vacuum control is too weak for this purpose. A finite-volume gap may collapse as $L\to\infty$, and a fixed-lattice gap says nothing about the tuned $a\to0$ limit. The regulator family and its comparison maps are part of the theorem.

## Recovery of observed QFT below a UV threshold

The causal-frame signature does not select $SU(3)$, nor should compatibility be advertised as doing so. It defines a class of admissible whole-state realizations. A Yang--Mills member is indexed by a compact simple group $G$; proving the axioms for every such $G$ remains the Clay obligation.

The phrase “below a UV threshold” is itself ill typed until the pre-QFT filtration has been soldered to local Lorentzian energy or length. It also must not mean a sharp spectral truncation of each local algebra: spectral projections are global and generally spoil algebra closure or locality. Keep the full local net and restrict comparison estimates to suitably smeared observables and matrix elements between states in a declared spectral window.

Let

$$
r=(a,L,M,b,\ldots),
\qquad
b=(g_{\mathrm{bg}},H_{\mathrm{bg}},R,\nabla R,\ldots),
$$

index the regulated surrounding theory and its actual background data, where $a$ is a length cutoff, $L$ a volume scale, and $M$ a heavy matching **energy**. Keep $M$, the cutoff energy $\Lambda_a=\hbar c/a$, the renormalization scale $\mu$, and $\Lambda_{\mathrm{YM}}^{(\mathsf s)}$ distinct. The probe energy $E$ labels the tested observable and state class; it is not part of the theory's identity. Two logically different correspondence contracts are then available.

**Retractive exact extension.** Conditional on the existence of an axiomatic target Yang--Mills net $\mathcal A_G$, a surrounding net $\mathcal B_{r,G}$ may contain it through natural injective $*$-homomorphisms

$$
J_{r,O}:\mathcal A_G(O)\hookrightarrow\mathcal B_{r,G}(O)
$$

and unital completely positive coarse-graining maps

$$
R_{r,O}:\mathcal B_{r,G}(O)\longrightarrow\mathcal A_G(O),
\qquad
R_{r,O}J_{r,O}=\operatorname{id}_{\mathcal A_G(O)}.
$$

The maps must commute with isotony morphisms and the relevant covariance actions, intertwine the dynamics, and induce the correctly directed state maps $\varphi_{\mathcal B}\mapsto\varphi_{\mathcal B}\circ J$ and $\omega_{\mathcal A}\mapsto\omega_{\mathcal A}\circ R$. Soundness requires admitted surrounding states to restrict to allowed target states; extendibility requires the declared target state class to arise or be approximated through the second map.

This retraction is stronger than a generic conservative extension. The map $J_OR_O$ is a UCP projection onto $J_O(\mathcal A_G(O))$ and hence a conditional expectation. If the surrounding state is $\widetilde\omega=\omega_{\mathcal A}\circ R$, that expectation is $\widetilde\omega$-preserving. The local-expectation no-go therefore makes a proper retractive extension impossible whenever $J_O(\mathcal A_G(O))\Omega$ is cyclic and $\Omega$ is separating for $\mathcal B_{r,G}(O)$. A proper exact surrounding must fail that target-subnet cyclicity condition, use a different comparison state or carrier, or omit the local retraction.

A one-sided retract also permits extra low-energy modes in $\mathcal B$. Equivalence in a probed regime requires either a reducing GNS complement carrying a restricted Hamiltonian uniformly above $M$, or an energy-constrained topology. For example, with $P_{\leq E}$ the spectral projection on the surrounding GNS carrier, require for every tested $B$

$$
\bigl\|P_{\leq E}
\bigl(B-JR(B)\bigr)
P_{\leq E}\bigr\|
\leq
C_B\|\boldsymbol\epsilon(E,r)\|^p.
$$

Full operator-norm convergence of a nontrivial idempotent $JR$ to the identity is not the intended claim.

**Approximate effective-field-theory recovery.** Ordinary renormalized Yang--Mills is empirically controlled in its laboratory domain even though an axiomatic four-dimensional pure-theory net is not yet constructed. For observables smeared on length scales much larger than $\hbar c/M$ and for matrix elements in a declared energy window, require explicit error bounds governed by

$$
\boldsymbol\epsilon(E,r)
=
\left(
\frac{aE}{\hbar c},
\frac{E}{M},
\frac{\hbar c}{LE},
\epsilon_{\mathrm{bg}}(E;b)
\right).
$$

Here $\epsilon_{\mathrm{bg}}(E;b)$ is derived from the background data rather than stored as a theory parameter; possible dimensionless terms include $\hbar H_{\mathrm{bg}}/E$, $\hbar c\sqrt{|R|}/E$, and adiabatic derivatives in the specified $b$. At finite parameters the assertion is $\|\boldsymbol\epsilon(E,r)\|\ll1$ with a norm and bound. The stronger continuum-decoupling limit holds $E$ in the physical window—at gap physics, $E\gtrsim\Delta_E\sim\Lambda_{\mathrm{YM}}$—while taking $a\to0$, $L\to\infty$, $M/\Lambda_{\mathrm{YM}}\to\infty$, and the background corrections to zero. Sending $E\to0$ would remove the spectral window whose gap is being tested.

In natural units only for the following local expansion, the same demand has the schematic form

$$
\Gamma_{r,\mu}^{\mathrm{phys}}
=
\Gamma_{\mathrm{YM},\mu}^{\mathrm{ren}}
\bigl(g_{\mathsf s}(\mu),\theta,\ldots\bigr)
+
\sum_{d>4,i}
\frac{C_{i,d}^{(\mathsf s)}(\mu)}{M^{d-4}}
\int_O\mathrm d^4x\,\mathcal O_{i,d}
+\mathcal R_{N,r}.
$$

Relevant and marginal threshold corrections must be matched separately, the coefficients run with $\mu$, and the remainder must be bounded in the tested class. This derivative expansion presupposes locality and analyticity in $p/M$; a horizon-scale or genuinely nonlocal correction is not automatically contained in the $d>4$ sum. Ward or BRST identities, unitarity, gauge-anomaly cancellation or matching, the correct trace anomaly, and exact Poincare covariance must hold in the Minkowski/decoupling limit. At finite curvature the appropriate demand is locally covariant QFT with Hadamard or microlocal state admissibility and quantified curvature corrections. [[compatible-with-existing-physics/local-physics-interface|The local-physics interface]] owns the full audit. If constructed, this route would supply compatibility plus constitutive closure, not emergence.

**Strong recovery.** If QFT itself is claimed to emerge from the pre-QFT data, the programme must construct a scaling or renormalization functor and prove convergence of states, observables, correlations, and dynamics to a Wightman or Haag--Kastler Yang--Mills theory; alternatively it may construct Euclidean Schwinger functions satisfying the Osterwalder--Schrader hypotheses and then reconstruct the Lorentzian theory. [[library/the-generally-covariant-locality-principle-a-new-paradigm-for-local-quantum-physics/inq|Locally covariant QFT]] supplies the relevant functorial grammar, while [[library/scaling-algebras-and-renormalization-group-in-algebraic-quantum-field-theory/inq|scaling algebras]] show how short-distance limits can be posed intrinsically for observable nets. This is much stronger than showing that new terms are small.

The minimal present claim should use approximate recovery, with exact extension stated only conditionally. The stronger route is required before saying that the framework derives QFT or completes the Clay existence theorem. A genuinely nonstationary cosmological spacetime may have no global time-translation Hamiltonian at all. Where a total generator exists, gapless gravitational or cosmological modes obstruct a total gap. An exact pure-Yang--Mills statement then requires an exact subnet or quotient whose GNS Hamiltonian is the pure-gauge one, a reducing projection commuting with the Hamiltonian and observable representation whose image exhausts the pure-gauge vacuum carrier, or a decoupling limit in which that carrier exists only in the limit. At finite gravitational coupling, arbitrarily soft gravitational excitations may leave only correlation or resonance thresholds rather than an exact gap of the total theory.

Finally, algebraic or weak-correlator recovery alone does not transfer a spectral gap: arbitrarily small spectral weight can disappear in such a limit. The mass-gap conclusion additionally requires the varying-carrier comparison maps, vacuum-projection convergence, uniform form coercivity, and identification of the limiting carrier with the pure-Yang--Mills vacuum representation from the preceding Mosco theorem.

## Algebraic meanings of the physical words

Within this construction the recurring terms have distinct mathematical jobs:

| Physical word | Algebraic or geometric role |
|---|---|
| space | the incidence, nesting, separation, and commutation relations among causal contexts; a metric can be a later consumer of a Dirichlet form or carré du champ |
| causality | the allowed direction and composition of context morphisms, together with locality or no-signalling constraints on their realizations |
| time | a realized one-parameter automorphism or unitary group; its orientation may be compared with a record order, but its rate is extra structure |
| energy | the self-adjoint generator $H$ of calibrated physical time; $h[\Psi]$ is its quadratic-form expectation, not a generic entropy or Hessian |
| mass | a Poincare-invariant spectral property after relativistic recovery; $m=E_{\mathrm{rest}}/c^2$ is a unit conversion, not conceptual identity |
| distinction grain | the canonically normalized dimensionless lower frame bound $\kappa_{\mathrm{fr}}$ |
| dimensional causal grain | the separately proposed correlation length $\lambda_*$; it enters this theorem only through a proved same-carrier calibration such as $E_*=\hbar c/\lambda_*$ |

This also limits the radiation intuition. A massless quantum has no rest frame, but an infinite-volume Minkowski vacuum theory with massless excitations can still possess local causal structure, observables, facts, dimensionful couplings, massive sectors, or a thermal rest frame; what it lacks is a global positive spectral gap. Finite-volume massless systems can instead have a box gap of order $1/L$. A conformal vacuum theory makes the stronger statement that there is no intrinsic scale. A positive gap is one sufficient robustness mechanism for finite-rate records, not a proved necessary condition for every possible record. [[causal-patch-boundary-and-two-times]] separates causal boundedness from UV regulation and gives the cross-carrier theorem needed before a dimensionless one-sided relaxation gap can be interpreted as a Hamiltonian mass gap.

The measurement analogy is therefore structural rather than literal. The factivity bridge above types the selection of a finite outcome separately from the dimensionless distinction defect and the Hamiltonian gap. Measurement and mass gap meet at the construction of a physical carrier and a complete family of alternatives; only the latter question invokes the energy-solder theorem.

## Where each existing clue can enter

| Clue | Legitimate contribution | Forbidden shortcut |
|---|---|---|
| Type III local factors | force state-, net-, and inclusion-sensitive localization | Type III implies a gap |
| Falcone--Takesaki core | canonical semifinite comparison and scale transport | core trace is physical energy or distance |
| Connes cocycles | coherent change of state presentation | cocycle parameter is automatically physical time |
| BKM or entropy Hessian | positive norm for state distinctions and exact expectation loss | distinguishability equals energy |
| conditional expectations | modularly admissible coarse channels and, for one compatible filtration, orthogonal shells | the trivial expectation to scalars explains the gap |
| fibers and descent | naturality and completeness of the wall family | formal gluing changes the physical carrier |
| knots and flux | on a finite pure-gauge graph, gauge closure sharpens the Haar flux-frame constant to $g(\Gamma)\lambda_G$: girth times the smallest allowed Casimir | graph cycles are already three-dimensional knots, or closed sectors exhaust all excitations |
| cusps or octonions | rigid incidence and candidate dimensionless coefficients | a pure number generates MeV |
| $c,\hbar,k_B$ | convert between already supplied physical time, length, mass, temperature, and energy scales | units manufacture a missing scale |
| $G$ | supplies a dimensionful gravitational coupling and, with $c,\hbar$, a Planck scale | a neutral conversion constant or a noncircular derivation of itself |
| Unruh or KMS temperature | possible clock-to-modular calibration after a physical acceleration is fixed | modular $2\pi$ alone sets the Yang--Mills scale |
| [[library/thermodynamics-of-spacetime-the-einstein-equation-of-state/inq|horizon thermodynamics]] | conditionally relates Einstein focusing to an already supplied universal entropy-per-area density and Unruh temperature | calculates that density or the Yang--Mills energy scale |
| [[library/on-the-origin-of-gravity-and-the-laws-of-newton/inq|entropic screen gravity]] | relates screen entropy gradients to force after bit-count and equipartition assumptions | hides that $G$ enters the screen normalization or supplies $E_*$ |
| cosmic expansion | supplies a rate $H_0$, hence the dimensionally valid energy $\hbar H_0$, subject to an independent cross-sector matching map | an FLRW rate is silently a stationary local QCD clock |

The current $4.2\,\mathrm{fm}$ causal-grain and $47\,\mathrm{MeV}$ diagnostics do not enter $E_*$ as a cutoff or particle energy. They are the same unit conversion, not independent evidence; their defensible role is a post-search numerical clue for a possible cross-sector relation. Any proposed numerical weld must be frozen before comparison, remain stable under unit and scheme changes, and prove why it acts on the same carrier as the Yang--Mills form.

## The first theorem programme

A concrete regulated target combines the exact lattice flux construction with a geometrically fixed causal-frame family. For each $r=(a,L)$, construct on one common physical GNS carrier a measurable family of gauge-equivariant, scale-local maps $\delta_{r,w}$ with canonically normalized response fibers and nonnegative dimensionless geometric measure $\nu_{\mathsf W,r}$. Require the resulting analysis operator to be densely defined and closable, and set

$$
\mathfrak d_r[\Psi]
=
\int_{\mathsf W_r}
\|\delta_{r,w}\Psi\|^2\,\mathrm d\nu_{\mathsf W,r}(w).
$$

The finite Haar carrier now supplies the first exact analytic benchmark for a possible realization of (P1). For a compact connected simple gauge group on a connected graph containing a cycle, the electric-flux analysis map restricted to gauge-invariant functions has the sharp frame constant

$$
\kappa_{\mathrm{Haar},\Gamma}
=
g(\Gamma)\lambda_G,
$$

where $g(\Gamma)$ is graph girth and $\lambda_G$ is the smallest nonzero Casimir in the declared invariant-metric convention. The proof is representation theoretic: every nontrivial closed spin network contains a cycle, and a Wilson character on a shortest cycle saturates the bound. [[gauge-descent-flux-fisher-coercivity]] gives the theorem and its assumptions. This is kinematic gauge closure, not factivity and not a specifically three-dimensional knot effect.

The physical vacuum changes the norm from product Haar to $\nu_{a,L}=\psi_{0,a,L}^2\mu_{a,L}$. A global density-ratio transfer is exact but normally deteriorates exponentially with volume. The sharper target is local: a uniform conditional Poincare constant plus a Wasserstein--Dobrushin influence matrix of spectral radius below one gives a vacuum-weighted flux Poincare bound. This is an exact finite Haar benchmark for (P1), not a realization of the causal-wall family. The wall-to-flux map and the interacting-vacuum, same-carrier, regulator-uniform estimate remain open.

If block expectations indexed by both scale and position are used to construct these channels, their defects form a general nonorthogonal frame unless a single compatible nested filtration or commuting multiresolution structure is separately proved. Only the ordered tower $F_j:\mathcal M_0\to\mathcal M_j$ above automatically gives orthogonal martingale differences. Prove directly that

$$
\mathfrak d_r[\Psi]
\geq
\kappa_{\mathrm{fr},0}\|(1-P_{\Omega_r})\Psi\|^2,
\tag{P1}
$$

and

$$
h_{r}[\Psi]
\geq
\eta_{\mathrm{sol},0}\widehat\Lambda_{\mathrm{YM},r}^{(s)}
\mathfrak d_r[\Psi],
\tag{P2}
$$

with $\kappa_{\mathrm{fr},0},\eta_{\mathrm{sol},0}>0$ independent of $a,L$. The fiber norms and measures must be natural under the regulator comparison maps and may not be rescaled by $a$ or $L$ to manufacture these uniform constants. Then construct the continuum comparison maps and prove the Mosco and vacuum-convergence hypotheses.

The measure and fiber norms must come from the causal/block geometry and renormalization prescription, not from the measured spectrum. (P1) is the causal-completeness theorem. (P2) is the energetic-solder theorem in the standard candidate yardstick. Either can fail independently. Together they imply the desired uniform gap.

The ground-state-transformed lattice identity says this programme is not empty: a flux Dirichlet form already equals the regulated energy form, and the Haar version has the exact girth--Casimir frame constant. The new work is to prove uniform local conditional gaps and subcritical block influence for the interacting vacuum, then show that their calibrated product survives renormalization.

## Stopping rule and failure contract

The framework has earned the status of a rigid research signature when its primitive wall category, transport, distinction maps, and dimensional solder contain no target-fitted functions. It has explained the gap for a member only when all of the following have been met:

1. the physical state and gauge quotient are constructed independently of the target spectrum;
2. the causal wall family is local, natural, and nontrivial, not the manufactured map $1-P_\Omega$;
3. the lower frame bound is proved uniformly in volume and regulator removal;
4. the energy-solder inequality is proved from member dynamics or adopted as a falsifiable constitutive law with an independent return value;
5. the dimensional yardstick is identified without unit alchemy or numerical fitting;
6. the Lorentzian or OS carrier, local net, covariance, spectral condition, and nontriviality survive the continuum limit; and
7. the conservative-restriction or strong-recovery contract is proved below the declared UV threshold.

Failure of any one gate localizes the mistake. A separating but non-frame wall gives no gap. A frame with no solder gives distinction without energy. A solder with no scale gives only dimensionless ratios. A finite-regulator bound with no uniform limit gives a lattice model, not the Clay theory. A low-energy fit with no independent construction gives redescription, not explanation.

The present verdict is therefore sharp: the causal-frame theorem supplies a principled mathematical shape for the category-error insight and identifies the operator signature that a pre-QFT construction would have to realize on the physical GNS carrier. The girth--Casimir theorem makes the first exact finite-regulator dent in (P1). It is not yet a solution of the Yang--Mills existence and mass-gap problem. The next genuine dent is the interacting part of (P1): prove from local vacuum dynamics, rather than a fitted spectrum, that conditional block distinctions have a uniform gap and that their total influence remains strictly below one along the continuum trajectory.
