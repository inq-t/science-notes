# Preparation Rank Controls the Returned Locality

A Gaussian comparison that is sharply localized before averaging need not remain local after its preparation is integrated out. For a shared complex preparation of rank \(m\), its small-norm tail competes with the dimension \(d\) of the retained configuration space. This yields an exact hierarchy: ordinary diffusion, a logarithmically paced diffusion, nonlocal jump motion, or failure to approach an identity transition. The dimension here counts configuration directions, not spacetime dimensions.

**Status: exact normalization and smooth-core generator limits for the compact homogeneous family below.** Preparation rank, comparison geometry and duration convention remain inputs. The result extends the negative-moment test in [[relative-multiplication-transfer-and-the-rotor-limit|the relative transfer]] and applies to [[spatial-word-comparison-and-mixed-motion|spatial word comparisons]]. It does not establish a field-theory continuum limit.

## One scalar preparation shared across a configuration

Let \(K\) be a compact connected Lie group of dimension \(d>0\), with normalized Haar measure. Choose a smooth function \(h\geq0\) such that
\[
h(g^{-1})=h(g),\qquad h^{-1}(0)=\{e\},\qquad
h(\exp X)=X^\mathsf TMX+O(|X|^4),\quad M>0.
\tag{PL1}
\]
Write \(dg=c_K[1+O(|X|^2)]dX\) near the identity. A squared distance between equivariant embedded configurations supplies such examples. If positivity as an operator is required, that embedding also supplies it by the Gaussian Fourier representation; (PL1) alone specifies a symmetric Markov kernel, not operator positivity.

Let \(S\sim\operatorname{Gamma}(m,1)\), \(m>0\). An isotropic complex Gaussian preparation with \(m\) independent components realizes integer \(m\). Set
\[
k_\alpha(g)=\mathbb E e^{-\alpha S h(g)}
=(1+\alpha h(g))^{-m},\quad
z_\alpha=\int_Kk_\alpha(g)dg,\quad
P_\alpha f(q)=z_\alpha^{-1}\int_Kk_\alpha(g)f(qg)dg.
\tag{PL2}
\]
Haar measure is stationary. The same \(S\) is shared among every component of this one comparison. Independent preparations for separate components instead multiply their kernels and define another law.

## Too little preparation rank prevents localization

If \(m<d/2\), the singularity \(h^{-m}\) is Haar integrable. Dominated convergence gives
\[
\alpha^m z_\alpha\longrightarrow Z_m:=\int_Kh(g)^{-m}dg,
\qquad
\frac{k_\alpha}{z_\alpha}
\longrightarrow\frac{h^{-m}}{Z_m}\quad\text{in }L^1(K).
\tag{PL3}
\]
Indeed, \(\alpha^m k_\alpha=(\alpha^{-1}+h)^{-m}\leq h^{-m}\), and near the identity integrability is precisely \(\int_0^\epsilon r^{d-1-2m}dr<\infty\). Consequently \(P_\alpha\) converges in operator norm on every \(L^p\), \(1\leq p\leq\infty\), to a nonlocal averaging operator, rather than to the identity.

Thus this family cannot have a finite infinitesimal generator on all smooth functions under a duration per step tending to zero. Increasing \(\alpha\) mainly selects unusually small preparations, instead of forcing nearby configurations. A fixed positive duration still defines a valid discrete process.

## Finite second localization moments return diffusion

For \(m>d/2\), localization does occur, with
\[
z_\alpha\sim J_m\alpha^{-d/2},\qquad
J_m=\frac{c_K\pi^{d/2}\Gamma(m-d/2)}
{\sqrt{\det M}\,\Gamma(m)}.
\tag{PL4}
\]
This follows by \(Y=\sqrt\alpha X\); the limiting density is proportional to \((1+Y^\mathsf TMY)^{-m}\). Its second moment is finite exactly when \(m>d/2+1\). In that regime, for smooth \(f\),
\[
\boxed{
\alpha(P_\alpha-I)f\longrightarrow
\frac{1}{4(m-d/2-1)}\Delta_M f,
\qquad
\Delta_M=\sum_{i,j}(M^{-1})_{ij}\mathsf X_i\mathsf X_j.
}
\tag{PL5}
\]
Here \(\mathsf X_i f(q)=\left.\partial_t f(qe^{te_i})\right|_0\). They are left-invariant fields, defined by right multiplication of the argument, and are skew-adjoint in Haar measure. The symmetric coefficients in \(\Delta_M\) remove any ambiguity from their ordering.

To check the constant, transform \(Y\) by \(M^{1/2}\). The normalized second moment is
\[
\frac{\int Y_iY_j(1+Y^\mathsf TMY)^{-m}dY}
{\int(1+Y^\mathsf TMY)^{-m}dY}
=\frac{(M^{-1})_{ij}}{2(m-d/2-1)}.
\tag{PL6}
\]
Inversion symmetry cancels the odd Taylor terms. Dominated convergence using the finite second moment controls the Taylor remainder and gives uniform convergence for each smooth \(f\). A fourth-moment error estimate needs the stronger inequality \(m>d/2+2\); it is not implicit in (PL5).

More generally, for a positive shared \(S\), the same argument with finite \(\mathbb E S^{-d/2-1}\) gives the coefficient
\[
\frac14\frac{\mathbb E S^{-d/2-1}}
{\mathbb E S^{-d/2}}.
\tag{PL7}
\]
For the Gamma law this is (PL5). A full-rank non-isotropic complex Gaussian has the same inverse-moment threshold, although the ratio is different.

## At the threshold the clock changes pace

At \(m=d/2+1\), the normalized second moment diverges logarithmically. Its truncation at \(|Y|=O(\sqrt\alpha)\) gives
\[
\boxed{
\frac{\alpha}{\log\alpha}(P_\alpha-I)f
\longrightarrow\frac14\Delta_Mf.
}
\tag{PL8}
\]
For the constant, after the same linear transformation, the angular second moment is \(|S^{d-1}|/d\), and the radial integral is \(\log\sqrt\alpha+O(1)\). Dividing by \(\int(1+|Y|^2)^{-d/2-1}dY=\pi^{d/2}/\Gamma(d/2+1)\) gives \(\tfrac12\log\alpha\) for each diagonal second moment. The Taylor coefficient supplies the further \(1/2\).

Split the integral into a small coordinate neighborhood and its complement. The complement and the fourth-order local remainder are \(O(\alpha^{-1})\) after normalization, hence vanish at pace \(\alpha/\log\alpha\). The quartic correction to \(h\) and quadratic Haar correction have the same bound. This proves the smooth-core limit, rather than merely a divergent-moment diagnosis.

The required nontrivial pace is a mathematical return up to a common constant. Its identification with physical duration remains a separate calibration.

## Intermediate rank returns jumps

Let \(s=m-d/2\in(0,1)\). For smooth \(f\),
\[
\alpha^s(P_\alpha-I)f(q)
\longrightarrow
\frac1{2J_m}\int_K
\frac{f(qg)+f(qg^{-1})-2f(q)}{h(g)^m}\,dg.
\tag{PL9}
\]
The symmetric difference is \(O(|X|^2)\); its radial majorant is \(r^{1-2s}dr\), which is integrable. Equation (PL4) and dominated convergence prove the formula. This operator has a jump kernel with local singularity \(|X|^{-d-2s}\). It is not an ordinary second-order differential generator; nor is it automatically the spectral fractional power of the Laplacian on the whole group.

At \(m=d/2\), replace the pace \(\alpha^s\) in (PL9) by \(\log\alpha\), and replace \(J_m\) by
\[
J_{\rm crit}=\frac{c_K\pi^{d/2}}
{\sqrt{\det M}\,\Gamma(d/2)},\qquad
z_\alpha\sim J_{\rm crit}\alpha^{-d/2}\log\alpha.
\tag{PL10}
\]
The same dominated numerator argument applies. The kernel now has an order-zero logarithmic singularity. Although \(P_\alpha\to I\), its infinitesimal return remains nonlocal.

The negative of either displayed jump generator has quadratic form
\[
\mathcal E(f)=\frac1{2J}\int_{K\times K}
h(g)^{-m}|f(qg)-f(q)|^2\,dq\,dg,
\tag{PL11}
\]
with the corresponding \(J\). This is positive. These core formulas do not claim norm convergence of transfer powers or a uniform estimate over growing groups.

## A concrete constraint on growing multiplication diagrams

On \(N\) independent \(SU(2)\) frame coordinates, \(d=3N\). Suppose one complex \(M_2\) preparation is shared across an embedding of all the word comparisons, so the squared comparison reduces to \(S h\), with \(S\sim\operatorname{Gamma}(4,1)\), and the embedding has nondegenerate tangent metric.

- One frame has ordinary diffusion: \(4>3/2+1\).
- Two frames are critical: \(4=6/2+1\), requiring the logarithmic pace (PL8).
- Three or more frames fail to localize: \(4<3N/2\), by (PL3).

Two independent \(M_2\) copies, jointly shared across the comparisons, give \(m=8\). This repairs the ordinary two-frame diffusion but eventually encounters the same obstruction as \(N\) grows. For a single globally shared scalar preparation, ordinary diffusion needs
\[
m>\frac{3N}{2}+1.
\tag{PL12}
\]
This is a constraint on this preparation architecture, not a universal rule relating matter species to spacetime dimension. If the comparison loses tangent directions, or a gauge quotient changes the carrier, the effective dimension and nondegeneracy must be checked again.

A viable field programme can instead test preparations assigned to bounded incidence neighborhoods, a preparation norm bounded away from zero, or a rank law growing with retained configuration dimension. These are distinct constitutive proposals. Local preparations must still pass the inherited-covariance, unit and source-sewing tests of [[marked-gaussian-constraints-and-sewing-measures|marked Gaussian constraints]]. Independently redrawing one global preparation in each subregion would change the joint law.

The constructive conjecture is that an admissible multiplication diagram determines both its preparation inventory and its comparison metric in a way stable under refinement. The present theorem supplies a discriminating test: positivity and algebraic coverage alone do not guarantee a local infinitesimal return, because integration over nearly invisible preparations can change the order of motion.
