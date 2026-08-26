# The Core-Scale Constitutive Signature

The three proposed signature axioms define a promising operator-algebraic schema for cosmodynamics, not yet one new operator. Their exact content is a canonical core with trace-scaling covariance, pointed spectral cuts, and normal state members; their proposed physical content is that this structure supplies cosmic scale and its local presentations. The distinction between those two contents must remain explicit.

## The present posit

The source proposal may be written as

$$
\begin{aligned}
\mathrm{S1}:&\quad O\longmapsto M(O),
&&\text{a local type-}\mathrm{III}_1\text{ net},\\
\mathrm{S2}:&\quad(\mathcal C,\tau,\beta_s,e_N),
&&\tau\circ\beta_s=e^s\tau,
\quad\beta_s(e_N)=e_{N+s},
\quad\tau(e_N)=e^N,\\
\mathrm{S3}:&\quad\Omega_d,
&&\text{a faithful normal state on }\mathcal C.
\end{aligned}
$$

S1 is an imported AQFT-type local carrier assumption, whose exact scope depends on the chosen net and hypotheses. S2 uses standard continuous-core mathematics and the exact pointed filtration constructed in [[wall-construction-interface/core-spectral-wall|The Core Spectral Wall]]. S3 selects a member of the state class. The physical identification of core trace scale with cosmic scale is **[PROPOSED CONSTITUTIVE LAW]**, not a consequence of the core theorem alone.

The phrase *operator signature* is potentially ambiguous: it can suggest metric signature, principal-symbol signature, or spectral-triple sign data. The more precise project term is **core-scale constitutive signature**: a typed package of carriers and covariance laws defining a class of possible models.

## The required net-indexed form

S1 and S2--S3 currently live at different levels. A local net assigns an algebra to every admissible region, whereas the core construction is displayed for one factor. A completed signature should contain something like

$$
O\longmapsto
\bigl(
\mathcal C_O,	au_O,\beta^O,
\{e^O_N\},\Omega_O
\bigr),
$$

together with the maps or correspondences induced by region inclusions and changes of presentation. It must say whether these maps preserve, rescale, or intertwine the traces, flows, cuts, and states. Locality, isotony, covariance, and composition are part of the signature rather than consequences of writing one core beside one net.

This is the natural setting for the desired Copernican theorem: construct the core wall over the groupoid of faithful weights, use Connes cocycles as comparison data, and prove which observables of the filtered family are invariant under change of pointing.

## Canonical structure and pointed presentation

The continuous core and its trace-scaling action are canonical up to their appropriate natural equivalence. The displayed filtration is not state-independent. A scalar rescaling of a weight translates the logarithmic coordinate, while a genuinely different faithful weight changes the affiliated density through noncommuting cocycle data.

Consequently,

$$
\text{canonical core}
\not\Longrightarrow
\text{canonical physical cuts}.
$$

The standard mathematics supplies an exact template for the sentence "invariant signature, state-dependent presentation." The claim that all physically admissible frames give the same wall content remains the **cocycle-naturality theorem target**. The frame question has acquired its correct mathematical form; it is not yet physically closed.

## The two-carrier wall

The algebraic pre-wall is intrinsically a cospan:

$$
\mathcal K_N=e_N\mathcal C e_N
\hookrightarrow
\mathcal A_N=\mathcal C^{(N)}
\hookleftarrow
\mathcal B_N=W^*(e_N).
$$

Finite trace-capacity belongs to the corner $\mathcal K_N$. The transported normal state and binary readout belong to the whole-core carrier $\mathcal A_N$, with $\mathcal B_N$ as a commutative context. The shared projection $e_N$ relates the packages without identifying their state spaces.

The correct physical object may therefore be a correspondence, cospan, or double-categorical wall rather than one carrier selected at the expense of the other. This is why the carrier decision gates the construction of $e_N\mapsto\Sigma_N$.

## What follows and what does not

Within the declared core hypotheses, the following are exact:

- trace and cut covariance;
- finite-corner normalization and transport;
- absence of a nonzero normal state invariant under the full trace-scaling action;
- the binary Fisher--BKM pulse for the specifically selected logistic density; and
- the carrier firewall between capacity and readout.

S1--S3 do not contain a physical quotient, Weyl or TT source, edge state, area measure, same-tangent map, canonical-energy bridge, or Newton coefficient. Therefore the renormalized source construction and the capacity--edge--area--$G$ weld are not yet "theorems inside the posit." They require further constitutive axioms or independent constructions.

Likewise, the abstract modular normalization and the geometric $2\pi$ appearing in Bisognano--Wichmann or half-sided-modular settings must be given their precise hypotheses. They are not automatically one universal measured constant of every core realization.

Finally, a candidate cosmic member should **contain** a compatible normal state. The sentence "the cosmos is one faithful normal state" is too strong: a state is neither a local net, a fact, a record, nor a history. [[program-core/axioms-and-principles|The Axiom and Principle Ledger]] should record the signature as a proposed schema and keep each later identification at its own claim level.
