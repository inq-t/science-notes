# The State--Geometry Charge Weld

Causal charge and causal capacity have different mathematical types. The state--geometry conjecture proposes a canonical same-tangent map from horizontal BKM response to gravitational canonical energy, together with a locally additive areal capacity measure. This would make geometry a representation of residual causal susceptibility and would give \(G\) the meaning of geometric compliance rather than an information addend.

## The horizontal state tangent

For a scale-indexed family, first construct

$$
N\longmapsto
(\Sigma_N,\mathcal A_N,\omega_N,\mathcal T_{N_2N_1}),
$$

where \(\mathcal T_{N_2N_1}\) supplies a valid comparison between fibers. After removing vertical modular-frame and central-normalization directions, let \(v_N\) be the physical horizontal tangent and define

$$
G^{\perp}_{NN}
:=g^{\mathrm{BKM}}_{\omega_N}(v_N,v_N).
$$

This is a squared speed or susceptibility. It is not the modular charge itself, and it is not automatically the entanglement capacity of the same state. [[deriving-value-of-g/causal-scale-derivation-target|The causal-scale derivation target]] records the tangent and normalization obstructions.

## Same-tangent conjecture

Suppose a soldering map sends the state tangent to a gravitational perturbation,

$$
\mathfrak S_\Sigma:
T_\omega\mathcal P_\Sigma^{\mathrm{state}}
\longrightarrow
T_g\mathcal P_\Sigma^{\mathrm{grav}}.
$$

The first conjectural requirement is a same-tangent isometry

$$
\boxed{
g^{\mathrm{BKM}}_\omega(v,v)
=Z_g\,
\mathcal E_{\mathrm{can}}^{(1)}
\bigl(\mathfrak S_\Sigma v,
\mathfrak S_\Sigma v\bigr),
}
$$

where \(\mathcal E_{\mathrm{can}}^{(1)}\) is computed from a unit-normalized gravitational kinetic term and \(Z_g\) remains symbolic. Existing controlled BKM--canonical-energy identities motivate the form. Inserting the measured gravitational normalization before computing the wall side would make the argument circular.

## Areal capacity measure

For measurable patches \(U\subseteq\Sigma\), require the renormalized horizontal norm to define a positive, countably additive measure

$$
\mu_{\mathrm{BKM}}^\perp(U)
:=G^{\perp}_{NN,\mathrm{ren}}[U].
$$

Let \(\mu_A\) be an independently normalized area measure. The strong Einstein-regime conjecture is

$$
\mu_{\mathrm{BKM}}^\perp\ll\mu_A,
\qquad
\boxed{
\frac{\mathrm d\mu_{\mathrm{BKM}}^\perp}
{\mathrm d\mu_A}
=\chi_*>0
}
$$

with \(\chi_*\) constant throughout a declared universality class of causal cuts. This is stronger than extensive scaling on one cosmological horizon.

The second weld is the independently derived entropy variation

$$
\delta\!\left(\frac{S_{\mathrm{hor}}}{k_B}\right)
=\chi_*\,\delta A.
$$

Together these give

$$
\chi_*
=\frac{c^3}{4G\hbar},
\qquad
G_{\mathrm{pred}}
=\frac{c^3}{4\hbar\chi_*}.
$$

Thus \(G\) is the inverse areal stiffness of causal capacity. The binary channel can fix a dimensionless profile but cannot determine the number of channels per square metre; this is the dimensional obstruction in [[deriving-value-of-g/obstructions-to-an-unconditional-proof|the obstruction audit]].

## Relation to the unit Ruble law

At a self-dual cut, the same weld would imply

$$
G^{\perp}_{NN}(N_c)
=\chi_*A_c
=\frac{S_c}{k_B},
$$

and hence

$$
\mathfrak R_c
:=\frac{k_B}{S_c}G^{\perp}_{NN}(N_c)
=1.
$$

[[deriving-value-of-g/noether-capacity-theorem|The Noether--capacity theorem]] gives one sufficient route under strong conformal-thermal and tangent-alignment hypotheses. The wall theory has not yet derived those hypotheses.

## What would refute the weld

The conjecture fails or changes universality class if the BKM measure is not local, finite, positive, or regulator independent; if its areal density depends uncontrollably on species or state; if the state and gravitational quadratic forms concern different tangents; if the normalization imports \(G\); or if local, cosmological, wave, lensing, and entropy measurements return inequivalent effective moduli.

The required source, target, equivariance, nondegeneracy, and preservation tests are instances of [[basic-concepts/soldering/entry|strict soldering discipline]].
