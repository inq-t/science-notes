# Many-Copy Exchange and the Weighted Diffusion

The determinant preparation's conditional link exchange has a definite many-copy return after the mean Fisher duration is applied: its response on every smooth pair of configuration sources converges to the Wilson-weighted gradient form, with coefficient one in the representation metric. The conditional posterior, its random center and its normalization all enter the proof. This identifies a configuration diffusion form selected by the declared exchange experiment. It does not identify that diffusion with physical time translation or prove convergence of the associated processes.

## The law, readout and duration remain fixed

Use the full-auxiliary link cut in [[auxiliary-copy-refinement-and-the-exchange-clock|AC1–5]] and the mean Fisher duration in [[determinant-response-sewing-and-relational-rigidity|DS10d]]. Fix a finite open hypercubic graph of dimension \(D\ge2\), with a plaquette, and set \(w=(2D)^{-1}\). Let \(G\) be a compact connected Lie group of positive dimension \(d\), with a faithful unitary representation \(\rho:G\to U(N)\). Equip its Lie algebra with
\[
Q_\rho(X,Y)=-\operatorname{Re}\operatorname{Tr}[d\rho(X)d\rho(Y)].
\tag{MD1}
\]
Faithfulness makes this an inner product; it is Ad-invariant. All Haar measures below have total mass one. The theorem applies to compact Abelian groups as well as compact simple groups.

The frame carrier is \(\mathcal X=G^E\). For each copy count \(\nu\), the joint law is exactly AC2, with
\[
Q_U=I-r_\nu P_U,
\qquad \xi^{(a)}\mid U\stackrel{\rm iid}{\sim}
\operatorname{CN}(0,C_U),\qquad C_U=Q_U^{-1}.
\]
Its frame marginal is \(\mu_\nu(dU)\propto(\det Q_U)^{-\nu}dU\). Choose the fixed-positive-Wilson-coupling path
\[
r_\nu\longrightarrow0,\qquad
b_\nu=2\nu r_\nu^4w^4\longrightarrow b\in(0,\infty),
\qquad q_\nu=2\nu r_\nu^2w^2.
\tag{MD2}
\]
Then \(q_\nu\to\infty\) and \(q_\nu r_\nu^2=b_\nu/w^2\). In particular \(r_\nu^2=O(q_\nu^{-1})\). The exact cycle expansion in [[cycle-determinants-and-the-pure-gauge-return|CY6–8]] gives
\[
\mu_\nu\longrightarrow\mu_{W,b}=Z_{W,b}^{-1}e^{-V_b}dU,
\qquad V_b(U)=b\sum_p[N-\operatorname{Re}\chi_\rho(U_p)],
\tag{MD3}
\]
in total variation, with uniform convergence of the normalized densities on this fixed graph.

At edge \(e=(x,y)\), retain \(\eta_e=(U_{e^c},\Xi)\). Let \(C_ef=\mathbb E[f(U)\mid\eta_e]\), \(T_{e,\nu}=C_e^*C_e\), and \(L_\nu=\sum_e(I-T_{e,\nu})\). The sum has one rate per raw link. The inner product is conjugate-linear in its first argument, so the exact response is
\[
\langle f,(I-T_{e,\nu})g\rangle_{\mu_\nu}
=\mathbb E_{\widehat\mu_\nu}
\operatorname{Cov}(f,g\mid\eta_e),
\quad
\operatorname{Cov}(f,g\mid\eta)
=\mathbb E[\overline f g\mid\eta]
-\overline{\mathbb E[f\mid\eta]}\mathbb E[g\mid\eta].
\tag{MD4}
\]
Each step samples a fresh complete preparation conditional on its incoming configuration. Copies are independent conditional on that configuration. Permanently retaining the same copies across steps would change the experiment.

For a \(Q_\rho\)-orthonormal basis \(X_1,\ldots,X_d\), define the left-edge directions explicitly by
\[
\mathsf X_{e,A}f(U)
=\left.\frac{d}{dt}\right|_{t=0}
f(U_{e^c},e^{tX_A}U_e),
\qquad
\langle\nabla_e f,\nabla_e g\rangle_{Q_\rho}
=\sum_A\overline{\mathsf X_{e,A}f}\,\mathsf X_{e,A}g.
\tag{MD5}
\]
The selected mean Fisher acceleration satisfies
\[
a_\nu=\frac1{d|E|}\sum_e
\mathbb E_{\mu_\nu}\operatorname{tr}_{Q_\rho}\mathcal I_e(U)
=q_\nu[1+O(r_\nu^2)]
\tag{MD6}
\]
by AC18–19. It is this specified acceleration, rather than an independently chosen mobility, that is tested below.

## The actual posterior has a concentrated random parameter

Put
\[
J_e=\sum_{a=1}^{\nu}\xi_y^{(a)}\xi_x^{(a)\dagger},
\qquad Z_e=\frac{J_e}{\nu r_\nu w}.
\]
The exact outgoing density from AC5 is
\[
p_e(V\mid\eta_e)
=\frac{\exp[q_\nu\operatorname{Re}\operatorname{Tr}(\rho(V)Z_e)]}
{\displaystyle\int_G
\exp[q_\nu\operatorname{Re}\operatorname{Tr}(\rho(W)Z_e)]\,dW}.
\tag{MD7}
\]
This denominator is the original conditional group integral. It is neither the Gaussian determinant normalizer nor a quantity recomputed after inserting a source.

Write \(V=hU_e\), where \(U_e\) is the incoming link, and set
\[
B_e=\rho(U_e)Z_e,\qquad
\phi_B(h)=\operatorname{Re}\operatorname{Tr}(\rho(h)B),
\qquad z(q,B)=\int_Ge^{q\phi_B(h)}dh.
\tag{MD8}
\]
Then the posterior in relative coordinates is exactly
\(z(q_\nu,B_e)^{-1}e^{q_\nu\phi_{B_e}(h)}dh\). The order of the matrices follows from \(V=hU_e\); it fixes the tangent convention in MD5.

For every fixed positive integer \(m\), there is a constant independent of \(U,\nu\) along MD2 such that
\[
\boxed{
\mathbb E[\|B_e-I\|_{\rm HS}^{2m}\mid U]
\le C_m\left[(\nu r_\nu^2)^{-m}+r_\nu^{4m}\right]
\le C_m' q_\nu^{-m}.}
\tag{MD9}
\]
To prove this, the bipartite Neumann expansion gives
\((C_U)_{yx}=r_\nu w\rho(U_e)^\dagger+O(r_\nu^3)\), uniformly in \(U\). Thus the conditional mean of \(B_e\) is \(I+O(r_\nu^2)\). For the fluctuations, center the independent matrix samples
\(\xi_y^{(a)}\xi_x^{(a)\dagger}\). Every fixed moment of a centered entry is uniformly bounded, because \(\|C_U\|\le(1-r_\nu)^{-1}\) and eventually \(r_\nu\le r_0<1\). Expand the \(2m\)-th moment of each real and imaginary sample sum. A term with an index appearing once vanishes by centering and independence. At most \(m\) distinct indices therefore survive, giving a bound \(C_m\nu^m\) before division by \(\nu^{2m}\). Finite matrix dimension and division by \((r_\nu w)^{2m}\) give the fluctuation term in MD9. The deterministic bias gives its other term.

For any fixed \(\delta>0\), the fourth-moment case implies the stronger tail control needed for a scaled response:
\[
\sup_U q_\nu\,
\mathbb P(\|B_e-I\|_{\rm HS}>\delta\mid U)
\le C\delta^{-4}q_\nu^{-1}\longrightarrow0.
\tag{MD10}
\]
Convergence of the parameter in probability alone would not justify multiplying a bounded posterior covariance by the diverging clock.

## A uniform posterior normalization and covariance lemma

There is a \(\delta>0\) for which every matrix \(B\) in the closed Hilbert–Schmidt ball \(\mathcal B_\delta=\{\|B-I\|\le\delta\}\) has a unique maximizer \(h_B\) of \(\phi_B\). It depends smoothly on \(B\), and \(h_I=e\). In exponential coordinates \(h=\exp(X)h_B\), define its negative Hessian
\[
A_B(X,Y)=
-\left.\partial_s\partial_t\right|_{s=t=0}
\phi_B(\exp(sX+tY)h_B).
\tag{MD11}
\]
The matrices of \(A_B\) in the \(Q_\rho\)-orthonormal basis are uniformly positive definite, and \(A_I=I_d\).

Indeed, \(\operatorname{Re}\operatorname{Tr}\rho(h)\le N\), with equality only when \(\rho(h)=I\), hence only when \(h=e\). Its negative Hessian there is MD1. The implicit function theorem and strict concavity in a fixed small exponential chart give the unique nearby maximum and uniform Hessian bounds. Compactness separates the value at the identity from the maximum outside that chart. Reducing \(\delta\) preserves this separation and proves that the nearby maximum is the unique global maximum.

Let \(\operatorname{Vol}_{Q_\rho}(G)\) denote the Riemannian volume before Haar normalization. Uniformly for \(B\in\mathcal B_\delta\), the actual denominator in MD8 has asymptotic
\[
\boxed{
z(q,B)=
e^{q\phi_B(h_B)}
\frac{(2\pi)^{d/2}}{\operatorname{Vol}_{Q_\rho}(G)}
q^{-d/2}(\det A_B)^{-1/2}
\,[1+O(q^{-1/2})].}
\tag{MD12}
\]
In the same chart, the posterior variable \(Y=\sqrt q\,X\) converges to the real Gaussian \(N(0,A_B^{-1})\), uniformly over this compact parameter set, including moments of every fixed degree. The mass outside the chart is exponentially small, uniformly in \(B\).

For completeness, the estimates are uniform because a fixed chart contains all \(h_B\), and the phase expansion there is
\[
q[\phi_B(\exp(Y/\sqrt q)h_B)-\phi_B(h_B)]
=-\tfrac12Y^TA_BY+O(q^{-1/2}|Y|^3).
\]
In a sufficiently small fixed chart, the phase is also bounded above by \(-c|Y|^2\) relative to its maximum, with \(c>0\) uniform. The Haar density in these coordinates is smooth, has value \(\operatorname{Vol}_{Q_\rho}(G)^{-1}\) at zero, and is independent of the translated center. Taylor expansion under a common Gaussian majorant, followed by the exponentially small outer-tail bound, gives MD12 and the moment assertions. The integrated cubic remainder is \(O(q^{-1/2})\), including after multiplication by any fixed polynomial in \(Y\). This argument uses the exact group normalizer throughout.

For complex \(C^3\) functions \(F,G\) on \(G\), let \(\operatorname{Cov}_{q,B}\) denote covariance in this posterior. If the functions range over a bounded \(C^3\) family, then uniformly over that family and \(B\in\mathcal B_\delta\),
\[
\boxed{
q\operatorname{Cov}_{q,B}(F,G)
=\sum_{A,C}(A_B^{-1})_{AC}
\overline{(\mathsf X_AF)(h_B)}
(\mathsf X_CG)(h_B)+O(q^{-1/2}).}
\tag{MD13}
\]
Here \(\mathsf X_AF(h)=\partial_tF(e^{tX_A}h)|_0\). Expand
\(F(\exp(Y/\sqrt q)h_B)=F(h_B)+q^{-1/2}\sum_A Y_A\mathsf X_AF(h_B)+O(q^{-1}|Y|^2)\), and similarly for \(G\). The centered Gaussian moments give MD13; the uniform fourth moments bound the Taylor products. Centering matters: the random maximum is not set equal to the incoming link before computing the conditional covariance.

The same estimates give the uniform-integrability bound on the good parameter set
\[
q\,|\operatorname{Cov}_{q,B}(F,G)|
\le C\|F\|_{C^1}\|G\|_{C^1}.
\tag{MD14}
\]
One can see this directly from Cauchy–Schwarz and
\(q\mathbb E|F(h)-F(h_B)|^2\le C\|F\|_{C^1}^2\), using the local second moment and exponentially small complement.

## The complete smooth-source response converges

**Finite-graph form theorem.** For every complex \(f,g\in C^3(\mathcal X)\), and each raw link \(e\),
\[
\boxed{
a_\nu\langle f,(I-T_{e,\nu})g\rangle_{\mu_\nu}
\longrightarrow
\int_{\mathcal X}
\langle\nabla_e f,\nabla_e g\rangle_{Q_\rho}\,d\mu_{W,b}.}
\tag{MD15}
\]
The conclusion is uniform when \(f,g\) range over bounded \(C^3\) families. It consequently includes complete smooth neutral multiplication sources and their mixed responses; it is not restricted to the plaquette estimator used in AC.

To prove it, condition first on the incoming \(U\). In MD13 use
\[
F_U(h)=f(U_{e^c},hU_e),\qquad
G_U(h)=g(U_{e^c},hU_e).
\]
These functions form a bounded \(C^3\) family because \(\mathcal X\) is compact. On \(\|B_e-I\|\le\delta\), MD13 applies. Its main term is a bounded continuous function of \((U,B_e)\). At \(B_e=I\), it is exactly \(\langle\nabla_e f,\nabla_e g\rangle_{Q_\rho}(U)\). Equation MD9 and uniform continuity therefore make its conditional average converge uniformly in \(U\) to that expression. For bounded \(C^3\) source families the required continuity estimates are uniform as well.

On the complement, use
\(|\operatorname{Cov}_{q,B}(F_U,G_U)|\le4\|f\|_\infty\|g\|_\infty\). Equation MD10 makes its contribution after multiplication by \(q_\nu\) tend to zero uniformly in \(U\). This is the missing-tail estimate that a purely pointwise Laplace expansion would not supply. Combining the two regions with MD4 yields
\[
q_\nu\langle f,(I-T_{e,\nu})g\rangle_{\mu_\nu}
-\int\langle\nabla_e f,\nabla_e g\rangle_{Q_\rho}\,d\mu_\nu
\longrightarrow0.
\tag{MD16}
\]
Finally use MD3 for the bounded gradient product and MD6 for \(a_\nu/q_\nu\to1\). This proves MD15. No posterior drift approximation, fitted potential or unproved diffusion limit enters the proof.

Equivalently, in the exact stationary experiment with \(U,U'\) independent conditional on \(\eta_e\),
\[
\tfrac12a_\nu\,
\mathbb E\!\left[(\overline{f(U')}-\overline{f(U)})
(g(U')-g(U))\right]
\longrightarrow
\int\langle\nabla_e f,\nabla_e g\rangle_{Q_\rho}\,d\mu_{W,b}.
\tag{MD17}
\]
The factor \(1/2\) is canceled by the two independent posterior boundary draws. The unit coefficient in MD15 is consistent with posterior covariance \(q_\nu^{-1}Q_\rho^{-1}\); it is not an extra factor of two from a real instead of complex preparation.

## The identified closed form is a weighted configuration diffusion

Summing MD15 over this finite edge inventory identifies the limiting smooth form
\[
\mathcal E_{W,b}(f,g)
=\sum_e\int
\langle\nabla_e f,\nabla_e g\rangle_{Q_\rho}\,d\mu_{W,b},
\qquad
a_\nu\langle f,L_\nu g\rangle_{\mu_\nu}
\longrightarrow\mathcal E_{W,b}(f,g).
\tag{MD18}
\]
For the normalized neutral plaquette source \(f_\nu\) of AC15, the same theorem gives
\(a_\nu\langle f_\nu,L_\nu f_\nu\rangle\to\mathcal E_{W,b}(F,F)/\operatorname{Var}_{\mu_{W,b}}F>0\). Both numerator and denominator are positive because \(F\) is nonconstant on the connected configuration space and the Wilson density is strictly positive. Thus this specific response has a nonzero limit in the proposed information units, strengthening AC's necessary pace bound without asserting a uniform gap.

On the compact manifold \(\mathcal X\), the smooth positive density \(m_b=d\mu_{W,b}/dU\) is bounded above and below. Hence this form has its usual closed extension with domain \(H^1(\mathcal X)\), in \(L^2(\mu_{W,b})\). Its nonnegative self-adjoint generator has the smooth-core expression
\[
\boxed{
\mathcal L_{W,b}
=\sum_{e,A}\left[-\mathsf X_{e,A}^{\,2}
+(\mathsf X_{e,A}V_b)\mathsf X_{e,A}\right]
=-m_b^{-1}\operatorname{div}(m_b\nabla).}
\tag{MD19}
\]
Haar integration by parts proves the expression and sign: each \(\mathsf X_{e,A}\) is divergence-free for Haar, while \(\mathsf X_{e,A}\log(d\mu_{W,b}/dU)=-\mathsf X_{e,A}V_b\). The corresponding Markov semigroup is \(e^{-t\mathcal L_{W,b}}\). Connectedness gives its constant zero-mode space. This construction and the ground-transform identity below are the standard weighted-form operations used in [[interacting-comparison-refinement|interacting comparison refinement]]; here the form's state and coefficient have been returned by MD15 rather than supplied independently.

The product gauge action preserves MD18, so the gauge-invariant subspace reduces the closed form and its generator. This gives its full neutral restriction without choosing coordinates on the possibly singular gauge quotient.

For comparison on Haar space, the unitary ground transform multiplies by
\(\psi_{W,b}=Z_{W,b}^{-1/2}e^{-V_b/2}\). If \(\Delta=\sum_{e,A}\mathsf X_{e,A}^2\), then
\[
\boxed{
\psi_{W,b}\mathcal L_{W,b}\psi_{W,b}^{-1}
=-\Delta+\tfrac14|\nabla V_b|^2-\tfrac12\Delta V_b.}
\tag{MD20}
\]
The source multiplication algebra is unchanged by this transform. Its constant zero mode becomes \(\psi_{W,b}\). The returned potential has both a squared-gradient term and a second-derivative term; a separately chosen linear Wilson magnetic potential is not the result of this calculation.

Equations MD15–18 prove convergence on every smooth pair, with the varying reference measures explicitly accounted for. They identify the canonical closed form associated with that limit. They do **not** prove Mosco convergence of the closed forms, strong-resolvent convergence, semigroup convergence or convergence of path laws. Those stronger claims require an additional lower-bound or compactness argument and are not consequences of smooth-core convergence alone. The result is also at fixed finite graph and fixed finite Wilson coupling, without uniform estimates in graph volume or lattice spacing.

The declared law and Fisher duration therefore pass a definite nonzero-response test and select a weighted configuration diffusion. The frame law in MD3 remains a probability on an entire finite Euclidean configuration. Calling the returned diffusion physical Yang–Mills time would require a separate identification of carrier and time-slice transfer; the two-boundary exchange construction alone supplies neither. The distinction is the one tested by [[sewn-transfer-clock-and-the-rotor-limit|the sewn transfer clock]].
