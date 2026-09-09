# Two-Endpoint Recovery and a Rare-State Escape

A three-state reversible positive transfer can erase every centered one-endpoint prediction while its two endpoints almost determine a normalized rare midpoint source. This remains true after every transition probability and every transfer eigenvalue are made strictly positive. The two-endpoint recovery gap then closes although the logarithmic transfer gap diverges. The construction separates a sufficient symmetric recovery certificate from a necessary condition for a positive finite-step transfer gap; it is not a continuous-time Markov or Yang–Mills counterexample.

## The two experiments use one stationary path law

Let \(P\) be a reversible Markov matrix on a finite probability space \((\mathcal S,\pi)\), positive as an operator on \(L^2(\pi)\). Let \(\Pi f=\pi(f)1\). In its stationary three-slice law, the midpoint \(Y\) and endpoints \(X,Z\) have joint probability
\[
\mathbb P(X=i,Y=j,Z=k)=\pi_jP_{ji}P_{jk}.
\tag{RE1}
\]
Thus the endpoints are independent conditional on the midpoint, and all conditional normalizers below come from this same law. Set
\[
Kf=\mathbb E[f(Y)\mid X,Z],\qquad
R^{(2)}=I-K^*K,
\qquad
\langle f,R^{(2)}f\rangle
=\mathbb E\operatorname{Var}(f(Y)\mid X,Z).
\tag{RE2}
\]
One endpoint instead leaves the exact residue
\[
\mathbb E\operatorname{Var}(f(Y)\mid X)
=\langle f,(I-P^2)f\rangle.
\tag{RE3}
\]
These are different conditional expectations, even though the same chronological kernel determines both.

[[three-block-bridge-factorization/inq|Three-block bridge factorization, TB17a–c]] already gives a growing high-girth graph construction in which one-ended transfer contraction tends to zero while the bridge floor closes. [[bridge-score-fusion-geometry/two-boundary-multiplication-and-predictive-tails|Two-boundary multiplication]] identifies the relevant extra structure: products of separately propagated endpoint functions, weighted in their actual joint law. The following example exhibits that distinction on three fixed states, without a graph-existence input.

## An exact rank-one transfer

Fix exponents
\[
\frac12<\beta<1,\qquad 0<\gamma<\frac12,
\qquad
q=p^\beta,\quad o=1-p-q,\quad
t=(p/q)^\gamma,
\tag{RE4}
\]
and let \(p\downarrow0\). The stationary law on
\(\mathcal S=\{R,S,O\}\) is \(\pi=(p,q,o)\). All statements below hold for sufficiently small positive \(p\), so \(o>0\). Define
\[
v_R=\sqrt{t/p},\qquad
v_S=\frac{o-t}{q}\sqrt{p/t},\qquad
v_O=-\sqrt{p/t}.
\tag{RE5}
\]
There is no fitted normalization: direct substitution gives
\[
pv_R+qv_S+ov_O=0,
\qquad
\alpha:=\|v\|_{L^2(\pi)}^2
=t+\frac{p(o-t)^2}{qt}+\frac{op}{t}.
\tag{RE6}
\]
Put \(u=v/\sqrt\alpha\) and use the actual rank-one operator
\[
\boxed{
P_{ij}=\pi_j(1+v_iv_j),\qquad
P=\Pi+\alpha\,u\otimes u,
\quad (u\otimes u)f=u\langle u,f\rangle_\pi.}
\tag{RE7}
\]
The mean-zero identity makes every row sum one. Detailed balance follows from
\(\pi_iP_{ij}=\pi_i\pi_j(1+v_iv_j)\). Since \(u\perp1\) and \(\|u\|=1\), its Hilbert eigenvalues are exactly \(1,\alpha,0\).

All entries are nonnegative. The only negative products involve \(O\). In fact \(v_Rv_O=-1\), and
\(-v_Sv_O=p(o-t)/(qt)\to0\). Eventually \(t<o\) and \(p(o-t)/(qt)<1\), which proves the assertion. In particular, the relevant entries are exactly
\[
\begin{aligned}
P_{RR}&=p+t,& P_{RS}&=1-p-t,& P_{RO}&=0,\\
P_{SR}&=\frac pq(1-p-t),&
P_{SS}&=q+\frac{p(o-t)^2}{qt},&
P_{SO}&=o\left[1-\frac{p(o-t)}{qt}\right],\\
P_{OR}&=0,&
P_{OS}&=q-\frac{p(o-t)}t,&
P_{OO}&=o(1+p/t).
\end{aligned}
\tag{RE8}
\]
Moreover
\[
\frac\alpha t
=1+\frac{p(o-t)^2}{qt^2}+\frac{op}{t^2}
\longrightarrow1.
\tag{RE9}
\]
Indeed \((p/q)/t^2=(p/q)^{1-2\gamma}\to0\), and the last term is smaller. Hence \(0<\alpha<1\) eventually and
\[
\|P-\Pi\|=\alpha\longrightarrow0,
\qquad \operatorname{gap}(I-P)=1-\alpha\longrightarrow1.
\tag{RE10}
\]
The one-step kernel has increasingly strong centered attenuation in the exact \(L^2(\pi)\) norm. The rare and less-rare states nevertheless have very different conditional roles: a midpoint \(R\) sends each endpoint to \(S\) with probability tending to one, while \(P_{SS}\sim p/(qt)\to0\).

## Two endpoints almost certify the rare midpoint

Write
\[
d_R=P_{RS}=1-p-t,\quad
d_S=P_{SS}=q+\frac{p(o-t)^2}{qt},\quad
d_O=P_{OS}=q-\frac{p(o-t)}t.
\]
The actual probability of the endpoint event \(A=\{X=S,Z=S\}\) and its exact midpoint posterior are
\[
D_p:=\mathbb P(A)=pd_R^2+qd_S^2+od_O^2,
\qquad
\mathbb P(Y=R\mid A)=\frac{pd_R^2}{D_p}.
\tag{RE11}
\]
Both normalizations matter. The false-positive endpoint weight obeys
\[
qd_S^2+od_O^2
\le 2q^3+\frac{2p^2}{qt^2}+q^2,
\tag{RE12}
\]
because \(0<o-t<1\) and \(0\le d_O\le q\) eventually. Dividing by \(p\), the right side tends to zero: \(q^2/p=p^{2\beta-1}\to0\) and \(p/(qt^2)\to0\). Therefore \(D_p/p\to1\) and the posterior in RE11 tends to one. The two endpoints identify a rare midpoint with probability high enough relative to that midpoint's own mass.

Use the complete centered unit source
\[
f_p(Y)=\frac{1_{\{Y=R\}}-p}{\sqrt{p(1-p)}}.
\tag{RE13}
\]
Conditional expectation is the best square-integrable predictor. The endpoint estimator
\(\widehat f_p=(1_A-p)/\sqrt{p(1-p)}\) therefore gives
\[
\begin{aligned}
\langle f_p,R^{(2)}f_p\rangle
&\le\mathbb E|f_p(Y)-\widehat f_p(X,Z)|^2\\
&=\frac{p(1-d_R^2)+qd_S^2+od_O^2}{p(1-p)}\\
&\le\frac{2(p+t)+2q^3/p+2p/(qt^2)+q^2/p}{1-p}
\longrightarrow0.
\end{aligned}
\tag{RE14}
\]
Here \(1-d_R^2=2(p+t)-(p+t)^2\le2(p+t)\). The estimate is an exact source test under RE1, not an inference from the unweighted pair of endpoint rows.

In contrast, for this same source, RE3 and RE10 give
\[
\mathbb E\operatorname{Var}(f_p(Y)\mid X)
\ge1-\alpha^2\longrightarrow1.
\tag{RE15}
\]
Each endpoint separately predicts asymptotically none of a centered unit distinction, while their product event predicts essentially all of this particular distinction. The \(L^\infty\) norm of \(f_p\) diverges like \(p^{-1/2}\); estimates on an individually bounded source without its variance normalization would miss this obstruction.

## Strict positivity and a Hamiltonian logarithm do not remove the escape

The zero transition entries and zero Hilbert eigenvalue are dispensable. Let \(\varepsilon=p^2\), and define
\[
\boxed{
\widetilde P=(1-2\varepsilon)P+\varepsilon\Pi+\varepsilon I.}
\tag{RE16}
\]
For small \(p\), this is a reversible Markov matrix with every transition entry strictly positive. Its Hilbert eigenvalues are
\[
1,\qquad
\lambda=(1-2\varepsilon)\alpha+\varepsilon,\qquad
\varepsilon,
\quad 0<\varepsilon<\lambda<1.
\tag{RE17}
\]
Thus it is injective and positive definite, \(\|\widetilde P-\Pi\|=\lambda\to0\), and the positive finite-step transfer Hamiltonian
\[
\widetilde H=-\log\widetilde P
\quad\text{has}\quad
\ker\widetilde H=\mathbb C1,
\qquad
\operatorname{gap}\widetilde H=-\log\lambda\longrightarrow\infty
\tag{RE18}
\]
when the displayed step has fixed unit thickness.

Use RE1 with \(\widetilde P\), and let \(\widetilde R^{(2)}\) be its actual bridge residue. Couple each endpoint draw with its old \(P\)-draw: with probability \(1-2\varepsilon\) keep that draw, and otherwise use the \(\Pi\)- or \(I\)-branch of RE16. The probability that either endpoint changes is at most \(4\varepsilon\). The indicator classification loss in RE14 lies between zero and one, so
\[
\boxed{
\langle f_p,\widetilde R^{(2)}f_p\rangle
\le\frac{p(1-d_R^2)+qd_S^2+od_O^2+4\varepsilon}{p(1-p)}
\longrightarrow0.}
\tag{RE19}
\]
Since \(\varepsilon=p^2\), the added normalized error is \(4p/(1-p)\). No change of invariant law or source normalization is hidden in this perturbation.

For every finite \(p\), all three middle states have positive probability conditional on every endpoint pair under \(\widetilde P\). Zero conditional variance consequently forces a middle function to be constant. Thus
\[
\ker\widetilde R^{(2)}=\mathbb C1,
\qquad
\operatorname{gap}\widetilde R^{(2)}
\le\langle f_p,\widetilde R^{(2)}f_p\rangle\longrightarrow0.
\tag{RE20}
\]
This is a closing gap above the whole invariant space, not just a test orthogonal to an unexamined constant vector.

## What the discriminator does and does not decide

For any proposed two-ended repair
\(\mathcal B_p\delta_p=I-\mathcal E_p\) on the centered carrier, where
\(\|\delta_pf\|^2=\langle f,\widetilde R^{(2)}f\rangle\), the bound
\(\|\mathcal E_p\|\le\rho<1\) would require
\[
\|\mathcal B_p\|
\ge\frac{1-\rho}{\|\delta_pf_p\|}
\longrightarrow\infty.
\tag{RE21}
\]
Hence a uniform bounded symmetric repair is a stronger property than a uniform gap of a positive finite-step chronological transfer. Its failure need not signal low physical energy. It may instead signal extra predictive power from the endpoint pair and a rare-source normalization. The exact one-ended residue \(I-\widetilde P^2\) already has a floor tending to one, as does the appropriately supported opposed-cut angle in [[two-slice-innovation-geometry/past-future-angle-and-the-transfer-gap|the past–future theorem]].

The continuous-time distinction is substantive. Although RE18 defines a Hamiltonian logarithm, it does not make all fractional powers \(\widetilde P^s\) Markov. In fact this example is not continuously Markov-embeddable. Its three eigenvalues are distinct, real and positive. Any real generator whose exponential is \(\widetilde P\) commutes with \(\widetilde P\), so it acts by a real scalar on each one-dimensional real eigenspace. It must therefore equal \(\log\widetilde P\), even without assuming reversibility of that generator. Put \(A=-\log\lambda\) and \(B=-\log\varepsilon\). Since \(u_Ru_O=-1/\alpha\), the \((R,O)\) entry of this only possible generator is
\[
(\log\widetilde P)_{RO}
=o\left[B-\frac{B-A}{\alpha}\right]<0
\tag{RE22}
\]
eventually. Indeed \(A/B\to\gamma(1-\beta)/2<1\) while \(\alpha\to0\). A Markov generator must have nonnegative off-diagonal entries. The construction therefore disproves an implication from positive reversible discrete transfer and its spectral gap at the declared one-step half-width; it does not establish the same failure at all larger slab widths or under continuous Markov-semigroup hypotheses. [[gaussian-bridge-gap-calibration/two-boundary-half-smoothing|The Gaussian and bit-flip half-smoothing theorem]] gives a positive control where that stronger structure does support a uniform bridge comparison.

For the reflected determinant proposal, this is a choice of proof burden. A two-ended repair may still follow from its particular boundary multiplication and source geometry, but it would establish more than the finite transfer-gap predicate alone. A route using oriented chronological prediction or the supported past–future angle targets the transfer attenuation directly. Neither route yet supplies the uniform non-Abelian estimates, physical continuum construction or Yang–Mills mass gap.
