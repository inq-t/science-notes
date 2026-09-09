# Cycle Moments and the Pure-Gauge Vacuum Return

The determinant chronology returns the complete positive transfer spectrum and bounded vacuum source histories of finite-volume Wilson theory when its auxiliary copies are removed along the many-copy trajectory. The proof normalizes closed cylinders by an explicit flat Gaussian factor, then reconstructs ordered eigenvalues from their even trace moments. It supplies a gap uniform in the auxiliary-copy limit at each fixed spatial graph and Wilson coupling. Its constants are not uniform in spatial volume or continuum removal; neither limit is proved here.

**Status: exact finite-cylinder identities; proved fixed-spatial-graph spectral and vacuum limits; open physical continuum and infinite-volume estimates.** [[reflection-sewing-and-the-auxiliary-boundary-carrier|RS1–18]] constructs the transfer and returns fixed-slab source forms. [[cycle-determinants-and-the-pure-gauge-return|CY6–8]] owns the determinant-to-Wilson action estimate. The new step uses closed trace moments to control the temporal vacuum as well as the finite histories, despite the changing auxiliary carriers.

## Keep the graph and temporal calibration fixed

Let \(\Lambda\) be a fixed finite open spatial subgraph of the homogeneous hypercubic slicing in RS, with \(N=|\Lambda|\), spatial edges \(E_{\rm sp}\), and elementary spatial plaquettes \(\mathcal P_{\rm sp}\). Take \(D\ge2\), \(w=(2D)^{-1}\), a compact group \(G\), and a faithful finite-dimensional unitary representation \(\rho\) of dimension \(n\). The nontrivial source and gap conclusions below use a graph with a physical loop; a spatial square suffices when \(D\ge3\).

Write \(\mathsf T_\nu\) for the positive RS transfer with \(\nu\) copies and
\[
r_\nu\longrightarrow0,\qquad
\kappa_\nu=r_\nu w,\qquad
b_\nu=2\nu r_\nu^4w^4\longrightarrow b\in(0,\infty).
\tag{CM1}
\]
In particular \(\nu r_\nu^6\to0\). The physical temporal step \(a_t>0\) is fixed in this limit. Restrict to the supported gauge-invariant auxiliary carrier when taking logarithms. The full-slice transfer has the same nonzero eigenvalues and traces by RS11.

Put the time direction on a circle of even length \(L\ge6\). This avoids short winding cycles that would change the length-four plaquette count. The periodic trace is exactly the original joint partition function:
\[
\operatorname{Tr}\mathsf T_\nu^L
=\int\det(I-r_\nu P_{U,L})^{-\nu}\prod_e dU_e .
\tag{CM2}
\]
All temporal and spatial links are integrated once, with normalized Haar measures. The Gaussian measures and the endpoint half-weights are those of RS; sewing the trace supplies every complete on-site weight.

## An explicit Gaussian normalization removes the extensive scalar

Let \(B_{\rm sp}\) be the scalar spatial adjacency matrix, with eigenvalues \(\beta_j\), \(1\le j\le N\). Define
\[
a_{\nu,j}=1-\kappa_\nu\beta_j,\qquad
d_{\nu,j}=\frac{a_{\nu,j}+
       \sqrt{a_{\nu,j}^2-4\kappa_\nu^2}}2,\qquad
q_{\nu,j}=\frac{\kappa_\nu}{d_{\nu,j}}.
\tag{CM3}
\]
The spatial degree bound gives \(a_{\nu,j}>2\kappa_\nu\), so \(d_{\nu,j}>0\) and \(0<q_{\nu,j}<1\). At the flat configuration, a spatial mode and temporal frequency \(\theta\) have precision
\[
a_{\nu,j}-2\kappa_\nu\cos\theta
=d_{\nu,j}(1-q_{\nu,j}e^{i\theta})
                (1-q_{\nu,j}e^{-i\theta}).
\]
Multiplying over the \(L\)-th roots of unity yields
\[
\det(I-r_\nu P_{I,L})^{-\nu}
=g_\nu^L z_{\nu,L},\qquad
g_\nu=\prod_{j=1}^N d_{\nu,j}^{-n\nu},\qquad
z_{\nu,L}=\prod_{j=1}^N(1-q_{\nu,j}^L)^{-2n\nu}.
\tag{CM4}
\]
The color multiplicity is \(n\); each complex Gaussian copy contributes one inverse determinant. No additional gauge-volume factor occurs.

This is a normalization from the flat reference precision, not a declaration that the interacting vacuum is Gaussian. Multiplication of \(\mathsf T_\nu\) by \(g_\nu^{-1}\) changes only its common energy offset, not any eigenvalue ratio or temporal duration. Set
\[
\mathsf S_\nu=g_\nu^{-1}\mathsf T_\nu .
\tag{CM5}
\]
At fixed \(\Lambda\), \(q_{\nu,j}=O(r_\nu)\). For every fixed even \(L\ge6\),
\[
0\le\log z_{\nu,L}
\le\frac{2n\nu\sum_jq_{\nu,j}^L}
          {1-\max_jq_{\nu,j}^L}
\longrightarrow0.
\tag{CM6}
\]

## The limiting Wilson transfer and its finite gap

On the spatial frame carrier \(L^2(G^{E_{\rm sp}},dU)\), let
\[
V_{\rm sp}(U)=
\sum_{p\in\mathcal P_{\rm sp}}
       [n-\operatorname{Re}\chi_\rho(U_p)].
\]
For an oriented spatial edge \(e:x\to y\), use the temporal plaquette word
\(U_e g_y V_e^{-1}g_x^{-1}\). The Wilson transfer kernel is
\[
T_{W,b}(U,V)
=e^{-bV_{\rm sp}(U)/2}
\int_{G^\Lambda}
\exp\!\left\{-b\sum_{e:x\to y}
  [n-\operatorname{Re}\chi_\rho(U_e g_y V_e^{-1}g_x^{-1})]\right\}
\prod_xdg_x\,
e^{-bV_{\rm sp}(V)/2}.
\tag{CM7}
\]
Its powers have exactly the Wilson cylinder partition functions in the convention of CY6. It is continuous and strictly positive pointwise on the compact frame space, and vanishes on the charged orthogonal complement after gauge projection.

For completeness, operator positivity follows from the central one-link factor
\[
e^{-bn}e^{b\operatorname{Re}\chi_\rho(g)}
=e^{-bn}\sum_{m\ge0}\frac{(b/2)^m}{m!}
       \chi_{(\rho\oplus\bar\rho)^{\otimes m}}(g).
\tag{CM8}
\]
Every coefficient of every irreducible character is nonnegative. Faithfulness ensures every irreducible occurs in some tensor word of \(\rho\) and \(\bar\rho\): their matrix coefficients form a point-separating self-adjoint algebra on \(G\), and Haar orthogonality excludes an irreducible absent from its dense span. Thus each one-link Fourier eigenvalue is strictly positive. Product convolution, gauge projection, and the bounded positive spatial sandwich give an injective positive operator on the invariant carrier. Smoothness gives compactness. The continuous positive kernel makes its top eigenvalue \(\lambda_{W,0}\) simple with a strictly positive vacuum \(\psi_W\).

The [[strong-coupling-gap-and-continuum-crossover/finite-spacing-transfer-and-bounded-flux-solder|finite-spacing Wilson analysis]] owns the distinction between this logarithmic transfer Hamiltonian and an independently supplied flux Laplacian. No temporal-continuum replacement is used here.

There is an elementary, deliberately volume-dependent, strict bound. Put
\[
a_b=\exp\{-2bn(|\mathcal P_{\rm sp}|+|E_{\rm sp}|)\}>0.
\]
Then \(a_b\le T_{W,b}(U,V)\le1\). If \(I_\psi=\int\psi_W\,dU\), the eigenvector equation gives \(\lambda_{W,0}\psi_W(U)\le I_\psi\). Its Markov ground transform therefore obeys
\[
P_W(U,dV)
\ge a_b\,\frac{\psi_W(V)}{I_\psi}\,dV.
\tag{CM9}
\]
Subtracting this common row leaves \((1-a_b)\) times a Markov kernel. Hence oscillations contract by at most \(1-a_b\). Every nonzero transfer eigenfunction is continuous after undoing the positive vacuum, so every nonconstant eigenmode has eigenvalue ratio at most \(1-a_b\). In particular, on a nontrivial invariant carrier,
\[
0<\gamma_W:=\frac{\lambda_{W,1}}{\lambda_{W,0}}
\le1-a_b<1,\qquad
\Delta_W=-a_t^{-1}\log\gamma_W>0.
\tag{CM10}
\]
Compactness and positivity are essential here; the displayed bound worsens with graph size and coupling. It is not a continuum mass estimate.

## Every even cylinder trace converges

The closed-walk proof of CY7 applies on these even cylinders. Backtracking walks are independent of \(U\), the length-four nontrivial walks are precisely the elementary plaquettes, and all remaining trace differences are nonnegative. Thus
\[
\det(I-r_\nu P_{U,L})^{-\nu}
=\det(I-r_\nu P_{I,L})^{-\nu}
 e^{-b_\nu V_{W,L}(U)-\mathcal R_{\nu,L}(U)},
\]
\[
0\le\mathcal R_{\nu,L}(U)\le
\varepsilon_{\nu,L}:=
\frac{\nu LNn}{3}\frac{r_\nu^6}{1-r_\nu}
\longrightarrow0.
\tag{CM11}
\]
Combining (CM2)–(CM6) gives
\[
\operatorname{Tr}\mathsf S_\nu^L
=z_{\nu,L}\int
 e^{-b_\nu V_{W,L}(U)-\mathcal R_{\nu,L}(U)}\,dU
\longrightarrow
Z_{W,L}(b)=\operatorname{Tr}T_{W,b}^L
\quad(L=6,8,10,\ldots).
\tag{CM12}
\]
This is an unnormalized trace limit, not only convergence of normalized finite-cylinder probabilities. The explicitly removed scalar is what makes it informative about the spectrum.

For any fixed bounded joint frame mark \(F\) on that cylinder the same statement holds with \(F\) inside the integral. For example, the error in replacing the exact integrand by the Wilson one is bounded by
\(\|F\|_\infty[|z_{\nu,L}-1|+z_{\nu,L}(1-e^{-\varepsilon_{\nu,L}})]\),
followed by continuity in \(b_\nu\). Sources on common slices remain a single joint insertion. Their RS conditional covariance is not dropped.

## Trace moments determine the ordered positive eigenvalues

Here is the compact-operator argument needed for the changing carriers. Write the positive eigenvalues of \(\mathsf S_\nu\) and \(T_{W,b}\), with multiplicity, in decreasing order as \((\lambda_{\nu,j})_j\) and \((\lambda_{W,j})_j\). Pad a finite list by zeros; a finite compact group can have a finite-dimensional Wilson carrier. Zero entries contribute nothing to the measures below.
The sixth-trace limit gives a common finite upper bound \(M\) for all eigenvalues when \(\nu\) is sufficiently large. Define finite measures on \([0,M^2]\):
\[
\sigma_\nu=\sum_j\lambda_{\nu,j}^6\,
                 \delta_{\lambda_{\nu,j}^2},\qquad
\sigma_W=\sum_j\lambda_{W,j}^6\,
                 \delta_{\lambda_{W,j}^2}.
\tag{CM13}
\]
For every integer \(p\ge0\), (CM12) says
\[
\int x^p\,d\sigma_\nu
=\operatorname{Tr}\mathsf S_\nu^{6+2p}
\longrightarrow
\operatorname{Tr}T_{W,b}^{6+2p}
=\int x^p\,d\sigma_W.
\]
Polynomials are uniformly dense in continuous functions on this common compact interval, and the total masses are bounded. Therefore \(\sigma_\nu\) converges weakly to \(\sigma_W\).

For any \(s>0\) that is not a limiting eigenvalue, integrate
\(x^{-3}1_{(s^2,M^2]}(x)\). It is bounded away from zero's endpoint and its only interior discontinuity has zero \(\sigma_W\)-mass. The resulting integers are the counts of eigenvalues greater than \(s\), so those counts converge and are eventually equal. Thresholds on either side of each positive limiting eigenvalue now give
\[
\boxed{\lambda_{\nu,j}\longrightarrow\lambda_{W,j}
\quad\text{for every fixed }j.}
\tag{CM14}
\]
For an index beyond a finite limiting rank, the same counting argument at every positive threshold gives convergence to zero. Accumulation at zero is allowed. No common-space operator-norm convergence, or identification of every auxiliary vector, has been asserted.

In particular the actual RS logarithmic gaps satisfy
\[
\boxed{
-a_t^{-1}\log\frac{\lambda_{\nu,1}}{\lambda_{\nu,0}}
\longrightarrow\Delta_W>0.}
\tag{CM15}
\]
The scalar \(g_\nu\) cancels in the ratio. For sufficiently large \(\nu\), every excitation of the supported auxiliary transfer has a gap bounded below by a positive constant depending on \(\Lambda,b,\rho,a_t\).

For the replica innovation of [[two-slice-innovation-geometry/oriented-innovation-and-finite-temporal-repair|OI19–28]], fix \(k\). Choose \((1-a_b)^k<\eta<1\). Equation (CM14) implies \(\|\mathcal K_{\parallel,\nu}\|\le\eta\) for all sufficiently large \(\nu\), including restriction to the centered cyclic frame-source sector. Thus OI25 holds there with \(c=1-\eta^2>0\), uniformly in auxiliary-copy removal at this fixed graph and coupling. This proves that part of the limit; it supplies neither a volume-independent constant nor a new finite-word positive decomposition.

## The same argument returns the actual vacuum source histories

Let \(\widehat T_\nu=\mathsf S_\nu/\lambda_{\nu,0}\), and let \(\Pi_{\nu,0}\) be its rank-one vacuum projection. The sixth-trace bound, the positive limit of \(\lambda_{\nu,0}\), and (CM14) give constants \(C<\infty\), \(0<\theta<1\), uniform for sufficiently large \(\nu\), such that
\[
\|\widehat T_\nu^L-\Pi_{\nu,0}\|_1
=\sum_{j\ge1}
\left(\frac{\lambda_{\nu,j}}{\lambda_{\nu,0}}\right)^L
\le C\theta^{L-6},
\qquad L\ge6.
\tag{CM16}
\]
The same bound holds for the limiting Wilson transfer with its own finite constants.

Take a fixed finite history of bounded spatial frame sources, keeping all coincident factors together. On the full RS slice carrier these are bounded multiplication operators; between them put the prescribed integer powers of the normalized transfer. Its norm is at most the product of the source bounds. Close this fixed history by a long source-free temporal cap. Equation (CM16) bounds the difference between its normalized cylinder expectation and its vacuum expectation uniformly in \(\nu\), with the cap length replacing \(L\). The normalized cylinder expectation at every fixed even total length converges by (CM12) and its marked version. The same cap estimate holds on the Wilson side. Taking the cylinder limit first at fixed length and then letting the cap grow proves
\[
\boxed{
\langle F_0(0)F_1(t_1)\cdots F_s(t_s)\rangle_{\nu,\rm vac}
\longrightarrow
\langle F_0(0)F_1(t_1)\cdots F_s(t_s)\rangle_{W,b,\rm vac}.}
\tag{CM17}
\]
The insertions are ordered products in the original marked chronology, not products of independently averaged coincident sources. On the supported auxiliary representation they use the actual RS conditional integrals. Their vacuum vectors and normalizers are selected by that same transfer.

In particular, for a bounded real nonconstant spatial Wilson observable \(F\), the full-slice vacuum variance converges to the strictly positive Wilson variance: \(\psi_W\) is everywhere positive on compact frame space. For the following source-compression conclusions, take \(G\) connected, as in [[auxiliary-boundary-sufficiency-and-the-wilson-source-algebra|AS1–13]]; this includes the compact simple Lie groups of the target. AS controls the conditional source defect in the RS vacuum. Its exact variance decomposition is
\(\operatorname{Var}_{\rm full}(F)=\operatorname{Var}_{\pi_\nu}(\Phi_\nu F)+\mathbb E_{\pi_\nu}[\Phi_\nu(F^2)-(\Phi_\nu F)^2]\).
Combining the two gives
\[
\operatorname{Var}_{\pi_\nu}(\Phi_\nu F)
\longrightarrow
\operatorname{Var}_{\psi_W^2dU}(F)>0.
\tag{CM18}
\]
Here \(F\) may be a fixed invariant polynomial such as a plaquette trace; AS is invoked within its stated source class. In particular, the changing auxiliary source presentation does not send all nontrivial physical vacuum fluctuations to zero.

## Fixed physical sources also return under chronological transport

The AS variance conclusion extends to each fixed continuous invariant frame source by uniform approximation with invariant matrix polynomials. Faithfulness supplies a dense matrix-coefficient algebra, and Haar averaging preserves approximation while making it invariant. Conditional averaging is a sup-norm contraction, so the polynomial approximation error stays uniformly controlled in \(\nu\). This extension concerns a fixed source on the fixed finite graph, not source complexity growing with refinement.

Let \(F\) be such a source, put \(f_\nu=\Phi_\nu F\), and let
\(G=P_W^kF\), with fixed integer \(k>0\). The positive continuous Wilson vacuum and kernel make \(G\) continuous, invariant and bounded. The marked vacuum limits in (CM17), together with the just-extended source variance estimate, give
\[
\boxed{
\|P_\nu^k\Phi_\nu F-\Phi_\nu(P_W^kF)\|_{L^2(\pi_\nu)}
\longrightarrow0.}
\tag{CM19}
\]
To prove it, expand the squared norm. Its first term is the two-time correlation
\(\langle\Phi_\nu F,P_\nu^{2k}\Phi_\nu F\rangle\),
which tends to \(\|P_W^kF\|^2\). Its second term tends to \(\|G\|^2\); here AS removes exactly the coincident-source defect. Its cross term tends to \(\langle P_W^kF,G\rangle=\|G\|^2\). The sum tends to zero. Complex sources use the real part of that cross term.

This also decides which part of the angular/auxiliary split remains on fixed physical sources. Use the actual \(k\)-slab posterior and variance terms of [[temporal-angular-cancellation-and-the-conditional-variance-ledger|TA12–18]]. Its retained spatial history \(\Theta\) includes the outer spatial frame \(U_k\). Thus \(F(U_k)\) is measurable in that conditional history, and conditional best approximation gives
\[
\mathcal V_{{\rm aux},\nu}(f_\nu)
\le
\mathbb E_{\rm vac}|\,\Phi_\nu F(\Xi_k)-F(U_k)\,|^2
\longrightarrow0.
\]
The marginal at the outer slice is the same selected full-slice vacuum. Temporal gauge changes transport both arguments, so this invariant error is unchanged. Apply the same estimate to \(\Phi_\nu G\), and use (CM19) and the contraction of conditional centering, to obtain
\[
\boxed{
\mathcal V_{{\rm aux},\nu}(f_\nu)\to0,\qquad
\mathcal V_{{\rm aux},\nu}(P_\nu^kf_\nu)\to0.}
\tag{CM20}
\]
Consequently the remaining spatial conditional-mean variances return as
\[
\begin{aligned}
\mathcal V_{{\rm sp},\nu}(f_\nu)
&\longrightarrow
\langle F,(I-P_W^{2k})F\rangle_{\pi_W},\\
\mathcal V_{{\rm sp},\nu}(P_\nu^kf_\nu)
&\longrightarrow
\langle P_W^kF,(I-P_W^{2k})P_W^kF\rangle_{\pi_W},
\qquad d\pi_W=\psi_W^2dU.
\end{aligned}
\tag{CM21}
\]
Their difference is the Wilson replica surplus
\(\langle F,(I-P_W^{2k})^2F\rangle_{\pi_W}\).
Thus the physical source response is carried by the spatial conditional means in this limit. A positive lower bound obtained by counting auxiliary Gaussian variance would target a contribution that actually disappears on these sources. Equations (CM19)–(CM21) are fixed-source statements; they do not supply a new bound uniform in arbitrary source complexity or physical refinement.

## What remains of the rigidity problem

The copy limit is now a return of the finite physical transfer spectrum, selected vacuum and bounded source chronology, with an explicit scalar normalization and no fitted clock. It holds for every supplied faithful compact-group representation satisfying the stated finite construction. It is not peculiar to non-Abelian groups; an Abelian compact finite-volume regulator can also have a positive transfer gap.

The bound (CM9) deteriorates exponentially with the number of spatial cells and with \(b\). Neither it nor moment convergence controls a simultaneous growing graph, the weak-bare-coupling trajectory, a continuum time calibration, or the required infinite-volume physical mass. The active non-Abelian surplus conjecture must improve that dependence through actual spatial interaction and sewing.

[[temporal-angular-cancellation-and-the-conditional-variance-ledger|Temporal angular cancellation]] locates why Haar gauge transport alone cannot provide that improvement. [[conditional-commutator-activity-and-the-neutral-tail|The neutral-tail test]] excludes a remainder made only from its proposed local commutator activities, while [[auxiliary-vacuum-curvature-and-horizontal-source-directions|the vacuum curvature test]] distinguishes the auxiliary flat-gradient geometry from this returned physical chronology. Their failures do not contradict the positive fixed-graph copy-limit result proved here.
