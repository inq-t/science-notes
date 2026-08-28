# Generalized CST-B2 Background Profile

This receipt releases the CST-B2 rate ν and canonical integrated reference ratio \(\mathfrak R_c\) against Pantheon+ and two DESI inputs. The canonical comparison uses the fully released 2025 DR2 BAO mean vector and covariance; a separate 2026 Ly\(\alpha\) published-Gaussian substitution is retained only as a provisional update. On the released data, the frozen unit point lies inside the nominal joint two-parameter \(\Delta\chi^2=2.30\) contour and added flexibility is not rewarded by AIC, although \(\nu=1\) sits just outside two one-dimensional \(\Delta\chi^2=1\) profiles. These are profile-likelihood contours, not posterior credible intervals or coverage-calibrated confidence intervals.

## Closure and exhaustive branch coordinate

For

$$
D:=1-\Omega_{m0}-\Omega_{r0},
\qquad
F_\nu(x):=
\left(\Omega_{m0}e^{3x}+\Omega_{r0}e^{4x}\right)
\operatorname{sech}^2(\nu x),
$$

the exact present-flatness equation is

$$
\boxed{
\frac{\mathfrak R_c}{2-\mathfrak R_c}F_\nu(x_c)=D.}
$$

The historical scalar called \(r_c\) is not the canonical integrated ratio:

$$
r_c=\frac{\mathfrak R_c}{2-\mathfrak R_c},
\qquad
\mathfrak R_c=\frac{2r_c}{1+r_c}.
$$

Set \(y=e^{x_c}>0\). The same closure is the exact generalized-power equation

$$
4\frac{\mathfrak R_c}{2-\mathfrak R_c}
\left(\Omega_{m0}y^{3+2\nu}+\Omega_{r0}y^{4+2\nu}\right)
=D(1+y^{2\nu})^2.
$$

It is an ordinary polynomial only for suitable rational or integral rates after a further substitution.

Rather than selecting one root at fixed \((\nu,\mathfrak R_c)\), the likelihood uses

$$
a_c:=\nu x_c,
\qquad
\boxed{
\mathfrak R_c=\frac{2D}{D+F_\nu(x_c)}.}
$$

Thus every admitted \((\Omega_{m0},\nu,x_c)\) labels one root-background pair and returns its canonical \(\mathfrak R_c\). This parameterizes all branches in the declared domain even when one fixed \((\Omega_{m0},\nu,\mathfrak R_c)\) has several roots. The expansion law depends smoothly on \((\Omega_{m0},\nu,a_c)\):

$$
E^2(z)=\Omega_{m0}(1+z)^3+\Omega_{r0}(1+z)^4
+D\frac{\cosh^2a_c}
{\cosh^2\!\left(a_c-\nu\ln(1+z)\right)}.
$$

The numerical envelope is

$$
0.15\le\Omega_{m0}\le0.50,
\quad
10^{-3}\le\nu\le4,
\quad
10^{-8}\le a_c\le10,
$$

with no artificial interior cutoff on \(0<\mathfrak R_c<2\). The upper \(a_c\) boundary is already in the observationally saturated constant-\(w\) tail over the data redshift range.

## Root theorem used by the profile

For \(x<0\),

$$
\frac{\mathrm d}{\mathrm dx}\ln F_\nu
=\frac{3\Omega_me^{3x}+4\Omega_re^{4x}}
{\Omega_me^{3x}+\Omega_re^{4x}}
-2\nu\tanh(\nu x)>0.
$$

Hence exactly one negative root exists iff \(\mathfrak R_c>2D\), a root lies at zero iff \(\mathfrak R_c=2D\), and no negative root exists iff \(\mathfrak R_c<2D\).

For \(x>0\) and \(0<\nu\le3/2\), the same derivative is strictly positive because its first term is at least three while \(2\nu\tanh(\nu x)<3\). Thus the positive root is unique when \(\mathfrak R_c<2D\) and absent when \(\mathfrak R_c\ge2D\), apart from the zero root at equality.

For \(3/2<\nu<2\), two stationary points and three positive roots can occur. For \(\nu>2\), the positive graph is unimodal and at most two positive roots occur. The receipt does not discard these branches: \(x_c\) is the fit coordinate. No branch switch occurs in any reported likelihood interval because every materially supported endpoint has \(\nu<3/2\).

## Released 2025 nested tests

The canonical ledger uses 1,580 Pantheon+ rows and all thirteen entries of the released DESI DR2 BAO mean vector with its released covariance. It fixes \(\Omega_{r0}=9.15\times10^{-5}\) and profiles the supernova offset and \(c/(H_0r_d)\) exactly as in [[causal-scale-theory/receipts/fit-late-time-background|the frozen-background receipt]].

| Positive-reference model | \(\chi^2_{\min}\) | best \(\Omega_{m0}\) | best \(\nu\) | best \(\mathfrak R_c\) | best \(x_c\) |
|---|---:|---:|---:|---:|---:|
| frozen unit | 1396.526309 | 0.322394 | 1 | 1 | 0.271746 |
| \(\mathfrak R_c=1\), \(\nu\) free | 1395.361037 | 0.315527 | 0.799485 | 1 | 0.273811 |
| \(\nu=1\), \(\mathfrak R_c\) free | 1396.489890 | 0.322106 | 1 | 1.014104 | 0.260904 |
| \(\nu,\mathfrak R_c\) free | 1394.628814 | 0.308398 | 0.578126 | 0.698656 | 0.504268 |

At the joint maximum, the historical scalar is \(r_c=0.536872\). The frozen unit point is

$$
\Delta\chi^2_{(1,1)}=1.897495
$$

above the two-parameter maximum, still below the nominal two-parameter \(\Delta\chi^2=2.30\) contour.

The released-data one-dimensional profiles are:

| Fit | \(\Delta\chi^2=1\) | \(\Delta\chi^2=3.84\) |
|---|---:|---:|
| \(\mathfrak R_c=1\), profile \(\nu\) | [0.5700, 0.9863] | [0.2093, 1.1448] |
| \(\nu=1\), profile \(\mathfrak R_c\) | [0.9416, 1.0900] | [0.8753, 1.1656] |
| both free, profile \(\nu\) | [0.08613, 0.9057] | [0.02078, 1.1408] |
| both free, profile \(\mathfrak R_c\) | \((0,1.0241]\), open lower tail | \((0,1.1682]\), open lower tail |

The distinction among those rows matters. With \(\mathfrak R_c=1\) imposed, releasing \(\nu\) improves the fit by \(1.1653\), so \(\nu=1\) falls just outside that one-dimensional \(\Delta\chi^2=1\) contour while remaining inside \(\Delta\chi^2=3.84\). With \(\nu=1\) imposed, \(\mathfrak R_c=1\) is comfortably inside both displayed contours. In the joint fit, the profiled \(\nu=1\) coordinate is outside \(\Delta\chi^2=1\), the profiled \(\mathfrak R_c=1\) coordinate is inside it, and the frozen point \((1,1)\) remains inside the joint two-parameter \(\Delta\chi^2=2.30\) contour. There is therefore no blanket “inside every one-dimensional contour” conclusion.

Both joint \(\mathfrak R_c\) contours are open toward zero. The attainable constant-\(w\) tail has \(\chi^2=1395.009421\), only \(0.380607\) above the joint maximum. Current released background data therefore do not independently identify \(\mathfrak R_c\) once \(\nu\) is also free.

Relative to frozen unit CST-B2, the released-data AIC changes are \(+0.8347\), \(+1.9636\), and \(+2.1025\) for, respectively, \(\nu\) free at \(\mathfrak R_c=1\), \(\mathfrak R_c\) free at \(\nu=1\), and both free. The corresponding BIC changes are \(+6.2081\), \(+7.3370\), and \(+12.8493\). Parameter penalties therefore favor the frozen member despite the lower generalized \(\chi^2\).

The bounded negative-reference audit gives \(\chi^2=1399.841979\), worse than frozen unit by \(3.3157\) and worse than the generalized positive-reference maximum by \(5.2132\). As in the provisional row below, this is a finite-domain numerical audit rather than a proof about every negative-reference extension.

This result is **[REPRODUCED GENERALIZED PROFILE — RELEASED 2025 INPUT]**. It is the canonical direct-background unity audit because both the DESI mean vector and covariance used by the fit are released artifacts.

## Provisional 2026 Gaussian-update nested tests

The receipt uses 1,580 released Pantheon+ rows, eleven released 2025 lower-redshift DESI distances, and the published two-dimensional 2026 Ly\(\alpha\) block. It fixes \(\Omega_{r0}=9.15\times10^{-5}\) and profiles the supernova offset and \(c/(H_0r_d)\) exactly as in [[causal-scale-theory/receipts/fit-late-time-background|the frozen-background receipt]]. The zero cross-covariance assumption must be replaced when DESI releases the full 2026 likelihood product.

| Positive-reference model | \(\chi^2_{\min}\) | best \(\Omega_{m0}\) | best \(\nu\) | best \(\mathfrak R_c\) | best \(x_c\) |
|---|---:|---:|---:|---:|---:|
| frozen unit | 1398.284564 | 0.325512 | 1 | 1 | 0.265996 |
| \(\mathfrak R_c=1\), \(\nu\) free | 1397.330616 | 0.319215 | 0.811096 | 1 | 0.267908 |
| \(\nu=1\), \(\mathfrak R_c\) free | 1398.099129 | 0.324437 | 1 | 1.031026 | 0.243144 |
| \(\nu,\mathfrak R_c\) free | 1397.260212 | 0.318144 | 0.759756 | 0.954720 | 0.301474 |

At the joint maximum, the legacy scalar is \(r_c=0.913363\). The unit point is only

$$
\Delta\chi^2_{(1,1)}=1.024352
$$

above the two-parameter maximum, below the nominal two-parameter \(\Delta\chi^2=2.30\) contour.

The one-dimensional profiles are:

| Fit | \(\Delta\chi^2=1\) | \(\Delta\chi^2=3.84\) |
|---|---:|---:|
| \(\mathfrak R_c=1\), profile \(\nu\) | [0.5717, 1.0042] | [0.1814, 1.1663] |
| \(\nu=1\), profile \(\mathfrak R_c\) | [0.9598, 1.1050] | [0.8942, 1.1781] |
| both free, profile \(\nu\) | [0.3287, 1.0195] | [0.00916, 1.2245] |
| both free, profile \(\mathfrak R_c\) | [0.1982, 1.0895] | \((0,1.2412]\) with an open lower tail |

The last lower endpoint is genuinely open, not a failed optimizer bracket. As \(\mathfrak R_c\to0\) and \(a_c\to+\infty\), the family contains the attainable constant-\(w\) limit

$$
\rho_X(z)/\rho_{X0}=(1+z)^{2\nu}.
$$

Its best direct fit has \(\chi^2=1398.686493\), still below the joint \(\Delta\chi^2=3.84\) threshold. Present background data therefore do not give a two-sided 95-percent profile bound on the integrated ratio.

## Provisional 2026 parameter cost and non-past branch

Relative to frozen unit CST-B2, the AIC changes are

$$
\Delta\mathrm{AIC}=
\begin{cases}
+1.0461,&\mathfrak R_c=1,\ \nu\text{ free},\\
+1.8146,&\nu=1,\ \mathfrak R_c\text{ free},\\
+2.9756,&\nu,\mathfrak R_c\text{ free}.
\end{cases}
$$

For the 1,593-element data vector, the corresponding BIC changes are \(+6.4194\), \(+7.1879\), and \(+13.7224\). The generalized maximum is descriptive flexibility, not evidence against either unit principle.

A separate finite audit over

$$
0.02\le\nu\le4,
\qquad
-10\le a_c<0
$$

finds no competitive present/future-reference solution. Its optimum runs to \(\nu=0.02\), \(a_c\to0^-\), and \(\chi^2=1401.629054\), the flat-\(\Lambda\) limit. It is worse than frozen unit CST-B2 by \(3.3445\) and worse than the generalized positive-reference maximum by \(4.3688\). This is a bounded numerical audit, not a proof about every negative-reference extension.

## Reproduction and status

Run the canonical released-data profile with

```powershell
python causal-scale-theory/receipts/fit-generalized-background.py `
  --dataset desi-dr2-bao-2025 `
  --bao-data-dir data/desi-dr2-bao-gaussian-likelihood `
  --pantheon-data-dir data/pantheon-plus-shoes-distance-likelihood/local `
  --output causal-scale-theory/receipts/generalized-background-fit-2025.json
```

Run the provisional published-Gaussian update with

```powershell
python causal-scale-theory/receipts/fit-generalized-background.py `
  --dataset desi-dr2-lya-2026 `
  --bao-data-dir data/desi-dr2-bao-gaussian-likelihood `
  --pantheon-data-dir data/pantheon-plus-shoes-distance-likelihood/local `
  --output causal-scale-theory/receipts/generalized-background-fit.json
```

The script verifies the source hashes, imports the base likelihood implementation, algebraically seeds the physical closure domain before optimization, profiles every stated nuisance and response parameter, and checks the nesting order. It writes [[causal-scale-theory/receipts/generalized-background-fit-2025.json|the released-data ledger]] and [[causal-scale-theory/receipts/generalized-background-fit.json|the provisional-update ledger]]. The released 2025 \(\nu=1\) profile directly replaces the old reported \(1.025\,[0.941,1.088]\) amplitude profile as the canonical late-time calculation; it does not claim to reproduce that historical likelihood or its differently named parameter exactly.

The supplemental 2026 result is **[PROVISIONAL PUBLISHED-GAUSSIAN UPDATE]**. It says that this published compression is compatible with both unity principles but does not identify either one; AIC prefers the frozen unit member to the added flexibility. Reproducibility of the calculation does not promote its input into a released likelihood. Neither ledger tests the microscopic meaning of \(\nu\), the horizon-capacity interpretation of \(\mathfrak R_c\), perturbations, or primary CMB anisotropies.
