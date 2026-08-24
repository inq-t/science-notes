# The Ruble Quotient and Its Possible Flows

The Ruble quantity is best defined as a dimensionless quotient comparing two independently normalized inverse-area moduli: the horizontal state-space capacity per causal area and the gravitational entropy capacity per causal area. Its value at the self-dual crossing is a distinguished evaluation; calling it constant, a fixed point, or a running coupling requires additional and mutually different structures.

## Two moduli

Suppose the renormalized horizontal BKM norm defines a local measure on an admissible causal cut $\Sigma$:

$$
\mu^\perp_{\mathrm{BKM}}(U)
=G^\perp_{NN,\mathrm{ren}}[U].
$$

Its areal density is

$$
\chi_{\downarrow}[\Sigma,\omega,v_N]
:=
\frac{\mathrm d\mu^\perp_{\mathrm{BKM}}}
{\mathrm d\mu_A}.
$$

Separately, in the Einstein regime define the gravitational entropy--area density

$$
\eta_{\mathrm E}
:=
\frac{\mathrm d(S_{\mathrm{hor}}/k_B)}
{\mathrm dA}
=\frac{c^3}{4\hbar G}.
$$

The two coefficients have the same units, $L^{-2}$, but different origins. The left is to be calculated from horizontal state geometry; the right is measured through horizon entropy or gravitational focusing. Using one to normalize the other before comparison makes the proposed equality circular.

## Definition of the quotient

Whenever both moduli are defined on the same physical cut and in compatible prescriptions, define

$$
\boxed{
\mathfrak R[\Sigma,\omega,v_N]
:=
\frac{\chi_{\downarrow}[\Sigma,\omega,v_N]}
{\eta_{\mathrm E}[\Sigma]}.
}
$$

At a self-dual cut $\Sigma_c$, with a linear area law and the required extensivity,

$$
\mathfrak R_c
=\frac{k_B}{S_c}G^\perp_{NN}(N_c).
$$

The subscript $c$ denotes evaluation at the crossing. It does not assert constancy along the full state path.

## Meaning of unity

The proposed unit law

$$
\boxed{\mathfrak R_c=1}
$$

means

$$
\chi_{\downarrow,c}=\eta_{\mathrm E,c}.
$$

The physical content is the equality of two independently typed response coefficients. The numeral one contains no new dimensional information. In this respect the quotient is closer to an equivalence-principle ratio than to a new coupling constant:

$$
\frac{\text{state capacity per area}}
{\text{gravitational capacity per area}}
=1.
$$

The conditional [[deriving-value-of-g/noether-capacity-theorem|Noether--Capacity Theorem]] gives one route to unity if the physical scale tangent is a unit escort tangent of a genuine $1+1$ conformal thermal channel and the same regulated entropy is horizon entropy. The current wall construction has not established those hypotheses.

## Four notions of variation

### State dependence

A fixed functional may have different values on different states:

$$
\mathfrak R:\mathfrak S_{\mathrm{adm}}\longrightarrow\mathbb R_+.
$$

The law defining the functional can be universal even when its output varies. This is a state-response law, not a numerical constant.

### Horizontal causal-scale flow

Along $N\mapsto(\Sigma_N,\omega_N,v_N)$, one may seek

$$
\frac{D\mathfrak R}{\mathrm dN}
=\beta^{\mathrm{hor}}_{\mathfrak R}
(\mathfrak R,\nu,\lambda_I,\ldots).
$$

This would describe change along a physical scale-state path. It is not automatically renormalization-group flow.

### Renormalization-group running

If $\mathfrak R(\mu)$ multiplies an operator in a renormalized effective action or algebraic scaling limit, then

$$
\mu\frac{\mathrm d\mathfrak R}{\mathrm d\mu}
=\beta_{\mathfrak R}
$$

would define genuine running. This requires an operator basis, regulator, subtraction scheme, thresholds, and a relation between $\mu$ and the physical wall construction.

### Change of universality class

Dependence on curvature, matter species, state, observer, or causal cut may indicate not running within one theory but a change of constitutive regime. A curvature-dependent modulus suggests higher-curvature gravity; a spacetime-dependent modulus suggests a varying-$G$ or scalar--tensor sector; an uncontrolled species dependence violates the desired universality.

## Matching is not a fixed point

The statements

$$
\mathfrak R(N_c)=1,
\qquad
\beta_{\mathfrak R}(1)=0,
\qquad
\mathfrak R(N)=1\ \text{for every }N
$$

mean respectively:

1. the path passes through unit matching at a distinguished cut;
2. unity is a fixed point of a declared flow; and
3. state and geometry remain exactly matched throughout the domain.

Only the first is presently proposed by the unit-amplitude principle. A self-dual point fixes the location of a symmetric extremum but does not determine its Hessian or prove a fixed-point equation.

## Relation to effective $G$

The quotient gives the conditional expression

$$
G_{\mathrm{eff}}
=\frac{\mathfrak R_\Sigma c^3}
{4\hbar\chi_{\downarrow}}.
$$

This is explanatory only if $\chi_{\downarrow}$ and $\mathfrak R_\Sigma$ are obtained without importing the desired gravitational coefficient. If $\eta_{\mathrm E}$ was defined from measured $G$ and then used to form $\mathfrak R$, the equation is a cross-calibration or consistency identity.

## Provisional naming judgment

- **Ruble quotient** is the safest current name.
- **Ruble functional** is appropriate when emphasizing its state and cut arguments.
- **Ruble coupling** is appropriate only if it multiplies a physical interaction or response term.
- **Running Ruble coupling** requires a genuine renormalization or coarse-graining flow.
- **Ruble fixed point** requires a beta function with $\beta_{\mathfrak R}(1)=0$.
- **Ruble's Constant** should not be the canonical mathematical type until universality and constancy are proved.
