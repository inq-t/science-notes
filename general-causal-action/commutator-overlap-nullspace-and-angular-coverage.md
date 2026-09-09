# Commutator Overlap: Nullspace and Angular Coverage

The scalar Gram overlap of commutator preparations retains every radial and even-axis channel on its natural feature quotient, but erases central phase and inversion information exactly. Its surviving angular dependence is therefore substantial without containing the signed relative-angle response required by the correlated Yang–Mills interface benchmark. The feature quotient also fails to respect frame multiplication; identifying it with a physical quotient would require a separate construction.

## The feature identifies precisely a radius and an unoriented axis

Use [[multiplication-sensitive-cycle-preparations|the tracial two-by-two preparation]], with \(V=M_2(\mathbb C)\), \(h=\operatorname{Tr}/2\), \(G=g_0P_0+gP_1\), \(g_0,g>0\), and \(\beta>0\). Define
\[
f_U(\xi)=e^{-\frac\beta2\|[U,\xi]\|_h^2},
\qquad
K_\beta(U,V)=\mathbb E_G[f_U(\xi)f_V(\xi)],
\quad U,V\in U(2).
\tag{AN1}
\]
Write a frame, up to central phase, as \(U=aI+i\sqrt t\,\mathbf n\cdot\boldsymbol\sigma\), where \(a^2+t=1\), \(0\le t\le1\). If \(z\in\mathbb C^3\) is the traceless preparation coordinate, then
\[
f_U(\xi)=
\exp\!\left[-2\beta t\bigl(|z|^2-|\mathbf n\cdot z|^2\bigr)\right].
\tag{AN2}
\]
Consequently the exact feature quotient is
\[
\boxed{\mathcal Q=\{(t,[\mathbf n]):0<t\le1,\ [\mathbf n]\in\mathbb {RP}^2\}\cup\{0\}.}
\tag{AN3}
\]
All axes at \(t=0\) represent the one central-frame feature. To prove exactness, equality of two features almost everywhere implies equality everywhere, by continuity and the full support of the Gaussian. Their logarithms then identify the quadratic matrices \(t(I-\mathbf n\mathbf n^T)\). Their two nonzero eigenvalues determine \(t\), and their null line determines \([\mathbf n]\), unless \(t=0\).

Normalized Haar measure pushes forward to
\[
d\mu_{\mathcal Q}
=\frac2\pi\sqrt{\frac{t}{1-t}}\,dt\,d\omega_{\mathbb {RP}^2},
\tag{AN4}
\]
where the axis measure is normalized. Indeed, the \(SU(2)\) half-trace has density \((2/\pi)\sqrt{1-a^2}\,da\); combining the two branches of \(t=1-a^2\) gives (AN4). Averaging the central phase of \(U(2)\) gives the same quotient law. There is no atom at \(t=0\).

Thus \(U\), \(e^{i\alpha}U\), and \(U^\dagger\) have the same feature. For \(SU(2)\), the generic ambiguity includes independent changes of the signs of \(a\) and the vector part. The scalar preparation variance \(g_0\) drops out of this kernel.

## Every even angular channel is present

For quotient points \((t,[\mathbf n])\), \((u,[\mathbf m])\), put
\[
p=2\beta gt,\quad q=2\beta gu,\quad s=1+p+q,
\quad c=\mathbf n\cdot\mathbf m.
\]
The half-strength specialization of the two-frame determinant gives
\[
\boxed{K_\beta(t,u,c)=\frac1{s\{s+pq(1-c^2)\}}.}
\tag{AN5}
\]
For \(t,u>0\), its uniformly convergent angular expansion is
\[
K_\beta(t,u,c)
=\sum_{k\ge0}\frac{(pq)^k}{s(s+pq)^{k+1}}c^{2k}.
\tag{AN6}
\]
All coefficients are positive. Odd spherical harmonics vanish, while every even degree \(2j\) has a strictly positive angular coefficient: for \(k\ge j\),
\[
\int_{-1}^1 c^{2k}P_{2j}(c)\,dc
=\frac{2(2k)!}{(2k-2j)!!(2k+2j+1)!!}>0.
\tag{AN7}
\]
For \(k<j\) this integral is zero. Rodrigues' formula and integration by parts give (AN7). Hence the retained interaction is not merely a function of the two frame traces: it contains all even relative-axis harmonics.

## There is no additional radial or even-angular nullspace

Let \(\mathsf T\) be the integral operator with kernel (AN1) on \(L^2(U(2),dU)\), and let \(\mathsf E_{\mathcal Q}\) denote conditional expectation onto quotient-measurable functions. Then
\[
\boxed{\ker\mathsf T=\ker\mathsf E_{\mathcal Q},
\qquad \overline{\operatorname{Ran}\mathsf T}=L^2(\mathcal Q,\mu_{\mathcal Q}).}
\tag{AN8}
\]
The range statement identifies the embedded quotient subspace of the original Haar carrier.

**Proof.** The Gram analysis map is
\[
(\mathsf Ah)(\xi)=\int f_U(\xi)h(U)\,dU,
\qquad \mathsf T=\mathsf A^\dagger\mathsf A.
\tag{AN9}
\]
It factors through \(\mathsf E_{\mathcal Q}\). It remains to show that it is injective on the quotient. If \(\mathsf Ah=0\) Gaussian-almost everywhere, continuity makes it zero for every preparation. Evaluate (AN2) on real traceless coordinates \(z=r\mathbf v\), \(|\mathbf v|=1\), and differentiate in \(r^2\) at zero. Compactness permits differentiation under the integral, giving
\[
\int h(t,[\mathbf n])\,t^k
\bigl[1-(\mathbf n\cdot\mathbf v)^2\bigr]^k\,d\mu_{\mathcal Q}=0
\quad\text{for every }k\ge0,\ \mathbf v\in S^2.
\tag{AN10}
\]
Projecting this identity onto an even spherical harmonic of degree \(2j\) in \(\mathbf v\) gives the radial moments of the corresponding coefficient of \(h\). The angular multiplier is nonzero for every \(k\ge j\), since
\[
\int_{-1}^1(1-c^2)^kP_{2j}(c)\,dc
=B(\tfrac12,k+1)
\frac{(\tfrac12)_j(-k)_j}{j!(k+\tfrac32)_j}\ne0.
\tag{AN11}
\]
Here \(B\) is Euler's beta function and \((a)_j\) the rising factorial. The identity follows by integrating the finite even-Legendre polynomial against the beta weight; for \(j>k\) it vanishes.

Thus every moment of the finite complex measure \(t^jh_{2j,m}(t)(2/\pi)\sqrt{t/(1-t)}\,dt\) is zero. Polynomial density on \([0,1]\) makes this measure zero. Since \(t^j>0\) away from the null endpoint, every radial harmonic coefficient vanishes. Even spherical harmonics are complete on \(\mathbb {RP}^2\), so \(h=0\). Finally, self-adjointness gives the range-closure identity in (AN8). \(\square\)

At \(\beta=0\), the kernel is constant and only the constant feature survives; (AN8) assumes \(\beta g>0\). Injectivity on an infinite-dimensional quotient is not a uniform lower bound for this compact operator. [[commutator-preparation-transfer-and-marked-gluing|The Gram transfer construction]] owns its positivity, normalization and supported clock.

## The missing sectors matter for composition and the interface

Every nonzero central-phase Fourier sector is annihilated. Within the central-invariant sector, every inversion-odd function is also annihilated. On \(SU(2)\), the kernel separately annihilates all center-odd functions, such as the fundamental half-trace, and all inversion-odd functions. Equation (AN8) proves that these identifications exhaust the nullspace; no further radial or even-axis directions disappear.

This equivalence is not a multiplication congruence. Take \(U=V=e^{i\pi\sigma_3/6}\). Although \(U\) and \(U^{-1}\) have identical features,
\[
t(UV)=\tfrac34,\qquad t(U^{-1}V)=0.
\tag{AN12}
\]
Therefore ordinary frame multiplication does not descend to \(\mathcal Q\). A feature quotient is not automatically an admissible algebraic or physical quotient.

The distinction is visible in [[coarse-response-memory/correlated-interface-tangent|the complete correlated-interface benchmark]]. Its loop coordinates are \(x=(a,\mathbf u)\), \(y=(b,\mathbf v)\), with \(z=\mathbf u\cdot\mathbf v\), and its exact tangent is \(A(a)b+B(a)z\), with \(B\not\equiv0\) at every positive internal coupling. The crossing half-trace \(b\) changes sign under \(y\mapsto-y\); the relative contraction \(z\) changes sign under \(y\mapsto y^{-1}\). Both are erased by the independent single-frame feature quotients. In fact the entire displayed tangent is odd under \(y\mapsto-y\).

Consequently this Gram quotient cannot reproduce that benchmark by directly identifying its frame labels with those loop holonomies. Even-axis dependence through \(c^2\) does not supply the signed \(z\) channel. This is an obstruction to that direct identification, not proof that the erased distinctions must be physical in every different construction.

A repair must retain orientation-sensitive and center-sensitive information when the intended physical observables require it, or supply a proved recovery map on a larger marked carrier. [[relative-multiplication-transfer-and-the-rotor-limit|The relative-multiplication comparison]] gives a distinct full-support construction; its additional information changes the kernel. Any claimed recovery of the Yang–Mills interface must still transport its full two-channel response, state and normalization, rather than only a scalar susceptibility.
