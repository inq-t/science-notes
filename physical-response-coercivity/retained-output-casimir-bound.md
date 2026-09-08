# Retained-Output Casimir Bound

A retained-output contraction loss can imply a mass gap only after it is pulled back to the full complex physical carrier, is uniformly coercive there, and is independently bounded by the reconstructed Poincare Casimir. The resulting square-root energy bound differs from the linear Hamiltonian bound available at a finite lattice regulator. A general noisy channel can supply positive output loss; one adapted preserving expectation supplies zero.

## The conditional Casimir stopping theorem on reconstructed members

Here $r$ ranges only over Lorentzian members for which a positive-energy Poincare representation has actually been reconstructed; it does not range over arbitrary finite lattice regulators from [[physical-response-coercivity/quotient-to-qft-realization|the quotient-to-QFT architecture (D19)]]. Let $\mathcal H_r$ be such a reconstructed physical carrier, with vacuum projection $P_{0,r}$ reducing the translation generators and with positive Poincare Casimir operator

$$
\mathcal C_r=H_r^2-c^2\mathbf P_r^2.
$$

Its closed quadratic form is

$$
\mathfrak c_r[\Psi]
:=
\left\|\mathcal C_r^{1/2}\Psi\right\|^2,
\qquad
\Psi\in\mathcal D_r:=\operatorname{Dom}(\mathcal C_r^{1/2}).
$$

Assume $H_rP_{0,r}=\mathbf P_rP_{0,r}=0$ and $P_{0,r}\mathcal D_r\subseteq\mathcal D_r$. The [[channel-loss-and-recovery/minimum-lift-output-forms|minimum-lift construction]] requires explicit Hilbert-space hypotheses here. Declare real BKM tangent Hilbert spaces $V_r,W_r$ and a bounded contraction

$$
A_r:V_r\longrightarrow W_r
$$

with closed reachable range \(W_r^{\mathrm{reach}}:=\operatorname{Ran}A_r\). The quotient/minimum-lift norm is then

$$
g_{A_r}^{\uparrow}(y,y)
:=
\inf_{A_rx=y}\|x\|_{V_r}^2,
\qquad
y\in W_r^{\mathrm{reach}},
$$

and the closed-range theorem gives a unique minimum lift in $(\ker A_r)^\perp$. Require

$$
\tau_{A_r}(y)
:=
g_{A_r}^{\uparrow}(y,y)-\|y\|_{W_r}^2
$$

to be the resulting nonnegative closed quadratic form on the reachable output carrier, and extend it to the complexification by Hermitian polarization. If $A_r$ is unbounded or its range is not closed, these conclusions are not automatic: one must instead construct the quotient completion, prove that the output metric extends there, and prove closability of the difference form before proceeding.

Let a complex-linear map $\mathcal J_r$ send $\mathcal D_r$ into the form domain of that complexified retained-output form, with $\mathcal J_rP_{0,r}=0$. Such a map is a substantive carrier bridge: BKM tangents are density perturbations, not Hilbert excitations by definition. [[channel-loss-and-recovery/preserving-expectation-loss|One preserving expectation with its adapted BKM metrics]] has \(\tau_{A_r}=0\) and cannot supply this lower bound. A general channel can genuinely contract the same declared metrics and give positive output loss, as [[channel-loss-and-recovery/binary-channel-witness|the binary-channel witness]] demonstrates. A non-adapted comparison is another possibility. A multi-channel construction must declare one common source and the order of combination and relaxation; [[trace-dirichlet-descent/shorted-response-filtration-and-the-leak-cocycle#Paired walls produce an exact tangential response|the sum-then-short theorem]] is one such construction, not a sum of separately vanishing output forms. Assume the pullback below is closable and define

$$
\mathfrak t_r[\Psi]
:=
\tau_{A_r}(\mathcal J_r\Psi).
\tag{D20}
$$

Assume, without using the desired spectrum to define any term, that for every $\Psi\in\mathcal D_r$,

$$
\mathfrak t_r[\Psi]
\geq
\kappa_r
\lVert(1-P_{0,r})\Psi\rVert^2
\tag{D21}
$$

and

$$
\mathfrak c_r[\Psi]
\geq
\eta_rE_{*,r}^2
\mathfrak t_r[\Psi].
\tag{D22}
$$

where $\kappa_r,\eta_r,E_{*,r}>0$. Because the estimates hold on the full Casimir form domain, [[mass-scale-calibration/joint-causal-generators-and-the-mass-casimir|the joint-Casimir theorem]] gives the **[CONDITIONAL EXACT IMPLICATION]**

$$
\boxed{
\Delta_{E,r}
\geq
E_{*,r}\sqrt{\eta_r\kappa_r}.}
\tag{D23}
$$

Here $\Delta_{E,r}:=\inf\sigma(H_r|_{(1-P_{0,r})\mathcal H_r})$ refers to the entire physical vacuum complement. The factors have distinct meanings:

| Factor | Type or carrier | Required origin |
|---|---|---|
| $\tau_{A_r}$ | retained output tangents | genuine metric contraction of a general channel, or another declared comparison/family construction; one adapted preserving expectation gives zero |
| pulled-back form $\mathfrak t_r$ | physical vacuum-complement | uniform coercivity, possibly certified by a separately typed closed-range theorem |
| $\kappa_r$ | scalar | dimensionless lower-frame constant for $\mathfrak t_r$ |
| $\eta_r$ | scalar | dimensionless comparison with the reconstructed Poincare Casimir |
| $E_{*,r}$ | unit line | independent RG or cross-sector scale calibration |

For a continuum theorem, $E_{*,r}\sqrt{\eta_r\kappa_r}$ must retain a positive lower limit under declared changing-carrier form convergence with sufficient recovery control, the vacuum projections must converge, and the effective nets must satisfy OS or direct positive-energy reconstruction. [[yang-mills-continuum-crossover/inq|Continuum crossover]] owns these transport and reconstruction obligations. A mixing gap of the channel, a local Hessian, or a finite-regulator singular value is not a substitute.

## The finite-lattice Hamiltonian comparison

At a finite lattice regulator, where continuous Poincare covariance and \(\mathcal C_r\) are unavailable, the legitimate stopping theorem uses the centered lattice Hamiltonian form

$$
\mathfrak h_r[\Psi]
:=
\left\|(H_r-E_{0,r})^{1/2}\Psi\right\|^2,
\qquad
\Psi\in\operatorname{Dom}\!\left((H_r-E_{0,r})^{1/2}\right).
$$

If on its form domain

$$
\mathfrak t_r[\Psi]
\geq
\kappa_r\|(1-P_{0,r})\Psi\|^2,
\qquad
\mathfrak h_r[\Psi]
\geq
\eta_rE_{*,r}\mathfrak t_r[\Psi],
$$

then [[measured-response-carriers/response-to-energy-comparison|the generic response-to-energy implication]] gives the regulated Hamiltonian bound

$$
\Delta_{H,r}
\geq
\eta_rE_{*,r}\kappa_r.
\tag{D23a}
$$

This is a finite-regulator spectral statement, not yet a mass-Casimir theorem. Uniform transport through regulator removal and Poincare reconstruction is still required before (D23) can be invoked.
