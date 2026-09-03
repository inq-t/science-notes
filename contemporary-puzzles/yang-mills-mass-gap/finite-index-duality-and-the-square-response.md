# Finite-Index Duality and the Square Response

A normal faithful finite-index conditional expectation between properly infinite von Neumann algebras contains an exact expectation-dependent square normalization. Its conjugate/Q-system data supply an intertwiner whose squared norm is the central Kosaki index; division by the square root of that index gives an isometry, which is necessarily proper in a factor when the chosen index exceeds one. Only for the minimal expectation and standard conjugate solution does this index become the intrinsic squared categorical dimension, whose logarithm is additive under fusion. This is a rigorous model of noninvertible distinction and a candidate source of the exponent \(q=2p\), not a Yang--Mills response theorem: the normalized isometry preserves every norm, a scalar index distinguishes no vacuum direction, and no energy scale or Poincare Casimir follows without a separately constructed physical carrier and coercive solder.

**Status: [EXACT -- PROPERLY INFINITE FINITE-INDEX EXPECTATIONS] for the expectation-dependent normalized-isometry theorem; [STANDARD -- MINIMAL EXPECTATION/STANDARD SOLUTION] for identifying minimal index with squared statistical dimension and for multiplicativity under Connes fusion in factor sectors; [CONDITIONAL] for the categorical/geometric \(D=4\) weld; [OPEN] for a Yang--Mills inclusion, response form, continuum limit, and Casimir comparison.**

## The channel is not yet the response

Let

$$
\iota:\mathcal N\hookrightarrow\mathcal M,
\qquad
E:\mathcal M\longrightarrow\iota(\mathcal N)
$$

be a normal faithful conditional expectation of finite Kosaki index between properly infinite von Neumann algebras. Write

$$
\Lambda_E:=\operatorname{Ind}(E)\in Z(\mathcal M)_{++},
\qquad
\Lambda_E\geq1.
$$

[[library/planar-algebraic-conditional-expectations/inq|Giorgetti's finite-index reconstruction]] proves that the inclusion and chosen expectation are equivalently encoded by conjugate morphisms and a Q-system. In the normalization used in that proof, there is an intertwiner \(\widetilde v\in\mathcal M\) such that

$$
\boxed{
\widetilde v^*\widetilde v=\Lambda_E,
\qquad
E(\widetilde v\widetilde v^*)=1.}
\tag{FI1}
$$

Giorgetti calls \(\widetilde v^*\), rather than \(\widetilde v\), the one-element Pimsner--Popa basis. This convention matters when comparing formulas.

The GNS or standard-form implementation of \(E\) is projection-like and normally has a kernel. It must not be identified with \(\widetilde v\). The expectation performs coarse graining; the conjugate intertwiner belongs to the duality data that make the finite-index descent algebraically controllable.

## Exact normalized-isometry theorem

Because \(\Lambda_E\) is central and invertible, define

$$
V_E:=\widetilde v\Lambda_E^{-1/2}.
\tag{FI2}
$$

Then

$$
\boxed{V_E^*V_E=1.}
\tag{FI3}
$$

Thus \(V_E\) is an isometry. If \(\mathcal M\) is a factor, so that \(\Lambda_E=\lambda1\), then

$$
E(V_EV_E^*)=\lambda^{-1}1.
\tag{FI4}
$$

For \(\lambda>1\), equation (FI4) rules out \(V_EV_E^*=1\). Hence

$$
\boxed{
\lambda>1
\quad\Longrightarrow\quad
V_E^*V_E=1,
\qquad
V_EV_E^*<1.}
\tag{FI5}
$$

The operator is one-to-one and norm preserving, but not onto. Its adjoint is onto but has the nonzero kernel

$$
\ker V_E^*=(1-V_EV_E^*)\mathcal H
\tag{FI6}
$$

in every faithful Hilbert-space representation. This is a deterministic one-sided geometry. Nothing random has been added: information becomes inaccessible only after one declares \(V_E^*\) to be the direction of descent and restricts attention to its output.

Proper infiniteness is structurally relevant here. An isometry from a finite-dimensional Hilbert space to itself is unitary, so a same-carrier proper isometry requires an infinite carrier. This is one reason Type III local algebras are better candidates for the pre-observable wall than finite matrix toys. It does not follow that Type III structure by itself produces dynamics, locality, or mass.

## The chosen index gives an exact square normalization

In a faithful representation \(\pi\), put

$$
A_E:=\frac12\log\pi(\Lambda_E),
\qquad
K_E:=\pi(\widetilde v),
\qquad
M_E:=e^{-A_E}=\pi(\Lambda_E)^{-1/2}.
\tag{FI7}
$$

Equations (FI1)--(FI3) become

$$
\boxed{
K_E^*K_E=e^{2A_E},
\qquad
K_EM_E=\pi(V_E),
\qquad
(K_EM_E)^*(K_EM_E)=1.}
\tag{FI8}
$$

This realizes the square-normalization grammar in [[compensated-incidence-response-and-four-dimensional-balance]] pointwise. It does not yet construct the nontrivial scale family required by that theorem. The canonical categorical square requires an additional minimality clause. For a subfactor inclusion morphism \(\iota\), its minimal expectation \(E^0\), standard conjugate solution, and associated dualizable factor correspondence \(X_\iota\),

$$
\operatorname{Ind}(E^0)
=[\mathcal M:\mathcal N]_0
=d(\iota)^2
=d(X_\iota)^2,
\tag{FI9}
$$

where \(d\) is the intrinsic statistical or categorical dimension. [[library/dualizability-and-index-of-subfactors/inq|Dualizability and index]] supplies the Type-I/II/III-compatible statement for subfactors. Under Connes fusion of dualizable factor correspondences,

$$
d(X_{32}\boxtimes X_{21})
=d(X_{32})d(X_{21}),
$$

so

$$
\boxed{
A_{31}=A_{32}+A_{21},
\qquad
A:=\log d.}
\tag{FI10}
$$

Categorical dimension supplies a multiplicative intrinsic size; its logarithm supplies an additive address; the **minimal** index supplies the square of that size. For an arbitrary finite-index expectation \(E\), the quantity \(A_E=\tfrac12\log\operatorname{Ind}(E)\) remains a valid chosen-expectation size, but it can exceed the intrinsic value and is not automatically additive under fusion. This firewall prevents a freely chosen expectation from becoming a supposedly canonical scale coordinate.

With finite-dimensional nontrivial centers, categorical dimension is generally matrix valued and the expectation index is central rather than scalar. Fusion composes the full correspondence or dimension matrix; scalar logarithms require minimal/standard solutions and matched spherical/Markov data. Diffuse centers require a more general central theory, not a finite matrix by default. [[spectral-wall-descent/scale-correspondence-stack]] and [[library/minimal-index-and-matrix-dimension-finite-centers/inq|the finite-center audit]] state that firewall.

## Why this is not yet a gap

The identity (FI8) is too perfect to be a physical coercivity theorem by itself. On a factor \(K_E^*K_E=\lambda I\): it sees no difference between the vacuum, a glueball direction, and any other vector. If an external vacuum projection is inserted,

$$
C_E:=V_E(1-P_0),
$$

then

$$
C_E^*C_E=1-P_0.
\tag{FI11}
$$

But (FI11) merely normalizes a preselected complement. It neither constructs \(P_0\) nor proves that this complement is the physical Yang--Mills nonvacuum carrier. Calling its unit lower bound a mass gap would be exactly the category error the programme is trying to remove.

Finite index supplies an order inequality on positive algebra elements,

$$
E(x)\geq\Lambda_E^{-1}x,
\qquad x\geq0,
\tag{FI12}
$$

under the relevant factor/minimal-expectation hypotheses. It does **not** imply a lower Hilbert-space frame bound for the \(L^2\) implementation of \(E\). That implementation is an orthogonal projection when \(E\) preserves the reference state and therefore has a nontrivial kernel for a proper inclusion. Algebra order, Hilbert norm, statistical dimension, and spectral energy are different types.

The range projection \(V_EV_E^*\) also depends on the chosen conjugate/Q-system realization up to the appropriate equivalence. For arbitrary \(E\), even the Kosaki index belongs to the chosen expectation; the intrinsic categorical datum is recovered from the minimal expectation and standard solution. None of these is an automatically physical detector subspace. A Yang--Mills use must construct the inclusion, expectation, and standard solution from gauge dynamics rather than choose them after inspecting a spectrum.

[[gauge-index-no-go-and-four-dimensional-center-square]] now closes one candidate and isolates another. For a faithful minimal action of an infinite compact effective group on a factor with separable predual, \(\mathcal M^G\subset\mathcal M\) has infinite index; that compact global fixed-point relation for \(SU(N)\) therefore cannot instantiate the finite-index theorem above. This does not describe local Gauss-law gauge reduction. A canonical finite remnant can occur instead in the four-dimensional ring inclusion between the additive and maximal observable algebras: the electric and magnetic center classes give \(\operatorname{Ind}=|Z(G)|^2\) under the stated pure-gauge net hypotheses. That square is topological sector capacity. It is trivial for centerless simple groups and hence cannot be the universal cause of the Yang--Mills gap.

The Hessian audit is equally restrictive. For a preserving expectation, restriction loss is exactly the squared BKM distance from the recovered tangent space, so its incoming quotient has constant one while its minimum over lifts of every retained tangent is zero. Away from the preserving state, fixed index does not bound the smallest positive Hessian ratio. Minimal index controls intrinsic categorical size; a chosen expectation index controls an expectation-dependent order bound; under additional finite-factor hypotheses an inclusion index can control maximal information loss. None is the lower response edge required for mass.

## The conditional four-dimensional weld

The square law suggests a cleaner version of the \(D=4\) clue, but a single fixed index cannot determine an exponent. This subsection concerns scalar factor-sector addresses, not a central operator or dimension matrix. Let \(S\subseteq\mathbb R\) be a declared unbounded additive address set. Suppose a normalization-rigid construction supplies a nonzero response family over \(S\) and, for every allowed nonzero translation \(t\) with \(A,A+t\in S\), proves the exact character law

$$
R_{\mathrm{dual}}(A+t)
=e^{2t}R_{\mathrm{dual}}(A).
\tag{FI13}
$$

A separately constructed codimension-two geometric response on the same family must obey

$$
R_{\partial,D}(A+t)
=e^{(D-2)t}R_{\partial,D}(A).
\tag{FI14}
$$

If a realization theorem proves the same address, the same nonzero response, and first inverse-length presentation,

$$
A_{\mathrm{cat}}=A_{\mathrm{geom}}=:A,
\qquad
R_{\mathrm{dual}}(A)=R_{\partial,D}(A),
\qquad
M=e^{-A}
\text{ has first inverse-length order},
\tag{FI15}
$$

throughout that family, then translating by every allowed \(t\) forces

$$
\boxed{D-2=2\quad\Longrightarrow\quad D=4.}
\tag{FI16}
$$

This would be stronger than importing the known engineering dimension of the Yang--Mills action: standard categorical duality would supply one response character and boundary geometry the other. It remains conditional because no theorem currently constructs a nontrivial scale family of standard correspondences, identifies log categorical dimension with log metric length, or transports the standard conjugate intertwiner to the physical boundary-flux response. Unknown prefactors, a merely asymptotic symbol, or equality at one fixed \(A\) do not force (FI16). A fixed finite index is bounded and has no bilateral scale tail; the bilateral and regulator-uniform hypotheses of the compensated-response theorem remain separate.

## The causal-grain typing

Three discrete-looking objects must not be merged:

| Object | Exact role | What it is not |
|---|---|---|
| Fredholm index of the reduced scale wall | oriented homotopy class of a one-sided crossing | Jones index or energy level |
| chosen Jones--Kosaki index \(\Lambda_E\) | expectation-dependent order size and conjugate-loop normalization | intrinsic categorical dimension or Hamiltonian gap |
| minimal index \(\operatorname{Ind}(E^0)\) | squared categorical dimension of the standard finite-index descent | response floor or Hamiltonian gap |
| spectral gap of the Poincare Casimir | uniform energetic separation of the physical vacuum | channel count or topological index |

They can nevertheless form a typed construction chain:

$$
\boxed{
\begin{aligned}
&\text{oriented wall class}
\longrightarrow
\text{candidate finite topological remnant or standard Q-system}
\longrightarrow
A=\log d,\\
&\text{descent-loss or flux response on retained tangents}
\longrightarrow
\text{uniform coercivity}
\longrightarrow
\text{full-Casimir solder}.
\end{aligned}}
\tag{FI17}
$$

The first line can model a primitive, topologically retained “mass-engagement” event. The second line is what could make it physical. [[causal-grain-as-a-mass-engagement-fossil]] therefore treats the grain as the possible index of a transition, not as a \(4.264\,\mathrm{fm}\) voxel or a \(46.27\,\mathrm{MeV}\) particle.

## Stopping conditions

This finite-index auxiliary branch advances the mass-gap programme only if it constructs:

1. a gauge-invariant inclusion or correspondence selected before any glueball spectrum is known;
2. its finite-index expectation or Q-system, with the relevant standard solution and composition law;
3. a map from the conjugate carrier to the OS interface or flux-tangent carrier;
4. a nontrivial response form on retained physical directions, not the scalar polar-normalization identity (FI8);
5. a regulator-uniform lower frame bound for that form;
6. an independent scale-character or RG calibration; and
7. a same-carrier comparison with the full \(3+1\)-dimensional Poincare Casimir.

Because the canonical center remnant is trivial for centerless simple groups, the universal coercivity route must work independently of this auxiliary branch. A proof of the Clay statement cannot require a nontrivial finite center or finite-index sector.

The route fails if low-index quantization is called an energy gap, if \(V_E^*V_E=1\) is advertised as Yang--Mills coercivity, or if the index is converted to MeV before a physical scale map exists. The exact contribution is narrower: **finite-index duality gives a principled algebraic reason for a squared response and a proper one-sided carrier.**
