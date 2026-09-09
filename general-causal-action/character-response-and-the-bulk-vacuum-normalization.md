# One Character Variation Links Bulk Vacuum Weight and the Soft Gap

The same prepared-character change has an extensive effect on the planar vacuum normalization and a soft-frequency effect on the first physical gap. Their normalized derivatives have a fixed ratio in the controlled growing-patch limit. Both responses come from the same compact Hamiltonian with its additive normalization retained. This supplies a joint bulk and spectral comparison; it does not identify the character parameter with cosmic scale or fix an independently allowed scalar normalization.

**Status: exact finite trace identity and proved joint response limit on the weighted planar confinement window.** [[equal-character-hessians-and-the-nonlinear-source-discriminator|EH]] fixes the preparation family and common energy unit. [[weighted-character-gap-coefficient-and-the-spatial-soft-mode|The spatial coefficient]] supplies its soft-mode response. [[uniform-weighted-character-return-and-the-soft-gap|The uniform weighted return]] controls the actual vacuum and gap derivatives. [[closed-normalization-and-cosmic-response|CN]] owns the distinction between closed normalization and a vacuum-centered spectrum.

## Keep the closed trace before centering the vacuum

On the open \(L\times L\) patch, put \(N=L^2\), \(n=L+1\), and retain every vertex Gauss constraint. Use EH's fixed representation and positive weight \(A_\varepsilon\), with \(\varepsilon\) in a compact interval \(I\subset(-1/14,1/16)\). Write
\[
\widehat H_{\varepsilon,L,h}
=h^2\mathsf C_{\rm raw}
+h^{-2}\sum_p w_\varepsilon(U_p),\qquad
w_\varepsilon=W_{A_\varepsilon}/15,\qquad
E=\kappa/h^2.
\tag{BV1}
\]
The potential vanishes at the identity. No parameter-dependent scalar is added to this specified operator. Derivatives in \(\varepsilon\) hold \(L,h,\kappa\) and the original source coordinates fixed, so the common physical energy unit \(E\) is unchanged.

Let \(\mathcal E_{\varepsilon,L}(h)\) be its actual vacuum energy and \(\Delta_{\varepsilon,L}(h)\) its first physical gap. For each fixed positive scaled duration \(T\), define
\[
Z_{\varepsilon,L,h}(T)
=\operatorname{Tr}_{\rm phys}e^{-T\widehat H_{\varepsilon,L,h}}.
\]
Compact ellipticity makes the heat operator trace class. The character derivative is bounded on this fixed compact carrier. Duhamel differentiation and trace cyclicity give
\[
-\frac1T\partial_\varepsilon\log Z(T)
=\frac{\operatorname{Tr}_{\rm phys}
 [(\partial_\varepsilon\widehat H)e^{-T\widehat H}]}
 {\operatorname{Tr}_{\rm phys}e^{-T\widehat H}}
\xrightarrow[T\to\infty]{}
\partial_\varepsilon\mathcal E_{\varepsilon,L}(h).
\tag{BV2}
\]
The limit uses the actual simple vacuum and its finite-system separation. It is taken at fixed \(L,h,\varepsilon\); no interchange with spatial growth is asserted.

Centering the transfer instead gives
\[
\overline Z(T)=e^{T\mathcal E_{\varepsilon,L}(h)}Z(T),\qquad
\partial_\varepsilon\log\overline Z(T)
=\partial_\varepsilon\log Z(T)
+T\partial_\varepsilon\mathcal E_{\varepsilon,L}(h).
\tag{BV3}
\]
The leading vacuum term cancels exactly. The relative excitation still changes. This is CN's scalar/centered distinction inside one explicitly normalized family.

## The vacuum character response is a local fourth moment

Let \(C_L=\sqrt{4I-\operatorname{Adj}_{L\times L}}\) and \(c_p=(C_L)_{pp}\). The harmonic vacuum has three color components at each face, with component variance \(c_p\). The fixed fourth-character tangent gives
\[
\partial_\varepsilon V_2
=-\frac7{120}\sum_p|X_p|^4.
\]
Since \(\mathbb E_0|X_p|^4=3(3+2)c_p^2\), the derivative of the second vacuum coefficient is
\[
\boxed{
v_L=-\frac78\sum_p c_p^2.}
\tag{BV4}
\]
The first operator and first vacuum correction are independent of \(\varepsilon\), so their virtual-transition term has zero parameter derivative. Formula (BV4) also follows directly from coefficientwise Feynman–Hellmann.

The uniform weighted return proves, for \(0<h n^{10}\le\eta_I\),
\[
\boxed{
\partial_\varepsilon\mathcal E_{\varepsilon,L}(h)
=h^2v_L+O_I(h^4n^{13}),}
\tag{BV5}
\]
uniformly in \(\varepsilon\in I\) and \(L\). This is a derivative estimate proved from differentiated compact quasimodes, not a derivative taken through an unspecified remainder. Integrating on \(I\) gives the same bound multiplied by \(|\varepsilon_2-\varepsilon_1|\) for the corresponding parameter difference.

## The squared diagonal has a bulk limit

Define
\[
c_\infty=\frac1{\pi^2}\int_0^\pi\!\!\int_0^\pi
\sqrt{4-2\cos x-2\cos y}\,dx\,dy,\qquad
B_L=\frac1{L^2}\sum_p c_p^2.
\tag{BV6}
\]
The spectral interval lies in \([0,8]\). The scalar inequality \(\sqrt\lambda\ge\lambda/\sqrt8\) and Cauchy–Schwarz imply
\[
\sqrt2\le c_p\le2,\qquad \sqrt2\le c_\infty\le2.
\]
To prove \(B_L\to c_\infty^2\), approximate \(\sqrt\lambda\) uniformly on \([0,8]\) by a fixed polynomial \(p_m\), with error at most \(\delta\). For any face farther than \(m\) graph steps from the boundary, the diagonal of \(p_m(4I-\operatorname{Adj})\) agrees with that on the infinite square lattice: every contributing walk has length at most \(m\) and remains inside the patch. Fourier transformation identifies the infinite-lattice square-root diagonal with \(c_\infty\). Therefore \(|c_p-c_\infty|\le2\delta\) on those interior faces.

The remaining boundary strip has \(O(mL)\) faces. The preceding uniform diagonal bounds yield
\[
\limsup_{L\to\infty}|B_L-c_\infty^2|\le8\delta.
\]
Taking arbitrarily small \(\delta\), after fixing the corresponding polynomial, proves
\[
\boxed{B_L\longrightarrow c_\infty^2,\qquad
\frac{v_L}{L^2}\longrightarrow-\frac78c_\infty^2.}
\tag{BV7}
\]
This argument concerns a specified harmonic covariance. It does not presume a thermodynamic limit of the compact vacuum.

## The same actual parameter controls two different spatial scales

Let \(\omega_L=2\sqrt2\sin(\pi/(2n))\). The spatial coefficient theorem gives
\[
\frac{k_L}{2\omega_L}\longrightarrow-\frac76c_\infty,
\]
where the actual gap derivative is
\(\partial_\varepsilon\Delta_{\varepsilon,L}(h)
=h^2k_L+O_I(h^4n^{13})\).
Introduce the two normalized actual responses
\[
\mathcal V_{L,h,\varepsilon}
=\frac{\partial_\varepsilon\mathcal E_{\varepsilon,L}(h)}
 {L^2h^2},\qquad
\mathcal G_{L,h,\varepsilon}
=\frac{\partial_\varepsilon\Delta_{\varepsilon,L}(h)}
 {2\omega_Lh^2}.
\tag{BV8}
\]
For every sequence \(L\to\infty\), \(0<h_L n^{10}\le\eta_I\), the two errors are respectively \(O_I(h_L^2n^{11})\) and \(O_I(h_L^2n^{14})\), which tend to zero. Thus, uniformly over \(\varepsilon\in I\),
\[
\boxed{
\mathcal V_{L,h_L,\varepsilon}\longrightarrow-\frac78c_\infty^2,
\qquad
\mathcal G_{L,h_L,\varepsilon}\longrightarrow-\frac76c_\infty,
\qquad
\frac{\mathcal G_{L,h_L,\varepsilon}}
 {\mathcal V_{L,h_L,\varepsilon}}
\longrightarrow\frac4{3c_\infty}.}
\tag{BV9}
\]
The limiting denominator is strictly negative, so the ratio is well defined for sufficiently large \(L\). The same limits hold for finite-difference responses divided by a nonzero \(\varepsilon_2-\varepsilon_1\), by the integrated uniform derivative estimates.

The bulk coefficient grows as \(L^2\); the gap coefficient decreases as \(1/L\). Their relation is fixed by the common covariance and character tangent. A large closed vacuum response therefore need not produce a size-independent excitation scale. In physical units the derivatives acquire the same factor \(E\), so their appropriately normalized ratio is unchanged.

The character redistribution is applied uniformly across faces, but it is not the homogeneous dilation of [[conditional-scale-scores-and-the-closed-response|CS17]]. A geometric cosmic-scale source has not been constructed. Moreover adding a scalar \(a(\varepsilon,L,h)I\) would shift (BV2), (BV5) and \(\mathcal V\) while leaving the gap and \(\mathcal G\) unchanged. BV9 is consequently a relation within the specified prepared amplitude and additive normalization; it does not remove CN's possible central freedom. The growing-patch window is still a rapidly confining isolated planar trajectory, with no fixed-coupling thermodynamic or four-dimensional Yang–Mills return asserted.
