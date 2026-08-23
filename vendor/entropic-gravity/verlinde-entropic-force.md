# Verlinde’s Entropic-Force Construction

Verlinde’s 2011 proposal treats space as emergent from holographic information and gravity as the macroscopic entropic response to relocating matter relative to information-bearing screens. Its equations exactly reproduce inertia, Newtonian gravity, Poisson’s equation, and static relativistic mass formulas once the entropy gradient, Unruh normalization, area bit density, and equipartition rules are supplied; the paper does not construct the microscopic screen theory that would necessitate those rules.

The primary source is [[vendor/entropic-gravity/sources/papers/1001.0785-verlinde-origin-gravity-laws-newton.pdf|Verlinde 2011]].

## Intended ontology

The proposed microscopic theory has energy, entropy, temperature, and time, but space in one holographic direction is emergent. Screens store information about the locations of matter and separate an already represented spatial region from a side which is not yet represented as space. The screen dynamics and its degrees of freedom are left unspecified.

The Newtonian potential and, in the static relativistic case, the redshift function serve as coarse-graining coordinates. Verlinde reverses the usual reading of the Unruh relation: screen temperature is treated as the temperature required for a body to have acceleration \(a\), rather than merely the temperature registered by an already accelerated detector.

## Particle-scale force

For a test body of mass \(m\) displaced normally toward a screen, postulate

$$
\Delta S
=2\pi k_B\frac{mc}{\hbar}\Delta x.
$$

The entropic virtual-work law is

$$
F\,\Delta x=T\,\Delta S.
$$

Assign the screen the Unruh-normalized temperature

$$
k_BT=\frac{\hbar a}{2\pi c}.
$$

Then

$$
F=ma.
$$

This is an exact cancellation among the three displayed premises. The factor \(2\pi\) in the entropy gradient is chosen to match the Unruh normalization; neither relation is calculated from screen microstates.

## Spherical screen and inverse-square gravity

Let a spherical screen of radius \(R\) have area \(A=4\pi R^2\). Assign it

$$
N=\frac{Ac^3}{G\hbar}
$$

degrees of freedom. The constant \(G\) enters through this normalization and is subsequently identified with Newton’s constant.

Assume equipartition and mass–energy equivalence:

$$
E=\frac12Nk_BT,
\qquad
E=Mc^2.
$$

Solving for \(T\) and inserting it into the entropic-force law gives

$$
F=\frac{GMm}{R^2}.
$$

The inverse-square dependence comes from the area growth of the spherical screen. Its coefficient comes from the assumed bit density, equipartition factor, and entropy-gradient normalization.

## General screens and Poisson’s equation

Let \(\mathcal S\) be an equipotential screen enclosing the mass density \(\rho\). Assign the local screen data

$$
dN=\frac{c^3}{G\hbar}\,dA,
\qquad
k_BT=\frac{\hbar}{2\pi c}
\nabla\Phi\cdot n,
$$

and use equipartition in integral form:

$$
Mc^2
=\frac12k_B\int_{\mathcal S}T\,dN.
$$

The result is Gauss’s law,

$$
M
=\frac{1}{4\pi G}
\int_{\mathcal S}\nabla\Phi\cdot d\mathbf A,
$$

and therefore

$$
\nabla^2\Phi=4\pi G\rho.
$$

This extends the screen representation beyond spherical symmetry. It also exposes its reconstructive character: the potential, its equipotential foliation, and its gradient are already used to define the thermodynamic screen data whose integral reproduces Poisson’s equation.

## Static relativistic construction

Now set \(c=k_B=1\). In a static spacetime with timelike Killing vector \(\xi^a\), define the redshift potential

$$
\phi=\frac12\ln(-\xi^a\xi_a),
$$

the static four-velocity

$$
u^a=e^{-\phi}\xi^a,
$$

and acceleration

$$
a^b=-\nabla^b\phi.
$$

For a constant-\(\phi\) screen with outward normal \(N^a\), assign the redshifted temperature

$$
T
=\frac{\hbar}{2\pi}
e^\phi N^b\nabla_b\phi
$$

and probe entropy gradient

$$
\nabla_aS
=-2\pi\frac{m}{\hbar}N_a.
$$

The entropic force measured relative to infinity is

$$
F_a=T\nabla_aS
=-me^\phi\nabla_a\phi.
$$

With

$$
dN=\frac{dA}{G\hbar},
\qquad
M=\frac12\int_{\mathcal S}T\,dN,
$$

one obtains

$$
M
=\frac{1}{4\pi G}
\int_{\mathcal S}
e^\phi\nabla\phi\cdot dA,
$$

which is the Komar mass for the static configuration.

Stokes’ theorem and the Killing identity give

$$
2\int_\Sigma
\left(
T_{ab}-\frac12Tg_{ab}
\right)n^a\xi^b\,dV
=
\frac{1}{4\pi G}
\int_\Sigma
R_{ab}n^a\xi^b\,dV.
$$

The left side is the standard Komar matter-volume expression. Its trace-reversed combination \(T_{ab}-\tfrac12Tg_{ab}\) is imported rather than derived from the screen thermodynamics; Verlinde remarks that the matter-side expression could “presumably” be fixed using conservation properties.

Verlinde then invokes arbitrary sufficiently small screens and local approximate timelike Killing fields, in analogy with Jacobson’s local construction, to infer the Einstein equation.

## What the construction establishes

Given its thermodynamic assignments, the construction consistently reproduces

- \(F=ma\);
- Newton’s inverse-square law;
- Gauss’s law and Poisson’s equation;
- the static holding force and Komar mass; and
- the Einstein tensor relation after the local-screen extension.

## What remains open

- the screen Hilbert space, state counting, and microscopic dynamics;
- a derivation of the probe entropy gradient away from a true horizon;
- why equipartition applies and on what relaxation scale;
- the status of non-horizon screens as physical thermodynamic systems;
- time-dependent or generic non-equilibrium spacetime;
- a screen-side derivation of the Komar trace-reversed matter source;
- force fluctuations and definite new observables; and
- an independent normalization of \(G\).

The source explicitly notes that away from true horizons the effective value of \(\hbar\), exact thermal equilibrium, and even the use of one screen are not settled. The most conservative classification is therefore a thermodynamic **reconstruction** of known gravitational laws with a proposed emergent interpretation, not a microscopic derivation from independently specified degrees of freedom.
