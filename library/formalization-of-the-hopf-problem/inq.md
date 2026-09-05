---
inq.module: "formalization-of-the-hopf-problem"
inq.include:
  - "./"
inq.ambient:
  - "**"
---
# Formalization of the Solution to the Hopf Problem

The Lean source constructs a complex-manifold atlas on the standard topological unit six-sphere, following the compact complex threefold in Levent Alpöge's manuscript. The pinned solution contains 248,818 lines. Its final construction transports an atlas modeled on $\mathbb C^3$ by a homeomorphism and proves the corresponding `IsManifold` statement; it does not specify compatibility with a preassigned smooth atlas. A source comment records the expected dependency output `propext`, `Classical.choice`, and `Quot.sound`; the comparator configuration permits those axioms and enables `nanoda`.

## Source

Boris Alexeev, formalization repository; the file states that most of the Lean code was written by Codex and that its mathematical content follows Levent Alpöge's manuscript.

- [Repository](https://github.com/plby/HopfProblem)
- [Pinned `Solution.lean` at commit `9ac8a456b526527837d7082ff775213ca8bc9809`](https://github.com/plby/HopfProblem/blob/9ac8a456b526527837d7082ff775213ca8bc9809/Solution.lean), committed August 27, 2026.
- [Comparator configuration](https://github.com/plby/HopfProblem/blob/9ac8a456b526527837d7082ff775213ca8bc9809/comparator/config.json)

No local copy is archived in this module. A static workspace audit of the pinned source found no `sorry`, `sorryAx`, declared `axiom`, `opaque`, or `unsafe` occurrence in executable code. The artifact was not rebuilt locally in this audit because the Lean toolchain was unavailable, so no independent kernel-acceptance or comparator-execution receipt is supplied here.
