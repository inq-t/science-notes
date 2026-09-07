# Partial-Trace Clock Consistency and the Fluctuation Limit

Successive partial traces of one round purification preserve the same total dimension and the same inherited response duration. Enlarging the purification environment, however, changes the retained reference law: at fixed matrix size it concentrates at the maximally mixed state, even after normalizing the response gap to one. Rescaled state fluctuations preserve an exact finite quantum Hilbert return and a faithful positive operator representation, not pointwise matrix multiplication. Their differential response approaches an Ornstein–Uhlenbeck expression and their stationary laws approach a Gaussian. This distinguishes clock consistency, a nonzero spectral threshold and nonvanishing observable distinctions; none alone supplies a physical field limit.

## One parent fixes the duration of successive readouts

Use [[purification-descent-and-the-matrix-response|matrix purification descent]]. Initially assume integers \(K\ge d\ge2\), put \(D=dK\), and give
\[
\Psi\in S^{2D-1}\subset\mathbb C^d\otimes\mathbb C^K
\]
normalized round law and generator \(\mathcal G=\Delta_S/4\). The state readout is \(\rho=\Psi\Psi^*\), its law is \(\nu_{d,K}\), and its inherited generator is \(L_{d,K}\). On affine symbols \(f_A(\rho)=\operatorname{Tr}(\rho A)\),
\[
L_{d,K}f_A=K\operatorname{Tr}A-Df_A,\qquad
\Gamma(f_A,f_B)=f_{A\circ B}-f_Af_B.
\tag{PT1}
\]
Here \(A,B\) are Hermitian and \(A\circ B=(AB+BA)/2\). The operator acts on functions of matrix states, not directly on vectors in \(\mathbb C^d\).

Factor \(d=d_A d_B\), with \(d_A\ge2\), and let \(R(\rho)=\operatorname{Tr}_B\rho\). Regroup the very same normalized amplitude as
\[
\mathbb C^{d_A}\otimes
(\mathbb C^{d_B}\otimes\mathbb C^K),\qquad
K_A=d_BK,\qquad d_AK_A=D.
\tag{PT2}
\]
This is a real orthogonal identification of the same sphere, not a second sampling prescription. The Gram readout of the regrouped amplitude is exactly \(R(\rho)\). Consequently
\[
\boxed{R_*\nu_{d,K}=\nu_{d_A,K_A}.}
\tag{PT3}
\]
The corresponding pullback \(R^*f=f\circ R\) is an isometry between the two reference \(L^2\) spaces. Since \(f_A\circ R=f_{A\otimes I_B}\), and
\[
\operatorname{Tr}(A\otimes I_B)=d_B\operatorname{Tr}A,\qquad
(A\otimes I_B)\circ(B\otimes I_B)=(A\circ B)\otimes I_B,
\]
(PT1) gives generator intertwining on every polynomial. More strongly, both function spaces are reducing invariant subspaces of the same spherical generator: the \(U(d_BK)\)-invariant subspace is contained in the \(U(K)\)-invariant one. Thus the inherited realizations satisfy
\[
\boxed{e^{tL_{d,K}}R^*=R^*e^{tL_{d_A,K_A}},\qquad t\ge0.}
\tag{PT4}
\]
This includes the corresponding transported operator domains. No change of duration is required when part of the retained matrix is reclassified as environment.

The map, measure and intertwining identities remain valid for \(K\ge1\) on their actual rank-constrained supports. The parent state then has rank at most \(\min(d,K)\), and the marginal at most \(\min(d_A,d_BK)\), with these ranks attained almost surely under round law. A rank-deficient parent can therefore have a faithful marginal. The determinant-density and full-dimensional polynomial formulas invoked below use \(K\ge d\); they are not silently extended to a lower-rank state variety.

## Gap normalization is compatible with this marginalization

The inherited complete spectrum in the full-rank family is
\[
\lambda_\ell=\ell(\ell+D-1),\qquad \ell=0,1,\ldots.
\]
Its constant ground space is one-dimensional and its centered gap is exactly \(D\), attained by traceless affine symbols. Define
\[
\widehat L_{d,K}=D^{-1}L_{d,K}.
\tag{PT5}
\]
Then \(-\widehat L_{d,K}\) has gap one, and (PT4) holds for these normalized generators too, because (PT2) preserves \(D\). This identifies a consistent response timeweight across readouts of one parent. It does not identify \(D\), or the normalized duration, with physical time or cosmic scale.

At \(d=2,K=4\), \(D=8\), this is the matrix return in [[octonionic-hopf-descent-and-the-complex-purification|the octonionic Hopf comparison]]. That comparison fixes a common parent for those maps, not a preferred environment size for all applications.

## A fixed clock gap need not preserve the ensemble distinctions

Round complex-sphere fourth moments give, for Hermitian \(A,B\),
\[
\mathbb E_{\nu_{d,K}} f_A=\frac{\operatorname{Tr}A}{d},\qquad
\boxed{\mathbb E_{\nu_{d,K}} f_Af_B
=\frac{K\operatorname{Tr}A\,\operatorname{Tr}B+\operatorname{Tr}(AB)}
{d(D+1)}.}
\tag{PT6}
\]
For example, the fourth-moment tensor of the normalized parent vector is
\((I+\mathrm{Swap})/[D(D+1)]\); applying it to
\((A\otimes I_K)\otimes(B\otimes I_K)\) gives the formula.

For traceless \(A\), the variance is therefore
\[
\operatorname{Var}_{\nu_{d,K}}f_A
=\frac{\operatorname{Tr}A^2}{d(D+1)}.
\tag{PT7}
\]
At fixed \(d\), letting \(K\to\infty\) gives
\[
\mathbb E\left\|\rho-\frac Id\right\|_{\mathrm{HS}}^2
=\frac{d^2-1}{d(D+1)}\longrightarrow0.
\tag{PT8}
\]
Thus \(\nu_{d,K}\) converges weakly to the point mass at \(I/d\). Because the state body is compact, every fixed continuous function of \(\rho\) converges in law, and in mean square against these varying laws, to its value at \(I/d\). Normalizing the gap has not prevented this concentration.

This is **ensemble variance of the expectation symbol**, not quantum variance within a state. For traceless \(A,B\), the latter symmetrized covariance is
\[
C_\rho(A,B)=\operatorname{Tr}\rho(A\circ B)-f_Af_B
\ \longrightarrow\ \frac{\operatorname{Tr}(AB)}d.
\tag{PT9}
\]
In particular a nonzero traceless observable still has positive quantum variance in \(I/d\). The finite algebra \(M_d(\mathbb C)\) has not become trivial. What collapses is the classical reference distribution of its density parameters. The normalized affine channel also remains nontrivial:
\[
e^{t\widehat L_{d,K}}f_A
=\frac{\operatorname{Tr}A}{d}
+e^{-t}\left(f_A-\frac{\operatorname{Tr}A}{d}\right).
\]
The same formula can act on expectation symbols while their reference ensemble fluctuations shrink.

## The rescaled fluctuations have an exact response

Choose a real basis \(T_1,\ldots,T_r\), \(r=d^2-1\), of traceless Hermitian matrices. Put
\[
G_{ij}=\frac{\operatorname{Tr}(T_iT_j)}d,\qquad
T_i\circ T_j=G_{ij}I+\sum_k c_{ij}^{\,k}T_k,
\]
\[
\xi_i=\sqrt{D+1}\,f_{T_i}.
\tag{PT10}
\]
Then \(G>0\), \(\mathbb E\xi_i=0\), and (PT6) gives the exact, \(K\)-independent identity
\[
\mathbb E(\xi_i\xi_j)=G_{ij}.
\tag{PT11}
\]
Transport \(\widehat L_{d,K}\) to these coordinates. Its drift is exactly \(-\xi\), and its co-metric is
\[
\boxed{
a^{(K)}_{ij}(\xi)
=\frac{D+1}{D}G_{ij}
+\frac{\sqrt{D+1}}{D}\sum_k c_{ij}^{\,k}\xi_k
-\frac{\xi_i\xi_j}{D}.
}
\tag{PT12}
\]
Indeed \(\Gamma_{\widehat L}(\xi_i,\xi_j)=(D+1)\Gamma_L(f_{T_i},f_{T_j})/D\); substitution of (PT10) proves every term. Hence the exact coordinate expression is
\[
\mathcal A_KF
=\sum_{ij}a^{(K)}_{ij}\partial_i\partial_jF
-\sum_i\xi_i\partial_iF.
\tag{PT13}
\]
The rescaled state bodies eventually contain every fixed compact set of \(\mathbb R^r\): any bounded traceless perturbation divided by \(\sqrt{D+1}\) preserves positivity of \(I/d\) for sufficiently large \(K\). On each such compact set, all coefficients of (PT13) converge to those of
\[
\boxed{\mathcal A_\infty F=G:\nabla^2F-\xi\cdot\nabla F.}
\tag{PT14}
\]
This Ornstein–Uhlenbeck generator has invariant centered Gaussian law with covariance \(G\). Its normalization uses the full second-order term \(G:\nabla^2\), not one half of it.

## The fluctuation variables have an exact operator return

The [[matrix-symbol-realization-and-the-clock-algebra|matrix-symbol realization]] sends \(I\) to the constant function and each \(T_i\) exactly to \(\xi_i\). It realizes the supplied \(M_d(\mathbb C)\) faithfully as positive operators on the affine \(L^2\) subspace, with its matrix norm and tracial state, and intertwines the normalized depolarizing channel. It also respects the same partial-trace identifications (PT2)–(PT4).

This is a genuine finite operator return despite concentration of the ensemble law. The represented matrices are not pointwise multiplication operators. The shared note proves both that distinction and the separate failure of this global Hilbert clock to preserve the matrix algebra or support a bounded-range spatial interpretation across arbitrarily separated tensor factors. No such spatial structure is assumed in the fluctuation limit below.

## The stationary Gaussian limit can be proved separately

Let \(z_1,\ldots,z_K\) be independent standard complex Gaussian vectors in \(\mathbb C^d\), with \(\mathbb E z_\alpha z_\alpha^*=I\). The Gaussian integration device in matrix purification gives exactly
\[
W=\sum_{\alpha=1}^Kz_\alpha z_\alpha^*,\qquad
\rho=W/\operatorname{Tr}W.
\]
For any fixed traceless Hermitian \(T\), define
\[
Y_K=\frac1{\sqrt D}\sum_{\alpha=1}^Kz_\alpha^*Tz_\alpha.
\]
The elementary Gaussian integral yields
\[
\log\mathbb E e^{iuY_K}
=-K\operatorname{Tr}\log\left(I-\frac{iuT}{\sqrt D}\right)
=-\frac{u^2}{2d}\operatorname{Tr}T^2+O(K^{-1/2}).
\tag{PT15}
\]
The linear term vanishes because \(\operatorname{Tr}T=0\). Also
\(\operatorname{Tr}W/D\to1\) in probability, while
\[
\sqrt{D+1}\,f_T
=\frac{\sqrt{D(D+1)}}{\operatorname{Tr}W}\,Y_K.
\]
The prefactor tends to one. Applying this argument to every linear combination of the \(T_i\) proves joint convergence of \(\xi\) to \(N(0,G)\). This establishes the stationary fluctuation limit independently of the coefficient calculation.

The exact finite laws, their stationary weak limit and the local coefficient convergence are distinct results. They alone do not prove dynamical convergence. [[purification-response-normalization-and-the-full-clock-limit|The full-clock theorem]] supplies that missing step using all polynomial moments and complete degree eigenspaces: polynomial-compatible Hilbert comparisons give norm-resolvent convergence, positive-time heat convergence and strong unitary-clock convergence. Neither argument asserts convergence of path measures or an interacting physical field theory.

The fluctuation rescaling also changes the tested distinctions: the matrices representing \(\xi_i\) as affine symbols have norms growing like \(\sqrt D\). It is not the preservation of every fixed bounded observable at finite amplitude. [[directed-analytic-realization/purification-fluctuation-and-the-oscillator-return|The limiting oscillator algebra]] is a different observable carrier, constructed from all polynomial fluctuations and their conjugate response, not the earlier matrix-symbol algebra under a new name.

The constructive lesson is a paired test for a proposed realization limit: preserve a correctly typed response duration **and** exhibit nonvanishing distinctions on the intended observable carrier. This family preserves duration under partial trace. As its environment grows, preserving nonvanishing ensemble fluctuations of expectation symbols in the reference \(L^2\) spaces requires the explicit fluctuation rescaling; the unrescaled symbols concentrate. This is not a loss of fixed represented quantum observables: their matrix norm and tracial within-state variance remain fixed. The distinction between those carriers is a concrete constraint on a future physical realization, not a Yang–Mills mass-gap derivation.
