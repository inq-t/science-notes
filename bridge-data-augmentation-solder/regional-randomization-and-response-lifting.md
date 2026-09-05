# Regional Randomization and Response Lifting

Independent regional readouts can be adjoined without changing the complete response of the original core--boundary relation. On the enlarged carrier, retaining the readouts becomes a deterministic projection, so the relative-leakage theorem applies. Its discarded-core condition must cover observables depending on both the original core and its readout. This makes probabilistic blocking usable without mistaking added readout uncertainty for a physical response.

**Status: [EXACT BOUNDED-OPERATOR IDENTITIES AND CONDITIONAL LIFTING THEOREM]; [EXACT SHARP GAUSSIAN CALIBRATION]; [OPEN] for a continuum Yang--Mills realization.** A probabilistic kernel is auxiliary mathematical integration data, not an assertion of ontic randomness.

## The regional product law

Let \(Y,Z\) be standard Borel core and boundary carriers with joint probability law \(\mu\). Adjoin normalized kernels by
\[
\widetilde\mu(dy,dx,dz,dw)
=\mu(dy,dz)\,q(dx\mid y)\,r(dw\mid z).
\tag{RR1}
\]
The kernels may be deterministic. The load-bearing condition is the displayed regional factorization: the core readout depends only on \(Y\), the boundary readout only on \(Z\), and the two are conditionally independent given the original pair.

The original law is unchanged after integrating out \(X,W\). This alone would not establish preservation of the complete enlarged response; that conclusion also uses regional independence.

## The extra observable directions have response one

Use centered marginal \(L^2\) carriers throughout. Write
\[
Kf(Z)=\mathbb E[f(Y)\mid Z],\qquad B=I-K^*K,
\]
and let \(J_Y:\mathcal H_Y\to\mathcal H_{Y,X}\), \(J_Z:\mathcal H_Z\to\mathcal H_{Z,W}\) be pullback isometries. Their adjoints average the private readouts conditional on the original regional variable.

The enlarged predictor factors exactly:
\[
\widetilde K=J_ZKJ_Y^*.
\tag{RR2}
\]
Indeed, conditioning on \(Z,W\) supplies no extra information about \(Y,X\) beyond \(Z\), while \(X\mid Y,Z=q(\cdot\mid Y)\). Therefore
\[
\boxed{\widetilde B
=J_YBJ_Y^*+(I-J_YJ_Y^*).}
\tag{RR3}
\]
On the orthogonal decomposition
\[
\mathcal H_{Y,X}
=J_Y\mathcal H_Y\oplus\ker J_Y^*,
\]
the response is \(B\oplus I\). Added core-noise directions have maximal conditional-variance response; they do not improve the original soft directions.

Since \(J_Y^*J_Y=J_Z^*J_Z=I\),
\[
\|\widetilde K\|\le\|K\|,\qquad
K=J_Z^*\widetilde KJ_Y,
\]
so equality holds. Define the normalized complete floor by \(\kappa_\mu:=1-\|K\|^2\), taking the zero-carrier operator norm to be zero. Equivalently, optimize lower certificates only within \([0,1]\); this also covers trivial centered carriers. Then the floors agree:
\[
\boxed{\kappa_{\widetilde\mu}=\kappa_\mu.}
\tag{RR4}
\]
These are bounded-operator identities in arbitrary Hilbert dimension. No discrete spectrum, conditional density or differential calculus is needed.

## Deterministic retention on the enlarged law

Retain \(X,W\) from the enlarged core \((Y,X)\) and boundary \((Z,W)\). Let \(B_c\) be the actual \(X\)--\(W\) response. For retained \(f(X)\), define
\[
A[f]=\mathbb E\operatorname{Var}(f(X)\mid Z),\qquad
\mathcal L[f]=\mathbb E\operatorname{Var}(\mathbb E[f(X)\mid Z]\mid W).
\tag{RR5}
\]
The exact decomposition is \(\langle f,B_cf\rangle=A[f]+\mathcal L[f]\). Suppose \(B_c\ge\kappa_c I\), \(\mathcal L[f]\le r_{\partial}A[f]\) for every retained observable, and
\[
\boxed{
\mathbb E\operatorname{Var}(F(Y,X)\mid X,Z)
\ge b\,\mathbb E\operatorname{Var}(F(Y,X)\mid X)}
\tag{RR6}
\]
for every \(F\in L^2(\mu_{Y,X})\), with \(0<b\le1\), \(0<\kappa_c\le1\), and \(0\le r_{\partial}<\infty\). The cap on \(b\) matters when the discarded core is trivial: for \(X=Y\), (RR6) is vacuous and cannot by itself bound \(b\). Then [[relative-boundary-leakage|relative lifting]] on the enlarged carrier and (RR4) give
\[
\boxed{\kappa_\mu\ge
\frac{b\,\kappa_c}{1+r_{\partial}}.}
\tag{RR7}
\]
A sufficient form of (RR6) is a uniform complete bridge floor \(b\) for the actual pair \((Y,Z)\mid X=x\), almost everywhere in \(x\). With the usual measurable disintegration and a countable dense determining class, these formulations are equivalent.

For a differential certificate of \(\mathcal L\), the context is now the posterior \(Z\mid W=w\). It is not a level set of a deterministic map \(Z\mapsto W\). Its derivatives vary \(z\) at fixed \(w\), and must use the actual posterior measure and metric. The family \(X\mid Z=z,W=w\) equals \(X\mid Z=z\) by (RR1). The domain and normalized-score hypotheses in [[conditional-fisher-coercivity/inq|conditional Fisher coercivity]] apply to this family. A global estimate \(\operatorname{Var}_Z(\mathbb E[f(X)\mid Z])\le r_{\partial}A[f]\) is also sufficient, since conditioning on \(W\) cannot increase that variance.

## The new discarded-core quantifier cannot be omitted

When \(X=q(Y)\) is deterministic, every observable of \((Y,X)\) is already an observable of \(Y\). With a probabilistic readout this is false. Testing (RR6) only for \(F=f(Y)\) is insufficient.

For an exact finite counterexample, let \(Y\) be uniform on \(\{a,b,c\}\). Given \(Y=a\), set \(Z=0\); given \(Y=b\), set \(Z=1\); at \(c\), let \(Z\) be fair. Independently conditional on \(Y\), choose
\[
\Pr(X=0\mid a)=\Pr(X=0\mid b)=\tfrac12,\qquad
\Pr(X=0\mid c)=0.
\tag{RR8}
\]
For \(f(a)=u,f(b)=v,f(c)=t\), the integrated numerator and denominator tested only on \(f(Y)\) are
\[
N=\frac{|u-t|^2+|v-t|^2}{12},\qquad
D=N+\frac{|u-v|^2}{8},\qquad N\ge D/4.
\tag{RR9}
\]
But
\[
F(Y,X)=\mathbf1_{\{X=0\}}
(\mathbf1_{\{Y=a\}}-\mathbf1_{\{Y=b\}})
\]
has zero conditional variance given \(X,Z\) and positive variance given \(X\). Thus the complete coefficient in (RR6) is zero. This counterexample concerns the abstract kernel theorem; it is not an example satisfying smooth common-positive-density Fisher hypotheses.

## A floor-one readout must retain the predictive classes

Suppose the regional kernel has a common sigma-finite reference,
\[
q(dx\mid y)=q(x,y)\lambda(dx),\qquad
0<q(x,y)<\infty
\quad(\mu_Y\otimes\lambda)\text{-almost everywhere}.
\tag{RR6a}
\]
Then the actual posterior \(\mu_{Y\mid X=x}\) is equivalent to \(\mu_Y\) for almost every \(x\). If (RR6) holds with \(b=1\), total variance forces \(Y\perp Z\mid X\). Regionality also gives
\(\mathcal L(Z\mid Y,X)=\mathcal L(Z\mid Y)\).
Posterior equivalence therefore makes this last conditional law constant on the original \(Y\)-support: \(Y,Z\) were independent already.

Thus a genuinely dependent original pair cannot acquire exact discarded-core coefficient one from a common-positive readout. Deterministic [[predictive-sufficient-interfaces|predictive statistics]], or readouts retaining such a statistic noiselessly, escape the hypothesis because their supports separate predictive classes. No uniform lower density bound is needed for this exact endpoint statement.

A quantitative comparison is available for bounded likelihood tilts. If
\(\mu'=w(Y)\mu/\mathbb E_\mu w\), with
\(A=\operatorname{osc}\log w<\infty\), then
\[
\boxed{
e^{-A}\kappa_\mu\le\kappa_{\mu'}
\le\min\{1,e^A\kappa_\mu\}.}
\tag{RR6b}
\]
Use the variational numerator
\(\inf_g\mathbb E|f(Y)-g(Z)|^2\) and denominator
\(\inf_c\mathbb E|f(Y)-c|^2\). Each changes between the same minimum and maximum density factors, whose ratio is \(e^A\); no squared ratio is needed.

Apply this to \(w(y)=q(x,y)\) for each actual posterior. Finite \(A_x\) preserves an exactly zero original floor, while a uniform \(A_x\) is needed to control a sequence of positive floors approaching zero. For \(m\) compact normalized gauge readout factors of strength \(\kappa\), the crude bound is \(A_x\le4\kappa m\). It is not volume-uniform merely because each factor is strictly positive.

The alternative [[predictive-sufficient-interfaces|discarded-prediction norm]] can sometimes avoid the essential conditional coefficient altogether. It has an additive loss budget and must be proved on the entire original or regional-augmented carrier.

## Independent Gaussian readout costs cancel exactly

Let \(Y,Z\) be standard jointly Gaussian with covariance \(t\), \(|t|<1\). Set
\[
d=1-t^2,\qquad
X=Y+\varepsilon_x,\quad W=Z+\varepsilon_w,\qquad
u=\operatorname{Var}\varepsilon_x,\quad v=\operatorname{Var}\varepsilon_w,
\]
with \(\varepsilon_x\sim N(0,u)\), \(\varepsilon_w\sim N(0,v)\), mutually independent and independent of \((Y,Z)\). Write \(A_0=1+u\), \(C_0=1+v\). For positive \(u,v\), Gaussian conditional covariance and the complete Hermite spectrum give
\[
\kappa_\mu=d,\qquad
\kappa_c=1-\frac{t^2}{A_0C_0},\qquad
b=\frac{dA_0}{u+d},\qquad
r_{\partial}=\frac{t^2v}{C_0(u+d)}.
\tag{RR10}
\]
The relative coefficient is an all-observable optimum, not just a linear test. Put \(\alpha=t^2/A_0\), \(q_0=1/C_0\). The degree-\(n\) Hermite quotient is
\[
r_n=\frac{\alpha^n(1-q_0^n)}{1-\alpha^n}.
\]
For \(0<\alpha,q_0<1\),
\[
\frac{r_n}{r_1}
=\alpha^{n-1}
\frac{\sum_{k<n}q_0^k}{\sum_{k<n}\alpha^k}\le1.
\]
Thus the first Hermite saturates relative leakage. Direct substitution yields
\[
\boxed{\frac{b\,\kappa_c}{1+r_{\partial}}=d.}
\tag{RR11}
\]
The formulas extend to zero readout noise by the deterministic limit, taking \(b=1\) when \(X=Y\). Independence \(t=0\) gives \(r_{\partial}=0\).

When core readout noise tends to infinity, the coarse floor tends to one and relative leakage tends to zero, but \(b\) tends to the original floor \(d\). The original difficulty has moved into discarded-core control. Independent erasure of both regions has the same exact structure for any original law: \(\kappa_c=1\), \(r_{\partial}=0\), and the optimal \(b\) is \(\kappa_\mu\).

## Shared auxiliary information changes the full carrier

Take independent original signs \(Y,Z\), but adjoin the same independent sign as \(X=W=\xi\). Each readout marginal is normalized; the joint readouts do not satisfy (RR1). The original floor is one, while the enlarged sides share the nonconstant observable \(\xi\), so their complete floor is zero.

Likewise \(X=Z\) introduces a boundary observable into the enlarged core and violates regionality. Shared independent noise need not alter prediction of the restricted original sources from \(Z,W\); the failure is already in the enlarged complete carrier. Do not conflate that failure with an original-source dependence claim.

## A genuine probabilistic tower

The allowed finite-depth law is
\[
\mu_0(dY_0,dZ_0)
\prod_{j<J}q_j(dY_{j+1}\mid Y_j)\,
r_j(dZ_{j+1}\mid Z_j).
\tag{RR12}
\]
Each \(\mu_j\) is the actual pair marginal, generally an integrated effective law. Applying (RR7) at every level gives
\[
\boxed{\kappa_0\ge
\kappa_J\prod_{j<J}\frac{b_j}{1+r_{\partial,j}}.}
\tag{RR13}
\]
The finite logarithmic budget in [[relative-boundary-leakage|the relative theorem]] therefore extends to these regional Markov towers.

For nested-algebra arguments on the full history law, use the regional suffix algebras \(\sigma(Y_j,\ldots,Y_J)\) and \(\sigma(Z_j,\ldots,Z_J)\), as in [[rg-covariance-residue/normalized-gauge-kernels-and-markov-residues|normalized Markov residues]]. Each suffix pair is a private regional augmentation of its current pair and has the same optimal floor. The single-time algebras need not be nested. History dependence requires an explicit regional Markov-state enlargement; cross-region or shared noise requires a different comparison theorem.

[[rg-covariance-residue/regional-gauge-readouts-and-conditional-lifting|Regional gauge readouts]] realize the one-step hypotheses on product Haar in a strong-coupling regime. Neither private augmentation nor the tower identity proves that its conditional loss budget stays finite through the Yang--Mills continuum limit.

[[receipts/regional_randomization_receipt.py|The finite receipt]] checks the exact enlargement, complete-carrier quantifier, Gaussian cancellation and Markov iteration.
