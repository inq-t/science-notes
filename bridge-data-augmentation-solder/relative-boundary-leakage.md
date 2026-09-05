# Relative Boundary Leakage

Prediction hidden by a coarse boundary can be bounded relative to the fine uncertainty that remains, rather than by an absolute error norm. Conditional Fisher geometry on the discarded boundary fibers supplies this comparison. Together with conditional control of discarded interior observables, it gives a multiplicative response-lifting theorem whose losses need only have a finite total logarithmic budget.

**Status: [EXACT CONDITIONAL THEOREM AND SHARP GAUSSIAN CALIBRATION]; [OPEN] for a uniform continuum Yang--Mills tower.** Every conditional law is taken from the same joint law; no physical time or energy is assumed.

## Measure hidden prediction against the remaining response

Use the fine core \(Y\), fine boundary \(Z\), and deterministic retained variables \(X=q(Y)\), \(W=r(Z)\) of [[coarse-boundary-leakage-and-response-lifting|same-law response lifting]]. In its notation,
\[
A:=J_X^*BJ_X,\qquad B_c=A+L^*L,\qquad
L=(I-R)KJ_X.
\tag{RL1}
\]
For a retained observable \(f(X)\), these forms are
\[
\begin{aligned}
\langle f,Af\rangle&=\mathbb E\operatorname{Var}(f(X)\mid Z),\\
\|Lf\|^2&=\mathbb E\operatorname{Var}(\mathbb E[f(X)\mid Z]\mid W).
\end{aligned}
\tag{RL2}
\]
The second quantity is how much extra prediction the fine boundary provides beyond \(W\). Suppose, for every retained observable,
\[
\boxed{L^*L\le r_{\partial}A,\qquad 0\le r_{\partial}<\infty.}
\tag{RL3}
\]
Then
\[
\boxed{A\ge\frac{1}{1+r_{\partial}}B_c.}
\tag{RL4}
\]
Unlike an absolute bound \(\|L\|^2\le\eta^2\), (RL3) compares the loss to the response in the same direction. It requires no inequality \(r_{\partial}<1\) and no subtraction smaller than the coarse floor. It is a different, potentially stronger hypothesis, not a consequence of a small absolute leakage norm.

## A geometric certificate on the actual boundary fibers

Disintegrate the actual boundary law as \(\nu(dz)=\nu_W(dw)\nu_w(dz)\), where \(\nu_w\) lives on \(r^{-1}(w)\). Assume these fibers have declared smooth metrics \(g_w\), reference measures and closed gradient forms. For almost every \(w\), require
\[
\operatorname{Var}_{\nu_w}g
\le\lambda_w^{-1}\int|d_{\!v}g|_{g_w^{-1}}^2\,d\nu_w,
\qquad \lambda_w>0.
\tag{RL5}
\]
Here \(d_{\!v}\) varies the discarded boundary while holding \(W\) fixed. Use the normalized score of the actual conditional family \(Y\mid Z=z\), restricted to these vertical tangents. It suffices that its Fisher tensor obey
\[
I_z^{\,Y\mid Z}\big|_{\ker dr}\le C_w g_w,\qquad
r_{\partial}:=\mathop{\mathrm{ess\,sup}}_w\frac{C_w}{\lambda_w}<\infty.
\tag{RL6}
\]
A smaller bound for \(X\mid Z\) is also sufficient if that conditional score family is constructed. A \(Z\)-independent readout \(q\) projects scores, so its Fisher tensor cannot exceed that of \(Y\mid Z\). A moving readout requires the extra terms in [[conditional-fisher-coercivity/coarse-graining-and-moving-context|Fisher transport]].

For \(g(z)=\mathbb E[f(X)\mid Z=z]\), the joint score-map bound gives
\[
|d_{\!v}g|_{g_w^{-1}}^2
\le C_w\operatorname{Var}(f(X)\mid Z=z).
\tag{RL7}
\]
Apply (RL5), then integrate over \(w\). Equations (RL2)--(RL3) follow. This is [[conditional-fisher-coercivity/inq|conditional Fisher coercivity]] applied inside each boundary fiber, not a new assumption that boundary and interior are independent.

The differentiation must be valid on a dense test class of retained observables, with their conditional means in the fiber form domains. Require a measurable direct-integral family of closed forms and the displayed uniform ratio. The resulting bounded inequality extends to all \(L^2\) observables by density and contraction of conditional expectations. If fiber coordinates change the hidden reference measure, include the Jacobian in the normalized score. A singular gauge quotient or moving support is not covered by merely naming its fibers.

An intrinsic alternative is a uniform positive fiber Poincare constant \(\lambda_{F,w}\) in the inverse conditional-Fisher form on admissible conditional means; then \(r_{\partial}=\mathop{\mathrm{ess\,sup}}_w\lambda_{F,w}^{-1}\) works. The background-metric branch (RL5)--(RL6) permits singular Fisher tensors. Its ratio is unchanged by a regular reparameterization or a common constant rescaling of each fiber metric: both \(C_w\) and \(\lambda_w\) transform together.

## Lift to every fine observable

In addition to (RL3), assume the actual coarse bridge has a normalized floor certificate \(0<\kappa_c\le1\) and the discarded interior satisfies
\[
\mathbb E\operatorname{Var}(F(Y)\mid X,Z)
\ge b\,\mathbb E\operatorname{Var}(F(Y)\mid X),
\qquad 0<b\le1,
\tag{RL8}
\]
for every fine observable. This gives the full inequality \(B\ge bQ\), not merely a compression to discarded observables. Since \(0\le B\le I\), [[two-slice-innovation-geometry/projection-conditioned-coercivity|projection-conditioned coercivity]] and (RL4) imply
\[
\boxed{\kappa_{\rm fine}\ge
\frac{b}{1+r_{\partial}}\kappa_c.}
\tag{RL9}
\]
The two factors answer different questions. The coefficient \(b\) prevents the full boundary from perfectly predicting discarded interior distinctions conditional on \(X\). The factor \(1/(1+r_{\partial})\) controls prediction of retained distinctions hidden by discarding part of that boundary.

[[predictive-sufficient-interfaces|Approximate predictive sufficiency]] gives an alternative when a rare conditional fiber makes the \(b\)-certificate too severe. If the complete discarded-prediction norm obeys \(\|KQ\|^2\le\delta\), then \(\kappa_{\rm fine}\ge\kappa_c/(1+r_\partial)-\delta\). This needs an additive margin; it is not the same loss budget as (RL9).

## The relative factor is sharp

Let \(W,V,\varepsilon\) be independent centered Gaussians with variances \(a,v,\sigma^2>0\), and set
\[
X=W+V+\varepsilon,\qquad Z=(W,V).
\tag{RL10}
\]
Retain \(X,W\). On a \(W\)-fiber, \(\lambda_w=1/v\), while the conditional \(X\)-family has vertical Fisher information \(1/\sigma^2\). Hence \(r_{\partial}=v/\sigma^2\).

The Gaussian conditional-expectation spectrum gives
\[
\kappa_c=\frac{v+\sigma^2}{a+v+\sigma^2},\qquad
\kappa_{\rm fine}=\frac{\sigma^2}{a+v+\sigma^2}
=\frac{\kappa_c}{1+r_{\partial}}.
\tag{RL11}
\]
The first Hermite observable \(f(X)=X\) saturates the comparison. Appending an independent discarded interior variable \(U\), with \(Y=(X,U)\), gives (RL8) with \(b=1\) without changing either floor. As \(\sigma^2\) tends to zero, the relative cost diverges exactly when fine prediction becomes almost perfect.

## A multiplicative continuum budget

For a deterministic, consistently pushed-forward tower, let the hypotheses hold at each level with
\[
b_j\ge(1+c_j)^{-1},\quad c_j\ge0,\qquad r_j\ge0.
\]
Starting from a terminal lower certificate \(\kappa_J\ge\kappa_T>0\), assign preceding certificates using (RL9). Then
\[
\boxed{\kappa_0\ge
\kappa_T\prod_{j<J}\frac1{(1+c_j)(1+r_j)}.}
\tag{RL12}
\]
If, uniformly in regulator and depth,
\[
\sum_{j<J}\big[\log(1+c_j)+\log(1+r_j)\big]\le M<\infty,
\]
then \(\kappa_0\ge e^{-M}\kappa_T>0\). Uniformly bounded sums of \(c_j+r_j\) suffice. No smallness condition \(M<1\) is needed; a fixed positive loss repeated indefinitely still erodes the certificate to zero.

The coefficients must come from the actual conditional laws and metrics at each level. Arbitrary readout noise, deleted predictors, or freely normalized response weights cannot be selected to manufacture the bound. [[regional-randomization-and-response-lifting|Regional randomization]] extends the theorem to probabilistic RG on a specified enlarged joint carrier. Its private regional kernels preserve the complete original floor exactly, and its discarded-core condition covers every enlarged-core observable.

[[collared-quasi-factorization-and-surface-response/fisher-collar-bound-for-wilson-laws|Coordinate deletion in a strong-coupling Wilson law]] supplies a concrete finite-regulator instance. It does not establish a summable loss along the weak-bare-coupling continuum trajectory. Once such a floor and an identified limiting law exist, [[bridge-floor-under-joint-limits|joint-limit persistence]] applies; physical mass still requires the separate vacuum-slab and translation reconstruction.

[[conditional-fisher-coercivity/receipts/relative_leakage_and_compact_gauge_receipt.py|The finite receipt]] checks the operator comparison on actual finite joint laws, Gaussian sharpness, and multiplicative budgets. It does not test a Yang--Mills continuum.
