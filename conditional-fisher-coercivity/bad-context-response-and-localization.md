# Bad-Context Response and the Cost of Localization

A rare conditioning context can support a unit-normalized fluctuation. Its probability alone therefore cannot control its contribution to a spectral estimate. When uniform fiber coercivity fails, a usable replacement must control the cost of concentrating a fluctuation on the unfavorable contexts, together with the retained mean. Total variance gives an exact conditional theorem specifying that replacement.

**Status: [EXACT CONDITIONAL THEOREM] on a declared joint probability and closed-form carrier; [OPEN] for uniform Wilson constants. Probability weights specify a state, not a stochastic ontology.**

## The operator acts on joint fluctuations

Let
\[
\mu(dR,dU)=\nu(dR)q_R(dU),\qquad
\mathcal H=L^2(\mu).
\tag{BC1}
\]
Write \(P f=\mathbb E[f\mid R]\), regarded as an orthogonal projection on the same joint carrier. For a measurable set \(B\) of retained contexts, multiplication by \(\mathbf1_B(R)\) commutes with \(P\). Consequently
\[
\Pi_B=\mathbf1_B(I-P),\qquad
\Pi_B^*=\Pi_B=\Pi_B^2,
\qquad
\|\Pi_Bf\|^2
=\int_B\operatorname{Var}_{q_R}f\,d\nu(R).
\tag{BC2}
\]
Whenever its range is nonzero, \(\|\Pi_B\|=1\), however small \(\nu(B)\) is. Thus a probability-small set is not an operator-small sector.

For an explicit product law, take a nonzero \(\chi(R)\) supported in \(B\) and a centered hidden function \(g(U)\). Then \(f=\chi g\) has \(Pf=0\) and
\[
\|\Pi_Bf\|^2=\operatorname{Var}_\mu f.
\tag{BC3}
\]
For a smooth product with an open \(B\), \(\chi\) can be a smooth compactly supported bump. Its retained gradient need not be small. That gradient is exactly one possible price of concentration which a joint estimate must retain.

## A sufficient joint-form bound

Let \(\mathcal E\) be a nonnegative closed quadratic form on \(\mathcal H\). On a form core \(\mathcal D\), assume its hidden contribution disintegrates into nonnegative fiber forms \(\mathcal E_{H,R}\):
\[
\mathcal E_H(f)=\int\mathcal E_{H,R}(f_R)\,d\nu(R)
\le\mathcal E(f).
\tag{BC4}
\]
Suppose the good contexts obey, for \(\nu\)-almost every \(R\notin B\) and every core test,
\[
\operatorname{Var}_{q_R}f_R
\le\lambda_0^{-1}\mathcal E_{H,R}(f_R),
\qquad \lambda_0>0.
\tag{BC5}
\]
Do not average the inverse fiber constants and silently factor the result. Instead seek constants \(a,c\ge0\), \(0\le b<1\), independent of the test, such that
\[
\|\Pi_Bf\|^2
\le a\,\mathcal E(f)+b\,\operatorname{Var}_\mu f,
\qquad
\operatorname{Var}_\mu(Pf)\le c\,\mathcal E(f).
\tag{BC6}
\]
The first is a localization/escape estimate on the actual joint law; the second controls the retained conditional mean. It is not necessary to assume \(Pf\) belongs to the form domain unless a proposed proof of the second inequality requires it.

Then
\[
\boxed{
\mathcal E(f)\ge
\frac{1-b}{\lambda_0^{-1}+a+c}
\operatorname{Var}_\mu f.}
\tag{BC7}
\]
Indeed, total variance and (BC4)--(BC6) give
\[
\operatorname{Var}_\mu f
=\int_{B^c}\operatorname{Var}_{q_R}f\,d\nu
+\|\Pi_Bf\|^2+\operatorname{Var}_\mu(Pf)
\le(\lambda_0^{-1}+a+c)\mathcal E(f)
+b\,\operatorname{Var}_\mu f.
\]
Absorb the last term. Form-core approximation, \(L^2\)-continuity of the projections, and closedness extend the conclusion to the full form domain.

This is a sufficient theorem, not a derivation of (BC6). Its difficulty is concentrated in a test-uniform localization bound and retained-response control. A small value of \(\nu(B)\) supplies neither automatically.

[[lyapunov-localization-certificate|The Lyapunov certificate]] now gives a test-independent way to establish the first half of (BC6). [[rg-covariance-residue/wilson-frustration-and-joint-escape|Its Wilson application]] proves it on a neighborhood of the explicit two-well exterior, with a stronger block-local variance remainder. [[rg-covariance-residue/wilson-exterior-force-localization|The force--curvature extension]] also controls an unequal-well exterior and combines both regions with one remainder. Other unfavorable contexts and the retained-mean estimate remain open.

## Normalization and physical scope

Rescaling the same form by \(\gamma>0\) sends
\[
\lambda_0\mapsto\gamma\lambda_0,\qquad
a\mapsto a/\gamma,\qquad c\mapsto c/\gamma.
\]
The dimensionless quantities \(\lambda_0a,\lambda_0c,b\) remain unchanged. This is a covariance of the estimate under a common choice of rate unit, not freedom to identify different generators.

For [[rg-covariance-residue/frustrated-su3-conditional-wells|frustrated Wilson conditionals]], the useful question is whether moving the surrounding links makes the apparent conditional barrier inexpensive or expensive in the **joint** form. [[contemporary-puzzles/yang-mills-mass-gap/two-scale-rg-descent-and-the-crossover-lemma|The two-scale retained lift]] supplies one route to the second part of (BC6); [[coarse-response-memory/inq|coarse response memory]] records why eliminating hidden dynamics also retains a return kernel.

Neither a joint configuration-gradient inequality nor a statistical weight is automatically a physical mass. An application still needs a proved comparison to the actual physical transfer or Hamiltonian and bounds uniform through the relevant continuum limit. Likewise this projection identity does not construct a fact-event or a conserved causal charge: [[conservation-of-causal-charge/causal-charge-meaning|capacity, charge and fact]] have distinct types.
