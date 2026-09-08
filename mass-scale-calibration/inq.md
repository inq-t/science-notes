---
inq.module: mass-scale-calibration
inq.include:
  - './'
inq.ambient:
  - 'receipts/*.py'
  - 'receipts/*.txt'
keywords:
  - mass
  - scale torsor
  - clock calibration
  - quantity lines
  - Poincare Casimir
  - joint causal generators
  - transfer attenuation
  - generalized Rayleigh quotient
  - exchange rates
---
# Mass, Scale, and Calibration

A spectral exclusion, a clock rate, an energy threshold, and an invariant mass are different mathematical objects. Their conversion requires a common carrier, independently normalized comparison maps, and—at the mass step—a compatible Poincare representation. This module develops that reusable calibration structure: it separates the dimensionless content of a gap from its units, identifies mass with a joint invariant rather than an arbitrary single generator, and states what a proposed geometric or entropic yardstick must supply. The conversion theorems are exact under their hypotheses; the primitive origin of the carrier, its positive edge, and its preferred calibration remains a construction problem.

## An invariant is not a chosen clock

[[mass-scale-calibration/mass-as-casimir-and-realization|The realization signature]] places relativistic mass in the joint translation representation. For strongly commuting generators \((H,\mathbf P)\) of a positive-energy Poincare representation,

\[
\mathcal C=H^2-c^2\mathbf P^2=M^2c^4.
\]

With \(P_0\) the complete zero-translation projection, Lorentz covariance gives

\[
H\geq\Delta(1-P_0)
\quad\Longleftrightarrow\quad
\mathcal C\geq\Delta^2(1-P_0).
\]

This equivalence is not available merely because a finite regulator or an auxiliary process has a positive generator. The internal gauge Casimir, the Poincare Casimir, and the center of an observable algebra are different objects. Nor does a positive mass threshold require a discrete excitation spectrum: boost covariance rules out positive normalizable **energy** eigenvectors in a nontrivial Poincare representation, while a sharp invariant mass is compatible with continuously varying momentum.

[[mass-scale-calibration/joint-causal-generators-and-the-mass-casimir|Joint causal generators]] gives the simplest concrete reason to seek mass at this joint level. In natural units on \(L^2(\mathbb R,d\theta)\),

\[
P_+=m e^{\theta},\qquad P_-=m e^{-\theta},\qquad
P_+P_-=m^2I,\qquad H=m\cosh\theta.
\]

Each null generator has spectrum down to zero, although their product has a positive floor. Opposite rescalings change the rapidity frame and preserve the product; a common rescaling changes its mass scale. The example supplies \(m\) as an input. A modular construction must still produce the compatible joint generators and prove their coercivity, not infer mass from one modular logarithm or one half-sided inclusion.

## The numerator and the yardstick

On an already reconstructed quantum carrier, [[mass-scale-calibration/mass-as-a-calibrated-distinction-rate|transfer attenuation]] gives the exact rate presentation

\[
R(\ell)
:=-\log\left\|e^{-\ell H/(\hbar c)}(1-P_0)\right\|
=\frac{\ell\Delta_E}{\hbar c},
\qquad
m_{\mathrm{gap}}=\frac{\hbar}{c}\frac{dR}{d\ell},
\]

where the last equality requires the Poincare equivalence above. The dimensionless numerator is logarithmic attenuation, not automatically entropy production or a count of recorded facts. A finite-time heat transfer is injective; its attenuation alone does not choose an outcome or produce a record.

[[mass-scale-calibration/hbar-clock-and-the-calibration-firewall|Clock and action calibration]] separates the corresponding upstream steps. If \(e^{-uK}\) has only an abstract dimensionless parameter, then \(u'=a u\) and \(K'=K/a\) describe the same family. A separately constructed clock comparison \(\nu=du/d\tau\) transforms as \(\nu'=a\nu\). Only the product \(\nu K\) has a fixed rate meaning. An action comparison \(\mathfrak a_Q\), identified with \(\hbar\) in the quantum presentation, then converts rate to energy. Exact carrier and vacuum identification gives

\[
\Delta_E=\mathfrak a_Q\nu\delta_K,
\qquad
m_{\mathrm{gap}}=\frac{\mathfrak a_Q\nu}{c^2}\delta_K,
\]

with \(\delta_K\) the nonzero-sector spectral infimum. With a weaker carrier map, these equalities must be replaced by domain-correct form comparisons and quantitative coverage. Planck's constant supplies neither the clock nor that coverage.

[[mass-scale-calibration/scale-torsor-and-the-global-local-gap-invariant|The positive scale torsor]] expresses the absence of a preferred numerical unit without asserting the absence of physical scale. Under matched transport between presentations, \(\ell\mapsto a\ell\) and an inverse-length generator \(K\mapsto K/a\) preserve the form \(\ell K\) and its dimensionless edge. This family covariance differs from exact dilation symmetry of one fixed nonzero operator, which forbids a positive lower spectral edge. It also differs from selecting a conformal metric section: [[conformal-scale-geometry/inq|conformal scale geometry]] owns that geometric operation, and [[scale-score-connection/inq|the scale-score connection]] owns differentiation between moving carriers.

## A relative edge requires two forms on one carrier

[[mass-scale-calibration/internal-yardstick-as-a-generalized-rate-edge|The generalized rate edge]] makes a proposed internal yardstick precise through

\[
Q_{\mathrm{rat}}
=\inf_{0\ne x\in\mathcal D}
\frac{\mathfrak a[x]}{\mathfrak b[x]}.
\]

The numerator and denominator must be comparably typed closed forms on a declared common domain, with \(\mathfrak b[x]>0\) there. The quotient is primary; writing \(B^{-1/2}AB^{-1/2}\) does not discharge its density, closure, or transformed-core requirements. Transporting both forms makes the relative edge meaningful; it does not prove that the edge is positive.

The reusable implication from such a response to physical energy belongs to [[measured-response-carriers/response-to-energy-comparison|response-to-energy comparison]]: a lower response bound, carrier coverage, and an independently normalized energy comparison are separate premises. A cosmological rate or categorical index may be proposed as calibration data, but the common-carrier, clock, and capacity identifications in the internal-yardstick note are conditional applications, not universal consequences of the quotient. The specific [[cosmological-scale-selection/cosmological-selection-of-the-yang-mills-yardstick|cosmological Yang--Mills selector]] remains a downstream proposal.

## Exchange rates do not identify the exchanged concepts

[[mass-scale-calibration/mass-and-g-as-dual-exchange-rates|The dual exchange-rate construction]] compares two distinct readings of a dimensionless ledger. Quantum transfer supplies an all-direction logarithmic rate; the Einstein horizon area law supplies the compliance \(dA/d(S/k_B)=4\hbar G/c^3\). Their composition is valid only after a same-ledger, same-tangent, same-clock theorem. A first-order entropy differential cannot simply be identified with a positive quadratic energy response, and nonzero gravitational compliance does not imply a positive mass gap.

The resulting research question is structural rather than metrological: which construction fixes the relative response, its complete carrier, and its calibration together without inserting the target spectrum? [[global-local-response-reconstruction/inq|Global--local response reconstruction]] owns the return from those data to local quantum field theory. The [[contemporary-puzzles/yang-mills-mass-gap/clay-contract-and-scale-assumptions|Clay contract]] adds the specific Yang--Mills existence, ultraviolet, and continuum requirements. Calibration clarifies those obligations; it does not replace their proof.
