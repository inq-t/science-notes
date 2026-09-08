# Mass-Scale Rhyme Sweep

The causal-grain rhyme sweep tests numerical matches to Yang–Mills and QCD scales against an empirical negative control, unit changes, and correlation lengths. No match in its declared factor family survives as evidence for a physical mass-gap mechanism. The later factor \(36\) was outside that search and remains a separate post-search proposal.

The [[causal-grain-cosmology/receipts/rhyme_sweep.py|rhyme-sweep calculation]] uses only the standard library and exits nonzero on a failed check. Its [[causal-grain-cosmology/receipts/rhyme-sweep-output.txt|stored sweep output]] records the tested family and controls. The finer census in [[the-grain-of-causal-scale/inbox/the-grain-in-every-register/entry|the grain-in-every-register history]] found about forty-two candidate coincidences per nat and explicitly quarantined the \(f_\pi/2\) siren; this ledger is its QCD-restricted, branch-aware companion. The later factor \(36\) is discussed in [[the-grain-of-causal-scale/inbox/causal-grain-and-the-yang-mills-gap/entry|the causal-grain gap packet]]. [[algebra/a2-weyl-radial-operator|The compact \(SU(3)\) radial audit]] adds a structural negative control: Weyl degree does not become the compact radial spectral gap.

## What was swept

The reduced-Compton mass presentation \(m_*=\hbar/(c\lambda_*)\) of the common-count scale on its two crossing branches — \(46.27\,\mathrm{MeV}/c^2\) (CMB-conditional, fixed physical densities) and \(47.21\,\mathrm{MeV}/c^2\) (Cepheid-conditional), both diagnostic inversions per [[the-grain-of-causal-scale/inq|the grain module]] — against twenty-one scale entries: two lattice determinations of the \(0^{++}\) glueball (1653 and 1730 MeV) and the \(2^{++}\); the string tension; \(\Lambda_{\overline{\mathrm{MS}}}\) at \(n_f=0,3,5\); \(f_\pi\) in both the 92- and 130-MeV conventions; both pion charge states, the kaon, eta, rho and proton; \(m_p/3\); the strange and light quark masses; the chiral scale \(4\pi f_\pi\); and the electron and muon masses as controls. The receipt compares the corresponding rest-energy numbers \(m_*c^2\). Forty-six distinct factors are tried: integers and their inverses to twelve, \(n\pi\) and inverses to six, \(\pi^2\), \(2\pi^2\), \(4\pi^2\), \(\sqrt2\), \(\sqrt3\), \(3/2\), \(2/3\), \(8/3\), \(3/8\), \(e\), \(e^2\), with coincident values deduplicated. Tolerance one percent. Total 1932 trials. The entries are deliberately correlated — two \(0^{++}\) values, two pions, two \(f_\pi\) conventions differing by \(\sqrt2\), \(m_p\) and \(m_p/3\) — so 1932 overstates the independent count; the empirical control below does not depend on that count.

## Result

| Quantity | Value |
|---|---|
| trials | 1932 |
| hits under 1% (CMB branch, Cepheid branch) | 7 (4, 3) |
| analytic expectation, log-uniform ratios over \([0.1,100]\) | 5.6 |
| two-sided Poisson tails \(P(N\le7)\), \(P(N\ge7)\) | 0.80, 0.33 |
| hits surviving both branches | **0** |
| empirical control: 4000 theory-free grains, log-uniform in \([20,200]\,\mathrm{MeV}\) | mean 2.79 hits per grain; central 95% interval \([0,7]\) |

The tolerance sensitivity is:

| Quantity at 5% | Value |
|---|---|
| hits per branch | 15, 15 |
| pairs surviving both branches | 10 |
| empirical control | mean 13.61 hits per grain; central 95% interval \([7,19]\) |

The seven hits are \(m_*\times2\approx f_\pi\), \(m_*\times3\approx m_{\pi^+}\), \(m_*\times3\pi\approx\sqrt\sigma\), \(m_*\times2\approx m_s\) on the CMB branch, and \(m_*\times7\approx\Lambda^{(3)}_{\overline{\mathrm{MS}}}\), \(m_*\times2\pi^2\approx m_p\), \(m_*/7\approx m_u+m_d\) on the Cepheid branch. The first is the already-quarantined \(f_\pi/2\) siren of the grain-in-every-register census; at the declared one-percent tolerance it does not survive the Cepheid branch. The two one-percent lists are disjoint. The branch spread is two percent, wider than that tolerance, so the closure cannot presently state a *branch-independent one-percent* coincidence. The observed counts, four and three, sit inside the central interval of theory-free grains, and the empirical mean of 2.79 hits per grain reproduces the analytic base rate of 2.80.

That zero is tolerance-specific. At five percent, \(2m_*\approx f_\pi(92)\) and nine other entries survive both branches. Each real branch has fifteen hits, still inside the corresponding control interval \([7,19]\). The broader-tolerance counts must therefore be judged against that broader base rate rather than imported into the one-percent result.

## The unit-artifact trap

\(\ln(m_P/m_*)=47.02\) on the CMB branch and \(47.00\) on the Cepheid branch, while \(m_*/\mathrm{MeV}=46.27\) and \(47.21\). The Cepheid agreement is \(0.4\%\). The log is dimensionless by construction; the count is a number of MeV and becomes \(0.047\) in GeV while the log does not move. There is nothing for a receipt to assert here — the invariance is arithmetic — so the receipt reports both quantities in both unit systems and asserts nothing. This is the most seductive number in the neighbourhood and it carries no information; it is recorded so that it stops being rediscovered.

## The correlation-length mismatch

The lightest state resolved in the pure-\(\mathrm{SU}(3)\) lattice spectrum is the \(0^{++}\) glueball, so the numerical gap candidate has correlation length \(\hbar c/m_{0^{++}}\approx0.11\)–\(0.12\,\mathrm{fm}\). The grain is \(\lambda_*\approx4.18\)–\(4.26\,\mathrm{fm}\) across the two branches. The ratio is thirty-five to thirty-seven, and the error is in the wrong direction for the grain to be the confinement scale: it is far too coarse. Deep inelastic scattering resolves structure three orders of magnitude below the grain. The receipt reports the ranges and asserts only that they fall where the prose says.

The declared factor family tested integers only through twelve. The proposal to inspect \(36=(-\partial_N\log|\mathfrak D_{A_2}|)^2\) was made after this thirty-five-to-thirty-seven mismatch was known, so it is not a surviving hit or an out-of-sample prediction of the sweep. Its only legitimate upgrade path is a pre-registered operator mechanism plus held-out dimensionless spectral ratios.

## Limits of the comparison

The sweep compares a cosmological diagnostic inversion — a number obtained by inserting measured \(G\) and \(H_c\) — against laboratory scales, which the grain module's own falsifier ("the line center is selected only by inserting measured \(G\) and then rediscovered") already forbids as evidence in either direction. A null result is therefore the only admissible outcome and does not by itself bear on the grain. The scale entries carry lattice and scheme uncertainties of several percent (glueballs, \(\Lambda\), \(\sqrt\sigma\)), so the one-percent tolerance is stricter than some inputs. The analytic chance model assumes log-uniform ratios and independent trials, neither exactly true; that is why the empirical control is the load-bearing comparison. At one percent no pair survives both branches; at five percent several do, and both the real and control counts rise. Branch stability is therefore not a tolerance-independent kill. The grain-in-every-register census uses a broader candidate set and reaches the same quarantine by a different route.

## What would change the conclusion

What each failure would kill:

| Failure | Kills |
|---|---|
| a coincidence surviving both branches at sub-percent level after the branch spread is resolved | the null result of this ledger, not the grain; it would enter the existing siren census, not become a claim |
| an independently constructed grain predicting \(m_{0^{++}}/\sqrt\sigma\) or \(m_{2^{++}}/m_{0^{++}}\) with no \(G\), \(H_c\), or unit input | [[contemporary-puzzles/yang-mills-mass-gap/mass-gap-no-gos#NG3 — Dimensionless data cannot supply the yardstick|NG3]]'s presumption that the programme has nothing to say here — this is the only admissible form of a positive result |
| a vault gap mechanism that survives removal of \(\lambda_*\) | [[contemporary-puzzles/yang-mills-mass-gap/mass-gap-no-gos#NG1 — A fixed-cutoff gap is insufficient|NG1]]'s presumption; it would then have to face the dilation and reconstruction tests in the same note |
| the unit-artifact reappearing as a claim anywhere in the vault | the vault's own discipline, not any physics |
