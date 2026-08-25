# Scale as a Modular Observable

The proposal is to treat cosmological scale as a physical register whose change is represented by a horizontal path through quantum states. The relevant observable is not ordinary modular flow at one fixed state, but the information-geometric response of a family of states as the scale changes; [[observable-map]] states the construction precisely.

This is a promising research programme, not a closed derivation of dark energy. Its reduced balanced-binary algebra is exact, and its homogeneous cosmology is rigid once the closure laws are granted. The construction of the required FLRW state family, the amplitude law, and the spacetime perturbation theory remain open.

> [!warning] Status of the long document
> [[scale-as-modular-observable/misc/scale-as-a-modular-observable|Scale as a Modular Observable — Revision 2]] is the latest long synthesis in this folder, but it is not free of errors. In particular, conformal weights do not force an integer soldering slope, and a two-dimensional normal plane is not automatically a two-dimensional CFT to which Cardy's formula applies. [[claim-audit]] gives the corrected status of its arguments; the chronological record remains under `chats/`.

## Construction

1. [[conformal-scale-geometry/causal-order-and-metric-scale|Causal order]] determines conformal geometry but leaves a positive scale section unspecified.
2. [[wall-construction-interface/vertical-and-horizontal-motion|Vertical modular flow]] is separated from horizontal motion through a scale-indexed family of states.
3. [[binary-information-geometry/entry|Normal chirality]] is proposed as the reduced homogeneous horizontal degree of freedom.
4. [[basic-concepts/soldering/affine-scale-state|Cocycle soldering]] gives a logarithmic state coordinate, conditional on ratio dependence, rank-one generation, and regularity.
5. [[program-core/ruble-equations#RE6 — Integrated reference matching|Weak unit matching]] and [[causal-scale-theory/anchored-response-density-postulate|the modular source law]] are additional physical inputs; [[conformal-scale-geometry/hawking-friedmann-identity|the horizon conversion]] supplies units.
6. The [[causal-scale-theory/unit-branch|conditional homogeneous response]] then follows on the unit branch.
7. [[binary-information-geometry/witten-darboux|The binary Witten pair]] is exact internal geometry, while its physical perturbation lift is still missing.

## Central conditional result

Use the normalized convention

$$
N:=\ln\frac{a}{a_0},
\qquad
N_c:=\ln\frac{a_c}{a_0},
\qquad
x:=N-N_c.
$$

If the active horizontal quotient is a balanced binary, the scale--state map has unit slope, the integrated reference matching ratio is one, and the proposed source and horizon-conversion laws hold, then

$$
\rho_X(N)
=\frac12\rho_{\mathrm{crit},c}\operatorname{sech}^2x,
$$

and separate conservation gives

$$
w_X(N)=-1+\frac23\tanh x,
$$

with the amplitude- and date-independent shape test

$$
9(1+w_X)^2+6\frac{\mathrm dw_X}{\mathrm dN}=4.
$$

These are deductions from the stated premises, not independent evidence for those premises.

## Claim ledger

| Status | Content |
|---|---|
| Exact after balanced binary reduction | exponential family, BKM metric, self-dual relative entropy, internal Witten factorization |
| Conditional mathematics | affine logarithmic soldering under its cocycle hypotheses; equation of state and shape invariant after the density profile and separate conservation are supplied |
| Physical choices or principles | binary normal reduction, unit slope, scale--capacity equivalence, all-history source law, horizontal horizon temperature |
| Background assumptions | flat FLRW, separate conservation, measured ordinary abundances, expanding branch, selected residual sector |
| Open | [[open-problems|explicit wall algebra and states, direct cocycle, covariant response tensor, perturbations, stability, and full likelihood analysis]] |
| Rejected | integrality of the soldering slope from conformal weights; normal-plane dimension implying a 2D CFT and Cardy capacity |
