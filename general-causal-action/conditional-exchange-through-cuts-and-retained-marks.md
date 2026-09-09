# Conditional Exchange Through Cuts and Retained Marks

Conditional boundary exchange has an exact one-step marginal, but its repeated marginal generally carries memory. Forgetting auxiliary information produces a different, explicitly positive one-step defect. These distinctions follow from one joint law and retain every admitted source. In the determinant preparation, the selected shared-link update has an exact \(SU(2)\) angular response, while a bounded preparation-norm mark detects when a forgotten holonomy cannot disappear from the subsequent experiment.

## The conditional law fixes both halves of an exchange

Use the joint law and cut prescription in [[determinant-response-sewing-and-relational-rigidity#Active candidate: conditional boundary exchange|DS10a–c]]. More generally let \(\widehat\mu\) be one probability law of the physical configuration \(U\) and an actual cut readout \(\eta\), including its retained outside and auxiliary data. Write
\[
\mathcal H=L^2(\mu_U),\qquad
\mathcal K=L^2(\mu_\eta),\qquad
Cf=\mathbb E[f(U)\mid\eta].
\]
Both marginals and every conditional below come from \(\widehat\mu\). The adjoint is
\[
C^*g=\mathbb E[g(\eta)\mid U],\qquad T=C^*C.
\tag{EC1}
\]
Thus a step draws \(\eta\) conditional on the incoming \(U\), then draws \(U'\) conditional on that same \(\eta\). Its stationary three-variable measure is
\[
d\mu_\eta(\eta)\,
\widehat\mu(dU\mid\eta)\,
\widehat\mu(dU'\mid\eta).
\tag{EC2}
\]
This is a two-boundary conditional experiment, not an independently chosen transition kernel.

For a bounded readout mark \(N(\eta)\), retain
\[
T_N=C^*M_NC,\qquad
\langle f,T_Ng\rangle
=\mathbb E\!\left[N(\eta)\overline{Cf(\eta)}\,Cg(\eta)\right],
\qquad T_N^*=T_{\overline N}.
\tag{EC3}
\]
Incoming and outgoing physical marks multiply \(f,g\). Finite linear combinations and the usual bounded monotone-class extension cover joint bounded marks on these retained variables. All source-free conditional normalizers stay fixed: inserting a mark is not recomputing the conditional law after tilting it. Any retained raw overall normalization travels with the same amplitude.

The source-free \(T\) is a positive self-adjoint Markov contraction, and
\[
\langle f,(I-T)f\rangle
=\mathbb E\left|f(U)-\mathbb E[f(U)\mid\eta]\right|^2.
\tag{EC4}
\]
For complex functions this is the conditional variance with the absolute square. Positivity assertions for arbitrary marked operators are not needed.

## Marginalizing a physical coordinate preserves one step exactly

Let \(X=\pi(U)\) be an actual retained physical readout. Its isometric pullback is \(Jf=f\circ\pi\), with \(\mathsf P=JJ^*\) the conditional expectation onto functions of \(X\). Set \(K=CJ\). Marginalize the original joint law to \((X,\eta)\), keeping the same readout marks. Its exchange is exactly
\[
\boxed{\overline T_N=K^*M_NK=J^*T_NJ.}
\tag{EC5}
\]
Indeed \(Kf=\mathbb E[f(X)\mid\eta]\), and its adjoint is conditional expectation from \(\eta\) to \(X\). Equation (EC5) identifies the entire stationary one-step marked measure, not just a covariance or a generator. It averages the incoming forgotten variables with their actual conditional law given \(X\).

It does not imply that the fine transition starting from every \(U\) depends only on \(X\). Define the leakage
\[
L_N=(I-\mathsf P)T_NJ.
\]
Two successive marked steps give the exact defect
\[
\boxed{
J^*T_{\overline N}T_NJ
-\overline T_{\overline N}\overline T_N
=L_N^*L_N\ge0.}
\tag{EC6}
\]
For different marks, the corresponding expression is \(L_{N_1}^*L_{N_2}\), with \(T_{\overline{N_1}}\) in the first fine step. Retained intermediate physical multiplication sources commute with \(\mathsf P\) and can be inserted in this identity; a nonnegative such source retains positivity when the two readout marks agree.

For the source-free process, autonomous inherited exchange is equivalent to \(L_1=0\). Exact autonomy through every retained marked temporal word is equivalent to \(L_N=0\) for every admitted readout mark. Sufficiency follows by multiplying the resulting intertwinings \(T_NJ=J\overline T_N\); necessity already follows from (EC6). The correct test therefore specifies which marks remain admitted.

There is a sharper criterion if **all** bounded marks of the full \(\eta\) remain retained:
\[
\boxed{
T_NJ=J\overline T_N\ \text{for all bounded }N(\eta)
\quad\Longleftrightarrow\quad
\widehat\mu(d\eta\mid U)=\widehat\mu(d\eta\mid X)
\ \text{almost surely}.}
\tag{EC7}
\]
Necessity follows by applying the intertwining to \(1\):
\(T_N1=\mathbb E[N(\eta)\mid U]\).
Bounded marks determine the conditional probability law. Conversely, if that law depends only on \(X\), then
\(\mathbb E[N(\eta)Kf(\eta)\mid U]\)
also depends only on \(X\), proving the intertwining. This is conditional sufficiency of the physical readout for the retained experiment. It is not a requirement that every proposed physical projection satisfy it.

## Removing auxiliary information changes the comparison

Now replace \(\eta\) by \(Y=q(\eta)\), while retaining \(X\). Let \(\iota:L^2(\mu_Y)\to\mathcal K\) be the isometric pullback and \(\mathsf Q=\iota\iota^*\). The exchange derived from the marginal law \((X,Y)\) is
\[
\overline T_Y=K^*\mathsf QK,
\qquad
\boxed{\overline T_\eta-\overline T_Y
=K^*(I-\mathsf Q)K\ge0.}
\tag{EC8}
\]
Its quadratic defect is
\[
\mathbb E\left|
\mathbb E[f(X)\mid\eta]-\mathbb E[f(X)\mid Y]
\right|^2.
\]
Equality for every \(f\) holds precisely when \(Y\) is conditionally sufficient for the retained physical readout: \(\mathbb E[f(X)\mid\eta]=\mathbb E[f(X)\mid Y]\). Agreement of the physical marginal alone does not establish this.

For a retained bounded mark \(N(Y)\), \(\mathsf Q\) commutes with multiplication by \(N\), and
\[
\boxed{
K^*M_NK-K^*\mathsf Q M_N\mathsf QK
=K^*(I-\mathsf Q)M_N(I-\mathsf Q)K.}
\tag{EC9}
\]
This is positive for \(N\ge0\), and is the marked conditional-covariance defect of the posterior readouts. A source on information actually removed from \(\eta\) cannot be preserved by simply renaming it a source on \(Y\).

Thus physical marginalization and auxiliary marginalization have different effects. The former gives the exact one-step compression (EC5), with possible temporal leakage. The latter discards part of the posterior information and changes that one-step exchange by (EC8). In comparison-clock language,
\(I-\overline T_Y=(I-\overline T_\eta)+K^*(I-\mathsf Q)K\).
No fitted normalization is involved in either identity.

## The retained temporal object includes its memory

For \(R=I-T\), decompose along \(\operatorname{ran}J\) and its orthogonal complement:
\[
A=J^*RJ,\qquad B=(I-\mathsf P)RJ=-L_1,\qquad
D=(I-\mathsf P)R(I-\mathsf P).
\]
On the hidden space \(D\ge0\). The exact resolvent is
\[
\boxed{
J^*(z+R)^{-1}J
=\left[z+A-B^*(z+D)^{-1}B\right]^{-1},
\qquad z>0.}
\tag{EC10}
\]
All operators are bounded at this finite comparison stage; \(z>0\) requires no assumed hidden gap. [[coarse-response-memory/inq|Coarse response memory]] owns the Schur proof and its time-domain interpretation. The same block formula applies to a finite sum of selected cut defects. The memory term and the marked leakage in (EC6) are consequences of the actual law. Discarding them is a new process prescription.

[[bridge-forgetting-and-the-inherited-marked-transfer|Bridge forgetting]] supplies a special positive control: its admitted retained marks do satisfy an exact intertwining when the unused conditional preparation is removed. Its every-width reset witness is a negative control against replacing an inherited composite by a freshly normalized comparison. Neither result licenses universal autonomy for the present determinant law.

## The determinant law selects a concrete shared-link exchange

Take \(Q_U=I-rP_U>0\) from DS3, with one variable on each raw link and \(\nu\) complex Gaussian copies. Conditional on the full frame configuration,
\[
\xi^{(a)}\mid U\sim\operatorname{CN}(0,Q_U^{-1}),
\qquad a=1,\ldots,\nu,
\tag{EC11}
\]
independently over copies. These are whole-graph covariances, not independently refreshed vertex priors. Fix an oriented raw edge \(e=(v,w)\), keep every other link in \(O\), and choose the actual cut readout \(\eta_e=(O,\Xi)\). Put
\[
J_e(\Xi)=\sum_{a=1}^{\nu}\xi_w^{(a)}(\xi_v^{(a)})^\dagger .
\]
The terms of the exponent containing \(U_e=h\) give exactly
\[
\boxed{
p_e(h\mid\Xi,O)
=\frac{\exp[2rw_e\operatorname{Re}\operatorname{Tr}(\rho(h)J_e)]}
{z_e(\Xi)},\quad
z_e(\Xi)=\int_G
e^{2rw_e\operatorname{Re}\operatorname{Tr}(\rho(g)J_e)}dg.}
\tag{EC12}
\]
The outside links enter through the inherited law (EC11). At this conditional stage the displayed edge density depends on their preparation record, not on a new comparison pace.

The selected marked update is therefore
\[
(T_e^Nf)(U)=
\int\widehat\mu(d\Xi\mid U)\,N(O,\Xi)
\int_Gp_e(h\mid\Xi,O)f(O,h)\,dh.
\tag{EC13}
\]
Both the Gaussian normalizer in (EC11) and \(z_e\) remain source free. Vertex gauge transformations carry \(J_e\), the preparations and the outside readout together; the joint law and this transition are covariant. Hence the selected update preserves the gauge-invariant physical subspace. Its action and its joint state are determined by this declared cut, without fitting a returned cell operator.

For two adjacent \(SU(2)\) cells, let \(p\) be their shared raw edge and let \(a,q\) be the ordered outer-path products held fixed by this update. Then
\[
x=ap^{-1},\qquad y=qp^{-1}.
\]
Use quaternion coordinates \(p=u_0I+i\sum_{i=1}^3u_i\sigma_i\), \(u\in S^3\), and the same convention for \(a,q\). Set
\[
t_A=2rw_e\operatorname{Re}\operatorname{Tr}(E_AJ_e),
\quad E_0=I,\ E_i=i\sigma_i,\quad
\varkappa=|t|,\quad
m(\varkappa)=\frac{I_2(\varkappa)}{I_1(\varkappa)}.
\]
Normalized Haar on \(S^3\) gives
\[
\boxed{
z_e=\frac{2I_1(\varkappa)}{\varkappa},\quad
\mathbb E[u\mid\Xi,O]=m(\varkappa)\widehat t,\quad
\mathbb E[uu^T\mid\Xi,O]
=\frac{m}{\varkappa}I_4+
\left(1-\frac{4m}{\varkappa}\right)\widehat t\,\widehat t^T.}
\tag{EC14}
\]
At \(\varkappa=0\), these are \(z_e=1\), mean zero and second moment \(I_4/4\). The character integral used in [[relative-multiplication-transfer-and-the-rotor-limit|the rotor multipliers]] gives \(z_e\); differentiating it once and twice gives the moments. In particular \(m'=1-m^2-3m/\varkappa\).

Since \(\operatorname{Tr}(ap^{-1})/2=a\cdot u\), the conditional product response is
\[
\boxed{
\mathbb E\!\left[
\frac{\operatorname{Tr}x}{2}\frac{\operatorname{Tr}y}{2}
\ \middle|\ \Xi,O\right]
=\frac{m}{\varkappa}(a\cdot q)
+\left(1-\frac{4m}{\varkappa}\right)
(a\cdot\widehat t)(q\cdot\widehat t).}
\tag{EC15}
\]
At zero \(t\) the answer is \((a\cdot q)/4\). Averaging this expression over the actual Gaussian law (EC11) gives \(T_e\) of the product source. The mixed angular channel is retained. The separate quantity
\(a\cdot q=\operatorname{Tr}(aq^{-1})/2=\operatorname{Tr}(xy^{-1})/2\)
is fixed by this one shared-link update, whereas the product source is nonconstant on the resampled \(S^3\) fiber. Because (EC12) has full support, the latter has strictly positive conditional variance. A single cut is therefore nontrivial on neutral observables but does not have a vacuum-only fixed space.

## A bounded retained mark detects a forgotten holonomy

Suppose the admitted readout keeps the whole preparation norm. For \(\varepsilon>0\), use the bounded gauge-invariant mark
\[
N_\varepsilon(\Xi)=
\exp\!\left[-\varepsilon\sum_a\|\xi^{(a)}\|^2\right].
\]
Gaussian integration with the original conditional normalization gives its exact outgoing marked row:
\[
\boxed{
F_\varepsilon(U):=T_{N_\varepsilon}1(U)
=\mathbb E[N_\varepsilon\mid U]
=\left[\frac{\det Q_U}{\det(Q_U+\varepsilon I)}\right]^\nu.}
\tag{EC16}
\]
This is a source insertion into the existing law, not a new conditional precision used to renormalize the process.

For a physical readout \(X=\pi(U)\), equations (EC6) and (EC16) give a fully neutral two-step witness:
\[
\boxed{
\left\langle1,
\left[J^*T_{N_\varepsilon}^{\,2}J
-(J^*T_{N_\varepsilon}J)^2\right]1
\right\rangle
=\mathbb E\operatorname{Var}(F_\varepsilon(U)\mid X).}
\tag{EC17}
\]
It is strictly positive whenever the retained preparation mark distinguishes configurations on a forgotten physical fiber.

The cycle expansion of DS4–5 checks that this can be an actual holonomy distinction. Let \(S_s(U)=\nu\log[\det(I-sP_U)/\det(I-sP_{\mathbf1})]\). Then
\[
\log\frac{F_\varepsilon(U)}{F_\varepsilon(\mathbf1)}
=S_r(U)-S_{r/(1+\varepsilon)}(U)
=\nu\sum_{n\ge1}\frac{r^n-[r/(1+\varepsilon)]^n}{n}
\left[\operatorname{Tr}P_{\mathbf1}^{\,n}
-\operatorname{Tr}P_U^{\,n}\right].
\tag{EC18}
\]
Every bracket is nonnegative by the closed-walk expansion. The difference is strict if a positive-weight cycle has a holonomy detected by the representation. In ordinary loop coordinates, forgetting such a cycle while retaining nearby old loop values therefore leaves a nonconstant \(F_\varepsilon\) on a positive-measure set of fibers. This tests a physical cycle, not a gauge change of presentation. If a cut retains fewer auxiliaries, the same test must instead use an actual retained mark; an unavailable whole norm cannot be silently inserted.

The admissible cut grammar is now constrained by explicit alternatives. It can retain the preparation information and the induced memory, as (EC5)–(EC10) require. It can remove auxiliary information and account for the positive defect (EC8)–(EC9). Or it can assert a memory-free sourced intertwining and face the conditional-sufficiency test (EC7), with (EC17) as a possible falsifier. These are different experiments. The identities do not provide a uniform rigidity bound, but they prevent a change of experiment from being hidden inside a claimed sewing equality.
