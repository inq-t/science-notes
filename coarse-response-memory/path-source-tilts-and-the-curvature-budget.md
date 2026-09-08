# Path-Source Tilts and the Curvature Budget

Resolving the prepared two-plaquette amplitude into its underlying paths makes every local contribution an explicit spherical exponential tilt. After conjugation averaging, each contribution has a known nonpositive latitude log-curvature. The remaining marginal-concavity condition compares posterior source variance with mean geometric curvature. Their endpoint values can be computed separately by varying one coupling before normalization. At late preparation times both terms grow quadratically while their difference stays finite, excluding any time-uniform fractional margin between them.

**Status: exact fixed-system source representation, component curvature, short-time budget and late-time fractional-margin obstruction; numerical separate-channel checks; all-time mixture sign certified separately at one coupling.** This resolves the [[replica-weighted-correlations-and-the-local-readout|replica mixture]] further without changing its state, electric metric or preparation. Quaternion coordinates below label \(SU(2)\), not four spacetime coordinates.

## The bounded source vectors are derived from the paths

Use the independent paths in [[positive-amplitude-kernel-and-preparation|the Gram construction]]: two shared paths \(S,T\) of speed \(\kappa\), and four outer paths \(B_1,\ldots,B_4\) of speed \(3\kappa\), all based at \(1\). Set
\[
C(B,S)_s=\operatorname{quat}(S_sB_s^{-1}),\qquad
\xi=\lambda\int_0^t[C(B_1,S)_s+C(B_3,T)_s]\,ds,
\quad
\zeta=\lambda\int_0^t[C(B_2,S)_s+C(B_4,T)_s]\,ds.
\tag{PS1}
\]
These are vectors in \(\mathbb R^4\), with \(|\xi|,|\zeta|\le2\lambda t\).
They are conditionally independent and identically distributed given
\(S,T\), not independent under their full joint law \(\mu_t\).

For unit quaternions \(x,y\), represented by \(X,Y\), the identity
\(q(xB_sS_s^{-1})=X\cdot C(B,S)_s\) gives
\[
P_t(x,y)^2=e^{-4\lambda t}
\mathbb E_{\mu_t}e^{X\cdot\xi+Y\cdot\zeta}.
\tag{PS2}
\]
Indeed each amplitude supplies two independent outer paths conditional
on one shared path; squaring supplies the second shared path.
No conditional normalization has yet been performed.

The Haar integral of a tilt on \(S^3\) is
\[
Z_4(v)=\int_{S^3}e^{vX_0}\,d\sigma(X)
=\sum_{n\ge0}\frac{v^{2n}}{4^n n!(n+1)!},
\qquad Z_4(0)=1.
\tag{PS3}
\]
The series follows by integrating powers of \(X_0\). Integrating \(Y\)
in (PS2), then normalizing, yields the actual complete local density
\[
\boxed{
R_t(X)=
\frac{\mathbb E_{\mu_t}[Z_4(|\zeta|)e^{X\cdot\xi}]}
{\mathbb E_{\mu_t}[Z_4(|\zeta|)Z_4(|\xi|)]}.
}
\tag{PS4}
\]
The hidden-loop factor \(Z_4(|\zeta|)\) is not optional. It retains
the effect of the shared path when the other output is integrated out.
Integrating the outer paths before this step recovers exactly the
squared-overlap weighting in (RW3).

## Conjugation supplies the component geometry

Simultaneous conjugation of all six paths preserves their law and
rotates the three-vector parts of \(\xi,\zeta\) together. This is
\(SO(3)\) invariance, not arbitrary \(SO(4)\) invariance. Write
\(\eta=\xi_0\), \(b=|\boldsymbol\xi|\), \(a=X_0\), \(h=1-a^2\).
The \(S^2\) directional integral therefore converts (PS4) to
\[
R_t(a)=
\frac{\mathbb E_{\mu_t}[Z_4(|\zeta|)k_{\eta,b}(a)]}
{\mathbb E_{\mu_t}[Z_4(|\zeta|)Z_4(|\xi|)]},
\qquad
k_{\eta,b}(a)=e^{\eta a}\frac{\sinh(b\sqrt h)}{b\sqrt h}.
\tag{PS5}
\]
These are densities relative to Haar; the latitude Jacobian is not
included in \(R_t\) or \(k\).

The [[conditional-fisher-coercivity/linear-tilted-sphere-coercivity#Averaging a fixed transverse tilt preserves latitude concavity|spherical tilt lemma]]
supplies explicit functions \(A_b(h),B_b(h)\ge0\) with
\[
Q_{\eta,b}(a):=(\log k_{\eta,b})'=\eta-2aA_b(h),
\qquad
J_b(a):=-(\log k_{\eta,b})''=2A_b(h)+4a^2B_b(h).
\tag{PS6}
\]
In particular every resolved component is log-concave; it is strictly
so when \(b>0\). This is a stronger resolution than an unknown Hessian
of a partly averaged feature. It is not a claim that log-concavity
survives arbitrary mixing: (LT15) explicitly disproves that claim.

The actual local posterior on the complete source is
\[
d\mu_{t,a}=
\frac{Z_4(|\zeta|)k_{\eta,b}(a)}
{\mathbb E_{\mu_t}[Z_4(|\zeta|)k_{\eta,b}(a)]}\,d\mu_t.
\tag{PS7}
\]
Consequently
\[
\boxed{
v_t(a):=(\log\sqrt{R_t})''
=\tfrac12\left[
\operatorname{Var}_{\mu_{t,a}}Q_{\eta,b}(a)
-\mathbb E_{\mu_{t,a}}J_b(a)\right].
}
\tag{PS8}
\]
All differentiations, including closed-interval limits, are justified
by the bounded source vectors and the regular tilt functions.
Neither term is the raw conditional Fisher metric: (PK5)--(PK6)
still govern that transported derivative on the original carrier.

Thus the unresolved concavity question is the specific source estimate
\(\operatorname{Var}_{\mu_{t,a}}Q\le E_{\mu_{t,a}}J\).
The right side is now explicit, but the left side depends on the actual
correlated preparation and its two required weight factors.
The parameter \(t\) remains Euclidean preparation time, not a newly
derived physical clock.

## The initial negative curvature comes from transverse spread

For fixed \(\kappa,\lambda>0\), uniformly in \(a\in[-1,1]\),
\[
\begin{aligned}
\operatorname{Var}_{\mu_{t,a}}Q
&=2\kappa^2\lambda^2t^4+O(t^5),\\
\mathbb E_{\mu_{t,a}}J
&=\tfrac43\kappa\lambda^2t^3
-\tfrac{11}{3}\kappa^2\lambda^2t^4+O(t^5),\\
v_t(a)&=-\tfrac23\kappa\lambda^2t^3
+\tfrac{17}{6}\kappa^2\lambda^2t^4+O(t^5).
\end{aligned}
\tag{PS9}
\]
Here is a source derivation rather than a fit to the marginal.
Each individual relative path \(C=SB^{-1}\) has Brownian speed
\(4\kappa\). For \(s\le u\) and any imaginary component \(j\),
\[
\mathbb E[C_j(s)C_j(u)]
=\tfrac14e^{-3\kappa(u-s)}(1-e^{-8\kappa s}),
\qquad
\operatorname{Cov}(C_0(s),C_0(u))
=6\kappa^2s^2+O(t^3).
\tag{PS10}
\]
The first identity follows from the first- and second-harmonic
eigenvalues; the second follows from
\(\mathbb E C_0(s)=e^{-3\kappa s}\) and
\(\mathbb E[C_0(s)^2]=(1+3e^{-8\kappa s})/4\).
The two summands forming \(\xi\) are independent before weighting.
Integrating their moment kernels gives
\[
\mathbb E b^2=4\kappa\lambda^2t^3
-11\kappa^2\lambda^2t^4+O(t^5),\qquad
\operatorname{Var}\eta=2\kappa^2\lambda^2t^4+O(t^5).
\tag{PS11}
\]
Use \(A_b(h)=b^2/6+O(b^4)\), \(B_b(h)=O(b^4)\),
\(\|b^2\|_{L^p}=O(t^3)\) and
\(\|\eta-E\eta\|_{L^p}=O(t^2)\) for fixed finite \(p\).
After removing scalar constants, the posterior weight differs from
one by \(O(t^2)\) in the needed fixed \(L^p\) norms.
Its effect on \(E b^2\) starts at \(O(t^5)\).
This proves the two separate expansions in (PS9).

The shared coupling has not disappeared from the source construction.
For example its tangent moments obey
\[
\operatorname{Cov}(\boldsymbol\xi)=
\tfrac43\kappa\lambda^2t^3 I_3+O(t^4),\qquad
\operatorname{Cov}(\boldsymbol\xi,\boldsymbol\zeta)=
\tfrac13\kappa\lambda^2t^3 I_3+O(t^4).
\tag{PS12}
\]
The common shared edge contributes the second covariance.
Replacing \(\xi,\zeta\) by independent sources erases it and
changes the later posterior, even though it leaves the leading
local variance in (PS11) unchanged.

Initially the geometric term precedes the source-score variance by
one power of \(t\). This explains the already established cubic
concavity coefficient. It does not improve the all-time or
large-coupling quantifiers of
[[heat-preparation-and-latitude-coercivity|the preparation theorem]].

## Off-sphere source derivatives separate the two channels

Introduce an auxiliary generating function with independent variables
\(s\in\mathbb R\), \(z\ge0\):
\[
F(s,z)=\mathbb E_{\mu_t}\left[
Z_4(|\zeta|)e^{s\eta}\frac{\sinh(b\sqrt z)}{b\sqrt z}\right].
\tag{PS13}
\]
The physical marginal is \(F(a,1-a^2)\) divided by a constant.
Derivatives in the extra variable do not add a spacetime dimension;
they probe moments of the already defined bounded source.

For \(r=\sqrt{s^2+z}>0\), \(u=s/r\), let
\[
G(r,u)=\int_G
\left[e^{-t[H_0-\lambda r\,q(x)-\lambda q(y)]}1(u,y)\right]^2dy.
\tag{PS14}
\]
Then \(F(s,z)=G(r,u)\): scale the first external quaternion by
\(r\) in (PS2). The kinetic operator is unchanged.
Equivalently use \(H_{\lambda r,\lambda}\) with its nonnegative
potential and multiply the squared amplitude by
\(e^{2\lambda(r+1)t}\). The amplitude must remain unnormalized.
Its coupling-dependent normalization cancels from ordinary latitude
curvature but not from these source moments.

At \(s=\sigma=\pm1,z=0\), evaluate \(G\) at \((r,u)=(1,\sigma)\).
The exact chain rules are
\[
\begin{aligned}
F_s&=\sigma G_r,&F_{ss}&=G_{rr},&
F_z&=(G_r-\sigma G_u)/2,\\
F_{sz}&=(\sigma G_{rr}-G_{ru}-\sigma G_r+2G_u)/2,\\
F_{zz}&=(G_{rr}-2\sigma G_{ru}+G_{uu}-G_r+3\sigma G_u)/4.
\end{aligned}
\tag{PS15}
\]
The \(u\) derivatives are regular one-sided latitude derivatives.
The endpoint posterior is proportional to
\(Z_4(|\zeta|)e^{\sigma\eta}d\mu_t\), and its moments are
\[
E\eta=F_s/F,\quad E\eta^2=F_{ss}/F,\quad
Eb^2=6F_z/F,\quad E\eta b^2=6F_{sz}/F,\quad Eb^4=60F_{zz}/F.
\tag{PS16}
\]
Thus one obtains separately
\[
\mathcal V_\sigma=\operatorname{Var}(\eta-\sigma b^2/3),
\qquad
\mathcal J_\sigma=E(b^2/3+2b^4/45),\qquad
v_t(\sigma)=(\mathcal V_\sigma-\mathcal J_\sigma)/2.
\tag{PS17}
\]
The last equality is an internal identity check, not independent
evidence that \(\mathcal V_\sigma\le\mathcal J_\sigma\).
Asymmetric coupling derivatives must retain the complete relational
carrier, including directions antisymmetric under exchanging the
two plaquettes. Equal-coupling exchange symmetry cannot be imposed
while changing the first coupling alone.

The [[receipts/two_plaquette_vacuum_receipt.py|full interacting receipt]]
implements these derivatives with five radius values and analytic
latitude jets. At \(\kappa=1,t=0.2\), endpoint order \((-1,+1)\), it gives:

| Coupling | Source variance \(\mathcal V\) | Geometric term \(\mathcal J\) | Ratio \(\mathcal V/\mathcal J\) |
|---|---|---|---|
| \(\lambda=2\) | \((0.00578804,0.00817606)\) | \((0.02691201,0.02519482)\) | \((0.215073,0.324513)\) |
| \(\lambda=16\) | \((1.69252190,1.75310400)\) | \((4.90395848,2.32238173)\) | \((0.345134,0.754873)\) |

Radius steps \(0.004,0.002,0.001\) and separate cutoffs \(10/12\),
\(14/16\) change the reported channels by less than
\(2.5\,10^{-7}\). The positive variances and moment covariances are
resolved finite diagnostics. The Galerkin family is not asserted
to define a positive source measure at every cutoff, and the
reconstruction identity is not a proof of the inequality.

## A uniform fractional margin is impossible at late time

Fix \(\kappa,\lambda>0\), and write
\(H(r)=H_0-\lambda r q(x)-\lambda q(y)\) for the **constant-free**
operator in (PS14), with \(a=q(x)\).
Let \(E(r)\) be its lowest eigenvalue and \(f_r>0\) its normalized
ground vector. Compact ellipticity gives a simple isolated
ground state; bounded analytic perturbation in \(r\) and
elliptic regularity give, locally near \(r=1\),
\[
G(r,u)=e^{-2tE(r)}C(r,u)[1+O(e^{-\delta t})],
\qquad
C(r,u)=\langle1,f_r\rangle^2\int f_r(u,y)^2dy>0.
\tag{PS18}
\]
This holds with the needed first and second \(r,u\) derivatives
and a fixed-system \(\delta>0\), possibly reduced to absorb
polynomial time factors. It uses a local uniform gap in the
coupling parameter of this compact system, not a volume- or
continuum-uniform mass gap.

Set \(d=-E'(1)\). This number is strictly positive.
The central flip \(x\mapsto-x\) preserves \(H_0\) and the right
potential, so \(E(r)=E(-r)\). If \(Q_r=I-|f_r\rangle\langle f_r|\),
the reduced-resolvent formula gives
\[
E''(r)=-2\lambda^2
\left\langle Q_r a f_r,(H(r)-E(r))_\perp^{-1}Q_r a f_r\right\rangle<0.
\tag{PS19}
\]
Strictness follows because \(f_r\) is positive and \(a\) is
nonconstant. Evenness and strict concavity imply \(E'(1)<0\).
Equivalently \(d=\lambda\langle a\rangle_{f_1^2}\).
This is a coupling response, not a mass-gap identification.
For the energy including the nonnegative potential constants,
the correct expression would be \(d=\lambda-E_{\rm phys}'(1)\).

Put \(L=\log G\). Equation (PS18) gives
\(L_r=2dt+O(1)\), \(L_{rr}=-2tE''(1)+O(1)\), while
\(L_u,L_{ru},L_{uu}=O(1)\). Substituting in (PS15)--(PS16) yields
\[
Eb^2=6dt+O(1),\quad Eb^4=60d^2t^2+O(t),\quad
\operatorname{Var}\eta=O(t),\quad
\operatorname{Cov}(\eta,b^2)=O(t),
\tag{PS20}
\]
where expectations use the actual endpoint posterior
\(\mu_{t,\sigma}\), and \(b\) retains its source-magnitude meaning.
For example the
last covariance is exactly
\(3[\sigma L_{rr}-L_{ru}-\sigma L_r+2L_u]\).
Thus \(\operatorname{Var}(b^2)=24d^2t^2+O(t)\), and
\[
\boxed{
\mathcal V_\sigma(t)=\tfrac83d^2t^2+O(t),\qquad
\mathcal J_\sigma(t)=\tfrac83d^2t^2+O(t),\qquad
\frac{\mathcal V_\sigma(t)}{\mathcal J_\sigma(t)}\longrightarrow1.
}
\tag{PS21}
\]
Nevertheless their exact difference is
\(\mathcal V_\sigma-\mathcal J_\sigma=L_{uu}(1,\sigma)\),
which converges to \(2v_{\rm ground}(\sigma)\), the finite
ground-marginal log-density curvature.
Therefore **no fixed \(\epsilon>0\)** can give
\(\mathcal V_\sigma\le(1-\epsilon)\mathcal J_\sigma\)
for all preparation times. This already excludes a margin
uniform over both latitude and time. It does not decide the
weaker inequality \(\mathcal V_\sigma\le\mathcal J_\sigma\).

For \(\lambda=2,\kappa=1\), the finite diagnostic gives
\(d\simeq0.593628682\), \((8/3)d^2\simeq0.939720031\).
The endpoint ratios at \(t=2\) are approximately
\((0.921411,0.967021)\); at \(t=8\) they are
\((0.994398,0.997897)\).
The latter log-amplitude curvatures \(v_t=(\log\sqrt R)''\)
have stabilized near
\((-0.17845379,-0.06435034)\), not zero.
Thus small relative separation coexists with a finite
negative difference. The theorem is (PS18)--(PS21), not
extrapolation from these finite times.
The persisted \(t=2,8\) checks refine both the radius step
and the cutoff; reported channel discrepancies are below
\(2.0\,10^{-7}\). The ground coefficient is computed from
the actual ground vector, not fitted to the late-time channels.

The source representation exposes what remains to be selected by
a more fundamental law: the correlated measure controlling the
competition in (PS8), not only positivity of its individual components.
[[certified-ground-marginal-and-late-preparation|The correlated additive remainder]]
is now certified at \(\kappa=\lambda=1\) for the ground state
and all positive preparation times, uniformly in latitude.
This succeeds despite (PS21): it bounds the difference directly,
not a fixed percentage separation of its growing terms.
The cubic initial layer and contractive whole-interval comparison
retain the correlations that separate estimates would lose.
Uniformity beyond this fixed system remains a separate question.
The supplied path geometry, speeds, potential and initial state still
determine this example. Neither its bounded source vectors nor its
component curvature construct a continuum translation representation
or a Yang--Mills mass gap.
