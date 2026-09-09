# Reflection Sewing and the Auxiliary Boundary Carrier

The same determinant preparation has a positive temporal transfer when its hypercubic amplitude is sewn across an actual time cut. No conditional-resampling clock is needed. The transfer retains all auxiliary boundary vectors and factors through their gauge-invariant carrier; spatial-link fiber directions can be exact null directions, so their original multiplication algebra does not automatically survive as a time-zero operator algebra. On every fixed finite slab, the many-copy Wilson limit also preserves the reflected frame-source forms. This supplies a chronological return from the declared amplitude, not a four-dimensional continuum construction or a uniform physical gap.

## Slice the existing joint amplitude

Use [[determinant-response-sewing-and-relational-rigidity|DS3 and DS10a]] with \(\nu\in\mathbb N_{>0}\), \(0<r<1\), a compact group \(G\), and a supplied unitary representation \(\rho:G\to U(n)\). Choose one coordinate of a homogeneous \(D\)-dimensional hypercubic graph as time, \(D\ge2\), and put \(w=(2D)^{-1}\), \(\kappa=rw>0\). Keep a fixed finite open spatial graph \(\Lambda\). This time direction and a duration assigned to one lattice step are declared realization data.

A slice consists of its spatial links \(U\) and all vectors
\(\Xi=(\xi_x^{(a)})_{x\in\Lambda,\,1\le a\le\nu}\). Use
\[
dq=\prod_{e\in E_{\rm sp}}dU_e\,d\Xi,\qquad
d\Xi=\prod_{x,a}\frac{d^{2n}\xi_x^{(a)}}{\pi^n},\qquad
\|\Xi\|^2=\sum_{x,a}\|\xi_x^{(a)}\|^2.
\tag{RS1}
\]
The spatial slice action and its half-weight are
\[
V(U,\Xi)=\|\Xi\|^2-
2\kappa\sum_{\{x,y\}\in E_{\rm sp},a}
\operatorname{Re}\bigl(\xi_x^{(a)*}\rho(U_{xy})\xi_y^{(a)}\bigr),
\qquad b(U,\Xi)=e^{-V(U,\Xi)/2}.
\tag{RS2}
\]
One orientation is used in the edge sum. The two oriented adjacency blocks give the factor two. The spatial degree is at most \(2(D-1)\), so
\[
V(U,\Xi)\ge c_{\rm sp}\|\Xi\|^2,\qquad
c_{\rm sp}=1-2(D-1)\kappa,\qquad
c_{\rm sp}-2\kappa=1-r>0.
\tag{RS3}
\]

Integrate only the temporal links between two neighboring slices. The actual temporal kernel is
\[
K(\Xi,\Xi')=
\int_{G^\Lambda}
\exp\!\left[
2\kappa\sum_{x,a}
\operatorname{Re}\bigl(\xi_x^{(a)*}\rho(g_x)\xi_x^{\prime(a)}\bigr)
\right]\prod_xdg_x,
\]
\[
\boxed{\quad
\mathsf T(q,q')=b(q)K(\Xi,\Xi')b(q').
\quad}
\tag{RS4}
\]
Every temporal link is shared by the same \(\nu\) copies. Haar integration is performed once per link, not independently for each copy. This is a kernel from the original Gaussian hopping amplitude, not a comparison built from its already integrated frame marginal.

For an open strip of \(N\) temporal steps, the original on-site weights at both endpoints give
\[
Z_N=\langle b,\mathsf T^N b\rangle_{L^2(dq)}.
\tag{RS5}
\]
Multiplying the kernels puts \(b^2=e^{-V}\) at every interior slice; the two boundary vectors supply the remaining halves. Thus sewing neighboring strips is ordinary kernel composition with the inherited slice measure.

## The cross-plane kernel is positive

View the auxiliary vector space as a real Euclidean space. Its unaveraged kernel is
\[
k_0(\Xi,\Xi')=e^{2\kappa\operatorname{Re}\langle\Xi,\Xi'\rangle}.
\]
The symmetric-tensor feature map
\[
\Phi_\kappa(\Xi)=
\bigoplus_{m\ge0}\sqrt{\frac{(2\kappa)^m}{m!}}\,\Xi^{\otimes m}
\tag{RS6}
\]
has inner product \(k_0\) and squared norm \(e^{2\kappa\|\Xi\|^2}\). The site group \(\mathcal G=G^\Lambda\) acts orthogonally, with the same \(\rho(g_x)\) on all copies at site \(x\). Its induced feature action is unitary. Let \(P_{\mathcal G}^{\rm feat}\) be its Haar projection. Then
\[
K(\Xi,\Xi')=
\langle\Phi_\kappa(\Xi),
P_{\mathcal G}^{\rm feat}\Phi_\kappa(\Xi')\rangle .
\tag{RS7}
\]
This proves positive definiteness. It also shows that \(K\) is invariant under separate site-gauge transformations of its two arguments. Pointwise, \(K>0\).

The weighted feature map has finite squared integral:
\[
\int b(q)^2K(\Xi,\Xi)\,dq
\le\int e^{-(c_{\rm sp}-2\kappa)\|\Xi\|^2}\,d\Xi
=(1-r)^{-n\nu|\Lambda|}<\infty.
\tag{RS8}
\]
Its Gram operator \(\mathsf T\) is therefore positive and trace class on
\(\mathcal H_{\rm slice}=L^2(dq)\). In particular it is bounded and self-adjoint. The bound uses the repeated homogeneous slicing, not merely positivity of the precision on one isolated finite graph.

Reflect an open strip across a temporal link plane, reversing the orientations of the crossed links and complex conjugating the positive-side observable. Integrating either half leaves a boundary amplitude \(h_F\). For bounded positive-side histories, the unnormalized reflected form is
\[
\int(\Theta F)G\,d\widehat\mu_{\rm unnorm}
=\langle h_F,\mathsf T h_G\rangle .
\tag{RS9}
\]
Equation (RS7) makes the diagonal nonnegative. The Gaussian estimate above justifies the integrals. This proves temporal link-reflection positivity of the joint law, and hence of its frame marginal for frame-only histories. On a periodic cylinder every crossed reflection component must be retained. Reflection-symmetric paired insertions preserve the same argument; arbitrary complex modifications of the action do not automatically define a new reflection-positive state.

This is a direct factorization for the present induced-boson amplitude. It uses the transfer/OS distinction recorded in [[global-local-response-reconstruction/vacuum-boundary-gluing-and-wall-response|vacuum boundary gluing]], rather than importing [[library/construction-of-a-selfadjoint-strictly-positive-transfer-matrix-for-euclidean-lattice-gauge-theories/inq|the Wilson transfer theorem]] as a theorem about a different action.

## The supported boundary carrier is determined by the factorization

Define the actual slice marginal weight
\[
m(\Xi)=\int b(U,\Xi)^2\,dU>0,\qquad
\mathcal H_{\rm aux}=L^2(m(\Xi)d\Xi).
\]
The map and its adjoint are
\[
(Jh)(U,\Xi)=b(U,\Xi)h(\Xi),\qquad
(J^*f)(\Xi)=\frac1{m(\Xi)}\int b(U,\Xi)f(U,\Xi)\,dU.
\tag{RS10}
\]
Thus \(J\) is an isometry. On \(\mathcal H_{\rm aux}\), let
\[
(\widetilde{\mathsf T}h)(\Xi)
=\int K(\Xi,\Xi')h(\Xi')m(\Xi')\,d\Xi'.
\]
Direct substitution gives
\[
\boxed{\mathsf T=J\widetilde{\mathsf T}J^*.}
\tag{RS11}
\]
This formulation never treats the unweighted exponential kernel as a bounded operator on Lebesgue \(L^2\).

Both \(m\) and \(J\) respect the site-gauge action. Temporal Haar integration makes \(\widetilde{\mathsf T}\) vanish on the orthogonal complement of
\[
\mathcal H_{\rm aux}^{\mathcal G}
=L^2(m\,d\Xi)^{G^\Lambda}.
\tag{RS12}
\]
It is injective on this invariant space. To see this, conjugate by multiplication by \(\sqrt m\) to \(L^2(d\Xi)\). Put
\[
s(\Xi)=\sqrt{m(\Xi)}e^{\kappa\|\Xi\|^2},\qquad
\mathsf C_\kappa(\Xi,\Xi')=e^{-\kappa\|\Xi-\Xi'\|^2}.
\]
Here \(s>0\), is gauge invariant, and is bounded by (RS3). The transformed operator is
\[
M_s\mathsf C_\kappa P_{\mathcal G}M_s.
\tag{RS13}
\]
Gaussian convolution commutes with the orthogonal gauge action and has a strictly positive Fourier multiplier. On invariant functions its quadratic form is therefore strictly positive on every nonzero \(M_sh\). Since \(M_s\) is injective, (RS13) has zero kernel there.

Consequently the closed support of the full transfer is exactly
\(J\mathcal H_{\rm aux}^{\mathcal G}\). In the full gauge-invariant slice carrier, its null space is \(\ker J^*\). Spatial-link directions with zero weighted fiber integral can therefore be exact null directions. Removing them is a consequence of the actual transfer form; it is not a declaration that the original pure-gauge slice Hilbert space has an injective transfer.

On its supported auxiliary carrier, the kernel is strictly positive, the operator is compact and positive, and its top eigenvalue \(\lambda_0>0\) is simple with a positive eigenvector. Normalizing by \(\lambda_0\) gives an injective positive contraction and hence
\[
H_{\rm aux}
=-\frac1{a_t}\log(\widetilde{\mathsf T}/\lambda_0)
\tag{RS14}
\]
on its spectral domain, for a declared temporal-step duration \(a_t>0\). Integer powers have the original chronological sewing law. No claim that fractional powers are Markov kernels, or that \(H_{\rm aux}\) is already pure Yang--Mills time translation, is needed. A finite compact transfer and a simple top eigenvalue supply no volume-uniform or continuum estimate.

## Preserve the source law through the boundary reduction

For a bounded slice source \(F(U,\Xi)\), compression gives
\[
J^*M_FJ=M_{\overline F},\qquad
\overline F(\Xi)=
\frac{\int b(U,\Xi)^2F(U,\Xi)\,dU}{m(\Xi)}.
\tag{RS15}
\]
For gauge-invariant \(F\), the returned function is gauge invariant. However
\[
\overline{FG}\ne\overline F\,\overline G\quad\text{in general},\qquad
\overline{|F|^2}-|\overline F|^2
=\operatorname{Var}(F\mid\Xi)\ge0.
\tag{RS16}
\]
The variance uses the actual slice conditional density \(b^2/m\). The null space of the full transfer need not be invariant under \(M_F\). Thus the original spatial Wilson multiplication algebra does not automatically act by its original time-zero multiplication on the supported carrier.

Full marked amplitudes remain available. At each slice, keep every coincident source factor inside one conditional integral in (RS15); averaging the factors separately would erase their conditional covariance. Products of sources at distinct slices insert the corresponding conditional factors between the actual transfers. Endpoint half-weights in (RS5) must also be retained.

Temporal-link marks are inserted before the Haar integral in (RS4). A source involving several slices or links retains all of its arguments until those variables are integrated. Such a source may return a kernel with memory rather than a single multiplication operator. Bounded cylinder marks are covered directly; Gaussian linear or quadratic marks additionally require integrability of the modified precision. None of these operations permits resetting a boundary law or dropping a determinant. This is the full-amplitude convention of [[conditional-exchange-through-cuts-and-retained-marks|sourced cut sewing]], applied to chronological transfer rather than resampling.

## The many-copy return preserves reflected frame histories

On a fixed finite open hypercubic slab with \(M\) vertices, use the [[cycle-determinants-and-the-pure-gauge-return|CY6–8]] path
\[
r_\nu\to0,\qquad b_\nu=2\nu r_\nu^4w^4\to b\in(0,\infty),\qquad
\varepsilon_\nu=
\frac{\nu Mn}{3}\frac{r_\nu^6}{1-r_\nu}\longrightarrow0.
\tag{RS17}
\]
Let \(p_\nu\) be its normalized frame density after integrating all auxiliaries, and \(p_{W,b_\nu}\) the Wilson density on that same slab. The explicit longer-walk estimate gives
\[
e^{-\varepsilon_\nu}\le
\frac{p_\nu}{p_{W,b_\nu}}
\le e^{\varepsilon_\nu}.
\]
Thus bounded positive-half frame histories satisfy
\[
\boxed{\quad
\left|
\langle\Theta F\,G\rangle_\nu-
\langle\Theta F\,G\rangle_{W,b_\nu}
\right|
\le(e^{\varepsilon_\nu}-1)\|F\|_\infty\|G\|_\infty.
\quad}
\tag{RS18}
\]
The same estimate applies to any fixed finite set of temporal shifts whose supports lie in the slab. Since \(b_\nu\to b\), continuity of the finite Wilson density also gives convergence to the fixed-\(b\) reflected forms.

This returns finite chronological source Gram forms and shifted matrix elements, not only a one-slice state. It does not identify the changing auxiliary Hilbert spaces, prove convergence of their transfer operators or spectra, or give uniform control in temporal depth or spatial volume: \(M\) remains in (RS17). It is therefore a concrete bridge toward a pure-gauge history return without a fresh boundary reset, while the common limiting carrier and physical continuum theorem remain to be constructed.

## What this revision selects

Temporal factorization selects the transfer and its supported boundary state from the same positive joint amplitude once the temporal slicing is declared. It avoids choosing an auxiliary conditional-update pace and then identifying that pace with physical time. The contrast with [[euclidean-configuration-diffusion-and-the-physical-clock|whole-configuration stochastic evolution]] is an operation-level distinction, not a demand for an extra fitted rate.

The group, representation, graph, hopping strength, copy law and physical temporal calibration remain declared. Reflection positivity does not by itself select four-dimensional locality, covariance, the required ultraviolet return or a positive infinite-volume energy edge. The next conjectural step can use (RS18) to seek a common chronological realization under the desired limits; it cannot replace that task by a gap of a finite auxiliary transfer.
