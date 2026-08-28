# The Puzzle as Contemporary Physics Poses It

Four distinct problems travel under the single name "dark energy," and their logical forms differ: a magnitude, a renormalization, a timing, and a function. Stating them separately is a precondition for asking whether one answer should be expected to cover them. The statements below are the standard ones, sourced to the literature rather than to this workspace; where a number is conventional or cutoff-dependent, that is said.

## P1 — The magnitude problem

Einstein's equation admits a term $\Lambda g_{ab}$ on dimensional grounds; general covariance does not forbid it. The problem is not its presence but its size. Observationally

$$
\rho_\Lambda\simeq0.7\,\rho_{\rm crit}
\sim\left(2\times10^{-3}\ \mathrm{eV}\right)^4 .
$$

Quantum field theory contributes zero-point energy from every mode. Cutting the sum off at a scale $M$ gives $\rho_{\rm vac}\sim M^4$, so the ratio to the observed value is roughly $10^{44}$ at the QCD scale, $10^{55}$ at the electroweak scale, and $10^{120}$ or so at the Planck scale — the figure usually quoted, and the origin of the phrase "the worst prediction in physics." The canonical statement of the problem in this form is Weinberg's 1989 review.

Two honest qualifications belong with the number. The cutoff estimate is not a renormalized prediction; a naive quartic cutoff is not even covariant, and the physically meaningful quantity is the renormalized coefficient, which is a measured input rather than a computed output. And the ratio depends on the cutoff choice by some seventy-five orders of magnitude, so "$10^{120}$" is a statement about a particular estimate, not a theorem. What survives both qualifications is the real difficulty: nothing in the framework relates the coefficient's observed value to any other scale in physics.

## P2 — The radiative-stability problem

Worse than the size is the instability. Every mass threshold in the theory contributes to the vacuum coefficient at order $m^4$, so a value tuned at one scale is regenerated at the next. The electron alone contributes some thirty orders of magnitude more than the observed total. The contrast with the Higgs mass is instructive and is usually stated too quickly. Softly broken supersymmetry still protects the Higgs mass, whose corrections then go as the breaking scale squared rather than as the cutoff squared. It does not protect the vacuum energy, whose contributions go as the fourth power of that scale. Only unbroken supersymmetry cancels the vacuum energy exactly, and it is broken; so the asymmetry is not that one quantity has a symmetry and the other does not, but that the same broken symmetry is soft for one and hard for the other.

This is a problem about renormalization, not about a number: it says that the small value is not merely unexplained but unstable under the corrections the rest of physics forces on it.

## P3 — The coincidence problem

Matter dilutes and a constant does not:

$$
\frac{\rho_\Lambda}{\rho_m}\propto a^3 .
$$

The ratio therefore sweeps through unity once, and only once, in the entire history. That it is of order one *now* — the crossover sits near $z\simeq0.3$ — selects our epoch out of a logarithmically long history for no stated reason.

This is a problem about timing. It is often waved away as a selection effect, but the anthropic version needs a prior over an ensemble and a habitability measure, and both are contested; Weinberg's 1987 bound is the serious version of the argument and it constrains rather than explains.

## P4 — The dynamics problem

Until recently $w=-1$ was consistent with everything, and the first three problems were the whole story. That changed with the DESI Baryon Acoustic Oscillation programme. Its DR2 analysis reports that the CPL parameterization

$$
w(a)=w_0+w_a(1-a)
$$

was preferred over $\Lambda$CDM in the 2025 BAO release at $3.1\sigma$ using BAO plus CMB, and between $2.8\sigma$ and $4.2\sigma$ depending on which supernova compilation was added. The August 2026 [[library/desi-dr2-results-iv/inq|DESI Ly$\alpha$ full-shape update]] shifts this to $2.7\sigma$ for DESI plus CMB and $3.0$--$3.5\sigma$ with the updated supernova samples. The favoured histories retain the same shape: $w>-1$ today and a phantom branch at higher redshift. The current DESI+CMB+DES-Dovekie summary, $(w_0,w_a)=(-0.821\pm0.054,-0.65\pm0.20)$, implies a CPL crossing near $z=0.38$; the precise epoch remains compilation- and parameterization-dependent.

Whatever its eventual fate, this is a problem of a different type from the first three. It is not about the value of a constant. It asks for a *function*, and it asks that function to cross the phantom divide — the one thing a canonical single scalar field cannot do without a ghost. That obstruction is not incidental to the present module; it is the subject of [[field-completion-no-gos]].

The evidence is genuinely provisional. The preference is carried largely by the lowest-redshift supernova anchor, the significances depend on the compilation, and the CPL basis is a two-parameter tangent family rather than a physical model, so the mapping from a preferred CPL quadrant to a physical mechanism is not one-to-one. None of that removes the structural point: $\Lambda$ is a constant, and the data are now asking about a shape.

## What the standard responses have in common

The catalogue is familiar: treat $\Lambda$ as an irreducible constant of nature and measure it; add a light scalar (quintessence, k-essence, phantom, quintom); modify gravity ($f(R)$, DGP, Horndeski, and their descendants); appeal to an anthropic selection over a landscape; or attribute the effect to inhomogeneity and backreaction.

Setting aside the anthropic and backreaction routes, every remaining option answers the question *what is dark energy?* by nominating an entry in an inventory — a new term on the matter side or a new term on the geometric side. Both are contents of spacetime. The measure-not-structure habit is what makes the first option, "shut up and calculate," feel like an answer at all: if $\Lambda$ is just a coupling, then measuring it is the whole job, and P1 through P3 are dissolved by declaring them not to be questions.

That move is unavailable to a programme whose motto is that there is a reason for everything. [[cosmodynamics/logical-roles|The division by logical role]] states the reason technically rather than as a preference: general relativity represents accelerated histories perfectly well once a source is supplied, and does not select the source law, explain the coefficient, or address its radiative behaviour. Representation is not constitutive closure. A brute constant is a place where the demand for a ground has been withdrawn rather than met.

## Why the bundling matters

If the four problems belong to one register, one answer should cover them, and the failure of every candidate to do so is evidence that the answer has not been found yet.

If they belong to different registers, the same failure means something else: that the question was malformed. [[register-audit]] argues for the second reading, and the argument is testable in the ordinary way, because a reclassification that merely renames things predicts nothing.

Sources for the standard statements above: S. Weinberg, *The cosmological constant problem*, Rev. Mod. Phys. **61** (1989) 1; S. Weinberg, *Anthropic bound on the cosmological constant*, Phys. Rev. Lett. **59** (1987) 2607; DESI Collaboration, *DESI DR2 Results II*, [[library/desi-dr2-results-ii/inq|arXiv:2503.14738]]; M. Cortês and A. R. Liddle, *On DESI's DR2 exclusion of $\Lambda$CDM*, [[library/on-desi-dr2-exclusion-of-lambda-cdm/inq|arXiv:2504.15336]].
