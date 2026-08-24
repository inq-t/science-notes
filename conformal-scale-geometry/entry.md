# Conformal Scale Geometry

Causal order fixes conformal geometry without fixing metric calibration; a positive scale section supplies that calibration, and tractor geometry packages its covariant derivatives. On a flat FLRW specialization, the same scale data yield exact identities for acceleration, apparent-horizon motion, horizon-area allocation, and the conversion between canonical horizon heat and Friedmann critical energy. These results require no causal-scale state-space source law.

The ordered argument begins with [[conformal-scale-geometry/causal-order-and-metric-scale|causal order and metric scale]]. Under the standard distinguishing and regularity hypotheses, causal order recovers a conformal class \([g]\), not a unique metric \(g\). A positive weight-one scale section \(\sigma\) selects a representative

$$
g^\sigma_{ab}=\sigma^{-2}g_{ab}.
$$

This distinguishes causal comparability from the calibration of lengths, durations, curvatures, temperatures, and densities.

[[conformal-scale-geometry/scale-tractor-transport|Scale-tractor transport]] packages \(\sigma\), its first derivative, and its trace-adjusted second derivative into a conformally covariant object. In four dimensions, parallel scale-tractor transport is equivalent to the selected metric being Einstein. With Einstein gravity already granted, the trace-free field equation can be written as a transport obstruction, while the trace and cosmological channels remain in a separate scalar norm equation.

On a spatially flat FLRW representative, [[conformal-scale-geometry/flrw-scale-section-kinematics|scale-section kinematics]] gives

$$
\sigma=a^{-1},
\qquad
\sigma'=-H,
\qquad
q=-1+\frac{\sigma\sigma''}{(\sigma')^2}.
$$

These are kinematic identities. Einstein dynamics enters only when an energy condition is related to scale convexity.

The physical apparent-horizon radius \(R_A=c/H\) then obeys

$$
\frac{\mathrm d\ln R_A}{\mathrm dN}=1+q.
$$

For an area-law horizon, [[conformal-scale-geometry/horizon-allocation|the horizon-allocation identity]] decomposes one scale e-fold as

$$
\mathrm dN
=\mathrm d\widehat\zeta_A
+\frac14\,\mathrm d\ln S_A,
\qquad
\mathrm d\widehat\zeta_A
:=\frac{1-q}{2}\,\mathrm dN.
$$

This is an exact differential decomposition of quantities reconstructed from one FLRW history. It is not yet a thermodynamic exchange law or a conserved Noether charge.

[[conformal-scale-geometry/hawking-friedmann-identity|The Hawking--Friedmann identity]] combines the canonical \(2\pi\) apparent-horizon temperature, the Einstein area entropy, and the flat Friedmann critical density:

$$
k_BT_A^{\mathrm{can}}\frac{S_A}{k_B}
=E_{\mathrm{MS},A}
=\rho_{\mathrm{crit}}V_A
$$

in \(3+1\) dimensions. [[conformal-scale-geometry/dimensional-horizon-conversion|The dimensional conversion]] gives the exact \(d\)-spatial-dimensional generalization,

$$
\frac{k_BT_A^{\mathrm{can}}(S_A/k_B)}{V_A}
=\frac{2}{d-1}\rho_{\mathrm{crit}}.
$$

The numerical factor is fixed by horizon and Friedmann geometry after Einstein gravity and its entropy normalization have been assumed.

Nothing in this module identifies metric scale with a horizontal quantum-state tangent, assigns the canonical horizon temperature to such a tangent, equates state capacity with gravitational entropy, supplies a cosmological response density, or selects a crossing branch. Those are additional constructions and principles governed by [[program-core/entry|the programme core]] and its specialist consumers.
