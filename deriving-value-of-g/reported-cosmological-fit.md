# The Reported Unit-Ruble Fit

The archive reports a background-cosmology consistency fit \(\mathfrak R_c\simeq1\), but the fitted quantity is an effective amplitude inside the assumed \(\operatorname{sech}^2\) source family, not a direct laboratory or microscopic measurement of a BKM horizon capacity. The result is worth preserving as phenomenological encouragement while its absent likelihood package prevents treating it as independently reproduced evidence.

## What was reported

In the historical notation \(\gamma=\mathfrak R_c\), with unit width fixed, the source law gives

$$
\Omega_{X,c}=\frac{\gamma}{2}.
$$

The archived analysis released \(\gamma\) as a background parameter within that family and reports

$$
\gamma=1.025,
\qquad
68\%\text{ interval }[0.941,1.088].
$$

It also reports \(\gamma=1.030\) with interval \([0.955,1.099]\) when \(\Omega_m\) is externally anchored. The claimed sensitivity enters mainly through the model's relation between \(\gamma\), flatness, and the crossing redshift.

These numbers occur in [[scale-as-modular-observable/misc/scale-as-a-modular-observable#P5 — The capacity ratio γ = 1|the archived P5 discussion]].

## What the fit actually tests

The likelihood does not observe

$$
\operatorname{Var}(K),
\qquad
G^{\perp}_{NN},
\qquad
\text{or}
\qquad
\frac{\mathrm dS_{\mathrm{hor}}}{\mathrm dA}
$$

directly. It observes distances and the background expansion history. Calling the released amplitude a capacity ratio uses the entire constitutive dictionary

$$
\text{background amplitude}
\longleftrightarrow
\text{horizontal BKM response}
\longleftrightarrow
\text{horizon capacity}.
$$

The fit can therefore test the effective source family and the unit-amplitude closure jointly. It cannot independently prove the microscopic arrows in that dictionary.

In particular, the exact binary calculation does not supply the identification: at the balanced binary state the horizontal \(Q\)-tangent has unit BKM norm while the modular variance of the same state is zero. The full horizon capacity must be a distinct extensive object whose coupling to the binary profile is separately proved.

## Reproducibility status

The workspace contains narrative tables and algebraic receipt scripts, but not the cited P1 likelihood package, full data manifest, covariance treatment, priors, nuisance-parameter implementation, branch handling, or machine-readable profile outputs. The canonical audits therefore withhold the quoted confidence interval pending reproduction.

The proper status is:

$$
\boxed{
\text{reported model-restricted fit near one}
\ne
\text{reproduced direct measurement of modular capacity}.}
$$

If the likelihood package is recovered, the fit should be rerun with \(\mathfrak R_c\), width, matter abundance, supernova calibration, and relevant nuisance parameters jointly profiled. Even a successful reproduction would remain phenomenological evidence for the closure, not a proof of [[noether-capacity-theorem|the microscopic capacity theorem]].

