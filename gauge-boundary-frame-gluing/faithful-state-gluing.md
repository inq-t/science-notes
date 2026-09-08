# Faithful State Gluing

A faithful gauge-invariant density preserves the finite boundary-charge carrier through an equivariant half-density unitary. Correlations remain in the vacuum, conditional expectations and transfer; conditional product structure requires additional independence across a separator.

## Faithful Wilson weights preserve the carrier, not the factorization

Use the finite graph, cut, and gauge actions of [[gauge-boundary-frame-gluing/finite-gauss-gluing|finite Gauss gluing]]. The general transport calculation is [[equivalent-measure-carriers/inq|equivalent-measure carrier transport]].

Let a normalized gauge-invariant law have a faithful density relative to
product Haar,

$$
\mathrm d\nu(a,b)=w(a,b)\,
\mathrm d\mu_A(a)\mathrm d\mu_B(b),
\qquad w>0\ \text{a.e.}
\tag{BG13}
$$

Write \(\nu_A,\nu_B\) for its marginals and define its correlation density

$$
r(a,b)
:=
\frac{\mathrm d\nu}{\mathrm d(\nu_A\otimes\nu_B)}(a,b).
\tag{BG14}
$$

Multiplication by \(r^{1/2}\) defines a gauge-equivariant unitary

$$
W:L^2(\nu)\longrightarrow L^2(\nu_A\otimes\nu_B),
\qquad
Wf=r^{1/2}f.
\tag{BG15}
$$

Consequently the exact weighted carrier identity is

$$
\boxed{
L^2(\nu)^{G^V}
\cong
\left(
L^2(\nu_A)^{K_A}
\widehat\otimes
L^2(\nu_B)^{K_B}
\right)^{K_\partial}.}
\tag{BG16}
$$

The boundary-charge pairing therefore survives for any faithful finite
Wilson slice density, including a strictly positive Perron ground-state
density. This is only a carrier equivalence. If \(r\neq1\), \(W\) is a
nonfactorizing correlation half-density, sends the constant vector to
\(r^{1/2}\), and does not turn the conditional expectation into product
integration. Explicitly,

$$
\mathbb E_\nu\!\left(f\mid\mathscr F_A\right)(a)
=
\int f(a,b)r(a,b)\,\mathrm d\nu_B(b).
\tag{BG17}
$$

The interacting state and transfer therefore remain in the matrix elements.
If \(r\) vanishes, \(W\) reaches only its support subspace; a singular joint
law need not admit this regional tensorization at all.

If a separator \(S\) contains every interaction crossing the cut and the
Wilson law is conditionally independent across \(A|S|B\), the corresponding
state carrier has a direct-integral form

$$
L^2(\nu)
\cong
\int^{\oplus}
L^2(\nu_{A\mid s})\widehat\otimes
L^2(\nu_{B\mid s})\,
\mathrm d\nu_S(s).
\tag{BG18}
$$

Boundary gauge matching acts fibrewise if the separator variables are
boundary-gauge invariant. For raw separator links the action generally
moves \(s\), relating different fibres; a stabilizer or equivariant
disintegration must then be specified. Without conditional
independence, the canonical conditional-product identification (BG18) is
not available as a constant-preserving identification respecting the regional multiplication actions. An abstract Hilbert-space unitary alone would not imply independence. The appropriate noncommutative
replacement is a correspondence or relative tensor product, with its state
and modular hypotheses stated explicitly.


[[gauge-boundary-frame-gluing/oriented-context-gluing-and-mixed-response|Oriented context gluing]] retains joint-state and mixed-response data that separate regional presentations cannot determine.
