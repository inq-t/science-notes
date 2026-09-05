# Finite Witnesses and Uniform Escape

On a compact family of backgrounds, strict instability witnessed in finitely many coordinates at every background forces one finite witness radius and one uniform negative margin. For central Wilson contexts this gives an exact alternative: either remote Hessian escape is uniformly local, or a single infinite two-well context has nonnegative Hessian against every finitely supported remote variation. The theorem reduces coverage to a stability classification; it does not establish instability, nonlinear escape, or a physical spectral gap.

## Compactness converts pointwise strict witnesses into uniform ones

Let \(K\) be compact and let \(\lambda_R:K\to\mathbb R\), \(R\ge R_0\), be continuous functions with \(\lambda_{R+1}\le\lambda_R\). Then
\[
\boxed{
(\forall\omega\in K)(\exists R)\ \lambda_R(\omega)<0
\quad\Longleftrightarrow\quad
(\exists R_*,\nu>0)(\forall\omega\in K)\
\lambda_{R_*}(\omega)\le-\nu.}
\tag{FC1}
\]
For the forward direction, the increasing open sets
\(O_R=\{\lambda_R<0\}\) cover \(K\). A finite subcover and nesting give
\(K=O_{R_*}\). The continuous function \(\lambda_{R_*}\) has a negative maximum on \(K\); its opposite is the required \(\nu\). The reverse implication is immediate.

Equivalently, exactly one of the following holds:

- one radius and one strictly negative margin work everywhere;
- some \(\omega_\infty\in K\) has \(\lambda_R(\omega_\infty)\ge0\) for every radius.

For the second formulation, the sets \(K_R=\{\lambda_R\ge0\}\) are compact and nested. If they are all nonempty, compactness makes their intersection nonempty. A finite numerical search with no witness does not establish this premise for every radius.

Strict negativity matters. A family of zero modes is not a family of escape directions. Compactness is also essential: a noncompact parameter family may require unbounded radii or have margins tending to zero.

## The central Wilson family is an actual compact carrier

Let \(E\) be the positively oriented links of \(\mathbb Z^4\), and put
\[
\Omega=\{1,z,z^2\}^{E},\qquad z=e^{2\pi i/3}.
\tag{FC2}
\]
Give \(\Omega\) its compact product topology. Each point \(\omega\) specifies actual links \(U_e=\omega_e I\), not independently assigned plaquette values. All lattice compatibility identities are automatic.

Fix an active edge \(e\). Its frozen star \(F\) consists of every link in any plaquette containing \(e\): the active link and eighteen others. Let \(K\subset\Omega\) be the nonempty cylinder where its six complementary staples sum to \(-3I\). By [[rg-covariance-residue/singular-staple-fibers-and-exact-conditional-symmetries|extremal source rigidity]], their products are three \(zI\)'s and three \(z^2I\)'s. The condition depends on finitely many finite-alphabet coordinates, so \(K\) is both open and closed, hence compact. The three central rotations can also be included as a finite union.

For real finitely supported link cochains \(a\) vanishing on \(F\), define
\[
q_\omega(a)=\sum_p w_p(\omega)(da)_p^2,\qquad
w_p(\omega)=
\begin{cases}1,&U_p=I,\\-1/2,&U_p\ne I.\end{cases}
\tag{FC3}
\]
The sum includes every plaquette touched by \(a\), including plaquettes crossing its support boundary. This is the central Wilson Hessian divided by \(\beta\), in one unit Lie-algebra direction. The eight color directions have the same scalar form at these central backgrounds. The sum does not define an infinite-volume Gibbs state; it defines a finite quadratic variation of the action.

Let \(E_R\) be nested whole-link boxes exhausting \(E\), put \(J_R=E_R\setminus F\), and take \(R_0\) large enough that \(J_R\ne\varnothing\). Define
\[
\lambda_R(\omega)=
\min_{\substack{\operatorname{supp}a\subset J_R\\
\sum_{j\in J_R}a_j^2=1}}q_\omega(a).
\tag{FC4}
\]
Only finitely many background links enter this finite symmetric matrix, so \(\lambda_R\) is locally constant. Zero extension gives
\(\lambda_{R+1}\le\lambda_R\).

Equation (FC1) now proves the exact central-context alternative:
\[
\boxed{
\begin{gathered}
\text{every }\omega\in K\text{ has a strict finite remote negative mode}\\
\Longleftrightarrow\
\exists R_*,\nu>0:\ \lambda_{R_*}(\omega)\le-\nu
\quad\forall\omega\in K.
\end{gathered}}
\tag{FC5}
\]
If this fails, there is one \(\omega_\infty\in K\) with
\[
q_{\omega_\infty}(a)\ge0
\quad\text{for every finitely supported }a\text{ vanishing on }F.
\tag{FC6}
\]
Neither alternative has been established for this \(K\). The point is that escape lengths cannot merely grow forever over this compact central family without producing such a limiting obstruction.

## A finite certificate has an exact verification target

At a fixed radius only finitely many central link patterns affect (FC4). Its matrices have rational entries. A verified strictly negative rational test cochain for every compatible pattern would provide a finite certificate of (FC5), with margin the minimum of the finitely many positive numbers \(-q_\omega(a)/\|a\|^2\). Rational witnesses suffice whenever a strict real witness exists, by continuity. The number of patterns may be prohibitively large; no exhaustive certificate is supplied here.

[[compatible-image-and-signed-curvature|Compatible-image compression]] gives an equivalent sign test. If \(d_R\) is the cochain derivative restricted to \(J_R\), retaining all touched plaquettes, and \(B_\omega\) selects the nontrivial ones, then
\[
\lambda_R(\omega)<0
\quad\Longleftrightarrow\quad
\left\|B_\omega d_R(d_R^*d_R)^\dagger d_R^*B_\omega\right\|>\tfrac23.
\tag{FC7}
\]
The norm threshold tests the overlap of compatible curvature with the negative plaquette sector. The reference derivative may have gauge null directions, depending on the selected support. In any case, nonnegative Hessian is only a second-order stability statement, not a nonlinear local minimum.

Any finite neighborhood involved in this test can be copied to a sufficiently large periodic lattice without changing its tested Hessian. Additional plaquettes where the copied neighborhood is joined to its periodic exterior must not enter the selected support; keeping a full plaquette collar ensures this.

## The missing physical steps remain distinct

Remote means that every differentiated link lies outside the frozen active star. This is sufficient for commutation with the active conditional law, but excludes compensating motions of factors inside its staple paths. Failure of (FC5) would not exclude every source-preserving or noncommuting escape mechanism.

A negative cochain does not itself supply a globally defined gauge-covariant diffusion field. Frame transport, derivatives of its coefficients, the actual symmetric generator and a global form bound must still be checked, as in [[rg-covariance-residue/critical-context-and-collective-escape|collective Wilson escape]]. A finite cover of Hessian witnesses does not automatically combine their Lyapunov remainders.

The criterion concerns the declared central cylinder, not all unfavorable \(SU(3)\) sources. Its instability premise, noncentral coverage, full-law coercivity, physical-time reconstruction and continuum limit remain open. [[library/k-string-tensions-and-center-vortices-at-large-n/inq|Greensite--Olejnik's]] classical center-vortex stability result for \(N>4\) does not decide this \(SU(3)\) frozen-star classification.
