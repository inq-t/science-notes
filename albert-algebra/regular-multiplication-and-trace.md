# Regular Multiplication and Trace

Multiplication by an Albert-algebra element is a self-adjoint operator on its trace Hilbert space. This gives an injective positive linear realization on a 27-dimensional complex carrier, with explicit trace formulas. It preserves the automorphism action but generally does not preserve the Jordan product; its full matrix carrier therefore contains distinctions absent from the original Jordan algebra.

On \(\mathcal H_J=J\otimes_{\mathbb R}\mathbb C\), let \(L_xy=x\circ y\). Associativity of the trace form makes \(L_x\) self-adjoint for real \(x\), and \(L_x\mathbf1=x\) proves injectivity. For a Jordan automorphism \(g\), its complex-linear unitary implementation satisfies
\[
U_gL_xU_g^*=L_{gx}.
\tag{EC9}
\]

The [[library/general-representation-theory-of-jordan-algebras/inq|Jordan representation notion]] includes regular multiplication. It does not assert an embedding into an associative algebra equipped with the symmetrized product. [[library/a-note-on-the-exceptional-jordan-algebra/inq|Albert's non-speciality theorem]] excludes such a faithful product-preserving embedding for this exceptional algebra; generally \(L_{x^2}\ne L_x^2\).

Choose a Jordan frame diagonalizing \(x\), with eigenvalues \(\lambda_1,\lambda_2,\lambda_3\). On its three diagonal directions \(L_x\) has eigenvalues \(\lambda_i\); on each eight-dimensional off-diagonal Peirce space it has eigenvalue \((\lambda_i+\lambda_j)/2\). Thus \(x\ge0\) implies \(L_x\ge0\), and
\[
\operatorname{Tr}_{\mathcal H_J}L_x=9\operatorname{tr}_Jx,\qquad
\operatorname{Tr}_{\mathcal H_J}L_x^2
=3\operatorname{tr}_J(x^2)+2(\operatorname{tr}_Jx)^2.
\tag{EC13}
\]
Indeed, summing the Peirce eigenvalues gives the first identity. Squaring them gives
\(\sum_i\lambda_i^2+2\sum_{i<j}(\lambda_i+\lambda_j)^2
=3\sum_i\lambda_i^2+2(\sum_i\lambda_i)^2\).

In particular the trace-free Jordan carrier and its regular image have
\(\|L_x\|_{\rm HS}^2=3\|x\|_J^2\) for \(x\in J_0\). This normalization does not extend by declaration to every tangent in \(M_{27}(\mathbb C)\).

For a real trace-orthonormal basis \((e_a)\), the same trace identity determines
\[
\sum_a L_{e_a}^2=3I+6P_{\mathbf1},\qquad
P_{\mathbf1}x=\frac{\operatorname{tr}_Jx}{3}\mathbf1.
\]
To see this, evaluate its quadratic form as \(\sum_a\|L_xe_a\|^2=\operatorname{Tr}L_x^2\) and polarize. The vector \(\mathbf1\), its rank-one projection \(P_{\mathbf1}\), and the matrix identity \(I=L_{\mathbf1}\) have different types.

Finally, commutators \([L_a,L_b]\) are Jordan derivations. This is a Jordan-identity consequence, independent of a matrix representation preserving products. It permits infinitesimal automorphisms to be computed in the regular carrier without replacing the exceptional product by an associative one.
