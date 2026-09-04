# Gauge Dirichlet Descent and the OS Carrier

A volume-uniform Poincare inequality for the Euclidean Wilson Langevin form reaches an interface marginal by two inequivalent arrows. Pulling interface observables into the whole gives a closed Markov cylinder form and inherits the edge exactly; minimizing over all bulk histories with the same conditional interface value gives a smaller least-cost trace with the same lower bound, but need not preserve Markovianity. Either construction yields a noncircular positive operator on a boundary probability carrier. It becomes the desired physical \(D_r\) only after an exact Osterwalder--Schrader carrier identification, a completely Dirichlet observable-algebra lift, and a normalized comparison with physical energy. Naive compression of the bulk Langevin semigroup generally fails the semigroup law, gauge averaging has the wrong kernel, and the available uniform estimate lies in a fixed-lattice strong-coupling region disjoint from the four-dimensional continuum trajectory.

**Status: [PRIMARY-SOURCE THEOREM] for the strong-coupling bulk Poincare and logarithmic-Sobolev constants; [EXACT DEDUCTION] for the closed Markov cylinder form, its inherited edge, and the conditional-infimum trace inequality; [EXACT NO-GO] for automatic Markovianity of the conditional-infimum branch; [CONDITIONAL CONSTRUCTION] for Osterwalder--Schrader transport; [EXACT OBSTRUCTION] for naive semigroup compression; [EXACT NO-GO] for the gauge-averaging defect; [OPEN] for the complete quantum carrier, energy comparison, and continuum limit.**

## The bulk theorem has an explicit volume-uniform edge

Fix a periodic cubic lattice with edge set \(E_L\), dimension \(d>1\), and gauge group \(SO(N)\) with \(N\geq3\) or \(SU(N)\) with \(N\geq2\). Its Wilson measure is

$$
\mathrm d\mu_{\beta,L}(Q)
=
Z_{\beta,L}^{-1}
\exp\!\left(
N\beta\,\operatorname{Re}\sum_p\operatorname{Tr}Q_p
\right)
\prod_{e\in E_L}\mathrm d\sigma_N(Q_e).
\tag{GDT1}
$$

In the normalization of [[library/a-stochastic-analysis-approach-to-lattice-yang-mills-at-strong-coupling/inq|Shen, Zhu, and Zhu]], the reversible Langevin generator has Dirichlet form

$$
\mathcal E_{E,L}[F]
=
\sum_{e\in E_L}
\int |\nabla_eF|^2\,\mathrm d\mu_{\beta,L}.
\tag{GDT2}
$$

Their finite-volume Poincare inequality is

$$
\mathcal E_{E,L}[F]
\geq
K_S\,
\|F-\mu_{\beta,L}(F)\mathbf 1\|_{L^2(\mu_{\beta,L})}^2,
\tag{GDT3}
$$

with

$$
K_S=
\begin{cases}
\dfrac{N-2}{4}-8N|\beta|(d-1),&G=SO(N),\\[6pt]
\dfrac N2-8N|\beta|(d-1),&G=SU(N).
\end{cases}
\tag{GDT4}
$$

Thus \(K_S>0\) when

$$
|\beta|<
\begin{cases}
\dfrac{N-2}{32N(d-1)},&G=SO(N),\\[6pt]
\dfrac1{16(d-1)},&G=SU(N).
\end{cases}
\tag{GDT5}
$$

The same paper proves the logarithmic-Sobolev estimate

$$
\operatorname{Ent}_{\mu_{\beta,L}}(F^2)
\leq
\frac{2}{K_S}\mathcal E_{E,L}[F]
\tag{GDT6}
$$

and \(L^2\) relaxation at rate \(K_S\). These constants do not depend on the torus side length \(L\). The scope is nevertheless precise: the metric and Brownian normalization are fixed by (GDT2), the lattice spacing is not being removed, and \(\beta\) remains in the strong-coupling window (GDT5).

The Wilson action and the product bi-invariant metric are invariant under lattice gauge transformations. It follows from these ingredients that the form and its semigroup preserve the gauge-invariant subspace. This covariance is a direct deduction from the construction, not a separately stated gauge-carrier theorem in the cited paper.

## States descend while observables pull back

Let \(X_L=G^{E_L}\), let \(\pi_\Sigma:X_L\to Y_\Sigma\) retain the link variables of a complete interface \(\Sigma\), and put

$$
\nu_\Sigma=(\pi_\Sigma)_*\mu_{\beta,L}.
\tag{GDT7}
$$

The pullback

$$
J_\Sigma:L^2(\nu_\Sigma)\longrightarrow L^2(\mu_{\beta,L}),
\qquad
J_\Sigma f=f\circ\pi_\Sigma,
\tag{GDT8}
$$

is an isometry. Its adjoint is conditional expectation onto the interface variables, expressed on the local carrier:

$$
q_\Sigma:=J_\Sigma^*,
\qquad
q_\Sigma F
=
\mathbb E_{\mu_{\beta,L}}[F\mid\pi_\Sigma].
\tag{GDT9}
$$

It preserves the constant and the mean and contracts centered \(L^2\)-norm:

$$
q_\Sigma\mathbf1=\mathbf1,
\qquad
\nu_\Sigma(q_\Sigma F)=\mu_{\beta,L}(F),
\qquad
\|(I-P_{\mathbf1})q_\Sigma F\|_2
\leq
\|(I-P_{\mathbf1})F\|_2.
\tag{GDT10}
$$

The first safe local response is the contravariant cylinder form

$$
\mathcal E^{\mathrm{cyl}}_\Sigma[f]
:=
\mathcal E_{E,L}[J_\Sigma f]
=
\sum_{e\in\Sigma}
\int|\nabla_ef|^2\,\mathrm d\nu_\Sigma.
\tag{GDT11}
$$

The equality on the right uses a literal coordinate interface: \(J_\Sigma f\)
has zero derivatives in hidden link directions. The range of \(J_\Sigma\) is
closed in \(L^2(\mu_{\beta,L})\), and the restriction of a closed form to this
range is closed. At a finite Wilson regulator, smooth interface cylinder
functions give a dense form core. Most importantly, for every normal
contraction \(C:\mathbb R\to\mathbb R\),

$$
J_\Sigma(C\circ f)=C\circ J_\Sigma f.
\tag{GDT12}
$$

The bulk Markov inequality therefore passes through \(J_\Sigma\). Thus
\(\mathcal E^{\mathrm{cyl}}_\Sigma\) is a closed Dirichlet form without a
lumpability hypothesis. The bulk Poincare inequality also gives directly

$$
\boxed{
\mathcal E^{\mathrm{cyl}}_\Sigma[f]
\geq
K_S\|f-\nu_\Sigma(f)\mathbf1\|_{L^2(\nu_\Sigma)}^2.}
\tag{GDT13}
$$

This is not the compression \(J_\Sigma^*P_tJ_\Sigma\). It is a new semigroup
generated by the restriction of the *form* to pulled-back observables.

There is also a sharper, covariant least-cost construction. Define the
infimal trace of the bulk form by

$$
\check{\mathcal E}_\Sigma[f]
:=
\inf\left\{
\mathcal E_{E,L}[F]:
F\in D(\mathcal E_{E,L}),\ q_\Sigma F=f
\right\}.
\tag{GDT14}
$$

The infimum eliminates all bulk representatives with the same conditional interface presentation. It is the specialization of the whole-to-local construction in [[trace-dirichlet-descent/inq|Trace Dirichlet Descent]], rather than an independently postulated slice generator.

For every admissible lift \(F\) of \(f\), equations (GDT3) and (GDT10) give

$$
\mathcal E_{E,L}[F]
\geq
K_S\|(I-P_{\mathbf1})F\|_2^2
\geq
K_S\|(I-P_{\mathbf1})q_\Sigma F\|_2^2.
\tag{GDT15}
$$

Taking the infimum over the fiber proves the exact trace inequality

$$
\boxed{
\check{\mathcal E}_\Sigma[f]
\geq
K_S\|f-\nu_\Sigma(f)\mathbf1\|_{L^2(\nu_\Sigma)}^2.}
\tag{GDT16}
$$

No independence of bulk and boundary variables is used in this step. More generally, the same conclusion holds for a state-preserving orthogonal conditional expectation on the relevant \(L^2\) carrier.

Since \(q_\Sigma J_\Sigma=I\), the two constructions obey

$$
\boxed{
K_S\operatorname{Var}_{\nu_\Sigma}(f)
\leq
\check{\mathcal E}_\Sigma[f]
\leq
\mathcal E^{\mathrm{cyl}}_\Sigma[f].}
\tag{GDT17}
$$

The two forms answer different questions. The right-hand form tests a local
observable by pulling it into the whole and is automatically Markov because
the pullback is multiplicative. The middle form asks for the least whole cost
among all representatives with the same conditional local value. It models
fiber elimination more sharply, but conditional expectation is not
multiplicative and need not commute with nonlinear contractions. Calling both
operations “restriction to the interface” hides the decisive variance.
Integrating out the bulk can also make the trace generator nonlocal, so
neither net locality nor finite propagation follows from (GDT17).

If \(\check{\mathcal E}_\Sigma\) is densely defined and closable, its closure still obeys (GDT16). If that closure is Markovian, its associated positive self-adjoint operator \(A_\Sigma\) satisfies

$$
\check{\mathcal E}_\Sigma[f]
=
\|A_\Sigma^{1/2}f\|^2,
\qquad
A_\Sigma\geq K_S(I-P_{\mathbf1}).
\tag{GDT18}
$$

The lower bound itself is exact. Closedness and Markovianity of this
particular conditional-expectation quotient are additional hypotheses;
positivity of an infimal form does not prove them.
[[trace-dirichlet-descent/inq#Conditional expectation alone does not preserve Markovianity|A six-vertex classical counterexample]]
shows that even infimizing a graph Dirichlet form through an ordinary
conditional expectation can violate the normal-contraction inequality. The
Wilson interface therefore needs a special trace theorem, not just the words
“conditional expectation.” If \(\pi_\Sigma\) is equivariant for the residual
interface gauge group, the same construction restricts to
\(L^2(\nu_\Sigma)^{GI}\) and retains (GDT18). The cylinder form already gives
a safe Markov generator \(A_\Sigma^{\mathrm{cyl}}\geq
K_S(I-P_{\mathbf1})\) on that invariant coordinate carrier.

## Osterwalder--Schrader transport is conditional but noncircular

Let \(\theta\) be Euclidean-time reflection, \(\mathscr F_+\) the positive-half field algebra, and \(\mathscr F_\Sigma\) a reflection-fixed separator. Suppose the Wilson measure has the reflection-Markov property for this separator. For gauge-invariant \(F,G\in\mathscr F_+\), put

$$
b_\Sigma F
:=
\mathbb E_\mu[F\mid\mathscr F_\Sigma].
\tag{GDT19}
$$

Conditional independence of the two halves then gives the exact factorization

$$
\langle[F],[G]\rangle_{\mathrm{OS}}
=
\int
\overline{b_\Sigma F}\,b_\Sigma G
\,\mathrm d\nu_\Sigma.
\tag{GDT20}
$$

Consequently the OS null space is \(\ker b_\Sigma\), and

$$
B_{\mathrm{OS}}[F]:=b_\Sigma F
\tag{GDT21}
$$

is an isometry from the reconstructed OS Hilbert space into \(L^2(\nu_\Sigma)^{GI}\). It is unitary onto that carrier if gauge-invariant interface insertions lie in the closure of its range. These hypotheses and the thick-interface issue are isolated in [[vacuum-boundary-gluing-and-wall-response]]; [[library/the-semigroup-characterization-of-osterwalder-schrader-path-spaces/inq|Klein]] and [[library/reflection-positivity-and-spectral-theory/inq|Jorgensen and Tian]] explain why the Markov property is stronger than reflection positivity alone.

One may now transport either interface operator through the OS isometry. For
the safe branch, if (GDT21) is unitary onto the declared coordinate carrier,
define

$$
D^{\mathrm{cyl}}_{\Sigma,L,\beta}
:=
B_{\mathrm{OS}}^*A^{\mathrm{cyl}}_\Sigma B_{\mathrm{OS}}.
\tag{GDT22}
$$

Then

$$
\boxed{
D^{\mathrm{cyl}}_{\Sigma,L,\beta}
\geq
K_S(I-P_{\Omega}).}
\tag{GDT23}
$$

For the least-cost branch, apply the trace construction to the positive-half
form domain with \(q_\Sigma=b_\Sigma\). If its closure is Markovian and
(GDT21) is unitary, define

$$
D_{\Sigma,L,\beta}
:=
B_{\mathrm{OS}}^*A_\Sigma B_{\mathrm{OS}}.
\tag{GDT24}
$$

Then

$$
\boxed{
D_{\Sigma,L,\beta}
\geq
K_S(I-P_{\Omega}).}
\tag{GDT25}
$$

The vacuum vector is the class of the constant function and is carried to
\(\mathbf1\). Thus both (GDT23) and (GDT25) are same-Hilbert-carrier,
vacuum-only edges constructed from the Euclidean whole form; neither \(H\)
nor its spectrum defines them. The first is presently the rigorous Markov
branch. The second adds a least-cost interpretation only when its additional
trace theorem holds.

This remains a conditional bridge rather than the current \(D_r\). Conjugating a classical \(L^2\) Markov semigroup by a Hilbert-space unitary produces a contraction semigroup, but does not by itself produce normal UCP maps on the complete noncommutative neutral observable algebra. One must also prove complete Dirichletness, identify the represented algebra, include electric-flux as well as link-coordinate observables, establish net naturality, and obtain the same-core comparison required in [[kazhdan-markov-process-carrier]]. In a continuum type-III net, a vacuum-preserving expectation onto a proposed local algebra is itself conditional on modular invariance by [[library/conditional-expectations-in-von-neumann-algebras/inq|Takesaki's theorem]].

## Naive compression does not produce a slice process

Let \(P_t=e^{-tA_E}\) be the bulk Langevin semigroup and let

$$
E_\Sigma:=J_\Sigma J_\Sigma^*
\tag{GDT26}
$$

be the orthogonal conditional-expectation projection onto slice-measurable functions. The natural compression

$$
Q_t:=J_\Sigma^*P_tJ_\Sigma
\tag{GDT27}
$$

is positive, unital, and state preserving for each fixed \(t\), but

$$
\begin{aligned}
Q_sQ_t
&=J_\Sigma^*P_sE_\Sigma P_tJ_\Sigma,\\
Q_{s+t}
&=J_\Sigma^*P_sP_tJ_\Sigma,
\end{aligned}
\tag{GDT28}
$$

so

$$
Q_{s+t}-Q_sQ_t
=
J_\Sigma^*P_s(I-E_\Sigma)P_tJ_\Sigma.
\tag{GDT29}
$$

The semigroup law therefore requires a lumpability or intertwining theorem. A sufficient condition is invariance of \(\operatorname{ran}J_\Sigma\) under every \(P_t\). For an interacting thin Wilson slice with \(\beta\neq0\), this invariant-subspace test fails: differentiating the Wilson action with respect to a slice link introduces the adjacent plaquette staples, including links outside the slice. Hence the bulk generator sends a slice-cylinder function to one depending on hidden neighboring variables. At \(\beta=0\), by contrast, the product diffusion does preserve the coordinate subspace.

Equation (GDT29) is a no-go only for the naive compression. It does not rule
out either form-generated interface process. The cylinder semigroup is
generated from (GDT11), not obtained by compressing \(P_t\); the trace
semigroup generated from (GDT14), if closed and Markovian, is a distinct
eliminated-boundary process. Neither is automatically the observed marginal
of the bulk Langevin process at all stochastic times.

Single-link heat-bath updates exhibit the same distinction. Each update is a conditional expectation and hence an orthogonal projection on \(L^2(\mu)\), but a sum or random scan is an algorithmic sampler on the Euclidean carrier. Its normalization must also be fixed: dividing a rate-one-per-link generator by \(|E_L|\) divides any spectral gap by \(|E_L|\). The explicit volume-uniform gauge-theory constant presently available here is the Langevin constant (GDT4), not a transfer of numerical heat-bath decorrelation into the physical spectrum.

## Gauge averaging is a projection to the carrier, not its defect

On the enlarged lattice field algebra, compact gauge averaging has the form

$$
\mathsf E_{\mathscr G}(x)
=
\int_{\mathscr G}U(g)xU(g)^*\,\mathrm dg.
\tag{GDT30}
$$

It is a canonical state-preserving conditional expectation onto the invariant algebra, as used concretely in [[library/entropic-order-parameters-in-weakly-coupled-gauge-theories/inq|Casini, Magan, and Martinez]]. Its defect has

$$
\ker(I-\mathsf E_{\mathscr G})
=
\operatorname{Fix}(\mathsf E_{\mathscr G}),
\tag{GDT31}
$$

which contains the entire gauge-invariant observable sector. After restriction to the physical algebra, \(\mathsf E_{\mathscr G}=I\). Thus \(I-\mathsf E_{\mathscr G}\) may separate gauge redundancy from invariant content, but it annihilates every physical excitation along with the vacuum and cannot be the vacuum-only \(D_r\). Gauge averaging may precede the trace construction; it cannot replace its coercive edge.

## The stochastic gap and the transfer gap are different statements

The Langevin parameter in (GDT2) is sampler time. The OS time translation reconstructed from Euclidean coordinate separation is the semigroup whose logarithm is the physical Hamiltonian. [[library/construction-of-a-selfadjoint-strictly-positive-transfer-matrix-for-euclidean-lattice-gauge-theories/inq|Luscher]] proves that the finite-regulator Wilson transfer matrix is self-adjoint and strictly positive, while [[library/gauge-field-theories-on-a-lattice/inq|Osterwalder and Seiler]] establish the corresponding physical positivity and strong-coupling Euclidean control. Strict positivity means that the transfer matrix has no zero eigenvalue; it is not a proof of a positive separation below its top eigenvalue. Its ground-state transform is an exact reversible one-step Markov operator, but using the unknown contraction edge of that operator as an input would merely rewrite \(H-E_0\). A comparison of its full kernel with an independently derived bounded cylinder response need not be circular.

Uniform exponential decay of Euclidean-time correlations, together with OS positivity, a unique vacuum, and density of reconstructed local states, can imply a transfer spectral gap by the spectral theorem. That is an indirect strong-coupling route. It does not identify the Langevin rate \(K_S\) with the transfer gap and does not give the whole-to-local operator factorization (GDT22) or (GDT24). [[past-future-angle-and-the-transfer-gap]] gives the exact transfer-semigroup version of this distinction.

There is now a precise finite-spacing solder target. Let \(P_T\) be the
vacuum-normalized transfer after its ground-state transform, and let
\(D_\Sigma^{\mathrm{cyl}}\) be the cylinder generator transported to the same
carrier, with the same vacuum fixed-space projection. Instead of the generally false unbounded domination
\(-\log P_T\gtrsim D_\Sigma^{\mathrm{cyl}}\), prove

$$
\boxed{
I-P_T
\geq
\eta_{a,L}
\left(I-e^{-\tau_aD_\Sigma^{\mathrm{cyl}}}\right),
\qquad
\eta_{a,L},\tau_a>0.}
\tag{GDT31a}
$$

All terms are bounded. The parameter \(\tau_a\) has reciprocal units to
\(D_\Sigma^{\mathrm{cyl}}\), so
\(\tau_aD_\Sigma^{\mathrm{cyl}}\) is dimensionless. With the dimensionless
invariant-link gradient normalization in (GDT2), both
\(D_\Sigma^{\mathrm{cyl}}\) and \(\tau_a\) are dimensionless; \(\tau_a\) is
a smoothing parameter, not Euclidean clock time. Equations (GDT23) and
\(-\log x\geq1-x\) would then give

$$
\boxed{
\Delta_T(a,L)
\geq
\frac{\hbar c}{a_\tau}
\eta_{a,L}
\left(1-e^{-\tau_aK_S}\right).}
\tag{GDT31b}
$$

[[finite-spacing-transfer-and-bounded-flux-solder|The bounded-solder audit]]
proves this implication and gives an exact (SU(2)) Wilson-character
counterexample to the unbounded comparison at fixed spacing. What remains is
to fix \(\tau_a\) from the independently declared cylinder/kinetic
normalization and derive \(\eta_{a,L}\) from the action or transfer kernels,
uniformly in the right limits, rather than tune either quantity from the
desired transfer spectrum.

The dimensional continuum target is equally important. Put

$$
q_{a,L}
:=
\eta_{a,L}\left(1-e^{-\tau_aK_S}\right).
\tag{GDT31c}
$$

A lower physical gap \(m_*\Lambda_{\mathrm{YM}}^{(\mathsf s)}\) requires

$$
\inf_L q_{a,L}
\geq
\frac{a_\tau\Lambda_{\mathrm{YM}}^{(\mathsf s)}}{\hbar c}\,m_*
\tag{GDT31d}
$$

along the regulator trajectory. Thus the required one-step lower bound
normally vanishes linearly with \(a_\tau\). If a genuine temporal-continuum
theorem identifies a dimensionless cylinder generator with the
Kogut--Susskind kinetic energy \(\kappa_{a_s}D_\Sigma^{\mathrm{cyl}}\), its
small-step normalization is

$$
\tau_a
=
\frac{a_\tau\kappa_{a_s}}{\hbar c}
+o(a_\tau).
\tag{GDT31e}
$$

Only after that common-form limit has been proved is an unbounded comparison
with the flux Laplacian an admissible energy solder.

No stochastic ontology follows. Langevin and heat-bath dynamics can be used as analytical devices for sampling the Euclidean measure and proving functional inequalities. Calling their parameter a physical time requires an additional dynamical postulate; it is not implied by invariance, reversibility, or a spectral gap of the sampler.

## Volume uniformity stops at the strong-coupling wall

For \(SU(N)\) in four dimensions, (GDT5) gives

$$
|\beta|<\frac1{48}.
\tag{GDT32}
$$

The four-dimensional continuum limit of Wilson Yang--Mills instead follows the asymptotically free weak-coupling trajectory. Consequently the exact constant \(K_S\) is uniform in spatial volume at fixed strong coupling, but not uniform along the required continuum trajectory. Volume uniformity is not lattice-spacing uniformity, boundary-condition uniformity, or physical-unit calibration.

Moreover \(K_S\) is dimensionless and depends on the chosen stochastic normalization. Rescaling the Langevin clock rescales both the form and its gap. To become a physical lower energy, (GDT23) or (GDT25) still needs an independently normalized, same-core comparison with the physical energy or response operator. At adjacent lattice slices a finite physical mass normally corresponds to a dimensionless contraction tending to one at rate \(a\), not to a fixed raw one-step deficit. The calibrated two-scale requirement is developed in [[two-scale-rg-descent-and-the-crossover-lemma]].

The viable theorem target is therefore:

$$
\begin{gathered}
\text{Euclidean whole form with a continuum-relevant uniform estimate}
\xrightarrow{\text{multiplicative observable pullback}}
\text{closed completely Dirichlet interface form}\\
\xrightarrow{\text{reflection-Markov OS unitary}}
D_r\text{ on the complete neutral physical carrier}
\xrightarrow{\text{bounded transfer-defect or temporal-limit comparison}}
H_r\text{ lower bound}.
\end{gathered}
\tag{GDT33}
$$

The pullback step and its inherited gap are exact in (GDT11)--(GDT13) at
fixed strong coupling; the continuum-relevant premise in (GDT33) is not. The
conditional-infimum alternative (GDT14)--(GDT18) retains the same lower bound
but still needs a special Markov theorem. For either route, the OS carrier
identification for a canonical gauge interface, the observable-algebra lift,
the energy solder, and transport through the asymptotically free continuum
limit remain open. This is nevertheless stronger than adjoining an unrelated
Markov operator: the candidate response is forced by the whole form, the
whole state fixes the interface marginal, and local observables acquire their
response only by being tested inside that whole.
