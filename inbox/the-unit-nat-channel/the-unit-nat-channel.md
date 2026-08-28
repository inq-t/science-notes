# The Unit-Nat Channel and the $\gamma$ Ladder

The last algebraic route to the carrier, performed. Its first finding dissolves a fit into a theorem: on the unit branch, $s_*$ is **not** a fitted quantity — [[deriving-g-v2/index-not-entropy|index-not-entropy]]'s own relation $\mathfrak R_c=\nu^2/s_*$ evaluated at the two unit principles $(\nu,\mathfrak R_c)=(1,1)$ forces $\boxed{s_*=1}$ exactly, with the reproduced profile ($\mathfrak R_c=1.014$, $[0.9416,1.0900]$) as its empirical check. Its second finding names the channel that carries exactly one nat: the **exponential state** — the KMS/thermal state of the unit-rate one-sided translation register, density $e^{-x}$ on $\mathbb R_+$, dual to the wall's own capacity $\tau(e_N)=e^N$ — whose differential entropy is $1-\ln\lambda$: convention-dependent (the movable origin, again) *until* the unit-rate principle fixes $\lambda=1$, whereupon $S=1$ nat exactly (receipt). The two unit principles and the unit-nat channel are one statement. With $s_*$ frozen, the only remaining unknown is the integer multiplicity $\gamma$, and the carrier prediction becomes a **parameter-free discrete ladder**:

$$
\boxed{\;\gamma\in\{1,2,3\}\;\Longrightarrow\;
m_*=59.48,\;47.21,\;41.24\ \mathrm{MeV}\ \text{(Cepheid)}
\;/\;58.19,\;46.18,\;40.34\ \text{(CMB branch)},\;}
$$

and the kill completes: **no standard scale sits within $9\%$ of any rung on either branch** (receipt; threshold set at 4%). Receipts: `unit_nat_receipts.py` (numpy; 8 checks; nonzero exit on failure).

## 1. $s_*$ was never free

The chain, each link owned: $\mathfrak R_c=\nu^2/s_*$ [index-not-entropy, conditional on channel additivity]; $\nu=1$ [[causal-scale-theory/unit-branch|the unit-rate principle]]; $\mathfrak R_c=1$ [the weak matching principle]. Composing: $s_*=1$ — a *consequence of the unit branch*, not a knob. The fitted $0.9861$ of the earlier notes was the pushforward of the measured $\mathfrak R_c=1.014$; its interval contains $1$, so the data are consistent with the forced value and add nothing to it. With $\zeta=\gamma s_*/3$ this pins $\zeta=\gamma/3$: the carrier closure $Gm_*^3=3\hbar^2H_c/(4\gamma c)$ has exactly one discrete unknown left.

The channel realizing $s_*=1$ is not exotic — it is the canonical state of the register the wall already owns. The one-sided translation structure ($\mathbb R_+$, the accessibility semigroup of the h.s.m.i. programme) has as its Gibbs state the exponential density $\lambda e^{-\lambda x}$, with $S=1-\ln\lambda$: the rescaling freedom is precisely the trace-scaling/movable-origin freedom of [[inbox/the-movable-origin-and-the-one-channel-cut/the-movable-origin-and-the-one-channel-cut|the origin note]], and the unit-rate principle is what breaks it. **One nat per channel is the entropy of the unit-rate exponential channel** (receipt to $10^{-6}$); the "selection question" of [[deriving-g-v2/inq|the second pass]] ("whether any algebraic principle selects $s_*=1$") is answered conditionally: the unit branch selects it, and the saturation value $\operatorname{Ind}\ge e^{2}$ follows.

## 2. The $\gamma$ ladder, and the completed kill

$\gamma$ counts channels per Compton cell, and the arc supplies exactly three structural candidates: $\gamma=1$ (one channel per cell — the literal reading); $\gamma=2$ (the accessible pair of the triple, the negative balancer excluded by Born positivity); $\gamma=3$ (the full triple, balancer included — and this rung *is* the ledger-level note's old $\zeta=1$ value $41.2$ MeV: the order-one window survives only here). The rungs are parameter-free per branch. Against the standard tables ($m_{\pi^\pm}$, $m_{\pi^0}$, $m_\pi/2$, $f_\pi$, $m_\mu$, $m_\mu/2$, $m_K/2$, $m_s(2\,\mathrm{GeV})$, $\Lambda_{\rm QCD}$, $m_e$, $m_p$, $\sqrt{m_em_p}$), the closest approach to any rung on either branch is $9.2\%$ (receipt). So, within the literal reading and the unit branch:

$$
\boxed{\text{the carrier is not a known particle scale at any small-integer multiplicity.}}
$$

Three outcomes remain, now sharply separated. Either the carrier is a **new capacity grain** at one of the six rung values — and the receipt states the falsifier in both directions: an independently constructed $47.2$ MeV grain at $\gamma=2$ would *confirm*, while an independently forced $70$ MeV grain would kill the unit branch itself, since no rung reaches it. Or $\gamma$ is a *dilution* ($\gamma<1$, channels rarer than cells), for which the required values have no algebraic owner — the two numerical sirens ($\gamma(m_{\pi^\pm})=0.0774$ against $1/4\pi$ at $2.8\%$ and $1/13$ at $0.6\%$) are receipted, flagged under the a-posteriori discipline, and **not used**. Or the literal spherical reading fails and the coefficient reverts to the general family of [[deriving-g-v2/closure-family-and-kills|the closure note]]. The route has done what algebra can do from the present axioms: it converted "a 40–63 MeV window at order-one conventions" into a six-value rigid ladder with no survivors among known scales.

## 3. The K-theoretic home, adopted

The Baum–Connes notes are adopted as the typing frame for what remains, with their guards intact: assembly transports, it does not select — a scalar needs a trace or cyclic-cocycle pairing; the modular $\mathbb R$-action needs only **Connes–Thom** ($K_i(A)\cong K_{i+1}(A\rtimes\mathbb R)$), not the open conjecture; and the one-sided $\mathbb R_+$ wall is *not* Baum–Connes territory at all — **Wiener–Hopf/Toeplitz, Deaconu–Renault, and Cuntz–Pimsner** machinery is the correct register. That last guard lands exactly on this note's finding: the unit-nat channel is the KMS state *of the Wiener–Hopf register*, so the prescribed machinery and the derived channel already live in the same algebra. The naturality square (assembly commuting with the wall correspondence $[W]\in KK$) is the K-theoretic form of the freezing law's "conserved while accessibility is lost," with a non-commuting defect typed as anomaly-candidate rather than flux; the three-shadow pairings $\langle x_{\rm wall},\phi_{\rm UV/hor/cos}\rangle$ are the K-theoretic form of the three reductions (birth rung / hierarchy / per-cell). The proposed primary-source module list (Baum–Connes–Higson; Connes–Thom; Connes–Skandalis; Le Gall; Tu; Higson–Lafforgue–Skandalis counterexamples; Muhly–Renault; Deaconu; Skandalis–Tu–Yu) is endorsed for `library/` intake under the library convention.

**The named next construction** — what would derive $\gamma$ rather than enumerate it: a Deaconu–Renault or Cuntz–Pimsner model of the wall chain (the $e^N$-scaling endomorphism as the Pimsner bimodule), whose $K_0$-class paired with the canonical gauge-invariant trace returns the **channel density per cell** — an integer or index, compared against the ladder. [OPEN CONSTRUCTION — the successor to this note.] Its discrete falsifier is already in place: a nontrivial first rung shifts the count by $\ln\lambda$, $\lambda\in\{4\cos^2(\pi/n)\}$, per the movable-origin note.

## 4. Obligations

1. $s_*=1$ is forced *given* the two unit principles and channel additivity; those premises carry their own open status ([[causal-scale-theory/unit-branch|unit-branch note]]: "neither unity follows from normalization convention or binary algebra"). The route converts a fit to a consequence, not to an unconditional theorem.
2. The $\gamma$ ladder assumes integer channels per cell; dilutions have no owner; the sirens are quarantined.
3. Differential entropy's convention-dependence is used, not hidden: the unit rate is the declared breaker of the rescaling freedom, and it is the same principle in both appearances.
4. The Wiener–Hopf/KMS identification of the unit-nat channel is typed at the density level; the operator-algebraic construction (the Toeplitz wall with its gauge trace) is part of the named next construction.
5. Baum–Connes-with-coefficients has counterexamples; any groupoid used must establish amenability or an equivalent hypothesis [their guard, adopted]. Citations for the module list to verify at intake.
6. Receipts require numpy; stdlib rewrite owed on promotion.
