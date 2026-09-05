# A Response Spectrum Is Relative to a Metric

A quadratic response supplies an invariant numerical spectrum only relative to a second, specified metric on the same tangent carrier. Raw Hessian eigenvalues can change under a dimensionless coordinate rescaling. The generalized spectrum survives simultaneous pullback of both forms, but still depends on their relative normalization. Thus a geometric integer, a dimensionless coefficient, a normalized response edge, and a physical mass are four different kinds of output.

## The finite-dimensional quotient

Let \(V\neq0\) be a finite-dimensional real vector space, let \(g\) be a positive-definite inner product, and let \(q\) be a symmetric nonnegative bilinear response. Suppose \(q\) and \(g\) have the same quantity type, so their quotient is dimensionless. Define the unique \(g\)-self-adjoint nonnegative endomorphism \(R\) by

$$
g(u,Rv)=q(u,v).
\tag{RS1}
$$

Its lower edge is

$$
\boxed{\lambda_*=\min_{v\neq0}\frac{q(v,v)}{g(v,v)}.}
\tag{RS2}
$$

The operator acts on **response tangents**, not on numbers, spacetime points, or masses. A physical application must specify which variations these tangents represent. Gauge-null directions must be quotiented with a justified metric; physical nonvacuum directions cannot be removed merely because they soften the edge.

For an invertible coordinate map \(J:V'\to V\), pull back both forms:

$$
q'=J^{\mathsf T}qJ,\qquad
g'=J^{\mathsf T}gJ,\qquad
R'=(g')^{-1}q'=J^{-1}RJ.
\tag{RS3}
$$

Consequently the generalized spectrum and (RS2) are unchanged. This follows either from similarity or from the bijective substitution \(v=Jv'\) in the quotient. The complex Hermitian version uses conjugate transpose.

The denominator is not optional. For

$$
q=\begin{pmatrix}3&0\\0&8\end{pmatrix},
\qquad g=I,\qquad
J=\begin{pmatrix}2&0\\0&1/2\end{pmatrix},
$$

the transformed response matrix has ordinary eigenvalues \(12,2\), whereas

$$
q'=\operatorname{diag}(12,2),\qquad
g'=\operatorname{diag}(4,1/4)
$$

still has generalized eigenvalues \(3,8\). All coordinates can be dimensionless. Absence of units did not make the raw eigenvalues invariant.

## Coordinate covariance does not fix normalization

An independent change of response conventions,

$$
q\mapsto aq,\qquad g\mapsto bg,\qquad a,b>0,
$$

changes the edge by

$$
\lambda_*\mapsto\frac{a}{b}\lambda_*.
\tag{RS4}
$$

Only a common change cancels. For example, changing an entropy ledger from nats to bits rescales its Hessian by \(1/\log2\); this cancels only if the reference metric carries the same change. A metric selected independently of the entropy ledger need not do so.

Thus the geometrically meaningful object is the **normalized pair** \((q,g)\), not “a Hessian with no units.” Choosing \(g=q\) when \(q>0\) makes \(R=I\) tautologically. It cannot establish a physical gap unless an independent theorem compares that metric to the complete physical norm with a uniform constant.

Nor does finite-dimensional positivity settle the infinite-dimensional case. On \(\ell^2(\mathbb N)\), the bounded operator \(Re_n=n^{-1}e_n\) has \(q(v,v)>0\) for every nonzero \(v\), but its infimum relative to the ordinary norm is zero. The closed-form and domain-correct extension of (RS2) is already stated in [[contemporary-puzzles/yang-mills-mass-gap/internal-yardstick-as-a-generalized-rate-edge|the generalized rate-edge theorem]].

[[rg-covariance-residue/multilevel-local-gauge-completion|The Gaussian multilevel completion]] gives a different, concrete carrier warning. Its terminal Schur response has a depth-uniform floor, but a coherent auxiliary field repeated across \(k+1\) levels has the same single terminal cost divided by a product norm \(k+1\) times as large. The enlarged lower edge can therefore tend to zero without any change to the terminal observable law. Enlarging a presentation is not an invertible change of coordinates on the original carrier; (RS3) does not license comparing its arbitrary product metric to the physical one.

## When a Hessian really transforms as a form

For a scalar \(F\) and a nonlinear coordinate change \(x=x(y)\), ordinary second derivatives obey

$$
\partial_a\partial_b(F\circ x)
=
(\partial_a x^i)(\partial_b x^j)\partial_i\partial_jF
+
(\partial_iF)\partial_a\partial_bx^i.
\tag{RS5}
$$

At a stationary point, \(\mathrm dF=0\), the last term vanishes and the Hessian is an intrinsic bilinear form. Away from stationarity, one needs a declared connection and \(\nabla\mathrm dF\), or the appropriate intrinsic information-metric construction. For example, \(F(x)=x\) has zero ordinary Hessian, but \(x=y+y^2\) gives second derivative \(2\) at \(y=0\). No response was created by changing coordinates.

[[affine-hessian-structure|Affine Hessian structure]] owns the connection and integrability requirements. [[rg-covariance-residue/compact-gauge-kernel-tangent-response|The normalized compact-kernel example]] adds a separate warning: even a correctly computed mode Hessian need not equal the Fisher metric of the sampled law.

## What a geometric numeral would have to explain

A dimension or index can genuinely be intrinsic without being an eigenvalue. To use it in a spectral prediction requires a theorem connecting that invariant to the normalized pair \((q,g)\), its operator domain, and its full relevant carrier. No inference from a rank, multiplicity, or integer label alone supplies that theorem.

If a mass-squared operator is identified with the response, its mass coefficient involves a square root; if an inverse-length translation generator is identified with it, its mass coefficient is linear after the clock/action conversion. The numeral alone does not decide between those two type signatures. [[contemporary-puzzles/yang-mills-mass-gap/scale-torsor-and-the-global-local-gap-invariant|The scale-torsor construction]] then distinguishes the invariant coefficient from the dimensional yardstick.

The finite congruence and normalization identities are checked in [[contemporary-puzzles/yang-mills-mass-gap/receipts/internal-yardstick-rate-edge-receipt.py|the rate-edge receipt]], including the carrier-map norm counterexample used to repair the scale-torsor gap implication. These matrix checks do not establish an infinite-dimensional response floor.
