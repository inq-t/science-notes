# Salvage Audit — causal-wall-spectral-calc

This module is a two-chat log, not a theory note. Chat 01 is already fully absorbed: three of its four outputs are byte-identical to files sitting with [[causal-wall-spectral-theory/old-versions/causal-wall-spectral-completion-v2_1|the archived v2.1 completion]], and its findings F1–F16 are dispositioned line-by-line in [[causal-wall-spectral-theory/latest-version/Causal_Wall_Spectral_Theory_v3_referee_disposition|the v3 disposition]]. Its one orphan is the receipt script both memos cite by name and neither directory contains. Chat 02 is unmigrated in its entirety, and the vault holds no A₂, ADE, du Val, Kleinian, Kähler, heat-kernel or spectral-action content anywhere else. That chat is therefore the only live question in the audit — and it splits cleanly: its classical mathematics is correct and textbook, its member-selection argument rests on an inference [[causal-wall-spectral-theory/critical-kernel|the canon has already revoked in writing]], and its single most valuable number is one the memo itself undersold by calibrating against the weaker of the two available measurements.

Verdict: retain three items, port one, and file the rest as an immutable log. Do not migrate the memo as written.

## 1. What is actually here

Nine files, ~110 KB, across `chats/01` and `chats/02`. `entry.md` is an unfilled stub. Nothing in the vault links to this module; `grep -ril "causal-wall-spectral-calc" --include=*.md` returns no hits anywhere.

Both receipt scripts execute and pass every declared check — 12/12 and 18/18 — and then exit nonzero writing their JSON to a hardcoded `/mnt/user-data/outputs/` path that does not exist outside the session that produced them. Neither is stdlib-only (`mpmath`, `sympy`). [[causal-scale-theory/receipts/README|The canon's receipt contract]] requires stdlib only, output written beside the script, and nonzero exit *on check failure* — all three are violated, the last one inverted.

## 2. Chat 01 — absorbed, with one orphan

| File | md5 | Status |
|---|---|---|
| `causal-wall-spectral-referee-report-v2.md` | `f48a896a…` | identical to `old-versions/` copy |
| `causal-wall-spectral-completion-v2_1.md` | `adb01507…` | identical to `old-versions/` copy |
| `causal_wall_spectral_receipts_v2_1.json` | `c9ad5c01…` | identical to `old-versions/` copy |
| `verify_causal_wall_spectral_v2_1.py` | `e2f44795…` | **exists nowhere else in the vault** |

The script is the only executable artifact backing receipts S1–S12, and both memos in `old-versions/` name it in their headers. There are zero `.py` files in `causal-wall-spectral-theory` outside vendored Planck/ACT/BICEP code, and [[causal-wall-spectral-theory/open-problems|CW–T7]] asks for exactly this class of object. It resolves a dangling citation at no epistemic cost: the twelve receipts it runs are arithmetic on the "exact or standard" tier — the trace algebra $\delta^{ij}\Pi_{ijkl}=0$, the $P_3$ spectrum $\ell(\ell+1)(\ell+2)$, the dictionary conversions, the $\mathfrak S$ bound routes agreeing to $0.0$ — none of which v3 touched.

What it does *not* buy: `[RECEIPT]` status does not transfer to the conclusions v3 revoked. S9 computes the Planck-vs-ACT tilt difference as 1.74σ and S12 computes a large-$N$ reading $N\approx4423$; both are arithmetic on inputs the canon now says do not support the inference drawn from them.

`prompt.md` / `response.md` for both chats exist nowhere else. `causal-wall-spectral-theory/convo/` covers the v2→v3 session and four successors but not these two.

## 3. Chat 02 — the A₂ wall memo

### 3.1 The import is real at its base

The 2026 counterexample to the Jacobian conjecture is genuine: a degree-7 map $F:\mathbb C^3\to\mathbb C^3$ with $\det DF=-2$ constant and not globally injective, found in July 2026 with AI assistance. Its published geometric digestion runs through exactly the objects the memo names — binary cubics, the multiplication map $\mathrm{Sym}^1\times\mathrm{Sym}^2\to\mathrm{Sym}^3$, resultants, $SL_2(\mathbb C)$ equivariance, and the splitting $C=L_1L_2L_3$ that gives a generic cubic three preimages. The $S_3$ on those three factors is not invented.

`[IMPORT CW-P3]` should nevertheless be decomposed before anything is retained, because it bundles three different things under one conditional:

- **Classical.** Receipts A1–A7 in full. $M=T_aT_b=\begin{pmatrix}0&1\\-1&1\end{pmatrix}$, $M^3=-\mathbf1$, order 6, char poly $t^2-t+1$, splitting field $\mathbb Q(\zeta_6)$; $B_3\twoheadrightarrow S_3$ and $SL(2,\mathbb Z)=B_3/\langle(\sigma_1\sigma_2)^6\rangle$; $\mathrm{MCG}(T^2\setminus\mathrm{pt})=SL(2,\mathbb Z)$ on the once-punctured-torus Milnor fibre; spectral numbers $\{5/6,7/6\}$, exponents $\{1,2\}$, $h=3$, $\mu=2$; $\operatorname{disc}(u^3+au+b)=-(4a^3+27b^2)$; Tschirnhaus depression; quasi-weight 12 under $(a,b)\mapsto(\lambda^4a,\lambda^6b)$; $j=6912a^3/(4a^3+27b^2)$ weight-zero. I re-verified every one of these independently. All are correct, and all are in the memo's own [E5] — Arnold–Gusein-Zade–Varchenko and Milnor. Cardano has the cubic depression from 1545. `[STANDARD]`, citable directly, needing no preprint.
- **Needs the unverifiable preprint.** One claim: that this particular counterexample's obstruction germ *is* $A_2$ with $S_3$ monodromy, plus the "(times one smooth parameter)" reduction from a 3-dimensional source to a 2-dimensional base. Not checkable from the vault; the JC-strand preprint is not staged here.
- **Neither classical nor imported.** Everything in §1 under "Reading adopted here": that the wall's near-conformal degeneration *is* the Keller obstruction, that its deformation space *is* the $A_2$ base, that the conformal fixed point *is* the discriminant locus, that $c^{(0)}(k)$ *is* the flow of the $A_2$ deformation coupling, that the wall algebra *is* the $\mathbb Z_6$-graded Milnor-fibration algebra. In the canon's vocabulary these are `[IDENTIFICATION — OPEN]`, six of them, and every number in §4–§7 descends from them alone.

The bundling matters because the status box makes the whole memo "conditional on CW-P3" as though CW-P3 were a filed theorem. Its load-bearing half is six unargued identifications, and the "18/18 pass" credential certifies only the classical half.

One typing question worth carrying forward: the memo calls the obstruction "the Keller obstruction (nonproperness)" and then describes the cover *ramifying* on the discriminant. Ramification of the auxiliary root-cover on $4a^3+27b^2=0$ is correct and classical. Non-properness of a Keller map is a statement about preimages escaping to infinity — and $F$ itself, being étale everywhere by $\det DF\equiv-2$, ramifies nowhere. Two different loci. Nothing numerical depends on which, which is itself a signal about how much work the geometry is doing.

### 3.2 What fails

**The three "welds" have prior probability near one.**

$\mu(A_2)=2$ "=" the class's invariant count is receipt A7, and A7 is literally `mu = 2; ok = (mu == 2)` — the Gröbner line that would compute $\mu$ is assigned and never read, and the right-hand side of the claimed weld is never touched by any code. The available small $A_2$ invariants take values $\{1,2,3,4,6,12\}$; any parameter count in that set matches, and the memo's own §8 ledger counts *three* numbers (one rational, two readings), not two.

$h(A_2)=3$ = sheet count is an identity for every $A_n$ — $h(A_n)=n+1=\deg$ — so it cannot fail for any $A$-type singularity and carries no information. It is filed as one of "two independent derivations of the same 3."

Removable $u^2$ = the constant-mode quotient $C^\infty(\Sigma)/\mathbb R$ matches two one-dimensional objects, and every $A_n$ ($n\ge2$), $D_n$ and $E_n$ normal form has exactly one removable subleading term. It is also double-spent: §2.6 reads it as the $\ell=0$ mode of $\zeta$, §6/R4 reads it as the gauge direction that kills the second NG vertex.

**"Exactly two members survive" is curation.** The $b$-table lists $b\in\{1,2,3,6\}$ and reports only $b=3$ inside the band $[3.13,6.27]\times10^{-3}$. But $b=4$ gives $4.93\times10^{-3}$ and $b=5$ gives $6.16\times10^{-3}$ — both inside it. ($b=4$ is the quasi-weight of the coordinate $a$, verified in the memo's own receipt A6.) Against Planck's $\alpha_s$ alone, all of $b\in\{1,2,3,6\}$ are alive at 0.86–1.78σ; Planck constrains $b$ not at all.

**The band itself is the revoked inference.** [[causal-wall-spectral-theory/critical-kernel|The canonical note]] already says it in as many words: *"Differences between best-fit $n_s$ values from distinct, overlapping likelihood combinations are not themselves an estimator of running."* The two tilts are quoted at the same pivot from nested datasets, so $\Delta\ln k=0$ and the "lever arms 1.5–3" are supplied by hand. The band is also *narrower* than the 1σ interval of the actual measurement it competes with. Member B's selection is 100% dependent on it and has no derivation left once it goes.

**Member B leans on the number the memo forbids leaning on.** CW-S3: *"is $d=h(A_2)$ a theorem or a coincidence? … Do not lean on it."* The memo then selects the survivor as $b=h(A_2)=3$, justifies it by "the same 3 as the sheet count and $P_3$'s order," sets the future success criterion to 3, and names it in the closing sentence.

**"Exactly one $m$ survivor" is a lattice artifact.** The candidate list $\{7/6,1,5/6,2/3,1/2,1/3,1/6\}$ is exactly $\{k/6:k=1..7\}$ — a grid, not a set of invariants. Two entries ($2/3$, $1/3$) are the one-variable-convention duplicates of $7/6$ and $5/6$; $1/2$ is the suspension variable's weight, an $A_1$ datum; exponent 2 is missing. Planck's 2σ survival window is $m<0.2536$, and a $1/6$-spaced lattice contains exactly one point below it — guaranteed before $A_2$ entered. At $1/12$ spacing (equally "$A_2$-salient": the gap over $\mu$), three survive.

**Two of the three corpses are not dead, and the third could never have lived.** N1 kills $\delta=1/6$ at "31σ" — using $\sigma(n_s)=0.0042$ where every other row uses $\sigma(\alpha_s)=0.0067$, and refuted on its own terms: $1/h^3=1/27=0.03704$ is **+0.46σ** from the measured $\delta$, and 27 is the coefficient in the memo's own verified discriminant. N2's "every route dies by $\ge10^6\times$" fails as a universal: $2\cdot6^9=20{,}155{,}392=1.030\times c^{(0)}$. N3's stated "$\ge19\times$" is arithmetically wrong — $222.2/12=18.52$, and the script's own test is `> 18` — the quantifier fails ($2\cdot3\cdot6\cdot12=432>222.2$), and the target $222.2=8/0.036$ is a *lower* bound from $r<0.036$, so nothing above it can ever be excluded. M-A2-3 is not a morgue entry.

**All three v3-revoked claims are load-bearing.** The $1/\sqrt{c^{(0)}}$ floor and the $|f_{\rm NL}|\gtrsim1$ class kill carry §6 and row 4's "headroom $10^2$"; the universal $|\alpha_s|\lesssim\delta^2$ bound carries the $3\times10^{-3}$ threshold that is the members' advertised signature; the tilt-drift inference carries member B entirely.

### 3.3 The one result the memo undersold

The memo calibrates its entire kill battery on Planck's $\alpha_s=-0.0045\pm0.0067$, cites the ACT DR6 extended-model paper only for a qualitative "mild positive-running preference," and never runs its own table against that paper's constraint. The canon mirrors the number and the posterior archive locally: $\alpha_s=0.0062\pm0.0052$ (P–ACT–LB). Confirmed against the source.

Run the table against it:

| hypothesis | $\alpha_s$ | $z$ vs Planck | $z$ vs P–ACT–LB |
|---|---|---|---|
| minimal class, $\alpha=0$ | 0 | +0.67 | −1.19 |
| **member C, $m=1/6$** | $5.85\times10^{-3}$ | +1.54 | **−0.07** |
| $m=1/3$ ("STRAINED, dying") | $1.17\times10^{-2}$ | +2.42 | +1.06 |
| $m=1/2$ ("DEAD") | $1.76\times10^{-2}$ | +3.29 | +2.18 |
| member B, $b=3$ | $3.70\times10^{-3}$ | +1.22 | −0.47 |

$\alpha_s=\delta/6$ lands **0.07σ** from the tightest published running measurement. That is the only number in the memo that looks like a retrodiction rather than a selection, and the memo does not report it.

It cuts both ways, and both directions matter. Against the better data the kill battery's headline — "every $O(1)$ $A_2$ exponent is dead or dying as a relevant rate" — is false: $m=1/3$ sits at +1.06σ, more comfortable than $m=1/6$ is against Planck. Survivor count goes from 2 to roughly 15. And the memo's "$O(1)$ exponents die" was never data in the first place: $\alpha=m\delta$ with $\sigma_\alpha=0.0067$ requires $m\lesssim0.25$, and an $O(1)$ number exceeds $0.25$ by definition.

## 4. Disposition

| Item | Disposition |
|---|---|
| `chats/01/outputs/*.md`, `*.json` | Duplicate. Absorbed and dispositioned. Drop or leave as inert log. |
| `chats/01/outputs/verify_causal_wall_spectral_v2_1.py` | **Retain — port.** Resolves a dangling citation in two memos already filed. |
| `chats/01/prompt.md`, `response.md` | Retain as log. Unique, no analogue in `convo/`. |
| A₂ dossier A1–A7 (the mathematics) | **Retain — but cite AGV/Milnor, not this memo.** All classical, all correct. |
| $\alpha_s=\delta/6$ at 0.07σ on P–ACT–LB | **Retain — the one live item.** Recalibrate before filing. |
| The three "welds" ($\mu=2$, $h=3$, removable $u^2$) | Do not retain. Prior ≈ 1; A7 is `2 == 2`. |
| Member B ($b=3$, $\alpha=3\delta^2$) | Do not retain. Selected wholly by the revoked drift band; $b=4,5$ omitted from its own table. |
| Morgue M-A2-1/2/3 | Do not retain as filed. Retain the *pattern* (§6). |
| The compression audit / "zero free functions" | Do not retain. Six open identifications plus an admitted-unproven weld are not a collapse. |
| "18/18 pass" as the memo's credential | Do not retain. No receipt tests any claim connecting $A_2$ to the wall. |
| Low-ℓ WATCH-2 | Retain as a strain, not a neutral watch. The 26% denominator is single-multipole cosmic variance; over $\ell=2$–30 it is ~4.6%, and both members predict *enhancement* where Planck leans low. |
| `chats/02/outputs/verify_a2_wall_v1.py` | Retain as log only. Dead assignments, hardcoded PASS strings, one wrong intermediate the author flagged and shipped. |
| `entry.md` stub | Fill. Currently violates the entry.md rule in [[AGENTS]]. |

## 5. Actions

1. **Move `verify_causal_wall_spectral_v2_1.py` into `causal-wall-spectral-theory/old-versions/`,** beside the two memos that cite it. Port to the canon's contract first: stdlib only (replace `mpmath`/`sympy` with exact rational arithmetic and closed forms — every check is elementary), write the JSON beside the script, and exit nonzero *on failure* rather than on success. Label `[RECEIPT]`; note in `claim-audit.md` that S9 and S12 are arithmetic on inputs whose inference v3 revoked.
2. **Open a note under `causal-wall-spectral-theory` for the $A_2$ reading, at `[IDENTIFICATION — OPEN]`, carrying only the recalibrated prediction.** The one thing worth writing down: a relevant clock of rate $m$ gives $\alpha_s=m\delta$, and $m=1/6$ — the $A_2$ spectral gap — yields $5.85\times10^{-3}$, which is 0.07σ from P–ACT–LB. State in the same paragraph that the selection is a $1/6$-lattice artifact, that $m=1/3$ survives the same data at 1.06σ, and that the sign of $m$ still requires CW-S1. `Upgrade criterion`: an independent derivation of $m$ from the deformation's anomalous dimension. `Failure criterion`: $\alpha_s\le0$ at 3σ, or $|\alpha_s|<10^{-3}$ established.
3. **Add the classical $A_2$ facts to `sources/` as AGV + Milnor,** not as a memo import. The dossier is textbook and the module's source library is the right home for it.
4. **Fold `chats/01` and `chats/02` into `causal-wall-spectral-theory/chats/`** and retire this module from `inq.toml`. Per [[AGENTS]], `./chats` is "a historical log of the discussion that surrounded the main content of *that* directory's theme" — and this theme is the spectral programme's. A sibling module holding a byte-identical copy of another module's history is the duplication the vault's own conventions forbid.
5. **Add one line to `open-problems.md` recording why the memo could not be promoted:** it is the vault's only attempt at the microscopic member that [[causal-wall-spectral-theory/open-problems|CW–T2]] asks for, and it failed not on its physics but on its epistemics — a curated candidate grid, a revoked selection statistic, and a credential that certified textbook facts. That is worth a sentence so the next attempt does not repeat it.

## 6. Do not recover

- **The Planck-vs-ACT tilt drift as a running estimator.** Already refuted in `critical-kernel.md`. Any future member selected by it is selected by nothing. The correct reference is the mirrored P–ACT–LB posterior.
- **A universal $|f_{\rm NL}|\gtrsim1$ kill, a $1/\sqrt{c^{(0)}}$ floor, or a universal $|\alpha_s|\lesssim\delta^2$ bound.** Revoked by v3; the A₂ memo re-imports all three. Re-importing them from this folder would be reviving a claim the canon killed once.
- **$c^{(0)}$ as a central charge or a large-$N$ count.** Revoked by v3; S12's $N\approx4423$ is the tempting re-entry point.
- **Small-integer coincidences between $A_2$ invariants and theory parameters, as evidence.** The available values are $\{1,2,3,4,6,12\}$ and the memo permits products, so a match is available for essentially any target. If such a coincidence is filed again it needs the prior stated in the same sentence.
- **Morgue entries for routes the theory already forbids.** N2 kills a route the memo's own status box declares unlawful. A corpse that could not have lived is not a credential, and counting it as one inflates the register.

## 7. Method note

Every number in §3 was recomputed independently, not read off the memo. Both scripts were executed. The ACT DR6 running constraint was checked against the source paper rather than against the vault's transcription of it. The two arithmetic errors found in the memo (N3's $\ge19\times$, which is 18.52; and the $1.76\times10^{-2}$ table entry, where the memo's own script prints $1.75\times10^{-2}$) are minor; the errors that matter are the omitted $b=4,5$ rows, the mixed $\sigma$ in N1, and the unrun table against the better measurement.
