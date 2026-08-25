# CST-B2 Present-Flatness Closure

For the flat, zero-residual CST-B2 background, present flatness eliminates the reference critical density and gives one implicit equation for the candidate-crossing date. The result is an exact conditional reduction of this member's homogeneous assumptions, not a microscopic selection of a root and not a theorem about every CST response member.

Assume a spatially flat \(3+1\)-dimensional GR--FLRW background containing matter, radiation, and the CST-B2 response, with no residual or additional sector. Let

$$
\Omega_{m0}\geq0,
\qquad
\Omega_{r0}\geq0,
\qquad
D:=1-\Omega_{m0}-\Omega_{r0}>0.
$$

Use

$$
N:=\ln\frac{a}{a_0},
\qquad
x:=N-N_c,
\qquad
x_c:=-N_c=\ln(1+z_c),
$$

and define

$$
M(x):=\Omega_{m0}e^{3x}+\Omega_{r0}e^{4x}.
$$

Let the crossing fraction and response profile be

$$
\Omega_{X,c}=\frac{\mathfrak R_c}{2},
\qquad
\rho_X(N)
=\frac{\mathfrak R_c}{2}\rho_{\mathrm{crit},c}
\operatorname{sech}^2(\nu x),
$$

with \(0<\mathfrak R_c<2\) and \(\nu>0\). Their physical provenance remains the conditional construction in [[causal-scale-theory/response-law|the response interface]].

## Elimination

Flatness at the crossing gives

$$
\left(1-\frac{\mathfrak R_c}{2}\right)
\frac{\rho_{\mathrm{crit},c}}{\rho_{\mathrm{crit},0}}
=M(x_c).
$$

At the present epoch, \(x=x_c\), so

$$
D
=\frac{\mathfrak R_c}{2}
\frac{\rho_{\mathrm{crit},c}}{\rho_{\mathrm{crit},0}}
\operatorname{sech}^2(\nu x_c).
$$

Eliminating \(\rho_{\mathrm{crit},c}/\rho_{\mathrm{crit},0}\) yields

$$
\boxed{
\frac{\mathfrak R_c}{2-\mathfrak R_c}
M(x_c)\operatorname{sech}^2(\nu x_c)
=D.}
$$

Equivalently, with

$$
F_\nu(x):=M(x)\operatorname{sech}^2(\nu x),
\qquad
T_{\mathfrak R}:=D\frac{2-\mathfrak R_c}{\mathfrak R_c},
$$

the allowed crossing dates are the real roots of

$$
F_\nu(x_c)=T_{\mathfrak R}.
$$

The equation may have more than one root. Each root labels a distinct background solution with the same parameter values; it is not another crossing inside one already-selected history.

## Present crossing

At \(x_c=0\),

$$
M(0)=\Omega_{m0}+\Omega_{r0}=1-D,
$$

and the closure equation reduces exactly to

$$
\boxed{\mathfrak R_c=2D.}
$$

Consequently, the present-crossing amplitude is fixed by the declared present complement. This does not promote \(\mathfrak R_c\) from an integrated crossing ratio to a universal constant.

## Scope

Curvature, a residual vacuum, interactions, an additional crossing component, or a different horizon/source conversion changes the closure. Numerical root counts and benchmark folds are receipts for this equation rather than premises of the theorem.
