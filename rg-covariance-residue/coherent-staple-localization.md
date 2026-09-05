# Coherent Staples Localize a Smaller Wilson Block

The active plaquettes share one link and cannot all reach their individual maxima independently. Preserving this compatibility in the action-Laplacian bound controls a frustrated context missed by the previous exterior-force certificate. An explicit example needs only two surrounding links and leaves a three-link innovation, with constants independent of ambient volume. This improves a concrete part of the joint-response construction; the remaining block form and continuum limit are not controlled.

## Keep the common active link when bounding the action

Use the complete four-dimensional Wilson law and metric of [[wilson-frustration-and-joint-escape|joint escape]]:
\[
\mu\propto e^{-\mathcal S}\prod_e dU_e,\qquad
\mathcal S=\beta\sum_p(1-\phi_p),\qquad
\phi_p=\tfrac13\operatorname{ReTr}U_p,\qquad
g=-\operatorname{ReTr}/3.
\tag{CS1}
\]
Fix an active link \(e\), and a nonempty *geometrically fixed* subset \(I\) of its six outer parallel links. Write \(k=|I|\). No plaquette contains two members of \(I\). Exactly \(k\) touching plaquettes contain \(e\); the other \(5k\) are exterior plaquettes.

Let \(W_j(R)\) be the complementary path of the active plaquette associated with \(j\in I\). All variables except \(U_e\) are retained in \(R\). Define
\[
M_I(R)=\sum_{j\in I}W_j(R),\qquad
\Phi_I^{\rm ext}(R)=\sum_{p\in\mathcal P_{{\rm ext},I}}\phi_p(R),
\]
\[
\boxed{
T_I(R)=h_3(M_I(R))+\Phi_I^{\rm ext}(R),\qquad
B_{I,r}=\{R:T_I(R)\le-r\},\quad r>0.}
\tag{CS2}
\]
The [[special-unitary-source-support|special-unitary support]] \(h_3\) is continuous and endpoint-gauge invariant. Thus \(B_{I,r}\) is a genuine retained, gauge-invariant set. It involves no choice of gauge slice or maximizing branch.

The normalized Casimir gives the exact partial Laplacian
\[
\Delta_I\mathcal S
=8\beta\left[
\tfrac13\operatorname{ReTr}(U_e^*M_I)
+\Phi_I^{\rm ext}\right].
\tag{CS3}
\]
Consequently
\[
\Delta_I\mathcal S\le-8r\beta\quad\hbox{on }B_{I,r},
\qquad
\Delta_I\mathcal S\le48k\beta\quad\hbox{everywhere}.
\tag{CS4}
\]
The global bound counts the actual \(6k\) touching plaquettes. The first inequality keeps their common active-link constraint.

## The exact small-block estimate

Let \(\mathcal S_I\) contain precisely the action terms meeting \(I\), let
\(L_I=\Delta_I-\nabla_I\mathcal S\cdot\nabla_I\), and use the positive function \(W=e^{\mathcal S_I}\). Then
\[
-L_IW/W=-\Delta_I\mathcal S.
\]
Set \(K=\{e\}\cup I\), \(Q_e=I-\mathbb E[\cdot\mid U_{e^c}]\),
\(Q_K=I-\mathbb E[\cdot\mid U_{K^c}]\), and
\(\mathcal E_I(f)=\int|\nabla_I f|^2d\mu\). The [[conditional-fisher-coercivity/lyapunov-localization-certificate|positive-function identity]] and (CS4) prove
\[
\boxed{
\|\mathbf1_{B_{I,r}}Q_ef\|^2
\le
\frac{\mathcal E_I(f)}{8\beta(r+6k)}
+\frac{6k}{r+6k}\|Q_Kf\|^2.}
\tag{CS5}
\]
Indeed apply that identity to \(f-\mathbb E[f\mid U_{K^c}]\). The subtracted function is independent of \(I\), so its subtraction does not change the selected gradient energy. Conditional variance bounds the left side by its restricted squared norm. No derivative of the active conditional mean, the support function, or the cut is used.

The estimate extends from the smooth core to the closed form domain. It restricts to gauge-invariant tests. For tests supported in \(B_{I,r}\), the same identity gives \(\mathcal E_I(f)\ge8r\beta\|f\|^2\).

The choice of \(I\) is fixed before the estimate. Selecting the most favorable \(I\) separately at every configuration does not automatically preserve the same energy and residual constants.

## A realizable context the previous force certificate misses

Take the active edge at the origin in direction \(\mu\), with transverse coordinate directions \(\nu_1,\nu_2,\nu_3\). Put \(z=e^{2\pi i/3}\). Set all transverse links to identity and assign the following parallel links:

- at \(+\nu_a\), assign \(zI\); at \(-\nu_a\), assign \(z^2I\), for \(a=1,2,3\);
- at \(+2\nu_a\), assign \(zI\); at \(-2\nu_a\), assign \(z^2I\);
- at \(\nu_1+\nu_2\), assign \(zI\);
- leave every other exterior parallel link at identity.

Use an interior patch or periodic side at least seven. These are actual link assignments, not independently imposed plaquette values. The six active staples still sum to \(-3I\), so the active conditional is exactly
\(q_\beta(U_e)\propto e^{-\beta\operatorname{ReTr}U_e}\).

Among the thirty exterior plaquettes, eight are identity and twenty-two have nontrivial central phase. Hence
\[
\Phi_J^{\rm ext}=8-22/2=-3.
\tag{CS6}
\]
All exterior forces vanish by centrality and tracelessness. The previous adaptive certificate (EF15) therefore gives
\[
\chi_\beta=-4\beta(6-3)=-12\beta,
\tag{CS7}
\]
which is not a positive localization certificate.

Now choose just the opposite transverse pair
\[
I=\{+\nu_3,-\nu_3\}.
\]
Each selected outer link has one identity and four nontrivial external plaquettes, so \(\Phi_I^{\rm ext}=-2\). Their active staples sum to \(zI+z^2I=-I\). Thus
\[
h_3(M_I)=\tfrac12,\qquad T_I=-\tfrac32.
\tag{CS8}
\]
The \(r=1\) cut contains an open neighborhood of this exterior, fixed independently of \(\beta\), and (CS5) gives
\[
\boxed{
\|\mathbf1_{B_{I,1}}Q_ef\|^2
\le\frac{\mathcal E_I(f)}{104\beta}
+\frac{12}{13}\|Q_{\{e,+\nu_3,-\nu_3\}}f\|^2.}
\tag{CS9}
\]
Its remainder is a three-link innovation, not the earlier seven-link one. At the displayed point, \(r=3/2\) gives \(1/(108\beta)\) and \(8/9\); the strict \(r=1\) choice ensures a neighborhood.

The six-link support cut also covers this exterior: \(h_3(-3I)-3=-3/2\). The smaller subset's benefit is the smaller residual carrier and a different form tradeoff, not a claim that its inequality dominates every larger-block estimate.

Choose one transverse direction geometrically for each active orientation throughout a periodic lattice. Every link then belongs to exactly two selected outer pairs. Summing (CS9) gives
\[
\sum_e\|\mathbf1_{B_e}Q_ef\|^2
\le\frac{\mathcal E_{\rm full}(f)}{52\beta}
+\frac{12}{13}\sum_e\|Q_{K_e}f\|^2.
\tag{CS10}
\]
The residual is a sum of local block forms, not the number of patches times global variance. Its coefficient being below one does not permit absorption. In fact, [[conditional-fisher-coercivity/finite-patch-projection-coercivity#An enlarged remainder is not absorbed by declaring its coefficient small|the neutral plaquette incidence test]] rules out direct scalar absorption of this particular block sum: any comparison to the single-link sum requires a coefficient at least three, while even the best nonempty pair cut has residual coefficient at least \(8/11\).

[[second-ring-commuting-escape|A second-ring derivative]] provides a different improvement at the displayed exterior. The link at \(+2\nu_3\) meets one identity and five nontrivial central plaquettes, none involving the active link. Its new negative-trace cut contains a fixed neighborhood of this point and yields \(1/(56\beta)\) times its gradient energy plus \(6/7\) times the original single-link innovation. This removes the enlarged remainder on that new cut; it does not strengthen (CS5) on the entire original support cut.

## Correcting the placement of the previous flux example

The exterior in [[su3-context-flux-obstruction|the bounded-flux obstruction]] has thirty external traces \(-1/3\) and zero exterior force. It was already controlled by the adaptive (EF15)--(EF17) certificate:
\[
\chi_\beta=-4\beta(6-10)=16\beta>0.
\tag{CS11}
\]
The earlier observation that it lies outside the two simpler cuts did not imply that a new joint localization proof was required. At that exterior, the present six-link support improves the estimate further: \(h_3(-2I)=1\), so \(T_J=-9\). Every \(r<9\) gives a fixed open neighborhood through (CS5). This leaves the frozen single-link transport obstruction intact.

The new context (CS6)--(CS8), by contrast, genuinely defeats the old adaptive certificate while satisfying the coherent support test. This is why retaining common-link geometry changes coverage rather than merely renaming an existing estimate.

## The remaining operator problem

The common-link support expresses compatibility of several observations of the same variable. It lowers an overly permissive bound without modifying the Wilson law, metric, or clock normalization. No extra field, chosen mass, or probability assumption is introduced.

The cuts do not cover all unfavorable contexts. [[critical-context-and-collective-escape|Collective modes]] and the remaining block response still require control. [[singular-staple-fibers-and-exact-conditional-symmetries|The extremal source-fiber theorem]] rules out manufacturing a smooth outer-only commuting escape from the pointwise kernel of the source derivative. Even exhaustive configuration-space localization would not by itself construct the physical Yang--Mills Hamiltonian or its continuum gap.

The [[receipts/coherent_staple_localization_receipt.py|finite receipt]] checks full-lattice incidence, the missed context, the source support, Casimir-normalized Laplacians, gauge covariance and overlap counts. The uniform estimate is the proof of (CS5), not finite sampling.
