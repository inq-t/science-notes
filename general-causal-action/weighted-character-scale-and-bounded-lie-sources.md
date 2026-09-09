# Weighted Character Scale and Bounded Lie Sources

A faithful unitary representation supplies both a positive identity cost and a bounded Lie-valued source. Their normalizations have different roles: the actual weighted character Hessian fixes the confinement scale, while projection of the odd matrix part fixes the source's linear Taylor coefficient. Keeping both permits the four-face source calculation to be compared across compact simple groups without replacing a reducible preparation's cost or importing quaternion constants.

**Status: exact representation identities, fixed-group scale conversion and bounded source construction.** The representation and positive preparation weight remain declared data. [[general-group-preparation-and-the-casimir-return|GG]] supplies faithful representations of every compact connected simple global form and the actual weighted character costs; [[local-incidence-preparations-and-the-gauge-transfer|LI18]] retains their finite spatial Hamiltonian.

## Keep the actual weighted character Hessian

Let \(G\) be compact and connected with simple Lie algebra \(\mathfrak g\), \(d=\dim\mathfrak g\), and let \(Q\) be an Ad-invariant positive inner product. Fix a faithful unitary representation \(\rho:G\to U(n)\), write \(T_X=d\rho(X)\), and take a Hermitian \(A>0\) commuting with \(\rho(G)\). Define
\[
W_A(U)=\operatorname{Re}\operatorname{Tr}[A(I-\rho(U))],\qquad
Q_A(X,Y)=-\operatorname{Re}\operatorname{Tr}(AT_XT_Y).
\tag{GM1}
\]
The form \(Q_A\) is real symmetric, positive definite and Ad-invariant. Symmetry follows by taking the trace of \(A[T_X,T_Y]\), which is zero. Positivity is
\(Q_A(X,X)=\operatorname{Tr}(AT_X^\dagger T_X)>0\) for \(X\ne0\), using \(A>0\) and injectivity of \(d\rho\). Simplicity therefore gives
\[
\boxed{Q_A=I_AQ,\qquad I_A>0.}
\tag{GM2}
\]
For a \(Q\)-orthonormal basis \(e_a\),
\(I_A=d^{-1}\sum_a\operatorname{Tr}(AT_{e_a}^\dagger T_{e_a})\).
Write \(I_\rho=I_I\) for the unweighted representation index.

Because \(A\) commutes with the representation,
\[
W_A(U)=\frac12\|(\rho(U)-I)A^{1/2}\|_{\rm HS}^2\ge0.
\]
It vanishes exactly at \(U=e\): equality forces \(\rho(U)=I\), and \(\rho\) is faithful. Moreover \(W_A(U^{-1})=W_A(U)\). Exponential expansion gives
\[
\boxed{
W_A(e^X)=\frac{I_A}{2}Q(X,X)
-\frac1{24}\operatorname{Re}\operatorname{Tr}(AT_X^4)
+O_{G,\rho,A,Q}(|X|^6).}
\tag{GM3}
\]
All odd terms vanish. The quadratic coefficient is scalar; the fourth-order trace is not determined by it.

This includes a faithful reducible representation. In GG20 the actual \(A=\overline A\) has positive scalar blocks \(a_r\), so \(I_A=\sum_r m_ra_rI_{\rho_r}\). The unweighted cost corresponds to \(A=I\). Substituting it for a non-scalar returned preparation weight changes the member of the family.

## Derive the physical scale before comparing coefficients

On the homogeneous four-face patch, retain the actual raw-edge electric Casimir and set
\[
H_{\kappa,g,A}
=\kappa\,\mathsf C_{\rm raw,Q}+g\sum_{p=1}^4W_A(U_p),
\qquad \kappa,g>0.
\]
Here the common coefficients and weight specify a homogeneous member of the finite incidence construction; heterogeneous returned cell weights are not silently homogenized. Define
\[
\boxed{
g_{\rm eff}=2I_Ag,\qquad
h=(\kappa/g_{\rm eff})^{1/4},\qquad
E=\sqrt{\kappa g_{\rm eff}}=\kappa/h^2.}
\tag{GM4}
\]
Then exactly
\[
\frac{H_{\kappa,g,A}}E
=h^2\mathsf C_{\rm raw,Q}
+\frac1{h^2}\sum_p\frac{W_A(U_p)}{2I_A}.
\tag{GM5}
\]
Writing \(U_p=e^{hX_p}\), the leading operator is
\[
\mathcal O_G
=-\sum_{p,q}(A_2)_{pq}\,Q(\nabla_p,\nabla_q)
+\frac14\sum_pQ(X_p,X_p),\qquad
A_2=4I-\operatorname{Adj}_{2\times2}.
\]
Its mode frequencies are \((\sqrt2,2,2,\sqrt6)\), each with \(d\) color components. Their Gaussian component variances are \(\omega_i\), and their vacuum energy contribution is \(d\omega_i/2\). Physical duration is the scaled duration divided by \(E\).

For the original fundamental \(SU(2)\) convention \(T_a=-i\sigma_a/2\), \(Q(e_a,e_b)=\delta_{ab}\) and \(A=I\), one has \(I_\rho=1/2\). Thus \(g_{\rm eff}=g\), recovering the earlier normalization. This check does not set \(I_A=1/2\) for another group, metric or preparation.

Under a change of metric convention \(Q'=cQ\), the same electric operator requires \(\kappa'=c\kappa\), while \(I_A'=I_A/c\). Hence
\[
E'=E,\qquad h'=\sqrt c\,h.
\tag{GM6}
\]
The physical scale is unchanged. In the corresponding orthonormal bases the structure constants scale by \(c^{-1/2}\), so their first-order combination with \(h\) is unchanged as well. A rational coefficient in the source contact supplies no absolute mass unit.

## Project the odd matrix part onto the represented Lie algebra

Use the real Hilbert–Schmidt inner product on skew-Hermitian matrices and let
\(\Pi_\rho:\mathfrak u(n)\to d\rho(\mathfrak g)\) be its orthogonal projection. Define
\[
B_\rho(U)=\frac{\rho(U)-\rho(U)^\dagger}{2},\qquad
\boxed{
q_\rho(U)=\frac12(d\rho)^{-1}\Pi_\rho B_\rho(U).}
\tag{GM7}
\]
The inverse is only on the represented Lie subspace, where \(d\rho\) is injective. It is not an inverse to the group representation or to the exponential map.

Equivalently, for a \(Q\)-orthonormal basis,
\[
\boxed{
q_\rho(U)
=-\frac1{4I_\rho}\sum_a
\operatorname{Re}\operatorname{Tr}
\!\left[T_{e_a}\bigl(\rho(U)-\rho(U)^\dagger\bigr)\right]e_a.}
\tag{GM8}
\]
The index here is the unweighted \(I_\rho\), because (GM7) uses the unweighted Hilbert–Schmidt projection. The cost index \(I_A\) remains in (GM4).

The map is real, globally smooth and bounded. Unitary conjugation preserves the represented Lie subspace and its orthogonal complement, so
\[
q_\rho(aUa^{-1})=\operatorname{Ad}_a q_\rho(U),\qquad
q_\rho(U^{-1})=-q_\rho(U).
\]
Its exponential Taylor expansion is
\[
\boxed{
q_\rho(e^{hX})
=\frac h2X+
\frac{h^3}{12}(d\rho)^{-1}\Pi_\rho(T_X^3)+O(h^5).}
\tag{GM9}
\]
Only the linear term is universal. In the original \(SU(2)\) fundamental convention, (GM7) is exactly the quaternion vector.

This map need not separate group elements and can vanish away from the identity. For example, the original \(SU(2)\) mark vanishes at both central elements. The faithful character cost still has its unique identity well, and the full faithful matrix-source algebra of [[prepared-readout-algebra-and-physical-source-completeness|RA]] remains available. No projection of the physical observable algebra onto the Lie-valued marks is made.

## Complete based words give bounded quadratic and oriented marks

Keep the four common-root comb face words \(U_p\) and the fixed Hadamard matrix \(O\). Put
\[
\mathbf Q_i=\sum_pO_{pi}q_\rho(U_p),\qquad
T_G(X,Y,Z)=Q(X,[Y,Z]).
\]
All \(\mathbf Q_i\) transform under the same root adjoint action. Consequently
\[
Q(\mathbf Q_i,\mathbf Q_j),\qquad
T_G(\mathbf Q_i,\mathbf Q_j,\mathbf Q_k)
\tag{GM10}
\]
are real bounded gauge-invariant physical sources with the original connector paths. In the scaled chart,
\(\mathbf Q_i=hY_i/2+O(h^3)\). Quadratic and cubic source normalizations are therefore \(4/h^2\) and \(8/h^3\), respectively.

[[all-group-oriented-kinetic-jet-and-source-lift|The all-group kinetic calculation]] derives their common first correction from the actual Lie brackets. [[fixed-group-compact-vacuum-and-oriented-source-return|The fixed-group compact return]] justifies multiplication of the rescaled marks in the moving vacuum. The construction retains the declared group, representation, weight, metric, graph and physical clock. It does not select those inputs or transport an \(SU(2)\) fourth-order gap coefficient to a different group.
