# The Tangent Bundle of a Hessian Manifold

The tangent bundle of a real Hessian manifold carries a natural integrable complex structure and Kähler metric whose conjugation fixes the zero section. For a three-dimensional Hessian manifold this yields a complex threefold of six real dimensions with a real three-dimensional fixed locus. The construction is exact, but it complexifies an already chosen real response manifold and therefore does not derive physical space from an antecedent \(S^6\).

## Horizontal and vertical splitting

Let \(M\) be a real \(n\)-manifold with affine connection \(\nabla\). At a point \((x,v)\in TM\), the connection gives a splitting

$$
T_{(x,v)}TM
\simeq
T_xM^{\mathrm H}\oplus T_xM^{\mathrm V}.
$$

For \(X,Y\in T_xM\), write the corresponding tangent as \((X,Y)\). Define

$$
J(X,Y)=(-Y,X).
$$

Then \(J^2=-\mathbf1\), so \(J\) is an almost-complex structure. Dombrowski's calculation shows that \(J\) is integrable precisely when the connection has vanishing curvature and torsion.

Given a positive metric \(g\) on \(M\), define

$$
\widetilde g((X,Y),(X',Y'))
=g(X,X')+g(Y,Y').
$$

Satoh's formulation shows how closure of the associated fundamental two-form is controlled by the dual connection. In the flat Hessian case, \((TM,J,\widetilde g)\) is Kähler.

## Affine complex coordinates

If \(x^i\) are \(\nabla\)-affine coordinates and \(y^i\) are their induced fiber coordinates, then

$$
z^i=x^i+iy^i
$$

are complex coordinates. Real affine transition functions complexify to holomorphic affine transition functions, so these local coordinates patch.

If \(g_{ij}=\partial_i\partial_j\Psi\), define

$$
K(z,\bar z)
:=2\Psi\!\left(\frac{z+\bar z}{2}\right).
$$

Then

$$
\frac{\partial^2K}
{\partial z^i\partial\bar z^j}
=\frac12g_{ij}.
$$

With the convention

$$
\omega=i\partial\bar\partial K,
\qquad
\mathrm ds^2
=2K_{i\bar j}\,\mathrm dz^i\mathrm d\bar z^j,
$$

this gives

$$
\omega=g_{ij}\,\mathrm dx^i\wedge\mathrm dy^j,
\qquad
\mathrm ds^2
=g_{ij}
\left(
\mathrm dx^i\mathrm dx^j
+\mathrm dy^i\mathrm dy^j
\right),
$$

which is precisely the fundamental form and real metric induced by \(\widetilde g\). Other common conventions move the factor of \(2\) between the Kähler potential, Hermitian components, and line element; the tensors above fix the convention used here.

## Canonical conjugation

Fiber negation defines

$$
\tau:TM\longrightarrow TM,
\qquad
\tau(x,y)=(x,-y).
$$

In the complex coordinates above,

$$
\tau(z)=\bar z.
$$

Thus \(\tau\) is antiholomorphic and involutive, and

$$
\operatorname{Fix}(\tau)
=\{(x,0):x\in M\}
\simeq M.
$$

This supplies the exact dimension relation

$$
\boxed{
\dim_{\mathbb R}M=n,
\quad
\dim_{\mathbb C}TM=n,
\quad
\dim_{\mathbb R}TM=2n.}
$$

For \(n=3\), the source is six-real-dimensional and its fixed locus is three-real-dimensional.

## Why this does not derive three-space

The direction of construction is

$$
\boxed{
\text{real Hessian }M
\longmapsto
\text{complexification }TM.}
$$

The real \(M\) and its dimension are inputs. If \(M\) is the CRF response manifold, its points label faithful states, readouts, or response parameters. They are not automatically spatial locations. A spatial interpretation still requires a carrier-realization map such as

$$
\mathfrak C:
M_{\mathrm{response}}
\longrightarrow
\mathsf{SpatialCarrier}_3
$$

with locality, measure, mode decomposition, topology, and observable nets derived on the target.

Nor does this construction choose an antiholomorphic involution on some independently supplied complex threefold \(X\). It manufactures a particular \(X=TM\) together with its conjugation. In general \(TM\) is noncompact, whereas the conditional complex \(S^6\) is compact and non-Kähler. They cannot be the same complex manifold, although they may describe different layers of one programme.

## What it does contribute

The tangent-bundle construction remains valuable in four ways.

1. It gives a canonical complexification of a proven Hessian response manifold rather than an arbitrary doubling of coordinates.
2. It supplies a controlled antiholomorphic involution and fixed real slice.
3. It provides a setting in which the Hessian potential becomes a Kähler potential, useful for testing holomorphic response coordinates and transport.
4. It gives a precise counterexample to the claim that “six real dimensions yielding three” must mean compactification or deletion: passing to the fixed locus selects a real submanifold of half the real dimension, although here that real half was selected at the start.

Fixed-locus formation is not a conditional expectation, quotient, or wall-descent process. For factive spacetime the remaining step is the realization described in [[algebra/real-forms-and-factive-spacetime|real forms and factive spacetime]]. Conjugation selects a real object; it does not create a one-sided record order or Lorentzian time.

## Primary sources

- P. Dombrowski, [[library/geometry-of-the-tangent-bundle/entry|*On the Geometry of the Tangent Bundle*]], *Journal fur die reine und angewandte Mathematik* 210 (1962), 73--88. This supplies the natural almost-complex structure and its integrability criterion.
- H. Satoh, [[library/almost-hermitian-structures-on-tangent-bundles/entry|*Almost Hermitian Structures on Tangent Bundles*]], arXiv:1908.10824, revised 2025; originally *Proceedings of the Eleventh International Workshop on Differential Geometry*, 105--118. This supplies the almost-Kähler/Kähler criteria in terms of the connection and its dual.

These sources construct geometry on \(TM\). They do not identify a response manifold with physical space or apply the construction to the anonymous \(S^6\) manuscript.
