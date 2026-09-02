# The \(A_2\) Weyl Measure Does Not Turn Degree into a Gap

The actual compact \(SU(3)\) radial kinetic operator tests the determinant fork more sharply than the provisional half-line model. Weyl integration forces the square root of the degree-six orbit density into the Hilbert amplitude, but the conjugated radial Laplacian is then governed by the \(SU(3)\) Casimir spectrum. Its first nonconstant class mode has \(C_2=4/3\) in the standard physics normalization, not \(9\) or \(36\). The \(3\to6\) determinant chain remains exact algebra, but an operator theorem—not a degree count—must turn it into Yang--Mills coercivity. The interacting many-link vacuum adds a further ground-state weight and is not settled by this one-link Haar calculation.

**Status: [EXACT COMPACT-GROUP GEOMETRY; DIAGNOSTIC MODEL].** The radial calculation applies to conjugation-invariant functions on one copy of \(SU(3)\). A full lattice gauge carrier has many links, vertexwise Gauss constraints, plaquette interactions, and a continuum limit. The calculation is a decisive type check, not a mass-gap computation.

## Lie-algebra Vandermonde and compact-group denominator

For a traceless Hermitian Lie-algebra element with eigenvalues \(r_1+r_2+r_3=0\), the polynomial Vandermonde is

$$
\Delta_{\mathfrak{su}(3)}(r)
:=
\prod_{i<j}(r_i-r_j).
$$

It is homogeneous of degree three, and its invariant square has degree six. This is the local, noncompact scaling calculation used in the determinant fork.

For a compact group element, the eigenvalues are phases \(e^{i\theta_j}\), and the Weyl denominator is instead trigonometric:

$$
\delta(\theta)
:=
\prod_{\alpha>0}
2i\sin\frac{\alpha(\theta)}2.
$$

The Weyl integration density is

$$
J(\theta)=|\delta(\theta)|^2.
$$

It has the same cubic small-angle leading term and the same amplitude--density square, but no global homogeneous radial coordinate:

$$
\delta(\varepsilon\theta)
=
C\,\varepsilon^3
\prod_{\alpha>0}\alpha(\theta)
+O(\varepsilon^5),
$$

With the displayed \(2i\sin(\alpha/2)\) convention and one fixed positive-root order, \(C=i^3=-i\); reversing root order can change its sign. In eigenangle coordinates the root product is the Lie-algebra Vandermonde, up to this fixed phase and coordinate normalization.

The logarithmic slope \(3\) is therefore a local tangent statement near the identity. It is not yet an eigenvalue of the compact radial Laplacian.

## The Hilbert carrier forces the half-density

Conjugation classes of \(SU(3)\) are parametrized by \(T/W\), where \(T\) is a maximal torus and \(W\simeq S_3\). Weyl integration identifies the class-function carrier with

$$
L^2(T/W,J\,\mathrm d\theta).
$$

Up to the fixed Weyl normalization, multiplication by the Weyl denominator gives the unitary map

$$
U:f\longmapsto\delta f
$$

from Weyl-invariant functions with measure \(J\,\mathrm d\theta\) to Weyl-anti-invariant functions with flat torus measure. Thus the square root of the orbit density is not optional:

$$
J=|\delta|^2
\quad\Longrightarrow\quad
U\text{ uses }\delta,\text{ not }J.
$$

This confirms the half-density warning in the causal-grain packet. It also shows why the warning does not by itself select a threshold of nine.

The target is the Weyl-anti-invariant subspace, not the full flat-torus carrier. Its functions vanish on reflection walls in the trace sense, and the self-adjoint operator below has the domain transported by \(U\) from the class-function Laplacian domain. Arbitrary torus plane waves are not additional radial states.

## Radial conjugation produces the Casimir

Let \(\rho\) be the half-sum of positive \(A_2\) roots. In the mathematical normalization with roots of squared length \(2\), the radial Laplacian obeys

$$
\boxed{
U(-\Delta_{SU(3)}^{\mathrm{rad}})U^{-1}
=
-\Delta_T-\lVert\rho\rVert^2.
}
$$

The Weyl character formula writes the irreducible character of highest weight \(\lambda\) as

$$
\chi_\lambda
=
\frac{A_{\lambda+\rho}}{A_\rho}.
$$

The corresponding radial eigenvalue in this normalization is

$$
\lVert\lambda+\rho\rVert^2-\lVert\rho\rVert^2
=
\langle\lambda,\lambda+2\rho\rangle.
$$

For the fundamental and adjoint weights these values are \(8/3\) and \(6\). The standard physics convention uses one half of this Laplacian:

$$
U(-\Delta_{\mathrm{phys}}^{\mathrm{rad}})U^{-1}
=
\frac12
\left(
-\Delta_T-\lVert\rho\rVert^2
\right),
$$

so

$$
C_2(p,q)
=
\frac13
\left(
p^2+q^2+pq+3p+3q
\right).
$$

Equivalently,

$$
C_2(\lambda)
=
\frac12
\left(
\lVert\lambda+\rho\rVert^2-\lVert\rho\rVert^2
\right).
$$

and hence

$$
C_2(1,0)=C_2(0,1)=\frac43,
\qquad
C_2(1,1)=3.
$$

The fundamental and antifundamental characters are the first nonconstant class modes. Polynomial degree three, density degree six, Witten thresholds nine and thirty-six, mathematical radial shift \(8/3\), and physics Casimir \(4/3\) are different invariants until a normalization and physical generator are declared.

[[library/the-full-laplace-beltrami-operator-on-u-n-and-su-n/inq|The compact \(U(N)\) and \(SU(N)\) Laplacian source]] owns the radial operator. [[contemporary-puzzles/yang-mills-mass-gap/receipts/a2_radial_receipt.py|The exact-arithmetic receipt]] checks the \(A_2\) root lengths, \(\rho\)-shift, representation dimensions, and Casimirs; [[contemporary-puzzles/yang-mills-mass-gap/receipts/a2-radial-receipt-output.txt|its stored output]] records the passing run. It verifies no physical carrier map.

## Why the \(9/36\) half-line model remains useful

For

$$
A_w=\partial_N+w,
\qquad
L_w=A_w^\dagger A_w,
$$

on the half-line with the induced Robin boundary condition,

$$
\sigma(L_w)=\{0\}\cup[w^2,\infty).
$$

This is an exact Witten model for a chosen exponential amplitude \(e^{-wN}\). It answers:

> What gap follows if this one-sided exponential is the vacuum amplitude of this operator?

The compact radial calculation answers a different question:

> What operator and spectrum are forced by the Haar geometry of conjugation classes of \(SU(3)\)?

The two operators are not unitarily identified. The half-line slope gives \(9\) when \(e^{-6N}\) is a probability density and \(36\) when it is declared an amplitude. The compact group gives the Casimir spectrum. A physical bridge must choose one carrier and prove the comparison; numerical recurrence cannot do that work.

## The determinant character is not a color character

Three exact obstructions prevent a direct identification with the complex-threefold determinant:

1. \(SU(3)\) has no nontrivial one-dimensional continuous characters. In particular, the determinant of its defining representation is identically one.
2. The Weyl denominator transforms by the sign representation of the Weyl group \(S_3\), not by a nontrivial character of color \(SU(3)\).
3. The weight-three action on \(\det T^{1,0}X\) is the scalar \(GL(1,\mathbb C)\) action on a complex frame. It is not automatically the defining representation of color \(SU(3)\).

The dimension formula

$$
\dim V_{p,q}
=
\frac{(p+1)(q+1)(p+q+2)}2
$$

equals one only for \((p,q)=(0,0)\), making the first obstruction explicit.

There is a related global obstruction on the integrable complex six-sphere. Every holomorphic function on a compact connected complex manifold is constant. Hence there is no nonconstant global holomorphic scalar map

$$
(S^6,J_{\mathrm{int}})
\longrightarrow
\mathfrak t_{\mathbb C}/W
\simeq
\mathbb C^2.
$$

Nontrivial holomorphic line bundles, their transition cocycles, meromorphic functions, and local maps can still exist. Any nonconstant *holomorphic* bridge must therefore use such local, meromorphic, bundle-valued, or correspondence data rather than a globally defined pair of holomorphic invariant polynomials. A smooth, measurable, or nonholomorphic bridge is not excluded, but must explain why holomorphicity is abandoned.

## What a valid \(S^6\)-to-\(SU(3)\) bridge must carry

The minimum credible construction has the type

$$
\boxed{
(K_X,\{g_{ij}\},\nabla^K)
\dashrightarrow
(\text{Weyl sign line},\delta,\nabla^{\mathrm{rad}})
\dashrightarrow
(\mathcal H_{\mathrm{phys}},\mathcal E_{\mathrm{flux}}).
}
$$

It must explain:

- why the canonical-line cocycle descends to the \(S_3\) alternating line;
- how local complex frames become gauge-orbit variables without identifying the stabilizer \(SU(3)\) with color by name alone;
- which connection or Dirac operator transports the line data;
- why the induced quadratic form is the physical electric-flux form; and
- why lower Casimir modes are absent if a higher discriminant sector is claimed to control the first excitation.

Until then, integrable \(S^6\) geometry can organize a possible carrier or polarization, but it does not select the Yang--Mills spectral coefficient.

## Consequence for the programme

The corrected picture has two exact chains separated by an open carrier map:

$$
\text{complex rank three on }S^6
\longrightarrow
\text{canonical determinant line}
\longrightarrow
\text{Hermitian norm-square}
\dashrightarrow
\text{Weyl sign line on }SU(3),
$$

and

$$
\delta
\longrightarrow
|\delta|^2
\longrightarrow
\boxed{\text{compact radial operator}}
\longrightarrow
\text{Casimir spectrum}.
$$

The dashed arrow is the missing identification. The exact compact \(SU(3)\) choice yields Casimirs; the separate exact half-line choice yields \(w^2\). The research problem is to construct a physical carrier map and compare its quadratic form with the many-link vacuum-weighted flux form, not to decide among \(4/3\), \(9\), and \(36\) by numerical appeal.
