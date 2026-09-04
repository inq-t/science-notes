# The Composite Realization Ledger

None of the attractive ingredients—Type III, cocycles, entropy Hessians, knots, exceptional stabilizers, or discrete wall crossing—currently acts on the complete neutral Yang--Mills vacuum carrier with a regulator-uniform positive edge. Their viable use is compositional: exceptional and topological geometry may construct the kinematic carrier, operator-algebraic descent organizes comparison and gluing, the full nonlinear whole law constructs the response operator, and Osterwalder--Schrader reconstruction identifies its edge with clock energy.

**Status: [EXACT] for the individual finite and categorical arrows cited below; [EXACT NO-GOS] for the carrier mismatches; [OPEN] for their natural composition and the uniform nonlinear response floor.**

## One admissible dependency chain

For the observed color member, [[contemporary-puzzles/yang-mills-mass-gap/octonionic-slice-groupoid-and-orientation-torsor|the octonionic quotient-stack construction]] supplies the strongest current kinematic chain:

$$
[S^6/G_2]\simeq B SU(3)
\longrightarrow
SU(3)^E/\!/SU(3)^V
\longrightarrow
\text{full nonlinear Wilson law}
\longrightarrow
K_r
\longrightarrow
\|K_rQ_r\|<1
\longrightarrow
\text{OS clock gap}.
\tag{RL1}
$$

Each arrow has a different job:

1. the quotient stack remembers the \(SU(3)\) stabilizer and its torsors;
2. graph transgression returns the lattice gauge groupoid;
3. the exceptional normal has an exact finite-regulator pullback to the Wilson color action after its fixed coefficient conversion;
4. integrating the nonlinear cylinder law defines the complete midpoint-to-boundary conditional prediction \(K_r\);
5. a strict norm bound supplies quantitative neutral-sector coercivity; and
6. reflection-positive transfer and continuum reconstruction turn that coercivity into the physical gap.

Only steps 1--3 and the finite-regulator implication in step 6 are presently exact. [[contemporary-puzzles/yang-mills-mass-gap/exceptional-normal-holonomy-and-the-residual-gauge-form|Exceptional normal holonomy]] proves the Wilson-action pullback used in step 3. Step 4 is well defined at finite regulator once the full law and boundary carrier are fixed. Step 5 is the principal missing theorem, while the four-dimensional continuum part of step 6 is the Clay existence problem.

For the Clay statement, which ranges over every compact simple \(G\), the first arrow must be replaced by a general group-indexed construction

$$
G
\longmapsto
G^E/\!/G^V
\longmapsto
\nu_{r,G}
\longmapsto
K_{r,G}.
\tag{RL2}
$$

The exceptional \(SU(3)\) branch can explain why the observed color carrier has a distinguished origin only if the required flag or pointing is itself selected. It cannot by itself prove the all-\(G\) theorem.

## Where the Type-III layer belongs

[[spectral-wall-descent/scale-correspondence-stack|The scale-correspondence prestack]] supplies a formal starting point for a pointed reflection-positive response prestack, schematically

$$
\mathfrak A:
\mathsf{Scale}
\longrightarrow
\operatorname{PSt}
\bigl(
\mathsf{Ctx},
\mathbf{W^*Corr}
\bigr).
\tag{RL3}
$$

Its objects carry algebras, faithful states or weights, reflections, translations, and declared whole-to-face maps. Its gluing arrows are correspondences with coherent relative tensor product; where actual prediction or forgetting is required, they must be supplemented by conditional expectations, operator-valued weights, instruments, or equivalent pointed CP data.

[[wall-construction-interface/core-spectral-wall|The core spectral wall]] and [[modular-cocycle-tomography/inq|modular cocycle tomography]] show what this layer can contribute:

- standard-form carriers for Type-III local algebras without pretending that regions have density matrices;
- canonical-core comparison across faithful weights and scale charts;
- Connes cocycles for relative state transport;
- finite corners in which regulated response can be calculated; and
- naturality conditions for response under change of presentation.

It does not select a physical state, supply a Euclidean slab length, turn a cocycle into a Stone generator, or force a spectral floor. Writing \(u_{\varphi|\psi}(t):=[D\varphi:D\psi]_t\), the general law is twisted:

$$
u_{\varphi|\psi}(t+s)
=
u_{\varphi|\psi}(t)\,
\sigma_t^\psi\!\left(u_{\varphi|\psi}(s)\right).
\tag{RL4}
$$

Only under additional invariance or commutation hypotheses does this reduce to an ordinary one-parameter group. The Connes cocycle is therefore comparison data rather than a clock group by default.

Relative entropy does provide an exact dimensionless descent ledger. For a channel \(\Phi\),

$$
\mathcal L_\Phi(\rho;\sigma)
:=
D(\rho\Vert\sigma)
-D(\Phi_*\rho\Vert\Phi_*\sigma)
\geq0,
\tag{RL4a}
$$

and composable channels obey

$$
\mathcal L_{\Psi\Phi}(\rho;\sigma)
=
\mathcal L_\Phi(\rho;\sigma)
+
\mathcal L_\Psi(\Phi_*\rho;\Phi_*\sigma).
\tag{RL4b}
$$

[[contemporary-puzzles/yang-mills-mass-gap/descent-loss-cocycle-and-recovery-fork|The descent-loss cocycle]] extends the restriction version to faithful states on Type-III algebras and identifies its Petz-recoverable zero set. This additive residue is an access-order cost, not a conserved substance or a rate. A state-preserving expectation gives a stronger Pythagorean split only after the relevant modular-invariance gate is satisfied. None of these facts supplies a physical collar or a positive lower floor.

Tomographic completeness must also be separated from quantitative response. Even if a selected state atlas has only scalars in the intersection of its centralizers, its joint analysis map may be injective with singular values tending to zero. The gap-bearing statement is not

$$
\ker\mathscr D=\mathbb C\Omega,
\tag{RL5}
$$

but

$$
\mathscr D^*\mathscr D
\geq
\kappa Q,
\qquad
\kappa>0,
\tag{RL6}
$$

on a separately normalized complete physical carrier.

## Safe response descent

Suppose \(N\subseteq M\) is a modularly invariant expected subalgebra for a faithful state and \(V:L^2(N)\to L^2(M)\) is its standard-form isometry. [[trace-dirichlet-descent/standard-form-pullback-and-reducing-wall|The standard-form pullback theorem]] shows that a closed completely Dirichlet whole form \(\mathcal E_M\) has the safe pullback

$$
\mathcal E_N[\eta]
:=
\mathcal E_M[V\eta],
\tag{RL7}
$$

provided the pulled-back form domain is dense. This preserves the completely Markov property under the stated matrix-standard-form hypotheses.

The superficially more “forgetful” construction

$$
\check{\mathcal E}_N[\eta]
:=
\inf_{q\xi=\eta}\mathcal E_M[\xi]
\tag{RL8}
$$

is a different operation. It agrees with (RL7) when the retained subspace reduces the whole form; without reduction or a separate lumpability theorem, it need not remain Markov. Thus descent cannot be treated as an untyped slogan. The choice between pullback, quotient, compression, and adiabatic elimination changes the dynamics.

## What topology can and cannot do

[[knotting-as-dimensional-presentation/inq|Knotting]], holonomy, characters, and indices can change operator domains and remove specified zero channels without making local differential geometry discrete. [[contemporary-puzzles/yang-mills-mass-gap/triangle-character-cusp-coercivity|The triangle-character theorem]] is the clean finite witness of this “global discreteness, local continuum” clue.

But sector separation is not neutral coercivity:

- ordinary knot type does not detect every topologically trivial local excitation;
- nontrivial triangle characters remove their twisted cusp zero modes while leaving the untwisted sector untreated;
- adjoint \(SU(3)\) holonomy retains Cartan-fixed directions;
- center twists charge lines rather than point-local glueball observables;
- superselection or categorical labels can be nontrivial even when the neutral vacuum representation remains gapless; and
- the finite normal Hessian of an exceptional flag cannot cover an infinite-dimensional OS form core.

The target operator must act inside the neutral representation. Its fixed space must be exactly the vacuum:

$$
\ker D_r
=
\mathbb C\Omega_r
\quad\text{and, more strongly,}\quad
D_r\geq\kappa_*Q_r.
\tag{RL9}
$$

The first equality is a qualitative obstruction statement. The inequality is the mass-gap datum.

## The nonlinear whole law is the gap engine

[[nonlinear-whole-law-surface-response/inq|Nonlinear whole-law surface response]] identifies the actual gap engine. Let \(Y\) be the complete gauge-invariant midpoint configuration and \(Z\) the jointly framed pair of slab boundaries under the full Perron-dressed Wilson law. Define

$$
K_rf
:=
\mathbb E_{\nu_r}[f(Y)\mid Z],
\qquad
B_r^{\mathrm{surf}}
:=
I-K_r^*K_r.
\tag{RL10}
$$

This operator automatically includes interactions encoded by the whole probability law. By contrast, the flat action Hessian forgets the Lie bracket, reduces to a color-repeated Maxwell cochain operator, and retains a volume-soft physical mode.

The strongest noncircular comparison target currently visible is

$$
\boxed{
B_r^{\mathrm{surf}}
\geq
\eta_*R_{r,s_*}^{\leftarrow}
\geq
\eta_*\gamma_*Q_r,}
\qquad
\eta_*,\gamma_*>0,
\tag{RL11}
$$

uniformly in regulator, volume, allowed boundary condition, and included physical sector. Here \(R_{r,s_*}^{\leftarrow}\) must be constructed independently from a reverse-prediction, Dirichlet, or whole-law response at fixed physical depth. Equation (RL11) would give

$$
\|K_rQ_r\|
\leq
\sqrt{1-\eta_*\gamma_*}
<1.
\tag{RL12}
$$

The arrow from (RL12) to a finite-regulator transfer gap is exact by [[contemporary-puzzles/yang-mills-mass-gap/collared-surface-response-to-the-clay-gap|the collared-surface theorem]] only after Perron or ground-state preparation makes the boundary channel stationary, identifies its data-augmentation operator with normalized physical transfer on the compatible vacuum carrier, and holds the slab at fixed physical thickness. [[library/gauge-field-theories-on-a-lattice/inq|Osterwalder--Seiler reflection positivity]] and [[library/from-euclidean-field-theory-to-quantum-field-theory/inq|Schlingemann reconstruction]] are the conventional return route, but reflection positivity alone is not a gap theorem. No current topological, exceptional, modular, or entropy theorem proves (RL11).

## The two shortest credible analytic routes

The existing rigorous endpoints suggest one shared RG bottleneck with two different last-mile certificates. The stronger complete-angle branch is:

$$
\text{gauge-covariant RG to fixed physical blocks}
\longrightarrow
\text{boundary-uniform mixing for the quasi-local polymer law}
\longrightarrow
\text{area-stable whole-cylinder }L^2\text{ factorization}
\longrightarrow
\sup_{a,L,p,\tau,\mathsf s}
\left\|K_{a,L,p,\tau,\mathsf s}^{(n_a)}
Q_{a,L,p,\tau,\mathsf s}\right\|
\leq\rho_*<1,
\qquad
n_a a_{\tau,a}\longrightarrow\ell_*>0.
\tag{RL13}
$$

[[auxiliary-response-localization/inq|Auxiliary response localization]] supplies a second branch:

$$
\begin{aligned}
&\text{gauge-covariant RG to fixed physical blocks}\\
&\longrightarrow
\text{uniform auxiliary }L^2\text{ forgetting plus quasi-local influence}\\
&\longrightarrow
\text{one normalization-invariant static exponent }\sigma_*>0\\
&\longrightarrow
\text{the same exponent on an OS-total centered local family}\\
&\longrightarrow
H\geq\hbar c\,\sigma_*Q.
\end{aligned}
\tag{RL13b}
$$

The auxiliary parameter is eliminated between its forgetting rate and influence speed; it is never identified with clock time. This branch permits observable-dependent prefactors and therefore avoids summing over an infinite transverse surface. It proves the spectral exclusion but not the stronger complete midpoint-to-boundary response angle.

Here the gauge group, global form, vacuum sector, and \(\theta=0\) theory are fixed; the supremum is only over cutoff, volume, boundary placement \(p\), allowed Euclidean orientation \(\tau\), and admissible discretization or blocking scheme \(\mathsf s\). The projection is onto the complete nonvacuum neutral carrier. After a genuine RG step the effective law is generally a quasi-local polymer interaction

$$
H_j=\sum_X\Phi_{j,X},
\tag{RL13a}
$$

not another nearest-neighbor Wilson plaquette law. Thus one must either prove the mixing and factorization estimate for this polymer law with summable tails and pull it back to the original cylinder, or use RG only as a proof device while establishing (RL13) directly for the original Wilson measure.

[[contemporary-puzzles/yang-mills-mass-gap/two-scale-rg-descent-and-the-crossover-lemma|Two-scale RG descent]] identifies the common missing theorem: ultraviolet control must enter an infrared mixing basin at a fixed physical scale with errors summable over the diverging number of block steps. [[contemporary-puzzles/yang-mills-mass-gap/asymptotically-free-response-crossover-lemma|The response-crossover lemma]] gives its present sharp signature. Nothing published proves the required volume-, cutoff-, boundary-, and sector-uniform \(L^2\) forgetting for the full terminal non-Abelian polymer law. Balaban-type control plausibly addresses quasi-locality, not that global floor.

On the complete-angle branch, [[collared-quasi-factorization-and-surface-response/inq|collared quasi-factorization]] identifies the next obstruction: the complete two-ended response must factorize without a transverse surface union bound. A concrete target is a complete conditional Hilbertian decay kernel that survives arbitrary pinnings. [[library/tensorizing-maximal-correlations/inq|Peyre's maximal-correlation theorem]] would then turn its block-to-block matrix norm into an area-stable bunch-to-bunch angle. A same-carrier solder to Perron-prepared OS transfer remains necessary.

On the dense-core branch, a static common exponent for every local OS vector replaces both surface tensorization and direct sampler-to-transfer comparison. Full OS reconstruction, positivity of the diagonal Euclidean autocorrelation, totality after the OS quotient, and uniformity of the exponent through the continuum limit remain necessary.

The known endpoint results do not yet compose. [[library/a-stochastic-analysis-approach-to-lattice-yang-mills-at-strong-coupling/inq|Strong-coupling lattice Yang--Mills]] supplies volume-uniform functional inequalities only under microscopic bare-Wilson strong-coupling hypotheses. Its auxiliary semigroup is not the Wilson transfer clock, but its forgetting and derivative-propagation bounds can be combined to prove a static spatial exponent without making that identification. This does not rule out an asymptotically free trajectory entering an infrared mixing basin after controlled RG; it says only that the published theorem does not establish that crossover. [[library/quasi-factorization-of-the-entropy-and-logarithmic-sobolev-inequalities-for-gibbs-random-fields/inq|Cesi's quasi-factorization]] offers one complete-angle route, but the published sufficient certificate becomes vacuous under the tested fixed-physical-area refinement. [[library/block-factorization-of-the-relative-entropy-via-spatial-mixing/inq|Caputo--Parisi]] offers another under its nearest-neighbor hypotheses. The technically concrete common core is now one decisive new theorem: asymptotically free RG entry into a terminal law with a uniform non-Abelian \(L^2\) floor and weighted influence control. Complete-pinning tensorization and transfer soldering are additional obligations only for the stronger response-angle certificate.

## Admission and kill conditions

A proposed realization is admissible only if it survives all of the following tests:

1. **Complete carrier:** it acts on the full gauge-invariant vacuum complement, including paired boundary charges, gauge cycles, crossing loops, topologically trivial excitations, and every claimed topological sector.
2. **Neutral coverage:** its common kernel contains no nonvacuum neutral direction.
3. **Whole-law origin:** it is derived from the integrated nonlinear law rather than only its flat Hessian, a multiplication operator, or a Killing-form coefficient.
4. **Fixed physical thickness:** the bound is uniform at a slab depth that remains nonzero under refinement; a raw adjacent-slice angle is expected to approach one.
5. **Uniformity:** the lower constant does not decay with volume, transverse area, or cutoff removal.
6. **Noncircularity:** neither the Hamiltonian gap, a fitted correlation length, nor the desired glueball spectrum enters the construction of the response.
7. **Clock separation:** modular flow, RG order, fusion depth, and wall iteration are not called physical time without an independent reconstruction.
8. **Scale separation:** a matched-ledger scale and a response attenuation are derived independently on the same carrier.
9. **Continuum recovery:** form convergence, vacuum convergence, reflection positivity, nontriviality, Poincare covariance, and Yang--Mills identification all survive.
10. **Scope honesty:** an exceptional \(SU(3)\) construction is not advertised as the Clay theorem for every compact simple group.

The composite route therefore assigns the clues rather than merging them. Topology can select admissible global domains; Type III and cocycles can organize presentation and comparison; Hessian and Dirichlet geometry can quantify response; the nonlinear whole law must produce the complete neutral angle; and OS reconstruction must supply the clock in which that angle is observed as a mass gap.
