# Conditional Fisher Geometry Under Coarse-Graining

A fixed readout can only decrease the Fisher information that a hidden conditional law carries about its retained context. With that context and its prior unchanged, this improves the inverse-Fisher certificate on the retained observable family. It does not recover omitted fine observables. If the readout itself uses the context being varied, an additional channel score changes the information balance; normalization does not remove that term.

**Status: [EXACT] under the stated regularity and common-domain hypotheses; [OPEN] for uniform control through a full Yang--Mills RG trajectory.** This note applies the score identities to [[inq|conditional Fisher coercivity]]; the [[scale-score-connection/inq|scale-score connection]] remains the owner of moving-channel transport.

## Hold the context fixed while changing the hidden readout

Start with \(\nu(dz)\beta_z(dy)\). Let \(Q(dx\mid y)\) be independent of \(z\), and let \(\alpha_z=\beta_zQ\). Under dominated differentiation or the corresponding quadratic-mean assumptions,
\[
s_X[h]=\mathbb E_z[s_Y[h]\mid X],\qquad
I_Y-I_X
=\mathbb E_z\operatorname{Cov}_z(s_Y\mid X)\ge0.
\tag{FG1}
\]
The covariance is a tensor on the same context tangent space. This follows by differentiating the pushed-forward law and applying total covariance to its normalized score. [[library/a-note-on-insufficiency-and-the-preservation-of-fisher-information/inq|Pollard's Theorem 7]] supplies the quadratic-mean fixed-statistic result; a fixed Markov kernel is treated by adjoining its output and then projecting.

If \(I_X,I_Y\) are positive definite, then
\[
I_X^{-1}\ge I_Y^{-1},\qquad
\mathcal E_{F,X}\ge\mathcal E_{F,Y}.
\tag{FG2}
\]
The prior \(\nu\), the context coordinates and the observables tested by these forms have not changed. Compatible closed realizations are required. Closures of the two ordered forms on a common dense test core give
\(\operatorname{Dom}\mathcal E_{F,X}\subseteq\operatorname{Dom}\mathcal E_{F,Y}\) and preserve their order. Thus a Poincare floor for \(\mathcal E_{F,Y}\) transfers to \(\mathcal E_{F,X}\) on its domain.

Rank loss does not permit naive Moore--Penrose inverse order. Although \(\operatorname{diag}(1,0)\le I_2\), its pseudoinverse does not dominate \(I_2\). The coordinate-independent dual form is
\[
\mathfrak d_I(\xi)
=\sup_h\{2\operatorname{Re}\xi(h)-I(h,h)\}.
\tag{FG3}
\]
It equals \(\xi^*I^+\xi\) on covectors annihilating \(\ker I\), and is infinite otherwise. Order reversal holds for these extended dual forms. A usable finite-energy Poincare statement still needs the identifiable quotient or admissible conditional-mean domain described in the parent theorem.

For complex covectors, take the supremum over the complexified tangent space with the Hermitian extension of \(I\); for real covectors the real tangent space suffices.

## Quantitative contraction of the entire Fisher tensor

The loss in (FG1) can be bounded below when the hidden law and readout have their own uniform geometry. Suppose each actual \(\beta_z\) has Poincare constant \(\rho>0\) in a declared metric on \(Y\), and the normalized forward Fisher tensor of \(q(dx\mid y)\), with context \(y\), obeys \(J_y^q\le Cg_Y\). Keep \(q\) independent of \(z\).

Apply [[inq|conditional Fisher coercivity]] to the joint law \(\beta_z(dy)q(dx\mid y)\), with \(z\) held fixed. The two centered prediction maps are adjoints, so the reverse conditional-mean map \(T_zf=\mathbb E[f(Y)\mid X,z]\) has
\[
\|T_z\|^2\le\tau,\qquad \tau:=\frac{C}{\rho+C}.
\tag{FG3a}
\]
The output score is \(T_zs_Y[h]\). Consequently
\[
\boxed{I_X\le\tau I_Y,\qquad I_Y-I_X\ge(1-\tau)I_Y.}
\tag{FG3b}
\]
This is a tensor inequality for every original context tangent, not a sum of component estimates. The normalized score must be in the relevant \(L^2\) space, and the uniform conditional Poincare and forward-score hypotheses must hold on the actual fixed-\(z\) law. The metric and Fisher tensor defining \(C\) live on \(Y\); those in \(I_Y,I_X\) live on the original context \(Z\). These are different comparison geometries.

For normalized regional gauge readouts, [[rg-covariance-residue/regional-gauge-readouts-and-conditional-lifting|the regional lifting calculation]] supplies \(C\) by a whole path-incidence norm. This quantitative data processing controls retained parameter sensitivity; it does not recover discarded observables without a separate lifting theorem.

## Better retained response is not a fine-space gap

There is also a derivative-free statement. Put
\[
(Q_{\rm obs}f)(y)=\int f(x)Q(dx\mid y),\qquad
K_Yg=\mathbb E[g(Y)\mid Z],\quad
K_Xf=\mathbb E[f(X)\mid Z].
\]
Then \(K_X=K_YQ_{\rm obs}\). Both maps preserve centering and \(Q_{\rm obs}\) is an \(L^2\) contraction in the actual marginal norms. Consequently a fine bridge floor \(\kappa_Y\) implies
\[
I-K_X^*K_X\ge\kappa_Y I
\tag{FG4}
\]
on the centered retained carrier. This implication runs from fine to retained, not backward.

For a sharp illustration, let
\[
Z\sim N(0,v),\quad
Y\mid Z=z\sim N(z,\sigma^2),\quad
X=Y+\eta,\quad \eta\sim N(0,\tau^2)
\]
with independent readout noise. Then
\[
I_Y=\sigma^{-2},\quad I_X=(\sigma^2+\tau^2)^{-1},\qquad
\kappa_Y=\frac{\sigma^2}{v+\sigma^2},\quad
\kappa_X=\frac{\sigma^2+\tau^2}{v+\sigma^2+\tau^2}.
\tag{FG5}
\]
The retained floor stays positive as \(\sigma^2\downarrow0\) with \(v,\tau^2>0\), while the fine floor closes. No original dynamics changed.

Even equality in (FG1) only preserves the selected parameter scores. A parameter-independent auxiliary sector can be discarded without Fisher loss, including a sector equipped with an independently specified generator of arbitrarily small gap. Statistical sufficiency for \(z\) does not determine that generator. This is not a counterexample to the parent complete-\(L^2\) theorem: retaining a statistic changes the observable carrier, and an auxiliary generator is not the physical transfer of the specified joint law.

By contrast, [[bridge-data-augmentation-solder/predictive-sufficient-interfaces|complete predictive sufficiency]] factors the actual conditional law and proves an exact response decomposition on the complete observable carrier. It still does not identify an independently specified generator on discarded variables. [[gaussian-bridge-gap-calibration/predictive-rank-and-physical-separation|The Gaussian identifiable quotient]] realizes both exact sufficiency and a sharp inverse-Fisher certificate.

Pollard's stronger example of Fisher preservation without classical sufficiency uses changing supports. It must not be presented as satisfying the parent note's common-positive-support assumptions.

## A context-dependent readout has its own information

For a smooth positive normalized kernel \(q_z(x\mid y)\), let
\[
u[h]=d_z\log q_z[h].
\]
The [[scale-score-connection/inq|moving-channel score identity]] gives
\[
s_X[h]=\mathbb E_z[s_Y[h]+u[h]\mid X].
\tag{FG6}
\]
Normalization implies \(\mathbb E_z[u\mid Y]=0\), hence the complete input and channel scores are orthogonal before projection. The exact tensor balance is
\[
\boxed{
I_Y+\mathbb E_Y I_Q-I_X
=\mathbb E_z\operatorname{Cov}_z(s_Y+u\mid X)\ge0.}
\tag{FG7}
\]
There is no general inequality \(I_X\le I_Y\) here. For the preceding Gaussian model with \(X=Y+az+\eta\),
\[
I_X=\frac{(1+a)^2}{\sigma^2+\tau^2}.
\tag{FG8}
\]
Choosing \(a=-1\) removes context dependence; large \(|a|\) increases it arbitrarily. All kernels remain normalized.

For Wilson blocking, a path readout using frozen boundary links depends on the context even if its tuning coefficient is fixed. Its normalizer and any moving reference measure contribute to the derivative. Similarly, blocking \(Z\) itself changes the context carrier and prior; (FG2) no longer applies without a new comparison.

[[bridge-data-augmentation-solder/coarse-boundary-leakage-and-response-lifting|The same-law lifting theorem]] identifies what is needed in that case: account for prediction hidden by the coarse boundary, then control discarded interior distinctions conditionally on the complete retained data. The Fisher metric transports a certificate only within this explicit map structure.
