# Bridge Forgetting and the Inherited Marked Transfer

Forgetting the rightmost cell of the three-cell chain returns the genuine old two-cell electric operator, with path weights \(3\kappa,\kappa,3\kappa\). Its finite transfer retains a composite comparison along the old exterior path. Replacing that composite by one newly paced Gaussian comparison changes the experiment: an explicit \(SU(2)\) Fourier coefficient differs, and a bounded preparation-norm mark separates the laws at every positive width. The inherited composite nevertheless remains positive and sews exactly when its full preparation data are retained.

## The retained exterior path has three edges

Use the actual paths and based loops of [[three-cell-incidence-and-shared-path-motion|three-cell incidence]]:
\[
x=up^{-1},\qquad y=a q b^{-1}p^{-1},\qquad
z=a v q^{-1}a^{-1}.
\]
Forgetting the right cell removes its exterior path \(v\). The surviving paths \(a,q,b^{-1}\) concatenate to the old right exterior path
\[
t=a q b^{-1},\qquad y=tp^{-1}.
\tag{BF1}
\]
The intervening vertices are now bivalent. The exact additive path theorem therefore gives the two-cell theta graph with paths \((u,p,t)\) and coefficients \((3,1,3)\kappa\). The group, metric and coefficient remain the supplied ones; no finite Gaussian preparation is reset in making this electric-operator statement.

On the complete carriers define
\[
\pi:G^3\to G^2,\quad \pi(x,y,z)=(x,y),\qquad
(If)(x,y,z)=f(x,y).
\tag{BF2}
\]
Normalized Haar makes \(I\) an isometry. It also intertwines simultaneous conjugation, so it restricts to the full physical carriers. Substituting \(If\) in (TC6), and not discarding any nonzero bridge row, yields
\[
\boxed{
\mathcal E_{\rm old}(f)=
\kappa\int_{G^2}\left[
3|L_xf|^2+3|L_yf|^2+|(R_x+R_y)f|^2
\right]dx\,dy .}
\tag{BF3}
\]
Equivalently,
\[
H_{\rm old}
=4\kappa(D_x+D_y)-2\kappa\sum_A R_{x,A}R_{y,A},
\qquad H_{\rm ch}I=IH_{\rm old}.
\tag{BF4}
\]
The identity holds first on smooth functions, then for the closed forms, operator domains and heat semigroups. It is the complete old two-cell operator, including its relative angular response, rather than only a statement about individual cell traces. A bounded potential \(V(x,y)\) and physical sources pulled back by \(I\) obey the same restriction. A new potential depending on \(z\) generally does not.

## The independent bridge construction has an exact projected experiment

Write the finite operator from [[prepared-frame-actions-and-the-bridge-return|prepared frame actions]] as
\[
S_\alpha=T_{a,\alpha}T_{b,\alpha}
F_{\parallel,\alpha}^{(3)}
T_{b,\alpha}T_{a,\alpha}.
\tag{BF5}
\]
The middle factor uses four common-endpoint paths \(P_0,P_1,P_2,P_3\), with old parent path \(P_1\). The coordinates are
\(x=P_0P_1^{-1}\), \(y=P_2P_1^{-1}\), \(z=P_3P_2^{-1}\).
The source-free bridge actions descend pointwise:
\[
\pi A_h=A_h^{\rm old}\pi,\quad
A_h^{\rm old}(x,y)=(x,hy),\qquad
\pi B_h=B_h^{\rm old}\pi,\quad
B_h^{\rm old}(x,y)=(x,yh^{-1}).
\tag{BF6}
\]
The exact conditional-family marginal (CF5) removes \(P_3\) while retaining \(P_1,P_0,P_2\) and their preparations. Consequently
\[
\boxed{
S_\alpha I=I\overline S_\alpha,\qquad
\overline S_\alpha=
T_{a,\alpha}^{\rm old}T_{b,\alpha}^{\rm old}
F_{\parallel,\alpha}^{(2)}
T_{b,\alpha}^{\rm old}T_{a,\alpha}^{\rm old}.}
\tag{BF7}
\]
The two-access middle factor still has path coefficients \((3,1,1)\kappa\); each pair of bridge occurrences adds \(\kappa\) to the right exterior path. This explains (BF3) without altering the old comparison pace inside the middle factor.

Equation (BF7) has a full marked version. At each substep retain its actual group increment, whole preparation and projected incoming and outgoing configurations. In the middle substep retain the parent and \(P_0,P_2\) preparation readouts, with all source-free normalizers. For every bounded joint mark measurable in these retained data, pushing the full path measure through \(\pi\) gives the corresponding marked version of the five-substep measure on the right of (BF7). This includes marks coupling different substeps. It follows by (BF6) at the bridge steps and by conditional leaf integration at the middle step. A mark depending on the forgotten \(P_3\) preparation or an unretained \(z\)-readout is not covered by calling it an old mark.

Thus the equality holds through arbitrary temporal products with such retained marks, including all scalar factors. Gauge-invariant marks, or their actual joint gauge averages, give the same statement on the physical carriers. No assertion that the marking operation preserves Hilbert positivity is needed.

For the source-free independent bridge law there is also a useful compression. Central inversion-symmetric increment densities make the left and right averages in (BF6) the same central convolution on the \(y\)-factor; denote the two densities' operators by \(C_{a,\alpha}\) and \(C_{b,\alpha}\). The middle operator commutes with left translations of \(y\): before quotienting, this is its exact covariance under independent left multiplication of \(P_2\). It follows that
\[
\overline S_\alpha=
F_{\parallel,\alpha}^{(2)}
C_{a,\alpha}^{\,2}C_{b,\alpha}^{\,2}.
\tag{BF8}
\]
This packages the bridge increments into a composite right-path kernel. General marks can destroy centrality and this convenient commutation, so the ordered marked law remains (BF7), not an unqualified replacement of its data by (BF8).

## Shared terminal preparations project before gauge quotient

The same projection argument applies to [[shared-preparation-actions-and-the-conditional-return|the transported shared-preparation palindrome]], with one essential change: keep its charged path carrier until after all substeps. At fixed terminal preparations \(\xi_i\), write
\[
R_{i,\xi_i}f(P_i)=
\frac1{\zeta_i(\xi_i)}
\int_G e^{-\alpha\|[\rho(k)-I]\xi_i\|^2/r_i}
f(P_i k)\,dk .
\tag{BF9}
\]
The terminal-to-root transport at a bridge substep is the current \(P_1\). The lifted actions are
\[
\begin{aligned}
\widehat A_k(P_0,P_1,P_2,P_3)
&=(P_0,P_1,P_1kP_1^{-1}P_2,P_1kP_1^{-1}P_3),\\
\widehat B_k(P_0,P_1,P_2,P_3)
&=(P_0,P_1,P_2k^{-1},P_3k^{-1}).
\end{aligned}
\tag{BF10}
\]
Their root increment is \(h=P_1kP_1^{-1}\), and their root preparation is \(\rho(P_1)\xi_j\). After the middle transition changes \(P_1\), a later bridge transports the same terminal preparation through that new \(P_1\).

Let \(I_{012}\) insert functions independent of \(P_3\). Both actions (BF10) preserve its range. The middle product \(\bigotimes_{i=0}^3R_{i,\xi_i}\) does too, because \(R_{3,\xi_3}1=1\). Hence the complete fixed-preparation charged palindrome projects exactly to the corresponding three-path palindrome. The quotient maps satisfy \(J_3I=I_{012}J_2\), so averaging and then taking the final-endpoint gauge quotient preserves this identity.

In particular, when both bridge types reuse only the retained preparation \(\xi_2\), the forgotten conditional preparation \(\xi_3\) integrates to one under the finite row law
\[
d\nu_\alpha(\xi)=
\prod_i\frac{\zeta_i(\xi_i)}
{b_i(\xi_{\operatorname{pa}(i)})}\,
P_i(d\xi_i\mid\xi_{\operatorname{pa}(i)}).
\tag{BF11}
\]
The retained marked marginal is exact, including all transported bridge readouts and the same terminal matrix reused at different substeps. This uses the normalized law and retained-parent condition of [[conditional-preparation-diagrams-and-ancestral-readout|ancestral preparation diagrams]]. If a retained bridge instead uses \(\xi_3\), that preparation remains part of the retained experiment even after its spatial loop is forgotten; deleting it would change the law.

This projection proof does not replace the independent positivity proof for the shared construction. Nor does it compress a fixed noncentral preparation to the physical quotient before applying its bridges. The charged order and current transport in (BF10) are part of the marked experiment.

## A finite Fourier coefficient detects the reset

There is an explicit \(SU(2)\) counterexample to replacing (BF7) by an ordinary two-cell single-comparison kernel. Use the defining representation and identical isotropic inventories with \(m=2k\), variance \(\sigma^2\), and sufficient \(k\). Set the conditional parent coefficients to zero in this example, so the path preparations are independent; this is an allowed member of the conditional family. Write \(S=\|\Xi\|^2\sim\operatorname{Gamma}(m,\sigma^2)\), and define
\[
Z(t)=\int_{SU(2)}
e^{-2t(1-\operatorname{Tr}h/2)}dh,\qquad
d(t)=\frac{I_2(2t)}{I_1(2t)}.
\tag{BF12}
\]
Here \(d(t)\) is the normalized fundamental-representation multiplier of a fixed-norm comparison. The character integral in [[relative-multiplication-transfer-and-the-rotor-limit|the exact rotor multipliers]] proves the formula. The whole-Gaussian multiplier and its finite row law are
\[
b(\beta)=
\frac{\mathbb E[Z(\beta S)d(\beta S)]}
{\mathbb E Z(\beta S)},\qquad
d\mu_\beta(S)=
\frac{Z(\beta S)dP(S)}{\mathbb E Z(\beta S)}.
\tag{BF13}
\]
Choose base parent and \(P_2\) comparison pace \(r\), \(P_0\) pace \(3r\), and bridge paces \(r/2\). With \(\beta=\alpha/r\), these are exactly the calibration weights required in (BF7). On the physical observable \(\operatorname{Tr}y/2\), the inherited independent-preparation transfer has multiplier
\[
\boxed{
B_{\rm inherited}(\beta)
=b(\beta)^2b(2\beta)^4.}
\tag{BF14}
\]
The two factors \(b(\beta)\) come from \(P_1,P_2\), and the four other factors come from the four bridge occurrences. A reset old two-cell kernel, keeping the same parent but replacing the right composite by one Gaussian comparison at pace \(3r\), instead has
\[
\boxed{
B_{\rm reset}(\beta)=b(\beta)b(\beta/3).}
\tag{BF15}
\]
Both have the returned right-path coefficient \(3\kappa\).

These finite functions are different. The Bessel series gives \(d(t)=t/2+O(t^3)\), and dominated convergence gives
\[
b(\beta)=c\beta+o(\beta),\qquad
c=\frac{\mathbb ES}{2}=\frac{m\sigma^2}{2}>0.
\]
Consequently
\[
B_{\rm inherited}(\beta)
=16c^6\beta^6+o(\beta^6),\qquad
B_{\rm reset}(\beta)=\frac{c^2}{3}\beta^2+o(\beta^2).
\tag{BF16}
\]
They differ for every sufficiently small positive width parameter \(\beta\). This is an exact analytic comparison, not an approximation to the strong-localization limit \(\alpha\to\infty\).

For the shared version reusing \(\xi_2\) in all four bridge occurrences, the same independent-root example instead gives
\[
B_{\rm shared}(\beta)
=b(\beta)\,
\mathbb E_{\mu_\beta}\!\left[
d(\beta S)d(2\beta S)^4\right]
=\frac{\mathbb ES\,\mathbb ES^5}{4}\beta^6
+o(\beta^6).
\tag{BF17}
\]
This too differs from (BF15). The whole matrix is reused while the increments are conditionally independent. The higher moment in (BF17) records that distinction. To justify the displayed asymptotics without a uniform power-series assumption, the positive Bessel series gives \(0\le d(t)\le t/2\); also \(Z(t)\le1\) and \(\mathbb EZ(\beta S)\to1\). Gaussian fifth moments then dominate the shared expression.

## A retained norm mark distinguishes every positive width

The stronger marked obstruction does not require independent path preparations. Let the old parent and right preparation satisfy
\(\eta=a\xi+\varepsilon\), with a nondegenerate isotropic innovation, and write \(S=\|\xi\|^2\), \(T=\|\eta\|^2\). Allow \(a\ne0\). Keep the parent pace fixed. At right pace \(r\), define
\[
\zeta_r(T)=Z(\alpha T/r),\qquad
b_r(S)=\mathbb E[\zeta_r(T)\mid S],\qquad
d\mu_0(S)=\frac{\zeta_{\rm parent}(S)dP(S)}
{\mathbb E\zeta_{\rm parent}(S)}.
\]
The inherited old norm law is
\[
d\nu_r(S,T)=d\mu_0(S)\,
\frac{\zeta_r(T)}{b_r(S)}P(dT\mid S).
\tag{BF18}
\]
It is unchanged by the independent bridge substeps, or by the shared charged palindrome at fixed preparations: each such source-free substep has unit row sum. The reset single right comparison at pace \(3r\) instead uses \(\nu_{3r}\).

For every \(\alpha>0\), these laws are unequal. If their conditional \(T\)-densities agreed for a fixed \(S\), then
\(Z(\alpha T/r)/Z(\alpha T/(3r))\) would be constant on \(T>0\). The noncentral Gaussian norm has strictly positive density there. But \(Z(0)=1\), \(Z'(0)=-2\), and the ratio has derivative \(-4\alpha/(3r)\) at zero, which is nonzero. Continuity excludes equality almost everywhere.

An explicit bounded joint norm mark is
\[
M_\alpha(S,T)=\operatorname{sgn}\!\left[
\frac{\zeta_r(T)}{b_r(S)}
-\frac{\zeta_{3r}(T)}{b_{3r}(S)}\right].
\]
Integrating the complete marked outgoing row against the constant function gives the strict difference
\[
\boxed{
\int M_\alpha\,d\nu_r-\int M_\alpha\,d\nu_{3r}
=\int d\mu_0(S)P(dT\mid S)
\left|\frac{\zeta_r(T)}{b_r(S)}
-\frac{\zeta_{3r}(T)}{b_{3r}(S)}\right|>0.}
\tag{BF19}
\]
Thus matching the returned kinetic coefficient cannot identify the complete old marked experiment at any positive finite width. The test fixes the natural old parent and right-preparation readouts; it does not exclude another law equipped with a separately proved source identification.

## Retain the composite as the old preparation data

The inherited operator \(\overline S_\alpha\) is itself a valid old transfer. Its positivity, self-adjointness, injectivity and Markov property follow either from (BF7) or from restriction of the full positive operator to the invariant range of \(I\). Its marked path measure retains the separate comparison preparations, their normalizers, transport frames and the ordered sewing. Repeated composition preserves (BF7) exactly.

This gives an honest access extension if the old two-cell experiment is already specified by that composite law: adding the rightmost cell and its conditionally normalized unused preparation preserves every retained mark described above. There is no need to compress the preparation record to one newly sampled Gaussian matrix. On the independent source-free sector, (BF8) provides its convolution description; the fuller marked record remains available when that description no longer suffices.

Removing a cell changes cycle rank and is a genuine access change. Collapsing the surviving bivalent chain \(a,q,b^{-1}\) into the path \(t\) is a presentation change only when this entire inherited comparison law travels with it. Replacing it by the reset single Gaussian comparison of (BF15) changes the old experiment, even though the electric operator has the same return. The remaining construction problem is to select a family whose composite old laws and marked transports agree across repeated spatial extensions, rather than choosing a new one-link preparation after each projection.
