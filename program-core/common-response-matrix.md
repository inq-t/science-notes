# The Common Response Matrix

The common response matrix is proposed as one positive Hessian geometry of observational descent from a homogeneous sub-observable datum. Its homogeneous entry measures response to global scale displacement; its mean-zero block measures differentiation among observational modes; its mixed block and, more importantly at a symmetric reference, its first mixed derivative test whether CST and CWST are genuinely reductions of one construction rather than separately fitted models.

## The matrix belongs to the descent, not necessarily the substrate

Let \(\mathfrak D\) be a space of admissible descent data. A point contains at least

$$
(\mathcal M,\omega,j,\mathcal T),
$$

where \(\mathcal M\) is a sub-observable algebra, \(\omega\) a faithful state, \(j\) an observational readout, and \(\mathcal T\) the transport that makes nearby readouts comparable. The physical tangent is formed only after the quotient in [[program-core/physical-quotient|the physical quotient]]. Around a homogeneous reference, seek a chart

$$
T\mathfrak D_{\mathrm{phys}}
\simeq
\mathbb R v_N
\oplus
H_{\mathrm{obs},0}
\oplus
H_{\mathrm{hid}},
$$

where:

- \(v_N\) changes global scale comparison;
- \(H_{\mathrm{obs},0}\) contains nonconstant, zero-mode-free observational differentiations;
- \(H_{\mathrm{hid}}\) contains internal, constrained, or not-directly-read-out algebraic modes.

The second summand is not assumed to be an inhomogeneous microscopic space. Under [[program-core/contextual-descent-from-homogeneity|contextual descent]], it is a tangent to how one homogeneous datum becomes differentially observable.

## Pullback construction

Choose a fixed observational carrier \(\mathcal B\) and normal unital completely positive readouts

$$
j_\lambda:\mathcal B\longrightarrow\mathcal M,
\qquad
\lambda=(N,\zeta,h).
$$

The induced state is

$$
\varphi_\lambda:=\omega_\lambda\circ j_\lambda.
$$

After transport to one carrier and removal of null directions, define

$$
\dot\varphi_I:=D\varphi(\partial_I),
\qquad
\boxed{
\mathbb G_{IJ}
:=g^{\mathrm{BKM}}_{\varphi}
(\dot\varphi_I,\dot\varphi_J).}
$$

This is the pullback of the BKM geometry along the descent/readout map. In the \((N,\zeta)\) sector it gives

$$
\boxed{
\mathbb G_{N\oplus\zeta}
=
\begin{pmatrix}
G_{NN}&G_{N\zeta}\\
G_{\zeta N}&G_{\zeta\zeta}
\end{pmatrix}.}
$$

The entries share a carrier, state, transport, tangent normalization, and renormalization prescription by construction. Positivity gives

$$
G_{NN}\geq0,
\qquad
G_{\zeta\zeta}\succeq0,
\qquad
|G_{N\zeta}(f)|^2
\leq
G_{NN}G_{\zeta\zeta}(f,f).
$$

This does not yet give the CST source or the CWST spatial precision. Those are separate consumer maps from one common response.

## An exact classical--quantum realization

A controlled factive precursor is a classical--quantum readout state

$$
\widehat\rho_\lambda
=
\int_X^{\oplus}
p_\lambda(x)\,
\sigma_{\lambda,x}\,
\mathrm d\mu(x),
$$

where \(X\) is the spectrum of a commutative record context, \(p_\lambda\) is its accessible law, and \(\sigma_{\lambda,x}\) is the conditional sub-observable state. Under fixed-carrier, faithfulness, and regularity hypotheses, relative entropy has the classical--quantum chain rule

$$
D(\widehat\rho\Vert\widehat\tau)
=D_{\mathrm{KL}}(p\Vert q)
+\int_Xp(x)
D(\sigma_x\Vert\tau_x)\,\mathrm d\mu(x).
$$

Its coincidence Hessian therefore gives the **[EXACT MODEL — UNDER THOSE HYPOTHESES]**

$$
\boxed{
\mathbb G_{IJ}^{\mathrm{CQ}}
=I^{\mathrm F}_{IJ}[p]
+\int_Xp(x)
g^{\mathrm{BKM}}_{IJ}[\sigma_x]
\,\mathrm d\mu(x).}
$$

The Fisher term measures differentiation of possible characters or records. The conditional BKM term measures the quantum response retained inside each fiber. A homogeneous law can therefore carry a nontrivial record-response geometry without making the underlying algebra a lumpy classical space.

The formula selects no actual \(x\). Pure conditional states may also lie on the boundary where ordinary BKM geometry is singular. A continuum realization must use faithful unconditioned states, fixed-support tangents, or a controlled limiting metric.

## Symmetry removes the quadratic mixed block

At a homogeneous and isotropic reference, \(v_N\) transforms in the trivial representation. If \(H_{\mathrm{obs},0}\) contains no trivial subrepresentation and the BKM form is invariant, representation orthogonality gives

$$
\boxed{G_{N\zeta}=0}
$$

at that reference. In a flat Fourier presentation, this is the orthogonality of the \(k=0\) mode to physical \(k\neq0\) modes. It is a **[CONDITIONAL THEOREM]**, not evidence that the two sectors have different origins.

The first common-origin witness is then one order higher. If the state family is an affine exponential family with log-partition potential \(\Psi(N,J)\),

$$
G_{IJ}=\partial_I\partial_J\Psi.
$$

Define its cubic response tensor

$$
\mathcal C_{IJK}
:=\partial_I\partial_J\partial_K\Psi.
$$

Then

$$
\boxed{
\mathcal C_{N\zeta\zeta}
=\partial_NG_{\zeta\zeta}}
$$

in the declared affine coordinates. Translation invariance permits

$$
\mathcal C_{N\zeta\zeta}(k,k')
=(2\pi)^d\delta^{(d)}(k+k')\,c_N(k)
$$

even though \(G_{N\zeta}=0\). The homogeneous direction can therefore control the spectrum of nonconstant distinctions without the reference state ceasing to be homogeneous.

This tensor is a derivative of a specified log-partition potential. It is not obtained by calling the third derivative of relative entropy a cumulant; [[basic-concepts/hessians/higher-relative-entropy-is-not-cumulants|the higher-derivative no-go]] forbids that shortcut. In a non-Hessian realization, the corresponding target is a covariant variation \(\nabla_NG_{\zeta\zeta}\) with its connection declared.

The equality of mixed third derivatives supplies an integrability test. A CST homogeneous response and a CWST spectral response chosen independently will generically fail to be derivatives of one \(\Psi\).

## A positive descent-cost realization

The pullback metric can arise from one more primitive positive functional. Let

$$
\mathcal R:\mathfrak D_{\mathrm{phys}}\longrightarrow\mathcal V
$$

be a descent residue valued in one transported response space, with \(\mathcal R(0)=0\) at the homogeneous reference. Let \(\mathscr K:\mathcal V\to\mathcal V^*\) be positive. Define

$$
\mathscr I_{\mathrm{desc}}(\lambda)
:=\frac12
\langle\mathcal R(\lambda),
\mathscr K\mathcal R(\lambda)\rangle.
$$

At the reference,

$$
\boxed{
\operatorname{Hess}_0\mathscr I_{\mathrm{desc}}
=J^*\mathscr KJ,
\qquad
J_I:=D_I\mathcal R|_0.}
$$

Thus all blocks arise as one Gram matrix:

$$
G_{IJ}=\langle J_I,\mathscr KJ_J\rangle.
$$

This imports the useful algebraic shape of an Onsager--Machlup equation-residual squared without importing stochastic spacetime ontology. The residue may measure physical horizontal failure of homogeneity, connection curvature, or deviation from a constitutive descent equation.

It must not be an ordinary sheaf mismatch whose vanishing merely defines admissible gluing, unless physical deviations from that condition are genuinely intended. A lumpy but globally compatible section is not a descent failure. [[basic-concepts/descent/entry|Descent]] and physical differentiation remain distinct.

## Reduction and hidden algebraic modes

Gauge directions should lie in the radical before the metric descends. Constrained or heavy physical directions are different: eliminating them generally produces a Schur complement rather than deletion of rows and columns.

Write \(x=(N,\zeta)\) and let \(h\) denote hidden or auxiliary modes. For

$$
\mathbb G
=
\begin{pmatrix}
G_{xx}&G_{xh}\\
G_{hx}&G_{hh}
\end{pmatrix},
$$

minimizing the quadratic descent cost over \(h\), when justified, gives

$$
\boxed{
G_{xx}^{\mathrm{eff}}
=G_{xx}-G_{xh}G_{hh}^{+}G_{hx}.}
$$

The pseudoinverse is taken only on the declared non-null eliminated sector. This formula makes three research possibilities precise:

- a hidden algebraic mode coupled to \(N\) can alter the effective homogeneous response;
- a hidden mode coupled to \(\zeta\) can generate a scale-dependent or nonlocal observable kernel;
- hidden internal Dirac blocks can produce small effective masses by the same Schur-complement grammar as a seesaw.

These are openings, not identifications with dark energy, dark matter, or neutrino mass. A BKM Hessian is not a stress tensor or a mass matrix. The relevant source, covariance-to-precision map, and covariant dynamics must still be built.

The order of operations is a theorem obligation:

$$
\text{quotient then Hessian}
\stackrel{?}{=}
\text{Hessian then physical reduction}.
$$

The equality holds for genuine radical directions under suitable regularity. It need not hold for constraints, auxiliary modes, or stochastic/CP deformations.

## What the Unitarity Principle could mean

[[conservation-of-causal-charge/unitarity-and-ontological-time|The dedicated Unitarity note]] owns the full distinction among reversible transport, charge, quadratic response, and record time. The consequences needed here are the following.

For a fixed completely positive readout, data processing gives contraction of distinguishability,

$$
\mathbb G_{\mathrm{obs}}
\preceq
\mathbb G_{\mathrm{pre}},
$$

on correctly transported tangents. Equality requires a sufficiency or recovery theorem. The deficit is not automatically gravity, time, or a conserved substance.

An exact matrix allocation requires an enlarged reversible realization. Suppose a BKM or GNS response Hilbert space carries isometric transport \(U_{21}\), and suppose orthogonal physical projections satisfy

$$
P_{\mathrm{obs}}+P_{\mathrm{grav}}
+P_{\mathrm{record}}+P_{\mathrm{hid}}=\mathbf1.
$$

For transported tangents \(v_I\),

$$
\mathbb G^{\mathrm{tot}}_{IJ}
=\sum_s
\langle P_sv_I,P_sv_J\rangle.
$$

If \(U_{21}\) is isometric, the total Gram matrix is preserved while its sector allocation can change. Without orthogonal projections, cross-correlations are additional terms and cannot be discarded. This is a quadratic norm balance, not a Noether charge.

The actual charge proposal remains the linear moment-map law in [[conservation-of-causal-charge/causal-individuation-balance|causal-individuation balance]]. Its first variation may generate charge, while the present matrix appears as a compatible second variation only after [[conservation-of-causal-charge/state-geometry-charge-weld|the state--geometry charge weld]].

Nor is ontological time another sectoral addend. Its candidate mathematical form is the orientation of persistent record inclusions,

$$
\mathcal R_{\Sigma_1}
\hookrightarrow
\mathcal R_{\Sigma_2}
\hookrightarrow\cdots,
$$

with compatible characters along the realized history. Ambient transport may be reversible while accessible record formation is a semigroup. [[conservation-of-causal-charge/factive-descent-and-records|Factive descent]] owns that one-sided layer.

## A Connes-style realization ansatz

Take a represented real algebraic datum

$$
(\mathcal A,\mathcal H,D,J,\gamma,\omega)
$$

in one fixed Morita or \(K\)-homology sector. Let

$$
K(N,\zeta,m)
=K_0+NQ_N+Q_\zeta+Q_F(m)
$$

be an affine modular or Dirac-derived generator family and

$$
\rho_{N,\zeta,m}
=\frac{e^{-K(N,\zeta,m)}}{Z(N,\zeta,m)}.
$$

Then

$$
\mathbb G_{AB}
=\partial_A\partial_B\log Z
=g^{\mathrm{BKM}}_\rho
(\delta_AK,\delta_BK)
$$

in the regular finite exponential-family regime. Here \(Q_N\) is a singlet scale generator, \(Q_\zeta\) a non-singlet observational operator sector, and \(Q_F(m)\) a finite internal-geometry sector.

Connes' inner fluctuations

$$
D_A=D+A+JAJ^{-1}
$$

give a concrete family of algebraic metric deformations while the algebra and index class remain fixed. A spectral projection, heat-kernel compression, or another completely positive resolution map built from \(D_A\) could provide the readout \(j_{N,\zeta,m}\). Constructing such a channel with composition, covariance, and continuum control is an open problem; the spectral action Hessian must not simply be identified with the positive BKM Hessian.

## Finite debugging model

Let \(\mathcal M=M_n(\mathbb C)\), let \(\rho\) be faithful, and let a commutative readout be a moving projective measurement

$$
P_i(\lambda)=U_\lambda P_iU_\lambda^*,
\qquad
p_i(\lambda)=\operatorname{Tr}(\rho P_i(\lambda)).
$$

The induced response is the classical Fisher matrix

$$
\boxed{
G_{IJ}
=\sum_i
\frac{\partial_Ip_i\,\partial_Jp_i}{p_i}.}
$$

It is a finite common response generated by one fixed matrix algebra and one family of contexts. If \(\rho=\mathbf1/n\), then \(p_i=1/n\) for every unitarily related projective context and \(G_{IJ}=0\). This exactly demonstrates the no-response lemma: a completely invariant state plus symmetry-equivalent readouts cannot explain observable differentiation. A nontrivial generator, state-context relation, boundary, holonomy, or pointing is indispensable.

## Construction gates

1. **CRM--0 — Homogeneous datum.** Specify factoriality, symmetry action, invariant state, or invariant Morita/index class; do not use one as a synonym for another.
2. **CRM--1 — Readout category.** Construct commutative contexts or CP readouts, their transport, overlaps, and effectivity.
3. **CRM--2 — Physical tangent.** Quotient presentation, gauge, central-normalization, and observationally null directions before removing the response radical.
4. **CRM--3 — Common positive form.** Calculate the full \((N,\zeta,h)\) BKM or descent-cost Hessian on one carrier and in one scheme.
5. **CRM--4 — Symmetry jet.** Prove the representation content, the status of \(G_{N\zeta}\), and the first allowed mixed tensor such as \(\nabla_NG_{\zeta\zeta}\).
6. **CRM--5 — Reduction theorem.** Derive the quotient and Schur-complement operations and control gauge, constraint, and heavy sectors.
7. **CRM--6 — Consumer maps.** Localize the homogeneous contraction for CST and construct the carrier-changing spatial precision map for CWST.
8. **CRM--7 — Reversible enlargement and records.** State whether CP contraction admits an equivariant dilation and construct the one-sided record filtration.
9. **CRM--8 — Dynamics and tests.** Derive a covariant response/action and independently calculate background, scalar, tensor, higher-point, mass, and record observables.

## Failure localization

- If the readout orbit is state preserving, the proposed differentiation is pure presentation and the response vanishes.
- If \(G_{NN}\) and \(G_{\zeta\zeta}\) require different carriers or prescriptions, there is no common matrix.
- If the mixed derivative integrability conditions fail, CST and CWST are not reductions of one Hessian family in that realization.
- If the physical matrix depends on whether constraints were removed before or after response was introduced, the reduction prescription is part of the theory and must be tested.
- If a CP deficit has no constructed complementary sector or recovery map, it cannot be called conserved information or geometry.
- If no character and persistent record are supplied, the construction explains correlated appearances but not an actual cosmic history.
- If the state--geometry weld or covariant dynamics fails, the matrix remains an information geometry and does not explain dark energy, dark matter, gravity, or particle mass.

The central payoff is nevertheless substantial: apparent lumpiness, homogeneous cosmic response, internal algebraic mass structure, and observational correlations can now be asked to arise from different contractions and reductions of one invariant algebraic descent geometry, without positing a lumpy sub-Planckian space.
