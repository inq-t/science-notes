# Audit of the Master Synthesis

The proposed synthesis plan had the right conceptual center—a versionless generalized canon, explicit claim status, failure localization, and a unit branch—but it was not safe to execute literally. This audit records the corrections applied while harmonizing the two masters and defines what the new module does and does not supersede.

## Verdict on the plan

The following decisions were sound and adopted:

- the $(\nu,\mathfrak R_c)$ family is canonical and $(1,1)$ is an evaluation;
- exact identities, conditional deductions, principles, constitutive laws, receipts, and open constructions are separated;
- the binary wall construction is imported from [[wall-construction-interface/entry|its shared owner]] rather than copied;
- failed derivations are retained as scoped no-gos;
- empirical tests are ordered by discriminating power, not by elegance;
- the old master and its audit remain available as provenance.

The following plan steps were rejected or revised:

1. **No source retirement.** The plan proposed moving leaves out of `causal-scale-master` and retiring `causal-scale-master-v8`. The user requested the new canon first and an obsolescence assessment later. Both inputs remain unchanged.
2. **No “unchanged” leaf migration.** Four old leaves needed mathematical correction or sharper premises: binary reflection, balanced reference weights, generalized width/amplitude, and the free-energy rationale.
3. **No universal $\nu=2$ existence bound.** The threshold classifies the radiation tail; finite roots depend on $(\nu,\mathfrak R_c,\Omega_{m0},\Omega_{r0})$.
4. **No combined horizon/vacuum leaf.** Exact clock algebra, the open horizontal-temperature identification, Hawking--Friedmann conversion, and the residual sector now have separate owners.
5. **No monolithic ledgers as sole owners.** Conjectures, no-gos, and open questions are individual notes; the ledgers only synthesize them.
6. **No perturbation or QFT reconstruction by implication.** CST imports the local sector through [[compatible-with-existing-physics/entry|the compatibility module]] and routes the shared wall problem externally.

## Harmonization by claim

| Claim | Older master | v8 audit | Canonical resolution |
|---|---|---|---|
| Reflection of $Q$ | Same noncentral $Q$ flipped by $J_{\mathrm{mod}}$ | Separates geometric reflection from Tomita conjugation | [[binary-geometry]] uses abstract $J_{\mathrm{refl}}$; full realization remains [[open-questions/binary-reflection-realization|open]] |
| Binary weights | Implicitly balanced | Identifies balance as an extra premise | Balance is stated before $2\cosh\theta$, $\tanh\theta$, or $\operatorname{sech}^2\theta$ |
| Soldering slope | Unit value hardwired | Carries $\nu=|\varrho_\perp|$ | [[scale-soldering]] proves affinity; [[width-principle]] separately proposes $\nu=1$ |
| Peak amplitude | Unit value hardwired | Carries $0<\mathfrak R_c<2$ | [[scale-capacity]] defines the invariant; [[unit-amplitude-principle]] separately proposes one |
| Extensive norm | Constant prefactor implicit | Listed only as a failure mode | [[open-questions/extensive-channel-normalization]] makes constancy a load-bearing assumption |
| Free-energy source | Motivated as curvature response | Labels the full-path step physical | [[relative-entropy-hessian]] owns the exact local result; [[free-energy-source]] owns the constitutive extension and its counterexample |
| Horizon normalization | Canonical temperature with a warning | Distinguishes $T_{\mathrm{hor}}$ and $T_{\mathrm{KH}}$ | [[horizontal-temperature]] isolates the open choice; [[hawking-friedmann]] contains only the resulting algebra |
| Response family | Unit pulse | General $(\nu,\mathfrak R_c)$ family and root atlas | [[generalized-background]] is canon; [[unit-branch]] contains the old evaluation |
| Width ceiling | Absent | Benchmark atlas properly qualified, but synthesis plan overgeneralized it | $\nu=2$ is an asymptotic threshold; no-root claim is benchmark-only |
| Witten pair | Exact internal factorization | Adds completion gates | [[witten-pair]] preserves the exact spectrum and refuses a spacetime lift without a covariant second variation |

## Two layers of dependency

The audit distinguishes **context and embedding** from **algebraic closure**. Causal reconstruction, tractor transport, and FLRW scale kinematics explain what scale means and how the result must interface with gravity. The pulse formula itself algebraically depends on the balanced channel, affine soldering, fixed extensive normalization, the capacity definition, constitutive source, and horizon conversion. [[closure-stack]] records both layers without pretending the first is a derivation of the second.

## Scope of the resulting canon

The new module owns the homogeneous causal-scale response and its conceptual foundations. It does not re-own:

- the general cross-fiber construction, which belongs to [[wall-construction-interface/entry]];
- primordial spectral descent, which belongs to [[causal-wall-spectral-theory/entry]];
- local GR/QFT preservation and recovery criteria, which belong to [[compatible-with-existing-physics/entry]];
- the broader conservation interpretation, which belongs to [[conservation-of-causal-charge/entry]].

The original planning packet is retained under [[junk-drawer/refactor-plan/synthesis-plan|the refactor-plan junk drawer]]. Its proposed migration stages and universal-bound language are historical inputs, not current instructions.

## Preservation result

No file in either source module was edited or moved during this synthesis. [[archive]] records local pointers and hashes. Whether those modules are obsolete, need compatibility stubs, or should be archived is deliberately deferred until this new graph has been reviewed.
