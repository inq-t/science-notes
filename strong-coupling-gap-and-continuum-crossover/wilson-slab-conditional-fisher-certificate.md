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

That failure identifies the required change of grouping: retain actual interacting histories across fixed-physical-depth blocks and control their induced conditional response. Replacing \(T^n\) with blocked kinetic factors would delete its intermediate magnetic terms. No nontrivial four-dimensional continuum law, universal glueball ratio or extension across the weak-bare-coupling trajectory follows from (WF11).

[[wilson-temporal-column-coercivity|Temporal-column coercivity]] performs this grouping for both the actual vacuum's gradient form and a complete bridge at positive blocked depth. Its additional ramp-to-Fisher argument survives time refinement at a small magnetic/electric ratio. This is a new estimate for the blocked bridge, not an extension of the adjacent-slice constant (WF11). The [[wilson-to-hamiltonian-vacuum-limit|continuous-time return]] passes the vacuum and transfer blocks; the predictor inequality then passes through their joint law without assuming convergence of conditional-expectation operators.

[[receipts/wilson_slab_fisher_receipt.py|The finite receipt]] checks incidence bounds, finite conditional covariance, normalized-score Fisher estimates and complete bridge matrices in a discrete gauge calibration. It tests the mechanism, not the infinite compact-group theorem or continuum limit.

## An interacting finite gauge bridge through time refinement

The same receipt now tests the missing *kind* of comparison on open square
graphs and a three-dimensional cube: form the actual interacting transfer,
prepare its Perron vacuum, and calculate the complete physical midpoint
predictor after blocking to a fixed half-slab. This is a finite
\(\mathbb Z_2\) gauge calibration, not a discretization of \(SU(2)\).
The construction below is exact finite-dimensional algebra; floating-point
eigenvalues test it but are not certified continuum bounds.

Let \(\Gamma=(V,E)\) be a connected finite graph with at least one cycle.
Its binary cycle space is
\[
\mathcal C=\ker(\partial:\mathbb F_2^E\to\mathbb F_2^V),
\qquad b=|E|-|V|+1.
\tag{WF13}
\]
Each cycle \(c\) defines the gauge-invariant character
\(\chi_c(U)=\prod_{e:c_e=1}U_e\). A spanning-tree cycle basis identifies
the full orbit space with \(\mathbb F_2^b\); its \(2^b\) characters form
the complete physical slice carrier. No low-energy or low-degree truncation
is taken. The cube has five independent cycles, not six: the product of
its six face holonomies is one. This is the finite Abelian case of
[[gauge-cycle-innovation-filtration/inq|the cycle filtration]].

Write \(F_{z,c}=2^{-b/2}\chi_c(z)\) for the orthogonal character matrix.
For a supplied electric rate \(\gamma>0\), set
\[
\tanh x_\varepsilon=e^{-\gamma\varepsilon},\qquad
H_E=F\operatorname{diag}(\gamma|c|)F^{\mathsf T},\qquad
K_\varepsilon=e^{-\varepsilon H_E}.
\tag{WF14}
\]
Here \(|c|\) counts edges in the binary cycle, including cancellations at
shared edges. The formula follows by restricting the independent-link
Wilson convolution to gauge-invariant characters. In particular,
\(x_\varepsilon=\operatorname{artanh}(e^{-\gamma\varepsilon})\), not the
\(SU(2)\) choice \(1/\varepsilon\). The character spectrum determines
the correct temporal calibration for the chosen group.

For the actual face cycles \(c_p\), supply a magnetic coefficient \(g\ge0\)
and define
\[
V_g(z)=g\sum_p(1-\chi_{c_p}(z)),\quad
T_\varepsilon=e^{-\varepsilon V_g/2}
K_\varepsilon e^{-\varepsilon V_g/2},\quad
H=H_E+V_g.
\tag{WF15}
\]
Neighboring plaquettes do not give independent two-state factors: they
share edges in (WF14), and \(H_E\) and \(V_g\) generally do not commute.
For \(n\varepsilon=\ell\), the finite-dimensional product formula gives
\(T_\varepsilon^n\to e^{-\ell H}\). Every intermediate magnetic factor
remains in \(T_\varepsilon^n\); replacing it by
\(e^{-\ell V_g/2}K_\varepsilon^n e^{-\ell V_g/2}\) changes the law.

Let \(\lambda_0\) and \(\psi>0\), with \(\sum_y\psi_y^2=1\), be the
top eigenpair of \(T_\varepsilon\). The state and reversible clock are
obtained from that same transfer:
\[
\pi_y=\psi_y^2,\qquad
P_{yz}=\frac{(T_\varepsilon)_{yz}\psi_z}{\lambda_0\psi_y},\qquad
R=P^n,\qquad J_{xz}=\pi_x(R^2)_{xz}.
\tag{WF16}
\]
Both endpoints are complete, independently gauge-quotiented slice states.
The normalized conditional-prediction matrix, acting on Euclidean versions
of the state-weighted carriers, is explicitly
\[
A_{(x,z),y}=\frac{\sqrt{\pi_y}\,R_{yx}R_{yz}}{\sqrt{J_{xz}}},
\qquad S=A^{\mathsf T}A.
\tag{WF17}
\]
Conditional independence of the two endpoints given the middle proves
this formula. It is the full predictor, not merely a covariance or Fisher
matrix of selected plaquettes. The independently checked raw-link
compression on two neighboring plaquettes verifies that these orbit
coordinates implement the physical quotient rather than discard a
nonvacuum mode. [[bridge-score-fusion-geometry/gauge-quotients-of-midpoint-bridges|Independent endpoint quotients]] explain why this differs from keeping raw endpoint frames.

With \(\widehat R=\operatorname{diag}(\sqrt\pi)R
\operatorname{diag}(1/\sqrt\pi)\), the checks use the exact order
\[
\widehat R^2\le S\le I,\qquad S\psi=\psi,\qquad
\kappa=1-\lambda_{\max}(S|_{\psi^\perp}).
\tag{WF18}
\]
In the following comparison, \(H\) and its excitation edges are in inverse
Euclidean-time units; an energy conversion is separate. The rate
certificate and independently diagonalized excitation edge are
\[
-\frac{\log(1-\kappa)}{2\ell}
\le\Delta_\varepsilon
:=-\frac1\varepsilon\log\frac{\lambda_1}{\lambda_0}.
\tag{WF19}
\]
This is [[bridge-data-augmentation-solder/inq|the bridge-to-transfer
comparison]] on one actual law. Neither \(\Delta_\varepsilon\) nor
\(\kappa\) is entered as a fit parameter. The graph, coefficients,
boundary convention and temporal yardstick *are* supplied, so their
calculation does not derive those inputs or the arena itself.

At each fixed graph, strict positivity and Perron simplicity also hold for
\(e^{-\ell H}\). To see the required irreducibility, let \(v_e\) record
which basis cycles contain edge \(e\), and let \(X_{v_e}\) translate the
orbit coordinate by that binary vector. Then
\(H_E=(\gamma/2)\sum_e(I-X_{v_e})\); chord-edge vectors include a basis,
so their flips connect the whole orbit space. A finite diagonal potential
does not remove those transitions. The strictly positive joint triple law
makes a perfectly boundary-recoverable midpoint function constant. On this
finite carrier, that proves \(\kappa_H(\ell)>0\).

Finite matrix convergence passes the vacuum and (WF17) to the limiting
bridge: all limiting denominators are positive. Consequently
\(\kappa_\varepsilon(\ell)\to\kappa_H(\ell)>0\). This continuity argument
is not uniform in graph size. It does not extend
[[wilson-to-hamiltonian-vacuum-limit|the compact-group vacuum-limit theorem]]
to bridge operators without additional kernel and conditional-law control.

### What the complete calculation measures

The receipt uses \(\gamma=1/2\), \(\ell=1/2\), magnetic coefficients
\(g=0,0.2,0.8\), and \(n=1,2,4,8,16,32\). It checks 72 refined
bridges on four graphs, in addition to the original single-plaquette and
conditional-Fisher checks. [[receipts/wilson-slab-fisher-receipt-output.txt|The saved receipt output]]
records the values and validation scope. The continuous-time *finite-cube* results are:

| \(g\) | Complete bridge floor \(\kappa_H\) | Excitation rate \(\Delta_H\) | Bridge-certified rate from (WF19) |
|---|---:|---:|---:|
| 0 | 0.757719643 | 2.000000000 | 1.417659722 |
| 0.2 | 0.710760050 | 1.803794803 | 1.240498660 |
| 0.8 | 0.724015532 | 1.875001005 | 1.287410688 |

These are numerical approximations, not interval-certified bounds. At
\(g=0.8\), the refined floor changes from \(0.739473417\) at \(n=1\)
to \(0.724030080\) at \(n=32\), approaching the directly calculated
continuous-time value. The normalized-transfer error decreases from
\(3.029\times10^{-2}\) to \(3.079\times10^{-5}\). Temporal refinement
therefore tests a positive limiting floor while the single-link
Dobrushin hypothesis (WF4) fails: already its temporal term
\(2\tanh x_\varepsilon=2e^{-\gamma\varepsilon}\) exceeds one at
all these refinements. Failure of that sufficient certificate is not
failure of the actual finite-system bridge.

The [[gaussian-bridge-gap-calibration/inq|Gaussian calibration]] is not a
universal readout formula. For this interacting cube,
\[
\kappa_H-\tanh(\ell\Delta_H)\simeq-0.010056220,
\qquad
\|[S_H,e^{-\ell(H-E_0)}]\|\simeq0.002108.
\tag{WF20}
\]
The computed noncommutation is a diagnostic of the same distinction proved
exactly by [[bridge-score-fusion-geometry/gauge-quotients-of-midpoint-bridges|the quotient-bridge counterexample]]:
the recovery operator need not be a scalar spectral function of the clock.
The two-boundary geometry and state belong to its input. The universal
statement used here is the one-sided order (WF18), not the Gaussian inverse
\(\Delta=\ell^{-1}\operatorname{artanh}\kappa\).

There is also an exact rational witness inside the one-plaquette family,
independent of the cube's floating-point spectrum. Choose
\(\gamma=1/2\), \(g=1/\sqrt3\), and
\(\ell=\sqrt3\log2/4\). The resulting Hamiltonian and Doob block are
\[
H=\begin{pmatrix}1&-1\\-1&1+2/\sqrt3\end{pmatrix},\quad
\Delta=4/\sqrt3,\quad
\pi=(3/4,1/4),\quad
R=\frac18\begin{pmatrix}7&1\\3&5\end{pmatrix}.
\tag{WF20a}
\]
Both \(R\) and the symmetric two-state block
\(\frac14\left(\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\right)\)
have nonconstant eigenvalue \(1/2\). For (WF20a), the actual endpoint law
is \(J=\frac1{64}\left(\begin{smallmatrix}39&9\\9&7\end{smallmatrix}\right)\).
Conditional variance of the normalized centered binary observable gives
\[
\kappa=\sum_{x,z=0}^1
\frac{R_{0x}R_{0z}R_{1x}R_{1z}}{J_{xz}}
=\frac{163}{273}
=\frac35-\frac4{1365}.
\tag{WF20b}
\]
The symmetric block instead has \(\kappa=3/5\). At the same \(\ell\),
these blocks have the same excitation rate but different complete bridge
floors. The receipt checks this identity with rational arithmetic. The
dependence on the state and observation relation cannot be removed merely
by knowing the clock's lowest spectral edge.

The next analytic obligation is not to find another positive finite
number. It is to control the *complete interacting bridge* uniformly as
the spatial graph, group representation content and physical regulators
change. This finite-group calculation neither bounds \(SU(2)\)'s
unbounded representation tail nor controls spatial volume or a
four-dimensional continuum trajectory.
