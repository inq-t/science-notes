# Critical Scalar Kernel

For a dimensionless scalar on a homogeneous, isotropic three-dimensional wall, positivity and exact dilation covariance force the flat inverse-covariance shape $C|k|^3$. This is a clean scaling theorem; the curved $P_3$ operator, its positivity, the response coefficient, and departures from criticality require additional geometric or microscopic input.

## Flat scaling theorem

Let the quadratic form be

$$
\mathscr Q[\zeta]
=\frac12\int\frac{\mathrm d^3k}{(2\pi)^3}
\mathcal K_\zeta(k)|\zeta_{\mathbf k}|^2.
$$

Assume:

1. translation and rotation invariance in three flat dimensions;
2. a real, dimensionless weight-zero scalar $\zeta$;
3. a positive quadratic form after the constant mode is removed; and
4. exact dilation covariance with no intrinsic scale.

Under $x\mapsto\lambda x$,

$$
\zeta_{\mathbf k}\mapsto\lambda^3\zeta_{\lambda\mathbf k}.
$$

Invariance of $\mathscr Q$ requires

$$
\mathcal K_\zeta(\lambda k)=\lambda^3\mathcal K_\zeta(k).
$$

Isotropy and positivity therefore give

$$
\boxed{
\mathcal K_\zeta(k)=C|k|^3,
\qquad C\ge0.}
$$

When $C>0$, the covariance has the scale-invariant shape $k^{-3}$. This result fixes a universality class, not the coefficient $C$ and not the physical origin of the scalar.

## Curved representative

For a conformal three-manifold $(\Sigma,[g])$ that is the boundary of suitable Poincaré--Einstein or scattering data, fractional conformal geometry supplies a critical operator $P_3^g$. In flat space,

$$
P_3=(-\Delta)^{3/2}.
$$

On the round three-sphere of radius $R$,

$$
\boxed{
P_3Y_{\ell mn}
=R^{-3}\ell(\ell+1)(\ell+2)Y_{\ell mn},
\qquad \ell\ge1.}
$$

The constant mode is in the kernel, matching the homogeneous quotient. The scattering construction and its conformal covariance are standard results of [[causal-wall-spectral-theory/sources/papers/0109089-graham-zworski-scattering-matrix-conformal-geometry.pdf|Graham--Zworski]] and the fractional-GJMS literature, including [[causal-wall-spectral-theory/sources/papers/1003.0398-chang-gonzalez-fractional-laplacian-conformal-geometry.pdf|Chang--González]]. The extension, energy, and positivity hypotheses relevant to a critical endpoint are developed further by [[causal-wall-spectral-theory/sources/papers/1012.0579-gonzalez-qing-fractional-conformal-laplacians-yamabe.pdf|González--Qing]] and [[causal-wall-spectral-theory/sources/papers/1406.1846-case-chang-fractional-gjms-operators.pdf|Case--Chang]]; they are not automatic consequences of conformal covariance.

The qualifications are structural:

- $P_3^g$ depends on filling or scattering data; flat symmetry does not select a unique nonlocal operator on every curved conformal manifold;
- different admissible fillings need not give identical global operators;
- self-adjoint domain, kernel, and positivity must be checked for the selected geometry;
- if the coefficient runs, the curved object cannot simply be written $C(k)P_3$ because a generic curved wall has no global momentum $k$; a covariant spectral-calculus definition such as a function of $P_3$ is needed.

The safe claim is therefore that $P_3$ is a natural conditional curved representative of the flat critical shape, not a universally unique positive wall precision.

## Fixed-point degeneracy

At an improved conformal fixed point, away from boundary, defect, virial-current, and anomaly contributions,

$$
T^i{}_i=0.
$$

Along a controlled deformation one may have schematically

$$
T^i{}_i=\beta^I\mathcal O_I
$$

up to the omitted terms, and hence

$$
\langle TT\rangle
\sim\beta^I\beta^J
\langle\mathcal O_I\mathcal O_J\rangle.
$$

If the operator correlators and mixing remain regular, the spin-zero response and scalar precision tend to zero:

$$
c^{(0)}\longrightarrow0,
\qquad
\mathcal K_\zeta\longrightarrow0.
$$

The inverse cannot then be formed on that direction. The correct operation is to quotient the null or gauge-redundant direction before inversion. A formal divergence of $\mathcal K_\zeta^{-1}$ at the exact fixed point is not a prediction of infinite observable structure.

Near, but not at, the fixed point one may write schematically

$$
\mathcal K_\zeta\simeq C\,P_3,
\qquad
C=\frac{\pi^2}{8}c^{(0)}.
$$

Two notions must remain separate:

$$
\left|\frac{\mathrm d\ln c^{(0)}}{\mathrm d\ln k}\right|\ll1
\quad\text{means slowly varying shape,}
$$

whereas

$$
\mathcal I_\zeta\gg1
\quad\text{means small scalar power.}
$$

The observed normalization corresponds to a large $c^{(0)}$ in the registered convention even though $c^{(0)}$ vanishes at the exact fixed point. This is not an algebraic contradiction: a microscopic theory could contain a large operator normalization multiplied by small beta functions. The required double scaling has not been derived, so “near critical” currently refers primarily to slow running, not to a computed distance from the fixed point.

## Tilt and running

From [[spectral-dictionary|the scalar dictionary]],

$$
\Delta_\zeta^2(k)=\mathcal I_\zeta(k)^{-1}.
$$

Therefore

$$
\boxed{
n_s(k)-1
=-\frac{\mathrm d\ln\mathcal I_\zeta}{\mathrm d\ln k}
=-\frac{\mathrm d\ln c^{(0)}}{\mathrm d\ln k},}
$$

and

$$
\boxed{
\alpha_s(k)
:=\frac{\mathrm dn_s}{\mathrm d\ln k}
=-\frac{\mathrm d^2\ln\mathcal I_\zeta}
{\mathrm d(\ln k)^2}.}
$$

These are exact logarithmic identities after the dictionary has been granted.

The minimal power-law member assumes

$$
c^{(0)}(k)
=c_*^{(0)}\left(\frac{k}{k_*}\right)^\delta,
\qquad
\delta=1-n_s=\text{constant}.
$$

It follows that

$$
\Delta_\zeta^2(k)
=A_s\left(\frac{k}{k_*}\right)^{-\delta},
\qquad
\boxed{\alpha_s=0.}
$$

Zero running is exact **by definition of this member**. The broader spectral formulation supplies no universal estimate $|\alpha_s|\lesssim\delta^2$ without a beta function or another microscopic flow law.

The [[causal-wall-spectral-theory/sources/papers/2503.14454-act-dr6-extended-cosmological-models.pdf|ACT DR6 extended-model analysis]] reports $\alpha_s=0.0062\pm0.0052$ for its P--ACT--LB combination, consistent with zero. The exact released [[causal-wall-spectral-theory/sources/data/act-dr6/p-actlite-l-b_nrun_camb/p-actlite-l-b_nrun_camb/p-actlite-l-b_nrun_camb.input.yaml|run definition]] and [[causal-wall-spectral-theory/sources/data/act-dr6/p-actlite-l-b_nrun_camb.tar.gz|posterior archive]] are mirrored locally; the label denotes a joint Planck-cut + ACT-lite + lensing + BAO combination, not ACT alone. Differences between best-fit $n_s$ values from distinct, overlapping likelihood combinations are not themselves an estimator of running. A robust nonzero running would reject the constant-exponent member while leaving the unrestricted positive-function formulation intact.

## Scope of falsification

- Failure of the $|k|^3$ leading shape under the stated exact symmetries rejects the critical flat member.
- Failure to find an admissible positive $P_3$ construction rejects a proposed curved realization, not the flat theorem.
- Nonzero running rejects the constant-exponent member, not the general function $c^{(0)}(k)$.
- A microscopic wall calculation that yields a different critical kernel rejects the causal-wall identification.

Because an arbitrary positive $c^{(0)}(k)$ can reproduce an arbitrary positive scalar power spectrum, the unrestricted spectral typing is not by itself a sharply predictive empirical theory.
