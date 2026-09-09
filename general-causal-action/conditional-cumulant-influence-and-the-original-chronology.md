# The Conditional Cumulant Has a Response in the Original Chronology

The derivative of the local conditional fourth cumulant is an exact mixed susceptibility of the original vacuum dynamics. Its influence observable includes every change of the conditional mean, covariance and retained marginal. At harmonic order the character response has a negative time-resolved kernel, whose integral is the positive cumulant coefficient. The kernel has an integrable tail uniformly in patch size. Returning that entire time profile to the growing compact theory requires more than the already controlled integrated statistic.

**Status: exact finite compact influence and susceptibility identities; evaluated harmonic temporal coefficient and uniform harmonic tail.** [[conditional-replica-cumulants-and-amplitude-stability|CRA]] constructs the same statistic from four conditional replicas. [[uniform-local-conditional-character-return|The uniform conditional return]] controls its actual parameter derivative. [[conditional-vacuum-rigidity-and-the-physical-gap|CV]] owns the complete physical-source susceptibility criterion. The replicas below express products in the inherited state; they do not define a replacement evolution.

## Differentiate the complete conditional statistic

Let \(Y=\widehat X_{r,h}\) be the original bounded GM vector mark, keep the full exterior face algebra \(S\), and use the actual normalized vacuum probability \(\mu\). Write
\[
m=\mathbb E[Y\mid S],\qquad Z=Y-m,\qquad
V=\mathbb E[ZZ^{\mathsf T}\mid S],\qquad
t=\mathbb E[Z|Z|^2\mid S],
\]
\[
\kappa_S=\mathbb E[|Z|^4\mid S]
-(\operatorname{Tr}V)^2-2\operatorname{Tr}(V^2),
\qquad \mathcal K(\mu)=\mathbb E_\mu\kappa_S .
\tag{CI1}
\]
The conditioning and source maps are fixed during the parameter change. Define the influence observable
\[
\boxed{
\begin{aligned}
F_\mu={}&|Z|^4-4t\cdot Z
-2(\operatorname{Tr}V)|Z|^2-4Z^{\mathsf T}VZ\\
&+(\operatorname{Tr}V)^2+2\operatorname{Tr}(V^2).
\end{aligned}}
\tag{CI2}
\]
It is bounded at every fixed \(h>0\), and
\(\mathbb E[F_\mu\mid S]=\kappa_S\).
The vectors and matrices transform covariantly under the common root gauge action, so \(F_\mu\) is a physical scalar. Although \(Y\) marks one face, \(F_\mu\) uses the complete exterior through \(m,V,t\); no one-face support is asserted for this influence observable.

For a normalized variation with joint probability score \(s\), the conditional score is \(s-\mathbb E[s\mid S]\). Differentiating the central fourth moment gives the terms
\[
\mathbb E[(s-\mathbb E[s\mid S])|Z|^4\mid S]
-4t\cdot\mathbb E[(s-\mathbb E[s\mid S])Z\mid S].
\]
Differentiating the two covariance contractions adds
\(-2(\operatorname{Tr}V)|Z|^2-4Z^{\mathsf T}VZ\)
inside that conditional expectation. The retained marginal also varies, contributing \(\mathbb E[s\mid S]\kappa_S\). Combining and centering these terms proves
\[
\boxed{\partial\mathcal K=\mathbb E_\mu[sF_\mu].}
\tag{CI3}
\]
There is no additional derivative of \(F_\mu\) on the right: it is the influence observable at the current law, already obtained by differentiating the whole statistic. Holding only the original conditional moment polynomial fixed would omit terms in CI2.

For a positive normalized real amplitude \(\psi\), \(\mu=\psi^2dm\), this is equivalently
\[
\partial\mathcal K=2\langle F_\mu\psi,\partial\psi\rangle.
\tag{CI4}
\]
CRA's amplitude derivative extends this identity without a uniform marginal-density lower bound. In the finite compact vacuum the amplitude is strictly positive, so the displayed score derivation is also direct.

## The vacuum parameter uses the inherited reduced resolvent

For EH's character family at fixed \(L,h\), let \(\widehat H_\varepsilon\) be the original scaled Hamiltonian, \(\mathcal E_\varepsilon\) its vacuum energy, and
\[
B_\varepsilon=\partial_\varepsilon\widehat H_\varepsilon,\qquad
K_\varepsilon=\widehat H_\varepsilon-\mathcal E_\varepsilon,\qquad
R_\varepsilon=K_\varepsilon^{-1}\big|_{\psi_\varepsilon^\perp}.
\]
The vacuum is simple. The derivative \(B_\varepsilon\) is bounded on this fixed compact carrier, and normalized Feynman–Hellmann gives
\[
\partial_\varepsilon\psi_\varepsilon
=-R_\varepsilon(B_\varepsilon-\mathbb E_\mu B_\varepsilon)
\psi_\varepsilon.
\]
Define the centered physical source vectors
\[
f_\varepsilon=(F_{\mu_\varepsilon}-\mathcal K(\mu_\varepsilon))
\psi_\varepsilon,\qquad
b_\varepsilon=(B_\varepsilon-\mathbb E_\mu B_\varepsilon)
\psi_\varepsilon.
\]
Then
\[
\boxed{
\partial_\varepsilon\mathcal K(\mu_\varepsilon)
=-2\langle f_\varepsilon,R_\varepsilon b_\varepsilon\rangle
=-2\int_0^\infty
\operatorname{Cov}_{\mu_\varepsilon}
 \bigl(F_{\mu_\varepsilon}(U_0),B_\varepsilon(U_s)\bigr)\,ds.}
\tag{CI5}
\]
Here \(U_s\) follows the stationary ground transform of \(e^{-sK_\varepsilon}\). The finite physical gap makes the integral absolutely convergent. Time, vacuum and source centering all belong to the original Hamiltonian.

This is a mixed matrix element of the full reduced resolvent. Its sign is not constrained by the positivity of either diagonal susceptibility. A positive derivative of this cumulant corresponds to a negative integrated mixed covariance in CI5, not to a positive lower bound on all physical innovations.

## The leading kernel is an explicit fourth-order contraction

For the harmonic law, set
\[
C_L=\sqrt{4I-\operatorname{Adj}_L},\qquad
\sigma=\bigl((C_L^{-1})_{rr}\bigr)^{-1},\qquad
\eta=X_r-\mathbb E_0[X_r\mid X_S]
=\sigma(C_L^{-1}X)_r.
\]
The conditional residual has three color components with covariance \(\sigma I_3\). CI2 becomes the radial fourth Hermite polynomial
\[
\boxed{
F_0=\mathcal H_{4,\sigma}(\eta)
=|\eta|^4-10\sigma|\eta|^2+15\sigma^2.}
\tag{CI6}
\]
Its conditional mean is zero. The source-coordinate correction of the original GM mark begins at \(h^2\), whereas the character insertion also begins at \(h^2\); it therefore does not change the coefficient calculated here.

In the inherited stationary Ornstein–Uhlenbeck chronology,
\[
\operatorname{Cov}_0(\eta_a(0),X_{p,b}(s))
=\sigma(e^{-sC_L})_{pr}\delta_{ab}.
\]
For two centered isotropic \(d\)-component Gaussian vectors with component cross covariance \(q\), Wick contraction gives
\[
\mathbb E[\mathcal H_{4,\sigma}(\eta)|X|^4]
=8d(d+2)q^4.
\]
One verification applies two Laplacians in each source to
\(\mathbb E[e^{u\cdot\eta-\sigma|u|^2/2}
e^{v\cdot X-c|v|^2/2}]=e^{qu\cdot v}\)
at \(u=v=0\). Lower Hermite degrees in \(|X|^4\) do not contribute.

Since \(d=3\) and the character coefficient is
\(B_2=-7\sum_p|X_p|^4/120\), the complete leading mixed kernel is
\[
\boxed{
\operatorname{Cov}_0(F_0(X_0),B_2(X_s))
=-7\sigma^4\sum_p(e^{-sC_L})_{pr}^4<0.}
\tag{CI7}
\]
Integrating recovers the conditional coefficient directly:
\[
\boxed{
-2\int_0^\infty\operatorname{Cov}_0(F_0(X_0),B_2(X_s))\,ds
=14\sigma^4J_{L,r},\qquad
J_{L,r}=\int_0^\infty\sum_p(e^{-sC_L})_{pr}^4\,ds.}
\tag{CI8}
\]
This uses the original harmonic clock. The factor \(14\) was not obtained from a conditional-update generator.

## The harmonic temporal tail is uniformly integrable

Write \(a_s^\Lambda(p,r)=(e^{-sC_L})_{pr}\). Positivity, killed-kernel comparison and [[lattice-poisson-tails-and-collar-localization|LP7]] give
\[
\sum_p a_s^\Lambda(p,r)^4
\le a_s^\infty(0)^2a_{2s}^\infty(0)
\le C(1+s)^{-6}.
\]
Also \(\sigma\le(C_L)_{rr}\le2\). Thus, uniformly in the containing patch and source face,
\[
\boxed{
\int_T^\infty
|\operatorname{Cov}_0(F_0(X_0),B_2(X_s))|\,ds
\le C(1+T)^{-5}.}
\tag{CI9}
\]
The finite bulk coefficient is compatible with the closing full harmonic gap: this particular mixed response has a uniformly integrable temporal tail. It need not detect the least coercive direction of the complete source algebra.

[[conditional-character-chronology-and-uniform-temporal-tails|The actual temporal return]] now controls this entire mixed profile in the growing compact theory. [[conditional-influence-vectors-and-the-original-source-carrier|The full influence vector]], [[magnetic-character-insertion-and-centered-source-control|the centered global insertion]] and [[centered-compact-chronology-and-integrable-source-return|the centered original chronology]] supply its independent inputs. The absolute time-integrated error, after division by \(h^2\), is \(O_I(hn^{15/2})\), with a uniform actual tail; this is stronger than comparing signed susceptibilities alone. A spatially sewn realization must additionally preserve [[regional-innovation-and-exterior-information-balance|RI's exterior channels]] and [[spatial-block-sewing-and-the-vacuum-cap-response|SB's vacuum caps, source exchange and lag terms]]. No complete-source OI bound or four-dimensional physical return has been proved here.
