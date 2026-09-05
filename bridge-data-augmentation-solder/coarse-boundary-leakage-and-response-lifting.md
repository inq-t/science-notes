# Coarse-Boundary Leakage and Response Lifting

A coarse bridge can acquire an artificial response floor by discarding boundary information that still predicts the retained interior. To lift a coarse estimate to the complete fine observable carrier, subtract that hidden prediction and control the discarded interior conditionally on both the retained core and the full boundary. A sharp positive-contraction theorem then multiplies the two genuine response constants. Iteration gives an explicit budget for what must survive through a diverging number of RG steps.

**Status: [EXACT SAME-LAW IDENTITIES AND CONDITIONAL LIFTING THEOREM]; [EXACT] finite counterexample and operator sharpness; [OPEN] uniform Yang--Mills bounds for the resulting multiscale budget.** All coarse laws below are actual pushforwards of one specified fine joint law.

## Coarsening the boundary can hide a predictor

Let \((Y,Z)\) be the fine core and boundary variables, with deterministic retained variables
\[
X=q(Y),\qquad W=r(Z).
\tag{BL1}
\]
Use their actual marginal \(L^2\) norms and work on centered carriers. Let \(J_X:\mathcal H_X\to\mathcal H_Y\) and \(J_W:\mathcal H_W\to\mathcal H_Z\) be the pullback isometries. Define
\[
Kf=\mathbb E[f(Y)\mid Z],\quad
B=I-K^*K,\quad
P=J_XJ_X^*,\quad Q=I-P,\quad R=J_WJ_W^*.
\tag{BL2}
\]
The actual coarse predictor is \(K_c=J_W^*KJ_X\). Its bridge response \(B_c=I-K_c^*K_c\) obeys
\[
\boxed{
J_X^*BJ_X=B_c-L^*L,\qquad
L=(I-R)KJ_X.}
\tag{BL3}
\]
Indeed split \(KJ_X\) orthogonally into its \(R\) and \(I-R\) parts. The operator \(L\) measures prediction from fine boundary data that is invisible to the retained boundary. It is not discarded core entropy or a coupling between coordinate gradients.

If
\[
B_c\ge\kappa_c I_{\mathcal H_X},\qquad
\|L\|\le\eta,\qquad
a:=\kappa_c-\eta^2>0,
\tag{BL4}
\]
then \(PBP\ge aP\). With no boundary coarsening, \(R=I\) and \(\eta=0\). Dropping boundary data may improve \(B_c\); it cannot justify dropping \(L^*L\).

## Control discarded distinctions with the complete conditioning data

Require, for every square-integrable fine observable \(f(Y)\),
\[
\boxed{
\mathbb E\operatorname{Var}(f(Y)\mid X,Z)
\ge b\,\mathbb E\operatorname{Var}(f(Y)\mid X),
\qquad 0<b\le1.}
\tag{BL5}
\]
This is a conditional bridge estimate inside the fibers of \(q\). It is not an ordinary fiber Poincare inequality, and it does not follow merely because those fibers are connected or their chosen diffusion mixes quickly.

Conditioning on \((X,Z)\) retains at least as much information as conditioning on \(Z\). Consequently (BL5) gives, on the complete fine carrier,
\[
\langle f,Bf\rangle
=\mathbb E\operatorname{Var}(f(Y)\mid Z)
\ge b\|Qf\|^2.
\tag{BL6}
\]
This is the full operator inequality \(B\ge bQ\), not just a lower bound on \(QBQ\). Since \(0\le B\le I\), [[two-slice-innovation-geometry/projection-conditioned-coercivity|projection-conditioned coercivity]] now proves
\[
\boxed{
B\ge b(\kappa_c-\eta^2)I_{\mathcal H_Y}.}
\tag{BL7}
\]
No cross-block norm is additionally needed: the stronger conditioning in (BL5) already controls cancellation between retained and discarded directions.

One way to prove (BL5) is to apply [[conditional-fisher-coercivity/inq|conditional Fisher coercivity]] to the actual law of the residual core and \(Z\), conditional on each \(X=x\). If that context law has Poincare constant \(\lambda_x\), and the conditional residual-core family has Fisher tensor at most \(C_x\) times its declared context metric, then
\[
b\ge\mathop{\mathrm{ess\,inf}}_x
\frac{\lambda_x}{\lambda_x+C_x}.
\tag{BL8}
\]
The required common fiber coordinates, reference measures, derivatives and domains must exist. A singular quotient is not covered merely by naming its fibers. In particular, (BL8) concerns \(Z\mid X=x\) and the residual core conditioned on \((X,Z)\), not the unconditioned boundary law or the original fine action before integration.

## A full-support failure of coarse inference

Let \(Y=(X,U)\), \(Z=(V,W)\), with all variables signs. Relative to four independent uniform signs, take joint density
\[
1+rXV,\qquad 0<r<1.
\tag{BL9}
\]
Retain \(X,W\). They are independent, so \(\kappa_c=1\). The discarded \(U\) is independent even conditional on \(X,Z\), giving \(b=1\). Nevertheless \(V\) predicts \(X\) with correlation \(r\), and
\[
\eta=r,\qquad
\inf\sigma(B|_{\mathcal H_Y})=1-r^2.
\tag{BL10}
\]
Thus a perfect coarse floor and perfect discarded-core floor coexist with a fine floor tending to zero. The missing term in (BL3) accounts for the failure exactly.

## A multiscale budget on the actual joint tower

Suppose deterministic core and boundary maps define consistent joint laws at levels \(j=0,\ldots,J\). Apply (BL4)--(BL5) at each level, always using the complete centered carriers and actual conditional laws. If \(\kappa_j\) denotes the optimal bridge floor, then
\[
\kappa_j\ge b_j(\kappa_{j+1}-\eta_j^2)
\tag{BL11}
\]
whenever the retained lower bound is positive. Iterating yields
\[
\boxed{
\kappa_0\ge
\left(\prod_{i<J}b_i\right)\kappa_J
-\sum_{j<J}
\left(\prod_{i\le j}b_i\right)\eta_j^2.}
\tag{BL12}
\]
A computable version starts with a terminal lower certificate and assigns each preceding certificate from the right side of (BL11), checking positivity. Arbitrary independently chosen lower certificates need not satisfy the recursion.
A fixed \(b<1\) repeated indefinitely erodes this certificate. Uniformly positive finite-step bounds alone do not survive \(J\to\infty\).

For a sufficient explicit budget, suppose
\[
\kappa_J\ge\kappa_T>0,\qquad
b_j\ge(1+c_j)^{-1},\quad c_j\ge0,\qquad
\sum_{j<J}c_j\le C_*,\qquad
\sum_{j<J}\eta_j^2\le E_*.
\]
Then
\[
\boxed{\kappa_0\ge e^{-C_*}\kappa_T-E_*}
\tag{BL13}
\]
provided the right side is positive. Positivity of this total budget also keeps the intermediate lower certificates positive. The coefficients \(c_j\) may be supplied by the ratios \(C_x/\lambda_x\) in (BL8); they are not freely chosen response weights.

For example, if the block-length ratio is \(L_0>1\), \(A,D\ge0\), and
\[
c_j\le A L_0^{-p(J-j)},\qquad
\eta_j^2\le D L_0^{-q(J-j)},\qquad p,q>0,
\]
then the sums are bounded by \(A/(L_0^p-1)\) and \(D/(L_0^q-1)\), independently of \(J\). This is a scale-relative sufficient estimate to prove, not a decay law derived here.

The [[rg-covariance-residue/inq|covariance-residue route]] instead controls discarded physical correlations and retained source tails. The present theorem targets the stronger complete bridge response directly. It does not equate a small conditional Fisher score with spacetime correlation decay, nor derive entry into a coercive infrared regime.

For probabilistic blocking, (BL1) is not a deterministic subalgebra relation on the original carrier. [[regional-randomization-and-response-lifting|Regional randomization]] supplies an extension on the enlarged joint law when the regional kernels use no shared auxiliary information. It preserves the complete original floor and uses regional suffix algebras for a Markov tower. Its discarded-core test must cover functions of both the fine field and its readout; random readout variables are not silently treated as functions of the fine field.

A continuum application still needs a uniform positive budget at fixed physical slab width, a nontrivial limiting joint law, and the separate transfer and OS/Poincare reconstruction. [[bridge-floor-under-joint-limits|Joint-limit persistence]] then passes the proved bridge floor; it does not prove these missing inputs.

[[relative-boundary-leakage|Relative boundary leakage]] gives a complementary lifting theorem: a conditional-Fisher bound on the discarded boundary fibers can prove \(L^*L\le r_{\partial}J_X^*BJ_X\). The coarse floor then loses the multiplicative factor \(1/(1+r_{\partial})\), not an absolute subtraction. A finite total logarithmic loss is sufficient, with no additional smallness threshold.

[[conditional-fisher-coercivity/receipts/coarse_fisher_and_bridge_lifting_receipt.py|The finite receipt]] checks (BL3), the conditional full-space inequality, random finite joint-law lifts, the exact sign example, and the multiscale arithmetic.
