# Zero-Residual Future Classes

For an ever-expanding zero-residual background, the rigid response has asymptotic dilution \(a^{-2\nu}\). Comparing that exponent with matter gives the exact conditional future classes, including acceleration, coasting, matter domination, and the presence or absence of a power-law event horizon.

Let the separately conserved response satisfy the hypotheses of [[causal-scale-theory/theorems/rigid-sech-response-identities|the rigid response theorem]], and suppose the background also contains noninteracting matter and radiation but no constant residual. As \(x=N-N_c\to+\infty\),

$$
\operatorname{sech}^2(\nu x)
\sim4e^{-2\nu x},
$$

so

$$
\boxed{
\rho_X\sim a^{-2\nu},
\qquad
w_X\longrightarrow-1+\frac{2\nu}{3}.}
$$

Matter and radiation scale as \(a^{-3}\) and \(a^{-4}\). Therefore:

- if \(0<\nu<3/2\), the response eventually dominates matter;
- if \(\nu=3/2\), response and matter have the same leading dilution;
- if \(\nu>3/2\), matter eventually dominates the response.

In the response-dominated regime \(0<\nu<3/2\), the Friedmann equation gives \(H\propto a^{-\nu}\), hence

$$
\boxed{a(t)\sim t^{1/\nu}.}
$$

It follows that:

- \(0<\nu<1\) gives asymptotic power-law acceleration;
- \(\nu=1\) gives asymptotic coasting;
- \(1<\nu<3/2\) gives response-dominated deceleration.

For this power-law future,

$$
\int^\infty\frac{\mathrm dt}{a(t)}
$$

converges exactly when \(0<\nu<1\). Thus the accelerating power-law class has a future event horizon, while the coasting and decelerating zero-residual classes have divergent future conformal time if expansion continues forever.

At \(\nu\geq3/2\), the matter-dominated leading behavior is nonaccelerating. A positive constant residual eventually dominates every class and produces de Sitter behavior; a negative residual can instead force a turnaround. Those are different sector assumptions, not corrections to the response theorem.

The asymptotic class does not determine whether a finite interval of acceleration occurred. That requires the full energy budget and [[causal-scale-theory/theorems/acceleration-condition|the acceleration condition]].
