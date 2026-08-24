# The Spectral Action Is an Observable Action

The spectral action is a powerful generator of observable Euclidean gravity, gauge, Higgs, and mass terms from represented spectral data. It should not be projected backward into the pre-observable register as a universal least-action law. Its trace, cutoff, test function, manifold representation, and variational interpretation already belong to an effective observable geometry.

## The spectral datum

A spectral triple consists of an involutive algebra \(\mathcal A\) represented on a Hilbert space \(\mathcal H\) and a self-adjoint operator \(D\) such that

$$
(1+D^2)^{-1/2}
\text{ is compact},
\qquad
[D,a]\text{ is bounded for }a\in\mathcal A.
$$

An even triple has a grading \(\gamma\) commuting with \(\mathcal A\) and anticommuting with \(D\). A real triple adds \(J\), the opposite-algebra action, and the appropriate \(KO\)-dimensional sign rules. [[library/ncg-standard-model-neutrino-mixing/entry|The local Connes source]] explicitly treats \(D\) as the representative of the \(KO\)-homology fundamental class.

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

For an even positive test function \(f\) and a scale \(\Lambda\),

$$
\boxed{
S_\Lambda(D_A)
=\operatorname{Tr}f(D_A/\Lambda).}
$$

In four-dimensional almost-commutative geometry, its heat-kernel expansion contains:

- an \(a_0\Lambda^4\) volume or cosmological term;
- an \(a_2\Lambda^2\) Einstein--Hilbert and mass sector; and
- an \(a_4\) sector containing curvature squared, Yang--Mills, Higgs kinetic, nonminimal curvature, and Higgs-potential terms.

The explicit formula in [[library/ncg-standard-model-neutrino-mixing/entry|the local source]] returns the Euclidean Standard Model coupled to gravity after the four-manifold \(M\), finite geometry \(F\), inner fluctuation, cutoff scale, and test-function moments have been supplied.

This is a major structural achievement. It is not a derivation of spacetime from the finite algebra. The construction begins with

$$
D=D_M\otimes\mathbf1+\gamma_M\otimes D_F.
$$

Nor does the spectral trace define a positive information metric. Its Hessian can have either sign, whereas BKM response is positive after the physical quotient.

## Why it belongs downstream of the wall

The action requires choices that already have observable meaning:

- a represented operator with a spectrum that can be counted;
- a trace or regularized trace;
- a resolution scale \(\Lambda\);
- a test function and its moments;
- a Euclidean-to-Lorentzian prescription; and
- a domain of fields or histories to vary.

The principle of stationary action may govern the observable geometry produced after descent. Nothing in the definition requires the pre-observable algebraic ground itself to be a history selected by extremizing \(S_\Lambda\). In this programme this observable spectral action is therefore a consumer of wall realization, not its ontological cause.

This boundary does not exclude a separately defined **atemporal internal spectral selector** on a moduli category of internal Dirac data. Such a functional could select or weight mathematical objects without presupposing temporal evolution. [[algebra/real-forms-and-factive-spacetime|The real-form realization note]] states that possibility. It would not be this observable action unless a functor transported the internal datum, trace, cutoff, and variational problem to the realized geometry, and it would not orient time without the independent fact-and-record process.

This also retypes spectral-action symmetry breaking. A \(G\)-invariant potential can have a minimum with stabilizer \(H\subset G\). The functional remains \(G\)-invariant while a selected minimizing representative is only \(H\)-invariant. That is conventional observable symmetry breaking. Within one fixed triple, the corresponding persistence question is answered by the \(K\)-homology or cyclic class in [[spectral-wall-descent/index-and-curvature-transgression|index and curvature transgression]]. Persistence across a wall that changes the algebra additionally requires an explicit \(KK\)-correspondence or pushforward.

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
- If context-dependent entropy is inferred from the conjugacy-invariant bulk action, the finite orbit counterexample applies.
- If heat entropy is used to derive Einstein gravity, the \(a_2\) cancellation must be overcome by a different functional or boundary term.
- If an observable minimum is used as the necessity of the pre-observable ground, the action has been moved across the wall without a descent theorem.
