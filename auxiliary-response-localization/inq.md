---
inq.module: "auxiliary-response-localization"
inq.include:
  - "**/*.md"
inq.ambient:
  - "**/*.py"
---
# Auxiliary Response Localization

A local reversible dynamics on a Euclidean whole law can be used as a proof instrument without being interpreted as physical or ontological time. Its arbitrary clock disappears when a forgetting rate is combined with an influence-propagation speed: the resulting quantity is a static inverse-distance response exponent. Equivalently, an inverse Witten operator on configuration-space score one-forms turns a local perturbation into its global susceptibility response; exponential localization of that response gives Euclidean clustering. One common physical exponent on a dense Osterwalder--Schrader local core then excludes low Hamiltonian spectrum.

**Status: [EXACT CONDITIONAL THEOREMS] for auxiliary-time elimination, Witten-resolvent localization, generator-rescaling invariance, and the dense-core spectral converse; [PRIMARY-SOURCE PRECEDENT] for strong-coupling lattice Yang--Mills; [OPEN] for regulator-uniform control on the four-dimensional asymptotically free trajectory and its continuum reconstruction.**

## The operator ledger

The construction uses several operators, and none may inherit the interpretation of another merely because their spectra have the same units after a convention is chosen.

| Symbol | Carrier | Operation | It is not |
|---|---|---|---|
| \(P_t=e^{-tL_0}\) | \(L^2(\mu)\) functions of a Euclidean configuration | auxiliary reversible averaging | Lorentzian or OS clock evolution |
| \(d\) | configuration functions to configuration-space one-forms | takes the score of a perturbation | a spacetime exterior derivative |
| \(L_1\) | configuration-space one-forms | transports susceptibility response | the physical Hamiltonian |
| \(L_1^{-1}dG\) | exact score one-forms | global response induced by the local score \(dG\) | a particle wavefunction |
| \(H_{\mathrm{OS}}\) | reconstructed physical Hilbert space | generates Euclidean clock translation and then Lorentzian energy | a sampler generator |

The candidate gap-bearing object before clock reconstruction is a decay rate per declared cut distance. The deeper invariant is the dimensionless product of that rate with a cut separation. Energy and mass arise only after a physical scale section, \(c\), and an action unit have been supplied by the recovery map.

## Eliminating the auxiliary clock

Let \((X,\mu)\) be a probability space carrying a unital, \(\mu\)-invariant Markov semigroup

$$
P_t=e^{-tL_0},
\qquad
\mu(P_th)=\mu(h).
\tag{ARL1}
$$

Let \(f\) and \(g\) be real-valued local square-integrable observables whose supports are separated by distance \(r\). Write \(h^\circ=h-\mu(h)\). Assume two estimates, uniform over the volumes, boundary conditions, and sectors under consideration.

First, centered functions forget at auxiliary rate \(\kappa>0\):

$$
\|P_th^\circ\|_2
\leq
e^{-\kappa t}\|h^\circ\|_2.
\tag{ARL2}
$$

Second, the failure of the semigroup to factor a separated product has a finite-influence estimate

$$
\left|
\mu\!\left(P_t(fg)-P_tf\,P_tg\right)
\right|
\leq
C_{f,g}e^{-\alpha(r-vt)},
\qquad 0\leq t\leq r/v,
\tag{ARL3}
$$

where \(\alpha>0\) is a spatial off-diagonal exponent and \(v>0\) is the **two-observable** influence speed appearing in this multiplicativity-defect bound, measured in distance per auxiliary time. The prefactor may depend on fixed support sizes and seminorms but not on the translation distance \(r\). This is a quasi-locality hypothesis on the proof dynamics, not a claim that stochastic time is physically real. If a source theorem instead gives two separately expanding cones and hence \(r-2vt\), replace \(v\) in (ARL3) by \(2v\); the optimized exponent changes accordingly.

Stationarity gives the exact split

$$
\boxed{
\operatorname{Cov}_\mu(f,g)
=
\mu\!\left(P_t(fg)-P_tf\,P_tg\right)
+
\operatorname{Cov}_\mu(P_tf,P_tg).}
\tag{ARL4}
$$

By (ARL2)--(ARL3) and Cauchy--Schwarz,

$$
|\operatorname{Cov}_\mu(f,g)|
\leq
C_{f,g}e^{-\alpha(r-vt)}
+
\|f^\circ\|_2\|g^\circ\|_2e^{-2\kappa t}.
\tag{ARL5}
$$

Choose \(t=\theta r/v\) and balance the two coefficients of \(r\) in the exponents. This maximizes the certified common exponential rate; when the two prefactors in (ARL5) differ, it need not be the pointwise minimizer of the full right-hand side. The balancing value and common exponent are

$$
\theta_*
=
\frac{\alpha v}{\alpha v+2\kappa},
\qquad
\boxed{
\sigma_{\mathrm{aux}}
=
\frac{2\alpha\kappa}{\alpha v+2\kappa}.}
\tag{ARL6}
$$

Thus

$$
|\operatorname{Cov}_\mu(f,g)|
\leq
\left(C_{f,g}+\|f^\circ\|_2\|g^\circ\|_2\right)
e^{-\sigma_{\mathrm{aux}}r}.
\tag{ARL7}
$$

This is an **[EXACT CONDITIONAL THEOREM]**. Invariance and unitality give (ARL4); reversibility is not used once (ARL2) is assumed. The auxiliary parameter has been eliminated. If the same generator is rescaled by \(L_0\mapsto qL_0\) with \(q>0\), equivalently \(P_t^{(q)}=P_{qt}\), then

$$
\kappa\mapsto q\kappa,
\qquad
v\mapsto qv,
\qquad
\alpha\mapsto\alpha,
\tag{ARL8}
$$

and (ARL6) is unchanged. Neither \(\kappa\) nor \(v\) is independently physical; their static response-cone combination is normalization invariant. Different admissible samplers for the same law can still give different nonoptimal certificates. A canonical number would require an independently selected sampler class and optimal constants, or a supremum over that declared class.

[[auxiliary-response-localization/receipts/auxiliary_response_localization_receipt.py|The finite receipt]] checks (ARL4), the optimized exponent, generator-rescaling invariance, and the linear-Gaussian Witten covariance identity. It tests none of the locality, Yang--Mills, RG, or continuum premises.

A scalar Poincare gap alone is therefore insufficient. It supplies (ARL2) after its normalization is declared but contains no physical distance. The locality or commutator estimate (ARL3) is the second indispensable input.

## The Witten-resolvent form

The same mechanism has a static formulation. Let

$$
X=\mathsf G^E,
\qquad
d\mu=Z^{-1}e^{-S}\,d\operatorname{vol},
\tag{ARL9}
$$

where \(\mathsf G\) is a compact Lie group and \(E\) is the finite set of lattice edges or blocked cells. Let \(d_\mu^*\) be the weighted adjoint of the configuration differential and define

$$
L_0=d_\mu^*d,
\qquad
L_1=dd_\mu^*+d_\mu^*d.
\tag{ARL10}
$$

Here \(L_1\) acts on one-forms over **configuration space**. Their components are indexed by edge or cell variables; they are not one-forms on reconstructed spacetime. For compatible self-adjoint realizations, the intertwining relation on a common smooth core and then by closure is

$$
dL_0=L_1d.
\tag{ARL11}
$$

Assume the required Poincare, closed-range, domain, and boundary-condition hypotheses, and assume that \(\ker L_0=\mathbb C1\) on the retained ergodic sector. For centered real-valued smooth observables \(F,G\), use the reduced inverse on \(\overline{\operatorname{Ran}d}\), the exact one-form sector. Then

$$
\boxed{
\operatorname{Cov}_\mu(F,G)
=
\left\langle dF,L_1^{-1}dG\right\rangle_{L^2(\mu;T^*X)}.}
\tag{ARL12}
$$

Indeed, if \(u=L_0^{-1}G\), then \(du=L_1^{-1}dG\), and integration by parts gives

$$
\langle F,G\rangle
=
\langle F,L_0u\rangle
=
\langle dF,du\rangle.
\tag{ARL13}
$$

Suppose \(G\) is supported in a cell set \(B\), and define a weight on configuration one-forms by

$$
(W_{\sigma,B}\omega)_e
=
e^{\sigma d(e,B)}\omega_e.
\tag{ARL14}
$$

If one \(\sigma>0\) and, for each fixed local observable class, one \(C_G<\infty\) work uniformly in cutoff, volume, allowed boundary condition, retained sector, and translation of \(G\), so that

$$
\|W_{\sigma,B}L_1^{-1}dG\|_2
\leq C_G
\tag{ARL15}
$$

holds, then every \(F\) supported in \(A\) obeys

$$
\boxed{
|\operatorname{Cov}_\mu(F,G)|
\leq
\|dF\|_2C_G
e^{-\sigma d(A,B)}.}
\tag{ARL16}
$$

This follows by inserting \(W_{\sigma,B}^{-1}W_{\sigma,B}\) in (ARL12). It identifies what the inverse operator operates on: a local score is sent to the whole-law susceptibility it induces, and the desired theorem says that this response is exponentially unable to remain equally strong at arbitrary distance.

For gauge-invariant \(F,G\), one may work on the smooth product \(\mathsf G^E\) rather than prematurely quotienting by the stratified gauge orbit space. With an invariant metric and action, \(L_0\) and \(L_1\) commute with the gauge action, while \(dF\) and \(dG\) are invariant exact forms annihilating vertical gauge directions. A scalar Poincare gap controls this exact sector, not every coexact or harmonic one-form. If a chosen generator has a fixed algebra larger than the constants, (ARL2) and the reduced inverse must instead use the orthogonal fixed-space projection, and every conclusion is confined to its complement. Neither these configuration-space one-forms nor their exact sector are carriers for a generalized one-form global symmetry; the later local OS argument reaches only the cyclic neutral vacuum representation unless an extended-operator totality theorem is added. Neither (ARL11) nor the parabolic Witten heat semigroup supplies finite propagation by itself; weighted off-diagonal control is a separate theorem.

[[exact-source-locality-without-a-full-form-gap|Exact-source locality]] supplies a sufficient off-diagonal estimate without a full one-form gap. Spatial weights need not preserve exact forms: bounded weighted growth is proved on the full nonnegative operator, while long-time decay is used only on the original exact source. Splitting those two estimates gives a static exponential bound. [[rg-covariance-residue/nonlinear-conditional-gauge-response|The normalized compact gauge law]] supplies explicit Hessian and locality constants in a conditional strong-coupling regime.

[[library/witten-laplacian-methods-for-the-decay-of-correlations/inq|Lo's Witten-Laplacian method]] proves this covariance-resolvent strategy for classes of lattice spin systems. [[library/witten-laplacian-on-a-lattice-spin-system/inq|Shigekawa]] supplies related volume- and boundary-uniform positive-degree form estimates. These are precedents for the operator signature, not Yang--Mills continuum theorems.

## From one common exponent to an OS gap

The complete spectral statement does not require one observable-independent prefactor. It does require one observable-independent exponent on a dense physical family.

Let a full Osterwalder--Schrader reconstruction produce a strongly continuous semigroup of positive self-adjoint contractions

$$
T(s)=e^{-sA},
\qquad
A=\frac{H-E_0}{\hbar c}\geq0
\tag{ARL16a}
$$

on \((\mathcal H,\Omega)\), where \(\|\Omega\|=1\), \(A\Omega=0\), \(P_0=\mathbf1_{\{0\}}(A)\), and \(Q=I-P_0\). Vacuum uniqueness is the additional assertion \(P_0=|\Omega\rangle\langle\Omega|\). The coordinate \(s\) is Euclidean length along the reconstructed clock axis. Suppose the linear span of \(\mathcal D_{\mathrm{loc}}\subset Q\mathcal H\), reconstructed from centered gauge-invariant local observables, is Hilbert-norm dense in \(Q\mathcal H\). Assume that one \(\sigma_*>0\) satisfies the positive diagonal autocorrelation bound, for every \(\psi\in\mathcal D_{\mathrm{loc}}\),

$$
0\leq
\langle\psi,e^{-sA}\psi\rangle
\leq
C_\psi e^{-\sigma_*s}
\qquad(s\geq s_\psi),
\tag{ARL17}
$$

where \(C_\psi\) and \(s_\psi\) may depend on \(\psi\). Then

$$
\boxed{
H-E_0\geq\hbar c\,\sigma_*Q.}
\tag{ARL18}
$$

To prove this, apply the spectral theorem to the positive measure

$$
\nu_\psi(B)
:=
\langle\psi,\mathbf1_B(A)\psi\rangle,
\qquad
B\in\mathcal B([0,\infty)).
\tag{ARL19}
$$

If \(\nu_\psi((0,\sigma_*))>0\), then for some \(\delta<\sigma_*\) it charges \((0,\delta]\), and

$$
\langle\psi,e^{-sA}\psi\rangle
\geq
e^{-\delta s}\|\mathbf1_{(0,\delta]}(A)\psi\|^2,
\tag{ARL19a}
$$

contradicting (ARL17) at large \(s\). Hence every \(\psi\in\mathcal D_{\mathrm{loc}}\) is annihilated by \(\mathbf1_{(0,\sigma_*)}(A)\). Density makes that projection zero on \(Q\mathcal H\), proving (ARL18).

This **[EXACT CONDITIONAL CONVERSE]** is stronger than decay in one glueball channel and weaker than a uniform complete-slice angle at one finite collar. Support-dependent constants are allowed. What must be uniform is the physical exponent and the theory, state, sector, and continuum identification. Equal-time spatial clustering alone is insufficient unless Euclidean covariance or another theorem carries the estimate to the OS translation direction. Reflection positivity alone is likewise insufficient: the translation semigroup and its passage through the OS null quotient are essential.

## Two non-equivalent stopping routes

There are now two rigorous analytic targets.

The **dense-core route** proves (ARL16) with one physical \(\sigma_*>0\) for every local observable in an OS-dense neutral family and invokes (ARL18). It avoids summing local estimates over an infinite transverse slice. It does not directly construct the complete midpoint-to-two-boundary prediction norm.

The stronger **complete-angle route** controls the full boundary response. For an RG-blocked law and distinct blocks \(b,b'\), let

$$
\rho_K(b,b')
:=
\operatorname*{ess\,sup}_{u_K}
\rho_{\mu(\,\cdot\mid U_K=u_K)}(U_b,U_{b'})
\tag{ARL19b}
$$

for every subfamily \(K\) of the remaining elementary variables required by the natural sigma-metalgebra, with the essential supremum taken over the conditioning values. A proposed complete-pinning estimate is

$$
\rho_K(b,b')
\leq
\varepsilon(b,b')
\leq
\min\{\kappa_0,Ae^{-m d(b,b')}\},
\qquad \kappa_0<1.
\tag{ARL20}
$$

Here \(\kappa_0,A,m\) and the essential-supremum estimate must be uniform in regulator, volume, allowed boundary condition, retained sector, and all declared pinnings.

Writing \(E_{I,J}=[\varepsilon(b,b')]_{I\times J}\), [[library/tensorizing-maximal-correlations/inq|Peyre's tensorization theorem]] gives

$$
\rho(U_I,U_J)
\leq
\min\{1,\|E_{I,J}\|_{\ell^2(J)\to\ell^2(I)}\}.
\tag{ARL20a}
$$

On a declared bounded-growth lattice, a Schur estimate bounds this norm by the geometric mean of the maximal row and column sums. A translation-covariant exponential kernel can therefore give a bound independent of transverse face area, although a subunit complete angle still requires the resulting operator norm—not merely each entry—to be smaller than one. This is the cleanest known route back to the response operator of [[global-local-response-reconstruction/inq|global--local response reconstruction]].

Ordinary pairwise covariance decay is not (ARL20). The estimate must survive arbitrary pinnings, gauge reduction, boundary conditions, sectors, and the full quasi-local polymer interaction. That stronger quantifier detects hidden common parity or topological variables that ordinary clustering can miss.

## The Yang--Mills theorem still owed

[[library/a-stochastic-analysis-approach-to-lattice-yang-mills-at-strong-coupling/inq|Shen, Zhu, and Zhu]] prove that the genuine Wilson law at sufficiently strong microscopic coupling has a volume-uniform auxiliary Poincare gap and exponential correlation decay. Their proof combines semigroup forgetting with control of how local derivatives spread. It is a concrete finite-regulator realization of the mechanism behind (ARL4)--(ARL7).

It does not solve the Clay problem. Four-dimensional continuum Yang--Mills approaches weak bare coupling, and the missing construction is a gauge-covariant RG theorem carrying that ultraviolet law to a fixed physical block scale at which either of the following holds uniformly:

1. the Witten or semigroup estimates yield one common physical exponent on an OS-dense gauge-invariant local core; or
2. the effective polymer law satisfies the complete conditional Hilbertian kernel estimate (ARL20).

The estimates must be uniform in cutoff, volume, admissible boundary condition, and retained neutral sector. They must survive the diverging number of RG steps, preserve reflection positivity or supply another valid reconstruction, and identify the limiting local theory as nontrivial Yang--Mills. This is the exact remaining analytic wall, not a request to guess a glueball number.

If \(m_a\) denotes a dimensionless exponent per raw Euclidean-time lattice step \(a_{\tau,a}\), the physical inverse length is

$$
\sigma_a=\frac{m_a}{a_{\tau,a}}.
\tag{ARL21}
$$

A certified positive continuum floor requires

$$
\liminf_{a\to0}\frac{m_a}{a_{\tau,a}}
\geq
\sigma_*>0.
\tag{ARL21a}
$$

Convergence to a specified finite edge would require the stronger limit \(m_a/a_{\tau,a}\to\sigma_*\); asymptotic equivalence is not needed for a lower-bound theorem. At a fixed physical blocked spacing \(b_*\), the corresponding conversion is \(\sigma_*=m_*/b_*\). This prevents a sampler gap or a lattice cutoff from being mistaken for a physical mass.

## The Copernican interpretation

The new invariant is not “particles lose memory at rate \(\kappa\).” It is that a local distinction induces a global response whose strength has a finite, clock-independent localization length. In the language of the programme, the whole law does not become local; rather, its response to a pointed local score admits an exponentially localized presentation.

After a positive-energy Poincare representation with Lorentz-invariant joint translation spectrum has been reconstructed, the static exponent has the following lower-edge presentations in the cyclic neutral vacuum representation:

$$
\Gamma_*=c\sigma_*,
\qquad
\Delta_E\geq\hbar\Gamma_*,
\qquad
M_{\mathrm{gap}}\geq\frac{\hbar}{c}\sigma_*.
\tag{ARL22}
$$

These are comparison maps, not equations of concepts. The primitive theorem concerns the response exponent; \(\Gamma_*\), energy, and invariant mass are its recovered clock, action, and Poincare presentations.

The Higgs field belongs to a different slot. A Higgs vacuum value can be a local coordinate for a reduction to a stabilizer, but pure Yang--Mills has no Higgs field and still owes a neutral mass gap. [[higgs-reduction-as-local-shadow/inq|The Higgs reduction note]] therefore treats the scalar as a possible local shadow of whole-to-local pointing, not as the complete gap operator or the origin of scale.

Cosmology and the geon conjecture may enter upstream by selecting the state, cut metric, or physical section \(b_*\) through a whole-boundary, entropy, or leakage law. They do not replace (ARL15), (ARL17), or (ARL20). The standard radiation-FLRW comparison that makes a Hubble harmonic far too soft is conditional on the recovered FLRW/QFT presentation; a deeper global--local map may evade that typing only by constructing a new dimensionless relation rather than equating unlike local measurements.

## Failure conditions

The route fails if:

- the auxiliary dynamics forgets but has no uniform influence control;
- the static exponent depends on the arbitrary normalization of \(L_0\);
- weighted one-form control holds only outside the gauge-invariant neutral carrier;
- decay is proved only for a preferred observable or with exponents tending to zero across a dense family;
- complete-angle claims are inferred from ordinary pair covariance;
- an order-one raw-lattice rate is confused with a finite continuum inverse length;
- cosmological, Higgs, or glueball measurements are used to fit the scale that the construction claims to derive; or
- OS positivity, vacuum uniqueness, continuum existence, and Yang--Mills identification are assumed rather than recovered.
