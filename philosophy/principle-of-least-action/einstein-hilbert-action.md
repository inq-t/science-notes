# Einstein--Hilbert Action

The Einstein--Hilbert action is the stationary-action formulation of general relativity. Instead of varying a particle trajectory in a fixed arena, it varies the spacetime metric $g_{\mu\nu}$ itself. Stationarity of the gravitational action plus the matter action yields Einstein's field equation.

## The action

In units with $c=1$, the bulk action in four spacetime dimensions is

$$
S[g,\psi]
=\frac{1}{16\pi G}
\int_\mathcal M
(R-2\Lambda)\sqrt{-g}\,\mathrm d^4x
+S_{\mathrm m}[g,\psi]
+S_{\mathrm{boundary}}.
$$

Here

- $R$ is the Ricci scalar of $g_{\mu\nu}$,
- $g$ is the determinant of the metric,
- $G$ is Newton's constant,
- $\Lambda$ is the cosmological constant,
- $\psi$ denotes the matter fields, and
- $S_{\mathrm{boundary}}$ is chosen to match the boundary data and make the variational problem well posed.

Sign conventions for curvature and the metric vary between authors. The internally consistent combination of action, stress-tensor definition, and field equation is what matters.

## Metric variation

Define the stress--energy tensor by

$$
T_{\mu\nu}
:=-\frac{2}{\sqrt{-g}}
\frac{\delta S_{\mathrm m}}{\delta g^{\mu\nu}}.
$$

After treating the boundary variation correctly, the metric variation has the bulk form

$$
\delta S
=\frac{1}{16\pi G}
\int_\mathcal M
\sqrt{-g}\,
\left(
G_{\mu\nu}+\Lambda g_{\mu\nu}
-8\pi G T_{\mu\nu}
\right)
\delta g^{\mu\nu}\,\mathrm d^4x.
$$

Requiring stationarity for arbitrary interior metric variations gives

$$
G_{\mu\nu}+\Lambda g_{\mu\nu}
=8\pi G T_{\mu\nu}.
$$

Varying the matter fields independently gives their equations of motion on the same dynamical spacetime.

## Why the boundary term matters

The Ricci scalar contains second derivatives of the metric. Their variation produces a total divergence, so the bulk Einstein--Hilbert integral alone is generally not stationary merely because the induced metric is fixed at a non-null boundary.

For a non-null boundary with Dirichlet metric data, the standard completion is the Gibbons--Hawking--York term,

$$
S_{\mathrm{GHY}}
=\frac{\varepsilon}{8\pi G}
\int_{\partial\mathcal M}
K\sqrt{|h|}\,\mathrm d^3x,
$$

where $h$ is the determinant of the induced metric, $K$ is the trace of the extrinsic curvature, and $\varepsilon$ depends on whether the boundary is timelike or spacelike and on convention. Null boundaries, corners, asymptotic regions, and alternative boundary data require their own careful terms.

Boundary terms can also determine conserved charges and the on-shell value used in semiclassical gravity. They are part of the physical variational problem, not disposable decoration.

## Diffeomorphism invariance

The action is built from spacetime scalars and is invariant under diffeomorphisms. This symmetry has several consequences:

- Coordinates label events but are not themselves observables.
- Some components of the metric equations are constraints rather than independent evolution equations.
- The contracted Bianchi identity,

$$
\nabla^\mu G_{\mu\nu}=0,
$$

is the Noether identity associated with diffeomorphism invariance.
- With the matter equations satisfied, it implies covariant stress--energy conservation,

$$
\nabla^\mu T_{\mu\nu}=0.
$$

Gauge-related metric variations correspond to the same physical geometry. This makes the gravitational action degenerate along diffeomorphism directions until a gauge or quotient description is chosen.

## Why this action is distinguished

In four dimensions, under the assumptions of locality, diffeomorphism invariance, a metric as the gravitational field, and field equations containing no more than second derivatives, the cosmological and Einstein--Hilbert terms provide the non-topological pure-metric dynamics. This is the four-dimensional content associated with Lovelock's result.

The statement depends on its assumptions. Additional fields, extra dimensions, nonlocality, or higher derivatives allow alternatives such as scalar--tensor theories, $f(R)$ gravity, and higher-curvature actions. These modify the dynamical content; they are not merely different notations for the Einstein--Hilbert action.

## Stationary, not a global minimum

Lorentzian gravitational action is normally treated through stationary phase, so no global-minimum interpretation is required. Even after continuation to Euclidean signature, the Einstein--Hilbert action has a conformal-factor problem: certain conformal metric variations can drive it without a lower bound. “Spacetime minimizes curvature” is therefore not a correct summary of general relativity.

The reliable statement is narrower and stronger: with specified matter, boundary terms, and boundary data, stationary metrics satisfy Einstein's equation.

## Related formulations

- **Palatini variation:** connection and metric or tetrad are varied independently. For the standard Einstein--Hilbert matter coupling, suitable assumptions recover the Levi--Civita connection, but more general actions or matter couplings can differ.
- **Tetrad and spin-connection actions:** these are natural when coupling fermions and clarifying local Lorentz symmetry.
- **ADM action:** spacetime is decomposed into spatial geometry plus lapse and shift, exposing Hamiltonian and momentum constraints.
- **Semiclassical effective action:** the [[quantum-action|quantum effective action]] includes corrections from quantum fields or metric fluctuations; its stationarity yields quantum-corrected equations rather than the bare Einstein equation.
- **Scale-tractor rewriting:** [[conformal-scale-geometry/scale-tractor-transport|the scale-tractor equation]] rewrites the trace-free Einstein equation in conformal-scale language. Rewriting field equations is distinct from supplying a complete action with matter, trace, and boundary sectors.
