# Response, Covariance, and Precision Registers

Quadratic objects that share a formula need not share a mathematical type. This note is the programme-wide routing ledger for Fisher and BKM response, covariance, precision, spectral filters, localized areal response, and gravitational quadratic forms; it records the legitimate bridges among them while leaving definitions, proofs, sources, and consumer constructions with their specialist owners.

## What a response claim must declare

Every response object should state:

1. its carrier and background state or field;
2. the tangent, source, or perturbation being varied;
3. whether the return is a bilinear form, operator, measure, or scalar contraction;
4. its integration measure, units, and normalization;
5. its central evaluation or sector policy;
6. its Euclidean, equilibrium, retarded, in-in, or other analytic prescription; and
7. the theorem or open map that gives it the claimed interpretation.

Changing one of these fields changes the response question even when the displayed kernel is unchanged.

## Canonical response ledger

| Term | Canonical type | Canonical owner |
|---|---|---|
| Hessian | second derivative or second variation of a named scalar or functional | [[basic-concepts/hessians/entry|Hessians]] |
| Fisher response | score covariance and local distinguishability of a classical parametric family | [[basic-concepts/hessians/fisher-response|Fisher response]] |
| BKM response | positive tangent form on faithful quantum states; one monotone quantum metric, not every quantum Fisher metric | [[basic-concepts/hessians/entry#Log-partition Hessians and Fisher geometry|Fisher and BKM geometry]] and [[hessian-response-geometry/bkm-selection-theorem|the BKM selection theorem]] |
| static susceptibility | derivative of an expectation with respect to a declared conjugate source | [[basic-concepts/hessians/fisher-response|Fisher response]] |
| Kubo real-time response | causal or frequency-dependent dynamical response with a time prescription | [[basic-concepts/hessians/entry#Actions, effective actions, and inverse covariance|functional Hessians and response]] |
| covariance | centered two-point fluctuation on a declared state or probability carrier | [[basic-concepts/hessians/entry|Hessians]] |
| probability or 1PI precision | inverse covariance or effective-action Hessian on a declared nondegenerate physical domain | [[basic-concepts/hessians/fourier-covariance-and-precision|Fourier covariance and precision]] |
| spectral multiplier or filter | functional-calculus operator with no automatic covariance or response interpretation | [[cauchy-spectral-envelope/entry|heat mixtures and Cauchy envelopes]] |
| center-valued response package | the central response density together with the inherited normal central law, before a consumer policy | [[program-core/center-valued-response|center-valued response and scalarization]] |
| common response form | the homogeneous, declared non-singlet observational, mixed, and hidden blocks on one physical tangent construction | [[program-core/common-response-form|the common response form]] |
| localized areal response | a measure-valued BKM form and its Radon--Nikodym density against independently normalized area | [[program-core/localized-areal-response-geometry|localized areal response geometry]] |
| scalar spatial precision | a three-dimensional inverse-covariance target for the wall scalar on a constructed physical carrier | [[causal-wall-spectral-theory/conjectures/bkm-to-spatial-precision|the scalar W2 conjecture]] |
| tensor spatial precision | a three-dimensional inverse-covariance target on a physical transverse-traceless two-polarization carrier | [[causal-wall-spectral-theory/conjectures/tt-bkm-to-spatial-precision|the tensor W2 conjecture]] |
| gravitational canonical energy | a quadratic form on physical gravitational perturbations in a declared covariant phase space | [[spectral-wall-descent/ads-calibration-and-ds-carrier|AdS calibration and the de Sitter carrier]] |
| capacity | a scalar contraction \(g(v,v)\) of a positive response form; not a linear charge or an action | [[program-core/symmetry-conservation-and-action|symmetry, conservation, and action]] |

## Exact same-carrier bridges

The reusable equalities are conditional theorems, not similarities of notation. For a regular classical exponential family in its natural coordinates,

$$
\operatorname{Hess}\psi
=I^{\mathrm F}
=\operatorname{Cov}.
$$

On a faithful commuting quantum family, the BKM form reduces to that Fisher covariance. For a regular Legendre pair on the same reduced physical domain,

$$
\Gamma^{(2)}
=\bigl(W^{(2)}\bigr)^{-1}.
$$

The linked Hessian and Fisher notes own the hypotheses and proofs. None of these identities changes carrier, supplies a causal prescription, or turns a state-space metric into a spacetime field equation.

## Central policy precedes scalar-valued or sector response

The canonical pre-consumer datum is

$$
\mathfrak G^Z
=(Z,\mathbf G^Z,\omega^Z).
$$

A scalar or sectorwise consumer must declare a policy

$$
\mathfrak G^Z
\xrightarrow{\ S_{\mathsf p}\ }
G^{\mathsf p}.
$$

Normal unconditioned evaluation, normalized conditional-sector geometry, algebraic character evaluation, and a post-instrument factual response are different policies. [[program-core/center-valued-response|The scalarization owner]] gives their exact relation, including the central Fisher term. A center-linear construction may instead retain the center throughout later carrier changes.

## Open carrier and interpretation changes

The project-specific arrows are longer than the same-carrier identities:

$$
G^{\mathsf p}
\dashrightarrow
\mu^{\mathrm{desc}}
\xrightarrow{\ \mathrm d/\mathrm d\mu_A\ }
\boldsymbol\chi,
$$

$$
G^{\mathsf p}_{NN}
\dashrightarrow
\rho_X,
$$

and the independent CWST branches

$$
\begin{aligned}
G^{\mathsf p}_{\zeta\zeta}
&\overset{\mathrm{W2}_{\mathrm s}}{\dashrightarrow}
\mathcal K^{\zeta}_{\mathrm{wall}}
\overset{\mathrm{W3}_{\mathrm s}}{\dashrightarrow}
\mathcal K_{\zeta_{\mathrm{cos}}},\\
G^{\mathsf p}_{\mathrm{TT}}
&\overset{\mathrm{W2}_{\mathrm t}}{\dashrightarrow}
\mathcal K^{\gamma}_{\mathrm{wall}}
\overset{\mathrm{W3}_{\mathrm t}}{\dashrightarrow}
\mathcal K_{\gamma_{\mathrm{cos}}}.
\end{aligned}
$$

Localization and comparison with area are open in [[program-core/localized-areal-response-geometry|the localized areal response construction]]. The CST response-to-density arrow is constitutive in [[causal-scale-theory/anchored-response-density-postulate|the homogeneous source note]]. Scalar and tensor W2 maps own distinct spatial carriers; scalar and tensor W3 maps own distinct Lorentzian field realizations. [[causal-wall-spectral-theory/holographic-spectral-adapter|The holographic adapter]] is a conditional factorization of selected source/response arrows, not a same-carrier identity and not a replacement for W3. A scoped equality between retained Fisher response and gravitational canonical energy does not make every BKM form gravitational.

Accordingly,

$$
\text{BKM response}
\ne
\text{Kubo response}
\ne
\text{spatial precision}
\ne
\text{areal modulus}
\ne
\text{canonical energy}
$$

unless the intervening maps are constructed with one compatible carrier ledger. [[program-core/operation-registers|The operation register]] types those arrows; [[program-core/ontological-registers|the ontological register]] types their inputs and outputs.
