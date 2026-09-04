# Triangle-Presentation Descent on the Neutral Adjoint Carrier

The character and augmentation routes miss a neutral observable sector because an equivariant map cannot carry a nontrivial charge directly into an invariant block. An irreducible presentation has a different canonical descendant: its operator carrier \(V\otimes\overline V\simeq\operatorname{End}(V)\), where scalar phase cancels. For the explicit \(C_3*C_4\) family, averaging conjugation over the two finite cyclic presentations gives two trace-preserving conditional expectations whose common range is exactly the scalar line. Their summed relative-entropy loss is coercive on every traceless finite-algebra density tangent, with optimal dimensionless floor \(1-|\cos 2\theta|\). This is an exact finite model of global discrete presentation producing a smooth distinction frame; it is not yet a gauge-invariant Yang--Mills carrier, a localized inner-unitary path, or a physical energy gap.

**Status: [EXACT FINITE-DIMENSIONAL THEOREM] for the conditional expectations, relative-entropy Hessian, spectrum, and orientation operator; [EXACT CONDITIONAL TARGET] for the direct-sum frame, complex localized-energy form, and cosmological bound after all hypotheses in (NA27)--(NA34) are supplied; [INTERPRETATION] for calling \(\operatorname{End}(V)\) the neutralized presentation carrier; [OPEN] for a natural map from gauge-invariant Yang--Mills state tangents, a Type-III regional realization, Hermitian energy-form-core coverage, regulator-uniform coercivity, and continuum survival.**

## From a charged presentation to its operator carrier

Let

\[
\Gamma=C_3*C_4
=
\langle a,b\mid a^3=b^4=1\rangle,
\qquad
\omega=e^{2\pi i/3},
\tag{NA1}
\]

and, for \(0<\theta<\pi/2\), define a unitary representation on \(V=\mathbb C^2\) by

\[
A:=\rho_\theta(a)
=
\begin{pmatrix}
1&0\\
0&\omega
\end{pmatrix},
\qquad
B_\theta:=\rho_\theta(b)
=
R_\theta
\begin{pmatrix}
1&0\\
0&i
\end{pmatrix}
R_\theta^{-1},
\tag{NA2}
\]

where

\[
R_\theta
=
\begin{pmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{pmatrix}.
\tag{NA3}
\]

Then \(A^3=B_\theta^4=I\), and the representation is irreducible throughout the displayed interval. [[global-discreteness-kazhdan-rigidity-and-the-gap]] uses this family to show that the cusp displacement can nevertheless approach zero.

Now change carrier:

\[
\mathcal M_\theta
:=
\operatorname{End}(V)
\cong
V\otimes\overline V,
\qquad
\tau(X):=\frac12\operatorname{Tr}X.
\tag{NA4}
\]

A scalar phase on \(V\) cancels in \(V\otimes\overline V\). The group acts on \(\mathcal M_\theta\) by conjugation,

\[
\operatorname{Ad}_{\rho_\theta(g)}(X)
=
\rho_\theta(g)X\rho_\theta(g)^*.
\tag{NA5}
\]

This is the first precise sense in which the carrier is *neutralized*. It is not the assertion that every element of \(\mathcal M_\theta\) is invariant under \(\Gamma\).

## The two presentation descents

Average over the two finite cyclic subgroups:

\[
\mathbb E_A(X)
:=
\frac13\sum_{r=0}^{2}A^rX A^{-r},
\qquad
\mathbb E_B(X)
:=
\frac14\sum_{r=0}^{3}B_\theta^rX B_\theta^{-r}.
\tag{NA6}
\]

These are unital, completely positive, trace-preserving conditional expectations. On the Hilbert carrier \(L^2(\mathcal M_\theta,\tau)\), they are orthogonal projections onto

\[
\operatorname{Ran}\mathbb E_A=\{A\}',
\qquad
\operatorname{Ran}\mathbb E_B=\{B_\theta\}'.
\tag{NA7}
\]

Irreducibility and Schur's lemma give

\[
\boxed{
\operatorname{Ran}\mathbb E_A
\cap
\operatorname{Ran}\mathbb E_B
=
\mathbb C I.}
\tag{NA8}
\]

Thus the joint invariant of the two presentation descents is the scalar line, even though either descent separately retains a nontrivial traceless direction.

## Exact neutralized frame spectrum

Let

\[
\mathcal M_{\mathrm{sa},0}
:=
\{X=X^*:\operatorname{Tr}X=0\}.
\tag{NA9}
\]

Using the Hilbert--Schmidt-orthonormal Pauli basis

\[
x:=\frac{\sigma_x}{\sqrt2},
\qquad
y:=\frac{\sigma_y}{\sqrt2},
\qquad
z:=\frac{\sigma_z}{\sqrt2},
\tag{NA10}
\]

the restrictions of the expectations to \(\mathcal M_{\mathrm{sa},0}\) are rank-one orthogonal projections:

\[
\mathbb E_A=P_z,
\qquad
\mathbb E_B=P_{n_\theta},
\qquad
n_\theta
=
\sin(2\theta)x+\cos(2\theta)z.
\tag{NA11}
\]

Their Friedrichs cosine is

\[
c_F(\theta)
=
|\langle z,n_\theta\rangle|
=
|\cos 2\theta|.
\tag{NA12}
\]

Define the presentation-loss operator

\[
\mathcal G_\theta
:=
2I-\mathbb E_A-\mathbb E_B.
\tag{NA13}
\]

On the full Hilbert carrier its kernel is \(\mathbb CI\). On the traceless self-adjoint carrier,

\[
\boxed{
\operatorname{spec}
\left(
\mathcal G_\theta
\big|_{\mathcal M_{\mathrm{sa},0}}
\right)
=
\left\{
1-|\cos 2\theta|,
1+|\cos 2\theta|,
2
\right\}.}
\tag{NA14}
\]

Consequently,

\[
\boxed{
\langle X,\mathcal G_\theta X\rangle_{\mathrm{HS}}
\geq
\left(1-|\cos 2\theta|\right)
\|X\|_{\mathrm{HS}}^2,
\qquad
X\in\mathcal M_{\mathrm{sa},0}.}
\tag{NA15}
\]

The lower constant is positive at every irreducible member but is not uniform over the family:

\[
1-|\cos 2\theta|
\longrightarrow0
\quad
\text{as }
\theta\longrightarrow0
\text{ or }
\theta\longrightarrow\frac\pi2.
\tag{NA16}
\]

The finite-order relations determine the two presentations but do not determine their relative angle. This is the exact distinction between discrete grammar and quantitative rigidity.

[[receipts/triangle-neutral-adjoint-frame-receipt.py|The finite receipt]] checks the cyclic relations, expectation projections, frame spectrum, Hessian identity, and orientation spectrum; its [[receipts/triangle-neutral-adjoint-frame-receipt-output.txt|stored output]] records representative angles.

## The same operator is a relative-entropy loss Hessian

Let \(\tau=I/2\) also denote the tracial density matrix. For \(X\in\mathcal M_{\mathrm{sa},0}\) and sufficiently small real \(s\), define

\[
\rho_s:=\frac12(I+sX).
\tag{NA17}
\]

Direct expansion gives

\[
D(\rho_s\Vert\tau)
=
\frac{s^2}{4}\operatorname{Tr}(X^2)
+O(s^3).
\tag{NA18}
\]

Because the two expectations preserve the trace, the state restricted to \(\operatorname{Ran}\mathbb E_A\) or \(\operatorname{Ran}\mathbb E_B\) is represented by \(\mathbb E_A(\rho_s)\) or \(\mathbb E_B(\rho_s)\). Define the two data-processing losses

\[
L_A(s)
:=
D(\rho_s\Vert\tau)
-
D(\mathbb E_A\rho_s\Vert\tau),
\tag{NA19}
\]

and analogously \(L_B(s)\). Their half-Hessians are

\[
q_A[X]
:=
\frac12L_A''(0)
=
\frac14\|(I-\mathbb E_A)X\|_{\mathrm{HS}}^2,
\tag{NA20}
\]

\[
q_B[X]
:=
\frac12L_B''(0)
=
\frac14\|(I-\mathbb E_B)X\|_{\mathrm{HS}}^2.
\tag{NA21}
\]

Therefore

\[
\boxed{
q_{\mathrm{pair}}[X]
:=
q_A[X]+q_B[X]
=
\frac14
\langle X,\mathcal G_\theta X\rangle_{\mathrm{HS}}.}
\tag{NA22}
\]

If

\[
q_{\mathrm{full}}[X]
:=
\frac12
\left.
\frac{\mathrm d^2}{\mathrm ds^2}
D(\rho_s\Vert\tau)
\right|_{s=0}
=
\frac14\|X\|_{\mathrm{HS}}^2,
\tag{NA23}
\]

then the sharp relative frame inequality is

\[
\boxed{
q_{\mathrm{pair}}[X]
\geq
\left(1-|\cos 2\theta|\right)
q_{\mathrm{full}}[X].}
\tag{NA24}
\]

This realizes, for the triangle presentation in finite Type I form, an algebraic prototype of the first arrow sought by [[localized-relative-entropy-and-the-energy-solder]]: presentation disagreement becomes a restriction-loss Hessian on finite-algebra density tangents. The path \(\rho_s=\tfrac12(I+sX)\) is affine and mixed-state. It is not an inner-unitary path—indeed every inner unitary fixes the trace \(\tau\). The carrier-and-path comparison to localized QFT tangents is therefore absent from this finite static model and must be supplied explicitly below.

## Handedness and stiffness share a pair but are not identical

The orientation-even response is \(\mathcal G_\theta\). The same ordered descents carry the orientation-odd operator

\[
\Omega_\theta
:=
\frac{1}{2i}
[\mathbb E_A,\mathbb E_B].
\tag{NA25}
\]

On the complexification of the traceless carrier,

\[
\operatorname{spec}(\Omega_\theta)
=
\left\{
0,
\pm\frac12\cos(2\theta)\sin(2\theta)
\right\}.
\tag{NA26}
\]

Exchanging \(A\) and \(B\) fixes \(\mathcal G_\theta\) and reverses \(\Omega_\theta\). The pair therefore contains both a reversal-even distinction modulus and a reversal-odd handedness witness. They cannot be identified:

- at \(\theta=\pi/4\), the frame floor is maximal, \(1\), while \(\Omega_\theta=0\);
- near either reducible endpoint, both the floor and the magnitude of the orientation witness vanish;
- in general a nonzero commutator does not determine the lower edge.

This proves only that an ordering-sensitive handedness witness and a positive distinction modulus can descend from one asymmetric presentation structure without being identical. Calling this witness physical chirality would require a graded chiral carrier or an index theorem, neither of which has been constructed here.

## What the operator operates on

The domains are now explicit:

| Map or operator | Carrier | Meaning |
|---|---|---|
| \(\rho_\theta\) | presentation space \(V\) | represents the global \(C_3*C_4\) relations |
| \(\operatorname{Ad}\rho_\theta\) | finite operator algebra \(\operatorname{End}(V)\) | compares presentations after scalar phase cancels |
| \(\mathbb E_A,\mathbb E_B\) | operators or density tangents | retain the two cyclically invariant presentations |
| \(q_A,q_B\) | traceless finite-algebra density tangents | measure distinction forgotten by each restriction |
| \(\mathcal G_\theta\) | the same traceless tangent carrier | charges failure to survive both descents |
| \(\Omega_\theta\) | complexified traceless carrier | remembers the order of the two descents |

Nothing here acts on spacetime, a cosmological scale, or a glueball wave function. The finite model supplies a normalized dimensionless response. [[cosmological-selection-of-the-yang-mills-yardstick]] investigates a separate dimensional selector, and Longo's theorem supplies a real physical energy comparison only after one constructs localized inner-unitary paths in a positive-energy QFT net and then controls their complex form-core extension.

## Exact conditional target with the cosmic yardstick

The two independent constructions can be combined without identifying their carriers, but one finite matrix frame cannot cover the physical vacuum complement. Its centered real carrier has dimension three, so no map from an infinite-dimensional energy-form core into that one carrier can have a lower frame bound. A full-carrier claim requires a family. Let

\[
\mathcal K_{\mathrm{pres},\mathbb R}
:=
\bigoplus_{\alpha\in\mathcal I}^{\ell^2}
\mathcal M_{\mathrm{sa},0}^{(\alpha)},
\qquad
\mathcal K_{\mathrm{pres}}
:=
\mathcal K_{\mathrm{pres},\mathbb R}
\otimes_{\mathbb R}\mathbb C,
\qquad
\kappa_{\mathrm{pres}}
:=
\inf_{\alpha\in\mathcal I}
\left(1-|\cos2\theta_\alpha|\right)>0,
\tag{NA27}
\]

and extend each finite real quadratic form by Hermitian polarization to \(\mathcal K_{\mathrm{pres}}\). Define

\[
Q_{\mathrm{full}}[X]
:=
\sum_\alpha q_{\mathrm{full}}^{(\alpha)}[X_\alpha],
\qquad
Q_{\mathrm{pair}}[X]
:=
\sum_\alpha q_{\mathrm{pair}}^{(\alpha)}[X_\alpha].
\tag{NA28}
\]

The fibrewise theorem gives \(Q_{\mathrm{pair}}\geq\kappa_{\mathrm{pres}}Q_{\mathrm{full}}\). Let \(\mathcal D_{\mathrm{loc}}^{\mathrm{GI}}\) be a complex \(H^{1/2}\)-form core of the physical gauge-invariant vacuum complement. Suppose one genuine restriction loss on one region \(B\), evaluated on the same localized paths used in Longo's theorem, has a positive Hermitian extension \(\widehat q_{\mathrm{loss},B}\) satisfying

\[
\widehat q_{\mathrm{loss},B}[\psi]
\leq
\frac{2\pi R_B}{\hbar c}
\|H^{1/2}\psi\|^2,
\qquad
\psi\in\mathcal D_{\mathrm{loc}}^{\mathrm{GI}}.
\tag{NA29}
\]

This is the complex-core obligation isolated in [[localized-relative-entropy-and-the-energy-solder]]; it does not follow merely because real local-unitary tangents span the core. Suppose there is also a spectrum-independent complex-linear analysis map

\[
J:
\mathcal D_{\mathrm{loc}}^{\mathrm{GI}}
\longrightarrow
\mathcal K_{\mathrm{pres}}
\tag{NA30}
\]

with the lower coverage and form-comparison estimates

\[
Q_{\mathrm{full}}[J\psi]
\geq
b_J\|\psi\|^2,
\qquad
\widehat q_{\mathrm{loss},B}[\psi]
\geq
Q_{\mathrm{pair}}[J\psi],
\qquad
b_J>0.
\tag{NA31}
\]

Then

\[
\widehat q_{\mathrm{loss},B}[\psi]
\geq
b_J\kappa_{\mathrm{pres}}
\|\psi\|^2.
\tag{NA32}
\]

Combining this lower bound with (NA29) gives

\[
\Delta_E
\geq
\frac{\hbar c}{2\pi R_B}
b_J\kappa_{\mathrm{pres}}.
\tag{NA33}
\]

If, independently, the common-count cell is proved to be the centered convex isotropic localization ball in [[cosmological-selection-of-the-yang-mills-yardstick]], then

\[
\boxed{
\Delta_E
\geq
b_J\kappa_{\mathrm{pres}}
(\gamma s_*)^{-1/3}
E_{A,c}\iota_c^{-2/3}.}
\tag{NA34}
\]

This is an exact implication from the displayed assumptions, not a realized mass prediction or positive evidence that Yang--Mills satisfies them. Its factorization is useful because every unknown is typed: \(b_J\) is physical-carrier coverage, \(\kappa_{\mathrm{pres}}\) is the uniform relative-presentation rigidity of the entire frame family, \((\gamma s_*)^{-1/3}\) is common-count multiplicity, and \(E_{A,c}\iota_c^{-2/3}\) is the whole-cosmos dimensional presentation. None of these factors can supply another's missing theorem. Repeating one fixed angle in infinitely many fibres would give \(\kappa_{\mathrm{pres}}=1-|\cos2\theta|\), but no principle here constructs those fibres or selects that angle. An abstract Hilbert-space embedding into repeated three-dimensional fibres is cheap; the hard content is naturality of \(J\) and domination of the entire summed presentation form by the single physical loss in (NA31).

## The remaining Yang--Mills theorem

The construction avoids the elementary charge mismatch but does not identify its neutralized operator carrier with the physical neutral sector. If \(\Gamma\) is interpreted as ordinary gauge or center symmetry, physical glueballs are already invariant and the form can still vanish on them. A valid transfer requires the spectrum-independent map \(J\) in (NA30), from a complex localized gauge-invariant vacuum form core into a centered presentation-comparison carrier, such that:

1. \(J\) is natural and has a uniform lower frame bound on the complex physical tangent core;
2. the common invariant on the centered comparison carrier is \(\{0\}\), while the corresponding uncentered physical family retains only the vacuum line;
3. the entire summed presentation form is dominated by one genuine regional restriction-loss Hessian with a regulator-uniform positive comparison constant;
4. that real path Hessian has a positive Hermitian extension with Longo's upper comparison on the complex \(H^{1/2}\)-form core;
5. at a fixed positive physical separation \(\ell_*\), the relative angle stays uniformly below one through volume and continuum limits, or an equivalent uniform logarithmic decay rate is proved; and
6. the reconstructed net and translation representation are those of pure Yang--Mills.

The finite theorem identifies the right kind of first arrow. Global discreteness supplies the presentations, passage to \(\operatorname{End}(V)\) removes scalar charge, irreducibility reduces their common commutant to one scalar line, and the relative presentation angle supplies coercivity. The infinite Yang--Mills problem is to derive an analogous family whose uniform angle is fixed by geometry rather than chosen through \(\theta\).
