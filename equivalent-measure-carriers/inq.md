---
inq.module: equivalent-measure-carriers
inq.include:
  - './'
inq.ambient:
  - '**'
keywords: [Radon–Nikodym, half-density, equivalent measures, conditional expectation]
---
# Equivalent Measure Carriers

Equivalent probability measures present the same Hilbert carrier through a square-root density unitary. That map transports the vacuum, conditional projections, operator domains and quadratic forms together; it does not make a correlated state independent or identify two separately chosen differential operators.

## The density determines the unitary and its range

Let \(\nu\ll\mu\) be probability measures on the same measurable space, with \(r=d\nu/d\mu\). Then

$$
W:L^2(\nu)\longrightarrow L^2(\mu),\qquad Wf=\sqrt r\,f,
\qquad \|Wf\|_\mu^2=\int r|f|^2\,d\mu=\|f\|_\nu^2.
$$

Its range is precisely \(L^2(\{r>0\},\mu)\). Indeed, a function \(g\) supported there has inverse \(g/\sqrt r\), whose squared \(\nu\)-norm is \(\|g\|_\mu^2\). Thus \(W\) is onto the full reference carrier exactly when \(\mu\) and \(\nu\) are equivalent. No upper or positive lower uniform bound on \(r\) is needed.

The normalized constant vector becomes \(\omega=W1=\sqrt r\). For any bounded measurable \(h\), \(WM_h=M_hW\). If an invertible group action preserves both measures, its Koopman representations also intertwine: invariance of both measures makes \(r\) invariant almost everywhere for each group element.

## Conditional projections also change presentation

Assume equivalence and let \(P_{\nu,\mathscr F}\) be conditional expectation onto a sub-sigma-algebra \(\mathscr F\). Its transported projection is

$$
WP_{\nu,\mathscr F}W^{-1}g
=\sqrt r\,\mathbb E_\nu\!\left[g/\sqrt r\mid\mathscr F\right].
$$

Its range is \(\sqrt r\,L^2(\mathscr F,\nu)\), which need not be the subspace of \(\mathscr F\)-measurable functions in \(L^2(\mu)\). Transporting only the Hilbert norm while leaving the conditional projection fixed changes the construction.

For a joint law on standard Borel spaces with \(\nu\sim\nu_A\otimes\nu_B\), take \(\mu=\nu_A\otimes\nu_B\). Since \(\nu_A\) is its marginal,

$$
\int r(a,b)\,d\nu_B(b)=1
\quad\text{for }\nu_A\text{-almost every }a.
$$

The conditional projection onto the first region therefore becomes

$$
(WP_{\nu,A}W^{-1}g)(a,b)
=\sqrt{r(a,b)}
\int\sqrt{r(a,b')}\,g(a,b')\,d\nu_B(b').
$$

The product-reference constant is the transported vacuum exactly when \(r=1\) almost everywhere, equivalently when the joint law is the product of its marginals. An abstract Hilbert-space factorization without the vacuum and regional multiplication actions does not express this independence.

## Operator and form domains travel with the map

For a self-adjoint operator \(L\) on \(L^2(\nu)\), its transported operator is

$$
\widetilde L=WLW^{-1},\qquad D(\widetilde L)=W D(L).
$$

For a densely defined closed nonnegative form \(q\), the transported form is

$$
\widetilde q(g,h)=q(W^{-1}g,W^{-1}h),
\qquad D(\widetilde q)=W D(q).
$$

Closedness and the operator spectrum are preserved by this unitary transport. Identifying \(\widetilde q\) with a separately chosen reference gradient form requires an additional calculation, including its domain. Equivalence of measures alone supplies neither uniform density bounds across a family nor coercive comparison of independently defined forms.
