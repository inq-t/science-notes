# The Center-Valued Common Response Form

The common response form is proposed as one positive, generally center-valued geometry on a transported physical tangent. Its homogeneous, observational, mixed, and hidden blocks become a matrix only after a chart and scalarization policy are chosen. This note owns their common carrier and the mixed-jet test of common origin; central resolution, Hessianity, localization, expectation balance, hidden-mode elimination, spatial realization, and fact formation are separate modules.

## The form belongs to the descent, not necessarily the substrate

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
- \(H_{\mathrm{obs},0}\) contains observational differentiations annihilated by a declared invariant averaging projector, when such a projector exists;
- \(H_{\mathrm{hid}}\) contains genuine auxiliary, heavy, constrained, or not-directly-read-out physical directions, not gauge or null directions already removed by the quotient.

The second summand is not assumed to be an inhomogeneous microscopic space. Under [[program-core/contextual-descent-from-homogeneity|contextual descent]], it is a tangent to how one homogeneous datum becomes differentially observable. The subscript \(0\) is therefore earned by a specified projection or representation decomposition; *mean zero* is not primitive structure.

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

After transport to one carrier and removal of null directions, the BKM pullback of one fully specified faithful state family is the scalar form

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

The entries share a carrier, state, transport, tangent normalization, and renormalization prescription by construction. If the carrier has a nontrivial center, this scalar form already uses the central probability law contained in the whole state. The pre-consumer construction nevertheless retains the sector-resolved package below so that averaging, sectorwise analysis, and later fact formation are not conflated. Positivity gives

$$
G_{NN}\geq0,
\qquad
G_{\zeta\zeta}\succeq0,
\qquad
|G_{N\zeta}(f)|^2
\leq
G_{NN}G_{\zeta\zeta}(f,f).
$$

This does not yet give the CST source or the CWST spatial precision. Those are separate consumer maps from one common response. [[hessian-response-geometry/inq|The Hessian-response module]] isolates the additional flat-connection, common-potential, center-evaluation, BKM-selection, and tangent-bundle conditions required for this pullback to be a genuine Hessian geometry rather than a collection of positive blocks.

## The center-resolved datum is retained

[[program-core/center-valued-response|Center-valued response and scalarization]] owns the classical--quantum chain rule, the central-weight Fisher term, positivity in central order, and the exact evaluation taxonomy. The common construction retains

$$
\mathfrak G^Z_{\lambda}
=
\left(
 Z(\mathcal B),
\mathbf G^Z,
\omega^Z_\lambda
\right),
$$

where \(\mathbf G^Z\) is the full sector-resolved response, including central-weight variation, and \(\omega^Z_\lambda\) is the normal central law inherited from the whole state. The center is \(Z(\mathcal B)\) because \(\varphi_\lambda=\omega_\lambda\circ j_\lambda\) is a state on the readout carrier \(\mathcal B\). Using \(Z(\mathcal M)\) instead would require an explicit center-preserving identification. Throughout this note a scalar \(G_{IJ}\) means either the unique trivial-center form, the normal unconditioned evaluation, or a normalized internal sector metric. Algebraic character evaluation is a fourth and different operation; it becomes factive only with an instrument, an outcome, and the requisite record structure.

Expectation loss, edge entropy, and spectral area are typed neighbors rather than entries of this form. [[spectral-wall-descent/conditional-expectation-balance|Conditional-expectation balance]] owns the retained/lost BKM theorem and its nested scale-tower extension. [[spectral-wall-descent/scale-correspondence-stack|The scale-correspondence stack]] owns compatible center transport and edge-state cocycles, while [[spectral-wall-descent/finite-index-area-weld|the finite-index area weld]] and [[deriving-value-of-g/spectral-index-area-route|the spectral index--area route]] own the area comparison. Writing response, edge entropy, and area in one tuple is useful bookkeeping only after their carriers are declared; it does not by itself construct a graded algebra or an equality among them.

## Symmetry can remove the quadratic mixed block

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

The equality of mixed third derivatives supplies an integrability test. A CST homogeneous response and a CWST spectral response chosen independently will generically fail to be derivatives of one \(\Psi\). One equality such as \(\partial_NG_{\zeta\zeta}=\mathcal C_{N\zeta\zeta}\) is necessary evidence, not a sufficient proof: [[hessian-response-geometry/affine-hessian-structure|the affine Hessian theorem]] owns the full connection, permutation, and common-potential obligations.

[[spectral-wall-descent/mixed-response-jet|The finite mixed-response jet]] realizes this pattern in \(M_3(\mathbb C)\) without fitting the blocks separately:

$$
G_{N\zeta}=0,
\qquad
\mathcal C_{N\zeta\zeta}
=\frac{1}{2\sqrt2}.
$$

The value is fixed by one matrix multiplication table and arithmetically cross-checked by finite differences.

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

It must not be an ordinary sheaf mismatch whose vanishing merely defines admissible gluing, unless physical deviations from that condition are genuinely intended. A lumpy but globally compatible section is not a descent failure. [[basic-concepts/descent/inq|Descent]] and physical differentiation remain distinct.

## Reduction and hidden algebraic modes

Gauge and presentation-null directions belong in the physical quotient or the radical before this form is interpreted. Hidden directions retained in \(H_{\mathrm{hid}}\) are different: they are physical auxiliary or heavy directions in the unreduced common form, and their removal must be derived rather than performed by deleting rows.

[[spectral-wall-descent/hidden-resolvent-and-seesaw|The hidden-resolvent module]] owns Schur reduction and the distinct homogeneous, spectral, and seesaw interpretations of its resolvent. [[spectral-wall-descent/response-determinant|The response--determinant module]] owns the companion determinant and sign ledger. [[program-core/singlet-response-completion|The singlet completion test]] owns the rank-one repair criterion. This note requires only that all eliminated directions first occur in the same positive form and that the chosen reduction be compatible with the physical quotient.

The order of operations remains a theorem obligation:

$$
\text{quotient then response}
\stackrel{?}{=}
\text{response then derived reduction}.
$$

It may hold for genuine radical directions under suitable regularity and fail for constraints, auxiliary modes, or completely positive deformations. A failure makes the reduction prescription part of the member data; it does not authorize interpreting the resulting block as a stress tensor, spatial precision, or mass matrix without the corresponding consumer map.

## Typed neighbors and consumers

A noninvertible wall may split a pre-wall response into retained and lost blocks, but that is a theorem about a chosen expectation or instrument, not another definition of the common form. [[spectral-wall-descent/conditional-expectation-balance|Conditional-expectation balance]] owns the exact finite Pythagorean split and explains why it is neither unitarity nor conservation of an information substance. [[conservation-of-causal-charge/unitarity-and-ontological-time|The unitarity audit]] owns the larger ontological boundary.

Localization is a separate operation on a declared scalarized or center-linear response. [[program-core/localized-areal-response-geometry|Localized areal response geometry]] owns its measure and Radon--Nikodym density. A spatial Fourier precision is a carrier-changing W2 consumer, while gravitational canonical energy and central area are further typed consumers. Agreement among these objects is a weld to be constructed, not a reason to call them entries of one matrix.

Factive selection and record extension occur later still. [[conservation-of-causal-charge/factive-descent-and-records|Factive descent]] owns compatible characters and one-sided records; [[program-core/record-scale-soldering|record--scale soldering]] owns any identification of their order with cosmic scale. Neither a fact nor time is an addend of the response form.

## A generator-family route

One possible provider is a single affine modular or Dirac-derived generator family \(K(N,\zeta,h)\) whose faithful Gibbs states are transported to the readout carrier. [[hessian-response-geometry/inq#When the Hessian is BKM|The Hessian-response module]] owns the exact BKM/log-partition formula, including the acceleration term for nonlinear generators. [[program-core/contextual-descent-from-homogeneity#What Connes supplies as precedent|Contextual descent]] owns the narrower lesson from inner fluctuations: rich represented differentiation can arise without extra ordinary spatial dimensions.

The finite version of this route is now constructed in [[wall-construction-interface/finite-cellular-markov-wall|the cellular Markov wall]]: one log-partition potential gives the homogeneous and mean-zero blocks, exact transport, a completely positive state law, and a state-preserving readout. The **physical continuum route remains open** until a causal carrier, physical quotient, renormalized localization, and source family are constructed on one member. A spectral-action Hessian is not the positive BKM pullback merely because both depend on one Dirac family.

## Finite witness

[[program-core/contextual-descent-from-homogeneity#A finite moving-context witness|The moving-projector witness]] calculates the classical Fisher pullback for one fixed matrix algebra and proves that it vanishes for a maximally mixed state along symmetry-equivalent contexts. It tests the no-response lemma that this note consumes. [[wall-construction-interface/finite-cellular-markov-wall|The cellular Markov wall]] supplies the complementary positive witness and owns its calculation; neither derivation is duplicated here.

## Construction gates

1. **CRF--0 — Common carrier.** Construct one readout family, transport, state family, and renormalization prescription before comparing blocks.
2. **CRF--1 — Physical tangent.** Remove presentation, gauge, normalization, and null directions; keep genuine auxiliary directions distinct from the radical.
3. **CRF--2 — Center-resolved form.** Calculate one positive \(\mathbf G^Z\) on the carrier of the descended state and retain its normal central law.
4. **CRF--3 — Block decomposition.** Construct the homogeneous, observational, mixed, and hidden subspaces, including the averaging projector or representation split that defines \(H_{\mathrm{obs},0}\).
5. **CRF--4 — Mixed-jet test.** Prove the symmetry status of \(G_{N\zeta}\) and the first allowed mixed tensor; if Hessianity is claimed, verify the full integrability conditions with the Hessian owner.
6. **CRF--5 — Derived reduction.** Show that any hidden-mode reduction is defined on this form and control its order relative to the physical quotient.

Localization, wall loss, spatial precision, gravity, facts, records, and empirical dynamics begin at linked consumer modules rather than extending this gate list.

## Failure localization

- If the readout orbit is state preserving, the proposed differentiation is pure presentation and its observational response vanishes.
- If the claimed blocks require incompatible carriers, states, central laws, tangent normalizations, or renormalization schemes, there is no common form.
- If the descended state lives on one algebra while \(\mathbf G^Z\) is assigned to an unrelated center, the center-resolved datum is ill typed.
- If no positive form survives the physical quotient, the response construction fails.
- If the full mixed integrability conditions fail, the blocks are not reductions of one Hessian family in that realization.
- If constraint removal changes the result and no derived order is selected, the effective common form is undefined.

The payoff is nevertheless substantial: homogeneous response, observational differentiation, and internal auxiliary structure can be tested as blocks of one transported algebraic geometry without positing a lumpy sub-Planckian space. Whether any block becomes cosmological density, spatial precision, gravity, mass, or a fact is deliberately left to the corresponding consumer.
