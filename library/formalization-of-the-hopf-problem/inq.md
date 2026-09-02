---
inq.module: "formalization-of-the-hopf-problem"
inq.include:
  - "./"
inq.ambient:
  - "**"
---
# Formalization of the Solution to the Hopf Problem

The Lean artifact constructs a complex-manifold atlas on the standard unit six-sphere and proves the corresponding `IsManifold` statement, following the compact complex threefold in Levent Alpöge's manuscript. The pinned solution contains 248,818 lines and ends with the exact theorem that there exists a `ChartedSpace` modeled on $\mathbb C^3$ for the unit $S^6$, together with a printed dependency list containing only `propext`, `Classical.choice`, and `Quot.sound`. Its comparator configuration checks the target theorem against those permitted axioms and enables the independent `nanoda` kernel.

## Source

Boris Alexeev, formalization repository; the file states that most of the Lean code was written by Codex and that its mathematical content follows Levent Alpöge's manuscript.

- [Repository](https://github.com/plby/HopfProblem)
- [Pinned `Solution.lean` at commit `9ac8a456b526527837d7082ff775213ca8bc9809`](https://github.com/plby/HopfProblem/blob/9ac8a456b526527837d7082ff775213ca8bc9809/Solution.lean), committed August 27, 2026.
- [Comparator configuration](https://github.com/plby/HopfProblem/blob/9ac8a456b526527837d7082ff775213ca8bc9809/comparator/config.json)

No local copy is archived in this module. A static workspace audit of the pinned source found no `sorry`, `sorryAx`, declared `axiom`, `opaque`, or `unsafe` occurrence in executable code. The artifact was not rebuilt locally in this audit because the Lean toolchain was unavailable, so kernel acceptance and comparator execution remain externally reported rather than independently reproduced here.
