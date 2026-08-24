# Horizons, black holes, entropy, and the meanings of time

## Four distinct notions of time

The framework uses several ordered parameters that must not be conflated.

| Symbol or notion | Meaning |
|---|---|
| causal order | a partial order on events; no metric duration is implied |
| proper or clock time $\tau$ | metric length along a timelike worldline |
| Weyl scale time $N$ | logarithmic change of the scale section, $N=\ln(a/a_c)$ |
| vertical modular parameter $s$ | automorphism parameter within one algebra/state fiber |
| horizontal state coordinate $\theta$ | relative modular polarization across a family of states |

The v5.0 inconsistency arose from treating the last two as the same parameter. They are different directions even when they use the same normal boost generator.

## Running horizon index

For a spherical horizon of areal radius $R_H$, define

$$
\boxed{
\mu_H:=\frac{|\kappa_H|R_H}{c^2}.
}
$$

It compares a normal-boost rate with an inverse geometric scale. It is a state-dependent index, not the Ruble number and not a measure of a total “amount of gravity.”

For a flat FLRW apparent horizon,

$$
R_A=\frac{c}{H},
$$

and the Kodama--Hayward surface gravity gives

$$
\boxed{
\mu_A=\frac{1-q}{2}=-\frac{I^2}{H^2}.
}
$$

The first equality is horizon kinematics; the second is scale-tractor geometry. In four-dimensional spherical Einstein gravity,

$$
S_A=k_B\frac{\pi R_A^2c^3}{G\hbar},
\qquad
E_A=\frac{c^4R_A}{2G},
$$

so, with the positive Kodama--Hayward temperature,

$$
\mu_A=\frac{T_AS_A}{E_A}.
$$

Representative values are

| regime | $w$ | $q$ | $\mu_A$ |
|---|---:|---:|---:|
| radiation | $1/3$ | $1$ | $0$ |
| matter | $0$ | $1/2$ | $1/4$ |
| coasting / acceleration threshold | $-1/3$ | $0$ | $1/2$ |
| de Sitter | $-1$ | $-1$ | $1$ |

Therefore

$$
\boxed{
\ddot a>0\iff\mu_A>\frac12.
}
$$

The value $1/2$ also equals $|\kappa|R/c^2$ for a four-dimensional Schwarzschild horizon. This identifies a shared dimensionless surface-gravity balance; it does not identify an FLRW spacetime with a Schwarzschild spacetime.

## Clock allocation

The dimensionless apparent-horizon entropy is

$$
\mathcal S_A=\frac{S_A}{k_B}=\frac{\pi c^5}{G\hbar H^2}.
$$

Hence

$$
\frac{\dd\ln\mathcal S_A}{\dd N}=4(1-\mu_A).
$$

Define a geometrically normalized vertical horizon rapidity potential $\eta_A$ by

$$
\frac{\dd\eta_A}{\dd t}=\frac{|\kappa_A|}{c}.
$$

Since $\dd N/\dd t=H$,

$$
\frac{\dd\eta_A}{\dd N}=\mu_A.
$$

Thus

$$
\boxed{
\dd N=\dd\eta_A+\frac14\dd\ln\mathcal S_A.
}
$$

One Weyl e-fold decomposes exactly into vertical horizon-rapidity advance and horizon-information growth. The horizontal fundamental law is instead

$$
\frac{\dd\theta}{\dd N}=1.
$$

Consequently,

$$
\boxed{
\theta'-\eta_A'
=1-\mu_A
=\frac14(\ln\mathcal S_A)'.
}
$$

This is the corrected relation among horizontal state motion, vertical horizon motion, and information capacity.

## Smarr and Hawking relations as scale homogeneity

For a one-scale asymptotically flat black hole in $D$ spacetime dimensions,

$$
E\propto R_H^{D-3},
\qquad
S\propto R_H^{D-2}.
$$

Euler homogeneity and $\dd E=T\dd S$ give

$$
\boxed{
(D-3)E=(D-2)TS.
}
$$

The Smarr relation is therefore the compatibility of thermodynamic variation with scale homogeneity. In four dimensions, $E=2TS$.

The cosmological relation used in the amplitude closure is not the stationary Schwarzschild Smarr relation. It uses the canonically normalized horizontal causal-diamond temperature,

$$
k_BT_c=\frac{\hbar c}{2\pi R_c},
$$

together with the apparent-horizon area law and Misner--Sharp marginality to obtain

$$
T_cS_c=E_{\rm MS,c}.
$$

This distinction between vertical dynamical surface gravity and horizontal modular normalization is essential.

## Holography as a controlled laboratory

In a holographic code subspace, the JLMS relation takes the schematic form

$$
K_A^{\rm CFT}
=\frac{\widehat A(\chi_A)}{4G_N\hbar}
+K_a^{\rm bulk}
+\text{central term}
+O(G_N).
$$

Boundary modular charge decomposes into a geometric area charge and a bulk modular charge. In related controlled settings:

- the Hessian of relative entropy equals gravitational canonical energy;
- modular Berry curvature maps to gravitational symplectic structure;
- crossed-product gravitational algebras make generalized entropy a genuine von Neumann entropy for suitable subregions.

These results do not prove the FLRW scale-capacity law. They establish that modular charge, area, information Hessian, symplectic form, and gravity can form one coherent subregion structure.
