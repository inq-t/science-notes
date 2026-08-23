# Jacobson’s Entanglement Equilibrium

Jacobson’s small-ball argument relates the first-order semiclassical Einstein equation to stationary total entropy in a small geodesic ball at fixed volume. The total combines an ultraviolet area term with infrared matter entanglement and takes the Bekenstein generalized-entropy form after its area coefficient is identified with \(1/(4\hbar G)\). The conformal-field version is a precise leading-order equivalence once a finite universal area density is assumed; the generic nonconformal extension requires additional conjectures and the argument does not establish a finite-variation entropy maximum.

The authoritative source is the published-version text [[vendor/entropic-gravity/sources/papers/1505.04753-jacobson-entanglement-equilibrium-einstein-equation.pdf|Jacobson 2016]]. The materially stronger original proposal is preserved separately as [[vendor/entropic-gravity/sources/papers/1505.04753v1-jacobson-entanglement-equilibrium-historical.pdf|the historical 2015 version]].

## Small-ball geometry

Let \(\Sigma\) be a small \((d-1)\)-dimensional geodesic ball of radius \(\ell\), centered at \(o\) and orthogonal there to an arbitrary unit timelike vector \(u^a\). Define

$$
C_d(\ell)
:=\frac{\Omega_{d-2}\ell^d}{d^2-1}.
$$

At fixed ball volume, the leading area variation is

$$
\delta A|_V
=-C_d(\ell)\,G_{ab}u^au^b.
$$

Relative to a maximally symmetric reference with

$$
G^{\mathrm{MSS}}_{ab}=-\lambda g_{ab},
$$

this becomes

$$
\delta A|_{V,\lambda}
=-C_d(\ell)
\bigl(G_{ab}+\lambda g_{ab}\bigr)u^au^b.
$$

This is a local geometric identity at leading order in the ball radius.

## Total-entropy split

Assume that the ultraviolet contribution to the vacuum entanglement has a finite, universal area density \(\eta\):

$$
\delta S_{\mathrm{UV}}=\eta\,\delta A.
$$

Write the first variation of the total entropy as

$$
\delta S_{\mathrm{tot}}
=\eta\,\delta A+\delta S_{\mathrm{IR}}.
$$

Only after the derived identification \(\eta=1/(4\hbar G)\) does this coincide with the usual Bekenstein generalized entropy \(A/(4\hbar G)+S_{\mathrm{IR}}\).

For a reference density matrix \(\rho_0\), the entanglement first law is

$$
\delta S_{\mathrm{IR}}
=\delta\langle\mathcal K\rangle,
\qquad
\mathcal K:=-\ln\rho_0.
$$

This identity is general for infinitesimal state variations. The crucial special property of a conformal field theory vacuum on a ball is that its modular generator is local:

$$
\mathcal K_B
=\frac{2\pi}{\hbar}
\int_\Sigma
\frac{\ell^2-r^2}{2\ell}
T_{00}\,dV.
$$

If the excitation and curvature scales are large compared with \(\ell\), the stress tensor is approximately constant across the ball and

$$
\delta S_{\mathrm{IR}}
=\frac{2\pi}{\hbar}
C_d(\ell)\,
\delta\langle T_{ab}\rangle u^au^b.
$$

## Stationarity and the field equation

The maximal-vacuum-entanglement hypothesis says that the locally maximally symmetric vacuum is an entropy maximum under simultaneous field and geometric variations at fixed ball volume. What the calculation directly uses is its first-order consequence:

$$
\delta S_{\mathrm{tot}}|_{V,\lambda}=0.
$$

Combining the area and matter variations gives

$$
\left[
G_{ab}+\lambda g_{ab}
-\frac{2\pi}{\hbar\eta}
\delta\langle T_{ab}\rangle
\right]u^au^b=0.
$$

Requiring this at every point and for every timelike \(u^a\), and then using the Bianchi identity and stress-energy conservation, yields

$$
G_{ab}+\Lambda g_{ab}
=\frac{2\pi}{\hbar\eta}
\delta\langle T_{ab}\rangle,
$$

with

$$
G=\frac{1}{4\hbar\eta}
$$

in \(c=k_B=1\) units. Vacuum or reference-state stress can be absorbed into \(\Lambda\), whose value remains undetermined.

For conformal matter and under the area-density assumption, the controlled statement is therefore

$$
\boxed{
\text{first-order fixed-volume total-entropy stationarity}
\iff
\text{semiclassical Einstein equation}
}
$$

at leading small-ball order.

## Scale hierarchy

The construction requires a window

$$
L_{\mathrm{UV}}
\ll\ell
\ll
L_{\mathrm{curv}},
L_{\mathrm{excitation}},
L_{\mathrm{QFT}}.
$$

The ball must be large enough for the universal area term to make sense and small enough that curvature, stress, and coupling variations are negligible across it.

## Nonconformal fields

For a generic QFT, the modular Hamiltonian of a ball is nonlocal. The published paper conjectures a small-ball form

$$
\delta\langle\mathcal K\rangle
=\frac{2\pi}{\hbar}C_d(\ell)
\left(
\delta\langle T_{00}\rangle+\delta X
\right),
$$

where \(\delta X\) is a scalar contribution which may depend on \(\ell\). The reference curvature is allowed to vary with the ball in a way that absorbs this term while leaving a spacetime-constant cosmological constant.

[[vendor/entropic-gravity/sources/papers/1601.00528-casini-galante-myers-comments-entanglement-equilibrium.pdf|Casini, Galante, and Myers]] and [[vendor/entropic-gravity/sources/papers/1602.01380-speranza-entanglement-excited-states.pdf|Speranza]] show why this extension is delicate. Relevant operators can produce terms of order \(\ell^{2\Delta}\); for \(\Delta\leq d/2\), these need not be subordinate to the desired \(\ell^d\) stress-tensor term. This does not invalidate the strict conformal first-order result, but it blocks a simple universal extrapolation to arbitrary QFT states.

## Version history and extensions

The first arXiv version conjectured a stronger nonconformal modular-energy relation. Later versions weakened it, restricted the claim explicitly to first-order vacuum variations, and allowed the reference curvature to depend on ball size. The published version is therefore the proper source for the theorem-shaped claim.

[[vendor/entropic-gravity/sources/papers/1612.04374-bueno-min-speranza-visser-higher-order-gravity.pdf|Bueno, Min, Speranza, and Visser]] replace area by an appropriate higher-curvature entropy and ordinary volume by a generalized volume. They recover the **linearized** higher-curvature equations under their hypotheses, not the full nonlinear equations of a generic higher-derivative theory.

[[vendor/entropic-gravity/sources/papers/1812.01596-jacobson-visser-causal-diamond-thermodynamics.pdf|Jacobson and Visser’s causal-diamond thermodynamics]] develops the geometric first law for maximally symmetric causal diamonds and clarifies the thermodynamic role of the conformal Killing flow. It strengthens the framework around the small-ball construction without deriving its ultraviolet entropy density.

[[vendor/entropic-gravity/sources/papers/1810.12236-svesko-equilibrium-to-einstein.pdf|Svesko’s causal-diamond analysis]] relates this first-law structure to a Clausius law for the reversible part of causal-diamond entropy. In that construction, fixing volume subtracts the irreversible background contribution, while a reversible entropy balance yields nonlinear equations for a broad class of diffeomorphism-invariant theories. This is a later extension with its own thermodynamic hypotheses, not a proof of Jacobson’s microscopic area-density premise.

## Exact boundary

- “Maximum” is a motivating hypothesis; first-order stationarity is what is proved equivalent to the field equation.
- The Einstein tensor may be nonlinear in the local metric, but the comparison is infinitesimal around a reference vacuum and leading order in \(\ell\).
- The finite area coefficient, matter conservation, and the applicable QFT modular energy are inputs.
- The argument does not derive matter content, quantum spacetime, an independent microscopic or numerical value of \(G\), or the value of \(\Lambda\).
