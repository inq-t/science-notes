# Soldering Three Scale Characters

The half-sided-modular affine coordinate, the trace capacity of a Connes-core cut, and the discriminant depth of the symmetric real $A_2$ degeneration each carry an exact exponential character. Their equality is not a theorem of any one construction; it is a clean fiber-product solder that can be adopted and then tested by a physical realization. On that solder, increasing affine scale and increasing core capacity are exactly balanced by decreasing discriminant, so $N\to+\infty$ can mean both infinite semifinite capacity and collapse of positive sheet-distinction to $\mathbb C\mathbf1$. This is a precise algebraic relation, not yet an identification with proper time, FLRW expansion, entropy, area, or energy flux.

## The three characters

The constructions begin independently.

For the positive translation parameter $r$ of [[half-sided-modular-tunnel|a half-sided-modular tunnel]], choose $r_*>0$ and define

$$
\chi_{\mathrm{aff}}(r):=\frac r{r_*}.
$$

The affine modular relation

$$
\Delta^{-it}U(r)\Delta^{it}=U(e^{2\pi t}r)
$$

gives $\chi_{\mathrm{aff}}=e^N$ when $N=2\pi t=\log(r/r_*)$. This fixes a logarithmic coordinate inside the represented affine group; it does not make modular parameter $t$ into proper time.

For the spectral projections $e_N$ of [[core-spectral-wall|the core spectral wall]], choose $e_0$ with $\tau(e_0)=1$ and define

$$
\chi_{\mathrm{core}}(e_N)
:=
\frac{\tau(e_N)}{\tau(e_0)}.
$$

Trace scaling gives $\chi_{\mathrm{core}}(e_N)=e^N$. Here $N$ is logarithmic semifinite trace-capacity.

For the symmetric real cubic

$$
p_t(u)=u^3-t^2u,
\qquad
\Delta_{A_2}(t)=-4t^6,
$$

choose $t_*>0$ and define the inverse discriminant character

$$
\chi_{A_2}(t)
:=
\left(\frac{|\Delta_{A_2}(t_*)|}{|\Delta_{A_2}(t)|}\right)^{1/6}
=\frac{t_*}{t}.
$$

Along $t=t_*e^{-N}$, the cubic discriminant formula gives $\chi_{A_2}=e^N$. [[algebra/a2-positive-completion|The $A_2$ positive-completion theorem]] separately interprets the finite fibers and cusp endpoint. The exponent $1/6$ is fixed by the quasihomogeneous discriminant on this ray; it is not a fitted cosmological exponent.

## The fiber-product solder

Define the matched locus

$$
\boxed{
\mathscr S
:=
\left\{
(r,e_N,t):
\frac r{r_*}
=
\frac{\tau(e_N)}{\tau(e_0)}
=
\left(\frac{|\Delta_{A_2}(t_*)|}{|\Delta_{A_2}(t)|}\right)^{1/6}
\right\}.}
$$

Equivalently, a point of $\mathscr S$ is labelled by one additive coordinate $N$ satisfying

$$
\boxed{
\frac{r(N)}{r_*}
=
\frac{\tau(e_N)}{\tau(e_0)}
=
\left(\frac{|\Delta_*|}{|\Delta_N|}\right)^{1/6}
=e^N.}
$$

Once this matching is declared, its consequences are exact:

$$
\frac{\mathrm d}{\mathrm dN}\log r(N)=1,
\qquad
\frac{\mathrm d}{\mathrm dN}\log\tau(e_N)=1,
\qquad
\frac{\mathrm d}{\mathrm dN}\log|\Delta_N|=-6,
$$

and

$$
\boxed{
\left(\frac{\tau(e_N)}{\tau(e_0)}\right)^6
\frac{|\Delta_N|}{|\Delta_*|}=1.}
$$

The last equation is a character balance, not a conservation law for energy, entropy, information, or causal charge. It compares three dimensionless multiplicative characters and nothing else.

## What the solder constructs

Once adopted, the solder removes relative reparameterization freedom among three already exact pointed one-parameter families. It gives:

- one compositional logarithmic coordinate;
- a fixed relative orientation among affine dilation, core capacity, and $A_2$ degeneration;
- a sixth-power invariant determined by the cubic discriminant weight; and
- an exact common base over which a later realization functor can be required to commute.

It does not prove that the three source families describe the same physical process. That assertion is precisely the extra matching datum encoded by $\mathscr S$. A physical theorem would have to construct maps from one upstream object into all three registers and show that the displayed equality is natural, rather than impose it after the fact.

The solder also does not select the logistic density or its width $\nu$ in the core spectral wall. Core trace scaling fixes the coefficient of $N$ in $\log\tau(e_N)$; the $A_2$ discriminant fixes the coefficient $-6$ in $\log|\Delta_N|$. Neither fixes a state-space response profile.

## Infinity and nothing in particular

On $\mathscr S$,

$$
N\to+\infty
\quad\Longrightarrow\quad
r(N)\to+\infty,
\qquad
\tau(e_N)\to+\infty,
\qquad
|\Delta_N|\to0.
$$

The three limits say different things. The affine register has unbounded dilation depth. The pointed core filtration exhausts a type-$\mathrm{II}_\infty$ carrier whose identity has infinite trace. Along the selected symmetric real ray, the $A_2$ positive observable algebra loses sheet distinctions and reaches $\mathbb C\mathbf1$ at the triple-root cusp. Hence the mathematically disciplined version of the philosophical proposal is:

> Infinite scale-capacity and no positive distinction of sheets can be opposite presentations of one soldered boundary.

“Nothing” here is neither the zero algebra nor the absence of structure. It is **nothing in particular** under the chosen positive observable functor: only the unit survives, while the nonreduced $A_2$ source retains the algebraic reason that distinctions disappeared. Conversely, the infinity is infinity of semifinite tracial capacity, not automatically an infinity of particles, spatial volume, duration, or energy.

This conjunction is stronger than a metaphor and weaker than a cosmology. It is an exact theorem on the declared fiber product $\mathscr S$ and an open claim that nature realizes that fiber product.

## The physical commutative square still owed

A physical wall would have to supply a common source object $\mathfrak P_N$ and natural maps making a diagram of the following type commute:

$$
\begin{array}{ccc}
\mathfrak P_N &\longrightarrow& (\mathcal C,e_N,\Omega_d)\\
\big\downarrow && \big\downarrow\scriptstyle{\log\tau(e_N)}\\
(\Sigma_N,\mathcal A_N,\omega_N) &\longrightarrow& \mathbb R_N
\end{array}
$$

together with compatible maps to the HSMI and $A_2$ registers. The lower-left object must be a Lorentzian causal realization, not merely a relabelled spectral projection. The horizontal physical map must supply locality, source tangents, records, and independently normalized area if those are claimed.

Failure of that square would leave the three characters mathematically exact but physically unrelated. Success would still leave the [[program-core/causal-capacity-equivalence|state--area--gravity weld]] and the [[program-core/record-scale-soldering|record--scale orientation]] as separate theorems.
