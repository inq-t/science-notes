# Transition Scores Control a Two-Input Lipschitz Response

The actual transition law of a compact weighted diffusion controls its nonlinear response without choosing an interacting eigenbasis. The inverse applied to the gradient pairing is bounded in the homogeneous Lipschitz norm, and the bound tensorizes over independent copies through a block-diagonal transition-score covariance. This controls arbitrary two inputs, not only a fixed multiplier, but it does not bound an extensive source in an edge-anchored connected norm.

**Status: exact for the supplied compact smooth block diffusions.** Every fixed finite Wilson block has finite constants at arbitrary finite coupling. Uniformity over independent copies of fixed block types is not uniformity over increasing interacting blocks or continuum coupling. The metric, vacuum and generator remain supplied; no physical mass gap or new clock is derived.

## The actual transition score is a joint gradient operator

Let \(M_b\) be a connected compact Riemannian manifold without boundary,
with smooth positive probability law \(d\mu_b=\psi_b^2d\mathrm{vol}_b\).
Use the complete raw carrier, including boundary charges when the block
is a gauge system. Supply a common \(\kappa>0\) and
\[
L_b=-\kappa(\Delta_b+2\nabla\log\psi_b\cdot\nabla),\qquad
P_t^b=e^{-tL_b},\qquad
\Gamma_b(f,g)=\kappa\langle\nabla f,\nabla g\rangle.
\tag{TS1}
\]
The gradient pairing is bilinear on complex functions. Its absolute
value is bounded by \(\kappa|\nabla f||\nabla g|\). Operator and form
domains are the inherited compact elliptic domains.

Let \(p_t^b(x,y)\) be the positive smooth kernel relative to \(\mu_b\).
Its score differentiates the starting point, not the invariant density:
\[
\zeta_t^b(x,y)=d_x\log p_t^b(x,y),\qquad
J_b(t,x)=\int\zeta_t^b\otimes\zeta_t^b\,
                    p_t^b(x,y)d\mu_b(y).
\tag{TS2}
\]
The metric identifies the last covariance with a positive tangent
operator. Differentiating the normalization gives mean score zero.
Thus \(dP_t^bf\) is the covariance of \(f\) with that score.

On any finite independent product, put
\(\mu=\bigotimes_b\mu_b\), \(L=\sum_bL_b\) and
\(P_t=\bigotimes_bP_t^b\). The conditional transition law is a product.
Scores from distinct blocks have zero cross covariance, so
\[
J(t,x)=\bigoplus_bJ_b(t,x_b),\qquad
C(t)=\sup_{b,x_b}\sqrt{\|J_b(t,x_b)\|_{\mathrm{op}}},
\qquad
\boxed{\|\nabla P_tv\|_\infty\le C(t)\|v\|_\infty.}
\tag{TS3}
\]
To prove the inequality, the map from scalar functions of the endpoint
to the starting-point tangent is covariance against \(\zeta\). Its
squared operator norm is \(\|J\|_{\mathrm{op}}\); centering the scalar
input cannot increase its second moment. The direct-sum identity uses
the **largest** block covariance eigenvalue, not its trace. Estimating
each output coordinate separately and summing would lose this fact.

## An integrable score bound gives the two-input inverse

Suppose a common envelope in (TS3) obeys
\[
\mathcal A=\int_0^\infty C(t)\,dt<\infty.
\tag{TS4}
\]
For a fixed finite product let \(Qv=v-\mu(v)\). The mean-zero inverse
exists by compact ellipticity. For smooth \(f,g\),
\[
\mathcal B(f,g)=L^{-1}Q\Gamma(f,g),\qquad
\Gamma=\sum_b\Gamma_b,
\]
satisfies
\[
\boxed{
\|\nabla\mathcal B(f,g)\|_\infty
\le\kappa\mathcal A\,
       \|\nabla f\|_\infty\|\nabla g\|_\infty.}
\tag{TS5}
\]
Indeed the gradient of the Poisson representation is
\(\int_0^\infty\nabla P_t\Gamma(f,g)dt\): the centering constant
has zero derivative. Apply (TS3) and the pointwise Cauchy--Schwarz
bound for \(\Gamma\). No supremum bound on the unknown inverse or
on the inputs themselves is inserted into this argument.

The natural space is \(W^{1,\infty}(M)/\mathbb C\), with norm
\(\|[f]\|=\|\nabla f\|_\infty\). This is a Banach space on each
connected compact product. The bilinear map (TS5) is well defined on
this quotient because \(\Gamma\) ignores additive constants.
The space is **not** an algebra under ordinary multiplication:
\([f][g]\) changes when a representative is shifted by a constant.
The bounded observable algebra and this derivative quotient therefore
remain distinct types. The
[[first-order-lift-and-spectral-product-tails#Preserve the actual weighted carrier|first-order commutator identity]]
identifies the same seminorm with
\(\kappa^{-1/2}\|[\mathscr D,M_f]\|\); it does not make multiplication
descend to the quotient.

For smooth time-dependent inputs with bounded gradients, the same proof
gives
\[
\boxed{
\sup_{t\ge0}\left\|\nabla\int_0^t
 P_{t-s}Q\Gamma(f_s,g_s)\,ds\right\|_\infty
\le\kappa\mathcal A
 \sup_s\|\nabla f_s\|_\infty
 \sup_s\|\nabla g_s\|_\infty.}
\tag{TS6}
\]
Bounded Sobolev inputs follow by weak derivative approximation or the
kernel formula; smooth functions need not be dense in the Lipschitz
norm. Additive scalar evolution has to be recovered separately when
this is applied to the
[[interacting-reference-and-spectral-product-control|actual re-centered logarithmic equation]].

## Finite block constants: curvature, mixing and a positive kernel

Here are sufficient quantitative block data, uniform over the chosen
fixed block types:
\[
\operatorname{Ric}_b-2\operatorname{Hess}\log\psi_b\ge-\omega g_b,
\quad \omega\ge0,
\qquad \operatorname{gap}(L_b)\ge\gamma>0,
\qquad 0<m\le p_a^b(x,y)\le M
\tag{TS7}
\]
for one \(a>0\). The gap is on the full raw carrier. Positivity of
\(\psi_b\) does not itself give a favorable curvature sign; a finite
negative bound suffices here. Smooth compactness gives finite data
for any fixed finite collection of blocks.

Define
\[
b_\omega(t)=
\begin{cases}
\sqrt{\omega/(1-e^{-2\kappa\omega t})},&\omega>0,\\
(2\kappa t)^{-1/2},&\omega=0.
\end{cases}
\tag{TS8}
\]
The Bochner gradient comparison implies the reverse Poincare inequality
\[
|\nabla P_t^bf|^2
\le b_\omega(t)^2\bigl(P_t^b|f|^2-|P_t^bf|^2\bigr).
\tag{TS9}
\]
For example, integrate
\(P_t|f|^2-|P_tf|^2=2\kappa\int_0^t
P_s|\nabla P_{t-s}f|^2ds\), using the curvature comparison
\(|\nabla P_tf|^2\le e^{2\kappa\omega s}
P_s|\nabla P_{t-s}f|^2\). Since (TS9) bounds the norm of
covariance against the transition score, \(J_b\le b_\omega(t)^2I\).

For \(t\ge a\), a single smoothing step and the raw gap give
\[
|\nabla P_t^bf(x)|^2
\le b_\omega(a)^2 M e^{-2\gamma(t-a)}\|Q_bf\|_{L^2(\mu_b)}^2.
\]
The kernel lower bound persists for all \(t\ge a\) by the semigroup
law. Subtract the transition mean of \(f\); its derivative is not
taken in this estimate, since it is a fixed scalar for the given
starting point. Comparing its \(\mu_b\) norm to its transition-law
norm then proves
\[
C(t)\le
\begin{cases}
b_\omega(t),&0<t\le a,\\
b_\omega(a)\sqrt{M/m}\,e^{-\gamma(t-a)},&t\ge a.
\end{cases}
\tag{TS10}
\]
Consequently a usable constant in (TS4) is
\[
\boxed{
\mathcal A\le
\begin{cases}
\operatorname{arcosh}(e^{\kappa\omega a})/(\kappa\sqrt\omega),&\omega>0,\\
\sqrt{2a/\kappa},&\omega=0
\end{cases}
\quad+\frac{b_\omega(a)\sqrt{M/m}}{\gamma}.}
\tag{TS11}
\]
The first term integrates the short-time \(t^{-1/2}\) singularity.
Positive curvature can give substantially better constants, as in
[[rg-covariance-residue/nonlinear-gauge-fiber-transport#A pointwise transport estimate from the actual conditional action|the existing Poisson-gradient estimate]].
Its conditional Euclidean Wilson law is not identified with the
Hamiltonian vacuum used here.

## Actual Wilson blocks provide explicit, albeit crude, finite data

For one fixed raw \(SU(2)\) block, let \(N\) be its link count,
\(P\) its elementary four-distinct-link plaquette count and \(n_e\)
the incidence of link \(e\). Supply
\(H=-\kappa\Delta+V\), \(V=\lambda\sum_p(1-q_p)\), \(\lambda\ge0\).
The
[[algebra/partial-bochner-and-ground-state-score|partial Bochner bound]]
and the product diameter imply the following safe data:
\[
\begin{gathered}
S=\frac\lambda\kappa\left(\sum_en_e^2\right)^{1/2},\qquad
F_*=\frac\lambda2\left(\sum_en_e^2\right)^{1/2},\\
V_*=2\lambda P,\quad E_*=\lambda P,\quad
R_* =e^{8\pi P\lambda/\kappa},\\
\|\nabla\log\psi\|_\infty\le S,\quad
\|\nabla V\|_\infty\le F_*,\quad
0\le V\le V_*,\quad E_0\le E_*,\quad
\max\psi/\min\psi\le R_*.
\end{gathered}
\tag{TS12}
\]
The raw gap from
[[interacting-reference-and-spectral-product-control#A block certificate must retain boundary charges|the full-carrier comparison]]
is at least \(\gamma=(3\kappa/4)R_*^{-2}\).

One can also obtain an upper Hessian bound without assuming one.
Let \(K_0=-\kappa\Delta\) be the free operator and let \(X\) be a
fixed unit product Killing field. It commutes with \(K_0\), so
the stationary equation gives the exact identity
\[
X\psi=e^{\tau E_0}e^{-\tau K_0}X\psi
-\int_0^\tau e^{sE_0}e^{-sK_0}X(V\psi)\,ds.
\tag{TS13}
\]
The free reverse Poincare bound is
\(\|\nabla e^{-sK_0}h\|_\infty\le(2\kappa s)^{-1/2}\|h\|_\infty\).
Using (TS12) in (TS13), for any \(\tau>0\), gives
\[
\operatorname{Hess}\log\psi\le B_\tau g,\qquad
B_\tau=R_*e^{\tau E_*}
\left[\frac{S}{\sqrt{2\kappa\tau}}
 +(F_*+V_*S)\sqrt{\frac{2\tau}{\kappa}}\right].
\tag{TS14}
\]
At a point choose \(X\) equal to the desired unit tangent. Its
integral curve is a geodesic; hence
\(\operatorname{Hess}\log\psi(X,X)=X^2\psi/\psi-(X\log\psi)^2\).
The negative last term need not be bounded to get the upper bound.
Thus \(\omega=\max(0,2B_\tau-1/2)\) is available in (TS7).
This is not an absolute Hessian bound or a favorable-sign claim.

Finally choose \(a=4/\kappa\). The free one-link Haar kernel obeys
\(3/4\le k_a^0(g)\le5/4\): its nonconstant character series is bounded
by \(\sum_{n\ge1}(n+1)^2e^{-n(n+2)}<1/4\).
Feynman--Kac and the ground-state transform therefore give
\[
\frac{M}{m}\le R_*^2e^{aV_*}(5/3)^N.
\tag{TS15}
\]
Indeed \(p_a(x,y)=e^{aE_0}k_a^V(x,y)/(\psi(x)\psi(y))\), and
\(e^{-aV_*}k_a^0\le k_a^V\le k_a^0\).
Equations (TS11)--(TS15), with for example \(\tau=1/\kappa\), give
an explicit finite-data constant for every finite coupling. Its
severe dependence on block size and coupling is part of the result,
not an estimate to discard after taking independent products.

## What tensorizes, and what still has to be assembled

The transition-score proof keeps the total Euclidean gradient norm
uniform over arbitrarily many independent copies of fixed block types.
It asserts no such uniformity for the supremum of the mean-zero inverse
or for an inhomogeneous \(W^{1,\infty}\) norm. It also does not identify
the auxiliary first-order lift with a new physical generator.

Even the homogeneous norm is not a local extensive-source norm. For
a fixed nonconstant smooth block source \(v\), on \(n\) independent
copies,
\[
V_n(x_1,\ldots,x_n)=\sum_{b=1}^nv(x_b),\qquad
\|\nabla V_n\|_\infty=\sqrt n\,\|\nabla v\|_\infty.
\tag{TS16}
\]
Each block can attain its own gradient maximum simultaneously.
Thus an \(n\)-independent constant in (TS5) is not an
\(n\)-independent input bound for the actual extensive source.

The remaining obligation is the
[[connected-preparation-and-local-normalization|edge-anchored absolute connected-support estimate]]:
control the union convolution of overlapping interactions in a norm
that records where their derivatives act. The block-diagonal covariance
argument does not supply that support-sensitive summation. The result
here bypasses an eigenbasis for a genuine two-input response while
retaining this separate spatial assembly problem.
