# Exterior Force Controls an Asymmetric Wilson Context

A frozen \(SU(3)\) link can have an exponentially slow conditional mode even when its surrounding plaquettes have positive real trace. A different full-law certificate controls such contexts: a sufficiently large surrounding-link force cannot be cancelled by the one active plaquette touching each surrounding link. The resulting local form estimate improves as the inverse coupling grows and is independent of ambient volume.

**Status: [EXACT FINITE-WILSON CONTEXT THEOREM] with a realizable unequal-well example; [OPEN] all-context closure, physical transfer and continuum mass gap.**

## A force on the surrounding-link carrier

Use the complete four-dimensional Wilson law, metric and patch geometry of [[wilson-frustration-and-joint-escape|joint Wilson escape]]:
\[
S=\beta\sum_p(1-\phi_p),\qquad
\phi_p=\tfrac13\operatorname{ReTr}U_p,\qquad
g(X,Y)=-\tfrac13\operatorname{ReTr}(XY).
\tag{EF1}
\]
The active link is \(e\), its six distinct outer parallel links are \(J\), and \(R\) retains all links other than \(e\). Each \(j\in J\) belongs to one active plaquette and five external plaquettes. No plaquette contains two members of \(J\). The patch is interior, or the periodic side length is at least five.

Define the dimensionless exterior force, a tangent vector at the actual surrounding link, by
\[
\mathcal F_j(R)
=-\sum_{\substack{p\in\mathcal P_{\mathrm{ext}}\\p\ni j}}\nabla_j\phi_p(R),
\qquad
B_\nabla=\{R:\|\mathcal F_j(R)\|_g\ge3
\text{ for every }j\in J\}.
\tag{EF2}
\]
This differentiates the full external action with respect to retained links; it does not differentiate the active-link conditional density with respect to a source parameter. All defining plaquettes exclude \(e\). The set is retained-measurable and gauge invariant, since the product metric and real-trace action are invariant.

For any plaquette traversing \(j\) once,
\[
\|\nabla_j\phi_p\|_g\le1.
\tag{EF3}
\]
Indeed, a unit tangent produces a derivative \(\frac13\operatorname{ReTr}(TX)\) after cyclically rearranging unitary factors, with \(\|T\|_{\mathrm{HS}}=\sqrt3\) and \(\|X\|_{\mathrm{HS}}=\sqrt3\). Hilbert--Schmidt Cauchy--Schwarz bounds its absolute value by one; inversion changes only the sign and unitary transports.

The sole active plaquette at each \(j\) can therefore cancel at most one unit of exterior force. For every active \(U_e\), on \(B_\nabla\),
\[
\|\nabla_jS\|\ge2\beta,\qquad
|\nabla_JS|^2\ge24\beta^2.
\tag{EF4}
\]
This uniformity in the hidden coordinate is why (EF2) supplies a context certificate.

## A half-action localizer retains the force-squared term

Let \(S_J\) include all 36 plaquettes touching \(J\), and let
\[
L_J=\Delta_J-\nabla_JS\cdot\nabla_J,\qquad
\mathcal E_J(f)=\int|\nabla_J f|^2\,d\mu,\qquad W=e^{S_J/2}.
\]
The [[conditional-fisher-coercivity/lyapunov-localization-certificate|positive-function identity]] yields
\[
V_W=-L_JW/W
=\tfrac14|\nabla_JS|^2-\tfrac12\Delta_JS.
\tag{EF5}
\]
The metric-normalized Casimir calculation gives
\(\Delta_JS=8\beta\sum_{p\cap J\ne\varnothing}\phi_p\le288\beta\) everywhere. Hence
\[
V_W\ge6\beta^2-144\beta\quad\text{on }B_\nabla,
\qquad V_W\ge-144\beta\quad\text{everywhere}.
\tag{EF6}
\]
For \(\beta>24\), keep \(\delta=6\beta^2-144\beta>0\) and \(M=144\beta\); their sum is exactly \(6\beta^2\).

Let \(K=\{e\}\cup J\),
\(Q_e=I-\mathbb E[\cdot\mid R]\), and
\(Q_K=I-\mathbb E[\cdot\mid U_{K^c}]\), all for the same full Wilson law. Then every test in the closed form domain obeys
\[
\boxed{
\|\mathbf1_{B_\nabla}Q_e f\|^2
\le\frac{\mathcal E_J(f)}{6\beta^2}
+\frac{24}{\beta}\|Q_K f\|^2,\qquad\beta>24.}
\tag{EF7}
\]
Apply the positive-function identity to
\(f-\mathbb E[f\mid U_{K^c}]\). The subtracted function is independent of \(J\), so its subtraction leaves \(\mathcal E_J\) unchanged. Conditional variance then bounds the left side by the corresponding restricted squared norm. This is the same nested-centering proof as (JE9), with the constants from (EF6), and does not assume a derivative estimate on the active conditional mean.

Tests vanishing outside \(B_\nabla\) satisfy
\[
\mathcal E_J(f)\ge6\beta(\beta-24)\|f\|^2.
\tag{EF8}
\]
Selecting the patch at every active link on the periodic lattice gives exactly sixfold outer-link overlap, hence
\[
\boxed{
\sum_e\|\mathbf1_{B_{\nabla,e}}Q_e f\|^2
\le\frac{1}{\beta^2}\mathcal E_{\mathrm{full}}(f)
+\frac{24}{\beta}\sum_e\|Q_{K_e}f\|^2,\qquad\beta>24.}
\tag{EF9}
\]
The last term is a sum of local block innovations, not a multiple of global variance. Its coefficient is less than one, at most \(1/2\) for \(\beta\ge48\), and tends to zero with large \(\beta\); no absorption of this different form has been proved. The inequalities restrict to gauge-invariant tests.

## A realizable context outside the negative-trace cut

Set every link other than the six outer links to identity, leaving the active link free. Put
\[
a=(3+4i)/5,\qquad
D=\operatorname{diag}(a,a,a^{-2})\in SU(3).
\tag{EF10}
\]
Assign two copies of each cyclic diagonal permutation of \(D\) to the six outer links. Since all transverse links are identity, the complementary staple products equal those assigned matrices. Their sum is
\[
S_{\mathrm{staple}}=2\operatorname{Tr}(D)I
=\frac{46+32i}{25}I.
\tag{EF11}
\]
Writing this as \(r e^{i\psi}I\) gives \(\tan\psi=16/23\) with
\(\pi/6<\psi<\pi/3\). The active conditional is
\[
dq(U_e)\propto
\exp\!\left[\frac{\beta r}{3}
\operatorname{ReTr}(e^{-i\psi}U_e)\right]dU_e.
\tag{EF12}
\]
Thus [[frustrated-su3-conditional-wells#Unequal wells persist without exact phase coexistence|the unequal-well theorem]] applies along this fixed source shape as \(\beta\) grows.

Every external plaquette is \(D_j\) or \(D_j^*\), with
\[
\phi_p=\frac{\operatorname{ReTr}D}{3}=\frac{23}{75}>0.
\tag{EF13}
\]
This exterior lies outside the earlier cut requiring all external traces to be at most \(-2/5\). It nevertheless lies strictly inside \(B_\nabla\). The traceless imaginary part of \(D\) is
\[
(\operatorname{Im}D)_0=\tfrac1{75}\operatorname{diag}(44,44,-88).
\]
Its norm computes the gradient of \(\operatorname{ReTr}D/3\). At each outer link, its five external real-trace functions coincide regardless of plaquette orientation, so the gradients add:
\[
\|\mathcal F_j\|
=5\sqrt{\tfrac13\operatorname{Tr}[(\operatorname{Im}D)_0^2]}
=\frac{44\sqrt2}{15}>3.
\tag{EF14}
\]
Both the force margin and the nondegenerate unequal wells persist under sufficiently small perturbations of the exterior links. Such an exterior neighborhood can be fixed independently of \(\beta\); the source-shape bounds, not an estimate of its probability, supply the asymptotic conditional obstruction.

The integers and the threshold in (EF2) are convenient certificate choices. They are not proposed fundamental constants or measured masses.

## One retained certificate combines force and curvature

The same proof yields a more flexible criterion without requiring a separate threshold at every outer link. For \(x_+=\max(x,0)\), define the retained functions
\[
A(R)=\sum_{j\in J}\bigl(\|\mathcal F_j(R)\|-1\bigr)_+^2,
\qquad
\chi_\beta(R)=\frac{\beta^2}{4}A(R)
-4\beta\left(6+\sum_{p\in\mathcal P_{\mathrm{ext}}}\phi_p(R)\right).
\tag{EF15}
\]
The reverse triangle bound and the six active trace bounds give, for every hidden \(U_e\),
\[
V_W(R,U_e)\ge\chi_\beta(R),\qquad
\chi_\beta(R)\ge-144\beta.
\tag{EF16}
\]
No derivative of \(A\) or of the cut is used, so its nonsmooth positive part causes no domain issue. For any \(\delta>0\), the retained set \(B_{\beta,\delta}=\{\chi_\beta\ge\delta\}\) therefore obeys
\[
\|\mathbf1_{B_{\beta,\delta}}Q_e f\|^2
\le\frac{\mathcal E_J(f)}{\delta+144\beta}
+\frac{144\beta}{\delta+144\beta}\|Q_Kf\|^2.
\tag{EF17}
\]
This is a sufficient pointwise lower certificate, not the exact minimum of \(V_W\) over the active link.

In particular, let \(B_\Delta\) be the previous negative-trace set. There \(\sum_{\mathrm{ext}}\phi_p\le-12\), so \(\chi_\beta\ge24\beta\). On \(B_\nabla\), \(A\ge24\), giving \(\chi_\beta\ge6\beta^2-144\beta\). For \(\beta\ge28\) a **single** certificate covers their union:
\[
\boxed{
\|\mathbf1_{B_\Delta\cup B_\nabla}Q_e f\|^2
\le\frac{\mathcal E_J(f)}{168\beta}+\frac67\|Q_Kf\|^2.}
\tag{EF18}
\]
Its summed gradient coefficient is \(1/(28\beta)\). This trades sharpness on each separate set for a common bound on the union, without adding two residual coefficients. The more adaptive cut in (EF17) can contain further geometries, but no exhaustive coverage theorem has been established.

The active trace bound in (EF15) is deliberately permissive: it replaces their common-link sum by six. [[coherent-staple-localization|Coherent staple localization]] keeps its exact support and permits smaller selected outer sets. It controls a central exterior where (EF15) is negative, using a three-link rather than seven-link residual carrier. The original bounds remain valid sufficient criteria.

## What this changes about the next proof obligation

The earlier negative action-Laplacian certificate controls one unstable context. The present force-squared certificate controls a nonstationary context whose plaquette traces are positive. Neither requires a new field: both act on the surrounding configuration variables of the same law. This is a concrete instance of the [[wall-construction-interface/vertical-and-horizontal-motion|vertical--horizontal distinction]], not a realization of the full wall interface.

The union of these two controlled sets has not been proved to contain all unfavorable conditional sources. [[critical-context-and-collective-escape|A critical three-strip configuration]] now gives an explicit omission: its active conditional has two wells, every force vanishes, each individual-link Hessian is positive, and \(\chi_\beta=-54\beta\). A transported 72-link variation supplies a separate collective certificate for that context. Equation (EF18) combines the present two cuts safely, but does not control the remaining block-innovation form or exclude soft collective modes.

Even a complete configuration-space Poincare estimate would still require the separately normalized physical transfer and continuum construction. The auxiliary diffusion parameter in \(L_J\) is not clock time, and its force-squared coefficient is not a glueball energy.

[[receipts/asymmetric_context_force_receipt.py|The finite receipt]] checks the exact source, plaquette orientations, external-force norm, unequal-well Hessians and nonlinear half-action localizer on the full patch. The proofs above, not finite sampling, establish the inequalities.
