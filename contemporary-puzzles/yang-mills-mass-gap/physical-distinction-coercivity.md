# Physical Distinction Coercivity

Measurement and the Yang--Mills mass gap share one exact carrier-level grammar, but not one mechanism. A projection supplies an exclusive question, a state supplies probabilities, an instrument supplies outcome-conditioned state change, and a Hamiltonian form assigns energy to physical departures from the vacuum. The mass gap is the uniform coercive cost of every such departure. The most concrete operator-algebraic route is staged: tempered Connes--Takesaki core maps, or another declared comparison functor, first place different regulator presentations on comparable carriers; Connes cocycles may then compare faithful reference states on one such carrier; and Takesaki's modular-invariance criterion can supply vacuum-preserving conditional expectations on an admissible regulator or comparison carrier. Ordinary proper nested AQFT region algebras cannot supply such a tower in the vacuum representation under Reeh--Schlieder hypotheses. Only an independently constructed Hamiltonian-form estimate can charge the surviving distinction shells.

**Status: [EXACT CENTERED GNS CARRIER; CONDITIONAL SHELL THEOREM; OPEN PHYSICAL CONSTRUCTION].** The centered GNS space, projection identities, spectral-gap equivalence, Takesaki existence gate, and orthogonal-shell implication are exact under the stated hypotheses. The centered carrier becomes physical only after gauge reduction, vacuum selection, and time realization. Constructing a regulator-natural filtration from four-dimensional Yang--Mills data, proving uniform shell coercivity without assuming the gap, and passing it to a nontrivial continuum theory remain open.

## What the polarizer actually separates

For one photon in an idealized two-mode polarization carrier, choose a linear analyzer direction \(\phi\) and write

$$
P_\phi=|\phi\rangle\langle\phi|,
\qquad
P_\phi^\perp=1-P_\phi.
$$

For the pure linear-polarization state \(|\theta\rangle\),

$$
\Pr(\mathrm{transmit})
=
\langle\theta|P_\phi|\theta\rangle
=
\cos^2(\theta-\phi),
$$

$$
\Pr(\mathrm{orthogonal\ channel})
=
\sin^2(\theta-\phi).
$$

An absorptive polarizer realizes transmit versus absorb; a polarizing beam splitter can realize two output channels. In either case, the binary structure comes from

$$
P_\phi^2=P_\phi,
\qquad
\sigma(P_\phi)\subseteq\{0,1\}.
$$

Call this a dimensionless **logical or projective gap**. It says that the selected question has two exclusive values. It says nothing about the spectrum of the physical Hamiltonian. Quantum formalism represents the input by a ray and assigns a probability law in each chosen context; it does not itself supply a simultaneous context-independent valuation of every possible polarization question. Bell's theorem enters for correlations between separated systems, while the standard Kochen--Specker theorem requires Hilbert dimension at least three. Under their respective hypotheses they constrain attempts to replace quantum probabilities by local or noncontextual predetermined values; neither turns the projection identity into a mass-gap theorem.

For a sharp measurement, the closest literal overlap is spectral:

$$
\text{measurement event: }E_A(B),
\qquad
\text{mass gap: }E_H((0,\Delta))=0.
$$

Both statements use spectral projections. The second says that an ideal energy measurement has no possible value strictly between the vacuum and \(\Delta\). It does not say that the spectrum above \(\Delta\) is discrete; a continuous spectrum may begin at the threshold. Nor does either spectral statement say that an outcome has actually occurred.

Their independence is already exact in two dimensions. On one fixed carrier take

$$
P=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
H_\varepsilon=
\begin{pmatrix}
0&0\\
0&\varepsilon
\end{pmatrix}.
$$

The yes/no spectrum of \(P\) remains \(\{0,1\}\), while the Hamiltonian gap is the independently chosen \(\varepsilon>0\). No algebraic manipulation of the projector's unit separation can supply the dimensional energy scale.

## The common carrier of observable distinctions

Let \((\mathfrak A,\omega)\) have GNS representation

$$
(\pi_\omega,\mathcal H_\omega,\Omega_\omega).
$$

Define the centered observable-distinction space

$$
\boxed{
\mathsf{Dist}_\omega(\mathfrak A)
:=
\overline{
\left\{
(\pi_\omega(a)-\omega(a)1)\Omega_\omega:
a\in\mathfrak A
\right\}}
=
\mathcal H_\omega\ominus\mathbb C\Omega_\omega.
}
$$

The equality follows from cyclicity of \(\Omega_\omega\). When \(\mathfrak A=\mathfrak A_{\mathrm{phys}}\), this is a carrier of physical Hilbert distinctions relative to the state, not yet a set of facts. For a projection \(p\in\mathfrak A\),

$$
\left\|
(\pi_\omega(p)-\omega(p)1)\Omega_\omega
\right\|^2
=
\omega(p)(1-\omega(p)).
$$

The projection supplies a yes/no question, the state supplies its weight, and the GNS norm detects whether that question distinguishes anything in the state.

Suppose physical time translations are implemented with positive generator \(H\),

$$
U(t)=e^{-itH/\hbar},
\qquad
H\Omega_\omega=0,
$$

and define the closed Hamiltonian form

$$
\mathfrak h[\Psi]
:=
\|H^{1/2}\Psi\|^2.
$$

If the vacuum line is the whole kernel, define the bottom of the nonvacuum spectrum by

$$
\boxed{
\Delta_*
:=
\inf_{\substack{
\Psi\in D(\mathfrak h)\cap\mathsf{Dist}_\omega(\mathfrak A)\\
\|\Psi\|=1
}}
\mathfrak h[\Psi]
=
\inf\sigma\!\left(H\big|_{\Omega_\omega^\perp}\right).
}
$$

The theory has a mass gap exactly when \(\Delta_*>0\). For every \(0<\Delta\leq\Delta_*\),

$$
\mathfrak h[\Psi]
\geq
\Delta\|\Psi\|^2,
\qquad
\Psi\in
D(\mathfrak h)\cap\mathsf{Dist}_\omega(\mathfrak A).
$$

For centered observables whose GNS vectors lie in the form domain, the same lower bound becomes

$$
\boxed{
\left\|
H^{1/2}(\pi_\omega(a)-\omega(a)1)\Omega_\omega
\right\|^2
\geq
\Delta
\left(
\omega(a^*a)-|\omega(a)|^2
\right).
}
$$

This is the exact content of the phrase **positive energetic infimum of an observable distinction**. The infimum need not be an attained eigenvalue. It does not mean that a detector click costs at least \(\Delta\), and it does not turn a probability law into an actual fact. It says that no normalized physical vector orthogonal to the vacuum can have arbitrarily small energy.

## Four meanings of distinction

The word must be firewalled across four carriers.

| Distinction | Carrier and map | What it means |
|---|---|---|
| gauge-vertical difference | \(F-E_{\mathcal G}F\) before the physical quotient | redundant presentation removed by Gauss descent |
| physical Hilbert distinction | \(\Psi\in\mathcal H_{\mathrm{phys}}\ominus\mathbb C\Omega\) | a nonvacuum physical direction to which gap coercivity applies |
| statistical score | \(\dot\nu=f\nu\), or its Hellinger image \(f\sqrt\nu\) | a real commuting presentation of selected state tangents |
| factive distinction | an obtained outcome, represented by a character only for an appropriate sharp atomic context, together with a persistent record | one contextual alternative that actually obtains |

The finite-regulator Fisher identity in [[gauge-descent-flux-fisher-coercivity]] realizes the third row inside a real multiplication sector of the second. It does not cover phase directions or the full noncommutative quantum tangent. [[sufficient-reason/quantum-interpretations|Quantum interpretation and the type change]] and [[conservation-of-causal-charge/factive-descent-and-records|factive descent and records]] own the fourth row.

This yields three compact questions:

$$
\begin{aligned}
\text{measurement asks:}&\quad
\text{which contextual distinction became factual?}\\
\text{superselection asks:}&\quad
\text{which distinctions can coexist coherently?}\\
\text{mass gap asks:}&\quad
\text{is the energetic infimum of physical distinction positive?}
\end{aligned}
$$

None of these predicates implies either of the others. A gapless theory can have discrete spin or polarization outcomes; a gapped theory can have observables with continuous spectrum; a superselection sector can be gapless; and a unique gapped vacuum need not solve the outcome problem.

[[mass-as-casimir-and-realization]] adds the representation-theoretic reason for this independence: momentum generates translations, mass is their Poincare Casimir, phase selection chooses a state or representation, and outcome actualization points within a readout context. These roles can coexist on one physical carrier without being one operator.

## The operator-signature ledger

The reversal tactic begins by asking what each operator operates on. Similar-looking arrows must not be composed until their carriers and codomains match.

| Operation | Operates on | Returns | Does not return |
|---|---|---|---|
| compact gauge average \(E_{\mathcal G}:\mathfrak F\to\mathfrak F^{\mathcal G}\), when available | field-algebra presentations | a gauge-invariant observable | a vacuum, excitation energy, or fact |
| event projection \(E_A(B):\mathcal H_{\mathrm{phys}}\to\mathcal H_{\mathrm{phys}}\) | physical state vectors | the subspace for one sharp proposition | an obtained outcome or an energy scale |
| instrument operation \(\mathcal I_\Delta:\mathfrak M\to\mathfrak M\) and its predual | observables and normal states | an outcome-indexed subnormalized posterior functional | which outcome obtains or a persistent record |
| conditional expectation \(E_j:\mathfrak M\to\mathfrak N_j\) and GNS projection \(\widehat E_j\) | observables and their declared \(L^2\) carrier | a retained algebra and orthogonal kept/forgotten decomposition | physical time or the energetic cost of the forgotten part |
| Hamiltonian \(H:D(H)\to\mathcal H_{\mathrm{phys}}\) and form \(\mathfrak h\) | physical vectors in their operator or form domains | time translation and energetic cost | a readout context, outcome, or record |
| core or comparison functor with state-compatible \(L^2\) implementation \(\mathcal J^{(2)}_{r'r}\) | compatible algebra--state presentations and their Hilbert realizations | transport to a comparable carrier | state selection, coercivity, or actuality |

The proposed construction uses the fourth row to decompose an \(L^2\) carrier only after a form-preserving identification with the second-row physical carrier, and the fifth row to charge that decomposition. The first and sixth rows are prior realization machinery; the third is a later measurement arrow. This order is the physical-carrier firewall.

## What a wall can measure without becoming time

Let

$$
E:\mathfrak M\longrightarrow\mathfrak N
$$

be a state-preserving conditional expectation whose GNS implementation \(\widehat E\) is an orthogonal projection on one declared physical \(L^2\) carrier. The operator \(1-\widehat E\) has spectrum contained in the trivial projection values \(\{0,1\}\). That is not a mass scale.

The physically meaningful comparison with the Hamiltonian form is instead the best constant \(\lambda_E\) in

$$
\boxed{
\mathfrak h[\Psi]
\geq
\lambda_E
\|(1-\widehat E)\Psi\|^2,
\qquad
\Psi\in D(\mathfrak h).
}
$$

This asks how much physical energy charges the distinctions erased by that particular wall. It is dimensionful because \(\mathfrak h\) is. The expectation supplies the decomposition; the Hamiltonian form supplies the cost. Even after taking the GNS implementation, identifying a proper nontrivial \(\widehat E\) with \(e^{-\tau H/\hbar}\) would fail: the former is idempotent and noninjective, while the latter is an injective semigroup operator at finite \(\tau>0\).

If \(\operatorname{Ran}\widehat E\) contains nonvacuum directions, \(\lambda_E>0\) does not by itself give the global mass gap. The wall has charged one family of distinctions and retained another. This is precisely why a complete filtration is useful.

### Stable inversion of which arrow?

After a physical reconstruction, let \(K\ge0\) be the self-adjoint inverse-length generator with \(\ker K=\mathbb C\Omega\). Fix \(\ell>0\), and work on the nonzero complement \(\mathcal H_0=\Omega^\perp\). The two bounded operators
\[
T_\ell=e^{-\ell K},\qquad
D_\ell=(I-T_\ell^2)^{1/2}
\]
are injective with dense range there. They ask opposite spectral questions. If
\(\sigma=\inf\operatorname{spec}(K|_{\mathcal H_0})\) and
\(M=\sup\operatorname{spec}(K|_{\mathcal H_0})\), functional calculus gives
\[
\inf_{\|\psi\|=1}\|T_\ell\psi\|^2=e^{-2\ell M},
\qquad
\inf_{\|\psi\|=1}\|D_\ell\psi\|^2=1-e^{-2\ell\sigma},
\]
with \(e^{-\infty}=0\). A bounded inverse on the range, equivalently closed range here, therefore means
\[
\boxed{
\begin{aligned}
\text{stable inversion of }T_\ell
&\ \Longleftrightarrow\ M<\infty
&&\text{(an ultraviolet ceiling)},\\
\text{stable inversion of }D_\ell
&\ \Longleftrightarrow\ \sigma>0
&&\text{(an infrared gap)}.
\end{aligned}}
\]
The bounded-below criterion proves both implications; dense closed range is the entire carrier.

On \(\mathbb C\Omega\oplus\ell^2(\mathbb N)\), \(Ke_n=ne_n\) has a gap but no bounded transfer inverse, whereas \(Ke_n=n^{-1}e_n\) has a bounded transfer inverse but no gap. These are exact operator examples, not candidate relativistic theories. A mass gap is an upper bound below one on vacuum-reduced transfer, or a positive lower bound on its defect—not a lower bound on transfer itself.

This \(D_\ell\) is a spectral diagnostic defined **after** \(K\). It cannot be advertised as an independently constructed wall. [[global-local-response-reconstruction/quantitative-descent-and-the-shape-of-a-gap#A constructive quantitative gluing map|The quantitative gluing theorem]] instead requires bounded recovery from its actual upstream response defect, followed by comparison with physical transfer. Stable cross-fiber transport alone supplies neither condition. Simultaneous rescaling \(K\mapsto aK,\ \ell\mapsto\ell/a\) preserves both operators and does not decide whether either edge is positive.

## The operator-algebraic contribution: transport first, shells second

The Connes--Takesaki contribution is the prior comparison problem. Tempered arrows and their canonical-core maps, or another explicitly constructed comparison functor, can compare different regions or regulators as described in [[wall-construction-interface/cross-fiber-transport|cross-fiber transport]]. Only after two faithful states have been placed on one von Neumann algebra can a relative Connes cocycle compare their modular presentations. These constructions do not select a state, produce an expectation, or prove a gap. Every algebra or core comparison used below must have a state-compatible Hilbert implementation

$$
\mathcal J^{(2)}_{r'r}:\mathcal H_r\longrightarrow\mathcal H_{r'},
$$

unitary or isometric when that is the declared comparison, or an admissible identification map in a specified generalized-Hilbert-space convergence scheme. If the filtrations are to define one continuum object rather than unrelated regulator-wise choices, these implementations and shell relabelings \(\phi_{r'r}\) must satisfy an exact or controlled asymptotic naturality law such as

$$
\mathcal J^{(2)}_{r'r}\widehat E_{r,j}
=
\widehat E_{r',\phi_{r'r}(j)}\mathcal J^{(2)}_{r'r}.
$$

An analogous cocycle-naturality condition is required when the faithful reference state is changed. Without these comparison laws, the construction below is Takesaki theory on separately chosen carriers, not yet a Connes--Takesaki continuum architecture.

On one fixed carrier, the promising role of modular theory is to construct expectations, not to rename modular flow as physical time. There are two controlled candidate carriers:

1. At finite regulator, use the commutative ground-state-transformed algebra

   $$
   \mathfrak M_{r,0}=L^\infty(X_r,\nu_r)
   $$

   on \(L^2(\nu_r)\), where \(\nu_r\) has full support in the declared measure class, and use the ground-state unitary \(U_{0,r}\) to identify its form with the gauge-invariant Hamiltonian form.
2. In a noncommutative comparison route, use a support-reduced, RG, core, or other von Neumann carrier on which the reference state is faithful normal. It cannot simply be a proper tower of ordinary vacuum local-region algebras: Reeh--Schlieder cyclicity and separation would force every vacuum-preserving expectation in that tower to be trivial. A pure vacuum vector state on the full \(B(\mathcal H_{\mathrm{phys}})\) is not faithful when \(\dim\mathcal H_{\mathrm{phys}}>1\). An explicit form-preserving map to the full physical vacuum carrier is therefore required.

Let \(\omega_r\) denote the faithful normal reference state on the chosen \(\mathfrak M_{r,0}\), and suppose there is a decreasing filtration

$$
\mathfrak M_{r,0}
\supseteq
\mathfrak M_{r,1}
\supseteq
\mathfrak M_{r,2}
\supseteq\cdots
$$

such that every member is invariant under the same modular flow,

$$
\sigma_t^{\omega_r}(\mathfrak M_{r,j})
=
\mathfrak M_{r,j}.
$$

[[library/conditional-expectations-in-von-neumann-algebras/inq|Takesaki's conditional-expectation theorem]] then supplies the \(\omega_r\)-preserving normal expectations

$$
E_{r,j}:\mathfrak M_{r,0}\longrightarrow\mathfrak M_{r,j}.
$$

Their GNS implementations \(\widehat E_{r,j}\) are orthogonal projections. For a nested family, uniqueness gives the required composition law, and the martingale differences

$$
D_{r,j}
:=
\widehat E_{r,j}-\widehat E_{r,j+1}
$$

are mutually orthogonal. Call such a family a **Takesaki-admissible distinction filtration**.

This terminology declares a sufficient architecture, not a necessary property of every gapped Yang--Mills theory. Modular invariance of useful gauge-local subalgebras is a severe condition and may fail. More sharply, [[causal-frame-coercivity#Conditional-expectation shells|the local-expectation no-go]] proves that proper vacuum-preserving expectations between ordinary nested AQFT region algebras are impossible under the standard cyclic/separating hypotheses. In the finite ground-state-transformed commutative carrier, ordinary conditional expectations onto sub-\(\sigma\)-algebras are easier to obtain; compatibility with gauge locality and electric flux remains the hard part.

### The anti-tautology gate

The filtration does no work merely by existing. The two-step family

$$
\mathfrak M_{r,0}\supset\mathbb C1
$$

is always available for a faithful state, and its only shell is \(I-P_{0,r}\). Its shell inequality is therefore exactly the desired mass-gap inequality with new notation. Likewise, a gap known in advance would supply the uniform shell bound for any orthogonal filtration.

To become a noncircular proof architecture, the admissible filtration must instead be:

- gauge-local or RG-defined from regulator geometry, subregions, gauge constraints, and declared coarse-graining data;
- natural under the regulator and state-frame comparison maps above;
- frozen before using the target spectrum, clustering rate, or glueball data; and
- free of nonvacuum spectral projections of \(H_r\), gap-derived vacuum decay, or any other input equivalent to the desired lower bound; the independently constructed vacuum line needed to define the centered carrier is not excluded.

Each \(c_{r,j}\) must then be estimated from independently controlled kinetic geometry, plaquette interaction, orbit density, gauge constraints, and RG data. Until this is done, the filtration is a decomposition of the missing inequality, not its mechanism.

Let \(H_r\) be the regulated physical Hamiltonian with ground energy \(E_{0,r}\), and set

$$
K_r:=H_r-E_{0,r}\geq0,
\qquad
\mathfrak h_r[\Psi]
:=
\|K_r^{1/2}\Psi\|^2.
$$

Require

$$
K_r\Omega_r=0,
\qquad
\ker K_r=\mathbb C\Omega_r,
\qquad
P_{0,r}:=E_{K_r}(\{0\}).
$$

Suppose the filtration is complete at this same vacuum,

$$
\widehat E_{r,0}=I,
\qquad
\widehat E_{r,j}\xrightarrow[j\to\infty]{\mathrm{strong}}P_{0,r},
$$

so that

$$
\sum_j\|D_{r,j}\Psi\|^2
=
\|(1-P_{0,r})\Psi\|^2.
$$

Equivalently,

$$
\bigcap_j\operatorname{Ran}\widehat E_{r,j}
=
\mathbb C\Omega_r.
$$

Let \(r=(a,L)\) run along one specified tuned RG trajectory in scheme \(\mathsf s\). Here \(\Lambda_{\mathrm{YM}}^{(\mathsf s)}\) denotes an **energy** yardstick; if another convention registers \(\Lambda\) as inverse length or mass, the required factor of \(\hbar c\) or \(c^2\) must be restored. The coefficients \(c_{r,j}\) and \(\gamma_{\mathsf s}\) are dimensionless, and the yardstick is fixed by the declared RG convention rather than defined from the gap.

At finite regulator, the exact ground-state unitary identifies \(\mathfrak h_r\) with the weighted electric-flux Dirichlet form. In a proposed continuum route, calling the form *electric flux* additionally requires renormalized derivations, closability, and a form-preserving OS or direct-Hamiltonian identification. The abstract shell implication itself needs only the physical Hamiltonian form. Its target is

$$
\boxed{
\mathfrak h_r[\Psi]
\geq
\Lambda_{\mathrm{YM}}^{(\mathsf s)}
\sum_j c_{r,j}\|D_{r,j}\Psi\|^2,
\qquad
c_{r,j}>0,
\quad
\Psi\in D(\mathfrak h_r),
\qquad
\inf_{r,j}c_{r,j}
=
\gamma_{\mathsf s}>0.
}
$$

This is one **joint** form estimate. \(L^2\)-orthogonality of the \(D_{r,j}\) does not make the Hamiltonian form diagonal and does not permit separate estimates for \(\mathfrak h_r[D_{r,j}\Psi]\) simply to be summed. A shell-by-shell proof must additionally show that every \(D_{r,j}\) preserves \(D(\mathfrak h_r)\), that distinct shells are form-orthogonal, and that the partial shell sums converge to \((1-P_{0,r})\Psi\) in form norm with the required uniform tail control; equivalently, it may prove a form-domain orthogonal direct-sum identity. A quantitative bound on all cross-terms and tails is another sufficient route. Otherwise the joint estimate must be proved directly.

Orthogonality immediately gives

$$
\mathfrak h_r[\Psi]
\geq
\gamma_{\mathsf s}
\Lambda_{\mathrm{YM}}^{(\mathsf s)}
\|(1-P_{0,r})\Psi\|^2,
\qquad
\Psi\in D(\mathfrak h_r).
$$

If \(\Lambda_{\mathrm{YM}}^{(\mathsf s')}=q\,\Lambda_{\mathrm{YM}}^{(\mathsf s)}\), the same already-established numerical lower bound can be re-registered by choosing \(\gamma_{\mathsf s'}=q^{-1}\gamma_{\mathsf s}\). This is not a forced transformation law for independently constructed, possibly nonoptimal shell constants. The physical spectral quantity is \(\Delta_*\); a shell bound becomes scheme-covariant only after naturality of the filtration and covariance or optimality of its constants have been proved.

For the continuum passage, put

$$
\widehat{\mathfrak h}_r
:=
\frac{\mathfrak h_r}{\Lambda_{\mathrm{YM}}^{(\mathsf s)}}.
$$

The same \(\mathcal J^{(2)}_{r'r}\) identifications used for filtration naturality must define the comparison of the varying Hilbert carriers. Generalized Mosco convergence of \(\widehat{\mathfrak h}_r\), generalized-strong convergence of \(P_{0,r}\), and recovery sequences for every limiting form-domain vector then pass the uniform form inequality to the limit. Strong resolvent convergence without vacuum-projection control is not enough.

This is the precise bridge from a **multiscale observational filtration** to a **gap**:

$$
\boxed{
\begin{aligned}
\text{nested physical readout or coarse-graining algebras}
&\longrightarrow
\text{orthogonal distinction shells},\\
\text{physical Hamiltonian form}
&\longrightarrow
\text{joint coercive control of every shell},\\
\text{uniform positive shell cost}
&\longrightarrow
\text{global vacuum coercivity}.
\end{aligned}}
$$

[[paired-scale-filtrations-and-the-invariant-incidence-wall]] extracts an exact address operator from this shell grammar. One resolution tower whose addresses are unbounded above produces a gapless inverse-scale operator, so stopping a single filtration cannot explain mass. Two cross-commuting filtrations instead produce a joint incidence support; a positive floor for their invariant product is equivalent to a diagonal ceiling on the mean shell address. This theorem does not replace the Hamiltonian estimate displayed above. It identifies the algebraic obstruction that must be generated before a separate same-carrier solder can compare the dimensionless incidence operator with the reconstructed Poincare Casimir.

[[compensated-incidence-response-and-four-dimensional-balance]] identifies the exact alternative when the form does not impose a hard support ceiling. If the joint shells reduce a positive response form with bottom coefficients \(\rho_{r,jk}\), then its pullback through the inverse-scale presentation has coefficients \(\rho_{r,jk}e^{-2p\overline N_{r,jk}}\). Uniform coercivity is therefore equivalent to a positive infimum of these compensated coefficients. Without shell reduction the target must remain the single closed-form estimate \(\mathfrak R_r[M_{p,r}f]\geq\kappa^2\|f\|^2\); Hilbert-space shell orthogonality does not remove response-form cross-terms. This types the candidate residue cost without assuming that forgotten information, boundary multiplicity, or entropy already carries energy.

This filtration is not strict Grothendieck descent: strict descent glues equivalent local presentations and need not forget anything. It is the project's observational or coarse-graining use of *descent*. Filtration alone supplies no cost; the Hamiltonian form alone supplies no independently useful multiscale decomposition. Their correctly typed composition is a proposed proof architecture, and becomes a physical mechanism only after the filtration itself has an independent selection and realization theorem.

## The full physical-carrier chain

The construction should run in this order:

$$
\boxed{
\begin{aligned}
(\text{field algebra},\text{gauge groupoid})
&\xrightarrow{\ \text{Gauss/BRST/fixed points and physical quotient}\ }
\mathfrak A_{\mathrm{phys}},\\
(\mathfrak A_{\mathrm{phys}},\omega_0)
&\xrightarrow{\ \mathrm{GNS}\ }
(\pi_0,\mathcal H_0,\Omega_0),\\
(\alpha_t,\omega_0;\text{ continuity, invariance, positive energy})
&\longrightarrow
(U(t),H,\mathfrak h),\\
(\mathfrak h,\{E_j\})
&\longrightarrow
\text{shell coercivity or its failure},\\
\mathfrak h
&\longrightarrow
(\partial,\Gamma,d_{\mathfrak h})
\quad\text{when the Dirichlet hypotheses hold}.
\end{aligned}}
$$

The first arrow is a construction obligation, not something the groupoid performs automatically; [[program-core/physical-quotient|the physical quotient]] owns its probe-relative and noncircular conditions. The action groupoid, stack, or crossed product may be needed to retain stabilizers, flux sectors, topology, and state-frame comparison that a coarse fixed-point spectrum forgets. A [[basic-concepts/torsors/inq|torsor]] can encode exact relative differences without a preferred origin only after an acting group and a free transitive action have been constructed. Strict [[basic-concepts/descent/inq|descent]] can prove that local presentations constitute one global object. None of these operations selects an outcome, supplies a physical clock, or proves coercivity.

The quasi-local physical \(C^*\)-algebra and the local von Neumann algebras used by Takesaki are also different carriers. Every von Neumann algebra admits an abstract standard form \((\mathfrak M,\mathcal H,J,\mathcal P^\natural)\); what is not automatic is that the chosen vacuum vector supplies the faithful modular realization on that carrier. That requires its restriction to be faithful normal and cyclic-separating in the represented algebra, or a declared passage to an appropriate supported algebra and its faithful GNS realization. An arbitrary global GNS vector does not discharge this condition. Likewise, the dynamics row requires a strongly continuous automorphism group preserving \(\omega_0\), its GNS implementation, and the positive-energy spectrum condition. State invariance alone does not make Stone's generator positive.

For a declared tracially symmetric conservative \(C^*\)-Dirichlet form, or under a specified nontracial KMS/modular derivation theorem with its closability and regularity hypotheses, a gradient correspondence may arise after the form is known. On a dense form \(*\)-algebra \(\mathfrak A_{\mathrm{form}}\subseteq\mathfrak A_{\mathrm{phys}}\), its type is

$$
\partial:\mathfrak A_{\mathrm{form}}\longrightarrow\mathcal H_\partial,
\qquad
\mathcal E_\omega(a,b)
:=
\mathfrak h(\pi_\omega(a)\Omega_\omega,
\pi_\omega(b)\Omega_\omega)
=
\langle\partial a,\partial b\rangle.
$$

A Dirac block built from \(\partial+\partial^*\) or a Connes distance is then additional structure. Connes fusion of sector correspondences is a separate bimodule construction and does not follow from this gradient. These structures may organize geometry, charge transport, or composition; none creates the vacuum form or proves its lower bound without a form-preserving comparison. [[carrier-first-reversal]] owns that acceptance test.

If a measurement claim is also made, append a different arrow:

$$
(\mathfrak A_{\mathrm{phys}},\omega;
\mathfrak D,\mathcal I)
\longrightarrow
\{\widetilde\omega_\Delta,p(\Delta)\}_{\Delta}
\dashrightarrow{\ \text{actuality and record writing}\ }
(\text{obtained outcome},\mathfrak R),
$$

On the standard Hilbert-space carrier \(\mathfrak A_{\mathrm{phys}}=\mathcal B(\mathcal H)\), with normal states and a nondegenerate measured observable, \(\mathcal I\) can be a completely positive instrument in [[library/quantum-measurement-information-and-completely-positive-maps/inq|Ozawa's measurement framework]], while \(\mathfrak D\) is the commutative readout context. The displayed arbitrary-algebra notation is only a typing template; extending it to a local or type-III algebra requires a broader instrument construction. In the Heisenberg convention the first arrow returns the subnormalized posterior functional \(\widetilde\omega_\Delta(a):=\omega(\mathcal I_\Delta(a))\) and its weight \(p(\Delta)=\widetilde\omega_\Delta(1)\). The normalized conditional state \(\omega_\Delta=\widetilde\omega_\Delta/p(\Delta)\) exists only when \(p(\Delta)>0\), or almost everywhere after a declared disintegration. This arrow does not select an outcome or make a record persistent. For a finite atomic sharp readout, an obtained value \(x\) can be represented by a character \(\chi_x\). For continuous or diffuse readouts, point evaluation need not be a normal character and singleton outcomes may have zero probability; measurable events and posterior-state disintegration are the safer types. The dashed arrow therefore requires an actuality rule or primitive datum plus record-writing and stability dynamics. The Hamiltonian gap does not supply it. Conversely, a two-outcome instrument does not supply Hamiltonian coercivity.

## The stopping condition

The corrected stopping discipline in `inbox/operator-signature-verdict/commentary/the-schrodinger-stopping-rule.md` separates mathematical completion from explanatory permission to stop.

### Necessary and sufficient mathematical stop

Once a nontrivial physical Yang--Mills theory, its positive-energy Hamiltonian, and its unique vacuum have been constructed, the whole-carrier inequality

$$
H\geq\Delta(1-P_0)
\quad\Longleftrightarrow\quad
\mathfrak h[\Psi]
\geq
\Delta\|(1-P_0)\Psi\|^2
\quad
(\Psi\in D(\mathfrak h)),
\qquad
\Delta>0,
$$

is necessary and sufficient for the mass gap. A shell filtration, Bakry--Emery curvature bound, Connes distance, \(A_2\) operator, or \(S^6\) geometry is at most a route to this statement.

### Sufficient stopping condition for the shell route

For one fixed compact simple gauge group \(G\), the member must freeze \(G\), the regulator action, the tuned RG trajectory, the topology and boundary conditions, and the admissible filtration class before the spectral estimate is attempted. The fully quantified [[library/quantum-yang-mills-theory/inq|Jaffe--Witten problem statement]] requires the construction for every compact simple \(G\). The shell architecture has succeeded for the fixed member only when all of the following hold:

1. the gauge-invariant regulated carriers, energy forms, physical-unit normalizations, faithful normal states on every algebra where Takesaki's theorem is invoked, and an admissible class of gauge-local regulator-natural filtrations are constructed without using the desired gap or a gap-equivalent estimate;
2. the expectations act as nested orthogonal projections on those same carriers and their terminal intersection is exactly the vacuum line;
3. the shell estimate has one positive lower bound uniform in shell depth, physical volume, and regulator removal;
4. the same \(\mathcal J^{(2)}_{r'r}\) comparison maps identify the carriers and filtrations, the scaled forms converge in the generalized Mosco sense, and the vacuum projections converge generalized-strongly, with recovery sequences sufficient to pass the bound to the limit;
5. the limit is a nontrivial four-dimensional gauge-invariant quantum field theory in an explicitly declared Wightman package, an Osterwalder--Schrader package that reconstructs one, or an at-least-as-strong Haag--Kastler package with locality, Poincare covariance, the joint spectrum condition, and a unique vacuum; its local gauge-invariant observables and short-distance correlations have the required Yang--Mills and asymptotic-freedom correspondence, and the estimate holds on the whole reconstructed vacuum representation rather than merely one selected glueball channel; and
6. Euclidean transfer is identified with physical time by Osterwalder--Schrader reconstruction, or a direct positive-energy Hamiltonian construction is supplied.

### Methodological permission to stop

The operator-signature verdict adds four disciplines that are not hypotheses of the spectral theorem but are required for an explanatory research claim:

- **Rigidity:** the physical package and admissible class of filtrations are fixed as part of a declared signature; one member of that class counts as physical only after an independent selection or correspondence theorem, and arbitrary functions are not changed for each target spectrum.
- **Correspondence:** the abstract shells are shown to live on the gauge-invariant Yang--Mills carrier through a form-preserving map that intertwines their quadratic form with physical energy.
- **Independent return:** \(\gamma_{\mathsf s}>0\), and any claimed ratio beyond positivity, is obtained without having been used to select the filtration or vacuum estimate.
- **Failure contract:** the route is rejected if the expectations are not common-carrier orthogonal projections, their intersection exceeds the vacuum line, \(\inf c_{r,j}=0\), the continuum limit is trivial or loses the bound, physical time is not realized, or the filtration was fitted to the target spectrum.

These are the same anti-flexibility and independent-return tests formalized canonically in [[wall-construction-interface/elimination-test|the elimination tests]]. Factive history is a later layer. It is not required by the Clay theorem. It becomes non-negotiable only if the construction is advertised as a solution to the measurement problem or as an explanation of how probabilities become records.

## The revised philosophical statement

The mass gap is not the gap between the words *either* and *or*. That gap is already present in the idempotence of a question. Nor is it the unexplained leap from a probability measure to one fact. It is the stronger dynamical statement that the physical vacuum complement has no arbitrarily cheap direction.

The proposed unification is therefore not

$$
\text{collapse}=\text{descent}=\text{mass}.
$$

It is

$$
\boxed{
\text{one carrier of distinctions}
+
\text{different arrows for quotient, cost, and fact}.
}
$$

The genuinely new target is to make the wall and the energy form coexist on that carrier. Then a wall can say which distinction is being forgotten, an independently energy-intertwined flux form can say what that distinction costs, and a complete uniformly charged tower can prove that physical difference from the vacuum begins above a positive energy threshold.
