# A Local Product Comparison Retains a Divergent Relative Response

Replacing conditional refresh by a local product comparison changes the relative process, but does not give its base and resolved boundary the same response scale. The inherited metric has indispensable cross terms and a relative cometric growing with refinement. Row normalization also selects an invariant state: weighting a comparison by the desired density generally returns a different density. These exact calculations distinguish a change of processing law from a change of coordinates or clock units.

**Status: exact finite-comparison states and differential identities; local Gaussian limits and an obstruction for the stated scalar normalization.** The group, product overlap and normalization protocol remain inputs. No effective slow-generator theorem, full-carrier homogenization, or physical mass identification is asserted.

## Keep state refinement separate from comparison refinement

Use the anchored \(SU(2)\) densities \(p_k\), their convolutions \(q_k=p_k*p_k\), and the metric \(Q=-2\operatorname{Tr}\) from [[sewn-overlap-refinement|the complete multiplier calculation]]. On \(M=G^2\), with product Haar measure \(d\mu=dx\,dy\), the proposed target state is

\[
w_k(x,y)=q_k(xy^{-1}),\qquad \int_Mw_k\,d\mu=1.
\tag{LP1}
\]

The integer \(k\) controls the width of this state. Introduce a separate integer \(m\) for the local product comparison,

\[
K_m((x,y),(x',y'))=p_m(x^{-1}x')p_m(y^{-1}y'),
\qquad T_m=B_m\otimes B_m.
\tag{LP2}
\]

This is the row-normalized version relative to Haar of the primitive overlap
\(\kappa(x^{-1}x')^m\kappa(y^{-1}y')^m\), where
\(\kappa(g)=(4+\chi_1(g))/6\). It is a symmetric positive Markov kernel. The single-factor principal-log covariance is \((12I+o(1))/m\) in a \(Q\)-orthonormal Lie coordinate. Consequently, on every fixed smooth test function,

\[
m(T_m-I)f\longrightarrow6\Delta_Mf,
\qquad \Delta_M=\Delta_x+\Delta_y.
\tag{LP3}
\]

Taylor expansion under the symmetric concentrated kernel proves (LP3): each factor contributes one half its covariance times its Laplacian. The fixed-degree multiplier expansion gives the same normalization. The limit is first taken at fixed \(k\). When \(m\) and \(k\) vary together, an infinitesimal expansion in the resolved variable additionally needs \(k/m\to0\) and control of the varying derivatives. The case \(m/k\to\lambda\in(0,\infty)\) is a different limit, computed below.

## The exact moving rows contain a mixed derivative

Put \(g=xy^{-1}\), so \(x=gy\) and \(d\mu=dg\,dy\). Fix a \(Q\)-orthonormal basis \(T_a\) of the Lie algebra. The conventions are explicit:

\[
\begin{aligned}
L_{g,a}F&=\left.\frac d{dt}\right|_0F(e^{tT_a}g,y),\\
R_{g,a}F&=\left.\frac d{dt}\right|_0F(ge^{tT_a},y),\\
X_{y,a}F&=\left.\frac d{dt}\right|_0F(g,e^{tT_a}y).
\end{aligned}
\tag{LP4}
\]

A left variation of the raw \(x\) coordinate gives \(g\mapsto e^{tT_a}g\). A left variation of raw \(y\) gives \((g,y)\mapsto(ge^{-tT_a},e^{tT_a}y)\). Thus the six inherited product rows are

\[
Z=(L_g,\ X_y-R_g),\qquad
\Delta_M=2\Delta_g+\Delta_y-2\sum_aR_{g,a}X_{y,a}.
\tag{LP5}
\]

The two copies of \(\Delta_g\) agree by bi-invariance. Rows acting on separate \(g,y\) coordinates commute; the mixed derivative is therefore exactly as displayed.

On the principal logarithm chart write \(g=\exp(Y/\sqrt{k})\), and define

\[
J(Z)=\frac{1-e^{-\operatorname{ad}Z}}{\operatorname{ad}Z},
\qquad
g^{-1}dg=J(Y/\sqrt{k})\frac{dY}{\sqrt{k}}.
\tag{LP6}
\]

The quotient at zero is its analytic continuation. This is the body Maurer--Cartan convention: a right variation \(ge^{tT_a}\) has body velocity \(T_a\), hence

\[
R_gF=\sqrt{k}\,J(Y/\sqrt{k})^{-T}\nabla_YF.
\tag{LP7}
\]

This checks the transpose and the sign in the moving row. Let \(\eta=dy\,y^{-1}\). Since \(dx\,x^{-1}=dg\,g^{-1}+\operatorname{Ad}_g\eta\), invariance of \(Q\) gives the exact covariant metric

\[
|dx\,x^{-1}|^2+|dy\,y^{-1}|^2
=2|\eta|^2+\frac2{\sqrt{k}}\langle\eta,JdY\rangle
+\frac1k|JdY|^2.
\tag{LP8}
\]

Equivalently, its cometric applied to a function is

\[
\boxed{
\sum_i|Z_iF|^2
=k|J^{-T}\nabla_YF|^2
+|X_yF-\sqrt{k}J^{-T}\nabla_YF|^2.
}
\tag{LP9}
\]

At \(Y=0\), the covariant and contravariant blocks, in the order \((y,Y)\), are

\[
\begin{pmatrix}2I&I/\sqrt{k}\\I/\sqrt{k}&I/k\end{pmatrix},
\qquad
\begin{pmatrix}I&-\sqrt{k}I\\-\sqrt{k}I&2kI\end{pmatrix}.
\tag{LP10}
\]

The global domain remains inherited from \(G^2\). The logarithm has a Haar-null cut, and this chart introduces no new boundary condition. Compactly supported resolved tests used below vanish before reaching that cut.

## Row normalization computes its own stationary state

For any fixed smooth strictly positive function \(v\) on \(M\), define the degree and normalized comparison

\[
d_{m,v}=T_mv,\qquad
P_{m,v}f=\frac{T_m(vf)}{d_{m,v}}.
\tag{LP11}
\]

Its exact invariant probability law is

\[
\boxed{
d\nu_{m,v}
=\frac{v\,T_mv}{\langle v,T_mv\rangle_\mu}\,d\mu.
}
\tag{LP12}
\]

Indeed, multiplying its transition density by \(v(z)d_{m,v}(z)\) leaves the symmetric conductance \(v(z)K_m(z,z')v(z')\). Positivity and compactness make all denominators positive. This proves detailed balance without presupposing the desired invariant law.

At fixed \(v\), (LP3) and division by the positive denominator give on smooth tests

\[
\begin{aligned}
m(I-P_{m,v})f
&\longrightarrow-6\left[\Delta_Mf
+2\nabla\log v\cdot\nabla f\right],\\
d\nu_{m,v}&\longrightarrow
\frac{v^2\,d\mu}{\int v^2d\mu}.
\end{aligned}
\tag{LP13}
\]

The cross derivatives in (LP5) enter this Laplacian and drift. Taking \(v=w_k\) therefore returns \(w_k^2\) in this narrow-comparison limit. Taking \(v=\sqrt{w_k}\) instead gives the desired limiting state \(w_k\) and the positive differential operator

\[
\mathcal A_k
=-6\left[\Delta_M+\nabla\log w_k\cdot\nabla\right]
=6\sum_i Z_i^{*,w_k}Z_i.
\tag{LP14}
\]

For each fixed \(k\), smooth positive weighting on the compact covering manifold gives the inherited \(H^2\) operator domain and \(H^1\) form domain. At finite \(m\), half weighting still has invariant density proportional to \(\sqrt{w_k}T_m\sqrt{w_k}\), not exactly \(w_k\). Half weighting changes the drift; it does not change (LP9).

There is an exact-state conservative alternative at finite \(m\):

\[
\mathcal G_{m,w}f
=m w^{-1/2}\left[fT_m\sqrt w-T_m(\sqrt w f)\right].
\tag{LP15}
\]

Its Dirichlet form in \(L^2(wd\mu)\) is

\[
\frac m2\int K_m(z,z')\sqrt{w(z)w(z')}
|f(z)-f(z')|^2\,d\mu(z)d\mu(z').
\tag{LP16}
\]

Thus it is a nonnegative self-adjoint conservative jump generator with exactly the state \(w\), and (LP14) is its smooth differential limit. Its total jump rate is \(mT_m\sqrt w/\sqrt w\). This is a different finite processing rule, not a proof that row normalization already preserved \(w\).

## The state and derivative must be transported together

Let \(s_a=R_{g,a}\log w_k\). Since \(w_k\) depends only on \(g\), (LP14) is exactly

\[
\mathcal A_k=-6\left[
2\Delta_g+\Delta_y-2R_g\cdot X_y
+2s\cdot R_g-s\cdot X_y\right].
\tag{LP17}
\]

In deriving it, \(L_g\log w_k\cdot L_gF=R_g\log w_k\cdot R_gF\) follows from the orthogonal adjoint action. The other product row differentiates the weight as \((X_y-R_g)\log w_k=-s\).

[[resolved-relative-boundary-and-two-clock-limits|The exact common-carrier construction]] owns the quantile maps that transport \(w_kdg\) to a fixed Gaussian measure. A coordinate pullback transports every row by its Jacobian. A subsequent density-unitary \(F\mapsto\sqrt{r}F\) transports a row \(Z\) to \(Z-\tfrac12Z\log r\). These are the [[conditional-fisher-coercivity/moving-fiber-connection|moving-fiber identities]], not additional Fisher potentials. Neither operation removes the principal symbol in (LP9).

The formulas here use the principal-log coordinate \(Y=\sqrt{k}\log g\). They are not derivative-convergence assertions for the quantile maps: weak convergence of a measure or convergence of its quantiles alone does not prove convergence of those maps' derivatives.

## A comparison at the state width has finite resolved jumps

Suppose \(m/k\to\lambda\in(0,\infty)\), and take \(v=w_k^\alpha\) with fixed \(\alpha>0\). For a central relative function, the product comparison reduces exactly to

\[
T_m[v(xy^{-1})]=(q_m*v)(xy^{-1}).
\tag{LP18}
\]

To verify this, write \(x'=xu_1\), \(y'=yu_2\) in the Haar integral. The relative increment contains \(u_1u_2^{-1}\), whose central law is \(q_m\); conjugation by \(y\) does not change that law. In particular, weighting by \(q_k\) gives the exact finite relative stationary density proportional to

\[
q_k(g)(q_m*q_k)(g).
\tag{LP19}
\]

The local density form of the anchored-overlap Laplace expansion gives, in \(Y=\sqrt{k}\log g\),
\(w_k\) proportional to \(\exp(-|Y|^2/48)\) at leading order. A \(q_m\) proposal has resolved increment covariance \(24I/\lambda\). The Baker--Campbell--Hausdorff correction vanishes on bounded resolved sets. The limiting row density is therefore proportional to

\[
\exp\left[-\frac{\lambda|Y'-Y|^2+\alpha|Y'|^2}{48}\right].
\tag{LP20}
\]

Completing the square yields

\[
\boxed{
Y'\mid Y\ \sim\
N\left(\frac{\lambda}{\lambda+\alpha}Y,
\frac{24}{\lambda+\alpha}I\right),\qquad
\Sigma_{\lambda,\alpha}
=\frac{24(\lambda+\alpha)}{\alpha(2\lambda+\alpha)}I.
}
\tag{LP21}
\]

The second covariance is the invariant Gaussian covariance: it solves
\(\Sigma=[\lambda/(\lambda+\alpha)]^2\Sigma+24I/(\lambda+\alpha)\).
It also follows directly by multiplying the two limiting factors in (LP12).

These are limits of the local transition laws and invariant probability laws. The Laplace expansion is uniform on bounded resolved sets; its Gaussian bounds and exponentially small mass outside fixed group neighborhoods control the normalization and polynomial moments. No full-carrier operator-norm convergence is inferred from this calculation. The base increment has size \(m^{-1/2}\), so the base is unchanged in this one-step resolved limit.

For \(m=k\) and \(\alpha=1\), (LP21) gives covariance \(16I\). In (LP19), the two factors have resolved covariances \(24I\) and \(48I\), whose product has covariance \(16I\). It is neither the original \(24I\) nor the narrow-comparison \(w_k^2\) covariance \(12I\). Half weighting at the same scale gives \(144I/5\), also different from \(24I\). Only the further limit \(\lambda\to\infty\) gives covariance \(12I/\alpha\), consistent with (LP13).

## One scalar pace does not preserve both inherited form directions

For the target-state differential clock (LP14), its form is exactly

\[
\mathcal E_k[F]
=6\int\left[k|J^{-T}\nabla_YF|^2
+|X_yF-\sqrt{k}J^{-T}\nabla_YF|^2\right]w_k(g)dg\,dy.
\tag{LP22}
\]

Choose a nonconstant smooth base test \(F=\phi(y)\). Its squared norm and form are independent of \(k\), with

\[
\mathcal E_k[\phi]=6\int|X_y\phi|^2dy.
\tag{LP23}
\]

Independently choose a smooth compactly supported nonconstant \(h\) on the resolved Lie algebra, and put \(F_k(g,y)=h(\sqrt{k}\log g)\). For sufficiently large \(k\), it extends smoothly by zero before the logarithm cut. Subtracting its state mean if desired does not change its form. The resolved measure tends to \(\gamma=N(0,24I)\), while \(J(Y/\sqrt{k})\to I\) uniformly on the support. Thus

\[
\|F_k\|^2\longrightarrow\|h\|_\gamma^2,\qquad
\frac{\mathcal E_k[F_k]}k
\longrightarrow12\int|\nabla_Yh|^2d\gamma>0.
\tag{LP24}
\]

Multiplying the whole form by one positive scalar \(c_k\) cannot make both (LP23) and (LP24) converge to finite nonzero values. The first requires \(c_k\) to tend to a finite positive constant; the second requires \(kc_k\) to do so. These are independent test directions of the inherited response. The proof retains all cross terms: their disappearance for either separate test does not authorize dropping them on mixed tests.

This does not identify the effective slow base generator after fast relative modes are eliminated. Mixed correctors can change that return. Nor does it claim a full quantile-carrier form limit without derivative estimates for its transport. It identifies the incompatible scaling of two explicitly resolved inherited directions.

Local density differentiation also shows why this differs from wholesale refresh. On bounded resolved charts, \(s\sim-\sqrt{k}Y/24\), so the leading relative part of (LP17) is

\[
-12k\left[\Delta_Y-\frac{Y}{24}\cdot\nabla_Y\right].
\tag{LP25}
\]

It is an Ornstein--Uhlenbeck differential row with fundamental rate \(k/2\), alongside mixed terms of order \(\sqrt{k}\). A local oscillator row has appeared, but its scale is still incompatible with finite base and relative response under one scalar normalization.

[[general-causal-action/gaussian-overlap-balancing-and-clock-sewing|Gaussian overlap balancing]] is a distinct constructive revision that constrains a comparison relative to its covariance and sewing law. [[rg-covariance-residue/gaussian-readout-naturality|Gaussian readout naturality]] tests how such a rule behaves under changes of readout. Neither is supplied by deleting the cross term or altering time units in this product metric. The [[directed-analytic-realization/purification-fluctuation-and-the-oscillator-return|purification oscillator return]] likewise has its own parent comparison. A claimed joint realization must state which operation selects its mobility and must still recover the [[coarse-response-memory/correlated-interface-tangent|certified relative-angle response]] when it claims the supplied Yang--Mills member.
