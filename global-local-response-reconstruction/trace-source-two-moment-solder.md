# The Trace Source Has Two Inequivalent Moments

The renormalized trace of the stress tensor is the cleanest existing common carrier between cosmic nonconformality and glueball spectroscopy: within one fixed theory, its thermal one-point function is the interaction measure \(\epsilon-3p\), while its vacuum connected two-point function has a positive-energy spectral measure in the scalar channel. These are derivatives of one source coupling evaluated in two state-dependent functionals, not two derivatives of one numerical observable; neither moment determines the other. The cosmological thermal carrier is full QCD or the wider material theory, whereas the Clay vacuum carrier is pure Yang--Mills, so their comparison additionally requires a theory-change map. A pre-QFT framework earns a genuine cosmology--mass-gap bridge only if one upstream scale response reconstructs both theory-specific returns and then extends the pure-gauge vacuum Hessian from the scalar trace channel to the complete physical carrier with a uniform positive edge.

**Status: [EXACT AT POSITIVE REGULATOR] for the source derivative and covariance identities; [STANDARD AFTER QFT RECONSTRUCTION] for the trace anomaly, thermal interaction measure, and vacuum spectral representation; [CONDITIONAL] for using a complete operator family to certify a Hamiltonian gap; [OPEN] for their common pre-QFT origin and four-dimensional Yang--Mills realization.**

## One source, not one number

Let \(\Theta_L=T^\mu{}_{\mu}\) be the renormalized Lorentzian stress-tensor trace after a local QFT, state, and renormalization prescription have been constructed. In the convention \(\mathcal L=-F^2/4\), with \(g\) inside \(F=\mathrm dA+gA\wedge A\) and \(\beta(g)=\mu\,\mathrm dg/\mathrm d\mu\), pure Yang--Mills has the schematic operator form

$$
\Theta_L
=
\frac{\beta(g)}{2g}[F^a_{\mu\nu}F^{a\mu\nu}]_R
+\text{BRST-exact, equation-of-motion, and total-derivative mixing},
\tag{TM1}
$$

With \(S=(4g^2)^{-1}\int\mathcal F^2\) and \(g\) removed from \(\mathcal F\), the displayed coefficient is instead proportional to \(-\beta(g)/(2g^3)\). [[library/trace-and-dilatation-anomalies-in-gauge-theories/inq|Collins, Duncan, and Joglekar]] establish the renormalized non-Abelian trace anomaly and its mixing qualifications; equation (TM1) is not a new derivation. Contact or seagull terms are not ordinary addends in the one-insertion operator identity. They occur distributionally when trace insertions or Weyl derivatives coincide. With dynamical quarks, mass operators and their anomalous dimensions enter as additional terms. Pure Yang--Mills and the early cosmos governed by full QCD are therefore different theories even when they use related trace insertions.

The Euclidean insertion \(\Theta_E\) requires a declared Wick-rotation and source-sign convention. Below it is normalized so that the homogeneous renormalized thermal first variation, after vacuum subtraction and division by four-volume, continues to \(\langle\Theta_L\rangle_T-\langle\Theta_L\rangle_0=\epsilon-3p\). This convention is load-bearing for the sign of the one-point return; the connected variance is insensitive to reversing the sign of the insertion.

At a finite positive Euclidean regulator, let \(\nu_\omega\) be a normalized commutative probability measure. For a source-independent dimensionless smeared insertion \(\Theta_E(J)\) linear in \(J\), including the required Euclidean action units, define one common source prescription in every state \(\omega\) by

$$
Z_\omega[J]
:=
\int
\exp\!\bigl(\Theta_E(J)\bigr)
\,\mathrm d\nu_\omega,
\qquad
W_\omega[J]:=\log Z_\omega[J].
\tag{TM2}
$$

For \(J=\sigma f\), whenever the relevant exponential moments permit differentiation under the integral,

$$
\left.\partial_\sigma W_\omega[\sigma f]\right|_0
=
\omega\!\left(\Theta_E(f)\right),
\qquad
\left.\partial_\sigma^2 W_\omega[\sigma f]\right|_0
=
\operatorname{Var}_\omega\!\left(\Theta_E(f)\right).
\tag{TM3}
$$

Equation (TM3) is ordinary variance because this regulator is a commutative Euclidean measure; a noncommutative Gibbs perturbation generally gives a Duhamel or BKM covariance. With two independent sources coupled to separated smearings \(f_0,f_\ell\), the mixed derivative is

$$
\left.
\partial_{\sigma_0}\partial_{\sigma_\ell}
W_\omega[\sigma_0f_0+\sigma_\ell f_\ell]
\right|_0
=
\operatorname{Cov}_\omega\!\left(\Theta_E(f_0),\Theta_E(f_\ell)\right).
\tag{TM3c}
$$

A functional source \(\sigma(x)\) packages the full connected two-point kernel. In continuum QFT, an actual Weyl deformation gives that kernel plus the local response \(\langle\delta\Theta(x)/\delta\sigma(y)\rangle\), with the chosen signs and anomaly counterterms. Thus “one operator, two moments” means one typed source family—not a numerical equality between its gradient and Hessian. A single integrated variance does not determine a spectral edge; the separated \(\ell\)-profile is essential.

[[exceptional-context-analysis-of-gauge-gradients|The differentiated exceptional frame]] gives a further useful distinction at a smooth finite gauge regulator. The same context-analysis map can factor the configuration-gradient form of \(\Theta_E(f)\) under different specified measures, with the same geometric coefficient \(9/13\). Its weighted adjoint and spectral constant nevertheless depend on the measure. A common geometric frame therefore does not identify a thermal mean, a source covariance, a configuration-gradient norm, and a vacuum spectral edge; the state and reconstruction maps remain essential.

This suggests a candidate field-theoretic content for [[global-local-response-reconstruction/yang-mills-balanced-fisher-grain|the balanced-Fisher score]]. Along a differentiable fixed-carrier effective-action path \(\mathrm d\nu_N=Z_N^{-1}e^{-S_N}\mathrm dm\), with \(N\)-independent \(m\) and all Jacobians absorbed into \(S_N\),

$$
A_N:=\partial_NS_N,
\qquad
s_N=-(A_N-\mathbb E_NA_N),
\qquad
\mathcal I_N=\operatorname{Var}_N(A_N).
\tag{TM3a}
$$

The sign says that the score is the **negative** centered action derivative. If a separately selected RG connection and continuum Ward identity identify \(A_N\) with a smeared scale-trace insertion, this proposes a centered trace direction. For an actual carrier-changing blocking, however, the midpoint score generally has the form

$$
s_N^{\mathrm{mid}}
=
\mathbb E_N\!\left[
s_N^{\mathrm{full}}+u_N^{\mathrm{block}}
\mid\text{midpoint}
\right],
\tag{TM3d}
$$

where \(u_N^{\mathrm{block}}\) is first defined as the conditional DQM score of the blocking kernel:

$$
\partial_N\sqrt{c_N(\,\cdot\mid x)}
=
\frac12u_N^{\mathrm{block}}(x,\cdot)
\sqrt{c_N(\,\cdot\mid x)}
\quad\text{in conditional }L^2.
\tag{TM3e}
$$

Under positive densities on common support, pointwise differentiability, and domination strong enough to pass the derivative through the marginal, \(u_N^{\mathrm{block}}=\partial_N\log c_N\) almost everywhere. Equation (TM3d) requires joint DQM sufficient to differentiate the marginal, or these stronger pointwise hypotheses; otherwise support or boundary terms may occur. The trace interpretation therefore requires both the RG connection and this contribution, or a theorem that removes it. If those obligations are met, the thermal mean of the insertion contributes to a free-energy trace return, while its covariance is a linear-source susceptibility that can be split into boundary-recoverable and midpoint-residual parts. For differentiation along the action path itself,

$$
\partial_N^2\log Z_N
=
\operatorname{Var}_N(\partial_NS_N)
-
\mathbb E_N(\partial_N^2S_N),
\tag{TM3b}
$$

so Fisher variance is not the full free-energy curvature unless the expectation of \(\partial_N^2S_N\) vanishes. Action curvature, connection, and contact terms must not be silently dropped. The linear auxiliary source in (TM2) isolates the covariance cleanly.

## The thermal return is a one-point trace ledger

In \(3+1\) dimensions, use the mostly-minus metric and a homogeneous isotropic equilibrium state. If \(\epsilon(T)\) and \(p(T)\) below denote consistently vacuum-subtracted densities, then

$$
\omega_T(\Theta_L)-\omega_0(\Theta_L)
=
\epsilon(T)-3p(T)
=:
\mathcal I_{\mathrm{th}}(T).
\tag{TM4}
$$

Equivalently, the right side is \((\epsilon_T-\epsilon_0)-3(p_T-p_0)\). With \(V_4\) a Euclidean four-volume in length units and the source convention fixed above, the homogeneous source relation is

$$
\epsilon(T)-3p(T)
=
\lim_{V_4\to\infty}
\frac{\hbar c}{V_4}
\left(
D_{\mathbf1}W_T[0]-D_{\mathbf1}W_0[0]
\right).
\tag{TM4a}
$$

Thus a constant Weyl-source derivative is extensive; obtaining (TM4) from it requires the displayed unit conversion, matched thermal and vacuum support, the thermodynamic limit, and the stated subtraction. This interaction measure detects departure from conformal radiation in a thermal state. A generic RG-depth derivative is not automatically this Weyl or temperature response.

Its cosmological history can be integrated into the dimensionless additive cocycle developed in [[contemporary-puzzles/yang-mills-mass-gap/trace-residue-as-a-scale-cocycle|trace residue as a scale cocycle]],

$$
\Xi_\Theta(N_1,N_2)
=
\int_{N_1}^{N_2}
\frac{\rho-3p}{\rho}\,\mathrm dN.
\tag{TM5}
$$

Equation (TM5) is a one-point, state-dependent history ledger for whatever cosmic sectors and vacuum convention enter \(\rho,p\). It can mark a nonconformal episode and is additive under concatenation. It is not automatically the lattice-QCD interaction measure: that identification requires a sector, subtraction, and thermal-to-cosmological state map. Nor is it a vacuum spectral floor, an entropy-production theorem, or the rest mass of the cosmological contents.

The empirically relevant transitions must also remain separated. Physical \((2+1)\)-flavor QCD has a smooth chiral crossover in the temperature band summarized by [[library/equation-of-state-in-2-plus-1-flavor-qcd/inq|HotQCD]]. Pure \(SU(3)\) Yang--Mills instead has a first-order thermal deconfinement transition, as continuum finite-size scaling confirms in [[library/precision-study-of-the-continuum-su3-yang-mills-theory/inq|the precision pure-gauge study]]. Higgs mass generation, confinement or hadronization, baryogenesis, a species becoming nonrelativistic, baryon loading of the photon fluid, and recombination are still other events. The phrase “baryons clicked on” must choose one of these return types before it can enter an equation.

## The vacuum return is a two-point spectral ledger

Now use the zero-temperature vacuum \(\Omega\), subtract the trace expectation, and smear into a nonzero gauge-invariant scalar vector \(\widehat\Theta\Omega\). Work first on a finite spatial torus, or with spatial wave packets followed by a controlled infinite-volume and zero-momentum limit; exact zero-momentum projection in infinite volume is distributional. Let \(P_0\) be the complete ground-energy projection, put \(Q=I-P_0\), and require \(\widehat\Theta\Omega\in Q\mathcal H\). For Euclidean test functions supported at positive time, the OS insertion is an equivalence class in the reflected positive-time quotient; time-zero notation for \(\widehat\Theta\Omega\) is shorthand for its reconstructed limit. After Osterwalder--Schrader reconstruction, its Euclidean correlation along a physical length \(\ell>0\) has the spectral form

$$
C_\Theta(\ell)
=
\left\langle
\widehat\Theta\Omega,
e^{-\ell(H-E_0)/(\hbar c)}
\widehat\Theta\Omega
\right\rangle
=
\int_{[0,\infty)}
e^{-\ell E/(\hbar c)}
\,\mathrm d\nu_\Theta(E).
\tag{TM6}
$$

The full OS package—reflection positivity, Euclidean translations, continuity, and the remaining reconstruction hypotheses—constructs the Hilbert space and positive contraction semigroup; the spectral theorem for its reconstructed self-adjoint generator then makes \(\nu_\Theta\) a positive measure. Its lower support edge

$$
\Delta_\Theta
:=
\inf\operatorname{supp}\nu_\Theta
\tag{TM7}
$$

is a scalar-channel energy threshold. In finite volume it is only an energy threshold because boosts and continuous momenta are absent. After Poincare-covariant infinite-volume reconstruction and the controlled zero-momentum limit, its invariant-mass presentation is \(m_\Theta=\Delta_\Theta/c^2\). If the trace overlaps the lightest stable \(0^{++}\) glueball, that state contributes an atom; multiparticle thresholds contribute continuous support.

For a finite nonzero measure, the entire large-collar profile—not the equal-time variance—recovers its lower support:

$$
\Delta_\Theta
=
-\hbar c
\lim_{\ell\to\infty}
\frac1\ell\log C_\Theta(\ell).
\tag{TM7a}
$$

This is a far stronger relation to glueballs than a coincidence between a cosmological energy scale and a tabulated mass. Yet one trace correlator still cannot prove the Clay gap. It probes only the scalar channel generated by \(\Theta\); the lightest physical excitation could lie in another channel, and directions orthogonal to \(\Theta\Omega\) are unseen.

## The complete-family upgrade

Let \(P_0=E_{H-E_0}(\{0\})\) project onto the complete ground-energy eigenspace and put \(Q=I-P_0\); replacing \(P_0\) by \(|\Omega\rangle\langle\Omega|\) would already assume vacuum uniqueness. Let \(\mathcal O\) be a gauge-invariant local operator family such that the centered vectors

$$
\mathcal D_{\mathcal O}
:=
\operatorname{span}
\left\{
Q(A-\langle\Omega,A\Omega\rangle)\Omega:A\in\mathcal O
\right\}
\tag{TM8}
$$

belong to \(\operatorname{Dom}(H-E_0)^{1/2}\cap Q\mathcal H\) and form a core for the Hamiltonian quadratic form restricted to \(Q\mathcal H\). A common lower edge becomes a full Hamiltonian gap only if

$$
\left\|(H-E_0)^{1/2}\psi\right\|^2
\geq
\Delta_*\|\psi\|^2
\quad
\text{for every }\psi\in\mathcal D_{\mathcal O},
\qquad
\Delta_*>0.
\tag{TM9}
$$

Closure then gives \(H-E_0\geq\Delta_*Q\). This proves a gap above the complete ground-energy eigenspace; it does not prove that \(P_0\) has rank one. Vacuum uniqueness is a separate reconstruction obligation. Equivalently, if the source vectors are total in \(Q\mathcal H\), their spectral measures must share a **uniform** positive support threshold. Separate positive thresholds without a uniform infimum are compatible with a gapless theory. This is a stopping certificate—essentially the gap theorem stated on a core—not an independent derivation. [[distinction-grain-spectrum/inq|The distinction-grain spectrum]] gives the same quantifier in conditional-response language.

The desired pre-QFT construction must therefore lift (TM3) from one scale tangent to a complete response form before using [[global-local-response-reconstruction/qft-recovery-contract|the QFT recovery contract]] to identify that form with (TM9). A nonzero thermal trace or even a scalar glueball pole does not perform this lift.

## The Copernican reversal stated precisely

The standard story says that a classically scale-invariant local gauge theory develops a scale through the anomaly and then asks why its spectrum is gapped. The reversal is to demand one upstream whole-law scale response whose local reconstruction has two derivatives:

$$
\begin{array}{rcl}
\text{thermal first moment}
&\longleftarrow&
\mathfrak R_{\mathrm{scale}}
\longrightarrow
\text{vacuum connected Hessian},\\[2mm]
\epsilon-3p
&&
\mathcal G_0:=D^2W_\Omega\big|_{\mathsf{Src}_0^+}.
\end{array}
\tag{TM10}
$$

The left return says that a chosen state is nonconformal. The right return is a connected correlation kernel whose separated profile encodes scalar spectral support. Only after a complete source family, insertion maps, and the clock carrier have been constructed can a uniform response edge become a mass-gap certificate. In this sense the cosmic trace history can be a fossil of the same scale-forming law without being the cause, numerical value, or proof of the glueball gap.

Here \(\mathsf{Src}_0^+\) is a declared positive-Euclidean-time test-source space and \(\vartheta\) is the anti-linear reflected adjoint; for the Hermitian scalar trace, \((\vartheta f)(x)=\overline{f(\theta x)}\), where \(\theta\) reverses Euclidean time. Before passing to time-zero reconstructed operators, the complexified OS kernel is the sesquilinear form

$$
\mathcal G_{\mathrm{OS}}(f,g)
:=
D^2W_\Omega[0](\vartheta f,g).
\tag{TM10a}
$$

Its insertion map into \(\mathcal H\) is a separate carrier-changing arrow from the OS quotient,

$$
J_\Theta:[f]_{\mathrm{OS}}\longmapsto\widehat\Theta(f)\Omega.
\tag{TM10b}
$$

After the reflection and null-space quotient have been included, the centered covariance pulls back as \(J_\Theta^*QJ_\Theta\). The energy-weighted object is instead the quadratic-form pullback

$$
\mathfrak h_\Theta([f],[g])
:=
\left\langle
(H-E_0)^{1/2}J_\Theta[f],
(H-E_0)^{1/2}J_\Theta[g]
\right\rangle
\tag{TM10c}
$$

on \(J_\Theta^{-1}\operatorname{Dom}(H-E_0)^{1/2}\). Writing \(J_\Theta^*(H-E_0)J_\Theta\) as an operator would require the stronger Hamiltonian-domain condition. One trace source reaches only a scalar cyclic subspace. Completeness cannot be created by writing the physical projection \(Q\) directly around an unreflected source Hessian.

This formulation also clarifies “mass as a rate.” The primitive common datum in (TM10) is a scale response. The word *rate* becomes legitimate only after the vacuum correlations are soldered to Euclidean persistence and a reconstructed Lorentzian clock:

$$
\Gamma_*
=
\frac{\Delta_*}{\hbar},
\qquad
m_*
=
\frac{\hbar\Gamma_*}{c^2}.
\tag{TM11}
$$

Here \(\Gamma_*\) is a rate per Lorentzian clock time. Relative to the Euclidean length \(\ell\) in (TM6), the attenuation rate is instead \(\Gamma_{\ell,*}=\Delta_*/(\hbar c)\). The thermal trace is neither rate. It is the first-moment image of the same proposed upstream source.

## Stopping condition

The trace-source bridge is realized only when one construction supplies:

1. a pre-clock scale source or cocycle and its oriented composition law;
2. two state reconstructions—vacuum and thermal—from one upstream object;
3. the contact-term-controlled first- and second-variation identities in the continuum;
4. the full-QCD to pure-Yang--Mills comparison, rather than identifying their crossovers;
5. a complete gauge-invariant operator family satisfying the uniform estimate (TM9);
6. vacuum uniqueness as an obligation distinct from the gap above the ground-energy space;
7. OS/Poincare recovery identifying its support edge with invariant mass; and
8. an independently selected dimensional scale or a proof that only the ratio \(\Delta_*/\Lambda_{\mathrm{YM}}\) is claimed.

Failure of item 5 leaves a useful scalar-channel bridge but not the mass-gap theorem. Failure of items 2 or 4 leaves a poetic cosmological analogy rather than a common-origin construction.
