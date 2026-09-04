# Wilson Path-Product Fibers

Edge-disjoint path products give a global Haar-preserving decomposition of a finite lattice gauge carrier into retained links and hidden fiber variables. This constructs an exact smooth conditional law without gauge fixing or a singular orbit-space chart. The retained derivative is a local Wilson plaquette score; distant induced interactions are conditional covariances of such scores. The construction supplies the finite carrier and density, not the uniform correlation estimate needed for the continuum mass gap.

**Status: [EXACT FINITE-REGULATOR GAUGE CONSTRUCTION]; [OPEN] uniform conditional response, source normalization, RG locality, and continuum realization.**

## A global product chart upstairs

Let \(G\) be a compact connected matrix Lie group with normalized Haar measure. On a finite lattice, choose oriented paths
\(P_b=(e_{b,1},\ldots,e_{b,\ell_b})\), each using an underlying edge once, with no edge shared between different paths. Paths may share vertices. Orient the edge variables along their paths; inversion preserves Haar measure.

Define

$$
V_b=U_{b,1}\cdots U_{b,\ell_b},\qquad
Z_b=(U_{b,1},\ldots,U_{b,\ell_b-1}).
\tag{WP1}
$$

Retain \(V=(V_b)\) and put all \(Z_b\) and unused fine links into the hidden coordinate \(Y\). The inverse reconstructs the last, or pivot, link:

$$
U_{e_b^*}=P_b(Z)^{-1}V_b,\qquad
P_b(Z)=Z_{b,1}\cdots Z_{b,\ell_b-1}.
\tag{WP2}
$$

Thus the change of variables is a smooth global bijection
\(\Psi:G^E\to G^{\mathcal B}\times G^{E-|\mathcal B|}\).
For fixed preceding links, replacing the pivot by \(V_b\) is left multiplication. Haar invariance and edge-disjointness give

$$
\boxed{\mathrm dU=\mathrm dV\,\mathrm dY.}
\tag{WP3}
$$

This is a change of coordinates before taking a quotient. It is not a maximal-tree gauge fixing and does not assume a smooth gauge orbit space. Overlapping path products do not inherit this product chart merely by being gauge covariant.

For the finite Wilson action \(S_\beta\), put
\(\widetilde S_\beta=S_\beta\circ\Psi^{-1}\). Then

$$
\begin{aligned}
\mathcal Z(V)&=\int e^{-\widetilde S_\beta(V,Y)}\,\mathrm dY,\\
\nu_V(\mathrm dY)&=\mathcal Z(V)^{-1}
e^{-\widetilde S_\beta(V,Y)}\,\mathrm dY,\\
\bar\mu(\mathrm dV)&=
\frac{\mathcal Z(V)}{\mathcal Z_{\mathrm{full}}}\,\mathrm dV.
\end{aligned}
\tag{WP4}
$$

Compactness and smoothness make \(\mathcal Z(V)\) strictly positive and smooth. For this class of block maps, existence of a smooth finite retained density relative to product Haar is **proved**, not an extra hypothesis. A volume-uniform local polymer expansion of \(-\log\mathcal Z\) is not proved. A positive finite density can have increasingly long-range interactions in its limits.

## Gauge covariance of the disintegration

Under \(U_e\mapsto g_{s(e)}U_eg_{t(e)}^{-1}\), the interior transformations telescope:

$$
V_b\mapsto g_{s(P_b)}V_bg_{t(P_b)}^{-1}.
\tag{WP5}
$$

The raw-link coordinates \(Y\) transform by their usual endpoint actions, independently of \(V\). Their product Haar measure is preserved. Gauge invariance of the Wilson action therefore yields

$$
\nu_{gV}=g_*\nu_V.
\tag{WP6}
$$

Consequently, the conditional expectation of a gauge-invariant fine observable is a gauge-invariant coarse observable. This does not choose \(G\) or a vacuum; it constructs a covariant block for the group and law supplied.

## The retained score is a pivot plaquette derivative

Use the right derivative

$$
R_{b,X}f(V)
=\left.\frac{\mathrm d}{\mathrm dt}\right|_{0}
f(\ldots,V_be^{tX},\ldots).
\tag{WP7}
$$

At fixed \(Y\), this changes only the pivot, \(U_{e_b^*}\mapsto U_{e_b^*}e^{tX}\). Thus

$$
s_{b,X}:=R_{b,X}\widetilde S_\beta
=(R_{e_b^*,X}S_\beta)\circ\Psi^{-1}.
\tag{WP8}
$$

For a fine source \(F\), write \(\widetilde F=F\circ\Psi^{-1}\) and
\(KF(V)=\nu_V(\widetilde F)\). The [[conditioned-source-transport|conditioned-source derivative]] becomes

$$
\boxed{R_{b,X}KF
=\nu_V(R_{b,X}\widetilde F)
-\operatorname{Cov}_{\nu_V}(s_{b,X},\widetilde F).}
\tag{WP9}
$$

The covariance is sesquilinear with its real score in the first slot. There is no missing Jacobian term in this chart. A source avoiding the pivot can have zero direct derivative but a nonzero covariance term: locality of the source before conditioning does not imply locality afterward.

Normalize the [[library/confinement-of-quarks/inq|Wilson action]] as

$$
S_\beta(U)=\beta\sum_p
\left(1-\frac1{d_{\mathsf R}}\operatorname{ReTr}\mathsf R(U_p)\right),
\qquad \beta\ge0,
\qquad
\kappa_{\mathsf R}
=\sup_{\|X\|=1}\|\mathrm d\mathsf R(X)\|_{\mathrm{op}}.
\tag{WP10}
$$

Here \(\mathsf R\) is the chosen unitary representation, and the Lie-algebra norm comes from a declared bi-invariant metric. For the incidence estimates below, assume each plaquette traverses four distinct underlying edges; degenerate periodic plaquettes require derivative-occurrence multiplicities instead. Let \(n_b\) count plaquettes containing the pivot and \(n_{bc}\) count plaquettes containing both distinct pivots. Unitarity and the normalized trace bound imply, for unit \(X,Y\),

$$
|s_{b,X}|\le\beta\kappa_{\mathsf R}n_b,\qquad
|R_{c,Y}R_{b,X}\widetilde S_\beta|
\le\beta\kappa_{\mathsf R}^2n_{bc}.
\tag{WP11}
$$

On a nondegenerate \(d\)-dimensional hypercubic lattice,
\(n_b\le2(d-1)\). These are bounds from explicit plaquette incidence; they do not presume a physical gap.

For \(\mathcal W=-\log\mathcal Z\), differentiation gives

$$
\begin{aligned}
R_{b,X}\mathcal W&=\nu_V(s_{b,X}),\\
R_{c,Y}R_{b,X}\mathcal W
&=\nu_V(R_{c,Y}R_{b,X}\widetilde S_\beta)
-\operatorname{Cov}_{\nu_V}(s_{c,Y},s_{b,X}).
\end{aligned}
\tag{WP12}
$$

For pivots sharing no plaquette, the direct term vanishes. Their entire induced coupling is the negative conditional score covariance. These are ordered derivatives; same-factor Riemannian Hessians require the connection term. This is a Wilson realization of the [[contemporary-puzzles/yang-mills-mass-gap/vacuum-boundary-gluing-and-wall-response#The nonlinear residue has a fixed sign|existing effective-Hessian identity]], not a new general Hessian formula.

The elementary covariance bound is only
\(\beta^2\kappa_{\mathsf R}^2n_bn_c\). It supplies no decay with separation and worsens as the conventional Wilson \(\beta\) grows.

## Spatial support and hidden derivatives

In fine coordinates, (WP8) depends only on the pivot's plaquette star. In the product chart, a pivot occurring in that star must be expanded using its path. An enclosing fine-link footprint is

$$
T_b=\operatorname{Star}(e_b^*)
\cup\!\!\bigcup_{c:\,e_c^*\in\operatorname{Star}(e_b^*)}P_c.
\tag{WP13}
$$

If \(\ell_c\le L\), this footprint has at most \(4n_bL\) fine links and lies within distance \(O(La)\) of the original pivot. Locality survives as bounded one-step geometry, not as strict support on just one fine plaquette star.

For a hidden coordinate \(z_k\) on path \(c\), set
\(Q=z_{k+1}\cdots z_{\ell_c-1}\). Its right variation acts on fine functions as

$$
\delta^{z_k}_Y
=R_Y^{e_{c,k}}-L_{\operatorname{Ad}_{Q^{-1}}Y}^{e_c^*}.
\tag{WP14}
$$

It moves the raw hidden link and compensates at the pivot so that \(V_c\) remains fixed. Each term differentiates plaquettes explicitly. With the independently chosen product metric on hidden coordinates, a safe bound is

$$
\|\nabla_Ys_{b,X}\|^2
\le16n_b^3L\,\beta^2\kappa_{\mathsf R}^4
\qquad(\|X\|=1).
\tag{WP15}
$$

To see the bound, each affected hidden-coordinate gradient has norm at most
\(2\beta\kappa_{\mathsf R}^2n_b\), and at most \(4n_bL\) coordinates occur. This gives the mixed-score input for conditional response estimates. It does not bound the inverse conditional Witten operator acting on that score.

## Haar measure does not fix the horizontal metric

Let \(\Gamma_{\mathrm{fine}}\) be the carré du champ from the original product bi-invariant metric on fine links. Then for a smooth coarse function \(f\),

$$
\boxed{\Gamma_{\mathrm{fine}}(f\circ B)
=\sum_b\ell_b\|\nabla_b f\|^2\circ B.}
\tag{WP16}
$$

Every edge in a path sends an orthonormal Lie-algebra variation to a coarse variation by an adjoint isometry. Summing over that edge's orthonormal basis gives \(\|\nabla_bf\|^2\); summing over the path gives \(\ell_b\). Edge-disjointness prevents overlap between paths.

Thus the inherited coarse mobility is \(\ell_b\), not one. The pivot-only lift in (WP7) is convenient for differentiation but is not the orthogonal horizontal lift for the original metric. Product-Haar factorization cannot justify silently using the chart product metric as the fine Dirichlet metric. [[contemporary-puzzles/yang-mills-mass-gap/two-scale-rg-descent-and-the-crossover-lemma|The general pullback-mobility formula]] owns this distinction.

## What this supplies to the crossover problem

The construction supplies a finite gauge-covariant carrier, smooth positive retained density, exact fixed-Haar conditional law, explicit score, and quantitative one-step derivative geometry. Those inputs are no longer merely schematic for this block class.

It does not partition the hidden fiber into independent bounded cells. Most fine links remain hidden, and path-product constraints alone do not show that they carry only ultraviolet fluctuations. The full generated action after one integration is \(\mathcal W\), not a one-coupling Wilson action; further blocking must use its actual scores and interactions. Reusing (WP11) for every subsequent effective law would erase the covariance term in (WP12).

[[thin-skeleton-and-block-average-coercivity|The thin-skeleton counterexample]] sharpens this limitation. For aligned straight paths composed from spacing \(a\) to fixed spacing \(b\), the identity fiber contains transverse, harmonic-free Maxwell variations with stiffness tending to zero as \(a\to0\) and volume grows. Thus this composite block does not have a geometry-only, uniform \(b^{-2}\) fluctuation floor. The exact Haar chart remains valid. The example neither disproves fixed-factor adjacent-shell estimates nor establishes gaplessness of the interacting conditional law. A volume-average comparison supplies a positive linear ultraviolet test, not a physical mass gap.

Reflection and coarse-translation compatibility must also be imposed on the path family. Edge-disjointness alone does not prove them. The source-normalization condition in [[conditioned-source-transport|conditioned source transport]] and the shell and terminal estimates in [[inq|RG covariance residue]] remain unproved on the asymptotically free trajectory. Known [[library/a-stochastic-analysis-approach-to-lattice-yang-mills-at-strong-coupling/inq|strong-coupling results]] do not extend to that trajectory merely because this coordinate change is exact.

[[regular-gauge-averages-and-the-selection-obstruction|The globally anchored average]] extends the fixed-Haar chart to averaged path families sharing an independent final pivot: \(V=K(Y)U_*\) has inverse \(U_*=K(Y)^*V\). The fixed-\(Y\) pivot score survives, but hidden derivatives now differentiate \(K\). The spatially adequate [[endpoint-averages-and-quadratic-ultraviolet-control|endpoint-average geometry]] must be realized by that same family before its Gaussian estimate can be combined with this chart. [[normalized-gauge-kernels-and-markov-residues|A normalized kernel]] avoids the pivot restriction at the cost of a different reverse conditional law.
