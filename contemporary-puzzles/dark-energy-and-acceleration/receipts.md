# Receipts

Four evidential layers are kept apart, because arithmetic agreement at one is not support for the layer beneath it: identity, receipt, background fit, and microscopic evidence. Layers one and two are discharged here by a runnable script. Layer three is an indicative comparison with published DESI DR2 fits in which the unit-branch tangent lands within a fraction of a sigma of one supernova combination, drifts to roughly two sigma from BAO plus CMB alone, and puts the phantom-crossing epoch systematically earlier than any of them. Layer four is empty, and while it is empty nothing below constitutes evidence for the wall construction, either unit principle, or the constitutive law.

The layer separation and its inequality chain are inherited from [[causal-scale-theory/empirical-status|the empirical status note]]; the reporting discipline and test ranking from [[causal-scale-theory/observables|observables and discriminating tests]]. This note applies them to the acceleration puzzle rather than restating them.

Everything numerical below is produced by `receipts/acceleration.py`, standard library only, nonzero exit on any failed check including under `--json`. It is not an independent implementation of the canonical receipt in `causal-scale-theory/receipts/`: the closure residual is the same equation and both use bisection, so that part is a regression check. What this script adds is cosmography — $q$ and $j$ from finite differences on $E^2(N)$, compared against the analytic tangent formulas — plus the branch, negative-control, and comparison blocks below.

## Layer 1 — identities

**[EXACT — AFTER REDUCTION]**, with the qualifier understood to cover the granted binary reduction *and* the separate-conservation background assumption that turns the density profile into an equation of state. The invariant

$$
9(1+w_X)^2+6w_X'=4\nu^2
$$

is verified to machine precision at $x\in\{-2,-0.75,-0.1,0,x_c,1,3\}$, is unchanged by amplitude for $\mathfrak R_c\in\{0.6,1.0,1.3\}$, and generalizes correctly for $\nu\in\{0.6,1.0,1.4,1.75\}$. The CPL locus

$$
w_a=\frac32(1+w_0)^2-\frac{2\nu^2}{3}
$$

is confirmed as an identity of the same family, not an independent result. [[causal-scale-theory/observables|Observables]] calls both exact conditional shape relations, which is the right description.

Two structural checks worth naming separately. **Branch domain.** [[causal-scale-theory/flatness-branches|The flatness closure]] defines $x_c=\ln(1+z_c)>0$, so admitted dates are positive roots and the canonical late branch is the smallest of them. The threshold at which the unconstrained closure equation's root leaves that admitted domain is $\mathfrak R_c=2D$ — exact and $\nu$-independent, since $\operatorname{sech}^2(0)=1$ — and the script confirms the root is admitted at $\mathfrak R_c=1.30$ and not at $1.45$. The numerical value $2D=1.378621$ at benchmark abundances is inherited from the archived v8 master rather than from the current canon. The script also reproduces the canonical benchmark fold atlas — one positive root at $\nu=1.5$, three at $\nu=1.7$, one at $\nu=1.9$, none at $\nu=2.0$ — together with the canon's own counterexample to a universal ceiling, positive roots at $\nu=2.0$ and $\nu=2.2$ when the same abundances are paired with $\mathfrak R_c=1.9$. The atlas is benchmark-specific and $\nu=2$ classifies radiation-tail asymptotics rather than bounding root existence.

**No future crossing of $-1/3$.** On the unit branch

$$
1+3w_X=2(\tanh x-1)=-\frac{4}{e^{2x}+1}<0
$$

for every finite $x$; [[causal-scale-theory/unit-branch|the unit branch note]] gives the reason acceleration nonetheless ends, which is that the negative response active mass falls as $a^{-4}$ against matter's $a^{-3}$. The script tests $\log|1+3w_X|$ rather than the magnitude, because the magnitude goes subnormal near $x\simeq355$ and reaches zero near $x\simeq373$, so a direct evaluation reports a spurious zero.

**[RECEIPT]** These are regression checks. An identity evaluated with the same formula on both sides confirms the reduction, not the physics.

## Layer 2 — background receipt

**[CONDITIONAL OUTPUT]** Unit branch, $\nu=\mathfrak R_c=1$, benchmark abundances $\Omega_{m0}=0.310598$ and $\Omega_{r0}=9.15\times10^{-5}$:

| Quantity | Value | Source |
|---|---:|---|
| crossing $x_c$ | $0.2940066$ | reproduces [[causal-scale-theory/unit-branch|unit branch]] |
| crossing redshift $z_c$ | $0.3417927$ | reproduces unit branch |
| $\Omega_{X,c}$ | $0.5$ | [[program-core/ruble-equations#RE8 — Homogeneous member return and CST-B2 specialization|weak unit matching plus the response law]] |
| $w_0$ | $-0.8094545$ | reproduces unit branch |
| $w_a$ | $-0.6122053$ | reproduces unit branch |
| $q_0$ | $-0.3369025$ | reproduces unit branch |
| $j_0$ | $-0.1112465$ | reproduces unit branch |
| acceleration entry | $z=0.7856935$ | reproduces unit branch |
| acceleration exit | $a/a_0=11.78652$ | reproduces unit branch |
| episode width | $3.046764$ e-folds | computed here |
| present position in episode | $19.03\%$ | computed here |

All are arithmetic consequences of the declared abundances, unit principles, late-root choice, flatness, separate conservation, and zero residual. There are no fitted dark-sector parameters.

The two cosmography rows are quoted at their closed-form values. The script obtains $q$ and $j$ by finite differences on $E^2(N)$ and then checks them against closed-form derivatives of the same function, which is the one place it does more than regress against stored literals; the finite-difference $j_0$ agrees with the closed form to $2\times10^{-8}$ and with the canonical literal to $6\times10^{-8}$. It also verifies that the response fraction today recovers $D$ when recomputed from the profile rather than from the closure, and that the density peak is located at $x=0$ rather than assumed there.

## Layer 3 — indicative comparison with published fits

The published DESI DR2 constraints, verbatim from the collaboration's own table:

| Combination | $\Omega_m$ | $w_0$ | $w_a$ | preference over $\Lambda$CDM |
|---|---:|---:|---:|---:|
| DESI+CMB | $0.353\pm0.021$ | $-0.42\pm0.21$ | $-1.75\pm0.58$ | $3.1\sigma$ |
| +Pantheon+ | $0.3114\pm0.0057$ | $-0.838\pm0.055$ | $-0.62^{+0.22}_{-0.19}$ | $2.8\sigma$ |
| +Union3 | $0.3275\pm0.0086$ | $-0.667\pm0.088$ | $-1.09^{+0.31}_{-0.27}$ | $3.8\sigma$ |
| +DESY5 | $0.3191\pm0.0056$ | $-0.752\pm0.057$ | $-0.86^{+0.23}_{-0.20}$ | $4.2\sigma$ |

Recomputing the unit-branch tangent at each row's own fitted $\Omega_m$, so the comparison is internally consistent rather than evaluated at a benchmark the row does not share:

| Combination | $w_0$ pred | offset | $w_a$ pred | offset | $z_c$ pred | $z$ where the CPL pair itself crosses |
|---|---:|---:|---:|---:|---:|---:|
| DESI+CMB | $-0.8573$ | $-2.08\sigma$ | $-0.6361$ | $+1.92\sigma$ | $0.2429$ | $0.4957$ |
| +Pantheon+ | $-0.8104$ | $+0.50\sigma$ | $-0.6127$ | $+0.03\sigma$ | $0.3397$ | $0.3537$ |
| +Union3 | $-0.8290$ | $-1.84\sigma$ | $-0.6228$ | $+1.51\sigma$ | $0.3000$ | $0.4399$ |
| +DESY5 | $-0.8194$ | $-1.18\sigma$ | $-0.6177$ | $+1.05\sigma$ | $0.3203$ | $0.4052$ |

Four observations, in the order that matters.

**The prediction is stiff and the data are not.** The predicted $w_0$ moves only from $-0.810$ to $-0.857$ across the full range of fitted $\Omega_m$, and $w_a$ barely moves at all. The observed $w_0$ moves from $-0.838$ to $-0.42$. So the agreement is not manufactured by matching abundances; the tangent is nearly abundance-independent, and the spread in the comparison is a spread in the data.

**The best and worst rows must be reported together.** Against Pantheon+ the prediction is $0.50\sigma$ in $w_0$ and $0.03\sigma$ in $w_a$ — for a point prediction with no dark-sector freedom, about as good as this kind of comparison gets. Against BAO plus CMB alone it is roughly $2\sigma$ in both, and in every row but Pantheon+ it sits on the $\Lambda$CDM side of the data: the framework predicts a *milder* departure from $w=-1$ than DESI's central values want. Reporting only the Pantheon+ row would be selection.

**The crossing epoch is adjacent but systematically early, not matching.** The reclassification *requires* a phantom crossing — $w_X<-1$ before, $>-1$ after, with the density maximum exactly at $w_X=-1$ — because that is what a pulse looks like, so the sign structure is a genuine structural prediction and it is the one the data confirm. The epoch is another matter. Predicted $z_c$ spans $0.24$ to $0.34$; solving each CPL pair for its own crossing gives $0.35$ to $0.50$. Those ranges do not overlap. Every combination crosses later than predicted, by $+0.014$ for Pantheon+ up to $+0.25$ for BAO+CMB — the same direction as the $w_0$ offsets, which is at least coherent, and not a match.

**The implied rate restates the $w_a$ offset rather than adding to it.** Inverting the locus on each published pair gives the scale-state rate that pair would imply if it were the exact tangent, with an envelope taken over the $1\sigma$ box on $(w_0,w_a)$:

| Combination | $\nu$ implied |
|---|---:|
| DESI+CMB | $1.84\ [1.44,2.21]$ |
| +Pantheon+ | $0.99\ [0.79,1.15]$ |
| +Union3 | $1.37\ [1.14,1.56]$ |
| +DESY5 | $1.20\ [1.01,1.34]$ |

The Pantheon+ row gives $\nu\simeq1.0\pm0.2$ against a principle that sets it to one. That is worth noting and it is *the same fact* as the $0.03\sigma$ in $w_a$ above, re-expressed — quoting it to four decimals would present one agreement as two. It must also not be described as a measurement of a microscopic scale-state rate: a phenomenological fit estimates the effective inverse width and crossing amplitude, while the modular interpretation predicts that the corresponding microscopic quantities equal one. Reading it the other way is what [[causal-scale-theory/no-gos/background-reconstruction-is-not-wall-construction|the reconstruction no-go]] forbids. At the other end, the BAO+CMB envelope reaches past the benchmark late-branch fold, so that pair is not accommodated on the intended branch at those abundances.

### Everything wrong with the comparison above

Stated plainly, because a comparison whose weaknesses live only in the reader's head is a fit dressed as a test. The first two items are not this module's caveats but the canon's.

- **Tangent against range.** [[causal-scale-theory/observables|Observables]] rates the linked $w_0$–$w_a$ tangent as "potentially useful, but generic CPL posteriors need not equal the local CST tangent," and says a credible analysis fits the forward model rather than interpreting a reconstruction as a wall measurement. The predicted pair is a local tangent at $z=0$ of a $\operatorname{sech}^2$ history; the observed pair is a CPL fit over a redshift range. The offsets are indicative and are not significances.
- **The invariant is weak here, not strong.** The same table rates the shape invariant structurally weak with present background coverage, because differentiation is noisy and the tails carry most of the rate leverage. It belongs as a consistency check after direct fitting, not as a headline.
- **No likelihood, no covariance.** A real test refits the $\operatorname{sech}^2$ history directly. The $(w_0,w_a)$ covariance is not in the workspace, so the implied-$\nu$ envelope is a box over a strongly anticorrelated pair and is not a confidence interval, and the sigma columns ignore that correlation entirely.
- **Non-Gaussian posteriors.** The $w_a$ intervals are asymmetric and at least one analysis notes they are not Gaussian, so one-sided sigma distances are a convenience.
- **No priority claim.** [[scale-as-modular-observable/misc/research-history|The research history]] records that an earlier master described its observational comparison as partly retrodictive, and that a later claim of the shape having been fixed before contact with data should not be used as historical evidence.
- **The abundances are inputs.** $\Omega_{m0}$ and $\Omega_{r0}$ come from data. "No fitted parameters" means no fitted *dark-sector* parameters; the root branch and zero residual are declared sector choices.
- **The evidence itself is provisional.** The preference for evolving dark energy is carried substantially by the lowest-redshift supernova anchor, and the significances depend on the compilation.
- **The negative control.** The logarithmic compression that makes the crossing come out recent is shared with $\Lambda$CDM and is not evidence; [[coincidence-reframed]] owns the argument and the script asserts the gap sizes.

### The prior background comparison

A background-only $\chi^2$ comparison against $\Lambda$CDM exists in the inherited material and is recorded in [[causal-scale-theory/empirical-status|the empirical status note]] with the status **[REPORTED FIT — LIMITED, NOT FULLY REPRODUCED]**. It is not restated here: a number whose pipeline cannot be regenerated gains nothing from appearing in a second note, and the comparison above is deliberately independent of it.

## Layer 4 — microscopic evidence

**[OPEN CONSTRUCTION]** Empty. No dynamical FLRW wall construction exists, so neither $\nu$ nor $\mathfrak R_c$ has been returned by anything other than the principles that set them. Until then, layer three tests an effective shape and cannot distinguish a modular derivation from any other mechanism engineered to produce the same $w(N)$. [[causal-scale-theory/observables|The test hierarchy]] ranks this the highest-discrimination test for exactly that reason.

## Not claimed here

Recorded so that no reader has to check: this module quotes no AIC or DIC ranking; no withheld v8 best-fit amplitude or rate value, both of which are outside the canon because their likelihood directories are absent; no neutrino inference, which the canon treats as a class-membership and negative-control exercise rather than distinctive support; no $f\sigma_8$, $\sigma_8$, $S_8$, lensing, or growth number of any kind, since the covariant response sector is unconstructed; and no claim that DESI has measured a microscopic scale-state rate or horizon capacity.

## What would kill the reclassification

Distinguished from what would merely revise the framework, since a failure that localizes is the programme's stated structural virtue.

**Kills the reclassification.** A regular, minimally coupled, positive-kinetic scalar history — or a positive-definite sigma-model history — that reproduces the full crossing, since that is a direct counterexample to the no-go's stated premises and [[field-completion-no-gos|the no-go]] is the reclassification's positive content. Note the narrowness: exhibiting *some* covariant completion is not a falsifier but the thing the programme is trying to build. Also fatal: a reconstructed response history that cannot satisfy $9(1+w_X)^2+6w_X'=$ any constant, subject to the power caveat above; more than one genuine density maximum or $w=-1$ crossing in the response sector; or a response with no phantom crossing at all, since a pulse must have one.

**Kills the unit branch but not the reclassification.** A crossing fraction differing from one half after assumptions are controlled, which falsifies $\mathfrak R_c=1$. A wall construction returning a finite, scheme-stable $\nu\ne1$. Data tightening at DESI's present central values, which would push the implied rate off the intended branch — the $2\sigma$ tension in the BAO+CMB row and the systematically late crossing epochs are where this bites first.

**Kills the sector but not the pulse.** A positive residual, which removes transient acceleration and the coasting future while leaving the exact binary profile untouched.

**Kills the response as physics without touching the type argument.** No conserved covariant $T^X_{ab}$ realizing the background, in which case the homogeneous response is not a physical sector and the cosmology reduces to an ansatz with suggestive notation.

Sources for the observational values in layer three: DESI Collaboration, *DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints*, [arXiv:2503.14738](https://arxiv.org/abs/2503.14738), Table 5 and Eqs. (25)–(28); significances cross-checked against M. Cortês and A. R. Liddle, [arXiv:2504.15336](https://arxiv.org/abs/2504.15336).
