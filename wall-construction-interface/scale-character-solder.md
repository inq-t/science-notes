# Soldering Scale Coordinates by One Character

The half-sided-modular affine parameter, the trace capacity of a Connes-core cut, and the discriminant depth of the symmetric real $A_2$ degeneration each admit an equivariant positive scale coordinate governed by the same character $\chi(s)=e^s$ of the additive scale group. Their equality is a clean fiber-product solder that can be adopted and then tested by a physical realization. An optional binary extension exposes a genuine normalization fork: identity matching to projection-coded log odds gives \(\nu=1/2\), while identity matching to the normalized-involution parameter gives \(\nu=1\). A separate nondegenerate incoming-density law selects the first branch's width within the logistic family without selecting its readout generator. These are precise algebraic consequences of proposed solders, not yet identifications with proper time, FLRW expansion, entropy, area, energy flux, or physical mass.

**Status: [EXACT — EQUIVARIANT COORDINATES]; [CONSTRUCTION AXIOM — THREE-REGISTER SOLDER]; [CONSTRUCTION AXIOM — OPTIONAL BINARY EXTENSIONS]; [OPEN CONSTRUCTION — PHYSICAL NATURALITY].**

## One character and three equivariant coordinates

The common character is

$$
\chi:(\mathbb R,+)\longrightarrow(\mathbb R_{>0},\times),
\qquad
\chi(s):=e^s.
$$

The three pointed constructions begin independently and carry actions of this additive parameter.

For the positive translation parameter $r$ of [[half-sided-modular-tunnel|a half-sided-modular tunnel]], choose $r_*>0$ and define

$$
\xi_{\mathrm{aff}}(r):=\frac r{r_*}.
$$

The affine modular relation

$$
\Delta^{-it}U(r)\Delta^{it}=U(e^{2\pi t}r)
$$

gives $\xi_{\mathrm{aff}}(e^s r)=\chi(s)\xi_{\mathrm{aff}}(r)$. Hence $\xi_{\mathrm{aff}}=e^N$ when $N=2\pi t=\log(r/r_*)$. The translation parameter itself obeys the additive law $U(r_1)U(r_2)=U(r_1+r_2)$, so $r/r_*$ is not being called a character of that translation group. The modular dilation action makes it an equivariant scale coordinate. This does not make modular parameter $t$ into proper time.

For the spectral projections $e_N$ of [[core-spectral-wall|the core spectral wall]], choose $e_0$ with $\tau(e_0)=1$ and define

$$
\xi_{\mathrm{core}}(e_N)
:=
\frac{\tau(e_N)}{\tau(e_0)}.
$$

Trace scaling gives

$$
\xi_{\mathrm{core}}(e_{N+s})
=\chi(s)\xi_{\mathrm{core}}(e_N),
\qquad
\xi_{\mathrm{core}}(e_N)=e^N.
$$

Here $N$ is logarithmic semifinite trace-capacity for the selected pointed filtration.

For the symmetric real cubic

$$
p_t(u)=u^3-t^2u,
\qquad
\Delta_{A_2}(t)=-4t^6,
$$

choose $t_*>0$ and define the inverse-discriminant scale coordinate

$$
\xi_{A_2}(t)
:=
\left(\frac{|\Delta_{A_2}(t_*)|}{|\Delta_{A_2}(t)|}\right)^{1/6}
=\frac{t_*}{t}.
$$

Under $t\mapsto e^{-s}t$,

$$
\xi_{A_2}(e^{-s}t)=\chi(s)\xi_{A_2}(t).
$$

Along $t=t_*e^{-N}$, the cubic discriminant formula therefore gives $\xi_{A_2}=e^N$. [[algebra/a2-positive-completion|The $A_2$ positive-completion theorem]] separately interprets the finite fibers and cusp endpoint. The exponent $1/6$ is fixed by the quasihomogeneous discriminant on this ray; it is not a fitted cosmological exponent.

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

The last equation is a scale-ratio balance, not a conservation law for energy, entropy, information, or causal charge. It compares three dimensionless equivariant coordinates governed by one character and nothing else.

## Extending the solder: the binary normalization fork

The binary contexts in [[core-spectral-wall|the core spectral wall]] carry two equally exact affine coordinates whose normalization depends on the chosen binary generator. Let \(P_+\) be the positive-outcome projection and let \(Q:=2P_+-\mathbf 1\) be the normalized involution. For

$$
Z(N)
=
\frac12\left[1+\tanh\!\bigl(\nu(N-N_c)\bigr)\right],
$$

define the projection-coded log-odds coordinate and the normalized-involution coordinate by

$$
\alpha(N;N_c)
:=
\log\frac{Z(N)}{1-Z(N)}
=2\nu(N-N_c),
\qquad
\theta(N;N_c)
:=
\frac12\alpha(N;N_c)
=\nu(N-N_c).
$$

Here \(\alpha\) is the natural parameter when the sufficient statistic is the idempotent \(P_+\in\{0,1\}\), whereas \(\theta\) is the parameter used by [[binary-information-geometry/balanced-exponential-family|the balanced binary exponential family]] for the normalized involution \(Q\in\{-1,+1\}\). The normalized states agree after \(\alpha=2\theta\), because the scalar part in \(P_+=(\mathbf1+Q)/2\) disappears on normalization. The two coordinates therefore describe the same probability family but not the same generator normalization.

The corresponding core-capacity difference is

$$
\zeta_{\mathrm{cap}}(N;N_c)
:=
\log\frac{\tau(e_N)}{\tau(e_{N_c})}
=N-N_c.
$$

There are consequently two different identity-equivariant extensions. The **projection-coded branch** requires

$$
\boxed{
\alpha(N;N_c)
=
\zeta_{\mathrm{cap}}(N;N_c).}
\tag{S1P}
$$

If adopted, it exactly fixes

$$
\boxed{
2\nu
=
\frac{\mathrm d}{\mathrm dN}\log\tau(e_N)
=1,
\qquad
\nu=\frac12.}
\tag{S2P}
$$

The **normalized-involution branch** instead requires

$$
\boxed{
\theta(N;N_c)
=
\zeta_{\mathrm{cap}}(N;N_c),}
\tag{S1Q}
$$

and therefore fixes

$$
\boxed{\nu=1.}
\tag{S2Q}
$$

Both are strict identity maps between pointed additive torsors. Thus “strict equivariance” alone does not remove the factor of two: one must first say which generator normalization carries the binary action. Because the core input \(e_N\) is itself a projection, (S1P) is the type-matched projection-to-projection candidate. That observation motivates the choice but does not derive a physical comparison map from the core.

## A boundary law that selects the projection-branch value

A separate construction axiom can select the same width as one side of the fork without selecting a physical binary generator or calling either parameter uniquely canonical. Let \(d_{\nu,N_c}\) be the Radon--Nikodym density of the normal state relative to canonical core trace. Since

$$
d_{\nu,N_c}(N)
=
e^{-N}q_{\nu,N_c}(N)
\sim
2\nu e^{-2\nu N_c}e^{(2\nu-1)N}
\qquad(N\to-\infty),
$$

the proposed **[CONSTRUCTION AXIOM — NONDEGENERATE INCOMING CORE DENSITY]**

$$
\boxed{
0<\lim_{N\to-\infty}d_{\nu,N_c}(N)<\infty}
\tag{S3}
$$

holds within the logistic family exactly when \(\nu=1/2\). It says that the state density is asymptotically neither erased nor amplified relative to the canonically normalized trace capacity at the incoming end. It is not a theorem of core normality, and the ideal boundary \(N=-\infty\) is not itself a finite core projection.

The exact critical variable is the mismatch of incoming exponents,

$$
\varepsilon_{\mathrm{in}}
:=
2\nu-\chi_{\mathrm{core}}
=2\nu-1.
$$

It gives the boundary-class trichotomy

$$
\boxed{
\lim_{N\to-\infty}d_{\nu,N_c}(N)
=
\begin{cases}
+\infty,&\varepsilon_{\mathrm{in}}<0,\\
e^{-N_c},&\varepsilon_{\mathrm{in}}=0,\\
0,&\varepsilon_{\mathrm{in}}>0.
\end{cases}}
\tag{S4}
$$

Translations of the pointed origin change the finite middle value but preserve all three classes. Thus \(2\nu=1\) is a genuine codimension-one **rate-matching wall**: the pointing weight and core capacity have equal incoming character. It is a more precise candidate for a “sweet spot” than harmonic resonance. A continuous family can cross this wall without any discontinuity at finite \(N\), but the relative-density half-factor detects a discrete change of Fredholm phase.

Indeed, on the translation-Haar carrier \(L^2(\mathbb R,\mathrm dN)\), define

$$
B_{\nu,N_c}
:=
\partial_N
-\partial_N\log\sqrt{d_{\nu,N_c}}
=
\partial_N+\frac12
+\nu\tanh\!\bigl(\nu(N-N_c)\bigr).
\tag{S4a}
$$

Its asymptotic coefficients are \(1/2-\nu\) and \(1/2+\nu\). The scalar sign-at-infinity theorem therefore gives

$$
\boxed{
\operatorname{ind}B_{\nu,N_c}
=
\begin{cases}
0,&\nu<1/2,\\
\text{undefined: non-Fredholm},&\nu=1/2,\\
1,&\nu>1/2.
\end{cases}}
\tag{S4b}
$$

At the middle value, \(\sqrt d\) is a bounded but non-normalizable incoming threshold solution and zero reaches the essential spectrum of \(B^*B\). [[contemporary-puzzles/yang-mills-mass-gap/indexed-scale-wall-and-the-causal-grain|The indexed-scale-wall theorem]] supplies the domains and proof. Thus \(\varepsilon_{\mathrm{in}}\) is simultaneously a boundary-class exponent and the sign that distinguishes two Fredholm phases. The critical member itself has no index, and transporting this reduced transition to a physical causal grain remains an open carrier problem.

This index statement depends on its declared carrier. Here \(d=e^{-N}q\) is treated as a density relative to core capacity and \(\sqrt d\) is placed on translation-Haar \(L^2(\mathrm dN)\). If the same differential expression is instead placed on the natural core-trace carrier \(L^2(e^N\mathrm dN)\), multiplication by \(e^{N/2}\) conjugates it to the ordinary probability factor \(A_\nu\), whose index remains \(+1\) for every \(\nu>0\). Core normality alone therefore does not select the phase-changing carrier; a physical realization must justify why translation-Haar relative density, rather than core-trace density, is the operative presentation.

At the selected value, the probability-density and half-density slopes are

$$
\lim_{N\to-\infty}\partial_N\log q
=2\nu
=1,
\qquad
\lim_{N\to-\infty}\partial_N\log\sqrt q
=\nu
=\frac12.
$$

Thus the probability-density exponent matches the trace-capacity-density character, while the amplitude exponent matches its half-density character. For the Witten--Darboux convention \(W=-\partial_N\log\sqrt q\), the incoming limit is \(W\to-1/2\). At the same selected value,

$$
d_{\frac12,N_c}(N)
=
\frac{e^{-N_c}}{(1+e^{N-N_c})^2},
\qquad
q_{\frac12,N_c}
=
G_{NN}^{\mathrm{bin}}.
$$

The last equality concerns coordinate coefficients in the canonically normalized \(N\)-coordinate, not geometric types: \(q\,\mathrm dN\) is a probability measure and \(G_{NN}^{\mathrm{bin}}\,\mathrm dN^2\) is a metric. Within the logistic family, (S1P), the boundary law (S3), and equality of these numerical coefficients are equivalent consequences of \(\nu=1/2\); they are not three independent pieces of evidence. [[contemporary-puzzles/yang-mills-mass-gap/pointing-coercivity-and-the-flat-partner-law|Pointing coercivity and the flat-partner law]] gives the associated sharp scale-shadow gap \(\nu^2=1/4\). The involution branch instead gives edge \(1\). Neither branch proves that its proposed capacity-to-readout comparison is physically compulsory.

## What the solder constructs

Once adopted, the solder removes relative reparameterization freedom among three already exact pointed equivariant families. It gives:

- one compositional logarithmic coordinate;
- a fixed relative orientation among affine dilation, core capacity, and $A_2$ degeneration;
- a sixth-power invariant determined by the cubic discriminant weight; and
- an exact common base over which a later realization functor can be required to commute.

It does not prove that the three source families describe the same physical process. That assertion is precisely the extra matching datum encoded by $\mathscr S$. A physical theorem would have to construct maps from one upstream object into all three registers and show that the displayed equality is natural, rather than impose it after the fact.

The original three-register solder does not select the logistic density or its width $\nu$ in the core spectral wall. Core trace scaling fixes the coefficient of $N$ in $\log\tau(e_N)$; the $A_2$ discriminant fixes the coefficient $-6$ in $\log|\Delta_N|$. The optional binary extension fixes a width only after the binary generator normalization is declared: (S1P) gives \(\nu=1/2\), (S1Q) gives \(\nu=1\), and a general orientation-preserving torsor automorphism leaves a positive scale factor free. The independent boundary axiom (S3) selects \(\nu=1/2\) within the logistic family.

## Infinity and nothing in particular

The finite matched locus $\mathscr S$ does not contain $r=+\infty$, $t=0$, or an object denoted $e_\infty$. In the asymptotic boundary of a chosen partial compactification $\overline{\mathscr S}$, the parameterized curve has

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

This conjunction is stronger than a metaphor and weaker than a cosmology. The finite scale-ratio identities are exact on the declared fiber product $\mathscr S$; the endpoint statement is their asymptotic boundary correspondence in $\overline{\mathscr S}$. It remains an open claim that nature realizes either structure.

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

Failure of that square would leave the three equivariant coordinates mathematically exact but physically unrelated. Success would still leave the [[program-core/causal-capacity-equivalence|state--area--gravity weld]] and the [[program-core/record-scale-soldering|record--scale orientation]] as separate theorems.
