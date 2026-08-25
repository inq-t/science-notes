# The CST Homogeneous Response-Family Interface

Causal Scale Theory is an architecture for homogeneous response members, not an assertion that every admissible wall has a balanced binary profile. After a wall construction, physical quotient, central scalarization, scale--state comparison, extensive normalization, and distinguished reference cut have been supplied, this interface separates a member's normalized response shape from the constitutive map that realizes it as a cosmological density. The currently developed member is the balanced-binary branch CST-B2; the finite $A_2$ calculation is an audit seed, not a second physical member.

## The member datum

Assume [[program-core/center-valued-response|a declared scalarization]] has turned the center-valued homogeneous response into a positive scalar response on one transported scale path. A rank-one homogeneous member $\mathcal M$ must then specify enough data to prove a factorization

$$
\boxed{
G^{\mathcal M}_{NN}(N)
=C_{\mathcal M}(N)\,
g_{\mathcal M}\!\left(\theta_{\mathcal M}(N)\right)
\left(\frac{\mathrm d\theta_{\mathcal M}}{\mathrm dN}\right)^2.}
$$

Here $g_{\mathcal M}$ is the reduced positive response coefficient, $\theta_{\mathcal M}$ is a canonically normalized state coordinate, and $C_{\mathcal M}$ is the remaining extensive factor in the declared comparison scheme. The factor $C_{\mathcal M}$ need not be an integer or a microscopic channel count. If central-weight response, hidden-mode reduction, or renormalization does not admit this factorization, the member must retain the fuller response rather than force it into this one-coordinate interface.

For an affine exponential family one may have

$$
g_{\mathcal M}=\Psi_{\mathcal M}'',
$$

but Hessianity is not part of the interface definition. [[hessian-response-geometry/entry|Hessian response geometry]] owns the additional flat-connection, common-potential, and BKM-selection obligations.

Choose a distinguished reference cut $N_c$, which is only a candidate crossing cut until the member constructs the relevant event, such that

$$
0<G^{\mathcal M}_{NN}(N_c)<\infty.
$$

Define the normalized member profile

$$
\boxed{
f_{\mathcal M}(N)
:=\frac{G^{\mathcal M}_{NN}(N)}
{G^{\mathcal M}_{NN}(N_c)},
\qquad
f_{\mathcal M}(N_c)=1.}
$$

The cut $N_c$ is a normalization point. It is a maximum, stationary point, symmetry center, or cosmological crossing only when the selected member and its downstream realization prove the corresponding statement.

Whenever the rank-one factorization holds,

$$
f_{\mathcal M}(N)
=\frac{C_{\mathcal M}(N)}{C_{\mathcal M}(N_c)}
\frac{g_{\mathcal M}(\theta_{\mathcal M}(N))}
{g_{\mathcal M}(\theta_{\mathcal M}(N_c))}
\left[
\frac{\theta'_{\mathcal M}(N)}
{\theta'_{\mathcal M}(N_c)}
\right]^2.
$$

Thus a reduced response curve alone does not fix the physical profile. A varying extensive factor, nonlinear soldering, changing central evaluation, or noncommuting hidden-mode reduction can move the maximum, change the tails, or invalidate a rigid member theorem.

## The cosmological return type

[[scale-capacity|The matching-ratio note]] defines $\mathfrak R_c$ by comparing the scalarized full-cut response at the distinguished reference cut with an independently normalized gravitational entropy measure. The historical subscript $c$ denotes the candidate crossing reference and becomes a physical crossing label only in a member that constructs that event. In spacetime dimension $D=d+1$ with $d>1$, [[free-energy-source|the anchored source postulate]] and [[horizontal-temperature|the horizontal-temperature identification]], followed by [[conformal-scale-geometry/dimensional-horizon-conversion|the dimensional Einstein--horizon conversion]], give the family-level **[CONDITIONAL OUTPUT]**

$$
\boxed{
\rho_X^{\mathcal M}(N)
=\frac{\mathfrak R_c}{d-1}
\rho_{\mathrm{crit},c}
f_{\mathcal M}(N).}
$$

Thus

$$
\Omega_{X,c}=\frac{\mathfrak R_c}{d-1}.
$$

For the present $3+1$ Einstein--FLRW specialization, $d=3$ and the coefficient is $\mathfrak R_c/2$, independently of the member's off-reference shape. This composition does not construct a stress tensor, conservation law, sound speed, perturbation sector, wall state, or the physical crossing event.

## The current balanced-binary member

The label **CST-B2** names the presently developed member with an exhaustive or explicitly conditioned balanced two-outcome channel. It uses

$$
g_{\mathrm{B2}}(\theta)=\operatorname{sech}^2\theta,
\qquad
\theta=\nu(N-N_c),
\qquad
C_{\mathrm{B2}}(N)=C_{\mathrm{B2},c}.
$$

Therefore

$$
f_{\mathrm{B2}}(N)
=\operatorname{sech}^2\!\bigl(\nu(N-N_c)\bigr).
$$

[[response-law|The CST-B2 response note]] owns the resulting two-parameter density. Its rigid equation-of-state, flatness-fold, future-class, and unit-rate results are theorems about CST-B2, not about every member admitted by this interface.

## The $A_2$ audit seed

On the equal-weight commuting three-state model, [[a2-ternary-response/entry|the $A_2$ audit]] gives the exact finite response

$$
g_{A_2}(\theta)
=\frac{2(\cosh\theta+2)}{(1+2\cosh\theta)^2},
\qquad
\boxed{g_{A_2}(0)=\frac23.}
$$

The raw value $2/3$ must be retained: dividing by it to compare shapes does not turn the ternary model into a unit-response physical wall. If one additionally grants affine soldering, constant extensivity, and $N_c$ at $\theta=0$, the normalized audit shape would be

$$
f_{A_2}^{\mathrm{audit}}(N)
=\frac{g_{A_2}(\nu[N-N_c])}{g_{A_2}(0)}
=\frac{3\bigl(\cosh(\nu[N-N_c])+2\bigr)}
{\bigl(1+2\cosh(\nu[N-N_c])\bigr)^2}.
$$

This is an **[EXACT FINITE SHAPE UNDER ADDED KINEMATIC HYPOTHESES]**, not a CST cosmology. No $A_2$ wall algebra, positive state bundle, global root tangent, central scalarization, extensive normalization, source map, or covariant dynamics has been constructed. The audit establishes that the binary member needs a derivation; it does not authorize substituting the ternary curve into the Friedmann equations.

## Construction and measurement

The member itself is fixed by constructing the wall channel or response plane, state and transport, scalarization, state coordinate, extensive factor, and source realization. Once those objects have been fixed independently of the target history, the normalized profile, peak or normalization location, tails, higher response, background history, and correlation data become calculable signatures. Measurement can reject or estimate a constructed member; it cannot decide retroactively which response object was constructed.
