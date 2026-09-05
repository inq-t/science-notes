# A Fisher Collar Bound for Nonlinear Wilson Laws

The actual finite Wilson law admits an explicit boundary-response floor in a strong-coupling regime. Compact-group curvature controls conditional and marginal fluctuations, while conditional Fisher information measures how much a boundary change can move the interior law. Integrating a collar improves the bound through an operator-norm score-covariance estimate that does not count surface cells. This removes a surface-area loss in this regime; it does not establish the weak-bare-coupling continuum trajectory.

**Status: [EXACT SUFFICIENT NONLINEAR FINITE-REGULATOR BOUNDS], uniform in volume and fixed exterior links under the displayed incidence and strong-coupling hypotheses; [OPEN] for continuum RG transport and physical reconstruction.**

## Action-derived constants

Use \(SU(r)\), \(r\ge2\), on a finite \(d\)-dimensional hypercubic lattice, \(d\ge2\), with the product metric and Wilson action
\[
g(X,Y)=-r^{-1}\operatorname{ReTr}(XY),\qquad
S_\beta(U)=\beta\sum_p(1-r^{-1}\operatorname{ReTr}U_p).
\tag{WC1}
\]
Assume \(\beta\ge0\), elementary plaquettes counted once, and no small-volume identifications repeating an edge within an elementary plaquette. Exterior links may be fixed arbitrarily.

The [[rg-covariance-residue/nonlinear-conditional-gauge-response|normalized compact-gauge calculation]] proves
\[
\operatorname{Ric}=\frac{r^2}{2}g,\qquad
\operatorname{Hess}S_\beta\ge-8\beta(d-1)g_{\rm product}.
\]
For disjoint link sets, the mixed Hessian operator norm is at most
\[
h:=6\beta(d-1).
\tag{WC2}
\]
The constants are incidence bounds: each link meets at most \(2(d-1)\) plaquettes, each with four edges; the off-diagonal row sum counts only the other three edges. The same column bound gives the operator norm by the Schur test.

Thus, throughout
\[
\boxed{\rho:=\frac{r^2}{2}-8\beta(d-1)>0,}
\tag{WC3}
\]
the full law and every frozen-link conditional law have Poincare constant at least \(\rho\). The weighted Bochner proof applies to each connected compact product of unfrozen links. Fixing additional links cannot enlarge the incidence bounds. Every coordinate marginal inherits the same Poincare estimate by applying the whole form to a coordinate pullback; no local formula for its marginal potential is needed.

[[library/a-stochastic-analysis-approach-to-lattice-yang-mills-at-strong-coupling/inq|Shen--Zhu--Zhu]] provide the primary strong-coupling precedent for this curvature method. The formulas here use (WC1), and the frozen-boundary, Fisher, and collar deductions below are proved from the stated bounds rather than quoted as their theorem.

## The direct boundary Fisher estimate

Partition the active links into retained boundary links \(D\) and interior links \(Y\), and let \(f\) depend on a core \(C\subseteq Y\). Use the actual marginal \(\nu_D\) and conditional law \(\beta_D(dY)\). The normalized boundary score is
\[
s_D[v]=-\partial_DS_\beta[v]
+\mathbb E_{\beta_D}\partial_DS_\beta[v].
\tag{WC4}
\]
The mixed Hessian bound and conditional Poincare inequality give
\[
I_D(v,v)=\operatorname{Var}_{\beta_D}(\partial_DS_\beta[v])
\le\frac{h^2}{\rho}\|v\|_{g_D}^2.
\tag{WC5}
\]
Since \(\nu_D\) inherits Poincare constant \(\rho\),
[[conditional-fisher-coercivity/inq|the background-metric Fisher theorem]] yields
\[
\boxed{
\mathbb E\operatorname{Var}(f(C)\mid D)
\ge\frac{\rho^2}{\rho^2+h^2}
\operatorname{Var}_\mu(f(C)).}
\tag{WC6}
\]
This is a bound for the nonlinear measured law, not for its identity Hessian alone. It holds for every square-integrable core observable by density, including complex gauge-invariant ones. If the retained raw boundary also contains exterior preparation information, its response is at most the endpoint-only bridge response, so (WC6) remains a sufficient lower bound for that bridge.

No nondegenerate Fisher metric is presumed: gauge or unidentifiable directions may make \(I_D\) singular. At \(\beta=0\), the score vanishes and the product law gives the exact floor one.

## Integrate the intervening collar before estimating its response

Now partition the active links into \(C,D,H\), with \(H\) intervening between core and boundary. Define the exact marginal potential
\[
V_{\rm eff}(C,D)=-\log\int e^{-S_\beta(C,D,H)}\,dH.
\tag{WC7}
\]
Do not replace it by a Wilson action with a new single coupling. For tangent combinations \(u\) on \(C\) and \(v\) on \(D\), the exact cross derivative is
\[
\operatorname{Hess}_{CD}V_{\rm eff}[u,v]
=\mathbb E_H\operatorname{Hess}_{CD}S_\beta[u,v]
-\operatorname{Cov}_H(\ell_C[u],\ell_D[v]),
\tag{WC8}
\]
where \(\ell_C[u]=\partial_CS_\beta[u]\), \(\ell_D[v]=\partial_DS_\beta[v]\), and the conditional law is \(H\mid C,D\). These are derivatives on distinct coordinate factors, so no same-factor connection term is omitted.

Suppose no plaquette meets both \(C\) and \(D\). The direct term is then zero. Let \(F_C,F_D\) be the hidden links on which \(d_H\ell_C\) and \(d_H\ell_D\) can be supported, and let
\[
q=\operatorname{dist}_{\rm int}(F_C,F_D),
\tag{WC9}
\]
where hidden links sharing an active plaquette are adjacent. If a source vanishes, the corresponding covariance vanishes; disconnected supports also have zero covariance under the factorized conditional law.

For the whole tangent combinations—not separate components—the incidence estimate gives
\[
\|d_H\ell_C[u]\|_{L^2(H|C,D)}\le h\|u\|,\qquad
\|d_H\ell_D[v]\|_{L^2(H|C,D)}\le h\|v\|.
\tag{WC10}
\]
Choose \(\theta>0\) and, for \(\beta>0\), put
\[
M_\theta=h(e^\theta-1),\qquad
m_\theta=\frac{\theta\rho}{\rho+M_\theta}.
\tag{WC11}
\]
The off-diagonal one-form Hessian has row and column sums at most \(h\). Parallel factor weights with logarithmic slope \(\theta\) therefore have conjugation defect at most \(M_\theta\).

Apply [[auxiliary-response-localization/exact-source-locality-without-a-full-form-gap|exact-source locality]] to the conditional law \(H\mid C,D\), then to (WC10). This proves the pointwise effective mixed-Hessian bound
\[
\boxed{
\|\operatorname{Hess}_{CD}V_{\rm eff}\|
\le h_{\rm eff}:=
h^2(\rho^{-1}+M_\theta^{-1})e^{-m_\theta q}.}
\tag{WC12}
\]
All bounds are uniform in the frozen \(C,D\) values and exterior configurations. There is no factor \(|F_C|\), \(|F_D|\), or interface area. It is the operator norm of the complete score map that is controlled. Summing separate covariance bounds over all boundary cells would lose this property. At \(\beta=0\), set \(h_{\rm eff}=0\) directly from independence; the reciprocals in (WC12) are not used.

## From the integrated collar to a complete response floor

Let \(Q_C=I-P_{\mathbf1}\) center the core marginal carrier, and let \(B_D\) be its conditional-variance operator given \(D\). The conditional core law \(C\mid D\) is a marginal of \((C,H)\mid D\), so its Poincare constant is still at least \(\rho\). The actual \(D\) marginal also has constant at least \(\rho\). Therefore (WC12) applied to the effective conditional score gives
\[
I_D^{\,C\mid D}\le\frac{h_{\rm eff}^2}{\rho}g_D,\qquad
\boxed{B_D\ge
\frac{\rho^2}{\rho^2+h_{\rm eff}^2}Q_C.}
\tag{WC13}
\]
No positive pointwise Hessian of \(V_{\rm eff}\) was assumed: the needed marginal and conditional Poincare estimates were inherited from the original law.

Use the better of the direct floor (WC6) and the collar floor (WC13). Equivalently replace \(h_{\rm eff}\) by
\(\widehat h=\min\{h,h_{\rm eff}\}\) in the resulting response bound; this minimum is a comparison of two proved response estimates, not necessarily a bound on the effective Hessian itself.

For [[global-local-response-reconstruction/boundary-frozen-heat-and-conditional-fisher-response|boundary-frozen interior heat]] with the same metric and law,
\[
\boxed{
R_s^{\,v}\ge
(1-e^{-s\rho})
\frac{\rho^2}{\rho^2+\widehat h^2}Q_C,\qquad
R_s^{\,v}\le B_D\le B_{\rm endpoints}.}
\tag{WC14}
\]
The endpoint comparison in (WC14) requires \(\sigma(\mathrm{endpoints})\subseteq\sigma(D)\); the other inequalities apply to the stated partition without this extra hypothesis. This gives both a concrete field-sensitive response and, under that inclusion, its temporal comparison. Its auxiliary parameter \(s\) is not physical clock time. Restricting these full-carrier form inequalities to gauge-invariant functions is valid; closing each collar under an independent gauge quotient before gluing is not part of the proof.

## A relative-leakage instance for coordinate deletion

There is a concrete one-step realization of [[bridge-data-augmentation-solder/relative-boundary-leakage|relative boundary leakage]] in this regime. Partition the active raw links as
\[
Y=(X,U),\qquad Z=(W,V),
\tag{WC16}
\]
and retain coordinate subsets \(X,W\). This is a deterministic product-coordinate deletion, not an arbitrary holonomy quotient or probabilistic RG kernel.

The actual \(V\mid W\) law is a coordinate marginal of \((Y,V)\mid W\), so it inherits Poincare constant \(\rho\). The normalized \(Y\mid Z\) family, restricted to vertical \(V\) tangents, has Fisher tensor at most \(h^2/\rho\) by (WC5). Consequently its relative boundary-prediction cost is at most
\[
r_{\partial}\le h^2/\rho^2.
\tag{WC17}
\]
For each fixed \(X=x\), the context law \(Z\mid X=x\) similarly inherits constant \(\rho\). The residual family \(U\mid(X,Z)\) has conditional Poincare constant \(\rho\) and mixed score-gradient bound \(h\). Conditional Fisher coercivity inside this fixed-\(X\) law therefore proves the full discarded-core hypothesis with
\[
b\ge\frac{\rho^2}{\rho^2+h^2}.
\tag{WC18}
\]
Thus an actual coarse response floor \(\kappa_c\) lifts to
\[
\boxed{\kappa_{\rm fine}\ge
\left(\frac{\rho^2}{\rho^2+h^2}\right)^2\kappa_c.}
\tag{WC19}
\]
All conditional laws here are obtained by freezing and marginalizing the original Wilson law, so the proof does not presume their effective potentials remain Wilson potentials. The direct floor (WC6) is stronger in this regime; (WC19) demonstrates how both distinct lifting hypotheses can be verified on a nonlinear gauge law.

This construction does not provide a scale-dependent improvement or summability at diverging depth. A fixed nonzero value of \(h^2/\rho^2\) at every step erodes the product certificate. Collar geometry or a new effective-law estimate must control those ratios along the actual tower.

## What remains along the continuum trajectory

The estimate is volume-uniform at fixed regulator and permits arbitrary fixed exterior links. Passing through vacuum preparation and a physical transfer still requires the convergence and identification gates in [[inq|the parent surface-response module]].

Most importantly, (WC3) means
\(\beta<r^2/[16(d-1)]\): it is an explicit **strong bare-coupling** regime. It does not persist as the four-dimensional asymptotically free bare coupling is taken toward its continuum limit. Failure of this sufficient curvature bound does not imply gaplessness.

The structural result worth transporting is not the bare number \(\rho\). It is the chain
\[
\text{normalized conditional scores}
\quad\longrightarrow\quad
\text{operator-norm collar susceptibility}
\ \longrightarrow\
\text{boundary Fisher comparison}
\ \longrightarrow\
\text{complete core response}.
\tag{WC15}
\]
A continuum proof must establish analogous estimates for the actual integrated effective law and its induced metrics at a fixed physical scale, without assuming the desired clustering or spectral edge. The collar bound removes the surface-cardinality loss under its hypotheses; it does not prove that those hypotheses survive RG.

[[rg-covariance-residue/regional-gauge-readouts-and-conditional-lifting|Regional gauge lifting]] extends the one-step calculation to normalized probabilistic readouts on an enlarged joint law. The collar bound can reduce retained boundary sensitivity; it does not automatically improve control of all discarded collar observables. [[bridge-data-augmentation-solder/coarse-boundary-leakage-and-response-lifting|Multiscale lifting]] still requires the actual iterated conditional geometry and a uniformly finite total loss. The one-step constants above do not supply that continuum tower.

The quantity to keep fixed is the physical core--boundary separation, not the list of all interior variables. [[gaussian-bridge-gap-calibration/predictive-rank-and-physical-separation|The Gaussian separation test]] has a vanishing all-interior floor but a positive midpoint floor. It also shows that small mixed Fisher norm need not yield a lower-rank sufficient interface; [[rg-covariance-residue/exact-wilson-interface-statistics|exact cross-plaquette reduction]] alone cannot bridge that distinction.
