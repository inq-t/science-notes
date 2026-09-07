# Overlap Kernels and Face Refinement

A faithful matrix-group comparison can determine a joint gauge law after face refinement: normalized powers of an anchored trace overlap converge, under convolution, to a heat kernel, and exact boundary integration turns those convolutions into coarse plaquette weights. This is a worked application of Chevyrev–Garban's carpet-refinement theorem, not a new four-dimensional construction. It advances from a comparison on one state space to boundary amplitudes on a supplied finite box, while exposing the many-channel composition that full spatial refinement must control. Temporal sewing distinguishes a declared anisotropic clock limit from a same-weight scheme whose fixed-carrier limit is singular.

**Status: [EXACT APPLICATION OF KNOWN RESULTS] for the compact-group limit and fixed-box gauge law; [EXACT] for finite boundary integration, the anisotropic fixed-spatial-graph clock limit, and the fixed-carrier same-weight obstruction; [OPEN] for arena selection, a full four-dimensional continuum family and its physical gap.**

## The comparison and its choices

Fix a nontrivial compact connected Lie group \(G\), normalized Haar measure
\(dg\), and a faithful finite-dimensional unitary representation
\(R:G\to U(r)\). On its Lie algebra put
\[
Q_R(X,Y)=-\operatorname{ReTr}(dR(X)dR(Y)).
\tag{OF1}
\]
Faithfulness makes this a positive definite, adjoint-invariant inner
product. It defines a bi-invariant metric and a nonpositive Laplacian
\(\Delta_{Q_R}\). For \(\chi=\operatorname{Tr}R\), choose
\[
\kappa(g)=\frac{2r+\operatorname{Re}\chi(g)}{3r},
\qquad \frac13\le\kappa(g)\le1,
\qquad \kappa(g)=1\Longleftrightarrow g=e.
\tag{OF2}
\]
This is literally an overlap. In the real Hilbert space
\(\mathbb R\oplus M_r(\mathbb C)_{\mathbb R}\), with real Frobenius pairing,
\[
v_g=\frac{(\sqrt{2r},R(g))}{\sqrt{3r}},
\qquad \|v_g\|=1,\qquad
\langle v_g,v_h\rangle=\kappa(g^{-1}h).
\tag{OF3}
\]
Integer powers are overlaps of feature tensors. As in
[[algebra/primitive-overlap-refinement-and-the-emergent-diffusion|primitive overlap refinement]],
these tensors do not supply a physical composite observable algebra.

Let
\[
p_N(g)=Z_N^{-1}\kappa(g)^{N^2},\qquad
Z_N=\int_G\kappa(g)^{N^2}\,dg,\qquad B_Nf=p_N*f
\tag{OF4}
\]
on the complete carrier \(L^2(G,dg)\). These are symmetric Markov
contractions and Hilbert-positive: \(\kappa=\tfrac23\mathbf1+
(\chi+\bar\chi)/(6r)\) has a nonnegative character expansion, as do its
integer powers. They are nevertheless finite-rank with exact zero modes.
Strict positivity of a density is not injectivity of its convolution
operator; \(-\log B_N\) is not a finite generator on the whole carrier.

The anchor is a choice, not a necessary natural number. Replacing
\(2\) by \(a>1\) in \((ar+\operatorname{Re}\chi)/((a+1)r)\) changes the
limiting diffusion coefficient to \((a+1)r/2\). The representation,
comparison law and matching of exponent \(N^2\) to subdivision count
are inputs.

## The local Hessian fixes the convolution limit

Set \(S=-\log\kappa\). Expanding the real trace in exponential coordinates,
with odd powers removed by inversion symmetry, gives
\[
S(\exp X)=\frac{Q_R(X,X)}{6r}+O(\|X\|^4).
\tag{OF5}
\]
The unique zero, compactness and nondegenerate Hessian give constants
\(\theta,\Theta,\rho_0>0\) such that
\[
S(g)\ge\theta\,\operatorname{dist}_{Q_R}(e,g)^2\quad(g\in G),
\qquad
S(g)\le\Theta\,\operatorname{dist}_{Q_R}(e,g)^2
\quad(\operatorname{dist}_{Q_R}(e,g)<\rho_0).
\tag{OF6}
\]
Thus \(S_N=N^2S\) satisfies Assumption 2.1(b) of
[[library/villain-action-in-lattice-gauge-theory/inq|Chevyrev–Garban]],
including its shrinking-ball upper bound.

For smooth odd coordinates \(\zeta\) agreeing with logarithm near \(e\),
in a \(Q_R\)-orthonormal basis, Laplace localization yields
\[
Z_N\asymp N^{-\dim G},\qquad
\mathbb E_{p_N}\zeta=0,\qquad
N^2\mathbb E_{p_N}[\zeta_a\zeta_b]\longrightarrow3r\,\delta_{ab}.
\tag{OF7}
\]
Rescaling \(X=Y/N\) leaves the Gaussian \(\exp(-|Y|^2/(6r))\).
For every closed \(C\) away from \(e\),
\(N^2\int_Cp_N(g)\,dg\to0\) exponentially:
this supplies the no-jump condition, not just unscaled concentration.
The diffusion central limit theorem used in their Lemma 2.4, applied at
step count \(N^2\) with these stronger tail bounds, therefore gives
\[
q_N(g)\,dg:=p_N^{*N^2}(g)\,dg\ \Longrightarrow\ h(g)\,dg,
\qquad
h=\text{heat density of }\exp\!\left(\frac{3r}{2}\Delta_{Q_R}\right)
\text{ started at }e.
\tag{OF8}
\]
Their convention \(V_\beta=\exp(\Delta/(2\beta))\) gives \(h=V_{1/(3r)}\).

Weak convergence cannot justify multiplying face densities.
Equation (OF8) verifies Assumption 2.1(a); (OF6) verifies 2.1(b).
The paper's gradient estimate and Lemmas 4.1–4.2 then give
\[
\boxed{\|q_N-h\|_\infty\longrightarrow0.}
\tag{OF9}
\]
This is a cited analytic upgrade with checked hypotheses, not an inference
from convergence on finitely many representations.

For simple Lie algebra, \(Q_R=I_R(-B_{\rm Kill})\), so representation
dependence in the limiting differential operator is an overall rate
\(3r/(2I_R)\). Product factors and tori can retain relative metric choices;
global group topology and finite-\(N\) kernels retain further data.
The group heat parameter has not been identified with physical clock time.

## Integrating the shared edge produces a joint law

For bounded class densities \(p,q\) and fixed boundary products \(A,B\),
\[
\int_G p(Au^{-1})q(uB)\,du=(p*q)(AB).
\tag{OF10}
\]
The substitution \(v=Au^{-1}\) proves the displayed identity even without
centrality. Centrality makes face starting points and conjugacy classes
compatible. Iterated merging on a regularly tiled planar disk gives the convolution of
its face weights at its oriented boundary holonomy: Chevyrev–Garban's
Lemma 3.3. Boundary variables are retained during interior integration,
not separately projected to trivial charges.

The disk restriction matters. Two faces meeting only at one vertex have
no shared edge to integrate. With normalized class weights \(p\) and
\(1\), their retained amplitude is \(p(u)\), not
\((p*1)(uv)=1\). Thus the connected-planar-multigraph wording of that
lemma cannot be used without an additional geometric hypothesis. The
ordinary disk/carpet refinements here admit the required successive
face merging; arbitrary exposed boundaries instead require the full
amplitude (OF15).

Fix a finite hypercubic box \(\Gamma\) in dimension \(d\ge2\), with edges
\(E\) and plaquettes \(F\). Use **free exterior boundary conditions**:
all edge variables, including exterior-boundary edges, are Haar-integrated.
The carpet \(\Gamma_N\) subdivides each existing face into \(N^2\) microfaces
and each edge into \(N\) segments; it does not fill coarse cells with
additional transverse faces. Let \(\pi_N:G^{E_N}\to G^E\) multiply the
segments along coarse edges.

Choose the face-product incidence law
\[
d\mu_N(U)=\mathcal Z_N^{-1}
\prod_{f\in F_N}p_N(\operatorname{Hol}_fU)\prod_{e\in E_N}dU_e.
\tag{OF11}
\]
It is a positive gauge-invariant state on the commutative configuration
algebra, not yet a reconstructed quantum vacuum.
**The face-product prescription and the coarse box remain inputs.**
Integrate face interiors using (OF10); then product Haar pushes forward to
product Haar under coarse-edge multiplication. Exactly at every \(N\),
\[
\boxed{(\pi_N)_*\mu_N=\mu_{\Gamma,q_N},\qquad
d\mu_{\Gamma,q_N}
=\mathcal Z_{\Gamma,q_N}^{-1}
\prod_{f\in F}q_N(\operatorname{Hol}_fU)\prod_{e\in E}dU_e.}
\tag{OF12}
\]
Equation (OF9) gives the fixed-box specialization of their Theorem 1.5:
\[
\boxed{(\pi_N)_*\mu_N\longrightarrow\mu_{\Gamma,h}
\quad\text{in total variation}.}
\tag{OF13}
\]
This determines actual gauge-state expectations, beyond the carrier
isomorphism in [[gauge-boundary-frame-gluing/inq|Gauss gluing]].
The edge law is generally non-product. On a planar disk, however, a change
to face increments can expose independence; boundary correlation is not
evidence of interacting four-dimensional continuum dynamics.

[[heat-state-continuity-and-response-closability|The nested-loop heat-state test]]
uses the exact heat semigroup itself as an area-additive face law. It
constructs a projective state and computes the complete restricted
one-loop response bounds. Nevertheless, additive perimeter-gradient
forms fail closability on its continuum carrier: nearby loop
observables converge in the state norm while their edge responses
remain orthogonal. Exact state sewing and exact finite form consistency
are therefore not sufficient for a continuum clock.

The fixed-volume qualification is quantitative. Set \(M=|F|\),
\(m_h=\min_Gh>0\), and \(\epsilon_N=\|q_N-h\|_\infty\).
For total variation defined as a supremum over events,
\[
\|\mu_{\Gamma,q_N}-\mu_{\Gamma,h}\|_{\rm TV}
\le\min\left\{1,\left(1+\frac{\epsilon_N}{m_h}\right)^M-1\right\}.
\tag{OF14}
\]
Indeed, \(R(U)=\prod_f(q_N/h)(\operatorname{Hol}_fU)\) satisfies
\(|R-1|\le(1+\epsilon_N/m_h)^M-1\) by product expansion. With \(E\)
expectation under \(\mu_{\Gamma,h}\),
\[
E|R/ER-1|\le E|R/ER-R|+E|R-1|
=|1-ER|+E|R-1|\le2E|R-1|.
\]
The dependence on face count is explicit; fixed-box convergence is not
a volume-uniform estimate.

## What closes under full boundary integration?

The larger finite object is a boundary amplitude, not necessarily one
scalar weight of one loop. Assign each original face factor to exactly
one block \(C\), expose its links shared with other blocks, and integrate
only the remaining links:
\[
\mathcal A_C(u_{\partial C})
=\int \prod_{f\ {\rm assigned\ to}\ C}
w_f(\operatorname{Hol}_fU)\,dU_{\operatorname{int}C}.
\tag{OF15}
\]
For bounded nonnegative weights these are nonnegative finite boundary
functions. If blocks meet along exposed links \(\Sigma\), which become
internal on gluing, with no other crossing factors and no face counted
twice, then
\[
\mathcal A_{C\cup D}
=\int_{G^\Sigma}\mathcal A_C\,\mathcal A_D\,dU_\Sigma.
\tag{OF16}
\]
External variables remain as arguments. Tonelli makes successive
integrations associative. This finite boundary-function class closes
under elimination; a one-parameter face-weight family generally does not.
Normalize after the required gluing when the resulting partition function
is nonzero, retaining its partition factors. Strictly positive overlap and
heat weights ensure this; arbitrary nonnegative factors can glue to zero.

An interior edge of a full \(d\)-dimensional hypercubic mesh touches
\(2(d-1)\) plaquettes. For \(d=4\), elimination involves six factors:
\[
\int_G\prod_{j=1}^{6}w_j(A_j u^{\varepsilon_j}B_j)\,du,
\qquad \varepsilon_j\in\{+1,-1\}.
\tag{OF17}
\]
For finite Peter–Weyl sums, expand representation matrix elements and
reverse indices for negative orientations. Haar integration is then the
projector
\[
P_{\rm Inv}
=\int_G\bigotimes_jR_{\lambda_j}^{(\varepsilon_j)}(u)\,du
\quad\text{onto}\quad
\operatorname{Inv}\!\left(\bigotimes_jV_{\lambda_j}^{(\varepsilon_j)}\right),
\tag{OF18}
\]
with the contragredient representation for a negative orientation.
The weights \(p_N,q_N\) are finite character sums, and the smooth heat
weight also permits this expansion. For arbitrary bounded weights use
bounded approximation and continuity of integration; pointwise Fourier
convergence must not be assumed.
This is not generally one dual-pair invariant line. All intertwiner
multiplicities and exposed boundary indices must be retained.
Carpet integration leaves these multiply incident coarse edges in place;
(OF12) does not assert closure under a full four-dimensional mesh
refinement. The obstruction is to a restricted face-weight ansatz,
not a proof that four-dimensional Yang–Mills cannot exist.

For \(h_t\) the density of \(\exp(t(3r/2)\Delta_{Q_R})\) started at \(e\),
heat weights satisfy \(h_{t_1}*h_{t_2}=h_{t_1+t_2}\): planar subdivision
has an additive parameter, but not automatically Lorentzian clock time.
Writing \(-\log\mathcal A_C\) afterwards gives an effective boundary action
where the amplitude is strictly positive. Its gluing is a logarithm of
an integral of products, not bare addition of classical actions.
[[philosophy/principle-of-least-action/why-an-action-at-all|The action-composition audit]]
separates these operations.

The next target is a constrained family of boundary amplitudes and carriers
stable under many-channel contractions across the required refinements,
yielding physical transfer with the correct uniform rate. Equations
(OF15)–(OF16) supply finite composition, not a selected continuum-consistent
family. Neither density positivity nor Hilbert positivity of \(B_N\) alone
is a reflection-positivity or reconstruction theorem. The supplied group,
arena and symmetric comparison remain; the Jordan object has not been
shown to produce them. A compact group-diffusion gap is not the magnetic,
Gauss-restricted physical threshold in
[[contemporary-puzzles/yang-mills-mass-gap/finite-spacing-transfer-and-bounded-flux-solder|finite-spacing transfer]].

## Temporal sewing needs a separate refinement law

The face law permits an actual transfer construction, but sharpening a
comparison is not yet shortening a clock interval. Fix a finite spatial
graph with edges \(E\) and chosen plaquettes \(F_s\). On
\(\mathcal H=L^2(G^E,dU)\), with physical subspace
\(\mathcal H_{\rm GI}=\mathcal H^{G^V}\), set
\[
W(U)=\sum_{p\in F_s}S(\operatorname{Hol}_pU),\qquad
K_N=B_N^{\otimes E},\qquad \varepsilon_N=N^{-2}.
\tag{TS1}
\]
The function \(W\ge0\) is bounded, smooth and gauge invariant at this
fixed graph. Independent temporal-link comparisons in temporal gauge
give \(K_N\); spatial face factors supply the two half-slice multipliers.
Integrating temporal gauge links is equivalently Gauss projection,
which commutes with these operators and is the identity on
\(\mathcal H_{\rm GI}\). The
[[vacuum-aligned-innovation-completion/boundary-action-fixed-points-and-physical-linearization|sewn path-kernel identity]]
retains the endpoint halfweights and every intervening spatial factor.

### A full-carrier clock under declared anisotropic scaling

Fix a dimensionless \(\gamma\ge0\). Assign temporal faces their original
weight \(p_N\), but spatial faces the weight
\(\kappa^{\varepsilon_N\gamma}\). The actual slab operator is
\[
T_N=M_{e^{-\varepsilon_N\gamma W/2}}K_N
M_{e^{-\varepsilon_N\gamma W/2}}.
\tag{TS2}
\]
Fractional spatial powers need pointwise positivity here, not a
positive character expansion: they enter as a multiplication sandwich.
This proves Hilbert positivity in the chosen temporal direction; it
does not assert reflection positivity in every spatial direction.

By (OF9) and Young's convolution inequality,
\(\|B_N^{N^2}-e^{(3r/2)\Delta_{Q_R}}\|\to0\). Finite tensor products
therefore obey the blocked criterion (BR1) of
[[strong-coupling-gap-and-continuum-crossover/wilson-to-hamiltonian-vacuum-limit#A blocked transfer can certify the entire generator|the transfer-to-generator lemma]].
It controls all representations, including the exact zero modes:
\[
\varepsilon_N^{-1}(I-K_N)
\longrightarrow A_0:=-\frac{3r}{2}\sum_{e\in E}\Delta_{Q_R,e}
\quad\text{in norm resolvent}.
\tag{TS3}
\]
Apply the bounded-multiplier argument (WH6) in the same note, with
\(V=\gamma W\). The blocked-transfer lemma also gives \(K_N\to I\)
strongly; \(A_0\) has compact resolvent and \(W\) is bounded at the
fixed graph. These supply the hypotheses of that argument. The exact result is
\[
\boxed{\|T_N^{n_N}-e^{-tH_\gamma}\|\longrightarrow0,
\qquad H_\gamma=A_0+\gamma W,
\qquad n_N\varepsilon_N\to t>0.}
\tag{TS4}
\]
The operator domain is \(D(A_0)=H^2(G^E)\); its form domain is
\(H^1(G^E)\), with their invariant parts after Gauss restriction.
Equation (TS4) concerns the exact sewn powers, not a replacement of
finite-step \(-\log T_N\) by \(I-T_N\).

The kernel of \(T_N\) is strictly positive pointwise, so it has a unique
normalized positive Perron vector \(\Omega_N\), which is gauge invariant.
Let \(\lambda_N=\|T_N\|\) and \(\widehat T_N=T_N/\lambda_N\).
The limiting compact-rotor Hamiltonian has a unique positive ground
state \(\Omega\) and ground energy \(E_0\). Norm convergence at positive
duration gives
\[
\Omega_N\to\Omega\text{ in }L^2,
\qquad
\widehat T_N^{n_N}\to e^{-t(H_\gamma-E_0)}\text{ in norm}.
\tag{TS5}
\]
The proof is the isolated Perron projection argument (WH8); the raw and
physical top eigenvalues agree. Each finite \(T_N\) remains finite rank,
which forbids a microscopic Hamiltonian logarithm on either carrier
whenever that carrier is infinite dimensional. A fully gauged tree's
one-dimensional physical carrier is not such a case.
The positive-time limit is injective on the complete declared carrier.

This supplies, rather than postulates, the all-duration pairings for
this member. For a specified isometry
\(J:\mathcal R\to\mathcal H_{\rm GI}\), a fixed duration \(\tau>0\), and
\(k_N\varepsilon_N\to\tau\), define
\[
R_{N,j}=J^*(\widehat T_N^{k_N})^jJ,
\qquad
R_{N,j}\longrightarrow J^*e^{-j\tau(H_\gamma-E_0)}J,
\quad j=0,1,\ldots .
\tag{TS6}
\]
All reflected-moment inequalities (HM2) in
[[global-local-response-reconstruction/compatible-spectral-readouts-and-positive-clock|positive-clock reconstruction]]
hold by temporal sewing and Hilbert positivity. The limiting zero-atom
test passes because the full heat transfer is injective. A proper
readout need not cover the whole physical carrier; it does not justify
discarding other sectors or replacing the sequence by powers of its
first compressed moment.

This is compact-rotor quantum mechanics on a supplied spatial graph,
not a four-dimensional continuum return. The graph, \(\gamma\), temporal
parameter and the anisotropic scaling in (TS2) remain independent inputs.
The overlap law fixes the kinetic coefficient once those choices are
made; it does not force their magnetic/electric ratio.

### The same-weight shortcut instead loses the entire clock

Keep that spatial graph fixed, use the same sharpening power on every
face, and try to assign \(\varepsilon_N=N^{-2}\) to a temporal layer.
After stripping irrelevant scalar face normalizations, the slab is now
\[
T_N^{\rm same}=M_NK_NM_N,\qquad
M_N=e^{-W/(2\varepsilon_N)}.
\tag{TS7}
\]
Assume \(\{W=0\}\) has product-Haar measure zero. This holds when there
is an ordinary spatial plaquette with an edge occurring once: its
holonomy is Haar distributed, and \(S(g)=0\) only at \(g=e\).
Trees with no spatial plaquettes are excluded.
Dominated convergence gives \(M_N\to0\) strongly and hence
\(\|T_N^{\rm same}f\|\le\|M_Nf\|\to0\).

Vacuum normalization does not repair this limit. To see that explicitly,
put \(d=\dim G\), \(D=d|E|\), and take a product neighborhood
\(A_N\) of the trivial links of radius \(a/N\), for fixed small \(a>0\).
Equations (OF5)–(OF7) imply fixed-graph constants with
\[
|A_N|\ge c_1N^{-D},\quad
M_N(U)\ge c_2\ (U\in A_N),\quad
\prod_ep_N(U_eV_e^{-1})\ge c_3N^D\ (U,V\in A_N).
\tag{TS8}
\]
The normalized indicator of \(A_N\) thus has Rayleigh quotient at least
\(c_1c_2^2c_3>0\). Although this trial vector is not gauge invariant,
the strictly positive kernel has its unique Perron vector in the
invariant space, so the raw and physical norms coincide. Consequently
\(\lambda_N^{\rm same}=\|T_N^{\rm same}\|\ge c_\Gamma>0\).
For \(Q_N=T_N^{\rm same}/\lambda_N^{\rm same}\),
\[
\boxed{Q_N\to0\text{ strongly},\qquad
Q_N^{n_N}\to0\text{ strongly for every sequence }n_N\ge1.}
\tag{TS9}
\]
The power assertion uses \(0\le Q_N\le I\), so
\(\|Q_N^{n_N}f\|\le\|Q_Nf\|\). Its normalized vacuum vectors escape
weakly: \(\langle f,\Omega_N^{\rm same}\rangle
=\langle Q_Nf,\Omega_N^{\rm same}\rangle\to0\).
Moment limits on a fixed isometric readout are \(R_0=I\) and
\(R_j=0\) for every \(j\ge1\): the zero-transfer atom of (HM6),
not a finite-energy clock or a mass-gap theorem.

This obstruction concerns **the fixed graph and fixed Haar carrier**.
It says nothing against simultaneous spatial mesh refinement or a
separately constructed changing-carrier limit. Nor is (TS7) the carpet
pushforward (OF12). It rules out identifying three different operations:
face sharpening, face subdivision, and refinement of observable duration.
For this fixed-graph finite-potential limit, the spatial exponent must
scale as \(\varepsilon_N\gamma\), not \(\varepsilon_N^{-1}\).
Any stronger whole-to-local construction must determine an appropriate
joint scaling and its carrier rather than infer a clock from positivity.

[[holonomy-refinement-and-clock-compatibility|Holonomy refinement]]
tests the next spatial step. Product-holonomy pullback adds the fine
kinetic coefficients even after faithful vacuum reweighting. The
fixed-graph clock above is therefore not already a compatible clock
on a spatial refinement tower; the observable embedding and induced
response tensor require their own construction.

## The exact response of a coincident boundary star

The many-way amplitude has a computable response before any clock is
assigned. Let \(w>0\) be a smooth central function on a compact connected
group with a fixed bi-invariant metric \(Q\), and \(m\ge2\). Define
\[
A(g_1,\ldots,g_m)=\int_G\prod_{i=1}^m w(g_i u^{-1})\,du,
\qquad F=-\log A.
\tag{SF1}
\]
The independent boundary carrier is \(G^m\). At the coincident tuple
\((e,\ldots,e)\), set \(\ell=\log w\),
\[
d\nu(z)=\frac{w(z)^m\,dz}{\int_Gw^m},\qquad
X_v\ell(z)=\left.\frac{d}{ds}\ell(e^{sv}z)\right|_{s=0},\qquad
C(v,a)=\mathbb E_\nu[X_v\ell\,X_a\ell].
\tag{SF2}
\]
These are scores in the actual conditional Haar law, not a saddle-point
replacement of that law. Haar integration by parts gives
\[
\mathbb E_\nu X_v\ell=0,\qquad
\mathbb E_\nu X_v^2\ell=-mC(v,v).
\tag{SF3}
\]
Differentiate \(F(e^{sv_1},\ldots,e^{sv_m})\), substituting \(z=u^{-1}\).
The logarithmic second derivative is minus the mean second derivative
minus the variance of the total score. Hence
\[
\boxed{
\operatorname{Hess}F(v,v)
=m\sum_iC(v_i,v_i)
-C\!\left(\sum_iv_i,\sum_iv_i\right)
=\sum_{i<j}C(v_i-v_j,v_i-v_j).}
\tag{SF4}
\]
The first derivative is zero, so this is the covariant Hessian.
Polarization gives \((mI-\mathbf1\mathbf1^\top)\otimes C\).
The complete-graph difference form was forced by gluing and common-motion
invariance, not inserted as an independent response matrix.

For simple Lie algebra and nonconstant central \(w\), adjoint invariance
gives
\[
C=cQ,\qquad
c=\frac1{\dim G}\mathbb E_\nu|\nabla\log w|_Q^2>0.
\tag{SF5}
\]
A nonzero invariant semidefinite form on a compact simple Lie algebra is
positive definite; otherwise its kernel is a nontrivial ideal.
The only null directions on \(G^m\) at coincidence are common motion.
On \(\sum_iv_i=0\), with the inherited product metric, the response
eigenvalue is \(mc\).

This conclusion is not yet a statement about all retained lattice links.
For a staple map \(g=g(R)\) through coincidence,
\[
\operatorname{Hess}(F\circ g)=(Dg)^*(\operatorname{Hess}F)Dg.
\tag{SF6}
\]
It may have additional null directions because \(Dg\) is not injective
modulo common motion. Nor does positivity at coincidence imply global
convexity; the cancelled Wilson staples in
[[rg-covariance-residue/su2-staple-elimination-and-response|exact staple elimination]]
already give a negative induced response.

For the specified anchor \(w=\kappa^k\), the conditional law is
\(\nu\propto\kappa^{km}\). The same local expansion as (OF5)–(OF7), now
also applied to its differentiated score, gives at fixed \(m\)
\[
C=\frac{k}{3rm}Q_R+O(1),\qquad
mC=\frac{k}{3r}Q_R+O(1)\quad(k\to\infty).
\tag{SF7}
\]
The \(O(1)\) is a bilinear-form bound in the fixed metric and representation.
The increased concentration of the shared link contributes \(1/m\);
the complete-graph factor contributes \(m\). Thus the leading quotient
stiffness does not acquire an extra factor merely because a four-dimensional
edge has six incident faces. This is a fixed-star response statement,
not a continuum physical rate.

There is an exact unequal-power extension. For
\(w_i=\kappa^{k_i}\), \(k_i>0\), put \(K=\sum_i k_i\) and
\(C_0=\mathbb E_{\kappa^K}[d\log\kappa\otimes d\log\kappa]\), using invariant
derivatives as in (SF2). Integration by parts then gives
\[
\operatorname{Hess}F
=\bigl[K\,\operatorname{diag}(k_i)-kk^\top\bigr]\otimes C_0,
\qquad k=(k_1,\ldots,k_m)^\top.
\tag{SF8}
\]
General blocked weights need not retain this common-profile form.

For fundamental \(SU(2)\), write \(u=zI+i\mathbf u\cdot\sigma\);
\(\kappa=(2+z)/3\) and \(Q_R=2g_{\rm round}\). Haar moments give
\[
J_n=\mathbb E_{\rm Haar}(2+z)^n
=\sum_{j=0}^{\lfloor n/2\rfloor}
\binom n{2j}2^{n-2j}\frac{\operatorname{Cat}_j}{4^j},
\quad \operatorname{Cat}_j=\frac1{j+1}\binom{2j}{j}.
\]
For integers \(k\ge1,m\ge2\), \(K=km\),
\[
c=\frac{k^2}{6}
\frac{-J_K+4J_{K-1}-3J_{K-2}}{J_K}.
\tag{SF9}
\]
This follows from
\(|\nabla\log w|_{Q_R}^2=(k^2/2)(1-z^2)/(2+z)^2\).
At \(k=1,m=6\), \(c=107/5614\) and the quotient eigenvalue is
\(mc=321/2807\). These are exact dimensionless derivatives of a stated
boundary integral, not predicted glueball energies.

The shared receipt independently differentiates the full product before
Haar integration, using polynomial moments rather than (SF4) to generate
the Hessian. It checks the diagonal, mixed and common-motion directions.
A static Hessian still does not determine all-duration propagation:
[[global-local-response-reconstruction/compatible-spectral-readouts-and-positive-clock#Reflected boundary moments can precede the spectrum|reflected boundary moments]]
identify the additional operator family needed for a clock.


## Exact finite calibration

The existing [[receipts/boundary_charge_gluing_receipt.py|boundary-gluing receipt]]
retains its two-link \(\mathbb Z_2\) control and adds the standard faithful
representation of \(S_3\). Its anchored overlap has values \(1,2/3,1/2\)
on the identity, transpositions and three-cycles. The receipt checks
324 exact two-face integrals, nine normalized joint laws, and full tensor
Haar projectors with
\[
\dim\operatorname{Inv}(V^{\otimes2})=1,\qquad
\dim\operatorname{Inv}(V^{\otimes4})=3,\qquad
\dim\operatorname{Inv}(V^{\otimes6})=11.
\tag{OF19}
\]
These follow from \((2^n+2)/6\) for the displayed even \(n\), using character
values \(2,0,-1\) and class sizes \(1,3,2\).

For \(p_k=\kappa^k/\int\kappa^k\), the normalized law
\(p_k(Au^{-1})p_k(uB)\,dA\,du\,dB\) has correlated framed boundary variables
but independent face-increment coordinates. At \(k=1\),
\(\operatorname{Cov}(\mathbf1_{A=e},\mathbf1_{B=e})=1/576\).
Also \((p_1*p_1)(e)=17/16\ne p_2(e)=36/17\):
pointwise sharpness powers are not convolution time.
[[receipts/boundary-charge-gluing-receipt-output.txt|The saved output]]
is finite evidence for gluing and channel multiplicities, not for the
compact connected group limit or a mass gap.

For the actual fundamental \(SU(2)\) overlap, the same receipt also
computes every nonzero harmonic block and handles the infinite
complement analytically. Write
\((4+\chi_1)^k=\sum_\ell a_{k,\ell}\chi_\ell\), with
\(\chi_1=2z\). Character multiplication gives the integer recurrence
\[
a_{k+1,\ell}=4a_{k,\ell}+a_{k,\ell-1}+a_{k,\ell+1},\qquad
a_{0,0}=1,\qquad a_{k,-1}=0,
\tag{TS10}
\]
with zero coefficients beyond the support. At \(k=N^2\), the
convolution eigenvalue is \(b_{N,\ell}=a_{k,\ell}/[(\ell+1)a_{k,0}]\),
and the target generator eigenvalue is \(3\ell(\ell+2)/2\).
The division by representation dimension is essential.

The measured full-carrier error
\(\|B_N^{N^2}-e^{(3r/2)\Delta_{Q_R}}\|\) decreases from
\(0.113891\) at \(N=1\) to \(0.0000488427\) at \(N=32\).
For \(\ell>N^2\), the approximate resolvent is the constant
\(1/(1+N^2)\), while the limiting resolvent tends to zero as
\(\ell\to\infty\). This infinite-tail supremum is included, not hidden
by the finite character cutoff. The six numerical refinements check
the one-link spectral formulas; (OF9), (BR1)–(BR3) and the bounded
perturbation proof, not these numbers, establish the clock limit.
