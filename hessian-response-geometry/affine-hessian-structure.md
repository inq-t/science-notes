# Affine Hessian Structure and the CRM Integrability Test

A positive response matrix is a Hessian metric only relative to a declared flat torsion-free connection. Locally, total symmetry of \(\nabla g\) is the integrability condition for one potential to generate the metric; globally, affine holonomy and the patching of local potentials remain additional obstructions.

## Definition

Let \(M\) be a smooth manifold, let \(\nabla\) be a flat torsion-free connection on \(TM\), and let \(g\) be a positive Riemannian metric. The triple \((M,\nabla,g)\) is Hessian if every point has a \(\nabla\)-affine chart in which

$$
g_{ij}=\partial_i\partial_j\Psi
$$

for a smooth strictly convex local potential \(\Psi\).

The connection is part of the object. Under a nonlinear change of coordinates, the matrix of ordinary second partial derivatives acquires non-tensorial terms. Writing

$$
g=\nabla\mathrm d\Psi
$$

makes the dependence explicit.

## The local Codazzi criterion

Define the cubic form

$$
C(X,Y,Z):=(\nabla_Xg)(Y,Z).
$$

For a Hessian metric this tensor is totally symmetric. Conversely, on a sufficiently small affine chart, flatness and torsion-freeness together with total symmetry of \(C\) allow two applications of the Poincare lemma and produce a local potential. In affine coordinates the condition is

$$
\partial_i g_{jk}
=\partial_j g_{ik}
=\partial_k g_{ij}.
$$

The result is **[EXACT LOCAL DIFFERENTIAL GEOMETRY]**. A single numerical equality of selected mixed derivatives does not prove it for all indices or throughout a neighborhood.

## Application to the common response form

Let \(\lambda^I=(N,\zeta^a,h^r)\) be affine response coordinates. If

$$
G_{IJ}=\partial_I\partial_J\Psi,
$$

then every third derivative is one component of the same cubic:

$$
\partial_NG_{ab}
=\partial_aG_{Nb}
=\partial_bG_{Na}.
$$

At a homogeneous symmetric reference, representation theory may force \(G_{Na}=0\). It does not force the derivatives above to vanish. Hence

$$
\mathcal C_{Nab}
=\partial_NG_{ab}
$$

can be the first witness that the homogeneous and observational blocks arise from one family.

This is stronger than matching their values. Given independently proposed functions \(G_{NN}(N)\) and \(G_{ab}(N,k)\), a common potential may fail to exist because their derivatives do not satisfy the required mixed relations after transport to one carrier.

## Dual connection and Legendre coordinates

The \(g\)-dual connection \(\nabla^*\) is defined by

$$
Xg(Y,Z)
=g(\nabla_XY,Z)+g(Y,\nabla_X^*Z).
$$

For a Hessian structure, \(\nabla^*\) is locally flat. If \(\theta^i\) are \(\nabla\)-affine coordinates and

$$
\eta_i:=\frac{\partial\Psi}{\partial\theta^i},
$$

then \(\eta_i\) are dual affine coordinates where the Legendre map is nondegenerate. The dual potential

$$
\Psi^*(\eta)
=\theta^i\eta_i-\Psi(\theta)
$$

satisfies

$$
\frac{\partial^2\Psi^*}{\partial\eta_i\partial\eta_j}
=(g^{-1})^{ij}.
$$

This is inverse metric geometry on the same finite response tangent. It does not construct the spatial mode carrier, Fourier measure, boundary conditions, or probability 1PI functional needed to call \(g^{-1}\) a cosmological covariance.

## Global obstructions

Local potentials may differ on overlaps by affine functions,

$$
\Psi_\alpha-\Psi_\beta
=a_i x^i+b,
$$

without changing the Hessian. A global scalar potential therefore requires the corresponding affine cocycle to be trivial. Further issues include:

- nontrivial affine holonomy;
- failure of one affine chart to cover the physical quotient;
- loss of strict convexity or rank at boundary states;
- topology preventing global dual coordinates;
- singular quotient strata; and
- scale-dependent carriers for which there is no one connection.

The CRM may therefore be locally Hessian while lacking one global log-partition function. Conversely, an arbitrary scalar functional written in coordinates does not define the intended intrinsic Hessian unless the connection and transformation law are declared.

## Statistical terminology boundary

In a regular statistical model, the Hessian cubic is often called the Amari--Chentsov tensor and its components encode third centered score moments in suitable classical exponential coordinates. A generic response potential need not have that probabilistic origin. The safe terminology is:

$$
\text{Hessian cubic }C=\nabla g
$$

until a statistical state family proves the stronger identification.

Likewise, equality of mixed third derivatives is an integrability condition, not a conservation law, equation of motion, or indication that response is transported unchanged through time.
