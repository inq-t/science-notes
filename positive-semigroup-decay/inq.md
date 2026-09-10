---
inq.module: positive-semigroup-decay
inq.include:
  - './'
keywords: [spectral support, positive semigroup, correlation decay, total family, energy gap, reconstruction]
---
# Positive Semigroup Decay

For a nonnegative self-adjoint generator, a common exponential bound on positive diagonal correlations of a Hilbert-total family excludes all lower positive spectrum. Each test vector may have its own prefactor and starting time. The theorem is a statement about one specified Hilbert space and generator; Euclidean field theory must separately construct that carrier and identify its correlations before the bound can become an energy or mass statement.

[[positive-semigroup-decay/total-family-spectral-gap|The total-family spectral-gap theorem]] uses positivity of the scalar spectral measure. Any nonzero spectral weight below the proposed edge would decay too slowly. Once that low spectral projection annihilates a total family, it vanishes on the whole vacuum complement. The conclusion supplies a uniform semigroup norm bound even though the input prefactors were not uniform over vectors.

Totality and a common exponent do different work. One observed channel can miss soft states; a total family with exponents tending to zero can still have no gap. [[distinction-grain-spectrum/inq#Every distinction may have a grain while the theory is gapless|The distinction-grain counterexample]] exhibits the latter failure. No operator-domain or form-domain core is required for the bounded correlations used here.

[[positive-semigroup-decay/source-pairing-limit-and-the-mass-gap|The source-pairing limit theorem]] carries a uniform fixed-time inequality through converging reflected source evaluations. In this route all finite linear combinations must satisfy the inequality, but the repair operators that establish it need not themselves converge. With full reconstruction and dense source coverage, the limiting inequality gives the physical gap and excludes additional zero-energy vectors.

[[positive-semigroup-decay/physical-reconstruction-and-units|Physical reconstruction and units]] states the additional contract: a full OS reconstruction, a total family in the intended ground-state complement, decay in the reconstructed translation direction, and a fixed physical length normalization. Lorentz-covariant joint translation spectrum is the further input needed to interpret the energy floor as invariant mass. A static correlation estimate or reflection positivity alone does not construct these objects.
