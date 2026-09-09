# Shared Preparation and the Two-Center Limit

The degree-normalized shared-preparation diffusion has a finite exchange rate between the two central elements of \(SU(2)\) as its commutator comparison becomes strong. Its stationary measure concentrates at those centers, while every mode beyond the constant and one center-odd mode becomes arbitrarily costly. The limiting rate follows from the same preparation's total mass and radial resistance. This is an iterated limit of a constructed compact-frame process, not a physical Yang–Mills mass statement.

## Fix the returned diffusion before strengthening the comparison

Use the tracial \(M_2(\mathbb C)\) pairing, \(G_{\rm ad}=P_0+P_1/9\), normalized Haar measure, and the round unit-sphere metric of [[shared-preparation-state-and-mobility|the shared state and mobility]]. First take its refinement limit \(\alpha\to\infty\) at each fixed finite \(\beta>0\), with exact degree normalization. Only then let \(\beta\to\infty\). No uniform estimate for a joint \(\alpha,\beta\) trajectory is asserted here.

Write \(U=\cos\theta I+i\sin\theta\,\mathbf n\cdot\boldsymbol\sigma\), \(0\le\theta\le\pi\), with normalized angular measure \(d\omega\) on \(S^2\). Put
\[
s_\beta(\theta)=\sqrt{9+4\beta\sin^2\theta},\qquad
A_\beta=\frac{729\sqrt\pi(s_\beta+2)}{2s_\beta(s_\beta+1)^2(s_\beta+3)^2},\qquad
B_\beta=\frac{243\sqrt\pi(2s_\beta+3)}{(s_\beta+1)^2(s_\beta+3)^2}.
\tag{TC1}
\]
These are the returned moments \(A_\beta=\mathbb E[f_U^2S^{-3/2}]\) and \(B_\beta=\mathbb E[f_U^2S^{-5/2}]\), not fitted densities. Define
\[
Z_\beta=\int A_\beta\,dU,\qquad
d\mu_\beta=Z_\beta^{-1}A_\beta\,dU,\qquad
L_\beta=-\frac1{4A_\beta}\operatorname{div}(B_\beta\nabla).
\tag{TC2}
\]
The positive generator \(L_\beta\) acts on \(L^2(\mu_\beta)\), with closed form
\[
\mathcal E_\beta(u)=\frac1{4Z_\beta}\int B_\beta|\nabla u|^2dU.
\tag{TC3}
\]
For each finite \(\beta\), its coefficients are smooth and strictly positive on the compact connected sphere. Its spectrum is discrete, counted with multiplicity, and \(0=\lambda_0(\beta)<\lambda_1(\beta)\le\lambda_2(\beta)\le\cdots\); the zero eigenspace consists of constants.

**Theorem.** Let
\[
\delta=1-\frac{\arctan(2\sqrt2)}{2\sqrt2}>0.
\]
There is a constant \(c_*>0\), independent of \(\beta\ge1\), such that
\[
\boxed{
\lambda_1(\beta)\longrightarrow\frac4{3\delta},\qquad
\lambda_2(\beta)\ge c_*\sqrt\beta.
}
\tag{TC4}
\]
The surviving mode distinguishes the two hemispheres \(\theta<\pi/2\) and \(\theta>\pi/2\). Their limiting centers are \(I\) and \(-I\). The following mass, resistance and coercivity estimates prove the complete spectral assertion.

## The normalization has an exact integral and limit

The Mellin representation of the preparation gives
\[
Z_\beta=\frac{729}{\Gamma(3/2)}
\int_0^\infty
\frac{r^{1/2}\,dr}{(r+1)(r+9)^{3/2}(r+9+4\beta)^{3/2}}.
\tag{TC5}
\]
Indeed, the determinant before Haar integration is \(729/[(r+1)(r+9)(r+9+4\beta\sin^2\theta)^2]\). The identity
\[
\frac2\pi\int_0^\pi\frac{\sin^2\theta\,d\theta}{(a+b\sin^2\theta)^2}
=\frac1{\sqrt a(a+b)^{3/2}}
\]
follows by differentiating \(\int_0^\pi(a+b\sin^2\theta)^{-1}d\theta=\pi/[\sqrt a\sqrt{a+b}]\) with respect to \(b\).

Dominated convergence in (TC5), followed by \(r=9v^2/(1-v^2)\), yields
\[
\begin{aligned}
\beta^{3/2}Z_\beta&\longrightarrow Z_*=
\frac{729}{4\sqrt\pi}\int_0^\infty\frac{r^{1/2}\,dr}{(r+1)(r+9)^{3/2}}
=\frac{729\delta}{16\sqrt\pi},\\
\int_0^\infty\frac{r^{1/2}\,dr}{(r+1)(r+9)^{3/2}}
&=\int_0^1\frac{2v^2}{1+8v^2}\,dv=\frac\delta4.
\end{aligned}
\tag{TC6}
\]
Away from both centers \(A_\beta=O(\beta^{-2})\), whereas \(Z_\beta\asymp\beta^{-3/2}\). Hence \(\mu_\beta\) converges weakly to \(\tfrac12(\delta_I+\delta_{-I})\). More precisely, each interval \(a/\sqrt\beta\le\theta\le b/\sqrt\beta\), for fixed \(0<a<b<\infty\), has a strictly positive limiting mass. This follows directly from (TC1) after setting \(\theta=v/\sqrt\beta\); the corresponding scaled core density is proportional to \(v^2A(\sqrt{9+4v^2})\), where \(A(s)\) denotes the rational expression in (TC1). The comparison (TC11) bounds the normalized scaled density by \(Cv^2/(1+v^2)^2\), proving tightness on each hemisphere.

## Resistance is measured between cores, not at the poles

Set
\[
w_\beta(\theta)=\frac2\pi A_\beta\sin^2\theta,\qquad
p_\beta(\theta)=\frac2\pi B_\beta\sin^2\theta.
\tag{TC7}
\]
For radial functions, (TC3) is \((4Z_\beta)^{-1}\int p_\beta|u'|^2d\theta\). If \(x_\beta\in[a/\sqrt\beta,b/\sqrt\beta]\) and \(\pi-y_\beta\) belongs to the same interval, then
\[
R_\beta(x_\beta,y_\beta):=\int_{x_\beta}^{y_\beta}\frac{d\theta}{p_\beta(\theta)},\qquad
\beta^{-3/2}R_\beta(x_\beta,y_\beta)\longrightarrow
R_*:=\frac{4\sqrt\pi}{243},
\tag{TC8}
\]
uniformly over these endpoints. At fixed \(0<\theta<\pi\), the rescaled integrand converges to \(2\sqrt\pi\sin\theta/243\). The bound
\[
\beta^{-3/2}p_\beta^{-1}(\theta)
\le C\left(\sin\theta+\beta^{-3/2}\sin^{-2}\theta\right)
\]
controls the moving ends: the second term integrates to \(O(\beta^{-1})\) outside the prescribed cores, and the first has arbitrarily small integral near either pole. This proves (TC8). The resistance from the literal pole is infinite at every finite \(\beta\); it must not replace the core-to-core resistance.

## Every additional mode costs at least order square root of beta

First separate angular harmonics. The radial coefficients preserve the spherical-harmonic decomposition, and
\[
D_\beta=\frac{B_\beta}{4A_\beta}
=\frac{s_\beta(2s_\beta+3)}{6(s_\beta+2)},\qquad
\frac{D_\beta}{\sin^2\theta}\ge\frac35\sqrt\beta.
\tag{TC9}
\]
Here \(D_\beta\ge3s_\beta/10\), \(s_\beta\ge2\sqrt\beta\sin\theta\), and \(\sin\theta\le1\). Every nonconstant angular harmonic has \(S^2\) eigenvalue at least two, so its Rayleigh quotient is at least \(6\sqrt\beta/5\).

For the radial part, work on one hemisphere \([0,\ell]\), \(\ell=\pi/2\). Let \(M_\beta=Z_\beta/2\), \(W_\beta(x)=\int_0^xw_\beta\), and let \(\bar u\) be the \(w_\beta\)-weighted mean there. The pairwise variance identity and weighted Cauchy–Schwarz give
\[
\int_0^\ell w_\beta|u-\bar u|^2
\le \mathfrak C_\beta\int_0^\ell p_\beta|u'|^2,\qquad
\mathfrak C_\beta=\frac1{M_\beta}
\int_0^\ell\frac{W_\beta(x)[M_\beta-W_\beta(x)]}{p_\beta(x)}\,dx.
\tag{TC10}
\]
For example, insert \(|u(y)-u(x)|^2\le(\int_x^yp_\beta|u'|^2)(\int_x^yp_\beta^{-1})\) into the double-integral variance identity and then interchange the integrals. This proves (TC10) directly, without a separate weighted-Hardy assumption.

Uniformly for \(\beta\ge1\), \(0<x\le\ell\), the explicit coefficients satisfy
\[
w_\beta(x)\asymp\frac{x^2}{(1+\beta x^2)^2},\qquad
p_\beta(x)\asymp\frac{x^2}{(1+\beta x^2)^{3/2}}.
\tag{TC11}
\]
The comparison constants are independent of \(x,\beta\). Split (TC10) at \(r_\beta=\beta^{-1/2}\). Below it, \(W_\beta/p_\beta\le Cx\), contributing \(O(\beta^{-1})\). Above it,

\(M_\beta-W_\beta(x)\le C\beta^{-2}/x\) and \(p_\beta(x)\ge c\beta^{-3/2}/x\),

so the remaining contribution is \(O(\beta^{-1/2})\). Consequently \(\mathfrak C_\beta\le C\beta^{-1/2}\).

For a general frame function, take its angular average at each \(\theta\) and the orthogonal angular residual. Norm and energy split between them. Apply (TC10) to the radial average on each hemisphere and (TC9) to the residual. Thus
\[
\mathcal E_\beta(u)\ge c_*\sqrt\beta\,\|u\|_{L^2(\mu_\beta)}^2
\quad\text{if both hemisphere means of }u\text{ vanish}.
\tag{TC12}
\]
This is a codimension-two condition, including all angular sectors. Min–max gives the asserted bound on \(\lambda_2\).

## The remaining exchange mode has matching variational bounds

Choose symmetric core endpoints \(x_\beta=a/\sqrt\beta\), \(y_\beta=\pi-x_\beta\). Let a radial trial function equal \(-1\) below \(x_\beta\), \(+1\) above \(y_\beta\), and interpolate linearly in the resistance coordinate between them. Reflection makes its mean zero, and its energy is exactly
\[
\mathcal E_\beta(u_\beta)=\frac1{Z_\beta R_\beta(x_\beta,y_\beta)}.
\tag{TC13}
\]
Its squared norm tends to one: on each bounded scaled core the interpolation differs from its endpoint constant by \(o(1)\), and the scaled core distributions are tight. Equations (TC6) and (TC8) therefore give \(\limsup\lambda_1\le1/(Z_*R_*)\).

This bounded trial value and (TC9) imply that the first excited eigenfunction is radial for sufficiently large \(\beta\). Choose it real, mean zero and norm one. Hemisphere coercivity forces its squared distance from its two hemisphere means to vanish. The two hemisphere masses are exactly equal, so, after choosing its sign, these means approach \(-1,+1\).

Each fixed core interval in (TC8) has positive limiting probability. There are therefore points \(x_\beta,y_\beta\) in those intervals where the eigenfunction approaches the respective hemisphere means. Weighted Cauchy–Schwarz across those points gives
\[
\lambda_1(\beta)\ge
\frac{|u_\beta(y_\beta)-u_\beta(x_\beta)|^2}
{4Z_\beta R_\beta(x_\beta,y_\beta)},\qquad
\liminf_{\beta\to\infty}\lambda_1(\beta)\ge\frac1{Z_*R_*}=\frac4{3\delta}.
\tag{TC14}
\]
Together with (TC13), this proves (TC4). The two-state positive generator with this surviving eigenvalue is \(\frac2{3\delta}\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\), on two states of probability one half. The eigenfunction statement concerns hemisphere averages in the varying spaces \(L^2(\mu_\beta)\), not convergence of fixed Haar wavefunctions to point-supported vectors.

The construction retains the center-odd distinction that the commutator feature quotient loses in [[commutator-overlap-nullspace-and-angular-coverage|the angular audit]]. It does so because the relative comparison remained on the full \(SU(2)\) carrier before either limit. It selects neither a spatial gauge diagram nor the comparison-clock calibration. A finite limiting exchange rate on these two centers is therefore a derived property of this preparation law, not a uniform continuum Yang–Mills gap.
