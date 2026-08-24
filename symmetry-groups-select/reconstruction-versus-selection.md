# Gauge Reconstruction Is Not Gauge Selection

AQFT can reconstruct a compact global internal group from a theory functor or from a suitable category of charged sectors, but those theorems begin with the decisive local-algebraic data already supplied. Applied to causal-scale theory, they become a symmetry-selection mechanism only if causal and modular principles independently determine that data; reconstructing the symmetry of an imported Standard Model fiber would merely recover an input.

## Choose the algebraic object first

The [[causal-wall-spectral-theory/causal-scale-interface#Three different objects called a wall|causal-wall audit]] distinguishes objects that the source dialogue initially grouped together:

| Object | Algebraic role | Relevance to internal symmetry |
|---|---|---|
| Four-dimensional observer-region net $O\mapsto\mathcal A_N(O)$ | local Lorentzian observables, locality, covariance, and charged representations | one fiberwise ingredient for sector analysis; not by itself a locally covariant theory functor |
| Horizon or cut sector | boost, area, corner, and possibly reduced normal degrees of freedom | may constrain boundary charges only after it is derived from the observer net |
| Three-dimensional Euclidean spectral QFT | stress-tensor response used in a conditional cosmological continuation | not automatically an observable net or a Connes finite spectral triple |
| Horizontal causal-scale structure $\Phi_{N_2:N_1}$ | comparison of algebras or states across scale | new proposed structure; not itself a Yang–Mills gauge group |
| Finite internal algebra $A_F$ and bimodule | internal representation data in spectral geometry | a separate microscopic candidate, absent from the current wall package |

The [[causal-wall-spectral-theory/causal-scale-interface#Minimal mathematical package|minimal interface]] still lacks a charged-sector category. It also requires an inclusion, isomorphism, common standard form, or other transport before Connes cocycles can compare states at different scales. Writing a wall assignment directly on a cut does not supply these missing structures. Fewster's natural-automorphism construction needs a functor over a spacetime category, not a single observer-region net. Ordinary DHR sectors also require bounded-region localization; Gauss-law charges such as electric charge need a broader sector framework.

## Two established reconstruction routes

In locally covariant QFT, a theory is a functor from a category of spacetimes to a category of algebras. Fewster proposes the natural automorphism group of that functor as its global gauge group and proves compactness under additional assumptions, including an energy-compactness condition in Minkowski space; see [[sources/papers/1201.3295-fewster-locally-covariant-automorphisms.pdf|Endomorphisms and automorphisms of locally covariant quantum field theories]].

In the DHR framework, a suitable symmetric tensor category of localized, transportable sectors with conjugates and finite statistics reconstructs a compact group and a charged field algebra. The construction and its hypotheses are reviewed in [[sources/papers/math-ph-0602036-halvorson-mueger-aqft.pdf|Algebraic Quantum Field Theory]]. Long-range gauge charges are not straightforward DHR sectors; the [[sources/papers/1906.09596-mund-rehren-schroer-gauss-law.pdf|Gauss-law obstruction]] is therefore relevant to any claimed reconstruction of the complete Standard Model.

Both routes are reconstruction theorems:

$$
\text{specified local theory or sector category}
\Longrightarrow
\text{compact global internal group}.
$$

They are not classification theorems saying that causal order, a binary normal plane, or modular flow forces the Standard Model category.

The reconstructed object is a compact global internal group acting on fields or sectors. Reconstruction alone does not produce a Yang–Mills connection, gauge bosons, a BRST complex, coupling constants, or gauge-field dynamics.

## The circularity test

The [[causal-wall-spectral-theory/causal-scale-interface#Logical role|interface formulation]] permits

$$
\mathcal A_N=\mathcal A_{\mathrm{QFT}}(M,g_N)
$$

as an input. If this is the Standard Model observable net, then $\operatorname{NatAut}$ or DHR reconstruction may recover its internal group, but the group entered through the fiber. The causal-scale contribution is the horizontal law $\Phi$, not the internal symmetry.

For genuine selection, the logical order must instead be:

1. state causal-wall axioms that do not contain the desired gauge group or representations;
2. construct the relevant locally covariant four-dimensional theory and an admissible framework for its short- and long-range charged sectors;
3. show that horizontal scale transport acts consistently on those sectors;
4. prove that the axioms restrict the sector category to a unique or sharply bounded class; and
5. reconstruct the group and verify its complete low-energy representation content.

If many categories survive, the framework provides an interpretation of internal symmetry but does not select it.

## Modular and internal automorphisms are different

The [[wall-construction-interface/vertical-and-horizontal-motion|modular automorphism group]] acts at fixed algebra and state, while [[wall-construction-interface/vertical-and-horizontal-motion|horizontal deformation]] moves through states. Neither is automatically the compact internal group acting on charged fields. The conditional character in [[basic-concepts/soldering/affine-scale-state|scale soldering]] belongs to the positive scale-ratio group $\mathbb R_+$; its weight is continuous, and choosing $\varrho_\perp=1$ is a physical representation choice. It does not produce the compact hypercharge group $U(1)$.

Geometric modular action can implement Lorentz transformations or PCT under strong hypotheses, as in [[sources/papers/funct-an-9302008-brunetti-guido-longo-modular-structure.pdf|Brunetti, Guido, and Longo]], but that does not identify normal reflection with weak isospin or charge conjugation. Such an identification would also endanger the required local separation between spacetime symmetry and internal gauge symmetry.

## “Spectral” names two unrelated constructions

The [[causal-wall-spectral-theory/spectral-dictionary#Three-dimensional stress response|causal-wall spectral dictionary]] uses spectral data for the continued two-point response of a three-dimensional stress tensor. A finite spectral triple uses data such as

$$
(A_F,H_F,D_F,J_F,\gamma_F).
$$

The shared word does not provide a map between them. Deriving a finite spectral geometry from the wall would be an additional theorem, not an unpacking of the existing spectral response.
