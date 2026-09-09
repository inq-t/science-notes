# Preparation Transport through Spatial Subdivision

A pure bivalent subdivision preserves the complete Gaussian experiment when it transports the old preparation, its readouts, sources and integration measures. Replacing that preparation by independent fine variables can match the returned electric and magnetic coefficients while losing a strictly positive mixed source response. The exact construction below specializes [[prepared-vacuum-fisher-comparison/coherent-source-subdivision|coherent source subdivision]] to the weak anchored transfers: it preserves their raw normalization and interacting physical operator, but does not select a preparation inventory for genuinely new cells.

## The coefficient condition includes the comparison pace

Use the one-link convention of [[local-incidence-preparations-and-the-gauge-transfer|local incidence preparations]]. Let \(\Xi_e\in M_2(\mathbb C)\) have circular complex Gaussian covariance \(\sigma_e^2I_4\), with pairing \(\operatorname{Tr}(A^\dagger B)/2\), and set \(S_e=\|\Xi_e\|^2\). Fix duration \(1/\alpha\), comparison weight \(r_e>0\), and
\[
K_{\alpha,e}(u,v)=\mathbb E e^{-(\alpha/r_e)S_ed(u,v)^2},
\qquad d(u,v)^2=2\left[1-\tfrac12\operatorname{Tr}(u^{-1}v)\right].
\tag{PT1}
\]
Its normalized continuum-time generator is \(\kappa_eD_Q\), where \(Q=-2\operatorname{Tr}\) and
\[
\kappa_e=r_e\frac{\mathbb E S_e^{-5/2}}{\mathbb E S_e^{-3/2}}
=\frac{2r_e}{3\sigma_e^2}.
\tag{PT2}
\]
For independently reconstructed fine link clocks, [[holonomy-state-refinement/holonomy-refinement-and-clock-compatibility|the additive clock theorem]] gives the exact condition under \(\pi(U_1,\ldots,U_b)=U_1\cdots U_b\):
\[
\boxed{\kappa_c=\sum_i\kappa_i
\quad\Longleftrightarrow\quad
\frac{r_c}{\sigma_c^2}=\sum_i\frac{r_i}{\sigma_i^2}.}
\tag{PT3}
\]
Necessity here is on the complete boundary-framed carrier. On a fully gauged graph one must use the identifiable cycle sums specified by that theorem.

With every \(r_i=r_c\), (PT3) requires the harmonic covariance rule \(\sigma_c^{-2}=\sum_i\sigma_i^{-2}\); equal pieces have \(\sigma_i^2=b\sigma_c^2\). With every \(\sigma_i^2=\sigma_c^2\), it instead requires the additive pace \(r_c=\sum_i r_i\). A harmonic covariance is therefore conditional on a fixed pace. These constants belong to the rank-four one-link preparation; the rank-eight two-cell word comparison has different constants.

The local incidence magnetic coefficient is
\[
\lambda_f=\frac52\beta_f\sum_e w_{fe}\sigma_e^2,
\qquad \sum_e w_{fe}=1.
\tag{PT4}
\]
Thus fixed covariance, additive pace and normalized redistribution of incidence weights can preserve both coefficients. This is a coefficient test of the limiting generator. Neither (PT3) nor (PT4) proves equality of the finite-width kernels or their marked preparations.

## A mixed source detects an independently reset preparation

Suppose two presentation slots contain unitary images of one original \(\Xi\sim\operatorname{CN}(0,\Gamma)\), with \(\Gamma>0\) on a complex \(m\)-dimensional carrier. Their norm marks measure the same \(S=\|\Xi\|^2\). Near \(t_1=t_2=0\),
\[
\begin{aligned}
Z_{\rm shared}(t_1,t_2)
&=\det[I+(t_1+t_2)\Gamma]^{-1},\\
\left.\partial_{t_1}\partial_{t_2}\log Z_{\rm shared}\right|_0
&=\operatorname{Tr}\Gamma^2>0.
\end{aligned}
\tag{PT5}
\]
For independent fresh variables of any positive covariances \(\Gamma_1,\Gamma_2\),
\[
Z_{\rm fresh}(t_1,t_2)
=\det(I+t_1\Gamma_1)^{-1}\det(I+t_2\Gamma_2)^{-1},
\qquad
\left.\partial_{t_1}\partial_{t_2}\log Z_{\rm fresh}\right|_0=0.
\tag{PT6}
\]
These formulas follow by the finite Gaussian integral; differentiating its logarithm gives the norm covariance. In the isotropic rank-four case the first answer is \(4\sigma^4\). Norms are gauge invariant, so the discrepancy is not an internal gauge direction. This already obstructs equality of the complete preparation laws when independently reset slots are meant to represent copies of the old variable. It does not exclude other explicitly correlated preparations or source maps.

Equations (PT5)–(PT6) use the original Gaussian prior. Localization changes the preparation law: the local incidence owner obtains \(\operatorname{Gamma}(5/2,\sigma_e^2)\) norm laws and the corresponding \(5/2\) mixed coefficient. At a fixed comparison, the actual posterior covariance must be used. No choice among these experiments permits replacing a shared variable by independent copies without checking its mixed sources.

## Transport the preparation on the complete path

For two pieces \(U=U_1U_2\), retain one preparation \(\xi\in E\), with covariance \(\Gamma>0\), and let \(L_U\) denote the unitary left action on its matrix carrier. Introduce the stage readouts
\[
\eta=L_{U_2}\xi,\qquad \zeta=L_{U_1}\eta=L_U\xi,
\qquad
B_{\mathbf U}\xi=
\begin{bmatrix}I\\ L_{U_2}\\L_U\end{bmatrix}\xi.
\tag{PT7}
\]
Their covariance is \(B_{\mathbf U}\Gamma B_{\mathbf U}^\dagger\), supported on the graph of this map. It is not a faithful Gaussian on three independent copies of \(E\). Longer cuts use the successive suffix products; multiplication associativity makes their readouts agree under regrouping. Other original readouts, including the adjoint transports of cell incidences, use their own actual representation maps in the same construction.

Fix \(d_E\xi=\prod_{a=1}^m d^2\xi_a/\pi\) in an orthonormal complex basis and
\(d\gamma_\Gamma(\xi)=(\det\Gamma)^{-1}e^{-\xi^\dagger\Gamma^{-1}\xi}d_E\xi\).
The supported joint law is exactly
\[
d\gamma_\Gamma(\xi)\,
\delta_{\mathbb C}^{m}(\eta-L_{U_2}\xi)\,
\delta_{\mathbb C}^{m}(\zeta-L_{U_1}\eta)\,d_E\eta\,d_E\zeta.
\tag{PT8}
\]
The complex deltas are normalized relative to \(d_E\). Successively integrating \(\zeta,\eta\) gives factor one: their coefficients in those integration fibers are identities. Thus there is no extra Gaussian norm or determinant from inserting the stages. Replacing this pushforward measure by intrinsic volume on the whole graph would change the convention. The distinction and its Jacobians are proved in [[marked-gaussian-constraints-and-sewing-measures|marked Gaussian sewing measures]].

For arbitrary joint linear source \(j\in E^{\oplus3}\) and Hermitian quadratic source \(T\) on all stage readouts, put
\[
j_{\rm eff}=B_{\mathbf U}^\dagger j,\qquad
T_{\rm eff}=B_{\mathbf U}^\dagger TB_{\mathbf U},\qquad
Q=\Gamma^{-1}+T_{\rm eff}>0.
\tag{PT9}
\]
Completing the square in the original \(\xi\) gives the full amplitude
\[
\boxed{\int e^{2\Re(j^\dagger B_{\mathbf U}\xi)
-(B_{\mathbf U}\xi)^\dagger T(B_{\mathbf U}\xi)}\,d\gamma_\Gamma(\xi)
=\frac{\exp(j_{\rm eff}^\dagger Q^{-1}j_{\rm eff})}
{\det\Gamma\,\det Q}.}
\tag{PT10}
\]
Every off-diagonal quadratic block contributes to \(T_{\rm eff}\). For two temporal endpoints, stack both endpoint stage maps on the same \(\xi\). Add the original coarse comparison precision to \(Q\); (PT10) then remains the complete marked kernel. For example, the anchored word owner adds
\(\{\alpha d(q,q')^2+\beta[V(q)+V(q')]/(2\alpha)\}I_E\).
The incidence owner instead adds its actual block diagonal free and weak-cell precision.

Under the internal vertex action \(U_1\mapsto U_1h^{-1}\), \(U_2\mapsto hU_2\), one has \(\eta\mapsto L_h\eta\), with \(\xi,\zeta\) unchanged. If \(D=\operatorname{diag}(I,L_h,I)\), transport \(j\mapsto Dj\) and \(T\mapsto DTD^\dagger\). Both effective sources in (PT9) stay fixed. Arbitrary additional marks on an intermediate readout can yield configuration-dependent effective sources; they need not equal an old constant source. Their complete amplitude is nevertheless given by (PT10) and the declared internal Haar integration. Equality to a specified old marked experiment requires transporting that experiment's source maps, not inventing new fixed marks.

## The physical transfer and its normalization are unchanged

Let \(X_c\) be a finite product of coarse \(SU(2)\) links, \(X_f\) its pure subdivisions, and \(\pi:X_f\to X_c\) the ordered products. Product Haar pushes forward to coarse Haar. The new internal vertex action has exactly the fixed-product fibers as its orbits, with normalized Haar conditional measure. Hence
\[
J:L^2(X_c)\longrightarrow L^2(X_f)^{\mathcal G_{\rm internal}},
\qquad J\psi=\psi\circ\pi
\tag{PT11}
\]
is unitary onto the entire internal-Gauss-invariant carrier. Old endpoint gauge actions intertwine as well.

Take the coarse unmarked kernel from [[anchored-word-cost-and-the-interacting-return|the anchored word return]] or the local incidence owner. Evaluate every old word on \(\pi\mathbf U\), retain every old preparation and measure, and define
\[
K_f(\mathbf U,\mathbf V)=K_c(\pi\mathbf U,\pi\mathbf V).
\qquad
\boxed{T_f=JT_cJ^\dagger.}
\tag{PT12}
\]
Here the integral operators use the original raw kernel; the identity on the full fine cover uses \(J^\dagger\) as fiber averaging. Direct integration over normalized Haar fibers proves it. The source-free row integral pulls back without alteration. In particular, the original constant normalization \(z_\alpha\), or \(Z_\alpha\) for many incidences, is exactly the same, not multiplied by newly assigned free-link factors.

For \(n\ge1\), normalized transfers therefore satisfy
\[
F_f^n=JF_c^nJ^\dagger,\qquad
F_fJ=JF_c,\qquad
\operatorname{Tr}(F_f^n)=\operatorname{Tr}(F_c^n)
\quad\text{when trace class}.
\tag{PT13}
\]
The first and third identities hold on the full cover, with zero on the orthogonal fiber sector. Consequently \(F_f\) is not injective on that redundant cover. On the complete physical internal-Gauss carrier it is unitarily identical to \(F_c\), retaining injectivity when the coarse transfer has it. This removes only the redundant bivalent presentation directions, not a newly created physical loop.

The weak cost is also transported before taking any limit: \(V_f=V_c\circ\pi\), with the same old \(S_e\) in every transported incidence and the same endpoint factors. Closed amplitudes keep the old \(z_\alpha^{-n}\) or \(Z_\alpha^{-n}\). Genuinely transported coarse marks preserve (PT12)–(PT13); arbitrary new stage marks use (PT9)–(PT10), followed by fiber integration, rather than an unmarked operator identity. Sources never authorize resetting a source-free normalization.

Thus this subdivision law preserves the full interacting operator already returned by the coarse preparation; it does not claim that products of freshly normalized determinant kernels close at finite width. Adding a genuine adjacent cell changes the physical carrier and can require new preparations, while retaining the variable on a shared old incidence, as in the local incidence construction. The remaining selection problem is to determine that whole preparation inventory and its transport from the declared algebra and marked diagram. Pure subdivision coherence alone does not answer it.

[[general-causal-action/calibrated-presentation-holonomy-and-spectral-return|Complete presentation calibration]] supplies a further test of this preservation: on the finite prepared physical carrier, a closed unitary transport fixing every source and one actual heat step is a scalar phase. Equality of spectra alone is weaker; the conclusion requires the complete source-and-clock experiment.

## Accessing an old subdivision vertex creates a new comparison obligation

There is an exact obstruction to treating these two operations independently. Start with an edge from \(v_0\) to \(v_2\), subdivided as \(U=U_1U_2\) through \(m\). Attach a new path \(W\) from \(v_0\) to \(m\). The path \(W\) may be represented by its framed product here. The enlarged graph has the genuine loop
\[
L=U_1W^{-1},\qquad
\psi(U_1,U_2,W)=\chi(L),
\tag{PT14}
\]
where \(\chi\) is any nontrivial irreducible \(SU(2)\) character. Under vertex gauges, \(U_1\mapsto h_0U_1h_m^{-1}\), \(U_2\mapsto h_mU_2h_2^{-1}\), and \(W\mapsto h_0Wh_m^{-1}\). Thus \(L\mapsto h_0Lh_0^{-1}\), and \(\psi\) is invariant under every vertex gauge. It has Haar mean zero and norm one. A previously redundant subdivision direction now changes a physical observable.

Take independent old and new rank-four Gaussian preparations for the two relative kernels (PT1), retaining the transported old product. The naive free extension is
\[
K_\alpha^0((U_1,U_2,W),(V_1,V_2,Z))
=K_{{\rm old},\alpha}(U_1U_2,V_1V_2)\,
K_{{\rm new},\alpha}(W,Z).
\tag{PT15}
\]
Divide by the exact free scalar \(z_{{\rm old},\alpha}z_{{\rm new},\alpha}\) to obtain \(F_\alpha^0\). This is a positive contraction with row integral one. At fixed \(A=V_1V_2\) and \(Z\), Haar integration over \(V_1\) gives
\(\int\chi(V_1Z^{-1})dV_1=0\). Consequently \(F_\alpha^0\psi=0\) for every \(\alpha>0\). Since \(\psi\) is already fully gauge invariant and the kernel commutes with the vertex action, Gauss restriction does not remove this obstruction.

Nor does a weak anchored potential repair the missing comparison. Write the joint old/new preparation as \(\xi\), with covariance \(\Gamma>0\), and its free comparison factor as \(e^{-\xi^\dagger B_\alpha(q,q')\xi}\), with \(B_\alpha\ge0\) and \(q=(U_1,U_2,W)\). Let the nonnegative gauge-covariant endpoint cost obey
\[
0\le C(q,\xi)\le M\|\xi\|^2,\qquad
f_{\alpha,q}(\xi)=e^{-C(q,\xi)/(2\alpha)}.
\tag{PT16}
\]
Here \(M\) is fixed, independently of \(\alpha\). This includes the actual loop cost
\(C=\beta[1-\tfrac12\operatorname{Tr}L](S_{\rm old}+S_{\rm new})\), with \(M=2\beta\), and bounded sums of norm-squared transported rows. Form \(K_\alpha\) by inserting these two endpoint factors into the same preparation integral as (PT15). Keep the same free scalar normalization, defining \(F_\alpha\). Conditional Gaussian distance positivity and the symmetric row bound make \(F_\alpha\) a positive contraction.

For a finite bound requiring no asymptotic expansion, the free Gaussian posterior at every fixed pair \(q,q'\) has covariance
\(Q^{-1}=(\Gamma^{-1}+B_\alpha)^{-1}\le\Gamma\).
The elementary inequality \(1-e^{-x}\le x\) gives
\[
0\le K_\alpha^0-K_\alpha
\le\frac{M}{\alpha}\mathbb E_\Gamma
\!\left[\|\xi\|^2e^{-\xi^\dagger B_\alpha\xi}\right]
\le\frac{M\operatorname{Tr}\Gamma}{\alpha}K_\alpha^0,
\qquad
\|F_\alpha-F_\alpha^0\|\le\frac{M\operatorname{Tr}\Gamma}{\alpha}.
\tag{PT17}
\]
The last step is the Schur bound with the exact free row integral. Thus for every integer \(n\ge1\),
\[
\boxed{\|F_\alpha^n\psi\|
\le\|F_\alpha\psi\|
\le\frac{M\operatorname{Tr}\Gamma}{\alpha},
\qquad
\|F_{n/t}^{\,n}\psi\|\longrightarrow0\quad(t>0).}
\tag{PT18}
\]
Any putative limit therefore annihilates this nonzero physical vector at every positive time. It cannot be a strongly continuous semigroup on the complete enlarged physical carrier, whose value at zero is the identity.

The failure concerns the inherited product comparison (PT15) with only weak endpoint additions. It does not invalidate the pure-subdivision theorem or the genuine-cell construction on an independently specified full link inventory. Attaching a path to a previously internal vertex makes that vertex accessible to a new physical distinction. The preparation must then be extended conditionally, or the leading comparison rows enlarged, so that the new distinction survives. Transporting the old preparation and adding a weak potential alone do not supply this extension.
