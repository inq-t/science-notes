# Holonomy Refinement and Clock Compatibility

Multiplying fine links into one coarse holonomy preserves a carrier, but it preserves an independent-link clock only when the fine diffusion coefficients add to the coarse coefficient. This exact condition survives faithful vacuum reweighting. The additive Haar construction does produce a compatible refinement clock; its full physical threshold is the infimum of weighted cycle lengths times the least Casimir, and vanishes when refinement introduces arbitrarily cheap loops. Mixed responses can change this geometry, yet a known metric-independent mixed construction leaves smooth closed-loop distinctions in its kernel. A continuum candidate must specify a compatible state, observable embedding and response geometry together, distinguishing instantaneous form compatibility from complete clock compatibility.

**Status: [ESTABLISHED] for additive weighted-Laplacian consistency; [EXACT] for the weighted pullback, adjacent-plaquette compression defect, closed-loop kernel test, and spectral threshold of a countable compatible Haar refinement clock; [OPEN] for a compatible interacting four-dimensional vacuum and a uniform physical threshold.**

## A product holonomy has an additive diffusion budget

Fix a nontrivial compact connected Lie group \(G\), a bi-invariant metric
\(Q\), and \(D=-\Delta_Q\ge0\). Subdivide a framed edge into \(b\ge2\)
segments and define
\[
\pi(U_1,\ldots,U_b)=U_1\cdots U_b,\qquad Jf=f\circ\pi.
\tag{HC1}
\]
Product Haar pushes forward to Haar, so
\(J:L^2(G)\to L^2(G^b)\) is isometric. Internal vertex gauge actions
cancel in the product; endpoint actions remain. This is a
boundary-framed map, not an early projection of each segment to its
trivial representation.

For positive coefficients \(\alpha_i\), put
\(D_f=\sum_i\alpha_iD_i\). Bi-invariance gives on smooth functions
\[
D_iJf=JDf,\qquad
D_fJf=J\left[\left(\sum_i\alpha_i\right)Df\right].
\tag{HC2}
\]
Varying one segment changes the product by a left or right translation
conjugated by the remaining segment product. Conjugation preserves
\(Q\), hence the orthonormal Casimir sum. The identity extends to
the usual \(H^2\) operator domains on these compact carriers;
equivalently convolution of central heat kernels gives
\[
e^{-tD_f}J=Je^{-t(\sum_i\alpha_i)D},\qquad t\ge0.
\tag{HC3}
\]
The pulled-back carrier reduces this fine heat evolution. Exact
same-clock consistency with \(D_c=\alpha_cD\) therefore requires
\[
\boxed{\alpha_c=\sum_i\alpha_i.}
\tag{HC4}
\]
A nonconstant matrix coefficient detects necessity. This is the
weighted-Laplacian construction of
[[library/differential-geometry-on-the-space-of-connections-via-graphs-and-projective-limits/inq|Ashtekar and Lewandowski]],
Section 6.1, Theorem 5 and its subdivision proof; Section 6.2 supplies
the compatible heat evolution. It is not a new mass-gap result.
Orientation reversal additionally requires the same weight on an edge
and its inverse.

For homogeneous lengths, (HC4) reads
\(\alpha(a)=b\alpha(a/b)\). Along this subdivision tower,
\(\alpha(a)/a\) is constant. A different clock comparison replaces
(HC4) by equality of the duration-weighted coefficients. One must
declare that comparison rather than silently rescale each clock.

## Gauss projection and a new density do not erase the factor

On a simple cycle \(C\), with distinct edge coordinates, let
\(f_C=\chi_\lambda(\operatorname{Hol}_C)\) for a nontrivial irreducible
representation. This is gauge invariant, has Haar mean zero and norm
one, and
\[
\left(\sum_e\alpha_eD_e\right)f_C
=C_2(\lambda)\left(\sum_{e\in C}\alpha_e\right)f_C.
\tag{HC5}
\]
A physical closed loop therefore detects the coefficient mismatch.
On the neutral carrier this witness identifies loop sums; individual
edge coefficients need not be separately identifiable. A fully gauged tree has no such
nonconstant witness.

More generally, let \(\pi:X_f\to X_c\) multiply disjoint subdivision
paths and forget any unused fine edges. Give the finite configuration
spaces smooth positive densities with \(\nu_c=\pi_*\nu_f\).
Then \(Jf=f\circ\pi\) is isometric on the weighted \(L^2\) spaces.
Write \(P_c\) for the specified fine segment path over coarse edge
\(c\). The pointwise gradient identity and disintegration give
\[
\boxed{
\sum_{e\in E_f}\alpha_e\int|\nabla_e(f\circ\pi)|_Q^2\,d\nu_f
=\sum_{c\in E_c}\left(\sum_{e\in P_c}\alpha_e\right)
\int|\nabla_cf|_Q^2\,d\nu_c.}
\tag{HC6}
\]
Unused edges contribute zero derivatives. Correlations in \(\nu_f\),
including those with discarded transverse links, do not alter this
equality. It is an application of the
[[trace-dirichlet-descent/inq#The variance-correct safe branch pulls observables back|observable-pullback form]],
not infimal elimination over a fibre.

For ground-state forms of finite Schrödinger operators
\(H_i=\alpha_i\sum D_e+V_i\), write \(\rho_i=\psi_i^2\), with smooth
positive normalized vacuum \(\psi_i\). The centered form obeys
\(\langle\psi_iF,(H_i-E_i)\psi_iF\rangle
=\alpha_i\int|\nabla F|^2\rho_i\).
If these vacuum laws have the stated exact marginal relation, their
Haar-carrier isometry is
\[
J_\psi f=\frac{\psi_f}{\psi_c\circ\pi}(f\circ\pi).
\tag{HC7}
\]
It sends \(\psi_c\) to \(\psi_f\), but (HC6) still holds in their
ground-state representations. Reweighting the vacuum alone cannot
cancel an independent-link principal-response mismatch. The marginal
relation itself is an additional requirement, not automatic for two
independently chosen lattice vacua.

[[prepared-vacuum-subdivision-and-the-recovered-clock|The prepared-vacuum Fisher test]]
establishes that relation exactly for pure subdivision: the pulled-back
positive eigenvector is the actual fine vacuum, and internal Gauss
invariance identifies the complete physical carriers. Nevertheless,
rebuilding the Fisher-dual source response changes the clock.
Its correction vanishes under increasingly fine redundant subdivision,
recovering the already supplied physical form. This is a failure of
the source-comparison prescription, not of the holonomy carrier map.

## The tensor condition is stronger than a scalar normalization

Allow a smooth positive diffusion cometric \(C_f\), represented using
the fixed product metrics as a positive endomorphism on tangent
vectors. It measures responses of gradients, and may have mixed blocks
between different links. For
\(\mathcal E_f(F)=\int\langle\nabla F,C_f\nabla F\rangle d\nu_f\),
the exact pulled-back form has cometric
\[
\boxed{\overline C_c(x)=
\mathbb E_{\nu_f}\!\left[D\pi\,C_f\,(D\pi)^*
\mid\pi=x\right].}
\tag{HC8}
\]
The adjoint uses the declared metrics; equivalently this transports a
bilinear form on covectors. Chain rule followed by conditional
integration proves (HC8). Equality with a supplied coarse cometric is
precisely the form-compatibility condition on the full framed smooth
observable algebra. For independent
scalar blocks it reduces to (HC6).

It is not sufficient for autonomous coarse dynamics. In local coarse
coordinates \(x^a\), write the fine Markov generator as
\(\mathcal A_f=\rho_f^{-1}\operatorname{div}(\rho_f C_f\nabla)\).
The chain rule for \(\mathcal A_f(f\circ\pi)\) involves both the
pointwise transported cometric and the drift \(\mathcal A_f\pi^a\).
Full generator intertwining requires both to be functions of \(\pi\)
with the coarse coefficients; their conditional averages alone do not
suffice. Under compact smooth uniformly elliptic hypotheses and these
pointwise identities, the smooth core gives semigroup intertwining.

Let \(L_f=-\mathcal A_f\ge0\) be the self-adjoint form generator.
Without that stronger condition the actual readout remains
\(R_t=J^*e^{-tL_f}J\), not the exponential of its first form moment.
The exact positive defect
\[
R_{2t}-R_t^2
=J^*e^{-tL_f}(I-JJ^*)e^{-tL_f}J\ge0
\tag{HC9}
\]
is owned by
[[coarse-response-memory/spectral-readout-and-the-visible-gap|spectral readout and memory]].
An autonomous compressed semigroup forces this defect to vanish and
the readout range to reduce the clock. The broader
[[global-local-response-reconstruction/compatible-spectral-readouts-and-positive-clock|moment reconstruction]]
does not demand that closure at every coarse context.

## Individually autonomous loop readouts can have a nonautonomous join

Take two adjacent square plaquettes with seven distinct links, product
Haar law, full vertex gauging, and no magnetic potential. Set
\(G=SU(2)\), \(Q=-2\operatorname{Tr}\), and
\[
H_0=\kappa\sum_{e=1}^7D_{Q,e},\qquad \kappa>0.
\tag{HC9a}
\]
The fundamental Casimir is \(3/4\). The common path has one edge and
the two outside paths have three each. By (HC2), their exact reduced
weights are \(\kappa,3\kappa,3\kappa\). The
[[gauge-cycle-innovation-filtration/loop-coordinates-and-the-induced-clock|theta-loop construction]]
therefore gives the full physical carrier
\(\mathcal H=L^2(G^2)^{\operatorname{Ad}G}\) and the operator
\[
H_0=4\kappa(D_x+D_y)-2\kappa\sum_aR_{x,a}R_{y,a}.
\tag{HC9b}
\]
Its domains are the inherited invariant \(H^2\) operator domain and
\(H^1\) form domain, not independently chosen domains on trace coordinates.

Let \(\chi=\operatorname{Tr}_{\mathbf2}\), and let \(\mathcal B\) be
the entire closed subspace of functions of \((\chi(x),\chi(y))\).
Write \(J:\mathcal B\hookrightarrow\mathcal H\) for inclusion,
\(P=JJ^*\) for Haar conditional expectation, and
\(C_t=J^*e^{-tH_0}J\). Each separate one-loop class space reduces
\(H_0\), with clock \(4\kappa D_Q\). Their joint character space
\(\mathcal B\), however, is smaller than the simultaneous-invariant
space \(\mathcal H\).

An exact witness identifies the missing distinction. Write
\(x=x_0I-i\mathbf x\cdot\boldsymbol\sigma\) and similarly for \(y\).
Put
\[
F=\chi(x)\chi(y),\qquad
Z=\mathbf x\cdot\mathbf y,\qquad
B=\tfrac12\chi(yx^{-1})=\tfrac14F+Z.
\tag{HC9c}
\]
The outside six-edge loop gives \(H_0B=(9\kappa/2)B\).
The product rule on the shared edge gives
\[
H_0F=6\kappa F-2\kappa Z
     =\tfrac{13\kappa}{2}F-2\kappa B,
\qquad
H_0(F-B)=\tfrac{13\kappa}{2}(F-B).
\tag{HC9d}
\]
Normalized Haar integration gives
\(\|F\|^2=1\), \(\|B\|^2=\langle F,B\rangle=1/4\);
thus \(F=B+(F-B)\) is an orthogonal spectral decomposition with
squared weights \(1/4\) and \(3/4\).

Conditional on \(x_0,y_0\), the two quaternion-vector orientations are
independent and uniform. Hence \(PZ=0\) and \(PB=F/4\). This is
conditioning on the complete joint character algebra, not projection
onto one trial vector. It proves
\[
\boxed{
C_tF=\left(\tfrac14e^{-9\kappa t/2}
           +\tfrac34e^{-13\kappa t/2}\right)F.}
\tag{HC9e}
\]
In particular,
\[
\boxed{
\langle F,(C_{2t}-C_t^2)F\rangle
=\tfrac3{16}
\left(e^{-9\kappa t/2}-e^{-13\kappa t/2}\right)^2
=\tfrac{3\kappa^2}{4}t^2+O(t^3).}
\tag{HC9f}
\]
The positive defect at every \(t>0\) rules out autonomous compressed
evolution on \(\mathcal B\). Averaging the mixed response away and
rebuilding a product class clock instead gives
\(e^{-6\kappa t}F\): the first derivative agrees, but the complete
return does not.

There is an exact finite repair. Adjoin the relative-loop observable
\(\chi(yx^{-1})\). The three real traces determine \(x_0,y_0\) and the
Gram matrix of the two quaternion vectors. Two vector pairs with the
same Gram matrix differ by an \(SO(3)\) rotation, including the
degenerate cases, and such rotations are the \(SU(2)\) adjoint action.
Thus the three traces separate simultaneous-conjugation orbits.
Their measurable algebra generates the entire physical \(L^2\)
carrier, and its inherited electric clock is autonomous. For this
isolated graph the repair restores all physical variables; it is
not yet an economical reduction for an arbitrarily large lattice.

The same two-channel return can be checked before the temporal
continuum limit. For normalized independent Wilson link convolution
with density proportional to \(e^{\beta\chi/2}\), \(\beta>0\), define
\(p_j=I_{j+1}(\beta)/I_1(\beta)\), where \(j\) is twice the spin.
The six outside links are fundamental. The common link is trivial
on \(B\) and spin one on \(F-B\). For integer \(n\ge0\),
\[
J^*T_\beta^nJF
=\left[\tfrac14p_1^{6n}
       +\tfrac34(p_1^6p_2)^n\right]F.
\tag{HC9g}
\]
This is the zero-magnetic transfer, not an interacting Wilson vacuum
or an identification of \(-\log T_\beta\) with a Laplacian at fixed
spacing. The
[[gauge-boundary-frame-gluing/receipts/overlapping_plaquette_transfer_receipt.py|overlapping-plaquette receipt]]
checks the actual seven-link Pauli derivatives, Haar channel weights,
and Wilson convolution at four values of \(\beta\).

This supplies a concrete correction to a proposed whole-to-local
axiom: closure of each individual observable context does not force
closure of their join. One must retain relational channels or retain
their nonautonomous spectral return. Neither operation proves a
continuum mass gap; the next issue is control of the additional
channels when more plaquettes and magnetic interactions are included.
In this free example the full electric gap and the rebuilt
joint-character gap both equal \(3\kappa\), witnessed by a single
plaquette character. The disagreement concerns the full dynamical
return, not those two numerical gap values.

[[coarse-response-memory/interacting-gauge-vacuum-and-local-memory|The
interacting vacuum calculation]] identifies the exact single-plaquette
hidden score and bounds its short-time coefficient uniformly in box
size. [[algebra/oriented-gram-descent-and-invariant-coverage|The
three-loop orientation test]] exposes a different obstruction: even
perfectly autonomous pairwise clocks can omit a physical invariant
sector. Temporal compatibility and observable completeness must both
survive the next gluing operation.

## A natural mixed response can still miss closed distinctions

The independent-edge ansatz is not the only consistent geometry.
Ashtekar–Lewandowski Section 7 constructs a different, potentially
degenerate cometric using mixed derivatives between edges that form
an analytic continuation at a vertex. Its consistency is not based
on additive length weights. This is a precedent for changing the
response geometry, not an argument that all compatible clocks must
obey (HC4).

It admits a direct kernel test. At a bivalent analytic-continuation
vertex, orient the two edge germs outward and write their invariant
derivatives in a \(Q\)-orthonormal Lie-algebra basis as
\(X_{e,a},X_{e',a}\). The positive vertex response is
\[
\mathcal E_v(F)=\frac12\sum_a
\left|(X_{e,a}+X_{e',a})F\right|^2.
\tag{HC10}
\]
This is the sum-of-squares form of their Section 7.3 operator,
including the two ordered mixed terms. A gauge-invariant function
is annihilated by the sum, which generates the vertex gauge action.

Take an embedded closed analytic circle, cut into at least three arcs,
and the nonconstant \(f_C\) in (HC5). Every vertex is bivalent with
analytic continuation, so every term (HC10) vanishes. Therefore
\[
\boxed{D^{\rm natural}f_C=0,\qquad
\langle1,f_C\rangle_{\rm Haar}=0,\qquad
\|f_C\|_{\rm Haar}=1.}
\tag{HC11}
\]
Here \(D^{\rm natural}=-\Delta^o\) on smooth cylindrical functions.
The displayed vectors are already in that domain, so the positive
Friedrichs realization retains them. Distinct irreducible characters
give infinitely many orthogonal zero modes. Cylindrical consistency
preserves these vectors under further graph refinement.
The finite-circle response is pointwise zero, so a faithful density
reweighting cannot make it positive while retaining that cometric.

This particular operator cannot supply a unique constant Haar vacuum
with a positive floor on its orthogonal complement. The test does
not exclude a gap above its entire enlarged kernel, and says nothing
against other cometrics or added interactions. It identifies what
this local analytic-continuation cancellation fails to detect: closed
holonomy. A mass-gap candidate must control such physical distinctions,
not only ignore redundant subdivision vertices.

## What this constrains in the Yang–Mills return

The fixed-graph clock in
[[overlap-kernels-and-face-refinement#Temporal sewing needs a separate refinement law|overlap temporal sewing]]
does not automatically extend through spatial refinement. In the
\(3+1\) electric scaling recorded in
[[contemporary-puzzles/yang-mills-mass-gap/finite-spacing-transfer-and-bounded-flux-solder|finite-spacing transfer]],
write \(\alpha(a)=\zeta_Q g(a)^2/a\). The fixed \(\zeta_Q>0\)
includes the Casimir metric and unit convention; in the cited standard
lattice normalization it is \(\hbar c/2\). A different normalization
of \(Q\) changes that factor as well as \(C_2\).
With the same convention and physical clock at both resolutions,
the uniform subdivision mismatch is
\[
\frac{b\alpha(a/b)}{\alpha(a)}
=b^2\frac{g(a/b)^2}{g(a)^2}.
\tag{HC12}
\]
For any trajectory with the fixed-ratio running property
\(g(a/b)^2/g(a)^2\to1\), this tends to \(b^2\), not one.
This is a conditional algebraic test, not a proof of that trajectory
or a four-dimensional nonexistence result.

At fixed geometric loop length \(\ell\), the pure-electric Haar
character energy scales as
\(C_2(\lambda)\zeta_Q\ell g(a)^2/a^2\). If this diverges,
the readout on that fixed thin-loop carrier tends to projection onto
constants at every positive duration. Neither this divergence nor
(HC11) is a glueball mass. They diagnose opposite failures of proposed
observable/response identifications.

The next construction must specify which whole-to-local observable
map, response tensor and spectral readout survive together. Mixed
effective responses, genuinely different or smeared observables, and
nonautonomous coarse clocks are possible changes of the hypotheses.
They must be constructed from the actual interacting law. Merely
replacing Haar by an unspecified vacuum, or declaring the group
Laplacian to be the physical Hamiltonian, does not discharge that work.

## A compatible refinement clock can be gapless

The additive branch supplies an actual limit operator, not only a
compatibility condition. Take a countable nested family of finite
connected graphs \(\Gamma_n\), with compatible inclusions of coarse
vertices. Every coarse edge is represented by a fine path with the
same endpoints and no repeated edge, with distinct coarse paths using disjoint fine edges;
other fine edges are forgotten. Keep the same \(G,Q\), product Haar
law and full vertex gauging. Require positive weights and
\(\alpha_{n,e}=\sum_{s\in P_e}\alpha_{n+1,s}\), in one common clock.
Then the finite physical carriers and operators
\[
\mathcal H_n=L^2(G^{E_n})^{G^{V_n}},\qquad
H_n=\left.\sum_{e\in E_n}\alpha_{n,e}D_e\right|_{\mathcal H_n}
\tag{HC13}
\]
have isometric holonomy pullbacks \(J_n\) with
\(e^{-tH_{n+1}}J_n=J_ne^{-tH_n}\), by (HC3) and independence of
unused edges. Pure bivalent subdivision adds no physical variables:
internal Gauss invariance makes every invariant depend only on the
path product. New cycles, in contrast, can enlarge the carrier.

Complete the algebraic Hilbert-space union to \(\mathcal H_\infty\).
The compatible finite heat operators define a symmetric contraction
semigroup on the union. Their norm bound extends it to the completion;
strong continuity follows by approximating a vector by one finite-stage
vector. Thus there is a positive self-adjoint generator
\[
T(t)=e^{-tH_\infty},\qquad
T(t)|_{\mathcal H_n}=e^{-tH_n}.
\tag{HC14}
\]
This directly constructs the clock on this countable refinement carrier.
It does not reconstruct a local four-dimensional quantum field theory.

Each stage is a reducing subspace of \(T(t)\). Its orthogonal projection
\(P_n\) therefore commutes with \(T(t)\), and \(P_n\to I\) strongly.
If \(f\in\ker H_\infty\), then every \(P_nf\) is fixed by its finite
clock and hence constant. The constants agree under the embeddings,
so \(f\) is constant. The limit has a unique vacuum even when its
spectral gap is zero.

Assume some stage contains a cycle. The
[[contemporary-puzzles/yang-mills-mass-gap/gauge-descent-flux-fisher-coercivity#Gauge invariance sharpens the constant to girth times Casimir|weighted girth theorem]]
gives the exact full-carrier result
\[
\boxed{
\inf\operatorname{spec}
\left(H_\infty|_{\mathbf1^\perp}\right)
=\lambda_G\inf_n g_{\alpha_n}(\Gamma_n),\qquad
\lambda_G=\min_{\lambda\ne1}C_2(\lambda).}
\tag{HC15}
\]
Stages without cycles have only constants and may be omitted from the
infimum. For the lower bound, each centered finite-stage heat operator
has norm at most the exponential of the negative proposed bound;
extend this estimate from their dense union. For the upper bound, the
minimum-Casimir character on a minimizing cycle is an exact normalized
eigenvector at its stage and remains the same eigenvector under every
later heat evolution. This also proves that small cycle weights yield
genuine near-zero physical states, not merely a weak estimate.

For example, take ordinary open hypercubic refinements in dimension
\(d\ge2\), spacing \(a_n=a_0b^{-n}\), integer \(b\ge2\), and coefficients
\(\alpha_{n,e}=\kappa a_n\), with fixed \(\kappa>0\).
Coarse edges split into \(b\) segments, and new elementary squares have
\[
g_{\alpha_n}(\Gamma_n)=4\kappa a_n,
\qquad
\inf\operatorname{spec}
\left(H_\infty|_{\mathbf1^\perp}\right)=0.
\tag{HC16}
\]
A fixed macroscopic box already suffices. Every old loop retains its
response, but new loops have decreasing response. This is different
from losing the gap merely by making the box larger. It also differs
from the nonconstant exact zero modes of (HC11): here only the vacuum
has zero energy, and positive eigenvalues accumulate toward it.

There is a quantitative state constraint. At each finite stage containing
a cycle, replace
Haar by a smooth invariant probability density \(w_n\), retaining the
same principal response, and let \(H_n^{w}\) be the positive generator
of \(\sum_e\alpha_{n,e}\int|\nabla_ef|^2w_n\,d\mu_H\).
If constants \(0<m\le M<\infty\), independent of \(n\), satisfy
\(m\le w_n\le M\), the minimizing Haar character gives
\[
\operatorname{gap}_{\mathbf1}H_n^w
\le \frac{M}{m}\lambda_G g_{\alpha_n}(\Gamma_n).
\tag{HC17}
\]
Indeed its weighted energy is at most \(M\) times its Haar energy,
whereas \(\operatorname{Var}_{w_n}(f)=\inf_z\int|f-z|^2w_n\,d\mu_H
\ge m\operatorname{Var}_{\mu_H}(f)\). This is the upper-bound use of
the existing bounded-density comparison, not an assumption that actual
Yang--Mills vacua satisfy it. The weighted clocks need not themselves
intertwine; (HC17) is a finite-stage obstruction to a uniform floor.

If these weighted states are also projectively consistent, the same
bound holds for a constructed whole clock. On the countable raw
projective-limit Haar space, \(w_n\) is a bounded positive martingale
and converges to a density \(w_\infty\), still between \(m\) and \(M\),
whose marginals are the supplied states. Equation (HC6) makes the
weighted cylinder forms consistent. On their common cylinder core,
\(m\mathcal E_H\le\mathcal E_w\le M\mathcal E_H\), and the two
\(L^2\) norms are equivalent. Closability of the Haar form therefore
proves closability of the weighted form: an \(\mathcal E_w\)-Cauchy
sequence tending to zero in \(L^2(w_\infty\mu_H)\) is Haar-form
Cauchy and tends to zero in Haar \(L^2\), so its weighted energy tends
to zero as well. The cylinder core for the Haar form follows from the
increasing reducing stage projections and each finite smooth core.

The closed weighted Dirichlet form supplies a positive self-adjoint
Markov generator \(H_\infty^w\) on the physical completion, with
constants as its entire kernel. Comparing energies and variances on
the equivalent form domains gives
\[
\frac{m}{M}\delta_H\le\delta_w\le\frac{M}{m}\delta_H,
\qquad
\delta_H=\inf\operatorname{spec}(H_\infty|_{\mathbf1^\perp}),
\quad
\delta_w=\inf\operatorname{spec}(H_\infty^w|_{\mathbf1^{\perp_w}}).
\tag{HC18}
\]
Thus \(\delta_H=0\) implies \(\delta_w=0\) for this actual whole
clock, not only for separate regulators. Its coarse readouts need not
be the exponentials of the finite weighted generators: form consistency
constructs the whole process without asserting autonomous coarse clocks.

Thus adding closed-loop response repairs the analytic-circle kernel
without ensuring a continuum gap. Within the homogeneous additive
hypercubic Haar refinement in (HC16), the complete clock is gapless; uniformly
bounded vacuum reweighting cannot provide a uniform positive floor
either. A candidate that succeeds must change a stated part of this
construction—its effective response, observable embeddings, state
comparison, or clock realization—and control the resulting law.

[[heat-state-continuity-and-response-closability|An exact area-dependent
heat state]] now tests a change outside the bounded-density branch.
Its shrinking single-loop threshold is of order perimeter divided by
area, so the Haar cheap-loop witness no longer works. But its
length-weighted cylinder form is not closable: edge-disjoint nearby
loops have orthogonal response while converging to the same state
observable. The whole operator is absent, rather than merely gapless.
A replacement that keeps uniformly bounded responses on these
approximating loops must retain mixed responses compatible with their
state convergence. Diverging response costs or a changed domain/readout
construction leave those hypotheses and require separate control.

[[shared-driver-response-and-the-nested-holonomy-clock|A shared driving
path]] gives a closed replacement on the full nested-holonomy path sector,
with an explicit minimum-kernel mixed response and all-duration character
correlations. The same state supports both gapped and gapless driver clocks.
Requiring annular response to be unchanged by restart in the same clock
selects constant intensity within that family; the state law alone does not.
