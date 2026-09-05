# Second-Ring Escape Preserves the Original Wilson Innovation

A farther link can change the cost of a frustrated Wilson environment without changing the active link's conditional law. For the explicit context previously controlled by a three-link remainder, one second-ring link gives a same-innovation localization estimate with overlap one. The improvement holds on a new cut containing that context, not on the entire earlier coherent-support cut.

## Move outside the active interaction star

Use the full four-dimensional Wilson law and metric of [[coherent-staple-localization|coherent staple localization]], at \(\beta>0\), on a periodic lattice of side at least seven. For each active orientation \(\mu\), fix one transverse direction \(\tau(\mu)\ne\mu\). If \(e=(x,\mu)\), select
\[
j(e)=(x+2\hat\tau(\mu),\mu),\qquad
\Theta_e(R)=\sum_{p\ni j(e)}\phi_p(R),\qquad
B_{e,r}=\{\Theta_e\le-r\},\quad r>0.
\tag{SE1}
\]
Exactly six plaquettes meet \(j(e)\), and none contains \(e\). Every active staple therefore excludes the differentiated link. The cut is retained-measurable and gauge invariant; its definition does not depend on \(\beta\).

With \(P_e=\mathbb E[\cdot\mid U_{e^c}]\) and \(Q_e=I-P_e\), every fixed-coordinate Lie derivative at \(j(e)\) commutes with \(P_e\). Thus
\[
\mathcal E_{j(e)}(Q_ef)\le\mathcal E_{j(e)}(f).
\tag{SE2}
\]
This is exact conditional independence, not a small-score approximation. It avoids the [[singular-staple-fibers-and-exact-conditional-symmetries|outer-only source-fiber obstruction]] by acting on a coordinate absent from the source.

## An action localizer has a same-innovation remainder

Let \(S_j\) contain all six plaquettes meeting \(j=j(e)\), with
\(L_j=\Delta_j-\nabla_jS\cdot\nabla_j\) and \(W=e^{S_j}\). The normalized Casimir and the positive-function identity give
\[
V_W=-L_jW/W=-\Delta_jS=-8\beta\Theta_e,\qquad
V_W\ge8r\beta\ \text{on }B_{e,r},\qquad
V_W\ge-48\beta\ \text{everywhere}.
\tag{SE3}
\]
Apply [[conditional-fisher-coercivity/lyapunov-localization-certificate|commuting localization]] directly to \(Q_ef\), using (SE2):
\[
\boxed{
\|\mathbf1_{B_{e,r}}Q_ef\|^2
\le\frac{\mathcal E_{j(e)}(f)}{8\beta(r+6)}
+\frac6{r+6}\|Q_ef\|^2.}
\tag{SE4}
\]
All norms use the same complete Wilson law, and the inequality extends to its closed gradient form domain. Gauge-invariant tests are included. No derivative of the cut or the active conditional mean is taken.

The map \(e\mapsto j(e)\) is a translation separately in each orientation, hence a bijection of lattice links. Summing costs no overlap factor:
\[
\sum_e\|\mathbf1_{B_{e,r}}Q_ef\|^2
\le\frac{\mathcal E_{\mathrm{full}}(f)}{8\beta(r+6)}
+\frac6{r+6}\mathcal H_{\mathrm{hb}}[f],
\qquad
\mathcal H_{\mathrm{hb}}[f]=\sum_e\|Q_ef\|^2.
\tag{SE5}
\]
Unlike an enlarged-block remainder, the last form is exactly the original innovation sum. If the complementary contexts independently obey
\(\sum_e\|\mathbf1_{B_{e,r}^c}Q_ef\|^2\le C_g\mathcal E_{\mathrm{full}}(f)\),
then
\[
\boxed{
\mathcal H_{\mathrm{hb}}[f]\le
\left(\frac{r+6}{r}C_g+\frac1{8r\beta}\right)
\mathcal E_{\mathrm{full}}(f).}
\tag{SE6}
\]
That complementary estimate is not established. Even with it, a separate lower bound for \(\mathcal H_{\mathrm{hb}}\) and the physical transfer/continuum construction would remain necessary.

## The earlier displayed context lies inside this cut

Take exactly the link assignment (CS6)--(CS8) of [[coherent-staple-localization|the coherent-support note]], with \(\tau(\mu)=\nu_3\). At \(j=x+2\hat\nu_3\), the parallel link is \(zI\). Its neighbor at \(x+\hat\nu_3\) is \(zI\), and its five other transverse neighbors are identity. The transverse links themselves are identity. Its six touching traces are therefore
\[
1,-\tfrac12,-\tfrac12,-\tfrac12,-\tfrac12,-\tfrac12,\qquad
\Theta_e=-\tfrac32.
\tag{SE7}
\]
The individual-link Hessian is \(-3\beta g/2\), and \(\Delta_jS=-12\beta\). Choosing \(r=1\) leaves a strict margin, so \(B_{e,1}\) contains an open neighborhood of this exterior, fixed independently of coupling. Equations (SE4)--(SE5) become
\[
\boxed{\|\mathbf1_{B_{e,1}}Q_ef\|^2
\le\frac{\mathcal E_{j(e)}(f)}{56\beta}+\frac67\|Q_ef\|^2.}
\tag{SE8}
\]
At the exact point, \(r=3/2\) instead gives coefficients \(1/(60\beta)\) and \(4/5\); the strict \(r=1\) choice supplies the neighborhood.

The earlier coherent-support theorem remains valid on its own larger-defined cut. Its new-context example, however, does not require the three-link residual once this second-ring direction is noticed. The cuts have different definitions; no global containment or domination is asserted.

[[conditional-fisher-coercivity/finite-patch-projection-coercivity#An enlarged remainder is not absorbed by declaring its coefficient small|The projection-incidence obstruction]] explains why this change of derivative matters: the earlier three-link block sum cannot be absorbed through a scalar comparison with the single-link sum, even in the gauge-invariant sector. Here no such comparison is needed.

The [[critical-context-and-collective-escape|critical strip example]] still requires collective motion rather than this coordinate diagnostic. Neither construction proves exhaustive coverage, and neither auxiliary diffusion rate is a glueball mass.

The [[receipts/commuting_context_rigidity_receipt.py|finite receipt]] checks the actual six-plaquette neighborhood, independence from the active source, nonlinear Casimir derivatives, gauge covariance and onefold overlap. The all-test inequality is the direct proof of (SE4).
