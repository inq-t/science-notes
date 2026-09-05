# Uniform Locality of the Accumulated Gaussian Conditional Law

The actual accumulated soft Gaussian gauge precision has exponentially decaying coefficients uniformly in blocking depth. Its apparent massless pole cancels in the transverse inverse because the block average respects the gradient relation. Combined with the terminal Schur lower bound, this gives depth- and volume-uniform exponential conditional covariance and coarse-source response for curvature observables. This closes the Gaussian conditional-locality step for the declared regular average; it does not give a nonlinear Yang--Mills estimate or an infrared mass gap.

## The two operators and their metrics

Use the chain, physical \(L^2\) metrics, fixed integer \(L\ge2\), and meshes \(b_k=L^ka\) in [[soft-gaussian-gauge-blocking]]. Fix \(\eta>0\) and the auxiliary partial-gauge coefficient \(\alpha>0\). Let \(\widehat P_k\) be the actual accumulated precision, extended by zero on gradients and harmonics. Let

$$
S_k=\widehat P_k+\alpha D_kZ_kD_k^*
+\frac{Q_k^*Q_k}{\eta b_{k+1}^2}
\tag{GL1}
$$

be the terminal Schur precision of [[multilevel-local-gauge-completion]]. It acts on all current bond potentials, not on the unweighted sum of all latent levels. That note proves
\(S_k\ge\beta_*b_{k+1}^{-2}I\), with \(\beta_*>0\) independent of \(k,a\), and volume.

We first prove spatial locality of \(\widehat P_k\), which is gapless, then use that locality and the conditional floor of \(S_k\) to localize its inverse. The two conclusions concern different operators.

## Uniform holomorphic control of the high aliases

Complexify the momentum variable in [[accumulated-readout-noise|the exact covariance symbol]]. For \(n=L^k\ge2\), use balanced aliases

$$
I_n=\{-\lfloor n/2\rfloor,\ldots,\lceil n/2\rceil-1\},
\qquad \delta_0=\frac1{10\sqrt d},
$$

on the padded cell \(|\operatorname{Re}z_\nu|<\pi+\delta_0\),
\(|\operatorname{Im}z_\nu|<\delta_0\). Put

$$
q_\ell=(z+2\pi\ell)/n,\qquad
h_{n,\ell}(z)=4n^2\sum_\nu\sin^2(q_{\ell,\nu}/2),
$$

$$
a_{n,\mu,\ell}(z)
=\Omega_n(q_\ell)_{\mu\mu}\Omega_n(-q_\ell)_{\mu\mu}.
\tag{GL2}
$$

Here \(\Omega_n\) is the regular-average multiplier (EA8d). The paired product is holomorphic and equals the squared modulus on real momentum. Using a complex modulus or a conjugate transpose at complex \(z\) would invalidate this argument.

For \(\ell\ne0\), write \(z+2\pi\ell=x+iy\). Balanced aliases give
\(|x_\nu|/(2n)<5\pi/6\), where \(|\sin t|\ge3|t|/(5\pi)\). Consequently

$$
\operatorname{Re}h_{n,\ell}(z)
\ge\frac9{25\pi^2}|x|^2-|y|^2\cosh(\delta_0/2)
\ge\frac14|\ell|^2.
\tag{GL3}
$$

For the last step use \(|x_\nu|\ge(\pi-\delta_0)|\ell_\nu|\) whenever \(\ell_\nu\ne0\) and \(d\delta_0^2=1/100\). The estimate is uniform in \(n\).

The geometric-series expression
\(d_n(t)=e^{i(n-1)t/2}\sin(nt/2)/(n\sin(t/2))\)
gives
\(|d_n(q_{\ell,\nu})|,|d_n(-q_{\ell,\nu})|
\le8/(1+|\ell_\nu|)\).
For \(\ell_\nu=0\), use the finite exponential sum at removable zeros; for \(\ell_\nu\ne0\), use the preceding sine bound in the denominator. Thus

$$
\left|\frac{a_{n,\mu,\ell}}{h_{n,\ell}}\right|
\le
\frac{4\,64^{d+1}}
{|\ell|^2(1+|\ell_\mu|)^4
\prod_{\nu\ne\mu}(1+|\ell_\nu|)^2}.
\tag{GL4}
$$

The right side is summable over \(\mathbb Z^d\setminus\{0\}\), including \(d=4\). The high-alias sum is therefore holomorphic and uniformly bounded on a common padded cell. Add the exact noise polynomial (AN4), whose coefficients are uniformly bounded, and call the result \(R_{k,\mu}(z)\).

This proof uses the actual volume/path-average shape, not discreteness of the lattice alone. The high sum is not separately periodic across cell seams; periodicity belongs to the complete alias expression.

## The principal pole cancels by the cochain identity

Near \(z=0\), define the removable entire quotients locally by

$$
r_\mu(z)=\frac{\sin(z_\mu/2)}{n\sin(z_\mu/(2n))},
\quad g(z)=\prod_\nu r_\nu(z)^2,
\quad a_\mu(z)=g(z)r_\mu(z)^2,
\quad h(z)=4n^2\sum_\nu\sin^2(z_\nu/(2n)).
\tag{GL5}
$$

The covariance diagonal before transverse compression is
\(\mathcal D_\mu=a_\mu/h+R_{k,\mu}\). Put

$$
B_\mu=a_\mu+hR_{k,\mu},\qquad
v_\mu=e^{iz_\mu}-1,\qquad v^-_\mu=e^{-iz_\mu}-1.
$$

The crucial exact identity is

$$
\sum_\mu\frac{v^-_\mu v_\mu}{a_\mu}
=\frac hg.
\tag{GL6}
$$

It is the Fourier expression of gradient compatibility. Therefore

$$
\sum_\mu\frac{v^-_\mu v_\mu}{B_\mu}
=hW,\qquad
W=\frac1g-\sum_\mu
\frac{v^-_\mu v_\mu R_{k,\mu}}{a_\mu B_\mu}.
\tag{GL7}
$$

At the origin, \(a_\mu=B_\mu=g=W=1\). The uniform bound on \(R_k\), the uniform local bounds on \(r_\mu\), and \(h=O(|z|^2)\) give one complex neighborhood of zero, independent of \(k\), where all \(a_\mu,B_\mu,g,W\) are nonzero with uniformly bounded inverses.

Write \(\mathcal B^{-1}=\operatorname{diag}(B_\mu^{-1})\).
Substitution into the constrained inverse (AN9) gives

$$
\boxed{
b_k^2\widehat P_k(z)
=h\mathcal B^{-1}
-\mathcal B^{-1}v\,W^{-1}v^-\mathcal B^{-1}.}
\tag{GL8}
$$

Indeed \(\mathcal D^{-1}=h\mathcal B^{-1}\), so the denominator
\(v^-\mathcal D^{-1}v\) is \(h^2W\); both powers cancel in its rank-one term. Formula (GL8) is holomorphic even across the complex zeros of \(h\). It also sets \(\widehat P_k(0)=0\), consistent with the harmonic-flat extension.

## A common periodic strip and exponential coefficients

Outside a smaller real neighborhood of zero, the principal denominator \(h\) has a uniform positive lower bound. Shrinking the imaginary width preserves it. The high-alias lemma then supplies uniform holomorphic bounds and, by Cauchy estimates, uniform first-derivative bounds for every \(\mathcal D_\mu\).

On this compact real complement, for \(k\ge1\),

$$
\eta\le\mathcal D_\mu(p)\le M_D,\qquad
v(p)^*\mathcal D(p)^{-1}v(p)\ge |v(p)|^2/M_D>0,
\tag{GL9}
$$

with one \(M_D\) and a uniform positive last lower bound. The first inequality follows from the latest readout noise, not from the principal alias. Uniform derivative bounds now give a common thinner complex neighborhood where both \(\mathcal D_\mu\) and the scalar inverse denominator stay nonzero. Thus (AN9) is holomorphic there with a uniform bound.

Together with (GL8), this covers the real momentum torus by neighborhoods of a common thickness. The full alias formula is periodic by relabeling residues; uniqueness of analytic continuation glues the local expressions. There exist constants \(\delta,C>0\), depending only on \(d,L,\eta\), such that \(b_k^2\widehat P_k\) is periodic, holomorphic, and bounded by \(C\) on \(|\operatorname{Im}z_\nu|<\delta\), for all \(k\ge1\).

For \(k=0\), the bare Maxwell symbol
\(\widehat p^2I-vv^*\) has finite range and handles that case separately. Contour shifting in each momentum component, using any \(\delta'<\delta\), yields Fourier coefficients

$$
\boxed{
\|b_k^2\widehat P_k(x)\|
\le C'e^{-\delta'|x|_1},
\qquad x\in\mathbb Z^d,}
\tag{GL10}
$$

uniformly in depth. Finite-torus coefficients are periodizations of these coefficients, since their symbols are the same functions sampled at the allowed momenta. Exponential row and column moments remain volume-uniform in the shortest periodic lattice distance.

The continuum-cutoff high-alias limit can also be taken by dominated convergence in (GL4), but no convergence rate or nonlinear continuum construction is needed for (GL10).

## Weighted terminal inversion without a full-stack norm

Group the \(d\) bond components by their initial vertex. Coefficients are operator matrix entries in orthonormal physical-\(L^2\) coordinates, equivalently discrete-sum Fourier coefficients; an integral-kernel convention would require the additional lattice-volume measure factor. Use the shortest periodic \(\ell^1\) distance between vertices, with physical spacing \(b_k\). Replacing this by bond-midpoint distance changes only a bounded block-scale offset.

Let \(B_k=b_{k+1}^2S_k\). Equation (GL10), together with the finite-range gauge and readout terms in (GL1), gives a uniform exponential row/column moment. In particular, both

$$
\begin{aligned}
\sup_x\sum_y\|(B_k)_{xy}\|
\left(e^{\theta d(x,y)/b_{k+1}}-1\right),\\
\sup_y\sum_x\|(B_k)_{xy}\|
\left(e^{\theta d(x,y)/b_{k+1}}-1\right)
\end{aligned}
\tag{GL11}
$$

tend uniformly to zero as \(\theta\downarrow0\). Choose one \(\theta>0\) making both at most \(\beta_*/2\).

For nonempty \(F\), let \(f(x)=d(x,F)/b_{k+1}\) and let \(W_\theta\) multiply by \(e^{\theta f(x)}\). The torus distance is Lipschitz, so the block Schur test bounds

$$
\|W_\theta S_kW_\theta^{-1}-S_k\|
\le\frac{\beta_*}{2b_{k+1}^2}.
$$

Since \(\|S_k^{-1}\|\le b_{k+1}^2/\beta_*\), a resolvent Neumann series gives
\(\|W_\theta S_k^{-1}W_\theta^{-1}\|\le2b_{k+1}^2/\beta_*\).
The size of \(W_\theta\) on a large finite torus never enters the bound. Hence

$$
\boxed{
\|\chi_ES_k^{-1}\chi_F\|
\le\frac{2b_{k+1}^2}{\beta_*}
e^{-\theta d(E,F)/b_{k+1}}.}
\tag{GL12}
$$

All constants are independent of volume, cutoff, and completed depth at fixed \(d,L,\eta,\alpha\). This argument acts on the terminal Schur carrier; it never assumes uniform coercivity of the enlarged full-stack operator.

## Conditional curvature observables and source response

Let \(\gamma_{k,B}\) be the completed terminal Gaussian with precision \(S_k\) and source \(Q_k^*B/(\eta b_{k+1}^2)\). Its curvature law equals the actual law of \(X_k\) conditional on \(X_{k+1}=B\). For smooth real curvature observables \(F,G\), define
\(N_{k,B}(F)=(\mathbb E_{\gamma_{k,B}}\|\nabla F\|_{b_k}^2)^{1/2}\).
Assume the gradients have the declared supports and finite norms. The Gaussian interpolation argument (LC16) and (GL12) imply

$$
|\operatorname{Cov}(F,G\mid B)|
\le\frac{2b_{k+1}^2}{\beta_*}
e^{-\theta d(\operatorname{supp}\nabla F,\operatorname{supp}\nabla G)/b_{k+1}}
N_{k,B}(F)N_{k,B}(G).
\tag{GL13}
$$

For a coarse perturbation \(h\), let \(E_h=\operatorname{supp}(Q_k^*h)\). Differentiating the normalized Gaussian law gives

$$
\left|\mathrm d_B\mathbb E_{\gamma_{k,B}}F[h]\right|
\le\frac{2}{\eta\beta_*}
e^{-\theta d(\operatorname{supp}\nabla F,E_h)/b_{k+1}}
N_{k,B}(F)\|h\|_{b_{k+1}}.
\tag{GL14}
$$

As in the one-step theorem, no nonlocal coarse projection of \(h\) is necessary. Uniform observable-gradient envelopes or control of renormalized sources are separate requirements; the Gaussian kernel bound does not supply them automatically.

[[library/the-classically-perfect-fixed-point-action-for-su3-gauge-theory/inq|DeGrand et al.]] supplies the covariance-iteration and transverse-inversion precedent. [[library/covariant-axial-gauge/inq|Dimock's accumulated hard-block analysis]] supplies a related decay-and-inversion architecture. The regular soft-kernel strip estimate (GL2)--(GL10) and the stated constants are derived here, not attributed to those different block constructions.

The [[rg-covariance-residue/receipts/gaussian_locality_receipt.py|Gaussian locality receipt]] checks the high-alias inequality on finite samples, (GL6)--(GL8), continuation to nonzero complex null-cone points, full-symbol periodicity and real positivity, and the weighted matrix lemma on a declared finite completion. These checks support the algebraic conventions; the analytic argument above, not finite sampling, supplies uniformity. The actual multilevel gauge Schur identity is tested separately by the [[rg-covariance-residue/receipts/endpoint_average_receipt.py|endpoint-average receipt]].

The distinction from a mass gap is exact. The prior symbol still vanishes quadratically at low momentum; local coefficients do not remove its infrared modes. Conditioning controls a shell while retaining the soft long-distance field downstream. A Yang--Mills proof still needs the full non-Abelian law, regulator-uniform source control, a positive retained infrared exponent, and the continuum reconstruction required by [[contemporary-puzzles/yang-mills-mass-gap/puzzle-as-posed|the Clay statement]].
