# Refining Holonomy and a Finite Continuum Threshold

Transport that approaches the identity on shrinking edges can retain a finite positive connection-spectrum threshold without subtracting an on-site counterterm. An explicit Pauli family has an exactly computable lattice edge, a uniform small-spacing bound and a continuum covariant Laplacian with the same limiting edge. This is a diagnostic of realization prescriptions: it distinguishes changing the transport law from merely reweighting a fixed transport. The background, its nonzero amplitude, the continuum arena and the clock prescription are supplied; the calculation does not select them or construct quantum Yang–Mills theory.

## Refine the connection, not only its edge weight

Fix \(d=2\) or \(3\), a spacing \(a>0\), and a declared constant \(g>0\), with \(ag\) dimensionless. On
\[
\mathfrak h_a=\ell^2(a\mathbb Z^d;\mathbb C^2,a^d),
\]
put
\[
U_j(a)=e^{iag\sigma_j},\qquad
(D_{j,a}x)(an)=
\frac{x(a(n+\hat j))-U_j(a)x(an)}{a}.
\tag{RH1}
\]
The Pauli matrices satisfy \(\{\sigma_i,\sigma_j\}=2\delta_{ij}I\). Each \(U_j(a)\) is in \(SU(2)\), and \(U_j(a)\to I\). Define
\[
L_a=\sum_jD_{j,a}^*D_{j,a}.
\tag{RH2}
\]
It acts on sections in this fixed connection, not on a probability law or wavefunction of connections.

For dimensionless lattice momentum \(k\in(-\pi,\pi]^d\), write
\(\theta=ag\), \(c=\cos\theta\) and \(s=\sin\theta\). The exact Fourier symbol is
\[
L_a(k)
=\frac1{a^2}\sum_j
\left(2I-U_j(a)e^{-ik_j}-U_j(a)^*e^{ik_j}\right)
\]
\[
=\frac2{a^2}
\left[
\left(d-c\sum_j\cos k_j\right)I
-s\sum_j\sin k_j\,\sigma_j
\right].
\tag{RH3}
\]
Consequently its two bands are
\[
\lambda_{\pm,a}(k)
=\frac2{a^2}
\left[
d-c\sum_j\cos k_j
\ \pm |s|\sqrt{\sum_j\sin^2k_j}
\right].
\tag{RH4}
\]
The sign attached to an eigenvector can change with \(s\); the ordered bands depend on \(|s|\).

## The exact lattice edge

Set \(x_j=\cos k_j\). Minimizing the lower band amounts to maximizing
\[
c\sum_jx_j+|s|\sqrt{d-\sum_jx_j^2},
\qquad -1\le x_j\le1.
\tag{RH5}
\]
The vector \((x_1,\ldots,x_d,\sqrt{d-\sum_jx_j^2})\) has norm \(\sqrt d\). Cauchy–Schwarz therefore bounds (RH5) by
\[
M=\sqrt{d^2c^2+ds^2}.
\]
Equality is attainable inside the cube: take
\[
x_j=\frac{dc}{M},\qquad
|\sin k_j|=\frac{\sqrt d\,|s|}{M}.
\tag{RH6}
\]
Indeed \(d^2c^2\le M^2\), and these expressions obey \(\cos^2k_j+\sin^2k_j=1\). The signs of the sines may be chosen independently.

Thus the infinite-lattice spectral infimum is exactly
\[
\boxed{
\Gamma_a:=\inf\sigma(L_a)
=\frac2{a^2}\left[d-\sqrt{d^2\cos^2(ag)+d\sin^2(ag)}\right].
}
\tag{RH7}
\]
The formula holds for every \(ag\), not merely in an expansion. A finite periodic torus samples only finitely many \(k\), so its edge is at least \(\Gamma_a\); equality requires that its momentum grid contain a minimizer. Those minimizers are not generally at zero momentum or on a prescribed finite grid.

At coarse spacings with \(ag\in\pi\mathbb Z\), (RH7) vanishes. A positive refinement bound therefore needs a specified small-spacing regime.

## A uniform bound and its finite limit

Rationalizing (RH7) gives
\[
\Gamma_a
=\frac{2(d-1)\sin^2(ag)}
{a^2\left[1+\sqrt{1-\frac{d-1}{d}\sin^2(ag)}\right]}.
\tag{RH8}
\]
Since the denominator's bracket is at most two,
\[
\Gamma_a\ge(d-1)\frac{\sin^2(ag)}{a^2}.
\]
Using \(\sin u\ge2u/\pi\) on \(0\le u\le\pi/2\), one obtains
\[
\boxed{
L_a\ge\delta_g I,\qquad
\delta_g:=\frac{4(d-1)}{\pi^2}g^2,
\quad 0<ag\le\frac\pi2.
}
\tag{RH9}
\]
The same bound holds on every finite periodic torus. It is independent of the number of sites and of the spacing in this regime.

The sharp edge has the limit
\[
\boxed{\Gamma_a\longrightarrow(d-1)g^2.}
\tag{RH10}
\]
For example, its small-spacing expansion is
\[
\Gamma_a
=(d-1)g^2
-\frac{(d-1)(d+3)}{12d}\,a^2g^4
+O(a^4g^6).
\tag{RH11}
\]
The limiting value is a consequence of the declared connection amplitude \(g\), not an internal determination of that amplitude.

## The continuum operator is local

Use physical momentum \(p=k/a\). Taylor expansion of (RH3), uniform on every fixed compact \(p\)-set, gives
\[
L_a(ap)\longrightarrow
L_g(p)=\left(|p|^2+dg^2\right)I
-2g\sum_jp_j\sigma_j.
\tag{RH12}
\]
The error on such a set is \(O(a^2)\) for fixed \(g\). In position space,
\[
\boxed{
L_g=\sum_{j=1}^d(-i\partial_j-g\sigma_j)^2.
}
\tag{RH13}
\]
Its closed form is \(\sum_j\|(-i\partial_j-g\sigma_j)f\|^2\) on \(H^1(\mathbb R^d;\mathbb C^2)\), and its self-adjoint operator domain is \(H^2(\mathbb R^d;\mathbb C^2)\). These statements also follow directly from its Hermitian Fourier symbol and its quadratic growth at large momentum.

The continuum bands are
\[
\boxed{
\lambda_{\pm,g}(p)
=|p|^2+dg^2\pm2g|p|
=(|p|\pm g)^2+(d-1)g^2.
}
\tag{RH14}
\]
Hence \(\inf\sigma(L_g)=(d-1)g^2\), agreeing with (RH10). The lower edge occurs on \(|p|=g\), not at \(p=0\). Its minimizing sphere is a spectral-support statement; on infinite space it does not give a normalizable edge eigenvector. The isolated lattice minimizers approach points on this sphere, while the lattice anisotropy vanishes at fixed physical momentum.

The same connection components cannot all be cancelled by one momentum and one spinor. In contrast, the one-direction version has \((p\pm g)^2\) bands and zero edge. The lower bound in dimensions two and three is not obtained by inserting a separate scalar term \(m^2I\); nevertheless, supplying the noncommuting components \(g\sigma_j\) has supplied substantial geometric data and a scale.

The [[cauchy-response-and-local-action|opposed-response prescription]] may take \(A_g=\sqrt{L_g}\) as a positive clock. Its wave equation has the local principal part \(\partial_t^2-\Delta\) and propagation speed at most one. For the covariant derivative \(\nabla_j=\partial_j-ig\sigma_j\), the local energy density \((|\dot q|^2+\sum_j|\nabla_jq|^2)/2\) bounds its normal flux, giving the usual exterior-cone energy estimate.

Nevertheless this is not a Poincaré vacuum construction. For the supplied spatial translations and the lower clock band \(E_-(p)=\sqrt{\lambda_{-,g}(p)}\),
\[
E_-(p)^2-|p|^2=dg^2-2g|p|<0
\quad\text{when }|p|>\frac{dg}{2}.
\tag{RH14a}
\]
Thus this one-particle joint spectrum is not in the standard forward light cone. Exact finite propagation, positive energy and a positive clock edge do not by themselves supply boost covariance or a mass Casimir.

Passing to the free global-charge-neutral sector does not remove this failure. On \(\mathfrak h\oplus\overline{\mathfrak h}\), the positive clock is \(A_g\oplus\overline A_g\), but the spatial translation generators are \(P_j\oplus(-\overline P_j)\): conjugating \(e^{-iyP_j}\) changes the generator's sign. A lower-band particle packet near \(p\), paired with the conjugate of a lower-band packet near original momentum \(-p\), has both constituents near physical momentum \(p\). Its joint spectral points approach
\[
(E_{\rm pair},P_{\rm pair})=(2E_-(p),2p),\qquad
E_{\rm pair}^2-|P_{\rm pair}|^2=4(dg^2-2g|p|).
\tag{RH14b}
\]
Choosing \(|p|>dg/2\) and sufficiently narrow packets gives neutral states supported outside the forward cone. This uses the same free pair carrier as [[positive-energy-pairs-and-the-neutral-gap]], not a new adjoint diffusion. Replacing \(P_j\) with covariant momenta \(P_j-g\sigma_j\) cannot simply fix the translation signature: their mutual commutators are \(g^2[\sigma_i,\sigma_j]\ne0\). A translation representation requires commuting generators.

## Vanishing elementary loops do not mean a flat continuum

For the actual path \(+i,+j,-i,-j\), composed in transport order, the plaquette is
\[
H_{ij,a}=U_j(a)^*U_i(a)^*U_j(a)U_i(a).
\]
For \(i\ne j\), Pauli multiplication gives
\[
H_{ij,a}
=I+a^2g^2[\sigma_i,\sigma_j]+O(a^3g^3),
\qquad
\frac12\operatorname{Tr}H_{ij,a}
=1-2\sin^4(ag).
\tag{RH15}
\]
Reversing the path changes the leading commutator's sign. In particular the frequently written product \(U_iU_jU_i^*U_j^*\) has the negative leading sign, not the path order displayed here.

Since \(H_{ij,a}\in SU(2)\), its trace identity implies the exact defect
\[
\boxed{
(I-H_{ij,a})^*(I-H_{ij,a})
=4\sin^4(ag)\,I.
}
\tag{RH16}
\]
Elementary loop holonomy tends to \(I\) at order \(a^2\), while the commutator of the continuum covariant derivatives remains nonzero. These are compatible statements: a finite curvature is tested by a shrinking area.

There is an important limitation of the earlier local certificate. One rooted square per vertex in directions \(1,2\) has congestion constant \(B=8\). The [[short-loop-holonomy-and-quantitative-gluing|short-loop bound]] therefore gives only
\[
L_a\ge\frac{\sin^4(ag)}{2a^2}I
=O(a^2g^4)I.
\tag{RH17}
\]
That certificate degenerates during refinement even though the sharp operator edge does not. Equations (RH7)–(RH10) use the full translation-invariant symbol to establish what this microscopic certificate misses. They are not a proof that every family with a nonzero continuum plaquette curvature has a positive spectral edge.

## Convergence on one declared comparison carrier

The continuum Hilbert carrier is
\(\mathfrak h=L^2(\mathbb R^d;\mathbb C^2)\). Put
\(\mathcal B_a=(-\pi/a,\pi/a]^d\), and use the unitary lattice Fourier transform
\[
(\mathcal F_ax)(p)
=\frac{a^d}{(2\pi)^{d/2}}
\sum_{n\in\mathbb Z^d}x(an)e^{-ian\cdot p},
\qquad p\in\mathcal B_a.
\tag{RH18}
\]
Let \(J_a:\mathfrak h_a\to\mathfrak h\) Fourier-transform by (RH18), extend by zero outside \(\mathcal B_a\), and inverse-transform in the continuum. It is an isometry, and \(J_aJ_a^*\to I\) strongly.

For every \(z>0\), the generalized embedded resolvent has Fourier multiplier
\[
\mathbf1_{\mathcal B_a}(p)\,[L_a(ap)+zI]^{-1}.
\]
Pointwise convergence (RH12) and the uniform norm bound \(1/z\) give, by dominated convergence,
\[
\boxed{
J_a(L_a+zI)^{-1}J_a^*
\longrightarrow(L_g+zI)^{-1}
\quad\text{strongly}.
}
\tag{RH19}
\]
This compares the different lattice carriers through specified embeddings; it is not a claim of operator-norm convergence of the unbounded Laplacians.

The uniform lower bound (RH9) also controls the inverse response. For every fixed \(\tau\in\mathbb R\), the continuous bounded function
\[
b_\tau(\lambda)=\frac{e^{-|\tau|\sqrt\lambda}}{2\sqrt\lambda},
\qquad \lambda\ge\delta_g,
\]
gives
\[
\boxed{
J_a\,\frac{e^{-|\tau|\sqrt{L_a}}}{2\sqrt{L_a}}\,J_a^*
\longrightarrow
\frac{e^{-|\tau|\sqrt{L_g}}}{2\sqrt{L_g}}
\quad\text{strongly}.
}
\tag{RH20}
\]
The proof is the same dominated-convergence argument for matrix multipliers. The positive root and the Euclidean duration are the stated response and clock conventions. This covariance cannot be assigned to an arbitrary different dynamics merely because its spatial symbol is positive.

## Local cell averages give the same covariance limit

The Fourier embedding is useful for proof but is not local in position. There is also a local comparison. Let \(I_a x\) equal \(x(an)\) on the centered cell
\[
C_{a,n}=an+[-a/2,a/2)^d.
\]
Then \(I_a\) is an isometry, and its adjoint is the cell-average map
\[
(R_af)(an)=\frac1{a^d}\int_{C_{a,n}}f(x)\,dx.
\tag{RH21}
\]
It sends a compactly supported smear to a finite lattice support, enlarged by at most a cell.

Set \(V_a=J_aR_a\). On the dense class with smooth compact Fourier support, for sufficiently small \(a\) there are no sampling aliases and
\[
\widehat{V_af}(p)
=\left[\prod_{j=1}^d
\operatorname{sinc}\left(\frac{ap_j}{2}\right)\right]\widehat f(p),
\qquad \operatorname{sinc}u=\frac{\sin u}{u}.
\tag{RH22}
\]
This tends to \(\widehat f\). Since \(V_a\) is a contraction, density proves \(V_a\to I\) strongly on \(\mathfrak h\). Its adjoint also converges strongly: the estimate
\(\|V_a^*f-f\|^2\le2\|f\|^2-2\operatorname{Re}\langle f,V_af\rangle\)
suffices.

For any uniformly bounded family of embedded functions of \(L_a\),
\[
I_a b(L_a)I_a^*
=V_a^*\,[J_ab(L_a)J_a^*]\,V_a.
\tag{RH23}
\]
Thus (RH19) and (RH20) also hold with \(I_a\) in place of \(J_a\). In particular the covariance between locally averaged smears converges:
\[
\left\langle R_af,\,
\frac{e^{-|\tau|\sqrt{L_a}}}{2\sqrt{L_a}}R_ah\right\rangle_{\mathfrak h_a}
\longrightarrow
\left\langle f,\,
\frac{e^{-|\tau|\sqrt{L_g}}}{2\sqrt{L_g}}h\right\rangle_{\mathfrak h}.
\tag{RH24}
\]
For the declared centered Gaussian laws, convergence of these covariances gives convergence of finite joint characteristic functions and Wick moments of smeared coordinate fields. It does not establish convergence of pointwise composite operators, interacting laws or entire observable nets.

## The diagnostic changes a premise, not the old theorem

[[pauli-transport-and-the-continuum-scaling-obstruction|The fixed-Pauli scaling obstruction]] holds the transports \(\sigma_j\) fixed while varying positive edge weights. The present family instead changes the transports themselves as \(e^{iag\sigma_j}\). The finite limit is therefore outside that obstruction's hypotheses. It demonstrates that the response realization can matter more than a global rescaling of its output.

The construction has not explained why the background should be constant, why its components should have this form, or why \(g\) should be nonzero. Nor does a supplied continuum \(\mathbb R^d\) derive an arena of observation. The invariant relation \(\inf\sigma(L_g)/g^2=d-1\) is exact for this family; the law and yardstick entering it remain inputs. A foundational construction would need to provide those data and an actual dynamics for them, not treat this positive example as the answer to that prior question.

The [[joint-transport-variance-and-the-source-free-obstruction|joint-variance and source-free test]] makes the missing background law concrete. Constant source-free magnetic Yang–Mills stationarity forces commuting Hermitian components, whereas the present \(g\sigma_j\) have nonzero source double commutators. The positive probe threshold is therefore not evidence that this prescribed background is a Yang–Mills vacuum.

The [[positive-energy-pairs-and-the-neutral-gap|positive-energy pair theorem]] is available for the unbounded self-adjoint root \(A_g\) under its stated form-domain and free Fock assumptions. The [[directed-analytic-realization/neutral-gaussian-return-of-holonomy-response|lattice Gaussian realization]] does not, however, license pointwise continuum Wick squares: their local definition and ultraviolet domains require a separate argument.

The [[directed-analytic-realization/refining_holonomy_receipt.py|refining-holonomy receipt]] and [[directed-analytic-realization/refining-holonomy-receipt-output.txt|its output]] check the finite matrix identities and refinement arithmetic. They do not replace the strong-convergence proof or supply the missing background-selection law.
