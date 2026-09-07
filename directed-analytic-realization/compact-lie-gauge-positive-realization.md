# A Positive Homogeneous Realization for Compact Lie Algebras

The homogeneous commutator potential gives a compact quantum realization for every nonzero compact semisimple Lie algebra and every number \(d\geq2\) of matrix slots. The relevant transverse cost is the trace norm of the adjoint map, not a peculiarity of the \(SU(2)\) cross product. This yields an actual unique gauge-invariant vacuum and a positive centered excitation gap at fixed normalization. It therefore does not select three spatial dimensions or a preferred simple gauge group. A positive-dimensional Lie-algebra center leaves free coordinates and defeats the conclusion on this same Cartesian carrier.

## The declared carrier and closed operator

Let \(\mathfrak g\) be a nonzero compact semisimple real Lie algebra of dimension \(n\), with a fixed positive invariant inner product. Let \(G\) be a connected compact group with this Lie algebra, acting by simultaneous adjoint transformations on
\[
Q=(a_1,\ldots,a_d)\in\mathfrak g^d,\qquad d\geq2.
\tag{CL1}
\]

Use the full Cartesian configuration space and its Lebesgue measure. Choose \(\epsilon>0\), a volume normalization \(\mathcal V>0\), and a nonzero real coupling \(\kappa\). Define

\[
\begin{aligned}
K&=-\frac{\epsilon^2}{2\mathcal V}\sum_{i=1}^d\Delta_{a_i},\\
V(Q)&=\frac{\mathcal V\kappa^2}{2}
\sum_{i<j}\|[a_i,a_j]\|^2,\qquad H=K+V .
\end{aligned}
\tag{CL2}
\]

Precisely, \(H\) is the operator of the closed nonnegative form
\[
\mathfrak h[u]
=\frac{\epsilon^2}{2\mathcal V}\|\nabla u\|_2^2
+\|V^{1/2}u\|_2^2,\qquad
\operatorname{Dom}\mathfrak h
=H^1(\mathfrak g^d)\cap L^2(V\,dQ).
\tag{CL3}
\]
Compactly supported smooth functions form a core: first cut off the tails in both form terms, then mollify on a compact set, where the polynomial potential is bounded. All operator inequalities below mean inequalities of forms.

The parameters, metric, kinetic law and homogeneous carrier remain inputs. For \(d=3\), the potential includes the [[chern-simons-response-and-gauge-action|transgression-derived homogeneous member]]. For general \(d\), (CL2) declares the same commutator model without claiming a three-dimensional transgression selects that number of slots.

## The adjoint trace measures transverse cost

Invariance of the metric makes \(\operatorname{ad}_a\) skew-adjoint. Put

\[
\tau(a)=\operatorname{Tr}_{\mathfrak g}
\sqrt{-\operatorname{ad}_a^2}.
\tag{CL4}
\]

Its kernel is exactly the Lie-algebra center. It is continuous and positively homogeneous. More explicitly, the nonzero singular values of a real skew-adjoint matrix occur in equal pairs. If they are \(\mu_1,\mu_1,\ldots,\mu_r,\mu_r\), and \(B\) is the Killing form, then

\[
\tau(a)^2=4\left(\sum_j\mu_j\right)^2
\geq4\sum_j\mu_j^2=-2B(a,a).
\tag{CL5}
\]

Let \(b_{\mathfrak g}>0\) be the smallest eigenvalue of the positive form \(-B\) relative to the supplied metric. Thus
\[
\tau(a)\geq\sqrt{2b_{\mathfrak g}}\|a\|.
\tag{CL6}
\]

This constant is not asserted optimal. Semisimplicity supplies positivity of \(-B\); compactness supplies the skew-adjoint oscillator geometry.

## A balanced fiber decomposition works for every \(d\geq2\)

On the smooth core, define

\[
T_i=
-\frac{\epsilon^2}{\mathcal V(d-1)}
\sum_{j\ne i}\Delta_{a_j}
+\frac{\mathcal V\kappa^2}{2}
\sum_{j\ne i}\|[a_i,a_j]\|^2.
\tag{CL7}
\]

Every kinetic term appears \(d-1\) times, and every pair potential twice, so
\[
\sum_iT_i=2H.
\tag{CL8}
\]
At \(d=3\), (CL7) is exactly the splitting in the [[homogeneous-gauge-positive-realization|original \(SU(2)\) proof]]. The adjusted kinetic coefficient makes the identity valid for other \(d\), too.

Fix \(a_i\) and diagonalize the nonnegative matrix \(-\operatorname{ad}_{a_i}^2\). For each other slot and each singular value \(\mu\), the corresponding one-coordinate operator is
\[
-\frac{\epsilon^2}{\mathcal V(d-1)}\partial_x^2
+\frac{\mathcal V\kappa^2\mu^2}{2}x^2
\ \geq\
\frac{\epsilon|\kappa|}{\sqrt{2(d-1)}}\mu.
\tag{CL9}
\]
This is the elementary harmonic-oscillator form inequality; \(\mu=0\) contributes a nonnegative free derivative term. Summing all eigen-directions and the \(d-1\) other slots, then integrating over the fixed \(a_i\), gives
\[
T_i\geq
\epsilon|\kappa|\sqrt{\frac{d-1}{2}}\,\tau(a_i).
\tag{CL10}
\]

No differentiable choice of eigenbasis is required: \(T_i\) has no derivative in its fixed parameter \(a_i\). The fiber inequality is coordinate independent and remains valid when eigenvalues coincide or vanish.

Combining (CL6), (CL8) and (CL10) yields

\[
\boxed{
H\geq\epsilon|\kappa|\sqrt{\frac{d-1}{8}}
\sum_i\tau(a_i)
\geq c\sum_i\|a_i\|,\qquad
c=\frac{\epsilon|\kappa|}{2}\sqrt{(d-1)b_{\mathfrak g}}>0.}
\tag{CL11}
\]

Since also \(H\geq K\), averaging proves
\[
\boxed{H\geq\frac12K+\frac c2\sum_i\|a_i\|.}
\tag{CL12}
\]

For the normalized \(SU(2)\) cross product, \(\tau(a)=2\|a\|\) and \(b_{\mathfrak g}=2\). At \(d=3\), \(\kappa=\mathcal V=1\), (CL11) becomes precisely \(H\geq\epsilon\sum_i\|a_i\|\). Already \(d=2\) gives a strictly positive coercive coefficient. This mechanism does not distinguish \(d=3\).

## Compactness selects a genuine vacuum and centered gap

Bounded form norm controls an \(H^1\) norm and a linear configuration moment. Since \(\sum_i\|a_i\|\geq|Q|\), (CL12) bounds the squared norm outside \(|Q|\leq R\) by a constant times \(R^{-1}\). Rellich compactness inside each ball then proves compact embedding of the form domain into \(L^2\), hence compact resolvent of \(H\).

The heat semigroup is positivity improving. The positive free heat kernel is multiplied by a strictly positive Brownian-bridge expectation: the continuous polynomial potential has a finite integral along each continuous path on a finite interval. Compact resolvent and positivity improvement therefore give a simple lowest eigenvalue \(E_0\) and a smooth strictly positive normalized eigenfunction \(\psi_0\). Moreover \(E_0>0\): zero energy would force zero gradient, hence an impossible nonzero constant \(L^2\) function on \(\mathfrak g^d\).

The adjoint action preserves measure and both form terms. Its averaging projection commutes with \(H\), and positivity and uniqueness force \(\psi_0\) to be invariant. Thus restriction to
\[
\mathcal H_{\mathrm{inv}}=L^2(\mathfrak g^d)^G
\tag{CL13}
\]
retains compact resolvent and the same unique ground state. This invariant carrier is infinite dimensional, as witnessed by smooth radial functions. Its next eigenvalue exists and satisfies
\[
\boxed{\Delta_{\mathrm{inv}}
=E_{1,\mathrm{inv}}-E_0>0.}
\tag{CL14}
\]

This is a complete invariant excitation gap for the declared matrix operator. The lower multiplier in (CL11) is not a numerical value for that centered gap. Nor does the proof posit random perturbations of a vacuum: it uses derivative norms, a closed form and its spectrum. The [[algebra/response-factorization-and-the-vacuum|quantum response theorem]] describes the additional divergence term obeyed by \(W_0=-\epsilon\log\psi_0\).

## A central factor remains free

For a compact reductive algebra with nonzero Lie-algebra center,
\(\mathfrak g=\mathfrak z\oplus\mathfrak s\), the invariant metric makes this decomposition orthogonal. The potential is independent of the central coordinates. On this same Cartesian carrier,

\[
H=
-\frac{\epsilon^2}{2\mathcal V}\Delta_{\mathfrak z^d}
\otimes I+I\otimes H_{\mathfrak s}.
\tag{CL15}
\]

The connected adjoint gauge group acts trivially on \(\mathfrak z\), so its invariant carrier retains the whole free factor. If \(\mathfrak s\ne0\), (CL15) has spectrum \([E_{0,\mathfrak s},\infty)\), with no normalizable bottom eigenstate; if \(\mathfrak s=0\), it is simply a free Laplacian. It has neither compact resolvent nor a positive gap above its spectral infimum. For example, increasingly broad normalized central wave packets, tensored with the semisimple ground state, have arbitrarily small excess energy.

This concerns a positive-dimensional Lie-algebra center, not the finite group center of \(SU(2)\) or \(SU(3)\). It also concerns uncompactified Cartesian matrix coordinates, not a different construction with compact holonomy variables. Likewise \(d=1\) or \(\kappa=0\) removes the entire interaction and leaves a free operator.

## The normalization and field-theory boundary remain

Set \(s=(\epsilon/(\mathcal V|\kappa|))^{1/3}\). The unitary dilation \(u(Q)\mapsto s^{nd/2}u(sQ)\) commutes with gauge transformations and gives

\[
\Delta_{\mathrm{inv}}(\epsilon,\mathcal V,\kappa)
=\epsilon^{4/3}|\kappa|^{2/3}\mathcal V^{-1/3}
\Delta_{\mathrm{inv}}(1,1,1).
\tag{CL16}
\]

The fixed Lie metric and \(d\) are unchanged in this formula. Thus the gap is positive at fixed parameters, but not volume uniform under this normalization, and no physical yardstick has been derived. The construction selects neither a gauge algebra nor a spatial dimension. It quantizes homogeneous matrices under global gauge transformations; it does not include the spatial derivative terms that can cancel commutators, local gauge gluing, infinitely many field modes or a proved reducing sector of the full Yang–Mills Hamiltonian.

The [[compact_lie_response_receipt.py|finite compact-Lie receipt]] checks the balanced coefficients, paired singular values, independent diagonal \(\mathfrak{su}(N)\) root traces, the \(SU(2)\) normalization, dilation and the free central-coordinate test. [[compact-lie-response-receipt-output.txt|Its stored output]] does not compute the centered spectral gap. The root tests use the \(-\operatorname{Tr}\) metric, while the cross-product \(SU(2)\) example uses \(-2\operatorname{Tr}\); their different Killing constants are kept explicit.
