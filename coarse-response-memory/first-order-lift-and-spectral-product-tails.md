# A First-Order Lift Controls Spectral Product Tails

A fixed smooth observable has controlled spectral leakage under the actual interacting ground-state operator, even when its product channels violate a sharp energy triangle. Factoring the supplied weighted Laplacian through the gradient yields a bounded first-order commutator. It controls a quadratic square-root-energy row and, by a separate argument, an operator norm between separated spectral windows. The constants require the observable's gradient, not an interacting gap or a favorable vacuum Hessian.

**Status: [EXACT] for the declared compact weighted diffusion; the operator-window argument also applies to the stated noncompact free control.** The first-order enlargement is an auxiliary factorization of a supplied operator, not a physical Dirac equation, a fermion postulate, or a derivation of the metric. These quadratic and operator bounds are not the absolute product moments required by the connected assembly theorem.

## Preserve the actual weighted carrier

Let \(M\) be a connected compact Riemannian manifold without boundary,
with a smooth strictly positive probability density
\(d\nu=\psi^2\,d\mathrm{vol}\). Fix \(\kappa>0\). The intended block
example is the full raw configuration space of a finite Wilson
Hamiltonian
\[
H=-\kappa\Delta+V,\qquad H\psi=E_0\psi,
\]
including boundary-charged functions. Its positive Doob operator is
\[
K=\psi^{-1}(H-E_0)\psi
=-\kappa(\Delta+2\nabla\log\psi\cdot\nabla).
\tag{FT1}
\]
The change of measure and adjoint are the actual
[[interacting-reference-and-spectral-product-control|interacting reference]],
not a replacement of its state by Haar measure.

Complexify the two Hilbert spaces
\[
\mathcal H_0=L^2(M,\nu),\qquad
\mathcal H_1=L^2(M,\nu;T^*M).
\]
Let \(d:\mathcal H_0\to\mathcal H_1\) be the closure of
\(\sqrt\kappa\,\nabla\) on smooth functions. It is densely defined
and closed, with domain \(H^1(M,\nu)\). Its adjoint \(d^*\) is the
weighted divergence operator on the domain of one-forms whose weak
weighted divergence lies in \(L^2\). Then
\[
d^*d=K,\qquad
\mathscr D=
\begin{pmatrix}0&d^*\\d&0\end{pmatrix},
\qquad
D(\mathscr D)=D(d)\oplus D(d^*).
\tag{FT2}
\]
The block operator \(\mathscr D\) is self-adjoint. Indeed the
standard closed-operator factorization has
\(\mathscr D^2=\operatorname{diag}(d^*d,dd^*)\), with both diagonal
operators positive self-adjoint; the resolvents of
\(\mathscr D\pm i\) follow from
\((\mathscr D\mp i)(\mathscr D^2+1)^{-1}\).
In particular the scalar square is exactly the supplied \(K\).
The one-form sector can have an infinite-dimensional zero kernel
\(\ker d^*\). No compact resolvent for \(\mathscr D\) is asserted.

For \(q\in C^\infty(M,\mathbb C)\), use multiplication by \(q\) on
both summands, denoted \(\mathsf M_q\). Put
\[
G=\|\nabla q\|_\infty,\qquad Q_0=\|q\|_\infty,\qquad
c_qf=\sqrt\kappa\,f\,\nabla q.
\]
The metric identifies the gradient with its one-form.
The product rules are
\[
d(qf)=q\,df+c_qf,\qquad
d^*(q\omega)=q\,d^*\omega-c_{\bar q}^*\omega.
\tag{FT3}
\]
They also prove that smooth multiplication preserves both domains.
Consequently
\[
\boxed{
[\mathscr D,\mathsf M_q]
=\begin{pmatrix}0&-c_{\bar q}^*\\c_q&0\end{pmatrix},
\qquad
\|[\mathscr D,\mathsf M_q]\|=\sqrt\kappa\,G.
}
\tag{FT4}
\]
The conjugate in the upper-right entry is necessary for complex
\(q\). The drift in \(d^*\) introduces no extra commutator term:
its zeroth-order multiplication commutes with \(q\).

The same product rule gives a useful domain estimate, for \(s>0\):
\[
\|d\,M_q(K+s)^{-1/2}\|
\le\sqrt{Q_0^2+\kappa G^2/s}.
\tag{FT5}
\]
Apply Cauchy--Schwarz to
\(Q_0\|df\|+\sqrt\kappa G\|f\|\), using
\(\|(K+s)^{1/2}f\|^2=\|df\|^2+s\|f\|^2\).
No counting of eigenvectors or eigenvalue multiplicities enters.

## An all-input-energy quadratic row

Choose any orthonormal scalar eigenbasis
\[
K\phi_i=\epsilon_i\phi_i,\qquad
\phi_0=1,\quad \epsilon_0=0,\qquad
r_i=\sqrt{\epsilon_i},\qquad
q_{ki}=\langle\phi_k,q\phi_i\rangle_\nu.
\tag{FT6}
\]
Compact ellipticity makes this basis complete, and connectedness
makes the zero scalar eigenvalue simple. The basis may be complex.
For every input \(i\),
\[
\boxed{
\sum_k(r_k-r_i)^2|q_{ki}|^2\le2\kappa G^2.
}
\tag{FT7}
\]
The sum runs over the complete raw scalar spectrum. In particular
there is no high-input-energy restriction and no finite cutoff.

To prove it for \(i>0\), set
\[
\eta_i=d\phi_i/r_i,\qquad
v_i^\pm=\frac1{\sqrt2}(\phi_i,\pm\eta_i).
\]
The \(\eta_i\) form an orthonormal basis of
\(\overline{\operatorname{Ran}d}\), and
\(\mathscr Dv_i^\pm=\pm r_i v_i^\pm\).
Together with the scalar zero vector \((\phi_0,0)\) and
\(\{0\}\oplus\ker d^*\), these give the spectral decomposition
needed below. Define \(a_{ki}=\langle\eta_k,q\eta_i\rangle\) for
\(k>0\). Directly,
\[
\langle v_k^\pm,\mathsf M_qv_i^+\rangle
=\frac{q_{ki}\pm a_{ki}}2.
\]
Since \(\mathsf M_qv_i^+\in D(\mathscr D)\), Parseval applied to
\((\mathscr D-r_i)\mathsf M_qv_i^+\) gives
\[
\begin{aligned}
\|[\mathscr D,\mathsf M_q]v_i^+\|^2
={}&\frac14\sum_{k>0}
\left[(r_k-r_i)^2|q_{ki}+a_{ki}|^2
 +(r_k+r_i)^2|q_{ki}-a_{ki}|^2\right]\\
&+\frac{r_i^2}{2}|q_{0i}|^2
 +\frac{r_i^2}{2}
   \|P_{\ker d^*}(q\eta_i)\|^2.
\end{aligned}
\tag{FT8}
\]
The last term retains the possibly infinite one-form zero eigenspace;
it is nonnegative, not set to zero. Because
\((r_k+r_i)^2\ge(r_k-r_i)^2\) and
\(|z+w|^2+|z-w|^2=2(|z|^2+|w|^2)\), the right side is at least
\(\tfrac12\sum_{k\ge0}(r_k-r_i)^2|q_{ki}|^2\).
Equation (FT4) proves (FT7).

For \(i=0\), no division by \(r_i\) is used. Instead
\[
\sum_k\epsilon_k|q_{k0}|^2
=\|dq\|_{\mathcal H_1}^2
=\kappa\int|\nabla q|^2\,d\nu
\le\kappa G^2,
\tag{FT9}
\]
This is the sharper exact vacuum-input identity, with \(d\) the
scaled closed derivative from (FT2).

Thus, for any \(R>0\),
\[
\sum_{k:\,|r_k-r_i|\ge R}|q_{ki}|^2
\le\min\!\left(Q_0^2,\frac{2\kappa G^2}{R^2}\right).
\tag{FT10}
\]
This controls both upward and downward leakage. It permits
nonzero channels beyond a sharp spectral triangle; it bounds
their aggregate quadratic weight instead of deleting them.

## A separate bound on whole spectral windows

Individual row estimates do not by themselves bound the operator
on a degenerate energy window. There is a separate,
basis-independent result:
\[
\boxed{
\left\|
1_{[(\sqrt E+R)^2,\infty)}(K)\,
M_q\,1_{[0,E]}(K)
\right\|
\le\min\!\left(Q_0,\frac{\sqrt{2\kappa}\,G}{R}\right),
\quad E\ge0,\ R>0.
}
\tag{FT11}
\]

Let \(r=\sqrt E\), and work first on the enlarged carrier.
Write \(P_{\rm lo}=1_{[-r,r]}(\mathscr D)\) and
\(P_+=1_{[r+R,\infty)}(\mathscr D)\). For
\(X_+=P_+\mathsf M_qP_{\rm lo}\), the Sylvester relation is
\[
A X_+-X_+B=T_+,\qquad
A=\mathscr D|_{\operatorname{Ran}P_+}\ge r+R,\quad
B=\mathscr D|_{\operatorname{Ran}P_{\rm lo}},\quad
\|B\|\le r,
\]
where \(T_+=P_+[\mathscr D,\mathsf M_q]P_{\rm lo}\).
The source window is contained in \(D(\mathscr D)\);
smooth multiplication preserves that domain. The separated
spectra therefore give the convergent integral
\[
X_+=\int_0^\infty
e^{-t(A-r)}T_+e^{t(B-r)}\,dt,\qquad
\|X_+\|\le\frac{\sqrt\kappa G}{R}.
\tag{FT12}
\]
One can verify the identity by differentiating
\(e^{-t(A-r)}X_+e^{t(B-r)}\); its norm tends to zero.
This also justifies the relation with the unbounded output
operator \(A\).

For \(P_-=1_{(-\infty,-r-R]}(\mathscr D)\), apply the same
argument to \(-\mathscr D\). Both branches have the same bound,
and their output ranges are orthogonal, so
\[
\|1_{[r+R,\infty)}(|\mathscr D|)
       \mathsf M_qP_{\rm lo}\|
\le\frac{\sqrt{2\kappa}G}{R}.
\]
Finally the scalar embedding \(Jf=(f,0)\) intertwines
\(|\mathscr D|\) with \(\sqrt K\), and multiplication respects
that embedding. Compressing this last inequality by \(J^*,J\)
proves (FT11). It neither sums individual row bounds nor
introduces a factor counting the window's multiplicity.

## Charged Wilson coefficients have explicit constants

On a raw \(SU(2)\) block with \(Q=-2\operatorname{Tr}\), let \(q\)
be a matrix coefficient of an open holonomy word with \(r\)
distinct links and fixed unit spinors at its ends. The same
estimates apply to a product of fundamental matrix entries on
distinct links, as occurs when expanding a crossing plaquette.
Inverse orientations are allowed. Then
\[
\|q\|_\infty\le1,\qquad
\|\nabla q\|_\infty^2\le r/2.
\tag{FT13}
\]
For one differentiated factor use \(T_a=-i\sigma_a/2\).
For unit spinors \(v,w\), the Pauli identity gives
\[
\sum_{a=1}^3|v^*T_aw|^2
=\frac{2-|v^*w|^2}{4}\le\frac12.
\]
The other word factors are unitary and merely change these
spinors or rotate the generator basis. Sum over the \(r\)
distinct links. For an entry product, undifferentiated entries
have modulus at most one, giving the same upper bound.

Consequently, on the actual full interacting block and at
every internal coupling,
\[
\sum_k(\sqrt{\epsilon_k}-\sqrt{\epsilon_i})^2|q_{ki}|^2
\le\kappa r,\qquad
\left\|P_{\ge(\sqrt E+R)^2}M_qP_{\le E}\right\|
\le\min(1,\sqrt{\kappa r}/R).
\tag{FT14}
\]
Neither a bound on \(\nabla\log\psi\) nor a raw-block gap
enters these constants. For a real normalized trace of one such
word, each link contributes \((1-q^2)/4\) to its squared gradient,
giving the improved bound \(G^2\le r/4\).
These are charged observables unless their endpoints and
contractions make them gauge invariant; the proof never
projects away their boundary charge sectors.

## What the bound does not supply

The
[[block-spectral-moments-and-connected-assembly#Squared spectral control does not choose an absolute coefficient basis|absolute spectral row problem]]
remains distinct. On a finite output window \(I\), Cauchy--Schwarz
only gives
\[
\sum_{k\in I}\omega_k|q_{ki}|
\le
\left(\sum_{k\in I}\omega_k^2\right)^{1/2}
\|1_I(K)q\phi_i\|.
\tag{FT15}
\]
The extra weighted channel count is precisely absent from the
quadratic and operator estimates above. An arbitrary two-input
product is also different from multiplication by this fixed
smooth \(q\): \(L^2\times L^2\to L^2\) is not generally bounded.
Thus (FT14) does not verify the four local moments (BM4), or
the connected bilinear estimate, by changing their norm labels.

There is a simple gapless control. On
\(L^2(\mathbb R,dx)\), take \(d=\sqrt\kappa\,\partial_x\) and
\(K=-\kappa\partial_x^2\), whose spectrum is \([0,\infty)\).
For \(q(x)=e^{i\xi x}\), the commutator norm is
\(\sqrt\kappa|\xi|\). The closed-operator and separated-window
proof still applies, although a discrete eigenbasis and
normalizable constant vacuum do not. The same type of tail
bound therefore coexists with no mass gap.

The exact content is a constraint on multiplication and spectral
transfer for one supplied state and kinetic geometry. It supplies
neither a hard spectral fusion rule, a nonzero lower edge, a
nonassociative multiplication, nor an independently selected
physical time parameter.
