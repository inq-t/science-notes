---
inq.module: albert-algebra
inq.include:
  - './'
inq.ambient:
  - '*.py'
keywords: [Albert algebra, exceptional Jordan algebra, Peirce decomposition, regular multiplication, octonions]
---
# Albert Algebra

The compact Albert algebra is the 27-dimensional Euclidean Jordan algebra of Hermitian three-by-three octonionic matrices. Its positive cone, trace metric, primitive idempotents and regular multiplication operators provide distinct but compatible carriers for finite comparison constructions. The algebra is exceptional: a faithful linear realization by ordinary matrices does not turn its Jordan product into an associative matrix product.

Write
\[
J=\mathfrak h_3(\mathbb O),\qquad
x\circ y=\tfrac12(xy+yx),\qquad
\langle x,y\rangle_J=\operatorname{tr}_J(x\circ y),\qquad
\operatorname{tr}_J\mathbf1=3.
\]
Each binary matrix product is well-defined; no associativity of a product of three octonionic matrices is assumed. The trace form is positive definite and associative with the Jordan product. The cone of squares is the cone of nonnegative Jordan spectra.

The compact automorphism group is \(F_4\). It fixes the unit and acts irreducibly on the real trace-free space \(J_0=\ker\operatorname{tr}_J\), of dimension 26. For a primitive idempotent \(p\), the eigenvalues of \(L_p:x\mapsto p\circ x\) are \(1,1/2,0\), with respective dimensions \(1,16,10\). The primitive orbit is \(F_4/\operatorname{Spin}(9)\); its tangent is the Peirce half-space. The zero Peirce space is a rank-two octonionic corner, whose nine trace-free directions carry the vector representation of \(\operatorname{Spin}(9)\). These representation facts are recorded by [[library/stability-of-compact-symmetric-spaces/inq|Semmelmann–Weingart, §4]] and [[library/exceptional-lie-groups-yokota/inq|Yokota]].

[[albert-algebra/regular-multiplication-and-trace|Regular multiplication and trace]] constructs the injective positive linear map \(x\mapsto L_x\) on \(J_{\mathbb C}\), derives its trace normalization, and distinguishes it from a product-preserving embedding. [[albert-algebra/coordinates-and-exact-arithmetic|Coordinates and exact arithmetic]] specifies the concrete octonion table and Hermitian basis used to calculate those products. Coordinate identities can certify a finite construction on this declared algebra; they do not select a physical state, context distribution or clock.
