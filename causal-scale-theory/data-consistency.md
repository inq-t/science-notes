# Is the CST Expansion Consistent with the Data?

Yes at the homogeneous-background level. On two fully released 2025 DESI-plus-supernova combinations, unit CST-B2 has a lower \(\chi^2\) than flat \(\Lambda\)CDM at equal parameter count; a provisional 2026 update gives the same answer. Adding compressed last-scattering distances to the released 2025 vector narrows that advantage without making the curve discrepant. A branch-aware generalized profile finds the unit point compatible and finds no information-criterion reward for releasing either unity parameter. Cepheid calibration preserves the favorable late-time comparison but exposes the unresolved absolute-scale cost: a sound horizon near \(136\ \mathrm{Mpc}\) and conditional low-age pressure under high-redshift extrapolation of the late-time ansatz. This establishes background consistency and a rigid observational signature—not the microscopic wall, a primary-CMB fit, or the perturbation sector.

## What was actually tested

The comparison freezes

$$
\nu=1,
\qquad
\mathfrak R_c=1,
\qquad
\rho_{\mathrm{res}}=0,
$$

uses the smallest positive flatness root, fixes \(\Omega_{r0}=9.15\times10^{-5}\), and fits only \(\Omega_{m0}\) as a background-shape parameter. Flat \(\Lambda\)CDM fits the same \(\Omega_{m0}\). Each model also carries the same two profiled calibrations: the supernova intercept and

$$
A=\frac{c}{H_0r_d}.
$$

The observable map is

$$
E(z)=\frac{H(z)}{H_0},
\qquad
\chi(z)=\int_0^z\frac{\mathrm dz'}{E(z')},
$$

$$
\frac{D_M}{r_d}=A\chi,
\qquad
\frac{D_H}{r_d}=\frac{A}{E},
\qquad
\frac{D_V}{r_d}=A\left(\frac{z\chi^2}{E}\right)^{1/3},
$$

while Pantheon+ constrains the shape of \((1+z_{\mathrm{hel}})\chi(z_{\mathrm{HD}})\) after its common magnitude offset is projected out. Thus the test does not assume a value of \(H_0\), \(r_d\), or the supernova absolute magnitude.

That scale freedom is also a limitation. Profiling \(A=c/(H_0r_d)\) makes this a test of the *shape* of expansion and of the BAO ruler product, not of the absolute Hubble scale. The receipt therefore neither resolves nor aggravates the Hubble tension by itself. An absolute prediction for \(H_0\) requires an independently constructed or measured sound horizon, standard-siren calibration, or another absolute ruler; importing a base-\(\Lambda\)CDM value of \(r_d\) is only a conditional conversion.

The archived inputs are 1,580 Pantheon+ rows after \(z_{\mathrm{HD}}>0.01\) and calibrator removal, with the full selected statistical-plus-systematic covariance, and 13 DESI distances with their covariance. [[causal-scale-theory/sources/late-time-background/README|The source manifest]] records provenance and hashes. [[causal-scale-theory/receipts/fit-late-time-background|The receipt]] owns the likelihood equations and validation checks.

## Result

| Comparison | Flat \(\Lambda\)CDM \(\chi^2_{\min}\) | Unit CST-B2 \(\chi^2_{\min}\) | \(\Delta\chi^2=\chi^2_{\mathrm{CST}}-\chi^2_{\Lambda\mathrm{CDM}}\) | CST best \(\Omega_{m0}\) |
|---|---:|---:|---:|---:|
| 2025 DESI DR2 BAO + Pantheon+ | 1399.8402 | 1396.5263 | \(-3.3139\) | \(0.32239\) |
| Provisional 2026 DESI galaxy BAO + Ly\(\alpha\) published-Gaussian update + Pantheon+ | 1401.6282 | 1398.2846 | \(-3.3437\) | \(0.32551\) |
| 2025 DESI DR2 BAO + Pantheon+ + historical project acoustic anchor | 1400.6308 | 1398.7940 | \(-1.8368\) | \(0.31362\) |
| 2025 DESI DR2 BAO + Pantheon+ + tight base-\(\Lambda\)CDM Planck-chain compression | 1400.8636 | 1399.3710 | \(-1.4925\) | \(0.31135\) |

Every covariance used in these rows passes a Cholesky positive-definiteness check. For the 1,593-element late-time vector, subtracting the three fitted quantities \((\Omega_{m0},\mathcal M,A)\) gives 1,590 nominal degrees of freedom. The provisional 2026 row has

$$
\frac{\chi^2}{\mathrm{dof}}=0.88153
\quad\text{for flat }\Lambda\mathrm{CDM},
\qquad
\frac{\chi^2}{\mathrm{dof}}=0.87942
\quad\text{for unit CST-B2}.
$$

The largest absolute Cholesky-whitened residual is \(4.02\) for \(\Lambda\)CDM and \(3.89\) for CST-B2. The reduced values are unusually low rather than high, so this compressed Gaussian likelihood supplies no conventional goodness-of-fit rejection of either curve. Because the covariance includes correlated systematic allowances and the 2026 Ly\(\alpha\) block is reconstructed, no calibrated tail probability is assigned. In this note, **consistent** means positive-definite likelihood plumbing, no gross whitened-residual failure, and fit quality at least competitive with the accepted reference on the same data—not consistency with every cosmological observable.

The provisional 2026-update CST profile interval is

$$
\Omega_{m0}=0.32551,
\qquad
\Delta\chi^2\le1: [0.31888,0.33232].
$$

Because the compared models have the same parameter count, their \(\Delta\mathrm{AIC}\) and \(\Delta\mathrm{BIC}\) equal the displayed \(\Delta\chi^2\). For the fully released 2025 Pantheon+ row, the maximized-likelihood ratio is about \(\exp(3.3139/2)=5.2\) in favor of the CST curve; the provisional update is nearly unchanged. This is not a Gaussian significance: the models are non-nested, the member was developed with knowledge of the broad late-time pattern, and no evidence integral over prior model space has been computed. The attenuation of that preference under the acoustic stress tests is more informative than the favorable late-time number. “Consistent and competitive” is the durable conclusion; “modestly preferred” applies only to these restricted distance likelihoods.

The receipt also recovers the collaboration benchmarks needed to trust the plumbing:

- Pantheon+ alone in flat \(\Lambda\)CDM: \(\Omega_m=0.33245\), against the published \(0.334\pm0.018\);
- 2025 DESI BAO alone: \(\Omega_m=0.29714\) and \(r_dh=101.55\ \mathrm{Mpc}\), against the published \(0.2975\pm0.0086\) and \(101.54\pm0.73\ \mathrm{Mpc}\);
- the 2026 DESI combination: \(\Omega_m=0.30136\), against the published \(0.3012\pm0.0079\).

These checks are more important than reproducing every decimal of the missing historical `P1/` package. The fully released 2025 row is the canonical reproduced likelihood. The 2026 row replaces its Ly\(\alpha\) block by the bivariate Gaussian published in Results IV and assumes zero cross-covariance with the lower-redshift DESI blocks pending a full release. It independently regenerates the historical reported pair \(1398.29\) versus \(1401.63\) to rounding and reproduces DESI's updated matter constraint, but its proper status is **[PROVISIONAL PUBLISHED-GAUSSIAN UPDATE]** rather than a released 2026 likelihood. The older monograph's separate \(1396.762\) versus \(1400.142\) table is close to, but not exactly regenerated by, the official 2025 release products and remains historical.

## The result survives the corrected DES-Dovekie reduction

[[causal-scale-theory/receipts/fit-des-dovekie-background|The DES-Dovekie robustness receipt]] replaces Pantheon+ by the 1,820-row recalibrated DES supernova release. It first reproduces the collaboration's flat-\(\Lambda\)CDM SN-only result,

$$
\Omega_m=0.330317,
\qquad
\chi^2=1640.2732,
$$

against the published \(0.330\pm0.015\) and \(1640.3\). The apparent alternative value \(1631.4205\) is not a data or covariance discrepancy: it is the profiled quadratic before adding the release likelihood's fixed analytic-marginalization term \(\ln(C/2\pi)=8.8526654\). That term cancels exactly between models.

The direct alternate-supernova comparisons are

| DESI + DES-Dovekie row | Flat \(\Lambda\)CDM \(\chi^2\) | Unit CST-B2 \(\chi^2\) | \(\Delta\chi^2\) |
|---|---:|---:|---:|
| Fully released 2025 BAO | \(1645.3287\) | \(1638.6235\) | \(-6.7052\) |
| Provisional 2026 published-Gaussian update | \(1647.0112\) | \(1640.4016\) | \(-6.6096\) |

Both comparisons have equal parameter count. The fully released row has 1,830 nominal degrees of freedom and reduced \(\chi^2=0.89909\) for \(\Lambda\)CDM versus \(0.89542\) for CST-B2, so neither curve has a high-residual goodness-of-fit failure. This strengthens the claim that the favorable late-time shape is not peculiar to Pantheon+'s calibration. It is a robustness check, not an independent likelihood multiplier: the supernova compilations share some low-redshift material, and both rows reuse the same DESI data. The proper evidential status is **[REPRODUCED BACKGROUND ROBUSTNESS TEST]**, not a second detection.

## Does the likelihood select the unit principles?

[[causal-scale-theory/receipts/fit-generalized-background|The generalized receipt]] uses the reference location itself as a branch coordinate, so it profiles all admitted root-background pairs rather than silently choosing the smallest closure root. On the fully released 2025 Pantheon+ and DESI likelihood it finds:

| CST-B2 profile | \(\chi^2_{\min}\) | best \(\nu\) | best \(\mathfrak R_c\) | \(\Delta\chi^2\) from frozen unit | \(\Delta\mathrm{AIC}\) from frozen unit |
|---|---:|---:|---:|---:|---:|
| frozen unit | 1396.5263 | 1 | 1 | 0 | 0 |
| \(\mathfrak R_c=1\), \(\nu\) free | 1395.3610 | 0.7995 | 1 | \(-1.1653\) | \(+0.8347\) |
| \(\nu=1\), \(\mathfrak R_c\) free | 1396.4899 | 1 | 1.0141 | \(-0.0364\) | \(+1.9636\) |
| both free | 1394.6288 | 0.5781 | 0.6987 | \(-1.8975\) | \(+2.1025\) |

The unit-rate value is just outside the nested \(\mathfrak R_c=1\), \(\Delta\chi^2=1\) interval \([0.5700,0.9863]\), but it is well inside that slice's \(\Delta\chi^2=3.84\) interval. The frozen point lies inside the nominal joint two-parameter \(\Delta\chi^2=2.30\) contour. More importantly, every released-data AIC difference is positive: the small likelihood gains do not repay the added parameters.

The jointly free profile is not a measurement of the best-fit decimals. Its \(\mathfrak R_c\) interval is open toward zero even at \(\Delta\chi^2=1\), because an attainable constant-\(w\) tail lies only \(0.381\) above the joint maximum. The strong statement is therefore not that observation has derived \(\nu=\mathfrak R_c=1\). It is that the independently proposed unit member lies in the supported region and is the more economical member under AIC/BIC. The provisional 2026 Gaussian update makes unity slightly more central but does not change that logical status.

## The last-scattering distance changes the verdict, not the viability

The repository's historical P1 note wrote

$$
\frac{D_M(z_*)}{r_d}=94.32\pm0.28
$$

as a fourteenth BAO-like point. That number is **not directly quoted by Planck**, and the archived note does not document how its \(0.28\) uncertainty was constructed. It is therefore retained only as a historical project sensitivity anchor built from

$$
\theta_*=\frac{r_s(z_*)}{D_M(z_*)},
\qquad
\frac{D_M(z_*)}{r_d}
=\frac{r_s(z_*)/r_d}{\theta_*}.
$$

The distinction matters. The receipt now reads the four official local Planck PR3 baseline chains and directly evaluates

$$
Q_*:=1000\frac{D_{M,*}[\mathrm{Gpc}]}{r_d[\mathrm{Mpc}]}
=94.31404\pm0.03458
$$

over 24,497 weighted chain rows. This reproduces the compressed quantity from primary products, but the tight posterior is conditional on the base-\(\Lambda\)CDM carrier. It is not a model-neutral CMB likelihood and must not be presented as one. [[causal-wall-spectral-theory/sources/data/entry|The Planck source ledger]] owns the archived official chain; [[library/planck-2018-cosmological-parameters/entry|Planck 2018 VI]] owns the primary cosmological-parameter analysis.

Two sensitivity runs make the dependence explicit:

- the undocumented historical \(0.28\) width reduces the CST improvement to \(\Delta\chi^2=-1.8368\);
- imposing the tight base-\(\Lambda\)CDM chain width gives \(\Delta\chi^2=-1.4925\).

Both lines attach the extra distance to the fully released 2025 DESI vector. The second is intentionally a hostile stress test, not valid alternate-model inference. It fixes \(z_*=1089.92\) and \(\Omega_{r0}=9.15\times10^{-5}\), collapses correlations with the physical baryon and radiation densities, and profiles only the common \(H_0r_d\) scale. Its proper meaning is nevertheless useful: even a sharply imposed early-distance summary taken from the incumbent carrier does not make the CST background curve discrepant, although it reduces the late-time likelihood advantage. A legitimate full-CMB verdict still requires recomputing recombination, sound-horizon physics, and anisotropy spectra in a covariant CST completion.

## Cross-check against the latest DESI summary

The direct fit above uses the public Pantheon+ release and no CMB. The August 2026 [[library/desi-dr2-results-iv/entry|DESI DR2 Results IV]] analysis supplies a useful but differently conditioned cross-check. With DESI, CMB, and DES-Dovekie supernovae it reports

$$
(w_0,w_a)=(-0.821\pm0.054,-0.65\pm0.20).
$$

At the canonical released-2025 CST best fit, the model's local tangent is

$$
(w_0,w_a)=(-0.82317,-0.61976).
$$

The per-axis offsets are only \(0.04\sigma\) and \(0.15\sigma\). This is striking adjacency, but not a second likelihood result: the CST pair is a local tangent rather than a finite-range CPL history, the published parameters are correlated, and the DESI analysis imports CMB perturbation physics that CST has not reconstructed. The same paper's DESI-plus-CMB fit without supernovae, \((-0.54,-1.39)\), lies much farther away. The contrast shows that low-redshift supernova information remains decisive rather than offering a compilation-independent confirmation.

The update still favors evolving dark energy over \(\Lambda\)CDM at \(2.7\sigma\) for DESI plus CMB and at \(3.0\)--\(3.5\sigma\) when the updated supernova samples are added. It also demonstrates the neutrino-mass direction that this programme anticipated: the reported 95% upper limit changes from \(0.0592\ \mathrm{eV}\) in \(\Lambda\)CDM to \(0.166\ \mathrm{eV}\) in \(w_0w_a\)CDM for DESI plus CMB. Because a general CPL carrier is not CST, this is evidence for the relevance of the question and the sign of the degeneracy—not a CST neutrino prediction or fit.

## The old benchmark is not the best-fit slice

The benchmark \(\Omega_{m0}=0.310598\) was explicitly an empirical input, not a prediction of the unit principles. On the canonical released-2025 likelihood it gives

$$
\chi^2_{\mathrm{CST}}=1398.9915,
\qquad
\Delta\chi^2=2.4652
$$

above CST's own best fit. It is mildly displaced as a fixed one-coordinate slice, not excluded. It remains \(0.8487\) \(\chi^2\) units better than best-fit flat \(\Lambda\)CDM on this restricted released likelihood, but the phrase “CST is preferred” still applies most cleanly to the family with the ordinary matter fraction fitted equally—not to the stale benchmark decimal.

With the historical acoustic anchor included, the same fixed benchmark has \(\chi^2=1399.2051\): \(0.4111\) above CST's own anchored best fit and \(1.4257\) below best-fit flat \(\Lambda\)CDM. “Recalibration indicated by late-time data” is therefore more precise than “benchmark excluded.”

Updating that empirical input to the released-2025 best fit \(\Omega_{m0}=0.32239\) leaves the qualitative signature intact but moves the linked packet:

| Quantity | Updated late-time-fit value |
|---|---:|
| \(z_c\) | \(0.31225\) |
| \(w_0\) | \(-0.82317\) |
| local \(w_a\) | \(-0.61976\) |
| \(q_0\) | \(-0.33652\) |
| \(j_0\) | \(-0.07346\) |
| acceleration entry | \(z=0.74641\) |
| acceleration exit | \(a/a_0=12.0516\) |
| \(H_0t_0\) | \(0.94360\) |

These linked values are generated, rather than copied, in [[causal-scale-theory/receipts/late-time-best-fit-prediction|the best-fit prediction ledger]].

The near invariance of \(q_0\) and the larger movement of \(j_0\) show where the shape is rigid and where the present placement matters. If one separately supplies the [[library/planck-2018-cosmological-parameters/entry|Planck 2018]] base-model value \(r_d=147.09\ \mathrm{Mpc}\), the fitted \(r_dh=99.324\ \mathrm{Mpc}\) corresponds to \(H_0=67.53\ \mathrm{km\,s^{-1}\,Mpc^{-1}}\); that calibration then gives \(t_0\simeq13.66\ \mathrm{Gyr}\). This is a conditional consistency chain, not an absolute prediction, because the sound horizon was imported from a model-dependent early-universe inference.

## Cepheid calibration exposes the absolute-scale obligation

The archived Pantheon+ table also contains 77 Cepheid-host calibrator rows. [[causal-scale-theory/receipts/fit-calibrated-background|The calibrated-background receipt]] retains them with the collaboration's logical selection and `CEPH_DIST` predictions, then profiles the common supernova magnitude exactly. It reproduces the published flat-\(\Lambda\)CDM Pantheon+SH0ES constraints before comparing the two curves on equal footing.

For calibrated supernovae alone, unit CST-B2 is slightly worse than flat \(\Lambda\)CDM, \(\Delta\chi^2=+1.2673\). Adding the fully released 2025 DESI distances reverses the comparison:

| Released 2025 DESI + calibrated Pantheon+SH0ES | \(\Omega_{m0}\) | \(H_0\) [\(\mathrm{km\,s^{-1}\,Mpc^{-1}}\)] | \(r_d\) [Mpc] | \(t_0\) [Gyr] | \(\chi^2\) |
|---|---:|---:|---:|---:|---:|
| flat \(\Lambda\)CDM | 0.30407 | 73.750 | 136.961 | 12.729 | 1465.3620 |
| unit CST-B2 | 0.32237 | 73.104 | 135.868 | 12.621 | 1462.3935 |

The equal-parameter difference is \(\Delta\chi^2=-2.9685\), so the absolute calibration does not undo the late-time background compatibility. But it closes the escape route hidden by profiling \(H_0r_d\): keeping the local Cepheid scale requires an early ruler near \(136\ \mathrm{Mpc}\). Relative to the Planck 2018 Table 1 marginalized value \(147.09\pm0.26\ \mathrm{Mpc}\) for the default Plik TT,TE,EE+lowE+lensing base-\(\Lambda\)CDM combination, the CST value is lower by \(5.64\sigma\) when the two quoted errors are treated as independent Gaussians. That is the inverse-distance-ladder form of the Hubble tension, not a model-neutral exclusion, because the comparison value imports the Planck carrier.

The same joint CST point gives \(t_0=12.621\pm0.186\ \mathrm{Gyr}\) under the receipt's local-Hessian propagation. This age extrapolates the late-time \(E(z)\) ansatz from the fitted \(z\le2.33\) range to \(y=\ln(1+z)=35\) at fixed \(\Omega_r\). Against the globular-cluster estimate \(13.5\pm0.27\ \mathrm{Gyr}\), using the smaller of Valcin et al.'s two combined-error choices, it is conditionally \(2.68\sigma\) low. The stellar likelihood is not reproduced here, and heterogeneous error budgets are only combined as independent Gaussians, so this is moderate pressure rather than a contradiction. It is nevertheless a real obligation: the late pulse does not by itself solve the Hubble tension; a high-\(H_0\) completion must construct the smaller sound horizon without ruining stellar ages, BBN, or the primary CMB.

This calibrated run is not independent evidence to multiply with the shape-only result. It reuses the same 1,580 Hubble-flow supernova rows and DESI vector; the new information is the retained absolute-distance calibration.

## Independent clocks distinguish the absolute branches

The released-2025 historical-acoustic-anchor fit gives \(\Omega_{m0}=0.31362\), \(r_dh=99.613\ \mathrm{Mpc}\), and

$$
H_0t_0=0.94971.
$$

If the same Planck base-model \(r_d=147.09\ \mathrm{Mpc}\) is supplied, these become

$$
H_0=67.72\ \mathrm{km\,s^{-1}\,Mpc^{-1}},
\qquad
H(0.57)=94.32\ \mathrm{km\,s^{-1}\,Mpc^{-1}},
\qquad
t_0=13.71\ \mathrm{Gyr}.
$$

Two differently constructed clocks are compatible with those numbers:

- the August 2026 DESI-DR1 cosmic-chronometer analysis reports \(H(0.57)=95.1^{+10.9}_{-6.0}\ \text{(stat.)}\pm11.3\ \text{(syst.)}\ \mathrm{km\,s^{-1}\,Mpc^{-1}}\) from a pivotal-redshift cosmographic fit ([Álvarez et al.](https://doi.org/10.48550/arXiv.2608.13178));
- globular-cluster dating gives \(t_U=13.5^{+0.16}_{-0.14}\ \text{(stat.)}\pm0.23\ \text{(sys.)}\ \mathrm{Gyr}\), or \(0.27\ \mathrm{Gyr}\) combined in quadrature ([[library/globular-cluster-age/entry|Valcin et al.]]).

Neither is a new confirmation. The chronometer uncertainty is broad and its promised 45-point covariance product is not yet available with the current preprint; the low-\(H_0\) CST scale above still imports \(r_d\). The useful conclusion is conditional and discriminating: current non-supernova clocks are compatible with the Planck-ruler-calibrated CST branch, while globular-cluster dating puts moderate pressure on the Cepheid-calibrated high-\(H_0\) branch. [[causal-scale-theory/receipts/acoustic-anchored-best-fit-prediction|The anchored prediction ledger]] records the linked dimensionless outputs.

## Signature and construction are different achievements

The background calculation separates what observation can now decide from what the programme must still build:

| Already measurable as a background signature | Still requires first-principles construction |
|---|---|
| whether the unit \(E(z)\) curve fits supernova and BAO distances | the scale-indexed wall algebra, states, and cross-fiber transport |
| whether nearby \((\nu,\mathfrak R_c)\) values improve the fit enough to justify extra freedom | the map from BKM response to a conserved covariant source |
| crossing placement, acceleration entry, present cosmography, and the conditional future class | scalar, vector, and tensor perturbations with stable characteristics |
| the fitted product \(H_0r_d\), or \(H_0\) after an external absolute calibration | an endogenous sound horizon or other absolute ruler |
| disagreement of the rigid curve with a released likelihood | the claim that the fitted amplitude is literally horizon capacity |

The left column can vindicate or kill the *signature* without settling the right column. The right column is not an optional interpretation pasted onto a successful curve: it is what would make the curve an explanation of why a cosmos has that form. Conversely, failure to finish the wall construction does not make a clean background retrodiction disappear; it fixes its present type as phenomenology rather than ontology.

## What the result means

**[REPRODUCED BACKGROUND EVIDENCE]** The finite response-shaped expansion is not in conflict with the distance data tested here. Its coherent one-to-two-percent departure from flat \(\Lambda\)CDM is in the direction the DESI-plus-supernova data favor, and it achieves that late-time fit without releasing a dark-history parameter.

**[CONDITIONAL EARLY-DISTANCE STRESS TEST]** Adding either the undocumented historical acoustic summary or the much tighter base-\(\Lambda\)CDM chain compression leaves CST competitive. This is stronger than a low-redshift-only check but weaker than primary-CMB evidence: both summaries import standard recombination and sound-horizon structure, and the tight one imports the incumbent cosmological carrier itself.

**[REPRODUCED ABSOLUTE-SCALE STRESS TEST]** Retaining Cepheid calibrators makes \(H_0\), \(r_d\), and \(t_0\) separately legible. It preserves the late-time fit but does not dissolve the absolute-scale problem: the high-\(H_0\) branch needs a smaller early ruler and, under the stated extrapolation, is moderately young relative to globular-cluster chronometry.

**[NOT MICROSCOPIC EVIDENCE]** Distances do not observe a BKM metric, modular flow, a binary wall quotient, capacity, or descent. An arbitrary positive component can be represented as an effective fluid, so a successful curve does not prove the proposed ontological reading. [[causal-scale-theory/no-gos/background-reconstruction-is-not-wall-construction|Background reconstruction is not wall construction]].

**[NOT A FULL COSMOLOGICAL FIT]** Primary CMB anisotropies, CMB lensing, structure growth, weak lensing, ISW correlations, and neutrino-mass posteriors require a conserved covariant perturbation completion. Borrowing a smooth-fluid perturbation prescription would test that borrowed carrier. Until [[causal-scale-theory/conjectures/covariant-response-sector|the covariant response sector]] exists, “consistent with all cosmological data” would be false.

**[REPRODUCED UNITY PROFILE]** The branch-aware profile releases \(\nu\) and \(\mathfrak R_c\) without choosing only the smallest closure root. On the fully released 2025 likelihood the unit-rate point is marginally outside one nested one-dimensional \(\Delta\chi^2=1\) slice, while the full unit point lies inside the nominal joint two-parameter 68-percent contour. Releasing the response parameters does not improve \(\chi^2\) enough to repay their information-criterion cost. The data therefore do not *measure* either unity principle, but neither do they ask for extra response freedom. [[causal-scale-theory/receipts/fit-generalized-background|The generalized receipt]] owns the branch theorem, intervals, and boundary audit.

## Current verdict

The careful answer is therefore:

$$
\boxed{
\begin{array}{l}
\text{unit CST-B2 on released late-time distances: consistent and competitive;}\\
\text{extra response parameters: compatible, but not selected by AIC;}\\
\text{with an early-distance compression: consistent; the late-time advantage narrows;}\\
\text{local-}H_0\text{ calibration: viable, but a smaller ruler and conditional age pressure remain;}\\
\text{old fixed-abundance benchmark: viable; recalibration remains data-dependent;}\\
\text{full perturbative cosmology: not yet constructed, hence not yet tested;}\\
\text{microscopic wall interpretation: neither confirmed nor tested by this fit.}
\end{array}}
$$

This is a genuine promotion in the programme's evidence ledger: the background comparison and generalized member profile are no longer merely reported, and the most obvious high-redshift compressed stress test has been run. It is also a clean boundary. The background data reveal a viable, economical signature; they do not license skipping the covariant construction that would make growth and primary-CMB predictions possible.
