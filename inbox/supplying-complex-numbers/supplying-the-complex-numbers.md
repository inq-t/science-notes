# Supplying ℂ

### A synthesis of the two selection arguments, with an audit

**Status.** Synthesis note. Draws together *Necessary Ambiguity* (Paper A, unconditional, compiled) and *The Necessity of i* (Paper B / document seventeen, conditional). Adds three new flags and one new open problem discovered in the course of the synthesis. Grades inline; pins and open problems at the end.

---

## 0. Provenance warning — read this first

This document is **reconstructed from the session record, not read off the filed sources.** The working directory was empty at the time of writing; `necessary-ambiguity.tex/.pdf` and `the-necessity-of-i.md` were not available on disk. Every clause below is faithful to the record of what was drafted, but the record is a transcript, not the artifact.

**Discipline:** before any clause here is cited, quoted, or shipped, it must be checked against the filed originals. Sections marked **[RECON]** are the ones where paraphrase risk is highest — the pincer table, the axiom statements, and the T1–T4 package.

---

## 1. Three different questions wear the same sentence

"Derive the complex numbers from the Jacobian counterexample" names three distinct projects. Only one of them is live. Separating them is the first job of this note, because the blocked route is the one the sentence most naturally suggests.

**(a) Derive ℂ from the algebra of the counterexample itself.**
*Status:* **[BLOCKED — circular].* The Alpöge map is an object in the category of polynomial self-maps **taken over ℂ from the outset**. Its coefficient field is a stipulation of the setting, not an output of the object. This is the standing flag already filed as Q3 in `keller-heisenberg-note.md`: *ℂ is an input of the present setting; nothing there derives it.* Any argument that extracts ℂ from the counterexample's internal algebra — its monodromy group, its Galois closure, its étale algebra — fails the compression test on inspection. **Input equals output.** The S₃ is genuinely there and genuinely forced; but it is forced *inside* a category whose ground field was assumed.

**(b) Derive that any host of braided obstruction-ambiguity must be ℂ.**
*Status:* **[THEOREM, conditional]** — this is the pincer, and it is the whole live route. It does not look at the counterexample's algebra at all. It varies the *field* across a classification and asks which fields can host the structure. The counterexample enters only later, and only to do two logical jobs that are not derivational (§5).

**(c) Derive the orientation — *i* rather than −*i*.**
*Status:* **[NOT AVAILABLE — and provably not by this route].** Nothing in the pincer breaks complex conjugation. The theorem necessitates that there *be* an *i*; the hand remains a convention. This dovetails, unprompted, with the coupling theorem's grace note in Paper A: existence of handedness is derivable, the hand itself is not.

**The reframe, stated once.** The program does not derive ℂ from the counterexample. It derives ℂ from a **demand about transportable ambiguity**, using the counterexample as the proof that the demand is satisfiable. That is a weaker claim than the sentence suggests and a much more defensible one.

---

## 2. Two papers, and why the seam is load-bearing

| | **Paper A — Necessary Ambiguity** | **Paper B — The Necessity of i** |
|---|---|---|
| Holds fixed | the field (ℂ) | the demands (D0–D3) |
| Interrogates | the object | the category |
| Logical form | unconditional theorems | conditional selection theorem |
| Exposure | none philosophical | axioms are choices |
| Worst-case referee | "elementary but correct" | "your axioms are choices" |
| Role in the ℂ question | supplies the **witness** | supplies the **selection** |

Merging them lets B's softness leak onto A. The hand-off between them is explicit and one-directional: **A proves the braided structure exists and is forced; B proves ℂ is the only place it could have lived.** B cites A's full-S₃ theorem as the realization of its axioms. A cites B only in a scope remark.

---

## 3. Paper A — the witness [RECON]

Paper A does not argue about ℂ. It establishes what any counterexample must carry, and in doing so hands B a realized instance rather than a merely consistent one.

**The floor.** Three named shoulders, then one step.
- Degree 1 — Keller's own birational case (1939).
- Degree 2 — Campbell's Corollary, quoted by page: the degree of a nowhere-degenerate polynomial map cannot be two (quadratic extensions are normal).
- Cyclic degree 3 — one line from Campbell's Theorem: degree = group order ⟹ Galois ⟹ invertible.
- **Conclusion:** full S₃ is the only survivor at the minimum. Every counterexample, every dimension, generic fiber degree ≥ 3; at the floor the ambiguity is a *complete symmetric triad*, necessarily.

**The descent lemma.** Monodromy is transitive; non-invariant fiber data is provably unobservable. Stated in dry mathematical language for the paper: *locally meaningful and fully determining, yet provably admits no globally single-valued description.* This is the pre-observable, without the word.

**The dyad.** Defined invariantly via the discriminant class of the étale algebra — no spectral presentation needed, so it applies to every minimal counterexample rather than only ones with a known cubic. Two complementary reductions of S₃: orientation (normal, A₃, descent-type) versus nomination (non-normal, S₂ stabilizer, vacuum-selection-type). Frame factorization P ≅ X₃ ×_U X₂ with canonical determinant triviality.

**The coupling package (T1–T4).** T1: the orientation dyad is the unique normal intermediate step in any resolution. T2: mirror closure — no orientation invariant exists on the base; the two 3-cycles are conjugate over the base. T3/T3′: on the double cover the classes separate, distinguished by χ versus χ̄; both parity operators proven (deck involution unconditionally; complex conjugation scoped to real-coefficient maps, meridian-reversal argument written out). T4: the Frobenius–Schur jump from real to complex type at dyad-death. Corollary: *handedness is born at, and only at, the funeral of the dyad.*

*(The Coxeter sign-convention gate dissolved during the drafting of T3′ and is no longer outstanding.)*

**What A contributes to the ℂ question, and only this:** the demands of Paper B are jointly *realized*, not merely consistent. Connected regular locus; degree-3 finite étale cover; certified full S₃ monodromy; wall exactly the nonproperness set. A theory of possible habitats is worth more when the habitat is occupied.

---

## 4. Paper B — the selection [RECON]

### 4.1 The demands

Four axioms, each motivated by a theorem or a definition rather than a preference.

- **D0 — commutative base.** The Jacobian-determinant formalism presupposes it. (Remark on quaternionic zero-set pathologies.)
- **D1 — continuous transport.** Fiber data must be comparable along paths. Facts are invariants; invariance presupposes re-description transport.
- **D2 — connected regular locus.** The wall must not sever comparability.
- **D3 — nontrivial monodromy *possible*.** This carries the section's one real proof: trivial monodromy plus irreducible source forces generic degree one, hence — via Zariski's Main Theorem and Białynicki-Birula–Rosenlicht — an automorphism. **An obstruction with trivial braiding is a contradiction, not an option.** The logic here is literally how Campbell's 1973 proof closes.

**Bracket, stated in the paper:** these axioms formalize "ambiguity with invariant structure"; whether physical determination instantiates them is not addressed.

### 4.2 Scope

Pontryagin's classification: the connected locally compact division rings are ℝ, ℂ, ℍ. Totally disconnected fields (p-adic) fail D1 outright — paths are constant, one line.

### 4.3 The pincer

One polynomial condition carves a wall whose real codimension equals the real dimension of the base field.

| Field | Wall codim | π₀ of complement | π₁ around wall | Verdict |
|---|---|---|---|---|
| ℝ | 1 | disconnects (sign-changing case) | — | transport blocked; ambiguity **sorted** |
| **ℂ** | **2** | connected | **nontrivial** | **the unique braided window** |
| ℍ | 4 | connected | trivial (codim ≥ 3 ⇒ simply connected complement) | monodromy dead ⇒ no obstruction |

**Theorem (conditional; assembly of classical parts).** *Among connected locally compact division rings, the demand that fiber-ambiguity admit connected, nontrivially braided transport selects ℂ uniquely: codimension two is the only codimension at which a wall can be encircled but not crossed, and codimension-two-from-one-condition is the defining property of the complex numbers.*

Slogan: **the *i* is the license for one algebraic condition to consume exactly two real dimensions.**

### 4.4 Lineage — the paper's strongest single asset

The pincer's engine — codimension ≥ 2 preserves π₁; normal coverings of simply connected bases trivialize — is **Campbell's own 1973 proof mechanism**, deployed there to prove the Galois case. §2 does not assemble topology trivia; it recognizes the working part of a classical theorem and generalizes it from a statement about maps into a selection principle about fields. This converts the referee objection *"these are elementary facts"* into the paper's pedigree. Campbell 2013/14 then anchors the ℝ column himself — invertible real maps force odd field degree and no nontrivial automorphisms — so both columns rest on the same authority, forty years apart.

### 4.5 The one-map exhibit — the paper's rhetorical core

The Alpöge map has **rational coefficients and real witness points**. Restricted to ℝ³ it is *already a real Keller counterexample.*

**Therefore the paper must never claim that no obstruction exists over ℝ.** That is false, and a referee kills it in one line.

The defensible claim is sharper and more interesting:

- **Over ℝ³** — the discriminant takes both signs, so the target *chambers*: a region with three real preimages, a region with one (real cubic root-counting), the wall separating them, fiber counts *jumping* across it. No monodromy, no comparability between chambers. Ambiguity **sorted**.
- **Over ℂ³** — the same wall has real codimension two: complement connected, fiber count constantly three, full S₃ braiding certified. Ambiguity **braided**.

One map, two fields, grammar absent versus grammar present. That contrast *is* the theorem, wearing an example.

---

## 5. What the counterexample is actually for

It is not empirical data, and the theorems do not need it. Had JC been proven true in 2026 instead of refuted, the selection theorem would read identically: *ℂ is the unique possible habitat of this structure — and it happens to be uninhabited.*

Two precise logical services, both non-derivational:

1. **Non-vacuity.** For eighty-seven years every conditional "if F is a counterexample, then…" was quantified over a possibly-empty set. A necessity theorem about members of an empty class is a sentence about nothing. One citation converts the entire contrapositive literature from a description of the well-behaved into an anatomy of actual defects.
2. **Realization.** D0–D3 are shown jointly satisfiable by exhibition, not by consistency argument — and, via §4.5, the ℝ/ℂ contrast is exhibited on a *single* map, which no consistency argument could do.

---

## 6. Downstream — what the selection buys, at declared grade

- **[WELD]** The Einstein-column chain softens from a flag to a conditional chain: *braided facts ⇒ ℂ (this pincer) ⇒ ℙ¹ ⇒ PGL₂(ℂ) ≅ SO⁺(3,1).* Only the last link is a theorem outright; the pincer's clauses are the remaining inputs.
- **[SLOT]** Phase as the central charge of braided ambiguity. The wall complement's π₁ carries a canonical central ℤ; its U(1) completion is **open** (this is P2). Until it is closed, *phase* is a name for a slot, not a derived object.
- **[RHYME]** Single-handedness. Polynomial maps are holomorphic; the rigid category is one-chirality by construction, the mirror sector structurally absent. This rhymes with the twistor thesis and with the weak interaction's missing mirror fermions. It is **not** a result — and the googly problem is the pre-named difficulty any filling must survive.
- **[CONTEXT — not confirmation]** Renou et al., *Nature* 2021, plus 2022 confirmations: real-amplitude quantum theory was made falsifiable in network Bell scenarios and falsified. Nature was asked "ℝ or ℂ?" and answered ℂ. **This is a different selection under different axioms.** It is convergent context. Citing it as support for the pincer would be a category error, and P4 exists precisely because nobody has shown the two roads are one road.

---

## 7. Audit

### 7.1 Compression test

| Route | Input | Output | Verdict |
|---|---|---|---|
| (a) ℂ from the counterexample's algebra | ℂ (stipulated as coefficient field) | ℂ | **Fails. Vacuous.** |
| (b) ℂ from the transport demand | connected + nontrivially braided transport; Pontryagin's classification; π₁ arithmetic of hypersurface complements | ℂ uniquely | **Passes — narrowly.** See F3. |
| (c) *i* versus −*i* | — | — | **Not attempted; provably unavailable here.** |

### 7.2 Three flags raised in the course of this synthesis

**[FLAG F1 — the ℝ column is conditional on sign change. New. Substantive.]**
The exclusion of ℝ runs: one condition ⟹ real codimension one ⟹ complement disconnects ⟹ D2 fails. The middle step holds when the discriminant **changes sign** (then {f > 0} and {f < 0} are disjoint nonempty opens covering the complement). It does not hold in general. A real polynomial can carve a locus of real codimension ≥ 2 — a sum of squares is the standard case — and the complement of a codimension-2 locus in ℝ³ can be *connected with nontrivial π₁* (complement of a line in ℝ³ has π₁ = ℤ). A real Keller counterexample of that shape would evade the pincer's ℝ column entirely.

The Alpöge witness does not have that shape — its discriminant demonstrably takes both signs, which is exactly why it chambers. So the exhibit is safe. The **theorem** is not, as stated.

Two repairs, and they are not equivalent:
- *(i)* Prove that a real Keller counterexample's discriminant must change sign. This preserves the theorem's strength. Filed as **P5**.
- *(ii)* Restate the axiom so the wall is *by definition* the vanishing locus of one condition of codimension one. This makes the ℝ exclusion definitional rather than derived and materially weakens the theorem.

Recommend (i). Do not ship B without resolving this.

**[FLAG F2 — the ℍ row is over-determined, which is good news for the circularity worry.]**
ℍ is excluded twice: by D0 (noncommutativity) and by the codimension arithmetic (codim 4 ⟹ simply connected complement ⟹ monodromy dead). D0 is the axiom most contaminated by the ambient polynomial category — it is imported from the setting that route (a) failed on — so its redundancy matters. Caveat, stated honestly: without D0 the notion of "one polynomial condition" over ℍ is not obviously well-defined, so the second exclusion is only available if one grants a sensible codimension count there. The row is therefore over-determined *modulo a definitional grant*, not unconditionally. Either way, the selection does not rest on D0 alone.

**[FLAG F3 — near-tautology risk in the theorem's own statement.]**
The clause *"codimension-two-from-one-condition is the defining property of the complex numbers"* is doing double duty as premise and conclusion. A hostile referee reads the theorem as: *demand two real dimensions per algebraic condition; obtain the field with two real dimensions per algebraic condition.* This is the same failure mode already caught in the Baez–Schwahn "completion theorem," where exceptionality alone forced the conclusion.

The defence is available and should be **written into the paper rather than left implicit**: the non-trivial content is the *bridge* — from a transport-theoretic demand (comparability of fiber data along paths, plus non-triviality of braiding) to a codimension count. Nothing in D1–D3 mentions dimension. The bridge is what has to be shown, and its two halves are classical (complements of complex hypersurfaces are connected; π₁ of a discriminant complement is nontrivial; codim ≥ 3 complements are simply connected). The theorem's added information over its inputs is exactly: Pontryagin's classification, plus that π₁ arithmetic. No more than that — and the paper should say so in the abstract, not wait to be asked.

### 7.3 What the argument does not do

1. No selection of *i* versus −*i*. Conjugation is unbroken; orientation stays conventional.
2. No claim about physics. The only sentence about reality in Paper B is a citation to somebody else's experiment.
3. Scope limited to Pontryagin's family. Nothing is said about fields outside local compactness.
4. D3 is proved *conditional on the others*; D1 and D2 remain motivated, not derived. This is P1 and it is the honest centre of gravity of the whole note.
5. It does not derive quantum mechanics, and it does not close the quantum-promotion question — what licenses the move from classical branched-cover data to quantum observable algebras, i.e. why the pair-groupoid yields M₃(ℂ) rather than commutative sheet-labels. The pincer supplies the ℂ in M₃(ℂ). It supplies nothing about the M₃.

---

## 8. Kill conditions

Registered with the result, per standing discipline.

- **K1.** A braided-obstruction theory over a disconnected field. Kills the D1 exclusion of the p-adics and with it the scope argument.
- **K2.** A demonstration that D2 or D3 can be weakened without losing the selection. Would show the axioms are stronger than the work requires — i.e. that the theorem is closer to F3's tautology reading than claimed.
- **K3.** A real Keller counterexample whose discriminant does not change sign (F1). Kills the ℝ column as derived.
- **K4.** A proof that trivial monodromy is compatible with a genuine obstruction. Kills D3's proof, and with it the claim that braiding is forced rather than assumed.

---

## 9. Open problems

- **P0 — [NEW, and it belongs first].** State explicitly, in the paper, that route (a) is blocked and why. The paper's own value depends on readers not mistaking it for the circular argument. Currently this is filed as Q3 in a *different* document; a reader of B alone would not find it.
- **P1.** Derive D1–D3 from a primitive characterization of irreversible determination. The axioms are motivated; one of them is proved conditional on the others. **This is the load-bearing gap.**
- **P2.** Exponentiate the braid centre to a continuous phase group. The wall complement's π₁ carries a canonical central ℤ; the U(1) completion is open.
- **P3.** Extend uniqueness beyond local compactness, or prove the scope sharp.
- **P4.** Connect this selection to the quantum-reconstruction selections (Hardy; Chiribella–D'Ariano–Perinotti; Masanes–Müller; the Renou falsification). *Are the two roads to ℂ one road?*
- **P5 — [NEW, from F1].** Prove that a real Keller counterexample's discriminant must change sign — or exhibit one where it does not.

Each is stated so a specialist can attack it in an afternoon. P5 is the one that gates shipping.

---

## 10. Status ledger

| Claim | Grade |
|---|---|
| Fiber degree ≥ 3 for every counterexample, every dimension | [THEOREM] (Paper A) |
| Full S₃ at the minimum | [THEOREM] (Keller + Campbell + one step) |
| Necessary orientation dyad; T1–T4 coupling package | [THEOREM] (Paper A) |
| Handedness born only at dyad-death | [THEOREM], scoped |
| Trivial braiding ⟹ no obstruction (D3) | [THEOREM], conditional on D0–D2 |
| ℂ uniquely satisfies D0–D3 among Pontryagin's family | [THEOREM], conditional; **ℝ column gated on P5** |
| ℂ derived from the counterexample's algebra | [MORGUE] — circular; input equals output |
| *i* versus −*i* | [OPEN] — provably not by this route |
| Phase as U(1) from the braid centre | [SLOT] — P2 |
| Chain to SO⁺(3,1) via ℙ¹ | [WELD] |
| Single-handedness / twistor rhyme | [RHYME] |
| Renou et al. as support | **[FLAG]** — convergent context only; P4 is open |

---

## 11. Outstanding pins

- Pontryagin — exact citation for the classification of connected locally compact division rings.
- Renou et al. 2021 + one 2022 confirmation experiment — exact citations.
- Stueckelberg 1960 — for the question's ancestry.
- Brieskorn — π₁ of discriminant complements.
- Białynicki-Birula–Rosenlicht 1962 — **done, exact coordinates.**
- Campbell 1973, 2013/14; Pinchuk 1994; Keller 1939 — **done, primary-verified.**
- The standing six metadata lines and two reserved DOIs, which gate everything already compiled.

---

*Compression test on this document: input was two paper skeletons and a transcript; output adds the three-question separation (§1), F1–F3, P0, P5, and the ledger. F1 and P5 are the only items that change what may be shipped.*
