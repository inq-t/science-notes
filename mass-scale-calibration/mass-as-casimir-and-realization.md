# Mass as Casimir and Realization

The deepest commonality among measurement, spontaneous symmetry breaking, and a mass gap is not one physical collapse mechanism. It is the possibility of a common grammar that admits distinguishable alternatives, together with separately typed possibilities of weighting them, pointing to one of them, recording that pointing, and assigning a dynamical cost. Relativistic mass occupies a particularly revealing slot in this grammar: momentum components generate translations within a Poincare representation, whereas mass is one Casimir label of its orbit or irreducible representation type. A Yang--Mills mass gap is then not “mass snapping into existence,” but the stronger spectral statement that the physical translation representation contains a vacuum atom and no nonvacuum spectral support arbitrarily close to it. The programme can explain that fact only by constructing the carrier and its representation, then proving coercivity; selection language alone cannot supply the gap.

**Status: [EXACT REPRESENTATION-THEORETIC DISTINCTIONS; EXACT COUNTEREXAMPLES; OPEN REALIZATION PROGRAMME].** The Robertson relation, moment-map/Casimir distinction, Poincare-sector classification, spectral-gap inequality, and typed separations below are standard or exact under their hypotheses. “Individuation under an invariant grammar” is a philosophical synthesis. No construction here proves four-dimensional Yang--Mills existence, chooses an actual measurement outcome, or derives a physical scale.

## The clue in the uncertainty principle

The useful intuition is that mass does not play the same algebraic role as momentum. The blanket sentence “the uncertainty principle does not apply to mass” is nevertheless too strong. For self-adjoint \(A,B\) and normalized \(\psi\in D(A)\cap D(B)\), the domain-safe Robertson bound is

$$
\Delta_\psi A\,\Delta_\psi B
\geq
\left|
\operatorname{Im}
\left\langle
(A-\langle A\rangle_\psi)\psi,
(B-\langle B\rangle_\psi)\psi
\right\rangle
\right|.
$$

Only when \(\psi\in D(AB)\cap D(BA)\) may its right-hand side be written

$$
\frac12
\left|
\langle\psi,[A,B]\psi\rangle
\right|.
$$

What is absent is a universal canonical observable \(Q_m\) satisfying

$$
[Q_m,M]=i\hbar 1
$$

for relativistic mass on every physical carrier. On one irreducible massive Poincare representation,

$$
M=m\,1,
$$

so \(\Delta_\psi M=0\) for every state in that representation and \(M\) commutes with every bounded operator on that irreducible carrier. The zero variance is not a new uncertainty principle. It says that the representation was already classified by a fixed mass.

On a reducible carrier, a superposition or mixture of distinct Poincare mass components can have \(\Delta M>0\), and Robertson applies to \(M\) and any other operator for which the commutator and domains are defined. For unstable excitations there need not even be a sharp one-particle mass eigenvalue; a resonance is encoded by scattering or correlation data rather than by a normalizable eigenvector. The exact clue is therefore:

$$
\boxed{
\text{momentum is a translation generator;}
\qquad
\text{mass is a Poincare-invariant function of its joint translation spectrum.}}
$$

[[library/the-uncertainty-principle/inq|Robertson's uncertainty relation]] supplies the general operator inequality. It does not privilege position and momentum except that their canonical commutator gives a state-independent lower bound.

## Classical reversal: mass labels the symplectic leaf

Let the proper orthochronous Poincare group act Hamiltonianly on a symplectic carrier \((X,\omega)\), with equivariant moment map

$$
J:X\longrightarrow\mathfrak p^*.
$$

For a translation generator \(e_\mu\in\mathfrak p\), the component

$$
P_\mu:=\langle J,e_\mu\rangle
$$

generates the corresponding spacetime translation. With signature \((+---)\), the first Poincare Casimir on \(\mathfrak p^*\) is

$$
C_1=P^\mu P_\mu.
$$

On a positive-energy massive coadjoint orbit,

$$
C_1=m^2c^2.
$$

The orbit carries its Kirillov--Kostant--Souriau symplectic form. Momentum components vary along it, while \(m\) is constant and supplies one invariant label of the symplectic leaf. The three-dimensional positive mass hyperboloid is only the momentum projection of the particle orbit and is not itself the full symplectic phase space; position or worldline and, when present, spin data complete the carrier. Energy sign and the Pauli--Lubanski or little-group data are also needed for orbit classification, and a Casimir level set need not be one orbit at singular or massless values.

There is a further type distinction. \(C_1\) is Poisson-central on the Lie--Poisson space \(\mathfrak p^*\). Its pullback \(C_1\circ J\) to a general Hamiltonian Poincare space is Poincare-invariant, but need not Poisson-commute with every function on that larger carrier. It becomes constant when the carrier itself is one transitive coadjoint orbit.

[[library/spinning-particles-coadjoint-orbits-and-hamiltonian-formalism/inq|Spinning particles, coadjoint orbits and Hamiltonian formalism]] supplies an explicit massive Poincare-orbit construction and its constrained Hamiltonian realization.

This gives the exact version of “mass is not in phase space”:

> On a fixed elementary mass-\(m\) orbit, mass is not an additional canonical coordinate. It is one invariant value classifying the orbit on which the canonical dynamics occurs.

The unqualified version is false. Mass has different types on different carriers.

| Carrier | Mathematical role of mass |
|---|---|
| fixed elementary coadjoint orbit | constant leaf label |
| ambient Lie--Poisson space \(\mathfrak p^*\) | Casimir function whose level sets organize orbits |
| unreduced relativistic particle phase space | parameter in the constraint \(P^2-m^2c^2=0\) |
| composite or field phase space | generally nonconstant invariant \(M^2=P_{\mathrm{tot}}^2/c^2\) |
| gravitational phase space | possible Hamiltonian boundary charge, such as an ADM-type mass under its hypotheses |

Two nonparallel photons provide the simplest correction. Although each has zero rest mass, their total four-momentum can be timelike:

$$
M_{\mathrm{pair}}^2c^4
=
2E_1E_2(1-\cos\theta).
$$

The composite invariant mass varies continuously with the relative angle. Thus mass is not metaphysically forbidden from being an observable function on phase space. It is non-dynamical only after one has restricted to a fixed elementary orbit.

## Quantum reversal: mass labels Poincare representation components

Let the Poincare group be represented strongly continuously and unitarily, with spacetime translations

$$
U(a)
=
\exp\!\left(-\frac{i}{\hbar}a^\mu P_\mu\right),
\qquad
P^\mu=(H/c,\mathbf P).
$$

Assume the joint spectrum condition

$$
\operatorname{sp}(P)\subseteq\overline V_+.
$$

The four commuting self-adjoint generators \(P_\mu\) have a joint spectral measure. Define the nonnegative mass-squared operator by functional calculus,

$$
M^2
:=
\frac{P^\mu P_\mu}{c^2}.
$$

On an irreducible positive-energy massive Poincare representation, Schur's lemma gives

$$
M^2=m^2\,1,
$$

and the remaining intrinsic label is a representation of the little group. This is the precise content behind the particle-language claim that mass and spin classify elementary relativistic sectors. [[library/on-unitary-representations-of-the-inhomogeneous-lorentz-group/inq|Wigner's classification]] is the primary source.

A quantum field theory vacuum Hilbert space is not one irreducible Poincare representation. Schematically, and suppressing multiplicities and continuum subtleties, its unitary Poincare representation can be decomposed as

$$
\mathcal H
=
\mathbb C\Omega
\oplus
\int_X^\oplus
\mathcal H_{m,s,\alpha}\,
\mathrm d\mu(m,s,\alpha),
$$

$$
M^2
=
0\,P_\Omega
\oplus
\int_X^\oplus
m^2 1_{m,s,\alpha}\,
\mathrm d\mu(m,s,\alpha).
$$

Stable one-particle species may appear as isolated mass hyperboloids. Multiparticle states normally provide continuous invariant-mass spectrum above thresholds. These Poincare components are not automatically superselection sectors of the observable algebra; local observables can create vectors with support across many invariant masses inside one vacuum representation. A positive mass gap therefore does **not** mean that every allowed mass is discrete. It means that the vacuum point is spectrally isolated from every nonvacuum excitation.

In a Poincare-covariant positive-energy vacuum representation, one convenient joint-spectrum statement is

$$
\boxed{
\operatorname{sp}(P)
\subseteq
\{0\}
\cup
\left\{
p\in\overline V_+:
p^\mu p_\mu\geq m_*^2c^2
\right\},
\qquad m_*>0.}
\tag{MG}
$$

Let \(E_P\) be the joint spectral measure and define the complete zero-momentum projection

$$
P_0:=E_P(\{0\}).
$$

The isolated set \(\{0\}\) in \((\mathrm{MG})\) is the vacuum four-momentum. The second set excludes nonzero null excitations as well as arbitrarily small timelike masses. Under full Lorentz covariance, invariance of the joint spectrum, and the spectrum condition,

$$
(\mathrm{MG})
\quad\Longleftrightarrow\quad
H\geq m_*c^2(1-P_0),
$$

in quadratic-form sense. Lorentz invariance is load-bearing in the converse: a timelike orbit contains its rest-energy point, while a nonzero null orbit contains energies arbitrarily close to zero under boosts. This is the exact bridge between the Hamiltonian and invariant-mass formulations; it is available only after Poincare covariance and the spectrum condition have been constructed.

[[mass-scale-calibration/mass-as-a-calibrated-distinction-rate]] gives the corresponding rate presentation. On the vacuum complement, the derivative of the dimensionless transfer depth \(R(\ell)=-\log\|e^{-\ell H/(\hbar c)}(1-P_0)\|\) is \(\Delta_E/(\hbar c)\); only the equivalence above licenses its final retyping as \(m_{\mathrm{gap}}=(\hbar/c)\,\mathrm dR/\mathrm d\ell\). This makes mass convertible to a calibrated persistence rate without turning it into a canonical phase-space coordinate or a stream of measurement outcomes.

### A Poincare Hamiltonian has no positive eigenvalues

**[EXACT CONSEQUENCE OF BOOST COVARIANCE]** A positive gap is compatible
with a continuous energy spectrum above its threshold. A positive
**energy eigenvalue** is not: in any strongly continuous positive-energy
unitary representation of the Poincare group with at least one spatial
dimension,
\[
\boxed{1_{\{E\}}(H)=0\quad\text{for every }E>0.}
\tag{PE1}
\]
This concerns normalizable Hilbert vectors, not generalized plane waves.
It requires neither separability nor an upper energy bound.

**Proof.** Let \(B_s\) implement a boost of rapidity \(s\) in the first
spatial direction, choosing its sign so that
\[
B_sHB_s^*=H\cosh s-cP_1\sinh s.
\tag{PE2}
\]
The right side is the self-adjoint operator defined by joint spectral
calculus, not an unqualified sum on arbitrary domains. For any vector
\(\psi\), let \(\mu_\psi\) be its finite joint spectral measure for
\((H,cP_1)\), and put \(Q_E=1_{\{E\}}(H)\). Spectral covariance gives
the nonnegative function
\[
F_\psi(s):=\langle\psi,B_sQ_EB_s^*\psi\rangle
=\int 1_{\{E\}}(h\cosh s-p\sinh s)\,d\mu_\psi(h,p).
\tag{PE3}
\]
For each fixed \((h,p)\) and \(E>0\), setting \(r=e^s>0\) turns the
level-set equation into
\[
(h-p)r^2-2Er+(h+p)=0.
\]
This nonzero polynomial has at most two roots, so the level set has
Lebesgue measure zero in rapidity. Tonelli's theorem yields
\(\int_{-R}^R F_\psi(s)\,ds=0\) for every \(R>0\). Strong continuity
of \(B_s\) makes \(F_\psi\) continuous; hence
\(\langle\psi,Q_E\psi\rangle=F_\psi(0)=0\). Since \(\psi\) was
arbitrary, \(Q_E=0\). Massless spectral points cause no exception:
when \(h=|p|>0\), the level equation has at most one root. The spectrum
condition separately identifies \(1_{\{0\}}(H)=P_0\), the complete
zero-translation subspace; it need not be one-dimensional. \(\square\)

There is also a **bounded-energy corollary**. If \(H\) is bounded in
such a representation, every nonzero point of its forward-cone joint
spectral support would acquire arbitrarily large energy under suitable
boosts, contradicting the bound. Thus \(H=0\) and all spatial
translation generators vanish. This excludes a fixed bounded
unit-rate response from being the nontrivial Poincare Hamiltonian
itself; it does not exclude its use as a transfer defect or a
comparison form.

The unbounded case is not rescued by a number-operator clock. Let
\(N=\sum_n n\Pi_n\) have a complete pure-point decomposition, allowing
infinite-dimensional eigenspaces. Every nonnegative scalar functional
calculus \(f(N)\), finite on the occupied eigenvalues, retains this
pure-point spectral type. If \(f(n)>0\) for any nonzero \(\Pi_n\), it
violates (PE1) as a proposed same-carrier Poincare Hamiltonian. A dense
closure of the numerical values \(f(n)\) would not change that spectral
type. Even a bounded map intertwining the same unitary clock with a
Poincare clock must annihilate every positive-eigenvalue subspace.

In particular, the full invariant
[[gauge-boundary-frame-gluing/shared-driver-response-and-the-nested-holonomy-clock|shared-driver OU clock]]
has an explicit eigenvector at energy \(2\) in its unit convention.
No positive rescaling of that clock can be the returned Hamiltonian.
It can still serve as an auxiliary response or as **internal mass
input on a new carrier**: a fixed discrete Casimir value
\(M=mI\) is compatible with continuously varying momentum and
\(H=\sqrt{c^2\mathbf P^2+m^2c^4}\). That construction changes the
translation carrier and operator; it is not a scalar reparametrization
of \(N\), and the mass-shell input alone does not construct an
interacting Yang--Mills theory. Finite boxes, compact spatial models,
and purely internal clocks need not admit the boosts used in (PE2).

## Three centers that must not be conflated

The word “central” tempts a false unification.

1. \(P^\mu P_\mu\) is central in the universal enveloping algebra of the Poincare Lie algebra and acts scalarly on an irreducible Poincare representation.
2. The center \(Z(\pi(\mathfrak A)'')\) of a represented observable algebra may decompose a state into superselection or phase components.
3. A commutative measurement context \(\mathcal D\) has a spectrum of characters that label its sharp classical alternatives.

These are different algebras and different decompositions. The Poincare Casimir need not be a central element of a local observable algebra. One interacting vacuum representation can contain many invariant masses. A character of one readout context need not choose a superselection sector, and a superselection character need not be a measurement outcome.

The finite-graph Yang--Mills calculation contains a fourth object:

$$
C_2^G(R),
$$

the dimensionless quadratic Casimir of the **internal gauge group**. It controls link-Laplacian eigenvalues in the regulated electric form. It is not the spacetime Casimir \(P^2\). [[strong-coupling-gap-and-continuum-crossover/gauge-descent-flux-fisher-coercivity]] proves how internal representation data contribute to a regulator-level coercivity constant; dynamics, the vacuum weight, continuum passage, and the energy scale are still required before that number can constrain \((\mathrm{MG})\).

## The common realization ledger

The same-concept intuition survives if it is stated one level of abstraction higher. A typed bookkeeping signature is

$$
\boxed{
\mathfrak R
=
\bigl(
I,
\pi:\mathcal X\to I,
p,
i_*,
\mathcal R_{i_*};
\mathcal K_h,D(\mathfrak h),\mathfrak h
\bigr).}
\tag{R}
$$

Here \(I\) is a measurable index space when probabilities are used; \(\pi\) presents a family of alternatives or fibers; \(p\in\operatorname{Prob}(I)\) is optional; \(i_*\in I\) is an optional obtained point; \(\mathcal R_{i_*}\) is an optional record attached to that point; and \(\mathfrak h\) is an optional closed positive form with declared Hilbert carrier \(\mathcal K_h\) and domain \(D(\mathfrak h)\). A map from the alternative family into the form carrier must also be supplied before \(\mathfrak h\) can price those alternatives.

Adjoining \(i_*\) records that an outcome or phase has been chosen; it does not construct the choice. Until a selection or actuality morphism is supplied, \(i_*\) is exogenous event data. Likewise, (R) is not yet a category, an invariant, or a theorem: no morphisms, group action, equivariance law, or preservation axiom has been declared. It is an interpretive type ledger showing which data a future construction must relate.

This is more general than “stratification.” A sharp PVM decomposes a Hilbert space into orthogonal spectral subspaces, but a generic superposition lies in no single eigenspace. A POVM may have overlapping effects and no subspace decomposition at all. A broken-symmetry vacuum family may be one smooth homogeneous orbit \(G/H\). A mass gap is an empty spectral interval, even when the spectrum above it is continuous.

| Phenomenon | Alternatives | Weighting | Pointing or selection | Dynamical cost |
|---|---|---|---|---|
| sharp measurement | measurable outcome space and PVM propositions \(B\mapsto E_A(B)\) | Born measure from a state | an obtained label or character; an instrument branch gives the conditional state **given** that label but does not obtain it | none follows from projectivity or discreteness |
| general measurement | measurable outcome space and POVM effects, which can overlap | Born measure | obtained outcome plus an outcome-indexed CP branch | independent of the Hamiltonian gap |
| spontaneous symmetry breaking | symmetry-related extremal phases, possibly in disjoint GNS representations rather than a canonical fiber bundle | optional ensemble | boundary condition, quasi-average, or thermodynamic phase prescription | may be positive or zero |
| mass gap | vacuum and nonvacuum spectral support of \(H,P_\mu\) | no probability law required | no measurement outcome is selected | the defining content is coercivity away from the vacuum |

The strongest defensible synthesis is therefore

$$
\boxed{
\text{organization of alternatives}
\neq
\text{pointing}
\neq
\text{record formation}
\neq
\text{energetic separation}.}
$$

Philosophically, these are species of **individuation under an invariant grammar**. Mathematically, they occupy different slots of the ledger (R). To make the grammar invariant, a future theory must supply the relevant group or groupoid actions and prove the preservation laws. It could then derive several slots from one construction, but it would have to display the maps rather than identify the words.

## Why collapse is not yet the gap

For a finite atomic commutative readout context \(\mathcal D\simeq\mathbb C^n\subseteq\mathcal M\), restriction gives

$$
\omega|_{\mathcal D}
\longleftrightarrow
\mu_{\omega,\mathcal D}
\in
\operatorname{Prob}(\operatorname{Spec}\mathcal D).
$$

A finite Heisenberg-picture instrument consists of normal completely positive maps \(\{\mathcal I_i\}_{i=1}^n\) whose sum is unital. It gives

$$
p_i=\omega(\mathcal I_i(1)),
\qquad
\omega_i(A)
=
\frac{\omega(\mathcal I_i(A))}{p_i}.
$$

The posterior \(\omega_i\) is defined when \(p_i>0\) and is conditional on \(i\). Neither the state, the PVM or POVM, nor the instrument alone returns the obtained label \(i_*\) and its durable record. General outcome spaces require a countably additive measurable instrument \(B\mapsto\mathcal I(B)\). [[library/an-operational-approach-to-quantum-probability/inq|Davies and Lewis]] supply the instrument framework; [[sufficient-reason/quantum-interpretations|Quantum interpretation and the type change]] records the remaining actuality debt.

By contrast, a gap says

$$
\mathfrak h[\Psi]
\geq
\Delta_E\|(1-P_0)\Psi\|^2.
$$

This is a statement about every vector in the form domain, whether or not anyone measures it. It supplies neither \(i_*\) nor \(\mathcal R\). A gap may make records dynamically robust, and a fact-forming wall may help construct the same carrier on which the gap is proved, but those are comparison theorems still to be built. [[physical-response-coercivity/physical-distinction-coercivity]] gives the exact same-carrier formulation.

## Why symmetry breaking is not yet the gap

Let \(G\) act on an infinite-system observable algebra by \(\alpha_g\), with \(G\)-invariant dynamics. For an extremal ground or KMS phase \(\omega\), spontaneous symmetry breaking means that the phase is not invariant:

$$
\omega\circ\alpha_g\neq\omega
$$

for some \(g\); in algebraic formulations the transformed state may lie in a disjoint GNS representation, so the symmetry need not be unitarily implementable within the selected phase. Noninvariance of an arbitrary prepared state would not by itself constitute SSB. The orbit of phases is organized by the stabilizer \(G_\omega\). This is state or phase pointing, not automatically a spectral bound. [[library/broken-symmetries/inq|Goldstone, Salam, and Weinberg]] prove, under the relativistic continuous-global-symmetry hypotheses, precisely the opposite tendency: a noninvariant vacuum entails massless excitations. Continuous global SSB is therefore a sharp counterexample to

$$
\text{selection}\Longrightarrow\text{gap}.
$$

Discrete broken phases can have a positive excitation gap in each selected pure-phase GNS representation, while symmetric phases can also be gapped. Symmetry-related infinite-volume vacua need not coexist as vectors in one “complete vacuum subspace.” For local gauge redundancy, [[library/impossibility-of-spontaneously-breaking-local-symmetries/inq|Elitzur's theorem]] blocks treating a gauge-variant order parameter as a gauge-invariant spontaneous breaking in the unfixed lattice theory. The Higgs mechanism reorganizes the physical linearized spectrum around a chosen field configuration, but pure Yang--Mills has no Higgs field and its expected gap is not a gauge-symmetry-breaking theorem.

## Counterexamples that type the distinction

Any proposed common mechanism must survive these tests.

- A projection has values \(0,1\) even on a gapless quantum field carrier. Discrete measurement alternatives do not imply an energy gap.
- A massive free scalar has a positive gap and a unique symmetry-invariant vacuum. A gap does not imply SSB or outcome actualization.
- A harmonic oscillator is gapped while its position observable has continuous spectrum. A gap does not discretize observation generally.
- A continuously broken relativistic global symmetry has selected vacuum phases and, under the Goldstone hypotheses, massless modes. SSB does not imply a gap.
- A measurement can preserve the same Poincare mass component before and after its recorded result. Outcome selection need not select a Poincare representation.
- A superselection sector can itself be gapless. Sector individuation does not imply coercivity.
- Two photons can have continuously variable composite invariant mass. “Mass is a sector label” is exact only for an elementary irreducible carrier, not every system.

There is an exact same-carrier no-go. Keep all alternatives, projections, obtained labels, and record data fixed on

$$
\mathcal H
=
\mathbb C\Omega\oplus\ell^2(\mathbb N),
$$

but choose either

$$
H_{\mathrm{gap}}
=
0\oplus 1,
\qquad
H_{\mathrm{soft}}
=
0\oplus
\operatorname{diag}
\left(1,\frac12,\frac13,\ldots\right).
$$

Both operators have the same unique vacuum line and can coexist with exactly the same measurement and record structure. The first has gap \(1\); the second has spectrum accumulating at zero and has no positive gap. Moreover, \(H\mapsto\lambda H\) leaves its eigenspaces and every selection datum fixed while rescaling the dimensional gap. Therefore no realization ledger lacking an independently constrained dynamical form can imply either positivity or the value of a gap.

These do not kill the philosophical unification. They identify its correct altitude: the invariant organization of alternatives is common; the physical operators that weight, point, record, and charge those alternatives are not.

## What observation of mass means

Momentum is operationally tied to translations: its components are the generators detected through spatial and temporal translation response. Mass is inferred invariantly from the joint energy--momentum structure—for example from a stable dispersion relation, a rest-energy determination, or a composite invariant reconstructed from decay products:

$$
E^2-c^2\mathbf p^2=m^2c^4.
$$

Within one irreducible Poincare representation, repeated ideal measurements do not reveal a fluctuating mass coordinate; they identify which representation the observed excitation instantiates. Momentum can vary continuously while mass remains fixed. This supports the user's contrast, but also establishes a limit:

> Relativistic mass is not conceptually prior to all space and time. As \(P^2\), it is defined by the geometry and symmetry of spacetime translations.

If the programme proposes a more primordial “mass” meaning resistance to factive formation, causal directedness, or obstruction to descent, that upstream object must receive a different symbol until a reconstruction functor proves that it becomes the Poincare Casimir or Hamiltonian threshold. Otherwise the desired conclusion has entered through vocabulary.

## Calibrating an already reconstructed mass

The Poincare invariant becomes a dimensional mass through a calibrated metric and comparison constants. [[quantity-lines-and-conformal-scales|Quantity lines and conformal scales]] distinguishes a reporting-unit basis from a physical metric section and states the extra map needed to relate them. [[gravitational-and-compton-lengths|Gravitational and Compton lengths]] then gives two reciprocal presentations of a supplied positive mass; neither conversion generates its value.

The [[dilation-covariant-spectra/inq|dilation theorem]] forbids a nontrivial positive spectral gap for one nonzero generator with exact unitary dilation covariance on the same carrier. The [[scale-torsor-and-the-global-local-gap-invariant|scale-family construction]] instead compares matched operators on calibrated members and preserves their dimensionless transfer edge. It allows a gap, but does not prove that edge positive. Selection of a member, a change of units and a renormalization-scheme change have separate transformation laws.

For pure Yang–Mills, the [[yang-mills-scale-and-gravity-decoupling|scale and gravity-decoupling contract]] keeps the renormalized gauge scale fixed independently of any gravitational embedding. The physical spectrum must be recovered on the pure-gauge carrier; a dimensional conversion or a scale anomaly does not supply that recovery.

## The Yang--Mills theorem target after the reversal

The representation-theoretic retyping changes the research question from

> What local field gives a mass to a massless gluon?

to

> Why does the physical gauge-invariant vacuum representation of translations have an isolated vacuum and no nonvacuum support adjacent to it?

That is a real improvement. It removes the gauge-potential mass-term category error while leaving the Clay problem intact. The official target still requires construction of the nontrivial continuum theory and a positive gap; [[contemporary-puzzles/yang-mills-mass-gap/puzzle-as-posed]] states it precisely.

A pre-QFT or boundary-first programme would make a genuine contribution by constructing, without using the desired spectrum:

1. a physical carrier, Poincare action, and joint spectrum condition recovered from the proposed prelocal geometry;
2. its gauge-invariant vacuum state and complete vacuum projection \(P_0\);
3. a canonical decomposition or joint spectral measure for the reconstructed translations;
4. a normalized dimensionless response form with a uniform positive lower bound on every nonvacuum physical direction;
5. a noncircular same-carrier comparison with the Hamiltonian form; and
6. an independent dimensional scale that survives regulator and infinite-volume limits.

The [[scale-relative-response-and-yang-mills|scale-relative response theorem]] supplies the conditional analytic core: a response lower bound in the physical norm, an independently normalized energy comparison, and coverage of a complex physical energy-form core imply a Hamiltonian floor. [[physical-response-coercivity/causal-frame-coercivity|Causal-frame coercivity]] supplies a family of response channels. [[global-local-response-reconstruction/causal-patch-boundary-and-two-times|The causal-patch comparison]] explains why a map forming or forgetting the observable carrier is not itself the tangential response form that gaps excitations within it.

The Casimir insight adds the spectral stopping condition. After Poincare recovery, the same theorem must imply

$$
\operatorname{sp}(P)
\subseteq
\{0\}
\cup
\{p\in\overline V_+:p^2\geq m_*^2c^2\}.
$$

This is where a dimensionless internal Casimir, knot invariant, index, boundary response, or entropy Hessian could enter: as part of the proof of a positive response lower bound, not as the mass itself. The independent yardstick supplies units. The Poincare reconstruction identifies the resulting energy threshold as mass. Every arrow has a different job.

## Operator ledger

| Operator or map | Operates on | Returns | Missing before a mass-gap conclusion |
|---|---|---|---|
| \(P_\mu\) | physical vectors in the translation-generator domains | infinitesimal spacetime translations | the spectrum must be constructed and controlled |
| \(M^2=P^2/c^2\) | joint spectral carrier of translations | invariant-mass classification | it does not isolate the vacuum by itself unless nonzero null sectors are excluded |
| internal \(C_2^G\) | gauge-group representations or link harmonics | dimensionless representation eigenvalue | vacuum dynamics, energy coefficient, and continuum survival |
| spectral projection \(E_A(B)\) | Hilbert vectors | subspace for a proposition | obtained outcome and record |
| instrument branch \(\mathcal I_i\) | states or observables | probability and conditional update | why \(i\) actually obtains |
| SSB phase-selection prescription | state space or thermodynamic net | one extremal phase/representation | no energy lower bound follows |
| wall expectation or formation map | pre-observable algebra/carrier | retained observable carrier | its defect vanishes on its range |
| tangential response form \(\mathfrak d\) | variations within the retained physical carrier | dimensionless distinction cost | energy solder and scale |
| Hamiltonian form \(h\) | physical vacuum representation | clock-translation energy | coercivity must be proved, not renamed |

The core reversal is therefore not “collapse, SSB, and mass gap are identical.” It is sharper:

$$
\boxed{
\begin{aligned}
\text{invariant grammar} &\;\text{organizes alternatives},\\
\text{pointing} &\;\text{individualizes a realization},\\
\text{record order} &\;\text{makes that realization persistent},\\
\text{coercivity} &\;\text{separates nonvacuum physical distinctions},\\
\text{Poincare covariance and the spectrum condition}
&\;\text{type the separation as invariant mass}.
\end{aligned}}
$$

That chain respects the hunch while exposing exactly what must still be constructed.
