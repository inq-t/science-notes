# Matrix Flat Partners: Rigidity and Its Limits

A matrix-valued superpotential with a scalar homogeneous partner is diagonalizable in one constant basis: it is a family of independent scalar logistic channels, not a non-Abelian extension. A nonscalar homogeneous partner can support genuinely noncommuting channels, but a normalizable zero mode alone then need not exclude gapless channels. This separates operator-level rigidity from the profile identities of one cosmological response and makes the proposed generalization of the binary wall precise.

## A scalar partner forces simultaneous diagonalization

Let \(W:\mathbb R\to\operatorname{Herm}(m)\) be \(C^1\) and set
\[
A=\partial_N+W(N),\qquad A^*=-\partial_N+W(N).
\]
Suppose on compactly supported smooth vectors that
\[
AA^*=-\partial_N^2+\lambda I,\qquad \lambda\in\mathbb R.
\tag{MF1}
\]
Equating coefficients gives
\[
W'=\lambda I-W^2.
\tag{MF2}
\]
Choose a constant unitary that diagonalizes \(W(N_0)\). In that basis, the diagonal solutions of the scalar equations \(w_j'=\lambda-w_j^2\) solve the matrix equation with the same initial value. Uniqueness of this finite-dimensional polynomial ODE makes them the unique solution wherever it exists. Therefore
\[
\boxed{[W(N),W(M)]=0\quad\text{for all }N,M.}
\tag{MF3}
\]
The scalar classification in [[witten-darboux|the Witten--Darboux theorem]] now applies channel by channel. Global smoothness excludes \(\lambda<0\). For \(\lambda=0\), it forces \(W=0\), which has no nonzero square-integrable \(A\)-zero mode. For \(\lambda=\nu^2>0\), each channel is
\[
w_j(N)=+\nu,\qquad -\nu,\qquad
\text{or}\quad \nu\tanh\!\left(\nu(N-N_{c,j})\right).
\tag{MF4}
\]
Every other real branch has a finite pole.

The resulting \(W,W'\) are bounded, so \(A,A^*\) have domain \(H^1(\mathbb R;\mathbb C^m)\), and their nonnegative self-adjoint products have domain \(H^2\). For \(\lambda=\nu^2>0\), if \(r\) channels are kinks, then
\[
\dim\ker A=r,\qquad \ker A^*=\{0\},\qquad
\operatorname{ind}(A:H^1\to L^2)=r.
\tag{MF5}
\]
When \(r>0\),
\[
\sigma(A^*A)=\{0\}\cup[\nu^2,\infty).
\tag{MF6}
\]
A nonzero normalizable pointing requires \(r\ge1\); a unique kernel line requires \(r=1\). Neither the existence nor uniqueness of that line fixes \(\nu\).

Thus changing a scalar coefficient into a matrix does not alone produce coupled color dynamics. The scalar partner law itself forbids the desired noncommutation.

## A nonscalar partner admits noncommuting channels

The scalar qualification is essential. Choose
\[
D=\begin{pmatrix}1&0\\0&2\end{pmatrix},\qquad
W_0=\varepsilon\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad 0<\varepsilon<1,
\]
and define
\[
F(N)=\cosh(DN)+D^{-1}\sinh(DN)W_0,\qquad
W(N)=F'(N)F(N)^{-1}.
\tag{MF7}
\]
Here \(\varepsilon\) is a fixed matrix-coupling parameter, not a stochastic perturbation. The factorization
\[
F(N)=\cosh(DN)\left[I+D^{-1}\tanh(DN)W_0\right]
\]
and \(\|D^{-1}\tanh(DN)W_0\|\le\varepsilon<1\) prove invertibility for all real \(N\). Since \(F''=D^2F\),
\[
W'=D^2-W^2,\qquad W(0)=W_0.
\]
Hermitian matrices are preserved by this Riccati equation; uniqueness therefore proves \(W=W^*\). It follows that
\[
AA^*=-\partial_N^2+D^2,
\quad\text{but}\quad
[W(0),W'(0)]=[W_0,D^2]\ne0.
\tag{MF8}
\]
This is a genuinely noncommuting, globally smooth homogeneous-partner example.

The inverse \(F^{-1}\) decays at least as \(e^{-|N|}\). More explicitly, with \(C_N=\cosh(DN)\) and \(B_N=I+D^{-1}\tanh(DN)W_0\),
\[
W=D\tanh(DN)+C_N^{-1}W_0B_N^{-1}C_N^{-1},
\qquad
\|W\|\le2+\frac{\varepsilon}{1-\varepsilon}.
\]
The Riccati equation then bounds \(W'\), so the standard \(H^1/H^2\) domains apply. The two columns of \(F^{-*}\) span \(\ker A\): differentiating \(F^{-*}\) gives \((F^{-*})'=-WF^{-*}\). Both columns are square-integrable. The partner has spectrum \([1,\infty)\); polar decomposition transfers its nonzero spectrum to \(A^*A\), giving
\[
\sigma(A^*A)=\{0\}\cup[1,\infty),\qquad \dim\ker A=2.
\tag{MF9}
\]
The bound is real mathematics, but the two positive entries of \(D\) were chosen. This example does not derive a universal matrix stiffness or a unique vacuum.

## One pointed channel does not control every channel

A still simpler nonscalar partner shows the missing hypothesis:
\[
W(N)=
\begin{pmatrix}
\nu\tanh(\nu N)&0\\0&0
\end{pmatrix},
\qquad
AA^*=-\partial_N^2+
\begin{pmatrix}\nu^2&0\\0&0\end{pmatrix}.
\tag{MF10}
\]
There is exactly one normalizable \(A\)-zero mode, in the first channel. The second channel is the free Laplacian and has continuous spectrum down to zero. Consequently \(A^*A\) has no positive lower edge on the complement of its kernel.

The generalization must therefore control **all** admitted directions, not merely exhibit one pointed state. An irreducible gluing law, a positive matrix lower bound derived upstream, or another quantitative coverage theorem would be new input.

## Which rigidity could matter physically

[[causal-scale-theory/theorems/rigid-sech-response-identities|CST's rigid-sech identities]] start from a stipulated positive density and a separate conservation equation. They constrain the resulting equation of state; they do not select the density. The flat-partner law instead constrains a differential operator strongly enough to select its profile, but remains a law on the declared \(N\)-carrier.

Neither result identifies \(N\) with proper time or its eigenvalues with mass. A physical extension must determine the partner, its allowed matrix or field directions, an independently normalized state norm, and a comparison with physical energy. [[hessian-response-geometry/relative-response-spectrum|Relative response geometry]] prevents a change of metric from supplying a bound by definition.

[[contemporary-puzzles/yang-mills-mass-gap/receipts/positivity_rigidity_audit_receipt.py|The audit receipt]] tests the nonscalar construction and a closing-gap sequence in the unpointed free channel. The simultaneous-diagonalization and spectral statements above are analytic proofs, not consequences of sampling.
