# Mass as Casimir and the Realization Signature

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

the dimensionless quadratic Casimir of the **internal gauge group**. It controls link-Laplacian eigenvalues in the regulated electric form. It is not the spacetime Casimir \(P^2\). [[gauge-descent-flux-fisher-coercivity]] proves how internal representation data contribute to a regulator-level coercivity constant; dynamics, the vacuum weight, continuum passage, and the energy scale are still required before that number can constrain \((\mathrm{MG})\).

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

This is a statement about every vector in the form domain, whether or not anyone measures it. It supplies neither \(i_*\) nor \(\mathcal R\). A gap may make records dynamically robust, and a fact-forming wall may help construct the same carrier on which the gap is proved, but those are comparison theorems still to be built. [[physical-distinction-coercivity]] gives the exact same-carrier formulation.

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

## Mass in gravitational and quantum length conversions

The phrase “scale distinguishes here and now from there and then” contains three different structures.

| Question | Minimal mathematical datum |
|---|---|
| which event or region? | points, regions, incidence, algebraic inclusion, or a record index |
| which events can influence which? | causal order or conformal cone structure |
| how much interval separates them? | a metric representative, equivalently a conformal scale section |

Causal order can determine a conformal class \([g]\) under the reconstruction hypotheses, but not its scale. A positive section

$$
\sigma\in\Gamma(\mathcal E[1])
$$

selects a representative \(g_\sigma=\sigma^{-2}\mathbf g\). [[conformal-scale-geometry/causal-order-and-metric-scale|Causal order and metric scale]] makes this distinction precise. The constant \(c\) then compares already calibrated spatial and temporal units and fixes the slope of the null cone in those units. It does not distinguish the events, select \(\sigma\), or make facts occur.

In a flat translation-invariant realization, let \(\eta_\sigma\) be the calibrated Minkowski representative preserved by translations and identify the dual translation Lie algebra with constant covectors. Only on that carrier may the global translation generators be contracted with the metric:

$$
\boxed{
M^2
=
\frac{\eta_\sigma^{-1}(P,P)}{c^2}
=
\frac{H^2}{c^4}
-
\frac{\mathbf P^2}{c^2}.}
\tag{S1}
$$

On a curved spacetime or for a nonconstant scale section, a local cotangent vector can have the pointwise norm \(m^2(x)=g_x^{-1}(p_x,p_x)/c^2\), but that is not automatically a global Poincare Casimir. A general change of physical scale geometry can destroy global translations altogether.

Equation (S1) says that the **dimensional norm requires a physically calibrated metric scale**. Causal order alone gives only its conformal type. A simultaneous change of conformal presentation for \(\mathbf g\) and \(\sigma\) leaves the physical metric \(g_\sigma\) unchanged, just as a mere change of units leaves dimensionless predictions unchanged. Physical mass variation would require an additional dynamical scale field and coupling. Conformal metric scale and renormalization-group scale are also different structures until a comparison law relates them.

### Unit scale and conformal scale are different torsors

Two \(\mathbb R_+\)-actions must be kept distinct. Physical dimensions can be represented by one-dimensional quantity lines \(\mathcal U_L,\mathcal U_T,\mathcal U_E,\mathcal U_M\), with

$$
\mathcal U_E
\cong
\mathcal U_M\otimes\mathcal U_L^2\otimes\mathcal U_T^{-2}.
$$

A choice of metre, second, joule, or kilogram is a basis choice in the corresponding line. In this quantity calculus,

$$
c\in\mathcal U_L\otimes\mathcal U_T^{-1},
\qquad
\hbar\in\mathcal U_E\otimes\mathcal U_T,
$$

so \(c:\mathcal U_T\to\mathcal U_L\) and \(\hbar:\mathcal U_T^{-1}\to\mathcal U_E\) are unit-line conversion isomorphisms. They compare temporal, spatial, frequency, and energetic measures; they do not themselves construct a causal cone or a dynamics.

For an already given positive mass \(m\in\mathcal U_M\), these maps give

$$
\boxed{
\mu_m
:=
\frac{mc}{\hbar}
\in\mathcal U_L^{-1},
\qquad
\lambda_C(m)=\mu_m^{-1}
\in\mathcal U_L.}
\tag{S1a}
$$

Thus it is the **inverse-Compton representative** of mass, after comparison by \(c\) and \(\hbar\), that is dual to length. The statement is undefined at \(m=0\).

Conformal weight is a separate grading. Let \(\pi:\mathsf{Sc}_{\mathrm{conf}}\to M\) be a principal \(\mathbb R_+\)-bundle whose fibers are torsors of conformal scales, and fix the quotient convention

$$
\mathcal E_{\mathrm{conf}}[w]
:=
(\mathsf{Sc}_{\mathrm{conf}}\times\mathbb R)/{\sim},
\qquad
(u,q)\sim(u\lambda,\lambda^{-w}q).
$$

Then

$$
\mathcal E_{\mathrm{conf}}[w]
\otimes
\mathcal E_{\mathrm{conf}}[v]
\cong
\mathcal E_{\mathrm{conf}}[w+v],
$$

and a positive \(\sigma\in\Gamma(\mathcal E_{\mathrm{conf}}[1])\) selects a metric representative. Conformal weight zero does not by itself mean physically dimensionless, and changing a unit basis is not the same operation as changing a physical conformal scale.

[[library/an-introduction-to-conformal-geometry-and-tractor-calculus/inq|Curry and Gover]] supply the conformal-density and scale calculus used here.

To turn a metrological length into a conformal scale requires an additional comparison, for example

$$
\iota:
M\times\mathcal U_L
\longrightarrow
\mathcal E_{\mathrm{conf}}[1].
\tag{S1b}
$$

Given \(\iota\), a nowhere-vanishing inverse-length field can define a conformal scale through its reciprocal. Without \(\iota\), the dimensional identity \(mc/\hbar\in\mathcal U_L^{-1}\) does not make a Poincare mass parameter into a spacetime field or choose a metric representative. In particular, the spectral threshold of a translation representation and a Weyl compensator are different objects until a realization theorem relates them.

The gravitational constants give the nonzero area quantity

$$
\ell_P^2
:=
\frac{\hbar G}{c^3}
\in\mathcal U_L^2.
$$

Multiplication is therefore the exact quantity-line isomorphism

$$
\boxed{
\mathcal U_L^{-1}
\xrightarrow{\ \ell_P^2\ }
\mathcal U_L,
\qquad
\mu_m
\longmapsto
\ell_P^2\mu_m
=
\frac{Gm}{c^2}
=
\ell_G(m).}
\tag{S1c}
$$

This is the defensible algebraic kernel of “mass lies between \(G\) and \(c\)”: multiplication by the Planck-area quantity maps the inverse-Compton representative of an already given mass to its gravitational length. It is a factorization among typed quantity lines, not a mechanism generating mass or an identification of mass with space or gravity.

### A gap obstructs exact same-carrier dilation covariance

Independently of either scale torsor, suppose \(s\mapsto V_s\) is a strongly continuous unitary representation on one Hilbert carrier, \(A\geq0\) is self-adjoint, and

$$
V_sAV_s^*
=
e^{-s}A
\qquad
\text{for every }s\in\mathbb R.
\tag{D}
$$

Here (D) is equality of self-adjoint operators, including \(V_sD(A)=D(A)\). Strong continuity is needed to speak of a dilation generator, although the spectral argument itself uses only unitary equivalence.

Unitary equivalence and spectral calculus imply

$$
\sigma(A)
=
e^{-s}\sigma(A).
$$

If \(A\neq0\), choose \(\lambda>0\) in its spectrum. Its dilation orbit \(\{e^{-s}\lambda:s\in\mathbb R\}\) is all of \((0,\infty)\); closedness of the spectrum adds \(0\). Hence

$$
\boxed{
A=0
\quad\text{or}\quad
\sigma(A)=[0,\infty).}
\tag{D0}
$$

Thus, when \(A\neq0\), zero cannot be separated by a positive interval from the nonzero spectral support of that **same operator on that same carrier**. The \(A=0\) branch is spectrally trivial and cannot describe nontrivial Yang--Mills translations. Changing the basis of the unit lines, or the trivialization used to present one fixed abstract conformal scale, does not evade the theorem. A genuine gap requires (D) to fail, passage to a different GNS carrier with its induced operator, or identification of the physical Hamiltonian with a different operator. Merely changing a state inside the same representation does not change \(\sigma(A)\).

Taking \(A=H\) gives the clean energy-gap obstruction and is the general spectral skeleton of [[the-grain-of-causal-scale/causal-spectrum|the HSMI no-gap theorem]]. In renormalized four-dimensional pure Yang--Mills, the nonzero beta function produces a flat-space trace or dilatation anomaly, so a fixed quantum theory is not expected to satisfy (D). The running coupling at a reference scale is traded for a scheme-labelled RG-invariant parameter \(\Lambda_{\mathrm{YM}}^{(\mathsf s)}\), taken here in an energy-valued convention. An inverse-length convention requires the factor \(\hbar c\). This still does not prove a gap: one must establish

$$
\Delta_E
=
\kappa_{\mathsf s}\Lambda_{\mathrm{YM}}^{(\mathsf s)},
\qquad
\kappa_{\mathsf s}>0,
$$

with the scheme dependence cancelling in the physical product. RG evolution is not itself a same-carrier unitary dilation group, and neither the anomaly nor asymptotic freedom proves \(\kappa_{\mathsf s}>0\).

### A fixed member may be gapped while the family is scale covariant

The preceding no-gap lemma applies to one operator on one Hilbert carrier. It does not forbid covariance of a *family* of theories carrying different nonzero scale parameters. Let

$$
\mathfrak T_\Lambda
=
(\mathfrak A_\Lambda,\omega_\Lambda,U_\Lambda),
\qquad
\Lambda>0,
$$

denote a putative one-scale family, with \(\Lambda\) energy-valued and the unit basis suppressed. If enlarging lengths by \(e^s\) induces comparison isomorphisms

$$
\mathfrak D_s^\Lambda:
\mathfrak T_\Lambda
\longrightarrow
\mathfrak T_{e^{-s}\Lambda},
\qquad
\mathfrak D_s^{e^{-t}\Lambda}
\circ
\mathfrak D_t^\Lambda
=
\mathfrak D_{s+t}^\Lambda,
\tag{D1}
$$

after the domains and identifications have been made precise, then (D1) relates *different members*. It is not the forbidden internal relation \(V_sH_\Lambda V_s^*=e^{-s}H_\Lambda\) on one fixed carrier. A fixed member with \(\Lambda>0\) can therefore be gapped even while the unpointed family is covariant under changes of scale.

Suppose the comparison maps also transport the physical translation spectrum. Homogeneity then requires

$$
\Delta_E(e^{-s}\Lambda)
=
e^{-s}\Delta_E(\Lambda).
\tag{D2}
$$

For a genuinely one-scale family this gives

$$
\boxed{
\Delta_E(\Lambda)
=
\kappa\Lambda,}
\tag{D3}
$$

where \(\kappa\) is dimensionless. Equation (D3) separates two questions that are often blurred. Family covariance explains why any gap, if present, scales linearly with the sole yardstick. It does not prove \(\kappa>0\). That strict inequality is precisely the infrared coercivity theorem still owed.

There is a torsor-like metrological aspect. Before one member is calibrated against another physical sector, the family has relative scale ratios but no preferred numerical origin or unit. A renormalization-scheme change

$$
\Lambda_{\mathsf s'}
=
C_{\mathsf s'\mathsf s}\Lambda_{\mathsf s}
$$

must be accompanied by

$$
\kappa_{\mathsf s'}
=
C_{\mathsf s'\mathsf s}^{-1}\kappa_{\mathsf s}
$$

so that \(\Delta_E\) is unchanged. Pointing this scale torsor expresses the answer in MeV; it is not what makes the ratio positive. [[register-audit]] uses this member--family distinction to locate the remaining Clay problem in the ultraviolet-to-infrared trajectory rather than in a contradiction between classical scale covariance and observed mass.

### Gravitational and reduced-Compton presentations

Gravity adds a second conversion. For a mass \(m\), define the gravitational length without the conventional Schwarzschild factor \(2\),

$$
\ell_G(m):=\frac{Gm}{c^2}.
\tag{S2}
$$

Conversely,

$$
m=\frac{c^2}{G}\,\ell_G.
\tag{S3}
$$

Thus \(G/c^2\) converts mass into a gravitational length, while \(c^2/G\) is a mass-per-length modulus. In the Einstein equation,

$$
G_{ab}+\Lambda g_{ab}
=
\frac{8\pi G}{c^4}T_{ab},
\tag{S4}
$$

the coefficient \(8\pi G/c^4\) converts stress--energy into curvature. It is useful, but interpretive, to call this a geometric **compliance**; the Einstein--Hilbert coefficient \(c^3/(16\pi G)\), with its convention-dependent normalization, supplies the reciprocal stiffness language at the action level. Hence larger \(G\) means stronger curvature response in the field equation and a smaller action coefficient. The constant \(G\) is not itself the amplitude of a scalar scale field. [[deriving-value-of-g/inq|Deriving the value of \(G\)]] develops the stiffness interpretation.

For \(m>0\), the reduced Compton wavelength is

$$
\lambda_C(m):=\frac{\hbar}{mc}.
\tag{S5}
$$

The two length presentations obey the exact identities

$$
\boxed{
\ell_G(m)\lambda_C(m)
=
\frac{\hbar G}{c^3}
=
\ell_P^2,}
\tag{S6}
$$

$$
\boxed{
\frac{\ell_G(m)}{\lambda_C(m)}
=
\frac{Gm^2}{\hbar c}
=
\alpha_G(m).}
\tag{S7}
$$

The same two maps define an exact involution on the positive mass line. With

$$
m_P:=\sqrt{\frac{\hbar c}{G}},
\qquad
\mathcal D(m):=\frac{m_P^2}{m},
$$

one has

$$
\mathcal D^2=1,
\qquad
\ell_G(\mathcal Dm)=\lambda_C(m),
\qquad
\lambda_C(\mathcal Dm)=\ell_G(m).
\tag{S7a}
$$

Its fixed point is the Planck mass, where the two length presentations coincide. This is a duality of dimensional presentations on \(m>0\), not a dynamical duality and not a prediction that any Yang--Mills excitation has Planck mass.

The mass is an input to both conversions: increasing \(m\) enlarges its gravitational length and contracts its reduced Compton wavelength, while their product is fixed by \(\hbar,G,c\). The latter is a characteristic relativistic quantum wavelength, not a theorem imposing a universal localization bound on every interacting, composite, or unstable excitation. [[deriving-value-of-g/capacity-identities|Capacity, compactness, and gravitational strength]] owns these identities and their information-capacity interpretation.

There is also a clean conceptual chain:

$$
\boxed{
(H,\mathbf P;\eta_\sigma)
\xrightarrow{\text{Casimir norm}}
M
\xrightarrow{\,G/c^2\,}
\text{gravitational length }\ell_G.}
\tag{S8}
$$

The first arrow combines clock and spatial translation generators into their Lorentz-invariant norm. Only at rest does it reduce to \(M=H/c^2\). For any witness \(m_*>0\) in \((\mathrm{MG})\), Lorentz covariance and the spectrum condition give \(\Delta_E\geq m_*c^2\). Equality holds when both are defined as the optimal lower thresholds of the nonvacuum joint spectrum and the positive Hamiltonian spectrum. The second arrow interprets an already obtained mass as a gravitational length. Neither arrow derives the threshold. Equations \((S2)\)--\((S7)\) reuse \(G\) and \(m\); they expose structure but cannot explain either numerical value.

This yields a decisive Yang--Mills firewall. The Clay pure Yang--Mills theory on Minkowski spacetime contains no dynamical \(G\); the requested gap belongs to that \(G\)-free theory. Any proposed embedding in a larger gravitational theory must therefore supply either an exact decoupled pure-Yang--Mills subtheory or observable net with the required carrier and dynamics, or a controlled limit

$$
G\longrightarrow0
$$

with its renormalized gauge scale held fixed and

$$
\alpha_G(m_{\mathrm{YM}})
=
\frac{Gm_{\mathrm{YM}}^2}{\hbar c}
\longrightarrow0.
$$

Such a limit must recover the pure Yang--Mills vacuum representation, its translation generator and spectrum condition, its gauge-invariant local net or a reconstruction-complete set of correlation functions, its gauge identities, and its renormalized scale. The background curvature must also disappear in Yang--Mills units, for example through \(|R|\lambda_{\mathrm{YM}}^2\to0\) and \(|\Lambda_{\mathrm{cosmo}}|\lambda_{\mathrm{YM}}^2\to0\). The full gravity-plus-matter Hamiltonian normally remains gapless because of arbitrarily soft gravitons even when \(\alpha_G(m_{\mathrm{YM}})\to0\); the desired gap must therefore be proved on the recovered pure-gauge carrier, not on the full gravitational Hilbert space. Neither \(\ell_G\to0\) nor convergence of a few correlators is a recovery theorem. Thus \(G\) may translate a previously derived Yang--Mills gap into gravitational geometry, or fix an external unit convention in a larger theory, but it cannot be an indispensable premise of a proof of the Clay pure-gauge gap unless the larger construction also proves the required gravity-decoupling and scale-matching theorem.

The observable content of any claim that \(G,\hbar,c\), or a cosmic scale varies lies in dimensionless ratios such as \(\alpha_G(m)\), \(mc^2/\Lambda_{\mathrm{YM}}^{(E)}\) when \(\Lambda_{\mathrm{YM}}^{(E)}\) denotes an energy scale, or a clock-rate ratio. A simultaneous change of all dimensional yardsticks can be a change of units. A physical evolving-scale theory must specify the dynamical field or section, the reference standards, and a dimensionless prediction.

The strongest live interpretation is consequently not “mass is caused by \(G\).” It is:

> Mass is a dimensionful Poincare invariant whose numerical value requires metric and unit calibration. The constant \(c\) compares clock and spatial measures, \(G\) converts stress--energy into geometric response, and \(\hbar\) converts generator scale into quantum phase and reduced Compton wavelength. A deeper theory must construct the physical comparison maps and show why their dimensionless relations are fixed.

## The Yang--Mills theorem target after the reversal

The representation-theoretic retyping changes the research question from

> What local field gives a mass to a massless gluon?

to

> Why does the physical gauge-invariant vacuum representation of translations have an isolated vacuum and no nonvacuum support adjacent to it?

That is a real improvement. It removes the gauge-potential mass-term category error while leaving the Clay problem intact. The official target still requires construction of the nontrivial continuum theory and a positive gap; [[puzzle-as-posed]] states it precisely.

A pre-QFT or boundary-first programme would make a genuine contribution by constructing, without using the desired spectrum:

1. a physical carrier, Poincare action, and joint spectrum condition recovered from the proposed prelocal geometry;
2. its gauge-invariant vacuum state and complete vacuum projection \(P_0\);
3. a canonical decomposition or joint spectral measure for the reconstructed translations;
4. a normalized dimensionless response form with a uniform positive lower bound on every nonvacuum physical direction;
5. a noncircular same-carrier comparison with the Hamiltonian form; and
6. an independent dimensional scale that survives regulator and infinite-volume limits.

The conditional analytic core is already explicit. Let \(H\geq0\) be self-adjoint with closed quadratic form

$$
h[\Psi]=\|H^{1/2}\Psi\|^2,
\qquad
D(h)=D(H^{1/2}),
$$

and let \(\mathfrak d\) be a closed positive dimensionless form on the same physical carrier with \(D(h)\subseteq D(\mathfrak d)\). If, for every \(\Psi\in D(h)\),

$$
\mathfrak d[\Psi]
\geq
\kappa\|(1-P_0)\Psi\|^2,
\qquad
h[\Psi]
\geq
\eta_{\mathrm{sol}}E_*\mathfrak d[\Psi],
$$

with \(\kappa>0\), \(\eta_{\mathrm{sol}}>0\), and \(E_*>0\), then

$$
H\geq
\eta_{\mathrm{sol}}\kappa E_*(1-P_0).
$$

The conclusion is an operator inequality in quadratic-form sense.

[[causal-frame-coercivity]] provides the family-valued version, and [[causal-patch-boundary-and-two-times]] proves why the operator that forms or forgets the observable carrier cannot itself be the tangential response form that gaps excitations within that carrier.

The Casimir insight adds the spectral stopping condition. After Poincare recovery, the same theorem must imply

$$
\operatorname{sp}(P)
\subseteq
\{0\}
\cup
\{p\in\overline V_+:p^2\geq m_*^2c^2\}.
$$

This is where a dimensionless internal Casimir, knot invariant, index, boundary response, or entropy Hessian could enter: as part of the proof of \(\kappa>0\), not as the mass itself. The independent yardstick supplies units. The Poincare reconstruction identifies the resulting energy threshold as mass. Every arrow has a different job.

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
