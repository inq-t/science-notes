# Relative Multiplication Transfer and the Rotor Limit

Comparing two left-multiplication readouts of one Gaussian matrix preparation gives a positive \(SU(2)\) convolution kernel with every Peter–Weyl sector present. Its normalized short-comparison powers converge to a rotor on the full group carrier. This repairs the angular and central information lost by a commutator-squared overlap. The group, preparation and duration remain declared inputs; the result is a compact-group transfer construction, not a four-dimensional Yang–Mills gap.

## A relative row keeps the central distinction

Use \(V=M_2(\mathbb C)\), \(h(X,Y)=\tfrac12\operatorname{Tr}(X^\dagger Y)\), and a centered circular complex Gaussian \(\xi\) with covariance \(G>0\) on the four-dimensional complex amplitude carrier. These are the conventions of [[multiplication-sensitive-cycle-preparations|the multiplication-sensitive preparation]]. Here choose the boundary group \(SU(2)\), with normalized Haar measure. For \(\alpha>0\), set
\[
D_{U,V}=L_U-L_V,\qquad L_U\xi=U\xi,
\qquad k_\alpha(U,V)=\mathbb E_Ge^{-\alpha\|D_{U,V}\xi\|^2}.
\tag{RT1}
\]
If \(g=U^\dagger V\), write \(x(g)=\tfrac12\operatorname{Re}\operatorname{Tr}g=\cos\theta\). The special \(SU(2)\) identity \(g+g^\dagger=2x(g)I_2\) gives
\[
D_{U,V}^\dagger D_{U,V}=2(1-x(g))I_V,
\qquad
\boxed{k_\alpha(g)=\det[I+2\alpha(1-x(g))G]^{-1}.}
\tag{RT2}
\]
Thus this is a central, inversion-symmetric relative kernel even for a general positive \(G\). In particular,
\[
\begin{aligned}
G=I:&\quad k_\alpha(g)=[1+2\alpha(1-x)]^{-4},\\
G=P_0+\tfrac19P_1:&\quad
k_\alpha(g)=[1+2\alpha(1-x)]^{-1}
[1+\tfrac{2\alpha}{9}(1-x)]^{-3}.
\end{aligned}
\tag{RT3}
\]
Here \(P_0,P_1\) are the scalar and traceless projections. The second covariance is the declared constitutive candidate from that preparation, not a uniquely selected state. Unlike the commutator overlap, \(k_\alpha(I)=1\) and \(k_\alpha(-I)=\det(I+4\alpha G)^{-1}<1\).

## Positivity and the complete representation spectrum

Put \(S=\|\xi\|^2\), so \(S>0\) almost surely. Equation (RT2) also has the positive mixture representation
\[
k_\alpha(g)=\mathbb E_G[e^{-\kappa}e^{\kappa x(g)}],
\qquad \kappa=2\alpha S.
\tag{RT4}
\]
Let \(\chi_n(\theta)=\sin((n+1)\theta)/\sin\theta\), \(n\ge0\), be the character of the dimension-\(n+1\) representation. The unnormalized convolution multiplier is
\[
a_{\alpha,n}
=\frac1{n+1}\int k_\alpha(g)\chi_n(g)\,dg
=\mathbb E_G\left[e^{-\kappa}\frac{2I_{n+1}(\kappa)}{\kappa}\right]>0.
\tag{RT5}
\]
Indeed, the Haar class measure is \((2/\pi)\sin^2\theta\,d\theta\). Its character integral against \(e^{\kappa\cos\theta}\) is \(I_n-I_{n+2}=2(n+1)I_{n+1}/\kappa\). Positivity follows directly from the series \(I_m(\kappa)=\sum_{j\ge0}(\kappa/2)^{2j+m}/[j!(j+m)!]\).

The multipliers strictly decrease with degree. The positive integral representation and one integration by parts give, for integer \(m\ge1\),
\[
\frac{I_{m+1}(\kappa)}{I_m(\kappa)}
=\frac{\int_{-1}^1 t e^{\kappa t}(1-t^2)^{m-1/2}dt}
{\int_{-1}^1 e^{\kappa t}(1-t^2)^{m-1/2}dt}
\in(0,1).
\tag{RT6}
\]
The mean is positive by pairing \(t\) with \(-t\), and is strictly below one. Averaging in (RT5) preserves the strict ordering.

Keep the raw normalization \(z_\alpha=\int k_\alpha\,dg=a_{\alpha,0}\). Define \(p_\alpha=k_\alpha/z_\alpha\) and its convolution \(R_\alpha\) on \(L^2(SU(2),dg)\). Then
\[
R_\alpha\big|_{\mathcal H_n}=b_{\alpha,n}I,
\qquad b_{\alpha,n}=a_{\alpha,n}/a_{\alpha,0},
\qquad 1=b_{\alpha,0}>b_{\alpha,1}>\cdots>0.
\tag{RT7}
\]
The continuous kernel gives a compact operator, hence \(b_{\alpha,n}\to0\). It is a positive, injective Markov transfer, with a unique constant fixed vector and every representation block \(\mathcal H_n\) present. Odd \(n\), corresponding to half-integer spins, survive. Pointwise positivity alone would not imply this; (RT5) proves it.

## The complete transfer approaches a rotor

Assign one comparison the duration \(1/\alpha\). This is an explicit pace convention. Let \(\Delta_{S^3}\) be the round unit-sphere Laplacian on \(SU(2)\), so \(-\Delta_{S^3}\) has eigenvalues \(n(n+2)\), and put \(D_Q=-\Delta_{S^3}/4\), matching [[sewn-transfer-clock-and-the-rotor-limit|the existing rotor convention]]. Define
\[
\rho_G=\frac{\mathbb E S^{-5/2}}{\mathbb E S^{-3/2}}>0.
\tag{RT8}
\]
These moments, and \(\mathbb E S^{-7/2}\), are finite: if \(\lambda_{\min}(G)>0\), then \(S\ge\lambda_{\min}(G)T\) under a standard Gaussian coupling, with \(T\sim\operatorname{Gamma}(4,1)\). Its negative moments are finite below order four.

For the normalized radial step distribution, a direct expansion gives
\[
\mathbb E_\alpha\theta^2
=\frac{3\rho_G}{2\alpha}+O(\alpha^{-2}),
\qquad \mathbb E_\alpha\theta^4=O(\alpha^{-2}).
\tag{RT9}
\]
Here is a useful justification that also keeps the normalization. In chord radius \(r=2\sin(\theta/2)\), the Haar radial measure is \((2/\pi)r^2\sqrt{1-r^2/4}\,dr\), \(0\le r\le2\), and the kernel is exactly \(\mathbb E e^{-\alpha Sr^2}\). Substitute \(u=\sqrt\alpha r\). The required radial integrals are
\[
\int_0^\infty u^{2j}\mathbb E e^{-Su^2}\,du
=\tfrac12\Gamma(j+\tfrac12)\mathbb E S^{-j-1/2},
\quad j=1,2,3.
\tag{RT10}
\]
Use \(|\sqrt{1-v}-1|\le v\), \(\theta^2=r^2+O(r^4)\), and these finite moments to control the measure correction and the truncated tails. This proves (RT9), and also
\[
z_\alpha=\frac{\mathbb E S^{-3/2}}{2\sqrt\pi}\,
\alpha^{-3/2}[1+O(\alpha^{-1})].
\tag{RT11}
\]
Isotropic Taylor expansion along group geodesics now gives, for every \(f\in C^4(SU(2))\),
\[
R_\alpha f=f+\frac{\rho_G}{4\alpha}\Delta_{S^3}f
+O_f(\alpha^{-2})
\quad\text{in the uniform norm}.
\tag{RT12}
\]
Odd terms cancel by inversion symmetry; the fourth-moment bound controls the remainder. In particular,
\[
-\alpha\log b_{\alpha,n}\longrightarrow
\rho_G\,\frac{n(n+2)}4.
\tag{RT13}
\]

Since every multiplier is positive, \(H_\alpha=-\alpha\log R_\alpha\) is a densely defined nonnegative self-adjoint operator on the full carrier, with domain \(\sum_n|\alpha\log b_{\alpha,n}|^2\|f_n\|^2<\infty\). Finite Peter–Weyl sums are a core. The limit \(H=\rho_GD_Q\) has the analogous domain with squared weights \([\rho_G n(n+2)/4]^2\). For every \(t>0\) and \(z>0\),
\[
\boxed{
\|R_\alpha^{\lfloor\alpha t\rfloor}-e^{-t\rho_GD_Q}\|\to0,
\qquad
\|(z+H_\alpha)^{-1}-(z+\rho_GD_Q)^{-1}\|\to0.}
\tag{RT14}
\]
To prove this, split into degrees at most \(M\) and their complement. Equation (RT13) handles the finite head. Strict ordering in (RT7) bounds each approximating tail by its degree-\(M+1\) multiplier or resolvent; the limiting tail tends to zero as \(M\to\infty\). Integer powers are actual sewn Markov transitions. No assertion that arbitrary fractional powers are Markov is needed.

For \(G=I\), \(S\sim\operatorname{Gamma}(4,1)\), so \(\rho_G=2/3\). For \(G=P_0+P_1/9\), the scaled radial profile is \(F(u)=(1+u^2)^{-1}(1+u^2/9)^{-3}\). Its integrals are
\[
\int_0^\infty u^2F(u)du=\frac{135\pi}{512},
\qquad \int_0^\infty u^4F(u)du=\frac{729\pi}{512},
\qquad \rho_G=\frac{18}{5}.
\tag{RT15}
\]
For the first integral, twice differentiate \(\int_0^\infty u^2/[(u^2+a^2)(u^2+b^2)]du=\pi/[2(a+b)]\) with respect to \(b^2\), then set \(a=1,b=3\) and multiply by \(729/2\). For the second, also use \(u^4=u^2(u^2+a^2)-a^2u^2\) and \(\int_0^\infty u^2/(u^2+b^2)^3du=\pi/(16b^3)\). Thus the limiting round-sphere diffusion constants are \(1/6\) and \(9/10\), with centered rotor gaps \(1/2\) and \(27/10\), respectively. These are the declared comparison-clock units.

## Retaining the commutator comparison as well

The repair need not discard the earlier interaction. Let \(f_U(\xi)=e^{-\beta\|[U,\xi]\|^2/2}\), with finite \(\beta\ge0\). The combined kernel
\[
\mathcal K_{\alpha,\beta}(U,V)
=\mathbb E_G\!\left[f_U(\xi)
e^{-\alpha\|(U-V)\xi\|^2}f_V(\xi)\right]
\tag{RT16}
\]
is positive semidefinite: for each \(\xi\), it is a Gaussian distance kernel multiplied on its two arguments by a positive function. It has the exact determinant with precision increment \(\alpha D_{U,V}^\dagger D_{U,V}+(\beta/2)(C_U^\dagger C_U+C_V^\dagger C_V)\), retaining the same preparation and all quadratic marks.

It is also injective on \(L^2(SU(2))\). Almost every Gaussian matrix \(\xi\) is invertible, so \(U\mapsto U\xi\) is an injective compact embedding. A Gaussian distance kernel has strictly positive energy on every nonzero finite complex measure: its Fourier representation integrates the squared Fourier transform against a strictly positive Gaussian density, and uniqueness of the Fourier transform excludes zero energy. Multiplying a nonzero Haar-density measure by \(f_U(\xi)>0\) and pushing it through this embedding preserves nonzeroness. Averaging the resulting strictly positive quadratic forms proves the claim.

The combined kernel is generally not convolution; (RT14) has been proved only for \(\beta=0\). Its preparation-feature interpretation is compatible with [[directed-analytic-realization/preparation-overlaps-and-the-transition-algebra|the positive overlap construction]], while its commutator part retains the joint interaction of [[multiplication-sensitive-cycle-preparations|the finite preparation law]]. [[preparation-compression-and-the-returned-potential|Preparation compression]] uses independent relative-transfer and feature preparations and proves a generator \(D(-\Delta+q)\). [[shared-preparation-state-and-mobility|The single-preparation calculation]] now gives (RT16)'s variable mobility, state and marked limit at every fixed finite \(\beta\). Exact degree normalization and fixed leading endpoint normalization return different potentials; neither may be identified with the independent-copy law without comparison.

Raw normalization remains part of sewing: the unnormalized convolution satisfies \(T_\alpha^m=z_\alpha^mR_\alpha^m\). Keeping \(z_\alpha\) and transported marks preserves the distinction between vacuum normalization and normalized response emphasized in [[closed-normalization-and-cosmic-response|the closed-source identity]]. The special scalar reduction in (RT2) is an \(SU(2)\) result; a higher-dimensional matrix group with the same covariance prescription needs a new invariance and spectrum analysis. Neither this relative row nor its rotor return selects a graph gauge theory, a cosmic state or a physical four-dimensional gap.
