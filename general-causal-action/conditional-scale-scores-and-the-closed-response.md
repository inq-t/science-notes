# Conditional Scale Scores and the Closed Response

Conditional normalization changes the homogeneous preparation source as well as the transfer. Each innovation-variance score is centered against its actual parent-conditioned comparison law. These scores are orthogonal in the complete free preparation experiment, while a closed weight or a physical readout can couple them again. The resulting exact Hessian retains the conditional contact terms. This extends the common-source normalization test to directed preparation diagrams without identifying auxiliary Fisher information with a physical gap or a cosmic restoring force.

## Vary the law rather than insert a fixed-normalizer mark

Use the finite same-port diagram of [[conditional-preparation-diagrams-and-ancestral-readout|PD1–14]], with fixed arrows, coefficients \(a_{ij}\), comparison paces, representation and width \(\alpha>0\). Give node \(i\)'s innovation the variance \(s_i\tau_i^2\), and write
\[
u_i=\log s_i,\qquad
\mu_i=\sum_{j\in\operatorname{pa}(i)}a_{ij}\xi_j,\qquad
t_i=\frac{\|\xi_i-\mu_i\|^2}{s_i\tau_i^2},\qquad m=nk.
\tag{CS1}
\]
All derivatives below hold the actual matrix coordinates fixed. In particular the parent values in \(\mu_i\) are held fixed, even when their own variance parameters change. The Gaussian conditional density has
\[
\partial_{u_i}\log P_i=t_i-m,
\qquad \partial_{u_i}t_i=-t_i.
\tag{CS2}
\]
Let \(\zeta_i(\xi_i)\) be the source-free group row integral and define
\[
\begin{aligned}
b_i(u_i,\xi_{\operatorname{pa}(i)})
&=\int\zeta_i(\xi_i)P_i(d\xi_i\mid\xi_{\operatorname{pa}(i)}),\\
\nu_i(d\xi_i\mid\xi_{\operatorname{pa}(i)})
&=\frac{\zeta_i(\xi_i)}{b_i}P_i(d\xi_i\mid\xi_{\operatorname{pa}(i)}),
\qquad \nu_D=\prod_i\nu_i.
\end{aligned}
\tag{CS3}
\]
Here \(\nu_D\) denotes the exact finite-width row preparation law, called \(\nu_{D,\alpha}\) in PD11. The dependence on \(\alpha\) is suppressed until the localization paragraph. It is not the original Gaussian prior.

The factors \(\zeta_i\) have no explicit \(u_i\)-dependence at fixed \(\xi_i\), whereas \(b_i\) must be recomputed when the Gaussian law changes. This is different from an auxiliary linear or quadratic mark, whose source-free denominator is held fixed in PD4. Confusing the two derivatives omits the terms below.

Write the conditional mean and variance as
\[
\overline t_i=\mathbb E_{\nu_i}[t_i\mid\operatorname{pa}(i)],
\qquad v_i=\operatorname{Var}_{\nu_i}(t_i\mid\operatorname{pa}(i)).
\tag{CS4}
\]
Differentiating the finite conditional integrals gives
\[
\boxed{
\partial_{u_i}\log b_i=\overline t_i-m,\qquad
\partial_{u_i}^2\log b_i=v_i-\overline t_i.}
\tag{CS5}
\]
Indeed \(\partial_{u_i}\overline t_i=-\overline t_i+v_i\), by differentiation of the normalized conditional law. At fixed width and parameters in a compact positive neighborhood, reciprocal-polynomial row bounds and Gaussian domination justify these derivatives and their moments. These are conditional versions of [[closed-normalization-and-cosmic-response|CN15]], with random parent data retained.

## The full preparation scores are orthogonal innovations

The complete score for node parameter \(u_i\) is
\[
\boxed{S_i:=\partial_{u_i}\log\nu_D=t_i-\overline t_i.}
\tag{CS6}
\]
Other conditional density factors depend on their own variance parameters and on the fixed matrix coordinates, not explicitly on \(u_i\). Thus (CS6) contains exactly one node contribution. In a topological ordering, let \(\mathcal F_i=\sigma(\xi_1,\ldots,\xi_i)\). Then
\[
\mathbb E[S_i\mid\mathcal F_{i-1}]=0,
\qquad
\mathbb E S_iS_j=\delta_{ij}\mathbb E v_i.
\tag{CS7}
\]
For \(i<j\), condition on \(\mathcal F_{j-1}\); \(S_i\) is measurable and the conditional mean of \(S_j\) vanishes. The diagonal identity is conditional variance. Consequently the Fisher matrix of the full preparation experiment is
\[
\boxed{I_{ij}^{\rm prep}=\delta_{ij}\mathbb E v_i.}
\tag{CS8}
\]
Each diagonal entry is finite and positive: the conditional density is positive on a full Gaussian carrier, on which \(t_i\) is not constant. The bound need not be uniform over growing depth or vanishing innovation variance.

These are parameter scores, not claims that the matrices or their norms are independent. Correlated sibling norm observables still have the persistent covariance proved in [[conditional-access-families-and-the-returned-clock|CF18–19]]. Orthogonality in (CS7) is supplied by the actual conditional centering in (CS6).

If all log variances move together, \(u_i=u\), put \(S=\sum_iS_i\) and \(B=\sum_i v_i\). At fixed matrices, the score derivatives satisfy
\[
\partial_{u_j}S_i=-\delta_{ij}(S_i+v_i),
\qquad
\partial_uS=-S-B,
\qquad
I_{uu}^{\rm prep}=\mathbb E B.
\tag{CS9}
\]
The derivative of \(\log\nu_D\)'s normalization vanishes, as it must: \(\mathbb E S=0\) and \(\mathbb E[S^2+\partial_uS]=0\).

For an ancestral set \(J\), choose a topological ordering with \(J\) first. PD's exact marginal theorem and (CS7) give
\[
\mathbb E[S\mid\xi_J]=\sum_{i\in J}S_i.
\tag{CS10}
\]
The retained scores and their joint law are unchanged when descendants are added. New descendants can add information to the complete experiment while leaving the retained marked experiment unchanged. A nonancestral readout instead retains the hidden normalizer from PD6 and need not have the nodewise score formula of an isolated diagram.

## A physical readout can couple the orthogonal scores

Let \(Y\) be a declared observation obtained from the preparations through a parameter-independent conditional law at fixed matrix values. It can include actual group increments and configurations. Extra normalized increment kernels built from a reused matrix satisfy this condition when their paces, width and row normalizers are functions of that matrix rather than explicit functions of \(u_i\). If the observation law or its source labels themselves vary with \(u_i\), their direct derivatives must also be included.

Under the usual dominated differentiation, the observed score is
\[
\widehat S_i(Y)=\mathbb E[S_i\mid Y].
\tag{CS11}
\]
This follows by differentiating the joint integral before normalizing the observed density. Applying total covariance gives the exact information balance
\[
\boxed{
I^{\rm obs}_{ij}
=\delta_{ij}\mathbb E v_i
-\mathbb E\operatorname{Cov}(S_i,S_j\mid Y),
\qquad 0\le I^{\rm obs}\le I^{\rm prep}.}
\tag{CS12}
\]
The matrix inequality is positive-semidefinite order. Thus a physical readout can have off-diagonal response even when the full innovation-parameter Fisher matrix is diagonal. The missing conditional covariance records which distinctions the observation has discarded. [[scale-score-connection/inq|Scale-score transport]] and [[rg-covariance-residue/joint-fisher-response-of-normalized-gauge-blocking|normalized gauge Fisher response]] own the corresponding moving-channel and physical-carrier distinctions.

There is no mass-gap conclusion in (CS12). Its parameters are Gaussian innovation variances. [[conditional-vacuum-rigidity-and-the-physical-gap|The physical gap criterion]] instead tests the actual centered Hamiltonian's full reduced resolvent on a dense physical source algebra. A comparison from (CS12) to that criterion must be constructed, with its norm and calibration, rather than inferred from the shared word “response.”

## Closed weighting restores mixed response and contact terms

Let \(W\ge0\) be a nonzero weight in the complete prepared experiment, independent of the variance parameters at fixed configurations, increments and matrices. Assume its integral and the score moments below are finite with local domination. Bounded \(W\) suffices here. A closed trace or a singular endpoint constraint requires its own integrability verification before this result is applied. Set
\[
Z_W(u)=\mathbb E_{\nu_D}W,
\qquad d\nu_W=Z_W^{-1}W\,d\nu_D,
\tag{CS13}
\]
including the parameter-independent conditional observation variables when present. Differentiation gives
\[
\boxed{
\partial_{u_i}\log Z_W=\mathbb E_W S_i,\qquad
\partial_{u_j}\partial_{u_i}\log Z_W
=\operatorname{Cov}_W(S_i,S_j)
-\delta_{ij}\mathbb E_W(S_i+v_i).}
\tag{CS14}
\]
For the common homogeneous path,
\[
\boxed{
\partial_u^2\log Z_W
=\operatorname{Var}_W(S)-\mathbb E_WS-\mathbb E_WB.}
\tag{CS15}
\]
The final two terms are the score's direct derivative, not optional subtractions. At \(W=1\), the curvature is zero even though the Fisher response \(\mathbb E B\) is positive. For a nontrivial weight, the reweighted scores can have mixed covariances. Their Fisher variance alone is therefore not the Hessian of the closed normalization, and neither expression has a prescribed sign as a cosmic restoring potential.

An explicitly variance-dependent interaction or endpoint source adds its direct first and second derivatives to (CS14). Holding such a source fixed after changing its physical definition is not justified. The [[closed-normalization-and-cosmic-response|raw scalar and homogeneous contact analysis]] remains in force; conditional Markov normalization does not select the otherwise admissible closed scalar character.

## The localized common-scale law still returns reciprocal dynamics

The same identities hold for the localized law after replacing \(\zeta_i\) by \(w_i=(\det_Qg_{\xi_i})^{-1/2}\) and \(b_i\) by \(h_i=\mathbb E[w_i\mid\operatorname{pa}(i)]\). The sufficient PD inventory and its polynomially weighted inverse-moment domination justify the required finite-diagram derivatives and moments. These are identities of the limiting law; the statement does not interchange an uncontrolled derivative with a limit.

For a common variance multiplier \(s=e^u\), the substitution \(\xi_i=\sqrt{s}\eta_i\) gives
\[
w_i(\sqrt{s}\eta_i)=s^{-d/2}w_i(\eta_i),\qquad
h_{i,s}(\sqrt{s}\eta_{\operatorname{pa}(i)})
=s^{-d/2}h_{i,1}(\eta_{\operatorname{pa}(i)}).
\tag{CS16}
\]
Hence the whole localized preparation law is exactly the pushforward of its \(s=1\) law under common matrix dilation. All conditional denominators transform with it. The inverse metric scales as \(s^{-1}\), while the positive quadratic moment scales as \(s\). For PD's actual kinetic and same-preparation anchored potential, with the declared paces and strengths fixed,
\[
H_s=s^{-1}K+sV.
\tag{CS17}
\]
This is the conditional-law extension of CN18, including [[shared-preparation-actions-and-the-conditional-return|the repeated-matrix action construction]] with its fixed paces and same-preparation endpoint cost. It does not introduce an independent choice of electric and magnetic coefficients. Its actual vacuum derivative is governed by CN19 with the full reduced resolvent and contact term. Preserving the reciprocal form does not select \(s\), force a positive infinite-volume gap, or identify this auxiliary dilation with cosmic scale.

The next common-source test can now use the correct score: transport the selected homogeneous variation and a complete physical source through the same closed preparation, keeping every parent normalizer. A proposed global/local relation must survive that mixed derivative and the physical return. Positive preparation Fisher information by itself is insufficient, but the score and its normalization are now explicit inputs to that test.
