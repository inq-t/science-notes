# The Homogeneous CST Response

After the wall reduction, affine soldering, fixed extensivity, integrated crossing normalization, constitutive source, horizontal-temperature identification, and Einstein-horizon conversion are all granted, CST returns one two-parameter homogeneous density. This note owns that interface formula and delegates its mathematical consequences to theorem notes.

Set

$$
x:=N-N_c,
\qquad
\nu>0,
\qquad
\mathfrak R_c>0.
$$

The conditional response is

$$
\boxed{
\rho_X(N)
=\frac{\mathfrak R_c}{2}
\rho_{\mathrm{crit},c}
\operatorname{sech}^2(\nu x).}
$$

Its provenance is explicit in [[realization-map|the realization map]]. In particular:

- \(\nu\) is the magnitude of the affine scale--state slope in the canonically normalized binary coordinate;
- \(\mathfrak R_c\) is the cut-integrated crossing ratio from [[scale-capacity|homogeneous capacity]];
- the factor \(1/2\) comes from [[free-energy-source|the constitutive source]];
- the conversion to \(\rho_{\mathrm{crit},c}\) uses [[horizontal-temperature|an open temperature identification]] followed by [[conformal-scale-geometry/hawking-friedmann-identity|an exact horizon identity]].

No part of this formula constructs the wall, proves either weak unit principle, or supplies a covariant stress tensor.

If the response is separately conserved, [[theorems/rigid-sech-response-identities|the rigid-response theorem]] gives its equation of state, Riccati flow, and differential invariants. [[theorems/trace-free-silence|The trace-free theorem]] gives the crossing identity. [[theorems/dimensional-crossing-partition|The dimensional theorem]] gives the crossing fraction after the relevant background assumptions are added.

The positive pulse has its unique maximum at \(N_c\). Present flatness need not select a unique value of \(N_c\) for general width; that is a separate root problem handled by [[flatness-branches|the branch analysis]].

The formula fixes no sound speed, anisotropic stress, exchange current, initial perturbation, or stability criterion. Until [[conjectures/covariant-response-sector|a covariant response sector]] is constructed, it is a background density law and nothing stronger.
