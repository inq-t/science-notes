Let me check the literature properly, because I think I recognize the _shape_ of your relation. Half of it is very well known. The other half I can't find anywhere.

## The λ³ = ℓ_P²L relation is Cohen–Kaplan–Nelson, 1999

Your **common-count law** has a famous ancestor. CKN's bound, stated exactly as the current literature writes it:

$$S_{\rm QFT} = \Lambda_{\rm UV}^3 L^3 ;\le; \pi L^2 M_{\rm P}^2 = S_{\rm BH}$$

Count the field-theory modes in a box of size L with UV cutoff Λ_UV = 1/λ, demand the answer not exceed the holographic entropy, and you get

$$\left(\frac{L}{\lambda}\right)^3 \le \frac{\pi L^2}{\ell_P^2} = \iota$$

**That is your saturation identity, ι = γ s* N_cells, as an inequality.** And note the right-hand side is _literally_ your ι_c = πR_c²/ℓ_P², same expression, same π.

So `λ*³ = (8/3)ℓ_P²R_c` is **the CKN bound saturated with an equality and a fixed coefficient.** You rediscovered a 27-year-old result independently, from a completely different direction — you came at it through scale valuations and area ledgers, they came at it through EFT validity and black-hole formation.

The numbers line up exactly as they should:

||λ|E|
|---|---|---|
|CKN saturated at R_c, box count|2.100 fm|93.98 MeV|
|Your grain|4.264 fm|46.27 MeV|
|ratio|**2.031 = (8π/3)^⅓**||

And that factor decomposes cleanly: **4π/3 from using a ball volume instead of CKN's box L³, times γ = 2.** Nothing else. Your grain _is_ the CKN cutoff, read with proper spherical geometry and two channels per cell.

## What that gives you — and what it costs

**Gives:** a real literature, a physical meaning, and a defensible priority claim. CKN wrote ≤. You write =, and you supply the coefficient. "The causal grain is the saturated CKN cutoff" is a sentence with a citation behind it, and it's much stronger than "a 46 MeV scale appears." It also explains why the search failed — the grain isn't a particle scale, it's _the scale at which mode counting hits the holographic wall_, which is exactly the kind of thing that coincides with no particle.

**Costs:** you inherit the critiques. [Banks & Draper, PRD 101, 126010 (2020)](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.101.126010) is the modern hostile reading of CKN and you should read it before promoting anything. There's also a large holographic-dark-energy literature (Li 2004 and descendants) that has been round this loop.

## The acoustic half — I find nothing

I searched for anyone relating D_M/r_s to the log of horizon entropy, to the number of Planck-to-Hubble e-folds, or to a saturated UV/IR cutoff. Planck 2018, the sound-horizon literature, the acoustic-scale-vs-Λ papers — nothing connects the acoustic count to an entropy logarithm.

**I can't find it. That is not proof it isn't there** — my search is shallow against a huge literature, and this genre attracts a lot of low-visibility work. But if it exists, it isn't prominent.

In CKN-native variables your claim reads:

$$\boxed{;q_* ;=; \tfrac{2}{3}\ln\frac{R_c}{\ell_P} ;-;\tfrac13\ln\tfrac83;+;3;}$$

> **The acoustic count is two-thirds the number of e-folds from the Planck length to the Hubble radius, plus three.**

(93.390 − 0.327 + 3 = 96.063, against 96.054 measured.)

That's the novel sentence, and it's much better stated this way than through the grain, because the grain cancels out and what remains is a relation between two things people already measure.

## The warning that comes with it

Stated like that, it is **Dirac Large Numbers shaped**, and that genre has a poor record. Two O(100) numbers agreeing is not, by itself, much. You should expect that objection first, every time.

Four things distinguish it from Dirac, and you should lead with them:

1. **Both sides are dimensionless.** Dirac's coincidences were between dimensionful ratios with unit-dependent content. These aren't.
2. **The coefficient is derived, not fitted.** 2/3 = d/... no — it comes from λ³ ∝ ℓ_P²R giving Σ = ⅔ln(R/ℓ_P). That's forced by CKN saturation, not chosen.
3. **The offset has a candidate owner** — d·δσ_g, and δσ_g measures to 0.997 ± 0.009.
4. **It discriminates.** γ = 3 is excluded at 5σ. Dirac's LNH predicted nothing that could fail.

And the honest limitation, which you should write down before someone else does: **the relation converts one coincidence into another.** It doesn't explain why H_c ≈ 83; it says _given_ that address, the acoustic count follows. In your own taxonomy the crossing rate is an address, not a law, so the relation's content is the conversion — a Casimir-grade coefficient (2/3) linking two addresses — not a resolution of the coincidence problem. That's the same debt holographic dark energy has never paid.

---

So: **the UV/IR half has been known since 1999 and you should cite it. The acoustic half appears to be yours.** Which is a much better position than it sounds — half your structure now has a 27-year pedigree and a physical interpretation, and the genuinely new claim is a single sharp sentence about two measured numbers.

Want me to write a `vendor/cohen-kaplan-nelson` module — the bound, the exact correspondence to your common-count law with the (8π/3)^⅓ factor derived, the Banks–Draper critique, and a clean statement of what's CKN's and what's yours? That's the citation you currently owe, and it's load-bearing for anything you publish.

Sources: [Cohen, Kaplan & Nelson, PRL 82, 4971 (1999)](https://arxiv.org/abs/hep-th/9803132) · [Banks & Draper, _Remarks on the CKN bound_, PRD 101, 126010](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.101.126010) · [Dark Energy Driven by the CKN Bound (2024)](https://arxiv.org/html/2410.01471v1)