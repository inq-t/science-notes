# Affine Scale--State Soldering

If transported cross-scale comparison is rank one, depends only on the scale ratio, composes without holonomy, and is measurable, its state coordinate is affine in logarithmic scale. This conditional theorem fixes the form of the soldering but neither its width nor the existence of the required wall transport.

Let

$$
x:=\ln\frac a{a_c}
=-\ln\frac\sigma{\sigma_c}
=N-N_c.
$$

Suppose a constructed comparison assigns a real coefficient $\Theta(r)$ to a positive scale ratio $r=a_2/a_1$ and satisfies:

1. **Rank one:** the relevant transported cocycle has one noncentral generator $Q$.
2. **Ratio dependence:** the coefficient depends on $(a_2,a_1)$ only through $r$.
3. **Composition:** successive comparisons obey
   $$
   \Theta(r_1r_2)=\Theta(r_1)+\Theta(r_2).
   $$
4. **Negligible holonomy:** comparison around the relevant scale path does not add another state-space component.
5. **Regularity:** $\Theta$ is measurable, or obeys another condition sufficient to exclude discontinuous Cauchy solutions.

Then the measurable homomorphisms from $(\mathbb R_+,\times)$ to $(\mathbb R,+)$ are

$$
\Theta(r)=\varrho_\perp\ln r.
$$

Centering the state coordinate at the crossing gives

$$
\boxed{\theta(N)=\varrho_\perp(N-N_c)=\varrho_\perp x.}
$$

This is a **[CONDITIONAL THEOREM]**. It is not a theorem that a physical Connes cocycle reduces to such a scalar coefficient; that is an output required from [[wall-construction-interface/entry|the wall construction]].

## Orientation and width

Reversing the binary convention sends

$$
Q\mapsto-Q,
\qquad
\theta\mapsto-\theta,
\qquad
\varrho_\perp\mapsto-\varrho_\perp.
$$

The orientation-independent width is therefore

$$
\nu:=|\varrho_\perp|>0.
$$

Once $Q^2=\mathbf1$ and the conjugate exponential coordinate are fixed, $\nu$ measures the rate of polarization per e-fold. [[width-principle]] considers the further law $\nu=1$.

## What the theorem does not fix

The affine theorem leaves a continuous real slope. [[no-gos/character-theory-does-not-fix-unit-width|The character-theory no-go]] owns the explicit homomorphism calculation and shows why neither real conformal weights nor the multiplicative Cauchy equation quantize $\varrho_\perp$. A unit value requires an additional normalization or principle.

The coordinate $\theta$ may also hide two different roles: a label on a family of states and a comparison datum obtained after transport. They coincide only if the connection and holonomy conditions make that identification legitimate. This live issue is isolated in [[open-questions/state-coordinate-and-holonomy]].
