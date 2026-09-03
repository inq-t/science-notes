# Two-Scale RG Descent and the Crossover Lemma

Renormalization-group blocking gives the carrier-first reversal a rigorous analytic target. Disintegration across a block map splits entropy exactly into a coarse contribution and conditional entropy on the forgotten fibers, while two-scale logarithmic-Sobolev theorems transfer coercivity when the fibers, coarse marginal, and macro--micro coupling are uniformly controlled. For four-dimensional Yang--Mills the missing theorem is now sharply located: prove that the weak-bare-coupling ultraviolet flow enters a strong-mixing basin at a fixed physical scale, with summable loss through the diverging number of blocking steps, and then transport physical correlation decay to the Osterwalder--Schrader Hamiltonian. Stochastic generators are proof instruments in this route, not ontological dice.

**Status: [EXACT DISINTEGRATION IDENTITY; ESTABLISHED TWO-SCALE LSI THEOREMS ON THEIR DECLARED CARRIERS; ESTABLISHED UV AND STRONG-COUPLING ENDPOINTS; OPEN FOUR-DIMENSIONAL YANG--MILLS CROSSOVER].** No functional inequality below is identified with a Lorentzian mass gap before the transfer and reconstruction maps are supplied.

## Four maps, only one physical gap

At scale $j$, distinguish:

| Object | Carrier | Meaning |
|---|---|---|
| $B_j:\mathcal X_j\to\mathcal X_{j+1}$ | gauge-field configurations | changes resolution |
| $(B_j)_*\mu_j=\mu_{j+1}$ | measures or effective densities | integrates unresolved variables |
| $\mathcal L_j$ | functions in $L^2(\mu_j)$ | auxiliary Langevin or heat-bath relaxation |
| $T_a=e^{-a(H_a-E_{0,a})/(\hbar c)}$ | OS physical Hilbert space | vacuum-normalized physical clock energy and mass gap |

The block map has no spectral gap. The RG transformation has stability exponents but not particle masses. The gap of $-\mathcal L_j$ is a stochastic-time mixing rate. The Yang--Mills mass gap is the positive spectral floor of $H$ after physical-carrier reconstruction.

These distinctions survive a deterministic ontology. A probability measure can be the observer-facing law or Euclidean calculational state of an inaccessible deterministic ground. Its Poincare or logarithmic-Sobolev inequality is still mathematically valid and may control correlations; it does not establish that the auxiliary diffusion is fundamental time.

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

[[library/a-general-two-scale-criteria-for-logarithmic-sobolev-inequalities/inq|Lelievre's nonlinear extension]] replaces $P$ by a smooth reaction coordinate $\xi:D\to M$. Its hypotheses require a uniformly nondegenerate Gram matrix $\nabla\xi\nabla\xi^{\mathsf T}$, uniform fiber LSI, coarse LSI, and a bound on the tangential derivative of the local mean force. This is closer to a geometric descent, but it does not yet cover gauge orbit space: stabilizers make the quotient stratified, and Balaban's gauge slices are local rather than one global smooth submersion.

## What the two known endpoints provide

Balaban's multiscale programme supplies much of the ultraviolet side: gauge-covariant averaging, regular configuration classes and local gauge fixing, constrained background minimizers, propagator estimates, small- and large-field effective densities, and four-dimensional ultraviolet stability. The official Yang--Mills problem statement emphasizes both the importance and the limit of those results: gauge-invariant expectations, a nontrivial continuum theory, and a volume-uniform gap still require new work.

At the other endpoint, strong-coupling lattice gauge theory has convergent expansions, reflection positivity, and transfer-matrix control. [[library/a-stochastic-analysis-approach-to-lattice-yang-mills-at-strong-coupling/inq|Shen, Zhu, and Zhu]] prove explicit volume-uniform Poincare and logarithmic-Sobolev inequalities, exponential ergodicity, and correlation decay for Wilson measures. For $SU(N)$, in their Wilson-action and metric normalization, their curvature estimate applies when

$$
|\beta|<\frac{1}{16(d-1)},
\qquad
K_S=\frac N2-8N|\beta|(d-1)>0,
$$

and gives $\operatorname{Var}_\mu(F)\leq K_S^{-1}\mathcal E(F,F)$ and $\operatorname{Ent}_\mu(F^2)\leq2K_S^{-1}\mathcal E(F,F)$. Their Langevin gap and their separately derived fixed-spacing correlation exponent are not the physical transfer-Hamiltonian gap.

The continuum trajectory approaches weak bare coupling. It therefore begins outside the strong-coupling basin. Applying a raw-link Dobrushin or Bakry--Emery estimate at the ultraviolet lattice scale cannot bridge the trajectory.

## Physical units reverse the naive gap estimate

Let $a$ be an isotropic Euclidean length spacing, so the Euclidean time step is $a/c$, and let $m_{\mathrm{lat}}(a)$ be a dimensionless decay exponent measured per lattice step. The associated energy is

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

Here $\Lambda_{\mathrm{YM}}$ is typed as an energy scale, consistently with $\Delta_E/\Lambda_{\mathrm{YM}}$. Equivalently, with inverse-length scale $\kappa_{\mathrm{YM}}:=\Lambda_{\mathrm{YM}}/(\hbar c)$, equation (RG5) reads $a_{j_*}\asymp\kappa_{\mathrm{YM}}^{-1}$.

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
7. reflection-positive OS reconstruction and comparison with the physical transfer Hamiltonian.

Under those hypotheses, a bound

$$
\left|
\langle F,\tau_tF\rangle_c
\right|
\leq
C_F e^{-m_*t}
$$

for a complete physical observable family, together with the required density and spectral hypotheses, would exclude spectral support in $(0,\hbar c\,m_*)$. The completeness clause matters: decay in one channel does not prove the full mass gap.

This is the exact role of the “wall.” Each RG arrow forgets fine coordinates and pays the conditional term in (RG1); the two-scale theorem states when coarse and fiber coercivity survive their coupling; the stopping condition asks whether the flow reaches a carrier on which infrared stiffness is manifest. None of that makes stochasticity fundamental. It turns the philosophical reversal into the concrete missing crossover lemma between Balaban's ultraviolet control and an OS-reconstructed physical spectral floor.
