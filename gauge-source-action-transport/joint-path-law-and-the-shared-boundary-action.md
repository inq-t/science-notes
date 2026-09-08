# Joint Path Law and the Shared Boundary Action

Two heat paths sharing a reference cannot admit independent right boundary actions within the declared deterministic finite-energy family. Their joint quadratic variation forces a common right control; violating it makes the joint laws singular, although each loop marginal permits its own transformation. The compatible action family survives a change of reference edge and every bounded positive interaction tilt.

**Status: exact admissibility classification within the stated transformation family on complete based paths.** The graph, positive heat speeds, group, metric and two-sided action ansatz remain inputs. The parameter indexing these heat paths is not identified with physical time, and no ontic randomness is assumed.

## The two loop paths retain a common reference

Let \(G\) be compact and connected with nonzero semisimple Lie
algebra, dimension \(d\), and bi-invariant metric \(Q\).
On \([0,T]\), take independent based heat paths \(a,b,c\), with
generators \(c_a\Delta_Q,c_b\Delta_Q,c_c\Delta_Q\), where all
three speeds are strictly positive. The complete readout is
\[
x=ba^{-1},\qquad y=ca^{-1},\qquad
\mu=\operatorname{Law}(x,y).
\tag{JP1}
\]
These are the path versions of
[[gauge-cycle-innovation-filtration/loop-coordinates-and-the-induced-clock|the theta-graph tree coordinates]].
Write \(\mathcal A,\mathcal B,\mathcal C\) for their unnormalized
right stochastic logarithms, for example
\(d\mathcal A=\circ da\,a^{-1}\).
Their independent quadratic-variation rates are \(2c_aI\),
\(2c_bI\), \(2c_cI\). Product differentiation gives
\[
d\mathcal X=d\mathcal B-\operatorname{Ad}_x d\mathcal A,\qquad
d\mathcal Y=d\mathcal C-\operatorname{Ad}_y d\mathcal A.
\]
Consequently the joint path law carries the covariance identity
\[
\boxed{
\frac{d}{dt}
\begin{pmatrix}
[\mathcal X]&[\mathcal X,\mathcal Y]\\
[\mathcal Y,\mathcal X]&[\mathcal Y]
\end{pmatrix}
=2\begin{pmatrix}
(c_a+c_b)I&c_a\operatorname{Ad}_{xy^{-1}}\\
c_a\operatorname{Ad}_{yx^{-1}}&(c_a+c_c)I
\end{pmatrix}.
}
\tag{JP2}
\]
Each individual path is an ordinary heat path. Their mixed
covariance, absent from the two separate marginal descriptions,
retains the reference they share.

## Admissibility forces the right controls to agree

Let \(p,q,r,s\) be deterministic absolutely continuous based
\(G\)-paths with square-integrable logarithmic velocities.
Consider the proposed transformation
\[
\mathcal T(x,y)=(x',y')
=(pxr^{-1},qys^{-1}).
\tag{JP3}
\]
Its controls have finite variation, so its actual martingale
cross-covariance rate is
\[
2c_a\operatorname{Ad}_{p x y^{-1}q^{-1}}.
\]
The native identity (JP2), evaluated on the transformed paths,
would require instead
\[
2c_a\operatorname{Ad}_{x'(y')^{-1}}
=2c_a\operatorname{Ad}_{p x r^{-1}s y^{-1}q^{-1}}.
\]
They agree exactly when \(r^{-1}s\in Z(G)\).

A scalar path witness proves singularity without any concern
about cancellation between covariance components. For a group
semimartingale \(z\), let
\(\mathcal Q_T(z)=\operatorname{tr}[\int\circ dz\,z^{-1}]_T\).
This is its metric quadratic-variation trace, not a drift or
relative entropy. A common measurable version can be obtained
from \(Q_n(z)=\sum_i d_Q(z_{t_i},z_{t_{i+1}})^2\) on deterministic
partitions with mesh tending to zero. These sums converge in
probability to the trace under each of the two semimartingale
laws below. Choose one deterministic subsequence converging
almost surely under both laws; its limit defines a common Borel
path statistic. This is enough for the separating event, without
asserting one universal pathwise version for every possible law.

Originally \(z=xy^{-1}=bc^{-1}\), so
\(\mathcal Q_T(z)=2(c_b+c_c)dT\) almost surely.
Set \(h=r^{-1}s\). The transformed relative path is
\[
z'=x'(y')^{-1}=p\,b(a^{-1}ha)c^{-1}q^{-1}.
\]
In its right logarithm the coefficient of the \(a\)-noise is
\(\operatorname{Ad}_{pba^{-1}}(\operatorname{Ad}_h-I)\).
The \(b\)- and \(c\)-coefficients are orthogonal adjoint rotations;
their driving martingales are independent. Thus
\[
\boxed{
\mathcal Q_T(z')
=2(c_b+c_c)dT+
2c_a\int_0^T\|\operatorname{Ad}_{h_t}-I\|_{\rm HS}^2\,dt.
}
\tag{JP4}
\]
The extra term is deterministic and strictly positive if \(h\)
is noncentral on a positive-measure set. The two path laws then
occupy disjoint full-measure events. They are mutually singular,
and \(D(\mathcal T_*\mu\Vert\mu)=+\infty\). In particular no
quasi-invariant source lift can realize this output transformation:
pushforward would preserve absolute continuity.

The center of connected compact semisimple \(G\) is finite.
Since the controls are continuous and based, the condition that
\(r^{-1}s\) remain central forces \(r=s\). Conversely, when
\(r=s\), the explicit native lift is
\[
(a,b,c)\longmapsto(ra,pb,qc).
\tag{JP5}
\]
The deterministic path-shift theorem in
[[gauge-path-fisher-response/path-shift-fisher-geometry-before-gauge-projection|path-shift Fisher geometry]]
proves equivalence of the source laws, and data processing gives
\[
D(\mathcal T_*\mu\Vert\mu)
\le\frac14\int_0^T
\left(
\frac{|r^{-1}\dot r|_Q^2}{c_a}
+\frac{|p^{-1}\dot p|_Q^2}{c_b}
+\frac{|q^{-1}\dot q|_Q^2}{c_c}
\right)dt<\infty.
\tag{JP6}
\]
Inverse controls supply equivalence in the other direction.
Therefore, within (JP3), finite-entropy admissibility is
**equivalent** to the shared-right condition.

Each loop marginal alone admits its deterministic two-sided
shift; there is no analogous shared-reference constraint on one
marginal. Equation (JP4) is a whole-to-part compatibility
obstruction, not failure of an individual loop model.
Its event is invariant under common constant conjugation, so
discarding only that common gauge frame does not hide the
quadratic-variation discrepancy.

## The selected family survives a change of tree

Choose \(b\) rather than \(a\) as the reference. The loop
coordinates become \(u=x^{-1}\), \(v=yx^{-1}\). With the now
required shared \(r\), the transformed coordinates obey
\[
u'=r\,u\,p^{-1},\qquad v'=q\,v\,p^{-1}.
\tag{JP7}
\]
This has exactly the same admissible form, with \(p\) as the
common right control. The raw control labels are permuted with
the reference edge. Necessity was established from the path
law before this covariance calculation; it was not manufactured
by defining the second family as a conjugate of the first.

For \(n\ge2\) paths \(x_i=b_i a^{-1}\) sharing the same positive-speed
reference, applying (JP4) to each pair forces all their right
controls to coincide. Independent left controls remain allowed.
The result is independent of the numerical values of the
positive speeds, but fails when the shared speed is zero.
For abelian \(G\), the adjoint obstruction vanishes; the
semisimple conclusion must not be exported to that case.

The earlier test using only left shifts in two tree charts
already has a simpler answer. Holding \(a\) fixed, left shifts
of \(x,y\) are native left shifts of \(b,c\). Holding \(b\) fixed,
left shifts of \(u,v\) are native left shifts of \(a,c\).
Together they are just the existing native family on all three
raw edges. If their infinitesimal chart controls are
\((h_x,h_y,h_u,h_v)\), the actual source Fisher is
\[
g=\frac12\int_0^T
\left(
\frac{|\dot h_u|^2}{c_a}
+\frac{|\dot h_x|^2}{c_b}
+\frac{|\dot h_y+\dot h_v|^2}{c_c}
\right)dt.
\tag{JP8}
\]
The duplicated \(c\)-directions have their actual cross term.
Their difference is a presentation redundancy acting trivially,
not an extra clock or a new physical radical.

## Why a seemingly harmless source lift can fail

Even for just \((a,b)\), holding \(a\) fixed while requesting
\(x=ba^{-1}\mapsto xk\) would require
\(b'=bK\), \(K=a^{-1}ka\).
This multiplier depends on a Brownian path, not merely on a
deterministic finite-energy control.
With left logarithms \(\mathcal A_L,\mathcal B_L\), the actual
product rule is
\[
d\mathcal B'_L
=\operatorname{Ad}_{K^{-1}}d\mathcal B_L
 +(I-\operatorname{Ad}_{K^{-1}})d\mathcal A_L
 +\operatorname{Ad}_{a^{-1}}(k^{-1}\dot k)\,dt.
\tag{JP9}
\]
Hence the \(b'\) marginal itself has extra quadratic-variation
trace \(2c_a\int\|I-\operatorname{Ad}_{k^{-1}}\|_{\rm HS}^2dt\).
For \(SU(2)\), \(Q=-2\operatorname{Tr}\), \(k_t=e^{\omega tT_3}\),
this addition is
\[
8c_a\left(T-\frac{\sin(\omega T)}{\omega}\right)>0
\quad(\omega\ne0).
\tag{JP10}
\]
The requested one-loop output shift has an admissible alternative
lift \(a\mapsto k^{-1}a,b\mapsto b\). The fixed-tree lift fails
because it changes noise covariance. For two loops, using this
alternative also moves \(y\mapsto yk\), exactly as (JP3)--(JP6)
require. Admissibility of a readout operation does not justify
every proposed lift of it.

## Interaction does not remove the compatibility condition

Let \(V\) be a smooth finite-evaluation function on compact
\(G^{2n}\), and let \(\lambda\) be finite. The cylinder density
\(\rho=Z^{-1}e^{-\lambda V(x,y)}\), bounded above and away from
zero, leaves the full-measure
quadratic-variation events unchanged. Thus the necessity in
(JP4) survives every such tilt. The native lift (JP5) also
remains quasi-invariant with finite entropy: its likelihood
is the old path likelihood times a bounded density ratio, and
bounded reweighting preserves integrability of the Gaussian
log-likelihood. For the invariant endpoint construction, keep
\(V\) gauge invariant so its vertex radical remains unchanged.

This does not identify marginal Fisher with retained-source
Fisher. Keeping the raw source and Haar vertex actions permits
the same finite Gauss carrier and
[[gauge-graph-source-response/loop-correlations-and-the-source-response|tilted-source coercivity argument]].
This does not equate the tilted Fisher tensors of a single-path
source and a two-factor-per-edge source: their likelihoods and
allowed actions remain part of the experiment.
Dualizing the marginal scores instead is a different experiment.
Nor does admissibility select \(V\): all such smooth
finite-evaluation tilts retain the same compatibility class.

The contribution to the
[[gauge-source-action-transport/source-action-transport-through-ordered-cuts|source-comparison programme]]
is a genuine restriction on the action ansatz, forced by the
joint law. Covariance matching is necessary for more general
adapted actions but is not by itself sufficient for
quasi-invariance or finite entropy. A broader classification
needs its actual likelihood theorem. The supplied diffusion
geometry, interaction selection, and Yang--Mills reconstruction
remain separate obligations.

[[gauge-path-fisher-response/receipts/two_sided_fisher_receipt.py|The source receipt]] checks
the noise Jacobians by actual Pauli-matrix derivatives in both
logarithmic frames, the full theta covariance, shared and
incompatible right controls, and the extra variation in
(JP10) by refined quadrature. These finite checks support the
algebra; (JP4)--(JP6) supply the path-law classification.
