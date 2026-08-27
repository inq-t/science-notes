# Connes Time as an Algebraic Dimension

Connes' modular theory supplies exactly the kind of temporal distinction of *type* needed by the causal-scale programme: spatial directions belong to the object being observed, whereas modular time is a one-parameter automorphism direction of the observable algebra relative to a state or weight. A faithful weight gives a local representative of the flow; Connes' cocycle compares representatives; their common outer class is attached to the algebra. None of this yet supplies a causal arrow, a clock duration, cosmic expansion, or proper time. The proposed grain enters where a positive one-sided global-to-local realization adjoins an oriented inclusion/translation order to this reversible flow and gives the realization one discrete unit of causal scale.

## The meaning

Ordinary coordinate language treats time as though it were one more entry in

$$
(x^1,x^2,x^3,t).
$$

The modular-algebraic picture has a different grammar:

$$
\boxed{
\text{space localizes observables within an object},
\qquad
\text{modular time acts on the algebra of observables}.
}
$$

The temporal parameter therefore does not initially label a point of the same carrier as the spatial coordinates. It labels an automorphism:

$$
t
\longmapsto
\sigma_t^\varphi
\in
\operatorname{Aut}(M).
$$

This is the exact sense in which the time dimension is unlike the others. It is a direction of algebraic change rather than a further component of the local object.

## State-relative modular flow

Let \(M\) be a von Neumann algebra and let \(\varphi\) be a faithful normal state or faithful normal semifinite weight. Tomita--Takesaki theory supplies the modular automorphism group

$$
\sigma^\varphi:
\mathbb R
\longrightarrow
\operatorname{Aut}(M),
\qquad
\sigma_{t+s}^\varphi
=
\sigma_t^\varphi\circ\sigma_s^\varphi.
$$

In a standard vector representation,

$$
\sigma_t^\varphi(x)
=
\Delta_\varphi^{it}x\Delta_\varphi^{-it}.
$$

The parameter \(t\) is an algebraic, dimensionless modular parameter. A physical duration is not present until a clock or thermal normalization is supplied.

For a finite Gibbs state

$$
\rho
=
\frac{e^{-\beta H}}{Z},
$$

one has, in a common Heisenberg convention,

$$
\sigma_t^\rho(A)
=
\rho^{it}A\rho^{-it}
=
\alpha_{-\beta\hbar t}(A).
$$

The sign depends on the convention for the physical automorphism group, but the type distinction does not: \(\beta\hbar\) converts a dimensionless modular parameter into a metric duration. Outside such a KMS identification, modular time is not already the reading of a laboratory clock.

The Connes--Rovelli thermal-time hypothesis proposes that the physical time flow of a generally covariant system is selected by its thermodynamic state through this modular group. The modular group itself is theorem-level; its identification with physical time is a physical hypothesis.

## Global outer time and local clock representatives

For two faithful normal states or weights \(\varphi\) and \(\psi\), the Connes cocycle derivative satisfies

$$
\sigma_t^\varphi(x)
=
(D\varphi:D\psi)_t\,
\sigma_t^\psi(x)\,
(D\varphi:D\psi)_t^*.
$$

The two flows therefore differ by an inner cocycle. Their common image

$$
\boxed{
\delta_M(t)
:=
[\sigma_t^\varphi]
\in
\operatorname{Out}(M)
}
$$

is independent of the chosen faithful weight. This gives a particularly exact global/local dictionary:

| Register | Algebraic object |
|---|---|
| global, presentation-independent temporal structure | the outer modular flow \(\delta_M:\mathbb R\to\operatorname{Out}(M)\) |
| local state or reference presentation | a faithful weight \(\varphi\) |
| local representative of the temporal flow | \(\sigma_t^\varphi\in\operatorname{Aut}(M)\) |
| comparison of local representatives | the cocycle \((D\varphi:D\psi)_t\) |

The global object is not a universal clock reading. It is the invariant class of possible algebraic clocks. A state selects a representative without making that representative absolute.

This is the natural Connes-level interpretation of the project's claim that causal ordering is relative to the global/local division while clock time is relative to a local frame.

There is an important size firewall. For a finite full matrix algebra \(M_n(\mathbb C)\), every automorphism is inner, so the outer modular flow is trivial. The finite exceptional/Jordan flags can organize a local complex context, but they cannot by themselves carry a nontrivial Connes outer time. That role requires the appropriate infinite observable algebra, such as the type-III local algebras imported from algebraic QFT, together with a proved relation to the finite context data.

## Four structures that must not be called the same time

### Modular automorphism flow

$$
\sigma_t^\varphi\in\operatorname{Aut}(M)
$$

is reversible and state-relative. By itself it has no preferred future half-line.

### The canonical core and its dual action

The crossed product

$$
\widetilde M
\simeq
M\rtimes_{\sigma^\varphi}\mathbb R
$$

can be made independent of the chosen faithful weight. It carries a dual action \(\theta_s\) and a semifinite trace \(\widetilde\tau\) with a convention such as

$$
\widetilde\tau\circ\theta_s
=
e^{-s}\widetilde\tau.
$$

This trace-scaling action is an algebraic scale flow. It does not become cosmological expansion, production of time, or a physical clock merely because its parameter is logarithmic.

The Connes--Takesaki flow of weights is the induced action on \(Z(\widetilde M)\), the center of the core. It must not be conflated with the dual action on the whole core. In the type-\(\mathrm{III}_1\) factor case the core center is trivial, so the ordinary flow of weights is trivial even though the dual action still scales the core trace.

### Causal order

A positive cone, inclusion, or compression semigroup supplies a one-sided relation such as

$$
S_W
=
\{g:\operatorname{Ad}_gM(W)\subseteq M(W)\}.
$$

This is the candidate pre-clock order. A reversible modular group can help construct such a semigroup through a half-sided modular inclusion, but the direction comes from the one-sided inclusion and positivity, not from the group law alone.

### Record, proper, conformal, and scale time

Record order is the compositional order of persistent facts. Proper time \(\tau\) is metric length along a timelike worldline. Conformal time satisfies \(d\eta=d\tau/a\) in FLRW. Scale-age is

$$
N=\ln\frac{a}{a_*},
\qquad
dN=H\,d\tau,
$$

along a declared expanding branch, while Misner's logarithmic time is \(\Omega=-N\). These are downstream geometric and historical readings. None is identical to \(t\), \(s\), or a Connes cocycle parameter without a soldering map.

## The causal grain is not a modular tick

Every nontrivial continuous one-parameter group has arbitrarily small positive parameters. Modular flow therefore has no canonical smallest interval:

$$
t>0
\quad\Longrightarrow\quad
\frac{t}{n}>0
\quad(n>1).
$$

The grain cannot be extracted from continuity alone. Its proposed construction needs a discrete event or index:

$$
\boxed{
\text{outer modular possibility}
\longrightarrow
\text{local modular representative}
\longrightarrow
\text{positive one-sided wall}
\xrightarrow{\ \nu=+1\ }
\text{fact and record}.
}
$$

The valuation of that primitive wall event may then be soldered to one unit of logarithmic scale. Thus:

- Connes time supplies the algebraic *kind* of temporal transformation;
- positivity and half-sidedness supply an oriented inclusion/translation order relative to a local algebra, without making the modular group irreversible;
- the wall index supplies discreteness;
- record composition supplies irreversible history; and
- metric and thermal soldering supply seconds.

The grain is one unit of causal realization and scale, not one equal step of the continuous modular parameter.

## The \(S^6\) fibered reading

In [[inbox/causal-grain-cmb-spectroscopy/s6-positivity-integrability-duality|the \(S^6\) positivity--integrability model]], each octonionic imaginary unit

$$
u\in S^6\cong G_2/SU(3)
$$

selects an associative complex observable fiber

$$
u
\longmapsto
\mathcal A_u,
\qquad
\varphi_u
\in
\mathcal W_{\mathrm{faithful}}(\mathcal A_u).
$$

The first assignment is the choice of associative context. The faithful weight is independent state-section data on that fiber; selecting \(u\) does not by itself select \(\varphi_u\).

There are then two independent reversible comparisons:

1. \(G_2\)-transport compares which complex slice \(u\) is used;
2. the Connes cocycle compares which faithful weight is used in one slice.

The causal descent is the additional noninvertible arrow that realizes one context and one record. Schematically,

$$
\begin{array}{ccc}
\text{exceptional positive whole}
&\longrightarrow&
[S^6/G_2]\text{ of complex contexts}
\\[2mm]
&&\downarrow\ \text{choose }u\text{ and independently supply }\varphi_u
\\[2mm]
&&(\mathcal A_u,\sigma_t^{\varphi_u})
\\[2mm]
&&\downarrow\ \text{positive wall and record}
\\[2mm]
&&\text{oriented local history}.
\end{array}
$$

The higher symmetry is therefore a covariance among possible local complex contexts and possible modular clocks. Energy conservation appears only after one selected flow is unitarily implemented in a physical representation by a self-adjoint Hamiltonian and the local dynamics has the corresponding time-translation invariance.

## The CMB clock solder

The CMB is an unusually apt thermal-time laboratory. Its monopole is an exceptionally accurate blackbody, while the anisotropies and polarization are small, coherent departures propagated through an expanding plasma. A reference photon-bath state \(\varphi_\gamma\) can therefore be asked to supply a modular flow, with perturbations treated relative to that state. The expanding recombination-era universe is not one exact global equilibrium KMS system, however, so an adiabatic family of weights or a genuinely nonequilibrium construction would have to be derived rather than assumed.

The Einstein--Boltzmann description uses conformal time:

$$
\theta_k(\eta_*)
=
\int^{\eta_*}kc_s(\eta)\,\mathrm d\eta.
$$

A Connes-level explanation cannot merely rename \(\eta\) as modular time. It must construct a clock solder

$$
\mathcal T_{\varphi,u}:
\mathrm dt_{\mathrm{mod}}
\longmapsto
\mathrm d\eta
$$

such that

$$
\int
\omega_{k,\varphi,u}^{\mathrm{mod}}\,
\mathrm dt_{\mathrm{mod}}
=
\int
kc_s(\eta)\,\mathrm d\eta.
$$

If one global outer flow and one natural family of local lifts generate one primordial state/covariance and, after the clock solder, one photon--baryon growing-mode phase, then TT, TE, and EE inherit their acoustic phase relations through distinct fixed kernels. Lensing and matter are separately calculated descendants of the same primordial state, background, and covariant response rather than additional quadratures of the acoustic oscillator. The CMB peak system could then be a fossil of an algebraically unified clock rather than a collection of independently fitted source phases.

That gives the model a strong compression target:

$$
\boxed{
\text{one outer temporal structure}
+
\text{one positive causal orientation}
+
\text{one clock solder}
\longrightarrow
\text{the common TT/TE/EE phase family}.
}
$$

A log-periodic residual is secondary. The primary explanatory success would be to derive the already observed phase coherence and local transfer geometry with fewer independent temporal inputs.

## Claim grades

| Statement | Grade |
|---|---|
| a faithful normal state or weight determines a modular automorphism group | theorem |
| faithful weights give modular groups with one common class in \(\operatorname{Out}(M)\) | theorem |
| a finite matrix context has a nontrivial outer modular time | false; its automorphisms are inner |
| the canonical core carries a trace-scaling dual action | theorem |
| the dual action, flow of weights, modular flow, and physical time are one object | false conflation |
| thermal time identifies a state's modular flow with physical dynamics | physical hypothesis |
| a positive half-sided inclusion supplies causal orientation | theorem under half-sided modular hypotheses; physical use proposed |
| the wall index gives a primitive causal-scale unit | programme conjecture |
| one outer flow and one clock solder explain the common CMB phase | principal empirical construction target |
