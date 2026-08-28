# The Horizon-Thermodynamic Route

Local horizon thermodynamics gives a controlled conditional derivation of the Einstein coupling from a universal entropy--area density. It establishes the downstream implication \(\eta_{\mathrm E}\mapsto G\); it does not calculate \(\eta_{\mathrm E}\) and therefore does not by itself predict the value of \(G\).

## Premises

The Jacobson construction requires, in a sufficiently small neighborhood of every spacetime point:

1. a local Rindler horizon through the point for each null direction;
2. an equilibrium cross-section whose null expansion and shear vanish at the base point;
3. an approximate boost generator and its Unruh temperature;
4. a local equilibrium entropy variation extensive in horizon area;
5. the Clausius relation \(\delta Q=T\,\delta S\);
6. leading-order null focusing from the Raychaudhuri equation; and
7. local stress conservation.

Write the entropy premise as

$$
\delta\!\left(\frac{S_{\mathrm{hor}}}{k_B}\right)
=\eta_{\mathrm E}\,\delta A,
$$

where \(\eta_{\mathrm E}\) is finite, positive, and spacetime-constant throughout the Einstein regime under consideration. For an observer with proper acceleration \(a\), the Unruh normalization is

$$
k_BT_U=\frac{\hbar a}{2\pi c}.
$$

The heat flux is the boost-energy flux of \(T_{ab}\) through the local horizon. Raychaudhuri focusing relates the same null integral to \(R_{ab}\) and the area change. With energy-normalized \(T_{ab}\) and explicit \(c\), the Clausius equality for every null vector \(k^a\) gives

$$
R_{ab}k^ak^b
=\frac{2\pi}{\hbar c\eta_{\mathrm E}}
T_{ab}k^ak^b.
$$

Because this holds for every null direction, the two symmetric tensors can differ only by a metric-proportional term:

$$
R_{ab}
-\frac{2\pi}{\hbar c\eta_{\mathrm E}}T_{ab}
=f g_{ab}.
$$

Stress conservation and the contracted Bianchi identity determine the scalar part up to a cosmological integration constant. The result is

$$
G_{ab}+\Lambda g_{ab}
=\frac{2\pi}{\hbar c\eta_{\mathrm E}}T_{ab}.
$$

Comparison with the Einstein equation

$$
G_{ab}+\Lambda g_{ab}
=\frac{8\pi G}{c^4}T_{ab}
$$

yields

$$
\boxed{G=\frac{c^3}{4\hbar\eta_{\mathrm E}}.}
$$

The original source is Ted Jacobson's [[library/thermodynamics-of-spacetime-the-einstein-equation-of-state/inq|“Thermodynamics of Spacetime: The Einstein Equation of State”]]. His later [[library/entanglement-equilibrium-and-the-einstein-equation/inq|entanglement-equilibrium argument]] supplies a related route under a finite universal vacuum-entanglement density hypothesis.

## What the route derives

The argument explains why the same coefficient appears in three registers:

$$
\text{entropy per causal area}
\longleftrightarrow
\text{null focusing per energy flux}
\longleftrightarrow
\text{Einstein curvature per stress}.
$$

It also explains why the cosmological term is not fixed by the local null calculation: metric-proportional terms vanish on contraction with \(k^ak^b\). This is compatible with the local/scalar split in [[conformal-scale-geometry/scale-tractor-transport|the scale-tractor equation]], but it does not solve the global cosmological-constant problem.

## What the route assumes

The area coefficient is an input. Substituting

$$
\eta_{\mathrm E}=\frac{c^3}{4\hbar G}
$$

from the known Bekenstein--Hawking law and then recovering Einstein's equation is a consistency derivation, not a numerical calculation of \(G\).

The local equilibrium and area-extensivity hypotheses also delimit the result. If the entropy functional depends on curvature, additional entropy-production or higher-curvature terms are generally required. If the coefficient varies with state or position, the resulting response is not ordinary Einstein gravity with constant \(G\). The derivation does not establish that an arbitrary BKM metric, entanglement divergence, or cosmological-wall capacity supplies the needed finite coefficient.

## The exact role in the causal-scale programme

Suppose a causal-scale construction independently returns an areal BKM modulus \(\chi_{\downarrow}\) and proves

$$
\chi_{\downarrow}=\eta_{\mathrm E}.
$$

Then the horizon-thermodynamic argument turns that result into

$$
G=\frac{c^3}{4\hbar\chi_{\downarrow}}.
$$

This downstream step is therefore not the weak point. The weak point is the upstream [[causal-scale-derivation-target|construction and universality proof]] that would license the equality.

## Claim status

| Component | Status |
|---|---|
| Unruh temperature and leading null focusing | Established in their stated local regimes |
| Einstein equation from universal area entropy plus local Clausius equilibrium | Conditional thermodynamic derivation |
| Numerical value of the entropy--area coefficient | Assumed, not produced by the derivation |
| Equality of that coefficient with Causal Scale Dynamics' horizontal BKM density | Open conjectural weld |
| Cosmological constant and radiative stability | Not fixed by the local null argument |
