# Oriented Source Products Have a Measurable Compact Contact

Every four-face quadratic has a fixed bounded cubic correction that realizes its first-order normal-form source vector in the actual compact vacuum. Products require more: the same transport forces a cubic contact term whose physical coefficient is proportional to \(h^2\). It cannot be supplied by a fixed smooth quartic probe with only higher Taylor terms. An explicit mixed cubic readout detects this contact even though its leading one-point mean vanishes.

**Status: proved fixed-patch compact realization of the first source and product jets.** [[four-face-oriented-normal-form-and-the-universal-source-lift|The oriented normal form]] fixes the real skew operator \(S_1\) and its source lift. [[four-face-source-products-and-the-oriented-contact|The product contact]] owns the complete contact formula. [[compact-source-normalization-and-the-nonlinear-return|CS]] supplies arbitrary-order actual vacuum control. The compact face words, comb connectors, Hamiltonian and scaled clock remain fixed. The composite coefficient below is a derived strength-dependent readout, and is identified as such.

[[fixed-group-compact-vacuum-and-oriented-source-return|GV1–12]] extends this actual vacuum and finite polynomial source return to every fixed compact connected simple group with its declared faithful weighted-character cost. The mixed coefficient becomes \(16\sqrt2\,\mathfrak F_Q/7\), with the weighted scale and bounded Lie source fixed independently. Its estimates are not uniform in group or growing patch.

## The vacuum determines the first multiplication lift

Work on the full physical four-face carrier with the mode variables and Gaussian vacuum of [[four-face-cubic-response-and-source-leakage|FC]]. Write
\[
h=(\kappa/g)^{1/4},\qquad
\widehat K_h=K_0+hV_1+O(h^2),\qquad
\psi_h=\Omega+h u+O(h^2)
\tag{CX1}
\]
in the common dilated half-density chart. The displayed vector expansions and all remainders in this note are at fixed patch and for fixed finite polynomial families. Let \(S_1\) be the real formally skew-adjoint polynomial differential operator satisfying
\[
[K_0,S_1]=-V_1,\qquad
u=S_1\Omega .
\]
Here formal adjoints and commutators are used on the polynomial-Gaussian core; no self-adjoint realization, global boundedness of \(S_1\), or construction of its exponential is required.

For a real invariant polynomial \(F\), define
\[
\boxed{
D(F)=\Omega^{-1}[S_1,M_F]\Omega,\qquad
\mathcal T_h F=F+hD(F).}
\tag{CX2}
\]
Then \(D(1)=0\), and multiplication by this corrected function gives
\[
\boxed{
(\mathcal T_hF)(\Omega+hS_1\Omega)
=(I+hS_1)(F\Omega)+O(h^2).}
\tag{CX3}
\]
The identity follows by expanding the commutator; it includes the vacuum correction rather than fitting a source against a fixed Gaussian.

Put \(m_F=\langle\Omega,F\Omega\rangle\) and
\(\sigma_F^2=\|(F-m_F)\Omega\|^2>0\). Skew-adjointness implies preservation of inner products to first order on every fixed polynomial family. Consequently, once the multiplier is realized in the compact theory, its actual mean and variance are \(m_F+O(h^2)\) and \(\sigma_F^2+O(h^2)\), and its actual normalized centered vector is
\[
\boxed{
\zeta_{F,h}
=\mathcal J_h(I+hS_1)
\frac{(F-m_F)\Omega}{\sigma_F}+O(h^2).}
\tag{CX4}
\]
The cutoff map \(\mathcal J_h\) is CS7's equivariant density isometry near the well. This is a norm statement about source vectors. It does not replace the differential operator \(M_F+h[S_1,M_F]\) by multiplication on every state.

## Quadratic sources need fixed cubic marks

Use the compact quaternion modes
\[
\mathbf Q_m=\sum_pO_{pm}\mathbf q_p,\qquad
\mathbf Q_m(hY)=\frac h2Y_m+O(h^3).
\]
For the actual four-face \(S_1\), its differential part has the form
\[
S_1=v_2(Y)\cdot\nabla-\frac47
\partial_0\cdot(\partial_1\times\partial_2),
\tag{CX5}
\]
where \(v_2\) is the fixed divergence-free homogeneous quadratic vector field of the normal-form owner. This note does not replace that field by its action on the vacuum.

If \(F\) is an invariant homogeneous quadratic, \(D(F)\) is an invariant homogeneous cubic. Differential degree gives only degrees three and one; there is no nonzero invariant linear polynomial under simultaneous color rotations. Therefore the fixed bounded physical mark
\[
\boxed{
\mathcal L_F(\mathbf Q)=F(\mathbf Q)+2D(F)(\mathbf Q)}
\tag{CX6}
\]
satisfies
\[
\frac4{h^2}\mathcal L_F(\mathbf Q(hY))
=F(Y)+hD(F)(Y)+O(h^2).
\]
All coefficients and comparison paths in \(\mathcal L_F\) are independent of \(h\). Equation (CX4) follows after actual centering and normalization. For \(F=|Y_0|^2\), this construction is exactly [[four-face-oriented-source-and-the-gap-following-probe|OS2's fixed probe]].

The compact remainder is not justified by multiplying an \(O(h^2)\) vacuum norm approximation by the scaled mark: its operator norm grows as \(O(h^{-2})\). Instead use CS's vacuum quasimode with norm error \(O(h^M)\), \(M\ge4\), before multiplication, and then expand its finite polynomial jets through first order. The multiplied residual is \(O(h^{M-2})\); Taylor and cutoff errors have the required order. For a scaled quartic mark below, choose \(M\ge6\) because its operator norm is \(O(h^{-4})\). Higher fixed accuracy is available whenever another marked factor is inserted.

## The product contact has a different physical scaling

For two homogeneous invariant quadratics define the symmetric contact
\[
\boxed{
\Gamma_D(F,G)=D(FG)-F D(G)-G D(F)
=\Omega^{-1}\bigl[\,[S_1,M_F],M_G\bigr]\Omega .}
\tag{CX7}
\]
The vector-field part is a derivation and contributes nothing. The constant third derivative in (CX5), after conjugating by \(\Omega\), has a linear second-derivative coefficient. This supplies an invariant cubic contact. Its constant third-derivative contribution on \(FG\) would have degree one and vanishes by invariance. Thus
\[
D(FG)=P_5+P_3,\qquad
P_5=F D(G)+G D(F),\qquad
P_3=\Gamma_D(F,G),
\]
with the displayed degrees literal homogeneous polynomial degrees.

The compact realization of \(\mathcal T_h(FG)\), normalized by \(16/h^4\), is
\[
\boxed{
\mathcal L_{FG,h}(\mathbf Q)
=F(\mathbf Q)G(\mathbf Q)+2P_5(\mathbf Q)
+\frac{h^2}{2}P_3(\mathbf Q).}
\tag{CX8}
\]
Indeed a homogeneous degree-five mark contributes \(hP_5\) after multiplication by \(32/h^4\), while the degree-three term contributes
\((16/h^4)(h^2/2)(h^3/8)P_3=hP_3\).
It follows that the actual centered normalized vector of this composite obeys (CX4) with \(F\) replaced by \(FG\), provided its harmonic variance is nonzero.

Equivalently one may retain the entire product of the two fixed individual lifts and add the contact:
\[
\boxed{
\mathcal L^{\mathrm{coh}}_{F,G,h}
=\mathcal L_F\mathcal L_G+\frac{h^2}{2}\Gamma_D(F,G)(\mathbf Q).}
\tag{CX9}
\]
This differs from (CX8) by the degree-six mark \(4D(F)D(G)\), which contributes only at order \(h^2\) after quartic normalization. Both realize the same first transported product.

When \(P_3\ne0\), the factor \(h^2/2\) is necessary in this smooth compact realization. A fixed smooth observable whose lower Taylor jets vanish and whose leading jet is the degree-four polynomial \(FG\) has only a homogeneous degree-five jet at the next order. It cannot also produce the required degree-three polynomial at that order. Adding a fixed cubic term instead creates an order-\(h^{-1}\) vector after quartic normalization. Subtracting an actual scalar mean cannot cancel it. Strength-dependent lower-degree terms are familiar possible definitions of a composite observable, but here their presence and coefficient are consequences to retain, not a fixed-probe claim.

If the factors are centered first, their actual scalar means also generate known lower-degree terms in their product. The contact (CX7) is unchanged under adding constants to either factor, so these centering terms do not remove the additional requirement in (CX9).

## A mixed readout detects the forced term

Take
\[
F=|Y_0|^2,\qquad G=|Y_1|^2,\qquad
T=T_{012}=Y_0\cdot(Y_1\times Y_2).
\]
The third-derivative coefficient in (CX5) gives
\[
\Gamma_D(F,G)=\frac47T,\qquad
\langle T\rangle_\Omega=0,\qquad
\langle T^2\rangle_\Omega=24\sqrt2 .
\tag{CX10}
\]
For example, the relevant Gaussian log derivative is
\(\partial_2\Omega/\Omega=-Y_2/(2\omega_2)=-Y_2/4\). Together with the two quadratic gradients, it turns the coefficient \(-4/7\) in (CX5) into the positive \(4/7\) in (CX10).

The difference between the coherent composite and the ordinary product of its individually lifted marks is the exact bounded compact function
\[
\Delta_h=\frac{2h^2}{7}
\mathbf Q_0\cdot(\mathbf Q_1\times\mathbf Q_2).
\]
Define the scaled comparison marks
\[
X_h=\frac{16}{h^4}\Delta_h,\qquad
Z_h=\frac8{h^3}
\mathbf Q_0\cdot(\mathbf Q_1\times\mathbf Q_2).
\]
Exactly on the compact space, \(X_h=(4/7)hZ_h\). In the chart, \(X_h=(4/7)hT+O(h^3)\) and \(Z_h=T+O(h^2)\). Their covariance is therefore \((4h/7)\operatorname{Var}_{\psi_h}(Z_h)\). Using the same actual compact vacuum in both factors, CS's higher-accuracy multiplication argument proves
\[
\boxed{
\operatorname{Cov}_{\psi_h}(X_h,Z_h)
=\frac{96\sqrt2}{7}\,h+O(h^2).}
\tag{CX11}
\]
The coefficient is the actual Gaussian contraction
\((4/7)\langle T^2\rangle_\Omega\), with no adjusted clock or fitted coupling. Actual centering cannot change it: \(\langle X_h\rangle_{\psi_h}=O(h^2)\) and \(\langle Z_h\rangle_{\psi_h}=O(h)\), so the product of their means is \(O(h^3)\). In contrast, the leading one-point mean of the contact vanishes by parity. A one-point comparison would therefore miss this first mixed-source effect.

## Which product is transported

As a formal map on invariant polynomials, \(\mathcal T_h=I+hD\) is unital and invertible modulo \(h^2\). Transporting ordinary multiplication onto its image gives
\[
\boxed{
A\star_h B
=\mathcal T_h(\mathcal T_h^{-1}A\,\mathcal T_h^{-1}B)
=AB+h\Gamma_D(A,B)+O(h^2).}
\tag{CX12}
\]
It is real, commutative and associative modulo \(h^2\), because it is a transported product. Pulling the ordinary product of corrected marks back to the original symbols instead has the opposite sign, \(FG-h\Gamma_D(F,G)\). Neither statement identifies \(\star_h\) with ordinary pointwise multiplication of the individually corrected compact marks.

The construction proves a finite-order product law on the polynomial source algebra and the compact realization of the specified quadratic factors and their quartic product. It does not close the twelve-dimensional quadratic-plus-cubic span under multiplication, construct an exact compact algebra isomorphism, or establish all chronological marked histories. Those claims require control on the corresponding product and history carriers. The nonzero coefficient (CX11) is already a fixed-law test that any such completion must reproduce.

## Forgetting an orientation leaves a positive area response

There is a positive conditional response associated with the same signed contact. In the harmonic vacuum, retain \(Y_0,Y_1\) and condition over the independent \(Y_2\), whose component variance is \(\omega_2=2\). For \(\Gamma=(4/7)T_{012}\),
\[
\boxed{
\mathbb E_0[\Gamma\mid Y_0,Y_1]=0,\qquad
\operatorname{Var}_0(\Gamma\mid Y_0,Y_1)
=\frac{32}{49}|Y_0\times Y_1|^2.}
\tag{CX13}
\]
Indeed \(T_{012}=(Y_0\times Y_1)\cdot Y_2\), so conditional Gaussian contraction gives the second identity directly. Integrating once more uses
\(\mathbb E_0|Y_0\times Y_1|^2=6\omega_0\omega_1=12\sqrt2\), recovering
\(\|\Gamma\Omega\|^2=384\sqrt2/49\).

The squared Lie bracket therefore occurs as a forced variance of hidden oriented source information. It is not thereby a term in the Hamiltonian. This normal-mode conditioning is a diagnostic, not an identification with a spatial edge cut. A spatial sewing test must use its inherited covariance and retain the access footprint of the corrected sources, whose cubic terms can involve faces outside the original quadratic's labels.
