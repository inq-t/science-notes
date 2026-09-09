# The Dependent Cube Face Has an Oriented Bracket Source

The ordered sixth-face word produces a cubic magnetic jet and a quadratic Lie-valued closure defect. A bounded scalar mark pairs that defect with the brackets of the five original faces and vanishes identically in an Abelian theory. The true coupled cube oscillator fixes its leading expectation and a signed pattern of pairwise responses. These are consequences of the supplied word, kinetic form and preparation; they do not follow from six independent face laws.

**Status: exact local word and source jets, with evaluated marked expectations in the derived harmonic vacuum.** [[closed-cube-face-words-and-the-prepared-amplitude|CW]] fixes the tree chart and ordered face words. [[closed-cube-raw-edge-kinetic-sewing|CK]] derives the original raw-edge kinetic operator and its harmonic covariance. The separate [[closed-cube-bracket-source-and-the-actual-vacuum-return|actual compact return]] supplies the passage from the Gaussian coefficients to the full ground state and chronology. A magnetic likelihood is not substituted for that ground state.

## Keep the ordered word and the weighted cost

Use a compact connected group with simple Lie algebra \(\mathfrak g\), an Ad-invariant positive metric \(Q\), and GM's faithful unitary representation \(\rho\) with positive commuting preparation weight \(A\). Keep
\[
W_A(g)=\operatorname{Re}\operatorname{Tr}[A(I-\rho(g))],
\qquad Q_A=I_AQ,\qquad
g_{\rm eff}=2I_Ag,\quad h=(\kappa/g_{\rm eff})^{1/4}.
\]
The scale is \(E=\kappa h^{-2}\), and the normalized magnetic cost is \(w_A=W_A/(2I_A)\). The cost weight \(A\) is retained; the Lie-valued source \(q_\rho\) uses GM's unweighted projection.

In CW's common-root chart,
\[
(F_1,\ldots,F_6)=(u,v,w,x,y,v^{-1}w^{-1}xuy).
\]
Write \(u=e^{hU},v=e^{hV},w=e^{hW},x=e^{hX},y=e^{hY}\), and define the ordered increments
\[
(Z_1,Z_2,Z_3,Z_4,Z_5)=(-V,-W,X,U,Y),\qquad
S=\sum_i Z_i,\qquad
C=\sum_{i<j}[Z_i,Z_j],\qquad B=\tfrac12C .
\tag{CD1}
\]
Thus \(F_6=e^{hZ_1}\cdots e^{hZ_5}\). The symbol \(B\) here is a Lie-valued polynomial, not the magnetic parameter insertion of the planar chronology.

Writing \(T_Z=d\rho(Z)\), expansion of the represented product through second order gives
\[
\rho(F_6)=I+h\sum_iT_{Z_i}
+h^2\left\{\frac12\sum_iT_{Z_i}^2+
\sum_{i<j}T_{Z_i}T_{Z_j}\right\}+O(h^3).
\]
Subtracting half the square of its first term in the logarithm gives, in the Lie algebra,
\[
\boxed{\log F_6=hS+h^2B+O(h^3).}
\tag{CD2}
\]
This derives the sign from the actual word order. All local remainders in this note are uniform on bounded Lie-coordinate sets for the fixed group and representation.

GM's expansion \(w_A(e^Z)=Q(Z,Z)/4+O(|Z|^4)\) now yields
\[
\boxed{
w_A(F_6)
=\frac{h^2}{4}Q(S,S)
+\frac{h^3}{2}Q(S,B)+O(h^4)
=\frac{h^2}{4}Q(S,S)
+\frac{h^3}{4}Q(S,C)+O(h^4).}
\tag{CD3}
\]
The first five face costs have no odd exponential-coordinate terms. Therefore the entire first magnetic correction of the scaled Hamiltonian \(H/E\) is
\[
\boxed{
V^{\rm mag}_1=\frac14Q(S,C)
=\frac14\sum_{i<j<k}T_Q(Z_i,Z_j,Z_k),
\qquad T_Q(X,Y,Z)=Q(X,[Y,Z]).}
\tag{CD4}
\]
To verify the last identity, collect one distinct triple in \(Q(S,C)\). The contributions from its three pairs have signs \(+,-,+\), leaving one Cartan three-form. Repeated indices contribute zero by invariance of \(Q\).

This polynomial is nonzero for a non-Abelian simple Lie algebra: keep three increments \(X,Y,[X,Y]\), with the other two zero, to obtain a nonzero Cartan term. It is odd under simultaneous sign reversal of the increments, so its harmonic Gaussian expectation is zero. A first-order full-vacuum response would also involve the electric and density jets; it cannot be read from (CD4) alone. In particular, the independent-face calculation in which the first magnetic jet vanishes does not apply to this dependent chart.

## A bounded closure defect detects the bracket

Use the original globally bounded, equivariant mark \(q_\rho\) of [[weighted-character-scale-and-bounded-lie-sources|GM7–9]]. Put
\[
(\zeta_1,\ldots,\zeta_5)
=(-q_\rho(v),-q_\rho(w),q_\rho(x),q_\rho(u),q_\rho(y)),
\]
\[
\boxed{
\mathcal R=2q_\rho(F_6)-2\sum_i\zeta_i,\qquad
\mathcal B=2\sum_{i<j}[\zeta_i,\zeta_j].}
\tag{CD5}
\]
The factor two uses GM's linear normalization
\(q_\rho(e^{hZ})=hZ/2+O(h^3)\). Equation (CD2) consequently gives
\[
\boxed{
\mathcal R=h^2B+O(h^3),\qquad
\mathcal B=h^2B+O(h^4).}
\tag{CD6}
\]
Every term uses the same common-root port. Both quantities are smooth bounded Lie-valued functions of the six original face words, subject to CW's exact sixth-face relation.

Define the following bounded real physical scalar marks:
\[
\boxed{
\mathcal M=Q(\mathcal R,\mathcal B),\qquad
\mathcal M_{ij}=Q(\mathcal R,4[\zeta_i,\zeta_j])\quad(i<j).}
\tag{CD7}
\]
Equivariance of \(q_\rho\), covariance of the bracket and invariance of \(Q\) give simultaneous-conjugation invariance. Their first nonzero jets are
\[
\boxed{
h^{-4}\mathcal M\longrightarrow Q(B,B),\qquad
h^{-4}\mathcal M_{ij}\longrightarrow Q(B,[Z_i,Z_j]).}
\tag{CD8}
\]
Likewise \(h^{-4}Q(\mathcal R,\mathcal R)\to Q(B,B)\). The mixed mark \(\mathcal M\) is not asserted to be globally nonnegative; only its leading polynomial is a square.

These bracket-coupled marks vanish identically when the Lie algebra is Abelian. The defect \(\mathcal R\) alone need not vanish in an Abelian theory, because the bounded source is nonlinear; its leading quadratic bracket term then vanishes and higher source-coordinate terms remain. The Abelian control also retains the dependent sixth face and its coupled quadratic cost. Replacing it by an independent sixth Gaussian would change the comparison.

There is a simple pointwise test that does not depend on a vacuum average. Set \(U=X=Y=0\) and choose \([V,W]\ne0\). Then
\[
B=\tfrac12[V,W],\qquad
V^{\rm mag}_1=0,\qquad
h^{-4}\mathcal M\longrightarrow\tfrac14Q([V,W],[V,W])>0 .
\tag{CD9}
\]
The oriented source can detect the ordered two-factor bracket even where the cubic character cost itself vanishes.

## Use the covariance derived from the twelve original edges

In the coordinates \((U,V,W,X,Y)\), let \(A_5\) be the principal kinetic matrix derived from all twelve edge rows in [[closed-cube-raw-edge-kinetic-sewing|CK6]]. The dependent face fixes the magnetic quadratic form:
\[
\ell=(1,-1,-1,1,1)^{\mathsf T},\qquad
G_5=I+\ell\ell^{\mathsf T},\qquad
\Sigma G_5\Sigma=A_5.
\tag{CD10}
\]
Thus the harmonic operator is
\(-\nabla^{\mathsf T}A_5\nabla+\tfrac14X^{\mathsf T}G_5X\), with one copy per Lie-algebra color. Its Gaussian covariance \(\Sigma\) is the unique positive solution of
\(\Sigma G_5\Sigma=A_5\). It is not \(G_5^{-1}\), which would instead describe a separately chosen magnetic Gaussian likelihood.

The exact diagonalization and covariance evaluation are given in [[closed-cube-raw-edge-kinetic-sewing|CK9–11]]. The full harmonic vacuum is invariant under the common root Gauss action, so it supplies the physical harmonic expectation of the scalar marks.

In the ordered signed coordinates \(Z\) of (CD1), let \(K\) be the scalar covariance:
\(\mathbb E Z_i^aZ_j^b=K_{ij}\delta_{ab}\) in a \(Q\)-orthonormal color basis. The result is particularly simple:
\[
\boxed{
K_{ii}=1+\frac{\sqrt6}{3},\qquad
K_{13}=K_{31}=K_{25}=K_{52}=-1+\frac{\sqrt6}{3},\qquad
K_{ij}=-\frac{\sqrt6}{6}\ \text{for all other }i\ne j.}
\tag{CD11}
\]
The exceptional pairs are the two opposite-face pairs among these five faces. This covariance includes the dependent face's magnetic term and the coupled raw-edge kinetic action. Both were needed to select it.

## The forced scalar coefficient and signed pair responses

Let
\[
\mathcal F_Q=\sum_{a,b,c}Q(e_a,[e_b,e_c])^2>0,\qquad
J_{ij}=\begin{cases}1&i<j,\\-1&i>j,\\0&i=j.\end{cases}
\]
The symbol \(J\) denotes this antisymmetric \(5\times5\) coefficient matrix. Wick contraction and antisymmetry of the structure constants give
\[
\mathbb E_0 Q([Z_i,Z_j],[Z_k,Z_l])
=\mathcal F_Q(K_{ik}K_{jl}-K_{il}K_{jk}).
\]
The pairing within either bracket vanishes. Summing the remaining two pairings proves the general covariance formulas
\[
\boxed{
\mathbb E_0 Q(B,[Z_i,Z_j])
=\frac{\mathcal F_Q}{2}(KJK)_{ij},\qquad
\mathbb E_0 Q(B,B)
=\frac{\mathcal F_Q}{8}\operatorname{Tr}(J^{\mathsf T}KJK).}
\tag{CD12}
\]
The trace is \(\|K^{1/2}JK^{1/2}\|_{\rm HS}^2>0\). Thus the total coefficient is positive for any positive covariance \(K\) and non-Abelian simple \(\mathfrak g\); its value still depends on the actual covariance.

Substituting (CD11) gives
\[
\boxed{
\mathbb E_0 Q(B,B)=
\mathcal F_Q\left(2+\frac{2\sqrt6}{3}\right).}
\tag{CD13}
\]
The pairwise coefficients \(\mathbb E_0 Q(B,[Z_i,Z_j])/\mathcal F_Q\) are:

| Ordered pair \(ij\) | Coefficient |
|---|---:|
| \(12\) | \(1+\sqrt6/6\) |
| \(13\) | \(\sqrt6/3\) |
| \(14\) | \(0\) |
| \(15\) | \(-1+\sqrt6/6\) |
| \(23\) | \(1+\sqrt6/6\) |
| \(24\) | \(1-\sqrt6/6\) |
| \(25\) | \(0\) |
| \(34\) | \(2\sqrt6/3\) |
| \(35\) | \(1-\sqrt6/6\) |
| \(45\) | \(1+\sqrt6/6\) |

This table follows directly from matrix multiplication in \(\mathbb Q(\sqrt6)\). As a check, one half the sum of its entries is \(2+2\sqrt6/3\), because \(B=\tfrac12\sum_{i<j}[Z_i,Z_j]\). The \(15\) channel is strictly negative and two channels vanish. The source-resolved result is therefore stronger than choosing only a positive square after the calculation.

The constant \(\mathcal F_Q\) carries the declared Lie-bracket and metric normalization. No fourth-order representation invariant appears at this leading source order. Such invariants do enter subsequent magnetic and source jets, so (CD13) does not erase the full preparation data.

## Word order, coordinate changes and the actual-return boundary

As an explicit comparison of different ordered laws, reverse the five factors while keeping the reference \(\zeta_i\), \(\mathcal B\) and pairwise bracket marks in their original order. The linear sum \(S\) stays fixed and \(B\) changes sign. Thus the cubic cost in (CD3) and the leading mixed coefficients in (CD8) change sign; the squared-defect coefficient does not. Reversing factor order is not inversion of the whole word, and it is not CW's original closure law.

A passive change of word or coordinate convention must instead transport the entire exact face map and every source. Reversing both the comparison order and the reference bracket orientation preserves the resulting scalar coefficient. A local coordinate change with identity derivative leaves the first nonzero quadratic jet of \(\mathcal R\) and the first nonzero fourth-order jets of \(\mathcal M,\mathcal M_{ij}\) unchanged as tensors. The isolated cubic coefficient of a cost with a nonzero quadratic term can change by the pullback of that quadratic term; it is not an independent coordinate-invariant response. Changing individual connector paths also requires transporting the original joint marks, not merely the central cost.

Equations (CD8), (CD12) and (CD13) are local marked jets evaluated in the Gaussian vacuum selected by CK's full kinetic-plus-magnetic operator. Their upgrade to actual expectations is the separate fixed-cube localization theorem in [[closed-cube-bracket-source-and-the-actual-vacuum-return|CQ]]; the bounded unscaled marks must be multiplied only after taking sufficiently accurate compact vacuum approximants. CW's normalized magnetic integral alone does not justify that upgrade.

The calculation isolates a non-Abelian sourced consequence of the supplied dependent face. It selects neither the group nor the preparation or clock, and it does not establish a gapping effect, a three-dimensional bulk theory or a four-dimensional continuum return. Shared-cell sewing and the full physical source response remain further obligations.
