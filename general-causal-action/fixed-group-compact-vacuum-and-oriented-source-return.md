# Fixed-Group Compact Vacua Realize the Oriented Source Lift

For every fixed compact connected group with simple Lie algebra, the four-face oriented source jets belong to an actual compact Hamiltonian and its actual vacuum. Faithfulness of the weighted character cost gives a unique magnetic well, while the raw chord rows make the operator elliptic on the smooth \(G^4\) cover. Equivariant localization and arbitrarily accurate vacuum quasimodes then justify the scaled quadratic, cubic and composite readouts. The constants may depend on the group, metric and preparation data; no uniform group or spatial limit is asserted.

**Status: proved fixed-group compact vacuum and first-order source return.** [[weighted-character-scale-and-bounded-lie-sources|GM]] fixes the weighted cost, effective scale and bounded Lie-algebra-valued mark. [[all-group-oriented-kinetic-jet-and-source-lift|AJ]] supplies the complete polynomial normal form. [[lie-bracket-source-contact-and-the-positive-comparison-test|The Lie contact]] owns its algebraic and Gaussian coefficient. The argument below extends [[compact-source-normalization-and-the-nonlinear-return|CS's actual-vacuum method]] without using a singular orbit-space chart or a previously computed \(SU(2)\) gap correction.

## Fix the global group and the actual cost

Let \(G\) be compact and connected, with simple Lie algebra \(\mathfrak g\), dimension \(d\), and a positive \(\operatorname{Ad}G\)-invariant metric \(Q\). Fix a faithful finite-dimensional unitary representation \(\rho\), and a positive definite Hermitian matrix \(A\) commuting with \(\rho(G)\). Set
\[
W_A(U)=\operatorname{Re}\operatorname{Tr}A(I-\rho(U)),\qquad
-\operatorname{Re}\operatorname{Tr}A\,d\rho(X)d\rho(Y)=I_AQ(X,Y).
\tag{GV1}
\]
Simplicity makes the invariant quadratic form a scalar multiple of \(Q\), and faithfulness gives \(I_A>0\). This includes the positive block weights of [[general-group-preparation-and-the-casimir-return|GG20]]; a reducible preparation is not replaced by an unweighted irreducible character.

On the same twelve-edge square patch, impose gauge transformations at all nine vertices and use the same comb connectors. The Hamiltonian and its actual scale are
\[
H_g=\kappa\sum_e C_{e,Q}+g\sum_{p=1}^4W_A(P_p),\qquad
g_{\mathrm{eff}}=2I_Ag,\quad
h=(\kappa/g_{\mathrm{eff}})^{1/4},\quad
E_h=\sqrt{\kappa g_{\mathrm{eff}}}=\kappa h^{-2}.
\tag{GV2}
\]
Here \(g\) is the raw cost strength. Equivalently, the potential is \(g_{\mathrm{eff}}\sum_p W_A(P_p)/(2I_A)\). Taylor expansion gives
\[
\frac{W_A(\exp x)}{2I_A}=\frac14|x|_Q^2+O(|x|^4).
\]
The absence of odd powers follows from unitarity and taking the real part.

Moreover
\[
W_A(U)=\frac12\operatorname{Tr}
A(I-\rho(U))^*(I-\rho(U))\ge0 .
\]
Since \(A>0\), equality requires \(\rho(U)=I\), hence \(U=I\). Global faithfulness, rather than merely injectivity of \(d\rho\), excludes additional central minima.

## Ellipticity holds on a smooth cover

Tree gauge identifies the full physical Hilbert space with
\[
\boxed{\mathcal H_{\mathrm{phys}}
=L^2(G^4,dP)^{\operatorname{Ad}G}.}
\tag{GV3}
\]
This is simultaneous conjugation, not four separate class-function spaces. The group-valued comb map in [[comb-face-transport-and-the-first-nonlinear-jet|FJ1]] uses only multiplication and inversion:
\[
P_{i,j}=H_{i,j-1}H_{i,j}^{-1},\qquad
H_{i,j}=P_{i,j}^{-1}\cdots P_{i,1}^{-1}.
\]
It is a global smooth diffeomorphism preserving product Haar measure for every compact \(G\).

The exact raw rows of FJ3–4 also make sense for this group, with each cross product replaced by the Lie bracket in their local jets. In particular the horizontal chord rows are
\[
Z_{i,1,T}=-\mathcal R_{i,1,T}+\mathcal L_{i,2,T},
\qquad Z_{i,2,T}=-\mathcal R_{i,2,T}.
\]
Left and right gradients have the same \(Q\)-norm. Solving this triangular system column by column gives, pointwise,
\[
\boxed{
\sum_{p,a}|\mathcal R_{p,T_a}f|^2
\le3\sum_{\text{horizontal chords }e,a}|Z_{e,T_a}f|^2
\le3\sum_{e,a}|Z_{e,T_a}f|^2,}
\tag{GV4}
\]
where \(T_a\) is \(Q\)-orthonormal. Smoothness and compactness give the reverse bound with a finite constant. The raw form is therefore uniformly elliptic on the smooth compact cover \(G^4\). This is not an assertion of ellipticity in singular quotient coordinates.

Every row is divergence-free in product Haar measure: its variable adjoint coefficient depends only on group coordinates that the row leaves fixed, exactly as in FJ4–5. Thus the cover operator is the nonnegative symmetric sum of squares plus the smooth real potential. Its closed form has a self-adjoint elliptic realization with compact resolvent. The cover is connected. The variational ground vector can be chosen strictly positive by elliptic positivity, and the ground-state form identity makes its eigenline simple: a second ground vector divided by the positive one has zero gradient. Group invariance then makes this actual ground vector simultaneously \(\operatorname{Ad}G\)-invariant. It is also the physical vacuum.

## The unique well separates the actual vacuum

All four face costs vanish only at the identity tuple. In a product exponential chart around that point, the potential has a positive definite Hessian, and the Haar density is smooth, positive and even. All charts, cutoffs and density maps below are equivariant under simultaneous conjugation.

After \(x=hX\) and division by \(E_h\), the leading oscillator is
\[
\mathcal O_G=-\partial^{\mathsf T}(A_2\otimes I_d)\partial
+\frac14|X|^2,\qquad A_2=4I-\operatorname{Adj}_{2\times2}.
\]
In the same Hadamard modes as FJ,
\[
\omega=(\sqrt2,2,2,\sqrt6),\qquad
\Omega=C_G\exp\!\left[-\sum_{i=0}^3\frac{|Y_i|_Q^2}{4\omega_i}\right],
\qquad e_0=\frac d2\sum_i\omega_i .
\tag{GV5}
\]
The Gaussian is invariant for every \(G\). On the full smooth cover, the first oscillator excitation above \(e_0\) has energy \(\sqrt2\). This cover separation already suffices for all vacuum estimates below; no second-order physical-gap coefficient is imported.

Here is a direct localization argument for that separation. Choose invariant IMS cutoffs at radius \(\delta_h=h^\alpha\), \(0<\alpha<1\). Uniform cover ellipticity bounds the scaled localization error by \(C h^2/\delta_h^2=o(1)\). Outside the inner chart ball, the unique-well property and its positive Hessian bound the scaled potential below by \(c\delta_h^2/h^2\), which diverges. Inside, the principal matrix approaches \(A_2\otimes I_d\), the density approaches its constant value, and the potential has its quadratic Taylor form. The local form therefore converges to that of \(\mathcal O_G\), with vanishing relative and additive error on bounded-energy spaces.

For the lower min–max estimate, extend the inside Dirichlet functions by zero in \(\mathbb R^{4d}\); the outside block escapes every fixed energy interval. For the upper estimate, cut off a fixed finite collection of oscillator eigenvectors and use their Gaussian tails. Their Gram and energy matrices converge. This proves convergence of each fixed ordered cover eigenvalue to its oscillator value, including multiplicities. In particular, for sufficiently small \(h\),
\[
\boxed{
|\widehat E_0(h)-e_0|=o(1),\qquad
\operatorname{dist}\!\left(\widehat E_0(h),
\operatorname{spec}(\widehat H_h)\setminus\{\widehat E_0(h)\}\right)
\ge\frac{\sqrt2}{2},}
\tag{GV6}
\]
where \(\widehat H_h=H_g/E_h\). Restriction to the physical invariant subspace cannot introduce an additional eigenvalue into this separated interval.

## Arbitrary-order quasimodes precede source multiplication

Let \(\rho_{\mathrm{Haar}}(x)\) be the local density and \(\chi\) a fixed invariant cutoff supported strictly inside the exponential chart, equal to one near the well. Define
\[
\mathcal J_hu(x)=h^{-2d}\rho_{\mathrm{Haar}}(x)^{-1/2}
\chi(x)\,u(x/h).
\tag{GV7}
\]
The dimension is \(4d\), so \(h^{-2d}\) is the half-density dilation. Inner products on every fixed polynomial-Gaussian family are preserved up to errors smaller than any prescribed power of \(h\).

All operator coefficients and the cost are smooth to arbitrary order. Taylor expansion gives polynomial differential jets \(V_{r,G}\), with \(V_{0,G}=\mathcal O_G\), and for each fixed polynomial-Gaussian \(u\) and integer \(M\),
\[
\left\|\widehat H_h\mathcal J_hu-
\mathcal J_h\sum_{r=0}^Mh^rV_{r,G}u\right\|
\le C_{G,Q,\rho,A,M,u}h^{M+1}.
\]
Polynomial Gaussian moments control the interior Taylor remainder. Derivatives of \(\chi\) act at \(|X|\asymp h^{-1}\), where all such tails decay faster than any prescribed power.

Solve the vacuum eigen-equation and normalization recursively. Each step involves a polynomial Gaussian, its scalar solvability condition, and the inverse of \(K_0=\mathcal O_G-e_0\) off the simple vacuum. A polynomial has finite Hermite expansion, so this inverse remains an algebraic polynomial-Gaussian operation. The construction commutes with the Gauss action. The separation (GV6) converts every finite-order residual into an actual vacuum norm approximation of the same order, after fixing the positive overlap.

The even local potential and density make \(V_{1,G}\) precisely AJ's odd kinetic jet. Its expectation in \(\Omega\) vanishes. AJ's real formally skew operator satisfies \([K_0,S_{1,G}]=-V_{1,G}\), hence uniqueness of the orthogonal vacuum correction gives
\[
\boxed{
\widehat E_0(h)=e_0+O(h^2),\qquad
\psi_h=\mathcal J_h\bigl(\Omega+hS_{1,G}\Omega\bigr)+O(h^2).}
\tag{GV8}
\]
Arbitrarily higher finite orders are available before truncating this statement. No analytic convergence of an infinite series or closure of \(S_{1,G}\) is needed.

## Fixed compact marks realize the centered source vectors

Use GM's smooth bounded equivariant Lie mark \(q_\rho:G\to\mathfrak g\), normalized by
\[
q_\rho(\exp x)=x/2+O(|x|^3),\qquad
q_\rho(U^{-1})=-q_\rho(U).
\]
Its normalization uses the unweighted representation trace metric, separately from \(I_A\) in the actual cost. Put \(\mathbf Q_i=\sum_pO_{pi}q_\rho(P_p)\), so \(\mathbf Q_i(hX)=hY_i/2+O(h^3)\).

For a real invariant homogeneous quadratic \(F\), AJ gives the homogeneous cubic
\[
D_G(F)=\Omega^{-1}[S_{1,G},M_F]\Omega .
\]
The fixed bounded compact observable and its scaled jet are
\[
\boxed{
\mathcal L_F=F(\mathbf Q)+2D_G(F)(\mathbf Q),\qquad
\frac4{h^2}\mathcal L_F=F+hD_G(F)+O(h^2).}
\tag{GV9}
\]
This concerns all ten quadratic comparisons on four copies of the simple adjoint representation. Their images lie in the four distinct-mode bracket cubics; it is not a classification of all invariant cubic polynomials of \(G\).

Let \(m_F=\langle F\rangle_{\Omega^2}\), \(\sigma_F^2=\operatorname{Var}_{\Omega^2}(F)>0\), and center and normalize \(\mathcal L_F\) in the actual compact vacuum. Then
\[
\boxed{
\zeta_{F,h}
=\mathcal J_h(I+hS_{1,G})
\frac{(F-m_F)\Omega}{\sigma_F}+O(h^2),}
\tag{GV10}
\]
and the mean and variance of \(4\mathcal L_F/h^2\) are \(m_F+O(h^2)\) and \(\sigma_F^2+O(h^2)\). For \(F=|Y_i|_Q^2\), these leading values are \(d\omega_i\) and \(2d\omega_i^2\).

To justify the multiplication step, first choose the actual vacuum approximation with error \(O(h^M)\), \(M\ge4\). The scaled fixed mark has operator norm \(O(h^{-2})\), leaving a multiplied error \(O(h^{M-2})\). Taylor expansion on the resulting finite polynomial-Gaussian quasimode supplies the first two jets. The identity
\[
(F+hD_G(F))(\Omega+hS_{1,G}\Omega)
=(I+hS_{1,G})(F\Omega)+O(h^2)
\]
and formal skew symmetry preserve means and inner products through first order. This proves (GV10) with the actual centering, rather than with a substituted Gaussian mean.

The same argument realizes every fixed finite family of invariant polynomial source vectors, not only quadratics. If \(F\) has degree at most \(m\), the normal-form structure gives \(\deg D_G(F)\le m+1\). Define the explicitly scaled compact readout
\[
\boxed{
\mathcal A_{F,h}
=F(2\mathbf Q/h)+hD_G(F)(2\mathbf Q/h).}
\tag{GV10a}
\]
It has operator norm \(O(h^{-m})\), is bounded at each fixed \(h>0\), and its local jet is \(F(Y)+hD_G(F)(Y)+O(h^2)\). Choose the vacuum approximation to order \(M\ge m+2\) before multiplication. Actual centering and normalization then prove (GV10) for this source whenever \(\sigma_F>0\), with constants uniform over the specified finite family. These are fixed polynomial labels with explicit strength-dependent compact realizations. For homogeneous quadratics, (GV10a) is precisely the scalar normalization of the fixed physical observable (GV9); that stronger fixed-observable property is not asserted for arbitrary polynomials.

## Composite contacts also return in the actual vacuum

For two such quadratics define
\[
\mathcal C_G(F,G)=D_G(FG)-F D_G(G)-G D_G(F).
\]
The Lie-contact theorem gives a homogeneous cubic. The compact composite
\[
\boxed{
\mathcal L^{\mathrm{coh}}_{F,G,h}
=\mathcal L_F\mathcal L_G
+\frac{h^2}{2}\mathcal C_G(F,G)(\mathbf Q)}
\tag{GV11}
\]
has, after scaling by \(16/h^4\), the jet \(FG+hD_G(FG)+O(h^2)\). Its actual centered normalized vector therefore obeys (GV10) with \(F\) replaced by \(FG\), when the latter has positive Gaussian variance. A vacuum approximation of order \(M\ge6\) pays the \(O(h^{-4})\) multiplier norm; further fixed accuracy handles any prescribed finite product of marks.

The individual observables \(\mathcal L_F,\mathcal L_G\) are fixed. The composite counterterm in (GV11) is explicitly strength-dependent through the calibrated \(h^2=(\kappa/g_{\mathrm{eff}})^{1/2}\). [[oriented-source-products-and-the-compact-contact-return|CX]] explains why a nonzero cubic contact cannot instead be hidden in a fixed smooth quartic mark.

Choose \(F=|Y_0|_Q^2\), \(G=|Y_1|_Q^2\), and define
\[
T_G(Y)=Q(Y_0,[Y_1,Y_2]),\qquad
\mathcal F_Q=\sum_{a,b,c}Q(T_a,[T_b,T_c])^2>0.
\]
The contact is \(4T_G/7\). Let \(\Delta_h=\mathcal L^{\mathrm{coh}}_{F,G,h}-\mathcal L_F\mathcal L_G\), and put
\[
X_h=\frac{16}{h^4}\Delta_h,\qquad
Z_h=\frac8{h^3}T_G(\mathbf Q).
\]
Exactly on the compact space, \(X_h=(4h/7)Z_h\). The independent Gaussian modes satisfy
\(\langle T_G^2\rangle_{\Omega^2}=4\sqrt2\,\mathcal F_Q\).
The same actual-vacuum estimates for the bounded cubic mark therefore give
\[
\boxed{
\operatorname{Cov}_{\psi_h}(X_h,Z_h)
=\frac{16\sqrt2}{7}\mathcal F_Q\,h+O(h^2).}
\tag{GV12}
\]
Actual centering does not change the leading coefficient: \(\langle Z_h\rangle_{\psi_h}=O(h)\) and \(\langle X_h\rangle_{\psi_h}=O(h^2)\). Its positivity is a measured source-contact response for the supplied fixed law, not a Hamiltonian potential or a mass-gap bound.

Every argument above fixes \(G,Q,\rho,A\), the four-face geometry and its connectors before \(h\to0\). It supplies actual first source and composite jets, including arbitrary finite quasimode accuracy needed for their normalization. It gives no uniformity over groups, representations or growing patches; no \(SU(2)\) nonlinear gap coefficient is asserted for another group. Complete chronological product histories and a four-dimensional continuum construction remain separate claims.
