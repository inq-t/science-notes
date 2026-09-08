# Pointed Preparation Stability and the Volume Test

Dividing a prepared vector by one positive reference pairing separates its accumulating amplitude from its changing shape. The resulting nonlinear equation can contract errors of an approximate shape even when a bound for the unnormalized evolution grows. This gives a practical full-carrier residual estimate. The same global pointing, however, fails a volume-uniformity test already for independent copies with an unchanged spectral gap: reference overlaps multiply, while local excitations need not soften.

**Status: exact normalized-flow estimate and tensor-product obstruction.**
The reference pairing and original generator are supplied data.
Normalization neither selects a measurement outcome nor derives a
new physical clock or a Yang--Mills vacuum.

## An affine section of a linear evolution

Let a real Banach carrier split as \(\mathbb R\oplus X_Q\), and
consider a linear evolution with block generator
\[
L=\begin{pmatrix}0&b\\c&D\end{pmatrix}.
\tag{PN1}
\]
Assume \(D\) generates a strongly continuous semigroup with
\(\|e^{tD}\|\le e^{-dt}\), \(d>0\), that \(b:X_Q\to\mathbb R\)
is bounded with norm at most \(\beta\), and that \(c\in X_Q\).
On a trajectory \(u=(u_0,u_Q)\) with \(u_0>0\), put
\(g=u_Q/u_0\). The quotient rule gives exactly
\[
g'=c+Dg-b(g)g,\qquad (\log u_0)'=b(g).
\tag{PN2}
\]
Adding a scalar multiple of the identity to \(L\) changes only
the second equation, not the shape equation. This is a change
of normalization, not a reparameterization of time.

For the stability result assume additionally \(b(g(t))\ge0\)
on the actual trajectory. This is a hypothesis to prove from
the preparation; it is not implied by the Banach splitting alone.
Given a differentiable trial \(y\) in the generator domain, define
its full residual
\[
e=y'-c-Dy+b(y)y.
\tag{PN3}
\]
For \(\delta=g-y\), subtraction leaves
\[
\delta'=(D-b(g))\delta-b(\delta)y-e.
\tag{PN4}
\]
The coefficient of the first scalar damping term is that of
the **actual** trajectory. Consequently, if \(\|y(t)\|\le M\)
and \(\alpha=d-\beta M>0\), variation of constants and Gronwall give
\[
\boxed{
\|\delta(t)\|\le e^{-\alpha(t-s)}\|\delta(s)\|
+\int_s^t e^{-\alpha(t-r)}\|e(r)\|\,dr.
}
\tag{PN5}
\]
Only the trial must satisfy the displayed size bound. No hidden
smallness bound on \(g\) has been inserted. Equivalently its
upper right norm derivative is bounded by
\(-\alpha\|\delta\|+\|e\|\). For nonsmooth solutions use the
mild equation and its integral norm inequality; the stated
finite-polynomial trials lie in the required domain.

A uniform residual \(\epsilon\) therefore contributes at most
\(\epsilon/\alpha\), not a growing exponential. A time-weighted
residual \(\|e(t)\|\le Ct^m\), with zero initial error, contributes
at most \(Ct^{m+1}/(m+1)\). At a discontinuity of a piecewise trial,
add its jump norm to the error budget. A small residual without
the correct initial value or jump accounting does not certify
the trajectory.

## The two-plaquette preparation supplies the hypotheses

Use \(\kappa=\lambda=1\), \(L=-K+M\), \(M=a+b\), and the
weighted harmonic norm in
[[certified-ground-marginal-and-late-preparation|the marginal certificate]]
(GC2). Let \(Q\) remove its Haar constant coefficient. Then
\[
D=-K|_Q+QMQ,\qquad c=QM1,\qquad b(g)=(Mg)_{000}.
\tag{PN6}
\]
The free nonconstant semigroup decays at least as \(e^{-3t}\)
blockwise, and \(\|QMQ\|_X\le5/2\). Bounded perturbation
therefore gives \(\|e^{tD}\|_X\le e^{-t/2}\).
The only coefficients contributing to \(b\) are
\[
b(g)=\tfrac12(g_{100}+g_{010}),\qquad
|b(g)|\le\tfrac14\|g\|_X,
\qquad \|c\|_X=2.
\tag{PN7}
\]

The declared harmonic matrix of \(-K+M\) has nonnegative
off-diagonal entries. Each finite harmonic compression thus
preserves nonnegative coefficients. Its full semigroup limit
does too. Starting from \(1\), \(u_0(0)=1\) and
\(u_0'=(Mu)_{000}\ge0\), so \(u_0\ge1\) and
\(b(g)\ge0\). This is positivity in a **specified coefficient
basis**, separate from pointwise positivity and from positivity
of the amplitude as an integral kernel. It is a property of
this operator and preparation, not an axiom about all states.
Bounded perturbation on \(X\) gives its finite-time membership
and the required passage from finite harmonics.

For any trial \(\|y\|_X\le1\), (PN5) now has
\[
\boxed{\alpha=1/4,\qquad
\|g(t)-y(t)\|_X\le e^{-(t-s)/4}\|g(s)-y(s)\|_X
+\int_s^t e^{-(t-r)/4}\|e(r)\|_X\,dr.}
\tag{PN8}
\]
The residual must include \(QM(1+y)\) outside the trial cutoff.
Applying (GC10) to \(1+g\) and \(1+y\) then controls the
actual marginal and its latitude derivatives, including poles.
This joins normalization, the full kinetic blocks, magnetic
multiplication and the readout in one estimate. It does not
replace the readout's memory by an autonomous physical clock.

In particular the certified ground shape has
\(\|Qf\|_X<0.9\), so it is an admissible stationary comparison
in (PN8). Once a trajectory is certified sufficiently close to
that actual ground shape at one finite time, its comparison
error contracts for every later time. An approximate ground
trial still needs its own residual or its certified distance
to the true stationary shape.

## Independent copies defeat a global vacuum-normalized norm

Let \(\phi\) be the unit ground vector of one interacting copy,
\(c_0=\langle1,\phi\rangle\), and \(f=\phi/c_0\).
It is nonconstant, so
\(0<c_0<1\) and \(\|f\|_X>1\). For \(L\) independent copies,
use the product harmonic weights and block Hilbert norms. Exact
factorization gives
\[
\langle1,\phi^{\otimes L}\rangle=c_0^L,\qquad
\|f^{\otimes L}\|_{X_L}=\|f\|_X^L,
\qquad
\|Q_Lf^{\otimes L}\|_{X_L}=\|f\|_X^L-1,
\tag{PN9}
\]
where \(Q_L\) removes only the one total Haar constant.
The block norm of a pure tensor is the product of block norms;
the weighted sums factor. Even without exponential harmonic
weights, \(\|f^{\otimes L}\|_2=\|f\|_2^L\) grows.

Yet the shifted product Hamiltonian
\[
\mathbb H_L=\sum_{j=1}^L(H-E_0)_j
\tag{PN10}
\]
has the same positive spectral gap as a single copy. Each
nonvacuum tensor excitation costs at least that gap, and
exciting just one factor attains it. The diverging comparison
norm thus occurs **without** a closing physical gap, added
interaction between copies, or a continuum subtlety.

This excludes treating the globally pointed bounds above as
volume-uniform estimates merely because their one-copy constants
are small. It does not exclude a uniform gap or every use of a
reference state. Local normalized comparisons stay unchanged
for independent copies; genuinely connected contributions vanish
across those copies.
[[connected-preparation-and-local-normalization|Connected log-preparation]]
makes that cancellation and its nonlinear assembly equation
exact on the same padded kinetic carrier. A scalable extension
must control its local derivative sums and compare them with
the actual conditional response. That is an assembly obligation,
not a consequence of performing more one-copy certificates.
