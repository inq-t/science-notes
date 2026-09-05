---
inq.module: "conditional-fisher-coercivity"
inq.include:
  - "./"
inq.ambient:
  - "**"
---
# Conditional Fisher Coercivity

The Fisher metric of a conditional family measures how strongly changes of the retained context alter the hidden law. A Poincare inequality for the context distribution in that metric forces a positive fraction of every hidden distinction to remain unpredictable from the context. The result is dimensionless, invariant under regular reparameterization, and tensorizes without a factor counting the context coordinates. It supplies a concrete geometric certificate for a global--local response floor; proving its hypotheses uniformly for the Yang--Mills continuum remains a separate task.

**Status: [EXACT CONDITIONAL THEOREM], with a direct proof; [EXACT] for the Gaussian calibration and independent-product rule; [OPEN] for a regulator-uniform Yang--Mills realization.** A statistical law here is a mathematical representation, not an assertion of stochastic ontology.

## A conditional law supplies its own comparison metric

Let \(Z\) be a smooth finite-dimensional context manifold, with probability law \(\nu\). On a fixed hidden carrier \(Y\), let
\[
\beta_z(dy)=b_z(y)m(dy),\qquad
\mu(dz,dy)=\nu(dz)\beta_z(dy),
\tag{CF1}
\]
where the conditional densities are positive on common support. Require differentiability under the integral for the observables used below, square-integrable scores, and the stated form-domain inclusions. A moving support or a context-dependent change of hidden coordinates requires extra derivative terms; it is not covered by simply reusing (CF1).

With natural logarithms, define the centered conditional score and its Fisher tensor by
\[
s_z[h]:y\longmapsto d_z\log b_z(y)[h],\qquad
I_z(h,k)=\langle s_z[h],s_z[k]\rangle_{L^2(\beta_z)}.
\tag{CF2}
\]
Normalization gives \(\beta_z(s_z[h])=0\). This metric belongs to the family \(z\mapsto\beta_z\), not to the marginal density \(\nu\) alone.

First suppose \(I_z\) is positive definite. Define the weighted boundary form
\[
\mathcal E_F(g)=\int_Z (dg)^*I_z^{-1}(dg)\,d\nu(z)
\tag{CF3}
\]
with a specified closed realization. Its generator is a weighted Fisher-metric Laplacian on \(L^2(\nu)\); it is the ordinary Laplace--Beltrami operator of \(I\) only for the appropriate volume measure. Suppose
\[
\mathcal E_F(g)\ge\lambda_F\operatorname{Var}_\nu(g),
\qquad \lambda_F>0.
\tag{CF4}
\]
It is enough to prove this on the conditional-mean image used below, with its form domain; a full boundary Poincare theorem is a stronger convenient hypothesis.

## The score projection theorem

For \(f=f(y)\), independent of \(z\), put \(Kf(z)=\beta_zf\). Work first on a dense linear test class \(\mathcal D\subset L^2(\mu_Y)\) for which differentiation is valid and \(K\mathcal D\subset\operatorname{Dom}\mathcal E_F\). Differentiation gives
\[
d(Kf)[h]=\langle s_z[h],f-\beta_zf\rangle_{\beta_z}.
\tag{CF5}
\]
Complex observables follow by complexification, with inner products conjugate-linear in the first slot.

Let \(S_z:T_zZ\to L^2_0(\beta_z)\) send \(h\) to \(s_z[h]\). Then \(I_z=S_z^*S_z\), and \(S_zI_z^{-1}S_z^*\) is the orthogonal projection onto the score span. Bessel's inequality therefore gives the dimension-free bound
\[
\boxed{
\|d(Kf)\|_{I_z^{-1}}^2
=\|P_{\mathrm{score},z}(f-\beta_zf)\|_{\beta_z}^2
\le\operatorname{Var}_{\beta_z}(f).}
\tag{CF6}
\]
Estimating each score component separately and then summing can introduce a false dimension or boundary-area factor. The joint score projection avoids that loss.

Write
\[
B(f)=\int\operatorname{Var}_{\beta_z}(f)\,d\nu(z).
\]
Integrating (CF6), applying (CF4), and using total variance yield
\[
\operatorname{Var}_\nu(Kf)\le\lambda_F^{-1}B(f),\qquad
\operatorname{Var}_\mu(f)=B(f)+\operatorname{Var}_\nu(Kf).
\]
Consequently
\[
\boxed{B(f)\ge\frac{\lambda_F}{1+\lambda_F}
\operatorname{Var}_\mu(f).}
\tag{CF7}
\]
The conclusion extends to the complete \(L^2\) carrier. Indeed, for \(f_n\in\mathcal D\) converging to \(f\), conditional expectation is an \(L^2\) contraction and
\[
\mathcal E_F(K(f_n-f_m))\le B(f_n-f_m)
\le\|f_n-f_m\|_{L^2(\mu_Y)}^2.
\]
Closedness of the form gives \(Kf\in\operatorname{Dom}\mathcal E_F\) and the same bound. On the centered hidden carrier, (CF7) says \(I-K^*K\ge
[\lambda_F/(1+\lambda_F)]I\). It bounds the complete conditional-variance response, not just a finite collection of parameter tangents. The parameter scores control the derivative of every conditional mean. The background-metric branch below uses the analogous dense-domain and closure argument.

The channel viewpoint is consistent with
[[library/strong-data-processing-inequalities-and-phi-sobolev-inequalities-for-discrete-channels/inq|Raginsky's functional-inequality framework]]. The differential certificate (CF2)--(CF7) is proved here; it is not being attributed to that discrete-channel paper.

## Degeneracy and coordinate invariance

If \(I_z\) is singular, the pointwise score identity survives using its Moore--Penrose inverse:
\[
(dKf)^*I_z^+(dKf)\le\operatorname{Var}_{\beta_z}(f).
\]
Indeed \(dKf\) annihilates \(\ker I_z\) and lies in the range of \(S_z^*\). On these admissible covectors the pseudoinverse contraction is intrinsic; an arbitrary-coordinate pseudoinverse does not define an invariant energy on arbitrary covectors. This pointwise identity alone does not give a boundary Poincare inequality. For a sufficiently smooth constant-rank family, the null-score directions integrate to local level sets of \(z\mapsto\beta_z\). Rank may instead jump, and a global identifiable quotient need not be smooth or Hausdorff. A naive pseudoinverse form may also admit nonconstant zero-energy functions.

A valid reduction must construct an identifiable quotient on which the conditional family descends, push forward \(\nu\), and establish the closed form and (CF4) there. Alternatively, formulate (CF4) directly on the admissible conditional-mean image. Deleting directions merely to obtain a gap is not justified.

Under a regular reparameterization \(z'=\phi(z)\), the score is a covector, \(I\) transforms as a covariant two-tensor, and \(\nu\) is pushed forward. The contractions in (CF3) are unchanged, so the corresponding operators are unitarily equivalent. Thus \(\lambda_F\) is not a coordinate or unit artifact. Changing the conditional family, forgetting extra data, or changing the prior \(\nu\) is not a reparameterization and can change the result.

## A background-metric certificate that permits singular Fisher information

Often a direct estimate is easier than constructing the intrinsic Fisher form. Let \(g_Z\) be a declared metric, and assume
\[
\operatorname{Var}_\nu(g)\le\lambda_Z^{-1}
\int|dg|_{g_Z^{-1}}^2\,d\nu,\qquad
I_z\le C\,g_Z,\quad \lambda_Z>0,\ C\ge0.
\tag{CF8}
\]
The score-map operator norm gives
\(|dKf|_{g_Z^{-1}}^2\le C\operatorname{Var}_{\beta_z}f\).
Repeating the proof gives
\[
\boxed{B(f)\ge\frac{\lambda_Z}{\lambda_Z+C}
\operatorname{Var}_\mu(f).}
\tag{CF9}
\]
This branch does not require invertibility of \(I\). When \(C=0\), boundary Poincare and (CF5) make every conditional mean constant, and the bound is one.

For a Gibbs family \(\beta_z\propto e^{-V(y,z)}m(dy)\),
\[
s_z[h]=-\partial_zV[h]+\beta_z(\partial_zV[h]).
\tag{CF10}
\]
If its conditional hidden Poincare constant is at least \(\rho>0\), and
\[
\|\nabla_Y\partial_ZV[h]\|_{L^2(\beta_z)}
\le H\,\|h\|_{g_Z},
\tag{CF11}
\]
then \(I_z\le(H^2/\rho)g_Z\). Hence
\[
\boxed{B(f)\ge
\frac{\rho\lambda_Z}{\rho\lambda_Z+H^2}
\operatorname{Var}_\mu(f).}
\tag{CF12}
\]
The conditional law, its normalized score, the context marginal, and both metrics must be the ones appearing in the actual joint law. An unrelated sampler with the same one-component marginal supplies none of these couplings.

## Gaussian calibration is sharp

Let \(0<\kappa<1\) and
\[
Z\sim N(0,1-\kappa),\qquad
Y\mid Z=z\sim N(z,\kappa).
\tag{CF13}
\]
Then \(Y\sim N(0,1)\), \(I_z=1/\kappa\), and
\[
\mathcal E_F(g)=\kappa\int|g'|^2\,d\nu,\qquad
\lambda_F=\frac{\kappa}{1-\kappa}.
\tag{CF14}
\]
Equation (CF7) gives exactly \(B\ge\kappa I\). The first Hermite observable \(f(Y)=Y\) saturates both inequalities; higher Hermites have bridge eigenvalues \(1-(1-\kappa)^n\).

In [[gaussian-bridge-gap-calibration/inq|the stationary Gaussian slab]],
\(\kappa=\tanh(\omega\ell)\). The sufficient context coordinate is the conditional mean \(Z=m\), not the redundant pair of endpoints: the latter has rank-one conditional Fisher information. As \(\omega\downarrow0\), the conditional fiber becomes stiffer while the boundary Fisher gap closes. This distinguishes residual stiffness from resistance to boundary reconstruction.

For independent pairs \((Y_i,Z_i)\), the conditional Fisher tensor is block diagonal, the context law is a product, and the form is the **sum**, not the average, of the component forms. Poincare tensorization gives
\[
\lambda_F^{\rm product}=\min_i\lambda_{F,i},
\tag{CF15}
\]
when the component constants are sharp. Gaussian products therefore recover the exact worst-mode bridge floor \(\min_i\kappa_i\), without a transverse-area penalty. Interacting pairs require a new proof; they do not tensorize by analogy.

## What survives a change of resolution

[[coarse-graining-and-moving-context|Fixed-context Fisher transport]] preserves the certificate in the forward direction: a fixed hidden readout reduces conditional Fisher information and cannot worsen the retained bridge floor. It does not lift a retained estimate to omitted fine observables. A context-dependent readout has an additional channel score, and coarsening the context itself changes the comparison.

[[bridge-data-augmentation-solder/coarse-boundary-leakage-and-response-lifting|Same-law response lifting]] supplies a reverse theorem with explicit hypotheses. A coarse bridge floor must pay for predictors hidden by the coarse boundary, while the discarded interior must retain a conditional response floor given both the retained core and complete boundary. The resulting constants have a precise multiscale loss budget.

[[bridge-data-augmentation-solder/relative-boundary-leakage|The relative version]] applies Fisher coercivity inside discarded boundary fibers. It replaces an absolute subtraction by a multiplicative factor, so a finite total logarithmic loss suffices. [[compact-su2-fisher-calibration|The compact Haar calibration]] shows why the conditional metric is essential: its response vanishes in the sharp-readout limit even though both marginal laws remain unchanged.

For one fixed joint law, the two centered prediction maps are adjoints, so the optimal complete conditional-variance floors agree in both directions. Their conditional gradient Poincare constants need not agree. [[rg-covariance-residue/joint-fisher-response-of-normalized-gauge-blocking|Normalized gauge blocking]] uses this distinction to obtain a reverse bounded-response certificate without assuming a posterior gradient gap.

For the different task of lifting an auxiliary gradient-form inequality, [[contemporary-puzzles/yang-mills-mass-gap/two-scale-rg-descent-and-the-crossover-lemma|the two-scale Fisher--Poincare certificate]] combines conditional Poincare, actual marginal Poincare, and normalized score control. It preserves the distinction between a bounded bridge response and an auxiliary mixing rate.

[[linear-tilted-sphere-coercivity|Linear-tilted sphere coercivity]] supplies one conditional ingredient without a small-field threshold: every finite linear tilt of the unit \(S^3\) has gradient gap at least one. It applies to actual \(SU(2)\) Wilson link conditionals, but their boundary Fisher response can still grow. [[rg-covariance-residue/frustrated-su3-conditional-wells|The \(SU(3)\) conditional counterexample]] shows why that uniform ingredient cannot be assumed for every compact gauge group or every weak-coupling exterior.

[[bad-context-response-and-localization|Bad-context response and localization]] replaces the all-context hypothesis with a precise joint-form target: control the energy cost of concentrating on the unfavorable contexts and separately bound the retained mean. A probability-small context set can still carry a norm-one fluctuation projection, so rarity by itself is not a spectral estimate.

[[lyapunov-localization-certificate|The positive-function certificate]] derives the required localization constants from the actual joint diffusion. [[rg-covariance-residue/wilson-frustration-and-joint-escape|The Wilson realization]] controls a specified frustrated neighborhood with volume-independent coefficients, retaining a local seven-link innovation instead of paying an extensive variance penalty. [[moving-fiber-connection|The inherited moving-fiber derivative]] supplies a complementary rule: transform the derivative together with the conditional Hilbert space. A positive Fisher coefficient in one band need not survive relaxation through the complementary bands.

[[finite-patch-projection-coercivity|Finite-patch projection coercivity]] adds a distinct actual-law route: the exact plaquette-sharing algebra of conditional projections transfers an exterior-uniform cube gap above \(1/n\) to a volume-independent heat-bath gap. It requires no finite-dimensional link approximation. The same analysis rules out direct absorption of the old seven-link remainder and explains why commuting escape must retain the original innovation.

[[gauge-reduced-patch-coercivity|Interior gauge reduction]] identifies which carrier must be tested. The full conditional-refresh gap vanishes at weak coupling through a redundant link witness; an exact gauge completion removes that distraction without changing invariant dynamics. But [[weak-coupling-patch-threshold|a surviving boundary path]] also lies below the proposed \(1/n\) threshold for fixed \(n\ge3\), and a neutral loop test defeats the global-invariant patch inequality for fixed \(n\ge8\). Their nonlinear Rayleigh limits are proved, not inferred from Hessians alone. [[gaussian-refresh-projection-spectrum|The Gaussian projection-frame theorem]] owns the reusable quadratic calculation. The surviving slow information must be retained in a different comparison or multiscale construction.

[[tensor-local-refresh-and-inverse-square-patches|The tensor-local Wilson transform]] supplies a sharper inverse-square patch criterion. It uses uniquely assigned, padded star supports, not the old whole-link cubes, and applies on the global invariant carrier without a finite color cutoff. The needed weak-coupling margin remains unproved. [[rg-covariance-residue/gaussian-harmonic-refresh-lifting|Harmonic retained/fiber lifting]] gives a complementary exact Gaussian construction: commuting same-law dynamics and one fine/coarse gradient comparison with no accumulated blocking-depth loss.

[[measure-preserving-horizontal-lifts|A measure-preserving horizontal connection]] supplies a nonlinear operator alternative to estimating the score term in a fixed frame. It makes conditional expectation reduce the lifted diffusion even with nonzero curvature. Recovering the inherited form requires uniform transport distortion; [[transport-cost-and-uniform-distortion|minimum average transport cost]] cannot replace that estimate. [[rg-covariance-residue/nonlinear-gauge-fiber-transport|The actual Wilson readout]] realizes the connection and bounds its distortion in a declared strong-coupling regime.

[[bounded-transport-and-cut-flux|Bounded transport and cut flux]] characterizes that missing distortion bound: every cut must have enough weighted capacity for the requested probability redistribution. A joint tangent-linear operator has an exact nuclear-norm dual test, and a strict uniform margin supplies smooth parameter-dependent transport. [[rg-covariance-residue/su3-context-flux-obstruction|An actual Wilson exterior variation]] violates the single-link bound for every admissible transport. Its leading Fisher response is carried by the relative well label, which must be retained or controlled through a larger joint carrier.

## Physical return and the unresolved estimate

For the actual stationary vacuum-prepared slab, identify \(Y\) with the complete midpoint configuration and \(Z\) with the joint boundary context, or a proved sufficient context. The
[[bridge-data-augmentation-solder/inq|bridge-to-transfer order]] then turns a regulator-uniform \(\lambda_F>0\) at fixed physical half-width \(\ell\) into the conditional energy bound
\[
\boxed{\Delta_E\ge\frac{\hbar c}{2\ell}\log(1+\lambda_F),}
\tag{CF16}
\]
subject to the separate transfer, continuum, and Poincare reconstruction hypotheses. This is a lower bound, not a numerical glueball prediction. The spectrum in (CF4) is a context-information spectrum; only the reconstruction comparison supplies energy units.

[[bridge-data-augmentation-solder/bridge-floor-under-joint-limits|The joint-limit theorem]] allows the uniform conditional-variance floor to pass through an identified joint cylinder limit without convergence of the Fisher tensor or generator. It preserves the response inequality, not the existence or nontriviality of the required continuum law.

[[collared-quasi-factorization-and-surface-response/fisher-collar-bound-for-wilson-laws|The Wilson collar estimate]] supplies an action-derived version of (CF12) in an explicit nonlinear strong-coupling regime. [[global-local-response-reconstruction/boundary-frozen-heat-and-conditional-fisher-response|Boundary-frozen heat]] supplies a bounded response already below the actual slab defect. Neither theorem proves that the dimensionless Fisher geometry remains coercive through the weak-bare-coupling continuum trajectory.

[[receipts/conditional_fisher_response_receipt.py|The finite receipt]] checks the score projection, the Gaussian sharpness and compression traps, finite conditional heat, and the dimension-free coupling estimates. These checks validate the stated finite identities, not the continuum hypothesis.

[[receipts/coarse_fisher_and_bridge_lifting_receipt.py|The transport and lifting receipt]] checks fixed and moving score balances, the sharp projection lemma, actual finite joint-law lifts, Gaussian two-scale constants, and summable-loss arithmetic.
