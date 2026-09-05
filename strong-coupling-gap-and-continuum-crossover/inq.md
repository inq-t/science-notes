---
inq.module: "strong-coupling-gap-and-continuum-crossover"
inq.include:
  - "./"
inq.ambient:
  - "**"
---
# Strong-Coupling Gaps and the Continuum Crossover

Pure lattice gauge theory is not generically unable to produce a mass gap: rigorous strong-coupling work gives exponential clustering and isolated glueball states at fixed regulator. The unsolved four-dimensional problem lies across the coupling diagram. Strong-coupling estimates apply at small lattice inverse coupling, whereas the asymptotically free continuum trajectory sends the bare inverse coupling to infinity and the one-step lattice contraction toward one. A continuum mass gap therefore requires a transfer estimate uniform in spatial volume whose logarithmic deficit scales linearly with the temporal lattice spacing, or equivalently a fixed-physical-slab contraction that survives regulator removal.

**Status: [PRIMARY-SOURCE THEOREM] for the finite-regulator transfer construction, strong-coupling clustering, and strong-coupling isolated glueball states; [EXACT SCALING CONSEQUENCE] for the one-step and fixed-slab continuum targets; [OPEN] for a volume-uniform estimate along the four-dimensional asymptotically free continuum trajectory.**

## A regulated gap is not the missing phenomenon

For Wilson lattice gauge theory at finite spatial volume and lattice spacing,
[[library/construction-of-a-selfadjoint-strictly-positive-transfer-matrix-for-euclidean-lattice-gauge-theories/inq|Luscher]]
constructs a bounded self-adjoint strictly positive transfer matrix \(T\) on
the gauge-invariant carrier. Strict positivity permits a logarithm, but it
does not by itself mean that the vacuum is unique or isolated:

$$
H_{a,L}
:=
-\frac{\hbar c}{\ell_a}
\log\widehat T_{a,L},
\qquad
\widehat T_{a,L}
:=
\frac{T_{a,L}}{\lambda_0(a,L)}.
\tag{SC1}
$$

Here \(\ell_a\) is the Euclidean length represented by one temporal lattice
step and \(\lambda_0\) is the top transfer eigenvalue. A gap is the stronger
statement that the spectrum of \(H_{a,L}-E_0\) on the vacuum complement has a
positive lower edge.

At sufficiently strong coupling, that stronger phenomenon is known.
[[library/gauge-field-theories-on-a-lattice/inq|Osterwalder--Seiler]] obtain
volume-uniform strong-coupling cluster control and physical positivity.
[[library/existence-of-glueballs-in-strongly-coupled-lattice-gauge-theories/inq|Schor]]
proves that plaquette correlations have an isolated simple pole in the
complex energy variable at large coupling, implying isolated one-particle
glueball states. More recently,
[[library/a-stochastic-analysis-approach-to-lattice-yang-mills-at-strong-coupling/inq|Shen--Zhu--Zhu]]
prove an infinite-volume measure, functional inequalities, and exponential
correlation decay for \(SU(N)\) under the explicit condition

$$
|\beta|<\frac1{16(d-1)}
\tag{SC2}
$$

in their \(N\beta\,\operatorname{ReTr}\) normalization. In \(d=4\), this is
\(|\beta|<1/48\).

The Langevin Poincare inequality in the last result is a gap for sampler
time, not automatically the Hamiltonian gap. Its exponential decay of the
actual Wilson correlations is physically relevant, and reflection
positivity can relate temporal correlation decay to transfer spectral
support. The two statements must not be conflated: an auxiliary Markov
generator and the Euclidean-time Wilson transfer are different operators.

[[wilson-slab-conditional-fisher-certificate|The conditional-Fisher slab certificate]] supplies an explicit same-vacuum realization of the bridge programme: a finite-history Dobrushin bound controls the true vacuum and its joint endpoint scores, then gives a complete midpoint floor and a physical transfer rate. Its small spatial and temporal Wilson parameters are stated separately. [[hamiltonian-product-vacuum-stability|Product-vacuum stability]] supplies a distinct continuous-time, fixed-spatial-lattice anchor by applying a published local-perturbation theorem to compact electric rotors. Neither certificate crosses the weak-bare-coupling continuum trajectory.

## The continuum trajectory leaves that theorem's regime

[[temporal-column-response/inq|Temporal-column response]] improves the time-refinement leg without dropping the interaction: a complete path is one variable in a compact Wasserstein metric, and its conditional block mixing bounds the cost of a local exterior insertion. [[wilson-temporal-column-coercivity|The Wilson application]] yields an explicit vacuum Poincare floor uniform in spatial volume and \(x\to\infty\) when \((d_s-1)\beta_s x\le1/200\). [[wilson-to-hamiltonian-vacuum-limit|The vacuum-limit theorem]] passes that floor to the continuous-time lattice Hamiltonian. This is not a finite-step Wilson-to-Laplacian form comparison or a complete two-endpoint bridge theorem; the small magnetic/electric ratio still excludes the spatial continuum trajectory.

For the standard four-dimensional Wilson normalization,

$$
\beta_{\mathrm{lat}}(a)
=
\frac{2N}{g_0(a)^2}.
\tag{SC3}
$$

Asymptotic freedom requires

$$
g_0(a)\longrightarrow0,
\qquad
\beta_{\mathrm{lat}}(a)\longrightarrow\infty
\qquad(a\downarrow0).
\tag{SC4}
$$

Strong-coupling expansions and the explicit bound (SC2) control a
neighborhood of \(\beta=0\). The continuum trajectory runs toward the
opposite end of the bare-coupling axis. The known theorem is therefore not a
slightly nonuniform version of the Clay target; it controls a disjoint
regime.

This identifies a precise crossover problem:

$$
\boxed{
\text{strong-coupling physical contraction}
\quad\xrightarrow{\text{RG and continuum control}}\quad
\text{finite positive physical rate at }\beta_{\mathrm{lat}}\to\infty .}
\tag{SC5}
$$

The arrow includes ultraviolet construction, infrared uniformity, vacuum
control, and scale setting. Universality heuristics do not constitute that
arrow.

## A proposed crossover proof and its missing inequalities

[[library/reflection-positive-construction-of-four-dimensional-su-n-yang-mills-theory-with-mass-gap-and-confinement/inq|Faizal and Shabir's proposed construction]], main article in arXiv v1, illustrates three distinct obligations. At printed pp. 128--129, (11.1)/(11.3) bound the next transfer operator **below**; (11.5) uses an **upper** bound that does not follow. Equation (11.8) also needs
\(\sum_k c_k\varepsilon_k<\Delta_0\), not merely a finite error sum. At printed p. 125, (10.72)--(10.74) allow an \(O(g_k^2)\) remainder with \(g_k^2\sim C/k\); that estimate does not establish absolute summability. It does not prove that the actual remainder diverges either: a sharper estimate or cancellation could repair it.

These are equation-level missing implications in the main article, not a verdict on every appended supporting paper, nor an impossibility theorem for reflection-positive renormalization or strong-to-weak coupling constructions. The paper does address entry into a controlled regime; that separate argument is not resolved by these three checks.

## A finite physical mass forces the one-step gap to close

Let \(P_{0,a,L}\) project onto the intended vacuum sector and suppose the
smallest nonvacuum energy tends to a finite physical value \(\Delta_E>0\).
Functional calculus gives

$$
\left\|
\widehat T_{a,L}(I-P_{0,a,L})
\right\|
=
\exp\!\left[
-\frac{\ell_a\Delta_E}{\hbar c}
+o(\ell_a)
\right].
\tag{SC6}
$$

Hence

$$
1-
\left\|
\widehat T_{a,L}(I-P_{0,a,L})
\right\|
=
\frac{\ell_a\Delta_E}{\hbar c}
+o(\ell_a).
\tag{SC7}
$$

The adjacent-slice transfer gap must close linearly with the regulator. A
fixed \(a\)-independent one-step deficit would instead describe an energy
diverging like \(\hbar c/\ell_a\). Conversely, proving only that every fixed
regulator has some positive deficit says nothing about whether its physical
rate survives.

This is why a fixed physical slab is the clean norm target. For
\(r>0\), set \(n_a=\lfloor r/\ell_a\rfloor\). The required form is

$$
\boxed{
\left\|
\widehat T_{a,L}^{\,n_a}
-P_{0,a,L}
\right\|_{\mathcal H_{\mathrm{phys},0}}
\leq
\exp\!\left[
-\frac{r\Delta_E}{\hbar c}+o(1)
\right]}
\tag{SC8}
$$

uniformly in spatial volume \(L\), followed by convergence of the carriers,
vacua, translations, and observables to a nontrivial continuum theory.
Equation (SC8) is equivalent to the one-step logarithmic-rate target

$$
\liminf_{a\downarrow0}\inf_L
\frac{\hbar c}{\ell_a}
\left[
-\log
\left\|
\widehat T_{a,L}(I-P_{0,a,L})
\right\|
\right]
>0,
\tag{SC9}
$$

provided the same vacuum-reduced physical carriers and limiting
normalization are controlled.

## Where the innovation programme enters

[[gauge-cycle-innovation-filtration/inq|Gauge-Cycle Innovation Filtration]]
and [[gauge-boundary-frame-gluing/inq|Gauge Boundary Frames and Gauss
Gluing]] do not attempt to analytically continue a strong-coupling series.
They supply a complete, gauge-correct block frame for the actual
Perron-dressed transfer. If

$$
q_{a,L}
:=
r_{a,L}+\sqrt{R_{a,L}S_{a,L}}
\tag{SC10}
$$

bounds its centered physical contraction, the correctly scaled target is

$$
\liminf_{a\downarrow0}\inf_L
\frac{\hbar c}{\ell_a}
[-\log q_{a,L}]
>0,
\tag{SC11}
$$

or a subunit version of the corresponding fixed-slab matrix. Boundary-charge
gluing prevents the local blocks from deleting cross-cut loops; complete
innovations prevent a hidden global parity or topological mode from escaping
the estimate.

The strong-coupling theorems provide a calibration demand: in their common
regime, a successful innovation or same-carrier Dirichlet estimate should
recover a positive physical transfer rate. The continuum theorem must then
control how that rate renormalizes as the bare trajectory leaves the
strong-coupling domain.

## Copernican lesson and claim boundary

The established strong-coupling gap is evidence against one overly broad
diagnosis: the Yang--Mills formalism does not fail to admit gapped physical
sectors at all. The unresolved problem is whether a nontrivial
four-dimensional continuum theory exists on the required physical carrier
and retains a finite, volume-uniform spectral edge.

The conceptual reversal still matters. A mass gap is not the binary spectrum
of a quotient, the \(\{0,1\}\) spectrum of a conditional expectation, or a
local symmetry label. It is a lower edge of the reconstructed
energy--momentum spectrum, equivalently a calibrated uniform attenuation rate
of every nonvacuum physical distinction. Carrier formation, boundary
gluing, attenuation, clock reconstruction, and dimensional calibration are
separate arrows. The new algebra can succeed only if it proves the estimate
on the same carrier and across the crossover, not by renaming an upstream
projection gap as mass.

## Sources

- [[library/construction-of-a-selfadjoint-strictly-positive-transfer-matrix-for-euclidean-lattice-gauge-theories/inq|Luscher]] supplies the genuine finite Wilson transfer and its physical gauge-invariant carrier.
- [[library/gauge-field-theories-on-a-lattice/inq|Osterwalder--Seiler]] supply reflection positivity and strong-coupling infinite-volume control.
- [[library/existence-of-glueballs-in-strongly-coupled-lattice-gauge-theories/inq|Schor]] supplies direct isolated-glueball spectral evidence at strong coupling.
- [[library/a-stochastic-analysis-approach-to-lattice-yang-mills-at-strong-coupling/inq|Shen--Zhu--Zhu]] supply explicit volume-uniform functional inequalities and exponential correlation decay in a declared strong-coupling region.
