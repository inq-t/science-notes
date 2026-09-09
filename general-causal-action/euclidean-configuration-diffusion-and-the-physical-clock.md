# Euclidean Configuration Diffusion and the Physical Clock

A reversible diffusion of the complete Euclidean field history can preserve the correct field measure while giving the wrong temporal response on its actual time-zero observables. In the exact Gaussian control, the inherited slice correlation is an \(\operatorname{erfc}\) profile; the physical slice transfer gives an exponential. Two frequencies exclude even a common nonlinear recalibration of those clocks. Temporal half-space sewing instead returns the correct boundary state and its square-root spatial response directly from the same quadratic action.

**Status: exact for the stated Abelian Gaussian model; conditional as a discriminator of the accelerated nonlinear exchange.** [[many-copy-exchange-and-the-weighted-diffusion|MD]] proves the smooth-source form returned by [[determinant-response-sewing-and-relational-rigidity#Conditional boundary exchange and its clock test|DS10d's accelerated exchange]] at fixed graph. Its continuation to a whole-history continuum diffusion is the hypothesis tested here; that continuation and a non-Abelian mass-gap conclusion are not proved. [[reciprocal-coefficients-and-the-field-gap-test|The field-gap test]] owns the transverse spatial dispersion; this note tests which operation deserves its physical clock.

## Fix the physical modes and retain the history

Use the finite transverse cochain space \(\mathcal T\) of FG1–2: longitudinal gauge directions are removed, and harmonic zero modes are explicitly held fixed. Thus \(K=d_1^*d_1>0\) on \(\mathcal T\). Declare positive electric and magnetic coefficients \(a,b\), and put
\[
H=\frac12\left[a\|P\|^2+b\,q^TKq\right],
\qquad
\Omega=(abK)^{1/2},
\qquad
\Omega_j=\sqrt{ab}\,\nu_j>0.
\tag{PC1}
\]
Here \(K\) has eigenvalues \(\nu_j^2\); \(a\) is a coefficient, not a lattice spacing. This is the oscillator decomposition already obtained in FG3–8.

The corresponding Euclidean history has geometric time coordinate \(\tau\) and quadratic action
\[
S_E[q]=\frac1{2a}\int_{\mathbb R}
\left(\|\partial_\tau q\|^2+q^T\Omega^2q\right)d\tau,
\qquad
M=\frac{-\partial_\tau^2+\Omega^2}{a}.
\tag{PC2}
\]
Its centered Gaussian law \(\mu_E\) has covariance \(M^{-1}\), or, in Euclidean frequency \(p_0\),
\[
C_E(p_0,j)=\frac{a}{p_0^2+\Omega_j^2}.
\tag{PC3}
\]
These are exact physical transverse modes of the noncompact Abelian Gaussian theory. For a compact non-Abelian theory they are only its stated quadratic control.

Every finite-dimensional calculation below can first be made with a finite periodic temporal interval and a frequency cutoff. Remove that cutoff and then take the temporal interval to infinity at fixed positive \(\Omega_j\). Formula (PC3) defines the resulting Gaussian history without a fictitious infinite-dimensional Lebesgue measure. Evaluation at \(\tau=0\) exists as the Gaussian limit of temporal smearings because its covariance integral is finite. The spatial inventory remains finite throughout the clock comparison.

## The full configuration diffusion has an additional time

Assume that the accelerated comparison becomes the positive weighted-gradient generator on the entire Euclidean configuration,
\[
L_{\rm hist}
=-d\,\mu_E^{-1}\operatorname{div}(\mu_E\nabla)
=d\left[-\Delta+(Mq)\cdot\nabla\right],
\qquad d>0.
\tag{PC4}
\]
The scalar \(d\) admits any one common clock normalization. Its value is not fitted separately to different modes. The semigroup is \(e^{-sL_{\rm hist}}\); its parameter \(s\) measures configuration resampling and is distinct from the coordinate \(\tau\) in (PC2).

At a finite temporal regulator, (PC4) is an Ornstein–Uhlenbeck generator. The stationary process satisfies
\[
dq_s=-dMq_s\,ds+\sqrt{2d}\,dW_s,
\qquad
C_{\rm hist}(s)=\mathbb E[q_s q_0^T]=M^{-1}e^{-dsM}.
\tag{PC5}
\]
In particular its linear Fourier rates are
\[
\lambda_{\rm hist}(p_0,j)=\frac d a(p_0^2+\Omega_j^2).
\tag{PC6}
\]
These formulae follow by solving the linear stochastic equation; \(dM M^{-1}+M^{-1}dM=2dI\) verifies the stationary covariance.

The complete Gaussian source response is fixed, not just its spectral edge. For real temporally regulated source vectors \(f_\ell\) inserted at resampling times \(s_\ell\),
\[
\mathbb E\exp\!\left(i\sum_\ell f_\ell^Tq_{s_\ell}\right)
=
\exp\!\left[
-\frac12\sum_{\ell,m}
f_\ell^T M^{-1}e^{-d|s_\ell-s_m|M}f_m
\right].
\tag{PC7}
\]
This uses an ordinary characteristic function, without the complex conjugation convention of an operator inner product. It determines every bounded Weyl-source correlation. Differentiation supplies polynomial marks with their Gaussian integrability.

For real symmetric matrices \(B,D\), let
\(F_B(q)=q^TBq-\operatorname{Tr}(BM^{-1})\). Wick's identity gives
\[
\mathbb E[F_B(q_s)F_D(q_0)]
=
2\operatorname{Tr}
\left[B C_{\rm hist}(s)D C_{\rm hist}(s)^T\right].
\tag{PC8}
\]
All expectations use the original source-free law. Inserting sources does not recompute the reference measure or its clock.

## The same history has a different physical slice transfer

The time-zero marginal of \(\mu_E\) is
\[
d\mu_0(q)=|\psi_0(q)|^2dq,
\qquad
\psi_0(q)\propto
\exp\!\left[-\frac1{2a}q^T\Omega q\right],
\qquad
\Sigma_0=\mathbb E_{\mu_0}[qq^T]=\frac a2\Omega^{-1}.
\tag{PC9}
\]
Indeed each mode has variance
\(\int_{\mathbb R}a(p_0^2+\Omega_j^2)^{-1}dp_0/(2\pi)=a/(2\Omega_j)\).
Thus the following comparison retains the correct equal-time state.

The actual Euclidean slice transfer of (PC1), centered at
\(E_0=\tfrac12\operatorname{Tr}\Omega\), has ground-state transform
\[
L_{\rm phys}
=\psi_0^{-1}(H-E_0)\psi_0
=-\frac a2\Delta_q+(\Omega q)\cdot\nabla_q
=-\frac a2\,\mu_0^{-1}\operatorname{div}(\mu_0\nabla_q).
\tag{PC10}
\]
Direct differentiation of \(\psi_0\) proves the identity. Consequently
\[
\langle q_j,e^{-tL_{\rm phys}}q_k\rangle_{\mu_0}
=\delta_{jk}\frac a{2\Omega_j}e^{-t\Omega_j}.
\tag{PC11}
\]
The transition mean is \(e^{-t\Omega}q\), and its conditional covariance is
\(\Sigma_0(I-e^{-2t\Omega})\). Replacing \(M^{-1}\) and \(dM\) in (PC7) by
\(\Sigma_0\) and \(\Omega\) gives every physical slice source correlation.

A weighted diffusion therefore **can** represent physical Euclidean evolution: (PC10) does so on the correct vacuum slice, with mobility \(a/2\). The operation in (PC4) acts on all Euclidean histories with their different precision \(M\). Equality of the word “diffusion” does not identify their carriers or sources. [[sewn-transfer-clock-and-the-rotor-limit|The rotor transfer test]] already separates these two kinds of operation for a compact finite family.

## Actual slice readout produces an error-function memory

Let \(J:L^2(\mu_0)\to L^2(\mu_E)\) pull back a slice observable by
\((JF)(q)=F(q(0))\). Its inherited one-step operator is
\[
P_s=J^*e^{-sL_{\rm hist}}J.
\tag{PC12}
\]
The same stationary history is resampled; no fresh slice process has been substituted. Using (PC3)–(PC5), its mode covariance is exactly
\[
\begin{aligned}
C_j^{\rm sl}(s)
&=\int_{\mathbb R}\frac{dp_0}{2\pi}
\frac{a}{p_0^2+\Omega_j^2}
\exp\!\left[-\frac{ds}{a}(p_0^2+\Omega_j^2)\right]\\
&=\boxed{\frac a{2\Omega_j}
\operatorname{erfc}\!\left(\Omega_j\sqrt{\frac{ds}{a}}\right).}
\end{aligned}
\tag{PC13}
\]
For a direct proof, differentiate the integral without its factor \(a\) with respect to \(c=ds/a>0\). Its negative derivative is
\(e^{-c\Omega_j^2}/(2\sqrt{\pi c})\).
The integral vanishes at \(c=\infty\); integration back to \(c\) yields (PC13), including its value at zero.

Write
\[
g_j(s)=\operatorname{erfc}\!\left(\Omega_j\sqrt{ds/a}\right),
\qquad G_s=\operatorname{diag}(g_j(s)).
\]
The full two-slice source law is Gaussian with diagonal blocks \(\Sigma_0\) and off-diagonal block \(\Sigma_0G_s\). Therefore \(P_s\), as a single conditional transition, has mean \(G_sq\) and covariance
\(\Sigma_0(I-G_s^2)\). For any number of actual resampling times, the slice readout is the Gaussian process with pair covariance
\[
\mathbb E[q_j(s,0)q_k(s',0)]
=\delta_{jk}\frac a{2\Omega_j}g_j(|s-s'|).
\tag{PC14}
\]
Equations (PC7) and (PC14) determine all its inherited sources.

Each \(P_s\) is a positive self-adjoint Markov contraction, but the family is not a semigroup: \(g_j(s+t)\ne g_j(s)g_j(t)\). Inserting a slice projection between two updates resets part of the history and changes the experiment. This is a concrete realization of [[conditional-exchange-through-cuts-and-retained-marks|EC6 and EC10's inherited leakage and memory]], rather than a failure of the exact one-step marginal.

At \(s=0\), the continuum temporal readout has a square-root cusp. Its linear slice coordinate lies in \(L^2(\mu_E)\) but not in the Dirichlet-form domain of this continuum history diffusion. The cusp is consistent with that domain fact; it is not an assertion that the finite temporal regulator has a nondifferentiable correlation.

## Two retained frequencies exclude a fitted clock

A common identification \(t=h(s)\) preserving these field source labels would require
\[
h(s)=-\frac1{\Omega_j}\log g_j(s)
\quad\text{for every retained }j.
\tag{PC15}
\]
Even allowing an arbitrary nonlinear scalar calibration cannot satisfy this for two distinct positive frequencies. Put \(z=\sqrt{ds/a}\). The elementary expansion of \(\operatorname{erfc}\) gives
\[
-\frac1{\Omega}\log\operatorname{erfc}(\Omega z)
=
\frac{2z}{\sqrt\pi}
+\frac{2\Omega z^2}{\pi}
+O(z^3).
\tag{PC16}
\]
The coefficient of \(z^2\) differs for \(\Omega_1\ne\Omega_2\). A constant linear rescaling already fails for one mode in this temporal continuum; permitting a nonlinear rescaling still fails for two. Changing a source's overall amplitude cannot repair its normalized autocorrelation.

At large \(s\),
\[
g_j(s)\sim
\frac{\exp[-(d/a)\Omega_j^2s]}
{\sqrt\pi\,\Omega_j\sqrt{ds/a}}.
\tag{PC17}
\]
Thus even its long-time exponential rate is proportional to \(\Omega_j^2\), whereas the physical transfer rate is \(\Omega_j\). In the soft spatial modes of FG8 this is quadratic versus linear momentum dependence. The additional power prefactor also remains. This tests the complete labelled response, not whether some unrelated relabelling of an abstract Hilbert basis could be devised.

The obstruction is not confined to colored linear fields. In the Abelian model, the transverse coordinate \(q_j\) can be replaced by its gauge-invariant field-strength smearing \(B_j=\nu_jq_j\), without changing either normalized profile. The centered quadratic source \(B_j^2-\mathbb E B_j^2\) is also gauge invariant.

For the non-Abelian **quadratic control only**, let \(D=\dim G\) independent color components have the invariant orthonormal color pairing. Put \(c_j=a/(2\Omega_j)\) and
\[
F_j=\sum_{A=1}^{D}(q_{j,A}^2-c_j),
\qquad
\|F_j\|_{\mu_0}^2=2D c_j^2.
\]
This source is invariant under the residual global adjoint action. Equation (PC8) gives
\[
\boxed{
\frac{\langle F_j,P_sF_j\rangle_{\mu_0}}{\|F_j\|_{\mu_0}^2}
=g_j(s)^2,
\qquad
\frac{\langle F_j,e^{-tL_{\rm phys}}F_j\rangle_{\mu_0}}
{\|F_j\|_{\mu_0}^2}
=e^{-2\Omega_jt}.}
\tag{PC18}
\]
For \(j\ne k\), the mixed neutral source
\(F_{jk}=\sum_Aq_{j,A}q_{k,A}\) has variance \(Dc_jc_k\) and respective normalized responses
\(g_j(s)g_k(s)\) and \(e^{-(\Omega_j+\Omega_k)t}\).
These are genuine source distinctions in the quadratic model; they are not claims that a free singlet is already an observable vector above the full interacting Yang–Mills vacuum. Bounded sources \(e^{i\theta F_j}\) recover these polynomial responses by differentiating at zero.

Using a spatial Gibbs weight in place of the actual marginal would introduce a separate error. The density
\(\exp[-bq^TKq/2]\) has covariance \((bK)^{-1}\), whereas (PC9) has covariance \(a\Omega^{-1}/2\). Their momentum powers differ, and one global field rescaling cannot equate them across modes. The stronger obstruction (PC13)–(PC18) arises even after retaining the correct marginal.

## Temporal sewing returns the square root at the boundary

There is a constructive change of explanatory order. Fix the boundary value \(q(0)=q_0\) on the positive temporal half-line, with decay at infinity. Completing the square gives
\[
\frac1{2a}\int_0^\infty
\left(\|q'\|^2+\|\Omega q\|^2\right)d\tau
=
\frac1{2a}\int_0^\infty\|q'+\Omega q\|^2d\tau
+\frac1{2a}q_0^T\Omega q_0.
\tag{PC19}
\]
The unique minimizing extension is \(q(\tau)=e^{-\tau\Omega}q_0\). Gaussian integration over fluctuations with zero boundary value contributes a boundary-independent factor. Hence one half-history returns the amplitude
\[
\Psi_+(q_0)\propto e^{-q_0^T\Omega q_0/(2a)}.
\]
Sewing two such halves with their common boundary returns precisely \(\mu_0\), with precision \(2\Omega/a\). Together with the kinetic mobility \(a/2\) fixed in (PC1)–(PC2), its ground-state transform is (PC10).

For a field this boundary response contains
\(\Omega=\sqrt{ab}\sqrt K\): it is the Dirichlet-to-Neumann response of the actual harmonic extension. The square root has been derived by eliminating a temporal half-space. It was not applied to the resampling generator after observing the desired dispersion. Integration across an actual temporal slab likewise yields the physical transfer and its multi-source exponentials. [[two-slice-innovation-geometry/past-future-angle-and-the-transfer-gap|The past–future theorem]] owns the abstract history/slice distinction; (PC19) displays its exact Gaussian boundary calculation.

If the accelerated DS comparison does return (PC4), its direct identification with physical time must therefore be retired under the retained Abelian source test. This leaves its auxiliary resampling interpretation intact. It also leaves open the separate temporal reconstruction of the **same** determinant amplitude: [[reflection-sewing-and-the-auxiliary-boundary-carrier|reflection sewing and the auxiliary boundary carrier]] tests that possibility with its actual supported carrier and source compression.

The next foundational law must specify which oriented temporal cuts and slab compositions define physical evolution, and which boundary sources survive their quotient. The Gaussian benchmark requires those operations to return (PC9)–(PC11) by integration, while preserving (PC13) as the different inherited resampling experiment. A form comparison with a physical gap would need its own source-compatible carrier map and uniform bounds; invariant measure, reflection positivity, or one fitted rate alone does not supply that comparison.
