# The Generalized Response Law

Given the CST constitutive closure and separate homogeneous conservation, the response density is a two-parameter $\operatorname{sech}^2$ pulse whose equation of state follows a Riccati flow and obeys an amplitude-independent differential invariant. These are conditional background deductions, not properties of binary information geometry alone.

Set

$$
x:=N-N_c,
\qquad
\nu>0,
\qquad
\mathfrak R_c>0.
$$

The closed response density is

$$
\boxed{
\rho_X(x)
=\frac{\mathfrak R_c}{2}\rho_{\mathrm{crit},c}
\operatorname{sech}^2(\nu x).}
$$

The profile uses [[causal-scale-theory/scale-soldering|affine soldering]], [[causal-scale-theory/scale-capacity|the peak ratio]], the fixed extensive normalization, [[causal-scale-theory/free-energy-source|the constitutive source]], and [[causal-scale-theory/hawking-friedmann|the horizon conversion]].

## Separate conservation

Assume

$$
\frac{\mathrm d\rho_X}{\mathrm dN}
+3(1+w_X)\rho_X=0.
$$

Since $\mathrm d/\mathrm dN=\mathrm d/\mathrm dx$,

$$
\boxed{
w_X(x)
=-1+\frac{2\nu}{3}\tanh(\nu x).}
$$

Writing $X:=1+w_X$ gives

$$
X'
=\frac{2\nu^2}{3}-\frac32X^2.
$$

The solution is a translated heteroclinic orbit between $X=\pm2\nu/3$. It is not a saddle-node flow.

## Differential invariant

Differentiation eliminates the crossing date and amplitude:

$$
\boxed{
9(1+w_X)^2+6w_X'=4\nu^2.}
$$

For a local CPL tangent $w(a)=w_0+w_a(1-a)$,

$$
w_a=-w'_0
=\frac32(1+w_0)^2-\frac{2\nu^2}{3}.
$$

Both relations apply to the separately identified $X$ sector. A posterior for a total effective equation of state, or for a differently normalized CPL model, is not automatically a measurement of them.

## Equivalent density identities

Let

$$
y:=\frac{\rho_X}{\rho_{X,c}}
=\operatorname{sech}^2(\nu x).
$$

The same binary normalization can be written without $w_X$ as

$$
\boxed{
y+\frac1{4\nu^2}
\left(\frac{\mathrm d\ln y}{\mathrm dN}\right)^2
=1,}
$$

or as the logarithmic-curvature equation

$$
\boxed{
\frac{\mathrm d^2\ln y}{\mathrm dN^2}
+2\nu^2y=0.}
$$

With $\Delta:=-\mathrm d\ln y/\mathrm dN=3(1+w_X)$, one obtains the Riccati form

$$
\Delta'
=2\nu^2-\frac12\Delta^2.
$$

These equations are equivalent only for the rigid constant-extensivity pulse. A scale-dependent channel factor would preserve the normalized binary identity while changing all three physical density relations.

## The crossing

At $x=0$,

$$
\Omega_{X,c}=\frac{\mathfrak R_c}{2}.
$$

If the crossing background is spatially flat, the total non-$X$ complement has fraction $1-\mathfrak R_c/2$. Positivity gives

$$
0<\mathfrak R_c<2,
$$

and

$$
\frac{\rho_{X,c}}{\rho_{\mathrm{non-}X,c}}
=\frac{\mathfrak R_c}{2-\mathfrak R_c}.
$$

Identifying that complement with matter plus radiation also requires zero residual and no additional crossing component. Equality occurs at $\mathfrak R_c=1$ under those premises.

The positive pulse has a maximum at $x=0$, and conservation gives $w_X(0)=-1$. For an arbitrary positive separately conserved component, $\rho'_X=0$ implies only a stationary point and $w_X=-1$; maximality here comes from the explicit pulse.

## Scope

This law fixes no covariant stress tensor, sound speed, anisotropic stress, or initial perturbation. It is the response node consumed by [[flatness-branches]], [[future-asymptotics]], and [[observables]].
