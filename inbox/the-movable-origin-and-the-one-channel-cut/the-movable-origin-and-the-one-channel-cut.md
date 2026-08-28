# The Movable Origin and the One-Channel Cut

The pasted derivation chain — $\iota_{A,c}=\pi/(H_ct_P)^2$, $G=\pi c^5/\hbar\iota_{A,c}H_c^2$, $\iota_A\,\alpha_G=\pi$ — is correct, and its own fourth step correctly concedes the circularity: fed a measured $H_c$, it reconstructs $G_N$ because $\iota_{A,c}$ was computed with $G_N$. This note identifies *what the needed construction actually is*, and it is not "derive $10^{122}$ from algebra." The obstruction already has a name in this vault: [[inbox/cosmodynamic-expansion-closure/typed-cosmic-ledger|the typed cosmic ledger]] records that the core wall returns relative trace capacity $\tau(e_N)=e^N$ **with a movable origin under weight rescaling**, and the radical-copernicanism audit named that mover: the trace-scaling module of the core. A scaling-covariant trace has no absolute count; only differences are invariant (receipt). So the needed construction is an **origin-fixer**, and there are exactly three typed candidates. The cheapest one collapses the problem: with the vault's own exact bookkeeping $d\ln\iota_A=2(1+q)\,dN$, the entire $10^{122}$ factors as $\iota_{A,c}=\iota_{\rm birth}\cdot e^{2\int(1+q)dN}$, and the single postulate $\iota_{\rm birth}=1$ — *the chain begins at the trivial inclusion* — makes the count a clock reading: $281.3$ nats $=257.8$ (radiation, $3.99$/e-fold over $64.6$ e-folds) $+23.5$ (matter+pulse, $3.00$/e-fold over $7.8$), receipted. Equivalently: $\alpha_G(H_{\rm birth})=\pi$ — gravity is order-$\pi$ at the one-channel cut, and both its present weakness and the $10^{122}$ are addresses, not constants. Receipts: `ledger_receipts.py` (numpy; 13 checks; nonzero exit on failure).

## 1. What the chain establishes, typed

Three receipted identities and one boundary. $\iota_A(H)\,\alpha_G(H)=\pi$ at *every* cut — the horizon ledger is the reciprocal gravitational coupling at the Hubble energy, which is the algebraic content of $S=A/4\ell_P^2$ rewritten per cut. The two calibration branches give $\iota_{A,c}=1.507\times10^{122}$ (this vault's CMB-conditional $H_c\simeq82.6$) and $1.321\times10^{122}$ (the Cepheid-calibrated $H_c=88.26$) — so **the Hubble tension is $0.13$ nats of crossing ledger** (receipt), a restatement, not a resolution. The round trip $G\to\iota\to G$ returns $G_N$ to $10^{-12}$ (receipt): reversal is calibration, not derivation — exactly as [[deriving-value-of-g/causal-scale-derivation-target|the anti-circularity list]] demands and as the packet's own fourth response already stated. Cross-checks of the packet pass: $H_0t_0=0.9518470$ on the benchmark; $H_c/H_0=E(z_c)=\sqrt{2\Omega_{X0}}\cosh x_c=1.2253$ at benchmark abundances, falling to $1.207$ at the Cepheid-fit $\Omega_m$ — the packet's two $H_c/H_0$ values are one $\Omega_m$-family, not a discrepancy.

## 2. Why the origin moves

"Derive $\iota_{A,c}$" is, as stated, a category mistake, and the vault has already recorded why in two registers. Operationally: the core wall's capacity is $\tau(e_N)=e^N$ with movable origin — rescaling $\tau\mapsto\lambda\tau$ shifts every $\ln\iota$ by $\ln\lambda$ and cancels in all differences (receipt). Structurally: the origin's mover is the **trace-scaling module** — for a type III$_1$ wall the core's trace is unique only up to the dual scaling flow, and the flow of weights is ergodic, so *no internal invariant of the algebra fixes an absolute count* [CITED — Takesaki duality; the radical-copernicanism notes own this vocabulary]. The replication obstruction of [[deriving-value-of-g/obstructions-to-an-unconditional-proof|the deriving-$G$ obstructions]] is the same fact in channel language. A derivation of the absolute ledger therefore requires an *additional* structure that breaks trace-scaling covariance. That is the construction we need, stated as itself.

## 3. The three origin-fixers

**(a) The II$_1$ completion.** If the wall family passes the half-sided-modular-inclusion gate (the radical-copernicanism gating question, [OPEN]), the modular crossed product exists [THEOREM], and with a charge spectrum bounded below the completion is type II$_1$: the trace is canonically normalized by $\mathrm{Tr}(\mathbf 1)=1$, and the ledger is counted *down* from the maximum as deficits — the CLPW-type theorem that renormalized trace differences equal generalized-entropy differences, $d\ln\mathrm{Tr}=dS_{\rm gen}/k_B$, is the existing literature derivation of "ledger $=$ area$/4G\hbar$" from algebra [CITED — verify before promotion]. But this origin sits at the *end*: it needs an asymptotic box, and [[causal-scale-theory/future-asymptotics|unit CST-B2 has none]] — the response coasts and acceleration exits. The II$_1$ fixer belongs to $\Lambda$CDM's future, not CST's.

**(b) The one-channel birth.** Fix the origin at the *start*: postulate that the wall chain begins at the **trivial inclusion** — index one, one channel, no distinctions; the initial object of the Jones tower, and the algebraic content of "nothing in particular." The vault's own mathematics for the rungs exists: [[deriving-g-v2/index-not-entropy|index-not-entropy]] retypes the ledger unit through the Watatani index, and [[hyperbolic-counting/inq|hyperbolic counting]] owns the Jones/ADE ladder with the affine wall at index four. This is the fixer developed in §4.

**(c) The external solder.** Fix the origin by a physical clock or record (the Chen–Penington route the radical-copernicanism inventory recommends when no exact KMS state exists) [CITED]. Honest, but it imports the datum this note is trying to type, so it is the fallback, not the construction.

## 4. The reduction theorem

The bridge is already in the vault and is exact: $d\ln\iota_A/dN=2(1+q)$ is *identically* $\iota_A\propto H^{-2}$, since $d\ln H/dN=-(1+q)$ ([[inbox/cosmodynamic-expansion-closure/typed-cosmic-ledger|the ledger note]] correctly calls it a reconstruction of shape, not a law; receipt: residual $10^{-12}$ over the full history). Therefore, for any choice of origin,

$$
\boxed{\;\iota_{A,c}
=\iota_{\rm birth}\cdot
\exp\!\Bigl(2\!\int_{\rm birth}^{c}(1+q)\,dN\Bigr),\;}
$$

and the whole content of the absolute count is the initial condition. Take fixer (b), $\iota_{\rm birth}=1$, which is equivalent to declaring the birth cut where $\alpha_G=\pi$ (receipt). Then, on the CMB-conditional background, the receipts return

$$
\ln\iota_{A,c}=281.31\ \text{nats}
=\underbrace{257.8}_{\text{radiation: }3.99\ \text{nats/e-fold}\times64.6}
+\underbrace{23.5}_{\text{matter+pulse: }3.00\times7.8},
$$

$72.5$ e-folds since the first cut. **The $10^{122}$ is not a constant of nature; it is the exponential of the causal history since the one-channel cut** — four nats per e-fold while radiation ruled, three under matter, read off at our address. This satisfies the anti-circularity list in the only way available: no measured $G$ enters *if* $t_P$ is defined by the birth cut rather than imported — that is, $G:=\pi c^5/\hbar H_{\rm birth}^2$ becomes the *definition* of the coupling by the chain's first rung, and its constancy is the statement that $\iota_A\propto H^{-2}$ exactly compensates the changing horizon (the packet's closing remark, now typed). One mystery replaces two: the smallness of $\alpha_G$ today and the size of the ledger are the same clock reading.

## 5. The theorem still owed, precisely

Fixer (b) is [CONSTITUTIVE CANDIDATE] until three gates close, all pre-existing in the vault: (i) the wall family is a chain of half-sided modular inclusions — the gating question, unresolved; (ii) the chain has a tower presentation whose initial object is the trivial inclusion, with [[wall-construction-interface/scale-character-solder|the scale-character solder]] sending tower depth to $\int(1+q)\,dN$ — this is where "one channel at the start" would stop being a postulate; (iii) the wall's trace capacity, BKM response, edge entropy, and geometric horizon entropy are soldered — the $\iota_{\rm wall}\overset{?}{=}\iota_A$ bridge the packet names, whose literature form is the crossed-product entropy theorem of fixer (a) [CITED — verify]. A sharp falsifier comes free from the Jones spectrum: if the tower's first rung is a nontrivial index $\lambda>1$, every count shifts by $\ln\lambda$ per rung, and below four the correction is *discrete* — $\lambda\in\{4\cos^2(\pi/n)\}$ — so a mismatch between the constructed and the calibrated ledger would be quantized, which is [[deriving-g-v2/index-not-entropy|index-not-entropy]]'s territory.

## 6. Obligations

1. Citations to verify before promotion: Takesaki duality / trace-scaling; the crossed-product generalized-entropy theorems (CLPW and successors); Wiesbrock's h.s.m.i. characterization; the Chen–Penington clock route.
2. The era breakdown uses the CMB-conditional carrier ($h=0.6784$, $\omega_m=0.1430$) — branch-dependent at the $0.13$-nat level, which *is* the Hubble tension in this register.
3. $\iota_{\rm birth}=1$ is constitutive until gate (ii); no claim that the algebra has selected it. The birth cut is *not* claimed to be a Planck-time event in the imported sense — it is defined by the chain, and $t_P$ inherits from it.
4. This note derives no new number; it relocates the underived number from "a $10^{122}$ count" to "the chain's first rung," which is smaller.
5. Receipts require numpy; stdlib rewrite owed on promotion.
