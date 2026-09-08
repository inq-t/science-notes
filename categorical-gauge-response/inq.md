---
inq.module: "categorical-gauge-response"
inq.include:
  - "**/*.md"
inq.ambient:
  - "**/*.py"
  - "**/*.txt"
keywords:
  - categorical rigidity
  - property T
  - quantum G2
  - fusion algebra
  - neutral observables
---
# Categorical Rigidity on a Gauge Carrier

Categorical rigidity can provide a response bound uniform over an admissible class of representations. To make that bound relevant to Yang–Mills, the categorical action must be realized on the complete physical neutral carrier, fix only the vacuum, and compare with its physical energy. The mathematical opportunity is to obtain rigidity from composition laws; the unresolved step is constructing that particular action and comparison, not identifying a positive categorical number.

[[categorical-gauge-response/global-discreteness-kazhdan-rigidity-and-the-gap|Discreteness and Kazhdan rigidity]] distinguish three claims: removal of a kernel, a positive bound in one representation, and a bound uniform over all relevant representations. They are not equivalent. The triangle group $C_3*C_4$ supplies an explicit warning: finite-order generators and nontrivial descent can coexist with almost-invariant vectors. The fixed character family in [[triangle-descent-response/inq|triangle descent response]] therefore does not establish a representation-uniform inequality.

[[categorical-gauge-response/quantum-g2-categorical-rigidity-and-the-carrier-firewall|Quantum $G_2$ categorical rigidity]] instead uses property (T) of the stated rigid $C^*$-tensor category at a fixed real deformation $q>0$, $q\ne1$. A normalized fusion average has a uniform positive defect away from its invariant vectors in admissible representations. Statistical dimension, index, and a positivity certificate used in the property-(T) proof are distinct from that defect bound. The classical $q=1$ limit, and the dependence on the selected generating average, prevent a dimension count from being substituted for the spectral estimate. The separate proposal to select $q$ by a whole-to-local balance remains conditional; it is not supplied by categorical rigidity itself.

## Realizing the action is the substantive step

[[categorical-gauge-response/categorical-action-on-the-neutral-wilson-carrier|An action on the neutral Wilson carrier]] formulates the missing construction through state-preserving completely positive maps, an admissible fusion representation on the associated Hilbert space, and a vacuum-only joint fixed space. Its response must detect neutral field distinctions, not only charged sector labels. Two concrete failures make this requirement testable: a character normalization can produce only a removable scalar energy offset, while a canonical averaging action can leave an entire nontrivial observable subalgebra fixed.

[[categorical-gauge-response/kazhdan-markov-process-carrier|The Kazhdan–Markov construction]] provides a conditional benchmark. Given a suitable state-preserving, vacuum-ergodic group action, its averaging defect and Poissonized process act on the same state carrier and inherit the Kazhdan bound. This ordinary group construction is not automatically a realization of the quantum-$G_2$ category. In either case, categorical rigidity supplies no physical unit of time and no comparison with the Yang–Mills Hamiltonian until those maps have been constructed.

A successful extension must therefore produce a non-scalar response on the full neutral vacuum complement and prove its physical-energy comparison along compatible regulators. [[global-local-response-reconstruction/inq|Global–local response reconstruction]] owns that downstream comparison problem. The result sought here is its categorical input; neither a supplied action nor a fixed-$q$ bound alone meets [[contemporary-puzzles/yang-mills-mass-gap/clay-contract-and-scale-assumptions|the Yang–Mills existence and mass-gap contract]].
