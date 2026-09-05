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
