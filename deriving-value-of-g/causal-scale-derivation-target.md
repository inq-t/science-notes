# The Causal-Scale Derivation Target

Causal Scale Dynamics can derive \(G\) only by constructing a scale-indexed causal-wall state, calculating its finite horizontal BKM norm per independently calibrated area, and proving that this coefficient is the universal horizon entropy density that controls Einstein focusing. The present binary geometry and unit Ruble law specify the desired answer's form but do not yet supply its dimensional magnitude.

## The object to construct

For each admissible causal cut \(\Sigma_N\), the theory needs data of the form

$$
N\longmapsto
(\Sigma_N,\mathcal A_N,\omega_N,\mathcal T_{N_2N_1}),
$$

where \(\mathcal A_N\) is a wall or causal-region algebra, \(\omega_N\) is a suitable state, and \(\mathcal T_{N_2N_1}\) transports states or observables to a common algebra before two scales are compared. Without this transport, \(\partial_N\omega_N\) and cross-scale relative entropy are not well typed. [[wall-construction-interface/cross-fiber-transport|Cross-fiber transport and state selection]] and [[causal-wall-spectral-theory/causal-scale-interface|the causal-scale interface]] state the broader operator-algebraic obligations.

After removing central normalization and vertical modular-frame directions, require a twice-differentiable horizontal family with a finite coincidence Hessian, or the corresponding regular operator-algebraic notion, so that

$$
D(\omega_{N+\delta N}\Vert\omega_N)
=\frac12G^{\perp}_{NN}[\Sigma_N,N]\,\delta N^2
+o(\delta N^2).
$$

The exact relation between a regular relative-entropy Hessian and the BKM metric is explained in [[basic-concepts/hessians/entry|Hessians]]. It does not guarantee that the full continuum wall theory has a finite extensive coefficient.

Define

$$
\chi_{\downarrow}[\Sigma_N,N]
:=\frac{G^{\perp}_{NN}[\Sigma_N,N]}{A_{\Sigma_N}}.
$$

Keep this distinct from the [[areal-information-modulus|Einstein entropy--area density]]

$$
\eta_{\mathrm E}
:=\frac{\mathrm d(S_{\mathrm{hor}}/k_B)}{\mathrm dA}.
$$

The relevant calculation is the extensive normalization, not merely the unit binary profile. The reduced balanced channel gives

$$
G^{\mathrm{BKM}}_{\theta\theta}
=\operatorname{sech}^2\theta
$$

per canonically normalized effective channel. It does not determine how many physical channels occur per square metre, which is precisely the missing dimensional content of \(\chi_{\downarrow}\).

It also does not equal the entanglement capacity of the same balanced binary state. For

$$
\rho_\theta=\frac{e^{\theta Q}}{2\cosh\theta},
$$

one has

$$
g^{\mathrm{BKM}}_{\theta\theta}
=\operatorname{sech}^2\theta,
\qquad
\operatorname{Var}_{\rho_\theta}(-\ln\rho_\theta)
=\theta^2\operatorname{sech}^2\theta.
$$

The first is one at the self-dual point and the second is zero. Any derivation must therefore keep the physical scale tangent distinct from the replica-temperature tangent until an alignment theorem is proved.

Write this distinction invariantly as

$$
v_N=\lambda v_{\mathrm{escort}}+v_\perp,
\qquad
g_{\mathrm{BKM}}(v_\perp,v_{\mathrm{escort}})=0.
$$

Then

$$
G^{\perp}_{NN}
=\lambda^2C_E+\lVert v_\perp\rVert^2.
$$

The unit-capacity claim requires both \(\lvert\lambda\rvert=1\) and \(v_\perp=0\), or a different theorem showing that the full combination equals horizon entropy. Positivity alone proves neither.

## The theorem target

A clean Einstein-universality theorem must first show that the renormalized horizontal norm localizes on a cut. For measurable patches \(U\subset\Sigma\), it should define a positive, countably additive measure

$$
\mu^{\perp}_{\mathrm{BKM}}(U)
:=G^{\perp}_{NN,\mathrm{ren}}[U].
$$

For a declared class \(\mathscr C_{\mathrm E}\) of local equilibrium causal cuts, this measure must be absolutely continuous with respect to the area measure \(\mu_A\), with constant Radon--Nikodym density

$$
\frac{\mathrm d\mu^{\perp}_{\mathrm{BKM}}}
{\mathrm d\mu_A}
=\chi_*>0.
$$

Equivalently, for every point \(p\) and every admissible nested family of regular patches \(U\downarrow p\), after the regulator is removed in a declared continuum prescription,

$$
\lim_{U\downarrow p}
\frac{G^{\perp}_{NN,\mathrm{ren}}[U]}
{A(U)}
=\chi_*,
$$

uniformly throughout the Einstein regime. This local-additivity requirement is stronger than observing large-area extensivity on one cosmological cut. The theorem must then independently establish

$$
\delta\!\left(\frac{S_{\mathrm{hor}}}{k_B}\right)
=\chi_*\,\delta A.
$$

The measure and constant-density conditions construct a local extensive state-space modulus. The entropy-variation equation is the state--geometry weld. Together they give

$$
\chi_*=\eta_{\mathrm E}
$$

and the [[horizon-thermodynamic-route|horizon-thermodynamic implication]] then yields

$$
G_{\mathrm{pred}}
=\frac{c^3}{4\hbar\chi_*}.
$$

Positivity of a nondegenerate BKM metric would give \(\chi_*>0\) and hence, on the positive unit-capacity branch, \(G_{\mathrm{pred}}>0\). It fixes the sign but not the magnitude.

At a self-dual cosmological cut obeying the linear Einstein area law, the same equality is expressed by

$$
\mathfrak R_c
:=\frac{k_B}{S_c}G^{\perp}_{NN}(N_c)
=1.
$$

[[program-core/ruble-equations#RE6 — Integrated crossing capacity|The Einstein-capacity upgrade target]] correctly records this as a conjecture rather than a result.

The [[noether-capacity-theorem|Noether--capacity theorem]] gives a sufficient route to the entropy equation: prove that the physical horizontal state is a unit escort deformation of a genuine \(1+1\) conformal thermal sector whose entropy is the horizon entropy. Conservation of its dilation current then forces \(C_E=S/k_B\). The burden shifts to constructing that sector and tangent rather than merely observing that the cut has a two-dimensional normal plane.

## The anti-circularity test

At a finite self-dual cut, the definitions give

$$
G_{\mathrm{eff}}
=\frac{\mathfrak R_c c^3A_c}
{4\hbar G^{\perp}_{NN}(N_c)}.
$$

On the unit branch \(\mathfrak R_c=1\), this reduces to the proposed prediction. It predicts \(G\) only if \(A_c\), \(G^{\perp}_{NN}\), and the Ruble law are fixed without using the desired coefficient. For a flat FLRW apparent horizon, \(A_c=4\pi c^2/H_c^2\), so the general conditional formula is

$$
G_{\mathrm{eff}}
=\frac{\mathfrak R_c\pi c^5}
{\hbar H_c^2G^{\perp}_{NN}(N_c)}.
$$

The calculation is circular if any of the following supplies the normalization:

- the Bekenstein--Hawking formula with an already measured \(G\);
- the [[conformal-scale-geometry/hawking-friedmann-identity|Hawking--Friedmann bridge]], which contains \(G\) in both horizon entropy and critical density;
- a fitted expansion history used both to define the wall and to infer its supposed source;
- the declaration \(G^{\perp}_{NN}=S_c/k_B\) used as a normalization rather than derived from the wall state; or
- Planck units introduced before the independent area coefficient is calculated.

A noncircular order is

$$
\text{wall algebra and state}
\longrightarrow
\text{renormalized horizontal BKM norm}
\longrightarrow
\chi_*
\longrightarrow
\text{capacity weld}
\longrightarrow
G_{\mathrm{pred}}.
$$

A more ambitious same-tangent route keeps the gravitational kinetic coefficient \(Z_g\) symbolic:

$$
G^{\perp}_{\mathrm{BKM}}(v_N,v_N)
=Z_g\,\mathcal E_{\mathrm{can}}^{(1)}(h[v_N],h[v_N]).
$$

Here \(\mathcal E_{\mathrm{can}}^{(1)}\) is canonical energy computed with a unit-normalized gravitational Lagrangian. If the microscopic wall side, the tangent map \(v_N\mapsto h[v_N]\), and the physical area are all constructed without \(G\), this equality could solve for \(Z_g\); the same covariant Noether structure would then determine the Wald entropy coefficient. Existing holographic BKM--canonical-energy identities demonstrate this architecture only after the gravitational normalization and AdS/CFT dictionary are supplied.

## The dimensional obstruction

The principles

$$
\nu=1,
\qquad
\mathfrak R_c=1
$$

are dimensionless. The constants \(c\), \(\hbar\), and \(k_B\), together with dimensionless mathematics, cannot produce an inverse area without an additional dimensional structure. A full calculation must therefore obtain an intrinsic spectral or geometric area, derive a length relative to another independently fixed physical scale, or admit an areal soldering quotient as new primitive data.

Explicitly,

$$
\left[\frac{c^3}{\hbar}\right]
=LM^{-1}T^{-2},
\qquad
[G]=L^3M^{-1}T^{-2},
$$

so

$$
G=\frac{c^3}{\hbar}\times(\text{area})
$$

up to a dimensionless coefficient.

This is the exact missing content hidden by setting \(c=\hbar=k_B=G=1\). The balanced binary family can fix a shape and a dimensionless normalization; it cannot by itself say how many distinguishable channels exist per square metre.

If the construction uses a measured cosmological radius \(R_c\) to supply \(A_c\), the result may still be a valuable cross-calibration between cosmological state geometry and laboratory gravity. It is not then a derivation from dimensionless first principles alone.

## Universality requirements

The candidate coefficient must be:

- finite and positive after a declared continuum limit;
- independent of regulator and unphysical renormalization conventions;
- invariant under reparameterization of the internal state coordinate;
- independent of the chosen representative cut, observer, and null orientation in the stated Einstein regime;
- local and extensive to the accuracy required by the horizon argument;
- stable under changes of low-energy matter content, or accompanied by a controlled renormalization law;
- computed from off-shell or independently fixed state data rather than the target cosmology; and
- the same coefficient seen by local Newtonian experiments, background Friedmann dynamics, growth and lensing, gravitational waves, and the entropy--area law.

The last condition matters because “\(G\)” can denote inequivalent effective couplings outside ordinary GR. [[compatible-with-existing-physics/cosmic-structure-tests|Tests of cosmic structure]] separates these observational registers.

## Failure modes are physical alternatives

| Result of the calculation | Consequence |
|---|---|
| No finite or scheme-independent \(\chi_{\downarrow}\) | The BKM route does not define a gravitational constant |
| \(\mathfrak R_c\ne1\) | The Scale--Capacity Equivalence Principle is false or must be modified |
| \(\chi_{\downarrow}=\chi_{\downarrow}(x)\) | A varying effective \(G\) or scalar--tensor sector, not Einstein gravity |
| Curvature-dependent modulus | Higher-curvature constitutive response is expected |
| State- or matter-dependent modulus | Equivalence-principle or universality violations requiring empirical bounds |
| Nonextensive dependence on the cut or its history | A nonlocal gravitational response rather than a local Einstein coefficient |
| Correct cosmological value but wrong local or wave-sector value | Cross-calibration failure; no universal \(G\) has been derived |

The current theory is strongest when these outcomes are allowed to falsify the weld. The target is not to rename the observed \(G\), but to make its coefficient the necessary output of a separately defined state geometry.
