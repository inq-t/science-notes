---
inq.module: "global-local-response-reconstruction"
inq.include:
  - "**/*.md"
---
# Global–Local Response Reconstruction

A pre-QFT explanation of a mass gap can be typed as a reconstruction problem. A directed whole-law system must construct local observable carriers and a covariantly specified whole-to-part response; local QFT is then recovered as a representation of that system, and mass is the Poincare presentation of a scale-covariant response edge. There are two genuinely alternative last-mile certificates. A regulator-uniform positive angle can separate every physical midpoint distinction from the information jointly recoverable at the two sides of a fixed physical slab. Alternatively, one clock-normalization-independent static localization exponent can become a common Euclidean-time exponent on an Osterwalder--Schrader-total local family. The first controls a complete boundary-response operator; the second already suffices for a qualitative vacuum-sector gap and need not construct that operator. Neither primitive certificate is itself a particle mass or a smallest length.

**Status: [EXACT DEFINITIONS] for the response operator and scale-covariant invariant; [EXACT CONDITIONAL THEOREMS] for complete-response edge to transfer gap and common OS exponent to Hamiltonian gap; [CONSTRUCTION TARGET] for the pre-QFT realization and QFT recovery; [OPEN] for four-dimensional Yang--Mills.**

## The Copernican change of primitives

The proposed reversal does not discard quantum field theory. It changes its logical place. Instead of assuming a local field algebra, a vacuum representation, and a Hamiltonian and then asking that Hamiltonian to explain its own infrared spectrum, begin with a whole-law object

$$
\mathfrak U
=
\bigl(
\mathsf{Cut},
\mathcal W,
\omega,
\vartheta_{\mathrm{OS}},
\mathsf{Corr},
\mathscr S,
\mathsf C,
\mathsf B
\bigr).
\tag{GR1}
$$

Its slots have distinct types:

- \(\mathsf{Cut}\) is a category of cuts, collars, and composable slabs. It is not initially a set of subsets of a metric spacetime.
- \(\mathcal W(c)\) is an algebra of whole-law distinctions available at \(c\in\mathsf{Cut}\), and \(\omega_c\) is a compatible positive state or weight.
- \(\vartheta_{\mathrm{OS}}\) is a Euclidean reflection structure. It is not the stress-tensor trace, ontological time, or a Lorentzian clock.
- \(\mathsf{Corr}\) assigns correspondences or pointed completely positive processes to directed gluing. Correspondences compose by relative tensor product; process maps compose as maps.
- \(\mathscr S\) is a positive scale torsor. It has ratios but no preferred absolute section.
- \(\mathsf C\) and \(\mathsf B\) are independently normalized whole and local response ledgers whose equality may select a section of \(\mathscr S\).

Reversible changes of presentation, directed formation maps, and reconstructed clock evolution are different arrows. A whole-to-part map may be noninjective without making the later local clock nonunitary. Before a Hilbert carrier and clock have been reconstructed, “the whole is nonunitary” is not a well-typed assertion; the exact statement is that some formation or readout arrows are noninvertible.

The required downstream map is

$$
\mathfrak U
\xrightarrow{\ \mathsf{Rec}\ }
\bigl(
\mathsf{Reg},
\mathcal A,
\omega,
\pi,\mathcal H,\Omega,
U,P_\mu,H
\bigr),
\tag{GR2}
$$

where the output has an isotonic local observable net, a physical vacuum representation, Poincare covariance, the spectrum condition, and a clock Hamiltonian. [[global-local-response-reconstruction/qft-recovery-contract|The recovery contract]] makes these obligations explicit. QFT may therefore remain the correct grammar of local appearance even if it is not the explanatory primitive.

A framework claimed to lie beneath both particle physics and cosmology needs a second return rather than a larger local QFT. [[global-local-response-reconstruction/cosmological-reconvergence-contract|The cosmological reconvergence contract]] requires vacuum and thermal/cosmological reconstructions from one whole object while forbidding their carriers from being collapsed. [[global-local-response-reconstruction/trace-source-two-moment-solder|The trace-source solder]] gives the first precise common test: one scale-source prescription must return a thermal one-point interaction measure in the relevant thermal theory and a connected vacuum two-point spectral response in pure Yang--Mills. These are theory- and state-specific images, not one numerical observable; one scalar channel is not the complete gap. [[global-local-response-reconstruction/radiation-era-horizon-confinement-no-go|The horizon-confinement no-go]] further proves that the lowest or any order-one harmonic of a recovered radiation-era Hubble patch is parametrically far below a QCD-scale edge, so cosmology can enter only through a more structural selection or reconstruction map unless it derives the missing hierarchy.

## What the response operator operates on

Fix a reflected slab in one regulated member \(r\). Let \((\mathcal W_r,\omega_r)\) be its whole algebra and state, with expected midpoint and two-boundary subalgebras

$$
\mathcal M_r,\mathcal B_r\subseteq\mathcal W_r.
\tag{GR3}
$$

Their state-preserving conditional expectations give standard-form isometries

$$
J_{M,r}:L^2_0(\mathcal M_r,\omega_r)
\longrightarrow L^2_0(\mathcal W_r,\omega_r),
\qquad
J_{\partial,r}:L^2_0(\mathcal B_r,\omega_r)
\longrightarrow L^2_0(\mathcal W_r,\omega_r),
\tag{GR4}
$$

where the subscript \(0\) removes the constant or vacuum direction. Define the midpoint-to-boundary conditional-prediction operator

$$
\boxed{
K_r:=J_{\partial,r}^{*}J_{M,r}.}
\tag{GR5}
$$

Thus \(K_r\) operates on centered physical midpoint distinctions and returns their best two-boundary prediction. Its return operator and defect are

$$
S_r:=K_r^*K_r,
\qquad
D_r:=I-S_r.
\tag{GR6}
$$

For every normalized midpoint vector \(f\),

$$
\langle f,D_rf\rangle
=
\inf_{b\in L^2_0(\mathcal B_r,\omega_r)}
\left\|J_{M,r}f-J_{\partial,r}b\right\|^2.
\tag{GR7}
$$

This is exact Hilbert geometry. \(D_r\) measures the irreducible part of a midpoint distinction that is not recoverable from both slab boundaries. It is a squared sine of a subspace angle, not automatically thermodynamic entropy, destroyed information, energy, or a count of facts. Those interpretations require additional realization maps.

The expectations in (GR3)--(GR4) are construction data, not automatic properties of arbitrary inclusions. In a Type-III realization, Takesaki's modular-invariance condition is one exact existence gate. The faces should be regulated time-zero, collar, boundary-frame, or renormalization contexts; under the usual Reeh--Schlieder hypotheses, they cannot simply be ordinary properly nested vacuum AQFT algebras with a vacuum-preserving expectation.

Let \(Q_r\) project onto the complete gauge-invariant vacuum complement of the midpoint carrier. The quantitative global--local distinction condition is

$$
\boxed{
\|K_rQ_r\|\leq\rho_*<1}
\quad\Longleftrightarrow\quad
\boxed{
Q_rD_rQ_r\geq(1-\rho_*^2)Q_r.}
\tag{GR8}
$$

Injectivity is insufficient. The right predicate is bounded-below response, equivalently positive transversality or closed range, on the entire claimed carrier. A finite list of probes, a charged sector, one glueball operator, or an abstract topological obstruction does not establish (GR8).

## The grain is a method, not the number

The response profile \(s\mapsto\|K_{r,s}Q_r\|\) is dimensionless. To present its decay as an inverse length, rate, energy, or mass, one must choose a scale section \(s=\ell\). [[the-grain-of-causal-scale/relational-grain-construction|Matched-ledger scale selection]] supplies one possible method:

$$
\mathsf C_X
=
\mathsf B_X(\ell_X).
\tag{GR9}
$$

The carrier label \(X\) is load-bearing. A CMB anisotropy carrier, a horizon cut, and a Yang--Mills vacuum slab generally have different ledgers and therefore different selected grains. The \(46\)--\(47\,\mathrm{MeV}\) presentation is evidence about one cosmological application of the method; it is not a universal input to (GR8). A common value would require a theorem identifying the carriers and both ledgers, not a numerical resemblance.

[[global-local-response-reconstruction/yang-mills-balanced-fisher-grain|The balanced-Fisher proposal]] supplies the first concrete Yang--Mills-specific selector in this framework: it chooses the RG scale at which one declared, covariantly transported dilation score is divided equally between two-boundary recoverability and midpoint residue. The fixed-carrier split is exact and the balance is dimensionless, but [[scale-score-connection/inq|scale differentiation requires an independently selected connection]], a moving blocking channel adds its own score, and exact blockings are nonunique. The existence, scheme covariance, and continuum stability of the root are open. [[distinction-grain-spectrum/inq|The distinction-grain spectrum]] makes the remaining quantifier explicit: one balanced tangent is one object-relative grain, whereas (GR8) is a uniform statement over every physical nonvacuum distinction.

Scale selection and response attenuation are separately certified, logically non-implicative outputs:

$$
\ell_X
\quad\text{from ledger matching},
\qquad
\rho_X
\quad\text{from whole-law conditional response}.
\tag{GR10}
$$

The two outputs may depend on one common law or even be computed from one response family; the claim is independence of their proof obligations and normalizations, not statistical independence. A topological integer, entropy count, or exceptional orbit may constrain a dimensionless response class. It cannot alone supply the dimensional gap. Conversely, dimensional analysis can generate a length without proving that the response at that length is bounded away from perfect recoverability.

## The joint invariant and the rate presentation

At a selected half-thickness \(\ell_X\), define the dimensionless attenuation depth

$$
\mu_X:=-\log\rho_X.
\tag{GR11}
$$

If \(\ell_X\mapsto a\ell_X\) under a change of scale section, the corresponding inverse-length edge transforms oppositely. The joint quantity

$$
\boxed{
\mu_X
=
\frac{E_{\mathrm{resp},X}\ell_X}{\hbar c}
=
\frac{M_{\mathrm{resp},X}\ell_Xc}{\hbar}}
\tag{GR12}
$$

is scale-invariant after energy and mass have been reconstructed. This is the precise version of the earlier Casimir clue: a single scale generator can transform nontrivially while a joint invariant of oppositely scaling directions remains fixed.

One may then define an attenuation rate

$$
\Gamma_X
:=
\frac{c}{\ell_X}\mu_X,
\tag{GR13}
$$

and obtain the dimensional presentations

$$
\displaystyle
E_{\mathrm{resp},X}=\hbar\Gamma_X,
\qquad
M_{\mathrm{resp},X}=\frac{\hbar}{c^2}\Gamma_X
=
\frac{\hbar}{c\ell_X}\mu_X.
\tag{GR14}
$$

Equations (GR13)--(GR14) define the response-derived lower-edge presentations; the actual spectral gap may be larger. They do not identify the concepts mass, energy, time, and response. They state the comparison maps that become available after a clock, a causal conversion \(c\), and a quantum action unit \(\hbar\) have been recovered or imported. Before those maps, \(\mu_X\) is the invariant object.

## Exact bridge to a Hamiltonian gap

Let the regulated reflected path law be stationary and reversible, with positive vacuum-normalized transfer step

$$
P_r
=
\exp\!\left[
-\frac{a_{\tau,r}}{\hbar c}(H_r-E_{0,r})
\right].
\tag{GR15}
$$

Take a slab of half-depth \(n_r\), so its physical half-thickness approaches

$$
n_ra_{\tau,r}\longrightarrow\ell_X>0.
\tag{GR16}
$$

Assume additionally that the transfer realization is Markov, so prediction from the midpoint to either one boundary at depth \(n_r\) is \(P_r^{n_r}\), and that this one-boundary datum is a subalgebra of the jointly framed two-boundary datum used in (GR5). Let the vacuum complement reduce the transfer and response operators. Reversibility identifies \((P_r^{n_r})^*P_r^{n_r}=P_r^{2n_r}\), and conditional-expectation data augmentation then gives

$$
Q_rP_r^{2n_r}Q_r
\leq
Q_rK_r^*K_rQ_r.
\tag{GR17}
$$

Consequently, the regulator-uniform bound (GR8) implies

$$
\boxed{
H_r-E_{0,r}
\geq
\frac{\hbar c}{n_ra_{\tau,r}}
\log(\rho_*^{-1})Q_r.}
\tag{GR18}
$$

At fixed physical thickness this has the nonzero limit candidate

$$
\Delta_*
=
\frac{\hbar c}{\ell_X}\log(\rho_*^{-1}).
\tag{GR19}
$$

The finite-regulator implication is exact; [[contemporary-puzzles/yang-mills-mass-gap/collared-surface-response-to-the-clay-gap|the collared-surface theorem]] gives the proof and lists the continuum hypotheses. A one-step bound at fixed lattice depth is not enough, because its physical thickness vanishes under refinement.

After Osterwalder--Schrader and Poincare reconstruction, (GR18) becomes an energy-spectrum statement and then an invariant-mass statement. Before that reconstruction it is a transfer estimate, not yet the Clay mass gap.

## Why the whole-law response is the explanatory locus

The response is defined from the joint slab law, not from a local classical two-jet. This matters in Yang--Mills. The flat Wilson-action Hessian abelianizes to a Maxwell cochain form and retains physical soft modes; it cannot yield the desired bound. [[nonlinear-whole-law-surface-response/inq|Nonlinear whole-law surface response]] therefore asks for the response after the compact gauge variables have been integrated and the collars glued.

The proposed category-error diagnosis can now be made without denying the standard problem:

1. a gauge-dependent field is not the gauge-invariant observable carrier;
2. a local action density is not the selected global vacuum representation;
3. a classical Hessian is not the whole-law conditional response;
4. a dimensionless response edge is not yet an energy;
5. an energy gap is not yet invariant mass until Poincare reconstruction.

The Clay problem itself remains well typed. The category mistake lies in expecting a coefficient or local perturbative presentation at the first level to contain the grounding reason for a spectral property at the fourth and fifth.

## Two exact stopping certificates

The complete fixed-collar response angle is the stronger boundary-response certificate, but it is not required by the exact spectral last mile. [[auxiliary-response-localization/inq|Auxiliary response localization]] proves the alternative route. A local proof dynamics may have an arbitrary time normalization; if its centered \(L^2\) forgetting rate and multiplicativity-defect influence speed are both controlled, eliminating that auxiliary time gives a normalization-invariant **static** inverse-distance exponent.

Let one limiting reflected law \(\omega_\infty\) satisfy the full OS hypotheses and reconstruct \((\mathcal H_\infty,H_\infty,P_{0,\infty})\). Put

$$
A_\infty
:=
\frac{H_\infty-E_{0,\infty}}{\hbar c}\geq0,
\qquad
P_{0,\infty}:=\mathbf1_{\{0\}}(A_\infty),
\qquad
Q_\infty:=I-P_{0,\infty}.
\tag{GR19a}
$$

If \(\mathcal D_{\mathrm{loc}}\subset Q_\infty\mathcal H_\infty\) has dense linear span and one \(\sigma_*>0\) satisfies, for every \(\psi\in\mathcal D_{\mathrm{loc}}\),

$$
0\leq
\langle\psi,e^{-sA_\infty}\psi\rangle
\leq
C_\psi e^{-\sigma_*s}
\qquad(s\geq s_\psi),
\tag{GR19b}
$$

where \(C_\psi<\infty\) and \(s_\psi<\infty\) may depend on \(\psi\), then the spectral theorem gives

$$
H_\infty-E_{0,\infty}
\geq
\hbar c\,\sigma_*Q_\infty.
\tag{GR19c}
$$

This dense-local-family route avoids a transverse-surface union bound because it annihilates the low spectral projection vector by vector and then uses Hilbert-space density. It does not construct the complete midpoint-to-two-boundary operator \(K_r\). Conversely, subjective pair correlations controlled uniformly under every subfamily pinning can be tensorized by [[library/tensorizing-maximal-correlations/inq|Peyre's theorem]] into \(\rho(U_I,U_J)\leq\min\{1,\|E_{I,J}\|_{2\to2}\}\). An area-stable complete angle requires the resulting matrix norm, not merely each entry, to be uniformly smaller than one. The two certificates have the same downstream spectral consequence under their respective limiting-law and reconstruction hypotheses, but different strengths and different missing lemmas.

## What the candidate mathematics can contribute

[[global-local-response-reconstruction/realization-ledger|The composite realization ledger]] gives the longer claim-and-gap audit. Its central verdict is that the clues compose but do not substitute for one another: topology may construct the carrier, Type III and cocycles organize comparison, the nonlinear whole law supplies the actual response, and OS reconstruction supplies the clock.

| Candidate structure | Legitimate contribution | What it does not yet provide |
|---|---|---|
| [[wall-construction-interface/core-spectral-wall|Type-III standard forms and canonical cores]] | standard-form carrier language, weight-independent core comparison, scale covariance, finite comparison corners | physical cut functor, selected vacuum, or clock Hamiltonian |
| [[modular-cocycle-tomography/inq|Connes cocycles]] | comparison of faithful state charts and a test for common blind directions | an ordinary one-parameter group, irreversible time, or a gap |
| [[trace-dirichlet-descent/standard-form-pullback-and-reducing-wall|conditional expectations and correspondences]] | typed restriction, prediction, forgetting, and composable gluing | a positive uniform response angle by themselves |
| [[hessian-response-geometry/inq|relative-entropy or BKM Hessians]] | positive local state-response forms with monotonicity | complete physical coverage or an energy solder |
| [[knotting-as-dimensional-presentation/inq|knots]], holonomy, and discrete descent | domain or sector restrictions and possible removal of specific zero channels | neutral-sector coverage, quantitative rigidity, or a continuum scale |
| [[contemporary-puzzles/yang-mills-mass-gap/octonionic-phase-space-and-the-born-rule-firewall|exceptional Jordan and Freudenthal geometry]] | candidate whole from which familiar stabilizers and symplectic phase carriers descend | state selection, dynamics, Born rule, or every compact simple \(G\) |
| entropy and horizon ledgers | possible independently normalized whole counts in (GR9) | automatic identity with Yang--Mills response or energy |

The common lesson is that algebraic obstruction supplies a kernel statement; the mass gap requires a quantitative, normalized, same-carrier inequality.

## The construction still owed

For every compact simple \(G\), let \(r\in\mathfrak R_G\) range along one declared directed net of volume and cutoff removal. A completed framework must construct a functorial family and one route-specific certificate

$$
\mathsf F_G:
\mathfrak U_G
\longmapsto
\left(
\left\{
\bigl((\mathcal W_{r,G},\omega_{r,G}),
\ell_{r,G},
\mathsf{Rec}_{r,G}\bigr)
\right\}_{r\in\mathfrak R_G},
\omega_{\infty,G},
\mathfrak C_G
\right)
\tag{GR20}
$$

where \(\omega_{\infty,G}\) is one nontrivial limiting reflected law along that same net, not a route-dependent subsequential limit, and \(\mathfrak C_G\) is either the complete-angle data \(\{K_{r,G},Q_{r,G}\}_r\) or the dense-local-family data \((\mathcal D_{\mathrm{loc},G},\sigma_*,\{F_{\psi,r}\})\). The construction must satisfy:

1. the regulated states and whichever certificate is selected come from upstream data without consulting the desired low spectrum;
2. in the complete-angle branch, \(Q_{r,G}\) covers the complete physical midpoint vacuum complement and (GR17) supplies the same-carrier transfer comparison; in the dense-local-family branch, the limiting vectors reconstructed from the coherent centered gauge-invariant families \(F_{\psi,r}\) have total span in \(Q_{\infty,G}\mathcal H_{\infty,G}\);
3. either the fixed-thickness inequality has \(\limsup_{r\to\infty}\|K_{r,G}Q_{r,G}\|<1\), or one common physical exponent is uniform in \(r\) for each coherent local family, with its prefactor and onset allowed to depend on the limiting vector but not on \(r\);
4. any scale selector is defined by carrier-appropriate ledgers independent of the selected certificate;
5. the Euclidean forms, vacua, and observable nets converge along the declared net to the single law \(\omega_{\infty,G}\); in the complete-angle branch the transfer semigroups or forms converge in a mode that preserves the uniform lower spectral bound, such as strong-resolvent or Mosco convergence under the stated identifications; in the dense-local-family branch the reflected-translated diagonal correlations converge for every \(F_{\psi,r}\), and all blocking or observable maps used there are compatible with reflection and physical time translation;
6. the full Osterwalder--Schrader hypotheses—reflection positivity together with the required Euclidean covariance, translations, continuity, regularity, and clustering data—hold for \(\omega_{\infty,G}\) and reconstruct the local QFT clock, Poincare covariance, and spectrum condition; and
7. the limiting theory has the short-distance and gauge-invariant observable content required of Yang--Mills.

The first three clauses are the proposed new explanatory mechanism. The last four are what prevent it from becoming a relabeling of the gap.

The analytic search can stop when, along the single directed family whose relevant Schwinger functions converge to \(\omega_{\infty,G}\), it returns either

$$
\boxed{
\begin{gathered}
n_ra_{\tau,r}\longrightarrow\ell_*>0,\\
\displaystyle
\limsup_{r\to\infty}
\left\|K_{r,G}Q_{r,G}\right\|
\leq\rho_*<1
\end{gathered}}
\tag{GR21a}
$$

or

$$
\boxed{
\begin{gathered}
\exists\,\sigma_*>0,\quad
\mathcal D_{\mathrm{loc},G}\subset Q_{\infty,G}\mathcal H_{\infty,G},\quad
\overline{\operatorname{span}\mathcal D_{\mathrm{loc},G}}
=Q_{\infty,G}\mathcal H_{\infty,G},\\[2mm]
\forall\psi\in\mathcal D_{\mathrm{loc},G}\ \exists C_\psi<\infty,\ s_\psi<\infty:\quad
0\leq
\langle\psi,e^{-sA_{\infty,G}}\psi\rangle
\leq C_\psi e^{-\sigma_*s}
\quad(s\geq s_\psi)
\end{gathered}}
\tag{GR21b}
$$

where \(\ell_*\) is selected independently of the desired low spectrum, and \(A_{\infty,G}=(H_{\infty,G}-E_{0,\infty,G})/(\hbar c)\), \(P_{0,\infty,G}=\mathbf1_{\{0\}}(A_{\infty,G})\), and \(Q_{\infty,G}=I-P_{0,\infty,G}\) are reconstructed from that same limiting law. The first certificate controls the complete Perron-dressed nonlinear Wilson response and reaches the limit through its transfer comparison. The second controls an OS-total local family directly after the quotient; its regulator-level proof must supply the coherent families and uniform prefactors required in clauses 2--5. Neither is presently known along the four-dimensional asymptotically free trajectory. Until one of them is proved together with the full reconstruction contract, Global--Local Response Reconstruction is a precise theorem programme, not a solution of the Yang--Mills existence and mass-gap problem.
