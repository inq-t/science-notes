# The Grain--Acoustic Characteristic

The sharpest CMB target found in the causal-grain search is a dimensionless characteristic equation for the angular acoustic count \(q_*:=\theta_*^{-1}=D_M(z_*)/r_s(z_*)\). It reuses only the programme's already selected spatial dimension \(3\), unit/rank-two coefficient \(\kappa_g=4\zeta=8/3\), and logarithmic grain depth \(\Sigma_c=\ln(R_c/\lambda_*)\):

$$
\boxed{
q_*\left(q_*^2+\frac83\right)
\stackrel{?}{=}
\left(3+\Sigma_c\right)^3.
}
$$

At the present central inputs this relation is extraordinarily close, and after the optional chiral clause CH3 it becomes a local-laboratory-to-CMB oracle in which \(H_c\), \(R_c\), \(\lambda_*\), and \(E_*\) all cancel. That economy makes it a valuable frozen theorem target. It is nevertheless a **post-search conjecture**, not present evidence: the integer shift, the reuse of \(8/3\), the chiral midpoint, and the compared CMB-conditioned branch were all noticed after inspecting the numbers, and current uncertainty is far too large to resolve the tiny cubic correction.

## The numerical clue

Write the angular sound-horizon ratio as

$$
q_*
:=
\frac{1}{\theta_*}
=
\frac{D_M(z_*)}{r_s(z_*)},
\qquad
\ell_A:=\pi q_*.
$$

The bundled Planck baseline best fit gives

$$
100\theta_*=1.041085,
\qquad
q_*^{\mathrm{obs}}=96.0536363505,
\qquad
\ell_A^{\mathrm{obs}}=301.761398309.
$$

The unit, rank-two common-count branch evaluated at the packet's CMB-conditioned crossing rate \(H_c=83.1058\,\mathrm{km\,s^{-1}\,Mpc^{-1}}\) gives

$$
\lambda_*=4.264251464\,\mathrm{fm},
\qquad
\Sigma_c
:=
\ln\frac{R_c}{\lambda_*}
=93.0628842654.
$$

The first clue is therefore

$$
q_*^{\mathrm{obs}}-\Sigma_c
=2.9907520852
\simeq3.
$$

This is an **observation-driven clue**. The \(H_c\) value on the right belongs to a CMB-conditioned homogeneous branch, so this comparison is not an independent prediction. It merely asks whether the nearby integer \(3\) has a structural owner.

One candidate owner exists in the critical-kernel theorem, but only after another correspondence is declared. For a weight-zero scalar in \(d\) spatial dimensions, a dilation \(x\mapsto e^s x\) sends its Fourier coefficient to

$$
\zeta_{\mathbf k}
\longmapsto
e^{ds}\zeta_{e^s\mathbf k}.
$$

A primitive log-scale interval \(\delta\sigma_g=1\) therefore contributes \(d\delta\sigma_g=3\) to the logarithmic Fourier-coefficient weight when \(d=3\). This makes

$$
L_g
\stackrel{?}{=}
\Sigma_c+d\delta\sigma_g
=
\Sigma_c+3
$$

a plausible Mellin/Fourier descent label. Identifying the response weight \(s_*=1\) from the unit-nat channel with the interval \(\delta\sigma_g=1\) is itself the unit-wall correspondence, not a notational identity. Nor does the critical theorem prove the affine shift: it concerns the transformation of a Fourier coefficient and precision kernel, whereas \(\Sigma_c\) is a total scale ratio and \(q_*\) is an acoustic projection ratio. An explicit carrier-changing Mellin-to-spatial-spectral map must show that these logarithms add.

## The unit-free grain dictionary

Let

$$
\kappa_g:=4\zeta,
\qquad
\lambda_*^3
=
\kappa_g\ell_P^2R_c,
\qquad
R_c:=\frac{c}{H_c}.
$$

On the unit, rank-two branch,

$$
s_*=1,
\qquad
\gamma=2,
\qquad
\zeta=\frac{\gamma s_*}{3}=\frac23,
\qquad
\kappa_g=\frac83.
$$

Define the relative grain, its reciprocal quality, and its logarithmic depth by

$$
g_c:=\frac{\lambda_*}{R_c},
\qquad
Q_c:=g_c^{-1},
\qquad
\Sigma_c:=\ln Q_c=-\ln g_c.
$$

The common-count law then has the equivalent dimensionless presentations

$$
\boxed{
Q_c
=
\frac{R_c}{\lambda_*}
=
\frac{\omega_*}{H_c}
=
\frac{E_*}{\hbar H_c}
=
\frac{\beta_cE_*}{2\pi}
=
\left(\frac{3\iota_c}{8\pi}\right)^{1/3}
=
\left(\frac{3}{8\alpha_H}\right)^{1/3},
}
$$

where

$$
\omega_*:=\frac{c}{\lambda_*},
\qquad
E_*:=\hbar\omega_*=\frac{\hbar c}{\lambda_*},
\qquad
\beta_c:=\frac{2\pi}{\hbar H_c},
\qquad
\iota_c:=\frac{\pi R_c^2}{\ell_P^2},
\qquad
\alpha_H:=\frac{G\hbar H_c^2}{c^5}.
$$

Thus

$$
\boxed{
\Sigma_c
=
\ln\frac{E_*}{\hbar H_c}
=
\ln\frac{\beta_cE_*}{2\pi}
=
\frac13\ln\frac{3\iota_c}{8\pi}
=
-\frac13\ln\!\left(\frac83\frac{G\hbar H_c^2}{c^5}\right).
}
$$

This is the requested cancellation ledger. Length, duration, frequency, energy, KMS inverse energy, areal information, and gravitational coupling are different presentations of one unit-free ratio. The equalities are exact **conditional on the common-count and Einstein-area clauses**. The notation \(\beta_c\) remains KMS-motivated until a state and automorphism flow are constructed; \(\iota_c\) is an areal ledger and is not silently identified with every notion of entropy or information.

## The minimal odd cubic

Set

$$
L_g:=3+\Sigma_c=3-\ln g_c.
$$

The proposed acoustic characteristic is

$$
\boxed{
\mathscr P_g(q)
:=
q(q^2+\kappa_g),
\qquad
\mathscr P_g(q_*)=L_g^3.
}
$$

This is the minimal polynomial ansatz simultaneously carrying four pieces of programme structure:

1. **orientation-compatible form:** \(\mathscr P_g\) is odd, so a future signed spectral generator could reverse under \(\mathscr D_g\mapsto-\mathscr D_g\);
2. **critical three-dimensional scaling:** its principal term is \(q^3\), matching the order-three kernel selected for a weight-zero scalar on a three-dimensional cut;
3. **positive local factor:** on the selected positive branch, \(q^2+\kappa_g>0\);
4. **no new continuous coefficient:** the lower-order coefficient is the same \(\kappa_g=4\zeta=8/3\) already appearing in the common-count law.

A possible operator target is therefore

$$
\mathscr D_g
\left(\mathscr D_g^2+4\zeta\right),
$$

restricted to its positive oriented sector. No such physical operator, domain, boundary condition, or CMB eigenvalue map has yet been constructed. Reusing \(4\zeta\) is economical only if that construction forces the reuse; today it is a discrete model choice made after seeing the clue.

Oddness does not itself supply causal direction. The observed ratio \(q_*=D_M/r_s\) is strictly positive and has no constructed negative causal counterpart. Directedness would require an operator involution or semigroup orientation whose positive spectral branch maps to \(q_*\).

The cubic has a unique positive root. Its exact hyperbolic form is

$$
q_*
=
2\sqrt{\frac{\kappa_g}{3}}
\sinh\!\left[
\frac13\operatorname{arsinh}\!\left(
\frac{3\sqrt3}{2\kappa_g^{3/2}}L_g^3
\right)
\right].
$$

For \(\kappa_g=8/3\),

$$
q_*
=
\frac{4\sqrt2}{3}
\sinh\!\left[
\frac13\operatorname{arsinh}\!\left(
\frac{27}{32\sqrt2}L_g^3
\right)
\right].
$$

The reason this form matters is algebraic, not decorative:

$$
\sinh 3s=4\sinh^3s+3\sinh s.
$$

The positive cubic is a noncompact triple-angle law. [[inbox/de-sitter-box-and-the-octonionic-ladder/de-sitter-box-and-the-octonionic-ladder|The de Sitter box]] supplies the compact counterpart: its trace-free horizon cubic is solved by \(\cos3\theta\), with three roots at \(120^\circ\) phase separations. [[inbox/causal-grain-cmb-spectroscopy/scale-phase-harmonic-descent|Scale--phase harmonic descent]] develops this noncompact/compact relation without pretending that a formal real-form change is already a physical map.

For \(L_g\gg1\),

$$
q_*
=
L_g-\frac{\kappa_g}{3L_g}+O(L_g^{-3}).
$$

Thus the raw integer clue \(q_*\simeq\Sigma_c+3\) is the leading term, while the already-owned coefficient \(8/3\) supplies the first small correction. At the CMB-conditioned central values,

$$
q_*^{\mathrm{cubic}}
=96.0536310674,
$$

only \(5.28\times10^{-6}\) below the bundled best-fit value. Equivalently,

$$
100\theta_*^{\mathrm{cubic}}
=1.0410850573.
$$

Solving for the coefficient from the central values gives

$$
\kappa_{\mathrm{central}}
:=
\frac{L_g^3-(q_*^{\mathrm{obs}})^3}{q_*^{\mathrm{obs}}}
=2.665144125,
$$

which is \(0.0571\%\) below \(8/3\). This numerical closeness must not be overread. Planck quotes \(100\theta_*=1.04109\pm0.00030\) for a closely related TT,TE,EE+lowE combination, corresponding to an uncertainty of about \(0.028\) in \(q_*\), over five thousand times the displayed central residual. Holding \(\Sigma_c\) fixed for illustration, that uncertainty induces order-\(8\) sensitivity in a coefficient inferred through the cubic. This is not a coefficient posterior: because \(H_c\) is itself CMB-conditioned, a real constraint requires the joint \((\theta_*,H_c)\) covariance from one matching likelihood. The data do not presently distinguish \(\kappa_g=8/3\) from a broad range of order-one corrections.

## The fully cancelled chiral oracle

The optional chiral clause CH3 proposes

$$
E_*^2
\stackrel{?}{=}
\frac{F_\pi^\chi E_{\pi^\pm}}{6},
$$

where \(F_\pi^\chi\) and \(E_{\pi^\pm}=m_{\pi^\pm}c^2\) are both read in energy units. The common-count law is equivalently

$$
H_c
=
\frac{8GE_*^3}{3\hbar^2c^5}.
$$

Combining them removes both the cosmic rate and the intermediate grain energy:

$$
Q_c
=
\frac{E_*}{\hbar H_c}
=
\boxed{
\frac{9\hbar c^5}{4G F_\pi^\chi E_{\pi^\pm}}
}.
$$

The acoustic conjecture becomes the compact laboratory-to-sky oracle

$$
\boxed{
q_*\left(q_*^2+\frac83\right)
\stackrel{?}{=}
\left[
3+\ln\!\left(
\frac{9\hbar c^5}
{4G F_\pi^\chi E_{\pi^\pm}}
\right)
\right]^3.
}
$$

Using the packet's current CH3 central prescriptions gives

$$
q_*^{\chi\pi}=96.053514309,
\qquad
100\theta_*^{\chi\pi}=1.041086323.
$$

The central \(100\theta_*\) value is \(1.27\) parts per million above the bundled best fit. This spectacular-looking number is **not a significance statement**. CH3 chose the pion datum, divisor \(3\), and midpoint form after the grain search; the cubic chose the shift and coefficient after the acoustic comparison; the decay-constant uncertainty is much larger than the central residual. The equation becomes evidential only after its structural maps are derived and its choices are frozen before a held-out measurement.

## Why the equation is geometrically motivated but not derived

Three exact antecedents make the conjecture worth preserving:

| Antecedent | Exact content | What it does not yet supply |
|---|---|---|
| [[critical-scale-kernels/curved-p3-representative|critical \(P_3\)]] | on round \(S^3\), the eigenvalue is \(R^{-3}\ell(\ell+1)(\ell+2)=R^{-3}(n^3-n)\) for \(n=\ell+1\) | no theorem identifies \(q_*\), \(\Sigma_c\), or the CMB transfer problem with that spectrum |
| [[inbox/de-sitter-box-and-the-octonionic-ladder/de-sitter-box-and-the-octonionic-ladder|de Sitter \(A_2\) box]] | a trace-free cubic organizes three horizon branches as one cosine sampled at \(2\pi/3\) | no box-spectrum functor maps its roots to acoustic peaks |
| [[binary-information-geometry/witten-darboux|Witten--Darboux factorization]] | a positive second-order factor has a reflectionless continuum with unit-modulus transmission phase | no covariant weld identifies its internal momentum with a curvature or acoustic mode |

The antecedents motivate an odd order-three characteristic, a positive quadratic factor, and a cubic-to-phase reading. They do **not** derive the particular affine label

$$
L_g=\Sigma_c+3,
$$

nor the use of \(4\zeta\) as the lower-order coefficient. In particular:

1. the natural round-\(S^3\) shift in \(P_3\) is \(n=\ell+1\), not \(\Sigma+3\);
2. \(4\zeta\) is the bulk/area common-count coefficient, not yet a proved curvature coefficient;
3. \(q_*=D_M/r_s\) is a projected acoustic ratio, not already an eigenvalue of \(P_3\).

These are the three required welds.

## What this could explain

The equation targets the **fundamental acoustic count**, not the entire Einstein--Boltzmann transfer function. If it were derived, it would fix

$$
\ell_A=\pi q_*,
\qquad
\ell_m^{\mathrm{ideal}}\simeq m\pi q_*.
$$

That is the common ruler behind the harmonic comb. Baryon loading, gravitational driving, neutrino free streaming, recombination width, diffusion, and projection then determine line strengths and calculable departures from integer spacing. This is close to the spectroscopic analogy: the characteristic fixes the common ladder, while the local photon--baryon geometry supplies splitting, phase shifts, amplitudes, and linewidths.

It does not by itself explain the photon--baryon relational geometry. A strong explanation must still derive the histories \(H(N)\), \(R(N)=3\rho_b/(4\rho_\gamma)\), opacity, and recombination, so that \(D_M\) and \(r_s\) are separately computed rather than merely constrained through their ratio.

## Frozen test protocol

The conjecture becomes a real low-parameter model only under the following order of work:

1. construct an invariant oriented operator whose positive-sector characteristic is \(q(q^2+4\zeta)\);
2. derive, rather than fit, the spectral label \(L_g=3+\Sigma_c\);
3. fix \(Q_c\) without the tested CMB acoustic data, either from a genuine wall construction or from the already frozen chiral clause;
4. predict \(\theta_*\), then propagate one phase through a standard or independently derived Boltzmann transfer calculation;
5. hold out TT, TE, EE peak phases, BAO ratios, lensing, or a future acoustic-scale determination;
6. count the present search choices in any statistical comparison.

The target fails if the operator cannot be built, if its shift or coefficient must be retuned by data set, if an independently selected \(Q_c\) predicts the wrong acoustic angle, or if the detailed TT/TE/EE spectra require independent phase corrections not generated by the shared transfer law.

[[inbox/causal-grain-cmb-spectroscopy/grain_acoustic_characteristic_receipts.py|The companion receipt]] checks every displayed cancellation and central-value calculation. It certifies arithmetic, not the characteristic equation, its statistical significance, or its physical interpretation.
