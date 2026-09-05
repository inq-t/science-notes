# A Conditional-Fisher Certificate for the Actual Wilson Slab

At sufficiently small spatial and temporal Wilson parameters, the finite-history law controls both the true vacuum's Poincare constant and the joint Fisher response of its two adjacent endpoints. Their combination gives a complete midpoint bridge floor uniform in spatial volume. The vacuum is obtained from the same interacting transfer throughout; no global comparison with Haar and no unproved locality of its effective action are needed. The single-link sufficient regime does not cover temporal refinement or the four-dimensional continuum trajectory.

**Status: [EXACT APPLICATION OF DOBRUSHIN VARIANCE AND OSCILLATION BOUNDS] to the declared finite Wilson family; [EXACT] for the resulting complete bridge and physical-transfer bounds; [OPEN] for crossover to continuum parameters.** This is an explicit realization of the known strong-coupling phenomenon, not a new solution of the Clay problem.

## One action, one path law, one vacuum

Let \(d_s\ge2\) and let the spatial graph be a finite hypercubic lattice with ordinary four-distinct-link plaquettes. Use \(G=SU(2)\), normalized Haar measure and
\[
\phi(g)=\tfrac12\operatorname{ReTr}g,\qquad
V_{\rm sp}(U)=\beta_s\sum_p[1-\phi(U_p)],\qquad
a=e^{-V_{\rm sp}/2},
\]
\[
k_x(U,Y)=\prod_e\frac{e^{x\phi(U_eY_e^{-1})}}{Z(x)},\qquad
T=M_aK_xM_a,\qquad x>0,\quad\beta_s\ge0.
\tag{WF1}
\]
For the gradient estimates use \(g(X,Y)=-\operatorname{ReTr}(XY)/2\). This is the unit-\(S^3\) metric: its Laplacian has eigenvalues \(4j(j+1)\), and its Haar Poincare constant is \(\lambda_H=3\). It is not the \(j(j+1)\) metric used in the kinetic normalization note. The final dimensionless Fisher/Poincare quotient is unchanged by a consistent common metric rescaling.

The [[vacuum-aligned-innovation-completion/boundary-action-fixed-points-and-physical-linearization|finite-history recursion]] gives, at fixed \(U_0=U\), the unnormalized path density
\[
\prod_{t=0}^{N-1}k_x(U_t,U_{t+1})
\prod_{t=1}^{N-1}e^{-V_{\rm sp}(U_t)}
e^{-V_{\rm sp}(U_N)/2}.
\tag{WF2}
\]
Its first marginal is proportional to
\(k_x(U,Y)a(Y)(T^{N-1}1)(Y)\,dY\).
At fixed finite spatial volume it tends to the actual Doob transition \(\eta_U=P_T(U,\cdot)\). The two-sided preparation has midpoint marginal
\[
\nu_N(dU)=\frac{(T^N1(U))^2}{\|T^N1\|_2^2}\,dU
\longrightarrow \nu(dU)=\psi(U)^2\,dU.
\tag{WF3}
\]
Only finite-volume Perron convergence is used to pass estimates; no uniform physical gap is assumed.

## Incidence controls the whole history

For one site \(i=(t,e)\), changing one neighboring variable changes the conditional log likelihood by oscillation at most \(4x\) for a temporal bond and \(4\beta_s\) for each shared spatial plaquette. The likelihood-ratio bound proved in the boundary-action note gives total-variation influence at most \(\tanh x\) and \(\tanh\beta_s\), respectively. Multiple plaquettes are handled by successively changing their contributions.

Choose a symmetric nonnegative dominating interdependence matrix \(C=C_t+C_s\). Every temporal site has at most two temporal neighbors. Each spatial link belongs to at most \(2(d_s-1)\) plaquettes, with three other links per plaquette. Hence
\[
q_t=2\tanh x,\qquad
q_s=6(d_s-1)\tanh\beta_s,\qquad
\boxed{q=q_t+q_s<1}
\tag{WF4}
\]
is sufficient for \(\|C\|_1,\|C\|_\infty,\|C\|_2\le q\), uniformly in history depth, spatial volume and fixed exterior data. Half-weight terminal potentials improve these estimates. Periodic boxes must be large enough not to identify links within a plaquette; otherwise actual multiplicities must replace these counts.

[[library/poincare-and-transportation-inequalities-for-gibbs-measures-under-the-dobrushin-uniqueness-condition/inq|Wu's Theorem 2.1]] applies with the trivial single-site metric, whose Wasserstein distance is total variation in the convention \(\sup_A|p(A)-q(A)|\). It gives
\[
(1-q)\operatorname{Var}_\mu F
\le\sum_i\mathbb E_\mu\operatorname{Var}(F\mid U_{-i})
\tag{WF5}
\]
for every finite-history law above. These TV coefficients have not been reinterpreted as geodesic Wasserstein coefficients.

Each single-link conditional has logarithmic density oscillation at most
\[
D_0=4\beta_s(d_s-1)+4x.
\]
Ordinary conditional Haar comparison therefore bounds its gradient Poincare constant below by \(\lambda_H e^{-D_0}\). Apply this separately after (WF5), then test only midpoint functions and pass (WF3):
\[
\boxed{\lambda_\nu\ge
\lambda_*:=\lambda_H e^{-D_0}(1-q).}
\tag{WF6}
\]
This is a gradient inequality for the actual vacuum law. It is not yet the physical energy inequality.

## The missing score covariance is now bounded

Write \(\delta_iF\) for the single-site oscillation of a bounded real function. For the history's auxiliary heat-bath semigroup, Wu's Proposition 2.5 gives oscillation propagation by \(e^{-t(I-C)}\). Integrating its covariance identity yields
\[
|\operatorname{Cov}_\mu(F,G)|
\le\tfrac14\,\delta(F)^{\mathsf T}(I-C)^{-1}\delta(G).
\tag{WF7}
\]
Indeed \(\operatorname{Cov}(F,G)=\int_0^\infty
\sum_i\mathbb E\operatorname{Cov}_i(F,Q_tG)\,dt\); each conditional covariance is bounded by one quarter of the product of oscillations. Symmetry of the chosen majorant removes transpose conventions. This use of auxiliary time proves a static covariance inequality.

The kinetic score \(s_e[v]=d_{U_e}\log k_x(U,Y)[v]\) depends only on \(Y_e\), and \(\delta_e(s_e[v])\le2x\|v\|_g\). Applying (WF7) to the first slice and then taking the horizon limit gives, on the full tangent direct sum,
\[
\boxed{I_\eta(U)(v,v)
=\operatorname{Var}_{\eta_U}\!\left(\sum_es_e[v_e]\right)
\le\frac{x^2}{1-q}\sum_e\|v_e\|_g^2.}
\tag{WF8}
\]
This joint estimate has no factor counting links or tangent components.

It also controls the mixed blocks isolated by [[vacuum-aligned-innovation-completion/local-perron-oscillation-and-conditional-coercivity|the Perron Hessian identity]]. Any path in the Neumann expansion of \((I-C)^{-1}\) connecting distinct spatial links must use at least one \(C_s\). Consequently
\[
\sum_{f\ne e}\|\operatorname{Cov}_{\eta_U}(s_e,s_f)\|
\le \frac{x^2q_s}{(1-q_t)(1-q)}.
\tag{WF9}
\]
This vanishes when the spatial interaction is absent. If \(d_{\rm sp}\) is the adjacency distance through shared plaquettes and \(q_t+e^\theta q_s<1\), inserting spatial weights similarly gives
\[
\|\operatorname{Cov}_{\eta_U}(s_e,s_f)\|
\le\frac{x^2e^{-\theta d_{\rm sp}(e,f)}}
{1-q_t-e^\theta q_s}.
\tag{WF10}
\]
Finite-horizon bounds precede the Perron limit, so these estimates do not assume locality of the unknown vacuum action.

## From the joint Fisher metric to the physical bridge

Under the stationary reversible Doob law, the past and future adjacent endpoints are conditionally independent given midpoint \(U\), each with law \(\eta_U\). Their joint forward Fisher tensor is therefore at most \(2x^2/(1-q)\) times the product metric. Combine this with (WF6) and [[conditional-fisher-coercivity/inq|conditional Fisher coercivity]].

The direct conditional-mean map first acts from endpoint observables to midpoint observables. Its centered adjoint is the physical midpoint predictor from the endpoints; the two operator norms agree. Thus the estimate covers every midpoint \(L^2\) distinction, not just the score span:
\[
\boxed{I-S_{\rm bridge}\ge\kappa_*Q_0,\qquad
\kappa_*=
\frac{\lambda_H e^{-D_0}(1-q)^2}
{\lambda_H e^{-D_0}(1-q)^2+2x^2}>0.}
\tag{WF11}
\]
The regularity and dense-core extension are those of the conditional-Fisher theorem. Positivity and smoothness on each finite compact carrier supply them here.

The raw estimate restricts to gauge-invariant midpoint functions. Independently quotienting the endpoints by the physical gauge action removes predictors and cannot reduce this residual floor. The [[bridge-score-fusion-geometry/gauge-quotients-of-midpoint-bridges|endpoint quotient theorem]] also retains the one-boundary order \(\bar P_T^2\le\bar S_{\rm bridge}\). Hence
\[
\|\bar P_TQ_0\|\le\sqrt{1-\kappa_*},\qquad
\boxed{\Delta_E\ge
-\frac{\hbar c}{2\ell_\tau}\log(1-\kappa_*).}
\tag{WF12}
\]
Here \(\ell_\tau\) is the declared temporal lattice length. This last step concerns the physical transfer logarithm; no sampler gap has been renamed as energy.

## The failure of the current crossover certificate is explicit

In three spatial dimensions, an isotropic choice \(x=\beta_s=b\) satisfies (WF4) when \(14\tanh b<1\). This is a small Wilson-parameter, strong-bare-coupling region. As \(x\to\infty\), \(q_t\to2\), so this single-link certificate fails even at \(\beta_s=0\), where [[bridge-score-fusion-geometry/wilson-bridge-envelopes-under-temporal-blocking|the pure kinetic blocked estimate]] already succeeds.

That failure identifies the next task: regroup the actual interacting histories into fixed-physical-depth blocks and control their induced conditional response. Replacing \(T^n\) with blocked kinetic factors would delete its intermediate magnetic terms. No nontrivial four-dimensional continuum law, universal glueball ratio or extension across the weak-bare-coupling trajectory follows from (WF11).

[[wilson-temporal-column-coercivity|Temporal-column coercivity]] now performs this grouping for the actual vacuum's gradient form: its bound survives time refinement at a small magnetic/electric ratio. It does not extend (WF11) itself. The [[wilson-to-hamiltonian-vacuum-limit|continuous-time return]] uses a separately proved vacuum limit and ground-state Dirichlet identity, not the adjacent-slice Fisher bound above.

[[receipts/wilson_slab_fisher_receipt.py|The finite receipt]] checks incidence bounds, finite conditional covariance, normalized-score Fisher estimates and complete bridge matrices in a discrete gauge calibration. It tests the mechanism, not the infinite compact-group theorem or continuum limit.
