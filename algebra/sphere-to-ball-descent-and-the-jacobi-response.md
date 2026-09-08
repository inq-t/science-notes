# Sphere-to-Ball Descent and the Jacobi Response

Projection of a round sphere onto a coordinate ball pushes forward both a measure and a differential response. The resulting weighted ball operator has an inherited self-adjoint realization, constant ground state and exact polynomial spectrum. In the rank-two octonionic corner, its projection onto a complex qubit corner gives density proportional to the square of the determinant and a normalized response gap of eight. A hidden rotational drift can make the whole process non-detailed-balanced while leaving this local return detailed-balanced. The round law, selected context and generator normalization remain inputs; the ball coordinates describe states, not physical spatial positions.

## A many-to-one presentation with an explicit measure

Let \(n>k\ge1\), put \(m=n-k\), and assume \(m\ge2\). Write a point of the unit round sphere as
\[
(x,y)\in S^{n-1}\subset\mathbb R^k\oplus\mathbb R^m,
\qquad |x|^2+|y|^2=1.
\]
Give the sphere its normalized round measure \(\sigma\), and define
\[
q:S^{n-1}\longrightarrow\overline B^k,\qquad q(x,y)=x.
\tag{SB1}
\]
Over \(|x|<1\), the fiber is the sphere
\[
y=\sqrt{1-|x|^2}\,\omega,\qquad \omega\in S^{m-1}.
\]
At \(|x|=1\) it collapses to one point. The boundary is part of the image, not removed as an inadmissible state.

Put \(u=1-|x|^2\). In the coordinates \((x,\omega)\), the induced round metric has horizontal block \(I+xx^T/u\), vertical block \(u\,g_{S^{m-1}}\), and no mixed block. Its volume factor is
\[
u^{-1/2}u^{(m-1)/2}=u^{(m-2)/2}.
\]
Dividing the fiber sphere area by the whole sphere area therefore gives
\[
\boxed{
d\nu(x)=q_*\sigma(dx)=w_{n,k}(x)\,dx,\qquad
w_{n,k}(x)=
\frac{\Gamma(n/2)}
{\pi^{k/2}\Gamma((n-k)/2)}
(1-|x|^2)^{(n-k-2)/2}.
}
\tag{SB2}
\]
There is no additional boundary atom. The exponent is not obtained from fiber area alone: the horizontal Jacobian supplies the extra power \(u^{-1/2}\). The conditional law on each interior fiber is normalized round measure on \(S^{m-1}\).

The same density formula remains valid for \(m=1\), with a two-point interior fiber and exponent \(-1/2\). The connected-fiber and hidden-plane construction below uses \(m\ge2\).

## Pullback and forgetting have opposite directions

Pullback is the isometry
\[
U:L^2(\overline B^k,\nu)\longrightarrow L^2(S^{n-1},\sigma),
\qquad Uf=f\circ q.
\tag{SB3}
\]
It is injective. Its adjoint averages over the forgotten fiber:
\[
(U^*F)(x)=
\int_{S^{m-1}}
F\!\left(x,\sqrt{1-|x|^2}\,\omega\right)d\sigma_{m-1}(\omega).
\tag{SB4}
\]
Thus \(UU^*\) is the conditional expectation onto functions of \(x\). It has a genuine kernel, containing each hidden coordinate \(y_j\). The point projection \(q\) is many-to-one, while its observable pullback \(U\) is an embedding; these are different statements about different arrows.

The range of \(U\) is precisely the subspace invariant under rotations of the hidden \(\mathbb R^m\). Round spherical evolution preserves that subspace.

## The spherical generator returns a ball operator

Use the full spherical Laplacian \(\Delta_S\), with nonpositive spectrum, rather than the half-Laplacian convention. In the rank-two octonionic case, [[primitive-state-diffusion/inq|overlap refinement]] constructs this operator from the primitive-state pairing and repeated tensor-overlap comparisons: its full-carrier generators converge to \(-\Delta_{S^8}\), without choosing that differential expression first. The comparison rule, invariant sphere law and time normalization remain declared data. The coordinate identities are
\[
\Delta_Sx_i=-(n-1)x_i,\qquad
\nabla_Sx_i\cdot\nabla_Sx_j=\delta_{ij}-x_ix_j.
\tag{SB5}
\]
They follow by tangentially projecting the ambient coordinate vectors:
\(\nabla_Sx_i=e_i-x_i(x,y)\). The chain rule then gives
\[
\Delta_S(f\circ q)=(\mathcal L_{n,k}f)\circ q,
\]
\[
\boxed{
\mathcal L_{n,k}f
=\sum_{i,j=1}^k(\delta_{ij}-x_ix_j)\partial_i\partial_jf
-(n-1)\sum_{i=1}^kx_i\partial_if.
}
\tag{SB6}
\]
The diffusion co-metric is
\[
a(x)=I-xx^T.
\tag{SB7}
\]
It is positive definite in the open ball, with radial eigenvalue \(1-|x|^2\) and tangential eigenvalue one. Its radial degeneracy at the boundary is inherited from the projection.

Writing \(\alpha=(n-k-2)/2\), differentiation of (SB2) verifies
\[
\mathcal L_{n,k}f
=\frac1{w_{n,k}}\operatorname{div}
\left(w_{n,k}a\nabla f\right).
\tag{SB8}
\]
Indeed \(\sum_i\partial_i a_{ij}=-(k+1)x_j\) and
\(a\nabla\log w_{n,k}=-2\alpha x\), whose sum is the drift in (SB6).

## The extension is inherited, not a chosen absorbing wall

The round Laplacian commutes with hidden rotations. Therefore its self-adjoint realization reduces the range of \(U\). Define
\[
H_{n,k}=-U^*\Delta_SU
\tag{SB9}
\]
on the transported operator domain. Its closed Markov form is
\[
\mathcal E[f]
=\int_{S^{n-1}}|\nabla_S(Uf)|^2\,d\sigma,\qquad
\operatorname{Dom}\mathcal E
=\{f:Uf\in H^1(S^{n-1})\}.
\tag{SB10}
\]
For smooth functions on the closed ball, and in particular polynomials,
\[
\mathcal E[f,h]
=\int_{B^k}\nabla\overline f^{\,T}a\nabla h\,d\nu.
\tag{SB11}
\]
Thus \(H_{n,k}\) is the nonnegative self-adjoint realization of \(-\mathcal L_{n,k}\) determined by the sphere.

No absorbing Dirichlet condition is imposed on \(|x|=1\). Constants belong to the operator domain and satisfy \(H_{n,k}1=0\). For polynomials the weighted normal flux tends to zero automatically:
\[
w_{n,k}\,a\,\mathbf n
\quad\text{is proportional to}\quad
(1-|x|^2)^{m/2}\mathbf n,
\]
where \(\mathbf n=x/|x|\) on concentric spheres approaching the boundary. This vanishing follows from the inherited measure and co-metric, not from requiring the boundary values of the polynomial to vanish.

## Orthogonal polynomials determine the entire spectrum

Let \(\mathcal P_\ell\) be the polynomials of total degree at most \(\ell\), viewed in \(L^2(\nu)\), and set
\[
\mathcal V_\ell=\mathcal P_\ell\ominus\mathcal P_{\ell-1},
\qquad \mathcal P_{-1}=\{0\}.
\]
These spaces have dimensions
\(\dim\mathcal V_\ell=\binom{k+\ell-1}{\ell}\). With the Euler operator \(D=x\cdot\nabla\), formula (SB6) is
\[
\mathcal L_{n,k}=\Delta_x-D^2-(n-2)D.
\tag{SB12}
\]
It preserves every \(\mathcal P_\ell\), and on a homogeneous leading term of degree \(\ell\) it acts as
\(-\ell(\ell+n-2)\), up to lower-degree terms.

Symmetry in \(L^2(\nu)\) also makes \(\mathcal V_\ell\) invariant: its pairing with \(\mathcal P_{\ell-1}\) remains zero because the latter is invariant. For \(f\in\mathcal V_\ell\),
\[
\bigl[\mathcal L_{n,k}+\ell(\ell+n-2)\bigr]f
\in\mathcal P_{\ell-1}\cap\mathcal V_\ell=\{0\}.
\]
Consequently
\[
\boxed{
H_{n,k}|_{\mathcal V_\ell}
=\ell(\ell+n-2)I,\qquad \ell=0,1,2,\ldots.
}
\tag{SB13}
\]

Polynomials are uniformly dense in the continuous functions on the closed ball, and continuous functions are dense in \(L^2(\nu)\). Hence the orthogonal sum of the \(\mathcal V_\ell\) is the entire Hilbert carrier. The eigenvalues in (SB13), with the displayed finite multiplicities, are therefore the exact spectrum.

This also proves the needed core statements. If \(f=\sum_\ell f_\ell\), \(f_\ell\in\mathcal V_\ell\), then
\[
\begin{aligned}
f\in\operatorname{Dom}\mathcal E
&\Longleftrightarrow
\sum_\ell\ell(\ell+n-2)\|f_\ell\|^2<\infty,\\
f\in\operatorname{Dom}H_{n,k}
&\Longleftrightarrow
\sum_\ell[\ell(\ell+n-2)]^2\|f_\ell\|^2<\infty.
\end{aligned}
\tag{SB14}
\]
Finite polynomial sums converge in the respective form and operator graph norms. The choice of extension has not been hidden in a formal differential expression.

In particular the ground space is precisely the constants, and
\[
\boxed{
H_{n,k}\ge(n-1)(I-P_1),\qquad
\operatorname{Var}_\nu(f)\le\frac1{n-1}\mathcal E[f].
}
\tag{SB15}
\]
Coordinate functions attain equality. For a direct check,
\(\mathbb E_\nu x_i=0\), \(\mathbb E_\nu x_i^2=1/n\), and
\(\mathcal E[x_i]=(n-1)/n\). At the next degree,
\(\mathcal L_{n,k}(|x|^2-k/n)=-2n(|x|^2-k/n)\).

## A non-detailed-balanced whole can have this same local return

For \(m\ge2\), choose the hidden-plane rotation
\[
Z=y_1\partial_{y_2}-y_2\partial_{y_1},
\qquad \omega\ne0,\qquad
\mathcal L_{\mathrm{whole}}=\Delta_S+\omega Z.
\tag{SB16}
\]
The rotation preserves \(\sigma\), commutes with \(\Delta_S\), and is skew-adjoint. Thus
\[
e^{t\mathcal L_{\mathrm{whole}}}
=e^{t\Delta_S}e^{\omega tZ},\qquad t\ge0,
\tag{SB17}
\]
is a measure-preserving Markov semigroup, while its generator's adjoint is
\(\Delta_S-\omega Z\), not \(\mathcal L_{\mathrm{whole}}\). The whole process fails detailed balance.

But \(Z(f\circ q)=0\). Therefore
\[
\boxed{
e^{t\mathcal L_{\mathrm{whole}}}U
=Ue^{t\mathcal L_{n,k}},\qquad
U^*e^{t\mathcal L_{\mathrm{whole}}}U
=e^{t\mathcal L_{n,k}}.
}
\tag{SB18}
\]
The local semigroup is self-adjoint in \(L^2(\nu)\), hence detailed-balanced. The same projection determines its law and its generator; a different local process was not fitted after taking the quotient.

This is a typed example of invisible whole-level circulation and a reversible local Markov law. Here “reversible” means detailed balance, not unitary heat evolution. The positive operator \(H_{n,k}\) separately supplies a Hilbert clock \(e^{-itH_{n,k}}\), which need not act by automorphisms of the ball's function algebra and is not a spacetime translation merely by being unitary.

The rotation itself is invertible and does not erase information. Finite-time spherical heat is contractive but linearly injective; the genuine kernel in this construction belongs to the fiber averaging \(U^*\). Neither the heat law nor its representation asserts an ontologically random selection or constructs an obtained record. The chosen round diffusion, hidden drift and clock duration remain modeling data; (SB18) does not derive the round structure from asymmetry alone.

## The rank-two octonionic specialization

The [[exceptional-state-comparison/peirce-context-averaging-and-the-emergent-qubit-process|selected Peirce corner]] is
\[
\mathcal P=\mathbb Rp\oplus\mathbb R^9
\cong\mathfrak h_2(\mathbb O),
\]
where \(p\) has Albert trace two and is the unit of this corner. Its primitive idempotents are
\[
e_v=\frac{p+v}{2},\qquad |v|=1,\qquad v\in S^8.
\tag{SB19}
\]
Indeed \(v^2=p\) in the spin factor, so \(e_v^2=e_v\), and its Albert trace is one. These are primitive elements of the rank-two corner, not the rank-two unit \(p\) itself.

The selected complex context retains a three-plane in \(\mathbb R^9\). Its positive Jordan retraction sends
\[
e_v\longmapsto\rho_x=\frac{I+x\cdot\sigma}{2},
\qquad x=q(v)\in\overline B^3.
\tag{SB20}
\]
The retained matrix has ordinary trace one. For a uniformly distributed \(v\) on the unit \(S^8\), (SB2) and (SB15) become
\[
\boxed{
d\nu(x)=\frac{105}{32\pi}(1-|x|^2)^2\,dx,\qquad
\operatorname{gap}H_{9,3}=8.
}
\tag{SB21}
\]
The fiber over an interior qubit state is \(S^5\). The state-space ball is continuous all the way to its rank-one boundary, which has zero \(\nu\)-measure but is still in the support.

This is not the earlier operation averaging three-plane retractions to obtain the finite qubit depolarizer with coefficient \(1/3\). Here the projection is fixed, the whole primitive elements carry round measure, and the Laplacian acts on square-integrable functions of their retained state parameters. In particular its infinitely many polynomial modes are not the three traceless directions of \(M_2(\mathbb C)\).

[[octonionic-hopf-descent-and-the-complex-purification|The Hopf factorization]]
now supplies a common parent for this return and a complex purification:
\(S^{15}\to S^8\to\overline B^3\) is exactly the Gram readout of a selected
\(\mathbb C^{2\times4}\) amplitude. The map transports the round measure and
\(\Delta_{15}/4\) to the same law and generator here.
[[purification-descent-and-the-matrix-response|Matrix purification descent]]
extends the latter construction to every finite matrix size, with a
determinant-weighted law and a complete polynomial spectrum.

## The determinant potential agrees, but the response metrics differ

Put \(u_x=I+x\cdot\sigma=2\rho_x\). Then
\(\det u_x=1-|x|^2\), and the [[positive-cone-processes-and-the-complex-corner|cone potential, PC5]] restricts to
\[
\mathcal F(x)=-\frac12\log(1-|x|^2).
\]
For the density in (SB21),
\[
\boxed{
-\log w_{9,3}(x)
=4\mathcal F(x)-\log\!\left(\frac{105}{32\pi}\right).
}
\tag{SB22}
\]
The sign matters: it is the **negative** logarithm of the Lebesgue density that gives the positive barrier. The density vanishes, rather than diverges, near the pure-state boundary.

Nevertheless equality of potentials does not identify response operators. In the affine Bloch coordinates,
\[
\operatorname{Hess}\mathcal F
=\frac{I}{1-|x|^2}
+\frac{2xx^T}{(1-|x|^2)^2},
\]
\[
(\operatorname{Hess}\mathcal F)^{-1}
=(1-|x|^2)
\left(I-\frac{2xx^T}{1+|x|^2}\right),
\tag{SB23}
\]
whereas the inherited diffusion co-metric is \(a=I-xx^T\). Away from \(x=0\), even their radial-to-tangential eigenvalue ratios differ. The spherical kinetic response was not obtained by inverting the determinant Hessian.

The gap is also not an eigenvalue of the forgetting defect \(I-UU^*\). That projection defect vanishes on every retained function \(Uf\), whereas the returned Laplacian distinguishes nonconstant retained functions. The projection and the whole generator are jointly specified data; a many-to-one map alone does not select the latter.

[[jordan-covariance-and-the-entropy-weighted-ball|Jordan covariance and weighted curvature]] identify the co-metric with symmetrized qubit covariance and its inverse with the SLD metric. The same hidden-fiber volume fixes the drift and a sharp weighted-curvature inequality. The [[finite-entropy-cost-and-rank-changing-readout|conditional entropy deficit]] separately quantifies the information lost by \(U^*\); it acts on incoming density distinctions, not on the same directions as the retained differential response.

The normalization of the sphere and its rotational Casimir fixes the numerical gap in (SB21). Replacing \(\Delta_S\) by \(\lambda\Delta_S\), \(\lambda>0\), multiplies that gap by \(\lambda\); choosing the half-Laplacian would give four. The whole sphere already has gap eight, and the quotient retains modes attaining it. The conditional measure and generator are constrained once the whole sphere law and the selected projection are given, but they do not supply a physical duration or explain why that whole law is selected.

The coordinates \(x\) are Bloch parameters of a retained state, not three physical spatial coordinates. The operator acts on distinctions among those parameters in \(L^2(\nu)\). Its internal response edge of eight is neither a Yang–Mills vacuum-complement theorem nor a Lorentz mass Casimir.

[[directed-analytic-realization/sphere_ball_descent_receipt.py|The shared sphere-ball receipt]] checks finite polynomial descent, moments, response identities and hidden rotations. [[directed-analytic-realization/sphere-ball-descent-receipt-output.txt|Its output]] is a finite consistency check; the spectral decomposition and inherited domain above establish the general operator statement.
