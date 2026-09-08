---
inq.module: "deriving-g-v2"
inq.include:
  - "**/*.md"
inq.ambient:
  - "**/*.py"
  - "**/*.txt"
keywords: [gravitational-normalization, modular-temperature, horizon-first-law, edge-entropy, index, matter-rulers]
---
# Deriving G, Second Pass: The G-Free First Law

The first pass, [[deriving-value-of-g/inq|deriving the value of G]], established what a derivation must construct and proved no-go lemmas against shortcuts. This second pass separates the G-free KMS conversion in selected horizon-temperature laws from the normalization converting a dimensionless first-law ledger into metric area. A value of G then requires an independently normalized area density, matter rulers and a same-tangent alignment theorem. The calculations test specific running laws and conditional edge-cell models; extending the cell entropy bound to general subfactor indices remains a separate mathematical requirement.

Claim labels follow [[program-core/axioms-and-principles#Status vocabulary|the programme status vocabulary]]. The [[deriving-g-v2/sources|source record]] identifies the external inputs; [[deriving-g-v2/receipts/README|the calculation record]] distinguishes reproduced arithmetic from the wall and entropy hypotheses it cannot establish.

## The argument in order

**1. The selected horizon-temperature laws are G-free in geometric-rate form.** **[STANDARD, WITH SETTING-SPECIFIC HYPOTHESES]** Unruh, Gibbons–Hawking, and Hawking-as-surface-gravity temperatures are proportional to their appropriate geometric rates with KMS factor $2\pi$. Bisognano–Wichmann proves the modular identification for the Minkowski wedge; the other cases have their own QFT-on-curved-background hypotheses. $G$ enters when a source is converted into the geometric acceleration or when entropy is normalized per area. [[the-modular-register-is-g-free]] performs the audit with sources.

**2. Written dimensionlessly, the first law loses G.** **[CONDITIONAL — REFORMULATION]** Define the wall ledger $\iota:=S/k_B$ and heat in modular units $q:=\delta Q/k_BT$. The Clausius relation at a local causal horizon is then

$$
q=\delta\iota ,
$$

and by the Jacobson argument this single dimensionless law, imposed at every local wedge, is equivalent to the Einstein equation. $G$ does not appear in the law. [[the-g-free-first-law]] states the premises, the theorem, and the failure conditions.

**3. G is the ledger-to-ruler exchange rate.** **[PROPOSED INTERPRETATION]** $G$ enters only through the presentation $\iota=\eta\,A$ of the ledger as metric area:

$$
G=\frac{c^3}{4\hbar}\,\frac{\mathrm dA}{\mathrm d\iota}.
$$

The constant everyone measures is the *price of measuring the ledger with rulers*. This is the first pass's areal compliance, retyped as a statement about presentation rather than about gravity.

The mass-gap application in [[mass-scale-calibration/mass-and-g-as-dual-exchange-rates|mass and G as dual exchange rates]] shows exactly what further theorem this reading would need. If the horizon ledger and physical transfer-attenuation ledger are the same differential on every nonvacuum tangent, their two exchange rates compose to $m=(c/4G)\,\mathrm dA/\mathrm d\tau$. Positive $G$ alone does not imply a positive mass floor; the missing datum is a uniform lower ledger rate over the whole physical vacuum complement.

**4. A matter scale must enter because rulers are matter.** **[EXACT — DIMENSIONAL LEMMA, plus INTERPRETATION]** The dimensional obstruction of the first pass is not an obstacle but an explanation: area is a matter-presented quantity, so any noncircular value of $G$ is necessarily relational to a chosen matter ruler. Per proton Compton cell the ledger holds $4.23\times10^{37}$ nats, whose square root is $m_P/2m_p$. The hierarchy problem, the weakness of gravity, and the value of $G$ are one sentence: rulers are coarse by that factor. [[rulers-are-matter]] owns the lemma and the numbers.

**5. The type-I edge model bounds the cell dimension.** **[CONDITIONAL ON THE CHANNEL MODEL AND A REPRODUCED BACKGROUND PROFILE]** The conditional map $s_*=1/\mathfrak R_c$ sends the fully released 2025 direct unit-rate profile to $s_*=0.9861$ nat, with $\Delta\chi^2\le1$ range $[0.9175,1.0621]$. The exact product-edge bound $s_*\le\log d$ requires integer cell dimension $d\ge3$ even at the wider $\Delta\chi^2\le3.84$ contour. A maximally mixed qutrit lies outside the narrower contour but inside the wider one. Extending this test to the sub-4 Jones ladder requires an independently established half-log entropy–index bound; Jones's theorem does not supply it. [[index-not-entropy]] distinguishes the finite-cell result, the conditional subfactor comparison, and the additional equality needed to nominate $e^2$.

**6. Dimensional analysis gives a functional family; the computed power laws are a subfamily.** **[EXACT DIMENSIONAL FORM plus SCOPED EMPIRICAL KILLS]** With one macroscopic radius $R_c$, one microscopic length $\lambda$, and dimensionless data $\mathbf g$, the general form is $\chi_*=\lambda^{-2}F(R_c/\lambda;\mathbf g)$. The examples choose $F=C s_*(R_c/\lambda)^a$. Lunar laser ranging excludes the displayed unscreened live-running power laws with $|a|\gtrsim0.005$ and the particular logarithmic ansatz; it does not exclude every possible function, screened law, or threshold. The computed closures and crossed-product circularity test are in [[closure-family-and-kills]].

**7. G's native register is a rate.** **[STANDARD REARRANGEMENT]** The energy flux through the apparent horizon is $(-\dot H/H^2)\,c^5/G\approx2\times10^{52}\,\mathrm W$ — and $c^5/G$ is the unique $G$-combination containing no $\hbar$ and no length. Read with Noether's second theorem and the flow of weights, the "leak" is the monotone rescaling of the vacuum weight, not an emission into anything. [[the-leak-register]] owns this.

**8. Neighbouring theories, and the randomness firewall.** **[ADOPTED COMMITMENT]** Jacobson, Verlinde, Padmanabhan, and postquantum gravity are positioned in [[relation-to-entropic-and-postquantum-gravity]], which also states the programme's standing commitment: stochasticity is a fact about access, never an ontology. Where those theories say "random," this programme says "the necessitating reason for the fact is inaccessible from within" — with the Bell–Kochen–Specker discipline of [[sufficient-reason/two-species-of-reason|two species of reason]] preventing that commitment from collapsing into hidden value-assignments.

## Present verdict

The correctly typed question splits. The **law** question is to construct a wall ledger and prove the G-free Clausius equality $q=\delta\iota$ on the supplied local-horizon geometry; this is the first pass's same-tangent and edge-density work in better variables. The **value** question is how many ledger units occur per independently normalized ruler cell. Within the illustrative monomial family, a fossil Weinberg closure ties $G$ to $H_c$ and a 40–63 MeV carrier, while the microscopic spectral closure does not; more general functions remain open. The **selection** question is whether any algebraic principle selects the candidate value $s_*=1$ and hence, under the additional saturation hypotheses, $\operatorname{Ind}=e^2$. The reproduced background profile is compatible with that value but does not establish it. Receipts prove the declared arithmetic only.

## Claim ledger

| Status | Content |
|---|---|
| Standard | Unruh, Gibbons–Hawking, and Hawking temperatures; KMS period; Clausius relation at horizons; Bekenstein–Hawking coefficient |
| Exact | The dimensional functional form under declared inputs; the dimensional obstruction; the type-I product-edge/tracial identity in the receipts |
| Conditional theorem | The G-free first law is equivalent to Einstein dynamics given the Jacobson premises; the product-cell dimension bound given channel additivity, the unit-rate branch and the reproduced profile |
| Reproduced background input | On the unit-rate branch, the fully released 2025 profile gives $\mathfrak R_c=1.014104$ with contours $[0.941572,1.089954]$ at $\Delta\chi^2\le1$ and $[0.875271,1.165563]$ at $\Delta\chi^2\le3.84$; this remains a model-restricted background result |
| Empirical or conditional exclusion | The declared unscreened live-running laws (LLR, factors 217 to 434; the displayed log ansatz, factor 2.3); the sub-4 Jones ladder only with an additional half-log entropy bound and the channel/profile hypotheses; a maximal qutrit is mildly disfavored, not excluded at the wider contour |
| Proposed interpretation | G as ledger-to-ruler exchange rate; the leak as weight rescaling; the ruler reading of the hierarchy |
| Adopted commitment | No ontic randomness: inaccessible necessitating reason, typed per the two-species distinction |
| Open | Lorentzian realization of [[wall-construction-interface/core-spectral-wall|the core pre-wall]]; the same-tangent weld between finite-corner trace-capacity, whole-core response, edge data, and area; the fossil-vs-microscopic fork; selection of \(\varphi,d,\nu\) and, under separate finite-index hypotheses, the value \(e^2\) |
