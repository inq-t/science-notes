# Horizon Clock Allocation

On the FLRW branch where $q\le1$, the apparent-horizon surface-gravity magnitude defines a nonnegative vertical rate $\mu_A=(1-q)/2$. Together with the area law, this yields an exact allocation of one Weyl e-fold between horizon rapidity and horizon-information growth; interpreting the rapidity as modular time remains conditional.

## Running horizon rate

For $R_A=c/H$, define

$$
\mu_A:=\frac{|\kappa_A|R_A}{c^2}.
$$

On the $q\le1$ branch used in v7,

$$
\mu_A=\frac{1-q}{2}=-\frac{I^2}{H^2}.
$$

Let the dimensionless area entropy be

$$
\mathcal S_A:=\frac{S_A}{k_B}
=\frac{\pi c^5}{G\hbar H^2}.
$$

Then

$$
\frac{\mathrm d\ln\mathcal S_A}{\mathrm dN}
=4(1-\mu_A).
$$

## Clock allocation identity

Define a geometrically normalized vertical rapidity potential by

$$
\frac{\mathrm d\eta_A}{\mathrm dt}
=\frac{|\kappa_A|}{c}.
$$

Since $\mathrm dN/\mathrm dt=H$,

$$
\frac{\mathrm d\eta_A}{\mathrm dN}=\mu_A.
$$

Combining the two rates gives

$$
\boxed{
\mathrm dN
=\mathrm d\eta_A
+\frac14\,\mathrm d\ln\mathcal S_A
}.
$$

One e-fold of Weyl scale change is partitioned into vertical horizon-rapidity advance and horizon-entropy growth. On the selected unit-slope branch, horizontal state displacement instead obeys $\mathrm d\theta/\mathrm dN=1$, so

$$
\frac{\mathrm d\theta}{\mathrm dN}
-\frac{\mathrm d\eta_A}{\mathrm dN}
=\frac14\frac{\mathrm d\ln\mathcal S_A}{\mathrm dN}.
$$

## Claim status

- **Exact on the stated branch:** the algebraic identity given flat FLRW, the area law, $q\le1$, and the chosen positive surface-gravity normalization.
- **Conditional interpretation:** treating $\eta_A$ as vertical modular time.
- **Physical choice:** the horizontal unit-slope law.
- **Not universal:** for $q>1$, the magnitude $\mu_A=|1-q|/2$ no longer supports the displayed allocation without a signed redefinition.

## Dependencies and uses

This note combines [[flrw-kinematics|FLRW scale kinematics]] with [[modular-flow|the vertical/horizontal distinction]].

## Provenance

Distilled from [[Causal_Scale_Dynamics_Master_v7_0|Causal Scale Dynamics Master v7.0]] with its domain assumption made explicit.
