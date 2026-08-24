# Analytic Continuation and State Selection

The holographic dictionary depends on more than the substitution \(q\mapsto-iq\). It simultaneously continues bulk or QFT parameters, selects a branch mapping regular Euclidean interior data to the Bunch--Davies cosmological state, and relates a Euclidean generating functional to a Lorentzian wavefunctional; changing any of these inputs changes the purported cosmological observable.

## The operational pseudo-QFT

In the original construction, the QFT dual to the cosmology is defined operationally:

1. calculate in the ordinary Euclidean QFT dual to the corresponding domain wall;
2. analytically continue momentum and the parameters inherited from the bulk gravitational coupling; and
3. take the imaginary part or spectral discontinuity in the registered branch.

For large-\(N\) examples the continuation is conventionally written

$$
\boxed{
\bar q=-iq,
\qquad
\bar N^2=-N^2,}
$$

or \(\bar N=-iN\) after a branch has been chosen. The barred theory is the ordinary Euclidean domain-wall QFT; the unbarred object after continuation is often called the pseudo-QFT. Continuing \(N\), or equivalently the gravitational coupling, is not optional bookkeeping: it controls the overall sign needed for positive cosmological power.

[[causal-wall-spectral-theory/sources/papers/0907.5542-mcfadden-skenderis-holography-for-cosmology.pdf|McFadden and Skenderis]] give the operational construction, while [[causal-wall-spectral-theory/sources/papers/1104.3894-mcfadden-skenderis-cosmological-three-point-correlators.pdf|their three-point analysis]] carries the continuation through nonlinear response.

## Vacuum and regularity

The Euclidean domain wall is chosen so that regularity in its interior maps to positive-frequency behavior in the far past of the cosmology. In the controlled single-clock calculation this selects the Bunch--Davies state. A different cosmological initial state requires a different real-time or boundary-state prescription; it is not obtained by retaining the same Euclidean QFT calculation and changing only its interpretation.

Thus the state is part of the dictionary:

$$
\text{regular Euclidean interior}
\xleftrightarrow[\text{chosen branch}]{}
\text{Bunch--Davies cosmological mode}.
$$

If the cosmology lacks the required asymptotic region or the Euclidean problem lacks an admissible regular solution, the original state argument does not apply.

## Wavefunction versus expectation value

Analytic continuation is cleanest at the level of a wavefunctional. Cosmological expectation values are then computed with the appropriate Lorentzian state, schematically

$$
\langle F\rangle_{\mathrm{cos}}
=\int\mathcal D\phi\,
|\Psi_{\mathrm{cos}}[\phi]|^2F[\phi],
$$

whereas an AdS or domain-wall construction uses different gluing data. [[causal-wall-spectral-theory/sources/papers/1104.2621-harlow-stanford-operator-dictionaries-wave-functions.pdf|Harlow and Stanford]] emphasize that continuation of wavefunctions does not make all operator dictionaries or expectation values identical.

This blocks three shortcuts:

- reverse relative entropy is not automatically a complex-conjugate wavefunctional;
- a Euclidean connected correlator is not automatically a Lorentzian in-in correlator; and
- positivity of one continued quadratic kernel does not establish full reflection positivity, unitarity, or causal reconstruction.

## Branch and sign registration

One may express the same physical response through \(-\operatorname{Im}B_{\mathrm{cont}}(-ik)\) or through the imaginary part on a specified lip of the \(q^2\) cut. These forms agree only after the continuation of theory parameters and the orientation

$$
\operatorname{Disc}F(s)
:=F(s+i0)-F(s-i0)
$$

or its opposite have been stated. This module therefore uses the positive responses \(\rho_A^{\mathrm{cos}}\) and \(\rho_B^{\mathrm{cos}}\) defined in [[vendor/holographic-cosmology/scalar-and-tensor-spectra|the spectrum note]], rather than inferring a sign from \(\operatorname{Disc}\) alone.
