# The Counting Rate of the Wall

The entropy-per-channel of [[deriving-g-v2/index-not-entropy|the index note]] retypes, via graph norms, into a growth rate: $s_*=\tfrac12\log\operatorname{Ind}=\log\lVert\Gamma\rVert$ is the nats-per-step of path counting on the wall's principal graph. Smith's classification then sorts the possibilities exactly, a one-line transcendence argument shows what "$s_*=1$ exactly" would mean, and the fit window's algebraic alternatives can be enumerated outright. The background profile is now reproduced; every graph-theoretic inference remains conditional on the unproved channel reading that turns its fitted amplitude into $s_*$.

## Smith's trichotomy

**[STANDARD]** Smith (1970): a finite connected simple graph has spectral norm $<2$ iff it is an ADE Dynkin diagram, and norm $=2$ iff it is an affine ADE diagram; everything else has norm $>2$. For finite-depth subfactors, with the usual principal-graph hypotheses, $\operatorname{Ind}=\lVert\Gamma\rVert^2$ (Jones 1983), so:

| Regime | Graphs | s* = log norm | Wall reading |
|---|---|---|---|
| norm < 2 | ADE exactly | the rigid Jones ladder, s < ln 2 | spherical: finite Weyl-type symmetry |
| norm = 2 | affine ADE exactly | s = ln 2, the one-bit ceiling (index 4) | Euclidean: the affine graphs Ã_n, D̃_n, Ẽ_n |
| norm > 2 | indefinite type | s > ln 2 | hyperbolic growth |

The path-graph identity $\lVert A_{n-1}\rVert=2\cos(\pi/n)$ makes the Jones ladder *literally* the ADE column (receipts verify $A_3\mapsto\sqrt2\mapsto$ index 2). That index-2 rung is not the type-I qubit edge factor used elsewhere in the vault, whose dimension $d=2$ gives index $d^2=4$ and ceiling $s=\ln2$. On the unit-rate channel map $s_*=1/\mathfrak R_c$, the reproduced profile on fully released 2025 data gives

$$
s_*=0.9861,
\qquad
\Delta\chi^2\le1:\ [0.9175,1.0621],
\qquad
\Delta\chi^2\le3.84:\ [0.8580,1.1425].
$$

Even the wider displayed contour lies above $\ln2$. Conditional on the channel map, it therefore says: **the wall's principal graph is beyond ADE — indefinite type, exponential path growth. The wall counts hyperbolically.** The data measure only the effective background amplitude; the graph type enters through the extra state--geometry identification. These are profile-likelihood contours, not posterior credible intervals.

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

Representative finite-depth-admissible indices in the current $\Delta\chi^2\le1$ fit window $[6.265,\,8.365]$ (products of Jones-ladder values and integers; receipts) include:

| Index | Structure | (s_*) | target precision in (mathfrak R_c) to separate from 1 |
|---|---|---|---|
| 6.854 | golden squared (two golden channels) | 0.9624 | 0.019 (x4 tighter than current) |
| 7 | integer (e.g. Z/7 fixed points) | 0.9730 | 0.014 (x5) |
| 7.236 | 2 x 4cos^2(pi/10) | 0.9895 | 0.005 (x14) |
| 7.365 | 2 x 4cos^2(pi/11) | 0.9984 | 0.0008 (x92) |
| 7.464 | 4 + 2 sqrt 3 | 1.0051 | 0.003 (x29) |
| 8 | three index-2 channels | 1.0397 | 0.020 (x4) |

**Honesty clause, load-bearing:** the algebraic set *accumulates* (the two-factor products sweep toward 8, passing within $\Delta s_*=0.0016$ of 1), so no finite-precision measurement can ever prove transcendence. What measurement can do is kill finite lists — and each algebraic survivor is not just a number but a *named symmetry* with independent obligations (fusion rules, graph structure, sector counting), so the fork is decided structurally, not decimally. At four times the current fit precision the golden and integer-7 candidates die or win; the deep-ladder twins require structure, not digits.

## Consequences and failure

If the wall is ever proved finite-depth, $s_*$ is forced onto a countable algebraic set and the exact unit matching law $\mathfrak R_c=1$ cannot simultaneously identify $s_*=1$ in this channel model: the nearby finite candidates are close to, but not equal to, one. Conversely a proof of infinite depth makes $s_*=1$ admissible and the self-normalizing reading live. Either resolution converts a normalization postulate into a theorem about a graph — which is what counting is for. Kill conditions inherit from the index note: channel additivity and the unit-rate branch remain load-bearing, and the reproduced background amplitude must still be proved to be the channel ratio.
