# Nonlinear Conditional Gauge Response

The normalized compact gauge kernel has an exact reverse-conditional Hessian on the full product-Haar carrier. Its normalization contributes both a mean correction and a positive covariance term. Path-incidence bounds then give a volume-uniform conditional Poincare estimate in an explicit strong-coupling regime, together with spatial locality of the one-form susceptibility. This is a nonlinear statement about the actual law, not its tangent Gaussian approximation.

**Status: [EXACT FINITE-CARRIER IDENTITIES AND SUFFICIENT UNIFORM BOUNDS].** The estimates below do not establish the weak-bare-coupling continuum trajectory or the iterated effective-law bounds.

## The law, metric, and score

Take \(G=SU(r)\), \(r\ge2\), and use the bi-invariant metric
\[
g(X,Y)=-r^{-1}\operatorname{ReTr}(XY)
\]
on anti-Hermitian traceless tangent generators. The fine configuration manifold is \(G^E\), not a singular gauge quotient. Haar measure is its normalized Riemannian volume; no coordinate Jacobian has been omitted.

Let
\[
S_\beta(U)=\beta\sum_p\left(1-r^{-1}\operatorname{ReTr}U_p\right),
\qquad
Z_b(U)=\sum_iw_{bi}W_{bi}(U),
\quad w_{bi}\ge0,\quad\sum_iw_{bi}=1,
\tag{NG1}
\]
where the paths for a given \(b\) have common endpoints. Write
\[
\phi(T,Z)=r^{-1}\operatorname{ReTr}(T^*Z),\qquad
N_\kappa(Z)=\int_Ge^{\kappa\phi(W,Z)}\,dW,\qquad
M_\kappa(Z)=\frac{\int_G W e^{\kappa\phi(W,Z)}\,dW}{N_\kappa(Z)}.
\tag{NG2}
\]
For \(\beta,\kappa\ge0\), the reverse law of [[normalized-gauge-kernels-and-markov-residues|the normalized gauge kernel]] is
\[
d\nu_V(U)=\mathcal Z(V)^{-1}e^{-A_V(U)}\,dU,
\qquad
A_V=S_\beta-\kappa\sum_b\phi(V_b,Z_b)
+\sum_b\log N_\kappa(Z_b).
\tag{NG3}
\]
This holds globally, including where an average \(Z_b\) is singular. Both \(\|Z_b\|_{\mathrm{op}}\) and \(\|M_\kappa(Z_b)\|_{\mathrm{op}}\) are at most one.

For \(V_b(t)=V_be^{tX}\), the fine-dependent coarse score is
\[
\ell_{b,X}=\frac{\kappa}{r}\operatorname{ReTr}(XV_b^*Z_b).
\tag{NG4}
\]
The coarse partition function contributes only a fine-independent constant to the normalized score and therefore disappears from a covariance. This is distinct from \(N_\kappa(Z_b(U))\), which depends on fine variables and cannot be dropped.

## The exact Hessian, including normalization

For product-manifold tangents \(\xi,\zeta\), differentiation of (NG2)--(NG3) gives
\[
\begin{aligned}
\operatorname{Hess}A_V(\xi,\zeta)
={}&\operatorname{Hess}S_\beta(\xi,\zeta)\\
&-\kappa\sum_b
\phi\!\left(V_b-M_\kappa(Z_b),
\operatorname{Hess}Z_b(\xi,\zeta)\right)\\
&+\kappa^2\sum_b\operatorname{Cov}_{q_\kappa(\cdot\mid Z_b)}
\left(\phi(W,dZ_b[\xi]),\phi(W,dZ_b[\zeta])\right).
\end{aligned}
\tag{NG5}
\]
The covariance term is positive semidefinite. The mean correction and covariance are the two chain-rule contributions from the log normalizer. This generalizes [[compact-gauge-kernel-tangent-response|the coincident-mode tangent Hessian]] without replacing the Haar law by a local Gaussian.

## A rank-normalized path bound

Let \(n_{p,e}\) count occurrences of \(e\) or \(e^{-1}\) in plaquette path \(p\); define \(n_{bi,e}\) similarly and \(p_{b,e}=\sum_iw_{bi}n_{bi,e}\). Repetitions count with multiplicity. Put
\[
D=\beta\sum_p n_pn_p^\top
+2\kappa\sum_{b,i}w_{bi}n_{bi}n_{bi}^\top.
\tag{NG6}
\]
For the product geodesic \(U_e(t)=U_e e^{tX_e}\), set \(x_e=\|X_e\|_g\). An inverse occurrence is \(e^{-tX_e}U_e^{-1}\), so the same counting applies.

Normalized Hilbert--Schmidt Cauchy--Schwarz gives
\[
r^{-1}|\operatorname{Tr}(A X B Y C)|
\le\|A\|_{\mathrm{op}}\|X\|_g\|Y\|_g
\tag{NG7}
\]
when \(B,C\) and any intervening path factors are unitary. There is no extra factor of \(r\). Summing differentiated occurrences gives
\[
|\phi(T,\operatorname{Hess}W[\xi,\xi])|
\le\|T\|_{\mathrm{op}}(n\cdot x)^2.
\]
Since \(\|V_b-M_\kappa(Z_b)\|_{\mathrm{op}}\le2\), dropping the positive covariance in (NG5) proves
\[
\boxed{\operatorname{Hess}A_V[\xi,\xi]
\ge-x^\top Dx
\ge-\|D\|_{2\to2}\|\xi\|^2.}
\tag{NG8}
\]
The estimate is uniform in all fine and retained configurations.

For this metric, the Killing form is \(B=-2r^2g\), hence the bi-invariant Ricci tensor is
\[
\operatorname{Ric}=-B/4=(r^2/2)g.
\]
The product has the same factorwise lower bound. Thus the weighted Bochner identity implies
\[
\boxed{
\rho:=r^2/2-\|D\|_{2\to2}>0
\quad\Longrightarrow\quad
\operatorname{Var}_{\nu_V}(F)
\le\rho^{-1}\int|dF|^2\,d\nu_V.}
\tag{NG9}
\]
One proof applies
\(\|L_0f\|_2^2=\|\nabla^2f\|_2^2+
\int(\operatorname{Ric}+\operatorname{Hess}A_V)(df,df)\,d\nu_V\)
to each nonconstant eigenfunction on the connected compact product. It forces every positive eigenvalue to be at least \(\rho\). Complex functions follow by real and imaginary parts.

For a volume-uniform sufficient criterion, use
\[
\|D\|_{2\to2}\le\max_e\sum_fD_{ef}
=\max_e\left[
\beta\sum_p n_{p,e}|p|
+2\kappa\sum_{b,i}w_{bi}n_{bi,e}|W_{bi}|
\right].
\tag{NG10}
\]
The required incidence control is **length-weighted**. Bounded numbers of arbitrarily long paths would not suffice. For standard elementary plaquettes of a hypercubic \(d\)-dimensional lattice, counted once and without small-volume edge identifications, the Wilson contribution is at most \(8\beta(d-1)\), with equality for edges having the full \(2(d-1)\) plaquette incidence. Open-boundary edges can contribute less. Readout terms impose their own bound.

Small \(\beta\) here means strong microscopic coupling in this stated Wilson convention. The criterion is sufficient and conservative; failure of (NG9) is not a proof of gaplessness. [[library/a-stochastic-analysis-approach-to-lattice-yang-mills-at-strong-coupling/inq|Shen, Zhu, and Zhu]] supply a primary strong-coupling precedent for uniform functional inequalities and correlation decay. Their action normalization and thresholds must not be copied into (NG9) without conversion.

## Locality on the actual one-form carrier

For distinct edges, the same estimates and covariance Cauchy--Schwarz give
\[
\|\operatorname{Hess}_{ef}A_V\|
\le J_{ef}:=D_{ef}+\kappa^2\sum_bp_{b,e}p_{b,f},
\qquad e\ne f.
\tag{NG11}
\]
Indeed, the linear score satisfies
\(|\phi(W,d_eZ_b[X])|\le p_{b,e}\|X\|_g\);
bounding each variance by its second moment gives the covariance coefficient in (NG11).

For an edge distance \(d_E\), reference length \(b_0>0\), and \(\theta>0\), use the factor weights \(W_{\theta,F}\) of [[auxiliary-response-localization/exact-source-locality-without-a-full-form-gap|the exact-source theorem]] and define
\[
M_\theta=
\max_e\sum_{f\ne e}J_{ef}
\left(e^{\theta d_E(e,f)/b_0}-1\right).
\tag{NG12}
\]
When needed choose a strictly positive upper bound for this expression. Symmetry of \(J\) gives the same column bound. The Schur test and the product Weitzenbock formula imply
\[
\|W_{\theta,F}L_1W_{\theta,F}^{-1}-L_1\|\le M_\theta.
\tag{NG13}
\]
Only the off-diagonal Hessian fails to commute with these parallel scalar edge weights. A bare commutator contains an extra absolute weight and is not the uniformly bounded object.

Equations (NG9) and (NG13), inserted into [[auxiliary-response-localization/exact-source-locality-without-a-full-form-gap|the exact-source locality theorem]], give
\[
|\operatorname{Cov}_{\nu_V}(F,G)|
\le
(\rho^{-1}+M_\theta^{-1})
\exp\!\left[-\frac{\theta\rho}{\rho+M_\theta}
\frac{d_E(\operatorname{supp}dF,\operatorname{supp}dG)}{b_0}\right]
\|dF\|_2\|dG\|_2.
\tag{NG14}
\]
Here (NG9) also supplies a full one-form floor, so a weighted inverse with \(M_\theta<\rho\) is a stronger available alternative. The exact-source theorem does not require that extra smallness: it also remains applicable if a scalar conditional gap is proved by another method while full one-form coercivity fails.

Uniform bounded interaction diameters and the length-weighted incidence sums control (NG12); more generally one needs the displayed exponentially weighted sums. The local coarse score obeys the sharper normalized bound
\[
\|d_e\ell_{b,X}\|
\le\kappa p_{b,e}\|X\|_g,
\qquad
\|d\ell_{b,X}\|_2
\le\kappa\|X\|_g\left(\sum_ep_{b,e}^2\right)^{1/2}.
\tag{NG15}
\]
Thus (NG14) controls the covariance term in the exact conditional derivative of a retained source. Point-to-set localization of an exact score is enough for this step; no arbitrary one-form inverse is required.

[[joint-fisher-response-of-normalized-gauge-blocking|Joint Fisher response]] combines these score bounds before summing tangent components. It controls the complete reverse Fisher tensor through the path-incidence operator, derives the actual coarse Hessian with its covariance subtraction, and supplies an alternative bidirectional conditional-variance certificate from the forward score and unchanged fine marginal.

## The unsolved continuation

This result concerns a Wilson fine action conditioned through one normalized compact kernel. Later exact RG actions need not remain Wilson actions: integrated correlations create additional interactions. Their scalar conditional gap, mixed-Hessian tails, and retained-source norms require new estimates. The parameter \(\kappa\) is a specified readout strength, not a derived physical constant.

For the narrower case of a raw \(SU(2)\) Wilson link with its exterior frozen, [[su2-staple-elimination-and-response|the exact linear-staple law]] now has a gradient bound at arbitrary finite coupling. This does not replace (NG9) for the whole reverse posterior, whose readout normalizers and interactions are nonlinear. Nor does it extend to every group: [[frustrated-su3-conditional-wells|a realizable \(SU(3)\) exterior]] makes the single-link conditional gap tend to zero as inverse coupling grows.

The [[uniform-gaussian-conditional-locality|depth-uniform Gaussian result]] controls a different, linear near-identity regime. Neither result bridges the non-Abelian crossover automatically. Nor can the exceptional representation's positive identity metric do so: [[contemporary-puzzles/yang-mills-mass-gap/faithful-and-adjoint-holonomy-response|the faithful color potential]] has negative Hessian at nontrivial central holonomies. Positive configuration-space Ricci curvature can dominate that potential curvature in (NG9), but it is not spacetime curvature or a physical mass by itself.

[[receipts/nonlinear_conditional_gauge_response_receipt.py|The nonlinear compact receipt]] checks (NG5), (NG8), and (NG11) on a two-loop \(SU(2)\) graph, including inverse and repeated path occurrences and the exact Haar normalizer reduced to one-dimensional quadrature. It tests the algebra and constants, not a continuum limit.
