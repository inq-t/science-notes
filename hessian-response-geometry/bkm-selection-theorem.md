# The Qualified BKM Selection Theorem

Bogoliubov--Kubo--Mori geometry is selected, up to an overall constant, by a precise conjunction on the full finite-dimensional faithful-state manifold: quantum monotonicity and mutual duality of the specific mixture and exponential connections. The weaker slogan “dually flat plus monotone implies BKM” suppresses the carrier and the connections that do the selecting and is not a valid theorem for an arbitrary CRF submanifold.

## The finite faithful-state manifold

Fix \(n<\infty\) and let

$$
\mathcal M_n
:=
\left\{
\rho\in M_n(\mathbb C):
\rho>0,
\ \operatorname{Tr}\rho=1
\right\}.
$$

For a faithful \(\rho\), define the Kubo--Mori operator

$$
\Omega_\rho(A)
:=
\int_0^1\rho^sA\rho^{1-s}\,\mathrm ds.
$$

On self-adjoint trace-zero density tangents \(X,Y\), the BKM metric is

$$
\boxed{
g^{\mathrm{BKM}}_\rho(X,Y)
=
\operatorname{Tr}
\left[X\,\Omega_\rho^{-1}(Y)\right].}
$$

Equivalently, for centered exponential scores \(A,B\),

$$
g^{\mathrm{BKM}}_\rho(A,B)
=
\int_0^1
\operatorname{Tr}
\left(
\rho^sA\rho^{1-s}B
\right)\,\mathrm ds.
$$

When all relevant operators commute, this reduces to ordinary covariance and hence to classical Fisher information.

## The two particular connections

The mixture or \((-1)\) connection is affine in density coordinates. The exponential or \((+1)\) connection is affine in normalized logarithmic coordinates. Their mutual duality with respect to \(g\) means

$$
Xg(Y,Z)
=g(\nabla_X^{(-1)}Y,Z)
+g(Y,\nabla_X^{(+1)}Z).
$$

This is not a claim that some unspecified pair of flat connections is dual. The quantum mixture and exponential structures are fixed before the metric is selected.

## Grasselli--Streater

Grasselli and Streater prove:

> On the finite-dimensional faithful-state manifold, if the \((+1)\) and \((-1)\) affine connections are dual with respect to a monotone Riemannian metric \(g\), then \(g\) is a scalar multiple of the BKM metric.

Here monotonicity means contraction under the relevant completely positive trace-preserving stochastic maps. Petz's classification supplies the family of quantum monotone metrics; the e/m-duality requirement singles out BKM from that family.

The sound implication is therefore

$$
\boxed{
\begin{gathered}
\text{full finite faithful-state manifold}\\
+\ \text{CPTP monotonicity}\\
+\ \text{duality of the specified e/m connections}
\end{gathered}
\Longrightarrow
g=c\,g_{\mathrm{BKM}},
\quad c>0.}
$$

This is **[EXACT -- FINITE DIMENSIONS]**.

## What the theorem does not say

It does not state

$$
\text{one convex potential}
\Longrightarrow
g_{\mathrm{BKM}},
$$

because any strictly convex potential has a Hessian metric. It also does not state the conclusion for:

- an arbitrary dually-flat manifold;
- a selected low-dimensional submanifold of \(\mathcal M_n\);
- a quotient with a nontrivial response radical;
- a family whose algebra or carrier changes with scale;
- nonfaithful boundary states; or
- a type-III local QFT algebra without a proved finite second variation.

A pullback \(\Phi^*g_{\mathrm{BKM}}\) along a CRF state map is certainly BKM-derived. But its uniqueness as the only admissible metric on the parameter space does not follow unless the relevant monotonicity and duality structures themselves descend and are sufficiently rich.

## Consequence for the CRF

[[program-core/common-response-form|The common response construction]] currently chooses a BKM pullback because relative-entropy response and data processing are desired. Grasselli--Streater can strengthen that choice only by applying the theorem on its actual carrier:

1. construct the metric on the full finite faithful-state manifold \(\mathcal M_n\);
2. prove monotonicity for the source theorem's stochastic-map class;
3. construct the standard mixture and exponential connections and prove their mutual duality;
4. conclude \(g=c\,g_{\mathrm{BKM}}\) on \(\mathcal M_n\); and
5. only then pull the selected metric back along the CRF state/readout map.

Constructing dual connections only on the CRF physical tangent and proving contraction only for the programme's chosen channels does not satisfy the cited theorem. That narrower route would require a new restricted uniqueness theorem.

The theorem selects the shape of the metric only up to \(c\). Applied independently to central sectors, it can also leave sector-dependent constants \(c_\alpha\). Neither it nor the pullback determines a common cross-sector normalization, areal normalization, Newton constant, spatial Fourier dimension, or extensive multiplicity. Those remain independent welds.

## Primary sources

- M. R. Grasselli and R. F. Streater, [[library/uniqueness-of-chentsov-metric-quantum-information-geometry/entry|*On the Uniqueness of the Chentsov Metric in Quantum Information Geometry*]], *Infinite Dimensional Analysis, Quantum Probability and Related Topics* 4 (2001), 173--182. The relevant statement is Theorem 18 in the current arXiv version.
- D. Petz, [[library/monotone-metrics-on-matrix-spaces/entry|*Monotone Metrics on Matrix Spaces*]], *Linear Algebra and its Applications* 244 (1996), 81--96. This classifies finite quantum monotone metrics by operator-monotone functions.
- H. Mori, [[library/transport-collective-motion-and-brownian-motion/entry|*Transport, Collective Motion, and Brownian Motion*]], *Progress of Theoretical Physics* 33 (1965), 423--455. This is a primary source for the canonical-correlation/linear-response structure from which the modern BKM name descends; it is not the uniqueness theorem.
