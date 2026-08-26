# The Mixmaster Import

The vault already contains, one wikilink from [[misner-log-time/entry|Misner log time]], a fully solved hyperbolic counting system: near-singularity mixmaster dynamics *is* — in a precise approximation — the boundary dynamics of the modular orbifold, and its chaos carries exact counts. This note states what can be imported without any new construction, at literature grade.

## The identification

**[STANDARD]** The Belinskii–Khalatnikov–Lifshitz era map of mixmaster (Bianchi IX) cosmology is the Gauss continued-fraction map $x\mapsto\{1/x\}$ on era parameters; mixmaster evolution is captured by the geodesic flow on the modular orbifold $\mathbb H/\mathrm{PSL}(2,\mathbb Z)$ — the $(2,3,\infty)$ base that [[geometry-is-counting]] identifies as the least cusped triangle orbifold (Chernoff and Barrow, Phys. Rev. Lett. **50**, 134 (1983); Cornish and Levin, Phys. Rev. Lett. **78**, 998 (1997), who made the chaos statement coordinate-invariant). The excursions into the cusp are the long Kasner eras: **the parabolic end of the orbifold is where the dynamics lingers** — the same parabolic locus that [[nilpotency-and-the-wall/the-trichotomy-identification|the trichotomy note]] types as the wall.

## The exact counts

**[STANDARD]** Three numbers come free. The Kolmogorov–Sinai entropy of the Gauss map with respect to the Gauss measure is

$$
h=\frac{\pi^2}{6\ln2}\approx2.373\ \text{nats per era}
$$

(Lévy's constant / Rokhlin's formula — note the numerator $\zeta(2)$ and the qubit's $\ln2$ in one constant). The geodesic flow on a curvature $-1$ surface has topological entropy exactly $1$ per unit hyperbolic length. And closed geodesics — periodic mixmaster histories — are counted by the prime geodesic theorem, $\#\{\ell\le L\}\sim e^L/L$, the hyperbolic prime-counting law.

## What the import is for

Two uses, typed. First, it is an existence proof: a cosmological dynamics whose "brutal counting" is *finished* — entropy per era, growth of periodic histories, all exact — because the underlying geometry is hyperbolic and rigid. It calibrates what a completed counting theory of the programme's wall chain should look like. Second, it is adjacent, not identical: mixmaster chaos lives in the anisotropy degrees of freedom near a singularity, not in the homogeneous scale response of [[causal-scale-theory/entry|CST]]; no identification of the era map with the wall chain is proposed. The honest bridge candidate is structural: both systems place their irreversible bookkeeping at the parabolic end of a modular-type base, and if the wall family's base is triangle-type ([[geometry-is-counting]]), the mixmaster case is the worked example of how counting theorems attach to such a base. Any stronger claim needs a map and is not made here.
