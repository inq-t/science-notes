# The Inherited Derivative on Moving Conditional Fibers

Writing a joint law as a family of conditional Hilbert spaces makes the relation between a distinction and its context explicit. But changing representation must also transform the derivative. A Fisher term obtained by differentiating a conditional vacuum is not automatically an added mass: in the inherited joint form its score correction cancels that term. A moving nonvacuum band can have genuine geometric cost, but complementary bands remain part of the operator.

**Status: [EXACT REPRESENTATION AND FORM IDENTITIES] on the stated smooth fixed-carrier conditional family; [NO DERIVATION OF A PHYSICAL CLOCK, JOINT LAW OR MASS GAP].**

## Transport the derivative with the carrier

Let the actual law be
\[
\mu(dx,du)=\nu(dx)q_x(u)m(du),\qquad
\int q_x\,dm=1,
\tag{MF1}
\]
where the hidden reference measure and both product metrics are fixed, \(q_x\) is smooth and positive, and all differentiations below are valid on a common form core. Write \(s_i=\partial_i\log q_x\).

Suppose the inherited horizontal energy is
\[
\mathcal E_{\mathrm{hor}}(F)
=\int|\partial_xF|_{g_x^{-1}}^2\,d\mu.
\tag{MF2}
\]
This is a declared derivative at fixed \(u\), not a consequence of the probability law alone. Multiplication by \(\sqrt{q_x}\) gives a unitary map
\[
\mathcal UF=\Psi=\sqrt{q_x}F:
L^2(\mu)\longrightarrow L^2(\nu\otimes m).
\]
Transporting the same derivative gives
\[
\boxed{
\mathcal U\partial_i\mathcal U^{-1}
=D_i:=\partial_i-\tfrac12s_i,\qquad
\mathcal E_{\mathrm{hor}}(F)
=\int|D\Psi|_{g_x^{-1}}^2\,d\nu\,dm.}
\tag{MF3}
\]
The conditional vacuum \(\phi_{0,x}=1\) becomes \(\psi_{0,x}=\sqrt{q_x}\). Exactly
\[
D_i\psi_{0,x}=0,
\qquad
\int|\partial_i\psi_{0,x}|^2\,dm
=\tfrac14\int s_i^2q_x\,dm.
\tag{MF4}
\]
The second expression is a Fisher coefficient; the first is its cancellation in the inherited horizontal form. Replacing \(D\) by bare \(\partial\) would change the operator.

This distinguishes two legitimate derivatives. The square-root-induced **metric connection** on the varying spaces \(L^2(q_xm)\) is \(\nabla_i^{\mathrm{met}}=\partial_i+s_i/2\); it becomes bare \(\partial_i\) in the fixed half-density representation. The original product derivative \(\partial_i\) becomes \(D_i\), not bare \(\partial_i\). [[scale-score-connection/inq|The scale-score connection]] owns metric transport and its naturality problem. Equation (MF3) instead preserves an already declared joint gradient form.

## A selected moving band has both connection and transverse cost

For a smooth normalized conditional mode \(\phi_x\in L^2(q_xm)\), use inner products conjugate-linear in the first slot and define
\[
c_i=\langle\phi_x,\partial_i\phi_x\rangle_{q_x},\qquad
Q_{\phi,x}=I-|\phi_x\rangle\langle\phi_x|,\qquad
G_{ij}=\langle Q_{\phi,x}\partial_i\phi_x,
Q_{\phi,x}\partial_j\phi_x\rangle_{q_x}.
\tag{MF5}
\]
Differentiating its normalization gives
\[
2\operatorname{Re}c_i
=-\int s_i|\phi_x|^2q_x\,dm.
\tag{MF6}
\]
Thus \(c_i\) is not generally an imaginary Berry connection: the measure is moving too.

For \(F(x,u)=a(x)\phi_x(u)\), orthogonal decomposition gives exactly
\[
\boxed{
\mathcal E_{\mathrm{hor}}(a\phi)
=\int\left[
|da+ca|_{g_x^{-1}}^2
+|a|^2\operatorname{tr}_{g_x}G
\right]d\nu.}
\tag{MF7}
\]
If a nonnegative conditional generator also satisfies \(H_x\phi_x=\lambda(x)\phi_x\), its vertical form adds \(\int\lambda(x)|a(x)|^2d\nu\). An eigenband must be chosen smoothly on the chart used; crossings, multiplicities and domains cannot be bypassed by choosing a discontinuous eigenvector.

These equations hold on the selected band. They do not lower-bound the complete operator by \(\lambda+\operatorname{tr}G\). Variations in the complement have cross terms and can relax the band cost. [[coarse-response-memory/inq|The complement/Schur and memory calculation]] gives the corresponding full-operator obligation. A consistent frame change preserves the form; choosing a different connection or dropping the complement changes the problem.

## The actual ground state returns coupled fiber equations

The same distinction can be made directly in a supplied
Schrödinger operator, without a band approximation. Let
\(X,Y\) be connected compact manifolds without boundary,
\[
H=H_A+H_B+W,\qquad H_A=-\kappa\Delta_A+V_A,\quad
H_B=-\kappa\Delta_B+V_B,\quad \kappa>0,\qquad
H\psi=E\psi,\quad \psi>0,\quad \|\psi\|=1,
\]
with smooth real potentials, product metric and inherited
\(H^2\) domain. Factor its actual positive vector as
\[
\chi(x)=\left(\int_Y\psi(x,y)^2dy\right)^{1/2},
\qquad \Phi_x(y)=\psi(x,y)/\chi(x),\qquad \|\Phi_x\|_Y=1.
\tag{MF12}
\]
These factors are smooth and positive. This is the established
conditional-amplitude method, not a new factorization principle;
[[library/correlated-electron-nuclear-dynamics-exact-factorization/inq|Abedi, Maitra and Gross]]
discuss exact factorization and its earlier stationary form.
The following compact positive-ground-state identities are
proved directly by substitution.

Normalization gives
\(\langle\Phi,\partial_i\Phi\rangle=0\) and
\(\langle\Phi,\Delta_A\Phi\rangle=-\|\nabla_A\Phi\|^2\).
In the actual conditional law \(\Phi_x^2dy\),
\[
(M_A)_{ij}=\langle\partial_i\Phi,\partial_j\Phi\rangle_Y,
\qquad T=g_A^{ij}(M_A)_{ij}=\|\nabla_A\Phi\|^2.
\tag{MF13}
\]
Thus the conditional half-score covariance is exactly the
pullback metric of the normalized positive fiber vector.
There is no phase connection in this real positive choice.

Put \(Q_x=I-|\Phi_x\rangle\langle\Phi_x|\) and
\(\epsilon(x)=\langle\Phi_x,(H_B+W_x)\Phi_x\rangle\).
Projecting the expanded eigen-equation parallel and perpendicular
to \(\Phi_x\) gives the two exact equations
\[
\boxed{[-\kappa\Delta_A+V_A+\epsilon+\kappa T]\chi=E\chi,}
\tag{MF14}
\]
\[
\boxed{(H_B+W_x-\epsilon)\Phi
=\kappa Q_x(\Delta_A+2\nabla\log\chi\cdot\nabla_A)\Phi.}
\tag{MF15}
\]
The right side of (MF15) is generally nonzero. The conditional
vector is not being identified with an instantaneous ground
vector of \(H_B+W_x\), and a reduced-resolvent formula based on
a presumed fiber gap is not justified. Differentiating this
equation also differentiates its horizontal response and \(Q_x\);
it does not isolate a bounded inverse times \(\partial_iW\).

For the [[coarse-response-memory/boundary-interaction-and-conditional-score-budget|shifted Wilson cut]],
let \(H_A\phi_A=E_A\phi_A\), \(H_B\phi_B=E_B\phi_B\), and
\[
\theta=\chi/\phi_A,\quad
h(x)=\langle\Phi_x,(H_B-E_B)\Phi_x\rangle\ge0,\quad
\bar W=\langle\Phi,W\Phi\rangle,\quad
\mathscr D_A^{\phi_A}=\Delta_A+
2\nabla\log\phi_A\cdot\nabla_A.
\]
In the convention \(E-E_A-E_B=-\delta\), (MF14) becomes
\[
-\kappa\frac{\mathscr D_A^{\phi_A}\theta}{\theta}
+h+\bar W+\kappa T=-\delta.
\tag{MF16}
\]
At any maximum of \(\theta\) this proves
\[
\kappa T+h\le\lambda N_\partial-\delta.
\tag{MF17}
\]
It is not a bound at the maximum of \(T\). At other points the
uncontrolled marginal term
\(\mathscr D_A^{\phi_A}\theta/\theta\) can compensate large
conditional response. Integrating (MF16) against \(\chi^2dx\)
reproduces the previous boundary Fisher budget, not an additional
essential-supremum estimate.

Finally, ground-transform the scalar operator (MF14) by \(\chi\).
Its retained form is exactly
\[
a_A[f]=\kappa\int_X\chi^2|\nabla_Af|^2dx.
\tag{MF18}
\]
The positive \(\kappa T\) is a genuine term in the untransformed
scalar equation, but it is **not an additional mass potential**
in this retained form. The omitted component remains
\[
Q_x(H-E)(\chi f\Phi)
=-2\kappa\chi\,g_A^{ij}(\partial_i f)(\partial_j\Phi),
\tag{MF19}
\]
which is the hidden drift in the boundary-budget construction.
Dropping it would change the full physical return, just as
dropping the complementary band in (MF7) does.

[[coarse-response-memory/radial-marginal-and-conditional-stress#The actual marginal retains both fiber costs|The adjacent-plaquette application]]
computes \(\epsilon+\kappa T\) through cubic order. Its
horizontal and hidden cubic kinetic terms cancel, and the
remaining effective potential is monotone at sufficiently
small coupling. This gives a curvature bound on that
marginal's inherited form without making its nonzero
hidden response disappear.

## The effective force is a weighted metric divergence

The two fiber costs in (MF14) have a useful combined first
variation. Keep the same fixed raw product, constant
\(\kappa\), real positive \(\Phi\), and common smooth core.
Write \(\rho_A=\chi^2\), \(M=M_A\), and
\(\mathcal F=\epsilon+\kappa T\). For a symmetric covariant
tensor use \((\operatorname{div}M)_i=\nabla^jM_{ji}\).
Then
\[
\boxed{
d\mathcal F
=\langle\Phi,(d_AW)\Phi\rangle_B
+\frac{2\kappa}{\rho_A}\operatorname{div}_A(\rho_A M).
}
\tag{MF20}
\]
The first term is the conditional mean of the explicit
interaction derivative, not the derivative of the conditional
mean of \(W\). The second is a covector on the retained raw
manifold. Here information metric means precisely (MF13);
this is not an identification with a spacetime stress tensor.

For the proof, put \(u=\log\chi\), \(\Phi_i=\nabla_i\Phi\).
Normalization gives \(\langle\Phi_i,\Phi\rangle=0\).
Differentiating \(\epsilon\) and applying (MF15) gives
\[
\partial_i\epsilon
=\langle\Phi,(\partial_iW)\Phi\rangle
+2\kappa\langle\Phi_i,\Delta_A\Phi\rangle
+4\kappa M_{ij}\nabla^ju.
\]
Meanwhile
\[
\partial_iT=2\langle\nabla^j\Phi,\nabla_i\nabla_j\Phi\rangle,
\qquad
\nabla^jM_{ji}
=\langle\Delta_A\Phi,\Phi_i\rangle
+\langle\nabla^j\Phi,\nabla_j\nabla_i\Phi\rangle.
\]
Covariant second derivatives commute on this Hilbert-valued
scalar. Combining these expressions proves (MF20), with no
curvature term, Killing assumption or fiber inverse.
Differentiation is on the fixed raw \(B\) carrier: a
coordinate-reduced expression for \(H_B\) can depend on retained
invariants without making the original raw operator
retained-dependent.

For a smooth retained vector field \(Z\), the equivalent weak
identity on compact \(A\) is
\[
\int_A\rho_A\,d\mathcal F(Z)
=\int_A\rho_A\langle\Phi,d_AW(Z)\Phi\rangle_B
-2\kappa\int_A\rho_A\langle M,\operatorname{sym}\nabla Z\rangle.
\tag{MF21}
\]
It uses no derivative of \(M\) after integration by parts.
It is nevertheless not a sign theorem: positive \(M\) need
not have a nonpositive divergence or contraction with an
indefinite deformation tensor.

[[coarse-response-memory/radial-marginal-and-conditional-stress#Radial force retains orbit stress|The radial gauge application]]
exhibits the missing contraction explicitly. Its shape
projection controls one operator norm while its orbit
components contribute to the effective force. A parent
construction that supplies a positive comparison tensor must
also make this differential compatibility hold; assigning
a convenient eigenvalue or trace does not ensure it.
Conversely, (MF20) is a necessary identity of the supplied
ground-state problem, not a sufficient reconstruction axiom
for its state or dynamics.

## Conditional relaxation supplies the time-dependent force

Keep the same time-independent compact product operator. From a
smooth strictly positive normalized initial vector form
\(\psi_t=e^{-tH}\psi_{\rm in}/\|e^{-tH}\psi_{\rm in}\|\),
and factor it by (MF12) at each time. Write
\(\bar E(t)=\langle\psi_t,H\psi_t\rangle\),
\(\rho_t=\chi_t^2\), and retain the actual
\(\epsilon_t,T_t,M_t,\mathcal F_t\) from (MF13)--(MF14).
Here \(t\) is the supplied heat parameter, not a reconstructed
Lorentzian clock or a postulated ontological time.

Projection of \(\dot\psi=-(H-\bar E)\psi\) gives
\[
\begin{aligned}
\dot\chi&=\kappa\Delta_A\chi
 -(V_A+\mathcal F-\bar E)\chi,\\
\dot\Phi&=\kappa Q(\Delta_A+2\nabla\log\chi\cdot\nabla_A)\Phi
 -(H_B+W-\epsilon)\Phi.
\end{aligned}
\tag{MF22}
\]
In particular \(\langle\Phi,\dot\Phi\rangle_B=0\). Define
the mixed derivative pairing and conditional speed
\[
\jmath_i=\langle\nabla_i\Phi,\dot\Phi\rangle_B,
\qquad n=\|\dot\Phi\|_B^2.
\]
The exact spatial and temporal balances are
\[
\boxed{
\begin{aligned}
d_A\mathcal F
 &=\langle\Phi,(d_AW)\Phi\rangle_B
   +2\kappa\rho^{-1}\operatorname{div}_A(\rho M)-2\jmath,\\
\partial_t\mathcal F
 &=2\kappa\rho^{-1}\operatorname{div}_A(\rho\jmath^\sharp)-2n.
\end{aligned}}
\tag{MF23}
\]
The first identity follows from the proof of (MF20), replacing
its stationary fiber equation by (MF22); the additional term
has a minus sign. For the second, differentiate
\(\epsilon+\kappa\|\nabla_A\Phi\|^2\), substitute (MF22),
and combine the two horizontal terms by the product rule.
The potentials have no explicit time derivative. All derivatives
still act on the fixed raw hidden carrier.

The conditional cost need not decrease at each point: it has a
spatial flux. Nor need its weighted integral decrease along the
coupled evolution, since
\[
\frac{d}{dt}\int_A\rho\mathcal F
 =\int_A\dot\rho\mathcal F-2\int_A\rho n.
\]
The moving marginal contributes the first term. Holding that
weight fixed gives a constrained weighted gradient flow of
\(\tfrac12\int\rho\mathcal F\); this frozen-weight statement
must not replace the actual coupled equations.

There is nevertheless an exact whole-state dissipation bound.
Orthogonality of the two factor velocities yields
\[
\boxed{
-\frac12\dot{\bar E}
=\operatorname{Var}_{\psi_t}(H)
=\|\dot\chi\|_A^2+\int_A\rho n.
}
\tag{MF24}
\]
The variance identity follows by differentiating the normalized
Rayleigh energy; the last equality expands
\(\dot\psi=\dot\chi\Phi+\chi\dot\Phi\).

The nonstationary force defect has an intrinsic estimate. Put
\[
\mathfrak r=d_A\mathcal F-\langle\Phi,(d_AW)\Phi\rangle_B
 -2\kappa\rho^{-1}\operatorname{div}_A(\rho M)=-2\jmath.
\]
Let \(A_xv=d_A\Phi(v)\). Then \(M=A_x^*A_x\) and
\(\jmath=A_x^*\dot\Phi\), so \(\mathfrak r\) lies in the
range of \(M\). Its dual quadratic form satisfies
\[
\boxed{
\mathfrak r^\top M^+\mathfrak r\le4n,\qquad
\int_0^{t_1}\!\!\int_A\rho\,
 \mathfrak r^\top M^+\mathfrak r
 \le2[\bar E(0)-\bar E(t_1)].
}
\tag{MF25}
\]
Here \(M^+\) denotes the inverse quadratic form on its range,
represented by the Moore--Penrose inverse in an orthonormal raw
frame. The first expression is four times the squared projection
of \(\dot\Phi\) onto \(\operatorname{Ran}A_x\). It is
coordinate invariant; no derivative of a pseudoinverse or
constant-rank hypothesis is used. Integration and (MF24) give
the second inequality.

The complementary squared speed distinguishes actual fiber
change from motion along retained-coordinate directions:
\[
\boxed{
n_\perp=n-\jmath^\top M^+\jmath
=\|(I-\Pi_{\operatorname{Ran}A_x})\dot\Phi\|_B^2\ge0.
}
\tag{MF26}
\]
Under a time-dependent relabelling of retained coordinates,
the local velocity changes by \(\dot\Phi\mapsto\dot\Phi+A_xv\).
Its normal component, and hence \(n_\perp\), is unchanged:
\(\jmath\mapsto\jmath+Mv\) and
\(n\mapsto n+2\jmath(v)+M(v,v)\) give the same cancellation.
This is a coordinate-invariant normal speed, not an invariant
under changing the heat parameter's units. Its pointwise formula
does not supply a smooth global transport when ranks change.
It vanishes in every stationary conditional vector, whether or
not the full theory is gapped, so it is not itself a mass.

Thus the same conditional vector supplies the spatial metric,
mixed relaxation current and a dissipative comparison. A
positive spatial tensor alone omits this compatibility. The
estimate bounds the nonstationary defect, not stationary stress
or an exponential decay rate. The Hamiltonian and heat law are
still inputs; no mass gap or emergent action principle has been
derived. In particular,
[[coarse-response-memory/heat-preparation-and-latitude-coercivity#The actual heat trajectory can leave the stationary shape class|the actual gauge heat trajectory]]
cannot be audited by imposing (MF20) at each finite time.

## A local loss density exposes the unclosed shape source

The same normalized heat equation has a density form without
singular fiber coordinates. Write \(V=V_A+V_B+W\),
\(R(x)=\int_Y\psi^2\), and define
\[
\mathcal J(x)=\int_Y[\kappa|\nabla_{A,B}\psi|^2+V\psi^2],
\qquad U=\mathcal J/R.
\]
The product rule for \(\Delta(\psi^2)\), followed by hidden
integration on the compact raw carrier, gives
\[
\boxed{
\partial_tR=\kappa\Delta_A R-2\mathcal J+2\bar E R,
\qquad
U=\kappa|\nabla_A\log\chi|^2+V_A+\mathcal F,
\qquad \int_A\mathcal J=\bar E.
}
\tag{MF27}
\]
If \(V\ge0\), then \(\mathcal J\ge0\). A constant potential
shift changes \(U\) and \(\bar E\) together but not the
normalized evolution or spatial derivatives of \(U\).
This density is the local quadratic-form cost, not the
possibly signed pointwise quotient \(\psi^{-1}H\psi\).

Its next evolution row is also exact. Put
\(\mathcal Q=\int_Y\dot\psi\,\nabla_A\psi\) and
\(\mathcal D=\int_Y\dot\psi^2\). One raw integration by
parts gives
\[
\boxed{
\partial_t\mathcal J
=2\kappa\operatorname{div}_A\mathcal Q
 -2\mathcal D+\bar E\,\partial_tR,\qquad
\mathcal Q=\dot\chi\,\nabla_A\chi+R\jmath^\sharp,\quad
\mathcal D=\dot\chi^2+Rn.
}
\tag{MF28}
\]
Thus integrated dissipation is controlled, but its local
flux and conditional speed are not determined by \(R\)
and \(\mathcal J\) alone. The
[[coarse-response-memory/heat-preparation-and-latitude-coercivity#The density contact equation keeps the local loss curvature|latitude contact equation]]
identifies the resulting shape obligation exactly.
A nonnegative local cost is not the curvature estimate
needed to preserve the marginal bound.

## The binary wall profile is a geometric coefficient, not a mass insertion

Take \(x\) in a compact interval with the ordinary horizontal derivative and a smooth positive marginal law. For
\[
q_x=(p,1-p),\qquad 0<p<1,
\]
the normalized centered mode is
\[
\phi_x=
\left(\sqrt{\frac{1-p}{p}},-\sqrt{\frac{p}{1-p}}\right).
\tag{MF8}
\]
Direct differentiation gives
\[
c=\frac{p'(2p-1)}{2p(1-p)},\qquad
\kappa=\frac{p'}{\sqrt{p(1-p)}},\qquad
\partial_x\phi=-\kappa\,1+c\phi,\qquad
G=\kappa^2=\frac{(p')^2}{p(1-p)}.
\tag{MF9}
\]
For the balanced family \(p=(1+\tanh x)/2\),
\[
c=\tanh x,\qquad
\kappa=\operatorname{sech}x,\qquad
G=\operatorname{sech}^2x.
\tag{MF10}
\]
This is the profile of [[program-core/ruble-equations#RE4 — Balanced binary specialization|the balanced Ruble member]], now appearing in a moving-band form with its operator specified.

Restore both conditional bands, \(F=a_0(x)1+a_1(x)\phi_x\). The complete horizontal energy is
\[
\boxed{
\mathcal E_{\mathrm{hor}}(F)
=\int\left[
|a_0'-\kappa a_1|^2+
|a_1'+c a_1|^2
\right]d\nu.}
\tag{MF11}
\]
The fixed-label observable \(F=(1,0)\) has \(a_0=p\), \(a_1=\sqrt{p(1-p)}\). Both squares vanish identically. A positive \(\operatorname{sech}^2x\) coefficient therefore coexists with zero horizontal energy for a nonconstant hidden observable. A vertical generator may still assign it positive energy; no gaplessness claim about that full generator follows.

The lesson is constructive: retain the whole matrix of band derivatives. A scalar profile or one projected potential cannot replace that matrix. The transport and source selection required by [[wall-construction-interface/inq|the wall-construction interface]] remain essential before calling \(x\) physical scale or identifying this energy with a clock rate. No quantum-field scalar has been added, but no mass has been generated merely by changing notation either.

[[measure-preserving-horizontal-lifts|A law-preserving transport connection]] is another legitimate operator choice: its derivative has a vertical transport term and makes conditional expectation horizontal. It may have nonzero curvature. Its half-density form differs from (MF3), and a separate metric-distortion comparison is required to bound it by the inherited form. This construction does not reverse the cancellation proved above.

[[rg-covariance-residue/receipts/joint_context_escape_receipt.py|The finite receipt]] checks the half-density cancellation, the centered-band coefficients and the complete binary derivative form. It does not select a physical joint law or a scale-to-clock map.
