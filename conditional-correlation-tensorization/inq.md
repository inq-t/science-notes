---
inq.module: conditional-correlation-tensorization
inq.include:
  - './'
keywords: [maximal correlation, conditional laws, pinning, tensorization, operator norm, surface response]
---
# Conditional Correlation Tensorization

Pairwise maximal-correlation bounds can control complete groups of variables when the same bounds survive conditioning on every relevant subfamily. The resulting bound is the operator norm of a matrix of pairwise coefficients. Exponential entries can give a surface-size-independent estimate after summation, but a strictly subunit group correlation requires that matrix norm itself to be smaller than one.

## The conditional family is part of the hypothesis

Let \((U_b)_{b\in\Lambda}\) be a finite family of standard-Borel random variables with joint probability law \(\mu\). Write \(\rho_\mu(U_I,U_J)\) for maximal correlation: the supremum of the absolute covariance of real centered unit-variance functions measurable with respect to the two generated sigma-algebras. Set it to zero when one of those centered spaces is trivial. Regular conditional laws make the following pinning expression meaningful:

$$
\rho_K(b,b')
:=
\operatorname*{ess\,sup}_{u_K}
\rho_{\mu(\,\cdot\mid U_K=u_K)}(U_b,U_{b'})
\tag{ARL19b}
$$

Require the same nonnegative coefficients \(\varepsilon(b,b')\) to bound this quantity for every \(K\subset\Lambda\setminus\{b,b'\}\) needed for the comparison. Taking all such subfamilies is a sufficient condition. An additional external conditioning variable can be included, provided the same estimates hold almost surely after it and every further subfamily pinning.

For finite disjoint groups \(I,J\subset\Lambda\), let \(E_{I,J}=[\varepsilon(b,b')]_{I\times J}\). [[library/tensorizing-maximal-correlations/inq|Peyre's Theorem 3.3.1]] gives

$$
\rho(U_I,U_J)
\leq
\min\{1,\|E_{I,J}\|_{\ell^2(J)\to\ell^2(I)}\}.
\tag{ARL20a}
$$

The all-subfamily condition is the paper's natural sigma-metalgebra condition: its Definition 3.1.13 and Remark 3.1.14 combine the supremum over subfamilies with essential suprema over conditioning values. Applying the theorem inside each regular conditional law gives the corresponding bound after a declared base pinning, when the same coefficients satisfy all further conditional hypotheses. Complete pinning is sufficient, not claimed necessary; the paper also gives weaker ordered hypotheses.

## Exponential entries still need an operator estimate

For variables attached to a metric set of blocks, one useful proposed certificate is

$$
\rho_K(b,b')
\leq
\varepsilon(b,b')
\leq
\min\{\kappa_0,Ae^{-m d(b,b')}\},
\qquad \kappa_0<1.
\tag{ARL20}
$$

Here \(A,m,\kappa_0\) and the conditional estimates must have the uniformity claimed by the application. For a nonnegative coefficient matrix, the Schur bound is
\[
\|E_{I,J}\|_{2\to2}\le
\left(\sup_{b\in I}\sum_{b'\in J}\varepsilon(b,b')\right)^{1/2}
\left(\sup_{b'\in J}\sum_{b\in I}\varepsilon(b,b')\right)^{1/2}.
\]
Uniform polynomial volume growth, or a specified summability bound compatible with the exponential rate, controls these sums independently of the number of transverse boundary cells. A sufficient separation can then make the bound subunit. Merely saying bounded growth is insufficient if its growth rate overwhelms the exponential decay; the actual row and column bounds must be checked.

Even when every entry is below one, their matrix norm may be at least one and (ARL20a) then yields only the trivial bound. Ordinary unconditioned pairwise covariance also misses the all-pinnings hypothesis. For instance, three unbiased signs constrained by \(U_3=U_1U_2\) are pairwise independent, but fixing one makes the other two perfectly correlated. Conditional coverage is substantive information about the joint law.

## Boundary response is a downstream application

The theorem controls complete sigma-algebras of the declared variables. [[collared-quasi-factorization-and-surface-response/inq|Collared surface response]] asks for such a uniform Hilbertian angle on the actual gauge-boundary law; identifying its blocks, sectors, metric and conditional laws remains necessary. This is a different certificate from [[positive-semigroup-decay/total-family-spectral-gap|common diagonal decay on a total family]], which can exclude low spectrum without first controlling complete boundary prediction norms.
