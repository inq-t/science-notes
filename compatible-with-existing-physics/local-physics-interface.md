# The Local-Physics Interface

Taking GR and QFT as local inputs replaces the demand to derive them with a precise interface obligation: every tested local causal context must carry the established metric, observable, state, and conservation structure, while the new cosmodynamic relations enter only through declared horizontal or global maps. This is a preservation theorem in the overlap domain, not a Standard Model reconstruction theorem.

## The local data

For each admissible causal region $O$, the imported fiber should declare at least

$$
\mathfrak L(O)
:=
(g_O,\mathcal A_O,\omega_O,\iota_{O_2:O_1}),
$$

where $g_O$ is the operational physical metric, $\mathcal A_O$ is the local observable algebra, $\omega_O$ is a physically admissible state, and $\iota$ denotes restriction or inclusion on overlapping regions.

The surrounding theory then adds structures such as a scale-to-state comparison, a horizon or causal-wall reduction, a global state admissibility condition, or a constitutive response. Those additions must be typed separately from the vertical dynamics already present in the fiber.

## Preservation rather than derivation

If GR plus the Standard Model is imported, the programme need not derive

- $SU(3)_c\times SU(2)_L\times U(1)_Y$;
- the observed fermion representations and Yukawa couplings;
- ordinary atomic, nuclear, or laboratory dynamics; or
- every known local scattering amplitude.

It must nevertheless avoid making those inputs mutually inconsistent. A local restriction should preserve, in the regimes assigned to established physics:

- one operational metric and compatible matter, light, and gravitational causal cones;
- local covariance, causal propagation, and the equivalence-principle bounds appropriate to the chosen gravitational description;
- the Bianchi identity and conservation of the total renormalized stress response;
- microcausality or the relevant algebraic no-signalling condition;
- physically admissible microlocal or Hadamard states where curved-spacetime QFT requires them;
- gauge and BRST Ward identities and the anomaly cancellation already present in the Standard Model;
- positivity or unitarity in the relevant Lorentzian description; and
- the measured constancy of local masses, charges, and dimensionless couplings unless variation is explicitly predicted and tested.

[[library/axiomatic-quantum-field-theory-in-curved-spacetime/inq|Hollands and Wald]] give one rigorous formulation of local and covariant QFT on curved backgrounds. [[library/notes-on-some-entanglement-properties-of-quantum-field-theory/inq|Witten's algebraic review]] explains why local QFT is naturally expressed through observable algebras rather than local density matrices. These are ingredients for stating the fiber, not evidence that the causal-scale gluing has already been built.

## GR need not remain exact at every scale

Importing GR locally does not require the classical Einstein equation to be the exact quantum effective equation at every curvature and energy. Renormalized QFT in curved spacetime permits curvature terms, trace anomalies, state-dependent stress contributions, and nonlocal effective response. [[library/quantum-fields-in-curved-spacetime/inq|The curved-spacetime QFT review]] and [[library/the-1-loop-effective-potential-for-the-standard-model-in-curved-spacetime/inq|the one-loop Standard Model calculation]] make that qualification concrete.

The appropriate local claim is that the surrounding framework preserves the empirically successful gravitational effective description to the measured accuracy of its regime. If it predicts additional curvature, scale, or wall effects, it must state their domain and confront the corresponding bounds.

## Two implementations of the restriction contract

An effective-action implementation may take the schematic form

$$
\Gamma_{\mathrm{joint}}
=\Gamma_{\mathrm{GR+SM}}^{\mathrm{ren}}
+\Delta\Gamma_{\mathrm{cosmo}},
$$

with matrix elements of $\Delta\Gamma_{\mathrm{cosmo}}$ bounded in local laboratory regimes and intentionally non-negligible only in the declared global sector.

An algebraic implementation instead requires an equivalence

$$
\operatorname{Res}_O(\mathfrak C_{\mathrm{joint}})
\simeq
\mathfrak L_{\mathrm{GR+QFT}}(O)
$$

for the relevant local contexts, together with coherent overlap maps. The second formulation is often closer to the proposed observer-relative wall architecture and does not presuppose that the entire theory has one ordinary action.

Neither implementation is yet supplied by the mere statement that QFT is a fiber. [[wall-construction-interface/inq|The wall-construction interface]] records the missing region family, state family, and transports; [[compatible-with-existing-physics/primordial-observable-interface|the primordial observable interface]] states the separate Lorentzian representation burden.

## A process enrichment can preserve the local net

The surrounding structure need not be another automorphism group or another
Lagrangian. It may add normal unital completely positive operations

\[
\Phi_O:\mathcal A(O)\longrightarrow\mathcal A(O)
\]

provided they are natural under inclusions,

\[
\Phi_{O_2}|_{\mathcal A(O_1)}=\Phi_{O_1}
\qquad(O_1\subset O_2),
\tag{LP1}
\]

preserve the declared vacuum or state family, and transform covariantly,

\[
\beta_g\Phi_O=\Phi_{gO}\beta_g.
\tag{LP2}
\]

Automorphisms are the reversible members of this larger process category;
expectations, averaged operations, and nonselective readouts need not be
invertible within it. Treating such maps as an enrichment leaves isotony,
locality, the Poincare action, and the Hamiltonian of the imported net
unchanged by definition. Existence of a coherent family satisfying (LP1)--
(LP2) is a separate theorem. An operation asserted to be an actual laboratory
or clock evolution would carry additional empirical obligations, but a
structural comparison or response probe can coexist formally with the
established local dynamics.

[[library/quantum-operations-on-conformal-nets/inq|Quantum Operations on Conformal Nets]]
is a rigorous lower-dimensional precedent: compatible,
vacuum-preserving, covariant UCP families exist on type-III local algebras,
and discrete subnet inclusions can organize them into hypergroups. It is not
a construction for four-dimensional Yang--Mills. The exact property-\((T)\)
gap benchmark and the additional energy-solder obligations are stated in
[[contemporary-puzzles/yang-mills-mass-gap/kazhdan-markov-process-carrier]].

There is also an exact compatibility model for the stronger whole-to-local
claim. If \(q:W\to L\) has a section \(h\), then
\(e=hq\) is an idempotent and

\[
\operatorname{End}(L)\cong e\operatorname{End}(W)e.
\]

Consequently the imported local QFT automorphisms may remain unitary in the
retained corner even though their whole-carrier representatives are
noninvertible relative to \(I_W\). [[algebra/retract-corners-and-local-unitarity|The
corner theorem]] proves this without identifying the local and whole
identities. If \(h\) is selected by minimizing a whole Dirichlet response,
[[trace-dirichlet-descent/inq|Dirichlet descent]] can additionally derive a
local positive generator, but an arbitrary least-cost quotient is not
automatically Markovian. The safe alternative pulls observables through an
expected inclusion. [[trace-dirichlet-descent/standard-form-pullback-and-reducing-wall|The
standard-form theorem]] proves that this restriction preserves complete
Dirichletness even for Type-III local algebras, provided the restricted domain
is dense. Compatibility still requires the corner action and form-generated
process to reproduce or compare with the given local net, state, Poincare
representation, and Hamiltonian; the existence of a retract does not select
them.

## Perturbations and measurable interfaces

A global theory need not reproduce the conceptual story by which conventional cosmology motivates primordial perturbations. It does have to calculate the local records through which the cosmos is measured. [[primordial-observable-interface|The primordial observable interface]] gives the full return type. For CMB, lensing, growth, clocks, or gravitational waves, it must either

1. map its whole-state data into the gauge-invariant variables and transfer machinery of established cosmology, or
2. supply an alternative end-to-end calculation of the same measured observables.

This is **observable representation adequacy**, not necessarily recovery of QFT. A positive spatial kernel alone does not establish causal propagation, stable metric response, or consistency of higher correlations. [[library/analyticity-and-unitarity-for-cosmological-correlators/inq|Analyticity and unitarity constraints on cosmological correlators]] illustrate why the observable hierarchy carries structure beyond positivity of one covariance.

## Failure conditions

The surrounding architecture fails in its local-physics claim if it entails, without a declared and empirically viable modification:

- different incompatible operational metrics for different matter sectors;
- superluminal signalling or contradictory overlap records;
- uncompensated stress nonconservation;
- ghost, gradient, or ill-posed evolution in a sector used to make observations;
- violation of established gauge or anomaly constraints;
- unbounded wall-induced fifth forces, Lorentz violation, or drift of local constants; or
- a cosmic state law that cannot be consistently restricted to the local states it claims to surround.

These are compatibility failures. Failure to derive the Standard Model is not one unless Standard Model emergence is itself part of the claim.
