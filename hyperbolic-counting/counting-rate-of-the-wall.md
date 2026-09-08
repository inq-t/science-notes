# Counting Rate of the Wall

A wall entropy becomes a graph-counting rate only after two separate identifications: an entropy–index equality and a theorem equating that index with the squared principal-graph norm. Under those hypotheses, Smith's finite-graph classification and the algebraicity of finite graph norms constrain the channel interpretation of the reproduced background profile. The exact one-nat principle would then exclude finite depth; the numerical table samples possible algebraic indices without classifying them.

## Smith's trichotomy

**[STANDARD]** Smith (1970): a finite connected simple graph has spectral norm $<2$ iff it is an ADE Dynkin diagram, and norm $=2$ iff it is one of the simple affine ADE diagrams; everything else has norm $>2$. Principal graphs can have multiple edges, so this simple-graph classification needs that additional hypothesis.

For a finite-index \(\mathrm{II}_1\) subfactor with finite principal graph \(\Gamma\), its Jones index satisfies \(\operatorname{Ind}_J=\lVert\Gamma\rVert^2\); finite depth also implies extremality. In general only \(\lVert\Gamma\rVert^2\le\operatorname{Ind}_J\) is automatic ([Jones–Morrison–Snyder, §2.1, Definition 2.4 and Fact 2.6](https://arxiv.org/html/1304.6141)). Thus an infinite-depth graph requires a separate norm–index equality before its counting rate can be read from index.

The additional physical equality \(s_*=\tfrac12\log\operatorname{Ind}_J\) is not supplied by either theorem. [[deriving-g-v2/index-not-entropy|The index note]] proves only a type-I product-edge entropy bound and identifies the extra saturation requirement. When both equalities hold, \(s_*=\log\lVert\Gamma\rVert\) is the exponential rate of graph-walk counts per edge step (with parity handled by a limsup). The graph-theoretic alternatives are:

| Regime | Finite simple graphs | Graph rate log norm | Conditional wall reading |
|---|---|---|---|
| norm < 2 | ADE | rate < ln 2 | sub-4 index under the norm identity |
| norm = 2 | simple affine ADE | rate = ln 2 | index 4 under the norm identity |
| norm > 2 | beyond the ADE threshold | rate > ln 2 | growth beyond the norm-2 threshold |

The path-graph identity $\lVert A_{n-1}\rVert=2\cos(\pi/n)$ reproduces the Jones-ladder numbers (receipts verify $A_3\mapsto\sqrt2\mapsto$ index 2). Smith's graph list alone is not a realization theorem for principal graphs. That index-2 rung is not the type-I qubit edge factor used elsewhere in the vault, whose dimension $d=2$ gives index $d^2=4$ and ceiling $s=\ln2$. On the unit-rate channel map $s_*=1/\mathfrak R_c$, the reproduced profile on fully released 2025 data gives

$$
s_*=0.9861,
\qquad
\Delta\chi^2\le1:\ [0.9175,1.0621],
\qquad
\Delta\chi^2\le3.84:\ [0.8580,1.1425].
$$

Even the wider displayed contour lies above $\ln2$. Under the channel map, the separate entropy–index equality, and the graph norm–index identity, it places the candidate graph norm above 2. If that graph is finite and simple, it lies beyond Smith's ADE and affine lists. With only an entropy upper bound one obtains an index lower bound; for an infinite-depth inclusion, a large index alone does not force its graph norm above 2. The data measure only the effective background amplitude. These are profile-likelihood contours, not posterior credible intervals.

## The transcendence theorem

**[SMALL THEOREM, CONDITIONAL APPLICATION]** A finite graph's norm is the largest root of an integer characteristic polynomial, hence an algebraic integer. In the finite-depth fusion-category setting the index is a cyclotomic integer (Etingof–Nikshych–Ostrik, Ann. Math. **162**, 581 (2005)). These statements concern the norm and index, not their logarithms. Since $e$ is transcendental (Hermite 1873), an inclusion with the independently proved equality \(s_*=\tfrac12\log\operatorname{Ind}_J\) obeys

$$
s_*=1\ \text{nat exactly}
\;\Longleftrightarrow\;
\operatorname{Ind}=e^2
\;\Longrightarrow\;
\text{no finite principal graph: infinite depth.}
$$

The contradiction uses the finite-depth norm–index theorem; it does not require a norm–index equality on the resulting infinite graph. A bare entropy value of one nat, or only a half-log upper bound, does not give this conclusion. The theorem excludes a finite-depth realization of this particular inclusion under the equality; it does not exclude every finite symmetry or finite sector in the theory. Its converse also fails: an algebraic index does not imply finite depth.

## The algebraic survivors in the window

If the entropy–index equality is supplied, the current $\Delta\chi^2\le1$ profile maps to the index window $[6.265,\,8.365]$. A bounded search over products of Jones-ladder values and selected integers gives representative finite-depth-admissible indices, including:

| Index | Example construction | Half-log, equal to s* only under the weld | Target precision in matching ratio to separate from 1 |
|---|---|---|---|
| 6.854 | golden squared (two golden channels) | 0.9624 | 0.019 (x4 tighter than current) |
| 7 | integer (e.g. Z/7 fixed points) | 0.9730 | 0.014 (x5) |
| 7.236 | 2 x 4cos^2(pi/10) | 0.9895 | 0.005 (x14) |
| 7.365 | 2 x 4cos^2(pi/11) | 0.9984 | 0.0008 (x92) |
| 7.464 | 4 + 2 sqrt 3 | 1.0051 | 0.003 (x29) |
| 8 | three index-2 channels | 1.0397 | 0.020 (x4) |

The displayed constructions are examples, not a classification of all finite-depth indices in this window. The family \(2\cdot4\cos^2(\pi/n)\) accumulates at 8, and the sampled \(n=11\) case has half-log within about 0.0016 of one. Neither observation proves arbitrary closeness to \(e^2\) or excludes a gap there. The receipt checks this finite sample and arithmetic separation estimates; structural classification would be needed to exclude all finite-depth alternatives. Finite-precision numbers alone do not establish exact transcendence, and an index value does not uniquely specify fusion rules or a symmetry.

## Consequences and failure

If the wall is proved finite-depth and the entropy–index equality holds, its index is algebraic and its entropy is half the log of that algebraic index. This rules out exact one-nat entropy under that equality. A proof of infinite depth only removes this particular obstruction; it does not select \(e^2\), supply the equality, or fix a graph growth rate. Channel additivity, the unit-rate branch, and identification of the background amplitude with the channel ratio remain independent requirements. Failure of the entropy–index equality retires this graph interpretation while leaving the profile and finite-graph theorems intact.
