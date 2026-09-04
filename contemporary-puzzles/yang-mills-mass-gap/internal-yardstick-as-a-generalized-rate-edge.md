# The Internal Yardstick as a Generalized Rate Edge

An internal mass yardstick should be a positive generalized spectral edge on one physical tangent carrier, not a quotient of unrelated equations that happen to share units. Two closed rate forms give such an edge: a locally constructed transfer or descent response and a cosmic scalar clock form calibrated by a global selector. This yields an exact conditional Hamiltonian-gap theorem and separates a sufficient lower rate from a cosmological scale-separation factor and a gravity-independent Yang--Mills coefficient. A dualizable endocorrespondence supplies a concrete discrete normalization candidate: if its categorical-index growth is naturally welded to horizon log-capacity, fusion depth quantizes the endpoint ratio of Hubble rates even while each local cosmological patch remains smooth.

**Status: [EXACT FUNCTIONAL ANALYSIS] for the generalized Rayleigh-edge and conditional energy-gap statements; [ESTABLISHED] for the optimal relative-entropy meaning of log index on infinite-dimensional factors; [STANDARD] for categorical-dimension multiplicativity in the factor, dualizable, standard-normalization setting; [EXACT CONDITIONAL COROLLARY] for the discrete cosmic scaling laws after the cosmic-capacity/index-capacity weld and two-cut common-count law are assumed; [CONJECTURE] for those physical welds and for lower-bounding the generalized rate edge by the common-count scale ratio; [OPEN] for the physical carrier, normalized forms, any nontrivial global-to-local carrier comparison, wall-to-cosmos synchronization, fossil transport, continuum limit, and gravity-decoupled pure Yang--Mills realization.**

## What the operator operates on

Let \(\mathcal K_0\) be a complex vacuum-reduced tangent carrier. It could arise as an Osterwalder--Schrader history-endpoint space, a standard-form \(L^2\) tangent space of a pointed whole algebra, or a regulator family proved to converge to one of these. Its vectors represent infinitesimal physical distinctions or histories after gauge-null and vacuum directions have been removed. They are not spacetime points, masses, entropy values, or abstract propositions.

Suppose \(\mathfrak a_{\mathrm{loc}}\) and \(\mathfrak b_{\mathrm{cos}}\) are densely defined closed positive quadratic forms of rate type. Fix any reference duration \(\tau_{\mathrm{ref}}>0\), used only to metrize their common form domain, and require \(\mathcal D\subseteq\operatorname{Dom}\mathfrak a_{\mathrm{loc}}\cap\operatorname{Dom}\mathfrak b_{\mathrm{cos}}\) to be a form core for the positive sum form with norm

\[
\|x\|_{\mathcal D}^2
:=
\|x\|^2
+\tau_{\mathrm{ref}}
\bigl(\mathfrak a_{\mathrm{loc}}[x]
+\mathfrak b_{\mathrm{cos}}[x]\bigr).
\]

Changing \(\tau_{\mathrm{ref}}\) to another finite positive value gives an equivalent core norm and introduces no physical clock. The intended meanings are

\[
\mathfrak a_{\mathrm{loc}}
=
\text{local transfer attenuation or tangential descent response},
\qquad
\mathfrak b_{\mathrm{cos}}
=
\text{global clock or capacity-flow comparison}.
\tag{RY1}
\]

Assume \(\mathfrak b_{\mathrm{cos}}[x]>0\) for every nonzero \(x\in\mathcal D\). The generalized lower edge is

\[
\boxed{
Q_{\mathrm{rat}}
:=
\inf_{0\neq x\in\mathcal D}
\frac{\mathfrak a_{\mathrm{loc}}[x]}
{\mathfrak b_{\mathrm{cos}}[x]}.}
\tag{RY2}
\]

The Rayleigh infimum (RY2) is primary; no operator product is needed to define it. If the forms are represented by positive self-adjoint operators \(A\) and \(B\), with \(B\geq\beta I\) for some \(\beta>0\), define the pullback form on

\[
\operatorname{Dom}\widetilde{\mathfrak a}
:=
\bigl\{y\in\mathcal K_0:
B^{-1/2}y\in\operatorname{Dom}\mathfrak a_{\mathrm{loc}}\bigr\}
\]

by

\[
\widetilde{\mathfrak a}[y]
:=
\mathfrak a_{\mathrm{loc}}[B^{-1/2}y]
\tag{RY3}
\]

If \(\widetilde{\mathfrak a}\) is densely defined and closed and \(B^{1/2}\mathcal D\) is a form core for it, the representation theorem supplies a positive self-adjoint relative operator \(\mathcal R\) with \(\widetilde{\mathfrak a}[y]=\|\mathcal R^{1/2}y\|^2\) and \(Q_{\mathrm{rat}}=\inf\sigma(\mathcal R)\). The transformed-core clause is what licenses replacement of the infimum over \(\mathcal D\) by the full spectral infimum. The symbol \(B^{-1/2}AB^{-1/2}\) is only form shorthand unless stronger operator-domain hypotheses are proved. The scalar-denominator case \(B=H_cI\) below is safe. In infinite volume the lower edge need not be an eigenvalue. Calling it a spectral edge rather than an eigenvalue keeps the formulation compatible with a continuous nonvacuum spectrum.

A possible input is a strongly continuous semigroup of injective positive self-adjoint contractions \(C_u\) on \(\mathbb C\Omega\oplus\mathcal K_0\), with fixed space exactly \(\mathbb C\Omega\). Let \(u\) be a canonically normalized dimensionless composition coordinate. Functional calculus then defines on \(\mathcal K_0\) the dimensionless generator

\[
\widehat K_{\mathrm{loc}}
=
-\frac1u\log C_u
,
\qquad
K_{\mathrm{loc}}^{(t)}
:=
\nu_u\widehat K_{\mathrm{loc}},
\qquad
[\nu_u]=T^{-1}.
\tag{RY4}
\]

Only after an independently constructed clock solder \(\nu_u\) is supplied can \(K_{\mathrm{loc}}^{(t)}\) represent the rate form \(\mathfrak a_{\mathrm{loc}}\). If \(u\) is one e-fold and the scale coordinate has been synchronized with proper time at the selected cut, the candidate is \(\nu_u=H_c\); that synchronization is not automatic. Under \(u'=au\), the same semigroup has \(\widehat K'_{\mathrm{loc}}=\widehat K_{\mathrm{loc}}/a\). A freely rescalable parameter has no intrinsic edge. [[past-future-angle-and-the-transfer-gap]] owns the supported transfer construction, while [[mass-as-a-calibrated-distinction-rate]] owns its clock calibration.

## Conditional rate-edge theorem

Fix a selected expanding cosmic cut with \(H_c>0\). Take

\[
\mathfrak b_{\mathrm{cos}}[x]
=
H_c\|x\|^2.
\tag{RY5}
\]

Let \(H_{\mathrm{YM}}\geq0\) be the reconstructed physical Hamiltonian and define its vacuum projection by \(P_0:=E_{H_{\mathrm{YM}}}(\{0\})\), so \(P_0\) reduces \(H_{\mathrm{YM}}\) and \(H_{\mathrm{YM}}P_0=0\). Suppose a spectrum-independent complex-linear form map

\[
J:
\operatorname{Dom}(H_{\mathrm{YM}}^{1/2})\cap(1-P_0)\mathcal H_{\mathrm{YM}}
\longrightarrow
\mathcal D
\tag{RY6}
\]

is isometric and an independently proved energetic solder satisfies

\[
\frac1\hbar
\|H_{\mathrm{YM}}^{1/2}\psi\|^2
\geq
\eta_{\mathrm{sol}}\,
\mathfrak a_{\mathrm{loc}}[J\psi],
\qquad
\eta_{\mathrm{sol}}>0.
\tag{RY7}
\]

If \(Q_{\mathrm{rat}}>0\), then (RY2), (RY5), and (RY7) give

\[
\boxed{
H_{\mathrm{YM}}
\geq
\hbar\eta_{\mathrm{sol}}H_cQ_{\mathrm{rat}}(1-P_0),
\qquad
\Delta_E
\geq
\hbar\eta_{\mathrm{sol}}H_cQ_{\mathrm{rat}}.}
\tag{RY8}
\]

This is an exact implication, but it is explanatory only if \(\mathfrak a_{\mathrm{loc}}\), \(J\), and \(\eta_{\mathrm{sol}}\) are constructed without the Hamiltonian edge being bounded. Defining \(\mathfrak a_{\mathrm{loc}}[J\psi]=\langle\psi,H_{\mathrm{YM}}\psi\rangle/\hbar\) would merely rewrite the problem. After full Poincare covariance, a unique vacuum, the spectrum condition, and Lorentz invariance of the joint translation spectrum are proved, the separate Casimir lemma converts (RY8) into

\[
m_{\mathrm{gap}}
\geq
\frac{\hbar\eta_{\mathrm{sol}}H_cQ_{\mathrm{rat}}}{c^2}.
\tag{RY9}
\]

Equation (RY8) is the scalar-denominator generalized-Rayleigh corollary of the theorem in [[causal-frame-coercivity]], not a second gap mechanism. [[localized-relative-entropy-and-the-energy-solder]] supplies one established upper bound on a response or relative-entropy form by the Hamiltonian form that a construction of (RY7) may consume. [[joint-causal-generators-and-the-mass-casimir#Energy gap and Casimir floor are equivalent only after Lorentz reconstruction]] owns the last step to (RY9).

## The scale ratio is not yet the rate edge

The common-count construction in [[cosmological-selection-of-the-yang-mills-yardstick]] gives the exact conditional scale ratio

\[
Q_{\mathrm{cc}}
:=
\frac{R_c}{\lambda_*}
=
\frac{E_*}{\hbar H_c}
=
e^{\Sigma_c},
\qquad
Q_{\mathrm{cc}}^3
=
\frac{3}{4\pi\gamma s_*}\frac{S_{A,c}}{k_B}.
\tag{RY10}
\]

This is a rate separation after the length-to-clock solder \(\omega_*=c/\lambda_*\), because \(Q_{\mathrm{cc}}=\omega_*/H_c\). It is not yet the spectral edge associated with (RY3). Compatibility with the lower-bound factorization [[cosmological-selection-of-the-yang-mills-yardstick#The pure-Yang--Mills decoupling fork|developed in the cosmological selector]] requires the sufficient comparison target

\[
\boxed{
\eta_{\mathrm{sol}}Q_{\mathrm{rat}}
\geq
\underline C_{\mathrm{YM}}^{(\mathsf s)}
C_{\mathrm{cos}}^{(\mathsf s)}
Q_{\mathrm{cc}},
\qquad
\underline C_{\mathrm{YM}}^{(\mathsf s)}>0,
\qquad
C_{\mathrm{cos}}^{(\mathsf s)}>0,}
\tag{RY11}
\]

where \(\underline C_{\mathrm{YM}}^{(\mathsf s)}\) is a lower-bound coefficient proved from the neutral Yang--Mills response independently of \(G\), \(H_c\), the measured gap, and the exact gap coefficient, while \(C_{\mathrm{cos}}^{(\mathsf s)}\) converts the cosmologically selected member to the fixed Yang--Mills convention. Equality would be a separate sharpness statement, not part of the existence proof. The normalizations of the two forms, \(\eta_{\mathrm{sol}}\), and the scheme conversion must be fixed prospectively; none is intrinsically one. Substitution in (RY8) yields

\[
\Delta_E
\geq
\underline C_{\mathrm{YM}}^{(\mathsf s)}
C_{\mathrm{cos}}^{(\mathsf s)}E_*.
\tag{RY12}
\]

The composition laws expose the missing theorem. If a one-e-fold transfer contraction has nonvacuum spectral radius \(\rho\), then its dimensionless attenuation edge is

\[
Q_{\mathrm{tr}}
=
-\log\rho.
\tag{RY13}
\]

Equating it with \(Q_{\mathrm{cc}}=e^{\Sigma_c}\) requires \(\rho=e^{-e^{\Sigma_c}}\), not merely a shared absence of units. A natural law \(\rho=e^{-\Sigma_c}\) would instead give \(Q_{\mathrm{tr}}=\Sigma_c\). A carrier-changing correspondence must therefore preserve the declared additive and multiplicative laws; dimensional agreement alone cannot establish (RY11).

For a one-e-fold contraction, \(Q_{\mathrm{tr}}\) is dimensionless. The corresponding physical rate form is \(H_cQ_{\mathrm{tr}}\|x\|^2\) only after the e-fold coordinate and the physical clock have been synchronized at the cut.

## Why an invariant edge cannot fix an unpointed scale

There is a dilation trilemma. Under the whole-solution dilation

\[
H_c\longmapsto\mu H_c,
\qquad
t\longmapsto\mu^{-1}t,
\qquad
\mu>0,
\tag{RY14}
\]

a dilation-invariant \(\mathcal R\) has a fixed \(Q_{\mathrm{rat}}\), so the proposed dimensional gap \(\hbar H_cQ_{\mathrm{rat}}\) still scales by \(\mu\). The edge has not selected an absolute member.

Suppose instead that one asks the operator to compensate the scale freedom through a unitary covariance, with equality of self-adjoint operators including their domains,

\[
V_\mu\mathcal RV_\mu^*
=
\mu^{-1}\mathcal R
\qquad
\text{for every }\mu>0.
\tag{RY15}
\]

Unitary invariance of the spectrum and (RY15) imply that if the positive spectrum contains one \(r>0\), it contains \(\mu^{-1}r\) for every \(\mu>0\). Its closure contains zero, so a nonzero positive operator satisfying this full covariance has

\[
\sigma(\mathcal R)=[0,\infty),
\qquad
\inf\sigma(\mathcal R)=0.
\tag{RY16}
\]

Thus one finite positive generalized edge cannot both remain gapped and compensate an unbroken continuous dilation symmetry within one unitarily equivalent family. A state, wall, boundary section, discrete orbit, or other pointing must first select a member. This is the operator version of the normalization obstruction in (CY17a)--(CY17d).

[[mass-as-casimir-and-realization#A gap obstructs exact same-carrier dilation covariance]] owns the general same-carrier spectral no-go; the present use applies it to the normalization pencil.

## Categorical depth as a discrete normalization candidate

Let \(\mathcal M\) be a factor and let \(X\) be an intrinsically normalized dualizable \(\mathcal M\)-\(\mathcal M\) correspondence with standard statistical dimension

\[
d:=d(X)>1.
\]

For \(n\in\mathbb N_0\), put

\[
X_0:=L^2(\mathcal M),
\qquad
X_n:=X^{\boxtimes_{\mathcal M}n},
\qquad
N_0:=N_b,
\qquad
\iota_0:=\iota_b.
\]

Multiplicativity under Connes fusion gives

\[
d(X_n)=d^n,
\qquad
\operatorname{Ind}_{\mathrm{cat}}(X_n):=d(X_n)^2=d^{2n},
\qquad
\mathscr A_n:=\log d(X_n)=n\log d.
\tag{RY17}
\]

When \(X\) is the sector endocorrespondence of a finite-index endomorphism \(\rho:\mathcal M\to\mathcal M\), \(\operatorname{Ind}_{\mathrm{cat}}(X)\) agrees, under the standard solution, with the minimal Jones--Kosaki index of \(\rho(\mathcal M)\subseteq\mathcal M\). It is not the index of an arbitrary chosen expectation. The correspondence is dualizable but noninvertible for \(d>1\); negative fusion powers are not supplied by taking its conjugate.

For a standard minimal finite-index sector on infinite-dimensional factors, the right side already has an exact operational meaning. If \(\varepsilon_{X_n}\) is the associated standard expectation, Longo and Witten's optimality theorem and the dual relative-entropy identity give

\[
\sup_\varphi
S(\varphi\Vert\varphi\circ\varepsilon_{X_n})
=
\log\operatorname{Ind}_{\mathrm{cat}}(X_n)
=
2n\log d,
\tag{RY17a}
\]

while the statewise loss for \(\varepsilon_{X_n}\) plus the complementary loss for its commutant-dual expectation equals the same constant. [[two-sided-index-capacity-and-the-cosmic-weld]] owns the hypotheses, the finite-dimensional factor-of-two firewall, and the exact two-sided formula.

There are then two physical hypotheses, not one. Directly identifying additive entropy increments would give \(\iota_n-\iota_b=2n\log d\) and \(H_n/H_b=(1+2n\log d/\iota_b)^{-1/2}\). The geometric ladder below uses the strictly stronger **multiplicative cosmic-cell/index-capacity weld** between a birth cut \(b\) and the cut assigned to fusion rung \(n\):

\[
\boxed{
\log\frac{\iota_n}{\iota_b}
=
\log\operatorname{Ind}_{\mathrm{cat}}(X_n)
=
2n\log d.}
\tag{RY18}
\]

Equation (RY18) is not implied by the finite product-edge identity \(\iota_{\mathrm{cell}}=\tfrac12\log\operatorname{Ind}\). The latter identifies an entropy count with a half-log index for an uncorrelated edge state; (RY17a) is the full, potentially side-information-assisted relative-entropy capacity; and (RY18) identifies the **logarithmic growth of a cosmic whole capacity** with that index capacity. These are three different functions or carriers. Constructing the last natural transformation is the load-bearing theorem target.

[[deriving-g-v2/index-not-entropy|Index, not entropy]] owns the restricted half-log identity and its normalization warnings. The factor of two on the index side is now fixed by the standard categorical/Kosaki index convention. The logarithm and capacity ratio on the cosmic side of (RY18) remain new physical clauses, not consequences of categorical multiplicativity. If both sides compose additively, the whole ladder follows from a single one-generator weld; the rung set is discrete only after \(X\), its standard normalization, and \(d\) have been fixed independently.

Assume an expanding flat Einstein--FLRW realization, fixed \(c,G,\hbar\), a common-count law at both cuts with the same \(\gamma s_*>0\), and a synchronization \(n\mapsto N_n\). Since \(\iota_A\propto H^{-2}\), \(Q_{\mathrm{cc}}\propto\iota_A^{1/3}\), and \(\omega_*=H Q_{\mathrm{cc}}\), (RY18) gives the exact conditional ladder

\[
\boxed{
\frac{H_n}{H_b}=d^{-n},
\qquad
\frac{Q_{\mathrm{cc},n}}{Q_{\mathrm{cc},b}}=d^{2n/3},
\qquad
\frac{\omega_{*,n}}{\omega_{*,b}}=d^{-n/3}.}
\tag{RY19}
\]

The same synchronization turns the smooth expansion history into the endpoint quantization condition

\[
\boxed{
\int_{N_b}^{N_n}\epsilon(N)\,\mathrm dN
=
\log\frac{H_b}{H_n}
=
n\log d.}
\tag{RY20}
\]

This is the precise sense in which a discrete global geometry can coexist with smooth local patches: \(H(N)\) may vary continuously between cuts, while the admissible endpoint ratios belong to the multiplicative ladder \(d^{-\mathbb N_0}\). If \(\iota_b\) is independently fixed in the Einstein-capacity normalization, then

\[
H_n
=
\left(
\frac{\pi c^5}{G\hbar\iota_b}
\right)^{1/2}d^{-n}.
\tag{RY21}
\]

Alternatively, an independently constructed proper duration can calibrate \(H_n\) through [[cosmological-selection-of-the-yang-mills-yardstick#Normalized acceleration can select a cut; it adds no independent unit|the age-calibration identity (CY17h)]], leaving (RY20) as the discrete endpoint constraint. Boltzmann's constant contributes through the dimensionless capacity \(\iota=S/k_B\); it does not by itself supply a duration or energy.

The ladder must stop at the selected engagement rung if \(\omega_*\) is to fossilize. Continuing (RY19) as a live law would make the local scale drift. If common count is asserted only at the selected cut, only the single-cut formula in (RY10) follows; the ratios involving \(Q_{\mathrm{cc}}\) and \(\omega_*\) require the stronger two-cut premise.

The finite algebra in (RY2), (RY17)--(RY20), and the independent-age identity is exercised by [[contemporary-puzzles/yang-mills-mass-gap/receipts/internal-yardstick-rate-edge-receipt.py|the internal-yardstick receipt]] and its [[contemporary-puzzles/yang-mills-mass-gap/receipts/internal-yardstick-rate-edge-receipt-output.txt|stored output]]. The receipt verifies arithmetic and a diagonal finite-form benchmark; it does not test the log-capacity weld, the common carrier, the Yang--Mills limit, or any physical premise.

For finite-dimensional centers, scalar \(d\) must be replaced by the dimension matrix or full correspondence. Scalar minimal index need not multiply without matched spherical or Markov data. [[spectral-wall-descent/scale-correspondence-stack]], [[finite-index-duality-and-the-square-response]], and [[library/minimal-index-and-matrix-dimension-finite-centers/inq|minimal index and matrix dimension]] own these normalization firewalls. [[gauge-index-no-go-and-four-dimensional-center-square]] also forbids the obvious shortcut: the faithful continuous \(SU(N)\) fixed-point inclusion is infinite-index, while the finite ring-center remnant \(|Z(G)|^2\) is not universal.

## The composed Copernican target

The proposed order of explanation is now

\[
\boxed{
\begin{aligned}
\text{whole }(X,d,n_c,\iota_b)
&\longrightarrow
(H_c,Q_{\mathrm{cc}},\omega_*),
\\
\text{neutral Yang--Mills geometry}
&\longrightarrow
(\mathcal K_0,\mathfrak a_{\mathrm{loc}},J,\eta_{\mathrm{sol}}),
\\
\text{scalar calibration of the local carrier}
&\longrightarrow
(\mathfrak b_{\mathrm{cos}},\mathcal R,Q_{\mathrm{rat}})
\longrightarrow
\Delta_E
\longrightarrow
m_{\mathrm{gap}}.
\end{aligned}}
\tag{RY22}
\]

The endocorrespondence composes in the whole categorical stack and supplies a candidate discrete depth through its scalar invariant. As presently formulated, the cosmic branch supplies only \(H_c\), and \(\mathfrak b_{\mathrm{cos}}=H_c\|\cdot\|^2\) is a cosmologically calibrated scalar form on the Yang--Mills carrier. This is a shared mathematical domain, not yet a realized common global/local carrier. A stronger claim would require a declared cosmological carrier and an explicit comparison or pullback map to \(\mathcal K_0\). The rate pencil acts on retained physical tangents and tests every nonvacuum direction. The Hamiltonian acts on the reconstructed local Hilbert space. No one operator performs all three tasks.

This construction is circular if \(d\), \(n_c\), \(\iota_b\), the synchronization, \(Q_{\mathrm{rat}}\), or the response normalization is chosen after inspecting BAO, a glueball mass, the number \(36\), or the Hamiltonian spectral projector. Its prospective content would be a derived fusion object, a unique wall rung, a natural log-capacity weld, and a regulator-uniform positive edge on the resulting physical carrier.

Nor may the cosmic scale replace the pure-Yang--Mills theorem. On the common-count branch,

\[
(\hbar H Q_{\mathrm{cc}})^3
=
\frac{3}{4\gamma s_*}
\frac{\hbar^2c^5H}{G}.
\tag{RY23}
\]

The joint \(G,H\to0\) limit depends on the path through \(H/G\). A controlled pure-gauge limit therefore requires a fossil-selection theorem that holds \(\Lambda_*:=\hbar H_cQ_{\mathrm{cc}}\) fixed while gravitational and cosmological modes decouple, plus an independent proof that \(\underline C_{\mathrm{YM}}^{(\mathsf s)}>0\) survives. Cosmology may select the realized member; it cannot substitute for neutral coercivity.

## Stopping condition

The internal-yardstick programme closes only when all of the following are constructed:

1. a complex vacuum-reduced physical tangent carrier and two closed positive forms of the same rate type, plus an explicit comparison map if a distinct cosmological carrier is claimed;
2. a canonical normalization of the transfer parameter and global clock form;
3. a regulator-uniform lower generalized edge without using the target spectrum;
4. a spectrum-independent energetic solder and Poincare reconstruction;
5. an intrinsically normalized whole correspondence, its categorical dimension, and a uniquely selected nonnegative fusion rung;
6. the natural log-capacity/index weld (RY18) and the synchronization (RY20);
7. an independently fixed birth capacity, proper duration, or other normalization-breaking section;
8. a proof of the lower comparison (RY11), respecting the different composition laws, with sharpness kept separate;
9. fossil transport of the selected dimensional member; and
10. a gravity-decoupled pure-Yang--Mills limit retaining the positive local coefficient.

The gain is not a mass-gap proof. It is a narrower statement of what “the yardstick arises internally” would mean: global algebra selects a discrete depth and a cosmic member; a generalized rate operator tests local distinctions on its physical carrier; and only the composed, carrier-correct theorem produces a physical lower edge.
