---
inq.module: "three-block-bridge-factorization"
inq.include:
  - "./"
inq.ambient:
  - "**"
---
# Three-Block Bridge Factorization

A functional inequality for the **whole Euclidean slab** can force the
midpoint bridge floor directly, but its block geometry must respect the
continuum scale. For an observable supported at the midpoint, every
resampling block that omits the midpoint contributes zero; a central block
contributes exactly the variance conditioned on its two Markov-boundary
slices. The naive disjoint initial--interior--final factorization is therefore
an exact sufficient theorem, yet it cannot have a regulator-uniform constant
on the full slab carrier because boundary-adjacent fields become almost
determined as the temporal spacing vanishes. Overlapping blocks with
fixed-physical collars remove that irrelevant obstruction and retain the
exact midpoint reduction. The hard Yang--Mills problem is a collared,
gauge-covariant whole-law factorization theorem, not a one-slice sampler gap.
Cesi's finite-range two-block theorem already handles the Wilson plaquette
interaction after a cell-spin retyping and, in fact, a disconnected union of
the two end collars is enough. What remains is a surface-uniform estimate:
the published sufficient constant pays for every transverse boundary cell
and does not survive the continuum scaling of a finite physical mass.

**Status: [EXACT] for the abstract disjoint and collared reductions and for
the adjacent-slice obstruction to a regulator-uniform disjoint full-carrier
constant; [ESTABLISHED INPUT] for the cited weighted block-factorization and
Dobrushin theorems under their stated spin-system hypotheses; [EXACT
CALIBRATION] for the pure-kinetic \(SU(2)\) divergence; [OPEN] for a
Perron-compatible, surface-uniform collared factorization along the
four-dimensional Yang--Mills continuum trajectory.**

## The whole-slab theorem

Let \(\mu\) be a probability law on a product carrier

$$
\Omega
=
\Omega_-\times\Omega_0\times\Omega_+,
\tag{TB1}
$$

where \(\Omega_-\) is the initial slice, \(\Omega_+\) the final slice, and
\(\Omega_0\) the entire open slab between them. Let \(Y\) be the distinguished
middle slice, measurable inside \(\Omega_0\). For a coordinate block
\(A\in\{-,0,+\}\), write

$$
\operatorname{Var}_A(F)
:=
\operatorname{Var}
\bigl(F\mid\sigma(\Omega_{A^c})\bigr).
\tag{TB2}
$$

Suppose the whole law satisfies the three-block variance factorization

$$
\operatorname{Var}_\mu(F)
\leq
C_{\mathrm{BF}}
\sum_{A\in\{-,0,+\}}
\mathbb E_\mu[\operatorname{Var}_A(F)]
\tag{TB3}
$$

for every \(F\in L^2(\mu)\), with \(C_{\mathrm{BF}}<\infty\).

Take \(F=f(Y)\). Since changing either boundary block while holding the
interior fixed cannot change \(f(Y)\),

$$
\operatorname{Var}_-(f(Y))
=
\operatorname{Var}_+(f(Y))
=0.
\tag{TB4}
$$

Conditioning on the complement of the open interior fixes precisely the two
boundary slices. Therefore

$$
\operatorname{Var}_0(f(Y))
=
\operatorname{Var}
\bigl(f(Y)\mid X_-,X_+\bigr).
\tag{TB5}
$$

Equations (TB3)--(TB5) give

$$
\boxed{
\mathbb E\!\left[
\operatorname{Var}
\bigl(f(Y)\mid X_-,X_+\bigr)
\right]
\geq
\frac{1}{C_{\mathrm{BF}}}
\operatorname{Var}_\nu(f),}
\tag{TB6}
$$

where \(\nu=\operatorname{Law}(Y)\). In the operator notation of
[[bridge-data-augmentation-solder/inq|Bridge Data-Augmentation Solder]],
put \(Q=I-\Pi_{\mathbf1}\) on one fixed probability sector. Then

$$
\boxed{
B^{\mathrm{br}}
\geq
C_{\mathrm{BF}}^{-1}Q.}
\tag{TB7}
$$

This is not a comparison between two unrelated dynamics. It is a direct
functional inequality for the same whole path law whose disintegration
defines the bridge.

The theorem also has a carrier-restricted form. If (TB3) is proved only for
the pullbacks of a closed physical subspace \(\mathcal H_{\mathrm{phys}}
\subseteq L^2(\nu)\), then (TB7) holds on that subspace. For Yang--Mills this
is preferable to pretending that gauge-variant link coordinates are physical,
but the chosen subspace must cover the full neutral vacuum complement.

## The disjoint full-carrier criterion is too strong

The exact implication above does not make a regulator-uniform disjoint
factorization plausible. Let \((X_k)_{k=0}^{2n}\) be a stationary Markov
chain with transition \(P\), and let \(\lambda_{\mathrm{dis}}\) be the
Poincare edge of the three-block resampling form in (TB3), so that
\(C_{\mathrm{BF}}^{\mathrm{dis}}:=\lambda_{\mathrm{dis}}^{-1}\) is its
optimal factorization constant, with value \(+\infty\) when the edge
vanishes:

$$
\lambda_{\mathrm{dis}}
:=
\inf_{F\perp1}
\frac{
\sum_{A\in\{-,0,+\}}
\mathbb E[\operatorname{Var}_A(F)]
}{
\operatorname{Var}(F)
}.
\tag{TB7a}
$$

Choose a centered normalized \(f\in L^2(\nu)\) and test the
boundary-adjacent interior observable \(F=f(X_1)\). The two outer block
terms vanish, while conditioning on both outer endpoints can only reduce the
variance left after conditioning on \(X_0\). Therefore

$$
\begin{aligned}
\lambda_{\mathrm{dis}}
&\leq
\mathbb E\!\left[
\operatorname{Var}\bigl(f(X_1)\mid X_0,X_{2n}\bigr)
\right]\\
&\leq
\mathbb E\!\left[
\operatorname{Var}\bigl(f(X_1)\mid X_0\bigr)
\right]
=
1-\|Pf\|^2.
\end{aligned}
\tag{TB7b}
$$

Taking the infimum over centered \(f\) gives the operator bound

$$
\boxed{
\lambda_{\mathrm{dis}}
\leq
1-\|PQ\|^2,}
\tag{TB7b1}
$$

where \(Q=I-\Pi_{\mathbf1}\). If \(Pf=pf\), then the best constant in
(TB3) obeys

$$
\boxed{
C_{\mathrm{BF}}^{\mathrm{dis}}
=
\lambda_{\mathrm{dis}}^{-1}
\geq
\frac{1}{1-|p|^2}.}
\tag{TB7c}
$$

This is an adjacent-slice obstruction, independent of how far the midpoint
lies from the outer boundaries. It does **not** say that the fixed-physical
midpoint bridge floor vanishes. It says that the full disjoint block carrier
contains boundary-adhesion directions that are irrelevant to that floor.

The divergence is not peculiar to an exactly known eigenfunction. Suppose
\(H_a\geq0\) is self-adjoint,
\(P_a=e^{-a_{\tau,a}H_a/(\hbar c)}\), and there are normalized centered
trial vectors \(f_a\in\mathcal D(H_a^{1/2})\) with
\(\|H_a^{1/2}f_a\|^2\leq E_*<\infty\). The scalar inequality
\(1-e^{-2u}\leq2u\) gives

$$
1-\|P_af_a\|^2
\leq
\frac{2a_{\tau,a}E_*}{\hbar c},
\qquad
\boxed{
C_{\mathrm{BF}}^{\mathrm{dis}}(a)
\geq
\frac{\hbar c}{2a_{\tau,a}E_*}.}
\tag{TB7c1}
$$

Thus any continuum limit retaining even one nonvacuum finite-energy
direction forces the disjoint full-carrier constant to diverge. This uses no
assumed positive gap. The same test remains inside the gauge-invariant path
carrier whenever \(f_a\) is gauge invariant.

The pure product-Wilson transfer gives an action-level calibration under the
full-vertex-gauging and no-extra-global-constraint hypotheses used in the
linked calculation. For \(SU(2)\), let \(x\) be the temporal Wilson
concentration and let
\(g(\Gamma)\) be the length of a shortest closed spin network on the spatial
graph. The fundamental shortest-loop mode has adjacent-slice eigenvalue

$$
p_{x,\Gamma}
=
\left(\frac{I_2(x)}{I_1(x)}\right)^{g(\Gamma)}.
\tag{TB7d}
$$

Since

$$
\frac{I_2(x)}{I_1(x)}
=
1-\frac{3}{2x}+O(x^{-2}),
\tag{TB7e}
$$

(TB7c) gives

$$
\boxed{
C_{\mathrm{BF}}^{\mathrm{dis}}
\geq
\frac{x}{3g(\Gamma)}+O(1).}
\tag{TB7f}
$$

Here \(x\to\infty\) with \(g(\Gamma)\) fixed, as on a fixed-girth plaquette
lattice. In the standard tree-level anisotropic \(SU(2)\) Wilson
normalization,
\(x=4a_s/(g_0^2a_\tau)\), so the bound diverges at least as
\(a_\tau^{-1}\) when \(a_s,g_0\) are fixed. On an isotropic asymptotically
free trajectory, \(x=4/g_0(a)^2\to\infty\). The exact transfer calculation is
developed in
[[contemporary-puzzles/yang-mills-mass-gap/finite-spacing-transfer-and-bounded-flux-solder|Finite-Spacing Transfer and the Bounded Flux Solder]].

## Fixed-physical collars give the right reduction

The weighted block theorem allows overlaps, which remove the
boundary-adhesion test without abandoning the whole law. On a path indexed
by \(0,\ldots,2n\), choose an integer \(1\leq r<n\) and define

$$
\begin{aligned}
A_-&=\{0,\ldots,r\},\\
A_0&=\{1,\ldots,2n-1\},\\
A_+&=\{2n-r,\ldots,2n\}.
\end{aligned}
\tag{TB7g}
$$

The outer blocks overlap the open-interior block in collars but omit the
midpoint \(n\). Let \(\nu=\operatorname{Law}(X_n)\), define

$$
\begin{aligned}
J_n &:L^2(\nu)\longrightarrow L^2(\mu),
&J_nf&:=f(X_n),\\
\mathscr L_\alpha
&:=
\sum_{A\in\{A_-,A_0,A_+\}}
\alpha_A\left(I-\mathsf E_{A^c}\right),
\qquad &\alpha_A&\geq0,
\end{aligned}
\tag{TB7g1}
$$

and write
\(\mathscr L_{3B}^{\mathrm{coll}}:=\mathscr L_{\mathbf1}\) for unit weights.
Suppose the corresponding weighted variance factorization holds:

$$
\gamma(\alpha)\operatorname{Var}_\mu(F)
\leq
C_{\mathrm{coll}}
\sum_{A\in\{A_-,A_0,A_+\}}
\alpha_A\,\mathbb E_\mu[\operatorname{Var}_A(F)],
\tag{TB7h}
$$

where
\(\gamma(\alpha)=\min_k\sum_{A\ni k}\alpha_A>0\). For
\(F=f(X_n)\), the two collar terms vanish, while
\(A_0^c=\{0,2n\}\). This gives the exact weighted compression

$$
\boxed{
J_n^*\mathscr L_\alpha J_n
=
\alpha_{A_0}B_n^{\mathrm{br}}.}
\tag{TB7h1}
$$

Consequently the weighted inequality gives

$$
\boxed{
B_n^{\mathrm{br}}
\geq
\frac{\gamma(\alpha)}
{C_{\mathrm{coll}}\alpha_{A_0}}\,Q.}
\tag{TB7i}
$$

With unit weights,
\(\mathscr L_\alpha=\mathscr L_{3B}^{\mathrm{coll}}\) and
\(\gamma(\alpha)=\alpha_{A_0}=1\). Taking

$$
n(a)a_{\tau,a}\longrightarrow\ell_*>0,
\qquad
r(a)a_{\tau,a}\longrightarrow\delta\in(0,\ell_*)
\tag{TB7j}
$$

makes both the bridge and the overlaps physical rather than fixed numbers of
ultraviolet slices. A boundary-adjacent test such as \(f(X_1)\) now receives
a contribution from the left collar block, so (TB7b) no longer forces the
factorization constant to diverge. The theorem remains a sufficient route,
not a proof that \(C_{\mathrm{coll}}\) stays bounded.

[[three-block-bridge-factorization/receipts/collared_block_factorization_receipt.py|The
finite path receipt]] enumerates a stationary Markov chain and checks the
disjoint bound, the exact collared compression
\(J_n^*\mathscr L_{3B}^{\mathrm{coll}}J_n=B_n^{\mathrm{br}}\), and the
large-\(x\) Bessel scaling. Its
[[three-block-bridge-factorization/receipts/collared-block-factorization-receipt-output.txt|stored
output]] records the passing run. It verifies finite arithmetic, not the
Wilson factor-graph extension or a continuum bound.

## Entropy factorization is a sufficient input

For a nonnegative density \(g\), define the conditional block entropy in the
usual way. For a block family \(\mathcal B\) with nonnegative weights
\(\alpha_A\) and positive coverage
\(\gamma(\alpha)=\min_x\sum_{A\ni x}\alpha_A\), suppose

$$
\gamma(\alpha)\operatorname{Ent}_\mu(g)
\leq
C_{\mathrm{EF}}
\sum_{A\in\mathcal B}
\alpha_A\mathbb E_\mu[\operatorname{Ent}_A(g)],
\tag{TB8}
$$

then first apply (TB8) to a bounded centered \(F\) and
\(g_\varepsilon=1+\varepsilon F\) for sufficiently small \(\varepsilon\),
so the density stays nonnegative. Comparing second-order terms as
\(\varepsilon\to0\) gives the identically weighted variance factorization;
truncation extends it to \(L^2\). For the unit-weight disjoint cover this is
(TB3) with \(C_{\mathrm{BF}}=C_{\mathrm{EF}}\), and for the collared cover it
is (TB7h) with \(C_{\mathrm{coll}}=C_{\mathrm{EF}}\). Thus

$$
\text{whole-slab entropy factorization}
\Longrightarrow
\text{whole-slab variance factorization}
\Longrightarrow
\text{bridge floor}.
\tag{TB9}
$$

Caputo and Parisi prove precisely this weighted block factorization of
entropy, uniformly in finite volume and external boundary condition, for
their class of nearest-neighbor lattice spin systems under strong spatial
mixing. Their coverage factor is

$$
\gamma(\alpha)
=
\min_x\sum_{A\ni x}\alpha_A.
\tag{TB9a}
$$

For both the disjoint and collared three-block covers with unit weights,
\(\gamma(\alpha)=1\), so (TB8) specializes literally. The overlapping family
(TB7g) therefore implies (TB7h) if the theorem's hypotheses and constant can
be established at the required physical collar scale. See
[[library/block-factorization-of-the-relative-entropy-via-spatial-mixing/inq|Block
Factorization of the Relative Entropy via Spatial Mixing]].

The Caputo--Parisi theorem does not immediately cover the raw-link Wilson
presentation: it is formulated for nearest-neighbor pair potentials, while a
plaquette is a four-link hyperinteraction. This is not the end of the route.
Cesi's earlier two-block quasi-factorization allows bounded finite-range
many-body interactions and compact continuous single-spin spaces. Assigning
each site the tuple of its outgoing links makes every plaquette a range-one
interaction of three cell spins. Moreover, for the midpoint application one
may combine the two end collars into one disconnected block \(D\). A
two-block inequality for \((D,A_0)\) already leaves only the middle-block
conditional variance and hence implies the bridge floor; no arbitrary-weight
three-block theorem is needed.

This closes the finite-regulator interaction-typing problem, but not the
uniform estimate. Cesi's proof bounds the dependence defect by a term
proportional to the number of transverse boundary cells. At fixed physical
collar width that sufficient test deteriorates in the infinite-area limit and
along a finite-mass continuum trajectory. The exact construction and the
resulting Hilbertian surface-response target are isolated in
[[collared-quasi-factorization-and-surface-response/inq|Collared
Quasi-Factorization and Surface Response]].

## A three-macroblock Dobrushin pilot

There is a more explicit but typically more restrictive finite-regulator
route for the disjoint product decomposition. Treat the three
sets \(\Omega_-,\Omega_0,\Omega_+\) themselves as the coordinates of a Gibbs
specification. Equip them with metrics and let

$$
\mathcal C=(c_{AB})_{A,B\in\{-,0,+\}}
\tag{TB10}
$$

be the Wasserstein Dobrushin interdependence matrix of their conditional
laws. For \(A\neq B\), define

$$
c_{AB}
:=
\sup_{\substack{
\xi=\xi'\text{ off }B\\
d_B(\xi_B,\xi'_B)>0}}
\frac{
W_{1,d_A}\!\left(
\mu_A(\mathord\cdot\mid\xi_{A^c}),
\mu_A(\mathord\cdot\mid\xi'_{A^c})
\right)
}{d_B(\xi_B,\xi'_B)}
\tag{TB10a}
$$

and put \(c_{AA}=0\). The coordinatewise proof of Liming Wu's variance
theorem extends to heterogeneous product coordinates
\(\Omega_-\times\Omega_0\times\Omega_+\) with their own metrics. Subject to
its regular-conditional-law and finite-second-moment hypotheses, it gives

$$
\bigl(1-r_{\mathrm{sp}}(\mathcal C)\bigr)
\operatorname{Var}_\mu(F)
\leq
\sum_A
\mathbb E_\mu[\operatorname{Var}_A(F)]
\tag{TB11}
$$

whenever \(r_{\mathrm{sp}}(\mathcal C)<1\). Specializing again to
\(F=f(Y)\) yields

$$
\boxed{
B^{\mathrm{br}}
\geq
\bigl(1-r_{\mathrm{sp}}(\mathcal C)\bigr)Q.}
\tag{TB12}
$$

See
[[library/poincare-and-transportation-inequalities-for-gibbs-measures-under-the-dobrushin-uniqueness-condition/inq|Poincare
and Transportation Inequalities for Gibbs Measures under the Dobrushin
Uniqueness Condition]].

This is categorically different from proving rapid mixing for a sampler on
the **one-slice marginal** \(\nu\). The latter does not know the temporal
coupling and cannot bound the bridge. The macroblock matrix in (TB10) belongs
to the full three-part spacetime law, so its central conditional variance is
already the temporal bridge residue.

Dobrushin control is likely too strong for the final continuum theorem. It is
valuable as a finite-volume pilot because every needed coefficient is an
explicit boundary-response estimate. Strong spatial mixing and block
factorization are the more flexible targets. Moreover, (TB7b) proves that a
uniform Dobrushin edge for the unblocked disjoint three-coordinate law cannot
survive temporal refinement on the full path carrier. A viable Dobrushin
variant would have to act after scale-adapted coarse graining or directly on
an overlapping-block dynamics; neither follows from Wu's coordinate theorem
by relabelling.

## The channel form

The endpoint pair defines a channel

$$
\mathcal B_\ell:
Y\longmapsto(X_-,X_+).
\tag{TB13}
$$

For the stationary input law \(\nu\), its fixed-input \(\chi^2\) contraction
coefficient on a centered carrier \(\mathcal H\) is

$$
\eta_{\chi^2,\mathcal H}(\nu,\mathcal B_\ell)
=
\|K_\ell|_\mathcal H\|^2.
\tag{TB14}
$$

Hence

$$
\boxed{
\kappa_{\mathcal H}^{\mathrm{br}}
=
1-\eta_{\chi^2,\mathcal H}(\nu,\mathcal B_\ell).}
\tag{TB15}
$$

This is the channel-Poincare interpretation developed by Raginsky: the
Dirichlet energy of a channel is the conditional variance left after its
output is known. See
[[library/strong-data-processing-inequalities-and-phi-sobolev-inequalities-for-discrete-channels/inq|Strong
Data Processing Inequalities and Phi-Sobolev Inequalities for Discrete
Channels]].

Equation (TB15) is an exact retyping, not a proof. Assuming the channel
coefficient is less than one by a uniform amount merely renames the bridge
target. Its value is that established SDPI, spatial-mixing, and block-dynamics
tools can now be judged by whether their hypotheses concern the actual
middle-to-endpoints channel.

## Transfer mixing cannot be used backwards

The endpoint observer can ignore one endpoint, so for a reversible half-slab
transfer \(P_\ell\),

$$
\|K_\ell Q\|
\geq
\|P_\ell Q\|.
\tag{TB16}
$$

Equivalently,

$$
\kappa_{\mathrm{br}}
\leq
1-\|P_\ell Q\|^2.
\tag{TB17}
$$

Thus a bridge floor implies transfer contraction; transfer contraction alone
does not imply a bridge floor. Two endpoints can recover a middle state
synergistically even when either endpoint by itself remembers very little.

This failure persists for reversible Markov kernels that are positive
semidefinite on \(L^2\). Along an admissible LPS sequence of degrees
\(d=p+1\to\infty\), with the auxiliary prime chosen so the graph is
bipartite and has girth at least ten, let
\(G_d=(L_d,R_d,E_d)\) be the resulting connected \(d\)-regular Ramanujan
graph. This is a subsequence construction, not an existence claim for every
integer degree. If \(K_d\) is normalized biadjacency, define the same-side
two-step kernel

$$
P_d:=K_dK_d^*
\quad\text{on }L^2(L_d,\mathrm{unif}).
\tag{TB17a}
$$

It is Markov, self-adjoint, and positive semidefinite as an \(L^2\) operator;
this does not mean that every transition probability is strictly positive.
The Ramanujan estimate
gives

$$
\|P_dQ_d\|
\leq
\frac{4(d-1)}{d^2}
\longrightarrow0.
\tag{TB17b}
$$

A two-step \(P_d\)-path has a natural lift obtained by sampling its three
hidden \(R_d,L_d,R_d\) vertices, hence is an underlying four-edge walk in
\(G_d\). With probability \((1-1/d)^3\), that lifted walk has no immediate
reversal. Girth at least ten then makes it the unique length-four path between
its endpoints, so on this event those endpoints determine the middle vertex.
If \(N_d=|L_d|\), the average trace
of the bridge Gramian therefore bounds its smallest centered eigenvalue by

$$
\boxed{
\kappa_d^{\mathrm{br}}
\leq
\frac{N_d}{N_d-1}
\left[1-(1-1/d)^3\right]
=
O(d^{-1}).}
\tag{TB17c}
$$

Yet \(\ker B_d^{\mathrm{br}}=\mathbb C1\): the bridge with equal endpoints
connects each vertex to every positive \(P_d\)-neighbor, and connectedness
of the same-side graph propagates equality. The underlying spectral/girth
theorem is due to Lubotzky, Phillips, and Sarnak; this bridge counterexample
is a derived application, not a result stated in their paper. See
[[library/ramanujan-graphs/inq|Ramanujan Graphs]].

Choose a subsequence with
\(\sup_i\|P_iQ_i\|<1\), \(\kappa_i^{\mathrm{br}}>0\), and
\(\kappa_i^{\mathrm{br}}\downarrow0\); every local bridge augmentation has
only constants fixed. Use simultaneous product evolution on the countable
product probability space. Finite-coordinate ANOVA and martingale
convergence then give one carrier with all three properties:

$$
\|P Q\|<1,
\qquad
\ker B^{\mathrm{br}}=\mathbb C1,
\qquad
\inf\sigma(B^{\mathrm{br}}|_{Q\mathcal H})=0.
\tag{TB18}
$$

The first condition is a genuine transfer gap. The second excludes exact
endpoint recovery. The third says approximate endpoint recovery still
destroys the bridge floor. Therefore the minimal qualitative slogan is not
"no deterministic recovery" but the quantitative estimate

$$
\boxed{
\|K_\ell Q\|<1.}
\tag{TB19}
$$

Along a family of regulators, the strict inequality must be uniform.

## Relative quasi-factorization isolates endpoint synergy

Let \(\mathsf E_-\) be conditional expectation onto the initial boundary and
\(\mathsf E_{-,+}\) conditional expectation onto both boundaries. For the
middle embedding \(J\), define

$$
\begin{aligned}
D_-&:=J^*(I-\mathsf E_-)J=I-P_\ell^*P_\ell,\\
B^{\mathrm{br}}&:=J^*(I-\mathsf E_{-,+})J,\\
A&:=(\mathsf E_{-,+}-\mathsf E_-)J.
\end{aligned}
\tag{TB20}
$$

Nested orthogonal projections give the exact decomposition

$$
\boxed{
D_-
=
B^{\mathrm{br}}+A^*A.}
\tag{TB21}
$$

The term \(A^*A\) is the extra predictive information supplied by revealing
the second endpoint after the first is known. If a transfer estimate gives

$$
D_-\geq\gamma Q,
\tag{TB22}
$$

then the precise additional hypothesis needed to infer a bridge floor is the
relative quasi-factorization

$$
\boxed{
D_-\leq C_{\mathrm{qf}}B^{\mathrm{br}},}
\tag{TB23}
$$

or equivalently

$$
A^*A
\leq
(C_{\mathrm{qf}}-1)B^{\mathrm{br}}.
\tag{TB24}
$$

Together they yield

$$
B^{\mathrm{br}}
\geq
\frac{\gamma}{C_{\mathrm{qf}}}Q.
\tag{TB25}
$$

Assume \(Q\) is the reducing complement of the common fixed space, so
\(0\leq D_-\leq Q\). Given a transfer floor \(\gamma>0\), existence of some
finite \(C_{\mathrm{qf}}\) is equivalent to existence of a bridge floor:
(TB23) and \(D_-\geq\gamma Q\) give (TB25), while
\(B^{\mathrm{br}}\geq\kappa Q\) gives
\(D_-\leq Q\leq\kappa^{-1}B^{\mathrm{br}}\). This does not solve the
problem; it identifies exactly what transfer mixing lacks: control of the
*synergy* between the two opposed boundaries.

The Gaussian calibration computes this constant rather than assuming it. For
a scalar mode with \(r=e^{-\omega\ell}\),

$$
C_{\mathrm{qf}}^{\mathrm{opt}}=1+r^2\leq2.
\tag{TB26}
$$

See [[gaussian-bridge-gap-calibration/inq|Gaussian Bridge-Gap Calibration]].

## Wilson programme

For a regulated Euclidean Wilson cylinder with outer preparation depth
\(m\), one may work either with its full fixed-boundary law or with the
normalized inner-slab marginal \(\mu_{a,L,m}^{\mathrm W}\) on the marked
time cells \(0,\ldots,2n\). The full law is preferable when applying a
translation-invariant finite-range theorem: conditioning on its preparation
variables only makes the raw middle defect smaller than the two-endpoint
bridge, which is the sufficient direction. A noncircular route is:

1. choose \(n(a)a_{\tau,a}\to\ell_*>0\) and a collar
   \(r(a)a_{\tau,a}\to\delta\in(0,\ell_*)\), and construct a declared
   time-cell carrier before forming the overlapping blocks in (TB7g). One
   may use the exact transfer-kernel chain of full slice configurations, or
   the outgoing-link cell-spin carrier in which every link variable belongs
   to exactly one cell and every plaquette becomes a range-one three-cell
   factor. The two presentations must be related by an explicit slice
   pushforward, not merely said to represent the same action;
2. prove either (TB7h), or the sufficient two-block inequality for the
   disconnected end block \(D=A_-\cup A_+\) and the interior \(A_0\), for
   the actual Wilson path law with one constant uniform in spatial volume,
   outer boundary data, preparation depth, regulator, and retained gauge-flux
   sector. Cesi supplies the finite-regulator implication under complete
   analyticity after the outgoing-link cell-spin retyping, but its published
   boundary-counting constant is not uniform in transverse area;
3. restrict through gauge-equivariant conditional expectations while
   retaining exposed boundary charges, diagonal Gauss gluing, and the
   vacuum-balance sector. To claim an in-sector block generator, prove that
   the physical sector projection commutes with every block expectation;
   otherwise prove (TB7h) only on the complete family of physical midpoint
   pullbacks. Do not gauge-close each collar separately;
4. pass \(m\to\infty\) to the stationary Perron-dressed bridge without
   replacing its endpoint base law by Haar measure;
5. use (TB7i), or the two-block reduction (CQ6) in
   [[collared-quasi-factorization-and-surface-response/inq|the surface-response
   module]], to obtain one regulator-uniform fixed-physical bridge floor;
6. use the already proved bridge-to-transfer order, then OS and Poincare
   reconstruction, to obtain the physical mass statement.

The raw-link option has an additional conditional-expectation gate. Let
\(V:L^2(\mu_{a,L,m}^{\mathrm W})\to L^2(\widetilde\mu)\) be the isometric
pullback along the slice pushforward, put
\(\widetilde J_n:=VJ_n\), and let
\(\widetilde{\mathsf E}_{A^c}\) condition on the raw coordinates outside
each block \(A\). Require \(X_n\) to be measurable from the declared
midpoint-cell coordinates and require both collar blocks \(A_\pm\) to omit
all those coordinates. Then their compressed terms vanish. With

$$
\widetilde{\mathscr L}_\alpha
:=
\sum_{A\in\{A_-,A_0,A_+\}}
\alpha_A\left(I-\widetilde{\mathsf E}_{A^c}\right),
$$

one has

$$
\widetilde J_n^*
\left(I-\widetilde{\mathsf E}_{A_\pm^c}\right)
\widetilde J_n
=0.
\tag{TB27a}
$$

If the raw exterior sigma-algebra for \(A_0\) contains the two endpoint
slice states, conditioning monotonicity therefore gives

$$
\boxed{
\widetilde J_n^*\widetilde{\mathscr L}_\alpha\widetilde J_n
=
\alpha_{A_0}\widetilde J_n^*
\left(I-\widetilde{\mathsf E}_{A_0^c}\right)
\widetilde J_n
\leq
\alpha_{A_0}B_n^{\mathrm{br}}.}
\tag{TB27}
$$

Consequently a raw-carrier version of (TB7h) gives

$$
\gamma(\alpha)\|Qf\|^2
\leq
C_{\mathrm{coll}}
\langle\widetilde J_nf,
\widetilde{\mathscr L}_\alpha\widetilde J_nf\rangle
\leq
C_{\mathrm{coll}}\alpha_{A_0}
\langle f,B_n^{\mathrm{br}}f\rangle,
\tag{TB27b}
$$

and hence exactly the bridge floor (TB7i). Exact compression instead
requires the stronger Markov-shielding identity

$$
\mathbb E_{\widetilde\mu}
\!\left[f(X_n)\mid\widetilde{\mathcal F}_{A_0^c}\right]
=
\mathbb E_{\widetilde\mu}
\!\left[f(X_n)\mid X_0,X_{2n}\right].
\tag{TB28}
$$

Equality of pushforward laws alone does not imply (TB28).

The disjoint alternative (TB3) is now ruled out as a uniform full-carrier
target by (TB7c1). Microscopic strong mixing uniform in lattice units would
also be too strong and could encode a divergent physical rate. The viable
target is a scale-adapted overlapping factorization with a fixed physical
collar. Cesi removes the need for a new finite-range hyperedge theorem, but
its \(L^\infty\) boundary telescoping introduces a surface-cardinality loss.
The next proof must replace that loss by a tensorizing \(L^2\) maximal-
correlation or Friedrichs-angle estimate derived from the Wilson action, or
obtain an equivalent scale-adapted finite-size or renormalization bound.

The route is "whole before part" in a precise sense. The functional
inequality is imposed or derived on the full path law with a cover adapted
to physical scale. Only afterward is it tested on a midpoint-supported
Euclidean cylinder observable, where the two collar terms vanish and the
bridge residue appears. No one-slice stochastic dynamics is promoted to
ontology or clock time.

## Claim boundary

- A one-slice Poincare or log-Sobolev inequality is neither (TB3) nor the
  collared whole-law inequality (TB7h).
- A regulator-uniform disjoint full-carrier factorization is not the target:
  (TB7c1) forces its best constant to diverge whenever a finite-energy
  nonvacuum direction survives temporal refinement.
- Strong spatial mixing is a strong sufficient input, not the definition of a
  mass gap and not known uniformly on the Yang--Mills continuum trajectory.
- The three-macroblock use of Wu is a coordinatewise heterogeneous extension
  of the cited theorem and still requires regular conditional laws, chosen
  block metrics, finite second moments, and an independently bounded
  interdependence matrix.
- Deriving spatial mixing from an assumed spectral gap, exponential
  clustering, or the desired bridge estimate would be circular here.
- The Caputo--Parisi nearest-neighbor theorem does not automatically include
  plaquette interactions. Cesi's finite-range theorem does include the
  cell-spin plaquette interaction, but it does not automatically supply
  gauge-sector restriction, Perron boundary weights, surface-uniformity, or
  continuum scaling.
- Overlap removes the elementary boundary-adhesion obstruction; it does not
  prove the uniform collared inequality.
- Gauge fixing is not harmless unless its carrier, Jacobian, residual gauge
  action, and boundary sectors are controlled.
- The whole-slab law is a probability representation. Conditional variance
  does not assert stochastic ontology.
- The bridge floor still needs physical transfer identification, OS
  reconstruction, vacuum uniqueness, locality, and Poincare covariance.

## Dependencies

- [[bridge-data-augmentation-solder/inq|Bridge Data-Augmentation Solder]]
- [[gaussian-bridge-gap-calibration/inq|Gaussian Bridge-Gap Calibration]]
- [[gauge-boundary-frame-gluing/inq|Gauge Boundary-Frame Gluing]]
- [[gauge-cycle-innovation-filtration/inq|Gauge-Cycle Innovation Filtration]]
- [[vacuum-aligned-innovation-completion/inq|Vacuum-Aligned Innovation Completion]]
- [[strong-coupling-gap-and-continuum-crossover/inq|Strong-Coupling Gap and Continuum Crossover]]
- [[collared-quasi-factorization-and-surface-response/inq|Collared Quasi-Factorization and Surface Response]]
- [[library/block-factorization-of-the-relative-entropy-via-spatial-mixing/inq|Block Factorization of the Relative Entropy via Spatial Mixing]]
- [[library/quasi-factorization-of-the-entropy-and-logarithmic-sobolev-inequalities-for-gibbs-random-fields/inq|Quasi-Factorization of the Entropy and Logarithmic Sobolev Inequalities for Gibbs Random Fields]]
- [[library/poincare-and-transportation-inequalities-for-gibbs-measures-under-the-dobrushin-uniqueness-condition/inq|Poincare and Transportation Inequalities for Gibbs Measures under the Dobrushin Uniqueness Condition]]
- [[library/strong-data-processing-inequalities-and-phi-sobolev-inequalities-for-discrete-channels/inq|Strong Data Processing Inequalities and Phi-Sobolev Inequalities for Discrete Channels]]
- [[library/ramanujan-graphs/inq|Ramanujan Graphs]]
