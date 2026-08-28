# The First Frozen Acoustic-Scale Likelihood Test

The CH0-selected minimal chiral-acoustic package passes its first nested-model test. Fixing \(100\theta_*=1.040971372121\) removes one continuous distance coordinate while costing only \(\Delta\chi^2\simeq0.06\)--\(0.34\) in fresh Planck and ACT TT/TE/EE fits; official full Planck chains give the consistent Gaussian surrogate \(0.15\)--\(0.17\). Formal AIC bookkeeping nominally favors the constrained objectives by \(1.66\)--\(1.94\) units. This is a genuine parameter-reduction result, but not independent evidence or a derivation of photon--baryon physics: the acoustic cubic was selected after inspecting the CMB target, and the fits import the standard transfer calculation.

## The package was frozen before this fit

In [[minimal-cosmodynamic-closure/prediction-contract|the prediction contract]], CH0 selects the PDG charged-pion-decay prescription. The tested object is larger: that branch plus the common-count construction and [[causal-grain-cosmology/inq#The equation that snapped into place|the post-search acoustic characteristic]]. This CH0-selected minimal package is

$$
Q_\chi
=
\frac{3\hbar c^5}{2G(F_\pi^\chi)^2},
\qquad
q_\chi\left(q_\chi^2+\frac83\right)
=
\left(3+\ln Q_\chi\right)^3,
\qquad
\theta_*^\chi=\frac1{q_\chi}.
$$

With the already declared laboratory convention

$$
F_\pi^\chi=\frac{130.2\,\mathrm{MeV}}{\sqrt2},
$$

the frozen central prediction is

$$
q_\chi=96.064121145112,
\qquad
\boxed{100\theta_*^\chi=1.040971372121}.
$$

No cosmological parameter was changed to improve that number during the tests below. The charged-pion midpoint branch CH3 was not substituted after unblinding. The declared \(\pm1.2\,\mathrm{MeV}\) laboratory uncertainty propagates to approximately

$$
\sigma_{100\theta_*,\mathrm{lab}}=0.00019977,
$$

but the nested fits use the frozen central value. The uncertainty is treated only as an external sensitivity calculation, never as a CMB-adjustable parameter.

The freeze is auditable rather than retrospective: git commit `6586159` records the cubic and \(100\theta_*=1.0409714\) on August 26, 2026 at 22:56 CDT, before either spectrum-profile script existed.

## The parameter being removed

The CH0-selected package predicts the physical CAMB acoustic angle

$$
\theta_*
=
\frac{r_s(z_{\tau=1})}{D_M(z_{\tau=1})},
$$

not CosmoMC's fast sampling approximation \(\theta_{\mathrm{MC}}\). The paired test is therefore

$$
\begin{aligned}
\mathcal M_6:
&\quad
(\omega_b,\omega_c,\theta_*,\ln A_s,n_s,\tau),\\
\mathcal M_5^{\mathrm{CH0}}:
&\quad
(\omega_b,\omega_c,\ln A_s,n_s,\tau),
\qquad
\theta_*=0.01040971372121.
\end{aligned}
$$

In both arms CAMB solves \(H_0\) anew at every point so that the requested physical angle is obtained. The recombination model, neutrino sector, transfer calculation, data, priors, calibration variables, and nuisance treatment are otherwise unchanged within each paired comparison.

The fresh profiles do not rely on CAMB's looser convenience solution for \(H_0\). They externally root the full returned physical angle, leaving residuals below \(10^{-13}\) in \(100\theta_*\). Their local optimizers terminate on cost or step-size criteria rather than the stricter gradient criterion, so the tables round \(\Delta\chi^2\) to three significant figures; the JSON files preserve the computational values and convergence diagnostics.

This distinction is numerically load-bearing. In the official Planck chains,

$$
100\theta_*-100\theta_{\mathrm{MC}}
=
0.00018392\pm0.00001503.
$$

Putting the package value into the \(\theta_{\mathrm{MC}}\) slot would misstate the tested physical angle by about \(0.60\) of Planck's acoustic-angle standard deviation.

## Results

The convention throughout is

$$
\Delta\chi^2
:=
\chi^2_{\mathrm{fixed}}-\chi^2_{\mathrm{baseline}},
\qquad
\Delta\mathrm{AIC}
=
\Delta\chi^2-2,
$$

because the frozen package removes exactly one continuous fitted coordinate. Here \(\chi^2\) includes the spectrum likelihood plus the stated Gaussian \(\tau\) and calibration constraints. Negative \(\Delta\mathrm{AIC}\) nominally favors the constrained objective, but this bookkeeping does not charge the package's post-search discrete construction.

| Test | Acoustic result | \(\Delta\chi^2\) | \(\Delta\mathrm{AIC}\) | Status |
|---|---:|---:|---:|---|
| Official Planck TT,TE,EE+lowl+lowE chains | \(1.04108750\pm0.00030494\) | \(0.1450\) | \(-1.8550\) | Gaussian profile surrogate |
| Official Planck TT,TE,EE+lowl+lowE+lensing chains | \(1.04109894\pm0.00030678\) | \(0.1729\) | \(-1.8271\) | Gaussian profile surrogate |
| Fresh Planck Plik-lite TT/TE/EE, 613 bins | fitted profile width \(\simeq0.00031\) | \(0.064\) | \(-1.936\) | paired spectrum likelihood |
| Fresh ACT DR6 TT/TE/EE, 135 bins | fitted profile width \(\simeq0.00031\) | \(0.332\) | \(-1.668\) | paired spectrum likelihood |

All four calculations answer the same first question the same way: **the CH0-selected package is well inside the acoustic likelihood ridge.** None shows a material loss of fit when the distance coordinate is removed.

### The official full-Planck chain geometry

The archived Planck chains contain the six sampled cosmological coordinates, all twenty-one Plik nuisance parameters, the likelihood value, and the derived physical \(100\theta_*\). They sampled \(\theta_{\mathrm{MC}}\), not exact \(\theta_*\); the calculation below conditions the derived physical coordinate under a local Gaussian approximation rather than pretending the chains were rerun. Their frequency-weighted results are

$$
100\theta_*
=
1.041087496\pm0.000304937
$$

without lensing and

$$
100\theta_*
=
1.041098935\pm0.000306781
$$

with lensing. The frozen prediction lies respectively \(-0.381\sigma\) and \(-0.416\sigma\) from those means. In a locally multivariate-Gaussian posterior, the marginal variance of one coordinate equals the corresponding profile variance, giving the first two \(\Delta\chi^2\) values in the table.

This is stronger than comparing the frozen prediction with a rounded published error bar because it uses every archived chain weight and the true derived \(\theta_*\). It remains a surrogate rather than a new constrained optimization. The Gaussian conditional shift in the lensing chain moves

$$
H_0:67.36\longrightarrow67.24\;\mathrm{km\,s^{-1}\,Mpc^{-1}},
$$

only \(-0.22\sigma\). The other base coordinates move by at most about \(0.15\sigma\). Thus the constraint does not hide a large compensation elsewhere, and it does not solve the local \(H_0\) tension.

When the laboratory uncertainty in \(F_\pi^\chi\) is convolved with Planck rather than ignored, the residual becomes only \(0.32\)--\(0.35\) combined standard deviations. That strengthens compatibility but weakens any claim of an extraordinarily sharp numerical prediction at current laboratory precision.

### The fresh Planck spectrum profile

The Planck test reconstructs the official Plik-lite v22 TTTEEE likelihood from its archived 613-bin data vector, Fortran-record covariance, bin limits, and bin weights. Plik-lite has already marginalized the high-\(\ell\) foreground sector into this covariance. The Python port reproduces the likelihood checkpoint embedded in Planck's own `.clik` directory to

$$
\Delta\ln\mathcal L=3.86\times10^{-9}.
$$

That receipt checks the spectrum units, TT/TE/EE ordering, binning, covariance endianness, and \(\mathrm{calPlanck}^{-2}\) convention.

The paired fits give

$$
\begin{array}{rcl}
\chi^2_{\mathrm{baseline}}&=&583.26446,\\
\chi^2_{\mathrm{fixed}}&=&583.32858,\\
\Delta\chi^2&=&0.06412.
\end{array}
$$

The baseline profile chooses \(100\theta_*\simeq1.04105\), while the package fixes \(1.04097137\). Cross-start fits keep \(\Delta\chi^2\) stable to about \(2\times10^{-3}\) relative and place the inferred local profile width near \(0.00031\), consistent with the independent official-chain width. The associated derived Hubble value changes only from about \(67.08\) to \(67.00\,\mathrm{km\,s^{-1}\,Mpc^{-1}}\).

This is a fresh whole-spectrum calculation, but not the final native Planck test. It uses marginalized Plik-lite rather than the explicit twenty-one-nuisance Plik likelihood, a Gaussian \(\tau\) proxy rather than SimAll lowE, and omits Commander low-\(\ell\) TT and lensing.

### The fresh ACT spectrum profile

The ACT calculation uses the archived scientific DR6 foreground-marginalized SACC data, all 135 TT/TE/EE bandpowers over the archived \(600\leq\ell\leq8500\) cuts, the full covariance, the ACT temperature and polarization calibrations, and the same calibration prior in both arms. It gives

$$
\begin{array}{rcl}
\chi^2_{\mathrm{baseline}}&=&151.16601,\\
\chi^2_{\mathrm{fixed}}&=&151.49759,\\
\Delta\chi^2&=&0.33158.
\end{array}
$$

The baseline profile chooses \(100\theta_*=1.04079035\); the package prediction is higher by \(0.00018102\), or \(0.58\) of the inferred local profile width. A simultaneous perturbed-start refit changes \(\Delta\chi^2\) by only \(3.1\times10^{-4}\), so the rounded penalty is stable. The remaining parameters absorb the constraint without distortion large enough to spoil TT, TE, or EE. Derived \(H_0\) changes from \(66.083\) to \(66.306\,\mathrm{km\,s^{-1}\,Mpc^{-1}}\).

This is an independent-instrument consistency check, not a prospective blind prediction. The CMB programme had already consulted ACT as an observational benchmark before this profile was run. It also uses a lower-cost stock CAMB transfer and a Gaussian lowE-\(\tau\) proxy rather than the archived production settings: CosmoRec, `lens_potential_accuracy=8`, boosted angular accuracy, disabled late-radiation truncation, and the exact Planck lowE stack. The displayed last digits are therefore transparent computational receipts, not production-accuracy precision.

The archived ACT extension chains provide three secondary checks:

| Archived chain | Frozen-prediction displacement |
|---|---:|
| ACT DR6+Planck lowE with \(n_{\rm run}\) | \(+0.225\sigma\) |
| Planck-cut+ACT+Planck lowT/lowE with \(n_{\rm run}\) | \(+0.043\sigma\) |
| Planck+ACT+lensing+DESI BAO with \(n_{\rm run}\) | \(-0.314\sigma\) |

Those chains are marked unconverged in their archived checkpoints and belong to an \(n_{\rm run}\) extension, so they are corroborating diagnostics rather than primary model comparisons.

## Did the model explain more with less?

In the narrow statistical sense, **yes, conditionally**:

1. The CH0-selected package supplies one fixed physical acoustic angle from \(G\), \(F_\pi^\chi\), and the declared discrete structure.
2. That value replaces one continuous CMB-fitted distance coordinate.
3. The same five remaining base parameters and unchanged nuisance treatment fit the full TT/TE/EE bandpower patterns with \(\Delta\chi^2<0.34\).
4. Formal AIC for the combined spectrum-plus-Gaussian-constraint objective therefore gives a nominal advantage of about \(1.7\)--\(1.9\) units.

This is more than a coincidence with one quoted central number. The frozen angle has been propagated through recombination, sound-horizon formation, projection, gravitational driving, baryon loading, diffusion, lensing of the primary spectra, and the TT/TE/EE covariance. The standard transfer calculation finds no need for a compensating new phase parameter.

But the stronger explanatory claim is still open. The fits import the entire Einstein--Boltzmann photon--baryon geometry. The package fixes its common angular ruler; it does not yet derive baryon loading, sound speed, recombination width, neutrino phase shift, diffusion damping, primordial amplitude, tilt, or polarization production from the causal grain. This is a successful **constraint transfer**, not yet a causal-grain derivation of the spectrum.

The nominal AIC result is also weak, not spectacular. AIC counts continuous fitted coordinates; it does not charge the model for discovering the affine shift \(+3\), reusing \(8/3\), selecting the positive cubic ansatz, or trying multiple chiral rhymes after inspecting the target. Those discrete choices carry a real description-length and look-elsewhere cost, so the number is not a post-selection-corrected model comparison.

## Circularity audit

Three statements must remain separate.

First, the CMB-conditioned \(4.264\,\mathrm{fm}\) reconstruction is not independent. Its crossing rate was obtained by matching a model distance to the Planck acoustic distance while leaving the sound horizon fixed. Feeding that realization back into \(q_*=D_M/r_s\) reuses the datum being explained.

Second, the CH0-selected package is algebraically free of \(H_c\), \(R_c\), \(\lambda_*\), and every CMB-fit parameter after the chiral cancellation. The likelihood code does not secretly infer its central value from Planck or ACT. In that limited sense the numerical constraint tested here is noncircular.

Third, the **functional law** that turns the chiral ratio into \(\theta_*\) was selected only after the CMB acoustic count was known. Algebraic cancellation removes direct data dependence; it does not turn a post-search construction into a prospective prediction. The present result therefore licenses

> the frozen package survives a one-parameter-reduction test and is compatible with the full harmonic spectra,

but not

> CMB data have independently confirmed the CH0-selected acoustic package.

The latter statement requires an immutable freeze followed by a genuinely uninspected measurement or a derived one-to-many prediction that was not used to select the law.

## What the test says about the harmonic ripples

The result gives a precise charitable interpretation of the grain's present role. It can set the **common acoustic address** at which the photon--baryon transfer function is read. Once that address is fixed, the standard relational geometry still supplies the pattern's internal spectroscopy:

$$
\text{common phase ruler}
\quad+\quad
\text{baryon loading, driving, transport, damping, projection}
\quad\longrightarrow\quad
TT,TE,EE.
$$

The profiles test one compressed scalar constraint against the entire bandpower vectors, not a list of independently predicted peak positions. The same TT/TE/EE bandpowers define the \(\theta_*\) likelihood, and the imported transfer physics correlates all of their peaks. The result therefore says that the frozen common ruler is compatible with the shared phase organization and has no damaging hidden correlation with the fitted loading, damping, or polarization parameters. It does not count each surviving peak as a separate causal-grain prediction. What remains unproved is the deep algebraic arrow from the global positive/nonassociative carrier to the local complex photon--baryon oscillator.

## The next decisive return

The immediate completion test is a native paired Planck minimization using full Plik, Commander, SimAll, lensing, all twenty-one high-\(\ell\) nuisance parameters, and the same exact-\(\theta_*\) CAMB solver in both arms. The full-chain geometry predicts that this should cost only \(\Delta\chi^2\simeq0.17\); a materially larger result would expose non-Gaussian or nuisance-profile structure missed here.

That calculation would complete the current-data likelihood audit, but it still would not erase post-selection. The first evidential return must instead be one of:

- a future acoustic-angle determination frozen out of the present search;
- a polarization, lensing, BAO, or higher-point quantity derived from the same grain operator before its data are inspected; or
- a one-to-many derivation of peak loading, phase shifts, and damping with no replacement continuous parameters.

The law now has the right status for that test: not proved, not independently confirmed, but economical, executable, and still alive.

## Reproducible artifacts

[[causal-grain-cosmology/cmb_nested_test.py|The chain test]] reads the archived Planck and ACT chains, hashes every source, checks the physical-\(\theta_*\) distinction, computes the Gaussian profile penalties, propagates the laboratory uncertainty, and records conditional parameter shifts in [[causal-grain-cosmology/cmb_nested_test.json|its machine-readable receipt]].

[[causal-grain-cosmology/planck_lite_profile.py|The Planck spectrum profile]] ports the archived reference likelihood, verifies Planck's embedded check value, runs both CAMB arms, and writes [[causal-grain-cosmology/planck_lite_profile.json|the Planck profile receipt]].

[[causal-grain-cosmology/act_spectrum_profile.py|The ACT spectrum profile]] reads the scientific DR6 SACC file, runs the paired TT/TE/EE fits, and writes [[causal-grain-cosmology/act_spectrum_profile.json|the ACT profile receipt]]. The runtime dependencies are CAMB 1.6.6, SciPy, NumPy, and SACC; the receipts freeze their exact versions and all data hashes.
