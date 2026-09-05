# Wilson Frustration and Joint Escape

The explicit \(SU(3)\) link conditional with two deep wells is not a local minimum of its full Wilson environment. Moving a surrounding link gives an exact downhill path. More strongly, a gauge-invariant neighborhood of that exterior obeys a joint localization inequality with a fixed absorption margin and no volume-dependent constant. This controls one genuine unfavorable context without assuming it is improbable.

**Status: [EXACT FINITE-WILSON ESCAPE AND LOCALIZATION THEOREM], uniform in ambient volume and valid for every \(\beta>0\); [NOT A COVER OF ALL UNFAVORABLE CONTEXTS OR A PHYSICAL MASS-GAP PROOF].**

## Fix the complete action and the neighborhood

Use a four-dimensional ordinary hypercubic lattice, with the displayed patch in its interior and no short periodic identifications. A periodic side length at least five suffices. Let
\[
S=\beta\sum_p(1-\phi_p),\qquad
\phi_p=\tfrac13\operatorname{ReTr}U_p,\qquad
\mu(dU)=Z^{-1}e^{-S}\prod_e dU_e,\qquad \beta>0,
\tag{JE1}
\]
with normalized \(SU(3)\) Haar measure and link metric
\[
g(X,Y)=-\tfrac13\operatorname{ReTr}(XY).
\]
The sum includes every surrounding plaquette, not just those touching the active link.

Choose an active link \(e\) in direction \(i\). Its six transverse neighbors carry six distinct parallel outer links; call their set \(J\). These outer links share no plaquette with each other. Each belongs to one plaquette containing \(e\) and five further plaquettes. Thus the plaquettes touching \(J\) divide into six active plaquettes and thirty external plaquettes, denoted \(\mathcal P_{\mathrm{ext}}\).

Retain every link except \(U_e\), writing the retained configuration as \(R\). Define
\[
B=\{R:\phi_p(R)\le-2/5\ \text{for all }p\in\mathcal P_{\mathrm{ext}}\}.
\tag{JE2}
\]
Every defining plaquette excludes \(e\), so \(B\) really is a retained-context set. It is gauge invariant.

The [[frustrated-su3-conditional-wells|two-well realization]] belongs to the interior of \(B\): set all transverse and remaining links to identity, three outer links to \(zI\), and three to \(z^2I\), where \(z=e^{2\pi i/3}\). Every external plaquette then has \(\phi_p=-1/2\), while the active conditional is \(q_\beta(U_e)\propto e^{-\beta\operatorname{ReTr}U_e}\). For each fixed \(\beta\), an open neighborhood therefore has both the prior small conditional Rayleigh quotients and the joint bound below. The continuity neighborhood may depend on \(\beta\); the set \(B\) and the localization constants below do not require a coupling-independent neighborhood for those conditional quotients.

## The frozen wells have exact downhill context directions

At a fully central link configuration, every plaquette is \(z_pI\). For \(U_e(t)=U_e e^{tX_e}\), tracelessness makes the first variation vanish. Trace commutators cancel in the second variation, giving
\[
\operatorname{Hess}S[X,X]
=\beta\sum_p\operatorname{Re}(z_p)
\left\|\sum_{e\in\partial p}\epsilon_{pe}X_e\right\|_g^2.
\tag{JE3}
\]
The signed sum is the ordinary linear cochain differential here because all adjoint transports are trivial at central links.

Its values are constrained to the compatible image of that differential. [[hessian-response-geometry/compatible-image-and-signed-curvature|The signed-image criterion]] gives the exact relative instability test; a negative plaquette coefficient alone is not a choice of a realizable variation.

At the active well \(U_e=zI\), the active-link coefficient is \(3-3/2=3/2\). Each of the three opposite-phase outer links has six nontrivial central plaquettes, giving coefficient \(-3\). Each matching-phase outer link has one identity and five nontrivial plaquettes, giving coefficient \(-3/2\). The outer-link coordinate space is consequently a 48-dimensional negative-definite restriction of the full Hessian. This is not an eigenvector claim about those individual coordinates. These variations change plaquette curvature and are not pure gauge.

There is also a finite path, not merely a Taylor test. For one opposite-phase outer link use
\[
U_j(t)=z^2e^{tT},\qquad T=i\,\operatorname{diag}(1,-1,0).
\]
Since \(\operatorname{Tr}e^{\pm tT}=1+2\cos t\) is real, all six changed plaquette traces give exactly
\[
\boxed{S(t)-S(0)=2\beta(\cos t-1).}
\tag{JE4}
\]
The full action decreases strictly for \(0<t<\pi\), dropping by \(4\beta\) at \(\pi\). A matching-phase outer link gives \(\beta(\cos t-1)\). Interchange \(z\) and \(z^2\) for the other active well.

## The action Laplacian supplies a test-uniform certificate

With the declared metric, an orthonormal basis \(T_a\) satisfies
\[
\sum_{a=1}^8T_a^2=-8I.
\]
Thus, whenever a plaquette traverses a link once,
\[
\Delta_j\phi_p=-8\phi_p.
\tag{JE5}
\]
Let \(\Delta_J=\sum_{j\in J}\Delta_j\). The incidence partition above gives
\[
\Delta_JS=8\beta\sum_{p\cap J\ne\varnothing}\phi_p.
\tag{JE6}
\]
On \(B\), each of the six active plaquettes is bounded by \(\phi_p\le1\), irrespective of \(U_e\). Therefore
\[
\Delta_JS\le8\beta[6-30(2/5)]=-48\beta
\quad\text{on }B,
\qquad
\Delta_JS\le288\beta\quad\text{everywhere}.
\tag{JE7}
\]
The second estimate counts all 36 touching plaquettes. No distributional approximation enters either bound.

Take the local action
\[
S_J=\beta\sum_{p\cap J\ne\varnothing}(1-\phi_p),\qquad
W=e^{S_J},
\]
and the actual symmetric partial generator and form
\[
L_J=\Delta_J-\nabla_JS\cdot\nabla_J,\qquad
\mathcal E_J(f)=\int\sum_{j\in J}|\nabla_jf|^2\,d\mu.
\tag{JE8}
\]
There is no \(1/2\) in this form convention. Because \(\nabla_JS_J=\nabla_JS\), [[conditional-fisher-coercivity/lyapunov-localization-certificate|the exact Lyapunov identity]] gives
\[
-L_JW/W=-\Delta_JS.
\]
Equation (JE7) supplies its constants \(\delta=48\beta\), \(M=288\beta\).

Let \(P=\mathbb E_\mu[\cdot\mid R]\), \(K=\{e\}\cup J\), and
\(P_C=\mathbb E_\mu[\cdot\mid U_{K^c}]\). Thus \(Q_K=I-P_C\) is the innovation of a joint seven-link update. For all tests in the closed form domain,
\[
\boxed{
\|\mathbf1_B(I-P)f\|_{L^2(\mu)}^2
\le\frac{\mathcal E_J(f)}{336\beta}
+\frac67\|Q_Kf\|_{L^2(\mu)}^2.}
\tag{JE9}
\]
For completeness, apply the positive-function identity to \(g=f-P_Cf\):
\[
336\beta\|\mathbf1_Bg\|^2
\le\mathcal E_J(g)+288\beta\|g\|^2.
\]
Because \(P_Cf\) is independent of \(J\), \(\mathcal E_J(g)=\mathcal E_J(f)\). Moreover \(P_Cf\) is \(R\)-measurable and \(B\) is a retained set, so conditional variance gives \(\|\mathbf1_B(I-P)f\|^2\le\|\mathbf1_Bg\|^2\). This avoids an unjustified derivative estimate on \(Pf\). Smooth positive finite-dimensional densities justify the conditional-mean operation on the smooth core, followed by closed-form extension.

Since \(\|Q_Kf\|^2\le\operatorname{Var}_\mu f\), the global-variance version of (JE9) follows too. The stronger block-local remainder is useful when combining patches.

Tests vanishing outside \(B\) satisfy the stronger supported-test statement
\[
\boxed{\mathcal E_J(f)\ge48\beta\|f\|^2.}
\tag{JE10}
\]
The fixed absorption margin \(1/7\) in (JE9) and the coefficient \(1/(336\beta)\) do not deteriorate with ambient volume. For \(\beta\ge\beta_0>0\) they are uniform in coupling as well. Neither \(\nu(B)\) nor a supposed typical boundary was used.

The action, \(B\), and selected-link form are gauge invariant, and \(P\) is equivariant. The estimates consequently restrict to gauge-invariant tests without selecting a singular gauge slice.

## Summing patches gives a form comparison, not an extensive variance penalty

On the periodic lattice, make this geometric selection for each positively oriented active link \(e\), with its own \(B_e,J_e,K_e\) and single-link innovation \(Q_e\). Every link belongs to exactly six outer sets \(J_e\). Summing (JE9) therefore gives
\[
\boxed{
\sum_e\|\mathbf1_{B_e}Q_ef\|^2
\le\frac{\mathcal E_{\mathrm{full}}(f)}{56\beta}
+\frac67\sum_e\|Q_{K_e}f\|^2.}
\tag{JE11}
\]
Both sides are sums of local forms on the same law. The last term is the Dirichlet form of the auxiliary joint-block heatbath with rate one for each \(K_e\). It is not the number of patches times the full variance.

The coefficients in this form comparison are volume independent. That does not establish a volume-independent spectral gap: a comparison controlling the block innovations and the remaining single-link sectors is still needed. In particular, no absorption of the final sum has been proved.

## What remains after this escape is controlled

The frozen active-link gap can shrink exponentially while the joint cost of confining a test to this exterior grows linearly in \(\beta\). These are different operators on different carriers. Holding the context immobile created an obstruction which is not stable under the joint variations.

This is an actual-law instance of [[conditional-fisher-coercivity/bad-context-response-and-localization|bad-context control]], but it is not a global Poincare theorem. The complement \(B^c\) has not been shown to have uniformly good fiber gaps. Other exteriors can give the same frustrated staple sum without placing thirty surrounding plaquettes in the region (JE2). A complete construction must cover or otherwise control those additional geometries, avoid accumulating losses under overlapping patches, and bound the retained mean and physical transfer through the continuum limit.

[[wilson-exterior-force-localization|Exterior-force localization]] extends the construction to an unequal-well exterior with positive external plaquette traces. Its half-action localizer combines force and curvature in one retained certificate and covers the union of the two displayed regions for \(\beta\ge28\), with one block-local remainder. The complement and that remainder remain to be controlled.

The local arithmetic constants are consequences of a declared lattice, group metric and cut. They are not a mass quantum or an independently selected physical yardstick.

[[receipts/joint_context_escape_receipt.py|The finite receipt]] checks full-lattice incidence, the exact finite escapes, signed Hessians, Casimir-normalized nonlinear Laplacians and the positive-function identity. The uniform theorem is the proof above, not finite sampling.
