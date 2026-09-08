# Gaussian Overlap Balancing Selects a Sewable Clock

A symmetric Gaussian proximity kernel can preserve a specified Gaussian state and generate an exact clock, but ordinary row normalization changes that state. Symmetric endpoint balancing repairs the state at every comparison width. Within this balanced constant-metric family, requiring one scalar clock to compose all widths forces the proximity cometric to be proportional to the full state covariance. The resulting process is exactly the Mehler semigroup, retaining every Gaussian fluctuation mode with its Hermite rate.

**Status: exact Gaussian construction and classification under the stated kernel, carrier and scalar-clock hypotheses.** The Gaussian state and the choice of Gaussian proximity comparisons are inputs. Balancing and exact scalar-clock sewing are additional constitutive requirements. This does not construct the corresponding comparisons on the sewn \(SU(2)\) carrier or recover a Yang–Mills theory. No novelty is claimed for Gaussian integration, symmetric kernel balancing or the Mehler process.

## Ordinary row normalization changes the state

Fix \(d\ge1\), positive definite matrices \(\Sigma,C\), and the probability measure \(\mu_\Sigma=N(0,\Sigma)\) on \(\mathbb R^d\). The covariance \(\Sigma\) specifies the state; \(C\) specifies the proximity cometric. They have the same coordinate covariance units, so the width \(\epsilon>0\) is dimensionless. Set

\[
K_\epsilon(z,z')
=\exp\left[-\frac{(z-z')^TC^{-1}(z-z')}{4\epsilon}\right],
\qquad D=2\epsilon C.
\tag{GB1}
\]

This is a symmetric positive-definite kernel, not a probability transition until its normalization is specified. Integrating against the source state gives the row degree

\[
d_\epsilon(z)
=\sqrt{\frac{\det D}{\det(\Sigma+D)}}
\exp\left[-\frac12z^T(\Sigma+D)^{-1}z\right].
\tag{GB2}
\]

The row-normalized transition \(P_\epsilon^{\rm row}(z,dz')=K_\epsilon(z,z')\mu_\Sigma(dz')/d_\epsilon(z)\) is exactly

\[
z'\mid z\sim N(Mz,V),\qquad
V=(\Sigma^{-1}+D^{-1})^{-1},\qquad
M=VD^{-1}=\Sigma(\Sigma+D)^{-1}.
\tag{GB3}
\]

The matrix order in this formula matters when \(C\) and \(\Sigma\) do not commute. Completing the square in the actual joint density proves it. Detailed balance holds for \(d_\epsilon\mu_\Sigma\), whose normalized covariance is

\[
\boxed{S_\epsilon=
[\Sigma^{-1}+(\Sigma+D)^{-1}]^{-1}
\longrightarrow\frac12\Sigma.}
\tag{GB4}
\]

Thus the carrier on which this row-normalized comparison is symmetric is \(L^2(N(0,S_\epsilon))\), not generally \(L^2(\mu_\Sigma)\). Positivity of the unnormalized kernel has not preserved the original state.

Expansion of the mean and covariance in (GB3) gives on smooth polynomial test functions

\[
\frac{P_\epsilon^{\rm row}-I}{\epsilon}f
\longrightarrow
C:\nabla^2f-2(C\Sigma^{-1}z)\cdot\nabla f.
\tag{GB5}
\]

The covariance \(\Sigma/2\) in (GB4) is exactly the invariant covariance of this limiting Ornstein–Uhlenbeck expression. For \(C=I\), its linear rates are twice the eigenvalues of \(\Sigma^{-1}\). For \(C=\Sigma\), all linear rates are two, but the state still has the wrong covariance.

Replacing the source density by its normalized square root changes the source covariance to \(2\Sigma\). The same row-normalization calculation then has limiting invariant covariance \(\Sigma\) and generator

\[
C:\nabla^2-(C\Sigma^{-1}z)\cdot\nabla.
\tag{GB6}
\]

This half-density correction is only a limiting repair: its finite-width invariant covariance need not equal \(\Sigma\). Equations (GB2)–(GB6) are explicit Gaussian calculations.

## Symmetric balancing preserves the full state exactly

Instead seek an endpoint factor \(a_\epsilon>0\) satisfying

\[
Q_\epsilon(z,z')
=a_\epsilon(z)K_\epsilon(z,z')a_\epsilon(z'),\qquad
\int Q_\epsilon(z,z')\,d\mu_\Sigma(z')=1.
\tag{GB7}
\]

The two endpoints use the same factor. This is symmetric balancing, rather than dividing each row by its own degree. The result is a self-adjoint Markov contraction on the one fixed carrier \(L^2(\mu_\Sigma)\).

Whiten the proximity metric and diagonalize the remaining covariance. Choose an orthogonal \(O\) with

\[
O^TC^{-1/2}\Sigma C^{-1/2}O
=\operatorname{diag}(\tau_1,\ldots,\tau_d),
\quad w=O^TC^{-1/2}z,\quad \tau_j>0.
\tag{GB8}
\]

Then the state is a product of \(N(0,\tau_j)\), while the proximity exponent is \(-|w-w'|^2/(4\epsilon)\). Put

\[
r_j=\sqrt{1+(\epsilon/\tau_j)^2}-\epsilon/\tau_j
=e^{-\operatorname{arsinh}(\epsilon/\tau_j)},\qquad
1-r_j^2=\frac{2\epsilon r_j}{\tau_j}.
\tag{GB9}
\]

The balancing factor is explicit:

\[
\boxed{
a_\epsilon(w)
=\prod_j(1-r_j^2)^{-1/4}
\exp\left[\sum_j\frac{r_jw_j^2}{2\tau_j(1+r_j)}\right].}
\tag{GB10}
\]

Substitution into (GB7), including its constants, gives the transition

\[
\boxed{w_j'\mid w\sim
N(r_jw_j,\tau_j(1-r_j^2)),
\quad\text{independently over }j.}
\tag{GB11}
\]

These variances and means preserve the specified state at every \(\epsilon>0\). Equivalently the kernel relative to that state is

\[
Q_\epsilon(w,w')
=\prod_j(1-r_j^2)^{-1/2}
\exp\left[
-\sum_j\frac{r_j^2(w_j^2+(w_j')^2)-2r_jw_jw_j'}
{2\tau_j(1-r_j^2)}\right].
\tag{GB12}
\]

This formula proves normalization directly by Gaussian integration. It is the product Mehler kernel. For example, as \(\epsilon\downarrow0\), the quadratic exponent of \(a_\epsilon\) tends to \(\tfrac14 z^T\Sigma^{-1}z\): apart from its width-dependent scalar, the balancing factor approaches the reciprocal square root of the state density. Its exact finite-width value, rather than that asymptotic replacement, is required for (GB7).

The balancing factors can be unbounded, but the returned operator is bounded. On compactly supported functions, the positive-definite Gaussian kernel makes the quadratic form of \(Q_\epsilon\) nonnegative after multiplication by \(a_\epsilon\). Markov contractivity and density then extend positivity to the complete \(L^2(\mu_\Sigma)\) carrier. Thus \(0\le Q_\epsilon\le I\).

Within centered Gaussian endpoint factors with an integrable balanced joint density, (GB10) is forced. To see the possible matrix ambiguity, in the whitened coordinates write the effective source precision as \(U>0\). Balancing requires

\[
U+(U^{-1}+2\epsilon I)^{-1}
=\operatorname{diag}(\tau_j^{-1}).
\tag{GB13}
\]

The left side is a strictly increasing scalar function of \(U\). Hence \(U\) commutes with the specified covariance and its positive eigenvalues are uniquely determined. In each direction the effective source variance is \(\tau_j(1+r_j)\). Normalization then fixes the positive scalar in (GB10). This argument does not assert a classification of arbitrary non-Gaussian kernels.

## One scalar clock forces the covariance cometric

All the balanced operators above commute and share the product Hermite basis. That fact alone does not make their one-parameter family a semigroup. Their mean multipliers are the \(r_j(\epsilon)\) in (GB9).

Impose the additional requirement that there exist one continuous strictly increasing reparameterization \(t=h(\epsilon)\), from \([0,\infty)\) onto itself with \(h(0)=0\), for which

\[
Q_{h^{-1}(t)}Q_{h^{-1}(s)}
=Q_{h^{-1}(t+s)}.
\tag{GB14}
\]

This requirement uses the complete fixed state and the same width in every direction. It permits no independently adjusted directional widths, extra interactions or width-dependent cometric.

**Within this family, (GB14) holds if and only if \(C=c\Sigma\) for some \(c>0\).** Indeed, restriction to the first Hermite mode in direction \(j\) gives a continuous multiplicative function of \(t\), so

\[
\operatorname{arsinh}(\epsilon/\tau_j)=\omega_j h(\epsilon),
\qquad\omega_j>0.
\tag{GB15}
\]

One nonconstant first mode already makes \(h\) smooth through (GB15); smoothness need not be independently postulated.

For two directions, \(\operatorname{arsinh}(\epsilon/\tau_i)/\operatorname{arsinh}(\epsilon/\tau_j)\) must be independent of \(\epsilon\). The linear coefficients of \(\operatorname{arsinh}(\epsilon/\tau)=\epsilon/\tau-\epsilon^3/(6\tau^3)+O(\epsilon^5)\) fix that ratio as \(\tau_j/\tau_i\). The cubic coefficients then force \(\tau_i^2=\tau_j^2\), hence \(\tau_i=\tau_j\). Thus \(C^{-1/2}\Sigma C^{-1/2}=c^{-1}I\).

Conversely, for \(C=c\Sigma\), all multipliers equal

\[
r=e^{-t},\qquad t=\operatorname{arsinh}(c\epsilon),
\qquad \epsilon=\frac{\sinh t}{c}.
\tag{GB16}
\]

Equation (GB11) becomes \(z'=e^{-t}z+\sqrt{1-e^{-2t}}\,\xi\), with an independent \(\xi\sim N(0,\Sigma)\). Composing these Gaussian transitions multiplies their means and adds their conditional covariances, giving exactly (GB14). In width coordinates, composition is

\[
\epsilon\star\eta
=\epsilon\sqrt{1+c^2\eta^2}
+\eta\sqrt{1+c^2\epsilon^2}.
\tag{GB17}
\]

The common clock normalization remains free: multiplying \(t\) by a positive constant changes the numerical generator by its inverse. The theorem restricts the relative response geometry. [[rg-covariance-residue/gaussian-readout-naturality|Gaussian readout naturality]] supplies the distinct analysis of what compatible linear readouts require; scalar-clock sewing here is a condition on a whole family of actual comparison kernels.

## The full return has an unbounded Hermite clock

With the canonical \(t\) in (GB16), the exact semigroup on \(L^2(\mu_\Sigma)\) is

\[
Q_t=e^{-tH_\Sigma},\qquad
H_\Sigma=-\Sigma:\nabla^2+z\cdot\nabla.
\tag{GB18}
\]

Finite Hermite spans form an operator core. A Hermite polynomial of total degree \(m\) has eigenvalue \(m\), and these polynomials form a complete orthogonal basis. Thus

\[
\sigma(H_\Sigma)=\{0,1,2,\ldots\},\qquad
\operatorname{mult}(m)=\binom{d+m-1}{m},\qquad
\ker H_\Sigma=\mathbb C1.
\tag{GB19}
\]

The closed form is \(\int (\nabla f)^T\Sigma\nabla f\,d\mu_\Sigma\); the spectral domain is the set of Hermite expansions with square-summable coefficients after multiplication by their degrees. A positive lower edge and the entire unbounded ladder follow from this stated process. A Gaussian state alone still does not select them.

For a general fixed \(C\), (GB11) also gives the small-width differential limit (GB6) on Hermite polynomials. Its directional linear rates are \(1/\tau_j\). Exact finite-width scalar-clock closure is the stronger property proved above; failure of (GB14) does not exclude such an infinitesimal diffusion limit.

Each finite-duration transition makes a Gaussian displacement with unbounded support. The infinitesimal generator is a local differential operator on this configuration space. Neither statement supplies spacetime locality, a finite propagation cone or physical translation generators. Its one-parameter reflection positivity follows from
\(\sum_{i,j}\langle f_i,Q_{t_i+t_j}f_j\rangle=\|\sum_iQ_{t_i}f_i\|^2\ge0\).

[[directed-analytic-realization/purification-fluctuation-and-the-oscillator-return|The purification fluctuation return]] owns the subsequent Gaussian-to-oscillator operator algebra and its distinctions from physical fields. The present parent is a balanced proximity law, rather than the purification construction.

## Resolving a correlated pair need not split its rates

For \(\Sigma_\rho=\begin{psmallmatrix}1&\rho\\\rho&1\end{psmallmatrix}\), \(0\le\rho<1\), the normalized coordinates

\[
y_\pm=\frac{z_1\pm z_2}{\sqrt{2(1\pm\rho)}}
\tag{GB20}
\]

give independent standard Gaussians. With \(C=\Sigma_\rho\), (GB18) becomes the same two-coordinate number operator at every \(\rho<1\). Both resolved linear modes have rate one, even while the unnormalized difference concentrates as \(\rho\uparrow1\). At \(\rho=1\) the original covariance is singular and outside the theorem; the nonsingular resolved carrier and its explicit comparisons are what remain fixed.

This contrasts with [[resolved-relative-boundary-and-two-clock-limits|the conditional-refresh construction]], where a resolved Gaussian state retained two incompatible clock scales. It supplies a concrete alternative processing law and a precise reason for its different return. It is not a proof that either Gaussian proximity or the balancing factor is induced by the original sewn group overlap. Constructing that connection, with its full boundary indices and refinement maps, remains open.

[[receipts/gaussian_overlap_balancing_receipt.py|The Gaussian balancing receipt]] checks exact rational Gaussian precision matrices, a noncommuting covariance/cometric example, balancing constants, scalar-clock sewing, and an unequal-direction obstruction. Its checks validate the displayed finite formulas; the classification and complete Hermite statements follow from the arguments above.

[[gaussian-sewing-rigidity|The fixed-state rigidity theorem]] now removes the Gaussian state ansatz: one exact square within this constant-metric scalar-width family forces a Gaussian density. [[quartic-overlap-sewing-tangent|The quartic tangent]] identifies a non-Gaussian composition defect, while [[interacting-comparison-refinement|positive interacting refinement]] still returns a full evolution from smaller steps. Exact closure of this proximity formula and existence of interacting dynamics are separate questions.
