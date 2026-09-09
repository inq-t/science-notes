# Seam Coupling Response and the Vacuum Cap

The vacuum response to changing a spatial seam is fixed by the same chronological transfer that generates its histories. Its logarithmic derivative is an integrated time response, with a half-weight at the boundary and full weights in the interior. Rectangular comparisons across a spatial cut remove the marginal normalizers and retain this complete response. Thus a bounded local seam action need not have a uniformly bounded vacuum effect: the missing estimate concerns the accumulated chronological influence of that action.

**Status: exact at fixed finite graph and coupling; exact product-carrier control; open uniform interface estimate.** [[cycle-moments-and-the-pure-gauge-vacuum-return|CM7–21]] returns the actual finite Wilson transfer and vacuum. [[vacuum-aligned-innovation-completion/boundary-action-fixed-points-and-physical-linearization|Boundary-action linearization]] identifies the derivative of temporal layer addition with the physical transfer. The derivative here changes the spatial interaction in every layer of that same law.

## Change one interaction in the actual transfer

Let \(T\) be a positive self-adjoint compact transfer with a strictly positive continuous kernel on the finite compact configuration carrier. Write
\[
T\psi=\lambda\psi,\qquad \psi>0,\qquad
\int\psi^2\,dU=1,\qquad
\pi(dU)=\psi(U)^2dU.
\]
All source functions below are real. For a bounded continuous invariant seam potential \(V\), define
\[
T_s=e^{-sV/2}Te^{-sV/2},\qquad
T_s\psi_s=\lambda_s\psi_s,\qquad
P_s f=\frac{T_s(\psi_s f)}{\lambda_s\psi_s}.
\tag{SV1}
\]
The vacuum is chosen positive and normalized for every \(s\) in a fixed finite interval. The simple Perron eigenvalue and its vector depend differentiably on \(s\). Positivity and the physical support are retained. The Wilson instance changes the coefficients of selected spatial plaquettes, keeping the temporal kernel and its duration fixed:
\[
V(U)=\sum_{p\in\mathcal P_{\rm seam}}
\alpha_p\,[n-\operatorname{Re}\chi_\rho(U_p)].
\tag{SV2}
\]
This is a diagnostic deformation of an already declared action. It does not independently choose a new clock or assert that the homogeneous coupling trajectory follows this deformation.

Set
\[
u_s=\partial_s\log\psi_s,\qquad
V_{c,s}=V-\pi_s(V).
\]
Normalization gives \(\pi_s(u_s)=0\). Differentiating the eigenvalue equation and using
\(T_s'=-\tfrac12(VT_s+T_sV)\) yields
\[
\boxed{\partial_s\log\lambda_s=-\pi_s(V),\qquad
(I-P_s)u_s=-\frac12(I+P_s)V_{c,s}.}
\tag{SV3}
\]
For example, division of the differentiated equation by \(\lambda_s\psi_s\) gives
\[
-\frac12(V+P_sV)+P_su_s
=\partial_s\log\lambda_s+u_s.
\]
Integration against \(\pi_s\) gives the scalar in (SV3); subtraction then gives its centered part.

At each fixed finite graph the centered contraction satisfies
\(q_s=\|P_s|_{L^2_0(\pi_s)}\|<1\). Therefore
\[
\boxed{
u_s=-\frac12V_{c,s}-\sum_{j=1}^{\infty}P_s^jV_{c,s}
=-\frac12(I-P_s)^{-1}(I+P_s)V_{c,s}.}
\tag{SV4}
\]
The series converges in \(L^2(\pi_s)\). The continuous strictly positive finite kernel also supplies fixed-graph uniform ergodicity, so for these continuous sources it converges uniformly and may be evaluated at specified boundary configurations. No volume-uniform convergence rate is claimed.

Each \(P_s^j\) is actual chronological composition. The inverse is a concise description of its convergent sum at fixed graph, not an inserted gap certificate. Its finite-word truncation has the exact remainder
\[
u_s+\frac12V_{c,s}+\sum_{j=1}^{m}P_s^jV_{c,s}
=-\sum_{j=m+1}^{\infty}P_s^jV_{c,s},
\]
\[
\left\|u_s+\frac12V_{c,s}
+\sum_{j=1}^{m}P_s^jV_{c,s}\right\|_2
\le \frac{q_s^{m+1}}{1-q_s}\|V_{c,s}\|_2.
\tag{SV5}
\]
This bound displays exactly where the existing finite-volume gap enters; it is not a proof that the bound survives refinement.

## The closed normalizer has the same chronological response

For a fixed bounded invariant source \(F\),
\[
\partial_s\pi_s(F)
=2\langle F-\pi_sF,u_s\rangle_{\pi_s}
=-\left\langle F-\pi_sF,
(I-P_s)^{-1}(I+P_s)V_{c,s}\right\rangle_{\pi_s}.
\tag{SV6}
\]
In particular, the same transfer normalization obeys
\[
\boxed{
\partial_s^2\log\lambda_s
=\operatorname{Var}_{\pi_s}(V)
+2\sum_{j=1}^{\infty}
\operatorname{Cov}_{\pi_sP_s^j}
\bigl(V(X_0),V(X_j)\bigr).}
\tag{SV7}
\]
The covariance at lag zero appears once; positive and negative chronological lags give the factor two. The sum is nonnegative because \(P_s\) is a positive self-adjoint operator. This is the infinite temporal-cylinder response per slice at fixed spatial graph. It is a derivative of the actual leading normalization, not a new auxiliary Fisher form. [[closed-normalization-and-cosmic-response|Closed-normalization response]] owns the proposed common microscopic and cosmological readout; (SV7) supplies a finite chronological instance without assigning a cosmological interpretation to it.

The same kernel therefore controls the vacuum change, the closed-normalization susceptibility and the temporal persistence of a seam source. None of these identities removes the need for an estimate uniform on the complete physical carrier.

## What the two vacuum caps retain

Split the spatial configuration into left variables \(a\), right variables \(b\) and retained separator variables \(z\), using the actual product frame carrier. Conditional densities are formed from \(\pi_s=\psi_s^2dU\). Define
\[
c_{s,z}(a,b)=
\left[
\frac{\pi_s(a,b\mid z)}
{\pi_s(a\mid z)\pi_s(b\mid z)}
\right]^{1/2}.
\tag{SV8}
\]
For a function \(f(a,b,z)\), let
\[
(\mathfrak r_z f)(a,a';b,b')
=f(a,b,z)+f(a',b',z)
-f(a,b',z)-f(a',b,z).
\]
Every function of \((a,z)\) alone, of \((b,z)\) alone, or of \(z\) alone cancels from \(\mathfrak r_z\). Since \(\log c_{s,z}\) is \(\log\psi_s\) minus such functions,
\[
\boxed{
\mathfrak r_z\log c_{s,z}=\mathfrak r_z\log\psi_s,\qquad
\partial_s\mathfrak r_z\log c_{s,z}
=-\frac12\mathfrak r_zV
-\sum_{j=1}^{\infty}\mathfrak r_z(P_s^jV_{c,s}).}
\tag{SV9}
\]
The cancellation applies to this rectangular comparison. It does not permit dropping the marginal or history normalizers from source expectations.

For a finite coupling interval,
\[
\mathfrak r_z\log\frac{c_{s_1,z}}{c_{s_0,z}}
=\int_{s_0}^{s_1}\mathfrak r_z u_s\,ds.
\tag{SV10}
\]
Thus an interface estimate can be tested on the transported seam sources in (SV9), retaining a finite chronological prefix and an explicitly bounded tail. A bare spatial bound on \(\|V\|_\infty\) supplies no uniform bound on that tail. Nor may an \(L^2\) bound alone be turned into a bound on pointwise rectangular oscillation; (SV9) uses the additional fixed-graph uniform convergence specified above.

In a sewn finite history both outer caps occur. Their logarithmic derivatives add before the full sourced normalization is differentiated. The covariance between the two cap scores is consequently retained. This is a restriction on the proposed estimate, rather than permission to replace the interacting vacuum by the product of its spatial marginals.

## A product control resolves which temporal energies enter

Only for this control, assume a product carrier and product transfer
\(P_0=P_L\otimes P_R\), with product vacuum \(\pi_L\otimes\pi_R\). This factorization is an explicit hypothesis, not a consequence of gauge fixing an arbitrary Wilson cut. Centering separately in each factor defines
\[
\mathcal Q_{\rm conn}
=(I-\Pi_L)\otimes(I-\Pi_R),\qquad
V_{\rm conn}=\mathcal Q_{\rm conn}V,
\]
where \(\Pi_L,\Pi_R\) project onto their vacuum constants. At the product state \(c_{0}=1\); differentiation of all three conditional densities in (SV8) gives
\[
\left.\partial_s\log c_s\right|_{s=0}
=-\frac12(I-P_L\otimes P_R)^{-1}
(I+P_L\otimes P_R)V_{\rm conn}.
\tag{SV11}
\]
All terms depending on only one factor cancel. For centered eigenfunctions
\[
P_L f_L=e^{-a_tE_L}f_L,\qquad
P_R f_R=e^{-a_tE_R}f_R,
\]
the coefficient on a product term \(v\,f_Lf_R\) in \(V_{\rm conn}\) is
\[
\boxed{
-\frac v2
\frac{1+e^{-a_t(E_L+E_R)}}{1-e^{-a_t(E_L+E_R)}}
=-\frac v2\coth\!\left(\frac{a_t(E_L+E_R)}2\right).}
\tag{SV12}
\]
The response sees the sum of the two chronological energies. It grows as \(-v/[a_t(E_L+E_R)]\) when that sum becomes small. The vacuum mode has been removed, but low-energy connected modes remain. A bounded seam coefficient therefore does not by itself exclude a large connected vacuum response.

This control identifies a concrete next calculation in a gauge theory: retain the charged boundary frames and their actual joint gauge projection when expanding the seam source into temporal modes. Independently taking the gauge-neutral quotient of each side may erase precisely the channels carried across the interface. [[gauge-boundary-frame-gluing/inq|Charged boundary gluing]] owns that distinction.

## The seam score is itself a chronological innovation

The same derivative also supplies the change of the actual transition law. Put
\[
w_s=u_s-\frac12V_{c,s}=-(I-P_s)^{-1}V_{c,s},
\qquad (I-P_s)w_s=-V_{c,s}.
\]
If \(p_s(x,y)\) is the density of \(P_s(x,dy)\), differentiation of (SV1) gives
\[
\boxed{
\partial_s\log p_s(x,y)
=w_s(y)-(P_sw_s)(x)=\delta_s w_s(x,y).}
\tag{SV13}
\]
Indeed, the direct derivative is
\(u_s(y)-u_s(x)-[V(x)+V(y)]/2+\pi_sV\);
(SV3) gives
\(P_sw_s=u_s+V_{c,s}/2\), yielding (SV13).
The score is conditionally centered at every incoming boundary. It is exactly the one-step oriented innovation of a source forced by the seam potential, rather than an independently supplied comparison direction.

Consequently
\[
\boxed{
\partial_s(P_sf)(x)
=\operatorname{Cov}_{P_s(x,\cdot)}(f,w_s),\qquad
\partial_s P_s^k
=\sum_{j=0}^{k-1}P_s^j(\partial_sP_s)P_s^{k-1-j}.}
\tag{SV14}
\]
These are derivatives of a fixed source \(f\); an \(s\)-dependent source contributes its own derivative. The operator formula computes how the transported source \(P_s^kf\), including its spatial spread, changes when the seam changes.

Its transition Fisher information, in the actual stationary pair norm, is
\[
\boxed{
\|\partial_s\log p_s\|_{L^2(\pi_sP_s)}^2
=\|\delta_sw_s\|^2
=\langle w_s,(I-P_s^2)w_s\rangle_{\pi_s}
=\partial_s^2\log\lambda_s.}
\tag{SV15}
\]
The last equality follows from (SV7) and \((I-P_s)w_s=-V_{c,s}\). Thus the closed-normalization susceptibility is an actual chronological innovation norm for this deformation. It is not a same-wall KMS defect, an auxiliary-coordinate gradient norm or a claim of a uniform positive floor.

For \(N\ge1\), the normalized stationary history
\(d\Gamma_{s,N}=\pi_s(dx_0)\prod_{j=0}^{N-1}P_s(x_j,dx_{j+1})\),
the complete score is equivalently
\[
\boxed{
\partial_s\log d\Gamma_{s,N}
=2u_s(x_0)+\sum_{j=0}^{N-1}\delta_sw_s(x_j,x_{j+1})
=u_s(x_0)+u_s(x_N)
-\frac12V_{c,s}(x_0)
-\sum_{j=1}^{N-1}V_{c,s}(x_j)
-\frac12V_{c,s}(x_N).}
\tag{SV16}
\]
Both vacuum caps, endpoint half-actions, all interior actions and the derivative of \(\lambda_s^{-N}\) are present. Source differentiation therefore uses covariance with this complete score. An additional conditioning or adjoining-block normalization subtracts its conditional mean; it cannot discard either cap. This gives an exact finite-source calculation for comparing the seam effect before and after the replica integration.

## The second variation retains the normalization contact term

All derivatives below are at fixed finite graph and fixed temporal kernel. Put
\[
\chi_s=\partial_s^2\log\lambda_s,\qquad
g_s(x)=\operatorname{Var}_{P_s(x,\cdot)}(w_s).
\]
Then \(\pi_sg_s=\chi_s\) by (SV15). Differentiating (SV3), applying (SV14) to the fixed argument \(w_s\), and using
\(\partial_s\pi_sV=-\chi_s\), gives
\[
\boxed{
(I-P_s)\dot u_s=g_s-\chi_s,\qquad
\pi_s\dot u_s=-2\pi_s(u_s^2).}
\tag{SV17}
\]
The second equality differentiates \(\pi_su_s=0\), including
\(\partial_s\pi_s=2u_s\pi_s\). Thus
\[
\dot u_s=(I-P_s)^{-1}(g_s-\chi_s)-2\pi_s(u_s^2).
\]
The inverse in this formula acts only on the centered function \(g_s-\chi_s\). The subtraction is the scalar fixed by normalization; changing it changes the second source response.

Write \(\mathcal L_{s,N}=\partial_s\log d\Gamma_{s,N}\) for the complete score in (SV16). For \(N\ge1\),
\[
\boxed{
\partial_s\mathcal L_{s,N}
=\dot u_s(x_0)+\dot u_s(x_N)-N\chi_s.}
\tag{SV18}
\]
There are \(N\) full seam weights after the endpoint halves are counted. The negative contact term is the derivative of the actual leading normalization. A positive transition Fisher information therefore does not imply that every history observable has positive second response.

For a fixed bounded real source \(F\), use the raw stationary moments
\[
C_N(s)=\mathbb E_{\Gamma_{s,N}}[F(X_0)F(X_N)]
=\langle F,P_s^NF\rangle_{\pi_s}.
\]
Their derivatives are
\[
\boxed{
\begin{aligned}
C_N'&=\mathbb E[F(X_0)F(X_N)\mathcal L_{s,N}],\\
C_N''&=\mathbb E\!\left[
F(X_0)F(X_N)
\{\mathcal L_{s,N}^2+\dot u_s(X_0)+\dot u_s(X_N)-N\chi_s\}
\right].
\end{aligned}}
\tag{SV19}
\]
At \(N=0\), instead use
\(C_0=\pi_s(F^2)\),
\(C_0'=2\pi_s(F^2u_s)\), and
\(C_0''=\pi_s[F^2(4u_s^2+2\dot u_s)]\).
These are raw moments of the fixed source. Differentiating a separately centered covariance requires differentiating its subtracted mean square as well.

The oriented innovation norm, surplus and their normalized quotient are
\[
D_k=C_0-C_{2k},\qquad
S_k=C_0-2C_{2k}+C_{4k},\qquad
\mathfrak c_k(F)=\frac{S_k}{D_k}\quad(D_k>0).
\]
Their coefficients cancel \((\pi_sF)^2\) identically, so these raw-moment formulas already include the moving centering required by the physical vacuum complement. Differentiation gives
\[
\boxed{
\mathfrak c_k'
=\frac{S_k'-\mathfrak c_kD_k'}{D_k},\qquad
\mathfrak c_k''
=\frac{S_k''-\mathfrak c_kD_k''-2\mathfrak c_k'D_k'}{D_k}.}
\tag{SV20}
\]
Neither sign follows from \(\chi_s\ge0\).

In the useful special case \(C_0(s)=1\), \(P_0F=\alpha F\), and all \(C_N'(0)=0\),
\[
\boxed{
\mathfrak c_k''(0)=
\frac{C_{4k}''(0)-(1+\alpha^{2k})C_{2k}''(0)}
{1-\alpha^{2k}}.}
\tag{SV21}
\]
[[adjacent-wilson-plaquette-and-the-chronological-surplus|The adjacent Wilson plaquette]] satisfies these conditions while its evolved source leaves the original region. [[finite-seam-response-and-the-two-spin-surplus|The finite seam-sign control]] separately exhibits opposite source responses under the same nonnegative seam deformation and distinguishes a regional quotient from the full-source floor.

## The relation to seek

The elementary identity is (SV3): the seam action forces its vacuum response through the existing chronology. A useful uniform theorem would control the complete marked response of this forced change under adjacent-block sewing, including both caps, the changed endpoint law and the separator channels. That theorem must act on the oriented innovation carrier of [[oriented-innovation-and-finite-temporal-repair|OI]], rather than only on spatial gradients or selected seam eigenmodes.

The present result makes the next conjecture more specific. Seek cancellation or contraction of the transported seam-response tail in the actual difference \(V_Q-C_{\rm lag}\), using the non-Abelian boundary composition. Bounding (SV4) by an already uniform global gap would reverse the intended proof. Calculating the finite words and their complete joint source response first leaves room for a stronger compositional law to supply the missing estimate.
