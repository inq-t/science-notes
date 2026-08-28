# $H_0$: Width, Address, Anchor

A principled derivation of $H_0$ splits, under this vault's own typing, into exactly three questions, and the sech$^2$ intuition turns out to be right about two of them. **Width**: the function sech$^2$ is not merely CST's response shape — it is *exactly* the de Sitter lapse in its own tortoise coordinate, with width $1/H$; the Hubble rate's native $T^{-1}$ is the width of the box read in causal depth, and the near-Nariai wave potential is exactly Pöschl–Teller with width $1/\kappa$. **Address**: on [[causal-scale-theory/unit-branch|the unit branch]], $H_0$ is not a constant of nature but the reading of the pulse at our position — one closed-form relation ties $(H_0,\omega_m,w_0)$ together with no free parameter, and the CMB-conditional conversion that [[causal-scale-theory/data-consistency|data-consistency]] names but does not compute comes out $H_0\simeq67.8\;\mathrm{km/s/Mpc}$. **Anchor**: the one dimensionful input can never come from structure alone (the same grammar as the deriving-$G$ obstruction), and $H_0t_{\mathrm P}\sim10^{-61}$ is the count still owed. Consequence, receipted: the pulse *raises* the CMB-anchored $H_0$ by only $+0.5$, so **the Hubble tension is not derivable from sech$^2$** — it stands as a falsifier fork, not a child, of the pulse. Receipts: `h0_receipts.py` (numpy; 16 checks; nonzero exit on failure).

## 1. Typing the request

$H_0$ is dimensionful, $T^{-1}$. No manipulation of dimensionless structure produces it, for the reason [[deriving-value-of-g/obstructions-to-an-unconditional-proof|the deriving-$G$ obstruction note]] already owns: constants $c,G,\hbar$ supply one time, $t_{\mathrm P}$, and the object needing explanation is the pure number $H_0t_{\mathrm P}\simeq1.19\times10^{-61}$ (receipt). So a principled account must factor as

$$
H_0=\underbrace{\text{one anchor}}_{\text{a }T^{-1}\text{ the theory owns}}\times\underbrace{\text{a dimensionless shape at our address}}_{\text{derivable}},
$$

and the *tension* — $73.04/67.4=1.083$, dimensionless — is the only $H_0$-adjacent quantity that could be pure structure. The receipts below settle what the sech$^2$ structure actually delivers for each factor.

## 2. Width: the three exact sech$^2$'s

The vault owns one sech$^2$ ([[causal-scale-theory/theorems/rigid-sech-response-identities|the rigid pulse]], [[binary-information-geometry/balanced-exponential-family|the balanced binary metric]]). There are two more, and they are exact theorems of the box rather than motifs:

- **The de Sitter lapse is sech$^2$.** In the static patch, $r=L\tanh(r_*/L)$, so $f=1-r^2/L^2=\operatorname{sech}^2(r_*/L)$ *identically* (receipt). The box, expressed in its own causal depth, is one sech$^2$ pulse of width $L=c/H$: **$H$'s native $T^{-1}$ is a sech$^2$ width.**
- **The near-Nariai potential is Pöschl–Teller.** Between the two horizons the wave potential converges to $V_0\operatorname{sech}^2(\kappa r_*)$, receipted at residuals $1.7\times10^{-2}\to5.4\times10^{-3}\to7.8\times10^{-4}$ as $m/m_N\to1$, with fitted width times surface gravity $\to1.00144$. At the $A_2$ fold of the earlier notes, the box's resonance problem *is* the sech$^2$ problem, and its width is again a $T^{-1}$: $\kappa$.
- **The pulse.** Conservation integrates $w=-1+\tfrac23\nu\tanh(\nu x)$ to $\rho_X\propto\operatorname{sech}^2(\nu x)$ exactly (receipt) — CST's density is a sech$^2$ of unit width *in e-folds* on the unit branch.

Three registers — causal depth $r_*$, tortoise resonance, e-fold time $N$ — one function, each width a Hubble-type rate. This is typed as a **[MOTIF — solder owed]**: same function, different carriers; the escort-tangent discipline forbids identifying them without a constructed map. What is *not* a motif is each individual identity, which is exact.

## 3. Address: the relation, and the benchmark recovered

On the unit branch with equal partition at the crossing, flatness gives the closed-form background of [[causal-scale-theory/generalized-background|CST-B2]], and the receipts reproduce the vault's benchmark to seven digits from the crossing condition alone: $x_c=0.2940066$, $z_c=0.3417927$, $w_0=-0.8094545$, $w_a=-0.6122053=-\tfrac23\operatorname{sech}^2x_c$, $q_0=-0.3369025$. Radiationless, the relation inverts in closed form:

$$
\boxed{\;\Omega_m=\frac{1}{1+e^{3x_c}\operatorname{sech}^2x_c},
\qquad
x_c=\operatorname{artanh}\!\Bigl(\tfrac32(1+w_0)\Bigr),
\qquad
H_0=100\sqrt{\omega_m\bigl(1+e^{3x_c}\operatorname{sech}^2x_c\bigr)}\;\tfrac{\mathrm{km/s}}{\mathrm{Mpc}}.\;}
$$

One equation linking three measured numbers $(H_0,\omega_m,w_0)$ with **no parameter free** — the unit branch's testable $H_0$ relation. What it says philosophically is the Copernican point: $H_0$ is *indexical*. The constants of the theory are the pulse and its anchor; $H_0$ is the pulse read at the address $x_c$ e-folds past the crossing. Asking "why is $H_0$ what it is" decomposes into "why this pulse" (structure), "why this anchor" (§5), and "why are we at this address" — and the third is not a physics question, which is precisely why $H_0$ resisted derivation.

## 4. The CMB-conditional $H_0$, and the tension verdict

[[causal-scale-theory/data-consistency|Data-consistency]] states that the shape fits "neither resolve nor aggravate the Hubble tension by itself" and that an absolute $H_0$ needs an imported ruler. Here is that conversion, computed differentially so pipeline systematics cancel: hold $(\omega_m,\omega_r)$ fixed at the Planck carrier values, require unit CST-B2 to reproduce flat $\Lambda$CDM's comoving distance to $z_*=1089.9$ (same code both sides; the pipeline re-solves $\Lambda$CDM to $h=0.6736$ exactly), and solve for $h$. Result [CARRIER-CONDITIONAL — the type declared in [[causal-scale-theory/observables|observables]]]:

$$
\boxed{\;H_0^{\text{unit CST-B2}\,|\,\mathrm{CMB}}=67.84\;\mathrm{km/s/Mpc},\qquad
\Omega_m=0.311,\quad z_c=0.342,\quad w_0=-0.810,\quad t_0=13.72\;\mathrm{Gyr}.\;}
$$

Three receipted facts fix the interpretation. The pulse is *invisible at recombination* ($\rho_X/\rho_{\mathrm{tot}}(z_*)\sim10^{-14}$): it has no early-time lever on $r_s$. Its $H(z)$ sits $+2\%$ above $\Lambda$CDM at $z\approx0.2$–$0.5$ and $-1.5\%$ below at $z\approx2$ (at equal $H_0,\omega_m$) — a falsifiable shape signature for DESI-class $H(z)$ data. And the net effect on the acoustic conversion is $+0.48$ km/s/Mpc — the right direction, one-tenth the size: the residual gap to SH0ES is $5.2$ km/s/Mpc $=5.0\sigma$ in SH0ES's own error. So:

$$
\boxed{\text{the Hubble tension is not derivable from the sech}^2\text{ structure; it is a falsifier fork of the pulse.}}
$$

Fork stated: either the local ladder carries systematics, or unit CST-B2 must buy its $H_0$ the way [[causal-scale-theory/receipts/fit-calibrated-background|the vault's own calibrated receipt]] already prices it — $r_d\simeq136$ Mpc and $t_0\simeq12.62$ Gyr — which is early-time physics the pulse does not supply. A principled derivation of the *tension* from CST would require the covariant perturbation sector or a recombination-side mechanism; neither exists in the vault, and this note constructs neither.

## 5. Anchor: whose $T^{-1}$ is it?

The theory's own rate is not $H_0$ but the crossing rate: $E(z_c)^2=2\Omega_{X0}\cosh^2x_c$ (receipt), so

$$
H_c=1.218\,H_0\simeq82\;\mathrm{km/s/Mpc},
\qquad
H_c^{-1}\simeq11.9\;\mathrm{Gyr},
$$

the pulse's peak rate — the one place a $T^{-1}$ is native to the structure. For the $\Lambda$CDM box the anchor has a counting form, $H_\infty t_{\mathrm P}=\sqrt{\pi/S_{dS}}$: a rate fixed by a ledger size, which puts the burden on deriving $S\sim10^{122}$ — the open target that belongs with [[hyperbolic-counting/inq|hyperbolic counting]] (whose ledger rate today, $2(1+q_0)=1.326$ nats per e-fold, is receipted here from the benchmark $q_0$). But unit CST-B2 diverges from the earlier box notes exactly here, and honestly: its response *coasts and dilutes* — acceleration exits at $a/a_0\simeq11.8$, there is **no asymptotic de Sitter box** and no future $S_{dS}$ to count. In CST the box of the previous notes is a passing wall; the anchor obligation transfers from the asymptotic ledger to the crossing data $(H_c,T_c,V_c)$ of [[causal-scale-theory/anchored-response-density-postulate|the anchored source postulate]] — which is [CONSTITUTIVE], exactly where CST has always parked it.

## 6. Obligations

1. Imported numbers to verify before promotion: Planck $\,(h,\omega_m,z_*)=(0.6736,0.1430,1089.9)$, SH0ES $73.04\pm1.04$, $\omega_r$ with massless-$\nu$ approximation ($\Sigma m_\nu$ treated as matter in the carrier — small systematic, flagged); DESI numbers are quoted from the vault's own receipts.
2. The conversion is carrier-conditional compression in the exact sense of [[causal-scale-theory/observables|observables]] — not a primary-CMB likelihood; the chain-level rerun the Mercury note demands remains the real test.
3. The three-sech$^2$ solder ([MOTIF]) is open; the two box-side identities are exact but their connection to the pulse's e-fold sech$^2$ is unconstructed.
4. Pöschl–Teller receipts are numeric limits, not symbolic proofs; Cardoso–Lemos is the source to verify.
5. No perturbation sector, no recombination physics, no $H_0$ from first principles — the anchor factor stays underived, and this note's claim is only that the *shape* factor and the *tension verdict* are now receipted.
6. Receipts require numpy; stdlib rewrite owed on promotion.
