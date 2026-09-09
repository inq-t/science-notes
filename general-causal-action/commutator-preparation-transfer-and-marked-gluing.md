# Commutator Preparation Transfer and Marked Gluing

The commutator overlap defines a positive trace-class transfer on the actual frame carrier. Its powers describe a path with a separate Gaussian preparation on each edge, and gluing generates correlations between those preparations. Perron normalization gives a reversible discrete path law, while complete source insertions retain the original normalization. This is a finite transfer construction; its supported logarithm and compact spectral gap do not establish a physical clock or a Yang–Mills gap.

## The overlap and its carrier

Use \(V=M_2(\mathbb C)\), \(h(X,Y)=\operatorname{Tr}(X^\dagger Y)/2\), a declared \(G>0\), and the normalized circular complex Gaussian \(P_G\) from [[multiplication-sensitive-cycle-preparations|the commutator preparation]]. Frames lie in \(\mathcal U=U(2)\) with normalized Haar measure. The same statements hold on its \(SU(2)\) restriction. For \(\beta>0\), put
\[
C_U\xi=[U,\xi],\quad D_U=C_U^\dagger C_U,\quad
f_U(\xi)=e^{-\beta\langle\xi,D_U\xi\rangle/2},\qquad
K_\beta(U,V)=\mathbb E_G[f_Uf_V].
\tag{TG1}
\]
Thus
\[
K_\beta(U,V)=
\frac1{\det G\det Q(U,V)},\qquad
Q(U,V)=G^{-1}+\frac\beta2(D_U+D_V).
\tag{TG2}
\]
The two-frame determinant in the preparation note applies with half-strength per branch. In particular, \(K_\beta(U,U)=w_\beta(U)\).

Define
\[
\mathsf A:L^2(\mathcal U,dU)\to L^2(P_G),\qquad
(\mathsf A\phi)(\xi)=\int f_U(\xi)\phi(U)\,dU,
\]
\[
(\mathsf T\phi)(U)=\int K_\beta(U,V)\phi(V)\,dV.
\tag{TG3}
\]
Since \(0<f_U\le1\),
\[
\boxed{
\mathsf T=\mathsf A^\dagger\mathsf A\ge0,\qquad
\operatorname{Tr}\mathsf T=\|\mathsf A\|_{\rm HS}^2
=\int w_\beta(U)\,dU\le1.}
\tag{TG4}
\]
The kernel of \(\mathsf A\) is square-integrable, proving the Hilbert–Schmidt assertion and hence trace class. The exact supported carrier is
\[
\mathcal H_{\rm supp}=(\ker\mathsf T)^\perp,\qquad
\ker\mathsf T=
\left\{\phi:\int f_U(\xi)\phi(U)dU=0\quad P_G\text{-a.e.}\right\}.
\tag{TG5}
\]
The map \(\mathsf A\) identifies the preparation overlap quotient through its polar decomposition; it is not itself an isometry for the original frame norm. [[directed-analytic-realization/preparation-overlaps-and-the-transition-algebra|Preparation overlaps]] owns the associated transition-algebra construction.

For conjugation-invariant \(G=g_0P_0+gP_1\), [[commutator-overlap-nullspace-and-angular-coverage|the angular coverage theorem]] identifies the complete quotient and its lost frame observables. That quotient is not automatically a physical gauge quotient.

## Perron normalization supplies a discrete path law

The kernel is continuous by dominated convergence and strictly positive everywhere. Compactness of \(\mathcal U^2\) gives a positive minimum. Consequently its largest eigenvalue \(\lambda_0>0\) is simple and has a continuous eigenfunction \(h_0>0\), normalized by \(\int h_0^2dU=1\).

Here is a direct justification of simplicity. Replacing a maximizing real eigenfunction by its absolute value cannot decrease its quadratic form. Strict positivity of the kernel excludes a sign-changing maximizer. The resulting nonnegative eigenfunction becomes strictly positive under \(\mathsf T\). Any second top eigenfunction orthogonal to it would change sign and violate the same strict inequality. Continuity follows from \(h_0=\lambda_0^{-1}\mathsf T h_0\).

The ground-state transform is
\[
\boxed{
p(U,dV)=\frac{K_\beta(U,V)h_0(V)}{\lambda_0h_0(U)}\,dV,
\qquad \pi(dU)=h_0(U)^2dU.}
\tag{TG6}
\]
Its rows integrate to one, and \(\pi(dU)p(U,dV)\) is symmetric. The stationary \(n\)-step path density is therefore
\[
\lambda_0^{-n}h_0(U_0)h_0(U_n)
\prod_{i=1}^nK_\beta(U_{i-1},U_i)
\prod_{i=0}^n dU_i.
\tag{TG7}
\]
The stationary slice law is the Perron law \(\pi\); the diagonal weight \(w_\beta(U)dU\) has a different role in (TG4).

On \(\mathcal H_{\rm supp}\), choose a step duration \(\tau>0\) and define
\[
H_\tau=-\tau^{-1}\log(\mathsf T/\lambda_0).
\tag{TG8}
\]
Spectral calculus makes this a nonnegative self-adjoint operator. The positive top eigenvalue is isolated, so its nonvacuum spectrum, when present, has a positive edge at fixed \(\beta,G,\tau\). This compact-transfer statement supplies no uniform spatial or continuum estimate. The support restriction matters, as in [[sewn-transfer-clock-and-the-rotor-limit|the rotor transfer]]: the full frame space has exact null directions. Integer powers give the path law; arbitrary fractional powers are not asserted to be pointwise Markov.

The original factor \(\lambda_0^n\) remains part of the closed amplitude. If parameters or homogeneous sources vary, its derivatives cannot be discarded merely because the transfer has been vacuum-normalized.

## Gluing uses a fresh preparation for each edge

The actual two-step kernel is
\[
\boxed{
\mathsf T^2(U,V)=
\int dW\int dP_G(\xi)dP_G(\eta)\,
f_U(\xi)f_W(\xi)f_W(\eta)f_V(\eta).}
\tag{TG9}
\]
The edge preparations \(\xi,\eta\) are independent before the middle-frame integration. More generally, (TG7) has one such preparation per edge. Associativity follows from integration of these fixed full amplitudes, with the Haar and preparation measures retained.

There are two exact failure tests. First,
\[
K_\beta(I,I)=1,\qquad
\mathsf T^2(I,I)=\int(\mathbb E_G f_W)^2dW<1.
\tag{TG10}
\]
For noncentral \(W\), \(f_W<1\) on a set of positive Gaussian measure. Such frames have positive Haar measure. Thus no kernel \(K_{\beta'}\) with the original normalization equals this square. This does not exclude closure in a larger class retaining scalar and source data.

Second, reusing one preparation over both edges would give
\[
\int\mathbb E_G[f_W^2]\,dW
-\mathsf T^2(I,I)
=\int\operatorname{Var}_G(f_W)\,dW>0.
\tag{TG11}
\]
The variance is strict for noncentral frames because \(G>0\) and \(\beta>0\). A common preparation over an entire path therefore defines a different law unless its persistent correlations are explicitly retained as extra history.

The algebraic frame \(I\) makes its comparison factor \(f_I=1\); it does not make the positive-width transfer an identity transition. A presentation unit must leave the full amplitude unchanged with its sources transported. The transition identity is the Dirac kernel, not the row \(K_\beta(I,V)\).

## Arbitrary preparation marks survive two-step sewing

For one edge, attach a linear source \(j\in V\) and a Hermitian mark \(T\), with \(Q(U,V)+T>0\). Gaussian integration gives
\[
K_\beta^{j,T}(U,V)=
\frac{\exp[j^\dagger(Q(U,V)+T)^{-1}j]}
{\det G\det(Q(U,V)+T)}.
\tag{TG12}
\]
This retains the normalized preparation measure, including its factor \((\det G)^{-1}\).

For two edges, allow a joint source \(\mathbf j=(j_1,j_2)\), a Hermitian block mark \(\mathbb T\) on \(V\oplus V\), and a bounded middle-frame insertion \(a(W)\). Assuming the following precision is positive for every \(W\), the complete marked amplitude is
\[
\mathbb Q_W=
\operatorname{diag}(Q(U,W),Q(W,V))+\mathbb T,
\]
\[
\boxed{
\mathcal Z^{(2)}(U,V;\mathbf j,\mathbb T,a)
=\int dW\,a(W)
\frac{\exp(\mathbf j^\dagger\mathbb Q_W^{-1}\mathbf j)}
{(\det G)^2\det\mathbb Q_W}.}
\tag{TG13}
\]
Block-diagonal marks reproduce the product of two marked edge kernels. Off-diagonal marks remain joint insertions; they cannot be replaced by independently marked factors. Arbitrary polynomial source derivatives follow from this generating amplitude. [[marked-gaussian-constraints-and-sewing-measures|Marked Gaussian sewing]] owns the corresponding source and normalization bookkeeping when additional linear constraints or readouts are imposed.

## The middle frame creates a measurable source correlation

Take \(G=g_0P_0+gP_1\), \(g_0,g>0\), and fix \(U=V=I\). In the normalized two-edge law from (TG9), let \(Y_\xi=\|P_1\xi\|^2\), \(Y_\eta=\|P_1\eta\|^2\). Given \(W\), the preparations are independent with the common covariance \(Q(I,W)^{-1}\). Their middle-frame law is
\[
\pi_{\rm br}(dW)=
\frac{K_\beta(I,W)^2}{\mathsf T^2(I,I)}\,dW.
\tag{TG14}
\]
For an \(SU(2)\) representative with angle \(\theta\),
\[
b(W)=\operatorname{Tr}[P_1Q(I,W)^{-1}]
=g+\frac{2g}{1+2\beta g\sin^2\theta}.
\]
Conditional independence and total covariance give
\[
\boxed{\operatorname{Cov}(Y_\xi,Y_\eta)
=\operatorname{Var}_{\pi_{\rm br}}b(W)>0.}
\tag{TG15}
\]
Equivalently, mark the two preparations by \(sP_1,tP_1\) in (TG13); then \(\partial_s\partial_t\log\mathcal Z^{(2)}|_{s=t=0}\) is the same positive variance. The generated correlation is in quadratic observables; centered linear cross-covariance remains zero.

This establishes positive finite transfer, exact marked gluing and a nontrivial correlation generated by composition. It does not show that the lost angular or central channels are physically dispensable, construct a spatial cycle grammar, or select the duration and continuum limits required for Yang–Mills or cosmology.
