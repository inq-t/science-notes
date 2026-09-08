# Quantity Lines and Conformal Scales

Physical unit lines and conformal density bundles encode different choices. Nonzero \(c,\hbar,G\) convert already specified quantities; a positive conformal scale section selects a metric representative. Turning a mass-derived length into such a section requires an additional smooth positive comparison of bundles. A global Poincare mass Casimir also requires a calibrated translation geometry, which a general curved metric does not supply.

## Calibrated translations and metric scale

Event or region labels, causal comparability, and the calibration of intervals are distinct data. [[conformal-scale-geometry/causal-order-and-metric-scale|Causal order and metric scale]] owns the conformal reconstruction hypotheses and the density-bundle construction. Write \(\mathcal E_{\mathrm{conf}}[w]\) for its weight-\(w\) bundle \(\mathcal E[w]\), and let \(\mathbf g\) be the conformal metric of weight two. A positive section \(\sigma\in\Gamma(\mathcal E_{\mathrm{conf}}[1])\) selects \(g_\sigma=\sigma^{-2}\mathbf g\). The constant \(c\) compares already calibrated spatial and temporal units; it does not select this section.

In a flat translation-invariant realization, let \(\eta_\sigma\) be the calibrated Minkowski representative preserved by translations, with signature \((+---)\), and identify the dual translation Lie algebra with constant covectors. For the strongly commuting physical translation generators \(P^\mu=(H/c,\mathbf P)\), the joint spectral calculus gives

$$
\boxed{
M^2
=
\frac{\eta_\sigma^{-1}(P,P)}{c^2}
=
\frac{H^2}{c^4}
-
\frac{\mathbf P^2}{c^2}.}
\tag{S1}
$$

The [[mass-scale-calibration/mass-as-casimir-and-realization|Poincare representation construction]] supplies the covariance and forward-cone spectrum condition under which this is a nonnegative invariant mass-squared operator. On curved spacetime or for a nonconstant physical scale section, the pointwise norm \(m^2(x)=g_x^{-1}(p_x,p_x)/c^2\) of a local cotangent vector is not automatically a global Poincare Casimir. A change of physical scale geometry can destroy global translations.

The signature above is declared for the mass norm. The \((-+++)\) convention used in [[conformal-scale-geometry/flrw-scale-section-kinematics|FLRW scale-section kinematics]] reverses the sign of a timelike metric norm; its formulas cannot be inserted into (S1) without that convention change.

## Unit-line conversion

Use oriented one-dimensional real quantity lines \(\mathcal U_L,\mathcal U_T,\mathcal U_E,\mathcal U_M\), with positive rays and the dimensional relation
\[
\mathcal U_E
\cong
\mathcal U_M\otimes\mathcal U_L^2\otimes\mathcal U_T^{-2}.
\]
A metre, second, joule, or kilogram is a positive basis choice in the corresponding line. With the nonzero physical conversion quantities
\[
c\in\mathcal U_L\otimes\mathcal U_T^{-1},
\qquad
\hbar\in\mathcal U_E\otimes\mathcal U_T,
\]
multiplication gives the positive isomorphisms
\(c:\mathcal U_T\to\mathcal U_L\) and
\(\hbar:\mathcal U_T^{-1}\to\mathcal U_E\).
They compare duration, length, frequency, and energy. They do not construct a causal cone or a dynamics. The [[library/the-international-system-of-units-si/inq|BIPM SI Brochure, §2.3.1]] gives a metrological example: the metre definition uses the fixed light-speed value together with the second, whose definition uses the specified caesium transition frequency. A reporting standard does not select a Yang–Mills spectral edge.

[[hbar-clock-and-the-calibration-firewall|The clock-calibration theorem]] proves why an abstract spectral generator still requires an independently selected clock or length parameter. Multiplication by \(\hbar\) cannot provide that missing normalization.

For an already given positive mass \(m\in\mathcal U_M\),

$$
\boxed{
\mu_m
:=
\frac{mc}{\hbar}
\in\mathcal U_L^{-1},
\qquad
\lambda_C(m)=\mu_m^{-1}
\in\mathcal U_L.}
\tag{S1a}
$$

The inverse-Compton representative \(\mu_m\), after comparison by \(c\) and \(\hbar\), is dual to length. Its reciprocal requires \(m>0\). Reduced Compton length is a characteristic relativistic quantum wavelength, not a universal localization bound for every interacting, composite, or unstable excitation.

## A physical scale section requires another map

The conformal-density tensor law
\(\mathcal E_{\mathrm{conf}}[w]\otimes\mathcal E_{\mathrm{conf}}[v]\cong\mathcal E_{\mathrm{conf}}[w+v]\)
and its change-of-presentation convention are those of [[conformal-scale-geometry/causal-order-and-metric-scale#Scale as a section|the canonical scale construction]], with [[library/an-introduction-to-conformal-geometry-and-tractor-calculus/inq|Curry and Gover]] as the source. Conformal weight zero does not imply physical dimensionlessness.

A passive change of unit basis changes the numerical component of a fixed quantity. Likewise, changing conformal presentation sends \(g\mapsto\widehat g=\Omega^2g\) and the displayed scale component \(\sigma\mapsto\widehat\sigma=\Omega\sigma\), leaving \(g_\sigma\) unchanged. Selecting a different physical scale section while holding the abstract conformal metric fixed is a different operation: \(\widetilde\sigma=e^f\sigma\) gives \(g_{\widetilde\sigma}=e^{-2f}g_\sigma\). Physical mass variation would require an additional dynamical scale field and coupling.

To turn a metrological length into a conformal scale, supply a positive smooth fiberwise linear isomorphism of real line bundles over the already given manifold \(M\),

$$
\iota:
M\times\mathcal U_L
\longrightarrow
\mathcal E_{\mathrm{conf}}[1].
\tag{S1b}
$$

A smooth positive inverse-length field \(\mu:M\to\mathcal U_L^{-1}\) can then define \(\sigma(x)=\iota_x(\mu(x)^{-1})\). Smoothness, positivity, and invertibility of \(\iota\) ensure that this is a smooth positive scale section. A nowhere-zero field of arbitrary sign would need a positive branch before selecting a positive section.

The comparison \(\iota\) is extra structure and is not canonically supplied by dimensional analysis. Under a passive unit change its components must transform with the unit basis so that the abstract section remains fixed. Without this map, \(mc/\hbar\in\mathcal U_L^{-1}\) does not turn a Poincare mass parameter into a spacetime field or select a metric representative. The spectral threshold and a Weyl compensator remain distinct until a realization theorem relates them.

Renormalization-group scale is another structure. [[scale-score-connection/inq|The scale-score connection]] supplies differentiation of a state family only after a common carrier bundle and its transport have been chosen. That connection is neither the conformal scale section nor the metrological comparison \(\iota\).

## Planck area converts inverse length to length

For positive \(G,c,\hbar\), the Planck area is the nonzero quantity
\[
\ell_P^2:=\frac{\hbar G}{c^3}\in\mathcal U_L^2.
\]
Multiplication gives the exact quantity-line isomorphism

$$
\boxed{
\mathcal U_L^{-1}
\xrightarrow{\ \ell_P^2\ }
\mathcal U_L,
\qquad
\mu_m
\longmapsto
\ell_P^2\mu_m
=
\frac{Gm}{c^2}
=
\ell_G(m).}
\tag{S1c}
$$

Here \(\ell_G(m)=Gm/c^2\) omits the Schwarzschild factor two: \(r_s(mc^2)=2\ell_G(m)\). [[deriving-value-of-g/capacity-identities|Capacity and compactness]] uses that Schwarzschild convention when comparing \(r_s\) with the reduced Compton length.

This factorization sends the inverse-Compton representative of an already given mass to its gravitational length. It generates no mass, selects no conformal section, and derives neither \(G\) nor a Yang–Mills threshold. The constants and the input mass already occur in both presentations.
