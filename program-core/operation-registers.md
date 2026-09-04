# Operations Between Registers

A cross-register claim is a claim about an arrow, not merely about the objects at its ends. This note is the programme-wide routing ledger for those arrows: it distinguishes presentation, descent, quotient, readout, selection, elimination, realization, and record operations while leaving their definitions and theorems with specialist owners.

## What an arrow claim must declare

Every proposed operation should name:

1. its source and target objects or categories;
2. the class of arrow being used and its variance;
3. any state, topology, involution, measure, or other extra datum it requires;
4. its kernel, image, obstruction, or discarded structure when those notions exist;
5. whether it is faithful, invertible, idempotent, completely positive, or selective;
6. how it composes with adjacent arrows; and
7. whether the arrow is constructed, postulated, conditional, or open.

The same formula can represent different operations when any of these fields changes.

## Canonical operation ledger

| Operation | Defining discriminator | Canonical owner |
|---|---|---|
| presentation equivalence | an invertible comparison inside the chosen presentation groupoid | [[algebra/local-global-individuation|local--global individuation]] |
| cross-fiber transport | a declared comparison between objects or states on different carriers | [[wall-construction-interface/cross-fiber-transport|cross-fiber transport]] |
| gluing | assembly from compatible pieces already given on subobjects | [[basic-concepts/gluing/inq|gluing]] |
| strict descent | a cover or site, coherent descent datum, comparison functor, and effectivity | [[basic-concepts/descent/inq|descent]] |
| physical quotient | identification relative to declared probes, followed by the required tangent reduction | [[program-core/physical-quotient|the physical quotient]] |
| semiorthogonal projection | an adjoint projection associated with an admissible decomposition, selecting one component and killing its declared complement | [[semiorthogonal-decompositions/definitions-and-projections|semiorthogonal projections]] |
| Verdier or dg quotient | a universal exact localization annihilating a declared thick or dg subcategory | [[semiorthogonal-decompositions/definitions-and-projections#Verdier and dg quotients|categorical quotients]] |
| categorical mutation | an equivalence changing a semiorthogonal presentation; it does not erase a component | [[semiorthogonal-decompositions/mutations-recollement-and-a2|mutations and recollement]] |
| contextual readout | a Heisenberg readout and induced state pullback returning an observable law, not an outcome | [[program-core/contextual-descent-from-homogeneity|contextual realization from homogeneity]] |
| conditional expectation | a normal unital completely positive idempotent onto a subalgebra, with its state and modular hypotheses declared | [[spectral-wall-descent/conditional-expectation-balance|conditional-expectation balance]] |
| conditioning or postselection | an outcome branch followed by normalization; not an everywhere deterministic trace-preserving channel | [[basic-concepts/conditioning/inq|conditioning and instruments]] |
| Schur elimination | elimination of a quadratic auxiliary block, returning an effective form and generally a determinant contribution | [[spectral-wall-descent/hidden-resolvent-and-seesaw|hidden resolvents and the seesaw]] |
| auxiliary-time elimination | balances \(L^2\) forgetting against influence propagation and removes the arbitrarily normalized proof clock, returning a static inverse-distance certificate | [[auxiliary-response-localization/inq|auxiliary response localization]] |
| spectral attenuation | functional-calculus filtering whose kernel and inverse stability must be checked | [[cauchy-spectral-envelope/inq|heat mixtures and Cauchy envelopes]] |
| stabilizer reduction | a section of an associated \(G/H\)-bundle presenting a reduction of structure group; not by itself a dynamical symmetry-breaking event | [[higgs-reduction-as-local-shadow/inq|Higgs reduction as a local shadow]] |
| real-form fixed locus | the equalizer of an antiholomorphic involution; not a fact-forming process | [[algebra/real-forms-and-factive-spacetime|real forms and factive spacetime]] |
| factual instrument or pointing | an outcome-labelled operation together with an obtained value; a law or bare character is insufficient | [[conservation-of-causal-charge/factive-descent-and-records|factive descent and records]] |
| record extension | a proper one-sided extension preserving earlier factual values | [[algebra/local-global-individuation|local--global individuation]] |
| carrier-changing realization | a typed map or functor between distinct mathematical carriers, with transported structure proved | [[causal-wall-spectral-theory/realization-map|the CWST realization map]] and [[algebra/real-forms-and-factive-spacetime|the real-form interface]] |
| soldering | in the strict sense, an equivariant nondegenerate identification with tangent geometry; broader programme uses must be labelled extensions | [[basic-concepts/soldering/inq|soldering]] |

This ledger classifies operations; it does not assert that any open programme arrow exists. For example, a categorical projector is not a conditional expectation, an injective heat filter is not literal forgetting, and a fixed locus is not an actual outcome. The specialist notes own those exact distinctions.

## Composition before identification

A typical fact-bearing construction contains several arrows:

$$
\text{presentation data}
\longrightarrow
\text{effective comparison or descent}
\longrightarrow
\text{observable law}
\dashrightarrow
\text{obtained value}
\longrightarrow
\text{persistent record}.
$$

No adjacent stages may be collapsed merely because one implementation uses the same underlying set, algebra, or symbol. In particular, contextual readout does not select a fact, and factual selection does not by itself construct a persistent history.

The words *descent*, *collapse*, *reduction*, *forgetting*, *residue*, and *realization* are therefore incomplete in a canonical claim unless the actual operation is named. [[program-core/ontological-registers|Ontological registers]] type the objects at the ends of these arrows; [[program-core/response-registers|response registers]] type the quadratic structures transported through some of them.
