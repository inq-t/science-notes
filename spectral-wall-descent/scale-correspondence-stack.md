# The Scale-Correspondence Stack

One candidate realization of the canonical wall package's presentation and transport slots is a scale-indexed tower of von Neumann algebras and correspondences whose overlaps glue by Connes fusion. Groupoid-valued presentation stacks preserve presentations and automorphisms; extra Q-system or expectation data add noninvertible observational loss; a pointed character and one-sided record extensions add facthood and ontological time. Keeping these layers separate lets a homogeneous upstream law yield sectoral observable distinctions without treating the final classical spectrum as the substrate.

## The object to construct

Let \(\mathsf{Ctx}\) be a site of admissible causal contexts and \(\mathsf{Scale}\) an ordered category of scale comparisons. The proposed correspondence provider is a pseudofunctor

$$
\boxed{
\mathfrak X_{\mathrm{corr}}:
\mathsf{Scale}
\longrightarrow
\operatorname{PSt}
\left(
\mathsf{Ctx},\mathbf{W^*Corr}
\right),}
$$

where \(\mathbf{W^*Corr}\) is the bicategory whose objects are von Neumann algebras, whose one-morphisms are correspondences, and whose composition is Connes fusion.

The symbol \(\mathfrak W\) is reserved for the full canonical package in [[wall-construction-interface/inq|the wall-construction interface]]. A completed wall package has a correspondence projection

$$
U_{\mathrm{corr}}(\mathfrak W)
=\mathfrak X_{\mathrm{corr}},
$$

but there is no automatic inverse: regions, cuts, observable contexts, source families, state-selection data, and physical quotients must be added and shown compatible before a correspondence prestack realizes the full interface.

Concretely, it must supply

$$
(N,U)\longmapsto
\left(
\mathcal M_N(U),
\omega_N(U),
D_N(U)
\right),
$$

and, for \(N_1\leq N_2\), a correspondence

$$
{}_{\mathcal M_{N_2}(U)}
X_{21}(U)_{\mathcal M_{N_1}(U)}.
$$

Scale composition is not an equality of carriers. It is a coherent isomorphism

$$
\boxed{
X_{32}(U)
\boxtimes_{\mathcal M_{N_2}(U)}
X_{21}(U)
\simeq
X_{31}(U),}
$$

satisfying the bicategorical associativity coherence.

A bare correspondence does not canonically determine a conditional expectation or a fixed edge state. Each proposed wall cell must additionally carry an explicit inclusion and expectation, a Q-system or Frobenius-algebra object with chosen standard solution, or equivalent data that derive both the completely positive map and its compatible edge state. Fusion coherence of \(X_{21}\) alone does not prove composition of those wall maps.

For properly infinite von Neumann algebras, the finite-index reconstruction theorem makes the missing datum exact. A normal faithful finite-index expectation is equivalent to a Q-system attached to the inclusion:

$$
\boxed{
\left(
\iota:\mathcal N\hookrightarrow\mathcal M,
E:\mathcal M\to\iota(\mathcal N)
\right)
\longleftrightarrow
Q_E=(\theta,x,w),
\qquad
\theta=\bar\iota\circ\iota.}
$$

For the conjugate solution encoded by \(w\), the expectation is recovered algebraically by

$$
\boxed{
\iota^{-1}E(m)
=
(w^*w)^{-1}w^*\bar\iota(m)w.}
$$

This is an equivalence between **inclusion plus chosen expectation** and Q-system, not between a bare correspondence and an expectation. Standard solutions recover the minimal expectation; calling that choice canonical additionally requires hypotheses such as a connected inclusion with finite-dimensional centers. With infinite centers, even minimal expectations need not be unique. Once \(E\) is fixed, its restriction to the relative commutant selects the sector edge states used by the central entropy operator. Finite index alone does not select them.

For a cover \(\{U_i\to U\}\), local algebras, states, spectral data, and overlap correspondences must satisfy effective descent. Until that theorem is proved, \(\mathfrak X_{\mathrm{corr}}\) is a correspondence prestack rather than a completed operator-algebraic stack.

## Four layers that must not be collapsed

The construction has four typed layers:

| Layer | Structure | What it does |
|---|---|---|
| presentation | groupoids or stacks of spectral presentations | retain automorphisms, stabilizers, and compatible local representatives |
| scale transport | \(W^*\)-correspondences and Connes fusion | compare different algebras without pretending they are one fixed carrier |
| observational descent | conditional expectations or declared CP instruments | remove inaccessible distinctions and generate the exact loss block when admissible |
| facthood and history | a pointed character plus nested record morphisms | select an actual outcome and orient persistent cosmic history |

Arrows in a groupoid-valued presentation stack are invertible; \(W^*\)-correspondences are generally noninvertible one-morphisms. A conditional expectation is generally neither invertible nor a \(*\)-homomorphism. A character may fail to be normal on a diffuse commutative von Neumann algebra. A record inclusion is one-sided. These are not defects in one construction; they are reasons that one categorical layer cannot perform all four jobs.

## Homogeneity and observable lumpiness

Suppose an upstream symmetry group \(G\) acts transitively on admissible presentations and a context has stabilizer \(H\). A chosen context exhibits only \(H\), while the action groupoid

$$
G\ltimes G/H
$$

retains the full symmetry of the family.

After finite-index descent, a context algebra may acquire a nontrivial center

$$
Z(\mathcal M_N(U))
=\bigoplus_\alpha\mathbb CP_\alpha.
$$

Its characters distinguish the sectors \(\alpha\), while each sector retains a noncommutative matrix or factor fibre. The observable coarse spectrum

$$
\operatorname{Spec}Z(\mathcal M_N(U))
$$

can therefore be sectorally discrete even when neither the upstream algebra nor its law contains primitive atoms. Turning those sector labels into spatial lumpiness additionally requires a localized net, support map, and effective gluing. The algebraic distinction itself arises from central idempotents of a descended context.

This is an algebraic model of the user's proposed appearance:

$$
\boxed{
\text{homogeneous law}
+\text{context and descent}
\longrightarrow
\text{sectoral observable differentiation}.}
$$

It does not prove that the physical sub-Planckian algebra is homogeneous. That claim requires the transitive action and an invariant state, class, or law to be specified rather than inferred from philosophical preference.

## The additive quantity is a cocycle, not a charge

On dualizable factor correspondences, categorical dimension is multiplicative:

$$
d(X_{32}\boxtimes X_{21})
=d(X_{32})d(X_{21}).
$$

Hence

$$
\Lambda_{21}:=\log d(X_{21})
$$

obeys

$$
\boxed{
\Lambda_{31}=\Lambda_{32}+\Lambda_{21}.}
$$

This is a monoidal valuation or additive scale cocycle. It is not a Noether charge transported through Newtonian time. It expresses coherent composition even when local presentations, stabilizers, states, and entropy partitions change.

With nontrivial centers, the scalar dimension is not the functorial invariant. The matrix dimension or full correspondence must be retained. For adjacent connected finite-center inclusions, composition of minimal expectations and multiplication of their scalar minimal indices require the intermediate spherical states to match,

$$
\boxed{
\omega_r^{\,\mathcal L\subset\mathcal N}
=
\omega_l^{\,\mathcal N\subset\mathcal M}.}
$$

Without this Markov condition, matrix dimensions still compose while scalar minimal index is generally only submultiplicative. Likewise, a central entropy operator

$$
\mathcal L_{21}
=\sum_\alpha S(\chi_{21,\alpha})P_\alpha
$$

becomes an additive cocycle only if the edge states satisfy a declared fusion or Markov compatibility. That compatibility is a theorem target, not a consequence of the word “stack.”

## Realization data are later choices

The candidate correspondence prestack is not itself a spacetime. A geometric realization requires at least

$$
(\mathcal M_N,\omega_N,D_N)
\longmapsto
(\Sigma_N,g_N,\nabla_N),
$$

together with area normalization, a solder form, real structure, causal signature, and covariance. Different real structures may realize the same complex homogeneous algebra as AdS-like or dS-like geometry. [[spectral-wall-descent/ads-calibration-and-ds-carrier|AdS calibration and the de Sitter carrier]] records what those two realizations can and cannot supply.

The observable spectral action is placed only after such a realization. Its Euler--Lagrange equations may select stable observable representatives, but least action does not create the correspondence tower assumed in writing the action.

## Provider completion

The correspondence provider is complete only if it supplies:

1. the context site and its coverage notion;
2. the algebras, faithful states, and declared spectral data on each context;
3. horizontal correspondences and their fusion coherence;
4. effective gluing on overlaps;
5. Q-system, inclusion-plus-expectation, or declared channel data for every noninvertible wall map; and
6. the compatible central edge state and composition law whenever an edge-entropy claim is made.

For the important special case in which each scale arrow is a tempered normal unital $*$-homomorphism, [[library/functoriality-of-connes-takesaki-flow-of-weights/inq|Elliott's theorem]] already makes the Falcone--Takesaki core functorial along chains. The open work is to prove that the physical arrows are tempered and to establish effective descent on genuine covers; core functoriality itself should not be advertised as the missing theorem. Arbitrary correspondences and center-valued flows require additional hypotheses.

## Downstream continuation is not provider completion

Even a completed correspondence provider does not by itself supply:

1. observer-accessible regions, selected geometric cuts, and the source readiness required by W0a and W0e;
2. [[program-core/physical-quotient|the physical quotient]];
3. finite or renormalized homogeneous and mean-zero blocks of [[program-core/common-response-form|the common response form]];
4. spectral area, a real structure, and any state--geometry weld; independence from measured gravity is additionally mandatory when the member claims to derive $G$; or
5. the later commutative character, actual outcome, and persistent record maps.

At present provider descent on a physical context site is an **[OPEN CONSTRUCTION]**. The finite models in [[spectral-wall-descent/twist-fixed-point-wall|the twisted fixed-point wall]] and [[spectral-wall-descent/finite-index-area-weld|the finite-index area weld]] supply local pieces; [[wall-construction-interface/finite-cellular-markov-wall|the finite cellular Markov wall]] adds an exact nonzero response benchmark. None supplies a dynamical FLRW instance or makes these downstream continuation gates consequences of correspondence coherence.

Primary sources: [[library/planar-algebraic-conditional-expectations/inq|finite-index expectations as Q-systems]], [[library/minimal-index-and-matrix-dimension-finite-centers/inq|minimal index and matrix dimension with finite centers]], and [[library/holographic-map-as-conditional-expectation/inq|conditional expectations selecting holographic edge states]].
