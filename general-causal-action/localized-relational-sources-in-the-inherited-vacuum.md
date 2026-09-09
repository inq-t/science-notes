# Localized Relational Sources in the Inherited Vacuum

A smooth quadratic source of pairing diameter \(R\) has a harmonic OI quotient at most \(1-\exp[-16\pi^2t/(\sqrt3(R+2))]\), uniformly in every containing larger Dirichlet patch. The source uses the larger patch's actual harmonic covariance throughout. Its construction therefore shows how increasing relational range creates a soft response inside an inherited vacuum, without preparing an independent smaller block. The proof uses explicit lattice differences and a spectral moment inequality; its constant is not optimized.

**Status: proved inherited-vacuum source construction and pairing-range upper bound.** [[additive-neutral-sources-and-the-pairing-range-test|AR]] fixes the mixed quadratic carrier and its OI quotient. [[inherited-planar-vacuum-and-the-regional-time-law|IR]] fixes the whole-patch covariance and chronology. [[finite-pairing-range-and-the-harmonic-innovation-floor|The finite-range comparison]] owns the complementary lower estimate and the smaller-box endpoint.

## A smooth source has the prescribed pairing diameter

Fix an integer \(R\ge0\), put \(m=R+2\), and define a sequence on the full integer line:
\[
\phi_j=
\begin{cases}
\sin^2(\pi j/m),&1\le j\le m-1,\\
0,&\text{otherwise}.
\end{cases}
\qquad u=\phi/\|\phi\|_2,\qquad b=u\otimes u.
\tag{LR1}
\]
Translate its complete square support into any open planar patch \(\Lambda\). Then \(\|b\|_2=1\), and the rank-one symmetric matrix \(B=bb^{\mathsf T}\) obeys
\[
B_{pq}=0\quad\text{if }|p-q|_\infty>R.
\]
The containing patch can be arbitrarily larger than this support. All estimates below are independent of the translation and of the distance to its outer boundary.

The exact one-dimensional normalization is
\[
\|\phi\|_2^2=
\begin{cases}
1,&m=2,\\
3m/8,&m\ge3,
\end{cases}
\qquad \|\phi\|_2^2\ge3m/8.
\tag{LR2}
\]
For \(m\ge3\), expand \(\sin^4x=(3-4\cos2x+\cos4x)/8\) and sum the finite roots of unity. The exceptional \(m=2\) value is direct.

## Zero extension retains the boundary derivatives

Let \(D=2I-S-S^*\) be the positive one-dimensional lattice Laplacian. With \(\gamma_m=1-\cos(2\pi/m)\),
\[
(D\phi)_j=-\gamma_m\cos(2\pi j/m)
\quad(1\le j\le m-1),
\]
\[
(D\phi)_0=(D\phi)_m=-\sin^2(\pi/m),
\qquad (D\phi)_j=0\quad(j\notin\{0,\ldots,m\}).
\tag{LR3}
\]
Thus the two exterior boundary terms are included. Using
\(\gamma_m\le2\pi^2/m^2\) and \(\sin^2(\pi/m)\le\pi^2/m^2\),
\[
\|D\phi\|_2^2
\le\frac{\pi^4}{m^4}[4(m-1)+2]
\le\frac{4\pi^4}{m^3},\qquad
\|Du\|_2\le\frac{4\sqrt{2/3}\,\pi^2}{m^2}.
\tag{LR4}
\]

On the full square lattice \(A_{\mathbb Z^2}=D\otimes I+I\otimes D\). Set
\[
K_*=8\sqrt{2/3}\,\pi^2.
\]
For \(A=A_\Lambda=4I-\operatorname{Adj}_\Lambda\), zero extension gives
\[
\boxed{\|Ab\|_2\le\|A_{\mathbb Z^2}b\|_2
\le\frac{K_*}{m^2}.}
\tag{LR5}
\]
The first inequality is restriction of the full-lattice output to \(\Lambda\); it does not alter the input. Moreover the quadratic energy is unchanged by enlarging the containing patch:
\[
e:=\langle b,Ab\rangle
=\langle b,A_{\{1,\ldots,m-1\}^2}b\rangle
\ge8\sin^2\frac{\pi}{2m}
\ge\frac8{m^2}.
\tag{LR6}
\]
The first lower bound is the Dirichlet sine eigenvalue of the support square; the second uses \(\sin x\ge2x/\pi\) on \([0,\pi/2]\). This support-energy identity concerns \(A\), not its square root. The inherited covariance used next is still \(C=\sqrt{A_\Lambda}\).

## A spectral moment controls the original quotient

Let \(\nu\) be a probability spectral measure on \([0,\infty)\), with finite second moment and positive first moment. Put
\[
r_t(\lambda)=1-e^{-2t\lambda},\qquad
\mathfrak q_t(\nu)=\frac{\int r_t^2\,d\nu}{\int r_t\,d\nu}.
\]
Then the following general bound holds for every \(t>0\):
\[
\boxed{
\mathfrak q_t(\nu)
\le1-\exp\!\left[
-2t\frac{\int\lambda^2\,d\nu}{\int\lambda\,d\nu}
\right].}
\tag{LR7}
\]
To prove it, define
\(d\sigma=\lambda\,d\nu/\int\lambda\,d\nu\) and
\(w_t(\lambda)=r_t(\lambda)/\lambda\), with its continuous value \(2t\) at zero. The function \(w_t\) is decreasing. Hence
\[
\operatorname{Cov}_\sigma(\lambda,w_t)\le0,
\]
as follows by integrating
\((\lambda-\lambda')[w_t(\lambda)-w_t(\lambda')]\le0\)
over two independent copies. The probability measure
\[
d\eta_t=\frac{r_t\,d\nu}{\int r_t\,d\nu}
=\frac{w_t\,d\sigma}{\int w_t\,d\sigma}
\]
therefore has mean energy at most
\(\int\lambda^2d\nu/\int\lambda d\nu\). Finally
\(\mathfrak q_t(\nu)=\int r_t\,d\eta_t\), and Jensen's inequality for the increasing concave function \(r_t\) proves (LR7). This is an inequality for the unchanged OI quotient, with its innovation denominator retained.

## The inherited rank-one source has two frequency draws

Let \(C=\sqrt{A_\Lambda}\), and let the three colors of \(X\) have the full covariance \(C\). For the supported vector \(b\), put
\[
\beta_j=\langle b,C^jb\rangle,\qquad
c=\beta_1,\qquad e=\beta_2,
\qquad
f_b=\frac{|b^{\mathsf T}X|^2-3c}{\sqrt6\,c}.
\tag{LR8}
\]
This is a normalized centered physical source; its covariance has not been replaced by that of the support square.

If \(\nu_b\) is the spectral measure of \(C\) at the unit vector \(b\), define
\(d\mu_b(\omega)=\omega\,d\nu_b(\omega)/c\).
IR's Wick formula gives
\[
\langle f_b,P_tf_b\rangle
=\left[\int e^{-t\omega}\,d\mu_b(\omega)\right]^2.
\]
Thus the source spectral measure is the law of
\(\lambda=\omega+\omega'\), for two independent draws from \(\mu_b\). Its moment ratio is exactly
\[
\frac{\mathbb E\lambda^2}{\mathbb E\lambda}
=\frac{\beta_3}{\beta_2}+\frac{\beta_2}{\beta_1}.
\tag{LR9}
\]
The factor three from color and the Wick factor two are already included in the normalization \(\sqrt6\,c\).

Cauchy–Schwarz gives
\(\beta_2^2\le\beta_1\beta_3\) and
\(\beta_3^2\le\beta_2\beta_4\). Since \(\beta_4=\|Ab\|_2^2\), equations (LR5)–(LR6) imply
\[
\frac{\mathbb E\lambda^2}{\mathbb E\lambda}
\le2\sqrt{\frac{\beta_4}{\beta_2}}
\le\frac{K_*}{\sqrt2\,m}.
\tag{LR10}
\]
Combining this with (LR7) proves the explicit inherited-vacuum bound
\[
\boxed{
\mathfrak q_t(f_b)
\le1-\exp\!\left[-\frac{16\pi^2t}{\sqrt3(R+2)}\right]
\le\min\left\{1,\frac{16\pi^2t}{\sqrt3(R+2)}\right\}.}
\tag{LR11}
\]
It holds for every containing larger patch, not only when the support fills the system. In particular AR5's \(c_R(t)\) obeys this upper bound. [[finite-pairing-range-and-the-harmonic-innovation-floor|PR9–10]] supplies the matching lower bound and proves \(c_R(t)\asymp\min\{1,t/(R+1)\}\) with universal constants. The present witness realizes that upper scale while retaining an arbitrarily larger containing vacuum.

The inherited source scale can also be retained explicitly. The same moment inequalities give
\[
\frac{\beta_2^{3/2}}{\sqrt{\beta_4}}
\le c\le\sqrt{\beta_2},
\qquad
\boxed{\frac{16\sqrt2}{K_*m}\le c\le\frac{\sqrt{K_*}}m.}
\tag{LR12}
\]
Thus the unnormalized harmonic source has variance \(6c^2\) of order \(m^{-2}\). This is a growing profile family, unlike FR's fixed finite profiles with a size-independent variance.

The compact invariant mark \(\left|\sum_p b_p\mathbf q_p\right|^2\) has this quadratic well expansion using the same comb connectors. [[compact-quadratic-carrier-and-the-pairing-range-return|QK1–16]] now returns every signed quadratic matrix, including this growing rank-one family, with its actual mean and variance. For each \(t_0>0\), a size-independent window \(h(L+1)^{10}\le\eta(t_0)\) gives the actual compact range floor of order \(\min\{1,t/(R+1)\}\) for \(t\ge t_0\) and \(0\le R\le L-1\). The numerical exponential in (LR11) is the harmonic bound; its compact comparison retains the quantified source and chronological errors. These statements do not return arbitrary-degree compact observables or supply a fixed-coupling continuum gap.
