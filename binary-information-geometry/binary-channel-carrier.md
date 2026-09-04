# The Binary Channel as a Carrier Test

On the balanced binary algebra, every state-preserving channel is controlled
by one scalar \(r\in[-1,1]\). Its GNS defect is \(1-r\), while its BKM
data-processing loss is \(1-r^2\). The reversible flip \(r=-1\) therefore
has zero information loss but maximal disagreement from the identity. This
finite theorem separates a categorical distinction operator from a
forgetting Hessian and shows why one binary probe cannot control an
infinite-dimensional physical vacuum carrier.

## The balanced algebra and its GNS tangent

Let

\[
\mathcal B
=
\operatorname{span}\{\mathbf1,Q\}
\cong
\mathbb C^2,
\qquad
Q=Q^*,
\qquad
Q^2=\mathbf1,
\]

and let the balanced faithful state obey

\[
\omega_0(Q)=0.
\]

In the GNS representation,

\[
\mathcal H_{\omega_0}
=
\mathbb C\Omega_0
\oplus
\mathbb C Q\Omega_0,
\qquad
\|Q\Omega_0\|^2=1.
\tag{BC1}
\]

Along [[balanced-exponential-family|the balanced exponential family]], put

\[
m_\theta:=\tanh\theta,
\qquad
s_\theta:=Q-m_\theta\mathbf1.
\]

Then

\[
\boxed{
g^{\mathrm{bin}}_{\theta\theta}
=
\operatorname{Var}_{\rho_\theta}(Q)
=
\|s_\theta\Omega_\theta\|^2
=
\operatorname{sech}^2\theta.}
\tag{BC2}
\]

Under the logarithmic-score identification, the real binary Fisher tangent
is represented isometrically by the centered GNS line
\(\mathbb R\,s_\theta\Omega_\theta\); at \(\theta=0\), this is
\(\mathbb R\,Q\Omega_0\). The state tangent and GNS vector remain different
carrier types despite this one-dimensional identification, as emphasized in
[[measured-response-carriers/inq|measured response carriers]]. Neither is the
whole GNS vacuum complement of any larger theory.

## Classification of balanced channels

A unital completely positive map
\(\Phi:\mathcal B\to\mathcal B\) is a Markov map on two points.
Preservation of the balanced state makes its stochastic matrix doubly
stochastic. Therefore there is a unique \(r\in[-1,1]\) such that

\[
\boxed{
\Phi_r(\mathbf1)=\mathbf1,
\qquad
\Phi_r(Q)=rQ.}
\tag{BC3}
\]

Conversely, every \(r\in[-1,1]\) defines such a channel. It is
\(\omega_0\)-symmetric, and its GNS implementation is

\[
V_r
=
P_{\Omega_0}
+r(I-P_{\Omega_0}).
\tag{BC4}
\]

Consequently, on the centered line,

\[
\boxed{
(I-V_r)|_{\Omega_0^\perp}
=(1-r)I.}
\tag{BC5}
\]

This is the exact one-dimensional GNS distinction edge.

## GNS disagreement is not information loss

The induced state-tangent map at the balanced state multiplies the real
one-dimensional binary tangent by \(r\). Hence, for every tangent \(X\) on
that line, the quadratic BKM data-processing loss is

\[
\boxed{
\mathcal Q_{\Phi_r,\omega_0}^{\mathrm{BKM}}[X]
=
(1-r^2)g_{\omega_0}^{\mathrm{BKM}}(X,X).}
\tag{BC6}
\]

Equations (BC5) and (BC6) are different:

\[
1-r^2=(1+r)(1-r).
\tag{BC7}
\]

At \(r=-1\), \(\Phi_{-1}\) exchanges the two points. It is a reversible
\(*\)-automorphism, so its BKM information loss vanishes, but

\[
(I-V_{-1})|_{\Omega_0^\perp}=2I.
\]

Hence

\[
\boxed{
\text{distance from the identity}
\ne
\text{irreversible forgetting}.}
\tag{BC8}
\]

This is not a merely verbal distinction. A categorical Kazhdan form built
from \(I-V\) measures failure to be invariant under selected generators.
A relative-entropy contraction defect measures information lost by a
channel. One can compare them only after the operation and carrier have been
chosen so that such a comparison is true.

## Lazification

The lazy channel

\[
\Psi_r:=\frac{\operatorname{id}+\Phi_r}{2}
\]

acts on the centered line by

\[
b:=\frac{1+r}{2}\in[0,1].
\]

Its two defects satisfy

\[
\left.(I-V_{\Psi_r})\right|_{\Omega_0^\perp}
=(1-b)I_{\Omega_0^\perp},
\qquad
\mathcal Q_{\Psi_r,\omega_0}^{\mathrm{BKM}}[X]
=(1-b^2)g_{\omega_0}^{\mathrm{BKM}}(X,X)
=(1+b)(1-b)g_{\omega_0}^{\mathrm{BKM}}(X,X),
\tag{BC9}
\]

where the first identity is on the centered GNS line and the second is on
the corresponding real binary state-tangent line.

Therefore, on that state-tangent line,

\[
(1-b)g_{\omega_0}^{\mathrm{BKM}}(X,X)
\leq
\mathcal Q_{\Psi_r,\omega_0}^{\mathrm{BKM}}[X]
\leq
2(1-b)g_{\omega_0}^{\mathrm{BKM}}(X,X).
\tag{BC10}
\]

Lazification makes the GNS implementation positive and makes the two
defects comparable in this binary model. It changes the operation and does
not supply a physical duration, a regional entropy theorem, or a clock
Hamiltonian.

## Fusion specialization

Suppose channels are indexed by simple objects of a rigid tensor category
and obey the normalized fusion law. On this binary carrier their parameters
must satisfy

\[
r_\alpha r_\beta
=
\sum_\gamma
\frac{N_{\alpha\beta}^{\ \ \gamma}d(\gamma)}
{d(\alpha)d(\beta)}
r_\gamma.
\tag{BC11}
\]

Equivalently, \(\alpha\mapsto d(\alpha)r_\alpha\) is a scalar
representation of the fusion algebra. Full annular or tube admissibility is
still an additional condition; the scalar relation does not prove it.

## The finite-rank firewall

One balanced binary probe sees only the real line
\(\mathbb R\,Q\Omega_0\). Any analysis map from an
infinite-dimensional physical vacuum complement into finitely many such
lines has an infinite-dimensional kernel. Therefore no finite binary family
can obey a positive lower-frame inequality on the complete carrier.

A physical use requires an infinite or direct-integral family of
equivariant binary readouts, joint kernel exactly the vacuum, a uniform
lower frame, compatibility with the proposed fusion action, and a
same-tangent energy comparison. The general carrier types and these
obligations are recorded in
[[measured-response-carriers/inq|measured response carriers]].
