# The Singlet Response-Completion Test

A single positive hidden scalar can repair exactly one positive rank-one mismatch between the common response matrix and a universal gravitational response. This is the precise algebraic content behind the suggestion that the extra singlet in twisted spectral geometry may complete a missing coupling relation. The criterion is necessary and sufficient for a fixed target; it also gives a clean falsifier when the mismatch has higher rank or the wrong sign.

## Universal response is an eigenvalue condition

Let \(W\) be the physical common-response matrix on a finite-dimensional tangent sector, and let \(K>0\) be a unit-normalized gravitational canonical-energy matrix pulled back to the same tangent space. A universal coupling means

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

Let \(x\) denote the retained response coordinates and \(s\) one hidden scalar. Consider

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
$$

then any \(L>0\) and

$$
b=\sqrt{L\lambda}\,u
$$

give the required completion.

This is the **[EXACT RANK-ONE COMPLETION THEOREM]**.

## What the Connes singlet would have to do

[[spectral-wall-descent/twist-fixed-point-wall|The twisted fixed-point wall]] supplies a twist-odd Majorana singlet and an observable spectral stiffness. [[spectral-wall-descent/response-determinant|The response--determinant bridge]] explains how its hidden operator could affect both response and the observable action.

For that singlet to complete the gravitational coupling, one must calculate on the same physical tangent space:

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

The published fact that a singlet improves the Higgs mass and vacuum stability does not establish this identity. The theorem says why one singlet is structurally germane: it can impose one missing response relation. It also says exactly when it cannot.

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

The candidate closure equation is therefore

$$
\boxed{
\mathcal R_{\mathrm{eff}}
=Z_{\mathrm{spec}}\mathbf1.}
$$

This would weld the common response to the observable spectral Einstein coefficient. It would still not numerically derive \(G\), because \(f_2\), \(\Lambda\), and \(c\) remain inputs unless the upstream algebra fixes them independently.

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

[[spectral-wall-descent/receipts/verify-spectral-wall.py|The finite receipt]] verifies the rank-one construction and the repeated generalized eigenvalue condition in a non-diagonal example.
