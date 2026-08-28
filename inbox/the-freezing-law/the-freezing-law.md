# The Freezing Law

The conservation half of the freezing law was already in the vault, one module over: [[conservation-of-causal-charge/two-channel-conversion-law|the two-channel conversion law]] proves $\tfrac{d}{dN}(C_++C_-)=0$ with the normalized balance $m^2+\tfrac1\nu\tfrac{dm}{dN}=1$, and the sech$^2$ pulse is *forced* as the conversion current of that conserved binary total — "not inserted as a force profile." What this note adds is the typed answer to the guiding intuition (the "grander symmetry" that replaces time-translation is not a spacetime symmetry at all — it is a **Casimir**, conserved by representation arithmetic, plus the leak register's weight rescaling), three exact balance receipts the intuition predicted (zero horizon free energy at every cut; zero *net* heat of the pulse over all history; strictly monotone ledger), the assembled freezing law with its Kill-1 evasion, and the honest form of "negative probability balances" (a conserved indefinite Wronskian current along scale, and Wigner negativity — receipted — with the octonionic wave-function typed as the open target). Two links in the chain are corrected: acceleration is an entropy-production *dip*, not a speedup, and the ledger is areal, not volumetric. Receipts: `freezing_receipts.py` (numpy; 14 checks; nonzero exit on failure).

## 1. The chain, typed

| Claim | Typed form | Verdict |
|---|---|---|
| conservation of energy is time symmetry | Noether I; FLRW has no timelike Killing vector | [STANDARD] — energy conservation genuinely fails |
| the cosmos leaks; the symmetry is *something else* | the leak = monotone weight rescaling ([[deriving-g-v2/the-leak-register|Noether II register]]); the surviving invariant = the binary **Casimir** $1=m^2+dm/dN$ | [THEIRS + typed here] |
| more past = more entropy | $d\ln\iota_A=2(1+q)\,dN$ with $1+q>0$ everywhere on the unit branch | [THEOREM — receipt: $\min(1+q)=0.663$] |
| more entropy = faster expansion | acceleration is the production **dip**: $4\to3\to1.33\to2$ nats/e-fold | [CORRECTED — receipt] |
| entropy up, temperature down ⟹ volume up | $E_H=T_HS_H$ exactly; $S\propto R_A^2$ | [CORRECTED to *area* — the vault's native $L^{-2}$ register] |
| negative probability balances | conserved indefinite Wronskian current; Wigner negativity with positive marginals | [STANDARD — receipts]; octonionic version [OPEN] |

## 2. Three exact balances

**The Casimir.** On the unit branch $m=\tanh u$: $m^2+m'=1$ identically, endpoints $m(\mp\infty)=\mp1$, the crossing the balanced cut $m=0$ where the conversion rate is maximal (receipts). In density form the same law reads $\rho_X\cosh^2u=\mathrm{const}$ — an **inversion charge**, invariant under $u\mapsto-u$ ($a\mapsto a_c^2/a$), whose fixed point is the crossing; the far-future $a^{-2}$ dilution of [[causal-scale-theory/future-asymptotics|future asymptotics]] and the far-past $a^{+2}$ growth are its two mirror faces. Per [[conservation-of-causal-charge/inq|the module's own typing]], this is conservation by *representation invariant*, exactly the case its entry warns must not be forced into the word "symmetry": no continuous time action is needed, and none survives.

**Zero free energy.** At every flat-FLRW cut, $F_H=E_H-T_HS_H=0$ *identically* (receipt): $E_H=c^5/2GH$ grows, $T_H\propto H$ falls, $S_H\propto H^{-2}$ grows, and the books close as $dE=T\,dS+S\,dT$ with $dF=0$. The "leak" is not lost down a drain; it is the entropy payment, and the payment is exact — the intuition's *it balances*, at the horizon register.

**Zero net heat.** The pulse's Clausius heat integrates to zero over the complete history: $\int_{-\infty}^{\infty}3(1+w_X)\rho_X\,dN=0$ by odd $\times$ even (receipt: $10^{-16}$, each half $=\rho_{\mathrm{crit},c}/2$). **The phantom era borrows exactly what the quintessence era repays.** The response is not a source or a sink over its whole life; it is a *loan*, peaked at the crossing.

## 3. The freezing law, assembled

$$
\boxed{
\begin{aligned}
&\textbf{Conservation:}\quad \tfrac{d}{dN}(C_++C_-)=0
&&\text{[THEOREM — two-channel conversion law]}\\
&\textbf{Selection:}\quad \text{read at the balanced cut } m=0
&&\text{[the inversion fixed point; allocation-symmetric]}\\
&\textbf{Weld:}\quad C_++C_-\;\mapsto\; n\cdot s_*\;\overset{?}{=}\;\iota_{A,c}
&&\text{[OWED: carrier, }\zeta\text{, per index-not-entropy]}
\end{aligned}}
$$

$G$ then reads a **conserved charge at its canonical cut**: $G=\pi c^5/(\hbar H_c^2\,\iota_{A,c})$ with $\iota_{A,c}$ the frozen total, not the instantaneous horizon count. Kill 1 is evaded *by type*: $\dot G=0$ because $\dot C=0$, even while $\iota_A(N)=\pi/(Ht_P)^2$ keeps growing — the growing horizon ledger and the frozen conversion total are different objects that coincide once, at the crossing, which is the fossil claim of [[deriving-g-v2/closure-family-and-kills|closure A]] stated as a conservation law rather than a coincidence. Why the crossing and no other cut: it is the unique fixed point of the inversion, the response maximum, the balanced allocation $m=0$, and the equal-partition cut — four selections, one point. What the law does *not* yet do: derive the magnitude of $C$ (that is the level of [[inbox/the-ledger-level/the-ledger-level|the ledger-level note]] — carrier and $\zeta$ unchanged) or prove the weld from the wall algebra.

## 4. The production profile, and one flagged near-coincidence

The ledger grows at $2(1+q)$ nats per e-fold: $3.999$ deep in radiation, $3.016$ in matter, dipping to $1.326$ in the acceleration episode, recovering to $2.000$ on the coast (receipts) — so [[hyperbolic-counting/inq|hyperbolic counting's]] "two nats per horizon e-fold" is the pulse's *future asymptote*, and de Sitter (production zero, ledger frozen at the maximum) is exactly what unit CST-B2 declines to reach. Acceleration is the ledger catching its breath, not speeding up — the corrected arrow. One receipt is flagged rather than built upon: on the benchmark background, **today sits $0.0008$ e-folds from the production minimum** ($u_{\min}=0.2932$ vs $u_0=0.2940$; equivalently $j_0\approx q_0+2q_0^2$ to $1\%$). This is $\Omega_m$-dependent, coincidence-grade, and the Mercury note's a-posteriori warning applies in full. It is recorded, not used.

## 5. The wave-function register

Three exact senses in which "negative probability balances," in ascending strength. *Classical*: the balance is carried by the **signed allocation** $m\in[-1,1]$ — the "negative" side is the other channel, and $1+w_X\propto m$ changes sign at the crossing: the phantom half *is* the negative-flux branch. *Semiclassical*: the cosmic Schrödinger equation conserves an indefinite current — the Wronskian of $\hat H\psi=m\psi$ is $a$-independent (receipt: drift $7\times10^{-4}$ across the exterior region) — the honest WDW "negative probability," whose two signs are the expanding and contracting branches, and which the dust clock resolves into the positive Born-dwell of the functor note. *Quantum*: a wave function's phase-space density genuinely goes negative while marginals stay positive and the total balances to one — receipted on the first excited state ($\min W=-1/\pi$, $\iint W=1$). What does **not** yet exist is the octonionic version: the Freudenthal phase space carries the two prerequisites (an invariant symplectic form; Freudenthal duality with $\tilde{\tilde x}=-x$ as an almost-complex candidate), so "a good wave-function on the normalized phase space" is a well-posed [OPEN CONSTRUCTION] — the quantization of $\mathfrak M(\mathfrak h_3(\mathbb O))$ — and nothing in this note pretends to have built it.

## 6. Obligations

1. The conservation and selection legs are theorems (theirs and receipted); the weld leg carries the whole remaining burden and inherits the ledger-level note's debts: the carrier, $\zeta$, and the count-to-$\iota_{A,c}$ identification.
2. The Casimir is conserved *within the response sector*; the claim that the same total is what $G$ reads is the fossil hypothesis, [CONSTITUTIVE] until the weld exists. Matter–response energy exchange beyond the declared conservation split would break the law and is its falsifier.
3. The near-coincidence in §4 is recorded under the a-posteriori discipline; no selection principle is claimed from it.
4. The horizon balance $F_H\equiv0$ uses the Gibbons–Hawking temperature at the flat apparent horizon [STANDARD, with the usual caveats on dynamical-horizon temperatures].
5. Receipts require numpy; stdlib rewrite owed on promotion.
