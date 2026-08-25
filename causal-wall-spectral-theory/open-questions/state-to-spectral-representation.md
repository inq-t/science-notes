# Compare BKM and Spatial Source Kernels

The first discriminating W2 calculation is to compute the BKM response and the Euclidean or spatial source kernel for the same wall carrier, state, source direction, quotient, and renormalization prescription. Its purpose is to determine the state-dependent transform between those two responses. [[causal-wall-spectral-theory/conjectures/state-response-is-spatial-precision|The scalar W2 conjecture]] owns the full carrier-changing construction; this note owns only the comparison experiment that can constrain or falsify one of its arrows.

## Controlled comparison datum

Fix a wall algebra and faithful state \((\mathcal A,\omega)\), a physical source tangent \(X\), its central-resolution policy, and one regulator and subtraction scheme. Compute independently:

$$
G^{\mathrm{BKM}}_\omega(X,X)
$$

from the faithful-state family, and a Euclidean, spectral, or probability-source quadratic kernel

$$
\Pi_\omega(J_X,J_X)
$$

for the explicitly paired source \(J_X\). If \(X\) and \(J_X\) live on different carriers, the source-pairing map and its measure conversion are part of the datum. Comparing kernels that use different states, source normalizations, physical quotients, or counterterm schemes would not test a W2 transform.

An algebraic exponential perturbation using faithful normal states and Araki relative Hamiltonians is one candidate starting point. A finite or lattice model can debug the transform but cannot by itself establish a type-III continuum return.

## Possible returns

The calculation should distinguish at least three outcomes:

1. a positive scalar multiplier on the tested sector;
2. a nontrivial modular-frequency or source kernel \(\mathcal M_\omega\) such that
   $$
   \Pi_\omega
   =\mathcal M_\omega[G^{\mathrm{BKM}}_\omega];
   $$
3. no positive, covariant transform on the proposed physical image.

Local contact terms must be reported separately rather than absorbed into the multiplier. A noninjective transform is not automatically a failure, but its kernel and effective image must be included in the physical quotient before a nondegenerate spatial precision is claimed.

## Optional holographic specialization

If the Euclidean kernel is a three-dimensional stress response, [[causal-wall-spectral-theory/spectral-realization|the optional holographic adapter]] owns the operator identification, state, regulator, branch, simultaneous continuation, and contact qualifications. The vendored spectrum dictionary begins only after that eligibility has been established. Neither the comparison nor the adapter constructs the W3 Lorentzian field map.

## Completion and failure

This calculation is complete when both kernels and their pairing are obtained independently of the desired primordial spectrum, with domains, measures, signs, contacts, and normalization recorded. It falsifies the tested transform if the paired source does not exist, the relation is state- or frequency-dependent contrary to a claimed scalar law, or no positive map survives on the declared physical image. Failure of this experiment rejects that proposed W2 factorization, not the generic BKM theorem, another W2 construction, or either W3 realization.
