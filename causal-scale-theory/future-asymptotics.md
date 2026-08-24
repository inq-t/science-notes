# Expansion History and Future Classes

Once a positive flatness root is selected, the generalized response fixes the homogeneous expansion history. Its zero-residual future is classified by the response dilution exponent $2\nu$; a positive residual overrides that classification with de Sitter behavior.

Let $x_c$ be a chosen root from [[flatness-branches]], let $x=N+x_c$, and set

$$
D:=1-\Omega_{m0}-\Omega_{r0}.
$$

The zero-residual expansion function is

$$
\boxed{
\begin{aligned}
E^2(x):=\frac{H^2(x)}{H_0^2}
=\;&\Omega_{m0}e^{3(x_c-x)}
+\Omega_{r0}e^{4(x_c-x)}\\
&+D\frac{\operatorname{sech}^2(\nu x)}
{\operatorname{sech}^2(\nu x_c)}.
\end{aligned}}
$$

Distance, age, and deceleration observables follow from this function. Structure growth additionally requires the covariant response and perturbation data that [[conjectures/covariant-response-sector|remain open]].

## Response asymptotics

From [[response-law]],

$$
\rho_X\sim a^{-2\nu},
\qquad
w_X\to-1+\frac{2\nu}{3}
\qquad(x\to+\infty).
$$

Compare the response dilution with matter, $\rho_m\sim a^{-3}$:

- $0<\nu<1$: the response dominates and gives asymptotic power-law acceleration;
- $\nu=1$: the response dominates, $w_X\to-1/3$, and expansion tends to coasting;
- $1<\nu<3/2$: the response dominates but the future decelerates;
- $\nu=3/2$: response and matter have the same leading dilution;
- $\nu>3/2$: matter eventually dominates.

These are zero-residual classes. A positive constant residual eventually dominates and yields de Sitter expansion; a negative one can force a turnaround if the total density reaches zero.

## Acceleration is not fixed by width alone

The existence and duration of an accelerating interval also depend on $\mathfrak R_c$, the chosen closure root, the ordinary abundances, and the residual sector. In particular, a unit-width model with sufficiently small amplitude need not accelerate.

[[unit-branch]] explains the more delicate unit result: its response density dominates at late scale, but its negative active mass decays faster than matter active mass, so acceleration ends at finite $a/a_0$ before the background approaches coasting.
