# Present Flatness and the Crossing Branches

Present flatness converts the generalized response into an implicit equation for its crossing date. The equation may have several positive roots, so the crossing is branch data. The value $\nu=2$ classifies the radiation-tail asymptotics but is not a universal root-existence bound.

Assume the zero-residual flat background with present matter and radiation abundances $\Omega_{m0},\Omega_{r0}$. Define

$$
N:=\ln\frac a{a_0},
\qquad
x:=N-N_c,
\qquad
x_c:=-N_c=\ln(1+z_c)>0,
$$

and

$$
D:=1-\Omega_{m0}-\Omega_{r0},
\qquad
M(x):=\Omega_{m0}e^{3x}+\Omega_{r0}e^{4x}.
$$

At the crossing, flatness and [[response-law|the peak fraction]] give

$$
\left(1-\frac{\mathfrak R_c}{2}\right)
\frac{\rho_{\mathrm{crit},c}}{\rho_{\mathrm{crit},0}}
=M(x_c).
$$

At the present epoch,

$$
D
=\frac{\mathfrak R_c}{2}
\frac{\rho_{\mathrm{crit},c}}{\rho_{\mathrm{crit},0}}
\operatorname{sech}^2(\nu x_c).
$$

Eliminating the crossing critical density yields

$$
\boxed{
\frac{\mathfrak R_c}{2-\mathfrak R_c}
M(x_c)\operatorname{sech}^2(\nu x_c)=D.}
$$

Equivalently, set

$$
F_\nu(x):=M(x)\operatorname{sech}^2(\nu x),
\qquad
T_{\mathfrak R}:=D\frac{2-\mathfrak R_c}{\mathfrak R_c}.
$$

The allowed dates are positive roots of

$$
F_\nu(x_c)=T_{\mathfrak R}.
$$

Each root defines a parameter-compatible background history. It is not another crossing inside one selected history. The canonical late branch is the smallest positive root unless a deeper selection rule is supplied.

## The tail threshold

If $\Omega_{r0}>0$, then

$$
F_\nu(x)
\sim4\Omega_{r0}e^{(4-2\nu)x}
\qquad(x\to+\infty).
$$

Hence

$$
\begin{array}{c|c}
0<\nu<2 & F_\nu(x)\to+\infty,\\
\nu=2 & F_\nu(x)\to4\Omega_{r0},\\
\nu>2 & F_\nu(x)\to0.
\end{array}
$$

This does not decide whether the finite graph crosses $T_{\mathfrak R}$. Root number depends on

$$
(\nu,\mathfrak R_c,\Omega_{m0},\Omega_{r0})
$$

and on the admitted domain for $x_c$. In the absence of radiation, the analogous tail threshold is $\nu=3/2$.

## Fold condition

A double root satisfies the closure equation and

$$
\frac{3\Omega_{m0}e^{3x}+4\Omega_{r0}e^{4x}}
{\Omega_{m0}e^{3x}+\Omega_{r0}e^{4x}}
-2\nu\tanh(\nu x)=0.
$$

For the inherited benchmark

$$
\Omega_{m0}=0.310598,
\qquad
\Omega_{r0}=9.15\times10^{-5},
\qquad
\mathfrak R_c=1,
$$

the reviewed atlas is:

- $0<\nu<1.558402308$: one positive late root;
- $\nu\simeq1.558402308$: one simple late root and a high-$x$ double root at $x\simeq6.10687$;
- $1.558402308<\nu<1.814657$: three positive roots;
- $\nu\simeq1.814657$: a late double root near $x\simeq0.64905$ plus one high-$x$ root;
- $1.814657<\nu<2$: one high-radiation root;
- $\nu\ge2$: no positive root for these benchmark inputs.

The final statement is benchmark-specific. [[receipts/background.json|The local receipt]] finds positive roots at $\nu=2$ and $\nu=2.2$ when the same abundances are paired with $\mathfrak R_c=1.9$.
