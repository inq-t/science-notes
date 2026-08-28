---
inq.module: "bianchi-protection-of-the-areal-modulus"
inq.include:
  - "**/*.md"
---
# Bianchi Protection of the Areal Modulus

In a connected nonvacuum Einstein fiber, a homogeneous spacetime-dependent gravitational calibration is incompatible with both the contracted Bianchi identity and covariant conservation of the total source. Under explicit assumptions, the Einstein coupling and areal modulus must therefore be constant on each connected nonvacuum interval. This is a consistency or no-go theorem for a variable-coupling Einstein ansatz, not a dynamical propagation law through the wall, and it does not calculate the calibration.

## The meaning

The fossil question contains two logically independent problems:

1. **calibration:** why does the state--geometry interface have this inverse-area modulus?;
2. **Einstein-fiber consistency:** can that modulus vary while the observable branch retains ordinary Einstein form and a conserved total source?

[[crossing-evaluated-flat-modulus/inq|The crossing-evaluated construction]] addresses the type of the first question. The Bianchi identity answers the second once the observable branch has ordinary Einstein form. It is therefore wrong to ask Bianchi covariance to select \(H_c\), \(m_*\), \(s_*\), or \(\zeta\), or to carry a datum across a singular or distributional wall. Its force is narrower: a smooth time-dependent coefficient cannot be inserted into an otherwise unchanged Einstein equation while the other assumptions remain intact.

## Conditional theorem

Let a connected Lorentzian region satisfy

$$
G_{ab}+\Lambda g_{ab}
=\kappa(x)T_{ab},
$$

with the following hypotheses:

1. the field equation has exact Einstein form;
2. \(\Lambda\) is spacetime constant;
3. the total stress tensor on the right-hand side is covariantly conserved,
   \(\nabla^aT_{ab}=0\), although its internal components may exchange energy;
4. \(\kappa=\kappa(t)\) is smooth and homogeneous in an FLRW region; and
5. the comoving energy density is nonzero.

The contracted Bianchi identity and metric compatibility give

$$
\nabla^aG_{ab}=0,
\qquad
\nabla^ag_{ab}=0.
$$

Taking the divergence of the field equation yields

$$
0
=\nabla^a(\kappa T_{ab})
=T_{ab}\nabla^a\kappa
+\kappa\nabla^aT_{ab}
=T_{ab}\nabla^a\kappa.
$$

In geometrized units, write the perfect-fluid stress tensor as

$$
T_{ab}
=(\varepsilon+p)u_au_b+pg_{ab},
$$

and homogeneity as \(\nabla_a\kappa=-\dot\kappa u_a\), with the displayed sign depending on the metric convention. Contracting with the comoving temporal direction gives

$$
\varepsilon\dot\kappa=0.
$$

On every connected interval where \(\varepsilon\ne0\),

$$
\boxed{
\dot\kappa=0.
}
$$

For the Einstein entropy--area density

$$
\eta_E:=\frac{c^3}{4\hbar G},
$$

the coupling can be written in either form

$$
\kappa
=\frac{8\pi G}{c^4}
=\frac{2\pi}{\hbar c\,\eta_E}.
$$

Consequently,

$$
\boxed{
\dot\kappa=0
\quad\Longleftrightarrow\quad
\dot G=0
\quad\Longleftrightarrow\quad
\dot\eta_E=0
}
$$

where the quantities are finite and positive.

The component identity is independently exercised by `inbox/the-carrier-and-zeta/carrier_zeta_receipts.py`.

## What the theorem does and does not say

The theorem establishes **path constancy within a smooth nonvacuum Einstein region**. It does not establish:

- the value of \(G\) or \(\eta_E\);
- equality between a BKM response and \(\eta_E\);
- the existence or naturality of a crossing event;
- constancy across different solutions;
- renormalization-group scale independence of every effective gravitational operator; or
- conservation of horizon entropy, accessible matter energy, or information.

In particular, it does not evolve an initial value through a distributional crossing or prove that the pre-wall and post-wall coefficients agree. That requires a junction condition, record map, top-form constraint, or another wall construction.

This distinction matches [[program-core/ontological-registers|the programme's register discipline]]: a pathwise constant, a presentation-invariant scalar, a model parameter, and a universal coefficient are not interchangeable claims.

The local thermodynamic route of [[deriving-g-v2/the-g-free-first-law|the G-free first law]] reaches the same boundary from another direction. The dimensionless relation between heat and ledger variation is independent of \(G\); \(G\) enters only through the conversion between area and ledger. Jacobson's primary horizon-equilibrium derivation, archived in [[deriving-value-of-g/sources/entry|the G source ledger]], likewise assumes a universal entropy density rather than calculating it.

[[philosophy/noether-conservation/second-theorem-and-gauge|The second Noether theorem]] owns the distinction between the off-shell Bianchi identity and the separate matter conservation premise. [[compatible-with-existing-physics/local-physics-interface|The local physics interface]] requires the same consistency from any imported GR--QFT fiber.

## Flux is compatible with a fixed modulus

Covariant conservation of the total stress tensor does not say that the energy inside a moving apparent horizon is constant. The subsystem boundary changes, and energy crosses it.

For a spatially flat FLRW apparent horizon \(R_A=c/H\), let \(\varepsilon\) and \(p\) denote physical energy density and pressure. A standard signed Kodama/apparent-horizon energy-supply convention gives

$$
P_A
=(\varepsilon+p)A_Ac
=\left(-\frac{\dot H}{H^2}\right)
\frac{c^5}{G}
=(1+q)\frac{c^5}{G},
$$

with the sign reversed when the horizon orientation is reversed; \(|P_A|\) is the corresponding magnitude. The factor \(c\) enters through \(HR_A=c\) in the horizon energy-supply law, not through a claim that ordinary matter crosses the boundary at speed \(c\). [[deriving-g-v2/the-leak-register|The leak register]] owns this calculation and its interpretation boundary.

The modulus can therefore be fixed while the physical flux varies:

$$
\partial_N\eta_E=0,
\qquad
\frac{P_A}{c^5/G}=1+q(N).
$$

This is the precise version of “the cosmos leaks without losing its law.” A flux-inclusive balance has the form

$$
Q_\xi[\Sigma_2]-Q_\xi[\Sigma_1]
+\mathcal F_\xi[W]=0,
$$

not \(Q_\xi[\Sigma_2]=Q_\xi[\Sigma_1]\) for an open subsystem. [[conservation-of-causal-charge/diagonal-charge-balance|Diagonal charge balance]] states the exact Hamiltonian template, while [[flux-record-and-top-form-realizations/inq|the realization module]] keeps Noether flux distinct from K-theory boundary maps and top-form flux.

## One coefficient under three restrictions

If a wall construction independently produces one \(\eta_*\), the theory faces a three-register consistency test:

$$
\boxed{
\eta_*
\stackrel{?}{=}
\frac{1}{4\ell_P^2}
\stackrel{?}{=}
\frac{cM}{2\hbar r_s}
\stackrel{?}{=}
\frac{\gamma s_*}{3}
\frac{c}{H_c\lambda_*^3}.
}
$$

The statuses are different:

- \(1/(4\ell_P^2)\) is a Planck-unit translation once \(G\) is already known;
- \(cM/(2\hbar r_s)\) follows exactly from the Schwarzschild relation \(r_s=2GM/c^2\);
- the last expression is the conditional fossil bulk-cell closure of [[bulk-area-cell-normalization/inq|the normalization module]].

[[conservation-of-causal-charge/black-hole-saturation-boundary|Black holes as a saturation boundary]] explains why the Schwarzschild equality is a stringent local restriction without making it an independent derivation. [[program-core/causal-capacity-equivalence|Causal-capacity equivalence]] requires the same coefficient in focusing, lensing, waves, cosmology, and horizon entropy.

For the cosmological restriction,

$$
H_c=H_0E(z_c).
$$

Uncalibrated supernova distances constrain the dimensionless luminosity-distance curve, which integrates \(1/E(z)\); they do not determine \(E(z)\) or the event address \(z_c\) model-independently. A parametric forward fit constrains \(E(z)\) and infers \(z_c\) only after the profile and selector define the event. Cepheids or another absolute ruler are then required to determine \(H_0\) and hence \(H_c\). Even then, the data test the right-hand side of the closure; they do not observe the microscopic wall.

The normalized flux shadow is G-free:

$$
\boxed{
\frac{P_A(z)}{c^5/G}
=1+q(z)
=(1+z)\frac{\mathrm d\ln E}{\mathrm dz}.
}
$$

Supernovae measure an integral of \(H^{-1}\), so differentiating a reconstructed Hubble diagram is covariance-sensitive. [[causal-scale-theory/receipts/fit-late-time-background|Forward fitting the distance law]] is the controlled test; calling the result a direct observation of wall flux would be too strong.

## Why index persistence is not Bianchi protection

Under a specified norm-continuous homotopy or a proved Morita equivalence, an assembled K-class can remain unchanged while local operator representatives flow. That kind of invariance is a useful structural rhyme, developed in [[spectral-wall-descent/index-and-curvature-transgression|index and curvature transgression]]. A generic changing family has no such guarantee. In either case K-theoretic invariance is not the differential identity \(\nabla^aG_{ab}=0\), does not imply \(\nabla^aT_{ab}=0\), and cannot replace the theorem above.

Conversely, Bianchi protection says nothing about whether the wall possesses a stable K-class. The proposed Baum--Connes naturality square in [[flux-record-and-top-form-realizations/inq|the assembly analysis]] is ancillary to this module, not a premise of its proof.

## Escape routes and failure conditions

The conclusion changes when any hypothesis changes. Important cases include:

- a spacetime-dependent \(\Lambda\) whose gradient compensates \(\nabla\kappa\);
- scalar--tensor or nonminimal theories in which derivative terms of the coupling belong on the geometric side;
- exchange between the displayed matter sector and an omitted sector, so \(\nabla^aT_{ab}\ne0\) for the subsystem;
- a quantum anomaly or approximation that violates the assumed conservation law;
- a vacuum region where \(T_{ab}\nabla^a\kappa=0\) is degenerate; and
- a distributional wall across which junction or source terms must be included.

In covariant modified gravity the Bianchi identity still holds, but it constrains the complete equations rather than forcing the isolated coefficient above to be constant. A successful fossil theory must therefore show both that the post-wall restriction is genuinely Einstein-class and that any wall source satisfies the corresponding junction balance.

[[vendor/entropic-gravity/jacobson-non-equilibrium-thermodynamics|Jacobson's non-equilibrium extension]] shows why a varying entropy density generally introduces additional production terms rather than leaving Einstein form untouched. Iyer and Wald, archived in [[deriving-value-of-g/sources/entry|the G source ledger]], and [[library/wald-zoupas-conserved-quantities/inq|Wald and Zoupas]] provide the primary covariant phase-space precedents for treating boundary charges and fluxes without pretending that a changing subsystem quantity violates the underlying identity.
