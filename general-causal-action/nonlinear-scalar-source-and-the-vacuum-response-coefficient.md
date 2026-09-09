# The Nonlinear Scalar Response Retains the Moving Vacuum

The first nonlinear coefficient of the planar scalar-source susceptibility is a finite oscillator-resolvent calculation once the actual kinetic, Haar and source jets are supplied. Parity removes the term linear in the confinement scale parameter, while two first-order virtual transitions still contribute at second order. Because the harmonic source occupies one exact physical eigenmode, its second-order shape correction cancels from the normalized susceptibility. The remaining coefficient contains both the shifted excitation energy and leakage into other modes, so it is not determined by the energy shift alone.

**Status: exact finite coefficient identities for the stated jets; compact realization and remainder control are separate inputs.** [[planar-patch-confinement-and-the-spatial-soft-mode|PP9–12]] fixes the actual compact source and its harmonic limit. [[quartic-seam-eigenvalues-and-the-generalized-pencil|QP]] and [[seam-coupling-response-and-the-vacuum-cap|SV17–21]] fix the need to retain vacuum normalization and source centering. [[compact-source-normalization-and-the-nonlinear-return|The compact-source return]] supplies the realization estimates needed to apply these identities to the original operator. Nothing here assigns a size-independent nonlinear mass term.

## Expand the actual operator and actual marked source

Fix the patch size \(L\), put \(h=(\kappa/g)^{1/4}\), and use the exact local face chart, Haar half-density and dilation from PP. In scaled energy units, write the operator jets as
\[
\widehat H_h=\mathcal O+hV_1+h^2V_2+o(h^2),
\qquad \mathcal O=\mathcal O_L.
\tag{NV1}
\]
The jets \(V_1,V_2\) must come from the original raw-edge kinetic operator, including the actual coordinate metric and Haar-density terms. The magnetic quartic contribution to \(V_2\) is
\(-\sum_p|X_p|^4/192\); it is not the whole operator jet. All computations below take place in the simultaneous-rotation-invariant oscillator carrier.

Equation (NV1) is a local asymptotic expansion on polynomial-Gaussian vectors. It does not define the global Hamiltonian by truncating its potential: the negative quartic Taylor term alone would not be a confining potential at infinity.

Let \(v_p=v_{11}(p)\), \(Y=\sum_pv_pX_p\), and rescale PP12's compact source by \(B_h=4\mathcal B_L/h^2\). Since
\[
\mathbf q_p(hX_p)
=\frac h2X_p-\frac{h^3}{48}|X_p|^2X_p+O(h^5|X_p|^5),
\]
its multiplication jets are
\[
\boxed{B_h=B_0+h^2B_2+O(h^4),\qquad
B_0=|Y|^2,\qquad
B_2=-\frac1{12}Y\cdot\sum_pv_p|X_p|^2X_p.}
\tag{NV2}
\]
The half-density transformation does not alter a multiplication source. Multiplying the compact source by \(4/h^2\) also does not alter its variance-normalized susceptibility.

Let \(\mathcal P\) be total normal inversion, \(X\mapsto-X\). Taylor degree gives
\[
\mathcal P\mathcal O\mathcal P=\mathcal O,
\quad \mathcal PV_1\mathcal P=-V_1,
\quad \mathcal PV_2\mathcal P=V_2,
\quad \mathcal PB_i\mathcal P=B_i\quad(i=0,2).
\tag{NV3}
\]
This is the parity of the scaled jets. It does not assume that simultaneous inversion of the compact non-Abelian holonomies preserves the original Hamiltonian. In particular \(V_1\) need not vanish.

## Normalize the vacuum before centering the source

Let \(\Omega\) be the normalized oscillator vacuum, of energy \(E_0\), and set
\[
K=\mathcal O-E_0,\quad Q=I-|\Omega\rangle\langle\Omega|,
\quad R=QK^{-1}Q.
\]
The inverse is the known harmonic reduced resolvent at this fixed patch. Write ordinary coefficients
\[
E_h=E_0+h^2e_2+o(h^2),\qquad
\psi_h=\Omega+hu+h^2v+o(h^2),
\]
with \(\|\psi_h\|=1\) and positive overlap with \(\Omega\). Then
\[
\boxed{u=-RV_1\Omega,\qquad
e_2=\langle\Omega,V_2\Omega\rangle
-\langle V_1\Omega,RV_1\Omega\rangle,}
\]
\[
\boxed{v=-R(V_1u+V_2\Omega)-\frac12\|u\|^2\Omega.}
\tag{NV4}
\]
The first vacuum correction \(u\) is odd and \(v\) is even. The last scalar in (NV4) is fixed by normalization. The linear energy coefficient vanishes by (NV3).

Define the actual source mean \(m_h=\langle\psi_h,B_h\psi_h\rangle\). Its linear coefficient also vanishes, while
\[
m_0=\langle\Omega,B_0\Omega\rangle,
\]
\[
\boxed{m_2=\langle u,B_0u\rangle
+2\operatorname{Re}\langle\Omega,B_0v\rangle
+\langle\Omega,B_2\Omega\rangle.}
\tag{NV5}
\]
Put \(b_h=B_h-m_h\) and \(F_h=b_h\psi_h\). The centered vector has coefficients
\[
F_0=(B_0-m_0)\Omega,\quad F_1=(B_0-m_0)u,
\]
\[
F_2=(B_0-m_0)v+(B_2-m_2)\Omega.
\tag{NV6}
\]
Although \(\langle\psi_h,F_h\rangle=0\), the vector \(F_2\) need not be orthogonal to \(\Omega\). It satisfies the moving-orthogonality condition
\[
\langle\Omega,F_2\rangle+
\langle u,F_1\rangle+\langle v,F_0\rangle=0.
\]
For the variance \(N_h=\|F_h\|^2\),
\[
\boxed{N_h=N_0+h^2N_2+o(h^2),\quad
N_0=\|F_0\|^2,\quad
N_2=\|F_1\|^2+2\operatorname{Re}\langle F_0,F_2\rangle.}
\tag{NV7}
\]
These formulas include the second vacuum vector, the source curvature and the changed mean. No linear term survives because \(F_0,F_2\) are even and \(F_1\) is odd.

## An inhomogeneous resolvent gives the complete coefficient

Let \(K_h=\widehat H_h-E_h\), and let \(R_h\) be its inverse on the actual vacuum complement. The unnormalized and normalized susceptibilities are
\[
T_h=\langle F_h,R_hF_h\rangle,
\qquad S_h=T_h/N_h.
\]
Solve \(K_hy_h=F_h\), \(\langle\psi_h,y_h\rangle=0\), coefficient by coefficient. With \(y_0=RF_0\), parity gives
\[
y_1=R(F_1-V_1y_0).
\]
The second vector is
\[
y_2=R\{F_2-V_1y_1-(V_2-e_2)y_0\}+c_2\Omega,
\quad
c_2=-\langle u,y_1\rangle-\langle v,y_0\rangle.
\]
The scalar enforces moving vacuum orthogonality; it drops from \(\langle F_0,y_2\rangle\), not from the underlying equation. Combining the three numerator terms gives
\[
\boxed{
T_2=2\operatorname{Re}\langle F_2,y_0\rangle
+\langle q,Rq\rangle
-\langle y_0,(V_2-e_2)y_0\rangle,
\qquad q=F_1-V_1y_0.}
\tag{NV8}
\]
Thus
\[
\boxed{S_h=S_0+h^2S_2+o(h^2),\qquad
S_0=\frac{\langle F_0,RF_0\rangle}{N_0},\qquad
S_2=\frac{T_2-S_0N_2}{N_0}.}
\tag{NV9}
\]
Equations (NV4)–(NV9) are an explicit finite algorithm from \(V_1,V_2,B_0,B_2\). In particular, discarding \(V_1\) because the linear response vanishes would discard the quadratic virtual transitions in both \(e_2\) and (NV8).

## The harmonic single-mode source cancels its direct shape correction

For PP's source, let \(\lambda=\lambda_{\min}(A_L)\). The exact Gaussian data are
\[
m_0=3\sqrt\lambda,\qquad N_0=6\lambda,\qquad
F_0=\sqrt{N_0}\,\phi,\quad K\phi=\delta\phi,
\quad \delta=2\sqrt\lambda,
\tag{NV10}
\]
where \(\phi\) is the normalized first physical scalar excitation. It is simple on the invariant carrier. With \(y_0=F_0/\delta\), the \(F_2\) terms in (NV8) and (NV7) cancel exactly:
\[
\boxed{
S_2=\frac1{N_0}\left[
\left\langle F_1-\frac{V_1F_0}{\delta},
R\left(F_1-\frac{V_1F_0}{\delta}\right)\right\rangle
-\frac{\|F_1\|^2}{\delta}
-\frac{\langle F_0,(V_2-e_2)F_0\rangle}{\delta^2}
\right].}
\tag{NV11}
\]
The source curvature \(B_2\), second vacuum vector \(v\), and mean coefficient \(m_2\) still affect the variance and unnormalized response at this order. Their cancellation is specific to this normalized response with a single-mode harmonic starting vector.

There is a useful spectral form of the same identity. Let
\[
R_\phi=(K-\delta)^{-1}\quad\text{on }\phi^\perp,
\qquad R_\phi\phi=0,
\]
**within the physical invariant carrier**. On the full colored oscillator space, the energy \(\delta\) has non-scalar degeneracies, so deleting only \(\phi\) there would not define this inverse. Define
\[
\eta_1=-R_\phi V_1\phi,
\qquad
\delta_2=\langle\phi,V_2\phi\rangle
-\langle V_1\phi,R_\phi V_1\phi\rangle-e_2,
\]
\[
\boxed{\ell=\frac{F_1}{\sqrt{N_0}}-\eta_1.}
\tag{NV12}
\]
The actual first excitation gap has coefficient \(\delta_h=\delta+h^2\delta_2+o(h^2)\). The vector \(\ell\) is the first difference between the normalized source vector and the changing excited eigenvector. It is odd and orthogonal to both \(\Omega\) and \(\phi\). If \(P_{1,h}\) is the continued first-excitation projection, its leakage is
\[
\boxed{
\left\|(I-P_{1,h})\frac{F_h}{\sqrt{N_h}}\right\|^2
=h^2\|\ell\|^2+o(h^2),
\qquad
S_2=-\frac{\delta_2}{\delta^2}
+\langle\ell,(R-\delta^{-1}I)\ell\rangle.}
\tag{NV13}
\]
The source is exactly centered against the actual vacuum, so this leakage has no vacuum component. Every other physical excitation has energy greater than \(\delta\); the second term in (NV13) is therefore nonpositive, and strictly negative if \(\ell\ne0\). A softening first excitation can coexist with a smaller normalized susceptibility when the leakage term dominates. The coefficient is not an abstract sign argument: each matrix element is determined by the specified jets and known oscillator denominators.

If \(V_1\Omega=V_1\phi=0\), then \(F_1=\eta_1=\ell=0\), and \(S_2=-\delta_2/\delta^2\). Under a regular higher-order expansion, leakage then starts at order \(h^4\) in squared norm. It is not permissible to assume this simplification on a multi-face patch without evaluating its odd kinetic jet.

## The covariance keeps the same leakage information

At any fixed scaled duration \(\tau\ge0\), let
\[
\mathcal C_h(\tau)
=\frac{\langle F_h,e^{-\tau K_h}F_h\rangle}{N_h}.
\]
The same spectral expansion gives
\[
\boxed{\mathcal C_h(\tau)
=e^{-\tau\delta}
+h^2\left[-\tau\delta_2e^{-\tau\delta}
+\langle\ell,(e^{-\tau K}-e^{-\tau\delta}I)\ell\rangle\right]
+o(h^2).}
\tag{NV14}
\]
Multiplying by \(N_h\) restores the unnormalized covariance, whose second coefficient includes \(N_2e^{-\tau\delta}\). At \(\tau=0\), the normalized correction is zero, as required. Integrating (NV14) in \(\tau\), with the fixed-patch reduced-gap control, gives (NV13).

For the innovation quotient at \(\tau>0\), set \(c_h(t)=\mathcal C_h(t)\) and
\[
\mathfrak r_h(\tau)=
\frac{1-2c_h(2\tau)+c_h(4\tau)}{1-c_h(2\tau)}.
\]
If \(c_h(t)=e^{-t\delta}+h^2c_2(t)+o(h^2)\), then its ordinary second coefficient is
\[
\boxed{\mathfrak r_2(\tau)
=\frac{c_2(4\tau)-(1+e^{-2\tau\delta})c_2(2\tau)}
{1-e^{-2\tau\delta}}.}
\tag{NV15}
\]
This retains the moving variance and both chronological moments, in the same manner as SV20–21. It is not obtained by replacing the source quotient with the first eigenvalue.

## What makes the calculation finite, and what realizes it

For smooth metric and density jets of a second-order kinetic operator, \(V_1\) raises polynomial-Gaussian degree by at most three and \(V_2\) by at most four. The source degrees are two and four. Thus \(u,v,F_1,F_2\) have degrees at most \(3,6,5,8\), respectively. Harmonic reduced resolvents preserve every finite Hermite-degree span. In (NV11)–(NV14), the reduced-resolvent inputs lie in Hermite degrees at most five; the direct \(V_2\) expectations are finite Gaussian contractions and require no inverse in a higher sector. The direct mean and variance ledger closes through degree eight. The number of coordinates is finite at each \(L\); no finite spectral cutoff is being used to approximate a missing transition.

The denominators are sums of the known frequencies \(\sqrt{\lambda_{rs}}\), with the specified ground or first-scalar energy removed. They are properties of the already proved harmonic problem. This does not insert an unknown nonlinear gap into the coefficient formula.

To identify these finite coefficients with the actual compact response requires all of the following, at the fixed patch:

- The actual chart and Haar half-density must supply \(V_1,V_2\), including all first-order and scalar kinetic terms, with controlled local Taylor remainders on the polynomial-Gaussian vectors used above.
- Equivariant localization and sufficiently accurate normalized vacuum quasimodes must justify multiplication by the scaled compact source. Its operator norm is \(O_L(h^{-2})\), so an unweighted vacuum error merely \(o(h^2)\) is insufficient. An error \(o(h^4)\), or an appropriate stronger weighted estimate, suffices for its source-vector coefficient through \(h^2\).
- The actual fixed-patch reduced gap and an inhomogeneous quasimode construction must control the Poisson solution, moving projection and remainder in (NV8). Covariance coefficients require the corresponding finite-time spectral or evolution control. The linked compact-source return treats these realization steps.

All coefficient subscripts here denote ordinary powers of \(h\); a second derivative with respect to \(h\) is twice its coefficient. The susceptibility is in scaled energy units. The actual unscaled variance-normalized susceptibility is \(S_h/\sqrt{\kappa g}\), while the first physical gap is
\[
\Delta_L(g)=\sqrt{\kappa g}\,\delta+\kappa\delta_2+o_L(\kappa)
\tag{NV16}
\]
when the required expansion is realized. The values, signs and \(L\)-dependence of \(\delta_2\), \(\ell\) and the complete source coefficient must still be calculated from the actual jets. The fixed-patch construction supplies neither constants uniform as \(\lambda_{\min}\to0\) nor an exchange of spatial-size and confinement limits.
