# The Balanced-Binary CST-B2 Response

After an exhaustive or explicitly conditioned balanced binary channel, affine soldering, fixed extensivity, integrated reference normalization, constitutive source, horizontal-temperature identification, and Einstein-horizon conversion are all granted, CST-B2 returns one two-parameter homogeneous density. [[response-family-interface|The response-family interface]] owns the member-independent return type; this note owns only the present balanced-binary specialization and delegates its consequences to theorem notes.

Set

$$
x:=N-N_c,
\qquad
\nu>0,
\qquad
\mathfrak R_c>0.
$$

The CST-B2 conditional response is

$$
\boxed{
\rho_X(N)
=\frac{\mathfrak R_c}{2}
\rho_{\mathrm{crit},c}
\operatorname{sech}^2(\nu x).}
$$

Its provenance is explicit in [[realization-map|the realization map]]. In particular:

- \(\nu\) is the magnitude of the affine scale--state slope in the canonically normalized binary coordinate;
- \(\mathfrak R_c\) is the integrated reference matching ratio from [[scale-capacity|homogeneous capacity]], historically called the crossing ratio when the reference event is physically realized;
- the factor \(1/2\) comes from [[free-energy-source|the constitutive source]];
- the conversion to \(\rho_{\mathrm{crit},c}\) uses [[horizontal-temperature|an open temperature identification]] followed by [[conformal-scale-geometry/hawking-friedmann-identity|an exact horizon identity]].

Thus \(\nu\) is the scale-state rate and the profile's inverse-scale parameter, not a width. For this binary profile the full width at half maximum is

$$
\boxed{
\Delta N_{\mathrm{FWHM}}
=\frac{2\operatorname{arcosh}\sqrt2}{\nu}.}
$$

In particular, the proposed value \(\nu=1\) gives \(\Delta N_{\mathrm{FWHM}}=2\operatorname{arcosh}\sqrt2\), not one e-fold. No part of this formula constructs the wall, proves either weak unit principle, or supplies a covariant stress tensor. A different normalized response member changes the function multiplying the reference amplitude without changing the family-level return type.

If the CST-B2 response is separately conserved, [[theorems/rigid-sech-response-identities|the rigid-sech theorem]] gives its equation of state, Riccati flow, and differential invariants. [[theorems/trace-free-silence|The stationary-density theorem]] gives the more general crossing identity. [[theorems/dimensional-crossing-partition|The dimensional theorem]] gives the member-independent crossing fraction after the relevant background assumptions are added.

For this fixed-extensivity binary profile, the positive pulse has its unique maximum at \(N_c\). The family interface treats \(N_c\) only as a normalization point until a member proves more. Present flatness need not select a unique value of \(N_c\) for general CST-B2 rate; that is a separate root problem handled by [[flatness-branches|the branch analysis]].

The formula fixes no sound speed, anisotropic stress, exchange current, initial perturbation, or stability criterion. Until [[conjectures/covariant-response-sector|a covariant response sector]] is constructed, it is a background density law and nothing stronger.
