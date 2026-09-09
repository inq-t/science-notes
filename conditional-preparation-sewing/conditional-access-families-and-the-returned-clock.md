# Conditional Access Families and the Returned Clock

Conditional normalization extends the old marked transfer coherently through any finite family of new accesses. For every declared compact simple group, a sufficient fixed matrix inventory gives finite Casimir clocks whose values are independent of how many sibling accesses are present. The old preparation and its localized law remain unchanged. This removes a growing shared-rank obstruction for this common-endpoint family, while leaving an explicit collective source response: many new preparations continue to share the same old random information.

## One common endpoint and a family of actual paths

Fix the faithful representation \(\rho:G\to U(n)\), metric \(Q\), and unnormalized Hilbert–Schmidt preparation carrier \(E=\mathbb C^{n\times k}\) of [[general-causal-action/general-group-preparation-and-the-casimir-return|the general-group theorem]]. Let \(d=\dim G\) and \(m=nk\). An old product \(A=U_1U_2\) passes through one intermediate vertex. New paths \(W_i\) reach that same vertex, and supply
\[
L_i=U_1W_i^{-1},\qquad B_i=L_iA=U_1W_i^{-1}U_1U_2.
\tag{CF1}
\]
Every \(B_i\) has the same initial and final endpoints as \(A\). For a finite index set \(I\), quotienting only the intermediate-vertex action gives the complete carrier \(L^2(G^{1+|I|})\), in coordinates \((A,(B_i)_{i\in I})\), with product Haar. Fixing these words and choosing \(U_1\) determines \(U_2\) and every \(W_i\); normalized Haar along this fiber proves the claim, as in [[conditional-preparation-sewing/conditional-preparation-extension-at-new-access|the single-access construction]]. The endpoint gauges act simultaneously on all words, and remain to be imposed if the physical experiment gauges them.

Keep one old preparation and use independent conditional innovations:
\[
\Xi\sim\operatorname{CN}(0,\sigma^2I_E),\qquad
\Eta_i=a_i\Xi+\varepsilon_i,\qquad
\varepsilon_i\sim\operatorname{CN}(0,\tau_i^2I_E),
\qquad \sigma,\tau_i>0.
\tag{CF2}
\]
The variables \(\Xi,\varepsilon_i\) are independent; the \(\Eta_i\) are generally correlated. All preparations occupy the common terminal endpoint. Their joint law therefore respects the simultaneous gauge transport by \(\rho(h_2)\). Each finite covariance is faithful, and its old marginal is fixed. This is a particular coherent joint covariance within [[conditional-preparation-sewing/access-ports-and-conditional-sewing|conditional sewing]]; conditional independence of the innovations is additional data.

For \(h_\zeta(g)=\|[\rho(g)-I]\zeta\|^2\), define
\[
p_{\alpha,\Xi}(A,A')=e^{-\alpha h_\Xi(A^{-1}A')},\qquad
q_{i,\alpha,\Eta_i}(B_i,B_i')=e^{-\alpha h_{\Eta_i}(B_i^{-1}B_i')},
\]
\[
z_\alpha=\mathbb E\int_Ge^{-\alpha h_\Xi(g)}dg,\qquad
b_{i,\alpha}(\Xi)=\mathbb E\!\left[\int_Ge^{-\alpha h_{\Eta_i}(g)}dg\mid\Xi\right].
\tag{CF3}
\]
Comparison paces are set to one in this module. The full marked family is
\[
\boxed{
F_{I,\alpha}^{M}(q,q')
=z_\alpha^{-1}\mathbb E\!\left[
M(\Xi,(\Eta_i)_{i\in I})p_{\alpha,\Xi}(A,A')
\prod_{i\in I}\frac{q_{i,\alpha,\Eta_i}(B_i,B_i')}
{b_{i,\alpha}(\Xi)}\right].}
\tag{CF4}
\]
All denominators are source-free and remain fixed during source differentiation. Bounded joint marks are always admissible; the same formula covers integrable linear, quadratic and transported readout sources. This is the constitutive conditional normalization of [[conditional-preparation-sewing/conditional-normalization-and-marked-access|marked access]], not a single unmodified Gaussian determinant.

## Every subset has its exact marked transfer

For \(J\subset I\), let a mark \(M\) retain only \(\Xi\) and the preparations indexed by \(J\). Conditional independence in (CF2) and the definition of each denominator give the finite-width identity
\[
\boxed{
\int_{G^{I\setminus J}}F_{I,\alpha}^{M}(q,q')
\prod_{i\notin J}dB_i'
=F_{J,\alpha}^{M}(q_J,q_J').}
\tag{CF5}
\]
Each forgotten conditional factor integrates to one before averaging the old preparation or the retained innovations. The identity holds in any removal order, includes its scalar factors, and survives every temporal product of the corresponding retained marked operators. It concerns actual retained readout maps; sources on forgotten preparations cannot be silently retained under the name of an old mark.

For the unmarked operators, conditioning on all preparations proves Hilbert positivity by the Gaussian distance embedding. Almost surely each \(\Eta_i\) and \(\Xi\) has full row rank if \(k\ge n\), so faithfulness gives injectivity on the full carrier. The denominator weights are positive and configuration independent. Symmetry and (CF5), followed by the old row integral, give unit row sum and a self-adjoint Markov contraction. Simultaneous endpoint gauge covariance is exact.

Thus adding any number of the declared accesses does not alter an existing subset's free marked transfer. This coherence fixes \(\Xi\) as the retained parent; it does not prove equivalence after choosing a different retained parent. It is stronger than preserving the subset's prior covariance. It does not assert that all possible joint innovations satisfying pairwise marginals are equivalent; (AP5–9) gives the contrary mixed-source example. Nor does (CF5) survive arbitrary new interactions depending on forgotten words.

## A shifted Gaussian has uniformly controlled inverse moments

The general-group return requires a conditional estimate absent from a merely centered Gaussian calculation. Let \(Y=M+Z\in\mathbb C^{n\times k}\), where \(M\) is any deterministic matrix and \(Z\) has independent circular Gaussian entries of variance \(\tau^2>0\). Write \(\ell(Y)=\lambda_{\min}(YY^\dagger)\). Then
\[
\boxed{\sup_M\mathbb E\ell(Y)^{-p}<\infty
\qquad\text{for }0<p<k-n+1.}
\tag{CF6}
\]
To prove this, condition on every row except row \(i\), and project row \(i\) onto the orthogonal complement of their span. Almost surely this complement has complex dimension \(r=k-n+1\); the independent row noise remains isotropic on it, with a possibly nonzero projected mean \(\mu_i\). The Schur identity of (GG7) gives
\[
[(YY^\dagger)^{-1}]_{ii}
=\operatorname{dist}(Y_i,\operatorname{span}\{Y_j:j\ne i\})^{-2},
\]
\[
\mathbb E(e^{-t\operatorname{dist}^2}\mid\text{other rows})
=(1+\tau^2t)^{-r}
e^{-t\|\mu_i\|^2/(1+\tau^2t)}
\le(1+\tau^2t)^{-r}.
\tag{CF7}
\]
The Laplace formula for a negative power therefore bounds its \(p\)-moment by \(\tau^{-2p}\Gamma(r-p)/\Gamma(r)\), uniformly in the conditional mean. Finally use \(\ell^{-1}\le\operatorname{Tr}(YY^\dagger)^{-1}\) and the finite-sum power bound. The rows remain independent after a deterministic shift; their projected means need not be independent.

If \(p<r\) strictly, Hölder with an exponent still below \(r/p\) also gives
\[
\mathbb E[\ell(Y)^{-p}(1+\|Y\|)^b]
\le C_{p,b,\tau}(1+\|M\|)^b
\qquad(b\ge0),
\tag{CF8}
\]
up to enlarging the constant. Gaussian positive moments give the displayed polynomial dependence on the mean. Constants may depend on the fixed dimensions and variance; no uniform claim is made as \(\tau\downarrow0\).

## Conditional normalization prevents an additional old localization weight

Let \(g_\zeta\) be the real tangent metric of (GG4), and put
\[
w(\zeta)=(\det_Qg_\zeta)^{-1/2},\qquad
h_i(\Xi)=\mathbb E[w(\Eta_i)\mid\Xi],\qquad
d\nu_0=\frac{w(\Xi)dP_0(\Xi)}{\mathbb E w(\Xi)}.
\tag{CF9}
\]
Use the fixed sufficient inventory
\[
k>n+\frac d2.
\tag{CF10}
\]
Since \(g_Y\ge\ell(Y)I\), (CF6) bounds \(\mathbb Ew(Y)\) and \(\mathbb E[w(Y)\operatorname{tr}_Qg_Y^{-1}]\) uniformly in every deterministic mean. The second bound uses \(p=d/2+1<k-n+1\). Polynomially weighted versions follow from (CF8).

Conversely, \(g_Y\le\|Y\|^2I\), because \(\|d\rho(X)\|_{\rm op}^2\le\|d\rho(X)\|_{\rm HS}^2=Q(X,X)\). Thus Jensen gives
\[
h_i(\Xi)\ge
\mathbb E(\|\Eta_i\|^{-d}\mid\Xi)
\ge\big(|a_i|^2\|\Xi\|^2+m\tau_i^2\big)^{-d/2}.
\tag{CF11}
\]
The conditional normalization is bounded away from zero by a reciprocal polynomial in the old norm, not by a uniform constant.

The exact row integral also has a useful bound before taking a limit. Integration over a sufficiently small exponential-coordinate ball yields
\(\int_Ge^{-\alpha h_Y(g)}dg\ge c(1+\alpha\|Y\|^2)^{-d/2}\): on that ball \(h_Y(g)\le C\|Y\|^2\operatorname{dist}_Q(g,e)^2\). Conditional Jensen then gives, for \(\alpha\ge1\),
\[
\alpha^{d/2}b_{i,\alpha}(\Xi)
\ge c\big(1+|a_i|^2\|\Xi\|^2+m\tau_i^2\big)^{-d/2}.
\tag{CF12}
\]
The upper row and second-moment bounds from (GG9), averaged conditionally and controlled by (CF6), are uniform in \(\Xi\). After division by (CF12), every scaled conditional second moment is polynomially bounded in \(\|\Xi\|\). These bounds are integrable against the old localization and its scaled second-moment majorant, by the polynomially weighted version of the centered inverse-moment theorem.

For \(c_G=\pi^{d/2}/\operatorname{Vol}_Q(G)\), conditional dominated localization now gives \(\alpha^{d/2}b_{i,\alpha}(\Xi)\to c_Gh_i(\Xi)\). The joint limiting preparation law is
\[
\boxed{
d\widetilde\nu_I
=d\nu_0(\Xi)
\prod_{i\in I}\frac{w(\Eta_i)}{h_i(\Xi)}P_i(d\Eta_i\mid\Xi).}
\tag{CF13}
\]
Each conditional factor is a probability measure. In particular the old marginal is exactly \(\nu_0\), independently of \(|I|\); adding siblings does not multiply it by extra \(h_i(\Xi)\). The locality/rank failure for one scalar norm shared through a growing unnormalized comparison, proved in [[general-causal-action/preparation-rank-and-locality|preparation rank and locality]], does not apply to this different normalization law.

## All finite families return consistent Casimir clocks

Define
\[
\kappa_0=\frac1{4d}\mathbb E_{\nu_0}\operatorname{tr}_Qg_\Xi^{-1},\qquad
\kappa_i=\frac1{4d}\mathbb E_{\nu_0}
\frac{\mathbb E[w(\Eta_i)\operatorname{tr}_Qg_{\Eta_i}^{-1}\mid\Xi]}
{h_i(\Xi)}\in(0,\infty).
\tag{CF14}
\]
The numerator is uniformly bounded by (CF6); the denominator estimate (CF11) reduces finiteness to an old polynomial moment. Simultaneous \(\rho(G)\) invariance of (CF13) makes the separately averaged inverse metrics scalar. Conditional tangent covariances are block diagonal in the actual path coordinates, so
\[
\boxed{H_I=\kappa_0D_{Q,A}+\sum_{i\in I}\kappa_iD_{Q,B_i},\qquad
\alpha(F_{I,\alpha}-I)f\longrightarrow-H_If,\qquad
F_{I,N/t}^{\,N}\longrightarrow e^{-tH_I}.}
\tag{CF15}
\]
The first limit is uniform for smooth functions; the product limit is strong on the complete carrier and its gauge-invariant subspace, uniformly on bounded nonnegative times. Every coefficient is identical to its value when that access is added alone. The old coefficient is exactly its isolated value. The sufficient inventory (CF10) is independent of the number of accesses.

For completeness, a fourth inverse moment is unnecessary under (CF10). Condition on \(\Xi\), so the relative group increments of the different new paths are independent, with their normalized conditional kernels. Each is invariant under inversion, as is the old fixed-preparation increment. Separate inversion cancels all linear and mixed second derivatives. Its individual second moments converge by (GG9), (CF6) and (CF12). A second-order Taylor remainder is bounded by \(o(1)\) times the sum of squared increments in a common small neighborhood. Outside that neighborhood, its contribution after multiplication by \(\alpha\) tends to zero by the individual second-moment tail bounds and conditional independence. Specifically, a cross-tail term \(\alpha\mathbb E[|\delta_i|^2\mathbf1_{|\delta_j|>\epsilon}\mid\Xi]\), \(i\ne j\), factors into the scaled second moment of increment \(i\) times the conditional tail probability of increment \(j\); the latter tends to zero, and the former has the preceding integrable old-preparation majorant. This also applies when one increment is the old fixed-preparation increment, with its row mass retained in the outer measure. Integrating over \(\Xi\) is dominated by the old inverse moments with polynomial factors described after (CF12). This proves the smooth-core limit. Finite Peter–Weyl sums give a dense invariant core, and exact contractivity proves the strong product return.

In the inherited \((U,L_i)\) coordinates, the same operator has the quadratic form
\[
\mathcal E_I(F)=\int\sum_a\left[
\kappa_0\left|\mathcal L_{U,e_a}F-
\sum_{i\in I}\mathcal R_{L_i,e_a}F\right|^2
+\sum_{i\in I}\kappa_i|\mathcal L_{L_i,e_a}F|^2\right]dU\prod_i dL_i.
\tag{CF16}
\]
Changing \(A\) on the left at fixed all \(B_i\) right-translates every \(L_i\) by the same inverse; changing \(B_i\) on the left changes only \(L_i\). Thus mixed loop motion is present, with the common old path supplying the common derivative. The formula is an exact coordinate transform of (CF15), not a derived bounded-incidence spatial lattice metric.

The consistency also permits a countable common-endpoint family as a cylinder construction. On product Haar, define \(F_{\infty,\alpha}\) on a cylinder by any finite operator containing its coordinates. Equation (CF5) makes this well defined; contractions and positivity extend it to all \(L^2\) of the countable product. The tensor heat semigroup with generator the closure of the finite sums in (CF15) is likewise fixed on cylinders. Convergence there, density and contractivity give the strong product limit on the countable carrier. This statement supplies no spatial continuum topology, gauge-field distribution or four-dimensional translation representation.

## The common old preparation leaves a collective response

Take the defining \(SU(2)\) representation, \(k\ge2\), identical nonzero \(a_i=a\), and identical \(\tau_i=\tau>0\). Write \(S=\|\Xi\|^2\), \(T_i=\|\Eta_i\|^2\). The special norm identity gives the lower sufficient inventory of [[conditional-preparation-sewing/conditional-normalization-and-marked-access|the SU(2) conditional return]]; it does not require the general bound (CF10). Under (CF13), \(S\sim\operatorname{Gamma}(m-3/2,\sigma^2)\), and the \(T_i\) are conditionally independent given \(S\), with conditional mean
\[
\mu(s)=\frac{h_{1/2}(s)}{h_{3/2}(s)},
\qquad h_p(s)=\mathbb E(T_i^{-p}\mid S=s).
\tag{CF17}
\]
The Poisson-mixture proof in (NA14) shows that \(\mu\) is strictly increasing when \(a\ne0\). Conditional moments through order two are finite and bounded by their untilted noncentral Gaussian norm moments, because the additional \(T_i^{-3/2}\) weight is decreasing. Consequently, for distinct siblings,
\[
\boxed{\operatorname{Cov}_{\widetilde\nu_I}(T_i,T_j)
=\operatorname{Var}_{\nu_0}(\mu(S))>0.}
\tag{CF18}
\]
There is no dependence on the number of other accesses. For \(N\) identical siblings the same conditional variance identity gives
\[
\operatorname{Var}\!\left(\frac1N\sum_{i=1}^NT_i\right)
=\operatorname{Var}_{\nu_0}(\mu(S))
+\frac1N\mathbb E_{\nu_0}\operatorname{Var}(T_1\mid S).
\tag{CF19}
\]
The shared component therefore survives averaging over arbitrarily many innovations. These are actual limiting preparation norm marks. The free operator (CF15) has the constant vacuum and product Haar configuration law in \((A,B_i)\), despite this auxiliary norm covariance; it is not a physical configuration-correlation theorem. [[physical-response-coercivity/conditional-vacuum-rigidity-and-the-physical-gap|Conditional vacuum rigidity]] specifies the stronger physical source map and mixed-response estimate that a mass-gap argument must supply.

## The same finite family returns a general-group interacting vacuum

For a finite set \(I\), retain the old preparation in every actual identity comparison and choose \(\beta_i\ge0\):
\[
\mathcal C_I(q,\Xi)=\frac12\sum_{i\in I}\beta_i
\|[\rho(L_i)-I_n]\rho(U)\Xi\|^2,\qquad
f_{\alpha,q}=e^{-\mathcal C_I(q,\Xi)/(2\alpha)}.
\tag{CF20}
\]
Insert \(f_{\alpha,q}f_{\alpha,q'}\) in (CF4), keeping every source-free \(b_{i,\alpha}(\Xi)\) and \(z_\alpha\). These are multiplication rows based at the common initial endpoint, with the old path transport retained. Conditional Gaussian distance positivity and domination by the free Markov kernel give positive injective contractions. The finite cost is bounded by \(2(\sum_i\beta_i)\|\Xi\|^2\), so the polynomially weighted bounds above justify its endpoint expansion without changing the sufficient inventory (CF10).

The resulting strong product limit is generated by
\[
\boxed{H_{I,\beta}=H_I+V_{I,\beta},\qquad
V_{I,\beta}=\sum_{i\in I}\beta_i\operatorname{Tr}
[\overline A_0(I_n-\operatorname{Re}\rho(L_i))],\qquad
\overline A_0=\mathbb E_{\nu_0}(\Xi\Xi^\dagger).}
\tag{CF21}
\]
The old marginal in (CF13) fixes \(\overline A_0\) independently of sibling count. Its commutation with \(\rho(G)\) removes \(\rho(U)\) only from the leading expected potential, as in the general-group weak-cost theorem. For irreducible \(\rho\), that owner gives \(\overline A_0=\sigma^2(m-d/2)I_n/n\); faithful reducible choices use its positive block coefficients. This generalizes the finite interacting SU(2) return (NA15–16). On each fixed compact carrier the operator is uniformly elliptic with bounded smooth potential, the inherited \(H^1\) form and \(H^2\) operator domains, and a simple positive gauge-invariant ground vector.

At zero strengths for newly added accesses, the entire retained interacting marked kernel still satisfies (CF5), since its endpoint features involve only the retained words and \(\Xi\). A positive new strength introduces a real interaction and generally changes that old readout. No interacting countable-family limit, uniform vacuum estimate or graph-independent physical gap follows from the free cylinder construction. Such a statement requires additional control of the potentials and of the actual interacting source response.

## Two accesses recover the complete two-plaquette operator

The two-sibling member has a concrete interacting calibration. Use \(SU(2)\) with its defining representation, \(k\ge2\), and \(m=2k\). Allow a new comparison pace \(r_i>0\) by replacing \(\alpha\) with \(\alpha/r_i\) in both \(q_{i,\alpha,\Eta_i}\) and \(b_{i,\alpha}(\Xi)\). The exact marked identity (CF5) is unchanged. The same constant \(r_i^{d/2}\) appears in the conditional numerator and row normalization, leaving (CF13) unchanged and multiplying \(\kappa_i\) by \(r_i\).

After imposing both endpoint Gauss actions, the full physical carrier is \(L^2(SU(2)^2)^{\operatorname{Ad}SU(2)}\) on \((L_1,L_2)\). The independent final-endpoint action removes \(U\); the initial-endpoint action conjugates the two loops together. Restricting (CF16), and choosing the declared positive paces \(r_i\kappa_i=3\kappa_0\), gives
\[
\begin{aligned}
H_{\rm el}
&=(\kappa_0+r_1\kappa_1)D_{Q,L_1}
+(\kappa_0+r_2\kappa_2)D_{Q,L_2}
-2\kappa_0\sum_a\mathcal R_{L_1,e_a}\mathcal R_{L_2,e_a}\\
&=4\kappa_0(D_{Q,L_1}+D_{Q,L_2})
-2\kappa_0\sum_a\mathcal R_{L_1,e_a}\mathcal R_{L_2,e_a}.
\end{aligned}
\tag{CF22}
\]
The metric convention matters. The [[coarse-response-memory/two-plaquette-vacuum-and-relational-state|two-plaquette benchmark]] uses \(Q_{\rm TP}=-2\operatorname{Tr}=2Q\), so \(D_Q=2D_{Q_{\rm TP}}\) and a \(Q\)-orthonormal derivative is \(\sqrt2\) times its \(Q_{\rm TP}\) counterpart. Consequently, with
\[
\boxed{\kappa_{\rm TP}=2\kappa_0
=\frac1{\sigma^2(m-5/2)},\qquad
\lambda_i=\beta_i\sigma^2(m-3/2),}
\]
\[
H_{I,\beta}
=4\kappa_{\rm TP}(D_{{\rm TP},1}+D_{{\rm TP},2})
-2\kappa_{\rm TP}\sum_a R_{{\rm TP},1,a}R_{{\rm TP},2,a}
+\lambda_1(1-a)+\lambda_2(1-b),
\qquad
H_{\rm el}(ab)=\kappa_{\rm TP}(6ab-z/2).
\tag{CF23}
\]
Here \(L_1=aI-i\mathbf x\cdot\boldsymbol\sigma\), \(L_2=bI-i\mathbf y\cdot\boldsymbol\sigma\), and \(z=\mathbf x\cdot\mathbf y\); these scalar trace coordinates are unrelated to the preparation coefficients \(a_i\). The last equality is the benchmark's exact kinetic mixed-response identity. Equal \(\lambda_i\) gives its symmetric operator, including its actual relational vacuum and inherited invariant domains. Arbitrary nonnegative \(\lambda_i\) are available through the declared \(\beta_i\). Nonzero conditional coefficients \(a_i\) can be retained throughout, so neither the shared norm response nor the composite-word mixed motion has been removed.

This is recovery of the complete finite two-plaquette operator after matching specified inputs. The ratio \(r_i\kappa_i=3\kappa_0\) has not been selected by the preparation law, and its finite-width marked kernel need not equal the raw-link construction in [[general-causal-action/local-incidence-preparations-and-the-gauge-transfer|local incidence preparation, LI12]]. The next geometric test must therefore involve a growing diagram with more than one conditional parent; repeating this two-access calibration alone supplies no new sewing principle.

The free family has exact extension order, all-subset marked consistency, fixed preparation rank per access, and stable finite clocks; every finite member also has the interacting return (CF21). Its graph nevertheless has a common endpoint and an increasing number of accesses sharing one old path. No spatial separation between the siblings has been derived. Reusing this pattern throughout a physical reconstruction requires a law for which accesses share a conditional parent, how transported covariances sew between distinct ports, and how the returned interacting physical source responses scale. Conditional normalization solves a definite growing-family consistency problem; it does not select the required Yang–Mills spatial family or the cosmological geometry.
