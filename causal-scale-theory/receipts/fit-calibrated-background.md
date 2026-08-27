# Cepheid-Calibrated Background Receipt

This receipt asks a narrower question than the uncalibrated expansion-shape fit: after retaining the Pantheon+ Cepheid-host rows and applying their measured host distance moduli exactly as the collaboration likelihood does, what absolute \(H_0\), sound-horizon scale, and cosmic age are implied by flat \(\Lambda\)CDM and by the frozen unit CST-B2 background? The answer is two-sided. CST-B2 remains competitive with flat \(\Lambda\)CDM on the fully released 2025 DESI-plus-calibrated-supernova likelihood, but the locally calibrated branch requires \(r_d\simeq136\ \mathrm{Mpc}\) and gives \(t_0\simeq12.62\ \mathrm{Gyr}\). Those are conditional tensions to be explained, not a model-neutral early-universe inference or a full-physics validation.

## The likelihood being reproduced

The public Pantheon+SH0ES table contains 1,701 light-curve rows. The [official likelihood implementation](https://github.com/PantheonPlusSH0ES/DataRelease/blob/c447f0fea703fcd0fff57de5000947b5ca81286b/Pantheon%2B_Data/5_COSMOLOGY/cosmosis_likelihoods/Pantheon%2BSH0ES_cosmosis_likelihood.py) selects

$$
(z_{\mathrm{HD}}>0.01)\ \lor\ {\tt IS\_CALIBRATOR}.
$$

That logical **or** matters. It retains 1,657 rows: 1,580 Hubble-flow rows and 77 Cepheid-calibrator rows. The 44 rejected rows are low-redshift noncalibrators. For a calibrator the theory value is the released `CEPH_DIST` distance modulus. For a Hubble-flow row it is

$$
D_{L,i}^{\mathrm{th}}
=\frac{c}{H_0}(1+z_{{\rm hel},i})
\chi(z_{{\rm HD},i}),
\qquad
\mu_i=5\log_{10}\!\left(\frac{D_{L,i}^{\mathrm{th}}}{1\ \mathrm{Mpc}}\right)+25,
\qquad
\chi(z)=\int_0^z\frac{dz'}{E(z')}.
$$

This is the flat-background reduction of the collaboration expression

$$
5\log_{10}\!\left[
(1+z_{\mathrm{HD}})(1+z_{\mathrm{hel}})
\frac{D_A(z_{\mathrm{HD}})}{1\ \mathrm{Mpc}}
\right]+25.
$$

One common absolute magnitude \(M\) is added to **every** selected row. The calibrators therefore constrain \(M\), while the Hubble-flow intercept constrains the combination containing \(H_0\); treating the calibrators merely as extra low-redshift cosmology points would be a type error.

At fixed \(\Omega_m\), define \(I_i=0\) on calibrators and \(I_i=1\) on Hubble-flow rows. Let \(b_i\) denote `CEPH_DIST` on the first set and \(5\log_{10}[\widehat c(1+z_{\mathrm{hel}})\chi]+25\) on the second, where \(\widehat c:=c/(1\ \mathrm{km\,s^{-1}})\) is the numerical speed in the declared units. Define likewise

$$
\widehat H_0:=\frac{H_0}{1\ \mathrm{km\,s^{-1}\,Mpc^{-1}}}.
$$

Then

$$
m_i-b_i=M+I_i\beta,
\qquad
\beta=-5\log_{10}\widehat H_0.
$$

With \(X=(\mathbf 1,I)\), the receipt profiles the correct common magnitude nuisance and the Hubble intercept by the exact generalized-least-squares projection

$$
\widehat{\boldsymbol a}
=(X^{\mathsf T}C_{\mathrm{SN}}^{-1}X)^{-1}
X^{\mathsf T}C_{\mathrm{SN}}^{-1}
(\boldsymbol m-\boldsymbol b),
\qquad
\boldsymbol a=(M,\beta).
$$

The joint row adds the 13-element fully released 2025 DESI DR2 BAO vector and covariance. Its common amplitude is

$$
A=\frac{c}{H_0r_d},
$$

profiled at fixed \(\Omega_m\) as in [[causal-scale-theory/receipts/fit-late-time-background|the uncalibrated background receipt]]. Once the Cepheid rows determine \(H_0\), the BAO amplitude determines \(r_d\). With

$$
h:=\frac{H_0}{100\ \mathrm{km\,s^{-1}\,Mpc^{-1}}},
$$

the quantity \(r_dh\) remains the directly fitted late-time ruler product.

The supernova-only fits therefore have three parameters \((\Omega_m,H_0,M)\); the joint fits have four \((\Omega_m,H_0,M,r_d)\). Both cosmologies have the same parameter count on each data vector. The reported \(\chi^2\) is the parameter-dependent quadratic. The covariance determinant and \(2\pi\) normalization are constant across the two models and cancel exactly in every displayed difference.

## Official flat-\(\Lambda\)CDM validation

[[library/pantheon-plus-analysis-cosmological-constraints/entry|Brout et al.]] report the marginalized Pantheon+SH0ES flat-\(\Lambda\)CDM constraints

$$
\Omega_m=0.334\pm0.018,
\qquad
H_0=73.6\pm1.1\ 
\mathrm{km\,s^{-1}\,Mpc^{-1}}.
$$

Using `m_b_corr` and the masked full statistical-plus-systematic covariance, the receipt finds the radiationless low-redshift maximum-likelihood point

$$
\Omega_m=0.331812,
\qquad
H_0=73.5328\ \mathrm{km\,s^{-1}\,Mpc^{-1}},
\qquad
M=-19.24406,
$$

with raw quadratic \(\chi^2=1452.0160\). The paper does not tabulate an absolute \(\chi^2\) for this row. The parameter differences are \(-0.12\) and \(-0.061\) of the paper's quoted \(1\sigma\) widths. Decimal identity is not expected because the paper quotes marginalized posterior summaries whereas this receipt reports a maximum-likelihood point.

This parity calculation sets \(\Omega_r=0\). The equal-footing comparison below fixes the project's common late-time value \(\Omega_r=9.15\times10^{-5}\), which shifts only the last displayed decimals. This is the relevant official-carrier validation.

## Equal-footing results

Local \(1\sigma\) errors below come from the inverse observed Hessian of \(-\ln L=\chi^2/2\), including the common magnitude nuisance. They are local Gaussian errors, not posterior credible intervals or coverage-calibrated confidence intervals.

The one-dimensional optimizer is restricted to \(0.15\leq\Omega_m\leq0.50\). Every reported minimum is strictly interior and lies below every point in a separate 151-point scan over \(0.05\leq\Omega_m\leq0.80\). That is a boundary and nonconvexity audit, not a proof over an unrestricted parameter domain.

| Calibrated Pantheon+SH0ES only | \(\Omega_m\) | \(H_0\ [\mathrm{km\,s^{-1}\,Mpc^{-1}}]\) | \(M\) | \(\chi^2\) |
|---|---:|---:|---:|---:|
| flat \(\Lambda\)CDM | \(0.33166\pm0.01804\) | \(73.533\pm1.017\) | \(-19.2441\pm0.0295\) | \(1452.0173\) |
| unit CST-B2 | \(0.31160\pm0.03231\) | \(73.125\pm1.003\) | \(-19.2418\pm0.0295\) | \(1453.2846\) |

Thus

$$
\Delta\chi^2_{\mathrm{CST}-\Lambda\mathrm{CDM}}=+1.2673
$$

for the calibrated supernova likelihood alone. Flat \(\Lambda\)CDM fits this vector slightly better, with no parameter-count difference.

| Released 2025 DESI DR2 BAO + calibrated Pantheon+SH0ES | \(\Omega_m\) | \(H_0\) | \(r_dh\ [\mathrm{Mpc}]\) | \(r_d\ [\mathrm{Mpc}]\) | \(\chi^2\) |
|---|---:|---:|---:|---:|---:|
| flat \(\Lambda\)CDM | \(0.30407\pm0.00793\) | \(73.750\pm1.012\) | \(101.008\pm0.672\) | \(136.961\pm2.042\) | \(1465.3620\) |
| unit CST-B2 | \(0.32237\pm0.00765\) | \(73.104\pm1.002\) | \(99.325\pm0.493\) | \(135.868\pm1.971\) | \(1462.3935\) |

Here

$$
\Delta\chi^2_{\mathrm{CST}-\Lambda\mathrm{CDM}}=-2.9685.
$$

At equal parameter count the CST-B2 curve fits this restricted joint background likelihood modestly better. The sign reversal between supernovae alone and supernovae plus BAO is useful: the result is being driven by the joint distance shape, not by a uniformly better fit to every ingredient.

## Covariance and residual audit

Both selected covariances pass Cholesky positive-definiteness checks. The receipt slices the released covariance and only then inverts it; slicing a precision matrix would define a different likelihood. It uses `m_b_corr`, not `MU_SH0ES` or the diagonal-only error columns. The profiled supernova and BAO nuisance normal-equation scores vanish below \(2\times10^{-9}\).

The nominal degrees of freedom are \(1657-3=1654\) for calibrated supernovae and \(1657+13-4=1666\) for the joint vector.

| Model and data | nominal \(\chi^2/\mathrm{dof}\) | largest \(\lvert L^{-1}r\rvert\) | number with \(\lvert L^{-1}r\rvert>3\) |
|---|---:|---:|---:|
| \(\Lambda\)CDM, calibrated SN | \(0.87788\) | \(4.002\) | 9 |
| CST-B2, calibrated SN | \(0.87865\) | \(3.948\) | 9 |
| \(\Lambda\)CDM, DESI + calibrated SN | \(0.87957\) | \(4.059\) | 9 |
| CST-B2, DESI + calibrated SN | \(0.87779\) | \(3.952\) | 9 |

The machine ledger also records the whitened mean, standard deviation, absolute quantiles, and counts above two, three, and four. Cholesky-whitened coordinates depend on row ordering; only their squared norm is invariant. The reduced values are low rather than high, so there is no conventional high-residual rejection of either curve. Because the covariance carries correlated systematic allowances, these nominal diagnostics are not assigned calibrated tail probabilities.

## The absolute-scale obligations

The local calibration exposes information that the shape-only receipt deliberately profiles away.

[[library/planck-2018-cosmological-parameters/entry|Planck 2018]], Table 1, gives the marginalized summary \(r_d=147.09\pm0.26\ \mathrm{Mpc}\) for its default Plik TT,TE,EE+lowE+lensing base-\(\Lambda\)CDM analysis. This receipt does not recompute that statistic from the local chains. Relative to that explicitly model-conditioned reference, the released joint fit gives

| Model | fitted \(r_d\) | difference from \(147.09\ \mathrm{Mpc}\) | conditional combined discrepancy |
|---|---:|---:|---:|
| flat \(\Lambda\)CDM | \(136.961\pm2.042\ \mathrm{Mpc}\) | \(-10.129\ \mathrm{Mpc}\) | \(4.92\sigma\) |
| unit CST-B2 | \(135.868\pm1.971\ \mathrm{Mpc}\) | \(-11.222\ \mathrm{Mpc}\) | \(5.64\sigma\) |

The combined values assume independent Gaussian errors. They restate the inverse-distance-ladder form of the Hubble tension; they are not a model-neutral exclusion of either late-time curve. In particular, this receipt does not calculate recombination or construct an endogenous sound horizon. A CST account that keeps the local Cepheid calibration must supply early-ruler physics capable of producing roughly \(136\ \mathrm{Mpc}\), rather than silently importing the base-\(\Lambda\)CDM value.

[[library/globular-cluster-age/entry|Valcin et al.]] infer \(t_U=13.5\pm0.27\ \mathrm{Gyr}\) from globular-cluster chronometry using the smaller of their two quoted total-error choices. This inference is comparatively insensitive to late-time cosmological parameters, but it still depends on stellar evolution, distances, abundances, and a cluster-formation delay; it is not assumption-free.

To calculate a cosmic age, the receipt extends each fitted homogeneous \(E(z)\) from the observed \(z\leq2.33\) domain to \(y=\ln(1+z)=35\), keeping \(\Omega_r=9.15\times10^{-5}\) fixed. For CST-B2 this is an explicit high-redshift extrapolation of the late-time ansatz, not an early-universe construction. Combining the resulting local-Hessian age error in quadrature with the quoted stellar-age error gives

| Model and data | fitted \(t_0\) | conditional difference from Valcin et al. |
|---|---:|---:|
| \(\Lambda\)CDM, calibrated SN | \(12.458\pm0.240\ \mathrm{Gyr}\) | \(2.89\sigma\) low |
| CST-B2, calibrated SN | \(12.718\pm0.342\ \mathrm{Gyr}\) | \(1.79\sigma\) low |
| \(\Lambda\)CDM, DESI + calibrated SN | \(12.729\pm0.193\ \mathrm{Gyr}\) | \(2.32\sigma\) low |
| CST-B2, DESI + calibrated SN | \(12.621\pm0.186\ \mathrm{Gyr}\) | \(2.68\sigma\) low |

The CST joint point therefore carries moderate conditional age pressure. It is not a contradiction: the comparison is local-Gaussian, treats two heterogeneous error budgets as independent, does not reproduce the stellar likelihood, and extends a background ansatz far beyond the fitted redshifts. It is nevertheless an obligation that should travel with any claim that the high-\(H_0\) calibrated branch is a complete resolution.

## Evidential boundary

This is a separately executable robustness test, not an independent multiplication of evidence. Its 1,580 Hubble-flow rows are the same Pantheon+ rows used by [[causal-scale-theory/receipts/fit-late-time-background|the shape-only receipt]], and the joint row reuses the same DESI BAO data. What is new is the retained 77-row Cepheid calibration and the resulting absolute-scale audit.

The durable conclusion is therefore precise:

$$
\text{unit CST-B2 is compatible with this calibrated late-time background likelihood,}
$$

but

$$
\text{the high-}H_0\text{ branch requires a smaller early ruler and pays an age cost.}
$$

Nothing here tests the perturbation sector, primary CMB spectra, CMB lensing, growth, ISW, BBN, or neutrino physics. Those still require the covariant observable map described in [[causal-scale-theory/observables|the observables interface]].

## Reproduction and provenance

Run

```powershell
python causal-scale-theory/receipts/fit-calibrated-background.py `
  --data-dir causal-scale-theory/sources/late-time-background `
  --output causal-scale-theory/receipts/calibrated-background-fit.json
```

The executable is [[causal-scale-theory/receipts/fit-calibrated-background.py|fit-calibrated-background.py]] and the complete machine ledger is [[causal-scale-theory/receipts/calibrated-background-fit.json|calibrated-background-fit.json]]. The numerical Hessian uses parameters \((\Omega_m,\ln H_0,M)\) or \((\Omega_m,\ln H_0,M,\ln r_d)\), a central step of \(5\times10^{-4}\) in each native coordinate, and repeats the calculation at half-step. The largest change in any reported local standard deviation is \(8.2\times10^{-6}\) fractionally.

The pinned official likelihood implementation is at DataRelease commit `c447f0fea703fcd0fff57de5000947b5ca81286b` and has SHA-256 `345fac3781a5cb930b95e91c1c07eb17dcf99b441703bb5e449477519240a59d`.

The archived public products and SHA-256 values are:

| Product | SHA-256 |
|---|---|
| `Pantheon+SH0ES.dat` | `1cb0fc379ef066afdc2ffd1857681cc478024570d8a3eba284fb645775198cf8` |
| `Pantheon+SH0ES_STAT+SYS.cov` | `abf806d966485e64afdb359c87bffc0ecc00d05eff0a31ced66f247385df0fdc` |
| `desi_dr2_bao_mean.txt` | `9ac154ab583ce759c0f7eef3c978c7c70a6ead2d18774caceadf1a350a640585` |
| `desi_dr2_bao_cov.txt` | `252a143274c8a07c78694c119617d36594f6d7965d00319ca611c6ffb886e509` |

[[data/pantheon-plus-shoes-distance-likelihood/entry|The Pantheon+SH0ES module]] and [[data/desi-dr2-bao-gaussian-likelihood/entry|the DESI DR2 module]] own the dataset identities, upstream URLs, and archive provenance. The receipt verifies every archived numeric-product hash before fitting; the official-code hash above is a pinned provenance record because that implementation is not duplicated locally. The executable exits nonzero if a numeric source, row-count, covariance, likelihood-parity, Hessian, search, nuisance-score, or whitening check fails.
