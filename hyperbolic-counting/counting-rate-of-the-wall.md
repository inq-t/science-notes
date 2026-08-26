# The Counting Rate of the Wall

The entropy-per-channel of [[deriving-g-v2/index-not-entropy|the index note]] retypes, via graph norms, into a growth rate: $s_*=\tfrac12\log\operatorname{Ind}=\log\lVert\Gamma\rVert$ is the nats-per-step of path counting on the wall's principal graph. Smith's classification then sorts the possibilities exactly, a one-line transcendence argument shows what "$s_*=1$ exactly" would mean, and the fit window's algebraic alternatives can be enumerated outright. Everything is conditional on the channel reading and the reported-limited fit, as before.

## Smith's trichotomy

**[STANDARD]** Smith (1970): a connected graph has spectral norm $<2$ iff it is an ADE Dynkin diagram, and norm $=2$ iff it is an affine ADE diagram; everything else has norm $>2$. For finite-depth subfactors $\operatorname{Ind}=\lVert\Gamma\rVert^2$ (Jones 1983), so:

| Regime | Graphs | s* = log norm | Wall reading |
|---|---|---|---|
| norm < 2 | ADE exactly | the rigid Jones ladder, s < ln 2 | spherical: finite Weyl-type symmetry |
| norm = 2 | affine ADE exactly | s = ln 2, the qubit ceiling | Euclidean: the qubit's graph is A3 |
| norm > 2 | indefinite type | s > ln 2 | hyperbolic growth |

The path-graph identity $\lVert A_{n-1}\rVert=2\cos(\pi/n)$ makes the Jones ladder *literally* the ADE column (receipts verify $A_3\mapsto\sqrt2\mapsto$ index 2, the qubit). The fitted $s_*\in[0.919,1.063]$ therefore says: **the wall's principal graph is beyond ADE — indefinite type, exponential path growth. The wall counts hyperbolically.** This is the graph-theoretic face of the "above the Jones wall" conclusion, and it types the wall's symmetry shadow as a hyperbolic-growth object.

## The transcendence theorem

**[SMALL THEOREM]** A finite graph's norm is the largest root of an integer characteristic polynomial — an algebraic integer; in the fusion-category setting dimensions are even cyclotomic integers (Etingof–Nikshych–Ostrik, Ann. Math. **162**, 581 (2005)). But $e$ is transcendental (Hermite 1873). Hence

$$
s_*=1\ \text{nat exactly}
\;\Longleftrightarrow\;
\operatorname{Ind}=e^2
\;\Longrightarrow\;
\text{no finite principal graph: infinite depth.}
$$

One nat per channel — the self-normalizing wall of [[deriving-g-v2/index-not-entropy|the index note]] — is incompatible with *any* finite quantum symmetry. The fork is now structural: **algebraic counting rate = finite symmetry with a specific graph; transcendental rate = infinite depth.**

## The algebraic survivors in the window

Enumerating finite-depth-admissible indices in the fit window $[6.285,\,8.376]$ (products of Jones-ladder values and integers; receipts):

| Index | Structure | s* | needed sigma(r_c) to separate from 1 |
|---|---|---|---|
| 6.854 | golden squared (two golden channels) | 0.9624 | 0.019 (x4 tighter than current) |
| 7 | integer (e.g. Z/7 fixed points) | 0.9730 | 0.014 (x5) |
| 7.236 | 2 x 4cos^2(pi/10) | 0.9895 | 0.005 (x14) |
| 7.365 | 2 x 4cos^2(pi/11) | 0.9984 | 0.0008 (x92) |
| 7.464 | 4 + 2 sqrt 3 | 1.0051 | 0.003 (x29) |
| 8 | three index-2 channels | 1.0397 | 0.020 (x4) |

**Honesty clause, load-bearing:** the algebraic set *accumulates* (the two-factor products sweep toward 8, passing within $\Delta s_*=0.0016$ of 1), so no finite-precision measurement can ever prove transcendence. What measurement can do is kill finite lists — and each algebraic survivor is not just a number but a *named symmetry* with independent obligations (fusion rules, graph structure, sector counting), so the fork is decided structurally, not decimally. At four times the current fit precision the golden and integer-7 candidates die or win; the deep-ladder twins require structure, not digits.

## Consequences and failure

If the wall is ever proved finite-depth, $s_*$ is forced onto the countable ladder and the unit matching law $\mathfrak R_c=1$ of [[causal-scale-theory/reference-cut-matching-ratio|homogeneous capacity]] is *false by arithmetic* — the nearest ladder points are 0.9984 and 1.0051, not 1. Conversely a proof of infinite depth (e.g. from the wall construction itself) makes $s_*=1$ admissible and the self-normalizing reading live. Either resolution converts a normalization postulate into a theorem about a graph — which is what counting is for. Kill conditions inherit from the index note: channel additivity, the unit-rate branch, and the fit's reproduction remain the load-bearing assumptions.
