# Path-Shift Fisher Geometry Before Gauge Projection

The heat state fixes a positive Fisher metric once its admissible path shifts are specified. Dualizing that metric on pointwise observable variations reproduces the closed shared-driver response, with no freely chosen intensity profile. This is a conditional selection rule, not selection by the state alone: the shift action and the Fisher-to-response prescription remain structural inputs. Gauge projection makes the order especially important. It erases every first-order score of these shifts, while the response obtained before projection remains nonzero on invariant observables.

**Status: [EXACT] for finite-energy path shifts, their relative entropy, Fisher dualization, and the specified gauge quotient; [EXACT] finite-holonomy distinction between the two handed response forms; [OPEN] for physical clock identification and a four-dimensional Yang--Mills realization.**

## A declared action on the whole path carrier

Use the compact connected semisimple group, bi-invariant metric \(Q\),
and Brownian path law \(\mu\) of
[[shared-driver-response-and-the-nested-holonomy-clock|the shared-driver
construction]]. Its area-indexed diffusion is
\(dX_t=\sqrt2 X_t\circ dB_t\), with generator \(\Delta_Q\).
Declare the group of absolutely continuous based paths \(k\), with
finite logarithmic energy, acting by pointwise **left multiplication**:
\[
\mathcal T_kX(t)=k(t)X(t),\qquad k(0)=e,\qquad
u_k(t)=\dot k(t)k(t)^{-1},\qquad
\int_0^T|u_k(t)|_Q^2dt<\infty.
\tag{PF1}
\]
This changes a holonomy presentation; it is not the residual gauge action
\(X\mapsto gXg^{-1}\). Nor is it a physical time evolution. Let
\(\mu_k=(\mathcal T_k)_*\mu\).

Keep the two stochastic logarithms distinct:
\[
B_t=\frac1{\sqrt2}\int_0^t X_s^{-1}\circ dX_s,\qquad
\beta^R_t=\frac1{\sqrt2}\int_0^t\circ dX_s X_s^{-1}.
\tag{PF2}
\]
Each is standard \(\mathfrak g\)-Brownian motion under \(\mu\), and
each determines the full path modulo null sets. They are related by
\(d\beta^R=\operatorname{Ad}_X dB\), a path-dependent stochastic
rotation, not a fixed linear orthogonal map of Wiener space.

## The state computes the cost of the shift

The product rule gives
\[
d\beta^R(\mathcal T_kX)
=\frac{u_k}{\sqrt2}\,dt+\operatorname{Ad}_k d\beta^R(X).
\tag{PF3}
\]
The latter rotation is deterministic and orthogonal. It preserves Wiener
law; the former term is a deterministic Cameron--Martin shift. Girsanov
therefore gives the normalized Radon--Nikodym density
\[
\rho_k(X)=\frac{d\mu_k}{d\mu}(X)
=\exp\left\{
\frac1{\sqrt2}\int_0^T Q(u_k,d\beta^R)
-\frac14\int_0^T|u_k|_Q^2dt\right\}.
\tag{PF4}
\]
Finite deterministic energy guarantees the exponential integrability
needed here. Under \(\mu_k\), the stochastic term in the exponent has mean
\(\tfrac12\int|u_k|^2\). Thus, using natural logarithms,
\[
\boxed{D(\mu_k\Vert\mu)
=\frac14\int_0^T|\dot k k^{-1}|_Q^2dt
=\frac14\int_0^T|k^{-1}\dot k|_Q^2dt.}
\tag{PF5}
\]
The second equality uses bi-invariance. One must not replace \(u_k\)
by the left logarithmic velocity in (PF4) without also changing its
stochastic frame.

The map \(\mathcal T_k\) is invertible. This positive relative entropy
measures distinguishability from the unshifted reference, not information
destroyed by the map or irreversible entropy production. The actual
forgetting operation considered below is the further gauge quotient.

This is an explicit application of
[[library/analysis-on-wiener-space-and-applications/inq|Üstünel's Wiener
analysis]], §1.5's Girsanov theorem and §13.5's deterministic group-path
translation identities. The source uses diffusion generator
\(\Delta_Q/2\); the \(\sqrt2\) in our diffusion gives the quarter
in (PF4)–(PF5). The left-multiplication formula above is derived directly
to make the side and sign conventions checkable.

There is a genuine composition law beneath this quadratic cost:
\[
u_{k\ell}=u_k+\operatorname{Ad}_k u_\ell.
\tag{PF6}
\]
It is a velocity cocycle. Its squared norm has a cross term, so the
entropy cost is not a generally additive conserved charge. Costs do add
for controls with disjoint time supports. The variable integrated here
is the supplied heat-area index, not an emergent physical clock or an
ontological temporal arrow.

## Dual Fisher geometry selects the minimum kernel

Let \(h\) be a based absolutely continuous Lie-algebra path with
\(\dot h\in L^2\), and set \(k_\varepsilon(t)=e^{\varepsilon h(t)}\).
Then \(u_{k_\varepsilon}=\varepsilon\dot h+O(\varepsilon^2)\) in
\(L^2\). Its score and coincidence metric are
\[
Z_h=\left.\partial_\varepsilon\rho_{k_\varepsilon}\right|_0
=\frac1{\sqrt2}\int_0^T Q(\dot h,d\beta^R),\qquad
g_\mu(h,j)=\mathbb E_\mu Z_hZ_j
=\frac12\int_0^TQ(\dot h,\dot j)dt.
\tag{PF7}
\]
The Fisher metric is the **second derivative**, not the coefficient of
\(\varepsilon^2\) itself, in (PF5). This agrees with the convention in
[[basic-concepts/hessians/fisher-response|Fisher response]].

For a real smooth cylinder \(F=f(X_{t_1},\ldots,X_{t_m})\), the action
on observable values is a different map:
\[
V_hF(X)=\left.\partial_\varepsilon
F(\mathcal T_{k_\varepsilon}X)\right|_0
=\sum_i Q(\nabla_{L,i}f,h(t_i)),
\]
where \(L_af(x)=\partial_v f(e^{vT_a}x)|_0\). Specify the following
**Fisher-dual response prescription**:
\[
\Gamma_{\rm F}(F)(X)
:=\sup_{h\ne0}\frac{|V_hF(X)|^2}{g_\mu(h,h)},\qquad
\mathcal E_{\rm F}(F)=\mathbb E_\mu\Gamma_{\rm F}(F).
\tag{PF8}
\]
The supremum is a pointwise cotangent norm using one fixed Hilbert space
of deterministic shift parameters. It is not the squared derivative of
the expectation of \(F\).

Writing \(h(t_i)=\int_0^{t_i}\dot h(s)ds\), Riesz duality gives
\[
\boxed{\Gamma_{\rm F}(F,G)
=2\sum_{i,j}\min(t_i,t_j)
Q(\nabla_{L,i}f,\nabla_{L,j}g).}
\tag{PF9}
\]
This is exactly (SD5), hence has the previously constructed cylinder
closure and full left-driver OU clock. No closability or gap is inferred
from Fisher positivity alone; those conclusions use that equality and
the path-space theorem already cited there.

Within the weighted family (SD12), the dual parameter metric would
instead be \(\tfrac12\int|\dot h|^2/a\), on its finite-energy domain.
Agreement with (PF7) for all localized time profiles forces \(a=1\)
almost everywhere: test \(\dot h=1_Ev\) on measurable
\(E\subset\{a\ge1/n\}\), and then take the union over \(n\).
This uses no bounded inverse when \(a\) approaches zero.
A freely inserted overall multiplier would likewise
change the declared prescription. The information unit is fixed here by
natural logarithms; conversion to physical clock units is not.

The gain is limited but precise: the heat state **plus** the specified
shift action **plus** (PF8) select the response and imply the same-clock
restart law. They do not derive either the action or (PF8) from a bare
probability space. This is one concrete instance of the
[[measured-response-carriers/inq|distinction between state tangents,
observable cotangents, and represented operators]].

## Gauge projection erases the first-order scores

Let \(\mathsf P_G\) average simultaneous conjugation, and consider the
restriction of \(\mu_{k_\varepsilon}\) to invariant observables. It is
represented on the full space by the invariant density
\(\bar\rho_\varepsilon=\mathsf P_G\rho_{k_\varepsilon}\).
Conjugation rotates \(\beta^R\) by \(\operatorname{Ad}_g\), hence
\[
\left.\partial_\varepsilon\bar\rho_\varepsilon\right|_0
=\mathsf P_G Z_h=Z_{\int_G\operatorname{Ad}_g h\,dg}=0.
\tag{PF10}
\]
Semisimplicity eliminates fixed Lie-algebra vectors. The first-order
Fisher metric of this **projected perturbation family** is zero.
It has no inverse to use in (PF8); a zero metric does not have a
canonical zero inverse or define a zero response operator.

By contrast, first forming (PF8) on the extended carrier and then
restricting to invariant observables gives a nonzero response. For the
\(SU(2)\) character \(f_t=\chi_{1/2}(X_t)\), with
\(Q=-2\operatorname{Tr}\),
\[
\mathcal E_{\rm F}(f_t)=2tJ(t)>0,\qquad
J(t)=\tfrac34(1-e^{-2t}),\qquad t>0.
\]
Every first derivative of its **expectation** along these state shifts
is nevertheless zero. Averaging a linear score and taking the squared
pointwise norm of an observable derivative are different operations.
This is an information-geometric counterpart of
[[inq#Closing the parts first loses physical loops|premature regional
closure]]: complementary noninvariant presentation data can be required
before forming a nonzero invariant response.

## The first retained change is explicitly quadratic

For \(SU(2)\), choose a real profile \(H(0)=0\) with
\(\tfrac12\int_0^T\dot H^2=1\), and put
\(k_\varepsilon=e^{\varepsilon HT_3}\).
Set \(Z_a=\tfrac1{\sqrt2}\int\dot H\,d\beta^R_a\). The three
\(Z_a\) are independent standard Gaussians, and (PF4) is exactly
\(e^{\varepsilon Z_3-\varepsilon^2/2}\). The adjoint orbit of \(T_3\)
is the unit two-sphere. With \(R=|Z|\), its full Haar average is
\[
\bar\rho_\varepsilon
=e^{-\varepsilon^2/2}
\frac{\sinh(\varepsilon R)}{\varepsilon R}
=1+\frac{\varepsilon^2}{6}(R^2-3)+O(\varepsilon^4).
\tag{PF11}
\]
The value at \(\varepsilon R=0\) is defined by continuity. Gaussian
integrability justifies differentiation and the ensuing entropy expansion.
Since \(\operatorname{Var}(R^2)=6\),
\[
D(\bar\rho_\varepsilon\mu\Vert\mu)
=\frac{\varepsilon^4}{12}+O(\varepsilon^6),
\qquad
D(\rho_{k_\varepsilon}\mu\Vert\mu)=\frac{\varepsilon^2}{2}.
\tag{PF12}
\]
For an independent normalization check,
\(\mathbb E\bar\rho_\varepsilon^2
=\sinh(\varepsilon^2)/\varepsilon^2\): average two independent unit
directions before the Gaussian expectation.

The one-sided parameter \(\eta=\varepsilon^2\ge0\) has score
\((R^2-3)/6\) and Fisher coefficient \(1/6\) at its boundary.
This is a new parameterization of a higher-order retained change, not
an inverse of the vanished \(\varepsilon\)-Fisher metric. It is not a
Born rule or a collapse mechanism.

There is also a clock distinction: \(R^2-3\) is second Wiener chaos
in \(\beta^R\), whereas the SD clock was transported from \(B\).
The nonlinear rotation in (PF2) need not preserve chaos. No claim that
this particular score is an SD eigenvector follows from (PF11).

## The choice of handed action remains visible

Pointwise **right** multiplication of paths has the same Fisher energy
at identity, but its observable variations use
\(R_af(x)=\partial_vf(xe^{vT_a})|_0\). Dualization then gives
\(2\sum\min(t_i,t_j)Q(\nabla_{R,i}f,\nabla_{R,j}g)\).
These two forms are conjugate by path inversion. They have the same
unit-clock threshold, but are not the same form on fixed invariant
readouts.

For one or two holonomies the ambiguity is invisible. Invariance under
simultaneous conjugation gives \(\sum_i\nabla_{L,i}F
=\sum_i\nabla_{R,i}F\), while each individual gradient has the same
norm in the two frames. Polarization then identifies the only mixed term
when there are two arguments. With three arguments, distinct minimum
weights can separate the mixed terms. Thus the two-holonomy restart
test (SD15) cannot distinguish these actions.

An exact finite cylinder distinguishes them. In unit-quaternion
coordinates \(g_i=(w_i,v_i)\), let
\(F(g_1,g_2,g_3)=\det(v_1,v_2,v_3)\), invariant under simultaneous
conjugation. Again specialize to \(Q=-2\operatorname{Tr}\), use
\(T_a=-i\sigma_a/2\), times \((1,2,3)\), and
\[
g_1=(0;(1,0,0)),\quad
g_2=(4/5;(0,3/5,0)),\quad
g_3=(0;(3/5,0,4/5)).
\]
Writing \(b_i=\partial_{v_i}F\), the gradients are
\(\nabla_{L,i}F=(w_ib_i+v_i\times b_i)/2\) and
\(\nabla_{R,i}F=(w_ib_i-v_i\times b_i)/2\).
Only their second components survive at this triple:
\[
(L_1,L_2,L_3)=\tfrac1{50}(9,16,-9),\qquad
(R_1,R_2,R_3)=\tfrac1{50}(-9,16,9),
\]
so
\[
\Gamma_L(F)=\frac{193}{625},\qquad
\Gamma_R(F)=\frac{481}{625}.
\tag{PF13}
\]
This is a pointwise statement; inversion symmetry can still make the
unlocalized diagonal integrals equal. To prove the forms differ, put
\(D=\Gamma_L(F)-\Gamma_R(F)\), a smooth invariant cylinder. For
either form the product rule gives
\[
\mathcal E(F,DF)-\tfrac12\mathcal E(D,F^2)
=\int D\,\Gamma(F)\,d\mu.
\]
The difference of these expressions is \(\int D^2d\mu>0\), because
the three-time heat law has strictly positive density and (PF13) makes
\(D\) nonzero on an open set. Thus at least one of these explicit
invariant bilinear pairings differs. Take \(T\ge3\) for this example.

The state cannot choose a handed presentation by itself. One must
retain the action as part of the object and transport it when the
presentation is inverted. Entropy supplies its metric; it does not
silently supply the action, a chirality of nature, or physical time.

[[two-sided-fisher-completion-and-the-neutral-carrier|Joint two-sided
Fisher geometry]] uses the actual cross-score covariance rather than
averaging the two response forms. Its finite cylinder domain is exactly
the simultaneous-conjugation-invariant algebra, and its closed joint
operator has non-attained threshold two. This removes handedness within
a specified larger action, but changes the response: its exact annular
calculation fails the separate same-clock restart law (SD15).

The [[receipts/path_shift_fisher_receipt.py|path-shift Fisher receipt]]
checks finite precision/cometric inversion, the full radial integrals
and their moment identities, and the rational handed-frame example.
Its [[receipts/path-shift-fisher-receipt-output.txt|recorded output]] is
numerical and algebraic evidence for these formulas, not the path-space
closure proof or a Yang--Mills continuum construction.
