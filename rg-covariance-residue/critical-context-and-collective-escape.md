# A Critical Context Requires Collective Escape

There is a compatible central Wilson configuration where the force vanishes, every individual link has positive quadratic response, and the active conditional still has two deep wells. A coordinated variation of 72 retained links gives negative curvature. Transporting that variation through a retained tree yields a smooth gauge-invariant joint localization estimate, with constants independent of ambient volume and no change to the Wilson law.

**Status: [EXACT FINITE-WILSON COLLECTIVE ESCAPE AND SAME-LINK CONTEXT BOUND]; [OPEN] complete context coverage, heat-bath coercivity and physical continuum gap.**

## A critical configuration missed by individual-link diagnostics

Use the full four-dimensional Wilson action and normalized link metric of [[wilson-frustration-and-joint-escape|joint Wilson escape]], on a periodic lattice of side \(L\ge8\). Let \(z=e^{2\pi i/3}\), \(s(r)=\mathbf1_{\{0,1\}}(r)\), and set
\[
U_0(x)=z^{s(x_1)+s(x_2)+s(x_3)}I,\qquad
U_i(x)=I\quad(i=1,2,3).
\tag{CE1}
\]
These are actual links. Their plaquettes therefore satisfy the lattice compatibility identities. Nontrivial plaquettes occur only at the two boundaries of each selected transverse strip.

All plaquettes are central, so every first variation vanishes by tracelessness. For the active link \(e\) in direction zero at the origin, the six complementary staples consist of three \(I\)'s and three \(z^2I\)'s:
\[
S_{\mathrm{staple}}=3(I+z^2I)=-3zI.
\tag{CE2}
\]
The conditional has exponent \(-\beta\operatorname{ReTr}(U_e^*z)\). The change \(U_e=zV\) reduces it to the [[frustrated-su3-conditional-wells|two-well family]], with wells \(U_e=I,z^2I\) and an exponentially small conditional gradient floor as \(\beta\) grows.

At a central configuration, the full Hessian is
\[
\operatorname{Hess}S[X,X]
=\beta\sum_p w_p\|(dX)_p\|_g^2,\qquad
w_p\in\{1,-1/2\}.
\tag{CE3}
\]
A direction-zero link meets at most three negative plaquettes; its individual-link Hessian is at least \(3\beta g/2\). A spatial link meets at most two; its individual-link Hessian is at least \(3\beta g\). Thus every coordinate link is strictly stable to second order.

For the active six-outer-link patch, the external trace sum is \(15/2\) and all exterior forces vanish. The previous [[wilson-exterior-force-localization#One retained certificate combines force and curvature|adaptive certificate]] is therefore
\[
\chi_\beta=-4\beta(6+15/2)=-54\beta<0.
\tag{CE4}
\]
This is a concrete uncovered context, not merely a possible flaw in that sufficient cut.

## A finite compatible direction has negative curvature

Let \(J\) consist of the 72 direction-zero links with
\[
x_0=1,\quad x_1\in\{0,1\},\quad x_2,x_3\in\{0,\ldots,5\}.
\]
Define \(v(r)=\sin[\pi(r+1)/7]\) on \(r=0,\ldots,5\), and zero elsewhere. Put
\[
a_x=\frac{\sqrt2}{7}s(x_1)v(x_2)v(x_3)
\quad(x_0=1),\qquad \sum_{j\in J}a_j^2=1.
\tag{CE5}
\]
The normalization follows from \(\sum_{r=0}^5v(r)^2=7/2\). For one unit Lie-algebra tangent \(T\), take \(X_j=a_jT\) on \(J\), zero elsewhere.

The \(x_1\)-curl lies on the two negative strip boundaries and contributes exactly \(-\beta/2\). Each of the other two spatial curl contributions is at most its positive-weight Dirichlet form. The zero-extended sine vector has
\[
\frac{\sum_r|v(r+1)-v(r)|^2}{\sum_r|v(r)|^2}
=4\sin^2(\pi/14).
\]
Therefore
\[
\boxed{
\operatorname{Hess}S[X,X]\le-\nu\beta,\qquad
\nu=\tfrac12-8\sin^2(\pi/14)>0.}
\tag{CE6}
\]
Numerically \(\nu\approx0.103875\); the proof is the sine identity and signed bound, not that decimal.

No plaquette containing a selected link contains the active link: their direction-zero links have different \(x_0\). All affected plaquettes must nevertheless remain in the action. The variation changes curvature and cannot be a pure gauge tangent.

[[hessian-response-geometry/compatible-image-and-signed-curvature|The compatible-image theorem]] gives the general meaning of (CE6). The negative plaquette sector must overlap sufficiently with the image of the link-to-plaquette differential. Positive individual-link diagonals do not test that overlap.

## A retained tree preserves coherent transport without gauge fixing

A negative Hessian at one point is not yet a localization theorem. To extend this direction smoothly and gauge covariantly, connect the sources of all links in \(J\) to \(r=(1,0,0,0)\) by a fixed tree of spatial links at \(x_0=1\). A tree with 71 edges suffices. It contains neither \(e\) nor a member of \(J\).

Let \(P_j\) be the ordered tree holonomy from the source of \(j\) to \(r\). For a root basis \(T_A\), orthonormal in \(g=-\operatorname{ReTr}/3\), define the collective vector fields by
\[
\mathscr X_A U_j=a_j(P_jT_AP_j^*)U_j
\quad(j\in J),\qquad
\mathscr X_A U_k=0\quad(k\notin J).
\tag{CE7}
\]
The tree is not differentiated, so \(\mathscr X_A P_j=0\). Each vector field is smooth and divergence-free for product Haar measure. At (CE1), every tree holonomy is identity.

Under a lattice gauge transformation, the eight root directions mix by the same orthogonal adjoint matrix. Summing over \(A\) therefore gives a gauge-invariant operator and form; no gauge slice is chosen. Averaging independent frames at every link would instead risk deleting the cross terms responsible for the collective variation.

With the inherited selected-link gradients,
\[
\sum_A|\mathscr X_A f|^2
\le\left(\sum_j a_j^2\right)\sum_{j\in J}|\nabla_j f|^2
=|\nabla_Jf|^2.
\tag{CE8}
\]
The coefficients and tree are chosen from patch geometry, not from an unknown mass spectrum.

## The collective localizer is an actual-law comparison

Let \(S_J\) contain every plaquette touching \(J\), and use
\[
\mathcal L=\sum_A\left[\mathscr X_A^2
-(\mathscr X_AS)\mathscr X_A\right],\qquad
\mathcal E_{\mathscr X}(f)=\int\sum_A|\mathscr X_Af|^2\,d\mu.
\tag{CE9}
\]
Haar divergence-freeness makes this generator symmetric for the full law \(\mu\propto e^{-S}\). Take the closure of the smooth-core form. By (CE8), it is dominated on the full gradient form domain by \(\mathcal E_J\).

Since \(\mathscr X_AS_J=\mathscr X_AS\), the [[conditional-fisher-coercivity/lyapunov-localization-certificate|positive-function identity]] with \(W=e^{S_J}\) gives
\[
-\mathcal LW/W=-\sum_A\mathscr X_A^2S.
\tag{CE10}
\]
At (CE1), summing (CE6) over the eight root directions gives a lower bound \(8\nu\beta\) for (CE10).

There is also a global bound. The basis satisfies \(\sum_AT_A^2=-8I\). Diagonal second-derivative terms use that identity, while mixed terms obey Hilbert--Schmidt Cauchy--Schwarz, yielding
\[
\left|\sum_A\mathscr X_A^2\phi_p\right|
\le8\left(\sum_{j\in p\cap J}|a_j|\right)^2.
\tag{CE11}
\]
Each plaquette contains at most two selected links, and each selected link belongs to six plaquettes. Hence
\[
\left|\sum_A\mathscr X_A^2S\right|
\le8\beta\sum_p\left(\sum_{j\in p\cap J}|a_j|\right)^2
\le96\beta.
\tag{CE12}
\]

The retained, gauge-invariant set
\[
B_{\mathrm{coll}}
=\left\{R:-\beta^{-1}\sum_A\mathscr X_A^2S(R)\ge4\nu\right\}
\tag{CE13}
\]
contains an open neighborhood of the displayed exterior. The action terms and tree in (CE13) exclude the active link, so this condition is uniform in arbitrary \(U_e\). The factor \(\beta\) cancels from its definition; the cut and its neighborhood do not depend on coupling.

Put \(P_e=\mathbb E[\cdot\mid R]\), \(Q_e=I-P_e\). No plaquette meets both \(e\) and \(J\), so the active conditional density is independent of every differentiated link. The tree coefficients also exclude \(U_e\). Hence
\[
\mathscr X_AP_e=P_e\mathscr X_A,\qquad
\mathcal E_{\mathscr X}(Q_ef)\le\mathcal E_{\mathscr X}(f)\le\mathcal E_J(f).
\]
The [[conditional-fisher-coercivity/lyapunov-localization-certificate#Commuting escape preserves the original innovation|commuting-escape certificate]], with \(\delta=4\nu\beta\) and \(M=96\beta\), therefore gives
\[
\boxed{
\|\mathbf1_{B_{\mathrm{coll}}}Q_e f\|^2
\le\frac{\mathcal E_J(f)}{\beta(96+4\nu)}
+\frac{96}{96+4\nu}\|Q_ef\|^2,\qquad\beta>0.}
\tag{CE14}
\]
This improves the earlier valid bound with \(Q_{\{e\}\cup J}\): its 73-link remainder was unnecessary. The improvement uses exact conditional independence under the selected derivatives, not smallness of a moving score. Tests supported in the cut also satisfy \(\mathcal E_J(f)\ge4\nu\beta\|f\|^2\).

The same-link coefficient \(b=96/(96+4\nu)\approx0.99569<1\) is suitable for absorption in a **complete** good/bad single-link decomposition. Choose one prescribed transverse ordering for each active direction and translate its patch to every active link. The 72-fold selected-link overlap gives summed gradient coefficient \(A=72/[\beta(96+4\nu)]\). If the complementary contexts separately satisfy \(\sum_e\|\mathbf1_{B_e^c}Q_ef\|^2\le C_g\mathcal E_{\rm full}(f)\), then
\[
\sum_e\|Q_ef\|^2\le
\left(\frac{96+4\nu}{4\nu}C_g+\frac{18}{\nu\beta}\right)
\mathcal E_{\rm full}(f).
\tag{CE15}
\]
That complementary estimate is not proved: the collective cut does not cover every unfavorable conditional. A separate gap for the site-innovation form would then be needed to control the full variance. Summing every rotation changes the overlap. These are volume-independent form coefficients, not an established volume-independent physical gap.

## Source boundary and the remaining question

[[library/k-string-tensions-and-center-vortices-at-large-n/inq|Greensite--Olejnik]] derives the central cosine-weight expansion and a plaquettewise sufficient stability condition in Section 3. The compatible-image test here does not treat a negative coefficient as an independent curvature variation. Our explicit linked construction proves one collective instability, not instability of every nonflat central configuration.

All results above concern the fundamental Wilson action. Replacing it with a blocked or adjoint-extended action changes the Hessian and requires a new proof.

This extends context control to a force-zero geometry missed by the previous cut and removes its enlarged-block remainder. Other central and noncentral contexts, global site-innovation coercivity and the physical transfer/continuum limits remain open. The seven-link remainders of the neighboring escape constructions do not inherit this commutation: their differentiated links enter the active conditional source. A classical negative mode is neither a glueball nor a quantum mass-gap theorem.

[[receipts/collective_context_escape_receipt.py|The finite receipt]] checks the full lattice, source, individual Hessians, supported collective curvature, transported gauge covariance and nonlinear localizer. It also checks the compatible-image theorem on rank-deficient finite matrices.
