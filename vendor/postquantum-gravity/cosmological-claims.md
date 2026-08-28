# The Cosmological Claims

Two papers apply the theory to problems normally assigned to dark matter and dark energy. Both are weaker than their titles suggest, and both are honestly hedged by their authors. The rotation-curve paper derives an anti-correlation between two metric coefficients, and obtains a MOND-like acceleration scale only after conditioning on the observed cosmological constant and choosing the cut-off radius to be the Hubble radius. The phantom-dark-matter paper has one clean result — diffusion drives the Hamiltonian constraint off its surface *positively on average* — and a final density estimate that misses the observed value by about thirty-one orders of magnitude. Neither should be cited as a success of the theory; the first is a suggestive calculation with an unfixed free parameter, the second is a candid null result.

## Anomalous rotation curves

Source: [[library/anomalous-galactic-rotation-curves/inq|Oppenheim and Russo]].

Restricting to static, spherically symmetric metrics of the Mannheim--Kazanas form, the classical-limit action makes the metric coefficients jointly Gaussian with **zero mean** and **negative correlation**. The authors state that all terms of the power series are kept and the unwanted ones marginalised by Gaussian integration, so the two-parameter presentation is a marginal rather than a truncation. Conditioning on the observed $\gamma_2=\Lambda/3$ at $r_{\max}=R_H$ gives

$$
\mu_{\gamma_1\mid\gamma_2}
=-\tfrac32\Lambda R_H\frac{1-4\beta}{5-18\beta},
$$

of order $10^{-10}\ \mathrm{m\,s^{-2}}$ — the MOND scale — and negative. Reading that sign as an extra inward acceleration follows from the paper's own potential convention but is an inference, not a statement in the source, which notes that the linearised theory has no preferred sign until nonlinear corrections enter.

Three things must be said about it. Dimensional analysis alone forces $\mu_{\gamma_1}\propto\gamma_2r_{\max}$, so the numerical coincidence is largely supplied by the choice $r_{\max}=R_H$ rather than predicted; the authors concede that "the theory does not precisely predict the coincidence." The expectation values are zero, so the result exists only after conditioning on one observed quantity. And the time integral is dropped, replaced by an undetermined parameter $\epsilon$ with $D_{0,T}=D_0c\epsilon$; consistency with tabletop bounds is then purchased by inferring $\epsilon\leq10^{-25}\,$s from the very consistency being claimed. On the reliability of the power-series model generally the authors add that "anything can be fit to a power series, and a fuller understanding of the probability distribution is required," and that a principal-component treatment would be preferable.

Separately, the paper argues that in a "diffusion regime" — defined by $\langle(\nabla\Phi)^2\rangle\gg\langle\nabla\Phi\rangle^2$, the mean square of the acceleration far exceeding the square of its mean — the extra variance acts as a positive effective mass, "a necessary condition for MOND behaviour." The acceleration scale here is not a constant of the theory: it depends on the size of the test mass and the averaging time, which the authors state plainly. The two halves of the paper are never joined into one derivation.

There is no modified field equation, no covariant formulation of the result, no rotation curve fitted, and no galaxy in the paper. The paper also reports against itself on the related question of the cosmological constant: obtaining $\Lambda$ from the variance of local fluctuations would need a dimensionless coupling some forty orders of magnitude from the tabletop bounds, which the authors read as evidence that local stochastic fluctuations are too small to contribute to $\Lambda$ that way.

**The Hertzberg--Loeb exchange.** An appendix replies to an arXiv comment (2404.13037, a preprint). The authors concede outright that a $\kappa_1r$ vacuum term cannot satisfy Newtonian matching for a localised source ("This is true"), that the random variables have zero expectation ("This is true"), and that the linear term alone does not fit modern data without the additional $\gamma_2$ term. They rebut the charges that the two-point function's short-distance singularity makes the theory ill defined, and that conditioning removes the correlation. The rebuttal on tabletop consistency turns entirely on the free parameter $\epsilon$. A reader assessing this paper should read the appendix first.

## Phantom cold dark matter

Source: [[library/phantom-cold-dark-matter/inq|Oppenheim, Panella and Pontzen]].

The clean result is a consequence of Itô's lemma. The Hamiltonian constraint $C_H$ is convex in the momentum $\pi_a$, and the noise enters $\pi_a$, so the second-order Itô term is positive definite:

$$
\dot C_H=D_2(a)\frac{3}{32\pi G}a^3N+\tfrac12\pi_aaN\bar\xi .
$$

The first term is a strictly positive drift for any $D_2>0$, requiring no inflation and no tuning. It is Jensen's inequality made dynamical, and the authors gloss it as the heating of a Brownian particle without friction. Constraint violation then gravitates as pressureless dust. That step is not this paper's: it recapitulates an argument of Kaplan and collaborators, in which the Bianchi identity together with stress-energy conservation and vanishing spatial constraint-violation components forces $w=0$. The paper's own contribution is the positive drift.

"Phantom" here means a source with no field and no Lagrangian behind it, gravitating like dust — **not** phantom dark energy, and not $w<-1$. The terminology collides with standard usage and should be flagged whenever the paper is cited.

The quantitative claim does not survive contact with the numbers.

$$
\Omega_c=\frac{4D_2}{\pi}e^{P}
\;\xrightarrow{\;P\approx55,\ D_2\lesssim10^{-54}\;}\;
\Omega_c\lesssim10^{-31},
$$

with the bound on $D_2$ itself holding only "in the case the fluctuations have no effective mass",

about thirty-one orders of magnitude short of $\Omega_{\mathrm{CDM}}\approx0.26$. The authors report this honestly and add that hitting the observed value would require a fine-tuned relation between $D_2$ and the number of e-folds. Three further problems compound it. The scaling of the diffusion coefficient with the scale factor requires an infrared cut-off the theory does not supply. The authors adopt averaging over a Hubble volume and defend it as averaging over the region in causal contact during the current e-fold; they offer a fixed-comoving alternative only "in the absence of a fully principled approach at present," and note separately that unless the scaling index is large enough the constraint keeps accumulating into radiation domination and would likely violate CMB constraints. The Hubble choice does satisfy that requirement, so the remark eliminates the alternative rather than indicting the choice. What remains is that the theory does not force the scheme, and the authors state plainly: "At present, we do not have a rigorous procedure for performing this renormalisation." Second, the whole effect is an $O(D_2)$ drift produced by Itô's lemma. The authors devote an appendix to the Itô/Stratonovich choice and argue for Itô as natural when the noise is treated as fundamental — but under the adopted scheme the noise is multiplicative, and the drift is not recomputed in the Stratonovich reading, so the sign and scaling are robust while the prefactor is not established. And the ratio of the fluctuation to the mean is enormous, so "positive on average" is achieved by a very wide two-sided distribution in which typical regions carry negative effective density; the authors' escape is an assumption about averaging, not a calculation.

The paper also concedes that its construction "is indeed valid only as a description within a preferred frame, the cosmological one," which is a serious admission for a theory of gravity, and that a stochastic dynamics respecting the constraint exactly can be constructed, though they expect such a theory to violate diffeomorphism invariance.

## How to weight these

The construction papers and the cosmology papers should not be cited at the same confidence. [[cq-construction]], [[no-ghosts-and-real-couplings]] and [[stochastic-modes]] carry results; these two carry proposals with named gaps. The one durable transferable item is the Itô drift: **a convex constraint plus noise in the conjugate variable produces a positive one-sided violation**, which is a general mechanism and does not depend on the cosmological application.
