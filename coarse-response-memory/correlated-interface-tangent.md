# The First Correlated Interface Response Has Two Radial Channels

Switching on one crossing interaction beside an already interacting plaquette forces a relative-angle response at every positive internal coupling. The complete first ground-state tangent reduces exactly to two coupled radial functions, with all radial harmonics retained. A lower bound supplied by the three external links converts its full residual into an error bound independent of internal coupling. This gives a quantitative target for a boundary composition law beyond fitting marginal states or one crossing correlation.

**Status: exact finite-system reduction and nonvanishing theorem; rigorous numerical enclosures at one declared coupling.** The Hamiltonian, group and electric metric remain inputs. The result advances the benchmark in [[product-boundary-frames-and-crossing-susceptibility|independent boundary frames]], not the selection of those inputs or the continuum Yang–Mills gap.

## Separate the internal preparation from the crossing source

Use the seven-link graph, complete invariant carrier and kinetic operator \(H_0\) of [[two-plaquette-vacuum-and-relational-state|the two-plaquette construction]]. Its orbit coordinates are \((a,b,z)\), with \(a,b\) the two half-traces and \(z\) the relative vector contraction. Set

\[
H(t)=H_{\rm ref}-t\gamma b,\qquad
H_{\rm ref}=H_0+\beta(1-a),\qquad
\kappa>0,\quad\beta\ge0,\quad\gamma>0.
\tag{IT1}
\]

The omitted scalar \(t\gamma\) affects the ground energy linearly, but does not affect the state. At \(t=0\), the normalized positive ground is \(f(a)\). With \(s=1-a^2\), \(r=\beta/\kappa\), and \(e=E_\beta/\kappa\),

\[
-sf''+3af'+r(1-a)f=ef,\qquad
\int f^2\,d\mu_H=1.
\tag{IT2}
\]

Here \(d\mu_H(a)=(2/\pi)\sqrt{1-a^2}\,da\). The normalized ground-state derivative and energy curvature are

\[
\dot\psi(0)=\gamma\eta,\qquad
\eta=(H_{\rm ref}-E_\beta)^{-1}(bf),\qquad
\mathcal E''(0)=-2\gamma^2\langle bf,\eta\rangle.
\tag{IT3}
\]

The inverse is on the vacuum complement. The source is centered since \(\int b\,dy=0\). These identities follow by differentiating the bounded perturbation of the simple ground eigenpair, including its normalization. In the ground-state carrier \(L^2(f^2dx\,dy)\), the corresponding relative response is \(\eta/f=L^{-1}b\).

## The reduction retains the entire angular response

The operator commutes with the second-loop Casimir \(D_y\). The source has second harmonic degree \(m=1\); that whole sector therefore reduces the operator and its inverse. In the complete invariant basis \(B_{nmk}\), fixing \(m=1\) allows precisely \(k=0,1\), for every permitted \(n\). Consequently the dimensionless tangent \(v=\kappa\eta\) has the exact form

\[
v=A(a)b+B(a)z.
\tag{IT4}
\]

This is a pair of radial functions, not a two-dimensional trial space. Direct application of the inherited cometric gives

\[
\begin{aligned}
-sA''+3aA'+[3+r(1-a)-e]A
  +\tfrac12(sB'-3aB)&=f,\\
-sB''+5aB'+[5+r(1-a)-e]B-\tfrac12A'&=0.
\end{aligned}
\tag{IT5}
\]

Conditional Haar integration over \(y\) gives the exact norm

\[
\|Ab+Bz\|^2
=\frac14\int\left(|A|^2+s|B|^2\right)d\mu_H(a).
\tag{IT6}
\]

Use the operator domain inherited from smooth functions on \(SU(2)^2\), or its complete harmonic core. The singular orbit coordinates do not supply independent endpoint boundary conditions.

Suppose \(B\equiv0\). The second equation forces \(A'=0\); the first gives

\[
f(a)=A[3+r(1-a)-e].
\]

The constant \(A\) cannot vanish. For \(r>0\), this affine function has nonzero slope. Substitution into (IT2) produces a nonzero quadratic term from \(r(1-a)f\), with no other quadratic term available to cancel it. Hence

\[
\boxed{\beta>0\quad\Longrightarrow\quad B\not\equiv0.}
\tag{IT7}
\]

Even an arbitrary trace-only response \(F(a)b\) misses this channel. This strengthens the earlier exclusion of a constant multiple of the crossing half-trace.

## A residual bound includes the uncomputed harmonics

On the entire reducing \(m=1\) sector,

\[
H_{\rm ref}-E_\beta\ge\frac{9\kappa}{4}I.
\tag{IT8}
\]

To see the bound, return to the raw seven links. The internal four-link Hamiltonian is at least \(E_\beta\) on its full raw carrier. Each of the three external links carries spin \(1/2\) in this sector and contributes \(3\kappa/4\). The inequality survives the whole Gauss restriction. This also explains [[product-boundary-frames-and-crossing-susceptibility#One internal plaquette gives an exact spectral comparison|the shifted charged spectral law]]. It is a bound for this source sector, not for every physical excitation.

For any trial \(\eta_N\) in its operator domain, a full residual therefore gives

\[
\|\eta_N-\eta\|
\le\frac4{9\kappa}
\|(H_{\rm ref}-E_\beta)\eta_N-bf\|.
\tag{IT9}
\]

The bound is uniform in finite \(\beta\), although the number of harmonics needed for a small residual can increase with \(\beta\).

One must also control the approximate internal vacuum. Let \(p\) be a normalized radial trial with positive ground overlap, and put

\[
\mu=\langle p,H_{\rm ref}p\rangle<3\kappa,
\qquad \rho=\|(H_{\rm ref}-\mu)p\|.
\]

On the radial carrier the first excited electric eigenvalue is \(3\kappa\). Nonnegativity of \(\beta(1-a)\) preserves that lower bound by min–max. Spectral decomposition and the Temple estimate give

\[
0\le\mu-E_\beta\le\delta_E:=\frac{\rho^2}{3\kappa-\mu},
\qquad
\|p-f\|\le\delta_f:=\frac{\sqrt2\rho}{3\kappa-\mu}.
\tag{IT10}
\]

For completeness, the Temple estimate follows from
\(\langle p,(H-E_\beta)(H-3\kappa)p\rangle\ge0\).
The excited component of \(p\) is bounded by \(\rho/(3\kappa-\mu)\); phase alignment then supplies the displayed vector bound. The threshold \(3\kappa\) is only being used on the radial carrier.

With \(R_N=(H_{\rm ref}-\mu)\eta_N-bp\), the practical certificate is

\[
\boxed{
\|\eta_N-\eta\|
\le\frac4{9\kappa}
\left(\|R_N\|+\delta_E\|\eta_N\|+\tfrac12\delta_f\right).
}
\tag{IT11}
\]

The factor \(1/2\) is exact: \(\|b(p-f)\|=\|p-f\|/2\). In a harmonic cutoff, multiplication by \(a\) creates omitted \(n=N+1\) coefficients. They enter both residuals; a finite eigensolver residual alone cannot certify (IT11).

## Analytic coefficients and a numerical enclosure

Perturbation at \(r=0\) yields

\[
v=\frac b3+r\frac{40ab+4z}{351}+O(r^2),\qquad
\frac vf=\frac b3+r\frac{ab+4z}{351}+O(r^2).
\tag{IT12}
\]

The mixed contraction \(ab+4z\) also occurs in [[radial-marginal-and-conditional-stress|the conditional amplitude expansion]]. Here the internal and crossing couplings are varied independently. Equation (IT5) extends the perturbative clue to an all-positive-internal-coupling nonvanishing theorem.

If \(S=\langle b,L^{-1}b\rangle\), the norm of the best scalar-correlation error is

\[
\begin{aligned}
\kappa S&=\frac1{12}+\frac{r^2}{8424}+O(r^4),\\
\inf_c\|L^{-1}b-cb\|_{f^2}
&=\frac{7|r|}{1404\kappa}+O(r^2/\kappa).
\end{aligned}
\tag{IT13}
\]

The second coefficient uses \(\langle a^2b^2\rangle_H=1/16\), \(\langle z^2\rangle_H=3/16\), and \(\langle abz\rangle_H=0\). The susceptibility is even in signed \(r\): the central flip \(x\mapsto-x\) preserves \(b\), and changes the internal coupling's sign up to a scalar energy shift. Thus its next displayed remainder is fourth order.

At \(\kappa=\beta=1\), [[receipts/correlated_interface_tangent_receipt.py|the interface receipt]] gives these outward decimal enclosures:

| Quantity | Certified interval |
| --- | --- |
| Internal ground energy \(E_\beta\) | \([0.91805817662429,\ 0.91805817662430]\) |
| Susceptibility \(S\) | \([0.08344516530979,\ 0.08344516530980]\) |
| Raw response norm \(\|\eta\|\) | \([0.16695973823108,\ 0.16695973823109]\) |
| Distance from every scalar multiple of \(bf\) | \([0.00481370292739,\ 0.00481370292742]\) |
| Relative-angle harmonic norm | \([0.00476678104552,\ 0.00476678104553]\) |

The receipt uses a floating solver only to propose rational trials. Exact rational interval arithmetic then encloses the full residuals, normalization, matrix square roots and error transfer. It proves a tangent error below \(10^{-12}\), including internal-vacuum uncertainty. Independent checks compare the reduced matrix with the complete invariant matrix and its tangent with unequal-coupling ground-state finite differences. Floating diagnostics at additional couplings are not included in the certified claim.

For the joint-realization programme, the resulting acceptance condition is concrete: a proposed boundary law should determine this two-channel response when it claims to recover the supplied finite Yang–Mills member. Reproducing the half-trace susceptibility alone does not meet that condition. Selecting a different finite model can be a useful construction, but must expose its own response and the missing recovery map.
