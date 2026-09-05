# Heat Envelopes and the Vacuum Vector

A complete prediction envelope must preserve the actual vacuum, not merely the underlying configuration space. Transporting an interacting stationary law to a Haar carrier moves its constant function to the Perron vector. A unit-prefactor comparison with the original Haar heat then usually fails; even an arbitrary finite prefactor can fail for an analytic, genuinely gapped compact Schrödinger model. The obstruction concerns the comparison, not the existence of a physical gap.

**Status: [EXACT] operator obstruction, rank-one criterion, circle example and centered-compression bound; [CONDITIONAL] same-state comparison routes; [OPEN] for uniform interacting Yang--Mills estimates.** [[inq|Vacuum-aligned completion]] owns the complete centered carrier. [[bridge-score-fusion-geometry/volume-uniform-fusion-envelopes|The compact fusion envelope]] supplies the Haar result whose physical transport is being tested.

## A full envelope has to fix the right vector

Let \(\mu\) be a reference probability measure, \(\psi>0\) normalized in \(L^2(\mu)\), and \(\nu=\psi^2\mu\). The isometry
\[
U_\psi:L^2(\nu)\longrightarrow L^2(\mu),\qquad U_\psi f=\psi f
\]
is unitary. For an actual midpoint predictor \(K_\nu\), its return operator \(S_\nu=K_\nu^*K_\nu\) is a positive contraction fixing \(1\). Thus
\[
A:=U_\psi S_\nu U_\psi^{-1},\qquad
A\psi=\psi,\qquad \Pi_\psi\le A\le I.
\tag{HV1}
\]
If a reference \(L\ge0\) has \(\ker L=\mathbb C1\), then for \(b>0\),
\[
\boxed{A\le e^{-bL}\quad\Longrightarrow\quad \psi\in\ker L.}
\tag{HV2}
\]
Indeed \(1=\langle\psi,A\psi\rangle\le\langle\psi,e^{-bL}\psi\rangle\le1\), so the spectral measure of \(\psi\) is supported at zero. A nonconstant interacting vacuum therefore forbids this full unit-prefactor Haar-heat comparison.

A finite prefactor is not an automatic repair. The rank-one inequality
\(\Pi_\psi\le C e^{-bL}\) holds for some finite \(C\) exactly when
\(\psi\in D(e^{bL/2})\), and its optimal constant is
\[
\boxed{C_{\min}=\|e^{bL/2}\psi\|^2.}
\tag{HV3}
\]
Weighted Cauchy--Schwarz proves sufficiency; testing on truncated spectral inverse images proves necessity. Since \(A\ge\Pi_\psi\), (HV3) is a necessary condition for \(A\le C e^{-bL}\), not a sufficient condition for the complete operator.

## An analytic gapped vacuum can fail every finite-prefactor test

On the circle with normalized Haar \(d\theta/(2\pi)\), choose \(\kappa>0\) and
\[
L=-\partial_\theta^2,\qquad
\psi_\kappa(\theta)=Z_\kappa^{-1/2}e^{\kappa\cos\theta},\qquad
Z_\kappa=\int e^{2\kappa\cos\theta}\frac{d\theta}{2\pi}.
\tag{HV4}
\]
Define \(D=\partial_\theta+\kappa\sin\theta\). Periodic integration by parts gives
\[
H=D^*D
=-\partial_\theta^2+\kappa^2\sin^2\theta-\kappa\cos\theta,\qquad
D\psi_\kappa=0.
\tag{HV5}
\]
The potential is bounded and analytic. The first-order equation makes the periodic kernel one-dimensional; ellipticity on the compact circle gives compact resolvent and a strictly positive gap above that vacuum. Its ground-state transform supplies an honest stationary reversible diffusion and hence actual midpoint bridges satisfying (HV1).

Put \(z=e^{i\theta}\). Multiplication of the two absolutely convergent series
\[
e^{\kappa(z+z^{-1})/2}=e^{\kappa z/2}e^{\kappa z^{-1}/2}
\]
gives, for \(n\ge0\),
\[
a_n=\sum_{r\ge0}
\frac{(\kappa/2)^{n+2r}}{(n+r)!\,r!}
\ge\frac{(\kappa/2)^n}{n!},\qquad
\widehat\psi_\kappa(n)=a_n/\sqrt{Z_\kappa}.
\]
Consequently, for every \(b>0\),
\[
e^{bn^2}|\widehat\psi_\kappa(n)|^2
\ge Z_\kappa^{-1}
\exp\!\left[bn^2+2n\log(\kappa/2)-2n\log n\right]
\longrightarrow\infty.
\tag{HV6}
\]
Testing \(A\le C e^{-bL}\) on Fourier unit vectors contradicts (HV6) for every finite \(C\). Thus analyticity of the vacuum and positivity of the true gap do not supply a Gaussian electric-frequency envelope on the uncentered Haar carrier.

The distinction persists under products. The sum of \(N\) copies of (HV5) has the same positive one-copy gap; a high Fourier mode in one coordinate still defeats every finite prefactor. Failure of the envelope is not failure of volume-independent physical coercivity.

## Centering avoids that obstruction but changes the statement

Let \(Q_\psi=I-\Pi_\psi\). A possible comparison is instead
\[
Q_\psi A Q_\psi\le Q_\psi e^{-bL}Q_\psi,
\quad\text{equivalently}\quad
A\le\Pi_\psi+Q_\psi e^{-bL}Q_\psi.
\tag{HV7}
\]
It is not excluded by (HV2). If \(L\ge\lambda_H(I-\Pi_1)\) and \(v\perp\psi\), then
\[
\langle v,e^{-bL}v\rangle
\le\left[1-(1-e^{-b\lambda_H})|\langle1,\psi\rangle|^2\right]\|v\|^2.
\tag{HV8}
\]
To see the overlap factor, use
\(|\langle1,v\rangle|^2\le(1-|\langle1,\psi\rangle|^2)\|v\|^2\).
The compressed reference family need not be a Markov kernel or a semigroup. Its reference floor is useful only after the actual comparison (HV7) is proved.

Moreover, the overlap can decay exponentially in product size. For the circle example,
\[
|\langle1,\psi_\kappa^{\otimes N}\rangle|^2
=\left[
\frac{\bigl(\int e^{\kappa\cos\theta}\,d\theta/(2\pi)\bigr)^2}
{\int e^{2\kappa\cos\theta}\,d\theta/(2\pi)}
\right]^N\longrightarrow0.
\tag{HV9}
\]
Strict Cauchy--Schwarz makes the bracket smaller than one. The true product gap stays positive, so this loss is another limitation of a comparison certificate.

## The adapted differential operator is the existing physical transform

On a smooth finite compact link carrier, take \(L=\nabla^*\nabla\) with reference adjoint, and smooth positive \(\psi\). The form
\(\int|\nabla f|^2\,d\nu\) has generator
\[
L_\nu=\psi^{-2}\nabla^*(\psi^2\nabla),\qquad
U_\psi L_\nu U_\psi^{-1}=L-M_{(L\psi)/\psi}.
\tag{HV10}
\]
If \(H=\eta L+V\), where \(V\) is a real multiplication potential, \(\eta>0\), and \(H\psi=E_0\psi\), this becomes
\[
\eta L_\nu=U_\psi^{-1}(H-E_0)U_\psi.
\tag{HV11}
\]
The [[contemporary-puzzles/yang-mills-mass-gap/gauge-descent-flux-fisher-coercivity|ground-state flux theorem]] already owns this exact identification. It requires the stated differential Hamiltonian and closed-form domains; a finite-spacing Wilson transfer logarithm need not have that form. The kinetic conversion \(\eta\) remains supplied, not independently predicted by renaming \(L_\nu\).

The practical correction is to compare operators on the same pointed carrier. [[markov-edge-measure-solder/inq|Stationary edge-measure comparison]] offers a sufficient route: an independently specified \(\nu\)-reversible reference \(R_\nu\) and actual return \(S_\nu\), with edge domination, yield
\[
I-S_\nu\ge c(I-R_\nu).
\]
For example \(R_\nu=(I+sA_\nu)^{-1}\) is Markov when \(A_\nu\) generates a \(\nu\)-reversible Markov semigroup, by exponential-time averaging. An independently proved reference gap \(\lambda_A\) would give the response floor \(cs\lambda_A/(1+s\lambda_A)\). Neither the edge comparison nor the reference gap is provided by (HV10) alone.

The distinguished state is therefore part of the operator's type. This is a concrete constraint on the proposed global--local construction, not a proof that QFT is inconsistent or that mass is a new substance. [[receipts/vacuum_heat_envelope_receipt.py|The receipt]] tests the finite rank-one criterion, centered overlap bound and circle factorization; the infinite obstruction is proved by (HV6).
