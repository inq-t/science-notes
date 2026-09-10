# Causal-Action Normalization and Coercivity

The normalization constraints of a causal fermion system remove elementary ways to erase its measure and operator amplitudes. They do not by themselves fix a metric scale or a positive comparison edge. The exact calculations below isolate three different tasks: normalizing a nontrivial realization, controlling spectral escape, and obtaining a positive response that survives refinement. They identify what a proposed law of stable facticity must add.

## Homogeneity and the independent constraint data

Use the finite-volume setting of [[library/causal-fermion-systems-an-elementary-introduction/inq|Finster–Jokel, §3.2]], with fixed spin dimension \(n\ge1\). Define
\[
\begin{aligned}
V&=\rho(\mathcal F_n),&
\tau&=\int\operatorname{tr}(x)\,d\rho(x),\\
\mathcal T[\rho]&=\iint
 \left(\sum_{i=1}^{2n}|\lambda_i^{xy}|\right)^2d\rho(x)d\rho(y),&
\mathcal S[\rho]&=\iint\mathcal L(x,y)\,d\rho(x)d\rho(y),
\end{aligned}
\]
where
\[
\mathcal L(x,y)=
\sum_i|\lambda_i^{xy}|^2-
\frac1{2n}\left(\sum_i|\lambda_i^{xy}|\right)^2.
\]
The constraints fix \(V>0\), fix \(\tau\), and bound \(\mathcal T\le C\). For the normalization argument take \(\tau\ne0\); the examples below use \(\tau>0\).

For \(u,v>0\), set \(D_v(x)=vx\) and \(\rho_{u,v}=u(D_v)_*\rho\). Since \((vx)(vy)=v^2xy\), both spectral expressions scale by \(v^4\). Consequently
\[
\boxed{
V_{u,v}=uV,\quad
\tau_{u,v}=uv\tau,\quad
\mathcal S[\rho_{u,v}]=u^2v^4\mathcal S[\rho],\quad
\mathcal T[\rho_{u,v}]=u^2v^4\mathcal T[\rho].}
\tag{CN1}
\]
Preserving nonzero \(V,\tau\) forces \(u=v=1\) within this family. Fixed volume excludes the zero measure and uniform changes of its weight; fixed nonzero trace then excludes uniform contraction of the operators. Fixed rank would not do this, since every \(v>0\) preserves rank.

The dimensionless combinations
\[
\frac{V^2\mathcal S}{\tau^4},\qquad
\frac{V^2\mathcal T}{\tau^4}
\tag{CN2}
\]
are invariant under both rescalings. Thus fixing volume and trace leaves the dimensionless cap \(CV^2/\tau^4\) as genuine data of this constrained problem. Equation (CN1) concerns measure weight and operator amplitude. It supplies no metric length-to-clock map, and its quartic degree is not a derivation of the four-dimensional Yang–Mills action.

## The upper bound controls an escape invisible to the action

Take \(n=1\), \(\mathcal H=\mathbb C^3\), and mutually orthogonal rank-one projections \(P_0,P_1,P_2\). For \(0<p<V\) put
\[
y=(\tau/p)P_0,\qquad
x_R=R(P_1-P_2),\qquad
\rho_R=p\delta_y+(V-p)\delta_{x_R},\quad R>0.
\]
The measure has volume \(V\) and integrated trace \(\tau\). The eigenvalues of \(x_R^2\) are \(R^2,R^2\), so \(\mathcal L(x_R,x_R)=0\). Mixed products with \(y\) vanish. Direct evaluation gives
\[
\mathcal S[\rho_R]=\frac{\tau^4}{2p^2},\qquad
\mathcal T[\rho_R]
=\frac{\tau^4}{p^2}+4(V-p)^2R^4.
\tag{CN3}
\]
The balanced spectrum can grow without increasing the causal action. The boundedness constraint excludes that escape. Its role is different from a lower stiffness bound.

## Nontrivial normalization still permits dilution

In one fixed infinite-dimensional Hilbert space choose mutually orthogonal rank-one projections \(P_i\), and set
\[
x_i=(\tau/V)P_i,\qquad
\rho_m=\frac Vm\sum_{i=1}^m\delta_{x_i}.
\tag{CN4}
\]
All \(x_i\) belong to \(\mathcal F_n\). Volume and trace equal \(V,\tau\) for every \(m\). Off-diagonal products vanish; the diagonal product has one nonzero eigenvalue \((\tau/V)^2\). Hence
\[
\boxed{
\mathcal T[\rho_m]=\frac{\tau^4}{V^2m},\qquad
\mathcal S[\rho_m]
=\left(1-\frac1{2n}\right)\frac{\tau^4}{V^2m}
\longrightarrow0.}
\tag{CN5}
\]
Any fixed positive cap \(C\) is satisfied for sufficiently large \(m\).

These are admissible measures, not a claimed family of causal-action minimizers. They show that the displayed constraints alone give no positive action floor uniformly in the number of independent sectors. The example does not contradict the finite-dimensional existence results reviewed by Finster and Jokel: a fixed finite-dimensional space cannot contain arbitrarily many such orthogonal sectors. It also does not assert that an action floor would be equivalent to a Hamiltonian gap.

For the foundational programme, the question is whether the law of admissible extension supplies a quantitative shared comparison beyond these action constraints. No physical response or chronology has been assigned to the sequence, so (CN5) does not compute a failure of that comparison. Requiring an algebra to be connected or forbidding exactly orthogonal blocks is insufficient by itself; increasingly weak couplings can approximate their separation. [[scale-bearing-descent/coherent-comparison-lifts-and-bounded-descent|Constructive descent and source extension]] asks for a complete bound fixed by the source rules.

## A nonnegative Lagrangian is not a positive kernel

For \(n=1\) in \(\mathbb C^2\), take
\[
x=\operatorname{diag}(1,0),\qquad
y=\operatorname{diag}(1,-1).
\]
Both belong to \(\mathcal F_1\). Their causal Lagrangian matrix is
\[
\begin{pmatrix}
\mathcal L(x,x)&\mathcal L(x,y)\\
\mathcal L(y,x)&\mathcal L(y,y)
\end{pmatrix}
=
\begin{pmatrix}
1/2&1/2\\
1/2&0
\end{pmatrix},
\qquad \det=-1/4.
\tag{CN6}
\]
Although every entry is nonnegative, this matrix is not positive semidefinite. The distinction is between nonnegativity on pairs and positivity on all complex linear combinations of preparations. The causal Lagrangian therefore cannot simply serve on the full operator class as the positive source kernel or the Hermitian response in [[measured-response-carriers/response-to-energy-comparison|the response-to-energy comparison]]. A restricted branch or a different pullback would require its own positivity argument.

A constrained second variation, a surface-layer form, or another response generated by the same law could supply the missing object. Each has its own domain and positivity problem. A local minimum gives nonnegative second derivatives along suitable twice-differentiable two-sided admissible curves, or the appropriate constrained second-order condition on critical directions. It does not automatically give a uniform lower bound, a complete quantum source carrier, or its physical chronology.

## The scale selection that remains

[[scale-bearing-descent/constitutive-resolution-and-the-yang-mills-return|Constitutive resolution]] separates the proposed return into a complete local source law, its inherited duration, and its positive response. For a chosen family, the quantitative target is
\[
b_rN_r(F)\le R_r(F,F)
\le L_r^2D_{r,\ell_r}(F)+\eta_rN_r(F),
\qquad
\liminf_r\frac{b_r-\eta_r}{L_r^2}>0,\quad
\ell_r\longrightarrow\ell_*>0.
\tag{CN7}
\]
Here \(R_r\) is a positive Hermitian form, \(0<L_r<\infty\), \(\eta_r\ge0\), and the positive margin is eventually bounded away from zero. The forms \(N_r\) and \(D_{r,\ell_r}\) are the centered norm and chronological innovation of the same complete returned sources. Neither is the total causal action. The source rules must determine \(R_r\) and the comparison map before evaluating the desired spectrum.

One law that selects admissible realizations and supplies (CN7) would do more than normalize an arena: it would keep its complete distinctions detectable while the local description changes. The surviving duration and dimensionless comparison margin are separate requirements. Together with the exact Yang–Mills return, they would make a positive mass threshold a consequence.
