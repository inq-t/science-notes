# Local Source Library

Five primary sources for the postquantum theory of classical gravity, centred on Oppenheim's group at UCL but with co-authors at Poznań, Southampton, METU, and Perimeter. One published paper supplies the covariant construction; four arXiv sources develop renormalisation, mode structure, and cosmological application. Files are stored under their upstream names; this note is the map from name to content.

## The archive

| File | Reference | Content |
|---|---|---|
| [[sources/2rcd-dzcf.pdf\|2rcd-dzcf.pdf]] | Oppenheim & Weller-Davies, *Covariant Path Integrals for Quantum Fields Backreacting on Classical Space-Time*, Phys. Rev. X **16**, 031007 (2026); DOI 10.1103/2rcd-dzcf | The foundational construction. Configuration-space CQ path integrals; complete positivity proved directly rather than through master equations; diffeomorphism-invariant CQ general relativity; purity conditional on the classical trajectory; no generation of entanglement by *local* CQ dynamics. |
| [[sources/arXiv-2402.17844v3.tar.gz\|arXiv-2402.17844v3]] | Grudka, Morris, Oppenheim, Russo & Sajjad, *Renormalisation of postquantum-classical gravity* | Maps the pure-gravity CQ path integral onto quadratic gravity; formal renormalisability without tachyons or negative-norm ghosts; positivity of the two-point function constrains the couplings; acceleration spectral density for tabletop tests. |
| [[sources/arXiv-2605.05375v1.tar.gz\|arXiv-2605.05375v1]] | Oppenheim & Sajjad, *Stochastic modes in postquantum classical gravity* | Linearises about Minkowski, performs a scalar-vector-tensor decomposition, identifies the stochastic degrees of freedom, and locates the indefinite sector. The most recent experimental window. |
| [[sources/arXiv-2402.19459v3.tar.gz\|arXiv-2402.19459v3]] | Oppenheim & Russo, *Anomalous contribution to galactic rotation curves due to stochastic spacetime* | The diffusion-regime proposal; anti-correlation between a linear metric term and a cosmological-constant term. Includes the authors' reply to the Hertzberg--Loeb arXiv comment. |
| [[sources/arXiv-2407.13820v2.tar.gz\|arXiv-2407.13820v2]] | Oppenheim, Panella & Pontzen, *Emergence of phantom cold dark matter from spacetime diffusion* | Diffusion drives the Hamiltonian constraint off its surface, positively on average; the violation gravitates as pressureless dust. |

The arXiv archives are LaTeX source packages; `main.tex` (or `PCDM.tex` for 2407.13820) carries the text, and the `.bib` files carry the upstream citation graph.

## Notation clash to watch

The published paper and the renormalisation paper write the decoherence--diffusion trade-off with the roles of the two coefficients transposed. The PRX writes $4D_0\succeq D_2^{-1}$, saturated at $4D_0=D_2^{-1}$; the renormalisation paper writes the saturation condition as $4D_2=D_1D_0^{-1}D_1$. Any formula copied between them must be checked rather than assumed.

## What is not here

The construction papers on which all five depend are cited but not mirrored: the original postquantum proposal, the classes-of-CQ-dynamics classification, the trajectories picture, the decoherence--diffusion trade-off paper, and the weak-field reduction. Any claim in this module resting on those is imported rather than checked here. The Hertzberg--Loeb comment (arXiv:2404.13037, a preprint) is likewise not mirrored, and is known only through the reply reproduced in 2402.19459v3.
