# Radial Conditional Differentiation

A smooth spherical conditional average can have regular derivatives even when its coordinate-level score and Hessian diverge separately. Hidden integration by parts removes those coordinate singularities exactly, at the cost of higher hidden derivatives. In the quaternionic case, a fourth hidden derivative can change the endpoint marginal curvature while all lower endpoint jets remain unchanged. This is a calculus of the readout, not a spectral-gap theorem.

**Status: exact identities for the stated smooth spherical averaging operator, with an exact lower-jet obstruction.** The sphere, its measure, invariant coordinates and averaging map are supplied. The formulas hold in every integer dimension \(d\ge2\); they do not select three spatial dimensions or a physical unit of scale.

## The averaging operator and its domain

Let \(a\in[-1,1]\), \(h=1-a^2\), and let \((b,\eta)\)
be two coordinates of a uniform point on the unit sphere
\(S^d\subset\mathbb R^{d+1}\). Their law on the unit disk is
\[
d\omega_d=\frac{d-1}{2\pi}
q^{(d-3)/2}\,db\,d\eta,\qquad
q=1-b^2-\eta^2\ge0.
\tag{RD1}
\]
It is uniform when \(d=3\). Define the linear averaging map
\[
(\mathcal R_dF)(a)=\int
F(a,b,\sqrt h\,\eta)\,d\omega_d(b,\eta).
\tag{RD2}
\]
Here \(F\) has a \(C^4\) representative on a neighborhood of
the compact orbit body
\[
\mathcal B=\{(a,b,z): |a|,|b|\le1,\quad
z^2\le(1-a^2)(1-b^2)\}.
\]
Every invariant polynomial is admissible. All partial
derivatives of \(F\) below hold the other \((a,b,z)\)
coordinates fixed; they are not derivatives at fixed
\((b,\eta)\). Write \(I_d\) for integration with (RD1)
after evaluation at \(z=\sqrt h\,\eta\).

## Hidden integration by parts removes the divisions

For a smooth disk integrand \(G\), integration in \(\eta\)
gives
\[
I_d[\eta G]=\frac1{d-1}I_d[q\,\partial_\eta G],\qquad
I_d[\eta qG]=\frac1{d+1}I_d[q^2\partial_\eta G].
\tag{RD3}
\]
The boundary factors are respectively
\(q^{(d-1)/2}\) and \(q^{(d+1)/2}\), both vanishing at
the disk edge, including for \(d=2\). No boundary flux is
discarded. These formulas also follow by a cutoff and its
dominated limit at the two tips of the disk.

Put \(R=\mathcal R_dF\). Direct differentiation on
\(|a|<1\) gives \(R'=I_d[F_a-a\eta F_z/\sqrt h]\).
Applying the first identity in (RD3) to \(F_z\) removes
the square-root denominator. Differentiating once more,
and applying both identities, yields
\[
\boxed{R'=I_d\left[F_a-\frac a{d-1}qF_{zz}\right],}
\tag{RD4}
\]
\[
\boxed{R''=I_d\left[
F_{aa}-\frac{2a}{d-1}qF_{azz}-\frac q{d-1}F_{zz}
+\frac{a^2q^2}{(d-1)(d+1)}F_{zzzz}\right].}
\tag{RD5}
\]
There are no negative powers of \(h\). The declared \(C^4\)
bounds give dominated endpoint limits and extend these
identities to one-sided derivatives at \(a=\pm1\).

The terms containing hidden derivatives are forced by
differentiating the same averaging map. Dropping them is
not a change of coordinates: it changes the derivative
of the returned function. Nevertheless (RD5) is one exact
regular representation, not a uniqueness assertion about
every possible representation of the averaging operator.

## The endpoint remembers a fourth hidden jet

At \(a=s=\pm1\), all integrands are evaluated at
\((s,b,0)\). Let \(d\mu_d(b)\) be the first-coordinate law
of the uniform \(S^d\). Conditional spherical moments give
\[
E[q\mid b]=\frac{d-1}{d}(1-b^2),\qquad
E[q^2\mid b]=\frac{d^2-1}{d(d+2)}(1-b^2)^2.
\]
Thus
\[
R'(s)=\int\left[F_a-\frac{s(1-b^2)}dF_{zz}\right]d\mu_d(b),
\tag{RD6}
\]
\[
\begin{aligned}
R''(s)=\int\bigg[&F_{aa}-\frac{2s(1-b^2)}dF_{azz}
-\frac{1-b^2}dF_{zz}\\
&+\frac{(1-b^2)^2}{d(d+2)}F_{zzzz}\bigg]d\mu_d(b).
\end{aligned}
\tag{RD7}
\]
For \(F>0\), let \(\chi=\sqrt R\). Its latitude curvature is
\[
(\log\chi)''=\frac{RR''-(R')^2}{2R^2}.
\tag{RD8}
\]

The fourth hidden jet cannot be inferred from the endpoint
conditional law and lower invariant jets. For \(d=3\), take
\[
F_\varepsilon=1+\varepsilon z^4,\quad \varepsilon>-1.
\]
This density is strictly positive on \(\mathcal B\), and
\(E_{S^3}\eta^4=1/8\) gives
\[
R_\varepsilon=1+\frac\varepsilon8(1-a^2)^2,
\qquad (\log\sqrt{R_\varepsilon})''(\pm1)=\varepsilon/2.
\tag{RD9}
\]
Along \(z=0\), its invariant jets of total order at most
three equal those of \(F_0=1\). Its endpoint curvature
nevertheless has either sign. Overall probability
normalization changes none of these logarithmic derivatives.
This disproves a universal sign criterion using only those
endpoint data, not criteria using a whole neighborhood or
additional dynamics.

## Why separate score bounds can diverge

Let \(F=\psi^2>0\) and
\(\phi(a,b,\eta)=\log\psi(a,b,\sqrt h\,\eta)\).
With the actual normalized hidden law
\(d\beta_a=\psi^2d\omega_d/R\), direct differentiation gives
\[
(\log\chi)''=E_{\beta_a}[\phi_{aa}]
+2\operatorname{Var}_{\beta_a}(\phi_a).
\tag{RD10}
\]
These derivatives do hold \((b,\eta)\) fixed.
The identity is a specialization of
[[rg-covariance-residue/conditioned-source-transport|conditional score response]].

Set
\[
C_{s,d}=\frac1d
\frac{\int(1-b^2)\psi_z(s,b,0)^2\,d\mu_d(b)}
{\int\psi(s,b,0)^2\,d\mu_d(b)}\ge0.
\]
Expanding both the numerator and the normalized hidden law
at \(z=0\) proves
\[
h\operatorname{Var}_{\beta_a}(\phi_a)\longrightarrow C_{s,d},
\qquad h E_{\beta_a}[\phi_{aa}]\longrightarrow-2C_{s,d}
\quad(a\to s).
\tag{RD11}
\]
For example, the singular term in \(\phi_a\) is
\(-a\eta\psi_z/(\sqrt h\psi)\). In the second identity,
the derivative of the conditional weight supplies the
additional \(2(\psi_z/\psi)^2\) term. Omitting that weight
change would miss the cancellation.

If \(C_{s,d}>0\), neither summand in (RD10) is uniformly
bounded at the endpoint, although (RD8) remains finite.
The regular formulas estimate their combination. This
chart score is not automatically an inherited physical
gradient or a spacetime rate. A comparison with such an
operator must retain its specified metric and transport.
