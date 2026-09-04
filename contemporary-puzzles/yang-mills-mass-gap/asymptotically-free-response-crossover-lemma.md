# The Asymptotically Free Response-Crossover Lemma

One unresolved analytic bridge is to carry the four-dimensional weak-bare-coupling Wilson law, by exact gauge-covariant blocking, to one fixed physical scale where the **full generated non-Abelian law** has a uniform centered \(L^2\) floor and a uniform weighted influence estimate. Their ratio produces a static inverse-distance response exponent independent of the sampler-clock normalization. A covariance-residue theorem then specifies sufficient estimates on both discarded fluctuations and transported sources; terminal mixing alone is not enough. Full Osterwalder--Schrader reconstruction turns one common exponent on a total local family into a Hamiltonian gap. This crossover has not been established here or in the sources reviewed.

**Status: [PROPOSED LEMMA]; [EXACT CONDITIONAL CONSEQUENCE] once the hypotheses below and the continuum OS contract hold; [OPEN] for four-dimensional continuous compact simple Yang--Mills.**

## Input family

Fix a compact simple gauge group \(G\), its global form, the \(\theta=0\)
vacuum theory, and an asymptotically free tuning selected by a declared
renormalization prescription rather than by the unknown mass gap. Here
\(\theta=0\) names the theory and intended vacuum representation, not a
finite-lattice topological sector. If uniformity over additional neutral
sectors is wanted, those sectors must be separately indexed and quantified.
Consider the four-dimensional Wilson measures

$$
\mu_a^{\Lambda,\tau,\mathsf s}
\tag{AFR1}
$$

indexed by ultraviolet spacing \(a\), finite volume \(\Lambda\), admissible boundary data \(\tau\), and allowed blocking scheme \(\mathsf s\). Let

$$
R_{a,j_*}:\mathcal X_a\longrightarrow\mathcal X_{b_a},
\qquad
b_a=L^{j_*(a)}a\in[r_*,Lr_*],
\tag{AFR2}
$$

be an exact gauge-covariant block map, with \(L>1\), to one independently selected physical scale \(r_*>0\). Use isotropic blocking so that the physical OS-axis block spacing is also \(b_a\); an anisotropic construction requires its separately bounded axis conversion. The scale must be fixed by an independent renormalization or whole-law selection condition, not by the unknown gap. Admissible block maps belong to a declared bounded-geometry gauge-covariant class; arbitrary pathological schemes are not quantified over. Admissible boundary data are those compatible with the intended reflection, thermodynamic limit, and uniform estimates. Define the exact image law

$$
\nu_a^{\Lambda,\tau,\mathsf s}
:=
(R_{a,j_*})_*\mu_a^{\Lambda,\tau,\mathsf s}.
\tag{AFR3}
$$

As an explicit Gibbs--polymer hypothesis, require the exact image law to have
a density relative to a declared retained product-Haar or constrained
reference measure \(\lambda_{a,j_*}^{\Lambda,\tau,\mathsf s}\), and require
the complete polymer sum to converge in the weighted interaction norm used by
the locality estimate:

$$
\mathrm d\nu_a(U)
=
Z_{a,j_*}^{-1}e^{-H_{a,j_*}(U)}
\,\mathrm d\lambda_{a,j_*}^{\Lambda,\tau,\mathsf s}(U),
\qquad
H_{a,j_*}(U)=\sum_X\Phi_{a,j_*,X}(U_X).
\tag{AFR4}
$$

Replacing (AFR4) by a fitted one-coupling Wilson action would erase the very nonlinear response that may open the gap.

For the explicit [[rg-covariance-residue/wilson-path-product-fibers|edge-disjoint path-product class]], the finite density part is already proved: a global Haar-preserving chart gives a smooth strictly positive image density relative to retained product Haar. This remains true under finite compositions of such blocks. The unresolved part of (AFR4) is the regulator-uniform weighted interaction expansion and locality of the **full** generated action. Haar factorization does not prove it.

Moreover, [[rg-covariance-residue/thin-skeleton-and-block-average-coercivity|the composite thin-skeleton test]] disproves a geometry-only \(b^{-2}\) Maxwell floor for the discarded fiber of aligned straight paths under joint refinement and volume growth. [[rg-covariance-residue/endpoint-averages-and-quadratic-ultraviolet-control|Endpoint averaging]] supplies a positive full observation inequality. [[rg-covariance-residue/soft-gaussian-gauge-blocking|The soft Gaussian law]] now has depth- and volume-uniform reverse conditional precision, with a [[rg-covariance-residue/compact-gauge-kernel-tangent-response|normalized compact-kernel match]] at fixed regulator. The remaining probabilistic comparison is uniform control of nonlinear remainders and large-field regions, not construction of the Gaussian soft law itself. The anchored deterministic branch separately needs a simultaneous spatial and common-pivot construction. Neither proves the nonlinear response and influence bounds in (AFR6)--(AFR7).

## The terminal response hypothesis

Construct from the exact action (AFR4) a unital invariant local Markov semigroup \(P_t^a\) for the law (AFR3), with the remaining regulator indices suppressed. Fix its local update-rate normalization for the whole regulator family before stating separate uniform constants. Its update geometry and constants may not use the Wilson transfer spectrum, a vacuum eigenfunction, the measured gap, or equivalent long-distance spectral input. This semigroup is an analytical device on Euclidean configurations, not physical time. Prove constants

$$
\kappa_*>0,\qquad
\alpha_*>0,\qquad
0<v_*<\infty,
\tag{AFR5}
$$

independent of \(a,\Lambda,\tau,\mathsf s\), such that every centered gauge-invariant \(h\) satisfies, for all \(t\geq0\),

$$
\|P_t^ah\|_2
\leq
e^{-\kappa_*t}\|h\|_2,
\tag{AFR6}
$$

and every pair of fixed-support local gauge-invariant observables \(f,g\), separated by \(r\) in blocked-lattice distance, satisfies

$$
\left|
\nu_a\!\left(
P_t^a(fg)-P_t^af\,P_t^ag
\right)
\right|
\leq
C_{f,g}
e^{-\alpha_*(r-v_*t)}
\tag{AFR7}
$$

for \(0\leq t\leq r/v_*\). Use bounded smooth gauge-invariant cylinder observables as the initial class. For every fixed renormalized source pair, the corresponding \(L^2\) norms and \(C_{f,g}\) must be uniform in \(a,\Lambda,\tau,\mathsf s\); the prefactor must also be independent of the translation distance. If the available influence theorem uses two separately expanding cones, its stated velocity must be converted to the two-observable convention in (AFR7).

The static block exponent returned by [[auxiliary-response-localization/inq|auxiliary response localization]] is

$$
m_*
:=
\frac{2\alpha_*\kappa_*}
{\alpha_*v_*+2\kappa_*}
>0.
\tag{AFR8}
$$

Under a global sampler-clock change
\(\mathcal L_a\mapsto q\mathcal L_a\), both \(\kappa_*\) and \(v_*\)
scale by \(q\), so \(m_*\) does not. Thus the certificate is \(m_*\), not
the separately normalization-dependent number \(\kappa_*\). If different
sampler geometries rather than global clock rescalings are compared, their
local rate normalization must instead be fixed in advance. The terminal
physical inverse-length floor is

$$
\boxed{
\sigma_{\mathrm{term}}
\geq
\frac{m_*}{Lr_*}
>0.}
\tag{AFR9}
$$

The factor \(Lr_*\) is the largest allowed physical block spacing in (AFR2).
Equation (AFR9) is a certified terminal-law lower bound, not necessarily the
optimal correlation exponent of the microscopic or continuum theory.

## The RG transport obligation

Terminal control is not enough if microscopic sources are lost during the diverging number of blocking steps. A finite total **additive covariance error** would destroy exponential decay at arbitrarily large separation, so bare summability is not enough. The transport theorem must preserve the form of the exponential estimate.

[[rg-covariance-residue/inq|RG covariance residue]] supplies one concrete sufficient route. For nested exact block sigma algebras on the original \(\mu_a\), put \(E_{a,j}=\mathbb E_{\mu_a}[\cdot\mid\mathcal B_{a,j}]\) and \(D_{a,j}=E_{a,j}-E_{a,j+1}\). Then

$$
\operatorname{Cov}_{\mu_a}(F_a,G_a)
=\operatorname{Cov}_{\mu_a}(E_{a,J}F_a,E_{a,J}G_a)
+\sum_{j<J}\langle D_{a,j}F_a,D_{a,j}G_a\rangle_{\mu_a}.
\tag{AFR9a}
$$

At discarded physical scales \(b_{a,j}=b_aL^{j-J}\), a bound

$$
|\langle D_{a,j}F_a,D_{a,j}G_{a,s}\rangle|
\le C_{F,G}(b_a/b_{a,j})^{p_{F,G}}
e^{-m_{\mathrm{sh}}s/b_{a,j}},
\qquad m_{\mathrm{sh}}>0,
\tag{AFR9b}
$$

uniform in the regulator family, sums to a physical exponent at least
\(m_{\mathrm{sh}}/(Lr_*)\). The source powers may vary, but the positive shell exponent must be common. A source-dependent onset \(s\ge s_{F,G}\), uniform in regulators, is allowed. When converting actual support separation to translation distance \(s\), reduce the common shell exponent if necessary; a fixed physical support offset cannot be absorbed into a cutoff-uniform shell prefactor.

The terminal estimate must apply directly to
\(\operatorname{Cov}_{\mu_a}(E_{a,J}F_a,E_{a,J}G_{a,s})\),
through controlled source tails or a conditional-kernel estimate. This,
together with (AFR9b), bounds the original covariance without requiring
translations to descend to the coarse carrier. To obtain the particular
translated-terminal formula (AFR10c), also require translation intertwining
as in (AFR10d), or an exponentially controlled mismatch between
\(E_{a,J}G_{a,s}\) and the pullback of the translated terminal representative.
Source locality alone does not establish that identity. This static route
needs no multiplicative retention product. Neither nesting nor a local block
map proves (AFR9b).

The source norms have an additional normalization obligation.
[[rg-covariance-residue/conditioned-source-transport|Conditioned source transport]]
derives their exact score-response derivative and a weighted influence
recurrence. A bounded cost \(M>1\) per step gives growth in \(b_{a,j}/a\),
not the allowed factor \(b_a/b_{a,j}\). At the terminal scale it can
diverge. The renormalized physical sources must satisfy a uniform envelope
through the entire tower; rescaling intermediate representatives does not
remove their inverse conversion in the original correlations.

An alternative inductive proof may use an exponent ledger: it assigns a dimensionless loss \(\eta_{a,j}^{\mathrm{exp}}\geq0\), expressed in one declared terminal-distance convention, and proves some \(m_0>0\) such that

$$
\sup_a
\sum_{j<j_*(a)}
\eta_{a,j}^{\mathrm{exp}}
\leq
m_*-m_0.
\tag{AFR10}
$$

If \(0\leq\eta_{a,j}<1\) instead measures multiplicative source retention in that proof, its required condition is a positive product such as

$$
\inf_a
\prod_{j<j_*(a)}(1-\eta_{a,j})
>0.
\tag{AFR10a}
$$

The actual conclusion owed by any transport proof must be stated on observables, not
only on constants. For every source pair \(F,G\) in the fixed local class,
require microscopic representatives \(F_a,G_a\), terminal representatives
\(\bar F_a,\bar G_a\), constants
\(C_{F,G}^{\mathrm{tr}}<\infty\) and \(\sigma_{\mathrm{tr}}>0\), and an
OS-axis distance comparison \(r_a(s)\) such that

$$
b_a r_a(s)\geq s-C_{\mathrm{dist}}b_a
\tag{AFR10b}
$$

and

$$
\left|
\operatorname{Cov}_{\mu_a}
   (F_a,\tau_s^{(a)}G_a)
-
\operatorname{Cov}_{\nu_a}
   (\bar F_a,\tau_{r_a(s)}^{(b_a)}\bar G_a)
\right|
\leq
C_{F,G}^{\mathrm{tr}}e^{-\sigma_{\mathrm{tr}}s}.
\tag{AFR10c}
$$

The constants in (AFR10b)--(AFR10c) are uniform in the regulator indices for
each fixed source pair. Exact reflection and translation compatibility is the
special case

$$
R_{a,j_*}\Theta_a=\Theta_{b_a}R_{a,j_*},
\qquad
R_{a,j_*}\tau_{nb_a}^{(a)}
=
\tau_n^{(b_a)}R_{a,j_*},
\tag{AFR10d}
$$

with zero comparison error on pulled-back coarse observables. If (AFR10d)
fails, (AFR10c) and preservation of the reflected OS pairing must be proved
directly on the original Wilson laws. Transporting a full fine auxiliary
functional inequality requires fiber coercivity and macro--micro coupling
control. The static OS route instead permits source-complete conditional
covariance localization such as (AFR9b), without proving a uniform gap for
every chosen fiber sampler. A physically gapless discarded field visible to
the source family would violate those static bounds; a slow auxiliary clock
alone need not. The massless discarded-species counterexample in
[[rg-covariance-residue/inq|RG covariance residue]] makes the distinction exact.

[[contemporary-puzzles/yang-mills-mass-gap/two-scale-rg-descent-and-the-crossover-lemma|Two-scale RG descent]] explains the stronger functional-inequality branch: fiber coercivity, transported coarse metric, and macro--micro coupling. Both branches require source completeness, boundary uniformity, and control of the exact generated law.

## Exact conditional consequence

Fix a countable reflection-supported local generating family and let
\(\mathcal A_0\) be its complex \(*\)-algebra span. The span is generally
uncountable; countability belongs to the generators. Use
\(\operatorname{Cov}(X,Y)=\mu(\overline X Y)-\overline{\mu(X)}\mu(Y)\)
and let \(\Theta_a\) denote the linear reflection pullback, so that the
conjugation in the OS pairing is supplied exactly once by covariance. For every
\(F,G\in\mathcal A_0\), require regulator representatives whose connected
Euclidean correlations converge to those of one limiting Euclidean law. For
every fixed \(F\), require the prelimit reflected diagonal correlations, at
all admissible OS-axis separations, to obey the regulator-uniform estimate

$$
0\leq
\operatorname{Cov}_{\mu_a}
   (\Theta_a F_a,\tau_s^{(a)}F_a)
\leq
C_F e^{-\sigma_0s}
\qquad(s\geq s_F),
\tag{AFR10e}
$$

where \(C_F\) and \(s_F\) may depend on \(F\), but not on
\(a,\Lambda,\tau,\mathsf s\) or the separation, and the exponent is common
to the whole algebra. Together with the assumed correlation convergence,
(AFR10e) passes to the same bound in the limiting Euclidean law. The
transport estimates give the normalization-invariant choice

$$
\sigma_0
:=
\min\!\left\{\frac{m_0}{Lr_*},\sigma_{\mathrm{tr}}\right\}
>0,
\tag{AFR10f}
$$

up to an arbitrarily small endpoint loss if the available estimates are
strict inequalities. On the exact shell route use \(m_0=m_*\) when terminal
source transport retains that exponent and
\(\sigma_{\mathrm{tr}}\ge m_{\mathrm{sh}}/(Lr_*)\); the shell-summation
theorem itself has no endpoint loss. The family may not drift with \(a\).

Assume either that the exact block maps commute with reflection and Euclidean
translations and preserve the OS form, or that the terminal estimate has
been transported back to the original reflection-positive Wilson laws. If
those laws have a nontrivial continuum limit satisfying the full OS
hypotheses, require a unique vacuum
\(P_0=\mathbf1_{\{0\}}(H-E_0)=|\Omega\rangle\langle\Omega|\).
Require explicitly that the centered limiting vectors
\(\psi_F\) reconstructed from \(\mathcal A_0\) satisfy

$$
\overline{\operatorname{span}}
\{\psi_F:F\in\mathcal A_0,\ \psi_F\perp\Omega\}
=
(I-P_0)\mathcal H_{\mathrm{OS}}.
\tag{AFR10g}
$$

With the usual OS placement of supports, the limiting diagonal correlation is
\(\langle\psi_F,e^{-s(H-E_0)/(\hbar c)}\psi_F\rangle\). The spectral theorem
then gives

$$
\boxed{
H-E_0
\geq
\hbar c\,\sigma_0
(I-P_0).}
\tag{AFR11}
$$

Equation (AFR11) is first an energy gap for the reconstructed OS time
translation. It becomes an invariant-mass statement only if the reconstructed
theory also carries a strongly continuous positive-energy Poincaré
representation, its joint energy--momentum spectrum is Lorentz invariant and
contained in the closed forward cone, and the vacuum is the unique
zero-momentum invariant vector. Under those additional hypotheses, every
nonzero massive spectral orbit contains its rest-energy point, while a
massless orbit would have arbitrarily small positive energy. Hence (AFR11)
implies

$$
M_{\mathrm{gap}}
\geq
\frac{\hbar}{c}\sigma_0.
\tag{AFR12}
$$

Equations (AFR11)--(AFR12) compare recovered presentations. The primitive content of the lemma is the transported positive static localization rate \(\sigma_0\) of whole-law response per physical cut distance.

## Why compactness and locality alone are insufficient

Ultraviolet control, compact variables, weak-coupling concentration, and
quasi-locality do not generically imply the conjunction (AFR6)--(AFR7). The
weak-coupling quadratic approximation is Maxwell-like and has volume-soft
physical modes. Continuous four-dimensional \(U(1)\) lattice gauge theory has
a massless Coulomb phase. These counterexamples rule out an argument from
compactness and locality alone. They do not prove that one named non-Abelian
mechanism is logically mandatory: the required distinction could enter through
the trajectory, full interaction, or state. A proposed proof must identify
which additional hypothesis excludes the gapless examples and verify it for
the actual asymptotically free non-Abelian law.

The required mechanism may appear as nonlinear commutator response, a
sector-complete obstruction, an orbit-space effect, or a whole-law Hessian
after unresolved variables have been integrated. Whatever its geometric
language, its analytic return must be the joint uniform floor and influence
certificate (AFR6)--(AFR7) on the complete centered gauge-invariant law.
Importing a Higgs mass or a positive quadratic carrier would assume the
structure that pure Yang--Mills is supposed to generate.

Known results occupy opposite sides of this wall. Balaban's rigorous
four-dimensional \(SU(2)\) compact-volume multiscale programme supplies
gauge-covariant ultraviolet control and quasi-local effective structure, but
not the regulator-uniform terminal sampler certificate (AFR6)--(AFR7).
[[library/a-stochastic-analysis-approach-to-lattice-yang-mills-at-strong-coupling/inq|Shen, Zhu, and Zhu]]
supply a volume-uniform \(L^2\) floor and derivative-propagation control for
\(SU(N)\) and \(SO(N)\) microscopic Wilson laws in their explicit
strong-coupling region. No theorem proves that the asymptotically free
trajectory enters a terminal law satisfying both kinds of estimate.

## Stronger optional certificate

The lemma above proves a qualitative vacuum-sector gap without controlling an infinite boundary face. If the programme also wants the complete whole-to-boundary response operator, replace (AFR7) by the stronger complete conditional estimate

$$
\operatorname*{ess\,sup}_{u_K}
\rho_{\nu_a(\cdot\mid U_K=u_K)}
\bigl(\sigma(U_b),\sigma(U_{b'})\bigr)
\leq
\min\{\kappa_0,Ae^{-m d(b,b')}\}
\tag{AFR13}
$$

for every admissible pinning \(K\) with \(b,b'\notin K\), uniformly in all
regulator indices. Here the essential supremum is taken with respect to the
\(U_K\)-marginal of \(\nu_a\), and
\(\nu_a(\cdot\mid U_K=u_K)\) is a chosen regular conditional law, defined for
almost every \(u_K\). Put
\(\epsilon_{bb'}:=\min\{\kappa_0,Ae^{-m d(b,b')}\}\). Under the hypotheses of
[[library/tensorizing-maximal-correlations/inq|Peyre's theorem]], (AFR13)
tensorizes for finite disjoint bunches \(I,J,K\) to

$$
\operatorname*{ess\,sup}_{u_K}
\rho_{\nu_a(\cdot\mid U_K=u_K)}
\bigl(\sigma(U_I),\sigma(U_J)\bigr)
\leq
\min\!\left\{
1,
\left\|[\epsilon_{bb'}]_{b\in I,b'\in J}\right\|_{\ell^2(J)\to\ell^2(I)}
\right\}.
\tag{AFR14}
$$

A collar width must then be chosen so that the supremum of this kernel norm
over the admissible separated bunches is strictly below one; the pointwise
bound \(\kappa_0<1\) alone is insufficient. This complete-angle branch detects
hidden common variables that ordinary covariance decay can miss, but it is not
required for the dense-total-set spectral argument.

## Kill conditions

The lemma has not been proved if:

- the \(L^2\) floor is established only at fixed strong bare coupling;
- the constants deteriorate with volume, cutoff, boundary condition, blocking scheme, or any separately quantified sector;
- the exact image law lacks the declared Gibbs--polymer representation or the weighted interaction norm needed by the influence theorem is not uniform;
- the sampler acts on a truncated or fitted action rather than the exact image law;
- only local derivative propagation is shown while a global centered mode remains;
- a composite path fiber is assumed ultraviolet from Haar factorization alone, or a linear ultraviolet fluctuation floor is identified with the terminal physical gap;
- the exponent is measured per raw lattice step and not converted at fixed physical scale;
- microscopic source transport, OS-distance comparison, or reflection/translation compatibility is replaced by a merely summable additive error;
- decay is confined to one glueball operator rather than an OS-total family;
- equal-time spatial decay is substituted for OS-time autocorrelation without Euclidean covariance;
- a measured mass, cosmological scale, or Higgs parameter fixes \(r_*\) circularly; or
- continuum existence, reflection positivity, vacuum structure, or Yang--Mills identification is omitted while the **conditional** lemma is advertised as a completed Clay construction.
