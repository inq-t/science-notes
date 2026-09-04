# A Local Completion of Soft Gauge Conditioning

One soft blocking step of a Maxwell field has an exactly equivalent local Gaussian representation for curvature observables. A blockwise partial-divergence gauge replaces the nonlocal coarse gauge projection without changing those conditional expectations. The completed precision has an explicit volume-uniform floor and finite spatial range, so a convergent inverse expansion gives exponential conditional covariance and source-response bounds at the block scale. This is a one-step Gaussian theorem, not a localization theorem for the accumulated nonlinear Yang--Mills law.

## The two carriers

Use the periodic \(d\)-dimensional cubical lattice of [[endpoint-averages-and-quadratic-ultraviolet-control|the endpoint-average theorem]], with fine mesh \(a\), fixed integer blocking factor \(n\ge2\), and \(b=na\). Keep enough blocks for its two-block patches. All scalar, bond, and plaquette inner products use the physical volume factors \(a^d\) or \(b^d\), and fixed real coefficient inner products.

Write \(D\) for the fine scalar gradient, \(C\) for fine curl, and \(D_c\) for the coarse gradient. Let \(Q_0\) be the scalar cell average and \(Q\) the parallel-path bond average. The supplied geometry gives

$$
QD=D_cQ_0,\qquad Q_0Q_0^*=I,\qquad \|Q\|\le1.
\tag{LC1}
$$

Thus \(E_0:=Q_0^*\) extends a coarse scalar as a blockwise constant fine scalar. Put \(P=I-E_0Q_0\), the **local** orthogonal projection onto block-mean-zero scalar fields. It is not a Coulomb projection.

On the harmonic-free Coulomb carrier \(H_f=\ker D^*\cap\{\text{constant bonds}\}^{\perp}\), the first reverse conditional law in [[soft-gaussian-gauge-blocking|soft Gaussian blocking]] has density

$$
\mu_B(\mathrm dA)\ \propto\
\exp\!\left[-\frac12\|CA\|_a^2
-\frac{\lambda}{2}\|\Pi_c(QA-B)\|_b^2\right]\mathrm dA,
\qquad
\lambda=\frac1{\eta b^2},\quad\eta>0.
\tag{LC2}
$$

Here \(B\) belongs to the harmonic-free coarse Coulomb carrier, and \(\Pi_c\) projects orthogonally off coarse gradients. On the mean-zero arguments in (LC2), it equals the harmonic-free coarse projection. The quotient projection makes the displayed precision nonlocal.

Instead use **all** fine bond coefficients and the local precision

$$
\boxed{
\mathcal L
=C^*C+\alpha DPD^*+\lambda Q^*Q,\qquad\alpha>0.}
\tag{LC3}
$$

The corresponding normalized Gaussian is

$$
\gamma_B(\mathrm dA)\ \propto\
\exp\!\left[-\frac12\|CA\|_a^2
-\frac{\alpha}{2}\|PD^*A\|_a^2
-\frac{\lambda}{2}\|QA-B\|_b^2\right]\mathrm dA.
\tag{LC4}
$$

Its extra coordinates are auxiliary gauge and harmonic coordinates. They are not additional physical fields.

## Exact equality on curvature observables

Let \(\Delta=D^*D\). Scalar cell Poincare gives

$$
\|\psi\|_a\le\frac b2\|D\psi\|_a,\qquad \psi\in\ker Q_0.
\tag{LC5}
$$

Indeed the internal Neumann cell Laplacian has smallest positive eigenvalue \(4a^{-2}\sin^2(\pi/(2n))\ge4/b^2\), and the full gradient energy includes the internal bonds. Consequently \(P\Delta P\) is positive definite on \(\ker Q_0\).

At a fixed gauge class represented by \(A\), parameterize the scalar gauge orbit by

$$
\phi=E_0u+\psi,\qquad \psi\in\ker Q_0,
\tag{LC6}
$$

with \(u\) taken modulo the single global scalar constant. Change the \(\psi\) coordinate to

$$
z=PD^*(A+D\phi)
=PD^*A+P\Delta E_0u+(P\Delta P)\psi.
\tag{LC7}
$$

This is an affine bijection for each \(u\), with Jacobian independent of \(A,B,u\). Its inverse need not be local; only the coefficients in (LC3) need locality. Meanwhile

$$
Q(A+D\phi)-B=QA-B+D_cu.
$$

Integrating \(z\) contributes a constant. Integrating \(u\) contributes another constant times

$$
\exp\!\left[-\frac{\lambda}{2}
\|\Pi_c(QA-B)\|_b^2\right].
\tag{LC8}
$$

The determinants may depend on regulator, volume, and gauge convention. They cancel in normalized expectations and do not have to be bounded uniformly for this identity.

Harmonic bond modes are not gauge modes. Since \(Q\) preserves constants and spatial means, the induced quotient density separates them as a Gaussian factor. Integrating them instead of fixing them to zero does not change the distribution of \(CA\). Thus, for every integrable \(F(A)=f(CA)\),

$$
\boxed{\mathbb E_{\mu_B}F=\mathbb E_{\gamma_B}F.}
\tag{LC9}
$$

In particular,

$$
\operatorname{Cov}_{\mu_B}(CA)=C\mathcal L^{-1}C^*.
\tag{LC10}
$$

The covariance of a chosen potential representative is not asserted to agree. Winding or harmonic-sensitive observables require a separate harmonic prescription.

This is the same gauge-orbit integration principle used in [[library/covariant-axial-gauge/inq|Dimock's modified Feynman gauge]], Proposition 5. The actual projector is different: his \(R_k\) projects onto \(\Delta(\ker Q_k)\), whereas \(P\) here projects onto \(\ker Q_0\). His hard-block constraint also requires the subtraction in equation (134). Neither his projector nor that subtraction is silently imported into the soft law (LC4).

## An explicit bound in the full carrier norm

Write \(A=A_\perp+D\phi\), where \(D^*A_\perp=0\), including possible harmonic modes. Then \(\|A_\perp\|_a=\|[A]\|_a\), the minimum gauge-class norm. In (LC6), the blockwise constant lift satisfies the exact interface-counting identity

$$
\|DE_0u\|_a^2=n\|D_cu\|_b^2.
\tag{LC11}
$$

There are \(n^{d-1}\) crossing bonds per coarse face, and their derivative divides by \(a\), rather than \(b\). Since \(D_cu=QA-QA_\perp\),

$$
\|DE_0u\|_a\le\sqrt n\bigl(\|QA\|_b+\|[A]\|_a\bigr).
$$

Pairing \(P D^*A=P\Delta\psi+P\Delta E_0u\) with \(\psi\), and using (LC5), gives

$$
\|D\psi\|_a
\le\frac b2\|PD^*A\|_a+\|DE_0u\|_a.
$$

Hence

$$
\|A\|_a
\le(1+2\sqrt n)\|[A]\|_a
+2\sqrt n\,\|QA\|_b
+\frac b2\|PD^*A\|_a.
\tag{LC12}
$$

Let \(c=c_{n,d}>0\) be the endpoint theorem's finite-patch constant. Applying its full observation inequality and squaring (LC12) yields

$$
\|A\|_a^2
\le A_1b^2\|CA\|_a^2+A_2\|QA\|_b^2
+\frac34b^2\|PD^*A\|_a^2,
\tag{LC13}
$$

where

$$
A_1=\frac{6d(1+2\sqrt n)^2}{cn^2},
\qquad
A_2=\frac{3(1+2\sqrt n)^2}{cn^d}+12n.
$$

Thus, on the full bond carrier,

$$
\boxed{
\frac{\beta}{b^2}I\le\mathcal L\le\frac{M}{b^2}I,
\quad
\beta=\min\left\{\frac1{A_1},\frac1{\eta A_2},\frac{4\alpha}{3}\right\}>0,
\quad
M=4d(1+\alpha)n^2+\eta^{-1}.}
\tag{LC14}
$$

The upper bound uses \(\|C\|^2,\|D\|^2\le4d/a^2\) and \(\|Q\|\le1\). These conservative constants are independent of total volume and numerical mesh scale at fixed \(n,d,\eta,\alpha\). They do not assert uniformity as the blocking factor grows.

## Local inverse and conditional source transport

Measure bond separation by the shortest periodic \(\ell^1\) distance between bond midpoints. The coefficients of (LC3) have range at most \(R_0=(d+4)b\): \(P\) couples vertices only within one block, gradients enlarge support by one fine bond, and each component of \(Q\) uses its two adjacent blocks.

Set \(T=I-b^2\mathcal L/M\) and \(r=1-\beta/M\in(0,1)\). Then

$$
\mathcal L^{-1}=\frac{b^2}{M}\sum_{j=0}^{\infty}T^j,
\qquad \|T\|\le r.
$$

For bond sets \(E,F\), finite range gives \(\chi_ET^j\chi_F=0\) when \(jR_0<\operatorname{dist}(E,F)\). Summing the remaining geometric tail proves

$$
\boxed{
\|\chi_E\mathcal L^{-1}\chi_F\|
\le\frac{b^2}{\beta}
\exp\!\left[-m\frac{\operatorname{dist}(E,F)}b\right],
\quad
m=\frac1{d+4}\log\frac{M}{M-\beta}>0.}
\tag{LC15}
$$

This estimate is independent of the size of either set. It is an operator-norm estimate, not a sum of entrywise bounds. The certificate depends on the auxiliary gauge parameter \(\alpha\), although the curvature law in (LC9) does not. Therefore \(\beta\) and \(m\) are nonoptimal bounds, not canonical geometric numerals or predicted masses.

It also controls nonlinear **observables of this Gaussian law**. Let \(F,G\) be real smooth curvature observables whose configuration gradients are supported on \(E,F_0\), with finite squared-gradient expectations. Gaussian interpolation gives

$$
\operatorname{Cov}_{\gamma_B}(F,G)
=\int_0^1
\mathbb E\left\langle\nabla F(X),
\mathcal L^{-1}\nabla G(X_t)\right\rangle_a\,\mathrm dt,
\tag{LC16}
$$

where \(X,Y\) are independent with law \(\gamma_B\), and
\(X_t=\mathbb EX+t(X-\mathbb EX)+\sqrt{1-t^2}(Y-\mathbb EX)\).
Both marginals remain \(\gamma_B\). The identity follows by differentiating their joint Gaussian covariance \(t\mathcal L^{-1}\), first for smooth test functions and then by Sobolev approximation. Consequently, with
\(N_B(F)=(\mathbb E_{\gamma_B}\|\nabla F\|_a^2)^{1/2}\),

$$
|\operatorname{Cov}_{\mu_B}(F,G)|
\le\frac{b^2}{\beta}e^{-m\operatorname{dist}(E,F_0)/b}
N_B(F)N_B(G).
\tag{LC17}
$$

For a coarse perturbation \(h\), put \(E_h=\operatorname{supp}(Q^*h)\). Differentiating (LC4) for an observable without explicit \(B\)-dependence gives

$$
\mathrm d_B\mathbb E_{\gamma_B}F[h]
=\lambda\,\operatorname{Cov}_{\gamma_B}
\bigl(F,\langle Q^*h,A\rangle_a\bigr),
$$

and therefore

$$
\boxed{
\left|\mathrm d_B\mathbb E_{\gamma_B}F[h]\right|
\le\frac1{\eta\beta}
e^{-m\operatorname{dist}(E,E_h)/b}
N_B(F)\|h\|_b.}
\tag{LC18}
$$

No coarse projection of the localized perturbation is needed. Formula (LC4) extends the curvature expectation to arbitrary coarse \(B\); coarse gradient and harmonic shifts leave it unchanged by the corresponding fine shifts. For bounded-gradient observables, \(N_B(F)\) can be replaced by a bound uniform in \(B\). For other source classes that uniformity remains to be proved.

This supplies a concrete one-step instance of [[conditioned-source-transport|the conditional score-response mechanism]]. The inverse operates on a configuration-space source derivative. Its spatial decay is not yet a physical clock-energy gap.

## Why the gauge completion is not arbitrary

A full-divergence penalty can change the desired law. In a finite cochain example, take \(A=(x,y)\), \(CA=x\), \(D\phi=(0,\phi)\), \(D_c\phi=(0,\phi)\), and

$$
Q=\begin{pmatrix}1&0\\1&1\end{pmatrix}.
$$

Then \(QD=D_c\), and the projected soft physical precision for \(x\) is \(1+\lambda\). Adding a naive penalty \(\alpha y^2\) to the raw-readout law produces the matrix

$$
\begin{pmatrix}1+2\lambda&\lambda\\\lambda&\lambda+\alpha\end{pmatrix}.
$$

Its \(x\)-marginal precision is \(1+\lambda+\alpha\lambda/(\alpha+\lambda)\), strictly larger. At \(\lambda=\alpha=1\), the curvature variance is \(2/5\) instead of \(1/2\). This abstract cochain example is not claimed to be a lattice average; it disproves the unrestricted gauge-completion shortcut.

In (LC3), only block-mean-zero gauge motion is penalized. Coarse gauge motion remains available for the exact projection in (LC8). That is the structural reason the local replacement preserves the intended observable law.

## What remains after one step

At blocking depth \(k>0\), the actual prior precision is \(P_k\) from the soft Gaussian recursion, not a fresh Maxwell operator. The same orbit argument can extend a gauge-invariant prior upstairs, but a lower comparison \(P_k\ge\Gamma^{-1}K_k\) does not control its spatial range or the weighted inverse. The finite-range proof cannot simply be repeated with that comparison.

The next Gaussian obligation is a uniform local or quantitatively decaying representation of the actual accumulated \(P_k\), or a local enlarged-field representation with controlled elimination. The nonlinear obligation additionally includes the full Wilson law, large fields, holonomies, and renormalized source norms. Finally the retained infrared term must be controlled: the initial Maxwell law remains massless despite the localized conditional fluctuation established here.

[[receipts/endpoint_average_receipt.py|The finite receipt]] checks the adapted completion against the quotient covariance and mean response, the norm constants, gauge-parameter independence, and the naive-completion counterexample. These checks supplement the dimension-independent proof; they do not certify the open multidepth or Yang--Mills conclusions.
