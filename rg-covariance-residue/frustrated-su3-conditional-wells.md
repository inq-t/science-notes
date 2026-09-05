# Frustrated SU(3) Conditional Wells

The uniform linear-tilt bound on \(SU(2)\cong S^3\) does not extend to all \(SU(3)\) Wilson link conditionals. Realizable exterior staple configurations create competing central wells, including unequal wells persisting over an open range of source shapes. Their single-link gradient Poincare constants tend to zero exponentially as inverse coupling grows. This rules out a coupling-independent certificate uniform over every boundary, not a physical Yang--Mills gap.

**Status: [EXACT CONDITIONAL COUNTEREXAMPLE] for the stated finite-link family and its ordinary Wilson-star realization; [NO CLAIM OF PHYSICAL GAPLESSNESS].**

## Two global minima from the determinant constraint

On \(SU(3)\), take normalized Haar measure, a fixed bi-invariant metric, and
\[
dq_\kappa(U)=Z_\kappa^{-1}e^{-\kappa V(U)}\,dU,\qquad
V(U)=\operatorname{ReTr}U,\qquad \kappa>0.
\tag{FW1}
\]
If the eigenvalues are \(e^{i\alpha},e^{i\beta},e^{-i(\alpha+\beta)}\), put \(s=(\alpha+\beta)/2,\ d=(\alpha-\beta)/2\). Then
\[
\begin{aligned}
V(U)&=2\cos s\cos d+2\cos^2s-1\\
&\ge2(|\cos s|-1/2)^2-3/2.
\end{aligned}
\tag{FW2}
\]
Attaining \(V=-3/2\) requires equality in (FW2) together with \(|\cos s|=1/2\). These conditions force all three eigenvalues to coincide at a nontrivial cube root of unity. Thus the only minima are
\[
zI,\ z^2I,\qquad z=e^{2\pi i/3},\qquad V_{\min}=-3/2.
\tag{FW3}
\]
They are nondegenerate. For small traceless anti-Hermitian \(X\),
\[
V(ze^X)=-3/2-\tfrac14\operatorname{Tr}X^2+O(\|X\|^3),
\tag{FW4}
\]
and the same holds at \(z^2I\). The eight-dimensional neighborhood of either well therefore gives, for \(\kappa\ge1\),
\[
Z_\kappa\ge c_0\kappa^{-4}e^{3\kappa/2}.
\tag{FW5}
\]
This estimate follows by integrating over a coordinate ball of radius proportional to \(\kappa^{-1/2}\), using the quadratic upper bound on \(V-V_{\min}\) and smooth positive Haar density.

## The exact barrier is one half

If \(t=\operatorname{Tr}U\) is real for \(U\in SU(3)\), its characteristic polynomial factors as
\[
\lambda^3-t\lambda^2+t\lambda-1
=(\lambda-1)(\lambda^2+(1-t)\lambda+1).
\tag{FW5a}
\]
Thus its eigenvalues include \(1\), with the remaining pair \(e^{\pm i\theta}\), and \(\operatorname{ReTr}U\ge-1\). Every path between \(zI\) and \(z^2I\) crosses the real-trace locus. Conversely the diagonal path
\[
D_\theta=\operatorname{diag}(e^{i\theta},e^{i\theta},e^{-2i\theta}),
\qquad 2\pi/3\le\theta\le4\pi/3
\]
has \(V(D_\theta)=2(\cos\theta+1/2)^2-3/2\), with maximum \(-1\) at \(\theta=\pi\). The minimax barrier above the minima is therefore exactly \(1/2\).

Compactness implies that for every \(\eta<1/2\), a sufficiently narrow fixed band \(|\operatorname{ImTr}U|\le a_\eta\) satisfies \(V\ge-3/2+\eta\). The smooth cutoff below can consequently use any such \(\eta\). Equality \(\eta=1/2\) is not supplied for a fixed band of positive width.

## A conditional Rayleigh quotient tends to zero

Choose a smooth odd function \(h\) equal to \(\pm1\) outside \([-a,a]\), where \(0<a<3\sqrt3/2\), and let
\[
f(U)=h(\operatorname{ImTr}U).
\tag{FW6}
\]
Inversion preserves Haar and \(V\) while changing \(f\)'s sign, so \(q_\kappa f=0\). The function equals opposite constants in neighborhoods of the two wells. Its gradient has compact support away from both minima, hence \(V\ge-3/2+\eta\) on that support for some \(\eta>0\).

Concentration near the two wells gives \(\operatorname{Var}_{q_\kappa}f\to1\). The bounded gradient and (FW5) give
\[
\int|\nabla f|^2\,dq_\kappa
\le C_0\kappa^4e^{-\kappa\eta}.
\]
Consequently the optimal conditional gradient gap obeys
\[
\boxed{
\lambda_{\mathrm{PI}}(q_\kappa)
\le C_1\kappa^4e^{-\kappa\eta}\longrightarrow0.}
\tag{FW7}
\]
The constants depend on the fixed metric and cutoff, not on \(\kappa\). A finite-\(\kappa\) gap still exists because the density is smooth and positive on a connected compact group.

## The exterior field is an actual Wilson staple sum

For a four-dimensional Wilson link, orient its six complementary staples \(W_p\) so that the conditional exponent is
\[
\frac{\beta}{3}\operatorname{ReTr}\!\left(U^*\sum_{p\ni e}W_p\right).
\tag{FW8}
\]
Choose three \(W_p=zI\) and three \(W_p=z^2I\). Their sum is \(-3I\), and (FW8) becomes \(-\beta\operatorname{ReTr}U\), exactly (FW1) with \(\kappa=\beta\).

This is compatible lattice data, not six independent plaquette values imposed in violation of a constraint. Each complementary path has its own outer edge parallel to the active link, displaced by one of the six transverse neighbors. Set the transverse edges to identity and choose these distinct outer parallel edges to realize the six central path products. Exclude short periodic identifications that merge those edges.

A gauge-invariant relative-loop version of the witness uses any reference staple \(W_{\mathrm{ref}}=zI\):
\[
h\!\left(\operatorname{ImTr}(z\,U W_{\mathrm{ref}}^*)\right).
\tag{FW9}
\]
The argument transforms by conjugation at the common source and reduces to \(h(\operatorname{ImTr}U)\) at the chosen exterior. The competing conditional wells are therefore distinguishable by relative Wilson data, not removed by a common endpoint change of frame.

For each finite \(\beta\), the fixed-test conditional Rayleigh quotient varies continuously with exterior links. The finite Wilson exterior marginal has full support. Nearby positive-measure exterior sets therefore have comparably small conditional quotients. The counterexample defeats an essentially uniform as well as a pointwise uniform bound independent of coupling; it does not quantify how probable those unfavorable sets are as \(\beta\) grows.

## Equal scalar strength does not identify the source orbit

For the general conditional source \(S\), put
\[
dq_S(U)\propto
\exp[(\beta/3)\operatorname{ReTr}(U^*S)]\,dU.
\tag{FW10}
\]
The simultaneous transformation \(S\mapsto gSh^*\), \(U\mapsto gUh^*\), with \(g,h\in SU(3)\), preserves the measure and metric. It therefore preserves the conditional Poincare constant. It also preserves \(\det S\), not only the singular values.

Two ordinary six-staple sums illustrate the distinction:
\[
S_+=4I+zI+z^2I=3I,\qquad
S_-=3zI+3z^2I=-3I.
\tag{FW11}
\]
Both have singular values \((3,3,3)\) and the same Frobenius norm. But \(\det S_+=27\), while \(\det S_-=-27\); no endpoint \(SU(3)\) change of frame identifies them. The positive source has a unique exponent maximum at \(U=I\), since \(\operatorname{ReTr}U\le3\) with equality only there. The negative source has the two maxima established above. Uniqueness in the positive case is not by itself a uniform-gap proof.

For an invertible matrix source, singular-value decomposition shows that the ordered singular values together with the determinant phase classify this two-sided orbit. A representative is \(e^{i\theta/3}\operatorname{diag}(s_1,s_2,s_3)\), with cube-root changes related by the center. This reduces a static conditional-spectrum question to four real orbit parameters. At singular sources the phase degenerates; keeping the polynomial \(\det S\) avoids an artificial phase branch.

[[special-unitary-source-support|The source-support theorem]] evaluates a different scalar of this same orbit exactly: the largest active-link trace response. Singular values and determinant phase reduce it to a global one-angle maximization. That scalar sharpens a joint localization bound; it is not the conditional Poincare constant.

This is not a license to discard the moving frame from the complete boundary response. A context derivative changes both orbit data and the probes represented in that frame. A sufficient quotient for conditional spectral constants need not be sufficient for all retained observables. The structural lesson agrees with [[program-core/explanatory-economy|explanatory economy]]: a single scalar yardstick can hide an essential choice of response geometry even when its dimensions and normalization are correct.

## Unequal wells persist without exact phase coexistence

The obstruction is not confined to the equal-depth source. With the metric \(g=-\operatorname{ReTr}/3\), define
\[
h_\psi(U)=\operatorname{ReTr}(e^{-i\psi}U),\qquad
dq_{\kappa,\psi}=Z_{\kappa,\psi}^{-1}e^{\kappa h_\psi(U)}\,dU,
\qquad \pi/6<\psi<\pi/3.
\tag{FW12}
\]
At \(U=z^jI\), tracelessness kills the linear term and
\[
\begin{aligned}
h_\psi(z^je^X)
&=3\cos(2\pi j/3-\psi)
+\tfrac12\cos(2\pi j/3-\psi)\operatorname{Tr}X^2
+O(\|X\|^3),\\
\operatorname{Hess}_{z^jI}h_\psi
&=-3\cos(2\pi j/3-\psi)\,g.
\end{aligned}
\tag{FW13}
\]
For \(j=0,1\), these Hessians are strictly negative. Moreover,
\[
h_\psi(I)>h_\psi(zI).
\tag{FW14}
\]
Thus the negative log density has a lower and a higher local well. The higher local well is metastable here in the precise variational sense proved next; no stochastic ontology is asserted.

Choose a small ball around \(zI\) in which \(h_\psi\le h_\ell:=h_\psi(zI)\). Take a smooth \(0\le f\le1\) equal to one in a smaller ball, supported in the first ball, with gradient supported on a compact annulus. Strict nondegeneracy gives an \(\eta>0\) such that \(h_\psi\le h_\ell-\eta\) on that annulus. The eight-dimensional quadratic estimate and bounded gradient imply
\[
\int f^2e^{\kappa h_\psi}\,dU
\ge c\kappa^{-4}e^{\kappa h_\ell},
\qquad
\int|\nabla f|^2e^{\kappa h_\psi}\,dU
\le C e^{\kappa(h_\ell-\eta)}.
\tag{FW15}
\]
A fixed neighborhood of \(I\) has \(h_\psi\ge h_\ell+d\) for some \(d>0\). Consequently \(q_{\kappa,\psi}(\operatorname{supp}f)\le C'e^{-\kappa d}\). Cauchy--Schwarz gives the important variance estimate
\[
\operatorname{Var}_{q_{\kappa,\psi}}f
\ge[1-q_{\kappa,\psi}(\operatorname{supp}f)]q_{\kappa,\psi}(f^2)
\ge\tfrac12q_{\kappa,\psi}(f^2)
\tag{FW16}
\]
for all sufficiently large \(\kappa\). Dividing (FW15) and cancelling the same partition function proves
\[
\boxed{\lambda_{\mathrm{PI}}(q_{\kappa,\psi})
\le C_\psi\kappa^4e^{-\kappa\eta_\psi}.}
\tag{FW17}
\]
Unlike the symmetric witness, this test's variance need not stay of order one. Both its variance and energy are small; the additional annular barrier makes their ratio small. No assertion that \(I\) is the only global maximum is needed.

The constants can be uniform when \(\psi\) ranges over a compact subinterval of \((\pi/6,\pi/3)\): the two Hessian bounds, height separation and chosen neighborhoods then have uniform margins. Small general matrix-source perturbations preserve the two nondegenerate local maxima and their height ordering by the implicit-function theorem. A sufficiently small source neighborhood has a uniform local cutoff construction as well. This is an open set of source shapes, not merely an equality locus for the determinant phase. The endpoints are excluded: the lower maximum loses its quadratic definiteness at \(\pi/6\), and the height separation used in (FW16) vanishes at \(\pi/3\).

This cancellation of a rare well's weight is consistent with the unequal-well Eyring--Kramers result in [[library/poincare-and-logarithmic-sobolev-inequalities-by-energy-landscape/inq|Menz--Schlichting]], Corollary 2.18. That Euclidean theorem is not being applied to the compact group: (FW13)--(FW17) provide the intrinsic proof here.

An actual six-staple realization uses two copies of each cyclic permutation of
\[
D=\operatorname{diag}(a,a,a^{-2}),\qquad a=(3+4i)/5.
\]
Their sum is \((46+32i)I/25\), whose phase obeys
\(\tan\psi=16/23\) in the interval above. In (FW12),
\(\kappa=\beta|46+32i|/75\).
[[wilson-exterior-force-localization|The exterior-force theorem]] constructs this lattice configuration, including its thirty additional plaquettes, and controls a neighborhood under the full joint law.

## What the failed certificate teaches

[[conditional-fisher-coercivity/linear-tilted-sphere-coercivity|The \(SU(2)\) estimate]] depends on quaternionic sphere geometry. A general \(SU(3)\) matrix source is not a single linear height on a round sphere, and the determinant constraint permits the two wells above. Compactness alone does not preserve its conditional floor through unbounded coupling.

The variational test differentiates only the active link. Its exterior-link gradients are uncontrolled, so (FW7) says nothing directly about the full gauge-invariant Hamiltonian or the complete temporal-column response. It also does not exclude a state-weighted treatment of bad contexts, larger joint blocks, or another operator realization.

The constructive next requirement is sharper: control unfavorable contexts under the **actual retained law**, together with their coupling to the retained response, instead of requiring every one-link conditional to have a coupling-independent floor. This is consistent with [[coarse-response-memory/inq|the hidden-return budget]], which needs control of the whole relation and cannot be inferred from a single conditional spectrum.

[[conditional-fisher-coercivity/bad-context-response-and-localization|The bad-context theorem]] types the replacement: bound the joint form cost of fluctuations concentrated on unfavorable contexts and separately control their retained mean. Rarity alone does not suffice, because multiplication by the bad-context indicator followed by conditional centering is still a norm-one projection whenever its range is nonzero.

[[wilson-frustration-and-joint-escape|Joint Wilson escape]] now constructs that replacement for a concrete neighborhood of the displayed exterior. The full action has downhill outer-link directions, and an action-Laplacian certificate bounds concentration on the neighborhood by outer-link energy plus a seven-link innovation with fixed coefficient \(6/7\). This includes surrounding plaquettes and does not average away rare tests. It does not cover all exteriors realizing a frustrated source.

[[receipts/staple_elimination_receipt.py|The finite receipt]] checks the eigenangle minimum, central staple realization and decreasing trial-function Rayleigh quotients by Weyl integration. The exponential upper-bound proof is (FW2)--(FW7), not those numerical samples.
