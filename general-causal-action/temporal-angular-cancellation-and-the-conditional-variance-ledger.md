# Temporal Angular Cancellation and the Conditional Variance Ledger

The temporal Haar variables in an open reflected slab are gauge transport: after the outer boundary and its spatial links are transported together, those angles are independent Haar variables and contribute no variance of a neutral conditional mean. Their positive score variance is canceled by an exact curvature term. The physical four-boundary variance still contains an auxiliary part and a spatial conditional-mean part, both weighted by the selected vacuum. Its rigidity surplus is the difference of these parts before and after chronological transport, so raw positivity of either angular term does not supply the required strict margin.

**Status: exact conditional identities for the finite reflected determinant law; explicit nonconstant Wilson-source control; open uniform physical rigidity estimate.** [[reflection-sewing-and-the-auxiliary-boundary-carrier|RS1–16]] owns the amplitude and supported vacuum. [[two-slice-innovation-geometry/oriented-innovation-and-finite-temporal-repair|OI19–28]] owns the actual three-slab diagram, its intertwiner, and the corrected-variance target. The calculation below resolves that diagram into its actual angular and auxiliary conditionals.

## Restore the temporal variables in one actual outer slab

Use the RS notation \(\kappa=rw>0\), spatial links \(U\), auxiliary slice \(z\), and
\[
V(U,z)=\|z\|^2-
2\kappa\sum_{\{v,w\},a}
\operatorname{Re}
\bigl(z_v^{(a)*}\rho(U_{vw})z_w^{(a)}\bigr),
\qquad
m(z)=\int e^{-V(U,z)}\,dU.
\tag{TA1}
\]
The supported top vector is \(\varphi>0\), normalized by
\(\int\varphi^2m\,dz=1\), with transfer eigenvalue \(\lambda_0>0\).
The physical vacuum law is
\(d\pi(z)=\varphi(z)^2m(z)dz\), on the site-gauge quotient. Expressions below use auxiliary representatives.

Write \(\rho_\Lambda(g)\) for the action of
\(g\in G^\Lambda\) on every copy at each site, and use the summed complex inner product over sites and copies. With the inner auxiliary boundary \(q\) fixed, the restored one-step law is
\[
d\widehat P_q(g,U,z)
=
\frac{\varphi(z)}
{\lambda_0\varphi(q)}
e^{-V(U,z)}
e^{2\kappa\operatorname{Re}\langle q,\rho_\Lambda(g)z\rangle}
\,dg\,dU\,dz.
\tag{TA2}
\]
Its normalization is the actual RS eigenvector equation. Integrating \(g,U\) returns \(P(q,dz)\), the selected ground-state transition. No vacuum factor or spatial partition weight has been replaced by a free Gaussian density.

Both \(m\) and \(\varphi\) are site-gauge invariant. Under
\[
z'=\rho_\Lambda(g)z,\qquad
U'_{vw}=g_vU_{vw}g_w^{-1},
\]
the measures are unchanged and \(V(U',z')=V(U,z)\). Therefore
\[
\boxed{
d\widehat P_q(g,U',z')
=
dg\,
\frac{\varphi(z')e^{-V(U',z')}
e^{2\kappa\operatorname{Re}\langle q,z'\rangle}}
{\lambda_0\varphi(q)}
\,dU'\,dz'.}
\tag{TA3}
\]
The temporal angles are exactly independent Haar variables in these transported coordinates.

After integrating \(U\), this proves the pointwise normalization identity
\[
Z_g(q):=
\int m(z)\varphi(z)
e^{2\kappa\operatorname{Re}\langle q,\rho_\Lambda(g)z\rangle}\,dz
=\lambda_0\varphi(q)
\quad\text{for every }g.
\tag{TA4}
\]
For a bounded neutral endpoint source \(u\), its conditional mean given \(q,g\) is consequently independent of \(g\):
\[
\mathbb E[u(Z)\mid q,g]=(Pu)(q),
\qquad
\boxed{\operatorname{Var}_{g\mid q}
\bigl(\mathbb E[u(Z)\mid q,g]\bigr)=0.}
\tag{TA5}
\]
The conditional law of \(Z\) itself rotates with \(g\). Neutrality of the source, rather than equality of those untransported auxiliary laws, gives (TA5).

This cancellation does not assert that all temporal-link marks vanish. An arbitrary mark in (TA2) is evaluated after the same change of variables in (TA3), with every remaining \(g\)-dependence retained. A mark invariant under the outer site-gauge action becomes a function of the transported boundary and spatial links. An open charged mark generally does not.

## The angular score has an exact compensating curvature

Fix \(q,g\), integrate the spatial links, and denote the resulting normalized auxiliary law by \(\eta_{q,g}\). Vary one site angle by \(g_t=e^{tX}g\), with \(X\) in its Lie algebra. Since \(Z_g(q)\) is constant in \(g\), the normalized score and its derivative are
\[
s_X(z)=
2\kappa\operatorname{Re}
\langle q,d\rho_\Lambda(X)\rho_\Lambda(g)z\rangle,
\qquad
s'_X(z)=
2\kappa\operatorname{Re}
\langle q,d\rho_\Lambda(X)^2\rho_\Lambda(g)z\rangle.
\tag{TA6}
\]
For each fixed \(q\), differentiation under the integral is justified by the Gaussian bound on \(m\) in RS3 and Cauchy–Schwarz with
\(\varphi\in L^2(m\,dz)\). Polynomial factors times the linear exponential remain integrable.

The first and second derivatives of (TA4) give
\[
\boxed{
\mathbb E_{\eta_{q,g}}s_X=0,
\qquad
\operatorname{Var}_{\eta_{q,g}}(s_X)
+\mathbb E_{\eta_{q,g}}s'_X=0.}
\tag{TA7}
\]
For every bounded neutral \(u\), differentiating its constant mean in (TA5) gives
\[
\boxed{\operatorname{Cov}_{\eta_{q,g}}(u,s_X)=0.}
\tag{TA8}
\]
For a complex source this is understood componentwise, or with the chosen conjugate in the covariance. All normalizers remain those of the source-free law. The positive Fisher term in (TA7) cannot be retained while discarding its compensating curvature.

For \(G=SU(2)\) in its defining representation, choose at one site
\(X=i\sigma_3/2\), so \(X^2=-I/4\). Then
\[
\operatorname{Var}_{\eta_{q,g}}(s_X)
=
\frac{\kappa}{2}\,
\mathbb E_{\eta_{q,g}}
\operatorname{Re}
\sum_a q_v^{(a)*}g_vz_v^{(a)}.
\tag{TA9}
\]
If \(q_v\ne0\), the real linear score \(s_X(z)\) is not constant. The strictly positive auxiliary density gives it strictly positive variance. Nevertheless its covariance with every neutral source remains zero. This is an exact non-Abelian score calculation; its positivity describes the gauge transport of the auxiliary coordinates.

## A genuine Wilson source sees the cancellation

Take an open spatial square, \(G=SU(2)\), and at least two auxiliary copies. Its bounded Wilson source and its actual RS compression are
\[
F(U)=\frac12\operatorname{Tr}(U_p),\qquad
f(z)=
\frac{\int e^{-V(U,z)}F(U)\,dU}{m(z)}.
\tag{TA10}
\]
Thus \(f\) belongs to the returned neutral frame-source family; it is not an independently chosen radial auxiliary observable.

At \(z=0\), all four spatial links have independent Haar laws and \(f(0)=0\).
At each vertex set the first two auxiliary columns to \(z_v=R I_2\), \(R>0\), and all further columns to zero. Each oriented spatial link then has the central conditional density
\[
\frac{e^{t a(U)}}{\int e^{t a(V)}dV}\,dU,
\qquad
a(U)=\tfrac12\operatorname{Tr}U,\qquad
t=4\kappa R^2>0.
\]
Put
\[
b(t)=\frac{\int a(U)e^{t a(U)}dU}
{\int e^{t a(U)}dU}.
\]
Conjugation symmetry makes the mean matrix \(b(t)I_2\). Inversion preserves this mean; independence of the four link conditionals therefore gives
\[
\boxed{f(z_R)=b(t)^4>0.}
\tag{TA11}
\]
The strict inequality follows by pairing \(a\) and \(-a\) under Haar measure: the numerator is the integral of \(a\sinh(ta)\), positive away from \(a=0\). The function \(f\) is continuous, so these distinct values imply nonconstancy on the full-support vacuum law.

Centering \(f\) in \(\pi\) produces a nonzero physical source in the cyclic frame sector. Equation (TA8) still gives zero angular score covariance for this source, while (TA9) is strictly positive at every tested inner boundary with \(q_v\ne0\). The example rules out using that raw temporal angular Fisher positivity as a lower frame for the complete neutral source response.

## The spatial conditional law keeps the actual vacuum

The temporal cancellation extends to a \(k\)-step outer slab by successively transporting each auxiliary slice and its spatial links to temporal gauge, while fixing the inner boundary \(q\). The \(k\) temporal angle fields then factor as independent Haar variables. The outer \(\varphi\) is invariant and stays in the amplitude.

Write \(A=P^k\), let \(z_0=q\), and denote the transported spatial links of the \(k\) outer slices by
\(\Theta=(U_1,\ldots,U_k)\). Define
\[
\begin{aligned}
W_q(\Theta,z_1,\ldots,z_k)
&=\varphi(z_k)
\exp\!\left[
-\sum_{j=1}^kV(U_j,z_j)
+2\kappa\sum_{j=1}^k
\operatorname{Re}\langle z_{j-1},z_j\rangle
\right],\\
\mathcal Z_\Theta(q)
&=\int W_q(\Theta,z_1,\ldots,z_k)
\prod_{j=1}^k dz_j .
\end{aligned}
\tag{TA12}
\]
The complete outer-slab normalization is
\(\int\mathcal Z_\Theta(q)d\Theta=\lambda_0^k\varphi(q)\).
Consequently its actual spatial and auxiliary conditionals are
\[
\boxed{
\omega_q(d\Theta)
=\frac{\mathcal Z_\Theta(q)}
{\lambda_0^k\varphi(q)}\,d\Theta,
\qquad
\eta_{q,\Theta}(dz_1\cdots dz_k)
=\frac{W_q(\Theta,z_1,\ldots,z_k)}
{\mathcal Z_\Theta(q)}\prod_j dz_j.}
\tag{TA13}
\]
Unlike the temporal Haar angles, the spatial links have a vacuum-weighted posterior. The conditional auxiliary law retains \(\varphi(z_k)\) and is not generally Gaussian.

For a neutral endpoint source \(u\), set
\[
M_u(q,\Theta)=\mathbb E_{\eta_{q,\Theta}}u(z_k),
\qquad
N_u(q,\Theta)=\operatorname{Var}_{\eta_{q,\Theta}}u(z_k).
\]
The conditional variance splits exactly:
\[
\operatorname{Var}_{A(q,\cdot)}u
=
\mathbb E_{\omega_q}N_u(q,\Theta)
+\operatorname{Var}_{\omega_q}M_u(q,\Theta).
\tag{TA14}
\]
The equality concerns neutral sources on the quotient; the transported auxiliary representatives have been used consistently. On the original untransported variables all temporal angles and transformed marks remain available through (TA3).

Integrate in the selected vacuum and define
\[
\begin{aligned}
\mathcal V_{\rm aux}(u)
&=\int\pi(dq)\,\mathbb E_{\omega_q}N_u,\\
\mathcal V_{\rm sp}(u)
&=\int\pi(dq)\,\operatorname{Var}_{\omega_q}M_u.
\end{aligned}
\]
Then
\[
\boxed{
\mathcal V_{\rm aux}(u)+\mathcal V_{\rm sp}(u)
=\|u\|_\pi^2-\|Au\|_\pi^2.}
\tag{TA15}
\]
Both terms are nonnegative, but neither is a separately selected Hamiltonian or gap.

For a spatial link varied as \(U_e(t)=e^{tX}U_e\), the normalized first-source derivative, whenever differentiation is admitted, is
\[
\frac{d}{dt}M_u(q,\Theta(t))\bigg|_{t=0}
=
\operatorname{Cov}_{\eta_{q,\Theta}}
\left(
u(z_k),\,
2\kappa\operatorname{Re}
\sum_a z_v^{(a)*}d\rho(X)\rho(U_e)z_w^{(a)}
\right).
\tag{TA16}
\]
The link belongs to its specified slice in (TA12). This is the derivative of a conditional coordinate with the selected \(\varphi\) held fixed, not a variation of the constitutive action followed by recomputing its vacuum. A source with explicit \(U_e\)-dependence contributes its own derivative as well. The covariance, including its normalization subtraction, uses the full vacuum-weighted law in (TA13).

## Resolve the actual four-boundary surplus

Use OI19's inner pair \((x,y)\), outer pair \((x',y')\), and
\(h_f(x,y)=f(y)-(Af)(x)\).
The outer branches are independent conditional on \(x,y\), so their conditional variance is
\[
\operatorname{Var}\bigl(f(Y')-(Af)(X')\mid x,y\bigr)
=
\operatorname{Var}_{A(y,\cdot)}f
+\operatorname{Var}_{A(x,\cdot)}Af.
\tag{TA17}
\]
The two inner marginals are both \(\pi\). Combining (TA15) with OI24 therefore gives the complete split
\[
\begin{aligned}
V_Q(h_f)
&=\mathcal V_{\rm aux}(f)+\mathcal V_{\rm sp}(f)
+\mathcal V_{\rm aux}(Af)+\mathcal V_{\rm sp}(Af),\\
C_{\rm lag}(h_f)
&=2\mathcal V_{\rm aux}(Af)+2\mathcal V_{\rm sp}(Af),\\
\boxed{V_Q(h_f)-C_{\rm lag}(h_f)}
&=\boxed{
[\mathcal V_{\rm aux}(f)-\mathcal V_{\rm aux}(Af)]
+[\mathcal V_{\rm sp}(f)-\mathcal V_{\rm sp}(Af)].}
\end{aligned}
\tag{TA18}
\]
Their sum equals \(\langle f,(I-A^2)^2f\rangle_\pi\), as required by the already proved ledger. There is no reason from (TA14) alone for either bracket in (TA18) to be nonnegative separately. In particular, positivity of the spatial angular variance \(\mathcal V_{\rm sp}\) does not bound its difference after transport.

The OI25 target is consequently
\[
[\mathcal V_{\rm aux}(f)-\mathcal V_{\rm aux}(Af)]
+[\mathcal V_{\rm sp}(f)-\mathcal V_{\rm sp}(Af)]
\ge
c[\mathcal V_{\rm aux}(f)+\mathcal V_{\rm sp}(f)]
\tag{TA19}
\]
on all normalized innovations in the physical source sector, with \(c>0\) uniform in the required limits. The terms now have actual conditional amplitudes. Temporal angular positivity cannot fill the missing margin because of (TA5)–(TA8); spatial angular positivity alone cannot fill it because the transported cost in (TA18) is retained.

## Preserve marked laws when resolving the conditionals

For one microscopic step per slab, the complete restored four-boundary amplitude is
\[
\begin{aligned}
d\widehat\Gamma
={}&\lambda_0^{-3}\varphi(z_0)\varphi(z_3)
\prod_{j=0}^{3}
\left[e^{-V(U_j,z_j)}dU_j\,dz_j\right]\\
&\times
\prod_{j=0}^{2}
\left[
e^{2\kappa\operatorname{Re}
\langle z_j,\rho_\Lambda(g_j)z_{j+1}\rangle}dg_j
\right].
\end{aligned}
\tag{TA20}
\]
Its chronology is \(z_0=x',z_1=x,z_2=y,z_3=y'\).
Integrating spatial and temporal links gives exactly OI28. For a \(k\)-step slab, retain the corresponding \(3k\) microscopic transitions and \(\lambda_0^{-3k}\), with the same two outer vacuum factors.

Every bounded joint frame/auxiliary source multiplies this amplitude before any conditional integration. A temporal gauge change transports that source together with the auxiliary vectors and spatial links. At a common slice, all original frame factors stay inside the same \(e^{-V}/m\) integral, including the finite [[auxiliary-boundary-sufficiency-and-the-wilson-source-algebra|RS/AS conditional-covariance defect]]. No marked denominator is recomputed. Arbitrary complex marks do not automatically preserve the nonnegative variance decomposition, although their full multilinear amplitudes remain exact.

The useful reduction is therefore specific. Temporal gauge transport has been removed from the proposed source of a positive margin by an exact cancellation. The remaining test is the coupled spatial and auxiliary decrease in (TA18), in the actual reflected vacuum and with its complete source normalization. Neither a free Gaussian replacement nor an uncorrected angular Fisher term evaluates that decrease.
