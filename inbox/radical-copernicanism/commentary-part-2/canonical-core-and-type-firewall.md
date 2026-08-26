# The Canonical Core and the Type Firewall

The canonical core provides exact covariance among modular presentations of one von Neumann algebra, but it cannot turn the physical $\mathrm{II}_1/\mathrm{II}_\infty$ distinction into a mere change of weight. This firewall separates weight-independent operator algebra from the additional observer, constraint, spectral, and representation data that select a gravitational algebra.

## What changing a weight does

Let $M$ be a von Neumann algebra and let $\varphi$ and $\psi$ be faithful normal semifinite weights. Their modular groups are related by the Connes cocycle derivative,

$$
\sigma_t^\varphi(x)
=(D\varphi:D\psi)_t\,
\sigma_t^\psi(x)
(D\varphi:D\psi)_t^*.
$$

Crossed-product presentations built from $\varphi$ and $\psi$ are correspondingly isomorphic. The Falcone--Takesaki construction packages all such presentations into a canonical, weight-independent core $\widetilde M$ carrying a canonical semifinite trace $\widetilde\tau$ and dual action $\theta_s$ with

$$
\widetilde\tau\circ\theta_s=e^{-s}\widetilde\tau.
$$

The canonical weight independence is **[STANDARD]**, as presented in [[library/noncommutative-flow-of-weights|The Non-Commutative Flow of Weights on a von Neumann Algebra]]. Reading it as democracy of reference presentations on fixed $M$ is an interpretive programme reading, not another theorem. It does not imply democracy of physically selected states or weights.

## The no-toggle statement

For fixed $M$, changing the faithful normal semifinite weight cannot change the isomorphism type of the canonical core. In particular, it cannot toggle that core between $\mathrm{II}_1$ and $\mathrm{II}_\infty$.

For a type-$\mathrm{III}_1$ factor, the Connes--Takesaki flow of weights on $Z(\widetilde M)$ is trivial because the center is trivial. The dual action on the whole core still scales its semifinite trace. Therefore:

$$
\boxed{
\text{flow of weights on }Z(\widetilde M)
\ne
\text{dual trace-scaling action on the core}.}
$$

The statement “the nonvanishing obstruction class is the flow of weights” must be revoked for the $\mathrm{III}_1$ case. Type-III-ness excludes a nonzero normal semifinite trace on $M$; identifying some separate descent obstruction with the dual action is an open theorem target.

Results asserting that states with trivial centralizer are generic on a specified algebra do not select the programme's physical state or weight. Nor do they eliminate holonomy or obstruction data attached to inclusions, correspondences, or cocycles; those live on different carriers and require their own construction.

## Where gravitational factor type enters

The physical algebra should be typed as the output of a richer construction,

$$
(M,\text{symmetry},\text{QRF},\text{constraint},
\text{representation},\text{KMS data},\text{spectral domain})
\longmapsto
\mathcal A_{\mathrm{phys}}.
$$

Witten's [[library/gravity-and-the-crossed-product|Gravity and the Crossed Product]] obtains a $\mathrm{II}_\infty$ algebra in a particular gravitational large-$N$ construction. Chandrasekaran--Longo--Penington--Witten's [[library/de-sitter-observables-algebra|An Algebra of Observables for de Sitter Space]] obtains a $\mathrm{II}_1$ algebra after dressing observables to a de Sitter observer. [[library/quantum-reference-frames-local-algebra-types|Quantum Reference Frames, Measurement Schemes and the Type of Local Algebras in Quantum Field Theory]] gives explicit thermal hypotheses under which a QRF-invariant algebra has a semifinite or finite trace.

These are related constructions, not two weight frames of one fixed core. A finite corner of a $\mathrm{II}_\infty$ factor may be $\mathrm{II}_1$, but the projection or constraint selecting that corner is additional data.

## Programme boundary

The dual parameter $s$ exists as part of the canonical core even for a static physical situation. Hence the trace-scaling law does not by itself represent cosmic expansion, produced time, horizon growth, or CST capacity growth. Every such identification requires the vertical-to-horizontal solder already demanded by [[wall-construction-interface/vertical-and-horizontal-motion|Vertical and Horizontal Motion]].

The reusable theorem and terminology belong in a future `basic-concepts/canonical-core` module. The wall interface should own only the consequences for vertical modular presentation versus horizontal physical realization.
