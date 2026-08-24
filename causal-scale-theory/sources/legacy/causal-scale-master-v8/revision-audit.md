# What the Proposed v8 Revision Contributes

The AI-written v8 proposal is cumulative: it usefully consolidates several safeguards already present in [[causal-scale-master/entry|the v7 master]], adds some generalized bookkeeping and empirical claims, and introduces new errors of its own. This audit distinguishes retained v7 structure, material additions in the AI synthesis, and corrections made during the present review rather than crediting the entire package to the revision.

The reviewed raw snapshot is identified by content hash:

- `inbox/causal-scale-dynamics-proposed-v8/causal-scale-dynamics-proposed-v8.md` — SHA-256 `256E8DAA93BB6122B48B380BFBB02343204ED73461C66F9CDDF7C82F09165DBE`;
- `inbox/causal-scale-dynamics-proposed-v8/receipts_revision2.py` — SHA-256 `8FDE1C3955CA9D96F100E3915CB7E42DE75B5A16D33EA21D016FF10303BE9B9A`.

These hashes preserve provenance without duplicating a large raw AI monolith inside the active module.

## Retained or clarified from v7

The proposal restates, often effectively, structure that was already part of the master programme:

- the vertical modular-flow versus horizontal state-deformation split;
- the invariant Ruble number
  $$
  \mathfrak R_c=(k_B/S_c)G^\perp_{NN}(N_c);
  $$
- the status of $\nu=1$ and $\mathfrak R_c=1$ as principles rather than established theorems;
- rejection of conformal-weight integrality as a derivation of unit width;
- rejection of “normal plane $\Rightarrow$ chiral CFT $\Rightarrow$ Cardy” as a capacity proof;
- anchoring the response amplitude at the self-dual event;
- the internal—not yet spacetime—status of the Witten pair;
- the distinction between local vacuum blindness and the open global residual sector.

Their repetition is still useful because the AI proposal gathers the autopsies and claim labels in one place. It should not be treated as their original source.

## Material additions worth adopting

The most useful forward moves in the proposed synthesis are:

- making the generalized $(\nu,\mathfrak R_c)$ family central to the accounting;
- displaying the generalized differential invariant and CPL tangent locus;
- insisting that width and amplitude occupy independent observable slots in the canonical binary normalization;
- expanding the receipt, prediction, kill-condition, and open-problem ledgers;
- gathering negative perturbative results that block naive identification of the Witten pair with matter growth;
- correcting and receipting the unit-branch jerk and chronology values.

These moves sharpen the programme, but their empirical claims and some of their mathematical interpretations still require the corrections below.

## Corrections made in this module

### The width ceiling is branch dependent

The proposal calls $\nu\simeq1.814$ an absolute flatness-existence ceiling. Its receipt computes a hybrid dust-form fold. With nonzero radiation, the exact benchmark closure develops a radiation-driven double root at $\nu=1.558402308$; between that value and $1.814657203$ it has three positive roots, and for $1.814657203<\nu<2$ only the very-high-redshift radiation root remains. Thus $1.814657203$ is the end of the smallest positive root continuously connected to the intended late branch, not the end of all roots.

### Horizon signs and temperatures need separate symbols

The signed quantity is

$$
\widehat\mu_A=(1-q)/2,
$$

while the surface-gravity magnitude is

$$
\mu_A=|1-q|/2.
$$

The horizontal normalization $T_{\rm hor}=\hbar c/(2\pi k_BR_A)$ differs from the Kodama–Hayward temperature by $\mu_A$. Identities using the signed clock cannot be extended to all branches by silently inserting a magnitude.

### The flow is heteroclinic, not a saddle-node pair

For $X=1+w_X$,

$$
X'=\frac{2\nu^2}{3}-\frac32X^2.
$$

Its two fixed points are hyperbolic, and the $\tanh$ solution is a heteroclinic orbit modulo translation. “Saddle-node fixed points” is the wrong dynamical classification.

### The claimed triple coincidence contains a generic identity

For positive separately conserved $\rho_X$,

$$
\rho_X'=0\quad\Longleftrightarrow\quad w_X=-1.
$$

These are one fact, not two independent predictions. The nontrivial additions are coincidence with binary self-duality and, when $\mathfrak R_c=1$, with dark–ordinary equality.

### The response does not cross its own active-mass boundary at exit

At unit width,

$$
1+3w_X=2(\tanh x-1)<0
$$

for every finite $x$. Cosmic acceleration ends because ordinary positive active mass overtakes the decaying negative response, not because the response reaches $w=-1/3$ at a finite exit time.

### Local vacuum blindness is not a complete vacuum solution

Central invariance of normalized states and trace-free blindness are exact. They do not determine the scalar integration constant, control the metric variation of the effective action, or establish radiative stability. The phrase “vacuum catastrophe dissolved” is therefore stronger than the demonstrated result.

### Background viability is not perturbative or QFT consistency

The proposal's homogeneous fit cannot establish stable perturbations, CMB/lensing/growth consistency, or recovery of QFT and the Standard Model. Those are separate gates with explicit requirements in [[perturbation-and-qft-interface]].

## Claims withheld pending reproducibility

The inbox snapshot does not contain the `P1/` package or `receipts_v8.py` cited by the proposal. The following claims are therefore not promoted into the synthesis as established results:

- the reported fit $\nu=0.800$ with its confidence interval;
- the reported fit $\mathfrak R_c=1.025$ with its confidence interval;
- the stated $\Delta\chi^2$ and AIC ranking;
- the neutrino-mass and perturbative-profile discussions;
- any claim that DESI directly measured modular width or horizon capacity.

They may be promising conditional reports. They need the actual likelihood code, data manifest, covariance treatment, priors, nuisance parameters, branch handling, and machine-readable outputs before they belong in a durable research module.

## Rhetoric deliberately not inherited

Several phrases in the proposed revision compress too much logical structure:

- “the homogeneous theory is closed” hides the unconstructed wall family, binary identification, constitutive law, horizon-temperature identification, conservation assumption, and residual-sector choice;
- “zero fitted constants” is parameter accounting, not premise accounting;
- “last configuration standing” depends on incomplete observational evidence and an incorrectly stated width ceiling;
- “measured unit laws” conflates effective-profile fits with microscopic modular measurements;
- multiple appearances of the same $\operatorname{sech}^2$ factor are one mathematical structure, not independent evidence.

The sharper formulation is that the **effective homogeneous history is rigid once a transparent closure stack is granted**. That remains an impressive property without overstating how much of the stack has been derived.

## Ideas retained only as research routes

The revision's best speculative remnants are preserved in [[conjecture-ledger]]:

- Euclidean periodicity as a possible—but obstructed—route to character quantization;
- a genuine near-horizon Virasoro construction as a possible route to capacity equality;
- a covariant descendant of the Witten pair;
- a global vacuum completion complementary to local central blindness;
- algebraic QFT reconstruction;
- causal-set and Keller parallels as zero-weight rhymes.

The raw AI document and receipt remain unmodified in the inbox. This module absorbs arguments, equations, and corrections only after retyping their logical status.
