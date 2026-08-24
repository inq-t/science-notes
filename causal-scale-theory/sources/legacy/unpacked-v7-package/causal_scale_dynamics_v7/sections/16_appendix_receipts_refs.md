# Receipt, data, and audit ledger

The accompanying script `receipts/receipts_v7.py` verifies the exact identities and benchmark values used in this note. The machine-readable output is `receipts/receipts_v7.json`; the expected field is

```json
"all_exact_residuals_zero": true
```

The receipts verify:

- binary moments and the BKM metric;
- affine-shape identities;
- Fisher length $\pi$;
- the Witten/Darboux factorization and zero mode;
- Hawking--Friedmann conversion;
- the dimension-dependent crossing fraction;
- the closed benchmark and radiation correction;
- present cosmography and the two acceleration transitions.

The package includes the earlier background-fit, direct-response, and economy-audit results used for the observational status section. These analyses use different baselines and are not combined as independent measurements.

The attached AI referee notes were used as adversarial inputs. Their useful results and rejected claims are recorded in the body. In particular:

- the cocycle argument for affine soldering was retained;
- the vertical/horizontal distinction was retained;
- the warnings about the sigma-model completion and response normalization were retained;
- conformal-weight integrality and the identification of a two-dimensional normal plane with a two-dimensional CFT were rejected.

# Epistemic status ledger

| statement | status |
|---|---|
| causal order fixes conformal geometry under standard hypotheses | standard theorem |
| scale as $\Gamma(\mathcal E[1])$ and scale tractor | standard conformal geometry |
| Einstein metric iff parallel scale tractor | standard theorem |
| trace-free tractor source equation | exact reformulation of GR |
| modular/gravitational boost-charge identity | physical unity principle, supported in controlled settings |
| fundamental normal chirality quotient | structural identification |
| affine cocycle law | conditional theorem from ratio dependence and measurability |
| $\vperp=1$ | fundamental representation choice |
| binary BKM metric $\sech^2\theta$ | exact after chirality reduction |
| scale--capacity number $\Ruble=1$ | fundamental equivalence principle |
| free-energy source law | constitutive definition motivated by relative entropy |
| Hawking--Friedmann conversion | exact horizon/Friedmann identity in the stated regime |
| closed homogeneous pulse | deduction from the preceding laws |
| Witten pair | exact internal horizontal construction |
| covariant perturbation theory | open |
| zero residual floor | global sector choice |
| sequestering completion | published candidate, not derived from the scale-capacity law |

# References

1. S. W. Hawking, A. R. King, and P. J. McCarthy, “A new topology for curved space-time which incorporates the causal, differential, and conformal structures,” *J. Math. Phys.* **17** (1976) 174.
2. D. B. Malament, “The class of continuous timelike curves determines the topology of spacetime,” *J. Math. Phys.* **18** (1977) 1399.
3. T. N. Bailey, M. G. Eastwood, and A. R. Gover, “Thomas’s structure bundle for conformal, projective and related structures,” *Rocky Mountain J. Math.* **24** (1994) 1191.
4. S. Curry and A. R. Gover, “An introduction to conformal geometry and tractor calculus, with a view to applications in general relativity,” [arXiv:1412.7559](https://arxiv.org/abs/1412.7559).
5. A. R. Gover, “Almost Einstein and Poincaré–Einstein manifolds in Riemannian signature,” *J. Geom. Phys.* **60** (2010) 182.
6. J. J. Bisognano and E. H. Wichmann, “On the duality condition for quantum fields,” *J. Math. Phys.* **17** (1976) 303.
7. H. Casini, M. Huerta, and R. C. Myers, “Towards a derivation of holographic entanglement entropy,” [arXiv:1102.0440](https://arxiv.org/abs/1102.0440).
8. R. M. Wald, “Black hole entropy is the Noether charge,” [arXiv:gr-qc/9307038](https://arxiv.org/abs/gr-qc/9307038).
9. T. Jacobson, “Thermodynamics of spacetime: The Einstein equation of state,” [arXiv:gr-qc/9504004](https://arxiv.org/abs/gr-qc/9504004).
10. T. Jacobson, “Entanglement equilibrium and the Einstein equation,” [arXiv:1505.04753](https://arxiv.org/abs/1505.04753).
11. D. L. Jafferis, A. Lewkowycz, J. Maldacena, and S. J. Suh, “Relative entropy equals bulk relative entropy,” [arXiv:1512.06431](https://arxiv.org/abs/1512.06431).
12. N. Lashkari and M. Van Raamsdonk, “Canonical energy is quantum Fisher information,” [arXiv:1508.00897](https://arxiv.org/abs/1508.00897).
13. B. Czech, L. Lamprou, S. McCandlish, and J. Sully, “Modular Berry Connection,” [arXiv:1712.07123](https://arxiv.org/abs/1712.07123).
14. B. Czech et al., “Changing states in holography: From modular Berry curvature to the bulk symplectic form,” [arXiv:2305.16384](https://arxiv.org/abs/2305.16384).
15. D. Petz, “Monotone metrics on matrix spaces,” *Linear Algebra Appl.* **244** (1996) 81.
16. N. N. Čencov, *Statistical Decision Rules and Optimal Inference*, AMS (1982).
17. S.-I. Amari and H. Nagaoka, *Methods of Information Geometry*, AMS/Oxford (2000).
18. M. R. Grasselli and R. F. Streater, “On the uniqueness of the Chentsov metric in quantum information geometry,” [arXiv:math-ph/0006030](https://arxiv.org/abs/math-ph/0006030).
19. R. Chatterjee, “Modular Self-Duality, Symmetrized Relative Entropy, and Bogoliubov–Kubo–Mori Susceptibility in Quantum Field Theory,” [arXiv:2605.19106](https://arxiv.org/abs/2605.19106).
20. K. Jensen, J. Sorce, and A. Speranza, “Generalized entropy for general subregions in quantum gravity,” [arXiv:2306.01837](https://arxiv.org/abs/2306.01837).
21. T. Faulkner and A. J. Speranza, “Gravitational algebras and the generalized second law,” [arXiv:2405.00847](https://arxiv.org/abs/2405.00847).
22. V. Chandrasekaran and É. É. Flanagan, “Subregion algebras in classical and quantum gravity,” [arXiv:2601.07915](https://arxiv.org/abs/2601.07915).
23. S. A. Hayward, “Unified first law of black-hole dynamics and relativistic thermodynamics,” [arXiv:gr-qc/9710089](https://arxiv.org/abs/gr-qc/9710089).
24. R.-G. Cai and S. P. Kim, “First law of thermodynamics and Friedmann equations of the Friedmann–Robertson–Walker universe,” [arXiv:hep-th/0501055](https://arxiv.org/abs/hep-th/0501055).
25. M. Akbar and R.-G. Cai, “Thermodynamic behavior of Friedmann equation at apparent horizon of FRW universe,” [arXiv:hep-th/0609128](https://arxiv.org/abs/hep-th/0609128).
26. J. de Boer, J. Järvelä, and E. Keski-Vakkuri, “Aspects of capacity of entanglement,” [arXiv:1807.07357](https://arxiv.org/abs/1807.07357).
27. T. Banks and K. M. Zurek, “Conformal description of near-horizon vacuum states,” *Phys. Rev. D* **104**, 126026 (2021), [arXiv:2108.04806](https://arxiv.org/abs/2108.04806).
28. T. Banks and P. Draper, “Generalized entanglement capacity of de Sitter space,” [arXiv:2404.13684](https://arxiv.org/abs/2404.13684).
29. D. Kastor, S. Ray, and J. Traschen, “Enthalpy and the mechanics of AdS black holes,” [arXiv:0904.2765](https://arxiv.org/abs/0904.2765).
30. N. Kaloper, A. Padilla, D. Stefanyszyn, and G. Zahariade, “A manifestly local theory of vacuum energy sequestering,” [arXiv:1505.01492](https://arxiv.org/abs/1505.01492).
31. N. Kaloper and A. Padilla, “Vacuum energy sequestering and graviton loops,” [arXiv:1606.04958](https://arxiv.org/abs/1606.04958).
32. A. Vikman, “Can dark energy evolve to the phantom?” [arXiv:astro-ph/0407107](https://arxiv.org/abs/astro-ph/0407107).
33. J. Lekner, “Reflectionless eigenstates of the $\sech^2$ potential,” *Am. J. Phys.* **75** (2007) 1151.
34. DESI Collaboration, “DESI DR2 results: measurements of baryon acoustic oscillations and cosmological constraints,” [arXiv:2503.14738](https://arxiv.org/abs/2503.14738).
35. DESI Collaboration, “DESI DR2 results: neutrino mass constraints,” [arXiv:2503.14744](https://arxiv.org/abs/2503.14744).
36. DESI Collaboration, “DESI DR2 Results IV: Ly$\alpha$-forest full-shape measurements and cosmological constraints,” [arXiv:2607.27410](https://arxiv.org/abs/2607.27410).
37. D. Brout et al., “The Pantheon+ analysis: cosmological constraints,” [arXiv:2202.04077](https://arxiv.org/abs/2202.04077).
38. X. Li and A. Shafieloo, “A simple phenomenological emergent dark energy model,” [arXiv:1906.08275](https://arxiv.org/abs/1906.08275).
39. L. Parker and A. Raval, “Vacuum-driven metamorphosis,” [arXiv:gr-qc/0312108](https://arxiv.org/abs/gr-qc/0312108).
40. J. Solà Peracaula et al., “Running vacuum in the Universe,” [arXiv:2203.13757](https://arxiv.org/abs/2203.13757).
