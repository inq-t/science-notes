# Spectral Action and Observable Response

The standard almost-commutative spectral action generates Euclidean gravity, gauge, Higgs, and mass terms from represented spectral data. That realization already assumes a spacetime spectral factor. An abstract spectral trace need not assume clock time or a manifold, so an internal spectral selector remains a legitimate deeper construction to investigate. What cannot be inferred from the trace alone is its physical interpretation, a state law, a relative response floor, or the Yang--Mills mass gap.

## The spectral datum

A spectral triple consists of an involutive algebra \(\mathcal A\) represented on a Hilbert space \(\mathcal H\) and a self-adjoint operator \(D\) such that

$$
(1+D^2)^{-1/2}
\text{ is compact},
\qquad
[D,a]\text{ is bounded for }a\in\mathcal A.
$$

An even triple has a grading \(\gamma\) commuting with \(\mathcal A\) and anticommuting with \(D\). A real triple adds \(J\), the opposite-algebra action, and the appropriate \(KO\)-dimensional sign rules. [[library/ncg-standard-model-neutrino-mixing/inq|The local Connes source]] explicitly treats \(D\) as the representative of the \(KO\)-homology fundamental class.

For a real triple, an inner fluctuation has the form

$$
A=\sum_i a_i[D,b_i],
\qquad
A=A^*,
\qquad
D_A=D+A+\varepsilon'JAJ^{-1}.
$$

These fluctuations generate gauge and Higgs fields in the almost-commutative Standard Model construction. They change the represented metric while remaining bounded perturbations of the fundamental cycle under the standard hypotheses.

## What the spectral action calculates

For an even positive test function \(f\), a scale \(\Lambda\), and hypotheses making \(f(D_A/\Lambda)\) trace class,

$$
\boxed{
S_\Lambda(D_A)
=\operatorname{Tr}f(D_A/\Lambda).}
$$

In four-dimensional almost-commutative geometry, its heat-kernel expansion contains:

- an \(a_0\Lambda^4\) volume or cosmological term;
- an \(a_2\Lambda^2\) Einstein--Hilbert and mass sector; and
- an \(a_4\) sector containing curvature squared, Yang--Mills, Higgs kinetic, nonminimal curvature, and Higgs-potential terms.

The explicit formula in [[library/ncg-standard-model-neutrino-mixing/inq|the local source]] returns the Euclidean Standard Model coupled to gravity after the four-manifold \(M\), finite geometry \(F\), inner fluctuation, cutoff scale, and test-function moments have been supplied.

This is a major structural achievement. It is not a derivation of spacetime from the finite algebra. The construction begins with

$$
D=D_M\otimes\mathbf1+\gamma_M\otimes D_F.
$$

Nor does the spectral trace define a positive information metric. Its Hessian can have either sign, whereas BKM response is positive after the physical quotient.

## When it belongs downstream of the wall

The ordinary almost-commutative physical interpretation requires:

- a represented operator with a spectrum that can be counted;
- a trace or regularized trace;
- a resolution scale \(\Lambda\);
- a test function and its moments;
- a Euclidean-to-Lorentzian prescription; and
- a domain of fields or histories to vary.

The principle of stationary action may govern the observable geometry produced after descent. Nothing in the definition requires the pre-observable algebraic ground itself to be a history selected by extremizing \(S_\Lambda\). In this programme this observable spectral action is therefore a consumer of wall realization, not its ontological cause.

This boundary does not exclude a separately defined **atemporal internal spectral selector** on a moduli category of internal Dirac data. Such a functional could select or weight mathematical objects without presupposing temporal evolution. [[algebra/real-forms-and-factive-spacetime|The real-form realization note]] states that possibility. It would not be this observable action unless a functor transported the internal datum, trace, cutoff, and variational problem to the realized geometry, and it would not orient time without the independent fact-and-record process.

This also retypes spectral-action symmetry breaking. A \(G\)-invariant potential can have a minimum with stabilizer \(H\subset G\). The functional remains \(G\)-invariant while a selected minimizing representative is only \(H\)-invariant. That is conventional observable symmetry breaking. Within one fixed triple, the corresponding persistence question is answered by the \(K\)-homology or cyclic class in [[spectral-wall-descent/index-and-curvature-transgression|index and curvature transgression]]. Persistence across a wall that changes the algebra additionally requires an explicit \(KK\)-correspondence or pushforward.

## The unbroken gauge Hessian has no automatic infrared floor

The pure gauge term recovered from the four-dimensional \(a_4\) coefficient has, at a flat trivial connection and with a positive invariant Lie-algebra inner product, quadratic action

$$
S_g^{(2)}(a)=\frac{1}{2g^2}\|da\|_{L^2}^2,\qquad
K_g=g^{-2}d^*d.
\tag{SA1}
$$

This operator acts on **connection perturbations**, not on the physical vacuum Hilbert space. Gauge directions \(a=d\phi\) are null. On transverse Fourier modes \(p\cdot\widehat a=0\), its eigenvalue is \(g^{-2}|p|^2\). A fixed finite torus supplies a lowest nonzero momentum; as its side \(R\) grows, that value is \(g^{-2}(2\pi/R)^2\to0\), even after harmonic modes are removed.

There is a more general **[EXACT QUADRATIC OBSTRUCTION]**. Suppose the stationary-background Hessian on \(\mathbb R^4\) is translation invariant, has matrix symbol \(K(p)\) continuous at zero, and satisfies the linear gauge identity

$$
K(p)(p\otimes X)=0
\quad\text{for every Lie-algebra vector }X.
\tag{SA2}
$$

For any direction \(n\), set \(p=\varepsilon n\), divide by \(\varepsilon\), and take the limit. Then \(K(0)(n\otimes X)=0\) for all \(n,X\), so \(K(0)=0\). If the form is nonnegative, normalized transverse wave packets with Fourier support in shrinking annuli about zero have Rayleigh quotients tending to zero. No positive \(L^2\) floor survives on this quadratic gauge quotient.

The usual rotation-invariant form is

$$
K_{\mu\nu}(p)
=(|p|^2\delta_{\mu\nu}-p_\mu p_\nu)
F(|p|^2/\Lambda^2),
\tag{SA3}
$$

with a color coefficient understood. Every finite local derivative expansion with \(F\) bounded near zero meets the obstruction. Adding a UV scale or more regular derivative terms does not by itself remove long-wavelength modes.

This is not limited to a truncated heat expansion. [[library/spectral-action-beyond-the-weak-field-approximation/inq|Iochum, Levy, and Vassilevich]] compute the noncompact, reference-subtracted action to second order in curvature with full momentum dependence. In their \(f(D^2/\Lambda^2)\) convention, equation (29) gives, for admissible \(f\) continuous at zero,

$$
w_\Lambda(0)=-\tfrac23 f(0).
\tag{SA4}
$$

The apparent \(1/p^2\) is removable: writing \(u=\alpha(1-\alpha)\), the integrand tends to \(f(0)(1-2u)\). Their anti-Hermitian curvature convention accounts for the negative sign. This is an infrared-regular quadratic example, not a theorem about every spectral triple or cutoff. Their noncompact action is the trace of an operator difference, not subtraction of two separately finite traces.

The hypotheses matter. A nonlocal transverse kernel \(\mu^2P_T(p)\), with \(P_T=I-pp^T/|p|^2\), is gauge invariant at quadratic order and has a positive transverse floor, but is not continuous at zero. A nonzero internal Higgs background can also add \(\|[a,\Phi_0]\|^2\); (SA1) addresses the unbroken directions commuting with \(\Phi_0\), not those massive directions. Exact finite-torus spectral traces can contain holonomy terms not captured by the infinite-volume symbol.

Most importantly, a bare Hessian is an inverse covariance only for a Gaussian law. The [[basic-concepts/hessians/inq|effective-action Hessian]] is a different object in an interacting theory. These statements neither disprove the nonperturbative Yang--Mills gap nor prove that a singular gauge propagator would establish it. They locate the missing mechanism beyond the bare quadratic return.

## A relative spectral construction, not a scalar substitution

A useful deeper candidate must retain at least the typed data

$$
\mathfrak S_c=
(\mathcal A,\mathcal H_{\rm spec},D;\,
 \mathcal B_c\hookrightarrow\mathcal A,\omega_c,\partial_c,\mathsf s_c),
\qquad
\partial_c:\mathcal D_c\subset L^2(\mathcal B_c,\omega_c)
\longrightarrow\mathcal K_c.
\tag{SA5}
$$

Here \(\mathcal H_{\rm spec}\) carries the spectral triple; \(\mathcal D_c\) is a dense domain of observable GNS classes; \(\mathcal K_c\) carries their response; and \(\mathsf s_c\) records normalization or a scale section. They are not one Hilbert space by notation. The state and response must be constructed from the proposed whole-to-local law; (SA5) records required types, not independent freely fitted parameters.

If \(\partial_c\) is closable and descends through the GNS null ideal, the squared norm of its closure defines \(L_c=\overline{\partial_c}^{\,*}\overline{\partial_c}\). [[contemporary-puzzles/yang-mills-mass-gap/carrier-first-reversal|The carrier-first construction]] owns this representation step. A spectral action could help select the upstream data or define a regulated weight, but a scalar functional alone supplies neither a normalized measure nor a physical vacuum. Recovering its classical Yang--Mills term is one test; recovering that theory's state, observables, and translations is another.

[[finite-spectral-wall|The finite relative-spectrum witness]] proves why the context in (SA5) cannot be omitted. Its entire bulk Dirac spectrum stays fixed while the centered response floor is \(4\sin^2(2\theta)\), including zero. Selecting the commutant as the readout and using the same Dirac commutator as response instead annihilates every retained observable. A second, relatively placed response structure is needed in that construction.

For a physical gap, a dimensionless lower bound for \(L_c\) must survive on a source-complete carrier and reach the reconstructed translation generator through the [[global-local-response-reconstruction/qft-recovery-contract|QFT recovery contract]]. [[lorentzian-spectral-envelope/inq|The transfer/energy dictionary]] then converts a common inverse-length exponent \(\sigma_*>0\) into \(\Delta_E\ge\hbar c\,\sigma_*\) and, with the required Poincare spectrum, a mass floor \(\hbar\sigma_*/c\). Equality requires the optimal complete-carrier exponent. This conversion is not a derivation of its yardstick.

The new [[rg-covariance-residue/endpoint-averages-and-quadratic-ultraviolet-control|Gaussian blocking estimate]] supplies one local-sector recovery test: a suitable gauge-compatible averaging map preserves curvature control through arbitrary blocking depth. [[rg-covariance-residue/normalized-gauge-kernels-and-markov-residues|Normalized gauge kernels]] supply an exact finite-law comparison without declaring probabilistic weights to be ontological dice. Neither commits the upstream theory to Yang--Mills action as primitive; neither supplies its missing interacting infrared estimate.

## The conjugacy-orbit no-go

For every unitary \(U\), functional calculus and cyclicity of the trace give the **[EXACT ORBIT IDENTITY]**

$$
\boxed{
S_\Lambda(UD_AU^*)
=S_\Lambda(D_A).}
$$

In the finite tracial identification, fix an observable context \(\mathcal B\subseteq\mathcal A\) and its trace-preserving conditional expectation \(E\), which then acts on density matrices. In general,

$$
\Sigma_E(U\rho U^*)
=D(U\rho U^*\Vert E(U\rho U^*))
$$

varies with \(U\). [[spectral-wall-descent/finite-spectral-wall|The finite matrix calculation]] gives an explicit family for which the spectral action is constant while the entropy defect ranges from zero to \(\ln2-h_2(p)\).

For a general von Neumann algebra, \(E\) acts on observables and the descended state is written using the appropriate predual map; the density-matrix notation above is not transferred to that setting without construction.

Therefore no universal scalar function \(F\) can satisfy

$$
\Sigma_E(\rho)
=F(S_\Lambda(D))
$$

even in the smallest finite model. If gravity is the geometric image of wall entropy, it cannot be the bulk spectral-action value alone. It must depend on relative data such as

$$
(D_A,\mathcal B\subseteq\mathcal A,E,\rho),
\qquad
\operatorname{Cone}(\mathcal B\hookrightarrow\mathcal A),
$$

or a boundary connection and its curvature.

## A useful negative entropy calculation

The normalized heat state

$$
\rho_t=\frac{e^{-tD_A^2}}{\operatorname{Tr}e^{-tD_A^2}}
$$

has entropy

$$
S(\rho_t)
=\log Z(t)-t\partial_t\log Z(t).
$$

[[spectral-wall-descent/heat-entropy-no-go|The heat-entropy calculation]] shows that its term linear in \(a_2\) cancels exactly. Ordinary normalized heat entropy therefore does not reproduce the Einstein--Hilbert coefficient at first subleading order; \(a_2\) reappears only quadratically at the next order. This rules out the simplest version of “spectral entropy is gravity.”

An unnormalized resolution-weighted multiplicity

$$
\mathfrak E(t)
:=\operatorname{Tr}\bigl[(1+tD_A^2)e^{-tD_A^2}\bigr]
$$

does retain \(a_2\). It may be investigated as a defect anti-information functional, but it is not von Neumann entropy and currently has no derived wall interpretation.

## What Connes' construction contributes

The most useful lessons are structural:

- zero metric dimension does not prevent rich internal metric data;
- gauge and Higgs fields can be inner metric fluctuations;
- a twisted fixed algebra can be reached by a canonical expectation while its singlet is normal to that fixed locus;
- one finite Dirac block can control several apparently different observable couplings;
- a \(K\)-homology class can persist while represented metric data changes; and
- the spectral action can package gravity and matter after an observable geometry exists.

[[spectral-wall-descent/twist-fixed-point-wall|The twisted fixed-point wall]] extracts the noninvertible expectation from the published twist without using action minimization as the wall law. The strongest local common-source example is the Majorana block \(M_R\). [[spectral-wall-descent/majorana-response-jacobian|Its response Jacobian]] makes the simultaneous dependence of gravitational, cosmological, Higgs, and neutrino sectors exact, while [[spectral-wall-descent/majorana-square-and-cosmic-pulse|its square completion]] separates a positive response orbit from a central residual. These remain downstream relationships.

[[spectral-wall-descent/response-determinant|The response--determinant bridge]] gives one controlled way for the same hidden operator to generate a positive Gaussian BKM Hessian and, after regularization, an observable action. The regulator and absolute determinant normalization remain independent data, so this bridge does not reverse the register order.

## Failure conditions

- If the proposed wall map is unitary or invertible, it does not encode genuine loss; a \(KK\)-equivalence alone also supplies no nonzero relative \(K\)-class, though it does not rule out every metric defect.
- If the output triple still imports \(M\), it has not derived spacetime.
- If a spectral-action Hessian is called BKM without a proof, positivity and type have been confused.
- If the unbroken bare gauge Hessian is assigned a uniform infrared floor while its Fourier symbol remains continuous at zero, (SA2) rules out that assignment; this is not a no-gap theorem for the interacting physical carrier.
- If context-dependent entropy is inferred from the conjugacy-invariant bulk action, the finite orbit counterexample applies.
- If heat entropy is used to derive Einstein gravity, the \(a_2\) cancellation must be overcome by a different functional or boundary term.
- If an observable minimum is used as the necessity of the pre-observable ground, the action has been moved across the wall without a descent theorem.

[[spectral-wall-descent/receipts/verify-spectral-wall.py|The finite verification receipt]] checks the relative-floor witness and the removable infrared form-factor limit for \(f(s)=e^{-s}\). It does not construct an interacting quantum law or test a continuum physical gap.
