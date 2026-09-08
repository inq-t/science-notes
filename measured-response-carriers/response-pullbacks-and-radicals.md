# Response Pullbacks and Radicals

Pulling a positive state metric back to parameter directions introduces precisely the directions invisible to the analysis map. Removing that radical is weaker than proving a uniform lower bound; finite observable response also requires derivatives to be continuous in the score norm.

## Parameter Hessians are pullbacks, not new carriers

Use the faithful state-tangent metric in
[[measured-response-carriers/state-tangent-bkm-bridge|the BKM state-tangent
construction]].

Let \(\lambda\mapsto\rho_\lambda\) be a regular faithful state family on one
fixed algebra, and let

\[
J_\lambda:T_\lambda M\longrightarrow
T_{\rho_\lambda}\mathcal S_{\mathrm{faithful}},
\qquad
J_\lambda v:=D\rho_\lambda(v).
\tag{MC20}
\]

The response metric on parameter space is the bilinear pullback

\[
G_\lambda(v,w)
:=
g_{\rho_\lambda}^{\mathrm{BKM}}
\!\left(J_\lambda v,J_\lambda w\right).
\tag{MC21}
\]

Equivalently, if \(g^\flat\) denotes the metric map from the target tangent
to its cotangent and \(J_\lambda^*\) is the algebraic dual map, then

\[
G_\lambda^\flat
=
J_\lambda^*g_{\rho_\lambda}^{\mathrm{BKM},\flat}J_\lambda.
\tag{MC21'}
\]

Because the target BKM metric is positive definite, the pullback radical is
exactly

\[
\boxed{
\operatorname{rad}G_\lambda
=
\ker J_\lambda.}
\tag{MC21a}
\]

More generally, for positive-definite target metrics \(g_\alpha\), analysis
maps \(J_\alpha\), and positive weights \(w_\alpha\), put

\[
Q[v]
:=
\sum_\alpha w_\alpha
g_\alpha(J_\alpha v,J_\alpha v)
\]

on the common domain where the sum is finite. Then

\[
\boxed{
\ker Q
=
\bigcap_\alpha\ker J_\alpha.}
\tag{MC21b}
\]

This is the pullback-frame theorem. Joint infinitesimal injectivity removes
the radical in finite dimensions; a uniform positive lower frame is the
stronger requirement in an infinite-dimensional physical tangent.
For inner-unitary state paths on one von Neumann algebra,
[[modular-cocycle-tomography/inq|modular cocycle tomography]] computes this
joint kernel exactly as an intersection of state centralizers and expresses
that intersection through Connes cocycles on one reference carrier.

There is an immediate finite-rank obstruction. If the physical vacuum
complement is infinite dimensional while
\(\bigoplus_\alpha\operatorname{Ran}J_\alpha\) is finite dimensional, then
\(\bigcap_\alpha\ker J_\alpha\neq\{0\}\). No finite family of
finite-dimensional response targets can therefore satisfy

\[
Q[v]\geq\kappa\|v\|_{\mathrm{phys}}^2
\qquad(\kappa>0)
\tag{MC21c}
\]

on the complete vacuum complement. A successful construction needs a joint
analysis map with a uniform closed-range bound. This could come from a finite
family of infinite-dimensional targets, an infinite or direct-integral
family, or a genuinely same-carrier operator with its own proved
vacuum-complement edge.

For a finite affine exponential family, \(G_\lambda\) is the Hessian of the
log-partition potential. Before reduction it can be only a positive
semidefinite premetric. On a constant-rank neighborhood with a smooth
quotient by the radical, a basic form descends to a positive metric.
Retaining an affine Hessian structure further requires the flat
torsion-free connection and local potential to descend, the latter modulo
affine functions along the fibers. The full mixed-derivative integrability
conditions belong to [[hessian-response-geometry/affine-hessian-structure|affine
Hessian structure]]. Metric descent and Hessian descent are therefore
different requirements.

The form \(G_\lambda\) canonically defines a map
\(T_\lambda M\to T_\lambda^*M\), not an endomorphism of
\(T_\lambda M\). Matrix eigenvalues require a separately chosen source norm
or Riesz identification and change when the parameter tangents are
renormalized. [[hessian-response-geometry/relative-response-spectrum|The
relative response spectrum]] makes this two-form comparison explicit.
Likewise, a real state-tangent form does not automatically
extend to a positive Hermitian form on a complex physical energy core.

Equation (MC21) acts on \(T_\lambda M\), not on
\(\mathcal H_\omega\). Fourier covariance inversion, spatial precision,
localized energy, and mass are later consumer maps. In particular, the
open W2 arrow in [[causal-wall-spectral-theory/inq]] is precisely a
carrier-changing map from such state response to a spatial
probability-precision operator.

## Fisher-invisible actions and finite observable response

Suppose a declared family of transformations \(T_\theta\) acts on a
probability space \((X,\mu)\), with differentiable pushed densities at
identity. Let \(S_v\in L^2(\mu)\) be the state score in parameter
direction \(v\), and \(V_vF(x)\) the pointwise derivative of an observable.
The score pullback metric is \(g(v,v)=\|S_v\|_2^2\).
These are two different analysis maps: \(S\) differentiates a state,
whereas \(v\mapsto V_vF(x)\) differentiates observable values.

Define the extended dual response by
\[
\Gamma(F)(x)=\inf\{C\ge0:\ |V_vF(x)|^2\le Cg(v,v)
\text{ for every }v\},\qquad \inf\varnothing=\infty .
\]
Then finite response requires \(V_vF(x)=0\) for every \(v\in\ker S\).
Otherwise a zero-score direction violates the displayed inequality for
every finite \(C\). An infinitesimal state-preserving action belongs
to this radical even if it moves individual points. In finite dimensions,
annihilating the radical suffices for a finite dual norm. In infinite
dimensions, continuity in the score norm is a further requirement;
annihilation alone does not supply it.

This is a general stabilizer-annihilation rule, not an identification
of a state symmetry with a physical gauge redundancy. Changing the
admissible transformation family changes the test. A weak, nondegenerate
score metric can also enforce invariance under limits of vanishing-cost
directions, as in
[[gauge-path-fisher-response/two-sided-fisher-completion-and-the-neutral-carrier|the
two-sided path-state construction]]. There the finite smooth cylinder
algebra, its \(L^2\) completion, and its closed response operator are
proved separately. None follows merely by writing an inverse of a
degenerate Fisher matrix.
