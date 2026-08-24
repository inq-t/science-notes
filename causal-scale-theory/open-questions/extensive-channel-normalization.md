# Open Question: Is the Extensive Channel Factor Constant?

The normalized binary model fixes a one-channel shape, not the cut-integrated response. The rigid CST pulse additionally assumes that the physical tangent normalization, renormalized multiplicity, and active channel content combine into a scale-independent extensive factor \(C_\perp(N)=C_{\perp,c}\).

The typed factorization is

$$
G^{\perp}_{NN}(N)
=C_\perp(N)
\left(\frac{\mathrm d\theta}{\mathrm dN}\right)^2
g^{\mathrm{bin}}_{\theta\theta}.
$$

Under affine soldering and the balanced binary reduction this becomes the formula recorded in [[program-core/ruble-equations|RE5 of the Ruble equations]]. The factor \(C_\perp\) need not be an integer: it may include channel multiplicity, trace or regulator normalization, the size of the selected cut, and norm contributed by degrees of freedom discarded by the binary reduction.

The open construction must separate those effects and determine whether \(C_\perp(N)\) is constant in the physical comparison scheme. [[program-core/descent-response-geometry|Descent-response geometry]] states the stronger local requirement: construct a measure-valued BKM form and compare it with independently normalized area. [[deriving-value-of-g/obstructions-to-an-unconditional-proof|The replication and dimensional obstructions]] show why the normalized binary algebra cannot settle this question.

If

$$
\gamma(N)
:=\frac{C_\perp(N)}{C_{\perp,c}}
$$

is nonconstant, the constitutive source acquires that factor and [[causal-scale-theory/theorems/rigid-sech-response-identities|the rigid density identities]] no longer apply in their stated form. That outcome would modify the homogeneous CST model without changing the exact balanced-binary geometry.
