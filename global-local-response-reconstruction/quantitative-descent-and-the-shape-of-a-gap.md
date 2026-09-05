# Quantitative Descent and the Shape of a Mass-Gap Construction

The strongest candidate is a state-dependent geometry of directed gluing whose normalized response cannot degenerate under refinement. Algebraic descent would organize compatible local presentations; a positive state would supply their comparison norm; quantitative rigidity would exclude almost-invisible physical distinctions; and a separate reconstruction would return local unitary clock dynamics. The missing principle is not merely that a distinction exists, but that the complete physical distinction carrier cannot approach zero response at one fixed physical scale.

**Status: [RESEARCH SYNTHESIS AND CANDIDATE CONSTRUCTION].** The operator identities and sufficient certificates below are exact under their stated assumptions. No existing workspace geometry is shown here to force those assumptions for continuum Yang--Mills.

## The primitive should be a relation with a state, not another field

[[inq|Global--Local Response Reconstruction]] and [[spectral-wall-descent/scale-correspondence-stack|the correspondence prestack]] already identify the appropriate slots:
\[
\mathfrak U=
(\mathsf{Ctx},\{\mathcal A_c,\omega_c\},
\mathsf{Corr},\mathsf{Loss},\mathscr S,\vartheta).
\tag{QD1}
\]
This is a schematic signature, not a completed definition of a new category. Contexts and admissible covers organize presentations; pointed correspondences compare carriers; declared CP maps or expectations implement particular restrictions; the scale torsor \(\mathscr S\) carries relative calibration; and \(\vartheta\) is a reflection datum for the proposed Euclidean reconstruction route. Their compatibility laws still have to be supplied.

The whole is not a second, larger spacetime region. It is the jointly compatible object presented through these contexts. Nor is it necessarily a single normalized density matrix: the [[wall-construction-interface/core-spectral-wall|canonical-core construction]] distinguishes a weight-valued whole from normal states that point within it.

This suggests a category with both invertible presentation changes and noninvertible processes, enriched by positive states, Hilbert norms, and quantitative comparison maps. An ordinary groupoid retains the first arrows but not every second arrow. Bare correspondence fusion does not select the process, expectation, or state.

There is existing mathematics for part of this shape. [[library/haag-kastler-stacks/inq|Haag--Kastler stacks]] formalize local-to-global descent of AQFTs. They still take Lorentzian manifolds as inputs: they neither derive spacetime nor prove a mass gap. The proposed advance would be a stateful, quantitatively controlled realization, not the mere replacement of the word “field” by “stack.”

## The operator acts on failures of joint recovery

At regulator \(r\) and fixed physical slab half-thickness \(\ell\), measured from midpoint to either boundary, let \(\mathcal H_r\) be the completed, gauge-invariant midpoint distinction carrier with its state norm, after genuine null redundancies have been removed. Let \(J_r\) embed it isometrically into the whole-law GNS carrier, and let \(P_{\partial,r}\) project onto information recoverable from the joint boundary context. These are the actual maps of the whole law, not fitted probes.

Define
\[
\delta_{r,\ell}=(I-P_{\partial,r})J_r,\qquad
R_{r,\ell}=\delta_{r,\ell}^*\delta_{r,\ell},
\qquad 0\le R_{r,\ell}\le I.
\tag{QD2}
\]
The output of \(\delta\) is a residual distinction in the whole carrier. It is not a spacetime displacement, an observed particle, or an outcome-selection event. Its squared norm is an irreducible prediction error. The state, not a count of coordinates, determines the norm.

The desired statement is
\[
\ker R_{r,\ell}=\mathbb C\Omega_r,\qquad
R_{r,\ell}\ge\kappa(I-P_{0,r}),\qquad
\kappa>0
\tag{QD3}
\]
uniformly along the regulated trajectory, with \(\ell>0\) fixed independently of the sought low spectrum. The first condition identifies the exact kernel; the second excludes normalized almost-kernel vectors. They are different conditions.

This is a relative Hodge-like signature: a comparison map and its adjoint produce a positive Laplacian-like operator. It becomes a genuine Hodge complex only after differentials, domains, and composition identities are constructed. The adjoint reverses a Hilbert pairing; it need not represent a realizable reversal of the underlying process.

Ordinary mass units enter later. Under the stationary reversible Markov, reflection-positive transfer, and continuum hypotheses in [[inq|the reconstruction theorem]], (QD3) with \(0<\kappa<1\) implies
\[
\Delta_E\ge
\frac{\hbar c}{2\ell}\log\frac1{1-\kappa}.
\tag{QD4}
\]
The equation is a lower bound, not a predicted optimal glueball mass. It cannot be used backward to define \(R\) from the desired spectrum.

## Positivity has to follow the carrier

The [[complex-presentation-without-polarization/polarization-and-positive-state-geometry|positivity--integrability audit]] supplies a useful separation, not a duality identifying all positive structures:

| Positive structure | What it acts on or tests | What it does not yet supply |
|---|---|---|
| Jordan order cone | nonnegative algebraic observables | a process, clock, or strict response edge |
| positive state and BKM form | normalized observable or state tangents | a spacetime Hilbert carrier or energy |
| completely positive restriction | an associative algebra and every matrix amplification | reflected Euclidean positivity or a gap |
| reflection-positive whole law | positive-time observables paired across a reflection | strict contraction on the vacuum complement |
| coercive response | the entire declared complement in its fixed norm | identification of that complement with physical Yang--Mills states |

There is an exact counterexample to collapsing the middle rows:
[[lorentzian-spectral-envelope/positive-kernels-and-reflection-positivity|a stationary sech-squared kernel]] has a positive Fourier transform but fails the reflected two-point test. Its legitimate roles as density, susceptibility, and Witten potential survive. The error lies in changing the object's role without changing its test.

## A finite exceptional realization of the desired shape

[[algebra/exceptional-context-response|Exceptional context response]] now supplies a constructive template. On \(J=\mathfrak h_3(\mathbb O)\), the prior order-three operation selects \(E=(I+w+w^2)/3\) with complex Jordan range. The exact defect is
\[
E(x^2)-(Ex)^2=E((x-Ex)^2)\ge0.
\]
The same operation determines the orientation-bearing residue and, after adjoining the pointed idempotent, the known exceptional flag stabilizer. Thus the symmetry and the positive response have a common algebraic input, without being identified.

For all conjugate contexts \(E_g\), the trace metric and normalized \(F_4\) Haar measure give
\[
\int\|(I-E_g)x\|_J^2\,dg
=\frac9{13}\|x\|_J^2,\qquad x\in J_0.
\tag{QD4a}
\]
This determines a bounded gluing inverse on the full trace-free Jordan carrier. The number follows from an operation and an irreducible representation, not a chosen spatial size.

More strongly, the regular operators \(L_x:y\mapsto x\circ y\) intertwine the Jordan retraction with an ordinary matrix CP expectation. On the faithful family \(\rho_\varepsilon=(I+\varepsilon L_x)/27\), the averaged relative-entropy loss is
\[
\frac{\varepsilon^2}{26}\|x\|_J^2+O(\varepsilon^3).
\tag{QD4b}
\]
This is an explicit order-to-information-response map. It requires neither an integrable complex structure on \(S^6\) nor a cosmological origin story.

The cyclic family has an explicit limitation: a nonzero balance tangent between \(\mathbb C\mathbf1\) and \(J_{0,\mathbb C}\) is fixed by every matrix expectation. [[algebra/primitive-peirce-response|The primitive Peirce completion]] repairs this finite gap by adding readouts determined by all primitive idempotents. An exact integer polynomial certificate for the regular-multiplier response gives
\[
\mathcal D\ge3(I-P_{\rm sc}),\qquad
\int\|(I-\Pi_p)T\|_{\rm HS}^2\,dp
\ge\frac1{13}\|(I-P_{\rm sc})T\|_{\rm HS}^2.
\tag{QD4c}
\]
It yields full finite matrix-state coverage and a nonsharp global relative-entropy contraction. The trace normalization and Haar weighting are declared geometric data; neither is a derived physical context law or clock.

The change to field configurations is separate. A fiberwise unital channel fixes every \(f(U)I\), leaving all scalar Wilson observables untouched. [[exceptional-context-analysis-of-gauge-gradients|The differentiated-context construction]] instead analyzes \(i\,d\rho(\nabla f)\), giving
\[
\|\mathcal A_{\rm ctx}f\|^2
=\frac9{13}\mathcal E_{K,\mu}(f).
\tag{QD4d}
\]
This is an exact frame for genuine configuration gradients under the specified law \(\mu\). Heat integration factors the bounded whole-law response already used in the slab comparison. The finite frame coefficient does not prove the measured-law Poincare bound: the unresolved task is still uniform field coverage and comparison to the actual boundary-recovery defect.

There is now a concrete geometric alternative. [[boundary-frozen-heat-and-conditional-fisher-response|Freeze the actual retained boundary]] when defining the auxiliary field heat: its bounded response is automatically below the bridge defect. [[conditional-fisher-coercivity/inq|Conditional Fisher coercivity]] then proves
\[
B_D\ge\frac{\lambda_F}{1+\lambda_F}Q_C
\]
from a Poincare inequality for the boundary law in the conditional family's Fisher metric. This controls every core observable, not just parameter tangents. [[collared-quasi-factorization-and-surface-response/fisher-collar-bound-for-wilson-laws|The Wilson collar theorem]] provides an explicit nonlinear, volume-uniform instance using the action, compact curvature and operator-norm score covariance. Its strong-coupling hypotheses are not yet controlled along the continuum trajectory. [[bridge-data-augmentation-solder/bridge-floor-under-joint-limits|The joint-limit theorem]] preserves a uniform response floor if the nontrivial limiting joint law can separately be constructed.

## Two ways algebra or geometry could force the inequality

### A positive algebraic certificate

Suppose the directed gluing relations select a positive bounded element \(R\) in a declared ordered \(*\)-algebra or admissible \(C^*\)-completion, and force
\[
\boxed{R^2-\kappa R=\sum_jB_j^*B_j,\qquad R\ge0,\quad\kappa>0.}
\tag{QD5}
\]
Every bounded admissible \(*\)-representation then has
\[
\sigma(\pi(R))\subset\{0\}\cup[\kappa,\infty).
\tag{QD6}
\]
Indeed, positivity of the represented right side gives
\(x(x-\kappa)\ge0\) on the spectrum; positivity of \(R\) excludes the negative branch. The spectral theorem proves (QD6).

Here the gap follows from an identity that can be checked before diagonalizing the physical Hamiltonian. [[library/noncommutative-real-algebraic-geometry-of-kazhdans-property-t/inq|Ozawa's property-(T) theorem]] is an exact precedent for this kind of algebraic certificate. [[contemporary-puzzles/yang-mills-mass-gap/quantum-g2-categorical-rigidity-and-the-carrier-firewall|Quantum-\(G_2\) categorical rigidity]] suggests an admissible-representation version; its positivity must be that of the appropriate tube or annular completion, not just formal fusion rules.

The physical work would be to derive the same normalized gluing element at fixed \(\ell\), represent it on the full neutral observable carrier, and prove that its invariant subspace is only the vacuum. A gauge-group action that fixes every gauge-invariant state fails that test. Universal rigidity is one sufficient route, not a necessary property of every possible Yang--Mills construction.

### A constructive quantitative gluing map

Alternatively, take \(T_r=\delta_{r,\ell}|_{\mathscr C_r}\) on a dense physical nonvacuum domain, with response target \(\mathcal K_r\), and construct an independently specified return map \(B_r:\mathcal K_r\to\mathcal H_{0,r}\) with
\[
B_rT_r=I-E_r,\qquad
\|B_r\|\le C,\qquad\|E_r\|\le\rho<1
\tag{QD7}
\]
uniformly in \(r\). Then
\[
\boxed{\|T_r\psi\|^2
\ge\frac{(1-\rho)^2}{C^2}\|\psi\|^2.}
\tag{QD8}
\]
This follows from
\((1-\rho)\|\psi\|\le\|(I-E_r)\psi\|
\le C\|T_r\psi\|\).

The meaningful construction is a gluing algorithm assembled from local extension maps, with bounded overlap or congestion and an error margin independent of the number of boundary cells. Choosing \(B_r\) as an inverse whose boundedness is inferred from the desired gap would be circular. [[gauge-boundary-frame-gluing/inq|Gauge boundary frames]] and [[markov-edge-measure-solder/inq|local form comparison]] describe relevant ingredients: keep boundary charge data open until parts have been glued, and avoid paying a separate uncontrolled loss for every surface cell.

This is what “geometry forces the bound” could mean concretely: a bounded reconstruction of every physical distinction from its response, with constants fixed by gluing geometry.

The arrow being inverted matters. Here \(T_r\) denotes the response analysis \(\delta_{r,\ell}\), not Euclidean transfer. [[contemporary-puzzles/yang-mills-mass-gap/physical-distinction-coercivity#Stable inversion of which arrow?|The inversion fork]] proves that bounded inversion of physical transfer would impose an ultraviolet ceiling, whereas bounded inversion of its defect detects an infrared gap. [[hessian-response-geometry/response-rigidity-and-multiplicity|Response rigidity]] separately tests when a simple scalar matching law can control the complete response: exact irreducibility or a uniform comparison is needed; a fixed entropy profile and total trace do not suffice.

## The continuum condition belongs to the measured law

An algebraic identity survives a \(*\)-representation, but exact coarse-graining is generally only completely positive. For a UCP map \(\Phi\) and self-adjoint \(R\), its Schwarz defect is
\[
V_\Phi(R):=\Phi(R^2)-\Phi(R)^2\ge0.
\tag{QD9}
\]
Applying \(\Phi\) to (QD5) gives
\[
\Phi(R)^2-\kappa\Phi(R)
=\sum_j\Phi(B_j^*B_j)-V_\Phi(R).
\tag{QD10}
\]
Thus positivity of the original certificate does not automatically imply the same polynomial certificate for the coarse image. The loss term must be retained and controlled. Linear order inequalities do pass through positive maps, but using them still requires the correct coarse response and vacuum-complement comparison.

This is a precise whole--part issue: taking the coarse image and taking a quadratic response do not commute. It parallels the conditional-covariance subtraction in [[rg-covariance-residue/conditioned-source-transport|source transport]] and the full [[rg-covariance-residue/nonlinear-conditional-gauge-response|normalized compact Hessian]]. The needed framework must carry this remainder through composition, not discard it as a normalization detail.

Three consequences follow.

First, topological nontriviality is too weak. A local integer gluing matrix \(A_n=I-S_n\), with \(S_n\) the nilpotent shift, has determinant one, zero kernel, trivial integral cokernel, and norm at most two. Yet
\[
\lambda_{\min}(A_n^*A_n)
=4\sin^2\!\frac{\pi}{4n+2}\longrightarrow0.
\tag{QD11}
\]
The formula follows by solving the tridiagonal eigenvalue recurrence with one free and one fixed endpoint. Even bounded local coefficients and a unit residue do not give a bounded gluing inverse.

Second, convergence must not allow soft normalized states to escape into growing volume, changing representations, or increasingly collective observables. Strong operator convergence alone does not exclude this: on \(\ell^2\),
\[
R_n=I-(1-1/n)|e_n\rangle\langle e_n|
\longrightarrow I\quad\text{strongly},
\qquad\inf\sigma(R_n)=1/n.
\tag{QD12}
\]
A compactness route would need a no-escape theorem for normalized low-response vectors, not just compact configuration fibers.

Third, ultraviolet stability is not infrared mass. [[rg-covariance-residue/uniform-gaussian-conditional-locality|The massless Gaussian construction]] already has uniform conditional response control through blocking depth. [[conditional-fisher-coercivity/weak-coupling-patch-threshold|The fixed-patch Wilson test]] now identifies the retained obstruction in the actual nonlinear law: a slow boundary-path response survives interior gauge reduction, and its neutral loop completion defeats the proposed \(1/n\) patch threshold on the global invariant carrier for fixed \(n\ge8\). This is a failure of that certificate, not of the mass gap. A nonlinear construction must control the retained law at one fixed physical scale as well as the fibers it discards. The needed bounds concern the full effective law, induced horizontal metric, interaction tails, and renormalized sources—not only the Wilson coefficient or a near-identity Hessian.

## The most suggestive small model of necessity

[[contemporary-puzzles/yang-mills-mass-gap/pointing-coercivity-and-the-flat-partner-law|The flat-partner pointing theorem]] has the explanatory form worth generalizing. For an ordered pair
\[
A=\partial_N+W(N),\qquad
AA^*=-\partial_N^2+\lambda,
\tag{QD13}
\]
with real smooth \(W\) on the entire line, a homogeneous partner and a nonzero normalizable vector in \(\ker A\) force \(\lambda>0\). The resulting logistic family has a positive scale-shadow edge. Normalizability alone would not: the same note gives heavy-tailed counterexamples.

This is closer to a grounding argument than an unexplained positive Hessian. A compatible pair of carrier laws makes zero edge impossible. But the homogeneous-partner law is an extra premise, its magnitude remains unfixed, and the carrier is a commutative logarithmic-scale shadow. The [[causal-scale-theory/theorems/rigid-sech-response-identities|cosmological profile identities]] are a different, weaker rigidity: they begin with the stipulated pulse and separate homogeneous conservation.

[[binary-information-geometry/matrix-flat-partner-rigidity|The matrix extension]] narrows the proposed next step. A scalar homogeneous matrix partner forces simultaneous diagonalization, hence independent scalar channels. A nonscalar positive partner can admit noncommuting channels, but its matrix stiffness is then extra data. Moreover, one normalizable kernel line can coexist with an unpointed gapless channel. A field-valued analogue must derive its partner law and control all physical directions, not merely replace scalar symbols with matrices.

An ordered factorization also explains how asymmetry can coexist with an even response: \(A^*A\) and \(AA^*\) share nonzero singular spectrum but can have different kernels. Their graded operator
\[
\mathcal D=
\begin{pmatrix}0&A^*\\A&0\end{pmatrix}
\]
packages this relation after domains are fixed. The index records kernel imbalance, not the magnitude of the gap. This is a plausible role for Clifford completion; it is not yet a physical chirality or time theorem.

## Cosmology is a second return of the same object, not a larger box

There is no intrinsic distinction between “microscopic” and “cosmic” in (QD1). Those descriptions enter through realized ratios and states. A meaningful cosmological extension asks the same upstream structure to return both a vacuum spectral law and a thermal or material history, with a common scale source and compatible normalizations.

The existing [[trace-source-two-moment-solder|trace-source construction]] makes this test precise: a thermal first moment yields a nonconformal equation-of-state response, while a vacuum separated two-point function yields a positive spectral measure. An entire family of such insertions, not one trace channel, is needed for a full mass bound.

The particularly useful relative cosmological invariant is
\[
\Xi_\Theta(N_1,N_2)
=\int_{N_1}^{N_2}\frac{\rho-3p}{\rho}\,dN
=\log\frac{a_2^4\rho_2}{a_1^4\rho_1},
\tag{QD14}
\]
under the explicitly declared homogeneous conservation law. [[contemporary-puzzles/yang-mills-mass-gap/trace-residue-as-a-scale-cocycle|Its composition law]] is additive and its value does not depend on the arbitrary origin of logarithmic scale. This is a promising return type for an upstream descent valuation. It is not yet that valuation: a nonconformal episode need not produce entropy, a coboundary need not be quantized, and a thermal expectation does not fix vacuum spectral support.

The [[cosmological-reconvergence-contract|reconvergence contract]] therefore seeks a common-source theorem, not equality by analogy. A clean first target is to construct the vacuum gap and a thermal scale in the same pure-gauge theory, giving a dimensionless ratio such as \(\Delta_E/(k_BT_c)\). A cosmological claim then needs the additional matter, state, and history maps. Pure Yang--Mills, full QCD, and the cosmic material mixture are not interchangeable carriers.

In particular, [[contemporary-puzzles/yang-mills-mass-gap/pair-annihilation-quotient-and-the-baryon-acoustic-carrier|the pair-annihilation quotient]] preserves a previously supplied net baryon charge; its relaxation generator annihilates all retained-charge observables. It can model exposure of an asymmetry without generating the asymmetry or its mass. “Mass engagement,” baryogenesis, and a vacuum gap can be related by a deeper construction, but the relationship has to act on these distinct objects.

This programme does not require a narrative of primordial jitter, inflation, or symmetry breaking as a trigger. Nor does rejecting such a narrative prove the alternative. The mathematical obligation is to construct the common object and both returns, retaining the observational constraints each return must satisfy.

## The Copernican change is in explanatory order

[[contemporary-puzzles/yang-mills-mass-gap/oriented-descent-angle-and-emergent-symmetry|An oriented arrow]] can determine its stabilizer, and [[algebra/quotient-unitarity-and-kernel-stabilization|a kernel stabilizer]] can determine which transformations descend to the local quotient. Exceptional geometry supplies concrete examples of this order. The remaining task is to make that same construction select the state, the response, and a certificate such as (QD5) or (QD7).

Unitarity is not time-reversal symmetry, and a unitary clock is compatible with a gap. The assumption to question is that a whole-to-part formation map must itself be a unitary clock evolution. Noninvertible realization and local unitary dynamics can be different arrows. Faithful expected compression has important rigidity restrictions, described in [[algebra/faithful-descent-rigidity-and-noiseless-unitarity|the noiseless-sector theorem]]; it cannot simply manufacture a nontrivial reversible sector from a self-adjoint dissipative clock.

Likewise, no preferred unit is not exact dilation symmetry within one vacuum. [[contemporary-puzzles/yang-mills-mass-gap/scale-torsor-and-the-global-local-gap-invariant|The scale-family theorem]] shows that exact same-carrier dilation covariance forbids a positive edge, whereas covariance between calibrated members can preserve a dimensionless gap. The construction must say how state selection, an anomaly, or another independently derived comparison selects a physical member.

My present deduction is therefore a **stateful, scale-covariant geometry of directed descent with quantitative rigidity and a physical reconstruction**. The name is descriptive, not a claim that a known mathematical category already solves the problem. The decisive advance would be an independently derived algebraic certificate or uniformly bounded gluing construction on the complete physical carrier, stable under the actual non-Abelian RG law. Merely adding a more general algebra, an exceptional sphere, or nonunitary language does not force that advance.
