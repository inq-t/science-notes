# Exact-Source Locality Without a Full One-Form Gap

A conditional susceptibility can be exponentially localized even when the full one-form operator has no positive spectral floor. The source of a covariance response is an exact one-form, and only that invariant sector needs a gap. Spatial weights act on the larger one-form space, where nonnegativity and a bounded locality defect suffice. Splitting the auxiliary evolution into short and long times keeps these two requirements separate.

**Status: [EXACT CONDITIONAL THEOREM], with a direct proof.** This refines the operator route in [[inq|auxiliary response localization]]. It does not derive a conditional Poincare constant for Yang--Mills.

## Carrier and the two bounds

Let \(X=\prod_{e\in E}M_e\) be a finite product of closed connected Riemannian manifolds, with smooth positive probability law
\[
d\mu=Z^{-1}e^{-U}\,d\mathrm{vol}.
\tag{ES1}
\]
Use the weighted de Rham complex on configuration space:
\[
L_0=d_\mu^*d,\qquad
K=L_1=dd_\mu^*+d_\mu^*d,\qquad
\mathcal E=\overline{\operatorname{Ran}d}.
\tag{ES2}
\]
The operators have their compatible self-adjoint realizations. The full \(K\) is nonnegative. The intertwining \(dL_0=Kd\) makes \(\mathcal E\) a reducing subspace. A scalar Poincare inequality with constant \(\rho>0\) gives
\[
K|_{\mathcal E}\ge\rho I.
\tag{ES3}
\]
This also follows from the unitary identification \(dL_0^{-1/2}\) between centered scalar functions and \(\mathcal E\). The theorem below only needs (ES3) on an invariant sector containing the actual exact sources.

Give the factor labels a distance \(d_E\), choose a spatial reference length \(b>0\), and write \(\chi_A\) for projection onto the cotangent summands labeled by \(A\subset E\). For a source set \(F\), define
\[
(W_{\theta,F}\omega)_e
=e^{\theta d_E(e,F)/b}\omega_e,\qquad \theta>0.
\tag{ES4}
\]
Assume these weights preserve the operator domain and, uniformly in \(F\),
\[
\|W_{\theta,F}KW_{\theta,F}^{-1}-K\|\le M_\theta,
\qquad 0<M_\theta<\infty.
\tag{ES5}
\]
A positive upper bound can be used even if the actual defect vanishes. For the finite compact product, the weights are bounded parallel bundle endomorphisms. The substantive requirement for a family of volumes or regulators is uniformity of \(M_\theta\), not boundedness in one finite volume.

## The short-time/long-time theorem

Let \(q=dG\) have factor support in \(F\), and let \(r=d_E(A,F)\). Then
\[
\boxed{
\|\chi_A(K|_{\mathcal E})^{-1}dG\|_2
\le
\left(\frac1\rho+\frac1{M_\theta}\right)
\exp\!\left[
-\frac{\theta\rho}{\rho+M_\theta}\frac r b
\right]\|dG\|_2.}
\tag{ES6}
\]
No positive floor on the full one-form space is assumed.

**Proof.** Since the original source lies in the invariant exact sector,
\[
\|\chi_Ae^{-tK}q\|_2\le e^{-\rho t}\|q\|_2.
\tag{ES7}
\]
On the full space, nonnegativity of \(K\) and bounded perturbation by (ES5) give
\[
\|W_{\theta,F}e^{-tK}W_{\theta,F}^{-1}\|
\le e^{M_\theta t}.
\]
Because \(W_{\theta,F}q=q\), this implies the different bound
\[
\|\chi_Ae^{-tK}q\|_2
\le e^{-\theta r/b+M_\theta t}\|q\|_2.
\tag{ES8}
\]
Integrate the minimum of (ES7) and (ES8), splitting at
\[
T=\frac{\theta r/b}{\rho+M_\theta}.
\]
The integral is exactly
\[
\left(\frac1\rho+\frac1{M_\theta}\right)
e^{-\theta\rho r/[b(\rho+M_\theta)]}
-\frac{e^{-\theta r/b}}{M_\theta}.
\tag{ES9}
\]
Since \((K|_{\mathcal E})^{-1}q=\int_0^\infty e^{-tK}q\,dt\), dropping the last nonpositive term proves (ES6). At \(r=0\), the sharper expression (ES9) is \(1/\rho\). \(\square\)

This is a static consequence of two estimates on an auxiliary evolution. If \(\rho=\rho_0b^{-2}\) and \(M_\theta=M_0b^{-2}\), its prefactor is \(b^2(\rho_0^{-1}+M_0^{-1})\), while the dimensionless decay rate per block is
\[
\sigma_\theta b=\frac{\theta\rho_0}{\rho_0+M_0}.
\tag{ES10}
\]
An auxiliary-clock rescaling multiplies both generator rates by the same factor and leaves this exponent unchanged. Identifying it with a physical inverse correlation length still requires actual spatial distance and the reconstruction hypotheses in [[inq|the parent theorem]].

## Covariance and conditional score transport

For smooth complex functions, with the inner product conjugate-linear in its first slot,
\[
\operatorname{Cov}_\mu(F,G)
=\langle dF,(K|_{\mathcal E})^{-1}dG\rangle_{L^2(\mu)}.
\tag{ES11}
\]
Indeed, write the centered Poisson solution \(u=L_0^{-1}(G-\mu G)\); then \(du=(K|_{\mathcal E})^{-1}dG\), and integration by parts proves (ES11). Consequently
\[
|\operatorname{Cov}_\mu(F,G)|
\le
\left(\rho^{-1}+M_\theta^{-1}\right)
e^{-\sigma_\theta d_E(\operatorname{supp}dF,\operatorname{supp}dG)}
\|dF\|_2\|dG\|_2.
\tag{ES12}
\]
For a conditional potential \(U_B\), the actual real score
\(\ell_h=\partial_BU_B[h]\) enters
\[
\partial_B\mathbb E_BF[h]
=\mathbb E_B(\partial_BF[h])
-\operatorname{Cov}_B(\ell_h,F).
\tag{ES13}
\]
Thus the inverse is applied to the exact local score \(d\ell_h\), not to an arbitrary one-form. [[rg-covariance-residue/conditioned-source-transport|Conditioned source transport]] owns the iteration and renormalized-source estimates that must follow.

## Why a weighted reduced inverse is not the proof

Spatial weights generally fail to preserve exactness. Already in a two-coordinate chart, \(f=x_1x_2\) gives
\[
df=x_2\,dx_1+x_1\,dx_2,\qquad
d(Wdf)=(w_2-w_1)\,dx_1\wedge dx_2.
\tag{ES14}
\]
Conjugating \(K|_{\mathcal E}\) by \(W\) as though \(W\mathcal E=\mathcal E\) is therefore unjustified. The proof above uses the full operator for weighted growth and the unweighted exact sector for decay.

Nor does (ES6) prove a block bound for arbitrary localized one-forms followed by projection to \(\mathcal E\): that projection can itself be nonlocal. The scope is localized exact sources. It is precisely the scope needed for (ES11)--(ES13).

On a product carrier, the weighted Weitzenbock expression
\[
K=\nabla_\mu^*\nabla+\operatorname{Ric}+\operatorname{Hess}U
\tag{ES15}
\]
shows how to check (ES5). Parallel scalar factor weights commute with the product connection, drift, and factorwise Ricci tensor. Only the off-diagonal potential Hessian remains. [[rg-covariance-residue/nonlinear-conditional-gauge-response|The normalized compact gauge law]] supplies an explicit such bound.

[[library/witten-laplacian-methods-for-the-decay-of-correlations/inq|Lo's weighted Witten analysis]] is a primary precedent for converting one-form response into correlation decay; its weighted coercivity hypothesis must not be replaced by positivity of a non-self-adjoint operator's spectrum. [[library/witten-laplacian-on-a-lattice-spin-system/inq|Shigekawa's lattice-spin estimates]] provide full positive-degree lower bounds under their assumptions. Neither source is being credited with the exact-source proof written here.

[[receipts/exact_source_locality_receipt.py|The finite Hilbert-complex receipt]] tests the split estimate on a cycle incidence complex whose one-form Laplacian has a harmonic kernel. Its exact-sector gap shrinks with cycle size: the receipt checks the theorem's sector logic, not a volume-uniform physical gap.
