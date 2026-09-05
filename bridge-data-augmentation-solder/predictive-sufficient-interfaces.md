# Predictive Sufficient Interfaces

The part of a region that matters for its response to another region is its complete conditional prediction law, not a chosen list of field averages. Exact sufficient statistics concentrate the entire nontrivial response on this relational interface; discarded observable directions then have response one. Approximate sufficiency instead needs an operator-norm bound on discarded prediction. Small average information loss alone is not that bound.

**Status: [EXACT MEASURE-THEORETIC FACTORIZATION AND BOUNDED-OPERATOR COMPARISONS]; [OPEN] for a tractable, physically separated Yang--Mills interface with a uniform continuum floor.** These are consequences of conditional expectation and sufficiency, with no novelty claim. A statistic is relative to the specified joint law.

## Let the conditional law select the statistic

Let \((Y,Z)\) have a joint probability law on standard Borel spaces. On centered marginal \(L^2\) carriers put
\[
Kf=\mathbb E[f(Y)\mid Z],\qquad B=I-K^*K,\qquad
\kappa_\mu=1-\|K\|^2.
\tag{PS1}
\]
The zero-carrier norm is zero, so normalized floors stay in \([0,1]\).

Regular conditional probabilities define probability-valued statistics
\[
T(y)=\mathcal L(Z\mid Y=y),\qquad
S(z)=\mathcal L(Y\mid Z=z).
\tag{PS2}
\]
Their measurable spaces use the evaluation sigma algebra. Versions differing on null sets give the same completed observable subalgebras. In particular,
\[
\sigma(T(Y))
=\sigma\{\mathbb E[h(Z)\mid Y]:h\text{ bounded measurable}\}
\tag{PS3}
\]
after completion; a countable determining class suffices.

The statistic \(X=T(Y)\) is minimal in the following precise sense: if a deterministic readout \(X'\) satisfies \(Y\perp Z\mid X'\), every conditional probability in (PS2) is \(X'\)-measurable. Hence \(\sigma(X)\subseteq\sigma(X')\) modulo null sets. The analogous statement holds on the boundary side.

This supplies a canonical measurable object, not a canonical finite-dimensional manifold, local field, metric, or computational compression. It may encode the whole original configuration. The [[gaussian-bridge-gap-calibration/predictive-rank-and-physical-separation|Gaussian calculation]] distinguishes smooth coordinate rank from Hilbert-space rank and from arbitrary measurable encodings.

## Exact sufficiency removes both lifting losses

More generally, choose deterministic \(X=T(Y)\), \(W=S(Z)\) satisfying
\[
Y\perp Z\mid X,\qquad X\perp Z\mid W.
\tag{PS4}
\]
The statistics (PS2) satisfy these conditions. Let \(J_X,J_W\) be their pullback isometries and let \(K_c\) predict \(X\)-observables from \(W\). Then
\[
\boxed{K=J_WK_cJ_X^*.}
\tag{PS5}
\]
The first condition makes every prediction of \(f(Y)\) depend on its conditional mean given \(X\); the second makes that prediction a function of \(W\).

Taking adjoints proves
\[
\boxed{
B=J_XB_cJ_X^*+(I-J_XJ_X^*),\qquad
B\simeq B_c\oplus I,\qquad \kappa_\mu=\kappa_c.}
\tag{PS6}
\]
The identity acts on all innovations orthogonal to functions of \(X\), including mixed retained/discarded observables. It is not merely a statement about selected coordinate fluctuations.

Equivalently, the joint law can be recovered by private regional conditional kernels:
\[
\mu(dy,dz)=\int\mu_{X,W}(dx,dw)\,
\mu_Y(dy\mid x)\,\mu_Z(dz\mid w).
\tag{PS7}
\]
This is [[regional-randomization-and-response-lifting|regional augmentation]] in reverse. In [[relative-boundary-leakage|relative lifting]], exact sufficiency gives \(b=1\) and \(r_\partial=0\).

The established statistical notion is the parameter-independent conditional fiber law behind the Fisher--Neyman factorization; [[library/information-geometry-and-sufficient-statistics/inq|Ay--Jost--Lê--Schwachhöfer]] give its information-geometric formulation. Here the complete opposite conditional law is retained, not merely a finite list of parameter scores. Consequently (PS6) does not contradict [[conditional-fisher-coercivity/coarse-graining-and-moving-context|the warning about Fisher preservation alone]], nor does it recover an independently chosen dynamics on omitted variables.

## Approximate sufficiency has a different coefficient

For a general deterministic core readout, put \(P=J_XJ_X^*\), \(Q=I-P\), and define its discarded prediction norm
\[
\boxed{\delta:=\|KQ\|^2.}
\tag{PS8}
\]
Exact core sufficiency is equivalent to \(\delta=0\). This norm measures what the boundary can predict about innovations omitted by \(X\), in the actual original \(L^2\) norms. It is not an entropy, a derivative norm or an essential supremum of conditional correlations.

[[bridge-score-fusion-geometry/two-boundary-multiplication-and-predictive-tails|Two-boundary multiplication]] gives concrete estimates for this norm on a stationary midpoint bridge. Exact one-ended sufficiency of an observable algebra survives two-ended conditioning, but approximate bounds must control products and the actual endpoint density. A retained linear spectral span is a different kind of object; the operator argument in (PS9) still applies to an arbitrary orthogonal splitting, whereas (PS10)'s coarse-statistic interpretation needs a conditional expectation.

Suppose the retained fine response has floor \(a>0\):
\[
J_X^*BJ_X\ge aI,\qquad 0<a\le1.
\]
Since
\[
KK^*=KPK^*+KQK^*,\qquad
\|KP\|^2\le1-a,
\]
one obtains
\[
\boxed{\kappa_\mu\ge \max\{0,a-\delta\}.}
\tag{PS9}
\]
In particular, relative boundary control supplies
\[
\boxed{\kappa_\mu\ge
\max\left\{0,\frac{\kappa_c}{1+r_\partial}-\delta\right\}.}
\tag{PS10}
\]
This is an alternative to the route through the full-space operator inequality \(B\ge bQ\). The conditional-fiber hypothesis used to prove that inequality is stronger still. The new route pays an additive cost and requires \(\delta<a\); it is an alternative to the multiplicative \(b\)-theorem, not an automatic improvement.

For a consistent tower, write \(p_j=(1+r_j)^{-1}\) and suppose the corresponding \(\delta_j\) are bounded on each actual level. Iteration yields
\[
\kappa_0\ge
\left(\prod_{j<J}p_j\right)\kappa_J
-\sum_{j<J}\delta_j\prod_{i<j}p_i.
\tag{PS11}
\]
For example, \(\sum_j\log(1+r_j)\le M\), \(\sum_j\delta_j\le D<e^{-M}\kappa_T\), and \(\kappa_J\ge\kappa_T>0\) suffice. Unlike the purely multiplicative budget, a positive margin over the accumulated additive loss is required.

If \(\mu\) has density \(k(y,z)\) relative to \(\mu_Y\otimes\mu_Z\), and the following residual is square-integrable, a concrete sufficient estimate is
\[
d(y,z)=k(y,z)-\mathbb E_{\mu_Y}[k(Y,z)\mid X=T(y)],
\qquad
\delta\le\int|d(y,z)|^2\,d\mu_Y\,d\mu_Z.
\tag{PS12}
\]
The conditional expectation in (PS12) uses the product-reference \(Y\)-measure with \(z\) fixed, not the correlated joint law. The kernel \(d\) represents \(KQ\), and the bound is its Hilbert--Schmidt bound. Only this residual must be square-integrable. A sum of many kernel components can introduce a dimension penalty; controlling the operator norm directly is preferable. No density is assumed in (PS1)--(PS11).

There is a qualified entropy certificate. If \(0\le k\le M<\infty\) uniformly, then \(k_c:=k-d\le M\). Strong convexity of \(s\log s\) on \([0,M]\) gives
\[
\boxed{\delta\le\int|d|^2\,d\mu_Y\,d\mu_Z
\le2M I(Y;Z\mid X).}
\tag{PS12a}
\]
Indeed, the integrated Bregman divergence
\(k\log(k/k_c)-k+k_c\) is \(I(Y;Z\mid X)\); pointwise it dominates \((k-k_c)^2/(2M)\). Thus (PS9) gives a positive floor when \(2M I(Y;Z\mid X)<a\). The density envelope is substantive. Finite-volume boundedness does not imply a bound uniform in volume and regulator, and a dimension penalty can hide inside \(M\).

## Rare conditional dependence can defeat the stronger certificate

Let \(S\sim\mathrm{Bernoulli}(\varepsilon)\), and conditional fair signs \(A,B\) have laws
\[
p(a,b\mid S=0)=\tfrac14,\qquad
p(a,b\mid S=1)=\tfrac14(1+\rho ab).
\]
Take \(Y=(S,A)\), \(X=S\), \(Z=B\), with \(0<\varepsilon<1\), \(0<\rho<1\). All joint atoms are positive. Then
\[
b_{\rm conditional}=1-\rho^2,\qquad
\delta=\varepsilon\rho^2,\qquad
\kappa_\mu=1-\varepsilon\rho^2.
\tag{PS13}
\]
The retained \(X\) is independent of \(Z\), so \(a=\kappa_c=1\) and \(r_\partial=0\). Equation (PS9) is exact. The essential conditional coefficient can approach zero while the original response remains near one. Thus trying to force every rare posterior to have the same strong bound can be an unnecessary obstruction in this sufficient proof strategy.

The conditional mutual information is
\[
I(Y;Z\mid X)=\varepsilon j(\rho),\quad
j(\rho)=\tfrac12[(1+\rho)\log(1+\rho)+(1-\rho)\log(1-\rho)].
\]
Its smallness does not explain (PS13); the direct operator norm does.

Nor does small mutual information guarantee a full gap. For binary variables with common rare marginal \(\Pr(1)=\varepsilon<1/2\), let
\[
\mu=
\begin{pmatrix}
1-\varepsilon-\eta&\eta\\
\eta&\varepsilon-\eta
\end{pmatrix},
\qquad \eta=\varepsilon^2(1-\varepsilon).
\tag{PS14}
\]
Every entry is positive. Yet \(I(Y;Z)\le h(\varepsilon)\to0\), while correlation is \(1-\varepsilon\) and
\[
\kappa_\mu=2\varepsilon-\varepsilon^2\longrightarrow0.
\]
The variance-one rare-atom observable amplifies the weakly weighted sector. Entropy remains useful, but an averaged entropy bound cannot replace the complete \(L^2\) estimate.

## The physical separation still has to survive

[[rg-covariance-residue/exact-wilson-interface-statistics|Wilson cross-plaquette interfaces]] realize (PS6) at arbitrary finite coupling. Their actual induced law retains the integrated bulk interactions; no positive uniform gap follows from exact factorization.

Moreover, [[gaussian-bridge-gap-calibration/predictive-rank-and-physical-separation|the Gaussian slab test]] shows that an all-interior bridge can lose its floor under refinement even when the fixed-distance midpoint bridge remains gapped. Exact compression preserves the carrier it is given, including a carrier that is unsuitable for the intended physical comparison.

The next construction must therefore preserve the specified midpoint and boundary separation while controlling either the induced complete interface response or the norm in (PS8). Naming a sufficient statistic does not supply those estimates. A state on noncommuting algebras is not automatically a joint probability law of the kind used here; a quantum sufficiency extension needs its own carrier and conditional maps.

[[receipts/predictive_interface_receipt.py|The receipt]] checks factorization, discarded-prediction lifting, rare-sector controls, nonlinear finite interfaces and Gaussian carrier distinctions.
