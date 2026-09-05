# Compact SU(2) Fisher Calibration

A normalized compact-group readout can leave both marginal distributions exactly Haar while its prediction defect tends to zero. Its conditional Fisher tensor detects this loss of uncertainty and gives an asymptotically sharp response certificate. The example separates the geometry of a conditional relation from the geometry of either marginal alone.

**Status: [EXACT COMPACT CALIBRATION], not a four-dimensional gauge-theory construction or a physical mass prediction.** Use the full fixed-frame group carrier, or a holonomy carrier with a declared residual symmetry. An isolated tree link quotiented by independent endpoint gauge transformations has no nonconstant physical observables.

## The same Haar marginal with different prediction strength

Equip \(SU(2)\cong S^3\) with the unit round metric
\[
g(X,Y)=-\tfrac12\operatorname{ReTr}(XY).
\]
Let \(U\) have normalized Haar law and condition \(V\) by
\[
q_\kappa(V\mid U)=
\frac{\exp[\kappa\operatorname{ReTr}(V^*U)/2]}{N_\kappa},
\qquad N_\kappa=\frac{2I_1(\kappa)}{\kappa},\quad \kappa>0.
\tag{SC1}
\]
The law is symmetric in \(U,V\); both marginals are Haar. At \(\kappa=0\), use \(N_0=1\) and independence.

[[contemporary-puzzles/yang-mills-mass-gap/finite-spacing-transfer-and-bounded-flux-solder|The existing Wilson convolution calculation]] gives predictor eigenvalues
\[
p_j(\kappa)=\frac{I_{2j+1}(\kappa)}{I_1(\kappa)},
\qquad j=0,\tfrac12,1,\ldots.
\tag{SC2}
\]
They act on the full Peter--Weyl matrix-coefficient sectors, as well as on their character subspace. The strict decrease in Bessel order makes \(j=\tfrac12\) the largest nonconstant eigenvalue. With
\[
A_\kappa:=I_2(\kappa)/I_1(\kappa),
\]
the complete centered bridge response therefore has exact floor
\[
\boxed{\kappa_{\rm bridge}=1-A_\kappa^2.}
\tag{SC3}
\]
The Bessel order result is recorded in [[library/on-an-inequality-for-modified-bessel-functions/inq|Soni's inequality]] and also follows from the positive integral representation in [NIST DLMF 10.32.2](https://dlmf.nist.gov/10.32.E2). The marginal Haar gradient gap stays equal to three for every \(\kappa\).

## Compute the conditional metric directly

By invariance set \(V=I\) and write
\[
U=u_0I+i\sum_{j=1}^3u_j\sigma_j,\qquad
\sum_{\alpha=0}^3u_\alpha^2=1.
\]
Along the unit tangent \(i\sigma_j\) of the context \(V\), the normalized reverse score is \(\kappa u_j\). Its mean is zero by rotational symmetry. A Haar rotation in the \((u_0,u_j)\) plane has derivative \(R u_0=u_j\), \(R u_j=-u_0\). Integrating \(R(u_j e^{\kappa u_0})\) over the sphere gives
\[
\kappa\,\mathbb E_{\kappa}u_j^2
=\mathbb E_{\kappa}u_0
=\partial_\kappa\log N_\kappa=A_\kappa.
\tag{SC4}
\]
Off-diagonal second moments vanish. Thus the full conditional Fisher tensor is
\[
\boxed{I_V^{\leftarrow}=\kappa A_\kappa\,g.}
\tag{SC5}
\]
The forward tensor is the same by exchange symmetry. The inverse-Fisher form is the round Haar Dirichlet form divided by \(\kappa A_\kappa\). Since the unit \(S^3\) Laplacian has eigenvalues \(l(l+2)\), its first positive eigenvalue is three. Therefore
\[
\lambda_F=\frac3{\kappa A_\kappa},\qquad
\boxed{B\ge\frac3{3+\kappa A_\kappa}I}
\tag{SC6}
\]
on the centered carrier, by [[inq|conditional Fisher coercivity]]. The \(j(j+1)\) Casimir convention in the Wilson-spectrum note uses a different metric normalization: here \(l=2j\), hence \(l(l+2)=4j(j+1)\). The predictor eigenvalues themselves do not depend on that auxiliary metric.

At \(\kappa=0\), the Fisher tensor vanishes; use the background-metric branch and exact independence rather than divide by zero.

## Exact cancellation in the coarse Hessian

The actual coarse potential is constant. Nevertheless, the averaged conditional potential Hessian is not zero. For a unit context direction, \(X^2=-I\), so the first term of [[rg-covariance-residue/joint-fisher-response-of-normalized-gauge-blocking|the effective-Hessian identity]] equals \(\kappa A_\kappa\). Its reverse Fisher subtraction equals the same number:
\[
\operatorname{Hess}W
=\kappa A_\kappa g-I_V^{\leftarrow}=0.
\tag{SC7}
\]
Discarding the covariance term would incorrectly attribute a growing curvature to an unchanged marginal.

For small and large readout strength,
\[
\begin{aligned}
\kappa\downarrow0:\quad&
1-A_\kappa^2=1-\kappa^2/16+O(\kappa^4),\\
&\frac3{3+\kappa A_\kappa}
=1-\kappa^2/12+O(\kappa^4),\\[1mm]
\kappa\to\infty:\quad&
1-A_\kappa^2=\frac3\kappa+O(\kappa^{-2}),\\
&\frac3{3+\kappa A_\kappa}
=\frac3\kappa+O(\kappa^{-2}).
\end{aligned}
\tag{SC8}
\]
The certificate is asymptotically sharp as the readout becomes nearly deterministic. The coefficient three is the dimension of the declared tangent sphere; it is not a derived three-dimensional spacetime or a glueball energy.

No marginal state, auxiliary marginal gradient gap, or group compactness alone fixes this conditional response. Nor does an arbitrary readout strength define a clock. This example calibrates the metric and its loss of coercivity; it does not explain what selects \(\kappa\) in an actual physical construction.

[[receipts/relative_leakage_and_compact_gauge_receipt.py|The compact receipt]] compares Haar quadrature with the normalizer, Fisher tensor, representation coefficients and asymptotic response.
