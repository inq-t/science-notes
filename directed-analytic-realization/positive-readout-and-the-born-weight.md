# Positive Readout and the Born Weight

Positive normalized linear evaluation on the returned compact transition algebra has exactly the density-operator trace form. Its pure evaluations assign squared-overlap weights, computable directly from the preparation kernel. A finite family of preparations also constructs a normalized finite readout through its frame operator. These are interpretation-neutral model-to-readout results under explicit algebraic assumptions, not a derivation of those assumptions, a selected outcome, or a mass gap.

## What the readout operates on

The [[preparation-overlaps-and-the-transition-algebra|preparation construction]]
returns a complex Hilbert carrier \(\mathcal K\ne0\) and its compact
transition algebra \(\mathfrak T=\mathcal K(\mathcal K)\).
An evaluation here means a bounded complex-linear functional
\[
\omega:\mathfrak T\longrightarrow\mathbb C,
\qquad \omega(T^*T)\ge0,\qquad \|\omega\|=1.
\tag{BR1}
\]
It assigns real numbers to self-adjoint tests. Positivity, linearity and
normalization are declared compatibility requirements on the readout,
not conclusions from the words *descent* or *forgetting*.
In infinite dimension the compact algebra has no identity, so (BR1)
does not impose an internal equation \(\omega(I)=1\).

The broad search for a model-to-observation map does not presuppose
probabilistic, Everettian or deterministic ontology. *Born form* below
names a particular mathematical evaluation law. The
[[program-core/operation-registers|operation ledger]] separates such a
law from the preparation, choice of test, obtained value and record.
An explanation of a useful readout law need not first settle how an
obtained value is interpreted.

## Positive linear evaluation fixes the trace form

Write \(\theta_{v,u}=|v\rangle\langle u|\), with the inner product
conjugate-linear in its first argument. Define
\[
b(u,v)=\omega(\theta_{v,u}).
\tag{BR2}
\]
This is a bounded sesquilinear form, since
\(|b(u,v)|\le\|\omega\|\|u\|\|v\|\), and it is positive because
\(\theta_{v,v}\ge0\). Therefore a unique bounded positive operator
\(\rho\) satisfies
\[
b(u,v)=\langle u,\rho v\rangle.
\tag{BR3}
\]
For every finite orthonormal family \(F\), its projection \(P_F\) is
compact and
\[
\sum_{e\in F}\langle e,\rho e\rangle
=\omega(P_F)\le1.
\tag{BR4}
\]
Taking the supremum over these families shows that \(\rho\) is
trace-class with \(\operatorname{Tr}\rho\le1\). Rank-one coefficients give
\[
\omega(\theta_{v,u})
=\langle u,\rho v\rangle
=\operatorname{Tr}(\rho\theta_{v,u}).
\]
Finite-rank density and boundedness extend this equality to all compact
operators. Moreover,
\(\|T\|\le1\) implies
\(|\operatorname{Tr}(\rho T)|\le\operatorname{Tr}\rho\), whereas the
finite-rank projections in (BR4) approach that trace. Hence
\[
\boxed{
\omega(T)=\operatorname{Tr}(\rho T),\qquad
\rho\ge0,\qquad \operatorname{Tr}\rho=\|\omega\|=1.
}
\tag{BR5}
\]
The matrix coefficients (BR3) prove uniqueness. Conversely every such
\(\rho\) gives (BR1). Finite orthonormal families, rather than an assumed
countable basis, make the argument valid also on a nonseparable carrier.

This is the usual compact-operator state representation, here applied
to an algebra supplied by the preparation construction. It is not a new
version of Gleason's theorem. It holds also in dimension two because
positive linear evaluation on the entire algebra is a stronger input
than additivity on projections alone; compare
[[sufficient-reason/two-species-of-reason|the projection-assignment distinction]].

The trace formula has a unique normal extension
\(\widetilde\omega(A)=\operatorname{Tr}(\rho A)\) to \(B(\mathcal K)\).
Thus an effect \(0\le E\le I\) has
\[
w_\rho(E):=\widetilde\omega(E)\in[0,1],\qquad
w_\rho(I-E)=1-w_\rho(E).
\tag{BR6}
\]
The unrestricted state classification for the compact algebra must not
be transferred to all states of \(B(\mathcal K)\): normality matters
there. Nor does it assert a density operator internal to a Type-III local
factor. Restricting a whole-carrier evaluation to a local algebra is a
different operation.

## Pure evaluation produces squared overlap

The extreme points of (BR1) are exactly the rank-one densities
\(P_\psi=|\psi\rangle\langle\psi|\), \(\|\psi\|=1\).
Indeed a density of rank at least two has a positive eigenvalue
\(0<\lambda<1\), giving a nontrivial decomposition
\(\rho=\lambda P_\psi+(1-\lambda)\rho'\).
Conversely, positivity forces every density in a convex decomposition
of \(P_\psi\) to vanish on \(\psi^\perp\). It must then equal
\(P_\psi\) by normalization.

For a unit probe \(\phi\), the corresponding binary question is the
projection \(P_\phi\), and
\[
\boxed{w_\psi(P_\phi)=|\langle\phi,\psi\rangle|^2.}
\tag{BR7}
\]
The square is fixed by the rank-one operator and the linear evaluation,
not chosen as an independent exponent after computing the overlap.
Purity does not make this evaluation multiplicative: with
\(\psi=e_0\) and the two-dimensional flip \(X\),
\(\omega_\psi(X)=0\) while \(\omega_\psi(X^2)=1\).
[[sufficient-reason/facticity-and-pointing|A pure state and a contextual character]]
therefore have different types.

For the actual preparations
\(x_{s,\xi}=e^{-sH}J\xi\) and
\(R_a=J^*e^{-aH}J\), suppose both selected endpoints are nonzero.
Normalize the first as the state and the second as the probe. Then
\[
\boxed{
w_{s\xi,t\eta}
=\frac{|\langle\eta,R_{s+t}\xi\rangle|^2}
{\langle\xi,R_{2s}\xi\rangle
 \langle\eta,R_{2t}\eta\rangle}.
}
\tag{BR8}
\]
The same positive kernel that fixed transition multiplication now fixes
this real scalar. Cauchy--Schwarz gives \(0\le w_{s\xi,t\eta}\le1\).
Independent nonzero complex rescalings of either endpoint cancel.
No spacetime unit or interpretation of randomness enters this quotient.
Choosing the preparation and tested ray remains an input.

## A finite preparation family supplies a finite readout

Let \(z_1,\ldots,z_N\) be a nonempty family of nonzero finite coherent
linear combinations of preparation vectors. Put
\(F=\operatorname{span}\{z_j\}\) and define on this finite-dimensional
space
\[
S_F=\sum_j|z_j\rangle\langle z_j|\big|_F>0,
\qquad f_j=S_F^{-1/2}z_j.
\tag{BR9}
\]
With \(E_j=|f_j\rangle\langle f_j|\) and
\(E_0=I-P_F\), one has
\[
E_j\ge0,\qquad \sum_{j=0}^N E_j=I.
\tag{BR10}
\]
Thus \(a\mapsto\sum_{j=0}^N a_jE_j\) is a unital positive readout
from the finite commutative algebra \(\mathbb C^{N+1}\) into
\(B(\mathcal K)\). Pulling the normal extension in (BR6) back along it returns
\[
(w_0,\ldots,w_N),\qquad
w_j=\operatorname{Tr}(\rho E_j)\ge0,\qquad
\sum_j w_j=1.
\tag{BR11}
\]
The family need not be orthogonal. The inverse frame operator supplies
normalization from the same overlap geometry, rather than separately
normalizing each ray and incorrectly adding overlapping tests to one.
This construction selects neither the family nor an instrument for its
implementation. A finite list of possible measured values additionally
requires a calibration \(j\mapsto a_j\); the list of weights alone is
not an obtained value.

Admitting every finite coherent preparation combination gives tests
that separate normal states. If \(\rho,\sigma\) agree on all their
normalized rank-one projections, then
\(\langle z,(\rho-\sigma)z\rangle=0\) on a dense linear subspace.
Continuity and polarization give \(\rho=\sigma\).
Mapping a model to its complete readout law therefore need not itself
forget the state. The
[[algebra/depolarizing-return-and-the-classical-record-threshold|informationally complete qubit readout]]
is another explicit witness. State-to-law, information loss, and an
obtained outcome are three distinct questions.

## What has and has not been grounded

The result is conditional but constructive: the returned transition
algebra and positive linear evaluation determine the trace form; pure
evaluation gives (BR8), and a chosen preparation frame gives (BR11).
No additional random source is needed to establish these algebraic
identities. This does not prove that an underlying random source exists
or does not exist.

[[sufficient-reason/noninvertible-presentation-and-apparent-chance|Noninvertible presentation]]
separately shows why inaccessible determining data can coexist with an
accessible readout law, and why noninjectivity alone determines no
weights. Here the substantive remaining questions are why the primitive
kernel is positive, why its compact transitions and positive linear
evaluations are the appropriate observable structure, and what selects
the physical preparations, tests and calibration. Interpretation of an
obtained result is not used as a premise or a prerequisite for this law.

For a clock \(H\ge0\), a zero weight in one state still does not imply
a gap. The operator assertion is
\(E_H((0,\delta))=0\): equivalently every normal state gives that
projection zero weight. A spectrally complete preparation family can
test this assertion by the
[[coarse-response-memory/spectral-readout-and-the-visible-gap|coverage theorem]],
but the readout formula supplies no such exclusion. The
[[two-slice-innovation-geometry/phase-modulus-pointing-and-euclidean-dwell|dwell theorem]]
likewise needs a uniform bound, not just positive weights or a finite
outcome list. Mass identification still needs the physical translation
structure.

[[positive_readout_receipt.py|The positive-readout receipt]] and
[[positive-readout-receipt-output.txt|its output]] check finite exact
matrix and preparation examples. The infinite-dimensional trace
representation and density arguments above have proofs, not numerical
certificates.
