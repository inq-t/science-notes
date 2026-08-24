# The Scale-Correspondence Stack

The wall should be modeled by a scale-indexed tower of von Neumann algebras and correspondences whose overlaps are intended to glue by Connes fusion. Groupoid-valued presentation stacks preserve presentations and automorphisms; extra Q-system or expectation data add the noninvertible descent; a pointed character and a one-sided record semigroup add facthood and ontological time. Keeping these layers separate lets a homogeneous upstream law yield sectoral observable distinctions without treating the final classical spectrum as the substrate.

## The object to construct

Let \(\mathsf{Ctx}\) be a site of admissible causal contexts and \(\mathsf{Scale}\) an ordered category of scale comparisons. The proposed carrier is a pseudofunctor

$$
\boxed{
\mathfrak W:
\mathsf{Scale}
\longrightarrow
\operatorname{PSt}
\left(
\mathsf{Ctx},\mathbf{W^*Corr}
\right),}
$$

where \(\mathbf{W^*Corr}\) is the bicategory whose objects are von Neumann algebras, whose one-morphisms are correspondences, and whose composition is Connes fusion.

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

For a cover \(\{U_i\to U\}\), local algebras, states, spectral data, and overlap correspondences must satisfy effective descent. Until that theorem is proved, \(\mathfrak W\) is a correspondence prestack rather than a completed operator-algebraic stack.

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

## Completion test

A physical instance is complete only if it supplies:

1. the context site and its coverage notion;
2. the algebras, faithful states, and spectral data on each context;
3. horizontal correspondences and their fusion coherence;
4. effective gluing on overlaps;
5. Q-system, inclusion, or standard-solution data deriving each wall expectation;
6. a modularly admissible finite-index gravitational expectation or a controlled substitute;
7. the algebraically selected central edge state and its composition law;
8. spectral area and real-structure data independent of measured gravity;
9. the later commutative readout, character, and persistent record maps; and
10. a demonstration that the same construction returns the homogeneous and mean-zero blocks of [[program-core/common-response-matrix|the common response matrix]].

At present this is an **[OPEN CONSTRUCTION]**. The finite models in [[spectral-wall-descent/twist-fixed-point-wall|the twisted fixed-point wall]] and [[spectral-wall-descent/finite-index-area-weld|the finite-index area weld]] supply local pieces of the proposed object; they do not yet supply a dynamical FLRW instance or effective descent on a physical context site.

Primary sources: [finite-index expectations as Q-systems](https://arxiv.org/abs/2111.04488), [minimal index and matrix dimension with finite centers](https://arxiv.org/abs/1805.09234), and [conditional expectations selecting holographic edge states](https://arxiv.org/abs/2008.04810).
