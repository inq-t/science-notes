# Conditional Background Model

The binary state geometry fixes a shape. It does not, by itself, say that this shape is a cosmological energy density or fix its normalization. This note keeps those steps separate.

## Exact binary geometry

After the normal-chirality reduction, let

$$
Q^2=1,
\qquad
\omega_\theta=\frac{e^{\theta Q}}{2\cosh\theta}.
$$

The denominator assumes a balanced two-outcome quotient: the $+1$ and $-1$ sectors have equal normalized weight. The relation $Q^2=1$ alone would also allow unequal degeneracies and would then give a different partition function.

The log-partition function $\Psi(\theta)=\ln(2\cosh\theta)$ gives

$$
m(\theta):=\langle Q\rangle_\theta=\tanh\theta,
$$

$$
g_{\theta\theta}^{\mathrm{BKM}}
=\Psi''(\theta)
=\operatorname{sech}^2\theta.
$$

Consequently,

$$
m^2+g_{\theta\theta}^{\mathrm{BKM}}=1.
$$

Reflection interchanges $\theta$ and $-\theta$. Their symmetrized relative entropy is

$$
\mathfrak S_J(\theta)
=S(\omega_\theta\Vert\omega_{-\theta})
+S(\omega_{-\theta}\Vert\omega_\theta)
=4\theta\tanh\theta,
$$

which has its unique minimum at $\theta=0$. These identities are exact within the reduced binary family. See [[binary-information-geometry/balanced-exponential-family|the balanced binary family]].

## Pullback along scale

Let

$$
x:=N-N_c,
\qquad
\theta=\varrho_\perp x.
$$

The normalized pullback metric is

$$
g_{NN}^{\mathrm{BKM}}
=\varrho_\perp^2
\operatorname{sech}^2(\varrho_\perp x).
$$

The coordinate-invariant object is the line element

$$
g_{NN}^{\mathrm{BKM}}\,\mathrm dN^2
=\operatorname{sech}^2\theta\,\mathrm d\theta^2.
$$

Thus $\varrho_\perp$ records how physical scale traverses the state path; it is not determined by the intrinsic binary curve.

## Constitutive density

The cosmological proposal promotes the binary BKM shape to a homogeneous density,

$$
\rho_X(N)
=A\operatorname{sech}^2(\varrho_\perp x),
\qquad A>0.
$$

This is the [[causal-scale-theory/free-energy-source|all-history modular source law]], not a consequence of the binary algebra. Define the cut-integrated crossing ratio of the extensive horizontal state by

$$
\mathfrak R_c
:=\frac{k_B}{S_c}G_{NN}^{\perp}(N_c).
$$

Combining the source law with the [[conformal-scale-geometry/hawking-friedmann-identity|flat-FLRW horizon conversion]] gives

$$
A=\frac12\rho_{\mathrm{crit},c}\mathfrak R_c.
$$

[[program-core/ruble-equations#RE6 — Integrated reference matching|Weak unit matching]] is the additional statement $\mathfrak R_c=1$. On that branch,

$$
\rho_X(N)
=\frac12\rho_{\mathrm{crit},c}
\operatorname{sech}^2(\varrho_\perp x).
$$

At $x=0$, flatness then gives

$$
\rho_X(N_c)=\rho_{\mathrm{ordinary}}(N_c),
$$

where ordinary means every non-response component, including radiation. The equality is conditional on the closure principle; it is not fixed by self-duality alone.

## Conservation and the shape invariant

If the response is separately conserved,

$$
\frac{\mathrm d\rho_X}{\mathrm dN}
=-3(1+w_X)\rho_X,
$$

then

$$
w_X(N)
=-1+\frac{2\varrho_\perp}{3}
\tanh(\varrho_\perp x),
$$

and

$$
\frac{\mathrm dw_X}{\mathrm dN}
=\frac{2\varrho_\perp^2}{3}
\operatorname{sech}^2(\varrho_\perp x).
$$

Eliminating $x$, $N_c$, and $A$ gives the exact conditional invariant

$$
\boxed{
9(1+w_X)^2
+6\frac{\mathrm dw_X}{\mathrm dN}
=4\varrho_\perp^2
}.
$$

For $X:=1+w_X$, the equivalent autonomous flow is

$$
\frac{\mathrm dX}{\mathrm dN}
=\frac{2\varrho_\perp^2}{3}
-\frac32X^2.
$$

This is a Riccati flow with two fixed points. Calling it a saddle-node normal form is stronger than the displayed equation warrants unless a control parameter and an actual bifurcation are supplied.

For the CPL tangent convention $w(a)=w_0+w_a(1-a)$,

$$
w_a=-\left.\frac{\mathrm dw_X}{\mathrm dN}\right|_{N=0},
$$

so the family lies on

$$
w_a
=\frac32(1+w_0)^2
-\frac{2\varrho_\perp^2}{3}.
$$

At unit slope the invariant has right-hand side $4$ and the CPL locus has intercept $-2/3$.

## Asymptotics and acceleration

For positive $\varrho_\perp$,

$$
w_X\longrightarrow
-1-\frac{2\varrho_\perp}{3}
\quad (N\to-\infty),
$$

$$
w_X\longrightarrow
-1+\frac{2\varrho_\perp}{3}
\quad (N\to+\infty).
$$

At unit slope, the response rises from the phantom side, crosses $w_X=-1$ at its density maximum, and decays as $a^{-2}$ toward $w_X=-1/3$.

A single finite era of total cosmic acceleration and a coasting future require more than this internal flow: they use the closed amplitude, flat expanding matter+radiation background, separate conservation, and an exactly zero nonnegative residual floor. A positive residual can restore permanent late de Sitter acceleration; negative-residual or recollapsing branches require a separate analysis.
