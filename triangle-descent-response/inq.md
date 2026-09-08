---
inq.module: "triangle-descent-response"
inq.include:
  - "**/*.md"
inq.ambient:
  - "**/*.py"
  - "**/*.txt"
keywords:
  - triangle group
  - descent
  - cusp coercivity
  - augmentation representation
  - neutral-sector coverage
---
# Triangle Descent and Spectral Response

The $(3,4,\infty)$ descent data admit an explicit unitary spectral model: nontrivial cusp characters remove the constant cusp channel and yield coercivity on a fixed hyperbolic orbifold. This makes a topological obstruction analytically testable. It also exposes the central limitation: a positive response on nontrivial character sectors does not automatically control the invariant, neutral sector needed for a Yang–Mills mass gap.

[[triangle-descent-response/s6-descent-defect-and-the-chirality-firewall|The descent-defect audit]] isolates the declared winding and lattice data from the stronger claims surrounding their [[algebra/s6-manuscript-branch|$S^6$ source construction]]. Its signed descent integer is not a mass, a chirality index, or a unit of action. In particular, the source's unipotent monodromy is not a positive-unitary representation. Passing to a unitary character is a new analytic realization of selected data, not an identification of the two carriers.

## A fixed geometric realization

[[triangle-descent-response/triangle-character-cusp-coercivity|The cusp construction]] uses the finite-area orbifold for $C_3*C_4$ and the twelve characters of its abelianization $C_{12}$. A character with nontrivial cusp phase shifts the Fourier modes away from zero. The resulting tail estimate, together with compactness on the core, gives compact resolvent and a strictly positive spectral bottom for each of the eleven nontrivial characters. A minimum over this finite family is positive at the fixed geometry. It is not a uniform theorem over changing geometries or arbitrary representations, and the sign of the descent integer is exchanged by complex conjugation without changing the spectrum.

[[triangle-descent-response/augmentation-descent-and-the-neutral-sector-firewall|Augmentation descent]] packages all eleven sectors without selecting one character. This makes the coverage boundary exact: the augmentation part may be coercive while an independent invariant part has arbitrary low spectrum. Neither projecting onto augmentation nor minimizing over augmentation lifts forces a positive response on an invariant input. Likewise, if one character sector is declared to be the entire physical theory, its lowest eigenvalue must be distinguished from the excitation gap above its own ground state.

## Changing the carrier does not finish the comparison

[[triangle-descent-response/triangle-presentation-descent-on-the-neutral-adjoint-carrier|The neutral adjoint construction]] tests a different realization: two finite-order actions on a matrix carrier have only scalars jointly fixed and can produce a positive response on traceless matrices. The response depends on their relative position and becomes soft in a limiting family. This is an explicit finite comparison model, not the neutral field carrier of Yang–Mills. [[categorical-gauge-response/global-discreteness-kazhdan-rigidity-and-the-gap|The failure of Kazhdan rigidity for the triangle group]] explains why finite-order presentation alone cannot make that bound uniform.

The remaining theorem must construct an analysis map from the complete physical vacuum complement into the descent response, prove that it is bounded below, and compare its response with physical energy under refinement. That is the interface with [[global-local-response-reconstruction/inq|global–local response reconstruction]]. The $A_2$ radial operator, its Weyl data, and the conditional three-sheeted inverse cover retain their separate [[algebra/a2-weyl-radial-operator|algebraic owner]]; their distinct carriers must not be identified merely because both constructions involve finite descent.
