# One Exact Gaussian Comparison Square Forces a Gaussian State

A symmetrically balanced Euclidean Gaussian proximity kernel cannot absorb a non-Gaussian state while retaining exact closure under one self-composition. If its square is another balanced kernel of the same constant-metric scalar-width form, the invariant probability law must itself be Gaussian, with covariance proportional to the proximity cometric. The endpoint factors need not initially be Gaussian or smooth. This isolates a rigidity of the comparison family, rather than a failure of non-Gaussian states to possess dynamics.

**Status: exact rigidity theorem under the fixed-state, positive-density and scalar-width hypotheses below.** The theorem does not derive a Gaussian ontology, exclude interacting diffusion limits, or classify variable-metric or non-Gaussian proximity laws. [[gaussian-overlap-balancing-and-clock-sewing|The Gaussian balancing construction]] owns the explicit Gaussian member and its complete Hermite clock.

## Fix the state and comparison type

Let \(d\ge1\), let \(C\) be a fixed positive definite matrix, and let

\[
d\mu(x)=\rho(x)dx,\qquad
0<\rho(x)<\infty\ \text{almost everywhere},\qquad
\int_{\mathbb R^d}\rho(x)dx=1.
\tag{GR1}
\]

For two widths \(\epsilon,\eta>0\), suppose positive finite measurable endpoint factors define

\[
Q_\delta(x,y)=a_\delta(x)a_\delta(y)
\exp\left[-\frac{(x-y)^TC^{-1}(x-y)}{4\delta}\right],
\qquad \delta\in\{\epsilon,\eta\},
\tag{GR2}
\]

and that each is balanced against the same state:

\[
\int Q_\delta(x,y)d\mu(y)=1
\quad\text{for almost every }x.
\tag{GR3}
\]

Symmetry, (GR3) and Jensen's inequality make these bounded self-adjoint Markov contractions on \(L^2(\mu)\). No Gaussian ansatz is imposed on \(a_\delta\) or \(\rho\). Assume just one exact operator identity,

\[
Q_\epsilon^2=Q_\eta.
\tag{GR4}
\]

Then there are \(m\in\mathbb R^d\) and \(\sigma^2>0\) such that

\[
\boxed{
\mu=N(m,\sigma^2 C),\qquad
\eta=2\epsilon\sqrt{1+(\epsilon/\sigma^2)^2}.
}
\tag{GR5}
\]

In particular, exact self-composition fails at every positive width for every non-Gaussian \(\mu\) satisfying (GR1), whenever the two balanced kernels exist. The proof requires neither an assumed local generator nor differentiability of a proposed time parameter.

## Conjugate to a kernel on Lebesgue space

Whitening by \(C^{-1/2}\) reduces the proof to \(C=I\). The transformed density includes the usual determinant Jacobian, so proving covariance \(\sigma^2 I\) in these coordinates proves covariance \(\sigma^2 C\) in the original ones.

Put \(\psi=\sqrt\rho\). Multiplication by \(\psi\) is a unitary map from \(L^2(\mu)\) to \(L^2(dx)\), and conjugates each comparison to the positive symmetric kernel

\[
K_\delta(x,y)=b_\delta(x)b_\delta(y)
e^{-|x-y|^2/(4\delta)},\qquad
b_\delta=a_\delta\psi.
\tag{GR6}
\]

It remains a contraction and satisfies \(K_\delta\psi=\psi\). Define

\[
c=\frac1{4\epsilon},\qquad
\widehat c=\frac1{4\eta},\qquad
M(s)=\int b_\epsilon(z)^2e^{-2c|z|^2+s\cdot z}dz.
\tag{GR7}
\]

Tonelli's theorem writes the composition kernel as

\[
(K_\epsilon^2)(x,y)
=b_\epsilon(x)b_\epsilon(y)
e^{-c(|x|^2+|y|^2)}M(2c(x+y)).
\tag{GR8}
\]

The operator identity implies equality of this kernel and \(K_\eta\) almost everywhere. One way to justify this step without postulating pointwise kernel composition is to test both positive kernels on indicators of bounded measurable sets. Their rectangle integrals are finite by the operator bound; equality of all these integrals gives equality of the locally integrable kernels.

Since the endpoint factors are positive and finite almost everywhere, (GR8) makes \(M(s)\) finite for almost every \(s\in\mathbb R^d\). Its finiteness domain is convex by Hölder's inequality. A full-measure convex domain contains every point: around any point choose a simplex of finite-domain points containing it in its interior. Hence \(M\) is finite everywhere. Finiteness in neighborhoods supplies integrable exponential bounds for all its derivatives. In particular \(M>0\) and \(\log M\) is smooth.

## The composition integral must be Gaussian

Let \(u_\delta=\log b_\delta\), and set

\[
F(r)=\log M(2cr),\qquad
v(x)=u_\eta(x)-u_\epsilon(x)
+(c-\widehat c)|x|^2.
\]

Taking logarithms of the kernel identity gives almost everywhere

\[
F(x+y)=v(x)+v(y)+2\widehat c\,x\cdot y.
\tag{GR9}
\]

The initially measurable \(v\) causes no differentiation gap. A Fubini slice at a suitable fixed \(y_0\) writes it almost everywhere as
\(F(x+y_0)-v(y_0)-2\widehat c\,x\cdot y_0\), a smooth function. Using that representative, (GR9) is an identity of smooth functions, since it already holds almost everywhere. Its mixed derivative is

\[
\partial_{x_i}\partial_{y_j}F(x+y)
=2\widehat c\,\delta_{ij}.
\tag{GR10}
\]

Thus the normalized finite measure with density proportional to
\(b_\epsilon(z)^2e^{-2c|z|^2}\) has a quadratic log moment-generating function, with covariance

\[
\frac{\widehat c}{2c^2}I.
\tag{GR11}
\]

Uniqueness of a moment-generating function finite in a neighborhood of zero identifies that measure as a nondegenerate Gaussian. This can also be checked by continuing the explicitly quadratic exponential to its characteristic function. In particular, \(u_\epsilon\) is quadratic with a scalar Hessian, almost everywhere.

Writing out its quadratic and linear parts therefore gives

\[
K_\epsilon(x,y)
=N\exp\left[-A(|x|^2+|y|^2)
+2c\,x\cdot y+\ell\cdot(x+y)\right],
\quad
A=\frac{c^2}{2\widehat c}>0,
\quad N>0.
\tag{GR12}
\]

This conclusion used arbitrary endpoint factors. It is stronger than checking closure within a previously assumed Gaussian balancing class.

## Boundedness and the fixed vector select the confining case

The contraction property forces \(A\ge c\). To see this, take a nonnegative nonzero compactly supported test function of fixed \(L^2\) norm and translate its support by \(Re\). If \(A<c\), its quadratic expectation under (GR12) grows like
\(\exp[2(c-A)R^2+O(R)]\), contradicting boundedness. If \(A=c\) and \(\ell\ne0\), translation in the direction of \(\ell\) likewise makes it grow exponentially in \(R\).

The remaining boundary case \(A=c\), \(\ell=0\) is a scalar Gaussian convolution. Its Fourier multiplier is a positive constant times \(e^{-|\xi|^2/(4c)}\). Contractivity makes that constant at most one, and the multiplier equals one at most on a Lebesgue-null set. Consequently it has no nonzero \(L^2\) fixed vector, contrary to \(K_\epsilon\psi=\psi\). Therefore

\[
A>c.
\tag{GR13}
\]

Complete the square using

\[
m=\frac{\ell}{2(A-c)},\qquad
\beta=\sqrt{A^2-c^2}>0.
\tag{GR14}
\]

Direct Gaussian integration shows that
\(\phi(x)=e^{-\beta|x-m|^2}\) is a positive \(L^2\) eigenvector of \(K_\epsilon\), with some positive eigenvalue \(\lambda\). Self-adjointness and the strictly positive inner product \(\langle\phi,\psi\rangle\) imply

\[
\lambda\langle\phi,\psi\rangle
=\langle K_\epsilon\phi,\psi\rangle
=\langle\phi,K_\epsilon\psi\rangle
=\langle\phi,\psi\rangle,
\]

so \(\lambda=1\).

This positive fixed vector is unique up to scale. Indeed, normalize \(\phi\) in \(L^2(dx)\), and conjugate by it to a Markov kernel on \(L^2(\phi^2dx)\). If another fixed vector gives \(h=\psi/\phi\), then

\[
0=\frac12\int K_\epsilon(x,y)\phi(x)\phi(y)
|h(x)-h(y)|^2dx\,dy.
\tag{GR15}
\]

The integral identity follows from the Markov marginals and is valid for \(h\in L^2(\phi^2dx)\). Strict positivity of the kernel makes \(h\) constant almost everywhere. Thus

\[
\rho(x)\propto e^{-2\beta|x-m|^2},\qquad
\sigma^2=\frac1{4\beta}.
\tag{GR16}
\]

Finally \(A=c^2/(2\widehat c)\) and
\(A^2-c^2=1/(16\sigma^4)\) give exactly the width relation in (GR5). In particular \(\eta>2\epsilon\). A finite normalizable fixed state excludes the free convolution equality \(\eta=2\epsilon\).

## Exact scalar sewing is therefore rigid beyond Gaussian ansatzes

If an entire balanced family (GR2) can be reparameterized as a strongly continuous Markov semigroup with a continuous increasing scalar width, it satisfies (GR4) for every positive time and hence has the Gaussian state (GR5). The explicit balancing formulas then give the common first-mode multiplier

\[
r(\epsilon)=\sqrt{1+(\epsilon/\sigma^2)^2}-\epsilon/\sigma^2.
\tag{GR17}
\]

Semigroup composition makes \(r(t+s)=r(t)r(s)\). Strong continuity and nontriviality imply \(r(t)=e^{-\omega t}\), \(\omega>0\), so

\[
\epsilon(t)=\sigma^2\sinh(\omega t).
\tag{GR18}
\]

Smoothness of this scalar time relation follows from the resulting operator identity; it was not required in the rigidity proof. With diffusion normalization \(\alpha=\omega\sigma^2\), the returned positive generator is

\[
-\alpha C:\nabla^2+
\frac{\alpha}{\sigma^2}(x-m)\cdot\nabla
\quad\text{on }L^2(N(m,\sigma^2C)).
\tag{GR19}
\]

This agrees with [[gaussian-overlap-balancing-and-clock-sewing|the Gaussian scalar-clock classification]]. The stronger conclusion here is that allowing non-Gaussian endpoint factors or a non-Gaussian invariant density does not enlarge this exact scalar-width sewing family.

## A quartic state fails this closure nonperturbatively

For example, in one dimension let

\[
\rho_g(x)=Z_g^{-1}
\exp\left[-\frac{(x-m)^2}{2s^2}-g(x-m)^4\right],
\qquad s^2>0,\quad g>0.
\tag{GR20}
\]

It is a smooth strictly positive probability density and is not Gaussian. Whenever its positive balanced comparisons of form (GR2) exist, no widths \(\epsilon,\eta>0\) can satisfy \(Q_\epsilon^2=Q_\eta\). The conclusion holds at every nonzero \(g\), without truncating a power series or assuming that the factors themselves have Gaussian form. [[quartic-overlap-sewing-tangent|The quartic sewing tangent]] supplies the separate perturbative question of how the defect first appears.

This does not prevent \(\rho_g\) from being the invariant state of a local reversible diffusion, or prevent balanced small comparisons from approaching its heat semigroup under repeated refinement. Exact closure of each finite-width Gaussian proximity member is stronger than such a limit. [[interacting-comparison-refinement|Interacting comparison refinement]] studies that distinct construction.

A non-Gaussian comparison kernel, varying response metric, additional boundary indices, or another composition rule changes the hypotheses. Those possibilities remain available to the joint-realization programme. The theorem identifies a restriction that must be relaxed to admit an interacting state; it does not authorize defining the primitive comparison to be the desired interacting heat kernel.
