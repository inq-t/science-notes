# Heat-Factor Response and the Compression Defect

Two independent heat paths give one heat-path readout while retaining source information that the readout forgets. Fisher dualization on the retained source produces a convex combination of the two handed response forms. Its invariant-cylinder closure defines a complete output clock compatible with neutral annular restart and with charged gluing across ordered path cuts. The latter keeps an endpoint-dependent frame correction rather than separately neutralizing the pieces. However, the original product Ornstein--Uhlenbeck clock does not descend through this readout: an explicit source-chaos component varies along a fiber on which every output observable is constant. Reconstructing an output clock from a restricted response is therefore genuinely different from compressing the source evolution.

**Status: [EXACT] for the specified heat factors, entropy and score decomposition, closed output response and non-attained threshold, neutral-annular restart, coherent charged gluing across finite ordered path cuts, and source-clock non-descent; [OPEN] for equality with the maximal restricted source form, selection of the source model, general spatial-graph clock gluing, and a four-dimensional physical realization.**

## Two sources, one complete path readout

Let \(G\) be compact and connected with nonabelian simple Lie algebra, fix a bi-invariant metric \(Q\), and let \(T_a\) be a \(Q\)-orthonormal basis. Fix \(0<T<\infty\), \(0<\alpha<1\), and \(\beta=1-\alpha\). For independent standard Lie-algebra Brownian motions \(B^U,B^V\), develop
\[
dU_s=\sqrt{2\alpha}\,U_s\circ dB^U_s,
\qquad
dV_s=\sqrt{2\beta}\,V_s\circ dB^V_s,
\qquad U_0=V_0=e.
\tag{HF1}
\]
The source is the product path space with law
\(\nu_{\alpha,\beta}=\mu_{\alpha,T}\otimes\mu_{\beta,T}\).
Its readout is the entire continuous path
\[
\pi(U,V)_s=X_s:=U_sV_s^{-1},
\qquad
\pi_*\nu_{\alpha,\beta}=\mu_T,
\qquad
(JF)(U,V)=F(\pi(U,V)).
\tag{HF2}
\]
Here \(\mu_T\) is the unit-speed heat law of
[[shared-driver-response-and-the-nested-holonomy-clock|the nested-holonomy construction]], and \(J:L^2(\mu_T)\to L^2(\nu_{\alpha,\beta})\) is an isometry. The claim is a path-law identity, not only equality of endpoint heat kernels.

To verify it, introduce the standard right stochastic logarithms
\[
dC^U_s=(2\alpha)^{-1/2}\circ dU_sU_s^{-1},
\qquad
dC^V_s=(2\beta)^{-1/2}\circ dV_sV_s^{-1}.
\]
They are independent Brownian motions. The adapted orthogonal rotation
\[
\begin{pmatrix}dC^X_s\\dD_s\end{pmatrix}
=
\begin{pmatrix}
\sqrt\alpha I&-\sqrt\beta\operatorname{Ad}_{X_s}\\
\sqrt\beta I&\sqrt\alpha\operatorname{Ad}_{X_s}
\end{pmatrix}
\begin{pmatrix}dC^U_s\\dC^V_s\end{pmatrix}
\tag{HF3}
\]
gives independent standard Brownian motions \(C^X,D\). These are Itô integrals; the group product rule gives
\(dX_s=\sqrt2\circ dC^X_sX_s\). Thus \(X\) has generator \(\Delta_Q\), and its full filtration is that of \(C^X\), modulo null sets. The other Brownian direction \(D\) is independent of the readout. This is an actual source/readout distinction.

Simultaneous conjugation of both source paths intertwines conjugation of \(X\). We use the complete neutral output carrier
\[
\mathcal H_{T,\mathrm{inv}}
=L^2(\mu_T)^{\operatorname{Ad}G}.
\tag{HF4}
\]
Neutrality here means one common conjugation of the entire path. It is not separate conjugation at every time or on both sides of every cut. The based source translations below have nondegenerate Fisher metric, so finite response under those translations alone does not force (HF4); the residual gauge symmetry and its invariant readout are specified separately.

## Actual entropy distinguishes source from output Fisher geometry

Declare deterministic absolutely continuous based paths \(k,l\), with square-integrable logarithmic velocities, acting on the source by
\[
(U,V)\longmapsto(kU,lV).
\]
The output transforms as \(X\mapsto kXl^{-1}\). Write
\(v_k=k^{-1}\dot k\), \(v_l=l^{-1}\dot l\), and
\(-\sum_a\operatorname{ad}(T_a)^2=c_AI\), with \(r(s)=e^{-c_As}\).
The scaled [[path-shift-fisher-geometry-before-gauge-projection|one-sided path-shift formula]] and independence give
\[
D(\nu_{k,l}\Vert\nu_{\alpha,\beta})
=\frac14\int_0^T
\left(\frac{|v_k|^2}{\alpha}+\frac{|v_l|^2}{\beta}\right)ds.
\tag{HF5}
\]
By contrast, [[two-sided-fisher-completion-and-the-neutral-carrier#The joint action has an actual state cost|the output entropy calculation]] gives
\[
D(\mu_{k,l}\Vert\mu_T)
=\frac14\int_0^T
\bigl(|v_k|^2+|v_l|^2-2r(s)Q(v_k,v_l)\bigr)ds.
\tag{HF6}
\]
Consequently the information discarded by this readout is exactly
\[
\begin{aligned}
D(\nu_{k,l}\Vert\nu_{\alpha,\beta})-D(\mu_{k,l}\Vert\mu_T)
=\frac14\int_0^T\left(
\frac\beta\alpha|v_k|^2+\frac\alpha\beta|v_l|^2
+2r(s)Q(v_k,v_l)\right)ds.
\end{aligned}
\tag{HF7}
\]
The velocity matrix has determinant \(1-r(s)^2>0\) for \(s>0\), so this difference is nonnegative. The relative-entropy chain rule identifies it with the mean conditional relative entropy of the source laws inside the fibers of \(\pi\), evaluated under the shifted output law. The translations themselves are invertible; the forgetting map is \(\pi\). Neither cost is automatically irreversible entropy production.

For infinitesimal based pairs \((h,j)\), the source Fisher metric is
\[
g_{\mathrm{src}}(h,j)
=\frac12\int_0^T
\left(\frac{|\dot h|^2}{\alpha}+\frac{|\dot j|^2}{\beta}\right)ds,
\tag{HF8}
\]
whereas the output metric has the block
\(\frac12\left(\begin{smallmatrix}I&-rI\\-rI&I\end{smallmatrix}\right)\).
These are second derivatives of entropy, with natural logarithms fixing the normalization.

The score loss can also be checked before averaging. The source score is
\[
S_{h,j}
=\frac1{\sqrt{2\alpha}}\int Q(\dot h,dC^U)
+\frac1{\sqrt{2\beta}}\int Q(\dot j,dC^V).
\]
Substituting (HF3) decomposes it as
\[
\begin{aligned}
S_{h,j}
={}&\frac1{\sqrt2}\int Q(\dot h-\operatorname{Ad}_X\dot j,dC^X)\\
&+\frac1{\sqrt2}\int Q\left(
\sqrt{\beta/\alpha}\,\dot h
+\sqrt{\alpha/\beta}\,\operatorname{Ad}_X\dot j,dD\right).
\end{aligned}
\tag{HF9}
\]
The first row is the conditional expectation of the score given the output; the second has zero conditional mean and is orthogonal to the first. Its expected Gram is the difference of the two Fisher metrics. Thus the diagonal source metric is not the result of simply deleting the output cross term. It belongs to a different, more informative experiment. [[trace-dirichlet-descent/conditional-score-shorting-and-observable-lifts|Conditional score shorting]] explains why this score projection must also be distinguished from pointwise observable differentiation.

## The output response has its own closed clock

For a smooth cylinder \(F=f(X_{t_1},\ldots,X_{t_m})\), use
\(L_af(x)=\partial_v f(e^{vT_a}x)|_0\) and
\(R_af(x)=\partial_v f(xe^{vT_a})|_0\), and set
\[
p_L(s)=\sum_{i:s\le t_i}\nabla_{L,i}f,
\qquad
p_R(s)=\sum_{i:s\le t_i}\nabla_{R,i}f.
\]
Its pointwise source-action derivative is
\(\int[Q(p_L,\dot h)-Q(p_R,\dot j)]ds\).
Dualizing (HF8) on that derivative gives
\[
\boxed{
\Gamma_\alpha(F)
=2\int_0^T\bigl(\alpha|p_L|^2+\beta|p_R|^2\bigr)ds,
\qquad
\mathcal E_\alpha^{\mathrm{cyl}}(F)
=\alpha\mathcal E_L(F)+\beta\mathcal E_R(F).
}
\tag{HF10}
\]
This is not the inverse of the output metric in (HF8). It retains the source metric through observable pullback.

There is an independent construction of exactly the same form. The normalized left stochastic logarithms
\(B^U=(2\alpha)^{-1/2}\int U^{-1}\circ dU\) and
\(B^V=(2\beta)^{-1/2}\int V^{-1}\circ dV\)
in (HF1) identify the source with a product Wiener space. Put
\[
\mathcal E_{\mathrm{src}}(A)
=\|D_{B^U}A\|_2^2+\|D_{B^V}A\|_2^2,
\qquad
N_{\mathrm{src}}=N_{B^U}+N_{B^V},
\qquad M_\tau=e^{-\tau N_{\mathrm{src}}}.
\tag{HF11}
\]
Each factor has unit OU rate; the heat speeds are already in its development map. The right logarithms used to compute entropy in (HF9) are not interchangeable with these left logarithms by a fixed linear Wiener rotation.

The shared-driver differentiation formula gives source responses with coefficients \(2\alpha\min(t_i,t_j)\) and \(2\beta\min(t_i,t_j)\). On \(JF\), left variation of \(U_i\) is left variation of \(X_i\), while left variation of \(V_i\) is inverse right variation of \(X_i\). Therefore
\[
\mathcal E_{\mathrm{src}}(JF)
=\mathcal E_\alpha^{\mathrm{cyl}}(F).
\tag{HF12}
\]
In particular the preform is closable: an output sequence converging to zero and Cauchy in response pulls back to such a sequence for a closed source gradient.

Define \(\mathcal E_\alpha\) to be the closure of (HF10) on the invariant smooth cylinders in (HF4). Those cylinders are dense, because finite evaluations generate the continuous-path sigma-algebra and compact-group averaging preserves smooth cylinders. The gradient chain rule, normal-contraction approximation and closure give a Dirichlet form. It therefore defines a conservative self-adjoint Markov clock
\[
H_\alpha\ge0,
\qquad P_\tau^\alpha=e^{-\tau H_\alpha},
\qquad H_\alpha\mathbf1=0.
\tag{HF13}
\]
The formula \(\alpha\mathcal E_L+\beta\mathcal E_R\) is a form identity on this closure, not an assertion about the domain of an algebraic sum of unbounded generators.

There is also a closed maximal source restriction with domain
\[
D_{\max}^{\mathrm{src}}
=\{F\in\mathcal H_{T,\mathrm{inv}}:JF\in D(\mathcal E_{\mathrm{src}})\}.
\tag{HF14}
\]
Its density follows from the cylinders it contains; its closedness follows from the closed source form and the closed range of \(J\). The Markov property follows by composing the same pointwise normal contraction with \(J\). Our cylinder closure is a restriction of (HF14). Equality is not asserted: it requires a core theorem in the source graph norm. Likewise, equality with the maximal intersection of the two one-handed form domains is not needed below. [[trace-dirichlet-descent/standard-form-pullback-and-reducing-wall#Exact pullback theorem|The standard-form pullback theorem]] owns this distinction at greater generality.

The immediate analytic target is [[trace-dirichlet-descent/standard-form-pullback-and-reducing-wall#A conditional approximation criterion for the missing core|grid-uniform Sobolev stability of conditional readout]]. Let \(C_n\) condition the source on successively finer finite output grids generating the complete path. Fixed-grid conditioning sends smooth source holonomy cylinders to smooth output cylinders by compact heat-kernel integration. An estimate
\(\mathcal E_{\mathrm{src}}(C_nA)\le a\mathcal E_{\mathrm{src}}(A)+b\|A\|_2^2\),
with finite constants independent of the grid and valid on a source core, would identify the minimal and maximal returned forms by that criterion. This is bounded stability, not the stronger energy contraction that would incorrectly demand source-clock descent. The grid-uniform estimate is not proved here.

Both one-handed invariant forms have lower threshold two. Their closed gradients and bounds extend (HF10) from the cylinder core, so
\[
\mathcal E_\alpha(F)\ge2\|F-\mathbb EF\|_2^2.
\]
For the adjoint character \(f\), the rigorous small-time expansions in
[[two-sided-fisher-completion-and-the-neutral-carrier#The complete threshold is two, but two is not an eigenvalue|the heat-character calculation]] give
\(\operatorname{Var}f(X_t)=2dc_A^2t^2+O(t^3)\) and
\(\mathbb E|\nabla f(X_t)|^2=2dc_A^2t+O(t^2)\).
Both rows agree on this central one-time readout, so its energy is
\(2t\mathbb E|\nabla f(X_t)|^2\). Hence
\[
\boxed{
\ker H_\alpha=\mathbb C\mathbf1,
\qquad
\inf\operatorname{spec}(H_\alpha|_{\mathbf1^\perp})=2.
}
\tag{HF15}
\]
The same kernel and threshold hold for the generator \(H_{\alpha,\max}\) of (HF14). Indeed \(JF\) is invariant under common conjugation of the source, whose first Wiener chaos has no fixed vectors because \(\mathfrak g^{\operatorname{Ad}G}=0\). The unit product-OU form therefore has lower bound two on every centered vector of this maximal domain. The same character trials give the upper bound. This does not identify the two domains or operators.

These are auxiliary response thresholds on the full specified carrier, not physical masses. The fiber argument below proves that neither threshold is attained; this is not inherited from the one-handed clocks.

## Neutral annular observations keep their complete clock

For \(s+t\le T\), define the increment-path isometry
\[
(I_{s,t}F)(X)
=F\bigl((X_s^{-1}X_{s+u})_{0\le u\le t}\bigr),
\qquad
I_{s,t}:\mathcal H_{t,\mathrm{inv}}\to\mathcal H_{T,\mathrm{inv}}.
\tag{HF16}
\]
It preserves both the state norm and the complete clock:
\[
\boxed{
P_\tau^{\alpha,T}I_{s,t}
=I_{s,t}P_\tau^{\alpha,t}
\qquad(\tau\ge0).
}
\tag{HF17}
\]
This is stronger than a single character-energy check.

**Proof.** In the left logarithm \(B\) of the output, the increment path
\(Z_u=X_s^{-1}X_{s+u}\) develops solely from
\(B_{s+u}-B_s\). In the right logarithm \(C\), the path
\(Y_u=X_{s+u}X_s^{-1}\) develops solely from
\(C_{s+u}-C_s\). Since \(Z_u=X_s^{-1}Y_uX_s\), neutrality gives
\(F(Z)=F(Y)\). Thus the same annular subspace is, in each Wiener realization, the invariant functions of the driver on one time interval. Conditional expectation over the other Gaussian directions and conjugation averaging commute with unit OU. Its orthogonal projection therefore reduces both one-handed clocks.

That projection also maps invariant smooth holonomy cylinders to invariant smooth annular cylinders. Integrate the finitely many past holonomies and the independent later heat increments; the remaining arguments are the finitely many annular holonomies, with endpoints inserted if necessary. Smoothness follows by differentiating smooth functions on compact powers of \(G\) under these finite probability integrals. Consequently the projection contracts each form norm on the common cylinder core and extends to their mixed cylinder closure. Its mixed cross form with the complementary subspace is zero. On the annular range, (HF10) becomes the same formula with the interval restarted at zero. Closing these core identities proves (HF17). \(\square\)

The same argument gives complete clock compatibility under increasing the terminal horizon and retaining a prefix. The parameter \(\alpha\) and the unit response duration \(\tau\) are held fixed across these comparisons.

For \(SU(2)\), the character \(z_{s,t}=\chi_{1/2}(X_s^{-1}X_{s+t})\) therefore has
\[
\mathcal E_\alpha(z_{s,t})=2tJ(t),
\qquad J(t)=\tfrac34(1-e^{-2t}),
\tag{HF18}
\]
independently of \(s\) and \(\alpha\). This differs from the root-dependent joint-output Fisher response. More importantly, (HF17) does not demand that every globally neutral observable belong to this separately neutral annular subspace. For example
\(\chi_{1/2}(X_{s+t})=\chi_{1/2}(X_sZ_t)\) remains an ordinary finite-energy cylinder of the full carrier. This avoids
[[two-sided-fisher-completion-and-the-neutral-carrier#Conditional restart changes both operator and carrier|the loss caused by neutralizing a frozen future fiber]]. The full-cut law explains how its charged factors are retained.

## Full ordered cuts retain the boundary charge

Take a cut at \(s\) of a path of duration \(s+t\). Keep the entire prefix \(A=X|_{[0,s]}\) and the left increment path \(Y_u=A_s^{-1}X_{s+u}\). These have independent heat laws, so concatenation gives a unitary
\[
\mathsf U_{s,t}:L^2(\mu_s)\widehat\otimes L^2(\mu_t)
\longrightarrow L^2(\mu_{s+t}),
\qquad
(\mathsf U_{s,t}f)(X)=f(A,Y).
\tag{HF18a}
\]
The inverse path is \(X_r=A_r\) before the cut and \(X_{s+u}=A_sY_u\) afterwards. This is a bijection of continuous based paths and of their smooth finite-holonomy cylinder algebras, after inserting the cut endpoint when necessary.

The right stochastic logarithm instead sees the independent increment
\(W_u=X_{s+u}A_s^{-1}=\operatorname{Ad}_{A_s}Y_u\).
The change between these two product presentations is the unitary
\[
(\mathsf T_s f)(A,W)
=f\bigl(A,\operatorname{Ad}_{A_s}^{-1}W\bigr).
\tag{HF18b}
\]
For every fixed prefix endpoint, conjugation preserves the future heat law. Conditional integration therefore proves unitarity, without pretending that the frame change is independent of the prefix.

Write \(\mathcal L_{s,t}\) and \(\mathcal R_{s,t}\) for the closed tensor-form sums of the two regional left and right OU forms, respectively. Independent left driver increments give
\(\mathcal E_L^{s+t}(\mathsf U_{s,t}f)=\mathcal L_{s,t}(f)\);
independent right driver increments give
\(\mathcal E_R^{s+t}(\mathsf U_{s,t}f)=\mathcal R_{s,t}(\mathsf T_s f)\).
Consequently the exact cut response is
\[
\boxed{
\mathcal E_{\alpha,\mathrm{cut}}^{\mathrm{cyl}}(f)
=\alpha\mathcal L_{s,t}(f)
+\beta\mathcal R_{s,t}(\mathsf T_s f)
=\mathcal E_\alpha^{\mathrm{cyl}}(\mathsf U_{s,t}f).
}
\tag{HF18c}
\]
The retained data are the two handed response rows and the endpoint frame. The already summed regional generators alone are not the specified input to (HF18c).

Both \(\mathsf U_{s,t}\) and \(\mathsf T_s\) intertwine simultaneous conjugation. Therefore the full neutral carrier is
\((L^2(\mu_s)\widehat\otimes L^2(\mu_t))^{\operatorname{Ad}G}\),
not the tensor product of separately neutral regional carriers. It retains [[inq#The whole is assembled from dual boundary charges|the complete pairing of contrary boundary representations]]. Close (HF18c) on the jointly invariant smooth cut cylinders. The cylinder bijection in (HF18a) is isometric for the displayed graph norms, so the closed cut domain maps exactly onto \(D(\mathcal E_\alpha^{s+t})\). In particular, its full semigroup obeys
\[
P_\tau^{\alpha,s+t}\mathsf U_{s,t}
=\mathsf U_{s,t}P_\tau^{\alpha,\mathrm{cut}}
\qquad(\tau\ge0)
\tag{HF18d}
\]
on that complete diagonal-invariant carrier. Jointly smooth finite cut cylinders may equivalently be approximated by finite sums of smooth product cylinders in \(C^1\) on compact powers of \(G\); this controls both rows of (HF18c). No assertion about the maximal intersection of tensor-form domains or the maximal source restriction is used.

The frame correction can be read directly on a real cut cylinder
\(f(A_{r_1},\ldots,A_{r_m};Y_{u_1},\ldots,Y_{u_n})\).
Let \(p_{R,A}(r)\) and \(p_{R,Y}(u)\) be its respective cumulative right gradients, and define its future conjugation derivative by
\[
\mathcal C_Y f
=\sum_j(\nabla_{R,Y_j}-\nabla_{L,Y_j})f.
\]
Then the twisted right row in (HF18c) is
\[
\boxed{
\Gamma_{R,\mathrm{cut}}(f)
=2\int_0^s|p_{R,A}(r)+\mathcal C_Yf|^2dr
+2\int_0^t|p_{R,Y}(u)|^2du.
}
\tag{HF18e}
\]
Indeed a right variation of the prefix endpoint sends
\(Y_u\) to \(e^{-\varepsilon h(s)}Y_ue^{\varepsilon h(s)}\);
it therefore adds \(\mathcal C_Yf\) to every prefix tail. Right variation of the future in its own frame contributes the second integral. The left row is the ordinary tensor-left sum. The charge term vanishes for a separately neutral future function, recovering the simpler annular law, but need not vanish on a jointly neutral observable.

This distinction is detectable on [[path-shift-fisher-geometry-before-gauge-projection#The choice of handed action remains visible|the invariant three-holonomy determinant]]. At its stated rational SU(2) triple and times \(1,2,3\), cut at \(s=2\). The untwisted tensor-right response is \(67/625\); the endpoint correction restores the actual whole value \(481/625\), while the whole left value is \(193/625\). Thus replacing (HF18c) by the tensor sum of regional mixed clocks changes a concrete globally neutral response.

For three consecutive pieces \(A_1,A_2,A_3\), let \(a_i\) be their endpoints. Their natural right increments are
\[
W_1=A_1,\qquad
W_2=\operatorname{Ad}_{a_1}A_2,\qquad
W_3=\operatorname{Ad}_{a_1a_2}A_3.
\tag{HF18f}
\]
Cutting the first two pieces before attaching the third gives the last frame \(a_1a_2\). Cutting inside the future first gives
\(\operatorname{Ad}_{a_1}\operatorname{Ad}_{a_2}A_3\), the same expression. Group multiplication and its adjoint action therefore make the two parenthesizations coincide exactly, including their cylinder pullbacks and closed forms. The same cumulative-endpoint rule handles any finite number of ordered cuts. Retaining the boundary frames yields coherent gluing, not an intrinsic reassociation defect. This is an ordered path theorem; extension to independently intersecting spatial graph regions remains a different construction problem.

The full cut is an invertible change of path presentation. The two-source readout \(\pi(U,V)=UV^{-1}\) is a different, many-to-one map. Exact cut gluing therefore does not imply that the source OU clock descends through \(\pi\).

[[source-action-transport-through-ordered-cuts|The retained-source cut]]
now lifts this comparison to the actual paired paths and their
transformation family. It preserves interacting likelihoods and
responses when those actions are transported, but not when new
independent actions are assigned after cutting. Its
[[gauge-cycle-innovation-filtration/loop-coordinates-and-the-induced-clock#The ordered response is a reduced chain geometry|paired-edge-chain realization]]
also identifies the unweighted ordered rows with a complete finite
graph response. The ordering retains incidence information lost by
the bare loop state; this is not an intrinsic time-arrow theorem.

## An output character has a non-output source-chaos component

Now specialize to \(G=SU(2)\), \(Q=-2\operatorname{Tr}\),
\(T_a=-i\sigma_a/2\), and \(c=3/4\). Let
\(f_t(X)=\operatorname{Tr}X_t\), and let \(\Pi_2\) project onto total second Wiener chaos of the source pair \((B^U,B^V)\). Put
\[
Z=\sqrt\alpha B^U-\sqrt\beta B^V.
\]
This is standard three-dimensional Brownian motion. Ordered Itô expansion gives the exact projection
\[
\boxed{
\Pi_2Jf_t
=-\frac{e^{-ct}}2\bigl(|Z_t|^2-3t\bigr),
\qquad
\|\Pi_2Jf_t\|_2^2=\frac32t^2e^{-2ct}>0.
}
\tag{HF19}
\]
To check the coefficient, the Itô drifts of \(U\) and \(V^{-1}\) are
\(-\alpha cU\) and \(-\beta cV^{-1}\). Using
\(\operatorname{Tr}(T_aT_b)=-\delta_{ab}/2\), the two same-factor second-chaos terms are
\[
-\frac{\alpha e^{-ct}}2(|B^U_t|^2-3t),
\qquad
-\frac{\beta e^{-ct}}2(|B^V_t|^2-3t),
\]
and the product of the first-chaos terms is
\(\sqrt{\alpha\beta}e^{-ct}Q(B^U_t,B^V_t)\).
Their sum is (HF19). The ordered expansions converge in \(L^2\), and chaos orthogonality separates this term from higher orders; no truncation is asserted for the character itself.

For a deterministic based finite-energy path \(k\), the transformation
\[
\mathcal R_k(U,V)=(Uk,Vk)
\tag{HF20}
\]
fixes \(\pi(U,V)\) pointwise. It is quasi-invariant for the source law: in each left logarithm it is a deterministic orthogonal rotation followed by a finite-energy Cameron--Martin shift. Explicitly,
\[
dB^{U,k}=\operatorname{Ad}_{k^{-1}}dB^U
+\frac{k^{-1}\dot k}{\sqrt{2\alpha}}ds,
\qquad
dB^{V,k}=\operatorname{Ad}_{k^{-1}}dB^V
+\frac{k^{-1}\dot k}{\sqrt{2\beta}}ds.
\]
The drift terms cancel in the specified combination:
\[
Z_t^k=\int_0^t\operatorname{Ad}_{k_s}^{-1}\,dZ_s.
\tag{HF21}
\]
Every output-measurable source vector must be unchanged almost surely by (HF20). Quasi-invariance is important here: it transports any exceptional null set of a claimed representation \(A=F\circ\pi\).

But (HF19) is not unchanged. Set \(R_s=\operatorname{Ad}_{k_s}^{-1}\). The two jointly Gaussian vectors \(Z_t,Z_t^k\) each have covariance \(tI_3\). Gaussian fourth moments give
\[
\mathbb E\left(|Z_t^k|^2-|Z_t|^2\right)^2
=4\left(3t^2-\left\|\int_0^t R_s\,ds\right\|_F^2\right).
\tag{HF22}
\]
The expression is strictly positive whenever the orthogonal matrix path \(R_s\) is not almost everywhere constant. Indeed
\(\|t^{-1}\int R_sds\|_F^2\le t^{-1}\int\|R_s\|_F^2ds=3\),
with equality exactly for an almost surely constant matrix. For example \(k_s=\exp(\omega sT_3)\), \(\omega\ne0\), gives
\[
\left\|\int_0^t R_sds\right\|_F^2
=t^2+\frac{8\sin^2(\omega t/2)}{\omega^2}<3t^2.
\]
Thus \(\Pi_2Jf_t\) is not an output-measurable vector. This argument uses the exact source fiber and an actual observable, not an assumed comparison of two chaos labels.

Equation (HF22) is the variance for the unscaled squared-norm difference. For the actual chaos observable in (HF19), the variance of its change under (HF20) is
\[
e^{-2ct}\left(3t^2-\left\|\int_0^t R_sds\right\|_F^2\right).
\tag{HF22a}
\]
At \(t=0.7\), \(\omega=1.2\), these values are approximately
\(0.225142509348\) and \(0.0196964657376\), respectively. They are not lower bounds on a compression defect or on distance to the output subspace: (HF20) is quasi-invariant, not measure preserving. Its Cameron--Martin cost can diverge when \(\alpha\) or \(\beta\) approaches zero. The argument assumes both speeds positive; the degenerate one-factor endpoints genuinely escape it.

## The source semigroup does not descend

Let \(P=JJ^*\) be the orthogonal projection onto the complete output subspace; the following applies either before or after common-conjugation invariance. If even one \(M_\tau\), with \(\tau>0\), preserved that subspace, self-adjointness would make it reducing for this operator. The distinct eigenvalues \(e^{-n\tau}\) identify every chaos projection as a spectral projection of \(M_\tau\), so \(P\) would commute with \(\Pi_2\). Equation (HF22) contradicts this for the basic vector \(Jf_t\). Hence
\[
\boxed{
M_\tau\operatorname{Ran}J\nsubseteq\operatorname{Ran}J
\quad\text{for every }\tau>0.
}
\tag{HF23}
\]
This is non-invariance of the whole subspace at each positive duration. It does not assert that the same endpoint character witnesses non-invariance at every duration.

The [[trace-dirichlet-descent/standard-form-pullback-and-reducing-wall#The operations that must not be conflated|general compression defect]] now has a concrete nonzero realization. For
\(C_\tau=J^*M_\tau J\),
\[
C_{2\tau}-C_\tau^2
=J^*M_\tau(I-P)M_\tau J\ge0,
\tag{HF24}
\]
and (HF23) makes this operator nonzero at every \(\tau>0\). The compressed maps preserve the state and are Markov one duration at a time, but they do not form a semigroup. In particular they cannot be the clock \(P_\tau^\alpha\) of (HF13), or any other output semigroup at all durations. This conclusion does not require equality between the minimal and maximal restricted form domains, or a proof about attainment of the mixed output threshold.

## The threshold is not attained in either closed realization

The fiber geometry gives a stronger general statement than the one-character witness. Let \(\mathcal C_n^{\mathrm{src}}\) denote total Wiener chaos of degree \(n\) in the two normalized source drivers. For every compact connected \(G\) with semisimple Lie algebra,
\[
\boxed{
\operatorname{Ran}J\ \cap\!
\bigcup_{N<\infty}\bigoplus_{n=0}^{N}\mathcal C_n^{\mathrm{src}}
=\mathbb C\mathbf1.
}
\tag{HF25}
\]
This holds even for the full unprojected output carrier. No nonconstant finite source-chaos polynomial is determined by \(UV^{-1}\).

**Proof.** Use the Gaussian Hilbert space
\(\mathsf H=L^2([0,T];\mathfrak g\oplus\mathfrak g)\)
of \((B^U,B^V)\). Under (HF20), the white-noise coordinates undergo the affine transformation with orthogonal linear part
\[
(O_kh)(s)
=\bigl(\operatorname{Ad}_{k_s}^{-1}\oplus
\operatorname{Ad}_{k_s}^{-1}\bigr)h(s)
\]
and Cameron--Martin shift
\(a_k(s)=((2\alpha)^{-1/2}v_k(s),(2\beta)^{-1/2}v_k(s))\).
For a finite-chaos vector \(A=\sum_{n=0}^N I_n(K_n)\), with symmetric square-integrable kernels, the highest transformed component is exactly
\[
\Pi_N(A\circ\mathcal R_k)
=I_N\bigl((O_k^*)^{\otimes N}K_N\bigr).
\tag{HF26}
\]
Translation contributes only lower degrees, and no original lower-degree component contributes at degree \(N\). The identity follows first for finite-rank kernels by the Gaussian polynomial translation formula. It extends to square-integrable kernels by the Wiener isometry and the bounded contractions with the fixed \(a_k\); quasi-invariance identifies the resulting \(L^2\) limit with actual composition by \(\mathcal R_k\).

If \(A\) is output-measurable, it is unchanged by every fiber action, so its highest kernel is invariant under \((O_k^*)^{\otimes N}\). Take pairwise disjoint positive time intervals and choose a based absolutely continuous \(k\) that is constant \(g\) on one interval and the identity on the others. Such paths exist because \(G\) is connected. On the corresponding product of intervals, only one tensor leg is rotated. Invariance for every \(g\) forces that leg into
\((\mathfrak g\oplus\mathfrak g)^{\operatorname{Ad}G}=0\).
Use rational intervals and a countable dense set of group elements to obtain the identities on one common full-measure set. Their products cover all tuples of pairwise distinct times, while coincident-time diagonals have product measure zero. Therefore \(K_N=0\). Descending induction proves (HF25). \(\square\)

In particular \(\mathcal C_2^{\mathrm{src}}\cap\operatorname{Ran}J=\{0\}\). If a centered vector attained the bound two for either \(H_\alpha\) or \(H_{\alpha,\max}\), its pulled-back source form would attain the product-OU bound. Common conjugation removes first chaos, and equality in
\(\sum_{n\ge2}n\|\Pi_n JF\|^2\ge2\sum_{n\ge2}\|\Pi_n JF\|^2\)
forces \(JF\in\mathcal C_2^{\mathrm{src}}\). Equation (HF25) then forces \(F=0\). Thus
\[
\boxed{
2\text{ is a spectral threshold but not an eigenvalue of }
H_\alpha\text{ or }H_{\alpha,\max}.
}
\tag{HF27}
\]
This conclusion does not identify their domains. Nor does (HF25) eliminate smooth holonomy cylinders: such a cylinder generally has infinitely many source-chaos components. An arbitrary infinite expansion has no highest degree, so the induction does not apply. The explicit character in (HF19) illustrates precisely why taking one of its source-chaos components need not preserve its status as an output observable.

[[haar-vertex-source-and-joint-gauge-response|The Haar-vertex graph source]]
now extends the retained-factor prescription to an arbitrary finite
graph with one endpoint per edge. Cost-free vertex frames return
Gauss invariance, and the same edge source fixes both the
gauge-averaged heat state and the shared response. Its rebuilt
endpoint clocks respect ordinary edge subdivision and have a
uniform auxiliary lower bound; the source OU still does not descend.
This is not a general multitime spatial-net construction or a
Yang--Mills state identification.

## What the source construction selects

The source heat speeds remain a genuine input. The output state is independent of \(\alpha\), but [[path-shift-fisher-geometry-before-gauge-projection#The choice of handed action remains visible|the three-holonomy handedness witness]] proves \(\mathcal E_L\ne\mathcal E_R\) on invariant observables, so different \(\alpha\) give different mixed forms. Swapping \(U,V\) sends \(X\) to \(X^{-1}\) and \(\alpha\) to \(1-\alpha\). Requiring this exchange as a symmetry of one fixed response selects \(\alpha=1/2\) within this family; it is an additional source symmetry, not a consequence of the common output heat law.

What is gained is a source-complete response construction whose rebuilt output clock survives neutral annular restart and coherently glues full charged carriers across ordered path cuts. What is not gained is literal source-clock descent, general spatial-graph clock gluing, selection of the heat state or transformation family, or a four-dimensional local field theory. The heat-area index, OU response duration and a physical translation parameter remain distinct.

The existing [[receipts/two_sided_fisher_receipt.py|two-sided receipt]] checks actual SU(2) adjoint-frame score rotations, the source/output/discarded Fisher blocks, a finite path-shift entropy example, and the scalar annular response (HF18). Its source-fiber addition tests actual Pauli tensor moments, the adjoint-frame integral at three quadrature orders, and both variances (HF22)--(HF22a) by a 729-node Gaussian degree-four integral. Its charged-cut test checks the three-holonomy frame correction in (HF18e), including the failure of the untwisted tensor-right response. Its additional normalized triangle integral
\(2(c_AT-1+e^{-c_AT})/(c_AT)^2\)
is only a finite kernel-overlap check; it is not a proof that two complete chaos subspaces intersect trivially or that the mixed threshold is not attained. The [[receipts/two-sided-fisher-receipt-output.txt|stored output]] records the earlier score and scalar-annular checks, not the later source-fiber and charged-cut additions. The current receipt reports those additions. The source-chaos and fiber arguments (HF19)--(HF27), rather than the finite diagnostics, establish non-descent and non-attainment.
