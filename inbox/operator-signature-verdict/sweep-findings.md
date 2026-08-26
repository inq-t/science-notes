# Sweep Findings

The string-search across the workspace that preceded this verdict, and the five findings that bear on it. Two would have changed the advice if missed.

## 1. A typing correction the vault already contains **[AUDIT ITEM — cross-reference, not contradiction]**

[[algebra/a2-positive-completion|The positive-completion note]] states: a self-adjoint nilpotent in a $C^*$-algebra is zero, and — the sentence that matters here — *the parabolic translation of a half-sided modular inclusion is parabolic in its finite-dimensional Lie-group representation, while its Hilbert-space implementer $U(r)=e^{irP}$ is unitary and its positive generator $P$ is not nilpotent.* This sharpens the boundary of the slogan "nilpotency is the algebraic signature of null" in [[nilpotency-and-the-wall/the-trichotomy-identification|the trichotomy note]]: the nilpotency lives in the group/monodromy register (defining representations, lattice monodromy $T_0=\mathbf1+N$), **not** in the operator register, where the same parabolic class is carried unitarily with a positive generator. The trichotomy note's claims are stated register-correctly as written, but the firewall between the two registers now has an explicit owner, and the trichotomy note should cite it. Consequence for [[nilpotency-and-the-wall/construction-bridges|Bridge 1]]: "nilpotent holonomy as the wall's defining datum" is a statement about transport/monodromy data, and must never be read as a demand for nilpotent Hilbert-space operators — the positive generator $P$ is the operator-register face of the same datum.

## 2. The codimension-two invariant has a third independent register **[UPGRADE]**

[[inbox/supplying-complex-numbers/the-necessity-of-i|The necessity of i]] (inbox, unprocessed) proves a conditional selection theorem: among connected locally compact division rings, only $\mathbb C$ makes one polynomial condition carve a wall of real codimension two — encircleable but not crossable, braided monodromy alive; $\mathbb R$ disconnects (codim 1), $\mathbb H$ trivializes the loop (codim 4). This is the same rank-two transverse invariant proposed in [[nilpotency-and-the-wall/a2-the-fourth-register|the fourth-register note]], arriving from field selection rather than from cuts or catastrophes. Three independent registers now say codimension two: the wall's null normal plane, the $A_2$ control plane, and the complex numbers' defining property. The signature's "interface with quantum is complex" clue and the codim-2 ledger are plausibly one fact; weaving the necessity-of-i note into the algebra module should be prioritized.

## 3. The wall-and-block computation is the lattice shadow of the two registers **[BENCHMARK]**

[[inbox/cpsg/the-wall-and-the-block|The wall and the block]] (inbox, flagged by its own README as a rough source) contains one exact and valuable computation: on a free lattice field, the *commutator* has a sharp causal front (suppression $5\times10^8$ outside an emergent cone) while the *vacuum correlations* have no fence at all. That is the vertical/horizontal — algebra/state — distinction of the programme rendered numerically: **the algebra has a front; the state has no fence.** It is also the correct lattice intuition for the signature's S1 (the net is where causality lives) versus S3 (the state points globally). Worth salvaging into a basic-concepts or wall-interface benchmark note regardless of the folder's other claims.

## 4. The referee lineage, located **[PROVENANCE]**

The six-item list's vocabulary ($e_N$, $\varphi,d,\nu$, whole-core versus finite-corner) matches [[wall-construction-interface/core-spectral-wall|the core spectral wall's]] own eight-item open list, of which it is a faithful compression; the earlier referee document in this lineage is `deriving-value-of-g/chats/02/response.md`, which seeded the first pass ($\chi_\downarrow$, the conversion square, the susceptibility reading) and whose alpha-paper audit (the $U(3)$ and $\mathrm{Cl}_7$ errors in the SSRN 137 derivation) remains the owner of that verdict. The exact six-item text does not appear in the vault; this folder quotes it from the user.

## 5. Candidate matter-side selector for the member slot **[POINTER]**

[[spectral-wall-descent/twist-fixed-point-wall|The twisted fixed-point wall]] (new) supplies $E_\rho=(1+\rho)/2$ with the Standard-Model algebra as fixed points — a concrete matter-coupled candidate for the "principled selection of $d$" once item 1's net exists, consistent with the verdict's dependency correction that the member comes from coupling, not from the signature.

## Search coverage

Greps run across all tracked markdown (excluding `.obsidian`): the referee phrases ("sharply isolated", "whole-core", "finite-corner", "AI-referee"); "operator signature" and Schrödinger (all prior occurrences in other roles — Bargmann, variational, Darboux — no prior owner of the positing analogy); inbox survey (`boltzmann-ledger`, `cpsg`, `hessian-geometry-and-the-library-tools`, `radical-copernicanism`, `supplying-complex-numbers`); new-file sweep by mtime against the last session write. Not read end-to-end: `boltzmann-ledger` (tex + pdf; appears to be a thermodynamic dictionary with checks) and the legacy v7/v8 archives — neither surfaced terms bearing on the six items.
