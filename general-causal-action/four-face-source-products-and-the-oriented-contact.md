# Four-Face Source Products and the Oriented Contact

The universal first-order source lift on the four-face patch does not preserve ordinary multiplication. The actual comb kinetic jet forces a nonzero cubic contact between two mode-radius sources: its coefficient is \(4/7\), with no fitted parameter. A corresponding first-order product correction is associative. The contact survives faithful point-coordinate and half-density changes, while its compact realization distinguishes a corrected composite from the ordinary product of separately corrected probes.

**Status: exact first-order polynomial-core calculation for the fixed four-face theory.** [[four-face-oriented-normal-form-and-the-universal-source-lift|The universal normal form]] owns the complete odd operator and linear quadratic-source lift. [[four-face-cubic-response-and-source-leakage|FC]] fixes the raw rows and mode orientation. [[oriented-source-products-and-the-compact-contact-return|The compact contact return]] realizes the resulting product comparison in the actual vacuum. No unitary exponential of an unbounded formal generator or spatially uniform product law is assumed.

[[lie-bracket-source-contact-and-the-positive-comparison-test|LC1–9]] proves the Cartan-form version of this contact for every compact connected simple group. Its Gaussian contraction retains the metric-dependent norm \(\mathfrak F_Q\), and its complete multiplier lift also fails the same-Gaussian \(L^2\) positive-comparison test.

## The actual third-derivative coefficient

Use the four vector modes \(Y_i\) of FC1, with
\[
\omega=(\sqrt2,2,2,\sqrt6),\qquad
K_0=\sum_i\left(-\omega_i^2\Delta_i+\tfrac14|Y_i|^2-\tfrac32\omega_i\right),
\qquad
\partial_i\Omega=-\frac{Y_i}{2\omega_i}\Omega .
\tag{PC1}
\]
The core consists of invariant polynomials times the normalized vacuum \(\Omega\). Let \(T(A,B,C)=A\cdot(B\times C)\), and \(T_{ijk}=T(Y_i,Y_j,Y_k)\) for increasing indices.

For a distinct triple \(i<j<k\), write the actual odd jet as
\[
V_1^{ijk}=v_iT(Y_i,\partial_j,\partial_k)
+v_jT(\partial_i,Y_j,\partial_k)
+v_kT(\partial_i,\partial_j,Y_k).
\]
The FJ rows, rotated by FC1, give directly
\[
v_i=-2\sum_e
(\bar s_{ej}\bar z_{eki}-\bar s_{ek}\bar z_{eji}),
\tag{PC2}
\]
with the other coefficients obtained by cyclic permutation. Derivatives of these linear row coefficients contribute zero by the alternating color contraction.

In the solution \([K_0,S_1]=-V_1\), use the triple ansatz
\[
S_1^{ijk}=u_iT(\partial_i,Y_j,Y_k)
+u_jT(Y_i,\partial_j,Y_k)
+u_kT(Y_i,Y_j,\partial_k)
+p_{ijk}T(\partial_i,\partial_j,\partial_k).
\]
The identities \([K_0,Y_i]=-2\omega_i^2\partial_i\) and
\([K_0,\partial_i]=-Y_i/2\) reduce its coefficients to
\[
u_i+u_j+u_k=0,\qquad
2\omega_k^2u_j+2\omega_j^2u_k+\tfrac12p_{ijk}=v_i,
\tag{PC3}
\]
and the two cyclic equations. Substitution of all twelve raw rows gives the following exact rational ledger:

| Triple | \((v_i,v_j,v_k)\) | \(p_{ijk}\) |
| --- | --- | --- |
| \(012\) | \((0,-1,0)\) | \(-4/7\) |
| \(013\) | \((3,-3,-1)\) | \(0\) |
| \(023\) | \((-1,1,-1)\) | \(0\) |
| \(123\) | \((-1,2,-2)\) | \(0\) |

For example, on \(012\), equation (PC3) gives
\(p_{012}=(6v_0+4v_1+4v_2)/7=-4/7\).
The repeated-mode terms of \(V_1\) have the form
\(Y_i\cdot(\partial_i\times\partial_j)\). Their angular factor commutes with the mode-\(i\) oscillator, so a first-order vector field supplies their normal form. They must be retained in the linear source lift, but yield no double multiplication commutator. Consequently
\[
\boxed{S_1=\mathscr V-\tfrac47\mathscr P,\qquad
\mathscr P=\partial_0\cdot(\partial_1\times\partial_2),}
\tag{PC4}
\]
where \(\mathscr V\) is the first-order polynomial vector field specified by the universal normal form. The third-order part in (PC4) is complete, not a restriction to its vacuum action.

## Compression to multiplication sources loses a product term

For an invariant polynomial \(F\), define its vacuum-equivalent multiplication correction
\[
\mathcal D(F)=\Omega^{-1}[S_1,M_F]\Omega .
\]
The operator commutator always obeys
\([S_1,M_FM_G]=[S_1,M_F]M_G+M_F[S_1,M_G]\).
Applying the resulting operators to \(\Omega\) instead gives
\[
\boxed{
\mathcal C(F,G):=\mathcal D(FG)-F\mathcal D(G)-G\mathcal D(F)
=\Omega^{-1}\bigl[\,[S_1,M_F],M_G\bigr]\Omega.}
\tag{PC5}
\]
The vector field \(\mathscr V\) contributes zero to \(\mathcal C\). Its missing information is entirely in the third-order part of (PC4).

Take arbitrary real invariant quadratics, including constants, and write
\(F_i=\nabla_iF\), \(G_i=\nabla_iG\). Their Hessians have the form
\(\partial_{i,a}\partial_{j,b}F=2B_{ij}\delta_{ab}\).
Every Hessian term in the double commutator therefore vanishes against the alternating color tensor. The remaining derivative acts on \(\Omega\), giving the complete bilinear formula
\[
\boxed{\begin{aligned}
\mathcal C(F,G)=\frac27\bigg[&
\frac{T(F_0,G_1,Y_2)+T(G_0,F_1,Y_2)}{\omega_2}\\
&+\frac{T(F_0,Y_1,G_2)+T(G_0,Y_1,F_2)}{\omega_1}\\
&+\frac{T(Y_0,F_1,G_2)+T(Y_0,G_1,F_2)}{\omega_0}
\bigg].
\end{aligned}}
\tag{PC6}
\]
This is a real cubic invariant, symmetric in \(F,G\), and unchanged by adding constants to either source.

For \(R_i=|Y_i|^2\), the nonzero distinct-radius contacts are
\[
\boxed{
\mathcal C(R_0,R_1)=\mathcal C(R_0,R_2)=\tfrac47T_{012},\qquad
\mathcal C(R_1,R_2)=\tfrac{4\sqrt2}{7}T_{012}.}
\tag{PC7}
\]
All \(\mathcal C(R_i,R_i)\) and all radius pairs containing \(R_3\) vanish. Equation (PC6) also controls mixed quadratic marks involving mode \(3\); for example,
\(\mathcal C(Y_0\cdot Y_3,R_1)=2T_{123}/7\).

The contact is nonzero on the physical invariant carrier: orthonormal \(Y_0,Y_1,Y_2\) give \(T_{012}=1\). Its Gaussian mean vanishes by parity, but the permitted oriented source detects it:
\[
\boxed{
\langle\mathcal C(R_0,R_1),T_{012}\rangle_{\Omega^2}
=\tfrac47\|T_{012}\Omega\|^2
=\frac{96\sqrt2}{7}>0.}
\tag{PC8}
\]
Testing only unmarked means would miss this product correction.

## The forced first-order product is associative

Let \(\mathcal T_h=I+h\mathcal D\) denote the formal multiplier lift on the invariant polynomial algebra. Then
\[
\mathcal T_h(FG)
=\mathcal T_h(F)\mathcal T_h(G)+h\mathcal C(F,G)+O(h^2).
\]
Thus the product transported onto the corrected marks is
\[
A\star_h B=AB+h\mathcal C(A,B)+O(h^2).
\tag{PC9}
\]
Here \(\mathcal C\) on general polynomial arguments is defined by (PC5); formula (PC6) is its explicit quadratic restriction. Pulling ordinary multiplication back through \(\mathcal T_h\) instead gives \(FG-h\mathcal C(F,G)+O(h^2)\).

Because (PC5) is the product defect of one linear map, it satisfies
\[
F\mathcal C(G,H)-\mathcal C(FG,H)
+\mathcal C(F,GH)-\mathcal C(F,G)H=0.
\tag{PC10}
\]
Direct expansion cancels every term involving \(\mathcal D\). Hence \(\star_h\) is associative modulo \(h^2\), as well as commutative and unital to this order. This is not an all-orders associative construction or a noncommutative bracket.

For homogeneous quadratic \(F,G\), their product lift splits into degrees five and three:
\[
\mathcal D(FG)=F\mathcal D(G)+G\mathcal D(F)+\mathcal C(F,G).
\]
Since the compact normal-mode vectors satisfy \(Q_i=hY_i/2+O(h^3)\), a quintic correction has the required first-order scaling after normalizing a quartic probe by \(16/h^4\). A cubic contact instead requires the explicit compact term
\[
\frac{h^2}{2}\mathcal C(F,G)(Q).
\tag{PC11}
\]
For \(R_0,R_1\) this is \(2h^2T_{012}(Q)/7\). A fixed nonzero cubic coefficient would scale as \(h^{-1}\), not \(h\), in that normalized quartic experiment. [[oriented-source-products-and-the-compact-contact-return|The actual compact realization]] retains this distinction between a corrected composite and an ordinary product of fixed corrected probes.

## Faithful point-coordinate changes preserve the contact

Consider a near-identity real point-coordinate and half-density unitary with first jet
\(W_h=I+hA+O(h^2)\), where
\[
A=v\cdot\partial+\tfrac12\operatorname{div}v .
\]
Conjugation gives \(V_1'=V_1+[A,K_0]\), and the transported normal form is \(S_1'=S_1+A\). Indeed \([K_0,S_1+A]=-V_1'\). For a graded coordinate change this is the same odd normalization, with the commuting ambiguity fixed as in the universal normal form. Since \([A,M_F]=M_{v\cdot\nabla F}\),
\[
\bigl[\,[A,M_F],M_G\bigr]=0,\qquad \mathcal C'(F,G)=\mathcal C(F,G).
\tag{PC12}
\]
The faithfully transported source jets change by a derivation, so the contact is unchanged as well. The half-density multiplication term commutes with every source.

The nonzero coefficient in (PC7) therefore cannot be removed by such a change of chart. This statement does not cover arbitrary differential unitaries that change the multiplication algebra, or a change of the physical connector observables. The result supplies a definite first-order source-composition correction within the existing theory; it changes neither its clock nor its physical-gap target.
