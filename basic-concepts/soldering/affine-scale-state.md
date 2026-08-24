# Affine Soldering of Scale Ratios to a State Coordinate

A regular rank-one comparison that depends only on ratios of positive scale sections and composes as an endpoint cocycle must be logarithmic in that ratio. This is a conditional character theorem about an extended scale--state bridge; it neither constructs the physical comparison nor fixes the continuous slope that relates scale to state.

## Positive scale-section ratios

Let \(L^+\to X\) be a positive ray bundle. If \(\sigma_1\) and \(\sigma_2\) are positive sections over the same region, there is a unique positive function \(r_{21}\) such that

$$
\sigma_2=r_{21}\sigma_1,
\qquad
r_{21}:=\frac{\sigma_2}{\sigma_1}>0.
$$

Suppose a proposed state-side comparison has already passed through the following reductions:

1. **Common carrier.** The states associated with different scale sections have been related by specified transport, so their comparison is well typed.
2. **Rank one.** After quotienting vertical, central, gauge, and physically null directions, the relevant comparison lies along one fixed nonzero generator \(Q\).
3. **Endpoint and ratio dependence.** Its coefficient is path independent on the domain under study and has the form
   $$
   \Theta(\sigma_2,\sigma_1)=F(r_{21})
   $$
   for one function \(F:\mathbb R_{>0}\to\mathbb R\). If the ratio varies over \(X\), this equation is understood pointwise with the same \(F\).
4. **Cocycle composition.** For every composable triple,
   $$
   \Theta(\sigma_3,\sigma_1)
   =\Theta(\sigma_3,\sigma_2)
   +\Theta(\sigma_2,\sigma_1).
   $$
5. **Full positive rescaling domain.** Every constant ratio \(r>0\) is admissible in the reduced comparison.
6. **Regularity.** The function \(F\) is Borel measurable. Continuity at one point or local boundedness would also suffice.

The first two hypotheses type the physical use of the coefficient. The last four are the mathematical hypotheses that force its form. In particular, path independence excludes an additional holonomy component; it is not a consequence of rank one alone.

## Conditional affine theorem

Under these hypotheses, there is a unique \(\kappa\in\mathbb R\) such that

$$
\boxed{
\Theta(\sigma_2,\sigma_1)
=\kappa\ln\frac{\sigma_2}{\sigma_1}.}
$$

To prove this, apply cocycle composition to two successive constant rescalings. Ratio dependence gives

$$
F(r_2r_1)=F(r_2)+F(r_1).
$$

Define \(f:\mathbb R\to\mathbb R\) by \(f(u):=F(e^u)\). Then

$$
f(u+v)=f(u)+f(v).
$$

Measurability excludes the discontinuous Cauchy solutions, so \(f(u)=\kappa u\). Therefore \(F(r)=\kappa\ln r\). Conversely, every real \(\kappa\) defines such a measurable cocycle, so the conclusion is exact and exhaustive under the stated hypotheses.

This is a **[CONDITIONAL THEOREM]**. A concrete wall construction must still supply the carrier, transport, quotient, generator, endpoint dependence, and regularity rather than infer them from the logarithmic answer.

## Weyl scale and the FLRW corollary

Choose a reference section \(\sigma_*\) and define logarithmic Weyl scale by

$$
N:=-\ln\frac{\sigma}{\sigma_*}.
$$

Let \(\sigma_c\) correspond to \(N_c\), and center a state coordinate by

$$
\theta(\sigma)-\theta(\sigma_c)
:=\Theta(\sigma,\sigma_c).
$$

Since

$$
\ln\frac{\sigma}{\sigma_c}=-(N-N_c),
$$

the theorem gives

$$
\boxed{
\theta(N)-\theta(N_c)
=\varrho_\perp(N-N_c),
\qquad
\varrho_\perp:=-\kappa.}
$$

This affine dependence is already a Weyl-scale corollary; it does not require cosmology. Only after imposing the homogeneous FLRW identification

$$
\sigma\propto a^{-1}
$$

does it become

$$
N-N_c=\ln\frac{a}{a_c},
\qquad
\theta-\theta_c
=\varrho_\perp\ln\frac{a}{a_c}.
$$

Thus the FLRW formula is a specialization of the scale-section theorem, not its premise. Neither \(N\) nor \(\theta\) is thereby identified with proper time, modular time, or an RG scale.

## Scope of the result

The theorem determines logarithmic form, not physical normalization. [[basic-concepts/soldering/continuous-character-no-go|The continuous-character no-go]] proves that \(\varrho_\perp\) remains an arbitrary real slope; a unit-width law is additional input.

If only a proper subgroup of positive rescalings is admissible, the classification applies only to that subgroup. If a different character \(F_p\) is allowed at each point, one obtains a field \(\kappa(p)\), not a universal coefficient. If comparison has holonomy or additional generators, no single endpoint scalar \(\Theta\) captures it. If regularity is dropped, discontinuous additive solutions survive.

Finally, this is *soldering* in the project's extended sense: it is a controlled bridge between a scale register and a state coordinate. It is not the tautological solder form on a frame bundle. [[basic-concepts/soldering/entry|The general soldering note]] owns that strict distinction.
