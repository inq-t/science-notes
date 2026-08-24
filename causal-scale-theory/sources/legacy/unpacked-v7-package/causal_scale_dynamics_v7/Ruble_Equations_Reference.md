---
title: "Causal Scale Dynamics"
subtitle: "Compact Reference to the Ruble Equations"
author: "Thomas Ruble"
date: "21 August 2026"
lang: en-US
papersize: letter
fontsize: 11pt
geometry: margin=0.8in
colorlinks: true
linkcolor: blue
urlcolor: blue
header-includes:
  - |
    \usepackage{amsmath,amssymb,mathtools,booktabs,longtable,array,microtype}
    \newcommand{\BKM}{\mathrm{BKM}}
    \newcommand{\E}{\mathcal E}
    \newcommand{\dd}{\mathrm d}
    \newcommand{\sech}{\operatorname{sech}}
    \newcommand{\avg}[1]{\left\langle #1\right\rangle}
    \newcommand{\vperp}{\varrho_\perp}
    \newcommand{\Ruble}{\mathfrak R_c}
---

> **Status.** Compact reference to the homogeneous theory. The scale-capacity equivalence law is a physical principle, not a theorem of mathematics. The covariant perturbation lift and global vacuum sector remain open.


The theory is most compactly stated as a sequence of definitions and one physical equivalence principle. The equations are organized by mathematical type rather than by discovery history.

## Kinematic and geometric register

**R1 — causal scale.**

$$
\boxed{
g_{\rm phys}=\sigma^{-2}\boldsymbol g,
\qquad
N=-\ln\frac{\sigma}{\sigma_c}=\ln\frac{a}{a_c}.
}
$$

The conformal metric $\boldsymbol g$ fixes causal cones; the scale section $\sigma\in\Gamma(\E[1])$ fixes physical calibration. $N$ is logarithmic Weyl scale, not Newtonian absolute time.

**R2 — scale tractor.**

$$
\boxed{
I_A=\frac14D_A\sigma.
}
$$

The scale tractor packages $\sigma$, its first derivative, and the trace combination of its second derivative.

**R3 — tractor transport and norm.**

$$
\boxed{
\left(\nabla_a\nabla_b\sigma+P_{ab}\sigma\right)_0
=\frac{4\pi G}{c^4}\sigma T_{ab}^{\circ},
}
$$

$$
\boxed{
I^2=\frac{2\pi G}{3c^4}T-\frac{\Lambda_g}{3}.
}
$$

The first equation is local and trace-free. The second fixes the scalar calibration channel up to a global constant.

## Horizontal state register

**R4 — normal chirality.**

$$
\boxed{
Q=P_+-P_-,
\qquad
Q^2=1,
\qquad
JQJ=-Q.
}
$$

$P_\pm$ project onto the two null lines of the Lorentzian normal plane of a codimension-two cut. The homogeneous horizontal response is assumed to factor through this fundamental chirality quotient.

**R5 — binary exponential family.**

$$
\boxed{
\omega_\theta=\frac{e^{\theta Q}}{2\cosh\theta},
\qquad
\Psi(\theta)=\ln(2\cosh\theta).
}
$$

Its dual coordinates and metric are

$$
\boxed{
\eta=\Psi'(\theta)=\tanh\theta,
\qquad
G^{\BKM}_{\theta\theta}=\Psi''(\theta)=\sech^2\theta.
}
$$

The identity

$$
\boxed{
\eta^2+G^{\BKM}_{\theta\theta}=1
}
$$

is the normalized binary moment relation $\avg{Q^2}=1$.

**R6 — horizontal soldering.**

Under the rank-one ratio and measurability hypotheses, the Connes cocycle chain rule gives

$$
\theta=\vperp(N-N_c).
$$

The theory selects the fundamental character

$$
\boxed{\vperp=1.}
$$

This is a physical representation choice: the fundamental null-normal character is identified with the fundamental scale/inverse-scale character. It is not a theorem of Cauchy's equation, and it is not obtained from an integer restriction on conformal weights.

## Scale-capacity closure

**R7 — Ruble scale-capacity number.**

Let $G^{\perp}_{NN}$ be the physical BKM norm of the selected horizontal scale tangent and $S_c$ the horizon entropy of the self-dual wall. Define

$$
\boxed{
\Ruble:=\frac{k_B}{S_c}G^{\perp}_{NN}(N_c).
}
$$

The Scale--Capacity Equivalence Principle is

$$
\boxed{\Ruble=1.}
$$

In canonical binary coordinates this is equivalently

$$
\boxed{
\frac{k_B}{S_c}G^{\perp}_{NN}(N)=\sech^2(N-N_c).
}
$$

It states that the fundamental Weyl translation is isometric, at self-duality, to the fundamental horizontal state translation when the BKM metric is normalized by horizon entropy.

**R8 — modular free-energy source.**

$$
\boxed{
\rho_X(N)=\frac{k_BT_c}{2V_c}G^{\perp}_{NN}(N).
}
$$

This is the constitutive law. It converts dimensionless relative-entropy curvature into energy density by the physical modular temperature and causal-wall volume. The factor $1/2$ is the Taylor coefficient of relative entropy at coincidence.

**R9 — Hawking--Friedmann conversion.**

For a flat four-dimensional FLRW apparent horizon,

$$
\boxed{
R_c=\frac{c}{H_c},
\qquad
\frac{S_c}{k_B}=\frac{\pi R_c^2c^3}{G\hbar},
\qquad
k_BT_c=\frac{\hbar c}{2\pi R_c},
}
$$

and

$$
\boxed{
k_BT_c\frac{S_c}{k_B}
=E_{\rm MS,c}
=\rho_{\rm crit,c}V_c.
}
$$

**R10 — closed source.**

Combining R7--R9 gives

$$
\boxed{
\rho_X(N)=\frac12\rho_{\rm crit,c}\sech^2(N-N_c).
}
$$

At the crossing,

$$
\boxed{
\Omega_{X,c}=\frac12,
\qquad
\rho_X(N_c)=\rho_{\rm ordinary}(N_c).
}
$$

The exact equality is with the complete non-dark sector. Relative to dust alone,

$$
\frac{\rho_X(N_c)}{\rho_m(N_c)}
=1+\frac{\rho_r(N_c)}{\rho_m(N_c)}+\cdots.
$$

## Dynamical consequences

**R11 — equation of state.**

Separate conservation,

$$
\rho_X'=-3(1+w_X)\rho_X,
$$

gives

$$
\boxed{
w_X(N)=-1+\frac23\tanh(N-N_c).
}
$$

**R12 — shape invariant.**

$$
\boxed{
9(1+w_X)^2+6w_X'=4.
}
$$

Equivalent forms are

$$
\boxed{
\frac{\rho_X}{\rho_*}
+\frac14\left(\frac{\dd\ln\rho_X}{\dd N}\right)^2=1,
}
$$

and

$$
X'=\frac23-\frac32X^2,
\qquad X:=1+w_X.
$$

**R13 — self-dual comparison.**

The symmetrized relative entropy of the state and its modular reflection is

$$
\boxed{
\mathfrak S_J(\theta)=4\theta\tanh\theta.
}
$$

It has a unique global minimum at $\theta=0$. Along the rigid history,

$$
\boxed{
\mathfrak S_J=6(N-N_c)(1+w_X).
}
$$

Thus relative-entropy positivity fixes the orientation of the $w_X=-1$ crossing relative to increasing Weyl scale.

**R14 — central blindness.**

$$
\boxed{
\operatorname{Var}(K+\alpha\mathbf1)=\operatorname{Var}(K).
}
$$

The local response is blind to the absolute energy zero. A global scalar lift remains in $\Lambda_g$.

![Dependency structure of the theory. The scale-capacity principle is the single new equivalence law closing the homogeneous amplitude.](figures/dependency_v7.pdf){width=94%}

## What is law, what is solution data, and what is measured

| Quantity | Type | Role |
|---|---|---|
| $[g]$ | causal/conformal geometry | fixes null cones and causal order |
| $\sigma$ | scale section | metric calibration |
| $N$ | Weyl coordinate | logarithmic scale displacement |
| $Q$ | normalized normal chirality | fundamental horizontal binary score |
| $\theta$ | horizontal state coordinate | relative modular polarization |
| $\Ruble$ | dimensionless equivalence number | entropy-normalized peak BKM speed; postulated value $1$ |
| $N_c$ | solution origin | location of the intrinsic self-dual event relative to today |
| $\Omega_{m0},\Omega_{r0}$ | measured state data | determine the location of the crossing in the closed background |
| $\Lambda_g$ | global lift/sector | not part of local trace-free transport; zero in the open-future branch |

The theory therefore contains no continuously fitted dark-history function and no independent dark amplitude. It does contain one explicit physical equivalence principle and one global sector choice.
