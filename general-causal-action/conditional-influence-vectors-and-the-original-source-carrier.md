# The Conditional Influence Returns as a Complete Source Vector

The moving conditional fourth-cumulant influence returns in the actual vacuum Hilbert space, with error \(C h(L+1)^{11/2}\). This controls the full vector needed by the original chronological covariance, not only a projected derivative or an integrated statistic. The proof keeps the original compact mark and complete exterior face algebra. Its essential step is a finite-polynomial input estimate whose output is the unprojected conditional influence.

**Status: proved uniform influence-vector return for the fixed weighted-character \(SU(2)\) family.** [[uniform-local-conditional-character-return|UL]] fixes the preparation, complete face coordinates and uniform confinement window. [[conditional-cumulant-influence-and-the-original-chronology|CI]] defines the actual influence. [[conditional-replica-cumulants-and-amplitude-stability|CRA]] controls its full amplitude gradient, and [[magnetic-parameter-tangents-and-uniform-vacuum-control|MVT]] supplies the compact vacuum approximation. A chronological return still requires the separate source insertion and evolution estimates.

## The actual centered vector

Use UL's compact preparation interval \(I\), open \(L\times L\) patch and notation
\[
n=L+1,\qquad \delta=hn^{10},\qquad \theta=hn^{11/2},
\qquad 0<\delta\le\eta_I .
\]
The complete retained exterior consists of every face except \(r\). Let \(v_{\varepsilon,L,h}\) be the real normalized actual vacuum, and let \(\mu=v^2\,dP\). For the identical original mark
\[
Y_h(P_r)=2q_\rho(P_r)/h
\]
write \(m=\mathbb E_\mu[Y_h\mid P_S]\), \(Z=Y_h-m\),
\(V=\mathbb E_\mu[ZZ^{\mathsf T}\mid P_S]\) and
\(t=\mathbb E_\mu[Z|Z|^2\mid P_S]\). CI's influence is
\[
\begin{aligned}
F_\mu={}&|Z|^4-4t\cdot Z
-2(\operatorname{Tr}V)|Z|^2-4Z^{\mathsf T}VZ\\
&+(\operatorname{Tr}V)^2+2\operatorname{Tr}(V^2).
\end{aligned}
\]
Its expectation is the integrated conditional cumulant
\(\mathbf K_\mu=\mathbb E_\mu F_\mu\). Define the centered physical vector
\[
\boxed{f_{\varepsilon,L,r,h}=(F_\mu-\mathbf K_\mu)v.}
\tag{IV1}
\]
Although the original mark occupies one face, \(F_\mu\) contains its full exterior conditional moments. No one-face support is asserted.

In the harmonic law put
\[
C_L=\sqrt{4I-\operatorname{Adj}_L},\qquad
\sigma=((C_L^{-1})_{rr})^{-1},\qquad
\eta=X_r-\mathbb E_0[X_r\mid X_S]
=\sigma(C_L^{-1}X)_r,
\]
\[
f_{0,L,r}=
\bigl(|\eta|^4-10\sigma|\eta|^2+15\sigma^2\bigr)\Omega_L.
\tag{IV2}
\]
This is a physical degree-four Hermite vector, centered in the harmonic vacuum. Since \(\eta\sim N(0,\sigma I_3)\),
\[
\|f_{0,L,r}\|^2=120\sigma^4,\qquad 0<\sigma\le2.
\tag{IV3}
\]
In particular its norm is bounded independently of the patch and source face.

Let \(\mathcal U_{L,h}\) be UL's exact principal-face-logarithm half-density map, with zero extension outside its product chart. The theorem is
\[
\boxed{
\|\mathcal U_{L,h} f_{\varepsilon,L,r,h}-f_{0,L,r}\|
\le C_I\theta,\qquad
\|f_{\varepsilon,L,r,h}\|\le C_I .}
\tag{IV4}
\]
Only the fixed approximation order and preparation interval enter the constants. The scale and full Gauss carrier are unchanged.

## The full gradient retains the influence

Let \(\mathfrak K_h(p)\) be CRA's homogeneous conditional-cumulant functional on real amplitudes, with the original fixed source and retained fibers. For every normalized amplitude \(p\),
\[
\boxed{\tfrac12\nabla\mathfrak K_h(p)=F_{p^2}p,\qquad
\mathfrak K_h(p)=\langle F_{p^2}p,p\rangle.}
\tag{IV5}
\]
The first identity holds in the full amplitude Hilbert space. It follows by differentiating the raw conditional moments including their marginal, or from CI's influence formula followed by homogeneity in the radial direction. The radial derivative fixes the constant that would be undetermined if only normalized variations were tested. At a zero fiber the product on the right is defined to be zero. Sign-changing approximate amplitudes are allowed.

Define, for normalized \(p\),
\[
\mathcal G_h(p)=\tfrac12\nabla\mathfrak K_h(p)
-\mathfrak K_h(p)p .
\]
CRA's global gradient Lipschitz bound, the quadratic bound on \(\mathfrak K_h\), and \(\|Y_h\|_\infty\le C_\rho h^{-1}\) imply
\[
\boxed{\|\mathcal G_h(p)-\mathcal G_h(q)\|
\le C_\rho h^{-4}\|p-q\|,\qquad \|p\|=\|q\|=1.}
\tag{IV6}
\]
This pays for both the influence and its actual vacuum centering. It does not require a lower bound on an actual or approximate retained marginal.

Use the common flat chart and UL's normalized vectors
\[
u=U_{18}/\|U_{18}\|,\qquad
q=\chi_{L,h}U_{18}/\|\chi_{L,h}U_{18}\|.
\]
MVT and UL prove
\[
\|v-q\|\le C_In\rho_{18},\qquad
\|q-u\|\le C_I\tau^8,\qquad
\rho_{18}=C_Ih^{19}n^{207/2},\qquad \tau=hn^{3/2}.
\]
The half-density transformation is parameter independent and facewise invertible modulo Haar-null sets. It preserves the exact exterior sigma algebra. Applying (IV6) twice therefore costs at most
\[
\boxed{C_I\{h^{-4}n\rho_{18}+h^{-4}\tau^8\}
=C_I\{h^{15}n^{209/2}+h^4n^{12}\}.}
\tag{IV7}
\]
These are comparisons of the actual source vectors with their cutoff and uncut positive squared-amplitude laws, all using the same source extension \(2q_\rho(e^{hX_r})/h\).

## The finite-input estimate has an unrestricted output

Write \(p=u/\Omega_L\), so that \(p\) is a normalized polynomial amplitude in \(L^2(\mu_0)\), of fixed total Hermite degree at most \(D=54\). On a harmonic exterior fiber,
\[
X_r=m_0(X_S)+\eta,\qquad \eta\sim N(0,\sigma I_3).
\]
The three-component Gaussian regression mean \(m_0\) has covariance bounded by \(2I_3\). Every fixed moment of \(m_0\) is therefore uniform in the patch size. On each fiber let \(\mathcal P_D\) be the degree-at-most-\(D\) polynomial space.

For a scalar source monomial \(A_j\) of degree \(j\le4\), use the multiplication map with its full output:
\[
R_{j,h}:\mathcal P_D\longrightarrow L^2(\eta),\qquad
R_{j,h}w=A_j\!\left(2q_\rho(e^{h(m_0+\eta)})/h\right)w .
\]
UL's global source estimates
\[
|\widetilde Y_h(X)|\le C_\rho|X|,\qquad
|\widetilde Y_h(X)-X|\le C_\rho h^2|X|^3
\]
and finite Gaussian moments prove
\[
\boxed{
\|R_{j,h}\|\le C_D(1+|m_0|)^j,\qquad
\|R_{j,h}-R_{j,0}\|
\le C_Dh^2(1+|m_0|)^{j+2}.}
\tag{IV8}
\]
No projection is applied to the output. Squaring the source polynomial merely requires Gaussian moments up to twice its degree; the bounds remain uniform for \(\sigma\le2\), without an inverse power of \(\sigma\).

The distinction matters: UL's compressed operators suffice to estimate an integrated derivative along polynomial directions, but those compressed gradients alone would not prove (IV4).

To see the required full-vector estimate, consider one raw-moment term in UL13–14. For a fiber amplitude \(p\), let
\[
s=\|p\|^2,\qquad a_j=\langle p,R_{j,h}p\rangle,\qquad
T(p)=s^{1-k}\prod_{\ell=1}^k a_{j_\ell},
\quad \sum_\ell j_\ell=4 .
\]
Here the inner product is well-defined despite the unrestricted output. Direct differentiation gives its full half-gradient
\[
\boxed{
\tfrac12\nabla T(p)
=(1-k)s^{-k}\Bigl(\prod_\ell a_{j_\ell}\Bigr)p
+s^{1-k}\sum_\ell
\Bigl(\prod_{b\ne\ell}a_{j_b}\Bigr)R_{j_\ell,h}p .}
\tag{IV9}
\]
For \(h>0\) this is the ordinary full Hilbert gradient of the bounded-source functional. At \(h=0\) it is the \(L^2\) representing vector on the polynomial domain; a globally bounded fourth-moment functional on all \(L^2\) is not asserted.

On the unit sphere of \(\mathcal P_D\), (IV8) bounds (IV9) and its derivative into the unrestricted \(L^2\) output by \(C_D(1+|m_0|)^4\). The map (IV9) is homogeneous of degree one. Its derivative is homogeneous of degree zero, and the map tends to zero at the origin. Integrating the derivative along segments, including through zero, proves
\[
\left\|\tfrac12\nabla T(p)-\tfrac12\nabla T(q)\right\|_{L^2(\eta)}
\le C_D(1+|m_0|)^4\|p-q\|_{L^2(\eta)}
\quad(p,q\in\mathcal P_D).
\tag{IV10}
\]
Sum the finitely many raw-moment terms for the complete invariant cumulant. The factor \(s^{1-k}\) includes its moving retained marginal throughout.

Taking the joint \(L^2\) norm in (IV10), then applying Hölder and conditional Jensen, yields
\[
\left\|\tfrac12\nabla\mathfrak K_h(p)
-\tfrac12\nabla\mathfrak K_h(1)\right\|_{L^2(\mu_0)}
\le C_D\|p-1\|_{L^4(\mu_0)}.
\]
Indeed \((1+|m_0|)^4\) has uniformly bounded \(L^4\) norm, and the conditional \(L^2\) norm of \(p-1\) has \(L^4\) norm bounded by its joint \(L^4\) norm. Equation (IV8), used in the same full-gradient formula, also gives
\[
\boxed{
\left\|\tfrac12\nabla\mathfrak K_h(p)
-\mathcal H_{4,\sigma}(\eta)\right\|_{L^2(\mu_0)}
\le C_D\{\|p-1\|_4+h^2\}.}
\tag{IV11}
\]
The second term controls the exact GM source's nonlinear coordinate correction. Its full influence at the Gaussian amplitude is compared to the linear-coordinate harmonic influence; the source itself has not been replaced in the actual theory.

## Center and return to the compact source carrier

UL17 gives \(\|p-1\|_4\le C_I\theta\). Also
\(\langle\mathcal H_{4,\sigma},1\rangle_0=0\), and its norm is uniformly bounded by (IV3). Since \(\|p\|_2=1\), (IV5) and (IV11) show
\[
|\mathfrak K_h(p)|
\le C_I(\theta+h^2),\qquad
\boxed{\|\mathcal G_h(p)-\mathcal H_{4,\sigma}\|_2
\le C_I(\theta+h^2).}
\tag{IV12}
\]
This explicitly retains the actual vacuum centering instead of identifying the source with a first oscillator excitation.

Combine (IV7) and (IV12), restoring the factor \(\Omega_L\) when moving from Gaussian to flat amplitudes. Every extra term fits \(C_I\theta\):
\[
\frac{h^{15}n^{209/2}}{\theta}
=\delta^{14}n^{-41},\qquad
\frac{h^4n^{12}}{\theta}
=\delta^3n^{-47/2},\qquad
\frac{h^2}{\theta}=h n^{-11/2}\le1 .
\]
This proves (IV4).

For an explicitly centered compact comparison vector, let
\(\mathcal J_{L,h}\) be CQ's cutoff inverse half-density map and
\[
Q_v=I-|v\rangle\langle v|,\qquad
\mathcal I_{L,h}=Q_v\mathcal J_{L,h}.
\]
The map \(\mathcal J_{L,h}\) already includes the magnetic cutoff. Both maps are contractions; no exact source-space isometry is claimed. UL and CQ also give
\(\|\mathcal U_{L,h}v-\Omega_L\|\le C_I\theta\) and
\(\|(1-\chi_{L,h})f_{0,L,r}\|\le C_I\tau^8\).
Using the harmonic centering of \(f_0\) proves
\[
\boxed{
\|f_{\varepsilon,L,r,h}-\mathcal I_{L,h}f_{0,L,r}\|
\le C_I\theta,\qquad
\|\mathcal I_{L,h}f_{0,L,r}\|\le C_I .}
\tag{IV13}
\]
This is the form appropriate for a centered Duhamel comparison in the original compact chronology.

For any centered partner vector \(b_h\), semigroup contraction alone bounds the influence-replacement error at every \(s\ge0\) by
\[
\left|
\langle f_h,e^{-sK_h}b_h\rangle
-\langle\mathcal I_{L,h}f_0,e^{-sK_h}b_h\rangle
\right|
\le C_I\theta\|b_h\|.
\tag{IV14}
\]
The [[magnetic-character-insertion-and-centered-source-control|global character insertion]] and the evolution comparison must supply their own estimates. A uniform influence norm does not by itself control long-time integrability, a complete chronological response matrix or all physical innovations. The present result retains the full exterior and original source on the isolated planar confinement window; it asserts no conditional operator-norm return or four-dimensional limit.
