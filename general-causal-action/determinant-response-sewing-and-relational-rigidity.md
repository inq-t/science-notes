# Determinant–Response Sewing and Relational Rigidity

One elimination can return both the weight of a configuration and its complete boundary response. For Gaussian auxiliary variables these outputs are a determinant and a Schur complement; their joint sewing is exact. When the retained variables describe how frames are related, the determinant generates interactions around cycles. The research proposal is to constrain this entire construction by one multiplication law, then seek mass and cosmic geometry as different readouts of its response.

**Status: exact finite elimination and cycle identities; three conjectures about primitive selection, physical rigidity, and a common cosmological response.** The determinant mechanism is established mathematics. The proposed gain would be a law selecting its inputs and physical realization together.

## One operation returns weight and response

Let \(Q>0\) be a finite Hermitian matrix on retained and interior complex variables \(v=(v_\partial,v_I)\). Completing the square gives

\[
\int e^{-v^*Qv}\prod_{j\in I}\frac{d^2v_j}{\pi}
=\frac{\exp[-v_\partial^*Q_{\partial|I}v_\partial]}
{\det Q_{II}},
\qquad
Q_{\partial|I}
=Q_{\partial\partial}-Q_{\partial I}Q_{II}^{-1}Q_{I\partial}.
\tag{DS1}
\]

For \(\nu\in\mathbb N_{>0}\) independent copies, the normalization is \((\det Q_{II})^{-\nu}\), with one retained quadratic form per copy. Define the joint datum

\[
\boxed{\mathfrak S_I(Q)
=\big((\det Q_{II})^{-\nu},\,Q_{\partial|I}\big).}
\tag{DS2}
\]

On a pair \((w,Q)\), elimination multiplies \(w\) by the determinant factor. For disjoint interior sets, successive elimination equals elimination of their union: the Schur complements associate, and their determinant factors multiply. This follows directly from (DS1) and Fubini. It is an equality of full retained amplitudes, including their normalization.

[[spectral-wall-descent/response-determinant|Response and determinant from one hidden operator]] already owns this two-output mechanism and its effective-action interpretation. The present proposal asks which algebraic presentation identities constrain its admissible inputs.

The two outputs have different jobs. The determinant changes the relative weights of retained configurations. The Schur complement preserves how arbitrary boundary data respond. Retaining only a normalized scalar density loses the latter; retaining only a quadratic form loses the former. With a spectral parameter, retain \(Q_{\partial|I}(z)\) at every admissible \(z\), not just its value at zero. [[coarse-response-memory/inq|Coarse response memory]] owns the resulting dynamical Schur formula.

This construction permits non-Gaussian retained laws in linear coordinates even though the eliminated variables are Gaussian: \(Q\) may depend nonlinearly on the retained variables. On compact frame groups, the invariant statement is that the induced Haar-relative law can be nonconstant. Neither setting falls under [[gaussian-sewing-rigidity|the constant-metric Gaussian sewing theorem]]. Integer \(\nu\) has an explicit Gaussian realization. Any real power of a positive determinant is a positive scalar weight; positive-definiteness of a proposed overlap kernel is a further requirement, as in [[algebra/determinant-preparation-positivity-and-the-rank-threshold|determinant preparation positivity]].

## Closed comparisons induce a cycle action

Here is a concrete member, with its inputs exposed. Supply a finite simple graph, a compact group \(G\), a unitary representation \(\rho:G\to U(d_\rho)\), and symmetric nonnegative edge weights \(w_{xy}\). Require the scalar weighted adjacency \(P_0=(w_{xy})\) to have norm at most one. Supply edge frames \(U_{yx}=U_{xy}^{-1}\), and set

\[
(P_Uf)_x=\sum_y w_{xy}\rho(U_{xy})f_y,
\qquad P_{\mathbf1}=P_0\otimes I_{d_\rho},
\qquad Q_U=I-rP_U,\quad 0<r<1.
\tag{DS3}
\]

Pointwise domination by \(P_0\) proves \(\|P_U\|\le1\); \(P_U\) is self-adjoint, hence \(Q_U>0\). Integrating \(\nu\) complex Gaussian frame fields gives \((\det Q_U)^{-\nu}\). Relative to identity transport, its induced action is

\[
\boxed{
S_{\circlearrowleft}(U)
=\nu\log\frac{\det(I-rP_U)}{\det(I-rP_{\mathbf1})}
=\nu\sum_{n\ge1}\frac{r^n}{n}
\left[\operatorname{Tr}P_{\mathbf1}^{\,n}
-\operatorname{Tr}P_U^{\,n}\right].
}
\tag{DS4}
\]

The series converges absolutely in finite dimension. Expanding the trace over rooted closed walks \(\gamma\), and pairing each walk with its reverse, writes each bracket as

\[
\sum_{\substack{\gamma\ \mathrm{closed}\\|\gamma|=n}}
w_\gamma\left[d_\rho-\operatorname{Re}\chi_\rho(U_\gamma)\right]
\ge0,\qquad
w_\gamma=\prod_{e\in\gamma}w_e.
\tag{DS5}
\]

Walks reducible entirely by immediate backtracking contribute zero. On a square lattice with no shorter cycles, the first nonconstant terms are plaquette holonomies at length four. Longer cycles occur automatically with coefficients \(r^n/n\) and their edge-weight products. Thus a sum over relational cycles arises from elimination; a separate plaquette potential was not needed for this finite member.

More precisely, on a finite open hypercubic lattice,

\[
S_{\circlearrowleft}(U)
=2\nu r^4\sum_p\left(\prod_{e\in p}w_e\right)
\left[d_\rho-\operatorname{Re}\chi_\rho(U_p)\right]+O(r^6).
\tag{DS5a}
\]

The coefficient counts four starting vertices and two orientations per plaquette. The remainder is a finite-graph small-\(r\) statement, not a volume-uniform continuum estimate.

With normalized Haar measure on each edge,

\[
d\mu(U)=Z^{-1}e^{-S_{\circlearrowleft}(U)}
\prod_e dU_e
\tag{DS6}
\]

is a continuous, strictly positive finite probability law. It is nonconstant when the graph and representation detect a holonomy. On a tree it is constant; after gauge fixing a single loop, its entire content may reduce to one holonomy variable. A nonconstant cycle weight is not already interacting four-dimensional Yang–Mills.

Under \(U_{xy}\mapsto g_xU_{xy}g_y^{-1}\), \(P_U\) changes by block-unitary conjugation. Both the determinant and the full boundary response transform compatibly. This is an exact symmetry of the supplied graph construction. It does not yet explain the group or why its frames should be the retained variables.

[[library/induced-qcd-at-large-n/inq|Kazakov and Migdal's induced gauge theory]] is a precedent for obtaining gauge interactions by eliminating auxiliary matter. Their adjoint-scalar, large-\(N\) model is not a theorem about (DS3), nor a completed solution for all compact simple groups. [[holonomy-state-refinement/overlap-kernels-and-face-refinement|Overlap kernels and face refinement]] already retains full exposed boundary amplitudes and normalization under associative integration. Equations (DS1)–(DS2) specialize that mechanism to explicit Gaussian elimination. The new proposal is to constrain the elementary amplitudes by algebraic presentation identities, with the unit test below giving a first finite selection result.

## Conjecture 1: multiplication selects the sewing grammar

Let \(V\) be a finite-dimensional unital algebra with multiplication \(\mu:V\otimes V\to V\) and a declared positive Hermitian pairing \(h\). Consider the discrepancy operator

\[
\partial_\mu=[\,I,-\mu\,],
\qquad
\mathbb Q_\mu(z)=zI+\partial_\mu^\dagger\partial_\mu,
\quad z>0.
\tag{DS7}
\]

Here \(\partial_\mu:V\oplus(V\otimes V)\to V\), while \(\mathbb Q_\mu(z)\) acts on the direct sum; the adjoint uses \(h\) and its tensor pairing. This is a possible elementary comparison, not a derived physical Hamiltonian. Its positive symmetry group is

\[
G_{\mu,h}
=\{u\in GL(V):u\mu=\mu(u\otimes u),\ u1=1,\ u^*hu=h\}.
\tag{DS8}
\]

The multiplication generally loses distinctions, whereas these invertible symmetries preserve it. This supplies a precise sense in which a directed operation admits symmetry as a stabilizer. Noninvertibility alone supplies neither temporal orientation nor the desired compact simple group.

The elementary cell already makes one useful distinction exact. Unitality makes \(\mu\) surjective. For \(n=\dim V\), its compatibility kernel has dimension \(n^2\):

\[
\ker\partial_\mu=\{(\mu w,w):w\in V\otimes V\}.
\]

Eliminating the tensor factor of \(\mathbb Q_\mu(z)\) gives

\[
\mathscr F_\mu(z)
=z\left[I+(zI+\mu\mu^\dagger)^{-1}\right],
\qquad
\mathscr F_\mu(0)=0,
\qquad
\mathscr F_\mu'(0)=I+(\mu\mu^\dagger)^{-1}.
\tag{DS8a}
\]

This follows from \(\mu(zI+\mu^\dagger\mu)^{-1}\mu^\dagger
=\mu\mu^\dagger(zI+\mu\mu^\dagger)^{-1}\).
Its determinant factor is
\([z^{n^2-n}\det(zI+\mu\mu^\dagger)]^{-\nu}\) for \(z>0\).
Thus one multiplication cell supplies a metric seed but no retained static stiffness. The hidden kernel \(\ker\mu\) decouples from \(V\); a zero-frequency inverse of \(\mu^\dagger\mu\) must be restricted to \(\operatorname{ran}\mu^\dagger\). Removing that kernel from a normalized response does not silently remove its determinant factor. Whether sewn cycles supply stiffness is the next substantive question.

**Conjecture 1.** A restricted class of oriented words in one elementary comparison, with specified unit and composition relations, admits a positive boundary evaluation whose joint elimination determines the state and full response without independently appended potentials, clocks or memory functions.

The substantive restriction must be on the admissible words and pairings: an unrestricted tensor can encode the desired operator. The missing map from \(\mu\) to the incidences and frame fields in (DS3) is part of this conjecture. [[directed-analytic-realization/preparation-overlaps-and-the-transition-algebra|Preparation overlaps]] supplies the positive carrier construction once a suitable evaluation exists; it does not select that evaluation.

A necessary first distinction is between an identity insertion and a real subdivision with positive duration. A pure presentation unit should satisfy

\[
\mathcal Z_{w\circ 1}(z)=\mathcal Z_w(z)
\quad\text{for all admissible }z.
\tag{DS9}
\]

Naively adding a copy of (DS7) need not do so. Already the right-unit comparison \(v-w\), with a term \(z(\|v\|^2+\|w\|^2)\), has interior elimination

\[
\left((z+1)^{-\nu\dim V},
\ \frac{z(z+2)}{z+1}I\right),
\tag{DS10}
\]

instead of the uninserted boundary datum \((1,zI)\). Even dividing out a scalar normalization does not repair the boundary response.

[[transparent-units-and-hidden-determinants|Joint unit transparency]] now supplies a finite selection theorem. With a fixed Gaussian integration measure, among positive semidefinite response metrics \(\Gamma\), the pencil

\[
Q_\Gamma(z)=z\Gamma+
\begin{pmatrix}I&-I\\-I&I\end{pmatrix}
\]

has both Schur response \(zI\) and a \(z\)-independent unit normalization precisely when \(\Gamma=\operatorname{diag}(I,0)\). The inserted variable is then an algebraic auxiliary with no independent clock weight. This insertion remains transparent in every positive boundary context, including finite forests of such leaves.

The determinant condition does real work. Already for scalars,
\(\Gamma_c=\left(\begin{smallmatrix}1+c&-c\\-c&c\end{smallmatrix}\right)\), \(c\ge0\), preserves the entire Schur response \(z\), while its hidden determinant is \(1+cz\). For \(c>0\), it hides a relative mode of rate \(1/c\). Extending this unit law to genuine multiplication requires a rule distinguishing presentation auxiliaries from physical distinctions.

[[multiplication-reassociation-and-the-process-metric|The reassociation test]] now separates two results. Giving each intermediate tensor a positive clock norm fails for every nontrivial finite unital algebra. Giving clock weight only to the endpoints returns a positive amplitude independent of every sequential reduction order, with iterated multiplication and its covariance sum retained. But an integrated identity leaf is not an identity transition: finite Gaussian noise accumulates along a wire. The latter requires zero innovation, or a whole-diagram correlation that cancels it. A single common Gaussian state for both unit presentations is also obstructed under the stated positive-noise hypotheses.

[[marked-gaussian-constraints-and-sewing-measures|Marked constrained amplitudes]] supply the full alternative for a joint Gaussian preparation: conditioning, coarsening and sequential independent constraints preserve all sources and normalization when their measure factors are retained. This includes a scalar from hidden sources, and distinguishes the volume of a relation surface from the measure of an identity's integration fiber.

Coherence still does not select the preparation. [[whole-multiplication-preparations-and-state-shape|The whole-diagram witness]] fixes multiplication on \(\mathbb C\oplus\mathbb C\), its pairing, both unit returns, both parenthesizations and the unmarked normalization, while varying a dimensionless output response. Conjecture 1 therefore needs a constitutive state rule beyond those identities. It may posit such a rule; it need not derive every axiom from no assumptions.

[[multiplication-sensitive-cycle-preparations|The commutator preparation]] gives a positive candidate: one joint law for an algebra element and retained unitary frames returns both a frame interaction and its conditional state. Its covariance rule uses the sum of squared multiplication commutators. It distinguishes tracial \(M_2(\mathbb C)\) from uniform-trace \(\mathbb C^4\), although their multiplication squares coincide. The particular covariance function and frame prior are declared inputs, and a commutator comparison is not yet a derived graph cycle.

Its [[commutator-preparation-transfer-and-marked-gluing|Gram transfer]] now gives an exact path and source law: each ordinary transfer edge has a separate preparation, and integrating the middle frame creates a positive covariance between quadratic edge observables. Reusing one preparation along the whole path changes the law. The [[commutator-overlap-nullspace-and-angular-coverage|complete angular audit]] also identifies a structural failure: the feature quotient retains all radial and even-axis channels but loses central and inversion information, and multiplication does not descend to it.

[[relative-multiplication-transfer-and-the-rotor-limit|Comparing relative left multiplications]] repairs that loss with an injective \(SU(2)\) transfer on all representation sectors. [[preparation-compression-and-the-returned-potential|The normalized compression law]] combines this comparison with the conditional preparations. Its product limit returns both a definite potential, the trace of their preparation metric, and a vacuum on the full frame carrier. This is a constructive state-and-dynamics example with declared comparison rules; the separate preparation roles can next be tested against the more economical single-preparation determinant.

## Active candidate: conditional boundary exchange

The selected experiment fixes a constitutive processing rule for the joint determinant preparation. Its fixed-duration uniform-rigidity claim has failed the copy-refinement test below; the complete preparation and conditional comparisons remain well-defined. At each admitted finite diagram, retain the full joint law before Gaussian elimination:
\[
d\widehat\mu_D(U,\xi)=\widehat Z_D^{-1}
\exp\!\left[-\sum_{a=1}^{\nu}(\xi^{(a)})^*Q_U\xi^{(a)}\right]
\prod_e dU_e\prod_{a,v}\frac{d^{2d_\rho}\xi_v^{(a)}}{\pi^{d_\rho}},
\qquad Q_U=I-rP_U>0.
\tag{DS10a}
\]
This is the same family as (DS3)–(DS6). Its frame marginal is \(\mu_D\propto(\det Q_U)^{-\nu}\prod_e dU_e\). The graph or four-dimensional realization sector, faithful representation, admissible \(r\), multiplicity and invariant pairings remain declared family data. The rule does not claim to derive them from no premises.

For an admitted cut \(p\), let \(\eta_p\) be its actual retained boundary/outside readout together with the auxiliary preparation data kept by that cut. Define
\[
C_pf=\mathbb E_{\widehat\mu_D}[f(U)\mid\eta_p],\qquad
T_p=C_p^*C_p,\qquad
R_D^{\rm cmp}=\sum_{p\in\mathcal P_D}(I-T_p).
\tag{DS10b}
\]
The adjoint uses the two marginals of this one joint law. Thus \(T_p\) is the transition obtained by reading \(\eta_p\) conditional on the incoming frame and then drawing the outgoing frame conditional on that same readout. Each distinct physical cut occurrence has one equal weight; a common duration calibration remains free before the additional rule below. Pure presentation subdivisions transport the old comparison history and do not create new cut occurrences. This last admissibility rule must be tested, not inferred from the drawing of a diagram.

At a fixed finite diagram, each \(T_p\) is a positive self-adjoint Markov contraction on \(L^2(\mu_D)\). The selected comparison clock is \(e^{-tR_D^{\rm cmp}}\), and
\[
\langle f,(I-T_p)f\rangle_{\mu_D}
=\mathbb E_{\widehat\mu_D}\operatorname{Var}(f(U)\mid\eta_p).
\tag{DS10c}
\]
This is the exact joint consequence of the proposed rule: the determinant state, conditional comparisons and relative cut rates cannot be retuned independently while retaining (DS10a)–(DS10b). The conditional-exchange protocol is an explicit new constitutive commitment, not a theorem forced by positivity. The clock is bounded at each finite diagram; its four-dimensional ultraviolet return is a further conjecture.

The operation can act on physical distinctions rather than gauge transformations. Suppose a neutral Wilson character is nonconstant on the resampled conditional fiber for a positive-measure set of retained data, and the conditional frame law has full support there. Its variance in (DS10c) is then strictly positive, so \(T_p\) changes it. Mere occurrence of a link in the word is insufficient: a character is unchanged by conjugating its entire argument. This is a nonzero-action test, not a uniform lower bound. The retained variables, gauge action and actual source must be specified in each application; freezing the entire loop would give zero variance.

**Exact sourced consequence.** [[conditional-exchange-through-cuts-and-retained-marks|EC1–18]] computes the actual link exchange, including a mixed neutral source on two adjacent \(SU(2)\) cells. Elimination preserves the complete marked law when the induced memory is retained. Projecting an exchange and then repeating that projected exchange instead produces a positive leakage term. Deleting auxiliary information also changes the comparison by an explicit positive defect. These results permit inherited memory; they do not require autonomous Markov closure under every spatial projection or assert that different update orders commute.

**Rejected uniform clock claim.** On a fixed open hypercubic graph, take the admitted many-copy Wilson path \(r_\nu\to0\), \(2\nu r_\nu^4w^4\to b>0\), where \(w=1/(2D)\). [[auxiliary-copy-refinement-and-the-exchange-clock|AC12–17]] proves that the complete comparison kernel consists only of constants, while a normalized neutral plaquette source has response \(O(r_\nu^2)\). Its actual joint-boundary recovery defect also tends to zero at fixed exchange duration. The limiting frame law is a nontrivial Wilson law. Thus (DS10b) has no fixed positive rigidity constant along this path in its unaccelerated units. An acceleration at least of order \(\nu r_\nu^2\) is necessary to avoid this particular obstruction, and is not sufficient for a gap.

The proposed finite-word relation that a completed cut tour absorbs its own repetition has also failed. [[cut-tour-absorption-and-the-injective-exchange|CT1–8]] constructs a uniformly bounded repair under that precise relation. CT10–11 then proves that faithful full-auxiliary exchanges with enough copies are injective, so a nontrivial finite tour cannot be idempotent. A change of duration cannot repair this algebraic failure. Other certificates remain possible, subject to the [[global-local-response-reconstruction/quantitative-descent-and-the-shape-of-a-gap|neutral sharpening]] and [[commutator-word-comparisons-and-neutral-soft-escape|flat-configuration]] controls.

**Active revised conjecture: duration from the preparation score.** Retain the joint law, full auxiliary readout and equal relative raw-link rates. On the homogeneous finite graph family, let \(d_G=\dim G>0\), use the declared tangent pairing \(Q_\rho(X,Y)=-\operatorname{Re}\operatorname{Tr}[d\rho(X)d\rho(Y)]\), and let \(\mathcal I_e(U)\) be the Fisher form of the actual conditional auxiliary law, as computed in AC18. Postulate one common duration by
\[
a_D=\frac{1}{d_G|E|}
\sum_{e\in E}\mathbb E_{\mu_D}
\operatorname{tr}_{Q_\rho}\mathcal I_e(U),
\qquad
\tau_D=a_D^{-1},
\qquad
\widehat R_D=a_D R_D^{\rm cmp}.
\tag{DS10d}
\]
The trace sums over a \(Q_\rho\)-orthonormal Lie-algebra basis. This is a specific new constitutive rule: one exchange takes the inverse of the mean auxiliary information per unit link tangent. It uses no measured gap, vacuum projector or separately fitted diagram rate. Its normalization uses the already declared tangent pairing; choosing information as duration is not forced by positivity, dimensional analysis or AC's necessary bound.

The rule is finite, strictly positive and gauge invariant. Indeed, \((1+r)^{-1}I\le Q_U^{-1}\le(1-r)^{-1}I\) in AC18 gives
\[
\frac{2\nu r^2w^2}{(1+r)^2}\le a_D
\le\frac{2\nu r^2w^2}{(1-r)^2}.
\]
The Fisher form transforms as a tangent tensor and \(Q_\rho\) is Ad-invariant, so its trace is unchanged by gauge presentation. Observational marks keep this reference clock fixed. A genuine variation of the constitutive preparation also differentiates \(a_D\), and hence contributes \((\partial a_D)R_D^{\rm cmp}\) to the varied generator.

The exact score calculation gives \(a_D=2\nu r^2w^2[1+O(r^2)]\), uniformly over this finite graph family with fixed \(D\). Thus the same law now fixes a duration with the necessary copy-refinement order while preserving relative cut rates. This does not establish a nonzero limiting response. A pure presentation change must transport the old cut inventory, tangent pairing and score; recomputing the mean over newly drawn dummy links would be a different rule. Genuine graph refinement and heterogeneous weights need a further test, not an automatic invariance claim.

This mean selects a global duration convention. On a disjoint union with the same group and tangent normalization,
\[
a_{D_1\sqcup D_2}
=\frac{|E_1|a_{D_1}+|E_2|a_{D_2}}{|E_1|+|E_2|}.
\]
Consequently the union's rescaled clock agrees with independently calibrated component clocks only when \(a_{D_1}=a_{D_2}\). The homogeneous copy limit has a common leading coefficient, but exact component-clock compatibility is not proved or postulated here. This is a further explicit test of the proposed duration convention.

The next decisive test is to derive the full-source limiting generator of \(\widehat R_D\) along the fixed-Wilson path, with no added mobility or potential, and determine whether it can supply the required physical clock. In particular, distinguish evolution of a complete Euclidean configuration by resampling from transfer between physical time slices, as [[sewn-transfer-clock-and-the-rotor-limit|TR]] requires. A weak-field and Abelian dispersion test should be performed on the declared carrier, using [[reciprocal-coefficients-and-the-field-gap-test|FG's propagation test]] only after that carrier is identified. If the returned clock is only an auxiliary stochastic evolution, retire its direct identification with physical time; a separate comparison theorem would then have to justify any remaining use in the rigidity programme. No such limit, identification or comparison theorem is claimed here.

## Conjecture 2: relational cycles force physical rigidity

The proposed physical clock must come from sewing actual slabs of the same positive state. If that construction returns a positive transfer \(T_\ell\), an appropriate vacuum normalization \(\lambda_0\), and a justified logarithm on its physical support, its candidate generator is

\[
H=-\ell^{-1}\log(T_\ell/\lambda_0).
\tag{DS11}
\]

Reflection positivity, the observable quotient and the meaning of \(\ell\) must be constructed. Finite-state positivity alone does not supply them. [[sewn-transfer-clock-and-the-rotor-limit|The sewn transfer rotor]] is a positive control: transfer evolution and conditional resampling of a joint law are different clocks.

**Conjecture 2.** For every compact simple gauge group \(G\) in the Clay target, a family selected by Conjecture 1 admits a nontrivial Yang–Mills return in which its relational cycles prevent arbitrarily soft neutral physical distinctions, uniformly through spatial-volume and continuum limits.

This conjecture concerns the complete vacuum sector generated by gauge-invariant observables, with the connection variables integrated in the same state. The graph, representation, \(r,\nu\), refinement rule and duration in the finite example are still inputs. Their replacement or selection is unresolved. In particular, a gap for vector sections at a fixed connection is not a gap for functions of dynamical connections; [[algebra/short-loop-holonomy-and-quantitative-gluing|short-loop quantitative gluing]] owns that carrier distinction.

The commutator candidate has a finite joint-context test: two retained frames coupled to one preparation have a response depending on their relative axes. Nonparallel noncentral frames remove the traceless common nullspace in its \(M_2\) member, while a scalar null direction always survives. Neither fact identifies a physical vacuum or supplies a translation generator. The normalized compression law now constructs a distinct full-frame generator \(D_G(-\Delta+q_\beta)\), with \(q_\beta\ge0\) returned by the preparation rule. Its first vacuum-centered gap initially decreases with comparison strength. Positive statistical cost therefore does not automatically strengthen physical rigidity; the observable carrier and complete vacuum subtraction remain essential.

Noncommutativity and a unique invariant vector do not suffice. On \(M_N(\mathbb C)\) with its Hilbert–Schmidt pairing, take clock and shift unitaries satisfying \(UV=e^{2\pi i/N}VU\). For

\[
D(X)=([U,X],[V,X]),
\qquad
\ker D=\mathbb CI,
\qquad
\operatorname{gap}(D^*D)=4\sin^2(\pi/N)\longrightarrow0.
\tag{DS12}
\]

Indeed, the basis \(U^aV^b\) diagonalizes the form with eigenvalues \(4\sin^2(\pi a/N)+4\sin^2(\pi b/N)\). A fixed-coefficient chain also admits arbitrarily long, slowly varying distinctions. The desired theorem must identify an additional rigidity that defeats these escape routes. [[global-local-response-reconstruction/quantitative-descent-and-the-shape-of-a-gap|Quantitative descent]] states the corresponding full-carrier requirement.

## Conjecture 3: cosmic normalization and local mass share a marked amplitude

In the bounded-coupling block setting of [[coarse-response-memory/inq|the memory theorem]], remove the actual vacuum and write

\[
H=\begin{pmatrix}A&B^*\\B&C\end{pmatrix}\ge0,
\qquad C\ge c_HI>0.
\]

The complete retained denominator and its first frequency derivative are

\[
\mathscr F(z)=z+A-B^*(z+C)^{-1}B,
\qquad
\boxed{\mathscr F'(0)=I+B^*C^{-2}B
=I+\int_0^\infty t\,B^*e^{-tC}B\,dt.}
\tag{DS13}
\]

The identity is exact: the induced norm remembers how long a hidden response can persist. It gives a candidate interpretation of inertia as accumulated relational response. It does not equate that norm with a mass eigenvalue.

**Conjecture 3.** The same selected amplitude determines a joint closed normalization and marked boundary response, admitting independently constructed homogeneous and local physical returns. Their transported mixed-source derivatives have a common origin. The harmonic-lift identification below is one candidate noncentral component:

\[
\mathbb G_{NN}\ \stackrel{?}{=}\ J_N^*\mathscr F'(0)J_N,
\qquad
\mathcal R_{\rm loc}(z)=J_{\rm loc}^*\mathscr F(z)^{-1}J_{\rm loc},
\quad z>0.
\tag{DS14}
\]

The first equality is a conjectured identification after transport, central resolution and unit calibration. \(J_N\) must be derived as a physical homogeneous-scale tangent, not chosen to force the equality. [[program-core/common-response-form|The common response form]] owns the independent state geometry and mixed-response test. Its BKM form is not automatically the harmonic-lift norm in (DS13). When a tangent differentiates an eliminated variable, its source insertion must also be carried through the integration; preserving an unmarked amplitude alone does not preserve every response witness.

[[closed-normalization-and-cosmic-response|Marked closed normalization]] supplies an exact finite generating identity: matrix-source derivatives of a determinant recover the complete open resolvent and its homogeneous variation. A decoupled hidden mode can contribute to the determinant while being absent from \(\mathscr F\). Conversely, unmarked eigenvalues do not determine local couplings. Even the marked identity leaves an additive scalar character on genuine diagrams possible unless the primitive law excludes it; unit transparency alone does not determine cosmic vacuum normalization.

The spectral measure of \(\mathcal R_{\rm loc}\), together with a totality theorem, could detect the physical gap after the translation and Poincaré return. A low-frequency coefficient alone cannot. For example,

\[
H_c=\begin{pmatrix}1+c&c\\c&c\end{pmatrix},\quad c>0:
\qquad \mathscr F_c(0)=1,\quad \mathscr F_c'(0)=2,
\quad \min\operatorname{spec}H_c\longrightarrow0
\quad(c\downarrow0).
\tag{DS15}
\]

Thus even identical static response and induced norm coexist with arbitrarily soft spectra. The full function \(\mathscr F_c(z)=z+1+c-c^2/(z+c)\) distinguishes them. [[coarse-response-memory/spectral-readout-and-the-visible-gap|Spectral readout]] owns the criterion using its complete support.

This is an opening for cosmology and microscopic dynamics to constrain one another through a shared operator. A dark-sector interpretation would require a constructed response and observable coupling. Soft cosmic directions visible in the required pure-gauge sector would close its gap; recovering a Yang–Mills sector from a larger parent requires an actual decoupling or sector-return theorem.

## The original hyperbolic clue has an operator home

For a nonnegative self-adjoint generator in calibrated clock units, let \(T_t=e^{-tH}\). The Cayley response satisfies

\[
\mathcal A_t=(I-T_t)(I+T_t)^{-1}
=\tanh(tH/2),
\qquad
\partial_t\mathcal A_t=\tfrac12H\,\operatorname{sech}^2(tH/2),
\quad t>0.
\tag{DS16}
\]

The derivative is a bounded operator for every positive \(t\). This is the susceptibility of a complete transfer response, consistent with [[two-slice-innovation-geometry/past-future-angle-and-the-transfer-gap|the past–future Cayley construction]] and [[quartic-overlap-sewing-tangent|the balancing tangent]]. For a spectral value \(E>0\), the inflection of its \(\operatorname{sech}^2(tE/2)\) factor occurs at \(tE/2=\operatorname{artanh}(1/\sqrt3)\).

The profile organizes response once the generator exists. The unproved content is a uniform exclusion of \(E\downarrow0\) on the required physical carrier. The proposed reversal is to seek that exclusion in the law of complete sewing, while allowing the same law to return the geometry in which the response is measured.
