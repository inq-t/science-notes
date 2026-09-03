# Gauge Reconstruction Is Not Gauge Selection

AQFT can reconstruct a compact global internal group from a theory functor or from a suitable category of charged sectors, but those theorems begin with the decisive local-algebraic data already supplied. Applied to causal-scale theory, they become a symmetry-selection mechanism only if causal and modular principles independently determine that data; reconstructing the symmetry of an imported Standard Model fiber would merely recover an input.

## Choose the algebraic object first

The [[wall-construction-interface/state-coordinate-types|wall state-coordinate audit]] distinguishes objects that the source dialogue initially grouped together:

| Object | Algebraic role | Relevance to internal symmetry |
|---|---|---|
| Four-dimensional observer-region net $O\mapsto\mathcal A_N(O)$ | local Lorentzian observables, locality, covariance, and charged representations | one fiberwise ingredient for sector analysis; not by itself a locally covariant theory functor |
| Horizon or cut sector | boost, area, corner, and possibly reduced normal degrees of freedom | may constrain boundary charges only after it is derived from the observer net |
| Three-dimensional Euclidean spectral QFT | stress-tensor response used in a conditional cosmological continuation | not automatically an observable net or a Connes finite spectral triple |
| Horizontal causal-scale structure $\Phi_{N_2:N_1}$ | comparison of algebras or states across scale | new proposed structure; not itself a Yang–Mills gauge group |
| Finite internal algebra $A_F$ and bimodule | internal representation data in spectral geometry | a separate microscopic candidate, absent from the current wall package |

The [[wall-construction-interface/inq#The minimal package|minimal wall interface]] still lacks a charged-sector category. It also requires an inclusion, isomorphism, common standard form, or other transport before Connes cocycles can compare states at different scales. Writing a wall assignment directly on a cut does not supply these missing structures. Fewster's natural-automorphism construction needs a functor over a spacetime category, not a single observer-region net. Ordinary DHR sectors also require bounded-region localization; Gauss-law charges such as electric charge need a broader sector framework.

## Two established reconstruction routes

In locally covariant QFT, a theory is a functor from a category of spacetimes to a category of algebras. Fewster proposes the natural automorphism group of that functor as its global gauge group and proves compactness under additional assumptions, including an energy-compactness condition in Minkowski space; see [[library/endomorphisms-and-automorphisms-of-locally-covariant-quantum-field-theories/inq|Endomorphisms and automorphisms of locally covariant quantum field theories]].

In the DHR framework, a suitable symmetric tensor category of localized, transportable sectors with conjugates and finite statistics reconstructs a compact group and a charged field algebra. The construction and its hypotheses are reviewed in [[library/algebraic-quantum-field-theory/inq|Algebraic Quantum Field Theory]]. Long-range gauge charges are not straightforward DHR sectors; the [[library/gauss-law-and-string-localized-quantum-field-theory/inq|Gauss-law obstruction]] is therefore relevant to any claimed reconstruction of the complete Standard Model.

Both routes are reconstruction theorems:

$$
\text{specified local theory or sector category}
\Longrightarrow
\text{compact global internal group}.
$$

They are not classification theorems saying that causal order, a binary normal plane, or modular flow forces the Standard Model category.

The reconstructed object is a compact global internal group acting on fields or sectors. Reconstruction alone does not produce a Yang–Mills connection, gauge bosons, a BRST complex, coupling constants, or gauge-field dynamics.

## Stabilizer-first is a third logical order

The exceptional-Jordan flag supplies a route that is neither reconstruction from an imported QFT nor symmetry breaking inside a preselected group. Let \(J=\mathfrak h_3(\mathbb O)\), let \(w\in F_4=\operatorname{Aut}(J)\) be the order-three orientation whose fixed algebra is \(\mathfrak h_3(\mathbb C)\), and let \(\ell\) be a trace-two idempotent in that fixed algebra. Then

$$
H_{\ell,w}:=\operatorname{Stab}_{F_4}(\ell,w)
\cong S(U(2)\times U(3)).
$$

Here the asymmetric pointed datum \((\ell,w)\) is prior and the familiar group is its stabilizer. This is a genuine **group-type selection theorem** conditional on the exceptional whole and the admissible flag type; it is not spontaneous breaking, because no \(H\)-symmetric vacuum or potential was assumed before \(H\) appeared.

The construction now reaches further. The projection \(F_4\to F_4/H\) is the principal torsor of local flag presentations. Coordinates of compatible comparison arrows in chosen lifts obey the ordinary \(H\)-valued lattice gauge law. The faithful 149-dimensional defining-data normal then supplies a holonomy response, and its pullback to the distinguished color factor is exactly the fundamental Wilson action:

$$
Q_N\circ\iota_{\mathrm c}^{E}=288Q_W,
\qquad
\beta_W=144\beta.
$$

Thus three levels must be distinguished:

1. **group-type selection:** the stabilizer theorem, now exact;
2. **finite-regulator action recovery:** the flag-torsor and color-Wilson theorem, exact after choosing the full normal carrier and color pullback; and
3. **QFT selection:** a state, bare coupling trajectory, physical carrier, continuum net, dynamics, and matter content determined from the deeper data, still open.

The result has genuine Copernican content because several familiar structures now follow from one prior pointed object. It does not yet show why the exceptional flag is physically admissible, why the color-only member rather than the full non-simple stabilizer is realized, or why its Wilson vacuum has a continuum mass gap. [[contemporary-puzzles/yang-mills-mass-gap/exceptional-normal-holonomy-and-the-residual-gauge-form|The exceptional normal-holonomy theorem]] owns the exact construction and its stopping conditions.

## The circularity test

The [[wall-construction-interface/inq#The interface is a dependency, not a theory|interface formulation]] permits

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

Geometric modular action can implement Lorentz transformations or PCT under strong hypotheses, as in [[library/modular-structure-and-duality-in-conformal-quantum-field-theory/inq|Brunetti, Guido, and Longo]], but that does not identify normal reflection with weak isospin or charge conjugation. Such an identification would also endanger the required local separation between spacetime symmetry and internal gauge symmetry.

## “Spectral” names two unrelated constructions

The [[vendor/holographic-cosmology/stress-tensor-response|holographic stress-response dictionary]] uses spectral data for the continued two-point response of a three-dimensional stress tensor. A finite spectral triple uses data such as

$$
(A_F,H_F,D_F,J_F,\gamma_F).
$$

The shared word does not provide a map between them. Deriving a finite spectral geometry from the wall would be an additional theorem, not an unpacking of the existing spectral response.
