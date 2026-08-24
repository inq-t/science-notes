# The Singlet Response-Completion Test

A single positive hidden scalar can repair exactly one positive rank-one mismatch between the common response matrix and a universal gravitational response. This is the precise algebraic content behind the suggestion that the extra singlet in twisted spectral geometry may complete a missing coupling relation. The criterion is necessary and sufficient for a fixed target; it also gives a clean falsifier when the mismatch has higher rank or the wrong sign.

## Universal response is an eigenvalue condition

Let \(W=W^T\) be the real symmetric physical common-response matrix on a finite-dimensional, nondegenerate gauge-quotiented tangent sector, and let \(K=K^T>0\) be a unit-normalized gravitational canonical-energy matrix pulled back to that same sector. A universal coupling means

$$
\boxed{W=Z_gK}
$$

for one scalar \(Z_g>0\), not merely on one preferred direction.

Define the basis-independent response ratio

$$
\boxed{
\mathcal R
:=K^{-1/2}WK^{-1/2}.}
$$

Then universal coupling holds if and only if

$$
\boxed{\mathcal R=Z_g\mathbf1.}
$$

Equivalently, every generalized eigenvalue of

$$
Wv=\lambda Kv
$$

must be the same. If the tangent dimension is \(m\), equality implies

$$
Z_g
=\left(\frac{\det W}{\det K}\right)^{1/m},
$$

but the determinant equation alone is not sufficient: matrices with unequal eigenvalues can have the same determinant.

On a one-dimensional tangent, some ratio \(Z_g\) always exists. A one-channel match is therefore calibration, not a universality test. The first nontrivial test requires at least two independent physical tangents, such as the homogeneous direction and an allowed mean-zero or tensor response direction.

## One positive singlet

Let \(W_0=W_0^T\) and let \(x\) denote the retained real response coordinates and \(s\) one hidden real scalar. Consider

$$
\mathscr I(x,s)
=\frac12x^TW_0x
+x^Tbs
+\frac12Ls^2,
\qquad
L>0.
$$

Eliminating \(s\) gives

$$
s_*=-L^{-1}b^Tx,
$$

and

$$
\boxed{
W_{\mathrm{eff}}
=W_0-\frac{bb^T}{L}.}
$$

Fix a target \(Z_gK\) and put

$$
\Delta:=W_0-Z_gK.
$$

There exists a positive stiffness \(L\) and a coupling vector \(b\) for which

$$
W_{\mathrm{eff}}=Z_gK
$$

if and only if

$$
\boxed{
\Delta\succeq0,
\qquad
\operatorname{rank}\Delta\leq1.}
$$

Indeed, necessity follows because \(bb^T/L\) is positive semidefinite of rank at most one. Conversely, if

$$
\Delta=\lambda uu^T,
\qquad
\lambda\geq0,
\qquad
\lVert u\rVert=1,
$$

then any \(L>0\) and

$$
b=\sqrt{L\lambda}\,u
$$

give the required completion.

This is the **[EXACT RANK-ONE COMPLETION THEOREM]**.

## What the Connes singlet would have to do

[[spectral-wall-descent/twist-fixed-point-wall|The twisted fixed-point wall]] supplies a twist-odd Majorana singlet and an observable spectral stiffness. [[spectral-wall-descent/response-determinant|The response--determinant bridge]] explains how its hidden operator could affect both response and the observable action.

No such common-tangent response block has yet been extracted from the Connes model. For that singlet to complete the gravitational coupling, one must calculate on the same physical tangent space:

$$
W_0,
\qquad
K,
\qquad
L_\sigma,
\qquad
b_\sigma,
$$

and verify

$$
W_0-Z_gK
=\frac{b_\sigma b_\sigma^T}{L_\sigma}.
$$

The published Higgs--singlet mixing matrix is not automatically the displayed response block, and the fact that a singlet improves the Higgs mass and vacuum stability does not establish this identity. The theorem says only what one real hidden scalar could cancel: a positive mismatch of rank at most one. It also says exactly when it cannot.

If the defect is

- indefinite, a stable eliminated scalar has the wrong sign;
- positive but rank \(r>1\), at least \(r\) independent positive hidden directions are required; or
- supported in a gauge/null direction, the quotient must be taken before the test.

## The observable spectral coefficient

In the noncommutative Standard Model normalization,

$$
\kappa_0^{-2}
=\frac{96f_2\Lambda^2-f_0c}{12\pi^2},
$$

so the coefficient of \(\int R\) is

$$
Z_{\mathrm{spec}}
=\frac{1}{2\kappa_0^2}
=\frac{96f_2\Lambda^2-f_0c}{24\pi^2}.
$$

Here \(Z_{\mathrm{spec}}\) is a bare cutoff-scale coefficient. It can be identified with a common-response target only if \(K\) is the gauge-quotiented second variation or canonical energy of the unit-coefficient Einstein--Hilbert functional in the same signature, background, boundary convention, and field normalization. Subject to that convention weld, the candidate closure equation is

$$
\boxed{
\mathcal R_{\mathrm{eff}}
=Z_{\mathrm{spec}}\mathbf1.}
$$

This would weld the common response to the bare observable spectral Einstein coefficient. It would still not numerically derive the infrared \(G\), because \(f_2\), \(\Lambda\), and \(c\) remain inputs unless the upstream algebra fixes them independently, and renormalization-group transport remains to be controlled.

## Test protocol

1. Form the physical quotient and choose at least two independent tangents.
2. Normalize \(K\) with the gravitational coefficient removed.
3. Compute \(W_0\) from one transported BKM or descent-cost construction.
4. Keep \(Z_g\) symbolic and inspect the generalized eigenvalues of \((W_0,K)\).
5. Compute the actual singlet coupling and stiffness rather than fitting \(b\) and \(L\).
6. Apply the rank and sign criterion.
7. Recompute the generalized spectrum after elimination.
8. Test the same \(Z_g\) in homogeneous, scalar, tensor, and local-gravity sectors.

The criterion concerns a quadratic response at one reference. Higher derivatives, covariance, locality, renormalization-group transport, and persistent records remain separate obligations.

[[spectral-wall-descent/receipts/verify-spectral-wall.py|The finite receipt]] constructs \(b\) from a chosen rank-one mismatch and checks the sufficiency direction plus the repeated generalized eigenvalue condition in a non-diagonal example. It does not extract or test the Connes singlet.
