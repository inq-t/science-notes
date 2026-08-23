# Causal Scale Theory

Causal Scale Theory is the intended versionless home of the programme currently spread across five generations of master document, two version-named modules, and an autopsy folder. This module does not yet contain the theory; it contains the refactoring plan that would bring the theory here. The plan's governing judgement is that the archive's present difficulty is architectural rather than physical: the same argument has been rewritten five times at different confidence levels, and the module boundaries record *when* each rewrite happened instead of *what each part is for*.

Claim labels follow the vocabulary registered in [[causal-scale-master-v8/entry|the v8 synthesis]]; lifting that vocabulary out of v8 is itself one of the planned moves.

## The smell

In software terms the archive contains `utils.py` and `utils_v2.py`. [[causal-scale-master/entry|causal-scale-master]] holds a clean distilled library of the v7 argument. [[causal-scale-master-v8/entry|causal-scale-master-v8]] holds a review layer that generalizes v7's two hardwired constants and corrects six of its statements. Neither is wrong. But a reader arriving at the vault cannot tell which is canon, and the answer is genuinely *both, in different respects* — which is exactly the condition a refactor exists to end.

A version number in a module name is a promise that someone will later decide which version won. That decision is this module's purpose.

## Where this module sits

The refactor is worth doing because it lets the programme acquire dependencies in both directions, which a self-contained master document cannot do.

Downward, onto the primitives library: the soldering of scale to state is an instance of [[basic-concepts/soldering/entry|soldering]]; the BKM metric is an instance of [[basic-concepts/hessians/entry|a Hessian geometry]]; the cross-fiber comparison problem is an instance of [[basic-concepts/descent/entry|descent]] over [[basic-concepts/fibers/entry|fibers]]. Every one of those connections is currently re-derived inside the theory instead of imported.

Upward, into the containing programme: [[cosmodynamics/causal-scale-sector|the cosmodynamic sector note]] already types this theory as one sector of a larger structure, and [[cosmodynamics/registers-and-type-discipline|registers and type discipline]] already owns the vertical/horizontal and scale/time distinctions that v7, v8, and the monograph each restate locally.

Sideways, onto the shared dependency: the unconstructed wall is now factored into [[wall-construction-interface/entry|the wall-construction interface]], shared with [[causal-wall-spectral-theory/entry|the spectral programme]].

A versionless module can hold those edges. A document named after its revision cannot.

## The four invariants of the refactor

These are the constraints any stage must respect. They are stated first because most of the plan's specific choices follow from them.

**Generalized-first.** The canon carries $(\nu,\mathfrak R_c)$ explicitly and treats $\nu=\mathfrak R_c=1$ as a named branch evaluation. v7 hardwired both to one and distributed that choice through its leaves; v8 pulled them back out. Hardwiring a value that the theory's own falsification programme wants to measure is the parameterization mistake, and [[synthesis-plan|the synthesis plan]] treats undoing it as the central content move rather than a presentational one.

**Status is content, not commentary.** A claim's type — standard, algebra, conditional theorem, identification, principle, constitutive law, sector, deduction, open — travels with the claim. This is the one discipline all five generations agree on and it is the reason the archive is auditable at all.

**No layer may borrow evidence from another.** Symbolic identity, background receipt, phenomenological fit, and microscopic construction are four distinct evidential layers, and arithmetic agreement at one is not support for the layer beneath. The recurrence of a single $\operatorname{sech}^2$ factor across the metric, the zero-mode density, and the partner potential is one structure seen three times, not three confirmations.

**Failures must localize.** The value of an explicit dependency stack is that a broken step damages a bounded region: a failed amplitude principle leaves tractor geometry standing; a failed perturbation lift leaves the binary algebra standing; a failed wall construction reduces the cosmology to an ansatz with suggestive notation but does not touch the exact identities. Any reorganization that makes a failure propagate further than it does today is a regression.

## What the plan contains

[[inventory|The inventory]] catalogues the five generations of master document and what each is uniquely authoritative for, with its known defects. The short version: the newest document is not the most reliable one on every axis, and one of the earliest is still the best statement of two arguments.

[[synthesis-plan|The synthesis plan]] gives the target module map, the note-by-note harmonization table for the places where v7 and v8 disagree, the new abstractions worth lifting, and a five-stage migration ordered so that every stage is separately reviewable and revertible.

[[salvage-ledger|The salvage ledger]] lists the specific results that exist in exactly one place — several of them inside receipt scripts rather than prose — and would be lost by any consolidation that worked only from the two newest documents.

[[receipts-plan|The receipts plan]] specifies the receipt contract, sorts the existing scripts by what they actually establish, records which quantitative claims are unreproducible and what code would have to exist to change that, and settles where data lives.

[[quarantine|The quarantine register]] holds the tensions that are neither resolved nor dismissible. Each entry states what would resolve it and what would kill it. This is deliberately not a junk drawer: junk-drawer material is dead, and quarantined material is live and blocking.

## Advice on sequencing

Do the additive work first and the moves last. Stages 1 and 2 of [[synthesis-plan|the plan]] write things that exist nowhere and thin duplication that is already documented; neither requires deciding anything irreversible. Only stage 3 moves files, and by then the target shape has been readable for a while.

Resist the temptation to write a sixth master document. The archive's failure mode is not insufficient synthesis — it is that each synthesis restated its predecessor's preamble in order to be self-contained, and the restatements drifted. The target is a small ordered set of notes with one owner per statement, in the style [[causal-scale-master/entry|the v7 library]] already demonstrates at the leaf level. What v7 got right was the leaves. What v8 got right was the parameterization. The refactor is mostly a matter of letting each keep what it was better at.

One caution about scope. This module should hold the homogeneous scale-response theory and nothing else. The perturbation and primordial-spectrum obligations belong to [[causal-wall-spectral-theory/entry|the spectral programme]], the local-preservation obligations to [[compatible-with-existing-physics/local-physics-interface|the local physics interface]], and the question of whether gauge structure can be recovered rather than imported to [[symmetry-groups-select/entry|symmetry groups select]]. A master document naturally accretes all of them; a module should decline.
