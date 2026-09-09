# The Local Conditional Character Contrast Returns Uniformly

The actual conditional fourth cumulant retains the higher-character preparation on the same growing-patch window that controls the physical soft gap. Its parameter derivative is \(14h^2\sigma_{L,r}^4J_{L,r}\), with error \(C h^3(L+1)^{17/2}\). This estimate keeps the original bounded Lie-valued source, its changing conditional mean and covariance, and the actual retained marginal. It makes the positive bulk coefficient an actual simultaneous compact return, rather than only a sequential coefficient limit.

**Status: proved uniform actual parameter derivative and integrated contrast for the fixed three-block \(SU(2)\) family.** [[character-memory-in-the-local-conditional-fourth-cumulant|LCM]] defines the statistic and evaluates its fixed-patch coefficient. [[conditional-replica-cumulants-and-amplitude-stability|CRA]] supplies the global amplitude stability estimate, and [[magnetic-parameter-tangents-and-uniform-vacuum-control|MVT]] supplies the actual vacuum tangent. The finite Gaussian-fiber bounds and the passage between compact cutoffs and full Gaussian fibers are proved below. Conditioning always retains the complete exterior face words.

## The actual statistic and uniform claim

Use [[uniform-weighted-character-return-and-the-soft-gap|UW's]] fixed representation and preparation family
\[
\rho=\rho_{1/2}\oplus\rho_1\oplus\rho_{3/2},\qquad
A_\varepsilon=(1+14\varepsilon)I_2
\oplus(1-16\varepsilon)I_3
\oplus(1+5\varepsilon)I_4.
\]
Fix a compact interval \(I\subset(-1/14,1/16)\). On the open \(L\times L\) patch, with every vertex Gauss constraint and the prepared comb face words, put
\[
n=L+1,\qquad h=(\kappa/(15g))^{1/4},\qquad
\delta=hn^{10},\qquad \theta=hn^{11/2},\qquad
C_L=\sqrt{4I-\operatorname{Adj}_L}.
\tag{UL1}
\]
The parameter derivative below holds \(L,h\), the electric operator and all source maps fixed. The physical scale remains \(E=\kappa h^{-2}\).

Choose any face \(r\) and retain all other complete faces \(S\). For the identical GM mark in every preparation, define
\[
Y_h(P_r)=2q_\rho(P_r)/h,\qquad
m_{\varepsilon,h}=\mathbb E_{\varepsilon,h}[Y_h\mid P_S],
\qquad Z=Y_h-m_{\varepsilon,h},\qquad
V=\mathbb E_{\varepsilon,h}[ZZ^{\mathsf T}\mid P_S],
\]
\[
\mathbf K_{\varepsilon,L,r}(h)
=\mathbb E_{\varepsilon,h}
\left\{\mathbb E_{\varepsilon,h}[|Z|^4\mid P_S]
-(\operatorname{Tr}V)^2-2\operatorname{Tr}(V^2)\right\}.
\tag{UL2}
\]
The outer expectation uses the corresponding actual retained marginal. This double trace of the conditional fourth-cumulant tensor is a physical scalar. No conditional covariance is inverted.

Set
\[
\sigma_{L,r}=\bigl((C_L^{-1})_{rr}\bigr)^{-1},\qquad
J_{L,r}=\int_0^\infty\sum_p(e^{-sC_L})_{pr}^4\,ds .
\]
There are constants \(C_I,\eta_I>0\), independent of \(L,r,\varepsilon\), such that
\[
\boxed{
\left|\partial_\varepsilon\mathbf K_{\varepsilon,L,r}(h)
-14h^2\sigma_{L,r}^4J_{L,r}\right|
\le C_Ih^3n^{17/2},\qquad
\varepsilon\in I,\quad 0<\delta\le\eta_I.}
\tag{UL3}
\]
The fixed window may be reduced to accommodate the finite approximation order eighteen used below. There is no limit in that order.

## Complete face coordinates survive the approximation

For \(SU(2)\), the principal logarithm identifies the open Lie-algebra ball of radius \(2\pi\), in the convention \(\exp(-iy\cdot\sigma/2)\), with the group minus \(-I\). The omitted point has Haar measure zero. Applying this chart separately to every face, dilating \(y=hX\), and multiplying by the square root of the exact product Haar density gives a parameter-independent unitary onto a subspace of \(L^2(dX)\). Extend vectors by zero outside the product chart.

This is a facewise measurable bijection modulo null sets. It therefore preserves the full retained face sigma algebra, including its conditional fibers. The common adjoint action is also respected. The same source on this common space is
\[
\widetilde Y_h(X)=2q_\rho(e^{hX})/h.
\tag{UL4}
\]
Outside the principal chart this formula is an auxiliary extension used only for Gaussian comparison. On the actual supported vectors it is exactly the original source.

Let \(v_\varepsilon\) be the normalized actual vacuum in this common carrier. For \(M=18\), let \(U_M=\sum_{j=0}^M h^j\psi_{j,\varepsilon}\) be the finite formal Gaussian vacuum vector, and define two normalized vectors in \(L^2(dX)\):
\[
u_\varepsilon=U_M/\|U_M\|,\qquad
q_\varepsilon=\chi_{L,h}U_M/\|\chi_{L,h}U_M\|.
\tag{UL5}
\]
Here \(\chi_{L,h}\) is [[compact-cutoffs-and-uniform-polynomial-quasimodes|CQ's]] exact magnetic cutoff, extended by zero. The vector \(q_\varepsilon\) is the flat representative of MVT's compact quasimode. Its square is a positive probability law even if the amplitude changes sign.

MVT proves, with a prime denoting \(\partial_\varepsilon\),
\[
\begin{gathered}
\|v-q\|\le C_In\rho_{18},\qquad
\|v'-q'\|\le C_Ih^{-2}n^4\rho_{18},\qquad
\|q'\|\le C_Ih^2n^3,\\
\rho_{18}=C_Ih^{19}n^{207/2}.
\end{gathered}
\tag{UL6}
\]
These are estimates for explicitly differentiated normalized vectors, not derivatives of unspecified error terms. They use UW's actual isolated vacuum and its reduced inverse.

The globally bounded mark satisfies \(\|\widetilde Y_h\|_\infty\le C_\rho h^{-1}\). CRA's replica kernel therefore has bound \(C_\rho h^{-4}\). Its \(C^{1,1}\) amplitude estimate gives
\[
\left|\partial_\varepsilon\mathbf K(v^2)
-\partial_\varepsilon\mathbf K(q^2)\right|
\le C_Ih^{-4}
\{\|v'-q'\|+\|v-q\|\|q'\|\}
\le C_Ih^{13}n^{215/2}.
\tag{UL7}
\]
Changing the fixed reference from Lebesgue measure to the harmonic Gaussian measure is just a common amplitude isometry; the replica functional still includes its induced retained marginal. Zero fibers contribute zero.

The cutoff must also be removed with its parameter derivative controlled. CQ's fixed-degree moments give, for any fixed integer \(a\ge0\), with \(\tau=hn^{3/2}\),
\[
\|q-u\|\le C_{I,a}\tau^{2a},\qquad
\|q'-u'\|\le C_{I,a}h^2n^3\tau^{2a},\qquad
\|u'\|\le C_Ih^2n^3 .
\tag{UL8}
\]
To obtain the second estimate, differentiate \(\chi u/\|\chi u\|\), keeping the cutoff fixed in \(\varepsilon\). The tails of \(u'\) cost its norm \(O(h^2n^3)\), since it lies in the same fixed Hermite-degree space. The derivative of the normalization differs from that of \(\|u\|=1\) by at most the same tail bound. Both denominators stay bounded below.

Apply CRA again with the common extension (UL4). Taking \(a=4\) gives
\[
\left|\partial_\varepsilon\mathbf K(q^2)
-\partial_\varepsilon\mathbf K(u^2)\right|
\le C_Ih^{-2}n^3\tau^8=C_Ih^6n^{15}.
\tag{UL9}
\]
The cutoff and all its derivative costs have thus been paid before using unbounded polynomial source estimates. In the stated window both (UL7) and (UL9) are smaller than the target error:
\[
\frac{h^{13}n^{215/2}}{h^3n^{17/2}}
=\delta^{10}n^{-1},\qquad
\frac{h^6n^{15}}{h^3n^{17/2}}
=\delta^3n^{-47/2}.
\]

## Finite Gaussian fibers control conditional normalization

Write \(\mu_0=\Omega_L^2dX\), whose covariance is \(C_L\otimes I_3\), and \(p_\varepsilon=u_\varepsilon/\Omega_L\). Conditional on \(X_S\),
\[
X_r=m_r(X_S)+\eta,\qquad
\eta\sim N(0,\sigma_{L,r}I_3).
\tag{UL10}
\]
The regression mean \(m_r\) is a three-component Gaussian with component variance \(C_{rr}-\sigma_{L,r}\le2\), and \(0<\sigma_{L,r}\le C_{rr}\le2\). Thus every fixed moment of \(m_r\) is uniformly bounded, for every patch and face. No lower bound on \(\sigma_{L,r}\) is required for the following lemma.

On each such fiber, \(p_\varepsilon\) belongs to the space of polynomials of degree at most \(D=3M\) in the three Gaussian variables \(\eta\). Let \(P_D\) be its orthogonal projection. For a source monomial \(F_j\) of degree \(j\le4\), compress its multiplication operator to that space:
\[
M_{j,h}=P_D M_{F_j(\widetilde Y_h(m_r+\eta))}P_D.
\]
The odd matrix exponential and the fixed orthogonal projection defining \(q_\rho\) give the global estimates
\[
|\widetilde Y_h(X)|\le C_\rho|X|,\qquad
|\widetilde Y_h(X)-X|\le C_\rho h^2|X|^3.
\tag{UL11}
\]
The first follows from the integral formula for \(e^{h\,d\rho(X)}-I\); the second follows from the third-order integral remainder for its odd part. Matrix unitarity bounds the integrands for every real \(X\). Fixed-degree Gaussian multiplication consequently gives
\[
\|M_{j,h}\|\le C_D(1+|m_r|)^j,\qquad
\|M_{j,h}-M_{j,0}\|
\le C_Dh^2(1+|m_r|)^{j+2}.
\tag{UL12}
\]
These bounds are uniform in \(L,r,h\). The finite fiber dimension depends only on \(D\); a small conditional variance improves the multiplication bound rather than introducing an inverse power.

For clarity, the fourth cumulant uses only finitely many such moment products. In any conditional law write
\[
a=\mathbb E Y,\quad M=\mathbb E YY^{\mathsf T},\quad
v=\mathbb E|Y|^2,\quad t=\mathbb E[|Y|^2Y],\quad s=\mathbb E|Y|^4 .
\]
Its invariant double trace is exactly
\[
s-4a\cdot t+4|a|^2v+8a^{\mathsf T}Ma
-6|a|^4-v^2-2\operatorname{Tr}(M^2).
\tag{UL13}
\]
Every term has total source degree four and at most four conditional moment factors.

For a fiber amplitude \(p\), put \(s_p=\|p\|^2\). Including the changing marginal, a term with \(k\) raw moments has the form
\[
T(p)=s_p^{\,1-k}\prod_{\ell=1}^k
\langle p,M_{j_\ell,h}p\rangle,\qquad
\sum_{\ell=1}^k j_\ell=4,\qquad T(0)=0 .
\tag{UL14}
\]
It is homogeneous of degree two. On the unit sphere its first two derivatives are bounded by a constant times \(\prod_\ell\|M_{j_\ell,h}\|\). Scaling then bounds its Hessian everywhere except zero by \(C_D(1+|m_r|)^4\). Its gradient tends to zero at zero and extends globally Lipschitz, by integrating along line segments and splitting a segment if it passes through zero. This is the finite-dimensional version of CRA's argument; it supplies a weighted bound for the polynomial source instead of the global \(h^{-4}\) bound.

Sum (UL14) according to (UL13) and integrate over the harmonic retained marginal. Denote the resulting functional by \(\mathfrak K_h(p)\). Since \(\|p\|_{L^2(\mu_0)}=1\), the fiber factor \(s_p\) is precisely the new retained marginal density; it must not be removed. Hölder and conditional Jensen now give, for finite-degree \(p,w\),
\[
\boxed{
|D\mathfrak K_h(p)[w]-D\mathfrak K_h(1)[w]|
\le C_D\|p-1\|_{L^4(\mu_0)}\|w\|_{L^4(\mu_0)}.}
\tag{UL15}
\]
Indeed \((1+|m_r|)^4\) has uniformly bounded \(L^2\) norm, while the conditional \(L^2\) norms of \(p-1\) and \(w\) have \(L^4\) norms bounded by their joint \(L^4\) norms. The same argument bounds \(D\mathfrak K_h(1)[w]\) by \(C_D\|w\|_4\). Equations (UL12)–(UL14) also imply
\[
|D\mathfrak K_h(1)[w]-D\mathfrak K_0(1)[w]|
\le C_Dh^2\|w\|_4 ,
\tag{UL16}
\]
using the higher, still bounded Gaussian moments of \(m_r\). These estimates allow zero approximate marginal fibers and never multiply uncontrolled conditional \(L^2\) errors.

## Differentiate the normalized polynomial law

MVT's improved formal tangent bounds are
\[
\psi'_0=\psi'_1=0,\qquad
\|\psi'_j\|\le C_{I,j}n^{11j/2-8}\quad(j\ge2).
\]
For a polynomial of fixed total Gaussian degree, every fixed \(L^q/L^2\) norm comparison is dimension independent. For even integer \(q\) this follows by expanding its finitely many Hermite chaoses, contracting their \(q\) tensor factors by Wick's rule, and applying Cauchy–Schwarz to each contraction; the number of contractions depends only on the degree and \(q\). Interpolation gives the other fixed exponents used here.

The normalized finite polynomial \(p_\varepsilon\) therefore satisfies
\[
\begin{gathered}
\|p_\varepsilon-1\|_4\le C_I\theta,\qquad
\|p'_\varepsilon\|_4\le C_Ih^2n^3,\\
\|p'_\varepsilon-h^2\beta_L\|_4
\le C_Ih^3n^{17/2},\qquad
\beta_L=\psi'_2/\Omega_L,\qquad
\|\beta_L\|_4\le C_In^3,\qquad \mathbb E_0\beta_L=0 .
\end{gathered}
\tag{UL17}
\]
Normalization does not add a lower-order term: formal norm coefficients vanish through order \(M\), including their explicit parameter derivatives. Alternatively the derivative of \(\|U_M\|\) can be bounded directly using those finite cancellations. The first possible omitted tangent after \(h^2\beta_L\) is \(h^3n^{17/2}\); later fixed powers form a bounded geometric envelope in \(\theta\).

Apply (UL15) with \(w=p'_\varepsilon\), then (UL17), then (UL16). The exact parameter derivative of the polynomial-law statistic obeys
\[
\begin{aligned}
\partial_\varepsilon\mathfrak K_h(p_\varepsilon)
&=D\mathfrak K_h(p_\varepsilon)[p'_\varepsilon]\\
&=h^2D\mathfrak K_0(1)[\beta_L]
+O_I(h^3n^{17/2}+h^4n^3)\\
&=h^2D\mathfrak K_0(1)[\beta_L]
+O_I(h^3n^{17/2}).
\end{aligned}
\tag{UL18}
\]
The source correction in (UL11) has been estimated, not discarded. It is common to all preparations and is multiplied here by a vacuum tangent beginning at order \(h^2\). Asymptotic parity could eliminate some formal odd coefficients, but no stronger even-order conditional remainder is needed or claimed.

## Evaluate the coefficient with all centering terms retained

At the Gaussian law the influence of the complete conditional cumulant is
\[
\mathcal H_{4,\sigma}(\eta)
=|\eta|^4-10\sigma|\eta|^2+15\sigma^2.
\]
Differentiating (UL13), including its marginal factor, gives
\[
D\mathfrak K_0(1)[\beta_L]
=2\mathbb E_0[\beta_L\mathcal H_{4,\sigma}(\eta)].
\tag{UL19}
\]
Its conditional mean is zero. This is also the Gaussian specialization of [[conditional-cumulant-influence-and-the-original-chronology|the exact conditional influence identity]]. The subtraction terms in \(\mathcal H_{4,\sigma}\) retain the moving mean and covariance.

LCM2–3 identifies \(\beta_L=\partial_\varepsilon b_\varepsilon\) by
\[
\mathcal L_{0,L}\beta_L
=\frac7{120}\left\{\sum_p|X_p|^4-\mathbb E_0\sum_p|X_p|^4\right\},
\qquad
(\beta_L)_4
=\frac7{120}\int_0^\infty\sum_p|(e^{-sC_L}X)_p|^4\,ds .
\tag{UL20}
\]
Lower Hermite degrees do not pair with \(\mathcal H_{4,\sigma}\). The cross covariance between \(\eta\) and \((e^{-sC_L}X)_p\) is \(\sigma(e^{-sC_L})_{pr}I_3\). Wick contraction gives
\[
\mathbb E_0\!\left[
\mathcal H_{4,\sigma}(\eta)|(e^{-sC_L}X)_p|^4\right]
=120\sigma^4(e^{-sC_L})_{pr}^4.
\]
Equivalently the same contraction can be applied to the full Ornstein–Uhlenbeck evolution of \(\sum_p|X_p|^4\); its additional lower-degree terms make no contribution. Hence
\[
\boxed{D\mathfrak K_0(1)[\beta_L]=14\sigma_{L,r}^4J_{L,r}.}
\tag{UL21}
\]
Combining (UL7), (UL9), (UL18) and (UL21) proves (UL3) for the actual compact statistic.

## The bulk limit now holds on the compact trajectory

Integrating the actual derivative over the parameter interval gives, including arbitrarily small contrasts,
\[
\boxed{
\left|\mathbf K_{\varepsilon_2,L,r}(h)
-\mathbf K_{\varepsilon_1,L,r}(h)
-14(\varepsilon_2-\varepsilon_1)h^2\sigma_{L,r}^4J_{L,r}\right|
\le C_I|\varepsilon_2-\varepsilon_1|h^3n^{17/2}.}
\tag{UL22}
\]
Every statistic and outer expectation uses its own actual vacuum, with the same face mark and conditioning algebra. The relative error after division by \(|\varepsilon_2-\varepsilon_1|h^2\) is at most
\[
C_Ihn^{17/2}=C_I\delta n^{-3/2}.
\tag{UL23}
\]
For a face whose distance to the boundary tends to infinity, LCM10–11 proves
\[
\sigma_{L,r}\longrightarrow\sigma_\infty>0,\qquad
J_{L,r}\longrightarrow J_\infty\in(0,\infty).
\]
Thus throughout \(0<hn^{10}\le\eta_I\), for distinct parameters in \(I\),
\[
\boxed{
\frac{\mathbf K_{\varepsilon_2,L,r}(h)
-\mathbf K_{\varepsilon_1,L,r}(h)}
{(\varepsilon_2-\varepsilon_1)h^2}
\longrightarrow14\sigma_\infty^4J_\infty>0.}
\tag{UL24}
\]
This is a simultaneous actual compact and bulk return, even when \(\delta\) stays fixed. It also holds for parameter pairs varying with the patch, provided they remain distinct and in \(I\), because (UL22) retains their difference.

The same strong-confinement trajectory makes the unrescaled contrast tend to zero. Its nonzero normalized coefficient records preparation information in this specified local conditional source; it does not distinguish continuum universality classes by itself. The theorem concerns an integrated conditional fourth cumulant on the isolated planar carrier. It neither returns all conditional operators in norm nor proves a full-source OI floor, a fixed-coupling thermodynamic limit or a four-dimensional physical theory.
