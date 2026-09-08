# Certifying the Ground Marginal and Every Preparation Time

A weighted harmonic norm and exact rational interval checks certify strict latitude log-concavity of the complete two-plaquette marginal at equal unit electric and magnetic coefficients, for every positive preparation time and at the ground-state limit. A cubic initial-layer estimate, full-residual comparison on compact time intervals and contraction toward the certified ground cover the entire trajectory, including both latitude poles. The proof controls the correlated curvature remainder without mistaking cutoff convergence or time samples for a bound.

**Status: computer-assisted fixed-system theorem, with analytic tail and heat bounds; no continuum Yang--Mills construction or mass-gap claim.**

The operator is the supplied compact system in
[[two-plaquette-vacuum-and-relational-state|the full relational construction]],
not a reconstructed field theory. Fix the dimensionless coefficients
\(\kappa=\lambda=1\), and write
\[
H=K+2-M,\qquad M=a+b.
\tag{GC1}
\]
All allowed simultaneous-conjugation-invariant channels are retained.
The parameter below is Euclidean preparation duration, not a derived
Lorentzian clock.

## A norm that sees the omitted harmonics

Let \(p_{nm}\) be the vector of normalized coefficients with
\(0\le k\le\min(n,m)\), using (TP15)--(TP19), and define
\[
\|p\|_X=\sum_{n,m\ge0}2^{n+m}\|p_{nm}\|_2,
\qquad Q=I-|1\rangle\langle1|.
\tag{GC2}
\]
Here \(Q\) removes the Haar constant, not the interacting ground
state. The weights are a proof device, not a physical scale.

The free operator preserves each block. Its eigenvalues there are
\[
\tfrac34[n(n+2)+m(m+2)]+j(j+1),
\quad j=|n-m|/2,\ldots,(n+m)/2.
\tag{GC3}
\]
In particular, \(K\ge3Q\). Since \(0\le2-M\le4\), min--max
and the constant trial vector give
\[
0\le E_0\le2,\qquad E_1\ge3,\qquad E_1-E_0\ge1.
\tag{GC4}
\]
The ground state is simple and strictly positive by compact ellipticity.
These finite-system estimates precede the new marginal certificate;
they are not an infinite-volume gap argument.
The spectral bounds here concern the invariant carrier in (TP1).
They are not bounds for every boundary-charged sector of the raw
seven-link operator. The positive ground is gauge invariant, but
[[interacting-reference-and-spectral-product-control#A block certificate must retain boundary charges|using this system as an assembly block]]
requires those additional sectors in its response certificate.

Each adjacent-block map of multiplication by \(a\) or \(b\) has
norm at most \(1/2\), by (TP19). Raising total degree multiplies
the weight by two; lowering divides it by two. Consequently
\[
\|M\|_{X\to X}\le\tfrac52,\qquad
\|(K+2-E_0)^{-1}Q\|_{X\to X}\le\tfrac13.
\tag{GC5}
\]
No coordinate derivative or unspecified Sobolev constant enters.

Normalize the actual ground vector \(f\) by \(\langle1,f\rangle=1\).
Its nonconstant part solves a contraction equation with norm at most
\(5/6\). The forcing \((K+2-E_0)^{-1}QM1\) has \(X\)-norm
at most \(2/3\), so
\[
\|Qf\|_X\le4,\qquad \|f\|_X\le5,
\qquad \|f\|_2^2\le17.
\tag{GC6}
\]
This also proves that the true vector belongs to \(X\): the Neumann
solution is in \(X\subset L^2\), and agrees with the actual ground
vector by the separate \(L^2\) contraction bound \(2/3\).
Exponential harmonic regularity has not been assumed.

## A full residual controls the true vector

Take any finite real trial \(p\) with \(p_{000}=1\), an approximate
energy \(E_*\), and its **full** residual
\[
r=(H-E_*)p.
\tag{GC7}
\]
This includes the magnetic neighbors outside the trial cutoff.
Suppose exact enclosures supply
\(\delta\ge\|r\|_2/\|p\|_2\) and \(E_*+\delta<3\).
The spectral-distance inequality and (GC4) then imply
\(|E_*-E_0|\le\delta\): no excited eigenvalue can account for
that residual interval.

Subtract the nonconstant equations for \(f\) and \(p\). Their
constant coefficients agree, so
\[
(K+2-E_0)Q(f-p)
=QM Q(f-p)+(E_0-E_*)Qp-Qr.
\]
Using (GC5) and absorbing the contraction gives
\[
\boxed{\|f-p\|_X\le
\eta:=2\bigl(\delta\|Qp\|_X+\|Qr\|_X\bigr).}
\tag{GC8}
\]
The factor two is \((3-5/2)^{-1}\). A small residual without
its weighted bound does not establish this estimate numerically.

## Conditional integration has explicit derivative bounds

For real invariant vectors put
\[
\mathcal B(p,q)(a)=\int p(x,y)q(x,y)\,dy,
\qquad a=\tfrac12\operatorname{Tr}x.
\tag{GC9}
\]
Different hidden harmonic degrees \(m\) are orthogonal even at
fixed \(x\). On one \((n,m)\) block, the normalized \(S^3\)
addition theorem gives
\[
\sup_x\|p_{nm}(x,\cdot)\|_{L^2_y}
\le(n+1)\|p_{nm}\|_2.
\]
The dimension of the full degree-\(n\) spherical harmonic space
is \((n+1)^2\); restriction to its invariant subspace cannot
increase this evaluation bound. A surviving cross marginal
is a central polynomial in \(a\) of degree at most \(d=n+n'\),
with supremum at most
\((n+1)(n'+1)\|p_{nm}\|_2\|q_{n'm}\|_2\).

The classical Markov polynomial inequalities have derivative
factors \(T_0(d)=1\), \(T_1(d)=d^2\), and
\(T_2(d)=d^2(d^2-1)/3\) on \([-1,1]\).
See the mathematical statement in
[Bun and Thaler, section 5.3](https://privacytools.seas.harvard.edu/sites/g/files/omnuum6656/files/privacytools/files/duallowerbounds.pdf).
Combining these factors with the weights in (GC2) proves
\[
\|\partial_a^j\mathcal B(p,q)\|_\infty
\le C_j\|p\|_X\|q\|_X,
\qquad (C_0,C_1,C_2)=(1,75/8,525/4).
\tag{GC10}
\]
For completeness, maximize
\(\lfloor(d+2)^2/4\rfloor T_j(d)/2^d\).
The maxima occur at \(d=0,5,8\), respectively (the first is
also attained at other low degrees). Writing
\(A_d=\lfloor(d+2)^2/4\rfloor\), use
\(A_{d+1}/A_d\le(d+3)/(d+1)\). The successive ratios for
\(j=1,2\) are then at most
\((d+3)(d+1)/(2d^2)\) and
\((d+3)(d+2)/(2d(d-1))\), strictly below one for
\(d\ge5,8\). Only the stated finite prefixes need checking.

The absolutely convergent differentiated series proves (GC10)
also for infinite \(X\) vectors, uniformly at both endpoints.
Thus if \(R_p=\mathcal B(p,p)\) and
\(R_f=\mathcal B(f,f)\), (GC8) gives
\[
\|R_f^{(j)}-R_p^{(j)}\|_\infty\le
\epsilon_j:=C_j(2\|p\|_X\eta+\eta^2),\quad j=0,1,2.
\tag{GC11}
\]
These marginals use vacuum-coefficient-one normalization.
Changing their overall positive normalization does not change
\(\partial_a^2\log\sqrt R\).

## A polynomial sign certificate transfers to the full marginal

Orthogonality of the hidden radial and angular factors gives
the exact finite polynomial
\[
R_p(a)=\sum_{m,k}(1-a^2)^k
\left[\sum_n
\frac{p_{nmk}C_{n-k}^{k+1}(a)}{\sqrt{h_{n-k,k}}}\right]^2.
\tag{GC12}
\]
Let \(N_p=(R_p')^2-R_pR_p''\). If certified polynomial bounds
give \(N_p\ge b>0\), \(R_p\ge l>0\), and
\(\|R_p^{(j)}\|_\infty\le M_j\), then
\[
\begin{aligned}
|N_f-N_p|&\le
2M_1\epsilon_1+\epsilon_1^2
+M_0\epsilon_2+M_2\epsilon_0+\epsilon_0\epsilon_2=:D,\\
R_f&\ge l-\epsilon_0.
\end{aligned}
\tag{GC13}
\]
When \(D<b\) and \(\epsilon_0<l\),
\[
\boxed{\partial_a^2\log\sqrt{R_f}
\le-\frac{b-D}{2(M_0+\epsilon_0)^2}<0}
\tag{GC14}
\]
on the **whole** closed latitude interval. There is no sample-grid
assumption. Bernstein coefficients provide a convenient finite
certificate: after \(a=2s-1\), each polynomial is a convex
combination of its Bernstein coefficients for \(0\le s\le1\).
Interval coefficients with rational endpoints keep this step exact.

## The heat remainder can also be bounded explicitly

Let \(\mathsf N\) denote the total-degree operator \(n+m\), and
let \(W_r=r^{\mathsf N}\). Along
\(r=3^s\), \(0\le s\le1\), the weighted evolution has generator
\[
(\log3)\mathsf N-K-2+W_rMW_r^{-1}.
\]
Formula (GC3) implies \(K\ge\tfrac32\mathsf N\), whereas
\(\log3<3/2\). The symmetric part of the last term is
\(\tfrac12(r+r^{-1})M\), bounded above by
\(r+r^{-1}\le10/3\), since \(\|M\|_2\le2\).
An energy estimate therefore gives
\[
\|W_3e^{-H}\|_{2\to2}\le e^{4/3}.
\]
Prove this first on finite total-degree cutoffs; the bounds
are independent of cutoff, and strong convergence followed
by lower semicontinuity gives the full weighted estimate.
By Cauchy--Schwarz over blocks,
\[
\|v\|_X\le\tfrac95\|W_3v\|_2,
\qquad \|e^{-H}\|_{2\to X}<7.
\tag{GC15}
\]
The factor \(9/5\) is the square root of
\(\sum_{n,m}(2/3)^{2(n+m)}\).

Write the unit ground vector as \(\phi=cf\), with
\(c=\langle1,\phi\rangle>0\). By (GC6), \(c^{-2}\le17\).
For \(t\ge1\), define the scalar-rescaled prepared vector
\[
F_t=c^{-2}e^{tE_0}e^{-tH}1.
\]
Its ground component is exactly \(f\). Apply (GC15) on the
last unit interval and (GC4) on the earlier interval:
\[
\boxed{\|F_t-f\|_X
\le952e^{-(t-1)}.}
\tag{GC16}
\]
Here \(952=17\cdot7\cdot8\), using \(e^{E_0}\le e^2<8\)
and \(\|(I-|\phi\rangle\langle\phi|)1\|_2\le1\).
No approximate excited spectrum is used.

Consequently the same finite sign test (GC11)--(GC14) controls
the entire late preparation interval after replacing \(\eta\)
by \(\eta+952e^{-(T-1)}\). Normalizing \(e^{-tH}1\) in
\(L^2\) changes neither this sign nor the local probability law.
This is an additive estimate of the connected curvature,
precisely the quantity left after the
[[path-source-tilts-and-the-curvature-budget#A uniform fractional margin is impossible at late time|late source cancellation]].

## The completed fixed-coupling certificate

For the normalized actual Haar preparation
\(\psi_t=e^{-tH}1/\|e^{-tH}1\|_2\), let
\(\chi_t(a)=\sqrt{\int\psi_t(x,y)^2dy}\).
Define \(\chi_\infty\) from the unit ground vector. The
analytic bounds above and the exact arithmetic below prove
\[
\boxed{\partial_a^2\log\chi_t(a)\le-\frac1{1000}
\quad(-1\le a\le1,\quad 30\le t\le\infty).}
\tag{GC17}
\]
Thirty is a sufficient dimensionless preparation threshold,
not a sharp transition, physical age, or newly selected clock.
By the
[[conditional-fisher-coercivity/linear-tilted-sphere-coercivity#Concave radial amplitudes retain the same bound|concave-amplitude inequality]],
the actual marginal therefore satisfies
\[
\int(1-a^2)|g'(a)|^2\,d\nu_t
\ge\operatorname{Var}_{\nu_t}g,
\qquad d\nu_t\propto\chi_t^2\sqrt{1-a^2}\,da,
\tag{GC18}
\]
on the inherited conservative form domain throughout this range.
It is a marginal form bound, not a statement that the readout
has become autonomous under the full dynamics.

The focused
[[receipts/ground_marginal_certificate.py|exact-arithmetic certificate]]
first uses the existing solver only to propose a trial. Rounding
defines a new **exact rational** coefficient vector with
\(n,m\le8\), \(p_{000}=1\), and an exact rational \(E_*\).
No assertion about the solver's eigenvector error is trusted.
The remaining checks use rational interval arithmetic; integer
square-root enclosures cover the irrational matrix and basis
normalizations. Magnetic neighbors at cutoff nine are included.

The run checks the following loose rational bounds directly:

| Certified quantity | Sufficient bound |
|---|---|
| \(\|p\|_X,\ \|Qp\|_X\) | \(<1.9,\ <0.9\) |
| \(\delta,\ \|Qr\|_X\) | \(<10^{-10},\ <10^{-8}\) |
| \(R_p\) on \([-1,1]\) | \(>0.5\), with \(\|R_p\|_\infty<1.91\) |
| \(\|R_p'\|_\infty,\ \|R_p''\|_\infty\) | \(<1.17,\ <0.64\) |
| \(N_p=(R_p')^2-R_pR_p''\) | \(>0.018\) everywhere |

These bounds alone already suffice for (GC17). The actual
enclosures are sharper: the weighted residual is below
\(1.137\,10^{-10}\); (GC8) gives
\(\eta<2.274\,10^{-10}\). The degree-sixteen marginal and
degree-thirty numerator have positive Bernstein lower bounds,
with \(N_p>0.01824605\). The late tail in (GC16) is enclosed
using
\[
952e^{-29}\le
\frac{952}{\sum_{j=0}^{100}29^j/j!}<2.422\,10^{-10}.
\]
After adding both errors, (GC13) still gives
\(N_{F_t}>0.0182455\), and (GC14) gives a curvature upper
bound less than \(-0.0025273\), hence the deliberately weaker
\(-1/1000\) in (GC17).

All inequalities used for acceptance are rational comparisons,
not comparisons of the rounded decimal display. The script
also prints a hash of the exact trial so different proposal
environments can be distinguished. The calculation certifies
the finite arithmetic premises; (GC2)--(GC16) supply the proof
that they control the full compact carrier and the infinite
late-time interval. No novelty claim is made for the underlying
spectral, polynomial or weighted-semigroup techniques.

## The initial layer retains its cubic zero

An absolute time-independent error would lose the sign as
\(t\downarrow0\), because the true curvature starts at order
\(t^3\). Instead remove only the scalar potential constant,
put \(A=K-M\), and define
\[
P(t)=e^{-tA}1,\qquad
P_7(t)=\sum_{j=0}^7\frac{(-tA)^j1}{j!}.
\tag{GI1}
\]
This is not a reset marginal evolution. \(K\) generates a
contraction on \(X\), and \(\|M\|_X\le5/2\), so
\(\|e^{-tA}\|_X\le e^{5t/2}\). Every \(A^j1\) is a finite
harmonic polynomial in the domain of the next power.
Taylor's integral remainder therefore gives
\[
\|P(t)-P_7(t)\|_X
\le e^{5t/2}t^8\frac{\|A^8 1\|_X}{8!}.
\tag{GI2}
\]
No convergence of the infinite Taylor series is asserted.

The separate
[[receipts/initial_preparation_certificate.py|initial-layer certificate]]
computes these finite polynomials by both the complete harmonic
matrix and the rational coordinate operator (TP3)--(TP4), through
degree seven; the harmonic calculation also supplies degree eight
for the remainder.
It proves the coefficient-norm upper bounds
\[
\frac{\|A^j1\|_X}{j!}\le
(1,2,21/4,12,26,55,119,260,576)_j,
\qquad0\le j\le8.
\tag{GI3}
\]
On \(0\le t\le t_0=1/20\), these imply
\(\|P_7(t)\|_X<9/8\) and
\(\eta(t):=\|P-P_7\|_X\le(8/7)576t^8\), because
\(e^{5t/2}\le e^{1/8}\le8/7\).

For the conditional marginal, the exact coordinate moments are
\[
I_a[b^{2m}z^{2j}]
=(1-a^2)^j\frac{(2m)!(2j)!}
{4^{m+j}m!j!(m+j+1)!},
\tag{GI4}
\]
and odd hidden powers vanish. These follow by taking two
coordinates of a uniform \(S^3\) vector, with
\(z=\sqrt{1-a^2}\,y_3\). They include the relational channel;
in particular the amplitude's third Taylor coefficient contains
\(z/6\).

Let \(R_7=I_aP_7^2\) and \(N_7=(R_7')^2-R_7R_7''\).
Its coefficients of \(t^0,t^1,t^2\) vanish exactly, while
\[
N_7=\frac43t^3+\frac{16a-17}{3}t^4
+\left(\frac{73}{5}-\frac{508a}{15}
+\frac{32a^2}{3}\right)t^5+\cdots.
\tag{GI5}
\]
The polynomial ends at degree twenty-eight in time.
Bounding every term after \(t^4\) by the sum of the absolute
values of its latitude coefficients gives
\(N_7/t^3>59/100\) throughout the full initial interval.
All coefficients in this calculation are rational.

For \(N(P)=(\partial_a I_aP^2)^2-(I_aP^2)(\partial_a^2I_aP^2)\),
the bilinear estimates (GC10) give the quartic difference bound
\[
|N(P)-N(P_7)|\le
\left(C_1^2+C_2\right)
\left[(p+\eta)^4-p^4\right],\qquad p=9/8,
\quad C_1^2+C_2=14025/64.
\tag{GI6}
\]
Expand the four amplitude slots and use (GC10) in each term.
After dividing by \(t^3\), the upper bound increases with
\(t\); at \(t_0\) the receipt proves it is below \(13/50\).
Since \(\|P\|_X\le8/7\), this proves
\[
\boxed{N(P)\ge\frac3{10}t^3,\qquad
\partial_a^2\log\sqrt{I_aP^2}\le-\frac{t^3}{12}
\quad(0\le t\le1/20,\ -1\le a\le1).}
\tag{GI7}
\]
The scalar removed in (GI1) and subsequent normalization do
not change this curvature. The bound is strict for \(t>0\);
at \(t=0\) the marginal is Haar. In both cases the inherited
marginal form satisfies (GC18).

For a subsequent time-interval comparison the receipt also
encloses \(P_7(t_0)/\langle1,P_7(t_0)\rangle\), with its
constant coefficient exactly one. The actual coefficient
\(\langle1,P(t)\rangle\ge1\), as shown by
[[pointed-preparation-stability-and-the-volume-test#The two-plaquette preparation supplies the hypotheses|the positive coefficient evolution]].
Writing \(p_0=\langle1,P_7(t_0)\rangle\ge1\), the quotient error is
\[
\left\|\frac{P(t_0)}{\langle1,P(t_0)\rangle}
-\frac{P_7(t_0)}{p_0}\right\|_X
\le\left(1+\frac{\|QP_7(t_0)\|_X}{p_0}\right)\eta(t_0)
<2.822\,10^{-8}.
\tag{GI8}
\]
Indeed subtract the two nonconstant quotients; their constant
coefficients agree. This error, and any change from interval
coefficients to a rational trial, must be retained at the next
interval's initial point.

## Compact time intervals and a contractive final tail

Write the actual pointed preparation as
\(f_t=P(t)/\langle1,P(t)\rangle=1+g_t\). On each time interval
\([s,s+h]\), take an exact rational harmonic polynomial curve
\[
p_t=1+y_t=\sum_{j=0}^{12}p_jT_j(2(t-s)/h-1),
\qquad (p_t)_{000}=1,
\tag{GP1}
\]
with harmonic cutoff eight. Its full nonlinear residual is
\[
e_t=p_t'+Hp_t-(Hp_t)_{000}p_t.
\tag{GP2}
\]
The scalar potential shift cancels in this equation. Its
constant coefficient vanishes exactly; its nonconstant part
is the residual (PN3) of
[[pointed-preparation-stability-and-the-volume-test|pointed preparation stability]].
Multiplication into harmonic cutoff nine is retained. The
Chebyshev product identity and \(|T_j|\le1\) give uniform
bounds on both \(\|y_t\|_X\) and \(\|e_t\|_X\) from their
coefficient norms, rather than their sampled values.

If \(\sup_t\|y_t\|_X<1\) and the residual is at most
\(\epsilon\), (PN8) bounds the full-trajectory error on the
entire interval by
\[
\|f_t-p_t\|_X\le\max\{d_s,4\epsilon\},
\tag{GP3}
\]
where \(d_s\) includes the previous error and the change to
the new trial at the junction. The first junction retains
(GI8). No interpolation-accuracy assumption enters: a
numerical approximation proposes a rational curve, whose
residual and initial discrepancy are then checked independently.

Formula (GC12) now gives a bivariate polynomial
\(R_p(t,a)\). Tensor-product Bernstein coefficients enclose
\(R_p,R_p',R_p''\) and \(N_p=R_p'^2-R_pR_p''\) on the whole
time--latitude rectangle. Primes here still mean latitude
derivatives. Equations (GC11)--(GC14) transfer their sign to
the actual trajectory using (GP3).

The [[receipts/preparation_interval_certificate.py|complete interval certificate]]
passes sixteen rectangles of width at most \(1/4\), covering
\([1/20,4]\). Their largest certified \(X\) error is below
\(4.843\,10^{-8}\). After all residual, junction and derivative
errors, the smallest remaining numerator margin is above
\(8.2834\,10^{-5}\). Thus every latitude and every time in
that compact interval has strictly negative log-curvature.
Floating eigendata are used only to propose the curves;
acceptance uses exact rational interval comparisons.

At \(t=4\), comparison to the certified ground trial and
(GC8) give \(\|f_4-f\|_X<5.059\,10^{-6}\), where \(f\)
is the actual ground shape. The ground receipt separately
checks \(\|Qf\|_X<0.9\), not merely this bound for its trial.
Applying (PN8) with the stationary comparison \(Qf\) gives
\[
\|f_t-f\|_X\le e^{-(t-4)/4}\|f_4-f\|_X
\quad(t\ge4).
\tag{GP4}
\]
Add the ground-trial error again before applying its polynomial
sign certificate. Even discarding the decay factor, the final
remaining numerator exceeds \(0.01305\), and the curvature
upper bound is below \(-0.0018081\) for every \(t\ge4\).
This completes the infinite tail without repeated time steps.
The earlier heat-smoothing argument (GC15)--(GC17) remains an
independent, weaker late-time certificate.

Combining (GI7), the compact rectangles and (GP4) proves
\[
\boxed{
\begin{gathered}
(\log\chi_t)''(a)<0
\quad(-1\le a\le1,\ 0<t\le\infty),\\
\int(1-a^2)|g'(a)|^2\,d\nu_t
\ge\operatorname{Var}_{\nu_t}g
\quad(0\le t\le\infty).
\end{gathered}}
\tag{GP5}
\]
The second line includes the Haar initial law. Strict curvature
does not have a time-independent negative margin as \(t\downarrow0\);
its cubic zero is essential. This proves the full preparation
statement at the one specified coupling, not at all couplings.

## What the certificate does and does not select

The mechanism is compatibility between the actual kinetic blocks,
the same magnetic multiplication, and the conditional readout.
The missing derivatives cannot be independently supplied or
inferred from an arbitrary positive kernel. This certificate
uses those shared structures to control a local
shape that their positive cone alone does not enforce.

The graph, group, kinetic normalization, potential and Haar
preparation nevertheless remain chosen inputs. The estimate
does not identify an octonionic multiplication defect with
conditional response, construct spatial extension, or prevent
soft modes when the graph and continuum regulators change.
It is a test a proposed parent law must reproduce, not that law.
The fixed-coupling preparation interval is now complete. The
[[pointed-preparation-stability-and-the-volume-test#Independent copies defeat a global vacuum-normalized norm|independent-copy obstruction]]
also shows why its global comparison norm cannot simply be
declared volume-uniform: that norm grows exponentially even
for copies whose gap stays fixed. The constructive question
is an assembly law for local or connected comparisons under
genuine cycle addition and continuum scaling. Repeating the
same certificate at many couplings would not answer it.
