# Yang–Mills Response Calibration

A static response exponent becomes a Yang–Mills energy or mass bound only after a nontrivial continuum law, total local observable family, physical distance scale, and OS/Poincare reconstruction have been supplied. Strong-coupling lattice estimates establish a finite-regulator precedent; the gauge-covariant passage from the asymptotically free trajectory to a fixed physical block scale remains open.

## The continuum construction still required

[[library/a-stochastic-analysis-approach-to-lattice-yang-mills-at-strong-coupling/inq|Shen, Zhu, and Zhu]] prove a volume-uniform auxiliary Poincare gap and correlation decay for the \(SU(N)\) and \(SO(N)\) Wilson laws under their explicit strong-coupling condition \(K_{\mathcal S}>0\). In Corollary 1.6, the decay exponent \(c_N\) depends on \(K_{\mathcal S},N,d\), while the prefactor can depend on the observable support sizes. Their proof combines semigroup forgetting with local-derivative propagation, realizing the mechanism of [[auxiliary-clock-elimination|(ARL4)–(ARL7)]]. This support-independent exponent is a useful precedent for the total-family requirement; the theorem does not establish uniformity under arbitrary pinnings or along a continuum trajectory.

Four-dimensional continuum Yang--Mills approaches weak bare coupling. The [[yang-mills-continuum-crossover/asymptotically-free-response-crossover-lemma|asymptotically free response-crossover lemma]] states the missing gauge-covariant RG construction: carry that ultraviolet law to a fixed physical block scale at which either of the following holds uniformly:

1. the [[witten-covariance-and-local-response|Witten]] or [[auxiliary-clock-elimination|semigroup]] estimates yield one common physical exponent on a gauge-invariant local family whose complex linear span is Hilbert-norm dense in the reconstructed vacuum complement; or
2. the effective polymer law satisfies the all-pinnings estimate (ARL20) of [[conditional-correlation-tensorization/inq|conditional correlation tensorization]], with the resulting bunch-to-bunch kernel norm uniformly below one.

The estimates must be uniform in cutoff, volume, admissible boundary condition, and retained neutral sector. They must survive the diverging number of RG steps, preserve reflection positivity or supply another valid reconstruction, and identify the limiting local theory as nontrivial Yang--Mills. For each chosen local observable pair, the complete covariance prefactor, including transported source norms, must remain controlled through the limit; uniform exponents alone do not ensure a limiting bound. Support separation must be compared to Euclidean time-translation length. Equal-time spatial clustering needs Euclidean covariance or another comparison theorem before it supplies the positive diagonal autocorrelations in [[positive-semigroup-decay/total-family-spectral-gap|the total-family spectral theorem]]. A Hilbert-total local family is sufficient; being an operator or form core is not required. The family must fill the declared vacuum complement, with vacuum uniqueness proved separately when a unique-vacuum claim is made.

## A lower edge per physical length

If \(m_a\) denotes a dimensionless exponent per raw Euclidean-time lattice step \(a_{\tau,a}\), the physical inverse length is

$$
\sigma_a=\frac{m_a}{a_{\tau,a}}.
\tag{ARL21}
$$

Together with the preceding limiting-law and uniformity hypotheses, a certified positive continuum floor requires

$$
\liminf_{a\to0}\frac{m_a}{a_{\tau,a}}
\geq
\sigma_*>0.
\tag{ARL21a}
$$

Convergence to a specified finite edge would require the stronger limit \(m_a/a_{\tau,a}\to\sigma_*\); asymptotic equivalence is not needed for a lower-bound theorem. At a fixed physical blocked spacing \(b_*\), the corresponding conversion is \(\sigma_*=m_*/b_*\). [[positive-semigroup-decay/physical-reconstruction-and-units|Physical reconstruction and units]] supplies the OS clock comparison, while [[mass-scale-calibration/mass-as-a-calibrated-distinction-rate|mass as a calibrated distinction rate]] owns the downstream conversion of an actual transfer edge. Neither a sampler gap nor a raw lattice exponent alone supplies that physical scale.

## The Copernican interpretation

The proposed invariant describes how a local distinction induces a whole-law response with a finite localization length independent of the proof clock. In the language of the programme, the response to a pointed local score admits an exponentially localized presentation.

After the common-exponent spectral comparison has been proved and a positive-energy Poincare representation with Lorentz-invariant joint translation spectrum has been reconstructed, the static exponent has the following lower-edge presentations in the cyclic neutral vacuum representation:

$$
\Gamma_*=c\sigma_*,
\qquad
\Delta_E\geq\hbar\Gamma_*,
\qquad
M_{\mathrm{gap}}\geq\frac{\hbar}{c}\sigma_*.
\tag{ARL22}
$$

These are comparison maps, not equations of concepts. The primitive theorem concerns the response exponent; \(\Gamma_*\), energy, and invariant mass are its recovered clock, action, and Poincare presentations.

The Higgs field belongs to a different slot. A Higgs vacuum value can be a local coordinate for a reduction to a stabilizer, but pure Yang--Mills has no Higgs field and still owes a neutral mass gap. [[higgs-reduction-as-local-shadow/inq|The Higgs reduction note]] therefore treats the scalar as a possible local shadow of whole-to-local pointing, not as the complete gap operator or the origin of scale.

Cosmology and the geon conjecture may enter upstream by selecting the state, cut metric, or physical section \(b_*\) through a whole-boundary, entropy, or leakage law. They do not replace [[witten-covariance-and-local-response|static response control]], [[positive-semigroup-decay/total-family-spectral-gap|the common-exponent bound on a total local family]], or [[conditional-correlation-tensorization/inq|complete conditional correlation control]]. The standard radiation-FLRW comparison that makes a Hubble harmonic far too soft is conditional on the recovered FLRW/QFT presentation; a deeper global--local map may evade that typing only by constructing a new dimensionless relation rather than equating unlike local measurements.

The estimates must apply on the gauge-invariant neutral carrier actually reconstructed. A preferred channel, rates tending to zero across the total family, or a complete-angle claim inferred from ordinary pair covariance cannot establish the stated floor. Cosmological, Higgs, or measured glueball scales cannot be used to fit the scale this construction claims to derive.
