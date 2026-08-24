# Postquantum Gravity

A theory in which spacetime stays classical while matter stays quantum, made consistent by letting the metric diffuse and the quantum state decohere at a fixed exchange rate. Its best result is structural rather than phenomenological: because the classical-quantum couplings are real where quadratic gravity's are imaginary, the same curvature-squared action that renormalises quadratic gravity carries no ghost, since it is a probability weight over metrics rather than a higher-derivative Lagrangian. Its cosmological applications are much weaker than their titles. Its deepest point of contact with this project is a result the published paper states plainly: at saturation of the decoherence--diffusion trade-off the quantum state remains pure conditioned on the classical trajectory — which the paper calls a remarkable consequence of that saturation, and which underwrites its general remark that in CQ dynamics, under certain natural conditions, there is no loss of quantum information.

## The construction

[[cq-construction]] sets out the formalism. A classical-quantum state assigns an unnormalised density matrix to each classical configuration, and preserving that state space under partial action forces completely positive, trace-preserving dynamics. The path integral therefore carries a Feynman--Vernon term that decoheres the matter and an Onsager--Machlup term that diffuses the metric,

$$
\mathcal I_{CQ}
=i\mathcal S_Q[\phi^+]-i\mathcal S_Q[\phi^-]
+i\mathcal S_{FV}
+\mathcal S_{\mathrm{diff}},
$$

with the diffusion term an equation of motion squared, suppressing geometries — if the kernel is positive definite — in proportion to how badly they violate Einstein's equations sourced by the average stress-energy over bra and ket. The construction is diffeomorphism invariant, complete positivity is proved directly rather than through a master equation, and *local* CQ dynamics provably cannot generate entanglement.

Two features are locked together rather than independently adjustable. Decoherence and diffusion trade against each other, and at saturation the conditioned quantum state stays pure while the unconditioned one decoheres.

## The idea worth taking

[[no-ghosts-and-real-couplings]] is the best thing in this vendor. Ostrogradsky's instability, and the negative-norm ghost that has dogged quadratic gravity since Stelle, both presuppose that the action generates deterministic evolution. Change one coefficient —

$$
\frac{i}{\hbar}\;=\;-\frac{1}{2D_2}
$$

— and the same $\int(\ddot q)^2$ is no longer a Lagrangian but the log-probability of a diffusion, whose Hamiltonian is the ordinary bounded one. The provenance differs accordingly: an $i\ddot q^2$ term comes from integrating out a negative-energy field, an $-\ddot q^2/2D_2$ term from integrating out a positive-energy noise source. The saddle points cease to be equations of motion and become most probable paths given initial *and* final data.

The trade is exact and should be stated as one: an indefiniteness problem in the norm has been converted into a positivity problem in a probability measure. That is progress only insofar as the positivity can be proved, and it has been proved sector by sector rather than wholesale.

## What follows, and what does not

[[renormalisation]] maps the pure-gravity path integral onto quadratic gravity, obtains formal renormalisability by power counting, and argues that the reality of the couplings flips the sign of the beta functions, so that the dimensionless couplings run to infinity in the ultraviolet and diffusion grows at short distances, with a conjectural bearing on black-hole singularities. Asymptotic freedom enters separately, inherited from scale-invariant quadratic gravity through the mapping. Positivity of the two-point function appears to force the bare cosmological-constant terms to vanish and to single out the scale-invariant theory. The authors name the open question themselves: whether the renormalisation prescription retains complete positivity.

[[stochastic-modes]] answers what actually fluctuates. A scalar-vector-tensor decomposition gives one spin-0 and two spin-2 modes, each diffusing around its own wave equation; the Newtonian potential and the vector are fixed by constraints. Crucially, the sector where the Lorentzian deWitt kernel is indefinite is the non-dynamical vector sector, so the indefiniteness is *relatively* benign — it sits where nothing propagates, once the path integral is restricted to continuous geometries, with off-shell tachyonic modes still not fully understood. The same paper records that reducing the phase space before adding noise is inequivalent to letting noise act on the full metric, a warning this project should heed on its own account.

[[cosmological-claims]] handles the two applications and downgrades both. The rotation-curve result is an anti-correlation between two marginalised metric coefficients, with the MOND-like scale largely supplied by choosing the cut-off radius to be the Hubble radius, and with tabletop consistency purchased through an undetermined time scale. The phantom-dark-matter paper has one clean mechanism — a constraint convex in a noisy variable acquires a positive Itô drift — and a final density thirty-one orders of magnitude below the observed one, which the authors report honestly.

[[vendor/postquantum-gravity/empirical-status|empirical status]] collects the bounds. The theory is squeezed from both sides at once; the newest source puts the surviving window at roughly five orders of magnitude in the dimensionless diffusion coefficient, and a confirmed observation of gravitationally induced entanglement would falsify it outright.

## Where this meets the programme

[[vendor/postquantum-gravity/commentary/descent-instead-of-diffusion|Descent instead of diffusion]] develops the reframing this module was commissioned for. Stochasticity cannot be removed — complete positivity forces it — but the meaning of the measure is not fixed by the mathematics, and conditional purity says that nothing is lost *along* a history. The mixedness of the unconditioned state is marginalisation over which history obtains, and that is a fact rather than a fluid. In this project's vocabulary the classical trajectory is a character and the Onsager--Machlup weight is the measure a sufficing reason delivers, so the switch from $e^{iS/\hbar}$ to $e^{-\mathcal I/2D_2}$ is the switch from a necessitating to a sufficing ground — the same switch that removes the ghost.

The residue reading has a concrete candidate as well. An Onsager--Machlup action is a cost functional, and in gravity that cost is the curvature-squared sector. That converts a slogan into a theorem target: derive an equation-of-motion-squared weight from a descent rather than postulate it.

What the vendor does not supply is the descent itself. A measure over global histories is not a site with transport and effectivity, and [[vendor/postquantum-gravity/commentary/translation-into-the-programme|the translation]] states the four construction tests that would decide whether the rhyme becomes a relation. [[vendor/postquantum-gravity/commentary/standard-physics-audit|The audit]] fixes the confidence at which each item may be cited, and [[source-map|the source map]] maps the archive.

## Claim levels

| Status                    | Content                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[STANDARD]**            | the CQ path integral construction, its complete positivity and diffeomorphism invariance; no generation of entanglement by *local* CQ dynamics, the locality hypothesis being load-bearing; the decoherence--diffusion trade-off and, at saturation, purity of the quantum state conditioned on the classical trajectory                                                        |
| **[EXACT]**               | the Ostrogradsky objection does not apply to an Onsager--Machlup weight, with the provenance argument distinguishing a negative-energy ghost from a positive-energy noise source; the identification of the dynamical stochastic modes and the location of the indefinite sector in the non-dynamical vector; the positive Itô drift of a constraint convex in a noisy variable |
| **[CONDITIONAL THEOREM]** | formal renormalisability, conditional on pole prescriptions in loops preserving complete positivity; positivity of the two-point function, shown sector by sector rather than wholesale                                                                                                                                                                                         |
| **[CONJECTURE]**          | ultraviolet growth of the diffusion, argued from an expected sign flip in the beta functions rather than computed; resolution of the black-hole singularity by dominance of fluctuations. Asymptotic freedom is not conjectural but inherited: it is a cited property of scale-invariant quadratic gravity, imported through the mapping                                        |
| **[REPORTED FIT]**        | the MOND-scale coincidence in the rotation-curve paper, obtained after conditioning and after choosing $r_{\max}=R_H$                                                                                                                                                                                                                                                           |
| **[NO-GO]**               | the phantom-dark-matter density falls short of $\Omega_{\mathrm{CDM}}$ by about thirty-one orders of magnitude, and reaching it would require a fine-tuned relation between the diffusion coefficient and the e-folds of radiation domination                                                                                                                                   |
| **[OPEN CONSTRUCTION]**   | positivity of the deWitt kernel and the effect of normalisation on the magnetic Weyl curvature, with a possible cost in covariance; boundary terms in a stochastic theory; constraints beyond linear order; equivalence of the path-integral and master-equation theories; the renormalisation-group map from laboratory to cosmological scales                                 |
| Outside this module       | whether conditional purity survives coarse-graining; whether the cost functional can be derived from a descent; and the actuality of any outcome, which the vendor no more supplies than the programme does                                                                                                                                                                     |
