# Partial Bochner Bounds for a Ground-State Score

Positive Ricci curvature bounds each component of a positive ground state's logarithmic gradient by the potential force in that component. On a product, the bound contains no factor counting the other components. The mixed derivatives enter as nonnegative squares rather than uncontrolled interactions. This provides a local estimate for an unknown joint state without replacing it by a product or prescribing a positive Hessian for its logarithm.

**Status: exact finite compact-carrier estimates.** The metric, kinetic coefficients and potential are inputs. The primary score bound controls ground-state regularity, not the spectral gap by itself. A separate neutral single-plaquette quotient estimate is proved below; no continuum Yang--Mills bound is claimed.

## The supplied operator and the derived score

Let \(M=\prod_{e\in E}M_e\), with each factor connected, compact
and without boundary. Use the product metric and volume, and let
\(\Delta_e\) have nonpositive spectrum. Supply
\[
H=-\sum_e\kappa_e\Delta_e+V,\qquad
\kappa_e>0,\quad V\in C^\infty(M,\mathbb R).
\tag{PB1}
\]
The operator has its compact elliptic \(H^2\) domain. Its normalized
ground vector \(\psi\) can be chosen smooth and strictly positive;
positivity improvement makes it unique. Put \(u=\log\psi\). The
eigenvalue equation becomes
\[
\sum_e\kappa_e\bigl(\Delta_eu+|\nabla_eu|^2\bigr)=V-E_0.
\tag{PB2}
\]
The ground-state transform acts on scalar functions:
\[
\mathcal L=-\psi^{-1}(H-E_0)\psi
=\sum_e\kappa_e(\Delta_e+2\nabla_eu\cdot\nabla_e).
\tag{PB3}
\]
It is nonpositive in \(L^2(\psi^2\,d\mathrm{vol})\). Its existence
is not being derived from the bound below.

Suppose \(\operatorname{Ric}_e\ge\rho_e g_e\), with \(\rho_e>0\).
Then
\[
\boxed{\|\nabla_e\log\psi\|_\infty
\le\frac{\|\nabla_eV\|_\infty}{\kappa_e\rho_e}.}
\tag{PB4}
\]
The norms and supremum are on the full product, not at a fixed
configuration of the other factors.

## Why the other factors introduce no volume factor

Set \(v_e=|\nabla_eu|^2\). The product connection and partial
Bochner identity give
\[
\frac12\mathcal L v_e
=\sum_j\kappa_j|\nabla_j\nabla_eu|^2
 +\kappa_e\operatorname{Ric}_e(\nabla_eu,\nabla_eu)
 +\langle\nabla_eu,\nabla_eV\rangle.
\tag{PB5}
\]
Indeed, differentiating the squared-gradient term in (PB2)
produces the mixed Hessian terms cancelled by the drift in
(PB3). The remaining mixed second derivatives are the
nonnegative squares displayed in (PB5). Curvature occurs only
in the \(e\)-th factor; the product has no mixed curvature.

At a global maximum of \(v_e\), its drift derivative vanishes
and every partial Laplacian is nonpositive. If
\(m_e=\|\nabla_eu\|_\infty\), (PB5) yields
\[
0\ge \kappa_e\rho_em_e^2-m_e\|\nabla_eV\|_\infty.
\]
For \(m_e>0\), divide by \(m_e\); for \(m_e=0\), (PB4) is
immediate. Neither \(E_0\), the normalization of \(\psi\), nor a
lower bound on \(\psi\) enters the estimate.

This is not a Bakry--Emery lower bound for the transformed
operator. No sign has been established for the Hessian of
\(-2\log\psi\), so (PB4) cannot be substituted for its weighted
curvature or for a state Poincare inequality.
[[coarse-response-memory/kinetic-hessian-bootstrap-and-uniform-response|A separate forced Killing-score bootstrap]]
does obtain a full Hessian bound throughout actual preparation
under an explicit small local-force condition. Its closed
Riccati inequality is additional work, not a consequence of
the first-score estimate alone.

## Compact gauge normalization

For \(SU(2)\) with \(Q=-2\operatorname{Tr}\), the round-sphere
radius is two and \(\operatorname{Ric}=Q/2\), as fixed in
[[holonomy-state-refinement/heat-state-continuity-and-response-closability|the heat-state normalization]].
A plaquette function \(q_p=\tfrac12\operatorname{Tr}\operatorname{Hol}_p\)
satisfies \(|\nabla_eq_p|\le1/2\) for each single edge occurrence.
For common \(\kappa\) and
\(V=\lambda\sum_p(1-q_p)\), (PB4) gives
\[
\boxed{\|\nabla_e\log\psi_\lambda\|_\infty
\le\lambda n_e/\kappa,\qquad\lambda\ge0.}
\tag{PB6}
\]
Here \(n_e\) counts incident occurrences. For elementary
plaquettes of an open three-dimensional cubical box, \(n_e\le4\).
The bound is uniform in the number of links, at fixed
\(\lambda/\kappa\), and requires no small-coupling hypothesis.
It is proved on the smooth raw product before the singular gauge
quotient. Gauge invariance of the positive vacuum then gives
the same score for physical readouts.

[[coarse-response-memory/local-score-bounds-and-the-order-of-hidden-response|The full-readout application]]
uses this bound to control conditional projection and hidden
first derivatives. It also shows why joining two readouts can
produce a hidden second derivative that this estimate cannot
control in the same norm.

The positive Ricci denominator is essential to this proof. A
torus factor does not meet that hypothesis. More general
compact semisimple groups require their actual metric Ricci
constant and representation-gradient bounds; the numerical
\(SU(2)\) constants must not be copied unchanged. Finite-product
uniformity alone does not construct an infinite-product vacuum
or a continuum Yang--Mills theory.

## A product reference turns the force into a boundary force

The complementary Killing-score identities below require no positive
weighted curvature. They control an integrated energy pairing, whereas
the following weighted argument controls a pointwise score.

There is a conditional extension useful when a region contains
many internally interacting links. Let \(M=M_A\times M_B\),
\(H_0=H_A+H_B\), with common kinetic coefficient \(\kappa\).
Its positive ground vector is
\(\phi=\phi_A\phi_B\). Let \(\psi\) be the positive ground vector
of \(H_0+W\), and put \(u=\log(\psi/\phi)\). Then
\[
\kappa\bigl(\Delta u+2\nabla\log\phi\cdot\nabla u
                  +|\nabla u|^2\bigr)=W-(E-E_0).
\tag{PB7}
\]
The relevant curvature is now the **full regional tensor**
\[
\mathcal R_A=\operatorname{Ric}_A
             -2\operatorname{Hess}_A\log\phi_A.
\]
Since \(\log\phi\) splits across \(A,B\), partial weighted
Bochner gives
\[
\frac12\mathcal L_\psi|\nabla_Au|^2
=\kappa\sum_{j=A,B}|\nabla_j\nabla_Au|^2
 +\kappa\mathcal R_A(\nabla_Au,\nabla_Au)
 +\langle\nabla_Au,\nabla_AW\rangle.
\tag{PB8}
\]
Consequently, **if** \(\mathcal R_A\ge r_Ag_A\) everywhere
for \(r_A>0\), the same maximum argument proves
\[
\boxed{\|\nabla_A\log(\psi/\phi)\|_\infty
\le\frac{\|\nabla_AW\|_\infty}{\kappa r_A}.}
\tag{PB9}
\]
No \(B\)-region curvature bound is needed. Diagonal linkwise
bounds on \(\mathcal R_A\) would not suffice: the mixed Hessian
of the internally correlated \(\phi_A\) belongs to this tensor.

For the raw regional readout in
[[coarse-response-memory/boundary-interaction-and-conditional-score-budget|the boundary-budget construction]],
the reference score \(\nabla_A\log\phi_A\) is retained.
Its conditional covariance therefore cancels, giving
\[
\begin{aligned}
M_A&\le\frac{\|\nabla_AW\|_\infty^2}{\kappa^2r_A^2}I,\\
\|B_Af\|^2&\le
\frac{4\|\nabla_AW\|_\infty^2}{\kappa r_A^2}\,a_A[f].
\end{aligned}
\tag{PB10}
\]
For \(W=-\lambda\sum_{p\in\partial}q_p\), let
\(n_e^\partial\) count crossing plaquettes incident to \(e\).
In an open three-dimensional cubical graph,
\[
\boxed{\|B_Af\|^2\le
\frac{\lambda^2\sum_{e\in A}(n_e^\partial)^2}
     {\kappa r_A^2}\,a_A[f]
\le\frac{12\lambda^2N_\partial}{\kappa r_A^2}\,a_A[f].}
\tag{PB11}
\]
Indeed \(|\nabla_eq_p|\le1/2\), \(n_e^\partial\le4\), and a
crossing square has at most three edges in \(A\).
This is a boundary-scaled form estimate only when the new
\(r_A\) has the required uniformity. Positive reference weighted
curvature would itself imply a regional Poincare estimate;
it is a substantive additional assumption, not a consequence
of the first-score bound (PB4).

## The required reference curvature can already be negative

Take \(A\) to be a single four-link plaquette and write its
actual ground vector as \(\phi_A=f(q)>0\). Its radial equation is
\[
-\kappa(1-q^2)f''+3\kappa qf'
 +\lambda(1-q)f=E_Af.
\tag{PB12}
\]
Smoothness at \(q=-1\) gives
\[
\frac{f'(-1)}{f(-1)}=\frac{2\lambda-E_A}{3\kappa}.
\tag{PB13}
\]
At holonomy \(-I\), move all four links coherently, each with
speed \(1/2\) in a \(Q\)-unit Lie algebra direction, including
the orientation signs. This is a unit product tangent \(v\)
and its holonomy trace is \(q(t)=-\cos t\). Therefore
\[
\boxed{
\mathcal R_A(v,v)
=\frac12-\frac{2(2\lambda-E_A)}{3\kappa}.}
\tag{PB14}
\]
The product Ricci term is \(1/2\); \(q'(0)=0\) and \(q''(0)=1\)
give the Hessian term. This is a calculation on the smooth
raw group product, not a singular-coordinate assumption.

The constant trial vector has energy \(\lambda\), and is not
an eigenvector when \(\lambda>0\). Hence \(E_A<\lambda\), so
\[
\mathcal R_A(v,v)<0\qquad(\lambda\ge3\kappa/4).
\tag{PB15}
\]
Thus (PB11) cannot be promoted to an automatic all-coupling
theorem for the actual Wilson vacuum. With \(\kappa=\lambda=1\),
the [[coarse-response-memory/receipts/two_plaquette_vacuum_receipt.py|existing plaquette receipt]]
finds approximately \(-0.22129455\), independently comparing
the endpoint character derivative with (PB13). The analytic
sign follows from the variational argument, not that decimal.

Negative weighted curvature does not mean absence of a gap or
failure of every boundary estimate.
[[conditional-fisher-coercivity/linear-tilted-sphere-coercivity|The linear-tilted sphere]]
already separates those claims in a different law.
Here the failed step is specifically replacing unknown
regional Hessian control by bare compact-group curvature.

## The invariant plaquette quotient has positive weighted curvature

The failure of the **raw** tensor in (PB14) is not the answer
on every subcarrier. For the same single-plaquette reference
set \(q=\cos\theta\), \(0<\theta<\pi\), and
\[
g(\theta)=\sin\theta\,f(\cos\theta)>0.
\]
The neutral quotient has measure
\(d\nu=(2/\pi)g^2d\theta\) and inherited form
\(\kappa\int|F'(\theta)|^2d\nu\).
The sine factor is the Haar orbit-volume Jacobian, not a
new potential fitted to the state. Equation (PB12) becomes
\[
-\kappa g''+\lambda(1-\cos\theta)g=(E_A+\kappa)g,\qquad
g(0)=g(\pi)=0.
\tag{QB1}
\]
These Dirichlet conditions are for \(g\), not for the observable
\(F\). The latter retains the conservative weighted form
inherited from smooth invariant functions on the raw group.

An elementary Riccati argument proves strict log-concavity.
Put \(p=(\log g)'\), \(r=p'\). Then
\[
p'=\frac{\lambda(1-\cos\theta)-E_A-\kappa}{\kappa}-p^2,
\qquad
r'=\frac{\lambda}{\kappa}\sin\theta-2pr.
\tag{QB2}
\]
Smooth positivity of \(f\) at both endpoints gives
\(r=-\theta^{-2}+O(1)\) near zero and
\(r=-(\pi-\theta)^{-2}+O(1)\) near \(\pi\).
For \(\lambda>0\), any interior zero of \(r\) would be a
strict upward crossing by (QB2). A function negative at
both ends cannot have only upward zero crossings. Hence
\(r<0\) everywhere. At \(\lambda=0\), \(g=\sin\theta\)
and \(r=-\csc^2\theta\) directly.
Consequently
\[
\boxed{
\rho_\lambda:=\inf_{0<\theta<\pi}
[-2(\log g)'']>0
\quad\text{at every fixed finite }\lambda/\kappa.
}
\tag{QB3}
\]
The curvature diverges positively at the endpoints, so the
strictly positive infimum is attained in the interior.
This proves a sign without inserting a convexity assumption
on the raw vacuum or the nonconvex cosine potential.

The one-dimensional weighted Poincare inequality then gives
\[
\kappa\int|F'|^2d\nu
\ge\kappa\rho_\lambda\operatorname{Var}_\nu(F).
\tag{QB4}
\]
One may first apply the weighted-curvature estimate on
\([\varepsilon,\pi-\varepsilon]\) with conservative endpoint
conditions and normalized restricted measure, then let
\(\varepsilon\) decrease to zero for the smooth invariant
core and extend by form closure. No absorbing condition on
physical observables is introduced.

This angular argument is a finite **neutral quotient** result.
It supplies no uniform lower bound on \(\rho_\lambda\) along
an unbounded coupling trajectory. The latitude argument below
does supply a uniform Poincare estimate by a different test,
but neither is a multi-plaquette quotient theorem or a
substitute for the full mixed regional tensor in (PB9).
The actual joint vacuum still carries shape--fiber coupling.
[[coarse-response-memory/boundary-interaction-and-conditional-score-budget#The physical estimate sees only the shape component|The projected conditional criterion]]
states that separate obligation.
The existing character receipt checks the quotient-curvature
formula on its finite samples; strict positivity in (QB3)
comes from the differential argument, not those samples.

## A latitude estimate is uniform in magnetic coupling

For the supplied single-plaquette operator (PB12), start its
positive heat amplitude at \(f_0(a)=1\), and put
\(w_t(a)=\log f_t(a)\), \(p=\partial_aw\),
\(v=\partial_a^2w\), \(h=1-a^2\). Scalar normalization
does not affect these derivatives. The exact equations are
\[
\begin{aligned}
\partial_tw&=\kappa[h(w''+(w')^2)-3aw']-\lambda(1-a),\\
\partial_tv&=\kappa\left[
h v''+(2hp-7a)v'+(-8-8ap)v+2hv^2-2p^2\right].
\end{aligned}
\tag{QB5}
\]
The second equation is obtained by twice differentiating
the first; in particular the magnetic term has no second
latitude derivative. Smooth radial invariance gives smooth
functions of \(a\) up to both endpoints, and strict
positivity on each compact finite-time cylinder makes all
the displayed coefficients bounded there.

The condition \(v\le0\) is preserved. Regard \(2hv^2\)
as the bounded zero-order coefficient \(2hv\) multiplying
\(v\), and apply the maximum principle with an exponential
barrier. At an interior positive maximum the diffusion and
drift terms have the required sign, while the source
\(-2p^2\) is nonpositive. At \(a=\pm1\), the diffusion
coefficient vanishes and the drift \(-7a\) points inward;
the one-sided derivative gives the same maximum argument.
No additional boundary condition is imposed in the
degenerate latitude chart. Since \(v_0=0\),
\[
\boxed{\partial_a^2\log f_t\le0\quad(t\ge0).}
\tag{QB6}
\]
For this fixed compact elliptic problem, normalized heat
converges in every smooth norm to the positive ground
vector. This uses the already established fixed-system
spectral isolation, not a uniform estimate. Taking the
limit in (QB6) proves \((\log\phi_\lambda)''\le0\) at
every finite \(\lambda\ge0\).

Apply
[[conditional-fisher-coercivity/linear-tilted-sphere-coercivity#Concave radial amplitudes retain the same bound|the concave-amplitude latitude inequality]]
to the actual ground marginal
\(d\nu_\lambda\propto\phi_\lambda(a)^2\sqrt h\,da\).
It gives the coupling-independent neutral bound
\[
\boxed{
\kappa\int h|F'|^2d\nu_\lambda
\ge\kappa\operatorname{Var}_{\nu_\lambda}F
\qquad(0\le\lambda<\infty).
}
\tag{QB7}
\]
The proof applies first on the inherited smooth invariant
core and extends by weighted form closure, as in (LT10).
It is not an optimal-constant claim: at \(\lambda=0\) the
neutral Haar gap is \(3\kappa\). Uniformity is in magnetic
coupling for this one supplied plaquette at fixed electric
coefficient; it is not a volume or continuum estimate.

Unlike angular log-concavity, latitude log-concavity survives
the rapidly tilted initial layer. The
[[coarse-response-memory/heat-preparation-and-latitude-coercivity#The actual heat trajectory can leave the stationary shape class|interacting trajectory test]]
explains that distinction. The coupled conditional terms
there prevent simply copying (QB5) to a many-plaquette
marginal. The actual two-plaquette preparation now satisfies
the condition for all times on a fixed small-coupling range,
by its full-evolution coefficient and uniform remainder.
An arbitrary-coupling or many-plaquette extension remains
a separate construction problem.

## Killing derivatives give an exact energy-weighted response

Return to the absolute score \(u=\log\psi\), common \(\kappa\),
\(\rho=\psi^2\), and \(K=-\mathcal L_\psi\). Let \(X,Y\) be fixed
Killing fields commuting with the kinetic Laplacian; constant
left/right link translations on a bi-invariant compact group qualify.
They preserve Haar volume. On the smooth raw compact carrier,
\[
\begin{aligned}
r_X&=Xu,\qquad \mathbb E_\rho r_X=0,\\
\mathcal L_\psi r_X&=XV,\\
\mathcal L_\psi(YXu)
+2\kappa\langle\nabla r_X,\nabla r_Y\rangle&=YX V.
\end{aligned}
\tag{KS1}
\]
Indeed a Killing field differentiates the metric gradient pairing
without a metric-variation term, and commutes with \(\Delta\).
Differentiate (PB2), then use
\([Y,\mathcal L_\psi]f=2\kappa\langle\nabla Yu,\nabla f\rangle\).
The second line is therefore not an equation with a discarded
mixed Hessian. Every displayed function lies in the compact elliptic
operator domain.

Stationarity and Haar integration by parts give
\[
\boxed{
\mathcal E_K(r_X,r_Y)
=\kappa\mathbb E_\rho\langle\nabla r_X,\nabla r_Y\rangle
=\tfrac12\mathbb E_\rho(YX V),\qquad
\mathbb E_\rho(YXu)=-2\mathbb E_\rho(r_Yr_X).
}
\tag{KS2}
\]
Commutation of \(X,Y\) is unnecessary: the antisymmetric difference
is \(\mathbb E_\rho([Y,X]V)=0\), by (KS1) for the Killing field
\([Y,X]\). In particular, the mixed score \(YXu\) is generally
not centered.

For a finite family of controls, define
\(R:\mathbb R^m\to L^2_0(\rho)\) by \(R\xi=X_\xi u\).
Its energy Gram is \(R^*KR\), interpreted as a form pullback;
its unweighted Gram is \(R^*R\). In this smooth finite setting,
\[
R^*KR=\tfrac12\mathbb E_\rho[\operatorname{Hess}_{\rm action}V]
\ge0.
\tag{KS3}
\]
The action Hessian means the symmetrized second variation under the
declared isometric controls, not an assumed pointwise convex
potential. The positivity is an averaged consequence of the
ground-state equation.

This is an instance of the established energy-weighted
double-commutator sum rule, not a newly invented spectral principle;
[[library/transition-sum-rules-in-the-shell-model/inq|Lu and Johnson]]
describe its spectral-moment meaning. Directly, for
\(P_X=-iX\) on Haar \(L^2\),
\[
\tfrac12\langle\psi,[P_X,[H,P_Y]]\psi\rangle
=\operatorname{Re}\langle P_X\psi,(H-E_0)P_Y\psi\rangle.
\]
The identification \(P_X\psi=-i\psi r_X\) gives (KS2).
A first spectral moment does not determine its lower support edge;
[[coarse-response-memory/spectral-readout-and-the-visible-gap|the full spectral readout]]
requires more information.

For a \(Q\)-unit \(SU(2)\) generator on one link,
\(X^2q_p=-q_p/4\) whenever that link occurs once in \(p\). Thus
\[
\boxed{
\mathcal E_K(r_X)=\frac{\lambda}{8}
\sum_{p\ni e}\mathbb E_\rho q_p\le\frac{\lambda n_e}{8}.
}
\tag{KS4}
\]
If two links share no plaquette, their energy-Gram entry vanishes
exactly. This is not independence, a pointwise vanishing mixed
score, or sparsity of the conditional covariance.
[[prepared-vacuum-fisher-comparison/physical-vacuum-lift-and-fisher-comparison#The score energy is a plaquette-corner response|The endpoint gauge decomposition]]
turns (KS4) into a volume-uniform matrix bound and a separate
charged-sector covariance bound.

The single-plaquette check does not project away this charge.
Write its based holonomy as \((q,\mathbf b)\), \(h=1-q^2\),
\(\psi=f(q)\), \(u=\log f\). A unit endpoint score is
\(r=-u'b_a/2\). Each of the four link differentials of holonomy
is an isometry, and the angular mean is \(b_a^2=h/3\). Hence
\[
\mathcal E_K(r)=\frac{\kappa}{12}
\int f^2\bigl[(hu''-qu')^2+2(u')^2\bigr]\,d{\rm Haar}(q),
\qquad
\|r\|_\rho^2=\frac1{12}\int f^2h(u')^2\,d{\rm Haar}(q).
\tag{KS5}
\]
The existing plaquette receipt evaluates these using character
derivatives and compares the first integral with
\(\lambda\langle q\rangle/8\). It is a finite numerical check
of the proved raw-carrier identity, not a physical-gap estimate.

## Conditioning retains a divergence that averaging removes

For a raw product split \(A,B\), put
\(\rho_A=\int\rho\,dB\) and \(P_A F=\mathbb E_\rho[F\mid A]\).
Integration of the divergence form of \(\mathcal L_\psi\) over
the compact hidden factor gives, for any smooth \(F\),
\[
P_A\mathcal L_\psi F
=\frac{\kappa}{\rho_A}
\operatorname{div}_A\bigl(\rho_A P_A\nabla_A F\bigr).
\]
Applying this to \(F=YXu\) in (KS1) yields
\[
\boxed{
2\kappa P_A\langle\nabla r_X,\nabla r_Y\rangle
=P_A(YX V)
-\frac{\kappa}{\rho_A}
\operatorname{div}_A\bigl(\rho_A P_A\nabla_A(YXu)\bigr).
}
\tag{KS6}
\]
The last term vanishes after integrating \(A\), not at each retained
configuration. It prevents replacing the integrated sparse response
by a sparse conditional tensor. In particular, (KS2) alone does not
bound the essential supremum of
\(M_A=\operatorname{Cov}_\rho(\nabla_Au\mid A)\) needed in
[[coarse-response-memory/boundary-interaction-and-conditional-score-budget|the exact differentiation--forgetting response]].
An inverse estimate must likewise identify its sector: the raw
charged score has a gauge-orbit bound, but the neutral physical
gap and the conditional-fiber estimate do not follow from it.
