# Lie-Bracket Source Contact and the Positive-Comparison Test

The four-face product contact is determined by the Lie bracket rather than a three-dimensional cross-product identity. For every compact connected simple group, the normalized first kinetic jet gives the same coefficient \(4/7\) multiplying its Cartan three-form. Gaussian response carries the metric-dependent structure-constant norm. The contact is nonzero precisely when the bracket is nonzero, and an invariant nonnegative square rules out interpreting the complete multiplier lift as positive conditional averaging.

**Status: exact first-order polynomial-core and Gaussian response theorem for the declared four-face law.** [[weighted-character-scale-and-bounded-lie-sources|The scale and source normalization]] fixes the invariant metric, representation data and physical units. [[all-group-oriented-kinetic-jet-and-source-lift|The all-group kinetic jet]] derives the normal form from the actual BCH incidence rows. [[fixed-group-compact-vacuum-and-oriented-source-return|The fixed-group compact return]] owns actual centering and realization of these marked responses. The result below neither fixes higher representation invariants nor transfers the \(SU(2)\) nonlinear gap coefficient to another group.

## The metric belongs to the statement

Let \(\mathfrak g\) be the Lie algebra of a compact connected simple group and let \(Q\) be an Ad-invariant positive inner product. In a \(Q\)-orthonormal basis \(E_a\), define
\[
f_{abc}=Q(E_a,[E_b,E_c]),\qquad
T_G(X,Y,Z)=Q(X,[Y,Z])=Q([X,Y],Z),
\]
\[
\boxed{\mathfrak F_Q=\sum_{a,b,c}f_{abc}^2
=\sum_{a,b}\|[E_a,E_b]\|_Q^2.}
\tag{LC1}
\]
Invariance of \(Q\) makes \(f_{abc}\) totally alternating. The norm \(\mathfrak F_Q\) is independent of the orthonormal basis, but not of the metric: replacing \(Q\) by \(aQ\) gives \(\mathfrak F_{aQ}=a^{-1}\mathfrak F_Q\). It vanishes exactly when the Lie bracket vanishes. No group-independent numerical value is substituted for it.

In the normalized four-face coordinates let the four independent Gaussian modes have
\[
\omega=(\sqrt2,2,2,\sqrt6),\qquad
\mathbb E_0[Y_i^aY_j^b]=\delta_{ij}\delta_{ab}\omega_i.
\]
Their square-root density satisfies
\[
\nabla_i\Omega=-\frac{Y_i}{2\omega_i}\Omega,\qquad
K_0=\sum_i\left(-\omega_i^2\Delta_{Q,i}
+\frac{\|Y_i\|_Q^2}{4}-\frac{\dim\mathfrak g}{2}\omega_i\right).
\tag{LC2}
\]
These coordinates and units are returned only after the actual weighted-character Hessian is normalized as in the scale owner.

## The full quadratic contact is a Cartan contraction

The all-group normal-form theorem gives on the polynomial-Gaussian core
\[
S_1=\mathscr V-\frac47\mathscr P_Q,\qquad
\mathscr P_Q=\sum_{a,b,c}f_{abc}
\partial_{0,a}\partial_{1,b}\partial_{2,c},\qquad
[K_0,S_1]=-V_1.
\tag{LC3}
\]
Here \(\mathscr V\) is the complete first-order polynomial vector field, including the repeated-mode angular terms. Define
\[
\mathcal D(F)=\Omega^{-1}[S_1,M_F]\Omega,\qquad
\mathcal C_Q(F,H)=\mathcal D(FH)-F\mathcal D(H)-H\mathcal D(F).
\]
Then \(\mathcal C_Q=\Omega^{-1}\bigl[\,[S_1,M_F],M_H\bigr]\Omega\). The vector-field term contributes zero.

For scalar quadratic pairings \(F=\sum_{ij}B_{ij}Q(Y_i,Y_j)+b\), with \(B\) real symmetric, set \(F_i=\nabla_iF\); define \(H_i\) similarly. Their Hessians are \(2B_{ij}\delta_{ab}\). Every Hessian term in the double commutator vanishes against \(f_{abc}\), leaving
\[
\boxed{\begin{aligned}
\mathcal C_Q(F,H)=\frac27\bigg[&
\frac{T_G(F_0,H_1,Y_2)+T_G(H_0,F_1,Y_2)}{\omega_2}\\
&+\frac{T_G(F_0,Y_1,H_2)+T_G(H_0,Y_1,F_2)}{\omega_1}\\
&+\frac{T_G(Y_0,F_1,H_2)+T_G(Y_0,H_1,F_2)}{\omega_0}
\bigg].
\end{aligned}}
\tag{LC4}
\]
Only the uncontracted Cartan tensor enters this identity. The factor \(\mathfrak F_Q\) appears when a Gaussian expectation contracts two such tensors.

For \(R_i=Q(Y_i,Y_i)\), put \(T=T_G(Y_0,Y_1,Y_2)\). In particular,
\[
\boxed{
\mathcal C_Q(R_0,R_1)=\mathcal C_Q(R_0,R_2)=\frac47T,\qquad
\mathcal C_Q(R_1,R_2)=\frac{4\sqrt2}{7}T.}
\tag{LC5}
\]
The self-contacts of individual radii and the radius pairs involving \(R_3\) vanish. Constants added to any source do not change its contact. As in [[four-face-source-products-and-the-oriented-contact|PC9–12]], this product defect gives a commutative associative product modulo the second order, with opposite signs for transported and pulled-back ordinary multiplication. Faithful first-order point-coordinate and half-density changes add a derivation and leave the contact unchanged.

## Gaussian contraction retains the structure-constant norm

The modes in \(T\) are independent, so direct contraction gives
\[
\mathbb E_0T=0,\qquad
\mathbb E_0T^2
=\omega_0\omega_1\omega_2\sum_{a,b,c}f_{abc}^2
=4\sqrt2\,\mathfrak F_Q.
\]
For \(\Gamma=\mathcal C_Q(R_0,R_1)=4T/7\), it follows that
\[
\boxed{
\langle\Gamma,T\rangle_0=\frac{16\sqrt2}{7}\mathfrak F_Q,\qquad
\|\Gamma\Omega\|^2=\frac{64\sqrt2}{49}\mathfrak F_Q.}
\tag{LC6}
\]
This is a nonzero mixed invariant-source response for every non-Abelian compact simple group, even though the one-point mean vanishes.

Conditioning on the first two modes uses \(T=Q([Y_0,Y_1],Y_2)\) and \(\omega_2=2\):
\[
\boxed{
\mathbb E_0[\Gamma\mid Y_0,Y_1]=0,\qquad
\operatorname{Var}_0(\Gamma\mid Y_0,Y_1)
=\frac{32}{49}\|[Y_0,Y_1]\|_Q^2.}
\tag{LC7}
\]
Indeed \(\mathbb E_0\|[Y_0,Y_1]\|_Q^2
=\omega_0\omega_1\mathfrak F_Q=2\sqrt2\,\mathfrak F_Q\), recovering (LC6) after integration. This is normal-mode conditioning in the harmonic law, not an identification of that partition with a spatial cut or of the squared bracket with a Hamiltonian potential.

For the \(SU(2)\) normalization with \(f_{abc}=\epsilon_{abc}\), \(\mathfrak F_Q=6\), so (LC6) reduces to the earlier \(96\sqrt2/7\) mixed coefficient and \(384\sqrt2/49\) contact norm. Other metrics or groups retain their own value of \(\mathfrak F_Q\).

## A positive-comparison obstruction in every non-Abelian case

If the bracket is nonzero, choose \(Q\)-orthonormal \(x,y\) with \(z=[x,y]\ne0\). Such a pair exists by subtracting the component of \(y\) parallel to \(x\) and then normalizing a noncommuting pair. At
\[
Y_0=x,\qquad Y_1=y,\qquad Y_2=-z,\qquad Y_3=0,
\]
invariance gives \(T=Q([x,y],-z)=-\|z\|_Q^2<0\). Let \(A=R_0+R_1\) and \(f=(A-2)^2\). Equation (LC5) yields
\[
\mathcal C_Q(A,A)=\frac87T,\qquad
\boxed{f=0,\qquad
\mathcal D(f)=2(A-2)\mathcal D(A)+\mathcal C_Q(A,A)
=-\frac87\|z\|_Q^2<0.}
\tag{LC8}
\]
The function \(f\) is globally nonnegative and Ad-invariant. A pointwise positive unital map with first jet \(\Phi_hF=F+h\mathcal D(F)+o(h)\) on these tests would make \(\Phi_hf\) negative at this fixed configuration for sufficiently small \(h>0\). Thus it cannot exist. Equivalently, positivity on squares would require \(\mathcal D(A^2)-2A\mathcal D(A)\ge0\), contrary to (LC8).

An invariant nonnegative smooth cutoff equal to one near the compact orbit of this configuration makes a bounded local witness without changing its differential jet. The obstruction concerns the complete prescribed multiplier lift, including products. It does not prohibit positive maps matching only its quadratic values, and it does not challenge positivity of the actual chronological transfer.

The obstruction also holds for a norm return on one common Gaussian measure \(d\mu_0=\Omega^2\,dY\). Suppose a positive unital source map, defined on the polynomial tests and their squares, satisfies
\[
\Phi_h A=A+h\mathcal D(A)+o_{L^2(\mu_0)}(h),\qquad
\Phi_h(A^2)=A^2+h\mathcal D(A^2)+o_{L^2(\mu_0)}(h).
\]
Its Schwarz defect is nonnegative. Since \(A,\mathcal D(A)\in L^2(\mu_0)\), expansion of the square and Cauchy–Schwarz give
\[
0\le\frac{\Phi_h(A^2)-(\Phi_h A)^2}{h}
\longrightarrow \mathcal C_Q(A,A)=\frac87T
\quad\text{in }L^1(\mu_0).
\tag{LC9}
\]
The nonnegative cone is closed in \(L^1\), whereas \(T<0\) on an open set of positive Gaussian measure. This is impossible. The conclusion uses the stated source jets on the same measure; it does not identify different compact carriers or replace an actual source-vector return by an unproved positive map.

Conversely, if the bracket vanishes, then \(f_{abc}=0\), the Cartan contact and every quantity in (LC6)–(LC7) vanish. In the corresponding Abelian BCH control the first odd kinetic jet vanishes as well. Thus this contact is nonzero if and only if the bracket is nonzero; no three-dimensional vector identity is needed in either direction.

## The universal coefficient does not complete the physical source algebra

The four Cartan triples generated from these quadratic pairings are the channels selected by this first antisymmetric kinetic jet. They are not asserted to span every invariant cubic source for every group. Additional invariant tensors, faithful matrix readouts and their products remain part of the complete source algebra.

The coefficient \(4/7\) belongs to the normalized incidence calculation. Representation-dependent character terms of fourth and higher order, other invariant contractions and the actual excited-state structure still enter nonlinear gap and source coefficients. Neither a common first contact nor the positive variance (LC7) establishes a universal gap correction, an all-orders positive source map, or a continuum Yang–Mills mass gap.
