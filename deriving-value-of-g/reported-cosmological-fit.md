# The Cosmological Matching-Ratio Profile

The canonical late-time receipt now directly profiles the integrated matching ratio on the unit-rate CST-B2 branch and finds \(\mathfrak R_c\simeq1\). This is reproduced evidence for an effective background amplitude inside the assumed \(\operatorname{sech}^2\) source family, not a direct laboratory or microscopic measurement of BKM horizon capacity. The older profile remains historically informative but is superseded for current numerical use.

## Current direct profile

[[causal-scale-theory/receipts/fit-generalized-background|The branch-aware generalized-background receipt]] uses the fully released 2025 DESI DR2 BAO mean vector and covariance with Pantheon+, fixes the scale-state rate at \(\nu=1\), profiles \(\Omega_{m0}\), the supernova offset, and \(c/(H_0r_d)\), and obtains

$$
\boxed{
\mathfrak R_c=1.014104,
\qquad
\Delta\chi^2\le1:[0.941572,1.089954],
\qquad
\Delta\chi^2\le3.84:[0.875271,1.165563].}
$$

These are one-dimensional profile-likelihood contours. They are not posterior credible intervals or coverage-calibrated confidence intervals. The unit value lies inside the narrower contour. Releasing \(\mathfrak R_c\) improves the frozen-unit maximum by only \(\Delta\chi^2=0.03642\) at the cost of one added shape parameter, so the data do not identify a nonunit value. The receipt keeps the 2026 Ly\(\alpha\) published-Gaussian substitution as a separately labeled provisional update; it is not the source of this canonical profile.

## What was reported historically

In the historical notation \(\gamma=\mathfrak R_c\), with unit scale-state rate fixed, the source law gives

$$
\Omega_{X,c}=\frac{\gamma}{2}.
$$

The archived analysis released \(\gamma\) as a background parameter within that family and reported

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

The fit can therefore test the effective source family and weak unit matching jointly. It cannot independently prove the microscopic arrows in that dictionary.

In particular, the exact binary calculation does not supply the identification: at the balanced binary state the horizontal \(Q\)-tangent has unit BKM norm while the modular variance of the same state is zero. The full horizon capacity must be a distinct extensive object whose coupling to the binary profile is separately proved.

## Reproducibility status

The fixed \(\mathfrak R_c=1\), \(\nu=1\) comparison and the current released-\(\mathfrak R_c\) profile are separately executable and reproducible on the same archived likelihood. [[causal-scale-theory/receipts/fit-late-time-background|The direct unit receipt]] archives the data manifest and covariances; the generalized receipt reuses its likelihood construction and parameterizes root-background pairs by \(x_c\), so it does not silently discard secondary flatness roots. Its canonical machine ledger is [[causal-scale-theory/receipts/generalized-background-fit-2025.json]].

The cited historical `P1/` package remains absent. Consequently the new result replaces the old \(1.025\,[0.941,1.088]\) profile as the canonical current calculation but does not claim to reproduce that older likelihood, data combination, nuisance treatment, or notation exactly.

The proper status is:

$$
\boxed{
\text{reproduced model-restricted background profile near one}
\ne
\text{reproduced direct measurement of modular capacity}.}
$$

Even this successful profile remains phenomenological evidence for the closure, not a proof of [[noether-capacity-theorem|the microscopic capacity theorem]]. In the jointly released \((\nu,\mathfrak R_c)\) calculation the full unit point is inside the nominal two-parameter \(\Delta\chi^2=2.30\) contour, although the profiled \(\nu=1\) coordinate lies just outside its one-dimensional \(\Delta\chi^2=1\) contour. Background distances do not derive either unity principle.
