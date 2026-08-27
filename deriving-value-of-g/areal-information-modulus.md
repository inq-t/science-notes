# The Areal Information Modulus

Einstein gravity assigns a fixed amount of dimensionless horizon entropy to a unit of causal area. Its coefficient can be read as an areal information modulus, while its inverse is the geometric compliance carried by \(G\). These are exact translations of the Einstein area law; they become an explanation of \(G\) only if the modulus is obtained independently.

## Entropy per area

Write horizon entropy in natural-log units:

$$
\mathcal S_{\mathrm{hor}}
:=\frac{S_{\mathrm{hor}}}{k_B}.
$$

In the Einstein semiclassical regime,

$$
\mathcal S_{\mathrm{hor}}
=\frac{Ac^3}{4\hbar G}
=\frac{A}{4\ell_P^2},
\qquad
\ell_P^2:=\frac{\hbar G}{c^3}.
$$

Define

$$
\eta_{\mathrm E}
:=\frac{\mathrm d\mathcal S_{\mathrm{hor}}}{\mathrm dA}
=\frac{c^3}{4\hbar G}
=\frac{1}{4\ell_P^2}.
$$

The subscript \(\mathrm E\) matters: this is the coefficient of the Einstein area law, not a generic property of every entropy, state, or gravitational theory. If the physical entropy density is used instead, then

$$
\frac{\mathrm dS_{\mathrm{hor}}}{\mathrm dA}
=k_B\eta_{\mathrm E},
\qquad
G=\frac{k_Bc^3}
{4\hbar\,\mathrm dS_{\mathrm{hor}}/\mathrm dA}.
$$

Boltzmann's constant enters only when dimensionless natural-log information is expressed in thermodynamic entropy units.

## Modulus and compliance

The inverse coefficient is

$$
\mathfrak a_{\mathrm E}
:=\eta_{\mathrm E}^{-1}
=4\ell_P^2.
$$

It has units of area per unit natural-log entropy. The pair

$$
\eta_{\mathrm E}
\quad\text{and}\quad
\mathfrak a_{\mathrm E}
$$

can be read respectively as areal stiffness and areal compliance. Then

$$
G=\frac{c^3\mathfrak a_{\mathrm E}}{4\hbar}.
$$

This realizes one part of the [[cosmodynamics/soldering-constants|soldering interpretation]]:

$$
\begin{aligned}
c&:\ \text{time calibration}\longleftrightarrow\text{length calibration},\\
\hbar&:\ \text{dimensionless phase}\longleftrightarrow\text{action},\\
k_B&:\ \text{dimensionless information}\longleftrightarrow\text{entropy},\\
\mathfrak a_{\mathrm E}&:\ \text{dimensionless horizon information}\longleftrightarrow\text{causal area}.
\end{aligned}
$$

The area law does not imply a tessellation into literal cells of area \(4\ell_P^2\). It fixes a response coefficient. Discreteness would require an independent spectral statement.

## Curvature response

Einstein's equation can be written as

$$
G_{ab}+\Lambda g_{ab}
=\frac{8\pi G}{c^4}T_{ab}
=\frac{2\pi}{\hbar c\eta_{\mathrm E}}T_{ab}.
$$

The dimensions display the proposed interpretation:

$$
\left[\frac{T_{ab}}{\hbar c}\right]=L^{-4},
\qquad
[\eta_{\mathrm E}]=L^{-2},
\qquad
\left[\frac{T_{ab}}{\hbar c\eta_{\mathrm E}}\right]=L^{-2}.
$$

Stress measured in quantum action--length units becomes curvature after division by the areal modulus. Large \(\eta_{\mathrm E}\) means that the same stress produces little curvature.

In the [[conformal-scale-geometry/scale-tractor-transport|scale-tractor rewriting]], the trace-free equation becomes

$$
\mathcal E_{ab}(\sigma)
=\frac{\pi}{\hbar c\eta_{\mathrm E}}
\,\sigma T^\circ_{ab}.
$$

This is an exact change of coefficient once Einstein gravity is assumed. It does not derive the modulus from tractor geometry.

## Action stiffness

With coordinates and volume conventions in which \(\int R\,\mathrm dV_g\) has dimensions of area, the [[philosophy/principle-of-least-action/einstein-hilbert-action|Einstein--Hilbert action]] satisfies

$$
S_{\mathrm{EH}}
=\frac{c^3}{16\pi G}
\int_M R\,\mathrm dV_g,
$$

and therefore

$$
\frac{S_{\mathrm{EH}}}{\hbar}
=\frac{\eta_{\mathrm E}}{4\pi}
\int_M R\,\mathrm dV_g.
$$

This displays the bulk curvature coefficient only; the cosmological term and the boundary terms required by the chosen variational problem remain separate.

The quantum phase cost of curvature is thus weighted by an inverse area. At a characteristic length \(L\), the dimensionless geometric action scales as

$$
\frac{S_{\mathrm{EH}}}{\hbar}
\sim \eta_{\mathrm E}L^2
\sim\frac{L^2}{\ell_P^2},
$$

up to geometric and normalization factors. “Spacetime is stiff” is an interpretation of this large coefficient at \(L\gg\ell_P\), not a literal material-medium model.

## Measured target in SI units

The [[data/codata-2022-fundamental-physical-constants/entry|2022 CODATA recommended value]] is

$$
G=6.67430(15)\times10^{-11}
\ \mathrm{m^3\,kg^{-1}\,s^{-2}}.
$$

Using exact SI values of \(c\) and \(h\), this corresponds to

$$
\ell_P=1.616255(18)\times10^{-35}\ \mathrm m,
$$

$$
\eta_{\mathrm E}
=9.57018(22)\times10^{68}\ \mathrm{m^{-2}},
$$

and

$$
\mathfrak a_{\mathrm E}
=1.044912(23)\times10^{-69}\ \mathrm{m^2}.
$$

These are translations of the measured \(G\), not new measurements or predictions. Their uncertainty is inherited from \(G\).

## What would add explanatory content

The equation

$$
\eta_{\mathrm E}=\frac{c^3}{4\hbar G}
$$

retypes \(G\) but cannot explain it, because the right-hand side was used to define the left. Explanatory content begins only when another construction returns a finite inverse-area coefficient without gravitational calibration and a theorem identifies that coefficient with the entropy density that controls focusing. The proposed construction is [[causal-scale-derivation-target|the causal-scale BKM modulus]].
