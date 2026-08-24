# Tilt and Running Identities

Once a positive scalar power is written as the reciprocal of a response coefficient, its tilt and running are exact logarithmic derivatives of that coefficient. A constant-exponent member has zero running by assumption; critical scaling alone supplies no universal bound of order the tilt squared.

## Response coefficient

In three flat dimensions write

$$
\mathcal K_\zeta(k)=C(k)|k|^3.
$$

Using [[basic-concepts/hessians/fourier-covariance-and-precision|the Fourier precision identity]],

$$
\Delta_\zeta^2(k)
=\frac{1}{2\pi^2C(k)}.
$$

Define the dimensionless spectral-response coefficient

$$
\mathcal I_\zeta(k)
:=\Delta_\zeta^2(k)^{-1}
=2\pi^2C(k).
$$

Any alternative response coefficient \(c^{(0)}(k)\) proportional to \(\mathcal I_\zeta(k)\) by a fixed positive normalization has the same logarithmic derivatives. The symbol \(\mathcal I_\zeta\) is not automatically BKM distinguishability, entropy, capacity, or a conserved information stock.

## Exact derivative identities

With

$$
n_s(k)-1
:=\frac{\mathrm d\ln\Delta_\zeta^2(k)}
{\mathrm d\ln k},
$$

one obtains

$$
\boxed{
n_s(k)-1
=-\frac{\mathrm d\ln\mathcal I_\zeta}
{\mathrm d\ln k}
=-\frac{\mathrm d\ln C}
{\mathrm d\ln k}.}
$$

The running is

$$
\boxed{
\alpha_s(k)
:=\frac{\mathrm dn_s}{\mathrm d\ln k}
=-\frac{\mathrm d^2\ln\mathcal I_\zeta}
{\mathrm d(\ln k)^2}
=-\frac{\mathrm d^2\ln C}
{\mathrm d(\ln k)^2}.}
$$

These are **[EXACT]** after the definitions and differentiability hypotheses are granted.

## Constant-exponent member

Suppose one selects

$$
C(k)=C_*
\left(\frac{k}{k_*}\right)^\delta
$$

with constant \(\delta\). Then

$$
n_s-1=-\delta,
\qquad
\boxed{\alpha_s=0.}
$$

This is **[CONDITIONAL OUTPUT]** of the constant-exponent assumption. It is not a universal prediction of a general positive response theory.

If \(\delta\) varies,

$$
\alpha_s
=-\frac{\mathrm d\delta}{\mathrm d\ln k}.
$$

No relation such as \(|\alpha_s|\lesssim\delta^2\) follows without a beta function, flow equation, analyticity estimate, or other microscopic restriction.

## Scope

These formulas are kinematic derivative identities. They do not calculate \(C(k)\), select a pivot, identify a wall state, or justify estimating running from differences between best-fit tilts obtained from distinct data combinations.

On a generic curved cut there is no global \(k\). A covariant notion of running must be defined through spectral scale, a pseudodifferential symbol, or another declared geometric flow; flat momentum formulas cannot simply be copied onto [[curved-p3-representative|a curved \(P_3\) operator]].
