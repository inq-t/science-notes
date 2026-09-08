# Measure-Preserving Horizontal Lifts

A smooth family of conditional laws admits a connection that transports the laws themselves. Conditional expectation then intertwines the lifted derivative with the retained derivative, so the retained subspace reduces the associated diffusion even when the connection has curvature. This supplies a nonlinear replacement for Gaussian harmonic translation. Its comparison with an inherited physical or auxiliary form requires a separate distortion bound; changing the derivative is not merely changing notation.

**Status: exact smooth compact-carrier construction and conditional form bounds. No regulator-uniform Yang--Mills estimate or physical-time identification follows from existence alone.**

## Transport the conditional measure

Let \(Z,Y\) be closed connected smooth Riemannian manifolds with fixed metrics. Write
\[
\mu(dz,dy)=\nu(dz)\beta_z(dy),\qquad
\beta_z=b_z\,dm_Y,
\tag{MH1}
\]
with smooth strictly positive normalized densities, including the marginal \(\nu\). Use \(P f(z)=\int f(z,y)\beta_z(dy)\), and also denote by \(P\) its orthogonal projection onto the pullback of \(L^2(\nu)\) in \(L^2(\mu)\).

For a base tangent \(h\in T_zZ\), the normalized score is \(s_h=d_Z\log b[h]\), with \(\beta_z(s_h)=0\). The positive conditional generator is
\[
A_z=-b_z^{-1}\operatorname{div}_Y(b_z\nabla_Y).
\]
Connectedness, ellipticity and compactness give a unique smooth mean-zero solution
\[
A_z\phi_h=s_h,\qquad \beta_z(\phi_h)=0,\qquad v_h=\nabla_Y\phi_h.
\tag{MH2}
\]
Smooth parameter dependence gives a bundle map \(v:T_zZ\to T_yY\). Its defining identity is
\[
\boxed{d_Zb[h]+\operatorname{div}_Y(b_zv_h)=0.}
\tag{MH3}
\]
Along a smooth path \(z(t)\), integrating \(\dot y=v_{\dot z}(y)\) transports \(\beta_{z(0)}\) to \(\beta_{z(t)}\). Smooth compactness ensures existence along finite paths. The weighted-divergence and gradient-velocity formalism is standard; [[library/geometric-calculations-on-wasserstein-space/inq|Lott, Section 2 and equation (3.5)]] give its measure-space formulation and curve transport. The conditional operator argument below is proved here, not attributed to that source.

The gradient solution is one choice, not the only one: adding \(w_h\) with \(\operatorname{div}_Y(b_zw_h)=0\) preserves (MH3).

## Conditional expectation becomes horizontal

For any smooth compatible choice of \(v\), define
\[
D_h f=d_Zf[h]+d_Yf[v_h],\qquad
Df=d_Zf+v^*d_Yf.
\tag{MH4}
\]
Differentiating the normalized conditional mean and integrating (MH3) by parts gives
\[
\boxed{d_Z(Pf)[h]=P(D_hf).}
\tag{MH5}
\]
This holds for arbitrary joint observables, not only those independent of \(z\). Applied to products, it also makes \(D\) a metric connection on the conditional \(L^2\) bundle and gives \(D1=0\).

This is a chosen law-preserving horizontal derivative. It generally differs from the inherited fixed-\(y\) derivative of [[moving-fiber-connection|the moving-fiber audit]]. One must compare their forms rather than replace one by the other silently.

In local base coordinates, multiplication by \(\sqrt{b_z}\) transforms it to
\[
\sqrt b\,D_i\,(\sqrt b)^{-1}
=\partial_i+v_i\cdot\nabla_Y+\tfrac12\operatorname{div}_Yv_i.
\]
The continuity equation fixes the last sign. The fixed-\(y\) derivative instead becomes \(\partial_i-s_i/2\). A half-density frame change therefore does not identify the two dynamics.

## An exact reducing subspace without flatness

On smooth joint functions define
\[
\mathcal E_H(f)=\int|Df|^2d\mu,\qquad
\mathcal E_V(f)=\int|d_Yf|^2d\mu.
\tag{MH6}
\]
Take their closures. Smooth vector fields on a compact manifold give closable Markov forms; the sum with \(\mathcal E_V\) is elliptic. No bracket-generating hypothesis is needed below.

For \(g=Pf\), \(Dg=d_Zg\). Equation (MH5) says \(P D(I-P)f=0\), hence
\[
\mathcal E_H(Pf,(I-P)f)=0,\qquad
\mathcal E_V(Pf,(I-P)f)=0.
\tag{MH7}
\]
Jensen gives \(\mathcal E_H(Pf)\le\mathcal E_H(f)\), so \(P\) preserves the closed form domain. Therefore \(P\) reduces both closed generators. The restriction of the horizontal generator to its range is exactly the actual marginal gradient generator \(A_c\) on \(L^2(\nu)\).

Let \(\lambda_c\) be its Poincare gap. If \(\lambda_\perp=\inf\operatorname{spec}(A_H|_{\ker P})\), then adding whole-fiber refresh at rate \(\alpha>0\) gives
\[
\operatorname{gap}\bigl(A_H+\alpha(I-P)\bigr)
=\min\{\lambda_c,\alpha+\lambda_\perp\}
\ge\min\{\lambda_c,\alpha\}.
\tag{MH8}
\]
The formula assumes the discarded subspace is nonzero; an absent subspace contributes \(+\infty\). Whole-fiber refresh commutes with \(A_H\). General vertical diffusion need not commute with it, despite sharing the reducing projection.

If the actual conditional gradient gaps satisfy \(\rho_z\ge\rho>0\), then total variance and (MH5) give
\[
\boxed{
\mathcal E_H(f)+\mathcal E_V(f)
\ge\min\{\lambda_c,\rho\}\operatorname{Var}_\mu(f).}
\tag{MH9}
\]
Indeed \(\mathcal E_V\ge\rho\|f-Pf\|_2^2\), and
\(\mathcal E_H\ge\mathcal E_c(Pf)\ge\lambda_c\operatorname{Var}_\nu(Pf)\).
These are complete-carrier bounds; a chosen fast refresh does not certify an inherited gradient gap.

## Curvature preserves the law, not every observable

For base vector fields \(h,k\), the vertical curvature is
\[
\mathcal R(h,k)=[D_h,D_k]-D_{[h,k]}.
\]
Applying (MH5) twice shows \(P(\mathcal R(h,k)f)=0\) for every smooth \(f\). Consequently
\[
\boxed{\operatorname{div}_Y(b_z\mathcal R(h,k))=0.}
\tag{MH10}
\]
It need not vanish. Holonomy around a base loop preserves the returned conditional law while possibly moving its observables. No path-independent global product trivialization was used in (MH7)--(MH9). This connection on a conditional bundle is not being identified with the Levi-Civita connection of Wasserstein space.

For an explicit local example on \(Y=S^1\), normalized Haar and
\(b_{a,b}(y)=1+a\cos y+b\sin y\), \(a^2+b^2<1\), the minimum-gradient velocities at the origin are
\[
v_a=-\sin y,\quad v_b=\cos y,\quad
\partial_a v_b=\tfrac12-\cos^2y,\quad
\partial_b v_a=\sin^2y-\tfrac12.
\]
Thus \([D_a,D_b]=\partial_y\) there: nonzero curvature is a law-preserving rotation of the uniform fiber. This local calculation can be embedded in a closed base by taking \(a=\varepsilon\sin z_1,b=\varepsilon\sin z_2\), with \(\sqrt2\varepsilon<1\).

## The comparison that returns to an inherited form

Suppose the entire tangent map has pointwise norm \(\|v(z,y)\|\le B\). For
\(\mathcal E_0(f)=\int(|d_Yf|^2+|d_Zf|^2)d\mu\), the triangular shear in (MH4) gives
\[
\mathcal E_H+\mathcal E_V\le C(B)\mathcal E_0,\qquad
C(B)=\frac{2+B^2+B\sqrt{B^2+4}}2.
\tag{MH11}
\]
This is the largest eigenvalue of the two-by-two shear Gram matrix. It bounds the complete coarse tangent operator, not a sum of independently bounded coordinates.
Therefore
\[
\boxed{\lambda_0\ge\frac{\min\{\lambda_c,\rho\}}{C(B)}.}
\tag{MH12}
\]
For a different inherited mobility, prove domination by that mobility instead. A coordinate Jacobian or an auxiliary time rescaling cannot supply it.

For observables \(F(y)\) independent of the augmented coordinate, a sharper restricted comparison is
\[
(\mathcal E_H+\mathcal E_V)(F)
\le(1+B^2)\int|d_YF|^2d\mu.
\tag{MH13}
\]
If the joint construction preserves an original \(Y\)-marginal, this returns a Poincare bound for that unchanged marginal with denominator \(1+B^2\).

[[transport-cost-and-uniform-distortion|The transport-cost counterexample]] shows why a small average velocity norm cannot replace (MH11). [[rg-covariance-residue/nonlinear-gauge-fiber-transport|The nonlinear gauge construction]] supplies an actual Wilson conditional family and an explicit strong-coupling bound on \(B\). Neither statement extends those constants through the continuum trajectory.

## A law-preserving lift has the marginal likelihood

Let \(\phi_\epsilon\) be a smooth base diffeomorphism and let
\[
T_\epsilon(z,y)=(\phi_\epsilon z,\Psi_{\epsilon,z}y),
\qquad
(\Psi_{\epsilon,z})_*\beta_z=\beta_{\phi_\epsilon z}.
\tag{MH14}
\]
The horizontal flow above supplies such a lift along a base flow.
Disintegration, tested against an arbitrary joint function, gives
\[
(T_\epsilon)_*\mu(dz,dy)
=(\phi_\epsilon)_*\nu(dz)\,\beta_z(dy).
\]
Consequently its actual likelihood and relative entropy are
\[
\boxed{
\frac{d(T_\epsilon)_*\mu}{d\mu}(z,y)
=\frac{d(\phi_\epsilon)_*\nu}{d\nu}(z),\qquad
D((T_\epsilon)_*\mu\Vert\mu)
=D((\phi_\epsilon)_*\nu\Vert\nu).
}
\tag{MH15}
\]
Thus for base velocity \(h\), the pushed-law score and its Fisher
pairing are
\[
S_h=-\operatorname{div}_\nu h,\qquad
g(h,k)=\int S_hS_k\,d\nu.
\tag{MH16}
\]
These are likelihood identities, not a choice of the Riemannian
metric in (MH6). The pointwise derivative on a joint observable
remains \(D_hF=d_ZF[h]+d_YF[v_h]\). Its score can be basic while
its observable derivative is not.

For a different retained-source experiment with readout \(R\),
differentiation of the marginal density instead gives
\[
S_{\rm marginal}=\mathbb E[S_{\rm source}\mid R],\qquad
g_{\rm source}-g_{\rm marginal}
=\mathbb E\operatorname{Cov}(S_{\rm source}\mid R)\ge0,
\tag{MH17}
\]
as a matrix or quadratic-form identity whenever the scores are
square-integrable. Therefore constructing (MH14) over an endpoint
law does not preserve a pre-existing path-source Fisher pairing.
It constructs an experiment whose likelihood contains only that
endpoint information. The
[[gauge-source-action-transport/source-action-transport-through-ordered-cuts|retained-source cut test]]
gives a strict compact-group example and an alternative that
transports the complete source.

Adding a conditionally divergence-free vertical velocity preserves
(MH15)--(MH16), but can change \(D_hF\) for nonbasic \(F\). Neither
the state nor this Fisher pairing alone selects the full connection.

## Gauge equivariance supplies a partial lift without inversion

For a finite raw link split \(G^{A\sqcup B}\), use the product
bi-invariant metric and a smooth strictly positive, vertex-gauge-
invariant joint density \(\rho(a,b)\). This includes the actual
finite-regulator vacuum density, not only a Wilson Gibbs law.
Let \(\beta_a(b)=\rho(a,b)/\rho_A(a)\). For vertex parameters
\(\xi\in\mathfrak g^V\), write the restricted gauge tangents in
the matrix frame \(\delta a_e\,a_e^{-1}\) as
\[
(\mathsf G_A(a)\xi)_e=\xi_{s(e)}-\operatorname{Ad}_{a_e}\xi_{t(e)},
\qquad
(\mathsf G_B(b)\xi)_e=\xi_{s(e)}-\operatorname{Ad}_{b_e}\xi_{t(e)}.
\tag{GE1}
\]
Gauge invariance and invariance of hidden Haar measure imply
\[
\beta_{g_Aa}(g_Bb)=\beta_a(b),\qquad
d_A\log\beta_a[\mathsf G_A\xi]
=-\mathsf G_B\xi\log\beta_a.
\tag{GE2}
\]
The marginal is gauge invariant. Since a fixed-parameter
\(\mathsf G_B\xi\) preserves Haar volume, (GE2) is precisely
\[
d_A\beta_a[\mathsf G_A\xi]
+\operatorname{div}_B(\beta_a\mathsf G_B\xi)=0.
\]
Thus \(h=\mathsf G_A\xi,\ v_h=\mathsf G_B\xi\) solves (MH3)
along a labelled gauge motion, without a conditional Poisson
inverse or spectral assumption.

At one vertex \(v\), with \(d_v^A>0\) retained incident edges
and no self-loops, the map from its parameter is injective:
\[
|\mathsf G_v^A\xi|^2=d_v^A|\xi|^2,\qquad
|\mathsf G_v^B\xi|^2=d_v^B|\xi|^2.
\tag{GE3}
\]
Its lift has norm \(\sqrt{d_v^B/d_v^A}\). Combining vertex
directions is a different problem: their retained motions can
cancel on shared links.

In particular, \(\mathsf G_B\xi\) descends to a function of
the tangent \(h=\mathsf G_A\xi\), preserving **every labelled
motion**, exactly when
\(\ker\mathsf G_A\subseteq\ker\mathsf G_B\).
A retained stabilizer \(\zeta\in\ker\mathsf G_A\) instead
satisfies
\[
\operatorname{div}_B(\beta_a\mathsf G_B\zeta)=0.
\tag{GE4}
\]
It may move hidden observables while leaving their conditional
law unchanged. The intrinsic lift is therefore specified
modulo this vertical circulation, not necessarily as one vector
field on the ordinary retained tangent bundle.

The product metric supplies one representative on every
constant-rank stratum:
\[
v_h(b)=\mathsf G_B(b)\mathsf G_A(a)^\dagger h,\qquad
h\in\operatorname{Ran}\mathsf G_A(a).
\tag{GE5}
\]
The Moore--Penrose inverse minimizes parameter norm. Its
coefficients depend only on \(a,h\), so (GE4) makes it
law-preserving. This is not generally minimum conditional
transport cost. A pointwise hidden-norm minimization may use
coefficients depending on \(b\); even if each \(Z_j\) preserves
\(\beta_a\), the field \(\sum_jc_j(b)Z_j\) has weighted
divergence \(\sum_jZ_jc_j\), which need not vanish.

## The metric-selected gauge lift can diverge at a stabilizer

This failure occurs on a fixed pair of adjacent squares.
Retain the left square \(A\), with three links equal to \(I\)
and its closing link \(e^{\varepsilon T_3}\), and take all
hidden links to be \(I\). Here \(T_1,T_3\) are orthonormal
\(SU(2)\), \(Q=-2\operatorname{Tr}\), generators. Put
\(\xi=T_1\) at all four retained vertices and zero at the two
remaining vertices.

For small nonzero \(\varepsilon\), the retained stabilizer on
its four vertices is the common \(T_3\) direction. The chosen
\(\xi\) is orthogonal to that kernel and to parameters at
vertices untouched by \(A\), so
\[
\mathsf G_A^\dagger\mathsf G_A\xi=\xi,\qquad
|\mathsf G_A\xi|=2|\sin(\varepsilon/2)|,\qquad
|\mathsf G_B\xi|=\sqrt2.
\tag{GE6}
\]
The last value comes from the two hidden edges leaving the
retained square. Therefore the representative (GE5) has norm
at least \(\sqrt2/[2|\sin(\varepsilon/2)|]\).
It is unbounded near the retained stabilizer wall even on
this fixed graph. Smooth positive vacuum densities do not
exclude its neighborhoods.

This is not an obstruction to every law-preserving lift:
(MH2) still gives a smooth bounded full-tangent lift on each
fixed compact smooth positive family. The divergence concerns
this metric-selected gauge representative; at the wall its
large motion tends toward conditional-law-preserving circulation.
It is not a divergent physical mass or a failure of the
underlying smooth state.

More fundamentally, these explicit gauge lifts cover the wrong
directions for a direct physical gap argument. If \(F\) is
invariant under the **whole** vertex action, then
\[
D_hF=(\mathsf G_A\xi+\mathsf G_B\xi)F=0,\qquad
d_A(P_AF)[h]=0.
\tag{GE7}
\]
A retained tree has no other tangent directions, but its
gauge-invariant observable algebra is only constants. Retained
cycles introduce genuine shape directions, which (GE2) does
not transport. The
[[coarse-response-memory/boundary-interaction-and-conditional-score-budget#The physical estimate sees only the shape component|quotient-horizontal response criterion]]
identifies their exact conditional estimate. Gauge symmetry
alone leaves every admissible joint density in play; it has
not selected that response or its spectrum.

The [[receipts/measure_preserving_lift_receipt.py|finite receipt]] checks conditional differentiation, curved transport and shear estimates on smooth circle families. It is not a simulation of continuum Yang--Mills.
