# Continuous Scale Characters Do Not Quantize the Slope

The continuous characters from positive multiplicative scale to an additive real state coordinate form a real one-parameter family. Ratio dependence, cocycle composition, continuity, and even an independently normalized rank-one generator therefore do not select unit slope.

## The character space

The exponential map is an isomorphism of topological groups,

$$
\exp:(\mathbb R,+)
\overset{\sim}{\longrightarrow}
(\mathbb R_{>0},\times).
$$

Consequently every continuous homomorphism

$$
\Theta:(\mathbb R_{>0},\times)
\longrightarrow(\mathbb R,+)
$$

corresponds to a continuous additive map

$$
f(u):=\Theta(e^u).
$$

Continuous additive maps on \(\mathbb R\) are precisely \(f(u)=\lambda u\). Hence

$$
\boxed{
\operatorname{Hom}_{\mathrm{cont}}
(\mathbb R_{>0},\mathbb R)
\cong\mathbb R,
\qquad
\Theta_\lambda(r)=\lambda\ln r.}
$$

The same conclusion holds for Borel-measurable homomorphisms. Evaluation at \(e\) supplies the explicit isomorphism

$$
\Theta\longmapsto\Theta(e)=\lambda.
$$

There is no distinguished primitive element in this character space. The values \(\lambda=2\), \(\lambda=\sqrt2\), and every other real value obey exactly the same continuity and composition laws as \(\lambda=1\).

## The normalized-generator countermodel

Suppose the state-side reduction has a fixed generator

$$
Q^*=Q,
\qquad
Q^2=\mathbf1,
$$

and a real coordinate \(\theta\) conjugate to \(Q\). For every \(\lambda\in\mathbb R\), positive rescaling can act by the translation

$$
\theta\longmapsto\theta+\lambda\ln r.
$$

These actions are continuous, rank one, and compositional:

$$
(r_2r_1)\cdot\theta
=r_2\cdot(r_1\cdot\theta).
$$

Normalizing \(Q\) removes the freedom to hide \(\lambda\) in an arbitrary rescaling of the generator. It makes different slopes physically comparable, but it supplies no equation that prefers one of them. Thus the hypotheses of [[basic-concepts/soldering/affine-scale-state|affine scale--state soldering]] admit a countermodel for every real slope.

In the Weyl-scale convention

$$
N-N_c=-\ln\frac{\sigma}{\sigma_c},
\qquad
\theta-\theta_c=\varrho_\perp(N-N_c),
$$

the exact no-go statement is

$$
\boxed{
\text{ratio dependence}
+\text{rank one}
+\text{cocycle composition}
+\text{regularity}
\not\vdash |\varrho_\perp|=1.}
$$

If the zero character is excluded by requiring a nontrivial bridge, the remaining slopes still fill \(\mathbb R\setminus\{0\}\). If orientation reversal is declared physically equivalent, the invariant width \(\nu:=|\varrho_\perp|\) still ranges continuously over \(\mathbb R_{>0}\).

## Why familiar quantization arguments do not apply

Real conformal weights do not form an integer lattice: the one-dimensional representations

$$
r\longmapsto r^w
$$

exist for every real \(w\). Passing to unitary characters does not help, because

$$
r\longmapsto e^{i\lambda\ln r}
$$

is a continuous character for every \(\lambda\in\mathbb R\). The domain \(\mathbb R_{>0}\simeq\mathbb R\) is noncompact and has no periodic logarithmic cycle whose winding would force an integer.

Quantization could arise only after adding structure not present in the affine theorem—for example, a compactified logarithmic-scale direction, a target lattice, an extension to a group with a discrete weight lattice, a boundary condition, or a microscopic selection rule. Such an addition would need its own physical justification and must show why the selected character is primitive.

The proposal \(\nu=1\) in [[program-core/axioms-and-principles|the unit-width principle]] is therefore logically independent of the affine character theorem. It may be adopted as a physical principle or eventually derived from a stronger construction, but it is not a consequence of continuity or character theory alone.
