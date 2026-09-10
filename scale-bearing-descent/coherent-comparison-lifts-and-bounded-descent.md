# Coherent Comparison Lifts and Bounded Descent

Bounded constructive descent becomes more precise when changing access is distinguished from adding new distinctions. An existing reconstruction law transports contractively through actual regional restriction, provided its inherited boundary information is retained. The harder conjecture asks for source-defined lifts whose complete composites stay bounded, together with control of the new response directions introduced by source extension. This makes the missing operation a coherent transport of comparisons and their remainders.

## What changes when access changes

A source is a possible insertion into a comparison, represented by a vector in the norm supplied by the common evaluation. Its innovation is what remains after prediction from the preceding accessible information. A repair reconstructs the centered source from that innovation, up to a controlled error. These three objects belong to different spaces and must be transported together.

Restricting access to an already fixed joint law does not add possible sources to that law. Enlarging a source family does. Increasing volume or refining a regulator can additionally change the joint law, its norm and its chronology. A theorem about the first operation cannot silently perform the others.

The [[two-slice-innovation-geometry/regional-innovation-and-exterior-information-balance|regional information identity]] makes this distinction concrete. When the predictor knows less, its prediction error contains an additional exterior-information term. Discarding that term and then asking the compressed response to reconstruct the source creates a different problem. The mathematical object to preserve is the comparison with its conditional information.

## A lift transports the repair

Let \(\mathcal H_f,\mathcal H_c\) be Hilbert source spaces with unit vacua \(\Omega_f,\Omega_c\), and let \(V:\mathcal H_c\to\mathcal H_f\) be an isometry satisfying \(V\Omega_c=\Omega_f\). Put \(Q_a=I-|\Omega_a\rangle\langle\Omega_a|\). Specify bounded actual analyses
\[
\delta_a:\mathcal H_a\longrightarrow\mathcal X_a,\qquad
\delta_a\Omega_a=0,\qquad a\in\{f,c\}.
\]
The innovation spaces \(\mathcal X_a\) need not be copies of the source spaces. Suppose an independently constructed repair satisfies
\[
B_f\delta_f=Q_f-E_f,\qquad \|E_f\|\le\rho<1.
\]
The [[scale-bearing-descent/phase-and-distinguishability-from-one-kernel|cyclic-comparison construction]] supplies such a seed conditionally on its source relation and actual factorization, with \(\rho=2/3\).

**Exact transport lemma.** A bounded comparison lift
\[
\boxed{\delta_fV=\Lambda_{f\leftarrow c}\delta_c}
\tag{CL1}
\]
defines
\[
\boxed{
B_c=V^*B_f\Lambda_{f\leftarrow c},\qquad
B_c\delta_c=Q_c-V^*E_fV,\qquad
\|B_c\|\le\|B_f\|\,\|\Lambda_{f\leftarrow c}\|.}
\tag{CL2}
\]
Substitution proves the identity, since \(V^*Q_fV=Q_c\). Thus a lift reconstructs the fine comparison of every retained source from its retained comparison. It need not invert the full analysis.

For successive changes, source inclusions compose as \(V_{02}=V_{01}V_{12}\). If the source rules give
\[
\Lambda_{0\leftarrow2}
=\Lambda_{0\leftarrow1}\Lambda_{1\leftarrow2},
\qquad
\sup_{\text{admissible composites}}\|\Lambda_{0\leftarrow n}\|
\le L<\infty,
\tag{CL3}
\]
then direct and sequential repairs agree, with
\[
B_n=V_{0n}^*B_0\Lambda_{0\leftarrow n},\qquad
\|B_n\|\le\|B_0\|L,\qquad
\|E_n\|\le\rho.
\]
On \(\Omega_n^\perp\), for \(C=\|B_0\|L>0\),
\[
\boxed{\|\delta_nf\|^2\ge\frac{(1-\rho)^2}{C^2}\|f\|^2.}
\tag{CL4}
\]
Indeed \(\|B_n\delta_nf\|=\|f-E_nf\|\ge(1-\rho)\|f\|\). Contractive lifts give \(L=1\). Separate bounds larger than one at every stage give no uniform bound on the composite.

For the conjectural construction, the maps in (CL1)–(CL3) must come from the marked source rules. Defining a lift by a spectral inverse after evaluating each model would not explain the estimate. Coherence on the complete declared carriers is a sufficient strong condition; equality only on the range of the analysis must be identified as such.

## Actual regional restriction has a contractive lift

Fix one stationary pair law for \((X_0,X_\ell)\), with marginal \(\pi\), and let
\[
\mathcal H_F=L^2(\pi),\qquad
\mathcal X_F=L^2(\operatorname{law}(X_0,X_\ell)).
\]
Let \(\mathcal B\) be an actual regional observable sigma algebra. Its one-endpoint and pair-law spaces are \(\mathcal H_B\) and \(\mathcal X_B\). Pullback gives isometries
\[
V_{FB}:\mathcal H_B\to\mathcal H_F,\qquad
J_{FB}:\mathcal X_B\to\mathcal X_F.
\]
All use the same law and the same separation \(\ell\).

Write \(F_F\) for conditional expectation on the full past endpoint \(\sigma(X_0)\) in \(\mathcal X_F\), and \(F_B\) for conditioning on the regional past endpoint in \(\mathcal X_B\). Define
\[
\delta_Ff=(I-F_F)f(X_\ell),\qquad
\delta_Bf=(I-F_B)f(B_\ell).
\]
These are bounded operators. The theorem only requires the pair law. Identifying the full endpoint predictor with prediction from the entire preceding history additionally uses a Markov realization.

The regional and full innovations are related by
\[
J_{FB}\delta_Bf
=\delta_FV_{FB}f+
\left(
\mathbb E[f(B_\ell)\mid X_0]
-\mathbb E[f(B_\ell)\mid B_0]
\right).
\tag{CL5}
\]
The last summand is a function of \(X_0\), orthogonal to the first. This is the exterior-information term of the regional identity. Applying \(I-F_F\) removes it, so
\[
\boxed{
\Lambda_{F\leftarrow B}=(I-F_F)J_{FB},\qquad
\|\Lambda_{F\leftarrow B}\|\le1,\qquad
\Lambda_{F\leftarrow B}\delta_B=\delta_FV_{FB}.}
\tag{CL6}
\]
Consequently every existing full repair transports to
\[
\boxed{
B_B=V_{FB}^*B_F(I-F_F)J_{FB},\qquad
B_B\delta_B=Q_B-V_{FB}^*E_FV_{FB},\qquad
\|B_B\|\le\|B_F\|.}
\tag{CL7}
\]
Here \(Q_B\) is the vacuum-complement projection, not the time-dependent regional predictor denoted \(Q_B(t)\) in the linked source note.

For nested regions \(\mathcal B\subset\mathcal C\subset\mathcal F\), define \(\Lambda_{C\leftarrow B}=(I-F_C)J_{CB}\) using the actual \(C\)-pair law. Since \(J_{FC}F_C\) takes values in the full past-endpoint subspace,
\[
\begin{aligned}
\Lambda_{F\leftarrow C}\Lambda_{C\leftarrow B}
&=(I-F_F)J_{FC}(I-F_C)J_{CB}\\
&=(I-F_F)J_{FB}
=\Lambda_{F\leftarrow B}.
\end{aligned}
\tag{CL8}
\]
The source inclusions also compose. Thus regional repair transport is exactly coherent and contractive through arbitrarily many nested restrictions.

This theorem preserves a seed; it does not create one. Its formula uses the inherited full repair and full conditional law, so it does not yet express that repair using only primitives available in the smaller presentation. Nor does it make the regional predictor an autonomous semigroup. In general \(\delta_F^*\delta_F=I-P_\ell^*P_\ell\), with \(P_\ell\) the full endpoint predictor. In a Markov return \(P_\ell=e^{-\ell H}\) with \(H\ge0\) self-adjoint, this becomes \(I-e^{-2\ell H}\). The regional predictor generally fails the semigroup law. The same chronology must be used throughout.

The converse fails: good response on selected regions need not control the global source carrier. The [[two-slice-innovation-geometry/inq#The hidden-parity obstruction is exact|hidden-parity example]] exhibits arbitrarily soft global information invisible to every proper regional marginal. Revealing that information is a source extension, not another application of (CL7). These pair-law results do not assume a vacuum-preserving conditional expectation onto every local algebra of a continuum quantum field theory; that stronger algebraic realization would require its own construction.

## Division is the lost part of a comparison lift

The [[scale-bearing-descent/constructive-descent-division|descent-division lemma]] starts with a different operation: hard compression of an analysis. Let \(S:\mathcal X_c\to\mathcal X_f\) be an isometry and set
\[
\delta_c=S^*\delta_fV,\qquad
L_\delta=(I-SS^*)\delta_fV,\qquad
B_c^{\rm comp}=V^*B_fS.
\]
Seek a source-defined bounded map \(F:\mathcal X_c\to\mathcal X_f\) with
\[
L_\delta=F\delta_c,\qquad S^*F=0.
\]
Then
\[
\boxed{
\Lambda=S+F,\qquad
\delta_fV=\Lambda\delta_c,\qquad
\Lambda^*\Lambda=I+F^*F.}
\tag{CL9}
\]
The two channels are orthogonal. In particular \(\|\Lambda\|\le\sqrt{1+\|F\|^2}\). The mixed lost term and its division are
\[
C_V=V^*B_fL_\delta=(V^*B_fF)\delta_c,\qquad
K_V=V^*B_fF,
\]
so the corrected repair is simply \(V^*B_f\Lambda=B_c^{\rm comp}+K_V\).

Factoring the whole \(L_\delta\) is stronger than factoring only \(C_V\). A valid mixed-term division need not admit this stronger lift. The gain, when it does, is that one can study the norm and composition of the entire transport instead of separately summing correction norms.

There is always a formal completion that retains the lost channel:
\[
\widehat\delta_cf=
\bigl(S^*\delta_fVf,\ (I-SS^*)\delta_fVf\bigr).
\]
The recombination \((x,y)\mapsto Sx+y\) is unitary from
\(\mathcal X_c\oplus\operatorname{ran}(I-SS^*)\) to \(\mathcal X_f\). Transport through it preserves the repair bound. This becomes a substantive construction when the source grammar realizes the completed channel, or rewrites it through retained comparisons as in (CL9). Merely adjoining all discarded data cannot establish a law on the smaller description.

## Existing constructions identify the missing ingredients

[[rg-covariance-residue/gaussian-harmonic-refresh-lifting|Gaussian harmonic lifting]] supplies a model of uniform composite control. For a hard covariance tower \(C_{j+1}=Q_jC_jQ_j^*\), its harmonic sections satisfy
\[
M_j=C_jQ_j^*C_{j+1}^{-1},\qquad
\boxed{
M_0\cdots M_{n-1}
=C_0(Q_{n-1}\cdots Q_0)^*C_n^{-1}.}
\tag{CL10}
\]
Intermediate covariance factors cancel. For the specified aligned regular gauge averages, the composite norm is bounded by \((\pi/2)^{d+1}\), independently of blocking depth. These maps act on configuration variations, not the innovation Hilbert spaces in (CL1). Their importance is the mechanism: estimate the composite once from its defining law. The retained Maxwell soft modes survive, so bounded transport alone supplies no seed gap.

[[rg-covariance-residue/nonlinear-gauge-fiber-transport|Nonlinear gauge-fiber transport]] constructs a lift for the actual conditional law by solving its conditional score equation. Under the stated curvature and incidence bounds it has a volume-uniform one-step strong-coupling estimate. It shows that a curved conditional family can be transported without pretending its fibers are identical Gaussians. Its Poisson inverse is not yet a finite source-word rule, and its composite norm through the continuum trajectory remains uncontrolled.

[[general-causal-action/conditional-boundary-translation-and-source-products|The four-face boundary message]] gives a nonzero interaction correction from the actual vacuum. Omitting face \(r\) shifts its conditional mean at first order by
\[
m_{r,h}=m_r+2h\sigma_rL_r,\qquad
L_r=\nabla_r\alpha,
\tag{CL11}
\]
where \(\alpha\) is the inherited amplitude score and \(L_r\) is a Lie-bracket field. The same conditional covariance supplies every Wick contraction of prescribed polynomial source products. Keeping the appropriate third face restores agreement of the two nested elimination routes. This is a concrete example of a remainder determining its repair, including mixed products that a mean-only message erases.

The first-order formula is controlled for specified fixed polynomial sources in the actual compact vacuum norm. It is not a bounded operator theorem on the entire source completion. Its promotion to exact Gaussian conditionals fails joint normalization: the resulting nonzero cubic exponential is not integrable. Higher conditional moments must therefore be supplied by the joint law. [[general-causal-action/conditional-replica-cumulants-and-amplitude-stability|Conditional replica stability]] gives norm estimates for fixed bounded source kernels without dividing by small marginal probabilities; this is useful for constructing a normed message algebra, not a completion theorem by itself.

[[general-causal-action/cut-tour-absorption-and-the-injective-exchange|Finite cut tours]] isolate another useful ingredient. A tour through \(m\) commuting layers gives an explicit word \(B\) with \(B\delta=I-W\) and \(\|B\|\le\sqrt m\), independently of the number of cuts in each layer. The proposed exact absorption \(W^2=W\) fails for the actual faithful exchanges, which are injective. The reusable lesson is the bounded-overlap repair formula; the missing requirement is a controlled nonvacuum residual, not exact erasure in finitely many steps. [[algebra/short-loop-holonomy-and-quantitative-gluing|Short-loop repair]] likewise turns telescoping and bounded congestion into a norm estimate, while its neutral-source control shows why section-level phase rigidity cannot be imported unchanged into gauge-invariant observables.

[[rg-covariance-residue/second-ring-commuting-escape|Second-ring Wilson escape]] provides a particularly concrete overlap mechanism. For the specified \(SU(3)\) Wilson law and unfavorable context, choose a differentiated link \(j(e)\) outside the active link's interaction star. Its derivative commutes with the active conditional expectation \(P_e\), so the estimate keeps \(Q_e=I-P_e\), the original innovation. The assignment \(e\mapsto j(e)\) is a bijection. At the stated neighborhood cut \(B_{e,1}\), summation gives
\[
\sum_e\|\mathbf1_{B_{e,1}}Q_ef\|^2
\le\frac{\mathcal E_{\rm full}(f)}{56\beta}
+\frac67\sum_e\|Q_ef\|^2.
\tag{CL13}
\]
The coefficient \(6/7\) multiplies exactly the original innovation sum, with no incidence factor from overlapping larger blocks. This is an actual-law, volume-independent localization estimate on its declared cuts. It does not yet give a division identity, cover their complementary contexts, or identify the auxiliary gradient form with physical time. Its useful instruction for a new construction is precise: choose transport directions that leave the active conditional law unchanged, and prove the overlap count before attempting absorption. The [[rg-covariance-residue/wilson-frustration-and-joint-escape|earlier joint escape]] has a different, enlarged-block remainder; the two estimates cannot be interchanged by naming both of them repair.

These results suggest a common target: a boundary message algebra closed under marked products, equipped with an evaluated norm in which composite comparison lifts can be estimated. Its relations must carry the conditional law, including the channels generated at the next order.

## Genuine source extension has its own test

An existing repair on a subspace does not reconstruct newly admitted sources. In [[general-causal-action/radius-orientation-source-extension-and-the-innovation-floor|the radius–orientation extension]], adding an actual mixed source lowers the optimal response of the earlier probe family while the Hamiltonian, law and clock stay fixed. The [[general-causal-action/four-face-oriented-source-extension-and-the-schur-surplus|oriented cubic extension]] further removes an apparent positive surplus and follows the negative physical-gap correction. Mixed source channels change the answer.

An interacting extension can also change the chronology itself. [[conditional-preparation-sewing/conditional-preparation-extension-at-new-access|New-access preparation]] preserves the old preparation marginal while joint localization changes its old clock. The [[conditional-preparation-sewing/conditional-access-families-and-the-returned-clock|access-family construction]] tracks the joint marked transfer. Thus compatibility must concern complete chronological comparisons, not preservation of an unmarked marginal alone.

There is an exact finite diagnostic for the response floor required by (CL4). For linearly independent centered sources \(z_1,\ldots,z_N\) in one actual Hilbert space, form
\[
\mathsf N_{ij}=\langle z_i,z_j\rangle,\qquad
\mathsf R_{ij}=\langle\delta z_i,\delta z_j\rangle,\qquad
\mathsf M_\gamma=\mathsf R-\gamma\mathsf N.
\]
The threshold \(\|\delta f\|^2\ge\gamma\|f\|^2\) holds on their span exactly when \(\mathsf M_\gamma\ge0\). Splitting old and new source coefficients gives, when \(A>0\),
\[
\boxed{
\mathsf M_\gamma=
\begin{pmatrix}A&C\\C^*&D\end{pmatrix}\ge0
\quad\Longleftrightarrow\quad
D-C^*A^{-1}C\ge0.}
\tag{CL12}
\]
Complete the old coefficient square to prove the equivalence. The Schur term measures the new direction after its best cancellation against old sources. Positive diagonal responses alone do not control it. Choose \(\gamma\) strictly below the old minimum to ensure \(A>0\); a singular old block requires the corresponding range condition.

The linked four-face calculation uses this same block principle for a different normalized quotient, with pencil
\(\langle z_i,R^2z_j\rangle-\gamma\langle z_i,Rz_j\rangle\).
Its denominator must not be substituted for \(\mathsf N\) above. Both tests retain the mixed matrix and its actual norm.

For one bounded analysis on one Hilbert carrier, a common \(\gamma>0\) on an increasing dense union of source spaces extends to its closure by continuity. Across changing volumes, states or clocks, that conclusion requires compatible realization maps and convergence of the full forms. Computing Schur complements diagnoses extension; a source identity must explain their uniform positivity. The inverse in the diagnostic is not a proposed primitive construction of the repair.

## The sharpened constructive conjecture

**Conjecture II, in comparison-lift form.** The selected marked source algebra admits a finite system of boundary-message rules, closed under its actual mixed source products. On its specified Yang–Mills vacuum branch these rules generate comparison lifts coherent under admissible assembly and refinement, with a bound on the complete composite in the evaluated norm. The same rules extend the seed repair to newly generated source directions with a common error below one and a common repair bound at fixed inherited comparison scale.

There are two construction obligations. Pure restrictions must realize the contractive formula (CL6) within the source grammar. Genuine extensions must supply the missing mixed directions and control them uniformly; they cannot merely relabel the old repair. A finite grammar may generate arbitrarily rich messages, so finitely many operation types do not imply bounded message size or norm.

The word “finite” also needs its scale. If bare primitives act within distance \(O(a)\), a uniformly bounded-degree word cannot span a fixed nonzero comparison length as \(a\to0\). Scale-dependent block primitives, a controlled growing word, or a genuinely global conditional operation are different possible responses. The locality hypothesis must be stated before making this support argument. The quadratic word-length estimate in [[scale-bearing-descent/variance-completed-rigidity|variance-completed rigidity]] is an upper estimate on possible loss, not a theorem that the loss must grow quadratically; exact cancellation can improve it. Declare support, degree, source norm and inherited separation together.

The first useful target is a new loop or mixed source coupled through two conditional parents: derive its comparison identity from the complete joint law, carry its nonzero boundary correction through two elimination routes, and estimate the combined repair in the actual norm. The four-face message supplies an interaction-sensitive starting expression. Restricting the result back to an old source carrier tests the exact transport theorem; adding further sources tests the unresolved extension step. Repeated assemblies should control both at one fixed threshold. The Gaussian cancellation and finite-layer estimates identify mechanisms worth reproducing; the source-extension controls specify what a candidate must survive.

If that rule also constructs the cyclic seed and returns the required physical chronology, (CL2)–(CL4) turn its algebraic stability into the threshold in [[scale-bearing-descent/mass-from-the-algebra-of-changing-access|Mass from the Algebra of Changing Access]]. The remaining Yang–Mills work is substantial: selection of the law, complete-source uniformity, fixed-scale continuum control and axiomatic reconstruction. The conceptual gain is precise: a positive mass threshold would express a finite cost of reconstructing distinctions, preserved by the law that relates their presentations.
