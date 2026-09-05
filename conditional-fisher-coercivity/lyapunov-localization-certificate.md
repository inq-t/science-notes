# A Lyapunov Certificate for Context Localization

A positive function on the actual joint carrier can certify that a fluctuation cannot remain concentrated in an unfavorable context without paying gradient energy. The certificate uses an integration-by-parts identity, not the probability of that context. It supplies explicit constants for the bad-context theorem and remains valid for a partial diffusion that moves only selected surrounding variables.

**Status: [EXACT CONDITIONAL THEOREM] for the stated conservative symmetric diffusion and form domains; [EXACT APPLICATION] to a specified Wilson neighborhood in the linked construction; [OPEN] for a complete continuum certificate.**

## A positive test function leaves a nonnegative remainder

Let \(\mu\) be a probability law on a compact smooth manifold without boundary, with smooth positive density. Let \(L\) be a conservative \(\mu\)-symmetric diffusion generator, with
\[
\mathcal E(f)=\int\Gamma(f)\,d\mu,\qquad
\int h(-Lk)\,d\mu=\int\Gamma(h,k)\,d\mu.
\tag{LC1}
\]
Here \(\Gamma\) uses the same mobility and normalization as \(L\), with no implicit factor \(1/2\) in \(\mathcal E\). It may differentiate only selected product coordinates. Its closed realization and a smooth form core are part of the datum.

For smooth \(W>0\), define the multiplication potential
\[
V_W=-\frac{LW}{W}.
\tag{LC2}
\]
The diffusion product rule and integration by parts give, for real smooth \(f\),
\[
\boxed{
\int V_W f^2\,d\mu
=\mathcal E(f)-\int W^2\Gamma(f/W)\,d\mu
\le\mathcal E(f).}
\tag{LC3}
\]
Indeed the left side equals \(2\int(f/W)\Gamma(f,W)-\int(f/W)^2\Gamma(W)\); completing the square proves the identity. Complex tests follow by real and imaginary parts. Compactness and positivity of \(W\) allow form-core extension. Noncompact carriers require separate integrability and cutoff arguments.

This is the integration-by-parts mechanism in [[library/a-simple-proof-of-the-poincare-inequality/inq|Bakry--Barthe--Cattiaux--Guillin]], printed page 64 before equation (2.3). Their global Poincare theorem also assumes a local Poincare estimate; the present context specialization is proved below rather than attributed to that paper.

## The bad-context coefficient is obtained without differentiating the conditional mean

Disintegrate \(\mu(dR,dU)=\nu(dR)q_R(dU)\), and let \(P=\mathbb E[\cdot\mid R]\). For a measurable retained set \(B\), write \(A=\{(R,U):R\in B\}\). Suppose independently of the test that
\[
V_W\ge\delta>0\ \text{on }A,\qquad
V_W\ge-M\ \text{on }A^c,\qquad M\ge0.
\tag{LC4}
\]
Then
\[
(\delta+M)\|\mathbf1_A g\|^2
\le\mathcal E(g)+M\|g\|^2.
\tag{LC5}
\]
Apply this to \(g=f-\mu f\). Conservativity gives \(\mathcal E(g)=\mathcal E(f)\). Since conditional variance minimizes distance to a context-dependent constant,
\[
\|\mathbf1_B(I-P)f\|^2
\le\|\mathbf1_B(f-\mu f)\|^2.
\]
Therefore
\[
\boxed{
\|\mathbf1_B(I-P)f\|^2
\le\frac{\mathcal E(f)}{\delta+M}
+\frac{M}{\delta+M}\operatorname{Var}_\mu f.}
\tag{LC6}
\]
This does not require a bound on \(\mathcal E(Pf)\), which would be a separate score/lift problem.

If \(\mathcal E\le\mathcal E_{\mathrm{joint}}\), (LC6) also holds with the full joint form on its right. Given the good-fiber floor \(\lambda_0\) and retained-mean constant \(c\) of [[bad-context-response-and-localization|the bad-context theorem]], one obtains
\[
\boxed{
\mathcal E_{\mathrm{joint}}(f)\ge
\frac{\delta}
{1+(\delta+M)(\lambda_0^{-1}+c)}
\operatorname{Var}_\mu f.}
\tag{LC7}
\]
Neither \(\lambda_0\) nor \(c\) is supplied by (LC4). In particular, separate favorable regions may still have an uncontrolled relative mode.

## Commuting escape preserves the original innovation

There is a sharper version when the escape directions leave the conditioned law unchanged. On a finite compact smooth product, write
\[
P_ef(R)=\int f(u,R)q_e(u\mid R)\,du,\qquad Q_e=I-P_e.
\]
Let \(X\) differentiate retained coordinates only, with smooth coefficients independent of \(u\). Differentiating the normalized conditional integral gives
\[
[X,P_e]f=\int f(u,R)\,X\log q_e(u\mid R)\,q_e(u\mid R)\,du .
\tag{LC10}
\]
Thus \(Xq_e=0\) implies \(XQ_e=Q_eX\). For a finite family of such fields,
\[
\mathcal E_X(Q_ef)=\sum_A\|Q_eX_Af\|_{L^2(\mu)}^2
\le\sum_A\|X_Af\|_{L^2(\mu)}^2=\mathcal E_X(f).
\tag{LC11}
\]
Smooth conditional integration preserves the initial core. Its \(L^2\) and form contractions extend to the closed form domain. No Haar divergence condition is needed for (LC10); the chosen actual-law symmetric generator must still satisfy (LC1) for the localizer.

Require that the localizer's actual-law symmetric generator \(L\) has precisely the Dirichlet form \(\mathcal E_X=\sum_A\|X_A\cdot\|^2\). Under (LC4) for that same generator, applying (LC5) directly to \(Q_ef\), rather than to an outside-block centering, now proves
\[
\boxed{
\|\mathbf1_BQ_ef\|^2
\le\frac{\mathcal E_X(f)}{\delta+M}
+\frac{M}{\delta+M}\|Q_ef\|^2.}
\tag{LC12}
\]
The remainder is the **same innovation** as on the left. For a finite-range Gibbs action, it suffices that no action term meet both the active variable and any differentiated variable, and that the field coefficients exclude the active variable. Sharing undifferentiated boundary data is allowed. This is exactly the geometry of [[rg-covariance-residue/critical-context-and-collective-escape|the critical collective Wilson patch]].

To state the possible closure without claiming coverage, suppose a family of retained cuts \(B_e\) has
\[
\sum_e\|\mathbf1_{B_e^c}Q_ef\|^2\le C_g\mathcal E_{\rm full}(f),\qquad
\sum_e\|\mathbf1_{B_e}Q_ef\|^2
\le A\mathcal E_{\rm full}(f)+b\sum_e\|Q_ef\|^2,\quad b<1.
\]
Then, for the unnormalized site-innovation form
\(\mathcal H_{\rm hb}[f]=\sum_e\|Q_ef\|^2\),
\[
\mathcal H_{\rm hb}[f]\le\frac{C_g+A}{1-b}\mathcal E_{\rm full}(f).
\tag{LC13}
\]
An independently proved heat-bath gap \(\mathcal H_{\rm hb}\ge\gamma\operatorname{Var}_\mu\) gives the gradient floor \(\gamma(1-b)/(C_g+A)\). [[finite-patch-projection-coercivity|Finite-patch projection coercivity]] supplies one sufficient route to that separate gap. Neither complete cut coverage nor its patch constants follow from (LC12).

## An action-relative certificate

For \(\mu\propto e^{-S}\) on a compact product manifold and a selected coordinate set \(J\), take
\[
L_J=\Delta_J-\nabla_JS\cdot\nabla_J.
\]
Let \(S_J\) contain exactly the action terms depending on those coordinates, so \(\nabla_JS_J=\nabla_JS\). For \(0<t\le1\),
\[
W=e^{tS_J},\qquad
V_W=t(1-t)|\nabla_JS|^2-t\Delta_JS.
\tag{LC8}
\]
The endpoint \(t=1\) is permitted on this finite compact carrier and gives the particularly simple identity
\[
V_W=-\Delta_JS.
\tag{LC9}
\]
It is not a new scalar mass field. It is a comparison function computed from the existing action and the inherited diffusion.

[[rg-covariance-residue/wilson-frustration-and-joint-escape|The Wilson escape construction]] proves (LC4) for one explicit neighborhood of a frustrated \(SU(3)\) source with constants proportional to the actual coupling and independent of surrounding volume. [[rg-covariance-residue/wilson-exterior-force-localization|Exterior-force localization]] uses \(t=1/2\) to retain the gradient-squared term; a single retained force--curvature certificate controls an additional unequal-well geometry and safely combines both regions.

A positive killed-process bound for tests supported in \(A\) follows immediately from (LC3). The converse use would be invalid: such a supported-test bound alone does not control unrestricted \(\mathbf1_Af\), because a cutoff can create gradient costs. The globally defined \(W\) and the outside lower bound in (LC4) account for those costs.

The diffusion parameter here is auxiliary configuration-space time. A physical mass needs the separately proved transfer/Hamiltonian comparison and continuum construction; no Lyapunov function supplies that change of operator.

[[rg-covariance-residue/critical-context-and-collective-escape|Collective Wilson escape]] supplies a non-coordinate instance of the same identity. A retained transport tree makes coordinated link fields Haar-divergence-free and their squared form gauge invariant. The action localizer then controls a force-zero context with positive individual-link Hessians, through a negative collective second variation.
