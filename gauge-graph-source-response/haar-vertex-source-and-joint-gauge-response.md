# Haar-Vertex Source and Joint Gauge Response

Haar vertex frames and retained edge heat paths jointly determine a gauge-invariant carrier, a positive state and a mixed electric-type response. The resulting closed endpoint clock has a uniform auxiliary lower bound and respects ordinary edge subdivision. Its source Ornstein--Uhlenbeck evolution does not generally descend to that endpoint clock, and neither construction supplies a Yang--Mills vacuum or physical translation generator.

**Status: [EXACT SOURCE CONSTRUCTION] for the specified finite graphs and the countable fixed-graph form closure below, under the compact connected semisimple group, heat laws, shift actions and Fisher-dual prescription.** No novelty claim is made for heat-kernel or gauge-averaging identities. The contribution to the programme is their explicitly checked joint realization and its limits.

## The source contains frames and retained edge factors

Let \(\Lambda=(\mathcal V,\mathcal E)\) be a finite oriented graph,
allowing multiple edges and loops. Fix a compact connected group
\(G\) with semisimple Lie algebra, a positive bi-invariant metric \(Q\),
\(T>0\), weights \(a_e>0\) and splits \(0<\theta_e<1\).
Write \(p_t\) for normalized heat density with generator \(\Delta_Q\).

Independently choose Haar vertex frames \(B_v\) and based heat paths
\[
U_e\sim\mu_{a_e\theta_e,T},\qquad
V_e\sim\mu_{a_e(1-\theta_e),T}.
\]
The endpoint readout is
\[
\boxed{x_e=B_{s(e)}Y_eB_{t(e)}^{-1},\qquad
Y_e=U_e(T)V_e(T)^{-1}.}
\tag{HV1}
\]
The indices \(s(e),t(e)\) denote graph endpoints, not times.
The path-product theorem in
[[gauge-path-fisher-response/heat-factor-response-and-the-compression-defect#Two sources, one complete path readout|the retained heat-factor construction]]
gives independent \(Y_e\) with density \(p_{a_eT}\).
The source-to-endpoint map is many-to-one.

Declare two types of source transformations:

- independent vertex-frame left translations \(B_v\mapsto g_vB_v\);
- independent based path translations
  \(U_e\mapsto k_eU_e,\ V_e\mapsto l_eV_e\), with finite logarithmic
  energy and \(k_e(0)=l_e(0)=1\).

The vertex transformations preserve the source law exactly. Product
independence and the scaled path-shift entropy formula give
\[
D(\nu_{k,l}\Vert\nu)=\frac14\sum_e\int_0^T
\left[
\frac{|k_e^{-1}\dot k_e|_Q^2}{a_e\theta_e}
+\frac{|l_e^{-1}\dot l_e|_Q^2}{a_e(1-\theta_e)}
\right]du.
\tag{HV2}
\]
For infinitesimal based controls \(h_e,j_e\), the Fisher norm is the
same quadratic integral with prefactor \(1/2\).
Natural logarithms fix this normalization. Every vertex-frame
direction has exactly zero score; no independent initial edge
translations have been included.

## The score radical returns the correct invariant carrier

Use the extended pointwise cotangent norm: it is finite precisely
when \(|Vf|^2\le Cg(V,V)\) for all declared controls, for some finite
\(C\). Zero-score motions must therefore annihilate the observable.
For a real smooth endpoint function \(f\), the vertex derivative is
\[
\mathcal G_vf
=\sum_{s(e)=v}\nabla_{L,e}f
-\sum_{t(e)=v}\nabla_{R,e}f.
\tag{HV3}
\]
A loop contributes to both sums. These are exactly the infinitesimal
Gauss directions, because the vertex transformation in (HV1) is
\(x_e\mapsto g_{s(e)}x_eg_{t(e)}^{-1}\).

Strict positivity of the endpoint density and smoothness promote
almost-everywhere annihilation to everywhere. Connectedness of \(G\)
then gives
\[
\boxed{\text{finite integrated smooth endpoint response}
\quad\Longleftrightarrow\quad
f\in C^\infty(G^{\mathcal E})^{G^{\mathcal V}}.}
\tag{HV4}
\]
Sufficiency follows from the finite edge metric calculation below.
This derives the correct finite-response constraint from the stated
source symmetry; it does not derive \(G\) or graph incidence from
nothing.

This differs from
[[gauge-path-fisher-response/two-sided-fisher-completion-and-the-neutral-carrier|joint output Fisher dualization]].
Applied independently to based output edges, its cheap diagonal
directions force separate edge conjugation and can exclude a valid
relative loop. Restricting that output action to common vertex
motions instead gives no response to invariant endpoints. Here the
zero-score directions are vertex gauge motions, while independent
based factor variations remain available.

## The same source fixes the mixed endpoint response

Write \(L_\xi f(x)=\partial_\epsilon f(e^{\epsilon\xi}x)|_0\) and
\(R_\xi f(x)=\partial_\epsilon f(xe^{\epsilon\xi})|_0\).
The endpoint cotangents for the source factors are
\[
\ell_e(f)=\operatorname{Ad}_{B_{s(e)}}^{-1}\nabla_{L,e}f,
\qquad
r_e(f)=-\operatorname{Ad}_{B_{t(e)}}^{-1}\nabla_{R,e}f.
\tag{HV5}
\]
The minus sign comes from \(V_e^{-1}\).
Evaluation at \(T\) in the based control metric has dual weight
\(2a_eT\theta_e\) or \(2a_eT(1-\theta_e)\), respectively.
Thus for invariant smooth real \(f,g\),
\[
\begin{aligned}
\Gamma_{\mathrm{src}}(Jf,Jg)
&=2T\sum_ea_e\left[
\theta_e Q(\ell_e(f),\ell_e(g))
+(1-\theta_e)Q(r_e(f),r_e(g))
\right]\\
&=\boxed{2T\sum_ea_eQ(\nabla_ef,\nabla_eg)
=:\Gamma_\Lambda(f,g).}
\end{aligned}
\tag{HV6}
\]
Both adjoint frames disappear by bi-invariance. Left and right
gradient pairings agree at one endpoint of an edge, so the splits
also disappear here. They need not disappear for multitime path
readouts or their source spectral data.

For two-vertex \(SU(2)\) quaternionic contexts with
\(Q=-2\operatorname{Tr}\), (HV6) is exactly the shared
response in
[[gauge-boundary-frame-gluing/oriented-context-gluing-and-mixed-response#Products and the shared response recover the whole algebra|the algebraic gluing construction]],
with its electric weights
\[
\alpha_e^{\mathrm{electric}}=2Ta_e.
\tag{HV7}
\]
In particular the same factor variation on an edge shared by two
observables supplies their cross term. It is not replaced by
independent copies in the two contexts. The corresponding determinant
replacement and cross-pair recovery therefore hold on the full
invariant algebra.

## The source also returns the state and its closed clock

The normalized endpoint density relative to product Haar is
\[
\boxed{w_\Lambda(x)
=\int_{G^{\mathcal V}}\prod_e
p_{a_eT}(B_{s(e)}^{-1}x_eB_{t(e)})\,dB.}
\tag{HV8}
\]
Integrating each \(x_e\) first proves normalization. Heat positivity,
compactness and smoothness imply \(w_\Lambda>0\), smooth, with a
positive minimum for each fixed graph and parameter choice.
Changing the integration frames proves gauge invariance.

On the complete physical carrier
\(\mathcal H_\Lambda=L^2(w_\Lambda dx)^{G^{\mathcal V}}\), close
\[
\mathcal E_\Lambda(f,g)
=\int\Gamma_\Lambda(\overline f,g)w_\Lambda\,dx.
\tag{HV9}
\]
Its form domain is inherited invariant \(H^1(G^{\mathcal E})\).
The associated nonnegative generator is
\[
\boxed{K_\Lambda
=-\frac{2T}{w_\Lambda}\sum_ea_e
\operatorname{div}_e(w_\Lambda\nabla_e),\qquad
D(K_\Lambda)=H^2(G^{\mathcal E})^{G^{\mathcal V}}.}
\tag{HV10}
\]
Uniform ellipticity and smooth positive weighting on this compact
finite raw product justify these domains. They are not a maximal
Sobolev assertion on singular orbit coordinates. The constant vacuum
is unique, since zero form energy forces every edge gradient to
vanish on the connected raw configuration space.

The second-order part is the electric law in (HV7). Its drift,
however, uses the state (HV8), which is not generally Haar or a
specified Yang--Mills vacuum. No independent potential was fitted
to choose that drift.

## A uniform auxiliary inequality comes from the source realization

Let \(N\) be unit product Ornstein--Uhlenbeck number operator on all
normalized \(U,V\) Wiener drivers. The path-space differentiation
identity in
[[gauge-path-fisher-response/heat-factor-response-and-the-compression-defect#The output response has its own closed clock|the heat-factor source form]]
gives
\[
\mathcal E_\Lambda(f,f)=\langle Jf,NJf\rangle
\tag{HV11}
\]
as quadratic forms on smooth endpoints, with the right side understood
as \(\|N^{1/2}Jf\|^2\). The vertex frames do not leave hidden physical
zero modes: for gauge-invariant \(f\),
\[
Jf(B,U,V)=f((Y_e)_e)
\]
is independent of every \(B_v\). Equivalently, the finite-response
source carrier after removing its vertex score radical is independent
of those frames. Extending \(N\) by zero on the \(B\) variables is
unnecessary; even in that extension a centered physical readout is
orthogonal to the entire frozen-frame kernel.

Simultaneous conjugation of all source paths rotates every Wiener
driver by the same adjoint action. Physical \(Jf\) is invariant under
this transformation. The first Gaussian chaos has no invariant
vector, since the semisimple Lie algebra has no fixed adjoint vector.
For centered \(f\), its chaos expansion therefore starts at degree
two. The source number-operator inequality and form closure yield
\[
\boxed{\mathcal E_\Lambda(f,f)
\ge2\|f-\mathbb E_{w_\Lambda}f\|^2.}
\tag{HV12}
\]
This bound holds on the full closed form domain, uniformly over the
finite graphs, positive weights and heat ages in this specified
family. If the graph has no physical nonconstant observables it is
vacuous. Otherwise it is a lower bound, not an assertion that two
is an eigenvalue or the exact endpoint spectral edge.

The rate is in the supplied unit source-response duration. The state
norm changes with heat ages and refinement. Neither its uniformity
nor the number two supplies a physical translation scale, a
four-dimensional continuum state, or Yang--Mills short-distance
behavior. This is not the missing Clay estimate in disguise: the
constructed family and carrier are explicitly different until those
return properties are proved.

## One countable source closes the fixed-graph infinite-volume form

Let the graph now be countable and locally finite, with positive finite
edge weights and the same \(T>0\). One countable product of the Haar
frames and independent factor paths defines (HV1) and its probability
law \(\mu_\Lambda\) directly. No density relative to infinite-product
Haar is asserted. Choose the full product-gauge invariant carrier
\[
\mathcal H_\Lambda=L^2(\mu_\Lambda)^{G^{\mathcal V}}.
\tag{HV16}
\]
Different boundary sectors or representations are not included in
this choice.

Finite smooth invariant cylinders are dense in this carrier.
Indeed finite-coordinate smooth functions are dense in the raw
space. Gauge averaging is an orthogonal projection, and on each
such cylinder involves only its finitely many incident vertices.
It therefore preserves finite smooth cylinders and approximates
every invariant vector.

Use the unit countable product-OU operator \(N\) on the normalized
factor drivers. On the invariant cylinders,
\[
\mathcal E_\Lambda(f)
=\|N^{1/2}Jf\|^2
=2T\sum_{e\in\operatorname{supp}f}a_e
       \int|\nabla_ef|_Q^2\,d\mu_\Lambda.
\tag{HV17}
\]
The closed source gradient proves closability. Define the physical
form to be its **own invariant-cylinder closure**. Normal contraction
and smooth approximation give a Dirichlet form, and its constant
core vector makes it conservative. The associated nonnegative
operator is defined by that closed form, not by an infinite-density
version of (HV10).

For cylinders, \(Jf\) is independent of the Haar frames. Approximation
and closedness of that source subspace give the same statement for
arbitrary physical \(L^2\) vectors. This avoids substituting random
frames into an arbitrary representative \(f(Y)\), which would be
unjustified when infinite-volume measures are singular. Common
conjugation still removes first Wiener chaos. Passing (HV12) through
the form closure proves
\[
\mathcal E_\Lambda(f)\ge2\operatorname{Var}_{\mu_\Lambda}(f),
\qquad \ker K_\Lambda=\mathbb C\mathbf1.
\tag{HV18}
\]
A finite cycle and nontrivial \(G\) give a nonconstant invariant
cylinder, since the corresponding finite marginal has full support.
On trees the chosen full gauge quotient has only constants.

This supplies a form core, not an operator core, a global \(H^2\)
domain, or equality with the maximal source pullback. The finite
states and forms agree on their embedded cylinders; their rebuilt
semigroups need not intertwine when cycles are added. This is an
actual infinite-volume auxiliary construction on a fixed spatial
graph. A four-dimensional continuum member, physical translations
and Yang--Mills short-distance behavior remain unconstructed.

[[gauge-graph-source-response/local-interaction-cocycle-and-global-source-response|Interacting local specifications]]
extend the countable construction through actual conditional
paired-path laws and their likelihood cocycle. Under the stated
weighted-Hessian bound, the full Fisher inverse and invariant-cylinder
form exist with controlled exterior corrections. The product-source
inequality (HV18) does not carry over merely from Fisher coercivity:
the interacting state and any tail/phase information must be tested
separately.

## Edge subdivision is a genuine representation equivalence

Split an edge into consecutive pieces with a new bivalent vertex
and \(a_e=a_{e_1}+a_{e_2}\), keeping \(T\) fixed. The coarse readout is
\(x_e=x_{e_1}x_{e_2}\). Intermediate frame cancellation and heat
convolution send the fine state to (HV8). Imposing Gauss invariance
at the new vertex leaves precisely the product holonomy, so the
fine and coarse physical carriers are unitarily identified.

Bi-invariance makes each of the two differentiated segment
contributions equal to the coarse gradient norm. Their weights add,
giving exactly the coarse form (HV9). Hence this unitary intertwines
the entire rebuilt endpoint semigroup, including its closed domain.
The argument iterates coherently for ordinary subdivisions and
edge-orientation reversal; reversing an edge exchanges its two heat
factors and inverts its holonomy.

Adding independent cycles, removing a region, or integrating out a
charged interface is not this equivalence. Nor does equivalence of
the rebuilt clocks identify their respective source OU dynamics.

## The source clock still does not descend

Already on two parallel \(SU(2)\) edges with
\(Q=-2\operatorname{Tr}\), put \(c=3/4\) and
\(F(x)=\operatorname{Tr}(x_0x_1^{-1})\).
Gauge invariance cancels the vertex frames. Let \(\mathbb E_1\)
integrate the two edge-one source paths, and let \(\Pi_2\) project
onto total second Wiener chaos. Independence gives
\[
\mathbb E_1 JF=e^{-ca_1T}\operatorname{Tr}(Y_0),\qquad
\mathbb E_1\Pi_2JF=\Pi_2^{(0)}\mathbb E_1JF.
\]
The scaled character calculation from the retained-factor construction
then gives, with standard
\(Z_0=\sqrt{\theta_0}B_0^U-\sqrt{1-\theta_0}B_0^V\),
\[
\mathbb E_1\Pi_2JF
=-\frac{a_0e^{-c(a_0+a_1)T}}2
\left(|Z_0(T)|^2-3T\right).
\tag{HV13}
\]
The quasi-invariant transformation
\((U_0,V_0)\mapsto(U_0k,V_0k)\), for a based deterministic finite-energy
path \(k\), fixes \(Y_0\) and every endpoint output. But it sends
\(Z_0(T)\) to \(\int_0^T\operatorname{Ad}_{k_u}^{-1}dZ_0(u)\).
For a nonconstant adjoint rotation path \(R_u\), write
\(Z_0^k(T)=\int_0^T R_u\,dZ_0(u)\). The change of squared norm obeys
\[
\mathbb E\left(|Z_0^k(T)|^2-|Z_0(T)|^2\right)^2
=4\left(3T^2-\left\|\int_0^T R_u\,du\right\|_F^2\right)>0.
\tag{HV14}
\]
Thus (HV13) is not fixed by a source fibre map. If \(\Pi_2JF\)
were an endpoint output, it would be fixed; independent
\(\mathbb E_1\) commutes with this transformation, and quasi-invariance
preserves the almost-everywhere equality. This is a contradiction.

The distinct eigenvalues \(e^{-n\tau}\) of \(e^{-\tau N}\) identify
every chaos projection for any \(\tau>0\). Self-adjointness therefore
implies that the complete physical endpoint subspace in this example fails to be
invariant under the source semigroup at every positive duration.
The rebuilt \(K_\Lambda\) is valid; its semigroup is not the compressed
source semigroup.

## The source family remains restrictive

For a simple oriented loop \(C\) using each edge at most once and an
irreducible representation \(\pi\), endpoint frames cancel and central
heat increments give
\[
\boxed{\mathbb E_{w_\Lambda}\chi_\pi(\operatorname{Hol}_C)
=(\dim\pi)\exp\!\left[-c_\pi T\sum_{e\in C}a_e\right],}
\tag{HV15}
\]
where \(-\Delta_Q\) has Casimir \(c_\pi\) in \(\pi\).
Reversed edges have the same central heat law. Thus these moments
depend on additive edge heat length; equal such lengths give equal
simple-loop character expectations regardless of enclosed geometry.
This is a strong consequence of source independence, not a
derivation of a Yang--Mills vacuum or a confinement law.

The inputs remain graph incidence, \(G,Q\), the heat factors and
Haar frames, their allowed transformations, and Fisher dualization.
The heat ages fix both the state and response; the splits are
source parameters invisible to these single-endpoint outputs.
Holding that full package fixed leaves no separately adjustable
endpoint mobility, but does not select the package from more
primitive principles.

Every overlap must use the same vertex frames and edge factors as
the whole source. Independently redrawing them in each context
changes the joint experiment and can erase the mixed response.

The advance over prescribing a Hamiltonian is an actual shared
source for carrier, state and mixed response. The next substantive
question is what source correlations or composition law replace
independent edge heat while retaining the correct zero-cost gauge
directions, complete relational observables and a controlled
response. Numerical conversion of (HV12) cannot answer that question.

[[gauge-graph-source-response/loop-correlations-and-the-source-response|Loop correlations]]
now supply that finite response construction through an exact averaged
endpoint Hessian. Its full source metric remains coercive, and the
same state fixes an explicit one-loop mobility. But ordinary
subdivision preserves the tilted state while changing its returned
response already at first order. Thus the unweighted subdivision
theorem above cannot simply be carried through a loop weight:
correlation and source comparison require a joint selecting law.

[[gauge-path-fisher-response/receipts/two_sided_fisher_receipt.py|The joint-source receipt]] checks
actual vertex-frame and factor derivatives, the retained diagonal
Fisher dual and its mixed observable contractions. Such finite checks
support the displayed response identities, not continuum
reconstruction or the analytic chaos argument.
