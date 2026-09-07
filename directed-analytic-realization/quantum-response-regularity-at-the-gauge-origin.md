# Quantum Response Regularity at the Gauge Origin

A nonzero quartic potential cannot be the squared gradient of a \(C^3\) scalar response having a local minimum at its degenerate origin. The homogeneous gauge model nevertheless has a smooth normalizable quantum vacuum whose logarithm has strictly positive quadratic response there. The quantum divergence term changes the equation, rather than repairing a classical eikonal solution by taking a pointwise spectral modulus. Its local stiffness is fixed by the actual global ground state, not by random-jitter assumptions or a supplied excitation gap.

## A quartic classical origin obstructs a smooth minimum

Work near \(0\) in a finite-dimensional real vector space with a fixed positive inner product. Suppose

\[
V(q)-V(0)=V_4(q)+o(|q|^4),
\tag{QR1}
\]

where \(V_4\) is a nonzero nonnegative homogeneous quartic polynomial. There is no \(C^3\) function \(W\) on a neighborhood of zero satisfying both

\[
W(q)\geq W(0),
\qquad
\frac12|\nabla W(q)|^2=V(q)-V(0).
\tag{QR2}
\]

To prove this, the minimum first gives \(\nabla W(0)=0\). If \(B=\operatorname{Hess}W(0)\), evaluation on \(q=tv\) and division of the eikonal identity by \(t^2\) give \(|Bv|^2/2=0\). Thus \(B=0\). Taylor expansion now starts with the homogeneous cubic

\[
W(q)-W(0)=\frac16D^3W(0)[q,q,q]+o(|q|^3).
\tag{QR3}
\]

A nonzero odd cubic changes sign under \(q\mapsto-q\), so the minimum forces this cubic to vanish identically. Polarization gives \(D^3W(0)=0\), and Taylor expansion of the gradient yields \(\nabla W(q)=o(|q|^2)\). Its square is therefore \(o(|q|^4)\), contradicting (QR1) along a direction with \(V_4(v)>0\). The argument rules out even a non-strict local minimum; it does not require strict convexity.

For the [[chern-simons-response-and-gauge-action|homogeneous gauge potential]] at unit volume,

\[
V(Q)=\frac12\|\operatorname{cof}Q\|_{\mathrm F}^2,
\qquad Q\in M_3(\mathbb R),
\tag{QR4}
\]

the direction \(Q=tI\) has \(V(tI)=3t^4/2\). The smooth signed solution \(W=\det Q\) satisfies the eikonal equation but has no minimum at zero. The theorem shows why a different smooth positive-minimum scalar response cannot simply replace it through the origin while preserving the same classical squared potential.

The regularity qualification is essential. The [[algebra/nonlinear-response-and-clock-realization|one-coordinate stable-branch example]] has

\[
V(q)=\frac12q^4,
\qquad W_{\rm st}(q)=\frac13|q|^3,
\qquad W_{\rm st}'=q|q|.
\tag{QR5}
\]

It has a minimum and solves the eikonal equation, but \(W_{\rm st}\) is \(C^2\), not \(C^3\), at zero. Thus the obstruction does not exclude lower-regularity value functions, signed responses, or branches defined away from the degenerate point. Nor does this one-coordinate example establish such a global branch for the matrix potential.

## The actual quantum state obeys a different equation

Use the [[homogeneous-gauge-positive-realization|positive homogeneous realization]], with supplied volume \(\mathcal V>0\), abstract quantization parameter \(\epsilon>0\), and an optional constant potential shift \(C\):

\[
H_{\epsilon,\mathcal V}
=-\frac{\epsilon^2}{2\mathcal V}\Delta_Q+V_{\rm tot}(Q),
\qquad
V_{\rm tot}(Q)=\frac{\mathcal V}{2}\|\operatorname{cof}Q\|_{\mathrm F}^2+C.
\tag{QR6}
\]

That construction proves compact resolvent and a unique smooth strictly positive normalized ground state \(\psi_0\), with energy \(E_0\). In particular \(E_0-C>0\). Define the actual quantum response function

\[
W_0=-\epsilon\log\psi_0.
\tag{QR7}
\]

It is smooth because \(\psi_0\) is everywhere positive. Direct substitution of the ground-state equation gives

\[
\boxed{
V_{\rm tot}-E_0
=\frac1{2\mathcal V}|\nabla W_0|^2
-\frac\epsilon{2\mathcal V}\Delta_QW_0.}
\tag{QR8}
\]

The divergence term and the ground-energy subtraction distinguish this quantum Hamilton–Jacobi identity from (QR2). The [[algebra/response-factorization-and-the-vacuum|factorization theorem]] owns the general metric, measure and domain requirements. Here \(W_0\) is obtained from the independently constructed positive operator, not postulated to equal the transgression.

## Symmetry fixes the local stiffness

Set

\[
s=\operatorname{Tr}(QQ^T),
\qquad t=\operatorname{Tr}((QQ^T)^2),
\qquad V_{\rm tot}-C=\frac{\mathcal V}{4}(s^2-t).
\tag{QR9}
\]

Both kinetic term and potential are invariant under \(Q\mapsto RQS\), with \(R,S\in O(3)\). This is a larger symmetry of the bosonic mechanical Hamiltonian: only simultaneous proper color rotations form its \(SU(2)\) adjoint gauge action. The full orthogonal product must not be called its gauge group.

The unique positive ground state inherits these symmetries, and so does \(W_0\). Row and column sign flips force \(\nabla W_0(0)=0\) and eliminate every off-diagonal Hessian entry. Row and column permutations make all nine diagonal entries equal. Hence

\[
\operatorname{Hess}_{Q}W_0(0)=\kappa I_9.
\tag{QR10}
\]

Evaluation of (QR8) at zero now fixes this coefficient:

\[
\boxed{
\kappa=\frac{2\mathcal V\,[E_0-V_{\rm tot}(0)]}{9\epsilon}>0.}
\tag{QR11}
\]

The energy difference makes the statement independent of adding a constant to the potential. With the actual configuration metric \(g=\mathcal V I\), the response is \(N_0=\operatorname{grad}_gW_0\), and its linearization is

\[
DN_0(0)=\frac\kappa{\mathcal V}I_9
=\frac{2[E_0-V_{\rm tot}(0)]}{9\epsilon}I_9.
\tag{QR12}
\]

Thus the origin is a strict local minimum of the actual smooth quantum response. This is not a global convexity theorem. The energy above the potential's minimum in (QR11) is also not the excitation gap \(E_{1,\rm inv}-E_0\).

## Higher jets retain the quantization dependence

At unit volume, orthogonal-product invariance gives the fourth-order expansion

\[
W_0(Q)=W_0(0)+\frac\kappa2s+a s^2+b t+O(|Q|^6).
\tag{QR13}
\]

Indeed singular-value decomposition reduces an invariant quartic polynomial to a symmetric quadratic polynomial in the three squared singular values; its two generators are \(s^2\) and \(t\). Odd Taylor terms vanish under \(Q\mapsto-Q\). Direct differentiation gives

\[
\Delta_Qs^2=44s,
\qquad \Delta_Qt=28s.
\tag{QR14}
\]

The degree-two part of (QR8) consequently requires

\[
\boxed{44a+28b=\kappa^2/\epsilon.}
\tag{QR15}
\]

This constrains the actual state's fourth jet but determines neither coefficient separately.

Let \(e_0=E_0(1,1)\) in the zero-offset convention. The homogeneous dilation theorem gives

\[
\kappa=\frac{2e_0}{9}\epsilon^{1/3}\mathcal V^{2/3},
\qquad
\frac\kappa{\mathcal V}
=\frac{2e_0}{9}(\epsilon/\mathcal V)^{1/3}.
\tag{QR16}
\]

In particular, at unit volume the positive combination (QR15) grows as \(\epsilon^{-1/3}\). At least one fourth-jet coefficient is unbounded as \(\epsilon\downarrow0\), so these responses have no uniform \(C^4\) control near the origin. Equivalently, normalized ground-state dilation gives
\(W_\epsilon(Q)=\mathrm{constant}(\epsilon)+\epsilon W_1(Q/\epsilon^{1/3})\); derivatives of order \(n\geq1\) scale with factor \(\epsilon^{1-n/3}\). This fourth-order conclusion alone is not a statement about \(C^3\) convergence.

## An explicit coupling makes the singular free limit visible

Optionally restore a real coupling \(g\) through
\(F=dA+(g/2)[A,A]\), while keeping the kinetic normalization fixed. With \(U_4=\|\operatorname{cof}Q\|_{\mathrm F}^2/2\), the homogeneous operator becomes

\[
H_{\epsilon,\mathcal V,g}
=-\frac{\epsilon^2}{2\mathcal V}\Delta_Q
+\mathcal V g^2 U_4(Q)+C.
\tag{QR17}
\]

For \(g\ne0\), the unitary dilation \(Q=\ell X\), with
\(\ell=(\epsilon/(\mathcal V|g|))^{1/3}\), gives the common spectral factor

\[
\lambda=\epsilon^{4/3}\mathcal V^{-1/3}|g|^{2/3},
\qquad
E_n-C=\lambda e_n,
\qquad \Delta_{\rm inv}=\lambda\delta_{\rm inv}.
\tag{QR18}
\]

Here \(e_n\) and \(\delta_{\rm inv}>0\) are the corresponding unit-parameter spectral constants, not fitted numbers. Equation (QR11) consequently becomes

\[
\boxed{
\kappa=\frac{2e_0}{9}
\epsilon^{1/3}\mathcal V^{2/3}|g|^{2/3}.}
\tag{QR19}
\]

The positive quantum response and gap are nonanalytic at the free endpoint \(g=0\); no massive free response operator was inserted. At that endpoint the operator is the free Laplacian plus \(C\), with no normalizable ground state on \(\mathbb R^9\), so an isolated vacuum cannot be analytically continued from \(g=0\) by assumption. This is an exact coupling law of the homogeneous model with its stated kinetic normalization, not a continuum Yang–Mills beta function or a proposed replacement for its nonperturbative scaling law.

The distinction is structural: a classical quartic eikonal minimum has a regularity obstruction, while the quantum divergence equation admits a smooth state-selected positive slope at every fixed \(\epsilon\). No premise of intrinsic stochastic jitter is needed for this deduction. The metric, positive kinetic law, quantization parameter and homogeneous carrier remain explicit inputs; neither local stiffness nor its scaling establishes a physical continuum mass gap.

The [[cubic-gauge-boundary-response-and-gauss-completion|spatial cubic construction]] exposes the same quartic harmonic sector as an obstruction to a particular free-response recursion. It does not supply the field-theoretic counterpart of (QR8). The [[gauge_boundary_response_receipt.py|finite receipt]] verifies the invariant quartic Laplacians and scaling identities, without computing \(E_0\), \(\kappa\), or the excitation gap numerically.

There is nevertheless a local geometric consumer of the actual state. On the small convex neighborhood supplied by (QR11), [[algebra/opposed-response-polarization-and-kahler-completion|opposed response polarization]] constructs explicit compatible complex tensors from two Hessians of this same \(W_0\). At the paired origin their geometric and arithmetic means both equal \(\kappa I_9\). This is response geometry on configuration pairs, not physical three-space; the local input does not grant global convexity or identify the actual state's higher jets with a family admitting a complete circle clock.
