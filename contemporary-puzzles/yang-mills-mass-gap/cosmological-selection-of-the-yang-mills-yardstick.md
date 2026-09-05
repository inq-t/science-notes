# Cosmological Selection of the Yang--Mills Yardstick

Cosmology can enter the mass-gap problem without being asked to manufacture local coercivity. The clean factorization is that Yang--Mills geometry must prove a positive dimensionless gap coefficient after its gauge data and scale convention are fixed, while a whole-cosmos boundary condition may select which dimensional member of the scale-covariant Yang--Mills family is physically realized. On the repository's common-count branch, the proposed yardstick has an exact conditional whole-to-part presentation: the candidate energy is the apparent-horizon energy divided by the two-thirds power of its dimensionless information capacity. Composing that scale with Longo's finite-width relative-entropy bound yields a precise conditional Hamiltonian-gap inequality and exposes the remaining width, fossilization, and decoupling obligations.

**Status: [EXACT DIMENSIONAL CLASSIFICATION] for the allowed combinations of the declared inputs; [EXACT CONDITIONAL IDENTITIES] after the Einstein--FLRW horizon ledger and common-count law are assumed; [EXACT CONDITIONAL LOCALIZED ENERGY-GAP THEOREM] after a positive-energy wedge-dual local net, localized differentiable paths, a positive Hermitian loss form on a complex \(H^{1/2}\)-form core, a localization-width map, and a regional descent-frame bound are supplied; [CONJECTURE] for cosmological selection of the Yang--Mills scale; [OPEN] for the selector, width map, fossil transport, neutral coercivity, Poincare reconstruction, continuum and infinite-volume limits, and gravity-decoupled pure-Yang--Mills construction.**

## Existence of a gap and selection of its scale are different theorems

Fix the compact simple gauge group, its global form and topological-angle data, and a renormalization-scale convention \(\mathsf s\). Let \(H_\Lambda\geq0\) denote the reconstructed physical Hamiltonian for the member \(\Lambda_{\mathrm{YM}}^{(\mathsf s)}\), and put \(P_0:=E_{H_\Lambda}(\{0\})\). A four-dimensional pure Yang--Mills result naturally separates into

\[
H_\Lambda(1-P_0)
\geq
\underline C_{\mathrm{YM}}^{(\mathsf s)}
\Lambda_{\mathrm{YM}}^{(\mathsf s)}
(1-P_0),
\qquad
\underline C_{\mathrm{YM}}^{(\mathsf s)}>0,
\tag{CY1}
\]

and a selection law

\[
\mathfrak S_{\mathrm{cos}}(\text{whole-cosmos data})
=
\Lambda_{\mathrm{realized}}^{(\mathsf s)}.
\tag{CY2}
\]

Equation (CY1) is the scale-free analytic problem: prove a positive dimensionless lower-bound coefficient on the physical vacuum complement, uniformly through infinite volume and continuum removal. The underline distinguishes this prospective coercivity constant from the exact ratio \(\Delta_E/\Lambda_{\mathrm{YM}}\), whose use inside a gap proof would be circular. The coefficient is not scheme-independent by itself; changing the definition of \(\Lambda_{\mathrm{YM}}\) changes its reciprocal normalization. Equation (CY2) is a boundary-condition or calibration problem: select one member of the fixed-convention one-scale family in physical units. A cosmological law can contribute to (CY2) without replacing (CY1), but it must also supply any scheme conversion without consulting the target spectrum. Conversely, a number in MeV does not establish (CY1).

This factorization is the Copernican opening. The local theory need not contain its own absolute normalization as an isolated object. The whole may select a member while the part supplies a positive dimensionless response in the fixed convention. But the two arrows must be constructed independently; otherwise a measured glueball mass can be hidden inside the alleged selector.

## Dimensional classification of the cosmic inputs

Let \(H>0\) be a selected Hubble rate and define

\[
\alpha_H:=\frac{G\hbar H^2}{c^5},
\qquad
\epsilon:=-\frac{\dot H}{H^2}
=1-\frac{\ddot a}{aH^2}
=1+q.
\tag{CY3}
\]

With \(c,G,\hbar,H\) as the dimensional inputs, Buckingham dimensional analysis implies that every scalar energy made from these quantities and dimensionless cosmographic data has the form

\[
E=\hbar H\,
F\!\left(
\alpha_H,
\epsilon,
\frac{\mathrm d\epsilon}{\mathrm dN},
Ht,
N-N_*,
\ldots
\right),
\qquad
N:=\log\frac a{a_*}.
\tag{CY4}
\]

Equivalently one may use the cosmic energy unit \(c^5/(GH)\), because it differs from \(\hbar H\) by the dimensionless number \(1/\alpha_H\). Integers, logarithms, Misner scale-age \(\Omega=-N\), deceleration, jerk, and higher normalized derivatives can determine the dimensionless function \(F\) or select the event at which it is evaluated. They do not create a unit.

Boltzmann's constant behaves similarly. A separately supplied temperature gives an energy \(k_BT\), but the canonical apparent-horizon assignment

\[
k_BT_A=\frac{\hbar H}{2\pi}
\tag{CY5}
\]

only repackages the Hubble quantum. The dimensionless entropy \(S_A/k_B\) can carry enormous structural information; \(k_B\) itself only converts that count into thermodynamic units.

There is a strict dimensional no-go behind this statement. From \(c,G,k_B\) and pure natural numbers or logarithms alone, no scalar of dimension inverse time—and no mass or energy—can be formed: removing the temperature dimension forces the power of \(k_B\) to vanish, after which the remaining mass and length equations exclude those targets. The combination \(c^5/G\) is a power, not a clock rate. One must additionally supply \(\hbar\), an independently normalized temperature, a duration, an energy, or an equivalent dimensional geometric density. Thus logarithmic structure may select a number, but it cannot silently become seconds.

If \(\hbar\) is deliberately withheld but \(c,G,H\) and an independently constructed dimensionless capacity \(\iota\) are allowed, the classification is instead

\[
E=\frac{c^5}{GH}\,
\widetilde F(\iota,\epsilon,Ht,N,\ldots).
\tag{CY5a}
\]

Thus those inputs do contain an energy unit, but it is the whole-cosmos unit. Producing a microscopic value requires a principled small dimensionless factor. The whole-capacity presentation below supplies precisely such a candidate, \(\widetilde F\propto\iota^{-2/3}\). Calling \(\iota\) the Bekenstein--Hawking capacity would reintroduce \(\hbar\); treating it as a primitive algebraic count would create a new theorem obligation instead.

For monomial members of (CY4),

\[
E_p:=\hbar H\,\alpha_H^{-p}
=E_P^{2p}(\hbar H)^{1-2p},
\qquad
E_P:=\sqrt{\frac{\hbar c^5}{G}}.
\tag{CY6}
\]

Dimensional analysis leaves \(p\) free. Geometry or algebra must select it.

## Common count selects the one-third member

At a distinguished cosmic cut, set

\[
R_c:=\frac c{H_c},
\qquad
\ell_P^2:=\frac{\hbar G}{c^3},
\qquad
\iota_c:=\frac{S_c}{k_B}
=\frac{\pi R_c^2}{\ell_P^2}.
\tag{CY7}
\]

The declared common-count law in [[causal-grain-cosmology/inq|causal-grain cosmology]] is

\[
\lambda_*^3
=
\frac{4\gamma s_*}{3}\ell_P^2R_c,
\tag{CY8}
\]

where \(s_*\) is the information per effective bulk cell and \(\gamma\) is the wall-to-area multiplicity. Equation (CY8) is not dimensional analysis: it follows only after equating the declared bulk-cell and boundary-capacity ledgers. It selects \(p=1/3\). With

\[
E_*:=\frac{\hbar c}{\lambda_*},
\qquad
m_*:=\frac{E_*}{c^2},
\tag{CY9}
\]

one obtains

\[
\boxed{
E_*^3
=
\frac{3}{4\gamma s_*}
\frac{\hbar^2c^5H_c}{G},
\qquad
m_*^3
=
\frac{3}{4\gamma s_*}
\frac{\hbar^2H_c}{Gc}.}
\tag{CY10}
\]

The canonical branch \((\gamma,s_*)=(2,1)\) gives the coefficient \(3/8\).

There is direct but split prior art for this dimensional cubic class. [[library/the-qcd-mass-gap-and-quark-deconfinement-scales-as-mass-bounds-in-strong-gravity/inq|Burikham, Harko, and Lake]] review an ordinary de Sitter minimum-length/cell-count scale \((\ell_P^2\ell_{\mathrm{dS}})^{1/3}\) and its associated mass \((\hbar^2\sqrt\Lambda/G)^{1/3}\). They then construct the distinct strong-gravity analogue \((\ell_{\mathrm{sP}}^2\ell_{\mathrm{sd}})^{1/3}\) by substituting a strong coupling and strong cosmological constant, alongside a separate static Buchdahl-bound route. This establishes provenance for the geometric-mean scaling, not support for the present carrier. Their strong-gravity model explicitly does not reproduce \(SU(3)\) color interactions, and its mass-generation mechanism assumes the glueball mass entering the mixing term a priori. The authors themselves state that this does not solve the mass-gap problem explicitly.

## The whole-to-part energy identity

The flat Einstein--FLRW apparent-horizon ledger in [[cosmic-geon-hypothesis-and-horizon-rate-ledger]] gives

\[
E_{A,c}
=
\frac{c^5}{2GH_c},
\qquad
M_{A,c}:=\frac{E_{A,c}}{c^2},
\qquad
\iota_c
=
\frac{\pi c^5}{G\hbar H_c^2}.
\tag{CY11}
\]

Substitution in (CY10) yields the exact equivalent presentation

\[
\boxed{
E_*
=
\left(\frac{6\pi^2}{\gamma s_*}\right)^{1/3}
E_{A,c}\,\iota_c^{-2/3},
\qquad
m_*
=
\left(\frac{6\pi^2}{\gamma s_*}\right)^{1/3}
M_{A,c}\,\iota_c^{-2/3}.}
\tag{CY12}
\]

On the canonical branch this coefficient is \((3\pi^2)^{1/3}\). Equation (CY12) is the sharpest current form of the Copernican proposal. It does not insert a small object into a large container. It algebraically rewrites the candidate inverse-length energy scale using one whole energy and one dimensionless whole capacity. The exponent \(2/3\) is not fitted: it is the algebraic shadow of converting an areal count into a three-volume cell relation. Locality enters only if the width map below is constructed. Within the declared Einstein--FLRW area ledger, however, \(E_A\) and \(\iota_A\) are not independent measurements: both are presentations of the same \(H\). Thus (CY12) is a strong retyping identity, not extra empirical information and not by itself a dynamical gap.

The same identity has a logarithmic rate presentation. Define

\[
Q_c:=\frac{R_c}{\lambda_*}
=\frac{E_*}{\hbar H_c},
\qquad
\Sigma_c:=\log Q_c.
\tag{CY13}
\]

Then

\[
\boxed{
Q_c
=
\left(
\frac{3\iota_c}{4\gamma s_*\pi}
\right)^{1/3},
\qquad
\Sigma_c
=
\frac13\log
\left(
\frac{3\iota_c}{4\gamma s_*\pi}
\right),
\qquad
E_*=\hbar H_c e^{\Sigma_c}.}
\tag{CY14}
\]

Thus \(\Sigma_c\) is a logarithmic scale count in nats. Misner time \(\Omega=-\log(a/a_*)\) may label the cut through a separately supplied relation \(H(\Omega)\), but it is a different scale ratio; identifying a Misner interval with \(\Sigma_c\) requires a dynamical map. The logarithm is meaningful because multiplicative scale ratios compose additively. It is not itself a clock frequency.

Writing \(\omega_{*,c}:=E_*/\hbar=c/\lambda_*\) shows what the dimensionless number measures:

\[
\boxed{
Q_c
=
\frac{\omega_{*,c}}{H_c},
\qquad
Q_c^3
=
\frac{3}{4\pi\gamma s_*}\frac{S_{A,c}}{k_B}.}
\tag{CY14a}
\]

Equivalently, define the dimensionless whole-to-local incidence scalar for any mass presentation \(m\),

\[
\Xi_m(t)
:=
\frac{1}{\iota_A(t)}
\left(
\frac{mc^2}{\hbar H(t)}
\right)^3
=
\frac{Gcm^3}{\pi\hbar^2H(t)}.
\tag{CY14b}
\]

The common-count relation is exactly the selected-cut condition

\[
\boxed{
\Xi_{m_*}(t_c)
=
\frac{3}{4\pi\gamma s_*}.}
\tag{CY14c}
\]

This is a more invariant statement of “mass is a rate.” The mass phase rate \(\omega_m=mc^2/\hbar\) is not equated with the Hubble rate; their cubed ratio is compared with the dimensionless capacity of the whole causal patch. The cube is the volume-cell incidence in three spatial dimensions, while \(S_A/k_B\) is the areal whole-capacity ledger. Thus (CY14c) is a global--local quotient, not an equation of units. It is still conditional on the common-count and Einstein--Bekenstein--Hawking premises, and it does not construct the categorical or Yang--Mills operator whose mass is being presented.

It is therefore a whole-to-local **rate-separation number**: the candidate microscopic angular rate divided by the cosmic logarithmic scale rate is the cube root of a dimensionless horizon capacity, up to the declared cell coefficient. Only after a clock-synchronization map places a local phase \(\theta_*\) and the cosmic scale coordinate on one time carrier, with \(\dot\theta_*=\omega_*\) and \(\dot N=H\), may one conclude \(\left.\mathrm d\theta_*/\mathrm dN\right|_c=Q_c\); then \(Q_c/(2\pi)\) counts ordinary cycles per e-fold at the cut. Before that solder, (CY14a) is a formal scalar rate presentation. It is not yet a geon quality factor. That stronger name would require a same-carrier theorem identifying \(-\mathrm d\log E_{\gamma,\mathrm{com}}/\mathrm dt=H\) as the loss law of the very whole mode whose retained presentation oscillates at \(\omega_*\). At present those two rates live on different carriers. [[internal-yardstick-as-a-generalized-rate-edge]] states the corresponding operator problem: calibrate a rate pencil on the physical tangent carrier by this cosmic scalar and, if a distinct global carrier is claimed, construct the comparison map rather than assuming it.

## Normalized acceleration can select a cut; it adds no independent unit

For the same apparent-horizon ledger,

\[
P_A=\epsilon\frac{c^5}{G},
\qquad
\frac{P_A}{E_A}
=
\frac{\mathrm d}{\mathrm dt}\log\iota_A
=2\epsilon H,
\qquad
\dot E_A=\frac{P_A}{2}.
\tag{CY15}
\]

For \(\epsilon_c\neq0\), the canonical common-count energy therefore also obeys

\[
\boxed{
E_*^3
=
\frac{3}{8\epsilon_c}\hbar^2H_cP_{A,c}.}
\tag{CY16}
\]

At the separately declared equal-partition cut \(\epsilon_c=3/4\), this becomes \(E_*^3=\hbar^2H_cP_{A,c}/2\). At \(\epsilon_c=0\), (CY16) is not a valid quotient even though the unreduced common-count formula (CY10) remains regular. Equation (CY16) is a genuine energy-from-rates identity, but it is still a recombination of Einstein--FLRW, horizon thermodynamics, and common count. It does not prove that the Yang--Mills vacuum realizes that scale.

Raw acceleration \(\ddot a/a\) has dimension \(T^{-2}\), but in this ledger it is \(H^2(1-\epsilon)\); once \(H\) is present it adds no independent dimensional generator. Normalized acceleration, inflationary e-folds, or a condition on entropy growth can nevertheless perform one essential job: select the cut.

There are actually two different selection problems. Under the dilation of whole solutions

\[
H(N)\longmapsto\mu H(N),
\qquad
t-t_*\longmapsto\mu^{-1}(t-t_*),
\tag{CY17a}
\]

the shape data \(\epsilon\), its \(N\)-derivatives, \(N-N_*\), and \(H(t-t_*)\) are invariant, whereas \(\iota_A\mapsto\mu^{-2}\iota_A\). Hence a shape equation can select an event,

\[
\mathcal C_{\mathrm{shape}}\!\left(
\epsilon,
\frac{\mathrm d\epsilon}{\mathrm dN},
N-N_*,
\ldots
\right)=0
\quad\Longrightarrow\quad
N=N_c,
\tag{CY17b}
\]

but it cannot fix the dilation normalization. A second equation containing an independently normalized absolute capacity can do so. If \(\mathfrak d_{\mathrm{alg}}\) denotes natural-number, index, or logarithmic data constructed by the global algebra, then the required type is

\[
\mathcal C_{\mathrm{norm}}(\iota_c;\mathfrak d_{\mathrm{alg}})=0
\quad\Longrightarrow\quad
\iota_c,
\qquad
H_c
=
\left(
\frac{\pi c^5}{G\hbar\iota_c}
\right)^{1/2}.
\tag{CY17c}
\]

Both selector equations must have unique stable solutions and must be derived without inspecting the target mass. Their logarithmic and temporal arguments must also be invariant under \(N\mapsto N+\beta\) and \(t\mapsto t+t_0\), unless the global construction itself distinguishes the reference event.

There is a particularly sharp equivalent target. If the global algebra selects \(\Sigma_c=\log(R_c/\lambda_*)\), then (CY13)--(CY14) force

\[
\boxed{
\iota_c
=
\frac{4\gamma s_*\pi}{3}e^{3\Sigma_c},
\qquad
H_c
=
\left(
\frac{3c^5}{4\gamma s_*G\hbar}
\right)^{1/2}
e^{-3\Sigma_c/2},
\qquad
E_*
=
\left(
\frac{3}{4\gamma s_*}
\right)^{1/2}
E_Pe^{-\Sigma_c/2}.}
\tag{CY17d}
\]

This is the clean internal-yardstick challenge: derive one normalization-sensitive logarithmic depth or capacity from an operator, index, or valuation. Given the stated \(c,G,\hbar\) and common-count premises, the absolute cosmic rate and candidate microscopic energy then follow. It is the normalization-first reversal already isolated in [[the-grain-of-causal-scale/inbox/causal-grain-and-the-yang-mills-gap/the-yardstick-is-a-rate]]. It remains conditional on the Einstein area/action solder; the later \(\hbar\) firewall still applies.

[[two-sided-index-capacity-and-the-cosmic-weld]] now fixes one algebraic candidate without fixing its cosmological realization. For a finite-index expectation between infinite-dimensional factors, the log index is exactly a supremal Araki relative-entropy loss and a two-sided expectation/commutant certainty budget. A standard sector realized over infinite-dimensional factors makes this \(2\log d(X)\), additive under fusion. Directly matching that additive quantity to \(\iota_A=S_A/k_B\) gives \(\iota_n-\iota_b=2n\log d\), not a geometric Hubble ladder. The stronger law \(\iota_n/\iota_b=d^{2n}\) instead treats the categorical index as a multiplier of effective horizon cells under an additional area-cell interpretation. Only that independent effective-cell-count weld gives \(H_n/H_b=d^{-n}\). The choice between these maps is part of \(\mathcal C_{\mathrm{norm}}\), not a theorem of subfactor theory.

[[quantum-g2-categorical-rigidity-and-the-carrier-firewall]] now supplies a nontrivial test of this architecture. For the fundamental object \(X\) in the quantum-\(G_2\) category, \(d_q(X)=1+2\cosh(2\eta)+2\cosh(8\eta)+2\cosh(10\eta)\), with \(\eta=\log q\), while categorical property \((T)\) gives a genuinely positive dimensionless rigidity edge for \(q\neq1\). On the explicitly conjectural multiplicative branch, \(\mathscr D_c=2n\log d_q(X)\) therefore determines \(|\eta|\) monotonically. The undeformed threshold is sharp: \(\mathscr D_c=2n\log7\) selects \(q=1\), where the capacity is positive but the categorical edge is zero; a strictly larger depth selects \(q\neq1\). Adding the separate proposed one-channel birth section turns the two existing crossing-rate anchors into the post-search ceiling \(n_{\max}=72\), with \(q\simeq1.017\)--\(1.018\) at that ceiling. This is an operator-informed selection diagnostic, not yet a physical result: the weld, fusion depth, and exceptional-to-Yang--Mills carrier map remain unconstructed, and the repeated number seventy-two cannot identify tensor depth with normal-representation multiplicity.

The strongest whole-history candidate already latent in the workspace makes the missing selector more concrete. Using the indexed-wall note's decay and capacity characters \(\nu\) and \(\chi\), declare a unit-ledger birth boundary and a transverse algebraic crossing,

\[
\mathcal C_{\mathrm{birth}}:
\iota_b=1,
\qquad
\delta_{\mathrm{wall}}(s)
:=2\nu(s)-\chi(s),
\qquad
\delta_{\mathrm{wall}}(s_c)=0,
\qquad
\left.\frac{\mathrm d\delta_{\mathrm{wall}}}{\mathrm ds}\right|_{s_c}\neq0,
\qquad
\mathfrak y(s_c)=N_c.
\tag{CY17e}
\]

The first is a boundary condition, not a theorem from a trivial inclusion: index one has zero logarithmic index entropy, and writing one nat requires the separate unit channel-weight solder \(s_*=1\). The wall equation is the spectrum-independent event prototype in [[causal-grain-as-a-mass-engagement-fossil]], while \(\mathfrak y\) denotes the still-unconstructed synchronization from its pre-clock cut to a cosmological e-fold address. Transversality is unoriented as written; an oriented index jump would require a sign choice on the two sides. If the whole dynamics independently returns \(\epsilon(N)\), then the exact mint law summarized in [[minimal-cosmodynamic-closure/inq|minimal cosmodynamic closure]] gives

\[
\boxed{
\mathscr D_c
:=
\log\frac{\iota_c}{\iota_b}
=
2\int_{N_b}^{N_c}\epsilon(N)\,\mathrm dN,
\qquad
H_c
=
\left(\frac{\pi c^5}{G\hbar}\right)^{1/2}
e^{-\mathscr D_c/2},
\qquad
\Sigma_c
=
\frac13\left[
\mathscr D_c+\log\frac{3}{4\gamma s_*\pi}
\right].}
\tag{CY17f}
\]

This is the clearest present stopping condition: derive both boundary sections and the finite dimensionless ledger depth \(\mathscr D_c\) from whole-cosmos dynamics. The current numerical depth and e-fold history use a CMB-conditioned background, so they only reconstruct \(H_c^{-2}\); they do not predict it.

The signed normalized Hubble-loss parameter integrates a depth, not a duration. With

\[
I_{bc}:=\int_{N_b}^{N_c}\epsilon(N)\,\mathrm dN,
\]

the flat Einstein--FLRW ledger gives

\[
\boxed{
I_{bc}
=
\log\frac{H_b}{H_c}
=
\frac12\log\frac{\iota_c}{\iota_b},
\qquad
Q_c
=
\left(\frac{3\iota_b}{4\pi\gamma s_*}\right)^{1/3}
e^{2I_{bc}/3}.}
\tag{CY17g}
\]

Here \(\epsilon=-\mathrm d\log H/\mathrm dN\); it is a signed normalized Hubble-loss parameter, not raw acceleration, and accelerated expansion corresponds to \(\epsilon<1\), not necessarily to negative \(\epsilon\). Equation (CY17g) says that the whole history accumulates logarithmic separation between the cosmic rate and the candidate retained rate. It still leaves the overall dilation normalization of the history unfixed until the birth capacity or another dimensional datum is supplied.

An independently calibrated proper age can supply that missing datum, but only in a sharply delimited sense. Given a shape \(\epsilon(N)\) and endpoints selected without using the age, define

\[
I(N):=\int_{N_b}^{N}\epsilon(u)\,\mathrm du,
\qquad
J_{bc}:=\int_{N_b}^{N_c}e^{I(N)}\,\mathrm dN.
\]

Since \(H(N)=H_b e^{-I(N)}\), a genuinely independent elapsed proper duration \(\Delta\tau_{bc}\) gives

\[
\boxed{
H_b=\frac{J_{bc}}{\Delta\tau_{bc}},
\qquad
H_c=\frac{J_{bc}}{\Delta\tau_{bc}}e^{-I_{bc}},
\qquad
\omega_{*,c}=Q_cH_c.}
\tag{CY17h}
\]

This is an exact age-calibration lemma, not automatically an internal derivation. If \(\Delta\tau_{bc}\) was reconstructed from the already normalized \(H(N)\), solving (CY17h) backward is circular. A stellar, atomic, acoustic, or background-inferred age must also be checked for dependence on the local mass scale being predicted. Misner time, e-fold number, \(H\Delta\tau\), and any other dilation-invariant age coordinate select shape but cannot fix the normalization. A theory that constructs its own clock and proper-duration unit would turn (CY17h) into an internal selector; an observed age makes it an empirical calibration.

This has not yet occurred for the displayed numerical grain. Its \(H_c=83.1058\,\mathrm{km\,s^{-1}\,Mpc^{-1}}\) is a fixed-physical-density, CMB-distance-conditioned input, and the existing equal-partition or CST redshift labels determine at most a shape-selected event, not the absolute dilation normalization. An internal yardstick theorem must construct (CY17c), (CY17d), or the two-boundary realization (CY17e)--(CY17f) without reusing the mass or acoustic datum under test.

## A live scale fails; a transported fossil is required

If (CY10) is evaluated at the current \(H(N)\) while \(G,c,\hbar,\gamma,s_*\) remain fixed, then

\[
\frac{\mathrm d}{\mathrm dN}\log E_*
=
-\frac{\epsilon}{3}.
\tag{CY18}
\]

The three rates relevant to the geon analogy can therefore be placed on one typed ledger:

\[
-\frac{\mathrm d}{\mathrm dt}
\log E_{\gamma,\mathrm{com}}
=H,
\qquad
\frac{\mathrm d}{\mathrm dt}\log\iota_A
=2\epsilon H,
\qquad
\frac{\mathrm d}{\mathrm dt}\log E_*
=-\frac{\epsilon H}{3}.
\tag{CY18a}
\]

The corresponding drift of the incidence scalar is

\[
\boxed{
\frac{\mathrm d}{\mathrm dt}\log\Xi_m
=
3\frac{\dot m}{m}
+\epsilon H.}
\tag{CY18b}
\]

For fixed local mass, \(\Xi_m\) is constant only on an exact de Sitter branch with \(\epsilon=0\). Holding the common-count incidence law fixed throughout a generic history instead forces \(\dot m/m=-\epsilon H/3\), reproducing (CY18). This turns the fossil requirement into a dimensionless null test: the relation may select one cut and then be transported, but it cannot be imposed as a live identity while ordinary masses remain constant.

The first equality in (CY18a) is radiation redshift in a fixed comoving cell, not literal flux through the apparent horizon; the second is growth of the area-law capacity, not automatically thermodynamic entropy production; and the third holds only for the rejected live-cut identification.

Ordinary local masses would drift with the expansion. The viable proposal is therefore not a live relation \(m=m(H(t))\). It requires a carrier transition at a distinguished cut and a transport law preserving the selected scale downstream:

\[
\text{whole-cosmos data at the selected cut}
\xrightarrow{\ \mathfrak S_{\mathrm{cos}}\ }
\Lambda_*
\xrightarrow{\ \text{fossil transport}\ }
\Lambda_{\mathrm{realized}}=\Lambda_*.
\tag{CY19}
\]

The second arrow is substantive. An index can remain constant under a Fredholm deformation, but an integer alone does not preserve a dimensional normalization. [[causal-grain-as-a-mass-engagement-fossil]] states the required wall-crossing and observable-survival tests.

## Longo converts the selected width into a physical gap

[[localized-relative-entropy-and-the-energy-solder]] supplies an established downstream energy comparison under explicit carrier hypotheses. Let \((\mathcal A,U,\Omega)\) be a wedge-dual positive-energy translation-covariant local net, let \(H\) generate its time translations, and let \(B\) be a region of width \(2R_B\). For bounded self-adjoint local observables, take \(U_s=e^{isA}\), \(\psi_A=(1-P_0)A\Omega\), and suppose the same paths are twice differentiable for the relevant Araki entropies and in the \(H^{1/2}\)-form norm. Longo and monotonicity then bound the real restriction-loss half-Hessian. To infer a spectral gap, assume additionally that it has a positive Hermitian extension \(\widehat q_{\mathrm{loss},B}\) to a complex \(H^{1/2}\)-form core \(\mathcal D_{B,\mathbb C}\), with

\[
\varkappa_B\|\psi\|^2
\leq
\widehat q_{\mathrm{loss},B}[\psi]
\leq
\frac{2\pi R_B}{\hbar c}
\|H^{1/2}\psi\|^2,
\qquad
\psi\in\mathcal D_{B,\mathbb C},
\qquad
\varkappa_B>0.
\tag{CY20}
\]

The complex upper comparison is not automatic merely because the real tangents span a core; it requires a directly constructed Hermitian form or a compatible conjugation commuting with \(H\). Closing the two forms now implies

\[
\Delta_E
\geq
\frac{\hbar c}{2\pi R_B}\varkappa_B.
\tag{CY21}
\]

Use \(\varkappa_B\), not \(k_B\), for the dimensionless descent stiffness. The symbols belong to different types.

The missing whole-to-local width solder is a natural map

\[
\mathfrak W:
\lambda_{\mathrm{common\ count}}
\longmapsto
R_{\mathrm{localization}}.
\tag{CY22}
\]

If this map proves \(R_B=\alpha\lambda_*\) for a dimensionless geometrically fixed \(\alpha>0\), then (CY21) becomes

\[
\boxed{
\Delta_E
\geq
\frac{\varkappa_B}{2\pi\alpha}
\left(\frac{3}{4\gamma s_*}\right)^{1/3}
\left(\frac{\hbar^2c^5H_c}{G}\right)^{1/3}.}
\tag{CY23}
\]

Equivalently,

\[
\Delta_E
\geq
\frac{\varkappa_B}{2\pi\alpha}
\left(\frac{6\pi^2}{\gamma s_*}\right)^{1/3}
E_{A,c}\iota_c^{-2/3}.
\tag{CY24}
\]

This is the first precise composition of the cosmic common-count yardstick with an established local QFT energy solder. It remains conditional twice: (CY8) has not been shown to be a localization or correlation length, and (CY20) has not been proved for the neutral Yang--Mills vacuum complement.

## The isotropic cell fixes the width coefficient conditionally

Common count declares an effective cell *volume*, not a radius. There is nevertheless one canonical width if an additional physical premise is true: suppose \(\gamma s_*>0\) and each effective cell is realized as the causal envelope of a centered, convex, rotationally invariant spatial localization domain with volume \(\lambda_*^3\). Its spatial base must then be a three-ball, and its Longo half-width is the ball radius:

\[
\frac{4\pi}{3}R_B^3=\lambda_*^3,
\qquad
R_B=\left(\frac{3}{4\pi}\right)^{1/3}\lambda_*.
\tag{CY24a}
\]

This supplies

\[
\alpha_{\mathrm{ball}}
=
\left(\frac{3}{4\pi}\right)^{1/3}
\tag{CY24b}
\]

without fitting a mass. Inserting it into (CY24) cancels every sphere and modular \(2\pi\) coefficient:

\[
\boxed{
\Delta_E
\geq
\varkappa_B(\gamma s_*)^{-1/3}
E_{A,c}\iota_c^{-2/3}.}
\tag{CY24c}
\]

The cancellation has a dimensionally general form. Let the integer \(d\geq2\), let \(D=d+1\), and consider spatially flat Einstein--FLRW slices. Let \(\omega_d\) be the Euclidean volume of the unit \(d\)-ball and use the standard Friedmann/Misner--Sharp apparent-horizon energy normalization

\[
\ell_{P,D}^{\,d-1}:=\frac{\hbar G_D}{c^3},
\qquad
R_A:=\frac cH,
\qquad
\rho_{\mathrm{crit}}^{(E)}
:=
\frac{d(d-1)}{16\pi}
\frac{c^2H^2}{G_D},
\qquad
E_A:=\rho_{\mathrm{crit}}^{(E)}\omega_dR_A^d
=
\frac{d(d-1)\omega_d}{16\pi}
\frac{c^{d+2}}{G_DH^{d-2}}.
\tag{CY24c0}
\]

Assume the corresponding \(D\)-dimensional Einstein area law, apparent-horizon identity, common-count law with \(\gamma s_*>0\), and finite-width entropy bound. Realize one cell as the causal envelope of the equal-volume spatial \(d\)-ball, so the half-width is its radius. Then

\[
\iota_A
=
\frac{d\omega_d}{4}
\left(\frac{R_A}{\ell_{P,D}}\right)^{d-1},
\qquad
\lambda_d^d
=
\frac{4\gamma s_*}{d}
\ell_{P,D}^{\,d-1}R_A,
\qquad
\left(\frac{R_A}{\lambda_d}\right)^d
=
\frac{\iota_A}{\gamma s_*\omega_d}.
\tag{CY24d}
\]

The horizon conversion

\[
\frac{\hbar H}{2\pi}\iota_A
=
\frac{2}{d-1}E_A
\tag{CY24e}
\]

and the equal-volume ball width \(R_B=\omega_d^{-1/d}\lambda_d\) give

\[
\boxed{
\Delta_E
\geq
\frac{2\varkappa_B}{d-1}
(\gamma s_*)^{-1/d}
E_A\iota_A^{-(d-1)/d}.}
\tag{CY24f}
\]

At \(d=3\), the prefactor \(2/(d-1)\) is exactly one and (CY24f) reduces to (CY24c). This is a genuine dimension-three normalization cancellation. It is not yet a selection theorem for three dimensions: \(d\), rotational cell geometry, the Einstein area law, and the identification of the effective cell with a QFT localization domain were all assumed. Knot topology has not entered the proof. The result instead isolates a sharp target: derive those premises from one whole-to-local construction and determine whether the cancellation survives without inserting \(d=3\) upstream.

The numerical \(6^2=36\) clue belongs entirely inside the unknown dimensionless product. If one sets \(R_B=\lambda_*\), certifying the lower bound \(\Delta_E\geq36E_*\) would require

\[
\frac{\varkappa_B}{2\pi}=36.
\tag{CY25}
\]

Under the isotropic-ball hypothesis, the same lower-bound claim instead requires

\[
\varkappa_B
=
\frac{72\pi}{(4\pi/3)^{1/3}}.
\tag{CY25a}
\]

Either coefficient must be derived from the normalized regional frame; the integer cannot be attached after looking at a glueball mass. A different width convention merely moves the obligation into \(\alpha\). To conclude the equality \(\Delta_E=36E_*\) would additionally require sharpness and saturation of both the regional lower-frame estimate and Longo's upper comparison.

## The \(\hbar\) firewall

Equation (CY12) can be written without an explicit \(\hbar\) if \(E_A\) and the dimensionless capacity \(\iota_A\) are independently primitive. But using the Bekenstein--Hawking identity in (CY11) has already inserted \(\hbar\). Therefore there are only two honest routes:

1. Treat \(\hbar\) as the established action-to-phase solder of the recovered local quantum theory. Then (CY10)--(CY24) are legitimate downstream physical identities, but not a pre-quantum derivation of action.
2. Construct \(\iota_A\) as an independent algebraic count and derive the action solder later. Then (CY12) may guide the pre-clock theory, but its equality to the Einstein area entropy and its conversion to MeV remain separate theorems.

Boltzmann's constant does not remove this fork. It converts entropy to a dimensionless count; it does not provide an action unit.

## The pure-Yang--Mills decoupling fork

The direct live formula has no path-independent gravity-free limit:

\[
E_*\propto\left(\frac{H_c}{G}\right)^{1/3}.
\tag{CY26}
\]

At fixed \(H_c\), \(G\to0\) sends it to infinity; at fixed \(G\), \(H_c\to0\) sends it to zero. Correlating the limits supplies extra physics. Consequently, a theory in which gravity or expansion is required for the *existence* of the positive gap is not yet a solution of the pure-Yang--Mills problem on Minkowski space.

The Clay-compatible route is instead

\[
\boxed{
\Delta_E
\geq
\underline C_{\mathrm{YM}}^{(\mathsf s)}
\Lambda_{\mathrm{YM}}^{(\mathsf s)},
\qquad
\underline C_{\mathrm{YM}}^{(\mathsf s)}>0
\ \text{proved without }G,H,
\qquad
\Lambda_{\mathrm{YM}}^{(\mathsf s)}
=C_{\mathrm{cos}}^{(\mathsf s)}E_*,
\qquad
C_{\mathrm{cos}}^{(\mathsf s)}>0}
\tag{CY27}
\]

with \(C_{\mathrm{cos}}^{(\mathsf s)}\) and every scheme conversion fixed independently of the target spectrum. Equality may be studied later as a sharpness problem; it is not needed for gap existence. Cosmology then selects the realized renormalization member; it does not create the local lower-frame theorem. A stronger gravity-coupled account must construct a reducing pure-gauge carrier or a controlled decoupling limit in which the state, observable net, translations, energy form, vacuum projector, and positive dimensionless constant all converge to those of pure Yang--Mills.

## Carrier ledger

The composed proposal has no single operator that secretly performs every job.

| Object | Domain or carrier | What it does |
|---|---|---|
| \(\mathcal C_{\mathrm{shape}}\) | dilation classes of whole cosmological histories with structurally fixed reference events | selects a cut address but not the absolute rate |
| \(\mathcal C_{\mathrm{norm}}\) | an independently normalized capacity plus global algebraic data | breaks the dilation orbit and selects \(\iota_c\), hence \(H_c\) |
| \(\mathfrak y\) | pre-clock wall cuts and cosmological history cuts | synchronizes the algebraic crossing \(s_c\) with the e-fold address \(N_c\); it is presently unconstructed |
| \(\mathfrak S_{\mathrm{cos}}\) | selected whole-state data | returns a dimensional Yang--Mills member |
| \(\mathfrak W\) | common-count cell geometry | returns a physical localization region and width |
| \(\widehat q_{\mathrm{loss},B}\) | a complex energy-form core of localized gauge-invariant state tangents at the vacuum | is the positive Hermitian extension measuring second-order distinction lost under regional restriction |
| \(\mathcal R\) | a common vacuum-reduced whole-to-local tangent carrier | compares independently constructed local and cosmic rate forms; its generalized lower edge is not automatically \(Q_c\) |
| \(H\) | reconstructed physical Hilbert space | generates clock translations and carries the energy gap |
| \(P_\mu P^\mu\) | joint spectrum of reconstructed translations | carries invariant mass |

The logical chain is therefore

\[
\text{whole-state selector}
\longrightarrow
\text{dimensional member and width}
\longrightarrow
\text{regional distinction Hessian}
\longrightarrow
\text{Hamiltonian energy floor}
\longrightarrow
\text{Poincare mass floor}.
\tag{CY28}
\]

The common-count scalar does not act on a glueball state. The relative-entropy Hessian does, after a tangent and region are constructed. Longo compares that form with \(H\) on the same localized path. The last arrow is a separate lemma: if full Poincare covariance, uniqueness of the vacuum, the spectrum condition, and Lorentz invariance of the joint translation spectrum have been constructed, a nonvacuum massless orbit would approach zero energy and a massive orbit of invariant mass \(m<\Delta_E/c^2\) would contain a rest energy below \(\Delta_E\). Under those hypotheses the Hamiltonian floor therefore gives the invariant-mass floor \(m\geq\Delta_E/c^2\). Without them, an energy gap is not yet a mass-Casimir theorem.

The [[contemporary-puzzles/yang-mills-mass-gap/receipts/cosmological-yardstick-receipt.py|cosmological yardstick receipt]] checks dimensions, coefficient cancellations, and the logarithmic-depth normalization identities. It does not validate a selector, the global-to-local carrier change, or a mass gap.

## What would count as success

The cosmological yardstick contributes to the mass-gap problem only if all of the following are supplied:

1. a unique shape selector (CY17b) and normalization selector (CY17c), logarithmic-depth selector (CY17d), or two-boundary construction (CY17e)--(CY17f), derived without a glueball datum, together with the synchronization \(\mathfrak y(s_c)=N_c\) when the wall is natively pre-clock;
2. a carrier-change or boundary-condition map sending that selected cut to a Yang--Mills scale member;
3. the width solder (CY22), rather than the declaration \(R_B=\lambda_*\);
4. a regional descent Hessian whose common kernel on the neutral physical carrier is exactly the vacuum;
5. a positive Hermitian extension and uniform lower bound (CY20) on a complex energy-form core, surviving volume and continuum limits;
6. fossil constancy under later cosmic evolution, despite the live drift (CY18);
7. a pure-Yang--Mills recovery or decoupling theorem of the form required by (CY27);
8. a fixed gauge group, global form, topological-angle sector, RG scheme, and spectrum-independent scheme-conversion rule; and
9. a prospectively frozen prediction not used to choose \(\gamma,s_*,\alpha,\varkappa_B\), or the crossing branch.

The current contribution is therefore exact but intermediate. Whole-cosmos data can be organized into a mathematically economical candidate yardstick; normalized acceleration or entropy growth may enter the shape selector, while an independently quantized capacity or logarithmic depth must fix the dilation normalization; a separately constructed synchronization must identify a pre-clock wall with a cosmological cut; common count selects the one-third monomial; and Longo turns a proved localization width plus a proved Hermitian distinction floor into Hamiltonian energy. The unproved heart is now sharply typed: construct both global selectors, the synchronization and global-to-local width arrows, the complex physical carrier, and neutral regional coercivity without importing the desired mass.
