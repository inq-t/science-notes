# Two-Scale RG Descent and the Crossover Lemma

Renormalization-group blocking gives the carrier-first reversal a rigorous analytic target. Disintegration across a block map splits entropy exactly into a coarse contribution and conditional entropy on the forgotten fibers, while observable pullback induces an exact conditional mobility tensor on the coarse carrier. Two-scale logarithmic-Sobolev theorems transfer coercivity only when the fibers, coarse marginal, transported metric, and macro--micro coupling are uniformly controlled. For four-dimensional Yang--Mills the missing theorem is now sharply located: prove that the weak-bare-coupling ultraviolet flow enters a strong-mixing basin at a fixed physical scale, with controlled loss through the diverging number of blocking steps. One may then either eliminate auxiliary time to obtain a common static exponent on an OS-total family, or prove a normalized same-carrier comparison with the OS transfer. Stochastic generators are proof instruments in both routes, not ontological dice.

**Status: [EXACT DISINTEGRATION, PULLBACK-MOBILITY, AND PRODUCT-FIBER IDENTITIES; ESTABLISHED TWO-SCALE LSI THEOREMS ON THEIR DECLARED CARRIERS; ESTABLISHED UV AND STRONG-COUPLING ENDPOINTS; OPEN FOUR-DIMENSIONAL YANG--MILLS CROSSOVER].** No functional inequality below is identified with a Lorentzian mass gap before the transfer and reconstruction maps are supplied.

## Four maps, only one physical gap

At scale $j$, distinguish:

| Object | Carrier | Meaning |
|---|---|---|
| $B_j:\mathcal X_j\to\mathcal X_{j+1}$ | gauge-field configurations | changes resolution |
| $(B_j)_*\mu_j=\mu_{j+1}$ | measures or effective densities | integrates unresolved variables |
| $\mathcal L_j$ | functions in $L^2(\mu_j)$ | auxiliary Langevin or heat-bath relaxation |
| $T_a=e^{-a(H_a-E_{0,a})/(\hbar c)}$ | OS physical Hilbert space | vacuum-normalized physical clock energy and mass gap |

The block map has no spectral gap. The RG transformation has stability exponents but not particle masses. The gap of $-\mathcal L_j$ is a stochastic-time mixing rate. The Yang--Mills mass gap is the positive spectral floor of $H$ after physical-carrier reconstruction.

These distinctions survive a deterministic ontology. A probability measure can be the observer-facing law or Euclidean calculational state of an inaccessible deterministic ground. Its Poincaré or logarithmic-Sobolev inequality is still mathematically valid and may control correlations; it does not establish that the auxiliary diffusion is fundamental time.

## Exact entropy descent along a block map

Let $V=B(U)$ be a coarse variable and disintegrate

$$
\mu(\mathrm dU)
=
\mu(\mathrm dU\mid V)\,\bar\mu(\mathrm dV),
\qquad
\bar\mu=B_*\mu.
$$

For nonnegative $F^2$ with finite entropy, conditional expectation gives the **[EXACT CHAIN RULE]**

$$
\boxed{
\operatorname{Ent}_\mu(F^2)
=
\operatorname{Ent}_{\bar\mu}
\!\left(\mathbb E_\mu[F^2\mid V]\right)
+
\int
\operatorname{Ent}_{\mu(\cdot\mid V)}(F^2)
\,\bar\mu(\mathrm dV).}
\tag{RG1}
$$

Here

$$
\operatorname{Ent}_\mu(f)
:=
\int f\log f\,\mathrm d\mu
-
\left(\int f\,\mathrm d\mu\right)
\log\left(\int f\,\mathrm d\mu\right).
$$

The second term in (RG1) is exactly the conditional entropy remaining inside the fibers. It is a rigorous meaning of distinction hidden by blocking. But the block map and $\mu$ are both load bearing: the fibers alone carry no weights, and (RG1) is an entropy identity rather than energy conservation or factual selection.

## Observable pullback induces the coarse metric

The direction of the arrows matters. Measures descend covariantly,
\(\bar\mu=B_*\mu\), while a coarse observable is tested in the fine theory by
the contravariant pullback

$$
J_Bf=f\circ B.
\tag{RG1a}
$$

Suppose the fine auxiliary form has carré-du-champ matrix \(M(x)\):

$$
\mathcal E_\mu(F)
=
\int_X
\langle\nabla F(x),M(x)\nabla F(x)\rangle
\,\mu(\mathrm dx).
\tag{RG1b}
$$

The induced cylinder form is then exactly

$$
\boxed{
\mathcal E_B^{\mathrm{cyl}}(f)
:=
\mathcal E_\mu(J_Bf)
=
\int_Y
\langle\nabla f(y),G_B(y)\nabla f(y)\rangle
\,\bar\mu(\mathrm dy),}
\tag{RG1c}
$$

where

$$
G_B(y)
:=
\mathbb E_\mu
\!\left[
DB\,M\,DB^*
\mid B=y
\right].
\tag{RG1d}
$$

This formula follows from the chain rule and disintegration. Because
\(J_B(C\circ f)=C\circ J_Bf\) for every normal contraction \(C\), the
cylinder form is Dirichlet whenever its fine parent is, and its restriction
to the closed pullback range is closed when densely defined. A fine Poincaré
constant passes to it exactly:

$$
\mathcal E_B^{\mathrm{cyl}}(f)
\geq
\lambda_\mu\operatorname{Var}_{\bar\mu}(f).
\tag{RG1e}
$$

But (RG1c) also exposes the normalization issue. A nonlinear block does not
generally produce the canonical unit-mobility form on \(Y\); it produces the
conditional tensor \(G_B\). To compare successive scales, one must choose a
coarse metric independently and prove horizontal ellipticity such as

$$
c_jg_{j+1}^{-1}
\leq
G_{B_j}
\leq
C_jg_{j+1}^{-1}
\tag{RG1f}
$$

on the gauge-invariant tangent bundle, with controlled constants. The linear
normalization \(PNP^{\mathsf T}=I\) used below is the flat prototype of this
requirement. Without (RG1f), “the same Poincaré constant survived blocking”
may only report that the auxiliary form and its unit of rate were transported
together.

The cylinder semigroup is generated from the restricted form
\(\mathcal E_\mu(J_Bf)\). It is not generally the compressed fine semigroup
\(J_B^*e^{t\mathcal L}J_B\), which fails the semigroup law unless the
pullback range is invariant. Nor can a coarse edge be run backward by itself.
For
\(\mu_\varepsilon=\nu\otimes\gamma_\varepsilon\), equipped with the sum of
the two factor forms, and projection onto the \(\nu\)-coordinate, the coarse
cylinder gap can stay fixed while the fine gap

$$
\lambda(\mu_\varepsilon)
=
\min\{\lambda(\nu),\lambda(\gamma_\varepsilon)\}
\longrightarrow0.
\tag{RG1g}
$$

Here the last limit assumes
\(\lambda(\gamma_\varepsilon)\to0\). Recovering a uniform fine auxiliary
Poincare inequality by this route therefore requires uniform fiber
coercivity and controlled coupling to coarse directions. This is the missing
information supplied by a two-scale theorem.

That requirement does not extend automatically to a static OS proof:
\(\lambda(\gamma_\varepsilon)\) belongs to the declared auxiliary form,
not necessarily a physical energy operator.
[[rg-covariance-residue/inq|RG covariance residue]] gives an alternative exact split into terminal
covariance and conditional shell covariances. Uniform physical localization
of the transported sources and shell covariances can suffice without a
uniform gap for every fiber sampler. A physically gapless discarded field
visible to the source family still defeats that route, whereas an arbitrarily
slow auxiliary clock does not.

## The linear two-scale coercivity theorem

[[library/a-two-scale-approach-to-logarithmic-sobolev-inequalities/inq|Grunewald, Otto, Villani, and Westdickenberg]] consider a linear coarse map $P:X\to Y$ between Euclidean spaces. If $N$ is their scale parameter, their Theorem 3 normalizes

$$
PNP^{\mathsf T}=\operatorname{id}_Y.
$$

In that normalization, assume:

1. every conditional fiber measure $\mu(\mathrm dx\mid y)$ satisfies $\operatorname{LSI}(\rho)$ uniformly;
2. the coarse marginal satisfies $\operatorname{LSI}(\lambda N)$; and
3. the mixed Hessian coupling between the macro and fiber tangent spaces is bounded by $\kappa$.

Then the fine measure satisfies an LSI with the explicit positive constant

$$
\boxed{
\mathcal T(\rho,\lambda,\kappa)
=
\frac12\left[
\rho+\lambda+\frac{\kappa^2}{\rho}
-
\sqrt{
\left(\rho+\lambda+\frac{\kappa^2}{\rho}\right)^2
-4\rho\lambda}
\right].}
\tag{RG2}
$$

When $\kappa=0$, this reduces to $\min\{\rho,\lambda\}$. The theorem makes “residue cost across scale” quantitative: coercivity survives only insofar as fiber and coarse stiffness dominate their coupling.

### A conditional-Fisher version for Poincare bounds

There is a direct \(L^2\) version on a fixed product
\(\mu(dz,dy)=\nu(dz)\beta_z(dy)\), with declared product metrics and the regularity, dense test class and closed forms of [[conditional-fisher-coercivity/inq|conditional Fisher coercivity]]. Assume conditional Poincare constant \(\rho>0\), actual marginal Poincare constant \(\lambda>0\), and normalized conditional Fisher bound \(I_z\le Cg_Z\).

For an arbitrary \(F(y,z)\), let \(u=\|d_YF\|_2\), \(v=\|d_ZF\|_2\). The conditional-mean derivative includes the direct derivative and score term. Conditional Poincare, the score-map norm, Minkowski's inequality and total variance give
\[
\operatorname{Var}_\mu F
\le\frac{u^2}{\rho}
+\frac1\lambda\left(v+\sqrt{C/\rho}\,u\right)^2.
\tag{RG2a}
\]
Inverting this two-dimensional coefficient matrix yields
\[
\boxed{\lambda_{\rm fine}\ge
T_F(\rho,\lambda,C)=
\frac{\rho+\lambda+C-
\sqrt{(\rho+\lambda+C)^2-4\rho\lambda}}2.}
\tag{RG2b}
\]
The inverse matrix has diagonal entries \(\rho,\lambda+C\), off-diagonal entries \(-\sqrt{\rho C}\), and determinant \(\rho\lambda\). A mixed score-derivative bound \(\kappa\) gives \(C\le\kappa^2/\rho\) and recovers the expression (RG2). These weaker hypotheses establish **Poincare**, not LSI.

No separate small-coupling threshold is needed for positivity of (RG2b), because \(\lambda\) is already the constant of the **actual marginal**. Replacing it by the constant of a second coordinate-conditional law changes the theorem. The Gaussian potential
\[
V(y,z)=\frac{\rho}{2}(y-\alpha z)^2+\frac{\lambda}{2}z^2
\]
has \(C=\rho\alpha^2\) and saturates (RG2b).

For a prescribed target \(0<t<\min(\rho,\lambda)\), the certificate reaches \(t\) exactly when
\[
\boxed{C\le\frac{(\rho-t)(\lambda-t)}{t}.}
\tag{RG2c}
\]
This follows from positivity of the two-dimensional inverse matrix minus \(tI\). If \(\rho>\lambda\), a useful sufficient degradation estimate is
\[
T_F\ge\frac{\lambda}{1+C/(\rho-\lambda)}.
\tag{RG2d}
\]
It follows by substituting the right side for \(t\) in (RG2c).

To iterate, start with a terminal certificate \(\underline\lambda_J>0\). Include a proved comparison \(m_j>0\) from the actual fine form to the chart product form and recursively assign
\[
\underline\lambda_j:=
\frac{m_j\underline\lambda_{j+1}}
{1+C_j/(\rho_j-\underline\lambda_{j+1})},
\qquad \rho_j>\underline\lambda_{j+1}.
\tag{RG2e}
\]
Check the displayed condition at each step, with all forms in the stated scale normalizations. Induction then proves the actual fine gap is at least
\[
\underline\lambda_0
=\underline\lambda_J
\prod_{j<J}\frac{m_j}
{1+C_j/(\rho_j-\underline\lambda_{j+1})}.
\]
Arbitrary independently chosen lower certificates do not telescope. Given a uniformly positive terminal certificate, uniform summability of the ratios and of negative logarithmic metric losses is sufficient to keep this product positive. Bounded loss per step is not sufficient at diverging depth. The actual normalized scores, induced metric and integrated marginal must be used at each step.

[[bridge-data-augmentation-solder/coarse-boundary-leakage-and-response-lifting|Same-law bridge lifting]] supplies a different two-scale theorem directly for the bounded conditional-variance response. Its fiber hypothesis conditions on both the retained core and the full boundary, and it subtracts predictors hidden by boundary coarsening. It does not require identifying this auxiliary Poincare constant with physical energy.

[[library/a-general-two-scale-criteria-for-logarithmic-sobolev-inequalities/inq|Lelievre's nonlinear extension]] replaces $P$ by a smooth reaction coordinate $\xi:D\to M$. Its hypotheses require a uniformly nondegenerate Gram matrix $\nabla\xi\nabla\xi^{\mathsf T}$, uniform fiber LSI, coarse LSI, and a bound on the tangential derivative of the local mean force. This is closer to a geometric descent, but it does not yet cover gauge orbit space: stabilizers make the quotient stratified, and Balaban's gauge slices are local rather than one global smooth submersion.

## What the two known endpoints provide

Balaban's multiscale programme supplies much of the ultraviolet side: gauge-covariant averaging, regular configuration classes and local gauge fixing, constrained background minimizers, propagator estimates, small- and large-field effective densities, and four-dimensional ultraviolet stability. The official Yang--Mills problem statement emphasizes both the importance and the limit of those results: gauge-invariant expectations, a nontrivial continuum theory, and a volume-uniform gap still require new work.

At the other endpoint, strong-coupling lattice gauge theory has convergent expansions, reflection positivity, and transfer-matrix control. [[library/a-stochastic-analysis-approach-to-lattice-yang-mills-at-strong-coupling/inq|Shen, Zhu, and Zhu]] prove explicit volume-uniform Poincaré and logarithmic-Sobolev inequalities, exponential ergodicity, and correlation decay for Wilson measures. For $SU(N)$, in their Wilson-action and metric normalization, their curvature estimate applies when

$$
|\beta|<\frac{1}{16(d-1)},
\qquad
K_S=\frac N2-8N|\beta|(d-1)>0,
$$

and gives $\operatorname{Var}_\mu(F)\leq K_S^{-1}\mathcal E(F,F)$ and $\operatorname{Ent}_\mu(F^2)\leq2K_S^{-1}\mathcal E(F,F)$. Their Langevin gap and their separately derived fixed-spacing correlation exponent are not the physical transfer-Hamiltonian gap.

The continuum trajectory approaches weak bare coupling. It therefore begins outside the strong-coupling basin. Applying a raw-link Dobrushin or Bakry--Emery estimate at the ultraviolet lattice scale cannot bridge the trajectory.

## Physical units reverse the naive gap estimate

Let $a$ be an isotropic Euclidean length spacing, so the Euclidean time step is $a/c$, and let $m_{\mathrm{lat}}(a)$ be a dimensionless decay exponent measured per lattice step. Fix one renormalization convention \(\mathsf s\), and let \(\Lambda_{\mathrm{YM}}^{(\mathsf s)}\) denote its energy-valued Yang--Mills transmutation scale, selected independently of the target gap. The associated energy is

$$
\Delta_E(a)
=
\frac{\hbar c}{a}
m_{\mathrm{lat}}(a).
\tag{RG3}
$$

A fixed order-one lowest lattice exponent would give $\Delta_E(a)\to\infty$, not a finite continuum Yang--Mills mass. If $\Delta_E(a)\to\Delta_E\in(0,\infty)$, then

$$
\boxed{
m_{\mathrm{lat}}(a)
\sim
\frac{a\Delta_E}{\hbar c}.}
\tag{RG4}
$$

If one proves only $\Delta_E(a)\geq\Delta_*>0$, the corresponding target is the lower bound $m_{\mathrm{lat}}(a)\geq a\Delta_*/(\hbar c)$. More exactly, if

$$
r_a
:=
\left\|T_a\restriction_{\Omega_a^\perp}\right\|,
$$

where $\Omega_a^\perp$ is assumed reducing for the vacuum-normalized $T_a=e^{-a(H_a-E_{0,a})/(\hbar c)}$, then $r_a=e^{-a\Delta_E(a)/(\hbar c)}$. Hence $-\log r_a=a\Delta_E(a)/(\hbar c)$, and $1-r_a\sim a\Delta_E/(\hbar c)$ when a finite continuum energy is approached. The desired lower bound shrinks in lattice units while remaining positive in physical units. “Uniform gap” must therefore name the dimensionful physical estimate, not an $a$-independent raw-lattice constant.

## The scale at which stopping could become meaningful

Let one RG step enlarge the lattice length by $L>1$:

$$
a_j=L^ja.
$$

The number of ultraviolet steps needed to reach a fixed physical scale diverges as $a\to0$. A candidate stopping scale satisfies

$$
a_{j_*(a)}
\asymp
\frac{\hbar c}{\Lambda_{\mathrm{YM}}},
\qquad
j_*(a)\longrightarrow\infty.
\tag{RG5}
$$

Here \(\Lambda_{\mathrm{YM}}\) abbreviates the fixed-scheme energy scale \(\Lambda_{\mathrm{YM}}^{(\mathsf s)}\), consistently with \(\Delta_E/\Lambda_{\mathrm{YM}}\). Equivalently, with inverse-length scale $\kappa_{\mathrm{YM}}:=\Lambda_{\mathrm{YM}}/(\hbar c)$, equation (RG5) reads $a_{j_*}\asymp\kappa_{\mathrm{YM}}^{-1}$.

The same blocking data also provide candidate logarithmic shell addresses

$$
N_j=N_0+j\log L.
$$

[[paired-scale-filtrations-and-the-invariant-incidence-wall]] shows why this does not by itself produce a gap. As $j_*(a)\to\infty$, the corresponding one-sided inverse-scale operator has spectral values accumulating at zero. Any floor obtained merely by keeping finitely many shells is therefore a cutoff artifact unless it is uniform through the limit. The structural alternative is a pair of oppositely transforming filtrations whose **joint incidence support** has a regulator-uniform diagonal ceiling. This preserves unbounded relative resolution while bounding the invariant mean address; it is a relation between towers, not an imposed endpoint of either tower.

There is also a nontruncating alternative. [[compensated-incidence-response-and-four-dimensional-balance]] shows that a joint-shell response with bottom coefficient \(\rho_{r,jk}\) produces a uniform soft wall exactly when

$$
\inf_{r,(j,k)\in\Sigma_r}
\rho_{r,jk}e^{-2p\overline N_{r,jk}}>0,
\tag{RG5a}
$$

provided the shells reduce the form; otherwise (RG5a) must be replaced by the direct pullback-form inequality. The RG problem can therefore be asked more sharply: derive the scale growth of \(\rho_{r,jk}\) from the effective interaction and its mixed Hessian, rather than either truncating deep shells or inserting compensating weights. [[library/spectral-gap-critical-exponent-for-glauber-dynamics-of-hierarchical-spin-models/inq|Bauerschmidt--Bodineau's hierarchical recursion]] is a useful precedent because it transports inverse-gap forms through covariance slices while also exhibiting critical models whose gaps still decay. It confirms that RG recursion is machinery for proving compensation, not compensation by itself.

The effective action there is not generally another one-parameter Wilson action. Write it as a quasi-local polymer interaction

$$
H_j(U)=\sum_X\Phi_{j,X}(U).
\tag{RG6}
$$

A meaningful **[PROPOSED STOPPING CONDITION]** is that this full interaction enters a coercive basin. If $\mathrm d\mu_j\propto e^{-H_j}\mathrm dU$, let $\operatorname{Hess}^{\mathrm{car}}$ mean the ordinary full Hessian on the unreduced compact-group product or the horizontal Hessian for a separately declared quotient metric. One sufficient Bakry--Emery coordinate is the full self-adjoint Hessian deficit

$$
\mathfrak I_j
:=
\sup_U
\left\|
\bigl(\operatorname{Hess}^{\mathrm{car}}H_j(U)\bigr)_-
\right\|_{\mathrm{op}},
\tag{RG7}
$$

with

$$
\mathfrak I_{j_*}
<
\rho_{\mathrm{Ric}}^{\mathrm{car}},
\tag{RG8}
$$

after the carrier, metric normalization, domains, and block boundary conditions have been fixed. On an unreduced product $G^E$ with product metric, $\rho_{\mathrm{Ric}}^{\mathrm{car}}$ is inherited from the compact group; a horizontal or stratified quotient requires its own Ricci or $\Gamma_2$ lower-bound theorem. Equivalently, (RG8) asks for $\operatorname{Ric}^{\mathrm{car}}+\operatorname{Hess}^{\mathrm{car}}H_j\geq K_jg$ with $K_j>0$. In the convention $\mathrm d\mu_j\propto e^{S_j}\mathrm dU$, the Hessian sign reverses. Working on the unreduced link product avoids quotient strata but retains gauge-redundant directions; working horizontally requires a separate stratified-quotient analysis. An alternative is a block Gibbs specification with Dobrushin matrix $C_{j_*}$ satisfying

$$
r_{\mathrm{sp}}(C_{j_*})<1.
\tag{RG9}
$$

Equations (RG8) and (RG9) are not claims already proved for Yang--Mills. They describe the sort of operator signature that would place the RG output inside an established strong-mixing theorem.

## The crossover theorem that would make a dent

A complete route would construct gauge-equivariant block maps and effective measures

$$
\mu_{j+1}=(B_j)_*\mu_j
$$

along the tuned asymptotically free trajectory and prove:

1. source-dependent Balaban-type estimates for gauge-invariant expectations;
2. scale-normalized uniform fiber constants $\rho_j$;
3. coarse constants $\lambda_{j+1}$ and coupling bounds $\kappa_j$ satisfying a two-scale recursion such as

   $$
   \lambda_j
   \geq
   \mathcal T(\rho_j,\lambda_{j+1},\kappa_j);
   \tag{RG10}
   $$

4. summable degradation through the diverging number $j_*(a)$ of ultraviolet steps;
5. entry at (RG5) into (RG8), (RG9), or another uniform coercive basin;
6. exponential decay of gauge-invariant Euclidean correlations in **physical** distance, uniformly in cutoff and volume; and
7. reflection-positive OS reconstruction, followed either by OS-total static
   decay or by a normalized same-carrier comparison with the physical transfer
   Hamiltonian.

The last item splits into two non-equivalent branches. A direct cylinder-to-transfer inequality must be normalized on one carrier. Alternatively, [[auxiliary-response-localization/inq|auxiliary response localization]] eliminates sampler time before reconstruction: a volume-uniform centered \(L^2\) contraction together with a weighted quasi-local influence estimate yields a static, normalization-invariant spatial exponent. If one common physical exponent holds on an OS-total centered local family, the spectral theorem supplies the Hamiltonian gap without a direct sampler-to-transfer solder. This second branch still requires the full infinite-volume and continuum OS law; it does not identify the sampler generator with \(H\) or prove the stronger complete-surface response angle.

On the direct branch, the comparison must be normalized on the same carrier. At finite Wilson
temporal spacing, an unbounded comparison of the transfer logarithm with the
cylinder gradient is generally false on the full carrier; the high-character
counterexample is proved in
[[finite-spacing-transfer-and-bounded-flux-solder#The fixed-spacing unbounded-solder no-go|the bounded-flux audit]]. Let \(P_{T,a,V}\) be the
ground-state-transformed normalized transfer on the reconstructed slice
carrier in finite spatial volume \(V\), and let \(D_{\mathrm{cyl},a,V}\) represent the transported cylinder
form, with the same vacuum fixed-space projection. The domain-safe target is

$$
\boxed{
I-P_{T,a,V}
\geq
\eta_{a,V}
\left(I-e^{-\tau_aD_{\mathrm{cyl},a,V}}\right),
\qquad
\eta_{a,V},\tau_a>0,}
\tag{RG11}
$$

where \(\tau_a\) has reciprocal units to \(D_{\mathrm{cyl},a,V}\), so
\(\tau_aD_{\mathrm{cyl},a,V}\) is dimensionless. In the dimensionless
invariant-link normalization, \(\tau_a\) is itself dimensionless and is a
smoothing parameter rather than Euclidean clock time. If

$$
D_{\mathrm{cyl},a,V}
\geq
\lambda_{\mathrm{cyl},a,V}(I-P_{0,a,V}),
$$

then \(-\log x\geq1-x\) gives

$$
\Delta_E(a,V)
\geq
\frac{\hbar c}{a_{\tau,a}}
\eta_{a,V}
\left(1-e^{-\tau_a\lambda_{\mathrm{cyl},a,V}}\right).
\tag{RG12}
$$

This statement is invariant under multiplying the auxiliary cylinder form by
a positive scalar provided \(\tau_a\) is scaled inversely, so that the bounded
operator \(\tau_aD_{\mathrm{cyl},a,V}\) is unchanged. The finite-transfer
continuum stopping condition is therefore

$$
\boxed{
\liminf_{a\downarrow0}
\inf_{V\in\mathcal V_a}
\frac{\hbar c}{a_{\tau,a}\Lambda_{\mathrm{YM}}}
\eta_{a,V}
\left(1-e^{-\tau_a\lambda_{\mathrm{cyl},a,V}}\right)
>0.}
\tag{RG13}
$$

Here \(\mathcal V_a\) is the declared cofinal family of admissible finite spatial volumes and boundary conditions used to construct the infinite-volume theory; the infimum states volume uniformity rather than a simultaneous-limit shortcut. The reference scale \(\Lambda_{\mathrm{YM}}\) is fixed independently by the declared renormalized-coupling/RG prescription, not by the unknown transfer edge.

The smoothing scale \(\tau_a\) must be fixed by the independently declared
cylinder/kinetic normalization, and \(\eta_{a,V}\) must be derived from the
kernels, action, or RG transport—not by tuning either quantity against the
unknown transfer edge. Equivalently, with

$$
q_{a,V}
:=
\eta_{a,V}
\left(1-e^{-\tau_a\lambda_{\mathrm{cyl},a,V}}\right),
\tag{RG13a}
$$

a nonzero lower gap in physical units requires
\(\inf_{V\in\mathcal V_a} q_{a,V}\gtrsim
a_{\tau,a}\Lambda_{\mathrm{YM}}/(\hbar c)\). A finite
continuum energy therefore corresponds to a one-step defect of order
\(a_{\tau,a}\), not a fixed raw defect. If a temporal-continuum theorem
identifies a dimensionless cylinder generator with a Kogut--Susskind kinetic
energy \(\kappa_{a_s}D_{\mathrm{cyl},a,V}\), its natural matching is

$$
\tau_a
=
\frac{a_{\tau,a}\kappa_{a_s}}{\hbar c}
\,[1+o(1)].
\tag{RG13b}
$$

A continuous-time Hamiltonian regulator supplies a distinct unbounded variant
of the direct branch only after
a common-carrier form theorem: if its physical form really obeys
\(\mathfrak h_a\geq\varepsilon_a\mathcal E_{\mathrm{cyl},a}\) on a common
form core with the required domain inclusion, then
\(\Delta_E(a)\geq\varepsilon_a\lambda_{\mathrm{cyl},a}\) remains exact.
This unbounded branch cannot be imported from a finite-spacing Wilson transfer
matrix without a temporal-continuum form theorem.

Both branches require vacuum-projection convergence and complete carrier
coverage. On the direct comparison branch, if the OS/interface map is only a
frame rather than a unitary, its uniform lower-frame constant is an additional
factor in the corresponding gap and stopping conditions. The auxiliary static
branch instead requires convergence of the reflected correlations and OS
totality; once those are proved, it needs no uniform frame constant.

Under the auxiliary-time-elimination hypotheses, the required positive
diagonal OS bound is

$$
0\leq
\left\langle
\psi_F,e^{-s(H-E_0)/(\hbar c)}\psi_F
\right\rangle
\leq
C_F e^{-\sigma_*s}
\qquad(s\geq s_F).
$$

Here \(s\) is physical Euclidean length along the OS axis and
\(\psi_F\) ranges over an OS-total centered local family. With the required
reconstruction and correlation-convergence hypotheses, this excludes spectral
support of the OS Hamiltonian in \((0,\hbar c\,\sigma_*)\). The prefactor
\(C_F\) and onset \(s_F\) may depend on \(F\); the exponent may not. Totality
removes the low spectral projection vector by vector, so no sum over a
transverse surface and no uniform frame prefactor is needed. Decay in one
channel, or exponents whose infimum over the total family is zero, does not
prove the full Hamiltonian gap. Calling it an invariant mass gap additionally
requires a positive-energy Poincaré representation with Lorentz-invariant
joint energy--momentum spectrum and a unique vacuum.

This is the exact role of the “wall.” Each RG arrow forgets fine coordinates and pays the conditional term in (RG1); the two-scale theorem states when coarse and fiber coercivity survive their coupling; the stopping condition asks whether the flow reaches a carrier on which infrared stiffness is manifest. None of that makes stochasticity fundamental. Balaban-type control plausibly supplies quasi-local effective interactions, while the missing non-Abelian theorem is a cutoff-, volume-, boundary-, and declared-vacuum-uniform \(L^2\) floor for the full terminal RG law, coupled to a compatible influence estimate. The auxiliary last mile sharpens the endpoint; it does not remove this crossover wall.
