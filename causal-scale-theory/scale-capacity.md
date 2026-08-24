# Homogeneous Scale Capacity

The CST capacity parameter is the crossing value of a cut-integrated state-to-gravitational response ratio. It is coordinate invariant once the physical horizontal tangent is fixed, but it is neither the local areal modulus, a universal constant, nor a number supplied by normalized binary geometry alone.

[[program-core/descent-response-geometry|The programme core]] distinguishes the local areal descent modulus \(\chi_N(p)\), the local matching field \(\mathfrak r_{\Sigma,N}(p)\), and the integrated cut ratio

$$
\mathfrak R_\Sigma(N)
=\frac{\mu^{\mathrm{desc}}_{v_N,v_N}(\Sigma_N)}
{\mu^{S,\mathrm{grav}}(\Sigma_N)}.
$$

CST specializes this hierarchy at its distinguished homogeneous crossing:

$$
\boxed{
\mathfrak R_c:=\mathfrak R_{\Sigma_c}(N_c)
=\frac{k_B}{S_c}G^\perp_{NN}(N_c),}
\qquad
\frac{S_c}{k_B}
:=\mu^{S,\mathrm{grav}}(\Sigma_c).
$$

The entropy measure in the denominator must be normalized independently of the state response. Otherwise unity would be installed by definition rather than returned as a physical comparison.

## Binary shape and extensive norm

After [[wall-construction-interface/binary-channel|a balanced binary reduction]] and [[basic-concepts/soldering/affine-scale-state|affine soldering]] are granted,

$$
g^{\mathrm{bin}}_{\theta\theta}
=\operatorname{sech}^2\theta,
\qquad
\theta=\varrho_\perp x,
\qquad
\nu=|\varrho_\perp|.
$$

The physical full-cut norm may carry an extensive factor:

$$
G^\perp_{NN}(N)
=C_\perp(N)\nu^2
\operatorname{sech}^2(\nu x).
$$

The rigid CST branch adds the assumption \(C_\perp(N)=C_{\perp,c}\). The crossing definition then gives

$$
C_{\perp,c}
=\frac{S_c}{k_B}\frac{\mathfrak R_c}{\nu^2},
\qquad
\boxed{
G^\perp_{NN}(N)
=\frac{S_c}{k_B}\mathfrak R_c
\operatorname{sech}^2(\nu x).}
$$

Thus the normalized curve fixes shape, while \(\mathfrak R_c\) carries the integrated normalization. A microscopic calculation that returns a scale-dependent \(C_\perp\) would change the physical pulse without contradicting the binary Casimir identity.

## Coordinate invariance and physical content

For any regular reparameterization \(\widetilde\theta=f(\theta)\),

$$
G^\perp_{NN}
=G^\perp_{\theta\theta}
\left(\frac{\mathrm d\theta}{\mathrm dN}\right)^2
=G^\perp_{\widetilde\theta\widetilde\theta}
\left(\frac{\mathrm d\widetilde\theta}{\mathrm dN}\right)^2.
$$

Accordingly, \(\mathfrak R_c\) does not depend on the chosen state coordinate. The separate numerical meaning of \(\nu\) requires the canonical generator normalization \(Q^2=\mathbf1\); an arbitrary rescaling of \(Q\) would otherwise move width between the coordinate and the metric.

The weak unit principle proposes \(\mathfrak R_c=1\). It says that two independently normalized *integrated* quantities match at one cut. It does not assert the strong local law \(\mathfrak r_{\Sigma,N}(p)=1\), prove a universal area modulus, or derive Newton's constant. Those stronger possibilities belong to [[program-core/causal-capacity-equivalence|causal-capacity equivalence]] and [[deriving-value-of-g/entry|the gravitational-value programme]].

Only after the constitutive source, horizontal temperature, and Einstein-horizon conversion are added does \(\mathfrak R_c\) determine a cosmological density fraction. [[theorems/dimensional-crossing-partition|The dimensional crossing theorem]] owns that downstream result.
