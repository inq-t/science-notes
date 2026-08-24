# Generalized Background and Branch Structure

Keeping the width $\nu$ and peak amplitude $\mathfrak R_c$ explicit reveals what the two unit principles actually predict, how present flatness dates the crossing, and where the proposed-v8 revision overstated a matter-era fold as an absolute existence ceiling. The exact matter-plus-radiation equation has multiple branches; the intended late-time cosmology is the smallest positive root continuously connected to the unit solution.

## Conventions

Use

$$
N=\ln\frac{a}{a_0},
\qquad
x=N-N_c,
\qquad
x_c:=-N_c=\ln\frac{a_0}{a_c},
$$

The intended late branch imposes the additional prior $x_c>0$, meaning the crossing lies in our past. The generalized closure also admits $x_c<0$ future-crossing solutions, which must not be discarded silently.

and

$$
M(x):=\Omega_{m0}e^{3x}+\Omega_{r0}e^{4x},
\qquad
D:=1-\Omega_{m0}-\Omega_{r0}.
$$

Matter and radiation use $N$:

$$
\rho_m=\rho_{m0}e^{-3N},
\qquad
\rho_r=\rho_{r0}e^{-4N}.
$$

The response is centered in $x$:

$$
\rho_X(N)
=\frac{\mathfrak R_c}{2}\rho_{\rm crit,c}
\operatorname{sech}^2(\nu x).
$$

This note assumes flat $3+1$ GR, a zero residual, and separately conserved matter, radiation, and response sectors.

## Crossing fractions and amplitude range

At $x=0$,

$$
\rho_{X,c}=\frac{\mathfrak R_c}{2}\rho_{\rm crit,c}.
$$

Flatness gives

$$
\Omega_{X,c}=\frac{\mathfrak R_c}{2},
\qquad
\Omega_{{\rm ordinary},c}=1-\frac{\mathfrak R_c}{2},
$$

and therefore

$$
\frac{\rho_{X,c}}{\rho_{{\rm ordinary},c}}
=\frac{\mathfrak R_c}{2-\mathfrak R_c}.
$$

Positive response and positive ordinary density require

$$
0<\mathfrak R_c<2.
$$

The upper bound is kinematic within this sector. Equality with ordinary density is the sharper unit-amplitude prediction

$$
\mathfrak R_c=1
\quad\Longleftrightarrow\quad
\rho_{X,c}=\rho_{{\rm ordinary},c}.
$$

In $d$ spatial dimensions the same marginal-horizon algebra gives

$$
\Omega_{X,c}=\frac{\mathfrak R_c}{d-1},
\qquad
\frac{\rho_{X,c}}{\rho_{{\rm ordinary},c}}
=\frac{\mathfrak R_c}{d-1-\mathfrak R_c},
$$

provided the dimensional generalization of the entropy, critical density, and source law is retained.

Positive response and ordinary fractions require

$$
0<\mathfrak R_c<d-1,
$$

and equal partition occurs at

$$
\mathfrak R_c=\frac{d-1}{2}.
$$

## Present flatness and elimination of the center

At the crossing,

$$
\frac{\rho_{\rm crit,c}}{\rho_{\rm crit,0}}
=\frac{2M(x_c)}{2-\mathfrak R_c}.
$$

Evaluating the response today and imposing flatness gives the exact closure equation

$$
\boxed{
\frac{\mathfrak R_c}{2-\mathfrak R_c}
M(x_c)\operatorname{sech}^2(\nu x_c)=D.
}
$$

Equivalently,

$$
F_\nu(x_c)=T_{\mathfrak R},
$$

where

$$
F_\nu(x):=M(x)\operatorname{sech}^2(\nu x),
\qquad
T_{\mathfrak R}:=D\frac{2-\mathfrak R_c}{\mathfrak R_c}.
$$

The center is thus solution data once $(\Omega_{m0},\Omega_{r0},\nu,\mathfrak R_c)$ and a root branch are specified. It is not automatically a single-valued function of those inputs. On the continuous unit-width branch,

$$
x_c>0
\quad\Longleftrightarrow\quad
\mathfrak R_c<2D.
$$

At the benchmark $2D=1.378621$. Thus the full kinematic interval $0<\mathfrak R_c<2$ includes future-crossing solutions; generalized likelihoods must search negative as well as positive roots unless a past-crossing prior is declared.

For the unit-amplitude branch,

$$
F_\nu(x_c)=D.
$$

## Fold equations and the radiation branch

Stationary points satisfy

$$
\frac{\mathrm d\ln F_\nu}{\mathrm dx}
=
\frac{3\Omega_{m0}e^{3x}+4\Omega_{r0}e^{4x}}
{\Omega_{m0}e^{3x}+\Omega_{r0}e^{4x}}
-2\nu\tanh(\nu x)=0.
$$

A fold solves this together with $F_\nu=T_{\mathfrak R}$. The large-$x$ behavior is

$$
F_\nu(x)
\sim
4\Omega_{m0}e^{(3-2\nu)x}
+4\Omega_{r0}e^{(4-2\nu)x}.
$$

Radiation therefore changes the global root topology. For any $\nu<2$, its asymptotic term grows; a sufficiently high-redshift root can survive after the late root has disappeared.

For the benchmark

$$
\mathfrak R_c=1,
\qquad
\Omega_{m0}=0.310598,
\qquad
\Omega_{r0}=9.15\times10^{-5},
$$

the positive-root atlas is:

| Width | Positive roots of present flatness |
|---|---|
| $0<\nu<1.558402308$ | one low-$x$ root |
| $\nu=1.558402308$ | one low root and a radiation-driven double root at $x=6.106871592$ |
| $1.558402308<\nu<1.814657203$ | three roots |
| $\nu=1.814657203$ | a late-branch double root at $x=0.649049974$ and one high-$x$ radiation root |
| $1.814657203<\nu<2$ | one very-high-$x$ radiation root |
| $\nu\ge2$ | no root for these benchmark inputs |

Examples make the separation vivid:

$$
\nu=1.8:
\quad
x_c\approx0.5466053,\ 0.8024096,\ 18.8519793,
$$

$$
\nu=1.9:
\quad
x_c\approx37.7040688.
$$

The often quoted $\nu_{\max}\simeq1.814$ is **not** an absolute existence ceiling. It is the terminal fold of the smallest positive root connected to the intended late-time branch. Strictly setting $\Omega_{r0}=0$ throughout gives $\nu_{\rm fold}\simeq1.81400853$. The supplied receipt's value $1.81413212$ is a **hybrid dust-form approximation**: it drops radiation from $M(x)$ but retains it in $D=1-\Omega_{m0}-\Omega_{r0}$. Neither approximation can describe the radiation-driven roots.

> **[SECTOR — LATE BRANCH]** The phenomenological late branch is the smallest positive flatness root continuously connected to the unit-width solution $x_c\simeq0.2940066$.

High-$x$ roots are mathematically real. They correspond to a radically earlier crossing and are rejected by the intended late-time phenomenology, not by nonexistence. Any likelihood varying $\nu$ or $\mathfrak R_c$ must state whether it enforces this branch, profiles over all roots, or assigns branch priors. The folds must be recomputed when the amplitude or ordinary abundances change.

The quoted folds and representative roots are reproduced without SciPy by [the reviewed background receipt](receipts/background.py).

## Flow equation and differential invariant

Separate conservation gives

$$
w_X=-1+\frac{2\nu}{3}\tanh(\nu x).
$$

Writing $X:=1+w_X$,

$$
X'=\frac{2\nu^2}{3}-\frac32X^2.
$$

The two fixed points

$$
w_\pm=-1\pm\frac{2\nu}{3}
$$

are hyperbolic. The $\tanh$ history is a heteroclinic orbit modulo translation, not a saddle-node pair.

Eliminating $x$ gives

$$
\boxed{
9(1+w_X)^2+6w_X'=4\nu^2.
}
$$

This invariant measures the width independently of the amplitude and crossing date, assuming the separately conserved response description is valid.

Use the CPL convention

$$
w(a)=w_0+w_a(1-a),
\qquad
w_a=-w'_0.
$$

The local CPL tangent at the present epoch is

$$
1+w_0=\frac{2\nu}{3}\tanh(\nu x_c),
$$

$$
w_a=-\frac{2\nu^2}{3}\operatorname{sech}^2(\nu x_c),
$$

so

$$
\boxed{
w_a=\frac32(1+w_0)^2-\frac{2\nu^2}{3}.
}
$$

This is a tangent relation, not an assertion that CPL extrapolation reproduces the exact history at all redshifts.

## Future classes

On the zero-residual branch,

$$
\rho_X\sim a^{-2\nu},
\qquad
w_X\to-1+\frac{2\nu}{3}.
$$

If the response dominates, the asymptotic scale factor behaves as

$$
a(t)\sim t^{1/\nu}.
$$

This gives distinct futures:

- $0<\nu<1$: response-dominated power-law acceleration;
- $\nu=1$: coasting, $a\sim t$, with no future event horizon;
- $1<\nu<3/2$: response-dominated deceleration;
- $\nu=3/2$: matterlike scaling;
- $\nu>3/2$: matter eventually dominates and decelerates;
- any positive constant residual eventually restores de Sitter expansion.

For unit width,

$$
1+3w_X=2(\tanh x-1)<0
$$

at every finite $x$. It approaches zero but does not cross it. The future acceleration exit occurs because the positive active mass of matter and radiation overtakes the decaying negative response, not because the response itself becomes decelerating at a finite time.

## Unit-branch benchmark

For the benchmark ordinary abundances above and the late root,

$$
x_c=0.2940066,
\qquad
z_c=e^{x_c}-1=0.3417927.
$$

The conditional background outputs are approximately

| Quantity | Unit-branch value |
|---|---:|
| $w_0$ | $-0.8094545$ |
| $w_a$ | $-0.6122053$ |
| $q_0$ | $-0.3369025$ |
| $j_0$ | $-0.1112465$ |
| acceleration entry | $z\approx0.7856935$ |
| acceleration exit | $a/a_0\approx11.7865$ |

These are arithmetic consequences of the stated background closure. They are not measurements, and agreement of a receipt script with them does not validate the wall state, the two unit principles, or the constitutive source law.
