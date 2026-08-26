# Deriving G, Second Pass: The G-Free First Law

The first pass, [[deriving-value-of-g/entry|deriving the value of G]], established what a derivation must construct and proved no-go lemmas against shortcuts. This second pass reorganizes the question around one typed observation: every thermal and modular quantity at a causal wall — Unruh temperature, Gibbons–Hawking temperature, Hawking temperature as surface gravity, the KMS period — is G-free, theorem-grade structure, while G lives entirely in the ledger that counts erased distinguishability. Written in the wall's own units the first law contains no G at all; G reappears only as the exchange rate between that ledger and its presentation as metric area. "The value of G" is then a statement about the grain of matter rulers, not about the strength of a force, and the no-gos of the first pass funnel into a single missing number plus a single alignment theorem. The 2026-08-26 session also produced two numerical kills — cosmological running of the modulus, and the entire rigid Jones series of wall channels — recorded here with receipts. Claim labels follow [[program-core/axioms-and-principles#Status vocabulary|the programme status vocabulary]] and its composition rule; nothing below outranks its weakest load-bearing edge.

## The argument in order

**1. The modular register is G-free.** **[STANDARD]** The temperature of an accelerated frame, of the de Sitter horizon, and of a black hole are all instances of one algebraic fact — modular flow with period $2\pi$ — and none of them contains $G$ except through the conversion of a *source* (a mass) into an *acceleration*. Every pure number in horizon thermodynamics ($2\pi$, $\tfrac14$, $8\pi$) is already fixed. [[the-modular-register-is-g-free]] performs the audit with sources.

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

**4. A matter scale must enter because rulers are matter.** **[EXACT — DIMENSIONAL LEMMA, plus INTERPRETATION]** The dimensional obstruction of the first pass is not an obstacle but an explanation: area is a matter-presented quantity, so any noncircular value of $G$ is necessarily relational to a chosen matter ruler. Per proton Compton cell the ledger holds $4.23\times10^{37}$ nats, whose square root is $m_P/2m_p$. The hierarchy problem, the weakness of gravity, and the value of $G$ are one sentence: rulers are coarse by that factor. [[rulers-are-matter]] owns the lemma and the numbers.

**5. The invariant is the index, not the entropy unit.** **[CONDITIONAL ON A REPORTED FIT]** The entropy-per-channel extracted from the reported matching-ratio fit, $s_*\in[0.92,1.06]$ nat, retypes multiplicatively as a Watatani/Jones index bound $\operatorname{Ind}\ge e^{2s_*}\approx e^2>4$. By Jones's theorem the index spectrum below 4 is a rigid quantized ladder whose entropies all sit at or below $\ln 2$; the fit therefore excludes the *entire* rigid series, places the wall inclusion in the continuum regime, and thereby explains why the gravitational constant is continuous rather than quantized. [[index-not-entropy]] states the assumptions, the ladder, and the kill conditions.

**6. The closure family is one-dimensional, and most of it is dead.** **[EXACT LEMMA plus EMPIRICAL KILLS]** At a homogeneous reference cut every macroscopic dimensionful datum reduces to $H_c$ or is circular through $G$, so every candidate closure has the form $\chi_*=C\,s_*\,R_c^{\,a}\lambda^{-(2+a)}$. Lunar laser ranging kills all live running with $|a|>0.005$ — including logarithmic running — leaving exactly two survivors: a pure-microscopic closure ($a=0$) and a fossilized cosmological closure frozen at the crossing. The four computed closures, their numbers, and the crossed-product circularity kill are in [[closure-family-and-kills]].

**7. G's native register is a rate.** **[STANDARD REARRANGEMENT]** The energy flux through the apparent horizon is $(-\dot H/H^2)\,c^5/G\approx2\times10^{52}\,\mathrm W$ — and $c^5/G$ is the unique $G$-combination containing no $\hbar$ and no length. Read with Noether's second theorem and the flow of weights, the "leak" is the monotone rescaling of the vacuum weight, not an emission into anything. [[the-leak-register]] owns this.

**8. Neighbouring theories, and the randomness firewall.** **[ADOPTED COMMITMENT]** Jacobson, Verlinde, Padmanabhan, and postquantum gravity are positioned in [[relation-to-entropic-and-postquantum-gravity]], which also states the programme's standing commitment: stochasticity is a fact about access, never an ontology. Where those theories say "random," this programme says "the necessitating reason for the fact is inaccessible from within" — with the Bell–Kochen–Specker discipline of [[sufficient-reason/two-species-of-reason|two species of reason]] preventing that commitment from collapsing into hidden value-assignments.

## Present verdict

The correctly typed question splits. The **law** question — prove $q=\delta\iota$ at the wall inclusion, with $\iota$ realized as the central edge ledger of [[spectral-wall-descent/entry|spectral wall descent]] — is G-free and entirely theorem-shaped; it is the first pass's same-tangent and edge-density welds in better variables. The **value** question — how many ledger units per ruler cell — is relational to matter by an exact dimensional lemma, and its two surviving closures are empirically distinguishable: the fossil closure ties $G$ to $H_c$ and a 40–63 MeV carrier through the frozen Weinberg relation, while the microscopic closure predicts no relation between $G$ and cosmology at all. The **selection** question — why the fitted index sits at the self-normalizing value $e^2$, one ledger unit per channel — is new, open, and stated at the end of [[index-not-entropy]]. Receipts for every number quoted in this module are in `receipts/`, run on this machine.

## Claim ledger

| Status | Content |
|---|---|
| Standard | Unruh, Gibbons–Hawking, and Hawking temperatures; KMS period; Clausius relation at horizons; Bekenstein–Hawking coefficient |
| Exact | The macroscopic collapse lemma at a homogeneous cut; the dimensional lemma; the closure-family parametrization; the type-I cell identity in the receipts |
| Conditional theorem | The G-free first law is equivalent to Einstein dynamics given the Jacobson premises; the index retyping given channel additivity and the unit rate branch |
| Reported-limited input | The matching-ratio fit 1.025 in [0.941, 1.088], inherited with its non-reproduced status from CST empirical status |
| Empirical kill | Live cosmological running of the modulus (LLR, factor 217 to 434, log-running factor 2.3); every maximally mixed rigid-ladder channel |
| Proposed interpretation | G as ledger-to-ruler exchange rate; the leak as weight rescaling; the ruler reading of the hierarchy |
| Adopted commitment | No ontic randomness: inaccessible necessitating reason, typed per the two-species distinction |
| Open | The wall inclusion itself; the same-tangent alignment; the fossil-vs-microscopic fork; the selection of index e² |
