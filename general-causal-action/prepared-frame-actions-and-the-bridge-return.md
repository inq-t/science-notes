# Prepared Frame Actions and the Bridge Return

A Gaussian preparation can compare a group increment and then let that increment act on several linked readouts. For the three-cell chain, two such actions supply exactly the missing upper and lower bridge motion. Their symmetric composition with the calibrated common-endpoint transfer is positive, injective and Markov at every finite width, and returns the complete inherited three-cell electric operator. A weak physical endpoint potential gives its interacting vacuum. Independent bridge preparations and their paces are declared inputs; their compatibility with a shared ancestral preparation law remains a separate construction problem.

## Prepare an increment, then apply its actual action

Use the faithful representation and sufficient matrix inventory of [[general-group-preparation-and-the-casimir-return|the general-group preparation theorem]]: \(G\) is compact and connected with simple Lie algebra, \(\rho:G\to U(n)\) is faithful, \(\Xi\in\mathbb C^{n\times k}\) is isotropic circular Gaussian of variance \(\sigma^2\), and \(k>n+\dim(G)/2\). Fix a bi-invariant metric \(Q=sQ_\rho\), \(s>0\), where \(Q_\rho(X,Y)=-\operatorname{Re}\operatorname{Tr}[d\rho(X)d\rho(Y)]\). Simplicity ensures that this includes every bi-invariant metric up to the declared scale.

For a comparison pace \(r>0\), define the central probability density
\[
\begin{aligned}
\eta_{\alpha,r}(h)
&=\frac1{z_{\alpha,r}}\mathbb E
\exp\!\left[-\frac{\alpha}{r}
\|[\rho(h)-I]\Xi\|^2\right],\\
z_{\alpha,r}
&=\mathbb E\int_G
\exp\!\left[-\frac{\alpha}{r}
\|[\rho(h)-I]\Xi\|^2\right]dh.
\end{aligned}
\tag{FA1}
\]
Write \(\gamma_Q>0\) for the coefficient returned by the unit-pace kernel relative to \(D_Q=-\Delta_Q\). In the notation of (GG11), \(\gamma_Q=s\,c_{\rho,k,\sigma}/4\). The general-group theorem proves
\[
\alpha(R_{\alpha,r}-I)f\longrightarrow-r\gamma_QD_Qf,
\qquad
R_{\alpha,r}f(g)=\int_G\eta_{\alpha,r}(h)f(gh)dh.
\tag{FA2}
\]
This is the same preparation law, with the pace used in both numerator and scalar normalization.

Let \(\Phi\) be a smooth left action of \(G\) preserving a probability measure \(dq\) on a compact smooth carrier \(M\). Its unitary representation is \(U_hf(q)=f(\Phi_{h^{-1}}q)\). Because \(\eta_{\alpha,r}\) is inversion symmetric, its prepared action operator may equally be written
\[
T_{\Phi,\alpha,r}f(q)
=\int_G\eta_{\alpha,r}(h)f(\Phi_hq)dh.
\tag{FA3}
\]
This operator is a self-adjoint Markov contraction. It is also Hilbert positive and injective, even if the action is not transitive or faithful. Indeed, the compact-group representation decomposes as
\[
L^2(M)=\widehat{\bigoplus}_{\tau}
V_\tau\otimes\mathcal M_\tau,\qquad
T_{\Phi,\alpha,r}
=\widehat{\bigoplus}_{\tau}
b_{\alpha/r,\tau}\,I_{V_\tau}\otimes I_{\mathcal M_\tau},
\qquad b_{\alpha/r,\tau}>0.
\tag{FA4}
\]
The strictly positive scalar multipliers are those of (GG3); the action only selects their multiplicities. Hence \(\langle f,T_{\Phi,\alpha,r}f\rangle>0\) for every nonzero \(f\), although no uniform positive lower bound over all sectors is asserted. Pointwise positivity and the unit row sum follow independently from the probability average in (FA3).

For a \(Q\)-orthonormal basis \(e_A\), put
\[
\mathscr D_{\Phi,A}f(q)
=\left.\frac{d}{dt}f(\Phi_{\exp(te_A)}q)\right|_0,
\qquad
D_\Phi=-\sum_A\mathscr D_{\Phi,A}^{\,2}.
\]
Then
\[
\boxed{\alpha(T_{\Phi,\alpha,r}-I)f
\longrightarrow-r\gamma_QD_\Phi f}
\quad\text{uniformly for }f\in C^\infty(M).
\tag{FA5}
\]
To prove this, apply the inversion-symmetric Taylor calculation of (GG9–10) to \(h\mapsto f(\Phi_hq)\). Compactness makes its derivatives and second-order remainder uniform in \(q\). The same preparation inverse moments dominate the averaged second moment and its spatial tail. The infinitesimal generator of the representation \(U\) has the opposite sign to \(\mathscr D_\Phi\), which disappears upon squaring. No freeness assumption, ellipticity of the individual action, or density kernel on all of \(M\times M\) is required: an individual transition can remain supported on one action orbit.

## The two missing bridges are genuine group actions

Take \(M=G^3\) with product Haar and coordinates \((x,y,z)\) from [[three-cell-incidence-and-shared-path-motion|the three-cell incidence calculation]]. Its full physical carrier is \(L^2(G^3)^{\operatorname{Ad}G}\). Retain the actual upper and lower bridge actions
\[
\begin{aligned}
A_h(x,y,z)&=(x,hy,hzh^{-1}),&
\mathscr D_{a,X}&=L_{y,X}+C_{z,X},\\
B_h(x,y,z)&=(x,yh^{-1},z),&
\mathscr D_{b,X}&=-R_{y,X}.
\end{aligned}
\tag{FA6}
\]
Both are smooth Haar-preserving left actions. They commute with one another. Under simultaneous conjugation \(\mathcal C_g\), they satisfy
\(\mathcal C_gA_h\mathcal C_g^{-1}=A_{ghg^{-1}}\) and the analogous identity for \(B_h\). Centrality of (FA1) therefore makes each averaged operator preserve the entire physical subspace.

The action \(A_h\) is exactly the induced change of the upper raw bridge \(a\); it advances the middle cell and conjugates the later cell's frame. The action \(B_h\) is the lower bridge change in the tree representative. Before choosing that representative its parameter is transported by \(\operatorname{Ad}_p\); the central increment law and invariant metric remove that common frame without discarding its action. Thus (FA6) supplies the rows (TC15), rather than interpreting an extra dependent word as an independent Haar coordinate.

The returned nonnegative action operators are
\[
D_a=-\sum_A(L_{y,A}+C_{z,A})^2,\qquad
D_b=-\sum_A R_{y,A}^{\,2}=D_y.
\tag{FA7}
\]
Their separate kernels may have many fixed functions. Positivity and injectivity in (FA4) concern the transfer operators, not a claim that each bridge generator alone has only a constant zero mode.

## A symmetric composition recovers the whole incidence form

Let \(F_{\parallel,\alpha}\) be the three-access member of [[conditional-access-families-and-the-returned-clock|the conditional family]], with four actual common-endpoint words \(P_0,P_1,P_2,P_3\). Gauge only the final endpoint first. The isometric pullback
\[
(JF)(P_0,P_1,P_2,P_3)
=F(P_0P_1^{-1},P_2P_1^{-1},P_3P_2^{-1})
\tag{FA8}
\]
identifies its quotient with \(L^2(G^3)\), retaining simultaneous root conjugation. Its transported finite-width transfer is positive, injective and Markov on this entire carrier. Choose the declared comparison paces, in numerator and corresponding normalizer, so that its four returned path coefficients are
\[
(\alpha_0,\alpha_1,\alpha_2,\alpha_3)
=(3\kappa,\kappa,\kappa,3\kappa),\qquad \kappa>0.
\tag{FA9}
\]
Here \(\alpha_j\) denotes a returned path coefficient as in (TC11); the finite-width parameter remains \(\alpha\). Every coefficient before pacing is positive and finite, so these choices exist. Scaling the old comparison pace as well is permitted if its old clock is not already \(\kappa\). The inherited conditional covariances, including nonzero parent coefficients, remain in place.

By (CF15) and the actual word change,
\[
\begin{aligned}
\alpha(F_{\parallel,\alpha}-I)f&\longrightarrow-H_\parallel f,\\
\mathcal E_\parallel(f)
&=\kappa\int_{G^3}\!\left[
3|L_xf|^2+3|L_zf|^2+
|(R_x+R_y)f|^2+|(L_y-R_z)f|^2
\right]dq .
\end{aligned}
\tag{FA10}
\]
This is precisely the four-path part of the chain, including its signed mixed derivatives; it is not a diagonal assignment to three cell clocks.

Use independent whole preparations for the bridge substeps, choosing paces \(r_a,r_b>0\) such that
\[
r_a\gamma_Q=r_b\gamma_Q=\frac{\kappa}{2}.
\tag{FA11}
\]
Different faithful Gaussian inventories for the two bridges would merely replace the corresponding \(\gamma_Q\) by their own coefficients. Define
\[
T_{a,\alpha}=T_{A,\alpha,r_a},\quad
T_{b,\alpha}=T_{B,\alpha,r_b},\qquad
\boxed{S_\alpha=
T_{a,\alpha}T_{b,\alpha}F_{\parallel,\alpha}
T_{b,\alpha}T_{a,\alpha}.}
\tag{FA12}
\]
The palindrome is a finite-width positivity statement. For \(K_\alpha=T_{b,\alpha}T_{a,\alpha}\),
\[
\langle f,S_\alpha f\rangle
=\langle K_\alpha f,F_{\parallel,\alpha}K_\alpha f\rangle>0
\quad(f\ne0).
\tag{FA13}
\]
Each factor is injective, and the outer factors are the adjoint of the inner pair. Thus \(S_\alpha\) is positive, self-adjoint and injective. Composition of the probability transitions makes it Markov and a contraction. Every factor commutes with the remaining gauge action. A generic unsymmetrized product would retain the generator sum but would not automatically retain Hilbert positivity.

Telescoping this fixed finite product and using (FA5), (FA10), and strong convergence of every factor to the identity gives
\[
\boxed{
\alpha(S_\alpha-I)f\longrightarrow-H_{\rm ch}f,\qquad
H_{\rm ch}=H_\parallel+\kappa D_a+\kappa D_b.}
\tag{FA14}
\]
The first limit is uniform on smooth functions. Each bridge occurs twice with coefficient \(\kappa/2\), which accounts for the full coefficient \(\kappa\). Its quadratic form is exactly (TC6):
\[
\begin{aligned}
\mathcal E_{\rm ch}(f)=\kappa\int_{G^3}\big[
&3|L_xf|^2+3|L_zf|^2+|R_yf|^2\\
&+|(R_x+R_y)f|^2+|(L_y-R_z)f|^2
+|(L_y+C_z)f|^2\big]dq .
\end{aligned}
\tag{FA15}
\]
In particular the construction restores the end-to-end angular witness (TC14), not merely the individual trace rates.

The individual actions need not preserve a common finite Peter–Weyl truncation on \(G^3\). That is unnecessary. The total form (FA15) is uniformly elliptic on the compact smooth product, with smooth core, \(H^1\) form domain and \(H^2\) operator domain. Its closure generates a contraction semigroup. Set \(S(0)=I\) and \(S(h)=S_{1/h}\) for \(h>0\). Strong continuity at zero, the core derivative (FA14), and contractivity give the Chernoff return
\[
\boxed{S_{N/t}^{\,N}\longrightarrow e^{-tH_{\rm ch}}
\quad\text{strongly},}
\tag{FA16}
\]
uniformly for \(t\) in bounded nonnegative intervals, with the identity at zero. Equivalently, telescope along smooth heat-semigroup orbits: the uniform core error tends to zero, and density plus contractivity extends the limit to all vectors. The same statements hold on the complete simultaneous-gauge invariant carrier.

## Physical interactions and marked substeps remain explicit

Choose a bounded smooth nonnegative gauge-invariant physical endpoint potential, for example
\[
V(x,y,z)=\lambda_x(1-\operatorname{Tr}x/2)
+\lambda_y(1-\operatorname{Tr}y/2)
+\lambda_z(1-\operatorname{Tr}z/2),
\quad \lambda_i\ge0,\quad G=SU(2).
\tag{FA17}
\]
Define \(M_{\alpha,V}f=e^{-V/(2\alpha)}f\) and
\[
S_{\alpha,V}=M_{\alpha,V}S_\alpha M_{\alpha,V}.
\]
It is a positive injective self-adjoint contraction, with row sums at most one. Expansion of the bounded endpoint factors gives
\[
\alpha(S_{\alpha,V}-I)f\longrightarrow-(H_{\rm ch}+V)f,\qquad
S_{N/t,V}^{\,N}\longrightarrow e^{-t(H_{\rm ch}+V)}
\quad\text{strongly}.
\tag{FA18}
\]
The inherited domains are unchanged. Compact connected ellipticity and the real smooth potential give a simple strictly positive ground vector, which is gauge invariant by uniqueness. This is the actual interacting three-cell operator on its full carrier. For \(SU(2)\), coefficients must be converted consistently if one uses \(Q_{\rm TP}=-2\operatorname{Tr}=2Q_\rho\); (FA1–18) already allow this through \(s=2\).

The potential (FA17) is a declared physical insertion. This construction does not yet derive it from the same bridge Gaussian norm, nor does equality of the returned operator establish equality of every finite-width preparation experiment.

There is nevertheless an exact marked amplitude for the new substeps. At each occurrence of a bridge action \(\Phi\), retain its increment \(h\), whole preparation \(\Xi\), and current configuration \(q\). For an admissible mark \(M\), use
\[
(T_{\Phi,\alpha,r}^{M}f)(q)
=\frac1{z_{\alpha,r}}\mathbb E\int_G
M(q,h,\Xi)\,
e^{-\alpha\|[\rho(h)-I]\Xi\|^2/r}
f(\Phi_hq)\,dh .
\tag{FA19}
\]
All source-free normalizers are held fixed. Bounded marks always suffice; Gaussian linear and quadratic marks are admitted where the resulting integral is finite. The central substep retains the complete marked conditional-family kernel. Sewing these five substeps integrates their actual intermediate configurations and increments and retains all scalar factors. Arbitrary integrable cross-substep marks can be inserted in that joint path integral.

The two occurrences of a bridge in (FA12) use independent preparations drawn from the same declared law; the symmetric operator product does not mean reuse of one sampled matrix. Identifying those samples would create a different joint amplitude and would require a new positivity and return proof. Marks need not preserve self-adjointness, positivity or centrality; those claims above concern the source-free transfer.

The result closes the specified finite three-cell incidence mismatch by adding the two actual bridge actions. It does not establish [[conditional-preparation-diagrams-and-ancestral-readout|ancestral marked consistency]] for this enlarged law: forgetting a spatial bridge generally changes its action on retained loops. A common-source construction must still select these actions, correlate or identify their preparations where required, sew their transported port data, and prove the intended retained marked identities. The declared finite calibration supplies neither those laws nor an estimate uniform over growing interacting spatial diagrams.
