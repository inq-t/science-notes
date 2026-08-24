# Flat Weight-Zero Precision

Translation invariance, rotational invariance, positivity, weight zero, and exact dilation covariance force a scalar precision kernel in \(d\) flat spatial dimensions to be a nonnegative constant times \(|k|^d\). In three dimensions the unique nonzero shape is therefore \(C|k|^3\); this theorem classifies a quadratic form and does not determine its physical origin or normalization.

## The theorem

Let \(\zeta\) be a real scalar of dilation weight zero on \(\mathbb R^d\). Consider the translation-invariant quadratic form

$$
\mathscr Q[\zeta]
=\frac12
\int\frac{\mathrm d^dk}{(2\pi)^d}
\mathcal K_\zeta(k)|\zeta_{\mathbf k}|^2
$$

on a declared physical subspace. Assume:

1. the quadratic form is diagonal in Fourier space by translation invariance;
2. rotations make \(\mathcal K_\zeta\) a function of \(|k|\);
3. \(\mathscr Q\geq0\);
4. \(\zeta(\lambda x)=\zeta(x)\) as a weight-zero field; and
5. \(\mathscr Q\) is exactly invariant under \(x\mapsto\lambda x\) for every \(\lambda>0\), with no intrinsic scale.

The Fourier coefficient transforms as

$$
\zeta_{\mathbf k}
\longmapsto
\lambda^d\zeta_{\lambda\mathbf k}.
$$

Changing variables in \(\mathscr Q\) gives the homogeneity condition

$$
\mathcal K_\zeta(\lambda k)
=\lambda^d\mathcal K_\zeta(k).
$$

For a measurable radial kernel this implies

$$
\boxed{
\mathcal K_\zeta(k)=C|k|^d,
\qquad C\geq0.}
$$

In \(d=3\),

$$
\boxed{\mathcal K_\zeta(k)=C|k|^3.}
$$

This is **[EXACT]** under the five assumptions. If the quadratic form is strictly positive on every retained nonzero mode, then \(C>0\).

## Covariance consequence

When the precision is invertible on the physical subspace, [[basic-concepts/hessians/fourier-covariance-and-precision|operator inversion]] gives

$$
P_\zeta(k)=\frac{1}{C|k|^d}.
$$

For \(d=3\), the conventional dimensionless power is constant:

$$
\Delta_\zeta^2(k)
=\frac{k^3P_\zeta(k)}{2\pi^2}
=\frac{1}{2\pi^2C}.
$$

Thus exact dilation covariance of a dimensionless three-dimensional scalar yields a scale-invariant two-point shape. The amplitude \(C^{-1}\) remains free.

## Physical quotient

The formula vanishes at \(k=0\). Removing that mode is legitimate only when constants are independently shown to be gauge, constrained, fixed by a normalization, or outside the observable sector. A null eigenvalue is not itself proof of redundancy.

The theorem also does not remove other gauge or constraint directions. They must be handled before the scalar Fourier representation is declared physical, following [[program-core/physical-quotient|the physical-quotient construction]].

## Failure and deformation

If translation invariance, isotropy, or exact dilation covariance fails, the conclusion need not hold. Approximate scale invariance may be represented by

$$
\mathcal K_\zeta(k)=C(k)|k|^3,
$$

but the function \(C(k)\) is new input until a flow equation or microscopic response calculates it. Features, additional scales, anisotropy, or nontranslation-invariant backgrounds require a more general operator.

The result does not establish reflection positivity, Lorentzian unitarity, locality, hyperbolicity, a stress-tensor representation, or the identity of \(\zeta\). Those are independent physical bridges.
