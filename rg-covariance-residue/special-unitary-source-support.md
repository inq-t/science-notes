# Special-Unitary Source Support

A collection of Wilson staples acts on one common link, so its largest possible response is the support of their sum over \(SU(3)\), not the sum of six independently maximized plaquettes. That support depends on determinant phase as well as singular values. It is an exact gauge-invariant scalar with a one-angle formula; no smooth choice of a maximizing link is needed.

## The common-link maximization

For a complex \(3\times3\) matrix \(M\), define
\[
h_3(M)=\max_{U\in SU(3)}\frac13\operatorname{ReTr}(U^*M).
\tag{SS1}
\]
This is a support function, not a mass or a spectral eigenvalue. Compactness attains the maximum. For \(g,h\in SU(3)\),
\[
h_3(gMh^*)=h_3(M),\qquad
|h_3(M)-h_3(N)|
\le\frac{\|M-N\|_*}{3}
\le\frac{\|M-N\|_{\rm HS}}{\sqrt3}.
\tag{SS2}
\]
The nuclear norm is denoted by \(\|\cdot\|_*\). Both estimates follow by bounding the same linear test at every unitary. The function is convex and positively homogeneous for nonnegative real scalars. The maximizing set transforms covariantly; a globally smooth single-valued maximizer is a different and generally impossible requirement.

The path-sum trace maximization also appears in [[library/smoothing-algorithms-for-projected-center-vortex-gauge-fields/inq|Virgili--Kamleh--Leinweber]], equation (35). Their subgroup update procedure is not the exact global formula proved here, and the properties of an iterative implementation must not be substituted for those of (SS1).

## Scalar sources remember the center

Write \(z=e^{2\pi i/3}\). The trace-minimum theorem in [[frustrated-su3-conditional-wells|the conditional-well note]] implies, for \(t=\operatorname{Tr}U/3\),
\[
\operatorname{Re}(z^{-j}t)\ge-\tfrac12,\qquad j=0,1,2.
\]
These three half-planes intersect in the triangle with vertices \(1,z,z^2\). Every vertex is attained. The support of the trace image therefore equals the support of this triangle:
\[
\boxed{
h_3(re^{i\theta}I)
=r\max_{j=0,1,2}\cos(\theta-2\pi j/3),
\qquad r\ge0.}
\tag{SS3}
\]
For \(r>0\), the maximizing links are precisely the maximizing central matrices. At a tie the trace lies on a supporting triangle edge, but the equality characterization in the trace-minimum theorem permits only its two endpoints. Thus there is one maximizing center generically and two on a tie ray.

For example,
\[
h_3(3I)=3,\quad h_3(-3I)=\tfrac32,\quad
h_3(-2I)=1,\quad h_3(-I)=\tfrac12.
\tag{SS4}
\]
The first two sources have identical singular values. Removing determinant phase would identify two different support values.

## An exact one-angle reduction

For invertible \(M=L\,\operatorname{diag}(\sigma_1,\sigma_2,\sigma_3)R^*\), put \(\delta=\arg\det M\). The substitution \(V=R^*U^*L\) turns the constraint into \(\det V=e^{i\delta}\). Diagonalize \(V=H\operatorname{diag}(e^{i\phi_j})H^*\). Its objective is
\[
\sum_{i,j}\sigma_i|H_{ij}|^2\cos\phi_j.
\]
The matrix \((|H_{ij}|^2)\) is doubly stochastic. Its linear objective is bounded by a permutation pairing, which is attained by a diagonal \(V\) with the same eigenphases and determinant. Hence
\[
3h_3(M)=
\max_{\phi_1+\phi_2+\phi_3\equiv\delta\ ({\rm mod}\ 2\pi)}
\sum_i\sigma_i\cos\phi_i.
\tag{SS5}
\]
Fix \(\phi_1=t\). Maximizing the other two phases with sum \(\delta-t\) gives
\[
\boxed{
3h_3(M)=\max_{t\in[-\pi,\pi]}
\left[
\sigma_1\cos t+
\sqrt{\sigma_2^2+\sigma_3^2+
2\sigma_2\sigma_3\cos(\delta-t)}
\right].}
\tag{SS6}
\]
This is a global maximization on a compact circle, not a prescription to choose one stationary point. Square-root-zero points must also be included.

If \(M\) is singular, a zero singular direction absorbs the determinant constraint without cost:
\[
h_3(M)=\|M\|_*/3.
\tag{SS7}
\]
In general
\[
\|M\|_*/6\le h_3(M)\le\|M\|_*/3.
\tag{SS8}
\]
The upper bound is the ordinary unitary support. For the lower bound in the nonsingular case choose \(V=e^{i\delta/3}I\) with the principal \(\delta\in[-\pi,\pi]\), so \(\cos(\delta/3)\ge1/2\).

A scalar determinant correction of the polar unitary is consequently a feasible lower bound, not normally an optimizer. At a smooth constrained optimum,
\(\sigma_i\sin\phi_i\) is one common multiplier; equal correction phases need not satisfy this when singular values differ.

The bracketed function in (SS6) is Lipschitz in \(t\) with constant
\(\ell=\sigma_1+\min(\sigma_2,\sigma_3)\), using the reverse triangle inequality on its complex-modulus term. For \(N\) equally spaced angles, if \(h_N\) is one third of the sampled maximum, then in exact arithmetic
\[
h_N\le h_3(M)\le h_N+\frac{\ell\pi}{3N}.
\tag{SS9}
\]
Thus a localization certificate may use a controlled *upper* enclosure. A sampled maximum alone is a lower bound and has the wrong direction for that use. Floating-point evaluation needs its own rounding enclosure before claiming a rigorous numerical certificate.

## Why the support is the right retained object

If \(W_j\) are complementary paths with the active link's endpoints, then
\[
\sum_j\frac13\operatorname{ReTr}(U^*W_j)
\le h_3\!\left(\sum_jW_j\right)\le\sum_jh_3(W_j).
\tag{SS10}
\]
The first bound keeps the requirement that all responses belong to one \(U\). For conjugate central staples \(zI,z^2I\), the rightmost value is two, but the common-link value is \(h_3(-I)=1/2\).

[[coherent-staple-localization|Coherent staple localization]] turns this compatibility gain into an actual joint-form estimate with a smaller block. It uses only the support value, not an arbitrarily chosen branch of the maximizing link.

The [[receipts/coherent_staple_localization_receipt.py|finite receipt]] checks determinant-phase sensitivity, the global-angle formula against feasible unitary tests, gauge invariance, and a full-lattice application. The exact support identities follow from the proofs above.
