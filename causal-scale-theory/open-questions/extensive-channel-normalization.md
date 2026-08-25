# Open Question: Is the Extensive Channel Factor Constant?

The normalized binary model fixes a one-channel shape, not the cut-integrated response. The rigid CST-B2 member additionally assumes that the physical tangent normalization, renormalized multiplicity, and active channel content combine into a scale-independent extensive factor \(C_\perp(N)=C_{\perp,c}\). The wider [[causal-scale-theory/response-family-interface|response-family interface]] permits a member-dependent factor \(C_{\mathcal M}(N)\).

The typed factorization is

$$
G^{\perp}_{NN}(N)
=C_\perp(N)
\left(\frac{\mathrm d\theta}{\mathrm dN}\right)^2
g^{\mathrm{bin}}_{\theta\theta}.
$$

Under affine soldering and the balanced binary reduction this becomes the CST-B2 formula recorded in [[program-core/ruble-equations|RE5 of the Ruble equations]]. The factor \(C_\perp\) need not be an integer: it may include channel multiplicity, trace or regulator normalization, the size of the selected cut, and norm contributed by degrees of freedom discarded by the binary reduction.

The open construction must separate those effects and determine whether \(C_\perp(N)\) is constant in the physical comparison scheme. [[program-core/descent-response-geometry|Descent-response geometry]] states the stronger local requirement: construct a measure-valued BKM form and compare it with independently normalized area. [[deriving-value-of-g/obstructions-to-an-unconditional-proof|The replication and dimensional obstructions]] show why the normalized binary algebra cannot settle this question.

Algebraic geometry and correspondence theory close only a typed subproblem. If the active channels form a locally free sheaf or local system over the scale base and transport preserves its trace pairing, its rank is locally constant. For dualizable factor correspondences, categorical dimension is multiplicative under fusion and its logarithm is additive; with centers, the dimension matrix or full correspondence must be retained, and scalar composition needs the relevant Markov matching. These results can control channel multiplicity. They do not control regulator normalization, horizontal tangent norm, selected cut size, edge-state data, or discarded modes. Thus locally constant rank does not prove

$$
C_\perp(N)=C_{\perp,c}.
$$

The conditional rank-three cover in [[algebra/a2-inverse-cover|the \(A_2\) model]] supplies no identification with this wall carrier.

If

$$
\gamma(N)
:=\frac{C_\perp(N)}{C_{\perp,c}}
$$

is nonconstant, the constitutive source acquires that factor and [[causal-scale-theory/theorems/rigid-sech-response-identities|the CST-B2 rigid density identities]] no longer apply in their stated form. That outcome would replace the rigid CST-B2 profile with another response-family member without changing the exact one-channel balanced-binary geometry.
