# Compare BKM and Spatial Source Kernels by Sector

The first discriminating W2 calculation in each admitted sector is to compute the BKM response and the Euclidean or spatial source kernel for the same wall carrier, state, source direction, quotient, and renormalization prescription. Its purpose is to determine the state-dependent transform between those two responses. [[causal-wall-spectral-theory/conjectures/bkm-to-spatial-precision|The scalar]] and [[causal-wall-spectral-theory/conjectures/tt-bkm-to-spatial-precision|TT]] W2 conjectures own their independent carrier-changing constructions; this note owns only the sectorwise comparison experiment that can constrain or falsify one arrow at a time.

## Controlled comparison datum

Fix a sector \(s\in\{0,2\}\), with \(s=0\) scalar and \(s=2\) transverse-traceless, and then fix that sector's wall algebra and faithful state \((\mathcal A_s,\omega_s)\), physical source tangent \(X_s\), central-resolution policy, regulator, and subtraction scheme. Scalar and TT comparisons are separate calculations. Compute independently:

$$
G^{\mathrm{BKM},s}_{\omega_s}(X_s,X_s)
$$

from the faithful-state family, and a Euclidean, spectral, or probability-source quadratic kernel

$$
\Pi^s_{\omega_s}(J_{X_s},J_{X_s})
$$

for the explicitly paired source \(J_{X_s}\). If \(X_s\) and \(J_{X_s}\) live on different carriers, the source-pairing map and its measure conversion are part of the datum. Comparing kernels that use different states, source normalizations, physical quotients, counterterm schemes, or spin sectors would not test one W2 transform.

An algebraic exponential perturbation using faithful normal states and Araki relative Hamiltonians is one candidate starting point. A finite or lattice model can debug the transform but cannot by itself establish a type-III continuum return.

## Possible returns

The calculation should distinguish at least three outcomes:

1. a positive scalar multiplier on the tested sector;
2. a nontrivial modular-frequency or source kernel \(\mathcal M_\omega\) such that
   $$
   \Pi^s_{\omega_s}
   =\mathcal M^s_{\omega_s}[G^{\mathrm{BKM},s}_{\omega_s}];
   $$
3. no positive, covariant transform on the proposed physical image.

Local contact terms must be reported separately rather than absorbed into the multiplier. A noninjective transform is not automatically a failure, but its kernel and effective image must be included in the physical quotient before a nondegenerate spatial precision is claimed.

## Optional holographic specialization

If the Euclidean kernel is a three-dimensional stress response, [[causal-wall-spectral-theory/holographic-spectral-adapter|the optional holographic adapter]] owns the operator identification, state, regulator, branch, simultaneous continuation, and contact qualifications. The vendored spectrum dictionary begins only after that eligibility has been established. Neither the comparison nor the adapter constructs the W3 Lorentzian field map.

## Completion and failure

One sector's calculation is complete when both kernels and their pairing are obtained independently of the desired primordial spectrum, with spin domain, carriers, measures, signs, contacts, and normalization recorded. It falsifies that sector's tested transform if the paired source does not exist, the relation is state- or frequency-dependent contrary to a claimed scalar-multiplier law, or no positive map survives on the declared physical image. Failure rejects that proposed sectoral W2 factorization, not the generic BKM theorem, the other spin sector, another W2 construction, or either W3 realization.
