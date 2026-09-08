---
inq.module: logistic-scale-geometry
inq.include:
  - './'
inq.exclude:
  - 'junk-drawer/'
inq.ambient:
  - 'receipts/*.py'
  - 'receipts/*.txt'
  - 'junk-drawer/**'
keywords:
  - logarithmic scale
  - logistic measure
  - Witten-Darboux factorization
  - Fredholm index
  - core capacity
  - resolvent frame
  - spectral center
---
# Logistic Scale Geometry

A logistic profile can define a coercive probability geometry, carry an oriented Fredholm class, or resolve the spectrum of an already supplied positive operator. These are three different constructions on declared scale carriers. Their exact relations separate the shape and orientation of a scale wall from the location of a physical spectral threshold; no logistic shape constant alone proves a Yang--Mills mass gap.

## A pointed probability carrier has a sharp scale edge

The [[binary-information-geometry/witten-darboux|binary Witten--Darboux calculation]] supplies the shared factorization for the probability density

\[
q_{\nu,N_c}(N)=\frac{\nu}{2}\operatorname{sech}^2\!\bigl(\nu(N-N_c)\bigr),
\qquad \nu>0.
\]

[[logistic-scale-geometry/pointing-coercivity-and-the-flat-partner-law|Pointing coercivity]] places it on the commutative scale shadow of [[wall-construction-interface/core-spectral-wall|the core spectral wall]]. After declaring the normalized scale derivation, the gradient form on \(L^2(q\,\mathrm dN)\) has sharp Poincare edge \(\nu^2\). Multiplication by \(\sqrt q\) transports that form to the ordered factor

\[
A_\nu=\partial_N+\nu\tanh\!\bigl(\nu(N-N_c)\bigr),
\qquad
A_\nu A_\nu^*=-\partial_N^2+\nu^2.
\]

One normalizable ordered zero mode and a constant partner force the logistic family and positivity of its width, but leave the magnitude of \(\nu\) free. A normalizable pointing without the partner law need not have a gap. The [[wall-construction-interface/scale-character-solder|scale-character comparison]] separately distinguishes projection-coded matching, which selects \(\nu=1/2\), from normalized-involution matching, which selects \(\nu=1\). Its optional incoming-density law selects the former width only within the stated logistic family.

## Orientation and capacity-relative threshold are different invariants

[[logistic-scale-geometry/indexed-scale-wall-and-the-causal-grain|The indexed wall]] proves that \(A_\nu:H^1(\mathbb R)\to L^2(\mathbb R)\) is Fredholm of index \(+1\) for every \(\nu>0\). That integer records the ordered passage between its asymptotic ends. The positive spectral edge can still vary continuously as \(\nu^2\); stability of the index is not a regulator-uniform gap estimate.

Removing the canonical trace-growth factor \(e^N\) from the probability density and treating the resulting relative coefficient as a half-density on translation-Haar scale instead gives

\[
B_\nu=\partial_N+\frac12+\nu\tanh\!\bigl(\nu(N-N_c)\bigr).
\]

Its index is zero for \(2\nu<1\), undefined at the non-Fredholm threshold \(2\nu=1\), and \(+1\) for \(2\nu>1\). At the threshold, the original probability factor still has edge \(1/4\). This change depends on the carrier: using the trace-weighted carrier would give an operator unitarily equivalent to \(A_\nu\). A possible homotopy memory of a wall crossing must therefore retain both the operator and its Hilbert-space domain.

## Spectral resolution locates centers without creating a gap

For a supplied dimensionless nonnegative self-adjoint \(\widehat L\), [[logistic-scale-geometry/resolvent-logistic-scale-transform|the resolvent--logistic transform]] uses

\[
Q_N=(e^N\widehat L)^{1/2}(1+e^N\widehat L)^{-1},
\qquad
\int_{\mathbb R}\|Q_Nf\|^2\,\mathrm dN
=\|(1-P_0)f\|^2,
\]

where \(P_0\) projects onto \(\ker\widehat L\). The resulting complex-linear analysis map preserves phase and has exact coverage on the positive spectral carrier. Each scalar spectral channel has the same logistic width \(\nu=1/2\), with center \(N_c=-\log\lambda\). Positive eigenvalues approaching zero send these centers to \(+\infty\) while preserving the universal shape.

A positive lower spectral edge is therefore an upper bound on the center operator \(-\log\widehat L\). [[scale-incidence-response/inq|Scale incidence response]] asks how independently constructed filtrations or response forms could enforce such a bound. The transform itself does not choose \(\widehat L\), bound its centers, or identify its carrier with the physical vacuum complement. [[logistic-scale-geometry/scale-wall-to-casimir-comparison|The scale-wall-to-Casimir comparison]] gives the full conditional implication, including the boundary-to-scale carrier mismatch and continuum requirements.

The pointing and resolvent notes link their finite receipts and retained output where available. Those checks exercise profile, factorization, normalization and finite-frame identities; the Sobolev-domain proofs, physical carrier selection and continuum comparison remain mathematical or construction obligations in the notes. [[logistic-scale-geometry/research-history|The research history]] preserves the earlier combined exposition.
