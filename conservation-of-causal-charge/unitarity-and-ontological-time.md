# Unitarity and Ontological Time

The proposed Unitarity Principle should not say that a scalar amount of information is divided among quantum state, gravity, and time. Its defensible form has four layers: reversible transport of an enlarged algebraic whole, a separate symmetry charge and Ward identity, a quadratic response geometry obtained by second variation, and a one-sided filtration of persistent records that supplies the orientation of ontological history.

## Unitarity is reversible transport

For an enlarged Hilbert or standard-form carrier, unitary transport satisfies

$$
U_{21}^*U_{21}=\mathbf1.
$$

At the algebraic level the corresponding ideal is a \(*\)-automorphism or isometric correspondence between the relevant cut fibers. Relative entropy and its BKM coincidence metric are invariant when states and tangents are transported covariantly by the same automorphism.

An accessible observer generally sees a completely positive channel rather than that automorphism. A Stinespring realization has the form

$$
\Phi(a)=V^*\pi(a)V.
$$

Data processing then gives

$$
D(\rho\Vert\sigma)
\geq
D(\Phi_*\rho\Vert\Phi_*\sigma)
$$

and, on regular transported tangents,

$$
G_{\mathrm{accessible}}
\preceq
G_{\mathrm{enlarged}}.
$$

The inequality says that a readout cannot increase distinguishability per fixed channel. It does not identify the deficit with gravity or prove that an additive complement exists. Equality requires a recovery or sufficiency theorem.

## Unitarity is not conservation of a chosen charge

A unitary preserves a self-adjoint generator \(Q\) only when

$$
U^*QU=Q.
$$

This is a symmetry statement in addition to unitarity. Conversely, an irreversible completely positive evolution can conserve \(Q\) when its Heisenberg generator satisfies

$$
\mathcal L^\dagger(Q)=0.
$$

The physical additive proposal is therefore still [[conservation-of-causal-charge/causal-individuation-balance|the diagonal causal charge]]:

$$
\Delta Q_\xi^{\mathrm{state+matter}}
+\Delta Q_\xi^{\mathrm{grav}}
+\Delta Q_\xi^{\mathrm{record}}
+\mathcal F_\xi[W]
=\mathcal A_\xi[W].
$$

Exact conservation requires the anomaly \(\mathcal A_\xi[W]\) to vanish. The plus signs become literal only after all sectors carry the same normalized generator in one charge fiber. Unitarity alone supplies neither that generator nor its moment map.

## The response matrix is the second-variation layer

[[program-core/common-response-matrix|The common response matrix]] is quadratic:

$$
\mathbb G_{IJ}
=g^{\mathrm{BKM}}(v_I,v_J).
$$

It can participate in the charge theory only if one variational construction gives

$$
\boxed{
\text{first variation}
\longrightarrow Q_\xi,
\qquad
\text{second variation}
\longrightarrow\mathbb G_{IJ}
\simeq Z_g\mathcal E^{\mathrm{can}}_{IJ}.}
$$

This is the role proposed in [[conservation-of-causal-charge/state-geometry-charge-weld|the state--geometry charge weld]]. Capacity is not another addend in the charge sum. It is a susceptibility or canonical-energy Hessian of the structure whose first variation carries charge.

If an enlarged response Hilbert space admits orthogonal projections

$$
P_{\mathrm{obs}}+P_{\mathrm{grav}}
+P_{\mathrm{record}}+P_{\mathrm{hid}}
=\mathbf1,
$$

then an exact Gram allocation is possible:

$$
\mathbb G^{\mathrm{tot}}_{IJ}
=\sum_s
\langle P_sv_I,P_sv_J\rangle.
$$

Isometric transport preserves the total matrix while the allocation changes. If the sector decomposition is not orthogonal, state--gravity--record cross-covariances are additional terms. Omitting them would be false additivity.

## A Casimir can be conserved without being information

For a finite-dimensional unitary representation with positive invariant form \(\kappa\) and fixed quadratic Casimir,

$$
C_2(T^{\mathrm{tot}})=c_R\mathbf1,
$$

one has the mean--covariance allocation

$$
\boxed{
c_R
=\|\mu^{\mathrm{tot}}\|_\kappa^2
+\operatorname{Tr}_\kappa\Sigma^{\mathrm{tot}}.}
$$

This is the higher-rank analogue of the binary Casimir. It is a fixed representation norm allocated between resolved order and residual susceptibility. The full covariance contains sectoral cross terms.

This is a legitimate meaning of “a symmetric quantity remains fixed,” but it is not entropy, a number of bits, or a Noether charge. Noncompact causal groups may lack a positive invariant form, and infinite-dimensional representations require domains and renormalization. In a Connes-style realization, an index, \(K\)-homology class, or [[ko-dimension-as-morita-class/entry|graded Morita class]] may be a more natural invariant than a positive scalar information budget.

## Ontological time is the record orientation

Temporal order is not a fourth stock \(Q_{\mathrm{time}}\). The candidate history structure is a directed family of stable record algebras

$$
\mathcal R_{\Sigma_1}
\xhookrightarrow{\;\iota_{21}\;}
\mathcal R_{\Sigma_2}
\xhookrightarrow{}\cdots,
\qquad
\iota_{32}\iota_{21}=\iota_{31}.
$$

A realized history is a compatible family of characters

$$
\chi_{\Sigma_2}\circ\iota_{21}
=\chi_{\Sigma_1}.
$$

Ambient presentation changes and reversible evolution may form a group. Record-preserving accessible arrows form a one-sided category or semigroup. Ontological time is the orientation of this second composition together with persistent pointing; it is not the modular parameter, the FLRW coordinate \(N\), or the time parameter of a reversible differential equation merely by identification.

The compatible characters are still not selected by the filtration. [[conservation-of-causal-charge/factive-descent-and-records|Factive descent]] owns the instrument, actual outcome, record stability, and observer-gluing obligations.

## A useful categorical picture

The four layers can be organized as a double structure:

- **horizontal arrows:** reversible comparison, gauge equivalence, and unitary or modular transport;
- **vertical arrows:** instruments, completely positive maps, endomorphisms, and record inclusions;
- **squares:** equivariance, charge accounting, and compatibility of record formation with physical transport.

The common response matrix is infinitesimal horizontal geometry after the physical quotient. Ontological history is vertical composition. A diagonal causal charge constrains both only when a common action or Ward identity makes the squares commute.

## Failure conditions

- If the enlarged transport is not isometric or its environment cannot be physically identified, “information moved rather than lost” is only a Stinespring possibility.
- If \(U^*QU\ne Q\), unitarity does not conserve the proposed charge.
- If the sectors require different generators or arbitrary relative normalization, their charge sum is notation.
- If sector cross-covariances are nonzero, a three-bin positive allocation is incomplete.
- If the causal symmetry is noncompact with no controlled positive form, its Casimir cannot be an information budget.
- If later allowed evolution generically erases the proposed record, no ontological arrow has been constructed.
- If the filtration has no compatible actual characters, it describes possible record growth rather than one history.
- If first and second variations do not arise from one action or covariant phase-space structure, the response matrix and causal charge remain neighboring conjectures rather than one Unitarity Principle.

The strongest present formulation is therefore: **one invariant algebraic or charge structure may persist while its observable response is redistributed among conditional state, geometry, correlations, and records; ontological time is the directed stabilization of that redistribution into one compatible factual history.**
