# Conditional Vacuum Rigidity and the Physical Gap

The complete physical source response of the returned interacting vacuum determines its gap: the negative ground-energy Hessian is its reduced resolvent, measured against the actual vacuum covariance. Conditional innovations split this response into blocks, but the mixed blocks must also be controlled. This gives a precise uniform marked-amplitude conjecture for the preparation programme. The ground-state Dirichlet theorem and conditional mixing estimates already have canonical owners; the additional test here concerns source completeness and the assembly of their full spectral response.

## Use the returned vacuum and every physical source

Fix a finite graph and one of the electric-plus-character Hamiltonians returned by [[local-incidence-preparations-and-the-gauge-transfer|local incidence preparation]]. Work on its entire gauge-invariant Haar carrier. Let \(\psi_0>0\) be its normalized ground vector, \(E_0\) its energy, and
\[
d\nu=\psi_0^2d\mu_{\rm Haar},\qquad
L=\psi_0^{-1}(H-E_0)\psi_0,\qquad
\mathcal E(f)=\sum_e\kappa_e\int|\nabla_e f|^2d\nu.
\tag{CV1}
\]
The [[strong-coupling-gap-and-continuum-crossover/gauge-descent-flux-fisher-coercivity|ground-state transform]] proves \(\mathcal E(f)=\langle f,Lf\rangle_\nu\), with the inherited closed form domain. The vacuum becomes \(1\); \(L^{-1}\) below acts only on its mean-zero physical complement. Compact ellipticity gives a positive gap at each fixed graph, without supplying a uniform gap over graphs or couplings.

Let \(F_1,\ldots,F_m\) be bounded real gauge-invariant multiplication observables and introduce the actual perturbed operators
\[
H(\theta)=H-\sum_i\theta_iF_i,\qquad
f_i=F_i-\mathbb E_\nu F_i,\qquad
\mathsf C_{ij}=\langle f_i,f_j\rangle_\nu.
\]
The parameters carry the units required to make each \(\theta_iF_i\) an energy. Bounded perturbation gives an analytic isolated ground-energy branch \(E(\theta)\). Differentiating its eigen-equation gives
\[
\boxed{\mathsf X_{ij}:=-\frac12
\left.\partial_{\theta_i}\partial_{\theta_j}E(\theta)\right|_0
=\langle f_i,L^{-1}f_j\rangle_\nu.}
\tag{CV2}
\]
The real Hamiltonian makes this a real symmetric matrix. Indeed the first vacuum derivative is \((H-E_0)^{-1}(F_i-\langle F_i\rangle)\psi_0\); pairing the two perturbation derivatives supplies the factor two. All sources act on one vacuum and one operator.

Write \(\Delta_{\rm phys}\) for the full centered physical gap. Spectral calculus gives the exact equivalence
\[
\boxed{\Delta_{\rm phys}\ge\Delta
\quad\Longleftrightarrow\quad
\mathsf X\le\Delta^{-1}\mathsf C
\ \text{for every finite family of bounded physical sources}.}
\tag{CV3}
\]
It is enough to use a dense real source algebra, such as finite smooth spin-network sums on the fixed graph. Its centered vectors are dense in \(L^2_0(\nu)_{\rm phys}\): Peter–Weyl density and gauge averaging apply, and the smooth positive finite-volume vacuum changes the norm by bounded factors. Constants and linearly dependent sources merely make \(\mathsf C\) singular; the displayed quadratic-form inequality needs no inverse of that matrix.

For clarity, the variational dual is
\[
\langle f,L^{-1}f\rangle_\nu
=\sup_{\substack{h\in D(\mathcal E)\\\mathbb E_\nu h=0}}
\{2\langle f,h\rangle_\nu-\mathcal E(h)\}.
\tag{CV4}
\]
Completing the square with \(L^{1/2}\) proves it. A Poincare lower bound therefore implies (CV3); conversely, the complete source inequality bounds \(L^{-1}\), and hence the spectrum of \(L\). Checking finitely many selected sources only bounds their visible subspace.

The homogeneous source of [[closed-normalization-and-cosmic-response|the common normalization response]] is one such direction after its nonlinear-source contact term is separated. Its positive susceptibility need not overlap the first excitation. A fixed collection of Gaussian linear and quadratic marks is not automatically a dense physical source algebra. [[prepared-readout-algebra-and-physical-source-completeness|Prepared readout completeness]] now supplies that map for the finite incidence and access constructions: calibrated cross-source jets recover faithful matrix entries, their pointwise algebra is dense, and joint gauge averaging retains the complete physical algebra. Its bounded multiplication insertions construct the actual \(H(\theta)\) family above. Gaussian averaging itself is not multiplicative; compatibility and bounds through the required growing diagrams remain further obligations.

[[conditional-cumulant-influence-and-the-original-chronology|The conditional-cumulant influence]] supplies another constructed physical source. It includes the actual conditional mean, covariance and retained-marginal changes, and its character derivative is an exact mixed matrix element of this same reduced resolvent. [[conditional-character-chronology-and-uniform-temporal-tails|The actual temporal return]] now controls this one response uniformly over all scaled times and in absolute time integral on the planar confinement window, with a uniform actual tail. Its sign, finite bulk coefficient and temporal integrability do not bound the complete mixed matrix in CV3.

## The same susceptibility is a sewn slab curvature

Hold the unperturbed vacuum endpoints fixed and retain the complete amplitude
\[
\mathcal W_T(\theta)=
\log\!\left[e^{TE_0}
\langle\psi_0,e^{-T H(\theta)}\psi_0\rangle\right],
\qquad T>0.
\tag{CV5}
\]
Here \(T\) is the duration of the returned finite Hamiltonian. It is not a separately assigned sampler clock. Dyson expansion with two insertions, followed by subtracting the product of the first derivatives, gives
\[
\boxed{\frac1{2T}
\left.\partial_{\theta_i}\partial_{\theta_j}\mathcal W_T\right|_0
=\langle f_i,R_Tf_j\rangle_\nu,\qquad
R_T=\int_0^T(1-t/T)e^{-tL}\,dt.}
\tag{CV6}
\]
Both sides are on the mean-zero carrier. The two time orderings agree by reversibility and the real structure. The triangular weight records the length available for two insertions separated by \(t\); it must not be dropped at finite \(T\).

For \(\lambda>0\), the scalar multiplier is
\[
r_T(\lambda)=\frac1\lambda-
\frac{1-e^{-T\lambda}}{T\lambda^2},
\qquad 0\le R_T\uparrow L^{-1}.
\tag{CV7}
\]
Monotonicity follows directly from the increasing nonnegative weight \((1-t/T)_+\). Thus uniform control of the complete marked curvature for every slab duration controls the full resolvent. The original normalization, source insertions and fixed endpoint convention travel together; renormalizing each insertion changes \(\mathcal W_T\). This is a test of the actual returned vacuum amplitude, not an identification of a free one-row normalization with an interacting partition function.

## Conditional innovations expose the mixed response obligation

Choose a finite descending family of observable sigma algebras on the full configuration law, invariant under the vertex gauge action. Let their conditional expectations be
\[
P_0=I,\qquad P_J=P_{\rm vac},\qquad
P_iP_j=P_{\max(i,j)},\qquad
D_j=P_{j-1}-P_j\quad(1\le j\le J).
\tag{CV8}
\]
Restrict these maps to the physical carrier. Gauge invariance of \(\nu\) makes that restriction legitimate. The mutually orthogonal projections \(D_j\) satisfy
\[
\operatorname{Var}_\nu F=\sum_j\|D_jF\|_\nu^2.
\tag{CV9}
\]
This is the exact martingale decomposition already used by the flux owner. Here the filtration represents declared observable access; it is not inferred from the Gaussian auxiliary inventory. Boundary frame data must remain available to sew charged regional components into physical observables. Separately neutralizing every region can discard the very distinctions being tested.

For each duration define the actual susceptibility blocks and their operator bounds
\[
\mathsf X_{ij}(T)=D_iR_TD_j,\qquad
b_{ij}(T)=\|\mathsf X_{ij}(T)\|,\qquad b_{ij}=b_{ji}\ge0.
\tag{CV10}
\]
The blocks are mixed source curvatures of (CV6), with the source directions restricted to the corresponding innovation spaces. Unlike differentiation of a conditional mean, this construction requires no assumption that a conditional projection preserves the energy domain: \(P_j,D_j,R_T\) are bounded on this fixed \(L^2\) carrier.

**Conditional-source assembly theorem.** If
\[
\sup_{T>0}\max_i\sum_j b_{ij}(T)\le B,\qquad 0<B<\infty,
\qquad\text{then}\qquad
\boxed{\Delta_{\rm phys}\ge B^{-1}.}
\tag{CV11}
\]
For \(f=\sum_i f_i\), \(f_i=D_if\), one has
\(\langle f,R_Tf\rangle\le\sum_{i,j}b_{ij}\|f_i\|\|f_j\|\).
Symmetry, \(2xy\le x^2+y^2\), and the row bound give at most \(B\sum_i\|f_i\|^2\). Let \(T\to\infty\) and apply (CV3). The same proof works with any certified upper matrix in place of \(b(T)\). The theorem is sufficient; cancellations or a sharper matrix norm can improve its estimate.

Diagonal control alone cannot substitute for the mixed rows. A finite example uses the uniform probability on \(N+1\) points. Successively merge one more point into a single partition cell, giving a decreasing conditional-expectation filtration with \(N\) rank-one innovations. Choose normalized real shell vectors \(h_1,\ldots,h_N\). On their mean-zero span define
\[
R_N=I+\mathbf1\mathbf1^\top,\qquad
L_N=R_N^{-1}=I-\frac{\mathbf1\mathbf1^\top}{N+1},
\tag{CV12}
\]
and let \(L_N1=0\) on the separate vacuum line. This is a nonnegative self-adjoint finite generator with unique positive constant ground vector. Multiplication sources \(F_j=h_j\) realize its matrix (CV2). Every diagonal block is \(2\), yet \(\|R_N\|=N+1\) and its gap is \(1/(N+1)\). This is a spectral assembly counterexample, not a proposed local gauge Hamiltonian or a claim about Markov positivity. It demonstrates a collective source direction missed by separate diagonal bounds.

## The uniform conjecture must estimate the actual conditional law

The existing local theory has more content than finite compactness. [[coarse-response-memory/kinetic-hessian-bootstrap-and-uniform-response|The kinetic Hessian bootstrap]] proves a volume-uniform gap and pointwise conditional Fisher control for the actual \(SU(2)\) Wilson vacuum at sufficiently small local magnetic/electric ratio. [[vacuum-aligned-innovation-completion/local-perron-oscillation-and-conditional-coercivity|The Perron conditional theorem]] gives another exact local estimate and a slow-mixture counterexample to local fiber control alone. Neither licenses continuation of its constants along a weak-bare-coupling continuum trajectory.

Conditional elimination also changes derivatives. On a declared raw product cut, its normalized conditional density \(p(y\mid x)\) obeys
\[
\nabla_x\mathbb E[F\mid x]
=\mathbb E[\nabla_xF\mid x]
+\operatorname{Cov}(F,\nabla_x\log p(y\mid x)\mid x).
\tag{CV13}
\]
[[coarse-response-memory/boundary-interaction-and-conditional-score-budget|The boundary score owner]] proves this identity for the actual vacuum and distinguishes integrated Fisher control from operator control. [[yang-mills-continuum-crossover/two-scale-rg-descent-and-the-crossover-lemma|The two-scale theorem]] assembles conditional and actual marginal Poincare bounds with this mixed-score cost. Its uniform iteration needs a summable total loss, not merely a finite constant at every step. These energy methods can supply estimates toward (CV11); the inverse operator appearing in (CV2) is not permission to assume the desired gap while estimating it.

**Complete-source rigidity conjecture.** For each compact connected simple gauge group and its specified global form, a selected conditional preparation law constructs the actual interacting vacuum, physical source algebra and access filtration through attachment and refinement. In independently fixed physical energy units \(\widehat\Lambda_a>0\), it proves
\[
\boxed{\sup_{a,\,L_{\rm box},\,\text{admissible boundary data},\,T>0}
\ \max_i\sum_j\widehat\Lambda_a\,b_{ij}^{\,a,L_{\rm box}}(T)
\le C_G<\infty.}
\tag{CV14}
\]
The theorem then gives \(\Delta_{a,L_{\rm box}}\ge\widehat\Lambda_a/C_G\) on the entire physical complement. \(C_G\) may depend on the chosen group; it is uniform in the required spatial and coupling limits. The source map, filtration, boundary sectors and uniform bound are substantive conjectural inputs here. Auxiliary preparation correlations do not themselves construct any of them.

For this to give a positive continuum gap, the independently established conversion to common physical energy units must keep \(\widehat\Lambda_a\) bounded away from zero. If the displayed quantities are in internal comparison units and their conversion is \(v_a>0\), the required condition is instead \(\liminf_{a\to0}v_a\widehat\Lambda_a>0\). A uniform dimensionless ratio alone does not prove this scale-return condition.

The noncircular challenge is to derive such complete marked bounds from the primitive comparison and conditional extension law, before assuming physical clustering or an inverse-gap norm. [[preparation-transport-through-spatial-subdivision|The new-access obstruction]] shows why retaining old source laws is not enough when an attachment makes a former presentation direction physical. Newly accessible source sectors and their mixed blocks must enter the same estimate. [[reciprocal-coefficients-and-the-field-gap-test|The soft-field test]] likewise excludes an argument based only on reciprocal coefficients or the quadratic incidence spectrum.

A continuum conclusion still requires the nontrivial vacuum/observable limit, physical transfer identification, full spectral-sector control and spacetime reconstruction stated by the flux owner and the [[contemporary-puzzles/yang-mills-mass-gap/clay-contract-and-scale-assumptions|Clay contract]]. The common-source advance is narrower: homogeneous normalization and local physical susceptibility can be generated by one law, but a mass gap demands control of its complete physical source geometry.
