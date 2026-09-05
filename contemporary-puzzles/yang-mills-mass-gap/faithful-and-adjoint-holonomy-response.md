# Faithful and Adjoint Holonomy Response

A faithful color probe and an adjoint probe can have exactly the same infinitesimal metric while losing different information globally. Their nonlinear discrepancy is the squared displacement of the normalized fundamental trace. This gives a precise distinction between local response geometry and global holonomy sensitivity, without adding a new stiffness or a physical gap.

**Status: [EXACT REPRESENTATION AND HESSIAN IDENTITIES].** The statements concern functions of group holonomy and their configuration-space Hessians, not the physical translation spectrum.

## Equal local metric, unequal global response

For \(U\in SU(N)\), define
\[
t(U)=\frac{\operatorname{tr}U}{N},\qquad
w(U)=1-\operatorname{Re}t(U).
\tag{FA1}
\]
Conjugation on
\(\operatorname{End}(\mathbb C^N)=\mathbb CI\oplus\mathfrak{sl}_N\)
has character \(|\operatorname{tr}U|^2=1+\chi_{\mathrm{adj}}(U)\).
Normalize the adjoint response to the same identity Hessian:
\[
a(U)=\frac{N^2-1}{2N^2}
\left(1-\frac{\chi_{\mathrm{adj}}(U)}{N^2-1}\right)
=\frac{1-|t(U)|^2}{2}.
\tag{FA2}
\]
The coefficient is \(4/9\) for \(SU(3)\). Direct subtraction gives
\[
\boxed{w(U)=a(U)+\frac12|1-t(U)|^2.}
\tag{FA3}
\]
Equivalently, divide the orthogonal Hilbert--Schmidt decomposition
\[
U-I=(U-tI)+(t-1)I
\]
by \(2N\) after taking squared norms. The traceless displacement contributes \(a\), and the scalar trace displacement contributes the remainder. No additional representation-theoretic conjecture enters.

Since \(|t|\le1\), one has \(0\le a\le w\). But at a nonidentity center element \(U=\zeta I\),
\[
a(\zeta I)=0,\qquad w(\zeta I)=1-\operatorname{Re}\zeta>0.
\tag{FA4}
\]
There is consequently no global bound \(a\ge c\,w\) with \(c>0\). Equality of tangent metrics does not supply global equivalence of nonlinear response.

## The lost distinction first appears beyond quadratic order

For traceless anti-Hermitian \(X\), use
\[
g_N(X,X)=N^{-1}\operatorname{tr}(X^*X).
\]
Then
\[
\operatorname{Hess}_I w(X,X)
=\operatorname{Hess}_I a(X,X)=g_N(X,X),
\tag{FA5}
\]
while
\[
w(e^{sX})-a(e^{sX})
=\frac{s^4}{8N^2}\bigl(\operatorname{tr}X^*X\bigr)^2
+O(s^6).
\tag{FA6}
\]
The quadratic trace displacement is real and the cubic one imaginary, so their degree-five cross term vanishes. The residue is invisible to an identity-Hessian comparison but not to finite holonomy.

More sharply, along a bi-invariant geodesic,
\[
\left.\frac{d^2}{ds^2}w(Ue^{sX})\right|_{s=0}
=-\frac1N\operatorname{ReTr}(UX^2).
\tag{FA7}
\]
At \(U=\zeta I\),
\[
\operatorname{Hess}_{\zeta I}w=(\operatorname{Re}\zeta)g_N,
\qquad
\operatorname{Hess}_{\zeta I}a=g_N.
\tag{FA8}
\]
For the two nontrivial \(SU(3)\) centers, \(w=3/2\) and its Hessian is \(-g_N/2\), whereas the adjoint response vanishes and has positive Hessian \(g_N\).

## What the exceptional construction retains

[[exceptional-normal-holonomy-and-the-residual-gauge-form|The exceptional normal probe]] already gives \(Q_N=288w\) per color plaquette at every holonomy, not merely near identity. Thus (FA3) decomposes the existing faithful response:
\[
Q_N=288a+144|1-t|^2.
\tag{FA9}
\]
It does not add an independently adjustable term, change the kinetic conversion in [[exceptional-wilson-same-carrier-factorization|the same-carrier Wilson factorization]], or turn the trace factor eight into an enhancement of the mass gap.

Replacing the faithful probe by its Hessian-matched adjoint version loses center information. This is not the same statement as [[twisted-holonomy-and-the-neutral-hessian|center neutrality of physical glueball states]]. A fundamental closed Wilson loop is gauge invariant and can distinguish the holonomies in (FA4); an adjoint character cannot. Probe sensitivity and the charge of a physical state have different carriers.

The negative potential Hessian in (FA8) also prevents a global convexity argument based solely on the positive identity metric. It does not imply a gapless interacting law: the full electric operator, vacuum weighting, and configuration-space Ricci term are different ingredients. [[rg-covariance-residue/nonlinear-conditional-gauge-response|The normalized compact conditional bound]] shows explicitly how those Hessian signs enter a valid sufficient estimate.

[[receipts/nonlinear_holonomy_probe_receipt.py|The finite holonomy receipt]] checks the exact decomposition, center values, matching identity Hessians, and quartic remainder for \(SU(2)\), \(SU(3)\), and \(SU(4)\). These checks certify the written finite-dimensional identities, not their missing physical realization.
