# Sources and Claim Status for Semiorthogonal Decompositions

The standard categorical claims in this module are grounded in the foundational literature on admissible subcategories, mutations, enhanced triangulated categories, geometric semiorthogonal decompositions, dg quotients, and recollement. The project's physical interpretation is kept separate from those theorems.

## Foundational primary sources

- A. Bondal and M. Kapranov, [“Representable Functors, Serre Functors, and Mutations”](https://doi.org/10.1070/IM1990v035n03ABEH000716), *Math. USSR-Izvestiya* **35** (1990), 519--541. Primary source for admissible subcategories, exceptional collections, and mutation formalism.

- A. Bondal and M. Kapranov, [“Enhanced Triangulated Categories”](https://doi.org/10.1070/SM1991v070n01ABEH001253), *Math. USSR-Sbornik* **70** (1991), 93--107. Primary source for the enhanced setting in which derived mapping complexes, rather than only degree-zero morphisms, are retained.

- A. Bondal, [“Representation of Associative Algebras and Coherent Sheaves”](https://doi.org/10.1070/IM1990v034n01ABEH000583), *Math. USSR-Izvestiya* **34** (1990), 23--42. Primary source relating strong exceptional collections to derived module categories and their mutations.

- A. Bondal and D. Orlov, [“Semiorthogonal Decomposition for Algebraic Varieties”](https://arxiv.org/abs/alg-geom/9506012) (1995). Primary geometric source for fully faithful functors, semiorthogonal decompositions, and birational constructions.

- D. Orlov, [“Projective Bundles, Monoidal Transformations, and Derived Categories of Coherent Sheaves”](https://doi.org/10.1070/IM1993v041n01ABEH002182), *Russian Acad. Sci. Izvestiya Mathematics* **41** (1993), 133--141. Primary source for projective-bundle and blow-up decompositions.

- A. Beilinson, J. Bernstein, and P. Deligne, [*Faisceaux pervers*](https://www.numdam.org/item/AST_1982__100__1_0/), *Astérisque* **100** (1982), especially the recollement formalism. Primary source for the six-functor gluing pattern used in the recollement note.

- V. Drinfeld, [“DG Quotients of DG Categories”](https://arxiv.org/abs/math/0210114), *Journal of Algebra* **272** (2004), 643--691. Primary source for dg quotients compatible with Verdier localization.

## Authoritative geometric and homological sources

- A. Kuznetsov, [“Semiorthogonal Decompositions in Algebraic Geometry”](https://arxiv.org/abs/1404.3143), *Proceedings of the ICM 2014*. Authoritative survey and convention check; it is not the originating primary source.

- A. Kuznetsov, [“Hochschild Homology and Semiorthogonal Decompositions”](https://arxiv.org/abs/0904.4330), 2009. Establishes additivity and projection-kernel results for admissible subcategories under its geometric hypotheses.

- A. Kuznetsov, [“Derived Categories of Cubic Fourfolds”](https://arxiv.org/abs/0808.3351), 2008. Primary source for the cubic-fourfold derived-category setting underlying the Kuznetsov component used by the local Hodge-atoms source.

## Analytic comparison source

- M. Takesaki, [“Conditional Expectations in von Neumann Algebras”](https://doi.org/10.1016/0022-1236(72)90004-3), *Journal of Functional Analysis* **9** (1972), 306--321. Primary source for the equivalence between modular invariance of a von Neumann subalgebra and existence of the corresponding faithful normal weight-preserving expectation, under the paper's semifiniteness hypotheses.

- A. Jaffe, A. Lesniewski, and K. Osterwalder, [“Quantum K-Theory I: The Chern Character”](https://doi.org/10.1007/BF01218474), *Communications in Mathematical Physics* **118** (1988), 1--14. Primary source for the heat-kernel entire cyclic cocycle now called the JLO character. This construction requires analytic heat-kernel and representation data; it is not supplied by a semiorthogonal decomposition alone.

The project's exact finite conditional-expectation and BKM comparison is developed independently in [[spectral-wall-descent/conditional-expectation-balance|conditional expectation balance]]. The cyclic-transgression target is in [[spectral-wall-descent/index-and-curvature-transgression|index and curvature transgression]].

## Local source under commentary

[[library/hodge-atoms-spectral-triples-bps/entry|Relating Hodge Atoms, Spectral Triples, and BPS Flows]] is a March 2026 primary preprint in the local library. It is useful because it places a Kuznetsov semiorthogonal component, Ext-quiver, birational modification, and JLO language in one proposed physical picture.

Its status must be divided:

- the Kuznetsov and Orlov semiorthogonal decompositions it imports are standard under their hypotheses;
- the one-sided \(\operatorname{RHom}\)-vanishing is exact categorical mathematics;
- its promotion of that vanishing to a full tunnelling selection rule is explicitly stated as a conjecture; and
- its claimed JLO localization requires an analytic realization not produced merely by the semiorthogonal decomposition.

This module therefore uses the source to motivate an interface problem, not as proof that categorical orthogonality is physical decoherence.

## Status of the project's proposed import

The phrase **categorical wall** means the following proposed package:

$$
(\mathcal T;\mathcal A,\mathcal B;\pi_{\mathcal A},P_{\mathcal A})
$$

with \(\mathcal T=\langle\mathcal A,\mathcal B\rangle\), \(\pi_{\mathcal A}:\mathcal T\to\mathcal A\) the retained-component projection, and \(P_{\mathcal A}=i_{\mathcal A}\pi_{\mathcal A}\) its idempotent endofunctor.

- Existence of such packages in the examples cited above: **[ESTABLISHED MATHEMATICS]**.
- Construction of the package from the project's actual \(A_2/S^6\) geometry: **[OPEN]**.
- Realization by a \(C^*\)- or von Neumann inclusion and completely positive expectation: **[OPEN]**.
- Compatibility with a faithful state, BKM geometry, Takesaki modular invariance, JLO character, and index pairings: **[OPEN]**.
- Identification with measurement, causal time, entropy production, or spacetime emergence: **[CONJECTURAL INTERPRETATION]**.
