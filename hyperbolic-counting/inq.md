---
inq.module: "hyperbolic-counting"
inq.include:
  - "**/*.md"
inq.ambient:
  - "**/*.py"
  - "**/*.txt"
keywords:
  - graph growth
  - principal graph
  - finite depth
  - entropy-index weld
  - hyperbolic orbifolds
  - horizon counting
---
# Hyperbolic Counting

Hyperbolic geometry is the regime where geometry is forced to be counting: orbifold areas are rational multiples of $\pi$, triangle bases are rigid and enumerable, graph norms classify growth, and volumes are topological. Run against the programme, this yields four results. The wall-channel analysis of [[deriving-g-v2/index-not-entropy|index, not entropy]] can be compared with Smith's graph classification only after an entropy–index equality and the appropriate principal-graph norm theorem are supplied. Under those hypotheses the fitted channel entropy puts the graph norm above 2; exact one-nat entropy would exclude finite depth. A bounded numerical table samples algebraic-index alternatives without classifying all wall symmetries. The holographic ledger is the exponential of a resolution depth — two nats per horizon e-fold, the codimension as a growth exponent, with $\mathrm d\iota/\iota=2(1+q)\,\mathrm dN$ tying ledger growth to deceleration exactly. Candidate wall bases with trichotomy monodromy are a countable list with exact rational invariants, the least being the modular orbifold. And the vault's Misner module sits one link from a fully solved hyperbolic counting system with entropy $\pi^2/6\ln2$ nats per era. Labels follow [[program-core/axioms-and-principles#Status vocabulary|the status vocabulary]]; the [[hyperbolic-counting/receipts/README|calculation record]] explains which numerical statements the receipts check.

## The results in order

**1. Geometry is counting.** **[STANDARD]** Gauss–Bonnet quantizes hyperbolic orbifold areas into rational multiples of $\pi$; triangle groups are rigid (zero moduli); Mostow rigidity makes volume topological in higher dimension. Consequence for [[algebra/theorem-programme|gate T3 and small target 5]]: three-marked wall bases carrying the trichotomy's monodromy data (elliptic, elliptic, parabolic) form a countable enumerable list — member selection over such bases is combinatorics, not analysis. [[geometry-is-counting]] owns the enumeration, the least-area observation that the minimal cusped base is the modular orbifold $(2,3,\infty)$ at $\pi/3$, the question this poses to the $S^6$ manuscript's $(3,4,\infty)$ at $5\pi/6$ — and the best firewall specimen yet found, $5\pi/6$ versus $\varphi^2$.

**2. The conditional graph-counting rate.** **[CONDITIONAL on the channel reading, entropy–index equality, and graph hypotheses + REPRODUCED BACKGROUND PROFILE]** The equality $s_*=\tfrac12\log\operatorname{Ind}_J$ needs an independent entropy theorem. For a finite-depth \(\mathrm{II}_1\) inclusion, $\operatorname{Ind}_J=\lVert\Gamma\rVert^2$ then makes entropy a graph-walk growth rate; infinite depth needs a separate norm–index equality. Smith's ADE and affine classification further assumes a finite connected simple graph. Under all applicable hypotheses, the profile $s_*\approx0.986$ places the norm above 2. The type-I qubit entropy ceiling $\ln2$ and graph norm-2 threshold coincide numerically without identifying their carriers: $A_3$ instead has squared norm 2. Under the entropy–index equality, exact $s_*=1$ gives transcendental index $e^2$ and excludes a finite principal graph. Algebraic index does not conversely imply finite depth, and these restrictions do not exclude every finite symmetry in a theory. [[counting-rate-of-the-wall]] develops the conditional theorem and a bounded sample of algebraic-index candidates.

**3. Two nats per horizon e-fold.** **[EXACT REARRANGEMENT + conditional reading]** The ledger is $\iota=\pi e^{2N_P}$ with resolution depth $N_P=\ln(R_A/\ell_P)$ — 140.3 today, 140.1 at flat-$\Lambda$CDM matter–$\Lambda$ equality, and 140.08 at the grain module's distinct programme crossing $H_c=83.1058$ — and along the expansion $\mathrm d\iota/\iota=2(1+q)\,\mathrm dN$: ledger growth per scale e-fold is set by the deceleration parameter and stalls in the de Sitter limit. Under the radial reading of scale, matching boundary growth $e^{(d-1)N}$ selects $d=3$. Independently, the Fisher geometry of location-scale families *is* hyperbolic — $H^{D+1}$, so $H^4$ for three-space — and Fisher volume counts distinguishable states. [[two-nats-per-e-fold]] owns both counters and their typed limits.

**4. The Misner import.** **[STANDARD, adjacent]** The BKL era map is the Gauss map — the boundary dynamics of the modular orbifold selected in result 1 — with Kolmogorov–Sinai entropy $\pi^2/(6\ln2)\approx2.373$ nats per era, geodesic-flow entropy one per unit length, and closed geodesics counted by the prime geodesic theorem. [[mixmaster-import]] states what [[misner-log-time/inq|the Misner module]] can import without new construction.

## Claim ledger

| Status | Content |
|---|---|
| Standard | Gauss–Bonnet orbifold areas; triangle-group rigidity; Smith's classification at norm 2; Mostow rigidity; Gauss-map entropy; prime geodesic theorem; Fisher geometry of Gaussian families is hyperbolic |
| Exact rearrangement | ledger = pi e^(2 N_P); d iota / iota = 2(1+q) dN; the bounded search over algebraic-index candidates |
| Small theorem | finite depth implies algebraic graph norm/index; exact s* = 1 excludes finite depth only with the entropy–index equality |
| Conditional | the channel reading of the reproduced profile, the separate entropy–index equality, and the graph norm hypotheses |
| Proposed | least-area member selection; the radial reading that turns the growth exponent into a dimension selector |
| Open | what selects (3,4,infinity) in the manuscript; whether the wall inclusion is algebraic or transcendental; the H4 rhyme |
